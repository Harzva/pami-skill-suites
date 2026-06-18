#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
PRESETS=['computer-vision','medical-ai','remote-sensing','multimedia','data-mining','signal-processing']
errs=[]; rows=[]
if (ROOT/'skills'/'presets').exists(): errs.append('presets must not be nested under default skills/')
for rel in ['resources/preset_registry.json','resources/preset_registry.yaml','resources/preset_coverage_matrix.json','resources/preset_coverage_matrix.yaml']:
    if not (ROOT/rel).exists(): errs.append(f'missing {rel}')
for pid in PRESETS:
    p=ROOT/'presets'/pid
    if not p.exists(): errs.append(f'missing presets/{pid}')
    for f in ['README.md','preset.yaml','prompt-pack.md','routing-profile.yaml','eval-profile.yaml']:
        if not (p/f).exists(): errs.append(f'{pid}: missing {f}')
    try:
        data=yaml.safe_load((p/'preset.yaml').read_text(encoding='utf-8')) or {}
        if data.get('preset_id')!=pid: errs.append(f'{pid}: preset_id mismatch')
        if data.get('visibility','').lower().find('not default')<0: errs.append(f'{pid}: visibility must state not default')
        if not data.get('target_journals'): errs.append(f'{pid}: no target_journals')
        if not data.get('default_module_bundle'): errs.append(f'{pid}: missing default_module_bundle')
        rows.append({'preset':pid,'journals':len(data.get('target_journals') or []),'visibility':data.get('visibility')})
    except Exception as e:
        errs.append(f'{pid}: cannot parse preset.yaml: {e}')
try:
    registry=json.loads((ROOT/'resources/preset_registry.json').read_text(encoding='utf-8'))
    ids=[p.get('id') for p in registry.get('presets',[])]
    for pid in PRESETS:
        if pid not in ids: errs.append(f'registry missing {pid}')
except Exception as e:
    errs.append(f'cannot parse preset_registry.json: {e}')
print(json.dumps({'presets':rows,'errors':errs},indent=2))
if errs: sys.exit(1)
