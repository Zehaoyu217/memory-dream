## Q1
clv-bgnbd-v1 rests on three dataset notes: the 2021 H1 holdout (ds-clv-holdout-2021h1), monthly revenue (ds-clv-revenue-monthly) and the origination cohort panel (ds-clv-cohort-panel). The holdout comes in through exp-501, revenue through feat-clv-arpu-v1, and the cohort panel through the holdout, revenue and feat-clv-tenure.
Notes: customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-revenue-monthly.md, customer-lifetime-value/ds-clv-cohort-panel.md

## Q2
Two decisions rest on it. dec-ed-gbm-for-watchlist comes through ed-logit-v1 → exp-201/exp-202 → find-ed-gbm-vs-logit. dec-ed-promote-v3 comes through feat-ed-bureau-slope-v1 → exp-207 / ed-gbm-v3 / find-ed-bureau-slope; it later replaced dec-ed-gbm-for-watchlist.
Notes: early-delinquency/dec-ed-gbm-for-watchlist.md, early-delinquency/dec-ed-promote-v3.md

## Q3
The line runs sfc-ets-v1 → sfc-lgbm-v2 → sfc-hier-v3, and sfc-hier-v3 is the one in force now. It is built on exp-207 (the MinT reconciliation test), feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/sfc-lgbm-v2.md

## Q4
disp-lgbm-v1 rests on two dataset notes: the analyst labels (ds-disp-analyst-labels) and cards.disputes (ds-disp-disputes). The labels come in directly and through dec-disp-labels-two-analyst; cards.disputes comes in through the labels and feat-disp-reason-text.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decisions rest on it. dec-fsm-timezone-utc comes through exp-101 → exp-102 / fnd-parity-pre-fix. dec-fsm-cutover comes through fnd-parity-post-fix, fsm-churn-xgb-v2 and fnd-churn-lift, which lead back to exp-101 and exp-107. model-monitoring/mm-limit-glm-v2 also uses it indirectly (through feat-fsm-util-ratio), but no decision is built on that model.
Notes: feature-store-migration/dec-fsm-timezone-utc.md, feature-store-migration/dec-fsm-cutover.md

## Q6
The line runs txc-logreg-v1 → txc-gbm-v2 → txc-gbm-v3, and txc-gbm-v3 is the one in force now. It is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
ed-gbm-v2 rests on two dataset notes: the current-account base (ds-ed-current-base) and the 30+ within 3 months label (ds-ed-label-30p3m). The base comes in through ed-gbm-v1's util-trend and cash-advance features; the label comes in through feat-ed-minpay-v2, which exp-205 and exp-206 use.
Notes: early-delinquency/ds-ed-current-base.md, early-delinquency/ds-ed-label-30p3m.md

## Q8
Five decisions rest on it. Four are in fraud-2026: dec-f26-maturity-60d, dec-f26-replace-f25 (through fraud26-gbm-v1), dec-f26-promote-v2 and dec-f26-promote-v3 (through fraud26-gbm-v2 and v3). The fifth is in dispute-triage: dec-disp-fraud-score-in, through feat-disp-fraud-score, which uses fraud26-gbm-v3.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests on two dataset notes: the test registry (ds-ep-test-registry) and the assignments table (ds-ep-assignments). The registry comes in through exp-507; the assignments table comes in through feat-ep-prior-logins-14d and feat-ep-tenure-months.
Notes: experiment-platform/ds-ep-test-registry.md, experiment-platform/ds-ep-assignments.md

## Q10
Three decisions rest on it. dec-hp-report-did comes through exp-404 and find-hp-effect-v2. dec-hp-smd-gate comes through hp-psm-v1 / feat-hp-bureau-delta → exp-408 / hp-psm-v2. dec-hp-6mo-default comes through hp-psm-v1 → exp-405 → find-hp-plan-length.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md