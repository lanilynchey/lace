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
      range: "X-Y units"
      description: "What 'low' means for this factor"
    medium:
      range: "X-Y units"
      description: "What 'medium' means for this factor"
    high:
      range: "X+ units"
      description: "What 'high' means for this factor"

  # Optional: very_low and very_high thresholds for factors with wide ranges
  # very_low:
  #   range: "X-Y units"
  #   description: "Extreme low"
  # very_high:
  #   range: "X+ units"
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
- Use ranges that make sense for the measurement unit
- Include descriptions that help users understand the levels
- Can add "very_low" and "very_high" for factors with extreme ranges

### Force Impacts
List all forces affected by this lifestyle factor with modifier values.

**Modifier Guidelines:**
- **Small impact:** ±0.01 to ±0.05
- **Moderate impact:** ±0.06 to ±0.15
- **Large impact:** ±0.16 to ±0.30
- **Extreme impact:** ±0.31+

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
      range: "0-20 min/day"
      description: "Minimal or no time in natural environments"
    medium:
      range: "20-60 min/day"
      description: "Moderate outdoor exposure, some nature contact"
    high:
      range: "60+ min/day"
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
      range: "0-20% of calories"
      description: "Primarily whole foods, minimal processing"
    medium:
      range: "20-50% of calories"
      description: "Mixed diet with moderate processed food"
    high:
      range: "50%+ of calories"
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

- [ ] All thresholds are clearly defined with ranges
- [ ] Modifiers are reasonable (typically ±0.01 to ±0.30)
- [ ] At least 3-8 forces are affected
- [ ] Reasoning is provided for each force impact
- [ ] Temporal dynamics make sense for the factor
- [ ] Notes explain any special considerations
- [ ] Measurement unit is clear and practical
- [ ] Threshold ranges don't overlap or have gaps

---

**Last Updated:** November 21, 2025
**Status:** Schema complete, ready for lifestyle factor mapping creation
