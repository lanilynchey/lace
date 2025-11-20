# Pattern Examples

## **Example 1: Abandonment Pattern**

```python
pattern_abandonment = PersistentPattern(
    theme="abandonment",
    encoded_in=StateSignature(
        belief=0.3,              # "People always leave"
        expectation=0.4,          # "Relationships will fail"
        embodiment=0.5,           # Body carries wound
        subconscious_memory=0.8   # Trauma from early abandonment
    ),
    origin="trauma",
    probability_weight=0.75,  # Strong bias
    manifestation_frequency=0.48,  # Matches to low-frequency timelines
    mutable=True,  # CAN be healed
    resistance_level=0.7  # Difficult but not impossible
)

# How it works:
# Your state_signature broadcasts frequency 0.48
# Manifestation engine queries worldline database
# Returns timelines where abandonment themes are probabilistically likely
# You experience "I keep attracting people who leave"
# Feels like destiny → Actually probability bias from current trauma encoding
```

**Breaking the Pattern:**
```python
# Heal trauma → reduce subconscious_memory (0.8 → 0.3)
# Update beliefs → increase belief (0.3 → 0.7)
# New frequency: (0.7*0.35 + 0.6*0.30 + 0.6*0.25 + 0.3*0.10) = 0.62
# Engine now matches DIFFERENT timelines
# Pattern broken via state editing, not "contract completion"
```

---

## **Example 2: Unavailable Partners Pattern**

```python
pattern_unavailable = PersistentPattern(
    theme="unavailable_partners",
    encoded_in=StateSignature(
        belief=0.4,              # "I'm not worthy of full presence"
        expectation=0.5,          # "Love will be conditional"
        embodiment=0.6,           # Body expects rejection
        subconscious_memory=0.7   # Pattern from childhood (parent unavailable)
    ),
    origin="subconscious_memory",
    probability_weight=0.68,
    manifestation_frequency=0.52,
    mutable=True,
    resistance_level=0.65
)

# Why this keeps happening:
# NOT because you "signed a contract to learn about love"
# BUT because your current state broadcasts 0.52 frequency
# Which probabilistically matches timelines where:
#   - Partners are emotionally unavailable
#   - Relationships reinforce "not worthy" belief
#   - Pattern gets reinforced (recursion loop)

# Free will is preserved:
# You can CHOOSE to heal the wound (Generative Awareness)
# Healing changes your broadcast → different matches
# No pre-fate, just probability + current state
```

---

[Previous: Why Patterns Exist](03_why_patterns_exist.md) | [Next: How Patterns Form →](05_how_patterns_form.md)

[Back to Index](../00_index.md)
