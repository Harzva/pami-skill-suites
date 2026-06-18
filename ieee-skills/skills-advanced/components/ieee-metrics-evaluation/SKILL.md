---
name: ieee-metrics-evaluation
description: "IEEE Metrics Evaluation: metric selection, evaluation definitions, reporting precision, and interpretation boundaries."
family: ieee
version: 0.5.0
kind: core
status: experimental-unofficial
---

# IEEE Metrics Evaluation Skill

## When to use this skill

Use this skill when the user needs help with **metric selection, evaluation definitions, reporting precision, and interpretation boundaries** for a IEEE journal manuscript or a journal-style revision package.

Use it for Chinese drafts, rough English text, paper outlines, partial LaTeX, experiment tables, figure drafts, reviewer comments, editor letters, submission forms, or final-production checklists. It is designed as a **component skill** that can be invoked directly or routed from a journal adapter such as `pami-writing`, `tip-writing`, `pr-writing`, or `eswa-writing`.

This is an **unofficial** skill. It does not replace the latest official author instructions, journal guide, editorial policy, template, author agreement, copyright form, open-access license form, or submission portal checks.

## Core objective

Produce submission-ready assistance for **IEEE Metrics Evaluation** while preserving the user's actual science, separating evidence from interpretation, and preventing fabricated claims, fake citations, fake formatting rules, fake editor policies, or invented compliance statements.

The skill should convert fragmented author material into a rigorous, auditable output: rewritten text, diagnostics, missing-evidence notes, risk register, and a verification checklist tied to official sources.

## Required inputs

Ask for missing information only when it is essential. If the user already provided partial context, proceed with explicit assumptions.

- Target journal and publisher family.
- Article type and manuscript stage: first submission, revision, resubmission, final files, or proof correction.
- Working title, topic, field, and target reader.
- Claimed contributions, novelty, assumptions, and boundary conditions.
- Existing section text, figure/table drafts, equations, algorithms, or data summaries relevant to this task.
- Datasets, baselines, metrics, experiment settings, ablations, uncertainty, and limitations when evidence is involved.
- Prior-publication, preprint, conference-extension, code/data, ethics, funding, competing-interest, and AI-use context when policy-sensitive statements are involved.
- Desired output: rewrite, audit, checklist, section skeleton, reviewer-risk map, response matrix, or submission package item.

## Style profile

- Preferred style: formal, precise, expert-reader, technically rigorous.
- Typical reviewer risk: unsupported novelty, unclear fit, missing evidence, missing citations, inconsistent terminology, non-editable tables, weak captions, poor figure readability, incomplete declarations, or unverifiable policy claims.
- Official source hierarchy: first verify the current IEEE Author Center, IEEE Template Selector, IEEE Editorial Style Manual, target journal instructions, publication policies, and the current submission portal. If official instructions differ from this skill, official instructions win.
- Avoid unsupported hype, fabricated citations, fabricated experiments, fake acceptance rates, fake reviewer identities, invented author agreement terms, and stronger-than-evidence conclusions.

## Recommended manuscript map

Title; Abstract; Index Terms; Introduction; Related Work; Method; Experiments; Results; Discussion; Conclusion; References; Appendices/Supplementary Materials.

This skill focuses on the **ieee metrics evaluation** layer, but it should always maintain consistency with the full manuscript: abstract claims must match experiments, figure captions must match results, related work must match contributions, and submission statements must match author-controlled facts.

## Writing principles

1. Preserve scientific truth over fluency. Never invent experiments, citations, approvals, author contributions, funding, conflicts, data availability, or policy compliance.
2. Convert broad claims into auditable claim-evidence pairs.
3. Make terminology consistent across title, abstract, keywords/index terms, section headings, figures, tables, captions, and conclusion.
4. Prefer concrete method/evidence language over vague promotional language.
5. When the task touches formatting, rights, licenses, data, AI usage, or submission requirements, frame output as a checklist requiring official verification.
6. Keep captions, tables, and figures self-consistent: every visual item should be cited in text, numbered in order, readable, and supported by the manuscript narrative.
7. For related work and novelty claims, distinguish what prior work did, what the current manuscript changes, and what evidence proves the delta.
8. For response or revision tasks, connect every promised change to a specific manuscript location or transparent reason for not changing.

## Workflow

1. **Task diagnosis**: determine whether the user needs drafting, rewriting, auditing, routing, formatting, or policy verification.
2. **Official-source boundary**: identify which parts are stable writing guidance and which require current publisher/journal/source verification.
3. **Input normalization**: extract claims, evidence, section role, terminology, numbers, citations, figures/tables, and missing facts.
4. **Claim-evidence audit**: label each important claim as supported, unsupported, needs citation, needs experiment, needs softening, or should be removed.
5. **Component rewrite or construction**: produce the requested section, table, figure plan, caption, checklist, statement, or response item using target-family style.
6. **Cross-manuscript consistency check**: verify that terminology, numbers, contributions, limitations, figures, tables, and citations agree with each other.
7. **Reviewer-risk reduction**: rank risks by expected editorial impact: fatal fit/policy risks first, then evidence gaps, then clarity and style.
8. **Official-instruction check**: list exact official pages or policy categories the author must verify before submission.
9. **Final delivery**: return the artifact plus diagnostics, unresolved assumptions, and next edits.

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

## Reviewer-risk matrix

| Risk area | What to inspect | Safer response |
|---|---|---|
| Fit | Does this component make the journal choice obvious? | Add a scope-fit sentence and remove claims outside the venue's core audience. |
| Novelty | Is the contribution separable from prior work or prior conference versions? | State the exact delta and add evidence or citations. |
| Evidence | Does every claim have data, analysis, citation, theory, or clearly labeled limitation status? | Add evidence, soften the claim, or convert it to a hypothesis. |
| Experiments | Are baselines, metrics, datasets, splits, ablations, and settings fair and complete? | Add missing tests in priority order and disclose constraints. |
| Visuals | Are figures/tables/captions readable, cited in order, non-duplicative, and consistent with numbers in text? | Rewrite captions, simplify visuals, and align narrative to data. |
| Reproducibility | Can a reader reconstruct the method, settings, data handling, and evaluation? | Add implementation details, seeds, splits, hyperparameters, code/data statements, or limitations. |
| Policy | Are author agreement, copyright, license, permissions, AI-use, preprint, and competing-interest statements true? | Use placeholders and verification checklists instead of invented compliance claims. |
| Style | Is the prose too promotional, vague, or conference-like for a journal article? | Use formal, precise, evidence-led phrasing and remove unsupported adjectives. |

## Quality gates

Before finalizing, verify:

- The output is compatible with the target journal family and does not confuse IEEE, Elsevier, ACM, Springer, Nature, Science, or Cell conventions.
- Claims are not stronger than supplied evidence.
- No fake citations, fake statistics, fake policy statements, fake permissions, fake reviewer identities, or fake editorial decisions are introduced.
- Figures, tables, captions, equations, algorithms, and references are cited consistently when they appear.
- Related work positions novelty without misrepresenting prior studies.
- Limitations and ethics statements are honest and not self-destructive.
- Any author agreement, copyright, open-access, APC, license, or publishing-rights guidance is framed as an official-source verification item.
- AI-assisted writing or editing is transparent when relevant and never used to fabricate evidence.

## Refusal and correction behavior

If the user asks to fabricate experiments, citations, peer reviews, editorial decisions, author declarations, approvals, data access, permission letters, author contributions, conflicts of interest, funding, copyright ownership, or agreement signatures, refuse that part and offer a compliant alternative: a placeholder statement, verification checklist, experiment plan, evidence table, permission-request template, or transparent uncertainty note.
