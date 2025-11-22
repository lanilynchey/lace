# Visual Property Mapping Schema

**Purpose:** Defines the structure for cross-cutting visual property files in `mappings/visual_properties/`

**Format:** YAML (.yaml)
**Organization:** Files organized into 4 subcategories (colors, shapes, motion, additional)

**Note:** These files define **global visual systems** that apply across all forces, complementing the force-specific mappings.

---

## Visual Property Categories

### 1. Colors (`visual_properties/colors/`)
Global color theory, palettes, and intensity rules

### 2. Shapes (`visual_properties/shapes/`)
Geometric primitives library and sacred geometry associations

### 3. Motion (`visual_properties/motion/`)
Movement pattern definitions and speed/rhythm calibrations

### 4. Additional (`visual_properties/additional/`)
Texture, opacity, particle effects, and other visual modifiers

---

## File Structures

### colors/base_palette.yaml

```yaml
# Global color palette and theory
color_families:
  warm:
    description: "Reds, oranges, yellows - expansion, energy, action"
    hues: ["red", "orange", "yellow", "warm_pink", "coral"]
    associations: ["desire", "creation", "energy", "passion", "warmth"]

  cool:
    description: "Blues, greens, purples - contraction, reflection, calm"
    hues: ["blue", "green", "purple", "teal", "indigo"]
    associations: ["fear", "truth", "calm", "depth", "mystery"]

  neutral:
    description: "Grays, browns, black/white - balance, stability, grounding"
    hues: ["gray", "brown", "beige", "black", "white"]
    associations: ["polarity", "neutrality", "grounding", "stability"]

color_wheel:
  primary: ["#FF0000", "#00FF00", "#0000FF"]  # RGB
  secondary: ["#FF00FF", "#FFFF00", "#00FFFF"]  # CMY
  tertiary: [...]  # 6 tertiary colors

emotional_color_associations:
  # Standard color therapy associations
  red: ["passion", "anger", "energy", "danger"]
  blue: ["calm", "sadness", "trust", "cold"]
  yellow: ["joy", "caution", "optimism", "intellect"]
  green: ["growth", "envy", "balance", "nature"]
  purple: ["spirituality", "luxury", "mystery", "transformation"]
  orange: ["enthusiasm", "creativity", "warmth", "adventure"]
  # ... more associations

notes: "LACE uses custom color system based on force properties, not strict color therapy. These are reference points."
```

### colors/intensity_mapping.yaml

```yaml
# How force activation level affects color properties
intensity_scaling:
  saturation:
    low_activation:   # 0.1-0.3
      multiplier: 0.5-0.7
      description: "Desaturated, muted colors"
    medium_activation: # 0.4-0.7
      multiplier: 0.8-1.0
      description: "Normal saturation"
    high_activation:   # 0.8-1.0
      multiplier: 1.0-1.2
      description: "Highly saturated, vivid colors"

  brightness:
    low_activation:
      multiplier: 0.4-0.6
      description: "Darker, subdued"
    medium_activation:
      multiplier: 0.7-0.9
      description: "Normal brightness"
    high_activation:
      multiplier: 0.9-1.0
      description: "Bright, radiant"

  color_shift:
    description: "How colors shift along their range as activation increases"
    pattern: "Generally darker → lighter, cooler → warmer (for warm colors), warmer → cooler (for cool colors)"

notes: "These are defaults - individual forces may override with custom intensity mappings"
```

### colors/coherence_effects.yaml

```yaml
# How overall coherence affects visual appearance
coherence_impact:
  high_coherence:  # 0.7-1.0
    saturation_modifier: +0.2
    brightness_modifier: +0.1
    clarity: "sharp_defined"
    visual_quality: "Perfect sacred geometry, harmonious colors, clear boundaries"

  medium_coherence:  # 0.4-0.7
    saturation_modifier: 0.0
    brightness_modifier: 0.0
    clarity: "normal"
    visual_quality: "Recognizable patterns, some asymmetry, occasional distortion"

  low_coherence:  # 0.0-0.3
    saturation_modifier: -0.3
    brightness_modifier: -0.2
    clarity: "fragmented_blurred"
    visual_quality: "Chaotic, muddy colors, broken symmetry, visual noise"

color_blending_by_coherence:
  high: "Distinct, harmonious - forces maintain identity while complementing"
  medium: "Some blending, visible tension between forces"
  low: "Muddy mixing, incoherent color combinations"

notes: "Coherence is the master modifier - it affects ALL visual properties simultaneously"
```

### shapes/geometric_primitives.yaml

```yaml
# Library of available geometric forms
primitives:
  sphere:
    description: "Perfect symmetry, wholeness, completion"
    complexity: "simple"
    dimensions: "3D"
    variations: ["perfect", "compressed", "expanded", "textured"]
    forces_using: ["coherence", "consciousness"]

  cube:
    description: "Stability, structure, grounding"
    complexity: "simple"
    dimensions: "3D"
    variations: ["perfect", "rotated", "stretched", "fragmented"]
    forces_using: ["polarity", "truth"]

  torus:
    description: "Flow, circulation, infinite loop"
    complexity: "medium"
    dimensions: "3D"
    variations: ["smooth", "twisted", "nested", "expanding"]
    forces_using: ["time", "karma"]

  spiral:
    description: "Evolution, expansion, growth"
    complexity: "medium"
    dimensions: "3D"
    variations: ["fibonacci", "logarithmic", "inward", "outward"]
    forces_using: ["desire", "creation", "evolution"]

  fractal:
    description: "Self-similarity, infinite complexity"
    complexity: "complex"
    dimensions: "3D"
    variations: ["mandelbrot", "julia", "tree", "organic"]
    forces_using: ["pattern", "beauty", "art"]

  # ... more primitives (helix, platonic solids, etc.)

combination_rules:
  nested: "One shape inside another (e.g., sphere within torus)"
  merged: "Two shapes blended into hybrid form"
  orbiting: "Multiple shapes in relationship, moving around each other"
  interpenetrating: "Shapes passing through each other"

notes: "Shapes can morph and combine - these are base templates, not rigid forms"
```

### shapes/sacred_geometry.yaml

```yaml
# Sacred geometry associations for forces
sacred_forms:
  flower_of_life:
    description: "19 overlapping circles forming flower pattern"
    symbolism: "Creation, unity, interconnection"
    complexity: "high"
    forces_associated: ["coherence", "pattern", "consciousness"]

  metatrons_cube:
    description: "13 circles with lines connecting all centers"
    symbolism: "Universal structure, Platonic solids container"
    complexity: "very_high"
    forces_associated: ["creation", "truth", "pattern"]

  vesica_piscis:
    description: "Two overlapping circles, almond shape in center"
    symbolism: "Duality, balance, birth of form"
    complexity: "low"
    forces_associated: ["polarity", "creation", "love"]

  sri_yantra:
    description: "9 interlocking triangles radiating from center"
    symbolism: "Divine feminine/masculine balance, cosmic order"
    complexity: "very_high"
    forces_associated: ["coherence", "truth", "beauty"]

  golden_spiral:
    description: "Fibonacci-based logarithmic spiral"
    symbolism: "Natural growth, divine proportion"
    complexity: "medium"
    forces_associated: ["pattern", "beauty", "creation"]

  # ... more sacred forms

usage_guidelines:
  when_to_use: "High coherence states, forces with strong pattern/structure associations"
  when_not_to_use: "Low coherence states (forms fragment), chaotic/entropic forces"
  activation_requirement: "Generally requires 0.6+ coherence to render sacred geometry clearly"

notes: "Sacred geometry appears when coherence is high and force properties align with geometric principles"
```

### motion/movement_types.yaml

```yaml
# Catalog of movement patterns
movement_patterns:
  expanding:
    description: "Growing outward from center"
    feeling: "Growth, opening, reaching out"
    speed_range: [0.1, 0.8]
    forces_using: ["desire", "hope", "creation"]

  contracting:
    description: "Collapsing inward toward center"
    feeling: "Withdrawal, protection, consolidation"
    speed_range: [0.2, 0.9]
    forces_using: ["fear", "death"]

  rotating:
    description: "Spinning around axis"
    feeling: "Cycles, ongoing process, stability in motion"
    speed_range: [0.1, 0.7]
    forces_using: ["time", "coherence", "karma"]

  oscillating:
    description: "Back and forth, pendulum-like"
    feeling: "Indecision, balance-seeking, rhythm"
    speed_range: [0.3, 0.9]
    forces_using: ["polarity", "judgment"]

  spiraling:
    description: "Rotating while expanding/contracting"
    feeling: "Evolution, journey, transformation"
    speed_range: [0.2, 0.6]
    forces_using: ["creation", "desire", "evolution"]

  flowing:
    description: "Smooth, organic, water-like"
    feeling: "Ease, grace, natural progression"
    speed_range: [0.1, 0.5]
    forces_using: ["love", "forgiveness", "grace"]

  stuck_looping:
    description: "Tight circular pattern with no progress"
    feeling: "Stuck, addictive, repetitive"
    speed_range: [0.5, 1.0]
    forces_using: ["Used for blocked patterns of any force"]

  chaotic:
    description: "Erratic, unpredictable, irregular"
    feeling: "Disorder, overwhelm, fragmentation"
    speed_range: [0.3, 1.0]
    forces_using: ["entropy", "madness", "war"]

  stillness:
    description: "No movement, static"
    feeling: "Peace, presence, void, death"
    speed_range: [0.0, 0.0]
    forces_using: ["death", "neutrality"]

notes: "Movement type can shift based on healthy vs stuck expression of the same force"
```

### motion/healthy_vs_stuck.yaml

```yaml
# Patterns for healthy vs blocked force expression
healthy_motion_characteristics:
  flow: "Smooth, natural, progressive"
  rhythm: "Steady, predictable, sustainable"
  direction: "Clear purpose, moving toward integration"
  flexibility: "Can adapt, change direction when needed"
  integration: "Coordinated with other forces, harmonious"
  examples:
    - "Desire as forward spiral (healthy expansion toward goals)"
    - "Fear as breathing rhythm (healthy alert + release)"
    - "Time as steady rotation (healthy ongoing process)"

stuck_motion_characteristics:
  flow: "Stuttering, blocked, repetitive"
  rhythm: "Erratic, unsustainable, jarring"
  direction: "Circular with no progress, stuck in loops"
  rigidity: "Cannot adapt, locked in pattern"
  fragmentation: "Disconnected from other forces, isolated"
  examples:
    - "Desire as tight loop (addiction, obsession)"
    - "Fear as frozen contraction (paralysis, chronic anxiety)"
    - "Time as jagged oscillation (fragmented sense of past/present/future)"

visual_indicators:
  healthy:
    motion_quality: "Fluid, graceful, purposeful"
    shape_integrity: "Maintains form while moving"
    color: "Clear, vibrant"

  stuck:
    motion_quality: "Jerky, strained, repetitive"
    shape_integrity: "Distorted, fragmented"
    color: "Muddy, dull"

notes: "Same force can express as healthy or stuck - motion patterns reveal which"
```

### additional/texture_opacity.yaml

```yaml
# Texture and transparency properties
textures:
  smooth:
    description: "Clean, polished, refined"
    use_cases: ["High coherence forces", "Tier 1-2 forces"]
    forces_using: ["coherence", "love", "beauty"]

  rough:
    description: "Coarse, unrefined, gritty"
    use_cases: ["Low coherence forces", "Physical/grounded forces"]
    forces_using: ["war", "pain"]

  fractal:
    description: "Self-similar, infinitely detailed"
    use_cases: ["Pattern-based forces", "Complex forces"]
    forces_using: ["pattern", "art", "consciousness"]

  ethereal:
    description: "Translucent, light, airy"
    use_cases: ["High consciousness forces", "Spiritual forces"]
    forces_using: ["consciousness", "grace"]

  solid:
    description: "Dense, opaque, heavy"
    use_cases: ["Grounded forces", "Material forces"]
    forces_using: ["death", "polarity"]

  fluid:
    description: "Liquid-like, flowing, organic"
    use_cases: ["Flowing forces", "Emotional forces"]
    forces_using: ["love", "forgiveness", "fear"]

opacity_guidelines:
  high_opacity: # 0.8-1.0
    description: "Solid, clearly defined, strong presence"
    when: "High activation, clear force expression, good boundaries"

  medium_opacity: # 0.5-0.7
    description: "Visible but somewhat transparent, moderate presence"
    when: "Medium activation, normal expression"

  low_opacity: # 0.2-0.4
    description: "Translucent, subtle, weak presence"
    when: "Low activation, emerging or fading force"

  variable_opacity:
    description: "Changes based on context, breathing effect"
    when: "Dynamic forces, oscillating patterns"

notes: "Texture and opacity add dimension - use to differentiate similar forces"
```

### additional/particle_effects.yaml

```yaml
# Particle systems for visual enhancement
particle_types:
  sparkles:
    description: "Small, bright, twinkling points"
    effect: "Magic, joy, high energy"
    density_range: ["sparse", "moderate", "dense"]
    forces_using: ["hope", "beauty", "joy"]

  trails:
    description: "Motion blur, path marking"
    effect: "Movement history, momentum"
    density_range: ["light", "moderate", "heavy"]
    forces_using: ["time", "creation", "desire"]

  dust:
    description: "Fine particles drifting"
    effect: "Age, decay, entropy"
    density_range: ["sparse", "moderate", "thick"]
    forces_using: ["entropy", "death", "memory"]

  smoke:
    description: "Wispy, flowing, dissipating"
    effect: "Mystery, transformation, obscurity"
    density_range: ["light", "moderate", "heavy"]
    forces_using: ["madness", "mystery", "entropy"]

  energy_waves:
    description: "Rippling, radiating pulses"
    effect: "Power, broadcast, influence"
    density_range: ["subtle", "moderate", "intense"]
    forces_using: ["creation", "consciousness", "truth"]

  none:
    description: "No particle effects"
    effect: "Clean, simple, minimal"
    forces_using: ["Forces that don't need particles"]

usage_guidelines:
  when_to_add: "High activation, dramatic expression, need for emphasis"
  when_to_omit: "Low activation, minimal expression, clean aesthetic desired"
  performance_note: "Particle effects are computationally expensive - use sparingly"

notes: "Particles are optional enhancement, not required. Default to 'none' unless force specifically benefits."
```

---

## Usage Notes

These visual property files serve as:

1. **Reference libraries** for force mappers creating individual force files
2. **Global systems** that apply across all forces (e.g., coherence effects)
3. **Shared vocabularies** for consistent terminology
4. **Implementation guidance** for developers building the visual system

When creating force mappings, reference these files for:
- Available shape options
- Color theory foundations
- Movement pattern definitions
- Texture and opacity standards
- Particle effect options

When implementing the visual system, these files provide:
- Global coherence modifiers
- Intensity scaling rules
- Interaction blending rules
- Healthy vs stuck motion patterns

---

**Last Updated:** November 21, 2025
**Status:** Schema complete, ready for visual property file creation
