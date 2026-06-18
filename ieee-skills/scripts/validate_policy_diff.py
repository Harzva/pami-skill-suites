#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
required=['resources/source_snapshots/latest.json','resources/policy_diff_report.json','resources/policy_diff_report.yaml','resources/official_source_change_log.json','resources/official_source_change_log.yaml','resources/affected_fragments_report.json','resources/affected_fragments_report.yaml','scripts/snapshot_official_sources.py','scripts/diff_source_snapshots.py','scripts/policy_diff_report.py','scripts/affected_fragments.py','docs/policy-diff-dashboard.html','docs/source-snapshots.html','docs/affected-fragments.html']
errs=[r for r in required if not (ROOT/r).exists()]
# Validate baseline warning exists.
try:
    rep=json.loads((ROOT/'resources/policy_diff_report.json').read_text(encoding='utf-8'))
    if 'live_verification_warning' not in rep: errs.append('policy_diff_report missing live_verification_warning')
except Exception as e: errs.append(f'policy_diff_report invalid: {e}')
print(json.dumps({'script':'validate_policy_diff.py','errors':errs,'passed':not errs},indent=2))
sys.exit(1 if errs else 0)
