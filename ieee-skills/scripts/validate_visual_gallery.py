#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
g=ROOT/'paper_templates'/'visual_gallery'
errs=[]
for rel in ['visual_gallery_manifest.json','visual_gallery_manifest.yaml','visual_gallery_index.csv','README.md','main_figures/index.md','motivation_figures/index.md','tables/index.md']:
    if not (g/rel).exists(): errs.append('missing paper_templates/visual_gallery/'+rel)
try:
    data=json.loads((g/'visual_gallery_manifest.json').read_text(encoding='utf-8'))
    assets=[r for r in data.get('assets',[]) if 'asset_id' in r]
    if not assets: errs.append('no visual assets')
    for r in assets:
        p=ROOT/r.get('local_path','')
        if not p.exists(): errs.append('missing asset '+str(p))
        if 'copyright_note' not in r: errs.append('missing copyright note '+r.get('asset_id','?'))
except Exception as e:
    errs.append(str(e))
print(json.dumps({'passed':not errs,'errors':errs},indent=2))
sys.exit(1 if errs else 0)
