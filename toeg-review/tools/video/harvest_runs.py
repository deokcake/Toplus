#!/usr/bin/env python3
"""대본 워크플로(toeg-scripts) 기록에서 번호별 해설 감수 결과를 모은다.
- 워크플로 journal.jsonl(started의 label ‘write:<번호>’/‘verify:<번호>’ ↔ result)을 읽는다.
- src/expl_review/runs/by_number.json = {번호: [{type, verdict, first, issues, proposed, note}]}  (재검증까지 끝난 번호)
- 진행 현황: 급별 대본 완료(재검증까지) 번호 수, 작성만 된 번호, 남은 번호.
사용: python3 tools/video/harvest_runs.py <workflows 폴더>"""
import sys, json, re, glob
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]

def main(W):
    wr, vr = {}, {}
    for j in sorted(glob.glob(str(Path(W) / "*/journal.jsonl"))):
        lab = {}
        for l in open(j, encoding="utf-8"):
            d = json.loads(l)
            if d.get("type") == "started": lab[d["agentId"]] = d.get("label", "")
            if d.get("type") != "result" or not isinstance(d.get("result"), dict): continue
            m = re.fullmatch(r"(write|verify):(\d-\d+)", lab.get(d.get("agentId"), ""))
            if not m or not d["result"].get("review"): continue
            (wr if m[1] == "write" else vr)[m[2]] = d["result"]
    out = HERE / "src/expl_review/runs/by_number.json"
    by = {}
    for k, v in vr.items():
        first = {x["type"]: x["verdict"] for x in wr.get(k, {}).get("review", [])}
        by[k] = [{"type": x["type"], "verdict": x["final_verdict"], "first": first.get(x["type"], x["final_verdict"]), "issues": x["issues"], "proposed": x["proposed"], "note": x.get("verifier_note", "")} for x in v["review"]]
    # 사용자 요청으로 문항 자체를 고친 경우 등: src/expl_review/overrides.json {"번호|유형": {...}}이 감수 결과를 덮는다
    OV = HERE / "src/expl_review/overrides.json"
    for kt, x in (json.load(open(OV, encoding="utf-8")) if OV.exists() else {}).items():
        k, T = kt.split("|")
        if k in by: by[k] = [y for y in by[k] if y["type"] != T] + [{"type": T, "first": x["verdict"], **x}]
    json.dump(by, open(out, "w", encoding="utf-8"), ensure_ascii=False)
    first_only = {k: [{"type": x["type"], "verdict": x["verdict"], "first": x["verdict"], "issues": x["issues"], "proposed": x["proposed"], "note": ""} for x in w["review"]] for k, w in wr.items() if k not in vr}
    json.dump(first_only, open(out.with_name("by_number_first.json"), "w", encoding="utf-8"), ensure_ascii=False)
    # 진행 현황: 번호마다 완료(작성+재검증) / 작성만(재검증 전) / 작성 중단(채움 파일만 있음) / 시작 전
    sys.path.insert(0, str(HERE / "tools" / "video")); import check_scripts as CS
    idx = json.load(open(HERE / "page/data/index.json", encoding="utf-8"))
    st = {}; L = ["# 영상 대본 진행 현황 (번호별)", "", "| 급 | 전체 | 완료(작성+재검증) | 재검증 전 | 작성 중단 | 시작 전 | 150초 넘는 편 |", "|---|---|---|---|---|---|---|"]
    lists = {}
    for g in "7654321":
        ks = [k for k in idx["order"] if k.split("-")[0] == g]; c = {"완료": [], "재검증 전": [], "작성 중단": [], "시작 전": []}; over = 0
        for k in ks:
            s = "완료" if k in vr else "재검증 전" if k in wr else "작성 중단" if (HERE / f"work/video/fill/{k}.json").exists() else "시작 전"
            c[s].append(k); st[k] = s
            for T in "ABCDEF":
                f = HERE / f"결과/영상대본/{g}급/{k}-{T}.json"
                if f.exists() and CS.est_total(json.load(open(f, encoding="utf-8"))) > CS.MAX_SEC: over += 1
        L.append(f"| {g}급 | {len(ks)} | {len(c['완료'])} | {len(c['재검증 전'])} | {len(c['작성 중단'])} | {len(c['시작 전'])} | {over} |")
        lists[g] = c
        print(f"{g}급: 완료 {len(c['완료'])}, 재검증 전 {len(c['재검증 전'])}, 작성 중단 {len(c['작성 중단'])}, 시작 전 {len(c['시작 전'])}, 150초 초과 {over}편")
    L += ["", "- 완료: 작성 에이전트(해설 6개 감수 + 대본 6편) → 재검증 에이전트까지 끝남", "- 재검증 전: 작성은 끝났고 재검증이 남음(대본 파일 있음)", "- 작성 중단: 작성 도중 멈춤(채움 파일만 있음, 처음부터 다시 쓰는 것이 안전)", "- 시작 전: 아무것도 없음", ""]
    for g in "7654321":
        for s in ("재검증 전", "작성 중단", "시작 전"):
            if lists[g][s]: L.append(f"- {g}급 {s} ({len(lists[g][s])}): " + ", ".join(k.split("-")[1] for k in lists[g][s]))
    json.dump(st, open(HERE / "work/video/status.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    open(HERE / "work/video/남은_문항.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("by_number:", len(by), "번호 →", out, "| 현황 → work/video/status.json, work/video/남은_문항.md")
    return by

if __name__ == "__main__": main(sys.argv[1])
