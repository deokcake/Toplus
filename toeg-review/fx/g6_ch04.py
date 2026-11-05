# 6급 CH4 일반동사 현재형·Do/Does·were (31~40) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def talk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 옳지 않은 설명이다. 따라서 정답이다." if i + 1 == a else " 옳은 설명이다. 따라서 오답이다.")) if w.endswith("므로") else (w + (" 옳지 않은 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.")) for i, (_, w) in enumerate(items)], k=items[a-1][1], s=s + ipos(a), **kw)
R_DO = "일반동사 현재형은 3인칭 단수 주어에 -s/-es를 붙이고, 그 밖의 주어에는 동사원형을 쓴다. 의문문은 Do/Does + 주어 + 동사원형 ~?, 부정문은 don't/doesn't + 동사원형으로 쓴다."

# 원문항 발문으로만 되돌리는 문항
for t in "BEF": F(6, 34, t, st="R", xr=[("이 문항의 기본형 의문문은 Do/Does로 시작해야 한다. 평서문 어순의 확인 질문은 이 조건과 다르다.", "일반동사 문장을 의문문으로 바꿀 때는 Do/Does로 시작해야 한다. 평서문 어순에 물음표만 붙인 것은 올바르게 바꾼 의문문이 아니다.")], s="발문이 ‘Do 또는 Does로 시작하는 기본형 의문문으로’라고 정답 형식을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
F(6, 36, "B", st="R", xr=[("이 문항은 가정법이 아닌 실제 과거 상황이다.", "If I were you처럼 가정을 나타내는 were는 따로 익힌다.")], s="발문에 ‘과거의 실제 상황을 나타내는 평서문에서’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
F(6, 38, "B", st="R", xr=[("Tom이 직접 책을 읽는다는 능동태 조건에서는 Does Tom read books?로 묻는다. Is Tom read books?는 이 조건에 맞지 않는다.", "일반동사 read의 의문문은 Does Tom read books?로 묻는다. be동사 Is와 동사원형 read를 함께 쓸 수 없다.")], s="발문에 ‘능동태 현재 의문문’ 조건이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "CF": F(6, 39, t, st="R", s="발문에 ‘현재형 일반동사 의문문이 되도록’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BDF": F(6, 40, t, st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 6-32 s가 붙지 않는 것: 원문항처럼 동사 뒤 빈칸 형식
R632 = "3인칭 단수 주어(he, she, it, 사람·동물 한 명/한 마리)의 현재형 일반동사에는 s를 붙이고, I·you·복수 주어(A and B 포함)에는 동사원형을 쓴다."
S632 = "원문항은 동사 뒤 빈칸(like___)에 s가 붙는지 판단하는 형식인데, 변형은 괄호 안 동사원형을 그대로 쓰는 문장을 고르게 바뀌었다. 원문항 발문과 빈칸 형식으로 되돌렸다."
S3 = lambda s_: f"3인칭 단수 주어({s_})라 s가 붙으므로"; NO = lambda s_: f"주어({s_})가 3인칭 단수가 아니어서 동사원형을 써 s가 붙지 않으므로"
def f632(t, items, a, s=S632):
    mk(6, 32, t, items, a, R632, s, st="R")
f632("B", [("Tom read___ books every night.", S3("Tom")), ("My dad drink___ coffee.", S3("My dad")), ("We play___ soccer after school.", NO("We")), ("The boy run___ fast.", S3("The boy")), ("He sing___ well.", S3("He"))], 3)
f632("C", [("My uncle drive___ to work.", S3("My uncle")), ("Birds build___ nests in spring.", NO("Birds")), ("The baby smile___ a lot.", S3("The baby")), ("Jane bake___ bread on Sundays.", S3("Jane")), ("The train leave___ at six.", S3("The train"))], 2)
f632("D", [("The girl ride___ a bike.", S3("The girl")), ("My mom make___ cookies.", S3("My mom")), ("Mina keep___ a diary.", S3("Mina")), ("Tom and Ben walk___ home together.", NO("Tom and Ben")), ("Our teacher speak___ slowly.", S3("Our teacher"))], 4)
f632("E", [("They read___ books every day.", NO("They")), ("The dog sleep___ here.", S3("The dog")), ("Jane love___ music.", S3("Jane")), ("Tom like___ cats.", S3("Tom")), ("She write___ letters.", S3("She"))], 1)
f632("F", [("The cat drink___ milk.", S3("The cat")), ("My sister play___ the piano.", S3("My sister")), ("He eat___ lunch at noon.", S3("He")), ("Tom need___ help.", S3("Tom")), ("You call___ me every night.", NO("You"))], 5)

# 6-34 C·D: 원문항 발문, 시제를 바꾼 문법적 의문문 오답은 형태 오류로, D는 제시문 새로
R634 = "현재형 일반동사 문장을 의문문으로 바꿀 때는 Do/Does + 주어 + 동사원형 ~?으로 쓰고, 원래 문장의 현재 시제를 유지한다."
F(6, 34, "C", st="R", c=["Do they plays soccer?", "Do they play soccer?", "Does they play soccer?", "Are they play soccer?", "They play soccer?"], a=2, r=R634,
  n=["Do 뒤에는 동사원형 play를 써야 하므로 오답이다.", "복수 주어 they에 Do + 동사원형 play로 바르게 바꿨으므로 정답이다.", "복수 주어 they에는 Does가 아니라 Do를 써야 하므로 오답이다.", "일반동사 의문문에는 be동사 Are를 쓰지 않으므로 오답이다.", "평서문 어순에 물음표만 붙였으므로 오답이다."],
  s="발문이 ‘Do 또는 Does로 시작하는 기본형 의문문으로’라고 정답 형식을 알려 주었다. 원문항 발문으로 되돌리고, 조건이 없으면 문법적으로 가능한 과거 의문문(Did they play soccer?)을 be동사 오답으로 바꿨다. 정답 위치 ②.")
F(6, 34, "D", st="R", p="She drinks milk every morning.", c=["She drinks milk every morning?", "Do she drink milk every morning?", "Does she drinks milk every morning?", "Does she drink milk every morning?", "Did she drinks milk every morning?"], a=4, r=R634,
  n=["평서문 어순에 물음표만 붙였으므로 오답이다.", "3인칭 단수 주어 she에는 Do가 아니라 Does를 써야 하므로 오답이다.", "Does 뒤에는 동사원형 drink를 써야 하므로 오답이다.", "Does + 주어 + 동사원형 drink로 바르게 바꿨으므로 정답이다.", "현재 시제를 과거 Did로 바꿨고 Did 뒤에도 동사원형을 써야 하므로 오답이다."],
  s="제시문(He walks to the library.)과 정답이 원문항(He walks to school.)과 거의 같았고 발문이 정답 형식을 알려 주었다. 원문항 발문으로 되돌리고 제시문을 새로 썼다. 정답 위치 ④.")

# 6-35 옳은 문장: 평서문 오류를 섞고 서로 다른 문장으로 유형마다 새로
R635 = "일반동사 현재형은 3인칭 단수 주어에 -s/-es(자음 + y는 -ies)를 붙이고, Do/Does 뒤에는 동사원형을 쓴다. 3인칭 단수 주어의 의문문·부정문에는 Does/doesn't를 쓴다."
S635 = "원문항은 평서문 수 일치 오류와 의문문 오류를 섞어 판별하는데, 변형은 모두 의문문이거나 한 문장을 다섯 가지로 바꾼 것이었고 오답이 유형마다 같았다. 평서문 오류를 섞어 서로 다른 문장으로 유형마다 새로 썼다."
def f635(t, items, a, s=S635):
    FIX.pop((6, 35, t), None)
    mk(6, 35, t, items, a, R635, s)
f635("B", [("My brother watchs TV.", "watch는 ch로 끝나 -es를 붙여 watches로 써야 하므로"), ("Do she like music?", "3인칭 단수 주어 she에는 Does를 써야 하므로"), ("Do you like milk?", "주어 you에 Do + 동사원형 like를 바르게 썼으므로"), ("They plays soccer.", "복수 주어 They에는 동사원형 play를 써야 하므로"), ("Does Mr. Kim teaches science?", "Does 뒤에는 동사원형 teach를 써야 하므로")], 3,
     S635 + " 원문항 정답 문장을 틀리게 바꾼 보기(Does the store sells bread?)도 다른 문장으로 바꿨다.")
f635("C", [("The children needs more paper.", "복수 주어 The children에는 동사원형 need를 써야 하므로"), ("Does your dog bark at night?", "3인칭 단수 주어에 Does + 동사원형 bark를 바르게 썼으므로"), ("Mina carrys a big bag.", "carry는 자음 + y라 carries로 써야 하므로"), ("Do he live near here?", "3인칭 단수 주어 he에는 Does를 써야 하므로"), ("I goes to bed at ten.", "주어 I에는 동사원형 go를 써야 하므로")], 2)
f635("D", [("Jiho flys a kite.", "fly는 자음 + y라 flies로 써야 하므로"), ("She washs her car.", "wash는 sh로 끝나 -es를 붙여 washes로 써야 하므로"), ("Does we have time?", "주어 we에는 Do를 써야 하므로"), ("The bus stop here.", "3인칭 단수 주어 The bus에는 stops를 써야 하므로"), ("Do your parents cook dinner?", "복수 주어에 Do + 동사원형 cook을 바르게 썼으므로")], 5)
f635("E", [("Does Jane study English?", "3인칭 단수 주어에 Does + 동사원형 study를 바르게 썼으므로"), ("He trys his best.", "try는 자음 + y라 tries로 써야 하므로"), ("You looks tired.", "주어 You에는 동사원형 look을 써야 하므로"), ("Do the baby cry a lot?", "3인칭 단수 주어 the baby에는 Does를 써야 하므로"), ("My uncle teach math.", "3인칭 단수 주어 My uncle에는 teaches를 써야 하므로")], 1)
f635("F", [("The girls sings well.", "복수 주어 The girls에는 동사원형 sing을 써야 하므로"), ("Does it rains a lot here?", "Does 뒤에는 동사원형 rain을 써야 하므로"), ("Tom miss his mom.", "3인칭 단수 주어 Tom에는 misses를 써야 하므로"), ("Do they play soccer?", "복수 주어에 Do + 동사원형 play를 바르게 썼으므로"), ("We doesn't like carrots.", "주어 We에는 don't를 써야 하므로")], 4)

# 6-36 were가 들어갈 수 없는 문장: 원문항 발문, 유형마다 문장 새로
R636 = "be동사 과거형 were는 you·we·they와 복수 주어(A and B, 복수 명사)에 쓰고, I·3인칭 단수 주어에는 was를 쓴다."
S636 = "발문에 ‘과거의 실제 상황을 나타내는 평서문에서’가 붙었고, 선택지 네 개(We happy, They students, The boys busy, You ready)가 유형마다 같았다. 원문항 발문으로 되돌리고 유형마다 문장을 새로 썼다."
WR = lambda s_: f"{s_}: you·복수 주어라 were가 들어갈 수 있으므로"; WS = lambda s_: f"{s_}: 3인칭 단수 주어라 were가 아니라 was를 쓰므로"
def f636(t, items, a, s=S636):
    mk(6, 36, t, items, a, R636, s, st="R")
f636("C", [("Jane ________ kind.", WS("Jane")), ("Tom and I ________ hungry.", WR("Tom and I")), ("The windows ________ open.", WR("The windows")), ("You two ________ late.", WR("You two")), ("My friends ________ at the mall.", WR("My friends"))], 1)
f636("D", [("The flowers ________ pretty.", WR("The flowers")), ("Your parents ________ worried.", WR("Your parents")), ("The cat ________ sleepy.", WS("The cat")), ("We all ________ tired.", WR("We all")), ("Those shoes ________ cheap.", WR("Those shoes"))], 3)
f636("E", [("The kids ________ in the pool.", WR("The kids")), ("You ________ right.", WR("You")), ("Mike and Sara ________ classmates.", WR("Mike and Sara")), ("The cookies ________ delicious.", WR("The cookies")), ("She ________ at home.", WS("She"))], 5)
f636("F", [("They ________ excited.", WR("They")), ("The rooms ________ dark.", WR("The rooms")), ("My cousins ________ from Canada.", WR("My cousins")), ("Tom ________ busy.", WS("Tom")), ("You and your sister ________ kind.", WR("You and your sister"))], 4)

# 6-38 옳은 의문문: 원문항 발문, 오답을 유형마다 새로, E는 원문항과 다른 문장으로
S638 = "발문에 ‘주어가 직접 행동하는 뜻의 능동태 현재 의문문’이 붙었고 오답 네 개가 B와 똑같았다(E는 선택지가 원문항과 같았다). 원문항 발문으로 되돌리고 유형마다 오답을 새로 썼다."
def f638(t, items, a, s=S638):
    FIX.pop((6, 38, t), None)
    mk(6, 38, t, items, a, R_DO, s, st="R")
f638("C", [("Does your sister plays the violin?", "Does 뒤에는 동사원형 play를 써야 하므로"), ("Do Mina know the answer?", "3인칭 단수 주어 Mina에는 Does를 써야 하므로"), ("Is he want some water?", "일반동사 want의 의문문에는 be동사 Is가 아니라 Does를 써야 하므로"), ("Do your cousins live in Seoul?", "복수 주어에 Do + 동사원형 live를 바르게 썼으므로"), ("Does we need a map?", "주어 we에는 Do를 써야 하므로")], 4)
f638("D", [("Does the bird sings?", "Does 뒤에는 동사원형 sing을 써야 하므로"), ("Do he wear glasses?", "3인칭 단수 주어 he에는 Does를 써야 하므로"), ("Is your dad cook dinner?", "일반동사 cook의 의문문에는 be동사 Is가 아니라 Does를 써야 하므로"), ("Does they walk to school?", "복수 주어 they에는 Do를 써야 하므로"), ("Do we need help?", "주어 we에 Do + 동사원형 need를 바르게 썼으므로")], 5)
f638("E", [("Does the baby cries often?", "Does 뒤에는 동사원형 cry를 써야 하므로"), ("Does you want some cake?", "주어 you에는 Do를 써야 하므로"), ("Do your friends live nearby?", "복수 주어에 Do + 동사원형 live를 바르게 썼으므로"), ("Is Jane like dogs?", "일반동사 like의 의문문에는 be동사 Is가 아니라 Does를 써야 하므로"), ("Do it rain a lot in July?", "주어 it에는 Does를 써야 하므로")], 3,
     "정답(Do you have a pen?)과 선택지 네 개가 원문항과 똑같았다. 원문항과 다른 문장으로 선택지를 새로 썼다.")
f638("F", [("Does your brother drive a car?", "3인칭 단수 주어에 Does + 동사원형 drive를 바르게 썼으므로"), ("Do Tom have a bike?", "3인칭 단수 주어 Tom에는 Does를 써야 하므로"), ("Does the shop opens at nine?", "Does 뒤에는 동사원형 open을 써야 하므로"), ("Are they go to the gym?", "일반동사 go의 의문문에는 be동사 Are가 아니라 Do를 써야 하므로"), ("Do you knows her?", "Do 뒤에는 동사원형 know를 써야 하므로")], 1)

# 6-39 (A)(B) Do/Does: 원문항 발문, 정답 조합을 원문항(Does - Do)과 다르게
R639 = "(A)와 (B)의 주어를 각각 확인하여 3인칭 단수면 Does, I·you·we·they·복수 주어면 Do를 쓴다."
S639 = "정답 조합(Does - Do)이 원문항과 같았고 발문에 ‘현재형 일반동사 의문문이 되도록’이 붙었다. 원문항 발문으로 되돌리고 주어를 바꿔 정답 조합이 원문항과 다르게 했다."
def f639(t, p, items, a, s=S639):
    mk(6, 39, t, items, a, R639, s, st="R", p=p, okdup=True)
f639("B", "(A) ________ your dog like bones?\n(B) ________ your cat like fish?", [("Do - Does", "(A): 3인칭 단수 주어 your dog에는 Does를 쓰므로"), ("Does - Do", "(B): 3인칭 단수 주어 your cat에는 Does를 쓰므로"), ("Is - Is", "일반동사 like의 의문문에는 be동사를 쓰지 않으므로"),
     ("Does - Does", "두 주어 모두 3인칭 단수라 Does - Does가 맞으므로"), ("Do - Do", "두 주어 모두 3인칭 단수라 Does를 써야 하므로")], 4)
f639("D", "(A) ________ your classmates study together?\n(B) ________ you help them?", [("Does - Do", "(A): 복수 주어 your classmates에는 Do를 쓰므로"), ("Do - Do", "복수 주어와 you 모두 Do를 쓰므로"), ("Do - Does", "(B): 주어 you에는 Do를 쓰므로"),
     ("Does - Does", "복수 주어와 you에는 Does를 쓰지 않으므로"), ("Are - Are", "일반동사 study, help의 의문문에는 be동사를 쓰지 않으므로")], 2)
f639("E", "(A) ________ they read books every day?\n(B) ________ Jane read comic books?", [("Does - Do", "(A): 주어 they에는 Do를, (B): 3인칭 단수 Jane에는 Does를 쓰므로"), ("Do - Do", "(B): 3인칭 단수 주어 Jane에는 Does를 쓰므로"), ("Does - Does", "(A): 주어 they에는 Do를 쓰므로"),
     ("Are - Is", "일반동사 read의 의문문에는 be동사를 쓰지 않으므로"), ("Do - Does", "they에 Do, Jane에 Does를 바르게 짝지었으므로")], 5)

# 6-40 틀린 설명을 한 학생: 원문항 발문, C·E는 그 두 문장에 대한 설명으로 새로
R640 = "3인칭 단수 주어의 일반동사 의문문은 Does, 그 밖의 주어는 Do로 시작하고, Do/Does 뒤의 본동사는 동사원형으로 쓴다."
S640 = "오답 설명 네 개가 B와 똑같았다. 원문항처럼 제시된 두 문장을 직접 가리키는 설명으로 유형마다 새로 썼다."
def f640(t, items, a, s=S640):
    FIX.pop((6, 40, t), None)
    talk(6, 40, t, items, a, R640, s, st="R")
f640("C", [("서연: (가)와 (나)는 모두 일반동사 like의 의문문이야.", "두 문장 모두 일반동사 like를 Do/Does로 물었으므로"), ("민수: (가)의 주어 'she'는 한 명이므로 'Do'를 써야 해.", "she는 3인칭 단수라 Does를 써야 하므로"),
     ("지훈: (나)의 주어 we에는 Do를 쓰는 게 맞아.", "주어 we의 의문문은 Do로 시작하므로"), ("하은: (가)에서 like에 s를 붙이지 않은 건 Does 뒤에는 동사원형을 쓰기 때문이야.", "Does 뒤의 본동사는 동사원형이므로"),
     ("도윤: (나)의 주어를 'Tom and I'로 바꿔도 Do를 그대로 쓸 수 있어.", "Tom and I는 복수 주어라 Do를 쓰므로")], 2)
f640("E", [("예린: (가)의 Tom은 3인칭 단수라서 Does를 앞에 썼어.", "3인칭 단수 주어의 의문문은 Does로 시작하므로"), ("시우: (나)의 they는 복수라서 Do를 썼어.", "복수 주어의 의문문은 Do로 시작하므로"),
     ("채원: 두 문장 모두 일반동사 read의 의문문이라 Do나 Does로 시작했어.", "일반동사 의문문은 Do/Does로 시작하므로"), ("준서: (나)의 주어를 'your sister'로 바꿔도 그대로 Do를 쓸 수 있어.", "your sister는 3인칭 단수라 Does를 써야 하므로"),
     ("유리: (가)의 read에 s를 붙이지 않은 건 Does 뒤에는 동사원형을 쓰기 때문이야.", "Does 뒤의 본동사는 동사원형이므로")], 4)


# ---- 2차 감수(2026-10) 추가 ----
# 6-31 D·F: 원문항과 같은 짝(like - likes, do - does / have - has)과 원문항 정답을 바르게 고친 짝(fix - fixes)
R631 = "3인칭 단수 현재형은 대부분 -s를 붙이고, s·x·sh·ch·o로 끝나면 -es(washes, fixes, goes), 자음 + y는 y를 i로 바꾸고 -es(studies)를 붙인다. 모음 + y는 -s만 붙이고(plays), have는 has가 된다."
def f631(t, items, a, s):
    mk(6, 31, t, items, a, R631, s)
f631("D", [("enjoy - enjoys", "모음 + y라 -s만 붙인 옳은 형태이므로"), ("go - gos", "o로 끝나면 -es를 붙여 goes로 써야 하므로"), ("study - studies", "자음 + y라 y를 i로 바꾸고 -es를 붙인 옳은 형태이므로"), ("catch - catches", "ch로 끝나 -es를 붙인 옳은 형태이므로"), ("miss - misses", "s로 끝나 -es를 붙인 옳은 형태이므로")], 2,
     "보기 두 개(like - likes, do - does)가 원문항 ①·④와 똑같았다. 겹치는 짝을 다른 동사로 바꿨다. 정답은 그대로다.")
f631("F", [("wash - washes", "sh로 끝나 -es를 붙인 옳은 형태이므로"), ("cry - cries", "자음 + y라 y를 i로 바꾸고 -es를 붙인 옳은 형태이므로"), ("mix - mixes", "x로 끝나 -es를 붙인 옳은 형태이므로"), ("study - studys", "자음 + y라 y를 i로 바꾸고 -es를 붙여 studies로 써야 하므로"), ("go - goes", "o로 끝나 -es를 붙인 옳은 형태이므로")], 4,
     "②(have - has)는 원문항 ⑤와 똑같고 ③(fix - fixes)은 원문항 정답(fix - fixs)을 바르게 고친 짝이었다. 겹치는 짝을 다른 동사로 바꿨다. 정답은 그대로다.")
# 6-33 B·D·E: 서술어가 같은 두 문장이 주어만 달리해 나오고 그 하나가 정답 → 짝 문장을 다른 문장으로
R633 = "일반동사 현재 부정문은 주어가 3인칭 단수면 doesn't, I·you·we·they·복수 주어면 don't를 쓴다."
S633 = "서술어가 같은 두 문장이 주어만 달리해 함께 나오고 그 하나가 정답이어서, 두 문장만 견주면 답이 나왔다. 정답이 아닌 쪽을 다른 문장으로 바꿨다. 정답은 그대로다."
def f633(t, items, a, s=S633):
    forms = [f for _, _, f in items]; odd = forms[a - 1]
    its = [(x, f"주어 {sj}에는 {f}가 들어가" + (" 나머지와 다르므로" if i + 1 == a else "므로")) for i, (x, sj, f) in enumerate(items)]
    mk(6, 33, t, its, a, R633, s)
f633("B", [("Jane ________ like apples.", "Jane(3인칭 단수)", "doesn't"), ("We ________ need help.", "We", "don't"), ("The dog ________ sleep here.", "The dog(3인칭 단수)", "doesn't"), ("Tom ________ ride a bike.", "Tom(3인칭 단수)", "doesn't"), ("My dad ________ cook.", "My dad(3인칭 단수)", "doesn't")], 2)
f633("D", [("The dog ________ eat rice.", "The dog(3인칭 단수)", "doesn't"), ("Tom ________ wear glasses.", "Tom(3인칭 단수)", "doesn't"), ("My sister ________ read books.", "My sister(3인칭 단수)", "doesn't"), ("Jane ________ like music.", "Jane(3인칭 단수)", "doesn't"), ("The boys ________ play soccer.", "The boys(복수)", "don't")], 5)
f633("E", [("I ________ need help.", "I", "don't"), ("You ________ like milk.", "You", "don't"), ("They ________ play baseball.", "They", "don't"), ("Jane ________ read comics.", "Jane(3인칭 단수)", "doesn't"), ("We ________ study English.", "We", "don't")], 4)
# 6-38 B: 정답 문장의 틀린 짝(Is Tom read books?)과 원문항 정답의 틀린 형태(Do you has a pen?)
f638("B", [("Does she likes music?", "Does 뒤에는 동사원형 like를 써야 하므로"), ("Does Tom read books?", "3인칭 단수 주어 Tom에 Does + 동사원형 read를 바르게 썼으므로"), ("Do we needs more time?", "Do 뒤에는 동사원형 need를 써야 하므로"),
            ("Is your mom work at a bank?", "일반동사 work의 의문문은 Is가 아니라 Does로 시작해야 하므로"), ("Do they plays soccer?", "Do 뒤에는 동사원형 play를 써야 하므로")], 2,
     "발문에 ‘능동태 현재 의문문’ 조건이 붙었고, 정답 문장의 틀린 짝(④ Is Tom read books?)과 원문항 정답을 틀리게 바꾼 문장(③ Do you has a pen?)이 있었다. 원문항 발문으로 되돌리고 두 보기를 다른 문장으로 바꿨다. 정답은 그대로다.")
# 6-40 B: 한 줄짜리 일반 규칙 → 두 문장을 짚는 설명 / D·F: 서로 정반대인 설명 쌍 제거
f640("B", [("영수: (가)와 (나)는 모두 일반동사 need의 의문문이라 Do나 Does로 시작했어.", "일반동사의 의문문은 Do/Does로 시작하므로"), ("민지: (가)의 주어 he는 3인칭 단수라서 Does를 썼어.", "3인칭 단수 주어의 의문문은 Does로 시작하므로"),
            ("준호: (나)의 주어 the boys는 복수니까 Do 대신 Are를 써서 'Are the boys need help?'라고 해야 해.", "일반동사 need의 의문문에는 be동사 Are가 아니라 Do를 쓰므로"), ("수진: (가)에서 need에 s를 붙이지 않은 건 Does 뒤에 동사원형을 쓰기 때문이야.", "Does 뒤에는 동사원형을 쓰므로"),
            ("태호: (나)의 주어를 'they'로 바꿔도 Do를 그대로 쓸 수 있어.", "they도 복수 주어라 Do를 쓰므로")], 3,
     "발문이 원문항과 달랐고, 설명이 두 문장과 관계없는 한 줄짜리 일반 규칙이어서 원문항 보기(두 문장을 짚어 설명)의 절반 길이였다. 원문항 발문으로 되돌리고 (가)·(나)를 짚는 설명으로 바꿨다. 정답 위치는 그대로다.")
f640("D", [("유나: 두 문장 모두 일반동사 play의 의문문이야.", "두 문장 모두 일반동사 play를 Do/Does로 물었으므로"), ("하린: (가)의 주어를 'Mina'로 바꿔도 Does를 그대로 쓸 수 있어.", "Mina도 3인칭 단수 주어라 Does를 쓰므로"), ("태호: Does 뒤의 본동사는 plays로 써야 해.", "Does 뒤에는 동사원형 play를 써야 하므로"),
            ("민지: (나)의 복수 주어에는 Do를 써.", "Mina and Jane은 복수 주어라 Do를 쓰므로"), ("서준: (가)의 주어는 3인칭 단수이므로 Does가 필요해.", "your brother는 3인칭 단수 주어라 Does를 쓰므로")], 3,
     "발문이 원문항과 달랐고, 틀린 설명(③ Does 뒤는 plays)과 정반대인 옳은 설명(② Do/Does 뒤에는 동사원형)이 함께 있어 둘만 견주면 답이 나왔다. 원문항 발문으로 되돌리고 ②를 다른 설명으로 바꿨다. 정답은 그대로다.")
f640("F", [("하나: (가)의 주어를 'Mina and Jane'으로 바꾸면 Does를 Do로 바꿔야 해.", "Mina and Jane은 복수 주어라 Do를 쓰므로"), ("준: 두 문장 모두 일반동사 walk의 의문문이야.", "두 문장 모두 일반동사 walk를 Do/Does로 물었으므로"), ("민호: (가)의 Mina는 3인칭 단수라 Does를 써.", "3인칭 단수 주어의 의문문은 Does로 시작하므로"),
            ("지우: Does 뒤에는 동사원형 walk가 와.", "Does 뒤에는 동사원형을 쓰므로"), ("수빈: (나)의 twins는 두 명이지만 'Does'를 써야 해.", "the twins는 복수 주어라 Do를 써야 하므로")], 5,
     "발문이 원문항과 달랐고, 틀린 설명(⑤ twins에 Does)과 정반대인 옳은 설명(① (나)의 복수 주어에는 Do)이 함께 있어 둘만 견주면 답이 나왔다. 원문항 발문으로 되돌리고 ①을 다른 설명으로 바꿨다. 정답은 그대로다.")
