## Q1
Four decision notes rest on ds-f26-labels-2026: dec-f26-replace-f25 (through fraud26-gbm-v1), dec-f26-maturity-60d (through the label-bias and label-lag questions), dec-f26-promote-v2 (through feat-f26-mcc-risk and exp-206-fraud-2026), and dec-f26-promote-v3 (through dec-f26-promote-v2).
Notes: memory/work/ds-f26-labels-2026.md, memory/work/feat-f26-mcc-risk.md, memory/work/exp-206-fraud-2026.md, memory/work/dec-f26-maturity-60d.md, memory/work/dec-f26-promote-v2.md, memory/work/dec-f26-promote-v3.md, memory/work/dec-f26-replace-f25.md

## Q2
ep-uplift-forest-v1 rests on ds-ep-test-registry, through exp-507-experiment-platform, and on ds-ep-assignments, through feat-ep-prior-logins-14d and feat-ep-tenure-months.
Notes: memory/work/ep-uplift-forest-v1.md, memory/work/exp-507-experiment-platform.md, memory/work/feat-ep-prior-logins-14d.md, memory/work/feat-ep-tenure-months.md, memory/work/ds-ep-test-registry.md, memory/work/ds-ep-assignments.md

## Q3
Three decision notes rest on ds-hp-matched-controls: dec-hp-6mo-default, dec-hp-report-did and dec-hp-smd-gate.
Notes: memory/work/dec-hp-6mo-default.md, memory/work/dec-hp-report-did.md, memory/work/dec-hp-smd-gate.md, memory/work/ds-hp-matched-controls.md

## Q4
fsm-churn-xgb-v2 rests on ds-fsm-legacy-features, through feat-fsm-util-ratio and the legacy churn model that fsm-churn-xgb-v1 was built on.
Notes: memory/work/fsm-churn-xgb-v2.md, memory/work/feat-fsm-util-ratio.md, memory/work/fsm-churn-xgb-v1.md, memory/work/ds-fsm-legacy-features.md

## Q5
Four current model notes build directly on a replaced feature: bt-logit-baseline on feat-bt-util-3m, cb-uplift-v1 on feat-cb-spend-base, cli-logreg-baseline on feat-cli-util-v1, and csb-lr-base on feat-csb-spend-raw. Other models that build on replaced notes (ae-score-v1, bt-xgb-v1, cb-elasticity-v1, cld-gbm-v2, cli-xgb-v1, cr-lgbm-v1, csb-xgb-v1, ep-cuped-v1, fraud25-gbm-v1) are themselves superseded, and ep-cuped-v2, fsm-churn-xgb-v2, fsm-spend-lgbm-v2 and fraud26-gbm-v3 build on current versions.
Notes: memory/work/bt-logit-baseline.md, memory/work/feat-bt-util-3m.md, memory/work/cb-uplift-v1.md, memory/work/feat-cb-spend-base.md, memory/work/cli-logreg-baseline.md, memory/work/feat-cli-util-v1.md, memory/work/csb-lr-base.md, memory/work/feat-csb-spend-raw.md