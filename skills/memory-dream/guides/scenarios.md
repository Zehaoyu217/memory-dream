# Scenarios: starting the lists for a kind of work

Read this at step 4 of setting a memory up (SKILL.md), after you have looked at the material. Every scenario uses the
same rule (guides/vocabulary.md); what changes is where the lists start. Start small: a line you leave out is kept as
the keeper's word and offered once it is common, while a line you add needlessly is one more choice in every reading.

For each scenario: **folders** (areas), **lists** (what to add to the seeds), **tags** (themes worth a line from the
start, if any) and **prove** (the kind of question SETUP.md's five should ask).

## Analytics and data science (the seeds)
- folders: one per project or study; `prefs/` per stakeholder; `glossary/` for metrics defined once.
- lists: nothing to add. The seeded kinds (`exp- fnd- dec- q- ds- feat- model metric`), types (dataset, segment,
  feature, model, metric) and links (uses, trained-on, evaluated-on, measured-by, replaces) cover it.
- tags: none at first. Later a theme that runs across projects: a regulation, a data-quality issue, a programme.
- prove: what came of an experiment; which model is current and what it was trained on; what uses a table.

## Software
- folders: one per service or repository area; `howto/` for procedures; `corrections/` for mistakes not to repeat.
- lists: `pack: software` in EDGES.md (calls, implements, deployed-to, configures, tested-by, blocked-by). Kinds
  (component, design, bug, release) and types (service, module, environment, release, test, issue) are seeded.
- notes point into code with `path#symbol`, never a bare `path:line`; `ask` marks a note STALE when its symbol is gone.
- tags: cross-cutting concerns that no folder holds: security, performance, a migration in progress.
- prove: why a design was chosen; what calls a service; which bug a release fixed.

## Finance and risk
- folders: one per desk, model or portfolio; `reporting/` for the rules of recurring reports.
- lists: the seeds cover it: types (instrument, portfolio, account, counterparty, policy, scenario, desk), kinds
  (risk, incident, model, decision, requirement, report). Add a type only for what people look up by name.
- tags: the regulations and controls a note bears on. These cut across desks, so they are tags, not folders.
- prove: which limit or decision is current (two live decisions on one thing are compared: CONFLICTS.md); what a
  model was validated on; who owns a risk.

## Research and literature
- folders: one per question or line of work; a paper's note sits with the question it serves.
- lists: `pack: research` in KINDS.md (hypothesis `hyp-`, paper `paper-`), TYPES.md (paper, method) and EDGES.md
  (cites, extends, contradicts, reproduces).
- tags: methods or datasets shared across questions, when they are not things people look up by name.
- prove: what a paper claims and what contradicts it; which hypotheses are still open.

## Operations
- folders: one per system or service; `runbooks/` for procedures (the ops pack makes its notes runbooks).
- lists: `pack: ops` in KINDS.md (runbook `rb-`, change `chg-`), TYPES.md (monitor, queue) and EDGES.md (alerts-on,
  runs-after, escalates-to, rolled-back-to).
- tags: failure themes that recur across systems: capacity, a dependency, a vendor.
- prove: what to do when an alert fires; what changed before an incident; what a job runs after.

## A personal or assistant memory
- folders: `prefs/` (`prefs/me-<topic>.md`, `prefs/<first>-<last>-<topic>.md`), `corrections/`, `howto/`, and a folder
  per piece of work as it comes.
- lists: the seeds; no model is needed, since kinds come from folders and prefixes. Beside Claude Code's own memory,
  add `@memory/DIGEST.md` to CLAUDE.md.
- tags: none, unless the person tags their own notes.
- prove: how this person wants a chart, a report or a reply; the mistake not to make again.

## Someone else's base, taken in
- `memory.py absorb <folder> --as <name>` makes it an origin in `memory/<name>/`. Its own ALIASES.md speaks of its
  own things; a name both sides use is two things until you write one line: `- auc = <name>:auc`.
- lists: leave yours as they are. Its words are counted like any keeper's and offered when they are common.
- prove: one question it answers that your notes do not, asked with `-p <name>`.

## A large corpus (thousands of notes)
- cost first: `memory.py dream --dry-run --packets` says how many calls and about how much. Tell the user before
  spending. Then `dream --packets` on a cheap model, or helper agents (`memory-dreamer`) on the packets in parallel.
- lists: raise each bar with the size of the corpus (for example `promote: 10 uses, 10 notes, 3 areas`) so the review
  sees only what is common, and keep each budget small enough for a person to read the list in a minute.
- the curator reads up to 60 folders a dream; the rest wait for the next one. Only folders whose things changed are
  read again.
- tags: start with none and let the loop propose them; with many folders, `promote: 5 uses, 5 notes, 2 areas` in
  TAGS.md keeps tags to themes that cross folders.
- prove: five questions across folders, plus one that needs a set (`ask --list`), not a search.
