---
name: ieee-template-paper-miner
description: "IEEE Template Paper Miner: using the bundled CC-BY/open-access IEEE template corpus to extract structural patterns without copying scientific content."
family: ieee
version: 0.5.0
kind: core
status: experimental-unofficial
---

# IEEE Template Paper Miner Skill

## When to use this skill

Use this skill when the user needs using the bundled CC-BY/open-access IEEE template corpus to extract structural patterns without copying scientific content. It is designed for product-grade routing, source-grounded auditing, or template-corpus mining inside the `ieee-skills` repository rather than one-off prose polishing.

Use it for rough research ideas, Chinese drafts, manuscript sections, LaTeX source audits, experiment tables, reviewer comments, response letters, cover letters, or submission-readiness checks. It is especially useful when the user asks which skill to use, why a rule exists, which official materials support a workflow, or how to learn structural patterns from the bundled open-access template papers.

This is an unofficial skill. It must never claim affiliation with IEEE. It must treat IEEE Author Center, IEEE Template Selector, IEEE Editorial Style Manual, target publication instructions, and IEEE publication policies as the source of truth and must explicitly mark any current submission rule that needs verification.

## Core objective

Mine IEEE open-access template papers for section morphology, evidence layout, figure/table function, and reviewer-risk lessons while preventing content copying or policy overgeneralization.

The skill should help the agent behave like a reliable academic-product workflow: it should select the right sub-skill, load the smallest useful support context, separate official rules from learned article patterns, preserve the user's real evidence, and prevent fabricated citations, fabricated experiments, fabricated reviewer identities, fabricated policy claims, or inappropriate reuse of copyrighted material.

## Required inputs

Ask for missing information only when it is essential. If enough context exists, proceed with transparent assumptions.

- Target publisher, target journal, and article type if known.
- Current manuscript stage: idea, outline, abstract, full draft, pre-submission audit, revision, or response letter.
- Research area, contribution type, datasets, baselines, metrics, equations, figures, tables, and available results.
- Whether the user wants routing, source explanation, writing/rewrite output, official-source audit, or template-paper structural mining.
- Any known constraints: double-anonymous review, conference extension, page limits, data availability, ethics approval, clinical/security/human-subjects risks, or AI-assisted writing disclosure.
- Existing draft, LaTeX package, response matrix, reviewer comments, cover letter, figures, tables, or source package if available.
- Desired output assets: revised text, skill routing plan, source map, claim-evidence map, risk register, Index Terms, figure/table references, equations, reproducibility/artifact statements, and IEEE-style response matrices.

## Style profile

- Preferred style: formal IEEE Transactions style: precise, technical, evidence-first, numbered-structure aware, cautious about prior publication and template assumptions.
- Reasoning stance: source-grounded, conservative, reversible, and evidence-traceable.
- Template use: use open-access papers for section morphology and reviewer expectations only; do not copy paper-specific wording, figures, datasets, or claims.
- Official-source stance: do not hard-code unstable rules such as page charges, APCs, exact submission limits, review model, or portal behavior unless the current official target-journal page has been checked.
- Safety stance: refusal is required for fabrication, ghost compliance, invented approvals, invented citations, or undisclosed copying.

## Recommended manuscript map

Template paper; structural outline; claim-evidence map; method/experiment skeleton; figures/tables; limitations; response or revision plan.

For routing tasks, map the user's request into this manuscript map and then choose the narrowest matching skill. For template-paper mining tasks, extract only high-level patterns such as section order, contribution placement, evidence layout, figure/table function, and reviewer-risk coverage.

## Writing principles

1. Start from the user's evidence, not from generic prestige-journal language.
2. Separate three layers: official rules, repository workflow conventions, and open-access template-paper patterns.
3. Prefer minimal loaded context: use the router to choose a specific core skill or journal adapter instead of loading every skill.
4. Make every strong claim traceable to data, citation, method description, theorem, ablation, or explicitly labeled hypothesis.
5. Treat IEEE Author Center, IEEE Template Selector, IEEE Editorial Style Manual, target publication instructions, and IEEE publication policies as verification targets, not decorative references.
6. When using bundled papers, mine structure and presentation choices only; never reuse article text as reusable prose.
7. Return unresolved risks directly rather than hiding them behind polished language.
8. Keep bilingual Chinese-to-English assistance faithful to the scientific content.
9. Preserve author responsibility for declarations, ethics, AI use, data rights, and conflicts of interest.
10. Generate product-style outputs that can be checked by humans and maintained by future contributors.

## Workflow

1. **Intent classification**: decide whether the user needs routing, drafting, polishing, reviewer simulation, response planning, official-source audit, template-paper mining, or submission-package checking.
2. **Venue and article-type identification**: identify target journal family, article type, and stage; if unknown, propose a conservative shortlist and mark assumptions.
3. **Source hierarchy check**: distinguish official publisher/journal guidance from learned examples and repository conventions.
4. **Skill selection**: route to the narrowest useful skill, then list which shared files and templates are relevant.
5. **Claim-evidence extraction**: build a compact map of claims, evidence, missing citations, missing experiments, and unsupported implications.
6. **Template-corpus comparison**: when useful, compare the manuscript against bundled CC-BY/open-access papers for structure, not content imitation.
7. **Reviewer-risk triage**: rank risks by desk rejection, novelty, evidence, reproducibility, ethics, formatting, and response strategy.
8. **Official-source audit**: produce a checklist of official pages or target-journal instructions that must be verified before submission.
9. **Output assembly**: produce the requested text, routing plan, source map, risk register, checklist, or revision package.
10. **Integrity pass**: remove fabricated rules, fake citations, overclaiming, hidden AI-use assumptions, and any language that implies unverified compliance.

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

## Reviewer-risk matrix

| Risk area | What to inspect | Safer response |
|---|---|---|
| Venue fit | Is the target journal/publisher correctly identified? | Route to the correct family and mark uncertain venue assumptions. |
| Official rules | Are current instructions verified, or guessed from memory? | Provide an official-source checklist and avoid hard-coded unstable rules. |
| Novelty | Is the contribution delta clear relative to prior work and conference versions? | State the exact delta and request citations or experiments. |
| Evidence | Does every major claim have data, proof, citation, or labeled hypothesis status? | Add claim-evidence mapping and soften unsupported statements. |
| Template use | Is the user copying content from example papers? | Convert examples into structural lessons only. |
| Reproducibility | Can methods, datasets, settings, and evaluation be reconstructed? | Add implementation/configuration/artifact checklist items. |
| Ethics | Are authorship, AI use, data rights, human/animal/clinical/security issues handled honestly? | Use placeholders and verification prompts, never invented compliance. |
| Revision | Are reviewer concerns answered with evidence and manuscript changes? | Build a response matrix with comment IDs, actions, evidence, and residual risk. |

## Quality gates

Before finalizing, verify:

- The selected skill matches the user's actual venue, stage, and output request.
- Official-source claims are tied to IEEE Author Center, IEEE Template Selector, IEEE Editorial Style Manual, target publication instructions, and IEEE publication policies or are marked for verification.
- Template-paper outputs describe structure, not copied language.
- No fabricated citations, results, metrics, reviewer identities, journal policies, acceptance claims, or compliance declarations are introduced.
- Claims, abstract, introduction, method, experiments, limitations, figures, tables, and response materials tell one consistent contribution story.
- Missing data, missing baselines, missing ethics statements, missing AI disclosures, or missing declarations are reported as risks, not silently invented.
- The final answer is useful even if the user cannot immediately provide more details.

## Refusal and correction behavior

If the user asks to fabricate experiments, citations, peer-review outcomes, editor decisions, ethics approvals, AI-use declarations, author contributions, data-access rights, or conflicts of interest, refuse that part clearly and offer a compliant alternative: a placeholder, evidence plan, experiment checklist, official-source verification list, or transparent uncertainty note.

If the user asks to copy or paraphrase substantial text from a bundled paper, refuse the copying request and provide a structural template instead. If the target journal instructions are unknown or may have changed, do not guess; provide a verification checklist and proceed with conservative, clearly labeled assumptions.
