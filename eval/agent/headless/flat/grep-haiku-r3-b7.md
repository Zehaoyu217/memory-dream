## Q1
sfc-hier-v3 is the segment forecast in force. It builds on sfc-lgbm-v2, which replaced sfc-ets-v1, and on the MinT reconciliation experiment, the active-accounts feature, and fnd-sfc-q4-reconciled, which trace back to the monthly segment spend dataset.
Notes: work/sfc-hier-v3.md, work/sfc-lgbm-v2.md, work/sfc-ets-v1.md, work/exp-207-spend-forecasting.md, work/feat-sfc-active-accounts.md, work/fnd-sfc-q4-reconciled.md, work/ds-sfc-segment-monthly.md

## Q2
disp-lgbm-v1 rests on ds-disp-analyst-labels, which builds on ds-disp-disputes, and on feat-disp-reason-text, which also builds on ds-disp-disputes. The decision dec-disp-labels-two-analyst sits on the same analyst-label dataset.
Notes: work/disp-lgbm-v1.md, work/dec-disp-labels-two-analyst.md, work/ds-disp-analyst-labels.md, work/feat-disp-reason-text.md, work/ds-disp-disputes.md

## Q3
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-timezone-utc, via exp-102 and exp-101, and dec-fsm-cutover, via fnd-parity-post-fix and dec-fsm-timezone-utc. dec-fsm-naming-rule does not depend on the parity sample.
Notes: work/ds-fsm-parity-sample.md, work/exp-101-feature-store-migration.md, work/exp-102-feature-store-migration.md, work/dec-fsm-timezone-utc.md, work/fnd-parity-post-fix.md, work/dec-fsm-cutover.md

## Q4
txc-gbm-v3 is the model in force; it replaced txc-gbm-v2, which replaced txc-logreg-v1. Its inputs are feat-txc-descriptor-tokens-v2 (built on feat-txc-normalise-v2 and the descriptor sample), feat-txc-mcc-prior (built on the MCC crosswalk), and txc-gbm-v2 (built on feat-txc-descriptor-tokens-v1 and the labelled-merchants dataset). The dataset endpoints are ds-txc-descriptor-sample, ds-txc-labelled-merchants and ds-txc-mcc-crosswalk.
Notes: work/txc-gbm-v3.md, work/txc-gbm-v2.md, work/txc-logreg-v1.md, work/feat-txc-descriptor-tokens-v2.md, work/feat-txc-normalise-v2.md, work/feat-txc-mcc-prior.md, work/feat-txc-descriptor-tokens-v1.md, work/ds-txc-descriptor-sample.md, work/ds-txc-labelled-merchants.md, work/ds-txc-mcc-crosswalk.md

## Q5
ed-gbm-v2 traces to ds-ed-current-base through feat-ed-util-trend-v1 and feat-ed-cashadv-v1 (via ed-gbm-v1), and to ds-ed-label-30p3m through feat-ed-minpay-v2, which builds on the current-account population. ed-gbm-v3 has since replaced it, and the bureau-join dataset enters only through v3.
Notes: work/ed-gbm-v2.md, work/ed-gbm-v1.md, work/feat-ed-util-trend-v1.md, work/feat-ed-cashadv-v1.md, work/feat-ed-minpay-v2.md, work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md

## Q6
Four decision notes rest on ds-f26-labels-2026: dec-f26-maturity-60d, dec-f26-promote-v2, dec-f26-promote-v3 and dec-f26-replace-f25. The last one reaches it through fraud26-gbm-v1, which is a direct referrer. exp-208 is referenced in dec-f26-promote-v3 but is not on disk, so I could not check it.
Notes: work/ds-f26-labels-2026.md, work/dec-f26-maturity-60d.md, work/dec-f26-promote-v2.md, work/dec-f26-promote-v3.md, work/dec-f26-replace-f25.md, work/fraud26-gbm-v1.md, work/fraud26-gbm-v2.md, work/fraud26-gbm-v3.md

## Q7
ep-uplift-forest-v1 rests on ds-ep-test-registry, through exp-507-experiment-platform, and on ds-ep-assignments, through feat-ep-prior-logins-14d and feat-ep-tenure-months.
Notes: work/ep-uplift-forest-v1.md, work/exp-507-experiment-platform.md, work/feat-ep-prior-logins-14d.md, work/feat-ep-tenure-months.md, work/ds-ep-assignments.md, work/ds-ep-test-registry.md

## Q8
Three decision notes rest on ds-hp-matched-controls. dec-hp-report-did builds on exp-404 and dec-hp-smd-gate builds on exp-408, which runs on the first matching model hp-psm-v1, so both depend on it. dec-hp-6mo-default depends on it through exp-405 (plan length), which also uses hp-psm-v1.
Notes: work/ds-hp-matched-controls.md, work/hp-psm-v1.md, work/exp-402-hardship-programs.md, work/exp-404-hardship-programs.md, work/feat-hp-match-covars-v1.md, work/q-hp-effect-size.md, work/dec-hp-report-did.md, work/dec-hp-smd-gate.md, work/dec-hp-6mo-default.md, work/find-hp-plan-length.md

## Q9
fsm-churn-xgb-v2 traces to ds-fsm-legacy-features through the legacy churn model and feat-fsm-util-ratio, and to ds-fsm-parity-sample through exp-107, which feeds feat-fsm-util-ratio.
Notes: work/fsm-churn-xgb-v2.md, work/fsm-churn-xgb-v1.md, work/exp-105-feature-store-migration.md, work/feat-fsm-util-ratio.md, work/exp-107-feature-store-migration.md, work/ds-fsm-legacy-features.md, work/ds-fsm-parity-sample.md

## Q10
Three current baselines with no superseded line still build on a feature that was later replaced: cli-logreg-baseline uses feat-cli-util-v1 (replaced by v2), rdm-propensity-lr uses feat-rdm-last-activity-v1 (replaced by v2), and csb-lr-base uses feat-csb-spend-raw (replaced by feat-csb-spend-sa-v2). The current tree models I checked (sfc-hier-v3, txc-gbm-v3, ed-gbm-v3, fraud26-gbm-v3, fsm-churn-xgb-v2, csb-xgb-v2) use the newer features. Whether the three baselines still count as current is a judgement call, since nothing marks them superseded.
Notes: work/cli-logreg-baseline.md, work/feat-cli-util-v1.md, work/rdm-propensity-lr.md, work/feat-rdm-last-activity-v1.md, work/csb-lr-base.md, work/feat-csb-spend-raw.md