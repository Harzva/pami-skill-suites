---
module: signal-processing
source_skill: signal-processing-writing
version: 0.8.0
status: context-safe-fragment
---

# Signal Processing Journal Module

> This is an internal fragment used by the skill-suite router. It is not a default top-level skill.

## Journal identity

- Full name: Signal Processing
- Common abbreviation: Signal Processing
- Publisher: Elsevier
- Field: signal processing theory, methods, algorithms, applications
- Typical manuscript type: research article, review/survey, revision, response-letter, or submission-package audit depending on the user request.

## Official URLs

- journal: Signal Processing
- short: Signal Processing
- publisher: Elsevier
- issn: 0165-1684
- homepage: https://www.sciencedirect.com/journal/signal-processing
- elsevier_journal_page: https://www.elsevier.com/journals/signal-processing/0165-1684
- guide_for_authors: https://www.sciencedirect.com/journal/signal-processing/publish/guide-for-authors
- submit_article: https://www.sciencedirect.com/journal/signal-processing/publish/guide-for-authors#submit-your-article
- scope: signal processing theory, methods, algorithms, applications
- latex_instructions: https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions
- copyright_policy: https://www.elsevier.com/about/policies-and-standards/copyright
- open_access_licenses: https://www.elsevier.com/about/policies-and-standards/open-access-licenses
- gen_ai_policy_journals: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- author_hub: https://www.elsevier.com/researcher/author
- policies_guidelines: https://www.elsevier.com/researcher/author/policies-and-guidelines
- highlights: https://www.elsevier.com/researcher/author/tools-and-resources/highlights
- graphical_abstract: https://www.elsevier.com/researcher/author/tools-and-resources/graphical-abstract
- open_access_choice: https://www.elsevier.com/researcher/author/open-access/choice
- permissions: https://www.elsevier.com/about/policies-and-standards/copyright/permissions
- editorial_manager_help: https://www.elsevier.support/publishing/answer/how-do-i-submit-a-manuscript-in-editorial-manager

## Writing style

- Preferred style: technical, complete, application-aware, reviewer-friendly, evidence-driven.
- Typical reviewer risk: black-box ML without signal rationale, missing complexity/robustness.
- Avoid unsupported hype, fabricated citations, fabricated experiments, fake acceptance rates, fake reviewer identities, invented policy claims, and stronger-than-evidence conclusions.

## Core objective

Produce submission-ready academic assistance for **Signal Processing** while preserving the user's actual scientific claims and separating evidence from speculation.

The skill should improve structure, language, claim discipline, experimental completeness, reviewer-risk awareness, and package readiness without fabricating results, citations, editorial rules, or author declarations.

## Routing hints

Use this journal module when the user mentions any of:

- signal processing skill
- signal-processing
- signal-processing-writing

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

This fragment was generated from `signal-processing-writing` during the v0.8.0 compact architecture migration. The original independent skill remains available under `skills-advanced/`.

## Official Source Compliance Matrix

| Required area | URL or status | Source tier | Verification status |
|---|---|---|---|
| Journal homepage | https://www.sciencedirect.com/journal/signal-processing | journal official rule | Live verification required before submission |
| Author instructions / Guide for Authors | https://www.sciencedirect.com/journal/signal-processing/publish/guide-for-authors | journal official rule | Live verification required before submission |
| Submission system | https://www.sciencedirect.com/journal/signal-processing/publish/guide-for-authors#submit-your-article | publisher official rule | Live verification required before submission |
| Manuscript template | https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions | publisher official rule | Live verification required before submission |
| Publishing agreement | https://www.elsevier.com/about/policies-and-standards/copyright | publisher official rule | Live verification required before submission |
| Copyright / license | https://www.elsevier.com/about/policies-and-standards/copyright | publisher official rule | Live verification required before submission |
| Open access | https://www.elsevier.com/researcher/author/open-access/choice | publisher official rule | Live verification required before submission |
| Ethics / integrity | https://www.elsevier.com/about/policies-and-standards/publishing-ethics | publisher official rule | Live verification required before submission |
| AI disclosure policy | https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals | publisher official rule | Live verification required before submission |
| Data / code availability | https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-guidelines | publisher official rule | Live verification required before submission |
| Permissions | https://www.elsevier.com/about/policies-and-standards/copyright/permissions | publisher official rule | Live verification required before submission |
| Last verified date | 2026-06-11 | repository audit metadata | Release audit date |
| Verification status | Official-source fields populated for v0.8.0; mutable journal rules still require live verification before real submission. | repository audit metadata | Needs live verification |

## Rule provenance classification

- Publisher official rule: publisher-wide author-center, template, publishing agreement, copyright/license, open access, ethics, AI disclosure, data/code, permissions, and production guidance from Elsevier official sources.
- Journal official rule: journal homepage, scope page, Guide for Authors / Information for Authors, society page, IEEE Xplore or ScienceDirect page, and submission-system instructions for **Signal Processing**.
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

- Expansion pack membership: signal-processing
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
