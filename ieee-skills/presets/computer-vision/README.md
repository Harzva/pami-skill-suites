# Computer Vision Preset Router

This preset is an optional discipline-specific routing profile for **IEEE Skills**. It is not a top-level skill and is not loaded by default.

## Context policy

```text
Presets are routing profiles, prompt packs, and evaluation profiles. They do not add top-level skills and must not increase default skill-listing context.
```

Use this preset when the user wants a discipline-fluent workflow, for example `Computer Vision` manuscript planning, journal fit routing, related-work audit, table/figure/caption upgrade, reviewer response, paper-mining structure extraction, or source-compliance check.

## Included journals

| Journal ID | Title | Maturity | Source-quality band |
|---|---|---:|---:|
| `pami` | TPAMI / PAMI | L4 | A |
| `tip` | IEEE TIP | L4 | A |
| `tcsvt` | IEEE TCSVT | L3 | A |
| `tvcg` | IEEE TVCG | L3 | A |

## Files

```text
README.md
preset.yaml
prompt-pack.md
routing-profile.yaml
eval-profile.yaml
```

## Safe use

- Route through `ieee-skill-suite` and its internal fragments.
- Keep this preset outside default `skills/` unless a maintainer intentionally creates a separate opt-in distribution.
- Verify mutable publisher and journal rules live before real submission.
- Use template papers only for structural observations, not for copying content.


## v1.5.0 Scenario Gallery

Includes `scenarios/`, `sample-outputs/`, `route-traces/`, and `evaluation-report.md`. These are optional preset resources and are not default top-level skills.
