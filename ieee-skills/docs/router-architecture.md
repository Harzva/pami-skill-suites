# Skill-Suite Router Architecture

Version: `0.5.0`

This repository uses a **flat-source, routed-suite** architecture.

## Design decision

The source-of-truth layout keeps every skill as an independently installable folder under `skills/`. The suite-level skill does not hide all other skills inside its folder. Instead, it reads registries and routes work to the right skills.

```text
skills/
├── ieee-skill-suite/
├── ieee-journal-router/
├── ieee-component-router/
├── ieee-submission-router/
├── <component-skill>/
└── <journal-adapter>/
```

## Why

Agent skill systems typically discover skills from `name`, `description`, and path first, then load full `SKILL.md` and references when needed. A flat layout lets the host discover each skill without paying the context cost of a single giant router prompt. The router still gives users a single entry point.

## Two release modes

### Full Suite Mode

Install multiple independent skills directly from `skills/`.

### Compact Suite Mode

Install one generated skill from `dist/compact-suite/ieee-skill-suite/`. Internal modules are Markdown references, not nested `SKILL.md` files.

## Route layers

1. Journal routing: target-journal adapter.
2. Component routing: manuscript parts such as table, figure, caption, related work, method, experiments, references, declarations.
3. Submission routing: cover letter, response letter, author agreement, copyright/license, open access, proofs, final files.

## Source files

- `resources/skill_registry.json`
- `resources/journal_registry.json`
- `resources/component_registry.json`
- `resources/submission_registry.json`
- `resources/routing_rules.json`
