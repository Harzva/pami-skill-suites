#!/usr/bin/env python3
from pathlib import Path
import json, yaml, sys
ROOT=Path(__file__).resolve().parents[1]
levels={'L0':'listed only','L1':'official homepage + author instructions','L2':'full official source matrix','L3':'source-refresh metadata + live-check support','L4':'paper-template card + evaluation task'}
rows=[]; packs=[]; counts={k:0 for k in levels}; errs=[]
base=ROOT/'expansion_packs'
if not base.exists(): errs.append('missing expansion_packs')
for p in sorted(base.iterdir() if base.exists() else []):
    if not p.is_dir(): continue
    data=yaml.safe_load((p/'journals.yaml').read_text()) or {}
    pc={k:0 for k in levels}
    for j in data.get('journals',[]):
        lvl=j.get('maturity_level')
        if lvl not in levels: errs.append(f'{p.name}/{j.get("id")}: invalid level {lvl}'); continue
        pc[lvl]+=1; counts[lvl]+=1
        rows.append({'pack_id':p.name,'journal_id':j.get('id'),'title':j.get('title'),'entry_type':j.get('entry_type'),'maturity_level':lvl,'maturity_label':levels[lvl],'needs_reverification':j.get('needs_reverification',True),'source_status':j.get('source_status'),'journal_fragment':j.get('journal_fragment'),'paper_template_cards':j.get('paper_template_cards',[]),'source_quality_score':j.get('source_quality_score'),'promotion_readiness':j.get('promotion_readiness')})
    packs.append({'pack_id':p.name,'title':data.get('title',p.name),'journal_entries':len(data.get('journals',[])),'maturity_counts':pc,'hardening':data.get('hardening',{})})
obj={'schema_version':'1.3.0','release_version':(ROOT/'VERSION').read_text().strip() if (ROOT/'VERSION').exists() else '1.3.0','publisher_family':'IEEE' if 'ieee' in ROOT.name.lower() else 'Elsevier','context_policy':'Expansion packs are opt-in and never increase default skills/ listing.','maturity_levels':levels,'summary':{'expansion_packs':len(packs),'journal_entries':len(rows),'unique_journals':len({row['journal_id'] for row in rows}),'maturity_counts':counts,'source_quality_scoring':'enabled','promotion_workflow':'staged only'},'packs':packs,'journals':rows}
(ROOT/'resources').mkdir(exist_ok=True)
(ROOT/'resources/journal_coverage_dashboard.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
(ROOT/'resources/journal_coverage_dashboard.yaml').write_text(yaml.safe_dump(obj,sort_keys=False,allow_unicode=True,width=120))
print(json.dumps({'dashboard':'resources/journal_coverage_dashboard.json','packs':len(packs),'journal_entries':len(rows),'errors':errs}, indent=2))
if errs: sys.exit(1)
