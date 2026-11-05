#!/usr/bin/env python3
"""수동 감수(rv/*.py)와 자동 점검(src/screen.json)을 합쳐 최종 판정을 만든다.

    python3 assemble.py            # 통계와 점검 목록 출력, final.json 저장
"""
import difflib, json, re, runpy, sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
OK, FXP, FXC, BAD = "적합", "수정(표기)", "수정(내용)", "부적합"
RANK = {OK: 0, FXP: 1, FXC: 2, BAD: 3}
ALIAS = {"수정 후 사용": FXC}


def load_manual():
    review, ref_notes, src = {}, {}, {}
    for p in sorted((HERE / "rv").glob("*.py")):
        d = runpy.run_path(str(p))
        for k, v in d.get("REVIEW", {}).items():
            if k in review:
                raise SystemExit(f"중복 판정: {k} ({p.name}, {src[k]})")
            review[k], src[k] = v, p.name
        ref_notes.update(d.get("REF_NOTES", {}))
    return review, ref_notes, src


def manual_for(review, g, n, t):
    item = review.get((g, n))
    if item is None:
        return None
    v = item.get(t) or item.get("*")
    if v is None:
        return None
    verdict, reason, fix = v
    forced = verdict.endswith("!")
    verdict = ALIAS.get(verdict.rstrip("!"), verdict.rstrip("!"))
    return verdict, reason, fix, forced


def norm_stem(s):
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"(고르세요|고르시오|고르십시오)[.?]?$", "고르시오", s)
    s = s.replace("가장 ", "").replace("다음 중 ", "다음 ").rstrip(".? ")
    return s


# 자동 점검 → 최소 판정
FORMAT_RULES = [  # (code, 메시지 패턴) → 수정(표기)
    ("A2", "선택지 형태 변경"),
    ("A3", "밑줄 제시가"),
    ("A3", "보기 문장 수"),
    ("A3", "제시문"),
    ("C3", "기호"),
    ("C3", "줄바꿈"),
    ("C4", "개수 선택지가"),
    ("A1", "발문 과제 변경 의심"),
    ("A1", "발문에 조건 추가"),
]
CONTENT_RULES = [  # 객관적으로 확인되는 원문항·유형 간 노출 → 수정(내용)
    ("C4", "유형과 선택지"),
    ("C4", "정답 선택지가 원문항 정답과 같은"),
    ("C4", "원문항 선택지를"),
    ("C4", "변형과 거의 같음"),
    ("C4", "원문항과 거의 같음"),
    ("C4", "본문이 원문항과 똑같음"),
    ("C4", "같은 기본형"),
    ("B3", "존재하지 않는 형태의 오답"),
]


def auto_level(r):
    lvl, why = OK, []
    for f in r["flags"]:
        code, msg, sev = f["code"], f["msg"], f["sev"]
        if code == "B3" and sev != "주요":
            continue
        for c, pat in CONTENT_RULES:
            if code == c and pat in msg:
                lvl = FXC if RANK[FXC] > RANK[lvl] else lvl
                why.append(("내용", code, msg))
                break
        else:
            for c, pat in FORMAT_RULES:
                if code == c and pat in msg:
                    if RANK[FXP] > RANK[lvl]:
                        lvl = FXP
                    why.append(("표기", code, msg))
                    break
            else:
                if code == "A1" and "발문 문구 변경" in msg:
                    a, b = norm_stem(r["ref_stem"]), norm_stem(r["stem"])
                    if difflib.SequenceMatcher(None, a, b).ratio() < 0.85:
                        if RANK[FXP] > RANK[lvl]:
                            lvl = FXP
                        why.append(("표기", code, msg))
    return lvl, why


def build():
    review, ref_notes, src = load_manual()
    screen = json.load(open(HERE / "src" / "screen.json", encoding="utf-8"))
    out, missing = [], []
    for r in screen:
        g, n, t = r["grade"], r["no"], r["type"]
        m = manual_for(review, g, n, t)
        if m is None:
            missing.append((g, n, t))
            continue
        mv, reason, fix, forced = m
        av, why = auto_level(r)
        final = mv if forced or RANK[mv] >= RANK[av] else av
        out.append({"id": r["id"], "type": t, "grade": g, "no": n, "manual": mv, "forced": forced,
                    "auto": av, "final": final, "reason": reason, "fix": fix,
                    "auto_why": why, "ref_note": ref_notes.get((g, n), ""), "src": src[(g, n)]})
    return out, missing, ref_notes


if __name__ == "__main__":
    out, missing, ref_notes = build()
    print("누락:", len(missing), missing[:10])
    print("수동:", Counter(o["manual"] for o in out))
    print("최종:", Counter(o["final"] for o in out))
    up = Counter((o["manual"], o["final"]) for o in out if o["manual"] != o["final"])
    print("자동으로 올라간 것:", up)
    json.dump(out, open(HERE / "final.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
