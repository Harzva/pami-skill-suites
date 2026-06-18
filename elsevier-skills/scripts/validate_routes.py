#!/usr/bin/env python3
from pathlib import Path
import sys, yaml, json, re
ROOT=Path(__file__).resolve().parents[1]
errs=[]; samples=[]
for suite in [p for p in (ROOT/'skills').iterdir() if p.is_dir() and p.name.endswith('skill-suite')]:
    data=yaml.safe_load((suite/'manifest.yaml').read_text(encoding='utf-8'))
    q='pami pattern recognition related work table caption response author agreement highlights graphical abstract'
    selected=[]
    for section in ['journals','components','submission']:
        for name,item in data.get(section,{}).items():
            aliases=item.get('aliases',[])
            if any(a and a.lower() in q for a in aliases):
                selected.append(f'{section}:{name}')
    if len(data.get('journals',{})) < 3: errs.append(f'{suite.name}: too few journals')
    if len(data.get('components',{})) < 10: errs.append(f'{suite.name}: too few components')
    if len(data.get('submission',{})) < 5: errs.append(f'{suite.name}: too few submission modules')
    samples.append({'suite':suite.name,'sample_selected':selected[:12]})
print(json.dumps({'samples':samples,'errors':errs}, indent=2))
if errs: sys.exit(1)
