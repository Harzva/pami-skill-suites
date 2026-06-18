# Installation Guide — Elsevier Skills v2.7.0

Recommended mode remains context-safe:

```text
dist/default-skills.zip
```

Other modes:

```text
dist/compact-suite.zip
dist/advanced-skills.zip
dist/full-suite.zip
dist/presets.zip
dist/visual-patterns.zip
```

Do not install `skills-advanced/`, `expansion_packs/`, or `presets/` as default top-level skills unless your agent can handle a large skill listing.

Visual pattern resources live in `resources/` and `paper_templates/extracted_visual_assets/` and are analysis-only.


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

## v2.4.0 Source Discovery Preflight
### v2.4.0: OA Candidate Source Discovery + DOI/License Preflight

This release adds an offline-safe 100-paper main-figure expansion workflow. It keeps the context-safe architecture unchanged: default `skills/` stays compact, while `skills-advanced/`, `expansion_packs/`, `presets/`, and `main_figure_site/` remain opt-in and not default-visible.

New artifacts include `source_discovery_candidates`, `doi_license_preflight_report`, `candidate_risk_scores`, `source_discovery_review_queue`, and `extraction_readiness_dashboard`. Pending candidates remain blocked until DOI, OA source, license, and permission review pass.


## v2.4.0 Candidate Evidence Cards

This release adds candidate evidence cards for the 100-paper main-figure workflow. Each card separates DOI evidence, publisher page evidence, repository OA evidence, license evidence, permission evidence, third-party material evidence, and manual reviewer notes. The metadata connector plan prepares future Crossref, OpenAlex, Unpaywall, publisher-page, and institutional-repository integration without claiming live verification in the offline release build.

New extraction remains blocked until the extraction gate is unlocked by complete evidence and manual review.

## v2.4.0 Evidence-Gated OA Candidate Promotion

v2.4.0 adds evidence-gated candidate promotion, connector simulation reports, candidate evidence diff reports, a human reviewer decision log, extraction-ready candidate lists, and metadata-only RAG-ready candidate lists. The default `skills/` layer remains context-safe and does not expose `skills-advanced/`, `expansion_packs/`, `presets/`, or `main_figure_site/` as top-level skills.

This is still an offline-safe release build: it does not claim live Crossref/OpenAlex/Unpaywall/publisher/repository verification and does not allow new figure extraction. Real reuse or public display requires DOI, OA source, license, permission, third-party-material, and human-review evidence to pass.

## v2.5.0 installation note

Install `dist/rag-governance.zip` only when you need the metadata-only RAG governance assets. It is optional and not part of the default top-level skills listing.


## v2.6.0 optional RAG evaluation assets

The visual query benchmark and RAG evaluator files are optional analysis assets. They do not add default top-level skills. Use `main_figure_site/data/visual_query_benchmark.json` and related reports for metadata-only retrieval testing.

## v2.7.0 RAG Trace UI + Visual Query Debugger

This release adds a metadata-only RAG trace/debugging layer for the main-figure corpus. It includes trace UI data, debug traces, query rewrite suggestions, missing-tag coverage, corpus expansion recommendations, and a human-evaluation dashboard. Image embedding and public-gallery modes remain blocked until evidence review and human approval pass.

