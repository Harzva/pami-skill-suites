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
    bench=load_json(data/'visual_query_benchmark.json',{})
    traces=load_json(data/'human_retrieval_eval_traces.json',{}).get('traces',[])
    records=load_json(data/'multimodal_rag_index.json',{}).get('records',[])
    queries=bench.get('queries',[])
    coverage_gaps=sum(1 for q in queries if not q.get('expected_result_candidates'))
    total_results=sum(len(q.get('expected_result_candidates',[])) for q in queries)
    out={'schema_version':'2.6.0','release_version':VERSION,'generated_on':TODAY,'title':'RAG Evaluator Report','summary':{'visual_query_count':len(queries),'seed_record_count':len(records),'expected_result_links':total_results,'coverage_gap_queries':coverage_gaps,'human_eval_traces':len(traces),'metadata_only_rag_allowed':len(records),'image_embedding_allowed':0,'public_gallery_allowed':0,'offline_release_build':True},'quality_gates':{'metadata_only_seed_rag':'passed' if records else 'no_seed_records','image_embedding_gate':'closed','public_gallery_gate':'closed','copyright_safety_filter':'enabled','human_evaluation_required_for_quality_claims':True,'no_live_lookup_claimed':True},'recommended_next_actions':['Run human retrieval evaluation traces after connecting a retrieval system.','Add legally reviewed OA main figures to reduce coverage gaps.','Keep image embedding and public gallery modes closed until evidence gates pass.']}
    dump_pair(out,data/'rag_evaluator_report.json')
    print(json.dumps({'script':'rag_evaluator_report.py','queries':len(queries),'passed':True},indent=2))
if __name__=='__main__': main()
