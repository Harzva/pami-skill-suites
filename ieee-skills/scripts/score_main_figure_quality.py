#!/usr/bin/env python3
from __future__ import annotations
import json, yaml, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'main_figure_site'
DATA = SITE / 'data'

def read_json(name):
    return json.loads((DATA/name).read_text(encoding='utf-8'))

def write_json(name, obj):
    (DATA/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def write_yaml(name, obj):
    (DATA/name).write_text(yaml.safe_dump(obj, sort_keys=False, allow_unicode=True), encoding='utf-8')


def main():
    scores = read_json('main_figure_quality_scores.json')
    total=len(scores.get('scores', [])); seeds=sum(1 for s in scores.get('scores', []) if s.get('quality_band')=='seed-review')
    out={'script':'score_main_figure_quality.py','score_records':total,'seed_review_records':seeds,'passed':total>=100}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out['passed'] else 1
if __name__ == '__main__': raise SystemExit(main())
