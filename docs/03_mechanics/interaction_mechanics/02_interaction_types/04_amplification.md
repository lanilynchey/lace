## 1. Amplification

**When:** Same-domain forces with aligned polarity interact

**Result:** Exponential increase in effect

**Mechanism:**
```python
def amplify(force_a, force_b):
    """Same-polarity forces reinforce"""
    if polarity(force_a) == polarity(force_b):
        if domain(force_a) == domain(force_b):
            return force_a * force_b  # Multiplicative, not additive
```

### **Examples:**

#### **hope() + luck() → manifestation_window**
```python
# Both expand possibility space
hope.extends(timeline_aperture)
luck.opens(anomaly_window)

# Together: massive probability shift
manifestation_window = hope * luck
# Beneficial events become highly likely
```

#### **fear() + judgment() → paranoia**
```python
# Both restrict and evaluate negatively
fear.suppresses(expansion)
judgment.detects(threat_patterns)

# Together: hypervigilance
paranoia = fear * judgment
# Everything becomes threatening
```

#### **love() + coherence() → bliss**
```python
# Both create harmony
love.entangles(fields)
coherence.aligns(internal_state)

# Together: unity consciousness
bliss = love * coherence
# Dissolution of boundaries
```

---
