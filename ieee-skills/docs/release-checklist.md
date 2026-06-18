# Release Checklist

Before publishing a release:

- [ ] Run `python scripts/validate_structure.py`.
- [ ] Run `python scripts/build_manifest.py`.
- [ ] Run `python scripts/quality_score.py`.
- [ ] Check `VERSION`, `CHANGELOG.md`, and `README.md`.
- [ ] Confirm unofficial disclaimer appears in README and skill files.
- [ ] Confirm official-source verification policy appears in shared docs.
- [ ] Zip the repository from its parent directory.
