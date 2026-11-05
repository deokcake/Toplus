#!/usr/bin/env python3
"""문장별 판정 점검: 지문의 문장 기호(a)~, ⓐ~, (A)~, (가)~, ㉠~)가 판정에 다 있는지, 옳음/틀림이 정답(조합·개수)과 맞는지.
사용: python3 tools/check/judge_check.py <DB 스냅샷 폴더> → 결과 줄"""
import json, re, sys, os, glob
sys.path.insert(0, "."); import explfmt
DB = sys.argv[1]; C5 = "①②③④⑤"
LAB = r"(?:[ⓐ-ⓗ]|㉠|㉡|㉢|㉣|㉤|\([A-H]\)|\([가-아]\)|[a-h]\)|\([a-h]\))"
def norm(l):
    l = l.strip(); m = re.match(r"\(([A-Ha-h가-아])\)|([a-h])\)", l)
    return (m[1] or m[2]) if m else l
def labels_in_passage(p):
    out = []
    for line in (p or "").split("\n"):
        m = re.match(r"^\s*(?:<보기>\s*)?(" + LAB + r")\s", line)
        if m: out.append(norm(m[1]))
    return out
VERD = [(r"옳음|옳다|맞음|^O\b|○|\bO\.", True), (r"틀림|틀리다|어색|^X\b|×|\bX\.", False)]
def verdicts(judge):
    out = {}
    txt = " ".join(re.sub(r"^문장별 판정:\s*", "", l.strip()) for l in judge)
    for m in re.finditer(r"(?:^|(?<=[\s.。]))(" + LAB + r")\s*[:.]?\s*(옳음|옳다|맞음|맞다|틀림|틀리다|어색함|어색하다|어색|O|X|○|×)?", txt):
        lab = norm(m[1]); w = m[2]
        if lab in out and out[lab] is not None: continue
        out[lab] = None if not w else (w in ("옳음", "옳다", "맞음", "맞다", "O", "○"))
    return out
def check(it):
    res = []; p = explfmt.parse(it.get("expl", "")); labs = labels_in_passage(it.get("passage", ""))
    if len(labs) < 3: return res
    V = verdicts(p["judge"])
    if not p["judge"]: return [("판정없음", ",".join(labs))]
    miss = [l for l in labs if l not in V]
    if miss: res.append(("판정빠짐", ",".join(miss)))
    if any(v is None for v in V.values()): res.append(("판정모호", ",".join(k for k, v in V.items() if v is None)))
    a = int(it["ans"]) if str(it["ans"]).isdigit() else 0
    if not a: return res
    st = it.get("stem", ""); ac = re.sub(r"</?u>", "", it["c"][a - 1]).strip()
    want_ok = bool(re.search(r"옳은|올바른|알맞은|바른|적절한", st)) and not re.search(r"옳지 않은|틀린|어색한|잘못된|않은", st)
    want_bad = bool(re.search(r"틀린|어색한|잘못된|옳지 않은|올바르지 않은|바르지 않은", st))
    oks = sorted(k for k, v in V.items() if v is True); bads = sorted(k for k, v in V.items() if v is False)
    m = re.fullmatch(r"(\d)개", ac)
    if m:
        n = int(m[1])
        if want_bad and len(bads) != n and not miss: res.append(("개수", f"틀림 {len(bads)} / 정답 {ac}"))
        elif want_ok and not want_bad and len(oks) != n and not miss: res.append(("개수", f"옳음 {len(oks)} / 정답 {ac}"))
    elif re.fullmatch(r"[\s,ⓐ-ⓗ㉠-㉤a-hA-H()가-아]+", ac) and "," in ac:
        S = sorted(norm(x) for x in re.findall(LAB.replace(r"[a-h]\)|", "") + r"|[a-h](?=,|$)|[A-H](?=,|$)", ac.replace(" ", "")))
        S = sorted(set(norm(x.strip()) for x in ac.split(",")))
        tgt = bads if want_bad else oks
        if S and tgt and S != sorted(tgt) and not miss: res.append(("조합", f"정답 {ac} / 판정 {'틀림' if want_bad else '옳음'} {','.join(tgt)}"))
    return res
rows = {t: {f'{r["g"]}-{r["n"]}': r for r in json.load(open(f"page/data/{t}.json"))} for t in "BCDEF"}
fix = {t: json.load(open(f"page/data/fix_{t}.json")) for t in "BCDEF"}
ref = json.load(open("page/data/ref.json"))
for k, r in ref.items():
    for c, d in check(r): print(f"REF A {k} {c} {d}")
for t in "BCDEF":
    for k, it in fix[t].items():
        for c, d in check(it): print(f"FIX {t} {k} {c} {d}")
    for f in glob.glob(f"{DB}/t_{t}/*.json"):
        k = os.path.basename(f)[:-5]; dd = json.load(open(f)); e = dd.get("edit")
        if not isinstance(e, dict) or not isinstance(e.get("expl"), str): continue
        b = rows[t][k]; it = {"stem": b["stem"], "passage": b["passage"], "c": list(b["c"]), "ans": b["ans"], "expl": e["expl"]}
        for ff in ("stem", "passage", "ans"):
            if isinstance(e.get(ff), str) and e[ff] not in ("", "None"): it[ff] = e[ff]
        for i, v in (e.get("c") or {}).items():
            if isinstance(v, str): it["c"][int(i)] = v
        for c, d in check(it): print(f"EFF {t} {k} {c} {d} done={bool(dd.get('done'))}")
