# Main-Figure Site v2.7.0 Skills


## v2.3.0 — Live DOI/OA Metadata Connector + Candidate Evidence Cards

This release adds a candidate evidence-card system for the 100-paper main-figure workflow. Each candidate now separates DOI evidence, publisher page evidence, repository OA evidence, license evidence, permission evidence, third-party material evidence, and manual reviewer notes. The release remains offline-safe: connector plans for Crossref, OpenAlex, Unpaywall, publisher pages, and institutional repositories are defined, but no live DOI/OA/license verification is claimed in the release build.

Extraction gate policy: no new figure extraction, public gallery hosting, or image reuse is allowed until evidence completeness and manual review pass. Seed assets may remain as structural-analysis metadata, but still require live license and permission re-check before public reuse.

### v2.4.0 evidence-gated promotion

The main-figure corpus now includes an evidence promotion queue, connector simulation report, human reviewer decision log, extraction-ready candidate list, and metadata-only RAG candidate list. This is an offline-safe workflow: it does not certify live DOI/OA/license status and does not authorize new figure extraction without human review.


## v2.4.0 Main-Figure Evidence Promotion Files

The main-figure promotion workflow is not installed as a default skill. To inspect it, open `main_figure_site/data/evidence_promotion_queue.json` or run `python scripts/validate_evidence_promotion.py` in the repository or standalone main-figure site.

## v2.4.0 Evidence-Gated OA Candidate Promotion

v2.4.0 adds an evidence-gated promotion workflow for main-figure OA candidates. It introduces connector simulation reports, candidate evidence diffs, human reviewer decision logs, extraction-ready candidate reports, and metadata-only RAG-ready candidate lists. The default `skills/` layer remains compact; `skills-advanced/`, `expansion_packs/`, `presets/`, and `main_figure_site/` remain opt-in and not default-visible.

Safety: no Sci-Hub, pirated PDFs, paywalled-only PDFs, copyright-unknown PDFs, or unauthorized image reuse. Offline release builds do not approve extraction automatically.

## v2.5.0 installation note

Install `dist/rag-governance.zip` only when you need the metadata-only RAG governance assets. It is optional and not part of the default top-level skills listing.


## v2.6.0 optional RAG evaluation assets

The visual query benchmark and RAG evaluator files are optional analysis assets. They do not add default top-level skills. Use `main_figure_site/data/visual_query_benchmark.json` and related reports for metadata-only retrieval testing.

## v2.7.0 RAG Trace UI + Visual Query Debugger

This release adds a metadata-only RAG trace/debugging layer for the main-figure corpus. It includes trace UI data, debug traces, query rewrite suggestions, missing-tag coverage, corpus expansion recommendations, and a human-evaluation dashboard. Image embedding and public-gallery modes remain blocked until evidence review and human approval pass.

