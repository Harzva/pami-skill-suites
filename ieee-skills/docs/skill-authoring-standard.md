# Skill Authoring Standard

## Required structure

Each skill folder must contain:

```text
SKILL.md
README.md
references/journal-profile.md
references/writing-patterns.md
references/reviewer-risk-map.md
checklists/submission-checklist.md
checklists/quality-gate.md
checklists/evidence-checklist.md
examples/example-prompts.md
examples/example-output-skeleton.md
```

## Required `SKILL.md` sections

- YAML front matter with `name`, `description`, `family`, `version`, `kind`, and `status`.
- When to use this skill.
- Core objective.
- Required inputs.
- Style profile.
- Recommended manuscript map.
- Writing principles.
- Workflow.
- Output contract.
- Reviewer-risk matrix.
- Quality gates.
- Refusal and correction behavior.

## Naming

- Use lowercase folder names.
- Use `family-topic` for core skills.
- Use `journal-acronym-writing` for journal adapters when the acronym is unambiguous.
- Avoid implying official publisher affiliation.
