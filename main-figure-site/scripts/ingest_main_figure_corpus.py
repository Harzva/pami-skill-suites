#!/usr/bin/env python3
"""Ingest already-extracted main figures into main_figure_site.
Offline-safe: does not download papers or claim permission status.
"""
from pathlib import Path
import json, shutil, re, argparse

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo', default='.')
    ap.add_argument('--site', default='main_figure_site')
    args=ap.parse_args()
    repo=Path(args.repo)
    manifest=repo/'paper_templates/extracted_visual_assets/visual_asset_manifest.json'
    if not manifest.exists():
        raise SystemExit('missing visual_asset_manifest.json')
    data=json.loads(manifest.read_text())
    site=repo/args.site
    (site/'gallery').mkdir(parents=True, exist_ok=True)
    (site/'data').mkdir(parents=True, exist_ok=True)
    records=[]
    for a in data.get('assets',[]):
        if a.get('asset_type')!='main_figure':
            continue
        src=repo/a['asset_path']
        if not src.exists():
            continue
        dest=site/'gallery'/src.name
        shutil.copy2(src,dest)
        records.append({'paper_id':a.get('paper_id'), 'title':a.get('title'), 'journal':a.get('journal'), 'license':a.get('license'), 'source_url':a.get('source_url'), 'main_figure_path':str(dest.relative_to(site)), 'permission_status':'requires-review-before-reuse'})
    (site/'data/main_figure_manifest.json').write_text(json.dumps({'schema_version':'2.0.0','current_seed_main_figures':len(records),'target_capacity_minimum':100,'entries':records},indent=2),encoding='utf-8')
    print(f'ingested {len(records)} main figures into {site}')
if __name__=='__main__': main()
