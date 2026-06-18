---
module: submission-highlights-file
source_skill: elsevier-submission-highlights-file
version: 0.8.0
status: context-safe-fragment
---

# Elsevier Submission Highlights File Module

> This is an internal fragment used by the skill-suite router. It is not a default top-level skill.

## Purpose

Produce submission-ready assistance for **Elsevier Submission Highlights File** while preserving the user's actual science, separating evidence from interpretation, and preventing fabricated claims, fake citations, fake formatting rules, fake editor policies, or invented compliance statements.

The skill should convert fragmented author material into a rigorous, auditable output: rewritten text, diagnostics, missing-evidence notes, risk register, and a verification checklist tied to official sources.

## When to use

Use this skill when the user needs help with **separate highlights file creation, filename convention, bullet quality, and submission package integration** for a Elsevier journal manuscript or a journal-style revision package.

Use it for Chinese drafts, rough English text, paper outlines, partial LaTeX, experiment tables, figure drafts, reviewer comments, editor letters, submission forms, or final-production checklists. It is designed as a **component skill** that can be invoked directly or routed from a journal adapter such as `pami-writing`, `tip-writing`, `pr-writing`, or `eswa-writing`.

This is an **unofficial** skill. It does not replace the latest official author instructions, journal guide, editorial policy, template, author agreement, copyright form, open-access license form, or submission portal checks.

## Official-source priority

Publisher and journal official pages override this repository, template-paper observations, and model memory. Treat all legal, fee, OA, license, submission-system, and policy information as requiring live verification before real submission.

## Required live checks

- Current journal author instructions or Guide for Authors.
- Submission system and required files.
- Publishing agreement / copyright / license options.
- Open-access choice and fee/APC information, if relevant.
- AI disclosure, ethics, data/code availability, conflict-of-interest, funding, and permission requirements.
- Any article-type, page-limit, figure/table, supplementary, or production-file requirements.

## Output contract

Return the following unless the user requests a narrower output:

- Revised or drafted text for the requested component.
- A structural diagnosis explaining what changed and why.
- Claim-evidence map with unsupported or over-strong claims marked.
- Missing citations, missing experiments, missing baselines, missing statistics, missing declarations, missing permissions, or missing official checks.
- Reviewer-risk list ranked by severity.
- Journal-family compliance reminders tied to official sources, not presented as guaranteed current rules.
- Suggested edits for surrounding sections when the component affects the whole manuscript.
- Explicit assumptions and items that require author confirmation.

## Compliance checklist

- Do not invent author declarations or approvals.
- Use placeholders for unknown facts.
- Separate author-provided facts from repository recommendations.
- Flag all mutable publication rules for live verification.
- Keep copies of official-source links used for the submission package.

## Common risks

- Treating old guide text as current.
- Confusing publisher-wide advice with journal-specific rules.
- Choosing a license or OA option without author/legal confirmation.
- Submitting AI-generated disclosure, COI, funding, or ethics statements that are not true for the authors.

## Safe wording templates

- `Live verification required before submission: [policy or file requirement].`
- `Author confirmation required: [declaration, funding, conflict, rights, data, code, ethics].`
- `Placeholder only; do not submit until verified against the current official journal instructions.`

## Rule provenance classification

- Publisher official rule: current Elsevier publisher-wide policies for publishing agreement, copyright, license, open access, research integrity, AI disclosure, data/code availability, permissions, and production requirements.
- Journal official rule: target journal Guide for Authors / Information for Authors, submission-system file requirements, article-type requirements, page limits, supplementary-material rules, and editor-specific instructions.
- Repository best-practice recommendation: checklist structure, safe wording, reviewer-response matrix, routing, and risk prioritization supplied by this unofficial skill-suite.
- Template-paper observation: open-access template-paper examples may inform structure or wording patterns only; they must not be copied and never override official sources.

## Official source anchors

- Publisher author center: https://www.elsevier.com/researcher/author
- Submission guidance: https://www.elsevier.com/researcher/author/policies-and-guidelines
- Publishing agreement: https://www.elsevier.com/about/policies-and-standards/copyright
- Copyright / license: https://www.elsevier.com/about/policies-and-standards/copyright
- Open access: https://www.elsevier.com/open-access
- Ethics / integrity: https://www.elsevier.com/about/policies-and-standards/publishing-ethics
- AI disclosure policy: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- Data / code availability: https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-guidelines
- Permissions: https://www.elsevier.com/about/policies-and-standards/copyright/permissions

## Live verification warning

Live verification required before submission. Do not finalize author-agreement, copyright, license, OA, APC/fee, AI disclosure, ethics, data/code, permissions, supplementary-material, or final-production decisions from cached repository text alone. Re-open the current publisher and journal pages, record the verification date, and obtain author/legal confirmation where required.
