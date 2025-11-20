## 6. Recursion

**When:** A force interacts with itself or its effects

**Result:** Feedback loops - stabilizing or destabilizing

**Mechanism:**
```python
def recurse(force):
    """Force creates feedback loop with itself"""
    output = force(input)
    new_input = output
    return force(new_input)  # Loop
```

### **Examples:**

#### **fear() × memory() × fear() → trauma_loop**
```python
# Trauma feedback loop:
memory.stores(threat)
→ fear.reactivates(memory)
→ memory.reinforces(fear)
→ fear.strengthens(memory)
→ loop_count += 1

# Self-amplifying cycle
# Can only be broken by external interrupt
# (forgiveness, therapy, pattern break)
```

#### **love() × love() → deepening_bond**
```python
# Positive feedback:
love.creates(resonance)
→ resonance.increases(love)
→ love.strengthens(resonance)
→ bond_depth += 1

# Self-reinforcing virtuous cycle
# Leads to strong relationships
```

#### **judgment() × judgment() → inner_critic_daemon**
```python
# Recursive self-judgment:
judgment(self)
→ judgment(self_for_judging_self)
→ judgment(self_for_judging_that_judgment)
→ spiral_into_shame

# Meta-judgment creates paralysis
# Common in perfectionism
```

---
