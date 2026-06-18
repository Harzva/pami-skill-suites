#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
errs=[]
for frag in (ROOT/'skills').glob('*skill-suite/static/submission/*.md'):
    txt=frag.read_text(encoding='utf-8',errors='ignore').lower()
    for phrase in ['publisher official rule','journal official rule','repository best-practice recommendation','template-paper observation','live verification warning','live verification required before submission']:
        if phrase not in txt:
            errs.append(f"{frag}: missing {phrase}")
for frag in (ROOT/'skills').glob('*skill-suite/static/journals/*.md'):
    if frag.name.endswith('-source-map.md'): continue
    txt=frag.read_text(encoding='utf-8',errors='ignore').lower()
    if 'live verification required before submission' not in txt:
        errs.append(f"{frag}: missing live verification warning")
print(json.dumps({'errors': errs}, indent=2))
sys.exit(1 if errs else 0)
