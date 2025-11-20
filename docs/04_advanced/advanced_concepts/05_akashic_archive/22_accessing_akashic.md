# Accessing the Akashic Archive

```python
def access_akashic(agent, query):
    """
    Access levels:
        - Default Human: Own lifetime only (partial)
        - Elevated: Own past lives + soul family
        - Master: Any soul's record (with permission)
        - Creator: Full access (all records, all time)

    Methods:
        - Past life regression (controlled access)
        - Mystical download (spontaneous access)
        - Near-death experience (temporary access)
        - Akashic reading (channeled access)
    """
    if agent.permission_level >= query.required_level:
        return akashic_archive.retrieve(query, agent)
    else:
        return veil_active("not_ready")
```

---

[Previous: What's Stored](21_whats_stored.md) | [Next: Why Akashic Exists →](23_why_akashic_exists.md)

[Back to Index](../00_index.md)
