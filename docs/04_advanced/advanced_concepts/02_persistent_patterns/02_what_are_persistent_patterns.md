# 1. Persistent Patterns & Probability Biasing

## **What Are Persistent Patterns?**

**Persistent patterns are deeply encoded probability biases** in your state_signature that attract certain life themes, relationships, and experiences.

**IMPORTANT:** LACE does NOT use "soul contracts" or pre-incarnation agreements. Instead, persistent patterns are **emergent from your current state** - they are probability weights, not pre-fated destinies.

```python
class PersistentPattern:
    """Probability bias encoded in state_signature"""

    # Identity
    soul_id: UUID
    pattern_id: UUID

    # Source (NOT pre-birth agreement)
    encoded_in: StateSignature  # Current state components
    origin: str  # "trauma", "belief", "subconscious_memory", "embodiment"

    # Behavioral Signature
    theme: str                   # What pattern attracts (e.g., "abandonment", "unavailable_partners")
    probability_weight: float    # Strength of bias (0-1)
    repetition_count: int        # How many times pattern has manifested

    # Editability
    mutable: bool = True         # Can be changed through Generative Awareness
    resistance_level: float      # How hard to edit (0=easy, 1=extremely difficult)

    # Field Dynamics
    manifestation_frequency: float  # Which worldlines this pattern matches to
```

**See Also:** [GLOSSARY.md - Persistent Patterns](../../../05_supporting/glossary/00_index.md), [BASE_STRUCTURE.md lines 344-360](../../../01_foundation/base_structure/00_index.md), [PRIMITIVES.md - Elo primitive](../../../01_foundation/primitives/00_index.md)

---

[Next: Why Patterns Exist →](03_why_patterns_exist.md)

[Back to Index](../00_index.md)
