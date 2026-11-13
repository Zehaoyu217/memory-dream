## Q1
Both `rdm-propensity-lr` and `rdm-uplift-v1` build directly on `feat-rdm-app-installed` and `feat-rdm-last-activity-v1`.
Notes: work/rdm-propensity-lr.md, work/rdm-uplift-v1.md, work/feat-rdm-app-installed.md, work/feat-rdm-last-activity-v1.md

## Q2
Four decision notes rest on `ds-csb-churn-labels`: `dec-csb-90d-window` directly, and `dec-csb-tenure-floor`, `dec-csb-ship-xgb-v1` and `dec-csb-ship-xgb-v2` through `fnd-csb-tenure-cut`, `csb-xgb-v1` and `csb-xgb-v2`.
Notes: work/ds-csb-churn-labels.md, work/dec-csb-90d-window.md, work/dec-csb-tenure-floor.md, work/dec-csb-ship-xgb-v1.md, work/dec-csb-ship-xgb-v2.md, work/fnd-csb-tenure-cut.md, work/csb-xgb-v1.md, work/csb-xgb-v2.md

## Q3
The note in force is `find-hp-effect-v2` (hardship enrolment lowers the 30-to-60 roll by 4.7pp). It is built on `exp-404-hardship-programs` (difference-in-differences), `exp-408-hardship-programs` (propensity matching holdout) and `find-hp-adjusted-effect`, the note it replaced. That note had replaced `find-hp-naive-effect`.
Notes: work/find-hp-naive-effect.md, work/find-hp-adjusted-effect.md, work/find-hp-effect-v2.md, work/exp-404-hardship-programs.md, work/exp-408-hardship-programs.md

## Q4
`csb-lr-base` rests on three dataset notes: `ds-csb-biz-accounts` at the root, plus `ds-csb-churn-labels` and `ds-csb-oot-2025q1`, which both build on it. It also uses the features `feat-csb-spend-raw` and `feat-csb-tenure-band`, which build on the same root.
Notes: work/csb-lr-base.md, work/ds-csb-biz-accounts.md, work/ds-csb-churn-labels.md, work/ds-csb-oot-2025q1.md, work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q5
Both `trv-ridge-v2` and `trv-ridge-v3` build directly on `feat-trv-cross-border-share` and `feat-trv-seasonality-adj`.
Notes: work/trv-ridge-v2.md, work/trv-ridge-v3.md, work/feat-trv-cross-border-share.md, work/feat-trv-seasonality-adj.md