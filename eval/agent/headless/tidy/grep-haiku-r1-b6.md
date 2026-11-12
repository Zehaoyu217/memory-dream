## Q1
Only one note from another project builds directly on fraud26-gbm-v3: dispute-triage's feat-disp-fraud-score. The dispute decision dec-disp-fraud-score-in depends on it only through that feature.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
churn-gbm-2025-v2 rests on four dataset notes, reached directly or through its feature, experiment and finding parents: ds-c25-accounts-snapshot, ds-c25-churn-labels, ds-c25-oot-2024h1 and ds-c25-app-engagement.
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-churn-labels.md, churn-2025/ds-c25-oot-2024h1.md, churn-2025/ds-c25-app-engagement.md

## Q3
Both rdm-propensity-lr and rdm-uplift-v1 build directly on feat-rdm-last-activity-v1 and feat-rdm-app-installed.
Notes: reactivation-dormant/feat-rdm-last-activity-v1.md, reactivation-dormant/feat-rdm-app-installed.md

## Q4
rdm-propensity-lr is still current and builds directly on feat-rdm-last-activity-v1, which feat-rdm-last-activity-v2 has replaced.
Notes: reactivation-dormant/rdm-propensity-lr.md, reactivation-dormant/feat-rdm-last-activity-v1.md, reactivation-dormant/feat-rdm-last-activity-v2.md

## Q5
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window directly, and dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 through csb-lr-base, csb-xgb-v1 and csb-xgb-v2.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The line ends at find-hp-effect-v2, which is current. It is built on exp-408, find-hp-adjusted-effect and exp-404; the earlier link, find-hp-adjusted-effect, was built on find-hp-naive-effect.
Notes: hardship-programs/find-hp-naive-effect.md, hardship-programs/find-hp-adjusted-effect.md, hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-408.md, hardship-programs/exp-404.md

## Q7
Only one note from another project builds directly on inc-gbm-v3: application-scorecard's feat-app-income-est.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three dataset notes: ds-csb-biz-accounts, ds-csb-churn-labels and ds-csb-oot-2025q1. The first two are reached through the feature and dataset parents.
Notes: churn-small-business/ds-csb-biz-accounts.md, churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md

## Q9
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 is still current and builds directly on feat-ror-value-band-v1, which feat-ror-value-band-v2 has replaced. The other current model, ror-roi-v2, builds only on the current v2 feature.
Notes: retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/feat-ror-value-band-v1.md, retention-offers-roi/feat-ror-value-band-v2.md