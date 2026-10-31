---
from: [ds-cr-calls]
updated: 2026-07-20
---
# Intent labels are wrap-up codes mapped to 14 intents, and about 11 percent are disputed
Labels come from the agent wrap-up code in `callcenter.calls.wrap_intent`, mapped to 14 intents. Multi-intent calls (6.1 percent) keep the first code.
Double-coding of 1,200 calls by the QA team in July 2026 agreed with the wrap-up code 89 percent of the time, so about 11 percent of labels are disputed.
Adjudicated labels for those 1,200 calls replace the wrap-up code in training from cr-lgbm-v3 onward (exp-106).
Source for adjudication: `callcenter.qa_double_code`, owner cx-analytics.
