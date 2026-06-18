#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

def find_data_root() -> Path:
    here = Path(__file__).resolve()
    for parent in [here.parent, *here.parents]:
        for rel in ("main_figure_site/data", "data"):
            p = parent / rel
            if (p / "rag_ingestion_governance.json").exists() or (p / "main_figure_manifest.json").exists():
                return p
    raise SystemExit("Could not locate main_figure_site/data or data directory")

def load(name, default=None):
    p = find_data_root() / name
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return default

def save(name, data):
    p = find_data_root() / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return p

def entries(data, key):
    if isinstance(data, dict) and isinstance(data.get(key), list): return data[key]
    if isinstance(data, dict):
        for v in data.values():
            if isinstance(v, list) and (not v or isinstance(v[0], dict)): return v
    return []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    data = find_data_root()
    action = Path(__file__).stem
    gov = load("rag_ingestion_governance.json", {})
    elig = load("rag_entry_eligibility_report.json", {})
    bench = load("rag_retrieval_benchmark.json", {})
    safety = load("rag_safety_filter_report.json", {})
    dash = load("rag_quality_dashboard.json", {})

    if action == "rag_ingestion_governance":
        required = ["rag_modes", "global_ingestion_rules", "current_status"]
        missing = [x for x in required if x not in gov]
        if missing: raise SystemExit(f"missing governance fields: {missing}")
        print(f"rag_ingestion_governance: passed ({gov.get('current_status',{}).get('seed_metadata_only_entries',0)} metadata-only seed records)")
    elif action == "rag_entry_eligibility":
        es = entries(elig, "entries")
        if len(es) < 100: raise SystemExit(f"expected >=100 eligibility entries, got {len(es)}")
        if any(e.get("image_embedding_rag") != "blocked_until_permission_evidence_and_human_approval" for e in es):
            raise SystemExit("image embedding gate must remain blocked")
        print(f"rag_entry_eligibility: passed ({len(es)} entries)")
    elif action == "build_rag_retrieval_benchmark":
        qs = entries(bench, "queries")
        if len(qs) < 6: raise SystemExit("expected at least 6 retrieval benchmark queries")
        print(f"build_rag_retrieval_benchmark: passed ({len(qs)} queries)")
    elif action == "rag_safety_filter":
        flags = entries(safety, "flags")
        if len(flags) < 100: raise SystemExit(f"expected >=100 safety flags, got {len(flags)}")
        if safety.get("summary",{}).get("image_embedding_allowed", 1) != 0: raise SystemExit("image embedding allowed must be 0")
        if safety.get("summary",{}).get("public_gallery_allowed", 1) != 0: raise SystemExit("public gallery allowed must be 0")
        print(f"rag_safety_filter: passed ({len(flags)} flags)")
    elif action == "rag_quality_dashboard":
        if not dash.get("summary"): raise SystemExit("missing quality dashboard summary")
        print("rag_quality_dashboard: passed")
    elif action == "validate_rag_governance":
        required = [
            "rag_ingestion_governance.json", "rag_entry_eligibility_report.json", "rag_retrieval_benchmark.json",
            "rag_safety_filter_report.json", "rag_quality_dashboard.json"
        ]
        missing = [r for r in required if not (data/r).exists()]
        if missing: raise SystemExit(f"missing required RAG files: {missing}")
        es = entries(elig, "entries")
        if len(es) < 100: raise SystemExit("eligibility entries must cover 100 candidates")
        if safety.get("summary",{}).get("image_embedding_allowed", 1) != 0: raise SystemExit("image embedding gate accidentally open")
        if safety.get("summary",{}).get("public_gallery_allowed", 1) != 0: raise SystemExit("public gallery gate accidentally open")
        print("validate_rag_governance: passed")
    else:
        raise SystemExit(f"unknown script action: {action}")

if __name__ == "__main__":
    main()
