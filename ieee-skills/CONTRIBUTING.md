# Contributing to IEEE Skills

Thank you for helping improve this journal skill-suite.

## Contribution priorities

High-value contributions:

- Fix official-source links or verification metadata.
- Improve existing journal fragments with current official instructions.
- Add legally usable paper cards and structure maps.
- Improve benchmark tasks, rubrics, and sample outputs.
- Improve context-safety, validation scripts, or documentation.

Low-value contributions:

- Adding many new top-level skills.
- Copying paper text into examples.
- Hard-coding mutable fees, page limits, or policies.

## Architecture rule

Keep `skills/` compact. New detailed modules should usually go under:

```text
skills/ieee-skill-suite/static/journals/
skills/ieee-skill-suite/static/components/
skills/ieee-skill-suite/static/submission/
```

Add independent skills under `skills-advanced/` only when they are valuable as opt-in units.

## Official-source rule

Every journal or legal/submission contribution must classify claims as:

- publisher official rule
- journal official rule
- repository best-practice recommendation
- template-paper observation

Mutable details must include `Live verification required before submission`.

## Validation

Before opening a pull request, run:

```bash
python scripts/run_smoke_tests.py
python scripts/validate_plugins.py
python scripts/validate_distribution.py
```
