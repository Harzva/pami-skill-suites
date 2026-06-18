#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
required=[
 'scripts/context_budget.py','scripts/validate_manifest.py','scripts/validate_routes.py','scripts/validate_sources.py',
 'scripts/validate_official_links.py','scripts/validate_live_verification_warnings.py',
 'scripts/live_source_check_matrix.py','scripts/source_age_policy.py','scripts/generate_source_badges.py','scripts/release_health_dashboard.py','scripts/validate_release_health.py',
 'scripts/validate_structure.py','scripts/validate_paper_corpus.py','scripts/validate_evals.py','scripts/run_evals.py',
 'scripts/validate_distribution.py','scripts/quality_score.py','scripts/validate_preset_scenarios.py','scripts/run_preset_evals.py',
 'resources/live_source_check_matrix.json','resources/source_age_policy_report.json','resources/release_health_dashboard.json','resources/source_badges.json',
 'docs/live-source-checks.html','docs/source-aging-policy.html','docs/release-health-dashboard.html'
]
errs=[]
for rel in required:
    if not (ROOT/rel).exists(): errs.append(f'missing {rel}')
macro=[p.name for p in (ROOT/'skills').iterdir() if p.is_dir() and p.name!='_shared'] if (ROOT/'skills').exists() else []
if len(macro)>10: errs.append(f'too many default macro skills: {len(macro)}')
for forbidden in ['skills-advanced','expansion_packs','presets']:
    if (ROOT/'skills'/forbidden).exists(): errs.append(f'{forbidden} exposed in default skills')
out={'smoke_tests':'static release-gate asset check','default_macro_skills':len(macro),'errors':errs,'passed':not errs}
print(json.dumps(out,indent=2))
sys.exit(1 if errs else 0)
