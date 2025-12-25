# Force Mapping Schema

**Purpose:** Defines the structure and fields for all force mapping files in `mappings/forces/`

**Format:** YAML (.yaml)
**One file per force:** 27 total files across 4 tiers

---

## Complete Structure

```yaml
force_name:
  # === METADATA ===
  metadata:
    tier: 1 | 2 | 3 | 4
    category: "primordial" | "governing" | "interface" | "emergent"
    dependencies: [list_of_forces]  # Forces this depends on
    source_doc: "path/to/force_documentation.md"  # Reference to philosophy docs

  # === COLOR PROPERTIES ===
  color_properties:
    base_color: "#HEXCODE"  # Primary representative color
    color_family: "warm" | "cool" | "neutral"
    color_range:  # Array of hex values for agent selection
      - "#HEX1"  # Darker/less intense
      - "#HEX2"
      - "#HEX3"
      - "#HEX4"  # Brighter/more intense

    saturation_base: 0.0-1.0  # Base saturation level
    brightness_base: 0.0-1.0  # Base brightness level

    intensity_modifier:  # How activation level affects color
      low_activation:    # 0.1-0.3
        color: "#HEXCODE"
        saturation: 0.0-1.0
        brightness: 0.0-1.0
      medium_activation: # 0.4-0.7
        color: "#HEXCODE"
        saturation: 0.0-1.0
        brightness: 0.0-1.0
      high_activation:   # 0.8-1.0
        color: "#HEXCODE"
        saturation: 0.0-1.0
        brightness: 0.0-1.0

    notes: "Explanation of color choice and associations"

  # === SHAPE PROPERTIES ===
  shape_properties:
    primary_shape: "sphere" | "cube" | "torus" | "spiral" | "helix" | "fractal" | "organic" | "irregular"
    sacred_geometry_association: "flower_of_life" | "metatrons_cube" | "vesica_piscis" | "sri_yantra" | null
    complexity_level: "simple" | "medium" | "complex"
    edge_type: "sharp" | "smooth" | "organic" | "crystalline"
    dimensionality: "2D" | "3D" | "hybrid" | "4D_projected"

    activation_modulation:  # How shape changes with intensity
      low_activation: "description of shape at low intensity"
      medium_activation: "description of shape at medium intensity"
      high_activation: "description of shape at high intensity"

    notes: "Explanation of shape choice and symbolism"

  # === MOTION PROPERTIES ===
  motion_properties:
    movement_type: "expanding" | "contracting" | "rotating" | "oscillating" | "spiraling" | "stuck_looping" | "flowing" | "chaotic" | "stillness"

    speed_base: 0.0-1.0  # Base movement speed

    speed_modifier:  # How activation affects speed
      low_intensity: 0.0-1.0   # Slower
      medium_intensity: 0.0-1.0
      high_intensity: 0.0-1.0  # Faster

    direction: "inward" | "outward" | "circular" | "linear" | "chaotic" | "bidirectional" | "multidirectional"
    rhythm: "steady" | "erratic" | "pulsing" | "wave_like" | "staccato" | "smooth_continuous"

    healthy_pattern:
      description: "What healthy expression of this force looks like in motion"
      characteristics: ["trait1", "trait2", "trait3"]

    stuck_pattern:
      description: "What blocked/unhealthy expression looks like in motion"
      characteristics: ["trait1", "trait2", "trait3"]

    notes: "Explanation of motion patterns and their meaning"

  # === VIBRANCY & SATURATION ===
  vibrancy_saturation:
    vibrancy_base: 0.0-1.0  # Base vibrancy level

    coherence_impact:  # How overall coherence affects this force's vibrancy
      high_coherence:    # 0.7-1.0
        modifier: "+0.1 to +0.3"
        description: "Clear, vibrant, well-defined"
      medium_coherence:  # 0.4-0.7
        modifier: "0.0"
        description: "Normal vibrancy"
      low_coherence:     # 0.0-0.3
        modifier: "-0.2 to -0.4"
        description: "Dull, fragmented, unclear"

    intensity_scaling:
      formula: "vibrancy = base + (activation_level * multiplier)"
      multiplier: 0.0-1.0

    interaction_modifier:  # How presence of other forces affects vibrancy
      synergistic: "+0.1 to +0.2"  # Paired with compatible force
      antagonistic: "-0.2 to -0.3"  # Clashing with incompatible force
      neutral: "0.0"

    notes: "Explanation of vibrancy behavior"

  # === ADDITIONAL PROPERTIES ===
  additional_properties:
    texture: "smooth" | "rough" | "fractal" | "ethereal" | "solid" | "fluid" | "crystalline" | "organic"

    opacity_range:
      min: 0.0-1.0  # Minimum opacity (most transparent)
      max: 0.0-1.0  # Maximum opacity (most solid)

    particle_effects: true | false
    particle_type: "sparkles" | "trails" | "dust" | "smoke" | "energy_waves" | "none"
    particle_density: "sparse" | "moderate" | "dense"

    sound_association:  # Optional - for future audio integration
      frequency_hz: number | null
      tone_description: "description" | null
      musical_note: "note" | null

    emotional_tone: "heavy" | "light" | "tense" | "flowing" | "sharp" | "soft" | "electric" | "grounding"

    consciousness_association: 0.01-1.0  # From existing framework if applicable

    notes: "Additional context, reasoning, or special considerations"

  # === INTERACTION EFFECTS ===
  interaction_effects:
    synergistic_with:  # Forces that amplify/harmonize with this one
      - force_name_1
      - force_name_2

    antagonistic_with:  # Forces that clash/conflict with this one
      - force_name_3
      - force_name_4

    neutralizes:  # Forces that cancel out or dampen this one
      - force_name_5

    amplified_by:  # Forces that boost this one when present
      - force_name_6

    visual_blending_rules:  # Specific visual outcomes when combined
      when_combined_with_X:
        force: "specific_force_name"
        color_effect: "blend" | "clash" | "alternate" | "new_color" | "dominant"
        shape_effect: "merge" | "separate_interfering" | "hybrid_form" | "nested" | "orbiting"
        motion_effect: "synchronized" | "chaotic" | "stuttering" | "amplified" | "dampened"
        result_description: "What this combination looks like"
        coherence_dependent: true | false

    notes: "Explanation of interaction behaviors"
```

---

## Field Descriptions

### Metadata
- **tier:** Which tier (1-4) this force belongs to
- **category:** Philosophical classification
- **dependencies:** Which forces this inherits from or depends on
- **source_doc:** Path to the conceptual documentation for reference

### Color Properties
- **base_color:** The single most representative color (hex code)
- **color_family:** Warm (reds, oranges, yellows), cool (blues, greens, purples), or neutral (grays, browns)
- **color_range:** Array of 4-6 hex codes spanning the color family (agent selects from this)
- **saturation_base:** How saturated/vivid the base color is (0.0 = grayscale, 1.0 = maximum saturation)
- **brightness_base:** How bright the base color is (0.0 = black, 1.0 = maximum brightness)
- **intensity_modifier:** How the color shifts as force activation changes from low to high

### Shape Properties
- **primary_shape:** The geometric form that best represents this force
- **sacred_geometry_association:** Connection to established sacred geometry patterns (if any)
- **complexity_level:** Simple (sphere, cube), medium (torus, helix), complex (fractal, multi-part)
- **edge_type:** Quality of edges/boundaries
- **dimensionality:** 2D, 3D, or beyond
- **activation_modulation:** How the shape transforms at different intensities

### Motion Properties
- **movement_type:** Primary motion pattern
- **speed_base:** Default speed (0.0 = stillness, 1.0 = maximum speed)
- **speed_modifier:** How activation level affects speed
- **direction:** Where the motion is going
- **rhythm:** Quality/tempo of the motion
- **healthy_pattern:** What balanced expression looks like
- **stuck_pattern:** What imbalanced/blocked expression looks like

### Vibrancy & Saturation
- **vibrancy_base:** Default vibrancy level
- **coherence_impact:** How overall state coherence affects this force's visual clarity
- **intensity_scaling:** Mathematical relationship between activation and vibrancy
- **interaction_modifier:** How other forces affect this force's vibrancy

### Additional Properties
- **texture:** Surface quality
- **opacity_range:** Transparency range (allows for semi-transparent vs solid visuals)
- **particle_effects:** Whether this force generates particle effects
- **sound_association:** Optional audio properties for multi-sensory implementation
- **emotional_tone:** The felt quality of this force
- **consciousness_association:** If this force maps to a specific consciousness level

### Interaction Effects
- **synergistic_with:** Forces that work well together
- **antagonistic_with:** Forces that create tension
- **neutralizes:** Forces that cancel this one out
- **amplified_by:** Forces that boost this one
- **visual_blending_rules:** Specific outcomes when forces combine

---

## Usage Examples

### Example 1: Simple Force (Tier 1 - Coherence)

```yaml
coherence:
  metadata:
    tier: 1
    category: "primordial"
    dependencies: ["pattern", "consciousness"]
    source_doc: "docs/02_forces/tier_1_forces/04_coherence.md"

  color_properties:
    base_color: "#FFD700"  # Golden
    color_family: "warm"
    color_range: ["#FFA500", "#FFD700", "#FFEC8B", "#FFFACD"]
    saturation_base: 0.9
    brightness_base: 0.95
    intensity_modifier:
      low_activation:
        color: "#FFA500"
        saturation: 0.6
        brightness: 0.7
      medium_activation:
        color: "#FFD700"
        saturation: 0.9
        brightness: 0.95
      high_activation:
        color: "#FFFACD"
        saturation: 1.0
        brightness: 1.0
    notes: "Gold represents alignment, integration, and high-value coherence"

  shape_properties:
    primary_shape: "sphere"
    sacred_geometry_association: "flower_of_life"
    complexity_level: "simple"
    edge_type: "smooth"
    dimensionality: "3D"
    activation_modulation:
      low_activation: "Small, dim sphere"
      medium_activation: "Clear, defined sphere"
      high_activation: "Radiant, perfect sphere with flower of life pattern"
    notes: "Sphere represents wholeness and perfect symmetry"

  motion_properties:
    movement_type: "rotating"
    speed_base: 0.4
    speed_modifier:
      low_intensity: 0.2
      medium_intensity: 0.4
      high_intensity: 0.7
    direction: "circular"
    rhythm: "steady"
    healthy_pattern:
      description: "Smooth, steady rotation - all parts moving in harmony"
      characteristics: ["balanced", "stable", "integrated"]
    stuck_pattern:
      description: "Wobbling, irregular rotation - parts not synchronized"
      characteristics: ["fragmented", "unstable", "disconnected"]
    notes: "Steady rotation represents integrated, harmonious state"
```

### Example 2: Complex Force (Tier 3 - Fear)

```yaml
fear:
  metadata:
    tier: 3
    category: "interface"
    dependencies: ["entropy", "polarity", "time", "death"]
    source_doc: "docs/02_forces/tier_3_forces/02_fear.md"

  color_properties:
    base_color: "#2C3E50"
    color_family: "cool"
    color_range: ["#1A252F", "#2C3E50", "#34495E", "#4A5F7F"]
    saturation_base: 0.4
    brightness_base: 0.3
    intensity_modifier:
      low_activation:
        color: "#4A5F7F"
        saturation: 0.3
        brightness: 0.4
      medium_activation:
        color: "#2C3E50"
        saturation: 0.4
        brightness: 0.3
      high_activation:
        color: "#1A252F"
        saturation: 0.5
        brightness: 0.2
    notes: "Deep blue-gray represents contraction, survival mode, threat perception"

  shape_properties:
    primary_shape: "contracting_sphere"
    sacred_geometry_association: null
    complexity_level: "medium"
    edge_type: "sharp"
    dimensionality: "3D"
    activation_modulation:
      low_activation: "Soft sphere with gentle inward pull"
      medium_activation: "Sharper sphere collapsing inward"
      high_activation: "Dense, heavily compressed sphere with sharp spikes"
    notes: "Contraction represents withdrawal, defense, self-protection"

  motion_properties:
    movement_type: "contracting"
    speed_base: 0.3
    speed_modifier:
      low_intensity: 0.2
      medium_intensity: 0.5
      high_intensity: 0.9
    direction: "inward"
    rhythm: "pulsing"
    healthy_pattern:
      description: "Alert awareness with option to expand - breathing rhythm"
      characteristics: ["protective", "discerning", "appropriate"]
    stuck_pattern:
      description: "Constant contraction with no release - frozen, rigid"
      characteristics: ["paralyzed", "hypervigilant", "chronic"]
    notes: "Fear as adaptive (healthy) vs fear as chronic pattern (stuck)"

  interaction_effects:
    synergistic_with: ["pain", "judgment", "entropy"]
    antagonistic_with: ["love", "hope", "courage"]
    neutralizes: ["desire"]
    visual_blending_rules:
      when_combined_with_desire:
        force: "desire"
        color_effect: "alternating"
        shape_effect: "separate_interfering"
        motion_effect: "stuttering"
        result_description: "Fear sphere contracting while desire spiral tries to expand - creates paralysis/freeze"
        coherence_dependent: true
```

---

## Validation Checklist

When creating a force mapping, verify:

- [ ] All required fields present
- [ ] Hex codes are valid 6-character codes
- [ ] All numeric values within 0.0-1.0 range
- [ ] Dependencies list only existing forces
- [ ] Source doc path is correct
- [ ] Color range has 4-6 values
- [ ] Visual properties feel intuitively right for the force
- [ ] Healthy vs stuck patterns are clearly differentiated
- [ ] Interaction effects make philosophical sense
- [ ] Notes explain non-obvious choices

---

## Tier-Specific Mapping Considerations

**Source of Truth:** See `docs/04_advanced/advanced_concepts/06_tier_implications/` for complete tier characteristics and activation patterns.

These guidelines translate tier philosophical characteristics into visual properties for mapping files.

### **Tier 1 (Primordial Forces - Axioms)**

**Source:** `docs/04_advanced/advanced_concepts/06_tier_implications/29_tier_1_primordial.md`

**Activation Display:**
- **Doc concept:** "Always present, never zero, slow changes" (0.20-0.80 typical range)
- **Mapping rule:** Display Tier 1 forces at minimum 0.20 opacity even when "dormant"
- **Visual cue:** Subtle glow or outline even at low activation (shows "always present")
- **Motion cue:** Slow, steady changes (no instant jumps from 0 → 1)

**Shape Complexity:**
- **Why:** Foundational forces → foundational shapes
- **Guidance:** Simple to medium (sphere, cube, torus, platonic solids, basic sacred geometry)
- **Example:** coherence() = sphere (perfect symmetry), entropy() = dissolving cube

**Color Palette:**
- **Why:** Universal forces → archetypal colors
- **Guidance:** Primary colors, foundational tones (gold, white, deep blue, silver)
- **Saturation:** Moderate to high (clear, defined, not muted)

**Motion Patterns:**
- **Why:** High stability → steady motion
- **Guidance:** Continuous, predictable, regular rhythm (rotating, pulsing, flowing)
- **Avoid:** Erratic, chaotic, stuttering motion

**Particle Effects:**
- **Density:** Moderate (geometric patterns, subtle energy fields)
- **Type:** Ordered, symmetrical (not chaotic)

---

### **Tier 2 (Governing Forces - Universal Laws)**

**Source:** `docs/04_advanced/advanced_concepts/06_tier_implications/31_tier_2_governing.md`

**Activation Display:**
- **Doc concept:** "Background regulators, moderate baseline" (0.30-0.70 typical range)
- **Mapping rule:** Display at medium opacity (0.30-0.70 range), less prominent than T3
- **Visual cue:** Steady presence without overwhelming interface
- **Motion cue:** Rhythmic, cyclical (especially time, karma)

**Shape Complexity:**
- **Why:** Regulatory forces → structured forms
- **Guidance:** Medium complexity (more than T1, less than T4)
- **Example:** time() = flowing helix, karma() = möbius strip (return loop)

**Color Palette:**
- **Why:** Universal regulators → neutral/cosmic tones
- **Guidance:** Silver, gray, cosmic purple, transcendent tones
- **Saturation:** Moderate (not vivid like T3, not primary like T1)

**Motion Patterns:**
- **Why:** Regulatory function → ordered cycles
- **Guidance:** Cyclical, wave-like, regulatory (forward flow, return loops)
- **Example:** time() flows forward, karma() cycles back

**Particle Effects:**
- **Density:** Moderate to high (trails, energy waves, temporal effects)
- **Type:** Flowing, cyclical (not static, not chaotic)

---

### **Tier 3 (Interface Forces - Experience Layer)**

**Source:** `docs/04_advanced/advanced_concepts/06_tier_implications/33_tier_3_interface.md`

**Activation Display:**
- **Doc concept:** "Highly variable, full 0.0-1.0 range, rapid shifts"
- **Mapping rule:** Allow FULL opacity range including complete transparency (0.0)
- **Visual cue:** Dramatic changes in size/intensity when activated
- **Motion cue:** Can shift rapidly (fear contracts quickly, hope expands suddenly)

**Shape Complexity:**
- **Why:** Emotional forces → expressive forms
- **Guidance:** Simple to complex (depends on emotional quality)
- **Example:** fear() = contracting sphere (simple), love() = radiating mandala (complex)

**Color Palette:**
- **Why:** Interface forces → immediately recognizable
- **Guidance:** VIVID, emotionally resonant, highly saturated
- **Examples:** Fear=dark blue-gray, Love=radiant pink-gold, Hope=warm orange, Desire=magenta
- **Saturation:** HIGH (emotions are intense when present)

**Motion Patterns:**
- **Why:** Emotional forces → expressive movement
- **Guidance:** Variable, reflects emotional quality (expanding, contracting, radiating, freezing)
- **Example:** Desire expands outward, fear contracts inward, love radiates, judgment pierces

**Particle Effects:**
- **Density:** HIGH (emotional expression benefits from rich visual feedback)
- **Type:** Sparkles, energy bursts, trails, auras (expressive, dynamic)

---

### **Tier 4 (Emergent Forces - Composite Phenomena)**

**Source:** `docs/04_advanced/advanced_concepts/06_tier_implications/35_tier_4_emergent.md`

**Activation Display:**
- **Doc concept:** "Often dormant, sudden activation, brief peaks, rarely exceeds 0.80"
- **Mapping rule:** Can be completely invisible (0.0), appears suddenly when triggered
- **Visual cue:** Dramatic entrance when activated (0.0 → 0.7 quickly)
- **Motion cue:** Intense but brief (spike, then fade or stabilize)

**Shape Complexity:**
- **Why:** Emergent phenomena → emergent forms
- **Guidance:** MOST COMPLEX (fractals, hybrid forms, multi-part, impossible geometry)
- **Example:** madness() = fractured kaleidoscope, beauty() = perfect golden ratio spiral, war() = clashing shards

**Color Palette:**
- **Why:** Composite forces → blended or unique colors
- **Guidance:** Combinations of parent force colors OR distinctive novel signatures
- **Examples:**
  - courage() = fear(blue) + hope(orange) + fire(red) = bronze-copper
  - beauty() = pattern + coherence + consciousness = prismatic rainbow
  - madness() = entropy(purple) + pattern(distorted) = fractured spectrum

**Motion Patterns:**
- **Why:** Emergent forces → complex movement
- **Guidance:** Can be chaotic, sublime, multi-layered, clashing, or synthesized
- **Example:** music() = harmonic waves, war() = explosive collisions, art() = creative spirals

**Particle Effects:**
- **Density:** HIGHEST (complex emergent phenomena)
- **Type:** Complex combinations (fractured light, harmonic resonance, clashing energies)

---

### Summary Table (Visual Guidance)

| Tier | Can Be 0.0? | Shape | Color | Motion | Particles |
|------|------------|-------|-------|--------|-----------|
| **T1** | No (min 0.20) | Simple-Medium | Primary/Archetypal | Steady | Moderate |
| **T2** | Rare (min ~0.30) | Medium | Neutral/Cosmic | Cyclical | Mod-High |
| **T3** | YES | Simple-Complex | VIVID Emotional | Variable | HIGH |
| **T4** | YES (often) | Most Complex | Blended/Unique | Chaotic-Sublime | HIGHEST |

---

### Implementation Notes

**These are VISUAL TRANSLATIONS of philosophical characteristics documented in /docs, not new concepts.**

**When mapping a force:**
1. Read force's philosophical documentation FIRST (`docs/02_forces/tier_X_forces/`)
2. Check tier implication docs for tier-wide characteristics
3. Use tier mapping guidance as BASELINE
4. Adjust for force-specific nature (exceptions allowed when philosophically warranted)
5. Document source references in mapping file

**Example:**
```yaml
# mappings/forces/tier_1/coherence.yaml

# SOURCE: docs/02_forces/tier_1_forces/05_coherence.md
# TIER GUIDANCE: docs/04_advanced/advanced_concepts/06_tier_implications/29_tier_1_primordial.md

# TIER-SPECIFIC BASELINE (from T1 characteristics):
# - Activation: Never below 0.20 (always present)
# - Shape: Simple (sphere - perfect symmetry)
# - Color: Primary/archetypal (gold)
# - Motion: Steady rotation (stable, predictable)
# - Particles: Moderate geometric patterns

# FORCE-SPECIFIC ADJUSTMENTS (from coherence.md):
# - coherence FORCE (active integration work) vs coherence STATE (result)
# - Sphere = wholeness, perfection, alignment
# - Gold = high value, integration, "the golden thread"
# - At high activation: flower of life pattern appears
```

**Exceptions are allowed:**
- Tier provides baseline, force nature determines specifics
- Example: polarity() (T1) may have oscillating motion despite T1 "steady" guidance
- Example: beauty() (T4) may use simple perfect forms despite T4 "complex" guidance
- Always document exceptions and their philosophical reasoning

**Cross-Reference:**
- **Source of truth:** `docs/04_advanced/advanced_concepts/06_tier_implications/`
- **Individual force docs:** `docs/02_forces/tier_X_forces/`
- **Force dependencies:** `docs/03_mechanics/inheritance_chains/`

---

## Notes on Agent Modulation

These mappings provide **base guidance**. The actual implementation will use autonomous agents to:

1. **Select exact colors** from the color_range based on context
2. **Modulate shapes** based on activation level and coherence
3. **Adjust motion speeds** dynamically based on intensity
4. **Apply interaction effects** when multiple forces are present
5. **Determine vibrancy** based on coherence and interactions

The mappings define the **possibility space** - agents navigate within that space based on real-time context.

---

**Last Updated:** November 22, 2025
**Status:** Schema complete with tier-specific guidance, ready for force mapping creation
