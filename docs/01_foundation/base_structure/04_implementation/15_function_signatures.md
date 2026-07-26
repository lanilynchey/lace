# Function Signature Standards

All forces in LACE follow consistent patterns.

## Standard Force Function

```python
def force_name(inputs) -> output:
    """
    Brief description of what this force does

    Args:
        input1: Description
        input2: Description

    Returns:
        output: Description

    Dependencies:
        - dependency1()
        - dependency2()

    Properties:
        - Property 1
        - Property 2

    Examples:
        >>> force_name(input)
        expected_output
    """
    # Implementation or pseudocode
    pass
```

## Example: fear()

```python
def fear(agent: Agent, scenario: Scenario) -> PreparedState:
    """
    Anticipatory threat simulation - forward-facing risk analysis

    Args:
        agent: The conscious entity running the simulation
        scenario: The potential threat being evaluated

    Returns:
        PreparedState: Agent with suppressed expansion + threat prep

    Dependencies:
        - memory() - Stores past threat data
        - consciousness() - Enables simulation
        - pattern() - Recognizes threat signatures

    Properties:
        - Suppresses expansion (narrows possibility space)
        - Loops when unresolved (creates anxiety)
        - Meant to trigger adaptation, not paralysis

    Examples:
        >>> fear(agent, scenario="financial_loss")
        PreparedState(expansion=0.2, readiness=0.8, loop_count=3)
    """
    simulation = run(possible_negative_outcome(scenario))
    suppress_expansion(agent)
    return prepare(agent, threat_signature(scenario))
```

---

**Previous:** [14_working_with_data_models.md](14_working_with_data_models.md) | **Next:** [16_interaction_protocols.md](16_interaction_protocols.md)
