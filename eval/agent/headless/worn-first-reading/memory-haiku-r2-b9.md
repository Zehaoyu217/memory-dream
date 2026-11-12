## Q1
clv-bgnbd-v1 rests on two dataset notes: ds-clv-cohort-panel (2.4M accounts from cards.accounts_monthly) and ds-clv-revenue-monthly (monthly revenue per account). It reaches them through feat-clv-arpu-v1, feat-clv-tenure and ds-clv-revenue-monthly.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3, which promotes ed-gbm-v3 to the watchlist, and dec-ed-gbm-for-watchlist, which it supersedes. Both reach it through ed-gbm-v3, exp-207, find-ed-bureau-slope or feat-ed-bureau-slope-v1.
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
The note in force at the end of the sfc-ets-v1 line is sfc-hier-v3 (sfc-ets-v1 was replaced by sfc-lgbm-v2, which was replaced by sfc-hier-v3). sfc-hier-v3 is built on exp-207, fnd-sfc-q4-reconciled, feat-sfc-active-accounts and sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/sfc-lgbm-v2.md

## Q4
disp-lgbm-v1 rests on two dataset notes: ds-disp-analyst-labels (8,900 hand labels, 7,450 with two-analyst agreement) and ds-disp-disputes (cards.disputes, 41,870 disputes). It reaches them through dec-disp-labels-two-analyst and q-disp-label-source.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-timezone-utc, which it directly informs through exp-102 and the parity results, and dec-fsm-cutover, which it reaches through the parity experiments and findings.
Notes: feature-store-migration/dec-fsm-timezone-utc.md, feature-store-migration/dec-fsm-cutover.md

## Q6
The note in force at the end of the txc-logreg-v1 line is txc-gbm-v3 (txc-logreg-v1 was replaced by txc-gbm-v2, which was replaced by txc-gbm-v3). txc-gbm-v3 is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
The recorded links show ed-gbm-v2 resting on one dataset, ds-ed-current-base, through ed-gbm-v1, feat-ed-util-trend-v1 and feat-ed-cashadv-v1. Its body also lists feat-ed-minpay-v2, which comes from ds-ed-label-30p3m, but that link is not recorded in the graph, so ds-ed-label-30p3m is included with that caveat.
Notes: early-delinquency/ds-ed-current-base.md, early-delinquency/ds-ed-label-30p3m.md

## Q8
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25 and dec-f26-promote-v3 in fraud-2026, plus dec-disp-fraud-score-in in dispute-triage. The last reaches it through feat-disp-fraud-score and fraud26-gbm-v3.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests on two dataset notes: ds-ep-assignments (4.2M units across 38 tests) and ds-ep-test-registry (38 tests with planned n and horizon). It reaches them through exp-507, feat-ep-prior-logins-14d and feat-ep-tenure-months.
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default. They reach it through the matched-control experiments, feat-hp-match-covars-v1, hp-psm-v1 and hp-psm-v2.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md