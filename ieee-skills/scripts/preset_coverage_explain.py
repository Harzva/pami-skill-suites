#!/usr/bin/env python3
from pathlib import Path
import argparse,json,yaml,sys
ROOT=Path(__file__).resolve().parents[1]; ap=argparse.ArgumentParser(); ap.add_argument('--preset'); args=ap.parse_args(); ids=[p.name for p in (ROOT/'presets').iterdir() if p.is_dir()]
if args.preset: ids=[x for x in ids if x==args.preset]
out={'preset_count':len(ids),'explanations':[{'preset_id':x,'default_visible':False,'scenario_gallery':f'presets/{x}/scenarios/','coverage_explanation':'optional preset coverage; not a default top-level skill'} for x in ids]}
(ROOT/'resources/preset_coverage_explain.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8'); (ROOT/'resources/preset_coverage_explain.yaml').write_text(yaml.safe_dump(out,sort_keys=False,allow_unicode=True),encoding='utf-8'); print(json.dumps(out,indent=2,ensure_ascii=False)); sys.exit(1 if args.preset and not ids else 0)
