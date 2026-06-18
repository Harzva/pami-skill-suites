#!/usr/bin/env python3
from pathlib import Path
import json,sys,yaml
ROOT=Path(__file__).resolve().parents[1]; PRESETS=['computer-vision','medical-ai','remote-sensing','multimedia','data-mining','signal-processing']; ER=[]; rows=[]
if (ROOT/'skills'/'presets').exists(): ER.append('presets must not be under default skills')
for pid in PRESETS:
 p=ROOT/'presets'/pid; sc=list((p/'scenarios').glob('*.yaml')); sm=list((p/'sample-outputs').glob('*.md')); tr=list((p/'route-traces').glob('*.json'))
 if len(sc)<3 or len(sm)<3 or len(tr)<3: ER.append(f'{pid}: expected >=3 scenarios/samples/traces')
 if not (p/'evaluation-report.md').exists(): ER.append(f'{pid}: missing evaluation-report.md')
 for f in sc:
  d=yaml.safe_load(f.read_text(encoding='utf-8')) or {}
  for k in ['scenario_id','preset_id','scenario_type','selected_skills_modules','official_source_warning','copyright_safe_paper_mining_warning','reviewer_risk_checklist','structured_output_contract']:
   if k not in d: ER.append(f'{pid}/{f.name}: missing {k}')
 for f in sm:
  txt=f.read_text(encoding='utf-8').lower()
  for x in ['selected skills/modules','official-source warning','copyright-safe paper-mining warning','reviewer-risk checklist','structured output contract']:
   if x not in txt: ER.append(f'{pid}/{f.name}: missing {x}')
 rows.append({'preset':pid,'scenarios':len(sc),'sample_outputs':len(sm),'route_traces':len(tr)})
for rel in ['resources/preset_eval_report.json','resources/preset_eval_report.yaml','resources/preset_route_trace_index.json','resources/preset_route_trace_index.yaml']:
 if not (ROOT/rel).exists(): ER.append(f'missing {rel}')
print(json.dumps({'preset_scenarios':rows,'errors':ER,'passed':not ER},indent=2)); sys.exit(1 if ER else 0)
