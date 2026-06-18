#!/usr/bin/env python3
from pathlib import Path
import argparse, json, sys
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--list', action='store_true')
parser.add_argument('--preset')
parser.add_argument('--scenario', default='writing-related-work')
args=parser.parse_args()
idx=ROOT/'resources/preset_route_trace_index.json'
if not idx.exists(): print(json.dumps({'error':'missing preset_route_trace_index.json'})); sys.exit(1)
data=json.loads(idx.read_text(encoding='utf-8'))
if args.list:
    print(json.dumps({'presets':[p['preset_id'] for p in data.get('presets',[])], 'scenarios':['writing-related-work','figure-table-caption','reviewer-response-submission']}, indent=2)); sys.exit(0)
if not args.preset: print(json.dumps({'error':'use --list or --preset'})); sys.exit(1)
p=ROOT/'presets'/args.preset/'route-traces'/f'{args.scenario}.json'
if not p.exists(): print(json.dumps({'error':f'missing {p.relative_to(ROOT)}'})); sys.exit(1)
print(p.read_text(encoding='utf-8'))
