#!/usr/bin/env python3
"""Build main/motivation figure pattern library from visual_rhetoric_report.json."""
import json, pathlib
try: import yaml
except Exception: yaml=None
ROOT=pathlib.Path(__file__).resolve().parents[1]; RES=ROOT/'resources'
def dump_yaml(path,obj):
    path.write_text(yaml.safe_dump(obj, sort_keys=False, allow_unicode=True) if yaml else json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')
def main():
    report=json.loads((RES/'visual_rhetoric_report.json').read_text(encoding='utf-8'))
    lib={'schema_version':'1.0','release_version':'1.9.0','use_scope':'abstract figure-structure patterns only','patterns':['pipeline-overview','taxonomy-map','problem-to-solution-overview','evidence-centered-main-figure'],'asset_links':[{'asset_id':a['asset_id'],'role':a['role'],'pattern':a['visual_rhetoric_pattern']} for a in report.get('assets',[]) if a.get('role') in ('main_figure','motivation_figure')], 'safety':'Do not copy source visuals.'}
    (RES/'figure_pattern_library.json').write_text(json.dumps(lib, indent=2, ensure_ascii=False), encoding='utf-8'); dump_yaml(RES/'figure_pattern_library.yaml', lib)
    print('figure patterns:', len(lib['patterns']))
if __name__=='__main__': main()
