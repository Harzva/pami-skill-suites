#!/usr/bin/env python3
"""Apply a conservative source-aging policy to official-source records.

Outputs resources/source_age_policy_report.*. This is a maintenance signal only; it does
not replace live publisher/journal verification before real submission advice.
"""
from pathlib import Path
import json, datetime, argparse
try:
    import yaml
except Exception:
    yaml = None
ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT/'resources'/'live_source_check_matrix.json'
OUT_JSON = ROOT/'resources'/'source_age_policy_report.json'
OUT_YAML = ROOT/'resources'/'source_age_policy_report.yaml'


def load(path):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'records':[], 'summary':{}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--max-unchecked-ratio', type=float, default=1.0, help='advisory threshold; release builds may allow 1.0 in offline mode')
    args = ap.parse_args()
    data = load(MATRIX)
    records = data.get('records', [])
    buckets = {}
    actions = {}
    for r in records:
        buckets[r.get('age_bucket','unknown')] = buckets.get(r.get('age_bucket','unknown'),0)+1
        act = r.get('maintenance_action','review')
        actions[act] = actions.get(act,0)+1
    unchecked_ratio = (buckets.get('unchecked',0) / len(records)) if records else 0
    report = {
        'policy_version':'1.6.0',
        'generated_at': datetime.date.today().isoformat(),
        'policy': {
            'fresh':'0-90 days since live check; still verify mutable instructions before real submission.',
            'aging':'91-180 days; refresh recommended.',
            'stale':'>180 days; refresh required before relying on source.',
            'unchecked':'No recorded live check; must be treated as needs reverification.',
        },
        'summary': {
            'total_records': len(records),
            'bucket_counts': buckets,
            'maintenance_actions': actions,
            'unchecked_ratio': round(unchecked_ratio, 4),
            'offline_release_allowed': True,
            'advisory_threshold': args.max_unchecked_ratio,
        },
        'recommendations': [
            'Run scripts/check_official_links_live.py --live in a networked maintenance environment.',
            'Run scripts/live_source_check_matrix.py after live checks to refresh matrix data.',
            'Run scripts/source_age_policy.py and scripts/release_health_dashboard.py before a release.',
            'Do not mark unchecked sources as healthy in an offline release build.',
        ],
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    if yaml:
        OUT_YAML.write_text(yaml.safe_dump(report, sort_keys=False, allow_unicode=True), encoding='utf-8')
    else:
        OUT_YAML.write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps(report['summary'], indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
