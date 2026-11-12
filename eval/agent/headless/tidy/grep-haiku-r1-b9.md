## Q1
clv-bgnbd-v1 rests on three dataset notes: ds-clv-cohort-panel, ds-clv-revenue-monthly (via feat-clv-arpu-v1) and ds-clv-holdout-2021h1 (via exp-501).
Notes: customer-lanifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/exp-501.md, customer-lifetime-value/feat-clv-arpu-v1.md, customer-lifetime-value/feat-clv-tenure.md, customer-lifetime-value/ds-clv-revenue-monthly.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-cohort-panel.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3 (via feat-ed-bureau-slope-v1 and ed-gbm-v3) and dec-ed-gbm-for-watchlist (via ed-logit-v1, exp-201 and find-ed-gbm-vs-logit).
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md, early-delinquency/ed-gbm-v3.md, early-delinquency/feat-ed-bureau-slope-v1.md, early-delinquency/ed-logit-v1.md, early-delinquency/exp-201.md, early-delinquency/find-ed-gbm-vs-logit.md, early-delinquency/ds-ed-bureau-join.md

## Q3
sfc-hier-v3 is the note in force (sfc-ets-v1 was replaced by sfc-lgbm-v2, which was replaced by sfc-hier-v3). It is built on sfc-lgbm-v2, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and exp-207.
Notes: spend-forecasting/sfc-ets-v1.md, spend-forecasting/sfc-lgbm-v2.md, spend-forecasting/sfc-hier-v3.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/fnd-sfc-q4-reconciled.md, spend-forecasting/exp-207.md

## Q4
disp-lgbm-v1 rests on ds-disp-disputes and ds-disp-analyst-labels, directly or through feat-disp-reason-text, dec-disp-labels-two-analyst and q-disp-label-source.
Notes: dispute-triage/disp-lgbm-v1.md, dispute-triage/feat-disp-reason-text.md, dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/q-disp-label-source.md, dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-timezone-utc (via exp-101/exp-102 and via exp-107/fnd-parity-pre-fix) and dec-fsm-cutover (via fnd-parity-post-fix).
Notes: feature-store-migration/dec-fsm-timezone-utc.md, feature-store-migration/dec-fsm-cutover.md, feature-store-migration/exp-101.md, feature-store-migration/exp-102.md, feature-store-migration/exp-107.md, feature-store-migration/fnd-parity-pre-fix.md, feature-store-migration/fnd-parity-post-fix.md, feature-store-migration/ds-fsm-parity-sample.md

## Q6
txc-gbm-v3 is the note in force (txc-logreg-v1 was replaced by txc-gbm-v2, which was replaced by txc-gbm-v3). It is built on txc-gbm-v2, feat-txc-descriptor-tokens-v2, feat-txc-normalise-v2 and feat-txc-mcc-prior.
Notes: txn-categorization/txc-logreg-v1.md, txn-categorization/txc-gbm-v2.md, txn-categorization/txc-gbm-v3.md, txn-categorization/feat-txc-descriptor-tokens-v2.md, txn-categorization/feat-txc-normalise-v2.md, txn-categorization/feat-txc-mcc-prior.md

## Q7
ed-gbm-v2 rests on ds-ed-current-base and ds-ed-label-30p3m, through ed-gbm-v1, the feat-ed-* inputs and exp-205/exp-206.
Notes: early-delinquency/ed-gbm-v2.md, early-delinquency/ed-gbm-v1.md, early-delinquency/exp-205.md, early-delinquency/exp-206.md, early-delinquency/feat-ed-util-trend-v1.md, early-delinquency/feat-ed-cashadv-v1.md, early-delinquency/feat-ed-minpay-v2.md, early-delinquency/ds-ed-label-30p3m.md, early-delinquency/ds-ed-current-base.md

## Q8
Five decision notes rest on ds-f26-labels-2026: dec-f26-replace-f25, dec-f26-maturity-60d, dec-f26-promote-v2 and dec-f26-promote-v3 (all in fraud-2026), and dispute-triage's dec-disp-fraud-score-in, which reaches it through the fraud26-gbm chain.
Notes: fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/fraud26-gbm-v3.md, dispute-triage/feat-disp-fraud-score.md, fraud-2026/ds-f26-labels-2026.md

## Q9
ep-uplift-forest-v1 rests on ds-ep-assignments and ds-ep-test-registry, through feat-ep-tenure-months, feat-ep-prior-logins-14d and exp-507.
Notes: experiment-platform/ep-uplift-forest-v1.md, experiment-platform/exp-507.md, experiment-platform/feat-ep-tenure-months.md, experiment-platform/feat-ep-prior-logins-14d.md, experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-smd-gate, dec-hp-report-did and dec-hp-6mo-default, through the hp-psm chain, feat-hp-match-covars-v1, exp-404, exp-408, find-hp-effect-v2 and find-hp-plan-length.
Notes: hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-6mo-default.md, hardship-programs/hp-psm-v1.md, hardship-programs/hp-psm-v2.md, hardship-programs/feat-hp-match-covars-v1.md, hardship-programs/exp-404.md, hardship-programs/find-hp-effect-v2.md, hardship-programs/find-hp-plan-length.md, hardship-programs/ds-hp-matched-controls.md