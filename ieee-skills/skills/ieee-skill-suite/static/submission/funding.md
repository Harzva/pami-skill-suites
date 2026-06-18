---
module: funding
source_skill: generated-canonical-submission
version: 0.8.0
status: context-safe-fragment
---

# Funding Module

> This is an internal fragment used by the skill-suite router. It is not a default top-level skill.

## Purpose

Handle the funding part of a IEEE manuscript workflow while keeping legal, publication, and policy claims source-grounded.

## When to use

Use when the user asks about funding, submission assets, revision materials, author declarations, rights, licenses, or final files.

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

- Publisher official rule: current IEEE publisher-wide policies for publishing agreement, copyright, license, open access, research integrity, AI disclosure, data/code availability, permissions, and production requirements.
- Journal official rule: target journal Guide for Authors / Information for Authors, submission-system file requirements, article-type requirements, page limits, supplementary-material rules, and editor-specific instructions.
- Repository best-practice recommendation: checklist structure, safe wording, reviewer-response matrix, routing, and risk prioritization supplied by this unofficial skill-suite.
- Template-paper observation: open-access template-paper examples may inform structure or wording patterns only; they must not be copied and never override official sources.

## Official source anchors

- Publisher author center: https://journals.ieeeauthorcenter.ieee.org/
- Submission guidance: https://journals.ieeeauthorcenter.ieee.org/submit-your-article-for-peer-review/the-ieee-article-submission-process/
- Publishing agreement: https://journals.ieeeauthorcenter.ieee.org/choose-a-publishing-agreement/
- Copyright / license: https://journals.ieeeauthorcenter.ieee.org/choose-a-publishing-agreement/about-the-ieee-copyright-form/
- Open access: https://journals.ieeeauthorcenter.ieee.org/choose-a-publishing-agreement/open-access-rights-management/
- Ethics / integrity: https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/
- AI disclosure policy: https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/
- Data / code availability: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/research-reproducibility/
- Permissions: https://journals.ieeeauthorcenter.ieee.org/choose-a-publishing-agreement/avoid-infringement-upon-ieee-copyright/

## Live verification warning

Live verification required before submission. Do not finalize author-agreement, copyright, license, OA, APC/fee, AI disclosure, ethics, data/code, permissions, supplementary-material, or final-production decisions from cached repository text alone. Re-open the current publisher and journal pages, record the verification date, and obtain author/legal confirmation where required.
