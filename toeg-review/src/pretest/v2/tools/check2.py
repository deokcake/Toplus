#!/usr/bin/env python3
"""프리테스트 문항 초안 자동 점검(2판: 난이도 맞추기 — 길이 상한·무거운 형식 금지 추가).
사용: python3 check2.py <초안.json> <입력 배치.json>
초안.json: [{"key","stem","passage","c":[5],"ans":1~5,"expl"}...]  (다른 필드는 무시)
ERR = 반드시 고칠 것, WARN = 확인할 것."""
import json, re, sys

LAB = re.compile(r"\((?:[A-E]|가|나|다|라|마|_ ?[A-E] ?_)\)|[ⓐ-ⓔ]|<보기>|<조건>|</?u>|_+|[①-⑤]")
def body(it):
    s = (it.get("passage") or "") + " " + " ".join(it["c"])
    return LAB.sub(" ", s)
def mw(it): return len(re.findall(r"[A-Za-z']+", body(it)))
def mc(it): return len(re.sub(r"\s+", "", re.sub(r"[,.!?]", "", body(it))))
CIRC = "①②③④⑤"

def sents(it):
    out = []
    for part in [(it.get("passage") or "")] + list(it["c"]):
        for line in re.split(r"\n|(?<=[.?!])\s+", part):
            t = re.sub(r"<[^>]+>", "", line)
            t = re.sub(r"\((?:[A-E]|가|나|다|라|마)\)|[ⓐ-ⓔ①-⑤]|_+", " ", t)
            w = re.findall(r"[a-z']+", t.lower())
            if len(w) >= 5: out.append(tuple(w))
    return out

def kind(it):
    c = [str(x).strip() for x in it["c"]]
    if all(re.fullmatch(r"\d\s*개", x) for x in c): return "count", 0
    if all(re.fullmatch(r"[ⓐ-ⓔ(A-E)가-마,\s]+", x) for x in c) and any("," in x for x in c): return "combo", 0
    k = max(len(re.findall(r"\([A-E]\)", x)) for x in c)
    return ("pair", k) if k >= 2 else ("single", 0)

def check(it, inp):
    E, W = [], []
    k = it.get("key"); ref = inp["ref"]
    c = it.get("c") or []
    if len(c) != 5 or any(not str(x).strip() for x in c): E.append("보기는 비지 않은 5개여야 함")
    norm = [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", str(x))).strip().lower() for x in c]
    if len(set(norm)) < len(norm): E.append("같은 보기가 있음")
    a = it.get("ans")
    if not isinstance(a, int) or not 1 <= a <= 5: E.append(f"정답 번호 오류: {a!r}"); return E, W
    at = str(c[a - 1]).strip()
    if at in ("0개", "없음", "없다", "0") or re.fullmatch(r"0\s*개", at): E.append("정답이 0개/없음 — 금지")
    labs = re.findall(r"^\s*(?:[ⓐ-ⓔ]|\([A-E]\)|\((?:가|나|다|라|마)\))", it.get("passage") or "", re.M)
    m = re.fullmatch(r"(\d)\s*개", at)
    if m and labs and int(m.group(1)) == len(labs): W.append(f"정답 {at} = 제시 문장 전부({len(labs)}개) — 다 맞거나 다 틀린 구성은 피할 것")
    if all(re.fullmatch(r"\d\s*개", str(x).strip()) for x in c):
        nums = [int(re.match(r"\d", str(x).strip()).group()) for x in c]
        if nums != sorted(nums): W.append("개수 보기는 작은 수부터 차례로")
        if 0 in nums: W.append("개수 보기에 0개가 있음(정답이 아니어도 가급적 1개~5개)")
    if inp.get("target_answer_position") and a != inp["target_answer_position"]:
        W.append(f"정답 위치 {CIRC[a-1]} (권장 {CIRC[inp['target_answer_position']-1]})")
    for f in ("stem", "passage"):
        s = it.get(f) or ""
        if s.count("<u>") != s.count("</u>"): E.append(f"{f} 밑줄 태그 짝이 안 맞음")
        if "\\n" in s: E.append(f"{f}에 글자 \\n이 들어 있음(실제 줄바꿈을 쓸 것)")
    for i, x in enumerate(c):
        if str(x).count("<u>") != str(x).count("</u>"): E.append(f"보기 {i+1} 밑줄 태그 짝이 안 맞음")
    if not re.search(r"(고르시오\.|고르세요\.|\?)\s*$", it.get("stem") or ""): W.append("발문 끝맺음 확인(…고르시오. / …것은?)")
    psg = it.get("passage") or ""
    nb = len(re.findall(r"_{3,}", psg))
    if nb >= 2 and not re.search(r"\([A-E]\)", psg): W.append("빈칸이 둘 이상인데 (A)·(B) 표시가 없음")
    # 길이
    rw, rc, nw, nc = mw(ref), mc(ref), mw(it), mc(it)
    if nw < rw or nc < rc: E.append(f"원문항보다 짧음: 낱말 {nw}/{rw}, 글자 {nc}/{rc} (지문+보기, 표시 기호 뺀 것)")
    # 2판: 길이 상한(원문항 1.3배 안팎, 최대 1.5배 / 아주 짧은 원문항은 +8낱말)
    cap = max(int(rw * 1.5), rw + 8)
    if nw > cap: E.append(f"원문항보다 너무 김: 낱말 {nw} > 상한 {cap} (원문항 {rw}) — 난이도가 올라감")
    elif nw > max(rw * 1.3, rw + 5): W.append(f"원문항의 {nw / max(rw, 1):.1f}배 — 1.3배 안팎으로 줄일 수 있는지")
    # 2판: 원문항에 없던 무거운 형식 금지
    rk, rn = kind(ref); nk, nn = kind(it)
    if nk == "count" and rk != "count": E.append("원문항이 개수형이 아닌데 개수 세기 형식 — 난이도가 올라감")
    if nk == "combo" and rk != "combo": E.append("원문항이 조합형이 아닌데 조합 고르기 형식 — 난이도가 올라감")
    if nk == "pair" and nn >= 3 and not (rk == "pair" and rn >= 3): E.append(f"빈칸 {nn}개 짝 고르기 — 원문항보다 판단할 곳이 많음")
    if nk == "pair" and nn == 2 and rk not in ("pair", "combo", "count"): W.append("원문항은 한 곳만 판단하는데 두 빈칸 짝 — 판단 개수가 늘지 않았는지")
    # 원문항·B~F 문장 재사용
    olds = {}
    for name, x in [("원문항", ref)] + [(t + "유형", v) for t, v in inp["existing_variants_BtoF"].items()]:
        for s in sents(x): olds.setdefault(s, name)
    for s in sents(it):
        if s in olds: E.append(f"{olds[s]} 문장을 그대로 씀: {' '.join(s)}"); continue
        for o, name in olds.items():
            a1, b1 = set(s), set(o)
            if len(a1 & b1) / max(1, len(a1 | b1)) >= 0.8 and abs(len(s) - len(o)) <= 2:
                W.append(f"{name} 문장과 거의 같음: {' '.join(s)}  ~  {' '.join(o)}"); break
    # 해설 짜임
    ex = it.get("expl") or ""
    lines = ex.split("\n")
    if not ex.startswith("핵심 규칙:"): E.append("해설은 ‘핵심 규칙:’으로 시작")
    for h in ("풀이 순서:", "문장별 판정:", "정답 판단:", "선택지 분석:"):
        if not any(l.startswith(h) for l in lines): E.append(f"해설에 ‘{h}’ 줄이 없음")
    order = [i for h in ("핵심 규칙:", "풀이 순서:", "문장별 판정:", "정답 판단:", "선택지 분석:") for i, l in enumerate(lines) if l.startswith(h)][:5]
    if order != sorted(order): E.append("해설 순서: 핵심 규칙 → 풀이 순서 → 문장별 판정 → 정답 판단 → 선택지 분석")
    opt = [l for l in lines if re.match(r"^[①-⑤] \[(정답|오답)\]", l)]
    if len(opt) != 5 or [l[0] for l in opt] != list(CIRC): E.append("선택지 분석은 ①~⑤ 다섯 줄([정답]/[오답])")
    else:
        right = [i + 1 for i, l in enumerate(opt) if "[정답]" in l]
        if right != [a]: E.append(f"선택지 분석의 [정답] 표시 {right} ≠ 정답 {a}")
    st = next((l for l in lines if l.startswith("풀이 순서:")), "")
    if st and not ("→ ②" in st and "①" in st): W.append("풀이 순서는 ① … → ② … → ③ … 꼴")
    if st and "정답은" not in st: W.append("풀이 순서 끝에 ‘정답은 …’")
    if re.search(r"(?<![①-⑤선택지 ])[①-⑤]\s*[은는의이가을]", st.replace("선택지 ", "선택지_")) and re.search(r"→ [①-⑤]\s", st): pass
    if re.search(r"→ ③ [①-⑤](?!\s*[.,]) ", st) or re.search(r"→ ② [①-⑤](?!\s*[.,]) ", st): W.append("풀이 순서 단계 번호 바로 뒤의 보기 번호는 ‘선택지 ④’처럼")
    for bad, why in (("..", "마침표 겹침"), ("?.", "‘?.’"), ("  ", "두 칸 띄어쓰기"), ("을(를)", "조사 병기"), ("이(가)", "조사 병기"), ("와(과)", "조사 병기"), ("은(는)", "조사 병기")):
        if bad in ex: W.append(f"해설에 {why}")
    sj = []; on = False
    for l in lines:
        if l.startswith("문장별 판정:"): on = True; continue
        if l.startswith("정답 판단:"): break
        if on and l.strip(): sj.append(l)
    if labs and len(sj) < len(labs): W.append(f"문장별 판정 줄 {len(sj)}개 < 제시 문장 {len(labs)}개")
    return E, W

def main():
    drafts = json.load(open(sys.argv[1], encoding="utf-8"))
    if isinstance(drafts, dict): drafts = drafts.get("items", [])
    inp = {x["key"]: x for x in json.load(open(sys.argv[2], encoding="utf-8"))}
    ne = 0; ans = []
    for it in drafts:
        k = it.get("key")
        if k not in inp: print(f"[{k}] ERR 입력 배치에 없는 key"); ne += 1; continue
        E, W = check(it, inp[k]); ne += len(E); ans.append(it.get("ans"))
        print(f"[{k}] 낱말 {mw(it)}/{mw(inp[k]['ref'])} 글자 {mc(it)}/{mc(inp[k]['ref'])} 정답 {it.get('ans')}" + ("  OK" if not E and not W else ""))
        for e in E: print("   ERR ", e)
        for w in W: print("   WARN", w)
    missing = [k for k in inp if k not in {d.get("key") for d in drafts}]
    if missing: print("ERR 빠진 문항:", missing); ne += len(missing)
    from collections import Counter
    print("정답 분포:", dict(sorted(Counter(ans).items())), "| ERR", ne)

if __name__ == "__main__": main()
