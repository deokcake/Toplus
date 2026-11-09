// ─────────────────────────────────────────────
//  시험지 · 학습지 공용 레이아웃 템플릿
//  render.py 가 만든 data.json 을 받아 PDF 로 조판한다.
//  이 파일은 "형식"만 담당한다. 내용은 절대 여기 쓰지 않는다.
// ─────────────────────────────────────────────

#let CJK = "Noto Sans CJK KR"
#let circled = ("①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨", "⑩")
#let qc = counter("q")

#let ACCENT = rgb("#1f3a5f")
#let SOFT = rgb("#eef2f7")
#let MUTED = rgb("#555555")
#let KEYRED = rgb("#b3261e")

// 문자열을 Typst 마크업으로 해석 (render.py 에서 이미 안전하게 이스케이프됨)
#let mk(s) = eval(s, mode: "markup")

#let blank(w) = box(width: w, baseline: 0.15em, line(length: 100%, stroke: 0.6pt))

// ── 상단 머리말 ──────────────────────────────
#let doc-header(data, mode) = {
  let meta = data.at("meta", default: (:))
  block(width: 100%, {
    align(center, {
      text(size: 17pt, weight: "bold", fill: ACCENT)[#data.at("title", default: "")]
      if mode == "key" {
        text(size: 12pt, weight: "bold", fill: KEYRED)[ (정답 · 해설)]
      }
    })
    v(0.35em)
    let bits = ()
    for k in ("subject", "grade", "unit", "date", "time_limit") {
      if k in meta { bits.push(meta.at(k)) }
    }
    if bits.len() > 0 {
      align(center, text(size: 9.5pt, fill: MUTED)[#bits.join("   ·   ")])
    }
    v(0.5em)
    let fields = data.at("student_fields", default: ())
    if fields.len() > 0 and mode == "student" {
      align(right, text(size: 10pt)[
        #for f in fields [#f #blank(4.5em) #h(0.8em)]
      ])
      v(0.2em)
    }
    line(length: 100%, stroke: 1.2pt + ACCENT)
  })
}

// ── 유의사항 상자 ────────────────────────────
#let notice(items) = {
  if items.len() == 0 { return }
  block(
    width: 100%, fill: SOFT, inset: (x: 9pt, y: 7pt), radius: 3pt,
    above: 0.8em, below: 1em,
    text(size: 9.5pt, fill: MUTED)[
      #for it in items [• #mk(it) \ ]
    ],
  )
}

// ── 보기(선택지) ─────────────────────────────
// 표시 폭 추정: 한글·한자 등 전각 문자는 2, 그 외는 1
#let vis-width(s) = s.codepoints().map(ch => if str.to-unicode(ch) > 0x2E80 { 2 } else { 1 }).sum(default: 0)

#let render-choices(choices, cols) = {
  let n = if cols == 0 {
    let m = choices.map(vis-width).fold(0, calc.max)
    if m <= 14 { 5 } else if m <= 44 { 2 } else { 1 }
  } else { cols }
  pad(left: 1.1em, top: 0.45em, grid(
    columns: n,
    column-gutter: 1.2em,
    row-gutter: 0.5em,
    ..choices.enumerate().map(p => [#circled.at(p.at(0)) #mk(p.at(1))]),
  ))
}

#let answer-lines(n) = {
  pad(left: 1.1em, top: 0.5em, {
    for _ in range(n) {
      v(1.7em)
      line(length: 100%, stroke: 0.5pt + luma(160))
    }
  })
}

#let work-box(h) = pad(left: 1.1em, top: 0.5em,
  rect(width: 100%, height: h, stroke: 0.5pt + luma(180), radius: 3pt))

// ── 문항 (문제지 모드) ───────────────────────
#let render-item(it, opts) = {
  let type = it.at("type", default: "short_answer")

  // 지문·설명 블록: 번호를 매기지 않는다
  if type == "passage" {
    block(width: 100%, breakable: true, above: 0.9em, below: 0.7em,
      block(width: 100%, stroke: (left: 2pt + ACCENT), inset: (x: 10pt, y: 6pt),
        fill: luma(250), {
          if "title" in it { text(weight: "bold", size: 10pt)[#mk(it.title)]; v(0.3em) }
          mk(it.at("text", default: ""))
          if "note" in it { v(0.25em); text(size: 8pt, fill: MUTED)[#mk(it.note)] }
        }))
    return
  }

  qc.step()
  block(width: 100%, breakable: false, above: 0.75em, below: 0.2em, {
    grid(
      columns: (auto, 1fr, auto),
      column-gutter: 0.45em,
      align: (top, top, top),
      text(weight: "bold", fill: ACCENT)[#context qc.display().],
      mk(it.at("prompt", default: "")),
      if opts.show_points and "points" in it {
        text(size: 8.5pt, fill: MUTED)[[#it.points pts]]
      } else { [] },
    )

    if "box" in it {
      pad(left: 1.1em, top: 0.4em, block(width: 100%, stroke: 0.5pt + luma(150),
        inset: (x: 8pt, y: 5pt), radius: 3pt, mk(it.box)))
    }
    if "table" in it {
      let rows = it.table
      pad(left: 1.1em, top: 0.45em, table(
        columns: rows.at(0).len(), stroke: 0.5pt + luma(150), inset: 5pt,
        ..rows.flatten().map(c => mk(c))))
    }

    if type == "multiple_choice" {
      render-choices(it.at("choices", default: ()), opts.choice_columns)
    } else if type == "true_false" {
      render-choices(("참", "거짓"), 4)
    } else if type == "matching" {
      pad(left: 1.1em, top: 0.5em, grid(
        columns: (1fr, 1fr), column-gutter: 2.5em,
        stack(spacing: 0.7em, ..it.at("left", default: ()).enumerate().map(p =>
          [(#numbering("1", p.at(0) + 1)) #mk(p.at(1)) #h(1fr) ·])),
        stack(spacing: 0.7em, ..it.at("right", default: ()).enumerate().map(p =>
          [· #h(0.6em) (#numbering("가", p.at(0) + 1)) #mk(p.at(1))])),
      ))
    } else if type == "essay" {
      if "answer_lines" in it { answer-lines(it.answer_lines) }
      else if "work_space" not in it { answer-lines(5) }
    } else if type == "short_answer" {
      if "answer_lines" in it { answer-lines(it.answer_lines) }
    }

    if "work_space" in it { work-box(it.work_space * 1mm) }
  })
}

// ── 문항 (정답·해설 모드) ────────────────────
#let render-key-item(it) = {
  if it.at("type", default: "") == "passage" { return }
  qc.step()
  let ans = if "answer" in it {
    let a = it.answer
    if type(a) == int { circled.at(a - 1) }
    else if type(a) == array { a.map(x => str(x)).join(", ") }
    else { mk(str(a)) }
  } else { text(fill: MUTED)[—] }

  block(width: 100%, breakable: false, above: 0.55em, {
    grid(
      columns: (2.2em, 1fr),
      align: (right + top, left + top),
      column-gutter: 0.5em,
      text(weight: "bold", fill: ACCENT)[#context qc.display().],
      {
        text(weight: "bold", fill: KEYRED)[정답: #ans]
        if "explanation" in it {
          v(0.15em)
          text(size: 9.5pt, fill: MUTED)[해설  #mk(it.explanation)]
        }
      },
    )
  })
}

// ── 정답지 상단 채점표 ───────────────────────
#let grid-table(items) = {
  let per = 10
  let n = items.len()
  for r in range(calc.ceil(n / per)) {
    let cells = ()
    let acells = ()
    for i in range(r * per, calc.min(n, (r + 1) * per)) {
      cells.push(text(size: 8pt, fill: MUTED)[#(i + 1)])
      let a = items.at(i).at("answer", default: none)
      acells.push(text(weight: "bold", fill: KEYRED)[#if type(a) == int { circled.at(a - 1) } else { str(a) }])
    }
    table(columns: per, align: center, inset: 3.5pt, stroke: 0.4pt + luma(170), ..cells, ..acells)
    v(0.25em)
  }
}

#let answer-grid(data, per-section: false) = {
  block(width: 100%, above: 0.6em, below: 0.3em, {
    if per-section {
      grid(columns: (1fr, 1fr), column-gutter: 1.2em, row-gutter: 0.5em,
        ..data.at("sections", default: ()).map(sec => {
          let items = sec.at("items", default: ()).filter(it => it.at("type", default: "") != "passage")
          block(width: 100%, {
            text(size: 8.5pt, weight: "bold", fill: ACCENT)[#mk(sec.at("title", default: ""))]
            v(0.15em)
            grid-table(items)
          })
        }))
    } else {
      let all = ()
      for sec in data.at("sections", default: ()) {
        for it in sec.at("items", default: ()) {
          if it.at("type", default: "") != "passage" { all.push(it) }
        }
      }
      grid-table(all)
    }
  })
}

// ── 섹션 ─────────────────────────────────────
#let render-section(sec, mode, opts, first: false) = {
  let broke = opts.section_pagebreak and mode == "student" and not first
  if broke { pagebreak() }
  if opts.number_per_section { qc.update(0) }
  if "title" in sec {
    block(width: 100%, above: if broke or first { 0.6em } else { 1.3em }, below: 0.5em,
      block(width: 100%, fill: SOFT, inset: (x: 8pt, y: 6pt), radius: 3pt,
        text(weight: "bold", size: 11.5pt, fill: ACCENT)[#mk(sec.title)]))
  }
  if "description" in sec and mode == "student" {
    block(below: 0.5em, text(size: 9.5pt, fill: MUTED)[#mk(sec.description)])
  }
  for it in sec.at("items", default: ()) {
    if mode == "key" { render-key-item(it) } else { render-item(it, opts) }
  }
}

// ── 진입점 ───────────────────────────────────
#let exam(data, mode: "student") = {
  let layout = data.at("layout", default: (:))
  let opts = (
    show_points: layout.at("show_points", default: true),
    choice_columns: layout.at("choice_columns", default: 0),
    section_pagebreak: layout.at("section_pagebreak", default: false),
    number_per_section: layout.at("number_per_section", default: false),
  )

  set text(font: CJK, size: layout.at("font_size", default: 10.5) * 1pt, lang: "ko")
  set par(justify: false, leading: 0.72em)
  set page(
    paper: layout.at("paper", default: "a4"),
    margin: (x: 16mm, y: 13mm),
    numbering: "1 / 1",
    columns: if mode == "key" { 2 } else { layout.at("columns", default: 1) },
  )
  show heading: set text(font: CJK)

  place(top, scope: "parent", float: true, {
    doc-header(data, mode)
    if mode == "student" { notice(data.at("instructions", default: ())) }
    if mode == "key" { answer-grid(data, per-section: opts.number_per_section) }
    v(0.2em)
  })

  qc.update(0)
  for (i, sec) in data.at("sections", default: ()).enumerate() {
    render-section(sec, mode, opts, first: i == 0)
  }
}
