#!/usr/bin/env python3
"""‘핵심 확인’ 변형 문항(번호마다 3개) 초안 자동 점검. check2.py(프리테스트 2판)에서 해설 점검을 빼고
세 변형이 서로 다른 형식인지, 원문항·B~F·프리테스트·다른 변형의 문장을 다시 쓰지 않았는지를 더했다.
사용: python3 check3.py <초안.json> <입력 배치.json>
초안.json: [{"key","variant":1~3,"stem","passage","c":[5],"ans":1~5, ...}]  ERR = 반드시 고칠 것, WARN = 확인할 것."""
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

def norm_stem(s): return re.sub(r"[\s‘’'\"().,?]", "", s or "")

def check(it, inp, siblings):
    """it = 변형 하나, inp = 그 번호의 입력, siblings = 같은 번호의 다른 변형들"""
    E, W = [], []
    ref = inp["ref"]; c = it.get("c") or []
    if len(c) != 5 or any(not str(x).strip() for x in c): E.append("보기는 비지 않은 5개여야 함")
    norm = [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", str(x))).strip().lower() for x in c]
    if len(set(norm)) < len(norm): E.append("같은 보기가 있음")
    a = it.get("ans")
    if not isinstance(a, int) or not 1 <= a <= 5: E.append(f"정답 번호 오류: {a!r}"); return E, W
    v = it.get("variant")
    if v not in (1, 2, 3): E.append(f"variant는 1~3: {v!r}")
    at = str(c[a - 1]).strip()
    if at in ("0개", "없음", "없다", "0") or re.fullmatch(r"0\s*개", at): E.append("정답이 0개/없음 — 금지")
    labs = re.findall(r"^\s*(?:[ⓐ-ⓔ]|\([A-E]\)|\((?:가|나|다|라|마)\))", it.get("passage") or "", re.M)
    m = re.fullmatch(r"(\d)\s*개", at)
    if m and labs and int(m.group(1)) == len(labs): W.append(f"정답 {at} = 제시 문장 전부({len(labs)}개) — 다 맞거나 다 틀린 구성은 피할 것")
    if all(re.fullmatch(r"\d\s*개", str(x).strip()) for x in c):
        nums = [int(re.match(r"\d", str(x).strip()).group()) for x in c]
        if nums != sorted(nums): W.append("개수 보기는 작은 수부터 차례로")
        if 0 in nums: W.append("개수 보기에 0개가 있음")
    tp = (inp.get("target_answer_positions") or [None, None, None])
    if v in (1, 2, 3) and tp[v - 1] and a != tp[v - 1]: W.append(f"정답 위치 {CIRC[a-1]} (권장 {CIRC[tp[v-1]-1]})")
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
    cap = max(int(rw * 1.5), rw + 8)
    if nw > cap: E.append(f"원문항보다 너무 김: 낱말 {nw} > 상한 {cap} (원문항 {rw}) — 난이도가 올라감")
    elif nw > max(rw * 1.3, rw + 5): W.append(f"원문항의 {nw / max(rw, 1):.1f}배 — 1.3배 안팎으로 줄일 수 있는지")
    # 무거운 형식
    rk, rn = kind(ref); nk, nn = kind(it)
    if nk == "count" and rk != "count": E.append("원문항이 개수형이 아닌데 개수 세기 형식 — 난이도가 올라감")
    if nk == "combo" and rk != "combo": E.append("원문항이 조합형이 아닌데 조합 고르기 형식 — 난이도가 올라감")
    if nk == "pair" and nn >= 3 and not (rk == "pair" and rn >= 3): E.append(f"빈칸 {nn}개 짝 고르기 — 원문항보다 판단할 곳이 많음")
    if nk == "pair" and nn == 2 and rk not in ("pair", "combo", "count"): W.append("원문항은 한 곳만 판단하는데 두 빈칸 짝 — 판단 개수가 늘지 않았는지")
    # 형식이 원문항·다른 변형과 다른가
    if norm_stem(it.get("stem")) == norm_stem(ref.get("stem")): E.append("발문이 원문항과 같음 — 형식을 옆으로 바꿀 것")
    for sb in siblings:
        if norm_stem(sb.get("stem")) == norm_stem(it.get("stem")): E.append(f"변형 {sb.get('variant')}과 발문이 같음 — 세 변형은 서로 다른 형식")
        if (sb.get("new_format") or "").strip() and (sb.get("new_format") or "").strip() == (it.get("new_format") or "").strip(): W.append(f"변형 {sb.get('variant')}과 new_format이 같음")
    # 문장 재사용(원문항·B~F·프리테스트·다른 변형)
    olds = {}
    srcs = [("원문항", ref)] + [(t + "유형", x) for t, x in inp["existing_variants_BtoF"].items()]
    if inp.get("existing_pretest"): srcs.append(("프리테스트", inp["existing_pretest"]))
    srcs += [(f"변형 {sb.get('variant')}", sb) for sb in siblings]
    for name, x in srcs:
        for s in sents(x): olds.setdefault(s, name)
    for s in sents(it):
        if s in olds: E.append(f"{olds[s]} 문장을 그대로 씀: {' '.join(s)}"); continue
        for o, name in olds.items():
            a1, b1 = set(s), set(o)
            if len(a1 & b1) / max(1, len(a1 | b1)) >= 0.8 and abs(len(s) - len(o)) <= 2:
                W.append(f"{name} 문장과 거의 같음: {' '.join(s)}  ~  {' '.join(o)}"); break
    # 낱말 보기 문항: 보기 묶음이 다른 출처와 거의 같은가(문장 재사용 검사는 5낱말 이상 문장만 보므로 따로 본다)
    mine = set(norm)
    for name, x in srcs:
        theirs = {re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", str(y))).strip().lower() for y in x.get("c", [])}
        same = len(mine & theirs)
        if same >= 4: E.append(f"{name}과 보기가 {same}개 같음 — 새 보기로")
        elif same == 3: W.append(f"{name}과 보기가 3개 같음")
    # 정답 보기가 원문항 정답 보기와 같은가(낱말 하나짜리 정답은 허용)
    ra = str(ref["c"][int(ref["ans"]) - 1]).strip().lower(); na = at.lower()
    if ra == na and len(re.findall(r"[a-z']+", na)) >= 3: W.append("정답 보기가 원문항 정답 보기와 같음")
    return E, W

def main():
    drafts = json.load(open(sys.argv[1], encoding="utf-8"))
    if isinstance(drafts, dict): drafts = drafts.get("items", [])
    inp = {x["key"]: x for x in json.load(open(sys.argv[2], encoding="utf-8"))}
    by = {}
    for it in drafts: by.setdefault(it.get("key"), []).append(it)
    ne = 0; ans = []
    for it in drafts:
        k = it.get("key")
        if k not in inp: print(f"[{k}#{it.get('variant')}] ERR 입력 배치에 없는 key"); ne += 1; continue
        sibs = [x for x in by[k] if x is not it]
        E, W = check(it, inp[k], sibs); ne += len(E); ans.append(it.get("ans"))
        print(f"[{k}#{it.get('variant')}] 낱말 {mw(it)}/{mw(inp[k]['ref'])} 글자 {mc(it)}/{mc(inp[k]['ref'])} 정답 {it.get('ans')}" + ("  OK" if not E and not W else ""))
        for e in E: print("   ERR ", e)
        for w in W: print("   WARN", w)
    for k in inp:
        vs = sorted(x.get("variant") for x in by.get(k, []))
        if vs != [1, 2, 3]: print(f"ERR {k}: 변형이 1·2·3 하나씩 있어야 함(지금 {vs})"); ne += 1
    from collections import Counter
    print("정답 분포:", dict(sorted(Counter(ans).items())), "| ERR", ne)

if __name__ == "__main__": main()
