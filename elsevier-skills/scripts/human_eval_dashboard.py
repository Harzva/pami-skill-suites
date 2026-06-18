#!/usr/bin/env python3
"""v2.7.0 helper script for RAG Trace UI + Visual Query Debugger.

This script is offline-safe. It reads local JSON/YAML assets only. It does not
perform live DOI/OA/license lookup, image embedding, gallery hosting, or figure
reuse permission inference.
"""
from __future__ import annotations
import json
from pathlib import Path

SCRIPT_NAME = Path(__file__).name


def site_root() -> Path:
    root = Path(__file__).resolve().parent.parent
    if (root / 'main_figure_site' / 'data').exists():
        return root / 'main_figure_site'
    return root


def require(path: Path):
    if not path.exists():
        raise SystemExit(f'Missing required file: {path}')
    return path


def load_json(path: Path):
    return json.loads(require(path).read_text(encoding='utf-8'))


def main() -> None:
    sroot = site_root()
    data = sroot / 'data'
    checks = {
        'build_rag_trace_ui_index.py': ['rag_trace_ui_index.json'],
        'visual_query_debugger.py': ['visual_query_debug_traces.json'],
        'query_rewrite_suggestions.py': ['query_rewrite_suggestions.json'],
        'missing_tag_coverage_report.py': ['missing_tag_coverage_report.json'],
        'corpus_expansion_recommendations.py': ['corpus_expansion_recommendations.json'],
        'human_eval_dashboard.py': ['human_eval_dashboard.json'],
        'validate_rag_trace_ui.py': [
            'rag_trace_ui_index.json',
            'visual_query_debug_traces.json',
            'query_rewrite_suggestions.json',
            'missing_tag_coverage_report.json',
            'corpus_expansion_recommendations.json',
            'human_eval_dashboard.json',
            'rag_entry_eligibility_report.json',
            'visual_query_benchmark.json',
        ],
    }
    files = checks.get(SCRIPT_NAME, [])
    for name in files:
        obj = load_json(data / name)
        if not isinstance(obj, dict):
            raise SystemExit(f'{name} is not a JSON object')
    if SCRIPT_NAME == 'validate_rag_trace_ui.py':
        trace = load_json(data / 'rag_trace_ui_index.json')
        debug = load_json(data / 'visual_query_debug_traces.json')
        rewrites = load_json(data / 'query_rewrite_suggestions.json')
        dashboard = load_json(data / 'human_eval_dashboard.json')
        if trace.get('context_policy', {}).get('image_embedding_allowed') is not False:
            raise SystemExit('image embedding gate must remain closed')
        if trace.get('context_policy', {}).get('public_gallery_allowed') is not False:
            raise SystemExit('public gallery gate must remain closed')
        if trace.get('trace_count', 0) <= 0:
            raise SystemExit('no RAG trace cards found')
        if len(debug.get('debug_traces', [])) != trace.get('trace_count'):
            raise SystemExit('debug trace count mismatch')
        if len(rewrites.get('suggestions', [])) != trace.get('trace_count'):
            raise SystemExit('rewrite suggestion count mismatch')
        if dashboard.get('completed_human_evaluations') != 0:
            raise SystemExit('offline release must not claim completed human evaluations')
    print(f'{SCRIPT_NAME}: passed')

if __name__ == '__main__':
    main()
