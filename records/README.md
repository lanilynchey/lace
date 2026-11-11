# LACE records

A record is one run of one chain. One JSON file per record. Every id in a record comes from `../glossary/`.

## Where things are

| Folder | What it holds |
|---|---|
| `examples/` | Worked records: one for each of fourteen chains, plus Full Grip and a Flood of emotion each taking all of your attention, the same Action at two supply levels, an Impulse held back, a Boredom that runs again, and a stalled Desire |

## Every record

```json
{
  "id": "record_0002",
  "chain": "chain_attention",
  "moment": "A notification lands mid-sentence",
  "steps": [
    { "step": "step_trigger", "gate": 1, "what": "Your phone buzzes while you are halfway through a sentence." },
    { "step": "step_detection", "gate": 1, "what": "You register the buzz." },
    { "step": "step_selection", "gate": 0, "what": "You keep your attention on the sentence." }
  ]
}
```

- `id`: `record_` and a four-digit number.
- `chain`: the glossary id of the chain that ran.
- `moment`: the run in one plain line.
- `state`: the state it ran in. The id of a file in `../states/`.
- `instance`: whose run it is. The id of one Instance.
- `reach`: on a run that belongs to a group: how wide, as a Reach level (`reach_circle`, `reach_community`, `reach_country`, `reach_world`). Left out when it is one person's.
- `open`: `true` on a stalled run. It stopped at a gate 0 because of a thought and can pick up again. When it does, the same record carries on from that step.
- `time`: when the run happened. Left out when it is not known.
- `emotion`: on a run of a chain that is the run of one emotion (Boredom, Anger). Holds `emotion`, `charge` and `stake`.
- `resources`: how full each resource or need was when the chain ran. Each entry has `resource` and `at`, a supply level. Left out when it is not known.
- `steps`: one line per step, in the chain's order.

## A step line

Every step line has three fields:

- `step`: the glossary id of the step.
- `gate`: the arrow into this step. 1 if the step happened, 0 if the chain stopped there.
- `what`: what happened at that step.

A step line carries more only when it applies:

- `source`: on Occurrence only. One of `source_lived`, `source_told`, `source_imagined`.
- `emotions`: on the Emotion step. One entry per emotion felt, more than one when they are felt together. Each entry has `emotion`, a glossary id from the Emotional Spectrum at any level; `charge`, how strong it was (`charge_flicker`, `charge_hum`, `charge_pulse`, `charge_surge` or `charge_flood`); and `stake`, what it was tied to (`stake_survival`, `stake_social` or `stake_self`).
- `sense`: on the Senses step. Which sense it came in by.
- `signals`: on the Body Signals step. Which signals showed: `signal_heartbeat`, `signal_breath`, `signal_nerves`, `signal_muscles`, `signal_posture`.
- `side`: on a "this or that" step. The name of the side that happened.
- `ran_again`: on a side that makes the chain run again. Holds `record`, the new run. This run ends there.
- `opened`: the step opened its own chain. Holds `chain`, that chain, and `record`, that run.
- `sparked`: the step started another chain. Each entry holds `link`, the Sparks link, and `record`, that run.
- `tilts`: the step changed how another chain runs. Each entry holds `link`, the Tilts link, and `record`, the run it changed.
- `tilted_by`: another chain changed how this step ran. Each entry holds `link`, the Tilts link, and `record`, the run it came from.
- `closed_by`: on a step with gate 0, when a low resource is why it closed. Each entry has `resource` and `at`, its supply level.

`record` is empty when that run is not written down.

## The rules

- A record's file is named with its number and the chain: `0007-action.json`.
- A record stops at its first gate 0. Steps after it are not written. A Chain Break closes the record. A Chain Stall leaves it `open`.
- A record also stops after a side whose `then` is `stops`. That step's gate is 1: the step happened, and the side ended the chain.
- A step line only uses a link that exists in the glossary.
- A step that opens the chain it is already in has no `opened`.
- A side that starts another chain does not end this run: the next step is still written.
- `closed_by` is stated by the record. It is not worked out from the resource's file.
