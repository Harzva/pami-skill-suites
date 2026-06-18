# Extracted Visual Assets

Generated for IEEE Skills v1.8.0.

This directory separates representative main figures, motivation/framework figures, and visually useful tables from the legal OA paper-template corpus for **analysis only**.

## Important copyright policy

- These images are extracted from open-access/template PDFs already included in `paper_templates/`.
- They are included to study structure, composition, caption logic, table organization, and visual communication patterns.
- Do not copy, republish, or reuse any figure/table content in a manuscript unless the original license and attribution/permission requirements allow it.
- For public reuse, re-check the source page and license.

## Folders

- `main_figures/` - first detected figure-like visual per paper.
- `motivation_figures/` - detected overview/framework/method/motivation visuals.
- `beautiful_tables/` - detected representative table crops.
- `contact_sheets/` - quick visual overview PNGs.
- `metadata/` - machine-readable asset metadata.

## Extraction method

The extraction is heuristic and caption-aware: the script searches figure/table captions and crops nearby page regions. It is intended for rapid analysis and may require manual refinement for exact figure boundaries.
