#!/usr/bin/env python3
"""‘핵심 확인’ 변형 문항 워크플로 결과를 모아 엑셀·MD로 만든다.
사용: python3 assemble3.py <workflow journal.jsonl> [<journal.jsonl> ...]
- journal의 result 줄(label write:/revise:/solve:/review:)에서 번호#변형마다 마지막 글을 모은다(revise가 write를 덮음).
- 마지막 검토(solve·review) 결과에서 심각한 지적이 남은 변형은 ‘검토 메모’에 적는다.
결과: src/core3/out/items.json, 결과/변형문항_1·2번/변형문항_1·2번_3개씩.xlsx, 급별 MD"""
import json, re, sys, collections
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
HERE = Path(__file__).resolve().parents[3]
RES = HERE / "결과/변형문항_1·2번"; OUT = HERE / "src/core3/out"; OUT.mkdir(parents=True, exist_ok=True)
C5 = "①②③④⑤"

def harvest(journals):
    items = {}; solve = {}; crit = {}; order = []; ver = {}; vround = {}   # ver: 글이 몇 번째 수정판인지, vround: 마지막 검증이 본 판
    for j in journals:
        lab = {}
        for l in open(j, encoding="utf-8"):
            d = json.loads(l)
            if d.get("type") == "started": lab[d["agentId"]] = d.get("label", "")
            if d.get("type") != "result" or not isinstance(d.get("result"), dict): continue
            L = lab.get(d.get("agentId"), ""); r = d["result"]
            if L.startswith(("write:", "revise:")):
                rnd = int(L.rsplit(":", 1)[1]) if L.startswith("revise:") else 0
                for it in r.get("items") or []:
                    i = f"{it['key']}#{it['variant']}"
                    if i not in items: order.append(i)
                    items[i] = it; ver[i] = rnd
            elif L.startswith("solve:"):
                rnd = int(L.rsplit(":", 1)[1])
                for x in r.get("results") or []: solve[x["id"]] = x; vround[("s", x["id"])] = rnd
            elif L.startswith("review:"):
                rnd = int(L.rsplit(":", 1)[1])
                for x in r.get("results") or []: crit[x["id"]] = x; vround[("c", x["id"])] = rnd
    # 검토 메모(마지막 결과 기준)
    for i, it in items.items():
        notes = []; s = solve.get(i); c = crit.get(i)
        if s and s.get("solved") != it["ans"]: notes.append(f"독립 풀이가 {('없음' if s['solved']==0 else C5[s['solved']-1])}을 고름(정답 {C5[it['ans']-1]}): {s.get('notes','')}")
        if s and [x for x in s.get("other_defensible", []) if x != it["ans"]]: notes.append("다른 보기도 가능: " + ", ".join(C5[x-1] for x in s["other_defensible"] if x != it["ans"]))
        if s: notes += [f"영어: {e}" for e in s.get("english_issues", [])]
        if c and c.get("difficulty_vs_reference") != "same": notes.append(f"난이도 {c['difficulty_vs_reference']}: {c.get('difficulty_reason','')}")
        if c: notes += [f"[{x['severity']}] {x['rule']}: {x['problem']}" for x in c.get("issues", []) if x.get("severity") != "minor"]
        it["review_note"] = "\n".join(notes); it["difficulty"] = (c or {}).get("difficulty_vs_reference", "")
        serious = bool(s and (s.get("solved") != it["ans"] or [x for x in s.get("other_defensible", []) if x != it["ans"]] or s.get("english_issues"))) or bool(c and (c.get("verdict") == "fix" or c.get("difficulty_vs_reference") == "harder"))
        seen = min(vround.get(("s", i), -1), vround.get(("c", i), -1))   # 두 검증이 모두 본 판
        if not (s and c): it["status"] = "검증 전"
        elif seen < ver.get(i, 0): it["status"] = "수정 후 재검증 전"; it["review_note"] = "(수정 전 판에 대한 지적)\n" + it["review_note"] if it["review_note"] else ""
        else: it["status"] = "지적 남음" if serious else "검증 통과"
    return [items[i] for i in order]

def main(journals):
    its = harvest(journals)
    idx = json.load(open(HERE / "page/data/index.json", encoding="utf-8"))
    chof = {f"{g}-{n}": f'{c["ch"]} {c["chn"]}' for g, chs in idx["grades"].items() for c in chs for n in c["nos"]}
    ref = json.load(open(HERE / "page/data/ref.json", encoding="utf-8"))
    key_order = {k: i for i, k in enumerate(idx["order"])}
    its.sort(key=lambda it: (key_order.get(it["key"], 9999), it["variant"]))
    json.dump(its, open(OUT / "items.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    wb = Workbook(); ws = wb.active; ws.title = "변형 문항(3개씩)"
    ws.append(["급", "챕터", "번호", "변형", "형식", "발문", "지문", "보기 ①", "보기 ②", "보기 ③", "보기 ④", "보기 ⑤", "정답", "출제 의도", "난이도 비교", "검토 메모(남은 지적)", "검증 상태"])
    for it in its:
        g, n = it["key"].split("-")
        ws.append([int(g), chof.get(it["key"], ""), int(n), it["variant"], it.get("new_format", ""), it["stem"], it.get("passage") or "", *it["c"], C5[it["ans"] - 1], it.get("design", ""), it.get("difficulty", ""), it.get("review_note", ""), it.get("status", "")])
        if it.get("review_note"): ws.cell(ws.max_row, 16).fill = PatternFill("solid", fgColor="FFF3CD")
        ws.cell(ws.max_row, 17).fill = PatternFill("solid", fgColor={"검증 통과": "D1E7DD", "지적 남음": "F8D7DA", "수정 후 재검증 전": "FFF3CD"}.get(it.get("status"), "EEEEEE"))
    for i, w in enumerate([5, 20, 6, 5, 26, 40, 46, 24, 24, 24, 24, 24, 6, 60, 10, 50, 10]): ws.column_dimensions[chr(65 + i)].width = w
    for c in ws[1]: c.font = Font(bold=True); c.fill = PatternFill("solid", fgColor="DDE3EC")
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "E2"; ws.auto_filter.ref = ws.dimensions
    # 원문항과 나란히 보는 시트
    ws2 = wb.create_sheet("원문항과 나란히")
    ws2.append(["급", "번호", "구분", "발문", "지문", "보기 ①", "보기 ②", "보기 ③", "보기 ④", "보기 ⑤", "정답", "형식"])
    for k in idx["order"]:
        vs = [it for it in its if it["key"] == k]
        if not vs: continue
        r = ref[k]; g, n = k.split("-")
        ws2.append([int(g), int(n), "원문항", r["stem"], r["passage"] or "", *r["c"], C5[int(r["ans"]) - 1], vs[0].get("ref_format", "")])
        for c in ws2[ws2.max_row]: c.fill = PatternFill("solid", fgColor="EEF3FF")
        for it in vs: ws2.append([int(g), int(n), f"변형 {it['variant']}", it["stem"], it.get("passage") or "", *it["c"], C5[it["ans"] - 1], it.get("new_format", "")])
    for i, w in enumerate([5, 6, 8, 40, 46, 24, 24, 24, 24, 24, 6, 26]): ws2.column_dimensions[chr(65 + i)].width = w
    for c in ws2[1]: c.font = Font(bold=True); c.fill = PatternFill("solid", fgColor="DDE3EC")
    for row in ws2.iter_rows(min_row=2):
        for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
    ws2.freeze_panes = "D2"
    RES.mkdir(parents=True, exist_ok=True); wb.save(RES / "변형문항_1·2번_3개씩.xlsx")
    for g in "7654321":
        L = [f"# {g}급 1·2번 문항 ‘핵심 확인’ 변형 (번호마다 3개)", ""]
        for k in idx["order"]:
            if k.split("-")[0] != g: continue
            vs = [it for it in its if it["key"] == k]
            if not vs: continue
            r = ref[k]; L.append(f"## {g}급 {k.split('-')[1]}번 — {chof.get(k,'')}"); L.append(f"원문항: {r['stem']}" + (f"  {r['passage']}" if r["passage"] else "") + "  " + " ".join(f"{C5[i]} {x}" for i, x in enumerate(r["c"])) + f"  (정답 {C5[int(r['ans'])-1]})"); L.append("")
            for it in vs:
                L.append(f"### 변형 {it['variant']} — {it.get('new_format','')}"); L.append(it["stem"])
                if it.get("passage"): L += ["", "  " + it["passage"].replace("\n", "\n  "), ""]
                L += [f"  {C5[i]} {x}" for i, x in enumerate(it["c"])] + [f"정답: {C5[it['ans']-1]}  ({it.get('status','')})"]
                if it.get("review_note"): L.append(f"검토 메모: {it['review_note']}")
                L.append("")
        open(RES / f"{g}급_변형문항_1·2번.md", "w", encoding="utf-8").write("\n".join(L))
    c = collections.Counter(it["key"].split("-")[0] for it in its); st = collections.Counter(it.get("status") for it in its)
    print(len(its), "items", dict(sorted(c.items())), "| 상태", dict(st), "→", RES)

if __name__ == "__main__": main(sys.argv[1:])
