#!/usr/bin/env python3
"""Validate v1.6 release-health artifacts."""
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
required=[
 'resources/live_source_check_matrix.json','resources/live_source_check_matrix.yaml',
 'resources/source_age_policy_report.json','resources/source_age_policy_report.yaml',
 'resources/release_health_dashboard.json','resources/release_health_dashboard.yaml',
 'resources/source_badges.json','resources/source_badges.yaml',
 '.github/workflows/source-refresh.yml',
 'docs/release-health-dashboard.html','docs/source-aging-policy.html','docs/live-source-checks.html',
]
errs=[]
for rel in required:
    if not (ROOT/rel).exists(): errs.append(f'missing {rel}')
try:
    dash=json.loads((ROOT/'resources/release_health_dashboard.json').read_text(encoding='utf-8'))
    if dash.get('context_safety',{}).get('default_macro_skills',99)>10: errs.append('default macro skills exceed context budget')
    if (ROOT/'skills'/'presets').exists(): errs.append('presets exposed under default skills')
    if (ROOT/'skills'/'expansion_packs').exists(): errs.append('expansion packs exposed under default skills')
except Exception as e:
    errs.append(f'bad release dashboard: {e}')
try:
    badges=json.loads((ROOT/'resources/source_badges.json').read_text(encoding='utf-8'))
    if 'badges' not in badges or 'source_status' not in badges['badges']: errs.append('source badge data incomplete')
except Exception as e:
    errs.append(f'bad source badges: {e}')
print(json.dumps({'script':Path(__file__).name,'errors':errs,'passed':not errs},indent=2))
sys.exit(1 if errs else 0)
