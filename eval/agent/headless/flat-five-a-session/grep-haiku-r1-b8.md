## Q1
Both rdm-propensity-lr and rdm-uplift-v1 build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1. rdm-uplift-v1 also builds on rdm-propensity-lr, which is a model, not a feature.
Notes: work/rdm-propensity-lr.md, work/rdm-uplift-v1.md, work/feat-rdm-app-installed.md, work/feat-rdm-last-activity-v1.md

## Q2
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window (directly), and dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 (through csb-lr-base, fnd-csb-tenure-cut and the csb-xgb models built on them).
Notes: work/dec-csb-90d-window.md, work/dec-csb-tenure-floor.md, work/dec-csb-ship-xgb-v1.md, work/dec-csb-ship-xgb-v2.md

## Q3
The note in force at the end of the find-hp-naive-effect line is find-hp-effect-v2 (-4.7pp). It is built on exp-404-hardship-programs (the difference-in-differences experiment), exp-408-hardship-programs (the propensity matching holdout experiment) and find-hp-adjusted-effect.
Notes: work/find-hp-naive-effect.md, work/find-hp-adjusted-effect.md, work/find-hp-effect-v2.md, work/exp-404-hardship-programs.md, work/exp-408-hardship-programs.md

## Q4
csb-lr-base rests on three dataset notes directly, ds-csb-churn-labels and ds-csb-oot-2025q1 and, through its feature notes, ds-csb-biz-accounts. ds-csb-biz-accounts is the root and builds on no other dataset.
Notes: work/csb-lr-base.md, work/ds-csb-churn-labels.md, work/ds-csb-oot-2025q1.md, work/ds-csb-biz-accounts.md, work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q5
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: work/trv-ridge-v2.md, work/trv-ridge-v3.md, work/feat-trv-cross-border-share.md, work/feat-trv-seasonality-adj.md