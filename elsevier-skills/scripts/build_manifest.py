#!/usr/bin/env python3
from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parents[1]
version=(ROOT/'VERSION').read_text(encoding='utf-8').strip() if (ROOT/'VERSION').exists() else 'v2.7.0'
def desc(p):
    txt=(p/'SKILL.md').read_text(encoding='utf-8', errors='ignore') if (p/'SKILL.md').exists() else ''
    m=re.search(r'^description:\s*["\']?(.+?)["\']?\s*$', txt, re.M)
    return m.group(1).strip() if m else ''
data={
    'version': version,
    'release_version': version,
    'updated_for': 'RAG Trace UI + Visual Query Debugger',
    'default_skills': [],
    'advanced_counts': {},
    'fragments': {},
    'paper_corpus': {},
    'evals': {}
}
for p in sorted((ROOT/'skills').iterdir()):
    if p.is_dir() and p.name != '_shared' and (p/'SKILL.md').exists():
        data['default_skills'].append({'name':p.name,'description':desc(p)})
adv=ROOT/'skills-advanced'
if adv.exists():
    for cat in ['journals','components','submission','routers','core']:
        data['advanced_counts'][cat]=len([p for p in (adv/cat).iterdir() if p.is_dir()]) if (adv/cat).exists() else 0
for suite in [p for p in (ROOT/'skills').iterdir() if p.is_dir() and p.name.endswith('skill-suite')]:
    data['fragments'][suite.name]={}
    for cat in ['journals','components','submission']:
        d=suite/'static'/cat
        data['fragments'][suite.name][cat]=len(list(d.glob('*.md'))) if d.exists() else 0
cm=ROOT/'paper_templates'/'corpus_manifest.json'
if cm.exists():
    corpus=json.loads(cm.read_text(encoding='utf-8'))
    data['paper_corpus']={'entries':len(corpus.get('entries',[])), 'open_access_papers':sum(1 for e in corpus.get('entries',[]) if e.get('type')=='open_access_paper'), 'official_templates':sum(1 for e in corpus.get('entries',[]) if e.get('type')=='official_template')}

evals=ROOT/'evals'
if evals.exists():
    data['evals']={
        'tasks':len(list((evals/'tasks').glob('*.yaml'))) if (evals/'tasks').exists() else 0,
        'rubrics':len(list((evals/'rubrics').glob('*.md'))) if (evals/'rubrics').exists() else 0,
        'sample_outputs':len(list((evals/'sample_outputs').glob('*.md'))) if (evals/'sample_outputs').exists() else 0,
        'manifest':'evals/benchmark_manifest.yaml'
    }

(ROOT/'skill_manifest.json').write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
print(json.dumps(data, indent=2, ensure_ascii=False))
