#!/usr/bin/env python3
"""Build a compact one-skill distribution from the full flat skill-suite.

The compact suite is intentionally a single skill directory. Internal modules are
Markdown references, not nested SKILL.md files, so host systems do not confuse them
with independently installed skills.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAMILY = ROOT.name.split("-")[0]
SUITE_NAME = f"{FAMILY}-skill-suite"
DIST = ROOT / "dist" / "compact-suite" / SUITE_NAME
FULL = ROOT / "dist" / "full-suite"


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)
    (FULL).mkdir(parents=True, exist_ok=True)

    skill_registry = json.loads((ROOT / "resources" / "skill_registry.json").read_text(encoding="utf-8"))
    journal_registry = json.loads((ROOT / "resources" / "journal_registry.json").read_text(encoding="utf-8"))
    component_registry = json.loads((ROOT / "resources" / "component_registry.json").read_text(encoding="utf-8"))
    submission_registry = json.loads((ROOT / "resources" / "submission_registry.json").read_text(encoding="utf-8"))
    routing_rules = json.loads((ROOT / "resources" / "routing_rules.json").read_text(encoding="utf-8"))

    write(DIST / "SKILL.md", f"""---
name: {SUITE_NAME}
description: "Compact {FAMILY.upper()} skill-suite router: route journal, component, submission, table, figure, caption, related-work, response, author-agreement, and official-source tasks from one installable skill."
family: {FAMILY}
version: {skill_registry.get('version', '0.0.0')}
kind: compact-router
status: experimental-unofficial
---

# Compact {FAMILY.upper()} Skill Suite

This is the one-skill distribution of `{ROOT.name}`. It is designed for users who want one installable skill that manages many internal modules.

## How it works

- The public skill is this `SKILL.md` file.
- Internal modules live under `references/journals/`, `references/components/`, and `references/submission/`.
- Internal modules are Markdown references, not nested `SKILL.md` files.
- Use `scripts/route_skill.py` to produce deterministic route plans.

## Routing workflow

1. Detect target journal or publisher family.
2. Detect manuscript components.
3. Detect submission-policy tasks.
4. Read only relevant internal modules.
5. Return a selected chain, official-source checks, and integrated output.

## Output contract

Return detected journal, selected internal modules, official-source checks, assumptions, revised/audited content, and reviewer-risk checklist.

## Safety

Never fabricate citations, experiments, author agreements, license choices, permissions, declarations, funding, ethics approvals, or editor decisions. Use author-fillable placeholders and official-source verification checklists instead.
""")
    write(DIST / "README.md", f"""# {SUITE_NAME}

Compact one-skill distribution generated from `{ROOT.name}`.

Install this folder when you want one router skill instead of many independent skills.
""")
    write(DIST / "references" / "registry.json", json.dumps({
        "skill_registry": skill_registry,
        "journal_registry": journal_registry,
        "component_registry": component_registry,
        "submission_registry": submission_registry,
        "routing_rules": routing_rules,
    }, indent=2, ensure_ascii=False) + "\n")
    write(DIST / "references" / "routing-policy.md", "# Routing policy\n\n" + "\n".join(f"- {x}" for x in routing_rules.get("selection_policy", [])) + "\n")
    write(DIST / "references" / "official-source-policy.md", "# Official-source policy\n\nPublisher and journal instructions are the source of truth. Treat repository rules as workflow guidance and verify live pages before submission.\n")
    for j in journal_registry.get("journal_adapters", []):
        write(DIST / "references" / "journals" / f"{j['skill']}.md", f"# {j['skill']}\n\nAliases: {', '.join(j.get('aliases', []))}\n\nSource skill: `skills/{j['skill']}`\n\nOfficial links file: `{j.get('official_links_file')}`\n")
    for c in component_registry.get("components", []):
        write(DIST / "references" / "components" / f"{c['component']}.md", f"# {c['component']}\n\nRoute to: `{c['skill']}`\n\nAliases: {', '.join(c.get('aliases', []))}\n\nCoupled components: {', '.join(c.get('coupled_components', []))}\n")
    for s in submission_registry.get("submission_tasks", []):
        write(DIST / "references" / "submission" / f"{s['task']}.md", f"# {s['task']}\n\nRoute to: `{s['skill']}`\n\nAliases: {', '.join(s.get('aliases', []))}\n\nRequires official verification: {s.get('requires_official_verification')}\n")
    (DIST / "scripts").mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "scripts" / "route_skill.py", DIST / "scripts" / "route_skill.py")

    write(FULL / "README.md", f"""# Full-suite distribution

The full suite is the repository-native layout: install independent skills directly from `skills/`.

Recommended for power users:

```bash
cp -r skills/{FAMILY}-skill-suite ~/.claude/skills/
cp -r skills/{FAMILY}-component-router ~/.claude/skills/
cp -r skills/{FAMILY}-table ~/.claude/skills/
```

Use compact-suite when you want one router skill only.
""")
    write(FULL / "manifest.json", json.dumps(skill_registry, indent=2, ensure_ascii=False) + "\n")
    print(f"Built compact suite at {DIST}")

if __name__ == "__main__":
    main()
