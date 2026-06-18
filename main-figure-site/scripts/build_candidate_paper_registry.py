#!/usr/bin/env python3
from __future__ import annotations
import json, yaml, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '.'
DATA = SITE / 'data'

def read_json(name):
    return json.loads((DATA/name).read_text(encoding='utf-8'))

def write_json(name, obj):
    (DATA/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def write_yaml(name, obj):
    (DATA/name).write_text(yaml.safe_dump(obj, sort_keys=False, allow_unicode=True), encoding='utf-8')


def main():
    manifest = read_json('main_figure_manifest.json')
    candidates = read_json('candidate_papers_100.json')
    required = ['paper_id','title','journal','year','DOI','source URL','license candidate','OA source type','permission review status','extraction readiness','target figure type']
    missing=[]
    for item in candidates.get('candidates', []):
        for key in required:
            if key not in item:
                missing.append({'candidate_id': item.get('candidate_id'), 'missing': key})
    result = {'script':'build_candidate_paper_registry.py','candidate_count': len(candidates.get('candidates', [])), 'seed_count': candidates.get('actual_seed_count', 0), 'missing_required_fields': missing, 'passed': len(missing)==0 and len(candidates.get('candidates', []))>=100}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['passed'] else 1
if __name__ == '__main__': raise SystemExit(main())
