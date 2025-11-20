# How Data Gets Into the Archive

```python
def death(agent):
    """
    Death uploads experience to Akashic

    Process:
        1. Extract all experience_log from agent
        2. Upload to akashic_archive
        3. Data becomes permanent record
        4. Agent's form terminates
        5. Core essence available for re-instantiation
    """
    # Extract lifetime data
    experience_data = extract(agent.experience_log)

    # Upload to Akashic archive
    akashic_archive.store(experience_data)

    # Form terminates
    release(agent.form)

    # Core available for next incarnation
    return reset(agent.core)
```

---

[Previous: What Is Akashic](19_what_is_akashic.md) | [Next: What's Stored →](21_whats_stored.md)

[Back to Index](../00_index.md)
