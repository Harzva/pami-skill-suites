#!/usr/bin/env python3
from pathlib import Path
import json, sys, re, hashlib
try:
    import yaml
except Exception:
    yaml = None
ROOT = Path(__file__).resolve().parents[1]
PT = ROOT / 'paper_templates'
REQ_CARD_FIELDS = [
    'Title','Journal','Year','DOI','License','Source URL','Local PDF path','Why included',
    'Abstract pattern','Introduction pattern','Related work pattern','Method pattern','Experiment pattern',
    'Table style','Figure style','Caption style','Limitations style','Reusable lessons','Copyright note'
]
ALLOWED = ['creative commons', 'cc by', 'cc by-nc', 'official template', 'official publisher', 'latex documentation', 'ctan']
BAD = ['sci-hub','scihub','libgen','z-library','annas-archive']
errs=[]
json_path = PT / 'corpus_manifest.json'
yaml_path = PT / 'corpus_manifest.yaml'
if not json_path.exists(): errs.append('missing paper_templates/corpus_manifest.json')
if not yaml_path.exists(): errs.append('missing paper_templates/corpus_manifest.yaml')
data = {}
if json_path.exists():
    data = json.loads(json_path.read_text(encoding='utf-8'))
entries = data.get('entries', [])
if not entries: errs.append('corpus_manifest has no entries')
for e in entries:
    eid = e.get('id','')
    src = (e.get('source_url') or '').lower()
    lic = (e.get('license') or '').lower()
    if any(b in src for b in BAD): errs.append(f'{eid}: prohibited source URL')
    if not any(a in lic for a in ALLOWED): errs.append(f'{eid}: license/source type not allowed: {e.get("license")}')
    rel = e.get('local_pdf_path') or e.get('file')
    if rel and not (PT/rel).exists(): errs.append(f'{eid}: missing PDF {rel}')
    card = PT / 'cards' / f'{eid}.md'
    if not card.exists():
        errs.append(f'{eid}: missing card')
    else:
        txt = card.read_text(encoding='utf-8', errors='ignore')
        for field in REQ_CARD_FIELDS:
            if field not in txt: errs.append(f'{eid}: card missing {field}')
        if 'Do not copy text' not in txt and 'Do not copy' not in txt:
            errs.append(f'{eid}: card missing copyright safety warning')
    smap = PT / 'extracted_structure_maps' / f'{eid}.md'
    if not smap.exists(): errs.append(f'{eid}: missing extracted structure map')
for note in ['abstract-patterns.md','introduction-patterns.md','related-work-patterns.md','method-patterns.md','experiment-patterns.md','table-patterns.md','figure-patterns.md','caption-patterns.md','limitations-patterns.md']:
    if not (PT/'mining_notes'/note).exists(): errs.append(f'missing mining note {note}')
print(json.dumps({'entries': len(entries), 'errors': errs}, indent=2))
if errs: sys.exit(1)
