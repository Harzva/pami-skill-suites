---
module: algorithm
source_skill: generated-canonical-component
version: 0.8.0
status: context-safe-fragment
---

# Algorithm Module

> This is an internal fragment used by the skill-suite router. It is not a default top-level skill.

## Purpose

Help users draft, rewrite, audit, or strengthen the algorithm part of a IEEE manuscript without loading every component skill into the default context.

## When to use

Use when the user asks about algorithm, manuscript structure, evidence quality, or reviewer-risk reduction for this component.

## Inputs needed

- Target journal or journal family.
- Current draft or notes for this component, if available.
- Claimed contribution and supporting evidence.
- Related figures, tables, equations, experiments, or reviewer comments.
- Any official journal constraints already known by the user.

## Output contract

- Diagnosis; revised or generated text; claim-evidence checks; missing evidence; reviewer-risk list; next edits.

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

- algorithm
