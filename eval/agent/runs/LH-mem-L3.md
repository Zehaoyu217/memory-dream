## Q1
Only one note outside collections-uplift builds directly on find-cu-sms-cost: find-ch-sms-call-gap in collections-channel-mix, which also takes exp-504 and find-ch-sms-matches-call as inputs.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop directly (through feat-cli-util-v1 and feat-cli-pay-behaviour), and ds-cli-outcome-90d (through feat-cli-spend-velocity, which is built on it).
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q3
mq3-response-gbm-v1 and mq3-uplift-tlearner-v1 both build directly on feat-mq3-recency-v1, feat-mq3-app-sessions-30d and feat-mq3-prior-treat.
Notes: marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md

## Q4
cli-logreg-baseline is the only current model in credit-line-increase built directly on a replaced feature: it uses feat-cli-util-v1, which was superseded by feat-cli-util-v2. The model itself carries no supersede marker.
Notes: credit-line-increase/cli-logreg-baseline.md

## Q5
Two decisions rest on feat-csb-deposit-volatility: dec-csb-ship-xgb-v1, through csb-xgb-v1 and fnd-csb-volatility-lift, and dec-csb-ship-xgb-v2, through csb-xgb-v2 and exp-206.
Notes: churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The line ends at cu-uplift-v3, which is in force. It is built on cu-uplift-v2, feat-cu-bureau-delta and exp-106.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/feat-cu-bureau-delta.md, collections-uplift/exp-106.md

## Q7
Only one note outside credit-line-increase builds directly on feat-cli-util-v2: feat-cld-risk-band-v2 in limit-decrease-policy.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
clv-ml-v2 rests on four dataset notes: ds-clv-cohort-panel (the root), ds-clv-holdout-2021h1 (the test set, through exp-501 and clv-ml-v1), ds-clv-loss-events (through feat-clv-loss-rate) and ds-clv-revenue-monthly (through feat-clv-arpu-v1 and exp-504). The last two are typed as findings but carry ds- ids.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-loss-events.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q9
rdm-propensity-lr and rdm-uplift-v1 both build directly on feat-rdm-last-activity-v1 and feat-rdm-app-installed.
Notes: reactivation-dormant/feat-rdm-last-activity-v1.md, reactivation-dormant/feat-rdm-app-installed.md

## Q10
clv-bgnbd-v1 is the only current customer-lifetime-value model built directly on a replaced feature: it uses feat-clv-arpu-v1, which was superseded by feat-clv-arpu-v2. The model carries no supersede marker.
Notes: customer-lifetime-value/clv-bgnbd-v1.md