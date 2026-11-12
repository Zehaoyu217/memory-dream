# KINDS — kinds of note. A note's kind is its frontmatter `type:`, else the kind whose prefix starts its filename
# (`exp-014` → experiment; `…-vN` is a model), else the kind of its area (`prefs/` → preference), else note. One line per
# kind: `- kind: definition | prefix: a, b | area: x, y | family: parent | role: R | digest: current | conflicts: yes
# | answers: yes | not: what it is not`. role ∈ question, evidence, state, rule, reference, log; project work is question,
# evidence and state. `answers: yes` kinds answer a question they are built on; `digest: current` kinds head the digest;
# `conflicts: yes` kinds are compared for disagreement (a child kind counts as its family). `general:` names the areas
# that span projects.
# Edit freely: a hand-written line is permanent (0 model calls); `pack: research, ops` adds a domain's kinds.
# The seed covers data, analytics, software and finance work.
general: prefs, reporting, glossary, corrections, howto, qa, people, log
- question: something asked and not yet settled | prefix: q | role: question
- experiment: a run with a method and a measured result | prefix: exp | family: finding | role: evidence
- finding: a result or observation that holds until superseded | prefix: fnd, find, finding | role: evidence | conflicts: yes | answers: yes | not: a single run (experiment)
# `inc-` is this bank's code for the income-estimation project (inc-gbm-v1), not a mark of incidents: the prefix was
# taken off the next line on 2026-11-11, when a note's name began to count before the dreamer's reading (RESULTS phase L).
- incident: a failure, outage, loss or error, and what was learned | family: finding | role: evidence
- decision: a choice made, with its reason | prefix: dec | role: state | digest: current | conflicts: yes | answers: yes
- plan: an intended course of action, with steps or dates | prefix: plan | role: state | digest: current
- requirement: a stated need or acceptance condition | prefix: req | role: state
- risk: a known exposure, its size and its owner | prefix: risk | role: state
- dataset: a table, file, feed or extract, and what it holds | prefix: ds | role: state
- feature: an input variable or feature set, and how it is built | prefix: feat | role: state
- model: a trained or rule-based model, scorecard or forecast, one version per note | prefix: model | role: state | digest: current | conflicts: yes
- metric: how something is measured | prefix: metric | family: term | role: state
- report: a recurring report, dashboard or deliverable, and its rules | prefix: rpt, report | role: reference
- component: a service, module, library or system and what it does, one per note | prefix: svc, mod, lib, sys | role: state
- design: an architecture or design decision, with the options weighed | prefix: adr, design | family: decision | role: state | digest: current | conflicts: yes | answers: yes
- bug: a defect observed, its cause and its fix | prefix: bug, fix | family: finding | role: evidence
- release: a shipped version or deployment, when and what changed | prefix: rel, release | role: state
- term: a defined word or concept | prefix: term | area: glossary | role: reference
- preference: how a named person wants things done | prefix: pref | area: prefs | family: rule | role: rule
- rule: a standing rule or procedure for the work | prefix: rule | area: reporting, howto | role: rule
- correction: a past mistake and the rule that prevents it | area: corrections | family: rule | role: rule
- log: a dated scratch line | area: log | role: log
- note: anything else | role: reference
