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
    obj=load('candidate_evidence_diff_report.json')
    require(obj, ['summary','items'], 'candidate_evidence_diff_report')
    if 'current_release' not in obj and 'baseline_release' not in obj:
        raise SystemExit('candidate_evidence_diff_report missing release comparison keys')
    if obj['summary'].get('candidates_with_evidence_content_changes', 0) != 0:
        raise SystemExit('offline v2.4 build should not claim live evidence content changes')
    ok(f"candidate_evidence_diff.py: passed ({len(obj['items'])} items)")
if __name__=='__main__': main()
