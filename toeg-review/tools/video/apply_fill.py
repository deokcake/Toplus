#!/usr/bin/env python3
"""채움 파일(fill) + 문항 → 최종 영상 대본 JSON·MD (src/video/SCRIPT_SPEC.md 2판), 그리고 자동 점검.
사용: python3 tools/video/apply_fill.py <key> [<key> ...]      예) python3 tools/video/apply_fill.py 7-56
입력: work/video/in/<key>.json (문항 A~F), work/video/fill/<key>.json (유형별 채움 내용, 아래 FILL 형식)
출력: 결과/영상대본/<급>급/<key>-<T>.json, .md  — 점검 ERR이 0이 될 때까지 fill을 고쳐 다시 돌린다.

FILL 형식 (유형마다 하나, {"A": {...}, "B": {...}, ...}):
{
 "title": "이 영상의 제목(문법 요소, 20자 안팎)",
 "intro": "이 문제는 …을 묻는 문제예요.",            # 장면 1. 화면에도 그대로 쓴다
 "problem_narration": "(선택) 장면 2 내레이션",       # 없으면 발문을 읽고 '먼저 풀어 보세요…'를 붙인다
 "rule": {"card": ["규칙 줄", "규칙 줄", "예) 대표 예문 (우리말 뜻)"], "narration": "…"},
 "steps": [{"note": "판서 메모", "highlight": ["화면 글 조각"], "strike": ["화면 글 조각"], "narration": "첫째, …"}, …],   # 2~4단계
 "check": {"lines": ["① 보기  ✗  이유", … 5줄], "narration": "…"},
 "summary": {"card": "기억할 것 한 줄", "narration": "정답은 N번이에요. 기억할 것, …"},
 "captions": ["장면1", …, "장면6"],                  # (선택) 없으면 자동
 "sec": [5, 15, 22, 36, 26, 10]
}"""
import sys, re, json, math
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(HERE / "tools" / "video"))
import make_scripts as MS, check_scripts as CS

C5 = MS.C5
NAMES = ["도입", "문제", "핵심 규칙", "풀이 순서", "선택지 확인", "정리"]

def item_text(it):
    opts = "\n".join(f"{C5[i]} {x}" for i, x in enumerate(it["c"]))
    pas = (it.get("passage") or "").strip()
    return it["stem"].strip() + ("\n\n" + pas if pas else "") + "\n\n" + opts, [it["stem"].strip()] + ([l for l in pas.split("\n") if l.strip()] if pas else []) + [f"{C5[i]} {x}" for i, x in enumerate(it["c"])]

def build(u, T, f):
    it = u["items"][T]; g = u["grade"]; k = u["key"]; n = k.split("-")[1]; a = int(it["ans"]); c = it["c"]
    ch = u["chapter"]; chnum = re.match(r"CH\s*(\d+)", ch); chnum = chnum[1] if chnum else ch
    head = f"{g}급 · {ch} · {n}번" + ("" if T == "A" else f" · {T} 유형")
    sec = list(f.get("sec") or [5, 15, 22, 36, 26, 10]); cap = list(f.get("captions") or [])
    cap += [""] * (6 - len(cap))
    txt, rev2 = item_text(it)
    intro = f["intro"].strip()
    s1 = {"no": 1, "name": "도입", "sec": sec[0], "screen": {"text": f"{head}\n\n{intro}", "highlight": [], "strike": [], "marks": {}, "reveal": [head, intro]},
          "narration": f"{g}급 챕터 {chnum}, {n}번" + ("" if T == "A" else f" {T} 유형") + f". {intro}", "caption": cap[0] or f["title"]}
    s2 = {"no": 2, "name": "문제", "sec": sec[1], "screen": {"text": txt, "highlight": [], "strike": [], "marks": {}, "reveal": rev2},
          "narration": (f.get("problem_narration") or (MS.tts(it["stem"]) + " 먼저 풀어 보세요. 영상을 잠시 멈춰도 좋아요.")).strip(), "caption": cap[1] or "먼저 풀어 보세요"}
    card = [x.strip() for x in f["rule"]["card"] if x.strip()]
    s3 = {"no": 3, "name": "핵심 규칙", "sec": sec[2], "screen": {"text": "핵심 규칙\n" + "\n".join(card), "highlight": [], "strike": [], "marks": {}, "reveal": ["핵심 규칙"] + card},
          "narration": f["rule"]["narration"].strip(), "caption": cap[2] or f["title"]}
    steps = [{"step": i + 1, "highlight": s.get("highlight") or [], "strike": s.get("strike") or [], "note": s.get("note", "")} for i, s in enumerate(f["steps"])]
    s4 = {"no": 4, "name": "풀이 순서", "sec": sec[3], "screen": {"text": txt, "highlight": [], "strike": [], "marks": {}, "steps": steps, "reveal": []},
          "narration": " ".join(s["narration"].strip() for s in f["steps"]), "caption": cap[3] or "풀이 순서"}
    lines = [x.strip() for x in f["check"]["lines"]]
    s5 = {"no": 5, "name": "선택지 확인", "sec": sec[4], "screen": {"text": "\n".join(lines), "highlight": [], "strike": [], "marks": {C5[i]: ("✓" if i + 1 == a else "✗") for i in range(5)}, "reveal": lines},
          "narration": f["check"]["narration"].strip(), "caption": cap[4] or f"정답 {C5[a-1]}"}
    s6 = {"no": 6, "name": "정리", "sec": sec[5], "screen": {"text": f"정답 {C5[a-1]} {c[a-1]}\n\n{f['summary']['card'].strip()}", "highlight": [], "strike": [], "marks": {}, "reveal": [f"정답 {C5[a-1]} {c[a-1]}", f["summary"]["card"].strip()]},
          "narration": f["summary"]["narration"].strip(), "caption": cap[5] or f"정답 {C5[a-1]}"}
    sc = [s1, s2, s3, s4, s5, s6]
    for s in sc: s["sec"] = max(int(s["sec"]), math.ceil(CS.scene_need(s)))   # 장면 길이는 실제 낭독 시간 이상으로
    return {"key": k, "type": T, "grade": g, "chapter": ch, "title": f["title"].strip(), "total_sec": sum(int(s["sec"]) for s in sc), "style": MS.STYLE, "scenes": sc,
            "source": {"stem": it["stem"], "passage": it.get("passage") or "", "c": c, "ans": a, "expl": it.get("expl", "")}}

def esc(s): return str(s).replace("|", "\\|").replace("\n", "<br>")

def md(d):
    a = d["source"]["ans"]; T = d["type"]
    L = [f"# {d['key']}{'' if T == 'A' else ' ' + T + ' 유형'} — {d['title']}", "",
         f"- 급·챕터·번호: {d['grade']}급 · {d['chapter']} · {d['key'].split('-')[1]}번" + ("" if T == "A" else f" · {T} 유형"),
         f"- 정답: {C5[a-1]}", f"- 총 길이: {d['total_sec']}초", "- 화면: 칠판에 분필로 판서하듯 ‘판서 순서’대로 한 줄씩 써 나간다. 강조 = 노란 분필, 지움 = 분필 줄 긋기.", "",
         "| 장면 | 길이 | 화면(판서 순서) | 내레이션 | 자막 |", "|---|---|---|---|---|"]
    for s in d["scenes"]:
        scr = s["screen"]; parts = [esc(scr["text"])]
        if scr.get("reveal") and s["no"] not in (2, 4): pass
        if scr.get("steps"):
            for st in scr["steps"]:
                bits = [f"**{st['step']}단계** {esc(st['note'])}"]
                if st["highlight"]: bits.append("강조 " + ", ".join(f"`{esc(x)}`" for x in st["highlight"]))
                if st["strike"]: bits.append("지움 " + ", ".join(f"`{esc(x)}`" for x in st["strike"]))
                parts.append(" / ".join(bits))
        if s["no"] == 4: parts[0] = "(장면 2의 판서를 그대로 두고 단계마다 강조·지움을 더한다)"
        L.append(f"| {s['no']}. {s['name']} | {s['sec']}초 | {'<br>'.join(parts)} | {esc(s['narration'])} | {esc(s['caption'])} |")
    L += ["", "## 원본 해설", "", "```", d["source"]["expl"].strip(), "```", ""]
    return "\n".join(L)

def run(key):
    u = json.load(open(HERE / f"work/video/in/{key}.json", encoding="utf-8"))
    F = json.load(open(HERE / f"work/video/fill/{key}.json", encoding="utf-8"))
    out = HERE / f"결과/영상대본/{u['grade']}급"; out.mkdir(parents=True, exist_ok=True)
    nerr = 0
    for T in "ABCDEF":
        if T not in F: print(f"[{key}-{T}] ERR fill 없음"); nerr += 1; continue
        try: d = build(u, T, F[T])
        except Exception as e: print(f"[{key}-{T}] ERR fill 형식 오류: {type(e).__name__}: {e}"); nerr += 1; continue
        E, W = CS.check(d)
        json.dump(d, open(out / f"{key}-{T}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        open(out / f"{key}-{T}.md", "w", encoding="utf-8").write(md(d))
        nerr += len(E)
        print(f"[{key}-{T}] {d['total_sec']}초 ERR {len(E)} WARN {len(W)}")
        for e in E: print("   ERR ", e)
        for w in W: print("   WARN", w)
    print(f"== {key}: ERR {nerr}")
    return nerr

if __name__ == "__main__":
    sys.exit(1 if sum(run(k) for k in sys.argv[1:]) else 0)
