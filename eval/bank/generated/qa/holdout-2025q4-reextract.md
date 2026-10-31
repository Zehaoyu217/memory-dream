---
updated: 2026-05-07
from: [howto/eval-set-freeze-date]
---
# Q: Can holdout-2025q4 be re-extracted to pick up late labels? A: No, the set is frozen and a re-extract would change labels.
Re-extracting changes the labels, so metrics would no longer be comparable with earlier runs that share the frozen set id. Late labels go into the next named holdout instead.
