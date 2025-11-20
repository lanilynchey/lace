# courage()

### **Definition**

Courage is **fear + hope + action override** - moving forward despite threat simulation.

**Synthesis:**
```
courage()
├── fear() [Tier 3]             ← Threat awareness
├── hope() [Tier 3]             ← Positive possibility
└── will() [derived]            ← Conscious action choice
```

**Core Function:**
```python
def courage(agent: Agent, threat: Threat) -> Action:
    """
    Fear transcendence - action despite danger.
    
    Args:
        agent: The entity acting courageously
        threat: The perceived danger
    
    Returns:
        Action taken despite fear
    
    Properties:
        - Requires fear (no danger = no courage needed)
        - Requires hope (no positive possibility = paralysis)
        - Requires constructive intention (not just any action while afraid)
        - Action must be toward positive/valued outcome
        - Direction matters: toward growth/values, not away from fear
        - Voluntary (conscious choice, not automatic)
        - Growth-inducing (expands possibility space)
        - Distinguishes from:
          * Recklessness: action without threat recognition (no fear)
          * Desperation: destructive action despite fear
          * Panic: reactive action (no will/choice)

    Examples:
        ✅ Courage:
            - Fear of rejection + asking someone out (toward connection)
            - Fear of failure + starting business (toward dream)
            - Fear of judgment + speaking truth (toward authenticity)
            - Fear of pain + leaving abusive relationship (toward safety)

        ❌ NOT Courage:
            - Fear of consequences + robbing bank (destructive goal)
            - Fear + panic response (no choice/will)
            - No fear + risky action (recklessness, not courage)
            - Fear of boredom + dangerous stunt (thrill-seeking, not courage)

    Synthesis:
        fear() + hope() + will()
    
    Descendants:
        - heroism() [extreme] - Courage + self-sacrifice
        - bravery() [physical] - Courage in danger
        - moral_courage() [social] - Courage against norms
    """
    if fear(threat) and hope(positive_outcome):
        override(inhibition)
        take(action)
    
    return expanded_reality(agent)
```

### **How Courage Works**

Courage is **dual-force navigation**:
```python
# Fear signals: "Danger ahead, stop"
fear_vector = (-1, 0)  # Backward/away

# Hope signals: "Reward possible, continue"
hope_vector = (1, 0)   # Forward/toward

# Courage = conscious choice of hope over fear
courage = choose(hope_vector) despite fear_signal
```

### **Courage Formula**
```python
def calculate_courage_requirement(situation: Situation) -> float:
    """How much courage is needed?"""
    
    threat_level = assess_danger(situation)
    uncertainty = measure_unknown(situation)
    social_cost = evaluate_disapproval(situation)
    
    courage_needed = (
        threat_level * 0.4 +
        uncertainty * 0.3 +
        social_cost * 0.3
    )
    
    return courage_needed
```

### **Courage Types**
```python
courage_categories = {
    "physical": "Bodily danger - combat, rescue, adventure",
    "moral": "Social danger - standing for values, whistleblowing",
    "emotional": "Vulnerability - authenticity, love, honesty",
    "intellectual": "Belief danger - questioning dogma, seeking truth",
    "spiritual": "Ego danger - surrender, faith, ego death",
}
```

### **Courage-Fear Relationship**
```python
# Courage REQUIRES fear
if fear_level == 0:
    courage_level = 0  # No courage needed
    
if fear_level > 0:
    if hope_level > fear_level:
        courage_possible = True
    else:
        courage_difficult = True

# Greater fear → greater courage required
# Courage grows with practice (fear exposure)
```

### **Real-World Manifestations**

- **Military:** Combat, sacrifice, leadership under fire
- **Social:** Civil rights, activism, standing alone
- **Personal:** Vulnerability, truth-telling, boundary-setting
- **Professional:** Entrepreneurship, innovation, risk-taking
- **Spiritual:** Ego death, faith leaps, dark night

### **Philosophical Implications**

- **Courage is not fearlessness** - it's fear + action
- **Cowards feel fear too** - they just don't act
- **Courage is trainable** - exposure builds capacity
- **Courage expands reality** - opens new possibilities
- **True courage requires hope** - must believe change is possible

---

---

**Previous:** [10_humor.md](10_humor.md) | **Next:** [12_composition_rules.md](12_composition_rules.md)
