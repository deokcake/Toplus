#!/usr/bin/env python3
"""최종 판정을 원본 엑셀 5개(B~F)에 감수 열로 붙이고, 요약 엑셀을 만든다.

    python3 export.py   →  결과/ 폴더
"""
import json
import os
import re
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/grammar-item-review/scripts"))
import assemble  # noqa: E402
import make_xlsx  # noqa: E402

OUT = HERE / "결과"
DL = Path(os.path.expanduser("~/Downloads"))
OK, FXP, FXC, BAD = assemble.OK, assemble.FXP, assemble.FXC, assemble.BAD
ORDER = [OK, FXP, FXC, BAD]
TYPES = "BCDEF"


# ---------- 자동 점검 문구를 사람이 읽는 말로 ----------
def plain_flag(code, msg):
    msg = re.sub(r"\s*\(원: .*$", "", msg)
    if "밑줄 제시가" in msg:
        return "원문항의 밑줄이 사라짐", "밑줄 복원"
    if code == "C3" and "기호" in msg:
        return msg, "보기 기호(ⓐ 등)와 줄바꿈 복원"
    if code == "C3" and "줄바꿈" in msg:
        return "본문 줄바꿈이 사라짐", "줄바꿈 복원"
    if "개수 선택지가" in msg:
        return msg, "개수 선택지를 1개→5개 순으로"
    if "선택지 형태 변경" in msg:
        return msg, "선택지 형태를 원문항과 같게"
    if "보기 문장 수" in msg:
        return msg, "보기 문장 수를 원문항과 같게"
    if code == "A3" and "제시문" in msg:
        return msg, "제시 방식을 원문항과 같게"
    if "발문 과제 변경" in msg or "발문 문구 변경" in msg:
        return "발문이 원문항과 다름", "발문을 원문항과 같게"
    if "발문에 조건 추가" in msg:
        return msg, "발문 조건 삭제"
    return msg, ""


def auto_text(r):
    seen, out = set(), []
    for f in r["flags"]:
        code, sev, msg = f["code"], f["sev"], f["msg"]
        if code == "C2":
            continue
        if code == "A1" and sev == "note" and "조건 추가" not in msg and "문구 변경" not in msg:
            continue
        if code == "A2" and sev == "note":
            continue
        t, _ = plain_flag(code, msg)
        if t not in seen:
            seen.add(t)
            out.append(t)
    return " / ".join(out)


FIX_KEYS = {"밑줄 복원": "밑줄", "줄바꿈 복원": "줄바꿈", "보기 기호(ⓐ 등)와 줄바꿈 복원": "기호",
            "개수 선택지를 1개→5개 순으로": "정렬|순으로", "선택지 형태를 원문항과 같게": "선택지 형태|원본 형식",
            "보기 문장 수를 원문항과 같게": "문장 수|네 문장|다섯 문장", "제시 방식을 원문항과 같게": "제시|원본 형식",
            "발문을 원문항과 같게": "발문", "발문 조건 삭제": "발문"}


def compose(o):
    reason, fix = o["reason"].strip(), o["fix"].strip()
    if o["final"] != o["manual"]:
        diffs, fixes = [], []
        for _kind, code, msg in o["auto_why"]:
            t, fx = plain_flag(code, msg)
            if t not in diffs:
                diffs.append(t)
            if fx and fx not in fixes and not re.search(FIX_KEYS.get(fx, "^$"), fix):
                fixes.append(fx)
        reason += " 다만 원본 형식과 다르다: " + ", ".join(diffs) + "."
        fix = ", ".join(x for x in [fix] + fixes if x)
    return reason, fix


# ---------- 원본 엑셀에 열 붙이기 ----------
NEW_HEAD = ["감수 판정", "판정 근거", "수정 제안", "자동 점검(원본 형식·노출)", "원문항 확인 사항"]
FILLS = ["FFDDF0E1", "FFFFF1CC", "FFFCE0C4", "FFF8CFCB"]  # 적합·표기·내용·부적합


def cell_style(sh, ref):
    m = re.search(r'<c r="%s"[^>]*?s="(\d+)"' % ref, sh)
    return int(m.group(1)) if m else 0


def clone_xf(xf, fill=None, halign="center"):
    """원본 셀 서식(xf)을 복제하되 채우기·정렬만 바꾼다(글꼴·테두리는 원본 그대로)."""
    head = re.match(r"<xf [^>]*?(?=/?>)", xf).group(0)
    if fill is not None:
        head = re.sub(r'fillId="\d+"', f'fillId="{fill}"', head)
        if "applyFill" not in head:
            head += ' applyFill="1"'
    if "applyAlignment" not in head:
        head += ' applyAlignment="1"'
    return f'{head}><alignment horizontal="{halign}" vertical="center" wrapText="1"/></xf>'


def patch_styles(st, sh):
    """이 통합 문서의 서식표에 감수 열 서식 5개(본문 1 + 판정 4)를 덧붙인다."""
    fills = re.search(r'<fills count="(\d+)">(.*?)</fills>', st, re.S)
    nf = int(fills.group(1))
    add = "".join(f'<fill><patternFill patternType="solid"><fgColor rgb="{c}"/><bgColor indexed="64"/></patternFill></fill>' for c in FILLS)
    st = st.replace(fills.group(0), f'<fills count="{nf + 4}">{fills.group(2)}{add}</fills>')
    xfs_m = re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>', st, re.S)
    nx = int(xfs_m.group(1))
    xfs = re.findall(r"<xf [^>]*?(?:/>|>.*?</xf>)", xfs_m.group(2), re.S)
    assert len(xfs) == nx
    base = xfs[cell_style(sh, "I2")]
    new = clone_xf(base, halign="left") + "".join(clone_xf(base, fill=nf + i) for i in range(4))
    st = st.replace(xfs_m.group(0), f'<cellXfs count="{nx + 5}">{xfs_m.group(2)}{new}</cellXfs>')
    return st, nx, {v: nx + 1 + i for i, v in enumerate(ORDER)}, cell_style(sh, "I1")


def cell(ref, text, s):
    return f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{escape(str(text))}</t></is></c>'


def export_type(t, info_by_row):
    src = next(p for p in DL.iterdir() if p.name.startswith(f"{t} type") and p.suffix == ".xlsx")
    zin = zipfile.ZipFile(src)
    sh = zin.read("xl/worksheets/sheet1.xml").decode("utf-8")
    st, text_s, vs, head_s = patch_styles(zin.read("xl/styles.xml").decode("utf-8"), sh)
    sh = re.sub(r'<dimension ref="A1:Q(\d+)"/>', r'<dimension ref="A1:V\1"/>', sh)
    colm = re.search(r'<col min="18" max="16384" width="9" style="(\d+)"/>', sh)
    cs = colm.group(1)
    sh = sh.replace(colm.group(0),
                    f'<col min="18" max="18" width="12" style="{cs}" customWidth="1"/>'
                    f'<col min="19" max="19" width="70" style="{cs}" customWidth="1"/>'
                    f'<col min="20" max="20" width="45" style="{cs}" customWidth="1"/>'
                    f'<col min="21" max="21" width="45" style="{cs}" customWidth="1"/>'
                    f'<col min="22" max="22" width="35" style="{cs}" customWidth="1"/>'
                    f'<col min="23" max="16384" width="9" style="{cs}"/>')

    def fix_row(m):
        head, rn, body = m.group(1), int(m.group(2)), m.group(3)
        head = head.replace('spans="1:17"', 'spans="1:22"')
        if rn == 1:
            cells = "".join(cell(f"{col}1", h, head_s) for col, h in zip("RSTUV", NEW_HEAD))
        else:
            final, reason, fix, auto, note = info_by_row[rn]
            cells = (cell(f"R{rn}", final, vs[final]) + cell(f"S{rn}", reason, text_s) +
                     cell(f"T{rn}", fix, text_s) + cell(f"U{rn}", auto, text_s) + cell(f"V{rn}", note, text_s))
        return f"{head}{body}{cells}</row>"

    sh, n = re.subn(r'(<row r="(\d+)"[^>]*>)(.*?)</row>', fix_row, sh, flags=re.S)
    assert n == len(info_by_row) + 1, (t, n)
    dst = OUT / f"{t} type 감수결과.xlsx"
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "xl/styles.xml":
                data = st.encode("utf-8")
            elif item.filename == "xl/worksheets/sheet1.xml":
                data = sh.encode("utf-8")
            zout.writestr(item, data)
    return dst


# ---------- 문제 유형 분류(판정 근거 문장에서) ----------
CATS = [
    ("발문·설명이 정답이나 규칙을 알려 줌", r"뜻을 적어 놓아|발문 괄호|발문.{0,200}?(알려|풀어 준|풀어 주|설명해 준|설명해 답|드러난|정답 형식|정답 구조|정답 기준)|발문 조건만으로"),
    ("원문항 문장·정답 재사용", r"원문항.{0,120}?(과|와) (똑같|같|거의 같|사실상 같)|원문항 정답(과| 조합과) (같|똑같)|원문항.{0,150}?그대로|원문항(을| 문장을) 줄인|원문항 정답과 이름|원문항과 [^.]{0,20}같|원문항을 본 학생|원문항.{0,60}?만 다르다|원문항의 (동사|수|말|선택지)[^.]{0,30}?가져와|COPY"),
    ("유형 간 오답 중복", r"유형 간 중복|[B-F]와 (똑)?같|[B-F]와 (선택지|오답)|다른 유형과 같|유형마다 (같|반복)|[B-F]~F에서 (같|반복)|사실상 같은 문항"),
    ("대비(짝) 단서", r"짝을 이|대비 단서|두 번 나와|반대되는|둘 중 하나가 답"),
    ("오답이 뻔하거나 존재하지 않는 형태", r"존재하지 않는 형태|뻔하|뻔히|바로 지워|쉽게 지워|관계없는|변별력|형식만으로 지워|조건만으로 지워|B3"),
    ("정답이 겉모양으로 드러남", r"이름만 보고|표시가 없는|정답에만|정답만[^.]{0,30}(눈에 띈|완전한|구체적)|형식만 보고 고를|형태만 보고|답을 그대로 보여|정답이 드러난|정답만 문맥에 맞|정답뿐|정답 노출|정답이 예측"),
    ("문항 형식·선택지 구조 변경", r"형식으로 바뀌|형식이 바뀌|원본 형식과 다름|A1|A2|A3|A4|B2|C3|인지 과정이 다르|순서가? 뒤섞|틀린 (설명|문장|짝)이 (없|하나도)|원문항\([^)]{0,40}\)과 다르"),
    ("평가 요소가 원문항과 다름(범위 축소 포함)", r"B1|취지가 약해"),
    ("난이도 변화", r"B4"),
    ("영어 표현 오류·부자연스러움", r"C2"),
    ("복수 정답·정답 시비 위험", r"C1"),
]


def categorize(text):
    return [name for name, pat in CATS if re.search(pat, text)]


def main():
    OUT.mkdir(exist_ok=True)
    out, missing, ref_notes = assemble.build()
    assert not missing, missing[:5]
    screen = {r["id"]: r for r in json.load(open(HERE / "src" / "screen.json", encoding="utf-8"))}
    by_key = {(o["type"], o["grade"], o["no"]): o for o in out}

    rows_all = []
    for t in TYPES:
        recs = json.load(open(HERE / "src" / f"{t}.json", encoding="utf-8"))
        info = {}
        for i, r in enumerate(recs):
            g, n = int(r["급수"].replace("급", "")), int(r["문제번호"])
            o = by_key[(t, g, n)]
            reason, fix = compose(o)
            auto = auto_text(screen[o["id"]])
            info[i + 2] = (o["final"], reason, fix, auto, o["ref_note"])
            rows_all.append([t, f"{g}급", n, r["챕터"], r["챕터명"], o["final"], reason, fix, auto, o["ref_note"]])
        print("저장:", export_type(t, info))

    # ---------- 요약 엑셀 ----------
    make_xlsx.VERDICT_STYLE.update({OK: 2, FXP: 3, FXC: 6, BAD: 4})
    make_xlsx.STYLES = make_xlsx.STYLES.replace(
        '<fills count="6">', '<fills count="7">').replace(
        '</fill></fills>', '</fill><fill><patternFill patternType="solid"><fgColor rgb="FFFCE0C4"/></patternFill></fill></fills>').replace(
        '<cellXfs count="6">', '<cellXfs count="7">').replace(
        '</cellXfs>', '<xf fillId="6" borderId="1" fontId="1" applyFill="1" applyBorder="1" applyFont="1" applyAlignment="1">'
                      '<alignment vertical="top" horizontal="center" wrapText="1"/></xf></cellXfs>')

    tot = Counter(o["final"] for o in out)
    by_t = {t: Counter(o["final"] for o in out if o["type"] == t) for t in TYPES}
    by_g = {g: Counter(o["final"] for o in out if o["grade"] == g) for g in range(1, 8)}
    head = ["구분", "적합", "수정(표기)", "수정(내용)", "부적합", "합계"]
    summ = [["전체"] + [tot[v] for v in ORDER] + [sum(tot.values())]]
    summ += [[f"{t} 유형"] + [by_t[t][v] for v in ORDER] + [sum(by_t[t].values())] for t in TYPES]
    summ += [[f"{g}급"] + [by_g[g][v] for v in ORDER] + [sum(by_g[g].values())] for g in range(1, 8)]

    ch = defaultdict(Counter)
    ch_name = {}
    for row in rows_all:
        key = (row[1], row[3])
        ch[key][row[5]] += 1
        ch_name[key] = row[4]
    ch_rows = []
    for (gname, chap), c in sorted(ch.items(), key=lambda x: (int(x[0][0][:-1]), int(re.sub(r"\D", "", x[0][1]) or 0))):
        total = sum(c.values())
        ch_rows.append([gname, chap, ch_name[(gname, chap)]] + [c[v] for v in ORDER] + [total, f"{(c[OK] + c[FXP]) / total:.0%}"])

    cat_count = Counter()
    for o in out:
        if o["final"] in (FXC, BAD):
            for name in categorize(o["reason"]):
                cat_count[name] += 1
    cat_rows = [[name, cat_count[name]] for name, _ in CATS]

    bad = [[o["type"], f"{o['grade']}급", o["no"], compose(o)[0], compose(o)[1]] for o in out if o["final"] == BAD]
    bad.sort(key=lambda r: (int(r[1][:-1]), r[2], r[0]))
    notes = [[f"{g}급", n, t] for (g, n), t in sorted(ref_notes.items())]

    legend = [
        [OK, "원문항과 유형·취지가 같고 결함이 없다. 그대로 쓸 수 있다."],
        [FXP, "내용은 맞지만 원본 형식과 다르다(발문 문구, 밑줄, 보기 기호·줄바꿈, 선택지 순서 등). 표기만 고치면 된다."],
        [FXC, "문제를 다시 손봐야 한다. 발문이 정답을 알려 줌, 원문항 문장·정답 재사용, 유형 간 오답 중복, 오답이 뻔함, 형식·평가 요소 변경 등."],
        [BAD, "정답 오류·복수 정답 위험이 크거나(C1), 원문항과 평가 문법 요소가 다르다(B1). 새로 만들어야 한다."],
    ]
    make_xlsx.write_workbook(OUT / "TOEG_변형문항_감수_요약.xlsx", [
        ("요약", head, summ),
        ("판정 기준", ["판정", "뜻"], legend),
        ("급수·챕터별", ["급수", "챕터", "챕터명"] + ORDER + ["합계", "그대로·표기만 수정 비율"], ch_rows),
        ("자주 나온 문제", ["문제 유형(수정(내용)·부적합 판정 근거 기준, 중복 집계)", "변형 문항 수"], cat_rows),
        ("부적합 목록", ["유형", "급수", "번호", "판정 근거", "수정 제안"], bad),
        ("원문항 확인 사항", ["급수", "번호", "내용"], notes),
        ("전체 판정", ["유형", "급수", "번호", "챕터", "챕터명", "판정", "판정 근거", "수정 제안", "자동 점검(원본 형식·노출)", "원문항 확인 사항"], rows_all),
    ])
    print("저장:", OUT / "TOEG_변형문항_감수_요약.xlsx")
    json.dump({"total": tot, "by_type": by_t, "by_grade": {str(k): v for k, v in by_g.items()},
               "chapters": ch_rows, "cats": cat_rows, "bad": bad, "notes": notes},
              open(HERE / "summary.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
