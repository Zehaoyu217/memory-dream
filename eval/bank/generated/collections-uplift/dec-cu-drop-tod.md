---
from: [find-cu-tod-leak]
updated: 2025-07-24
---
# Decision: drop feat-cu-call-tod-v1 from all early-collections models
Agreed 2025-07-24 by Raj Patel and Sam Lee after find-cu-tod-leak.
The feature used post-contact calls, so the training estimate was too high and the live estimate would have been lower.
Removed from the cu-resp-v1 retrain and excluded from cu-uplift-v2. Day-part call scheduling is handled by a dialler rule, not by a model.
