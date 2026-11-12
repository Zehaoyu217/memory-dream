## Q1
The only note in another project built directly on fraud26-gbm-v3 is dispute-triage's feature feat-disp-fraud-score. Inside fraud-2026, dec-f26-promote-v3 also rests on it directly, and more dispute-triage notes depend on it through that feature.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
Tracing churn-gbm-2025-v2 back to the start, it rests on four datasets: ds-c25-accounts-snapshot, ds-c25-app-engagement, ds-c25-oot-2024h1 and ds-c25-churn-labels. It reaches all of them through other notes, not directly.
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-oot-2024h1.md, churn-2025/ds-c25-churn-labels.md

## Q3
Both models build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1. feat-rdm-last-activity-v1 has since been replaced by feat-rdm-last-activity-v2.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
Only rdm-propensity-lr: it is still current and builds directly on feat-rdm-last-activity-v1, which feat-rdm-last-activity-v2 replaced. rdm-uplift-v1 does the same but is itself replaced. rdm-uplift-v2 rests directly on only one replaced note, exp-307, which is an experiment.
Notes: reactivation-dormant/rdm-propensity-lr.md

## Q5
Four decisions rest on ds-csb-churn-labels. dec-csb-90d-window builds on it directly. dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 reach it through other notes.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The line runs find-hp-naive-effect → find-hp-adjusted-effect → find-hp-effect-v2, so find-hp-effect-v2 is in force now (−4.7pp). It builds on exp-404, find-hp-adjusted-effect and "the propensity matching holdout experiment". The tool couldn't match that last phrase to a note, but the note's text and exp-408's content identify it as exp-408.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md, hardship-programs/find-hp-adjusted-effect.md

## Q7
The only note in another project built directly on inc-gbm-v3 is application-scorecard's feature feat-app-income-est. Other application-scorecard notes, including app-scorecard-v4, depend on it through that feature.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three datasets. It builds directly on ds-csb-churn-labels and ds-csb-oot-2025q1, and reaches ds-csb-biz-accounts through ds-csb-churn-labels.
Notes: churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q9
Both models build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj. trv-ridge-v3 also adds feat-trv-funnel-v2.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
Only ror-uplift-v1: it is still current and builds directly on feat-ror-value-band-v1, which feat-ror-value-band-v2 replaced. ror-roi-v1 is itself replaced, and ror-roi-v2 uses the current value band v2.
Notes: retention-offers-roi/ror-uplift-v1.md