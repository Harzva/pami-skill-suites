# Journal Skill Suites Main-Figure Gallery + Multimodal RAG Corpus

A standalone main-figure website and multimodal scientific-figure RAG scaffold for Journal Skill Suites v2.7.0.

## Current release: v2.7.0

v2.7.0 adds the metadata-only RAG trace UI, visual query debugging data, query rewrite suggestions, missing-tag coverage, corpus expansion recommendations, and human-evaluation dashboard.

Image embedding and public-gallery reuse remain blocked until evidence review and human approval pass.

## Current seed corpus

- Actual seeded main figures: 11
- Target schema capacity: 100+ legally sourced OA paper main figures
- Status: scaffold-ready, not yet a complete 100-paper corpus

## Directories

```text
docs/                         Static website
gallery/                      Main figure image files for structural analysis
data/main_figure_manifest.*   Corpus manifest
data/main_figure_cards/       One card per seeded figure
data/multimodal_rag_index.*   RAG-ready metadata index
data/visual_tags.*            Visual rhetoric tags
data/license_registry.*       Permission and license review metadata
```

## Copyright safety

Use this site for structural analysis only. Do not copy, redraw, publish, or reuse figures, captions, labels, layouts, or paper-specific claims without verifying the original license, attribution requirements, third-party material status, and target venue policy.

## v2.1.0: 100-Paper OA Expansion Workflow

This site now includes a 100-entry candidate workflow for lawful OA main-figure corpus expansion:

- `data/candidate_papers_100.json`
- `data/oa_source_review_report.json`
- `data/main_figure_extraction_tasks.json`
- `data/main_figure_quality_scores.json`
- `data/duplicate_visual_check_report.json`

Only seed records are actual extracted visual assets. Pending slots are intentionally marked as blocked until source URL, license candidate, OA source type, and permission review are complete.

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


## v2.6.0 Visual Query Benchmark

The standalone site now includes visual query benchmark data, expected retrieval cards, human retrieval evaluation traces, failure taxonomy, query-tag coverage matrix, and RAG evaluator report. Only metadata-only seed records are eligible; image embedding and public-gallery modes remain blocked.

## v2.7.0 RAG Trace UI + Visual Query Debugger

This release adds a metadata-only RAG trace/debugging layer for the main-figure corpus. It includes trace UI data, debug traces, query rewrite suggestions, missing-tag coverage, corpus expansion recommendations, and a human-evaluation dashboard. Image embedding and public-gallery modes remain blocked until evidence review and human approval pass.
