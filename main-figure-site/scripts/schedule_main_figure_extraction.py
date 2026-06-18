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
    tasks = read_json('main_figure_extraction_tasks.json')
    total=len(tasks.get('tasks', [])); ready=sum(1 for t in tasks.get('tasks', []) if t.get('status')=='completed-existing-seed')
    out={'script':'schedule_main_figure_extraction.py','total_tasks':total,'completed_seed_tasks':ready,'blocked_tasks':total-ready,'passed':total>=100}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out['passed'] else 1
if __name__ == '__main__': raise SystemExit(main())
