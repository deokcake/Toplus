#!/usr/bin/env python3
"""확정본 문항 불러오기(기준 문항 A, 변형 B).
- 기준 문항: page/data/ref.json (감수 완료 확정본)
- B 유형: page/data/B.json(원안)에 검토 페이지 DB의 감수자 확정(edit)을 덮어쓴 것. DB 스냅샷은 src/db_tB/*.json (2026-10-26, 풀이 정정 반영)."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
C5 = "①②③④⑤"
idx = json.load(open(HERE / "page/data/index.json", encoding="utf-8"))
CHAP = {}
for g, chs in idx["grades"].items():
    for c in chs:
        for n in c["nos"]: CHAP[f"{g}-{n}"] = (c["ch"], c["chn"])

def merged_edit(base, e):
    out = {"stem": base["stem"], "passage": base["passage"], "c": list(base["c"]), "ans": str(base["ans"]), "expl": base.get("expl", "")}
    if not e: return out
    # 검토 페이지(effItem)와 같은 규칙: 문자열이면 빈 문자열("")도 감수자가 정한 값이다(본문을 지운 경우).
    for k in ("stem", "passage", "expl"):
        if isinstance(e.get(k), str): out[k] = e[k]
    if e.get("ans") not in (None, ""): out["ans"] = str(e["ans"])
    ec = e.get("c")
    if isinstance(ec, dict):
        for i, v in ec.items():
            if v is not None and 0 <= int(i) < 5: out["c"][int(i)] = v
    elif isinstance(ec, list):
        out["c"] = [v if v is not None else out["c"][i] for i, v in enumerate(ec)]
    return out

def load_ref():
    ref = json.load(open(HERE / "page/data/ref.json", encoding="utf-8"))
    return {k: {"stem": r["stem"], "passage": r["passage"], "c": list(r["c"]), "ans": str(r["ans"]), "expl": r.get("expl", "")} for k, r in ref.items()}

def load_B(db_dir=HERE / "src/db_tB"):
    rows = json.load(open(HERE / "page/data/B.json", encoding="utf-8"))
    out, src = {}, {}
    for r in rows:
        k = f"{r['g']}-{r['n']}"
        f = Path(db_dir) / f"{k}.json"
        e = json.load(open(f, encoding="utf-8")).get("edit") if f.exists() else None
        out[k] = merged_edit(r, e); src[k] = "감수자 확정" if e else "원안"
    return out, src

def order():
    """index.json의 문항 순서: [(g, n), ...]"""
    return [(int(g), n) for g, chs in idx["grades"].items() for c in chs for n in c["nos"]]
