"""수정 예시 기록: F(급, 번호, 유형, ...) 로 한 문항씩 등록한다.
st 발문('R' = 원문항 발문, 생략 = 변형 그대로) / p 본문 / c 보기 5개 / a 정답
r 핵심 규칙(생략 = 변형 해설의 것) / k 정답 판단 / pre 보기 앞 판정 줄들 / n 보기별 해설 5개
op 'sortc' = 개수 선택지 정렬 / s 수정 요지(필수)"""
FIX = {}
def F(g_, no_, t_, /, **kw):
    key = (g_, no_, t_)
    assert key not in FIX, f"중복 등록 {key}"
    assert kw.get("s"), f"수정 요지 없음 {key}"
    FIX[key] = kw

# ---- fx 파일에서 쓰는 공용 도우미 ----
import json as _json, re as _re
_ROWS = {}
def V(g, n, t):
    """변형 문항 원래 값(dict: stem, passage, c, ans, expl ...)"""
    if t not in _ROWS:
        _ROWS[t] = {f'{r["g"]}-{r["n"]}': r for r in _json.load(open(f"page/data/{t}.json", encoding="utf-8"))}
    return _ROWS[t][f"{g}-{n}"]
_REF = None
def R(g, n):
    global _REF
    if _REF is None: _REF = _json.load(open("page/data/ref.json", encoding="utf-8"))
    return _REF[f"{g}-{n}"]

def tense(x):
    """동사 덩어리의 시제 이름"""
    x = x.strip()
    if _re.match(r"had been \w+ing\b", x): return "과거완료진행"
    if _re.match(r"(has|have) been \w+ing\b", x): return "현재완료진행"
    if _re.match(r"(was|were) \w+ing\b", x): return "과거진행"
    if _re.match(r"(is|are|am) \w+ing\b", x): return "현재진행"
    if _re.match(r"(was|were) \w+(ed|en|n|t)\b", x): return "be동사 과거 + 과거분사(수동·상태)"
    if _re.match(r"had \w+", x): return "과거완료"
    if _re.match(r"(has|have) \w+", x): return "현재완료"
    if _re.match(r"will have \w+", x): return "미래완료"
    if _re.match(r"will \w+", x): return "미래"
    return None

AUXN = {"has": "현재완료의 has", "have": "현재완료의 have", "had": "과거완료의 had", "was": "be동사 과거 was", "were": "be동사 과거 were", "is": "be동사 현재 is", "are": "be동사 현재 are", "will": "미래의 will", "did": "과거 의문문의 did", "do": "현재 의문문의 do", "does": "현재 의문문의 does", "am": "be동사 현재 am"}
IRR_PAST = set("rode drank sold took found left got began lost made went came saw ate wrote bought thought brought caught taught ran sang swam gave told said met kept slept felt sat stood won spoke broke chose drove flew grew knew threw wore forgot hid fell held heard paid sent spent built lent meant understood became did had was were".split())
def vform(p):
    p = p.strip()
    if p.lower() in AUXN: return AUXN[p.lower()].replace(p.lower(), p) if p[0].isupper() else AUXN[p.lower()]
    t = tense(p)
    if t: return t
    w = p.split()[0]
    if w.lower() == "to" and len(p.split()) > 1: return "to부정사"
    if w in IRR_PAST: return "단순과거"
    if w.endswith("ing"): return "-ing형"
    if w.endswith("ed"): return "단순과거"
    if w.endswith("s") and not w.endswith("ss"): return "현재형"
    return "동사원형"
def _split(ch):
    parts = [x.strip() for x in _re.split(r"\s+[-—–]\s+", ch)]
    return [_re.sub(r"^\([A-E]\)\s*", "", x) for x in parts]
def tnotes(c, ans, need, k="", labs=None, plain=False):
    """짝 고르기 보기별 해설. 정답 보기와 다른 자리만 짚는다.
    need = 자리별 근거 문장(예: '과거의 기준 사건까지 계속된 동작에는 had been + -ing을 쓴다.')"""
    good = _split(c[ans - 1]); out = []
    for i, ch in enumerate(c):
        if i + 1 == ans: out.append((k + " " if k else "") + "모든 자리가 알맞으므로 정답이다."); continue
        parts = _split(ch); bits = []
        for j, x in enumerate(parts):
            if j < len(good) and x != good[j]:
                lab = (labs[j] if labs else ["첫째 빈칸", "둘째 빈칸", "셋째 빈칸", "넷째 빈칸"][j])
                desc = "" if plain or _re.search(r"[가-힣]", x) else vform(x) + "이어서 "
                bits.append(f"{lab} {x}: {desc}맞지 않는다. {need[j]}")
        out.append(" ".join(bits) + " 따라서 오답이다.")
    return out

def setnotes(c, wrong, what="틀린 문장"):
    """'A, C, E' 같은 조합 보기 해설. wrong = 정답 집합(예: 'A, C, E')"""
    W = [x.strip() for x in wrong.split(",")]; out = []
    for ch in c:
        S = [x.strip() for x in ch.split(",")]
        extra = [x for x in S if x not in W]; miss = [x for x in W if x not in S]
        if not extra and not miss: out.append(f"{what} {', '.join(W)}를 빠짐없이 골랐으므로 정답이다."); continue
        bits = []
        if extra: bits.append(f"{', '.join(extra)}는 {what}이 {'아니고' if miss else '아니다'}")
        if miss: bits.append(f"{what} {', '.join(miss)}를 빠뜨렸다")
        out.append(", ".join(bits) + ". 따라서 오답이다.")
    return out

MOD = {"should": "했어야 했다는 후회·비판", "might": "그랬을지도 모른다는 불확실한 추측", "may": "그랬을지도 모른다는 추측",
       "could": "그럴 수도 있었다는 가능성", "must": "틀림없이 그랬을 것이라는 강한 확신", "cannot": "그랬을 리 없다는 강한 부정 추측",
       "can't": "그랬을 리 없다는 강한 부정 추측", "must not": "그러지 않았음이 틀림없다는 확신", "should not": "하지 말았어야 했다는 후회"}
def mnotes(c, ans, ctx, k=""):
    """(A) x - (B) y 조동사 짝 해설. ctx = 자리별 흐름 설명(예: '하지 않은 일을 아쉬워하는 흐름')"""
    good = _split(c[ans - 1]); out = []
    for i, ch in enumerate(c):
        parts = _split(ch)
        if i + 1 == ans:
            out.append((k + " " if k else "") + " ".join(f"({'ABCD'[j]}) {x}는 {ctx[j]}에 맞는다." for j, x in enumerate(parts)) + " 따라서 정답이다."); continue
        bits = [f"({'ABCD'[j]}) {x} have + 과거분사는 {MOD.get(x, x)}을 나타내므로 {ctx[j]}에 맞지 않는다." for j, x in enumerate(parts) if j < len(good) and x != good[j]]
        out.append(" ".join(bits) + " 따라서 오답이다.")
    return out


# ---- 2026-10-06 감수 메모 반영용 도우미(fx/z*.py에서 쓴다) ----
C5 = "①②③④⑤"
def RE(g_, n_, t_, **kw):
    """기존 수정 예시(F 등록)를 바탕으로 일부만 바꿔 다시 등록한다. 없으면 새로 등록한다."""
    old = FIX.pop((g_, n_, t_), None) or {}
    if "n" in kw or "x" in kw:
        for k_ in ("x", "keepx", "okx", "op", "xr"): old.pop(k_, None)
    if "c" in kw and not ({"n", "x", "keepx", "okx"} & (set(kw) | set(old))):
        raise AssertionError(f"{(g_, n_, t_)} 보기를 바꾸면 해설(n)이 필요")
    old.update(kw); F(g_, n_, t_, **old)
def OLD(g_, n_, t_): return FIX.get((g_, n_, t_)) or {}
def OK(i, a): return " 정답이다." if i == a else " 오답이다."
def pos(a): return f" 정답 위치 {C5[a-1]}."
def numc(): return list(C5)
def numbered(words):
    """낱말 사이에 ①~⑤를 넣은 문장: ['My','cousin','lives','Seoul','.'] → '① My ② cousin ③ lives ④ Seoul ⑤.'"""
    out = []
    for i, w in enumerate(words):
        out.append(C5[i] + ("" if w == "." else " ") + w)
    return " ".join(out).replace(" ⑤.", " ⑤.")
MEMO = "감수 메모 반영: "
