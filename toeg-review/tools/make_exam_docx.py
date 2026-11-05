#!/usr/bin/env python3
"""기준 문항(A)과 B 유형 확정본의 학생용 시험지와 정답·해설을 급수별 워드 파일로 만든다.
사용: python3 tools/make_exam_docx.py [A|B|all] [급수 ...]
  → 결과/시험지/TOEG_n급_기준문항_시험지.docx·_정답해설.docx, TOEG_n급_B유형_시험지.docx·_정답해설.docx"""
import json, re, sys, math
from pathlib import Path
from docx import Document
from docx.shared import Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ROW_HEIGHT_RULE, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent)); import final_items as FI
SRC = {"A": FI.load_ref(), "B": FI.load_B()[0]}
NAME = {"A": ("기준문항", "", "기준 문항"), "B": ("B유형", " (B형)", "B 유형(변형 문항)")}
idx = json.load(open(HERE / "page/data/index.json", encoding="utf-8"))
OUT = HERE / "결과/시험지"; OUT.mkdir(parents=True, exist_ok=True)
C5 = "①②③④⑤"
KO = "맑은 고딕"; EN = "Times New Roman"
LABELS = ("핵심 규칙:", "풀이 순서:", "문장별 판정:", "정답 판단:", "선택지 분석:")

def set_fonts(run, size=None, bold=None, color=None):
    run.font.name = EN
    rpr = run._r.get_or_add_rPr(); rf = rpr.find(qn("w:rFonts"))
    if rf is None: rf = OxmlElement("w:rFonts"); rpr.insert(0, rf)
    rf.set(qn("w:ascii"), EN); rf.set(qn("w:hAnsi"), EN); rf.set(qn("w:eastAsia"), KO); rf.set(qn("w:cs"), EN)
    if size: run.font.size = Pt(size)
    if bold is not None: run.bold = bold
    if color: run.font.color.rgb = RGBColor.from_string(color)

def add_runs(p, text, size=None, bold=None, color=None):
    """<u>…</u>를 밑줄 런으로 바꿔 넣는다."""
    for part in re.split(r"(<u>.*?</u>)", text, flags=re.S):
        if not part: continue
        if part.startswith("<u>"):
            r = p.add_run(part[3:-4]); r.underline = True
        else: r = p.add_run(part)
        set_fonts(r, size, bold, color)
    return p

def fmt(p, text="", size=None, bold=None, color=None, align=None, after=2, before=0, left=None, hanging=None, keep_next=False, keep=False, line=1.12):
    """이미 있는 문단에 서식을 입힌다."""
    pf = p.paragraph_format; pf.space_after = Pt(after); pf.space_before = Pt(before); pf.line_spacing = line
    if left is not None: pf.left_indent = Mm(left)
    if hanging is not None: pf.first_line_indent = Mm(-hanging)
    if align: p.alignment = align
    pf.keep_with_next = keep_next; pf.keep_together = keep
    if text: add_runs(p, text, size, bold, color)
    return p

def para(container, text="", size=None, bold=None, color=None, **kw):
    return fmt(container.add_paragraph(), text, size, bold, color, **kw)

def tiny(p, pt=3):
    """빈 문단을 고정 높이(pt)로 줄인다. 표와 표 사이 간격용."""
    pf = p.paragraph_format; pf.space_after = Pt(0); pf.space_before = Pt(0)
    pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(pt); pf.keep_with_next = False; pf.keep_together = False
    for r in p.runs: r.font.size = Pt(2)
    ppr = p._p.get_or_add_pPr(); rpr = ppr.find(qn("w:rPr"))
    if rpr is None: rpr = OxmlElement("w:rPr"); ppr.append(rpr)
    sz = OxmlElement("w:sz"); sz.set(qn("w:val"), "4"); rpr.append(sz)
    return p

def cell_margins(cell, top=0, left=0, bottom=0, right=0):
    tcPr = cell._tc.get_or_add_tcPr(); mar = OxmlElement("w:tcMar")
    for side, v in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        e = OxmlElement(f"w:{side}"); e.set(qn("w:w"), str(v)); e.set(qn("w:type"), "dxa"); mar.append(e)
    tc_insert(tcPr, mar)

def table_indent(table, mm):
    tblPr = table._tbl.tblPr
    for e in tblPr.findall(qn("w:tblInd")): tblPr.remove(e)
    ind = OxmlElement("w:tblInd"); ind.set(qn("w:w"), str(Mm(mm).twips)); ind.set(qn("w:type"), "dxa")
    # tblInd는 tblCellSpacing 뒤, tblBorders 앞
    anchor = next((c for c in tblPr if c.tag.split("}")[1] in ("tblBorders", "shd", "tblLayout", "tblCellMar", "tblLook")), None)
    (anchor.addprevious(ind) if anchor is not None else tblPr.append(ind))

def no_split(table):
    for row in table.rows:
        trPr = row._tr.get_or_add_trPr(); cs = OxmlElement("w:cantSplit"); trPr.append(cs)

PPR_AFTER_SHD = ["tabs", "suppressAutoHyphens", "kinsoku", "wordWrap", "overflowPunct", "topLinePunct", "autoSpaceDE", "autoSpaceDN", "bidi", "adjustRightInd", "snapToGrid", "spacing", "ind",
                 "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc", "textDirection", "textAlignment", "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr", "sectPr", "pPrChange"]
def shade(p, fill):
    """문단 음영. w:shd는 pBdr 뒤, tabs·spacing·ind·jc 앞에 와야 한다."""
    ppr = p._p.get_or_add_pPr(); shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    for child in ppr:
        if child.tag.split("}")[1] in PPR_AFTER_SHD: child.addprevious(shd); return
    ppr.append(shd)

def set_cols(section, n, space_mm=9, sep=True):
    sectPr = section._sectPr
    for c in sectPr.findall(qn("w:cols")): sectPr.remove(c)
    cols = OxmlElement("w:cols"); cols.set(qn("w:num"), str(n)); cols.set(qn("w:space"), str(int(space_mm * 56.7)))
    if sep and n > 1: cols.set(qn("w:sep"), "1")
    # w:cols는 w:pgMar 뒤에 와야 한다
    pgmar = sectPr.find(qn("w:pgMar"))
    (pgmar.addnext(cols) if pgmar is not None else sectPr.append(cols))

def setup(doc, two_cols):
    st = doc.styles["Normal"]; st.font.name = EN; st.font.size = Pt(10.5)
    rpr = st.element.get_or_add_rPr(); rf = rpr.find(qn("w:rFonts"))
    if rf is None: rf = OxmlElement("w:rFonts"); rpr.insert(0, rf)
    rf.set(qn("w:ascii"), EN); rf.set(qn("w:hAnsi"), EN); rf.set(qn("w:eastAsia"), KO)
    z = doc.settings.element.find(qn("w:zoom"))
    if z is not None and z.get(qn("w:percent")) is None: z.set(qn("w:percent"), "100")
    sec = doc.sections[0]; sec.page_width = Mm(210); sec.page_height = Mm(297)
    sec.left_margin = sec.right_margin = Mm(15); sec.top_margin = Mm(16); sec.bottom_margin = Mm(14)
    sec.header_distance = Mm(8); sec.footer_distance = Mm(7)
    return sec

def footer_pagenum(section, label):
    f = section.footer; f.is_linked_to_previous = False
    p = f.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(label + "  -  "); set_fonts(r, 9, color="666666")
    for tag, txt in (("begin", None), (None, "PAGE"), ("end", None)):
        r = p.add_run(); set_fonts(r, 9, color="666666")
        if tag:
            fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), tag); r._r.append(fc)
        else:
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = txt; r._r.append(it)

def tbl_widths(t, widths_mm):
    """표 폭을 확정한다: tblW(dxa)·tblLayout fixed·gridCol·tcW를 모두 같은 값으로 맞춘다.
    python-docx는 gridCol을 본문 전체 폭(180mm)으로 두므로, 격자 폭을 따르는 뷰어(한글·구글 문서 등)에서는
    2단 안의 상자가 옆 단까지 뻗어 글이 겹친다."""
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
    return t

TCPR_ORDER = ["cnfStyle", "tcW", "gridSpan", "hMerge", "vMerge", "tcBorders", "shd", "noWrap", "tcMar", "textDirection", "tcFitText", "vAlign", "hideMark", "headers", "cellIns", "cellDel", "cellMerge", "tcPrChange"]
def tc_insert(tcPr, el):
    """tcPr 자식 순서(스키마)에 맞춰 넣는다. 순서가 틀리면 윈도우 워드가 파일을 '깨진 파일'로 본다."""
    name = el.tag.split("}")[1]; idx = TCPR_ORDER.index(name)
    for child in tcPr:
        tag = child.tag.split("}")[1]
        if tag in TCPR_ORDER and TCPR_ORDER.index(tag) > idx: child.addprevious(el); return el
    tcPr.append(el); return el

def cell_fill(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr(); shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill); tc_insert(tcPr, shd)

def cell_text(cell, text, size=10.5, bold=None, align=None, after=1):
    p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(after); p.paragraph_format.space_before = Pt(0)
    if align: p.alignment = align
    add_runs(p, text, size, bold); return p

def plain(s): return re.sub(r"</?u>", "", s)

def passage_box(host, text, width_mm):
    """제시문을 테두리 상자(한 칸 표)로 host 셀 안에 만든다. 탭으로 나뉜 줄은 상자 안의 표로.
    python-docx가 표 뒤에 붙이는 빈 문단을 돌려준다(호출한 쪽에서 재사용하거나 줄인다)."""
    lines = text.split("\n")
    t = host.add_table(rows=1, cols=1); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_widths(t, [width_mm]); no_split(t)
    cell = t.rows[0].cells[0]; cell_margins(cell, 80, 120, 80, 120)
    pend = None  # 안쪽 표 뒤에 생긴 빈 문단(다음 줄에 재사용)
    first = True; i = 0
    while i < len(lines):
        if "\t" in lines[i] and i + 1 < len(lines) and "\t" in lines[i + 1]:
            rows = []
            while i < len(lines) and "\t" in lines[i]: rows.append(lines[i].split("\t")); i += 1
            if pend is not None: tiny(pend, 4); pend = None
            if first: tiny(cell.paragraphs[0], 2)
            ncol = max(len(r) for r in rows)
            nt = cell.add_table(rows=len(rows), cols=ncol); nt.style = "Table Grid"; nt.alignment = WD_TABLE_ALIGNMENT.CENTER
            inner = width_mm - 5.0  # 칸 안쪽 여백(좌우 120dxa)과 테두리만큼 뺀다
            lens = [max(len(plain(r[ci])) if ci < len(r) else 0 for r in rows) + 2 for ci in range(ncol)]
            tbl_widths(nt, [round(inner * l / sum(lens), 1) for l in lens])
            for ri, r in enumerate(rows):
                for ci, v in enumerate(r):
                    cell_text(nt.rows[ri].cells[ci], v, 10, bold=(ri == 0 or ci == 0), align=WD_ALIGN_PARAGRAPH.CENTER, after=0)
                    if ri == 0: cell_fill(nt.rows[ri].cells[ci], "F2F2F2")
            pend = cell.paragraphs[-1]; first = False; continue
        if pend is not None: p = pend; pend = None
        else: p = cell.paragraphs[0] if first else cell.add_paragraph()
        p.paragraph_format.space_after = Pt(1); p.paragraph_format.line_spacing = 1.15
        add_runs(p, lines[i], 10.5, bold=(lines[i].strip() == "<보기>") or None)
        first = False; i += 1
    if pend is not None: tiny(pend, 2)
    return host.paragraphs[-1]

def numonly(r): return all(x.strip() == C5[i] for i, x in enumerate(r["c"]))

NBSP = "\u00a0"
def add_item(doc, n, r, col_mm, heading=None):
    """문항 하나(챕터 제목·발문·제시문·보기)를 테두리 없는 한 칸 표에 넣는다.
    행에 '나누지 않음'을 걸어 두면 워드·한글·구글 문서 어디서든 문항이 단이나 쪽에서 갈라지지 않는다."""
    wrap = doc.add_table(rows=1, cols=1); wrap.alignment = WD_TABLE_ALIGNMENT.LEFT
    tbl_widths(wrap, [col_mm]); no_split(wrap)
    cell = wrap.rows[0].cells[0]; cell_margins(cell, 0, 0, 40, 0)
    nxt = cell.paragraphs[0]  # 다음에 쓸 문단(셀의 첫 문단 또는 표 뒤 빈 문단)
    def take():
        nonlocal nxt
        if nxt is not None: p, nxt = nxt, None; return p
        return cell.add_paragraph()
    if heading:
        shade(fmt(take(), heading, 10.5, bold=True, after=3, before=4, keep_next=True), "E8EEF7")
    p = fmt(take(), keep_next=True, keep=True, after=2, before=3, left=6, hanging=6)
    add_runs(p, f"{n}. ", 10.5, bold=True); add_runs(p, r["stem"], 10.5)
    if r["passage"]:
        nxt = passage_box(cell, r["passage"], col_mm - 2)
    if numonly(r):
        if nxt is not None: tiny(nxt, 2)
        return
    opts = [plain(x) for x in r["c"]]
    longest = max(len(o) for o in opts)
    per_row = 5 if longest <= 4 else 3 if longest <= 9 else 2 if longest <= 14 else 1
    if per_row > 1 and all("\n" not in o for o in opts):
        # 짧은 보기는 테두리 없는 표에 한 줄 n개씩: 뷰어마다 글자 폭이 달라도 보기 하나가 줄 중간에서 갈라지지 않는다
        if nxt is not None: tiny(nxt, 2); nxt = None
        rows = math.ceil(5 / per_row)
        ot = cell.add_table(rows=rows, cols=per_row); ot.alignment = WD_TABLE_ALIGNMENT.LEFT
        tbl_widths(ot, [(col_mm - 7) / per_row] * per_row); table_indent(ot, 6)
        for i, x in enumerate(r["c"]):
            c = ot.rows[i // per_row].cells[i % per_row]; cell_margins(c, 0, 0, 0, 40)
            fmt(c.paragraphs[0], after=1, before=(1 if i < per_row else 0), line=1.12, keep=True)
            add_runs(c.paragraphs[0], C5[i] + NBSP + x, 10.5)
        nxt = cell.paragraphs[-1]; tiny(nxt, 2)
        return
    for i, x in enumerate(r["c"]):
        sub = x.split("\n")
        p = fmt(take(), after=1, before=(1 if i == 0 else 0), left=10, hanging=4, keep=True, keep_next=(i < 4 or len(sub) > 1))
        add_runs(p, C5[i] + NBSP + sub[0], 10.5)
        for j, s_ in enumerate(sub[1:]): fmt(take(), s_, 10.5, after=1, left=10, keep_next=(i < 4 or j < len(sub) - 2))

def answer_table(doc, pairs, per_row=10, num_h=6.5, ans_h=9):
    """정답표(교사용)와 답안지(학생용) 공용. 번호 줄(음영) 아래 답 줄, 한 줄에 10문항.
    답이 None이면 빈 칸(학생이 쓰는 칸). 칸 폭·줄 높이가 같아 두 장을 나란히 놓고 채점할 수 있다."""
    chunks = [pairs[i:i + per_row] for i in range(0, len(pairs), per_row)]
    t = doc.add_table(rows=len(chunks) * 2, cols=per_row); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for ci, ch in enumerate(chunks):
        ra, rb = t.rows[2 * ci], t.rows[2 * ci + 1]
        ra.height = Mm(num_h); rb.height = Mm(ans_h); ra.height_rule = rb.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
        for j in range(per_row):
            a, b = ra.cells[j], rb.cells[j]
            a.vertical_alignment = b.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            cell_fill(a, "F2F2F2")
            if j < len(ch):
                n, ans = ch[j]
                cell_text(a, str(n), 10, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=0)
                cell_text(b, C5[int(ans) - 1] if ans is not None else "", 11, align=WD_ALIGN_PARAGRAPH.CENTER, after=0)
    tbl_widths(t, [180 / per_row] * per_row)
    return t

def explain(doc, text):
    lines = [l for l in text.split("\n") if l.strip()]
    i = 0
    while i < len(lines):
        l = lines[i]
        lab = next((x for x in LABELS if l.startswith(x)), None)
        if lab:
            body = l[len(lab):].strip()
            if lab == "문장별 판정:" and not body:
                nxt = [m for m in lines[i + 1:i + 2]]
                if not nxt or any(nxt[0].startswith(x) for x in LABELS): i += 1; continue
            p = para(doc, after=1, left=4, hanging=4, line=1.15)
            add_runs(p, lab + " ", 10, bold=True, color="1F3A5F")
            if body: add_runs(p, body, 10)
        elif re.match(r"^[①-⑤] \[", l):
            p = para(doc, after=1, left=8, hanging=4, line=1.15); add_runs(p, l, 10)
        else:
            p = para(doc, after=1, left=8, line=1.15); add_runs(p, l, 10)
        i += 1

def build(g, kind="A"):
    ref = SRC[kind]; fn, tag, desc = NAME[kind]
    chs = idx["grades"][str(g)]; nos = [n for c in chs for n in c["nos"]]
    total = len(nos)
    # ---------- 학생용 시험지 ----------
    doc = Document(); sec = setup(doc, True); set_cols(sec, 1)
    footer_pagenum(sec, f"TOEG {g}급 문법 평가{tag}")
    p = para(doc, f"TOEG {g}급 문법 평가{tag}", 18, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=2)
    p = para(doc, f"{desc} {total}문항 · 객관식(5지선다)", 10, align=WD_ALIGN_PARAGRAPH.CENTER, after=6, color="555555")
    t = doc.add_table(rows=1, cols=4); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for c, (lab, w) in zip(t.rows[0].cells, (("학년/반", 40), ("이름", 50), ("날짜", 40), ("점수", 50))):
        cell_text(c, lab + ":  ", 10.5, bold=True, after=0)
    tbl_widths(t, [40, 50, 40, 50]); t.rows[0].height = Mm(10)
    para(doc, "※ 각 문항에서 가장 알맞은 것을 하나만 골라 답안지에 번호를 쓰시오.", 9.5, after=4, before=4, color="333333")
    sec2 = doc.add_section(WD_SECTION.CONTINUOUS); set_cols(sec2, 2)
    tiny(doc.add_paragraph(), 2)  # 2단 구역은 문단으로 시작해야 한다(한글은 표로 시작하면 첫 표 뒤에서 단을 나눈다)
    col_mm = 85  # 단 폭 (180 - 9) / 2 = 85.5mm
    for c in chs:
        head = f"{c['ch']}  {c['chn']}   ({c['nos'][0]}~{c['nos'][-1]}번)"
        for k, n in enumerate(c["nos"]):
            add_item(doc, n, ref[f"{g}-{n}"], col_mm, heading=head if k == 0 else None)
            tiny(doc.add_paragraph(), 3)  # 표와 표 사이(워드는 사이에 문단이 없으면 표를 합친다)
    sec3 = doc.add_section(WD_SECTION.NEW_PAGE); set_cols(sec3, 1)
    para(doc, f"TOEG {g}급 문법 평가{tag}  답안지", 15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=4)
    t = doc.add_table(rows=1, cols=3); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for c, (lab, w) in zip(t.rows[0].cells, (("학년/반", 50), ("이름", 70), ("점수", 60))):
        cell_text(c, lab + ":  ", 10.5, bold=True, after=0)
    tbl_widths(t, [50, 70, 60]); t.rows[0].height = Mm(10)
    para(doc, "문항 번호 아래 칸에 정답 번호(①~⑤)를 쓰시오.", 9.5, after=4, before=4, color="333333")
    answer_table(doc, [(n, None) for n in nos])
    f1 = OUT / f"TOEG_{g}급_{fn}_시험지.docx"; doc.save(f1)
    # ---------- 정답·해설 ----------
    doc = Document(); sec = setup(doc, False); set_cols(sec, 1)
    footer_pagenum(sec, f"TOEG {g}급 문법 평가{tag} · 정답 및 해설")
    para(doc, f"TOEG {g}급 문법 평가{tag}  정답 및 해설", 18, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=2)
    para(doc, f"{desc} {total}문항 · 교사용", 10, align=WD_ALIGN_PARAGRAPH.CENTER, after=8, color="555555")
    h = para(doc, "정답표", 12, bold=True, after=3, before=2); shade(h, "E8EEF7")
    answer_table(doc, [(n, ref[f"{g}-{n}"]["ans"]) for n in nos])
    para(doc, "", after=6)
    h = para(doc, "문항별 해설", 12, bold=True, after=3, before=6); shade(h, "E8EEF7")
    for c in chs:
        para(doc, f"{c['ch']}  {c['chn']}", 11, bold=True, after=2, before=8, keep_next=True, color="1F3A5F")
        for n in c["nos"]:
            r = ref[f"{g}-{n}"]
            p = para(doc, keep_next=True, after=1, before=5)
            add_runs(p, f"{n}.  정답 {C5[int(r['ans']) - 1]}", 11, bold=True)
            add_runs(p, "   " + r["stem"], 9.5, color="666666")
            explain(doc, r["expl"])
    f2 = OUT / f"TOEG_{g}급_{fn}_정답해설.docx"; doc.save(f2)
    return f1, f2, total

if __name__ == "__main__":
    args = sys.argv[1:]; kinds = ["A"]
    if args and args[0].upper() in ("A", "B", "ALL"): kinds = ["A", "B"] if args[0].upper() == "ALL" else [args[0].upper()]; args = args[1:]
    gs = [int(x) for x in args] or [1, 2, 3, 4, 5, 6, 7]
    for kind in kinds:
        for g in gs:
            f1, f2, total = build(g, kind); print(f"{kind} {g}급 {total}문항 → {f1.name}, {f2.name}")
