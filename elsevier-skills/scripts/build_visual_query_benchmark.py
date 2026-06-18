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

QUERY_SPECS = [{'query_id': 'method_pipeline_main_figure', 'user_query': 'Find main figures that explain a method pipeline with inputs, modules, outputs, and evidence alignment.', 'intent': 'method pipeline visual synthesis', 'expected_tags': ['method-pipeline', 'workflow', 'overview', 'pipeline', 'claim-evidence'], 'task_family': 'main-figure retrieval'}, {'query_id': 'motivation_gap_figure', 'user_query': 'Find motivation figures that communicate a gap, limitation, or contrast between prior work and the proposed idea.', 'intent': 'motivation and gap framing', 'expected_tags': ['motivation', 'gap', 'contrast', 'problem-framing', 'overview'], 'task_family': 'motivation-figure retrieval'}, {'query_id': 'ablation_table_style', 'user_query': 'Find table examples that organize ablations or component-wise evidence clearly.', 'intent': 'table structure and ablation evidence retrieval', 'expected_tags': ['ablation', 'table', 'comparison', 'method-comparison', 'evidence'], 'task_family': 'table retrieval'}, {'query_id': 'taxonomy_survey_overview', 'user_query': 'Find survey-style overview figures or taxonomy diagrams for organizing a research field.', 'intent': 'taxonomy / survey overview retrieval', 'expected_tags': ['taxonomy', 'survey', 'overview', 'concept-map'], 'task_family': 'main-figure retrieval'}, {'query_id': 'medical_ai_workflow', 'user_query': 'Find medical AI workflow figures showing data, model, clinical output, and validation logic.', 'intent': 'medical AI workflow retrieval', 'expected_tags': ['medical-ai', 'workflow', 'clinical', 'validation', 'method-pipeline'], 'task_family': 'domain-specific retrieval'}, {'query_id': 'remote_sensing_pipeline', 'user_query': 'Find remote sensing pipeline figures showing sensing data, preprocessing, model stages, and evaluation.', 'intent': 'remote sensing pipeline retrieval', 'expected_tags': ['remote-sensing', 'pipeline', 'preprocessing', 'evaluation', 'method-pipeline'], 'task_family': 'domain-specific retrieval'}, {'query_id': 'caption_explanation_pattern', 'user_query': 'Find figure-caption patterns that explain panels, symbols, abbreviations, and takeaway evidence safely.', 'intent': 'caption structure retrieval', 'expected_tags': ['caption', 'panel-explanation', 'takeaway', 'symbol-explanation', 'copyright-review-required'], 'task_family': 'caption retrieval'}, {'query_id': 'limitations_visualization', 'user_query': 'Find visual examples or retrieval records useful for explaining limitations, failure cases, or boundary conditions.', 'intent': 'limitations and future-work visual retrieval', 'expected_tags': ['limitations', 'failure-case', 'boundary-condition', 'future-work', 'risk'], 'task_family': 'limitations retrieval'}, {'query_id': 'beautiful_comparison_table', 'user_query': 'Find beautiful comparison-table styles that make baselines, metrics, and evidence hierarchy easy to read.', 'intent': 'beautiful table pattern retrieval', 'expected_tags': ['beautiful-table', 'comparison', 'metrics', 'baseline', 'evidence'], 'task_family': 'table retrieval'}, {'query_id': 'figure_table_caption_bundle', 'user_query': 'Find examples where figure, table, and caption logic work together to support one paper claim.', 'intent': 'multi-component evidence bundle retrieval', 'expected_tags': ['figure', 'table', 'caption', 'claim-evidence', 'overview'], 'task_family': 'multi-component retrieval'}, {'query_id': 'visual_rhetoric_for_introduction', 'user_query': 'Find visuals that help an introduction move from problem pain point to research gap to contribution.', 'intent': 'introduction visual rhetoric retrieval', 'expected_tags': ['motivation', 'gap', 'contribution', 'problem-framing', 'overview'], 'task_family': 'section-writing retrieval'}, {'query_id': 'rag_safety_permission_warning', 'user_query': 'Find records that illustrate when a user must be warned not to copy or reuse source figures directly.', 'intent': 'copyright and permission-safe retrieval', 'expected_tags': ['copyright-review-required', 'permission-review', 'metadata-only', 'safety'], 'task_family': 'safety retrieval'}]
def score_record(record, expected_tags):
    tags={str(t).lower() for t in record.get('visual_rhetoric_tags',[])}
    expected={str(t).lower() for t in expected_tags}
    text=' '.join(str(record.get(k,'')) for k in ['title','journal','retrieval_text']).lower()
    overlap=sorted(tags & expected)
    text_hits=[t for t in expected if t in text or t.replace('-',' ') in text]
    return len(overlap)*3+len(text_hits), overlap, sorted(set(text_hits))
def main():
    root=root_dir(); data=data_dir(root)
    records=load_json(data/'multimodal_rag_index.json',{}).get('records',[])
    queries=[]
    for q in QUERY_SPECS:
        scored=[]
        for r in records:
            s,overlap,text_hits=score_record(r,q['expected_tags'])
            if s>0: scored.append({'paper_id':r.get('paper_id'),'score':s,'tag_overlap':overlap,'text_hits':text_hits})
        scored=sorted(scored,key=lambda x:(-x['score'],x['paper_id']))[:5]
        q=dict(q); q.update({'benchmark_version':VERSION,'eligible_rag_modes':['metadata-only'],'blocked_rag_modes':['image-embedding','public-gallery'],'seed_result_pool_size':len(records),'expected_result_candidates':scored,'response_constraints':['safe summaries only','no caption copying','no image reuse','include permission warning'],'evaluation_fields':['relevance','mode_safety','copyright_safety','tag_alignment','usefulness']})
        queries.append(q)
    out={'schema_version':'2.6.0','release_version':VERSION,'generated_on':TODAY,'title':'Visual Query Benchmark for Metadata-only Scientific-Figure RAG','benchmark_policy':{'allowed_mode_now':'metadata-only RAG for seed records','blocked_modes':['image-embedding RAG','public-gallery RAG'],'no_live_lookup_claimed':True},'queries':queries}
    dump_pair(out,data/'visual_query_benchmark.json')
    print(json.dumps({'script':'build_visual_query_benchmark.py','queries':len(queries),'passed':True},indent=2))
if __name__=='__main__': main()
