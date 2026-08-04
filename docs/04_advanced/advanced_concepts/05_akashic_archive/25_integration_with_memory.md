# Integration with memory() Force

**Key Distinction:**
- **memory()** [Tier 2 force] = individual agent's **local** memory (MemoryBank stored in agent instance)
- **Akashic Archive** = **universal** memory (all agents, all lifetimes, the one shared reality's full history)

```python
# Local vs. Universal Memory
local_memory = agent.memory  # MemoryBank - this lifetime only
universal_memory = akashic_archive  # All lifetimes, all souls

# At death: Local → Universal
def death(agent):
    # Upload local memory to universal archive
    akashic_archive.store(agent.memory)

    # Local memory wiped for next incarnation
    agent.memory = MemoryBank()

    # Universal memory persists
    return akashic_archive

# High coherence agents can query universal
if agent.coherence >= 0.85:
    past_life_data = akashic_archive.query(agent.soul_id, lifetime=-1)
    # "Past-life regression" = querying own akashic records
```

---

[Previous: Implementation Architecture](24_implementation_architecture.md) | [Next: Primitive Integration →](26_primitive_integration.md)

[Back to Index](../00_index.md)
