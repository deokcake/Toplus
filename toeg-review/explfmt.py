#!/usr/bin/env python3
"""해설의 짜임을 하나로 맞춘다: 핵심 규칙 → 풀이 순서 → 문장별 판정 → 정답 판단 → 선택지 분석.
parse(text)  어떤 꼴의 해설이든 다섯 부분으로 가른다.
compose(p)   다섯 부분을 정해진 순서의 글로 엮는다(문장별 판정이 없으면 빈칸).
페이지(index.html)의 splitExpl()이 같은 규칙으로 엑셀 칸을 나눈다."""
import re
C = "①②③④⑤"
HEAD = {"[선택지별 구체 해설]", "[상세 해설]", "선택지별 해설", "[선택지별 해설]", "선택지별 분석", "선택지 분석", "선택지 분석:", "선택지별 분석:"}
RULE = re.compile(r"^(?:핵심 규칙|판단 기준)\s*[:：]\s*")
STEP = re.compile(r"^풀이 순서\s*[:：]\s*")
KEY = re.compile(r"^정답 판단\s*[:：]\s*")
JUDGE = re.compile(r"^[^:：①-⑤]{0,8}판정\s*[:：]\s*")
DONE = re.compile(r"^완성 문장\s*[:：]\s*")

def parse(text):
    p = {"rule": [], "steps": [], "judge": [], "key": [], "done": [], "opts": [[] for _ in C]}
    cur = None
    for raw in str(text or "").replace("\r", "").split("\n"):
        l = raw.strip()
        if not l or l in HEAD: continue
        if l[0] in C:
            i = C.index(l[0]); p["opts"][i].append(l[1:].strip()); cur = ("opt", i); continue
        for name, pat in (("rule", RULE), ("steps", STEP), ("key", KEY), ("judge", JUDGE), ("done", DONE)):
            m = pat.match(l)
            if m:
                rest = l[m.end():].strip()
                if rest: p[name].append(rest)
                cur = (name, None); break
        else:
            if cur and cur[0] == "opt": p["opts"][cur[1]].append(l)
            elif cur and cur[0] in ("steps", "key"): p[cur[0]].append(l)
            else: p["judge"].append(l)      # 규칙·판정 뒤에 이어지는 문장별 판정 줄
    return p

def derive_key(opt_lines, sym):
    """정답 보기의 해설에서 ‘정답 판단’ 한 줄을 만든다."""
    t = " ".join(opt_lines).strip()
    t = re.sub(r"^\[정답\]\s*", "", t)
    if not t: return f"정답은 {sym}이다."
    if re.search(r"정답이다\.?$", t): return re.sub(r"정답이다\.?$", f"정답은 {sym}이다.", t)
    if re.search(r"니다\.?\s*(?:바르게 고치면.*)?$", t): return f"정답은 {sym}입니다. {t}"
    return f"{t} 따라서 정답은 {sym}이다." if t.endswith(".") else f"{t}. 따라서 정답은 {sym}이다."

def fill(p, ans, rule=""):
    """빠진 핵심 규칙·정답 판단을 채운다. ans = 정답 번호(1~5)."""
    if not p["rule"] and rule: p["rule"] = [rule]
    if not p["key"] and 1 <= int(ans) <= 5: p["key"] = [derive_key(p["opts"][int(ans) - 1], C[int(ans) - 1])]
    if p["done"]:
        p["key"] = ["완성 문장: " + " ".join(p["done"])] + p["key"]; p["done"] = []
    return p

def compose(p):
    out = ["핵심 규칙: " + " ".join(p["rule"]), "풀이 순서: " + " ".join(p["steps"])]
    j = p["judge"]
    out.append("문장별 판정:" + (" " + j[0] if len(j) == 1 else ""))
    if len(j) > 1: out += j
    out.append("정답 판단: " + " ".join(p["key"]))
    out.append("선택지 분석:")
    for i, o in enumerate(p["opts"]):
        if o: out.append(C[i] + " " + o[0]); out += o[1:]
    return "\n".join(tidy(x.rstrip()) for x in out)

_ALT = {"을(를)": ("을", "를"), "를(을)": ("을", "를"), "이(가)": ("이", "가"), "가(이)": ("이", "가"), "은(는)": ("은", "는"), "는(은)": ("은", "는"), "과(와)": ("과", "와"), "와(과)": ("과", "와")}
_CLOSED = {"at", "it", "but", "not", "get", "cut", "put", "up", "cup", "book"}   # 짧게 닫힌 음절이라 받침으로 읽는 영어 낱말(앳, 잇, 컵 …)
def _batchim(w):
    """낱말 끝소리에 받침이 있는가. 한글은 글자로, 영어는 읽는 소리로 어림한다(-l·-m·-n·-ng는 받침, -t·-d·-s 등은 ‘트·드·스’로 읽혀 받침 없음)."""
    c = w[-1]
    if "가" <= c <= "힣": return (ord(c) - 0xAC00) % 28 != 0
    w = w.lower()
    return w in _CLOSED or bool(re.search(r"(ng|[lmn])$", w))
def tidy(line):
    """기계로 이어 붙인 글의 흔적을 정리한다: 마침표 두 개, ‘?.’, 띄어쓰기 두 칸, ‘을(를)’ 같은 조사 병기."""
    line = re.sub(r"(?<!\.)\.\.(?!\.)", ".", line)
    line = re.sub(r"([?!])\.(?=\s|$)", r"\1", line)
    line = re.sub(r"(?<=\S) {2,}(?=\S)", " ", line)
    alt = "|".join(re.escape(a) for a in _ALT)
    return re.sub(rf"([가-힣A-Za-z']+)({alt})", lambda m: m.group(1) + _ALT[m.group(2)][0 if _batchim(m.group(1)) else 1], line)

def cells(p):
    """엑셀 칸: 핵심 규칙, 풀이 순서, 문장별 판정, 정답 판단, 선택지 ①~⑤ 분석"""
    return [" ".join(p["rule"]), " ".join(p["steps"]), "\n".join(p["judge"]), " ".join(p["key"])] + ["\n".join(o) for o in p["opts"]]

def restructure(text, ans, rule=""):
    return compose(fill(parse(text), ans, rule))

def unlabel(it):
    """본문·보기에 (A)·(B) 표시가 없는 두 빈칸(밑줄) 문항인데 해설이 (A)·(B)로 가리키면 ‘첫째 빈칸’·‘둘째 빈칸’(밑줄 문항은 ‘밑줄’)으로 바꾼다."""
    body = it["stem"] + it["passage"] + "".join(it["c"])
    if "(A) " not in it["expl"] or re.search(r"\(\s*(?:<u>)?\s*A\s*(?:</u>)?\s*\)|Ⓐ", body): return it["expl"]
    w = "빈칸" if re.search(r"_{3,}", it["passage"]) else "밑줄"
    return it["expl"].replace("(A) ", f"(첫째 {w}) ").replace("(B) ", f"(둘째 {w}) ")

if __name__ == "__main__":
    import json
    ref = json.load(open("page/data/ref.json", encoding="utf-8"))
    t = ref["1-5"]["expl"]; print(restructure(t, ref["1-5"]["ans"])); print(cells(parse(restructure(t, ref["1-5"]["ans"]))))
