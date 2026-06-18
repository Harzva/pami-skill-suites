---
module: method
source_skill: ieee-method-algorithm
version: 0.8.0
status: context-safe-fragment
---

# IEEE Method + Algorithm Module

> This is an internal fragment used by the skill-suite router. It is not a default top-level skill.

## Purpose

Produce submission-ready academic assistance for **IEEE Method + Algorithm** while preserving the user's actual scientific claims and separating evidence from speculation.

The skill should improve structure, language, claim discipline, experimental completeness, reviewer-risk awareness, and package readiness without fabricating results, citations, editorial rules, or author declarations.

## When to use

Use this skill when the user is preparing, revising, polishing, auditing, or responding to reviews for **IEEE Transactions / Journals** work related to **method exposition, notation, algorithms, architecture, and implementation clarity**.

Use it for rough notes, Chinese drafts, partial English text, experiment tables, reviewer comments, revision plans, cover letters, response letters, or pre-submission audits.

This is an **unofficial** skill. It does not replace the latest official author instructions, journal guide, editorial policy, template, or submission portal checks.

## Inputs needed

- Target journal or journal family.
- Current draft or notes for this component, if available.
- Claimed contribution and supporting evidence.
- Related figures, tables, equations, experiments, or reviewer comments.
- Any official journal constraints already known by the user.

## Output contract

Return the following unless the user requests a narrower output:

- Revised or drafted text.
- Structural diagnosis.
- Claim-evidence map.
- Venue-fit and reviewer-risk list.
- Missing experiments, baselines, citations, limitations, declarations, or formatting checks.
- Suggested figure/table/storyline changes.
- Final submission-readiness checklist.
- Explicit assumptions and items that require official source verification.

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

- ieee-method-algorithm
- method
