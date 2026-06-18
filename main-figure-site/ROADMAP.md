# ROADMAP.md


## v2.3.0 — Live DOI/OA Metadata Connector + Candidate Evidence Cards

This release adds a candidate evidence-card system for the 100-paper main-figure workflow. Each candidate now separates DOI evidence, publisher page evidence, repository OA evidence, license evidence, permission evidence, third-party material evidence, and manual reviewer notes. The release remains offline-safe: connector plans for Crossref, OpenAlex, Unpaywall, publisher pages, and institutional repositories are defined, but no live DOI/OA/license verification is claimed in the release build.

Extraction gate policy: no new figure extraction, public gallery hosting, or image reuse is allowed until evidence completeness and manual review pass. Seed assets may remain as structural-analysis metadata, but still require live license and permission re-check before public reuse.

## v2.4.0: Evidence-Gated OA Candidate Promotion + Connector Simulation Reports

This release adds an evidence-gated candidate promotion workflow for the main-figure corpus. It preserves the context-safe compact architecture: advanced skills, expansion packs, presets, and main_figure_site assets remain opt-in and are not default-visible top-level skills.

New v2.4.0 artifacts include:

- `evidence_promotion_queue.json/yaml`
- `connector_simulation_report.json/yaml`
- `candidate_evidence_diff_report.json/yaml`
- `human_reviewer_decision_log.json/yaml`
- `extraction_ready_candidates.json`
- `rag_ready_metadata_candidates.json`

Safety rule: no candidate may enter new figure extraction or public gallery hosting until DOI, OA source, exact license, permission, third-party-material, and human-review evidence pass the gate.


## v2.4.0 Completed

- Evidence-gated candidate promotion queue.
- Offline metadata connector simulation reports.
- Candidate evidence diff reports.
- Human reviewer decision log.
- Extraction-ready and metadata-only RAG-ready candidate lists.

## Next: v2.5.0

Focus on RAG ingestion governance, vector-index schemas, and figure-card retrieval quality without exposing the main-figure site as default top-level skills.

## v2.4.0 Evidence-Gated OA Candidate Promotion

v2.4.0 adds an evidence-gated promotion workflow for main-figure OA candidates. It introduces connector simulation reports, candidate evidence diffs, human reviewer decision logs, extraction-ready candidate reports, and metadata-only RAG-ready candidate lists. The default `skills/` layer remains compact; `skills-advanced/`, `expansion_packs/`, `presets/`, and `main_figure_site/` remain opt-in and not default-visible.

Safety: no Sci-Hub, pirated PDFs, paywalled-only PDFs, copyright-unknown PDFs, or unauthorized image reuse. Offline release builds do not approve extraction automatically.

## After v2.5.0

Next: v2.6.0 should add visual-query benchmark datasets and human-evaluated retrieval traces while keeping public-gallery and image-embedding modes permission-gated.


## v2.7.0 — RAG Trace UI + Visual Query Debugger

- Preserves context-safe compact architecture and keeps advanced/preset/main-figure assets out of default top-level skills.
- Adds RAG trace UI index, visual query debug traces, query rewrite suggestions, missing-tag coverage report, corpus expansion recommendations, and human-evaluation dashboard.
- Keeps metadata-only seed RAG allowed while image-embedding and public-gallery RAG remain blocked until evidence and human approval pass.
- Adds GitHub Pages documentation for RAG trace UI, visual query debugging, query rewriting, corpus expansion recommendations, and human-evaluation dashboard.
- Strictly prohibits Sci-Hub, pirated PDFs, paywalled-only PDFs, copyright-unknown PDFs, and unauthorized image reuse.
