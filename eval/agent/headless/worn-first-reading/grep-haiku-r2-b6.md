## Q1
Only one note from another project builds directly on fraud26-gbm-v3: dispute-triage's feat-disp-fraud-score, whose "Builds on" line names fraud-2026/fraud26-gbm-v3. dec-disp-fraud-score-in only creates a dependency on it; its own "Builds on" line names exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
churn-gbm-2025-v2 rests on four dataset notes: ds-c25-accounts-snapshot, ds-c25-app-engagement, ds-c25-churn-labels and ds-c25-oot-2024h1. The last two come through exp-101 (label window) and churn-lr-base-2025 (the 2024 holdout), which feed dec-c25-label-60d and churn-gbm-2025 (v1).
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-churn-labels.md, churn-2025/ds-c25-oot-2024h1.md

## Q3
rdm-propensity-lr and rdm-uplift-v1 both build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
rdm-propensity-lr is still current and builds directly on feat-rdm-last-activity-v1, which feat-rdm-last-activity-v2 replaced in June 2025. The other current model, rdm-uplift-v2, builds only on live features.
Notes: reactivation-dormant/rdm-propensity-lr.md, reactivation-dormant/feat-rdm-last-activity-v1.md, reactivation-dormant/feat-rdm-last-activity-v2.md

## Q5
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window directly, and dec-csb-tenure-floor through exp-202 and csb-lr-base. dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 reach it through csb-xgb-v1 and csb-xgb-v2, which both build on dec-csb-tenure-floor.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The line runs find-hp-naive-effect → find-hp-adjusted-effect → find-hp-effect-v2. The note in force is find-hp-effect-v2 (-4.7pp via hp-psm-v2), which builds on the difference-in-differences experiment exp-404, the propensity-matching holdout experiment exp-408, and find-hp-adjusted-effect.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/find-hp-adjusted-effect.md, hardship-programs/find-hp-naive-effect.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md

## Q7
Only application-scorecard's feat-app-income-est builds directly on income-estimation's inc-gbm-v3.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three dataset notes: ds-csb-biz-accounts, ds-csb-churn-labels and ds-csb-oot-2025q1. The features it uses (feat-csb-spend-raw and feat-csb-tenure-band) both trace back to ds-csb-biz-accounts.
Notes: churn-small-business/ds-csb-biz-accounts.md, churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md

## Q9
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 is still in use (ror-roi-v2 ranks on it) and builds directly on feat-ror-value-band-v1, which feat-ror-value-band-v2 replaced.
Notes: retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/feat-ror-value-band-v1.md, retention-offers-roi/feat-ror-value-band-v2.md