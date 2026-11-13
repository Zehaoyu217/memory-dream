## Q1
Both build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1. rdm-uplift-v1 also builds on rdm-propensity-lr, which is not a feature.
Notes: work/feat-rdm-app-installed.md, work/feat-rdm-last-activity-v1.md

## Q2
Four decision notes rest on ds-csb-churn-labels. dec-csb-90d-window uses it directly. dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 reach it through csb-lr-base, exp-202, exp-203, csb-xgb-v1 and csb-xgb-v2.
Notes: work/dec-csb-90d-window.md, work/dec-csb-tenure-floor.md, work/dec-csb-ship-xgb-v1.md, work/dec-csb-ship-xgb-v2.md

## Q3
The note in force is find-hp-effect-v2, which gives a -4.7pp effect on the 30-to-60 roll. It builds on exp-404-hardship-programs (difference-in-differences), exp-408-hardship-programs (propensity matching holdout) and find-hp-adjusted-effect.
Notes: work/find-hp-effect-v2.md, work/exp-404-hardship-programs.md, work/exp-408-hardship-programs.md, work/find-hp-adjusted-effect.md

## Q4
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts beneath both of them (and beneath its feature inputs).
Notes: work/ds-csb-churn-labels.md, work/ds-csb-oot-2025q1.md, work/ds-csb-biz-accounts.md

## Q5
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: work/feat-trv-cross-border-share.md, work/feat-trv-seasonality-adj.md