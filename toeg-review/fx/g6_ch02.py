# 6급 CH2 인칭대명사·be동사·지시대명사 (11~20) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."

# 원문항 발문으로만 되돌리는 문항
for t in "BCDE": F(6, 13, t, st="R", s="발문에 ‘현재형 be동사를 사용하여’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDEF": F(6, 17, t, st="R", s="발문에 ‘우리말의 거리·수에 맞게’, ‘(첫 빈칸에서는 소문자로 쓴다.)’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDEF": F(6, 20, t, st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 6-11 주격 대명사: 정답 짝을 원문항(you and I - you)과 다르게
R611 = "사람·사물을 대신할 때 나를 포함한 여럿은 we, 너를 포함한 여럿(나 제외)은 you, 그 밖의 여럿은 they, 남자 한 명은 he, 여자 한 명은 she, 사물·동물 하나는 it으로 받는다."
S611 = "정답 짝(you and I - you)이 원문항과 같았다. 정답 짝을 원문항과 다르게 새로 썼다."
def f611(t, items, a, s=S611):
    FIX.pop((6, 11, t), None)
    mk(6, 11, t, items, a, R611, s)
f611("B", [("my sister and I - they", "my sister and I: 나를 포함한 여럿이라 we로 받아야 하므로"), ("my grandmother - she", "my grandmother: 여자 한 명이라 she로 바르게 받았으므로"), ("the dog - it", "the dog: 동물 하나라 it으로 바르게 받았으므로"),
           ("Tom and Jerry - they", "Tom and Jerry: 나와 너를 포함하지 않는 여럿이라 they로 바르게 받았으므로"), ("my uncle - he", "my uncle: 남자 한 명이라 he로 바르게 받았으므로")], 1)
f611("F", [("my aunt - she", "my aunt: 여자 한 명이라 she로 바르게 받았으므로"), ("Mr. Kim - he", "Mr. Kim: 남자 한 명이라 he로 바르게 받았으므로"), ("the books - it", "the books: 여러 권이라 they로 받아야 하므로"),
           ("my brother and I - we", "my brother and I: 나를 포함한 여럿이라 we로 바르게 받았으므로"), ("you and Jiho - you", "you and Jiho: 너를 포함한 여럿이라 you로 바르게 받았으므로")], 3)

# 6-12 be동사가 다른 것: 원문항 문장을 되풀이하지 않고 새로
R612 = "현재형 be동사는 주어가 I면 am, 3인칭 단수(he, she, it, 사람 한 명, 셀 수 없는 명사)면 is, you·we·they와 복수 주어(A and B 포함)면 are를 쓴다."
S612 = "원문항 문장(It ____ on the desk, You ____ very kind, We ____ busy 등)을 명사 한두 개만 바꿔 그대로 썼고 정답 문장도 같았다. 문장을 새로 쓰고, 유형에 따라 is 네 개 속 are 하나, are 네 개 속 am 하나처럼 다른 조합도 넣었다."
def f612(t, items, a, s=S612):
    mk(6, 12, t, items, a, R612, s)
f612("B", [("The children _______ in the garden.", "The children: 복수 주어라 are가 들어가 나머지와 같으므로"), ("My shoes _______ too small.", "My shoes: 복수 주어라 are가 들어가 나머지와 같으므로"), ("Mr. Brown _______ our new teacher.", "Mr. Brown: 3인칭 단수 주어라 is가 들어가 나머지(are)와 다르므로"),
           ("Jiho and his dog _______ good friends.", "Jiho and his dog: 복수 주어라 are가 들어가 나머지와 같으므로"), ("You and Tom _______ late again.", "You and Tom: 복수 주어라 are가 들어가 나머지와 같으므로")], 3)
f612("C", [("The water _______ very cold.", "The water: 셀 수 없는 명사라 is가 들어가 나머지와 같으므로"), ("Your idea _______ great.", "Your idea: 3인칭 단수 주어라 is가 들어가 나머지와 같으므로"), ("This bag _______ heavy.", "This bag: 3인칭 단수 주어라 is가 들어가 나머지와 같으므로"),
           ("Mina and Sumi _______ twins.", "Mina and Sumi: 복수 주어라 are가 들어가 나머지(is)와 다르므로"), ("My room _______ clean.", "My room: 3인칭 단수 주어라 is가 들어가 나머지와 같으므로")], 4)
f612("D", [("I _______ hungry now.", "I: 주어 I에는 am이 들어가 나머지(are)와 다르므로"), ("Tom and I _______ classmates.", "Tom and I: 복수 주어라 are가 들어가 나머지와 같으므로"), ("The cookies _______ sweet.", "The cookies: 복수 주어라 are가 들어가 나머지와 같으므로"),
           ("Those boys _______ tall.", "Those boys: 복수 주어라 are가 들어가 나머지와 같으므로"), ("You _______ my best friend.", "You: 주어 you에는 are가 들어가 나머지와 같으므로")], 1)
f612("E", [("The weather _______ nice today.", "The weather: 3인칭 단수 주어라 is가 들어가 나머지와 같으므로"), ("He _______ at the library.", "He: 3인칭 단수 주어라 is가 들어가 나머지와 같으므로"), ("My phone _______ in my bag.", "My phone: 3인칭 단수 주어라 is가 들어가 나머지와 같으므로"),
           ("The movie _______ really funny.", "The movie: 3인칭 단수 주어라 is가 들어가 나머지와 같으므로"), ("Your glasses _______ on the table.", "Your glasses: 복수 주어라 are가 들어가 나머지(is)와 다르므로")], 5)
f612("F", [("We _______ in the same class.", "We: 복수 주어라 are가 들어가 나머지와 같으므로"), ("The baby _______ asleep.", "The baby: 3인칭 단수 주어라 is가 들어가 나머지(are)와 다르므로"), ("The pens _______ in the box.", "The pens: 복수 주어라 are가 들어가 나머지와 같으므로"),
           ("My father and mother _______ doctors.", "My father and mother: 복수 주어라 are가 들어가 나머지와 같으므로"), ("They _______ from Canada.", "They: 복수 주어라 are가 들어가 나머지와 같으므로")], 2)

# 6-13 F: 원문항 발문으로 되돌리면 Were - weren't도 답이 되어 보기를 바꿈
F(6, 13, "F", st="R", c=["Are - aren't", "Are - is", "Is - isn't", "Is - are", "Are - are"], a=1,
  n=["복수 주어 those에 Are, 부정 대답에 they aren't를 바르게 썼으므로 정답이다.", "대답의 주어 they에는 is가 아니라 aren't를 써야 하므로 오답이다.", "복수 주어 those에는 Is가 아니라 Are를 써야 하므로 오답이다.", "복수 주어 those에는 Is가 아니라 Are를 쓰고, No 대답에는 aren't를 써야 하므로 오답이다.", "No로 답했으므로 are가 아니라 aren't를 써야 하므로 오답이다."],
  s="발문에 ‘현재형 be동사를 사용하여’가 붙었다. 원문항 발문으로 되돌리면 보기 ‘Were - weren't’도 답이 될 수 있어, 이 보기를 ‘Are - is’로 바꿨다. 정답 위치 ①.")

# 6-14 소유격 밑줄: 원문항 문장을 되풀이하지 않고 새로, 오류 대명사도 유형마다 다르게
R614 = "명사 앞에서 소유를 나타낼 때는 소유격(my, your, his, her, its, our, their)이나 명사 + ’s를 쓴다. 주격(I, he, she, we, they)이나 목적격(him)을 명사 앞에 쓰지 않는다."
S614 = "원문항 문장(This is not he ___, These are her shoes, This is my girlfriend 등)을 명사 한두 개만 바꿔 그대로 썼고 정답 문장도 같았다. 문장을 새로 쓰고, 잘못 쓴 대명사도 유형마다 다르게 했다."
OK14 = "명사 앞에 소유격을 바르게 썼으므로"; OKS = "명사 앞에 명사 + ’s로 소유를 바르게 나타냈으므로"
def f614(t, items, a, s=S614):
    mk(6, 14, t, [(x, w or OK14) for x, w in items], a, R614, s)
f614("B", [("Is this <u>your</u> umbrella?", ""), ("<u>Our</u> school is big.", ""), ("I like <u>its</u> color.", ""), ("That is <u>she</u> bike.", "주격 she가 아니라 소유격 her를 써야 하므로"), ("These are <u>Tom's</u> pencils.", OKS)], 4)
f614("C", [("<u>Their</u> house is near the park.", ""), ("This is <u>him</u> jacket.", "목적격 him이 아니라 소유격 his를 써야 하므로"), ("<u>My brother's</u> room is small.", OKS), ("Where is <u>your</u> cap?", ""), ("The dog wags <u>its</u> tail.", "")], 2)
f614("D", [("<u>We</u> classroom is on the second floor.", "주격 We가 아니라 소유격 Our를 써야 하므로"), ("Is that <u>her</u> cat?", ""), ("I love <u>my</u> grandma.", ""), ("<u>Mina's</u> sister is tall.", OKS), ("Those are <u>their</u> bags.", "")], 1)
f614("E", [("This is <u>Jiho's</u> desk.", OKS), ("<u>His</u> dad is a pilot.", ""), ("<u>They</u> car is red.", "주격 They가 아니라 소유격 Their를 써야 하므로"), ("I know <u>her</u> name.", ""), ("Is this <u>our</u> table?", "")], 3)
f614("F", [("<u>Your</u> sister is kind.", ""), ("Tom lost <u>his</u> key.", ""), ("The bird is in <u>its</u> nest.", ""), ("<u>My friend's</u> dog is cute.", OKS), ("This is <u>I</u> notebook.", "주격 I가 아니라 소유격 my를 써야 하므로")], 5)

# 6-16 be동사 빈칸: 원문항 발문, 제시 문장 새로(과거형 was가 답이 되지 않게)
R616 = "현재형 be동사는 I am, he/she/it is, you/we/they are로 구별한다. now처럼 지금을 나타내는 말이 있으면 과거형 was는 쓸 수 없다."
S616 = "발문에 ‘현재형 be동사’가 붙었고, 제시 문장(___ very kind)이 원문항과 주어만 달랐다. 원문항 발문으로 되돌리고 제시 문장을 새로 썼다. 보기의 was가 답이 되지 않도록 필요한 곳에는 now를 넣었다."
def f616(t, p, items, a, s=S616):
    mk(6, 16, t, items, a, R616, s, st="R", p=p)
BE0 = "be는 동사원형이라 주어 뒤에 그대로 쓸 수 없으므로"
f616("B", "Tom _______ in his room now.", [("be", BE0), ("am", "am은 주어 I에만 쓰므로"), ("is", "3인칭 단수 주어 Tom에 맞는 현재형이므로"), ("was", "now가 있어 과거형 was를 쓸 수 없으므로"), ("are", "are는 you·복수 주어에 쓰므로")], 3)
f616("C", "I _______ hungry right now.", [("be", BE0), ("is", "is는 3인칭 단수 주어에 쓰므로"), ("was", "right now가 있어 과거형 was를 쓸 수 없으므로"), ("am", "주어 I에 맞는 현재형이므로"), ("are", "are는 you·복수 주어에 쓰므로")], 4)
f616("D", "She _______ at the bus stop now.", [("are", "are는 you·복수 주어에 쓰므로"), ("was", "now가 있어 과거형 was를 쓸 수 없으므로"), ("is", "3인칭 단수 주어 She에 맞는 현재형이므로"), ("be", BE0), ("am", "am은 주어 I에만 쓰므로")], 3)
f616("E", "We _______ on the playground now.", [("was", "주어 We에는 was를 쓰지 않으므로"), ("are", "주어 We에 맞는 현재형이므로"), ("is", "is는 3인칭 단수 주어에 쓰므로"), ("be", BE0), ("am", "am은 주어 I에만 쓰므로")], 2)
f616("F", "My parents _______ at work today.", [("be", BE0), ("was", "복수 주어 My parents에는 was를 쓰지 않으므로"), ("am", "am은 주어 I에만 쓰므로"), ("are", "복수 주어 My parents에 맞는 현재형이므로"), ("is", "is는 3인칭 단수 주어에 쓰므로")], 4, "발문에 ‘현재형 be동사’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 6-18 틀린 의문문: 짝 문장 없애기
R618 = "be동사 의문문은 be동사 + 주어 ~?로 쓰고, be동사는 주어에 맞춰 Am/Is/Are를 고른다."
S618 = "정답 문장과 짝을 이루는 옳은 문장이 함께 있어 대비 단서가 되었다. 짝 문장을 다른 문장으로 바꿨다."
OKQ = "주어에 맞는 be동사로 의문문을 바르게 만들었으므로"
def f618(t, items, a, s=S618):
    FIX.pop((6, 18, t), None)
    mk(6, 18, t, [(x, w or OKQ) for x, w in items], a, R618, s)
f618("C", [("Is the dog big?", ""), ("Are your parents at home?", ""), ("Are they students?", ""), ("Are you ready?", ""), ("Are Jane kind?", "3인칭 단수 주어 Jane에는 Is를 써야 하므로")], 5)
f618("D", [("Is the boys busy?", "복수 주어 the boys에는 Are를 써야 하므로"), ("Is it cold?", ""), ("Are we late?", ""), ("Am I next?", ""), ("Is she ready?", "")], 1)
f618("F", [("Is she home?", ""), ("Are these cookies for me?", ""), ("Are the cats outside?", ""), ("Is Tom tall?", ""), ("Am the books new?", "복수 주어 the books에는 Are를 써야 하므로")], 5)


# ---- 2차 감수(2026-10) 추가 ----
# 6-11 C·D·E: 원문항 보기를 이름만 바꿔 그대로 씀(her brother - he는 똑같음), C와 E는 틀린 짝도 같은 꼴
S611B = "보기가 원문항 보기를 이름만 바꾼 것이었고(her brother - he는 원문항 ②와 똑같다), 원문항과 다른 명사로 새로 썼다."
f611("C", [("Mr. Park - he", "Mr. Park: 남자 한 명이라 he로 바르게 받았으므로"), ("you and Jane - she", "you and Jane: 너를 포함한 여럿이라 you로 받아야 하므로"), ("the students - they", "the students: 여럿이라 they로 바르게 받았으므로"),
           ("my mother and I - we", "my mother and I: 나를 포함한 여럿이라 we로 바르게 받았으므로"), ("this bike - it", "this bike: 사물 하나라 it으로 바르게 받았으므로")], 2, S611B + " 틀린 짝은 그대로다.")
f611("D", [("the cats - they", "the cats: 여럿이라 they로 바르게 받았으므로"), ("Ms. Lee - she", "Ms. Lee: 여자 한 명이라 she로 바르게 받았으므로"), ("my friend and I - we", "my friend and I: 나를 포함한 여럿이라 we로 바르게 받았으므로"),
           ("my parents - it", "my parents: 두 사람이라 they로 받아야 하므로"), ("the boy - he", "the boy: 남자 한 명이라 he로 바르게 받았으므로")], 4, S611B + " 틀린 짝은 그대로다.")
f611("E", [("the teachers - they", "the teachers: 여럿이라 they로 바르게 받았으므로"), ("my cousin and I - we", "my cousin and I: 나를 포함한 여럿이라 we로 바르게 받았으므로"), ("this pencil - it", "this pencil: 사물 하나라 it으로 바르게 받았으므로"),
           ("Mrs. Brown - she", "Mrs. Brown: 여자 한 명이라 she로 바르게 받았으므로"), ("Jisu and her sister - she", "Jisu and her sister: 두 사람이라 they로 받아야 하므로")], 5, S611B + " 틀린 짝도 C(you and Jane - she)와 겹치지 않게 바꿨다.")
# 6-13 F: 정답 조합(Are - aren't)이 D와 같음 → Am I ~? 대화로
FIX.pop((6, 13, "F"), None)
mk(6, 13, "F", [("Are - am", "주어 I에는 Are가 아니라 Am을 쓰고, 대답의 주어 you에는 am을 쓸 수 없으므로"), ("Am - aren't", "주어 I에 Am, 부정 대답의 you에 aren't를 바르게 썼으므로"), ("Is - aren't", "주어 I에는 Is가 아니라 Am을 써야 하므로"),
    ("Am - isn't", "대답의 주어 you에는 isn't가 아니라 aren't를 써야 하므로"), ("Are - aren't", "주어 I에는 Are가 아니라 Am을 써야 하므로")], 2,
   "현재형 be동사는 주어가 I면 am, you·복수면 are, 3인칭 단수면 is를 쓴다. 의문문은 be동사 + 주어 ~?이고, I로 물으면 you로 답한다.",
   "발문에 ‘현재형 be동사를 사용하여’가 붙었고, 정답 조합(Are - aren't)이 D와 같았다. 원문항 발문으로 되돌리고 주어가 I인 대화로 바꿔 정답 조합이 다른 유형과 겹치지 않게 했다.", st="R", p="A: _______ I late for the class?\nB: No, you _______.")
# 6-15 E·F: 틀린 문장이 B·C와 거의 같음(Is they ~? / Are she your ~?)
R615 = "be동사는 주어에 맞춘다: I am, he/she/it·단수 주어 is, you/we/they·복수 주어 are. 의문문은 be동사 + 주어 ~?, 부정문은 be동사 + not이다."
OK15 = "주어에 맞는 be동사를 바르게 썼으므로"
def f615(t, items, a, s):
    mk(6, 15, t, [(x, w or OK15) for x, w in items], a, R615, s)
f615("E", [("He is my uncle.", ""), ("Is the weather warm?", ""), ("Are these your books?", ""), ("The boys are busy.", ""), ("Are your father a cook?", "단수 주어 your father에는 Is를 써야 하므로")], 5,
     "틀린 문장(Is they in the classroom?)이 B(Is they your friends?)와 거의 같았다. 틀린 문장을 다른 주어의 문장으로 바꿨다. 정답 위치는 그대로다.")
f615("F", [("Is Tom at home?", ""), ("The girls is in the garden.", "복수 주어 The girls에는 are를 써야 하므로"), ("We are not tired.", ""), ("These are my gloves.", ""), ("Is the cat under the chair?", "")], 2,
     "틀린 문장(Are she your teacher?)이 C(Are she your cousin?)와 거의 같았다. 틀린 문장을 다른 문장으로 바꿨다. 정답 위치는 그대로다.")
# 6-18 E: 틀린 문장(Are the dog hungry?)이 B(Are the puppy hungry?)와 거의 같음
f618("E", [("Is the cat small?", ""), ("Are the girls happy?", ""), ("Is Tom home?", ""), ("Are the books new?", ""), ("Are your uncle a farmer?", "단수 주어 your uncle에는 Is를 써야 하므로")], 5,
     "틀린 문장(Are the dog hungry?)이 B(Are the puppy hungry?)와 거의 같았다. 틀린 문장을 다른 문장으로 바꿨다. 정답 위치는 그대로다.")
# 6-19 F: 대화와 설명이 B와 거의 같음(Is the girls ~ / Is the boys ~), 발문에 ‘한국어로’가 빠짐
R619 = "be동사는 주어의 수와 인칭에 맞춘다. 주어가 복수(they, the girls, your parents, A and B)이면 are를 쓴다. 의문문에서도 마찬가지다."
mk(6, 19, "F", [("'parents'가 가족을 뜻하는 말이어서 is를 쓸 수 없기 때문이다.", "be동사는 낱말의 뜻이 아니라 주어의 수에 맞추므로"), ("뒤에 'at home'이라는 장소 표현이 오기 때문이다.", "be동사는 뒤에 오는 말이 아니라 주어에 맞추므로"),
    ("'your parents'는 두 사람을 가리키는 복수 주어이므로 이에 어울리는 be동사 'are'를 써야 한다.", "복수 주어에는 are를 쓰므로"), ("'your'가 2인칭이므로 주어와 관계없이 are를 써야 하기 때문이다.", "be동사는 your가 아니라 주어 your parents 전체의 수에 맞추므로"),
    ("대답에 'are'가 있으면 질문에도 반드시 같은 낱말을 써야 하기 때문이다.", "질문의 be동사는 대답이 아니라 주어에 맞추므로")], 3, R619,
   "대화(Is the boys in the music room?)와 설명이 B(Is the girls in the gym?)와 거의 같았고, 발문에 ‘한국어로’가 빠져 있었다. 원문항 발문으로 되돌리고 대화와 설명을 새로 썼다.", st="R", p="A: <u>Is</u> your parents at home?\nB: Yes, they are.", okdup=True, okx=True)
# 6-20 C: 정답 설명이 B와 같음((A)의 These ~ are)
FIX.pop((6, 20, "C"), None)
mk(6, 20, "C", [("(B)의 books는 하나이므로 book으로 고쳐야 한다.", "These are와 함께 쓰여 여러 권을 가리키므로 복수형 books가 맞으므로"), ("(A)의 These는 멀리 있는 여러 개를 가리킨다.", "These는 가까이 있는 여러 개를 가리키므로"), ("(D)의 notebook은 복수 명사이므로 are와 함께 써야 한다.", "notebook은 단수 명사라 is와 함께 쓰므로"),
    ("These와 This는 수와 관계없이 바꾸어 쓸 수 있다.", "These는 여러 개, This는 한 개를 가리켜 바꿔 쓸 수 없으므로"), ("(C)의 This는 가까이 있는 한 개를 가리키므로 is와 함께 쓴다.", "This는 가까이 있는 한 개를 가리키고 단수 be동사 is와 쓰므로")], 5,
   "this/that은 한 개, these/those는 여러 개를 가리킨다. this·these는 가까이 있는 것, that·those는 멀리 있는 것이다. be동사와 뒤의 명사도 수를 맞춘다.",
   "발문이 원문항과 달랐고, 정답 설명((A)의 These는 가까이 있는 여러 개를 가리키므로 are와 함께 쓴다)이 B와 같았다. 원문항 발문으로 되돌리고 정답 설명을 (C)에 대한 것으로 바꿨다. 지문은 그대로다.", st="R")
