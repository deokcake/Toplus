#!/usr/bin/env python3
"""python3 tools/check/show.py FIX|EFF|REF 유형 번호 [낱말,...] [DB폴더] — 문항과, 낱말이 나오는 해설 줄을 보인다."""
import json, sys, re, os
lay, t, k = sys.argv[1:4]; words = [w for w in (sys.argv[4].split(",") if len(sys.argv) > 4 and sys.argv[4] else [])]
DB = sys.argv[5] if len(sys.argv) > 5 else None
rows = {f'{r["g"]}-{r["n"]}': r for r in json.load(open(f"page/data/{t}.json"))} if t != "A" else {}
if lay == "REF": it = json.load(open("page/data/ref.json"))[k]
elif lay == "FIX": it = json.load(open(f"page/data/fix_{t}.json"))[k]
else:
    b = rows[k]; e = json.load(open(f"{DB}/t_{t}/{k}.json")).get("edit") or {}
    it = {"stem": b["stem"], "passage": b["passage"], "c": list(b["c"]), "ans": b["ans"], "expl": b.get("expl", "")}
    for f in ("stem", "passage", "ans", "expl"):
        if isinstance(e.get(f), str) and e[f] not in ("", "None"): it[f] = e[f]
    for i, v in (e.get("c") or {}).items():
        if isinstance(v, str): it["c"][int(i)] = v
print(f"== {lay} {t} {k} ans={it['ans']} | {it['stem']}")
if it.get("passage"): print("  P:", it["passage"].replace("\n", " ⏎ "))
for i, c in enumerate(it["c"]): print(f"  {'①②③④⑤'[i]} {c}")
for l in it["expl"].split("\n"):
    if not words or any(re.search(r"\b" + re.escape(w) + r"\b", l, re.I) for w in words): print("   >", l[:400])
if t != "A" and k in rows and lay != "REF":
    b = rows[k]; print("  [원안] P:", (b["passage"] or "").replace("\n", " ⏎ ")[:200], "| C:", " | ".join(b["c"])[:200])
