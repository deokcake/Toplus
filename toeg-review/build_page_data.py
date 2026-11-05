#!/usr/bin/env python3
"""온라인 감수 페이지용 데이터(page/data)와 엑셀 틀(page/tpl)을 만든다."""
import io, json, re, shutil, sys, zipfile
from xml.sax.saxutils import escape
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.argv = ["x", str(HERE / "src")]
import screen, assemble, export

OUT = HERE / "page"
ref, _ = screen.load()
out, missing, ref_notes = assemble.build()
assert not missing
by_key = {(o["type"], o["grade"], o["no"]): o for o in out}
scr = {r["id"]: r for r in json.load(open(HERE / "src" / "screen.json", encoding="utf-8"))}

# 기준 문항 전체 점검 결과(audit/ref_audit.json): 문항 내용은 그대로 두고 확인 사항만 덧붙인다
AUD = json.load(open(HERE / "audit" / "ref_audit.json", encoding="utf-8")) if (HERE / "audit" / "ref_audit.json").exists() else {}
refj = {}
for (g, n), r in ref.items():
    refj[f"{g}-{n}"] = {"stem": r["stem"], "passage": r["passage"], "c": r["choices"], "ans": r["answer"],
                        "inline": bool(r.get("inline")), "note": ref_notes.get((g, n), ""), "audit": AUD.get(f"{g}-{n}", [])}
# 기준 문항 수정(audit/ref_fixes.py) 적용: 수정 전 원문항은 orig에 남기고 내려받기용 기록 엑셀을 만든다
sys.path.insert(0, str(HERE / "audit"))
import apply_ref_fixes
_changed = apply_ref_fixes.apply(refj)
# 2차 감수(rv2/*.py): 원문항 해설(문항별 풀이 순서 포함)을 붙이고, 변형 문항 판정을 2차 판정으로 바꾼다
import rv2build
EX2, REV2 = rv2build.load()
for _k, _r in refj.items():
    _g, _n = map(int, _k.split("-"))
    _r["expl"] = rv2build.ref_expl(EX2[(_g, _n)], _r)
json.dump(refj, open(OUT / "data" / "ref.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

index = {"types": "BCDEF", "grades": {}, "verdicts": {}, "style": {}}
review2 = []
def patch_tpl(data, changes, style):
    """감수결과 엑셀의 판정(R)·판정 근거(S)·수정 제안(T) 칸을 2차 감수 결과로 바꾼다."""
    zin = zipfile.ZipFile(io.BytesIO(data)); sh = zin.read("xl/worksheets/sheet1.xml").decode("utf-8")
    def cell(ref, text, s): return f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{escape(str(text))}</t></is></c>'
    def fix_row(m):
        rn = int(m.group(2))
        if rn not in changes: return m.group(0)
        final, reason, fix = changes[rn]; body = m.group(3)
        for col, text, st in (("R", final, style[final]), ("S", reason, style["text"]), ("T", fix, style["text"])):
            body, k = re.subn(r'<c r="%s%d"[^>]*?(?:/>|>.*?</c>)' % (col, rn), lambda _m: cell(f"{col}{rn}", text, st), body, count=1, flags=re.S)
            assert k == 1, (col, rn)
        return f"{m.group(1)}{body}</row>"
    sh, n = re.subn(r'(<row r="(\d+)"[^>]*>)(.*?)</row>', fix_row, sh, flags=re.S)
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for item in zin.infolist():
            z.writestr(item, sh.encode("utf-8") if item.filename == "xl/worksheets/sheet1.xml" else zin.read(item.filename))
    return out.getvalue()
for t in "BCDEF":
    rows = []; tplchg = {}
    recs = json.load(open(HERE / "src" / f"{t}.json", encoding="utf-8"))
    for i, r in enumerate(recs):
        g, n = int(r["급수"].replace("급", "")), int(r["문제번호"])
        o = by_key[(t, g, n)]
        reason, fix = export.compose(o)
        rows.append({"rn": i + 2, "g": g, "n": n, "ch": r["챕터"], "chn": r["챕터명"],
                     "stem": r["문제명"], "passage": r["본문"],
                     "c": [r[f"보기 문항{k}"] for k in range(1, 6)], "ans": r["정답"], "expl": r["설명"],
                     "v": o["final"], "why": reason, "fix": fix, "auto": export.auto_text(scr[o["id"]])})
        recs2 = REV2.get((g, n, t), [])
        if recs2:
            row = rows[-1]; v0 = row["v"]; vs = [x["v"] for x in recs2 if x.get("v")]
            if vs and vs[-1] != v0: row["v1"] = v0; row["v"] = vs[-1]
            row["rv2"] = [{"v": x.get("v", ""), "why": x.get("why", ""), "fix": x.get("fix", ""), "fx": bool(x.get("fx"))} for x in recs2]
            whys = " ".join(x["why"] for x in row["rv2"] if x["why"]); fixes = "; ".join(x["fix"] for x in row["rv2"] if x["fix"])
            review2.append({"key": f"{g}-{n}", "type": t, "v0": row.get("v1", ""), "v": row["v"], "why": whys, "fix": fixes, "fx": any(x["fx"] for x in row["rv2"])})
            if "v1" in row:
                tplchg[i + 2] = (row["v"], "[2차 감수] " + whys + "\n[1차 감수] " + reason, ("[2차 감수] " + fixes + ("\n[1차 감수] " + fix if fix else "")) if fixes else fix)
            else:
                tplchg[i + 2] = (row["v"], reason + "\n[2차 감수] " + whys, fix)
        index["verdicts"].setdefault(f"{g}-{n}", {})[t] = rows[-1]["v"]
        if t == "B":
            gd = index["grades"].setdefault(str(g), [])
            if not gd or gd[-1]["ch"] != r["챕터"]:
                gd.append({"ch": r["챕터"], "chn": r["챕터명"], "nos": []})
            gd[-1]["nos"].append(n)
    json.dump(rows, open(OUT / "data" / f"{t}.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    src = HERE / "결과" / f"{t} type 감수결과.xlsx"
    import base64
    st = zipfile.ZipFile(src).read("xl/styles.xml").decode()
    nx = int(re.search(r'<cellXfs count="(\d+)"', st).group(1)) - 5
    index["style"][t] = {"text": nx, "적합": nx + 1, "수정(표기)": nx + 2, "수정(내용)": nx + 3, "부적합": nx + 4}
    (OUT / "tpl" / f"{t}.json").write_text(json.dumps({"b64": base64.b64encode(patch_tpl(src.read_bytes(), tplchg, index["style"][t])).decode()}))
index["order"] = [f"{r['g']}-{r['n']}" for r in json.load(open(OUT / "data" / "B.json", encoding="utf-8"))]

# 프리테스트(P): 급·챕터마다 고른 원문항 80개에 대해 형식을 바꿔 새로 만든 문항(src/pretest/P.json).
# 유형 목록에 P를 붙이되, 이 유형에는 80개 번호만 있다(index.subset). 내려받기 엑셀 틀은 B 틀에서 같은 번호의 행을 가져와 만든다.
def p_tpl(data, prows, pos, text_style):
    zin = zipfile.ZipFile(io.BytesIO(data)); sh = zin.read("xl/worksheets/sheet1.xml").decode("utf-8")
    rows = {int(m.group(2)): m for m in re.finditer(r'(<row r="(\d+)"[^>]*>)(.*?)</row>', sh, flags=re.S)}
    head, tail = sh[:rows[1].start()], sh[rows[max(rows)].end():]
    def cell(ref, text, s): return f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{escape(str(text))}</t></is></c>'
    out = [rows[1].group(0)]
    for r in prows:
        brn, rn = pos[f"{r['g']}-{r['n']}"] + 2, r["rn"]; m = rows[brn]
        attrs = re.sub(r'\s(?:ht|customHeight)="[^"]*"', "", m.group(1)).replace(f'r="{brn}"', f'r="{rn}"', 1)
        cells = {c.group(1): c.group(0) for c in re.finditer(r'<c r="([A-Z]+)%d"[^>]*?(?:/>|>.*?</c>)' % brn, m.group(3), flags=re.S)}
        sty = lambda col: (re.search(r'\ss="(\d+)"', cells.get(col, "")) or [None, str(text_style)])[1]
        vals = {"E": "프리테스트", "I": r["stem"], "J": r["passage"], "P": r["ans"], "Q": r["expl"], "R": "", "S": r["why"], "T": "", "U": r["auto"], "V": ""}
        vals.update({col: r["c"][i] for i, col in enumerate("KLMNO")})
        body = ""
        for col in "ABCDEFGHIJKLMNOPQRSTUV":
            if col in vals: body += cell(f"{col}{rn}", vals[col], text_style if col in "RSTUV" else sty(col))
            elif col in cells: body += cells[col].replace(f'r="{col}{brn}"', f'r="{col}{rn}"', 1)
        out.append(f"{attrs}{body}</row>")
    sh = re.sub(r'<dimension ref="A1:V\d+"/>', f'<dimension ref="A1:V{len(prows) + 1}"/>', head + "".join(out) + tail)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for item in zin.infolist():
            z.writestr(item, sh.encode("utf-8") if item.filename == "xl/worksheets/sheet1.xml" else zin.read(item.filename))
    return buf.getvalue()
PT = HERE / "src" / "pretest" / "P.json"
if PT.exists():
    import base64
    pos = {k: i for i, k in enumerate(index["order"])}
    chof = {f"{g}-{n}": (c["ch"], c["chn"]) for g, chs in index["grades"].items() for c in chs for n in c["nos"]}
    pitems = sorted(json.load(open(PT, encoding="utf-8")), key=lambda x: pos[x["key"]])
    prows = []
    for i, x in enumerate(pitems):
        g, n = map(int, x["key"].split("-")); ch, chn = chof[x["key"]]
        prows.append({"rn": i + 2, "g": g, "n": n, "ch": ch, "chn": chn, "stem": x["stem"], "passage": x["passage"], "c": x["c"], "ans": str(x["ans"]), "expl": x["expl"],
                      "v": "신규 출제", "why": f"원문항 형식: {x['ref_format']}\n프리테스트 형식: {x['new_format']}\n{x['design']}", "fix": "", "auto": x.get("auto", "")})
    json.dump(prows, open(OUT / "data" / "P.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    (OUT / "data" / "fix_P.json").write_text("{}")
    index["types"] += "P"; index["subset"] = {"P": [f"{r['g']}-{r['n']}" for r in prows]}; index["labels"] = {"P": "프리테스트"}
    index["style"]["P"] = index["style"]["B"]
    btpl = base64.b64decode(json.load(open(OUT / "tpl" / "B.json"))["b64"])
    (OUT / "tpl" / "P.json").write_text(json.dumps({"b64": base64.b64encode(p_tpl(btpl, prows, pos, index["style"]["B"]["text"])).decode()}))
    print("프리테스트:", len(prows), "문항")
# 해설 감수(Claude 지적·수정안): src/expl_review/review.json → data/expl_review.json. 승인은 페이지에서 DB(t_A·t_B…)의 explAudit에 기록된다.
index.setdefault("labels", {})["A"] = "원문항"
XR = HERE / "src" / "expl_review" / "review.json"
json.dump(json.load(open(XR, encoding="utf-8")) if XR.exists() else {}, open(OUT / "data" / "expl_review.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
json.dump(index, open(OUT / "data" / "index.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
apply_ref_fixes.build_xlsx(_changed, refj, index, OUT / "data" / "ref_changes.xlsx")
json.dump(review2, open(OUT / "data" / "review2.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
import rv2xlsx
rv2xlsx.build_ref_expl(refj, index, OUT / "data" / "ref_expl.xlsx")
print("2차 감수:", len(review2), "건 (판정 바뀜", sum(1 for x in review2 if x["v0"]), "· 수정 예시 고침", sum(1 for x in review2 if x["fx"]), ")")
for p in sorted((OUT / "data").glob("*.json")) + sorted((OUT / "tpl").glob("*")):
    print(p.name, p.stat().st_size)
print(index["style"])
