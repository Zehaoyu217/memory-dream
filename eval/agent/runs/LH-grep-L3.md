## Q1
Only one note from another project builds directly on collections-uplift/find-cu-sms-cost: collections-channel-mix/find-ch-sms-call-gap, which lists it in its from: line. The other direct child, dec-cu-promote-v3, is in the same project.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
cli-logreg-baseline rests on two dataset notes, ds-cli-eligible-pop (directly, and via feat-cli-util-v1, feat-cli-pay-behaviour and q-cli-utilization-trigger) and ds-cli-outcome-90d (via feat-cli-spend-velocity).
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q3
Both mq3-response-gbm-v1 and mq3-uplift-tlearner-v1 build directly on three feature notes: feat-mq3-recency-v1, feat-mq3-app-sessions-30d and feat-mq3-prior-treat. The gbm also uses feat-mq3-email-open-90d, which the T-learner does not.
Notes: marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md

## Q4
One current model does: cli-logreg-baseline builds directly on feat-cli-util-v1, which feat-cli-util-v2 has replaced. The other current CLI model, cli-xgb-v3, builds on no superseded feature or dataset note.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md

## Q5
Two decision notes rest on feat-csb-deposit-volatility, both through the XGBoost line: dec-csb-ship-xgb-v1 (via csb-xgb-v1) and dec-csb-ship-xgb-v2 (via csb-xgb-v2). The deposit-volatility feature also feeds exp-203 and fnd-csb-volatility-lift, but those are not decisions.
Notes: churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The line runs cu-uplift-v1, replaced by cu-uplift-v2, replaced by cu-uplift-v3. cu-uplift-v3 is in force and is built on cu-uplift-v2, feat-cu-bureau-delta and exp-106.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/feat-cu-bureau-delta.md, collections-uplift/exp-106.md

## Q7
Only one note from another project builds directly on credit-line-increase/feat-cli-util-v2: limit-decrease-policy/feat-cld-risk-band-v2. The other two direct children, cli-xgb-v2 and exp-106, are in the same project.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
clv-ml-v2 rests on four dataset notes: ds-clv-cohort-panel, ds-clv-loss-events, ds-clv-holdout-2021h1 and ds-clv-revenue-monthly. It reaches them through feat-clv-tenure, feat-clv-loss-rate, exp-501, feat-clv-arpu-v1, exp-504 and related notes.
Notes: customer-lifetime-value/ds-clv-cohort-panel.md, customer-lifetime-value/ds-clv-loss-events.md, customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/ds-clv-revenue-monthly.md

## Q9
Both rdm-propensity-lr and rdm-uplift-v1 build directly on feat-rdm-last-activity-v1 and feat-rdm-app-installed. rdm-uplift-v1 also builds on rdm-propensity-lr itself, which is a model, not a feature.
Notes: reactivation-dormant/feat-rdm-last-activity-v1.md, reactivation-dormant/feat-rdm-app-installed.md

## Q10
One current model does: clv-bgnbd-v1 builds directly on feat-clv-arpu-v1, which feat-clv-arpu-v2 has replaced. clv-ml-v2, the other current model, builds on no superseded feature or dataset note.
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/feat-clv-arpu-v1.md