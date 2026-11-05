#!/usr/bin/env python3
"""문항과 해설(핵심 규칙 빼고)을 짧게 보인다. python3 tools/check/compact.py 키목록파일(json: ["3-6E",...])"""
import json, sys, re
sys.path.insert(0, "."); import explfmt
keys = json.load(open(sys.argv[1])); C5 = "①②③④⑤"
fix = {t: json.load(open(f"page/data/fix_{t}.json")) for t in "BCDEF"}
rows = {t: {f'{r["g"]}-{r["n"]}': r for r in json.load(open(f"page/data/{t}.json"))} for t in "BCDEF"}
def pl(s): return re.sub(r"\s+", " ", re.sub(r"</?u>", "_", s or "")).strip()
for kk in keys:
    t, k = kk[-1], kk[:-1]; it = fix[t][k]; p = explfmt.parse(it["expl"])
    print(f"#### {kk} ans={it['ans']} | {pl(it['stem'])[:70]}")
    if it["passage"]: print("  P:", pl(it["passage"].replace("\n", " / "))[:900])
    print("  C:", " | ".join(f"{C5[i]}{pl(c)}" for i, c in enumerate(it["c"]))[:900])
    if p["judge"]: print("  J:", " || ".join(pl(x) for x in p["judge"])[:1600])
    print("  K:", pl(" ".join(p["key"]))[:300])
    for i, o in enumerate(p["opts"]): print(f"  {C5[i]}", pl(" ".join(o))[:260])
