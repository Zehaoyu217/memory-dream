## Q1
Only one note outside fraud-2026 is built directly on fraud26-gbm-v3: dispute-triage/feat-disp-fraud-score.md, which scores each dispute's authorisation with the model.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
churn-gbm-2025-v2 rests on four dataset notes: ds-c25-accounts-snapshot (directly through its features and the models behind it), ds-c25-app-engagement, ds-c25-oot-2024h1 and ds-c25-churn-labels. The last three reach it through other notes in the chain.
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-oot-2024h1.md, churn-2025/ds-c25-churn-labels.md

## Q3
Both rdm-propensity-lr and rdm-uplift-v1 build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
rdm-propensity-lr is the only current model that builds directly on a replaced feature: it uses feat-rdm-last-activity-v1, which was replaced by v2 in June 2025. rdm-uplift-v2, the current targeting model, uses only current features.
Notes: reactivation-dormant/rdm-propensity-lr.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q5
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window and dec-csb-tenure-floor directly or through the LR baseline and experiments, and dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 through the XGBoost models.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The note in force is find-hp-effect-v2 (hardship enrolment reduces the 30-to-60 roll by 4.7pp). It is built on exp-404, exp-408 and find-hp-adjusted-effect.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md, hardship-programs/find-hp-adjusted-effect.md

## Q7
Only one note of another project is built directly on inc-gbm-v3: application-scorecard/feat-app-income-est.md, which uses its income band.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three dataset notes directly: ds-csb-churn-labels, ds-csb-oot-2025q1 and ds-csb-biz-accounts, which is also the root of the chain.
Notes: churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q9
Both trv-ridge-v2 and trv-ridge-v3 build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 is the only current model that builds directly on a replaced feature: it uses feat-ror-value-band-v1, which was superseded by feat-ror-value-band-v2. ror-roi-v2, the current ROI model, uses only current features.
Notes: retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/feat-ror-value-band-v1.md