---
from: [aml-xgb-v2, exp-405, exp-407, ds-aml-oot]
supersedes: [aml-xgb-v2]
updated: 2026-07-07
---
# aml-xgb-v3: recalibrated on Jan-Jun 2026 dispositions; top-40% capture 96.3%
Recalibrated ranker on the same five features with Jan-Jun 2026 dispositions.
On aml-oot-2026h1: 96.3% of SAR-referred alerts in the top 40% of the queue (exp-407).
Current ranker; orders the queue only, suppression rule set in dec-aml-ranker-v3.
