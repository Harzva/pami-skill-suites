#!/usr/bin/env python3
"""Score visual assets for analysis readiness, not scientific quality."""
import json, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]; RES=ROOT/'resources'
def main():
    report=json.loads((RES/'visual_rhetoric_report.json').read_text(encoding='utf-8'))
    scores=[]
    for a in report.get('assets',[]):
        s=a.get('analysis_stats',{})
        score=100
        if s.get('width') and s.get('height') and min(s['width'],s['height'])<700: score-=15
        if s.get('contrast_proxy') is not None and s['contrast_proxy']<80: score-=10
        scores.append({'asset_id':a['asset_id'],'asset_path':a['asset_path'],'score':max(score,50),'scope':'analysis-readiness-only'})
    out={'schema_version':'1.0','release_version':'1.9.0','scores':scores,'safety':'Scores are not permission to reuse visuals.'}
    (RES/'visual_asset_scores.json').write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')
    print('visual asset scores:', len(scores))
if __name__=='__main__': main()
