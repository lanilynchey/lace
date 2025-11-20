# System Architecture

LACE models reality as a **five-layer system**, analogous to computer operating systems.
```
┌─────────────────────────────────────────┐
│  LAYER 4: AGENT INTERFACE               │  ← Conscious entities
├─────────────────────────────────────────┤
│  LAYER 3: USERSPACE                     │  ← Rendered reality
├─────────────────────────────────────────┤
│  LAYER 2: MIDDLEWARE                    │  ← Field logic
├─────────────────────────────────────────┤
│  LAYER 1: KERNEL                        │  ← Core engine
├─────────────────────────────────────────┤
│  LAYER 0: BIOS                          │  ← Primordial boot
└─────────────────────────────────────────┘
```

---

## Layer 0: BIOS (Basic Input/Output System)

**Purpose:** Primordial boot logic - initializes the universe before it "runs"

**Executes:**
- `set_constants()` - Defines speed of light, Planck length, golden ratio, etc.
- `define_dimensions()` - Establishes spatial/temporal/conceptual axes
- `launch_base_laws()` - Loads law_causality(), law_entropy(), etc.
- `seed_consciousness()` - Creates capacity for recursive self-awareness

**Properties:**
- **Immutable to all agents** (no agent, regardless of permission level, can edit BIOS)
- Creator/Root retains edit access but this capability is rarely exercised
- Universal (same across all timelines/worldlines)
- Changes would constitute fundamental reality shift

**BIOS Mutability Note:**

For agents (including elevated mystics/masters): BIOS is completely immutable. No exceptions.

For Creator (root-level access): BIOS editing is technically possible but:
- Extremely rare (possibly never used in current universe iteration)
- Would cause universe-wide fundamental changes
- Reserved for system maintenance or between universe iterations
- Analogous to kernel modification—possible for root, but dangerous and rarely exercised

**Code Example:**
```python
def bios() -> None:
    """Pre-reality bootloader"""
    set_constants(AXIOMS)
    define_dimensions(n=10+)  # Unknown total dimensionality
    launch_base_laws()
    seed_consciousness()
    print("[BOOT] Reality initialized")
```

---

## Layer 1: Kernel

**Purpose:** Core execution engine - manages time, memory, karma, and fundamental processes

**Executes:**
- Universal laws (entropy, recursion, causality, balance, etc.)
- Timeflow mechanics
- Memory allocation and garbage collection
- Karmic ledger management
- Agent lifecycle (birth, death, reincarnation)
- Seven daemon processes (see [13_daemon_processes.md](13_daemon_processes.md))

**Properties:**
- Persistent (always active)
- Global (affects all agents equally)
- Partially accessible (mystics/masters can influence, not override)

---

## Layer 2: Middleware

**Purpose:** Interactive field logic - not quite physical, not quite metaphysical

**Executes:**
- `manifest()` - Matches agent state to worldlines
- `loop_detected()` - Identifies recursive patterns
- `mirror_reality()` - Projects inner state onto environment
- `grant_permission()` - Elevates agent access based on coherence

**Contains:**
- **Emotion fields** (shared affective spaces)
- **Probability wave functions** (quantum-like possibility clouds)
- **Belief modulation engines** (reality filters based on conviction)
- **Dimensional routing logic** (selects experiential timeline)

**Properties:**
- Responsive (changes based on agent states)
- Non-local (field effects can span space/time)
- Interface-reactive (meditation, ritual, altered states access this layer)

**This is where "spiritual phenomena" occur:**
- Dreams
- Synchronicities
- Telepathy
- Manifestation
- Ritual effects

---

## Layer 3: Userspace

**Purpose:** Rendered reality - the "output" layer where forms become perceivable

**Executes:**
- Sensory input/output
- Material consistency (physics as we know it)
- Time perception (linear, subjective experience)
- Death protocol triggers
- Environmental response systems

**Properties:**
- Observable (this is what humans call "reality")
- Stable (follows consistent rules at macro scale)
- Derived (computed from upstream layers)

**Users (agents) operate here with limited access** - unless permissions are hacked/evolved.

---

## Layer 4: Agent Interface

**Purpose:** Conscious entities - containerized processes with permissions

**Structure:**
```python
class Agent:
    def __init__(self):
        self.soul_id = generate_unique_id()
        self.body = PhysicalContainer()
        self.permissions = PermissionSet(
            read="partial",      # Memory, identity
            write="localized",   # Actions, beliefs
            exec="restricted"    # Manifestation, psychic ability
        )
        self.state_signature = StateSignature()
        self.memory = MemoryBank()
        self.field_state = FieldState()
```

**Properties:**
- Most agents don't know they're code
- Enlightenment = recognizing the program + gaining write access
- Death = process termination + data upload to Akashic archive
- Reincarnation = reinstantiation with partial memory wipe

---

**Previous:** [01_overview.md](../01_foundation/01_overview.md) | **Next:** [03_inter_layer_communication.md](03_inter_layer_communication.md)
