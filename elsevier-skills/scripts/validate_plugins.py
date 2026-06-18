#!/usr/bin/env python3
from pathlib import Path
import json, sys, zipfile
ROOT=Path(__file__).resolve().parents[1]
errs=[]; rows=[]
plugins=ROOT/'plugins'
if not plugins.exists(): errs.append('missing plugins/')
for mode in ['default','compact']:
    d=plugins/mode
    for rel in ['plugin.yaml','plugin.json','README.md']:
        if not (d/rel).exists(): errs.append(f'missing plugins/{mode}/{rel}')
    z=ROOT/'dist'/f'plugin-{mode}.zip'
    row={'mode':mode,'zip_exists':z.exists()}
    if z.exists():
        try:
            with zipfile.ZipFile(z) as f:
                bad=f.testzip(); names=set(f.namelist())
                if bad: errs.append(f'{z.name}: bad file {bad}')
                for expected in [f'plugin-{mode}/plugin.yaml', f'plugin-{mode}/README.md']:
                    if expected not in names: errs.append(f'{z.name}: missing {expected}')
                row['file_count']=len(names)
        except Exception as e: errs.append(f'{z.name}: {e}')
    else:
        errs.append(f'missing dist/plugin-{mode}.zip')
    rows.append(row)
print(json.dumps({'plugins':rows,'errors':errs}, indent=2))
if errs: sys.exit(1)
