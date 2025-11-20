# 2. Reincarnation Mechanics

## **What Is Reincarnation in LACE?**

**Reincarnation is the mechanism by which death() leads to rebirth** - not guaranteed to occur, but high probability based on unresolved patterns and karma balance.

**LACE Position:** Reincarnation is modeled as a **potential literal mechanism** showing how it would work computationally, without claiming certainty that it occurs.

```python
def reincarnate(agent: Agent) -> Agent:
    """
    Create new instance with partial memory wipe

    Reincarnation Mechanics:
    1. soul_id persists (same soul across lifetimes)
    2. instance_id regenerated (new lifetime container)
    3. incarnation_count incremented
    4. Partial memory wipe (episodic cleared, patterns persist)
    5. Karma balance carries forward
    6. Persistent patterns (probability biases) continue

    See BASE_STRUCTURE.md lines 354-374 for complete specification
    """

    new_instance = Agent(
        soul_id=agent.soul_id,  # SAME - persistent identity across incarnations
        instance_id=generate_new(),  # NEW - unique to this lifetime
        incarnation_count=agent.incarnation_count + 1,  # Increment

        # Memory handling
        memory=MemoryBank(
            long_term=[],  # Episodic memories WIPED (specific events forgotten)
            implicit=agent.memory.implicit,  # Skills/patterns PERSIST
            suppressed=partial_carry(agent.memory.suppressed)  # Some trauma bleeds through
        ),

        # Carry forward
        karma_balance=agent.karma_balance,  # Debt/credit continues
        persistent_patterns=agent.persistent_patterns,  # Probability biases continue

        # Reset
        body=new_physical_container(),  # Fresh form
        field_state=reset_to_default(),  # Fresh energy signature
    )

    return new_instance
```

---

[Previous: Key Insights](../02_persistent_patterns/07_key_insights.md) | [Next: Memory Persistence →](09_memory_persistence.md)

[Back to Index](../00_index.md)
