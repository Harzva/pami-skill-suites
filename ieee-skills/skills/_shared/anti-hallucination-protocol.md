# Anti-hallucination Protocol

Use this protocol for every IEEE skill.

## Never fabricate

- Citations, DOIs, page numbers, reviewer identities, editor names, acceptance rates, impact factors, experiments, metrics, datasets, or ethical approvals.

## Use placeholders when evidence is missing

Examples:

```text
[Add citation for transformer-based segmentation baseline]
[Report mean ± standard deviation over N seeds]
[Verify target journal's current reference style]
```

## Separate facts from suggestions

Label outputs as:

- `Known from user input`
- `Inferred from context`
- `Suggested addition`
- `Requires verification`

## Claim-evidence rule

Every strong claim must point to at least one of:

- User-provided result.
- Verified source.
- Explicitly labeled hypothesis.
- Planned experiment.
