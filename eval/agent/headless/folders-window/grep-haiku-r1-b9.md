## Q1
clv-bgnbd-v1 rests on three dataset notes: the cohort panel (ds-clv-cohort-panel) directly through its tenure feature, the monthly revenue dataset (ds-clv-revenue-monthly) through feat-clv-arpu-v1, and the 2021 H1 holdout (ds-clv-holdout-2021h1) through exp-501. The revenue and holdout notes both trace back to the cohort panel.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-revenue-monthly.md, customer-lifetime-value/ds-clv-holdout-2021h1.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3 through ed-gbm-v3 and feat-ed-bureau-slope-v1, and dec-ed-gbm-for-watchlist through find-ed-gbm-vs-logit, exp-201 and the ed-logit-v1 scorecard.
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
The line runs sfc-ets-v1 → sfc-lgbm-v2 → sfc-hier-v3, so sfc-hier-v3 is in force. It is built on the MinT reconciliation experiment (exp-207), feat-sfc-active-accounts, fnd-sfc-q4-reconciled and the per-segment LightGBM model sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/sfc-lgbm-v2.md

## Q4
disp-lgbm-v1 rests on two dataset notes: the analyst dispute labels (ds-disp-analyst-labels), which the two-analyst label rule is built on, and the cards.disputes dataset (ds-disp-disputes), which the analyst labels and the reason-text feature both build on.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-timezone-utc through exp-101, exp-102 and fnd-parity-pre-fix, and dec-fsm-cutover through fnd-parity-post-fix and fsm-churn-xgb-v2. dec-fsm-naming-rule does not, because its lineage (exp-103) never touches the sample.
Notes: feature-store-migration/dec-fsm-timezone-utc.md, feature-store-migration/dec-fsm-cutover.md

## Q6
The line runs txc-logreg-v1 → txc-gbm-v2 → txc-gbm-v3, so txc-gbm-v3 is in force. It is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
ed-gbm-v2 rests on two dataset notes: the current-account base (ds-ed-current-base), which its utilisation-trend and cash-advance features build on, and the 30+ within 3 months label (ds-ed-label-30p3m), which its payment-to-minimum feature builds on.
Notes: early-delinquency/ds-ed-current-base.md, early-delinquency/ds-ed-label-30p3m.md

## Q8
Four decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d through its experiments and label-bias finding, dec-f26-replace-f25 through fraud26-gbm-v1, and dec-f26-promote-v2 and dec-f26-promote-v3 through fraud26-gbm-v2 and fraud26-gbm-v3.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-promote-v3.md

## Q9
ep-uplift-forest-v1 rests on two dataset notes: the assignments table (ds-ep-assignments), which the prior-logins and tenure features build on, and the test registry (ds-ep-test-registry), which exp-507 builds on.
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-6mo-default through exp-405 and hp-psm-v1, dec-hp-smd-gate through exp-408 and hp-psm-v2, and dec-hp-report-did through exp-404.
Notes: hardship-programs/dec-hp-6mo-default.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-report-did.md