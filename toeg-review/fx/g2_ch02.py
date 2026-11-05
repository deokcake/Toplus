# 2급 CH2 시제 (11~20) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 2-13 완료형 과거분사: 원문항 발문·밑줄 복원, 같은 동사의 옳은 짝 문장 교체
R13 = "현재완료·과거완료는 have/has/had + 과거분사(p.p.)로 만든다. 불규칙동사는 과거형과 과거분사형이 다를 수 있으므로 각각 확인한다."
OKP = "과거분사를 바르게 썼다({}). 어색하지 않으므로"
BADP = "과거분사 자리에 {}. {}(으)로 고쳐야 하는 어색한 곳이므로"
S13 = "발문이 ‘완료 시제의 동사 형태가 잘못된 문장’으로 바뀌고 밑줄이 없어 원문항 발문과 밑줄 형식으로 되돌렸다."
mk(2, 13, "B", [("The price has <u>risen</u> recently.", "has risen: " + OKP.format("rise-rose-risen")), ("The team has <u>winned</u> three games this season.", "has winned: " + BADP.format("없는 형태를 썼다(win-won-won)", "has won")),
                ("They have <u>built</u> a new bridge.", "have built: " + OKP.format("build-built-built")), ("I have <u>forgotten</u> his name.", "have forgotten: " + OKP.format("forget-forgot-forgotten")),
                ("She has <u>swum</u> across the lake.", "has swum: " + OKP.format("swim-swam-swum"))], 2, R13,
   S13 + " 원문항 ⑤와 겹치는 ‘has seen that film’을 ‘has swum across the lake’로 바꿨다.", st="R")
mk(2, 13, "C", [("I have <u>broken</u> the rule once.", "have broken: " + OKP.format("break-broke-broken")), ("They have <u>spoken</u> to him.", "have spoken: " + OKP.format("speak-spoke-spoken")),
                ("Tom has <u>driven</u> this car before.", "has driven: " + OKP.format("drive-drove-driven")), ("I have <u>wrote</u> to her several times.", "have wrote: " + BADP.format("과거형을 썼다(write-wrote-written)", "have written")),
                ("We have <u>thrown</u> away the old boxes.", "have thrown: " + OKP.format("throw-threw-thrown"))], 4, R13,
   S13 + " 정답 문장과 같은 동사를 옳게 쓴 ‘have written’ 문장이 대비 단서가 되어 ‘have thrown away’ 문장으로 바꿨다.", st="R")
mk(2, 13, "D", [("We have <u>made</u> progress.", "have made: " + OKP.format("make-made-made")), ("Jane has <u>lent</u> me a book.", "has lent: " + OKP.format("lend-lent-lent")),
                ("She has <u>gave</u> me useful advice.", "has gave: " + BADP.format("과거형을 썼다(give-gave-given)", "has given")), ("He has <u>known</u> her for years.", "has known: " + OKP.format("know-knew-known")),
                ("They have <u>taken</u> the test.", "have taken: " + OKP.format("take-took-taken"))], 3, R13,
   S13 + " 정답 문장과 같은 동사를 옳게 쓴 ‘has given’ 문장이 대비 단서가 되어 ‘has lent’ 문장으로 바꾸고 정답 위치를 옮겼다.", st="R")
mk(2, 13, "E", [("Tom has <u>come</u> early.", "has come: " + OKP.format("come-came-come")), ("They have <u>chosen</u> a leader.", "have chosen: " + OKP.format("choose-chose-chosen")),
                ("She has <u>drawn</u> a picture.", "has drawn: " + OKP.format("draw-drew-drawn")), ("I have <u>ridden</u> a horse.", "have ridden: " + OKP.format("ride-rode-ridden")),
                ("We have <u>took</u> the same bus before.", "have took: " + BADP.format("과거형을 썼다(take-took-taken)", "have taken"))], 5, R13,
   S13 + " 정답 문장과 같은 동사를 옳게 쓴 ‘have taken’ 문장이 대비 단서가 되어 ‘have ridden’ 문장으로 바꿨다.", st="R")
mk(2, 13, "F", [("Tom has <u>chose</u> a different topic.", "has chose: " + BADP.format("과거형을 썼다(choose-chose-chosen)", "has chosen")), ("She has <u>drunk</u> enough water.", "has drunk: " + OKP.format("drink-drank-drunk")),
                ("They have <u>done</u> the work.", "have done: " + OKP.format("do-did-done")), ("We have <u>grown</u> tomatoes this year.", "have grown: " + OKP.format("grow-grew-grown")),
                ("I have <u>found</u> my keys.", "have found: " + OKP.format("find-found-found"))], 1, R13,
   S13 + " 정답 문장과 같은 동사를 옳게 쓴 ‘have chosen’ 문장이 대비 단서가 되어 ‘have grown’ 문장으로 바꾸고 정답 위치를 옮겼다.", st="R")

# 2-15 개수 보기 정렬 + 줄바꿈
for t, (o, nw) in {"B": ("⑤", "③"), "C": ("①", "③"), "D": ("③", "④"), "E": ("③", "④"), "F": ("④", "④")}.items():
    F(2, 15, t, p="BR", op="sortc", s=f"개수 선택지를 2개~6개 순으로 정렬(정답 {o}→{nw})하고, 한 줄로 이어 쓴 a)~f)를 한 줄에 한 문장씩 나눴다.")

# 2-16 상태동사: 답을 알려 주던 발문을 원문항대로
S16 = "발문이 ‘일반적인 상태를 나타내는 단순현재 문장이 되도록’이라고 답의 형태를 알려 주어, 원문항 발문 ‘밑줄 친 부분을 바르게 고친 것’으로 되돌렸다."
XR16 = [("이 문항은 일반적인 상태를 단순현재로 표현하도록 요구한다. ", "상태를 나타내는 동사(know, believe, own, need, resemble 등)는 보통 진행형으로 쓰지 않고 단순현재로 쓴다. ")]
for t in "BCDF":
    F(2, 16, t, st="R", xr=XR16, s=S16 + " 보기와 정답은 그대로다.")
mk(2, 16, "E", [("resembling", "resembling: -ing 형태만으로는 문장의 동사가 될 수 없다. 완성문: Tom resembles his father."), ("is resemble", "is resemble: be동사와 동사원형을 직접 이어 쓸 수 없다. 완성문: Tom resembles his father."),
                ("is resembled", "is resembled: 수동형이다. ‘닮다’라는 뜻의 상태동사는 수동태로 쓰지 않는다. 완성문: Tom resembles his father."),
                ("resembles", "resembles: 상태동사를 단순현재로 쓰고 3인칭 단수 주어(Tom)에 맞춰 -s를 붙였다. 완성문: Tom resembles his father."),
                ("resemble", "resemble: 주어가 3인칭 단수(Tom)이므로 -s가 붙어야 한다. 완성문: Tom resembles his father.")], 4,
   "상태를 나타내는 동사(know, believe, own, need, resemble 등)는 보통 진행형으로 쓰지 않고 단순현재로 쓴다. 단순현재형은 주어와 수를 일치시킨다.",
   S16 + " ‘now’가 있어 진행형(점점 이해해 가는 중)도 가능했던 ‘Tom is understanding the problem now.’를 진행형으로 쓸 수 없는 ‘Tom is resembling his father.’로 바꾸고 정답 위치를 옮겼다.",
   st="R", p="Tom <u>is resembling</u> his father.", k="‘닮다(resemble)’는 상태를 나타내는 동사라 진행형으로 쓰지 않는다. 3인칭 단수 주어에 맞춰 resembles로 고친다. 완성문: Tom resembles his father.")

# 2-18 시간·조건 부사절: 괄호 조건 삭제, B·C는 정답 조합을 원문항과 다르게
ST18 = "다음 중 밑줄 친 부분이 어법상 옳은 문장을 모두 빠짐없이 묶은 것은?"
R18 = "미래의 시간·조건을 나타내는 부사절(when, after, until, if, unless 등)에서는 미래의 일도 현재형으로 쓴다. 옳은 문장을 빠짐없이 모두 묶은 보기를 고른다."
XRR = ("발문의 단순 미래 조건과 모두 선택 조건을 적용한다.", "옳은 문장을 빠짐없이 모두 묶은 보기를 고른다.")
c = ["(B), (D)", "(A), (B)", "(A), (C)", "(B), (C), (D)", "(C), (D)"]
F(2, 18, "B", st=ST18, p="(A) If it <u>will rain</u> tomorrow, we'll cancel the picnic.\n(B) I'll message you when I <u>get</u> home.\n(C) We won't leave until Dad <u>will finish</u> his call.\n(D) We'll start after everyone <u>arrives</u>.",
  c=c, a=1, r=R18, pre=["문장별 판정: (A) X. 미래의 조건을 나타내는 if 부사절에는 현재형을 쓴다: will rain → rains. 교정문: If it rains tomorrow, we'll cancel the picnic.",
                        "문장별 판정: (B) O. 시간 부사절(when)에서 현재형(get)으로 미래의 도착을 나타냈다.",
                        "문장별 판정: (C) X. 시간 부사절(until)에는 현재형을 쓴다: will finish → finishes. 교정문: We won't leave until Dad finishes his call.",
                        "문장별 판정: (D) O. 시간 부사절(after)에서 현재형(arrives)을 쓰고 단수 취급하는 주어(everyone)와 수를 맞췄다."],
  k="옳은 문장은 (B), (D)이고, 이 둘을 빠짐없이 묶은 보기가 정답이다.", n=setnotes(c, "(B), (D)", "옳은 문장"),
  s="정답 조합 (A), (C)가 원문항 정답과 같았고, 발문 괄호가 판단 조건을 알려 주었다. 괄호를 지우고, 의지로 읽힐 수 있는 ‘unless Tom will come’ 대신 ‘until Dad will finish’를 넣어 옳은 문장을 (B), (D)로 옮겼다. 문장마다 줄을 바꿨다. 정답 위치 ①.")
c = ["(A), (C)", "(B), (C)", "(A), (B), (D)", "(B), (C), (D)", "(A), (C), (D)"]
F(2, 18, "C", st=ST18, p="(A) If Jane <u>will be</u> free, she will join us.\n(B) She will call you when the meeting <u>ends</u>.\n(C) I'll wait here until the bus <u>comes</u>.\n(D) Let's go out after the rain <u>stops</u>.",
  c=c, a=4, r=R18, pre=["문장별 판정: (A) X. 미래의 조건을 나타내는 if 부사절에는 현재형을 쓴다: will be → is. 교정문: If Jane is free, she will join us.",
                        "문장별 판정: (B) O. 시간 부사절(when)에서 현재형(ends)으로 회의가 끝날 미래 시점을 나타냈다.",
                        "문장별 판정: (C) O. 시간 부사절(until)에서 현재형(comes)으로 버스가 올 미래 시점을 나타냈다.",
                        "문장별 판정: (D) O. 시간 부사절(after)에서 현재형(stops)으로 비가 그칠 미래 시점을 나타냈다."],
  k="옳은 문장은 (B), (C), (D)이고, 셋을 빠짐없이 묶은 보기가 정답이다.", n=setnotes(c, "(B), (C), (D)", "옳은 문장"),
  s="정답 조합 (A), (C)가 원문항 정답과 같았고, 발문 괄호가 판단 조건을 알려 주었다. 괄호를 지우고 틀린 문장을 (A) 하나로 줄여 옳은 문장이 (B), (C), (D)가 되게 했다. 문장마다 줄을 바꿨다. 정답 위치 ④.")
F(2, 18, "D", st=ST18, p="BR", xr=[XRR, ("단순 미래 조건에서 will snow를", "미래의 조건 부사절이므로 will snow를")], s="발문 끝의 괄호 조건(각 will은 단순 미래…)을 지웠다. 문장마다 줄을 바꿨다. 보기와 정답은 그대로다.")
F(2, 18, "E", st=ST18, p="BR", xr=[XRR, ("if의 단순 미래 조건절에서", "if의 조건 부사절에서")], s="발문 끝의 괄호 조건(각 will은 단순 미래…)을 지웠다. 문장마다 줄을 바꿨다. 보기와 정답은 그대로다.")
F(2, 18, "F", st=ST18, p="BR", xr=[XRR], s="발문 끝의 괄호 조건(각 will은 단순 미래…)을 지웠다. 문장마다 줄을 바꿨다. 보기와 정답은 그대로다.")

# 2-19 단순과거 vs 현재완료 설명: 오답 네 개를 유형마다 새로
R19 = "현재완료는 have/has + p.p.로 과거의 경험·완료·계속·결과를 현재와 연결하고, yesterday·ago처럼 끝난 과거 시점에는 단순과거를 쓴다."
S19 = "오답 네 개가 B와 똑같아서, 유형마다 다른 오개념으로 오답 설명을 새로 쓰고 정답 위치를 옮겼다. 원문항처럼 본문에 <보기> 표시도 넣었다."
P19 = lambda t: "<보기>\n" + V(2, 19, t)["passage"]
mk(2, 19, "C", [("(A)는 지금도 안경이 깨져 있음을 반드시 뜻하고, (B)는 안경을 이미 고쳤음을 뜻한다.", "(A)의 단순과거는 어제 깨진 사건만 말할 뿐 지금 상태는 알려 주지 않고, 현재 결과와 연결되는 것은 (B)이다. 두 문장의 설명을 뒤바꿨으므로"),
                ("(A)와 (B) 모두 앞으로 안경이 깨질 것이라는 예측을 나타낸다.", "두 문장 모두 이미 일어난 일을 나타내며 미래의 예측이 아니므로"),
                ("(B)에 yesterday를 덧붙여 ‘Tom has broken his glasses yesterday.’로 써도 어법상 옳다.", "현재완료는 끝난 과거 시점을 나타내는 말(yesterday)과 함께 쓸 수 없으므로"),
                ("(A)는 어제의 사건을 말하고, (B)는 현재도 안경이 깨진 결과가 이어짐을 강조한다.", "(A)의 단순과거는 어제라는 특정 과거 사건을, (B)의 현재완료는 그 결과가 지금까지 이어짐을 나타낸다는 차이를 정확히 설명하므로"),
                ("(A)의 동사는 과거분사로, ‘깨진’이라는 수동의 뜻을 나타낸다.", "(A)의 동사는 과거형(broke)으로, 주어가 안경을 깨뜨린 능동의 과거 사건을 나타내므로")], 4, R19, S19, p=P19("C"))
mk(2, 19, "D", [("(A)는 특정 시각(at 8)이 있으므로 현재완료로 고쳐 써야 한다.", "끝난 과거의 특정 시각이 있는 문장은 단순과거로 쓰는 것이 맞아 고칠 필요가 없으므로"),
                ("(A)는 지금 기차를 타고 있다는 뜻이고, (B)는 기차를 놓친 과거 사건만을 말한다.", "(A)는 8시에 기차를 놓친 과거 사건이고 지금 기차를 타고 있다는 뜻이 없다. (B)도 과거 사건만이 아니라 현재 결과와 연결되므로"),
                ("(A)는 특정 시각의 과거 사건이고, (B)는 현재의 결과와 관련된 완료 상황을 나타낸다.", "(A)의 단순과거는 8시라는 특정 시각의 사건을, (B)의 현재완료는 놓친 결과가 지금 상황과 관련됨을 나타낸다는 차이를 정확히 설명하므로"),
                ("(B)는 ‘have + 과거형’으로 이루어진 과거완료 시제이다.", "(B)는 have + 과거분사로 된 현재완료이며, 과거완료는 had + 과거분사이므로"),
                ("(A)와 (B)는 모두 기차를 놓친 결과가 지금까지 이어짐을 똑같이 강조한다.", "(A)의 단순과거는 현재 결과를 강조하지 않고 과거 시각의 사건만 말하므로")], 3, R19, S19, p=P19("D"))
mk(2, 19, "E", [("(A)는 last night라는 과거 시점, (B)는 현재 열쇠가 없는 결과를 중심으로 한다.", "(A)의 단순과거는 어젯밤이라는 과거 시점의 사건을, (B)의 현재완료는 지금 열쇠가 없는 결과를 나타낸다는 차이를 정확히 설명하므로"),
                ("(B)는 잃어버린 열쇠를 이미 되찾았다는 뜻을 분명히 나타낸다.", "현재완료의 결과 용법은 잃어버린 결과가 지금도 이어짐, 곧 아직 열쇠가 없음을 나타내므로"),
                ("(A)는 열쇠를 잃어버리는 동작이 지금도 진행 중임을 나타낸다.", "(A)의 단순과거는 어젯밤에 끝난 일을 나타내며 진행의 뜻이 없으므로"),
                ("(B)에서 has 대신 had를 써도 시제와 의미가 달라지지 않는다.", "had를 쓰면 과거의 어느 시점보다 앞선 일을 나타내는 과거완료가 되어 시제와 의미가 달라지므로"),
                ("(A)는 과거 시점 표현이 있으므로 과거완료로 바꿔야 어법상 옳다.", "끝난 과거 시점의 사건은 단순과거로 쓰는 것이 맞고, 과거완료는 기준이 되는 다른 과거 시점이 있어야 쓰므로")], 1, R19, S19, p=P19("E"))
mk(2, 19, "F", [("(A)는 가게가 지금도 닫혀 있다는 사실을 분명히 알려 준다.", "단순과거는 9시에 문을 닫은 과거 사건만 말하고 지금 상태는 알려 주지 않으므로"),
                ("(B)의 동사 형태도 과거형이므로 두 문장은 모두 단순과거이다.", "(B)는 has + 과거분사로 된 현재완료이므로"),
                ("(B)는 가게가 문을 닫은 정확한 시각을 알려 준다.", "현재완료는 닫은 결과가 지금 이어짐을 나타낼 뿐 정확한 과거 시각을 말하지 않으며, 시각을 말하는 것은 (A)이므로"),
                ("(A)는 현재완료 시제로, 9시 이후 지금까지 계속 닫혀 있음을 나타낸다.", "(A)는 동사의 과거형만 쓴 단순과거이므로"),
                ("(A)는 9시에 닫힌 과거 사건, (B)는 현재 닫혀 있는 결과를 나타낸다.", "(A)의 단순과거는 9시라는 과거 시점의 사건을, (B)의 현재완료는 지금 닫혀 있는 결과를 나타낸다는 차이를 정확히 설명하므로")], 5, R19, S19, p=P19("F"))

# 2-20 옳은 문장 개수: 보기 정렬·줄바꿈, C·E는 원문항의 Does + 동사원형 요소를 되살림
def br20(p): return re.sub(r" (?=\([나-마]\) )", "\n", p)
for t, (o, nw) in {"B": ("④", "③"), "D": ("②", "④"), "F": ("②", "④")}.items():
    F(2, 20, t, p=br20(V(2, 20, t)["passage"]), op="sortc", s=f"개수 선택지를 1개~5개 순으로 정렬(정답 {o}→{nw})하고, 한 줄로 이어 쓴 (가)~(마)를 한 줄에 한 문장씩 나눴다.")
R20 = "현재완료는 현재와 연결된 기간·결과·완료를 나타낸다. yesterday·last night·ago처럼 끝난 과거 시점이나 때를 묻는 when 의문문에는 단순과거를 쓴다. do/does/did 뒤 본동사는 원형이다."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]
F(2, 20, "C", p="(가) She has seen him last Monday.\n(나) Does he always walks to school?\n(다) Tom has worked here since May.\n(라) I have already eaten.\n(마) When have you called her yesterday?",
  c=CNT5, a=2, r=R20, pre=["문장별 판정: (가) X. 끝난 과거 시점(last Monday)에는 단순과거를 쓴다. 교정문: She saw him last Monday.",
                           "문장별 판정: (나) X. 조동사(Does) 뒤의 본동사는 원형이어야 한다. 교정문: Does he always walk to school?",
                           "문장별 판정: (다) O. 5월부터 지금까지(since May) 일해 온 기간이므로 현재완료(has worked)가 맞다.",
                           "문장별 판정: (라) O. 이미 먹었다는 완료를 현재완료(have already eaten)로 나타냈다.",
                           "문장별 판정: (마) X. 과거 시점(yesterday)의 때를 묻는 의문문에는 현재완료를 쓰지 않는다. 교정문: When did you call her yesterday?"],
  k="옳은 문장은 (다), (라)로 2개이다.", n="cnt",
  s="개수 선택지 순서가 뒤섞여 1개~5개 순으로 정렬했다. 원문항의 ‘Does + 주어 + -s 동사’ 오류가 빠져 있어 (나)를 ‘Does he always walks …’로 바꿔 이 문법 요소를 되살렸다(옳은 문장 2개). 문장마다 줄을 바꿨다. 정답 위치 ②.")
F(2, 20, "E", p="(가) Tom has bought the bike yesterday.\n(나) Does your sister works here?\n(다) I have known her since 2020.\n(라) We have come back an hour ago.\n(마) When have they left this morning?",
  c=CNT5, a=1, r=R20, pre=["문장별 판정: (가) X. 끝난 과거 시점(yesterday)에는 단순과거를 쓴다. 교정문: Tom bought the bike yesterday.",
                           "문장별 판정: (나) X. 조동사(Does) 뒤의 본동사는 원형이어야 한다. 교정문: Does your sister work here?",
                           "문장별 판정: (다) O. 2020년부터 지금까지(since 2020) 알고 지낸 상태이므로 현재완료(have known)가 맞다.",
                           "문장별 판정: (라) X. 끝난 과거 시점(an hour ago)에는 단순과거를 쓴다. 교정문: We came back an hour ago.",
                           "문장별 판정: (마) X. 때를 묻는 when 의문문에는 현재완료를 쓰지 않는다. 교정문: When did they leave this morning?"],
  k="옳은 문장은 (다) 하나뿐이므로 1개이다.", n="cnt",
  s="개수 선택지 순서가 뒤섞여 1개~5개 순으로 정렬했다. 원문항의 ‘Does + 주어 + -s 동사’ 오류가 빠져 있어 (나)를 ‘Does your sister works …’로 바꾸고, 다른 유형과 정답 개수가 겹치지 않게 (라)를 ‘have come back an hour ago’로 바꿨다(옳은 문장 1개). 문장마다 줄을 바꿨다. 정답 위치 ①.")

# ---- 2차 감수(2026-10) 추가 ----
# 2-11 B~F: 없는 형태·수 불일치 오답 → 원문항처럼 형태는 바르고 시제만 틀린 오답으로
R11 = "yesterday, last ~처럼 끝난 과거 시점에는 과거형을 쓰고, since ~, for ~ now처럼 과거부터 지금까지 이어지는 기간에는 현재완료(have/has + 과거분사)를 쓴다."
S11 = "오답이 없는 형태이거나 주어와 수가 맞지 않아 시제를 따지지 않고도 지워졌다. 원문항처럼 형태는 바르고 시제만 틀린 오답으로 바꿨다."
def f11(t, c, a, w1, w2, p=None, extra=""):
    past, perf = c[a - 1].split(" — ")
    def note(x):
        l, r = x.split(" — ")
        if l == past and r == perf: return f"{w1}에는 과거형({past}), {w2}에는 현재완료({perf})를 쓰므로"
        if l != past and r != perf: return f"두 빈칸 모두 시제가 맞지 않으므로"
        if l != past: return f"끝난 과거 시점({w1})과 현재완료({l})를 함께 쓸 수 없으므로"
        return f"지금까지 이어지는 기간({w2})에는 {r}이(가) 아니라 현재완료를 써야 하므로"
    mk(2, 11, t, [(x, note(x)) for x in c], a, R11, S11 + extra, **({"p": p} if p else {}))
f11("B", ["ran into — haven't talked to", "ran into — didn't talk to", "ran into — don't talk to", "have run into — haven't talked to", "have run into — didn't talk to"], 1, "last Monday", "since last winter",
    p="A: I _____ Jisoo at the library last Monday.\nB: Really? I _____ her since last winter.", extra=" 과거형도 쓸 수 있는 for almost a year는 since last winter로 바꿨다.")
f11("C", ["has lost — has used", "lost — used", "lost — has used", "lost — uses", "has lost — used"], 3, "yesterday", "since middle school")
f11("D", ["visited — went", "have visited — have been", "visited — have been", "visited — go", "have visited — went"], 3, "last April", "since I moved here",
    p="A: We _____ the museum last April.\nB: I _____ there twice since I moved here.", extra=" 과거형도 쓸 수 있는 twice this year는 twice since I moved here로 바꿨다.")
f11("E", ["started — worked", "has started — has worked", "started — works", "started — has worked", "has started — worked"], 4, "last month", "for four weeks now")
f11("F", ["have finished — have loved", "finished — loved", "finished — love", "finished — have loved", "have finished — loved"], 4, "during the last vacation", "since I was in middle school",
    p="A: I _____ this novel during the last vacation.\nB: Oh, I _____ that novel since I was in middle school.", extra=" 과거형·진행형도 쓸 수 있는 yet 문장은 since가 있는 문장으로 바꿨다.")

# 2-14 B~F: 오답 대화의 대답이 토막이라 정답만 드러남 → 모든 대답을 완전한 문장으로, 한 줄 대화로
R14 = "현재완료는 ago, yesterday, last night, at noon처럼 끝난 과거 시점을 나타내는 말이나 When did ~?에 대한 대답에 쓸 수 없다. 이때는 과거형을 쓴다."
S14 = "오답 대화의 대답이 ‘At nine.’, ‘Yes.’ 같은 토막이라 시제를 따질 수 있는 대답이 정답뿐이었다. 원문항처럼 모든 대답을 완전한 문장으로 쓰고, 두 줄로 나뉜 대화를 원문항처럼 한 줄로 했다."
OK14 = {"exp": "경험을 현재완료로 묻고 답해 올바르므로", "dur": "지금까지의 기간을 현재완료로 묻고 답해 올바르므로", "now": "지금 하는 일을 현재진행형으로 묻고 답해 올바르므로", "fut": "앞으로의 일을 will로 묻고 답해 올바르므로",
        "past": "과거의 일을 과거형으로 묻고 답해 올바르므로", "done": "완료 여부를 현재완료로 묻고 답해 올바르므로"}
def f14(t, items, a, bad):
    mk(2, 14, t, [(x, bad if i + 1 == a else OK14[w]) for i, (x, w) in enumerate(items)], a, R14, S14)
f14("B", [("A: Will you join us for lunch tomorrow? B: Yes, I will. I'd love to.", "fut"), ("A: What is your sister doing now? B: She is practicing the piano.", "now"),
          ("A: When did you submit the report? B: I have submitted it two hours ago.", ""), ("A: How long have you known Mr. Kim? B: I have known him for eight years.", "dur"),
          ("A: Have you ever tried Thai food? B: Yes, I have tried it twice.", "exp")], 3, "two hours ago라는 과거 시점과 현재완료를 함께 쓸 수 없다. I submitted it two hours ago.로 써야 하므로")
f14("C", [("A: When did Jane leave the office? B: She has left at noon.", ""), ("A: Have you finished your science project yet? B: Yes, I have just finished it.", "done"),
          ("A: How long has she worked at the bank? B: She has worked there since May.", "dur"), ("A: When did you arrive at the hotel? B: I arrived at nine last night.", "past"),
          ("A: Are you reading the newspaper now? B: No, I am watching the news.", "now")], 1, "at noon이라는 과거 시점과 현재완료를 함께 쓸 수 없다. She left at noon.으로 써야 하므로")
f14("D", [("A: Did you see the game last night? B: Yes, I have seen it last night.", ""), ("A: What will you do this weekend? B: I will visit my grandparents.", "fut"),
          ("A: When did Jane come back from Canada? B: She came back yesterday.", "past"), ("A: How long has your brother played tennis? B: He has played it for three years.", "dur"),
          ("A: Have they ever been to Jeju? B: Yes, they have been there several times.", "exp")], 1, "last night이라는 과거 시점과 현재완료를 함께 쓸 수 없다. I saw it last night.으로 써야 하므로")
f14("E", [("A: When did the class end? B: It ended at three o'clock.", "past"), ("A: Have you eaten dinner yet? B: No, I haven't eaten anything yet.", "done"),
          ("A: How long has Tom lived in this town? B: He has lived here since 2020.", "dur"), ("A: Are they waiting for the bus? B: Yes, they are waiting at the stop.", "now"),
          ("A: When did Tom call you? B: He has called me yesterday.", "")], 5, "yesterday라는 과거 시점과 현재완료를 함께 쓸 수 없다. He called me yesterday.로 써야 하므로")
f14("F", [("A: Have you seen this movie before? B: Yes, I have seen it twice.", "exp"), ("A: How long have you studied English? B: I have studied it for six years.", "dur"),
          ("A: Will Jane come to the meeting? B: Yes, she will come after lunch.", "fut"), ("A: Did they arrive on Monday? B: Yes, they have arrived on Monday.", ""),
          ("A: When did your cousins leave? B: They left on Tuesday morning.", "past")], 4, "on Monday라는 과거 시점과 현재완료를 함께 쓸 수 없다. They arrived on Monday.로 써야 하므로")

# 2-18 B~F: 발문을 원문항과 같게(옳은 문장으로만 짝지어진 것), 옳은 문장 둘 + 두 문장 조합 보기
R18b = "미래의 시간·조건을 나타내는 부사절(when, after, until, if, unless 등)에서는 미래의 일도 현재형으로 쓴다."
S18b = "원문항처럼 옳은 문장이 둘이 되게 하고 보기를 모두 두 문장 조합으로 맞춰, 발문을 원문항과 같게 했다(괄호 조건 삭제). 정답 조합은 원문항((A), (C))과 겹치지 않게 했다. 문장마다 줄을 바꿨다."
def f18(t, sents, c, a, extra=""):
    L = "ABCD"
    ok = ", ".join(f"({L[i]})" for i, (_, o, _) in enumerate(sents) if o)
    FIX.pop((2, 18, t), None)
    F(2, 18, t, st="R", p="\n".join(f"({L[i]}) {x}" for i, (x, _, _) in enumerate(sents)), c=c, a=a, r=R18b,
      pre=[f"문장별 판정: ({L[i]}) {'O' if o else 'X'}. {w}" for i, (_, o, w) in enumerate(sents)],
      k=f"옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), s=S18b + extra + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f18("B", [("If it <u>will rain</u> tomorrow, we'll cancel the picnic.", 0, "조건 부사절(if)에는 현재형을 쓴다: will rain → rains."), ("I'll message you when I <u>get</u> home.", 1, "시간 부사절(when)에서 현재형으로 미래를 나타냈다."),
          ("We won't leave until Dad <u>will finish</u> his call.", 0, "시간 부사절(until)에는 현재형을 쓴다: will finish → finishes."), ("We'll start after everyone <u>arrives</u>.", 1, "시간 부사절(after)에서 현재형으로 미래를 나타냈다.")],
    ["(B), (D)", "(A), (B)", "(A), (C)", "(B), (C)", "(C), (D)"], 1)
f18("C", [("If Jane <u>will be</u> free, she will join us.", 0, "조건 부사절(if)에는 현재형을 쓴다: will be → is."), ("She will call you when the meeting <u>will end</u>.", 0, "시간 부사절(when)에는 현재형을 쓴다: will end → ends."),
          ("I'll wait here until the bus <u>comes</u>.", 1, "시간 부사절(until)에서 현재형으로 미래를 나타냈다."), ("Let's go out after the rain <u>stops</u>.", 1, "시간 부사절(after)에서 현재형으로 미래를 나타냈다.")],
    ["(A), (C)", "(B), (C)", "(A), (D)", "(C), (D)", "(B), (D)"], 4)
f18("D", [("I'll tell you if I <u>find</u> it.", 1, "조건 부사절(if)에서 현재형으로 미래를 나타냈다."), ("We will leave when Tom <u>will get</u> here.", 0, "시간 부사절(when)에는 현재형을 쓴다: will get → gets."),
          ("If it <u>will snow</u>, school will close.", 0, "조건 부사절(if)에는 현재형을 쓴다: will snow → snows."), ("I'll stay until the movie <u>ends</u>.", 1, "시간 부사절(until)에서 현재형으로 미래를 나타냈다.")],
    ["(C), (D)", "(B), (C)", "(A), (D)", "(A), (C)", "(A), (B)"], 3)
f18("E", [("When Jane <u>finishes</u>, we'll go.", 1, "시간 부사절(when)에서 현재형으로 미래를 나타냈다."), ("If the weather <u>is</u> good, we'll hike.", 1, "조건 부사절(if)에서 현재형으로 미래를 나타냈다."),
          ("I'll call after I <u>will arrive</u>.", 0, "시간 부사절(after)에는 현재형을 쓴다: will arrive → arrive."), ("We won't start until everyone <u>will come</u>.", 0, "시간 부사절(until)에는 현재형을 쓴다: will come → comes.")],
    ["(B), (C)", "(A), (B)", "(A), (D)", "(C), (D)", "(A), (C)"], 2)
f18("F", [("If he <u>will be</u> late, we'll start without him.", 0, "조건 부사절(if)에는 현재형을 쓴다: will be → is."), ("I'll text you when I <u>reach</u> the station.", 1, "시간 부사절(when)에서 현재형으로 미래를 나타냈다."),
          ("We'll eat after Mom <u>gets</u> home.", 1, "시간 부사절(after)에서 현재형으로 미래를 나타냈다."), ("Unless it <u>will rain</u>, we'll play outside.", 0, "조건 부사절(unless)에는 현재형을 쓴다: will rain → rains.")],
    ["(A), (B)", "(A), (C)", "(C), (D)", "(B), (D)", "(B), (C)"], 5)

# 2-19 B: 정답만 ‘(A)는 …, (B)는 …’ 꼴의 긴 설명 → 오답도 같은 꼴로, <보기> 표시
mk(2, 19, "B", [("(A)는 과거의 일이 현재까지 영향을 미치는 현재완료이고, (B)는 과거의 사건만을 말하는 과거 시제이다.", "(A)가 과거 시제, (B)가 현재완료인데 거꾸로 설명했으므로"),
                ("(A)는 오늘 아침에 일어난 과거의 사건 자체를 말하고, (B)는 그 결과 지금 우산이 없는 상태임을 나타낸다.", "(A)의 단순과거는 과거 사건을, (B)의 현재완료는 그 결과가 지금까지 이어짐을 나타낸다는 차이를 바르게 설명했으므로"),
                ("(A)는 this morning이 있어 어법상 틀린 문장이고, (B)만 올바른 문장이다.", "과거 시점 표현 this morning은 과거형과 함께 쓰는 올바른 표현이므로"),
                ("(A)와 (B)는 형태만 다를 뿐 나타내는 뜻에는 아무 차이가 없다.", "(B)만 지금도 우산이 없다는 현재의 결과를 나타내므로"),
                ("(A)는 우산을 여러 번 두고 내린 경험을 나타내고, (B)는 지금 두고 내리는 중임을 나타낸다.", "(A)는 한 번의 과거 사건이고 (B)는 진행형이 아니므로")], 2, R19,
   "정답만 ‘(A)는 …, (B)는 …’ 꼴의 긴 설명이고 오답은 짧은 한 줄이라 형식으로 답이 드러났다. 지문에 없는 yesterday를 말하는 오답도 있었다. 원문항처럼 다섯 보기를 모두 두 문장을 견주는 설명으로 다시 쓰고, 본문에 <보기> 표시를 넣었다.", p=P19("B"))
