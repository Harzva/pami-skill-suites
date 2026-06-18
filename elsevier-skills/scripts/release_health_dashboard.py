#!/usr/bin/env python3
"""Generate a release health dashboard for the journal skill-suite repository."""
from pathlib import Path
import json, datetime, zipfile
try:
    import yaml
except Exception:
    yaml = None
ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT/'resources'/'release_health_dashboard.json'
OUT_YAML = ROOT/'resources'/'release_health_dashboard.yaml'


def load_json(rel, default):
    p = ROOT/rel
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else default


def safe_count_dir(rel):
    p = ROOT/rel
    return len([x for x in p.iterdir() if x.is_dir() and x.name != '_shared']) if p.exists() else 0


def zip_health():
    out=[]
    dist=ROOT/'dist'
    for zpath in sorted(dist.glob('*.zip')) if dist.exists() else []:
        ok=True; bad=None
        try:
            with zipfile.ZipFile(zpath) as z:
                bad=z.testzip()
                ok=bad is None
        except Exception as e:
            ok=False; bad=str(e)
        out.append({'name': zpath.name, 'size_bytes': zpath.stat().st_size, 'ok': ok, 'bad_member': bad})
    return out


def main():
    version = (ROOT/'VERSION').read_text(encoding='utf-8').strip() if (ROOT/'VERSION').exists() else 'unknown'
    source_matrix = load_json('resources/live_source_check_matrix.json', {'summary':{}})
    age = load_json('resources/source_age_policy_report.json', {'summary':{}})
    eval_report = load_json('resources/preset_eval_report.json', {'summary':{}})
    preset_registry = load_json('resources/preset_registry.json', {'presets':[]})
    coverage = load_json('resources/journal_coverage_dashboard.json', {'summary':{}})
    source_trust = load_json('resources/source_trust_tiers.json', {'summary':{}})
    human_review = load_json('resources/human_review_queue.json', {'summary':{}})
    source_records = source_matrix.get('summary', {})
    dist = zip_health()
    default_macro = safe_count_dir('skills')
    advanced = sum(1 for _ in (ROOT/'skills-advanced').rglob('SKILL.md')) if (ROOT/'skills-advanced').exists() else 0
    status = 'offline-maintenance-ready'
    if default_macro > 10:
        status = 'attention-required-context-budget'
    dashboard = {
        'dashboard_version':'1.7.0',
        'generated_at': datetime.date.today().isoformat(),
        'repository': ROOT.name,
        'version': version,
        'overall_status': status,
        'context_safety': {
            'default_macro_skills': default_macro,
            'max_allowed_default_macro_skills': 10,
            'advanced_skills_not_default_visible': not (ROOT/'skills'/'skills-advanced').exists(),
            'expansion_packs_not_default_visible': not (ROOT/'skills'/'expansion_packs').exists(),
            'presets_not_default_visible': not (ROOT/'skills'/'presets').exists(),
        },
        'source_health': {
            'total_records': source_records.get('total_records',0),
            'unique_urls': source_records.get('unique_urls',0),
            'healthy': source_records.get('healthy',0),
            'needs_reverification': source_records.get('needs_reverification',0),
            'unchecked': source_records.get('unchecked',0),
            'stale': source_records.get('stale',0),
            'policy_note':'Offline release builds may be maintenance-ready while source records remain unchecked; run live checks before relying on mutable publication details.',
        },
        'source_aging': age.get('summary', {}),
        'source_trust': {
            'enabled': True,
            'tier_counts': source_trust.get('summary',{}).get('tier_counts',{}),
            'records': source_trust.get('summary',{}).get('records',0),
            'records_needing_reverification': source_trust.get('summary',{}).get('records_needing_reverification',0),
        },
        'human_review_queue': {
            'enabled': True,
            **human_review.get('summary',{}),
            'queue_file': 'resources/human_review_queue.json',
        },
        'coverage': coverage.get('summary', coverage.get('maturity_counts', {})),
        'presets': {
            'count': len(preset_registry.get('presets', [])) if isinstance(preset_registry.get('presets', []), list) else 0,
            'eval_summary': eval_report.get('summary', {}),
        },
        'distribution': {
            'zip_count': len(dist),
            'all_zip_integrity_ok': all(d.get('ok') for d in dist),
            'zips': dist,
        },
        'recommended_maintenance_commands': [
            'python scripts/check_official_links_live.py --live',
            'python scripts/report_stale_sources.py',
            'python scripts/live_source_check_matrix.py',
            'python scripts/source_age_policy.py',
            'python scripts/generate_source_badges.py',
            'python scripts/release_health_dashboard.py',
            'python scripts/classify_source_trust.py',
            'python scripts/build_human_review_queue.py',
            'python scripts/validate_source_trust.py',
        ],
    }
    OUT_JSON.write_text(json.dumps(dashboard, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    if yaml:
        OUT_YAML.write_text(yaml.safe_dump(dashboard, sort_keys=False, allow_unicode=True), encoding='utf-8')
    else:
        OUT_YAML.write_text(json.dumps(dashboard, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps({'repository':ROOT.name,'overall_status':status,'default_macro_skills':default_macro,'dist_zip_count':len(dist),'source_records':source_records.get('total_records',0)}, indent=2))

if __name__ == '__main__':
    main()
