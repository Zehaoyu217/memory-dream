## Q1
Five decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-promote-v3, dec-f26-replace-f25 and dec-disp-fraud-score-in. dec-f26-promote-v2 is itself superseded by v3, but it still rests on the dataset.
Notes: work/dec-f26-maturity-60d.md, work/dec-f26-promote-v2.md, work/dec-f26-promote-v3.md, work/dec-f26-replace-f25.md, work/dec-disp-fraud-score-in.md

## Q2
ep-uplift-forest-v1 rests on two dataset notes, directly and through exp-507-experiment-platform and the feature notes: ds-ep-test-registry and ds-ep-assignments.
Notes: work/ds-ep-test-registry.md, work/ds-ep-assignments.md

## Q3
Three decision notes rest on ds-hp-matched-controls: dec-hp-6mo-default, dec-hp-report-did and dec-hp-smd-gate. They reach it through the hp-psm chain (hp-psm-v1, hp-psm-v2 and the exp-40x notes).
Notes: work/dec-hp-6mo-default.md, work/dec-hp-report-did.md, work/dec-hp-smd-gate.md

## Q4
fsm-churn-xgb-v2 rests on ds-fsm-legacy-features, through feat-fsm-util-ratio. That is the legacy features dataset (ml.legacy_feats_v1, 214 features, 18.4M account-months).
Notes: work/ds-fsm-legacy-features.md, work/feat-fsm-util-ratio.md, work/fsm-churn-xgb-v2.md

## Q5
Six current model notes build on feature notes that have since been replaced: cb-uplift-v1 (feat-cb-spend-base), csb-lr-base (feat-csb-spend-raw), rdm-propensity-lr (feat-rdm-last-activity-v1), cli-logreg-baseline (feat-cli-util-v1), bt-logit-baseline (feat-bt-util-3m) and churn-lr-base-2025 (pre-correction utilisation and holdout definitions, a judgement call). Excluded: fsm-churn-xgb-v2 (its inputs are current), and rdm-uplift-v1 and churn-gbm-2025 (both superseded by their v2 notes).
Notes: work/cb-uplift-v1.md, work/csb-lr-base.md, work/rdm-propensity-lr.md, work/cli-logreg-baseline.md, work/bt-logit-baseline.md, work/churn-lr-base-2025.md