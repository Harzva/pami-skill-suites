#!/usr/bin/env python3
"""Offline-safe v2.3.0 helper for main-figure evidence workflows."""
from __future__ import annotations
import json, sys
from pathlib import Path

def site_root() -> Path:
    cwd = Path.cwd()
    if (cwd / 'main_figure_site' / 'data').exists():
        return cwd / 'main_figure_site'
    if (cwd / 'data').exists():
        return cwd
    raise SystemExit('Run from repository root or main-figure-site root.')

def load_json(p: Path):
    with open(p, encoding='utf-8') as f:
        return json.load(f)

def require(p: Path):
    if not p.exists():
        raise SystemExit(f'Missing required path: {p}')
    return p


def main():
    root = site_root(); data = root / 'data'
    plan = load_json(require(data / 'metadata_connector_plan.json'))
    connectors = plan.get('connectors', [])
    required = {'crossref','openalex','unpaywall','publisher-official-page','institutional-repository'}
    found = {c.get('connector_id') for c in connectors}
    missing = required - found
    if missing:
        raise SystemExit(f'Missing connector plan entries: {sorted(missing)}')
    print('metadata connector plan entries:', len(connectors))
if __name__ == '__main__': main()
