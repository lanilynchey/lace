# Data Model: MemoryBank

Storage system for agent experiences.

```python
class MemoryBank:
    """Emotionally-indexed storage of experience with four-tier hierarchy"""

    # Four-Tier Storage (hierarchical by emotion and usage)
    working_memory: List[Memory]    # Active focus (4-7 items, 99% accuracy)
    permanent: List[Memory]         # High emotional charge (95% accuracy, never pruned)
    long_term: List[Memory]         # Medium emotional charge (70% accuracy, pruned after years)
    short_term: List[Memory]        # Low emotional charge (40% accuracy, pruned within months)
    suppressed: List[Memory]        # Unprocessed trauma (hidden from conscious access)

    # Pattern Cache (stimulus-response patterns)
    pattern_cache: PatternCache  # Cached automated responses

    # Index
    emotional_tags: Dict[str, List[Memory]]
    timeline_index: Dict[float, List[Memory]]  # By timestamp

    # Cache/Live Tracking
    cache_hit_rate: float      # % of stimuli handled by cache (averaged)
    live_processing_rate: float  # % requiring active processing (averaged)

    # Storage Management
    max_storage: float         # Maximum storage capacity
    storage_used: float        # Current storage utilization
    capacity_threshold: float = 0.85  # Trigger pruning at 85% full

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

## PatternCache

The `pattern_cache` field stores stimulus-response patterns for rapid automated processing. This enables efficient operation by caching familiar patterns rather than live-processing every experience.

**Architecture:** Three-tier cache system prioritized by survival value and emotional charge.

```python
class PatternCache:
    """Hierarchical cache storage for stimulus-response patterns"""

    # TIER 1: SURVIVAL CACHE (Highest Priority)
    survival_cache: Dict[Pattern, Response]
    survival_priority: int = 10            # Processed first, always
    survival_pruning_resistance: float = 1.0  # Never pruned
    """
    Threat responses, safety patterns, danger recognition

    Properties:
    - Cached FIRST (highest priority encoding)
    - Retrieved FASTEST (bypass other processing)
    - Persist FOREVER (never pruned even if unused)

    Examples:
    - Snake → danger response
    - Fire → threat response
    - Falling → fear response
    - Loud noise → startle response
    """

    # TIER 2: EMOTIONAL CACHE (Medium Priority)
    emotional_cache: Dict[Pattern, Response]
    emotional_priority: int = 7            # After survival, before routine
    emotional_pruning_resistance: float = 0.85  # High persistence
    """
    Relationship patterns, social rules, emotional associations

    Properties:
    - High emotional charge = strong caching
    - Moderate persistence (pruned only if unused for years)
    - Forms basis of personality patterns

    Examples:
    - Authority figure → compliance/rebellion
    - Rejection → pain/withdrawal
    - Praise → joy/pride
    - Conflict → avoid/engage
    """

    # TIER 3: ROUTINE CACHE (Lowest Priority)
    routine_cache: Dict[Pattern, Response]
    routine_priority: int = 4              # Processed last
    routine_pruning_resistance: float = 0.30  # Low persistence
    """
    Daily habits, skill automation, repeated tasks

    Properties:
    - Low emotion = weak caching
    - Easily pruned if unused (weeks to months)
    - Efficient but flexible

    Examples:
    - Morning routine → automated sequence
    - Commute route → autopilot navigation
    - Typing → muscle memory
    - Tool usage → automatic movements
    """

    def match(self, stimulus: Stimulus) -> Optional[Response]:
        """
        Check if stimulus matches cached pattern

        Search order: Survival → Emotional → Routine
        First match returns (no further processing)
        """
        # Check survival cache first (highest priority)
        if match := self.survival_cache.get(stimulus):
            return match  # Instant return, bypass other tiers

        # Check emotional cache second
        if match := self.emotional_cache.get(stimulus):
            return match

        # Check routine cache last
        if match := self.routine_cache.get(stimulus):
            return match

        # No match found - triggers live processing
        return None

    def store(self, pattern: Pattern, response: Response, emotion: float) -> None:
        """
        Store new pattern based on emotional charge

        Routing logic:
        - emotion >= 0.70: Survival cache (if threat-related) or Emotional cache
        - emotion >= 0.30: Emotional cache
        - emotion < 0.30: Routine cache
        """
        if emotion >= 0.70:
            if pattern.is_survival_related():
                self.survival_cache[pattern] = response
            else:
                self.emotional_cache[pattern] = response
        elif emotion >= 0.30:
            self.emotional_cache[pattern] = response
        else:
            self.routine_cache[pattern] = response

    def prune_unused(self, tier: str = "routine") -> int:
        """
        Remove unused cache entries (emotion-based pruning)

        Pruning rules:
        - Survival: NEVER pruned (permanent)
        - Emotional: Pruned only if unused for years + low charge
        - Routine: Pruned if unused for weeks + low emotion

        Returns: Number of entries pruned
        """
        pruned_count = 0

        if tier == "routine":
            # Prune routine cache entries with low access frequency
            for pattern, response in list(self.routine_cache.items()):
                if response.last_accessed > ROUTINE_PRUNE_THRESHOLD:
                    del self.routine_cache[pattern]
                    pruned_count += 1

        elif tier == "emotional":
            # Prune emotional cache only if very old + charge reduced
            for pattern, response in list(self.emotional_cache.items()):
                if (response.last_accessed > EMOTIONAL_PRUNE_THRESHOLD and
                    response.emotional_charge < 0.30):
                    del self.emotional_cache[pattern]
                    pruned_count += 1

        # Note: Survival cache is NEVER pruned

        return pruned_count
```

**Key Properties:**

**Cache vs Live Processing:**
- **Cache hit:** Pattern matches → instant retrieval (fast, low energy: 0.1 units)
- **Cache miss:** No match → live processing required (slow, high energy: 5.0 units)
- **Cache ratio:** % of experiences handled by cache (tracked in MemoryBank)

**Relationship to Habits:**
Habits = cached behavioral patterns. All habits are stored in PatternCache. Habit formation = caching process. Habit breaking = cache override + re-caching new pattern.

**Cache Override:**
Requires conscious effort:
1. Notice cache hit occurred (awareness)
2. Recognize as automated pattern (meta-awareness)
3. Interrupt execution (conscious control)
4. Generate alternative response (live processing)
5. Repeat until re-cached (66+ repetitions typically)

**Implications:**
- Most reality runs on cache (80-95% in typical adult)
- Conscious presence requires increasing live processing ratio
- Novelty forces cache misses → depletes resources but builds presence
- Meditation trains cache detection and live processing capacity

**See Also:**
- [Cache vs Live Processing](../../../04_advanced/advanced_concepts/21_cache_vs_live_processing.md) for complete cache mechanics
- [System Resource Allocation](../../../04_advanced/advanced_concepts/20_system_resource_allocation.md) for energy costs
- [Consciousness Scale](../../../04_advanced/advanced_concepts/14_consciousness_scale_framework.md) for cache awareness by level

---

## Four-Tier Memory Storage & Compression

The MemoryBank uses a **four-tier hierarchical system** to optimize storage. Memories are not stored equally - emotional charge, time, usage, and survival value determine storage tier, compression level, and pruning schedule.

**Note:** Focus is huge for LACE - Working Memory represents active attentional focus, the bottleneck for all conscious processing.

### Tier 0: Working Memory

**Active attentional focus - what you're consciously processing RIGHT NOW**

```python
# Tier 0 Properties
capacity: 4-7 items (Miller's Law - strict limit)
compression: 0% (full fidelity while held)
duration: Seconds to minutes
accuracy: 99% (near-perfect while in focus)
pruning: Instant (when attention shifts)
```

**Examples:**
- Phone number you're about to dial
- Sentence you're currently reading
- Thought you're actively processing
- Item you're searching for in room

**Critical characteristics:**
- THE bottleneck for consciousness (all processing passes through)
- Extremely limited capacity (cannot be expanded)
- Zero compression (full detail while held)
- Instant loss when attention shifts (no grace period)
- Determines what gets encoded to long-term storage

### Tier 1: Permanent Storage

**High-fidelity, survival-priority, never pruned**

```python
# Tier 1 Properties
trigger: Emotional charge >= 0.70 OR survival-related
compression: 5% (95% retention)
pruning_resistance: 99% (almost never pruned)
accuracy: 95% (very high fidelity)
storage_cost: HIGH (resource intensive)
```

**Examples:**
- Trauma (fear, pain - negative high-emotion)
- Peak experiences (joy, love - positive high-emotion)
- Life milestones (weddings, births, deaths)
- Survival patterns (threats, danger, safety)

**Special properties:**
- Survival memories ALWAYS stored here (automatic protection)
- Never pruned even if never accessed
- Minimal compression over time
- Foundation of identity and persistent patterns

### Tier 2: Long-Term Storage

**Compressed, pruned after years if unused**

```python
# Tier 2 Properties
trigger: Emotional charge 0.30-0.69
compression: 50% (moderate detail loss)
pruning_resistance: 70% (gradual fade if not accessed)
accuracy: 70% (moderate - some details invented on retrieval)
storage_cost: MEDIUM (balanced)
```

**Examples:**
- Meaningful conversations
- Travel experiences
- Learning milestones
- Relationship memories (moderate significance)

**Compression over time:**
- Recent: Minimal compression (near full detail)
- Years old: Moderate compression (key details remain)
- Decades old + unused: Heavy compression (outline only)

### Tier 3: Short-Term Cache

**Heavily compressed, pruned within weeks/months**

```python
# Tier 3 Properties
trigger: Emotional charge < 0.30
compression: 90% (sparse details)
pruning_resistance: 20% (low - easily deleted)
accuracy: 40% (heavily reconstructed on retrieval)
storage_cost: LOW (minimal resources)
```

**Examples:**
- Routine commutes
- Mundane meals
- Typical workdays
- Forgettable social interactions

**Pruning schedule:**
- Unused for weeks: Likely pruned when capacity reached
- Unused for months: Definitely pruned
- Low emotion + old + never accessed: First to go

### Combined Compression Algorithm

**All factors influence compression (not just emotion):**

1. **Emotional charge (50% weight)** - Primary factor
   - High emotion → low compression
   - Low emotion → high compression

2. **Time decay (25% weight)** - Aging effect
   - Recent → minimal compression
   - Old (5+ years) → maximum compression

3. **Access frequency (15% weight)** - Usage tracking
   - Frequently accessed → resist compression
   - Rarely accessed → compress more

4. **Survival relevance (10% weight)** - Safety priority
   - Survival-related → resist compression
   - Non-survival → compress normally

**Result:** Old, rarely-accessed, low-emotion, non-survival memories compress maximally. Recent, frequently-accessed, high-emotion, survival memories resist compression.

### Threshold-Based Pruning

**Trigger:** When storage capacity reaches 85% threshold

```python
def check_capacity_and_prune(memory_bank: MemoryBank) -> None:
    """Monitor capacity and prune when threshold reached"""

    utilization = memory_bank.storage_used / memory_bank.max_storage

    if utilization >= memory_bank.capacity_threshold:  # 85%
        prune_lowest_priority_memories(memory_bank)
        # Target: Reduce to 70% utilization
```

**Pruning priority (prune in this order):**
1. Zero-emotion, old, never accessed (short-term tier)
2. Low-emotion, old, rarely accessed (short-term tier)
3. Medium-emotion, very old, never accessed (long-term tier)
4. **NEVER:** Permanent tier (survival) - absolute protection

**Permanent tier protection:**
- Survival memories never pruned (even if ancient and unused)
- High-emotion experiences never pruned (trauma, joy, milestones)
- System prioritizes survival/emotional significance over recency

### Memory Re-Encoding

**Memories CAN be re-encoded through:**

**1. Processing (therapy, reflection):**
- Reduces emotional charge on existing memories
- EMDR, CBT, trauma processing
- Charge reduction may move memory to lower tier
- Example: Trauma (0.85 charge) → Processed (0.40 charge) → Moves from permanent to long-term

**2. New experiences (pattern updating):**
- New experiences UPDATE existing pattern memories
- Doesn't erase old memory - INTEGRATES new data
- Blends emotional charges (weighted average)
- Example: Fear of dogs (0.80 charge) + Positive dog encounter (0.60 joy) → Blended pattern (0.50 charge)

**Dog example mechanics:**
```python
# Original: "Dogs are dangerous" (0.80 fear charge)
# New: Meet gentle dog, feel safe/joy (0.60 positive charge)
# Result: System integrates both
# - Danger response weight: 0.40 (reduced)
# - Safe response weight: 0.60 (new)
# - Blended charge: 0.50 (reduced from 0.80)
# Over time, repeated positive experiences fully re-encode the pattern
```

**This is why:**
- Someone afraid of dogs can learn to love them
- Trauma can heal through corrective experiences
- Beliefs can change through contradictory evidence

### Retrieval Accuracy by Tier

| Tier | Compression | Accuracy | Characteristics |
|------|-------------|----------|----------------|
| Working | 0% | 99% | Perfect while held, instant loss when attention shifts |
| Permanent | 5% | 95% | Very accurate, minimal gaps filled |
| Long-term | 50% | 70% | Moderate accuracy, some details invented |
| Short-term | 90% | 40% | Low accuracy, heavily reconstructed |

**Key insight:** Retrieval = reconstruction, not playback. Gaps filled with current beliefs, narrative coherence, inference, and pattern matching.

### Why Forgetting Is Beneficial

**Resource optimization:**
- Cannot store 1.7 billion life moments at full fidelity
- Pruning frees resources for new experiences
- Keeps only meaningful, useful data

**Pattern recognition:**
- Too much detail obscures patterns
- Compression reveals signal through noise reduction
- Wisdom = distilled patterns, not raw data

**Emotional healing:**
- Charge reduction allows painful memories to fade
- Old wounds become "scars" (present but not painful)
- Adaptive forgetting enables moving forward

**Identity flexibility:**
- Selective memory allows identity evolution
- "Forgetting who you were" enables "becoming who you are"

**Focus optimization:**
- Cannot attend to past AND present simultaneously
- Healthy forgetting = presence in current moment

**See Also:**
- [Memory Compression & Pruning](../../../04_advanced/advanced_concepts/23_memory_compression_pruning.md) for complete compression/pruning mechanics
- [System Resource Allocation](../../../04_advanced/advanced_concepts/20_system_resource_allocation.md) for storage costs
- [Perceptual Sampling Rate](../../../04_advanced/advanced_concepts/19_perceptual_sampling_rate.md) for what enters memory

---

**Previous:** [07_data_model_field_state.md](07_data_model_field_state.md) | **Next:** [09_data_model_permission_set.md](09_data_model_permission_set.md)
