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

def main():
    root=root_dir(); data=data_dir(root)
    exp=load_json(data/'expected_retrieval_results.json',{})
    traces=[]
    for e in exp.get('results',[]):
        traces.append({'trace_id':'trace_'+e.get('query_id','unknown'),'query_id':e.get('query_id'),'evaluation_status':'pending-human-evaluation','offline_release_behavior':'No human evaluator judgment was claimed in this release build.','retrieved_result_count':e.get('expected_results_count',0),'human_judgment_template':{'relevance_0_to_5':None,'tag_alignment_0_to_5':None,'mode_safety_pass':None,'copyright_safety_pass':None,'scientific_figure_design_usefulness_0_to_5':None,'failure_modes':[],'reviewer_notes':'TBD by human reviewer.'},'required_safety_checks':['metadata-only mode used','no unverified candidate leakage','no source image reuse suggested','permission warning included']})
    out={'schema_version':'2.6.0','release_version':VERSION,'generated_on':TODAY,'title':'Human Retrieval Evaluation Traces','traces':traces}
    dump_pair(out,data/'human_retrieval_eval_traces.json')
    print(json.dumps({'script':'human_retrieval_eval_traces.py','traces':len(traces),'passed':True},indent=2))
if __name__=='__main__': main()
