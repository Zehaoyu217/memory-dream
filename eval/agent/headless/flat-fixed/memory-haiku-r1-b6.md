## Q1
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (through xs-gbm-v2) and dec-xs-retrain-quarterly (through find-xs-drift-2026 and exp-407). The proxy was replaced by feat-xs-payroll-flag-v2, but the chain above it is still in the memory.
Notes: work/feat-xs-balance-proxy.md, work/xs-gbm-v1.md, work/xs-gbm-v2.md, work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md

## Q2
The current model is mrisk-gbm-v3 (AUC 0.91), which replaced mrisk-gbm-v2 after mrisk-gbm-v1 was superseded. It is built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md, work/mrisk-gbm-v2.md

## Q3
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop, which feeds feat-cli-util-v1, feat-cli-pay-behaviour and q-cli-utilization-trigger, and ds-cli-outcome-90d, which feeds feat-cli-spend-velocity. The chain stops there because ds-cli-eligible-pop reads cards.limits_history, which has no note.
Notes: work/cli-logreg-baseline.md, work/feat-cli-util-v1.md, work/feat-cli-spend-velocity.md, work/feat-cli-pay-behaviour.md, work/q-cli-utilization-trigger.md, work/ds-cli-eligible-pop.md, work/ds-cli-outcome-90d.md

## Q4
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 (through clv-ml-v1) and dec-clv-ship-ml-v2 (through clv-ml-v2).
Notes: work/ds-clv-holdout-2021h1.md, work/exp-501-customer-lifetime-value.md, work/clv-ml-v1.md, work/dec-clv-ship-ml-v1.md, work/clv-ml-v2.md, work/dec-clv-ship-ml-v2.md

## Q5
The current segment model is pbs-gmm-v3 (five components, seed ARI 0.81). It is built on exp-403-payment-behavior-segments, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: work/pbs-gmm-v3.md, work/exp-403-payment-behavior-segments.md, work/feat-pbs-timing-v2.md, work/pbs-gmm-v2.md

## Q6
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre, which feeds the recent-call feature and the naive call-effect experiment, and ds-xs-offer-log, which sits behind it.
Notes: work/xs-call-uplift-v1.md, work/exp-403-callcentre-naive.md, work/feat-xs-call-recent.md, work/find-xs-call-overstated.md, work/ds-xs-callcentre.md, work/ds-xs-offer-log.md

## Q7
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through the triage experiments and models.
Notes: work/ds-disp-analyst-labels.md, work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md

## Q8
The current recovery model is rs-xgb-v3, which replaced rs-xgb-v2 after rs-xgb-v1 was superseded. It is built on exp-308-recovery-scoring and rs-xgb-v2.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md

## Q9
clv-bgnbd-v1 rests on three dataset notes: ds-clv-cohort-panel, ds-clv-holdout-2021h1 and ds-clv-revenue-monthly.
Notes: work/clv-bgnbd-v1.md, work/exp-501-customer-lifetime-value.md, work/feat-clv-arpu-v1.md, work/feat-clv-tenure.md, work/ds-clv-cohort-panel.md, work/ds-clv-holdout-2021h1.md, work/ds-clv-revenue-monthly.md

## Q10
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3 (through ed-gbm-v3) and dec-ed-gbm-for-watchlist (through the scorecard and bureau-slope chain).
Notes: work/ds-ed-bureau-join.md, work/ed-logit-v1.md, work/feat-ed-bureau-slope-v1.md, work/ed-gbm-v3.md, work/dec-ed-promote-v3.md, work/dec-ed-gbm-for-watchlist.md