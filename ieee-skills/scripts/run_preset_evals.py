#!/usr/bin/env python3
from pathlib import Path
import json,yaml,sys
ROOT=Path(__file__).resolve().parents[1]; PRESETS=['computer-vision','medical-ai','remote-sensing','multimedia','data-mining','signal-processing']; reps=[]
for pid in PRESETS:
 p=ROOT/'presets'/pid; sc=list((p/'scenarios').glob('*.yaml')); sm=list((p/'sample-outputs').glob('*.md')); tr=list((p/'route-traces').glob('*.json')); status='passed' if len(sc)>=3 and len(sm)>=3 and len(tr)>=3 else 'failed'; reps.append({'preset_id':pid,'scenario_count':len(sc),'sample_output_count':len(sm),'route_trace_count':len(tr),'status':status})
report={'release_version':(ROOT/'VERSION').read_text().strip() if (ROOT/'VERSION').exists() else 'unknown','summary':{'preset_count':len(reps),'scenario_count':sum(x['scenario_count'] for x in reps),'sample_output_count':sum(x['sample_output_count'] for x in reps),'route_trace_count':sum(x['route_trace_count'] for x in reps),'passed':all(x['status']=='passed' for x in reps)},'presets':reps,'errors':[]}
(ROOT/'resources/preset_eval_report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8'); (ROOT/'resources/preset_eval_report.yaml').write_text(yaml.safe_dump(report,sort_keys=False,allow_unicode=True),encoding='utf-8'); print(json.dumps(report,indent=2,ensure_ascii=False)); sys.exit(0 if report['summary']['passed'] else 1)
