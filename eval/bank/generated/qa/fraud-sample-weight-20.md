---
updated: 2025-07-08
from: [howto/sampling-stratified-by-segment]
---
# Q: What weight is given to non-fraud rows in the fraud training sample? A: 20, because only 5 percent of non-fraud rows are kept.
All labelled fraud cases are kept. Weight 20 restores the base rate to the book.
Ben Carter's finance team reconciles exposure using the stratum counts in the run manifest.
