## Q1
clv-bgnbd-v1 is built on exp-501, feat-clv-arpu-v1 and feat-clv-tenure. Following those back, it rests on three dataset notes: the 2021 H1 holdout (ds-clv-holdout-2021h1), the monthly revenue table (ds-clv-revenue-monthly) and, under both of those, the origination cohort panel (ds-clv-cohort-panel).
Notes: customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-revenue-monthly.md, customer-lifetime-value/ds-clv-cohort-panel.md

## Q2
Two decision notes rest on it. dec-ed-gbm-for-watchlist rests on it through ed-logit-v1 → exp-201/exp-202 → find-ed-gbm-vs-logit. dec-ed-promote-v3 rests on it through feat-ed-bureau-slope-v1 → exp-207, find-ed-bureau-slope and ed-gbm-v3. dec-ed-drop-limit-feature does not rest on the bureau join.
Notes: early-delinquency/dec-ed-gbm-for-watchlist.md, early-delinquency/dec-ed-promote-v3.md

## Q3
sfc-ets-v1 was replaced by sfc-lgbm-v2, which was replaced by sfc-hier-v3, the note in force now. sfc-hier-v3 is built on exp-207 (the MinT reconciliation experiment), feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2 (the per-segment LightGBM).
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/sfc-lgbm-v2.md

## Q4
disp-lgbm-v1 is built on dec-disp-labels-two-analyst, ds-disp-analyst-labels and feat-disp-reason-text. Following those back, it rests on two dataset notes: the analyst labels (ds-disp-analyst-labels) and, under them and the reason-text feature, cards.disputes (ds-disp-disputes).
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on it. dec-fsm-timezone-utc rests on it through exp-101 → exp-102 and fnd-parity-pre-fix. dec-fsm-cutover rests on it through fnd-parity-post-fix, fnd-churn-lift (via exp-107) and fsm-churn-xgb-v2. dec-fsm-naming-rule does not rest on the parity sample. model-monitoring/mm-limit-glm-v2 also uses a feature built on the sample, but no decision note builds on that model.
Notes: feature-store-migration/dec-fsm-timezone-utc.md, feature-store-migration/dec-fsm-cutover.md

## Q6
txc-logreg-v1 was replaced by txc-gbm-v2, which was replaced by txc-gbm-v3, the note in force now. txc-gbm-v3 is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 (the descriptor normalisation feature) and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
ed-gbm-v2 is built on ed-gbm-v1, exp-205 and exp-206. Following those back, it rests on two dataset notes: the current-account base (ds-ed-current-base), through the cash-advance and utilisation features, and the 30+ in 3 months label (ds-ed-label-30p3m), through feat-ed-minpay-v2.
Notes: early-delinquency/ds-ed-current-base.md, early-delinquency/ds-ed-label-30p3m.md

## Q8
Four fraud-2026 decision notes rest on it: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-promote-v3 and dec-f26-replace-f25 (through fraud26-gbm-v1). A fifth sits in another project: dispute-triage/dec-disp-fraud-score-in rests on it through feat-disp-fraud-score, which uses fraud26-gbm-v3.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-promote-v3.md, fraud-2026/dec-f26-replace-f25.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 is built on exp-507, feat-ep-prior-logins-14d and feat-ep-tenure-months. Following those back, it rests on two dataset notes: the test registry (ds-ep-test-registry) and the assignments table (ds-ep-assignments).
Notes: experiment-platform/ds-ep-test-registry.md, experiment-platform/ds-ep-assignments.md

## Q10
Three decision notes rest on it. dec-hp-report-did rests on it through exp-404 and find-hp-effect-v2. dec-hp-smd-gate rests on it through hp-psm-v1 → exp-408 and hp-psm-v2. dec-hp-6mo-default rests on it through hp-psm-v1 → exp-405 → find-hp-plan-length.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md