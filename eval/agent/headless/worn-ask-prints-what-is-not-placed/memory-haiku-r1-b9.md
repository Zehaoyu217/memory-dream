## Q1
clv-bgnbd-v1 rests directly on feat-clv-arpu-v1 and feat-clv-tenure, which rest on the dataset notes ds-clv-cohort-panel and ds-clv-revenue-monthly. The note also names a "bg/nbd versus gbm accuracy test" that has no note in the memory, so the chain may be incomplete.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3, which is built on ed-gbm-v3 and the bureau-slope finding, and dec-ed-gbm-for-watchlist, which is built on the chain through ed-gbm-v3 and ed-gbm-v2.
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
The note in force at the end of the sfc-ets-v1 line is sfc-hier-v3, which replaced sfc-lgbm-v2. sfc-hier-v3 is built on exp-207, fnd-sfc-q4-reconciled, feat-sfc-active-accounts and sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/sfc-lgbm-v2.md

## Q4
disp-lgbm-v1 rests directly on ds-disp-analyst-labels, and through dec-disp-labels-two-analyst and feat-disp-reason-text it reaches ds-disp-disputes. The dataset notes are therefore ds-disp-analyst-labels and ds-disp-disputes.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-cutover and dec-fsm-timezone-utc. Both come through exp-101, exp-102 and fnd-parity-pre-fix.
Notes: feature-store-migration/dec-fsm-cutover.md, feature-store-migration/dec-fsm-timezone-utc.md

## Q6
The note in force at the end of the txc-logreg-v1 line is txc-gbm-v3, which replaced txc-gbm-v2. txc-gbm-v3 is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
ed-gbm-v2 rests on ds-ed-current-base, reached through ed-gbm-v1 and the feat-ed-cashadv-v1 and feat-ed-util-trend-v1 features. That is the only dataset note in its chain.
Notes: early-delinquency/ds-ed-current-base.md

## Q8
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25 and dec-f26-promote-v3 in fraud-2026, plus dec-disp-fraud-score-in in dispute-triage, which reaches it through the fraud-2026 score.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests directly on exp-507, feat-ep-prior-logins-14d and feat-ep-tenure-months. Through those it reaches the dataset notes ds-ep-assignments and ds-ep-test-registry.
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default. They reach it through exp-402, hp-psm-v1, hp-psm-v2 and the related findings.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md