## Q1
clv-bgnbd-v1 rests on three dataset notes: the cohort panel (ds-clv-cohort-panel), the 2021 H1 holdout (ds-clv-holdout-2021h1), and monthly revenue (ds-clv-revenue-monthly). It reaches them through exp-501, feat-clv-arpu-v1 and feat-clv-tenure.
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3 and dec-ed-gbm-for-watchlist. The first comes through feat-ed-bureau-slope-v1 and ed-gbm-v3, and the second through ed-logit-v1 and feat-ed-bureau-slope-v1.
Notes: early-delinquency/ds-ed-bureau-join.md, early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
The line runs sfc-ets-v1, then sfc-lgbm-v2, then sfc-hier-v3, which is the note in force now. sfc-hier-v3 is built on exp-207, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/sfc-lgbm-v2.md

## Q4
disp-lgbm-v1 rests on two dataset notes: ds-disp-analyst-labels directly, and ds-disp-disputes through it.
Notes: dispute-triage/disp-lgbm-v1.md, dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-timezone-utc, which comes through exp-102 and exp-101, and dec-fsm-cutover, which the index lists among the notes resting on it.
Notes: feature-store-migration/ds-fsm-parity-sample.md, feature-store-migration/dec-fsm-timezone-utc.md, feature-store-migration/dec-fsm-cutover.md

## Q6
The line runs txc-logreg-v1, then txc-gbm-v2, then txc-gbm-v3, which is the note in force now. txc-gbm-v3 is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/txc-logreg-v1.md, txn-categorization/txc-gbm-v2.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md

## Q7
ed-gbm-v2 rests on two dataset notes. ds-ed-current-base comes through ed-gbm-v1 and the cash-advance and utilisation-trend features. ds-ed-label-30p3m comes through feat-ed-minpay-v2, which the chain missed because the ed-gbm-v2 note names that feature only in its text. I found that link by reading ed-gbm-v2.md and feat-ed-minpay-v2.md.
Notes: early-delinquency/ed-gbm-v2.md, early-delinquency/ds-ed-current-base.md, early-delinquency/ds-ed-label-30p3m.md, early-delinquency/feat-ed-minpay-v2.md

## Q8
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25 and dec-f26-promote-v3 in fraud-2026, and dec-disp-fraud-score-in in dispute-triage, which reaches it through feat-disp-fraud-score.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests on two dataset notes: ds-ep-assignments and ds-ep-test-registry, both reached through exp-507 and the feature notes.
Notes: experiment-platform/ep-uplift-forest-v1.md, experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default. All three come through the matched-control experiments and the hp-psm models.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md