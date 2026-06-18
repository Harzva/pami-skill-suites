---
module: ai-disclosure
source_skill: generated-canonical-submission
version: 0.8.0
status: context-safe-fragment
---

# Ai Disclosure Module

> This is an internal fragment used by the skill-suite router. It is not a default top-level skill.

## Purpose

Handle the ai disclosure part of a Elsevier manuscript workflow while keeping legal, publication, and policy claims source-grounded.

## When to use

Use when the user asks about ai disclosure, submission assets, revision materials, author declarations, rights, licenses, or final files.

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

- Compliance-aware checklist; safe draft wording; missing fields; official links to verify; unresolved assumptions; risk register.

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
