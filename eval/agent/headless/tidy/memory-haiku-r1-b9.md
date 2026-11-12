## Q1
clv-bgnbd-v1 rests on three dataset notes: the cohort panel of 2.4M accounts, the 2021 H1 holdout, and monthly revenue per account. It reaches them directly or through exp-501, feat-clv-arpu-v1 and feat-clv-tenure.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
Two decisions rest on ds-ed-bureau-join: dec-ed-promote-v3 and dec-ed-gbm-for-watchlist. Both reach it through ed-gbm-v3 and the bureau-slope feature.
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
The note in force is sfc-hier-v3, which replaced sfc-lgbm-v2 after sfc-ets-v1 was superseded. It is built directly on sfc-lgbm-v2, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and exp-207.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/sfc-lgbm-v2.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/exp-207.md

## Q4
disp-lgbm-v1 rests on two dataset notes: the analyst labels (8,900 hand labels, 7,450 with two-analyst agreement) directly, and the dispute table cards.disputes through them.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Three decisions rest on ds-fsm-parity-sample: dec-fsm-cutover and dec-fsm-timezone-utc are the two in the chain. dec-fsm-cutover comes through exp-107 and fnd-parity-post-fix, and dec-fsm-timezone-utc through exp-102 and fnd-parity-pre-fix.
Notes: feature-store-migration/dec-fsm-cutover.md, feature-store-migration/dec-fsm-timezone-utc.md

## Q6
The note in force is txc-gbm-v3, which replaced txc-gbm-v2 after txc-logreg-v1 was superseded. It is built directly on txc-gbm-v2, feat-txc-descriptor-tokens-v2, feat-txc-normalise-v2 and feat-txc-mcc-prior.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/txc-gbm-v2.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/feat-txc-mcc-prior.md

## Q7
ed-gbm-v2 rests on two dataset notes: the current-account base and the 30+ DPD within 3 months label. It reaches them directly or through ed-gbm-v1, exp-205 and exp-206, and their features.
Notes: early-delinquency/ds-ed-current-base.md, early-delinquency/ds-ed-label-30p3m.md

## Q8
Five decisions rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25, dec-f26-promote-v3 and, in dispute-triage, dec-disp-fraud-score-in. The last one reaches it through the fraud26 score feeding dispute triage.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests on two dataset notes: the assignments table (4.2M units across 38 tests) and the test registry (38 tests with owners and planned metrics). It reaches them directly or through exp-507 and its two features.
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decisions rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default. They reach it through the matched-control experiments, hp-psm-v1 and hp-psm-v2, and the bureau-delta feature.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md