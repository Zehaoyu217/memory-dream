---
from: [exp-502]
updated: 2025-05-08
---
# Four of 38 tests failed sample ratio checks because the bot filter ran only in treatment
exp-502: the bot filter was applied at readout, not at assignment, and only to the treatment arm. The filter removed sessions unevenly across arms.
Fixed by moving the filter to assignment time for both arms. Basis for dec-ep-srm-gate.
