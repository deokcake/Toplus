#!/usr/bin/env python3
"""원문항 해설 내려받기용 엑셀(page/data/ref_expl.xlsx + .json) 만들기."""
import base64, datetime, json, sys, zipfile
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "audit"))
from apply_ref_fixes import STYLES, _cell, _col

def build_ref_expl(refj, index, path):
    chap = {}
    for g, chs in index["grades"].items():
        for c in chs:
            for n in c["nos"]: chap[f"{g}-{n}"] = (c["ch"], c["chn"])
    import explfmt
    head = ["급수", "챕터", "챕터명", "문제번호", "발문", "본문", "보기 ①", "보기 ②", "보기 ③", "보기 ④", "보기 ⑤", "정답",
            "핵심 규칙", "풀이 순서", "문장별 판정", "정답 판단", "선택지 ① 분석", "선택지 ② 분석", "선택지 ③ 분석", "선택지 ④ 분석", "선택지 ⑤ 분석"]
    widths = [6, 8, 18, 8, 34, 44, 22, 22, 22, 22, 22, 6, 50, 60, 50, 46, 40, 40, 40, 40, 40]
    rows = ['<row r="1" ht="24" customHeight="1">' + "".join(_cell(f"{_col(i)}1", h, 1) for i, h in enumerate(head)) + "</row>"]
    rn = 2
    for k in index["order"]:
        r = refj[k]; g, n = k.split("-"); ch, chn = chap.get(k, ("", ""))
        c = list(r["c"]) + [""] * (5 - len(r["c"]))
        vals = [f"{g}급", ch, chn, n, r["stem"], r["passage"], *c[:5], str(r["ans"]), *explfmt.cells(explfmt.parse(r.get("expl", "")))]
        rows.append(f'<row r="{rn}">' + "".join(_cell(f"{_col(i)}{rn}", v, 2) for i, v in enumerate(vals)) + "</row>"); rn += 1
    last = _col(len(head) - 1)
    cols = "".join(f'<col min="{i+1}" max="{i+1}" width="{w}" customWidth="1"/>' for i, w in enumerate(widths))
    sheet = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
             f'<dimension ref="A1:{last}{rn-1}"/><sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>'
             f'<sheetFormatPr defaultRowHeight="15"/><cols>{cols}</cols><sheetData>{"".join(rows)}</sheetData>'
             f'<autoFilter ref="A1:{last}{rn-1}"/></worksheet>')
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
          '<sheets><sheet name="원문항 해설" sheetId="1" r:id="rId1"/></sheets>'
          f'<definedNames><definedName name="_xlnm._FilterDatabase" localSheetId="0" hidden="1">\'원문항 해설\'!$A$1:${last}${rn-1}</definedName></definedNames></workbook>')
    wbrels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
              '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
              '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>')
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    core = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            f'<dc:title>TOEG 원문항 해설</dc:title><dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created></cp:coreProperties>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", ct); z.writestr("_rels/.rels", rels); z.writestr("docProps/core.xml", core)
        z.writestr("xl/workbook.xml", wb); z.writestr("xl/_rels/workbook.xml.rels", wbrels)
        z.writestr("xl/styles.xml", STYLES); z.writestr("xl/worksheets/sheet1.xml", sheet)
    json.dump({"b64": base64.b64encode(open(path, "rb").read()).decode()}, open(str(path)[:-5] + ".json", "w"))
    return rn - 2
