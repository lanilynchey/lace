## Worldline Matching Mechanics

**How the system finds your match**

```python
def find_closest_worldline(broadcast_frequency):
    """
    Query worldline database for closest vibrational match

    Process:
        1. Receive broadcast_frequency
        2. Search all available worldlines
        3. Calculate resonance match for each
        4. Return highest resonance worldline

    Returns:
        Timeline: Closest matching experiential path
    """
    # Get all possible worldlines
    worldlines = query_timeline_database()

    # Calculate resonance for each
    matches = []
    for worldline in worldlines:
        resonance = calculate_resonance(broadcast_frequency, worldline.frequency)
        matches.append((worldline, resonance))

    # Sort by resonance (highest first)
    matches.sort(key=lambda x: x[1], reverse=True)

    # Return best match
    best_match = matches[0][0]
    return best_match
```

### **Resonance Calculation**

```python
def calculate_resonance(agent_frequency, worldline_frequency):
    """
    How closely two frequencies match

    Formula:
        resonance = 1 - abs(agent_frequency - worldline_frequency)

    Returns:
        float: 0-1 (1 = perfect match, 0 = no match)
    """
    difference = abs(agent_frequency - worldline_frequency)
    resonance = 1 - difference

    return resonance
```

**Example:**

```python
# Your frequency:
agent_frequency = 0.75  # Moderately high vibration

# Available worldlines:
worldline_a.frequency = 0.76  # Very close
worldline_b.frequency = 0.45  # Far
worldline_c.frequency = 0.74  # Very close

# Resonance:
resonance(agent, worldline_a) = 0.99  # Best match
resonance(agent, worldline_b) = 0.70  # Poor match
resonance(agent, worldline_c) = 0.99  # Also good match

# Result:
manifest(worldline_a OR worldline_c)  # Whichever has higher coherence
```

---

