## Q1
It rests on three dataset notes: ds-clv-cohort-panel and ds-clv-holdout-2021h1 directly, and ds-clv-revenue-monthly through feat-clv-arpu-v1 (the six-month revenue feature). The cohort panel also feeds feat-clv-tenure and ds-clv-revenue-monthly.
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/exp-501.md, customer-lifetime-value/feat-clv-arpu-v1.md, customer-lifetime-value/feat-clv-tenure.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-revenue-monthly.md, customer-lifetime-value/ds-clv-cohort-panel.md

## Q2
dec-ed-promote-v3 and dec-ed-gbm-for-watchlist. The first rests on ed-gbm-v3 and the bureau-slope chain (exp-207, feat-ed-bureau-slope-v1). The second rests on find-ed-gbm-vs-logit, which goes through exp-201 and the champion scorecard ed-logit-v1.
Notes: early-delinquency/ds-ed-bureau-join.md, early-delinquency/feat-ed-bureau-slope-v1.md, early-delinquency/exp-207.md, early-delinquency/ed-gbm-v3.md, early-delinquency/find-ed-bureau-slope.md, early-delinquency/dec-ed-promote-v3.md, early-delinquency/ed-logit-v1.md, early-delinquency/exp-201.md, early-delinquency/find-ed-gbm-vs-logit.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
sfc-hier-v3 is in force (sfc-ets-v1 was replaced by sfc-lgbm-v2, which was replaced by sfc-hier-v3). It is built on exp-207 (MinT reconciliation), feat-sfc-active-accounts, fnd-sfc-q4-reconciled and the per-segment LightGBM model sfc-lgbm-v2.
Notes: spend-forecasting/sfc-ets-v1.md, spend-forecasting/sfc-lgbm-v2.md, spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/fnd-sfc-q4-reconciled.md

## Q4
ds-disp-analyst-labels and ds-disp-disputes. The analyst labels rest on the cards.disputes table, and disp-lgbm-v1 uses those labels both directly and through dec-disp-labels-two-analyst and q-disp-label-source.
Notes: dispute-triage/disp-lgbm-v1.md, dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/q-disp-label-source.md, dispute-triage/feat-disp-reason-text.md, dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
dec-fsm-cutover and dec-fsm-timezone-utc. Both trace back to the parity sample through exp-101 and exp-102 (the timezone decision), and through exp-107 and feat-fsm-util-ratio (the cutover decision).
Notes: feature-store-migration/ds-fsm-parity-sample.md, feature-store-migration/exp-101.md, feature-store-migration/exp-102.md, feature-store-migration/fnd-parity-pre-fix.md, feature-store-migration/dec-fsm-timezone-utc.md, feature-store-migration/fnd-parity-post-fix.md, feature-store-migration/exp-107.md, feature-store-migration/feat-fsm-util-ratio.md, feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fnd-churn-lift.md, feature-store-migration/dec-fsm-cutover.md

## Q6
txc-gbm-v3 is in force (txc-logreg-v1 was replaced by txc-gbm-v2, which was replaced by txc-gbm-v3). It is built on feat-txc-descriptor-tokens-v2, feat-txc-normalise-v2 (the descriptor normalisation), feat-txc-mcc-prior and txc-gbm-v2.
Notes: txn-categorization/txc-logreg-v1.md, txn-categorization/txc-gbm-v2.md, txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md

## Q7
ds-ed-current-base and ds-ed-label-30p3m. ed-gbm-v2 rests on the current-account base through ed-gbm-v1 and its features, and on the 30+ label through feat-ed-minpay-v2 (used in exp-205 and exp-206).
Notes: early-delinquency/ed-gbm-v2.md, early-delinquency/ed-gbm-v1.md, early-delinquency/feat-ed-cashadv-v1.md, early-delinquency/feat-ed-util-trend-v1.md, early-delinquency/ds-ed-current-base.md, early-delinquency/exp-205.md, early-delinquency/feat-ed-minpay-v2.md, early-delinquency/ds-ed-label-30p3m.md, early-delinquency/exp-206.md

## Q8
dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-promote-v3 and dec-f26-replace-f25. The first three rest on the 60-day maturity cut, which depends on the 2026 labels; dec-f26-replace-f25 rests on fraud26-gbm-v1, which was trained on those labels.
Notes: fraud-2026/ds-f26-labels-2026.md, fraud-2026/q-f26-label-lag.md, fraud-2026/exp-201.md, fraud-2026/exp-202.md, fraud-2026/fraud26-find-label-bias.md, fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/ds-f26-oot-2026h1.md, fraud-2026/exp-207.md, fraud-2026/exp-208.md, fraud-2026/dec-f26-promote-v3.md

## Q9
ds-ep-assignments and ds-ep-test-registry. ep-uplift-forest-v1 rests on exp-507, which uses the test registry, and on the prior-logins and tenure features, both of which are built on the assignments table.
Notes: experiment-platform/ep-uplift-forest-v1.md, experiment-platform/exp-507.md, experiment-platform/feat-ep-prior-logins-14d.md, experiment-platform/feat-ep-tenure-months.md, experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
dec-hp-6mo-default, dec-hp-report-did and dec-hp-smd-gate. Each rests on ds-hp-matched-controls through exp-405 and hp-psm-v1, exp-404 (difference-in-differences), or exp-408 and feat-hp-bureau-delta.
Notes: hardship-programs/ds-hp-matched-controls.md, hardship-programs/hp-psm-v1.md, hardship-programs/exp-404.md, hardship-programs/exp-405.md, hardship-programs/find-hp-plan-length.md, hardship-programs/dec-hp-6mo-default.md, hardship-programs/feat-hp-bureau-delta.md, hardship-programs/exp-408.md, hardship-programs/hp-psm-v2.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/find-hp-effect-v2.md, hardship-programs/dec-hp-report-did.md