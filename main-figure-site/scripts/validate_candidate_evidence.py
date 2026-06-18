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

REQUIRED_CARD_SECTIONS = ['doi_evidence','publisher_page_evidence','repository_oa_evidence','license_evidence','permission_evidence','third_party_material_evidence','manual_reviewer_notes']

def main():
    root = site_root(); data = root / 'data'
    source = load_json(require(data / 'source_discovery_candidates.json'))
    cards_dir = require(data / 'candidate_evidence_cards')
    require(data / 'evidence_completeness_scores.json')
    require(data / 'evidence_completeness_scores.yaml')
    require(data / 'extraction_gate_report.json')
    require(data / 'extraction_gate_report.yaml')
    require(data / 'metadata_connector_plan.json')
    require(data / 'metadata_connector_plan.yaml')
    records = source.get('records', [])
    failures = []
    for rec in records:
        cid = rec.get('candidate_id')
        p = cards_dir / f'{cid}.json'
        if not p.exists():
            failures.append(f'missing card json {cid}')
            continue
        card = load_json(p)
        for sec in REQUIRED_CARD_SECTIONS:
            if sec not in card:
                failures.append(f'{cid}: missing {sec}')
        if card.get('extraction_gate') in ('open','allowed'):
            failures.append(f'{cid}: extraction gate unexpectedly open')
    if failures:
        raise SystemExit('\n'.join(failures[:20]))
    print(f'candidate evidence validation passed: {len(records)} records')
if __name__ == '__main__': main()
