#!/usr/bin/env python3
from pathlib import Path
import argparse, yaml, json
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser()
ap.add_argument('--query', required=True)
args=ap.parse_args(); q=args.query.lower()
out=[]
for suite in [p for p in (ROOT/'skills').iterdir() if p.is_dir() and p.name.endswith('skill-suite')]:
    data=yaml.safe_load((suite/'manifest.yaml').read_text(encoding='utf-8'))
    selected=[]
    for sec in ['journals','components','submission']:
        for name,item in data.get(sec,{}).items():
            if any(a and a.lower() in q for a in item.get('aliases',[])):
                selected.append({'section':sec,'name':name,'module':item.get('module')})
    out.append({'suite':suite.name,'query':args.query,'selected_modules':selected})
print(json.dumps(out, indent=2, ensure_ascii=False))
