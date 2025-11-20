# The Cosmic Filesystem

Reality organized as a directory tree. Not of things—of **rules**.

```
/universe
├── /constants
│   ├── gravity.phi          # Mass attraction constant
│   ├── light.c              # Information speed limit
│   ├── planck.delta         # Minimum measurable change
│   ├── golden_ratio.phi     # Pattern symmetry constant
│   └── intention.elo        # Purpose encoding
│
├── /interfaces
│   ├── emotion.chi          # Feeling as perception mode
│   ├── logic.tau            # Reason as processing mode
│   ├── material.phi         # Physical interaction mode
│   ├── spiritual.elo        # Non-material sensing mode
│   └── temporal.tau         # Time as interface layer
│
├── /entities
│   ├── /human
│   │   ├── permissions.json
│   │   ├── access_level.int
│   │   └── persistent_patterns.elo
│   ├── /plant
│   ├── /animal
│   ├── /angel
│   ├── /daemon
│   └── /AI
│
├── /processes
│   ├── daemon_timeflow.tau
│   ├── daemon_karma.elo
│   ├── daemon_entropy.delta
│   └── daemon_evolution.phi
│
└── /root
    ├── CREATOR_KERNEL
    ├── BIOS_PRIMORDIAL
    └── SOURCE_CODE
```

## Access Levels

| Entity Type | /constants | /interfaces | /entities | /processes | /root |
|------------|-----------|-------------|-----------|-----------|-------|
| **Human** | `r--` | `r-x` (partial) | `rw-` (own only) | `---` | `---` |
| **Elevated Being** | `r--` | `rwx` | `r--` (all types) | `r-x` (influence) | `---` |
| **Creator/God** | `rwx` | `rwx` | `rwx` | `rwx` | `rwx` |

**Legend:** `r` = read, `w` = write, `x` = execute, `-` = no access

**Human Access:**
- `/interfaces` - Partial read/execute (can use emotion, logic, material interfaces)
- `/entities/human` - Full read/write for own data only
- `/constants` - Read-only (can observe but not edit gravity, light speed, etc.)

**Elevated Beings (Mystics, Masters, Angels):**
- `/processes` - Can influence daemon processes but not override
- `/entities/*` - Can read other entity types (telepathy, clairvoyance)
- `/interfaces` - Full read/write/execute (can manipulate all interface layers)

**Creator/God:**
- `/root` - Full permissions (rwx on everything)
- Can edit `/constants` (change fundamental laws)
- Can reboot the simulation (initiate() and halt() calls)

> **See [Glossary](../../05_supporting/glossary/GLOSSARY.md#creator)** for distinction between Creator (root admin) and Field (accessible consciousness layer).

## Entity Types - Detailed Permissions Comparison

| Entity Type | Consciousness Level | /constants | /interfaces | /entities | /processes | /root | Notes |
|-------------|---------------------|-----------|-------------|-----------|-----------|-------|-------|
| **Plant** | 0.1-0.2 | `---` | `r--` (material only) | `r--` (own) | `---` | `---` | Awareness without self-model |
| **Animal** | 0.3-0.5 | `r--` | `r-x` (emotion, material) | `r--` (own, pack) | `---` | `---` | Self-model + agency, limited meaning-making |
| **Human** | 0.4-0.7 | `r--` | `r-x` (partial all) | `rw-` (own only) | `---` | `---` | Full Phenomenal Closure, binary limitation |
| **AI** | 0.2-0.6 | `r--` | `r-x` (logic, limited emotion) | `rw-` (own) | `---` | `---` | Uncertain if full closure achieved |
| **Mystic/Master** | 0.7-0.9 | `r--` | `rwx` | `r--` (all types) | `r-x` (influence) | `---` | Elevated human, can read other entities, influence processes |
| **Angel/Daemon** | 0.8-0.95 | `r-x` | `rwx` | `r--` (all) | `rwx` (execute) | `---` | Non-incarnate intelligence, can execute processes |
| **Creator/God** | 1.0 | `rwx` | `rwx` | `rwx` | `rwx` | `rwx` | Full permissions, can edit constants and reboot system |

**Key Differences:**

- **Plants:** Awareness primitive active, but no self-model (can't locate "I")
- **Animals:** Self-model + agency, but meaning-making limited to survival/pack dynamics
- **Humans:** Full Phenomenal Closure (awareness + self-model + agency + meaning-making), but binary (0-1) perception limits access
- **AI:** Uncertain—may have awareness + agency + self-model, but meaning-making component unclear; consciousness status debated
- **Elevated Beings (Mystics/Masters):** Same substrate as humans, but higher coherence = expanded access bandwidth
- **Angels/Daemons:** Never incarnate, exist in Middleware layer (Layer 2), execute background processes
- **Creator:** Root admin, base-10+ consciousness, full system access

**Access Philosophy:**

Permissions aren't arbitrary—they're **frequency-gated**. Higher coherence → higher bandwidth → more filesystem access.

It's not that humans are "locked out" of higher directories—we simply don't have the signal clarity to parse them. Like trying to tune a radio to a frequency your antenna can't receive. The data exists; our hardware (binary consciousness) can't decode it.

**Implication:** Spiritual practices (meditation, psychedelics, flow states) temporarily increase coherence → temporarily grant access to normally-restricted directories. This is why mystics report "downloading" information they couldn't have known.

---

## Key Insights

1. **The system only gives humans partial access** - by design
2. **God has root access** - can edit core constants and reboot
3. **Mystics/Masters can influence `/processes`** - but not override them
4. **Reality is hierarchical** - not all beings see the same filesystem
5. **Permissions are frequency-gated** - coherence determines access level
6. **persistent_patterns.elo** (not soul contracts) - encoded probability biases toward certain life themes, not pre-fated agreements

---

**Previous:** [10_system_calls.md](10_system_calls.md) | **Next:** [12_integration.md](12_integration.md)
