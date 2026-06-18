# Computer Vision Expansion Pack

This opt-in expansion pack groups IEEE journal coverage for the **computer vision** area.

## Context-safety rule

This pack does **not** expose additional default skills. It is consumed through the suite router, imported as fragments, or installed as an advanced optional pack.

## Files

- `journals.yaml` — journal entries, coverage maturity levels, and opt-in routing hints.
- `fragment_import_manifest.yaml` — safe import instructions for maintainers.
- `source_quality_report.json` — source-quality and maturity summary.

## Maturity levels

| Level | Meaning |
|---|---|
| L0 | listed only |
| L1 | official homepage + author instructions |
| L2 | full official source matrix |
| L3 | source-refresh metadata + live-check support |
| L4 | paper-template card + evaluation task |

## Maintenance policy

Before promoting a journal into core suite coverage, verify official sources, update source-health metadata, add paper-template cards when lawful, and add at least one benchmark task when the journal reaches L4.


## v1.3.0 Hardening

This pack now includes source-quality scoring, a staged L0→L3 promotion workflow, a pack-specific evaluation task placeholder, and a paper-card TODO list.

Files added:

- `source_quality_report.md`
- `eval_tasks/computer-vision_coverage_task.yaml`
- `paper_card_todo.md`
- `promotion_queue.md`

Context-safety rule: importing a journal candidate from this pack must not create a new default top-level skill. Use suite/static fragments or optional advanced skills only.
