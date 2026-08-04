## Broadcast Frequency Calculation

These four components combine into a **broadcast frequency**:

```python
def calculate_broadcast_frequency(state_signature):
    """
    Weighted sum of state components = your vibrational output

    Returns:
        float: 0-1 frequency used to compute your state mutation, validated by the field
    """
    return (
        state_signature.belief * 0.35 +
        state_signature.expectation * 0.30 +
        state_signature.embodiment * 0.25 +
        state_signature.subconscious_memory * 0.10
    )
```

### **Weighting Explanation**

- **Belief (35%)** - Foundational assumptions shape everything
- **Expectation (30%)** - Forecast determines probable futures
- **Embodiment (25%)** - Actual state must match (can't fake this)
- **Subconscious Memory (10%)** - Background noise (but can override if trauma is strong)

**Alternative Equation (Emotional Charging):**

```python
broadcast_frequency = ∑(emotion × repetition × importance)
```

**Where:**
- **Emotion** = Charge level (higher emotion = stronger signal)
- **Repetition** = How often you loop this pattern
- **Importance** = Weight you assign (consciously or unconsciously)

---

### Weighting Rationale

These weights (0.35, 0.30, 0.25, 0.10) represent LACE's current working model based on:

**Conceptual reasoning:**
- **Belief (35%)** - Deepest layer, hardest to change, most foundational. Inherited unconsciously from family/culture/trauma, operates as baseline "what's possible."
- **Expectation (30%)** - Prediction engine based on past data. Future-oriented forecast that can override conscious intent through pattern recognition.
- **Embodiment (25%)** - Present-state compiler (can't be faked, but can shift quickly). Somatic state is the honest signal - breath, posture, nervous system encode actual frequency.
- **Subconscious Memory (10%)** - Background noise (though trauma can spike this temporarily to override other components when wound is triggered).

**Phase 1 Status:** These are **provisional weights** that model observed patterns. They are internally consistent across LACE documentation (see [Base Structure](../../../01_foundation/base_structure/00_index.md) line 382 for weight verification) but not yet empirically validated.

**Phase 2 Goal:** Empirical testing to validate or refine weights. Weights may vary by person, context, or developmental stage.

**Alternative model consideration:** Equal weights (0.25 each) would suggest all components matter equally, but this would contradict LACE's "body as compiler" emphasis and observed hierarchy where deep beliefs tend to override surface intentions. Current distribution reflects LACE's hierarchy of influence based on depth of encoding.

**See Also:** [Base Structure](../../../01_foundation/base_structure/00_index.md) - StateSignature class | [Function Library](../../function_library/00_index.md) - manifest() function

---

