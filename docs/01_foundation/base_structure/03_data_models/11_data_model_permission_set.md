# Data Model: PermissionSet

What an agent can read, write, and execute.

```python
class PermissionSet:
    """Access control for reality manipulation"""

    # Base Permissions (Default Human)
    read: str = "partial"      # Memory, identity
    write: str = "localized"   # Actions, beliefs
    exec: str = "restricted"   # Manifestation, psychic ability

    # Elevated Permissions (Mystics, Masters)
    # read: str = "expanded"   # Karma, timelines, others
    # write: str = "transdimensional"  # Field-level changes
    # exec: str = "partial_root"  # Create/override local systems

    # Root Permissions (Creator)
    # read: str = "full"       # All information
    # write: str = "universal" # Edit constants, laws
    # exec: str = "root"       # Full system control

    # Dynamic Unlocks
    temporary_permissions: List[Tuple[str, float]]  # (permission, duration)
    earned_permissions: List[str]  # Permanent upgrades
```

## Permission Elevation Mechanics

How agents gain expanded access to reality manipulation:

```python
# Constants
PERMISSION_UNLOCK_THRESHOLD = 0.85  # Coherence needed for temporary elevation
STABILITY_DURATION = 7200  # Seconds coherence must be maintained (2 hours)

def check_permission_elevation(agent: Agent) -> None:
    """
    Continuously monitors agent coherence and grants/revokes permissions

    Elevation types:
    1. Temporary - Granted when coherence sustained above threshold
    2. Earned - Permanent upgrades from soul contract completion

    Called by: coherence_monitor daemon (continuous check)
    """
    current_coherence = agent.state_signature.coherence

    # Check for temporary elevation
    if current_coherence >= PERMISSION_UNLOCK_THRESHOLD:
        duration = calculate_stability_duration(agent)

        if duration >= STABILITY_DURATION:
            unlock_temporary_permission(
                agent,
                permission="expanded_read",  # Can read karma, timelines, others
                duration=duration * 0.5  # Permission lasts half of stability time
            )

    # Check for earned elevation (permanent)
    if pattern_transcended(agent) or major_initiation(agent):
        grant_permanent_permission(
            agent,
            new_level=agent.access_level + 1,
            new_permissions=["transdimensional_write", "partial_root_exec"]
        )

    # Revoke temporary permissions if coherence drops
    for perm, expiry in agent.permissions.temporary_permissions:
        if current_coherence < PERMISSION_UNLOCK_THRESHOLD * 0.9:  # 10% buffer
            revoke_permission(agent, perm)


def calculate_stability_duration(agent: Agent) -> float:
    """
    How long has coherence been maintained above threshold?

    Returns:
        Seconds of continuous high-coherence state
    """
    history = agent.coherence_history[-100:]  # Last 100 measurements
    stable_count = sum(1 for c in history if c >= PERMISSION_UNLOCK_THRESHOLD)
    return stable_count * MEASUREMENT_INTERVAL  # seconds
```

## Permission Elevation Triggers

**Temporary Elevation:**
1. **Extended coherence** - Meditation, breathwork, sustained practice
2. **Flow states** - Peak experiences, deep presence

**Earned Elevation (Permanent, but Conditional):**
1. **Pattern transcendence** - Breaking through persistent limiting patterns
2. **Major initiation** - Significant spiritual milestones, mastery attainments
3. **Ego dissolution** - Nondual states, unity consciousness experiences
4. **Grace events** - Divine intervention (rare, unknowable criteria)

**Permission Levels:**
- **Level 0 (Default Human):** Partial read, localized write, restricted exec
- **Level 5 (Mystic/Master):** Expanded read, transdimensional write, partial root exec
- **Level 10 (Creator/Root):** Full read, universal write, root exec

## Reversibility

**Temporary permissions:**
- Revoked immediately when coherence drops below threshold (0.85 → 0.765 with 10% buffer)
- Examples: Meditation states, flow states, peak experiences

**Earned permissions (Conditional Permanent - E2 Model):**
- Generally permanent within lifetime
- **Can be revoked on extreme regression:**
  - Deep pattern regression (returning to old trauma loops)
  - Serious ethical violations
  - Major "dark night" collapse
- Revocation is rare but possible (keeps stakes high)

**Grace permissions:**
- Duration set by system (unknowable to agent)
- Revocation at system's discretion

## Note on Knowledge vs Permission

There's a nuanced relationship between choice, knowledge, and permissions:
- **You can't unknow what you know** (knowledge is irreversible)
- **But you can forget you understand** (lose access to how to apply knowledge)
- **Permission loss ≠ knowledge loss** (you still know, but lose ability to execute)

Example: Enlightened being regresses into trauma → still has the knowledge/awareness, but loses the permission to operate from that state (coherence drops, permissions revoke).

This is different from choice-based permissions (you can always choose differently), because once you've seen certain truths, they're permanent knowledge. The permission to ACT on that knowledge, however, is conditional on your current state.

**[This integration with choice/knowledge requires further development and may be expanded in future iterations]**

---

**Previous:** [10_data_model_location_imprint.md](10_data_model_location_imprint.md) | **Next:** [12_data_model_environmental_context.md](12_data_model_environmental_context.md)
