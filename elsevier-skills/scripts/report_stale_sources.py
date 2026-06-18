#!/usr/bin/env python3
"""Summarize source records that need reverification."""
from pathlib import Path
import json, datetime
try:
    import yaml
except Exception:
    yaml=None
ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/'resources'/'source_refresh_report.json'
OUT_MD=ROOT/'resources'/'stale_source_report.md'
OUT_JSON=ROOT/'resources'/'stale_source_report.json'

def main():
    data=json.loads(REPORT.read_text(encoding='utf-8')) if REPORT.exists() else {'records':[],'summary':{}}
    stale=[r for r in data.get('records',[]) if r.get('needs_reverification') or r.get('status') not in {'healthy'}]
    out={'generated_at': datetime.date.today().isoformat(), 'publisher': data.get('publisher'), 'stale_count': len(stale), 'records': stale}
    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')
    lines=[f"# Stale Source Report", "", f"Generated: {out['generated_at']}", f"Publisher: {out.get('publisher')}", f"Records needing reverification: {len(stale)}", ""]
    lines.append('| Scope | Owner | Field | Status | URL |')
    lines.append('|---|---|---|---|---|')
    for r in stale[:500]:
        lines.append(f"| {r.get('scope','')} | {r.get('owner','')} | {r.get('field','')} | {r.get('status','')} | {r.get('url','')} |")
    OUT_MD.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(json.dumps({'stale_count': len(stale), 'output': str(OUT_MD.relative_to(ROOT))}, indent=2))

if __name__ == '__main__':
    main()
