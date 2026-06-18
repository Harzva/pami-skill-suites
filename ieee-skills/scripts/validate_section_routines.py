#!/usr/bin/env python3
"""Validate experiment/formula/motivation/limitations/conclusion routine libraries."""
import json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
required=['section_routine_library.json','experiment_organization_library.json','formula_organization_library.json','motivation_organization_library.json','limitations_future_work_library.json','conclusion_organization_library.json']
miss=[f for f in required if not (ROOT/'resources'/f).exists()]
if miss:
    print('missing section routine libraries:', miss); sys.exit(1)
for f in required:
    obj=json.loads((ROOT/'resources'/f).read_text(encoding='utf-8'))
    text=json.dumps(obj, ensure_ascii=False).lower()
    if f!='section_routine_library.json' and ('fixed_routines' not in obj or 'output_contract' not in obj):
        print('bad routine file:', f); sys.exit(1)
print('validate_section_routines.py: passed')
