#!/usr/bin/env python3
"""TOEG 변형 문항(B~F) 자동 1차 점검.

기준 문항(docx에서 뽑은 ref.json)과 변형 문항(엑셀에서 뽑은 B.json~F.json)을
(급수, 문제번호)로 짝지어, 사람이 풀지 않아도 기계적으로 확인할 수 있는 항목을 점검한다.
결과: screen.json (변형마다 flags 목록)

    python3 screen.py <src 폴더>
"""
import difflib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
CIRC = "①②③④⑤"
TYPES = "BCDEF"


# ---------------- 파싱 ----------------
def parse_ref_item(text):
    lines = [l.rstrip() for l in text.split("\n")]
    m = re.match(r"(\d+)\.\s*(.*)", lines[0])
    stem = m.group(2).strip()
    answer = None
    body = []
    for l in lines[1:]:
        s = l.strip()
        if not s:
            continue
        if s.startswith("정답"):
            a = re.search(r"[①②③④⑤]", s)
            answer = CIRC.index(a.group()) + 1 if a else None
        else:
            body.append(s)
    tail = body[-5:]
    if len(tail) == 5 and all(tail[i].startswith(CIRC[i]) for i in range(5)):
        choices = [t[1:].strip() for t in tail]
        passage = "\n".join(body[:-5])
        inline = bool(re.search(r"[①②③④⑤]", passage))
    else:
        passage = "\n".join(body)
        inline = True
        # 지문 속 ①<u>…</u> 형식: 번호 뒤 밑줄 부분(없으면 다음 단어)을 선택지로 본다
        choices = [m.group(1) or m.group(2) for m in re.finditer(r"[①②③④⑤]\s*(?:<u>(.*?)</u>|(\S+))", passage)]
    return {"stem": stem, "passage": passage, "choices": choices, "answer": answer, "inline": inline}


def load():
    ref_raw = json.load(open(SRC / "ref.json", encoding="utf-8"))
    ref = {(int(g), int(n)): parse_ref_item(t) for g, items in ref_raw.items() for n, t in items.items()}
    var = {}
    for t in TYPES:
        for r in json.load(open(SRC / f"{t}.json", encoding="utf-8")):
            g = int(r["급수"].replace("급", ""))
            n = int(r["문제번호"])
            choices = [r[f"보기 문항{i}"].strip() for i in range(1, 6)]
            ans = r["정답"].strip()
            var[(t, g, n)] = {
                "type": t, "grade": g, "no": n, "chapter": r["챕터"], "chapter_name": r["챕터명"],
                "stem": r["문제명"].strip(), "passage": r["본문"].strip(), "choices": choices,
                "answer": int(ans) if ans.isdigit() else None, "answer_raw": ans, "expl": r["설명"],
            }
    return ref, var


# ---------------- 도우미 ----------------
def norm(s):
    s = re.sub(r"</?u>", "", s)
    s = s.replace("’", "'").replace("‘", "'").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


def stem_core(s):
    """괄호 속 부가 조건을 떼어 낸 발문 핵심."""
    return norm(re.sub(r"\([^)]*\)", "", s)).rstrip(".?")


TASKS = [
    ("개수", r"개수|몇 개"),
    ("배열", r"배열|번째"),
    ("다른 것", r"다른 것|다른 하나|쓰임이 다른|종류가 다른"),
    ("같은 것", r"같은 것|쓰임이 같은"),
    ("짝·연결", r"짝지어진|연결된|순서대로|짝지은"),
    ("틀린 것", r"어색|틀린|잘못|올바르지 않|올바르지 못|옳지 않|바르지 않|적절하지 않|알맞지 않|맞지 않|부자연"),
    ("옳은 것", r"옳은|올바른|알맞은|바른|자연스러운|적절한|맞는|들어갈"),
]


HINT_TERMS = (r"과거완료|현재완료|미래완료|과거진행|현재진행|진행형|단순현재|단순과거|현재형|과거형|미래형|능동|수동|"
              r"to부정사|동명사|원형부정사|동사원형|분사|관계대명사|관계부사|선행사|전치사|접속사|형용사|부사|최상급|비교급|원급|"
              r"가정법|조동사|3인칭|단수|복수|목적격|주격|소유격|재귀|목적어|보어|주어|that절|명사절|부사절|간접의문문|"
              r"도치|강조|수 일치|수일치|상태동사|셀 수 없는|불규칙|규칙 변화|의문사|부정문|의문문|명령문|감탄문|"
              r"had better|cannot but|used to|be going to|would rather|not only|as if|It ~ that")


def task_of(stem):
    s = re.sub(r"\([^)]*\)", "", stem)
    found = [name for name, pat in TASKS if re.search(pat, s)]
    return found[0] if found else "기타", found


def has_blank(s):
    return bool(re.search(r"_{2,}|\(\s*\)|\[\s*\]|빈칸", s))


LABEL_PATTERNS = [
    ("ⓐ", r"[ⓐⓑⓒⓓⓔⓕⓖ]"),
    ("(a)", r"(?:^|\s)\([a-gA-G]\)\s"),
    ("a)", r"(?:^|\s)[a-gA-G]\)\s"),
    ("A.", r"(?:^|\s)[A-G]\.\s"),
    ("a", r"(?:^|\s)[a-g]\s+(?=[A-Z])"),
]


def label_style(passage):
    for name, pat in LABEL_PATTERNS:
        if len(re.findall(pat, passage)) >= 2:
            return name
    return None


def labeled_count(passage):
    st = label_style(passage)
    return len(re.findall(dict(LABEL_PATTERNS)[st], passage)) if st else 0


def choice_form(choices):
    cs = [norm(c) for c in choices if c]
    if all(re.fullmatch(r"\d+\s*개", c) for c in cs):
        return "개수"
    if all(re.fullmatch(r"[ⓐ-ⓖa-gA-G가-하ㄱ-ㅎ㉠-㉦(),\s]+", c) or c in ("해당 없음", "없음") for c in cs):
        return "기호 조합"
    if all(" - " in c or " / " in c for c in cs):
        return "짝"
    words = [len(re.sub(r"<[^>]+>", "", c).split()) for c in choices if c]
    if words and max(words) <= 3:
        return "단어·구"
    return "문장"


def expl_marks(expl):
    """해설에서 선택지별 [정답] 표시를 찾는다."""
    marks = {}
    for line in expl.split("\n"):
        s = line.strip()
        if not s or s[0] not in CIRC:
            continue
        k = CIRC.index(s[0]) + 1
        head = s[:60]
        if re.search(r"\[정답\]|- 정답|— 정답|\(정답\)|정답\.", head):
            marks[k] = True
        elif re.search(r"\[오답\]|- 오답|오답\.", head):
            marks.setdefault(k, False)
    return marks


def count_judgments(expl):
    """개수형 해설의 '문장별 판정'에서 옳음/틀림 수."""
    ok = len(re.findall(r"(?:^|\n)\s*\(?[a-gⓐ-ⓖ]\)?\s*(?:옳음|O\b|\[옳음\])", expl))
    bad = len(re.findall(r"(?:^|\n)\s*\(?[a-gⓐ-ⓖ]\)?\s*(?:틀림|X\b|\[틀림\])", expl))
    return ok, bad


# ---------------- 점검 ----------------
def screen(ref, var):
    out = []
    by_ref = defaultdict(list)
    for key, v in var.items():
        by_ref[(v["grade"], v["no"])].append(v)

    for (t, g, n), v in sorted(var.items(), key=lambda kv: (kv[0][1], kv[0][2], kv[0][0])):
        r = ref[(g, n)]
        flags = []

        def flag(code, sev, msg):
            flags.append({"code": code, "sev": sev, "msg": msg})

        # A1 발문
        rt, rall = task_of(r["stem"])
        vt, vall = task_of(v["stem"])
        stem_same = stem_core(r["stem"]) == stem_core(v["stem"])
        added = re.findall(r"\(([^)]*)\)", v["stem"])
        near = {"틀린 것", "옳은 것", "짝·연결"}
        if rt != vt:
            hard = rt in near and vt in near or "기타" in (rt, vt)
            flag("A1", "◐", f"발문 과제 변경 의심: ‘{rt}’ → ‘{vt}’ (원: {r['stem']} / 변형: {v['stem']})")
        elif not stem_same:
            flag("A1", "note", f"발문 문구 변경(과제 동일): 원 ‘{r['stem']}’ → 변형 ‘{v['stem']}’")
        if added and not re.findall(r"\(([^)]*)\)", r["stem"]):
            flag("A1", "note", f"발문에 조건 추가: ({added[0]})")

        # 발문에 문법 단서 추가 (정답 노출·과제 단순화)
        terms = re.findall(HINT_TERMS, re.sub(r"\([^)]*\)", "", v["stem"]))
        new_terms = sorted({x for x in terms if x not in r["stem"]})
        if new_terms and (len(v["stem"]) > len(r["stem"]) + 15 or len(new_terms) >= 2):
            flag("C4", "주요", "발문에 원문항에 없던 문법 단서 추가: " + ", ".join(new_terms[:4]))
        paren = " ".join(re.findall(r"\(([^)]*)\)", v["stem"]))
        if paren and not re.findall(r"\(([^)]*)\)", r["stem"]):
            pt = sorted({x for x in re.findall(HINT_TERMS, paren) if x not in r["stem"]})
            if pt:
                flag("C4", "경미", "발문 괄호 조건에 문법 설명이 들어감: " + ", ".join(pt[:4]))

        # A2 선택지
        nv = sum(1 for c in v["choices"] if c)
        if nv != len(r["choices"]):
            flag("A2", "○", f"선택지 수 {len(r['choices'])} → {nv}")
        rf, vf = choice_form(r["choices"]), choice_form(v["choices"])
        if rf != vf:
            flag("A2", "◐", f"선택지 형태 변경: {rf} → {vf}")

        # A3 제시 방식
        rtext = r["stem"] + r["passage"] + " ".join(r["choices"])
        vtext = v["stem"] + v["passage"] + " ".join(v["choices"])
        r_u, v_u = "<u>" in rtext, "<u>" in vtext
        if "밑줄" in v["stem"] and not v_u:
            flag("C3", "치명", "발문은 ‘밑줄 친 부분’을 묻는데 문항에 밑줄 표시가 없음")
        elif r_u and not v_u:
            flag("A3", "◐", "원문항의 밑줄 제시가 변형에서 사라짐")
        if v_u and vtext.count("<u>") != vtext.count("</u>"):
            flag("C2", "주요", "밑줄 태그 <u> 짝이 맞지 않음")
        if bool(r["passage"]) != bool(v["passage"]):
            flag("A3", "◐", "제시문(본문) " + ("있음 → 없음" if r["passage"] else "없음 → 있음"))
        if "빈칸" in v["stem"] and not re.search(r"_{2,}|\(\s*[A-E]?\s*\)_*|\[\s*\]", v["passage"] + " ".join(v["choices"])):
            flag("C3", "치명", "발문은 빈칸을 묻는데 빈칸 표시가 없음")
        for lab in re.findall(r"\(([A-C])\)", v["stem"]):
            if not re.search(rf"\(\s*{lab}\s*\)", v["passage"] + " ".join(v["choices"])):
                flag("C3", "치명", f"발문의 ({lab})가 본문·선택지에 없음")
                break
        rl, vl = label_style(r["passage"]), label_style(v["passage"])
        if r["passage"] and v["passage"]:
            rc, vc = labeled_count(r["passage"]), labeled_count(v["passage"])
            if rl and vl and rl != vl:
                sev = "주요" if vl == "a" else "경미"
                flag("C3", sev, f"보기 문장 기호 변경: {rl} → {vl}" + (" (기호·줄바꿈 없이 한 줄로 이어짐)" if vl == "a" else ""))
            if rc and vc and rc != vc:
                flag("A3", "◐", f"보기 문장 수 {rc}개 → {vc}개")
            if "\n" in r["passage"] and "\n" not in v["passage"] and len(v["passage"]) > 60:
                if vl != "a":
                    flag("C3", "경미", "본문 줄바꿈이 사라져 한 줄로 이어짐")
        if rl and v["passage"] and not vl:
            flag("C3", "주요", f"원문항의 보기 기호({rl})가 변형 본문에서 사라짐")
        ch_all = " ".join(v["choices"])
        if re.search(r"[ⓐ-ⓖ]", ch_all) and vl and vl != "ⓐ":
            flag("C3", "주요", f"선택지는 ⓐ 기호를 쓰는데 본문은 {vl} 기호")

        # C1 정답
        if v["answer"] is None or not (1 <= v["answer"] <= 5) or not v["choices"][v["answer"] - 1]:
            flag("C1", "치명", f"정답 표기 이상: ‘{v['answer_raw']}’")
        marks = expl_marks(v["expl"])
        trues = [k for k, x in marks.items() if x]
        if len(trues) > 1:
            flag("C1", "치명", f"해설에 [정답] 표시가 여러 개: {', '.join(CIRC[k-1] for k in trues)}")
        elif len(trues) == 1 and v["answer"] and trues[0] != v["answer"]:
            flag("C1", "치명", f"정답 칸 {CIRC[v['answer']-1]} ↔ 해설의 정답 {CIRC[trues[0]-1]} 불일치")
        if vf == "개수" and v["answer"]:
            m = re.match(r"(\d+)", norm(v["choices"][v["answer"] - 1]))
            said = re.search(r"정답 판단[^\n]*?(\d+)\s*개", v["expl"])
            if m and said and int(said.group(1)) != int(m.group(1)):
                flag("C1", "치명", f"개수 불일치: 해설은 {said.group(1)}개라는데 정답 선택지는 {m.group(1)}개")
            nums = [int(re.match(r"(\d+)", norm(c)).group(1)) for c in v["choices"] if re.match(r"\d+", norm(c))]
            if nums and nums != sorted(nums):
                flag("C4", "주요", "개수 선택지가 1개→5개 순서가 아님: " + ", ".join(f"{x}개" for x in nums))

        # C2 표기
        cn = [norm(c) for c in v["choices"] if c]
        dup = [c for c, k in Counter(cn).items() if k > 1]
        if dup:
            flag("C1", "치명", f"같은 선택지가 두 번 나옴: {dup[0]}")
        for i, c in enumerate(v["choices"], 1):
            if re.search(r"  +", c) or c != c.strip():
                flag("C2", "경미", f"{CIRC[i-1]} 공백 이상")
                break
        if vf == "문장":
            ends = [bool(re.search(r"[.?!]\s*(</u>)?\s*$", c)) for c in v["choices"] if c]
            if any(ends) and not all(ends):
                flag("C2", "경미", "선택지 문장 끝 마침표 유무가 섞여 있음")
        if re.search(r"[가-힣]", " ".join(v["choices"])) and not re.search(r"[가-힣]", " ".join(r["choices"])) and vf == "문장":
            flag("A2", "note", "원문항과 달리 선택지에 한글이 섞임")

        # 원문항·다른 유형과 중복
        rn = {norm(c) for c in r["choices"]}
        def is_sent(c):
            c = re.sub(r"<[^>]+>", "", c)
            if re.fullmatch(r"(\s*\(?[가-하A-Ga-gⓐ-ⓖㄱ-ㅎ]\)?\s*[,/-]?)+", c) or re.fullmatch(r"[\sA-Ga-gⓐ-ⓖ(),]+", c) or (len(re.findall(r"\([A-E]\)", c)) >= 2 and len(re.sub(r"\([A-E]\)", "", c).split()) <= 8):  # 기호 조합·(A)(B) 짝은 문장이 아님
                return False
            return not re.search(r"\s[-–—/]\s", c) and len(re.findall(r"[A-Za-z'가-힣]+", c)) >= 3
        same_choices = [i for i, c in enumerate(v["choices"], 1) if is_sent(c) and norm(c) in rn]
        # 조합형 선택지(a - an - a 등)는 문항끼리 겹치는 게 당연하므로 비교에서 뺀다
        has_sent = any(is_sent(c) for c in v["choices"])

        def content(it):
            chs = [c for c in it["choices"] if is_sent(c)] if has_sent else it["choices"]
            return norm(it["passage"] + " " + " ".join(chs))

        whole_r, whole_v = content(r), content(v)
        sim_cut = 0.85 if has_sent else 0.95
        sim = difflib.SequenceMatcher(None, whole_r, whole_v).ratio()
        if sim >= sim_cut and whole_v:
            flag("C4", "주요", f"원문항과 거의 같음 (유사도 {sim:.0%})")
        elif len(same_choices) >= 3:
            flag("C4", "주요", f"원문항 선택지를 {len(same_choices)}개 그대로 사용")
        if v["answer"] and r["answer"] and 1 <= v["answer"] <= 5:
            va, ra = v["choices"][v["answer"] - 1], r["choices"][r["answer"] - 1]
            if (is_sent(va) or (vf == "짝" and len(va.split(" - ")) == 2)) and norm(va) == norm(ra):
                flag("C4", "주요", "정답 선택지가 원문항 정답과 같은 문장 (원문항을 본 학생에게 정답 노출)")
        rp = norm(r["passage"])
        if rp and len(rp) > 80 and norm(v["passage"]) == rp:
            flag("C4", "주요", "본문이 원문항과 똑같음")
        for other in by_ref[(g, n)]:
            if other["type"] >= t:
                continue
            wo = content(other)
            s2 = difflib.SequenceMatcher(None, wo, whole_v).ratio()
            if s2 >= sim_cut and whole_v:
                flag("C4", "주요", f"{other['type']}유형 변형과 거의 같음 (유사도 {s2:.0%})")

        # 존재하지 않는 형태의 오답: 다른 선택지(…s)에 -ing/-ly/-ed를 덧붙인 형태
        words = {norm(c) for c in v["choices"] if c}
        fake = sorted({c for c in words for x in words
                       if x.endswith("s") and not x.endswith("ss") and len(x) > 2 and c != x
                       and re.search(rf"\b{re.escape(x)}(ing|ly|ed|es)\b", c)})
        if len(fake) >= 2:
            flag("B3", "주요", f"존재하지 않는 형태의 오답 {len(fake)}개: " + ", ".join(fake[:4]))
        elif fake:
            flag("B3", "경미", "존재하지 않는 형태의 오답: " + fake[0])
        # 짝 선택지에서 같은 기본형이 두 번 나옴 → 정답 단서
        single_parts = all(" " not in part.strip() for c in v["choices"] if c for part in re.split(r"\s[-–—/]\s", norm(c)))
        if vf == "짝" and single_parts:
            lefts = [re.split(r"\s[-–—/]\s", norm(c))[0] for c in v["choices"] if c]
            rep_left = [x for x, k in Counter(lefts).items() if k > 1]
            rights = [re.split(r"\s[-–—/]\s", norm(c))[-1] for c in v["choices"] if c]
            derived = sum(1 for a, b in zip(lefts, rights) if a[:3] == b[:3])  # baby - babies 같은 기본형-변화형 짝
            if rep_left and len(lefts) >= 5 and len(set(lefts)) == len(lefts) - 1 and derived >= 3:
                flag("C4", "주요", f"같은 기본형 ‘{rep_left[0]}’이 선택지에 두 번 나와 정답 단서가 됨")
        # 다른 유형과 선택지 문장 공유
        mine = {norm(c) for c in v["choices"] if is_sent(c)}
        for other in by_ref[(g, n)]:
            if other["type"] >= t:  # 앞선 유형과 겹칠 때만 뒤 유형에 표시
                continue
            shared = mine & {norm(c) for c in other["choices"] if is_sent(c)}
            if len(shared) >= 3:
                flag("C4", "주요", f"{other['type']}유형과 선택지 {len(shared)}개가 같은 문장")
                break

        # 해설이 관례를 전제하는 경우 (논란 소지)
        hedge = re.search(r"이 문항(에서는|은|의)[^\n]{0,60}(기준|요구|전제|간주|따라|본다)", v["expl"])
        if hedge:
            flag("C2", "확인", "해설이 ‘" + hedge.group(0)[:70] + "…’처럼 특정 관례를 전제함 → 다른 답이 가능한지 확인 필요")

        out.append({
            "id": f"{g}급-{n:03d}-{t}", "type": t, "grade": g, "no": n,
            "chapter": v["chapter"], "chapter_name": v["chapter_name"],
            "ref_stem": r["stem"], "ref_answer": r["answer"],
            "stem": v["stem"], "answer": v["answer"], "sim": round(sim, 2),
            "flags": flags,
        })
    return out


def main():
    ref, var = load()
    res = screen(ref, var)
    json.dump(res, open(SRC / "screen.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    c = Counter()
    for r in res:
        for f in r["flags"]:
            c[(f["code"], f["sev"], re.sub(r"[:(（].*", "", f["msg"])[:40])] += 1
    for k, n in sorted(c.items(), key=lambda x: -x[1]):
        print(n, *k)
    pos = defaultdict(Counter)
    for r in res:
        pos[r["type"]][r["answer"]] += 1
    for t in TYPES:
        print(t, "정답 위치", dict(sorted(pos[t].items())))


if __name__ == "__main__":
    main()
