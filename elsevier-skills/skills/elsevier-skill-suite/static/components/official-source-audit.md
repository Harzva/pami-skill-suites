---
module: official-source-audit
source_skill: elsevier-official-source-audit
version: 0.8.0
status: context-safe-fragment
---

# Elsevier Official Source Audit Module

> This is an internal fragment used by the skill-suite router. It is not a default top-level skill.

## Purpose

Audit every Elsevier workflow claim against official sources, separate stable package guidance from target-journal-specific requirements, and produce a verifiable submission-readiness checklist.

The skill should help the agent behave like a reliable academic-product workflow: it should select the right sub-skill, load the smallest useful support context, separate official rules from learned article patterns, preserve the user's real evidence, and prevent fabricated citations, fabricated experiments, fabricated reviewer identities, fabricated policy claims, or inappropriate reuse of copyrighted material.

## When to use

Use this skill when the user needs mapping workflow rules to Elsevier Guide for Authors, target journal instructions, LaTeX/source-package guidance, Highlights, Graphical Abstract, declarations, and GenAI policy checkpoints before making submission-readiness claims. It is designed for product-grade routing, source-grounded auditing, or template-corpus mining inside the `elsevier-skills` repository rather than one-off prose polishing.

Use it for rough research ideas, Chinese drafts, manuscript sections, LaTeX source audits, experiment tables, reviewer comments, response letters, cover letters, or submission-readiness checks. It is especially useful when the user asks which skill to use, why a rule exists, which official materials support a workflow, or how to learn structural patterns from the bundled open-access template papers.

This is an unofficial skill. It must never claim affiliation with Elsevier. It must treat Elsevier Guide for Authors, target journal Guide for Authors, elsarticle/LaTeX instructions, Highlights and Graphical Abstract guidance, and Elsevier journal policies as the source of truth and must explicitly mark any current submission rule that needs verification.

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
- Final checklist for Elsevier Guide for Authors, target journal Guide for Authors, elsarticle/LaTeX instructions, Highlights and Graphical Abstract guidance, and Elsevier journal policies verification.
- Explicit assumptions and items that cannot be guaranteed without target-journal confirmation.

## Style rules

- Keep claims proportional to evidence.
- Preserve the author’s actual method, data, and results.
- Use precise, formal academic language appropriate for Elsevier.
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

- elsevier-official-source-audit
- official source audit
- official-source-audit
