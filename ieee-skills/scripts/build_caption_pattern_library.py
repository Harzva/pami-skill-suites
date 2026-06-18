#!/usr/bin/env python3
"""Build caption pattern library."""
import json, pathlib
try: import yaml
except Exception: yaml=None
ROOT=pathlib.Path(__file__).resolve().parents[1]; RES=ROOT/'resources'
def dump_yaml(path,obj): path.write_text(yaml.safe_dump(obj, sort_keys=False, allow_unicode=True) if yaml else json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')
def main():
    lib={'schema_version':'1.0','release_version':'1.9.0','caption_moves':['identify visual object','state context','decode encodings','state supported takeaway','point to details'],'failure_modes':['title-only caption','unsupported interpretation','omitted symbols','copied source wording'],'safety':'Do not copy source captions.'}
    (RES/'caption_pattern_library.json').write_text(json.dumps(lib, indent=2, ensure_ascii=False), encoding='utf-8'); dump_yaml(RES/'caption_pattern_library.yaml', lib)
    print('caption moves:', len(lib['caption_moves']))
if __name__=='__main__': main()
