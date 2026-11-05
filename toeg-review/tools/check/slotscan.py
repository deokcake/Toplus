# 풀이 순서 칸(rv2 EX의 유형별 값)에 든 영어 낱말이 그 문항(발문·지문·보기·다른 해설 줄)에 없으면 표시한다.
import json, re, sys, os, glob
sys.path.insert(0, ".")
import rv2build
N = sys.argv[1]
EX, _ = rv2build.load()
STOP = set("""a an the and or but not to of in on at for by with from as is are am was were be been being do does did have has had will would can could shall should may might must
it its this that these those there here he she they we you i me him her them us my your his our their who what which when where why how whose whom yes no than then so if also too very
much many more most less few little some any all both each every either neither nor only just ing ed ly""".split())
done = {}
for t in "CDEF":
    for f in glob.glob(f"{N}/db13/t_{t}/*.json"):
        d = json.load(open(f, encoding="utf-8")); done[(os.path.basename(f)[:-5], t)] = bool(d.get("done"))
out = []
for t in "CDEF":
    fx = json.load(open(f"page/data/fix_{t}.json", encoding="utf-8"))
    base = {f'{r["g"]}-{r["n"]}': r for r in json.load(open(f"page/data/{t}.json", encoding="utf-8"))}
    for k in sorted(set(base) | set(fx), key=lambda x: tuple(map(int, x.split("-")))):
        g, n = map(int, k.split("-")); ex = EX.get((g, n)) or {}
        sl = ex.get(t)
        if sl is None: continue
        vals = [sl] if isinstance(sl, str) else list(sl)
        it = fx.get(k) or base.get(k)
        lines = it.get("expl", "").split("\n")
        rest = "\n".join(l for l in lines if not l.startswith("풀이 순서"))
        text = re.sub(r"</?u>", "", " ".join([it.get("stem", ""), it.get("passage", ""), " ".join(it.get("c", [])), rest])).lower()
        words = set(w.lower().strip("'’-") for v in vals for w in re.findall(r"[A-Za-z][A-Za-z'’-]+", str(v)))
        miss = sorted(w for w in words if w not in STOP and len(w) >= 3 and w not in text and w.rstrip("s") not in text)
        if miss: out.append((k, t, done.get((k, t)), miss, next((l for l in lines if l.startswith("풀이 순서")), "")[:300]))
for k, t, dn, miss, st in out: print(f"{k}{t} done={dn} miss={miss}\n    {st}")
print(len(out), "open:", sum(1 for x in out if not x[2]))
