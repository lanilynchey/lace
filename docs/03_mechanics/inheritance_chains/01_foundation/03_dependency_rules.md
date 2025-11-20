## Dependency Rules

All inheritance chains in LACE follow these structural rules:

### **1. Acyclicity (No Circular Dependencies)**
- **Rule:** No force can depend on itself, directly or indirectly (A→B→C→A is forbidden)
- **Why:** Circular dependencies create infinite loops and break computability
- **Example:** fear() cannot depend on judgment() if judgment() also depends on fear()

### **2. Tier Ordering (Downward Flow)**
- **Rule:** Dependencies flow from lower tiers to higher tiers only (Tier 1 → 2 → 3 → 4)
- **Why:** Ensures axioms remain foundational and prevents logical contradictions
- **Example:** Tier 3 forces can depend on Tier 1 or Tier 2, but Tier 2 cannot depend on Tier 3

### **3. Axiom Grounding (All Roads Lead to Tier 1)**
- **Rule:** Every force must trace back to at least one Tier 1 axiom
- **Why:** Ensures all forces derive from fundamental building blocks
- **Example:** Any force that cannot be traced to entropy(), consciousness(), pattern(), coherence(), or polarity() is incomplete

### **4. Conditional Dependencies (Context-Dependent)**
- **Rule:** Some dependencies are marked [conditional] - required only in specific contexts
- **Why:** Real-world force activation varies by situation
- **Example:** fear() uses judgment() for social threats but bypasses it for immediate physical danger
- **Notation:** `├── force() [Tier X] [conditional] ← explanation`

### **5. No Dependency on Laws**
- **Rule:** Forces do not inherit from or depend on system laws
- **Why:** Laws regulate how forces operate (external constraints), they don't compose forces (internal structure)
- **Example:** entropy() doesn't depend on law_entropy(); the law regulates how entropy behaves

These rules ensure LACE's inheritance structure remains:
- **Computable** - Can be traced algorithmically
- **Consistent** - No logical contradictions
- **Complete** - All forces ground out in axioms
- **Clear** - Relationships are unambiguous

---
