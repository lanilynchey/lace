# LACE Mappings Navigation Guide

**Last Updated:** November 22, 2025
**Purpose:** Fast lookup guide for finding information across 83+ mapping files
**Total Files:** 83+ files across 9 directories

---

## Quick Directory Overview

```
mappings/
├── forces/                    # 26 force files (base visual properties per force)
├── visual_properties/         # 16 cross-cutting visual system files
├── interactions/              # 8 force interaction & visual blending files
├── lifestyle/                 # 34 lifestyle factor modifier files
├── scales/                    # 5 reference scale files
├── schemas/                   # 3 schema/template documentation files
└── NAVIGATION_GUIDE.md       # This file!
```

---

## Looking for Force Information?

### Base Force Mappings (colors, shapes, motion, etc.)

**Location:** `mappings/forces/tier_X/[force_name].yaml`

**Which forces exist where:**

**Tier 1 (Primordial) - 5 forces:**
- `forces/tier_1/entropy.yaml`
- `forces/tier_1/consciousness.yaml`
- `forces/tier_1/pattern.yaml`
- `forces/tier_1/coherence.yaml`
- `forces/tier_1/polarity.yaml`

**Tier 2 (Governing) - 6 forces:**
- `forces/tier_2/time.yaml`
- `forces/tier_2/karma.yaml`
- `forces/tier_2/truth.yaml`
- `forces/tier_2/memory.yaml`
- `forces/tier_2/death.yaml`
- `forces/tier_2/creation.yaml`

**Tier 3 (Interface) - 7 forces:**
- `forces/tier_3/desire.yaml`
- `forces/tier_3/fear.yaml`
- `forces/tier_3/hope.yaml`
- `forces/tier_3/forgiveness.yaml`
- `forces/tier_3/love.yaml`
- `forces/tier_3/pain.yaml`
- `forces/tier_3/judgment.yaml`

**Tier 4 (Emergent) - 8 forces:**
- `forces/tier_4/art.yaml`
- `forces/tier_4/music.yaml`
- `forces/tier_4/war.yaml`
- `forces/tier_4/madness.yaml`
- `forces/tier_4/beauty.yaml`
- `forces/tier_4/luck.yaml`
- `forces/tier_4/humor.yaml`
- `forces/tier_4/courage.yaml`

**What's in each force file:**
- Base colors (primary/secondary with hex codes)
- Base shapes (geometric forms and sacred geometry)
- Base motion (movement type, speed, rhythm)
- Additional properties (texture, opacity, particles)
- Intensity modifiers (how activation level affects appearance)
- Interaction effects (how force changes when interacting)
- Tier-specific guidance

---

## Looking for Visual Property Rules?

**Location:** `mappings/visual_properties/[category]/[file].yaml`

### Colors (4 files)

**Base color palette & theory:**
→ `visual_properties/colors/base_palette.yaml`
- Color families (warm, cool, neutral)
- Color wheel (primary, secondary, tertiary)
- Emotional color associations

**How activation affects colors:**
→ `visual_properties/colors/intensity_mapping.yaml`
- Saturation by activation level
- Brightness by activation level
- Color shift patterns

**How coherence affects colors:**
→ `visual_properties/colors/coherence_effects.yaml`
- High coherence: vivid, harmonious
- Medium coherence: normal
- Low coherence: muddy, chaotic

**How force interactions affect colors:**
→ `visual_properties/colors/interaction_effects.yaml`
- Force collision color rules
- Blending vs separation patterns

---

### Shapes (4 files)

**Available geometric forms:**
→ `visual_properties/shapes/geometric_primitives.yaml`
- Sphere, cube, torus, spiral, fractal, etc.
- Combination rules (nested, merged, orbiting)

**Sacred geometry associations:**
→ `visual_properties/shapes/sacred_geometry.yaml`
- Flower of life, Metatron's cube, etc.
- Force-to-sacred-form mappings

**Shape complexity by tier:**
→ `visual_properties/shapes/complexity_by_tier.yaml`
- Tier 1: Simple, foundational forms
- Tier 2: Medium complexity
- Tier 3: Variable complexity
- Tier 4: Complex, composite forms

**Edge/surface textures:**
→ `visual_properties/shapes/edge_textures.yaml`
- Smooth, rough, crystalline, organic
- Texture by coherence and force type

---

### Motion (4 files)

**Types of movement:**
→ `visual_properties/motion/movement_types.yaml`
- Linear, circular, spiral, chaotic, stillness
- Movement vocabulary

**Speed calibrations:**
→ `visual_properties/motion/speed_calibrations.yaml`
- Speed by activation level
- Speed by force tier
- Relative motion scaling

**Rhythm & pulse patterns:**
→ `visual_properties/motion/rhythm_patterns.yaml`
- Steady, pulsing, erratic, breathing
- Rhythm tied to force characteristics

**Healthy vs stuck motion:**
→ `visual_properties/motion/healthy_vs_stuck.yaml`
- Healthy: fluid, dynamic, balanced
- Stuck: frozen, looping, stuttering

---

### Additional Properties (3 files)

**Particle effects:**
→ `visual_properties/additional/particle_effects.yaml`
- Sparkles, trails, auras, emanations
- Particle behavior by force

**Texture & opacity:**
→ `visual_properties/additional/texture_opacity.yaml`
- Surface qualities (smooth, rough, crystalline)
- Transparency/opacity rules

**Vibrancy & saturation:**
→ `visual_properties/additional/vibrancy_saturation.yaml`
- Overall visual energy/intensity
- Saturation modulation rules

---

### Rendering Hierarchy (1 file)

**Visual prominence when multiple forces active:**
→ `visual_properties/rendering_hierarchy.yaml`
- Which forces should be foreground vs background
- 5 prominence tiers (dominant, strong, moderate, low, dormant)
- Tier-based modulation (foundational vs emergent)
- Interaction-based prominence effects
- Coherence-based clarity modulation
- Complete implementation guidance with worked examples

---

## Looking for Interaction Rules?

**Location:** `mappings/interactions/[category]/[file].yaml`

### Force-to-Force Interactions (4 files + matrix)

**Synergistic pairs (amplify):**
→ `interactions/force_to_force/synergistic_pairs.yaml`
- Forces that strengthen each other
- Example: desire + hope = amplified manifestation drive

**Antagonistic pairs (cancel):**
→ `interactions/force_to_force/antagonistic_pairs.yaml`
- Forces that weaken/oppose each other
- Example: fear + courage = tension/override

**Neutralizing pairs (balance):**
→ `interactions/force_to_force/neutralizing_pairs.yaml`
- Forces that create equilibrium
- Example: entropy + creation = dynamic balance

**Complex interactions (3+ forces):**
→ `interactions/force_to_force/complex_interactions.yaml`
- Multi-force combinations
- Emergent phenomena from force synthesis

**Complete interaction matrix:**
→ `interactions/interaction_matrix.yaml`
- 26×26 force interaction lookup table
- Quick reference for any force pair

---

### Visual Blending (3 files)

**How colors mix when forces interact:**
→ `interactions/visual_blending/color_mixing_rules.yaml`
- Additive vs subtractive blending
- Gradient creation between forces
- Dominant force color rules

**How shapes interact/combine:**
→ `interactions/visual_blending/shape_interaction_rules.yaml`
- Nesting, merging, orbiting patterns
- Shape morphing during interaction
- Geometric interference patterns

**How motion patterns collide:**
→ `interactions/visual_blending/motion_collision_rules.yaml`
- Motion synchronization
- Motion cancellation
- Emergent motion patterns

---

## Looking for Lifestyle Factor Effects?

**Location:** `mappings/lifestyle/[category]/[file].yaml`

### Physical Body (6 files)

- `lifestyle/physical_body/sleep_quality.yaml`
- `lifestyle/physical_body/exercise_frequency.yaml`
- `lifestyle/physical_body/breath_work.yaml`
- `lifestyle/physical_body/posture_alignment.yaml`
- `lifestyle/physical_body/hydration.yaml`
- `lifestyle/physical_body/cold_exposure.yaml`

### Food & Nutrition (2 files)

- `lifestyle/food_nutrition/diet_quality.yaml`
- `lifestyle/food_nutrition/meal_timing.yaml`

### Mental & Spiritual (6 files)

- `lifestyle/mental_spiritual/meditation_practice.yaml`
- `lifestyle/mental_spiritual/gratitude_practice.yaml`
- `lifestyle/mental_spiritual/self_compassion.yaml`
- `lifestyle/mental_spiritual/therapy_counseling.yaml`
- `lifestyle/mental_spiritual/learning_practice.yaml`
- `lifestyle/mental_spiritual/journaling_practice.yaml`

### Social Connections (2 files)

- `lifestyle/social_connections/social_connection_quality.yaml`
- `lifestyle/social_connections/intimacy_depth.yaml`

### Work & Productivity (3 files)

- `lifestyle/work_productivity/purpose_work_alignment.yaml`
- `lifestyle/work_productivity/work_life_balance.yaml`
- `lifestyle/work_productivity/autonomy_agency.yaml`

### Creative & Expressive (2 files)

- `lifestyle/creative_expressive/creative_expression.yaml`
- `lifestyle/creative_expressive/play_recreation.yaml`

### Environment & Nature (3 files)

- `lifestyle/environment_nature/nature_exposure.yaml`
- `lifestyle/environment_nature/sunlight_exposure.yaml`
- `lifestyle/environment_nature/air_quality.yaml`

### Media & Information (2 files)

- `lifestyle/media_information/screen_time.yaml`
- `lifestyle/media_information/content_quality.yaml`

**Total:** 34 lifestyle factors across 8 categories

**What's in each lifestyle file:**
- Factor description and scale (0.0-1.0)
- Affected forces with modifiers (+/- values)
- Temporal dynamics (onset time, duration, decay)
- Thresholds (when effects activate)
- Interaction effects with other factors

---

## Looking for Reference Scales?

**Location:** `mappings/scales/[file].yaml`

**Force activation levels (dormant/low/medium/high/extreme):**
→ `scales/force_activation_ranges.yaml`
- Activation intensity ranges (0.0-1.0)
- Visual impact by activation level
- Activation dynamics (rate of change by force)
- Typical activation ranges by tier

**Consciousness levels & perception abilities:**
→ `scales/consciousness_levels.yaml`
- Consciousness scale (0.0-1.0)
- Perceptual capacities at each level
- Visual rendering capabilities
- Threshold effects

**Coherence thresholds & manifestation power:**
→ `scales/coherence_thresholds.yaml`
- Coherence scale (0.0-1.0)
- Manifestation power by coherence
- Visual quality thresholds
- System state implications

**Mastery levels (novice to master):**
→ `scales/mastery_levels.yaml`
- 7 mastery levels (0.0-1.0)
- Skill indicators at each level
- Force activation impacts by mastery
- Cross-domain mastery transfer

**Temporal dynamics & change rates:**
→ `scales/temporal_dynamics.yaml`
- Force activation/deactivation rates by tier
- Coherence shift timelines
- Lifestyle factor onset timelines
- Recovery and adaptation periods

---

## Looking for Schema/Template Files?

**Location:** `mappings/schemas/[file].md`

**Force mapping file structure:**
→ `schemas/force_mapping_schema.md`
- Template for creating new force files
- Required sections and fields
- Format specifications
- Examples

**Lifestyle factor file structure:**
→ `schemas/lifestyle_factor_schema.md`
- Template for creating new lifestyle files
- Required sections and fields
- Modifier magnitude guidance
- Temporal dynamics structure

**Visual property file structure:**
→ `schemas/visual_property_schema.md`
- Template for creating visual property files
- Cross-cutting system definitions
- Format specifications
- Examples

---

## Common Use Cases

### "How does [force] look visually?"

**Steps:**
1. Check `forces/tier_X/[force].yaml` for base properties (colors, shapes, motion)
2. Check `visual_properties/colors/intensity_mapping.yaml` for activation effects
3. Check `visual_properties/colors/coherence_effects.yaml` for coherence modulation
4. Check `visual_properties/motion/speed_calibrations.yaml` for motion scaling

**Example: "How does fear look visually?"**
1. `forces/tier_3/fear.yaml` → base color: icy blue, base shape: jagged spikes, base motion: jittery
2. `intensity_mapping.yaml` → high fear activation = darker blue, faster motion
3. `coherence_effects.yaml` → low coherence = fragmented, chaotic appearance
4. Result: High fear + low coherence = dark fragmented spikes moving jerkily

---

### "How do [force A] and [force B] interact?"

**Steps:**
1. Check `interactions/interaction_matrix.yaml` for quick lookup
2. Check `interactions/force_to_force/` for detailed interaction mechanics
3. Check `interactions/visual_blending/` for visual representation rules

**Example: "How do fear and hope interact?"**
1. `interaction_matrix.yaml` → antagonistic tension (fear suppresses hope)
2. `force_to_force/antagonistic_pairs.yaml` → detailed mechanics
3. `visual_blending/color_mixing_rules.yaml` → icy blue vs warm gold = contested gradient

---

### "What lifestyle factors affect [force]?"

**Steps:**
1. Search all `lifestyle/` category folders for force name
2. Each lifestyle file lists affected forces with modifiers
3. Cross-reference with force file to see complete impact

**Example: "What lifestyle factors affect coherence?"**
- Search lifestyle files for "coherence"
- Find: sleep_quality (+0.15), meditation_practice (+0.20), exercise (+0.08), etc.
- Cross-reference with `forces/tier_1/coherence.yaml` for visual impact

---

### "What changes quickly vs slowly?"

**Steps:**
1. Check `scales/temporal_dynamics.yaml` for tier-by-tier timelines
2. Check `scales/force_activation_ranges.yaml` activation_dynamics section for speed categories
3. Check tier implication docs for conceptual understanding

**Example: "Which forces change instantly?"**
1. `temporal_dynamics.yaml` → Tier 3 forces: seconds to minutes
2. `force_activation_ranges.yaml` → instant_shift category: fear, pain, desire, beauty, courage
3. Tier docs → explains why (survival/emotional responses)

---

### "What's normal for Tier X forces?"

**Steps:**
1. Check tier implication docs (`docs/04_advanced/advanced_concepts/06_tier_implications/`)
2. Check `scales/temporal_dynamics.yaml` for tier-specific patterns
3. Check `scales/force_activation_ranges.yaml` activation_dynamics for tier groupings

**Example: "What's normal for Tier 1 forces?"**
1. Tier docs → always present, rarely at extremes, slow changes
2. `temporal_dynamics.yaml` → typical range 0.20-0.80, changes over days-months
3. `force_activation_ranges.yaml` → gradual_shift category lists all Tier 1 forces

---

### "How do I create a new [force/lifestyle/visual property] file?"

**Steps:**
1. Check appropriate schema file for template
2. Follow required sections and format
3. Reference similar existing files for examples

**Example: "How do I create a new force file for 'love'?"**
1. Check `schemas/force_mapping_schema.md` for template
2. Follow sections: base_colors, base_shapes, base_motion, intensity_modifiers, etc.
3. Reference `forces/tier_3/fear.yaml` as Tier 3 example

---

## File Organization Principles

### Directory Purposes

**forces/tier_X/:** Individual force mappings
- **Purpose:** "What does THIS specific force look like?"
- **Contains:** Complete visual properties for one force
- **One file per force:** All properties in single location

**visual_properties/:** Cross-cutting visual systems
- **Purpose:** "How does THIS visual system work across ALL forces?"
- **Contains:** Global rules applying to all forces
- **Examples:** Color theory, shape library, motion vocabulary

**interactions/:** Force combination mechanics
- **Purpose:** "What happens when forces/visuals COMBINE?"
- **Contains:** Force-to-force relationships, visual blending rules
- **Examples:** Synergistic pairs, color mixing, shape merging

**lifestyle/:** External factor modifiers
- **Purpose:** "How does THIS lifestyle factor MODIFY forces?"
- **Contains:** Force activation modifiers from lifestyle choices
- **Examples:** Sleep quality affects coherence, exercise affects entropy

**scales/:** Reference ranges and thresholds
- **Purpose:** "What do these numbers mean?"
- **Contains:** Scale definitions, thresholds, temporal patterns
- **Examples:** Activation ranges, consciousness levels, mastery stages

**schemas/:** Templates and documentation
- **Purpose:** "How do I create new files?"
- **Contains:** File structure templates, format specs, examples
- **Examples:** Force schema, lifestyle schema, visual property schema

---

### Key Distinctions

**Force files vs Visual property files:**
- **Force file:** ALL visual properties for ONE force (fear.yaml = fear's colors + shapes + motion)
- **Visual property file:** ONE visual system for ALL forces (base_palette.yaml = color theory for all forces)

**Interaction files vs Force files:**
- **Force file:** How force appears in isolation
- **Interaction file:** How forces change when combined

**Lifestyle files vs Force files:**
- **Force file:** Force's intrinsic properties
- **Lifestyle file:** External factors that modify force activation

**Scales vs Schemas:**
- **Scale file:** Reference ranges and thresholds (what numbers mean)
- **Schema file:** File structure templates (how to create files)

---

## Document Hierarchy

**Source of Truth:** `/docs` directory
- All conceptual content originates in documentation
- Philosophical foundation, force definitions, system laws

**Display Layer:** `/mappings` directory (THIS directory)
- ⚠️ **MAPPINGS DISPLAY DOCS - NOTHING ORIGINATES HERE**
- Visual representation of documented concepts
- Practical implementation guidance
- All content sourced from /docs

**Cross-References:**
- Mapping files reference doc files as `source_docs`
- When in doubt, check docs for conceptual clarity
- Mappings organize doc content for implementation

---

## Tips for Navigation

1. **Start broad, narrow down:** Directory → category → specific file
2. **Use schemas for structure:** Templates show what's available
3. **Follow cross-references:** Files link to related content
4. **Check "see_also" sections:** Files suggest related lookups
5. **Common pattern:** Force file → visual property files → interaction files
6. **Update this guide:** When adding files, update navigation guide

---

## Future Additions (Planned)

- **mastery/:** Mastery-specific visual modifications
- **emergent_conditions/:** Tier 4 activation condition mappings
- **lifestyle/substances/:** Substance effects (caffeine, alcohol, etc.)
- **lifestyle/trauma_healing/:** Trauma/shadow work factors

---

**Questions? Check:**
1. This navigation guide (orientation)
2. Schema files (structure/templates)
3. Scale files (reference ranges)
4. Docs directory (conceptual foundation)

**Need to add a file? Check:**
1. Appropriate schema for template
2. Similar existing files for examples
3. Update this navigation guide when done

---

*Last Updated: November 22, 2025*
*Total Files: 93+ (26 forces complete, 16 visual properties, 8 interactions, 34 lifestyle, 5 scales, 3 schemas)*
