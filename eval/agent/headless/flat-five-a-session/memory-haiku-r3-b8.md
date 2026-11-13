## Q1
Both `rdm-propensity-lr` and `rdm-uplift-v1` build directly on `feat-rdm-app-installed` (app installed flag) and `feat-rdm-last-activity-v1` (months since last activity, v1).
Notes: work/feat-rdm-app-installed.md, work/feat-rdm-last-activity-v1.md, work/rdm-propensity-lr.md, work/rdm-uplift-v1.md

## Q2
Four decision notes rest on `ds-csb-churn-labels`: `dec-csb-90d-window` directly, and `dec-csb-tenure-floor`, `dec-csb-ship-xgb-v1` and `dec-csb-ship-xgb-v2` through other notes built on it. About 90 other notes have a builds-on link the memory could not match, so one of them could be a missed decision; I grepped the decision notes for churn-label mentions and found no others.
Notes: work/ds-csb-churn-labels.md, work/dec-csb-90d-window.md, work/dec-csb-tenure-floor.md, work/dec-csb-ship-xgb-v1.md, work/dec-csb-ship-xgb-v2.md

## Q3
The note in force is `find-hp-effect-v2`, the current 4.7pp hardship effect. It builds on `exp-404-hardship-programs` (difference-in-differences) and on `find-hp-adjusted-effect`, which was itself superseded. Its text also names "the propensity matching holdout experiment", which I matched by reading to `exp-402-hardship-programs` (the 6.1pp matched estimate), since the memory did not link it.
Notes: work/find-hp-effect-v2.md, work/exp-404-hardship-programs.md, work/find-hp-adjusted-effect.md, work/exp-402-hardship-programs.md

## Q4
`csb-lr-base` rests on three dataset notes: `ds-csb-churn-labels` and `ds-csb-oot-2025q1` directly, and `ds-csb-biz-accounts` through the churn labels and the spend and tenure features. `ds-csb-biz-accounts` has no upstream note, so that is the start of the chain.
Notes: work/csb-lr-base.md, work/ds-csb-churn-labels.md, work/ds-csb-oot-2025q1.md, work/ds-csb-biz-accounts.md

## Q5
`trv-ridge-v2` and `trv-ridge-v3` both build directly on `feat-trv-cross-border-share` (monthly cross-border share of travel spend) and `feat-trv-seasonality-adj` (STL seasonal component removed).
Notes: work/feat-trv-cross-border-share.md, work/feat-trv-seasonality-adj.md, work/trv-ridge-v2.md, work/trv-ridge-v3.md