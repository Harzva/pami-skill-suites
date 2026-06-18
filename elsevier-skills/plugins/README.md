# Plugin Packaging — Elsevier Skills v1.2.0

This directory contains plugin metadata templates for installing Elsevier Skills as an agent skill package.

Generated plugin bundles are created by:

```bash
python scripts/build_distribution.py
```

Output artifacts:

```text
dist/plugin-default.zip
dist/plugin-compact.zip
```

## Modes

- `default`: default macro skills, recommended for most users.
- `compact`: one `elsevier-skill-suite` router skill, recommended for the smallest listing.

These plugin packages preserve the same context-safe architecture as the repository itself. Advanced skills remain opt-in and are not default-visible.


Expansion packs remain opt-in and are not default-visible.
