#!/usr/bin/env python3
from pathlib import Path
import argparse,json,sys
ROOT=Path(__file__).resolve().parents[1]; PRESETS=['computer-vision','medical-ai','remote-sensing','multimedia','data-mining','signal-processing']; ap=argparse.ArgumentParser(); ap.add_argument('--list',action='store_true'); ap.add_argument('--preset'); ap.add_argument('--scenario'); args=ap.parse_args(); rows=[]
for pid in PRESETS:
 for f in sorted((ROOT/'presets'/pid/'route-traces').glob('*.json')):
  d=json.loads(f.read_text(encoding='utf-8')); rows.append({'preset_id':pid,'scenario_id':d.get('scenario_id'), 'trace_path':str(f.relative_to(ROOT)), 'steps':len(d.get('steps') or [])})
if args.preset: rows=[r for r in rows if r['preset_id']==args.preset]
if args.scenario: rows=[r for r in rows if r['scenario_id']==args.scenario]
out={'route_trace_count':len(rows),'traces':rows}; (ROOT/'resources/preset_route_trace_index.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8'); print(json.dumps({'presets':PRESETS} if args.list else out,indent=2,ensure_ascii=False)); sys.exit(1 if args.preset and not rows else 0)
