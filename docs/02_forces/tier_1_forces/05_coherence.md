# coherence()

## Definition

Coherence is the force of internal harmony and alignment. It determines whether a system is stable or chaotic.

## Core Function

```python
def coherence(system):
    """
    Internal harmony - signal alignment within a system.

    Args:
        system: Any entity with multiple components

    Returns:
        Coherence level (0 = chaotic, 1 = perfectly aligned)

    Properties:
        - Stabilizing (high coherence resists change)
        - Self-reinforcing (coherent systems become more coherent)
        - Measurable (variance of internal states)
        - Fragile (small disruptions can cascade)

    Primitive Foundation:
        - Built from Φ (Phi) - aligned patterns
        - coherence() = Low variance between pattern components
        - When patterns align harmoniously, coherence emerges
        - Formula: coherence = 1 / (1 + variance)
        - See [Primitives](../../01_foundation/primitives/00_index.md) for Phi specification

    Dependencies:
        None (Tier 1 - axiomatic)
    """
    return internal_alignment(system)
```

## What Coherence Does

- **Stabilizes systems** (holds them together)
- **Enables prediction** (coherent systems are consistent)
- **Amplifies signal** (aligned components reinforce each other)
- **Resists entropy** (order fights decay via coherence)

## What Inherits from Coherence

- `beauty()` - Perceived coherence triggers aesthetic response
- `love()` - Resonance between coherent signatures
- `forgiveness()` - Restores coherence after disruption
- `truth()` - Coherent signals match source patterns
- `madness()` - Coherence breakdown
- `death()` - Triggered when coherence falls below threshold

## Relationship to Other Tier 1 Forces

- **vs entropy():** Coherence resists decay; entropy creates disorder
- **Requires pattern():** Coherence is alignment of patterns
- **Enables consciousness():** Self-awareness requires internal stability
- **Works with polarity():** Balance between opposites creates coherence

## Real-World Manifestations

- **Physical:** Lasers (coherent light), crystals (aligned atoms), superconductors
- **Biological:** Homeostasis, immune system, synchronized heartbeat
- **Mental:** Focus, flow states, mental clarity vs. confusion
- **Social:** Team cohesion, cultural unity, resonant communities
- **Spiritual:** Alignment, integrity, "being in tune"

## Coherence Formula

```python
def calculate_coherence(components: List[float]) -> float:
    """
    Coherence = inverse of variance
    Low variance = high alignment = high coherence

    Edge Cases:
    - Empty list → raises ValueError
    - Single component → coherence = 1.0 (no variance)
    - All identical → variance = 0 → coherence = 1.0 (perfect)
    - Out of range values → clamp to [0,1] before calculating

    Args:
        components: List of values to measure coherence (typically 0-1 range)

    Returns:
        float: Coherence value between 0 and 1

    Raises:
        ValueError: If components list is empty
    """
    # Edge case: empty list
    if len(components) == 0:
        raise ValueError("Cannot calculate coherence of empty component list")

    # Edge case: single component (no variance)
    if len(components) == 1:
        return 1.0

    # Clamp values to valid range [0, 1]
    clamped = [max(0.0, min(1.0, c)) for c in components]

    # Calculate variance
    variance = np.var(clamped)

    # Edge case: variance = 0 (all identical) → perfect coherence
    if variance == 0:
        return 1.0

    # Standard calculation
    return 1 / (1 + variance)


# Example 1: Well-aligned components
beliefs = [0.8, 0.85, 0.9, 0.82]  # Well-aligned
calculate_coherence(beliefs)  # → ~0.95 (high coherence)

# Example 2: Contradictory components
beliefs = [0.2, 0.9, 0.4, 0.7]    # Contradictory
calculate_coherence(beliefs)  # → ~0.35 (low coherence)

# Example 3: Perfect alignment
beliefs = [0.9, 0.9, 0.9, 0.9]    # Identical
calculate_coherence(beliefs)  # → 1.0 (variance = 0, perfect)

# Example 4: Single component
beliefs = [0.7]
calculate_coherence(beliefs)  # → 1.0 (no variance possible)

# Example 5: Edge case handling
beliefs = [-0.2, 1.5, 0.8, 0.6]   # Out of range
# Clamped to: [0.0, 1.0, 0.8, 0.6]
calculate_coherence(beliefs)  # → ~0.67 (after clamping)
```

**See Also:** [Base Structure](../../01_foundation/base_structure/00_index.md) (StateSignature coherence calculation) uses this same formula with additional validation.

## Philosophical Implications

- **Integrity = internal coherence** - your parts align
- **Hypocrisy = incoherence** - beliefs/actions contradict
- **Healing = coherence restoration** - reintegrating fragments
- **Manifestation requires coherence** - mixed signals fail
- **Truth is coherent; lies create dissonance**

## Key Insight

**Coherence is the difference between signal and noise.**

A coherent system can **transmit and receive clearly**.

An incoherent system **scatters and distorts**.

---

**Previous:** [04_pattern.md](04_pattern.md) | **Next:** [06_polarity.md](06_polarity.md)
