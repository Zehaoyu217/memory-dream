## Q1
Three dataset notes: ds-clv-cohort-panel, ds-clv-holdout-2021h1 and ds-clv-revenue-monthly, reached through exp-501, feat-clv-arpu-v1 and feat-clv-tenure. One note names a "bg/nbd versus gbm accuracy test" that has no note of its own, so this chain may be incomplete.
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/exp-501.md, customer-lifetime-value/feat-clv-arpu-v1.md, customer-lifetime-value/feat-clv-tenure.md, customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
Two decisions rest on ds-ed-bureau-join: dec-ed-promote-v3 and dec-ed-gbm-for-watchlist. They reach it through ed-logit-v1, feat-ed-bureau-slope-v1 and ed-gbm-v3.
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
The note in force at the end of the line is sfc-hier-v3 (sfc-ets-v1 was replaced by sfc-lgbm-v2, which was replaced by sfc-hier-v3). sfc-hier-v3 is built directly on sfc-lgbm-v2, exp-207, feat-sfc-active-accounts and fnd-sfc-q4-reconciled.
Notes: spend-forecasting/sfc-hier-v3.md, spend-forecasting/sfc-lgbm-v2.md, spend-forecasting/exp-207.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/fnd-sfc-q4-reconciled.md

## Q4
Two dataset notes: ds-disp-analyst-labels (direct) and ds-disp-disputes (through dec-disp-labels-two-analyst and ds-disp-analyst-labels).
Notes: dispute-triage/disp-lgbm-v1.md, dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decisions rest on ds-fsm-parity-sample: dec-fsm-timezone-utc (via exp-102 and fnd-parity-pre-fix) and dec-fsm-cutover (via fnd-parity-post-fix).
Notes: feature-store-migration/dec-fsm-timezone-utc.md, feature-store-migration/dec-fsm-cutover.md

## Q6
The note in force at the end of the line is txc-gbm-v3 (txc-logreg-v1 was replaced by txc-gbm-v2, which was replaced by txc-gbm-v3). txc-gbm-v3 is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/txc-gbm-v2.md

## Q7
Two dataset notes: ds-ed-current-base (via ed-gbm-v1, feat-ed-cashadv-v1 and feat-ed-util-trend-v1) and ds-ed-label-30p3m (via feat-ed-minpay-v2, which ed-gbm-v2 lists as a feature). The link from ed-gbm-v2 to feat-ed-minpay-v2 is stated in ed-gbm-v2's own text, not as a recorded link.
Notes: early-delinquency/ed-gbm-v2.md, early-delinquency/ed-gbm-v1.md, early-delinquency/feat-ed-cashadv-v1.md, early-delinquency/feat-ed-util-trend-v1.md, early-delinquency/feat-ed-minpay-v2.md, early-delinquency/ds-ed-current-base.md, early-delinquency/ds-ed-label-30p3m.md

## Q8
Five decisions rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25, dec-f26-promote-v3 and, in dispute-triage, dec-disp-fraud-score-in.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
Two dataset notes: ds-ep-assignments and ds-ep-test-registry, reached through exp-507, feat-ep-prior-logins-14d and feat-ep-tenure-months.
Notes: experiment-platform/ep-uplift-forest-v1.md, experiment-platform/exp-507.md, experiment-platform/feat-ep-prior-logins-14d.md, experiment-platform/feat-ep-tenure-months.md, experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decisions rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default. One finding, find-hp-effect-v2, may also rest on it, but that link is not recorded.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md