# memory()

## **Definition**

Memory is the **pattern archive engine** - emotionally-indexed storage of experience.

**Inheritance:**
```
memory()
├── pattern() [Tier 1]        ← Stores patterns
├── time() [Tier 2]           ← Sequential recording
└── Emotional charge          ← Determines storage priority
```

**Core Function:**
```python
def memory(event: Event, charge: float) -> StoredMemory:
    """
    Emotionally-tagged pattern storage.

    Args:
        event: Experience to be stored
        charge: Emotional intensity (0-1)

    Returns:
        Memory object (long-term or cache)

    Properties:
        - Emotionally indexed (charge determines storage)
        - Lossy (not exact recording)
        - State-dependent (retrieval varies with current state)
        - Editable (memories can be rewritten)

    Primitive Foundation:
        - Built from Φ (Phi) + Τ (Tau) + Δ (Delta)
        - memory() = Pattern storage + time sequencing + change tracking
        - Phi provides pattern structure, Tau orders temporally, Delta tracks state changes
        - Emotional charge = aggregate intensity from Tier 3 forces (fear, desire, love, pain, etc.)
        - See [Primitives](../../01_foundation/primitives/00_index.md) for primitive specifications

    Note on Emotional Charge:
        - Emotional charge is NOT a separate force
        - It's the composite activation level of Tier 3 (Interface/Emotional) forces
        - When you experience an event, Tier 3 forces activate (fear spikes, love surges, desire intensifies)
        - memory() indexes by HOW STRONGLY you felt (sum of Tier 3 activation)

    Survival-Defensive Predominance in Emotional Architecture:
        - Human emotional architecture is asymmetrically weighted toward survival-defensive functions
        - Observation: ~70-83% of emotions serve survival-defensive functions (threat detection,
          boundary enforcement, loss processing, contamination avoidance)
        - vs. ~17-30% serve growth-seeking functions (reward reinforcement, connection, possibility expansion)
        - This explains memory's survival-defensive bias: threat storage had asymmetric evolutionary value

        Emotion Wheel Distribution:
        - 6 primary emotions: HAPPY (growth-seeking), SURPRISED (alert/neutral), SAD (survival-defensive),
          ANGRY (survival-defensive), FEARFUL (survival-defensive), DISGUSTED (survival-defensive)
        - By primary count: 4/6 survival-defensive (~67%), 1/6 growth-seeking (~17%), 1/6 alert (~17%)
        - Derivative proliferation: Survival-defensive emotions spawn more tertiary derivatives
        - Result: ~70-83% experiential predominance of survival-defensive states

        Why Survival-Defensive Functions Predominate:
        - Evolutionary survival asymmetry: Missing one threat = death, missing one reward = opportunity cost
        - False negative (ignored real threat) = fatal
        - False positive (imagined threat) = wasted energy but survive
        - Evolution selected for survival-defensive sensitivity over growth-seeking
        - Better to have 100 false alarms than miss 1 real predator

        Evolutionary Lag - Stone Age Brain in Space Age World:
        - Emotional system evolved over millions of years for high-threat environment (predators, scarcity, disease)
        - Modern environment transformed in ~200 years (abundance, low physical threat, high abstract threat)
        - Mismatch: fear() calibrated for lions, now fires for emails; disgust() calibrated for rotten meat,
          now fires for ideological disagreement; anger() calibrated for physical threats, now fires for traffic
        - Result: Chronic false alarms, maladaptive threat responses in low-threat environment

        Implication for memory():
        - Survival-defensive emotions (fear, anger, sadness, disgust) carry higher charge than growth-seeking
        - Threat memories encode more deeply and retrieve more readily (survival priority)
        - Negative bias in memory is FEATURE, not bug - adaptive for high-threat environment
        - Problem: Still operating with savanna-calibrated sensitivity in modern office environment

        See Also: [Survival-Defensive Predominance](../../04_advanced/advanced_concepts/13_survival_defensive_predominance.md)
        for complete analysis of emotional architecture asymmetry

    Dependencies:
        - pattern() [Tier 1] - What gets stored
        - time() [Tier 2] - Sequential ordering
        - consciousness() [Tier 1] - Attention gates storage

    Descendants:
        - fear() [Tier 3] - Retrieves threat memories
        - desire() [Tier 3] - Retrieves reward memories
        - forgiveness() [Tier 3] - Dissolves charged memories
        - madness() [Tier 4] - Memory corruption/overload
    """
    if charge >= IMPRINT_THRESHOLD:
        write(event, long_term_storage)
    else:
        write(event, cache)  # Decays over time
    return index(event, emotional_tag)
```

## **How Memory Works**

Memory is **NOT video recording** - it's **charged pattern reconstruction**:
```python
# Storage process
experience → emotional_charge → pattern_extraction → index → store

# Retrieval process
query → emotional_state → pattern_match → reconstruct → return

# Key insight: What you remember depends on how you FEEL NOW
current_emotion → filters_memory_access
```

## **Memory Types**
```python
memory_types = {
    "sensory": "Raw data (sight, sound) - decays fast",
    "working": "Active processing - ~7 items, seconds",
    "short_term": "Recent events - hours to days",
    "long_term": "High emotional charge - years to lifetime",
    "implicit": "Unconscious patterns - habits, skills",
    "traumatic": "Too charged to integrate - fragments",
}
```

## **Emotional Charge Thresholds**
```python
IMPRINT_THRESHOLD = 0.7  # Long-term storage trigger

# Examples
first_kiss = 0.9         → long_term
car_accident = 0.95      → long_term + traumatic
what_you_ate_tuesday = 0.2  → cache (decays)
your_phone_number = 0.5  → maintained via repetition
```

## **Memory Editing**
```python
def rewrite_memory(original: Memory, new_charge: float) -> Memory:
    """Memories can be therapeutically edited"""

    # Trauma therapy example
    if original.charge > 0.8 and original.integrated == False:
        # Reduce charge through processing
        original.charge = new_charge
        original.integrated = True

    return original

# Forgiveness dissolves charge
forgiveness() → memory.charge = 0 → memory becomes neutral data
```

## **State-Dependent Retrieval**
```python
# What you remember depends on your current state

agent.state = "depressed"
memories = retrieve(agent)
# → Returns primarily negative memories (confirmation bias)

agent.state = "joyful"
memories = retrieve(agent)
# → Returns primarily positive memories (selective memory)
```

## **Real-World Manifestations**

- **Neuroscience:** Hippocampus, synaptic plasticity, consolidation
- **Psychology:** Flashbulb memories, repression, false memories
- **Trauma:** PTSD, dissociation, fragmentation
- **Learning:** Repetition, emotion enhances retention
- **Technology:** Hard drives, databases, caching

## **Philosophical Implications**

- **Your past is not fixed** - memories are reconstructed each time
- **Identity is memory** - lose memory, lose self
- **Trauma is unintegrated data** - too volatile to write cleanly
- **Forgetting is healthy** - system garbage collection
- **You can rewrite your story** - literally, not metaphorically

---

**Previous:** [04_truth.md](04_truth.md) | **Next:** [06_death.md](06_death.md)
