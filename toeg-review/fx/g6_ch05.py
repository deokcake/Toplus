# 6급 CH5 일반동사 과거형 (41~50) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 원문항 발문으로만 되돌리는 문항
for t in "BCDEF": F(6, 42, t, st="R", s="발문에 ‘과거의 일을 나타내도록’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDEF": F(6, 45, t, st="R", xr=[("과거를 나타내는 조건에 맞지 않는다.", "과거를 나타내는 문장이 될 수 없다.")] if t in "DE" else [], s="발문이 ‘원문의 뜻을 유지하면서, 시간 표현까지 과거의 일에 맞게 바꾼 문장’으로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDEF": F(6, 46, t, st="R", s="발문에 ‘과거의 일을 나타내도록’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDEF": F(6, 47, t, st="R", s="발문이 ‘우리말의 부정 의미와 시간 정보를 빠짐없이 나타낸 문장’으로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDEF": F(6, 48, t, st="R", xr=[("과거진행형 질문으로 바뀌어 단순과거 긍정 의문문이라는 조건 및 did로 답하는 대화와 다르다.", "과거진행형 질문으로 바뀌어 did로 답하는 대화와 맞지 않는다.")] if t == "D" else [], s="발문이 ‘과거의 긍정 의문문이 되도록’이라고 알려 주어 Do/Does·Did not으로 시작하는 오답이 바로 지워졌다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 6-43 두 빈칸: 원문항 발문, 둘째 문장에도 과거 시간 표현
S643 = "발문에 ‘두 문장을 모두 과거의 일로 완성하도록’이 붙었고, 둘째 문장에 시간 표현이 없어 발문 조건에 기대야 시제가 정해졌다. 원문항 발문으로 되돌리고 둘째 문장에 과거 시간 표현을 넣었다. 보기와 정답은 그대로다."
for t, p in [("B", "- They _______ arrive on time yesterday.\n- Jane _______ the window before class yesterday."), ("C", "She _______ watch TV yesterday.\nTom _______ his room last night."),
             ("D", "- We _______ watch the movie last night.\n- Mina _______ the door for her grandma an hour ago."), ("E", "They _______ visit us last week.\nMy dad _______ dinner last Sunday."),
             ("F", "I _______ read the book yesterday.\nShe _______ the box last night.")]:
    F(6, 43, t, st="R", p=p, s=S643)

# 6-50 옳은 문장: 원문항과 다른 철자 오류, 눈에 띄지 않는 정답 문장
R650 = "규칙 과거형은 -ed를 붙이고, -e로 끝나면 -d만(hoped, danced), 자음 + y는 y를 i로 바꾸고 -ed(cried, worried), 강세 있는 단모음 + 단자음은 자음을 겹쳐 -ed(planned, shopped)를 붙인다. w·x로 끝나거나 모음 두 개 뒤의 자음, 강세가 앞에 있는 visit·open·listen은 겹쳐 쓰지 않으며, pay의 과거형은 paid이다."
S650 = "오답 네 개가 원문항의 철자 오류(rainned, studyed, droped, carryed)를 그대로 썼고, 정답이 원문항처럼 ‘X and I + 부사 + 과거형 + yesterday’ 구조의 긴 문장이라 눈에 띄었다. 원문항과 다른 철자 오류로 오답을 새로 쓰고, 정답도 다른 문장과 길이가 비슷한 짧은 문장으로 바꿨다."
def f650(t, items, a, s=S650):
    mk(6, 50, t, items, a, R650, s)
f650("B", [("We waitted for the bus.", "wait는 모음 두 개(ai) 뒤의 자음이라 겹쳐 쓰지 않고 waited로 써야 하므로"), ("Mina enjoied the concert.", "enjoy는 모음 + y라 y를 그대로 두고 enjoyed로 써야 하므로"), ("Tom visitted his aunt.", "visit는 강세가 앞 음절에 있어 t를 겹쳐 쓰지 않고 visited로 써야 하므로"),
           ("The kids clapped their hands.", "clap은 단모음 + 단자음이라 p를 겹쳐 clapped로 바르게 썼으므로"), ("I openned the window.", "open은 강세가 앞 음절에 있어 n을 겹쳐 쓰지 않고 opened로 써야 하므로")], 4)
f650("C", [("She hoped to win the game.", "hope는 -e로 끝나 -d만 붙여 hoped로 바르게 썼으므로"), ("They danceed at the party.", "dance는 -e로 끝나 -d만 붙여 danced로 써야 하므로"), ("He shoped for shoes.", "shop은 단모음 + 단자음이라 p를 겹쳐 shopped로 써야 하므로"),
           ("I listenned to music.", "listen은 강세가 앞 음절에 있어 n을 겹쳐 쓰지 않고 listened로 써야 하므로"), ("Dad fixxed the chair.", "x는 겹쳐 쓰지 않으므로 fixed로 써야 하므로")], 1)
f650("D", [("The baby cryed all night.", "cry는 자음 + y라 y를 i로 바꾸고 cried로 써야 하므로"), ("We joged in the park.", "jog는 단모음 + 단자음이라 g를 겹쳐 jogged로 써야 하므로"), ("My dad worried about me.", "worry는 자음 + y라 y를 i로 바꾸고 worried로 바르게 썼으므로"),
           ("Jane hurryed to school.", "hurry는 자음 + y라 y를 i로 바꾸고 hurried로 써야 하므로"), ("He liveed in Busan.", "live는 -e로 끝나 -d만 붙여 lived로 써야 하므로")], 3)
f650("E", [("She payed for the tickets.", "pay의 과거형은 불규칙형 paid이므로"), ("We planed a trip.", "plan은 단모음 + 단자음이라 n을 겹쳐 planned로 써야 하므로"), ("He rubed his eyes.", "rub은 단모음 + 단자음이라 b를 겹쳐 rubbed로 써야 하므로"),
           ("They stoped the car.", "stop은 단모음 + 단자음이라 p를 겹쳐 stopped로 써야 하므로"), ("The dog chased the ball.", "chase는 -e로 끝나 -d만 붙여 chased로 바르게 썼으므로")], 5)
f650("F", [("I tryed my best.", "try는 자음 + y라 y를 i로 바꾸고 tried로 써야 하므로"), ("The girls smiled at me.", "smile은 -e로 끝나 -d만 붙여 smiled로 바르게 썼으므로"), ("Tom chated with friends.", "chat은 단모음 + 단자음이라 t를 겹쳐 chatted로 써야 하므로"),
           ("We copyed the notes.", "copy는 자음 + y라 y를 i로 바꾸고 copied로 써야 하므로"), ("It snowwed a lot.", "w는 겹쳐 쓰지 않으므로 snowed로 써야 하므로")], 2)


# ---- 2차 감수(2026-10) 추가 ----
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
R_PAST = "과거의 일은 동사의 과거형으로 쓴다. 규칙동사는 -ed를 붙이고(자음 + y는 -ied, 단모음 + 단자음은 자음을 겹쳐 -ed), 부정문은 didn't + 동사원형, 의문문은 Did + 주어 + 동사원형 ~?으로 쓴다."
def redo(n, t, items, a, s, **kw):
    FIX.pop((6, n, t), None)
    mk(6, n, t, items, a, kw.pop("r", R_PAST), s, st="R", **kw)
# 6-41 F: 정답 짝(plan - planed)이 C와 같고, cry - cried는 원문항 정답을 바르게 고친 짝
mk(6, 41, "F", [("wash - washed", "-ed를 붙인 옳은 형태이므로"), ("stop - stopped", "단모음 + 단자음이라 p를 겹쳐 쓴 옳은 형태이므로"), ("skip - skiped", "단모음 + 단자음이라 p를 겹쳐 skipped로 써야 하므로"), ("try - tried", "자음 + y라 y를 i로 바꾸고 -ed를 붙인 옳은 형태이므로"), ("open - opened", "강세가 앞에 있어 n을 겹쳐 쓰지 않은 옳은 형태이므로")], 3,
   "규칙 과거형은 -ed를 붙인다. 자음 + y는 y를 i로 바꾸고 -ed(cried, tried), 강세 있는 단모음 + 단자음으로 끝나면 자음을 겹쳐 -ed(stopped, planned)를 붙인다.",
   "정답 짝(plan - planed)이 C와 똑같았고, ④(cry - cried)는 원문항 정답(cry - cryed)을 바르게 고친 짝이었다. 두 짝을 다른 동사로 바꿨다. 정답 위치는 그대로다.")
# 6-42 E: 같은 단원 46번 원문항(She ___ a movie last night. — watched)과 거의 같음
redo(42, "E", [("cooks", "last night이 있어 현재형을 쓸 수 없으므로"), ("did cooked", "did와 과거형을 함께 쓸 수 없으므로"), ("cooked", "last night에 맞는 과거형이므로"), ("cook", "last night이 있어 현재형을 쓸 수 없고 주어 She와도 맞지 않으므로"), ("cooking", "be동사 없이 -ing형만 쓸 수 없으므로")], 3,
     "발문에 ‘과거의 일을 나타내도록’이 붙었고, 문장과 정답(She ___ TV last night. — watched)이 같은 단원 46번 원문항(She ___ a movie last night. — watched)과 거의 같았다. 원문항 발문으로 되돌리고 동사를 바꿨다.", p="She _______ dinner last night.")
# 6-43 C·E·F: 원문항처럼 문장 앞에 ‘-’ / D·F: 정답(didn't - opened)이 B와 같음
for _t in "CE":
    FIX[(6, 43, _t)]["p"] = "\n".join("- " + x for x in FIX[(6, 43, _t)]["p"].split("\n"))
    FIX[(6, 43, _t)]["s"] = S643.replace(" 보기와 정답은 그대로다.", " 원문항처럼 두 문장 앞에 ‘-’를 붙였다. 보기와 정답은 그대로다.")
S643B = "발문에 ‘두 문장을 모두 과거의 일로 완성하도록’이 붙었고, 정답(didn't - opened)이 B와 똑같았다. 원문항 발문으로 되돌리고 둘째 문장의 동사를 바꿔 정답이 겹치지 않게 했다. 둘째 문장에는 과거 시간 표현을 넣었다."
redo(43, "D", [("didn't - closed", "과거 부정 didn't와 과거형 closed를 바르게 짝지었으므로"), ("doesn't - closed", "last night이 있어 doesn't를 쓸 수 없고 주어 We와도 맞지 않으므로"), ("weren't - closed", "일반동사 watch의 부정에 weren't를 쓸 수 없으므로"), ("don't - closed", "last night이 있어 don't를 쓸 수 없으므로"), ("didn't - close", "an hour ago가 있어 과거형 closed를 써야 하므로")], 1, S643B,
     p="- We _______ watch the movie last night.\n- Mina _______ the door for her grandma an hour ago.")
redo(43, "F", [("didn't - washes", "last night이 있어 현재형 washes를 쓸 수 없으므로"), ("don't - washed", "yesterday가 있어 don't를 쓸 수 없으므로"), ("didn't - wash", "last night이 있어 과거형 washed를 써야 하므로"), ("doesn't - washed", "yesterday가 있어 doesn't를 쓸 수 없고 주어 I와도 맞지 않으므로"), ("didn't - washed", "과거 부정 didn't와 과거형 washed를 바르게 짝지었으므로")], 5, S643B + " 원문항처럼 두 문장 앞에 ‘-’도 붙였다.",
     p="- I _______ read the book yesterday.\n- She _______ the dishes last night.")
# 6-45 F: 정답에만 to work가 있음 → 모든 보기에 넣음
redo(45, "F", [("She takes the subway to work yesterday.", "yesterday가 있는데 현재형 takes를 썼으므로"), ("She did took the subway to work yesterday.", "did와 과거형 took을 함께 쓸 수 없으므로"), ("She taked the subway to work yesterday.", "take의 과거형은 불규칙형 took이므로"),
     ("She take the subway to work yesterday.", "과거형이 아니고 주어 She와도 맞지 않으므로"), ("She took the subway to work yesterday.", "take의 과거형 took을 바르게 썼으므로")], 5,
     "발문이 원문항과 달랐고, 오답 네 개에는 원문에 있는 to work가 빠져 있어 정답만 문장이 온전했다. 원문항 발문으로 되돌리고 모든 보기에 to work를 넣었다. 정답은 그대로다.")
# 6-46 C~F: 같은 단원 42번(원문항·변형)과 문장·정답이 겹침, B와 F는 정답 낱말(cleaned)도 같음
S646 = "발문에 ‘과거의 일을 나타내도록’이 붙었고, 문장과 정답이 같은 단원의 다른 문항(%s)과 거의 같았다. 원문항 발문으로 되돌리고 동사를 바꿨다."
def f646(t, p, base, past, a, dup, order):
    its = {"past": (past, "과거의 때를 나타내는 말에 맞는 과거형이므로"), "base": (base, "과거의 때를 나타내는 말이 있어 현재형을 쓸 수 없으므로"), "s": (base + ("es" if base.endswith(("s", "sh", "ch", "x")) else "s"), "과거의 때를 나타내는 말이 있어 현재형을 쓸 수 없으므로"),
           "ing": ((base[:-1] if base.endswith("e") else base) + "ing", "be동사 없이 -ing형만 쓸 수 없으므로"), "did": ("did " + past, "did와 과거형을 함께 쓸 수 없으므로")}
    redo(46, t, [its[k] for k in order], a, S646 % dup, p=p)
f646("C", "They ________ at the party last night.", "dance", "danced", 3, "42번 D: They ___ English yesterday. — studied", ["base", "ing", "past", "did", "s"])
f646("D", "Jane ________ her aunt yesterday.", "call", "called", 2, "42번 F: Tom ___ his uncle last week. — visited", ["ing", "past", "base", "did", "s"])
f646("E", "Tom ________ to the radio yesterday.", "listen", "listened", 2, "42번 원문항: I ___ the violin yesterday. — played", ["base", "past", "s", "ing", "did"])
f646("F", "We ________ the wall last week.", "paint", "painted", 4, "42번 B: We ___ the room yesterday. — cleaned, 46번 B의 정답도 cleaned", ["ing", "did", "s", "past", "base"])
# 6-47 C~F: 원문항 발문으로 되돌리면 때를 나타내는 말만 빠진 옳은 문장이 정답과 헷갈림 → 분명히 틀린 문장으로 / F는 B와 거의 같은 문장
S647 = "발문이 ‘우리말의 부정 의미와 시간 정보를 빠짐없이 나타낸 문장’으로 바뀌었다. 원문항 발문으로 되돌리면 때를 나타내는 말만 빠진 옳은 문장(%s)이 정답과 헷갈릴 수 있어, 분명히 틀린 문장으로 바꿨다."
redo(47, "C", [("Jane didn't go to school last week.", "didn't + 동사원형 go로 과거 부정을 바르게 나타냈으므로"), ("Jane doesn't go to school last week.", "last week가 있어 doesn't를 쓸 수 없으므로"), ("Jane didn't went to school last week.", "didn't 뒤에는 동사원형 go를 써야 하므로"),
     ("Jane weren't go to school last week.", "일반동사 go의 부정에 weren't를 쓸 수 없으므로"), ("Jane go to school last week.", "부정문이 아니고 과거형도 아니므로")], 1, S647 % "Jane didn't go to school." + " 정답은 그대로다.")
redo(47, "D", [("They study English yesterday.", "부정문이 아니고 과거형도 아니므로"), ("They doesn't study English yesterday.", "yesterday가 있어 doesn't를 쓸 수 없고 주어 They와도 맞지 않으므로"), ("They didn't studied English yesterday.", "didn't 뒤에는 동사원형 study를 써야 하므로"),
     ("They didn't study English yesterday.", "didn't + 동사원형 study로 과거 부정을 바르게 나타냈으므로"), ("They weren't study English yesterday.", "일반동사 study의 부정에 weren't를 쓸 수 없으므로")], 4, S647 % "They didn't study English." + " 정답은 그대로다.")
redo(47, "E", [("Tom play soccer yesterday.", "부정문이 아니고 과거형도 아니므로"), ("Tom weren't play soccer yesterday.", "일반동사 play의 부정에 weren't를 쓸 수 없으므로"), ("Tom didn't played soccer yesterday.", "didn't 뒤에는 동사원형 play를 써야 하므로"),
     ("Tom doesn't play soccer yesterday.", "yesterday가 있어 doesn't를 쓸 수 없으므로"), ("Tom didn't play soccer yesterday.", "didn't + 동사원형 play로 과거 부정을 바르게 나타냈으므로")], 5, S647 % "Tom didn't play soccer." + " 정답은 그대로다.")
redo(47, "F", [("We didn't visited our grandma last weekend.", "didn't 뒤에는 동사원형 visit을 써야 하므로"), ("We visit our grandma last weekend.", "부정문이 아니고 과거형도 아니므로"), ("We doesn't visit our grandma last weekend.", "last weekend가 있어 doesn't를 쓸 수 없고 주어 We와도 맞지 않으므로"),
     ("We didn't visit our grandma last weekend.", "didn't + 동사원형 visit으로 과거 부정을 바르게 나타냈으므로"), ("We weren't visit our grandma last weekend.", "일반동사 visit의 부정에 weren't를 쓸 수 없으므로")], 4,
     "발문이 원문항과 달랐고, 우리말과 정답(우리는 어젯밤 TV를 보지 않았다)이 B(Tom은 어젯밤 TV를 보지 않았다)와 주어만 달랐다. 원문항 발문으로 되돌리고 문장을 새로 썼으며, 때를 나타내는 말만 빠진 옳은 문장도 분명히 틀린 문장으로 바꿨다.", p="우리는 지난 주말에 할머니를 방문하지 않았다.")
