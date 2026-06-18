---
name: elsevier-component-router
description: "Elsevier Component Router: detect manuscript components such as table, figure, caption, related work, method, experiment, ablation, references, declarations, and route them to the correct component skills. Use for Elsevier AI, computer vision, pattern recognition, expert systems, information science, and medical AI journals."
family: elsevier
version: 0.5.0
kind: router
status: experimental-unofficial
---

# Elsevier Component Router

## When to use this skill

Use this skill when the user needs routing, orchestration, or skill selection inside the **Elsevier Skills** repository. The router is especially useful when a request mentions multiple manuscript details, mixes target-journal style with policy-sensitive submission work, or needs a single output assembled from several independent skills.

This is an unofficial product-layer skill. It helps select and coordinate skills, but it does not replace the latest Elsevier author instructions, journal guide, editorial policy, template, author agreement, copyright form, open-access license form, or submission portal checks.

## Core objective

Route a manuscript task to the smallest sufficient chain of journal adapters, component skills, and submission skills. The router must make the selection transparent, state why each skill was selected, and preserve scientific and legal integrity.

The router should produce an integrated answer rather than a pile of disconnected checklists. It should also identify official-source-sensitive items and ask the author to verify live publisher pages before submission.

## Required inputs

Ask for missing information only when essential. If the user provides partial context, proceed with explicit assumptions.

- Target journal, publisher family, or candidate venues.
- Manuscript stage: outline, draft, first submission, revision, resubmission, final files, proof correction, or post-acceptance rights question.
- Task type: draft, rewrite, polish, audit, review simulation, reviewer response, cover letter, declarations, copyright/license, or submission package.
- Manuscript component names: abstract, related work, method, table, figure, caption, experiment, baseline, ablation, statistics, conclusion, references, supplementary material, or data/code statement.
- Existing text, tables, figures, reviewer comments, official form fields, author decisions, or journal links when available.
- Whether the output should be a route plan only or a route plan plus drafted/revised manuscript content.

## Style profile

- Preferred style: precise, auditable, conservative on policy, and explicit about assumptions.
- Typical router risk: choosing too many skills, choosing the wrong publisher family, hiding official-source uncertainty, or treating writing heuristics as current policy.
- Official source hierarchy: publisher-wide author instructions, target journal guide, editorial policy, template instructions, submission portal, author agreement, copyright/license pages, and the user's supplied official links. If official instructions differ from repository guidance, official instructions win.
- Avoid unsupported hype, fake citations, fabricated rules, fake acceptance-rate claims, invented editor policies, invented agreement terms, or invented permissions.

## Recommended manuscript map

Title; Authors and metadata; Abstract; Keywords or Index Terms; Introduction; Related Work; Method; Algorithms; Equations; Experiments; Results; Tables; Figures; Captions; Discussion; Limitations; Conclusion; References; Supplementary Material; Declarations; Cover Letter; Response Letter; Final Files; Proof Corrections.

This router does not edit every component by itself. It selects the right combination of skills so that detailed work is delegated to the appropriate component or journal skill.


## Component-layer routing behavior

Use this router when the user names one or more manuscript components. It should combine adjacent skills when the components are coupled.

Common component routes include: title → `elsevier-title-author-metadata`, abstract → `elsevier-abstract-keywords`, keywords → `elsevier-keywords`, introduction → `elsevier-introduction`, related-work → `elsevier-related-work`, contribution-positioning → `elsevier-contribution-positioning`, problem-formulation → `elsevier-problem-formulation`, method → `elsevier-method-experiment`, algorithm → `elsevier-algorithm-pseudocode`, equation → `elsevier-equation`, theory-proof → `elsevier-theory-proof`, experiment → `elsevier-method-experiment`, dataset-protocol → `elsevier-dataset-protocol`, baseline-selection → `elsevier-baseline-selection`.

Figures, tables, and captions should often be routed together because captions must match visual content and manuscript claims. Related work, contribution positioning, and citation integrity should also often be routed together because novelty framing depends on prior-work representation.


## Writing principles

1. Keep the router lightweight: select skills first, then load only the files needed for the current task.
2. Prefer explicit routing over implicit guessing when the journal or component is ambiguous.
3. Preserve publisher-family boundaries. Do not apply Elsevier Highlights rules to an IEEE-only submission unless the user asks for cross-publisher comparison.
4. Treat official policy, author agreement, copyright/license, open access, and submission portal requirements as live verification targets.
5. Separate scientific evidence work from formatting work and from rights/policy work.
6. Route figures, tables, and captions together when consistency matters.
7. Route related work, citations, contribution positioning, and novelty claims together when reviewer-risk is about originality.
8. Route response letters with revision diff, manuscript location, and reviewer-risk register skills.
9. Never invent citations, experiments, permissions, declarations, author roles, funding, data access, licenses, or editor decisions.
10. Return assumptions and unresolved items instead of pretending the route is certain.

## Workflow

1. **Task diagnosis**: identify publisher family, target journal, manuscript stage, requested components, policy-sensitive items, and desired output type.
2. **Journal routing**: if a journal is named or implied, map aliases to an independent journal adapter. If ambiguous, state the ambiguity and route conservatively.
3. **Component routing**: map manuscript components to component skills. Combine coupled components such as figure/table/caption or related-work/citation/contribution.
4. **Submission routing**: map cover letter, response, author agreement, copyright/license, open access, AI disclosure, declarations, final files, and proofs to submission skills.
5. **Official-source audit**: identify which selected route items require live official-source verification.
6. **Skill chain minimization**: remove redundant skills and keep the smallest sufficient chain.
7. **Integrated action plan**: explain the route in plain language and sequence the work.
8. **Deliverable generation**: draft, rewrite, audit, or checklist the requested content using the selected skill chain.
9. **Risk register**: list reviewer, editor, policy, and formatting risks ranked by severity.
10. **Author verification list**: state what the author must confirm before submission.

## Output contract

Return the following unless the user asks for a narrower output:

- Detected publisher family, target journal, manuscript stage, and task type.
- Selected skill chain with one-line justification for each selected skill.
- Official-source constraints and live pages/categories to verify.
- Integrated action plan ordered by manuscript or submission workflow.
- Drafted/revised/audited content when enough input is available.
- Missing inputs, evidence gaps, policy uncertainties, and assumptions.
- Reviewer-risk list ranked by severity.
- Next-step checklist suitable for the author or corresponding author.

## Reviewer-risk matrix

| Risk area | What to inspect | Safer response |
|---|---|---|
| Wrong journal route | Does the request mention a journal, acronym, or publisher family? | Map aliases and state ambiguity before applying a journal adapter. |
| Wrong component route | Does the task require table, figure, caption, related work, method, experiment, or submission work? | Select the smallest sufficient component chain. |
| Official-source drift | Could the rule have changed on the live website or submission portal? | Mark as official-source verification rather than a fixed rule. |
| Context overload | Is the router trying to load every skill? | Use registry-based routing and load only relevant skills. |
| Fabrication | Does the task invite invented citations, experiments, policies, permissions, or declarations? | Refuse fabrication and provide placeholders or verification checklists. |
| Manuscript inconsistency | Do abstract claims, tables, figures, captions, and conclusions disagree? | Route to claim-evidence, table, figure, caption, and results skills. |
| Revision inconsistency | Are reviewer responses not tied to manuscript changes? | Route to response, revision-diff, and risk-register skills. |
| Rights/policy confusion | Are copyright, license, OA, or author agreement terms uncertain? | Route to author-agreement and official-source audit skills. |

## Quality gates

Before finalizing, verify:

- The selected skills exist in the repository registry.
- The route does not confuse IEEE, Elsevier, ACM, Springer, Nature, Science, or Cell conventions.
- Journal adapters are independent and not treated as aliases of generic writing skills.
- Component skills remain reusable and are not hidden only inside the suite router.
- Policy-sensitive output is framed as an author verification item unless confirmed by official sources.
- The output does not fabricate citations, experiments, statistics, author declarations, rights, permissions, or editorial decisions.
- The route can be reproduced from `resources/skill_registry.json`, `resources/journal_registry.json`, `resources/component_registry.json`, and `resources/routing_rules.json`.

## Refusal and correction behavior

If the user asks the router to fabricate experiments, citations, peer reviews, editor decisions, author agreements, copyright ownership, license choices, permission letters, ethics approvals, data access, funding, conflicts of interest, author contributions, or AI-use disclosures, refuse that part and offer a compliant route: evidence collection, official-source verification, a placeholder statement, a permission-request template, or a transparent author checklist.
