#!/usr/bin/env python3
"""Build the human review queue from trust tiers, official-source registry, and expansion packs."""
from pathlib import Path
import json, datetime, sys
try:
    import yaml
except Exception:
    yaml=None
ROOT=Path(__file__).resolve().parents[1]
TODAY=datetime.date.today().isoformat()

def load_json(path, default): return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default

def dump_json(path, data): path.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
def dump_yaml(path, data):
    if yaml: path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding='utf-8')
    else: path.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

def expansion_journals():
    packs=ROOT/'expansion_packs'
    if not (packs.exists() and yaml): return []
    out=[]
    for pack in sorted(p for p in packs.iterdir() if p.is_dir()):
        fp=pack/'journals.yaml'
        if not fp.exists(): continue
        data=yaml.safe_load(fp.read_text(encoding='utf-8')) or {}
        for j in data.get('journals',[]) or []:
            jj=dict(j); jj['pack_id']=data.get('pack_id') or pack.name; out.append(jj)
    return out

def main():
    trust=load_json(ROOT/'resources/source_trust_tiers.json', {'records':[]})
    registry=load_json(ROOT/'resources/official_source_registry.json', {'journals':[]})
    publisher='IEEE' if ROOT.name.startswith('ieee') else 'Elsevier'
    cats={k:[] for k in ['high-risk mutable links','stale official links','missing author-instruction links','missing copyright/license links','missing AI disclosure links','L0/L1 expansion-pack candidates']}
    for r in trust.get('records',[]):
        if r.get('source_trust_tier') in {'publisher-official','journal-official','society-official'}:
            if r.get('mutable_publication_detail') and r.get('needs_reverification'): cats['high-risk mutable links'].append(r)
            if r.get('age_bucket')=='stale': cats['stale official links'].append(r)
    for j in registry.get('journals',[]) or []:
        fields=j.get('fields',{}) or {}; base={'journal_id':j.get('id'),'title':j.get('title') or j.get('id'),'path':j.get('path'),'publisher':publisher,'source_trust_tier':'unverified-candidate','needs_reverification':True}
        if not (fields.get('author_instructions') or fields.get('guide_for_authors')): cats['missing author-instruction links'].append({**base,'missing_field':'author_instructions or guide_for_authors','maintenance_action':'add journal-specific author instructions / Guide for Authors URL'})
        if not (fields.get('copyright_license') or fields.get('publishing_agreement')): cats['missing copyright/license links'].append({**base,'missing_field':'copyright_license or publishing_agreement','maintenance_action':'add official copyright/license or publishing agreement URL'})
        if not fields.get('ai_disclosure_policy'): cats['missing AI disclosure links'].append({**base,'missing_field':'ai_disclosure_policy','maintenance_action':'add publisher/journal AI disclosure policy URL or mark not verified'})
    for j in expansion_journals():
        if j.get('maturity_level') in {'L0','L1'}:
            cats['L0/L1 expansion-pack candidates'].append({'pack_id':j.get('pack_id'),'journal_id':j.get('id'),'title':j.get('title'),'maturity_level':j.get('maturity_level'),'entry_type':j.get('entry_type'),'source_trust_tier':'unverified-candidate','needs_reverification':True,'maintenance_action':'promote only after full official-source matrix, source-refresh metadata, and live verification warnings are added; do not add as default top-level skill'})
    items=[]
    for cat,vals in cats.items():
        for idx,item in enumerate(vals,1):
            priority='P0' if cat in {'missing copyright/license links','missing AI disclosure links'} else ('P1' if cat in {'high-risk mutable links','L0/L1 expansion-pack candidates'} else 'P2')
            items.append({'category':cat,'priority':priority,'item_index':idx, **item})
    q={'schema_version':'1.0','release_version':'1.7.0','generated_at':TODAY,'repository':ROOT.name,'publisher_family':publisher,'offline_safe_policy':'Human-review queue is generated from cached metadata and dry-run source checks. It identifies review needs; it does not claim live URL health.','review_categories':{k:{'count':len(v)} for k,v in cats.items()},'summary':{'total_queue_items':len(items),'P0':sum(1 for x in items if x['priority']=='P0'),'P1':sum(1 for x in items if x['priority']=='P1'),'P2':sum(1 for x in items if x['priority']=='P2')},'queue':items}
    dump_json(ROOT/'resources/human_review_queue.json', q); dump_yaml(ROOT/'resources/human_review_queue.yaml', q)
    report={'schema_version':'1.0','release_version':'1.7.0','generated_at':TODAY,'repository':ROOT.name,'summary':q['summary'],'source_trust_summary':trust.get('summary',{}),'recommended_next_actions':['Run live source checks in a networked environment.','Review P0 missing copyright/license or AI-disclosure records first.','Promote L0/L1 expansion candidates only through staged fragment workflow.','Do not use unverified candidates for real submission advice.'],'reports':{'source_trust_tiers':'resources/source_trust_tiers.json','human_review_queue':'resources/human_review_queue.json','release_health_dashboard':'resources/release_health_dashboard.json'}}
    dump_json(ROOT/'resources/source_review_report.json', report); dump_yaml(ROOT/'resources/source_review_report.yaml', report)
    print(json.dumps(q['summary'], indent=2, ensure_ascii=False))
if __name__=='__main__': main()
