#!/usr/bin/env python3
from pathlib import Path
import json, sys, re
ROOT=Path(__file__).resolve().parents[1]
req=['journal_homepage','author_instructions','submission_system','manuscript_template','publishing_agreement','copyright_license','open_access','ethics_integrity','ai_disclosure_policy','data_code_availability','permissions']
reg_path=ROOT/'resources'/'official_source_registry.json'
errs=[]
if not reg_path.exists(): errs.append('missing resources/official_source_registry.json')
else:
    data=json.loads(reg_path.read_text(encoding='utf-8'))
    for j in data.get('journals',[]):
        fields=j.get('fields',{})
        for k in req:
            v=fields.get(k,'')
            if not isinstance(v,str) or not (v.startswith('http') or v.startswith('Not verified')):
                errs.append(f"{j.get('id')}: missing/invalid {k}: {v}")
        if 'live verification required' not in j.get('verification_status','').lower():
            errs.append(f"{j.get('id')}: missing live verification status")
for frag in (ROOT/'skills').glob('*skill-suite/static/journals/*.md'):
    if frag.name.endswith('-source-map.md'): continue
    txt=frag.read_text(encoding='utf-8',errors='ignore').lower()
    for phrase in ['official source compliance matrix','journal homepage','author instructions','submission system','manuscript template','publishing agreement','copyright / license','open access','ai disclosure policy','data / code availability','permissions','last verified date','verification status']:
        if phrase not in txt:
            errs.append(f"{frag}: missing phrase {phrase}")
print(json.dumps({'errors': errs}, indent=2))
sys.exit(1 if errs else 0)
