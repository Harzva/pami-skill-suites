#!/usr/bin/env python3
"""Create a new skill skeleton."""
from pathlib import Path
import argparse
import textwrap

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip() if (ROOT / "VERSION").exists() else "0.0.0"

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text).lstrip(), encoding="utf-8")

p = argparse.ArgumentParser()
p.add_argument("name")
p.add_argument("--family", default=ROOT.name.split("-")[0])
p.add_argument("--kind", default="journal-adapter")
p.add_argument("--short", default=None)
p.add_argument("--scope", default="academic manuscript workflow")
args = p.parse_args()

name = args.name.lower()
short = args.short or name
skill_dir = ROOT / "skills" / name
if skill_dir.exists():
    raise SystemExit(f"Skill already exists: {skill_dir}")

write(skill_dir / "SKILL.md", f"""
---
name: {name}
description: "{short}: {args.scope}."
family: {args.family}
version: {VERSION}
kind: {args.kind}
status: experimental-unofficial
---

# {short} Skill

## When to use this skill

Use this skill for {args.scope}. This is unofficial and must be checked against current official author instructions.

## Core objective

Help draft, revise, audit, and respond to manuscript materials while preserving the user's actual scientific claims.

## Required inputs

- Target journal.
- Research problem and contribution.
- Method summary.
- Experiments and evidence.
- Existing draft or reviewer comments.

## Style profile

- Technical, evidence-driven, reviewer-facing.
- Avoid fabricated citations, results, policies, or declarations.

## Recommended manuscript map

Abstract; Introduction; Related Work; Method; Experiments; Discussion; Limitations; Conclusion.

## Writing principles

1. Make claims traceable to evidence.
2. Separate facts from assumptions.
3. Verify official instructions before submission.

## Workflow

1. Diagnose fit.
2. Map contribution.
3. Audit evidence.
4. Rewrite structure.
5. Reduce reviewer risks.
6. Return final checklist.

## Output contract

Return revised text, diagnosis, claim-evidence map, risks, missing materials, and checklist.

## Reviewer-risk matrix

| Risk | Check | Fix |
|---|---|---|
| Novelty | Is the gap clear? | Clarify delta. |
| Evidence | Are claims supported? | Add data/citations or soften. |

## Quality gates

- No fabricated evidence.
- Official instructions marked for verification.
- Limitations included.

## Refusal and correction behavior

Refuse fabrication and offer placeholders or experiment plans.
""")
write(skill_dir / "README.md", f"# {short}\n\nSkill `{name}` for {args.scope}.\n")
for rel in ["references/journal-profile.md", "references/writing-patterns.md", "references/reviewer-risk-map.md", "checklists/submission-checklist.md", "checklists/quality-gate.md", "checklists/evidence-checklist.md", "examples/example-prompts.md", "examples/example-output-skeleton.md"]:
    write(skill_dir / rel, f"# {rel}\n\nTODO: customize for `{name}`.\n")
print(f"Created {skill_dir}")
