#!/usr/bin/env python3
from pathlib import Path
import json, argparse, html

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--site', default='main_figure_site')
    args=ap.parse_args(); site=Path(args.site)
    data=json.loads((site/'data/main_figure_manifest.json').read_text())
    cards=[]
    for e in data.get('entries',[]):
        img=e.get('site_image_path') or e.get('main_figure_path')
        cards.append(f'<section><img src="../{html.escape(img)}" style="max-width:100%"><h3>{html.escape(e.get("title",""))}</h3><p>{html.escape(e.get("journal",""))}</p></section>')
    (site/'docs').mkdir(exist_ok=True)
    (site/'docs/gallery.html').write_text('<!doctype html><meta charset="utf-8"><h1>Main Figure Gallery</h1>'+''.join(cards), encoding='utf-8')
    print('gallery built')
if __name__=='__main__': main()
