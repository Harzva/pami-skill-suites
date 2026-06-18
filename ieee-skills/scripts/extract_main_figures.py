#!/usr/bin/env python3
"""Dry-run extractor placeholder.
For v2.0.0, main figures are copied from the existing legal visual asset corpus.
Future live extraction must verify OA license and permission status before storing crops.
"""
from pathlib import Path
import argparse, json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo', default='.')
    args=ap.parse_args(); repo=Path(args.repo)
    m=repo/'paper_templates/extracted_visual_assets/visual_asset_manifest.json'
    if not m.exists(): raise SystemExit('missing visual_asset_manifest.json')
    data=json.loads(m.read_text())
    n=sum(1 for a in data.get('assets',[]) if a.get('asset_type')=='main_figure')
    print(f'dry-run: {n} existing main figures available; no new PDFs downloaded')
if __name__=='__main__': main()
