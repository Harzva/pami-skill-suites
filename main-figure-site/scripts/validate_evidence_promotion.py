#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
try:
    import yaml
except Exception:
    yaml = None

def data_dir() -> Path:
    root = Path.cwd()
    if (root/'main_figure_site'/'data').exists(): return root/'main_figure_site'/'data'
    if (root/'data').exists(): return root/'data'
    raise SystemExit('Cannot find main_figure_site/data or data')

def load(name):
    p=data_dir()/name
    if not p.exists(): raise SystemExit(f'Missing {p}')
    return json.loads(p.read_text(encoding='utf-8'))

def require(obj, keys, name):
    miss=[k for k in keys if k not in obj]
    if miss: raise SystemExit(f'{name} missing keys: {miss}')

def ok(msg): print(msg)

def main():
    required=[
        'evidence_promotion_queue.json','connector_simulation_report.json','candidate_evidence_diff_report.json',
        'human_reviewer_decision_log.json','extraction_ready_candidates.json','rag_ready_metadata_candidates.json']
    d=data_dir()
    for name in required:
        if not (d/name).exists(): raise SystemExit(f'missing {d/name}')
        obj=json.loads((d/name).read_text(encoding='utf-8'))
        if obj.get('release_version') not in {'v2.4.0','2.4.0'}: raise SystemExit(f'{name} wrong release_version')
    q=json.loads((d/'evidence_promotion_queue.json').read_text(encoding='utf-8'))['queue']
    r=json.loads((d/'rag_ready_metadata_candidates.json').read_text(encoding='utf-8'))['rag_ready_metadata_candidates']
    if any(i.get('can_promote_to_extraction_ready') for i in q): raise SystemExit('unexpected extraction-ready promotion')
    ok(f"validate_evidence_promotion.py: passed ({len(q)} candidates, {len(r)} metadata-only RAG records)")
if __name__=='__main__': main()
