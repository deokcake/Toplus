#!/usr/bin/env python3
"""영상 대본 묶음 만들기: 결과/영상대본/<급>급/*.json →
- 결과/영상대본/<급>급_대본.md (급별 한 파일, 번호·유형 순)
- 결과/영상대본/영상대본_전체.xlsx (‘영상 목록’ 한 줄 = 한 편, ‘장면’ 한 줄 = 한 장면)
- 결과/영상대본/영상대본_<급>급.zip (급별 JSON·MD 낱개 파일)
사용: python3 tools/video/bundle_scripts.py"""
import json, re, zipfile
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
HERE = Path(__file__).resolve().parents[2]
OUT = HERE / "결과/영상대본"
C5 = "①②③④⑤"

def order(p):
    m = re.match(r"(\d+)-(\d+)-([A-F])", p.stem); return (int(m[1]), int(m[2]), m[3])

def main():
    docs = []
    for g in range(1, 8):
        d = OUT / f"{g}급"
        if not d.exists(): continue
        fs = sorted(d.glob("*-*-[A-F].json"), key=order)
        if not fs: continue
        md = [f"# TOEG {g}급 풀이 영상 대본 ({len(fs)}편)", ""]
        for f in fs:
            docs.append(json.load(open(f, encoding="utf-8")))
            md += [open(f.with_suffix(".md"), encoding="utf-8").read().rstrip(), "", "---", ""]
        open(OUT / f"{g}급_대본.md", "w", encoding="utf-8").write("\n".join(md))
        with zipfile.ZipFile(OUT / f"영상대본_{g}급.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for f in fs:
                z.write(f, f"{g}급/{f.name}"); z.write(f.with_suffix(".md"), f"{g}급/{f.with_suffix('.md').name}")
        print(f"{g}급 {len(fs)}편")
    wb = Workbook(); a = wb.active; a.title = "영상 목록"
    a.append(["급", "챕터", "번호", "유형", "제목", "총 길이(초)", "정답", "파일"])
    s = wb.create_sheet("장면")
    s.append(["급", "번호", "유형", "장면", "이름", "길이(초)", "화면 글", "판서 순서", "풀이 단계(강조·지움)", "보기 표시", "내레이션", "자막"])
    for d in docs:
        g = d["grade"]; n = int(d["key"].split("-")[1]); T = d["type"]
        a.append([g, d["chapter"], n, T, d["title"], d["total_sec"], C5[d["source"]["ans"] - 1], f"{g}급/{d['key']}-{T}.json"])
        for sc in d["scenes"]:
            scr = sc["screen"]
            steps = "\n".join(f"{st['step']}단계: {st['note']}" + (f" | 강조 {', '.join(st['highlight'])}" if st["highlight"] else "") + (f" | 지움 {', '.join(st['strike'])}" if st["strike"] else "") for st in scr.get("steps") or [])
            marks = " ".join(f"{k}{v}" for k, v in (scr.get("marks") or {}).items())
            s.append([g, n, T, sc["no"], sc["name"], sc["sec"], scr["text"], "\n".join(scr.get("reveal") or []), steps, marks, sc["narration"], sc["caption"]])
    for ws, widths in ((a, [5, 22, 6, 5, 34, 10, 6, 22]), (s, [5, 6, 5, 5, 10, 8, 50, 40, 50, 18, 70, 24])):
        for i, w in enumerate(widths): ws.column_dimensions[chr(65 + i)].width = w
        for c in ws[1]: c.font = Font(bold=True); c.fill = PatternFill("solid", fgColor="DDE3EC")
        ws.freeze_panes = "A2"; ws.auto_filter.ref = ws.dimensions
    for row in s.iter_rows(min_row=2):
        for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(OUT / "영상대본_전체.xlsx"); print("전체", len(docs), "편 →", OUT / "영상대본_전체.xlsx")

if __name__ == "__main__": main()
