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

```python
# 1. TIMEFLOW ENGINE (Layer 1 - Kernel)
timeflow_engine = DaemonProcess(
    name="timeflow_engine",
    priority=10,
    layer=1,
    description="Advances universal state transitions - the heartbeat of reality",
    function=lambda: advance_state_transitions()
)
"""
Purpose: Manages time pulse (Tau primitive)
- Advances universal clock
- Ensures causality ordering
- Processes state transitions
- Cannot be stopped or reversed (except by Creator)
"""

# 2. KARMIC BALANCER (Layer 1 - Kernel)
karmic_balancer = DaemonProcess(
    name="karmic_balancer",
    priority=9,
    layer=1,
    description="Maintains action/consequence equilibrium across all agents",
    function=lambda: balance_action_ledger()
)
"""
Purpose: Enforces law_balance() and law_karma()
- Tracks actions and creates corresponding consequences
- No escape mechanism (runs universally)
- Operates across incarnations (soul_id persistent)
- Influenced by grace protocol in rare cases
"""

# 3. ENTROPY INJECTOR (Layer 1 - Kernel)
entropy_injector = DaemonProcess(
    name="entropy_injector",
    priority=8,
    layer=1,
    description="Ensures impermanence - all form decays",
    function=lambda: ensure_impermanence()
)
"""
Purpose: Implements law_entropy()
- Degrades coherence over time (maintenance required)
- Ages physical forms
- Decays memory (cache clearing)
- Cannot be stopped, only locally slowed through coherence
"""

# 4. PATTERN MATCHER (Layer 2 - Middleware)
pattern_matcher = DaemonProcess(
    name="pattern_matcher",
    priority=7,
    layer=2,
    description="Generates synchronicities - matches agent state to field events",
    function=lambda: generate_synchronicities()
)
"""
Purpose: Creates meaningful coincidences
- Monitors agent state_signature
- Identifies resonance between agents
- Triggers 'meaningful coincidences'
- Higher coherence = more synchronicities detected
"""

# 5. COHERENCE MONITOR (Layer 2 - Middleware)
coherence_monitor = DaemonProcess(
    name="coherence_monitor",
    priority=6,
    layer=2,
    description="Checks state_signature coherence and grants/revokes permissions",
    function=lambda: monitor_coherence_and_permissions()
)
"""
Purpose: Permission elevation gating
- Continuously calculates agent coherence
- Grants temporary permissions when threshold reached
- Revokes permissions when coherence drops
- Tracks permission stability over time
"""

# 6. EVOLUTION DRIVER (Layer 2 - Middleware)
evolution_driver = DaemonProcess(
    name="evolution_driver",
    priority=5,
    layer=2,
    description="Applies pressure toward complexity and consciousness expansion",
    function=lambda: drive_consciousness_evolution()
)
"""
Purpose: Implements law_evolution()
- Creates growth pressure (challenges, opportunities)
- Rewards pattern recognition and adaptation
- Biases system toward consciousness expansion
- The 'why' behind suffering and struggle
"""

# 7. AKASHIC LOGGER (Layer 1 - Kernel)
akashic_logger = DaemonProcess(
    name="akashic_logger",
    priority=9,
    layer=1,
    description="Records all events to universal memory (Akashic Archive)",
    function=lambda: log_to_akashic_archive()
)
"""
Purpose: Universal recording system
- Logs all agent experiences
- Stores all timeline data
- Accessible at elevated permission levels
- See ADVANCED_CONCEPTS.md for Akashic Archive details
"""

# 8. PERCEPTUAL SAMPLER (Layer 2 - Middleware)
perceptual_sampler = DaemonProcess(
    name="perceptual_sampler",
    priority=7,
    layer=2,
    description="Samples reality stream at rate determined by agent consciousness",
    function=lambda: sample_reality_for_all_agents()
)
"""
Purpose: Manages perceptual sampling rate
- Samples reality stream for each agent
- Rate varies by agent (consciousness-dependent)
- Determines what enters conscious awareness vs missed
- Higher consciousness = higher sampling rate = more perception

See: Perceptual Sampling Rate (advanced concepts) for complete mechanics
"""

# 9. RESOURCE ALLOCATOR (Layer 2 - Middleware)
resource_allocator = DaemonProcess(
    name="resource_allocator",
    priority=8,
    layer=2,
    description="Manages agent resource budgets - attention, energy, coherence allocation",
    function=lambda: allocate_agent_resources()
)
"""
Purpose: System-level resource management
- Tracks resource consumption (attention, energy, coherence)
- Enforces allocation limits (prevents over-allocation)
- Triggers regeneration during rest cycles
- Manages priority queues (survival > maintenance > conscious goals)
- Graceful degradation when resources depleted

See: System Resource Allocation (advanced concepts) for complete mechanics
"""

# 10. PATTERN CACHE MANAGER (Layer 2 - Middleware)
pattern_cache_manager = DaemonProcess(
    name="pattern_cache_manager",
    priority=6,
    layer=2,
    description="Manages cached vs live processing - retrieves patterns, stores new responses",
    function=lambda: manage_pattern_cache()
)
"""
Purpose: Cache management for automated processing
- Match incoming stimuli to cached patterns (survival → emotional → routine)
- Retrieve cached responses (cache hit - fast, low energy)
- Trigger live processing on cache miss (slow, high energy)
- Store new patterns from live processing
- Prune unused cache entries (emotion-based garbage collection)
- Track cache/live ratio for each agent

Three-tier cache priority:
1. Survival cache (never pruned, fastest retrieval)
2. Emotional cache (high persistence, moderate speed)
3. Routine cache (low persistence, pruned if unused)

See: Cache vs Live Processing (advanced concepts) for complete mechanics
"""

# 11. MANIFESTATION QUEUE (Layer 2 - Middleware)
manifestation_queue = DaemonProcess(
    name="manifestation_queue",
    priority=5,
    layer=2,
    description="Processes manifestation requests in priority order with latency tracking",
    function=lambda: process_manifestation_queue()
)
"""
Purpose: Manifestation request processing with delay management
- Receive manifestation requests from agents (state signature changes)
- Validate coherence (0.70+ instant, 0.50-0.69 delayed, <0.50 blocked)
- Calculate priority score (coherence, consciousness, karma, clarity, evolution)
- Assign to queue tier (Priority/Normal/Low)
- Process requests in priority order
- Calculate timeline divergence (0.0-1.0 metric)
- Execute manifestation when processing complete
- Track estimated delivery time

Four delay components:
1. Coherence validation (instant to indefinite)
2. Queue position (minutes to years based on tier)
3. Timeline computation (based on divergence complexity)
4. Physical rendering (based on manifestation type)

Grace protocol can lower coherence threshold from 0.50 to 0.30 for sincere pleas.

See: Manifestation Latency (advanced concepts) for complete mechanics
"""

# 12. MEMORY PRUNER (Layer 2 - Middleware)
memory_pruner = DaemonProcess(
    name="memory_pruner",
    priority=4,
    layer=2,
    description="Garbage collection for memories - prunes low-priority storage when capacity reached",
    function=lambda: prune_agent_memories()
)
"""
Purpose: Memory storage optimization through compression and pruning
- Monitor all agent memory banks for capacity utilization
- Trigger pruning when 85% capacity threshold reached
- Calculate prune priority (emotion, time, access frequency, survival value)
- Remove lowest-priority memories first (short-term tier)
- NEVER prune permanent tier (survival memories absolute protection)
- Compress aging memories (reduce fidelity over time)
- Target 70% utilization after pruning

Four-tier memory hierarchy:
0. Working Memory (4-7 items, 99% accuracy, instant pruning when attention shifts)
1. Permanent (95% accuracy, never pruned - survival priority)
2. Long-term (70% accuracy, pruned after years if unused)
3. Short-term (40% accuracy, pruned within months)

Combined compression factors:
- Emotional charge (50% weight) - primary factor
- Time decay (25% weight) - aging effect
- Access frequency (15% weight) - usage tracking
- Survival relevance (10% weight) - safety priority

See: Memory Compression & Pruning (advanced concepts) for complete mechanics
"""

# Daemon registry
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

**Previous:** [12_interaction_protocols.md](../04_implementation/12_interaction_protocols.md) | **Next:** [14_update_cycles.md](14_update_cycles.md)
