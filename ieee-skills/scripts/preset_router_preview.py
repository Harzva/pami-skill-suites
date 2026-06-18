#!/usr/bin/env python3
from pathlib import Path
import argparse, json, yaml, sys
ROOT=Path(__file__).resolve().parents[1]
PRESETS=ROOT/'presets'

def load_yaml(path):
    with open(path,'r',encoding='utf-8') as f: return yaml.safe_load(f) or {}

def list_presets():
    registry_path=ROOT/'resources/preset_registry.json'
    if registry_path.exists():
        return json.loads(registry_path.read_text(encoding='utf-8')).get('presets',[])
    return [{'id':p.name,'path':str(p.relative_to(ROOT))} for p in PRESETS.iterdir() if p.is_dir()]

def preview(preset_id, task):
    p=PRESETS/preset_id
    if not p.exists(): raise SystemExit(f'unknown preset: {preset_id}')
    preset=load_yaml(p/'preset.yaml')
    routing=load_yaml(p/'routing-profile.yaml')
    q=(task or '').lower()
    selected_components=[]
    rules={
        'related-work':['related-work','citation','contribution-positioning'],
        'abstract':['abstract','contribution-positioning'],
        'caption':['figure','table','caption','visual-accessibility'],
        'figure':['figure','caption','visual-accessibility'],
        'table':['table','caption','results-reporting'],
        'reviewer':['response-letter','reviewer-response-matrix','revision-diff'],
        'response':['response-letter','reviewer-response-matrix','revision-diff'],
        'submission':['cover-letter','author-agreement','copyright','open-access','final-files'],
        'source':['official-source-compliance','live-verification'],
        'compliance':['official-source-compliance','live-verification'],
        'paper':['paper-mining-safety','structure-map'],
        'template':['paper-mining-safety','structure-map'],
    }
    for key, comps in rules.items():
        if key in q:
            selected_components.extend(comps)
    if not selected_components:
        selected_components=['abstract','related-work','table','figure','caption','official-source-compliance']
    selected_components=list(dict.fromkeys(selected_components))
    journals=preset.get('target_journals',[])[:5]
    return {
        'preset_id': preset_id,
        'task': task,
        'suite_router': preset.get('default_module_bundle',{}).get('suite'),
        'selected_journal_candidates': [{'id':j.get('id'),'title':j.get('title'),'maturity_level':j.get('maturity_level')} for j in journals],
        'selected_component_modules': selected_components,
        'official_source_warning': 'Live verification required before real submission advice.',
        'context_policy': preset.get('context_policy'),
        'visibility': preset.get('visibility')
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--list',action='store_true')
    ap.add_argument('--preset')
    ap.add_argument('--task',default='')
    args=ap.parse_args()
    if args.list:
        print(json.dumps({'presets':list_presets()},indent=2)); return
    if not args.preset:
        raise SystemExit('use --list or --preset PRESET_ID')
    print(json.dumps(preview(args.preset,args.task),indent=2))
if __name__=='__main__': main()
