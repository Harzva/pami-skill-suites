#!/usr/bin/env python3
"""Classify official and repository sources into trust tiers.

Offline-safe by default: this script classifies provenance from local registries and
reports. It does not certify live URL health.
"""
from pathlib import Path
import json, datetime, sys
try:
    import yaml
except Exception:
    yaml = None
ROOT=Path(__file__).resolve().parents[1]
TODAY=datetime.date.today().isoformat()
TIERS={
 'publisher-official': {'priority':10,'description':'Publisher-wide official source such as author center, policy, template, publishing agreement, copyright/license, open access, AI, data/code, or permissions page.'},
 'journal-official': {'priority':9,'description':'Target-journal homepage, Guide for Authors / Information for Authors, scope page, journal page, or submission instructions.'},
 'society-official': {'priority':8,'description':'Society or owner page associated with a journal.'},
 'repository-best-practice': {'priority':4,'description':'Unofficial skill-suite routing, output contract, context-safety, and reviewer-risk guidance.'},
 'template-paper-observation': {'priority':3,'description':'Structural observation from lawful paper-template corpus. Never copy text/figures/tables/captions.'},
 'unverified-candidate': {'priority':1,'description':'Candidate or incomplete source that requires human review before use for real submission advice.'},
}
SOCIETY_DOMAINS=['computer.org','embs.org','signalprocessingsociety.org','ieee-cas.org','itsoc.org','cis.ieee.org','comsoc.org','grss-ieee.org','ieee-ras.org','ieeeaccess.ieee.org']

def load_json(path, default):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default

def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

def dump_yaml(path, data):
    if yaml:
        path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding='utf-8')
    else:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

def classify(rec, publisher):
    scope=str(rec.get('scope','')).lower(); field=str(rec.get('field','')).lower(); tier=str(rec.get('source_tier','')).lower(); url=str(rec.get('url','')).lower()
    if rec.get('maturity_level') in {'L0','L1'} or rec.get('entry_type')=='candidate': return 'unverified-candidate'
    if 'template' in scope or rec.get('source_type') in {'paper-template','template-paper','paper-card'}: return 'template-paper-observation'
    if 'repository' in tier or scope.startswith('repository'): return 'repository-best-practice'
    if any(d in url for d in SOCIETY_DOMAINS) and 'ieeeauthorcenter' not in url and 'open.ieee.org' not in url: return 'society-official'
    if 'journal' in tier or field in {'journal_homepage','homepage','xplore','science_direct','scope','guide_for_authors'}: return 'journal-official'
    if publisher.lower().startswith('elsevier') and field in {'author_instructions','guide_for_authors','journal_homepage'}: return 'journal-official'
    if 'publisher' in tier or scope == 'publisher_common_source': return 'publisher-official'
    return 'repository-best-practice'

def iter_records():
    publisher='IEEE' if ROOT.name.startswith('ieee') else 'Elsevier'
    live=load_json(ROOT/'resources/live_source_check_matrix.json', {'records':[]})
    for r in live.get('records',[]):
        rr=dict(r); rr['record_origin']='live_source_check_matrix'; rr['source_trust_tier']=classify(rr,publisher); yield rr
    for field,path,desc in [
        ('context_safe_architecture','docs/context-safety.html','Context-safe compact architecture policy'),
        ('routing_policy','skills/%s-skill-suite/manifest.yaml' % ('ieee' if publisher=='IEEE' else 'elsevier'),'Suite routing manifest'),
        ('evaluation_harness','evals/README.md','Static benchmark and sample-output evaluation harness'),
        ('preset_workflows','presets/','Opt-in discipline-specific preset router policy'),
    ]:
        yield {'scope':'repository_best_practice','owner':ROOT.name,'field':field,'url':path,'description':desc,'record_origin':'repository_policy','source_trust_tier':'repository-best-practice','needs_reverification':False,'mutable_publication_detail':False,'age_bucket':'not-applicable','maintenance_action':'review during release updates'}
    corpus=load_json(ROOT/'paper_templates/corpus_manifest.json', {'entries':[]})
    for e in corpus.get('entries',[]):
        yield {'scope':'template_paper_observation','owner':e.get('journal','paper-corpus'),'field':'paper_template','url':e.get('source_url') or e.get('local_pdf_path') or '', 'paper_id':e.get('id'), 'title':e.get('title'), 'license':e.get('license'), 'record_origin':'paper_templates/corpus_manifest.json','source_trust_tier':'template-paper-observation','needs_reverification':True,'mutable_publication_detail':False,'age_bucket':'unchecked','maintenance_action':'re-check source/license before redistribution; use only for structure mining'}
    packs=ROOT/'expansion_packs'
    if packs.exists() and yaml:
        for pack in sorted(p for p in packs.iterdir() if p.is_dir()):
            fp=pack/'journals.yaml'
            if not fp.exists(): continue
            data=yaml.safe_load(fp.read_text(encoding='utf-8')) or {}
            for j in data.get('journals',[]) or []:
                if j.get('maturity_level') in {'L0','L1'} or j.get('entry_type') in {'candidate','listed-only'}:
                    yield {'scope':'expansion_pack_candidate','owner':data.get('pack_id') or pack.name,'field':'candidate_journal','url':j.get('journal_homepage') or j.get('homepage') or '', 'journal_id':j.get('id'), 'title':j.get('title'), 'maturity_level':j.get('maturity_level'), 'entry_type':j.get('entry_type'), 'record_origin':f'expansion_packs/{pack.name}/journals.yaml','source_trust_tier':'unverified-candidate','needs_reverification':True,'mutable_publication_detail':True,'age_bucket':'unchecked','maintenance_action':'promote through human review queue before using for real submission advice'}

def main():
    records=list(iter_records())
    counts={k:0 for k in TIERS}
    for r in records: counts[r.get('source_trust_tier','repository-best-practice')]=counts.get(r.get('source_trust_tier','repository-best-practice'),0)+1
    out={'schema_version':'1.0','release_version':'1.7.0','generated_at':TODAY,'repository':ROOT.name,'publisher_family':'IEEE' if ROOT.name.startswith('ieee') else 'Elsevier','offline_safe_policy':'Trust tiers classify provenance and review priority. They do not certify live URL health unless live check scripts were run in networked mode.','tiers':TIERS,'tier_priority_order':list(TIERS.keys()),'summary':{'records':len(records),'tier_counts':counts,'records_needing_reverification':sum(1 for r in records if r.get('needs_reverification')),'human_review_required':sum(1 for r in records if r.get('needs_reverification') or r.get('source_trust_tier')=='unverified-candidate')},'records':records}
    dump(ROOT/'resources/source_trust_tiers.json', out); dump_yaml(ROOT/'resources/source_trust_tiers.yaml', out)
    print(json.dumps(out['summary'], indent=2, ensure_ascii=False))
if __name__=='__main__': main()
