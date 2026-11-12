## Q1
clv-bgnbd-v1 rests on three dataset notes: ds-clv-cohort-panel, ds-clv-holdout-2021h1 and ds-clv-revenue-monthly. It reaches them through exp-501, feat-clv-arpu-v1, feat-clv-tenure and q-clv-model-choice. The tool reported one unmatched link, "the bg/nbd versus gbm accuracy test", and that is exp-501, which is already in the chain.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
Two decision notes rest on ds-ed-bureau-join, both indirectly: dec-ed-gbm-for-watchlist and dec-ed-promote-v3. dec-ed-promote-v3 replaced dec-ed-gbm-for-watchlist and is the one in force.
Notes: early-delinquency/dec-ed-gbm-for-watchlist.md, early-delinquency/dec-ed-promote-v3.md

## Q3
The line runs sfc-ets-v1 → sfc-lgbm-v2 → sfc-hier-v3, so sfc-hier-v3 is in force now. It is built on exp-207, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/sfc-lgbm-v2.md

## Q4
disp-lgbm-v1 rests on two dataset notes: ds-disp-analyst-labels, which it uses directly, and ds-disp-disputes, which it reaches through other notes. The chain also includes dec-disp-labels-two-analyst, feat-disp-reason-text and q-disp-label-source.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample, both indirectly: dec-fsm-cutover and dec-fsm-timezone-utc.
Notes: feature-store-migration/dec-fsm-cutover.md, feature-store-migration/dec-fsm-timezone-utc.md

## Q6
The line runs txc-logreg-v1 → txc-gbm-v2 → txc-gbm-v3, so txc-gbm-v3 is in force now. It is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
ed-gbm-v2 rests on one dataset note, ds-early-delinquency's ds-ed-current-base. It reaches it through ed-gbm-v1, feat-ed-cashadv-v1 and feat-ed-util-trend-v1.
Notes: early-delinquency/ds-ed-current-base.md

## Q8
Five decision notes rest on ds-f26-labels-2026, all indirectly: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25 and dec-f26-promote-v3 in fraud-2026, and dec-disp-fraud-score-in in dispute-triage.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests on two dataset notes: ds-ep-assignments and ds-ep-test-registry. It reaches them through exp-507, feat-ep-prior-logins-14d and feat-ep-tenure-months.
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls, all indirectly: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md