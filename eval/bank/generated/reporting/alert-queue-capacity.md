---
updated: 2026-03-02
---
# The fraud ops queue can work about 50 alerts a day, which sets the precision@50 target
- Ops capacity is about 50 alerts per analyst-day across the queue, so the alert threshold is set to keep the top 50 a day useful.
- A model is only moved to production if precision@50 is at or above its predecessor on the latest holdout.
- Capacity changes are agreed with Daniel Okafor before the threshold changes.
