# IEEE Skills v2.7.0

[![Version](https://img.shields.io/badge/version-v2.7.0-blue)](./release-notes.md) [![Context Safe](https://img.shields.io/badge/context--safe-compact--by--default-brightgreen)](./docs/context-safety.html) [![Visual Patterns](https://img.shields.io/badge/visual%20patterns-v2.7.0-purple)](./docs/visual-rhetoric-analyzer.html) [![Official Sources](https://img.shields.io/badge/official%20sources-live%20check%20required-yellow)](./docs/live-source-checks.html) [![License](https://img.shields.io/badge/license-MIT-lightgrey)](./LICENSE)

Context-safe AI-agent skill-suite for IEEE journal manuscripts.

This repository is **unofficial** and is not affiliated with IEEE. It does not provide legal advice and does not replace the latest official instructions from the publisher, target journal, society owner, or submission system.

## Current release: v2.7.0

v2.7.0 is the current public release. It adds a metadata-only RAG trace UI and visual query debugger while preserving the compact default skill surface.

Release gates remain conservative: image embedding, new figure extraction, and public-gallery reuse stay blocked until DOI/OA/license evidence, permission evidence, third-party-material review, and human approval pass.

## What v2.0.0 adds

v2.0.0 adds a **Visual Rhetoric Analyzer + Figure/Table/Caption Pattern Library**, plus structural routine libraries for:

- experiment organization;
- formula / equation organization;
- motivation organization;
- future limitations and future work;
- conclusion writing.

It keeps the context-safe architecture intact:

```text
skills/            default macro skills only
skills-advanced/   optional independent skills, not default-visible
expansion_packs/   optional discipline coverage packs
presets/           optional preset routers and scenario galleries
```

Default macro skills: **8**.

## New v2.0.0 resources

```text
resources/visual_rhetoric_report.json
resources/figure_pattern_library.json
resources/table_pattern_library.json
resources/caption_pattern_library.json
resources/visual_asset_review_queue.json
resources/visual_style_dashboard.json
resources/section_routine_library.json
resources/experiment_organization_library.json
resources/formula_organization_library.json
resources/motivation_organization_library.json
resources/limitations_future_work_library.json
resources/conclusion_organization_library.json
```

## Visual asset safety

The extracted visual assets are for **visual-structure analysis only**. Do not copy, redraw, publish, or reuse figures, tables, captions, labels, or layouts from source papers without verifying license, attribution, third-party material status, and target venue policy.

## Future v2.0.0 target

A separate main-figure website and multimodal scientific-figure RAG corpus with at least 100 legally sourced OA main-figure papers.

See:

- [Visual Rhetoric Analyzer](./docs/visual-rhetoric-analyzer.html)
- [Figure Pattern Library](./docs/figure-pattern-library.html)
- [Table Pattern Library](./docs/table-pattern-library.html)
- [Caption Pattern Library](./docs/caption-pattern-library.html)
- [Section Routine Library](./docs/section-routine-library.html)
- [Main-Figure RAG Roadmap](./docs/main-figure-rag-roadmap.html)


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


## v2.3.0 Candidate Evidence Cards

This release adds candidate evidence cards for the 100-paper main-figure workflow. Each card separates DOI evidence, publisher page evidence, repository OA evidence, license evidence, permission evidence, third-party material evidence, and manual reviewer notes. The metadata connector plan prepares future Crossref, OpenAlex, Unpaywall, publisher-page, and institutional-repository integration without claiming live verification in the offline release build.

New extraction remains blocked until the extraction gate is unlocked by complete evidence and manual review.

### v2.4.0 evidence-gated promotion

The main-figure corpus now includes an evidence promotion queue, connector simulation report, human reviewer decision log, extraction-ready candidate list, and metadata-only RAG candidate list. This is an offline-safe workflow: it does not certify live DOI/OA/license status and does not authorize new figure extraction without human review.


## v2.4.0 Evidence-Gated Candidate Promotion

This release adds an evidence-gated candidate promotion workflow for the main-figure corpus. It adds promotion queues, connector simulation reports, evidence diff reports, human reviewer decision logs, extraction-ready candidate lists, and metadata-only RAG candidate lists. The workflow remains offline-safe: no live DOI/OA/license lookup is claimed, and no new figure extraction is allowed without human review.

## v2.4.0 Evidence-Gated OA Candidate Promotion

v2.4.0 adds an evidence-gated promotion workflow for main-figure OA candidates. It introduces connector simulation reports, candidate evidence diffs, human reviewer decision logs, extraction-ready candidate reports, and metadata-only RAG-ready candidate lists. The default `skills/` layer remains compact; `skills-advanced/`, `expansion_packs/`, `presets/`, and `main_figure_site/` remain opt-in and not default-visible.

Safety: no Sci-Hub, pirated PDFs, paywalled-only PDFs, copyright-unknown PDFs, or unauthorized image reuse. Offline release builds do not approve extraction automatically.

## v2.5.0 RAG Governance

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


## v2.6.0 Visual Query Benchmark + Human Retrieval Evaluation Traces

This release adds a metadata-only visual query benchmark, expected retrieval result cards, human retrieval evaluation trace templates, retrieval failure taxonomy, query-to-tag coverage matrix, and RAG evaluator report. The default `skills/` layer remains compact; `skills-advanced/`, `expansion_packs/`, `presets/`, and `main_figure_site/` remain opt-in and not default-visible.

Current policy: metadata-only seed records may be used for safe retrieval summaries. Image-embedding RAG and public-gallery RAG remain blocked until DOI/OA/license evidence, permission evidence, third-party-material review, and human reviewer approval pass.

## v2.7.0 RAG Trace UI + Visual Query Debugger

This release adds a metadata-only RAG trace/debugging layer for the main-figure corpus. It includes trace UI data, debug traces, query rewrite suggestions, missing-tag coverage, corpus expansion recommendations, and a human-evaluation dashboard. Image embedding and public-gallery modes remain blocked until evidence review and human approval pass.
