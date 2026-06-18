#!/usr/bin/env python3
from pathlib import Path
import json, argparse, sys
REQUIRED=['paper_id','title','journal','year','doi','license','source_url','site_image_path','safe_summary','visual_rhetoric_tags','linked_paper_section','reusable_structure_lessons','copyright_safety_note']
PROHIBITED=['sci-hub','scihub','libgen','z-library','pirate']

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--site', default='main_figure_site')
    args=ap.parse_args(); site=Path(args.site)
    errors=[]
    for rel in ['data/main_figure_manifest.json','data/main_figure_cards','data/multimodal_rag_index.json','data/visual_tags.json','data/license_registry.json']:
        if not (site/rel).exists(): errors.append(f'missing {rel}')
    if errors:
        print('\n'.join(errors)); sys.exit(1)
    m=json.loads((site/'data/main_figure_manifest.json').read_text())
    if m.get('target_capacity_minimum',0) < 100: errors.append('target_capacity_minimum must be >=100')
    for e in m.get('entries',[]):
        for k in REQUIRED:
            if k not in e: errors.append(f'{e.get("paper_id")}: missing {k}')
        img=site/e.get('site_image_path','')
        if not img.exists(): errors.append(f'{e.get("paper_id")}: image path missing')
        url=(e.get('source_url') or '').lower()
        if any(x in url for x in PROHIBITED): errors.append(f'{e.get("paper_id")}: prohibited source marker in URL')
        if not (site/'data/main_figure_cards'/f"{e.get('paper_id')}.md").exists(): errors.append(f'{e.get("paper_id")}: missing card')
    if errors:
        print('\n'.join(errors)); sys.exit(1)
    print(f'validate_main_figure_corpus.py: passed ({len(m.get("entries",[]))} seeded figures; capacity {m.get("target_capacity_minimum")})')
if __name__=='__main__': main()
