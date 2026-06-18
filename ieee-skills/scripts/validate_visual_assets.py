#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
base=ROOT/'paper_templates/extracted_visual_assets'
required=['visual_asset_manifest.json','visual_asset_manifest.yaml','visual_asset_index.csv','README.md','main_figures/index.md','motivation_figures/index.md','beautiful_tables/index.md','extraction_report.md']
errs=[r for r in required if not (base/r).exists()]
try:
    data=json.loads((base/'visual_asset_manifest.json').read_text(encoding='utf-8'))
    if len([a for a in data.get('assets',[]) if a.get('asset_path')]) < 3:
        errs.append('too few extracted visual assets')
except Exception as e:
    errs.append(f'visual_asset_manifest invalid: {e}')
print(json.dumps({'script':'validate_visual_assets.py','errors':errs,'passed':not errs},indent=2))
sys.exit(1 if errs else 0)
