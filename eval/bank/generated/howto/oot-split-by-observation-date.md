---
updated: 2025-06-03
supersedes: [howto/split-random-holdout]
---
# Split on observation date, with a six-month gap and a three-month OOT tail
The OOT set is the last three observation months. Training stops six months before the OOT window starts, and those six months are left unused as a gap. Split on `observation_date`, never on account, so each account lands in one period only.
Example: training uses observation months through 2024-12, the gap is 2025-01 to 2025-06, and the OOT set is observation 2025-07 to 2025-09.
The gap exists because labels for the last training months are still maturing. Alex Chen made the random split not allowed in review on 2025-06-03.
