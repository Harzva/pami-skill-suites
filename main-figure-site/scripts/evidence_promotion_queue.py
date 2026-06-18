#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
try:
    import yaml
except Exception:
    yaml = None

def data_dir() -> Path:
    root = Path.cwd()
    if (root/'main_figure_site'/'data').exists(): return root/'main_figure_site'/'data'
    if (root/'data').exists(): return root/'data'
    raise SystemExit('Cannot find main_figure_site/data or data')

def load(name):
    p=data_dir()/name
    if not p.exists(): raise SystemExit(f'Missing {p}')
    return json.loads(p.read_text(encoding='utf-8'))

def require(obj, keys, name):
    miss=[k for k in keys if k not in obj]
    if miss: raise SystemExit(f'{name} missing keys: {miss}')

def ok(msg): print(msg)

def main():
    obj=load('evidence_promotion_queue.json')
    require(obj, ['schema_version','release_version','summary','queue','promotion_policy'], 'evidence_promotion_queue')
    q=obj['queue']
    if not isinstance(q, list) or not q: raise SystemExit('promotion queue empty')
    for item in q:
        require(item, ['candidate_id','promotion_status','promotion_priority','can_promote_to_extraction_ready','required_evidence_before_promotion'], 'queue item')
        if item.get('can_promote_to_extraction_ready') is True:
            raise SystemExit('offline release must not mark extraction-ready candidates')
    ok(f"evidence_promotion_queue.py: passed ({len(q)} items)")
if __name__=='__main__': main()
