## Q1
Two decisions rest on feat-xs-balance-proxy. dec-xs-top-decile-offer rests on it through xs-gbm-v2 (the "boosting model with payroll"), which was built on xs-gbm-v1 and feat-xs-payroll-flag-v2, and both of those were built on the proxy. dec-xs-retrain-quarterly rests on it through find-xs-drift-2026 → exp-407-oot-2026h1 → xs-gbm-v2.
Notes: work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md

## Q2
The line runs mrisk-gbm-v1 → mrisk-gbm-v2 → mrisk-gbm-v3, and mrisk-gbm-v3 is in force now. It is built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md, work/mrisk-gbm-v2.md

## Q3
cli-logreg-baseline was built on feat-cli-pay-behaviour, feat-cli-spend-velocity and feat-cli-util-v1. Through them it rests on two datasets: ds-cli-eligible-pop (directly under the pay-behaviour and util features, and under q-cli-utilization-trigger) and ds-cli-outcome-90d (under spend velocity), which itself builds on ds-cli-eligible-pop.
Notes: work/ds-cli-eligible-pop.md, work/ds-cli-outcome-90d.md

## Q4
Two decisions rest on ds-clv-holdout-2021h1. dec-clv-ship-ml-v1 rests on it through clv-ml-v1, which was built on clv-bgnbd-v1 and exp-503, both resting on exp-501, which uses the holdout. dec-clv-ship-ml-v2 rests on it through clv-ml-v2 and dec-clv-ship-ml-v1.
Notes: work/dec-clv-ship-ml-v1.md, work/dec-clv-ship-ml-v2.md

## Q5
The line runs pbs-kmeans-v1 → pbs-gmm-v2 → pbs-gmm-v3, and pbs-gmm-v3 is the current segment model. It is built on exp-403-payment-behavior-segments, feat-pbs-timing-v2 and pbs-gmm-v2 (the "second gmm segment model").
Notes: work/pbs-gmm-v3.md, work/exp-403-payment-behavior-segments.md, work/feat-pbs-timing-v2.md, work/pbs-gmm-v2.md

## Q6
xs-call-uplift-v1 was built on exp-403-callcentre-naive, feat-xs-call-recent and find-xs-call-overstated. All three lead back to ds-xs-callcentre (the call-centre contact dataset), which builds on ds-xs-offer-log (the eligible offer log). ds-xs-offer-log builds only on the question note q-xs-propensity.
Notes: work/ds-xs-callcentre.md, work/ds-xs-offer-log.md

## Q7
Four decisions rest on ds-disp-analyst-labels. dec-disp-labels-two-analyst builds on it directly. dec-disp-autoresolve-090 and dec-disp-autoresolve-095 rest on it through disp-lgbm-v2 and the exp-301→305 chain. dec-disp-fraud-score-in rests on it through exp-307 → exp-306 → disp-find-autoresolve-96.
Notes: work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md

## Q8
The line runs rs-xgb-v1 → rs-xgb-v2 → rs-xgb-v3, and rs-xgb-v3 is in force now (dec-rs-promote-v3 moved agency placement to it). It is built on exp-308-recovery-scoring and rs-xgb-v2.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md

## Q9
clv-bgnbd-v1 was built on exp-501 (the BG/NBD versus GBM accuracy test), feat-clv-arpu-v1 (the six-month average revenue feature) and feat-clv-tenure (months on book). Through them it rests on ds-clv-holdout-2021h1, ds-clv-revenue-monthly and ds-clv-cohort-panel, which all three trace back to.
Notes: work/ds-clv-holdout-2021h1.md, work/ds-clv-revenue-monthly.md, work/ds-clv-cohort-panel.md

## Q10
Two decisions rest on ds-ed-bureau-join. dec-ed-gbm-for-watchlist rests on it through find-ed-gbm-vs-logit → exp-201 → ed-logit-v1, which uses the bureau join. dec-ed-promote-v3 rests on it through ed-gbm-v3, exp-207 and find-ed-bureau-slope, all of which go back to feat-ed-bureau-slope-v1, which is built on the bureau join.
Notes: work/dec-ed-gbm-for-watchlist.md, work/dec-ed-promote-v3.md