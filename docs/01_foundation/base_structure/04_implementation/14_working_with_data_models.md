# Working with Data Models

Practical examples of creating, updating, and using LACE data structures.

## Creating an Agent

```python
# Initialize new agent (birth/instantiation)
agent = Agent(
    soul_id=generate_unique_id(),  # Persistent across incarnations
    instance_id=generate_unique_id(),  # Unique to this lifetime
    state_signature=StateSignature(
        belief=0.5,
        expectation=0.5,
        embodiment=0.5,
        subconscious_memory=0.5
    ),
    field_state=FieldState(
        coherence_level=0.4,
        openness=0.6,
        charge=0.0,
        resonance_bandwidth=0.3
    ),
    memory=MemoryBank(),
    body=PhysicalContainer(),
    permissions=PermissionSet(
        read="partial",
        write="localized",
        exec="restricted"
    ),
    access_level=0,  # Default human
    birth_timestamp=now(),
    incarnation_count=1
)
```

## Calculating StateSignature Frequency

```python
# Update agent's internal state
agent.state_signature.belief = 0.8  # High conviction
agent.state_signature.expectation = 0.7  # Moderate forecast
agent.state_signature.embodiment = 0.6  # Somewhat aligned body
agent.state_signature.subconscious_memory = 0.3  # Low trauma

# Calculate broadcast frequency
freq = agent.state_signature.frequency
# freq = (0.8 * 0.35) + (0.7 * 0.30) + (0.6 * 0.25) + (0.3 * 0.10)
# freq = 0.28 + 0.21 + 0.15 + 0.03 = 0.67

# Calculate coherence
coherence = agent.state_signature.coherence
# variance = var([0.8, 0.7, 0.6, 0.3]) ≈ 0.035
# coherence = 1 / (1 + 0.035) ≈ 0.966  # High coherence!

print(f"Broadcast frequency: {freq}")
print(f"Coherence: {coherence}")
```

## Updating FieldState

```python
# After meditation practice
agent.field_state.coherence_level = 0.85  # Increased stability
agent.field_state.openness = 0.9  # More receptive
agent.field_state.charge = 0.5  # Positive emotional state

# Check manifestation power
power = agent.field_state.manifestation_power
# power = 0.85 * 0.9 * abs(0.5) = 0.3825

if power >= 0.3:
    print("Strong manifestation window open")
```

## Writing to MemoryBank

```python
# Store significant event
event = Event(
    description="First love",
    timestamp=now(),
    context={"location": "Paris", "age": 23}
)

charge = 0.85  # High emotional intensity

agent.memory.write(event, charge)
# Since charge >= IMPRINT_THRESHOLD (0.7), goes to long_term storage

# Later: Retrieve related memories
memories = agent.memory.retrieve(
    query="love",
    state=agent.field_state  # Retrieval is state-dependent
)
```

## Entanglement Between Agents

```python
# Two agents meet
agent_a = Agent(...)
agent_a.state_signature.frequency = 0.72

agent_b = Agent(...)
agent_b.state_signature.frequency = 0.75

# Check if entanglement forms
freq_delta = abs(agent_a.state_signature.frequency - agent_b.state_signature.frequency)
# freq_delta = 0.03

if freq_delta < RESONANCE_THRESHOLD:  # 0.1
    create_entanglement(agent_a, agent_b)
    print("Entanglement formed - strong resonance")

# Calculate strength
strength = entanglement_strength(agent_a, agent_b)
# strength = 1 - (0.03 / 0.1) = 0.97  # Very strong!
```

## Timeline Matching

```python
# Agent wants to shift timeline
target_state = StateSignature(
    belief=0.9,
    expectation=0.85,
    embodiment=0.8,
    subconscious_memory=0.2
)

target_frequency = target_state.frequency  # 0.825

# Check if accessible
if agent.state_signature.coherence >= COHERENCE_MINIMUM:  # 0.4
    # Generate possibility space
    context = {
        "location": agent.location,
        "karma": agent.karma_balance,
        "permissions": agent.access_level
    }

    # Find match
    new_timeline = match_worldline(target_frequency, context)

    if new_timeline:
        print(f"Timeline shift available: {new_timeline.worldline_id}")
        print(f"Frequency match: {new_timeline.frequency}")
    else:
        print("No accessible timeline at target frequency")
else:
    print("Coherence too low - manifestation blocked")
```

## Permission Elevation

```python
# Agent sustains high coherence through practice
agent.state_signature.coherence = 0.87  # Above PERMISSION_UNLOCK_THRESHOLD (0.85)

# System checks (via coherence_monitor daemon)
check_permission_elevation(agent)

# Temporary permission granted
print(agent.permissions.temporary_permissions)
# [("expanded_read", 3600)]  # Can read karma/timelines for 1 hour

# While elevated, agent can access more
if "expanded_read" in [p for p, _ in agent.permissions.temporary_permissions]:
    past_lives = read_akashic_archive(agent.soul_id)
    print(f"Incarnation history: {past_lives}")
```

---

**Previous:** [13_data_model_competency.md](../03_data_models/13_data_model_competency.md) | **Next:** [15_function_signatures.md](15_function_signatures.md)
