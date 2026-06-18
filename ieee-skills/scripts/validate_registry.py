#!/usr/bin/env python3
"""Validate registries against skills/ folders."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "resources"
SKILLS = ROOT / "skills"
errors = []

def err(x): errors.append(x)

def load(name):
    p = RES / name
    if not p.exists():
        err(f"missing {name}"); return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        err(f"cannot parse {name}: {exc}"); return {}

skill_registry = load("skill_registry.json")
journal_registry = load("journal_registry.json")
component_registry = load("component_registry.json")
submission_registry = load("submission_registry.json")
routing_rules = load("routing_rules.json")

folder_names = {p.name for p in SKILLS.iterdir() if p.is_dir() and not p.name.startswith("_")}
registry_names = {s.get("name") for s in skill_registry.get("skills", [])}
if folder_names - registry_names:
    err("skills missing from registry: " + ", ".join(sorted(folder_names - registry_names)))
if registry_names - folder_names:
    err("registry has stale skills: " + ", ".join(sorted(registry_names - folder_names)))

for s in skill_registry.get("skills", []):
    name = s.get("name")
    if name not in folder_names:
        continue
    for rel in ["SKILL.md", "README.md", "references/journal-profile.md", "checklists/quality-gate.md"]:
        if not (SKILLS / name / rel).exists():
            err(f"{name}: missing {rel}")

for j in journal_registry.get("journal_adapters", []):
    skill = j.get("skill")
    if skill not in folder_names:
        err(f"journal adapter not found: {skill}")
    for rel in ["references/official-links.md", "references/author-agreement-notes.md"]:
        if not (SKILLS / skill / rel).exists():
            err(f"{skill}: missing {rel}")

for group_name, group, key in [("component", component_registry.get("components", []), "skill"), ("submission", submission_registry.get("submission_tasks", []), "skill")]:
    for item in group:
        skill = item.get(key)
        if skill and skill not in folder_names:
            err(f"{group_name} references missing skill: {skill}")

for router in routing_rules.get("default_chain", []):
    if router not in folder_names:
        err(f"routing default_chain references missing router: {router}")

if errors:
    print("Registry validation failed:\n")
    for e in errors: print("-", e)
    sys.exit(1)
print("Registry validation passed.")
