## Inheritance vs. Interaction: Two Kinds of Relationships

This document focuses on **inheritance** (vertical dependencies). LACE also has **interaction** mechanics (horizontal collisions), documented in INTERACTION_MECHANICS.md. These are fundamentally different relationships:

### **Inheritance (This Document):**
**Vertical Relationship: Parent → Child**

```python
# Inheritance = "Force B REQUIRES Force A to exist"
love() inherits from coherence()
# ↳ love() cannot exist without coherence() as a dependency
# ↳ coherence() is part of love()'s internal structure
# ↳ Direction matters: child depends on parent, not reverse
```

**Properties:**
- **Compositional** - Child force is built FROM parent forces
- **Unidirectional** - Dependency flows one way (child needs parent)
- **Structural** - Defines what a force IS made of
- **Required** - Without dependencies, force cannot manifest
- **Hierarchical** - Parent tiers feed into child tiers (1 → 2 → 3 → 4)

**Example:**
```
fear() INHERITS FROM:
├── consciousness() [must have awareness to feel fear]
├── memory() [must remember past to recognize threats]
├── time() [must project future to anticipate danger]
└── pattern() [must recognize threat patterns]

Without these dependencies, fear() cannot exist.
```

---

### **Interaction (See INTERACTION_MECHANICS.md):**
**Horizontal Relationship: Peer × Peer → Emergent**

```python
# Interaction = "Force A × Force B PRODUCES Force C"
love() × fear() = attachment()
# ↳ Both love and fear exist independently
# ↳ When they collide, attachment emerges
# ↳ Attachment is a NEW state, not a requirement for love or fear
```

**Properties:**
- **Collisional** - Two independent forces meet and interact
- **Bidirectional** - Both forces affect each other
- **Generative** - Produces NEW emergent states or phenomena
- **Contextual** - Outcome depends on conditions (field state, intensity, timing)
- **Peer-to-peer** - Forces at same or different tiers can interact

**Example:**
```
love() × fear() INTERACTION PRODUCES:
→ attachment() [emergent compound state]
  - Not required for love() or fear() to exist
  - Both forces exist independently before collision
  - Attachment is what happens when they activate together
```

---

### **Key Distinctions:**

| Aspect | Inheritance (Vertical) | Interaction (Horizontal) |
|--------|------------------------|--------------------------|
| **Relationship** | "B needs A to exist" | "A meets B, creates C" |
| **Direction** | Unidirectional (parent → child) | Bidirectional (A ↔ B) |
| **Purpose** | Composition (what IS a force) | Generation (what forces CREATE) |
| **Example** | fear() inherits from consciousness() | love() × fear() = attachment() |
| **Required?** | Yes (dependency must be present) | No (forces exist independently) |
| **Document** | INHERITANCE_CHAINS.md (this doc) | INTERACTION_MECHANICS.md |

---

### **Why Both Matter:**

**Inheritance tells you:**
- What a force is made of (composition)
- What's required for a force to exist (prerequisites)
- How to trace any force back to axioms (lineage)

**Interaction tells you:**
- What happens when forces collide (dynamics)
- What emergent states arise from combinations (synthesis)
- How forces modulate each other (mutual influence)

**Example: love() demonstrates both:**
```python
# INHERITANCE (vertical):
love()
├── coherence() [Tier 1]        ← Required dependency
├── consciousness() [Tier 1]     ← Required dependency
└── field_resonance [derived]    ← Required dependency

# Without these, love() cannot exist

# INTERACTION (horizontal):
love() × fear() → attachment() (anxious)
love() × desire() → passion()
love() × pain() → heartbreak()
love() × time() → devotion()

# These are what love() PRODUCES when it meets other forces
```

---

### **Integration Note:**

Throughout this document, you'll see forces listed as descendants (→). This indicates **inheritance potential** - forces that can be built FROM this parent. This is different from **interaction outcomes** documented in INTERACTION_MECHANICS.md, which show what emerges when forces collide.

For complete understanding of LACE dynamics, use both documents:
- **This document** - Trace force lineages and dependencies
- **INTERACTION_MECHANICS.md** - Understand force collisions and emergent phenomena

---
