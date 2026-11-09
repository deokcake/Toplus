#!/usr/bin/env node
/**
 * exam-worksheet JSON → 편집 가능한 Word 문서(.docx) 두 개 (문제지, 정답·해설지).
 *
 *   node tools/scripts/make_docx.js TheReading_7-1_FinalTest.json [출력폴더]
 *
 * 마크업: ⟪word⟫ = 밑줄, *text* = 굵게, ______ = 빈칸, 상자(box) 안의 "\\\n" = 줄바꿈.
 */
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, BorderStyle,
  ShadingType, AlignmentType, LineRuleType, PositionalTab, PositionalTabAlignment, PositionalTabRelativeTo,
  PositionalTabLeader, UnderlineType, Footer, PageNumber, VerticalAlign,
} = require("docx");

const src = process.argv[2];
const outDir = process.argv[3] || path.dirname(src);
const data = JSON.parse(fs.readFileSync(src, "utf8"));

// ── 치수(DXA, 1440 = 1inch). A4 세로, 좌우 18mm, 상하 15mm
const PAGE_W = 11906, PAGE_H = 16838, M_X = 1020, M_Y = 850;
const TEXT_W = PAGE_W - 2 * M_X;           // 9866
const ACCENT = "1F3A5F", SOFT = "EEF2F7", MUTED = "555555", KEYRED = "B3261E", RULE = "999999";
const CIRCLED = ["①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨", "⑩"];
const FONT = { ascii: "Times New Roman", hAnsi: "Times New Roman", eastAsia: "Malgun Gothic", cs: "Times New Roman" };
const KFONT = { ascii: "Malgun Gothic", hAnsi: "Malgun Gothic", eastAsia: "Malgun Gothic", cs: "Malgun Gothic" };

const NOBORDER = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: NOBORDER, bottom: NOBORDER, left: NOBORDER, right: NOBORDER, insideHorizontal: NOBORDER, insideVertical: NOBORDER };
const thin = { style: BorderStyle.SINGLE, size: 4, color: RULE };
const allThin = { top: thin, bottom: thin, left: thin, right: thin, insideHorizontal: thin, insideVertical: thin };

// ── 인라인 마크업 → TextRun[]
function runs(text, base = {}) {
  const out = [];
  const re = /⟪(.+?)⟫|\*(.+?)\*|(_{3,})/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    if (m[1] !== undefined) out.push(new TextRun({ text: m[1], underline: { type: UnderlineType.SINGLE }, ...base }));
    else if (m[2] !== undefined) out.push(new TextRun({ text: m[2], bold: true, ...base }));
    else out.push(new TextRun({ text: "________", ...base }));
    last = m.index + m[0].length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out;
}
const para = (text, opts = {}, base = {}) => new Paragraph({ children: runs(text, base), ...opts });
// 표와 표 사이를 띄우는 아주 낮은 빈 문단 (붙어 있는 두 표가 하나로 합쳐지는 것을 막는다)
const spacer = (h = 80) => new Paragraph({ spacing: { before: 0, after: 0, line: h, lineRule: LineRuleType.EXACT }, children: [] });
const visWidth = (s) => [...s].reduce((n, ch) => n + (ch.codePointAt(0) > 0x2e80 ? 2 : 1), 0);

// ── 공통 조각
function header(mode) {
  const meta = data.meta || {};
  const bits = ["subject", "grade", "unit", "time_limit"].filter((k) => meta[k]).map((k) => meta[k]);
  const out = [
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { after: 40 },
      children: [
        new TextRun({ text: data.title, bold: true, size: 36, color: ACCENT }),
        ...(mode === "key" ? [new TextRun({ text: "  (정답 · 해설)", bold: true, size: 24, color: KEYRED, font: KFONT })] : []),
      ],
    }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 80 }, children: [new TextRun({ text: bits.join("   ·   "), size: 19, color: MUTED })] }),
  ];
  if (mode === "student" && (data.student_fields || []).length) {
    out.push(new Paragraph({
      alignment: AlignmentType.RIGHT, spacing: { after: 60 },
      children: data.student_fields.flatMap((f) => [new TextRun({ text: `${f} `, size: 20 }), new TextRun({ text: "______________", size: 20 }), new TextRun({ text: "    ", size: 20 })]),
    }));
  }
  out.push(new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: ACCENT, space: 1 } }, spacing: { after: 100 }, children: [] }));
  if (mode === "student" && (data.instructions || []).length) {
    out.push(new Paragraph({
      shading: { type: ShadingType.CLEAR, fill: SOFT }, spacing: { before: 40, after: 120, line: 280 },
      indent: { left: 120, right: 120 },
      children: data.instructions.flatMap((t, i) => [...(i ? [new TextRun({ break: 1 })] : []), new TextRun({ text: "• ", color: MUTED, size: 19 }), ...runs(t, { size: 19, color: MUTED })]),
    }));
  }
  return out;
}

function sectionHeading(title, first) {
  return new Paragraph({
    pageBreakBefore: !first,
    shading: { type: ShadingType.CLEAR, fill: SOFT }, spacing: { before: first ? 80 : 0, after: 100 },
    indent: { left: 120 }, keepNext: true,
    children: [new TextRun({ text: title, bold: true, size: 24, color: ACCENT })],
  });
}

function cell(children, width, opts = {}) {
  return new TableCell({ width: { size: width, type: WidthType.DXA }, margins: { top: 60, bottom: 60, left: 100, right: 100 }, verticalAlign: VerticalAlign.TOP, children, ...opts });
}
function layoutTable(cellsPerRow, items, mk) {
  const colW = Math.floor(TEXT_W / cellsPerRow);
  const widths = Array(cellsPerRow).fill(colW);
  const rows = [];
  for (let i = 0; i < items.length; i += cellsPerRow) {
    const slice = items.slice(i, i + cellsPerRow);
    while (slice.length < cellsPerRow) slice.push(null);
    rows.push(new TableRow({ children: slice.map((it) => cell(it === null ? [new Paragraph({})] : mk(it), colW, { borders: noBorders })) }));
  }
  return new Table({ width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: widths, borders: noBorders, rows });
}

// ── 지문 상자(왼쪽 굵은 선 + 옅은 배경)
function passageBlock(it) {
  const paras = [];
  if (it.title) paras.push(new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: it.title, bold: true, size: 20 })] }));
  for (const p of it.text.split(/\n\s*\n/)) paras.push(new Paragraph({ spacing: { after: 70, line: 270 }, children: runs(p.replace(/\s*\n\s*/g, " "), { size: 20 }) }));
  if (it.note) paras.push(new Paragraph({ spacing: { before: 40, after: 0, line: 240 }, children: runs(it.note, { size: 16, color: MUTED }) }));
  const accent = { style: BorderStyle.SINGLE, size: 18, color: ACCENT };
  return new Table({
    width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: [TEXT_W], borders: noBorders,
    rows: [new TableRow({ children: [cell(paras, TEXT_W, { borders: { top: NOBORDER, bottom: NOBORDER, right: NOBORDER, left: accent }, shading: { type: ShadingType.CLEAR, fill: "FAFAFA" }, margins: { top: 80, bottom: 80, left: 200, right: 160 } })] })],
  });
}

// ── 문제지 문항
function questionBlock(it, qno, showPoints) {
  const out = [];
  const [first, ...rest] = (it.prompt || "").split(/\n\s*\n/);
  const head = new Paragraph({
    spacing: { before: 130, after: 40 }, keepNext: true,
    indent: { left: 440, hanging: 440 },
    tabStops: [{ type: "right", position: TEXT_W }],
    children: [
      new TextRun({ text: `${qno}. `, bold: true, color: ACCENT }),
      ...runs(first),
      ...(showPoints && it.points !== undefined ? [new TextRun({ children: [new PositionalTab({ alignment: PositionalTabAlignment.RIGHT, relativeTo: PositionalTabRelativeTo.MARGIN, leader: PositionalTabLeader.NONE }), `[${it.points} pts]`], size: 17, color: MUTED })] : []),
    ],
  });
  out.push(head);
  for (const p of rest) out.push(new Paragraph({ indent: { left: 440 }, spacing: { after: 40, line: 270 }, keepNext: true, children: runs(p) }));
  if (it.box) {
    const lines = it.box.split(/\\\n|\n/).map((s) => s.replace(/\\\s*$/, "").trim()).filter(Boolean);
    out.push(new Table({
      width: { size: TEXT_W - 440, type: WidthType.DXA }, columnWidths: [TEXT_W - 440], indent: { size: 440, type: WidthType.DXA }, borders: allThin,
      rows: [new TableRow({ children: [cell(lines.map((l) => new Paragraph({ spacing: { after: 40 }, children: runs(l) })), TEXT_W - 440, { borders: allThin })] })],
    }));
    out.push(spacer());
  }
  if (it.table) {
    const ncol = it.table[0].length;
    const widths = ncol === 2 ? [1700, 4600] : [1500, 2600, 2600];
    const total = widths.reduce((a, b) => a + b, 0);
    out.push(new Table({
      width: { size: total, type: WidthType.DXA }, columnWidths: widths, indent: { size: 440, type: WidthType.DXA }, borders: allThin,
      rows: it.table.map((row) => new TableRow({ children: row.map((c, i) => cell([new Paragraph({ children: runs(c) })], widths[i], { borders: allThin })) })),
    }));
    out.push(spacer());
  }
  if (it.type === "multiple_choice") {
    const choices = it.choices.map((c, i) => `${CIRCLED[i]} ${c}`);
    const m = Math.max(...it.choices.map(visWidth));
    const ncol = m <= 14 ? 5 : m <= 44 ? 2 : 1;
    if (ncol === 1) choices.forEach((c) => out.push(new Paragraph({ indent: { left: 440 }, spacing: { after: 20 }, children: runs(c) })));
    else {
      out.push(new Table({
        width: { size: TEXT_W - 440, type: WidthType.DXA }, indent: { size: 440, type: WidthType.DXA },
        columnWidths: Array(ncol).fill(Math.floor((TEXT_W - 440) / ncol)), borders: noBorders,
        rows: (() => {
          const rows = [];
          for (let i = 0; i < choices.length; i += ncol) {
            const slice = choices.slice(i, i + ncol); while (slice.length < ncol) slice.push("");
            rows.push(new TableRow({ children: slice.map((c) => cell([new Paragraph({ spacing: { after: 0 }, children: runs(c) })], Math.floor((TEXT_W - 440) / ncol), { borders: noBorders, margins: { top: 10, bottom: 10, left: 40, right: 40 } })) }));
          }
          return rows;
        })(),
      }));
    }
  }
  return out;
}

// ── 정답지: 채점표 + 문항별 정답·해설
function answerGrid(all) {
  const out = [];
  const per = 10, colW = Math.floor(TEXT_W / per);
  for (let r = 0; r < all.length; r += per) {
    const slice = all.slice(r, r + per);
    const nums = slice.map((_, i) => new TableCell({ width: { size: colW, type: WidthType.DXA }, borders: allThin, margins: { top: 30, bottom: 30 }, children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: String(r + i + 1), size: 16, color: MUTED })] })] }));
    const ans = slice.map((it) => new TableCell({ width: { size: colW, type: WidthType.DXA }, borders: allThin, margins: { top: 30, bottom: 30 }, children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: typeof it.answer === "number" ? CIRCLED[it.answer - 1] : String(it.answer), bold: true, color: KEYRED, font: KFONT })] })] }));
    out.push(new Table({ width: { size: colW * slice.length, type: WidthType.DXA }, columnWidths: Array(slice.length).fill(colW), borders: allThin, rows: [new TableRow({ children: nums }), new TableRow({ children: ans })] }));
    out.push(new Paragraph({ spacing: { after: 60 }, children: [] }));
  }
  return out;
}
function keyItem(it, qno) {
  const ans = typeof it.answer === "number" ? CIRCLED[it.answer - 1] : String(it.answer);
  const out = [new Paragraph({
    spacing: { before: 160, after: 40 }, keepNext: true, indent: { left: 440, hanging: 440 },
    children: [new TextRun({ text: `${qno}. `, bold: true, color: ACCENT }), new TextRun({ text: `정답: ${ans}`, bold: true, color: KEYRED, font: KFONT })],
  })];
  if (it.explanation) out.push(new Paragraph({ indent: { left: 440 }, spacing: { after: 40, line: 280 }, children: [new TextRun({ text: "해설  ", size: 19, color: MUTED, font: KFONT }), ...runs(it.explanation, { size: 19, color: MUTED, font: KFONT })] }));
  return out;
}

function build(mode) {
  const children = [...header(mode)];
  let qno = 0;
  const allItems = [];
  data.sections.forEach((sec, si) => {
    children.push(sectionHeading(sec.title, si === 0 || mode === "key"));
    for (const it of sec.items) {
      if (it.type === "passage") { if (mode === "student") { children.push(passageBlock(it)); children.push(spacer(100)); } continue; }
      qno += 1; allItems.push(it);
      if (mode === "student") children.push(...questionBlock(it, qno, (data.layout || {}).show_points !== false));
      else children.push(...keyItem(it, qno));
    }
  });
  if (mode === "key") children.splice(header("key").length, 0, ...answerGrid(allItems));
  return new Document({
    creator: "TOPLUS", title: data.title + (mode === "key" ? " (정답·해설)" : ""),
    styles: { default: { document: { run: { font: FONT, size: 21 }, paragraph: { spacing: { after: 60 } } } } },
    sections: [{
      properties: { page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: M_Y, bottom: M_Y, left: M_X, right: M_X } } },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT, " / ", PageNumber.TOTAL_PAGES], size: 18, color: MUTED })] })] }) },
      children,
    }],
  });
}

(async () => {
  const stem = data.title.replace(/[^\w가-힣 \-]/g, "").trim().replace(/\s+/g, "_");
  for (const [mode, suffix] of [["student", "문제지"], ["key", "정답해설"]]) {
    const buf = await Packer.toBuffer(build(mode));
    const out = path.join(outDir, `${stem}_${suffix}.docx`);
    fs.writeFileSync(out, buf);
    console.log(out);
  }
})();
