# Lifestyle Factor Mapping Schema

**Purpose:** Defines the structure for lifestyle factor → force activation mappings in `mappings/lifestyle/`

**Format:** YAML (.yaml)
**Organization:** One file per lifestyle factor, organized into 8 category folders

---

## Complete Structure

```yaml
factor_name:
  # === METADATA ===
  metadata:
    category: "food_nutrition" | "environment_nature" | "social_connections" | "physical_body" | "creative_expressive" | "media_information" | "mental_spiritual" | "work_productivity"
    measurement_unit: "min/day" | "hours/week" | "servings/day" | "times/week" | "quality_scale" | "binary" | "custom"
    data_source: "self_report" | "health_app" | "wearable" | "external_api"

  # === THRESHOLDS ===
  thresholds:
    low:
      range: [lower_bound, upper_bound]  # Array format: [inclusive_lower, exclusive_upper]
      midpoint: value                     # Representative value for interpolation (required)
      description: "What 'low' means for this factor"
    medium:
      range: [lower_bound, upper_bound]
      midpoint: value
      description: "What 'medium' means for this factor"
    high:
      range: [lower_bound, null]          # null for open-ended upper bound (e.g., "60+")
      midpoint: value
      ceiling: value                      # Optional: max value for interpolation in open-ended ranges
      description: "What 'high' means for this factor"

  # Optional: very_low and very_high thresholds for factors with wide ranges
  # very_low:
  #   range: [lower_bound, upper_bound]
  #   midpoint: value
  #   description: "Extreme low"
  # very_high:
  #   range: [lower_bound, null]
  #   midpoint: value
  #   ceiling: value
  #   description: "Extreme high"

  # === FORCE IMPACTS ===
  force_impacts:
    force_name_1:
      low: +/-0.XX     # Modifier at low threshold
      medium: +/-0.XX  # Modifier at medium threshold
      high: +/-0.XX    # Modifier at high threshold
      reasoning: "Why this force is affected by this lifestyle factor"

    force_name_2:
      low: +/-0.XX
      medium: +/-0.XX
      high: +/-0.XX
      reasoning: "Explanation"

    # Include all forces affected (typically 3-8 forces per lifestyle factor)

  # === INTERACTION EFFECTS ===
  interaction_effects:  # Optional - how this factor interacts with others
    synergistic_with:
      - factor_name: "other_lifestyle_factor"
        effect: "Combined effect amplified"
    antagonistic_with:
      - factor_name: "other_lifestyle_factor"
        effect: "Combined effect reduced or canceled"

  # === TEMPORAL DYNAMICS ===
  temporal_dynamics:  # Optional - time-based effects
    immediate_effect: "What happens within hours"
    short_term_effect: "What happens within days (1-7)"
    long_term_effect: "What happens over weeks/months (7+)"
    cumulative: true | false  # Does this build up over time?
    decay_rate: "fast" | "moderate" | "slow" | null

  # === NOTES ===
  notes: "Additional context, research references, special considerations, implementation notes"

  # === RESEARCH SUPPORT ===
  research_support:  # Optional - evidence base
    empirical_evidence: "Brief summary of research supporting these mappings"
    anecdotal_evidence: "Common patterns observed"
    lace_framework_basis: "How this connects to LACE philosophy"
```

---

## Field Descriptions

### Metadata
- **category:** Which lifestyle domain this belongs to
- **measurement_unit:** How this factor is measured
- **data_source:** Where the data comes from (self-report, device, API)

### Thresholds
Define what constitutes "low", "medium", and "high" levels for this factor.
- **range:** Array `[lower, upper]` using lower-inclusive, upper-exclusive convention
  - `[0, 20]` means 0 ≤ value < 20
  - Use `null` for open-ended upper bounds: `[60, null]` means 60+
- **midpoint:** Representative value for this threshold (required for interpolation)
  - Typically the middle of the range: `[0, 20]` → midpoint 10
  - For open-ended ranges, use reasonable estimate: `[60, null]` → midpoint 90
- **ceiling:** (Optional) Maximum value for interpolation in open-ended ranges
  - Prevents unrealistic extrapolation beyond diminishing returns
  - Example: `[60, null]` with ceiling 120 caps interpolation at 120 min
- **description:** Human-readable explanation of what this threshold means
- Can add "very_low" and "very_high" for factors with extreme ranges

### Force Impacts
List all forces affected by this lifestyle factor with modifier values.

**Positive modifiers (+):** Increase the force level
**Negative modifiers (-):** Decrease the force level
**Zero (0.00):** No effect at that threshold

Include "reasoning" to explain WHY this force is affected.

### Interaction Effects
How this lifestyle factor interacts with other lifestyle factors:
- **Synergistic:** Combined effect is greater than sum
- **Antagonistic:** Combined effect is less than sum or canceled

### Temporal Dynamics
How quickly effects manifest and how long they last:
- **Immediate:** Within hours (e.g., caffeine, meditation)
- **Short-term:** Within days (e.g., sleep improvement)
- **Long-term:** Weeks/months (e.g., diet changes, exercise routine)
- **Cumulative:** Does the effect build over time?
- **Decay rate:** How quickly the effect fades without maintenance

### Notes
Any additional context, caveats, or implementation considerations.

### Research Support
Optional field to cite evidence:
- Empirical research (studies, data)
- Anecdotal patterns (commonly observed)
- LACE framework basis (philosophical reasoning)

---

## Modifier Magnitude Decision Tree

**Purpose:** Guidance for determining appropriate modifier sizes when creating lifestyle factor files

**Principle:** Modifier magnitude should reflect the force's sensitivity to this lifestyle factor AND the lifestyle factor's overall importance.

---

### Magnitude Categories

#### MINIMAL (±0.01 to ±0.08)
**Use when:**
- Very subtle effects
- Force has low sensitivity to this factor
- Factor has minor importance
- Effects are indirect or secondary

**Examples:**
- Screen time's effect on pattern recognition: ±0.05
- Meal timing's effect on consciousness: ±0.03
- Air quality's effect on judgment: ±0.05

**Characteristics:**
- Barely noticeable impact
- Multiple factors needed to see meaningful change
- Often used for "nice to have" factors

---

#### SMALL (±0.08 to ±0.15)
**Use when:**
- Noticeable but not major effects
- Force has moderate sensitivity to this factor
- Factor has some importance but isn't foundational
- Effects accumulate over time

**Examples:**
- Exercise's effect on entropy: -0.12
- Diet quality's effect on coherence: +0.10
- Nature exposure's effect on fear: -0.15
- Gratitude practice's effect on hope: +0.12

**Characteristics:**
- Noticeable with consistent practice
- Part of healthy baseline lifestyle
- Contributes to overall wellbeing
- Cumulative effects matter

---

#### MODERATE (±0.15 to ±0.30)
**Use when:**
- Significant, clearly noticeable effects
- Force has high sensitivity to this factor
- Factor has substantial importance
- Effects are direct and measurable

**Examples:**
- Sleep quality's effect on coherence: -0.25 (low) / +0.15 (high)
- Meditation practice's effect on fear: -0.20 (medium) / -0.35 (high)
- Social connection quality's effect on love: +0.25
- Exercise's effect on pain: -0.20

**Characteristics:**
- Clearly felt impact
- Important for transformation
- Direct cause-effect relationship
- Measurable within days/weeks

---

#### LARGE (±0.30 to ±0.45)
**Use when:**
- Major, profound effects
- Force has extreme sensitivity to this factor
- Factor is foundational/critical
- Effects are immediate and dramatic

**Examples:**
- Meditation practice's effect on coherence: +0.40 (high)
- Sleep deprivation's effect on entropy: +0.30
- Sunlight exposure's effect on circadian rhythm: -0.40 (low) / +0.35 (high)
- Meditation practice's effect on consciousness: +0.35 (high)

**Characteristics:**
- Profound, transformative impact
- Critical for healthy functioning
- Often foundational practices (sleep, meditation, sunlight)
- Effects visible quickly

---

#### EXTREME (±0.45+)
**Use when:**
- Life-or-death impacts
- Complete system breakdown or breakthrough
- Critical survival factors
- Rare and exceptional circumstances

**Examples:**
- Severe sleep deprivation (36+ hours): entropy +0.50, coherence -0.45
- Acute trauma: coherence -0.60, fear +0.55
- Near-death experience: consciousness +0.70 (temporary peak)
- Severe malnutrition: all forces -0.40 to -0.60

**Characteristics:**
- System-level crisis or breakthrough
- Not sustainable (temporary extremes)
- Rare in normal lifestyle mapping
- Use sparingly, only for genuine extremes

---

### Decision Criteria

**Ask these questions when determining magnitude:**

1. **How sensitive is the force to this factor?**
   - Low sensitivity → smaller modifier
   - High sensitivity → larger modifier

2. **How important is this lifestyle factor overall?**
   - Minor factor → smaller modifier
   - Critical factor → larger modifier

3. **Is the effect direct or indirect?**
   - Direct → larger modifier
   - Indirect → smaller modifier

4. **How quickly are effects felt?**
   - Immediate → potentially larger (if also important)
   - Delayed → potentially smaller (unless cumulative)

5. **Is this foundational or supplementary?**
   - Foundational (sleep, food, safety) → larger modifiers
   - Supplementary (hobbies, preferences) → smaller modifiers

---

### Magnitude by Force Type

**Tier 1 Forces (Primordial - slow-changing):**
- Generally require LARGER modifiers to shift (0.15-0.40)
- Effects accumulate over time
- Foundational lifestyle factors have strongest impact
- Examples: sleep → coherence (+0.15), meditation → consciousness (+0.35)

**Tier 2 Forces (Governing - background):**
- Generally use MODERATE modifiers (0.10-0.30)
- Effects systematic and regulatory
- Lifestyle factors influence rhythms and patterns
- Examples: sunlight → circadian rhythm (+0.35), journaling → memory (+0.20)

**Tier 3 Forces (Interface - fast-changing):**
- Can use WIDER range (0.05-0.35) depending on directness
- More responsive to lifestyle interventions
- Therapeutic practices have strong effects
- Examples: therapy → fear (-0.30), exercise → pain (-0.20)

**Tier 4 Forces (Emergent - situational):**
- Generally use SMALLER modifiers (0.05-0.20)
- Harder to directly influence (emergent from parent forces)
- Lifestyle factors work through parent force activation
- Examples: creative practice → art (+0.15), play → humor (+0.10)

---

### Asymmetry Considerations

**Negative effects often stronger than positive:**
- Sleep deprivation: coherence -0.25 (large negative)
- Good sleep: coherence +0.15 (moderate positive)
- **Reason:** Easier to break down than build up

**Threshold effects:**
- Small lifestyle improvements: small modifiers
- Crossing critical threshold: jump to larger modifier
- Example: meditation 0→10 min = +0.10, 10→30 min = +0.25

**Ceiling effects:**
- Diminishing returns at high levels
- First improvements = larger modifiers
- Later improvements = smaller additional gains
- Example: sleep 5→7 hours (+0.20), sleep 7→9 hours (+0.05)

---

### Common Patterns

**Critical Foundational Factors (use LARGE modifiers):**
- Sleep quality: -0.30 to +0.25
- Sunlight exposure: -0.40 to +0.35
- Meditation practice: +0.35 to +0.40 (high)
- Severe trauma/crisis: -0.45 to -0.60

**Important Regular Factors (use MODERATE modifiers):**
- Exercise frequency: ±0.15 to ±0.25
- Diet quality: ±0.10 to ±0.20
- Social connection: ±0.15 to ±0.25
- Therapy/counseling: ±0.20 to ±0.30

**Supplementary Factors (use SMALL modifiers):**
- Gratitude practice: ±0.08 to ±0.15
- Journaling: ±0.08 to ±0.12
- Nature exposure (supplementary): ±0.10 to ±0.15
- Creative hobbies: ±0.05 to ±0.15

**Minor/Indirect Factors (use MINIMAL modifiers):**
- Room temperature: ±0.03 to ±0.08
- Music listening (casual): ±0.05 to ±0.10
- Meal timing (if adequate food): ±0.03 to ±0.08

---

### Validation Checks

**When reviewing modifiers, verify:**

✅ **Progression makes sense:**
- low → medium → high should show logical progression
- Larger lifestyle factor improvement = larger modifier change
- No bizarre jumps (e.g., low: +0.05, medium: +0.40)

✅ **Relative magnitude makes sense:**
- More important factors have larger modifiers
- More sensitive forces show larger changes
- Foundational factors > supplementary factors

✅ **Ranges are realistic:**
- Total possible modifier from all lifestyle factors shouldn't exceed ±1.0
- Single factor shouldn't dominate (unless genuinely critical)
- Multiple moderate factors can compound to large total effect

✅ **Asymmetry is appropriate:**
- Negative effects often larger than positive (easier to break than build)
- Makes sense given the force and factor relationship

✅ **Matches existing patterns:**
- Compare to similar lifestyle factors already created
- Maintain consistency across files
- Use established ranges as reference

---

### Examples by Scenario

**Scenario 1: Creating "Cold Exposure" (physical_body)**

Force: entropy
- Sensitivity: High (cold stress triggers cellular adaptation)
- Importance: Moderate (beneficial but not critical)
- Effect: Direct (physical stimulus)
- **Decision: MODERATE** → low: +0.10, medium: 0.0, high: -0.20

Force: fear
- Sensitivity: Moderate (cold can trigger fear response)
- Importance: Low for this factor
- Effect: Indirect (psychological response)
- **Decision: SMALL** → low: +0.10, medium: +0.05, high: 0.0

---

**Scenario 2: Creating "Chronic Stress" (mental_spiritual)**

Force: coherence
- Sensitivity: Extreme (stress fragments coherence dramatically)
- Importance: Critical (foundational nervous system state)
- Effect: Direct and immediate
- **Decision: LARGE** → low: +0.15, medium: 0.0, high: -0.40

Force: fear
- Sensitivity: Extreme (stress = chronic fear activation)
- Importance: Critical
- Effect: Direct
- **Decision: LARGE** → low: -0.10, medium: +0.10, high: +0.35

---

**Scenario 3: Creating "Houseplants" (environment_nature)**

Force: entropy
- Sensitivity: Low (plants reduce visual chaos)
- Importance: Minor (aesthetic/mood)
- Effect: Indirect
- **Decision: MINIMAL** → low: +0.03, medium: 0.0, high: -0.05

Force: hope
- Sensitivity: Low (caring for life provides minor uplift)
- Importance: Minor
- Effect: Indirect (symbolic)
- **Decision: SMALL** → low: 0.0, medium: +0.05, high: +0.08

---

### Reference Table

| Magnitude | Range | Typical Use | Force Tiers | Examples |
|-----------|-------|-------------|-------------|----------|
| **MINIMAL** | ±0.01-0.08 | Subtle, indirect effects | All tiers | Room temp, casual music |
| **SMALL** | ±0.08-0.15 | Noticeable, supplementary | T1, T3, T4 | Gratitude, journaling, hobbies |
| **MODERATE** | ±0.15-0.30 | Significant, important | All tiers | Exercise, diet, social connection |
| **LARGE** | ±0.30-0.45 | Major, foundational | T1, T2 | Sleep, meditation, sunlight |
| **EXTREME** | ±0.45+ | Life/death, rare | T1, T3 | Severe trauma, crisis, extremes |

---

### Notes

- These are GUIDELINES, not rigid rules
- Context matters - use judgment
- When in doubt, start conservative (smaller) and adjust based on empirical feedback
- Consult existing similar lifestyle factors for reference
- Document reasoning in the file's notes section

---

## Threshold Interpolation Rules

**Problem:** Lifestyle factor measurements often fall between defined thresholds. How should force modifiers be calculated for in-between values?

**Solution:** Use **linear interpolation** between threshold midpoints to create smooth, continuous modifier curves.

### Why Interpolation Matters

Without interpolation, small changes in behavior can produce unrealistic jumps in force modifiers:
- **Without:** 19 min outdoor time = coherence +0.00, 20 min = coherence +0.08 (sudden jump)
- **With interpolation:** 19 min = +0.00, 19.5 min = +0.04, 20 min = +0.08 (smooth transition)

Interpolation reflects reality: small behavioral changes → small force impacts.

---

### Updated Threshold Format

Each threshold must define:

```yaml
thresholds:
  low:
    range: [0, 20]        # [lower_bound, upper_bound] - lower-inclusive, upper-exclusive
    midpoint: 10          # Representative value for this threshold (used for interpolation)
    description: "Minimal or no time in natural environments"
  medium:
    range: [20, 60]       # 20 ≤ value < 60
    midpoint: 40          # Typical "medium" value
    description: "Moderate outdoor exposure"
  high:
    range: [60, null]     # 60+ with no upper limit
    midpoint: 90          # Representative "high" value
    ceiling: 120          # Optional: max value for interpolation (beyond this, cap at high modifier)
    description: "Significant time in natural settings"
```

**Field Definitions:**
- **range:** Array `[lower, upper]` defining boundaries
  - Lower bound is **inclusive** (≥)
  - Upper bound is **exclusive** (<)
  - Use `null` for open-ended upper bounds (e.g., "60+")
- **midpoint:** Representative value for this threshold level (required for interpolation)
- **ceiling:** (Optional) Maximum value for interpolation in open-ended ranges
- **description:** Human-readable explanation

---

### Boundary Rules

**Standard Convention: Lower-Inclusive, Upper-Exclusive**

- `[0, 20)` means: 0 ≤ value < 20 (includes 0, excludes 20)
- `[20, 60)` means: 20 ≤ value < 60 (includes 20, excludes 60)
- `[60, ∞)` means: 60 ≤ value (includes 60, no upper limit)

**Examples:**
- 0 min → "low" threshold
- 19.9 min → "low" threshold
- 20 min → "medium" threshold (boundary belongs to higher threshold)
- 60 min → "high" threshold

---

### Interpolation Formula

For any measured value between two thresholds, use linear interpolation:

```python
def interpolate_modifier(value, thresholds, force_modifiers):
    """
    Calculate force modifier using linear interpolation between threshold midpoints.

    Args:
        value: Measured value (e.g., 25 min outdoor time)
        thresholds: Dict with 'low', 'medium', 'high' threshold configs
        force_modifiers: Dict with modifier values at each threshold

    Returns:
        Interpolated modifier value (float)

    Example:
        value = 25 min
        Falls between low (midpoint 10) and medium (midpoint 40)
        low_modifier = +0.00, medium_modifier = +0.08

        ratio = (25 - 10) / (40 - 10) = 15/30 = 0.5
        interpolated = 0.00 + (0.08 - 0.00) * 0.5 = +0.04
    """

    # Determine which thresholds value falls between
    if value < thresholds['medium']['range'][0]:
        # Between low and medium
        t1_midpoint = thresholds['low']['midpoint']
        t2_midpoint = thresholds['medium']['midpoint']
        mod1 = force_modifiers['low']
        mod2 = force_modifiers['medium']

    elif value < thresholds['high']['range'][0]:
        # Between medium and high
        t1_midpoint = thresholds['medium']['midpoint']
        t2_midpoint = thresholds['high']['midpoint']
        mod1 = force_modifiers['medium']
        mod2 = force_modifiers['high']

    else:
        # Above high threshold
        if 'ceiling' in thresholds['high'] and value < thresholds['high']['ceiling']:
            # Continue interpolating up to ceiling
            t1_midpoint = thresholds['high']['range'][0]  # Lower bound of high
            t2_midpoint = thresholds['high']['ceiling']
            mod1 = force_modifiers['high']
            mod2 = force_modifiers['high']  # Same modifier (no increase beyond high)
        else:
            # Beyond ceiling or no ceiling defined - cap at high modifier
            return force_modifiers['high']

    # Calculate interpolation ratio
    ratio = (value - t1_midpoint) / (t2_midpoint - t1_midpoint)
    ratio = max(0.0, min(1.0, ratio))  # Clamp to [0, 1]

    # Linear interpolation
    return mod1 + (mod2 - mod1) * ratio
```

---

### Example Calculations

**Factor:** Outdoor Time (from updated example below)

**Thresholds:**
```yaml
low:    [0, 20],   midpoint: 10
medium: [20, 60],  midpoint: 40
high:   [60, null], midpoint: 90, ceiling: 120
```

**Force Impact (Coherence):**
```yaml
coherence:
  low: +0.00    # At 10 min
  medium: +0.08 # At 40 min
  high: +0.15   # At 90 min
```

**Calculations:**

| Measurement | Falls Between | Ratio | Calculation | Result |
|-------------|---------------|-------|-------------|--------|
| 10 min | low midpoint | 0.0 | 0.00 + (0.08 - 0.00) × 0.0 | **+0.00** |
| 15 min | low → medium | 0.167 | 0.00 + (0.08 - 0.00) × 0.167 | **+0.013** |
| 25 min | low → medium | 0.5 | 0.00 + (0.08 - 0.00) × 0.5 | **+0.04** |
| 35 min | low → medium | 0.833 | 0.00 + (0.08 - 0.00) × 0.833 | **+0.067** |
| 40 min | medium midpoint | 0.0 | 0.08 + (0.15 - 0.08) × 0.0 | **+0.08** |
| 65 min | medium → high | 0.5 | 0.08 + (0.15 - 0.08) × 0.5 | **+0.115** |
| 90 min | high midpoint | 1.0 | 0.08 + (0.15 - 0.08) × 1.0 | **+0.15** |
| 150 min | beyond ceiling | — | Cap at high | **+0.15** |

---

### Open-Ended Range Handling

For ranges like "60+ min/day", define a **ceiling** for interpolation purposes:

```yaml
high:
  range: [60, null]      # 60+ with no explicit upper limit
  midpoint: 90           # Represents "typical high" (e.g., 1.5x lower bound)
  ceiling: 120           # Maximum for interpolation (e.g., 2x lower bound)
  description: "Significant time in natural settings"
```

**Behavior:**
- **60-90 min:** Interpolate from medium modifier → high modifier
- **90-120 min:** Already at high modifier (no further increase)
- **120+ min:** Cap at high modifier (diminishing returns beyond ceiling)

**Reasoning:** Most lifestyle factors exhibit diminishing returns - going from 0→60 min has larger impact than 60→120 min. Ceiling prevents unrealistic extrapolation.

---

### Negative Modifier Interpolation

Interpolation works identically for negative modifiers (no special handling needed).

**Example: Processed Food → Coherence**
```yaml
coherence:
  low: +0.00       # 0-20% processed (good)
  medium: -0.08    # 20-50% processed (moderate)
  high: -0.18      # 50%+ processed (bad)
```

**Calculation at 35% processed (between medium and high):**
- Falls between medium (midpoint 35%) and high (midpoint 65%)
- Ratio: (35 - 35) / (65 - 35) = 0.0
- Interpolated: -0.08 + ((-0.18) - (-0.08)) × 0.0 = **-0.08**

**Calculation at 50% processed:**
- Falls between medium (midpoint 35%) and high (midpoint 65%)
- Ratio: (50 - 35) / (65 - 35) = 15/30 = 0.5
- Interpolated: -0.08 + ((-0.18) - (-0.08)) × 0.5 = -0.08 + (-0.10 × 0.5) = **-0.13**

---

### Edge Cases

**Below lowest threshold:**
- Example: -5 min outdoor time (impossible measurement)
- Treat as 0 min → return low threshold modifier

**Exact boundary values:**
- Example: Exactly 20 min (boundary between low and medium)
- Belongs to medium threshold (lower-inclusive rule)
- Apply interpolation normally

**Missing midpoint:**
- If midpoint not defined, calculate as: `(lower + upper) / 2`
- For open-ended ranges, use: `lower * 1.5` as default midpoint

**Missing ceiling:**
- If ceiling not defined for open-ended range, cap at high threshold modifier
- No interpolation beyond high threshold

---

### Implementation Checklist

When creating lifestyle factor mappings with interpolation:

- [ ] All thresholds use array format: `[lower, upper]`
- [ ] All thresholds define `midpoint` values
- [ ] Open-ended ranges include `ceiling` (or document capping behavior)
- [ ] Boundary notation uses lower-inclusive, upper-exclusive convention
- [ ] Force modifiers progress logically (low → medium → high makes sense)
- [ ] Test edge cases: boundaries, extremes, negative values
- [ ] Document any non-standard interpolation behavior in `notes`

---

## Usage Examples

### Example 1: Outdoor Time (Environment/Nature Category)

```yaml
outdoor_time:
  metadata:
    category: "environment_nature"
    measurement_unit: "min/day"
    data_source: "self_report"

  thresholds:
    low:
      range: [0, 20]        # 0 to 19.99... minutes
      midpoint: 10          # Representative "low" value
      description: "Minimal or no time in natural environments"
    medium:
      range: [20, 60]       # 20 to 59.99... minutes
      midpoint: 40          # Representative "medium" value
      description: "Moderate outdoor exposure, some nature contact"
    high:
      range: [60, null]     # 60+ minutes (no upper limit)
      midpoint: 90          # Representative "high" value (1.5x lower bound)
      ceiling: 120          # Max for interpolation (2x lower bound)
      description: "Significant time in natural settings, daily nature immersion"

  force_impacts:
    coherence:
      low: +0.00
      medium: +0.08
      high: +0.15
      reasoning: "Natural environments reduce mental fragmentation, increase present-moment awareness"

    pattern:
      low: -0.05
      medium: +0.05
      high: +0.12
      reasoning: "Nature exposure enhances pattern recognition through fractal geometries and natural rhythms"

    entropy:
      low: +0.08
      medium: +0.02
      high: -0.10
      reasoning: "Lack of nature increases internal chaos; nature exposure provides organizing influence"

    consciousness:
      low: +0.00
      medium: +0.03
      high: +0.06
      reasoning: "Extended nature time can elevate baseline awareness and perceptual capacity"

    fear:
      low: +0.05
      medium: +0.00
      high: -0.08
      reasoning: "Indoor/urban environments maintain threat vigilance; nature reduces survival-mode activation"

  interaction_effects:
    synergistic_with:
      - factor_name: "physical_movement"
        effect: "Outdoor movement amplifies benefits of both factors"
      - factor_name: "meditation"
        effect: "Nature + meditation practice creates enhanced coherence"

  temporal_dynamics:
    immediate_effect: "Stress reduction, nervous system regulation within 20 minutes"
    short_term_effect: "Improved mood, sleep quality within 3-5 days"
    long_term_effect: "Baseline coherence increase, reduced anxiety patterns over 4+ weeks"
    cumulative: true
    decay_rate: "moderate"

  notes: "Effects more pronounced in natural settings (forests, water, mountains) vs urban parks. Morning outdoor time has strongest impact on circadian rhythm and coherence."

  research_support:
    empirical_evidence: "Shinrin-yoku (forest bathing) research shows measurable cortisol reduction, HRV improvement"
    anecdotal_evidence: "Consistent reports of clarity, peace, perspective-shift after nature time"
    lace_framework_basis: "Natural environments exhibit high coherence patterns (fractals, golden ratio, rhythmic cycles) that entrain human state signatures toward greater coherence"
```

### Example 2: Processed Food Consumption (Food/Nutrition Category)

```yaml
processed_food_intake:
  metadata:
    category: "food_nutrition"
    measurement_unit: "% of daily calories"
    data_source: "self_report"

  thresholds:
    low:
      range: [0, 20]        # 0-19.99% of calories
      midpoint: 10          # Representative "low" (10% processed)
      description: "Primarily whole foods, minimal processing"
    medium:
      range: [20, 50]       # 20-49.99% of calories
      midpoint: 35          # Representative "medium" (35% processed)
      description: "Mixed diet with moderate processed food"
    high:
      range: [50, null]     # 50%+ of calories
      midpoint: 65          # Representative "high" (65% processed)
      ceiling: 80           # Max for interpolation (beyond 80%, cap at high modifier)
      description: "Diet dominated by packaged, processed foods"

  force_impacts:
    entropy:
      low: +0.00
      medium: +0.10
      high: +0.20
      reasoning: "Processed foods lack coherent nutritional patterns, increase systemic disorder"

    coherence:
      low: +0.00
      medium: -0.08
      high: -0.18
      reasoning: "Lack of nutritional alignment creates internal fragmentation and inflammation"

    consciousness:
      low: +0.00
      medium: -0.03
      high: -0.08
      reasoning: "Poor nutrition reduces cognitive clarity and perceptual capacity"

    energy:
      low: +0.00
      medium: -0.05
      high: -0.12
      reasoning: "Processed foods create blood sugar instability, reduce sustained energy"

    pattern:
      low: +0.00
      medium: -0.04
      high: -0.10
      reasoning: "Inflammation and nutritional deficiency impair pattern recognition capacity"

  interaction_effects:
    antagonistic_with:
      - factor_name: "whole_foods_intake"
        effect: "High processed + low whole foods = compounded negative effect"
      - factor_name: "physical_movement"
        effect: "Exercise benefits reduced when combined with poor nutrition"

  temporal_dynamics:
    immediate_effect: "Energy fluctuations, blood sugar spikes within 1-3 hours"
    short_term_effect: "Digestive issues, mood impacts within 1-3 days"
    long_term_effect: "Chronic inflammation, reduced baseline coherence over weeks/months"
    cumulative: true
    decay_rate: "slow"

  notes: "Definition of 'processed' includes refined grains, added sugars, artificial ingredients, highly-processed oils. Effects vary by individual sensitivity and overall diet quality."

  research_support:
    empirical_evidence: "Ultra-processed food research shows correlation with inflammation markers, cognitive decline, mood disorders"
    anecdotal_evidence: "Consistent reports of improved mental clarity, emotional stability when reducing processed food"
    lace_framework_basis: "Whole foods carry coherent biological information patterns; processing degrades these patterns into entropic noise"
```

### Example 3: Social Isolation (Social Connections Category)

```yaml
social_isolation:
  metadata:
    category: "social_connections"
    measurement_unit: "meaningful_interactions/week"
    data_source: "self_report"

  thresholds:
    low:
      range: "7+ meaningful interactions/week"
      description: "Regular, quality social connection with inner/outer circles"
    medium:
      range: "3-6 meaningful interactions/week"
      description: "Moderate social engagement"
    high:
      range: "0-2 meaningful interactions/week"
      description: "Isolated, minimal social contact"

  force_impacts:
    fear:
      low: +0.00
      medium: +0.08
      high: +0.18
      reasoning: "Lack of social connection triggers threat detection, survival mode"

    love:
      low: +0.00
      medium: -0.10
      high: -0.22
      reasoning: "Love force requires connection to activate; isolation starves this force"

    hope:
      low: +0.00
      medium: -0.06
      high: -0.15
      reasoning: "Isolation reduces future possibility perception; connection provides hope signals"

    pain:
      low: +0.00
      medium: +0.08
      high: +0.16
      reasoning: "Humans are social beings; isolation creates existential pain"

    coherence:
      low: +0.00
      medium: -0.06
      high: -0.14
      reasoning: "Social feedback provides reality-testing and coherence maintenance"

    consciousness:
      low: +0.00
      medium: -0.02
      high: -0.06
      reasoning: "Sustained isolation can reduce perceptual capacity and awareness"

  interaction_effects:
    synergistic_with:
      - factor_name: "work_stress"
        effect: "Isolation + work stress creates compounded fear/pain activation"
      - factor_name: "media_consumption"
        effect: "Isolation + excessive screen time intensifies disconnection"

  temporal_dynamics:
    immediate_effect: "Loneliness feelings within hours of prolonged isolation"
    short_term_effect: "Mood decline, anxiety increase within days"
    long_term_effect: "Chronic fear/pain patterns, reduced coherence over weeks/months"
    cumulative: true
    decay_rate: "moderate"

  notes: "Quality matters more than quantity. One deep connection > many superficial interactions. Introversion vs isolation are different (introverts can be non-isolated with fewer connections)."

  research_support:
    empirical_evidence: "Loneliness research shows impacts on cortisol, inflammation, mortality risk comparable to smoking"
    anecdotal_evidence: "Consistent reports of depression, anxiety, existential crisis during prolonged isolation"
    lace_framework_basis: "Humans are relational beings; consciousness develops and maintains through connection. Isolation contradicts core design."
```

---

## Implementation Notes

### Calculating Total Force Modification

When a user has multiple lifestyle factors active:

```python
def calculate_total_force_level(base_force_level, lifestyle_factors):
    """
    Apply all relevant lifestyle factor modifiers to a force
    """
    total_modifier = 0.0

    for factor in lifestyle_factors:
        # Get user's level for this factor (low/medium/high)
        user_level = get_user_level(factor)

        # Get modifier for this force at this level
        modifier = factor.force_impacts[force_name][user_level]

        # Add to total
        total_modifier += modifier

    # Apply modifier (capped at 0.0-1.0)
    new_force_level = max(0.0, min(1.0, base_force_level + total_modifier))

    return new_force_level
```

### Handling Synergistic/Antagonistic Effects

```python
def apply_interaction_effects(modifiers, lifestyle_factors):
    """
    Adjust modifiers based on factor interactions
    """
    for factor_a in lifestyle_factors:
        for factor_b in lifestyle_factors:
            if factor_b in factor_a.interaction_effects.synergistic_with:
                # Amplify: multiply by 1.2-1.5
                modifiers[factor_a] *= 1.3

            if factor_b in factor_a.interaction_effects.antagonistic_with:
                # Reduce: multiply by 0.5-0.8
                modifiers[factor_a] *= 0.7

    return modifiers
```

---

## Validation Checklist

When creating a lifestyle factor mapping, verify:

- [ ] All thresholds use array format: `[lower, upper]`
- [ ] All thresholds define `midpoint` values
- [ ] Open-ended ranges (`[X, null]`) include `ceiling` or document capping behavior
- [ ] Threshold boundaries use lower-inclusive, upper-exclusive convention
- [ ] Threshold ranges don't overlap or have gaps
- [ ] Modifiers are reasonable (typically ±0.01 to ±0.45, see Modifier Magnitude Decision Tree section above)
- [ ] Force modifiers progress logically (low → medium → high makes sense)
- [ ] At least 3-8 forces are affected
- [ ] Reasoning is provided for each force impact
- [ ] Temporal dynamics make sense for the factor
- [ ] Notes explain any special considerations or non-standard interpolation
- [ ] Measurement unit is clear and practical

---

**Last Updated:** November 22, 2025
**Status:** Schema complete with threshold interpolation rules, ready for lifestyle factor mapping creation
