#!/usr/bin/env python3
from pathlib import Path
import sys, json, yaml
ROOT=Path(__file__).resolve().parents[1]
PACKS=['computer-vision','medical-ai','remote-sensing','multimedia','data-mining','signal-processing']
LEVELS={'L0','L1','L2','L3','L4'}
errs=[]; rows=[]
base=ROOT/'expansion_packs'
if not base.exists(): errs.append('missing expansion_packs/')
for pack in PACKS:
    d=base/pack
    if not d.exists(): errs.append(f'missing expansion_packs/{pack}/'); continue
    for rel in ['README.md','journals.yaml','fragment_import_manifest.yaml','source_quality_report.json','source_quality_report.md','paper_card_todo.md','promotion_queue.md']:
        if not (d/rel).exists(): errs.append(f'{pack}: missing {rel}')
    try:
        data=yaml.safe_load((d/'journals.yaml').read_text())
        journals=data.get('journals',[])
        if not journals: errs.append(f'{pack}: journals.yaml has no journals')
        for j in journals:
            for key in ['id','title','entry_type','maturity_level','needs_reverification','import_action']:
                if key not in j: errs.append(f'{pack}/{j.get("id","unknown")}: missing {key}')
            if j.get('maturity_level') not in LEVELS: errs.append(f'{pack}/{j.get("id")}: invalid maturity level {j.get("maturity_level")}')
            if j.get('entry_type') == 'imported-fragment':
                frag=j.get('journal_fragment')
                if not frag or not (ROOT/frag).exists(): errs.append(f'{pack}/{j.get("id")}: missing journal fragment {frag}')
            if j.get('entry_type') == 'candidate-l0' and j.get('maturity_level')!='L0':
                errs.append(f'{pack}/{j.get("id")}: candidate must be L0')
            if 'source_quality_score' not in j: errs.append(f'{pack}/{j.get("id")}: missing source_quality_score')
            if 'promotion_readiness' not in j: errs.append(f'{pack}/{j.get("id")}: missing promotion_readiness')
        rows.append({'pack':pack,'journals':len(journals),'levels':{lvl:sum(1 for j in journals if j.get('maturity_level')==lvl) for lvl in sorted(LEVELS)}})
    except Exception as e:
        errs.append(f'{pack}: cannot parse journals.yaml: {e}')
    try:
        m=yaml.safe_load((d/'fragment_import_manifest.yaml').read_text())
        if 'context_safety_rules' not in m: errs.append(f'{pack}: import manifest missing context_safety_rules')
    except Exception as e:
        errs.append(f'{pack}: cannot parse fragment_import_manifest.yaml: {e}')
    try:
        q=json.loads((d/'source_quality_report.json').read_text())
        if 'summary' not in q or 'journals' not in q: errs.append(f'{pack}: source_quality_report missing summary/journals')
        if q.get('schema_version') != '1.3.0': errs.append(f'{pack}: source_quality_report schema should be 1.3.0')
    except Exception as e:
        errs.append(f'{pack}: cannot parse source_quality_report.json: {e}')
for rel in ['resources/journal_coverage_dashboard.json','resources/journal_coverage_dashboard.yaml','resources/source_quality_scores.json','resources/source_quality_scores.yaml','resources/pack_maturity_report.json','resources/pack_maturity_report.yaml','resources/coverage_diff_report.json','resources/coverage_diff_report.yaml']:
    if not (ROOT/rel).exists(): errs.append(f'missing {rel}')
print(json.dumps({'expansion_pack_validation':rows,'errors':errs}, indent=2))
if errs: sys.exit(1)
