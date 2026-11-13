## Q1
The dataset notes under clv-bgnbd-v1 are ds-clv-cohort-panel, ds-clv-holdout-2021h1 and ds-clv-revenue-monthly, reached directly or through exp-501, feat-clv-arpu-v1 and feat-clv-tenure. One link in its text, "the bg/nbd versus gbm accuracy test", has no note of its own, so the chain may be incomplete.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3, which rests on ed-gbm-v3 and feat-ed-bureau-slope-v1, and dec-ed-gbm-for-watchlist, which rests on ed-gbm-v3 and exp-207.
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
The note in force at the end of the sfc-ets-v1 line is sfc-hier-v3, which replaced sfc-lgbm-v2. sfc-hier-v3 is built directly on exp-207, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2. The older chain runs through sfc-lgbm-v2 to feat-sfc-cpi-lag6, feat-sfc-lags-v1, feat-sfc-season-v2 and sfc-ets-v1.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/sfc-lgbm-v2.md, spend-forecasting/exp-207.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/fnd-sfc-q4-reconciled.md

## Q4
The dataset notes under disp-lgbm-v1 are ds-disp-analyst-labels and ds-disp-disputes. The first is direct, and the second is reached through the two-analyst label decision and q-disp-label-source.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-timezone-utc, which rests on exp-102 and the pre-fix finding, and dec-fsm-cutover, which is reached through the chain of the parity experiments.
Notes: feature-store-migration/dec-fsm-timezone-utc.md, feature-store-migration/dec-fsm-cutover.md

## Q6
The note in force is txc-gbm-v3, which replaced txc-gbm-v2 and so the end of the txc-logreg-v1 line. txc-gbm-v3 is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
The chain gives ds-ed-current-base as the dataset under ed-gbm-v2. ed-gbm-v2 also uses feat-ed-minpay-v2 as a feature, and that note builds on ds-ed-label-30p3m. The link to ds-ed-label-30p3m is stated in the notes' text but not recorded as a chain link, so it is reached by my reading of the text.
Notes: early-delinquency/ds-ed-current-base.md, early-delinquency/ds-ed-label-30p3m.md, early-delinquency/feat-ed-minpay-v2.md

## Q8
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25 and dec-f26-promote-v3 in fraud-2026, and dispute-triage/dec-disp-fraud-score-in, which reaches it through fraud26-gbm-v3.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
The dataset notes under ep-uplift-forest-v1 are ds-ep-assignments and ds-ep-test-registry. The first is reached through feat-ep-tenure-months and feat-ep-prior-logins-14d, and the second through exp-507.
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default. The chain also names find-hp-effect-v2 as a possible further link, but that is a finding, not a decision.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md