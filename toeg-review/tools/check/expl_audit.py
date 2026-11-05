#!/usr/bin/env python3
"""해설 전수 점검: 문항(발문·지문·보기·정답)과 해설이 맞는지 본다.
사용: python3 tools/check/expl_audit.py <DB 스냅샷 폴더(t_B..t_F 하위)> [<예전 게시본 data 폴더> ...]
대상 REF(원문항), FIX(Claude 수정 예시, page/data/fix_*.json), EFF(DB edit을 덮어쓴 문항)."""
import json, re, sys, os, glob, collections
sys.path.insert(0, "."); import explfmt
C5 = "①②③④⑤"; L5 = "ⓐⓑⓒⓓⓔⓕ"
DB = sys.argv[1]; OLDDIRS = sys.argv[2:]
STOP = set("""a an the and or but not to of in on at for by with from as is are am was were be been being do does did have has had will would can could shall should may might must
it its this that these those there here he she they we you i me him her them us my your his our their who what which when where why how whose whom yes no than then so if also too very
much many more most less few little some any all both each every either neither nor only just ing ed ly er est s es""".split())
def plain(s): return re.sub(r"\s+", " ", re.sub(r"</?u>", "", s or "")).replace("’", "'").replace("‘", "'").strip()
def toks(s): return set(w.lower().strip("'-") for w in re.findall(r"[A-Za-z][A-Za-z'’-]+", plain(s)))
def itext(it): return plain(" ".join([it.get("stem", ""), it.get("passage", ""), " ".join(it.get("c", []))]))
def blank_rx(line):
    l = plain(line)
    l = re.sub(r"\((?:\s*[A-E]\s*)?\)\s*_{2,}|_{2,}|\(\s*[A-E]?\s*\)", "\x00", l)
    parts = [re.escape(x) for x in l.split("\x00")]
    return re.compile(r"(?:.{0,60}?)".join(parts).replace(r"\ ", r"\s*"), re.I) if len(parts) > 1 else None
def quote_ok(q, it):
    q = plain(q).strip(" .!?,"); txt = itext(it).lower()
    if not q or q.lower() in txt: return True
    for line in re.split(r"\n|(?<=[.!?])\s+", it.get("passage", "") or ""):
        rx = blank_rx(line)
        if rx and rx.search(q): return True
    return False
QUOTES = re.compile(r"‘([^’]{3,}?)’|“([^”]{3,}?)”|\"([^\"]{3,}?)\"|(?<![A-Za-z])'([A-Za-z][^'\n]{6,}?)'(?![A-Za-z])")
def quotes(s):
    out = []
    for m in QUOTES.finditer(s or ""):
        q = next(x for x in m.groups() if x)
        if re.search(r"[A-Za-z]", q) and not re.search(r"[가-힣]", q) and len(q.split()) >= 2: out.append(q)
    return out
def check(it, olds, label):
    """olds: 예전 판 문항 dict 목록. 결과: [(강도, 코드, 내용)]"""
    out = []; ex = it.get("expl", "") or ""
    if not ex.strip(): return [(3, "해설없음", "")]
    p = explfmt.parse(ex); ans = str(it.get("ans", "")); a = int(ans) if ans.isdigit() else 0
    txt = itext(it); cur = toks(txt)
    # 1) 선택지 해설과 정답 표시
    nopt = sum(1 for o in p["opts"] if o)
    if nopt and nopt < 5: out.append((2, "선택지해설빠짐", f"{nopt}개"))
    for i, o in enumerate(p["opts"]):
        if not o: continue
        tag = re.match(r"\[(정답|오답)\]", o[0])
        if tag and a and (tag[1] == "정답") != (i + 1 == a): out.append((3, "정답표시", f"{C5[i]} {tag[1]} / 정답 {C5[a-1]}"))
        body = " ".join(o)
        if a and re.search(r"(?<!오)정답이다\.?$|정답입니다", body) and i + 1 != a and "옳지 않은" not in body: out.append((2, "보기해설정답말", f"{C5[i]}"))
    # 2) 정답 판단·풀이 순서 끝의 번호
    for sec in ("key", "steps"):
        s = " ".join(p[sec])
        for m in re.finditer(r"정답은\s*(?:선택지\s*)?([①-⑤])", s):
            if a and C5.index(m[1]) + 1 != a: out.append((3, "번호어긋남", f"{sec}: 정답은 {m[1]} / 실제 {C5[a-1]}"))
    # 3) 예전 판에만 있던 낱말·인용
    old = set()
    for o in olds: old |= toks(itext(o))
    body = "\n".join([" ".join(p["steps"]), "\n".join(p["judge"]), " ".join(p["key"])] + [" ".join(o) for o in p["opts"]])
    used = toks(body)
    stale = sorted(w for w in used - cur if w in old and w not in STOP and len(w) >= 3)
    if stale: out.append((2, "예전낱말", ", ".join(stale[:12])))
    for q in quotes(body):
        if not quote_ok(q, it):
            inold = any(quote_ok(q, o) for o in olds)
            out.append((3 if inold else 1, "인용(예전판)" if inold else "인용없음", q[:80]))
    # 4) 문장별 판정 기호가 지문에 있는지
    pas = plain(it.get("passage", ""))
    for l in p["judge"]:
        m = re.match(r"^(?:문장별 판정:\s*)?([ⓐ-ⓕ]|\([가-바]\)|\([A-F]\))", l)
        if m and m[1] not in pas: out.append((2, "판정기호없음", m[1]))
    # 5) 개수형: 정답 판단의 개수와 정답 보기
    if a and re.fullmatch(r"\d개|없음", plain(it["c"][a - 1])):
        k = " ".join(p["key"]); m = re.search(r"(\d)개", k)
        if m and m[1] + "개" != plain(it["c"][a - 1]): out.append((3, "개수어긋남", f"판단 {m[1]}개 / 정답 {it['c'][a-1]}"))
    return out

ref = json.load(open("page/data/ref.json", encoding="utf-8"))
rows = {t: {f'{r["g"]}-{r["n"]}': r for r in json.load(open(f"page/data/{t}.json", encoding="utf-8"))} for t in "BCDEF"}
fix = {t: json.load(open(f"page/data/fix_{t}.json", encoding="utf-8")) for t in "BCDEF"}
olds_fix = {t: [json.load(open(f"{d}/fix_{t}.json", encoding="utf-8")) for d in OLDDIRS if os.path.exists(f"{d}/fix_{t}.json")] for t in "BCDEF"}
db = {t: {} for t in "BCDEF"}
for t in "BCDEF":
    for f in glob.glob(f"{DB}/t_{t}/*.json"): db[t][os.path.basename(f)[:-5]] = json.load(open(f, encoding="utf-8"))
def merged(base, e):
    out = {"stem": base["stem"], "passage": base["passage"], "c": list(base["c"]), "ans": str(base["ans"]), "expl": base.get("expl", "")}
    for k in ("stem", "passage", "ans", "expl"):
        if isinstance(e.get(k), str) and e.get(k) not in ("", "None"): out[k] = e[k]
    ec = e.get("c")
    if isinstance(ec, dict):
        for i, v in ec.items():
            if isinstance(v, str) and 0 <= int(i) < 5: out["c"][int(i)] = v
    return out
res = []
for k, r in ref.items():
    olds = [r["orig"]] if isinstance(r.get("orig"), dict) else []
    for f in check(r, olds, "REF"): res.append(("REF", "A", k, None) + f)
for t in "BCDEF":
    for k, it in fix[t].items():
        olds = [rows[t][k]] + [o[k] for o in olds_fix[t] if k in o and o[k] != it]
        for f in check(it, olds, "FIX"): res.append(("FIX", t, k, None) + f)
    for k, d in db[t].items():
        e = d.get("edit")
        if not isinstance(e, dict) or not any(isinstance(v, (str, dict)) for v in e.values()): continue
        it = merged(rows[t][k], e)
        olds = [rows[t][k], fix[t].get(k) or {}] + [o[k] for o in olds_fix[t] if k in o]
        olds = [o for o in olds if o and (o.get("passage"), o.get("c")) != (it["passage"], it["c"])]
        for f in check(it, olds, "EFF"): res.append(("EFF", t, k, bool(d.get("done"))) + f)
json.dump(res, open(os.environ.get("OUT", "/dev/stdout") if os.environ.get("OUT") else "expl_audit_result.json", "w"), ensure_ascii=False)
cnt = collections.Counter((x[0], x[4], x[5]) for x in res)
for kk, v in sorted(cnt.items()): print(kk, v)
print("문항 수(층·유형·번호):", len(set(x[:3] for x in res)), "강 3:", len(set(x[:3] for x in res if x[4] == 3)))
