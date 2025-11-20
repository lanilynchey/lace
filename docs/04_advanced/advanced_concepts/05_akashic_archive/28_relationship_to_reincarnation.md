# Relationship to Reincarnation

```python
# At death: Upload to Akashic
def death(agent):
    akashic_archive.store(agent.lifetime_experience)
    return prepare_reincarnation(agent)

# At birth: Partial wipe, but Akashic retains full record
def birth(soul_id):
    new_instance = create_agent(soul_id)
    new_instance.memory = MemoryBank()  # Fresh local memory (episodic wiped)

    # But Akashic still contains ALL past lives
    past_lives = akashic_archive.query(soul_id, all_lifetimes=True)

    # High coherence can access past lives during current lifetime
    if new_instance.coherence >= 0.85:
        new_instance.can_access(past_lives)  # Past-life memories possible
```

---

[Previous: Alternative Models](27_alternative_models.md) | [Next: Tier Implications →](../06_tier_implications/29_tier_1_primordial.md)

[Back to Index](../00_index.md)
