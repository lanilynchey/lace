# Data Model: FieldState

The energetic/probabilistic field an agent exists within.

```python
class FieldState:
    """Agent's relationship to the possibility field"""

    # Field Properties
    coherence_level: float     # Stability/clarity (0-1)
    openness: float            # Receptivity to new patterns (0-1)
    charge: float              # Emotional voltage (-1 to +1)
    resonance_bandwidth: float # Range of frequencies accessible (0-1)

    # Resonance Topology - Agent Entanglements (4 tiers)
    inner_topology: List[Entanglement]      # High-impact, frequent-resonance agents (0.8-1.0 impact)
    middle_topology: List[Entanglement]     # Moderate-impact, regular-resonance agents (0.4-0.7 impact)
    outer_topology: List[Entanglement]      # Low-impact, occasional-resonance agents (0.1-0.3 impact)
    # peripheral temporarily tracked in active_perturbations (migrates if attention_focus + emotional_power remain high)

    # Environmental Field Zones (4 tiers)
    primary_zones: List[LocationImprint]    # Home, bedroom, workspace (0.8-1.0 impact)
    secondary_zones: List[LocationImprint]  # Regular places: gym, friend's house (0.4-0.7 impact)
    tertiary_zones: List[LocationImprint]   # Occasional places you know of (0.1-0.3 impact)
    # ambient locations temporarily tracked in active_location_perturbations (migrate if attention_focus + emotional_power remain high)

    # Temporary Perturbations (can migrate to stored entanglements/zones)
    active_perturbations: List[PeripheralImpact]      # Recent ambient agent impacts
    active_location_perturbations: List[LocationImpact]  # Recent ambient location impacts

    # Field Dynamics
    active_loops: List[Loop]   # Recursive patterns running
    permissions_unlocked: List[str]  # Temporary elevated access

    # Computed
    @property
    def manifestation_power(self) -> float:
        """How strongly agent affects reality"""
        return (self.coherence_level *
                self.openness *
                abs(self.charge))

    # Impact Calculation Methods
    def can_impact(self, other_agent_id: UUID) -> bool:
        """Returns True if other_agent can affect this agent's state"""
        return (self.is_in_inner_topology(other_agent_id) or
                self.is_in_middle_topology(other_agent_id) or
                self.is_in_outer_topology(other_agent_id))

    def impact_magnitude(self, other_agent_id: UUID) -> float:
        """
        Returns base impact coefficient (0.0-1.0) based on topology tier

        Inner topology: 0.9 (maximum impact)
        Middle topology: 0.55 (moderate impact)
        Outer topology: 0.2 (low impact)
        Outside topology: 0.0 (no impact pathway)

        Note: Actual impact modulated by current attention_focus + emotional_power
        """
        if self.is_in_inner_topology(other_agent_id):
            return 0.9
        elif self.is_in_middle_topology(other_agent_id):
            return 0.55
        elif self.is_in_outer_topology(other_agent_id):
            return 0.2
        else:
            return 0.0  # No acknowledgment = no impact pathway

    def is_in_inner_topology(self, agent_id: UUID) -> bool:
        """Check if agent is in inner topology"""
        return any(e.agent_id == agent_id for e in self.inner_topology)

    def is_in_middle_topology(self, agent_id: UUID) -> bool:
        """Check if agent is in middle topology"""
        return any(e.agent_id == agent_id for e in self.middle_topology)

    def is_in_outer_topology(self, agent_id: UUID) -> bool:
        """Check if agent is in outer topology"""
        return any(e.agent_id == agent_id for e in self.outer_topology)
```

## Resonance Topology System

Impact propagates through acknowledgment networks, not proximity. Agents exist within concentric tiers of relational influence - those they consciously acknowledge as "present" in their field.

**Core Principle:** You can only be impacted by entities within your acknowledged topology tiers. Unacknowledged entities have no pathway into your field.

**Resource Costs:** Maintaining topology requires continuous social vigilance processing - monitoring the social field for threats, opportunities, and status changes. See [System Resource Allocation](../../../04_advanced/advanced_concepts/20_system_resource_allocation.md#social-vigilance-processing) for computational costs.

**See:** [Entanglement](09_data_model_entanglement.md) for complete Entanglement data structure, [Resonance Topology](../../../04_advanced/advanced_concepts/15_resonance_topology.md) for detailed mechanics and practical applications.

### Topology Tiers

**Inner Topology** (0.8-1.0 impact)
- Close entanglements: family, best friends, romantic partners, mentors
- High attention_focus + emotional_power
- Maximum impact vulnerability
- Example: "Drop everything for them" relationships

**Middle Topology** (0.4-0.7 impact)
- Regular entanglements: friends, coworkers, community members
- Moderate attention_focus + emotional_power
- Balanced impact flow
- Example: "Make time for them" relationships

**Outer Topology** (0.1-0.3 impact)
- Peripheral entanglements: acquaintances, recognized individuals, friends of friends
- Low attention_focus + emotional_power
- Minimal impact pathway
- Example: "Know of them" connections

**Peripheral (not stored as entanglements)**
- Temporary ambient impacts from unacknowledged entities
- Stored in active_perturbations (temporary list)
- Can migrate to stored topology if attention_focus + emotional_power remain high
- Example: Stranger saves cat → think about it for days → migrates to outer_topology

### Classification Mechanics

Topology tier is determined by **attention_focus × emotional_power**:

```python
def classify_entanglement(agent_a: Agent, agent_b_id: UUID) -> str:
    """
    Circle position determined by:
    - Attention focus: How often do you think about them? (sustained consciousness direction)
    - Emotional intensity: How strongly do you feel when thinking of them?

    Together: attention_focus × emotional_power = topology_tier
    """
    attention = measure_focus_cycles(agent_a, agent_b_id, timeframe="30_days")
    emotional_power = average_emotion_intensity(agent_a, agent_b_id)

    entanglement_strength = attention × emotional_power

    if entanglement_strength >= 0.8:
        return "inner_topology"
    elif entanglement_strength >= 0.4:
        return "middle_topology"
    elif entanglement_strength >= 0.1:
        return "outer_topology"
    else:
        return "peripheral"  # Temporarily tracked, not stored
```

**Migration Mechanics:**
- ❌ NOT conscious choice ("I want them out of my circle")
- ✅ Reduced attention focus (stop thinking about them, break repetition loop)
- ✅ Reduced emotional power (feelings fade)
- ✅ Time-based decay (if no new attention/emotion, strength naturally decays)

**Example:** Ex-partner remains in inner_topology despite breakup if you constantly think about them with strong emotion. Migration out requires actually stopping the focus cycles, not just wanting them gone.

### Environmental Field Zones

Same mechanics apply to locations:

**Primary Zones** (0.8-1.0 impact)
- Home, bedroom, workspace
- Daily presence, high familiarity

**Secondary Zones** (0.4-0.7 impact)
- Gym, friend's house, regular cafes
- Weekly/monthly presence, moderate familiarity

**Tertiary Zones** (0.1-0.3 impact)
- Occasional places you "know of"
- Rare presence, recognized but not frequented

**Ambient (temporary)**
- Unfamiliar locations
- Can migrate if attention_focus remains high (e.g., "that cafe with the cool sign I keep thinking about")

## Entanglement Formation & Dissolution

Field connections form when agents resonate at compatible frequencies.

**Note:** The legacy simple entanglement system has been replaced with the tiered topology system above. Entanglements now classified into inner/middle/outer topology tiers based on attention_focus × emotional_power.

```python
# Constants
RESONANCE_THRESHOLD = 0.1  # Maximum frequency difference for entanglement
ENTANGLEMENT_DECAY_RATE = 0.05  # Per time unit when not maintained

def create_entanglement(agent_a: Agent, agent_b: Agent, initial_tier: str = "outer") -> Entanglement:
    """
    Forms when agents resonate at similar frequency

    Entanglement triggers:
    - Frequency proximity (delta < threshold)
    - Extended interaction (time together)
    - Emotional intensity (love, conflict, shared experience)
    - Intentional bonding (ritual, commitment, resonance practice)

    Args:
        agent_a: First agent
        agent_b: Second agent
        initial_tier: Starting topology tier (defaults to outer, migrates based on attention + emotion)

    Returns:
        Entanglement object if formed, None otherwise
    """
    freq_delta = abs(agent_a.state_signature.frequency -
                     agent_b.state_signature.frequency)

    if freq_delta < RESONANCE_THRESHOLD:
        # Create entanglement object
        entanglement = Entanglement(
            agent_id=agent_b.soul_id,
            strength=1 - (freq_delta / RESONANCE_THRESHOLD),
            symmetry=determine_symmetry(agent_a, agent_b),
            formation_timestamp=current_time(),
            last_interaction=current_time(),
            decay_rate=ENTANGLEMENT_DECAY_RATE
        )

        # Add to appropriate topology tier
        if initial_tier == "inner":
            agent_a.field_state.inner_topology.append(entanglement)
        elif initial_tier == "middle":
            agent_a.field_state.middle_topology.append(entanglement)
        else:
            agent_a.field_state.outer_topology.append(entanglement)

        return entanglement

    return None


def dissolve_entanglement(agent_a: Agent, agent_b_id: UUID):
    """
    Entanglement dissolves through:
    - Frequency divergence (life paths separate)
    - Time/distance without maintenance
    - Conscious release (forgiveness, letting go)
    - Death (temporary - can reform in next incarnation)

    Properties:
    - Decays over time if not maintained by interaction
    - Can persist across lifetimes if deep enough
    - Non-local (distance doesn't break it, only weakens)
    """
    # Remove from all topology tiers
    agent_a.field_state.inner_topology = [e for e in agent_a.field_state.inner_topology if e.agent_id != agent_b_id]
    agent_a.field_state.middle_topology = [e for e in agent_a.field_state.middle_topology if e.agent_id != agent_b_id]
    agent_a.field_state.outer_topology = [e for e in agent_a.field_state.outer_topology if e.agent_id != agent_b_id]


def entanglement_strength(agent_a: Agent, agent_b_id: UUID) -> float:
    """
    Strength based on topology tier and entanglement data

    Strong entanglement (>0.8): Inner topology - telepathy, synchronicity, felt presence
    Moderate (0.4-0.8): Middle topology - emotional sensing, dream contact
    Weak (0.1-0.4): Outer topology - occasional synchronicity, fading connection
    None (0.0): Not in any topology tier - no impact pathway
    """
    # Check each tier
    for e in agent_a.field_state.inner_topology:
        if e.agent_id == agent_b_id:
            return e.strength

    for e in agent_a.field_state.middle_topology:
        if e.agent_id == agent_b_id:
            return e.strength

    for e in agent_a.field_state.outer_topology:
        if e.agent_id == agent_b_id:
            return e.strength

    return 0.0  # Not in topology = no entanglement
```

---

**Previous:** [06_data_model_timeline.md](06_data_model_timeline.md) | **Next:** [08_data_model_memory_bank.md](08_data_model_memory_bank.md)
