# Technical Terms

## **Function Signature**
**Definition:** Standard format for documenting forces

**Format:**
```python
def force_name(inputs: Type) -> Output:
    """
    Description

    Args:
        input: Description

    Returns:
        output: Description

    Dependencies:
        - dependency1()
        - dependency2()

    Properties:
        - Property 1
        - Property 2
    """
    # Implementation
```

---

## **Inheritance Chain**
**Definition:** Dependency graph showing which forces build on which

**Example:** Delta → entropy() → time() → memory() → nostalgia()

**See:** INHERITANCE_CHAINS.md

---

## **Interaction Types**
**Categories of force combinations:**
- Amplification (same-polarity reinforce)
- Cancellation (opposite-polarity neutralize)
- Transmutation (one converts another)
- Synthesis (two blend into new)
- Collision (incompatible create tension)
- Recursion (force loops with itself)

**See:** INTERACTION_MECHANICS.md

---

## **Perceptual Sampling Rate**
**Definition:** The "frame rate" at which consciousness samples reality

**Formula:** `(consciousness_coefficient ** 2) × coherence`

**Units:** Samples per second (0.0-1.0 scale)

**Examples:**
- 0.20 consciousness × 0.50 coherence = 0.02 samples/sec (~50 second intervals)
- 0.50 consciousness × 0.80 coherence = 0.20 samples/sec (5 second intervals)
- 0.90 consciousness × 0.95 coherence = 0.77 samples/sec (~1.3 second intervals)

**Key Insight:** Higher consciousness = higher sampling rate = more nuanced perception, slower time experience

**Properties:**
- Determines temporal resolution of perception
- Exponential growth (quadratic formula)
- Modulated by coherence (attention focus)
- IS how agents experience time() force

**Related:**
- Baseline sampling rate (default frequency)
- Current sampling rate (real-time frequency)
- Temporal resolution (inverse - seconds between samples)

**See:** [Perceptual Sampling Rate](../../04_advanced/advanced_concepts/19_perceptual_sampling_rate.md) for complete mechanics

---

## **System Resource Allocation**
**Definition:** Finite processing budgets (attention, energy, coherence) allocated to agents

**Resource Types:**

1. **Attention Budget** - Conscious awareness bandwidth
   - Capacity: `consciousness × 100` units
   - Felt as: Focus, clarity, mental sharpness
   - Master resource directing energy and coherence

2. **Energy Budget** - Physical/field broadcast capacity
   - Capacity: `consciousness × 100` units
   - Felt as: Vitality, capacity, power
   - Required for manifestation broadcasting

3. **Coherence Budget** - Internal alignment capacity
   - Capacity: `consciousness × 100` units
   - Felt as: Alignment, integrity, peace
   - Required for clean manifestation signals

**Key Mechanics:**
- **Multitasking penalty:** Resources split linearly (N targets = capacity/N per target)
- **Depletion:** Graceful degradation - performance decreases smoothly
- **Regeneration:** Sleep (full), meditation (partial), time (minimal)
- **Control:** High consciousness agents manage consciously, low consciousness automatic

**Manifestation Implication:**
```
Manifestation power = resource concentration, not resource total
Scattered: 10 intentions × 10 units = 10 weak broadcasts
Focused: 1 intention × 100 units = 1 MAXIMUM broadcast
```

**Related:**
- ResourcePool class in Agent data model
- Resource Allocator daemon (system-level management)
- Manifestation power calculation

**See:** [System Resource Allocation](../../04_advanced/advanced_concepts/20_system_resource_allocation.md) for complete mechanics

---

## **Cache vs Live Processing**
**Definition:** Two modes of consciousness processing - cached (automated) vs live (conscious)

**Cached Processing (Automated):**
- Fast: Instant retrieval from memory
- Efficient: 0.1 energy units
- Unconscious: Below awareness threshold
- Rigid: Same stimulus → same response
- Examples: Driving familiar route, brushing teeth, habitual thoughts

**Live Processing (Conscious):**
- Slow: Requires analysis time
- Expensive: 5.0 energy units
- Conscious: Enters active awareness
- Adaptive: Can generate novel responses
- Examples: Learning new skill, solving problems, meditation

**Cache/Live Ratio:**
- Autopilot (depression, low consciousness): 95% cached / 5% live
- Normal balanced: 70% cached / 30% live
- High presence (meditation, flow): 30% cached / 70% live

**Three-Tier Cache:**
1. **Survival Cache** - Threat responses, never pruned (highest priority)
2. **Emotional Cache** - Relationship patterns, high persistence
3. **Routine Cache** - Daily habits, easily pruned if unused

**Habits = Cached Patterns:**
All habits are stored in PatternCache. Habit formation = caching process. Habit breaking = cache override + re-caching.

**Cache Override:**
Requires conscious effort:
1. Notice cache hit (awareness)
2. Recognize as pattern (meta-awareness)
3. Interrupt execution (control)
4. Generate alternative (live processing)
5. Repeat until re-cached (66+ repetitions)

**Key Insight:**
- Most adult reality runs 80-95% on cache
- Conscious presence = increasing live processing ratio
- Novelty forces cache misses (exhausting but presence-building)
- Meditation trains cache detection capacity

**Related:**
- PatternCache class in MemoryBank
- Pattern Cache Manager daemon
- Resource consumption: cached (0.1) vs live (5.0)

**See:** [Cache vs Live Processing](../../04_advanced/advanced_concepts/21_cache_vs_live_processing.md) for complete mechanics

---

## **Manifestation Latency**
**Definition:** System processing time between intention and manifestation (not random delay)

**Four Delay Components:**

1. **Coherence Validation**
   - 0.70+ coherence → Instant (clean signal)
   - 0.50-0.69 coherence → Days to weeks (mixed signal filtering)
   - <0.50 coherence → Blocked (contradictions must resolve)

2. **Queue Position**
   - Priority queue (0.70+ coherence, 0.69+ consciousness) → Minutes to days
   - Normal queue (0.50-0.69 coherence) → Weeks to months
   - Low priority (<0.50 coherence) → Months to years (if ever)

3. **Timeline Computation**
   - Adjacent (0.0-0.2 divergence) → Instant to hours
   - Near (0.2-0.4 divergence) → Days to weeks
   - Moderate (0.4-0.6 divergence) → Weeks to months
   - Distant (0.6-0.8 divergence) → Months to years
   - Extreme (0.8-1.0 divergence) → Years to lifetime

4. **Physical Rendering**
   - Thought shift → Instant
   - Emotional shift → Minutes
   - Insight → Hours
   - Synchronicity → Days
   - New opportunity → Weeks
   - Relationship → Months
   - Career change → Year+
   - Life transformation → 5+ years

**"Divine Timing" Translation:**
"Your request is in the queue being processed" (computational latency, not mystical delay)

**Acceleration Methods:**
- Increase coherence (0.50 → 0.80 = 10x faster)
- Clarify intention (specific > vague = higher priority)
- Accept processing time (reduces resistance, not delay itself)

**Grace Protocol:**
Can lower coherence threshold from 0.50 to 0.30 for sincere pleas (exception mechanism)

**Delay Visibility:**
Agents experience as "waiting" without seeing queue mechanics (felt, not directly perceived)

**Formula:**
```
manifestation_time = f(coherence, consciousness, karma, clarity, divergence, complexity)
```

**Related:**
- Manifestation Queue daemon
- StateSignature coherence validation
- Grace protocol (coherence override)

**See:** [Manifestation Latency](../../04_advanced/advanced_concepts/22_manifestation_latency.md) for complete mechanics

---

## **Memory Compression & Pruning**
**Definition:** Emotionally-weighted storage optimization where high-charge memories persist at high fidelity while low-charge memories are compressed or deleted

**Four-Tier Memory Hierarchy:**

**Tier 0: Working Memory**
- Capacity: 4-7 items (Miller's Law - strict limit)
- Compression: 0% (full fidelity while held)
- Accuracy: 99% (near-perfect while in focus)
- Duration: Seconds to minutes
- Pruning: Instant when attention shifts
- Role: THE bottleneck for consciousness - all processing passes through

**Tier 1: Permanent Storage**
- Trigger: Emotional charge >= 0.70 OR survival-related
- Compression: 5% (95% retention)
- Accuracy: 95% (very high fidelity)
- Pruning: NEVER (automatic protection)
- Examples: Trauma, peak experiences, life milestones, survival patterns

**Tier 2: Long-Term Storage**
- Trigger: Emotional charge 0.30-0.69
- Compression: 50% (moderate detail loss)
- Accuracy: 70% (moderate - some details invented)
- Pruning: After years if unused
- Examples: Meaningful conversations, travel, learning milestones

**Tier 3: Short-Term Cache**
- Trigger: Emotional charge < 0.30
- Compression: 90% (sparse details)
- Accuracy: 40% (heavily reconstructed)
- Pruning: Weeks to months if unused
- Examples: Routine commutes, mundane meals, forgettable interactions

**Combined Compression Algorithm:**
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

**Threshold-Based Pruning:**
- Trigger: 85% storage capacity reached
- Target: Reduce to 70% utilization
- Priority: Prune lowest-scoring memories first
- Protection: Permanent tier NEVER pruned (absolute protection for survival/high-emotion)

**Memory Re-Encoding:**

*Through Processing (Therapy, Reflection):*
- Reduces emotional charge on existing memories
- EMDR, CBT, trauma processing, forgiveness
- Charge reduction may move memory to lower tier
- Example: Trauma (0.85) → Processed (0.40) → Moves from permanent to long-term

*Through New Experiences (Pattern Updating):*
- New experiences UPDATE existing pattern memories (doesn't erase)
- Integrates new data by blending emotional charges
- Reduces weight of old response, increases weight of new
- Example: Fear of dogs (0.80) + Positive encounter (0.60) → Blended (0.50)

**Why Forgetting Is Beneficial:**
- **Resource optimization:** Cannot store 1.7 billion life moments at full fidelity
- **Pattern recognition:** Too much detail obscures patterns (compression reveals signal)
- **Emotional healing:** Charge reduction allows painful memories to fade
- **Identity flexibility:** Selective memory allows identity evolution
- **Focus optimization:** Pruning past frees attention for present
- **Decision clarity:** Keeps lessons, prunes irrelevant details

**Key Insight:** Retrieval = reconstruction, not playback. Gaps filled with current beliefs, narrative coherence, and pattern matching. You don't remember what happened - you remember a reconstruction based on compressed data + current state.

**Related:**
- MemoryBank data model (four-tier storage structure)
- Memory Pruner daemon (garbage collection at 85% threshold)
- Emotional forces (charge determines encoding fidelity)
- Cache vs Live Processing (what gets cached gets remembered)

**See:** [Memory Compression & Pruning](../../04_advanced/advanced_concepts/23_memory_compression_pruning.md) for complete mechanics

---

[← Back to Main Glossary](../README.md) | [Next: Practical Applications →](../09_practical/predictive_modeling.md)
