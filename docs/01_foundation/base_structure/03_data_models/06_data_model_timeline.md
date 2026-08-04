# Data Model: StateTrajectory

**Revision note:** This document previously modeled reality as many pre-existing "worldlines" that agents matched/jumped between. It has been rewritten around a single continuously-mutating reality instead - see [`working/timeline_model_revision.md`](../../../../working/timeline_model_revision.md) for the full reasoning. The rest of the framework has since been brought in line with this model; this file remains the canonical reference for the `StateTrajectory` schema and terminology.

The single, actual path an agent's state has taken through reality - not one of many possible paths.

```python
class StateTrajectory:
    """The record of what actually happened, plus what's currently computing next"""

    # Contents
    events: List[Event]                          # Key moments in this trajectory
    projection_confidence: float                  # Likelihood currently-computing next state resolves as projected (0-1)
    coherence: float                              # Internal consistency (0-1)

    # Relationships
    previous_state: Optional[UUID]                # Prior point in this same trajectory
    projected_next: Optional[StateProjection]     # Single continuously-updating projection, not a menu of alternatives

    # Metadata
    dimensionality: int        # How many dimensions agent perceives
    access_requirement: int    # Minimum permission level needed
```

**Key Insight:**
- There is one reality; this is the record of your actual path through it
- You don't "match" to a pre-existing path - your state mutations *are* the path, computed directly
- Manifestation = a state mutation becoming rendered/perceptible, not a jump to a different pre-existing timeline

## State Mutation Protocol

How an agent's state actually changes, given intention and coherence (probabilistic, not deterministic):

```python
def compute_state_mutation(current_state: StateSignature, intention: Intention, coherence: float) -> StateDelta:
    """
    Compute how current state mutates given intention

    Mutation is PROBABILISTIC, not deterministic:
    - High coherence = narrow distribution (outcome nearly certain)
    - Low coherence = wide distribution (scattered, unpredictable outcome)
    - Accounts for entropy() injection and manifestation variance

    Args:
        current_state: Agent's current state_signature
        intention: What the agent is oriented toward
        coherence: Agent's internal signal alignment (0-1)

    Returns:
        StateDelta representing the computed mutation

    Algorithm:
        1. Determine candidate mutation space (consistent with current state + intention)
        2. Filter by permission level (can't mutate into restricted states)
        3. Calculate mutation using Gaussian distribution centered on intended target
        4. Return the computed mutation (variance narrowed by coherence)
    """
    # Calculate variance based on coherence
    # Higher coherence = lower variance = tighter distribution around intended outcome
    base_variance = 0.1  # Base noise level
    sigma = base_variance / (1 + coherence)  # Coherence narrows distribution

    # Sample the actual mutation from a distribution centered on the intended target
    delta = sample_gaussian(mean=intention.target_state, sigma=sigma)

    # Filter against permission level
    if not within_permission(delta, agent.access_level):
        delta = clamp_to_permitted(delta)

    return delta
```

**Mutation Behavior:**
- **Probabilistic outcome** (not exact deterministic) - the same underlying math as before, just describing how far the *actual* outcome lands from the *intended* one, not which pre-existing timeline gets selected
- High coherence (0.9) → very tight distribution (outcome nearly certain)
- Moderate coherence (0.6) → moderate spread (some variance)
- Low coherence (0.3) → wide distribution (scattered outcome)
- Most likely outcome = closest to intended target, but variance possible

## Trajectory Inertia

How hard is it to redirect an ongoing trajectory?

```python
def calculate_inertia(agent: Agent, current_trajectory: StateTrajectory) -> float:
    """
    Inertia = resistance to a trajectory changing direction

    Formula: inertia = duration_in_pattern * emotional_investment

    Properties:
    - Longer sustained pattern → harder to redirect
    - Higher emotional attachment → stronger resistance
    - Fresh pattern → low inertia (easy to redirect)
    - Trauma-bonded pattern → very high inertia (stuck in loop)

    Note: This is the same formula as grip strength in
    The Grip Mechanism (attention_focus × emotional_power) - duration in
    a pattern is a proxy for sustained attention. Same mechanism, applied
    to trajectory direction instead of a specific memory or relationship.
    """
    duration = time_in_pattern(agent, current_trajectory)  # seconds
    investment = emotional_attachment_level(agent, current_trajectory)  # 0-1

    inertia = (duration / 86400) * investment  # Normalize by days
    return inertia


def redirect_difficulty(current_inertia: float, mutation_magnitude: float) -> str:
    """
    Determine how difficult a trajectory redirection will be

    Returns: "easy", "moderate", "difficult", or "requires_major_event"
    """
    difficulty_score = current_inertia * mutation_magnitude

    if difficulty_score < 0.1:
        return "easy"  # Fresh pattern, small redirection
    elif difficulty_score < 0.3:
        return "moderate"  # Requires intention and coherence
    elif difficulty_score < 0.6:
        return "difficult"  # Major life change or trauma needed
    else:
        return "requires_major_event"  # Death, awakening, grace protocol
```

**Key Properties:**
- Fresh pattern = low inertia (trajectory is malleable)
- Long duration + attachment = high inertia (trajectory feels fixed)
- Large intended mutations = harder than small adjustments
- Trauma creates inertia loops (hardest to redirect) - see [The Grip Mechanism](../../../04_advanced/advanced_concepts/24_grip_mechanism.md) for the release pathways

## Choice Points

Choice points are moments where free will directs which mutation actually occurs.

```python
def choice_point(agent: Agent, decision: Decision, trajectory: StateTrajectory) -> StateDelta:
    """
    Choice does NOT branch reality - it determines which single mutation
    actually happens. Unchosen options are never instantiated; they have
    no ontological status. See free_will_code_authorship() - freedom is
    sequential self-authorship (can't change this moment's choice, can
    change how you respond going forward), not selection among branches.

    Trigger conditions (same moments that would have "branched" under
    the old model - now simply moments of higher mutation-magnitude):
    - Significant decision (high karma weight)
    - Quantum measurement (observer collapse - see law_observation())
    - Grace intervention (system override)
    - Collective field shift (see update_cycles.md - collective_field.readiness)
    """
    mutation = compute_state_mutation(
        current_state=agent.state_signature,
        intention=decision.chosen_intention,
        coherence=agent.state_signature.coherence
    )

    trajectory.events.append(Event(decision, mutation, timestamp=now()))
    trajectory.previous_state = trajectory.current_state_id

    return mutation
```

**Key Properties:**
- Each decision produces one mutation; nothing else is instantiated
- Quantum mechanics: observer measurement = mutation-determining event, not a branch point
- There is one trajectory; it has one actual history
- The agent experiences the single trajectory that is actually occurring - there is no "other branch" to shift between, only a different mutation that could have been chosen and wasn't

---

**Previous:** [05_data_model_state_signature.md](05_data_model_state_signature.md) | **Next:** [07_data_model_field_state.md](07_data_model_field_state.md)
