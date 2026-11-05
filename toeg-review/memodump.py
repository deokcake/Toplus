#!/usr/bin/env python3
"""사용자 메모가 있는 문항 덤프: 원문항, B(공유 저장소 반영), B 수정 예시, C~F 최종(예시 있으면 예시)"""
import json, sys, os, glob, re
S = sys.argv[1]; keys = sys.argv[2:]
ref = json.load(open("page/data/ref.json", encoding="utf-8"))
rows = {t: {f'{r["g"]}-{r["n"]}': r for r in json.load(open(f"page/data/{t}.json", encoding="utf-8"))} for t in "BCDEF"}
fix = {t: json.load(open(f"page/data/fix_{t}.json", encoding="utf-8")) for t in "BCDEF"}
C = "①②③④⑤"
def fmt(it, expl=False):
    s = "S:" + it["stem"].replace("\n", " ⏎ ")
    if it.get("passage"): s += "\n   P:" + it["passage"].replace("\n", " ⏎ ")
    s += "\n   C:" + " ".join(f"{C[i]}{c}" for i, c in enumerate(it["c"])) + f" ▶{it['ans']}"
    if expl and it.get("expl"): s += "\n   X:" + it["expl"].replace("\n", " / ")[:900]
    return s
for k in keys:
    d = json.load(open(f"{S}/db3/t_B/{k}.json", encoding="utf-8")); ed = d.get("edit") or {}; r = rows["B"][k]
    def cat(i):
        c = ed.get("c"); v = c[i] if isinstance(c, list) and i < len(c) else (c.get(str(i)) if isinstance(c, dict) else None)
        return v if isinstance(v, str) else None
    eff = {"stem": ed.get("stem") if isinstance(ed.get("stem"), str) else r["stem"], "passage": ed.get("passage") if isinstance(ed.get("passage"), str) else r["passage"],
           "c": [cat(i) if cat(i) is not None else r["c"][i] for i in range(5)], "ans": ed.get("ans") if isinstance(ed.get("ans"), str) else r["ans"], "expl": ed.get("expl") if isinstance(ed.get("expl"), str) else r["expl"]}
    R = ref[k]
    print(f"\n#### {k}  [{r['ch']} {r['chn']}]  판정:{d.get('verdict')} 확인:{bool(d.get('done'))}")
    for u, n in (d.get("notes") or {}).items():
        if isinstance(n, dict) and n.get("text"): print("   메모:", n["text"].replace("\n", " / "))
    print("R  " + fmt(R, True))
    fb = fix["B"].get(k)
    same = fb and all(eff[f] == fb[f] for f in ("stem", "passage", "c")) and str(eff["ans"]) == str(fb["ans"])
    print("B현재 " + fmt(eff, "--x" in sys.argv) + ("   (=B예시)" if same else ""))
    if fb and not same: print("B예시 " + fmt(fb) + "\n   요지:" + fb["sum"][:200])
    for t in "CDEF":
        f = fix[t].get(k); v = rows[t][k]; it = f if f and f.get("only") != "expl" else v
        print(f"{t}{'예시' if it is f else '변형'} " + fmt(it))
