# Candidate Evidence Card: elsevier-candidate-slot-038

## Metadata

- **Paper ID**: elsevier-oa-candidate-038
- **Publisher family**: Elsevier
- **Proposed title**: TBD — pending Elsevier OA paper selection #038
- **Proposed journal**: Medical Image Analysis
- **Year**: TBD
- **Target figure type**: method_pipeline_figure
- **Source status**: pending-evidence-collection
- **Evidence completeness score**: 8
- **Extraction gate**: blocked_until_doi_oa_license_permission_evidence_complete

## Doi Evidence

- **Proposed Doi**: TBD — collect from official publisher page or DOI registry during OA review
- **Doi Status**: pending-doi-discovery
- **Evidence Status**: missing-or-TBD
- **Required Actions**:
- query Crossref or DOI registry
- confirm title/year/journal match
- record canonical DOI URL
- **Notes**: DOI evidence alone is not enough for OA figure extraction.
## Publisher Page Evidence

- **Proposed Source Url**: TBD — must be official OA publisher page, author page, or institutional repository
- **Source Type**: pending_oa_source_collection
- **Evidence Status**: missing-or-TBD
- **Required Actions**:
- open official publisher article page
- capture license/copyright statement
- record official PDF availability if any
- **Notes**: Do not use Sci-Hub, pirated PDFs, or paywalled-only PDFs.
## Repository Oa Evidence

- **Candidate Repository Url**: TBD or not applicable
- **Evidence Status**: needs-manual-review
- **Required Actions**:
- check author or institutional repository version
- record rights statement and version type
- confirm repository copy is legally hosted
- **Notes**: Repository OA evidence may differ from publisher license evidence.
## License Evidence

- **License Candidate**: TBD — must be CC BY / CC BY-NC / publisher-permitted OA / author repository OA
- **Evidence Status**: missing-or-TBD
- **Accepted License Examples**:
- CC BY
- CC BY-NC
- publisher-permitted OA
- author/institutional repository OA with permitted analysis use
- **Required Actions**:
- record exact license text
- record attribution requirements
- record no-derivatives / non-commercial limitations when present
- **Notes**: A license candidate is not a final permission decision.
## Permission Evidence

- **Permission Risk**: high
- **Permission Status**: requires-human-review
- **Required Actions**:
- confirm figure extraction is allowed for analysis/gallery/RAG metadata
- decide whether images can be hosted or only referenced
- record attribution format
- **Notes**: Public gallery display and RAG storage may have stricter requirements than private structural analysis.
## Third Party Material Evidence

- **Status**: unknown-until-visual-and-caption-review
- **Required Actions**:
- check caption and article for third-party material notices
- flag figures containing reused photos/logos/maps/screenshots/datasets
- exclude or seek permissions if third-party status is unclear
- **Notes**: Third-party elements can invalidate apparent article-level reuse permission.
## Manual Reviewer Notes

- **Reviewer**: TBD
- **Last Reviewed**: not-reviewed-in-offline-release-build
- **Decision**: do-not-extract-new-assets-yet
- **Notes**: Offline scaffold only. Live DOI/OA/license verification is required before any new extraction or public hosting.

## Copyright Safety Note

This evidence card is for source review and structural-analysis workflow planning only. Do not extract, host, copy, redraw, publish, or reuse any figure, caption, label, layout, or paper-specific claim until DOI, OA source, license, permission, and third-party-material evidence are complete and manually approved.

## Prohibited Sources

- Sci-Hub
- pirated PDF
- paywalled-only PDF
- copyright-unknown PDF
- unauthorized image reuse

---

## v2.4.0 Promotion State

- Promotion gate: `blocked_until_connector_evidence_and_human_review_pass`
- Human review required: yes
- New figure extraction allowed: no
- Metadata-only RAG allowed: no
- Safety note: v2.4.0 adds promotion workflow metadata only; it does not certify live DOI/OA/license evidence.
