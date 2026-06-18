# Medical Ai Preset Evaluation Report

Release: v1.5.0

## Scope

This is a static preset-level release report. It checks that the preset has scenario files, sample outputs, route traces, and a clear output contract. It does not claim peer-review success or live official-source validity.

## Scenario matrix

| Scenario | Purpose | Component modules | Submission modules |
|---|---|---:|---:|
| `writing-related-work` | Writing / related-work scenario | 6 | 0 |
| `figure-table-caption` | Figure-table-caption scenario | 6 | 0 |
| `reviewer-response-submission` | Reviewer-response or submission-compliance scenario | 3 | 11 |

## Checklist

- [x] `scenarios/` exists.
- [x] `sample-outputs/` exists.
- [x] `route-traces/` exists.
- [x] Sample outputs include selected skills/modules.
- [x] Sample outputs include official-source warnings.
- [x] Sample outputs include copyright-safe paper-mining warnings.
- [x] Sample outputs include reviewer-risk checklists.
- [x] Sample outputs include structured output contracts.
- [x] Preset remains outside default `skills/`.
