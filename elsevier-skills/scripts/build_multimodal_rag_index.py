#!/usr/bin/env python3
from pathlib import Path
import json, argparse

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--site', default='main_figure_site')
    args=ap.parse_args(); site=Path(args.site)
    m=json.loads((site/'data/main_figure_manifest.json').read_text())
    records=[]
    for e in m.get('entries',[]):
        records.append({'id':e['paper_id'], 'image_path':e.get('site_image_path') or e.get('main_figure_path'), 'text_for_retrieval': f"{e.get('title')} | {e.get('journal')} | {e.get('safe_summary','')}", 'metadata': e})
    (site/'data/multimodal_rag_index.json').write_text(json.dumps({'schema_version':'2.0.0','records':records},indent=2), encoding='utf-8')
    print(f'RAG records: {len(records)}')
if __name__=='__main__': main()
