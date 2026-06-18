#!/usr/bin/env python3
from pathlib import Path
import json, yaml, sys
ROOT=Path(__file__).resolve().parents[1]
LEVEL_BASE={'L0':5,'L1':20,'L2':45,'L3':65,'L4':78}
def score(j):
    official=j.get('official_sources') or {}; missing=official.get('missing_fields') or []
    s=LEVEL_BASE.get(j.get('maturity_level','L0'),0)
    if official.get('matrix_status')=='full matrix populated': s+=8
    if 'source_status' in j and 'needs_reverification' in j: s+=6
    if not missing: s+=3
    if j.get('entry_type')=='imported-fragment' and j.get('journal_fragment'): s+=4
    if j.get('paper_template_cards'): s+=5
    if j.get('evaluation_tasks'): s+=4
    if j.get('source_status') in ['live-checked-ok','healthy']: s+=10
    s=min(s,100)
    band='A' if s>=90 else 'B' if s>=75 else 'C' if s>=55 else 'D' if s>=30 else 'E'
    return {'score':s,'band':band,'live_check_required':True,'caveat':'Static score only. Run check_official_links_live.py --live before real submission advice.'}
all_rows=[]; errs=[]; pack_rows=[]
for pack in sorted((ROOT/'expansion_packs').iterdir() if (ROOT/'expansion_packs').exists() else []):
    if not pack.is_dir(): continue
    data=yaml.safe_load((pack/'journals.yaml').read_text()) or {}
    rows=[]; counts={'L0':0,'L1':0,'L2':0,'L3':0,'L4':0}
    for j in data.get('journals',[]):
        sc=score(j); j['source_quality_score']=sc
        counts[j.get('maturity_level','L0')]=counts.get(j.get('maturity_level','L0'),0)+1
        row={'pack_id':pack.name,'journal_id':j.get('id'),'title':j.get('title'),'maturity_level':j.get('maturity_level'),'score':sc['score'],'band':sc['band'],'needs_reverification':j.get('needs_reverification',True)}
        rows.append(row); all_rows.append(row)
    (pack/'journals.yaml').write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True,width=120))
    report={'schema_version':'1.3.0','pack_id':pack.name,'summary':{'journal_entries':len(rows),'average_source_quality_score':round(sum(r['score'] for r in rows)/len(rows),2) if rows else 0,'maturity_counts':counts,'live_verification_required':True},'journals':rows}
    (pack/'source_quality_report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    pack_rows.append({'pack_id':pack.name,**report['summary']})
obj={'schema_version':'1.3.0','release_version':(ROOT/'VERSION').read_text().strip() if (ROOT/'VERSION').exists() else '1.3.0','summary':{'entries':len(all_rows),'average_score':round(sum(r['score'] for r in all_rows)/len(all_rows),2) if all_rows else 0,'bands':{b:sum(1 for r in all_rows if r['band']==b) for b in ['A','B','C','D','E']},'l0_candidates':sum(1 for r in all_rows if r['maturity_level']=='L0')},'scores':all_rows}
(ROOT/'resources').mkdir(exist_ok=True)
(ROOT/'resources/source_quality_scores.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
(ROOT/'resources/source_quality_scores.yaml').write_text(yaml.safe_dump(obj,sort_keys=False,allow_unicode=True,width=120))
print(json.dumps({'source_quality_scores':'resources/source_quality_scores.json','entries':len(all_rows),'errors':errs},indent=2))
if errs: sys.exit(1)
