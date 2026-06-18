# Final Validation Report - v2.7.0

Repository: `ieee-skills`
Publisher family: IEEE
Generated on: 2026-06-18
Release name: RAG Trace UI + Visual Query Debugger

## Summary

v2.7.0 is the current validated release for the IEEE skill suite. The release preserves the compact default skill layer and keeps advanced skills, expansion packs, presets, and main-figure assets opt-in.

## Release gates

- `make all`: passed
- `python3 scripts/build_manifest.py`: passed
- `python3 scripts/validate_structure.py`: passed
- `python3 scripts/quality_score.py`: passed
- `python3 scripts/validate_manifest.py`: passed
- `python3 scripts/build_distribution.py`: passed
- `python3 scripts/validate_distribution.py`: passed, `42` dist zip files generated
- `python3 scripts/validate_release_health.py`: passed
- `python3 scripts/run_smoke_tests.py`: passed

## Context safety

- Default macro skills: `8`
- `skills-advanced/`: optional, not default-visible
- `expansion_packs/`: optional, not default-visible
- `presets/`: optional, not default-visible
- `main_figure_site/`: optional, not default-visible

## Main-figure and RAG safety

- Metadata-only seed RAG remains allowed.
- Image embedding remains blocked.
- Public-gallery reuse remains blocked.
- New figure extraction remains blocked until DOI/OA/license evidence, permission evidence, third-party-material review, and human approval pass.

## Notes

This validation is an offline-safe release gate. It does not certify live DOI/OA/license status, official URL freshness, publisher policy changes, or permission to reuse source-paper visuals.
