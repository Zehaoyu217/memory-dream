## Q1
clv-bgnbd-v1 rests on three dataset notes: the cohort panel, the 2021 H1 holdout, and monthly revenue per account, the last two through exp-501 and feat-clv-arpu-v1.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3 directly through ed-gbm-v3, and dec-ed-gbm-for-watchlist through ed-gbm-v3 and the bureau-slope chain.
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
The line is sfc-ets-v1 → sfc-lgbm-v2 → sfc-hier-v3, and sfc-hier-v3 is the one in force. It is built on exp-207, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/sfc-lgbm-v2.md

## Q4
disp-lgbm-v1 rests on two dataset notes: the analyst hand labels directly, and the underlying disputes table through them.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-cutover and dec-fsm-timezone-utc, the latter through exp-102 and fnd-parity-pre-fix.
Notes: feature-store-migration/dec-fsm-cutover.md, feature-store-migration/dec-fsm-timezone-utc.md

## Q6
The line is txc-logreg-v1 → txc-gbm-v2 → txc-gbm-v3, and txc-gbm-v3 is the one in force. It is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
ed-gbm-v2 rests on one dataset note, ds-ed-current-base, through ed-gbm-v1 and the two features feat-ed-cashadv-v1 and feat-ed-util-trend-v1. One unresolved feature, feat-ed-minpay-v2, may also link to ed-gbm-v2, but the notes don't confirm it.
Notes: early-delinquency/ds-ed-current-base.md

## Q8
Five decision notes rest on ds-f26-labels-2026: four in fraud-2026 and dec-disp-fraud-score-in in dispute-triage, the last through the fraud score feature and disp-lgbm-v3.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests on two dataset notes: ds-ep-assignments and ds-ep-test-registry, both reached through exp-507 and its features.
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default, all reached through the matched-control experiments and models.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md