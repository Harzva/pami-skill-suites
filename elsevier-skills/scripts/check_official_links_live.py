#!/usr/bin/env python3
"""Check official links and refresh resources/source_refresh_report.*.

Default mode is offline-safe dry run. Use --live in a networked environment.
"""
from pathlib import Path
import argparse, json, time, urllib.request, urllib.error, datetime
try:
    import yaml
except Exception:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_JSON = ROOT / 'resources' / 'official_source_registry.json'
REPORT_JSON = ROOT / 'resources' / 'source_refresh_report.json'
REPORT_YAML = ROOT / 'resources' / 'source_refresh_report.yaml'


def load_registry():
    return json.loads(REGISTRY_JSON.read_text(encoding='utf-8'))


def iter_records(data):
    seen = set()
    def add(scope, owner, field, url):
        if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
            return
        key=(scope, owner, field, url)
        if key in seen: return
        seen.add(key)
        yield {'scope': scope, 'owner': owner, 'field': field, 'url': url}
    for k,v in (data.get('publisher_common_sources') or {}).items():
        yield from add('publisher_common_source', data.get('publisher','publisher'), k, v)
    for j in data.get('journals', []) or []:
        owner=j.get('id') or j.get('title') or 'journal'
        for k,v in (j.get('fields') or {}).items():
            yield from add('journal_source', owner, k, v)


def check_url(url, timeout=12):
    req = urllib.request.Request(url, method='HEAD', headers={'User-Agent':'journal-skill-suite-link-check/1.6.0'})
    start=time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return {'ok': 200 <= resp.status < 400, 'http_status': resp.status, 'final_url': resp.geturl(), 'error': None, 'response_time_ms': int((time.time()-start)*1000)}
    except urllib.error.HTTPError as e:
        # Some sites block HEAD; retry GET.
        if e.code in {403,405,429}:
            try:
                req2 = urllib.request.Request(url, method='GET', headers={'User-Agent':'journal-skill-suite-link-check/1.6.0'})
                with urllib.request.urlopen(req2, timeout=timeout) as resp:
                    return {'ok': 200 <= resp.status < 400, 'http_status': resp.status, 'final_url': resp.geturl(), 'error': None, 'response_time_ms': int((time.time()-start)*1000)}
            except Exception as e2:
                return {'ok': False, 'http_status': getattr(e2, 'code', None), 'final_url': None, 'error': str(e2), 'response_time_ms': int((time.time()-start)*1000)}
        return {'ok': False, 'http_status': e.code, 'final_url': None, 'error': str(e), 'response_time_ms': int((time.time()-start)*1000)}
    except Exception as e:
        return {'ok': False, 'http_status': None, 'final_url': None, 'error': str(e), 'response_time_ms': int((time.time()-start)*1000)}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--live', action='store_true', help='perform network checks')
    ap.add_argument('--timeout', type=int, default=12)
    args=ap.parse_args()
    data=load_registry()
    now=datetime.date.today().isoformat()
    out=[]
    for rec in iter_records(data):
        if args.live:
            res=check_url(rec['url'], timeout=args.timeout)
            status='healthy' if res['ok'] else 'warning_or_broken'
            rec.update(res)
        else:
            status='not_checked_dry_run'
            rec.update({'ok': None, 'http_status': None, 'final_url': None, 'error': None, 'response_time_ms': None})
        rec.update({'status': status, 'last_live_checked': now if args.live else 'not-run-dry-run', 'needs_reverification': not bool(rec.get('ok'))})
        out.append(rec)
    report={
        'report_version':'1.6.0',
        'publisher': data.get('publisher'),
        'generated_at': now,
        'mode': 'live' if args.live else 'dry-run',
        'summary': {
            'total_records': len(out),
            'unique_urls': len({r['url'] for r in out}),
            'checked_live': len(out) if args.live else 0,
            'healthy': sum(1 for r in out if r.get('ok') is True),
            'needs_reverification': sum(1 for r in out if r.get('needs_reverification')),
        },
        'records': out,
    }
    REPORT_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
    if yaml:
        REPORT_YAML.write_text(yaml.safe_dump(report, sort_keys=False, allow_unicode=True), encoding='utf-8')
    print(json.dumps(report['summary'], indent=2))

if __name__ == '__main__':
    main()
