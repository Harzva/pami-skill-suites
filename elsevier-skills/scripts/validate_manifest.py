#!/usr/bin/env python3
from pathlib import Path
import sys, yaml, json
ROOT=Path(__file__).resolve().parents[1]
errs=[]
for suite in [p for p in (ROOT/'skills').iterdir() if p.is_dir() and p.name.endswith('skill-suite')]:
    mf=suite/'manifest.yaml'
    if not mf.exists(): errs.append(f'missing manifest: {suite.name}'); continue
    data=yaml.safe_load(mf.read_text(encoding='utf-8'))
    for key in ['suite','default_skills','journals','components','submission','official_source_policy']:
        if key not in data: errs.append(f'{suite.name}: missing {key}')
    for section in ['journals','components','submission']:
        for name, item in data.get(section,{}).items():
            mod=suite/item.get('module','')
            if not mod.exists(): errs.append(f'{suite.name}: missing module {section}/{name}: {mod}')
print(json.dumps({'errors':errs}, indent=2))
if errs: sys.exit(1)
