#!/usr/bin/env python3
"""영상 대본 JSON 자동 점검(2판 규격). 사용: python3 tools/video/check_scripts.py <대본.json 또는 폴더> ...
ERR = 고쳐야 함, WARN = 확인."""
import sys, re, json, glob, os
C5 = "①②③④⑤"
BAD_NARR = re.compile(r"[①②③④⑤ⓐⓑⓒⓓⓔ]|</?u>|→|_{3,}|-ing|-s\b|-es\b|\(A\)|\(B\)|\(C\)")
SELF = re.compile(r"오늘|같은 원리|앞 영상|다음 영상|이전 영상|지난 영상|다른 영상|이번 시간|지난 시간|변형 문제|원문항")
ODD = re.compile(r"[/+~=]|\.\.\.")
NAMES = ["도입", "문제", "핵심 규칙", "풀이 순서", "선택지 확인", "정리"]
RANGE = {1: (6, 14), 2: (10, 22), 3: (14, 32), 4: (25, 50), 5: (16, 40), 6: (6, 14)}

def norm(s): return re.sub(r"\s+", " ", str(s or "")).strip()

# 실제 낭독 시간 추정(초): ko-KR-SunHiNeural 실측 36장면으로 맞춤(장면당 오차 평균 0.9초)
def speak(t):
    t = str(t or "")
    return 0.188 * len(re.findall(r"[가-힣]", t)) + 0.393 * len(re.findall(r"[A-Za-z]+", t)) + 0.197 * len(re.findall(r"\d", t)) + 0.368 * (len(re.findall(r"[.?!]", t)) + t.count(","))
MAX_SEC, AIM_SEC = 150, 140
def scene_need(s):
    """그 장면에 실제로 필요한 초: 낭독 + 여유(장면 2는 풀어 볼 시간 6초)."""
    return speak(s.get("narration", "")) + (6 if s.get("no") == 2 else 1)
def est_total(d): return sum(max(int(s.get("sec", 0)), scene_need(s)) for s in d.get("scenes") or [])
def check(d):
    E, W = [], []
    sc = d.get("scenes") or []; src = d.get("source") or {}; a = src.get("ans")
    if [s.get("name") for s in sc] != NAMES: E.append(f"장면 이름/순서가 규격과 다름: {[s.get('name') for s in sc]}")
    if not d.get("title", "").strip(): E.append("title 비어 있음")
    tot = sum(int(s.get("sec", 0)) for s in sc)
    if tot != d.get("total_sec"): E.append(f"total_sec {d.get('total_sec')} ≠ 장면 합 {tot}")
    est = est_total(d)
    if est > MAX_SEC:
        per = ", ".join(f"{x.get('name')} {max(int(x.get('sec', 0)), scene_need(x)):.0f}" for x in sc)
        E.append(f"실제 낭독 기준 추정 {est:.0f}초 > {MAX_SEC}초(2분 30초). 꼭 필요한 내용만 남기세요: 규칙은 이 문제를 푸는 데 필요한 것만(형태·쓰임 + 예문 1개), 풀이 단계는 결정적 근거만 2~3단계, 앞 장면에서 한 말 되풀이 금지, 선택지 확인은 정답 이유 + 학생이 고를 오답 2개. 장면별 초: {per}")
    elif est > AIM_SEC: W.append(f"실제 낭독 기준 추정 {est:.0f}초(권장 {AIM_SEC}초 이내)")
    if tot < 60: W.append(f"총 길이 {tot}초가 너무 짧음")
    for s in sc:
        no = s.get("no"); lo, hi = RANGE.get(no, (1, 999))
        if not lo <= int(s.get("sec", 0)) <= hi: W.append(f"장면 {no} 길이 {s.get('sec')}초(권장 {lo}~{hi})")
        nar = s.get("narration", "") or ""
        if BAD_NARR.search(nar): E.append(f"장면 {no} 내레이션에 읽을 수 없는 기호: {BAD_NARR.search(nar).group(0)!r}")
        if SELF.search(nar) or SELF.search(s.get("screen", {}).get("text", "")): E.append(f"장면 {no}에 금지 표현(오늘은/같은 원리 문제/다른 영상 언급)")
        sents = [x for x in re.split(r"(?<=[.?!])\s+", nar.strip()) if re.search(r"[가-힣]", x)]
        lim = 5 if no in (3, 4, 5) else (4 if no == 2 else 3)   # 장면 2는 지문을 ‘빈칸’ 넣어 읽은 문장 1개를 더 허용
        if len(sents) > lim: W.append(f"장면 {no} 내레이션 한국어 {len(sents)}문장(이 장면은 {lim}문장 이내)")
        scr = s.get("screen") or {}; text = scr.get("text", "") or ""
        for fld in ("highlight", "strike", "reveal"):
            for frag in scr.get(fld) or []:
                if frag and norm(frag) not in norm(text): E.append(f"장면 {no} {fld} 조각이 화면 글에 없음: {frag[:40]!r}")
        for st in scr.get("steps") or []:
            for fld in ("highlight", "strike"):
                for frag in st.get(fld) or []:
                    if frag and norm(frag) not in norm(text): E.append(f"장면 {no} 단계 {st.get('step')} {fld} 조각이 화면 글에 없음: {frag[:40]!r}")
        if no == 2 and re.search(r"[✓✗]|정답", text): E.append("장면 2 화면에 정답 표시가 있음")
        if no == 2:
            for i, c in enumerate(src.get("c") or []):
                if norm(c) not in norm(text): E.append(f"장면 2 화면에 보기 {C5[i]} 원문이 없음")
            if norm(src.get("stem", "")) not in norm(text): E.append("장면 2 화면에 발문 원문이 없음")
        if no == 5 and a:
            marks = scr.get("marks") or {}
            if marks.get(C5[a - 1]) != "✓" or any(marks.get(C5[i]) == "✓" for i in range(5) if i + 1 != a): E.append(f"장면 5 marks가 정답 {C5[a-1]}과 어긋남: {marks}")
        if no == 6 and a and f"{a}번" not in nar: E.append(f"장면 6 내레이션에 '정답은 {a}번'이 없음")
        if no == 1 and not re.search(r"^\d급 챕터 [^,]+, \d+번( [B-F] 유형)?\. 이 문제는 ", nar): E.append("장면 1 내레이션이 ‘N급 챕터 M, K번. 이 문제는 …’ 꼴이 아님")
        if ODD.search(nar): W.append(f"장면 {no} 내레이션에 소리 내어 읽기 어려운 기호: {ODD.search(nar).group(0)!r}")
        if no == 5:
            lines = [l for l in text.split("\n") if l.strip()]
            if len(lines) != 5: E.append(f"장면 5 화면 줄 수 {len(lines)}(보기마다 한 줄, 5줄)")
            for i, l in enumerate(lines[:5]):
                if not l.startswith(C5[i]): E.append(f"장면 5 {i+1}째 줄이 {C5[i]}로 시작하지 않음")
                elif i < len(src.get("c") or []) and norm(src["c"][i]) not in norm(l): E.append(f"장면 5 {C5[i]} 줄에 보기 원문이 없음")
                if ("✓" in l) != (a == i + 1): E.append(f"장면 5 {C5[i]} 줄의 ✓/✗ 표시가 정답과 어긋남")
        if no == 3 and len(norm(nar)) < 40: W.append("장면 3 규칙 설명이 짧음(형태·뜻·예문)")
    return E, W

def main(paths):
    files = []
    for p in paths: files += sorted(glob.glob(os.path.join(p, "*.json"))) if os.path.isdir(p) else [p]
    ne = nw = 0; bad = []
    for f in files:
        try: d = json.load(open(f, encoding="utf-8"))
        except Exception as e: print(f"[{os.path.basename(f)}] ERR JSON 읽기 실패: {e}"); ne += 1; continue
        E, W = check(d); ne += len(E); nw += len(W)
        if E or W:
            print(f"[{os.path.basename(f)}] {d.get('total_sec')}초")
            for e in E: print("   ERR ", e)
            for w in W: print("   WARN", w)
        if E: bad.append(os.path.basename(f))
    print(f"files {len(files)} | ERR {ne} in {len(bad)} files | WARN {nw}")
    return bad

if __name__ == "__main__": main(sys.argv[1:])
