# Product design philosophy

`elsevier-skills` is designed to be comparable to a polished academic skill product, not a loose prompt list.

## Product goal

Help researchers draft, revise, audit, and respond to reviews for Elsevier journal-family manuscripts while keeping every claim traceable to user-provided evidence, official instructions, or clearly labeled structural examples.

## Why the repository is structured this way

1. **Reusable skill units**: each skill is a full folder because reliable agents need references, checklists, examples, and output contracts around `SKILL.md`. This follows the design pattern documented by the `nature-skills` installation guide: a skill folder is the reusable unit, and `skills/_shared/` supports router-style skills.
2. **Core skills + journal adapters**: core skills encode common workflows; adapters specialize tone, risks, and manuscript maps for high-value journals.
3. **Official-source map**: high-stakes submission details change. The repo records what official materials were used and which workflow decisions came from them.
4. **Template-paper corpus**: published open-access papers provide real structural examples, but only for architecture and presentation patterns.
5. **Quality gates**: every skill includes anti-fabrication behavior, reviewer-risk matrices, and source-verification reminders.

## Source hierarchy

1. Current target-journal Guide for Authors / Information for Authors.
2. Official Elsevier author-center, policy, template, and style pages.
3. Official template/class documentation.
4. Repository shared policies and checklists.
5. Bundled open-access paper templates used only for structure.

## Why official sources are not embedded as rigid rules

Some details such as article categories, page limits, charges, review model, required declarations, source file names, and portal behavior can change. Therefore, skills phrase these as verification gates. This makes the repository safer and easier to maintain.
