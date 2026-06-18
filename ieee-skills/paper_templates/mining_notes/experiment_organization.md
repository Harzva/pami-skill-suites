# Experiment Organization

Publisher family: IEEE

Convert experimental evidence into a reviewer-legible chain from protocol to result to interpretation.

## Fixed routines

### Setup-first protocol

**Sequence:** task/dataset → baselines → metrics → implementation details → fairness controls → result table → interpretation

**Reviewer risk:** Missing implementation details makes gains look non-reproducible.

### Claim-evidence alignment

**Sequence:** claim → primary metric → supporting table/figure → statistical/ablation support → failure case

**Reviewer risk:** Overclaiming if a claim is not backed by an explicit result.

### Ablation staircase

**Sequence:** base model → add component A → add component B → full model → sensitivity/failure analysis

**Reviewer risk:** Ablation without rationale reads like parameter fishing.

### Fair comparison block

**Sequence:** same split → same metric → same training budget → same input resolution/feature → same test protocol

**Reviewer risk:** Reviewers will attack unfair or under-specified baselines.

## Output contract

- experiment map
- claim-evidence table
- missing baseline list
- reviewer-risk checklist

## Safety note
These routines are structural best-practice patterns, not official publisher rules and not text to copy from template papers.
