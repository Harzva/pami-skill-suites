#!/usr/bin/env python3
"""Generate source-verification badge data for README/GitHub Pages."""
from pathlib import Path
import json, datetime
try:
    import yaml
except Exception:
    yaml = None
ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT/'resources'/'live_source_check_matrix.json'
DASH = ROOT/'resources'/'release_health_dashboard.json'
OUT_JSON = ROOT/'resources'/'source_badges.json'
OUT_YAML = ROOT/'resources'/'source_badges.yaml'


def load(path, default):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default


def badge(label, message, color):
    return {'schemaVersion':1, 'label':label, 'message':message, 'color':color}


def main():
    matrix=load(MATRIX, {'summary':{}})
    dash=load(DASH, {'overall_status':'unknown','context_safety':{},'distribution':{}})
    trust=load(ROOT/'resources'/'source_trust_tiers.json', {'summary':{}})
    queue=load(ROOT/'resources'/'human_review_queue.json', {'summary':{}})
    s=matrix.get('summary', {})
    total=s.get('total_records',0); needs=s.get('needs_reverification',0); healthy=s.get('healthy',0)
    if total and healthy == total:
        source_msg='verified'; source_color='brightgreen'
    elif total and needs == total:
        source_msg='pending live check'; source_color='yellow'
    else:
        source_msg=f'{healthy}/{total} healthy'; source_color='orange'
    context_ok = dash.get('context_safety',{}).get('default_macro_skills', 999) <= dash.get('context_safety',{}).get('max_allowed_default_macro_skills',10)
    dist_ok = dash.get('distribution',{}).get('all_zip_integrity_ok', False)
    badges={
        'generated_at': datetime.date.today().isoformat(),
        'badges': {
            'source_status': badge('official sources', source_msg, source_color),
            'context_safety': badge('context safety', 'compact' if context_ok else 'review', 'brightgreen' if context_ok else 'red'),
            'distribution': badge('dist zips', 'ok' if dist_ok else 'review', 'brightgreen' if dist_ok else 'red'),
            'live_check_policy': badge('live check', 'required before submission', 'blue'),
            'source_trust': badge('source trust', 'human review queue', 'blueviolet' if trust.get('summary') else 'lightgrey'),
            'human_review': badge('human review', f"{queue.get('summary',{}).get('total_queue_items',0)} queued", 'orange'),
        },
        'markdown_examples': {
            'source_status': '![official sources](https://img.shields.io/badge/official%20sources-pending%20live%20check-yellow)',
            'context_safety': '![context safety](https://img.shields.io/badge/context%20safety-compact-brightgreen)',
            'live_check_policy': '![live check](https://img.shields.io/badge/live%20check-required%20before%20submission-blue)',
            'source_trust': '![source trust](https://img.shields.io/badge/source%20trust-human%20review%20queue-blueviolet)',
            'human_review': '![human review](https://img.shields.io/badge/human%20review-queue%20generated-orange)',
        }
    }
    OUT_JSON.write_text(json.dumps(badges, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    if yaml:
        OUT_YAML.write_text(yaml.safe_dump(badges, sort_keys=False, allow_unicode=True), encoding='utf-8')
    else:
        OUT_YAML.write_text(json.dumps(badges, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps({'source_status':source_msg,'context_ok':context_ok,'dist_ok':dist_ok}, indent=2))

if __name__ == '__main__':
    main()
