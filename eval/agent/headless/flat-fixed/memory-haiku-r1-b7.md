## Q1
sfc-ets-v1 was replaced by sfc-lgbm-v2, which was replaced by sfc-hier-v3, the note in force now. sfc-hier-v3 is built on exp-207-spend-forecasting, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2.
Notes: work/sfc-ets-v1.md, work/sfc-lgbm-v2.md, work/sfc-hier-v3.md, work/exp-207-spend-forecasting.md, work/feat-sfc-active-accounts.md, work/fnd-sfc-q4-reconciled.md

## Q2
disp-lgbm-v1 rests on two dataset notes: ds-disp-analyst-labels directly, and ds-disp-disputes through it and feat-disp-reason-text.
Notes: work/ds-disp-analyst-labels.md, work/ds-disp-disputes.md

## Q3
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-cutover, and dec-fsm-timezone-utc (via exp-102 and fnd-parity-pre-fix, both built on exp-101).
Notes: work/dec-fsm-cutover.md, work/dec-fsm-timezone-utc.md

## Q4
txc-logreg-v1 was replaced by txc-gbm-v2, which was replaced by txc-gbm-v3, the note in force now. txc-gbm-v3 is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: work/txc-logreg-v1.md, work/txc-gbm-v2.md, work/txc-gbm-v3.md, work/feat-txc-descriptor-tokens-v2.md, work/feat-txc-mcc-prior.md, work/feat-txc-normalise-v2.md

## Q5
ed-gbm-v2 rests on two dataset notes, ds-ed-current-base and ds-ed-label-30p3m, both reached through its feature and experiment chain.
Notes: work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md

## Q6
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-replace-f25, dec-f26-promote-v3, and dec-disp-fraud-score-in (the last via the fraud-2026 score chain).
Notes: work/dec-f26-maturity-60d.md, work/dec-f26-promote-v2.md, work/dec-f26-replace-f25.md, work/dec-f26-promote-v3.md, work/dec-disp-fraud-score-in.md

## Q7
ep-uplift-forest-v1 rests on two dataset notes, ds-ep-assignments and ds-ep-test-registry, reached through exp-507-experiment-platform and its features.
Notes: work/ds-ep-assignments.md, work/ds-ep-test-registry.md

## Q8
Three decision notes rest on ds-hp-matched-controls: dec-hp-report-did, dec-hp-6mo-default and dec-hp-smd-gate.
Notes: work/dec-hp-report-did.md, work/dec-hp-6mo-default.md, work/dec-hp-smd-gate.md

## Q9
fsm-churn-xgb-v2 rests on two dataset notes: ds-fsm-legacy-features (via fsm-churn-xgb-v1 and the util-ratio feature) and ds-fsm-parity-sample (via exp-105, exp-107 and exp-101).
Notes: work/ds-fsm-legacy-features.md, work/ds-fsm-parity-sample.md

## Q10
Ten current models build directly on a feature that has since been replaced: bt-logit-baseline, cb-uplift-v1, churn-lr-base-2025, cli-logreg-baseline, clv-bgnbd-v1, csb-lr-base, inc-linear-baseline, mq3-response-gbm-v1, rdm-propensity-lr and ror-uplift-v1. The memory's model list marks each replaced input, and none of these models carries a SUPERSEDED marker. I did not open each feature note to confirm its replacement.
Notes: work/bt-logit-baseline.md, work/cb-uplift-v1.md, work/churn-lr-base-2025.md, work/cli-logreg-baseline.md, work/clv-bgnbd-v1.md, work/csb-lr-base.md, work/inc-linear-baseline.md, work/mq3-response-gbm-v1.md, work/rdm-propensity-lr.md, work/ror-uplift-v1.md