# The real index of the bank, as readings

`notes/`: 1,677 extraction files, the dreamer's (Claude Haiku) raw reading of each note of the 1,677-note bank, keyed by
the note's content hash, exactly as `memory.py dream` wrote them on 2026-11-02 ($2.69 for 1,687 calls, $0.0016 per call,
58% of input tokens from cache; four review calls, $0.03). `EDGES.md`, `TYPES.md`, `ALIASES.md`, `CONFLICTS.md`,
`KINDS.md`: the registries after the review (6 relation types and 8 thing types on probation, 87 alias lines, 81
conflict verdicts). `restore.py` copies them into an assembled bank so the graph is rebuilt with no model, which makes
every "with the index" number in README and RESULTS reproducible from the repository (`tests/retrieval_gate.py bank-index`).
