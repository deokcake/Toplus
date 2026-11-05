import json, re, sys, glob
sys.path.insert(0, ".")
import fxbuild
ref = json.load(open("page/data/ref.json", encoding="utf-8"))
files = sys.argv[2:]
keys = []
for f in files:
    src = open(f, encoding="utf-8").read()
    for m in re.finditer(r'(?:RE|L)\((\d+), (\d+), "([CDEF])"', src): keys.append((int(m[1]), int(m[2]), m[3]))
    for m in re.finditer(r'F89\("([DEF])"', src): keys.append((1, 89, m[1]))
keys = sorted(set(keys))
raw = fxbuild.load(); fxbuild.raw_kw.update(raw)
import rv2build, explfmt
EX2, _ = rv2build.load()
def ew(s): return len(re.findall(r"[A-Za-z][A-Za-z'’-]*", re.sub(r"</?u>", "", s or "")))
def om(c): return sum(ew(x) for x in c) / len(c)
bad = []
for key in keys:
    it = fxbuild.build(key, raw[key]); g, n, t = key
    st = rv2build.steps_for(EX2[(g, n)], t, it)
    it["expl"] = explfmt.restructure(rv2build.set_steps(it["expl"], st), it["ans"], EX2[(g, n)]["r"])
    R = ref[f"{g}-{n}"]; rp, ro = ew(R["passage"]), om(R["c"]); p, o = ew(it["passage"]), om(it["c"])
    short = (rp >= 6 and p < rp) or (ro >= 4 and o < ro)
    plain = re.sub(r"</?u>", "", it["stem"] + " " + it["passage"] + " " + " ".join(it["c"]))
    quotes = re.findall(r"[‘'“\"]([A-Za-z][^‘’'“”\"]{6,}?)[’'”\"]", it["expl"])
    miss = [q for q in quotes if q.strip(" .") not in plain and q.strip(" .")[:-1] not in plain]
    print(f"{g}-{n}{t} a{it['ans']} P{p}/{rp} O{o:.1f}/{ro:.1f}{' ★SHORT' if short else ''} | {st[-170:] if st else '(no steps)'}")
    if miss: print("     ⚠ 해설 인용이 문항에 없음:", miss[:4])
    if short or miss: bad.append(f"{g}-{n}{t}")
print("문제:", bad)
