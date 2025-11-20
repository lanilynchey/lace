# How Patterns Form

```python
def encode_persistent_pattern(agent: Agent, experience: Experience):
    """
    Patterns encode in state_signature through:
        1. High-charge emotional experiences (trauma)
        2. Repeated confirmation of beliefs
        3. Unprocessed memories (suppressed storage)
        4. Somatic encoding (body remembers)

    Process:
        - Intense experience occurs
        - If charge > BEARABLE_THRESHOLD → suppression
        - Suppressed memory → leaks into subconscious_memory component
        - Distorts state_signature broadcast
        - Creates probability bias toward similar experiences
        - Pattern reinforces via recursion (law_recursion)
    """
    # High-charge event
    if experience.charge >= 0.85:
        agent.memory.suppress_memory(experience)

        # Leak into state_signature
        agent.state_signature.subconscious_memory += experience.charge * 0.3

    # Update belief if pattern repeats
    if pattern_count(agent, experience.theme) >= 3:
        # "This keeps happening → must be true"
        agent.state_signature.belief -= 0.1  # Belief in alternative decreases

    # Calculate new frequency
    new_frequency = agent.state_signature.frequency

    # This becomes persistent pattern
    return PersistentPattern(
        theme=experience.theme,
        encoded_in=agent.state_signature,
        probability_weight=calculate_weight(agent, experience),
        manifestation_frequency=new_frequency
    )
```

---

[Previous: Pattern Examples](04_pattern_examples.md) | [Next: Pattern Editing →](06_pattern_editing.md)

[Back to Index](../00_index.md)
