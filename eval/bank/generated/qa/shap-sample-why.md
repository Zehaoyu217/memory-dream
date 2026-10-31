---
updated: 2026-03-12
from: [howto/shap-sample-size]
---
# Q: Why is SHAP computed on 5,000 accounts instead of the full OOT set? A: The full OOT set takes about four hours, and 5,000 accounts reproduce the top ten ranking.
The sample is stratified 50/50 across score decile bands 1 to 5 and 6 to 10. It was used for the 2026 retention model review.
