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
    obj=load('human_reviewer_decision_log.json')
    require(obj, ['log_policy','summary','entries'], 'human_reviewer_decision_log')
    if obj['summary'].get('approved_for_new_extraction', -1) != 0:
        raise SystemExit('offline release must not approve new extraction')
    ok(f"human_reviewer_decision_log.py: passed ({len(obj['entries'])} entries)")
if __name__=='__main__': main()
