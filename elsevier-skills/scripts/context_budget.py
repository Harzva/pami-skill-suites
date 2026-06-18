#!/usr/bin/env python3
from pathlib import Path
import re, sys, json
ROOT = Path(__file__).resolve().parents[1]
MAX_SKILLS=10; MAX_DESC=350; MAX_TOTAL=3000
skills_dir=ROOT/'skills'
def desc_of(p):
    txt=(p/'SKILL.md').read_text(encoding='utf-8', errors='ignore') if (p/'SKILL.md').exists() else ''
    m=re.search(r'^description:\s*["\']?(.+?)["\']?\s*$', txt, re.M)
    return m.group(1).strip() if m else ''
skills=[p for p in skills_dir.iterdir() if p.is_dir() and p.name != '_shared' and (p/'SKILL.md').exists()]
rows=[{'name':p.name,'description_chars':len(desc_of(p))} for p in skills]
total=sum(r['description_chars'] for r in rows)
errors=[]
if len(skills)>MAX_SKILLS: errors.append(f'default skill count {len(skills)} > {MAX_SKILLS}')
for r in rows:
    if r['description_chars']>MAX_DESC: errors.append(f"{r['name']} description {r['description_chars']} > {MAX_DESC}")
if total>MAX_TOTAL: errors.append(f'total description budget {total} > {MAX_TOTAL}')
print(json.dumps({'default_skill_count':len(skills),'total_description_chars':total,'skills':rows,'errors':errors}, indent=2))
if errors: sys.exit(1)
