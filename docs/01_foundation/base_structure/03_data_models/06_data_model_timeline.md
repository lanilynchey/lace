# Data Model: Timeline / Worldline

A possible experiential path through reality.

```python
class Timeline:
    """A possible worldline - one potential reality path"""

    # Identity
    worldline_id: UUID
    frequency: float           # Vibrational signature

    # Contents
    events: List[Event]        # Key moments in this timeline
    probability: float         # Likelihood given current state (0-1)
    coherence: float           # Internal consistency (0-1)

    # Relationships
    branches_from: Optional[UUID]      # Parent timeline
    branches_to: List[UUID]            # Possible futures

    # Metadata
    dimensionality: int        # How many dimensions agent perceives
    access_requirement: int    # Minimum permission level needed
```

**Key Insight:**
- Infinite timelines exist simultaneously
- You don't "create" your timeline - you **match** to one
- Manifestation = jumping to adjacent timeline with higher coherence

## Timeline Matching Protocol

How agents connect to worldlines based on frequency (probabilistic model):

```python
def match_worldline(agent_frequency: float, coherence: float, context: Dict) -> Timeline:
    """
    Find probabilistic frequency match in worldline space

    Matching is PROBABILISTIC, not deterministic:
    - High coherence = narrow distribution (almost deterministic)
    - Low coherence = wide distribution (scattered, unpredictable)
    - Accounts for manifestation variance and uncertainty

    Args:
        agent_frequency: Agent's calculated state_signature frequency (0-1)
        coherence: Agent's internal signal alignment (0-1)
        context: Current location, permissions, karma, persistent patterns

    Returns:
        Timeline probabilistically matched to agent's frequency

    Algorithm:
        1. Generate possibility space (all accessible timelines given context)
        2. Filter by permission level (can't access restricted worldlines)
        3. Calculate probability weights using Gaussian distribution
        4. Return probabilistically selected timeline (weighted by frequency proximity)
    """
    # Generate accessible worldlines
    worldlines = generate_possibility_space(context)

    # Filter by permissions
    viable = [w for w in worldlines if w.access_requirement <= agent.access_level]

    # Calculate variance based on coherence
    # Higher coherence = lower variance = tighter distribution
    base_variance = 0.1  # Base noise level
    sigma = base_variance / (1 + coherence)  # Coherence narrows distribution

    # Calculate probability weights (Gaussian distribution)
    probability_weights = []
    for w in viable:
        freq_diff = w.frequency - agent_frequency
        weight = exp(-((freq_diff)**2) / (2 * sigma**2))
        probability_weights.append(weight)

    # Normalize weights
    total_weight = sum(probability_weights)
    normalized_weights = [w / total_weight for w in probability_weights]

    # Probabilistically select timeline
    selected = random.choice(viable, weights=normalized_weights)

    return selected
```

**Matching Behavior:**
- **Probabilistic matching** (not exact deterministic)
- High coherence (0.9) → very tight distribution (almost deterministic)
- Moderate coherence (0.6) → moderate spread (some variance)
- Low coherence (0.3) → wide distribution (scattered manifestation)
- Most likely match = closest frequency, but variance possible

## Timeline Stickiness

How hard is it to jump timelines?

```python
def calculate_stickiness(agent: Agent, current_timeline: Timeline) -> float:
    """
    Stickiness = resistance to timeline shifting

    Formula: stickiness = inhabitance_duration * emotional_investment

    Properties:
    - Longer in timeline → harder to shift
    - Higher emotional attachment → stronger inertia
    - Fresh incarnation → low stickiness (easy to shift)
    - Trauma bonding → very high stickiness (stuck in loop)
    """
    duration = time_in_timeline(agent, current_timeline)  # seconds
    investment = emotional_attachment_level(agent, current_timeline)  # 0-1

    stickiness = (duration / 86400) * investment  # Normalize by days
    return stickiness


def shift_difficulty(current_stickiness: float, frequency_delta: float) -> str:
    """
    Determine how difficult a timeline shift will be

    Returns: "easy", "moderate", "difficult", or "requires_major_event"
    """
    difficulty_score = current_stickiness * frequency_delta

    if difficulty_score < 0.1:
        return "easy"  # Fresh in timeline, small shift
    elif difficulty_score < 0.3:
        return "moderate"  # Requires intention and coherence
    elif difficulty_score < 0.6:
        return "difficult"  # Major life change or trauma needed
    else:
        return "requires_major_event"  # Death, awakening, grace protocol
```

**Key Properties:**
- Fresh incarnation = low stickiness (reality is malleable)
- Long inhabitance + attachment = high stickiness (reality feels solid)
- Large frequency shifts = harder than small adjustments
- Trauma creates "stickiness loops" (hardest to escape)

## Worldline Branching Mechanics

Timelines branch at **choice points** - moments where free will creates divergence.

```python
# When a branch occurs:
def create_branch(parent_timeline: Timeline, choice: Decision) -> Timeline:
    """
    Timelines branch at free will moments

    Branch triggers:
    - Significant decision (high karma weight)
    - Quantum measurement (observer collapse)
    - Grace intervention (system override)
    - Collective field shift (group manifestation)
    """
    new_timeline = Timeline(
        worldline_id=generate_id(),
        frequency=calculate_new_frequency(choice),
        branches_from=parent_timeline.worldline_id
    )

    parent_timeline.branches_to.append(new_timeline.worldline_id)

    return new_timeline
```

**Key Properties:**
- Each decision creates new branch; old path remains accessible
- Quantum mechanics: observer measurement = branch point
- All branches exist simultaneously in superposition
- Agent experiences ONE branch but can shift between adjacent timelines

---

**Previous:** [05_data_model_state_signature.md](05_data_model_state_signature.md) | **Next:** [07_data_model_field_state.md](07_data_model_field_state.md)
