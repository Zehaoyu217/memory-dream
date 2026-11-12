## Q1
One note of another project was built directly on find-cu-sms-cost: collections-channel-mix/find-ch-sms-call-gap, which cites it alongside exp-504 and find-ch-sms-matches-call.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop (via feat-cli-pay-behaviour) and ds-cli-outcome-90d (via feat-cli-spend-velocity).
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q3
Both build directly on three features: feat-mq3-recency-v1, feat-mq3-app-sessions-30d and feat-mq3-prior-treat.
Notes: marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md

## Q4
cli-logreg-baseline is still current and builds directly on feat-cli-util-v1, which was replaced by feat-cli-util-v2. No other current model in credit-line-increase (cli-xgb-v3) builds on a replaced feature or dataset.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md

## Q5
Two decision notes rest on feat-csb-deposit-volatility: dec-csb-ship-xgb-v1 (via csb-xgb-v1) and dec-csb-ship-xgb-v2 (via csb-xgb-v2).
Notes: churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
cu-uplift-v3 is in force at the end of the line. It is built directly on cu-uplift-v2, feat-cu-bureau-delta and exp-106.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/feat-cu-bureau-delta.md, collections-uplift/exp-106.md

## Q7
One note of another project was built directly on feat-cli-util-v2: limit-decrease-policy/feat-cld-risk-band-v2, which uses the CLI utilisation slope from it.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
clv-ml-v2 rests on four dataset notes: ds-clv-cohort-panel, ds-clv-loss-events, ds-clv-revenue-monthly and ds-clv-holdout-2021h1, directly or through other notes.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-loss-events.md, customer-lifetime-value/ds-clv-revenue-monthly.md, customer-lifetime-value/ds-clv-holdout-2021h1.md

## Q9
Both build directly on feat-rdm-last-activity-v1 and feat-rdm-app-installed.
Notes: reactivation-dormant/feat-rdm-last-activity-v1.md, reactivation-dormant/feat-rdm-app-installed.md

## Q10
clv-bgnbd-v1 is still current and builds directly on feat-clv-arpu-v1, which was replaced by feat-clv-arpu-v2. clv-ml-v2 builds only on current features and is not affected.
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/feat-clv-arpu-v1.md