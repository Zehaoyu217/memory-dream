## Q1
sfc-ets-v1 is superseded by sfc-lgbm-v2, which is superseded by sfc-hier-v3, the note in force. sfc-ets-v1 builds on ds-sfc-segment-monthly.
Notes: work/sfc-ets-v1.md, work/sfc-lgbm-v2.md, work/sfc-hier-v3.md, work/ds-sfc-segment-monthly.md

## Q2
disp-lgbm-v1 traces through dec-disp-labels-two-analyst back to the dataset roots ds-disp-analyst-labels and ds-disp-disputes.
Notes: work/disp-lgbm-v1.md, work/dec-disp-labels-two-analyst.md, work/ds-disp-analyst-labels.md, work/ds-disp-disputes.md

## Q3
No decision note rests directly on ds-fsm-parity-sample. Its direct consumers are q-fsm-parity-threshold, exp-101 and exp-107.
Notes: work/ds-fsm-parity-sample.md, work/q-fsm-parity-threshold.md, work/exp-101-feature-store-migration.md, work/exp-107-feature-store-migration.md

## Q4
txc-logreg-v1 leads to txc-gbm-v2, then txc-gbm-v3, which is current and shipped under dec-txc-ship-gbm-v3.
Notes: work/txc-logreg-v1.md, work/txc-gbm-v2.md, work/txc-gbm-v3.md, work/dec-txc-ship-gbm-v3.md

## Q5
ed-gbm-v2 traces back to the dataset roots ds-ed-current-base and ds-ed-label-30p3m. It is superseded by ed-gbm-v3.
Notes: work/ed-gbm-v2.md, work/ed-gbm-v3.md, work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md

## Q6
The decision notes resting on ds-f26-labels-2026 are dec-f26-replace-f25, dec-f26-maturity-60d, dec-f26-promote-v2 and dec-f26-promote-v3.
Notes: work/ds-f26-labels-2026.md, work/dec-f26-replace-f25.md, work/dec-f26-maturity-60d.md, work/dec-f26-promote-v2.md, work/dec-f26-promote-v3.md

## Q7
ep-uplift-forest-v1 traces back to the dataset roots ds-ep-test-registry and ds-ep-assignments.
Notes: work/ep-uplift-forest-v1.md, work/exp-507-experiment-platform.md, work/feat-ep-prior-logins-14d.md, work/feat-ep-tenure-months.md, work/ds-ep-test-registry.md, work/ds-ep-assignments.md

## Q8
The decision notes resting on ds-hp-matched-controls are dec-hp-6mo-default, dec-hp-report-did and dec-hp-smd-gate.
Notes: work/ds-hp-matched-controls.md, work/hp-psm-v1.md, work/hp-psm-v2.md, work/dec-hp-6mo-default.md, work/dec-hp-report-did.md, work/dec-hp-smd-gate.md

## Q9
fsm-churn-xgb-v2 traces back to the dataset roots ds-fsm-legacy-features and ds-fsm-parity-sample. ds-fsm-txn-source is not reached by its chain.
Notes: work/fsm-churn-xgb-v2.md, work/fsm-churn-xgb-v1.md, work/feat-fsm-util-ratio.md, work/feat-fsm-payment-lag-v2.md, work/exp-107-feature-store-migration.md, work/ds-fsm-legacy-features.md, work/ds-fsm-parity-sample.md

## Q10
cb-uplift-v1 is current and builds directly on feat-cb-spend-base, which is replaced by feat-cb-spend-band-v2. ror-uplift-v1 is current and builds directly on the first value band feature, feat-ror-value-band-v1, which is replaced by feat-ror-value-band-v2.
Notes: work/cb-uplift-v1.md, work/feat-cb-spend-base.md, work/feat-cb-spend-band-v2.md, work/ror-uplift-v1.md, work/feat-ror-value-band-v1.md, work/feat-ror-value-band-v2.md