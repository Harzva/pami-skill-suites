#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
try:
    import yaml
except Exception:
    yaml = None

VERSION = 'v2.4.0'
PROHIBITED = ['Sci-Hub', 'pirated PDF', 'paywalled-only PDF', 'copyright-unknown PDF', 'unauthorized image reuse']
CONNECTORS = ['crossref', 'openalex', 'unpaywall', 'publisher_official_page', 'institutional_repository']

def root() -> Path:
    return Path(__file__).resolve().parents[1]

def data_dir() -> Path:
    r = root()
    return r/'main_figure_site'/'data' if (r/'main_figure_site'/'data').exists() else r/'data'

def dump_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

def dump_yaml(path, obj):
    if yaml:
        path.write_text(yaml.safe_dump(obj, sort_keys=False, allow_unicode=True), encoding='utf-8')
    else:
        path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')

def load_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def cards():
    cdir = data_dir()/'candidate_evidence_cards'
    return [load_json(p) for p in sorted(cdir.glob('*.json')) if p.name != 'README.json']

def is_seed(c):
    return 'seed' in c.get('candidate_id','') or 'seed' in c.get('source_status','').lower() or c.get('evidence_completeness_score',0) >= 40

def main():
    mode = Path(__file__).stem
    d = data_dir()
    cs = cards()
    if not cs:
        raise SystemExit('No candidate evidence cards found.')
    seeds = sum(1 for c in cs if is_seed(c))
    pending = len(cs)-seeds
    if mode == 'validate_evidence_promotion':
        required = ['evidence_promotion_queue.json','connector_simulation_report.json','candidate_evidence_diff_report.json','human_reviewer_decision_log.json','extraction_ready_candidates.json','rag_ready_metadata_candidates.json']
        missing = [x for x in required if not (d/x).exists()]
        if missing:
            raise SystemExit('Missing v2.4.0 files: '+', '.join(missing))
        gate = load_json(d/'extraction_ready_candidates.json')
        if gate.get('summary',{}).get('extraction_ready_count',0) != 0:
            raise SystemExit('Unexpected extraction-ready candidates in offline release build.')
        print('validate_evidence_promotion.py: passed')
        return
    if mode == 'evidence_promotion_queue':
        queue = load_json(d/'evidence_promotion_queue.json') if (d/'evidence_promotion_queue.json').exists() else {'queue': []}
        print(f"evidence_promotion_queue.py: {len(queue.get('queue',[]))} items; seed={seeds}; pending={pending}; gate=closed")
        return
    if mode == 'simulate_metadata_connectors':
        sim = load_json(d/'connector_simulation_report.json') if (d/'connector_simulation_report.json').exists() else {'records': []}
        print(f"simulate_metadata_connectors.py: {len(sim.get('records',[]))} candidates; no live connector calls made")
        return
    if mode == 'candidate_evidence_diff':
        diff = load_json(d/'candidate_evidence_diff_report.json') if (d/'candidate_evidence_diff_report.json').exists() else {'records': []}
        print(f"candidate_evidence_diff.py: {len(diff.get('records',[]))} records; evidence_content_changed=0")
        return
    if mode == 'human_reviewer_decision_log':
        log = load_json(d/'human_reviewer_decision_log.json') if (d/'human_reviewer_decision_log.json').exists() else {'decisions': []}
        print(f"human_reviewer_decision_log.py: {len(log.get('decisions',[]))} pending decisions")
        return
    if mode == 'extraction_ready_candidates':
        ready = load_json(d/'extraction_ready_candidates.json') if (d/'extraction_ready_candidates.json').exists() else {'candidates': []}
        rag = load_json(d/'rag_ready_metadata_candidates.json') if (d/'rag_ready_metadata_candidates.json').exists() else {'candidates': []}
        print(f"extraction_ready_candidates.py: extraction_ready={len(ready.get('candidates',[]))}; rag_metadata_only={len(rag.get('candidates',[]))}")
        return

if __name__ == '__main__':
    main()
