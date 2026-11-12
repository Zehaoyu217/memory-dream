## Q1
The dataset notes behind clv-bgnbd-v1 are ds-clv-cohort-panel (2.4M accounts from cards.accounts_monthly) and ds-clv-revenue-monthly (from cards.txn_daily and cards.payments_daily). They reach it through feat-clv-arpu-v1 and feat-clv-tenure.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
The decisions resting on ds-ed-bureau-join are dec-ed-promote-v3, which promotes ed-gbm-v3 to the watchlist, and dec-ed-gbm-for-watchlist. Both reach it through feat-ed-bureau-slope-v1 and ed-gbm-v3.
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
The note in force is sfc-hier-v3, the current segment forecast with total MAPE 2.3%, which replaced sfc-lgbm-v2 and, before that, sfc-ets-v1. It is built on exp-207, fnd-sfc-q4-reconciled, feat-sfc-active-accounts and sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/sfc-lgbm-v2.md

## Q4
The dataset notes behind disp-lgbm-v1 are ds-disp-analyst-labels (8,900 hand labels, 7,450 with two-analyst agreement) and ds-disp-disputes (cards.disputes, 41,870 disputes). They are reached through dec-disp-labels-two-analyst and the question q-disp-label-source.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
The decisions resting on ds-fsm-parity-sample are dec-fsm-timezone-utc, which moves all date windows to UTC, and dec-fsm-cutover. Both reach it through exp-101, exp-102 and the parity findings.
Notes: feature-store-migration/dec-fsm-timezone-utc.md, feature-store-migration/dec-fsm-cutover.md

## Q6
The note in force is txc-gbm-v3, the current model with macro-F1 0.83 on txc-oot-2026h1, which replaced txc-gbm-v2 and, before that, txc-logreg-v1. It is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
The only dataset note behind ed-gbm-v2 is ds-ed-current-base, the current-account base at 0 DPD. It reaches ed-gbm-v2 through ed-gbm-v1, feat-ed-cashadv-v1 and feat-ed-util-trend-v1.
Notes: early-delinquency/ds-ed-current-base.md

## Q8
The decisions resting on ds-f26-labels-2026 are dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25 and dec-f26-promote-v3 in fraud-2026, plus dec-disp-fraud-score-in in dispute-triage. The last one reaches it through feat-disp-fraud-score and fraud26-gbm-v3.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
The dataset notes behind ep-uplift-forest-v1 are ds-ep-assignments (4.2M units across 38 tests) and ds-ep-test-registry (38 tests with owner, metric and planned n). They reach it through feat-ep-prior-logins-14d, feat-ep-tenure-months and exp-507.
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
The decisions resting on ds-hp-matched-controls are dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default. They reach it through hp-psm-v1, hp-psm-v2 and the matched-controls experiments.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md