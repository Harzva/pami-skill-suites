#!/usr/bin/env python3
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
errs=[]
if not (ROOT/'skills').exists(): errs.append('missing skills')
for forbidden in ['presets','expansion_packs','skills-advanced']:
    if (ROOT/'skills'/forbidden).exists(): errs.append(f'{forbidden} must not be default-visible')
macro=[p.name for p in (ROOT/'skills').iterdir() if p.is_dir() and p.name!='_shared'] if (ROOT/'skills').exists() else []
if len(macro)>10: errs.append(f'too many default skills: {len(macro)}')
for rel in ['presets','resources/preset_eval_report.json','resources/preset_route_trace_index.json','resources/release_health_dashboard.json','resources/live_source_check_matrix.json','resources/source_badges.json','resources/source_trust_tiers.json','resources/human_review_queue.json','resources/source_review_report.json']:
    if not (ROOT/rel).exists(): errs.append(f'missing {rel}')
print(json.dumps({'script':Path(__file__).name,'default_macro_skills':len(macro),'errors':errs,'passed':not errs},indent=2))
sys.exit(1 if errs else 0)
