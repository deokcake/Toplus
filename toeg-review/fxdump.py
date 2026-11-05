#!/usr/bin/env python3
"""수정 예시 작성용 출력: python3 fxdump.py <급> <시작> <끝>"""
import json, sys
g, a, b = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
C = "①②③④⑤"
ref = json.load(open("page/data/ref.json", encoding="utf-8"))
rows = {t: {f'{r["g"]}-{r["n"]}': r for r in json.load(open(f"page/data/{t}.json", encoding="utf-8"))} for t in "BCDEF"}
def ch(cs, ans):
    try: ai = int(ans)
    except: ai = 0
    return " ".join(f"{C[i]}{c}" for i, c in enumerate(cs)) + f" | 답{C[ai-1] if 1 <= ai <= 5 else ans}"
def pl(p): return p.replace("\n", " ⏎ ")
for n in range(a, b + 1):
    k = f"{g}-{n}"; R = ref[k]
    need = [t for t in "BCDEF" if rows[t][k]["v"] != "적합"]
    print(f"### {k} REF: {R['stem']}" + (f"  ※원문항 확인: {R['note']}" if R.get("note") else ""))
    if R["passage"]: print("  P:", pl(R["passage"]))
    print("  ", ch(R["c"], R["ans"]))
    if not need: print("  (모두 적합)"); continue
    for t in "BCDEF":
        r = rows[t][k]; ok = r["v"] == "적합"
        st = "" if r["stem"] == R["stem"] else " S:" + r["stem"]
        if ok:
            print(f" [{t}] 적합{st}")
            if r["passage"]: print("   P:", pl(r["passage"]))
            print("   ", ch(r["c"], r["ans"])); continue
        print(f" [{t}] ★{r['v']}{st}")
        if r["passage"]: print("   P:", pl(r["passage"]))
        print("   ", ch(r["c"], r["ans"]))
        print("   WHY:", r["why"][:260]); print("   FIX:", r["fix"][:160])
        lines = r["expl"].split("\n")
        rule = next((l for l in lines if l.startswith("핵심 규칙")), "")
        extra = [l.split(":")[0] for l in lines if ":" in l[:10] and not l.startswith(("핵심 규칙", "풀이 순서"))]
        print("   RULE:", rule[:150], ("| 기타:" + ",".join(dict.fromkeys(extra))) if extra else "")
