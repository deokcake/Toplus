#!/usr/bin/env python3
"""간단한 마크다운 → 워드(docx) 변환기. 제목(#·##·###), 문단, 글머리(-), 번호(1.), 표(|), **굵게**를 지원한다.
한글(HWP)·구글 문서에서도 표가 어긋나지 않도록 표 폭(tblW·gridCol·tcW)을 맞춘다."""
import re
from docx import Document
from docx.shared import Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

KO = "맑은 고딕"; EN = "맑은 고딕"
TCPR_ORDER = ["cnfStyle", "tcW", "gridSpan", "hMerge", "vMerge", "tcBorders", "shd", "noWrap", "tcMar", "textDirection", "tcFitText", "vAlign", "hideMark"]

def set_font(run, size=None, bold=None, color=None, italic=None):
    run.font.name = EN
    rpr = run._r.get_or_add_rPr(); rf = rpr.find(qn("w:rFonts"))
    if rf is None: rf = OxmlElement("w:rFonts"); rpr.insert(0, rf)
    for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"): rf.set(qn(a), KO)
    if size: run.font.size = Pt(size)
    if bold is not None: run.bold = bold
    if italic is not None: run.italic = italic
    if color: run.font.color.rgb = RGBColor.from_string(color)

def add_inline(p, text, size=10.5, color=None, bold=None):
    for part in re.split(r"(\*\*.*?\*\*|`[^`]*`)", text):
        if not part: continue
        if part.startswith("**"): r = p.add_run(part[2:-2]); set_font(r, size, True, color)
        elif part.startswith("`"): r = p.add_run(part[1:-1]); set_font(r, size, bold, "1F3A5F")
        else: r = p.add_run(part); set_font(r, size, bold, color)

def tc_insert(tcPr, el):
    name = el.tag.split("}")[1]; i = TCPR_ORDER.index(name)
    for ch in tcPr:
        t = ch.tag.split("}")[1]
        if t in TCPR_ORDER and TCPR_ORDER.index(t) > i: ch.addprevious(el); return
    tcPr.append(el)

def shade_cell(cell, fill):
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    tc_insert(cell._tc.get_or_add_tcPr(), shd)

def tbl_widths(t, widths_mm):
    tbl = t._tbl; tblPr = tbl.tblPr
    tw = tblPr.find(qn("w:tblW"))
    if tw is None:
        tw = OxmlElement("w:tblW"); st = tblPr.find(qn("w:tblStyle"))
        (st.addnext(tw) if st is not None else tblPr.insert(0, tw))
    tw.set(qn("w:type"), "dxa"); tw.set(qn("w:w"), str(Mm(sum(widths_mm)).twips))
    t.autofit = False
    grid = tbl.tblGrid
    for gc in list(grid): grid.remove(gc)
    for w in widths_mm:
        gc = OxmlElement("w:gridCol"); gc.set(qn("w:w"), str(Mm(w).twips)); grid.append(gc)
    for row in t.rows:
        for i, cell in enumerate(row.cells):
            if i < len(widths_mm): cell.width = Mm(widths_mm[i])

def shade_para(p, fill):
    ppr = p._p.get_or_add_pPr(); shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    after = ["tabs", "spacing", "ind", "jc", "rPr", "sectPr"]
    for ch in ppr:
        if ch.tag.split("}")[1] in after: ch.addprevious(shd); return
    ppr.append(shd)

def footer_pagenum(section, label):
    """바닥글: 문서 이름 - 쪽 번호."""
    f = section.footer; f.is_linked_to_previous = False
    p = f.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(label + "  -  "); set_font(r, 9, color="666666")
    for tag, txt in (("begin", None), (None, "PAGE"), ("end", None)):
        r = p.add_run(); set_font(r, 9, color="666666")
        if tag:
            fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), tag); r._r.append(fc)
        else:
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = txt; r._r.append(it)

def new_doc(title, subtitle=None, date=None):
    doc = Document()
    st = doc.styles["Normal"]; st.font.name = EN; st.font.size = Pt(10.5)
    rpr = st.element.get_or_add_rPr(); rf = rpr.find(qn("w:rFonts"))
    if rf is None: rf = OxmlElement("w:rFonts"); rpr.insert(0, rf)
    for a in ("w:ascii", "w:hAnsi", "w:eastAsia"): rf.set(qn(a), KO)
    st.paragraph_format.space_after = Pt(4); st.paragraph_format.line_spacing = 1.25
    z = doc.settings.element.find(qn("w:zoom"))
    if z is not None and z.get(qn("w:percent")) is None: z.set(qn("w:percent"), "100")
    sec = doc.sections[0]; sec.page_width = Mm(210); sec.page_height = Mm(297)
    sec.left_margin = sec.right_margin = Mm(20); sec.top_margin = Mm(20); sec.bottom_margin = Mm(18)
    sec.footer_distance = Mm(8); footer_pagenum(sec, title)
    p = doc.add_paragraph(); r = p.add_run(title); set_font(r, 20, True, "1F3A5F"); p.paragraph_format.space_after = Pt(2)
    if subtitle:
        p = doc.add_paragraph(); r = p.add_run(subtitle); set_font(r, 11, False, "555555"); p.paragraph_format.space_after = Pt(2)
    if date:
        p = doc.add_paragraph(); r = p.add_run(date); set_font(r, 9.5, False, "777777"); p.paragraph_format.space_after = Pt(10)
    return doc

def heading(doc, text, level):
    p = doc.add_paragraph(); size = {1: 15, 2: 12.5, 3: 11}[level]
    r = p.add_run(text); set_font(r, size, True, "1F3A5F" if level < 3 else "333333")
    pf = p.paragraph_format; pf.space_before = Pt({1: 16, 2: 11, 3: 7}[level]); pf.space_after = Pt(4); pf.keep_with_next = True
    if level == 1: shade_para(p, "E8EEF7")
    return p

def table(doc, rows, widths=None, header=True):
    ncol = max(len(r) for r in rows)
    t = doc.add_table(rows=len(rows), cols=ncol); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    total = 170.0
    if not widths:
        # 열 폭: 가장 긴 글 길이에 비례하되, 짧은 열도 최소 폭(한글 4~5자)을 보장한다
        lens = [min(max(max(len(x) for x in (r[c] if c < len(r) else "").split("<br>")) for r in rows) + 2, 60) for c in range(ncol)]
        minw = 16.0 if ncol <= 4 else 13.0
        rest = total - minw * ncol
        widths = [round(minw + rest * l / sum(lens), 1) for l in lens]
    tbl_widths(t, widths)
    for ri, r in enumerate(rows):
        for ci in range(ncol):
            cell = t.rows[ri].cells[ci]; p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(1); p.paragraph_format.line_spacing = 1.15
            txt = r[ci] if ci < len(r) else ""
            for li, line in enumerate(txt.split("<br>")):
                if li: p = cell.add_paragraph(); p.paragraph_format.space_after = Pt(1); p.paragraph_format.line_spacing = 1.15
                add_inline(p, line.strip(), 9.5, bold=(True if header and ri == 0 else None))
            if header and ri == 0: shade_cell(cell, "DCE6F1")
    sp = doc.add_paragraph(); sp.paragraph_format.space_after = Pt(2)
    return t

def bullet(doc, text, level=0, numbered=None):
    p = doc.add_paragraph(); pf = p.paragraph_format
    pf.left_indent = Mm(6 + 6 * level); pf.first_line_indent = Mm(-4.5); pf.space_after = Pt(2); pf.line_spacing = 1.22
    mark = f"{numbered}. " if numbered else ("• " if level == 0 else "– ")
    r = p.add_run(mark); set_font(r, 10.5)
    add_inline(p, text, 10.5)
    return p

def render(doc, md):
    lines = md.strip("\n").split("\n"); i = 0; num = 0
    while i < len(lines):
        l = lines[i].rstrip()
        if not l.strip(): num = 0; i += 1; continue
        if l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells): rows.append(cells)
                i += 1
            table(doc, rows); continue
        m = re.match(r"^(#{1,3})\s+(.*)", l)
        if m: heading(doc, m.group(2), len(m.group(1))); i += 1; continue
        m = re.match(r"^(\s*)-\s+(.*)", l)
        if m: bullet(doc, m.group(2), len(m.group(1)) // 2); i += 1; continue
        m = re.match(r"^(\d+)\.\s+(.*)", l)
        if m: num += 1; bullet(doc, m.group(2), 0, numbered=num); i += 1; continue
        if l.startswith(">"):
            p = doc.add_paragraph(); add_inline(p, l[1:].strip(), 10, "444444"); p.paragraph_format.left_indent = Mm(6); shade_para(p, "F5F5F5"); i += 1; continue
        p = doc.add_paragraph(); add_inline(p, l.strip(), 10.5); i += 1
    return doc
