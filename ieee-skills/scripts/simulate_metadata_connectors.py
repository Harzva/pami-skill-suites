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
    obj=load('connector_simulation_report.json')
    require(obj, ['summary','connectors','simulation_policy'], 'connector_simulation_report')
    expected={'crossref','openalex','unpaywall','publisher_official_page','institutional_repository_metadata'}
    got={c.get('connector_id') for c in obj['connectors']}
    missing=expected-got
    if missing: raise SystemExit(f'missing connector simulations: {missing}')
    if obj['simulation_policy'].get('live_lookup_performed') is not False:
        raise SystemExit('offline release must not claim live connector lookup')
    ok(f"simulate_metadata_connectors.py: passed ({len(got)} connectors)")
if __name__=='__main__': main()
