## Q1
Only one note of another project is built directly on fraud26-gbm-v3: dispute-triage/feat-disp-fraud-score, which scores each dispute's authorisation with the model.
Notes: fraud-2026/fraud26-gbm-v3.md, dispute-triage/feat-disp-fraud-score.md

## Q2
churn-gbm-2025-v2 rests on four dataset notes: ds-c25-accounts-snapshot and ds-c25-oot-2024h1 (both through other notes), and ds-c25-app-engagement and ds-c25-churn-labels (also through other notes). None of them is a direct input.
Notes: churn-2025/churn-gbm-2025-v2.md, churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-oot-2024h1.md, churn-2025/ds-c25-churn-labels.md

## Q3
rdm-propensity-lr and rdm-uplift-v1 both build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1. The other feature inputs (balance band, prior response) feed only rdm-propensity-lr.
Notes: reactivation-dormant/rdm-propensity-lr.md, reactivation-dormant/rdm-uplift-v1.md, reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
rdm-propensity-lr is the one still-current model that builds directly on a replaced feature, feat-rdm-last-activity-v1 (now superseded by feat-rdm-last-activity-v2). rdm-uplift-v2 is current but uses only live features and notes.
Notes: reactivation-dormant/rdm-propensity-lr.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q5
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window directly, and dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 through other notes.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The note in force is find-hp-effect-v2, a finding that the 30-to-60 roll effect is -4.7pp. It is built directly on exp-404, exp-408 and find-hp-adjusted-effect.
Notes: hardship-programs/find-hp-naive-effect.md, hardship-programs/find-hp-adjusted-effect.md, hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md

## Q7
Only one note of another project is built directly on inc-gbm-v3: application-scorecard/feat-app-income-est, the income band feature for applicants.
Notes: income-estimation/inc-gbm-v3.md, application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts through them and feat-csb-spend-raw.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q9
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: travel-spend-recovery/trv-ridge-v2.md, travel-spend-recovery/trv-ridge-v3.md, travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 is still current and builds directly on feat-ror-value-band-v1, which has been replaced by feat-ror-value-band-v2. ror-roi-v2 is current, but its replaced input is a model (ror-roi-v1), not a feature or dataset.
Notes: retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/feat-ror-value-band-v1.md