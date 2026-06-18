#!/usr/bin/env python3
from pathlib import Path
import json, yaml, hashlib, datetime, argparse
ROOT=Path(__file__).resolve().parents[1]

def dump_json(path,obj): path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')
def dump_yaml(path,obj): path.parent.mkdir(parents=True,exist_ok=True); path.write_text(yaml.safe_dump(obj,sort_keys=False,allow_unicode=True),encoding='utf-8')
def collect():
    reg=ROOT/'resources/official_source_registry.json'
    data=json.loads(reg.read_text(encoding='utf-8')) if reg.exists() else {}
    records=[]
    for k,v in data.get('publisher_common_sources',{}).items():
        if isinstance(v,str) and v.startswith('http'):
            records.append({'scope':'publisher','journal_id':None,'field':k,'url':v,'path':'resources/official_source_registry.json','source_class':'publisher-wide'})
    for j in data.get('journals',[]):
        for k,v in j.get('fields',{}).items():
            if isinstance(v,str) and v.startswith('http'):
                records.append({'scope':'journal','journal_id':j.get('id'),'journal_title':j.get('title'),'field':k,'url':v,'path':j.get('path',''),'source_class':'journal-specific'})
    return records

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--label', default=None)
    args=ap.parse_args()
    records=collect()
    today=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H%M%SZ')
    label=args.label or today
    snap={'schema_version':'1.0','generated_on':today,'snapshot_mode':'offline-registry-snapshot','records_count':len(records),'unique_url_count':len({r['url'] for r in records}),'records':records,'content_note':'Offline snapshot of recorded official-source fields; no remote content fetched.'}
    snap['snapshot_hash']=hashlib.sha256(json.dumps(records,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    out=ROOT/'resources/source_snapshots'
    dump_json(out/f'{label}.json',snap); dump_yaml(out/f'{label}.yaml',snap)
    dump_json(out/'latest.json',snap); dump_yaml(out/'latest.yaml',snap)
    print(json.dumps({'snapshot':str(out/f'{label}.json'),'records':len(records),'hash':snap['snapshot_hash']},indent=2))
if __name__=='__main__': main()
