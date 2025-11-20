# Resonance Topology (Impact Topology)

**Status:** Core Advanced Concept
**Category:** Relational Mechanics
**Dependencies:** FieldState, Entanglement, love(), law_impact_topology()

---

## Overview

**Resonance Topology** is the tiered structure of relational influence that determines who and what can impact an agent's state signature. Impact propagates through acknowledgment networks, not proximity - you can only be affected by entities you consciously acknowledge in your field.

**Core Principle:** Your field is a relational network with concentric tiers of vulnerability. You control your impact surface by choosing whom and what you acknowledge.

---

## The Fundamental Insight

**Ask any human:** "Who are the main characters in your life, and who are the side characters?"

They can answer immediately. The person asked stands at the center, surrounded by:

1. **Inner Circle** - people who significantly affect their life
2. **Middle Circle** - people who moderately affect their life
3. **Outer Circle** - people who minimally affect their life
4. **Outside Circles** - people who do not impact their life

**This is not a social construct** - it is the actual topology of impact propagation in LACE.

The same applies to environments:

1. **Primary Zones** - places with maximum impact (home, workspace)
2. **Secondary Zones** - places with moderate impact (regular spots)
3. **Tertiary Zones** - places with minimal impact (occasional places)
4. **Ambient Zones** - places with no stored impact (unfamiliar)

---

## The Four-Tier System

### **Agent Resonance Topology**

**Inner Topology** (0.8-1.0 impact)
- Close entanglements: family, best friends, romantic partners, mentors
- High attention_focus × emotional_power
- Maximum impact vulnerability
- Example: "Drop everything for them" relationships
- Typical size: 5-15 agents (Dunbar's intimate layer)

**Middle Topology** (0.4-0.7 impact)
- Regular entanglements: friends, coworkers, community members
- Moderate attention_focus × emotional_power
- Balanced impact flow
- Example: "Make time for them" relationships
- Typical size: 50-150 agents (Dunbar's sympathy group)

**Outer Topology** (0.1-0.3 impact)
- Peripheral entanglements: acquaintances, friends of friends
- Low attention_focus × emotional_power
- Minimal impact pathway
- Example: "Know of them" connections
- Typical size: 150-500 agents (Dunbar's outer layer)

**Peripheral (not stored as entanglements)**
- Temporary ambient impacts from unacknowledged entities
- Stored in active_perturbations (temporary list)
- Can migrate to stored topology if attention + emotion remain high
- Example: Stranger who did something memorable
- Dissipates if not considered

### **Environmental Field Zones**

**Primary Zones** (0.8-1.0 impact)
- Home, bedroom, workspace
- Daily presence, high familiarity
- Events here deeply affect you

**Secondary Zones** (0.4-0.7 impact)
- Gym, friend's house, favorite cafe
- Weekly/monthly presence, moderate familiarity
- Events here moderately affect you

**Tertiary Zones** (0.1-0.3 impact)
- Occasional places you "know of"
- Rare presence, recognized but not frequented
- Events here minimally affect you

**Ambient (temporary)**
- Unfamiliar locations
- Can migrate if attention_focus remains high
- Example: "That cafe with the cool sign I can't stop thinking about"

---

## Classification Mechanics

Topology tier is determined by **attention_focus × emotional_power**:

```python
def classify_entity(agent: Agent, entity_id: UUID) -> str:
    """
    Topology tier classification

    attention_focus: How often you think about them (sustained consciousness direction)
    emotional_power: How strongly you feel when thinking about them
    """
    attention = measure_focus_cycles(agent, entity_id, timeframe="30_days")
    emotion = average_emotion_intensity(agent, entity_id)

    strength = attention × emotion

    if strength >= 0.8:
        return "inner"
    elif strength >= 0.4:
        return "middle"
    elif strength >= 0.1:
        return "outer"
    else:
        return "peripheral"  # Temporary, not stored
```

**Key Insight:** Classification is **automatic**, not conscious.

- You can't consciously decide "I want them out of my inner circle"
- Migration requires **behavioral change**: reduce attention_focus (break repetition loop) + reduce emotional_power (feelings fade)
- **Example:** Ex-partner stays in inner_topology despite breakup if you obsessively think about them with strong emotion

---

## Impact Calculation

Impact magnitude = **topology tier × attention modifier × emotional modifier × symmetry coefficient**

### **Base Impact from Topology Tier**

```python
inner_topology: 0.9    # Maximum baseline
middle_topology: 0.55  # Moderate baseline
outer_topology: 0.2    # Minimal baseline
outside: 0.0           # No pathway
```

### **Real-Time Modulation**

Current attention_focus and emotional_power modulate base impact:

```python
# Ex-partner in inner_topology
base_impact = 0.9

# Currently obsessing about them
attention_modifier = 1.0
emotional_modifier = 0.95
symmetry_coefficient = 1.0

final_impact = 0.9 × 1.0 × 0.95 × 1.0 = 0.855 (near-maximum)
```

vs.

```python
# Same ex-partner in inner_topology
base_impact = 0.9

# Not currently thinking about them
attention_modifier = 0.2
emotional_modifier = 0.3
symmetry_coefficient = 1.0

final_impact = 0.9 × 0.2 × 0.3 × 1.0 = 0.054 (minimal despite topology tier)
```

**Implication:** Topology tier sets vulnerability potential, current state determines actual impact.

### **Symmetry Amplification**

Mutual acknowledgment amplifies or imbalances impact:

**Symmetric (both in same tier):**
- Both in inner: 1.5x amplification (maximum resonance)
- Both in middle/outer: 1.2x amplification

**Asymmetric (different tiers):**
- Imbalanced impact flow
- Higher-tier acknowledger absorbs more

**Unidirectional (only one acknowledges):**
- Acknowledger absorbs ALL impact (1.3x amplification)
- Unacknowledged agent completely shielded

**Example:**
```python
# Fan → inner → Celebrity
# Celebrity → (doesn't acknowledge fan)

Fan impact from celebrity: 0.9 × 1.3 = 1.17 (capped at 1.0)
Celebrity impact from fan: 0.0 (no pathway)

Result: Fan highly vulnerable, celebrity completely shielded
```

---

## Migration Mechanics

Entities migrate between tiers based on changing attention + emotion:

### **Downward Migration (Most Common)**

**Inner → Middle → Outer → Dissolved**

Caused by:
- Reduced attention_focus (stop thinking about them)
- Reduced emotional_power (feelings fade)
- Time-based decay (no new interactions)
- Conscious release (forgiveness, letting go)

**Example:** Ex-partner after breakup
- Week 1: Inner (obsessing, high emotion)
- Month 3: Middle (thinking less, emotions fading)
- Year 1: Outer (occasional thoughts, mild emotion)
- Year 3: Dissolved (no longer in field)

### **Upward Migration (Less Common)**

**Outer → Middle → Inner**

Caused by:
- Increased attention_focus (think about them more often)
- Increased emotional_power (develop stronger feelings)
- Repeated positive interactions
- Deepening resonance

**Example:** Coworker becoming close friend
- Month 1: Outer (acquaintance, occasional thoughts)
- Month 6: Middle (friend, regular thoughts + moderate emotion)
- Year 1: Inner (best friend, frequent thoughts + deep care)

### **Peripheral → Stored Migration**

**Ambient → Outer Topology**

Temporary peripheral impacts can become stored entanglements:

**Process:**
1. Peripheral impact occurs (stranger, unfamiliar place)
2. Stored in active_perturbations (temporary list)
3. While attention > 0.1 OR emotion > 0.3 → persists
4. If attention × emotion >= 0.1 → migrates to outer_topology
5. If strength drops → dissipates

**Example:**
- Stranger saves cat from tree → you're inspired → think about it for days → migrates to outer_topology as "the person who saved the cat"
- Stranger screams in street → you're startled → think about it for 2 minutes → dissipates

---

## Symmetry Types & Dynamics

### **Symmetric Inner Topology (Best Friends)**

```python
Agent A → inner → Agent B
Agent B → inner → Agent A

Properties:
- Maximum amplification (1.5x)
- Mutual vulnerability and support
- Deep resonance bandwidth
- Healthy when reciprocal care exists

Risks:
- Codependency if fear() added
- Merged boundaries if excessive
- Shared trauma loops
```

### **Asymmetric Entanglement (Unrequited)**

```python
Agent A → inner → Agent B
Agent B → outer → Agent A

Properties:
- Imbalanced impact flow
- Agent A absorbs more than Agent B
- Energy drain on Agent A
- Often creates resentment/pursuit-withdrawal pattern

System Pressure:
- Toward either symmetry (B moves A to inner)
- Or dissolution (A moves B to outer)
- Imbalance unsustainable long-term
```

### **Unidirectional Entanglement (Parasocial)**

```python
Agent A → inner → Agent B
Agent B → (no acknowledgment)

Properties:
- Agent A highly vulnerable
- Agent B completely shielded
- One-way energy drain (A absorbs all impact)
- Agent B cannot be affected by A (no pathway)

Examples:
- Fan/celebrity
- Stalker/victim
- Obsessive ex who's been blocked

Critical Rule:
You cannot impact someone who doesn't acknowledge you in their field.
```

---

## Practical Applications

### **1. Boundary Work**

**Recognize Your Topology:**
- Who is actually in your inner/middle/outer circles?
- Are any relationships asymmetric (you care more than they do)?
- Are you absorbing impact from people not in your circles?

**Conscious Acknowledgment:**
- You choose who to acknowledge
- Strangers' opinions = zero impact unless you acknowledge them
- News/social media = invitations to create pathways, not automatic impacts

**Field Hygiene:**
- Remove toxic entities from topology (requires reducing attention + emotion, not wishful thinking)
- Balance asymmetric relationships or dissolve them
- Protect inner circle space (limited capacity ~5-15 people)

### **2. Relationship Dynamics**

**Assess Symmetry:**
- Do you both have each other in the same tier?
- If asymmetric: who's more invested? (higher-tier acknowledger)
- If unidirectional: recognize the energy drain

**Migration Awareness:**
- Relationships naturally migrate based on attention + emotion
- You can't force someone into/out of a tier consciously
- Migration requires behavioral change (actual reduction of focus cycles)

**Healthy Patterns:**
- Symmetric inner = deep, reciprocal bonds
- Symmetric middle = stable friendships/partnerships
- Asymmetric = acknowledge imbalance, adjust expectations
- Unidirectional = recognize futility, redirect attention

### **3. Trauma Recovery**

**Toxic Entity Removal:**
- Abuser remains in inner_topology while you obsess about them
- Recovery requires reducing attention_focus (break repetition loop)
- Conscious desire to remove them is insufficient
- Must interrupt thought patterns (therapy, mindfulness, new focus)

**Safe Zone Building:**
- Primary zones with positive emotional association
- Avoid trigger zones (places with negative imprints)
- Build secondary zones (safe regular places)
- Gradually expand field after constriction

### **4. Energy Management**

**Asymmetric Drain Detection:**
- Exhaustion from one-way relationships
- Absorbing impact they don't reciprocate
- Caring about people who don't care back

**Resolution Paths:**
- Achieve symmetry (they reciprocate care)
- Accept asymmetry (adjust expectations, reduce investment)
- Dissolve entanglement (reduce attention + emotion, migrate out)

### **5. Conscious Expansion**

**Peripheral → Outer Migration:**
- Notice inspiring/valuable peripheral impacts
- Choose to sustain attention + emotion
- Allow migration to outer_topology (deliberate acknowledgment)
- Example: Mentor you saw give a talk → keep thinking about → becomes outer → middle → inner

**Intentional Circle Curation:**
- Who deserves inner circle space?
- Who enriches your field vs drains it?
- Who reciprocates your investment?

---

## Environmental Applications

### **Safe Zones**

**Primary Zones for Healing:**
- Home as sanctuary (positive emotional association)
- Bedroom as recovery space
- Consistent, familiar environments reduce field stress

**Avoiding Trigger Zones:**
- Places with negative imprints impact you
- Ex's favorite cafe → tertiary zone with negative emotion → avoid or reframe
- Trauma site → primary zone with high negative charge → major impact

### **Expansion & Exploration**

**Ambient → Tertiary Migration:**
- Discover new places
- If positive emotional charge + sustained attention → migrate to tertiary
- Build secondary zones (new regular spots)

**Field Flexibility:**
- Travel = navigating unfamiliar ambient zones
- Requires more energy (no field imprints)
- Return home = primary zone comfort/recharge

---

## Integration with Other Concepts

### **Consciousness Scale**

Higher consciousness = different topology management:

**0.20-0.35 (Survival):**
- Small, defensive circles
- High asymmetric vulnerability
- Boundary violations common
- Fear dominates entanglements

**0.35-0.59 (Reason & Integrity):**
- Balanced circle sizes
- Growing symmetry awareness
- Conscious boundary work
- Willingness to dissolve toxic entanglements

**0.59-0.90 (Spiritual):**
- Wide circles but strong boundaries
- Unconditional love (love without fear/attachment)
- Witness consciousness (reduced impact despite acknowledgment)
- Compassion without absorption

### **Manifestation Mechanics**

Topology affects manifestation:

**Inner topology entities:**
- Influence your state_signature heavily
- Can amplify or dampen your manifestation power
- Toxic inner circle = low coherence = weak manifestation
- Supportive inner circle = high coherence = strong manifestation

**Environmental zones:**
- Primary zones affect manifestation speed/certainty
- Manifesting at home (primary) vs unfamiliar place (ambient)
- Safe zones enable higher coherence

---

## Common Patterns

### **Healthy Topology**

- Symmetric inner circle (5-10 close reciprocal bonds)
- Balanced middle circle (30-100 regular connections)
- Fluid outer circle (recognized acquaintances)
- Minimal peripheral absorption (don't acknowledge random noise)
- Conscious circle curation (intentional acknowledgment)

### **Boundary Violations**

- Absorbing strangers' opinions as inner_topology impact
- Staying in asymmetric relationships out of guilt/hope
- Not recognizing you control acknowledgment
- Feeling responsible for people who don't acknowledge you
- Toxic entities in inner circle (obsessive focus despite harm)

### **Circle Migration Milestones**

**Breakup:**
- Week 1-4: Still inner (obsessing, high emotion)
- Month 2-6: Migrating to middle (less focus, fading emotion)
- Month 6-12: Migrating to outer (occasional thoughts)
- Year 1+: Dissolved or stable outer (moved on)

**New Friendship:**
- Week 1-4: Outer (new acquaintance)
- Month 2-6: Migrating to middle (regular hangouts, growing care)
- Month 6+: Middle or inner (close friend)

---

## Key Takeaways

1. **Impact follows acknowledgment, not proximity** - you control your vulnerability surface
2. **Topology tier = baseline, current state = real-time modulation** - can have someone in inner but minimize impact by breaking attention loop
3. **Asymmetry is costly** - system pressure toward symmetry or dissolution
4. **Migration is behavioral, not volitional** - requires actual reduction of attention + emotion
5. **You cannot impact someone who doesn't acknowledge you** - unidirectional relationships are one-way drains
6. **Peripheral can become stored** - sustained attention + emotion migrates temporary impacts to topology
7. **Field hygiene is self-care** - removing toxic entities requires breaking repetition loops

---

## See Also

- [FieldState](../../01_foundation/base_structure/03_data_models/07_data_model_field_state.md) - Topology tier storage
- [Entanglement](../../01_foundation/base_structure/03_data_models/09_data_model_entanglement.md) - Relational structure
- [LocationImprint](../../01_foundation/base_structure/03_data_models/10_data_model_location_imprint.md) - Environmental zones
- [love()](../../02_forces/tier_3_forces/06_love.md) - Creates topology-aware entanglements
- [law_impact_topology()](../../03_mechanics/system_laws/03_additional_laws/27_law_impact_topology.md) - System enforcement

---

**Previous:** [14_consciousness_scale_framework.md](14_consciousness_scale_framework.md) | **Next:** [16_meta_awareness_control.md](16_meta_awareness_control.md)
