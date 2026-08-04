# Τ (Tau) - Time Pulse

A unit of "state refresh." The clock tick of reality.

```python
class Tau:
    """The primitive of temporal progression"""

    def __init__(
        self,
        interval: float,
        observer_dependent: bool = True
    ):
        self.interval = interval            # Length of pulse
        self.observer_dependent = observer_dependent

    def tick(self, system: 'System') -> Any:
        """
        Advance system state by one frame

        Args:
            system: The system to advance

        Returns:
            Current system state after advancement
        """
        system.advance()
        return system.current_state
```

**What Tau Governs:**
- Frame rate of consciousness
- Perceptual sampling
- "Now" vs "then" distinction
- Memory formation (events discretized by tau)

**Real-World Manifestation:**
- Present moment awareness
- Flow state (tau slows down)
- Trauma (tau freezes)
- Anticipation (tau accelerates)

## Tau and Observer-Relative Time

**Key Property:** `observer_dependent: bool = True`

Time in LACE has TWO components:

1. **Objective Time** - Physical processes that occur regardless of observation (trees grow, stars burn, entropy increases)
2. **Subjective Time** - Observer-relative rendering based on state_signature and consciousness level

**LACE's Position:** There is one you, on one continuously-mutating trajectory - not multiple pre-existing versions across parallel timelines. What varies is how densely you sample Tau's pulse (your `consciousness_bandwidth`), which changes how that single trajectory *feels* to move through. Physical time progresses (aging, decay), but experiential time is rendered per observer.

**How Tau Varies Between Observers:**

1. **Flow State** (High coherence, deep focus)
   - Tau interval decreases subjectively (time slows)
   - More "frames" processed per objective second
   - Athletes describe "the ball moved in slow motion"
   - Physical time unchanged; perceptual sampling increased

2. **Trauma/Freeze Response** (Overwhelm, dissociation)
   - Tau freezes or becomes erratic
   - Memory formation disrupted (gaps, fragmentation)
   - PTSD flashbacks = Tau stuck in loop, replaying same frame
   - Objective time continues; subjective time halts

3. **Anticipation/Anxiety** (Low coherence, scattered attention)
   - Tau accelerates subjectively (time races)
   - Fewer frames processed, gaps in awareness
   - "Where did the day go?"
   - Physical processes unaffected; perceptual frames dropped

4. **Deep Meditation** (Consciousness approaching coherence = 1.0)
   - Tau may stop entirely for observer
   - Experience of timelessness, "eternal now"
   - Body continues aging; consciousness exits temporal flow

**Connection to Physics:**
- Einstein's relativity: Time dilation near massive objects (objective effect on spacetime)
- LACE interpretation: Mass affects consciousness field → also affects Tau rendering (subjective effect)
- Both objective spacetime curvature AND subjective consciousness state modify time experience

**Implication:** There is no single "universal now"—only local renderings of temporal progression. The universe has one objective trajectory (physical causality), but consciousness renders it differently based on state.

---

**Previous:** [02_delta.md](02_delta.md) | **Next:** [04_chi.md](04_chi.md)
