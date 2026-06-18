#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml, re, subprocess
ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / 'evals'
checks=[]; errors=[]
def add(name, passed, details=None):
    checks.append({'name':name,'passed':bool(passed),'details':details or {}})
    if not passed: errors.append(name)
# Validate eval files first
try:
    proc=subprocess.run([sys.executable, str(ROOT/'scripts'/'validate_evals.py')], cwd=ROOT, text=True, capture_output=True, timeout=60)
    add('validate_evals.py', proc.returncode==0, {'stdout_tail':proc.stdout[-800:], 'stderr_tail':proc.stderr[-400:]})
except Exception as e:
    add('validate_evals.py', False, {'error':str(e)})
# Static scoring by required section coverage
scores=[]
for task_file in sorted((EVALS/'tasks').glob('*.yaml')):
    data=yaml.safe_load(task_file.read_text(encoding='utf-8')) or {}
    sample=ROOT/data.get('sample_output','')
    txt=sample.read_text(encoding='utf-8', errors='ignore') if sample.exists() else ''
    requirements=['Selected skills/modules','Official-source warning','Copyright-safe paper-mining warning','Reviewer-risk checklist','Structured output contract']
    hit=sum(1 for r in requirements if r in txt)
    score=round(hit/len(requirements)*10,2)
    scores.append({'task_id':data.get('task_id',task_file.stem),'score':score,'required_modules':data.get('required_modules',[])})
add('sample_output_static_scores', all(s['score']>=10 for s in scores), {'scores':scores})
# Route smoke check through manifest aliases where possible
for suite in (ROOT/'skills').glob('*skill-suite'):
    manifest=suite/'manifest.yaml'
    if not manifest.exists(): continue
    data=yaml.safe_load(manifest.read_text(encoding='utf-8')) or {}
    q='abstract related work figure caption table reviewer response submission package official source paper mining'
    selected=[]
    for section in ['components','submission','journals']:
        for name,item in data.get(section,{}).items():
            if any(a and a.lower() in q for a in item.get('aliases',[])):
                selected.append(f'{section}:{name}')
    add(f'route_coverage:{suite.name}', len(selected)>=5, {'selected':selected[:20]})
summary={'benchmark_version':'1.2.0','checks':checks,'errors':errors,'passed':not errors}
print(json.dumps(summary, indent=2, ensure_ascii=False))
if errors: sys.exit(1)
