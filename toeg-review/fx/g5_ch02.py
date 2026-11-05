# 5급 CH2 be동사·일반동사 현재형 (11~20) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
R_PR = "현재 시제에서 3인칭 단수 주어의 일반동사에는 -s/-es를 붙이고(자음 + y는 y를 i로 바꾸고 -es), 그 밖의 주어에는 동사원형을 쓴다. be동사는 I에 am, 3인칭 단수에 is, you·복수에 are를 쓴다."

# 5-11 3인칭 단수 현재형: 원문항 발문과 우리말, 실제로 나오는 오류 형태의 오답
S511 = "오답에 없는 형태(studiesing, to studie 등)가 여럿이라 쉽게 지워졌다. 원문항처럼 be + 동사원형, be + -s형, 동사원형, -ing형 같은 실제로 나오는 오류 형태로 오답을 바꿨다."
F(5, 11, "B", st="R", p="아기는 배가 고플 때 운다.\n" + V(5, 11, "B")["passage"], s="원문항의 우리말 해석이 빠지고 발문이 바뀌었다. 원문항 발문과 우리말 해석으로 되돌렸다. 보기와 정답은 그대로다.")
def f511(t, ko, en, v3, base, a, order):
    why = {v3: f"3인칭 단수 주어라 -s형({v3})을 쓰므로", f"is {base}": "일반동사 앞에 be동사를 쓸 수 없으므로", f"is {v3}": "일반동사 앞에 be동사를 쓸 수 없으므로",
           base: "3인칭 단수 주어에는 -s/-es를 붙여야 하므로", base + "ing" if not base.endswith("n") else base + "ning": "-ing형만으로는 동사 자리에 쓸 수 없으므로"}
    mk(5, 11, t, [(x, why[x]) for x in order], a, R_PR, S511, st="R", p=f"{ko}\n{en}", okdup=True)
f511("C", "Tom은 영어를 공부한다.", "Tom _______(study) English.", "studies", "study", 2, ["is study", "studies", "is studies", "study", "studying"])
f511("D", "그 소년은 TV를 본다.", "The boy _______(watch) TV.", "watches", "watch", 1, ["watches", "is watch", "watch", "is watches", "watching"])
f511("E", "Jane은 상자를 나른다.", "Jane _______(carry) a box.", "carries", "carry", 3, ["carry", "is carries", "carries", "carrying", "is carry"])
f511("F", "그 개는 빨리 달린다.", "The dog _______(run) fast.", "runs", "run", 5, ["is run", "running", "run", "is runs", "runs"])

# 5-12 be동사 짝: 원문항처럼 문장별 우리말 해석, E는 정답 조합을 새로
S512 = "원문항의 문장별 우리말 해석이 빠졌다. 원문항처럼 우리말 해석을 붙였다. 보기와 정답은 그대로다."
for t, k1, k2 in [("B", "나는 여행 갈 준비가 되어 있다.", "그들은 지금 밖에 있니?"), ("C", "나는 배가 고프다.", "그들은 준비되었니?"), ("D", "Tom은 집에 있다.", "너는 바쁘니?"), ("F", "Jane은 행복하다.", "내가 늦었니?")]:
    l1, l2 = V(5, 12, t)["passage"].split("\n")
    F(5, 12, t, st="R", p=f"{l1} ({k1})\n{l2} ({k2})", s=S512)
mk(5, 12, "E", [("am - Is", "주어 You에는 are, 주어 we에는 Are를 쓰므로"), ("is - Are", "주어 You에는 are를 쓰므로"), ("are - Am", "주어 we에는 Are를 쓰므로"), ("are - Are", "You에 are, we에 Are를 바르게 썼으므로"), ("is - Is", "You와 we에는 모두 are를 쓰므로")], 4,
   "be동사는 I에 am, 3인칭 단수에 is, you·복수(we, they)에 are를 쓴다.", "정답 조합(are - Is)이 원문항과 같았다. 문장을 새로 써서 정답 조합을 are - Are로 바꾸고 우리말 해석을 붙였다.",
   st="R", p="You _______ my best friend. (너는 나의 가장 친한 친구이다.)\n_______ we late? (우리가 늦었니?)", okdup=True)

# 5-13 동사 형태가 틀린 문장: 원문항 발문, 짝 없이 유형마다 새로(be동사 문장 포함)
S513 = "정답 문장과 같은 문장의 옳은 형태가 함께 있어 대비 단서가 되었고 오답 네 개가 유형마다 같았다. 짝 문장 없이 유형마다 새로 썼고 원문항처럼 be동사 문장도 넣었다."
OK13 = "주어에 맞는 동사 형태를 바르게 썼으므로"
def f513(t, items, a, s=S513):
    mk(5, 13, t, [(x, w or OK13) for x, w in items], a, R_PR, s, st="R")
F(5, 13, "B", st="R", s="발문이 ‘현재형 일반동사의 형태’로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f513("C", [("My dad watches TV.", ""), ("Jane go to school by bus.", "3인칭 단수 주어 Jane에는 goes를 써야 하므로"), ("They have two dogs.", ""), ("The students are in the gym.", ""), ("Tom studies English.", "")], 2)
f513("D", [("Mina fixes her bike.", ""), ("We are good friends.", ""), ("My brother play soccer.", "3인칭 단수 주어 My brother에는 plays를 써야 하므로"), ("The birds sing in the morning.", ""), ("She tries her best.", "")], 3)
f513("E", [("The sun rises in the east.", ""), ("You are very kind.", ""), ("My uncle has a car.", ""), ("The girls dances well.", "복수 주어 The girls에는 dance를 써야 하므로"), ("Dad washes the dishes.", "")], 4)
f513("F", [("Jane is my sister.", ""), ("My cat sleeps a lot.", ""), ("They watch movies on Fridays.", ""), ("He carries a heavy bag.", ""), ("The kids is in the park.", "복수 주어 The kids에는 are를 써야 하므로")], 5)

# 5-14 부정문 틀린 문장: 원문항 발문, be동사 부정과 do 부정을 섞어 유형마다 새로
R514 = "be동사 부정은 am not, isn't, aren't로, 일반동사 현재 부정은 3인칭 단수 주어에 doesn't + 동사원형, 그 밖에는 don't + 동사원형으로 쓴다."
S514 = "원문항은 be동사 부정과 do 부정을 섞어 판별하는데, 변형은 모두 don't/doesn't 문장이라 범위가 좁았고 짝 문장과 같은 오답이 반복되었으며 발문도 달랐다. 원문항 발문으로 되돌리고 be동사 부정문을 섞어 유형마다 새로 썼다."
OK14 = "주어에 맞는 부정 형태를 바르게 썼으므로"
def f514(t, items, a, s=S514):
    mk(5, 14, t, [(x, w or OK14) for x, w in items], a, R514, s, st="R")
f514("B", [("They aren't hungry.", ""), ("Tom doesn't drink coffee.", ""), ("I'm not a student.", ""), ("The dog doesn't bark at night.", ""), ("Mina doesn't studies after dinner.", "doesn't 뒤에는 동사원형 study를 써야 하므로")], 5,
     S514 + " 정답 위치도 원문항(③)과 겹치지 않게 했다.")
f514("C", [("We aren't late.", ""), ("My sister doesn't like milk.", ""), ("The shop isn't open today.", ""), ("He don't play games.", "3인칭 단수 주어 He에는 doesn't를 써야 하므로"), ("I don't need a new bag.", "")], 4)
f514("D", [("You aren't alone.", ""), ("They don't live here.", ""), ("Jane isn't a nurse.", ""), ("Tom doesn't eat meat.", ""), ("The kids isn't at school.", "복수 주어 The kids에는 aren't를 써야 하므로")], 5)
f514("E", [("She doesn't watch TV.", ""), ("My parents doesn't work on Sundays.", "복수 주어 My parents에는 don't를 써야 하므로"), ("I am not tired.", ""), ("It isn't cold today.", ""), ("We don't have class today.", "")], 2)
f514("F", [("He doesn't goes to the gym.", "doesn't 뒤에는 동사원형 go를 써야 하므로"), ("Tom isn't hungry now.", ""), ("They aren't at home.", ""), ("I don't know his name.", ""), ("Jane doesn't speak Chinese.", "")], 1)

# 5-15 질문과 대답 짝: 원문항 발문, be동사·do 질문을 섞고 대답의 오류로
R515 = "be동사 의문문에는 be동사로, Do/Does 의문문에는 do/does로 답하며, 대답의 주어는 질문의 주어에 맞춘다(you → I, this → it)."
S515 = "원문항은 be동사/do 질문과 대답을 섞어 판별하는데, 변형은 모두 be동사 질문이었거나 오답이 질문의 형태 오류였고 짝 대화와 같은 오답이 반복되었다. 원문항 발문으로 되돌리고 be동사·do 질문을 섞어 대답의 오류로 유형마다 새로 썼다."
OK15 = "질문의 동사와 주어에 맞게 바르게 대답했으므로"
def f515(t, items, a, s=S515):
    mk(5, 15, t, [(x, w or OK15) for x, w in items], a, R515, s, st="R")
f515("B", [("A: Do you like pizza? B: Yes, I am.", "Do 의문문에는 do로 답하므로"), ("A: Is Tom your brother? B: No, he doesn't.", "be동사 의문문에는 isn't로 답하므로"), ("A: Are the cookies fresh? B: Yes, they are.", ""),
           ("A: Does she swim well? B: Yes, she do.", "주어 she에는 does로 답하므로"), ("A: Are you tired? B: Yes, you are.", "you에 대한 질문에는 I로 답하므로")], 3)
f515("C", [("A: Does your dad cook? B: Yes, he does.", ""), ("A: Are you hungry? B: No, I don't.", "be동사 의문문에는 I'm not으로 답하므로"), ("A: Is it your bag? B: Yes, it does.", "be동사 의문문에는 is로 답하므로"),
           ("A: Do they play tennis? B: Yes, they are.", "Do 의문문에는 do로 답하므로"), ("A: Is Jane at home? B: No, she aren't.", "주어 she에는 isn't로 답하므로")], 1)
f515("D", [("A: Do you know him? B: No, I am not.", "Do 의문문에는 don't로 답하므로"), ("A: Is the cat sleeping? B: Yes, it does.", "be동사 의문문에는 is로 답하므로"), ("A: Does Mina like cats? B: No, she don't.", "주어 she에는 doesn't로 답하므로"),
           ("A: Are we late? B: No, we don't.", "be동사 의문문에는 aren't로 답하므로"), ("A: Are your friends here? B: Yes, they are.", "")], 5)
f515("E", [("A: Is this your pen? B: Yes, I am.", "this는 it으로 받아 Yes, it is로 답하므로"), ("A: Do you have a pet? B: No, I don't.", ""), ("A: Does Tom walk to school? B: Yes, he is.", "Does 의문문에는 be동사가 아니라 does로 답하므로"),
           ("A: Are they students? B: Yes, they do.", "be동사 의문문에는 are로 답하므로"), ("A: Is he tall? B: No, he doesn't.", "be동사 의문문에는 isn't로 답하므로")], 2)
f515("F", [("A: Does it rain a lot here? B: Yes, it is.", "Does 의문문에는 does로 답하므로"), ("A: Am I right? B: Yes, I am.", "I에 대한 질문에는 you로 받아 Yes, you are로 답하므로"), ("A: Do your parents work? B: No, they aren't.", "Do 의문문에는 don't로 답하므로"),
           ("A: Is Jane your friend? B: Yes, she is.", ""), ("A: Does he like music? B: Yes, he do.", "주어 he에는 does로 답하므로")], 4)

# 5-16 Does/Do 질문의 대답: 같은 주어에 동사만 틀린 오답
R516 = "Do/Does 의문문에는 Yes, 주어 + do/does. / No, 주어 + don't/doesn't.로 짧게 답한다. 주어가 3인칭 단수면 does, 그 밖에는 do를 쓴다."
S516 = "원문항 오답은 같은 주어에 동사만 틀린 대답인데, 변형 오답은 주어가 맞지 않는 대답이라 바로 지워졌고 유형마다 반복되었다. 원문항처럼 같은 주어의 틀린 대답으로 오답을 새로 썼다."
def f516(t, p, items, a, s=S516):
    mk(5, 16, t, items, a, R516, s, p=p, okdup=True)
f516("C", "Does Tom like pizza?", [("No, he isn't.", "Does 의문문에는 be동사로 답하지 않으므로"), ("No, he don't.", "3인칭 단수 he에는 doesn't를 쓰므로"), ("No, he doesn't.", "Does 의문문에 doesn't로 바르게 답했으므로"), ("No, he likes.", "짧은 대답에는 does/doesn't를 쓰고 뜻도 맞지 않으므로"), ("No, he can't.", "Does 의문문에는 can으로 답하지 않으므로")], 3)
f516("D", "Do your parents work?", [("Yes, they do.", "Do 의문문에 do로 바르게 답했으므로"), ("Yes, they are.", "Do 의문문에는 be동사로 답하지 않으므로"), ("Yes, they does.", "복수 they에는 do를 쓰므로"), ("Yes, they works.", "짧은 대답에는 do를 쓰므로"), ("Yes, they can.", "Do 의문문에는 can으로 답하지 않으므로")], 1)
f516("E", "Do you study English?", [("No, I am not.", "Do 의문문에는 be동사로 답하지 않으므로"), ("No, I doesn't.", "주어 I에는 don't를 쓰므로"), ("No, I can't.", "Do 의문문에는 can으로 답하지 않으므로"), ("No, I don't.", "Do 의문문에 don't로 바르게 답했으므로"), ("No, I not study.", "부정은 don't로 만들므로")], 4)
f516("F", "Does the dog sleep here?", [("Yes, it is.", "Does 의문문에는 be동사로 답하지 않으므로"), ("Yes, it does.", "Does 의문문에 does로 바르게 답했으므로"), ("Yes, it do.", "3인칭 단수 it에는 does를 쓰므로"), ("Yes, it sleeps.", "짧은 대답에는 does를 쓰므로"), ("Yes, it can.", "Does 의문문에는 can으로 답하지 않으므로")], 2)

# 5-17 원문항 발문
S517 = "발문이 원문항과 달랐고, 일부는 빈칸마다 넣을 동사까지 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
for t in "BCDEF": F(5, 17, t, st="R", s=S517)

# 5-18 어색한 축약형: 원문항처럼 잘못 만든 축약형을 정답으로, 짝 없이 유형마다 새로
ST518 = "다음 중 밑줄 친 축약형의 쓰임이 어법상 어색한 문장을 고르세요."
R518 = "be동사 축약형은 I'm, you're, he's, she's, it's, we're, they're와 isn't, aren't로 쓴다. 아포스트로피(')는 빠진 글자 자리에 찍으며, I'am, She'is, is'nt 같은 형태는 없다."
S518 = "원문항은 잘못 만든 축약형(amn't)을 찾는 문항인데, 변형은 isn't/aren't의 수 일치 오류를 찾게 해 평가 요소가 달랐고, 짝 문장과 같은 오답이 반복되었다. 원문항처럼 잘못 만든 축약형을 정답으로 하여 유형마다 새로 썼다."
OK18 = "축약형을 바르게 만들어 썼으므로"
def f518(t, items, a, s=S518):
    mk(5, 18, t, [(x, w or OK18) for x, w in items], a, R518, s, st=ST518)
f518("B", [("They<u>'re</u> in the library.", ""), ("We <u>aren't</u> ready.", ""), ("I<u>'m</u> not sure.", ""), ("He <u>is'nt</u> hungry.", "is not의 축약형은 isn't로, 아포스트로피는 o 자리에 찍으므로"), ("It<u>'s</u> cold today.", "")], 4,
     "정답(We isn't)이 원문항(amn't)과 달리 수 일치 오류를 물었다. 원문항처럼 잘못 만든 축약형(is'nt)을 정답으로 새로 썼다.")
f518("C", [("You<u>'re</u> late.", ""), ("She<u>'is</u> my sister.", "She is의 축약형은 She's이므로"), ("We <u>aren't</u> busy.", ""), ("It <u>isn't</u> my bag.", ""), ("I<u>'m</u> fine.", "")], 2)
f518("D", [("He<u>'s</u> a doctor.", ""), ("They <u>aren't</u> here.", ""), ("I<u>'am</u> not tired.", "I am의 축약형은 I'm이므로"), ("She <u>isn't</u> sad.", ""), ("We<u>'re</u> classmates.", "")], 3)
f518("E", [("We<u>'re</u> ready.", ""), ("You <u>aren't</u> alone.", ""), ("It<u>'s</u> my turn.", ""), ("I<u>'m</u> not angry.", ""), ("They <u>are'nt</u> at school.", "are not의 축약형은 aren't로, 아포스트로피는 o 자리에 찍으므로")], 5)
f518("F", [("She <u>isnt</u> here.", "is not의 축약형에는 아포스트로피를 찍어 isn't로 쓰므로"), ("They<u>'re</u> brothers.", ""), ("I<u>'m</u> sleepy.", ""), ("He <u>isn't</u> busy.", ""), ("We <u>aren't</u> late.", "")], 1)

# 5-19 y → ies 규칙: B 원문항 발문, C~F는 <보기>와 오답을 새로
F(5, 19, "B", st="R", s="발문에 ‘3인칭 단수형’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
R519 = "자음 + y로 끝나는 동사는 y를 i로 바꾸고 -es를 붙인다(study → studies). 모음 + y는 -s만 붙이고(play → plays), -s·-sh·-ch·-x·-o로 끝나면 -es를 붙인다."
S519 = "<보기>가 원문항과 똑같았고(studies, carries) 오답 묶음이 유형마다 같았으며, 일부는 정답이 <보기>의 동사 그대로였다. <보기> 동사와 오답을 유형마다 새로 썼다."
YIES = "자음 + y로 끝나 y를 i로 바꾸고 -es를 붙이는 동사들이라 <보기>와 같으므로"
VY = "모음 + y로 끝나 -s만 붙이므로"; ES = "-s·-sh·-ch·-x·-o로 끝나 -es만 붙이므로"; S = "-s만 붙이는 동사들이므로"; IRR = "불규칙하게 변하거나 다른 규칙을 따르므로"
def f519(t, bogi, items, a, s=S519):
    mk(5, 19, t, items, a, R519, s, st="R", p="<보기>\n" + bogi, okdup=True)
f519("C", "My brother <u>tries</u> hard.\nThe baby <u>cries</u> at night.", [("watch, wash", ES), ("worry, study", YIES), ("play, stay", VY), ("go, do", ES), ("like, make", S)], 2)
f519("D", "She <u>worries</u> a lot.\nHe <u>hurries</u> to school.", [("fix, mix", ES), ("enjoy, say", VY), ("copy, fly", YIES), ("teach, catch", ES), ("have, go", IRR)], 3)
f519("E", "The bird <u>flies</u> high.\nMom <u>dries</u> the clothes.", [("buy, pray", VY), ("push, finish", ES), ("come, write", S), ("carry, marry", YIES), ("do, go", ES)], 4)
f519("F", "Tom <u>copies</u> the notes.\nShe <u>replies</u> quickly.", [("study, bury", YIES), ("kiss, pass", ES), ("play, enjoy", VY), ("wash, brush", ES), ("have, do", IRR)], 1)

# 5-20 Do/Be 의문문 설명: B 원문항 발문, D~F는 그럴듯한 오개념 오답을 새로
F(5, 20, "B", st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
R520 = "일반동사 의문문은 Do/Does + 주어 + 동사원형(3인칭 단수 주어면 Does), be동사 의문문은 Am/Is/Are + 주어 + 보어·장소로 만든다."
S520 = "설명 오답 네 개가 C와 똑같았다. 원문항처럼 그럴듯한 오개념으로 유형마다 오답 설명을 새로 썼다."
OK20 = "두 빈칸에 들어갈 말과 그 이유를 바르게 설명했으므로"
def f520(t, items, a, s=S520):
    mk(5, 20, t, items, a, R520, s)
f520("D", [("(A)와 (B) 모두 주어가 they이므로 Are를 써야 한다.", "(A)에는 일반동사 study가 있어 Do를 써야 하므로"), ("(A)는 영어를 공부하는 능력을 묻는 것이므로 Can만 쓸 수 있다.", "능력을 묻는 문장이 아니고 Do로 물을 수 있으므로"),
           ("(A)는 복수 주어의 일반동사 의문문이라 Do, (B)는 be동사 문장이라 Are를 쓴다.", OK20), ("(A)는 주어가 복수이므로 Does, (B)는 명사가 복수이므로 Is를 쓴다.", "복수 주어에는 Do와 Are를 쓰므로"),
           ("둘 다 일반적인 사실을 묻는 질문이라 Do를 쓰는 것이 원칙이다.", "(B)는 일반동사가 없는 be동사 문장이므로")], 3)
f520("E", [("(A)는 3인칭 단수 일반동사 의문문이라 Does, (B)는 장소를 묻는 be동사 문장이라 Is를 쓴다.", OK20), ("둘 다 주어가 Tom이므로 Is를 써야 한다.", "(A)에는 일반동사 read가 있어 Does를 써야 하므로"),
           ("(A)는 과거의 일일 수 있으므로 Did만 쓸 수 있다.", "과거를 나타내는 말이 없고 현재의 습관을 묻는 문장이므로"), ("(A)는 read가 있으므로 Do, (B)는 at home이 있으므로 Does를 쓴다.", "3인칭 단수 Tom에는 Does를, (B)에는 Is를 쓰므로"),
           ("두 문장 모두 Tom이 한 명이므로 Does를 쓴다.", "(B)는 일반동사가 없는 be동사 문장이므로")], 1)
f520("F", [("두 문장 모두 주어가 we이므로 Do를 쓴다.", "(B)는 일반동사가 없는 be동사 문장이므로"), ("(A)는 도움이 필요한지 묻는 것이라 Are, (B)는 준비를 묻는 것이라 Do를 쓴다.", "일반동사 need가 있는 (A)에 Do, 형용사 ready 앞 (B)에 Are를 쓰므로"),
           ("(A)는 주어가 복수이므로 Does를 쓰고, (B)는 Is를 쓴다.", "복수 주어에는 Do와 Are를 쓰므로"), ("두 문장 모두 형용사가 있으므로 Are를 쓴다.", "(A)에는 형용사가 아니라 일반동사 need가 있으므로"),
           ("(A)는 일반동사 need가 있어 Do, (B)는 형용사 ready 앞 be동사 문장이라 Are를 쓴다.", OK20)], 5)


# ---- 2차 감수(2026-10) 추가 ----
# 5-16 B: 오답의 주어 형태가 틀려(him, its) 형태만으로 지워짐 → 원문항처럼 같은 주어에 동사만 다른 대답으로
mk(5, 16, "B", [("Yes, it is.", "Does 의문문에는 be동사로 답하지 않으므로"), ("Yes, it do.", "3인칭 단수 it에는 does를 쓰므로"), ("Yes, it does.", "Does 의문문에 does로 바르게 답했으므로"),
     ("Yes, it barks.", "짧은 대답에는 일반동사가 아니라 does를 쓰므로"), ("Yes, it can.", "Does 의문문에는 can으로 답하지 않으므로")], 3, R516,
     "발문이 원문항과 달랐고, 오답 세 개(Yes, him does. / Yes, its does. / No, it not.)는 주어나 부정의 형태부터 틀려 대답의 규칙을 몰라도 지워졌다. 원문항 발문으로 되돌리고, 원문항처럼 같은 주어에 동사만 다른 대답으로 오답을 썼다.", st="R", p="Does your dog bark when strangers come?")

# 5-20 B, C: 정답만 길고 구체적이며 오답은 한 줄짜리 일반론 → 원문항처럼 그럴듯한 오개념으로
FIX.pop((5, 20, "B"), None)
S520L = "정답만 (A)·(B)를 나누어 길게 설명하고 오답 네 개는 한 줄짜리 일반론이라 길이만으로 정답이 드러났다. 원문항처럼 모든 보기를 (A)·(B)에 대한 그럴듯한 설명으로 썼다."
mk(5, 20, "B", [("(A)와 (B) 모두 주어가 Mina이므로 Is를 써야 한다.", "(A)에는 일반동사 read가 있어 Does를 써야 하므로"), ("(A)는 일반동사 read가 있으므로 Does를 쓰고, (B)는 뒤에 명사가 와서 상태를 묻는 be동사 문장이므로 Is를 쓴다.", OK20),
           ("(A)는 매주 되풀이되는 일이므로 Do를 쓰고, (B)는 Is를 쓴다.", "주어 Mina가 3인칭 단수라 Do가 아니라 Does를 쓰므로"), ("(A)는 책을 읽는 능력을 묻는 것이므로 Can만 가능하고, (B)는 Does를 쓴다.", "능력을 묻는 문장이 아니고 (B)에는 be동사가 필요하므로"),
           ("(A)와 (B) 모두 Mina 한 사람에 대해 묻고 있으므로 둘 다 Does를 써야 한다.", "(B)에는 일반동사가 없어 Does를 쓸 수 없으므로")], 2, R520,
     "발문이 원문항과 달랐고, " + S520L + " 원문항 발문으로 되돌렸다.", st="R")
f520("C", [("(A)와 (B) 모두 주어가 she이므로 Is를 써야 한다.", "(A)에는 일반동사 like가 있어 Does를 써야 하므로"), ("(A)는 좋아하는 것을 묻는 것이므로 Is를 쓰고, (B)는 직업을 묻는 것이므로 Does를 쓴다.", "두 자리를 반대로 설명했으므로"),
           ("(A)는 일반동사 like가 있지만 주어가 한 명이므로 Do를 쓰고, (B)는 Is를 쓴다.", "3인칭 단수 주어에는 Do가 아니라 Does를 쓰므로"),
           ("(A)는 3인칭 단수 주어의 일반동사 의문문이라 Does를 쓰고, (B)는 뒤에 명사(a singer)가 오는 be동사 문장이라 Is를 쓴다.", OK20), ("둘 다 현재의 사실을 묻는 질문이므로 Does를 쓰는 것이 원칙이다.", "(B)에는 일반동사가 없어 Does를 쓸 수 없으므로")], 4, S520L)
