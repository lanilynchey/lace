## 2. Cancellation

**When:** Opposite-polarity forces meet

**Result:** Neutralization or transmutation

**Mechanism:**
```python
def cancel(force_a, force_b):
    """Opposite forces neutralize or transmute"""
    if polarity(force_a) == opposite(polarity(force_b)):
        if strength(force_a) == strength(force_b):
            return null  # Perfect cancellation
        else:
            return dominant_force - weaker_force  # Partial
```

### **Examples:**

#### **desire() × fear() → freeze**
```python
# Desire pulls forward, fear pulls back
desire.vector = (+1, 0)  # Forward motion
fear.vector = (-1, 0)    # Backward inhibition

# Result: paralysis
freeze_state = desire + fear
if freeze_state.duration > threshold:
    spawn(anxiety)
```

#### **hope() × despair() → neutrality or struggle**
```python
# Hope expands timeline, despair collapses it
if hope.strength > despair.strength:
    result = diminished_hope
elif despair.strength > hope.strength:
    result = deepened_despair
else:
    result = numb_neutrality  # Neither forward nor back
```

#### **order() × chaos() → edge_of_chaos**
```python
# Where life and creativity emerge
order.creates(structure)
chaos.injects(randomness)

# Perfect balance: maximum complexity
edge_of_chaos = order * chaos
# Where innovation happens
```

---
