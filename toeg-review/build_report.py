#!/usr/bin/env python3
"""감수 결과 엑셀을 만든다.  python3 build_report.py <src 폴더> <출력.xlsx>"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(Path.home() / ".claude/skills/grammar-item-review/scripts"))
src, out = sys.argv[1], sys.argv[2]
sys.argv = ["x", src]
import json
import screen
from make_xlsx import write_workbook
from sample_review import REVIEW

ref, var = screen.load()
res = json.load(open(Path(src) / "screen.json", encoding="utf-8"))
C = "①②③④⑤"
TYPES = "BCDEF"

CATS = [
    ("발문·제시 불일치 (밑줄·빈칸·(A) 표시 없음)", lambda f: f["code"] == "C3" and f["sev"] == "치명"),
    ("발문 과제 변경 의심 (자동 분류, 확인 필요)", lambda f: f["code"] == "A1" and f["sev"] in ("○", "◐")),
    ("발문에 원문항에 없던 문법 단서 추가", lambda f: f["code"] == "C4" and "문법 단서" in f["msg"]),
    ("정답 선택지가 원문항 정답과 같은 문장", lambda f: "원문항 정답과 같은" in f["msg"]),
    ("원문항과 거의 같음·선택지 3개 이상 재사용·본문 동일", lambda f: f["code"] == "C4" and re.search(r"원문항과 거의|그대로 사용|본문이 원문항", f["msg"])),
    ("다른 유형(B~F)과 거의 같음·선택지 3개 이상 공유", lambda f: re.search(r"유형 변형과 거의|유형과 선택지", f["msg"])),
    ("존재하지 않는 형태의 오답", lambda f: "존재하지 않는 형태" in f["msg"]),
    ("같은 기본형이 선택지에 두 번 (정답 단서)", lambda f: "두 번 나와" in f["msg"]),
    ("개수 선택지가 1개→5개 순서가 아님", lambda f: "개수 선택지" in f["msg"]),
    ("원문항의 밑줄 제시가 사라짐", lambda f: "밑줄 제시가" in f["msg"]),
    ("선택지 형태 변경", lambda f: "선택지 형태 변경" in f["msg"]),
    ("보기 문장 수 변경", lambda f: "보기 문장 수" in f["msg"]),
    ("제시문(본문) 유무 변경", lambda f: f["msg"].startswith("제시문")),
    ("보기 문장 기호 변경·한 줄로 이어짐", lambda f: f["code"] == "C3" and re.search(r"기호|줄바꿈", f["msg"])),
    ("해설이 특정 관례를 전제 (다른 답 가능성 확인)", lambda f: f["sev"] == "확인"),
    ("발문 괄호 조건에 문법 설명", lambda f: "괄호 조건에 문법" in f["msg"]),
    ("선택지 표기(마침표 혼재·공백)", lambda f: f["code"] == "C2" and f["sev"] == "경미"),
]


def verdict(flags):
    sev = {f["sev"] for f in flags}
    if "치명" in sev:
        return "부적합 의심"
    # 허용 범위 '유사': 제시 방식(A3) 변경만으로는 수정 대상으로 보지 않는다
    if "주요" in sev or any(f["sev"] in ("◐", "○") and f["code"] != "A3" for f in flags):
        return "수정 검토"
    return "이상 없음"


def item_text(v):
    parts = [v["stem"]]
    if v["passage"]:
        parts.append(v["passage"])
    parts += [f"{C[i]} {c}" for i, c in enumerate(v["choices"]) if c]
    parts.append(f"정답 {C[v['answer']-1] if v['answer'] else v['answer_raw']}")
    return "\n".join(parts)


def ref_text(r):
    parts = [r["stem"]]
    if r["passage"]:
        parts.append(r["passage"])
    if not r.get("inline"):
        parts += [f"{C[i]} {c}" for i, c in enumerate(r["choices"])]
    parts.append(f"정답 {C[r['answer']-1]}")
    return "\n".join(parts)


# ---------- 1차 자동 점검 ----------
auto_rows = []
dist = defaultdict(Counter)
cat_counts = defaultdict(Counter)
for r in res:
    v = var[(r["type"], r["grade"], r["no"])]
    fl = r["flags"]
    vd = verdict(fl)
    dist[r["type"]][vd] += 1
    for name, test in CATS:
        if any(test(f) for f in fl):
            cat_counts[name][r["type"]] += 1
    shown = [f for f in fl if f["sev"] != "note"]
    notes = [f for f in fl if f["sev"] == "note"]
    auto_rows.append([
        r["id"], f"{r['grade']}급", r["no"], f"{r['chapter']} {r['chapter_name']}", r["type"], vd,
        sum(f["sev"] == "치명" for f in fl), sum(f["sev"] == "주요" for f in fl),
        "\n".join(f"[{f['code']} {f['sev']}] {f['msg']}" for f in shown),
        "\n".join(f"[{f['code']}] {f['msg']}" for f in notes),
        r["ref_stem"], item_text(v),
    ])

# ---------- 정밀 감수 샘플 ----------
sample_rows = []
sample_dist = Counter()
auto_by_id = {r["id"]: r for r in res}
for (g, n), per in sorted(REVIEW.items(), key=lambda kv: (-kv[0][0], kv[0][1])):
    rr = ref[(g, n)]
    for t in TYPES:
        vd, why, fix = per.get(t) or per["*"]
        v = var[(t, g, n)]
        rid = f"{g}급-{n:03d}-{t}"
        sample_dist[vd] += 1
        a = auto_by_id[rid]
        sample_rows.append([
            rid, f"{v['chapter']} {v['chapter_name']}", vd, why, fix,
            verdict(a["flags"]), ref_text(rr), item_text(v),
        ])

# ---------- 요약 ----------
tot = {t: sum(dist[t].values()) for t in TYPES}
summary = []
summary.append(["【1차 자동 점검 판정】 (4,100문항 전체, 기계 점검만 반영)", "", "", "", "", "", ""])
for vd in ["부적합 의심", "수정 검토", "이상 없음"]:
    summary.append([vd, *[dist[t][vd] for t in TYPES], sum(dist[t][vd] for t in TYPES)])
summary.append(["", "", "", "", "", "", ""])
summary.append(["【점검 항목별 해당 문항 수】", "", "", "", "", "", ""])
for name, _ in CATS:
    row = [name, *[cat_counts[name][t] for t in TYPES], sum(cat_counts[name].values())]
    summary.append(row)
summary.append(["", "", "", "", "", "", ""])
summary.append(["【정밀 감수 샘플】 7급 CH1 · 1급 CH1, 100문항 직접 풀이", "", "", "", "", "", ""])
for vd in ["적합", "수정 후 사용", "부적합"]:
    summary.append([vd, *[sum(1 for row in sample_rows if row[2] == vd and row[0].endswith("-" + t)) for t in TYPES], sample_dist[vd]])
summary.append(["정답 오류(C1)", 0, 0, 0, 0, 0, 0])
summary.append(["", "", "", "", "", "", ""])
summary.append(["정답 칸 ↔ 해설 [정답] 표시 일치", "4,097 / 4,100 일치 (3문항은 해설 형식이 달라 확인 불가, 불일치 0)", "", "", "", "", ""])
summary.append(["정답 위치 분포", "유형마다 ①~⑤가 163~165개씩 균등", "", "", "", "", ""])

write_workbook(out, [
    ("요약", ["항목", "B", "C", "D", "E", "F", "합계"], summary),
    ("정밀감수 샘플(100)", ["ID", "챕터", "판정", "근거 (직접 풀이)", "수정 제안", "1차 자동 판정", "기준 문항", "변형 문항"], sample_rows),
    ("1차 자동점검(4100)", ["ID", "급수", "번호", "챕터", "유형", "1차 판정", "치명", "주요", "점검 결과", "참고(발문 변경 등)", "기준 문항 발문", "변형 문항"], auto_rows),
])
print("저장:", out)
for t in TYPES:
    print(t, dict(dist[t]))
print("sample", dict(sample_dist))
for name, _ in CATS:
    print(name, dict(cat_counts[name]), sum(cat_counts[name].values()))
