## Q1
The only note of another project built directly on fraud26-gbm-v3 is dispute-triage/feat-disp-fraud-score, which scores each dispute's authorisation with that model. The fraud-2026 listing shows no other outside dependents of that model.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
churn-gbm-2025-v2 rests on four dataset notes: ds-c25-accounts-snapshot, ds-c25-app-engagement, ds-c25-oot-2024h1 and ds-c25-churn-labels. Some reach it only through the decision, experiment and feature notes it builds on directly.
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-oot-2024h1.md, churn-2025/ds-c25-churn-labels.md

## Q3
rdm-propensity-lr and rdm-uplift-v1 both build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1. The feat-rdm-balance-band note says it is used by uplift-v1, but uplift-v1's own build links do not include it, so I have left it out.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
rdm-propensity-lr is the only current model that builds directly on a replaced feature, feat-rdm-last-activity-v1 (replaced by v2). It is current because no note marks it superseded. rdm-uplift-v1 also uses that feature but is superseded, and rdm-uplift-v2 uses only the current v2 feature.
Notes: reactivation-dormant/rdm-propensity-lr.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q5
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window directly, and dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 through the notes they build on.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The note in force at the end of the line is find-hp-effect-v2, which builds on the difference-in-differences experiment exp-404 and on find-hp-adjusted-effect. Its text also cites a "propensity matching holdout experiment" that no note is linked to; exp-408 is the likely match, but that link is my inference.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/find-hp-adjusted-effect.md, hardship-programs/exp-408.md

## Q7
The only note of another project built directly on inc-gbm-v3 is application-scorecard/feat-app-income-est, which uses the live income estimate as an applicant feature.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts through them.
Notes: churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q9
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 is the only current model that builds directly on a replaced feature, feat-ror-value-band-v1 (replaced by v2). It is current because no note marks it superseded. ror-roi-v1 is also replaced and is excluded, and ror-roi-v2 builds only on the current v2 feature.
Notes: retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/feat-ror-value-band-v1.md