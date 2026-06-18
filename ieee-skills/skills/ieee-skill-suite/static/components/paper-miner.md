---
module: paper-miner
source_skill: ieee-template-paper-miner
version: 0.8.0
status: context-safe-fragment
---

# IEEE Template Paper Miner Module

> This is an internal fragment used by the skill-suite router. It is not a default top-level skill.

## Purpose

Mine IEEE open-access template papers for section morphology, evidence layout, figure/table function, and reviewer-risk lessons while preventing content copying or policy overgeneralization.

The skill should help the agent behave like a reliable academic-product workflow: it should select the right sub-skill, load the smallest useful support context, separate official rules from learned article patterns, preserve the user's real evidence, and prevent fabricated citations, fabricated experiments, fabricated reviewer identities, fabricated policy claims, or inappropriate reuse of copyrighted material.

## When to use

Use this skill when the user needs using the bundled CC-BY/open-access IEEE template corpus to extract structural patterns without copying scientific content. It is designed for product-grade routing, source-grounded auditing, or template-corpus mining inside the `ieee-skills` repository rather than one-off prose polishing.

Use it for rough research ideas, Chinese drafts, manuscript sections, LaTeX source audits, experiment tables, reviewer comments, response letters, cover letters, or submission-readiness checks. It is especially useful when the user asks which skill to use, why a rule exists, which official materials support a workflow, or how to learn structural patterns from the bundled open-access template papers.

This is an unofficial skill. It must never claim affiliation with IEEE. It must treat IEEE Author Center, IEEE Template Selector, IEEE Editorial Style Manual, target publication instructions, and IEEE publication policies as the source of truth and must explicitly mark any current submission rule that needs verification.

## Inputs needed

- Target journal or journal family.
- Current draft or notes for this component, if available.
- Claimed contribution and supporting evidence.
- Related figures, tables, equations, experiments, or reviewer comments.
- Any official journal constraints already known by the user.

## Output contract

Return the following unless the user requested a narrower output:

- Recommended skill or skill sequence, with rationale.
- Source-grounding map: official rule, repository convention, template-paper pattern, or unresolved verification item.
- Revised or drafted text if a writing task was requested.
- Claim-evidence map and missing-evidence list.
- Reviewer-risk register with severity, likely reviewer concern, and mitigation.
- Template-paper lessons, limited to structural observations.
- Final checklist for IEEE Author Center, IEEE Template Selector, IEEE Editorial Style Manual, target publication instructions, and IEEE publication policies verification.
- Explicit assumptions and items that cannot be guaranteed without target-journal confirmation.

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

- ieee-template-paper-miner
- paper miner
- paper-miner
