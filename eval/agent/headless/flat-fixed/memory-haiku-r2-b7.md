## Q1
sfc-hier-v3 is the note in force at the end of the sfc-ets-v1 → sfc-lgbm-v2 → sfc-hier-v3 line. It builds directly on exp-207-spend-forecasting, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2.
Notes: work/sfc-hier-v3.md, work/exp-207-spend-forecasting.md, work/feat-sfc-active-accounts.md, work/fnd-sfc-q4-reconciled.md, work/sfc-lgbm-v2.md

## Q2
disp-lgbm-v1 rests on two dataset notes: ds-disp-analyst-labels directly, and ds-disp-disputes through it.
Notes: work/ds-disp-analyst-labels.md, work/ds-disp-disputes.md

## Q3
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-cutover, via fsm-churn-xgb-v2, and dec-fsm-timezone-utc, via exp-102-feature-store-migration.
Notes: work/dec-fsm-cutover.md, work/dec-fsm-timezone-utc.md

## Q4
txc-gbm-v3 is the note in force at the end of the txc-logreg-v1 → txc-gbm-v2 → txc-gbm-v3 line. It builds directly on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: work/txc-gbm-v3.md, work/feat-txc-descriptor-tokens-v2.md, work/feat-txc-mcc-prior.md, work/feat-txc-normalise-v2.md, work/txc-gbm-v2.md

## Q5
ed-gbm-v2 rests on two dataset notes: ds-ed-current-base, via the cash-advance and utilisation-trend features, and ds-ed-label-30p3m, via the min-pay feature.
Notes: work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md

## Q6
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25 and dec-f26-promote-v3 through the fraud26 models, and dec-disp-fraud-score-in through feat-disp-fraud-score.
Notes: work/dec-f26-maturity-60d.md, work/dec-f26-promote-v2.md, work/dec-f26-replace-f25.md, work/dec-f26-promote-v3.md, work/dec-disp-fraud-score-in.md

## Q7
ep-uplift-forest-v1 rests on two dataset notes: ds-ep-assignments and ds-ep-test-registry, both through exp-507-experiment-platform and its features.
Notes: work/ds-ep-assignments.md, work/ds-ep-test-registry.md

## Q8
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-6mo-default and dec-hp-smd-gate, all through the hardship experiments and models.
Notes: work/dec-hp-report-did.md, work/dec-hp-6mo-default.md, work/dec-hp-smd-gate.md

## Q9
fsm-churn-xgb-v2 rests on two dataset notes: ds-fsm-legacy-features, through feat-fsm-util-ratio and the migration experiments, and ds-fsm-parity-sample, through exp-101 and exp-107.
Notes: work/ds-fsm-legacy-features.md, work/ds-fsm-parity-sample.md

## Q10
Ten current model notes build directly on a feature that has since been replaced: bt-logit-baseline (feat-bt-util-3m), cb-uplift-v1 (feat-cb-spend-base), churn-lr-base-2025 (feat-c25-util-v1), cli-logreg-baseline (feat-cli-util-v1), clv-bgnbd-v1 (feat-clv-arpu-v1), csb-lr-base (feat-csb-spend-raw), inc-linear-baseline (feat-inc-payroll-cadence-v1), mq3-response-gbm-v1 (feat-mq3-recency-v1), rdm-propensity-lr (feat-rdm-last-activity-v1) and ror-uplift-v1 (feat-ror-value-band-v1). No current model builds directly on a replaced dataset.
Notes: work/bt-logit-baseline.md, work/cb-uplift-v1.md, work/churn-lr-base-2025.md, work/cli-logreg-baseline.md, work/clv-bgnbd-v1.md, work/csb-lr-base.md, work/inc-linear-baseline.md, work/mq3-response-gbm-v1.md, work/rdm-propensity-lr.md, work/ror-uplift-v1.md