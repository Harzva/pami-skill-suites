#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml
TODAY='2026-06-17'
VERSION='v2.6.0'

def root_dir():
    return Path(__file__).resolve().parents[1]

def data_dir(root):
    p=root/'main_figure_site'/'data'
    return p if p.exists() else root/'data'

def load_json(path, default=None):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return default if default is not None else {}

def dump_pair(obj, json_path):
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')
    json_path.with_suffix('.yaml').write_text(yaml.safe_dump(obj, sort_keys=False, allow_unicode=True), encoding='utf-8')

REQUIRED=['visual_query_benchmark.json','expected_retrieval_results.json','human_retrieval_eval_traces.json','retrieval_failure_taxonomy.json','query_tag_coverage_matrix.json','rag_evaluator_report.json']
def main():
    root=root_dir(); data=data_dir(root); errs=[]
    for f in REQUIRED:
        p=data/f
        if not p.exists(): errs.append('missing '+str(p))
        else:
            obj=load_json(p,{})
            if obj.get('schema_version')!='2.6.0': errs.append(f+' wrong schema_version')
    bench=load_json(data/'visual_query_benchmark.json',{})
    if len(bench.get('queries',[]))<8: errs.append('visual_query_benchmark needs at least 8 queries')
    traces=load_json(data/'human_retrieval_eval_traces.json',{})
    if len(traces.get('traces',[]))!=len(bench.get('queries',[])): errs.append('trace/query count mismatch')
    report=load_json(data/'rag_evaluator_report.json',{})
    if report.get('summary',{}).get('image_embedding_allowed')!=0: errs.append('image embedding gate should be closed')
    if report.get('summary',{}).get('public_gallery_allowed')!=0: errs.append('public gallery gate should be closed')
    print(json.dumps({'script':'validate_visual_query_benchmark.py','errors':errs,'passed':not errs},indent=2))
    sys.exit(1 if errs else 0)
if __name__=='__main__': main()
