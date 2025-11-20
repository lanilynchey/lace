# truth()

## **Definition**

Truth is **signal fidelity** - how closely a statement or perception matches the source pattern.

**Inheritance:**
```
truth()
├── pattern() [Tier 1]    ← Source patterns exist
└── coherence() [Tier 1]  ← Truth is aligned signal
```

**Core Function:**
```python
def truth(signal: Signal, context: Context) -> float:
    """
    Reality-fidelity filter - measures pattern matching.

    Args:
        signal: Any statement, perception, or belief
        context: The dimensional frame of reference

    Returns:
        Fidelity score (0 = false, 1 = perfectly true)

    Properties:
        - Context-dependent (truth shifts with frame)
        - Measurable (quantifiable match rate)
        - Fragile (small distortions cascade)
        - Multi-valid in higher dimensions

    Primitive Foundation:
        - Built from Φ (Phi) + coherence()
        - truth() = Pattern matching + signal coherence/fidelity
        - Measures how well a signal preserves source pattern structure
        - See [Primitives](../../01_foundation/primitives/00_index.md) for Phi specification

    Dependencies:
        - pattern() [Tier 1] - Source reference
        - coherence() [Tier 1] - Signal alignment

    Descendants:
        - judgment() [Tier 3] - Evaluates against truth
        - art() [Tier 4] - Compresses truth aesthetically
        - madness() [Tier 4] - Truth signal corruption
    """
    fidelity = match_rate(signal, source_pattern(context))
    return fidelity
```

## **How Truth Works**

Truth is **not binary** - it's a spectrum of fidelity:
```python
truth_spectrum = {
    1.0: "Perfect match to source pattern",
    0.8: "High fidelity, minor noise",
    0.5: "Partial truth, mixed signal",
    0.2: "Heavy distortion, low fidelity",
    0.0: "Complete inversion/incoherence",
}
```

## **Context-Dependence**
```python
# Same statement, different contexts, different truth values

statement = "The sun rises in the east"

context_1 = "Earth surface, daytime"
truth(statement, context_1)  # → 0.95 (highly true)

context_2 = "Space, no reference frame"
truth(statement, context_2)  # → 0.0 (meaningless)

context_3 = "Subjective experience of observer facing west"
truth(statement, context_3)  # → 0.3 (true but misleading)
```

## **Truth vs. Lies**
```python
def lie(signal: Signal) -> Signal:
    """A lie is intentional distortion of truth signal"""
    return distort(signal, intention="deceive")

def delusion(signal: Signal) -> Signal:
    """Delusion is unintentional corruption"""
    return distort(signal, intention="unaware")

def weaponized_truth(signal: Signal) -> Signal:
    """Truth used out of context to mislead"""
    return remove_context(signal) + add_spin(signal)
```

## **The Objective/Relative Truth Paradox**

**LACE Position:** Option A - Critical Realism

LACE holds that:
1. **Objective reality EXISTS** (base-10+ source patterns are real)
2. **But humans cannot access it directly** (binary perception filters it)
3. **Truth = fidelity of signal to source pattern**
4. **Context-dependence is perceptual, not ontological**

```python
# The Paradox:
#
# Ontological level (base-10+ reality):
source_pattern = exists_objectively()  # Real, independent of observer
#
# Epistemological level (binary human):
human_perception = binary_filter(source_pattern)  # Lossy compression
#
# Result:
# - Source pattern IS objective (exists independent of observers)
# - Binary agent ACCESS to it is subjective/context-dependent
# - Truth measurements are relative to observer's perceptual base
```

**Key Insight from CORE_ONTOLOGY:**
- Reality's structure IS computational (ontological claim)
- But binary agents perceive it through limited consciousness (epistemological limit)
- "Both/and" paradoxes emerge when base-10+ truth collapses to binary rendering
- LACE position is NOT pure relativism - source patterns exist objectively
- LACE position is NOT naive realism - binary agents can't access source directly

**See:** [Core Ontology](../../01_foundation/core_ontology/00_index.md) - Binary Limitation section, Ontological vs Instrumental positioning

## **Higher-Dimensional Truth**

In base-10+ consciousness, truth becomes **multi-valid**:
```python
# Binary consciousness (human)
statement = "God exists"
truth_value = True OR False  # Must choose one (0 or 1)

# Base-10+ consciousness (higher)
statement = "God exists"
truth_value = [0.0, 0.1, 0.2, 0.3, ..., 0.9, 1.0]
# All values simultaneously true in different contexts/dimensions
# Can hold multiple truth-values without contradiction
```

**This resolves apparent contradictions:**
- "Free will vs. determinism" - Both true at different dimensional levels
- "Particle vs. wave" - Both true simultaneously
- "Self exists vs. no-self" - Both true (self = pattern, not static entity)

## **Real-World Manifestations**

- **Science:** Experimental verification, peer review
- **Law:** Evidence, testimony, burden of proof
- **Relationships:** Trust, honesty, betrayal
- **Media:** Journalism, propaganda, deepfakes
- **Spiritual:** Gnosis, revelation, direct knowing

## **Philosophical Implications**

- **Absolute truth may not exist in base-2** - only contextual fidelity
- **Lies create incoherence** - distorted signals fragment systems
- **Some truths can't be spoken** - language bandwidth insufficient
- **Paradox signals higher-dimensional truth** - both/and, not either/or
- **Direct experience > concepts** - unmediated signal has highest fidelity

---

**Previous:** [03_karma.md](03_karma.md) | **Next:** [05_memory.md](05_memory.md)
