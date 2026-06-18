#!/usr/bin/env python3
"""Print a concise source-review report for maintainers."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
report=json.loads((ROOT/'resources/source_review_report.json').read_text(encoding='utf-8'))
queue=json.loads((ROOT/'resources/human_review_queue.json').read_text(encoding='utf-8'))
out={
 'repository': ROOT.name,
 'release_version': report.get('release_version'),
 'queue_summary': queue.get('summary'),
 'categories': {k:v.get('count') for k,v in queue.get('review_categories',{}).items()},
 'next_actions': report.get('recommended_next_actions',[]),
}
print(json.dumps(out, indent=2, ensure_ascii=False))
