## Q1
Only one note outside fraud-2026 is built directly on fraud26-gbm-v3: dispute-triage/feat-disp-fraud-score, which takes the model's score for each dispute's authorisation. The other outside notes (dec-disp-fraud-score-in, disp-lgbm-v3, exp-307, exp-308) reach it only through that feature.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
churn-gbm-2025-v2 rests on four dataset notes: ds-c25-accounts-snapshot, ds-c25-app-engagement, ds-c25-churn-labels and ds-c25-oot-2024h1. None is a direct input; all four are reached through its features, experiments and decisions.
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-churn-labels.md, churn-2025/ds-c25-oot-2024h1.md

## Q3
Both build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1. The second is now superseded by feat-rdm-last-activity-v2.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
Only rdm-propensity-lr. It has no superseded marker and builds directly on feat-rdm-last-activity-v1, which was replaced by feat-rdm-last-activity-v2. The current rdm-uplift-v2 uses only current features.
Notes: reactivation-dormant/rdm-propensity-lr.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q5
Four decision notes rest on ds-csb-churn-labels. dec-csb-90d-window is direct; dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 come through the csb-lr-base and csb-xgb chain.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The note in force is find-hp-effect-v2 (4.7pp). It builds on exp-404 (difference-in-differences), find-hp-adjusted-effect (itself replaced) and exp-408, which I matched to the "propensity matching holdout experiment" by name since no explicit link was recorded.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/find-hp-adjusted-effect.md, hardship-programs/exp-408.md

## Q7
Only application-scorecard/feat-app-income-est, the income-band feature for applicants, is built directly on inc-gbm-v3.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts through them and through its spend and tenure features.
Notes: churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q9
Both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 is the only current model that does this. It has no superseded marker, still feeds ror-roi-v2, and builds directly on feat-ror-value-band-v1, which was replaced by feat-ror-value-band-v2.
Notes: retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/feat-ror-value-band-v1.md