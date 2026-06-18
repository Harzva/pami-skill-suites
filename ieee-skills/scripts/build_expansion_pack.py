#!/usr/bin/env python3
from pathlib import Path
import shutil, zipfile, json
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'; DIST.mkdir(exist_ok=True)
PACKS_DIR=ROOT/'expansion_packs'
errs=[]; outputs=[]
def zipdir(src,zpath,arcroot=None):
    if zpath.exists(): zpath.unlink()
    with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as z:
        for p in src.rglob('*'):
            if p.is_file():
                z.write(p, (arcroot/p.relative_to(src)) if arcroot else p.relative_to(src.parent))
for pack in sorted(PACKS_DIR.iterdir() if PACKS_DIR.exists() else []):
    if not pack.is_dir(): continue
    zpath=DIST/f'expansion-pack-{pack.name}.zip'
    zipdir(pack,zpath,Path(pack.name))
    outputs.append(str(zpath.relative_to(ROOT)))
# Aggregate zip containing all expansion packs.
agg=DIST/'expansion-packs.zip'
if agg.exists(): agg.unlink()
with zipfile.ZipFile(agg,'w',zipfile.ZIP_DEFLATED) as z:
    for pack in sorted(PACKS_DIR.iterdir() if PACKS_DIR.exists() else []):
        if pack.is_dir():
            for p in pack.rglob('*'):
                if p.is_file(): z.write(p, Path('expansion_packs')/pack.name/p.relative_to(pack))
outputs.append(str(agg.relative_to(ROOT)))
print(json.dumps({'built_expansion_pack_zips':outputs,'errors':errs}, indent=2))
if errs: raise SystemExit(1)
