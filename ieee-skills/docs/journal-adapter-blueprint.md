# Journal Adapter Blueprint

Use this blueprint when adding a new IEEE journal skill.

## Required research before adding an adapter

1. Confirm the journal belongs to the intended publisher/society.
2. Capture the official journal page and Guide for Authors or author instructions.
3. Identify article types, scope, required submission assets, and recurring reviewer expectations.
4. Avoid hardcoding rules that change frequently.

## Adapter content model

- Scope and audience.
- Methodological expectations.
- Experimental expectations.
- Common rejection reasons.
- Submission-package reminders.
- Official-source verification tasks.

## Minimum pull request checklist

- [ ] New folder under `skills/`.
- [ ] `SKILL.md` passes `scripts/validate_structure.py`.
- [ ] All companion files present.
- [ ] `skill_manifest.json` updated by `scripts/build_manifest.py`.
- [ ] No false official affiliation language.
