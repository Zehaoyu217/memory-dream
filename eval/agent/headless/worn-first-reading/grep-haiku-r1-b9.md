## Q1
clv-bgnbd-v1 rests on ds-clv-cohort-panel, directly and through feat-clv-tenure and exp-501. It also rests on ds-clv-revenue-monthly, through feat-clv-arpu-v1, and on ds-clv-holdout-2021h1, through exp-501.
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/exp-501.md, customer-lifetime-value/feat-clv-arpu-v1.md, customer-lifetime-value/feat-clv-tenure.md, customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-revenue-monthly.md, customer-lifetime-value/ds-clv-holdout-2021h1.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-gbm-for-watchlist, through ed-logit-v1 and find-ed-gbm-vs-logit, and dec-ed-promote-v3, through feat-ed-bureau-slope-v1, exp-207 and find-ed-bureau-slope.
Notes: early-delinquency/dec-ed-gbm-for-watchlist.md, early-delinquency/dec-ed-promote-v3.md, early-delinquency/ds-ed-bureau-join.md, early-delinquency/ed-logit-v1.md, early-delinquency/exp-201.md, early-delinquency/find-ed-gbm-vs-logit.md, early-delinquency/feat-ed-bureau-slope-v1.md, early-delinquency/exp-207.md, early-delinquency/find-ed-bureau-slope.md

## Q3
The line runs sfc-ets-v1, then sfc-lgbm-v2, then sfc-hier-v3. sfc-hier-v3 is the note in force, adopted by dec-sfc-ship-hier-v3 with nothing replacing it since. It is built on exp-207 (MinT reconciliation), feat-sfc-active-accounts, fnd-sfc-q4-reconciled and the per-segment LightGBM model, sfc-lgbm-v2.
Notes: spend-forecasting/sfc-ets-v1.md, spend-forecasting/sfc-lgbm-v2.md, spend-forecasting/sfc-hier-v3.md, spend-forecasting/dec-sfc-ship-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/fnd-sfc-q4-reconciled.md

## Q4
disp-lgbm-v1 rests on ds-disp-analyst-labels, directly and through dec-disp-labels-two-analyst and q-disp-label-source. It also rests on ds-disp-disputes, through feat-disp-reason-text and ds-disp-analyst-labels.
Notes: dispute-triage/disp-lgbm-v1.md, dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/q-disp-label-source.md, dispute-triage/feat-disp-reason-text.md, dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-timezone-utc, through exp-102 and exp-101, and dec-fsm-cutover, through fnd-parity-post-fix, fsm-churn-xgb-v2 and feat-fsm-util-ratio (via exp-107). dec-fsm-naming-rule does not rest on it.
Notes: feature-store-migration/dec-fsm-timezone-utc.md, feature-store-migration/dec-fsm-cutover.md, feature-store-migration/ds-fsm-parity-sample.md, feature-store-migration/exp-101.md, feature-store-migration/exp-102.md, feature-store-migration/exp-107.md, feature-store-migration/fnd-parity-post-fix.md, feature-store-migration/feat-fsm-util-ratio.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/exp-105.md

## Q6
The line runs txc-logreg-v1, then txc-gbm-v2, then txc-gbm-v3. txc-gbm-v3 is the note in force, and it is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 (the descriptor normalisation feature) and txc-gbm-v2.
Notes: txn-categorization/txc-logreg-v1.md, txn-categorization/txc-gbm-v2.md, txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md

## Q7
ed-gbm-v2 rests on ds-ed-current-base, through ed-gbm-v1 and feat-ed-cashadv-v1 or feat-ed-util-trend-v1, and on ds-ed-label-30p3m, through exp-205 and feat-ed-minpay-v2.
Notes: early-delinquency/ed-gbm-v2.md, early-delinquency/ed-gbm-v1.md, early-delinquency/exp-205.md, early-delinquency/exp-206.md, early-delinquency/feat-ed-cashadv-v1.md, early-delinquency/feat-ed-util-trend-v1.md, early-delinquency/feat-ed-minpay-v2.md, early-delinquency/ds-ed-current-base.md, early-delinquency/ds-ed-label-30p3m.md

## Q8
Four fraud-2026 decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-replace-f25, dec-f26-promote-v2 and dec-f26-promote-v3. One decision in another project, dispute-triage/dec-disp-fraud-score-in, also rests on it, through feat-disp-fraud-score and fraud26-gbm-v3.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md, fraud-2026/ds-f26-labels-2026.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/fraud26-gbm-v3.md, fraud-2026/fraud26-find-label-bias.md, fraud-2026/q-f26-label-lag.md, fraud-2026/exp-201.md, fraud-2026/exp-202.md

## Q9
ep-uplift-forest-v1 rests on ds-ep-test-registry, through exp-507, and on ds-ep-assignments, through feat-ep-prior-logins-14d and feat-ep-tenure-months.
Notes: experiment-platform/ep-uplift-forest-v1.md, experiment-platform/exp-507.md, experiment-platform/feat-ep-prior-logins-14d.md, experiment-platform/feat-ep-tenure-months.md, experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-6mo-default, through find-hp-plan-length, exp-405 and hp-psm-v1; dec-hp-report-did, through exp-404 and find-hp-effect-v2; and dec-hp-smd-gate, through exp-408 and hp-psm-v2.
Notes: hardship-programs/dec-hp-6mo-default.md, hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/ds-hp-matched-controls.md, hardship-programs/find-hp-plan-length.md, hardship-programs/exp-405.md, hardship-programs/hp-psm-v1.md, hardship-programs/exp-404.md, hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-408.md, hardship-programs/hp-psm-v2.md