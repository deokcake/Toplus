#!/usr/bin/env python3
"""기준 문항 수정(audit/ref_fixes.py)을 ref.json에 적용한다.
- 고친 문항에는 수정 전 원문항을 orig에, 수정 내용을 fixed에 남긴다(다시 돌려도 orig에서 시작해 두 번 고치지 않는다).
- 수정 전·후를 비교한 내려받기용 엑셀 page/data/ref_changes.xlsx를 만든다(바뀐 칸은 빨간 글씨).
사용: python3 audit/apply_ref_fixes.py   (build_page_data.py도 apply()를 불러 쓴다)"""
import json, re, sys, zipfile, datetime
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ref_fixes import FIXES, DASH, DASH_P

FIELDS = ("stem", "passage", "c", "ans")

def apply(refj):
    changed = {}
    for k, r in refj.items():
        if r.get("orig"):                      # 이미 적용된 적이 있으면 원래 값에서 다시 시작
            for f in FIELDS: r[f] = json.loads(json.dumps(r["orig"][f]))
        r.pop("orig", None); r.pop("fixed", None)
    for k in sorted(set(FIXES) | set(DASH) | set(DASH_P), key=lambda x: tuple(map(int, x.split("-")))):
        r = refj[k]; orig = {f: json.loads(json.dumps(r[f])) for f in FIELDS}; sums = []
        fx = FIXES.get(k)
        if fx:
            if "stem" in fx: r["stem"] = fx["stem"]
            if "passage" in fx: r["passage"] = fx["passage"]
            for old, new in fx.get("psub", []):
                assert r["passage"].count(old) == 1, f"{k} 본문에서 찾지 못함: {old}"
                r["passage"] = r["passage"].replace(old, new)
            for i, v in fx.get("c", {}).items(): r["c"][i] = v
            if "ans" in fx: r["ans"] = fx["ans"]
            sums.append(fx["sum"])
        if k in DASH:
            r["c"] = [x.replace("–", "-") for x in r["c"]]
            sums.append("보기의 구분 기호(–)를 -로 통일했다.")
        if k in DASH_P:
            r["passage"] = r["passage"].replace("–", "-")
            sums.append("본문의 구분 기호(–)를 -로 통일했다.")
        if any(orig[f] != r[f] for f in FIELDS):
            r["orig"] = orig; r["fixed"] = sums; changed[k] = r
    return changed

# ---------- 엑셀(수정 전·후 기록) ----------
def _esc(s): return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
def _col(i):
    s = ""; i += 1
    while i: i, m = divmod(i - 1, 26); s = chr(65 + m) + s
    return s
def _cell(ref, text, style):
    t = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", str(text))
    return f'<c r="{ref}" s="{style}" t="inlineStr"><is><t xml:space="preserve">{_esc(t)}</t></is></c>'

STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<fonts count="3"><font><sz val="10"/><name val="Malgun Gothic"/><family val="3"/><charset val="129"/></font><font><b/><sz val="10"/><name val="Malgun Gothic"/><family val="3"/><charset val="129"/></font><font><sz val="10"/><color rgb="FFFF0000"/><name val="Malgun Gothic"/><family val="3"/><charset val="129"/></font></fonts>
<fills count="4"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill><fill><patternFill patternType="solid"><fgColor rgb="FFDCE9FB"/><bgColor indexed="64"/></patternFill></fill><fill><patternFill patternType="solid"><fgColor rgb="FFF2F2F2"/><bgColor indexed="64"/></patternFill></fill></fills>
<borders count="2"><border><left/><right/><top/><bottom/><diagonal/></border><border><left style="thin"><color rgb="FFB7C4D6"/></left><right style="thin"><color rgb="FFB7C4D6"/></right><top style="thin"><color rgb="FFB7C4D6"/></top><bottom style="thin"><color rgb="FFB7C4D6"/></bottom><diagonal/></border></borders>
<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="6">
<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>
<xf numFmtId="0" fontId="1" fillId="2" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment horizontal="center" vertical="center" wrapText="1"/></xf>
<xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>
<xf numFmtId="0" fontId="2" fillId="0" borderId="1" xfId="0" applyFont="1" applyBorder="1" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>
<xf numFmtId="0" fontId="0" fillId="3" borderId="1" xfId="0" applyFill="1" applyBorder="1" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>
<xf numFmtId="0" fontId="1" fillId="3" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment horizontal="center" vertical="top" wrapText="1"/></xf>
</cellXfs>
<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>"""

def build_xlsx(changed, refj, index, path):
    chap = {}
    for g, chs in index["grades"].items():
        for c in chs:
            for n in c["nos"]: chap[f"{g}-{n}"] = f'{c["ch"]} {c["chn"]}'
    aud = json.load(open(HERE / "ref_audit.json", encoding="utf-8")) if (HERE / "ref_audit.json").exists() else {}
    head = ["문항", "단원", "결함 등급", "결함 내용", "수정 내용", "구분", "발문", "본문", "보기 ①", "보기 ②", "보기 ③", "보기 ④", "보기 ⑤", "정답"]
    widths = [9, 16, 8, 42, 42, 8, 32, 42, 24, 24, 24, 24, 24, 6]
    rows = ['<row r="1" ht="24" customHeight="1">' + "".join(_cell(f"{_col(i)}1", h, 1) for i, h in enumerate(head)) + "</row>"]
    order = {"치명": 0, "중대": 1, "경미": 2}
    keys = sorted(changed, key=lambda k: (min([order[a["level"]] for a in aud.get(k, [])] or [3]), tuple(map(int, k.split("-")))))
    rn = 2
    for k in keys:
        r = refj[k]; o = r["orig"]; g, n = k.split("-")
        lv = " / ".join(sorted({a["level"] for a in aud.get(k, [])}, key=lambda x: order[x])) or "표기"
        prob = "\n".join(a["problem"] for a in aud.get(k, [])) or "보기 구분 기호(-, –)가 섞여 있다."
        fix = "\n".join(r["fixed"])
        def vals(x): return [x["stem"], x["passage"], *x["c"], str(x["ans"])]
        before, after = vals(o), vals(r)
        common = [f"{g}급 {n}번", chap.get(k, ""), lv, prob, fix]
        for label, vv, other in (("수정 전", before, None), ("수정 후", after, before)):
            cells = []
            for i, v in enumerate(common): cells.append(_cell(f"{_col(i)}{rn}", v if label == "수정 전" else "", 4 if label == "수정 전" else 2))
            cells.append(_cell(f"F{rn}", label, 5 if label == "수정 전" else 2))
            for j, v in enumerate(vv):
                st = 3 if (other is not None and v != other[j]) else (4 if label == "수정 전" else 2)
                cells.append(_cell(f"{_col(6 + j)}{rn}", v, st))
            rows.append(f'<row r="{rn}">' + "".join(cells) + "</row>"); rn += 1
    cols = "".join(f'<col min="{i+1}" max="{i+1}" width="{w}" customWidth="1"/>' for i, w in enumerate(widths))
    sheet = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
             f'<dimension ref="A1:N{rn-1}"/><sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>'
             f'<sheetFormatPr defaultRowHeight="15"/><cols>{cols}</cols><sheetData>{"".join(rows)}</sheetData>'
             f'<autoFilter ref="A1:N{rn-1}"/></worksheet>')
    ct = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
          '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/>'
          '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
          '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
          '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
          '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/></Types>')
    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/></Relationships>')
    wb = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
          '<sheets><sheet name="원문항 수정 기록" sheetId="1" r:id="rId1"/></sheets>'
          f'<definedNames><definedName name="_xlnm._FilterDatabase" localSheetId="0" hidden="1">\'원문항 수정 기록\'!$A$1:$N${rn-1}</definedName></definedNames></workbook>')
    wbrels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
              '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
              '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>')
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    core = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            f'<dc:title>TOEG 원문항 수정 기록</dc:title><dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created></cp:coreProperties>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", ct); z.writestr("_rels/.rels", rels); z.writestr("docProps/core.xml", core)
        z.writestr("xl/workbook.xml", wb); z.writestr("xl/_rels/workbook.xml.rels", wbrels)
        z.writestr("xl/styles.xml", STYLES); z.writestr("xl/worksheets/sheet1.xml", sheet)
    # 페이지가 내려받기용으로 읽는 사본(엑셀 양식 파일 tpl/*.json과 같은 base64 JSON)
    import base64
    json.dump({"b64": base64.b64encode(open(path, "rb").read()).decode()}, open(str(path)[:-5] + ".json", "w"))
    return rn - 2

if __name__ == "__main__":
    root = HERE.parent
    refj = json.load(open(root / "page/data/ref.json", encoding="utf-8"))
    index = json.load(open(root / "page/data/index.json", encoding="utf-8"))
    changed = apply(refj)
    json.dump(refj, open(root / "page/data/ref.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    nrows = build_xlsx(changed, refj, index, root / "page/data/ref_changes.xlsx")
    print(f"수정한 기준 문항 {len(changed)}개 (결함 수정 {len(set(FIXES) & set(changed))}, 구분 기호만 {len(set(changed) - set(FIXES))}) · 엑셀 {nrows}행")
