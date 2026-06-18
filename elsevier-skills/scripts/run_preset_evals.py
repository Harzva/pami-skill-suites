#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'resources/preset_eval_report.json').read_text(encoding='utf-8'))
errors=[]; rows=[]
for p in data.get('presets',[]):
    ok=p.get('scenario_count',0)>=3 and p.get('sample_output_count',0)>=3 and p.get('route_trace_count',0)>=3 and p.get('status')=='passed'
    rows.append({'preset':p.get('preset_id'),'passed':ok,'scenario_count':p.get('scenario_count'),'sample_output_count':p.get('sample_output_count'),'route_trace_count':p.get('route_trace_count')})
    if not ok: errors.append(f"preset eval failed: {p.get('preset_id')}")
print(json.dumps({'preset_eval_results':rows,'errors':errors,'passed':not errors}, indent=2))
if errors: sys.exit(1)
