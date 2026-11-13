# SETUP — what this memory is for, and how it is kept

for: the past work of a card-analytics team, about forty projects (fraud, collections, churn, credit lines,
marketing uplift and the platform under them) and the house rules they share. People ask what a model was built
on, what replaced what, which decisions rest on a dataset, and what is current.

a note here: one thing per file: a question, an experiment, a finding, a decision, a dataset, a feature, a model
version. Four lines is usual. The `# ` line is the claim. These notes carry no `from:` or `supersedes:` line: a note
says in its closing sentence what it builds on and what it replaces, by the other note's id or in a few words.

areas: the notes of every project are in one folder, `work/`, about 1,200 of them, with no folder a project: a
note's own name and words say which project it belongs to. `prefs/`, `reporting/`, `glossary/`, `corrections/`,
`howto/`, `qa/` span the projects; `log/` holds daily scratch lines.

who writes: the analysts and their agents, as they work. Nobody rewrites a note; a newer note replaces an older one.

who keeps: Haiku 5.5 through `claude -p --model haiku` with no tools, `dream --packets -j 6`, a dozen notes a call;
the second reading, the curator and the review run in the same dream. `work/` is too large to list in a prompt, so
a keeper is shown the notes near the ones it reads. Read once on 2026-11-12; a changed note is read again.

vocabulary: `KINDS.md` is the seed with the `inc` prefix taken off the incident line (it is this bank's code for the
income-estimation project). `TYPES.md` and `EDGES.md` are the seeds. No tags.

## proof
- what replaced aml-xgb-v2? -> work/aml-xgb-v3.md
- which dataset holds the analyst outcomes of the aml alerts? -> work/ds-aml-dispositions.md
- what is the current fraud model of 2026 built on? -> work/fraud26-gbm-v3.md
- what is the KYC risk band feature? -> work/feat-aml-kyc-band.md
- why does the suppression cut stay at 0.18? -> work/dec-aml-suppress-018.md
