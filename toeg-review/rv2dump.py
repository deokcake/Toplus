#!/usr/bin/env python3
"""2차 감수용 묶음 보기: python3 rv2dump.py <급> <챕터 번호> [번호…]
원문항(수정 후) + 유형별 변형(지금 상태: db에서 고친 것 반영) + Claude 수정 예시를 한 번에 보여 준다."""
import json, sys, os, re
C = "①②③④⑤"
ref = json.load(open("page/data/ref.json", encoding="utf-8"))
idx = json.load(open("page/data/index.json", encoding="utf-8"))
rows = {t: {f'{r["g"]}-{r["n"]}': r for r in json.load(open(f"page/data/{t}.json", encoding="utf-8"))} for t in "BCDEF"}
fix = {t: json.load(open(f"page/data/fix_{t}.json", encoding="utf-8")) for t in "BCDEF"}
def db(t, k):
    p = f"rv2/db/t_{t}/{k}.json"
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None
def one(s): return s.replace("\n", " ⏎ ")
def cs(c, a):
    try: a = int(a)
    except Exception: a = 0
    return " ".join(f"{C[i]}{x}" for i, x in enumerate(c)) + f" ▶{C[a-1] if 1 <= a <= 5 else a}"
def item(tag, it, base=None, R=None):
    st = it["stem"]
    if R and st == R["stem"]: st = "=R"
    elif base and st == base["stem"]: st = "=V"
    p = it["passage"]
    if base and p == base["passage"] and p: p = "=V"
    c = cs(it["c"], it["ans"])
    if base and it["c"] == base["c"] and str(it["ans"]) == str(base["ans"]): c = "=V"
    return f"  {tag} S:{st} | P:{one(p)} | C:{c}"
g, ch = sys.argv[1], int(sys.argv[2]); only = set(sys.argv[3:])
chs = idx["grades"][g]; cd = chs[ch - 1]
print(f"##### {g}급 {cd['ch']} {cd['chn']} ({cd['nos'][0]}~{cd['nos'][-1]})")
for n in cd["nos"]:
    if only and str(n) not in only: continue
    k = f"{g}-{n}"; R = ref[k]
    print(f"\n#### {k}\nR S:{R['stem']} | P:{one(R['passage'])} | C:{cs(R['c'], R['ans'])}")
    if R.get("fixed"): print("  (원문항 수정: " + " ".join(R["fixed"]) + ")")
    for t in "BCDEF":
        V = rows[t][k]; F = fix[t].get(k); d = db(t, k)
        has_st = any(l.startswith("풀이 순서") for l in V["expl"].split("\n"))
        need = "풀이○" if (F or has_st) else "풀이×"
        print(f"{t} {V['v']} {need} | {V['why'][:140]}")
        print(item("V", V, R=R))
        cur = None
        if d and isinstance(d.get("edit"), dict):
            e = d["edit"]; cur = dict(V)
            if e.get("stem") is not None: cur["stem"] = e["stem"]
            if e.get("passage") is not None: cur["passage"] = e["passage"]
            if isinstance(e.get("c"), dict): cur["c"] = [e["c"].get(str(i), V["c"][i]) if e["c"].get(str(i)) is not None else V["c"][i] for i in range(5)]
            if e.get("ans") is not None: cur["ans"] = e["ans"]
        if F:
            print(item("F", F, base=V, R=R) + f" | {F['sum'][:110]}")
        if cur and (not F or any(cur[x] != F[x] for x in ("stem", "passage", "c")) or str(cur["ans"]) != str(F["ans"])):
            print(item("E(지금 고쳐진 상태)", cur, base=V, R=R))
        if d:
            notes = [v.get("text", "") for v in (d.get("notes") or {}).values() if isinstance(v, dict) and v.get("text")]
            vv = d.get("verdict")
            if vv or notes: print(f"  사람: 판정 {vv or '-'} / 메모 {one(' // '.join(notes))[:300]}")
