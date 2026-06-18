# Data Mining Prompt Pack

These prompts are reusable entry points for the optional `data-mining` preset. They should route through `ieee-skill-suite`, not through newly exposed top-level skills.

## 1. Full discipline routing

```text
Use `ieee-skill-suite` with the `data-mining` preset. Detect the target journal, select only the needed journal/component/submission fragments, and return: selected modules, official-source warnings, structured output contract, reviewer-risk checklist, and next actions.
```

## 2. Abstract and contribution upgrade

```text
Use the `data-mining` preset to revise this abstract for a target IEEE journal. Preserve factual claims, separate contribution from evidence, flag unsupported claims, and include live-verification warnings for mutable journal requirements.
```

## 3. Related work audit

```text
Use the `data-mining` preset to audit the related work. Diagnose taxonomy gaps, missing comparison axes, citation positioning risks, novelty overlap risks, and recommended paragraph-level restructuring.
```

## 4. Figure/table/caption package

```text
Use the `data-mining` preset to audit tables, figures, and captions. Check if each visual has a claim, evidence role, self-contained caption, accessible labeling, and reviewer-safe interpretation.
```

## 5. Reviewer response

```text
Use the `data-mining` preset to draft a reviewer-response matrix. Classify each comment, map changes to manuscript sections, avoid overclaiming, and flag when additional experiments or official-source verification are needed.
```

## 6. Paper-template mining

```text
Use the `data-mining` preset with the paper-miner skill. Extract structure patterns only. Do not copy text, figures, captions, tables, equations, or paper-specific claims.
```
