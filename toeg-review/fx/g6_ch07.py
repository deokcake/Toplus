# 6급 CH7 조동사 can·may·must·have to (61~70) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def talk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 옳지 않은 설명이다. 따라서 정답이다." if i + 1 == a else " 옳은 설명이다. 따라서 오답이다.")) if w.endswith("므로") else (w + (" 옳지 않은 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.")) for i, (_, w) in enumerate(items)], k=items[a-1][1], s=s + ipos(a), **kw)
R_MD = "조동사 can(능력·허락), may(허락·추측), must(의무·강한 추측), should(충고) 뒤에는 주어와 관계없이 동사원형을 쓰고, 조동사 자체에는 -s를 붙이지 않는다."

# 원문항 발문으로만 되돌리는 문항
for t in "BCDEF": F(6, 61, t, st="R", xr=[("must는 이 문항에서 의무를", "must는 여기서 의무를")] + ([("뒤에 이 문항의 동사원형을", "뒤에 동사원형을")] if t in "BDEF" else []), s="발문에 ‘우리말의 의무 의미와 일치하도록’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDEF": F(6, 62, t, st="R", s="발문에 ‘허락을 나타내는 우리말과 뜻이 일치하고, 문장 형태도 올바른’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDEF": F(6, 63, t, st="R", s="발문에 ‘문장 형태가 올바르고 ~해야 한다라는 뜻을 유지하는’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDE": F(6, 65, t, st="R", s="발문에 ‘현재의 능력을 같은 뜻으로 나타내도록’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BDEF": F(6, 68, t, st="R", s="발문에 ‘현재의 능력을 같은 뜻으로 나타내도록’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 6-64 조동사 밑줄: 여러 조동사를 섞어 유형마다 새로
S664 = "원문항은 여러 조동사(may, can, must, should) 뒤 형태를 판별하는데, 변형은 모두 may 문장이라 범위가 좁았고 오답 네 개가 B와 똑같았다. 여러 조동사를 섞어 유형마다 새로 썼다."
OK64 = "조동사 뒤에 동사원형을 바르게 썼으므로"
def f664(t, items, a, s=S664):
    mk(6, 64, t, [(x, w or OK64) for x, w in items], a, R_MD, s)
f664("B", [("Tom <u>can swim</u> well.", ""), ("They <u>may are</u> busy.", "may 뒤에는 be동사의 원형 be를 써야 하므로"), ("We <u>must wear</u> a helmet.", ""), ("She <u>should go</u> to bed early.", ""), ("You <u>may sit</u> here.", "")], 2,
     "선택지가 모두 may 문장이라 원문항보다 범위가 좁았다. can, must, should 문장을 섞어 새로 썼다.")
f664("C", [("She <u>cans</u> play the violin.", "조동사 can에는 -s를 붙이지 않으므로"), ("We <u>should listen</u> to our teacher.", ""), ("You <u>may take</u> a cookie.", ""), ("I <u>must go</u> now.", ""), ("He <u>can ride</u> a horse.", "")], 1)
f664("D", [("You <u>should wash</u> your hands.", ""), ("I <u>may be</u> late today.", ""), ("Tom <u>can plays</u> the drums.", "can 뒤에는 동사원형 play를 써야 하므로"), ("We <u>must stop</u> at the red light.", ""), ("They <u>may visit</u> us.", "")], 3)
f664("E", [("My dad <u>can fix</u> the car.", ""), ("You <u>must not run</u> here.", "must not 뒤에 동사원형을 바르게 썼으므로"), ("It <u>may snow</u> tonight.", ""), ("She <u>should to join</u> us.", "should 뒤에는 to 없이 동사원형 join을 써야 하므로"), ("We <u>should save</u> water.", "")], 4)

# 6-65 F: E와 같은 주어(They)를 바꿈
F(6, 65, "F", st="R", p="You and Tom can swim well.\n= You and Tom ________ able to swim well.", r="현재의 능력을 뜻하는 can은 주어에 맞는 am/is/are able to로 바꿀 수 있다.",
  n=["be는 원형이라 주어 뒤에 그대로 쓸 수 없으므로 오답이다.", "복수 주어 You and Tom에 맞는 are를 썼으므로 정답이다.", "can 뒤에 able to를 이어 쓸 수 없으므로 오답이다.", "am은 주어 I에만 쓰므로 오답이다.", "is는 3인칭 단수 주어에 쓰므로 오답이다."],
  s="발문에 ‘현재의 능력을 같은 뜻으로 나타내도록’이 붙었고, 주어(They)와 정답(are)이 E와 같았다. 원문항 발문으로 되돌리고 주어를 You and Tom으로 바꿨다. 정답 위치 ②.")

# 6-66 B: 원문항과 거의 같은 제시 문장을 새로
F(6, 66, "B", p="My uncle may ________ us this weekend.", c=["visiting", "visits", "to visit", "is visit", "visit"], a=5, r="추측·허락의 may 뒤에는 주어와 관계없이 동사원형을 쓴다.",
  n=["may 뒤에는 -ing형을 쓸 수 없으므로 오답이다.", "may 뒤에는 -s형을 쓸 수 없으므로 오답이다.", "may 뒤에는 to 없이 동사원형을 쓰므로 오답이다.", "may 뒤에 be동사와 동사원형을 함께 쓸 수 없으므로 오답이다.", "may 뒤에 동사원형 visit을 바르게 썼으므로 정답이다."],
  s="제시 문장(It may ___ tonight.)이 원문항(It may ___ today.)과 거의 같았다. 제시 문장과 동사를 새로 썼다. 정답 위치 ⑤.")

# 6-68 C: B와 거의 같은 제시문을 새로
F(6, 68, "C", st="R", p="My brother is able to ride a horse.\n= My brother ( __________ ) a horse.", c=["is can ride", "able to ride", "can rides", "can ride", "can riding"], a=4, r="현재의 능력을 나타낼 때 can + 동사원형과 be able to + 동사원형을 바꾸어 쓸 수 있다.",
  n=["can 앞에 be동사를 함께 쓸 수 없으므로 오답이다.", "be동사 없이 able to만으로는 동사 자리를 채울 수 없으므로 오답이다.", "can 뒤에는 동사원형 ride를 써야 하므로 오답이다.", "can + 동사원형 ride로 is able to ride와 같은 뜻을 나타냈으므로 정답이다.", "can 뒤에는 -ing형을 쓸 수 없으므로 오답이다."],
  s="제시문(They are able to swim.)과 정답이 B와 거의 같았고 발문에 조건이 붙었다. 원문항 발문으로 되돌리고 제시문을 새로 썼다. 정답 위치 ④.")

# 6-69 (A)(B) have to 의문문: 원문항처럼 빈칸 밑줄과 (A)/(B) 표기, C·F는 정답 조합을 새로
R669 = "have to의 현재 의문문은 Do/Does + 주어 + have to + 동사원형?으로 쓰고, 3인칭 단수 주어의 긍정문에는 has to를 쓴다. Does 뒤에는 has가 아니라 have를 쓴다."
S669 = "빈칸 밑줄이 사라지고 선택지 표기가 원문항과 달랐다. 원문항처럼 빈칸 밑줄과 (A)/(B) 표기를 되살렸다."
BL = lambda x: f"(<u>    {x}    </u>)"
def f669(t, p, items, a, s=S669 + " 보기와 정답은 그대로다."):
    mk(6, 69, t, items, a, R669, s, p=p, okdup=True)
L = lambda a_, b_: f"(A): {a_}\t(B): {b_}"
f669("B", f"A: {BL('A')} you {BL('B')} wear this?\nB: Yes, I do.", [(L("Does", "has to"), "주어 you에는 Does가 아니라 Do를 쓰므로"), (L("Is", "have to"), "have to의 의문문에는 be동사 Is를 쓰지 않으므로"), (L("Do", "have to"), "주어 you에 Do, 그 뒤에 have to를 바르게 썼으므로"),
     (L("Do", "has to"), "Do 뒤에는 has to가 아니라 have to를 쓰므로"), (L("Are", "have to"), "have to의 의문문에는 be동사 Are를 쓰지 않으므로")], 3)
f669("C", f"A: {BL('A')} Jane have to study today?\nB: Yes, she {BL('B')} to.", [(L("Do", "has"), "(A): 3인칭 단수 주어 Jane에는 Does를 쓰므로"), (L("Does", "have"), "(B): 긍정 대답의 3인칭 단수 주어 she에는 has to를 쓰므로"), (L("Does", "has"), "의문문에 Does, 긍정 대답에 she has to를 바르게 썼으므로"),
     (L("Is", "has"), "(A): have to의 의문문에는 be동사 Is를 쓰지 않으므로"), (L("Do", "have"), "(A): Jane에는 Does를, (B): she에는 has를 쓰므로")], 3,
     S669 + " 정답 조합(Does - have to)이 원문항과 같아, 대답을 ‘Yes, she has to.’로 바꿔 정답 조합이 Does - has가 되게 했다.")
f669("D", f"A: {BL('A')} they {BL('B')} go now?\nB: Yes, they do.", [(L("Do", "have to"), "복수 주어 they에 Do, 그 뒤에 have to를 바르게 썼으므로"), (L("Do", "has to"), "Do 뒤에는 has to가 아니라 have to를 쓰므로"), (L("Are", "have to"), "have to의 의문문에는 be동사 Are를 쓰지 않으므로"),
     (L("Is", "have to"), "have to의 의문문에는 be동사 Is를 쓰지 않으므로"), (L("Does", "has to"), "복수 주어 they에는 Do를 쓰고 그 뒤에는 have to를 쓰므로")], 1)
f669("E", f"A: {BL('A')} Tom and Ben {BL('B')} clean the room?\nB: Yes, they do.", [(L("Is", "have to"), "have to의 의문문에는 be동사 Is를 쓰지 않으므로"), (L("Are", "have to"), "have to의 의문문에는 be동사 Are를 쓰지 않으므로"), (L("Does", "has to"), "복수 주어 Tom and Ben에는 Do를 쓰고 그 뒤에는 have to를 쓰므로"),
     (L("Do", "has to"), "Do 뒤에는 has to가 아니라 have to를 쓰므로"), (L("Do", "have to"), "복수 주어 Tom and Ben에 Do, 그 뒤에 have to를 바르게 썼으므로")], 5)
f669("F", f"A: Mina {BL('A')} to finish the report today.\nB: Oh, {BL('B')} she have to do it now?", [(L("have", "Does"), "(A): 3인칭 단수 주어 Mina의 긍정문에는 has to를 쓰므로"), (L("has", "Do"), "(B): 3인칭 단수 주어 she의 의문문에는 Does를 쓰므로"), (L("is", "Does"), "(A): ‘~해야 한다’는 is to가 아니라 has to로 쓰므로"),
     (L("have", "Do"), "(A): Mina에는 has를, (B): she에는 Does를 쓰므로"), (L("has", "Does"), "긍정문에 Mina has to, 의문문에 Does she have to를 바르게 썼으므로")], 5,
     S669 + " 정답 조합(Does - have to)이 원문항과 같아, 긍정문과 의문문을 이어 정답 조합이 has - Does가 되게 했다.")

# 6-70 <보기> 분석: 원문항처럼 <보기> 문장을 직접 분석한 설명으로
R670 = "have to는 must와 비슷하게 ‘~해야 한다’는 뜻이고, 3인칭 단수 긍정문에는 has to를 쓴다. 부정문(don't/doesn't have to, ~할 필요가 없다)과 의문문(Do/Does ~ have to?)에서는 have to를 쓴다."
S670 = "원문항은 <보기> 문장을 분석한 설명을 판별하는데, 변형은 <보기>와 관계없는 have to 일반 규칙이 선택지 대부분이었고 오답 네 개가 B와 똑같았다. 원문항 발문으로 되돌리고 <보기> 문장을 직접 분석한 설명으로 유형마다 새로 썼다."
def f670(t, items, a, s=S670):
    talk(6, 70, t, items, a, R670, s, st="R")
f670("B", [("'doesn't have to'는 '~할 필요가 없다'는 뜻으로 쓰였다.", "doesn't have to는 ‘~할 필요가 없다’는 뜻이므로"), ("주어가 He이므로 doesn't 뒤에서도 'has to'로 써야 한다.", "doesn't 뒤에는 has to가 아니라 have to를 쓰므로"),
           ("'go'는 have to 뒤에 온 동사원형이다.", "have to 뒤에는 동사원형이 오므로"), ("'He doesn't have to go.'는 'He must not go.'와 뜻이 다르다.", "must not은 ‘~하면 안 된다’는 금지의 뜻이므로"),
           ("주어를 'They'로 바꾸면 'They don't have to go.'가 된다.", "복수 주어의 부정문에는 don't have to를 쓰므로")], 2)
f670("C", [("'have to'는 '~해야 한다'는 의무의 뜻으로 쓰였다.", "have to는 의무를 나타내므로"), ("주어가 We이므로 has to가 아닌 have to를 썼다.", "주어 We에는 have to를 쓰므로"),
           ("이 문장을 부정문으로 바꾸면 'We have not to study now.'가 된다.", "have to의 부정문은 don't have to로 만들어 We don't have to study now.가 되므로"), ("'study'는 have to 뒤에 온 동사원형이다.", "have to 뒤에는 동사원형이 오므로"),
           ("'now'는 공부해야 하는 때를 나타낸다.", "now가 공부해야 하는 때를 나타내므로")], 3)
f670("D", [("주어 She가 3인칭 단수이므로 has to를 썼다.", "3인칭 단수 주어의 긍정문에는 has to를 쓰므로"), ("'has to'는 조동사 must와 비슷한 뜻이다.", "has to와 must는 모두 의무를 나타내므로"),
           ("'go'는 has to 뒤의 동사원형이다.", "has to 뒤에는 동사원형이 오므로"), ("주어를 'I'로 바꾸면 'I has to go home.'이라고 써야 한다.", "주어 I에는 has to가 아니라 have to를 쓰므로"),
           ("의문문으로 바꾸면 'Does she have to go home?'이 된다.", "3인칭 단수 주어의 have to 의문문은 Does ~ have to로 만들므로")], 4)
f670("E", [("주어를 'they'로 바꾸면 'Does they have to work?'라고 써야 한다.", "주어 they에는 Does가 아니라 Do를 써서 Do they have to work?가 되므로"), ("'Does'는 주어 he가 3인칭 단수이므로 썼다.", "3인칭 단수 주어의 의문문에는 Does를 쓰므로"),
           ("Does가 앞에 있으므로 has to가 아니라 have to를 썼다.", "Does 뒤에는 have to를 쓰므로"), ("이 질문에 긍정으로 답하면 'Yes, he does.'라고 할 수 있다.", "Does 의문문에는 does로 답하므로"),
           ("'work'는 have to 뒤의 동사원형이다.", "have to 뒤에는 동사원형이 오므로")], 1)


# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, s, r=R_MD, **kw):
    FIX.pop((6, n, t), None)
    mk(6, n, t, items, a, r, s, **kw)
# 6-61 F: 우리말 해석을 원문항처럼 다음 줄에
FIX[(6, 61, "F")]["p"] = "We _______ wear seat belts.\n(우리는 안전벨트를 해야 한다.)"
FIX[(6, 61, "F")]["s"] = "발문에 ‘우리말의 의무 의미와 일치하도록’이 붙었고 우리말 해석이 문장과 같은 줄에 있었다. 원문항 발문으로 되돌리고 해석을 원문항처럼 다음 줄에 두었다. 보기와 정답은 그대로다."
# 6-62 C·F: 정답 위치가 원문항·B와 모두 ①이라 보기 순서를 바꿈
S662 = "발문에 ‘허락을 나타내는 우리말과 뜻이 일치하고, 문장 형태도 올바른’이 붙었다. 원문항 발문으로 되돌렸다. 정답 위치가 원문항·B와 모두 ①이어서 보기 순서를 바꿨다."
R662 = "‘~해도 된다’는 허락은 may + 동사원형으로 나타낸다. must와 have to는 ‘~해야 한다’는 의무다. 조동사 뒤에는 동사원형을 쓴다."
redo(62, "C", [("You may reading this book.", "may 뒤에는 -ing형이 아니라 동사원형 read를 써야 하므로"), ("You have to read this book.", "have to는 ‘~해야 한다’는 의무이므로"), ("You may read this book.", "may + 동사원형으로 허락을 바르게 나타냈으므로"),
     ("You do may read this book.", "may 앞에 do를 쓸 수 없으므로"), ("You must read this book.", "must는 ‘~해야 한다’는 의무이므로")], 3, S662, r=R662, st="R")
redo(62, "F", [("Mina has to open the window.", "has to는 ‘~해야 한다’는 의무이므로"), ("Mina must open the window.", "must는 ‘~해야 한다’는 의무이므로"), ("Mina may opens the window.", "may 뒤에는 동사원형 open을 써야 하므로"),
     ("Mina may open the window.", "may + 동사원형으로 허락을 바르게 나타냈으므로"), ("Mina is open the window.", "be동사와 일반동사 원형을 함께 쓸 수 없고 허락의 뜻도 없으므로")], 4, S662, r=R662, st="R")
# 6-64 B~F: 밑줄 범위를 원문항처럼 한 단어로(조동사 뒤의 동사)
S664B = "원문항은 밑줄이 한 단어인데 변형은 ‘조동사 + 동사’ 두 단어에 밑줄을 쳤다. 원문항처럼 한 단어(조동사 뒤의 동사)에만 밑줄을 쳤다."
def g664(t, items, a, s):
    redo(64, t, [(x, w or OK64) for x, w in items], a, s)
g664("B", [("Tom can <u>swim</u> well.", ""), ("They may <u>are</u> busy.", "may 뒤에는 be동사의 원형 be를 써야 하므로"), ("We must <u>wear</u> a helmet.", ""), ("She should <u>go</u> to bed early.", ""), ("You may <u>sit</u> here.", "")], 2,
     "선택지가 모두 may 문장이라 원문항보다 범위가 좁았다. can, must, should 문장을 섞어 새로 썼다. " + S664B)
g664("C", [("She must <u>finishes</u> her homework.", "must 뒤에는 동사원형 finish를 써야 하므로"), ("We should <u>listen</u> to our teacher.", ""), ("You may <u>take</u> a cookie.", ""), ("I must <u>go</u> now.", ""), ("He can <u>ride</u> a horse.", "")], 1, S664 + " " + S664B)
g664("D", [("You should <u>wash</u> your hands.", ""), ("I may <u>be</u> late today.", ""), ("Tom can <u>plays</u> the drums.", "can 뒤에는 동사원형 play를 써야 하므로"), ("We must <u>stop</u> at the red light.", ""), ("They may <u>visit</u> us.", "")], 3, S664 + " " + S664B)
g664("E", [("My dad can <u>fix</u> the car.", ""), ("You must not <u>run</u> here.", "must not 뒤에 동사원형을 바르게 썼으므로"), ("It may <u>snow</u> tonight.", ""), ("She should <u>joining</u> us.", "should 뒤에는 -ing형이 아니라 동사원형 join을 써야 하므로"), ("We should <u>save</u> water.", "")], 4, S664 + " " + S664B)
g664("F", [("Mina can <u>speak</u> French.", ""), ("You may <u>use</u> this computer.", ""), ("They should <u>bring</u> water.", ""), ("We must <u>leave</u> now.", ""), ("Tom may <u>arrives</u> after lunch.", "may 뒤에는 동사원형 arrive를 써야 하므로")], 5, S664B + " 문장과 정답은 그대로다.")
# 6-67 D: 빈칸 문장(she must ___ a teacher)이 원문항(he must ___ a teacher)과 같음
redo(67, "D", [("is", "must 뒤에는 동사원형을 써야 하므로"), ("being", "must 뒤에 -ing형을 쓸 수 없으므로"), ("to be", "must 뒤에는 to 없이 동사원형을 쓰므로"), ("be", "must 뒤에 be동사의 원형 be를 써서 ‘~임이 틀림없다’는 추측을 나타내므로"), ("are", "must 뒤에는 동사원형을 써야 하므로")], 4,
     "빈칸이 든 문장(she must ___ a teacher)이 원문항(he must ___ a teacher)과 주어만 달랐다. 대화를 새로 썼다. 보기와 정답은 그대로다.",
     r="must 뒤에는 동사원형을 쓴다. must be ~는 ‘~임이 틀림없다’는 강한 추측을 나타낸다.", p="A: Who is that man?\nB: He is carrying a guitar, so he must ________ a musician.")
