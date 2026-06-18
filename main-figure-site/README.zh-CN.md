# Main-Figure Site Skills


## v2.3.0 — Live DOI/OA Metadata Connector + Candidate Evidence Cards

This release adds a candidate evidence-card system for the 100-paper main-figure workflow. Each candidate now separates DOI evidence, publisher page evidence, repository OA evidence, license evidence, permission evidence, third-party material evidence, and manual reviewer notes. The release remains offline-safe: connector plans for Crossref, OpenAlex, Unpaywall, publisher pages, and institutional repositories are defined, but no live DOI/OA/license verification is claimed in the release build.

Extraction gate policy: no new figure extraction, public gallery hosting, or image reuse is allowed until evidence completeness and manual review pass. Seed assets may remain as structural-analysis metadata, but still require live license and permission re-check before public reuse.

### v2.4.0 evidence-gated promotion

The main-figure corpus now includes an evidence promotion queue, connector simulation report, human reviewer decision log, extraction-ready candidate list, and metadata-only RAG candidate list. This is an offline-safe workflow: it does not certify live DOI/OA/license status and does not authorize new figure extraction without human review.


## v2.4.0 Evidence-Gated Candidate Promotion

本版本新增主图语料的证据门控候选晋升流程，包括 promotion queue、connector simulation report、evidence diff report、human reviewer decision log、extraction-ready candidates 和 metadata-only RAG candidates。该流程仍然是离线安全构建：不声称已经完成 DOI/OA/license 实时核验，也不允许在没有人工复核的情况下抽取新主图。

## v2.4.0 Evidence-Gated OA Candidate Promotion

v2.4.0 adds an evidence-gated promotion workflow for main-figure OA candidates. It introduces connector simulation reports, candidate evidence diffs, human reviewer decision logs, extraction-ready candidate reports, and metadata-only RAG-ready candidate lists. The default `skills/` layer remains compact; `skills-advanced/`, `expansion_packs/`, `presets/`, and `main_figure_site/` remain opt-in and not default-visible.

Safety: no Sci-Hub, pirated PDFs, paywalled-only PDFs, copyright-unknown PDFs, or unauthorized image reuse. Offline release builds do not approve extraction automatically.

## v2.5.0 RAG 治理

## v2.5.0: RAG Ingestion Governance + Retrieval Quality Evaluation

本版本新增 metadata-only RAG governance for the main-figure corpus while keeping image-embedding RAG and public-gallery RAG blocked until permission evidence and human reviewer approval pass.

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

上下文安全架构保持不变: advanced skills, expansion packs, presets, and `main_figure_site/` are not default top-level skills.

Safety policy: only metadata-only seed records may enter RAG in this release. Image embedding and public-gallery use require DOI/OA/license evidence, permission evidence, third-party-material review, and human reviewer approval.


## v2.6.0 视觉检索 Benchmark + 人工检索评测 Trace

本版本新增 metadata-only 视觉检索 benchmark、expected retrieval result cards、human retrieval evaluation traces、retrieval failure taxonomy、query-to-tag coverage matrix 和 RAG evaluator report。默认 `skills/` 仍然保持少量 macro skills；`skills-advanced/`、`expansion_packs/`、`presets/`、`main_figure_site/` 仍然不作为默认顶层 skill 暴露。

当前策略：只允许 seed records 进入 metadata-only RAG。image-embedding RAG 和 public-gallery RAG 仍然关闭，必须等待 DOI/OA/license evidence、permission evidence、第三方素材审查和人工复核通过。

## v2.7.0 RAG Trace UI + Visual Query Debugger

本版本新增 metadata-only RAG trace/debugging 层，包括 trace UI 数据、visual query debug traces、query rewrite suggestions、missing-tag coverage、corpus expansion recommendations 和 human-evaluation dashboard。image embedding 与 public gallery 仍然关闭，必须等 evidence review 和 human approval 通过后才能开启。

