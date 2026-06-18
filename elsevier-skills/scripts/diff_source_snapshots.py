#!/usr/bin/env python3
from pathlib import Path
import json, yaml, argparse, sys
ROOT=Path(__file__).resolve().parents[1]

def dump_json(path,obj): path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')
def dump_yaml(path,obj): path.parent.mkdir(parents=True,exist_ok=True); path.write_text(yaml.safe_dump(obj,sort_keys=False,allow_unicode=True),encoding='utf-8')
def load(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def key(r): return (r.get('scope'),r.get('journal_id'),r.get('field'))
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--old', default=None)
    ap.add_argument('--new', default=str(ROOT/'resources/source_snapshots/latest.json'))
    args=ap.parse_args()
    new=load(args.new) if Path(args.new).exists() else {'records':[]}
    old=load(args.old) if args.old and Path(args.old).exists() else {'records':[]}
    oldm={key(r):r for r in old.get('records',[])}; newm={key(r):r for r in new.get('records',[])}
    added=[]; removed=[]; changed=[]
    for k,r in newm.items():
        if k not in oldm: added.append(r)
        elif oldm[k].get('url')!=r.get('url'): changed.append({'key':list(k),'old':oldm[k],'new':r})
    for k,r in oldm.items():
        if k not in newm: removed.append(r)
    report={'schema_version':'1.0','mode':'snapshot-diff' if args.old else 'baseline-no-previous-snapshot','old_snapshot':args.old,'new_snapshot':args.new,'summary':{'added_records':len(added) if args.old else 0,'removed_records':len(removed) if args.old else 0,'changed_records':len(changed) if args.old else 0,'baseline_inventory_records':len(newm) if not args.old else 0},'changes':{'added':added if args.old else [],'removed':removed if args.old else [],'changed':changed if args.old else []},'live_verification_warning':'Diff compares recorded fields; run live source checks separately for URL health.'}
    dump_json(ROOT/'resources/policy_diff_report.json', report); dump_yaml(ROOT/'resources/policy_diff_report.yaml', report)
    print(json.dumps(report['summary'],indent=2))
if __name__=='__main__': main()
