# 5급 CH4 현재진행형 (31~40) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
R_ING = "현재진행형은 am/is/are + 동사원형-ing로 쓰고, 부정문은 be동사 뒤에 not을, 의문문은 be동사를 주어 앞에 둔다. be동사는 주어에 맞춰 am/is/are를 쓴다."

# 5-32, 5-37, 5-40 원문항 발문
F(5, 32, "B", st="R", s="발문에 ‘현재진행형으로’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
F(5, 37, "B", st="R", s="발문에 ‘be동사’가 붙어 넣을 말의 종류를 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
F(5, 40, "B", st="R", s="발문이 ‘현재진행형이 문법적으로 옳은 문장만 묶인 것’으로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 5-31 -ing형 짝: 원문항처럼 규칙이 까다로운 옳은 짝으로 유형마다 새로
R531 = "-ing형은 대부분 동사원형에 -ing를 붙인다. -e로 끝나면 e를 빼고(make → making), -ie로 끝나면 ie를 y로 바꾸며(lie → lying), 강세 있는 단모음 + 단자음으로 끝나면 자음을 한 번 더 쓴다(run → running). 자음 + y, 모음 + y는 그대로 -ing를 붙인다."
S531 = "옳은 짝 오답 네 개(play - playing, cut - cutting, write - writing, read - reading)가 유형마다 같았다. 원문항처럼 규칙이 까다로운 옳은 짝으로 유형마다 새로 썼다."
E_ = "-e로 끝나 e를 빼고 -ing를 바르게 붙였으므로"; IE = "-ie로 끝나 ie를 y로 바꾸고 -ing를 바르게 붙였으므로"; DBL = "단모음 + 단자음으로 끝나 자음을 한 번 더 쓰고 -ing를 바르게 붙였으므로"; Y = "y로 끝나도 그대로 -ing를 바르게 붙였으므로"; PL = "그대로 -ing를 바르게 붙였으므로"
def f531(t, items, a, s=S531):
    mk(5, 31, t, items, a, R531, s)
f531("C", [("die - dying", IE), ("stop - stopping", DBL), ("come - coming", E_), ("enjoy - enjoying", Y), ("run - runing", "단모음 + 단자음으로 끝나 자음을 한 번 더 써서 running으로 써야 하므로")], 5)
f531("D", [("get - getting", DBL), ("ride - riding", E_), ("make - makeing", "-e로 끝나 e를 빼고 making으로 써야 하므로"), ("carry - carrying", Y), ("plan - planning", DBL)], 3)
f531("E", [("take - taking", E_), ("come - comming", "-e로 끝나는 동사라 e만 빼고 coming으로 써야 하므로"), ("put - putting", DBL), ("see - seeing", "-ee로 끝나면 e를 빼지 않고 그대로 -ing를 바르게 붙였으므로"), ("shop - shopping", DBL)], 2,
     "옳은 짝 오답 네 개가 유형마다 같았고, 정답(lie - lieing)이 B와 똑같았다. 원문항처럼 규칙이 까다로운 옳은 짝으로 오답을 새로 쓰고 정답도 B와 다르게(come - comming) 바꿨다.")
f531("F", [("have - having", E_), ("drop - dropping", DBL), ("fly - flying", Y), ("swim - swiming", "단모음 + 단자음으로 끝나 자음을 한 번 더 써서 swimming으로 써야 하므로"), ("give - giving", E_)], 4)

# 5-33 틀린 문장: 원문항 발문, 긍정·부정·의문문을 섞어 짝 없이 유형마다 새로
S533 = "원문항은 진행형 긍정·부정·의문문을 섞어 판별하는데, 변형은 모두 의문문이라 범위가 좁았고 짝 문장과 같은 오답이 반복되었다. 긍정·부정·의문문을 섞어 짝 문장 없이 유형마다 새로 썼다."
OK33 = "주어에 맞는 be동사와 -ing형으로 진행형을 바르게 만들었으므로"
def f533(t, items, a, s=S533):
    mk(5, 33, t, [(x, w or OK33) for x, w in items], a, R_ING, s, st="R")
f533("B", [("The students are taking a test.", ""), ("The dog isn't sleeping under the chair.", ""), ("Is Tom waiting outside?", ""), ("Are Mina cooking dinner now?", "3인칭 단수 주어 Mina에는 Is를 써야 하므로"), ("I'm not listening to music.", "")], 4,
     "발문이 ‘현재진행형 의문문이 틀린 것’으로 바뀌어 범위를 알려 주었고 모두 의문문이었다. 원문항 발문으로 되돌리고 긍정·부정문을 섞었다. 정답은 그대로다.")
f533("C", [("Jane is reading a comic book.", ""), ("Are the kids swimming in the river?", ""), ("Tom isn't watching TV now.", ""), ("We are not playing games.", ""), ("My brother are taking a shower.", "3인칭 단수 주어 My brother에는 is를 써야 하므로")], 5)
f533("D", [("Is your dad driving now?", ""), ("They aren't eating lunch.", ""), ("She not is singing a song.", "부정문은 be동사 뒤에 not을 두어 is not singing으로 써야 하므로"), ("I am drawing a picture.", ""), ("Are you making a cake?", "")], 3)
f533("E", [("Mina and Tom is walking to school.", "복수 주어 Mina and Tom에는 are를 써야 하므로"), ("The baby is crying.", ""), ("Am I talking too fast?", ""), ("He isn't fixing the door.", ""), ("Are they dancing on the stage?", "")], 1)
f533("F", [("The dog is running after the cat.", ""), ("Does Jane cooking dinner now?", "진행형 의문문은 Does가 아니라 be동사로 시작해 Is Jane cooking으로 써야 하므로"), ("We're waiting for you.", ""), ("The girls aren't laughing.", ""), ("Is it snowing outside?", "")], 2)

# 5-34 진행형 질문의 대답: B 원문항 발문, C~F는 같은 주어의 틀린 대답
F(5, 34, "B", st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
R534 = "be동사 진행형 의문문에는 Yes, 주어 + be동사. / No, 주어 + be동사 + not.으로 답한다. 대답의 주어는 질문의 주어에 맞추고(you → I, Jane → she), 시제도 질문과 같게 현재형 be동사를 쓴다."
S534 = "원문항 오답은 같은 주어의 틀린 대답(they don't, they weren't 등)인데, 변형 오답은 주어가 맞지 않는 대답이라 바로 지워졌고 유형마다 반복되었다. 원문항처럼 같은 주어의 틀린 대답으로 유형마다 새로 썼다."
def f534(t, p, items, a, s=S534):
    mk(5, 34, t, items, a, R534, s, p=p, okdup=True)
f534("C", "A: Is Jane reading? ⏎ B: _________________".replace(" ⏎ ", "\n"), [("No, she doesn't.", "be동사 의문문에는 does로 답하지 않으므로"), ("No, she isn't.", "Is 의문문에 isn't로 바르게 답했으므로"), ("No, she wasn't.", "현재진행형 질문에 과거형 wasn't로 답했으므로"), ("Yes, she does.", "be동사 의문문에는 does로 답하지 않으므로"), ("Yes, he is.", "Jane은 she로 받아야 하므로")], 2)
f534("D", "A: Are you studying?\nB: _________________", [("Yes, I do.", "be동사 의문문에는 do로 답하지 않으므로"), ("Yes, you are.", "you에 대한 질문에는 I로 답하므로"), ("Yes, I was.", "현재진행형 질문에 과거형 was로 답했으므로"), ("Yes, I am.", "Are you 질문에 I am으로 바르게 답했으므로"), ("No, I don't.", "be동사 의문문에는 don't로 답하지 않으므로")], 4)
f534("E", "A: Is Tom running?\nB: _________________", [("Yes, he is.", "Is 의문문에 he is로 바르게 답했으므로"), ("Yes, he does.", "be동사 의문문에는 does로 답하지 않으므로"), ("No, he doesn't.", "be동사 의문문에는 doesn't로 답하지 않으므로"), ("No, he wasn't.", "현재진행형 질문에 과거형 wasn't로 답했으므로"), ("Yes, she is.", "Tom은 he로 받아야 하므로")], 1)
f534("F", "A: Are we walking too fast?\nB: _________________", [("No, we don't.", "be동사 의문문에는 don't로 답하지 않으므로"), ("Yes, they are.", "we에 대한 질문에 they로 답했으므로"), ("No, we aren't.", "Are we 질문에 we aren't로 바르게 답했으므로"), ("Yes, we do.", "be동사 의문문에는 do로 답하지 않으므로"), ("No, we weren't.", "현재진행형 질문에 과거형 weren't로 답했으므로")], 3,
     S534 + " 질문(Are we late?)이 진행형이 아니어서 진행형 질문(Are we walking too fast?)으로 바꿨다.")

# 5-35 올바른 문장: B 원문항 발문, D~F는 짝 없이 원문항처럼 여러 종류의 오류로
S535 = "정답 문장과 같은 문장의 틀린 형태가 함께 있어 대비 단서가 되었고 오답 네 개가 C와 똑같았다. 원문항처럼 철자·어순·be동사 수 일치·be + 동사원형 오류를 섞어 짝 문장 없이 유형마다 새로 썼다."
def f535(t, items, a, s=S535):
    mk(5, 35, t, items, a, R_ING, s)
f535("D", [("Is she makeing a cake?", "make의 -ing형은 e를 빼고 making으로 써야 하므로"), ("They not are sleeping.", "부정문은 be동사 뒤에 not을 두어 are not으로 써야 하므로"), ("Mom is washing the dishes.", "3인칭 단수 주어에 is + -ing로 진행형을 바르게 만들었으므로"),
           ("Are you listen to me?", "be동사 뒤에는 동사원형이 아니라 -ing형 listening을 써야 하므로"), ("The kids is laughing loudly.", "복수 주어 The kids에는 are를 써야 하므로")], 3)
f535("E", [("Tom are riding a bike.", "3인칭 단수 주어 Tom에는 is를 써야 하므로"), ("He isn't runing now.", "run의 -ing형은 n을 한 번 더 써서 running으로 써야 하므로"), ("We are eat dinner.", "be동사 뒤에는 동사원형이 아니라 -ing형 eating을 써야 하므로"),
           ("Is the baby sleeping now?", "be동사를 주어 앞에 두고 -ing형을 써서 의문문을 바르게 만들었으므로"), ("She doesn't singing.", "진행형 부정문은 doesn't가 아니라 isn't + -ing로 써야 하므로")], 4)
f535("F", [("I'm not wearing a hat.", "주어 I에 am not + -ing로 부정문을 바르게 만들었으므로"), ("Are they swiming?", "swim의 -ing형은 m을 한 번 더 써서 swimming으로 써야 하므로"), ("My dad not is cooking.", "부정문은 be동사 뒤에 not을 두어 is not으로 써야 하므로"),
           ("Is Jane write a letter?", "be동사 뒤에는 동사원형이 아니라 -ing형 writing을 써야 하므로"), ("You is drawing well.", "주어 You에는 are를 써야 하므로")], 1)

# 5-36 우리말 뜻 제시: 원문항 발문
R536 = "‘~하고 있다’는 지금 진행 중인 일이므로 am/is/are 뒤에 동사원형-ing를 쓴다. be동사 뒤에 동사원형·현재형·과거형은 쓸 수 없다."
S536 = "발문이 ‘알맞은 -ing형을 고르시오’라고 정답 형태를 알려 주었다. 원문항처럼 우리말 뜻을 제시하는 발문으로 바꿨다."
def f536(t, ko, items, a, s=S536):
    mk(5, 36, t, items, a, R536, s, st=f"다음 빈칸에 '{ko}'라는 의미가 되도록 알맞은 단어를 고르세요.")
V_ = lambda v: f"be동사 뒤에 동사원형({v})을 쓸 수 없으므로"
f536("B", "그림을 그리고 있다", [("draws", "3인칭 단수 현재형이라 is 뒤에 쓸 수 없으므로"), ("drawing", "is와 함께 ‘그리고 있다’는 진행의 뜻이 되므로"), ("draw", "is 뒤에 동사원형을 쓸 수 없으므로"), ("drawed", "draw의 과거형은 drew이고, 과거형은 진행의 뜻이 되지 않으므로"), ("to draw", "to부정사는 ‘그리고 있다’는 진행의 뜻이 되지 않으므로")], 2, S536 + " 보기와 정답은 그대로다.")
f536("C", "편지를 쓰고 있다", [("writing", "is와 함께 ‘쓰고 있다’는 진행의 뜻이 되므로"), ("writes", "3인칭 단수 현재형이라 is 뒤에 쓸 수 없으므로"), ("write", "is 뒤에 동사원형을 쓸 수 없으므로"), ("to write", "to부정사는 ‘쓰고 있다’는 진행의 뜻이 되지 않으므로"), ("wrote", "과거형이라 is 뒤에 쓸 수 없고 진행의 뜻도 되지 않으므로")], 1, S536 + " 보기와 정답은 그대로다.")
f536("D", "축구를 하고 있다", [("played", "과거형이라 are 뒤에 쓸 수 없고 진행의 뜻도 되지 않으므로"), ("to play", "to부정사는 ‘하고 있다’는 진행의 뜻이 되지 않으므로"), ("plays", "3인칭 단수 현재형이라 are 뒤에 쓸 수 없으므로"), ("playing", "are와 함께 ‘하고 있다’는 진행의 뜻이 되므로"), ("play", "are 뒤에 동사원형을 쓸 수 없으므로")], 4, S536 + " 보기 순서를 바꿔 정답 위치가 C와 겹치지 않게 했다.")
f536("E", "책을 읽고 있다", [("reads", "3인칭 단수 현재형이라 am 뒤에 쓸 수 없으므로"), ("reader", "‘읽는 사람’이라는 명사라 ‘읽고 있다’는 뜻이 되지 않으므로"), ("reading", "am과 함께 ‘읽고 있다’는 진행의 뜻이 되므로"), ("to read", "to부정사는 ‘읽고 있다’는 진행의 뜻이 되지 않으므로"), ("read", "am 뒤에 동사원형을 쓸 수 없으므로")], 3, S536 + " 보기 순서를 바꿔 정답 위치가 D와 겹치지 않게 했다.")
f536("F", "방을 청소하고 있다", [("clean", "are 뒤에 동사원형을 쓸 수 없으므로"), ("cleans", "3인칭 단수 현재형이라 are 뒤에 쓸 수 없으므로"), ("to clean", "to부정사는 ‘청소하고 있다’는 진행의 뜻이 되지 않으므로"), ("cleaned", "과거형이라 are 뒤에 쓸 수 없고 진행의 뜻도 되지 않으므로"), ("cleaning", "are와 함께 ‘청소하고 있다’는 진행의 뜻이 되므로")], 5, S536 + " 보기와 정답은 그대로다.")

# 5-38 우리말 → 영어: 원문항 발문, 마침표 오답 대신 평서문 어순 + 물음표 오답
R538 = "현재진행형 의문문은 Am/Is/Are + 주어 + 동사원형-ing ~?로 쓴다. Do/Does로 시작하지 않고, 평서문 어순에 물음표만 붙이지 않는다."
S538 = "발문이 ‘be동사로 시작하는 기본 어순의 현재진행형 의문문으로’라고 정답 형식을 알려 주었고 ‘문장부호도 확인하시오’가 붙었다. 원문항 발문으로 되돌리고, 마침표만 다른 오답은 원문항처럼 평서문 어순에 물음표를 붙인 오답으로 바꿨다."
def f538(t, items, a, s=S538):
    mk(5, 38, t, items, a, R538, s, st="R")
DO = lambda d: f"진행형 의문문은 조동사({d})가 아니라 be동사로 시작하므로"; DECL = "평서문 어순에 물음표만 붙였으므로"; BASE = lambda v: f"be동사 뒤에는 동사원형이 아니라 -ing형({v})을 써야 하므로"
f538("B", [("Does she writing a letter now?", DO("Does")), ("Are she writing a letter now?", "주어 she에는 Is를 써야 하므로"), ("She is writing a letter now?", DECL), ("Is she write a letter now?", BASE("writing")), ("Is she writing a letter now?", "Is + 주어 + -ing로 진행형 의문문을 바르게 만들었으므로")], 5,
     "발문이 ‘be동사로 시작하는 기본 어순의 현재진행형 의문문으로’라고 정답 형식을 알려 주었고 ‘문장부호도 확인하시오’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f538("C", [("Does Jane reading a book now?", DO("Does")), ("Jane is reading a book now?", DECL), ("Are Jane reading a book now?", "주어 Jane에는 Is를 써야 하므로"), ("Is Jane reading a book now?", "Is + 주어 + -ing로 진행형 의문문을 바르게 만들었으므로"), ("Is Jane read a book now?", BASE("reading"))], 4)
f538("D", [("Do you studying English now?", DO("Do")), ("Are you studying English now?", "Are + 주어 + -ing로 진행형 의문문을 바르게 만들었으므로"), ("Is you studying English now?", "주어 you에는 Are를 써야 하므로"), ("You are studying English now?", DECL), ("Are you study English now?", BASE("studying"))], 2)
f538("E", [("Is Tom watching TV now?", "Is + 주어 + -ing로 진행형 의문문을 바르게 만들었으므로"), ("Does Tom watching TV now?", DO("Does")), ("Tom is watching TV now?", DECL), ("Are Tom watching TV now?", "주어 Tom에는 Is를 써야 하므로"), ("Is Tom watch TV now?", BASE("watching"))], 1)
f538("F", [("Are we clean the room now?", BASE("cleaning")), ("We are cleaning the room now?", DECL), ("Are we cleaning the room now?", "Are + 주어 + -ing로 진행형 의문문을 바르게 만들었으므로"), ("Is we cleaning the room now?", "주어 we에는 Are를 써야 하므로"), ("Do we cleaning the room now?", DO("Do"))], 3)


# ---- 2차 감수(2026-10) 추가 ----
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
# 5-32 C: 없는 형태(writ) → 원문항의 wining처럼 -ing 철자 오류로
mk(5, 32, "C", [("Jane writing a letter.", "be동사 없이 -ing형만 써서 문장이 되지 않으므로"), ("Jane does writing a letter.", "진행형은 does가 아니라 be동사와 함께 쓰므로"), ("Jane is writing a letter.", "is + writing으로 ‘쓰고 있다’를 바르게 나타냈으므로"),
    ("Jane is writeing a letter.", "write의 -ing형은 e를 빼고 writing으로 써야 하므로"), ("Jane is wrote a letter.", "be동사 뒤에 과거형 wrote를 쓸 수 없으므로")], 3, R_ING,
   "오답 ④의 writ는 쓰이지 않는 형태였다. 원문항의 wining처럼 -ing형 철자를 틀린 오답(writeing)으로 바꿨다. 정답은 그대로다.")
# 5-35 B: 정답 문장의 틀린 짝(We don't waiting for the bus.)을 다른 문장으로 / C: 짝 문장과 짧은 문장을 원문항 수준으로
mk(5, 35, "B", [("I am not study now.", "be동사 뒤에는 동사원형이 아니라 -ing형 studying을 써야 하므로"), ("We aren't waiting for the bus.", "주어 We에 aren't + -ing로 부정문을 바르게 만들었으므로"), ("My brother doesn't doing his homework.", "진행형 부정문은 doesn't가 아니라 isn't + -ing로 써야 하므로"),
    ("Mina aren't washing the dishes.", "3인칭 단수 주어 Mina에는 isn't를 써야 하므로"), ("The boys is playing outside.", "복수 주어 The boys에는 are를 써야 하므로")], 2, R_ING,
   "발문이 ‘현재진행형 문장이 문법적으로 옳은 것’으로 바뀌었고, 정답 문장과 같은 문장의 틀린 형태(We don't waiting for the bus.)가 함께 있어 둘만 견주면 되었다. 원문항 발문으로 되돌리고 짝 문장을 다른 문장으로 바꿨다. 정답은 그대로다.", st="R")
mk(5, 35, "C", [("He doesn't walking to school.", "진행형 부정문은 doesn't가 아니라 isn't + -ing로 써야 하므로"), ("I is not sleeping now.", "주어 I에는 am을 써야 하므로"), ("My sister are doing her homework.", "3인칭 단수 주어 My sister에는 is를 써야 하므로"),
    ("We not are having lunch.", "부정문은 be동사 뒤에 not을 두어 are not으로 써야 하므로"), ("They aren't playing soccer.", "복수 주어 They에 aren't + -ing로 부정문을 바르게 만들었으므로")], 5, R_ING,
   "정답 문장과 거의 같은 문장의 틀린 형태(They isn't playing.)가 함께 있었고, 두세 단어짜리 문장이 많았다. 짝 문장을 없애고 문장 길이를 원문항 수준으로 맞췄다. 정답은 그대로다.")
# 5-39 B: 정답만 길고 ②와 서로 어긋남 / C: B와 같은 문장(It is snowing) / E·F: 틀린 설명이 뻔하고 서로 같은 꼴
R539 = "현재진행형은 am/is/are + 동사원형-ing로 지금 진행 중인 일을 나타낸다. be동사는 주어에 맞추고, 부정문은 be동사 뒤에 not, 의문문은 be동사를 주어 앞에 둔다. 과거에 진행 중이던 일은 was/were + -ing로 쓴다."
OKD = "문장을 바르게 설명했으므로"
def f539(t, p, items, a, s):
    mk(5, 39, t, [(x, w or OKD) for x, w in items], a, R539, s, p=p, st="R")
f539("B", "It is snowing heavily outside.", [("snowing은 snow에 -ing을 붙인 형태이다.", ""), ("날씨를 나타내는 비인칭주어 it이 쓰였다.", ""), ("주어 it은 3인칭 단수이므로 is가 필요하다.", ""),
     ("의문문으로 바꾸면 Does it snowing heavily outside?가 된다.", "진행형 의문문은 Does가 아니라 be동사를 앞에 두어 Is it snowing ~?으로 쓰므로"), ("현재 진행 중인 날씨이므로 is snowing을 썼다.", "")], 4,
     "정답 설명만 다른 보기의 두 배쯤 길고, ②(비인칭주어 it)와 서로 어긋나 둘만 견주면 답이 나왔다. 길이가 비슷하고 진행형 의문문 만들기를 묻는 틀린 설명으로 바꿨다. 정답 위치는 그대로다.")
f539("C", "The wind is blowing hard now.", [("주어 The wind는 3인칭 단수이므로 is를 쓴다.", ""), ("현재진행형은 be동사와 동사 -ing형으로 만든다.", ""), ("blowing은 blow의 과거형이므로 지난 일을 나타낸다.", "blowing은 과거형이 아니라 -ing형이고, is blowing은 지금 진행 중인 일을 나타내므로"),
     ("의문문은 Is the wind blowing hard now?로 만들 수 있다.", ""), ("now는 현재진행형과 잘 어울리는 시간 표현이다.", "")], 3,
     "제시문(It is snowing now.)이 B(It is snowing heavily outside.)와 거의 같은 문장이었다. 제시문을 다른 문장으로 바꾸고 설명을 그에 맞췄다. 정답 위치는 그대로다.")
f539("E", "They are playing now.", [("주어를 Tom으로 바꿔도 be동사는 are를 그대로 쓴다.", "Tom은 3인칭 단수라 is로 바꿔야 하므로"), ("They는 복수 주어이므로 are를 쓴다.", ""), ("now는 현재진행형과 잘 어울린다.", ""),
     ("부정문은 They are not playing now.로 만들 수 있다.", ""), ("playing은 play에 -ing을 붙인 형태이다.", "")], 1,
     "틀린 설명이 ‘They is playing now.는 올바른 문장이다’여서 ②(They는 복수 주어이므로 are)만 보아도 답이 나왔고 F와 같은 꼴이었다. 주어를 바꿨을 때의 be동사를 묻는 설명으로 바꿨다. 정답 위치는 그대로다.")
f539("F", "I am studying now.", [("의문문은 Am I studying now?로 만들 수 있다.", ""), ("주어 I와 함께는 am을 쓴다.", ""), ("지난 일을 나타내려면 am은 그대로 두고 studying만 studied로 바꾼다.", "과거에 진행 중이던 일은 am을 was로 바꿔 was studying으로 써야 하므로"),
     ("studying은 study에 -ing을 붙인 형태이다.", ""), ("now는 현재 진행 중임을 나타낸다.", "")], 3,
     "틀린 설명이 ‘I is studying now.는 올바른 문장이다’여서 ②(I와 함께는 am)만 보아도 답이 나왔고 E와 같은 꼴이었다. 시제를 바꿨을 때의 형태를 묻는 설명으로 바꿨다. 정답 위치는 그대로다.")
# 5-40 C~F: 세 단어 문장 → 원문항 수준 길이, 오류 종류도 원문항처럼(be + 동사원형·3인칭형 등), 정답 조합을 유형마다 다르게
R540 = "현재진행형은 am/is/are + 동사원형-ing로 쓴다. be동사는 주어에 맞추고, be동사 뒤에 동사원형이나 -s형을 쓰지 않으며, be동사를 빼고 -ing형만 쓰지도 않는다."
S540 = "문장이 대부분 세 단어로 원문항(대여섯 단어)보다 짧았다. 문장 길이와 오류 종류를 원문항 수준으로 맞추고 정답 조합이 유형마다 겹치지 않게 했다."
def f540(t, lines, judge, ok, s=S540):
    c = V(5, 40, t)["c"]; a = c.index(ok) + 1
    F(5, 40, t, p="<보기>\n" + "\n".join(lines), c=c, a=a, r=R540, pre=["문장별 판정: " + " ".join(judge)], k=f"어법상 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), okdup=True, s=s + " 선택지는 그대로다." + ipos(a))
f540("C", ["(가) Look! The children are flying kites.", "(나) My sister is brushes her teeth now.", "(다) I am doing my homework right now.", "(라) We are wait for the school bus."],
     ["(가) O. 복수 주어에 are + flying을 썼다.", "(나) X. is 뒤에는 brushes가 아니라 brushing을 쓴다.", "(다) O. 주어 I에 am + doing을 썼다.", "(라) X. are 뒤에는 wait가 아니라 waiting을 쓴다."], "(가), (다)")
f540("D", ["(가) My uncle washing his car now.", "(나) The boys are riding their bikes in the park.", "(다) She is baking cookies for her family.", "(라) I is looking for my glasses now."],
     ["(가) X. be동사가 빠졌다(is washing).", "(나) O. 복수 주어에 are + riding을 썼다.", "(다) O. 주어 She에 is + baking을 썼다.", "(라) X. 주어 I에는 am을 쓴다."], "(나), (다)")
f540("E", ["(가) We are studies math in the library.", "(나) He are watching a movie now.", "(다) They are building a sandcastle on the beach.", "(라) I am helping my dad in the kitchen."],
     ["(가) X. are 뒤에는 studies가 아니라 studying을 쓴다.", "(나) X. 주어 He에는 is를 쓴다.", "(다) O. 주어 They에 are + building을 썼다.", "(라) O. 주어 I에 am + helping을 썼다."], "(다), (라)")
f540("F", ["(가) Tom is jogging along the river.", "(나) Look! The cat is climbing the tree.", "(다) We are clean the classroom now.", "(라) The girls is jumping rope outside."],
     ["(가) O. 주어 Tom에 is + jogging을 썼다.", "(나) O. 주어 The cat에 is + climbing을 썼다.", "(다) X. are 뒤에는 clean이 아니라 cleaning을 쓴다.", "(라) X. 복수 주어 The girls에는 are를 쓴다."], "(가), (나)")
