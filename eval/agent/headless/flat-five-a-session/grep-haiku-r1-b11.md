## Q1
Two decision notes rest on feat-xs-balance-proxy. dec-xs-top-decile-offer rests on it through exp-405-top-decile and xs-gbm-v2, which builds on xs-gbm-v1. dec-xs-retrain-quarterly rests on it through exp-407-oot-2026h1 and the same xs-gbm-v2 → xs-gbm-v1 chain.
Notes: work/feat-xs-balance-proxy.md, work/xs-gbm-v1.md, work/xs-gbm-v2.md, work/exp-405-top-decile.md, work/exp-407-oot-2026h1.md, work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md

## Q2
The note in force is mrisk-gbm-v3. It is built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2. The line runs mrisk-gbm-v1 → mrisk-gbm-v2 → mrisk-gbm-v3.
Notes: work/mrisk-gbm-v1.md, work/mrisk-gbm-v2.md, work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md

## Q3
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop and ds-cli-outcome-90d. The first is the root, and the second builds on it. The chain goes through feat-cli-pay-behaviour, feat-cli-spend-velocity and feat-cli-util-v1, and through q-cli-utilization-trigger for the utilisation feature.
Notes: work/cli-logreg-baseline.md, work/feat-cli-pay-behaviour.md, work/feat-cli-spend-velocity.md, work/feat-cli-util-v1.md, work/q-cli-utilization-trigger.md, work/ds-cli-outcome-90d.md, work/ds-cli-eligible-pop.md

## Q4
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2. This follows explicit "Builds on" links only. The holdout reaches dec-clv-ship-ml-v1 through exp-501-customer-lifetime-value → clv-bgnbd-v1 → clv-ml-v1, and dec-clv-ship-ml-v2 through clv-ml-v2 → clv-ml-v1.
Notes: work/dec-clv-ship-ml-v1.md, work/dec-clv-ship-ml-v2.md, work/exp-501-customer-lifetime-value.md, work/clv-bgnbd-v1.md, work/fnd-clv-bgnbd-bias.md, work/exp-503-customer-lifetime-value.md, work/clv-ml-v1.md, work/clv-ml-v2.md

## Q5
The note in force is pbs-gmm-v3. It is built on exp-403-payment-behavior-segments, feat-pbs-timing-v2 and pbs-gmm-v2. The line runs pbs-kmeans-v1 → pbs-gmm-v2 → pbs-gmm-v3.
Notes: work/pbs-kmeans-v1.md, work/pbs-gmm-v2.md, work/pbs-gmm-v3.md, work/exp-403-payment-behavior-segments.md, work/feat-pbs-timing-v2.md