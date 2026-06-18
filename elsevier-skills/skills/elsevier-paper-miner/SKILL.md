---
name: elsevier-paper-miner
description: "Mine the lawful template-paper corpus for section structure, figure/table/caption patterns, and reviewer-risk lessons without copying protected text."
family: elsevier
version: 1.2.0
kind: macro
status: experimental-unofficial
---

# Elsevier Paper Miner

## Purpose

Mine the local `paper_templates/` corpus for manuscript architecture. This skill studies **structure, section flow, evidence organization, table/figure/caption logic, and reviewer-risk patterns**. It must not copy text, figures, tables, captions, equations, benchmark interpretations, or paper-specific claims.

## Corpus sources

- Corpus manifest: `paper_templates/corpus_manifest.yaml` and `paper_templates/corpus_manifest.json`
- Paper cards: `paper_templates/cards/`
- Extracted structure maps: `paper_templates/extracted_structure_maps/`
- Thematic mining notes: `paper_templates/mining_notes/`
- Open-access papers bundled in this release: 6
- Official template/manual PDFs bundled in this release: 1

## When to use

Use this skill when the user asks for:

- a template-paper based section skeleton;
- abstract / introduction / related work / method / experiment patterns;
- table, figure, or caption style mining;
- reviewer-risk lessons derived from lawful open-access examples;
- journal-specific examples without copying source content.

## Required operating rules

1. Use only corpus entries with allowed source/license metadata.
2. Prefer `paper_templates/cards/<paper-id>.md` before opening the PDF.
3. Use `extracted_structure_maps/` for section sequencing and visual-evidence patterns.
4. Use `mining_notes/` for cross-paper style summaries.
5. Never copy source text, captions, figures, tables, equations, or paper-specific claims.
6. If the user wants submission/legal guidance, route to `elsevier-skill-suite` and official-source fragments instead of relying on template papers.
7. For real submission, live-check publisher and target-journal instructions.

## Workflow

1. Detect target publisher, journal, article type, and manuscript component.
2. Select the smallest relevant corpus subset.
3. Read the Paper Card first; use the PDF only to confirm structural observations.
4. Extract a neutral skeleton or checklist.
5. Rewrite using the user's own evidence, terminology, and experimental results.
6. Return a copyright-safe output with a source-use warning.

## Output contract

Return:

- selected corpus entries;
- source/license status;
- structural observations;
- reusable section skeleton;
- table/figure/caption lessons if relevant;
- reviewer-risk checklist;
- forbidden-copying warning;
- items requiring live official-source verification.


## v1.2.0 evaluation benchmark awareness

When demonstrating this skill, prefer the benchmark tasks in `evals/tasks/` and sample-output contracts in `evals/sample_outputs/`. For paper-mining tasks, always include a copyright-safe warning and use template papers only for structure and pattern extraction.


## Extracted visual assets

Use `paper_templates/extracted_visual_assets/` when the user wants to analyze main figures, motivation/framework diagrams, or table design patterns. These assets are for structure analysis only and must not be copied into manuscripts. Always include the copyright-safe warning and point to `visual_asset_manifest.json` when citing the corpus internally.
