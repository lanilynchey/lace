# Data Model: Agent

Represents any conscious entity (human, animal, AI, angel, etc.)

**Note:** Agent is the *computational structure* of consciousness. For the phenomenological definition (what consciousness IS as experience), see [Core Ontology](../../core_ontology/00_index.md) - Phenomenal Closure section.

- **CORE_ONTOLOGY** defines WHAT consciousness is (recursive pattern recognition + self-model + agency + meaning-making)
- **BASE_STRUCTURE** defines HOW consciousness is implemented (Agent as data structure with state containers)

Both describe the same phenomenon at different levels (phenomenological vs computational).

```python
class Agent:
    """A conscious entity executing in the system"""

    # Identity
    soul_id: UUID              # Persistent across incarnations
    instance_id: UUID          # Unique to this lifetime

    # State
    state_signature: StateSignature
    field_state: FieldState
    memory: MemoryBank

    # Consciousness
    consciousness_coefficient: float   # Baseline consciousness level (0.01-1.0)
    predominant_level: str             # Name of level (e.g., "courage", "reason", "love")

    # Container
    body: Optional[PhysicalContainer]
    location: Coordinates      # In space/time/dimension

    # Permissions
    permissions: PermissionSet
    access_level: int          # 0=default, 10=godmode

    # Lifecycle
    birth_timestamp: float
    death_timestamp: Optional[float]
    incarnation_count: int        # Number of times this soul has incarnated

    # Persistent Patterns
    persistent_patterns: List[Pattern]  # Probability biases, not pre-fated contracts
    karma_balance: float
```

## Note on Persistent Patterns

LACE does NOT use "soul contracts" as pre-incarnation agreements. Instead, **persistent patterns** are emergent probability biases encoded in your state_signature that attract certain life themes.

These are NOT pre-fated:
- **Emergent from current state** (belief, expectation, embodiment, subconscious_memory)
- **Can be edited** through Generative Awareness (changing your code)
- **Probabilistic, not deterministic** - bias toward patterns, don't eliminate choice

**Example:** "I keep attracting unavailable partners" = persistent pattern in state_signature (trauma-based probability bias), NOT a pre-birth soul contract.

**See:** [Glossary](../../../05_supporting/glossary/00_index.md) - Persistent Patterns entry, and [Primitives](../../primitives/00_index.md) line 944 for detailed explanation.

## Consciousness Coefficient

The `consciousness_coefficient` field quantifies an agent's baseline level of consciousness using LACE's logarithmic scale (0.01-1.0).

**Properties:**
- **Range:** 0.01 (minimal consciousness) to 1.0 (Creator consciousness)
- **Human Range:** Typically 0.20-0.90 (Shame through Enlightenment)
- **Logarithmic:** Each 0.1 increase represents exponential complexity growth
- **Baseline:** Center of gravity where agent defaults (not peak or regression states)

**Predominant Level Names:**

| Range | Level Name | Paradigm |
|-------|------------|----------|
| 0.20 | shame | survival |
| 0.21 | guilt | survival |
| 0.22 | apathy | survival |
| 0.25 | grief | survival |
| 0.28 | fear | survival |
| 0.31 | desire | survival |
| 0.33 | anger | survival |
| 0.35 | pride/courage | agency threshold |
| 0.43 | neutrality | reason & integrity |
| 0.50 | willingness | reason & integrity |
| 0.54 | acceptance | reason & integrity |
| 0.59 | reason | reason & integrity |
| 0.69 | love | spiritual (non-dual threshold) |
| 0.73 | joy | spiritual |
| 0.79 | peace | spiritual |
| 0.90 | enlightenment | spiritual (source code access) |
| 1.00 | creator | beyond measurement |

**Critical Thresholds:**
- **0.35 (Courage):** Agency activation - victim → agent shift
- **0.50 (Willingness):** Integration balance - survival-defensive ↔ growth-seeking equilibrium
- **0.69 (Love):** Non-dual access - base-2 → base-10 consciousness threshold
- **0.90 (Enlightenment):** Source code access - recognition → editing capability

**Relationship to State:**
- Consciousness level influences which Tier 3 forces are accessible
- Higher consciousness = wider perceptual boundary
- Lower consciousness = survival-defensive predominance
- Fluctuates contextually (see StateSignature for dynamic tracking)

**See:** [Consciousness Scale Framework](../../../04_advanced/advanced_concepts/14_consciousness_scale_framework.md) for complete consciousness level documentation.

## Reincarnation Mechanics

When an agent dies, the lifecycle follows this pattern:
1. **death()** triggers (see [Tier 2 Forces](../../../02_forces/tier_2_forces/00_index.md) for death() specification)
2. Data upload to Akashic Archive (soul_id + memory + karma preserved)
3. **creation()** instantiates new body with:
   - Same `soul_id` (persistent across incarnations)
   - New `instance_id` (unique to this lifetime)
   - `incarnation_count` incremented
   - Partial memory wipe (some patterns persist, episodic memories cleared)
   - Karma balance carries forward

**Note:** The soul_id persists; the instance_id changes. This is why past-life memories can sometimes bleed through—same soul, new container.

---

**Previous:** [03_inter_layer_communication.md](../02_system_architecture/03_inter_layer_communication.md) | **Next:** [05_data_model_state_signature.md](05_data_model_state_signature.md)
