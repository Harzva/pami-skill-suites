#!/usr/bin/env python3
"""Validate visual rhetoric and pattern-library artifacts for release."""
import json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
required=['visual_rhetoric_report.json','figure_pattern_library.json','table_pattern_library.json','caption_pattern_library.json','visual_asset_review_queue.json','visual_style_dashboard.json']
missing=[f for f in required if not (ROOT/'resources'/f).exists()]
if missing:
    print('missing visual pattern files:', missing); sys.exit(1)
report=json.loads((ROOT/'resources/visual_rhetoric_report.json').read_text(encoding='utf-8'))
if not report.get('assets'):
    print('visual_rhetoric_report has no assets'); sys.exit(1)
for f in required:
    obj=json.loads((ROOT/'resources'/f).read_text(encoding='utf-8'))
    if 'copy' not in json.dumps(obj).lower() and f not in ('visual_style_dashboard.json',):
        print('safety/copy warning may be missing:', f); sys.exit(1)
print('validate_visual_patterns.py: passed')
