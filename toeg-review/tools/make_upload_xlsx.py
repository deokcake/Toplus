#!/usr/bin/env python3
"""시험 사이트 문제등록 양식(17열) 엑셀 만들기 — 기준 문항(A)과 B 유형 확정본.
사용: python3 tools/make_upload_xlsx.py  → 결과/업로드/TOEG_기준문항(A)_문제등록.xlsx, TOEG_B유형_문제등록.xlsx
양식: 'B type 감수용.xlsx'(문제등록 시트)와 같은 열·서식. 정답은 숫자 문자열, 밑줄은 <u>…</u> 그대로."""
import sys
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
sys.path.insert(0, str(Path(__file__).resolve().parent))
import final_items as FI

OUT = FI.HERE / "결과/업로드"; OUT.mkdir(parents=True, exist_ok=True)
HEADER = ["양식명", "급수", "챕터", "챕터명", "문제 분류", "문제 유형(객관식:1/주관식:2)", "난이도", "문제번호", "문제명", "본문",
          "보기 문항1", "보기 문항2", "보기 문항3", "보기 문항4", "보기 문항5", "정답", "설명"]
WIDTHS = {"A": 10, "B": 8, "C": 10, "D": 27, "E": 12, "F": 19, "G": 10, "H": 11, "I": 40, "J": 40, "K": 36, "L": 36, "M": 36, "N": 36, "O": 36, "P": 8, "Q": 120}
FONT = "Malgun Gothic"
thin = Side(style="thin", color="BFBFBF"); BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)

def write(path, cls, items):
    wb = Workbook(); ws = wb.active; ws.title = "문제등록"
    ws.append(HEADER)
    for g, n in FI.order():
        it = items[f"{g}-{n}"]; ch, chn = FI.CHAP[f"{g}-{n}"]
        c = (list(it["c"]) + [""] * 5)[:5]
        ws.append(["TOEG", f"{g}급", ch, chn, cls, "1", None, str(n), it["stem"], it["passage"] or None] + c + [str(it["ans"]), it["expl"]])
    for col, w in WIDTHS.items(): ws.column_dimensions[col].width = w
    ws.row_dimensions[1].height = 44
    for cell in ws[1]:
        cell.font = Font(name=FONT, size=10, bold=True, color="FFFFFF"); cell.fill = PatternFill("solid", fgColor="26384A")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True); cell.border = BORDER
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.font = Font(name=FONT, size=10); cell.alignment = Alignment(vertical="center", wrap_text=True); cell.border = BORDER
    ws.freeze_panes = "A2"
    wb.save(path); return ws.max_row - 1

if __name__ == "__main__":
    n1 = write(OUT / "TOEG_기준문항(A)_문제등록.xlsx", "A", FI.load_ref())
    B, src = FI.load_B()
    n2 = write(OUT / "TOEG_B유형_문제등록.xlsx", "B", B)
    import collections
    print(f"기준 문항 {n1}행, B 유형 {n2}행 →", OUT, dict(collections.Counter(src.values())))
