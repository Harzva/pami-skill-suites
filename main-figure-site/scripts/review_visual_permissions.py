#!/usr/bin/env python3
from pathlib import Path
import json, argparse

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--site', default='main_figure_site')
    args=ap.parse_args(); site=Path(args.site)
    m=json.loads((site/'data/main_figure_manifest.json').read_text())
    q={'schema_version':'2.0.0','items':[]}
    for e in m.get('entries',[]):
        q['items'].append({'paper_id':e['paper_id'],'priority':'P1','checks':['license','attribution','third-party material','target venue policy'],'source_url':e.get('source_url')})
    (site/'data/visual_permission_review_queue.json').write_text(json.dumps(q,indent=2),encoding='utf-8')
    print(f'permission review queue: {len(q["items"])}')
if __name__=='__main__': main()
