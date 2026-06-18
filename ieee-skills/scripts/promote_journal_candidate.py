#!/usr/bin/env python3
from pathlib import Path
import argparse, yaml, json, re, sys
ROOT=Path(__file__).resolve().parents[1]
def slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
parser=argparse.ArgumentParser(description='Create a staged journal-fragment draft from an expansion-pack candidate. Does not modify default skills/.')
parser.add_argument('--pack', required=True)
parser.add_argument('--journal-id', required=True)
parser.add_argument('--target-level', default='L3')
parser.add_argument('--apply', action='store_true', help='reserved for future use; current script still stages only')
args=parser.parse_args()
pack=ROOT/'expansion_packs'/args.pack/'journals.yaml'
if not pack.exists(): raise SystemExit(f'missing pack: {pack}')
data=yaml.safe_load(pack.read_text()) or {}
match=None
for j in data.get('journals',[]):
    if j.get('id')==args.journal_id: match=j; break
if not match: raise SystemExit(f'journal not found: {args.journal_id}')
outdir=ROOT/'resources/promoted_fragments_staging'/args.pack
outdir.mkdir(parents=True, exist_ok=True)
out=outdir/f"{slug(match.get('id') or match.get('title'))}.md"
content=f"""# Draft Journal Fragment: {match.get('title')}

> Staging draft for official-source review only.
> Do not add this file to default `skills/`. Import only after official-source verification.

## Journal identity

- ID: {match.get('id')}
- Title: {match.get('title')}
- Source expansion pack: {args.pack}
- Current maturity: {match.get('maturity_level')}
- Target maturity: {args.target_level}

## Official Source Matrix TODO

- Journal homepage: Not verified yet
- Author instructions / Guide for Authors: Not verified yet
- Submission system: Not verified yet
- Manuscript template: Not verified yet
- Publishing agreement: Not verified yet
- Copyright / license: Not verified yet
- Open access: Not verified yet
- Ethics / integrity: Not verified yet
- AI disclosure policy: Not verified yet
- Data / code availability: Not verified yet
- Permissions: Not verified yet

## Required checks before promotion

1. Populate the full official-source matrix.
2. Run `python scripts/check_official_links_live.py --live`.
3. Add source-refresh metadata.
4. Add `Live verification required before submission` warning.
5. Run `python scripts/validate_pack_maturity.py`.
6. Keep the fragment inside `skill-suite/static/journals/` or optional `skills-advanced/`; never add it as a default macro skill.

## Context safety

Promotion must not increase the default top-level skill listing.
"""
out.write_text(content)
manifest=outdir/f"{slug(match.get('id') or match.get('title'))}.promotion.json"
manifest.write_text(json.dumps({'pack':args.pack,'journal_id':args.journal_id,'title':match.get('title'),'staged_fragment':str(out.relative_to(ROOT)),'target_level':args.target_level,'default_skill_exposure':'forbidden','needs_official_verification':True},indent=2)+'\n')
print(json.dumps({'staged_fragment':str(out.relative_to(ROOT)),'manifest':str(manifest.relative_to(ROOT)),'default_skill_exposure':'forbidden'},indent=2))
