## Q1
The notes that clv-bgnbd-v1 rests on, directly or through others, are three dataset notes: the cohort panel, the 2021 H1 holdout and the monthly revenue set.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3, which promoted ed-gbm-v3, and dec-ed-gbm-for-watchlist, which that promotion superseded but which still rests on the join.
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
sfc-ets-v1 was replaced by sfc-lgbm-v2, which was replaced by sfc-hier-v3, the note in force now. sfc-hier-v3 is built on exp-207, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/sfc-lgbm-v2.md

## Q4
disp-lgbm-v1 rests on two dataset notes: the analyst-labels set directly, and the full disputes table through the labels decision and the label-source question.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Five decision notes rest on ds-fsm-parity-sample: dec-fsm-cutover and dec-fsm-timezone-utc, plus the decision chain they sit in. Only dec-fsm-cutover and dec-fsm-timezone-utc are decision notes in that chain.
Notes: feature-store-migration/dec-fsm-cutover.md, feature-store-migration/dec-fsm-timezone-utc.md

## Q6
txc-logreg-v1 was replaced by txc-gbm-v2, which was replaced by txc-gbm-v3, the note in force now. txc-gbm-v3 is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
ed-gbm-v2 rests on two dataset notes: the current-account base, through ed-gbm-v1 and the cash-advance and utilisation-trend features, and the 30+ within 3 months label, through the min-pay feature. The min-pay link was not matched by the tool, so I checked it by reading ed-gbm-v2 and feat-ed-minpay-v2.
Notes: early-delinquency/ds-ed-current-base.md, early-delinquency/ds-ed-label-30p3m.md

## Q8
Five decision notes rest on ds-f26-labels-2026: four in fraud-2026 (the 60-day maturity rule, the v2 promotion, the replacement of the fraud-2025 model, and the v3 promotion), and the dispute-triage decision to add the fraud score.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests on two dataset notes: the assignments table and the test registry, both reached through exp-507 and the feature notes.
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: the difference-in-differences reporting decision, the standardised-mean-difference gate, and the six-month default plan length.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md