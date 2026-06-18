#!/usr/bin/env python3
from pathlib import Path
import sys, json
ROOT=Path(__file__).resolve().parents[1]
errs=[]
for suite in [p for p in (ROOT/'skills').iterdir() if p.is_dir() and p.name.endswith('skill-suite')]:
    for frag in (suite/'static'/'journals').glob('*.md'):
        if frag.name.endswith('-source-map.md'): continue
        txt=frag.read_text(encoding='utf-8', errors='ignore').lower()
        for phrase in ['## official urls','official source compliance matrix','rule provenance classification','live verification required','source refresh metadata','last_live_checked','source_status','needs_reverification','official_link_health']:
            if phrase not in txt: errs.append(f'{frag}: missing {phrase}')
    for frag in (suite/'static'/'submission').glob('*.md'):
        txt=frag.read_text(encoding='utf-8', errors='ignore').lower()
        for phrase in ['required live checks','rule provenance classification','publisher official rule','journal official rule','repository best-practice recommendation','template-paper observation','live verification warning']:
            if phrase not in txt: errs.append(f'{frag}: missing {phrase}')
for rel in ['resources/official_source_registry.json','resources/source_refresh_report.json','resources/source_refresh_report.yaml']:
    if not (ROOT/rel).exists(): errs.append(f'missing {rel}')
print(json.dumps({'errors':errs}, indent=2))
if errs: sys.exit(1)
