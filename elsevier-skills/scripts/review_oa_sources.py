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
    report = read_json('oa_source_review_report.json')
    forbidden = ['Sci-Hub','pirated PDFs','paywalled-only PDFs','copyright-unknown PDFs','unauthorized image reuse']
    records = report.get('items', [])
    errors=[]
    for item in records:
        src = str(item.get('source_url',''))
        if any(bad.lower() in src.lower() for bad in forbidden):
            errors.append({'candidate_id': item.get('candidate_id'), 'error':'forbidden source marker in URL'})
    out={'script':'review_oa_sources.py','records':len(records),'ready_for_extraction':sum(1 for i in records if i.get('ready_for_extraction')),'errors':errors,'passed':not errors and len(records)>=100}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out['passed'] else 1
if __name__ == '__main__': raise SystemExit(main())
