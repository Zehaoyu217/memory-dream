## Q1
clv-bgnbd-v1 rests directly on exp-501, feat-clv-arpu-v1 and feat-clv-tenure, and through them on three datasets: ds-clv-cohort-panel, ds-clv-holdout-2021h1 and ds-clv-revenue-monthly.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q2
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3 (directly through ed-gbm-v3 and exp-207) and dec-ed-gbm-for-watchlist (through ed-logit-v1 and feat-ed-bureau-slope-v1). One other early-delinquency note, feat-ed-minpay-v2, has an unmatched link that may point at this dataset, but it is a feature, not a decision.
Notes: early-delinquency/dec-ed-promote-v3.md, early-delinquency/dec-ed-gbm-for-watchlist.md

## Q3
The line runs sfc-ets-v1 → sfc-lgbm-v2 → sfc-hier-v3, so sfc-hier-v3 is the note in force. It is built on exp-207, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2.
Notes: spend-forecasting/sfc-hier-v3.md

## Q4
disp-lgbm-v1 rests directly on dec-disp-labels-two-analyst, ds-disp-analyst-labels and feat-disp-reason-text, and through them on ds-disp-disputes and q-disp-label-source. The dataset notes are ds-disp-analyst-labels and ds-disp-disputes.
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/ds-disp-disputes.md

## Q5
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-cutover (through exp-101 and exp-107) and dec-fsm-timezone-utc (through exp-102 and exp-107).
Notes: feature-store-migration/dec-fsm-cutover.md, feature-store-migration/dec-fsm-timezone-utc.md

## Q6
The line runs txc-logreg-v1 → txc-gbm-v2 → txc-gbm-v3, so txc-gbm-v3 is in force. It is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: txn-categorization/txc-gbm-v3.md

## Q7
ed-gbm-v2 rests directly on ed-gbm-v1, and through ed-gbm-v1 and its features on the dataset ds-ed-current-base. The memory does not link ed-gbm-v2 to ds-ed-label-30p3m, though exp-206 uses feat-ed-minpay-v2, which comes from that label dataset, so that link is worth checking.
Notes: early-delinquency/ds-ed-current-base.md

## Q8
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25 and dec-f26-promote-v3 in fraud-2026, and dec-disp-fraud-score-in in dispute-triage, which reaches it through the fraud-2026 score.
Notes: fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
ep-uplift-forest-v1 rests directly on exp-507, feat-ep-prior-logins-14d and feat-ep-tenure-months, and through them on ds-ep-assignments and ds-ep-test-registry.
Notes: experiment-platform/ds-ep-assignments.md, experiment-platform/ds-ep-test-registry.md

## Q10
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-smd-gate and dec-hp-6mo-default.
Notes: hardship-programs/dec-hp-report-did.md, hardship-programs/dec-hp-smd-gate.md, hardship-programs/dec-hp-6mo-default.md