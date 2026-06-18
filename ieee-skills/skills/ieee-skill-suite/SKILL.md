---
name: ieee-skill-suite
description: "Context-safe IEEE journal manuscript skill-suite with routing for writing, review, response, figure/table, citation, submission, official-source checks, and paper-template mining."
family: ieee
version: 1.2.0
kind: macro-router
status: experimental-unofficial
---

# IEEE Skill Suite Router

## Purpose

This is the default router for the IEEE journal skill-suite. It manages journal modules, manuscript component modules, and submission/legal modules without exposing every detailed skill in the default skill listing.

## Context-safe architecture

Use progressive disclosure:

1. Load this suite skill first.
2. Read `manifest.yaml` to detect journal, component, and task aliases.
3. Load only the internal fragments needed for the user request from `static/journals/`, `static/components/`, and `static/submission/`.
4. Use `skills-advanced/` only for optional independent skill installation or development.

## Routing dimensions

- Journal adapters: target-journal modules under `static/journals/`.
- Component modules: abstract, introduction, related work, method, experiments, tables, figures, captions, equations, limitations, conclusion, references, and appendices under `static/components/`.
- Submission modules: cover letter, response letter, author agreement, copyright/license, open access, declarations, data/code availability, and final files under `static/submission/`.

## Official-source policy

For author agreements, copyright, license options, open access, fees, page limits, submission portals, AI disclosure, ethics, data/code policy, and final-file rules, always mark `Live verification required before submission` unless the user provides current official instructions.

## Output contract

Always return:

1. Detected task and target journal.
2. Selected minimal modules.
3. Official-source constraints and live-check items.
4. Manuscript-level action plan or generated content.
5. Reviewer-risk list and next edits.


## v1.2.0 evaluation benchmark awareness

When demonstrating this skill, prefer the benchmark tasks in `evals/tasks/` and sample-output contracts in `evals/sample_outputs/`. For paper-mining tasks, always include a copyright-safe warning and use template papers only for structure and pattern extraction.
