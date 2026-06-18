#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
PRESETS=['computer-vision','medical-ai','remote-sensing','multimedia','data-mining','signal-processing']
SCENARIOS=['writing-related-work','figure-table-caption','reviewer-response-submission']
errors=[]; rows=[]
if (ROOT/'skills'/'presets').exists(): errors.append('presets must not be nested under default skills/')
for pid in PRESETS:
    base=ROOT/'presets'/pid
    if not base.exists(): errors.append(f'missing presets/{pid}'); continue
    for d in ['scenarios','sample-outputs','route-traces']:
        if not (base/d).exists(): errors.append(f'{pid}: missing {d}/')
    if not (base/'evaluation-report.md').exists(): errors.append(f'{pid}: missing evaluation-report.md')
    for sid in SCENARIOS:
        scen=base/'scenarios'/f'{sid}.yaml'; sample=base/'sample-outputs'/f'{sid}.md'; tr=base/'route-traces'/f'{sid}.json'
        if not scen.exists(): errors.append(f'{pid}: missing {scen.relative_to(ROOT)}')
        if not sample.exists(): errors.append(f'{pid}: missing {sample.relative_to(ROOT)}')
        if not tr.exists(): errors.append(f'{pid}: missing {tr.relative_to(ROOT)}')
        if scen.exists():
            data=yaml.safe_load(scen.read_text(encoding='utf-8')) or {}
            if data.get('scenario_id')!=sid: errors.append(f'{pid}/{sid}: scenario_id mismatch')
            if 'not a default' not in data.get('visibility','').lower(): errors.append(f'{pid}/{sid}: missing non-default visibility')
            if not data.get('selected_skills'): errors.append(f'{pid}/{sid}: missing selected_skills')
            if not data.get('selected_modules',{}).get('suite_router'): errors.append(f'{pid}/{sid}: missing suite_router')
            if not data.get('reviewer_risk_checklist'): errors.append(f'{pid}/{sid}: missing reviewer risk checklist')
            if not data.get('structured_output_contract'): errors.append(f'{pid}/{sid}: missing structured output contract')
        if sample.exists():
            txt=sample.read_text(encoding='utf-8').lower()
            for phrase in ['selected skills/modules','official-source warning','copyright-safe paper-mining warning','reviewer-risk checklist','structured output contract']:
                if phrase not in txt: errors.append(f'{pid}/{sid}: sample missing {phrase}')
        if tr.exists():
            data=json.loads(tr.read_text(encoding='utf-8'))
            if not data.get('steps'): errors.append(f'{pid}/{sid}: route trace missing steps')
            if 'not a default' not in data.get('visibility_policy','').lower(): errors.append(f'{pid}/{sid}: route trace missing visibility')
    rows.append({'preset':pid,'scenarios':sum((base/'scenarios'/f'{s}.yaml').exists() for s in SCENARIOS),'sample_outputs':sum((base/'sample-outputs'/f'{s}.md').exists() for s in SCENARIOS),'route_traces':sum((base/'route-traces'/f'{s}.json').exists() for s in SCENARIOS)})
for rel in ['resources/preset_eval_report.json','resources/preset_eval_report.yaml','resources/preset_route_trace_index.json','resources/preset_route_trace_index.yaml']:
    if not (ROOT/rel).exists(): errors.append(f'missing {rel}')
print(json.dumps({'preset_scenarios':rows,'errors':errors,'passed':not errors}, indent=2))
if errors: sys.exit(1)
