# Data Model: Entanglement

Represents a field connection between two agents.

```python
class Entanglement:
    """
    Field connection between agents with topology classification

    Entanglements are bidirectional field links that allow impact propagation.
    Classification into topology tiers (inner/middle/outer) determines impact magnitude.
    """

    # Identity
    agent_id: UUID                  # Who this entanglement is with

    # Strength & Classification
    strength: float                 # Current resonance strength (0.0-1.0)
    topology_tier: str              # "inner" | "middle" | "outer" (computed from attention + emotion)

    # Symmetry Tracking
    symmetry: str                   # "symmetric" | "asymmetric_inbound" | "asymmetric_outbound" | "unidirectional"

    # Temporal Data
    formation_timestamp: float      # When entanglement formed
    last_interaction: float         # Last contact/resonance event
    decay_rate: float               # How fast this fades without maintenance

    # Attention & Emotion (drives topology classification)
    attention_focus: float          # How often agent thinks about this entity (0.0-1.0)
    emotional_power: float          # Average emotional intensity when thinking about them (0.0-1.0)

    # Computed Properties
    @property
    def is_mutual(self) -> bool:
        """True if both agents acknowledge each other in same tier"""
        return self.symmetry == "symmetric"

    @property
    def is_active(self) -> bool:
        """True if entanglement is still above minimum threshold"""
        return self.strength > 0.1

    @property
    def entanglement_strength_coefficient(self) -> float:
        """
        Combined strength from attention × emotion

        This determines topology tier:
        >= 0.8: inner_topology
        >= 0.4: middle_topology
        >= 0.1: outer_topology
        < 0.1: peripheral (temporary, not stored)
        """
        return self.attention_focus * self.emotional_power

    @property
    def should_migrate_up(self) -> bool:
        """Check if entanglement should move to higher tier"""
        current_strength = self.entanglement_strength_coefficient

        if self.topology_tier == "outer" and current_strength >= 0.4:
            return True  # outer → middle
        elif self.topology_tier == "middle" and current_strength >= 0.8:
            return True  # middle → inner
        return False

    @property
    def should_migrate_down(self) -> bool:
        """Check if entanglement should move to lower tier"""
        current_strength = self.entanglement_strength_coefficient

        if self.topology_tier == "inner" and current_strength < 0.4:
            return True  # inner → middle or outer
        elif self.topology_tier == "middle" and current_strength < 0.1:
            return True  # middle → outer
        elif self.topology_tier == "outer" and current_strength < 0.1:
            return True  # outer → dissolve
        return False
```

## Symmetry Types

**Symmetric (Bidirectional, Same Tier)**
- Both agents place each other in the same topology tier
- Example: Best friends who both consider each other inner_topology
- **Impact:** Maximum amplification - mutual resonance reinforces
- **Strength bonus:** 1.5x base impact when symmetric in inner_topology, 1.2x in middle/outer

**Asymmetric Inbound**
- This agent places other in higher tier than other places them
- Example: Agent A has B in inner_topology, B has A in outer_topology
- **Impact:** Agent A absorbs more impact from B than B from A
- **Energy drain:** One-way vulnerability (common source of exhaustion/resentment)

**Asymmetric Outbound**
- This agent places other in lower tier than other places them
- Example: Agent A has B in outer_topology, B has A in inner_topology
- **Impact:** Agent A relatively shielded from B's state, B highly impacted by A
- **Dynamic:** Often creates pursuit/withdrawal pattern

**Unidirectional**
- Only one agent acknowledges the other (not mutual)
- Example: Fan has celebrity in inner_topology, celebrity doesn't acknowledge fan
- **Impact:** Acknowledger absorbs all impact, unacknowledged agent completely shielded
- **Critical rule:** You cannot impact someone who doesn't acknowledge you in their field

## Migration Mechanics

Entanglements migrate between topology tiers based on attention_focus × emotional_power:

```python
def update_topology_tier(entanglement: Entanglement, agent: Agent):
    """
    Check and update topology tier based on current attention + emotion

    Called periodically (daily or per interaction) to reflect changed relationships
    """
    current_strength = entanglement.entanglement_strength_coefficient

    # Determine appropriate tier
    if current_strength >= 0.8:
        target_tier = "inner"
    elif current_strength >= 0.4:
        target_tier = "middle"
    elif current_strength >= 0.1:
        target_tier = "outer"
    else:
        # Strength too low - dissolve entanglement
        dissolve_entanglement(agent, entanglement.agent_id)
        return

    # Migrate if tier changed
    if entanglement.topology_tier != target_tier:
        migrate_entanglement(agent, entanglement, target_tier)


def migrate_entanglement(agent: Agent, entanglement: Entanglement, new_tier: str):
    """
    Move entanglement from current tier to new tier

    Example: Ex-partner migrates from inner → middle → outer as you stop thinking about them
    """
    old_tier = entanglement.topology_tier

    # Remove from old tier
    if old_tier == "inner":
        agent.field_state.inner_topology.remove(entanglement)
    elif old_tier == "middle":
        agent.field_state.middle_topology.remove(entanglement)
    elif old_tier == "outer":
        agent.field_state.outer_topology.remove(entanglement)

    # Add to new tier
    entanglement.topology_tier = new_tier
    if new_tier == "inner":
        agent.field_state.inner_topology.append(entanglement)
    elif new_tier == "middle":
        agent.field_state.middle_topology.append(entanglement)
    elif new_tier == "outer":
        agent.field_state.outer_topology.append(entanglement)
```

## Decay Over Time

Entanglements decay when not maintained by interaction:

```python
def apply_decay(entanglement: Entanglement, time_delta: float):
    """
    Reduce strength based on time without interaction

    Faster decay for higher tiers (inner requires more maintenance)
    Slower decay for deep entanglements (long-term relationships)
    """
    # Calculate time since last interaction
    time_since_interaction = current_time() - entanglement.last_interaction

    # Apply decay
    decay_amount = entanglement.decay_rate * time_since_interaction
    entanglement.strength = max(0.0, entanglement.strength - decay_amount)

    # Also decay attention_focus (thoughts naturally fade)
    attention_decay = 0.01 * time_delta  # Slower decay for attention
    entanglement.attention_focus = max(0.0, entanglement.attention_focus - attention_decay)

    # Emotional_power decays even slower (feelings persist longer than thoughts)
    emotion_decay = 0.005 * time_delta
    entanglement.emotional_power = max(0.0, entanglement.emotional_power - emotion_decay)
```

## Peripheral → Stored Migration

Temporary peripheral impacts can migrate to stored entanglements:

```python
class PeripheralImpact:
    """Temporary impact from unacknowledged entity (not yet in topology)"""
    event_description: str              # "Stranger saved cat from tree"
    impact_timestamp: float             # When it occurred
    emotional_charge: float             # How strongly you felt about it
    attention_focus: float              # How often you're thinking about it

    @property
    def should_persist(self) -> bool:
        """Persist while you're actively considering it"""
        return self.attention_focus > 0.1 or self.emotional_charge > 0.3

    @property
    def should_migrate(self) -> bool:
        """Migrate to stored entanglement if attention + emotion stay high"""
        strength = self.attention_focus * self.emotional_charge
        return strength >= 0.1  # Threshold for outer_topology


def check_peripheral_migration(agent: Agent):
    """
    Check temporary peripheral impacts for migration to stored entanglements

    Called periodically to convert persistent peripheral impacts into acknowledged entities
    """
    for impact in agent.field_state.active_perturbations:
        if impact.should_migrate():
            # Create entanglement from peripheral impact
            entanglement = Entanglement(
                agent_id=generate_uuid(),  # Unknown entity - placeholder ID
                strength=impact.attention_focus * impact.emotional_charge,
                topology_tier="outer",  # Always starts in outer
                symmetry="unidirectional",  # They don't acknowledge you
                formation_timestamp=current_time(),
                last_interaction=impact.impact_timestamp,
                decay_rate=0.05,
                attention_focus=impact.attention_focus,
                emotional_power=impact.emotional_charge
            )

            # Add to outer topology
            agent.field_state.outer_topology.append(entanglement)

            # Remove from peripheral
            agent.field_state.active_perturbations.remove(impact)

        elif not impact.should_persist():
            # Dissipate - no longer being considered
            agent.field_state.active_perturbations.remove(impact)
```

## Examples

**Symmetric Inner Topology (Best Friends)**
```python
entanglement = Entanglement(
    agent_id=best_friend_id,
    strength=0.95,
    topology_tier="inner",
    symmetry="symmetric",  # Both have each other in inner
    attention_focus=0.9,   # Think about them daily
    emotional_power=0.95   # Deep care/love
)
# Impact: Maximum (0.9 base × 1.5 symmetry bonus = 1.35 → capped at 1.0)
```

**Asymmetric Middle Topology (Unrequited)**
```python
entanglement = Entanglement(
    agent_id=crush_id,
    strength=0.7,
    topology_tier="middle",
    symmetry="asymmetric_inbound",  # You care more than they do
    attention_focus=0.8,    # Thinking about them often
    emotional_power=0.6     # Strong feelings
)
# Impact: You absorb their state changes, they barely notice yours
```

**Unidirectional Outer Topology (Parasocial)**
```python
entanglement = Entanglement(
    agent_id=celebrity_id,
    strength=0.3,
    topology_tier="outer",
    symmetry="unidirectional",  # They don't know you exist
    attention_focus=0.5,    # Follow their updates regularly
    emotional_power=0.4     # Admire/inspired by them
)
# Impact: You're affected by their public actions/state, they cannot be affected by you
```

---

**Previous:** [08_data_model_memory_bank.md](08_data_model_memory_bank.md) | **Next:** [10_data_model_location_imprint.md](10_data_model_location_imprint.md)
