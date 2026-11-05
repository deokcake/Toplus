#!/usr/bin/env python3
"""수정 예시 조립·점검: python3 fxbuild.py [--check 급] [--write]
fx/*.py 의 F(...) 기록을 원문항 양식(발문·본문·보기·정답·해설)으로 조립하고
유형 간 중복·밑줄·정답 번호 등을 점검한다. --write 면 page/data/fix_<유형>.json 저장."""
import json, re, sys, glob, difflib, collections
import fxlib
C = "①②③④⑤"
ref = json.load(open("page/data/ref.json", encoding="utf-8"))
rows = {t: {f'{r["g"]}-{r["n"]}': r for r in json.load(open(f"page/data/{t}.json", encoding="utf-8"))} for t in "BCDEF"}

def load():
    fxlib.FIX.clear()
    for f in sorted(glob.glob("fx/*.py")):
        g = {k: getattr(fxlib, k) for k in dir(fxlib) if not k.startswith("_")}
        exec(compile(open(f, encoding="utf-8").read(), f, "exec"), g)
    return dict(fxlib.FIX)

def remap_lines(lines, order):
    """보기별 해설 줄(①~⑤로 시작)을 새 순서로 옮기고 번호를 다시 붙인다."""
    by = {}; rest_idx = []
    for i, l in enumerate(lines):
        if l[:1] in C and l[1:3] == " [": by[C.index(l[0])] = i
    if len(by) != 5: return lines
    out = list(lines); pos = sorted(by.values())
    for j, old in enumerate(order):
        out[pos[j]] = C[j] + lines[by[old]][1:]
    return out


def add_breaks(p):
    """사라진 줄바꿈 복원: b) (b) (B) ⓑ • 화자(A:, Tom:) 앞에서 줄을 바꾼다."""
    p = re.sub(r"\s+(?=(?:\(?[b-hB-H]\)|[ⓑ-ⓗ]|•|[A-Z][a-z]{0,9}:)\s)", "\n", p.strip())
    return p

def combo_notes(c, ans, k):
    parts = [re.split(r"\s+-\s+", x) for x in c]; good = parts[ans - 1]
    labels = []
    for i, g in enumerate(good):
        m = re.match(r"(\([A-E]\)|[ⓐ-ⓔ])\s*(.*)", g)
        labels.append((m.group(1), m.group(2)) if m else (["첫째", "둘째", "셋째", "넷째", "다섯째"][i] + " 빈칸", g))
    out = []
    for j, ps in enumerate(parts):
        if j + 1 == ans: out.append((k + " " if k else "") + "모든 자리가 맞으므로 정답이다."); continue
        bad = [f"{labels[i][0]} 자리는 {labels[i][1]}가 맞다" for i, x in enumerate(ps) if i < len(good) and x.strip() != good[i].strip()]
        out.append(", ".join(bad) + ". 따라서 오답이다.")
    return out

def build(key, kw):
    g, n, t = key; k = f"{g}-{n}"; R = ref[k]; V = rows[t][k]
    stem = R["stem"] if kw.get("st") == "R" else kw.get("st", V["stem"])
    passage = R["passage"] if kw.get("p") == "R" else kw.get("p", V["passage"])
    c = list(kw.get("c", V["c"]))
    ans = kw.get("a", int(V["ans"]) if str(V["ans"]).isdigit() else 0)
    lines = V["expl"].split("\n")
    if kw.get("op") == "sortc":
        order = sorted(range(len(c)), key=lambda i: int(re.search(r"\d+", c[i]).group()))
        c = [c[i] for i in order]
        if "a" not in kw: ans = order.index(ans - 1) + 1
        if "n" not in kw and "x" not in kw: lines = remap_lines(lines, order)
    if passage == "BR": passage = add_breaks(V["passage"])
    if "x" in kw: expl = kw["x"]
    elif "n" in kw:
        nn = kw["n"]
        if nn == "cnt":
            nn = [f"{kw['k']} 이 보기의 {x}{'은' if x == '없음' else '는'} 실제 개수와 일치{'한다' if i + 1 == ans else '하지 않는다'}." for i, x in enumerate(c)]
        elif nn == "combo":
            nn = combo_notes(c, ans, kw.get("k", ""))
        assert len(nn) == len(c), f"{key} 해설 {len(nn)}개/보기 {len(c)}개"
        head = lines[0] if lines and lines[0].startswith("[") else "[선택지별 구체 해설]"
        rule = kw.get("r") or next((l.split(":", 1)[1].strip() for l in lines if l.startswith("핵심 규칙")), "")
        out = [head] + (["핵심 규칙: " + rule] if rule else []) + list(kw.get("pre", []))
        if kw.get("k"):
            kk = kw["k"]
            if kk.endswith("므로"): kk += " 옳지 않은 설명이다." if "옳지 않은 설명" in nn[ans - 1] else " 정답이다."
            out.append("정답 판단: " + kk)
        out += [f"{C[i]} [{'정답' if i + 1 == ans else '오답'}] {nn[i]}" for i in range(len(c))]
        solve = next((l for l in lines if l.startswith("풀이 순서")), "")
        if solve and kw.get("solve", True): out.append(solve)
        expl = "\n".join(out)
    else:
        assert "c" not in kw or kw.get("keepx"), f"{key} 보기를 바꿨는데 해설(n)이 없음"
        expl = "\n".join(lines)
    for a_, b_ in kw.get("xr", []):
        assert a_ in expl, f"{key} 해설에 '{a_}' 없음"
        expl = expl.replace(a_, b_)
    if "n" in kw and "x" not in kw: expl = "\n".join(smooth(l) for l in expl.split("\n"))
    return {"stem": stem, "passage": passage, "c": match_sep(R["c"], c), "ans": ans, "expl": expl, "sum": kw["s"], **({"only": kw["only"]} if kw.get("only") else {})}

def match_sep(refc, c):
    """보기의 구분 기호를 원문항과 같게: ' - ' / ' – ' / ' — ', '(A): x / (B): y'"""
    dash = [" – ", " — ", " - "]
    rs = next((x for x in dash if all(x in o for o in refc)), None)
    fs = next((x for x in dash if all(x in o for o in c)), None)
    if rs and fs and rs != fs: c = [o.replace(fs, rs) for o in c]
    if all(re.match(r"\(A\): .+ / \(B\): ", o) for o in refc) and all(re.match(r"\(A\) .+ - \(B\) ", o) for o in c):
        c = [re.sub(r"\(([A-E])\) ", r"(\1): ", o).replace(" - (", " / (") for o in c]
    return c

def smooth(line):
    """보기 해설 한 문장에 '~므로 ~므로 정답/오답이다'가 겹치면 앞의 '므로'를 '고,'로 바꾼다."""
    if not re.match(r"[①-⑩] \[", line): return line
    parts = re.split(r"(?<=다\.) ", line)
    out = []
    for sent in parts:
        if re.search(r"므로 (정답|오답)이다\.$", sent) and sent.count("므로") >= 2:
            head, tail = sent.rsplit("므로", 1)
            head = re.sub(r"으?므로(?=[ (（‘'])", "고,", head)
            head = re.sub(r"고,\s*\(", "고(", head).replace("고,(", "고(")
            sent = head + "므로" + tail
        out.append(sent)
    return " ".join(out)

def nz(s):
    s = re.sub(r"</?u>", "", s).lower()
    s = re.sub(r"[①-⑤ⓐ-ⓔ]", "", s)
    return re.sub(r"[\s.,!?'\"“”‘’()\-:;]+", " ", s).strip()
def sents(s):
    return [x for x in (nz(p) for p in re.split(r"(?<=[.!?])\s+|\n|/", re.sub(r"</?u>", "", s))) if len(re.findall(r"[A-Za-z]+", x)) >= 4]

raw_kw = {}
def check(fixes, only_g=None):
    probs = []
    groups = collections.defaultdict(dict)
    for (g, n, t), it in fixes.items(): groups[(g, n)][t] = it
    for (g, n), fx in sorted(groups.items()):
        if only_g and g != only_g: continue
        k = f"{g}-{n}"; R = ref[k]
        final = {t: fx.get(t) or {"stem": rows[t][k]["stem"], "passage": rows[t][k]["passage"], "c": rows[t][k]["c"]} for t in "BCDEF"}
        def pool(it):
            out = set(nz(c) for c in it["c"] if len(nz(c).split()) >= 4 and not re.search(r"\([A-E]\)|\s-\s|[ⓐ-ⓔ],|^\d+개$|^\(?[A-Za-z]\)?(,\s*\(?[A-Za-z]\)?)+$", c))
            return out | set(sents(it["passage"]))
        refp = pool({"c": R["c"], "passage": R["passage"]})
        for t, it in fx.items():
            if it.get("only") == "expl": continue      # 문항은 변형 그대로라 점검할 것이 없다
            tag = f"{k}{t}"; V = rows[t][k]
            if not (1 <= it["ans"] <= len(it["c"])): probs.append(f"{tag} 정답 번호 {it['ans']}")
            if len(it["c"]) != len(R["c"]): probs.append(f"{tag} 보기 수 {len(it['c'])} (원문항 {len(R['c'])})")
            for fld in [it["stem"], it["passage"]] + it["c"]:
                if fld.count("<u>") != fld.count("</u>"): probs.append(f"{tag} 밑줄 짝 안 맞음: {fld[:40]}")
            if len(set(nz(c) + "|" + "".join(re.findall(r"[ⓐ-ⓩ①-⑳]", c)) for c in it["c"])) < len(it["c"]): probs.append(f"{tag} 같은 보기가 두 번")
            if R.get("inline") and any(it["passage"].count(x) != 1 for x in C): probs.append(f"{tag} 본문 속 ①~⑤ 표시 확인")
            if it["stem"] == V["stem"] and it["passage"] == V["passage"] and it["c"] == V["c"] and str(it["ans"]) == str(V["ans"]) and it["expl"] == V["expl"]:
                probs.append(f"{tag} 바뀐 것이 없음")
            kw0 = raw_kw.get((g, n, t), {})
            if it["stem"] != V["stem"] and not ({"n", "x", "okx"} & set(kw0)):
                bad = [l[:50] for l in it["expl"].split("\n") if re.search(r"지정|조건에 맞|조건과 다르|조건에는|조건만|발문이 (요구|지정|찾)|발문 조건|명시된|명시적|이 문항은 .*(요구|지정)", l) and not l.startswith("풀이 순서")]
                if bad: probs.append(f"{tag} 발문을 바꿨는데 해설에 옛 발문 흔적: {bad[:3]}")
            if kw0.get("okdup"): continue
            same_text = nz(it["passage"]) == nz(V["passage"]) and [nz(x) for x in it["c"]] == [nz(x) for x in V["c"]]
            if same_text: continue
            mine = pool(it)
            same_ref = mine & refp
            if same_ref and it["passage"] != R["passage"]: probs.append(f"{tag} 원문항과 같은 문장: {sorted(same_ref)[:2]}")
            for u in "BCDEF":
                if u == t: continue
                other = pool(final[u]); dup = mine & other
                if dup: probs.append(f"{tag} {u}유형과 같은 문장 {len(dup)}개: {sorted(dup)[:2]}")
                for a in mine - other:
                    for b in other:
                        if difflib.SequenceMatcher(None, a, b).ratio() >= 0.93: probs.append(f"{tag} {u}유형과 거의 같은 문장: {a[:40]} ≈ {b[:40]}")
    return probs

if __name__ == "__main__":
    raw = load(); raw_kw.update(raw); fixes = {}; errs = []
    for key, kw in raw.items():
        try: fixes[key] = build(key, kw)
        except Exception as e: errs.append(f"{key} 조립 오류: {e}")
    # 2차 감수(rv2): 문항마다 다른 ‘풀이 순서’를 해설 끝에 넣는다
    import rv2build, explfmt
    EX2, _ = rv2build.load()
    for (g, n, t), it in fixes.items():
        try:
            st = rv2build.steps_for(EX2[(g, n)], t, it)
            assert st, "풀이 순서 칸 없음"
            it["expl"] = explfmt.restructure(rv2build.set_steps(it["expl"], st), it["ans"], EX2[(g, n)]["r"]).replace("일치한지 않는다", "일치하지 않는다")
        except Exception as e: errs.append(f"{(g, n, t)} 풀이 순서: {e}")
    # 판정이 적합이라 수정 예시가 없는 변형 문항: 문항은 그대로 두고 해설만 같은 짜임(문항별 풀이 순서 포함)으로 고친 예시를 만든다
    nexpl = 0
    for t in "BCDEF":
        for k, V in rows[t].items():
            g, n = map(int, k.split("-"))
            if (g, n, t) in fixes: continue
            it = {"stem": V["stem"], "passage": V["passage"], "c": list(V["c"]), "ans": int(V["ans"]), "expl": V["expl"]}
            try:
                st = rv2build.steps_for(EX2[(g, n)], t, it)
                assert st, "풀이 순서 칸 없음"
            except Exception as e: errs.append(f"{(g, n, t)} 풀이 순서: {e}"); continue
            it["expl"] = explfmt.restructure(rv2build.set_steps(V["expl"], st), it["ans"], EX2[(g, n)]["r"]).replace("일치한지 않는다", "일치하지 않는다")
            it["sum"] = "문항(발문·본문·보기·정답)은 그대로 두고, 해설을 ‘핵심 규칙 → 풀이 순서 → 문장별 판정 → 정답 판단 → 선택지 분석’ 순서로 다시 짜고 이 문항에 맞는 풀이 순서를 넣었다."
            it["only"] = "expl"
            fixes[(g, n, t)] = it; raw_kw[(g, n, t)] = {"okdup": True}; nexpl += 1
    # 본문에 (A)·(B) 표시가 없는 두 빈칸 문항: 해설의 (A)·(B)를 ‘첫째 빈칸’·‘둘째 빈칸’으로 바꾼다
    for it in fixes.values(): it["expl"] = explfmt.unlabel(it)
    only = int(sys.argv[sys.argv.index("--check") + 1]) if "--check" in sys.argv else None
    probs = errs + check(fixes, only)
    need = {(r["g"], r["n"], t) for t in "BCDEF" for r in rows[t].values() if r["v"] != "적합"}
    done = need & set(fixes)
    print(f"수정 예시 {len(fixes)}개 (대상 {len(need)}개 중 {len(done)}개), 대상 밖 {len(set(fixes) - need)}개 (그중 해설만 고친 예시 {nexpl}개)")
    by_g = collections.Counter(g for g, n, t in done); tot = collections.Counter(g for g, n, t in need)
    print("급별:", " ".join(f"{g}급 {by_g[g]}/{tot[g]}" for g in sorted(tot)))
    for p in probs: print(" !", p)
    if "--write" in sys.argv:
        for t in "BCDEF":
            out = {f"{g}-{n}": it for (g, n, tt), it in sorted(fixes.items()) if tt == t}
            json.dump(out, open(f"page/data/fix_{t}.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
        print("저장: page/data/fix_B..F.json")
