## Q1
No decision note builds on ds-cr-ivr-paths directly. Through feat-cr-ivr-path-v1 it reaches dec-cr-lgbm (via cr-lgbm-v1 and cr-logreg-v1), dec-cr-pilot and dec-cr-cost-matrix (via the lightgbm router chain), and dec-cr-caller-v2 (via fnd-cr-leak-corrected, assuming its "out-of-time router check" is exp-104).

Notes: work/dec-cr-lgbm.md, work/dec-cr-pilot.md, work/dec-cr-cost-matrix.md, work/dec-cr-caller-v2.md, work/cr-lgbm-v1.md, work/cr-logreg-v1.md, work/feat-cr-ivr-path-v1.md, work/ds-cr-ivr-paths.md, work/exp-104-call-center-routing.md, work/fnd-cr-leak-corrected.md

## Q2
The note in force is cli-xgb-v3, since no later version exists. It builds on the out-of-time AUC check for cli-xgb-v2 (exp-106-credit-line-increase), exp-107-credit-line-increase and find-cli-uplift-wins.

Notes: work/cli-xgb-v3.md, work/cli-xgb-v2.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md

## Q3
cr-lgbm-v1 rests on two dataset notes: ds-cr-ivr-paths (via feat-cr-ivr-path-v1) and ds-cr-calls (via feat-cr-caller-history-v1 and feat-cr-transcript-tfidf-v1). Its tenure feature reads cards.accounts_monthly directly, which has no note.

Notes: work/cr-lgbm-v1.md, work/feat-cr-ivr-path-v1.md, work/feat-cr-caller-history-v1.md, work/feat-cr-transcript-tfidf-v1.md, work/ds-cr-ivr-paths.md, work/ds-cr-calls.md

## Q4
fraud25-gbm-v1 and fraud25-gbm-v2 both build directly on four feature notes: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. The fraud label arrival lag is also shared, but it is not a feature note.

Notes: work/fraud25-gbm-v1.md, work/fraud25-gbm-v2.md, work/feat-f25-amt-ratio.md, work/feat-f25-device-age.md, work/feat-f25-hour-band.md, work/feat-f25-velocity-v1.md

## Q5
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. The first two reach it through cb-elasticity-v1 or v2 and feat-cb-spend-base, and dec-cb-threshold-2500 reaches it through dec-cb-adopt-banded-tiers.

Notes: work/dec-cb-adopt-banded-tiers.md, work/dec-cb-extend-flat-pilot.md, work/dec-cb-threshold-2500.md, work/cb-elasticity-v1.md, work/cb-elasticity-v2.md, work/find-cb-flat-wins.md, work/feat-cb-spend-base.md, work/feat-cb-grocery-share.md, work/ds-cb-spend-panel.md

## Q6
The note in force is disp-lgbm-v3, since disp-lgbm-v2 was superseded on 2026-09-14. It builds on dec-disp-fraud-score-in, disp-lgbm-v2, the fraud score lift experiment on v3 (exp-307-dispute-triage) and the fraud-2026 score feature (feat-disp-fraud-score).

Notes: work/disp-lgbm-v3.md, work/dec-disp-fraud-score-in.md, work/disp-lgbm-v2.md, work/exp-307-dispute-triage.md, work/feat-disp-fraud-score.md

## Q7
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 (the 2025 q4 cashback pilot) directly, and ds-cb-spend-panel through feat-cb-spend-base. The first match is by description, since the pilot note's title is `cb-pilot-2025q4`.

Notes: work/cb-elasticity-v1.md, work/ds-cb-pilot-2025q4.md, work/feat-cb-spend-base.md, work/ds-cb-spend-panel.md

## Q8
mq3-response-gbm-v1 and mq3-uplift-tlearner-v1 share three feature notes directly: feat-mq3-recency-v1, feat-mq3-app-sessions-30d (matched from "30-day app sessions") and feat-mq3-prior-treat (matched from "prior campaign contact feature", which is an inference from the description).

Notes: work/mq3-response-gbm-v1.md, work/mq3-uplift-tlearner-v1.md, work/feat-mq3-recency-v1.md, work/feat-mq3-app-sessions-30d.md, work/feat-mq3-prior-treat.md

## Q9
Directly, dec-cb-metric-24h rests on ds-cb-call-linkage. Through fnd-cb-volume-shift, dec-cb-rollout-60 does too. dec-cb-metric-48h and dec-cb-handoff-v2 reach it only through fnd-cb-def-sensitivity and fnd-cb-repeat-contact, whose cited replays (exp-306 and exp-307) build on ds-cb-call-linkage; that link is from the body text, not an explicit builds-on line.

Notes: work/dec-cb-metric-24h.md, work/dec-cb-rollout-60.md, work/fnd-cb-volume-shift.md, work/dec-cb-metric-48h.md, work/dec-cb-handoff-v2.md, work/fnd-cb-def-sensitivity.md, work/fnd-cb-repeat-contact.md, work/exp-306-chatbot-deflection.md, work/exp-307-chatbot-deflection.md, work/ds-cb-call-linkage.md

## Q10
The note in force is ed-gbm-v3, since no later version exists. It builds on ed-gbm-v2, the bureau slope lift experiment (exp-207-early-delinquency) and feat-ed-bureau-slope-v1.

Notes: work/ed-gbm-v3.md, work/ed-gbm-v2.md, work/exp-207-early-delinquency.md, work/feat-ed-bureau-slope-v1.md