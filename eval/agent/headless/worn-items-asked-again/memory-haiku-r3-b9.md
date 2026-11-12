## Q1
clv-bgnbd-v1 rests on two dataset notes, ds-clv-cohort-panel (2.4M accounts by origination quarter) and ds-clv-revenue-monthly (monthly revenue per account), reached through feat-clv-arpu-v1 and feat-clv-tenure.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3, which promotes ed-gbm-v3 to the watchlist, and dec-ed-gbm-for-watchlist. Both reach it through ed-logit-v1 or feat-ed-bureau-slope-v1.
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
The note in force is sfc-hier-v3, the current segment forecast with 2.3% total MAPE. It is directly built on exp-207, fnd-sfc-q4-reconciled, feat-sfc-active-accounts and sfc-lgbm-v2, and through sfc-lgbm-v2 it goes back to sfc-ets-v1 and ds-sfc-segment-monthly.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/sfc-lgbm-v2.md

## Q4
disp-lgbm-v1 rests on two dataset notes, ds-disp-analyst-labels (8,900 hand labels) and ds-disp-disputes (cards.disputes, 41,870 disputes). The second is reached through dec-disp-labels-two-analyst and feat-disp-reason-text.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-timezone-utc, which moves all date windows to UTC, and dec-fsm-cutover. Both reach it through exp-101 and fnd-parity-pre-fix.
Notes: feature-store-migration/dec-fsm-timezone-utc.md, feature-store-migration/dec-fsm-cutover.md

## Q6
The note in force is txc-gbm-v3, the current model with macro-F1 0.83. It is directly built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2, and through txc-gbm-v2 it goes back to txc-logreg-v1.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
ed-gbm-v2 rests directly on ed-gbm-v1, and through it on feat-ed-cashadv-v1 and feat-ed-util-trend-v1. Its only dataset note is ds-ed-current-base, the 0-DPD current-account scoring base.
Notes: early-delinquency/ds-ed-current-base.md

## Q8
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25 and dec-f26-promote-v3 in fraud-2026, plus dispute-triage/dec-disp-fraud-score-in, which reaches it through the fraud-2026 score feature.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests on two dataset notes, ds-ep-assignments (4.2M unit-test rows) and ds-ep-test-registry (38 tests with pre-registered metrics). They are reached through exp-507, feat-ep-prior-logins-14d and feat-ep-tenure-months.
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default. They reach it directly or through hp-psm-v1 and hp-psm-v2.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md