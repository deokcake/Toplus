# 풀이 순서 중간(마지막 '정답은' 앞)에 정답과 다른 보기 번호가 '만/뿐/맞다/옳다'와 함께 나오면 표시한다.
import json, re, sys, os, glob
N = sys.argv[1]
done = {}
for t in "CDEF":
    for f in glob.glob(f"{N}/db13/t_{t}/*.json"):
        d = json.load(open(f, encoding="utf-8")); done[(os.path.basename(f)[:-5], t)] = bool(d.get("done"))
C = "①②③④⑤"
for t in "CDEF":
    fx = json.load(open(f"page/data/fix_{t}.json", encoding="utf-8"))
    base = {f'{r["g"]}-{r["n"]}': r for r in json.load(open(f"page/data/{t}.json", encoding="utf-8"))}
    for k in sorted(set(base) | set(fx), key=lambda x: tuple(map(int, x.split("-")))):
        it = fx.get(k) or base.get(k); a = int(it["ans"]) if str(it["ans"]).isdigit() else 0
        st = next((l for l in it.get("expl", "").split("\n") if l.startswith("풀이 순서")), "")
        if not st or not a: continue
        body = re.sub(r"(풀이 순서: |→ )[①-⑤] ", r"\1", st)
        body = re.sub(r"정답은 [①-⑤].*$", "", body)
        bad = []
        for m in re.finditer(r"(?:선택지 )?([①-⑤])([^①-⑤→]{0,30})", body):
            if C.index(m[1]) + 1 != a: bad.append(m[0][:50])
        if bad: print(f"{k}{t} done={done.get((k, t))} ans={C[a-1]} bad={bad}\n    {st[:280]}")
