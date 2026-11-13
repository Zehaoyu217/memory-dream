## Q1
rdm-propensity-lr and rdm-uplift-v1 both build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1.
Notes: work/rdm-propensity-lr.md, work/rdm-uplift-v1.md, work/feat-rdm-app-installed.md, work/feat-rdm-last-activity-v1.md

## Q2
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window directly, and dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 through other notes. Ninety other notes may also depend on it, but the memory does not confirm that, so I left them out.
Notes: work/ds-csb-churn-labels.md, work/dec-csb-90d-window.md, work/dec-csb-tenure-floor.md, work/dec-csb-ship-xgb-v1.md, work/dec-csb-ship-xgb-v2.md

## Q3
The line runs find-hp-naive-effect → find-hp-adjusted-effect → find-hp-effect-v2, so find-hp-effect-v2 is in force. It builds on exp-404-hardship-programs and find-hp-adjusted-effect, plus a propensity matching holdout experiment that its text names but no note links to; that is most likely exp-402-hardship-programs.
Notes: work/find-hp-effect-v2.md, work/exp-404-hardship-programs.md, work/find-hp-adjusted-effect.md, work/exp-402-hardship-programs.md

## Q4
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts through ds-csb-churn-labels and the two feature notes.
Notes: work/csb-lr-base.md, work/ds-csb-churn-labels.md, work/ds-csb-oot-2025q1.md, work/ds-csb-biz-accounts.md

## Q5
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: work/trv-ridge-v2.md, work/trv-ridge-v3.md, work/feat-trv-cross-border-share.md, work/feat-trv-seasonality-adj.md