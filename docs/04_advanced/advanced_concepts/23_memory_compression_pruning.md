# Memory Compression & Pruning

**Memories are not stored equally - emotional charge determines what persists vs gets pruned.**

High-emotion experiences are encoded with maximum fidelity and resist compression. Neutral experiences are compressed immediately (lossy compression - details discarded). Zero-emotion experiences are pruned entirely within days. This is not memory failure - it's resource optimization. The system cannot store everything at full resolution, so it prioritizes emotionally significant data. Your memory is not a recording - it's a curated highlight reel weighted by emotional intensity.

---

## Overview

Memory is not a camera - it's a compression algorithm. The brain/consciousness does NOT record every moment in perfect detail. Instead, it applies **lossy compression** to most experiences, saving storage space by discarding "irrelevant" information.

**What determines "relevance"?** **Emotional charge.**

The stronger the emotion attached to an experience, the higher the fidelity it's encoded at, and the longer it resists compression/pruning.

**Computer analogy:**
- **Raw video:** 4K resolution, 60fps, massive file size (unsustainable for long-term storage)
- **Compressed video:** 720p, 24fps, ~90% smaller file (lossy - details lost but viewable)
- **Thumbnail:** Low-res snapshot, ~99% smaller (barely recognizable)
- **Deleted:** Removed entirely to free space

**Memory storage:**
- **High-emotion:** Full resolution, rich detail, permanent storage (trauma, peak joy, first love)
- **Medium-emotion:** Compressed version, key details retained, long-term storage (meaningful conversations, travel)
- **Low-emotion:** Heavy compression, sparse details, medium-term storage (routine days, mundane tasks)
- **Zero-emotion:** Pruned within days, no storage (commutes, trivial moments)

---

## The Four-Tier Memory System

**Note:** Focus is huge for LACE - Working Memory represents active attentional focus.

```python
class MemoryStorage:
    """Hierarchical memory storage with four tiers"""

    # TIER 0: WORKING MEMORY (Current Focus)
    working_memory: List[Memory]
    capacity: int = 4-7  # Limited slots (Miller's Law)
    compression_level: float = 0.0  # No compression (full fidelity)
    duration: str = "seconds to minutes"
    accuracy: float = 0.99  # Near-perfect while held
    """
    Active attentional focus - what you're consciously processing RIGHT NOW

    Properties:
    - Extremely limited capacity (4-7 items maximum)
    - Zero compression (full detail while in focus)
    - Extremely short duration (seconds to minutes)
    - Near-perfect accuracy (99%)
    - Determines what gets encoded to long-term storage

    Examples:
    - Phone number you're about to dial
    - Sentence you're currently reading
    - Thought you're actively processing
    - Item you're searching for in room

    Critical: This is THE bottleneck for consciousness
    - All conscious processing passes through working memory
    - Overflow = immediate loss (forgotten instantly)
    - Attention direction = working memory allocation
    """

    # TIER 1: PERMANENT STORAGE (Emotional charge >= 0.70)
    permanent_memories: List[Memory]
    compression_level: float = 0.05  # 95% retention, minimal compression
    pruning_resistance: float = 0.99  # Almost never pruned
    storage_cost: float = HIGH  # Resource intensive
    accuracy: float = 0.95  # Very high accuracy on retrieval
    """
    High-fidelity, never pruned (survival priority)

    Examples:
    - Trauma (fear, pain - negative high-emotion)
    - Peak experiences (joy, love - positive high-emotion)
    - Life milestones (weddings, births, deaths)
    - First-time experiences with strong impact
    """

    # TIER 2: LONG-TERM STORAGE (Emotional charge 0.30-0.69)
    long_term_memories: List[Memory]
    compression_level: float = 0.50  # 50% retention, moderate compression
    pruning_resistance: float = 0.70  # Gradually fades if not accessed
    storage_cost: float = MEDIUM  # Balanced
    accuracy: float = 0.70  # Moderate accuracy (some details invented)
    """
    Compressed, pruned after years if unused

    Examples:
    - Meaningful conversations
    - Travel experiences
    - Learning milestones
    - Relationship memories (moderate significance)
    """

    # TIER 3: SHORT-TERM CACHE (Emotional charge < 0.30)
    short_term_cache: List[Memory]
    compression_level: float = 0.90  # 90% compression, sparse details
    pruning_resistance: float = 0.20  # Pruned within weeks/months
    storage_cost: float = LOW  # Minimal resources
    accuracy: float = 0.40  # Low accuracy (heavily invented on retrieval)
    """
    Heavily compressed, pruned within weeks/months

    Examples:
    - Routine commutes
    - Mundane meals
    - Typical workdays
    - Forgettable social interactions
    """

    # TIER 4: PRUNED ENTIRELY (Emotional charge ~0.0)
    # No storage - deleted within days
    # Cannot be retrieved (data loss)
    """
    No storage allocated, immediate pruning

    Examples:
    - Most moments of most days
    - Background environmental details
    - Transitions between activities
    - Countless micro-moments (blinking, breathing, walking)
    """
```

---

## Combined Compression Algorithm

Compression determined by multiple factors (not just emotion):

```python
def calculate_compression(memory: Memory, agent: Agent) -> float:
    """
    Determine compression level based on combined factors

    All factors influence compression:
    - Emotional charge (primary factor)
    - Time since encoding (older = more compressed)
    - Access frequency (unused = more compressed)
    - Survival relevance (threat patterns = less compressed)
    """

    # Factor 1: Emotional charge (50% weight)
    emotion_factor = 1.0 - memory.emotional_charge
    # High emotion (0.9) → low compression (0.1)
    # Low emotion (0.1) → high compression (0.9)

    # Factor 2: Time decay (25% weight)
    age = now() - memory.timestamp
    time_factor = min(1.0, age / (365 * 5))  # Max compression at 5 years
    # Recent → low additional compression
    # Old → high additional compression

    # Factor 3: Access frequency (15% weight)
    access_frequency = memory.access_count / max(1, age / 365)  # Accesses per year
    frequency_factor = 1.0 - min(1.0, access_frequency / 10)
    # Frequently accessed → low compression
    # Rarely accessed → high compression

    # Factor 4: Survival relevance (10% weight)
    if memory.is_survival_related():
        survival_factor = 0.0  # No additional compression for survival memories
    else:
        survival_factor = 0.5  # Some compression for non-survival

    # Combined compression score
    compression = (
        emotion_factor * 0.50 +
        time_factor * 0.25 +
        frequency_factor * 0.15 +
        survival_factor * 0.10
    )

    return min(0.95, max(0.05, compression))  # Clamp to 5-95%
```

**Key insight:** Old, rarely-accessed, low-emotion memories get maximum compression. Recent, frequently-accessed, high-emotion, survival-related memories resist compression.

---

## Pruning Mechanics (Threshold-Based)

**Trigger:** When storage capacity reached

```python
class MemoryPruner:
    """Garbage collection for memories when capacity threshold reached"""

    CAPACITY_THRESHOLD = 0.85  # Prune when 85% full

    def check_and_prune(self, agent: Agent) -> None:
        """
        Monitor storage capacity and prune when threshold reached
        """
        current_utilization = agent.memory_bank.storage_used / agent.memory_bank.max_storage

        if current_utilization >= self.CAPACITY_THRESHOLD:
            # Trigger pruning to free space
            self.prune_low_priority_memories(agent)

    def prune_low_priority_memories(self, agent: Agent) -> int:
        """
        Remove memories with lowest priority scores

        Pruning priority (prune in this order):
        1. Zero-emotion, old, never accessed
        2. Low-emotion, old, rarely accessed
        3. Medium-emotion, very old, never accessed
        4. High-emotion memories: NEVER pruned (permanent tier)
        """
        pruned_count = 0

        # Calculate prune score for each memory
        for memory in agent.memory_bank.all_memories():
            prune_score = self.calculate_prune_priority(memory)

            if prune_score >= PRUNE_THRESHOLD:
                agent.memory_bank.delete(memory)
                pruned_count += 1

                # Stop when enough space freed
                if agent.memory_bank.utilization < 0.70:  # Target 70%
                    break

        return pruned_count

    def calculate_prune_priority(self, memory: Memory) -> float:
        """
        Higher score = more likely to be pruned

        Survival memories: NEVER pruned (score always 0.0)
        """
        # Survival memories never pruned
        if memory.tier == "permanent" or memory.is_survival_related():
            return 0.0  # Absolute protection

        # Emotional charge (primary factor - 50%)
        emotional_factor = 1.0 - memory.emotional_charge

        # Time since last access (25%)
        time_since_access = now() - memory.last_accessed
        recency_factor = min(1.0, time_since_access / 365)

        # Age (15%)
        age_factor = min(1.0, (now() - memory.timestamp) / (365 * 5))

        # Access frequency (10%)
        access_frequency = memory.access_count / max(1, age_factor)
        frequency_factor = 1.0 - min(1.0, access_frequency / 10)

        # Combined prune score
        prune_score = (
            emotional_factor * 0.50 +
            recency_factor * 0.25 +
            age_factor * 0.15 +
            frequency_factor * 0.10
        )

        return prune_score
```

**Pruning rules:**
- **Permanent tier (survival):** NEVER pruned (automatic protection)
- **Long-term:** Pruned only if very old + charge reduced + never accessed
- **Short-term:** Pruned when capacity reached + low emotion + old
- **Working memory:** Automatically cleared when attention shifts (seconds to minutes)

---

## Memory Re-Encoding

**Memories CAN be re-encoded through processing AND new experiences:**

### Through Processing (Therapy, Reflection)

```python
def process_memory(memory: Memory, agent: Agent) -> Memory:
    """
    Conscious processing can reduce emotional charge

    Methods:
    - Therapy (EMDR, CBT, trauma processing)
    - Reflection (journaling, meditation on experience)
    - Forgiveness (releasing emotional charge)
    - Reframing (changing interpretation)
    """
    # Original encoding
    original_charge = memory.emotional_charge  # e.g., 0.85 (trauma)

    # Processing reduces charge
    processing_effect = apply_therapeutic_processing(memory, agent)
    new_charge = max(0.1, original_charge - processing_effect)

    # Update memory with reduced charge
    memory.emotional_charge = new_charge

    # If charge drops below thresholds, may move to lower tier
    if new_charge < 0.70 and memory.tier == "permanent":
        memory.tier = "long_term"  # No longer permanent
        memory.compression_level = 0.50  # Now compressible

    return memory
```

### Through New Experiences (Pattern Updating)

**Example: Dog fear re-encoding**

```python
def update_pattern_memory(old_experience: Memory, new_experience: Experience) -> Memory:
    """
    New experiences can update existing pattern memories

    Example: Fear of dogs updated by positive dog encounter
    """
    # Original memory: "Dogs are dangerous" (high fear, 0.80 charge)
    original_pattern = old_experience.pattern  # "dog → danger"
    original_charge = old_experience.emotional_charge  # 0.80 (fear)

    # New experience: Meet gentle dog, feel safe/joy
    new_pattern = new_experience.pattern  # "dog → safe/joy"
    new_charge = new_experience.emotional_charge  # 0.60 (positive)

    # System INTEGRATES both experiences (doesn't replace)
    integrated_pattern = {
        "dog": {
            "danger_response": original_charge * 0.40,  # Reduced weight
            "safe_response": new_charge * 0.60,         # New weight
        }
    }

    # New blended emotional charge
    blended_charge = (original_charge * 0.40 + new_charge * 0.60) / 2
    # Result: 0.50 charge (reduced from 0.80)

    # Update original memory with blended pattern
    old_experience.pattern = integrated_pattern
    old_experience.emotional_charge = blended_charge
    old_experience.note = "Updated through new experience"

    return old_experience
```

**Key insight:** New experiences don't erase old memories - they UPDATE the pattern by:
1. Adding new data points to the pattern
2. Reducing weight of old response
3. Increasing weight of new response
4. Blending emotional charges
5. Over time, positive experiences can fully re-encode negative pattern

**This is why:**
- Someone afraid of dogs can learn to love them (gradual re-encoding through repeated positive experiences)
- Trauma can heal through corrective experiences (not just therapy)
- Beliefs can change through contradictory evidence (pattern updating)

---

## Why Forgetting Is Beneficial (Full Section)

### The Necessity of Pruning

**If we remembered everything:**

```python
# Total experienced moments in 80-year life
conscious_hours = 80 * 365 * 16  # Awake hours
moments_per_hour = 3600  # Seconds
total_moments = conscious_hours * moments_per_hour
# Result: ~1.7 BILLION moments

# Storage at full fidelity
storage_per_moment = 1_MB  # Conservative estimate
total_storage_needed = total_moments * storage_per_moment
# Result: 1.7 PETABYTES of storage

# IMPOSSIBLE - system cannot support this
```

**Pruning is not failure - it's essential optimization.**

### Benefits of Forgetting

**1. Resource Efficiency**
- Finite storage capacity (brain/consciousness has limits)
- Full-fidelity storage unsustainable
- Compression/pruning frees resources for new experiences
- System optimizes by keeping only meaningful data

**2. Pattern Recognition Enhancement**
- Too much detail obscures patterns
- Compression reveals signal through noise reduction
- "Forgetting the trees to see the forest"
- Wisdom = distilled patterns, not raw data retention

**3. Emotional Healing**
- Charge reduction allows painful memories to fade
- Not erasure - but compression reduces emotional impact
- Old wounds become "scars" (present but not painful)
- Adaptive forgetting = moving forward from trauma

**4. Identity Flexibility**
- If all moments equally remembered, identity becomes rigid
- Selective memory allows identity evolution
- "I used to be X" possible because low-charge X-moments compressed/pruned
- Forgetting who you were enables becoming who you are

**5. Focus Optimization**
- Cannot attend to past AND present simultaneously
- Pruning past frees attention for now
- "Living in the past" = over-weighting compressed memories
- Healthy forgetting = presence in current moment

**6. Decision Clarity**
- Too many remembered options = analysis paralysis
- Pruning irrelevant experiences sharpens decision-making
- Keep the lessons, prune the details
- "I learned X from that experience" (lesson retained, details compressed)

**7. Relationship Renewal**
- Forgetting minor conflicts allows relationship repair
- If every slight perfectly remembered = accumulating resentment
- Healthy relationships require selective forgetting
- "Letting go" = allowing low-charge conflicts to compress/prune

### What Gets Kept vs Pruned

**The system prioritizes:**

**KEEP (high-fidelity, resist pruning):**
- Survival-critical information (threats, safety, danger patterns)
- High-emotion experiences (trauma, joy, love, milestones)
- Frequently-accessed patterns (skills, knowledge, relationships)
- Recent experiences (working memory → consolidation period)

**COMPRESS (reduced fidelity, keep outline):**
- Medium-emotion experiences (meaningful but not pivotal)
- Moderately-used patterns (occasional reference)
- Aging memories with reduced charge (healed trauma)

**PRUNE (complete deletion):**
- Zero-emotion moments (routine, trivial, background)
- Never-accessed memories (encoded but never retrieved)
- Extremely old low-charge data (decades-old mundane moments)
- Capacity-constrained garbage collection (make room for new)

---

## Retrieval Accuracy by Tier

**Per-tier accuracy tracking:**

| Tier | Compression | Accuracy | Characteristics |
|------|-------------|----------|----------------|
| **Working Memory** | 0% | 99% | Perfect while held, instant loss if attention shifts |
| **Permanent** | 5% | 95% | Very accurate, minimal gaps, mostly factual |
| **Long-term** | 50% | 70% | Moderate accuracy, some details invented to fill gaps |
| **Short-term** | 90% | 40% | Low accuracy, heavily reconstructed, many gaps filled with inference |
| **Pruned** | 100% | 0% | Complete data loss, cannot be retrieved |

**Key insight:** "Remembering" = reconstruction, not playback. Gaps filled with:
- Current beliefs (what makes sense now)
- Narrative coherence (what fits the story)
- Similar memories (pattern matching)
- Inference (what "must have" happened)

**You don't remember what happened - you remember a reconstruction based on compressed data + current state.**

---

## Integration with Other Concepts

**Memory compression & pruning connects to:**

- **[Cache vs Live Processing](21_cache_vs_live_processing.md)** - What gets cached is what gets remembered
- **[System Resource Allocation](20_system_resource_allocation.md)** - Memory storage consumes finite resources
- **[Perceptual Sampling Rate](19_perceptual_sampling_rate.md)** - Sampling rate determines what enters memory
- **[MemoryBank](../../01_foundation/base_structure/03_data_models/08_data_model_memory_bank.md)** - Storage tiers and compression structure
- **[Consciousness Scale](14_consciousness_scale_framework.md)** - Higher consciousness = better encoding initially

---

## Technical Implementation

For implementation details, see:
- **MemoryBank data model** - Four-tier storage structure with compression/pruning
- **Memory Pruner daemon** - System-level garbage collection
- **Tier 3 Emotional Forces** - Emotional charge determines encoding fidelity

---

**Previous:** [22 Manifestation Latency](22_manifestation_latency.md) | **Next:** [24 The Grip Mechanism](24_grip_mechanism.md)
