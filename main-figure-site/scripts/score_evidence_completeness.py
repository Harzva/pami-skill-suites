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
    scores = load_json(require(data / 'evidence_completeness_scores.json'))
    summary = scores.get('summary', {})
    print('total_candidates:', summary.get('total_candidates'))
    print('extraction_allowed_now:', summary.get('extraction_allowed_now'))
    if summary.get('extraction_allowed_now', 1) != 0:
        raise SystemExit('Offline release should not unlock new extraction.')
if __name__ == '__main__': main()
