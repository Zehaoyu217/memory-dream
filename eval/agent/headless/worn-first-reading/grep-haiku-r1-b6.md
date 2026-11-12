## Q1
Only one note: dispute-triage's feat-disp-fraud-score builds directly on fraud26-gbm-v3. The other dispute-triage notes that mention it, such as dec-disp-fraud-score-in, build on that feature rather than on the model itself.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
Four dataset notes: ds-c25-accounts-snapshot, ds-c25-churn-labels, ds-c25-app-engagement and ds-c25-oot-2024h1 (the 2024 holdout). They are reached through churn-gbm-2025-v2's feature, decision and experiment parents.
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-churn-labels.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-oot-2024h1.md

## Q3
Both build on feat-rdm-app-installed and feat-rdm-last-activity-v1.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
rdm-propensity-lr is the only one. It is still kept as the baseline and builds directly on feat-rdm-last-activity-v1, which was replaced by feat-rdm-last-activity-v2. rdm-uplift-v2 is current but builds only on non-replaced features.
Notes: reactivation-dormant/rdm-propensity-lr.md

## Q5
Four decision notes: dec-csb-90d-window directly, dec-csb-tenure-floor via exp-202 and csb-lr-base, and dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 via the csb-xgb model line.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
find-hp-naive-effect was replaced by find-hp-adjusted-effect (6.1pp), which was replaced by find-hp-effect-v2 (4.7pp). find-hp-effect-v2 is in force and builds on the difference-in-differences experiment exp-404, the propensity matching holdout experiment exp-408 and find-hp-adjusted-effect.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md, hardship-programs/find-hp-adjusted-effect.md

## Q7
Only one: application-scorecard's feat-app-income-est builds directly on inc-gbm-v3.
Notes: application-scorecard/feat-app-income-est.md

## Q8
Three dataset notes: ds-csb-biz-accounts, ds-csb-churn-labels and ds-csb-oot-2025q1. All trace back to the SMB accounts base.
Notes: churn-small-business/ds-csb-biz-accounts.md, churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md

## Q9
Both build on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 is the only one. It is still current and builds directly on feat-ror-value-band-v1, which was replaced by feat-ror-value-band-v2. ror-roi-v2 builds only on the current v2 band.
Notes: retention-offers-roi/ror-uplift-v1.md