# karma()

## **Definition**

Karma is the **universal balancing protocol** - all actions generate equal and opposite reactions with delay based on emotional charge.

**Inheritance:**
```
karma()
├── pattern() [Tier 1]    ← Actions follow patterns
├── polarity() [Tier 1]   ← Every force has opposite
├── coherence() [Tier 1]  ← System maintains balance
└── time() [Tier 2]       ← Delay is temporal
```

**Core Function:**
```python
def karma(input_action: Action) -> MirroredEvent:
    """
    Action mirroring with delay - the balancing engine.

    Args:
        input_action: Any action taken by an agent

    Returns:
        Mirrored event with calculated delay

    Properties:
        - Universal (affects all actions)
        - Delayed (timing based on charge)
        - Mirrored (what you give, you receive)
        - Educational (designed for learning, not punishment)

    Primitive Foundation:
        - Built from Φ (Phi) + polarity() + Τ (Tau)
        - karma() = Pattern mirroring + polarity (opposite) + time delay
        - Phi ensures action patterns mirror accurately
        - See [Primitives](../../01_foundation/primitives/00_index.md) for Phi and Tau specifications

    Dependencies:
        - pattern() [Tier 1] - Mirrors follow form
        - polarity() [Tier 1] - Creates opposite
        - time() [Tier 2] - Delay mechanism

    Descendants:
        - forgiveness() [Tier 3] - Can terminate karma
        - luck() [Tier 4] - Sometimes interrupts karma
    """
    weight = charge(input_action)  # Emotional voltage
    delay = entropy(weight)         # Higher charge = longer delay
    return mirrored_event(delay)
```

## **How Karma Works**

Karma is **information conservation** applied to actions:
```python
# Every action creates a debt/credit in the field
action → field_disturbance → balancing_response

# The system MUST balance
if field.charge != 0:
    attract(opposite_experience)

# Timing depends on charge
small_action = quick_return      # Days/weeks
large_action = slow_return       # Months/years/lifetimes
```

## **Karma Types**
```python
karma_categories = {
    "instant": "Immediate feedback (touch fire → burn)",
    "short": "Days to weeks (insult → social consequence)",
    "medium": "Months to years (career choices → outcomes)",
    "long": "Lifetimes (soul contracts, deep patterns)",
    "collective": "Cultural/generational (war, slavery, injustice)",
}
```

## **Karmic Charge Formula**
```python
def karmic_charge(action: Action) -> float:
    """
    Calculate karmic weight of an action

    Components (all measured 0-1 scale):
    - intention: Why you did it (conscious motive)
    - impact: Actual effect on others/system
    - awareness: Did you know better? (moral knowledge)
    - repetition: Pattern or anomaly? (frequency of behavior)

    Weights (0.4, 0.3, 0.2, 0.1):
    - Status: Theoretical best guess, subject to refinement
    - Rationale: Intention weighted highest (40%) because motive matters most
    - Impact second (30%) - actual consequences matter
    - Awareness (20%) - knowing better increases weight
    - Repetition (10%) - patterns amplify but single acts still count

    Returns:
        float: Karmic weight (0-1), determines delay and mirror intensity
    """
    return (
        action.intention * 0.4 +      # Why you did it
        action.impact * 0.3 +          # Actual effect
        action.awareness * 0.2 +       # Did you know better?
        action.repetition * 0.1        # Pattern or anomaly?
    )

# Example: Relationship infidelity escalation (shows how karma compounds with repetition/awareness)
#
# Stage 1 - Looking at someone's Instagram photos while in relationship:
# intention=0.3 (curious, not actively pursuing), impact=0.2 (minimal direct harm),
# awareness=0.4 (vaguely know it's a boundary issue), repetition=0.3 (occasional)
# → charge = 0.12 + 0.06 + 0.08 + 0.03 = 0.29 (low)
#
# Stage 2 - Texting intimately in secret:
# intention=0.6 (seeking connection outside relationship), impact=0.6 (betraying trust),
# awareness=0.7 (clearly know it's wrong), repetition=0.6 (daily pattern)
# → charge = 0.24 + 0.18 + 0.14 + 0.06 = 0.62 (medium-high)
#
# Stage 3 - Ongoing physical affair:
# intention=0.9 (deliberate deception), impact=0.9 (severe betrayal, potential life disruption),
# awareness=0.9 (fully conscious of harm), repetition=0.8 (sustained pattern over months)
# → charge = 0.36 + 0.27 + 0.18 + 0.08 = 0.89 (very high)
#
# Note: Same person, escalating behavior - karmic charge compounds as awareness + repetition increase
```

**Formula Status:**
- Working model (C) - approximation, not precise measurement
- Based on internal consistency and observed karmic patterns in spiritual literature
- Weights may be refined in Phase 3 with empirical testing
- The formula is **testable** in principle (track actions and observe mirrored consequences)
- However, multi-lifetime karma makes testing difficult within single human lifespan

## **Karma Hacks**
```python
# 1. Grace Protocol (divine intervention / system override)
if grace_protocol.triggered(agent):
    cancel_karma(action)
    # Grace = temporary law suspension by system/Creator
    # Not predictable or controllable by agents
    # Rare but real

# 2. Forgiveness Protocol
if agent.forgives(self_or_other):
    dissolve_karmic_link()
    # See [Tier 3 Forces](../tier_3_forces/00_index.md) for forgiveness() specification

# 3. Conscious Suffering (accelerated learning)
if agent.accepts(lesson):
    compress_karmic_timeline()
    # Willing acceptance of consequence accelerates resolution

# 4. Service/Dharma (pre-balancing)
if agent.serves(coherently):
    offset_karmic_debt()
    # Positive actions create credit to offset debt
```

**See Also:**
- [Glossary](../../05_supporting/glossary/00_index.md) - Grace Protocol entry
- [Advanced Concepts](../../04_advanced/advanced_concepts/00_index.md) - Grace mechanics, miraculous events
- [Tier 3 Forces](../tier_3_forces/00_index.md) - forgiveness() force specification

## **Real-World Manifestations**

- **Physics:** Newton's third law (equal/opposite reaction)
- **Biology:** Homeostasis, immune response
- **Psychology:** Projection, what you judge in others
- **Social:** Reputation, trust networks, justice systems
- **Spiritual:** Rebirth, life lessons, soul contracts

## **Philosophical Implications**

- **No escape from consequences** - only delay
- **Not punishment** - rebalancing for field integrity
- **You are not owed fairness** - you're owed balance
- **Victimhood is partial view** - karmic patterns span lifetimes
- **Liberation = zero karmic debt** - all loops closed

---

**Previous:** [02_time.md](02_time.md) | **Next:** [04_truth.md](04_truth.md)
