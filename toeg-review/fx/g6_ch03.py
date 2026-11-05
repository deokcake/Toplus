# 6급 CH3 be동사 과거형 (21~30) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
R_WAS = "be동사 과거형은 주어가 I·3인칭 단수면 was, you·we·they·복수 주어(A and B 포함)면 were를 쓴다. 부정은 wasn't/weren't, 의문문은 Was/Were + 주어 ~?로 쓴다."

# 원문항 발문으로만 되돌리는 문항
for t in "BCDEF": F(6, 22, t, st="R", s="발문이 ‘지시 대상·소유·시간 정보를 빠짐없이 나타낸 문장’으로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDEF": F(6, 24, t, st="R", s="발문에 ‘과거형 be동사를 사용하여 긍정 의문문과 그 대답’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BDEF": F(6, 27, t, st="R", s="발문에 ‘과거형 be동사를 사용하여’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
F(6, 26, "E", st="R", s="발문에 ‘과거의 상황을 나타내도록’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 6-21 be동사 과거형 고르기: 원문항처럼 문장 없이 형태만 제시
S621 = "원문항은 문장 없이 be동사 형태 중 과거형을 고르는 형식인데, 변형은 문장 빈칸에 주어에 맞는 과거형을 고르는 형식으로 바뀌었다. 원문항처럼 문장 없이 형태만 제시하고, 부정 축약형·의문문 첫머리 형태 등으로 유형마다 보기를 달리했다."
PRS = lambda w: f"{w}: 현재형이므로"
def f621(t, items, a, s=S621):
    mk(6, 21, t, items, a, R_WAS, s, st="R", p="")
f621("B", [("are", PRS("are")), ("be", "be: 동사원형이므로"), ("is", PRS("is")), ("were", "were: are의 과거형이므로"), ("am", PRS("am"))], 4)
f621("C", [("isn't", "isn't: is not을 줄인 현재형이므로"), ("wasn't", "wasn't: was not을 줄인 과거형이므로"), ("aren't", "aren't: are not을 줄인 현재형이므로"), ("am not", "am not: 현재형 부정이므로"), ("is not", "is not: 현재형 부정이므로")], 2)
f621("D", [("weren't", "weren't: were not을 줄인 과거형이므로"), ("aren't", "aren't: are not을 줄인 현재형이므로"), ("isn't", "isn't: is not을 줄인 현재형이므로"), ("am not", "am not: 현재형 부정이므로"), ("is not", "is not: 현재형 부정이므로")], 1)
f621("E", [("are not", "are not: 현재형 부정이므로"), ("is not", "is not: 현재형 부정이므로"), ("am not", "am not: 현재형 부정이므로"), ("do not", "do not: be동사가 아니라 일반동사의 부정에 쓰므로"), ("was not", "was not: was의 부정으로 과거형이므로")], 5)
f621("F", [("Are", "Are: 의문문 첫머리에 오는 현재형이므로"), ("Is", "Is: 의문문 첫머리에 오는 현재형이므로"), ("Were", "Were: 의문문 첫머리에 오는 과거형이므로"), ("Am", "Am: 의문문 첫머리에 오는 현재형이므로"), ("Do", "Do: be동사가 아니라 일반동사 의문문에 쓰므로")], 3)

# 6-23 틀린 부정문: 짝 문장 없이 유형마다 새로
S623 = "정답 문장과 같은 문장의 옳은 형태가 함께 있어 대비 단서가 되었고 오답 네 개가 유형마다 같았다. 짝 문장 없이 유형마다 새로 썼다."
OK23 = "주어에 맞는 wasn't/weren't를 바르게 썼으므로"
def f623(t, items, a, s=S623):
    mk(6, 23, t, [(x, w or OK23) for x, w in items], a, R_WAS, s)
f623("B", [("You weren't at the library.", ""), ("The soup wasn't hot.", ""), ("I wasn't tired.", ""), ("They wasn't busy.", "복수 주어 They에는 weren't를 써야 하므로"), ("The door wasn't open.", "")], 4,
     S623 + " 원문항 정답을 바르게 고친 문장(It wasn't heavy.)과 D의 틀린 문장의 짝(We weren't at home.)도 다른 문장으로 바꿨다.")
f623("D", [("My shoes weren't dirty.", ""), ("He wasn't at the party.", ""), ("We wasn't at home.", "주어 We에는 weren't를 써야 하므로"), ("The test wasn't easy.", ""), ("You weren't late.", "")], 3)
f623("E", [("The kids weren't noisy.", ""), ("Jane weren't a student.", "3인칭 단수 주어 Jane에는 wasn't를 써야 하므로"), ("My dad wasn't angry.", ""), ("The stores weren't open.", ""), ("I wasn't hungry.", "")], 2)
f623("F", [("The birds weren't in the cage.", ""), ("The milk wasn't cold.", ""), ("You weren't alone.", ""), ("Her friends weren't there.", ""), ("I weren't at the bus stop.", "주어 I에는 wasn't를 써야 하므로")], 5)

# 6-25 대답 고르기: 원문항처럼 같은 주어의 형태 오류 오답
R625 = "Was/Were 의문문에는 Yes, 주어 + was/were. / No, 주어 + wasn't/weren't.로 답한다. 대답의 주어는 질문의 주어를 대명사로 받고(the cookies → they, Jane → she), 시제도 과거로 맞춘다."
S625 = "원문항 오답은 같은 주어(they/it)의 형태 오류인데, 변형 오답은 질문과 맞지 않는 대명사라 바로 지워졌고 B와 같은 오답이 반복되었다. 원문항처럼 질문 주어에 맞는 대명사의 형태 오류로 오답을 유형마다 새로 썼다."
def f625(t, q, items, a, s=S625, **kw):
    mk(6, 25, t, items, a, R625, s, p=q, **kw)
f625("B", "Were Tom and Ben busy?", [("No, they weren't.", "Were 질문에 복수 대명사 they와 weren't로 바르게 답했으므로"), ("Yes, they was.", "복수 주어 they에는 were를 써야 하므로"), ("No, they aren't.", "과거 질문에 현재형 aren't로 답했으므로"),
     ("Yes, we were.", "Tom and Ben은 we가 아니라 they로 받아야 하므로"), ("No, they wasn't.", "복수 주어 they에는 weren't를 써야 하므로")], 1)
f625("C", "Were you tired?", [("Yes, I were.", "주어 I에는 was를 써야 하므로"), ("Yes, I am.", "과거 질문에 현재형 am으로 답했으므로"), ("Yes, I did.", "be동사 질문에 did로 답했으므로"), ("Yes, I was.", "you에 대한 질문에 I와 was로 바르게 답했으므로"), ("No, I'm not.", "과거 질문에 현재형 I'm not으로 답했으므로")], 4,
     "발문이 ‘한 사람에게 묻는 질문에 그 사람이 직접 답한’이라고 정답의 주어를 알려 주었고 오답이 B와 같았다. 원문항 발문으로 되돌리고, 조건 없이도 답이 하나로 정해지도록 오답을 모두 주어 I의 형태 오류로 새로 썼다.", st="R")
f625("D", "Was the soup hot?", [("No, it wasn't.", "the soup를 it으로 받아 wasn't로 바르게 답했으므로"), ("No, it doesn't.", "be동사 과거 질문에 doesn't로 답했으므로"), ("No, it isn't.", "과거 질문에 현재형 isn't로 답했으므로"),
     ("No, we weren't.", "the soup는 we가 아니라 it으로 받아야 하므로"), ("No, it weren't.", "단수 주어 it에는 wasn't를 써야 하므로")], 1,
     "원문항은 짧은 대답 문장 다섯 개 중 고르는 형식인데 선택지 형식이 원문항과 다르게 판정되었다. 원문항처럼 같은 주어의 짧은 대답 문장(No, it …)으로 모두 맞추고, 다른 유형과 겹치지 않게 오답을 새로 썼다.")
f625("E", "Was the cake good?", [("Yes, it is.", "과거 질문에 현재형 is로 답했으므로"), ("Yes, it were.", "단수 주어 it에는 was를 써야 하므로"), ("Yes, it was.", "the cake를 it으로 받아 was로 바르게 답했으므로"), ("Yes, it does.", "be동사 과거 질문에 does로 답했으므로"), ("Yes, they were.", "the cake는 they가 아니라 it으로 받아야 하므로")], 3)
f625("F", "Was Jane at home?", [("Yes, she were.", "단수 주어 she에는 was를 써야 하므로"), ("No, she isn't.", "과거 질문에 현재형 isn't로 답했으므로"), ("Yes, she did.", "be동사 질문에 did로 답했으므로"), ("No, she wasn't.", "Jane을 she로 받아 wasn't로 바르게 답했으므로"), ("Yes, he was.", "Jane은 he가 아니라 she로 받아야 하므로")], 4)

# 6-26 빈칸 be동사: 원문항 발문, 제시 문장 새로(과거 시간 표현)
R626 = "yesterday, last night, ago처럼 과거를 나타내는 말이 있으면 be동사 과거형을 쓰고, 주어에 맞춰 was/were를 고른다."
S626 = "발문에 ‘과거의 상황을 나타내도록’이 붙었고, 제시 문장(___ at the park yesterday)이 원문항과 주어만 달랐다. 원문항 발문으로 되돌리고 과거 시간 표현이 든 제시 문장을 새로 썼다."
def f626(t, p, items, a, s=S626):
    mk(6, 26, t, items, a, R626, s, st="R", p=p)
NOW = lambda w: f"{w}: 현재형이라 과거를 나타내는 말과 맞지 않으므로"
f626("B", "The boys ________ very hungry after the game last night.", [("was", "was: 복수 주어 The boys에는 were를 쓰므로"), ("is", NOW("is")), ("were", "were: 복수 주어의 과거형이므로"), ("are", NOW("are")), ("am", "am: 주어 I에만 쓰는 현재형이므로")], 3)
f626("C", "We ________ in the same class last year.", [("were", "were: 주어 We의 과거형이므로"), ("am", "am: 주어 I에만 쓰는 현재형이므로"), ("is", NOW("is")), ("are", NOW("are")), ("was", "was: 주어 We에는 were를 쓰므로")], 1)
f626("D", "She ________ sick in bed two days ago.", [("am", "am: 주어 I에만 쓰는 현재형이므로"), ("are", NOW("are")), ("is", NOW("is")), ("were", "were: 3인칭 단수 주어 She에는 was를 쓰므로"), ("was", "was: 3인칭 단수 주어의 과거형이므로")], 5)
f626("F", "Tom ________ late for school yesterday morning.", [("are", NOW("are")), ("was", "was: 3인칭 단수 주어의 과거형이므로"), ("am", "am: 주어 I에만 쓰는 현재형이므로"), ("were", "were: 3인칭 단수 주어 Tom에는 was를 쓰므로"), ("is", NOW("is"))], 2)

# 6-27 C: 정답 조합을 원문항(Was - wasn't)과 다르게
F(6, 27, "C", st="R", p="A: ________ Tom busy yesterday?\nB: Yes, he ________. He had a lot of homework.", c=["Were - were", "Was - wasn't", "Were - wasn't", "Was - weren't", "Was - was"], a=5, r=R_WAS,
  n=["3인칭 단수 주어 Tom에는 Was를 쓰므로 오답이다.", "Yes로 답했으므로 wasn't가 아니라 was를 써야 하므로 오답이다.", "Tom에는 Was를 쓰고, Yes로 답했으므로 was를 써야 하므로 오답이다.", "he에는 weren't를 쓰지 않고, Yes로 답했으므로 was를 써야 하므로 오답이다.", "Tom에 Was, Yes 대답에 he was를 바르게 썼으므로 정답이다."],
  s="정답 조합(Was - wasn't)이 원문항과 같았고 발문에 ‘과거형 be동사를 사용하여’가 붙었다. 원문항 발문으로 되돌리고 Yes 대답으로 바꿔 정답 조합이 Was - was가 되게 했다. 정답 위치 ⑤.")

# 6-28 의문문 배열: 원문항 발문, 주어진 어구만으로 만든 어순 오류
R628 = "be동사 과거 의문문은 Was/Were + 주어 + 보어·장소 + 시간 표현?의 어순으로 쓴다. 평서문 어순에 물음표만 붙이거나 보어·장소를 주어 앞에 두지 않는다."
S628 = "발문이 ‘be동사로 시작하는 기본형 의문문’이라고 정답 형식을 알려 주었고, 마침표로 끝나거나 주어진 적 없는 단어가 든 오답은 형식만으로 지워졌다. 원문항 발문으로 되돌리고 원문항처럼 주어진 어구만 쓴 어순 오류로 오답을 바꿨다."
DECL = "평서문 어순에 물음표만 붙였으므로"; OK28 = "Was/Were + 주어 + 보어·장소의 어순으로 바르게 배열했으므로"; FRONT = "보어·장소 표현이 주어 앞에 와서 어순이 맞지 않으므로"; TIME = "시간 표현으로 시작한 평서문 어순에 물음표만 붙였으므로"
def f628(t, items, a, s=S628):
    mk(6, 28, t, items, a, R628, s, st="R")
f628("B", [("Tom was at school?", DECL), ("Was Tom at school?", OK28), ("Was at school Tom?", FRONT), ("At school was Tom?", FRONT), ("At school Tom was?", "장소 표현으로 시작하고 be동사가 문장 끝에 와서 어순이 맞지 않으므로")], 2)
f628("C", [("Jane was at the museum yesterday?", DECL), ("Was at the museum Jane yesterday?", FRONT), ("Was Jane at the museum yesterday?", OK28), ("Yesterday Jane was at the museum?", TIME), ("At the museum was Jane yesterday?", FRONT)], 3)
f628("D", [("Were tired the boys?", FRONT), ("The boys were tired?", DECL), ("Tired were the boys?", FRONT), ("Were the boys tired?", OK28), ("Tired the boys were?", "보어로 시작하고 be동사가 문장 끝에 와서 어순이 맞지 않으므로")], 4)
f628("E", [("She was at home yesterday?", DECL), ("Was at home she yesterday?", FRONT), ("Yesterday she was at home?", TIME), ("At home was she yesterday?", FRONT), ("Was she at home yesterday?", OK28)], 5)
f628("F", [("Were the students in the library yesterday?", OK28), ("Were in the library the students yesterday?", FRONT), ("The students were in the library yesterday?", DECL), ("In the library were the students yesterday?", FRONT), ("Yesterday the students were in the library?", TIME)], 1)

# 6-29 지문 밑줄: 원문항처럼 밑줄 번호만 제시(주어 표시 삭제)
R629 = "지문의 각 문장에서 주어를 먼저 찾고, 주어가 I·3인칭 단수면 was, 복수(A and B 포함)면 were인지 확인한다."
S629 = "선택지마다 ‘(주어: My friends)’처럼 각 be동사의 주어를 알려 주어 수 일치 판단이 쉬워졌고, 선택지 형식이 원문항(밑줄 번호만)과 달랐다. 주어 표시를 지우고 원문항처럼 밑줄 번호만 제시했다."
NUMS = ["①", "②", "③", "④", "⑤"]
def f629(t, why, a, s=S629, **kw):
    F(6, 29, t, c=NUMS, a=a, r=R629, n=[w + (" 정답이다." if i + 1 == a else " 오답이다.") for i, w in enumerate(why)], okdup=True, s=s + ipos(a), **kw)
f629("B", ["주어 My friends는 복수라 was가 아니라 were를 써야 하므로", "주어 The weather는 단수라 was를 바르게 썼으므로", "주어 Our teachers는 복수라 were를 바르게 썼으므로", "주어 I에 was를 바르게 썼으므로", "주어 We에 were를 바르게 썼으므로"], 1)
f629("C", ["주어 The paintings는 복수라 were를 바르게 썼으므로", "주어 The old camera는 단수라 were가 아니라 was를 써야 하므로", "주어 My parents는 복수라 were를 바르게 썼으므로", "주어 I에 was를 바르게 썼으므로", "주어 It에 was를 바르게 썼으므로"], 2)
f629("D", ["주어 The tents는 복수라 were를 바르게 썼으므로", "주어 The air는 단수라 was를 바르게 썼으므로", "주어 My cousins는 복수라 was가 아니라 were를 써야 하므로", "주어 Our dog는 단수라 was를 바르게 썼으므로", "주어 We에 were를 바르게 썼으므로"], 3,
     S629 + " 틀린 문장의 주어(My brother and I)가 원문항의 틀린 문장(My little brother and I ③was)과 같아 다른 주어로 바꿨다.",
     p="Last night, we camped by a lake. The tents ①<u>were</u> ready. The air ②<u>was</u> cold. My cousins ③<u>was</u> inside a tent. Our dog ④<u>was</u> quiet. We ⑤<u>were</u> safe.")
f629("E", ["주어 Her friends는 복수라 were를 바르게 썼으므로", "주어 The gifts는 복수라 were를 바르게 썼으므로", "주어 Mina는 단수라 was를 바르게 썼으므로", "주어 The cake는 단수라 were가 아니라 was를 써야 하므로", "주어 Everyone은 단수로 받아 was를 바르게 썼으므로"], 4)
f629("F", ["주어 The lions는 복수라 were를 바르게 썼으므로", "주어 A monkey는 단수라 was를 바르게 썼으므로", "주어 My cousins는 복수라 were를 바르게 썼으므로", "주어 I에 was를 바르게 썼으므로", "주어 The weather는 단수라 were가 아니라 was를 써야 하므로"], 5)

# 6-30 옳은 문장 개수와 이유: <보기>와 설명을 유형마다 새로
R630 = "(가)~(다)의 주어를 각각 찾아 was/were를 판정한 뒤, 옳은 문장의 개수·문장·이유가 모두 맞는 설명을 고른다. 한 명·한 개(I 포함)는 was, you와 둘 이상(A and B, 복수 명사, 복수 대명사)은 were이다."
S630 = "<보기> 세 문장이 원문항과 명사만 다르고(box → bag/chair/desk/book) 설명 다섯 개도 원문항·유형마다 같아, 선택지 순서만 바뀐 문항이었다. <보기> 문장과 설명을 유형마다 새로 쓰고, 옳은 문장의 개수도 유형마다 달리했다."
def f630(t, lines, judge, items, a, s=S630):
    F(6, 30, t, p="<보기>\n" + "\n".join(lines), c=[x for x, _ in items], a=a, r=R630, pre=["문장별 판정: " + j for j in judge], k=items[a-1][0].split(".")[0] + "이다.",
      n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + ipos(a))
f630("B", ["(가) My brother was sick.", "(나) My brothers was sick.", "(다) My brother and I were sick."], ["(가) O. 한 사람인 주어에 was를 썼다.", "(나) X. 복수 주어 My brothers에는 were를 써야 한다.", "(다) O. 둘 이상인 주어에 were를 썼다."],
     [("2개 - (가), (다)가 맞음. 한 사람인 주어에는 'was', 'A and B'처럼 둘 이상인 주어에는 'were'를 써야 함.", "개수·문장·이유가 모두 맞으므로"), ("1개 - (가)만 맞음. 'I'가 들어간 주어에는 항상 'was'를 써야 함.", "My brother and I는 둘 이상이라 were가 맞으므로"),
      ("2개 - (가), (나)가 맞음. 주어가 사람이면 수와 관계없이 'was'를 씀.", "복수 주어 My brothers에는 were를 써야 하므로"), ("1개 - (다)만 맞음. 가족을 나타내는 주어에는 'were'만 씀.", "한 사람인 My brother에는 was가 맞으므로"),
      ("3개 - 모두 맞음. 과거형은 주어의 수를 따지지 않음.", "과거형도 주어의 수에 따라 was/were를 구별하므로")], 1)
f630("C", ["(가) The dogs were hungry.", "(나) The dog were hungry.", "(다) They was hungry."], ["(가) O. 복수 주어에 were를 썼다.", "(나) X. 단수 주어 The dog에는 was를 써야 한다.", "(다) X. 복수 대명사 They에는 were를 써야 한다."],
     [("2개 - (가), (다)가 맞음. 대명사 주어 뒤에는 'was'를 써도 됨.", "복수 대명사 They에는 were를 써야 하므로"), ("2개 - (가), (나)가 맞음. 동물 주어에는 단수·복수 모두 'were'를 씀.", "한 마리인 The dog에는 was를 써야 하므로"),
      ("1개 - (나)만 맞음. 'dog'처럼 한 마리일 때 'were'를 씀.", "한 마리에는 was를 쓰고 (가)도 옳은 문장이므로"), ("1개 - (가)만 맞음. 복수 주어 The dogs와 They에는 'were', 단수 The dog에는 'was'를 써야 함.", "개수·문장·이유가 모두 맞으므로"),
      ("0개 - 모두 틀림. 동물 주어에는 be동사 과거형을 쓰지 않음.", "동물 주어에도 be동사 과거형을 쓰고 (가)는 옳은 문장이므로")], 4)
f630("D", ["(가) You was late.", "(나) You were late.", "(다) Mina and you were late."], ["(가) X. you에는 한 사람이어도 were를 쓴다.", "(나) O. you에 were를 썼다.", "(다) O. 둘 이상인 주어에 were를 썼다."],
     [("1개 - (나)만 맞음. 'Mina and you'는 한 사람처럼 보아 'was'를 써야 함.", "Mina and you는 둘 이상이라 were가 맞으므로"), ("2개 - (가), (나)가 맞음. 'you'는 한 사람일 때 'was', 여러 사람일 때 'were'를 씀.", "you에는 한 사람이어도 were를 쓰므로"),
      ("2개 - (나), (다)가 맞음. 'you'는 한 사람이어도 'were'를 쓰고, 'Mina and you'처럼 둘 이상인 주어에도 'were'를 씀.", "개수·문장·이유가 모두 맞으므로"), ("3개 - 모두 맞음. 'you'가 들어간 주어에는 'was'와 'were'를 모두 쓸 수 있음.", "you에는 was를 쓰지 않으므로"),
      ("1개 - (가)만 맞음. 'you'는 2인칭 단수이므로 'was'를 씀.", "you에는 한 사람이어도 were를 쓰므로")], 3)
f630("E", ["(가) Tom was tired.", "(나) Tom and Jerry were tired.", "(다) We were tired."], ["(가) O. 한 사람인 주어에 was를 썼다.", "(나) O. 둘 이상인 주어에 were를 썼다.", "(다) O. 주어 We에 were를 썼다."],
     [("2개 - (가), (나)가 맞음. 'We'에는 'was'를 써야 함.", "주어 We에는 were가 맞으므로"), ("3개 - 모두 맞음. 단수 주어 Tom에는 'was', 복수 주어 Tom and Jerry와 We에는 'were'를 썼음.", "개수·문장·이유가 모두 맞으므로"),
      ("1개 - (가)만 맞음. 사람 이름이 들어간 주어에는 항상 'was'를 씀.", "Tom and Jerry는 둘이라 were가 맞으므로"), ("2개 - (나), (다)가 맞음. 'Tom'은 3인칭이므로 'were'를 써야 함.", "3인칭 단수 Tom에는 was가 맞으므로"),
      ("1개 - (다)만 맞음. 1인칭 주어에만 'were'를 쓸 수 있음.", "복수 주어에는 인칭과 관계없이 were를 쓰므로")], 2)
f630("F", ["(가) It was sunny.", "(나) The children was happy.", "(다) The children were happy."], ["(가) O. 날씨를 나타내는 It에 was를 썼다.", "(나) X. children은 child의 복수형이라 were를 써야 한다.", "(다) O. 복수 주어에 were를 썼다."],
     [("2개 - (가), (나)가 맞음. 'children'은 -s가 없으므로 단수로 보아 'was'를 씀.", "children은 -s가 없어도 child의 복수형이므로"), ("1개 - (다)만 맞음. 날씨를 나타내는 'It'에는 'were'를 써야 함.", "날씨의 It은 단수라 was가 맞으므로"),
      ("3개 - 모두 맞음. 'children'에는 'was'와 'were'를 모두 쓸 수 있음.", "복수 주어 children에는 were만 쓰므로"), ("1개 - (나)만 맞음. 'children'은 한 무리를 가리키므로 'was'를 쓰고, 'It'에는 'were'를 씀.", "children에는 were를, It에는 was를 쓰므로"),
      ("2개 - (가), (다)가 맞음. 날씨의 'It'은 단수라 'was', 'children'은 'child'의 복수형이라 'were'를 씀.", "개수·문장·이유가 모두 맞으므로")], 5)


# ---- 2차 감수(2026-10) 추가 ----
# 6-22 E: 원문항 발문으로 되돌리면 ①(I was tired.)도 틀린 문장이 아니게 됨 → 분명히 틀린 문장으로
FIX.pop((6, 22, "E"), None)
mk(6, 22, "E", [("I am tired yesterday.", "어제의 일에 현재형 am을 쓸 수 없으므로"), ("I were tired yesterday.", "주어 I에는 were가 아니라 was를 써야 하므로"), ("I was tired yesterday.", "주어 I에 was, ‘어제’에 yesterday를 바르게 썼으므로"),
    ("I is tired yesterday.", "주어 I에 is를 쓸 수 없고 과거의 일도 아니게 되므로"), ("I was tired tomorrow.", "tomorrow는 ‘내일’이라 ‘어제’와 맞지 않으므로")], 3, R_WAS,
   "발문이 ‘지시 대상·소유·시간 정보를 빠짐없이 나타낸 문장’으로 바뀌었다. 원문항 발문으로 되돌리면 ①(I was tired.)은 ‘어제’만 빠진 옳은 문장이라 정답과 헷갈릴 수 있어, 분명히 틀린 문장으로 바꿨다. 정답은 그대로다.", st="R")
# 6-27 E·F: 정답 조합(Were - weren't)이 B와 같음 → 서로 다른 조합으로
for _t in "EF": FIX.pop((6, 27, _t), None)
mk(6, 27, "E", [("Were - were", "복수 주어 the boys에 Were, Yes 대답의 they에 were를 바르게 썼으므로"), ("Were - wasn't", "Yes로 답했고 they에는 wasn't를 쓸 수 없으므로"), ("Was - weren't", "복수 주어 the boys에는 Was를 쓸 수 없으므로"),
    ("Were - weren't", "Yes로 답했으므로 weren't를 쓸 수 없으므로"), ("Was - was", "복수 주어 the boys와 they에는 was를 쓸 수 없으므로")], 1, R_WAS,
   "발문에 ‘과거형 be동사를 사용하여’가 붙었고, 정답 조합(Were - weren't)과 대화의 짜임이 B와 같았다. 원문항 발문으로 되돌리고 Yes 대답으로 바꿔 정답 조합이 Were - were가 되게 했다. 보기는 그대로다.",
   st="R", p="A: ________ the boys at school yesterday?\nB: Yes, they ________. They were in the gym.")
mk(6, 27, "F", [("Were - wasn't", "Yes로 답했으므로 wasn't를 쓸 수 없으므로"), ("Was - was", "주어 you에는 Was를 쓸 수 없으므로"), ("Were - weren't", "Yes로 답했고 주어 I에는 weren't를 쓸 수 없으므로"),
    ("Were - was", "주어 you에 Were, Yes 대답의 I에 was를 바르게 썼으므로"), ("Was - weren't", "주어 you에는 Was를 쓸 수 없고 Yes로 답했으므로")], 4, R_WAS,
   "발문에 ‘과거형 be동사를 사용하여’가 붙었고, 정답 조합(Were - weren't)이 B와 같았다. 원문항 발문으로 되돌리고 대화를 바꿔 정답 조합이 Were - was가 되게 했다.",
   st="R", p="A: ________ you at the concert last night?\nB: Yes, I ________. It was great.")
