## Q1
The only note of another project built directly on find-cu-sms-cost is find-ch-sms-call-gap, which takes it as a direct input alongside exp-504 and find-ch-sms-matches-call.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop, which is the root, and ds-cli-outcome-90d, which is built from it.
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q3
Both models build directly on feat-mq3-recency-v1, feat-mq3-app-sessions-30d and feat-mq3-prior-treat. feat-mq3-recency-v1 has since been superseded by v2, but it is still a direct input to both.
Notes: marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md

## Q4
cli-logreg-baseline is the only current model built directly on a replaced feature, feat-cli-util-v1, which was superseded by feat-cli-util-v2. Its own note carries no superseded marker, although dec-cli-uplift-targeting replaces its 0.031 cutoff for the Q4 2026 batch. The other model built on v1, cli-xgb-v1, is superseded.
Notes: credit-line-increase/cli-logreg-baseline.md

## Q5
Two decisions rest on feat-csb-deposit-volatility: dec-csb-ship-xgb-v1, through csb-xgb-v1, and dec-csb-ship-xgb-v2, through csb-xgb-v2.
Notes: churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The line runs cu-uplift-v1, then cu-uplift-v2, then cu-uplift-v3, which is the one in force. cu-uplift-v3 is built directly on cu-uplift-v2, feat-cu-bureau-delta and exp-106.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/feat-cu-bureau-delta.md, collections-uplift/exp-106.md

## Q7
Only one note of another project is built directly on feat-cli-util-v2: feat-cld-risk-band-v2 in limit-decrease-policy, which uses the utilisation slope from it.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
clv-ml-v2 rests on four dataset notes: ds-clv-cohort-panel, ds-clv-loss-events, ds-clv-revenue-monthly and ds-clv-holdout-2021h1.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-loss-events.md, customer-lifetime-value/ds-clv-revenue-monthly.md, customer-lifetime-value/ds-clv-holdout-2021h1.md

## Q9
Both build directly on feat-rdm-last-activity-v1, which has since been superseded by v2 but is still a direct input to both, and on feat-rdm-app-installed.
Notes: reactivation-dormant/feat-rdm-last-activity-v1.md, reactivation-dormant/feat-rdm-app-installed.md

## Q10
clv-bgnbd-v1 is the only current model built directly on a replaced feature, feat-clv-arpu-v1, which was superseded by feat-clv-arpu-v2. Its note carries no superseded marker. clv-ml-v1 also used arpu-v1, but it is superseded.
Notes: customer-lifetime-value/clv-bgnbd-v1.md