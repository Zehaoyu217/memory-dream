## Q1
Through the two features, clv-bgnbd-v1 rests on ds-clv-cohort-panel and ds-clv-revenue-monthly. It also rests on ds-clv-holdout-2021h1 through exp-501, the BG/NBD versus GBM accuracy test its text names but the graph does not link.
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/feat-clv-arpu-v1.md, customer-lifetime-value/feat-clv-tenure.md, customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-revenue-monthly.md, customer-lifetime-value/exp-501.md, customer-lifetime-value/ds-clv-holdout-2021h1.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3 and dec-ed-gbm-for-watchlist, both reached through ed-gbm-v3 and feat-ed-bureau-slope-v1.
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
sfc-hier-v3 is the note in force at the end of the sfc-ets-v1 → sfc-lgbm-v2 → sfc-hier-v3 line. It is built directly on exp-207, fnd-sfc-q4-reconciled, feat-sfc-active-accounts and sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/sfc-lgbm-v2.md

## Q4
disp-lgbm-v1 rests on ds-disp-analyst-labels directly and on ds-disp-disputes through it and the label-source question.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-cutover and dec-fsm-timezone-utc, the latter through fnd-parity-pre-fix and exp-102.
Notes: feature-store-migration/dec-fsm-cutover.md, feature-store-migration/dec-fsm-timezone-utc.md

## Q6
txc-gbm-v3 is the model in force at the end of the txc-logreg-v1 → txc-gbm-v2 → txc-gbm-v3 line. It is built directly on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
ed-gbm-v2 rests on ds-ed-current-base through ed-gbm-v1. Its text also names feat-ed-minpay-v2, which the graph does not link, and that feature rests on ds-ed-label-30p3m.
Notes: early-delinquency/ds-ed-current-base.md, early-delinquency/ds-ed-label-30p3m.md, early-delinquency/feat-ed-minpay-v2.md

## Q8
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25 and dec-f26-promote-v3 in fraud-2026, and dec-disp-fraud-score-in in dispute-triage, reached through the fraud26 models and feat-disp-fraud-score.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests on ds-ep-assignments and ds-ep-test-registry, reached through exp-507 and the two features.
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default, reached through hp-psm-v1, hp-psm-v2 and the matching experiments.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md