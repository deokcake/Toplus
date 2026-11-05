#!/usr/bin/env python3
"""문제은행 양식(toeg_문제은행_형식.xlsx, Numbers 내보내기)에 확정본을 채운다.
사용: python3 tools/make_bank_xlsx.py [출력 경로]
- 양식: src/template/toeg_문제은행_형식.xlsx (시트·열·서식 그대로, 예시 행만 지우고 채움)
- 모의고사 시트: 기준 문항(A)·B·C. 열 level(급) · chapter(챕터 번호) · unit(챕터 안 문항 순서) · unit_type(A=기준 문항, B, C) · question · passage · option_1~5 · answer
  순서 급 → 챕터 → A·B·C → unit (양식 예시와 같은 순서), 행 색은 양식처럼 유형별(A 초록·B 노랑·C 분홍).
- 본고사 시트: D·E·F. unit_type 열이 없고, 양식 안내(“한 유닛에 여러 문제를 넣을 때는 레벨·챕터·유닛을 똑같이”)대로
  같은 원문항의 D·E·F를 같은 level·chapter·unit으로 세 행씩 넣는다. 순서 급 → 챕터 → unit → D·E·F.
  행 서식은 칠 없는 예시 행(6행)을 따른다(3~5행의 노란 칠과 L3 안내 글은 예시 설명이라 지운다).
- 줄바꿈은 양식 예시처럼 ‘↵’로 쓴다. 밑줄 <u>…</u>와 표의 탭은 그대로 둔다.
- B~F: page/data/{유형}.json(원안)에 검토 페이지 DB의 확정(edit)을 덮어쓴 것(페이지 effItem과 같은 규칙). DB 스냅샷 src/db_t{유형}_20261028."""
import sys, json, math, re
from copy import copy
from pathlib import Path
from openpyxl import load_workbook
sys.path.insert(0, str(Path(__file__).resolve().parent))
import final_items as FI

HERE = FI.HERE
TEMPLATE = HERE / "src/template/toeg_문제은행_형식.xlsx"
SNAP = {t: HERE / f"src/db_t{t}_20261028" for t in "BCDEF"}
MOCK, MAIN = "모의고사 - 모의고사", "본고사 - 본고사"
NL = "↵"

def load_type(t):
    rows = json.load(open(HERE / f"page/data/{t}.json", encoding="utf-8"))
    out = {}
    for r in rows:
        k = f"{r['g']}-{r['n']}"
        f = SNAP[t] / f"{k}.json"
        e = json.load(open(f, encoding="utf-8")).get("edit") if f.exists() else None
        out[k] = FI.merged_edit(r, e)
    return out

def cell_text(s):
    s = (s or "").replace("\r\n", "\n").replace("\r", "\n").strip("\n")
    return s.replace("\n", NL) if s else None

def chapters():
    """[(급, 챕터 번호, [번호…])]"""
    out = []
    for g, chs in FI.idx["grades"].items():
        for c in chs:
            out.append((int(g), int(re.sub(r"\D", "", c["ch"])), c["nos"]))
    return out

def est_lines(text, width):
    if not text: return 1
    w = sum(2 if ord(ch) > 0x2E80 else 1 for ch in text)
    per = max(8, int(width * 1.15))
    return sum(max(1, math.ceil(sum(2 if ord(ch) > 0x2E80 else 1 for ch in part) / per)) for part in text.split(NL)) if NL in text else max(1, math.ceil(w / per))

def clear_rows(ws, first):
    for rng in list(ws.merged_cells.ranges):
        if rng.min_row >= first: ws.unmerge_cells(str(rng))
    if ws.max_row >= first: ws.delete_rows(first, ws.max_row - first + 1)

def grab(ws, r, ncol):
    return [{"font": copy(c.font), "fill": copy(c.fill), "border": copy(c.border), "alignment": copy(c.alignment),
             "number_format": c.number_format, "protection": copy(c.protection)} for c in (ws.cell(r, j) for j in range(1, ncol + 1))]

def col_widths(ws, ncol):
    """열 너비. 양식에는 F:J처럼 묶어 정의한 열이 있어 글자(‘G’)로 찾으면 openpyxl이 새 열 정의를 만들어 겹친다(엑셀 복구 경고) → 묶음 범위에서 찾는다."""
    w = {}
    for d in ws.column_dimensions.values():
        for i in range(d.min or 1, (d.max or d.min or 1) + 1): w.setdefault(i, d.width)
    return [w.get(j) or 13 for j in range(1, ncol + 1)]

def item_vals(it):
    """question · passage · option_1~5 · answer"""
    c = (list(it["c"]) + [""] * 5)[:5]
    return [cell_text(it["stem"]), cell_text(it["passage"])] + [cell_text(x) for x in c] + [int(it["ans"])]

def put_row(ws, r, vals, style, passage_col, passage_fmt, widths):
    for j, v in enumerate(vals, 1):
        cell = ws.cell(r, j, v); s = style[j - 1]
        cell.font = copy(s["font"]); cell.fill = copy(s["fill"]); cell.border = copy(s["border"])
        cell.alignment = copy(s["alignment"]); cell.protection = copy(s["protection"])
        cell.number_format = passage_fmt if (j == passage_col and v) else s["number_format"]
    lines = max(est_lines(v if isinstance(v, str) else "", widths[j - 1]) for j, v in enumerate(vals, 1))
    ws.row_dimensions[r].height = max(20.25, round(lines * 13.2 + 6, 2))

def build(out_path):
    wb = load_workbook(TEMPLATE)
    items = {"A": FI.load_ref(), **{t: load_type(t) for t in "BCDEF"}}
    counts = {t: 0 for t in "ABCDEF"}

    # ---- 모의고사: A·B·C ----
    ws = wb[MOCK]
    head = [c.value for c in ws[2]]
    assert head[:12] == ["level", "chapter", "unit", "unit_type", "question", "passage", "option_1", "option_2", "option_3", "option_4", "option_5", "answer"], head
    # 양식 예시: 3행(A, 머리글 바로 아래라 위 테두리가 진함), 4~7행 A, 8~12행 B, 13~17행 C — 유형마다 채우기 색이 다르다
    first, tstyle = grab(ws, 3, 12), {"A": grab(ws, 4, 12), "B": grab(ws, 9, 12), "C": grab(ws, 14, 12)}
    passage_fmt = ws.cell(7, 6).number_format  # 본문이 있는 예시 칸(F7)의 서식
    widths = col_widths(ws, 12)
    clear_rows(ws, 3)
    r = 3
    for g, ch, nos in chapters():
        for t in "ABC":
            for unit, n in enumerate(nos, 1):
                put_row(ws, r, [g, ch, unit, t] + item_vals(items[t][f"{g}-{n}"]), first if r == 3 else tstyle[t], 6, passage_fmt, widths)
                counts[t] += 1; r += 1
    n_mock = r - 3

    # ---- 본고사: D·E·F (같은 원문항의 세 유형을 같은 unit으로) ----
    wm = wb[MAIN]
    head = [c.value for c in wm[2]]
    assert head[:11] == ["level", "chapter", "unit", "question", "passage", "option_1", "option_2", "option_3", "option_4", "option_5", "answer"], head
    mstyle = grab(wm, 6, 12)                      # 칠 없는 예시 행(L열은 값 없이 테두리만)
    m_passage_fmt = wm.cell(9, 5).number_format   # 본문이 있는 예시 칸(E9)의 서식
    mwidths = col_widths(wm, 12)
    clear_rows(wm, 3)
    r = 3
    for g, ch, nos in chapters():
        for unit, n in enumerate(nos, 1):
            for t in "DEF":
                put_row(wm, r, [g, ch, unit] + item_vals(items[t][f"{g}-{n}"]) + [None], mstyle, 5, m_passage_fmt, mwidths)
                counts[t] += 1; r += 1
    n_main = r - 3

    for sh in (ws, wm):
        for rr in [k for k in sh.row_dimensions if k > sh.max_row]: del sh.row_dimensions[rr]
    wb.active = wb.sheetnames.index(MOCK)
    wb.save(out_path)
    return counts, n_mock, n_main

if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "결과/업로드/TOEG_문제은행_A~F_확정본.xlsx"
    out.parent.mkdir(parents=True, exist_ok=True)
    counts, n_mock, n_main = build(out)
    print(out, "모의고사", n_mock, "행 / 본고사", n_main, "행", counts)
