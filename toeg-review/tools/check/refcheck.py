# 풀이 순서가 보기 번호(①~⑤)나 지문 기호(ⓐ~ⓔ, a~e, (A)~(E), (가)~(마))를 짚고 바로 뒤에 영어를 인용하면, 그 영어가 그 보기·문장에 실제로 있는지 본다.
import json, re, sys, os, glob
N = sys.argv[1]; only_open = "--all" not in sys.argv
done = {}
for t in "CDEF":
    for f in glob.glob(f"{N}/db13/t_{t}/*.json"):
        d = json.load(open(f, encoding="utf-8")); done[(os.path.basename(f)[:-5], t)] = bool(d.get("done"))
STOP = set("a an the and or to of in on at for by with is are am was were be it this that he she they we you i not do does did can will".split())
C = "①②③④⑤"; L5 = "ⓐⓑⓒⓓⓔ"; K5 = ["(가)", "(나)", "(다)", "(라)", "(마)"]
def plain(s): return re.sub(r"</?u>", "", s or "").lower()
def lines_of(p):
    out = {}
    for l in (p or "").split("\n"):
        l2 = l.strip()
        m = re.match(r"^([ⓐ-ⓔ]|\([A-E]\)|\([가-마]\)|[a-e][.)])\s*", l2)
        if m:
            tag = m[1]; i = L5.index(tag) if tag in L5 else ("ABCDE".index(tag[1]) if tag.startswith("(") and tag[1] in "ABCDE" else (["가","나","다","라","마"].index(tag[1]) if tag.startswith("(") else "abcde".index(tag[0])))
            out[i] = plain(l2)
    return out
for t in "CDEF":
    fx = json.load(open(f"page/data/fix_{t}.json", encoding="utf-8"))
    base = {f'{r["g"]}-{r["n"]}': r for r in json.load(open(f"page/data/{t}.json", encoding="utf-8"))}
    for k in sorted(set(base) | set(fx), key=lambda x: tuple(map(int, x.split("-")))):
        if only_open and done.get((k, t)): continue
        it = fx.get(k) or base.get(k)
        st = next((l for l in it.get("expl", "").split("\n") if l.startswith("풀이 순서")), "")
        if not st: continue
        body = re.sub(r"(풀이 순서: |→ )[①-⑤] ", r"\1", st)
        opts = [plain(c) for c in it.get("c", [])]; pl = lines_of(it.get("passage", ""))
        bad = []
        for m in re.finditer(r"(?:선택지 )?([①-⑤])(?:[은는이가의만]|만|도)?\s*([^①-⑤→.]{0,60})", body):
            i = C.index(m[1]); seg = m[2]
            if i >= len(opts): continue
            ws = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'’]+", seg) if w.lower() not in STOP]
            miss = [w for w in ws if w not in opts[i] and w.rstrip("s") not in opts[i] and w not in plain(it.get("passage", ""))]
            # 고친 꼴(괄호 속, '로 고친다', '이 맞다')은 보기에 없을 수 있으니 2개 이상 빠질 때만
            if len(miss) >= 1 and len([w for w in ws if w in opts[i]]) == 0 and ws: bad.append(f"{m[1]}:{'/'.join(miss)}")
        for m in re.finditer(r"(?<![A-Za-z])([ⓐ-ⓔ]|[a-e](?= [A-Za-z])|\([A-E]\))\s+([A-Za-z][^,.→]{0,40})", body):
            tag = m[1]; i = L5.index(tag) if tag in L5 else ("ABCDE".index(tag[1]) if tag.startswith("(") else "abcde".index(tag))
            if i not in pl: continue
            ws = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'’]+", re.sub(r"\([^)]*\)", "", m[2])) if w.lower() not in STOP]
            if ws and not any(w in pl[i] for w in ws): bad.append(f"{tag}:{'/'.join(ws)}")
        if bad: print(f"{k}{t} done={done.get((k, t))} bad={bad}\n    {st[:300]}")
