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
    cards_dir = require(data / 'candidate_evidence_cards')
    source = load_json(require(data / 'source_discovery_candidates.json'))
    md_cards = list(cards_dir.glob('*.md'))
    json_cards = list(cards_dir.glob('*.json'))
    if len(md_cards) < len(source.get('records', [])) or len(json_cards) < len(source.get('records', [])):
        raise SystemExit('Evidence card count is smaller than source discovery record count.')
    print(f'candidate evidence cards: {len(json_cards)} json / {len(md_cards)} md')
if __name__ == '__main__': main()
