# Φ (Phi) - Pattern Symmetry

Governs form and self-replication. The structural logic of existence.

```python
class Phi:
    """The primitive of pattern and form"""

    def __init__(
        self,
        symmetry: float,
        fractal: bool = False,
        golden_ratio: float = 1.618033988749895
    ):
        self.symmetry = symmetry       # Degree of order
        self.fractal = fractal         # Self-similar?
        self.golden_ratio = golden_ratio

    def generate(self, seed: Any) -> Any:
        """
        Create structured form from seed

        Args:
            seed: Initial pattern to replicate or form

        Returns:
            Generated form (fractal or static)
        """
        if self.fractal:
            return recursively_replicate(seed)
        else:
            return static_form(seed)
```

**What Phi Governs:**
- Fibonacci sequences in nature
- Crystal formation
- DNA structure
- Beauty (coherent pattern recognition)

**Real-World Manifestation:**
- Spiral galaxies
- Nautilus shells
- Flower petal arrangements
- Musical harmony

---

**Previous:** [04_chi.md](04_chi.md) | **Next:** [06_elo.md](06_elo.md)
