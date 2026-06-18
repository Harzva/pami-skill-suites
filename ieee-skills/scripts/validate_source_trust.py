#!/usr/bin/env python3
"""Validate v1.7 source trust and human review artifacts."""
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
required=[
 'resources/source_trust_tiers.json','resources/source_trust_tiers.yaml',
 'resources/human_review_queue.json','resources/human_review_queue.yaml',
 'resources/source_review_report.json','resources/source_review_report.yaml',
 'scripts/classify_source_trust.py','scripts/build_human_review_queue.py','scripts/review_queue_report.py',
 'docs/source-trust-tiers.html','docs/human-review-queue.html','docs/source-review-workflow.html'
]
tiers=['publisher-official','journal-official','society-official','repository-best-practice','template-paper-observation','unverified-candidate']
errs=[]
for rel in required:
    if not (ROOT/rel).exists(): errs.append(f'missing {rel}')
try:
    trust=json.loads((ROOT/'resources/source_trust_tiers.json').read_text(encoding='utf-8'))
    for t in tiers:
        if t not in trust.get('tiers',{}): errs.append(f'missing trust tier {t}')
    if not trust.get('records'): errs.append('source trust records empty')
    if sum(trust.get('summary',{}).get('tier_counts',{}).values()) != len(trust.get('records',[])): errs.append('tier counts do not match record count')
except Exception as e: errs.append(f'bad source_trust_tiers.json: {e}')
try:
    q=json.loads((ROOT/'resources/human_review_queue.json').read_text(encoding='utf-8'))
    for c in ['high-risk mutable links','stale official links','missing author-instruction links','missing copyright/license links','missing AI disclosure links','L0/L1 expansion-pack candidates']:
        if c not in q.get('review_categories',{}): errs.append(f'missing queue category {c}')
    if q.get('summary',{}).get('total_queue_items',0) != len(q.get('queue',[])): errs.append('queue item count mismatch')
except Exception as e: errs.append(f'bad human_review_queue.json: {e}')
macro=[p.name for p in (ROOT/'skills').iterdir() if p.is_dir() and p.name!='_shared'] if (ROOT/'skills').exists() else []
if len(macro)>10: errs.append(f'too many default macro skills: {len(macro)}')
for forbidden in ['skills-advanced','expansion_packs','presets']:
    if (ROOT/'skills'/forbidden).exists(): errs.append(f'{forbidden} must not be default-visible')
print(json.dumps({'script':Path(__file__).name,'default_macro_skills':len(macro),'errors':errs,'passed':not errs}, indent=2))
sys.exit(1 if errs else 0)
