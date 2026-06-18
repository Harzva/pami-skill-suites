#!/usr/bin/env python3
from pathlib import Path
import zipfile,json,sys
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
required=['default-skills.zip','compact-suite.zip','advanced-skills.zip','full-suite.zip','plugin-default.zip','plugin-compact.zip','presets.zip','preset-scenarios.zip','source-maintenance.zip','source-trust-review.zip','source-policy-diff.zip','visual-assets.zip','rag-evaluation.zip']
# Also require per-pack dist files if directories exist.
if (ROOT/'expansion_packs').exists():
    required.append('expansion-packs.zip')
    for d in (ROOT/'expansion_packs').iterdir():
        if d.is_dir(): required.append(f'expansion-pack-{d.name}.zip')
if (ROOT/'presets').exists():
    for d in (ROOT/'presets').iterdir():
        if d.is_dir():
            required.append(f'preset-{d.name}.zip'); required.append(f'preset-scenarios-{d.name}.zip')
errs=[]
for r in required:
    p=DIST/r
    if not p.exists(): errs.append(f'missing dist/{r}')
    else:
        try:
            with zipfile.ZipFile(p) as z:
                bad=z.testzip()
            if bad: errs.append(f'{r}: bad {bad}')
        except Exception as e: errs.append(f'{r}: {e}')
print(json.dumps({'dist_count':len(list(DIST.glob('*.zip'))) if DIST.exists() else 0,'required_count':len(required),'errors':errs,'passed':not errs},indent=2))
sys.exit(1 if errs else 0)
