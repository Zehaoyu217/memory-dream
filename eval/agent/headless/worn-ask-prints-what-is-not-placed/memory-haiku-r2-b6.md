## Q1
The only note from another project built directly on fraud26-gbm-v3 is dispute-triage/feat-disp-fraud-score, which scores each dispute's authorisation with the model.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
churn-gbm-2025-v2 rests on four dataset notes: ds-c25-accounts-snapshot, ds-c25-app-engagement, ds-c25-churn-labels and ds-c25-oot-2024h1.
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-churn-labels.md, churn-2025/ds-c25-oot-2024h1.md

## Q3
rdm-propensity-lr and rdm-uplift-v1 both build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
rdm-propensity-lr is still current (it is kept as the baseline) and builds directly on feat-rdm-last-activity-v1, which was replaced by feat-rdm-last-activity-v2. rdm-uplift-v2 is current too, but all its inputs are current.
Notes: reactivation-dormant/rdm-propensity-lr.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q5
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window directly, and dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 through other notes.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The note in force now is find-hp-effect-v2 (hardship enrolment cuts the 30-to-60 roll by 4.7pp). It is built on exp-404, exp-408 and find-hp-adjusted-effect.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md, hardship-programs/find-hp-adjusted-effect.md

## Q7
The only note from another project built directly on inc-gbm-v3 is application-scorecard/feat-app-income-est, which uses the live income estimate as an applicant band.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts through them.
Notes: churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q9
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 is the only current model that builds directly on a replaced feature: it uses feat-ror-value-band-v1, which feat-ror-value-band-v2 replaced. The other current model, ror-roi-v2, uses only current features.
Notes: retention-offers-roi/ror-uplift-v1.md