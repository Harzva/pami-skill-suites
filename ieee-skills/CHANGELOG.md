# Changelog

## v2.0.0 — Visual Rhetoric Analyzer + Figure/Table/Caption Pattern Library

- Added visual rhetoric report and dashboard.
- Added figure, table, and caption pattern libraries.
- Added experiment/formula/motivation/limitations/conclusion routine libraries.
- Added visual asset review queue and validation scripts.
- Added GitHub Pages pages for visual pattern analysis and section routines.
- Preserved context-safe architecture: advanced skills, expansion packs, and presets remain opt-in.

## v1.8.0 - Live Source Check Automation + Release Health Dashboard

- Added `scripts/live_source_check_matrix.py`.
- Added `scripts/source_age_policy.py`.
- Added `scripts/release_health_dashboard.py`.
- Added `scripts/generate_source_badges.py`.
- Added `.github/workflows/source-refresh.yml` scheduled maintenance workflow.
- Added `resources/live_source_check_matrix.*`.
- Added `resources/source_age_policy_report.*`.
- Added `resources/release_health_dashboard.*`.
- Added `resources/source_badges.*`.
- Added source maintenance documentation pages.
- Added issue templates for stale official links, source refresh requests, and preset scenario updates.
- Preserved context-safe compact architecture: default `skills/` remains small, while advanced skills, expansion packs, and presets remain opt-in.


## v1.4.0 - Discipline-Specific Preset Routers

- Added optional discipline preset routers under `presets/`.
- Added preset registry and coverage matrix resources.
- Added preset validation, build, and router-preview scripts.
- Added preset distribution zips.
- Added GitHub Pages documentation for presets, preview, and discipline workflows.
- Preserved compact default `skills/`; presets remain opt-in and not default-visible.


## v1.3.0 - Discipline Pack Hardening + L0→L3 Promotion Workflow

- Added source-quality scoring for expansion-pack journal entries.
- Added promotion workflow for L0 candidate journals.
- Added pack-specific evaluation task placeholders and paper-card todo lists.
- Added coverage diff, source-quality, and pack-maturity reports.
- Added docs for promotion, source-quality scoring, and coverage diffs.
- Preserved context-safe compact architecture; advanced skills remain opt-in.

## v1.3.0 - Official Link Refresh + Community Contribution Workflow

- Added `scripts/check_official_links_live.py` and `scripts/report_stale_sources.py`.
- Added `resources/source_refresh_report.json` and `resources/source_refresh_report.yaml`.
- Added source-refresh metadata to 22 journal fragments.
- Added contributor templates for journal fragments, component fragments, paper cards, and official-source updates.
- Added GitHub Pages documentation for contribution workflow, source verification, and release maintenance.
- Preserved context-safe compact architecture; advanced skills remain opt-in.

## v1.3.0 — Public Release + GitHub Pages + Plugin Packaging

Released: 2026-06-12

This release turns the repository into a public-release-ready journal skill-suite.

### Added

- Final public README and Chinese README.
- Final installation guide with default, compact, advanced, full, and plugin modes.
- GitHub Pages product site with architecture, context safety, official-source, paper-template, evaluation, benchmark, examples, and FAQ pages.
- Plugin packaging metadata under `plugins/` and generated plugin zip bundles under `dist/`.
- `release-notes.md` and `FINAL_VALIDATION_REPORT.md`.
- Public release checklist, citation instructions, badges, and nature-skills comparison.
- `scripts/validate_plugins.py` release gate.

### Preserved

- Context-safe compact architecture from v0.6.0.
- Official-source compliance layer from v0.7.0.
- Template paper corpus and paper mining from v0.8.0.
- Evaluation tasks, rubrics, and sample outputs from v0.9.0.

### Important

This project is unofficial and is not affiliated with IEEE. Mutable publishing details require live verification before real submission.

---

## v0.8.0 - Official-Source Deep Compliance

- Kept context-safe compact architecture from v0.6.0.
- Added `resources/official_source_registry.yaml` and `.json`.
- Added `scripts/validate_official_links.py` and `scripts/validate_live_verification_warnings.py`.
- Strengthened `scripts/validate_sources.py` for journal official-source matrices and submission/legal live verification warnings.
- Added rule provenance classification to submission/legal fragments.
- Updated GitHub Pages official-source, compliance, and journal-source-map pages.
- Regenerated default / compact / advanced / full distributions.

## v0.6.0 - Context-Safe Compact Architecture

- Reduced default-visible skills to 8 macro skills.
- Moved journal, component, and submission details into skill-suite static fragments.
- Preserved independent skills under `skills-advanced/`.
- Added context budget, manifest, route, source, distribution, and smoke-test validation scripts.
- Added default / compact / advanced / full distribution packages.
- Updated GitHub Pages product site for context-safe architecture.

## v0.5.0 - Skill-Suite Router Architecture

- Added suite-level router skill `ieee-skill-suite`.
- Added component router `ieee-component-router` and submission router `ieee-submission-router`.
- Upgraded journal router `ieee-journal-router`.
- Added JSON/YAML registries for skills, journals, components, submission tasks, and routing rules.
- Added deterministic routing CLI and registry/route validation scripts.
- Added compact one-skill distribution under `dist/compact-suite/`.
- Added full-suite distribution notes under `dist/full-suite/`.
- Updated GitHub Pages website with router and compact-suite pages.
- Updated README and Chinese README for full-suite vs compact-suite installation.


## v0.5.0 - Skill-Suite Router Architecture

- Added suite-level router skill `ieee-skill-suite`.
- Added component router `ieee-component-router` and submission router `ieee-submission-router`.
- Upgraded journal router `ieee-journal-router`.
- Added JSON/YAML registries for skills, journals, components, submission tasks, and routing rules.
- Added deterministic routing CLI and registry/route validation scripts.
- Added compact one-skill distribution under `dist/compact-suite/`.
- Added full-suite distribution notes under `dist/full-suite/`.
- Updated GitHub Pages website with router and compact-suite pages.
- Updated README and Chinese README for full-suite vs compact-suite installation.


## v0.5.0 - Skill-Suite Router Architecture

- Added suite-level router skill `ieee-skill-suite`.
- Added component router `ieee-component-router` and submission router `ieee-submission-router`.
- Upgraded journal router `ieee-journal-router`.
- Added JSON/YAML registries for skills, journals, components, submission tasks, and routing rules.
- Added deterministic routing CLI and registry/route validation scripts.
- Added compact one-skill distribution under `dist/compact-suite/`.
- Added full-suite distribution notes under `dist/full-suite/`.
- Updated GitHub Pages website with router and compact-suite pages.
- Updated README and Chinese README for full-suite vs compact-suite installation.


## v0.3.0 - 2026-06-11

Product-grade upgrade toward nature-skills-style usability.

- Added explicit product design philosophy docs in English and Chinese.
- Added official source map and machine-readable source JSON.
- Added paper template corpus with bundled open-access/CC-BY PDFs and official/reference templates.
- Added per-paper template analysis notes.
- Added meta/router skills for journal routing, official-source auditing, and template-paper mining.
- Added README.zh-CN.md.
- Strengthened shared policies for source grounding and template-paper use.
- Updated all skill front matter to version 0.3.0.

## 0.2.0 - 2026-06-11

### Added

- Expanded skill coverage with additional core workflow skills and journal adapters.
- Added shared policies for official-source verification, claim-evidence discipline, reproducibility, ethics, limitations, and publication integrity.
- Added per-skill `writing-patterns.md`, `reviewer-risk-map.md`, `quality-gate.md`, `evidence-checklist.md`, and `example-output-skeleton.md`.
- Added `scripts/build_manifest.py`, `scripts/quality_score.py`, and `scripts/new_skill.py`.
- Upgraded `scripts/validate_structure.py` with deeper section and support-file checks.
- Added GitHub issue templates, pull request template, and validation workflow.
- Added resource index files for downstream automation.

### Changed

- Normalized all skill front matter to version `0.2.0`.
- Strengthened anti-hallucination and official-instruction verification language.

## 0.1.0

- Initial repository skeleton with core writing/review/response skills and first journal adapters.
## 0.4.0 - 2026-06-11

- Added GitHub Pages promotional website under `docs/`.
- Added granular manuscript component skills: table, figure, caption, related work, author agreement, copyright, open access, and more.
- Added per-journal official-link files and author-agreement notes.
- Added repository polish files and Pages deployment workflow.
- Added source topology resources and component coverage matrix.


## v1.3.0 Journal Coverage Expansion Packs

- Added opt-in `expansion_packs/` for computer vision, medical AI, remote sensing, multimedia, data mining, and signal processing.
- Added coverage maturity levels L0–L4.
- Added `resources/journal_coverage_dashboard.json` and `.yaml`.
- Added `scripts/validate_expansion_packs.py`, `scripts/build_expansion_pack.py`, and `scripts/coverage_dashboard.py`.
- Preserved compact default `skills/` visibility; advanced and expansion coverage remain opt-in.


## v1.5.0

Added preset evaluation harness and user scenario gallery.


## v1.8.0 — Source Trust Tiers + Human Review Queue

- Added source trust tiers: publisher-official, journal-official, society-official, repository-best-practice, template-paper-observation, and unverified-candidate.
- Added human review queue for high-risk mutable links, stale links, missing author-instruction/copyright/license/AI-disclosure links, and L0/L1 expansion-pack candidates.
- Added source review scripts, resources, and GitHub Pages documentation.
- Preserved context-safe compact architecture; advanced skills, expansion packs, and presets remain opt-in.

## v1.8.0 - Policy Diff Engine + Visual Gallery

- Added source snapshot and policy diff engine.
- Added official source change log and affected-fragments report.
- Added visual gallery extraction from lawful corpus PDFs.
- Added visual-gallery package and policy-diff package to distributions.
- Added GitHub Pages pages for policy diff, snapshots, affected fragments, and visual gallery.


## v1.8.0: Policy Diff + Visual Asset Analysis Layer

This release adds official-source snapshots, a policy diff engine, affected-fragment reporting, and `paper_templates/extracted_visual_assets/`. Extracted main figures, motivation/framework figures, and representative tables are separated for structure analysis only; they are not reusable publication assets unless the original source license and attribution requirements are re-checked.


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


## v2.4.0 - Evidence-Gated OA Candidate Promotion + Connector Simulation Reports

Added evidence promotion queues, connector simulation reports, candidate evidence diffs, human reviewer decision logs, extraction-ready candidate lists, RAG-ready metadata candidate lists, validation scripts, and GitHub Pages documentation.

## v2.4.0 Evidence-Gated OA Candidate Promotion

v2.4.0 adds an evidence-gated promotion workflow for main-figure OA candidates. It introduces connector simulation reports, candidate evidence diffs, human reviewer decision logs, extraction-ready candidate reports, and metadata-only RAG-ready candidate lists. The default `skills/` layer remains compact; `skills-advanced/`, `expansion_packs/`, `presets/`, and `main_figure_site/` remain opt-in and not default-visible.

Safety: no Sci-Hub, pirated PDFs, paywalled-only PDFs, copyright-unknown PDFs, or unauthorized image reuse. Offline release builds do not approve extraction automatically.

## v2.5.0

- Added RAG ingestion governance, eligibility report, retrieval benchmark, safety filter, quality dashboard, scripts, docs, and optional `dist/rag-governance.zip`.


## v2.6.0 - Visual Query Benchmark + Human Retrieval Evaluation Traces

- Added `visual_query_benchmark.*`.
- Added `expected_retrieval_results.*`.
- Added `human_retrieval_eval_traces.*`.
- Added `retrieval_failure_taxonomy.*`.
- Added `query_tag_coverage_matrix.*`.
- Added `rag_evaluator_report.*`.
- Added validation/build scripts for the benchmark assets.
- Added GitHub Pages pages for benchmark, human evaluation, failure taxonomy, and evaluator report.


## v2.7.0 — RAG Trace UI + Visual Query Debugger

- Preserves context-safe compact architecture and keeps advanced/preset/main-figure assets out of default top-level skills.
- Adds RAG trace UI index, visual query debug traces, query rewrite suggestions, missing-tag coverage report, corpus expansion recommendations, and human-evaluation dashboard.
- Keeps metadata-only seed RAG allowed while image-embedding and public-gallery RAG remain blocked until evidence and human approval pass.
- Adds GitHub Pages documentation for RAG trace UI, visual query debugging, query rewriting, corpus expansion recommendations, and human-evaluation dashboard.
- Strictly prohibits Sci-Hub, pirated PDFs, paywalled-only PDFs, copyright-unknown PDFs, and unauthorized image reuse.
