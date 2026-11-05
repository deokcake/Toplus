#!/usr/bin/env python3
"""문항·해설 → 영상 대본 뼈대(초안) JSON. (src/video/SCRIPT_SPEC.md 2판: 문항마다 1편, 6장면, 칠판 판서)
사용: python3 tools/video/make_scripts.py --out <폴더> [--types ABCDEF] [key ...]
- 화면 글은 문항에서 그대로 가져오고, 내레이션은 해설을 TTS용으로 기호만 바꾼 초안이다(에이전트가 말로 다듬는다).
- B~F는 page/data/{T}.json + DB 스냅샷(src/db_t{T}_20261028)의 edit을 덮어쓴 확정본. 해설이 바뀌면(승인 반영) 이 스크립트를 다시 돌린다."""
import sys, re, json, argparse
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(HERE / "tools")); sys.path.insert(0, str(HERE))
import final_items as FI, explfmt

C5 = "①②③④⑤"; L5 = "ⓐⓑⓒⓓⓔ"
STYLE = {"board": "chalkboard", "writing": "handwritten-reveal", "chalk": "white", "accent": "yellow",
         "note": "짙은 녹색 칠판에 분필 글씨. 내레이션 문장에 맞춰 screen.reveal 순서대로 판서하듯 써 내려간다. 강조는 노란 분필 밑줄, 지움은 분필 줄 긋기, ✓/✗는 분필 표시."}

def tts(s):
    """해설·문항 글을 읽을 수 있는 말로: 기호 → 말."""
    s = str(s or "")
    s = re.sub(r"<u>(.*?)</u>", r"밑줄 친 \1", s)
    s = re.sub(r"_{3,}", "빈칸", s)
    for i, c in enumerate(C5): s = s.replace(c, f"{i+1}번")
    for i, c in enumerate(L5): s = s.replace(c, f"{'에이 비 씨 디 이'.split()[i]} 문장")
    s = re.sub(r"\((A|B|C|D|E)\)", lambda m: f"{'에이 비 씨 디 이'.split()[ord(m[1])-65]} 빈칸", s)
    s = s.replace("→", " 따라서 ").replace("·", ", ")
    for a, b in (("-ing형", "ing형"), ("-ing", "ing형"), ("-s/-es", "s나 es"), ("-es", "es"), ("-s형", "s형"), ("-s", "s형"), ("-ed", "ed"), ("-ies", "ies"), ("-ly", "ly")): s = s.replace(a, b)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def steps_of(expl):
    p = explfmt.parse(expl); st = " ".join(p["steps"])
    parts = [x.strip() for x in re.split(r"→\s*", st) if x.strip()]
    out = []
    for x in parts:
        x = re.sub(r"^[①②③④⑤]\s*", "", x).strip()
        if x: out.append(x)
    return p, out[:4] if out else [st]

def desc_of(stem):
    s = re.sub(r"^다음\s*", "", stem.strip())
    if re.search(r"고르(시오|세요)\.?$", s): return re.sub(r"고르(시오|세요)\.?$", "고르는 문제예요", s)
    if re.search(r"것은\s*\?$", s): return re.sub(r"것은\s*\?$", "것을 찾는 문제예요", s)
    if s.endswith("?"): return s[:-1].strip() + "라고 묻는 문제예요"
    return s.rstrip(".") + " 문제예요"

def opt_reasons(p, ans):
    out = []
    for i, o in enumerate(p["opts"]):
        body = re.sub(r"^\[(정답|오답)\]\s*", "", " ".join(o)).strip()
        out.append(body)
    return out

def short(s, n=46):
    s = re.sub(r"\s*(정답|오답)이다\.?$", "", s).strip()
    return s if len(s) <= n else s[:n - 1] + "…"

def build(key, T, it, g, ch, chn):
    n = key.split("-")[1]; a = int(it["ans"]); c = list(it["c"]); expl = it.get("expl", "") or ""
    p, steps = steps_of(expl)
    rule = " ".join(p["rule"]).strip(); keyj = " ".join(p["key"]).strip(); judge = [l for l in p["judge"] if l.strip()]
    reasons = opt_reasons(p, a)
    opts = "\n".join(f"{C5[i]} {x}" for i, x in enumerate(c))
    item_txt = it["stem"].strip() + ("\n\n" + it["passage"].strip() if (it.get("passage") or "").strip() else "") + "\n\n" + opts
    head = f"{g}급 · {ch} {chn} · {n}번" + ("" if T == "A" else f" · {T} 유형")
    desc = desc_of(it["stem"])
    s1 = {"no": 1, "name": "도입", "sec": 5, "screen": {"text": f"{head}\n\n이 문제는 {desc}.", "highlight": [], "strike": [], "marks": {}, "reveal": [head, f"이 문제는 {desc}."]},
          "narration": f"{g}급 챕터 {ch.replace('CH', '').strip()}, {n}번" + ("" if T == "A" else f" {T} 유형") + f". 이 문제는 {tts(desc)}.", "caption": f"이 문제는 {desc}"}
    reveal2 = [it["stem"].strip()] + ([l for l in it["passage"].split("\n") if l.strip()] if (it.get("passage") or "").strip() else []) + [f"{C5[i]} {x}" for i, x in enumerate(c)]
    s2 = {"no": 2, "name": "문제", "sec": 15, "screen": {"text": item_txt, "highlight": [], "strike": [], "marks": {}, "reveal": reveal2},
          "narration": tts(it["stem"]) + " 먼저 풀어 보세요. 영상을 잠시 멈춰도 좋아요.", "caption": "먼저 풀어 보세요"}
    rule_lines = [x.strip() for x in re.split(r"(?<=[.다])\s+(?=[가-힣A-Za-z])", rule) if x.strip()] or [rule]
    s3 = {"no": 3, "name": "핵심 규칙", "sec": 22, "screen": {"text": "핵심 규칙\n" + "\n".join(rule_lines), "highlight": [], "strike": [], "marks": {}, "reveal": ["핵심 규칙"] + rule_lines},
          "narration": tts(rule), "caption": short(rule_lines[0], 30)}
    ords = ["첫째", "둘째", "셋째", "넷째"]
    st_objs = [{"step": i + 1, "highlight": [], "strike": [], "note": x} for i, x in enumerate(steps)]
    s4 = {"no": 4, "name": "풀이 순서", "sec": 36, "screen": {"text": item_txt, "highlight": [], "strike": [], "marks": {}, "steps": st_objs, "reveal": []},
          "narration": " ".join(f"{ords[i]}, {tts(x)}" for i, x in enumerate(steps)), "caption": " → ".join(short(x, 14) for x in steps)}
    marks = {C5[i]: ("✓" if i + 1 == a else "✗") for i in range(5)}
    lines5 = [f"{C5[i]} {x}  {'✓' if i + 1 == a else '✗'}  {short(reasons[i])}" for i, x in enumerate(c)]
    wrong = [i for i in range(5) if i + 1 != a]
    pick = sorted(wrong, key=lambda i: -len(reasons[i]))[:3]; pick.sort()
    nar5 = tts(keyj or f"정답은 {C5[a-1]}이다.") + " " + " ".join(f"{i+1}번: {tts(reasons[i])}" for i in pick)
    s5 = {"no": 5, "name": "선택지 확인", "sec": 26, "screen": {"text": "\n".join(lines5), "highlight": [], "strike": [], "marks": marks, "reveal": lines5},
          "narration": nar5, "caption": f"정답 {C5[a-1]}, 오답 이유 확인"}
    s6 = {"no": 6, "name": "정리", "sec": 10, "screen": {"text": f"정답 {C5[a-1]} {c[a-1]}\n\n{rule_lines[0]}", "highlight": [c[a-1]], "strike": [], "marks": {}, "reveal": [f"정답 {C5[a-1]} {c[a-1]}", rule_lines[0]]},
          "narration": f"정답은 {a}번. 기억할 것: {tts(rule_lines[0])}", "caption": f"정답 {C5[a-1]}"}
    scenes = [s1, s2, s3, s4, s5, s6]
    return {"key": key, "type": T, "grade": g, "chapter": f"{ch} {chn}", "title": "", "total_sec": sum(s["sec"] for s in scenes), "style": STYLE, "scenes": scenes,
            "source": {"stem": it["stem"], "passage": it.get("passage") or "", "c": c, "ans": a, "expl": expl, "judge": judge}}

def load_all(types):
    idx = json.load(open(HERE / "page/data/index.json", encoding="utf-8")); ref = json.load(open(HERE / "page/data/ref.json", encoding="utf-8"))
    chof = {f"{g}-{n}": (c["ch"], c["chn"]) for g, chs in idx["grades"].items() for c in chs for n in c["nos"]}
    base = {t: {f"{r['g']}-{r['n']}": r for r in json.load(open(HERE / f"page/data/{t}.json", encoding="utf-8"))} for t in "BCDEF" if t in types}
    def eff(t, k):
        f = HERE / f"src/db_t{t}_20261028/{k}.json"
        e = json.load(open(f, encoding="utf-8")).get("edit") if f.exists() else None
        it = FI.merged_edit(base[t][k], e); return {"stem": it["stem"], "passage": it["passage"] or "", "c": list(it["c"]), "ans": int(it["ans"]), "expl": it["expl"]}
    for k in idx["order"]:
        g = int(k.split("-")[0]); ch, chn = chof[k]
        if "A" in types:
            r = ref[k]; yield k, "A", {"stem": r["stem"], "passage": r["passage"] or "", "c": r["c"], "ans": int(r["ans"]), "expl": r.get("expl", "")}, g, ch, chn
        for t in "BCDEF":
            if t in types: yield k, t, eff(t, k), g, ch, chn

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); ap.add_argument("--types", default="ABCDEF"); ap.add_argument("keys", nargs="*")
    a = ap.parse_args(); out = Path(a.out); out.mkdir(parents=True, exist_ok=True); n = 0
    for k, T, it, g, ch, chn in load_all(a.types):
        if a.keys and k not in a.keys: continue
        doc = build(k, T, it, g, ch, chn)
        json.dump(doc, open(out / f"{k}-{T}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1); n += 1
    print(n, "drafts →", out)
