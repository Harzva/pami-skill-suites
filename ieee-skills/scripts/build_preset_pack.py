#!/usr/bin/env python3
from pathlib import Path
import zipfile, json
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'; DIST.mkdir(exist_ok=True)
PRESETS=ROOT/'presets'
outputs=[]; errs=[]
RESOURCE_FILES=[
 'resources/preset_registry.json','resources/preset_registry.yaml',
 'resources/preset_coverage_matrix.json','resources/preset_coverage_matrix.yaml',
 'resources/preset_eval_report.json','resources/preset_eval_report.yaml',
 'resources/preset_route_trace_index.json','resources/preset_route_trace_index.yaml',
 'resources/release_health_dashboard.json','resources/source_badges.json'
]
def add_tree(z, src, arcroot):
    if not src.exists(): return
    for p in sorted(src.rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc':
            z.write(p, arcroot/p.relative_to(src))
if not PRESETS.exists():
    errs.append('missing presets/')
else:
    for preset in sorted(p for p in PRESETS.iterdir() if p.is_dir()):
        zpath=DIST/f'preset-{preset.name}.zip'
        if zpath.exists(): zpath.unlink()
        with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED,compresslevel=1) as z:
            add_tree(z, preset, Path(preset.name))
            for rel in RESOURCE_FILES:
                f=ROOT/rel
                if f.exists(): z.write(f, Path(preset.name)/rel)
        outputs.append(str(zpath.relative_to(ROOT)))
        zpath2=DIST/f'preset-scenarios-{preset.name}.zip'
        if zpath2.exists(): zpath2.unlink()
        with zipfile.ZipFile(zpath2,'w',zipfile.ZIP_DEFLATED,compresslevel=1) as z:
            for sub in ['scenarios','sample-outputs','route-traces']: add_tree(z,preset/sub,Path(preset.name)/sub)
            if (preset/'evaluation-report.md').exists(): z.write(preset/'evaluation-report.md',Path(preset.name)/'evaluation-report.md')
        outputs.append(str(zpath2.relative_to(ROOT)))
    agg=DIST/'presets.zip'
    if agg.exists(): agg.unlink()
    with zipfile.ZipFile(agg,'w',zipfile.ZIP_DEFLATED,compresslevel=1) as z:
        add_tree(z, PRESETS, Path('presets'))
        for rel in RESOURCE_FILES:
            f=ROOT/rel
            if f.exists(): z.write(f, rel)
    outputs.append(str(agg.relative_to(ROOT)))
    scen=DIST/'preset-scenarios.zip'
    if scen.exists(): scen.unlink()
    with zipfile.ZipFile(scen,'w',zipfile.ZIP_DEFLATED,compresslevel=1) as z:
        for preset in sorted(p for p in PRESETS.iterdir() if p.is_dir()):
            for sub in ['scenarios','sample-outputs','route-traces']: add_tree(z,preset/sub,Path('presets')/preset.name/sub)
            if (preset/'evaluation-report.md').exists(): z.write(preset/'evaluation-report.md',Path('presets')/preset.name/'evaluation-report.md')
    outputs.append(str(scen.relative_to(ROOT)))
print(json.dumps({'built_preset_zips':outputs,'errors':errs},indent=2))
if errs: raise SystemExit(1)
