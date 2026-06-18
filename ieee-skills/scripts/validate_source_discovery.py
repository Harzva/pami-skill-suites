#!/usr/bin/env python3
"""Validate all v2.3.0 source-discovery workflow files.

Offline-safe v2.3.0 maintenance utility. It reads the local main_figure_site/data
records and does not download PDFs or use prohibited sources.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

PROHIBITED = ['Sci-Hub', 'pirated PDF', 'paywalled-only PDF', 'copyright-unknown PDF', 'unauthorized image reuse']

def find_data_dir() -> Path:
    here = Path(__file__).resolve()
    candidates = [here.parent.parent / 'main_figure_site' / 'data', here.parent.parent / 'data']
    for c in candidates:
        if (c / 'candidate_papers_100.json').exists() or (c / 'source_discovery_candidates.json').exists():
            return c
    raise SystemExit('Cannot locate main_figure_site/data or data directory.')

def load_json(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)

def main() -> int:
    data = find_data_dir()
    mode = 'validate'
    if mode == 'discover':
        obj = load_json(data / 'source_discovery_candidates.json')
        records = obj.get('records', [])
        missing = [r for r in records if not all(k in r for k in ['candidate_id','paper_id','proposed title','proposed journal','proposed DOI','proposed source URL','source type','license candidate','DOI status','OA status','permission risk','extraction readiness'])]
        if missing:
            print(f'FAIL: {len(missing)} records missing required fields')
            return 1
        print(f'PASS: source discovery records={len(records)} data_dir={data}')
    elif mode == 'preflight':
        obj = load_json(data / 'doi_license_preflight_report.json')
        items = obj.get('items', [])
        bad = []
        for item in items:
            url = str(item.get('proposed source URL',''))
            if any(p.lower() in url.lower() for p in ['sci-hub', 'scihub']):
                bad.append(item.get('candidate_id'))
        if bad:
            print('FAIL: prohibited source markers found: ' + ', '.join(bad[:10]))
            return 1
        print(f"PASS: preflight items={len(items)} passed={sum(1 for i in items if i.get('preflight passed'))}")
    elif mode == 'risk':
        obj = load_json(data / 'candidate_risk_scores.json')
        print('PASS: risk summary=' + json.dumps(obj.get('summary',{}), ensure_ascii=False))
    elif mode == 'queue':
        obj = load_json(data / 'source_discovery_review_queue.json')
        print('PASS: review queue summary=' + json.dumps(obj.get('summary',{}), ensure_ascii=False))
    elif mode == 'readiness':
        obj = load_json(data / 'extraction_readiness_dashboard.json')
        print('PASS: readiness summary=' + json.dumps(obj.get('summary',{}), ensure_ascii=False))
    elif mode == 'validate':
        required = ['source_discovery_candidates.json','doi_license_preflight_report.json','candidate_risk_scores.json','source_discovery_review_queue.json','extraction_readiness_dashboard.json']
        missing = [name for name in required if not (data / name).exists()]
        if missing:
            print('FAIL: missing ' + ', '.join(missing))
            return 1
        records = load_json(data/'source_discovery_candidates.json').get('records',[])
        if len(records) < 100:
            print(f'FAIL: expected 100 records, found {len(records)}')
            return 1
        print(f'PASS: v2.3.0 source discovery workflow valid; records={len(records)}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
