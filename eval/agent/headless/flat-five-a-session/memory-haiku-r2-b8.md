## Q1
Both rdm-propensity-lr and rdm-uplift-v1 build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1.
Notes: work/feat-rdm-app-installed.md, work/feat-rdm-last-activity-v1.md

## Q2
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window directly, and dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 through other notes built on it.
Notes: work/dec-csb-90d-window.md, work/dec-csb-tenure-floor.md, work/dec-csb-ship-xgb-v1.md, work/dec-csb-ship-xgb-v2.md

## Q3
The note in force now is find-hp-effect-v2 (4.7pp reduction in the 30-to-60 roll). It builds on find-hp-adjusted-effect and exp-404-hardship-programs, and on a propensity matching holdout experiment that the memory does not link to a note; that is most likely exp-402-hardship-programs, the source of find-hp-adjusted-effect, but this is unconfirmed.
Notes: work/find-hp-effect-v2.md, work/find-hp-adjusted-effect.md, work/exp-404-hardship-programs.md

## Q4
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts through ds-csb-churn-labels, which is the start of the chain.
Notes: work/ds-csb-churn-labels.md, work/ds-csb-oot-2025q1.md, work/ds-csb-biz-accounts.md

## Q5
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: work/feat-trv-cross-border-share.md, work/feat-trv-seasonality-adj.md