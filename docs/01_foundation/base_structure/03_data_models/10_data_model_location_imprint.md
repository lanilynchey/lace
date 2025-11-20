# Data Models: LocationImprint & LocationImpact

Environmental field zones - how locations impact agents based on familiarity and emotional association.

## LocationImprint

Stored field zone with encoded familiarity (primary/secondary/tertiary zones).

```python
class LocationImprint:
    """
    Stored environmental field zone

    Locations encoded in agent's field based on visit frequency + emotional association + attention focus.
    Similar mechanics to agent entanglements - impact magnitude determined by tier classification.
    """

    # Identity
    location_id: UUID                   # Unique identifier for this location
    location_name: str                  # Human-readable name ("Home", "Mom's house", "Favorite cafe")
    coordinates: Optional[Coordinates]  # Physical location (optional - can be conceptual)

    # Field Classification
    zone_tier: str                      # "primary" | "secondary" | "tertiary" (computed from visit + emotion + attention)
    field_strength: float               # Overall impact rating (0.0-1.0)

    # Visit Patterns
    visit_frequency: float              # How often you go there (0.0-1.0)
    last_visit: float                   # Timestamp of last visit
    total_time_spent: float             # Cumulative time at this location

    # Emotional Encoding
    emotional_association: float        # How you feel about it (-1.0 to +1.0)
    dominant_emotions: List[str]        # ["safe", "creative", "anxious"] - emotional signature

    # Attention & Memory
    attention_focus: float              # How often you think about it (0.0-1.0)
    memory_strength: float              # How vividly you remember it (0.0-1.0)

    # Temporal Data
    first_encoded: float                # When this location first entered your field
    decay_rate: float                   # How fast this fades without visits

    # Computed Properties
    @property
    def zone_strength_coefficient(self) -> float:
        """
        Combined strength from visit_frequency × emotional_association × attention_focus

        Determines zone tier:
        >= 0.8: primary_zone
        >= 0.4: secondary_zone
        >= 0.1: tertiary_zone
        < 0.1: ambient (temporary, not stored)
        """
        return (visit_frequency * 0.4 +
                abs(emotional_association) * 0.3 +
                attention_focus * 0.3)

    @property
    def impact_magnitude(self) -> float:
        """Base impact from zone tier"""
        if self.zone_tier == "primary":
            return 0.9
        elif self.zone_tier == "secondary":
            return 0.55
        elif self.zone_tier == "tertiary":
            return 0.2
        else:
            return 0.0

    @property
    def is_safe_zone(self) -> bool:
        """True if emotional association is positive and strong"""
        return self.emotional_association > 0.6 and self.field_strength > 0.5

    @property
    def is_trigger_zone(self) -> bool:
        """True if emotional association is negative and strong"""
        return self.emotional_association < -0.6 and self.field_strength > 0.5

    @property
    def should_migrate_up(self) -> bool:
        """Check if location should move to higher tier"""
        current_strength = self.zone_strength_coefficient

        if self.zone_tier == "tertiary" and current_strength >= 0.4:
            return True  # tertiary → secondary
        elif self.zone_tier == "secondary" and current_strength >= 0.8:
            return True  # secondary → primary
        return False

    @property
    def should_migrate_down(self) -> bool:
        """Check if location should move to lower tier"""
        current_strength = self.zone_strength_coefficient

        if self.zone_tier == "primary" and current_strength < 0.4:
            return True  # primary → secondary or tertiary
        elif self.zone_tier == "secondary" and current_strength < 0.1:
            return True  # secondary → tertiary
        elif self.zone_tier == "tertiary" and current_strength < 0.1:
            return True  # tertiary → dissolve
        return False
```

## LocationImpact

Temporary impact from unfamiliar location (ambient zone, not yet stored).

```python
class LocationImpact:
    """
    Temporary environmental impact from unfamiliar location

    Similar to PeripheralImpact for agents - can migrate to stored LocationImprint
    if attention_focus + emotional_charge remain high.
    """

    # Description
    location_description: str           # "That cafe with the cool sign"
    coordinates: Optional[Coordinates]  # If known

    # Impact Data
    impact_timestamp: float             # When you encountered it
    emotional_charge: float             # How strongly you felt about it (0.0-1.0)
    attention_focus: float              # How often you're thinking about it (0.0-1.0)

    # Context
    event_description: Optional[str]    # What happened there ("Saw amazing street art")
    sensory_details: Optional[Dict]     # Visual/auditory/olfactory memories

    # Computed Properties
    @property
    def should_persist(self) -> bool:
        """Persist while you're actively considering it"""
        return self.attention_focus > 0.1 or self.emotional_charge > 0.3

    @property
    def should_migrate(self) -> bool:
        """Migrate to stored zone if attention + emotion stay high"""
        strength = self.attention_focus * self.emotional_charge
        return strength >= 0.1  # Threshold for tertiary_zone

    @property
    def location_strength_coefficient(self) -> float:
        """Combined strength for migration calculation"""
        return self.attention_focus * self.emotional_charge
```

## Migration Mechanics

Locations migrate between zone tiers based on visit frequency + emotional association + attention focus:

```python
def update_zone_tier(location: LocationImprint, agent: Agent):
    """
    Check and update zone tier based on current visit/emotion/attention patterns

    Called after each visit or periodically to reflect changed relationships with places
    """
    current_strength = location.zone_strength_coefficient

    # Determine appropriate tier
    if current_strength >= 0.8:
        target_tier = "primary"
    elif current_strength >= 0.4:
        target_tier = "secondary"
    elif current_strength >= 0.1:
        target_tier = "tertiary"
    else:
        # Strength too low - dissolve location imprint
        dissolve_location_imprint(agent, location.location_id)
        return

    # Migrate if tier changed
    if location.zone_tier != target_tier:
        migrate_location(agent, location, target_tier)


def migrate_location(agent: Agent, location: LocationImprint, new_tier: str):
    """
    Move location from current tier to new tier

    Example: Favorite cafe migrates primary → secondary → tertiary as you stop visiting
    """
    old_tier = location.zone_tier

    # Remove from old tier
    if old_tier == "primary":
        agent.field_state.primary_zones.remove(location)
    elif old_tier == "secondary":
        agent.field_state.secondary_zones.remove(location)
    elif old_tier == "tertiary":
        agent.field_state.tertiary_zones.remove(location)

    # Add to new tier
    location.zone_tier = new_tier
    if new_tier == "primary":
        agent.field_state.primary_zones.append(location)
    elif new_tier == "secondary":
        agent.field_state.secondary_zones.append(location)
    elif new_tier == "tertiary":
        agent.field_state.tertiary_zones.append(location)
```

## Ambient → Stored Migration

Temporary ambient location impacts can migrate to stored zones:

```python
def check_location_migration(agent: Agent):
    """
    Check temporary location impacts for migration to stored zones

    Example: "That cafe with the cool sign" → think about it for days → migrates to tertiary_zone
    """
    for impact in agent.field_state.active_location_perturbations:
        if impact.should_migrate():
            # Create location imprint from ambient impact
            location = LocationImprint(
                location_id=generate_uuid(),
                location_name=impact.location_description,
                coordinates=impact.coordinates,
                zone_tier="tertiary",  # Always starts in tertiary
                field_strength=impact.location_strength_coefficient,
                visit_frequency=0.0,  # Haven't actually visited (or visited once)
                last_visit=impact.impact_timestamp,
                total_time_spent=0.0,
                emotional_association=impact.emotional_charge,
                dominant_emotions=[],
                attention_focus=impact.attention_focus,
                memory_strength=impact.emotional_charge,  # Strong memory if emotionally charged
                first_encoded=current_time(),
                decay_rate=0.05
            )

            # Add to tertiary zones
            agent.field_state.tertiary_zones.append(location)

            # Remove from ambient
            agent.field_state.active_location_perturbations.remove(impact)

        elif not impact.should_persist():
            # Dissipate - no longer being considered
            agent.field_state.active_location_perturbations.remove(impact)
```

## Decay Over Time

Location imprints decay when not visited or thought about:

```python
def apply_location_decay(location: LocationImprint, time_delta: float):
    """
    Reduce field strength based on time without visits

    Slower decay for primary zones (home remains encoded even during travel)
    Faster decay for tertiary zones (occasional places fade quickly)
    """
    # Calculate time since last visit
    time_since_visit = current_time() - location.last_visit

    # Decay rate depends on tier
    if location.zone_tier == "primary":
        decay_multiplier = 0.5  # Slow decay (home stays encoded)
    elif location.zone_tier == "secondary":
        decay_multiplier = 1.0  # Normal decay
    else:  # tertiary
        decay_multiplier = 2.0  # Fast decay (quickly forgotten)

    # Apply decay
    decay_amount = location.decay_rate * time_since_visit * decay_multiplier
    location.field_strength = max(0.0, location.field_strength - decay_amount)

    # Also decay attention_focus (thoughts naturally fade)
    attention_decay = 0.01 * time_delta
    location.attention_focus = max(0.0, location.attention_focus - attention_decay)
```

## Examples

**Primary Zone (Home)**
```python
home = LocationImprint(
    location_id=home_id,
    location_name="Home",
    zone_tier="primary",
    field_strength=0.95,
    visit_frequency=1.0,        # Daily presence
    emotional_association=0.8,   # Safe, comfortable
    attention_focus=0.9,        # Think about it often
    dominant_emotions=["safe", "relaxed", "private"]
)
# Impact: Maximum - events at home deeply affect you
```

**Secondary Zone (Favorite Cafe)**
```python
cafe = LocationImprint(
    location_id=cafe_id,
    location_name="Daily Grind Coffee",
    zone_tier="secondary",
    field_strength=0.6,
    visit_frequency=0.5,        # Visit 2-3x per week
    emotional_association=0.7,   # Creative, inspired
    attention_focus=0.4,        # Think about it occasionally
    dominant_emotions=["creative", "social", "energized"]
)
# Impact: Moderate - experiences there affect your mood/productivity
```

**Tertiary Zone (Cool Sign Place)**
```python
cool_place = LocationImprint(
    location_id=cool_place_id,
    location_name="That building with the mural",
    zone_tier="tertiary",
    field_strength=0.25,
    visit_frequency=0.0,        # Never actually visited
    emotional_association=0.6,   # Aesthetic appreciation
    attention_focus=0.4,        # Keep thinking about it
    dominant_emotions=["inspired", "curious"]
)
# Impact: Low but persistent - you keep thinking about going there
```

**Ambient → Tertiary Migration (Migrating Example)**
```python
# Starts as ambient
ambient = LocationImpact(
    location_description="Cafe with amazing architecture",
    impact_timestamp=current_time(),
    emotional_charge=0.8,       # Really loved it
    attention_focus=0.7         # Can't stop thinking about it
)

# After days of thinking about it
# strength = 0.8 × 0.7 = 0.56 >= 0.1 threshold
# → Migrates to tertiary_zone as LocationImprint
```

---

**Previous:** [09_data_model_entanglement.md](09_data_model_entanglement.md) | **Next:** [11_data_model_permission_set.md](11_data_model_permission_set.md)
