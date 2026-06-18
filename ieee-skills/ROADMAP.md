# Roadmap

## v2.0.0 — Visual Rhetoric Analyzer + Pattern Libraries

Completed:

- visual rhetoric report;
- main/motivation figure patterns;
- beautiful table patterns;
- caption patterns;
- experiment/formula/motivation/limitations/conclusion routine libraries.

## v2.0.0 — Main-Figure Website + Multimodal Research-Figure RAG

Planned:

- collect at least 100 legally sourced OA main-figure papers;
- build a standalone main-figure gallery website;
- create multimodal RAG ingestion schema;
- store figure metadata, safe descriptions, captions summaries, visual tags, and section links;
- build retrieval for “show me motivation figures like X” and “design a PAMI-style main figure skeleton”.

Safety: no copyrighted visual reuse without license and permission checks.


## v2.0.0 Main-Figure Website + Multimodal Scientific-Figure RAG Corpus

This release adds `main_figure_site/`, a copyright-safe scaffold for a 100+ open-access paper main-figure gallery and multimodal scientific-figure RAG corpus.

Key additions:

- `main_figure_site/docs/` static website.
- `main_figure_site/gallery/` seeded main-figure images from the existing legal OA template corpus.
- `main_figure_site/data/main_figure_manifest.json` and `.yaml`.
- `main_figure_site/data/main_figure_cards/` with one card per seeded figure.
- `main_figure_site/data/multimodal_rag_index.json` for retrieval-oriented metadata.
- `main_figure_site/data/visual_tags.json` and `license_registry.json`.
- `main_figure_site/data/candidate_backlog_100.json` for the 100+ OA main-figure expansion plan.

Safety policy: visual assets are for structural analysis only. Do not copy, redraw, publish, or reuse figures, captions, labels, layouts, or paper-specific claims without verifying license, attribution requirements, third-party material status, and target venue policy.

## v2.1.0 update: 100-Paper OA Main-Figure Corpus Expansion Workflow

This release adds a workflow-ready 100-paper candidate registry for lawful OA main-figure corpus expansion. It preserves the context-safe compact architecture: `skills-advanced/`, `expansion_packs/`, `presets/`, and `main_figure_site/` remain opt-in and are not default top-level skills.

The registry distinguishes actual seed figures from pending candidate slots. Pending entries are not verified papers and cannot be extracted until source URL, license, OA source type, and permission status are reviewed. Forbidden sources include Sci-Hub, pirated PDFs, paywalled-only PDFs, copyright-unknown PDFs, and unauthorized image reuse.

## v2.3.0 Source Discovery Preflight
### v2.3.0: OA Candidate Source Discovery + DOI/License Preflight

This release adds an offline-safe 100-paper main-figure expansion workflow. It keeps the context-safe architecture unchanged: default `skills/` stays compact, while `skills-advanced/`, `expansion_packs/`, `presets/`, and `main_figure_site/` remain opt-in and not default-visible.

New artifacts include `source_discovery_candidates`, `doi_license_preflight_report`, `candidate_risk_scores`, `source_discovery_review_queue`, and `extraction_readiness_dashboard`. Pending candidates remain blocked until DOI, OA source, license, and permission review pass.


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
