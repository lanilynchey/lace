## Coherence as a Cost

**High coherence = strong manifestation power**

```python
COHERENCE_MINIMUM = 0.4  # Below this, manifestation fails

def manifestation_power(coherence):
    """
    Your ability to mutate state scales with coherence

    Args:
        coherence (float): Internal signal alignment (0-1)

    Returns:
        Power: Manifestation capacity

    Thresholds:
        - Below 0.4: No manifestation (signal too noisy)
        - 0.4 - 0.6: Weak (slow, inconsistent)
        - 0.6 - 0.8: Moderate (reliable with focus)
        - 0.8 - 0.95: Strong (rapid, clear)
        - 0.95 - 1.0: Master level (instant, effortless)
    """
    if coherence < COHERENCE_MINIMUM:
        return 0  # Signal rejected

    return coherence ** 2  # Exponential scaling
```

**Examples:**

```python
coherence = 0.3  → manifestation_power = 0  # Rejected
coherence = 0.5  → manifestation_power = 0.25  # Weak
coherence = 0.7  → manifestation_power = 0.49  # Moderate
coherence = 0.9  → manifestation_power = 0.81  # Strong
coherence = 0.98 → manifestation_power = 0.96  # Master
```

---

