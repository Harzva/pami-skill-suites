---
name: elsevier-figure-table
description: "Audit and improve Elsevier figures, tables, captions, result reporting, and visual consistency using compact component fragments."
family: elsevier
version: 1.2.0
kind: macro
status: experimental-unofficial
---

# Elsevier Figure Table

## Purpose

This is a default macro skill for the Elsevier context-safe journal skill-suite. It keeps the default skill listing small while routing detailed journal, component, and submission needs through `elsevier-skill-suite/manifest.yaml` and internal static fragments.

## When to use

Use this skill for figures, tables, captions, visual accessibility, result reporting, and consistency checks. If the request mentions a specific journal, manuscript component, or submission/legal item, pair this macro skill with `elsevier-skill-suite` routing rather than loading every advanced skill.

## Context-safe operating rule

- Do not expose every advanced skill by default.
- Prefer suite static fragments for journal/component/submission details.
- Use `skills-advanced/` only when the user explicitly wants an independent skill or repository development work.
- Treat official publisher and journal pages as the highest authority.

## Workflow

1. Identify the target journal or publisher family.
2. Identify task type: writing, review, response, figure/table/caption, citation, submission, or paper-template mining.
3. Ask the suite manifest for the smallest relevant module set.
4. Produce the requested artifact with claim-evidence discipline and official-source warnings where needed.

## Output contract

Return a concise routing diagnosis, selected modules, revised/generated content or checklist, reviewer-risk notes, and items requiring live official-source verification.
