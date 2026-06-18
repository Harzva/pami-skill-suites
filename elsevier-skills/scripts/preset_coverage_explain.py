#!/usr/bin/env python3
from pathlib import Path
import argparse, json, sys
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(); parser.add_argument('--preset'); args=parser.parse_args()
data=json.loads((ROOT/'resources/preset_registry.json').read_text(encoding='utf-8'))
rows=[]
for p in data.get('presets',[]):
    if args.preset and p.get('id')!=args.preset: continue
    rows.append({'preset':p.get('id'),'default_visible':p.get('default_visible'),'journal_count':p.get('journal_count'),'scenario_count':p.get('scenario_count'),'note':'Preset coverage is opt-in and does not increase default skill listing context.'})
print(json.dumps({'preset_coverage_explain':rows}, indent=2))
