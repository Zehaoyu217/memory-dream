## Q1
One note in another project was built directly on fraud26-gbm-v3: the feature feat-disp-fraud-score in dispute-triage.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
Through every note churn-gbm-2025-v2 rests on, it reaches three datasets. They are ds-c25-accounts-snapshot (through the feature notes), ds-c25-churn-labels (through dec-c25-label-60d, exp-101 and fnd-c25-90d-feedback-lag) and ds-c25-app-engagement (through q-c25-app-lift and the app-lift findings).
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-churn-labels.md, churn-2025/ds-c25-app-engagement.md

## Q3
Both models build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1. feat-rdm-last-activity-v1 has since been replaced by v2.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
Two current models qualify: rdm-propensity-lr and rdm-uplift-v1. Neither has been replaced, and both still build directly on feat-rdm-last-activity-v1, which feat-rdm-last-activity-v2 replaced. rdm-uplift-v2 uses v2, so it does not qualify.
Notes: reactivation-dormant/rdm-propensity-lr.md, reactivation-dormant/rdm-uplift-v1.md

## Q5
Four decision notes rest on ds-csb-churn-labels. dec-csb-90d-window builds on it directly. dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 reach it through csb-lr-base and the experiments built on it.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The line runs find-hp-naive-effect → find-hp-adjusted-effect → find-hp-effect-v2, so find-hp-effect-v2 is in force now (a 4.7pp reduction in the 30-to-60 roll). It is built on exp-404, exp-408 and find-hp-adjusted-effect, which it replaced.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md, hardship-programs/find-hp-adjusted-effect.md

## Q7
One note in another project was built directly on inc-gbm-v3: the feature feat-app-income-est in application-scorecard.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests directly on the datasets ds-csb-churn-labels and ds-csb-oot-2025q1. Through those notes and its features, it also rests on ds-csb-biz-accounts.
Notes: churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q9
Both models build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj. Only trv-ridge-v3 adds feat-trv-funnel-v2.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
One model qualifies: ror-uplift-v1. It is still current and builds directly on feat-ror-value-band-v1, which feat-ror-value-band-v2 replaced. ror-roi-v2 uses value band v2, and ror-roi-v1 has been replaced, so neither counts.
Notes: retention-offers-roi/ror-uplift-v1.md