#!/usr/bin/env python3
"""풀이 순서·보기 해설 점검(원문항 + B~F 수정 예시). 결과: 키, 층, 근거, 풀이 순서
사용: python3 tools/check/steps_audit.py <DB 스냅샷 폴더>"""
import json, re, sys, os, glob
sys.path.insert(0, "."); import rv2build, explfmt
DB = sys.argv[1]
EX, _ = rv2build.load()
C5 = "①②③④⑤"; L5 = "ⓐⓑⓒⓓⓔⓕ"
STOP = set("""a an the and or but not to of in on at for by with from as is are am was were be been being do does did have has had will would can could shall should may might must
it its this that these those there here he she they we you i me him her them us my your his our their who what which when where why how whose whom yes no than then so if also too very
much many more most less few little some any all both each every either neither nor only just ing ed ly""".split())
done = {}
for t in "BCDEF":
    for f in glob.glob(f"{DB}/t_{t}/*.json"):
        done[(os.path.basename(f)[:-5], t)] = bool(json.load(open(f)).get("done"))
def plain(s): return re.sub(r"\s+", " ", re.sub(r"</?u>", "", s or "")).replace("’", "'").lower()
def lines_of(p):
    out = {}
    for l in (p or "").split("\n"):
        l2 = l.strip()
        m = re.match(r"^([ⓐ-ⓕ]|\([A-F]\)|\([가-바]\)|[a-f][.)]|㉠|㉡|㉢|㉣|㉤)\s*", l2)
        if m: out[m[1].strip("().")] = plain(l2)
    return out
def audit(key, layer, t, it):
    out = []
    g, n = map(int, key.split("-")); ex = EX.get((g, n)) or {}
    ans = int(it["ans"]) if str(it["ans"]).isdigit() else 0
    lines = it.get("expl", "").split("\n")
    st = next((l for l in lines if l.startswith("풀이 순서")), "")
    rest = "\n".join(l for l in lines if not l.startswith("풀이 순서"))
    text = plain(" ".join([it.get("stem", ""), it.get("passage", ""), " ".join(it.get("c", []))]))
    alltxt = text + " " + plain(rest)
    opts = [plain(c) for c in it.get("c", [])]; pl = lines_of(it.get("passage", ""))
    # 1) 칸 낱말
    sl = ex.get(t if layer != "REF" else "R")
    if sl is not None and st:
        vals = [sl] if isinstance(sl, str) else list(sl)
        ws = set(w.lower().strip("'-") for v in vals for w in re.findall(r"[A-Za-z][A-Za-z'’-]+", str(v)))
        miss = sorted(w for w in ws if w not in STOP and len(w) >= 3 and w not in alltxt and w.rstrip("s") not in alltxt)
        if miss: out.append(("칸낱말", ",".join(miss)))
    body = re.sub(r"(풀이 순서: |→ )[①-⑤] ", r"\1", st)
    body2 = re.sub(r"정답은 [①-⑤].*$", "", body)
    # 2) 보기 번호 뒤 영어가 그 보기에 있는지
    for m in re.finditer(r"(?:선택지 )?([①-⑤])(?:[은는이가의]|만|도)?\s*([^①-⑤→.]{0,60})", body2):
        i = C5.index(m[1])
        if i >= len(opts): continue
        ws = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'’]+", m[2]) if w.lower() not in STOP]
        if ws and not any(w in opts[i] for w in ws) and not any(w in plain(it.get("passage", "")) for w in ws):
            out.append(("보기번호", f"{m[1]}:{'/'.join(ws)}"))
        if ans and C5.index(m[1]) + 1 != ans and re.match(r"(?:만|[은는이가] [^.]{0,40}?(?:맞다|옳다|바르게|정답))", m[2] if m[2] else ""):
            out.append(("번호어긋남", m[1]))
    # 3) 지문 기호 뒤 영어가 그 문장에 있는지
    for m in re.finditer(r"(?<![A-Za-z])([ⓐ-ⓕ]|[a-f](?= [A-Za-z])|\([A-F]\)|\([가-바]\)|㉠|㉡|㉢|㉣)\s+([A-Za-z][^,.→]{0,40})", body2):
        tag = m[1].strip("()")
        if tag not in pl: continue
        ws = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'’]+", re.sub(r"\([^)]*\)", "", m[2])) if w.lower() not in STOP]
        if ws and not any(w in pl[tag] for w in ws): out.append(("기호문장", f"{m[1]}:{'/'.join(ws)}"))
    # 4) 해설이 가리키는 기호가 문항에 있는지
    raw = " ".join([it.get("stem", ""), it.get("passage", ""), " ".join(it.get("c", []))])
    for lab in sorted(set(re.findall(r"\(([A-E])\)", it.get("expl", "")))):
        if f"({lab})" not in raw and not re.search(r"\b%s\b" % lab, re.sub(r"[^A-E(]", " ", raw)): out.append(("없는기호", f"({lab})"))
    for lab in sorted(set(re.findall(r"[ⓐ-ⓕ]", it.get("expl", "")))):
        if lab not in raw: out.append(("없는기호", lab))
    return out, st
res = []
ref = json.load(open("page/data/ref.json"))
for k, r in ref.items():
    o, st = audit(k, "REF", "A", r)
    if o: res.append((k, "REF", "A", None, o, st))
for t in "BCDEF":
    fx = json.load(open(f"page/data/fix_{t}.json"))
    for k, it in fx.items():
        o, st = audit(k, "FIX", t, it)
        if o: res.append((k, "FIX", t, done.get((k, t)), o, st))
json.dump(res, open(os.environ.get("OUT", "steps_audit.json"), "w"), ensure_ascii=False)
import collections
print(len(res), collections.Counter((r[1], r[2]) for r in res), collections.Counter(c for r in res for c, _ in r[4]))
