---
updated: 2025-05-12
supersedes: [glossary/recall-at-k]
---
# recall@k divides by total positives, not by k
The old note divided by k. recall@k is positives in the top-k divided by total positives in the evaluation set. Dividing by k gives precision@k. The two definitions were swapped in the old notes.
Affected: the Q1 2025 deck's "recall@10%" values (4.6% in the example) were precision. Recall on the same set is 56%.
