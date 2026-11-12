## Q1
find-cu-sms-cost has one note from another project built directly on it: collections-channel-mix/find-ch-sms-call-gap, which also takes exp-504 and find-ch-sms-matches-call as inputs.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
cli-logreg-baseline rests on two dataset notes, ds-cli-eligible-pop (directly through feat-cli-pay-behaviour) and ds-cli-outcome-90d (through feat-cli-spend-velocity).
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q3
Both mq3-response-gbm-v1 and mq3-uplift-tlearner-v1 build directly on feat-mq3-recency-v1, feat-mq3-app-sessions-30d and feat-mq3-prior-treat.
Notes: marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md

## Q4
cli-logreg-baseline is the only current model in credit-line-increase built directly on a replaced feature: it takes feat-cli-util-v1, which was superseded by feat-cli-util-v2 in October 2025. The other current model, cli-xgb-v3, builds on no replaced feature or dataset.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md

## Q5
Two decisions rest on feat-csb-deposit-volatility: dec-csb-ship-xgb-v1 (through csb-xgb-v1) and dec-csb-ship-xgb-v2 (through csb-xgb-v2 and exp-206).
Notes: churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md, churn-small-business/feat-csb-deposit-volatility.md

## Q6
The line cu-uplift-v1 → cu-uplift-v2 → cu-uplift-v3 ends at cu-uplift-v3, which is in force. It is built on cu-uplift-v2, feat-cu-bureau-delta and exp-106.
Notes: collections-uplift/cu-uplift-v1.md, collections-uplift/cu-uplift-v2.md, collections-uplift/cu-uplift-v3.md, collections-uplift/feat-cu-bureau-delta.md, collections-uplift/exp-106.md

## Q7
Of other projects, only limit-decrease-policy/feat-cld-risk-band-v2 is built directly on feat-cli-util-v2 (alongside feat-cld-risk-band-v1).
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md, credit-line-increase/feat-cli-util-v2.md

## Q8
clv-ml-v2 rests on four dataset notes: ds-clv-cohort-panel, ds-clv-loss-events, ds-clv-revenue-monthly and ds-clv-holdout-2021h1, directly or through its ancestors.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-loss-events.md, customer-lifetime-value/ds-clv-revenue-monthly.md, customer-lifetime-value/ds-clv-holdout-2021h1.md

## Q9
rdm-propensity-lr and rdm-uplift-v1 both build directly on feat-rdm-last-activity-v1 and feat-rdm-app-installed.
Notes: reactivation-dormant/feat-rdm-last-activity-v1.md, reactivation-dormant/feat-rdm-app-installed.md

## Q10
clv-bgnbd-v1 is the one current model in customer-lifetime-value built directly on a replaced feature: it takes feat-clv-arpu-v1, which was superseded by feat-clv-arpu-v2 in November 2025. The other current model, clv-ml-v2, builds only on current features.
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/feat-clv-arpu-v1.md