#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml, re
ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / 'evals'
REQUIRED_TASK_FIELDS = ['task_id','benchmark_version','publisher','target_journal','query','required_modules','expected_output_sections','rubrics','sample_output','safety_warnings']
REQUIRED_SAMPLE_MARKERS = ['Selected skills/modules','Official-source warning','Copyright-safe paper-mining warning','Reviewer-risk checklist','Structured output contract']
errors=[]; warnings=[]; task_rows=[]
if not EVALS.exists():
    errors.append('missing evals/')
else:
    for rel in ['tasks','rubrics','sample_outputs','README.md','benchmark_manifest.yaml','benchmark_manifest.json']:
        if not (EVALS/rel).exists(): errors.append(f'missing evals/{rel}')
    rubric_files = {p.name for p in (EVALS/'rubrics').glob('*.md')} if (EVALS/'rubrics').exists() else set()
    for task_file in sorted((EVALS/'tasks').glob('*.yaml')) if (EVALS/'tasks').exists() else []:
        data=yaml.safe_load(task_file.read_text(encoding='utf-8')) or {}
        missing=[f for f in REQUIRED_TASK_FIELDS if f not in data]
        if missing: errors.append(f'{task_file.name}: missing fields {missing}')
        tid=data.get('task_id',task_file.stem)
        sample_rel=data.get('sample_output','')
        sample_path=ROOT/sample_rel if sample_rel else None
        if not sample_path or not sample_path.exists(): errors.append(f'{task_file.name}: missing sample output {sample_rel}')
        else:
            txt=sample_path.read_text(encoding='utf-8', errors='ignore')
            for marker in REQUIRED_SAMPLE_MARKERS:
                if marker not in txt: errors.append(f'{sample_path.relative_to(ROOT)}: missing marker {marker}')
            if 'official' in task_file.stem or 'submission' in task_file.stem or 'response' in task_file.stem:
                if 'Live verification' not in txt and 'live verification' not in txt:
                    errors.append(f'{sample_path.relative_to(ROOT)}: missing live verification language')
            if 'paper_mining' in task_file.stem:
                for phrase in ['Do not copy','mines only structure']:
                    if phrase not in txt: errors.append(f'{sample_path.relative_to(ROOT)}: missing paper-mining safety phrase {phrase}')
        for r in data.get('rubrics',[]):
            if r not in rubric_files: errors.append(f'{task_file.name}: unknown rubric {r}')
        if len(data.get('required_modules',[])) < 2: errors.append(f'{task_file.name}: too few required_modules')
        task_rows.append({'task':tid,'rubrics':data.get('rubrics',[]),'required_modules':data.get('required_modules',[])})
    if len(task_rows) < 8: errors.append(f'too few eval tasks: {len(task_rows)} < 8')
print(json.dumps({'task_count':len(task_rows),'tasks':task_rows,'errors':errors,'warnings':warnings}, indent=2, ensure_ascii=False))
if errors: sys.exit(1)
