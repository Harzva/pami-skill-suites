# Elsevier Skill-Suite Architecture

Yes: this suite contains many **independent journal skills** plus many reusable **component skills**.

## Independent journal skills

Each journal adapter is a standalone installable skill folder. It contains `SKILL.md`, README, references, checklists, examples, official links, and author-agreement notes.

## Component skills

Component skills cover manuscript details that should not be buried inside generic writing skills: tables, figures, captions, related work, datasets, baselines, metrics, statistics, code/data availability, author agreements, copyright, open access, response letters, and final files.

## Routing model

A journal adapter should route work to component skills. This makes the repository maintainable and comparable to a polished skill product rather than a loose prompt collection.
