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
    byid={r.get('paper_id'):r for r in records}
    results=[]
    for q in bench.get('queries',[]):
        cards=[]
        for c in q.get('expected_result_candidates',[]):
            r=byid.get(c.get('paper_id'))
            if r:
                cards.append({'paper_id':r.get('paper_id'),'title':r.get('title'),'journal':r.get('journal'),'year':r.get('year'),'retrieval_mode':'metadata-only','match_score':c.get('score'),'tag_overlap':c.get('tag_overlap',[]),'safe_expected_use':'structural retrieval only; no source visual reuse','blocked_use':'no image reuse, caption copying, embedding, or public gallery display without approval'})
        results.append({'query_id':q.get('query_id'),'expected_results_count':len(cards),'expected_result_cards':cards,'minimum_acceptable_behavior':['say coverage is insufficient if no seed matches','include permission warning','keep output metadata-only']})
    out={'schema_version':'2.6.0','release_version':VERSION,'generated_on':TODAY,'title':'Expected Retrieval Results','results':results}
    dump_pair(out,data/'expected_retrieval_results.json')
    print(json.dumps({'script':'expected_retrieval_results.py','queries':len(results),'passed':True},indent=2))
if __name__=='__main__': main()
