## Q1
clv-bgnbd-v1 rests on three dataset notes: ds-clv-cohort-panel, ds-clv-revenue-monthly and ds-clv-holdout-2021h1. It gets there through exp-501 (the BG/NBD vs GBM test), feat-clv-arpu-v1 (six-month revenue) and feat-clv-tenure (months on book).
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/exp-501.md, customer-lifetime-value/feat-clv-arpu-v1.md, customer-lifetime-value/feat-clv-tenure.md, customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-revenue-monthly.md, customer-lifetime-value/ds-clv-holdout-2021h1.md

## Q2
Two decision notes: dec-ed-gbm-for-watchlist and dec-ed-promote-v3. The first reaches ds-ed-bureau-join through find-ed-gbm-vs-logit, exp-201 and the scorecard ed-logit-v1; the second through feat-ed-bureau-slope-v1, exp-207, ed-gbm-v3 and find-ed-bureau-slope.
Notes: early-delinquency/ds-ed-bureau-join.md, early-delinquency/ed-logit-v1.md, early-delinquency/exp-201.md, early-delinquency/find-ed-gbm-vs-logit.md, early-delinquency/dec-ed-gbm-for-watchlist.md, early-delinquency/feat-ed-bureau-slope-v1.md, early-delinquency/exp-207.md, early-delinquency/ed-gbm-v3.md, early-delinquency/find-ed-bureau-slope.md, early-delinquency/dec-ed-promote-v3.md

## Q3
sfc-hier-v3 is the note in force. The line runs sfc-ets-v1, replaced by sfc-lgbm-v2, which was replaced by sfc-hier-v3. sfc-hier-v3 is built on exp-207 (MinT reconciliation), feat-sfc-active-accounts, fnd-sfc-q4-reconciled and the per-segment LightGBM model, sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/sfc-lgbm-v2.md, spend-forecasting/sfc-ets-v1.md, spend-forecasting/exp-207.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/fnd-sfc-q4-reconciled.md

## Q4
disp-lgbm-v1 rests on two dataset notes: ds-disp-analyst-labels and ds-disp-disputes (cards.disputes). It reaches them through the two-analyst label decision (dec-disp-labels-two-analyst, with q-disp-label-source) and the reason-text feature feat-disp-reason-text.
Notes: dispute-triage/disp-lgbm-v1.md, dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/q-disp-label-source.md, dispute-triage/feat-disp-reason-text.md, dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes: dec-fsm-timezone-utc and dec-fsm-cutover. The first rests on ds-fsm-parity-sample through exp-101, exp-102 and fnd-parity-pre-fix. The second rests on it through fnd-parity-post-fix, fnd-churn-lift, exp-105 and exp-107, which also feed fsm-churn-xgb-v2.
Notes: feature-store-migration/ds-fsm-parity-sample.md, feature-store-migration/exp-101.md, feature-store-migration/exp-102.md, feature-store-migration/exp-107.md, feature-store-migration/fnd-parity-pre-fix.md, feature-store-migration/fnd-parity-post-fix.md, feature-store-migration/dec-fsm-timezone-utc.md, feature-store-migration/dec-fsm-cutover.md, feature-store-migration/fnd-churn-lift.md, feature-store-migration/exp-105.md, feature-store-migration/feat-fsm-util-ratio.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/fsm-churn-xgb-v2.md

## Q6
txc-gbm-v3 is the note in force. The line runs txc-logreg-v1, replaced by txc-gbm-v2, which was replaced by txc-gbm-v3. txc-gbm-v3 is built on feat-txc-descriptor-tokens-v2, feat-txc-normalise-v2, feat-txc-mcc-prior and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/txc-gbm-v2.md, txn-categorization/txc-logreg-v1.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/feat-txc-mcc-prior.md

## Q7
ed-gbm-v2 rests on two dataset notes: ds-ed-current-base and ds-ed-label-30p3m. It gets there through ed-gbm-v1, exp-205, exp-206, and the features feat-ed-util-trend-v1, feat-ed-cashadv-v1 and feat-ed-minpay-v2.
Notes: early-delinquency/ed-gbm-v2.md, early-delinquency/ed-gbm-v1.md, early-delinquency/exp-205.md, early-delinquency/exp-206.md, early-delinquency/feat-ed-util-trend-v1.md, early-delinquency/feat-ed-cashadv-v1.md, early-delinquency/feat-ed-minpay-v2.md, early-delinquency/ds-ed-label-30p3m.md, early-delinquency/ds-ed-current-base.md

## Q8
Four fraud-2026 decisions rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-replace-f25, dec-f26-promote-v2 and dec-f26-promote-v3. A fifth, dispute-triage's dec-disp-fraud-score-in, rests on it across projects through feat-disp-fraud-score and fraud26-gbm-v3.
Notes: fraud-2026/ds-f26-labels-2026.md, fraud-2026/ds-f26-oot-2026h1.md, fraud-2026/q-f26-label-lag.md, fraud-2026/exp-201.md, fraud-2026/exp-202.md, fraud-2026/fraud26-find-label-bias.md, fraud-2026/dec-f26-maturity-60d.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/feat-f26-mcc-risk.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/exp-206.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/exp-207.md, fraud-2026/fraud26-gbm-v3.md, fraud-2026/exp-208.md, fraud-2026/fraud26-find-geo-drift.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/feat-disp-fraud-score.md, dispute-triage/exp-307.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests on two dataset notes: ds-ep-assignments and ds-ep-test-registry. It reaches them through exp-507, feat-ep-prior-logins-14d and feat-ep-tenure-months.
Notes: experiment-platform/ep-uplift-forest-v1.md, experiment-platform/exp-507.md, experiment-platform/feat-ep-prior-logins-14d.md, experiment-platform/feat-ep-tenure-months.md, experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-6mo-default, dec-hp-report-did and dec-hp-smd-gate. They reach it through exp-405 and hp-psm-v1 (plan length), exp-404 (difference-in-differences), and exp-408 and hp-psm-v2 (the caliper-matched effect).
Notes: hardship-programs/ds-hp-matched-controls.md, hardship-programs/hp-psm-v1.md, hardship-programs/hp-psm-v2.md, hardship-programs/exp-404.md, hardship-programs/exp-405.md, hardship-programs/exp-408.md, hardship-programs/find-hp-plan-length.md, hardship-programs/find-hp-effect-v2.md, hardship-programs/dec-hp-6mo-default.md, hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md