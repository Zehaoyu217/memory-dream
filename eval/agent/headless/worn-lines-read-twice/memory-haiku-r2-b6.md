## Q1
The only note from another project built directly on fraud26-gbm-v3 is dispute-triage/feat-disp-fraud-score, which scores each dispute's authorisation with that model.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
churn-gbm-2025-v2 rests on four dataset notes: ds-c25-accounts-snapshot, ds-c25-app-engagement, ds-c25-oot-2024h1 and ds-c25-churn-labels. The first two are reached directly or through its feature and experiment chain, and the others through its label and holdout chain.
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-oot-2024h1.md, churn-2025/ds-c25-churn-labels.md

## Q3
Both models build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1. The v1 last-activity feature has since been replaced by v2.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
rdm-propensity-lr is the only current model that builds directly on a replaced note. It uses feat-rdm-last-activity-v1, which has been superseded by feat-rdm-last-activity-v2. The current rdm-uplift-v2 uses only v2 and the other live features.
Notes: reactivation-dormant/rdm-propensity-lr.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q5
Four decision notes rest on ds-csb-churn-labels, either directly or through the models and experiments built on it: dec-csb-90d-window, dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The note in force at the end of the line is find-hp-effect-v2, which sets the current hardship effect at -4.7pp. It builds on exp-404 (the difference-in-differences experiment), find-hp-adjusted-effect, and exp-408 (the propensity matching holdout experiment, which its text cites by content rather than by id).
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/find-hp-adjusted-effect.md, hardship-programs/exp-408.md

## Q7
Only one note from another project is built directly on inc-gbm-v3: application-scorecard/feat-app-income-est, the live income band feature for applicants.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts through them, since it is the base population for both.
Notes: churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q9
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 is the only current model that builds directly on a replaced note. It uses feat-ror-value-band-v1, which feat-ror-value-band-v2 replaced. ror-roi-v2 is current but builds on the replaced model ror-roi-v1, not on a feature or dataset.
Notes: retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/feat-ror-value-band-v1.md