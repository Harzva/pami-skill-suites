# Product parity report against nature-skills-style repositories

This repository intentionally follows the product pattern visible in `nature-skills`: installable skill folders, shared support materials, router-style decomposition, and task-specific skills.

Reference product:

- https://github.com/Yuan1z0825/nature-skills
- https://github.com/Yuan1z0825/nature-skills/blob/main/install.md

## Parity checklist

| Product feature | Implemented here | Notes |
|---|---|---|
| Complete `skills/<name>/` units | Yes | Each skill has `SKILL.md`, README, references, checklists, and examples. |
| Shared support content | Yes | `skills/_shared/` stores source policies, evidence maps, reviewer-risk taxonomies, product philosophy, and template-paper policy. |
| Router/meta skills | Yes | `ieee-journal-router`, `ieee-official-source-audit`, and `ieee-template-paper-miner`. |
| Core workflows | Yes | Writing, polishing, reviewer simulation, response, cover letter, citation, figures/tables, reproducibility, revision strategy. |
| Journal adapters | Yes | High-value adapters for the target publisher family. |
| Official-source design notes | Yes | `docs/official-source-map.md`, `resources/official_sources.json`. |
| Template-paper corpus | Yes | `paper_templates/open_access_papers/` with license notes and analysis sheets. |
| Validation tooling | Yes | Manifest builder, structure validator, quality scorer, CI workflow. |
| Anti-fabrication behavior | Yes | Required in every `SKILL.md`. |

## Remaining differences

This repository does not claim to be official and does not include paid/copyright-unclear papers. That is a deliberate product-quality decision.
