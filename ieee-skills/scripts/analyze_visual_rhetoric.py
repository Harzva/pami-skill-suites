#!/usr/bin/env python3
"""Analyze extracted visual assets and regenerate visual_rhetoric_report.*.
Offline-safe: reads only local visual_asset_manifest and image files.
"""
import json, pathlib, statistics
from collections import Counter
try:
    import yaml
except Exception:
    yaml = None
try:
    from PIL import Image, ImageStat
except Exception:
    Image = None
ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'resources'
MANIFEST = ROOT / 'paper_templates' / 'extracted_visual_assets' / 'visual_asset_manifest.json'
def dump_yaml(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    if yaml: path.write_text(yaml.safe_dump(obj, sort_keys=False, allow_unicode=True), encoding='utf-8')
    else: path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')
def stats(rel):
    p = ROOT / rel
    if not p.exists() or Image is None:
        return {'width': None, 'height': None, 'orientation': 'unknown'}
    im = Image.open(p).convert('RGB')
    w,h = im.size
    st = ImageStat.Stat(im.resize((min(w,256),min(h,256))))
    mean=sum(st.mean)/3
    contrast=sum((hi-lo) for lo,hi in st.extrema)/3
    return {'width':w,'height':h,'aspect_ratio':round(w/h,3),'orientation':'wide' if w/h>1.35 else ('tall' if h/w>1.35 else 'balanced'),'brightness':round(mean,2),'contrast_proxy':round(contrast,2)}
def role(a): return a.get('asset_type','unknown')
def pattern(a):
    r=role(a)
    t=(a.get('title') or '').lower()
    if r=='main_figure' and 'survey' in t: return 'taxonomy-overview-map'
    if r=='main_figure': return 'architecture-or-overview-map'
    if r=='motivation_figure': return 'problem-gap-to-method-motivation'
    if r=='beautiful_table': return 'result-comparison-or-ablation-table'
    return 'visual-evidence'
def main():
    data=json.loads(MANIFEST.read_text(encoding='utf-8'))
    items=[]; counts=Counter()
    for a in data.get('assets',[]):
        s=stats(a.get('asset_path',''))
        p=pattern(a); counts[p]+=1
        items.append({'asset_id':f"{a.get('paper_id')}::{role(a)}::p{a.get('page')}",'paper_id':a.get('paper_id'),'role':role(a),'asset_path':a.get('asset_path'),'journal':a.get('journal'),'visual_rhetoric_pattern':p,'analysis_stats':s,'use_scope':'structure-analysis-only'})
    report={'schema_version':'1.0','release_version':'1.9.0','asset_total':len(items),'pattern_counts':dict(counts),'assets':items,'copyright_safety':'Do not copy, redraw, or publish extracted assets without license and permission checks.'}
    OUT.mkdir(exist_ok=True)
    (OUT/'visual_rhetoric_report.json').write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
    dump_yaml(OUT/'visual_rhetoric_report.yaml', report)
    print('visual rhetoric assets:', len(items))
if __name__ == '__main__': main()
