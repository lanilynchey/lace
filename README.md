# LACE

*Language for Articulating Computational Existence*

**Life, written like code.**

## What is LACE?

LACE is language to describe how a life runs. It writes thoughts, feelings, habits and relationships as named parts with rules, the way a system is described.

LACE describes what a person can reach within a reality that holds more than we can reach.

## The core belief

**We are binary beings living in a base-10 reality.**

We live through yes and no. Good or bad. Right or wrong. Like or dislike. Go on, or stop. Every moment resolves into ones and zeros, and many of them together, in context, make a rich and complicated life. Holding two feelings at once, grey areas and "maybe" all happen in ones and zeros.

Reality has more than that: the digits 0 to 9. LACE holds that 2 to 9 are here with us right now, not somewhere far away, but what they are is beyond what ones and zeros can reach.

Whether anything lies beyond ten, nobody knows. Whoever or whatever made the system has access to all ten, and anything beyond.

So the humility is built in. There is far more we can't know than we can.

## The Flower

A flower is part of this coded reality, and we experience it through our ones and zeros. We can interact with it and name it down to its atoms, but we can't create a flower. If we tried, it would look like every flower before it ([Nothing From Nothing](glossary/01-foundations/rules/nothing-from-nothing.json)).

Throughout LACE, we look through the lens of a flower. `glossary/00-the-flower/` holds the Flower and its lenses. Each lens is one truth the Flower shows, and points at the part of LACE that proves it.

## Everything runs as a chain

Every step in a chain is a gate: **1**, it passes and the chain goes on, or **0**, it stops there.

The most important chain is **Thought**, because it is the main mechanism of your Current State:

```
I'm the funny one in my family.

Thought       1   I'm the funny one in my family.
Repetition    1   You think it at every family dinner, for years.
Belief        1   It becomes who you are at home.
Perception    1   You see every quiet moment at the table as yours to fill.
Emotion       1   A lift when they laugh, a small dread when they don't.
Action        1   You make the joke.
Habit         1   You joke before anyone else has spoken.
Behaviour     1   You are the one who lightens every room.
Results       1   The family laughs, and comes to you for it.
Reinforcement 1   Each laugh confirms the thought.
Reality       1   In your family, you are the funny one.
```

A 0 anywhere and it stops: the thought never becomes a belief, the belief never becomes a habit. Changing a life means changing where your chains stop, and how far they progress.

## The pieces

- **Chains** (96): Thought, Perception, Emotion, Action, Memory, Desire, Connection, Need and the chains that come off them.
- **Steps** (310): the points in a chain. One step can sit in many chains.
- **Sides**: a step named "this or that" splits. *Inhibition or Action.* Each side says what happens next.
- **Links**: one chain **sparks** another, or **tilts** how another runs. A memory tilts what you perceive.
- **States**: everything true about you at one moment. Your **Current** State, the **Desired** one, and the **Gap** between them.
- **Records**: one run of one chain, written down.
- **Surroundings**: everything outside you. Circles, Groups, Environment, Intake, Influences, Impact.

## In here

| Folder | What it holds |
|---|---|
| `glossary/` | Every thing in LACE, one JSON file each. 874 of them. |
| `states/` | Everything true about one person at one moment. |
| `records/` | Runs of chains, step by step. |
| `tools/` | The checker. |

## Start here

1. `glossary/MAP.md`: every chain, every link, every side and every lens of the Flower, on one page.
2. `glossary/README.md`: what a file looks like and what each field means.
3. `states/README.md` and `records/README.md`: how a moment and a run are written.
4. `glossary/index.json`: everything that connects to any id.

## Check it

```
python3 tools/build_index.py
```

Stops at the first thing that's wrong, then rebuilds the map and the index.

## License

LACE is licensed under [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).

You can share it, and build on it, as long as you credit Lani Lynchey and don't use it commercially.

## Contact

For questions, collaborations or conversation: lani@ladiduh.com

---

*"There is so much to know. So much so, that I know nothing at all. And everything I know could be totally wrong."*
