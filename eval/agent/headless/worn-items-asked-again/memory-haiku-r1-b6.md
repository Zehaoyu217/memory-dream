## Q1
The only note in another project built directly on fraud26-gbm-v3 is dispute-triage's feat-disp-fraud-score, which scores each dispute's original authorisation with that model.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
churn-gbm-2025-v2 rests on four dataset notes: ds-c25-accounts-snapshot, ds-c25-app-engagement, ds-c25-churn-labels and ds-c25-oot-2024h1. Some of these are reached only through other notes, not directly.
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-churn-labels.md, churn-2025/ds-c25-oot-2024h1.md

## Q3
Both models build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1. rdm-propensity-lr also uses balance band and prior response, but rdm-uplift-v1 does not list those as direct inputs.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
rdm-propensity-lr is still current (kept as the baseline, not superseded) and builds directly on feat-rdm-last-activity-v1, which was replaced by feat-rdm-last-activity-v2. rdm-uplift-v2 is the current targeting model, but its inputs are all current, so it does not qualify.
Notes: reactivation-dormant/rdm-propensity-lr.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q5
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window directly, and dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 through other notes.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The line ends at find-hp-effect-v2, the finding in force now (4.7pp, from exp-404 and the adjusted-effect lineage). It is built directly on exp-404, exp-408 and find-hp-adjusted-effect.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md, hardship-programs/find-hp-adjusted-effect.md

## Q7
Only one note in another project is built directly on inc-gbm-v3: application-scorecard's feat-app-income-est, which uses the live income estimate for applicant bands.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts through them.
Notes: churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q9
Both models build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 is still current and builds directly on feat-ror-value-band-v1, which was replaced by feat-ror-value-band-v2. The current ror-roi-v2 does not qualify, because its only replaced input is the model ror-roi-v1, not a feature or dataset.
Notes: retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/feat-ror-value-band-v1.md