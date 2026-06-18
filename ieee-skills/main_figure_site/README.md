# IEEE Main-Figure Gallery + RAG Scaffold

A standalone main-figure website and multimodal scientific-figure RAG scaffold for Journal Skill Suites v2.0.0.

## Current seed corpus

- Actual seeded main figures: 5
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
