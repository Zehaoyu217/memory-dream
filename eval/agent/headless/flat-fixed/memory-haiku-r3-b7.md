## Q1
sfc-ets-v1 was replaced by sfc-lgbm-v2, which was replaced by sfc-hier-v3, the note in force now. sfc-hier-v3 is built on sfc-lgbm-v2, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and exp-207-spend-forecasting, and those rest on the monthly segment spend dataset ds-sfc-segment-monthly.
Notes: work/sfc-hier-v3.md, work/sfc-lgbm-v2.md, work/sfc-ets-v1.md, work/feat-sfc-active-accounts.md, work/fnd-sfc-q4-reconciled.md, work/exp-207-spend-forecasting.md

## Q2
disp-lgbm-v1 rests on two dataset notes: ds-disp-analyst-labels directly, and ds-disp-disputes through it.
Notes: work/ds-disp-analyst-labels.md, work/ds-disp-disputes.md

## Q3
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-cutover, through fsm-churn-xgb-v2 and fnd-parity-post-fix, and dec-fsm-timezone-utc, through exp-102-feature-store-migration.
Notes: work/dec-fsm-cutover.md, work/dec-fsm-timezone-utc.md

## Q4
txc-logreg-v1 was replaced by txc-gbm-v2, which was replaced by txc-gbm-v3, the note in force now. txc-gbm-v3 is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: work/txc-gbm-v3.md, work/txc-gbm-v2.md, work/txc-logreg-v1.md, work/feat-txc-descriptor-tokens-v2.md, work/feat-txc-mcc-prior.md, work/feat-txc-normalise-v2.md

## Q5
ed-gbm-v2 rests on two dataset notes: ds-ed-current-base and ds-ed-label-30p3m, both reached through its features and experiments.
Notes: work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md

## Q6
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25 and dec-f26-promote-v3 through the fraud-2026 model chain, and dec-disp-fraud-score-in through feat-disp-fraud-score and fraud26-gbm-v3.
Notes: work/dec-f26-maturity-60d.md, work/dec-f26-promote-v2.md, work/dec-f26-replace-f25.md, work/dec-f26-promote-v3.md, work/dec-disp-fraud-score-in.md

## Q7
ep-uplift-forest-v1 rests on two dataset notes: ds-ep-assignments and ds-ep-test-registry, both reached through its features and exp-507-experiment-platform.
Notes: work/ds-ep-assignments.md, work/ds-ep-test-registry.md

## Q8
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-6mo-default and dec-hp-smd-gate, all through the hardship propensity-matching models and experiments.
Notes: work/dec-hp-report-did.md, work/dec-hp-6mo-default.md, work/dec-hp-smd-gate.md

## Q9
fsm-churn-xgb-v2 rests on two dataset notes: ds-fsm-legacy-features directly through its features and fsm-churn-xgb-v1, and ds-fsm-parity-sample through exp-101-feature-store-migration. The tool's output also mixed in the unrelated churn-xgb-v2 chain, which I excluded.
Notes: work/ds-fsm-legacy-features.md, work/ds-fsm-parity-sample.md

## Q10
Ten current model notes build directly on a feature that has since been replaced: cb-uplift-v1 (feat-cb-spend-base), churn-lr-base-2025 (feat-c25-util-v1), csb-lr-base (feat-csb-spend-raw), cli-logreg-baseline (feat-cli-util-v1), clv-bgnbd-v1 (feat-clv-arpu-v1), bt-logit-baseline (feat-bt-util-3m), rdm-propensity-lr (feat-rdm-last-activity-v1), ror-uplift-v1 (feat-ror-value-band-v1), inc-linear-baseline (feat-inc-payroll-cadence-v1) and mq3-response-gbm-v1 (feat-mq3-recency-v1). This comes from the model list's "(replaced)" markers and I did not open each note; no current model was found building on a replaced dataset.
Notes: work/cb-uplift-v1.md, work/churn-lr-base-2025.md, work/csb-lr-base.md, work/cli-logreg-baseline.md, work/clv-bgnbd-v1.md, work/bt-logit-baseline.md, work/rdm-propensity-lr.md, work/ror-uplift-v1.md, work/inc-linear-baseline.md, work/mq3-response-gbm-v1.md