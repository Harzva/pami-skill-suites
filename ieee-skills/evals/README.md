# Evaluation, Examples, and Task Benchmarks

This directory defines the static benchmark suite for `ieee-skills` v1.2.0.

## Goals

- verify that the context-safe router selects relevant modules;
- check that official-source warnings are present when mutable publisher/journal rules are involved;
- check that paper-mining tasks remain copyright-safe;
- provide sample outputs that demonstrate structured output contracts;
- support release smoke tests before public packaging.

## Directory layout

```text
evals/
├── tasks/           # YAML benchmark tasks
├── rubrics/         # Human-readable scoring rubrics
├── sample_outputs/  # Golden-style sample outputs for static checks
└── README.md
```

## Run

```bash
python scripts/validate_evals.py
python scripts/run_evals.py
```

The evaluator is intentionally static: it verifies task structure, required sample-output sections, safety warnings, and routing metadata. It does not claim to grade real model quality.
