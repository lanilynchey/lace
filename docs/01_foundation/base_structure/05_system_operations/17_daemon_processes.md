# Daemon Processes

Background operations that run continuously - cannot be stopped by agents.

```python
class DaemonProcess:
    """Always-running system operation"""

    name: str
    priority: int              # 0=low, 10=critical
    layer: int                 # Which system layer it operates on
    description: str

    def run(self) -> None:
        """Execute daemon logic"""
        pass
```

## The Twelve Core Daemons

### 1. Timeflow Engine (Layer 1 - Kernel)

```python
timeflow_engine = DaemonProcess(
    name="timeflow_engine",
    priority=10,
    layer=1,
    description="Advances universal state transitions - the heartbeat of reality",
    function=lambda: advance_state_transitions()
)
```

**Purpose:** Manages time pulse (Tau primitive)
- Advances universal clock
- Ensures causality ordering
- Processes state transitions
- Cannot be stopped or reversed (except by Creator)

### 2. Karmic Balancer (Layer 1 - Kernel)

```python
karmic_balancer = DaemonProcess(
    name="karmic_balancer",
    priority=9,
    layer=1,
    description="Maintains action/consequence equilibrium across all agents",
    function=lambda: balance_action_ledger()
)
```

**Purpose:** Enforces law_balance() and law_karma()
- Tracks actions and creates corresponding consequences
- No escape mechanism (runs universally)
- Operates across incarnations (soul_id persistent)
- Influenced by grace protocol in rare cases

### 3. Entropy Injector (Layer 1 - Kernel)

```python
entropy_injector = DaemonProcess(
    name="entropy_injector",
    priority=8,
    layer=1,
    description="Ensures impermanence - all form decays",
    function=lambda: ensure_impermanence()
)
```

**Purpose:** Implements law_entropy()
- Degrades coherence over time (maintenance required)
- Ages physical forms
- Decays memory (cache clearing)
- Cannot be stopped, only locally slowed through coherence

### 4. Pattern Matcher (Layer 2 - Middleware)

```python
pattern_matcher = DaemonProcess(
    name="pattern_matcher",
    priority=7,
    layer=2,
    description="Generates synchronicities - matches agent state to field events",
    function=lambda: generate_synchronicities()
)
```

**Purpose:** Creates meaningful coincidences
- Monitors agent state_signature
- Identifies resonance between agents
- Triggers 'meaningful coincidences'
- Higher coherence = more synchronicities detected

### 5. Coherence Monitor (Layer 2 - Middleware)

```python
coherence_monitor = DaemonProcess(
    name="coherence_monitor",
    priority=6,
    layer=2,
    description="Checks state_signature coherence and grants/revokes permissions",
    function=lambda: monitor_coherence_and_permissions()
)
```

**Purpose:** Permission elevation gating
- Continuously calculates agent coherence
- Grants temporary permissions when threshold reached
- Revokes permissions when coherence drops
- Tracks permission stability over time

### 6. Evolution Driver (Layer 2 - Middleware)

```python
evolution_driver = DaemonProcess(
    name="evolution_driver",
    priority=5,
    layer=2,
    description="Applies pressure toward complexity and consciousness expansion",
    function=lambda: drive_consciousness_evolution()
)
```

**Purpose:** Implements evolutionary growth pressure — see [law_transformation(): Evolution as Transformation with Memory](../../../03_mechanics/system_laws/03_additional_laws/22_law_transformation.md#evolution-transformation-with-memory) and [Evolutionary Process](../../../04_advanced/advanced_concepts/12_evolutionary_process.md)
- Creates growth pressure (challenges, opportunities)
- Rewards pattern recognition and adaptation
- Biases system toward consciousness expansion
- The 'why' behind suffering and struggle

### 7. Akashic Logger (Layer 1 - Kernel)

```python
akashic_logger = DaemonProcess(
    name="akashic_logger",
    priority=9,
    layer=1,
    description="Records all events to universal memory (Akashic Archive)",
    function=lambda: log_to_akashic_archive()
)
```

**Purpose:** Universal recording system
- Logs all agent experiences
- Stores all timeline data
- Accessible at elevated permission levels
- See: [Akashic Archive](../../../04_advanced/advanced_concepts/05_akashic_archive/19_what_is_akashic.md) for complete architecture

### 8. Perceptual Sampler (Layer 2 - Middleware)

```python
perceptual_sampler = DaemonProcess(
    name="perceptual_sampler",
    priority=7,
    layer=2,
    description="Samples reality stream at rate determined by agent consciousness",
    function=lambda: sample_reality_for_all_agents()
)
```

**Purpose:** Manages perceptual sampling rate
- Samples reality stream for each agent
- Rate varies by agent (consciousness-dependent)
- Determines what enters conscious awareness vs missed
- Higher consciousness = higher sampling rate = more perception

**See:** [Perceptual Sampling Rate](../../../04_advanced/advanced_concepts/19_perceptual_sampling_rate.md) for complete mechanics

### 9. Resource Allocator (Layer 2 - Middleware)

```python
resource_allocator = DaemonProcess(
    name="resource_allocator",
    priority=8,
    layer=2,
    description="Manages agent resource budgets - attention, energy, coherence allocation",
    function=lambda: allocate_agent_resources()
)
```

**Purpose:** System-level resource management
- Tracks resource consumption (attention, energy, coherence)
- Enforces allocation limits (prevents over-allocation)
- Triggers regeneration during rest cycles
- Manages priority queues (survival > maintenance > conscious goals)
- Graceful degradation when resources depleted

**See:** [System Resource Allocation](../../../04_advanced/advanced_concepts/20_system_resource_allocation.md) for complete mechanics

### 10. Pattern Cache Manager (Layer 2 - Middleware)

```python
pattern_cache_manager = DaemonProcess(
    name="pattern_cache_manager",
    priority=6,
    layer=2,
    description="Manages cached vs live processing - retrieves patterns, stores new responses",
    function=lambda: manage_pattern_cache()
)
```

**Purpose:** Cache management for automated processing
- Match incoming stimuli to cached patterns (survival → emotional → routine)
- Retrieve cached responses (cache hit - fast, low energy)
- Trigger live processing on cache miss (slow, high energy)
- Store new patterns from live processing
- Prune unused cache entries (emotion-based garbage collection)
- Track cache/live ratio for each agent

**Three-tier cache priority:**
1. Survival cache (never pruned, fastest retrieval)
2. Emotional cache (high persistence, moderate speed)
3. Routine cache (low persistence, pruned if unused)

**See:** [Cache vs Live Processing](../../../04_advanced/advanced_concepts/21_cache_vs_live_processing.md) for complete mechanics

### 11. Manifestation Queue (Layer 2 - Middleware)

```python
manifestation_queue = DaemonProcess(
    name="manifestation_queue",
    priority=5,
    layer=2,
    description="Processes manifestation requests in priority order with latency tracking",
    function=lambda: process_manifestation_queue()
)
```

**Purpose:** Manifestation request processing with delay management
- Receive manifestation requests from agents (state signature changes)
- Validate coherence (0.70+ instant, 0.50-0.69 delayed, <0.50 blocked)
- Calculate priority score (coherence, consciousness, karma, clarity, evolution)
- Assign to queue tier (Priority/Normal/Low)
- Process requests in priority order
- Calculate timeline divergence (0.0-1.0 metric)
- Execute manifestation when processing complete
- Track estimated delivery time

**Four delay components:**
1. Coherence validation (instant to indefinite)
2. Queue position (minutes to years based on tier)
3. Timeline computation (based on divergence complexity)
4. Physical rendering (based on manifestation type)

Grace protocol can lower coherence threshold from 0.50 to 0.30 for sincere pleas.

**See:** [Manifestation Latency](../../../04_advanced/advanced_concepts/22_manifestation_latency.md) for complete mechanics

### 12. Memory Pruner (Layer 2 - Middleware)

```python
memory_pruner = DaemonProcess(
    name="memory_pruner",
    priority=4,
    layer=2,
    description="Garbage collection for memories - prunes low-priority storage when capacity reached",
    function=lambda: prune_agent_memories()
)
```

**Purpose:** Memory storage optimization through compression and pruning
- Monitor all agent memory banks for capacity utilization
- Trigger pruning when 85% capacity threshold reached
- Calculate prune priority (emotion, time, access frequency, survival value)
- Remove lowest-priority memories first (short-term tier)
- NEVER prune permanent tier (survival memories absolute protection)
- Compress aging memories (reduce fidelity over time)
- Target 70% utilization after pruning

**Four-tier memory hierarchy:**
0. Working Memory (4-7 items, 99% accuracy, instant pruning when attention shifts)
1. Permanent (95% accuracy, never pruned - survival priority)
2. Long-term (70% accuracy, pruned after years if unused)
3. Short-term (40% accuracy, pruned within months)

**Combined compression factors:**
- Emotional charge (50% weight) - primary factor
- Time decay (25% weight) - aging effect
- Access frequency (15% weight) - usage tracking
- Survival relevance (10% weight) - safety priority

**See:** [Memory Compression & Pruning](../../../04_advanced/advanced_concepts/23_memory_compression_pruning.md) for complete mechanics

## Daemon Registry

```python
daemons = [
    timeflow_engine,
    karmic_balancer,
    entropy_injector,
    pattern_matcher,
    coherence_monitor,
    evolution_driver,
    akashic_logger,
    perceptual_sampler,
    resource_allocator,
    pattern_cache_manager,
    manifestation_queue,
    memory_pruner
]
```

**Properties:**
- Daemons run continuously (no pause, no stop for agents)
- Elevated beings (mystics, masters) can **influence** but not override
- Only Creator has kill/restart privileges
- Priority determines execution order when conflicts occur

---

**Previous:** [16_interaction_protocols.md](../04_implementation/16_interaction_protocols.md) | **Next:** [18_update_cycles.md](18_update_cycles.md)
