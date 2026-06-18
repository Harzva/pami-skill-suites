#!/usr/bin/env python3
"""Build a live-source check matrix from the official source registry and latest refresh report.

This script is offline-safe by default. It does not perform HTTP requests. It consolidates
publisher and journal URL records, latest dry-run/live statuses, age policy buckets, and
maintenance recommendations into resources/live_source_check_matrix.*.
"""
from pathlib import Path
import json, datetime, argparse
try:
    import yaml
except Exception:
    yaml = None
ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT/'resources'/'official_source_registry.json'
REFRESH = ROOT/'resources'/'source_refresh_report.json'
OUT_JSON = ROOT/'resources'/'live_source_check_matrix.json'
OUT_YAML = ROOT/'resources'/'live_source_check_matrix.yaml'

MUTABLE_FIELDS = {'author_instructions','submission_system','manuscript_template','publishing_agreement','copyright_license','open_access','ethics_integrity','ai_disclosure_policy','data_code_availability','permissions','guide_for_authors','publication_fee','apc','page_limits'}


def load_json(path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding='utf-8'))


def iter_registry_records(registry):
    # Publisher-wide sources
    publisher = registry.get('publisher') or 'publisher'
    for field, url in (registry.get('publisher_common_sources') or {}).items():
        if isinstance(url, str) and url.startswith(('http://','https://')):
            yield {
                'scope':'publisher_common_source', 'owner':publisher, 'field':field,
                'url':url, 'source_tier':'publisher official rule'
            }
    # Journal-specific fields
    for journal in registry.get('journals', []) or []:
        owner = journal.get('id') or journal.get('title') or 'journal'
        title = journal.get('title') or owner
        for field, url in (journal.get('fields') or {}).items():
            if isinstance(url, str) and url.startswith(('http://','https://')):
                tier = 'journal official rule' if field in {'journal_homepage','homepage','xplore','science_direct','scope','author_instructions','guide_for_authors'} else 'publisher official rule'
                yield {
                    'scope':'journal_source', 'owner':owner, 'journal_title':title, 'field':field,
                    'url':url, 'source_tier':tier
                }


def refresh_index(refresh):
    idx = {}
    for rec in refresh.get('records', []) or []:
        idx[(rec.get('scope'), rec.get('owner'), rec.get('field'), rec.get('url'))] = rec
        idx[(rec.get('url'))] = rec
    return idx


def age_bucket(last_checked):
    if not last_checked or str(last_checked).startswith('not-run') or str(last_checked).lower() in {'unknown','not checked','none'}:
        return {'bucket':'unchecked', 'age_days':None, 'policy':'live verification required'}
    try:
        d = datetime.date.fromisoformat(str(last_checked)[:10])
        age = (datetime.date.today() - d).days
    except Exception:
        return {'bucket':'unknown', 'age_days':None, 'policy':'live verification required'}
    if age <= 90:
        return {'bucket':'fresh', 'age_days':age, 'policy':'acceptable for repository maintenance; verify before real submission'}
    if age <= 180:
        return {'bucket':'aging', 'age_days':age, 'policy':'refresh recommended'}
    return {'bucket':'stale', 'age_days':age, 'policy':'refresh required'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fail-on-stale', action='store_true', help='exit nonzero if any source is stale or unchecked')
    args = ap.parse_args()
    registry = load_json(REGISTRY, {})
    refresh = load_json(REFRESH, {'records':[], 'summary':{}, 'mode':'missing'})
    idx = refresh_index(refresh)
    rows = []
    for base in iter_registry_records(registry):
        rec = idx.get((base['scope'], base['owner'], base['field'], base['url'])) or idx.get(base['url']) or {}
        last = rec.get('last_live_checked') or 'not-run-in-release-build'
        status = rec.get('status') or 'not_checked'
        age = age_bucket(last)
        mutable = base['field'] in MUTABLE_FIELDS or base['scope'] == 'journal_source'
        rows.append({
            **base,
            'status': status,
            'ok': rec.get('ok'),
            'http_status': rec.get('http_status'),
            'last_live_checked': last,
            'age_days': age['age_days'],
            'age_bucket': age['bucket'],
            'source_policy': age['policy'],
            'mutable_publication_detail': bool(mutable),
            'needs_reverification': bool(rec.get('needs_reverification', True)) or age['bucket'] in {'unchecked','unknown','stale'},
            'maintenance_action': 'run live check before real submission advice' if age['bucket'] in {'unchecked','unknown','stale'} else 'monitor',
        })
    summary = {
        'publisher': registry.get('publisher'),
        'generated_at': datetime.date.today().isoformat(),
        'source_refresh_mode': refresh.get('mode','unknown'),
        'total_records': len(rows),
        'unique_urls': len({r['url'] for r in rows}),
        'healthy': sum(1 for r in rows if r.get('ok') is True),
        'needs_reverification': sum(1 for r in rows if r.get('needs_reverification')),
        'unchecked': sum(1 for r in rows if r.get('age_bucket') == 'unchecked'),
        'stale': sum(1 for r in rows if r.get('age_bucket') == 'stale'),
        'mutable_records': sum(1 for r in rows if r.get('mutable_publication_detail')),
    }
    out = {
        'matrix_version':'1.6.0',
        'offline_safe_policy':'This matrix is generated from registry and refresh-report data. It does not imply live health unless check_official_links_live.py --live has been run.',
        'age_policy': {
            'fresh':'0-90 days since live check',
            'aging':'91-180 days since live check',
            'stale':'>180 days since live check',
            'unchecked':'no live check recorded',
        },
        'summary': summary,
        'records': rows,
    }
    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    if yaml:
        OUT_YAML.write_text(yaml.safe_dump(out, sort_keys=False, allow_unicode=True), encoding='utf-8')
    else:
        OUT_YAML.write_text(json.dumps(out, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    if args.fail_on_stale and summary['needs_reverification']:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
