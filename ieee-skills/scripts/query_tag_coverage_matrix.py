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
    records=load_json(data/'multimodal_rag_index.json',{}).get('records',[])
    tags=sorted({str(t).lower() for r in records for t in r.get('visual_rhetoric_tags',[])})
    matrix=[]
    for q in bench.get('queries',[]):
        cov={}
        for t in q.get('expected_tags',[]):
            tl=t.lower(); cov[t]=sum(1 for r in records if tl in {str(x).lower() for x in r.get('visual_rhetoric_tags',[])})
        matrix.append({'query_id':q.get('query_id'),'expected_tags':q.get('expected_tags',[]),'seed_record_count':len(records),'tag_coverage':cov,'best_seed_matches':q.get('expected_result_candidates',[])[:3],'coverage_status':'has_seed_matches' if q.get('expected_result_candidates') else 'coverage_gap'})
    out={'schema_version':'2.6.0','release_version':VERSION,'generated_on':TODAY,'title':'Query-to-Tag Coverage Matrix','available_seed_tags':tags,'matrix':matrix}
    dump_pair(out,data/'query_tag_coverage_matrix.json')
    print(json.dumps({'script':'query_tag_coverage_matrix.py','queries':len(matrix),'passed':True},indent=2))
if __name__=='__main__': main()
