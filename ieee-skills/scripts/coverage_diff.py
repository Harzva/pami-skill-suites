#!/usr/bin/env python3
from pathlib import Path
import json, yaml, sys
ROOT=Path(__file__).resolve().parents[1]
res=ROOT/'resources'
base_path=res/'journal_coverage_dashboard_v1.2.0_baseline.json'
cur_path=res/'journal_coverage_dashboard.json'
if not cur_path.exists():
    import subprocess
    subprocess.check_call([sys.executable, str(ROOT/'scripts/coverage_dashboard.py')])
cur=json.loads(cur_path.read_text())
base=json.loads(base_path.read_text()) if base_path.exists() else cur

def counts(obj): return obj.get('summary',{}).get('maturity_counts',{})
def entries(obj): return { (j.get('pack_id'), j.get('journal_id')): j for j in obj.get('journals',[]) }
be,ce=entries(base),entries(cur)
added=[{'pack_id':k[0],'journal_id':k[1]} for k in sorted(set(ce)-set(be))]
removed=[{'pack_id':k[0],'journal_id':k[1]} for k in sorted(set(be)-set(ce))]
changed=[]
for k in sorted(set(be)&set(ce)):
    if be[k].get('maturity_level') != ce[k].get('maturity_level'):
        changed.append({'pack_id':k[0],'journal_id':k[1],'from':be[k].get('maturity_level'),'to':ce[k].get('maturity_level')})
obj={'schema_version':'1.3.0','baseline_release':'1.2.0','current_release':(ROOT/'VERSION').read_text().strip() if (ROOT/'VERSION').exists() else '1.3.0','summary':{'added_entries':len(added),'removed_entries':len(removed),'maturity_changes':len(changed),'baseline_maturity_counts':counts(base),'current_maturity_counts':counts(cur),'context_policy':'Expansion packs remain opt-in and do not add default top-level skills.'},'added_entries':added,'removed_entries':removed,'maturity_changes':changed,'notes':['v1.3.0 focuses on hardening, scoring, promotion workflow, and pack evaluation placeholders; coverage entries may remain unchanged.']}
(res/'coverage_diff_report.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
(res/'coverage_diff_report.yaml').write_text(yaml.safe_dump(obj,sort_keys=False,allow_unicode=True,width=120))
print(json.dumps({'coverage_diff_report':'resources/coverage_diff_report.json','added':len(added),'removed':len(removed),'maturity_changes':len(changed)},indent=2))
