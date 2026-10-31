---
from: [dq-late-logit-v2, fnd-late-model-lift, dec-dq-late-alert-rule-v1]
updated: 2026-02-12
supersedes: [dec-dq-late-alert-rule-v1]
---
# Decision: pre-alert at 06:30 on D+1 when dq-late-logit-v2 gives above 0.6; page at 11:00 stays
At 06:30 the model scores each due partition. Probability above 0.6 sends a pre-alert to the data-eng channel so someone can check the upstream job.
The 11:00 not-landed page from dec-dq-late-alert-rule-v1 stays as the hard backstop.
