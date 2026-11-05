#!/usr/bin/env python3
"""번호마다 대본·해설 감수 작업 입력을 만든다: work/video/in/<key>.json
{key, grade, chapter, items:{A..F:{stem,passage,c,ans,expl}}, prior_review:{T:{verdict,issues,proposed,note,verified}}}
- 문항은 make_scripts.load_all과 같다(A = ref.json, B~F = 확정본 = page/data + DB 스냅샷 edit).
- prior_review: 이미 끝난 해설 감수(src/expl_review/runs/merged_done.json = 재검증까지, review_only.json = 1차 검토만)."""
import sys, json
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(HERE / "tools" / "video"))
import make_scripts as MS

def prior():
    R = HERE / "src/expl_review/runs"; out = {}
    if (R / "merged_done.json").exists():
        for b, rows in json.load(open(R / "merged_done.json", encoding="utf-8")).items():
            for x in rows: out[(x["key"], x["type"])] = {"verdict": x["verdict"], "issues": x["issues"], "proposed": x["proposed"], "note": x.get("note", ""), "verified": True}
    if (R / "review_only.json").exists():
        for b, r in json.load(open(R / "review_only.json", encoding="utf-8")).items():
            for x in r["results"]: out.setdefault((x["key"], x["type"]), {"verdict": x["verdict"], "issues": x["issues"], "proposed": x["proposed"], "note": "", "verified": False})
    return out

if __name__ == "__main__":
    out = HERE / "work/video/in"; out.mkdir(parents=True, exist_ok=True)
    PR = prior(); units = {}
    for k, T, it, g, ch, chn in MS.load_all("ABCDEF"):
        u = units.setdefault(k, {"key": k, "grade": g, "chapter": f"{ch} {chn}", "items": {}, "prior_review": {}})
        u["items"][T] = it
        if (k, T) in PR and PR[(k, T)]["verdict"] != "이상 없음": u["prior_review"][T] = PR[(k, T)]
        elif (k, T) in PR: u["prior_review"][T] = {"verdict": "이상 없음", "verified": PR[(k, T)]["verified"]}
    for k, u in units.items(): json.dump(u, open(out / f"{k}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(units), "inputs →", out, "| with prior review:", sum(1 for u in units.values() if u["prior_review"]))
