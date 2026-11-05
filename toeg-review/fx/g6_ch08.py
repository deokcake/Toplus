# 6급 CH8 조동사의 뜻·의문문·부정 (71~80) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 원문항 발문으로만 되돌리는 문항
for t in "CDF": F(6, 72, t, st="R", xr=[("이 문항은 추측의 부정만 비교한다.", "문장의 내용으로 둘 중 어느 뜻인지 판단한다."), ("금지의 해석은 이 문항에서 제외했다.", "여기서는 금지로 읽으면 문장의 뜻이 어색하다.")], s="발문이 ‘may를 가능성의 추측으로 사용한’, ‘(허락·금지의 뜻은 제외한다.)’라고 정답의 뜻을 알려 주었다. 원문항 발문으로 되돌렸다. 금지로 읽기 어려운 문장이라 보기와 정답은 그대로다.")
F(6, 73, "E", st="R", xr=[("이 문항에서는 직접 허락을 구하는 Can I가 필요하다.", "허락을 구하려면 Can I를 써야 한다.")], s="발문이 ‘허락을 묻는 뜻을 유지하면서 … 기본형 의문문’이라고 정답의 뜻과 형식을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDEF": F(6, 77, t, st="R", xr=[("평서문 어순의 확인 질문은 대화에서 가능하지만, Can으로 시작하는 기본형 조건과 다르다.", "평서문 어순에 물음표만 붙인 것은 의문문으로 바르게 바꾼 것이 아니다.")], s="발문이 ‘현재의 능력을 묻도록, Can으로 시작하고 물음표로 끝나는 기본형 의문문’이라고 정답 형식을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDEF": F(6, 80, t, st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 6-72 B·E: 원문항 발문으로 되돌리면 금지로도 읽히는 문장을 상태 동사 문장으로
R672 = "may not은 ‘~하지 않을지도 모른다’는 추측의 부정이나 ‘~해서는 안 된다’는 불허를 나타낸다. be, know, like처럼 상태를 나타내는 말과 함께 쓰이면 주로 추측의 뜻이다."
S672 = "발문이 ‘may를 가능성의 추측으로 사용한’, ‘(허락·금지의 뜻은 제외한다.)’라고 정답의 뜻을 알려 주었다. 원문항 발문으로 되돌리고, 조건 없이는 금지로도 읽히는 문장을 원문항처럼 상태를 나타내는 문장으로 바꿨다."
GUESS = "may not이 상태를 나타내는 말과 함께 쓰여 ‘~하지 않을지도 모른다’는 추측의 뜻이 되므로"
def f672(t, p, items, a, s=S672):
    mk(6, 72, t, items, a, R672, s, st="R", p=p)
f672("B", "Tom may not be hungry now.", [("Tom은 지금 절대 배가 고프지 않다.", "may not은 ‘절대 ~아니다’라는 단정이 아니므로"), ("Tom은 지금 배가 고프지 않을지도 모른다.", GUESS), ("Tom은 지금 배가 고파서는 안 된다.", "배고픈 상태를 금지하는 뜻은 어색하고, may not은 여기서 추측을 나타내므로"),
     ("Tom은 지금 배가 고플 필요가 없다.", "‘~할 필요가 없다’는 don't have to의 뜻이므로"), ("Tom은 지금 배가 고플 수 없다.", "‘~할 수 없다’는 can't의 뜻이므로")], 2)
f672("E", "Mina may not like spicy food.", [("Mina는 매운 음식을 좋아할 필요가 없다.", "‘~할 필요가 없다’는 don't have to의 뜻이므로"), ("Mina는 매운 음식을 좋아해서는 안 된다.", "좋아하는 마음을 금지하는 뜻은 어색하고, may not은 여기서 추측을 나타내므로"), ("Mina는 매운 음식을 좋아하지 않을지도 모른다.", GUESS),
     ("Mina는 매운 음식을 반드시 좋아한다.", "may not은 부정의 추측이지 ‘반드시 ~한다’는 뜻이 아니므로"), ("Mina는 매운 음식을 좋아할 수 없다.", "‘~할 수 없다’는 can't의 뜻이므로")], 3)

# 6-73 같은 의미: 원문항 발문, 마침표·평서문 오답 대신 원문항처럼 뜻이 다른 조동사 의문문
R673 = "May I ~?와 Can I ~?는 모두 허락을 묻는다. Must I ~?와 Do I have to ~?는 의무를, Should I ~?는 조언을, Do I ~?는 사실을 묻는다."
S673 = "발문이 ‘허락을 묻는 뜻을 유지하면서 … 조동사로 시작하고 물음표로 끝나는 기본형 의문문’이라고 정답의 뜻과 형식을 알려 주어 마침표·평서문 오답이 바로 지워졌다. 원문항 발문으로 되돌리고, 원문항처럼 뜻이 다른 조동사 의문문으로 오답을 바꿨다."
CAN = "Can I ~?도 허락을 묻는 표현이라 May I ~?와 뜻이 같으므로"; MUST = "Must I ~?는 ‘~해야 하나요?’라는 의무를 묻는 표현이므로"; SHD = "Should I ~?는 ‘~하는 게 좋을까요?’라는 조언을 묻는 표현이므로"; HAVE = "Do I have to ~?는 ‘~해야 하나요?’라는 의무를 묻는 표현이므로"; DO = "Do I ~?는 허락이 아니라 사실을 묻는 표현이므로"
def f673(t, items, a, s=S673):
    mk(6, 73, t, items, a, R673, s, st="R")
f673("B", [("Must I use your pen?", MUST), ("Can I use your pen?", CAN), ("Should I use your pen?", SHD), ("Do I have to use your pen?", HAVE), ("Do I use your pen?", DO)], 2)
f673("C", [("Do I have to go home now?", HAVE), ("Must I go home now?", MUST), ("Should I go home now?", SHD), ("Can I go home now?", CAN), ("Do I go home now?", DO)], 4)
f673("D", [("Do I open the window?", DO), ("Should I open the window?", SHD), ("Do I have to open the window?", HAVE), ("Must I open the window?", MUST), ("Can I open the window?", CAN)], 5)
f673("F", [("Can I sit here?", CAN), ("Must I sit here?", MUST), ("Do I sit here?", DO), ("Should I sit here?", SHD), ("Do I have to sit here?", HAVE)], 1)

# 6-74 have to 질문의 대답: 원문항 발문, 원문항처럼 질문 주어의 형태 오류 오답
R674 = "Do/Does ~ have to …? 질문에는 Yes, 주어 + do/does. / No, 주어 + don't/doesn't.로 짧게 답한다. has나 must to, be동사로 답하지 않는다."
S674 = "발문이 ‘질문에서 사용한 do/does로 짧게 답할 때’라고 정답 형식을 알려 주었고, 오답이 질문 주어와 맞지 않아 바로 지워졌으며 유형마다 반복되었다. 원문항 발문으로 되돌리고, 원문항처럼 질문 주어의 형태 오류로 오답을 유형마다 새로 썼다."
def f674(t, q, items, a, s=S674):
    mk(6, 74, t, items, a, R674, s, st="R", p=q)
f674("B", "Do you have to study today?", [("No, I am not.", "have to 질문에는 be동사로 답하지 않으므로"), ("Yes, I have.", "Do 질문에는 have가 아니라 do로 답하므로"), ("No, I don't.", "Do you 질문에 I don't로 바르게 답했으므로"), ("No, I don't have.", "don't have로 끝내면 뜻이 달라지고 짧은 대답은 I don't로 하므로"), ("Yes, I must to.", "must 뒤에는 to를 쓰지 않고 Do 질문에는 do로 답하므로")], 3)
f674("C", "Does Jane have to clean the room?", [("Yes, she have.", "Does 질문에는 have가 아니라 does로 답하므로"), ("No, she doesn't.", "Does 질문에 she doesn't로 바르게 답했으므로"), ("No, she wasn't.", "have to 질문에는 be동사로 답하지 않으므로"), ("Yes, she do.", "3인칭 단수 주어 she에는 does를 쓰므로"), ("Yes, she can.", "have to 질문에는 can으로 답하지 않으므로")], 2)
f674("D", "Does Tom have to wear a helmet?", [("Yes, he has.", "Does 질문에는 has가 아니라 does로 답하므로"), ("Yes, he is.", "have to 질문에는 be동사로 답하지 않으므로"), ("No, he don't.", "3인칭 단수 주어 he에는 doesn't를 쓰므로"), ("Yes, he does.", "Does 질문에 he does로 바르게 답했으므로"), ("Yes, he must to.", "must 뒤에는 to를 쓰지 않고 Does 질문에는 does로 답하므로")], 4)
f674("E", "Do they have to go now?", [("Yes, they has.", "복수 주어 they에는 has를 쓰지 않고 do로 답하므로"), ("Yes, they are.", "have to 질문에는 be동사로 답하지 않으므로"), ("No, they haven't to.", "have to의 부정은 haven't to가 아니라 don't have to이므로"), ("No, they doesn't.", "복수 주어 they에는 don't를 쓰므로"), ("Yes, they do.", "Do they 질문에 they do로 바르게 답했으므로")], 5)
f674("F", "Do the visitors have to leave now?", [("No, they don't.", "Do 질문에 they don't로 바르게 답했으므로"), ("Yes, they have.", "Do 질문에는 have가 아니라 do로 답하므로"), ("No, they not have to.", "부정은 not만 넣지 않고 don't have to로 만들므로"), ("No, they haven't.", "have to 질문에는 haven't로 답하지 않으므로"), ("No, they aren't.", "have to 질문에는 be동사로 답하지 않으므로")], 1)

# 6-75 틀린 문장: 여러 조동사 의문문을 섞어 유형마다 새로
R675 = "can, may, must, should는 주어 앞에 두어 의문문을 만들고 뒤에 동사원형을 쓴다. have to는 Do/Does + 주어 + have to + 동사원형?으로 묻고, 3인칭 단수 주어에는 Does를 쓴다."
S675 = "원문항은 여러 조동사 의문문(Can, May, Must, Does … have to)을 섞어 판별하는데, 변형은 모두 Do/Does … have to 의문문이라 범위가 좁았고 오답 네 개가 B와 똑같았다. 여러 조동사 의문문을 섞어 유형마다 새로 썼다."
OKQ = "조동사를 주어 앞에 두고 동사원형을 써서 의문문을 바르게 만들었으므로"; OKH = "주어에 맞는 Do/Does와 have to로 의문문을 바르게 만들었으므로"
def f675(t, items, a, s=S675):
    mk(6, 75, t, items, a, R675, s)
f675("B", [("Can Mina ride a bike?", OKQ), ("Must we wear uniforms?", OKQ), ("May I use your phone?", OKQ), ("Do she have to study?", "3인칭 단수 주어 she에는 Does를 써야 하므로"), ("Does your dad have to work today?", OKH)], 4)
f675("C", [("Do Tom have to clean the room?", "3인칭 단수 주어 Tom에는 Does를 써야 하므로"), ("Can they speak Korean?", OKQ), ("Must I finish it now?", OKQ), ("Should we call her?", OKQ), ("May we come in?", OKQ)], 1)
f675("D", [("Should I take an umbrella?", OKQ), ("Does Jane has to work?", "Does 뒤에는 has to가 아니라 have to를 써야 하므로"), ("Can your brother swim?", OKQ), ("Do you have to go now?", OKH), ("Must we be quiet here?", OKQ)], 2)
f675("F", [("May I ask a question?", OKQ), ("Must the kids go to bed early?", OKQ), ("Can he plays the guitar?", "can 뒤에는 동사원형 play를 써야 하므로"), ("Do they have to wait?", OKH), ("Should I bring a gift?", OKQ)], 3)

# 6-76 must not의 뜻: 선택지 표현 방식을 통일(모두 문장의 동사를 넣은 뜻)
R676 = "must not은 ‘~해서는 안 된다’는 금지를 나타낸다. can(~할 수 있다), may(~해도 된다, ~할지도 모른다), must(~해야 한다), don't have to(~할 필요가 없다)와 구별한다."
S676 = "오답은 ‘할 수 있다, 해도 된다’처럼 일반적인 뜻인데 정답에만 문장의 동사가 들어 있어 눈에 띄었다. 모든 선택지에 문장의 동사를 넣어 표현 방식을 통일했다."
def f676(t, p, items, a, s=S676):
    mk(6, 76, t, items, a, R676, s, p=p)
NOTM = "must not은 ‘~해서는 안 된다’는 금지를 나타내므로"; C_ = "‘~할 수 있다’는 can의 뜻이므로"; M_ = "‘~해도 된다’는 허락의 may의 뜻이므로"; G_ = "‘~할지도 모른다’는 추측의 may의 뜻이므로"; D_ = "‘~할 필요가 없다’는 don't have to의 뜻이므로"; MU = "‘~해야 한다’는 must의 뜻이므로"
f676("B", "You <u>must not</u> eat in the library.", [("먹을 수 있다", C_), ("먹어도 된다", M_), ("먹어서는 안 된다", NOTM), ("먹을지도 모른다", G_), ("먹을 필요가 없다", D_)], 3,
     S676 + " 동사도 C(touch)와 겹치지 않게 eat으로 바꿨다.")
f676("D", "We <u>must not</u> be late.", [("늦어도 된다", M_), ("늦을 필요가 없다", D_), ("늦을 수 있다", C_), ("늦으면 안 된다", NOTM), ("늦을지도 모른다", G_)], 4)
f676("E", "You <u>must not</u> swim here.", [("수영할 필요가 없다", D_), ("수영하면 안 된다", NOTM), ("수영해도 된다", M_), ("수영할지도 모른다", G_), ("수영할 수 있다", C_)], 2)
f676("F", "Students <u>must not</u> use phones during the test.", [("사용할 수 있다", C_), ("사용할지도 모른다", G_), ("사용해서는 안 된다", NOTM), ("사용해야 한다", MU), ("사용할 필요가 없다", D_)], 3,
     "선택지가 원문항과 달리 목적어까지 넣은 문장 형태였다. 원문항처럼 짧은 뜻 표현(사용할 수 있다 등)으로 맞췄다.")

# 6-78 can't = be not able to: 원문항처럼 두 칸 빈칸, be + not 조합 선택지
R678 = "능력의 can't는 주어에 맞는 am/is/are not able to로 바꿀 수 있다. do/does not은 be동사 자리에 쓸 수 없다."
S678 = "원문항의 두 칸 빈칸(____ ____)이 한 칸으로 바뀌고 발문에 ‘현재의 능력이 없다는 뜻을 유지하도록’ 조건이 붙었으며, 조건이 없으면 긍정형(are 등)도 들어갈 수 있었다. 원문항 발문과 두 칸 빈칸으로 되돌리고 선택지를 be + not 조합만으로 바꿨다."
NG = lambda w: f"주어에 맞지 않는 {w}이므로"
DN = "do/does not은 be동사 자리에 쓸 수 없으므로"
def f678(t, s1, s2, items, a, s=S678):
    mk(6, 78, t, items, a, R678, s, st="R", p=f"{s1}\n= {s2}")
f678("B", "The boys can't swim.", "The boys ________ ________ able to swim.", [("am not", "am not은 주어 I에만 쓰므로"), ("is not", "is not은 3인칭 단수 주어에 쓰므로"), ("are not", "복수 주어 The boys에 맞는 are not이므로"), ("do not", DN), ("does not", DN)], 3,
     S678 + " 주어(They)가 D와 같아 The boys로 바꿨다.")
f678("C", "I can't go.", "I ________ ________ able to go.", [("are not", "are not은 you·복수 주어에 쓰므로"), ("is not", "is not은 3인칭 단수 주어에 쓰므로"), ("do not", DN), ("am not", "주어 I에 맞는 am not이므로"), ("does not", DN)], 4)
f678("D", "They can't lift the heavy table.", "They ________ ________ able to lift the heavy table.", [("does not", DN), ("are not", "복수 주어 They에 맞는 are not이므로"), ("is not", "is not은 3인칭 단수 주어에 쓰므로"), ("do not", DN), ("am not", "am not은 주어 I에만 쓰므로")], 2)
f678("E", "Jane can't cook.", "Jane ________ ________ able to cook.", [("do not", DN), ("am not", "am not은 주어 I에만 쓰므로"), ("are not", "are not은 you·복수 주어에 쓰므로"), ("does not", DN), ("is not", "3인칭 단수 주어 Jane에 맞는 is not이므로")], 5)
f678("F", "We can't help.", "We ________ ________ able to help.", [("are not", "주어 We에 맞는 are not이므로"), ("is not", "is not은 3인칭 단수 주어에 쓰므로"), ("am not", "am not은 주어 I에만 쓰므로"), ("does not", DN), ("do not", DN)], 1)

# 6-79 E: 원문항과 거의 같은 제시 문장을 새로
F(6, 79, "E", p="<보기>\nMy parents may not be at home.\n→ 주어가 'My parents'임에도 불구하고 'are'가 아니라 'be'를 쓴 이유는 (________)이기 때문입니다.",
  c=["be가 명사이기 때문에", "not 뒤에는 동사원형만 와서", "may라는 조동사 뒤에서는 주어가 복수여도 동사원형을 써야 해서", "My parents가 복수라서", "home 앞에는 are가 올 수 없어서"], a=3,
  r="조동사 may 뒤에는 주어의 인칭·수와 관계없이 동사원형을 쓴다. be동사의 원형은 be이다.",
  n=["be는 명사가 아니라 be동사의 원형이므로 오답이다.", "not 뒤라서가 아니라 조동사 may 뒤라서 원형을 쓰므로 오답이다.", "조동사 may 뒤에는 주어와 관계없이 동사원형 be를 쓰므로 정답이다.", "주어가 복수라면 are를 써야 하므로 be를 쓴 이유가 될 수 없어 오답이다.", "home 앞에도 are를 쓸 수 있고, be를 쓴 이유는 조동사 may이므로 오답이다."],
  s="제시 문장(He may not be at the museum.)이 원문항(He may not be at school.)과 거의 같았다. 주어를 복수(My parents)로 바꾸고 문장을 새로 써서 are 대신 be를 쓴 이유를 묻게 했다. 정답 위치 ③.")


# ---- 2차 감수(2026-10) 추가 ----
# 6-79 C·D·F: 제시문 틀(S may not be + 장소)과 정답 설명이 B와 같음 → 조동사를 바꿔 새로
R679 = "조동사(may, must, can, will) 뒤에는 주어와 관계없이 동사원형을 쓴다. be동사의 원형은 be다."
def f679(t, sent, subj, wrongbe, items, a, s):
    FIX.pop((6, 79, t), None)
    mk(6, 79, t, items, a, R679, s, p=f"<보기>\n{sent}\n→ 주어가 '{subj}'임에도 불구하고 '{wrongbe}'가 아니라 'be'를 쓴 이유는 ( )이기 때문입니다.")
S679 = "제시문의 틀(~ may not be + 장소)과 정답 설명(조동사 may 뒤에는 동사원형)이 B와 똑같았다. 조동사를 바꿔 제시문과 설명을 새로 썼다. 빈칸 모양도 원문항처럼 ( )로 맞췄다."
f679("C", "Tom must be very tired.", "Tom", "is", [("Tom 뒤에는 항상 be만 써야 해서", "주어가 Tom이어도 보통은 is를 쓰므로"), ("be가 추측의 뜻을 가진 조동사라서", "be는 조동사가 아니라 be동사의 원형이므로"), ("조동사 'must' 뒤에는 주어와 관계없이 동사원형을 써야 해서", "조동사 뒤에는 동사원형을 쓰므로"),
      ("tired가 형용사라서", "형용사 앞이라고 be를 쓰는 것은 아니므로"), ("very 앞에는 be만 올 수 있어서", "very와 be동사의 형태는 관계가 없으므로")], 3, S679)
f679("D", "Mina can be a good leader.", "Mina", "is", [("be가 is보다 더 공손해서", "be와 is는 공손함의 차이가 아니므로"), ("leader가 명사라서", "명사 앞이라고 be를 쓰는 것은 아니므로"), ("Mina가 여자 이름이어서", "주어의 성별과 be동사의 형태는 관계가 없으므로"),
      ("'can'은 조동사이고, 조동사 뒤에는 동사의 원래 모양(원형)이 와야 해서", "조동사 뒤에는 동사원형을 쓰므로"), ("good 앞에는 is를 쓸 수 없어서", "is good처럼 쓸 수 있으므로")], 4, S679)
f679("F", "Jane will be twelve next year.", "Jane", "is", [("be가 미래의 뜻을 혼자 나타내서", "미래의 뜻은 be가 아니라 will이 나타내므로"), ("숫자 twelve 앞에는 be만 올 수 있어서", "is twelve처럼 쓸 수 있으므로"), ("Jane 뒤에는 항상 is를 생략해서", "주어가 Jane이어도 보통은 is를 쓰므로"),
      ("조동사 'will' 뒤에는 주어와 관계없이 동사원형을 써야 해서", "조동사 뒤에는 동사원형을 쓰므로"), ("be가 is의 과거형이어서", "is의 과거형은 was이고 be는 원형이므로")], 4, S679)
FIX[(6, 79, "E")]["p"] = FIX[(6, 79, "E")]["p"].replace("(________)", "( )")
