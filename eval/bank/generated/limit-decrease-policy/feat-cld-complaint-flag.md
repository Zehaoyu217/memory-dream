---
from: [ds-cld-complaint-calls]
updated: 2025-03-03
---
# feat-cld-complaint-flag: call-level flag for limit-related complaints in callcenter.calls
Flag is 1 when the call reason is 'complaint', 'limit query' or 'fee dispute' within 30 days of a decrease.
About 3.4% of decrease-cohort accounts flagged in the first 30 days.
Used as the label in cld-complaint-logit and the control comparison in exp-203.
