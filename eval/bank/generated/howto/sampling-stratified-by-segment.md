---
updated: 2025-07-02
---
# Sample training accounts stratified by book segment and product
Stratify on book segment (prime, near-prime, subprime) and product (classic, gold, platinum). Sample 20% of accounts for general credit models. For fraud models keep every labelled fraud case and 5% of non-fraud, and give non-fraud rows weight 20 in training so the base rate matches the book.
Stratum counts are written to the run manifest so Ben Carter's finance team can reconcile exposure to the full book.
