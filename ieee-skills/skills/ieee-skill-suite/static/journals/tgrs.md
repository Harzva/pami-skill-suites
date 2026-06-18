---
module: tgrs
source_skill: tgrs-writing
version: 0.8.0
status: context-safe-fragment
---

# IEEE TGRS Journal Module

> This is an internal fragment used by the skill-suite router. It is not a default top-level skill.

## Journal identity

- Full name: IEEE Transactions on Geoscience and Remote Sensing
- Common abbreviation: TGRS
- Publisher: IEEE Geoscience and Remote Sensing Society
- Field: remote sensing, geoscience, radar, hyperspectral imaging, earth observation
- Typical manuscript type: research article, review/survey, revision, response-letter, or submission-package audit depending on the user request.

## Official URLs

- journal: IEEE Transactions on Geoscience and Remote Sensing
- short: TGRS
- publisher: IEEE Geoscience and Remote Sensing Society
- homepage: https://www.grss-ieee.org/publications/transactions-on-geoscience-and-remote-sensing/
- xplore: https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=36
- author_instructions: https://www.grss-ieee.org/publications/transactions-on-geoscience-and-remote-sensing/
- scope: remote sensing, geoscience, radar, hyperspectral imaging, earth observation
- author_center: https://journals.ieeeauthorcenter.ieee.org/
- article_templates: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/authoring-tools-and-templates/tools-for-ieee-authors/ieee-article-templates/
- template_selector: https://template-selector.ieee.org/
- publishing_agreement: https://journals.ieeeauthorcenter.ieee.org/choose-a-publishing-agreement/
- open_access_rights: https://journals.ieeeauthorcenter.ieee.org/choose-a-publishing-agreement/open-access-rights-management/
- ai_guidelines: https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/
- structure_article: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-the-text-of-your-article/structure-your-article/
- submission_process: https://journals.ieeeauthorcenter.ieee.org/submit-your-article-for-peer-review/the-ieee-article-submission-process/
- submission_policies: https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/
- copyright_infringement: https://journals.ieeeauthorcenter.ieee.org/choose-a-publishing-agreement/avoid-infringement-upon-ieee-copyright/
- editorial_style_manual: https://journals.ieeeauthorcenter.ieee.org/your-role-in-article-production/ieee-editorial-style-manual/
- graphics_resolution: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/
- graphics_file_formatting: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/file-formatting/
- supplementary_materials: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/prepare-supplementary-materials/

## Writing style

- Preferred style: formal, precise, expert-reader, contribution-dense, technically rigorous.
- Typical reviewer risk: missing evidence, unclear fit, overclaiming, formatting assumptions.
- Avoid unsupported hype, fabricated citations, fabricated experiments, fake acceptance rates, fake reviewer identities, invented policy claims, and stronger-than-evidence conclusions.

## Core objective

Produce submission-ready academic assistance for **IEEE TGRS** while preserving the user's actual scientific claims and separating evidence from speculation.

The skill should improve structure, language, claim discipline, experimental completeness, reviewer-risk awareness, and package readiness without fabricating results, citations, editorial rules, or author declarations.

## Routing hints

Use this journal module when the user mentions any of:

- ieee tgrs skill
- ieee transactions on geoscience and remote sensing
- tgrs
- tgrs-writing

Pair with component modules: abstract, related-work, method, experiment, table, figure, caption, citation/references, limitations, response-letter, and submission modules.

## Output contract

Return the following unless the user requests a narrower output:

- Revised or drafted text.
- Structural diagnosis.
- Claim-evidence map.
- Venue-fit and reviewer-risk list.
- Missing experiments, baselines, citations, limitations, declarations, or formatting checks.
- Suggested figure/table/storyline changes.
- Final submission-readiness checklist.
- Explicit assumptions and items that require official source verification.

## Live verification required

Before real submission, verify the latest official pages for submission system, manuscript template, page limits, article types, supplementary files, publication fees or APCs, publishing agreement, copyright/license, open-access option, AI disclosure, data/code policy, and permissions.

## Source note

This fragment was generated from `tgrs-writing` during the v0.8.0 compact architecture migration. The original independent skill remains available under `skills-advanced/`.

## Official Source Compliance Matrix

| Required area | URL or status | Source tier | Verification status |
|---|---|---|---|
| Journal homepage | https://www.grss-ieee.org/publications/transactions-on-geoscience-and-remote-sensing/ | journal official rule | Live verification required before submission |
| Author instructions / Guide for Authors | https://www.grss-ieee.org/publications/transactions-on-geoscience-and-remote-sensing/ | journal official rule | Live verification required before submission |
| Submission system | https://journals.ieeeauthorcenter.ieee.org/submit-your-article-for-peer-review/the-ieee-article-submission-process/ | publisher official rule | Live verification required before submission |
| Manuscript template | https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/authoring-tools-and-templates/tools-for-ieee-authors/ieee-article-templates/ | publisher official rule | Live verification required before submission |
| Publishing agreement | https://journals.ieeeauthorcenter.ieee.org/choose-a-publishing-agreement/ | publisher official rule | Live verification required before submission |
| Copyright / license | https://journals.ieeeauthorcenter.ieee.org/choose-a-publishing-agreement/avoid-infringement-upon-ieee-copyright/ | publisher official rule | Live verification required before submission |
| Open access | https://journals.ieeeauthorcenter.ieee.org/choose-a-publishing-agreement/open-access-rights-management/ | publisher official rule | Live verification required before submission |
| Ethics / integrity | https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/ | publisher official rule | Live verification required before submission |
| AI disclosure policy | https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/ | publisher official rule | Live verification required before submission |
| Data / code availability | https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/research-reproducibility/ | publisher official rule | Live verification required before submission |
| Permissions | https://journals.ieeeauthorcenter.ieee.org/choose-a-publishing-agreement/avoid-infringement-upon-ieee-copyright/ | publisher official rule | Live verification required before submission |
| Last verified date | 2026-06-11 | repository audit metadata | Release audit date |
| Verification status | Official-source fields populated for v0.8.0; mutable journal rules still require live verification before real submission. | repository audit metadata | Needs live verification |

## Rule provenance classification

- Publisher official rule: publisher-wide author-center, template, publishing agreement, copyright/license, open access, ethics, AI disclosure, data/code, permissions, and production guidance from IEEE official sources.
- Journal official rule: journal homepage, scope page, Guide for Authors / Information for Authors, society page, IEEE Xplore or ScienceDirect page, and submission-system instructions for **IEEE TGRS**.
- Repository best-practice recommendation: writing structure, reviewer-risk framing, component routing, output contracts, and safety checks generated by this unofficial skill-suite.
- Template-paper observation: style observations from open-access template papers, when present, are used only for structural learning and never override official publisher or journal rules.

## Official-source usage policy

Use the URLs above as the starting source map. Do not treat cached repository text as final for legal, fee, license, page-limit, APC, template, AI disclosure, data/code, permission, or submission-system decisions. Before real submission, re-open the current official page and record the live verification date in the submission package.

<!-- SOURCE REFRESH METADATA START -->
## Source Refresh Metadata

- **last_live_checked**: `not-run-in-release-build`
- **source_status**: `pending-live-check`
- **needs_reverification**: `true`
- **official_link_health**: `unchecked in offline release build; run scripts/check_official_links_live.py --live before relying on mutable publication details.`
- **source_refresh_report**: `resources/source_refresh_report.json`
- **release_added**: `v1.2.0`

Live verification required before submission: submission systems, author instructions, templates, publishing agreements, copyright/license terms, open-access options, AI disclosure policies, data/code availability requirements, permissions, page limits, and supplementary-file requirements may change.
<!-- SOURCE REFRESH METADATA END -->

## Coverage expansion metadata

- Expansion pack membership: remote-sensing
- Coverage maturity level: L3 — source-refresh metadata + live-check support
- Dashboard source: `resources/journal_coverage_dashboard.json`
- Import policy: opt-in expansion packs must not increase default `skills/` visibility.
- Live verification required before real submission: yes



<!-- V1.6 SOURCE MAINTENANCE START -->
## v1.6 Source Maintenance

- **live_source_check_matrix**: `resources/live_source_check_matrix.json`
- **source_age_policy_report**: `resources/source_age_policy_report.json`
- **release_health_dashboard**: `resources/release_health_dashboard.json`
- **source_badges**: `resources/source_badges.json`
- **scheduled_workflow**: `.github/workflows/source-refresh.yml`
- **offline_safe_policy**: unchecked links must remain pending until `scripts/check_official_links_live.py --live` is run.

Mutable publication details require live verification before real submission advice.
<!-- V1.6 SOURCE MAINTENANCE END -->

<!-- V1.7 SOURCE TRUST START -->
## v1.7 Source Trust and Human Review

- **source_trust_tiers**: `resources/source_trust_tiers.json`
- **human_review_queue**: `resources/human_review_queue.json`
- **source_review_report**: `resources/source_review_report.json`
- **source_trust_policy**: publisher/journal/society official sources outrank repository recommendations; template-paper observations are structure-mining aids only; unverified candidates require human review.
- **human_review_status**: mutable publication details remain queued until live source checks are run and reviewed.

Do not use cached repository text as the final authority for submission systems, author instructions, copyright/license terms, open-access options, AI disclosure, data/code policies, permissions, fees, page limits, or supplementary-file rules.
<!-- V1.7 SOURCE TRUST END -->
