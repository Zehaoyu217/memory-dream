## Q1
clv-bgnbd-v1 rests on two feature notes, feat-clv-arpu-v1 and feat-clv-tenure. Those trace back to two dataset notes: ds-clv-cohort-panel and ds-clv-revenue-monthly.
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/feat-clv-arpu-v1.md, customer-lifetime-value/feat-clv-tenure.md, customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3, which promotes ed-gbm-v3, and dec-ed-gbm-for-watchlist, which was superseded by dec-ed-promote-v3. Both get there through ed-gbm-v3, feat-ed-bureau-slope-v1 and ed-logit-v1.
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
The note in force now is sfc-hier-v3, since sfc-ets-v1 was replaced by sfc-lgbm-v2 and sfc-lgbm-v2 was replaced by sfc-hier-v3. sfc-hier-v3 is built directly on exp-207, fnd-sfc-q4-reconciled, feat-sfc-active-accounts and sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/sfc-ets-v1.md, spend-forecasting/sfc-lgbm-v2.md, spend-forecasting/exp-207.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/feat-sfc-active-accounts.md

## Q4
disp-lgbm-v1 rests on two dataset notes: ds-disp-analyst-labels directly, and ds-disp-disputes through it and through feat-disp-reason-text.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-timezone-utc, which is built on exp-102 and fnd-parity-pre-fix, and dec-fsm-cutover. Both trace back through exp-101 or exp-107 to the parity sample.
Notes: feature-store-migration/dec-fsm-timezone-utc.md, feature-store-migration/dec-fsm-cutover.md

## Q6
The note in force now is txc-gbm-v3, since txc-logreg-v1 was replaced by txc-gbm-v2 and txc-gbm-v2 was replaced by txc-gbm-v3. txc-gbm-v3 is built directly on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/txc-logreg-v1.md, txn-categorization/txc-gbm-v2.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md

## Q7
ed-gbm-v2 is built directly on ed-gbm-v1. Through that it rests on feat-ed-cashadv-v1, feat-ed-util-trend-v1 and ds-ed-current-base, so the only dataset note is ds-ed-current-base.
Notes: early-delinquency/ed-gbm-v2.md, early-delinquency/ds-ed-current-base.md

## Q8
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25, dec-f26-promote-v3, and dispute-triage/dec-disp-fraud-score-in. The last one reaches the dataset through feat-disp-fraud-score, which is built on fraud26-gbm-v3.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests on two dataset notes: ds-ep-assignments and ds-ep-test-registry. It reaches them through exp-507, feat-ep-prior-logins-14d and feat-ep-tenure-months.
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default. They reach the dataset through matching experiments and models such as exp-402, hp-psm-v1 and hp-psm-v2.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md