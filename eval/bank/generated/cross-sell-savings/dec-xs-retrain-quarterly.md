---
from: [find-xs-drift-2026, exp-407-oot-2026h1]
updated: 2026-07-14
---
# Decision: xs-gbm retrains quarterly, with the payroll pattern set rebuilt on 2026 descriptors
Replaces the earlier retrain-when-needed rule. Retraining each quarter picks up the new descriptors within one quarter of a change.
The payroll pattern set is rebuilt first; the retrained model is scored on xs-oot-2026h1 before release.
