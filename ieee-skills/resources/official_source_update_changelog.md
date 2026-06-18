# Official Source Update Changelog

## v1.6.0 - 2026-06-13

- Added live source check matrix generation.
- Added source aging policy reports.
- Added release health dashboard reports.
- Added source verification badge data.
- Added scheduled source refresh workflow.
- No offline release build record is marked as live healthy unless a live check has actually been run.

## Maintenance note

Run `python scripts/check_official_links_live.py --live` before using mutable publisher or journal source records for real submission advice.
