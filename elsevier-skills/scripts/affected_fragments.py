#!/usr/bin/env python3
from pathlib import Path
import json, yaml
ROOT=Path(__file__).resolve().parents[1]
def dump_json(path,obj): path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')
def dump_yaml(path,obj): path.parent.mkdir(parents=True,exist_ok=True); path.write_text(yaml.safe_dump(obj,sort_keys=False,allow_unicode=True),encoding='utf-8')
report=json.loads((ROOT/'resources/policy_diff_report.json').read_text(encoding='utf-8')) if (ROOT/'resources/policy_diff_report.json').exists() else {'changes':{}}
affected=[]
for change_type in ['added','removed','changed']:
    for item in report.get('changes',{}).get(change_type,[]):
        rec=item.get('new') or item.get('old') or item
        path=rec.get('path')
        if path:
            affected.append({'change_type':change_type,'path':path,'field':rec.get('field'),'journal_id':rec.get('journal_id')})
obj={'schema_version':'1.0','affected_fragments_count':len(affected),'affected_fragments':affected,'note':'Generated from policy diff report. Human review required before updating submission advice.'}
dump_json(ROOT/'resources/affected_fragments_report.json',obj); dump_yaml(ROOT/'resources/affected_fragments_report.yaml',obj)
print(json.dumps({'affected_fragments_count':len(affected)},indent=2))
