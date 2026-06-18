# Elsevier Journal Skill-Suite Architecture

This repository is a **skill-suite**, not a single prompt. It has two layers:

1. **Core component skills**: reusable manuscript parts such as title, abstract, related work, tables, figures, captions, experiments, response letters, copyright/license checks, and final files.
2. **Independent journal adapter skills**: target-journal skills such as `pami-writing`, `tip-writing`, `pr-writing`, or `eswa-writing`. Each adapter has its own folder, profile, official links, author-agreement notes, reviewer-risk map, checklists, and examples.

A journal adapter should route to component skills rather than duplicating all logic. Example:

```text
pami-writing -> ieee-related-work + ieee-method-details + ieee-experimental-design + ieee-figure + ieee-table + ieee-caption + ieee-author-agreement
```

This makes the suite maintainable and closer to a product repository: users can install only the adapters or components they need, and maintainers can update publisher-wide policy skills without rewriting every journal adapter.
