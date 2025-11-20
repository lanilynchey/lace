# Data Model: Competency

Domain-specific mastery tracking - how skilled an agent is at particular activities, from fundamental capacities (thinking, breathing) to specialized skills (piano, mathematics).

**Architectural Note:** This is orthogonal to consciousness (global awareness). An agent can have high consciousness (0.8) with low mastery in piano (0.3), or low consciousness (0.3) with high mastery in running (0.9). They are independent dimensions.

```python
class Competency:
    """
    Domain-specific mastery level

    Tracks skill/expertise in a particular domain, from novice (0.0) to master (1.0).
    Everything has mastery levels - not just skills (piano, running) but also
    fundamental capacities (thinking, breathing, deciding, speaking).

    Key insight: Just because you CAN do something ≠ you're GOOD at it.
    Most people are unconsciously incompetent (0.2-0.4) at fundamental capacities.
    """

    # Identity
    domain: str                     # What is being mastered ("piano", "thinking", "running")
    category: str                   # "skill", "fundamental_capacity", "knowledge", "art", "sport"

    # Mastery Level
    mastery_level: float            # Current mastery (0.0-1.0 scale)
    baseline: float                 # Starting point (affected by perceptual_boundary)
    peak_mastery: float             # Highest level achieved (high-water mark)

    # Progression Tracking
    hours_practiced: float          # Total deliberate practice time
    last_engagement: float          # Timestamp of last practice/use
    first_started: float            # When domain was first attempted
    progression_history: List[Tuple[float, float]]  # [(timestamp, mastery_level)]

    # Development Factors (0.0-1.0 each)
    deliberate_practice_quality: float      # Quality of practice (not just time)
    thought_focus_level: float              # Sustained attention on improvement
    emotion_overcome_score: float           # Persistence through frustration
    feedback_integration: float             # Learning from mistakes
    pattern_recognition_ability: float      # Understanding domain structure

    # Context
    related_competencies: List[str]         # Other domains that transfer knowledge
    transfer_coefficient: float             # How much prior experience helped (0.1-1.0)

    # Computed Properties
    @property
    def mastery_stage(self) -> str:
        """
        Four classical stages of competency

        Returns stage name based on mastery_level:
        - Unconscious Incompetence (0.0-0.25)
        - Conscious Incompetence (0.25-0.45)
        - Conscious Competence (0.45-0.70)
        - Unconscious Competence (0.70-1.0)
        """
        if self.mastery_level < 0.25:
            return "unconscious_incompetence"  # Don't know that I don't know
        elif self.mastery_level < 0.45:
            return "conscious_incompetence"    # Know that I don't know
        elif self.mastery_level < 0.70:
            return "conscious_competence"      # Know that I know (requires effort)
        else:
            return "unconscious_competence"    # Don't know that I know (automatic)

    @property
    def mastery_descriptor(self) -> str:
        """Human-readable mastery level description"""
        if self.mastery_level < 0.1:
            return "never_attempted"
        elif self.mastery_level < 0.25:
            return "absolute_beginner"
        elif self.mastery_level < 0.35:
            return "novice"
        elif self.mastery_level < 0.45:
            return "beginner"
        elif self.mastery_level < 0.55:
            return "intermediate"
        elif self.mastery_level < 0.65:
            return "competent"
        elif self.mastery_level < 0.75:
            return "advanced"
        elif self.mastery_level < 0.85:
            return "expert"
        elif self.mastery_level < 0.95:
            return "master"
        else:
            return "virtuoso"

    @property
    def state_elevation_potential(self) -> float:
        """
        How much this mastery elevates consciousness when engaged

        High mastery (0.7+) provides temporary consciousness boost
        when agent is actively engaged in the domain.

        Returns:
            Boost to effective_consciousness (0.0-0.2)
        """
        if self.mastery_level >= 0.9:
            return 0.15 + (self.mastery_level - 0.9) * 0.5  # 0.15-0.20
        elif self.mastery_level >= 0.7:
            return 0.08 + (self.mastery_level - 0.7) * 0.35  # 0.08-0.15
        elif self.mastery_level >= 0.5:
            return 0.03 + (self.mastery_level - 0.5) * 0.25  # 0.03-0.08
        else:
            return 0.0  # No elevation below intermediate

    @property
    def is_stagnant(self) -> bool:
        """True if no improvement in last 6 months"""
        if not self.progression_history:
            return False

        six_months_ago = current_time() - (6 * 30 * 24 * 60 * 60)
        recent_history = [m for (t, m) in self.progression_history if t > six_months_ago]

        if not recent_history:
            return True  # No practice = stagnant

        return max(recent_history) - min(recent_history) < 0.02  # Less than 2% improvement

    @property
    def decay_rate(self) -> float:
        """
        How fast mastery decays without practice

        Motor skills decay slower, knowledge decays faster
        Higher mastery decays slower (well-ingrained patterns)
        """
        # Base decay depends on category
        category_decay = {
            "fundamental_capacity": 0.001,  # Very slow (breathing, thinking - hard to forget)
            "motor_skill": 0.005,            # Slow (riding bike, swimming)
            "knowledge": 0.015,              # Medium (facts, formulas)
            "skill": 0.01,                   # Medium (piano, cooking)
            "art": 0.008,                    # Medium-slow (drawing, music)
            "sport": 0.007                   # Medium-slow (muscle memory)
        }.get(self.category, 0.01)

        # Higher mastery = slower decay (deeply ingrained)
        mastery_factor = 1.0 - (self.mastery_level * 0.5)

        return category_decay * mastery_factor


def calculate_baseline_mastery(agent: Agent, new_domain: str, domain_category: str) -> float:
    """
    Calculate starting mastery level for new domain based on perceptual boundary

    Perceptual boundary (prior experience) affects where you start.
    Transfer learning: related domains provide baseline above zero.

    Args:
        agent: Agent attempting new domain
        new_domain: Domain being learned
        domain_category: Category of domain

    Returns:
        Baseline mastery level (0.1-0.6 depending on transfer)

    Examples:
        - Olympic runner trying cycling: baseline 0.45-0.55
        - Concert pianist trying guitar: baseline 0.35-0.45
        - Child trying piano (no experience): baseline 0.10-0.15
        - Mathematician trying programming: baseline 0.45-0.55
    """
    # Find related competencies in agent's existing mastery
    related_competencies = find_related_domains(agent, new_domain, domain_category)

    if not related_competencies:
        # No related experience - complete novice
        return 0.10 + (random.random() * 0.05)  # 0.10-0.15

    # Calculate transfer coefficient based on similarity
    similarity_scores = []
    for related_domain in related_competencies:
        similarity = calculate_domain_similarity(related_domain, new_domain)
        mastery = agent.competencies[related_domain].mastery_level
        similarity_scores.append((similarity, mastery))

    # Apply transfer coefficients
    total_transfer = 0.0
    for similarity, mastery in similarity_scores:
        if similarity >= 0.8:  # Very similar (piano → keyboard)
            transfer_coefficient = 0.70
        elif similarity >= 0.6:  # Moderately similar (running → swimming)
            transfer_coefficient = 0.40
        elif similarity >= 0.3:  # Loosely similar (any sport → new sport)
            transfer_coefficient = 0.20
        else:  # Barely related
            transfer_coefficient = 0.10

        total_transfer += mastery * transfer_coefficient

    # Average and normalize
    baseline = total_transfer / len(similarity_scores)

    # Cap baseline at 0.6 (can't start as expert)
    return min(0.60, max(0.10, baseline))


def find_related_domains(agent: Agent, new_domain: str, category: str) -> List[str]:
    """
    Find existing competencies related to new domain

    Examples:
        new_domain="cycling", category="sport" → ["running", "swimming"]
        new_domain="guitar", category="music" → ["piano", "music_theory"]
        new_domain="programming", category="knowledge" → ["mathematics", "logical_thinking"]
    """
    related = []

    for domain, competency in agent.competencies.items():
        # Check category match
        if competency.category == category:
            related.append(domain)
            continue

        # Check semantic similarity (would need domain ontology)
        # Placeholder for domain similarity calculation
        if domains_are_related(domain, new_domain):
            related.append(domain)

    return related


def calculate_domain_similarity(domain_a: str, domain_b: str) -> float:
    """
    Calculate semantic similarity between two domains (0.0-1.0)

    Examples:
        piano, keyboard → 0.9 (very similar)
        piano, guitar → 0.6 (same category, different execution)
        running, swimming → 0.5 (both cardio, different movement)
        running, cycling → 0.7 (very similar movement patterns)
        piano, mathematics → 0.2 (both require practice, but unrelated)
        cooking, chemistry → 0.4 (overlapping knowledge)
    """
    # This would use domain ontology in actual implementation
    # Placeholder returning similarity score
    similarity_map = {
        ("piano", "keyboard"): 0.9,
        ("piano", "guitar"): 0.6,
        ("piano", "violin"): 0.5,
        ("running", "swimming"): 0.5,
        ("running", "cycling"): 0.7,
        ("mathematics", "programming"): 0.7,
        ("mathematics", "physics"): 0.8,
        ("cooking", "chemistry"): 0.4,
        # ... extensive mapping
    }

    return similarity_map.get((domain_a, domain_b), 0.1)


def develop_mastery(competency: Competency, practice_session: Dict) -> float:
    """
    Update mastery based on practice session

    Mastery progression requires intentional development:
    - Deliberate practice (40%)
    - Thought focus (25%)
    - Overcoming emotion (20%)
    - Feedback integration (10%)
    - Pattern recognition (5%)

    Args:
        competency: Current competency
        practice_session: {
            "duration": hours,
            "quality": 0.0-1.0,
            "focus_level": 0.0-1.0,
            "frustration_overcome": 0.0-1.0,
            "mistakes_corrected": int,
            "new_patterns_learned": int
        }

    Returns:
        New mastery level
    """
    # Extract session data
    duration = practice_session["duration"]
    quality = practice_session["quality"]
    focus = practice_session["focus_level"]
    emotion = practice_session["frustration_overcome"]
    feedback = min(1.0, practice_session["mistakes_corrected"] / 10.0)
    patterns = min(1.0, practice_session["new_patterns_learned"] / 5.0)

    # Calculate mastery gain
    mastery_gain = (
        (duration * quality) * 0.40 +      # Deliberate practice
        focus * 0.25 +                      # Thought focus
        emotion * 0.20 +                    # Overcoming emotion
        feedback * 0.10 +                   # Feedback integration
        patterns * 0.05                     # Pattern recognition
    )

    # Scale by current level (harder to improve at high mastery)
    difficulty_multiplier = 1.0 - (competency.mastery_level * 0.5)
    mastery_gain *= difficulty_multiplier

    # Apply gain
    new_mastery = competency.mastery_level + (mastery_gain * 0.001)  # Small incremental gain

    # Update tracking
    competency.mastery_level = min(1.0, new_mastery)
    competency.peak_mastery = max(competency.peak_mastery, new_mastery)
    competency.hours_practiced += duration
    competency.last_engagement = current_time()
    competency.progression_history.append((current_time(), new_mastery))

    # Update development factors
    competency.deliberate_practice_quality = (competency.deliberate_practice_quality * 0.9) + (quality * 0.1)
    competency.thought_focus_level = (competency.thought_focus_level * 0.9) + (focus * 0.1)
    competency.emotion_overcome_score = (competency.emotion_overcome_score * 0.9) + (emotion * 0.1)
    competency.feedback_integration = (competency.feedback_integration * 0.9) + (feedback * 0.1)
    competency.pattern_recognition_ability = (competency.pattern_recognition_ability * 0.9) + (patterns * 0.1)

    return new_mastery


def apply_mastery_decay(competency: Competency, time_delta: float):
    """
    Reduce mastery when not practiced

    Decay rate depends on:
    - Domain category (motor skills decay slower)
    - Current mastery level (higher mastery more resistant)
    - Time since last practice

    Args:
        competency: Competency to apply decay
        time_delta: Time since last check (seconds)
    """
    time_since_practice = current_time() - competency.last_engagement
    decay_rate = competency.decay_rate

    # Only decay if no practice for > 1 week
    if time_since_practice < (7 * 24 * 60 * 60):
        return

    # Calculate decay
    decay_amount = decay_rate * (time_since_practice / (30 * 24 * 60 * 60))  # Per month

    # Apply decay (never goes below baseline)
    competency.mastery_level = max(
        competency.baseline,
        competency.mastery_level - decay_amount
    )
```

---

## Mastery Scale (0.0-1.0 Continuous)

**Named levels every ~0.1:**

| Range | Descriptor | Stage | Characteristics |
|-------|------------|-------|-----------------|
| 0.00-0.10 | Never Attempted | Unconscious Incompetence | No awareness of domain |
| 0.10-0.25 | Absolute Beginner | Unconscious Incompetence | Aware it exists, tried once |
| 0.25-0.35 | Novice | Conscious Incompetence | Knows they're bad, practicing basics |
| 0.35-0.45 | Beginner | Conscious Incompetence | Struggling but improving |
| 0.45-0.55 | Intermediate | Conscious Competence | Can perform with focus |
| 0.55-0.65 | Competent | Conscious Competence | Performs well with effort |
| 0.65-0.75 | Advanced | Conscious Competence → Unconscious | Approaching automaticity |
| 0.75-0.85 | Expert | Unconscious Competence | Automatic, effortless execution |
| 0.85-0.95 | Master | Unconscious Competence | Creates new patterns in domain |
| 0.95-1.00 | Virtuoso | Transcendent Mastery | Redefines what's possible |

**Four Classical Stages:**

1. **Unconscious Incompetence (0.0-0.25)**
   - "I don't know that I don't know"
   - No awareness of skill gap
   - Example: Child who's never seen a piano

2. **Conscious Incompetence (0.25-0.45)**
   - "I know that I don't know"
   - Aware of mistakes, struggling
   - **Emotionally hardest stage** (frustration, self-doubt)
   - Example: Week 1-3 of piano lessons

3. **Conscious Competence (0.45-0.70)**
   - "I know that I know (but requires effort)"
   - Can perform with concentration
   - **Most people plateau here** (adequate performance, never master)
   - Example: Playing piano with sheet music, focused practice

4. **Unconscious Competence (0.70-1.0)**
   - "I don't know that I know (it's automatic)"
   - Effortless execution, flow state accessible
   - **State elevation occurs here** (temporary consciousness boost)
   - Example: Concert pianist improvising, muscle memory

---

## State Elevation Mechanic

When agent engages in domain where they have mastery (0.7+), their **effective consciousness temporarily increases**.

```python
def calculate_effective_consciousness(agent: Agent, current_domain: Optional[str]) -> float:
    """
    Calculate agent's effective consciousness in current context

    Base consciousness is global awareness level.
    When engaged in mastery domain, gets temporary boost.

    Args:
        agent: Agent
        current_domain: What they're currently doing (None if idle)

    Returns:
        Effective consciousness (may be higher than base)

    Examples:
        - Agent with consciousness 0.50 playing piano (mastery 0.85)
          → effective 0.50 + 0.12 = 0.62 (Reason level)

        - Olympian with consciousness 0.50 running (mastery 0.92)
          → effective 0.50 + 0.16 = 0.66 (approaching Love/flow state)

        - Agent with consciousness 0.50 doing random task (no mastery)
          → effective 0.50 (no boost)
    """
    base_consciousness = agent.consciousness_coefficient

    if not current_domain:
        return base_consciousness  # Not engaged in specific domain

    competency = agent.competencies.get(current_domain)
    if not competency:
        return base_consciousness  # No competency in this domain

    # Get state elevation potential from mastery
    boost = competency.state_elevation_potential

    effective_consciousness = base_consciousness + boost

    return min(1.0, effective_consciousness)  # Cap at 1.0
```

**Why This Happens:**

- **Flow state access:** High mastery enables flow (deep absorption, time distortion)
- **Automatic execution:** Unconscious competence frees up cognitive resources
- **Pattern mastery:** Deep domain knowledge enables higher-order thinking
- **Confidence:** Mastery reduces anxiety, opens perceptual bandwidth

**Examples:**

```python
# Olympian running
olympian = Agent(consciousness_coefficient=0.50)  # Willingness (base)
olympian.competencies["running"] = Competency(mastery_level=0.92)  # Master

effective_state_while_running = 0.50 + 0.16 = 0.66  # Elevated to near-Love (0.69)
# Explains "runner's high" and flow states during competition

# Concert pianist performing
pianist = Agent(consciousness_coefficient=0.54)  # Acceptance (base)
pianist.competencies["piano"] = Competency(mastery_level=0.88)  # Master

effective_state_while_playing = 0.54 + 0.14 = 0.68  # Elevated to near-Love (0.69)
# Explains transcendent experiences during performance

# Mathematician solving equations
mathematician = Agent(consciousness_coefficient=0.59)  # Reason (base)
mathematician.competencies["mathematics"] = Competency(mastery_level=0.85)  # Expert/Master

effective_state_while_solving = 0.59 + 0.12 = 0.71  # Elevated to Love (0.69+)
# Explains "mathematical beauty" and mystical states during discovery

# Novice giving speech
novice_speaker = Agent(consciousness_coefficient=0.50)  # Willingness (base)
novice_speaker.competencies["public_speaking"] = Competency(mastery_level=0.35)  # Beginner

effective_state_while_speaking = 0.50 + 0.0 = 0.50  # No boost (below 0.5 threshold)
# Explains anxiety and struggle
```

---

## Everything Has Mastery Levels

**Not just skills - fundamental capacities too:**

Most people never train fundamental capacities, remaining unconsciously incompetent (0.2-0.4).

### Fundamental Capacities (Often Overlooked)

```python
fundamental_capacities = {
    # Cognitive
    "thinking": {
        "novice_0.3": "Reactive, emotional, logical fallacies",
        "master_0.85": "Metacognition, systems thinking, conscious reasoning"
    },

    "attention_control": {
        "novice_0.25": "Scattered, easily distracted, reactive",
        "master_0.80": "Laser focus, sustained attention, flow access"
    },

    "pattern_recognition": {
        "novice_0.30": "Surface-level, misses connections",
        "master_0.85": "Sees systems, anticipates patterns, abstracts principles"
    },

    "learning_itself": {
        "novice_0.30": "Passive, inefficient, trial-and-error",
        "master_0.82": "Meta-learning, accelerated acquisition, transfer mastery"
    },

    "deciding": {
        "novice_0.30": "Impulsive, regret-heavy, emotional override",
        "master_0.80": "Deliberate, values-aligned, considers consequences"
    },

    # Somatic
    "breathing": {
        "novice_0.20": "Unconscious, shallow chest breathing",
        "master_0.80": "Conscious breath control, diaphragmatic, pranayama"
    },

    "movement": {
        "novice_0.35": "Clumsy, unaware, inefficient",
        "master_0.85": "Graceful, body awareness, efficient biomechanics"
    },

    # Emotional
    "emotional_regulation": {
        "novice_0.30": "Reactive, overwhelmed, unconscious patterns",
        "master_0.82": "Conscious processing, healthy expression, equanimity"
    },

    # Social
    "listening": {
        "novice_0.25": "Waiting to speak, poor active listening, misses nuance",
        "master_0.82": "Deep listening, reads between lines, empathic resonance"
    },

    "speaking": {
        "novice_0.35": "Filler words, unclear, rambling",
        "master_0.85": "Precise, compelling, intentional word choice"
    },
}
```

**Key insight:** Just because you CAN do something ≠ you're GOOD at it

Most people:
- **Thinking:** 0.3-0.4 (mediocre, reactive)
- **Breathing:** 0.2-0.3 (terrible, unconscious)
- **Deciding:** 0.3-0.4 (impulsive, regret-prone)
- **Listening:** 0.2-0.3 (poor active listening)
- **Emotional regulation:** 0.3-0.4 (reactive, overwhelmed)

**Masters exist in these domains:**
- Meditation master: Breathing 0.85, Attention 0.88
- Therapist: Listening 0.82, Emotional regulation 0.80
- Philosopher: Thinking 0.88, Pattern recognition 0.85
- Decision scientist: Deciding 0.82

---

## Specialization: The Apple Tree Principle

**Core insight:** "The best apple tree doesn't try to grow pears"

Power comes from **depth in few domains**, not breadth across many.

```python
def specialization_analysis(agent: Agent) -> Dict:
    """
    Analyze agent's specialization strategy

    Specialist: Few domains (2-5) at high mastery (0.7+)
    Generalist: Many domains (10+) at low mastery (0.4-0.5)

    Returns:
        Analysis of specialization effectiveness
    """
    masteries = [c.mastery_level for c in agent.competencies.values()]
    masteries_sorted = sorted(masteries, reverse=True)

    # Specialization metrics
    top_3_average = sum(masteries_sorted[:3]) / 3 if len(masteries_sorted) >= 3 else 0.0
    domain_count = len(masteries)
    expert_count = len([m for m in masteries if m >= 0.7])

    # Specialization index
    specialization_index = top_3_average * expert_count / max(1, domain_count)

    # Classification
    if specialization_index >= 0.6:
        profile = "highly_specialized"  # Deep expertise, narrow focus
        strength = "Differentiated, high value, irreplaceable"
    elif specialization_index >= 0.3:
        profile = "moderately_specialized"  # Some depth, reasonable breadth
        strength = "Balanced, valuable in multiple contexts"
    else:
        profile = "generalist"  # Broad but shallow
        strength = "Versatile but replaceable, low differentiation"

    return {
        "profile": profile,
        "top_3_average": top_3_average,
        "expert_domains": expert_count,
        "total_domains": domain_count,
        "specialization_index": specialization_index,
        "strength": strength
    }
```

**Examples:**

**Olympian (Optimal Specialization):**
```python
olympian = {
    "100m_sprint": 0.95,  # World-class
    "200m_sprint": 0.88,  # Elite
    "weightlifting": 0.75, # Expert (supporting skill)
    "nutrition": 0.68,     # Advanced (supporting)
    "marathon": 0.30,      # Terrible (and that's fine!)
    "swimming": 0.35,      # Beginner (and that's fine!)
}
# Specialization index: 0.87 (highly specialized)
# Value: Exceptional at ONE thing = Olympic medals
```

**"Jack of All Trades" (Suboptimal):**
```python
generalist = {
    "piano": 0.45, "guitar": 0.42, "singing": 0.48,
    "painting": 0.44, "writing": 0.46, "cooking": 0.43,
    "running": 0.41, "swimming": 0.44, "yoga": 0.42,
    "programming": 0.47, "design": 0.45, "marketing": 0.44
}
# Specialization index: 0.18 (generalist)
# Value: Adequate at many things = easily replaceable
```

**Optimal Strategy:**
- **Master 2-5 domains** (0.7-0.9) - This is your differentiation
- **Maintain competence in 5-10 domains** (0.5-0.6) - Supporting skills
- **Accept incompetence in everything else** - Don't waste energy

**Why specialization matters:**
- Value comes from being **exceptional** at SOMETHING, not adequate at EVERYTHING
- Olympians, virtuosos, experts command value through DEPTH
- Generalists are replaceable - no unique offering
- Energy is finite - deep mastery requires focused investment

---

## Examples

### High-Mastery Olympian

```python
usain_bolt = Agent(
    consciousness_coefficient=0.52,  # Willingness (base)
    competencies={
        "100m_sprint": Competency(
            domain="100m_sprint",
            category="sport",
            mastery_level=0.98,  # World record holder
            baseline=0.55,       # Athletic background (perceptual boundary transfer)
            peak_mastery=0.98,
            hours_practiced=15000,
            state_elevation_potential=0.18  # Massive boost when running
        ),
        "200m_sprint": Competency(
            mastery_level=0.92,  # Also world-class
            baseline=0.65,       # Transfer from 100m (very similar)
            state_elevation_potential=0.16
        ),
        "marathon": Competency(
            mastery_level=0.35,  # Terrible (and that's optimal!)
            baseline=0.40,       # Some cardio transfer, but wrong muscle type
            state_elevation_potential=0.0
        )
    }
)

# When running 100m:
effective_consciousness = 0.52 + 0.18 = 0.70  # Elevated to Love level (flow state)

# When attempting marathon:
effective_consciousness = 0.52 + 0.0 = 0.52  # No boost (not his domain)
```

### Concert Pianist

```python
concert_pianist = Agent(
    consciousness_coefficient=0.59,  # Reason (base)
    competencies={
        "piano": Competency(
            domain="piano",
            category="art",
            mastery_level=0.88,  # Master
            baseline=0.15,       # Started as child (no prior music)
            peak_mastery=0.88,
            hours_practiced=12000,
            state_elevation_potential=0.14
        ),
        "music_theory": Competency(
            mastery_level=0.82,  # Expert (supporting skill)
            baseline=0.35,       # Learned alongside piano
            state_elevation_potential=0.11
        ),
        "guitar": Competency(
            mastery_level=0.48,  # Intermediate
            baseline=0.42,       # High transfer from piano (music theory, rhythm)
            state_elevation_potential=0.0  # Below threshold
        ),
        "painting": Competency(
            mastery_level=0.35,  # Beginner
            baseline=0.20,       # Artistic sensibility transfer, but different medium
            state_elevation_potential=0.0
        )
    }
)

# When performing piano:
effective_consciousness = 0.59 + 0.14 = 0.73  # Elevated to Joy level (transcendent experience)
```

### Mathematician

```python
mathematician = Agent(
    consciousness_coefficient=0.62,  # Reason (base)
    competencies={
        "topology": Competency(
            domain="topology",
            category="knowledge",
            mastery_level=0.92,  # World-class
            baseline=0.52,       # Strong math background (perceptual boundary)
            peak_mastery=0.92,
            hours_practiced=8000,
            state_elevation_potential=0.16
        ),
        "abstract_algebra": Competency(
            mastery_level=0.78,  # Expert
            baseline=0.48,       # Math transfer
            state_elevation_potential=0.09
        ),
        "programming": Competency(
            mastery_level=0.55,  # Competent
            baseline=0.48,       # High transfer (logical thinking, abstraction)
            state_elevation_potential=0.03
        ),
        "painting": Competency(
            mastery_level=0.28,  # Novice
            baseline=0.15,       # Low transfer (different domain)
            state_elevation_potential=0.0
        )
    }
)

# When solving topology problems:
effective_consciousness = 0.62 + 0.16 = 0.78  # Elevated to Peace level (mathematical beauty/mystical states)
```

### Most People (Unconsciously Incompetent at Fundamentals)

```python
average_person = Agent(
    consciousness_coefficient=0.43,  # Neutrality (base)
    competencies={
        # Fundamental capacities (never trained)
        "thinking": Competency(mastery_level=0.35),        # Mediocre
        "breathing": Competency(mastery_level=0.22),       # Terrible
        "deciding": Competency(mastery_level=0.38),        # Reactive
        "emotional_regulation": Competency(mastery_level=0.32),  # Reactive
        "attention_control": Competency(mastery_level=0.28),     # Scattered
        "listening": Competency(mastery_level=0.26),       # Poor

        # Maybe one skill pursued
        "cooking": Competency(mastery_level=0.52),         # Intermediate
        "driving": Competency(mastery_level=0.62),         # Advanced
    }
)

# No state elevation (nothing above 0.7)
# Remains at base consciousness in all contexts
```

---

## Relationship to Other Components

### Competency vs. Consciousness

**Orthogonal (Independent) Dimensions:**

| Consciousness | Competency (Domain) | Example |
|---------------|---------------------|---------|
| High (0.8) | Low (0.3) | Enlightened beginner learning piano |
| Low (0.3) | High (0.9) | Unconscious virtuoso pianist |
| High (0.7) | High (0.9) | Conscious master (rare, powerful) |
| Low (0.3) | Low (0.3) | Unconscious incompetent |

**Key insight:** You can be spiritually enlightened (0.8 consciousness) but terrible at piano (0.3 mastery). They're separate dimensions.

### Competency + Consciousness = Power

```python
manifestation_power = base_consciousness + (active_competency_boost if engaged)

# High consciousness + high mastery in engaged domain = exceptional power
enlightened_master = 0.80 + 0.15 = 0.95  # Near-perfect manifestation in that domain
```

### Competency Affects Perceptual Boundary

As you master a domain, your perceptual boundary expands:
- Pianist can imagine/create music that non-musicians can't
- Mathematician can conceive abstract spaces that others can't
- Athlete can visualize movement patterns that others can't

**This creates upward spiral:**
1. Master domain → expand perceptual boundary
2. Expanded boundary → can imagine more possibilities
3. More possibilities → higher baseline in related domains
4. Repeat

---

**Previous:** [12_data_model_environmental_context.md](12_data_model_environmental_context.md) | **Next:** (End of data models)
