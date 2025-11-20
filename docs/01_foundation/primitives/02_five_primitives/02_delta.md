# Δ (Delta) - Change

The smallest unit of transition. The atom of "becoming."

```python
from typing import Any, Union
import numpy as np

class Delta:
    """The primitive of transformation"""

    def __init__(
        self,
        magnitude: float,
        direction: np.ndarray,
        irreversible: bool = False
    ):
        self.magnitude = magnitude      # How much change
        self.direction = direction      # Direction of change
        self.irreversible = irreversible # Can it be undone?

    def apply(self, state: Any) -> Any:
        """
        Change propagates through system

        Args:
            state: Current system state

        Returns:
            Modified state after delta applied
        """
        return state + self.magnitude * self.direction
```

**What Delta Governs:**
- State transitions (A → B)
- Motion and momentum
- Time's arrow (entropy increases via delta accumulation)
- Evolution and decay

**Real-World Manifestation:**
- Temperature change
- Aging
- Learning (neural state change)
- Mood shifts

---

**Previous:** [01_overview.md](../01_foundation/01_overview.md) | **Next:** [03_tau.md](03_tau.md)
