#!/usr/bin/env python3
from pathlib import Path
import json, yaml, sys
ROOT=Path(__file__).resolve().parents[1]
errs=[]; rows=[]
required_resources=['resources/source_quality_scores.json','resources/source_quality_scores.yaml','resources/pack_maturity_report.json','resources/pack_maturity_report.yaml','resources/coverage_diff_report.json','resources/coverage_diff_report.yaml']
for rel in required_resources:
    if not (ROOT/rel).exists(): errs.append(f'missing {rel}')
for pack in sorted((ROOT/'expansion_packs').iterdir() if (ROOT/'expansion_packs').exists() else []):
    if not pack.is_dir(): continue
    for rel in ['source_quality_report.json','source_quality_report.md','paper_card_todo.md','promotion_queue.md']:
        if not (pack/rel).exists(): errs.append(f'{pack.name}: missing {rel}')
    ev=list((pack/'eval_tasks').glob('*.yaml')) if (pack/'eval_tasks').exists() else []
    if not ev: errs.append(f'{pack.name}: missing eval_tasks/*.yaml')
    data=yaml.safe_load((pack/'journals.yaml').read_text()) or {}
    if 'hardening' not in data: errs.append(f'{pack.name}: journals.yaml missing hardening section')
    for j in data.get('journals',[]):
        jid=j.get('id','unknown')
        if 'source_quality_score' not in j: errs.append(f'{pack.name}/{jid}: missing source_quality_score')
        if 'promotion_readiness' not in j: errs.append(f'{pack.name}/{jid}: missing promotion_readiness')
        if j.get('promotion_readiness',{}).get('context_safety','').lower().find('default')<0: errs.append(f'{pack.name}/{jid}: promotion readiness missing default skill safety note')
        if j.get('maturity_level')=='L0' and j.get('promotion_readiness',{}).get('eligible_for_direct_core_import'):
            errs.append(f'{pack.name}/{jid}: L0 candidate cannot be direct-core-import eligible')
    rows.append({'pack':pack.name,'journals':len(data.get('journals',[])),'eval_tasks':len(ev)})
# Ensure default skills small and no expansion pack under skills/.
skills=[p.name for p in (ROOT/'skills').iterdir() if p.is_dir() and p.name!='_shared'] if (ROOT/'skills').exists() else []
if len(skills)>10: errs.append(f'default skills too many: {len(skills)}')
if any('expansion' in s for s in skills): errs.append('expansion pack appears in default skills/')
print(json.dumps({'pack_maturity_validation':rows,'default_skills':len(skills),'errors':errs},indent=2))
if errs: sys.exit(1)
