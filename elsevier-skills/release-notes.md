# Elsevier Skills v2.7.0 Release Notes

## Current release

v2.7.0 adds the metadata-only RAG Trace UI and Visual Query Debugger for the main-figure workflow. It preserves the compact default skill surface, keeps advanced packs optional, and keeps image embedding, public-gallery reuse, and new figure extraction blocked until evidence review and human approval pass.

The sections below retain the historical release trail for the assets that v2.7.0 includes.

## Main-Figure Website + Multimodal Scientific-Figure RAG Corpus

This release adds `main_figure_site/` and a 100+ corpus-ready schema for legally sourced OA paper main figures.

The current seed corpus uses only the main figures already extracted from the repository's open-access template-paper corpus. Additional records must pass OA source, license, attribution, third-party material, and target-venue policy review.

## Context safety

Default `skills/` remains compact. `skills-advanced/`, `expansion_packs/`, `presets/`, and `main_figure_site/` are not default top-level skills.

## New scripts

- `scripts/ingest_main_figure_corpus.py`
- `scripts/extract_main_figures.py`
- `scripts/build_main_figure_gallery.py`
- `scripts/build_multimodal_rag_index.py`
- `scripts/validate_main_figure_corpus.py`
- `scripts/review_visual_permissions.py`

## v2.1.0 update: 100-Paper OA Main-Figure Corpus Expansion Workflow

This release adds a workflow-ready 100-paper candidate registry for lawful OA main-figure corpus expansion. It preserves the context-safe compact architecture: `skills-advanced/`, `expansion_packs/`, `presets/`, and `main_figure_site/` remain opt-in and are not default top-level skills.

The registry distinguishes actual seed figures from pending candidate slots. Pending entries are not verified papers and cannot be extracted until source URL, license, OA source type, and permission status are reviewed. Forbidden sources include Sci-Hub, pirated PDFs, paywalled-only PDFs, copyright-unknown PDFs, and unauthorized image reuse.

## v2.4.0 Source Discovery Preflight
### v2.4.0: OA Candidate Source Discovery + DOI/License Preflight

This release adds an offline-safe 100-paper main-figure expansion workflow. It keeps the context-safe architecture unchanged: default `skills/` stays compact, while `skills-advanced/`, `expansion_packs/`, `presets/`, and `main_figure_site/` remain opt-in and not default-visible.

New artifacts include `source_discovery_candidates`, `doi_license_preflight_report`, `candidate_risk_scores`, `source_discovery_review_queue`, and `extraction_readiness_dashboard`. Pending candidates remain blocked until DOI, OA source, license, and permission review pass.


## v2.4.0 — Live DOI/OA Metadata Connector + Candidate Evidence Cards

This release adds a candidate evidence-card system for the 100-paper main-figure workflow. Each candidate now separates DOI evidence, publisher page evidence, repository OA evidence, license evidence, permission evidence, third-party material evidence, and manual reviewer notes. The release remains offline-safe: connector plans for Crossref, OpenAlex, Unpaywall, publisher pages, and institutional repositories are defined, but no live DOI/OA/license verification is claimed in the release build.

Extraction gate policy: no new figure extraction, public gallery hosting, or image reuse is allowed until evidence completeness and manual review pass. Seed assets may remain as structural-analysis metadata, but still require live license and permission re-check before public reuse.

## v2.4.0 Evidence-Gated OA Candidate Promotion

v2.4.0 adds evidence-gated candidate promotion, connector simulation reports, candidate evidence diff reports, a human reviewer decision log, extraction-ready candidate lists, and metadata-only RAG-ready candidate lists. The default `skills/` layer remains context-safe and does not expose `skills-advanced/`, `expansion_packs/`, `presets/`, or `main_figure_site/` as top-level skills.

This is still an offline-safe release build: it does not claim live Crossref/OpenAlex/Unpaywall/publisher/repository verification and does not allow new figure extraction. Real reuse or public display requires DOI, OA source, license, permission, third-party-material, and human-review evidence to pass.

## v2.5.0

## v2.5.0: RAG Ingestion Governance + Retrieval Quality Evaluation

This release adds metadata-only RAG governance for the main-figure corpus while keeping image-embedding RAG and public-gallery RAG blocked until permission evidence and human reviewer approval pass.

Key additions:

- `main_figure_site/data/rag_ingestion_governance.json`
- `main_figure_site/data/rag_entry_eligibility_report.json`
- `main_figure_site/data/rag_retrieval_benchmark.json`
- `main_figure_site/data/rag_safety_filter_report.json`
- `main_figure_site/data/rag_quality_dashboard.json`
- `scripts/rag_ingestion_governance.py`
- `scripts/rag_entry_eligibility.py`
- `scripts/build_rag_retrieval_benchmark.py`
- `scripts/rag_safety_filter.py`
- `scripts/rag_quality_dashboard.py`
- `scripts/validate_rag_governance.py`

Context-safety remains unchanged: advanced skills, expansion packs, presets, and `main_figure_site/` are not default top-level skills.

Safety policy: only metadata-only seed records may enter RAG in this release. Image embedding and public-gallery use require DOI/OA/license evidence, permission evidence, third-party-material review, and human reviewer approval.


# v2.6.0 Release Notes

v2.6.0 adds Visual Query Benchmark and Human Retrieval Evaluation Traces to the metadata-only scientific-figure RAG workflow. It does not enable image embedding or public gallery use. No new figure extraction is allowed without evidence-gated permission review and human approval.


## v2.7.0 — RAG Trace UI + Visual Query Debugger

- Preserves context-safe compact architecture and keeps advanced/preset/main-figure assets out of default top-level skills.
- Adds RAG trace UI index, visual query debug traces, query rewrite suggestions, missing-tag coverage report, corpus expansion recommendations, and human-evaluation dashboard.
- Keeps metadata-only seed RAG allowed while image-embedding and public-gallery RAG remain blocked until evidence and human approval pass.
- Adds GitHub Pages documentation for RAG trace UI, visual query debugging, query rewriting, corpus expansion recommendations, and human-evaluation dashboard.
- Strictly prohibits Sci-Hub, pirated PDFs, paywalled-only PDFs, copyright-unknown PDFs, and unauthorized image reuse.
