# Official Source Update Changelog

Version: v1.6.0

This changelog records maintenance changes to publisher and journal source metadata. It does not claim that live HTTP verification has been completed in the release build.

## 2026-06-13 — v1.6.0

- Added live source check matrix tooling.
- Added source aging policy reports.
- Added release health dashboard resources.
- Added source verification badge data.
- Added scheduled source-refresh workflow template.
- Release build mode: offline-safe dry-run.
- Live HTTP check performed: no.

Before real submission advice, run:

```bash
python scripts/live_source_check_matrix.py --live
python scripts/check_official_links_live.py --live
python scripts/source_age_policy.py
python scripts/release_health_dashboard.py
```
