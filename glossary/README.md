# LACE glossary

Every thing in the system, one JSON file per thing. This is the single source of names: a record, a page or an agent refers to a thing by its `id` from here.

States live next to this folder in `../states/`, and runs of chains in `../records/`.

## Where things are

| Folder | What it holds | Files |
|---|---|---|
| `00-the-flower/` | The Flower, and its lenses sorted by the part of LACE each one proves, in folders matching the ones below | 78 |
| `01-foundations/` | The Base System: its cycle, resources, stakes and rules | 42 |
| `02-core/` | The three cores: Attention, Time, State | 22 |
| `03-chain-system/` | What a chain is made of: step, gate, core, kinds, links, record, occurrence, source, reach, chain rules | 36 |
| `04-chains/` | Every chain, in twelve groups, plus the links between chains | 288 |
| `05-steps/` | Every step | 310 |
| `06-body/` | The Body: its signals, weight, height, age, health, what it inherits and goes through | 14 |
| `07-surroundings/` | Circles, groups, environment, impact, influences, intake and the five senses | 47 |
| `08-form/` | The Render, the Form and its forms, appearance, death | 10 |
| `09-making/` | Expressions and the forms of Art, combinations | 13 |
| `10-skills/` | Skills, skill levels, base skills and skill limits | 14 |

Inside `04-chains/`:

| Folder | Chains |
|---|---|
| `01-attention/` | Attention |
| `02-perception/` | Perception and its spur |
| `03-thought/` | Thought, its zoom-ins and spurs |
| `04-emotion/` | Emotion and its chains, plus `spectrum/` (every emotion), `levels/`, `charge/`, `survival-responses/`, `terms/` |
| `05-action/` | Action |
| `06-memory/` | Memory |
| `07-desire/` | Desire |
| `08-communication/` | Communication |
| `09-connection/` | Connection |
| `10-need/` | Need |
| `11-creation/` | Creation |
| `12-change/` | Change |
| `links/` | Every Sparks and Tilts link |

A folder is only for finding files. What a thing is and what it belongs to are always in the file itself.

## Finding connections

Two generated files save you from searching every file. Both are built from the glossary files and are never edited by hand.

| File | What it holds |
|---|---|
| `MAP.md` | Every chain that stands on its own with the chains that come off it, every link, every side, and every lens of the Flower. Read this first for the whole picture. |
| `index.json` | For every id, everything that connects to it. Keys are listed below. |

Keys in `index.json`, each present only when it applies:

| Key | What it holds |
|---|---|
| `name`, `is`, `file`, `part_of` | Copied from the thing's own file. |
| `parts` | Everything whose `part_of` is this. |
| `steps`, `kind` | On a chain: its steps and kind. |
| `step_in` | The chains that use this as a step. |
| `opens`, `opened_by` | The chain this step opens, and the steps that open this chain. |
| `zoom_in_of`, `zoom_ins` | The step a zoom-in looks closer at, and the zoom-ins of this step. |
| `sides` | On a two-sided step: its sides and what each leads to. |
| `started_by_side` | The sides that start this. |
| `links_out`, `links_in` | Links leaving and reaching this, with their steps and any `when`. |
| `emotion`, `chain` | The emotion a chain is the run of, and the chains that are the run of this emotion. |
| `named_in` | Other files that name this: as a refill, a draw, an override, or what running low affects. |
| `records` | Records that are runs of this chain. |

## Every file

Five fields, in this order:

```json
{
  "id": "cycle_creation",
  "name": "Creation",
  "is": "term",
  "definition": "Making something new.",
  "part_of": "base_system_cycle"
}
```

| Field | What it holds |
|---|---|
| `id` | The thing's one id. Never reused. An id that starts with `step_`, `chain_`, `link_`, `emotion_` or `rule_` is always that kind of file. |
| `name` | What it is called. |
| `is` | What the file is: `step`, `chain`, `link`, `emotion`, `rule` or `term`. |
| `definition` | Only what the thing is. |
| `part_of` | The id of the one thing it belongs to. Empty if it belongs to nothing. |

Two things can share a name when one is the chain of how the other runs: Creation and the Creation chain. `is` tells them apart.

## The six kinds of file

### chain

A run of steps.

| Field | What it holds |
|---|---|
| `kind` | `chain` (stands on its own), `spur` (comes off another chain) or `zoom-in` (a closer look at one step of another chain). |
| `emotion` | On a chain that is the run of one emotion: that emotion. Anger points at Angry. |
| `refills` | On a chain that meets a need: the resources it refills when it completes. Sleep refills Attention Reserve and Energy. |
| `steps` | The ids of its steps, in order. |
| `locked` | `true` when the steps are settled and not to be changed. |
| `of_step` | On a zoom-in: the step it looks closer at. |
| `note` | A plain remark about the chain. |

Core is not a kind of chain. Attention, Time and State are the three cores, and each runs through every chain. Attention also has a chain of its own.

### step

One point in a chain. A step belongs to no single chain, so its `part_of` is empty.

| Field | What it holds |
|---|---|
| `used_in` | The ids of every chain that uses it. |
| `opens` | The chain this step opens, when it has one. Inside that same chain it opens nothing: there it is the moment itself. |

A zoom-in can be reached two ways: from the step it looks closer at (its `of_step`), and from a step that carries its name. Decision is a closer look at Intention, and the Decision step opens it too.

| Field | What it holds |
|---|---|
| `sides` | On a step named "this or that": its two sides. |

Each side has a `name` and a `then`, what happens after it:

| `then` | Meaning |
|---|---|
| `carries on` | The next step runs. |
| `stops` | The chain stops there. |
| `ends` | It was the last step. |
| an id | What it starts. When it is the chain's own id, the chain runs again. |

A side that starts another chain also has a Sparks link. Starting another chain does not stop this one: its next step still runs.

Anything a chain uses as a step carries `used_in`, whatever its `is`. Survival Scan is a term that four chains use as a step.

### link

A connection into a chain. It usually leaves another chain, and it can also leave a term: Survival Scan tilts Perception. Its `part_of` is `structure_sparks` (one chain starts another) or `structure_tilts` (one chain changes how another runs).

| Field | What it holds |
|---|---|
| `from` | What it leaves. |
| `at` | The step it leaves at. Empty when it is no one step. |
| `to` | The chain it reaches. |
| `enters` | The step it enters at. Empty when it is no one step. |
| `when` | On a link that only holds sometimes: what has to be true. A Flood of emotion, for one. |

### emotion

One emotion in the Emotional Spectrum.

| Field | What it holds |
|---|---|
| `rooted_in` | On a Rooted Emotion: the emotion it grows out of. Courageous is rooted in Fearful. |
| `places` | Where it sits in the spectrum. Each place has a `level` (`main`, `secondary` or `tertiary`) and `under`, the emotions above it. An emotion can sit in more than one place. |

### rule

Something that always holds: the Base Rules and the chain rules. A rule a chain uses as a step carries `used_in`, like Chain Break in Discipline.

### term

Everything else. No extra fields of its own.

### A resource

A term under System Resources also says how it moves over time.

| Field | What it holds |
|---|---|
| `refilled_by` | What refills it. |
| `always_drawn_by` | What draws from it all the time, whether or not anything else is happening. |
| `depleted_by` | What uses it up while it is happening. Each entry has `what`, and `more_with`: the thing that makes it draw more as it rises. |
| `low_from` | The supply level where running low starts. |
| `when_low` | What happens as it runs low. This is Fade beginning. Each entry has `what`, in plain words, and `affects`, the thing it makes harder. |

How full a resource is is its Supply. It has five named levels, in `01-foundations/resources/supply/`: Drained, Worn, Thinning, Ample, Brimming. `order` runs from 1 (Drained) to 5 (Brimming).

## Fields any file can carry

| Field | What it holds |
|---|---|
| `checks` | What an agent can test. Each one is a plain statement of what must hold. |
| `overridden_by` | What can drown it out while it stays on. Survival Scan is on with an override: Full Grip or a Flood of emotion. |
| `order` | The thing's position among its siblings: the five charges, the five supply levels, the five skill levels, the circles, the reach. |
| `stake_order` | Which stake comes first for this thing. For Desires: Survival, then Self, then Social. For the Survival Scan weighing a threat, and for Needs: Survival, then Social, then Self. |
| `by_stake` | On Needs: every need, grouped by the stake it is tied to. A need can be a term (Air), a resource (Food), a chain (Sleep, Belonging) or a step (Safety). |
| `met_by` | On Needs: the chains that meet a need. |
| `grows_with` | On Skills: what makes a skill grow. |
| `includes` | Things that belong in this group but already exist elsewhere in the glossary, such as the Decision chain in Base Skills, or Music in Media. |
| `entries` | On an Intake category: the kinds of intake in it, one word each where possible. |
| `allows` | On a rule: the options it leaves open. |
| `gives` | On The Render: what you are given at the start. |
| `may_be_shaped_by` | On The Render: what may shape it. How is not known. |
| `comes_by` | On Death: the ways it comes. |
| `begins_at` | On a life stage: what marks its start. Waiting begins at Death. |
| `of`, `makes` | On a combination: the two things combined, and what they make. |
| `between` | On Creation: the two States it happens between. |
| `closes_with` | On The Gap: what closes it. |
| `comes_from` | What it is made from or comes from. Signature State comes from Chain Progression and Chain Length; Inherited comes from The Render. |
| `moves_in_by`, `moves_out_by` | On Circles: what moves a person closer, and what moves them further away. |
| `made_of` | On State: what a state is made of. |
| `circles` | On Places: the circles a place can be in, the same ones people are in. |
| `tied_to` | On Places: the State that holds how a place is for you. |
| `is_a` | The kind of thing this is, when it also belongs somewhere else. Stagnation Impact is an Impact, Impact is an Occurrence, and The Flower is a Flower. |
| `shows` | On a lens of The Flower: the parts of LACE that prove what the lens shows. |
| `stages` | On Life Stages: its stages in order. Fade is the third, and is the same Fade as in the System Cycle. |
| `status` | Why a thing is not finished: `to build`. Nothing carries it at present. |

## The rules

- A thing exists once. Something used as a step in a chain is still one file.
- A definition doesn't carry what the thing leads to or what it comes from. "The good feeling after a behaviour." Not "...that makes you want to repeat it."
- A list of parts never sits inside a definition.
- A field name can't be a word the glossary already uses for something else.
- Every id a file points at exists in the glossary.
- No dates, no "decided", no "potential". The file states the thing as it is.
