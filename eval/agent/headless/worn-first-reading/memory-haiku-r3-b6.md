## Q1
Only `dispute-triage/feat-disp-fraud-score` is built directly on fraud26-gbm-v3 from another project. `dispute-triage/dec-disp-fraud-score-in` records a dependency on the model, not a build link.
Notes: dispute-triage/feat-disp-fraud-score.md, dispute-triage/dec-disp-fraud-score-in.md, fraud-2026/fraud26-gbm-v3.md

## Q2
churn-gbm-2025-v2 rests on three dataset notes: ds-c25-accounts-snapshot, ds-c25-app-engagement and ds-c25-churn-labels.
Notes: churn-2025/churn-gbm-2025-v2.md, churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-churn-labels.md

## Q3
Both rdm-propensity-lr and rdm-uplift-v1 build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1.
Notes: reactivation-dormant/rdm-propensity-lr.md, reactivation-dormant/rdm-uplift-v1.md, reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
rdm-propensity-lr is the only current model that builds directly on a replaced feature, feat-rdm-last-activity-v1, which is now superseded by feat-rdm-last-activity-v2. It is still kept as the baseline. rdm-uplift-v2 is current but uses only current inputs, and rdm-uplift-v1 also uses the replaced feature but has been replaced itself.
Notes: reactivation-dormant/rdm-propensity-lr.md, reactivation-dormant/feat-rdm-last-activity-v1.md, reactivation-dormant/feat-rdm-last-activity-v2.md, reactivation-dormant/rdm-uplift-v2.md

## Q5
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window and dec-csb-tenure-floor directly through their inputs, and dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 through the csb-xgb models and experiments that were built on it.
Notes: churn-small-business/ds-csb-churn-labels.md, churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The current finding is find-hp-effect-v2, which reports a 4.7pp reduction in the 30-to-60 roll. It is built on exp-404, exp-408 and find-hp-adjusted-effect.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/find-hp-naive-effect.md, hardship-programs/find-hp-adjusted-effect.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md

## Q7
Only application-scorecard/feat-app-income-est builds directly on inc-gbm-v3 from another project. It uses the live income estimate for the applicant income band.
Notes: application-scorecard/feat-app-income-est.md, income-estimation/inc-gbm-v3.md

## Q8
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts through the feature notes.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q9
Both trv-ridge-v2 and trv-ridge-v3 build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: travel-spend-recovery/trv-ridge-v2.md, travel-spend-recovery/trv-ridge-v3.md, travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 is the only current model that builds directly on a replaced feature, feat-ror-value-band-v1, which feat-ror-value-band-v2 superseded. It still feeds the current ror-roi-v2 model.
Notes: retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/feat-ror-value-band-v1.md, retention-offers-roi/feat-ror-value-band-v2.md, retention-offers-roi/ror-roi-v2.md