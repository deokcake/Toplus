#!/usr/bin/env python3
"""감수용 압축 출력: python3 dump.py <src> <급> <시작번호> <끝번호>"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
src, g, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
sys.argv = ["x", src]
import screen
ref, var = screen.load()
flags = {r["id"]: r["flags"] for r in json.load(open(Path(src) / "screen.json", encoding="utf-8"))}
C = "①②③④⑤"
for n in range(a, b + 1):
    r = ref[(g, n)]
    print(f"### {g}급 {n} REF: {r['stem']}")
    if r["passage"]: print("  P:", r["passage"].replace("\n", " / "))
    if not r.get("inline") or len(r["choices"]) == 5 and r["passage"].count("①") == 0:
        print("  ", " ".join(f"{C[i]}{c}" for i, c in enumerate(r["choices"])), "| 답", C[r["answer"]-1])
    else:
        print("   | 답", C[r["answer"]-1])
    for t in "BCDEF":
        v = var[(t, g, n)]
        st = "" if v["stem"] == r["stem"] else " S:" + v["stem"]
        fl = [f"{f['code']}{f['sev']}:{f['msg'][:48]}" for f in flags[f"{g}급-{n:03d}-{t}"] if f["sev"] not in ("note",) and f["code"] != "A1"]
        print(f" [{t}]{st}" + (f"  ⚑ {' | '.join(fl)}" if fl else ""))
        if v["passage"]: print("  P:", v["passage"].replace("\n", " / "))
        inline_v = v["passage"].count("①") > 0 and not any(len(c.split()) > 3 for c in v["choices"])
        if not inline_v:
            print("  ", " ".join(f"{C[i]}{c}" for i, c in enumerate(v["choices"])), "| 답", C[v["answer"]-1] if v["answer"] else v["answer_raw"])
        else:
            print("   | 답", C[v["answer"]-1] if v["answer"] else v["answer_raw"])
