# Product philosophy

`ieee-skills` is built as a product-style skill repository, not a single prompt collection.

## Design commitments

1. **Whole-folder reusable skills**: every skill contains `SKILL.md`, references, checklists, and examples. This mirrors the reusable skill-unit design used by `nature-skills`, whose install guide emphasizes copying the entire skill folder rather than only `SKILL.md`.
2. **Source hierarchy**: official publisher and target-journal instructions outrank repository conventions and example papers.
3. **Evidence discipline**: the system must not invent experiments, references, reviewer identities, declarations, or compliance statements.
4. **Template-paper corpus**: bundled open-access/CC-BY papers are used to learn structure and section choreography, not to copy text.
5. **Router-first workflow**: meta-skills route requests to precise core skills or journal adapters so the agent loads only the relevant guidance.

## Why this exists

IEEE Transactions/Journals-style manuscripts require different outputs and reviewer-risk controls. A high-quality skill repo should encode those differences into checklists, output contracts, and official-source verification steps rather than relying on memory or generic academic-writing prompts.
