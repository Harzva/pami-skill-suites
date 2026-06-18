# IEEE Skills v2.7.0

面向 IEEE 期刊投稿的上下文安全型 Journal Skill-Suite。本仓库为非官方项目，不隶属于 IEEE。

## 当前发布版本：v2.7.0

v2.7.0 是当前公开发布版本，新增 metadata-only RAG trace UI 与 visual query debugger，同时保持默认 skill 列表紧凑。

图像 embedding、新图提取和公开图库复用仍然关闭，必须等 DOI/OA/license 证据、权限证据、第三方材料审查和人工审批通过后才能解锁。

## v2.0.0 新增内容

本版新增：

- Visual Rhetoric Analyzer；
- 主图 / 动机图 pattern library；
- 漂亮表格 pattern library；
- caption pattern library；
- 实验组织套路；
- 公式 / equation 组织套路；
- 动机组织套路；
- 未来局限 / future work 组织套路；
- 总结 conclusion 组织套路。

继续保持上下文安全架构：

```text
skills/            只放少量默认 macro skills
skills-advanced/   高级可选独立 skills，不默认暴露
expansion_packs/   可选学科扩展包，不默认暴露
presets/           可选 preset routers，不默认暴露
```

默认 macro skills 数量：**8**。

## 重要版权说明

视觉资产只用于结构分析，不能直接复制、重画、发表或当作可复用素材。真实复用前必须检查原论文 license、署名要求、第三方材料状态和目标期刊政策。

## v2.0.0 目标

后续将单独做论文主图网站和多模态科研绘图 RAG 知识库，目标至少 100 篇合法 OA 论文主图。


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

## v2.1.0 更新：100 篇 OA 论文主图扩展工作流

本版本加入了面向 100 篇合法 OA 论文主图的候选注册表、来源预审、抽取任务、质量评分和重复视觉检查流程。仍然保持 context-safe compact architecture：`skills-advanced/`、`expansion_packs/`、`presets/`、`main_figure_site/` 都不会默认暴露为 top-level skills。

当前注册表会区分已有 seed 主图和待收集 candidate slot。待收集条目不是已验证论文，必须完成 source URL、license、OA source type 和 permission review 后才能抽取主图。严格禁止 Sci-Hub、盗版 PDF、付费墙 PDF、版权不明 PDF 和未授权图片复用。

## v2.3.0 Source Discovery Preflight
### v2.3.0: OA Candidate Source Discovery + DOI/License Preflight

This release adds an offline-safe 100-paper main-figure expansion workflow. It keeps the context-safe architecture unchanged: default `skills/` stays compact, while `skills-advanced/`, `expansion_packs/`, `presets/`, and `main_figure_site/` remain opt-in and not default-visible.

New artifacts include `source_discovery_candidates`, `doi_license_preflight_report`, `candidate_risk_scores`, `source_discovery_review_queue`, and `extraction_readiness_dashboard`. Pending candidates remain blocked until DOI, OA source, license, and permission review pass.


## v2.3.0 候选证据卡与 Metadata Connector 计划

本版本为主图网站 / RAG workflow 增加候选证据卡系统。每个候选论文都会区分 DOI 证据、出版社页面证据、机构仓储 OA 证据、license 证据、permission 证据、第三方素材证据和人工复核备注。v2.3.0 仍然是离线安全构建，不声称已经完成 Crossref / OpenAlex / Unpaywall / 出版社页面的 live lookup。

在 extraction gate 解锁之前，禁止新增抽图、公开展示或复用任何主图资产。

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
