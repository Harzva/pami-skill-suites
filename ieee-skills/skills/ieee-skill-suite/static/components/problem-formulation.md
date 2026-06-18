---
module: problem-formulation
source_skill: ieee-problem-formulation
version: 0.8.0
status: context-safe-fragment
---

# IEEE Problem Formulation Module

> This is an internal fragment used by the skill-suite router. It is not a default top-level skill.

## Purpose

Produce submission-ready assistance for **IEEE Problem Formulation** while preserving the user's actual science, separating evidence from interpretation, and preventing fabricated claims, fake citations, fake formatting rules, fake editor policies, or invented compliance statements.

The skill should convert fragmented author material into a rigorous, auditable output: rewritten text, diagnostics, missing-evidence notes, risk register, and a verification checklist tied to official sources.

## When to use

Use this skill when the user needs help with **problem definition, assumptions, input-output contract, variables, constraints, and task setup** for a IEEE journal manuscript or a journal-style revision package.

Use it for Chinese drafts, rough English text, paper outlines, partial LaTeX, experiment tables, figure drafts, reviewer comments, editor letters, submission forms, or final-production checklists. It is designed as a **component skill** that can be invoked directly or routed from a journal adapter such as `pami-writing`, `tip-writing`, `pr-writing`, or `eswa-writing`.

This is an **unofficial** skill. It does not replace the latest official author instructions, journal guide, editorial policy, template, author agreement, copyright form, open-access license form, or submission portal checks.

## Inputs needed

- Target journal or journal family.
- Current draft or notes for this component, if available.
- Claimed contribution and supporting evidence.
- Related figures, tables, equations, experiments, or reviewer comments.
- Any official journal constraints already known by the user.

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

## Style rules

- Keep claims proportional to evidence.
- Preserve the author’s actual method, data, and results.
- Use precise, formal academic language appropriate for IEEE.
- Do not invent citations, numbers, experiments, policies, declarations, or reviewer identities.
- When formatting is journal-specific, route through the journal module and official-source policy.

## Evidence requirements

- Every quantitative claim must connect to a result, table, figure, metric, citation, or clearly labeled hypothesis.
- Every novelty claim must identify the baseline or prior-work contrast.
- Every limitation or ethical statement must be honest and non-fabricated.

## Reviewer-risk checklist

- Is the component clear to an expert reviewer?
- Are all strong claims evidenced?
- Are terms consistent with abstract, method, results, figures, and tables?
- Are missing baselines, ablations, statistics, or citations explicitly flagged?
- Are journal-specific formatting requirements marked for official-source verification?

## Common failure modes

- Overclaiming beyond supplied evidence.
- Mixing contribution, method, and result claims without traceability.
- Treating repository advice as official journal policy.
- Copying template-paper phrasing instead of learning structure.

## Pairing modules

- Journal module for target venue fit.
- `related-work` for novelty positioning.
- `table`, `figure`, and `caption` when results or visuals are involved.
- `response-letter` when reviewer comments are involved.

## Routing aliases

- ieee-problem-formulation
- problem formulation
- problem-formulation


## v1.9.0 Pattern Library Linkage

This component should consult `resources/motivation_organization_library.json` and `paper_templates/mining_notes/` for reusable organization routines. These routines are structural best practices and visual/paper-mining observations; they do not override publisher or journal official rules.

Required safety reminder: do not copy source-paper wording, captions, figure layouts, table values, or visual designs. Use only abstract organization patterns.
