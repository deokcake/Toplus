#!/usr/bin/env python3
"""수정 예시(fx/*.py)의 등록 이력을 따라, 지문·보기·정답이 바뀐 뒤 해설 부분(n·pre·k·x)이 새로 쓰이지 않은 문항을 찾는다.
결과: 키 → {"content": 마지막 내용 변경 파일, "n": 마지막 보기 해설 파일, ...}"""
import json, glob, sys, collections
sys.path.insert(0, "."); import fxlib
H = collections.defaultdict(list); CUR = [None]
_F, _RE = fxlib.F, fxlib.RE
def F(g_, no_, t_, /, **kw):
    H[(g_, no_, t_)].append((CUR[0], "F", sorted(kw))); return _F(g_, no_, t_, **kw)
def RE(g_, n_, t_, **kw):
    H[(g_, n_, t_)].append((CUR[0], "RE", sorted(kw)))
    old = fxlib.FIX.pop((g_, n_, t_), None) or {}
    if "n" in kw or "x" in kw:
        for k_ in ("x", "keepx", "okx", "op", "xr"): old.pop(k_, None)
    if "c" in kw and not ({"n", "x", "keepx", "okx"} & (set(kw) | set(old))):
        raise AssertionError(f"{(g_, n_, t_)} 보기를 바꾸면 해설(n)이 필요")
    old.update(kw); _F(g_, n_, t_, **old)
fxlib.F = F; fxlib.RE = RE
fxlib.FIX.clear()
for f in sorted(glob.glob("fx/*.py")):
    CUR[0] = f.split("/")[-1]
    g = {k: getattr(fxlib, k) for k in dir(fxlib) if not k.startswith("_")}
    g["F"] = F; g["RE"] = RE
    exec(compile(open(f, encoding="utf-8").read(), f, "exec"), g)
out = {}
for key, hs in H.items():
    last = {}
    for i, (f, kind, ks) in enumerate(hs):
        for k in ks:
            last[k] = i
    fin = fxlib.FIX.get(key, {})
    cont = max([last.get(k, -1) for k in ("p", "c", "a", "st")])
    rec = {"content_at": hs[cont][0] if cont >= 0 else None, "calls": [(f, kind, ks) for f, kind, ks in hs]}
    flags = []
    if cont >= 0:
        if not ({"n", "x"} & set(fin)): flags.append("원안해설+내용변경")
        else:
            nx = max(last.get("n", -1), last.get("x", -1))
            if nx < cont: flags.append("보기해설이전")
        if "pre" in fin and last.get("pre", -1) < cont and ("p" in hs[cont][2] or "c" in hs[cont][2]): flags.append("판정이전")
        if "k" in fin and last.get("k", -1) < cont: flags.append("판단이전")
    rec["flags"] = flags
    out["%d-%d%s" % key] = rec
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "fx_history.json", "w"), ensure_ascii=False)
c = collections.Counter(f for r in out.values() for f in r["flags"])
print(len(out), c, "문항:", sum(1 for r in out.values() if r["flags"]))
