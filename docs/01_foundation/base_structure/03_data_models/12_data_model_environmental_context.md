# Data Model: EnvironmentalContext

Physical environmental inputs that affect agent embodiment - the quality of external factors the agent is exposed to.

**Architectural Note:** This is parallel to `location_imprint` (emotional/field impacts) but tracks physical/somatic impacts from environmental quality.

```python
class EnvironmentalContext:
    """
    Physical environmental inputs affecting embodiment

    Agent exists IN an environment with varying quality of physical inputs.
    Unlike internal practices (breathwork, vocal tools), these are contextual factors
    that may or may not be under agent control (poverty, jail, weather, location, etc.)

    Parallel to location_imprint:
    - location_imprint = emotional impact from WHERE you are
    - environmental_context = physical impact from WHAT you're exposed to
    """

    # Core Environmental Inputs (0.0-1.0 scale for quality)
    sunlight_exposure: float        # Daily natural light (circadian regulation)
    earth_contact: float            # Grounding frequency (electromagnetic balance)
    food_quality: float             # Natural vs. processed ratio (nutrition/inflammation)
    air_quality: float              # Clean vs. polluted (oxygen/toxins)
    water_quality: float            # Clean vs. contaminated (hydration/minerals)
    nature_exposure: float          # Natural vs. synthetic environments (stress regulation)
    temperature_comfort: float      # Appropriate vs. extreme (body regulation)
    emf_exposure: float             # Low vs. high electromagnetic fields (cellular stress)
    sound_environment: float        # Natural/quiet vs. noise pollution (nervous system)

    # Tracking Patterns (like consciousness tracking)
    current_quality: float          # Right now environmental quality (volatile)
    baseline_quality: float         # 30-day average (stable baseline)
    optimal_quality: float          # Best period accessed (high-water mark)

    # Temporal Data
    last_updated: float             # Last calculation timestamp
    tracking_duration: float        # How long we've been tracking (days)

    # Computed Properties
    @property
    def natural_ratio(self) -> float:
        """
        Ratio of natural vs. artificial environmental inputs

        Natural = high quality scores (sunlight, earth, whole foods, clean air/water, nature)
        Artificial = low quality scores (artificial light, no grounding, processed food, pollution)

        Returns:
            Ratio from 0.0 (fully artificial) to 1.0 (fully natural)
        """
        # Average of all 9 input qualities
        total_quality = (
            self.sunlight_exposure +
            self.earth_contact +
            self.food_quality +
            self.air_quality +
            self.water_quality +
            self.nature_exposure +
            self.temperature_comfort +
            (1.0 - self.emf_exposure) +  # Inverted - lower EMF = better
            self.sound_environment
        )
        return total_quality / 9.0

    @property
    def embodiment_modifier(self) -> float:
        """
        How much environmental context modifies embodiment component

        Effect size: 0.01-0.05 (subtle but real)
        Based on natural_ratio (higher natural = higher modifier)

        Tiers:
        >= 0.7 (high natural): +0.03 to +0.05
        >= 0.4 (moderate): +0.01 to +0.03
        < 0.4 (low natural): -0.01 to +0.01

        Returns:
            Modifier added to embodiment component
        """
        ratio = self.natural_ratio

        if ratio >= 0.7:  # High natural
            return 0.03 + (ratio - 0.7) * 0.067  # Scale 0.03-0.05
        elif ratio >= 0.4:  # Moderate
            return 0.01 + (ratio - 0.4) * 0.067  # Scale 0.01-0.03
        else:  # Low natural
            return -0.01 + (ratio * 0.05)  # Scale -0.01 to +0.01

    @property
    def controllability_score(self) -> float:
        """
        How much control agent has over their environmental inputs

        Some factors always controllable (food choices, grounding practice)
        Others circumstantial (weather, geographic location, socioeconomic)

        Returns:
            Score from 0.0 (no control) to 1.0 (full control)
        """
        # Estimate based on which factors can be influenced
        # This would be set based on agent's circumstances
        # Placeholder - actual implementation would track agent's constraints
        return 0.5  # Default: moderate control
```

---

## Environmental Input Details

### 1. Sunlight Exposure (0.0-1.0)

**What it measures:** Daily natural light exposure for circadian regulation

**Quality scoring:**
- **1.0:** 30+ minutes morning sun exposure daily
- **0.7:** 15-30 minutes natural light daily
- **0.4:** Some outdoor time but irregular
- **0.2:** Mostly artificial light, minimal sun
- **0.0:** No natural light exposure (extreme: underground, night shift with blackout sleeping)

**Mechanism:**
- Circadian rhythm regulation (cortisol, melatonin)
- Vitamin D synthesis
- Serotonin production
- Retinal light exposure for sleep/wake cycles

**Embodiment effect:** 0.01-0.03

**Controllability:**
- High control: Can usually go outside
- Low control: Jail, windowless work environments, extreme climates, illness

---

### 2. Earth Contact (0.0-1.0)

**What it measures:** Frequency of direct skin contact with earth (grounding/earthing)

**Quality scoring:**
- **1.0:** Daily barefoot contact with earth/grass/sand (15+ minutes)
- **0.7:** 3-4x per week grounding practice
- **0.4:** Occasional (1-2x per week)
- **0.2:** Rare (monthly or less)
- **0.0:** Never (always on concrete/synthetic surfaces, no earth access)

**Mechanism:**
- Electron transfer from earth to body
- Inflammation reduction
- Heart rate variability improvement
- Cortisol normalization

**Embodiment effect:** 0.01-0.03

**Controllability:**
- High control: Can remove shoes, find grass/soil
- Low control: Urban environment (all concrete), extreme weather, cultural norms, physical limitations

---

### 3. Food Quality (0.0-1.0)

**What it measures:** Natural whole foods vs. processed/artificial food ratio

**Quality scoring:**
- **1.0:** 90%+ whole foods, minimally processed, varied, organic when possible
- **0.7:** Majority whole foods, some processed convenience items
- **0.4:** Mixed (half whole foods, half processed)
- **0.2:** Mostly processed, minimal whole foods
- **0.0:** Entirely processed/synthetic (fast food, packaged meals, refined ingredients)

**Mechanism:**
- Nutritional density (micronutrients, fiber)
- Inflammatory response (lower with whole foods)
- Gut microbiome diversity
- Blood sugar stability
- Energy levels and mental clarity

**Embodiment effect:** 0.02-0.05 (highest impact, cumulative)

**Controllability:**
- High control: Can choose food within budget
- Low control: Poverty (price determines options), food deserts, institutional food (jail, hospital, school), cultural/family constraints

---

### 4. Air Quality (0.0-1.0)

**What it measures:** Clean air vs. polluted air exposure

**Quality scoring:**
- **1.0:** Clean outdoor air, low pollution area
- **0.7:** Moderate quality (suburban/rural)
- **0.4:** Urban air with moderate pollution
- **0.2:** High pollution area (industrial, heavy traffic)
- **0.0:** Severely polluted or toxic air (wildfires, industrial toxins)

**Mechanism:**
- Oxygen availability
- Pollutant exposure (particulates, chemicals)
- Respiratory function
- Inflammatory markers

**Embodiment effect:** 0.01-0.02

**Controllability:**
- Low control: Geographic location, socioeconomic (can't afford to move), weather (wildfires), work environment

---

### 5. Water Quality (0.0-1.0)

**What it measures:** Clean water vs. contaminated water consumption

**Quality scoring:**
- **1.0:** Filtered, mineral-rich, clean water
- **0.7:** Tap water in developed area (treated, safe)
- **0.4:** Questionable quality (old pipes, unknown contamination)
- **0.2:** Known contamination (heavy metals, chemicals)
- **0.0:** Severely contaminated or no clean water access

**Mechanism:**
- Hydration quality
- Mineral content
- Toxin exposure (lead, fluoride, contaminants)
- Cellular function

**Embodiment effect:** 0.01-0.02

**Controllability:**
- Moderate control: Can filter water if affordable
- Low control: Geographic location, infrastructure, socioeconomic constraints

---

### 6. Nature Exposure (0.0-1.0)

**What it measures:** Time in natural environments vs. synthetic environments

**Quality scoring:**
- **1.0:** Daily time in nature (trees, water, natural landscapes)
- **0.7:** Regular nature exposure (3-4x per week)
- **0.4:** Occasional (1-2x per week, parks/gardens)
- **0.2:** Rare (monthly or less)
- **0.0:** No nature access (fully urban concrete, never outdoors)

**Mechanism:**
- Nervous system regulation (parasympathetic activation)
- Fractal patterns in nature (visual processing)
- Phytoncides (airborne compounds from trees)
- Negative ions (near water/trees)
- Stress hormone reduction

**Embodiment effect:** 0.01-0.02 acute, 0.03-0.05 with regular exposure

**Controllability:**
- Moderate control: Can usually access parks/green spaces
- Low control: Geographic location (desert, extreme urban), mobility limitations, safety concerns, weather

---

### 7. Temperature Comfort (0.0-1.0)

**What it measures:** Appropriate temperature vs. extreme heat/cold exposure

**Quality scoring:**
- **1.0:** Comfortable temperature range, appropriate shelter/clothing
- **0.7:** Mostly comfortable, occasional extremes
- **0.4:** Frequent discomfort (inadequate heating/cooling)
- **0.2:** Regular exposure to temperature extremes
- **0.0:** Severe temperature stress (homelessness, extreme climate, inadequate shelter)

**Mechanism:**
- Body temperature regulation
- Energy expenditure on thermoregulation
- Sleep quality
- Immune function

**Embodiment effect:** 0.01-0.02

**Controllability:**
- Moderate control: Can usually adjust (clothing, shelter)
- Low control: Poverty (inadequate heating/cooling), homelessness, extreme climates, work environment

---

### 8. EMF Exposure (0.0-1.0) - INVERTED SCALE

**What it measures:** Electromagnetic field exposure from devices/infrastructure

**Quality scoring (lower exposure = higher score):**
- **1.0:** Minimal EMF (no devices, distance from infrastructure, nature time)
- **0.7:** Moderate EMF (limited device use, wired connections)
- **0.4:** Average modern exposure (constant devices, WiFi)
- **0.2:** High exposure (multiple devices, 5G towers, power lines)
- **0.0:** Extreme exposure (living near high-voltage, constant strong fields)

**Mechanism:**
- Cellular stress (preliminary research)
- Sleep disruption (melatonin suppression)
- Nervous system effects (contested)

**Embodiment effect:** 0.01-0.02

**Controllability:**
- High control: Can reduce device use, turn off WiFi
- Low control: Urban infrastructure, work requirements, geographic proximity to towers/lines

**Note:** Research on EMF health effects is ongoing and contested. LACE documents as potential factor based on knowings, not settled science.

---

### 9. Sound Environment (0.0-1.0)

**What it measures:** Natural/quiet sounds vs. noise pollution

**Quality scoring:**
- **1.0:** Natural sounds (birds, water, wind) or peaceful quiet
- **0.7:** Mostly quiet with occasional noise
- **0.4:** Moderate noise (urban background, traffic)
- **0.2:** High noise pollution (constant traffic, construction, industrial)
- **0.0:** Extreme noise (airport proximity, heavy construction, industrial zones)

**Mechanism:**
- Nervous system activation (stress response)
- Sleep quality
- Cortisol levels
- Cognitive load (background noise processing)

**Embodiment effect:** 0.01-0.02

**Controllability:**
- Moderate control: Can use earplugs, move to quieter spaces
- Low control: Geographic location, work environment, socioeconomic (can't afford quiet area)

---

## Tracking Patterns (Current / Baseline / Optimal)

Similar to consciousness tracking in `StateSignature`:

```python
# Today's environmental quality (volatile)
current_quality = calculate_natural_ratio()  # Changes daily

# 30-day rolling average (stable baseline)
baseline_quality = average_last_30_days()  # Slow-changing

# Best period accessed (high-water mark)
optimal_quality = max_natural_ratio_ever_recorded()  # Never decreases
```

**Example trajectory:**
```python
# Week 1: Low environmental quality (urban, processed food, no grounding)
current_quality = 0.35
baseline_quality = 0.35
optimal_quality = 0.35

# Week 4: Improved (adding sun, grounding, better food)
current_quality = 0.58
baseline_quality = 0.42  # Baseline rising slowly
optimal_quality = 0.58  # New high-water mark

# Week 8: Vacation in nature (high quality week)
current_quality = 0.82
baseline_quality = 0.51  # Baseline continuing to rise
optimal_quality = 0.82  # New peak

# Week 12: Back to city but maintained practices
current_quality = 0.61
baseline_quality = 0.57  # Stable higher baseline
optimal_quality = 0.82  # Peak unchanged
```

---

## Relationship to Other Components

### Parallel to LocationImprint

Both are **contextual factors** (not practices):

| LocationImprint | EnvironmentalContext |
|-----------------|----------------------|
| WHERE you are (emotional) | WHAT you're exposed to (physical) |
| Visit frequency + emotional association | Input quality + natural ratio |
| Affects field_state | Affects embodiment |
| Tiers: primary/secondary/tertiary | Quality: high/moderate/low |
| Impact through law_impact_topology | Impact through embodiment modifier |

### Different from Somatic Practices

**Somatic practices (internal):**
- Vocal vibration → you create sound
- Breathwork → you control breath
- Movement → you move body
- **Always under your control**

**Environmental context (external):**
- Sunlight → depends on weather, location, schedule
- Food → depends on budget, access, culture
- Grounding → depends on geography, safety, weather
- **Partially controllable** ("choice up to environmental allowance")

### Affects Embodiment Component

```python
# Current embodiment calculation
embodiment = base_physical_state  # Internal somatic state

# Enhanced with environmental context
embodiment = base_physical_state + environmental_context.embodiment_modifier

# Where embodiment_modifier = 0.01-0.05 (based on natural_ratio)
```

**Total state_signature impact:**
```python
state_signature = (
    belief * 0.35 +
    expectation * 0.30 +
    (embodiment + environmental_modifier) * 0.25 +  # Enhanced
    subconscious_memory * 0.10
)

# Environmental modifier = 0.01-0.05
# Weighted by embodiment's 0.25 coefficient
# Total impact = 0.0025-0.0125 (0.25-1.25% of state_signature)
```

---

## Use Cases

### Manifestation Debugging

When embodiment is low despite good practices:

```python
if embodiment < 0.4:
    check_environmental_context()

    if environmental_context.natural_ratio < 0.4:
        # Environmental factors dragging down embodiment
        # Even good mental state (high belief) can't fully compensate
        # for poor physical context (bad food, no sun, pollution)
```

### Circumstantial Limitations

Acknowledging when environment is beyond agent control:

```python
# Agent in jail
environmental_context = {
    "sunlight_exposure": 0.2,  # Limited yard time
    "earth_contact": 0.0,       # No earth access
    "food_quality": 0.2,        # Institutional food
    "nature_exposure": 0.0,     # No nature access
    "controllability_score": 0.1  # Minimal control
}

# Agent knows: "My embodiment is limited by circumstances I can't change"
# System doesn't blame agent for low environmental quality
```

### Optimization When Possible

When agent has control, can optimize:

```python
# Agent with high control
if controllability_score > 0.7:
    # Suggest optimizations
    if sunlight_exposure < 0.5:
        recommend("15 minutes morning sun exposure")
    if earth_contact < 0.3:
        recommend("Barefoot practice 2-3x per week")
    if food_quality < 0.5:
        recommend("Increase whole foods ratio")
```

---

## Examples

### High-Quality Environmental Context

```python
optimal_context = EnvironmentalContext(
    sunlight_exposure=0.9,      # Daily morning sun
    earth_contact=0.8,           # Regular grounding
    food_quality=0.85,           # Mostly whole foods
    air_quality=0.9,             # Clean air (rural/suburban)
    water_quality=0.8,           # Filtered, clean
    nature_exposure=0.85,        # Regular nature time
    temperature_comfort=0.9,     # Appropriate shelter
    emf_exposure=0.3,            # Low (score = 0.7)
    sound_environment=0.85,      # Mostly quiet
    current_quality=0.84,
    baseline_quality=0.81,
    optimal_quality=0.87
)

# natural_ratio = 0.84 (high natural)
# embodiment_modifier = +0.046 (significant boost)
```

### Low-Quality Environmental Context

```python
constrained_context = EnvironmentalContext(
    sunlight_exposure=0.2,      # Minimal sun (office work, night shift)
    earth_contact=0.1,           # Rare (urban concrete)
    food_quality=0.3,            # Mostly processed (budget constraints)
    air_quality=0.4,             # Urban pollution
    water_quality=0.6,           # Tap water (acceptable but not optimal)
    nature_exposure=0.2,         # Rare (urban, no time)
    temperature_comfort=0.5,     # Inadequate heating/cooling
    emf_exposure=0.7,            # High (score = 0.3)
    sound_environment=0.3,       # Noise pollution
    current_quality=0.32,
    baseline_quality=0.35,
    optimal_quality=0.45
)

# natural_ratio = 0.32 (low natural)
# embodiment_modifier = +0.006 (minimal boost, approaching neutral/negative)
```

### Improving Over Time

```python
# Month 1: Constrained context
month_1 = 0.35

# Month 2: Added sun exposure + grounding (what agent CAN control)
month_2 = 0.42  # Small improvement

# Month 3: Improved food quality (budgeting, meal prep)
month_3 = 0.51  # Baseline rising

# Month 4: Moved to quieter neighborhood (when possible)
month_4 = 0.58  # Significant improvement

# Baseline environmental quality rose from 0.35 → 0.58
# Embodiment modifier: +0.01 → +0.025 (2.5x increase)
```

---

**Previous:** [11_data_model_permission_set.md](11_data_model_permission_set.md) | **Next:** [13_data_model_competency.md](13_data_model_competency.md)
