#!/usr/bin/env python3
"""해설 감수 결과 → 엑셀 (결과/해설감수/해설감수_결과.xlsx).
원본: src/expl_review/runs/merged_done.json(5번호 묶음, 재검증까지), review_only.json(1차 검토만),
      src/expl_review/runs/by_number_first.json(대본 워크플로 1차 검토만), by_number.json(번호마다 검토 + 재검증), src/expl_review/overrides.json(사용자 요청 수정). 뒤에 오는 것이 앞의 것을 덮는다."""
import json, re
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
HERE = Path(__file__).resolve().parents[1]
R = HERE / "src/expl_review/runs"

def collect():
    rows = {}
    if (R / "review_only.json").exists():
        for b, r in json.load(open(R / "review_only.json", encoding="utf-8")).items():
            for x in r["results"]: rows[(x["key"], x["type"])] = {**x, "first": x["verdict"], "note": "", "stage": "1차 검토만(재검증 전)"}
    if (R / "by_number_first.json").exists():
        for k, xs in json.load(open(R / "by_number_first.json", encoding="utf-8")).items():
            for x in xs: rows[(k, x["type"])] = {**x, "key": k, "stage": "1차 검토만(재검증 전)"}
    if (R / "merged_done.json").exists():
        for b, xs in json.load(open(R / "merged_done.json", encoding="utf-8")).items():
            for x in xs: rows[(x["key"], x["type"])] = {**x, "stage": "검토 + 재검증"}
    if (R / "by_number.json").exists():
        for k, xs in json.load(open(R / "by_number.json", encoding="utf-8")).items():
            for x in xs: rows[(k, x["type"])] = {**x, "key": k, "stage": "검토 + 재검증"}
    OV = HERE / "src/expl_review/overrides.json"
    for kt, x in (json.load(open(OV, encoding="utf-8")) if OV.exists() else {}).items():
        k, T = kt.split("|"); rows[(k, T)] = {**x, "key": k, "type": T, "first": x["verdict"], "stage": "사용자 요청으로 문항 수정"}
    return rows

def main():
    rows = collect()
    cur = {}
    for f in (HERE / "work/video/in").glob("*.json"):
        u = json.load(open(f, encoding="utf-8")); cur.update({(u["key"], T): it["expl"] for T, it in u["items"].items()})
    order = lambda k: (int(k[0].split("-")[0]), int(k[0].split("-")[1]), k[1])
    wb = Workbook(); ws = wb.active; ws.title = "해설 감수"
    H = ["급", "번호", "유형", "최종 판정", "단계", "지적 (종류 · 위치 · 내용)", "현재 해설", "수정안", "검증 메모"]
    ws.append(H)
    fills = {"수정 필요": "F8D7DA", "보완 권장": "FFF3CD", "이상 없음": "D1E7DD"}
    thin = Side(style="thin", color="BBBBBB")
    for key in sorted(rows, key=order):
        x = rows[key]; g, n = key[0].split("-")
        iss = "\n".join(f"[{i['kind']}] {i['where']} · {i['detail']}" for i in x.get("issues") or [])
        ws.append([int(g), int(n), "원문항(A)" if key[1] == "A" else key[1], x["verdict"], x["stage"], iss, cur.get(key, ""), x.get("proposed") or "", x.get("note") or ""])
        ws.cell(ws.max_row, 4).fill = PatternFill("solid", fgColor=fills.get(x["verdict"], "FFFFFF"))
    widths = [5, 6, 9, 10, 14, 60, 70, 70, 40]
    for i, w in enumerate(widths): ws.column_dimensions[chr(65 + i)].width = w
    for row in ws.iter_rows():
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top"); c.border = Border(top=thin, bottom=thin, left=thin, right=thin)
    for c in ws[1]: c.font = Font(bold=True); c.fill = PatternFill("solid", fgColor="DDE3EC")
    ws.freeze_panes = "D2"; ws.auto_filter.ref = ws.dimensions
    # 요약 시트
    s = wb.create_sheet("요약", 0)
    from collections import Counter
    s.append(["해설 감수 결과", ""]); s["A1"].font = Font(bold=True, size=13)
    s.append(["감수한 해설", len(rows)]); s.append(["전체 해설", 4920])
    c = Counter(x["verdict"] for x in rows.values())
    for v in ("수정 필요", "보완 권장", "이상 없음"): s.append([v, c.get(v, 0)])
    st = Counter(x["stage"] for x in rows.values())
    for v, n in st.items(): s.append([v, n])
    kinds = Counter(i["kind"] for x in rows.values() for i in x.get("issues") or [])
    s.append([]); s.append(["지적 종류", "건수"])
    for k, n in kinds.most_common(): s.append([k, n])
    s.column_dimensions["A"].width = 26; s.column_dimensions["B"].width = 12
    out = HERE / "결과/해설감수"; out.mkdir(parents=True, exist_ok=True)
    wb.save(out / "해설감수_결과.xlsx"); print(len(rows), "rows →", out / "해설감수_결과.xlsx", dict(c), dict(st))

if __name__ == "__main__": main()
