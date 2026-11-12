## Q1
clv-bgnbd-v1 rests on two dataset notes: ds-clv-cohort-panel (directly through feat-clv-tenure and feat-clv-arpu-v1) and ds-clv-revenue-monthly (through feat-clv-arpu-v1). Its text also names a "bg/nbd versus gbm accuracy test" that no note is linked to, so the chain may be incomplete.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3 (via find-ed-bureau-slope, exp-207 and feat-ed-bureau-slope-v1) and dec-ed-gbm-for-watchlist (via find-ed-gbm-vs-logit, exp-201 and ed-logit-v1).
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
The note in force at the end of the sfc-ets-v1 → sfc-lgbm-v2 → sfc-hier-v3 line is sfc-hier-v3. It is built on exp-207, fnd-sfc-q4-reconciled, feat-sfc-active-accounts and sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/sfc-lgbm-v2.md

## Q4
disp-lgbm-v1 rests on two dataset notes: ds-disp-analyst-labels (directly) and ds-disp-disputes (through ds-disp-analyst-labels and feat-disp-reason-text).
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-cutover (via fnd-churn-lift and fnd-parity-post-fix) and dec-fsm-timezone-utc (via exp-102 and fnd-parity-pre-fix).
Notes: feature-store-migration/dec-fsm-cutover.md, feature-store-migration/dec-fsm-timezone-utc.md

## Q6
The note in force at the end of the txc-logreg-v1 → txc-gbm-v2 → txc-gbm-v3 line is txc-gbm-v3. It is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
ed-gbm-v2 rests on one dataset note, ds-ed-current-base, reached through ed-gbm-v1, feat-ed-cashadv-v1 and feat-ed-util-trend-v1. Its description also mentions a min-pay ratio, but no link to feat-ed-minpay-v2 or ds-ed-label-30p3m is recorded for ed-gbm-v2, so I have not included them.
Notes: early-delinquency/ds-ed-current-base.md

## Q8
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25 and dec-f26-promote-v3 in fraud-2026, and dispute-triage/dec-disp-fraud-score-in, which reaches it through fraud26-gbm-v3.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests on two dataset notes: ds-ep-assignments (through feat-ep-prior-logins-14d and feat-ep-tenure-months) and ds-ep-test-registry (through exp-507).
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did (via exp-404), dec-hp-smd-gate (via exp-408 and hp-psm-v2) and dec-hp-6mo-default (via exp-405 and find-hp-plan-length).
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md