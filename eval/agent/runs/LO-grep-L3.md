## Q1
One note in another project builds directly on find-cu-sms-cost: find-ch-sms-call-gap in collections-channel-mix. Its `from:` lists collections-uplift/find-cu-sms-cost, and it narrows the "SMS gets 83% of call uplift" result to the top 20% only, not the whole 8-29 DPD group.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
cli-logreg-baseline is built on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour (q-cli-utilization-trigger sits in between too). Following those back, it rests on two dataset notes: ds-cli-eligible-pop and ds-cli-outcome-90d. The second comes in through feat-cli-spend-velocity and itself builds on ds-cli-eligible-pop.
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q3
Both models list three feature notes directly in `from:`: feat-mq3-recency-v1, feat-mq3-app-sessions-30d and feat-mq3-prior-treat. feat-mq3-email-open-90d is used only by the response model.
Notes: marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md

## Q4
cli-logreg-baseline is the only one. No note replaces it, and it builds directly on feat-cli-util-v1, which feat-cli-util-v2 replaced. cli-xgb-v1 also uses feat-cli-util-v1 but was itself replaced by cli-xgb-v2, and no dataset note in the project has been replaced.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-util-v2.md

## Q5
Two decision notes rest on it: dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2. The first is reached through csb-xgb-v1 and fnd-csb-volatility-lift (via exp-203); the second through csb-xgb-v2, exp-206 and dec-csb-ship-xgb-v1. dec-csb-ship-xgb-v1 has since been replaced by dec-csb-ship-xgb-v2.
Notes: churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The line runs cu-uplift-v1, then cu-uplift-v2 (2025-12-09), then cu-uplift-v3 (2026-03-06). cu-uplift-v3 is the one in force; no note replaces it, and dec-cu-promote-v3 promoted it to call routing. It is built on cu-uplift-v2, feat-cu-bureau-delta and exp-106.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/feat-cu-bureau-delta.md, collections-uplift/exp-106.md

## Q7
One note in another project builds directly on feat-cli-util-v2: feat-cld-risk-band-v2 in limit-decrease-policy. It rebuilds the four risk bands using the CLI 6-month utilisation slope.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
Following clv-ml-v2 back through clv-ml-v1, the experiments, the decisions and the features, it rests on all four dataset notes in the project: ds-clv-cohort-panel, ds-clv-holdout-2021h1, ds-clv-loss-events and ds-clv-revenue-monthly.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-loss-events.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q9
By their `from:` lists, both build directly on feat-rdm-last-activity-v1 and feat-rdm-app-installed. The text of rdm-uplift-v1 also mentions prior response and balance band, but those two notes are not in its `from:` list.
Notes: reactivation-dormant/feat-rdm-last-activity-v1.md, reactivation-dormant/feat-rdm-app-installed.md

## Q10
clv-bgnbd-v1 is the only one. No note replaces it (it is kept as the marketing sanity check), and it builds directly on feat-clv-arpu-v1, which feat-clv-arpu-v2 replaced. clv-ml-v1 also used feat-clv-arpu-v1 but was replaced by clv-ml-v2, which uses arpu-v2.
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/feat-clv-arpu-v1.md, customer-lifetime-value/feat-clv-arpu-v2.md