# Template Paper Corpus

This directory provides the lawful, source-recorded template-paper corpus for `ieee-skills`.

## v0.8.0 structure

```text
paper_templates/
├── corpus_manifest.yaml
├── corpus_manifest.json
├── cards/
├── extracted_structure_maps/
├── mining_notes/
├── open_access_papers/
└── official_templates/
```

## Corpus size

- Open-access research papers: 5
- Official template/manual PDFs: 2

## Principle

Use these papers like architecture references: study structure, not wording.

Allowed mining targets:

- section sequencing;
- abstract/introduction/related-work/method/experiment patterns;
- table, figure, and caption logic;
- reviewer-risk patterns;
- claim-to-evidence organization.

Forbidden uses:

- copying text, captions, equations, figures, tables, or layouts;
- copying paper-specific claims or benchmark interpretations;
- using template papers as legal advice or a substitute for official journal instructions.

## Workflow

1. Start with `corpus_manifest.yaml`.
2. Read the corresponding `cards/<paper-id>.md`.
3. Check `extracted_structure_maps/<paper-id>.md` for section sequencing.
4. Use `mining_notes/` for cross-paper patterns.
5. Rewrite from the user's own evidence.
6. Verify target-journal instructions before submission.


## Extracted visual assets (v1.8.0)

`paper_templates/extracted_visual_assets/` separates main figures, motivation/framework figures, and representative table crops from the lawful corpus for visual-structure analysis. These assets are not reusable manuscript assets unless the original license and attribution/permission requirements are re-checked.
