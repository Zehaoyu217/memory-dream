---
from: [fraud-2026/fraud26-gbm-v3, ds-disp-disputes]
updated: 2026-08-27
---
# feat-disp-fraud-score: fraud26-gbm-v3 score on the original authorisation
Score from fraud-2026/fraud26-gbm-v3 for the auth_id behind each dispute, scored at authorisation time.
Lifts precision at 0.95 from 94.0% to 95.3% on disp-oot-2026h1 (exp-307).
Requires the fraud-2026 model to be live; agreed in dec-disp-fraud-score-in.
