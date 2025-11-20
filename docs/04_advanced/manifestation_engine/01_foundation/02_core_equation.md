## Core Equation: State Signature

Your **state_signature** is the encoded self-state that determines which timeline you match.

```python
state_signature = (
    belief +
    expectation +
    embodiment +
    subconscious_memory
)
```

### **1. Belief**
**What you assume is true** (often inherited unconsciously)

```python
belief: float  # 0-1 scale

# Examples:
belief("I am worthy") = 0.9  # Strong
belief("Money is evil") = 0.7  # Moderate
belief("I am safe") = 0.3  # Weak
```

**Properties:**
- Most beliefs are inherited (family, culture, trauma)
- Operate below conscious awareness
- Shape what feels "possible"
- Can be rewritten through embodiment

---

### **2. Expectation**
**The forecast you're running** (what you think will happen)

```python
expectation: float  # 0-1 scale

# Examples:
expectation("I'll succeed") = 0.8  # High
expectation("I'll be rejected") = 0.6  # Moderate
expectation("Things will work out") = 0.4  # Low
```

**Properties:**
- Future-oriented
- Based on past pattern recognition
- Can override conscious intent
- Influenced heavily by recent experience

---

### **3. Embodiment**
**Your current pattern of being** (how you're actually showing up)

```python
embodiment: float  # 0-1 scale

# Examples:
embodiment("confidence") = 0.9  # Fully in state
embodiment("scarcity") = 0.7  # Mostly in state
embodiment("abundance") = 0.2  # Barely in state
```

**Properties:**
- Somatic (held in the body)
- Most honest signal (can't be faked)
- Breath, posture, nervous system state
- **This is the compiler** - must match to manifest

---

### **4. Subconscious Memory**
**All unresolved loops, karmas, traumas, oaths**

```python
subconscious_memory: float  # 0-1 scale (noise level)

# Examples:
subconscious_memory(trauma="abandonment") = 0.8  # High interference
subconscious_memory(trauma="failure") = 0.5  # Moderate interference
subconscious_memory(integrated=True) = 0.1  # Low interference
```

**Properties:**
- Background noise that distorts signal
- Operates without conscious awareness
- Can override everything else
- Reduced through healing (presence + integration)

---

