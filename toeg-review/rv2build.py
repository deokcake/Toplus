#!/usr/bin/env python3
"""2차 감수 기록(rv2/g*.py) 조립·점검
  python3 rv2build.py --check <급> <챕터>   그 챕터의 빠진 문항·칸을 알려 준다
  python3 rv2build.py --show <급> <번호>     조립된 원문항 해설과 유형별 풀이 순서를 보여 준다
  python3 rv2build.py --write               rv2/out/ref_expl.json, steps.json, review2.json 저장"""
import json, re, glob, sys, os
import rv2lib
C = "①②③④⑤"
def load():
    rv2lib.EX.clear(); rv2lib.REV.clear()
    for f in sorted(glob.glob("rv2/g*.py")):
        exec(compile(open(f, encoding="utf-8").read(), f, "exec"), {"X": rv2lib.X, "RV": rv2lib.RV, "EX": rv2lib.EX, "REV": rv2lib.REV})
    return rv2lib.EX, rv2lib.REV
def plain(s): return re.sub(r"</?u>", "", s).strip()
def steps_for(kw, who, it):
    """who = 'R' 또는 유형. it = 그 문항(dict: c, ans). 칸이 없으면 None."""
    tpl = kw.get("st"); slots = kw.get(who)
    if isinstance(slots, str):
        # 문자열 한 개: 틀에 칸이 하나({0})면 그 칸의 값, ①로 시작하면 그 문항만 통째로 다른 풀이 순서
        ns = len(set(re.findall(r"\{(\d+)\}", tpl))) if tpl is not None else -1
        if "→ ②" in slots or tpl is None: tpl, slots = slots, ()      # 통째로 다른 풀이 순서
        elif ns == 1: slots = (slots,)                                 # 칸 하나의 값
        elif ns == 0 and not slots.strip(): slots = ()                 # 칸이 없는 틀
        else: raise AssertionError(f"문자열 칸({slots[:20]})을 틀(칸 {ns}개)에 넣을 수 없음")
    if tpl is None: return None
    nslot = len(set(re.findall(r"\{(\d+)\}", tpl)))
    if slots is None:
        if nslot: return None
        slots = ()
    if not isinstance(slots, (tuple, list)): slots = (slots,)
    assert len(slots) == nslot, f"칸 수 {len(slots)} ≠ 틀의 칸 {nslot}"
    ans = int(it["ans"]); a = plain(it["c"][ans - 1])
    return "풀이 순서: " + josa(tpl.format(*slots, a=a, n=C[ans - 1]))
_JOSA = [(r"([②④⑤])이(?=[\s,.])", r"\1가"), (r"([①③])가(?=[\s,.])", r"\1이"), (r"([②④⑤])은(?=[\s,.])", r"\1는"), (r"([①③])는(?=[\s,.])", r"\1은"),
         (r"([②④⑤])을(?=[\s,.])", r"\1를"), (r"([①③])를(?=[\s,.])", r"\1을"), (r"([②④⑤])과(?=[\s,.])", r"\1와"), (r"([①③])와(?=[\s,.])", r"\1과"),
         (r"③로(?=[\s,.])", "③으로"), (r"([①②④⑤])으로(?=[\s,.])", r"\1로")]
def josa(s):
    """정답 번호({n}) 뒤의 조사를 번호 읽는 소리(일·이·삼·사·오)에 맞춘다."""
    for p, r in _JOSA: s = re.sub(p, r, s)
    # 단계 번호 바로 뒤에 보기 번호가 오면(‘③ ④만 …’) 헷갈리므로 ‘선택지’를 붙인다
    return re.sub(r"((?:^|→ )[①-⑤] )(?=[①-⑤])", r"\1선택지 ", s)
def note(x, right):
    x = x.strip()
    if x.endswith("므로") or not re.search(r"[.)]$|다$", x): return x + (" 정답이다." if right else " 오답이다.")
    return x if not x.endswith("다") else x + "."
def ref_expl(kw, R):
    ans = int(R["ans"]); nn = kw["n"]
    assert len(nn) == len(R["c"]), f"해설 {len(nn)}개 / 보기 {len(R['c'])}개"
    out = ["[선택지별 구체 해설]", "핵심 규칙: " + kw["r"]] + list(kw.get("pre", []))
    if kw.get("k"): out.append("정답 판단: " + kw["k"])
    out += [f"{C[i]} [{'정답' if i + 1 == ans else '오답'}] {note(nn[i], i + 1 == ans)}" for i in range(len(nn))]
    st = steps_for(kw, "R", R)
    assert st, "원문항 풀이 순서 칸(R) 없음"
    out.append(st)
    import explfmt
    return explfmt.restructure("\n".join(out), ans)
def set_steps(expl, st):
    lines = [l for l in expl.split("\n") if not l.startswith("풀이 순서")]
    return "\n".join(lines + [st])
def has_steps(expl): return any(l.startswith("풀이 순서") for l in expl.split("\n"))

if __name__ == "__main__":
    EX, REV = load()
    ref = json.load(open("page/data/ref.json", encoding="utf-8"))
    idx = json.load(open("page/data/index.json", encoding="utf-8"))
    rows = {t: {f'{r["g"]}-{r["n"]}': r for r in json.load(open(f"page/data/{t}.json", encoding="utf-8"))} for t in "BCDEF"}
    fix = {t: json.load(open(f"page/data/fix_{t}.json", encoding="utf-8")) for t in "BCDEF"}
    def final(t, k): return fix[t].get(k) or rows[t][k]
    def needs(t, k): return k in fix[t] or has_steps(rows[t][k]["expl"])
    probs = []
    def chk(g, n):
        k = f"{g}-{n}"; kw = EX.get((g, n))
        if not kw: probs.append(f"{k} 기록 없음"); return
        try: ref_expl(kw, ref[k])
        except Exception as e: probs.append(f"{k} 원문항 해설: {e}")
        for t in "BCDEF":
            if not needs(t, k): continue
            try:
                if not steps_for(kw, t, final(t, k)): probs.append(f"{k}{t} 풀이 순서 칸 없음")
            except Exception as e: probs.append(f"{k}{t} 풀이 순서: {e}")
    if "--check" in sys.argv:
        i = sys.argv.index("--check"); g = sys.argv[i + 1]; ch = int(sys.argv[i + 2])
        nos = idx["grades"][g][ch - 1]["nos"]
        for n in nos: chk(int(g), n)
        print(f"{g}급 CH{ch}: {len(nos)}문항, 문제 {len(probs)}건")
        for p in probs: print(" !", p)
    elif "--show" in sys.argv:
        i = sys.argv.index("--show"); g = int(sys.argv[i + 1]); n = int(sys.argv[i + 2]); k = f"{g}-{n}"
        print(ref_expl(EX[(g, n)], ref[k]))
        for t in "BCDEF":
            if needs(t, k): print(t, steps_for(EX[(g, n)], t, final(t, k)))
    else:
        done = sorted(EX)
        for g, n in done: chk(g, n)
        print(f"기록 {len(done)}/{len(ref)}문항, 문제 {len(probs)}건, 재감수 기록 {len(REV)}건")
        for p in probs[:40]: print(" !", p)
        if "--write" in sys.argv:
            os.makedirs("rv2/out", exist_ok=True)
            json.dump({f"{g}-{n}": ref_expl(EX[(g, n)], ref[f"{g}-{n}"]) for g, n in done}, open("rv2/out/ref_expl.json", "w", encoding="utf-8"), ensure_ascii=False)
            json.dump([{"key": f"{g}-{n}", "type": t, **{a: b for a, b in r.items()}} for (g, n, t), rs in sorted(REV.items()) for r in rs], open("rv2/out/review2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print("저장: rv2/out/ref_expl.json, review2.json")
