## State Alignment Mechanics

**Revision note:** This document previously modeled manifestation as searching a database of pre-existing "worldlines" and selecting the closest match. It has been rewritten around direct state mutation instead - see [`working/timeline_model_revision.md`](../../../../working/timeline_model_revision.md) and [`StateTrajectory`](../../../01_foundation/base_structure/03_data_models/06_data_model_timeline.md) for the full reasoning and replacement schema.

**How the system computes your next state**

```python
def calculate_target_alignment(current_frequency, intention_frequency):
    """
    How closely current state aligns with an intended target state

    Process:
        1. Receive current state_signature frequency
        2. Receive intention's target frequency
        3. Calculate alignment between the two
        4. Feed alignment into compute_state_mutation() (see StateTrajectory),
           which uses it to narrow or widen the mutation's variance

    Returns:
        float: Alignment score (0-1) - how far current state is from target

    Note: This does NOT search a database of pre-existing alternatives.
    There is one current state and one intended target; this measures
    the gap between them directly, which then determines how large and
    how certain the resulting mutation is.
    """
    alignment = calculate_resonance(current_frequency, intention_frequency)
    return alignment
```

### **Resonance Calculation**

```python
def calculate_resonance(current_frequency, target_frequency):
    """
    How closely current state matches an intended target

    Formula (unchanged from before - this was always just a distance
    formula, never actually dependent on multiverse framing):
        resonance = 1 - abs(current_frequency - target_frequency)

    Returns:
        float: 0-1 (1 = perfect alignment, 0 = no alignment)
    """
    difference = abs(current_frequency - target_frequency)
    resonance = 1 - difference

    return resonance
```

**Example:**

```python
# Your current frequency:
current_frequency = 0.75  # Moderately high vibration

# Your intended target:
intended_frequency = 0.76  # Very close to current - small mutation needed

# Resonance:
resonance(current, intended) = 0.99  # High alignment, small state delta required

# Result:
# compute_state_mutation() computes a small, high-confidence mutation
# toward the intended target - not a "jump" to a pre-existing alternative worldline
```

**What changed and why:** the underlying math is identical to before - `1 - abs(difference)` was never actually a claim about multiverse structure, just a distance formula. What changed is what the two numbers being compared *mean*: previously, "your frequency" vs. "a candidate worldline pulled from a database of many." Now, "your current state" vs. "your own intended target" - one comparison, not a search across many pre-existing options, and the result feeds directly into how the state actually mutates rather than which pre-built reality gets selected.

---

**See Also:** [StateTrajectory](../../../01_foundation/base_structure/03_data_models/06_data_model_timeline.md) - `compute_state_mutation()`, the function this alignment score feeds into | [Manifestation Latency](../../../04_advanced/advanced_concepts/22_manifestation_latency.md) - how divergence (the inverse of alignment) determines processing delay

---
