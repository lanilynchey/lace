# LACE states

A state is everything that is true about one Instance at one moment. Chains run inside a state, and what they produce changes it. Every id in a state comes from `../glossary/`.

## Where things are

| Folder | What it holds |
|---|---|
| `examples/` | Making friends after moving to a new city, as a Current State and a Desired State |

## Every state

- `id`: `state_` and a four-digit number.
- `state`: which State this is: `state_current`, `state_desired`, `state_signature`, `state_past`, `state_peak` or `state_place_state`. A Place State is how one place is for you, and carries emotions like any other state.
- `instance`: whose state it is.
- `moment`: when, in one plain line.
- `time`: when, exactly. Left out when it is not known.

Everything below is left out when it is not known.

- `resources`: how full each resource is. Each entry has `resource` and `at`, a supply level.
- `emotions`: what is being felt. Each entry has `emotion`, `charge` and `stake`.
- `needs`: how met each need is. Each entry has `need` and `at`, a supply level.
- `skills`: each entry has `what`, in plain words, and `at`, a skill level.
- `beliefs`: what is held as true, in plain words.
- `where`: the place, in plain words.
- `around`: who is near. Each entry has `circle`, a circle level, and `what`, in plain words.
- `usual`: how things usually go, in plain words.
- `body`: what is true about the body. Each entry has `what`, a part of the Body (`body_weight`, `body_height`, `body_age`, `body_health`, `body_conditions`, `body_inherited`, `body_changes`), and `is`, in plain words.
- `preferences`: what you prefer, in plain words. In a Signature State, these together are your taste.
- `circle`: on a Place State, which circle the place is in for you.
- `influences`: what is pulling on you over time. Each entry has `from`, in plain words; `part`, the part of Surroundings it comes from (`surroundings_circles`, `surroundings_groups`, `surroundings_environment` or `surroundings_intake`); and `on`, the chain it pulls on.

## The rules

- A record names the state it ran in with `state`.
- The Gap is what differs between one Instance's Current State and its Desired State.
- No amounts. Everything is a named level or plain words.
