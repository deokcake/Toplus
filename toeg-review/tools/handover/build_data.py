#!/usr/bin/env python3
"""외부 업체 전달용 엑셀 자료 만들기.
사용: python3 tools/handover/build_data.py <db5 폴더>   (db5/t_B/*.json = 검토 페이지 DB의 B 유형 문서)
결과: 결과/외부전달/TOEG 변형 문항 출제 자료 (외부 전달용)/ 안의 엑셀 5개"""
import json, glob, re, sys, collections
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

HERE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(HERE)); import explfmt
DB = Path(sys.argv[1]) if len(sys.argv) > 1 else None
H = HERE / "결과/외부전달/TOEG 변형 문항 출제 자료 (외부 전달용)"
C5 = "①②③④⑤"; TYPES = "BCDEF"
FONT = "맑은 고딕"
idx = json.load(open(HERE / "page/data/index.json", encoding="utf-8"))
ref = json.load(open(HERE / "page/data/ref.json", encoding="utf-8"))
V = {t: json.load(open(HERE / f"page/data/{t}.json", encoding="utf-8")) for t in TYPES}
FX = {t: json.load(open(HERE / f"page/data/fix_{t}.json", encoding="utf-8")) for t in TYPES}
VA = json.load(open(HERE / "page/data/variant_audit.json", encoding="utf-8"))
SCREEN = {r["id"]: r for r in json.load(open(HERE / "src/screen.json", encoding="utf-8"))}
CHAP = {}
for g, chs in idx["grades"].items():
    for c in chs:
        for n in c["nos"]: CHAP[f"{g}-{n}"] = (c["ch"], c["chn"])
ORDER = idx["order"]
DBB = {}
if DB:
    for f in glob.glob(str(DB / "t_B" / "*.json")):
        DBB[Path(f).stem] = json.load(open(f, encoding="utf-8"))

# ---------------- 엑셀 서식 ----------------
thin = Side(style="thin", color="BFBFBF"); BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
HEAD_FILL = PatternFill("solid", fgColor="DCE6F1"); NOTE_FILL = PatternFill("solid", fgColor="FFF8DC")
def sheet(wb, title, header, rows, widths, note_cols=(), freeze="A2"):
    ws = wb.create_sheet(title)
    ws.append(header)
    for r in rows: ws.append(["" if v is None else v for v in r])
    for i, w in enumerate(widths, 1): ws.column_dimensions[get_column_letter(i)].width = w
    for cell in ws[1]:
        cell.font = Font(name=FONT, bold=True, size=10); cell.fill = HEAD_FILL; cell.border = BORDER
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 30
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.font = Font(name=FONT, size=10); cell.border = BORDER
            cell.alignment = Alignment(vertical="top", wrap_text=True)
    for ci in note_cols:
        for row in ws.iter_rows(min_row=2, min_col=ci, max_col=ci):
            for cell in row: cell.fill = NOTE_FILL
    if freeze: ws.freeze_panes = freeze
    if rows: ws.auto_filter.ref = f"A1:{get_column_letter(len(header))}{len(rows) + 1}"
    return ws

def guide(wb, title, lines, width=110):
    """안내 시트: (제목, 본문) 줄 목록."""
    ws = wb.create_sheet(title, 0)
    ws.column_dimensions["A"].width = 26; ws.column_dimensions["B"].width = width
    r = 1
    for a, b in lines:
        ws.cell(r, 1, a).font = Font(name=FONT, bold=bool(a), size=10)
        c = ws.cell(r, 2, b); c.font = Font(name=FONT, size=10); c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.cell(r, 1).alignment = Alignment(vertical="top", wrap_text=True)
        r += 1
    return ws

def fresh():
    wb = Workbook(); wb.remove(wb.active); return wb

def ex9(expl):
    cells = list(explfmt.cells(explfmt.parse(expl)))
    return (cells + [""] * 9)[:9]

def opts(c): return (list(c) + [""] * 5)[:5]
def gn(k): g, n = k.split("-"); return f"{g}급", int(n)
def rv2_last(r):
    rv = r.get("rv2") or []
    return rv[-1] if rv else None
def final_why(r):
    x = rv2_last(r); return (x["why"] if x and x.get("why") else r.get("why", ""))
def final_fix(r):
    x = rv2_last(r); return (x.get("fix") or r.get("fix") or "") if x else (r.get("fix") or "")
def flags_text(g, n, t):
    s = SCREEN.get(f"{g}급-{n:03d}-{t}")
    if not s or not s.get("flags"): return ""
    return "\n".join(f"{f['code']}({f['sev']}): {f['msg']}" for f in s["flags"])

# ---------------- 확정본 글 정하기 ----------------
def merged_edit(base, e):
    out = {"stem": base["stem"], "passage": base["passage"], "c": list(base["c"]), "ans": base["ans"], "expl": base.get("expl", "")}
    if not e: return out
    # 검토 페이지(effItem)와 같은 규칙: 문자열이면 빈 문자열("")도 감수자가 정한 값이다(본문을 지운 경우).
    for k in ("stem", "passage", "expl"):
        if isinstance(e.get(k), str): out[k] = e[k]
    if e.get("ans") not in (None, ""): out["ans"] = e["ans"]
    ec = e.get("c")
    if isinstance(ec, dict):
        for i, v in ec.items():
            if v is not None and 0 <= int(i) < 5: out["c"][int(i)] = v
    elif isinstance(ec, list):
        out["c"] = [v if v is not None else out["c"][i] for i, v in enumerate(ec)]
    return out

def final_item(t, r):
    """(글, 출처, 비고)"""
    k = f"{r['g']}-{r['n']}"; fx = FX[t].get(k)
    base = {"stem": r["stem"], "passage": r["passage"], "c": r["c"], "ans": r["ans"], "expl": r.get("expl", "")}
    def changed(a, b): return not (a["stem"] == b["stem"] and a["passage"] == b["passage"] and list(a["c"]) == list(b["c"]) and str(a["ans"]) == str(b["ans"]))
    if t == "B" and DBB.get(k, {}).get("edit"):
        d = DBB[k]; it = merged_edit(base, d["edit"])
        src = "감수자 확정(검토 페이지)" if changed(it, base) else "원안 유지(해설 보강)"
        note = ""
        if d.get("verdict") == "부적합" and not d.get("done"): note = "감수자 부적합 판정 뒤 확인 완료 표시가 없음 — 다시 확인 권장"
        return it, src, note
    if fx:
        it = {"stem": fx["stem"], "passage": fx["passage"], "c": list(fx["c"]), "ans": fx["ans"], "expl": fx.get("expl", "")}
        return it, ("수정 예시 적용" if changed(it, base) else "원안 유지(해설 보강)"), ""
    return base, "원안 유지", ""

def user_verdict(k):
    d = DBB.get(k) or {}; return d.get("verdict") or ""
def user_notes(k):
    d = DBB.get(k) or {}; ns = d.get("notes") or {}
    return "\n".join(v.get("text", "") for v in ns.values() if isinstance(v, dict) and v.get("text"))

MARK = [("표기 약속", ""),
        ("밑줄", "밑줄 친 부분은 <u>…</u> 태그로 감싼다. 예: The soup <u>tastes deliciously</u> today."),
        ("본문 속 번호", "본문 안에서 번호를 고르는 문항은 번호를 글 안에 넣고(①<u>attended</u>), 보기 칸에는 해당 낱말(또는 번호만)을 둔다."),
        ("줄바꿈", "본문·보기 안의 줄바꿈은 셀 안 줄바꿈(Alt+Enter)으로 둔다. 대화문은 ‘A: …’ ‘B: …’ 줄로, <보기>는 ‘<보기>’ 줄 뒤에 항목을 둔다."),
        ("표", "표로 보여 줄 자료는 칸을 탭(Tab)으로 나눈 줄 여러 개로 적는다(예: Name⇥Tom⇥Jerry)."),
        ("보기 기호", "선택지는 ①~⑤ 다섯 개. 본문 안 항목 기호는 원문항과 같게(ⓐ~ⓔ, (A)/(B), (가)~(마), ㄱ~ㄹ 등)."),
        ("정답", "정답은 1~5 숫자 하나."),
        ("해설", "핵심 규칙 → 풀이 순서 → 문장별 판정(없으면 비움) → 정답 판단 → 선택지 분석(①~⑤) 순서. 자세한 규칙은 ‘01_출제 규칙/04 해설 작성 규칙과 예시’ 참고.")]

# ================= 1. 기준 문항 =================
wb = fresh()
head = ["급수", "챕터", "챕터명", "문제번호", "발문", "본문", "보기 ①", "보기 ②", "보기 ③", "보기 ④", "보기 ⑤", "정답",
        "핵심 규칙", "풀이 순서", "문장별 판정", "정답 판단", "선택지 ① 분석", "선택지 ② 분석", "선택지 ③ 분석", "선택지 ④ 분석", "선택지 ⑤ 분석", "원문항 수정 여부"]
rows = []
for k in ORDER:
    r = ref[k]; g, n = gn(k); ch, chn = CHAP[k]
    rows.append([g, ch, chn, n, r["stem"], r["passage"], *opts(r["c"]), int(r["ans"]), *ex9(r.get("expl", "")), "감수 중 수정됨" if r.get("fixed") else ""])
sheet(wb, "기준 문항(820)", head, rows, [6, 7, 16, 8, 34, 44, 22, 22, 22, 22, 22, 6, 46, 56, 40, 44, 36, 36, 36, 36, 36, 12])
rows = []; total = 0
for g, chs in idx["grades"].items():
    for c in chs:
        rows.append([f"{g}급", c["ch"], c["chn"], f"{c['nos'][0]}~{c['nos'][-1]}", len(c["nos"])]); total += len(c["nos"])
rows.append(["합계", "", "", "", total])
sheet(wb, "급수·챕터 구성", ["급수", "챕터", "챕터명", "문항 번호", "문항 수"], rows, [8, 8, 24, 12, 8])
guide(wb, "안내", [("TOEG 기준 문항(원문항) 820문항", "변형 문항을 만들 때 기준이 되는 원문항 전체입니다. 2026-10-06 감수까지 반영된 확정본이며, 감수 중 고친 문항은 마지막 열에 표시했습니다(수정 전 내용은 ‘04_감수 기록/TOEG_원문항 수정 기록.xlsx’)."),
                  ("시트", "기준 문항(820): 문항 본문과 정답, 해설(5부분)  /  급수·챕터 구성: 급수마다 챕터 이름과 문항 번호 범위"),
                  ("급수", "7급이 가장 쉽고 1급이 가장 어렵습니다. 문항 번호는 급수 안에서 1번부터 이어집니다."),
                  ("해설 열", "핵심 규칙·풀이 순서·문장별 판정·정답 판단·선택지 ①~⑤ 분석의 9칸. 문장별 판정은 문장을 하나씩 판정하는 문항에만 있습니다."),
                  *MARK])
wb.save(H / "02_기준 문항(원문항)/TOEG_기준문항_전체(820).xlsx"); print("기준 문항 ok")

# ================= 2. 변형 확정본 =================
wb = fresh()
head = ["양식명", "급수", "챕터", "챕터명", "문제 분류", "문제 유형(객관식:1/주관식:2)", "난이도", "문제번호", "문제명", "본문",
        "보기 문항1", "보기 문항2", "보기 문항3", "보기 문항4", "보기 문항5", "정답", "설명", "확정 출처", "원안 판정(감수)", "비고"]
widths = [7, 6, 7, 14, 8, 10, 6, 8, 34, 44, 22, 22, 22, 22, 22, 6, 60, 14, 12, 24]
stat = collections.Counter(); FINAL = {}
for t in TYPES:
    rows = []
    for r in V[t]:
        k = f"{r['g']}-{r['n']}"; ch, chn = CHAP[k]
        it, src, note = final_item(t, r); FINAL[(t, k)] = it
        verdict = user_verdict(k) if t == "B" and user_verdict(k) else r["v"]
        stat[(t, src)] += 1
        rows.append(["TOEG", f"{r['g']}급", ch, chn, t, 1, "", r["n"], it["stem"], it["passage"], *opts(it["c"]), int(it["ans"]), it["expl"], src, verdict, note])
    sheet(wb, f"{t} 유형", head, rows, widths, note_cols=(18, 19, 20))
guide(wb, "안내", [("TOEG 변형 문항 확정본 (B~F 유형, 4,100문항)", "원문항 820개마다 변형 문항 5개(B·C·D·E·F)를 감수해 확정한 본문입니다. 열 구성은 문제등록 양식(납품 양식)과 같고, 뒤에 ‘확정 출처·원안 판정·비고’ 세 열을 덧붙였습니다."),
                  ("확정 출처", "감수자 확정(검토 페이지): 감수자가 검토 페이지에서 확정한 글(B 유형)  /  수정 예시 적용: 감수 수정 예시를 적용한 글  /  원안 유지(해설 보강): 원안 문항은 그대로 두고 해설만 새 짜임으로 바꾼 글"),
                  ("원안 판정(감수)", "처음 납품된 원안에 대한 판정입니다. 적합 / 수정(표기) / 수정(내용) / 부적합. 판정 근거와 수정 방향은 ‘04_감수 기록’ 폴더의 감수 결과 파일에 있습니다. 확정본은 판정과 무관하게 모두 바로 쓸 수 있는 상태입니다."),
                  ("유형 B~F", "유형 사이에 형식 차이는 없습니다. 같은 원문항의 다섯 변형이 서로 다른 문장을 써야 한다는 뜻의 구분입니다."),
                  *MARK])
wb.save(H / "03_변형 문항(B~F)/TOEG_변형문항_확정본(B~F).xlsx"); print("확정본 ok", dict(stat))

# ================= 3. 감수 결과 =================
wb = fresh()
head = ["급수", "챕터", "챕터명", "유형", "문제번호", "원안 발문", "원안 본문", "원안 보기 ①", "원안 보기 ②", "원안 보기 ③", "원안 보기 ④", "원안 보기 ⑤", "원안 정답",
        "1차 판정", "최종 판정", "판정 근거", "수정 방향", "자동 점검 표시", "감수자 판정", "감수자 메모", "확정본 처리"]
widths = [6, 7, 14, 6, 8, 32, 40, 20, 20, 20, 20, 20, 6, 10, 10, 50, 40, 36, 10, 36, 16]
cat_rows = collections.defaultdict(list); bad = []; vstat = collections.Counter(); gstat = collections.Counter()
CATS = [("발문·설명이 정답이나 규칙을 알려 줌", r"발문.*(알려|단서|규칙)|발문이 정답"),
        ("원문항 문장·정답 재사용(노출)", r"원문항(의|과)? ?(문장|정답|보기|선택지).*(같|그대로|재사용|겹)|쌍둥이 문장|원문항과 거의 같"),
        ("유형 간 오답·문장 중복", r"(B|C|D|E|F)와 (똑같|같)|유형(과|끼리|간).*(같|중복|겹)"),
        ("대비(짝) 단서", r"대비|짝을|함께 나와|두 번 나와"),
        ("없는 형태·뻔한 오답", r"없는 형태|존재하지 않|뻔한|매력도"),
        ("길이·겉모양으로 정답이 드러남", r"길이|가장 길|겉모양|눈에 띄"),
        ("형식·표기가 원문항과 다름(밑줄·<보기>·기호·줄바꿈)", r"밑줄|<보기>|줄바꿈|기호|표기"),
        ("평가 요소·과제가 원문항과 다름", r"평가 요소|과제|범위|형식이 다르|발문이 (바뀌|달라)"),
        ("복수 정답·정답 오류", r"복수 정답|정답이 둘|정답 없|정답 오류|정답 시비"),
        ("영어 표현 오류·부자연스러움", r"원어민|부자연|어색한 영어|철자|오류형"),
        ("난이도·수준 차이", r"난이도|어렵|쉬워|수준")]
for t in TYPES:
    rows = []
    for r in V[t]:
        k = f"{r['g']}-{r['n']}"; ch, chn = CHAP[k]; why = final_why(r); fix = final_fix(r)
        it, src, note = final_item(t, r)
        uv = user_verdict(k) if t == "B" else ""; un = user_notes(k) if t == "B" else ""
        rows.append([f"{r['g']}급", ch, chn, t, r["n"], r["stem"], r["passage"], *opts(r["c"]), int(r["ans"]), r.get("v1") or r["v"], r["v"], why, fix, flags_text(r["g"], r["n"], t), uv, un, src])
        vstat[(t, r["v"])] += 1; gstat[(f"{r['g']}급", r["v"])] += 1
        if r["v"] != "적합":
            for name, pat in CATS:
                if re.search(pat, why): cat_rows[name].append((f"{r['g']}급 {r['n']}번 {t}", why, fix))
        if r["v"] == "부적합": bad.append([f"{r['g']}급", ch, chn, t, r["n"], why, fix, src])
    sheet(wb, f"{t} 유형", head, rows, widths, note_cols=(19, 20))
guide(wb, "안내", [("TOEG 변형 문항 감수 결과", "처음 납품된 원안 4,100문항을 감수한 기록입니다. 원안 글과 판정, 판정 근거, 수정 방향을 유형별 시트에 담았습니다. 어떤 문항이 왜 걸렸는지 보면 출제 때 피해야 할 점을 알 수 있습니다."),
                  ("1차 판정 / 최종 판정", "1차는 2026-09-28 감수, 최종은 2026-10-02 전체 재감수(2차)와 2026-10-06 감수자 메모 반영까지의 판정입니다."),
                  ("판정", "적합: 그대로 쓸 수 있음  /  수정(표기): 내용은 맞지만 원문항 형식과 다름(발문 문구·밑줄·기호·줄바꿈)  /  수정(내용): 문제를 다시 손봐야 함  /  부적합: 정답 오류·복수 정답 위험이 크거나 평가 요소가 다름"),
                  ("자동 점검 표시", "기계 점검(형식·노출·정답 표기)에서 걸린 항목. 코드는 감수 기준표의 C1~C7·B3을 따릅니다."),
                  ("감수자 판정·메모", "검토 페이지에서 감수자가 직접 남긴 판정과 메모(B 유형). 비어 있으면 감수 판정을 그대로 따른 것입니다."),
                  ("확정본 처리", "이 원안이 확정본(03_변형 문항)에서 어떻게 처리됐는지.")])
wb.save(H / "04_감수 기록/TOEG_변형문항_감수 결과(원안·판정·사유).xlsx"); print("감수 결과 ok")

# ================= 4. 통계·자주 나온 결함 =================
wb = fresh()
VS = ["적합", "수정(표기)", "수정(내용)", "부적합"]
rows = [[f"{t} 유형", *[vstat[(t, v)] for v in VS], sum(vstat[(t, v)] for v in VS)] for t in TYPES]
rows.append(["전체", *[sum(vstat[(t, v)] for t in TYPES) for v in VS], 4100])
for g in "1234567": rows.append([f"{g}급", *[gstat[(f'{g}급', v)] for v in VS], sum(gstat[(f'{g}급', v)] for v in VS)])
sheet(wb, "판정 요약", ["구분", *VS, "합계"], rows, [10, 10, 10, 10, 10, 10])
rows = []
for name, _ in CATS:
    L = cat_rows.get(name, []); L2 = sorted(L, key=lambda x: len(x[1]))[: max(0, len(L))]
    exs = [x for x in L2 if 40 <= len(x[1]) <= 160][:2] or L2[:2]
    cells = []
    for e in exs: cells += [e[0], e[1], e[2]]
    cells += [""] * (6 - len(cells))
    rows.append([name, len(L), *cells])
sheet(wb, "자주 나온 결함", ["결함 유형(판정 근거 기준, 중복 집계)", "문항 수", "예시 1 문항", "예시 1 근거", "예시 1 수정 방향", "예시 2 문항", "예시 2 근거", "예시 2 수정 방향"], rows, [36, 8, 14, 50, 36, 14, 50, 36])
sheet(wb, "부적합 목록", ["급수", "챕터", "챕터명", "유형", "문제번호", "판정 근거", "수정 방향", "확정본 처리"], bad, [6, 7, 14, 6, 8, 60, 40, 16])
rows = [[*gn(x["key"]), x["type"], x["level"], x["problem"], x["fix"], {"예시적용": "수정 예시 적용", "직접수정": "직접 수정"}.get(x["how"], x["how"])] for x in VA]
sheet(wb, "변형 점검(원문항 수정 연동)", ["급수", "문제번호", "유형", "등급", "문제", "조치", "처리"], rows, [6, 8, 6, 6, 60, 50, 12])
guide(wb, "안내", [("TOEG 변형 문항 감수 통계", "최종 판정 분포와, 수정·부적합 판정의 근거에서 자주 나온 결함 유형을 정리했습니다. 출제 전에 ‘자주 나온 결함’ 시트를 한 번 읽어 두면 같은 실수를 피할 수 있습니다."),
                  ("변형 점검(원문항 수정 연동)", "감수 중 원문항을 고치면서, 같은 결함이 있거나 맞춰 고쳐야 했던 변형 문항 목록입니다.")])
wb.save(H / "04_감수 기록/TOEG_감수 통계·자주 나온 결함.xlsx"); print("통계 ok", {k: len(v) for k, v in cat_rows.items()})

# ================= 5. 납품 양식 =================
wb = fresh()
head = ["양식명", "급수", "챕터", "챕터명", "문제 분류", "문제 유형(객관식:1/주관식:2)", "난이도", "문제번호", "문제명", "본문",
        "보기 문항1", "보기 문항2", "보기 문항3", "보기 문항4", "보기 문항5", "정답", "설명"]
it = FINAL[("B", "1-1")]
ex = ["TOEG", "1급", "CH 1", "문장의 구조", "B", 1, "", 1, it["stem"], it["passage"], *opts(it["c"]), int(it["ans"]), it["expl"]]
ws = sheet(wb, "문제등록", head, [ex], [7, 6, 7, 14, 8, 10, 6, 8, 34, 44, 22, 22, 22, 22, 22, 6, 60])
for cell in ws[2]: cell.fill = NOTE_FILL
guide(wb, "작성 요령", [("TOEG 변형 문항 납품 양식", "‘문제등록’ 시트의 열 구성대로 납품합니다. 2행은 작성 예시(노란 바탕)이며 실제 납품 때는 지우고 그 자리부터 채웁니다. 유형 B~F는 시트를 나누지 말고 한 시트에 이어 적어도 되고, 유형별 파일로 나눠도 됩니다."),
                       ("양식명", "항상 TOEG"), ("급수", "‘1급’~‘7급’"), ("챕터 / 챕터명", "기준 문항 파일의 ‘급수·챕터 구성’ 시트와 같게"),
                       ("문제 분류", "변형 유형 B·C·D·E·F 중 하나"), ("문제 유형", "객관식은 1"), ("난이도", "비워 둠"),
                       ("문제번호", "원문항(기준 문항)의 번호. 변형 문항은 원문항과 같은 번호를 씁니다."),
                       ("문제명", "발문. 원문항의 발문을 그대로 씁니다(조건·형식 포함)."), ("본문", "제시문·대화문·<보기>·표. 없으면 비움."),
                       ("보기 문항1~5", "선택지 ①~⑤의 내용(기호는 빼고 내용만)."), ("정답", "1~5 숫자 하나"),
                       ("설명", "해설. 핵심 규칙 → 풀이 순서 → 문장별 판정 → 정답 판단 → 선택지 분석 순서(‘04 해설 작성 규칙과 예시’ 참고)."),
                       *MARK])
wb.save(H / "05_참고 자료/납품 양식/TOEG_변형문항_납품 양식.xlsx"); print("양식 ok")
