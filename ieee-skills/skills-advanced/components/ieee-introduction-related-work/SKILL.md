---
name: ieee-introduction-related-work
description: "IEEE Introduction + Related Work: problem-gap-contribution framing and prior-work positioning."
family: ieee
version: 0.5.0
kind: core
status: experimental-unofficial
---

# IEEE Introduction + Related Work Skill

## When to use this skill

Use this skill when the user is preparing, revising, polishing, auditing, or responding to reviews for **IEEE Transactions / Journals** work related to **problem-gap-contribution framing and prior-work positioning**.

Use it for rough notes, Chinese drafts, partial English text, experiment tables, reviewer comments, revision plans, cover letters, response letters, or pre-submission audits.

This is an **unofficial** skill. It does not replace the latest official author instructions, journal guide, editorial policy, template, or submission portal checks.

## Core objective

Produce submission-ready academic assistance for **IEEE Introduction + Related Work** while preserving the user's actual scientific claims and separating evidence from speculation.

The skill should improve structure, language, claim discipline, experimental completeness, reviewer-risk awareness, and package readiness without fabricating results, citations, editorial rules, or author declarations.

## Required inputs

Ask for missing information only when it is essential. If the user already provided partial context, proceed with explicit assumptions.

- Target journal or journal family.
- Article type, if known.
- Working title and research area.
- Research problem, motivation, and practical or theoretical gap.
- Core contributions and novelty relative to prior work.
- Method summary, equations, algorithms, architecture, or system design.
- Datasets, baselines, metrics, experimental settings, and available results.
- Ablations, sensitivity tests, robustness checks, statistical tests, and failure cases.
- Known limitations, ethical constraints, data restrictions, or deployment risks.
- Existing draft text, figures, tables, reviewer comments, or decision letter, if any.
- Desired output type: rewrite, outline, review, response letter, checklist, cover letter, figure/table audit, or full submission-package audit.

## Style profile

- Preferred style: formal, precise, expert-reader, contribution-dense, technically rigorous.
- Typical reviewer risk: weak gap articulation, strawman baselines, insufficient distinction from prior work.
- Avoid unsupported hype, fabricated citations, fabricated experiments, fake acceptance rates, fake reviewer identities, invented policy claims, and stronger-than-evidence conclusions.

## Recommended manuscript map

Abstract; Index Terms; Introduction; Related Work; Method; Theory/Analysis; Experiments; Ablations; Limitations; Conclusion; References; Appendices/Supplementary Materials when needed.

## Writing principles

1. Prefer precise, formal, technical prose over broad editorial storytelling.
2. Make the problem, gap, method novelty, assumptions, and evidence separable.
3. Use Index Terms and terminology consistently across abstract, introduction, method, tables, and conclusion.
4. Treat every formatting rule as a reminder to verify the latest official IEEE author instructions for the target publication.

## Workflow

1. **Fit diagnosis**: identify venue, article type, audience, contribution type, and desk-rejection risks.
2. **Contribution map**: separate problem, gap, method novelty, evidence, limitations, and implications.
3. **Claim-evidence audit**: mark every strong claim as supported, unsupported, needs citation, needs experiment, or should be softened.
4. **Structure rewrite**: improve section order, paragraph logic, terminology, transitions, and figure/table references.
5. **Method and evidence strengthening**: identify missing implementation details, assumptions, baselines, ablations, statistics, complexity, robustness, and failure analysis.
6. **Journal-family adaptation**: adapt tone, section expectations, output assets, and submission package reminders for IEEE Transactions / Journals.
7. **Reviewer-risk reduction**: generate a prioritized risk register with high-impact fixes first.
8. **Official-instruction check**: Verify the current IEEE Author Center, IEEE Template Selector, target journal author instructions, and publication ethics requirements before submission.
9. **Final delivery**: return the requested text plus diagnostics, checklists, and unresolved assumptions.

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

## Reviewer-risk matrix

| Risk area | What to inspect | Safer response |
|---|---|---|
| Novelty | Is the contribution separable from prior work and previous conference versions? | State the exact delta and add evidence or citations. |
| Evidence | Does every claim have data, analysis, citation, or clearly labeled hypothesis status? | Add a claim-evidence map and soften unsupported claims. |
| Experiments | Are baselines, metrics, datasets, ablations, and settings fair and complete? | Propose missing tests in priority order. |
| Reproducibility | Can a reader reproduce the method, settings, environment, and evaluation? | Add implementation details, configs, seeds, splits, and artifact statements. |
| Ethics and integrity | Are citations, declarations, authorship, data rights, and limitations honest? | Use placeholders rather than invented compliance claims. |
| Formatting | Are template, reference, figure, and submission-package assumptions verified? | Add a verification checklist tied to official author instructions. |

## Quality gates

Before finalizing, verify:

- The target journal name is not confused with another publisher, society, or similarly named venue.
- Claims are not stronger than the supplied evidence.
- No fake citations, fake statistics, fake acceptance rates, reviewer identities, or editorial rules are introduced.
- The abstract, introduction, method, experiments, conclusion, and cover/response materials tell the same contribution story.
- Limitations are honest and not self-destructive.
- Formatting reminders are framed as checks against current official instructions, not guaranteed rules.
- AI-assisted writing or editing is presented transparently when relevant and never used to fabricate evidence.

## Refusal and correction behavior

If the user asks to fabricate experiments, citations, peer reviews, editorial decisions, author declarations, approvals, data access, or conflict-of-interest statements, refuse that part and offer a compliant alternative such as a placeholder, search query list, experiment plan, evidence table, or transparent uncertainty note.
