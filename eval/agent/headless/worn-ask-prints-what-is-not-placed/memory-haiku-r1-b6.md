## Q1
The only note in another project built directly on fraud26-gbm-v3 is dispute-triage/feat-disp-fraud-score, which scores each dispute's authorisation with it. The dispute-triage decision dec-disp-fraud-score-in mentions the model as a dependency, but its "from" list does not name it, so I did not count it.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
churn-gbm-2025-v2 rests on four dataset notes: ds-c25-accounts-snapshot and ds-c25-oot-2024h1 are in its chain, and ds-c25-app-engagement and ds-c25-churn-labels come in through the earlier churn-gbm-2025 model and its experiments.
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-oot-2024h1.md, churn-2025/ds-c25-churn-labels.md

## Q3
Both models build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1. The other feature notes are on one model each, or on the other only through the shared chain.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
rdm-propensity-lr is still current, with no superseded marker, and it builds directly on feat-rdm-last-activity-v1, which was replaced by feat-rdm-last-activity-v2. rdm-uplift-v1 also uses that feature, but it has been superseded by rdm-uplift-v2, so it is not current.
Notes: reactivation-dormant/rdm-propensity-lr.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q5
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window directly, and dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 through the chain that runs via csb-lr-base, exp-201 and the XGBoost models.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The line runs find-hp-naive-effect → find-hp-adjusted-effect → find-hp-effect-v2, and find-hp-effect-v2 is the one in force. It is built directly on exp-404, exp-408 and find-hp-adjusted-effect.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md, hardship-programs/find-hp-adjusted-effect.md

## Q7
Only one note in another project is built directly on inc-gbm-v3: application-scorecard/feat-app-income-est, which takes the income band from it. The other notes that cite it are all inside income-estimation.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three dataset notes directly, ds-csb-churn-labels and ds-csb-oot-2025q1, and one through them, ds-csb-biz-accounts, which is the base population for the whole project.
Notes: churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q9
Both trv-ridge-v2 and trv-ridge-v3 build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj. trv-ridge-v3 also uses feat-trv-funnel-v2, which v2 does not.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 is the only current model that builds directly on a replaced feature or dataset note. It uses feat-ror-value-band-v1, which was replaced by feat-ror-value-band-v2. ror-roi-v2 is also current, but it builds on v2 of that feature.
Notes: retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/feat-ror-value-band-v1.md