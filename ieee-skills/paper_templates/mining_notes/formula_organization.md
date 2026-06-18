# Formula Organization

Publisher family: IEEE

Make mathematical notation serve the method narrative instead of becoming opaque decoration.

## Fixed routines

### Define-before-use

**Sequence:** symbol table → problem setting → objective → constraints → optimization/algorithm link

**Reviewer risk:** Undefined symbols break reviewer trust.

### Equation-to-algorithm bridge

**Sequence:** mathematical objective → closed-form/intuitive reading → algorithmic step → complexity/implementation note

**Reviewer risk:** Equations that do not map to implementation feel ornamental.

### Assumption-lemma-consequence

**Sequence:** assumption → formal statement → proof sketch or citation → practical consequence

**Reviewer risk:** Theoretical claims without assumptions invite rejection.

### Notation consistency audit

**Sequence:** dimensions → indices → sets → random variables → loss terms → hyperparameters

**Reviewer risk:** Notation drift causes method ambiguity.

## Output contract

- notation table
- equation purpose map
- implementation bridge
- ambiguity list

## Safety note
These routines are structural best-practice patterns, not official publisher rules and not text to copy from template papers.
