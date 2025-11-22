# System Resource Allocation

**Agents have finite processing budgets (attention, energy, coherence capacity) allocated by the system.**

You cannot focus on everything simultaneously. Every conscious process consumes resources from a limited pool. Multitasking fragments coherence by splitting resources. Resource management is THE critical factor in manifestation power - coherent focus on single target = maximum resource allocation = fastest manifestation.

---

## Overview

Consciousness is not unlimited - it runs on finite computational resources. Like a computer with limited RAM, CPU cycles, and bandwidth, agents have **fixed processing capacity at any given moment**. This is not a flaw - it's an architectural constraint that ensures system stability.

---

## The Three Primary Resources

### 1. Attention Budget (Chi Allocation)

**What it is:** Limited conscious awareness bandwidth

**Capacity:** `consciousness_coefficient × 100` units

**Properties:**
- Can only hold ~4-7 items in active focus simultaneously
- Fragmented across multiple targets = weak signal per target
- Concentrated on single target = strong signal
- Master resource that directs energy and coherence allocation

**Depletion causes:**
- Decision fatigue (each choice consumes attention)
- Multitasking (splitting across targets)
- Novel stimuli (requires active processing)
- Sustained focus without rest

**Regeneration:**
- Full: Sleep (8 hours)
- Partial: Meditation, rest, low-stimulus environments
- Minimal: Time-based gradual recovery

---

### 2. Energy Budget (Metabolic/Field Capacity)

**What it is:** Physical and field broadcast power capacity

**Capacity:** `consciousness_coefficient × 100` units

**Properties:**
- Physical: Nervous system ATP, glucose, neurotransmitters
- Energetic: Field charge capacity, broadcast power
- Depletes with use, regenerates with rest
- Limited daily allocation

**Depletion causes:**
- Live processing (vs cached responses)
- Emotional intensity (high charge states)
- Physical exertion
- Stress/survival mode

**Regeneration:**
- Full: Sleep + nutrition
- Partial: Rest, nourishment, relaxation
- Activity-based: Certain activities regenerate (joy, flow states)

---

### 3. Coherence Budget (Processing Integrity)

**What it is:** Internal alignment capacity

**Capacity:** `consciousness_coefficient × 100` units

**Properties:**
- Maintaining conflicting beliefs costs coherence resources
- Resolving contradictions requires processing overhead
- Limited bandwidth for simultaneous coherent threads
- Determines manifestation signal quality

**Depletion causes:**
- Holding contradictory beliefs simultaneously
- Internal conflict (should vs want)
- Cognitive dissonance
- Fragmented intentions

**Regeneration:**
- Full: Resolving contradictions, belief alignment
- Partial: Meditation, coherence practices
- Minimal: Time-based gradual recovery

---

## Capacity Calculation

```python
def calculate_resource_capacity(agent: Agent) -> ResourcePool:
    """
    Calculate agent's maximum resource capacity

    Formula: consciousness_coefficient × 100 (linear scaling)
    """
    max_attention = agent.consciousness_coefficient * 100
    max_energy = agent.consciousness_coefficient * 100
    max_coherence = agent.consciousness_coefficient * 100

    return ResourcePool(
        max_attention=max_attention,
        max_energy=max_energy,
        max_coherence=max_coherence
    )

# Examples:
# 0.20 consciousness = 20 units each resource
# 0.50 consciousness = 50 units each resource
# 0.90 consciousness = 90 units each resource
```

**Key insight:** Higher consciousness = larger resource pool, but still FINITE.

---

## Resource Allocation Mechanics

### Multitasking Penalty (Linear Split)

```python
def allocate_attention(targets: List[Target], total_attention: float) -> Dict[Target, float]:
    """
    Attention splits linearly across targets

    N targets = total_attention / N per target
    """
    n_targets = len(targets)
    attention_per_target = total_attention / n_targets

    return {target: attention_per_target for target in targets}

# EXAMPLE 1: Focused (single target)
# 100 units / 1 target = 100 units per target → STRONG signal

# EXAMPLE 2: Multitasking (10 targets)
# 100 units / 10 targets = 10 units per target → WEAK signal per target
```

**Implication:** Multitasking reduces power per target proportionally. Ten intentions receive 1/10th the power each.

---

### Automatic vs Conscious Allocation

**Low consciousness (0.20-0.35):**
- Mostly automatic allocation (system controls)
- Survival processes get priority
- Limited conscious control

**Mid consciousness (0.43-0.59):**
- Partial conscious control (agent directs attention)
- System manages energy/coherence automatically
- Growing awareness of resource states

**High consciousness (0.69-0.90):**
- High conscious control (agent manages all resources)
- Can override automatic allocation
- Full awareness of resource states
- Strategic resource management

---

### Depletion Consequences (Graceful Degradation)

Performance decreases smoothly as resources deplete:

```python
def performance(current_resources: float, max_resources: float) -> float:
    """
    Performance degrades gracefully with resource depletion
    """
    resource_percentage = current_resources / max_resources

    if resource_percentage >= 0.80:
        return 1.0  # Peak performance
    elif resource_percentage >= 0.50:
        return 0.8  # Slight degradation
    elif resource_percentage >= 0.20:
        return 0.5  # Noticeable impairment
    else:
        return 0.2  # Severely impaired
```

**Observable effects:**
- Decision quality decreases
- Emotional regulation weakens
- Coherence drops (more internal conflict)
- Manifestation power reduces

---

## Regeneration Mechanics (Hybrid)

**Sleep (Full Regeneration):**
- 8 hours sleep = 100% restoration all resources
- Critical for sustained high performance
- Cannot be skipped without penalty

**Meditation (Partial Regeneration):**
- Attention: ~30% restoration per hour
- Coherence: ~40% restoration per hour
- Energy: ~20% restoration per hour

**Time (Minimal Regeneration):**
- Gradual recovery during low-demand activities
- ~5-10% per hour of rest
- Insufficient for sustained depletion

**Activity-Based (Selective):**
- Joy/flow states regenerate energy
- Problem-solving regenerates attention (in domain)
- Belief resolution regenerates coherence

---

## Social Vigilance Processing

Humans are fundamentally social predators AND social prey. Our main threats are other humans. Our main opportunities are other humans. Our survival depends on navigating human dynamics.

Therefore, agents run a **continuous background vigilance daemon** that monitors the social field for threats, opportunities, hierarchy shifts, coalitions, and betrayal potential.

This is not "relationship maintenance cost per entanglement." This is **survival processing of the social field.**

### The Vigilance Daemon

```python
def social_vigilance_daemon(agent: Agent) -> float:
    """
    Continuous background process monitoring social field

    Constantly assesses:
    - Threat detection: Who's dangerous? Who might harm me?
    - Opportunity detection: Who's valuable? Who can help me?
    - Hierarchy positioning: Where do I stand?
    - Coalition mapping: What alliances exist?
    - Betrayal potential: Who might turn on me?
    - Status tracking: Am I rising or falling?

    Returns: vigilance_load (0.0-1.0) - fraction of attention consumed
    """
    field_complexity = calculate_field_complexity(agent)      # 0.0-1.0
    stakes_intensity = calculate_stakes_intensity(agent)      # 0.0-1.0
    vigilance_factor = calculate_vigilance_factor(agent)      # 0.0-1.0

    vigilance_load = field_complexity × stakes_intensity × vigilance_factor

    return vigilance_load  # 0.0-1.0
```

**Key insight:** Runs as background process even when not consciously thinking about people. Survival-level threat/opportunity monitoring.

### Resource Consumption Model

**All coefficients use LACE's 0.0-1.0 scale.**

#### Field Complexity (0.0-1.0)

How complex is the social field to monitor?

```python
def calculate_field_complexity(agent: Agent) -> float:
    """
    Field complexity approaches 1.0 as topology fills
    Uses saturation function (never exceeds 1.0)
    """
    # Weighted contribution per tier
    inner_weight = 0.08   # Inner requires more monitoring
    middle_weight = 0.025 # Middle moderate monitoring
    outer_weight = 0.008  # Outer minimal monitoring

    # Sum entanglements weighted by attention_focus
    inner_load = sum(inner_weight × e.attention_focus
                    for e in agent.field_state.inner_topology)
    middle_load = sum(middle_weight × e.attention_focus
                     for e in agent.field_state.middle_topology)
    outer_load = sum(outer_weight × e.attention_focus
                    for e in agent.field_state.outer_topology)

    raw_complexity = inner_load + middle_load + outer_load

    # Saturate to 1.0 asymptotically
    field_complexity = 1.0 - (1.0 / (1.0 + raw_complexity))

    return field_complexity  # 0.0-1.0
```

**Examples:**
- Small field (3 inner, 10 middle, 20 outer): complexity = 0.32 (32%)
- Large field (10 inner, 40 middle, 80 outer): complexity = 0.635 (64%)
- Extreme field (15 inner, 60 middle, 120 outer): complexity = 0.723 (72%)

Field complexity saturates asymptotically - can't exceed 1.0, but grows harder to manage.

#### Stakes Intensity (0.0-1.0)

How high are the stakes in this social field?

```python
def calculate_stakes_intensity(agent: Agent) -> float:
    """
    Stakes based on threat/opportunity/power dynamics
    """
    threat_level = assess_environmental_threat(agent)        # 0.0-1.0
    opportunity_level = assess_opportunity_level(agent)      # 0.0-1.0
    power_differential = calculate_power_differential(agent) # 0.0-1.0

    stakes_intensity = (threat_level × 0.5 +
                       opportunity_level × 0.3 +
                       power_differential × 0.2)

    return stakes_intensity  # 0.0-1.0
```

**Examples:**
- Safe community: stakes = 0.29 (29% - low threat, good support)
- Toxic workplace: stakes = 0.815 (82% - high threat, high stakes)
- Casual gathering: stakes = 0.24 (24% - low threat, moderate opportunity)

#### Vigilance Factor (0.0-1.0)

Consciousness modulation of vigilance intensity.

```python
def calculate_vigilance_factor(agent: Agent) -> float:
    """
    Lower consciousness = higher vigilance (survival hypervigilance)
    Higher consciousness = lower vigilance (witness mode)
    """
    consciousness = agent.consciousness_coefficient  # 0.0-1.0

    if consciousness < 0.35:
        # Survival: High vigilance
        vigilance_factor = 1.0 - (consciousness × 0.5)
    elif consciousness < 0.69:
        # Reason: Moderate vigilance
        vigilance_factor = 1.0 - (consciousness × 0.6)
    else:
        # Spiritual: Reduced vigilance
        vigilance_factor = 0.9 - (consciousness × 0.5)

    return max(0.4, min(1.0, vigilance_factor))  # Clamped 0.4-1.0
```

**Examples:**
- consciousness = 0.20 → vigilance = 0.90 (90% - survival hypervigilance)
- consciousness = 0.50 → vigilance = 0.70 (70% - moderate)
- consciousness = 0.90 → vigilance = 0.45 (45% - witness mode)

### Complete Examples

```python
# EXAMPLE 1: Safe community, moderate consciousness
field_complexity = 0.32   # Small field
stakes_intensity = 0.29   # Low stakes
vigilance_factor = 0.70   # Moderate consciousness
vigilance_load = 0.32 × 0.29 × 0.70 = 0.065 (6.5% of attention budget)
# Result: Energizing environment

# EXAMPLE 2: Toxic workplace, moderate consciousness
field_complexity = 0.42   # Medium field
stakes_intensity = 0.815  # Very high stakes
vigilance_factor = 0.70   # Moderate consciousness
vigilance_load = 0.42 × 0.815 × 0.70 = 0.240 (24% of attention budget)
# Result: Significant continuous drain

# EXAMPLE 3: Extreme field, toxic environment, low consciousness
field_complexity = 0.723  # Very large field
stakes_intensity = 0.85   # Very toxic
vigilance_factor = 0.875  # Survival mode
vigilance_load = 0.723 × 0.85 × 0.875 = 0.538 (54% of attention budget)
# Result: Severe continuous drain
```

### What Vigilance Explains

**1. Social Exhaustion**

Not "too many people" - vigilance intensity matters.

Same 10 people:
- Low-stakes gathering: vigilance_load = 0.061 (6% - energizing)
- High-stakes work event: vigilance_load = 0.210 (21% - exhausting)

**3.4x difference** in resource drain for same field size.

**2. Toxic Environments**

Why they destroy you:

Small field (5 people), extremely toxic:
- vigilance_load = 0.230 (23% continuous drain)
- Plus active interaction costs
- Little left for manifestation, creativity, joy

**3. Introversion vs Extraversion**

Individual variation in vigilance sensitivity:

```python
# Optional agent property
vigilance_sensitivity: float  # 0.5-1.0

# Introvert: Higher sensitivity (1.0)
# Same field costs more to monitor
# Faster depletion, needs more recovery

# Extravert: Lower sensitivity (0.5)
# Same field costs less
# Slower depletion or regenerative processing
```

Not about social skill - about processing sensitivity.

**4. Relationship Capacity Limits**

Field complexity saturates toward 1.0 as field grows:

Very large field:
- raw_complexity = 3.265
- field_complexity = 0.766 (77%)

Natural emergence of capacity limits from resource constraints.

**5. Context Dependency**

Same people, different contexts = vastly different costs:

- Safe community: stakes = 0.25 (vigilance relaxed)
- Competitive environment: stakes = 0.85 (vigilance intense)

**3.4x difference** for identical field.

### Vigilance Overload

When vigilance_load > 0.7 (consuming >70% of attention budget):

**Resource starvation:**
```python
available_for_manifestation = max(0.0, 1.0 - vigilance_load)
available_for_decisions = max(0.0, 1.0 - vigilance_load)
```

Little remains for anything but survival monitoring.

**Chronic stress (if sustained):**
```python
if vigilance_load > 0.7:
    stress_level = min(1.0, (vigilance_load - 0.7) / 0.3)
    # Reduced regeneration
    # Health impacts
```

Creates natural pressure to reduce field complexity or change environmental stakes.

### Active Social Processing (Burst Costs)

Beyond continuous vigilance, active interaction includes:

**Agent State Simulation (Theory of Mind):**
- Temporarily modeling another agent's state_signature
- Predicting their actions/reactions
- Cost: Burst attention (0.2-0.5) + energy (0.2-0.4)
- Duration: Active simulation period

**Emotional Resonance Detection:**
- Reading field charge, sensing emotional states
- Cost: Attention (0.1-0.3) + energy (0.1-0.3) during interaction

**Coalition Strategy Processing:**
- Planning alliances, assessing betrayal risk
- Cost: Coherence (0.15-0.4) + attention (0.1-0.3)

All burst costs use 0.0-1.0 coefficients, consumed during active engagement.

---

## What This Explains

### 1. Why Multitasking Degrades Performance

Not about "ability" - about resource mathematics:
- 100 units spread across 10 tasks = 10 units each
- Weak signal per task = slow/no manifestation
- Fragmented coherence = poor outcomes

### 2. Why Decision Fatigue Is Real

Every decision consumes attention + energy:
- Morning: Full pool → decisions easy
- Evening: Depleted pool → decisions hard, avoid/defer
- Not "willpower" - actual resource exhaustion

### 3. Why Conflicting Beliefs Drain Energy

Maintaining contradictions costs coherence resources continuously:
- "I want love" + "I'm unlovable" = constant processing overhead
- System must reconcile conflict = resource drain
- Resolving contradiction = resources freed

### 4. Why Focus Is Manifestation Leverage

```python
# SCATTERED: 10 intentions × 10 units each = 10 weak broadcasts
# FOCUSED: 1 intention × 100 units = 1 MAXIMUM broadcast

# Manifestation power = resource concentration, not resource total
```

### 5. Why Sleep Deprivation Destroys Performance

Sleep = resource regeneration period:
- Deprivation = operating on depleted pool
- Observable: Impaired decisions, emotional volatility, memory issues
- Not "tiredness" - resource bankruptcy

---

## Resource Visibility

**Agents experience resources as:**

**Attention:** Felt as focus, clarity, mental sharpness
- High: "I feel clear, focused, present"
- Low: "I can't concentrate, scattered, foggy"

**Energy:** Felt as vitality, capacity, power
- High: "I feel energized, capable, strong"
- Low: "I'm exhausted, depleted, drained"

**Coherence:** Felt as alignment, integrity, peace
- High: "I feel aligned, certain, integrated"
- Low: "I feel conflicted, confused, torn"

**Note:** Agents at all consciousness levels FEEL resource states, but high consciousness agents can perceive and manage them consciously.

---

## Practical Applications

### Optimizing Resource Management

**Attention optimization:**
- Single-tasking (full resources to one target)
- Batching similar tasks (reduce switching costs)
- Scheduled focus blocks (protect concentration)

**Energy optimization:**
- Strategic rest (regenerate before depletion)
- Flow state cultivation (efficient resource use)
- Joy practices (activity-based regeneration)

**Coherence optimization:**
- Resolve contradictions (free ongoing costs)
- Simplify belief systems (reduce complexity)
- Align values with actions (minimize dissonance)

---

## Integration with Other Concepts

**System resource allocation connects to:**

- **[Perceptual Sampling Rate](19_perceptual_sampling_rate.md)** - Sampling consumes attention resources
- **[Cache vs Live Processing](21_cache_processing.md)** - Cached processing uses minimal resources, live processing maximum
- **[StateSignature](../../01_foundation/base_structure/03_data_models/05_data_model_state_signature.md)** - Coherence is both resource and metric
- **[Manifestation Engine](../../04_advanced/manifestation_engine/)** - Resource concentration determines manifestation power
- **[Consciousness Scale](14_consciousness_scale_framework.md)** - Resource capacity scales with consciousness

---

## Technical Implementation

For implementation details, see:
- **Agent data model** - ResourcePool structure
- **Resource Allocator daemon** - system-level resource management
- **Manifestation Engine** - power calculation using resource concentration

---

**Previous:** [19 Perceptual Sampling Rate](19_perceptual_sampling_rate.md) | **Next:** [21 Cache vs Live Processing](21_cache_processing.md)
