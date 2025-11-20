# Data Model: MemoryBank

Storage system for agent experiences.

```python
class MemoryBank:
    """Emotionally-indexed storage of experience"""

    # Storage
    long_term: List[Memory]    # High emotional charge
    cache: List[Memory]        # Low emotional charge (decays)
    suppressed: List[Memory]   # Unprocessed trauma (hidden)

    # Index
    emotional_tags: Dict[str, List[Memory]]
    timeline_index: Dict[float, List[Memory]]  # By timestamp

    # Functions
    def write(self, event: Event, charge: float) -> None:
        """Store memory based on emotional intensity"""
        memory = Memory(event, charge, timestamp=now())
        if charge >= IMPRINT_THRESHOLD:
            self.long_term.append(memory)
        else:
            self.cache.append(memory)

    def retrieve(self, query: str, state: FieldState) -> List[Memory]:
        """Retrieval is state-dependent"""
        # Memories retrieved based on current emotional state
        pass

    def suppress_memory(self, memory: Memory) -> None:
        """
        Automatic suppression if charge exceeds bearable threshold

        Suppression triggers:
        - Emotional charge > BEARABLE_THRESHOLD (too intense to process)
        - Threatens identity coherence (challenges core beliefs)
        - Overwhelming trauma (safety mechanism)

        Effects:
        - Memory moved to suppressed storage
        - Leaks into subconscious_memory component of StateSignature
        - Creates distortion in frequency broadcast
        - Can surface through dreams, somatic symptoms, triggers

        Note: Suppression is protective but creates manifestation distortion
        """
        BEARABLE_THRESHOLD = 0.85  # Maximum processable emotional intensity

        if memory.charge > BEARABLE_THRESHOLD:
            self.suppressed.append(memory)

            # Leak into subconscious distortion
            increase_subconscious_distortion(magnitude=memory.charge * 0.3)

            # Remove from conscious access
            if memory in self.long_term:
                self.long_term.remove(memory)
```

**Key Insight:**
- Memory is NOT truth - it's emotionally charged snapshots
- Trauma = data too volatile to write cleanly (automatic suppression)
- Suppressed memories distort state_signature (leak into subconscious_memory component)
- Forgiveness = dissolving emotional charge on memory
- Healing = retrieving suppressed memories and reducing charge

---

**Previous:** [07_data_model_field_state.md](07_data_model_field_state.md) | **Next:** [09_data_model_permission_set.md](09_data_model_permission_set.md)
