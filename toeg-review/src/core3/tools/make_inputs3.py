#!/usr/bin/env python3
"""번호가 1·2로 끝나는 원문항(164개)을 모아 (1) 정리 엑셀·MD, (2) 출제 워크플로 입력 배치(src/core3/in/*.json)를 만든다.
입력 배치 항목: key, grade, no, chapter, chapter_name, ref{stem,passage,c,ans,expl}, existing_variants_BtoF{B..F}, existing_pretest(있으면), target_answer_positions[3]"""
import json, re, sys, collections
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
HERE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(HERE / "tools" / "video")); import make_scripts as MS

OUT = HERE / "src/core3"; (OUT / "in").mkdir(parents=True, exist_ok=True)
RES = HERE / "결과/변형문항_1·2번"; RES.mkdir(parents=True, exist_ok=True)
idx = json.load(open(HERE / "page/data/index.json", encoding="utf-8"))
P = {x["key"]: x for x in json.load(open(HERE / "src/pretest/P.json", encoding="utf-8"))}
chof = {f"{g}-{n}": (c["ch"], c["chn"]) for g, chs in idx["grades"].items() for c in chs for n in c["nos"]}
sel = [k for k in idx["order"] if int(k.split("-")[1]) % 10 in (1, 2)]
items = {}
for k, T, it, g, ch, chn in MS.load_all("ABCDEF"):
    if k in sel: items.setdefault(k, {})[T] = it

def rule_of(expl):
    m = re.search(r"핵심 규칙:\s*(.*)", expl or ""); return m.group(1).strip() if m else ""
def targets(k, ans):
    """세 변형의 권장 정답 위치: 원문항 정답을 뺀 네 자리 가운데 번호에 따라 돌려 가며 셋"""
    g, n = map(int, k.split("-")); avail = [p for p in (1, 2, 3, 4, 5) if p != ans]
    s = (n * 3 + g) % 4
    return [avail[(s + i) % 4] for i in range(3)]

units = []
for k in sel:
    g, n = map(int, k.split("-")); ch, chn = chof[k]; A = items[k]["A"]
    units.append({"key": k, "grade": g, "no": n, "chapter": ch, "chapter_name": chn,
                  "ref": {"stem": A["stem"], "passage": A["passage"], "c": A["c"], "ans": A["ans"], "expl": A["expl"]},
                  "existing_variants_BtoF": {T: {kk: items[k][T][kk] for kk in ("stem", "passage", "c", "ans")} for T in "BCDEF"},
                  "existing_pretest": ({kk: P[k][kk] for kk in ("stem", "passage", "c", "ans")} if k in P else None),
                  "target_answer_positions": targets(k, A["ans"])})
# 배치: 급별로 5번호씩
batches = []
for g in "7654321":
    us = [u for u in units if u["grade"] == int(g)]
    for i in range(0, len(us), 5):
        b = us[i:i + 5]; bid = f"K{g}_{i // 5 + 1:02d}"
        json.dump(b, open(OUT / "in" / f"{bid}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        batches.append({"id": bid, "grade": int(g), "keys": [u["key"] for u in b], "file": str(OUT / "in" / f"{bid}.json")})
json.dump(batches, open(OUT / "in" / "_batches.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump({g: [f'{c["ch"]} {c["chn"]}' for c in chs] for g, chs in idx["grades"].items()}, open(OUT / "in" / "_chapters.json", "w", encoding="utf-8"), ensure_ascii=False)

# 정리 엑셀 + MD
C5 = "①②③④⑤"
wb = Workbook(); ws = wb.active; ws.title = "원문항 정리(1·2번)"
ws.append(["급", "챕터", "번호", "핵심 규칙(원문항 해설)", "발문", "지문", "보기 ①", "보기 ②", "보기 ③", "보기 ④", "보기 ⑤", "정답", "프리테스트 있음"])
for u in units:
    r = u["ref"]
    ws.append([u["grade"], f'{u["chapter"]} {u["chapter_name"]}', u["no"], rule_of(r["expl"]), r["stem"], r["passage"] or "", *r["c"], C5[int(r["ans"]) - 1], "O" if u["existing_pretest"] else ""])
for i, w in enumerate([5, 22, 6, 60, 40, 48, 26, 26, 26, 26, 26, 6, 10]): ws.column_dimensions[chr(65 + i)].width = w
for c in ws[1]: c.font = Font(bold=True); c.fill = PatternFill("solid", fgColor="DDE3EC")
for row in ws.iter_rows(min_row=2):
    for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
ws.freeze_panes = "D2"; ws.auto_filter.ref = ws.dimensions
wb.save(RES / "원문항_정리_1·2번.xlsx")
L = ["# 1·2로 끝나는 원문항 정리 (164개)", ""]
for g in "7654321":
    L.append(f"## {g}급"); L.append("")
    for u in units:
        if u["grade"] != int(g): continue
        r = u["ref"]; L.append(f"### {g}급 {u['no']}번 — {u['chapter']} {u['chapter_name']}")
        L.append(f"- 핵심 규칙: {rule_of(r['expl'])}")
        L.append(f"- {r['stem']}");
        if r["passage"]: L += ["", "  " + r["passage"].replace("\n", "\n  "), ""]
        L += [f"  {C5[i]} {x}" for i, x in enumerate(r["c"])] + [f"- 정답: {C5[int(r['ans'])-1]}" + ("  (프리테스트 문항 있음)" if u["existing_pretest"] else ""), ""]
open(RES / "원문항_정리_1·2번.md", "w", encoding="utf-8").write("\n".join(L))
print(len(units), "numbers,", len(batches), "batches →", OUT / "in", "|", RES)
print(collections.Counter(u["grade"] for u in units), "pretest overlap", sum(1 for u in units if u["existing_pretest"]))
