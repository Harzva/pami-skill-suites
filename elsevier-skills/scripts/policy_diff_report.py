#!/usr/bin/env python3
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
report=json.loads((ROOT/'resources/policy_diff_report.json').read_text(encoding='utf-8'))
summary=report.get('summary',{})
print(json.dumps({'policy_diff_summary':summary,'mode':report.get('mode'),'warning':report.get('live_verification_warning')},indent=2))
