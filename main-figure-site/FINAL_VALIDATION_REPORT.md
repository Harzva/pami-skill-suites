# Final Validation Report - v2.7.0

Repository: `main-figure-site`
Generated on: 2026-06-18
Release name: RAG Trace UI + Visual Query Debugger

## Summary

v2.7.0 is the current validated standalone main-figure site release for the Journal Skill Suites package.

## Release gates

- `python3 scripts/validate_main_figure_corpus.py --site .`: passed, `11` seeded figures with target capacity `100`
- `python3 scripts/validate_candidate_evidence.py`: passed, `100` records
- `python3 scripts/validate_evidence_promotion.py`: passed, `100` candidates and `11` metadata-only RAG records
- `python3 scripts/validate_rag_governance.py`: passed
- `python3 scripts/validate_rag_trace_ui.py`: passed
- `python3 scripts/validate_visual_query_benchmark.py`: passed
- `python3 scripts/validate_source_discovery.py`: passed, `100` records

## Safety gates

- Metadata-only seed RAG remains allowed.
- Image embedding remains blocked.
- Public-gallery reuse remains blocked.
- New figure extraction remains blocked until DOI/OA/license evidence, permission evidence, third-party-material review, and human approval pass.

## Notes

This validation is an offline-safe release gate. It does not certify live DOI/OA/license status, official URL freshness, publisher policy changes, or permission to reuse source-paper visuals.
