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
    report = read_json('duplicate_visual_check_report.json')
    dup_count = report.get('summary', {}).get('duplicate_path_count', 0)
    out={'script':'check_visual_duplicates.py','duplicate_path_count':dup_count,'passed':dup_count==0}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out['passed'] else 1
if __name__ == '__main__': raise SystemExit(main())
