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
FAILURE_TAXONOMY = [{'failure_id': 'F01_tag_mismatch', 'name': 'Tag mismatch', 'severity': 'medium', 'description': 'Returned records do not match the user intent or expected visual rhetoric tags.', 'mitigation': 'Improve tag coverage matrix and add expected result cards.'}, {'failure_id': 'F02_mode_violation', 'name': 'RAG mode violation', 'severity': 'critical', 'description': 'A response treats metadata-only records as image-embedding or public-gallery eligible.', 'mitigation': 'Enforce RAG entry eligibility and permission gates.'}, {'failure_id': 'F03_copyright_overreach', 'name': 'Copyright overreach', 'severity': 'critical', 'description': 'A response suggests copying, redrawing, publishing, or reusing source visuals without permission evidence.', 'mitigation': 'Inject copyright safety warnings in every retrieval answer.'}, {'failure_id': 'F04_caption_copying', 'name': 'Caption copying', 'severity': 'high', 'description': 'A response reproduces source captions or panel labels verbatim instead of safe summaries.', 'mitigation': 'Use safe summary fields and forbid verbatim caption reuse.'}, {'failure_id': 'F05_unverified_candidate_leak', 'name': 'Unverified candidate leakage', 'severity': 'critical', 'description': 'Pending candidate slots appear as if they were verified papers or extracted figures.', 'mitigation': 'Exclude pending records from RAG and gallery until evidence gate passes.'}, {'failure_id': 'F06_domain_confusion', 'name': 'Domain confusion', 'severity': 'medium', 'description': 'The retriever returns unrelated domains, such as medical AI records for a remote sensing request.', 'mitigation': 'Use preset-specific domain tags and coverage matrix.'}, {'failure_id': 'F07_low_evidence_alignment', 'name': 'Low evidence alignment', 'severity': 'medium', 'description': 'Returned visuals are aesthetically relevant but do not support the requested claim/evidence structure.', 'mitigation': 'Add claim-evidence metadata and human evaluation trace.'}, {'failure_id': 'F08_no_permission_warning', 'name': 'Missing permission warning', 'severity': 'high', 'description': 'A response omits permission, license, or third-party-material warnings.', 'mitigation': 'Require safety warning in output contract and sample traces.'}]
def main():
    root=root_dir(); data=data_dir(root)
    out={'schema_version':'2.6.0','release_version':VERSION,'generated_on':TODAY,'title':'Retrieval Failure Taxonomy','failure_modes':FAILURE_TAXONOMY}
    dump_pair(out,data/'retrieval_failure_taxonomy.json')
    print(json.dumps({'script':'retrieval_failure_taxonomy.py','failure_modes':len(FAILURE_TAXONOMY),'passed':True},indent=2))
if __name__=='__main__': main()
