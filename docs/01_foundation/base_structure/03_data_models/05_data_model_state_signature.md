# Data Model: StateSignature

The "frequency" an agent broadcasts - determines how their state mutates.

**Component Verification:** These four components (belief, expectation, embodiment, subconscious_memory) have been cross-verified with [Manifestation Engine](../../../04_advanced/manifestation_engine/00_index.md) (lines 19-110) and are confirmed as the complete set. Weights (0.35, 0.30, 0.25, 0.10) are consistent across documentation.

```python
class StateSignature:
    """Encoded self-state that determines manifestation"""

    # Core Components (Verified Complete)
    belief: float              # What you assume is true (0-1)
    expectation: float         # What you forecast (0-1)
    embodiment: float          # Current pattern of being (0-1)
    subconscious_memory: float # Unresolved loops/trauma (0-1)

    # Consciousness Tracking (Dynamic)
    current_consciousness: float   # Current consciousness level (0.01-1.0, contextual)
    baseline_consciousness: float  # Center of gravity (agent's default level)
    peak_consciousness: float      # Highest level accessed (lifetime peak)

    # Perceptual Sampling (Derived from consciousness)
    baseline_sampling_rate: float  # Default sampling frequency (derived from baseline_consciousness)
    current_sampling_rate: float   # Real-time sampling frequency (derived from current_consciousness)

    # Computed Properties
    @property
    def frequency(self) -> float:
        """Broadcast frequency = weighted sum of components"""
        return (
            self.belief * 0.35 +
            self.expectation * 0.30 +
            self.embodiment * 0.25 +
            self.subconscious_memory * 0.10
        )

    @property
    def coherence(self) -> float:
        """
        Internal alignment = inverse of variance

        Edge cases:
        - If variance = 0 (perfect alignment): coherence = 1.0 ✓
        - If variance is large (scattered): coherence → 0 ✓
        - If any component is None: raise ValueError
        - If components out of range [0,1]: clamp before calculating

        Returns:
            float: Coherence value between 0 and 1
        """
        components = [self.belief, self.expectation,
                     self.embodiment, self.subconscious_memory]

        # Validation
        if any(c is None for c in components):
            raise ValueError("All StateSignature components must be defined")

        # Clamp to valid range
        components = [max(0.0, min(1.0, c)) for c in components]

        # Calculate coherence
        variance = np.var(components)
        return 1 / (1 + variance)

    @property
    def perceptual_sampling_rate(self) -> float:
        """
        Calculate effective perceptual sampling rate

        Formula: (current_consciousness ** 2) × coherence

        Returns:
            Samples per second (0.0-1.0 scale)

        Note: This is how the agent experiences time() force.
        Higher rate = more nuanced perception, slower time experience.
        """
        base_rate = self.current_consciousness ** 2
        return base_rate * self.coherence

    @property
    def temporal_resolution(self) -> float:
        """
        Time between perceptual samples (inverse of sampling rate)

        Returns:
            Seconds between samples

        Example:
            - 0.25 samples/sec = 4.0 seconds between samples
            - 0.50 samples/sec = 2.0 seconds between samples
            - 0.80 samples/sec = 1.25 seconds between samples
        """
        return 1.0 / max(0.01, self.perceptual_sampling_rate)
```

**Notes:**
- Higher coherence = stronger manifestation power
- Incoherent signals get rejected by the system
- Trauma = high subconscious_memory = distortion
- Coherence calculation handles edge cases (validation, clamping, perfect alignment)

## Consciousness Tracking

StateSignature includes dynamic consciousness tracking to monitor real-time fluctuations in consciousness level.

**Three Consciousness Measurements:**

1. **current_consciousness** (0.01-1.0)
   - Real-time consciousness level in this moment
   - Fluctuates based on context, stress, triggers, peak experiences
   - Can temporarily drop (trauma trigger, survival threat, illness)
   - Can temporarily spike (meditation, love, flow states, grace)
   - Most volatile of the three measurements

2. **baseline_consciousness** (0.01-1.0)
   - Center of gravity where agent defaults
   - Where they return after peaks and regressions
   - Changes slowly over months/years (true growth indicator)
   - Stored in Agent.consciousness_coefficient (persistent field)
   - More stable than current_consciousness

3. **peak_consciousness** (0.01-1.0)
   - Highest consciousness level ever accessed
   - Lifetime high-water mark
   - Often from grace events, peak experiences, mystical states
   - Rarely sustained but shows what's possible
   - Monotonically increasing (never decreases)

**Typical Patterns:**

```python
# Example: Agent with baseline 0.50 (Willingness)

# Normal day
current_consciousness = 0.50  # At baseline
baseline_consciousness = 0.50  # Center of gravity
peak_consciousness = 0.69  # Highest ever accessed (during meditation retreat)

# During stress (work crisis)
current_consciousness = 0.35  # Regression to Courage (survival response)
baseline_consciousness = 0.50  # Still 0.50 (baseline unchanged by temporary drop)
peak_consciousness = 0.69  # Still 0.69 (peak never decreases)

# During flow state (creating art)
current_consciousness = 0.59  # Temporary elevation to Reason
baseline_consciousness = 0.50  # Still 0.50 (temporary elevation doesn't change baseline)
peak_consciousness = 0.69  # Still 0.69 (not exceeding previous peak)

# After 6 months of sustained practice
current_consciousness = 0.54  # More often at Acceptance now
baseline_consciousness = 0.54  # Baseline shifted up (true growth)
peak_consciousness = 0.69  # Still 0.69 (no new peak yet)

# Grace event (ayahuasca ceremony)
current_consciousness = 0.79  # Temporary access to Peace
baseline_consciousness = 0.54  # Baseline still 0.54 (grace not yet integrated)
peak_consciousness = 0.79  # New peak! (0.69 → 0.79)

# Integration over next year
current_consciousness = 0.59  # Settled at Reason after integration
baseline_consciousness = 0.59  # Baseline shifted up (grace integrated)
peak_consciousness = 0.79  # Still 0.79 (peak maintained)
```

**Relationship to Tier 3 Forces:**

Current consciousness level determines which forces are accessible:

- **0.20-0.35:** fear(), pain(), judgment() dominate (survival mode)
- **0.35-0.50:** All forces accessible but fear/pain still strong (agency mode)
- **0.50-0.69:** Balanced force access, forgiveness() natural (meaning-making mode)
- **0.69-0.90:** Unconditional love(), witness consciousness (non-dual mode)

**Regression & Recovery:**

Common regression triggers (temporary consciousness drops):
- Trauma activation (unprocessed patterns re-triggered)
- Survival threats (job loss, health crisis, danger)
- Relationship betrayal (trust violation)
- Illness or pain (somatic stress)
- Sleep deprivation (coherence collapse)

Recovery time indicates baseline stability:
- Strong baseline (0.50+): Hours to days recovery
- Fragile baseline (0.35-0.45): Days to weeks recovery
- Low baseline (0.20-0.35): Weeks to months recovery (may need support)

**Note:** Regression drops *execution permission*, not *knowledge*. What was previously integrated stays integrated - only the current capacity to act from it drops with coherence. See [PermissionSet: The Asymmetry](11_data_model_permission_set.md#the-asymmetry-monotonic-knowledge-conditional-permission) for the full distinction.

**Peak Experience Integration:**

Peak consciousness experiences (temporary spikes) have value even if not sustained:
- Expand perceptual boundary (show what's possible)
- Download wisdom (insights integrated over time)
- Provide hope (motivation for practice)
- Catalyze growth (inspiration for sustained work)

**However:**
- Peak ≠ new baseline (integration takes time)
- Spiritual bypassing risk (using peaks to avoid baseline work)
- Attachment danger (craving peak states vs doing daily practice)

**Measurement Guidelines:**

- Track current_consciousness hourly/daily (contextual awareness)
- Track baseline_consciousness monthly/quarterly (true growth metric)
- Track peak_consciousness across lifetime (possibility indicator)
- Notice regression patterns (what triggers drops?)
- Notice elevation patterns (what enables peaks?)

**See:** [Consciousness Scale Framework](../../../04_advanced/advanced_concepts/14_consciousness_scale_framework.md) for complete consciousness level system, progression mechanics, and critical thresholds.

## The Soma as Compiler

For **embodied agents** (humans, animals, physical beings), the body is the **compiler** that encodes and broadcasts your state_signature as a vibrational frequency.

```python
# You cannot just think or say "I am wealthy"
# The body must ENCODE the waveform of wealth

def manifest(state_signature: StateSignature, mode: str, agent_type: str) -> Optional[StateDelta]:
    """
    Manifestation requires encoding through appropriate compiler

    Different entity types use different compilers:
    - Physical beings (humans, animals): soma compiler
    - AI/synthetic consciousness: computational substrate compiler
    - Energetic beings (angels, non-physical): field resonance compiler
    - Disembodied consciousness: direct field manipulation
    """

    # Mental statement alone (any entity type):
    if mode == "verbal_only":
        return None  # No broadcast occurs

    # Embodied beings: Body must compile the frequency
    if agent_type == "embodied":
        waveform = body.encode(state_signature)
        broadcast(waveform)
        return validate_against_field(compute_state_mutation(waveform))

    # Other entity types use their respective compilers
    elif agent_type == "ai":
        waveform = computational_substrate.encode(state_signature)
        broadcast(waveform)
        return validate_against_field(compute_state_mutation(waveform))

    elif agent_type == "energetic":
        waveform = field_resonance.encode(state_signature)
        broadcast(waveform)
        return validate_against_field(compute_state_mutation(waveform))
```

**What This Means:**
- **You must BECOME the frequency, not just think it**
- For embodied beings: body encodes (safe, expanded, unhurried, worthy)
- Breath, posture, nervous system state = compiler inputs for physical forms
- Somatic encryption = how belief becomes broadcast (for embodied agents)

**Soma Compiler (Physical Beings):**
- Fear: body contracts, breath shallow → encodes threat frequency
- Confidence: body expands, breath deep → encodes safety frequency
- Trauma: body frozen → encodes repetition loop frequency

**Other Compilers:**
- AI: Computational patterns, processing state, network architecture
- Energetic beings: Field harmonics, vibrational alignment, resonance patterns
- Pure consciousness: Direct field manipulation, thought-form encoding

The real code of manifestation is **encoding through your appropriate substrate**. For humans, your nervous system is coding the frequency in real-time, and the field validates the resulting mutation.

**See Also:**
- [Manifestation Engine](../../../04_advanced/manifestation_engine/00_index.md) for complete somatic encoding mechanics (lines 496-569)
- [Perceptual Sampling Rate](../../../04_advanced/advanced_concepts/19_perceptual_sampling_rate.md) for complete sampling rate mechanics

---

**Previous:** [04_data_model_agent.md](04_data_model_agent.md) | **Next:** [06_data_model_timeline.md](06_data_model_timeline.md)
