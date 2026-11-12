# TYPES — kinds of thing the notes name, read "X is a <type>". Constrained open, like EDGES.md: the dreamer types each
# thing with one of these or an alias; a thing of any other type keeps the dreamer's word, shown as other/<word>; a word
# becomes a type only over the bar, through the review, within the budget; a (proposed <date>) type still under the bar
# after the probation goes back to a word. `family:` groups types for the viewer and the shape check (C12); `drop:`
# names words that are never things (grep finds files and numbers), `drop-names:` names that are never things whatever
# their type (`*` stands for anything; a base about code deletes what it wants kept). Edit freely: a hand-written line
# is permanent (0 model calls); `pack: research, ops` adds a domain's types. The seed covers data, analytics, software
# and finance.
promote: 5 uses, 5 notes, 2 areas
budget: 40
probation: 60 days
- person: a named individual | aka: people, user, analyst, engineer, manager, owner | family: party | not: a team or a company
- team: a named team or group of people | aka: group, squad, crew | family: party
- organisation: a company, client, vendor, regulator or other body | aka: organization, company, vendor, client, regulator, firm | family: party
- term: a defined word, concept or method | aka: concept, method, definition, technique | not: a measured quantity (metric)
- metric: a measured quantity used to judge something | aka: kpi, measure, statistic, score | not: a single value or threshold
- tool: software or a platform used to do the work | aka: library, platform, framework, package, software | family: system | not: a service the team runs (service)
- document: a report, deck, specification, policy document or paper named as a thing | aka: report, deck, spec, paper, memo, template
- dataset: a table, file, feed or extract of records | aka: table, data set, feed, extract, view, source | not: one column of it (feature), one subset of it (segment)
- segment: a defined subset of records, customers or accounts | aka: cohort, population, subset, tier | family: dataset
- feature: an input variable or set of variables | aka: column, variable, field, feature set, attribute | not: the table it comes from (dataset)
- model: a trained or rule-based model, scorecard, forecast or one version of it | aka: scorecard, classifier, forecast model, algorithm
- pipeline: a job, pipeline or scheduled process that moves or transforms data | aka: job, dag, workflow, etl, process | family: system
- dashboard: a dashboard or report page people read regularly | aka: report page, bi report | family: document
- service: a running service, API or application | aka: api, app, application, endpoint, system | family: system
- module: a code module, package, repository or component | aka: repo, repository, component, class, function, script | family: system
- environment: a cluster, host, environment or deployment target | aka: cluster, host, prod, staging, region | family: system
- release: a named version or release of software | aka: version, build, tag | family: system
- instrument: a security, loan, contract or product that is traded, held or sold | aka: security, bond, loan, product, contract, derivative
- portfolio: a portfolio, book, fund or set of holdings | aka: book, fund, holdings
- account: a customer, ledger or trading account | aka: ledger, wallet
- counterparty: a client, issuer, borrower or counterparty in a transaction | aka: issuer, borrower, lender, obligor | family: party
- policy: a policy, limit, regulation or control that constrains the work | aka: regulation, limit, control, standard, mandate | family: rule
- scenario: a stress, forecast or planning scenario | aka: stress test, case, what-if
- desk: a trading desk, business unit or department | aka: business unit, department, division, unit | family: party
- flag: a feature flag, configuration setting or option | aka: feature flag, setting, config, option | family: system
- test: a test suite, test case or benchmark named as a thing | aka: suite, test case, benchmark | family: system
- issue: a ticket, issue or pull request named as a thing | aka: ticket, pr, pull request, bug report, merge request | family: document
- experiment (proposed 2026-11-12): a named analysis, study or A/B test run and identified by an id such as exp-404; differs from finding (the conclusion drawn) and model (the artifact trained) | family: experiment
- finding (proposed 2026-11-12): a named conclusion or claim drawn from analysis, not the file that holds it; differs from document (the written report) | family: document
- decision (proposed 2026-11-12): a recorded choice about what to do, agreed by named people; differs from policy (a standing rule that constrains work) | family: decision
- project (proposed 2026-11-12): a named piece of work or initiative that runs over time; differs from pipeline (a single job that moves data) | family: project
- question (proposed 2026-11-12): an open question a note raises for later answer; differs from finding (answered) | aka: open-question | family: question
- channel (proposed 2026-11-12): a route for reaching customers such as SMS, email or push; differs from campaign (a planned send over that route) | family: channel
- proposal (proposed 2026-11-12): a suggested option put forward for choice and not yet decided; differs from decision (agreed) | family: proposal
- review (proposed 2026-11-12): a formal assessment of a model, project or decision; differs from document (the written report that results) | family: review
- cutoff (proposed 2026-11-12): a score threshold used to accept, decline or flag accounts; differs from metric (a measured quantity) and flag (a configuration setting) | family: cutoff
- campaign (proposed 2026-11-12): a planned outreach wave sent to customers; differs from project (general work) and channel (the medium used) | family: campaign
drop: number, date, file, notebook, note, line, page, link
drop-names: *.py, *.sql, *.ipynb, *.csv, *.parquet, *.json, *.md, *notebook*, nb-*, *-script
