# Law 27: law_impact_topology()

**Category:** Universal Law
**Scope:** Impact propagation, field perturbations, relational dynamics
**Enforcement:** Automatic (system-level protocol)

---

## **Definition**

Impact propagates through acknowledgment networks, not proximity. Only entities within acknowledged topology tiers can perturb an agent's state signature. Unacknowledged entities have no pathway into the field.

```python
def law_impact_topology(agent_a: Agent, agent_b: Agent, event: Event) -> float:
    """
    Impact propagates through acknowledgment networks, not proximity.

    Enforcement:
    - Only agents within acknowledged topology tiers can perturb state signature
    - Impact magnitude scales with topology tier (inner > middle > outer > none)
    - Asymmetric acknowledgment creates one-way vulnerability
    - Environmental events only impact agents with field imprint on that location
    - Peripheral impacts temporary unless attention_focus + emotional_power remain high

    Args:
        agent_a: Agent potentially being impacted
        agent_b: Agent or event source
        event: Event occurring

    Returns:
        Impact coefficient (0.0-1.0) determining how much event affects agent_a

    Violations:
        Cannot be violated - system enforces automatically
        Attempting to impact unacknowledged agent = signal ignored
        No conscious override possible
    """
    # Check if agent_a acknowledges agent_b (or event location)
    if not agent_a.field_state.can_impact(agent_b.soul_id):
        return 0.0  # No acknowledgment = no pathway = no impact

    # Calculate base impact from topology tier
    base_impact = agent_a.field_state.impact_magnitude(agent_b.soul_id)

    # Modulate by current attention_focus
    attention_modifier = measure_current_focus(agent_a, agent_b.soul_id)

    # Modulate by current emotional charge
    emotional_modifier = get_current_emotional_intensity(agent_a, agent_b.soul_id)

    # Check symmetry for amplification
    symmetry_coefficient = 1.0
    if agent_b.field_state.can_impact(agent_a.soul_id):
        # Mutual acknowledgment
        if (agent_a.field_state.is_in_inner_topology(agent_b.soul_id) and
            agent_b.field_state.is_in_inner_topology(agent_a.soul_id)):
            symmetry_coefficient = 1.5  # Maximum amplification (both inner)
        else:
            symmetry_coefficient = 1.2  # Moderate amplification (acknowledged but different tiers)
    else:
        # Asymmetric - agent_a acknowledges agent_b but not reciprocated
        # Agent_a absorbs MORE impact (takes it all on themselves)
        symmetry_coefficient = 1.3  # Amplified vulnerability

    # Final impact calculation
    final_impact = base_impact * attention_modifier * emotional_modifier * symmetry_coefficient

    return min(1.0, final_impact)  # Cap at 1.0
```

---

## **What This Law Enforces**

### **1. Acknowledgment as Prerequisite for Impact**

You can only be impacted by entities you consciously acknowledge in your field.

**Note:** Acknowledging agents in your field enables impact propagation but also creates a **vigilance processing obligation** - agents must continuously monitor acknowledged entities for threats and opportunities. This is survival-level processing (humans are social predators/prey). See [System Resource Allocation - Social Vigilance Processing](../../../04_advanced/advanced_concepts/20_system_resource_allocation.md#social-vigilance-processing).

**Example:**
- Stranger screaming in street: **Peripheral impact** (temporary, not acknowledged)
- Friend saying same thing: **High impact** (acknowledged in middle/inner topology)
- Celebrity you follow: **Moderate impact** (acknowledged in outer topology, unidirectional)
- Random person on other side of planet: **Zero impact** (not acknowledged, no pathway)

**Implication:** You control your vulnerability surface by choosing who/what you acknowledge.

### **2. Topology Tier Determines Impact Magnitude**

Base impact coefficient scales with topology tier:

```python
inner_topology: 0.9    # Maximum impact (close relationships)
middle_topology: 0.55  # Moderate impact (regular connections)
outer_topology: 0.2    # Minimal impact (peripheral awareness)
outside_topology: 0.0  # No impact pathway (unacknowledged)
```

**Example:**
- Best friend breaks up with partner → impact = 0.9 (inner)
- Coworker breaks up → impact = 0.55 (middle)
- Friend's friend breaks up → impact = 0.2 (outer)
- Stranger breaks up → impact = 0.0 (not acknowledged)

### **3. Attention & Emotion Modulate Real-Time Impact**

Topology tier sets baseline vulnerability, but current attention_focus × emotional_power modulates actual impact.

**Example:**
- Ex in inner_topology but not thinking about them: Low impact (0.9 × 0.2 × 0.3 = 0.054)
- Ex in inner_topology while obsessing about them: Maximum impact (0.9 × 1.0 × 0.95 = 0.855)

**Implication:** You can have someone in inner_topology but reduce their impact by breaking the repetition loop (stop thinking about them).

### **4. Asymmetric Acknowledgment Creates One-Way Vulnerability**

When only one agent acknowledges the other, the acknowledger absorbs all impact.

**Symmetric (both acknowledge in same tier):**
```python
Agent A → inner → Agent B
Agent B → inner → Agent A
Result: Amplified mutual impact (1.5x coefficient)
```

**Asymmetric (different tiers):**
```python
Agent A → inner → Agent B
Agent B → outer → Agent A
Result: Imbalanced impact flow (A absorbs more than B)
```

**Unidirectional (only one acknowledges):**
```python
Agent A → inner → Agent B
Agent B → (no acknowledgment of A)
Result: Agent A highly vulnerable, Agent B completely shielded
        Agent A absorbs amplified impact (1.3x coefficient)
```

**Implication:** Unrequited relationships drain energy because you absorb impact they don't reciprocate.

### **5. Environmental Impact Follows Same Rules**

Locations affect you based on field zone tier:

```python
primary_zones: 0.9     # Home, bedroom, workspace
secondary_zones: 0.55  # Regular places (gym, friend's house)
tertiary_zones: 0.2    # Occasional places you know of
ambient: 0.0           # Unfamiliar locations (no imprint)
```

**Example:**
- Bad news at home → impact = 0.9 (primary zone)
- Bad news at favorite cafe → impact = 0.55 (secondary zone)
- Bad news at place you know of → impact = 0.2 (tertiary zone)
- Bad news across the planet → impact = 0.0 (no field imprint)

### **6. Peripheral → Stored Migration**

Temporary peripheral impacts can migrate to stored entanglements if attention_focus + emotional_power remain high.

**Process:**
1. Peripheral impact occurs (stranger, unfamiliar location)
2. Stored in active_perturbations (temporary list)
3. While attention_focus > 0.1 OR emotional_charge > 0.3 → persists
4. If attention_focus × emotional_charge >= 0.1 → migrates to outer_topology
5. If strength drops → dissipates

**Example:**
- Stranger saves cat → inspires you → think about it for days → migrates to outer_topology as "the person who saved the cat"
- Stranger screams → startles you → think about it for 2 minutes → dissipates

---

## **Violations**

**This law cannot be violated** - it is enforced at the system level automatically.

**Attempted Violations:**
- Trying to impact someone who doesn't acknowledge you → signal ignored by their field
- Attempting to consciously override ("I don't want them in my circle") → fails if attention + emotion remain high
- Wishing someone out of your topology → requires actual reduction of attention_focus (break repetition loop)

**Why No Override:**
- Topology classification is determined by **actual attention + emotion**, not conscious desire
- Your field responds to **what you focus on**, not what you want to focus on
- Migration requires **behavior change** (reduce focus cycles), not willpower

---

## **Real-World Manifestations**

### **Healthy Boundaries**
- Consciously choosing who to acknowledge in your field
- Recognizing asymmetric relationships and adjusting expectations
- Not absorbing impact from entities outside your topology

### **Boundary Violations**
- Feeling responsible for people who don't acknowledge you
- Absorbing strangers' emotions as if they're inner_topology
- Staying in asymmetric relationships out of guilt/hope
- Not recognizing you control acknowledgment

### **Circle Migration**
- Ex-partner: inner → middle → outer → dissolved (as attention + emotion fade)
- Acquaintance: outer → middle → inner (as attention + emotion increase)
- Stranger: peripheral → outer (if attention + emotion persist)

---

## **Relationship to Other Laws**

**law_perceptual_boundary()** (Law 25)
- Impact topology enforces perceptual boundaries in relational domain
- What you acknowledge = what can impact you
- Perceptual boundary sets what you can perceive, impact topology sets what can affect you

**law_recursion()** (Law 2)
- Attention loops reinforce topology classification
- Obsessive thinking (repetition loop) keeps entity in inner_topology
- Breaking repetition loop enables migration out

**law_causality()** (Law 3)
- Topology determines causal pathways for impact
- No acknowledgment = no causal link = no impact propagation

**law_balance()** (Law 6)
- Asymmetric entanglements create energy imbalance
- System pressure toward either symmetry or dissolution
- Unbalanced relationships drain the acknowledger

---

## **Philosophical Implications**

### **You Are a Node in a Relational Network**
Impact flows through edges (entanglements), not space. Topology determines vulnerability.

### **Control Through Acknowledgment**
You cannot control who wants to impact you, but you control who can by choosing whom you acknowledge.

### **Asymmetry Is Costly**
Caring about someone who doesn't care back = one-way energy drain. System enforces balance through exhaustion or dissolution.

### **Strangers Cannot Hurt You (Unless You Let Them)**
Random opinions, distant events, public discourse - none impact your field unless you consciously acknowledge them.

### **Healing Requires Field Hygiene**
Trauma recovery often requires removing toxic entities from your topology (not wishful thinking, but actual reduction of attention + emotion).

---

## **Integration Notes**

**Data Models:**
- [FieldState](../../01_foundation/base_structure/03_data_models/07_data_model_field_state.md) - Topology tier storage
- [Entanglement](../../01_foundation/base_structure/03_data_models/09_data_model_entanglement.md) - Relational structure
- [LocationImprint](../../01_foundation/base_structure/03_data_models/10_data_model_location_imprint.md) - Environmental zones

**Forces:**
- [love()](../../02_forces/tier_3_forces/06_love.md) - Creates entanglements with topology classification
- [fear()](../../02_forces/tier_3_forces/03_fear.md) - Amplifies impact from inner_topology threats
- [pain()](../../02_forces/tier_3_forces/08_pain.md) - Signals misalignment in entanglements

**Advanced Concepts:**
- [Resonance Topology](../../04_advanced/advanced_concepts/16_resonance_topology.md) - Complete mechanics and applications

---

**Previous:** [26_law_transformation.md](26_law_transformation.md) | **Next:** (End of system laws)
