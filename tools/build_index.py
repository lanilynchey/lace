"""Checks the glossary, states and records, then builds glossary/index.json and glossary/MAP.md.

Run from the lace folder:  python3 tools/build_index.py
It stops with a message at the first thing that is wrong: an id that points at nothing,
an id whose prefix does not match what the file is, a chain and a step that disagree,
a side with no outcome, or a record that does not follow its chain.
Both outputs are generated. Change the glossary files, then run this again.
"""
import json, glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G = os.path.join(ROOT, "glossary")
D = {}
for f in sorted(glob.glob(os.path.join(G, "**", "*.json"), recursive=True)):
    if os.path.basename(f) == "index.json":
        continue
    d = json.load(open(f))
    if d["id"] in D:
        sys.exit("duplicate id " + d["id"])
    d["_file"] = os.path.relpath(f, G)
    D[d["id"]] = d

def need(i, where):
    if i not in D:
        sys.exit(f"{where} points at {i}, which does not exist")

I = {i: {"name": d["name"], "is": d["is"], "file": d["_file"], "part_of": d["part_of"]} for i, d in D.items()}
def add(i, key, val):
    I[i].setdefault(key, []).append(val)

for i, d in D.items():
    if d["part_of"]:
        need(d["part_of"], i); add(d["part_of"], "parts", i)
    for s in dict.fromkeys(d.get("steps", [])):
        need(s, i); add(s, "step_in", i)
        if i not in D[s].get("used_in", []): sys.exit(f"{i} uses {s} as a step, but {s} does not list it in used_in")
    for c in d.get("used_in", []):
        need(c, i)
        if i not in D[c].get("steps", []): sys.exit(f"{i} lists {c} in used_in, but {c} does not use it as a step")
    if d["is"] == "chain" and d.get("kind") not in ("chain", "spur", "zoom-in"):
        sys.exit(f"{i} has kind {d.get('kind')}")
    if d.get("steps"):
        I[i]["steps"] = d["steps"]; I[i]["kind"] = d["kind"]
    if d.get("opens"):
        need(d["opens"], i); I[i]["opens"] = d["opens"]; add(d["opens"], "opened_by", i)
    if d.get("of_step"):
        need(d["of_step"], i); I[i]["zoom_in_of"] = d["of_step"]; add(d["of_step"], "zoom_ins", i)
    if d.get("sides"): I[i]["sides"] = d["sides"]
    for sd in d.get("sides", []):
        t = sd["then"]
        if t == "": sys.exit(f"{i} has a side with no then")
        if t not in ("carries on", "stops", "ends"):
            need(t, i); add(t, "started_by_side", {"step": i, "side": sd["name"]})
    if d["is"] == "link":
        for k in ("from", "to"): need(d[k], i)
        for k in ("at", "enters"):
            if d[k]: need(d[k], i)
        kind = "sparks" if d["part_of"] == "structure_sparks" else "tilts"
        row = {"link": i, "kind": kind, "at": d["at"], "to": d["to"], "enters": d["enters"]}
        if d.get("when"): need(d["when"], i); row["when"] = d["when"]
        add(d["from"], "links_out", row)
        add(d["to"], "links_in", {"link": i, "kind": kind, "from": d["from"], "at": d["at"], "enters": d["enters"]})
    for p in d.get("places", []):
        for u in p["under"]: need(u, i)
    for k in ("refilled_by", "always_drawn_by", "overridden_by"):
        for x in d.get(k, []):
            need(x, i); add(x, "named_in", {"by": i, "as": k})
    for e in d.get("depleted_by", []):
        need(e["what"], i); add(e["what"], "named_in", {"by": i, "as": "depleted_by"})
        if e["more_with"]: need(e["more_with"], i); add(e["more_with"], "named_in", {"by": i, "as": "more_with"})
    for w in d.get("when_low", []):
        need(w["affects"], i); add(w["affects"], "named_in", {"by": i, "as": "when_low"})
    if d.get("emotion"):
        need(d["emotion"], i); I[i]["emotion"] = d["emotion"]; add(d["emotion"], "chain", i)
    head = i.split("_")[0]
    if head in ("step", "chain", "link", "emotion", "rule") and head != d["is"]:
        sys.exit(f"{i} starts with {head}_ but is a {d['is']}")
    if d.get("rooted_in"):
        need(d["rooted_in"], i); I[i]["rooted_in"] = d["rooted_in"]; add(d["rooted_in"], "named_in", {"by": i, "as": "rooted_in"})
    for k in ("refills", "met_by", "grows_with", "includes", "gives", "may_be_shaped_by", "comes_by", "of", "between", "closes_with", "comes_from", "made_of", "tied_to", "moves_in_by", "moves_out_by"):
        for x in d.get(k, []):
            need(x, i); add(x, "named_in", {"by": i, "as": k})
    for grp in d.get("by_stake", []):
        need(grp["stake"], i)
        for x in grp["needs"]: need(x, i); add(x, "named_in", {"by": i, "as": "by_stake"})
    if d.get("makes"):
        need(d["makes"], i); add(d["makes"], "named_in", {"by": i, "as": "makes"})
    if d.get("circles"):
        need(d["circles"], i); add(d["circles"], "named_in", {"by": i, "as": "circles"})
    for x in d.get("shows", []):
        need(x, i); add(x, "named_in", {"by": i, "as": "shows"})
    if d.get("is_a"):
        need(d["is_a"], i); add(d["is_a"], "named_in", {"by": i, "as": "is_a"})
    if d.get("begins_at"):
        need(d["begins_at"], i); add(d["begins_at"], "named_in", {"by": i, "as": "begins_at"})
    for x in d.get("stages", []):
        need(x, i); add(x, "named_in", {"by": i, "as": "stages"})
    for x in d.get("stake_order", []):
        need(x, i); add(x, "named_in", {"by": i, "as": "stake_order"})
    if d.get("low_from"): need(d["low_from"], i); add(d["low_from"], "named_in", {"by": i, "as": "low_from"})

for f in sorted(glob.glob(os.path.join(ROOT, "records", "**", "*.json"), recursive=True)):
    r = json.load(open(f)); need(r["chain"], r["id"]); add(r["chain"], "records", r["id"])
    def feel(e):
        for k in ("emotion", "charge", "stake"):
            if k in e: need(e[k], r["id"])
    if "emotion" in r:
        feel(r["emotion"])
        if D[r["chain"]].get("emotion") != r["emotion"]["emotion"]: sys.exit(f"{r['id']} names an emotion its chain is not the run of")
    if "reach" in r: need(r["reach"], r["id"])
    if r.get("open") and r["steps"][-1]["gate"] != 0: sys.exit(f"{r['id']} is open but did not stop at a gate 0")
    order = D[r["chain"]]["steps"]
    for n, s in enumerate(r["steps"]):
        if n >= len(order) or s["step"] != order[n]: sys.exit(f"{r['id']} step {n + 1} is out of the chain's order")
        if s["gate"] == 0 and n != len(r["steps"]) - 1: sys.exit(f"{r['id']} carries on after a gate 0")
        for e in s.get("emotions", []): feel(e)
        if "source" in s: need(s["source"], r["id"])
        if "opened" in s: need(s["opened"]["chain"], r["id"])
        if "sense" in s: need(s["sense"], r["id"])
        for x in s.get("signals", []): need(x, r["id"])
        for k in ("sparked", "tilts", "tilted_by"):
            for l in s.get(k, []): need(l["link"], r["id"])
        if "side" in s and s["side"] not in [x["name"] for x in D[s["step"]]["sides"]]: sys.exit(f"{r['id']} names a side that does not exist")
    for s in r["steps"]:
        need(s["step"], r["id"])
        for c in s.get("closed_by", []): need(c["resource"], r["id"]); need(c["at"], r["id"])

S = {}
for f in sorted(glob.glob(os.path.join(ROOT, "states", "**", "*.json"), recursive=True)):
    s = json.load(open(f)); S[s["id"]] = s
    need(s["state"], s["id"])
    for e in s.get("resources", []): need(e["resource"], s["id"]); need(e["at"], s["id"])
    for e in s.get("needs", []): need(e["need"], s["id"]); need(e["at"], s["id"])
    for e in s.get("emotions", []):
        for k in ("emotion", "charge", "stake"):
            if k in e: need(e[k], s["id"])
    for e in s.get("skills", []): need(e["at"], s["id"])
    for e in s.get("around", []): need(e["circle"], s["id"])
    if "circle" in s: need(s["circle"], s["id"])
    for e in s.get("body", []): need(e["what"], s["id"])
    for e in s.get("influences", []): need(e["part"], s["id"]); need(e["on"], s["id"])
for f in sorted(glob.glob(os.path.join(ROOT, "records", "**", "*.json"), recursive=True)):
    r = json.load(open(f))
    if "state" in r and r["state"] not in S: sys.exit(f"{r['id']} runs in {r['state']}, which does not exist")

json.dump(I, open(os.path.join(G, "index.json"), "w"), indent=1, ensure_ascii=False)

# MAP.md
N = lambda i: D[i]["name"]
chains = [i for i, d in D.items() if d["is"] == "chain"]
kids = {}
for c in chains:
    p = D[c]["part_of"]
    if p in D and D[p]["is"] == "chain": kids.setdefault(p, []).append(c)
roots = [c for c in chains if not (D[c]["part_of"] in D and D[D[c]["part_of"]]["is"] == "chain")]
out = ["# LACE map", "", "Generated from the glossary files. Do not edit by hand.", "",
       "Every chain that stands on its own, with the chains that come off it, then the Flower, the links and the sides. Indented chains belong to the one above.", ""]
def tree(c, depth):
    d = D[c]; tag = "" if d["kind"] == "chain" else f" ({d['kind']})"
    out.append("  " * depth + f"- **{N(c)}**{tag}: " + " → ".join(N(s) for s in d["steps"]))
    for k in sorted(kids.get(c, []), key=N): tree(k, depth + 1)
for r in sorted(roots, key=lambda c: D[c]["_file"]):
    out.append(f"## {N(r)}"); out.append(""); out.append(D[r]["definition"]); out.append("")
    tree(r, 0); out.append("")
lenses = [(D[i]["_file"].split("/")[2], D[i]) for i in D if D[i]["part_of"] == "base_the_flower"]
out += ["## The Flower", "", D["base_the_flower"]["definition"] + " Each lens shows one truth, and points at the part of LACE that proves it.", ""]
for folder in sorted(set(f for f, _ in lenses)):
    out += ["### " + folder, "", "| Lens | What it shows | Proves |", "|---|---|---|"]
    for f, l in sorted((x for x in lenses if x[0] == folder), key=lambda x: x[1]["name"]):
        out.append(f"| {l['name']} | {l['definition']} | {', '.join(N(s) for s in l['shows'])} |")
    out.append("")
out += ["## Links between chains", "", "| Link | From | At step | To | Enters at | When |", "|---|---|---|---|---|---|"]
for i, d in sorted(D.items(), key=lambda x: x[1]["name"]):
    if d["is"] == "link":
        out.append(f"| {d['name']} | {N(d['from'])} | {N(d['at']) if d['at'] else ''} | {N(d['to'])} | {N(d['enters']) if d['enters'] else ''} | {N(d['when']) if d.get('when') else ''} |")
out += ["", "## Every side", "", "| Chain | Step | Side | Then |", "|---|---|---|---|"]
for i, d in sorted(D.items(), key=lambda x: x[1]["name"]):
    for sd in d.get("sides", []):
        t = sd["then"]
        out.append(f"| {', '.join(N(c) for c in d['used_in'])} | {d['name']} | {sd['name']} | {N(t) + (' (runs again)' if t in d['used_in'] else '') if t in D else t} |")
open(os.path.join(G, "MAP.md"), "w").write("\n".join(out) + "\n")
print(f"{len(D)} things, {len(chains)} chains, index.json and MAP.md written")
