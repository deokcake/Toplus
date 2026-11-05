# 4급 CH5 미래시제 will / be going to (41~50) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]

# 4-41 not의 위치: 원문항 형식(우리말 + 문장 속 번호 위치)
ST441 = "다음 문장에서 not이 들어갈 위치로 알맞은 것을 고르시오."
R441 = "will의 부정은 will not + 동사원형, be going to의 부정은 be동사 뒤에 not을 넣어 be not going to + 동사원형으로 쓴다."
S441 = "원문항은 문장 속 번호 위치에 not을 넣는 위치 선택형인데, 변형은 빈칸에 들어갈 부정 형태를 고르는 형식으로 바뀌었다. 원문항 발문과 형식(우리말 + 문장 속 ①~⑤ 위치)으로 되돌리고 유형마다 정답 위치를 달리했다."
def f441(t, ko, sent, words, a, why, s=S441):
    mk(4, 41, t, [(w, why if i + 1 == a else "not이 들어갈 자리가 아니므로") for i, w in enumerate(words)], a, R441, s, st=ST441, p=f"{ko}\n{sent}", okdup=True)
f441("B", "그녀는 이번 주말에 이모를 방문하지 않을 것이다.", "She ① is ② going ③ to ④ visit ⑤ her aunt this weekend.", ["is", "going", "to", "visit", "her"], 2, "be동사 is 뒤에 not을 넣어 is not going to가 되므로")
f441("C", "우리는 오늘 밤 저녁을 요리하지 않을 것이다.", "① We ② will ③ cook ④ dinner ⑤ tonight.", ["We", "will", "cook", "dinner", "tonight"], 3, "will 뒤, 동사원형 cook 앞에 not을 넣어 will not cook이 되므로")
f441("D", "그들은 오늘 밤 집에 없을 것이다.", "They will ① be ② at ③ home ④ tonight ⑤.", ["be", "at", "home", "tonight", "."], 1, "will 뒤, 동사원형 be 앞에 not을 넣어 will not be가 되므로")
f441("E", "내 여동생과 나는 쇼핑하러 가지 않을 것이다.", "My ① sister ② and I ③ are ④ going ⑤ to go shopping.", ["sister", "and", "are", "going", "to"], 4, "be동사 are 뒤에 not을 넣어 are not going to가 되므로")
f441("F", "이번 여름에 우리 가족은 캠핑을 가지 않을 것이다.", "This ① summer, ② our ③ family ④ will ⑤ go camping.", ["summer", "our", "family", "will", "go"], 5, "will 뒤, 동사원형 go 앞에 not을 넣어 will not go가 되므로")

# 4-42 be going to 부정문: 원문항 발문, 옳은 축약형 대신 틀린 형태의 오답
S442 = "발문에 ‘be going to 문장을’과 ‘축약형을 쓰지 않을 것’ 조건이 붙었고, 옳은 축약형(isn't going to)을 오답에 넣어 조건으로 걸러야 했다. 원문항 발문으로 되돌리고 그 오답을 틀린 형태로 바꿨다."
R442 = "be going to의 부정문은 be동사 바로 뒤에 not을 넣어 be not going to + 동사원형으로 쓴다. do/does로 부정하거나 to를 빼면 틀린다."
NOTBE = "not은 be동사 뒤에 와야 하므로"
def f442(t, p, items, a, s=S442):
    mk(4, 42, t, items, a, R442, s, st="R", p=p)
f442("B", "Tom is going to visit his uncle.", [("Tom is not going to visit his uncle.", "be동사 is 뒤에 not을 바르게 넣었으므로"), ("Tom is not go to visit his uncle.", "going을 go로 바꿔 틀렸으므로"), ("Tom not is going to visit his uncle.", NOTBE),
     ("Tom does not going to visit his uncle.", "be going to는 does로 부정하지 않으므로"), ("Tom is going to visit his uncle.", "부정문으로 바꾸지 않았으므로")], 1)
f442("C", "Mina is going to join the club.", [("Mina is not go to join the club.", "going을 go로 바꿔 틀렸으므로"), ("Mina does not going to join the club.", "be going to는 does로 부정하지 않으므로"), ("Mina not is going to join the club.", NOTBE),
     ("Mina is going to join the club.", "부정문으로 바꾸지 않았으므로"), ("Mina is not going to join the club.", "be동사 is 뒤에 not을 바르게 넣었으므로")], 5,
     "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘Mina is going to join the club.’으로 바꾸고 원문항 발문으로 되돌렸다.")
f442("D", "They are going to play soccer.", [("They do not going to play soccer.", "be going to는 do로 부정하지 않으므로"), ("They are going to play soccer.", "부정문으로 바꾸지 않았으므로"), ("They are not going to play soccer.", "be동사 are 뒤에 not을 바르게 넣었으므로"),
     ("They are not go to play soccer.", "going을 go로 바꿔 틀렸으므로"), ("They are not going play soccer.", "going 뒤의 to가 빠졌으므로")], 3)
f442("E", "I am going to buy a new bag.", [("I am not go to buy a new bag.", "going을 go로 바꿔 틀렸으므로"), ("I am going to buy a new bag.", "부정문으로 바꾸지 않았으므로"), ("I am not going to buy a new bag.", "be동사 am 뒤에 not을 바르게 넣었으므로"),
     ("I do not going to buy a new bag.", "be going to는 do로 부정하지 않으므로"), ("I not am going to buy a new bag.", NOTBE)], 3, S442 + " 없는 형태(amn't)도 틀린 어순으로 바꿨다.")
f442("F", "We are going to leave early.", [("We not are going to leave early.", NOTBE), ("We are not go to leave early.", "going을 go로 바꿔 틀렸으므로"), ("We are not going to leave early.", "be동사 are 뒤에 not을 바르게 넣었으므로"),
     ("We are going to leave early.", "부정문으로 바꾸지 않았으므로"), ("We do not going to leave early.", "be going to는 do로 부정하지 않으므로")], 3)

# 4-43 미래의 be going to가 아닌 것: 유형마다 문장을 새로
R443 = "be going to + 동사원형은 미래의 계획·예측을 나타내고, be going to + 장소(the park, school)는 go의 진행형으로 ‘지금 ~에 가고 있다’는 뜻이다."
S443 = "be going to 오답 네 문장이 B와 똑같았다. 유형마다 문장을 새로 썼다."
def FUT(v): return f"be going to + 동사원형({v})으로 미래를 나타내므로"
def MOV(pl): return f"going to 뒤에 장소({pl})가 와서 ‘지금 가고 있다’는 현재진행의 뜻이므로"
def f443(t, items, a, s=S443):
    mk(4, 43, t, items, a, R443, s, st="R")
f443("B", [("I am going to clean my room.", FUT("clean")), ("My dad is going to the bank now.", MOV("the bank")), ("Mina is going to learn French.", FUT("learn")), ("We are going to have a party.", FUT("have")), ("They are going to take a taxi.", FUT("take"))], 2,
     "정답(He is going to the park now.)이 원문항과 똑같았다. 문장을 모두 새로 썼다.")
f443("C", [("He is going to fix the bike.", FUT("fix")), ("The kids are going to sing a song.", FUT("sing")), ("I am going to wear a jacket.", FUT("wear")), ("We are going to meet at six.", FUT("meet")), ("She is going to school now.", MOV("school"))], 5)
f443("D", [("Jane is going to bake cookies.", FUT("bake")), ("It is going to snow tonight.", FUT("snow")), ("They are going to the museum now.", MOV("the museum")), ("You are going to love this movie.", FUT("love")), ("He is going to be a doctor.", FUT("be"))], 3,
     "발문이 ‘to 뒤에 장소 명사가 와서 전치사로 쓰인 것’이라고 정답을 풀어 주었고 오답이 B와 같았다. 원문항 발문으로 되돌리고 문장을 새로 썼다.")
f443("E", [("Tom is going to the library now.", MOV("the library")), ("We are going to visit Jeju.", FUT("visit")), ("My mom is going to buy a car.", FUT("buy")), ("I am going to call Jane.", FUT("call")), ("They are going to watch a play.", FUT("watch"))], 1)
f443("F", [("She is going to write a card.", FUT("write")), ("Minho is going to join us.", FUT("join")), ("We are going to take pictures.", FUT("take")), ("They are going to the hospital now.", MOV("the hospital")), ("I am going to read this book.", FUT("read"))], 4)

# 4-44 옳은 문장: 원문항처럼 미래 표현의 서로 다른 형태 오류
R444 = "will과 be going to 뒤에는 동사원형을 쓴다. be going to의 be동사를 빼지 않고, will과 be going to를 겹쳐 쓰지 않으며, 시간·조건 부사절(when, after, if)에서는 미래 대신 현재형을 쓴다."
S444 = "원문항은 미래 표현의 여러 형태 오류(be 누락, will + 과거형, going to + -ing 등)를 판별하는데, 변형 오답은 모두 ‘시간 부사절에 will’ 한 가지였고 유형마다 같았다. 원문항처럼 서로 다른 형태 오류로 오답을 유형마다 새로 썼다."
NOBE = "be going to에서 be동사가 빠졌으므로"; WPAST = "will 뒤에는 과거형이 아니라 동사원형을 쓰므로"; GOING = "be going to 뒤에는 -ing형이 아니라 동사원형을 쓰므로"; WGT = "will과 be going to를 겹쳐 쓸 수 없으므로"; WS = "will 뒤에는 -s를 붙이지 않은 동사원형을 쓰므로"
def f444(t, items, a, s=S444):
    mk(4, 44, t, items, a, R444, s)
f444("B", [("She going to start piano lessons.", NOBE), ("They will eat after they finish the game.", "will + 동사원형과 시간 부사절의 현재형(finish)을 바르게 썼으므로"), ("We will visited the museum tomorrow.", WPAST),
           ("He is going to playing tennis.", GOING), ("I will going to help you.", WGT)], 2)
f444("C", [("Tom going to buy a new phone.", NOBE), ("I will cleaned my room later.", WPAST), ("She will stay home if it rains tomorrow.", "will + 동사원형과 조건 부사절의 현재형(rains)을 바르게 썼으므로"),
           ("We are going to having a picnic.", GOING), ("They will going to leave soon.", WGT)], 3, S444 + " 정답(I will call you when I arrive at the airport.)이 원문항과 같아 새로 썼다.")
f444("D", [("Mina will studies hard for the test.", WS), ("He going to be late.", NOBE), ("I am going to visiting my aunt.", GOING), ("She will study when she gets home.", "will + 동사원형과 시간 부사절의 현재형(gets)을 바르게 썼으므로"), ("We will going to swim.", WGT)], 4)
f444("E", [("Dad will fixes the car tomorrow.", WS), ("We going to watch a movie.", NOBE), ("They are going to moving next month.", GOING), ("I will going to call her.", WGT), ("Tom will go out when the rain stops.", "will + 동사원형과 시간 부사절의 현재형(stops)을 바르게 썼으므로")], 5)
f444("F", [("We will start when Jane comes.", "will + 동사원형과 시간 부사절의 현재형(comes)을 바르게 썼으므로"), ("Jane going to sing at the concert.", NOBE), ("He will took the test next week.", WPAST), ("They are going to building a house.", GOING), ("I will going to study.", WGT)], 1)

# 4-45 옳은 문장 개수: 원문항 형식(ⓐ~ⓔ, 1개~5개)
R445 = "will + 동사원형(부정 will not/won't), be going to + 동사원형(부정 be not going to)으로 쓴다. will에는 -s를 붙이지 않고, not은 will·be동사 뒤에 온다."
S445 = "보기 기호 ⓐ~ⓔ가 a~e로 바뀌어 한 줄로 이어졌고 선택지 순서가 뒤섞였다. 원문항 형식(ⓐ~ⓔ 줄바꿈, 1개~5개)으로 되돌렸다."
def f445(t, lines, judge, ok, s=S445):
    n = len(ok.split(","))
    F(4, 45, t, p="\n".join(lines), c=CNT5, a=n, r=R445, pre=["문장별 판정: " + j for j in judge], k=f"어법상 옳은 문장은 {ok}로 {n}개이다.", n="cnt", s=s + ipos(n))
f445("B", ["ⓐ Tom will be home.", "ⓑ Are they going to visit?", "ⓒ I am not going to go.", "ⓓ She won't studies.", "ⓔ We will eat later."],
     ["ⓐ O. will + 동사원형 be이다.", "ⓑ O. be going to 의문문이다.", "ⓒ O. be going to 부정문이다.", "ⓓ X. won't 뒤에는 동사원형 study를 쓴다.", "ⓔ O. will + 동사원형이다."], "ⓐ, ⓑ, ⓒ, ⓔ")
f445("C", ["ⓐ It will be sunny tomorrow.", "ⓑ She not will come.", "ⓒ Tom going to call you.", "ⓓ They wills arrive soon.", "ⓔ Are you going to visiting him?"],
     ["ⓐ O. will + 동사원형 be이다.", "ⓑ X. not은 will 뒤에 와서 will not come으로 쓴다.", "ⓒ X. be going to의 be동사(is)가 빠졌다.", "ⓓ X. will에는 -s를 붙이지 않는다.", "ⓔ X. going to 뒤에는 동사원형 visit을 쓴다."], "ⓐ",
     "ⓐ~ⓒ가 원문항 문장과 같았고 기호·선택지 순서도 원본과 달랐다. 문장을 새로 쓰고 원문항 형식으로 되돌렸으며 정답 개수를 1개로 바꿨다.")
f445("D", ["ⓐ She will study.", "ⓑ Tom going to play soccer.", "ⓒ We are going to leave.", "ⓓ I won't be late.", "ⓔ Does she going to come?"],
     ["ⓐ O. will + 동사원형이다.", "ⓑ X. be going to의 be동사(is)가 빠졌다.", "ⓒ O. be going to + 동사원형이다.", "ⓓ O. won't + 동사원형이다.", "ⓔ X. be going to 의문문은 Is she going to로 쓴다."], "ⓐ, ⓒ, ⓓ")
f445("E", ["ⓐ They will come.", "ⓑ She is going to study.", "ⓒ Tom won't goes home.", "ⓓ Are you going to play?", "ⓔ We will not be late."],
     ["ⓐ O. will + 동사원형이다.", "ⓑ O. be going to + 동사원형이다.", "ⓒ X. won't 뒤에는 동사원형 go를 쓴다.", "ⓓ O. be going to 의문문이다.", "ⓔ O. will not + 동사원형이다."], "ⓐ, ⓑ, ⓓ, ⓔ",
     S445)
f445("F", ["ⓐ I am going to buy a bag.", "ⓑ Will he come?", "ⓒ She wills study.", "ⓓ We not are going to leave.", "ⓔ They will help us."],
     ["ⓐ O. be going to + 동사원형이다.", "ⓑ O. Will + 주어 + 동사원형 의문문이다.", "ⓒ X. will에는 -s를 붙이지 않는다.", "ⓓ X. not은 be동사 뒤에 와서 are not going to로 쓴다.", "ⓔ O. will + 동사원형이다."], "ⓐ, ⓑ, ⓔ",
     S445 + " 틀린 문장이 하나뿐이던 것을 ⓓ도 틀린 문장으로 바꿔 3개로 했다.")

# 4-46 will + 동사원형: 원문항 발문, C는 문장을 새로
S446 = "발문이 ‘will + 동사원형을 사용하여’라고 정답 구조를 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
for t in "BDEF": F(4, 46, t, st="R", xr=[x for x in [("이 문항은 will 미래형을 요구하므로", "미래의 일에는 will을 쓰므로")] if x[0] in V(4, 46, t)["expl"]], s=S446)
mk(4, 46, "C", [("is travel", "be동사 뒤에 동사원형을 바로 쓸 수 없으므로"), ("will travels", "will 뒤에는 -s를 붙이지 않은 동사원형을 쓰므로"), ("does travel", "does로는 미래를 나타내지 못하므로"),
                ("will travel", "will + 동사원형으로 미래를 바르게 나타냈으므로"), ("will to travel", "will 뒤에 to를 쓰지 않으므로")], 4,
   "미래 조동사 will 뒤에는 동사원형을 쓰며, 주어에 따라 will이나 뒤 동사에 -s를 붙이지 않는다.", "제시문과 정답(will stay)이 원문항과 똑같았고 발문이 정답 구조를 알려 주었다. 제시문을 새로 쓰고 원문항 발문으로 되돌렸다.",
   st="R", p="My parents ________________ to Jeju next month.", okdup=True)

# 4-47 will 의문문 네 번째 단어: 원문항 발문, C는 구조를 새로
S447 = "발문에 ‘Will로 시작하는 의문문’, ‘시간 부사는 문장 끝’ 조건이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
for t in "BDEF": F(4, 47, t, st="R", xr=[x for x in [("이 문항은 시간 부사를 문장 끝에 두도록 지정했다.", "시간 부사는 보통 문장 끝에 둔다.")] if x[0] in V(4, 47, t)["expl"]], s=S447)
mk(4, 47, "C", [("your", "Will your sister help us?에서 두 번째 단어이므로"), ("will", "Will은 첫 번째 단어이므로"), ("help", "Will your sister help us?에서 네 번째 단어이므로"), ("sister", "세 번째 단어이므로"), ("us", "다섯 번째 단어이므로")], 3,
   "will 의문문은 Will + 주어 + 동사원형 ~?의 어순이다.", "‘Will ___ be ready + 시간 부사’ 구조와 정답 단어(ready)가 원문항과 같았다. 단어를 새로 써서 Will your sister help us?로 바꿨다.",
   st="R", p="( your / will / help / sister / us / ? )", okdup=True)

# 4-48 be going to 의문문 짝: 줄바꿈 복원, C는 문장을 새로
S448 = "보기 (가)~(라)의 줄바꿈이 사라져 한 줄로 이어졌다. 원문항처럼 한 줄에 한 문장씩 나눴다. 보기와 정답은 그대로다."
J448 = {"B": ["(가) O. 주어 they에 Are를 썼다.", "(나) O. 단수 주어 Jane에 Is를 썼다.", "(다) X. 주어 we에는 Are를 쓴다.", "(라) X. 주어 you에는 Are를 쓴다."],
        "D": ["(가) O. 단수 주어 Tom에 Is를 썼다.", "(나) O. 복수 주어 the boys에 Are를 썼다.", "(다) X. 주어 they에는 Are를 쓴다.", "(라) X. 단수 주어 Jane에는 Is를 쓴다."],
        "E": ["(가) O. 주어 I에 Am을 썼다.", "(나) O. 주어 you에 Are를 썼다.", "(다) X. 주어 we에는 Are를 쓴다.", "(라) X. 단수 주어 Tom에는 Is를 쓴다."],
        "F": ["(가) O. 단수 주어 she에 Is를 썼다.", "(나) O. 주어 they에 Are를 썼다.", "(다) X. 주어 you에는 Are를 쓴다.", "(라) X. 복수 주어 the boys에는 Are를 쓴다."]}
for t in "BDEF":
    c = V(4, 48, t)["c"]
    F(4, 48, t, p=re.sub(r" (?=\([나-라]\))", "\n", V(4, 48, t)["passage"]), c=c, a=c.index("(가), (나)") + 1,
      r="be going to 의문문은 주어에 맞는 be동사(I-Am, 3인칭 단수-Is, you·복수-Are)를 문장 앞에 둔다.", pre=["문장별 판정: " + j for j in J448[t]],
      k="어법상 옳은 문장은 (가), (나)이다.", n=setnotes(c, "(가), (나)", "옳은 문장"), okdup=True, s=S448)
c448 = ["(가), (나)", "(나), (다)", "(다), (라)", "(가), (다)", "(가), (라)"]
F(4, 48, "C", p="(가) Is your dad going to drive?\n(나) Am you going to come?\n(다) Are the students going to sing?\n(라) Is they going to eat?", c=c448, a=4,
  r="be going to 의문문은 주어에 맞는 be동사(I-Am, 3인칭 단수-Is, you·복수-Are)를 문장 앞에 둔다.",
  pre=["문장별 판정: (가) O. 단수 주어 your dad에 Is를 썼다.", "문장별 판정: (나) X. 주어 you에는 Are를 쓴다.", "문장별 판정: (다) O. 복수 주어 the students에 Are를 썼다.", "문장별 판정: (라) X. 주어 they에는 Are를 쓴다."],
  k="어법상 옳은 문장은 (가), (다)이다.", n=setnotes(c448, "(가), (다)", "옳은 문장"), okdup=True,
  s="(가)~(다)가 원문항 문장과 같았고 정답 조합((가), (라))도 같았다. 문장을 새로 쓰고 원문항처럼 줄바꿈했으며 정답 조합을 (가), (다)로 바꿨다." + ipos(4))

# 4-49 -ing를 동사원형으로 고치는 이유: 원문항 밑줄, 그럴듯한 오개념 오답
R449 = "be going to의 to는 부정사를 만드는 to이므로 뒤에 동사원형이 와서 미래의 계획을 나타낸다."
S449 = "원문항 오답은 그럴듯한 오개념 설명인데, 변형 오답(‘미래문에는 일반동사를 쓰면 안 된다’ 등)은 뻔하고 유형마다 반복되었으며, 정답만 제시 문장의 동사를 직접 언급해 눈에 띄었다. 밑줄도 사라졌다. 원문항처럼 밑줄을 넣고, 그럴듯한 오개념으로 오답을 유형마다 새로 썼다."
TOINF = "be going to의 to는 부정사의 to라 뒤에 동사원형이 오므로 바른 설명이라"
def f449(t, ing, base, jo1, jo2, p, items, a, s=S449):
    st = f"다음 문장에서 '{ing}'{jo1} '{base}'{jo2} 고쳐야 하는 이유를 가장 바르게 설명한 것은?"
    mk(4, 49, t, items, a, R449, s, st=st, p=p)
f449("B", "studying", "study", "을", "로", "Tom is going to <u>studying</u> tonight.",
     [("'Tom'이 3인칭 단수이므로 동사에 -ing를 붙이면 안 되기 때문이다.", "주어의 인칭은 -ing형과 관계없으므로"), ("'tonight'은 아직 오지 않은 때이므로 -ing형을 쓸 수 없기 때문이다.", "때를 나타내는 말이 아니라 to 때문에 동사원형을 쓰므로"),
      ("'is' 뒤에는 반드시 동사원형이 와야 하기 때문이다.", "is 바로 뒤가 아니라 to 뒤의 동사를 고치는 것이므로"), ("'be going to'의 'to'는 부정사를 만드는 to이므로 뒤에 동사원형이 와야 하기 때문이다.", TOINF),
      ("'study'는 '공부하다'의 뜻일 때 -ing형으로 쓸 수 없기 때문이다.", "study도 -ing형(studying)으로 쓸 수 있으므로")], 4)
f449("C", "joining", "join", "을", "으로", "My brother is going to <u>joining</u> the soccer team.",
     [("'join'은 '가입하다'의 뜻일 때 진행형으로 쓸 수 없기 때문이다.", "동사의 뜻이 아니라 to 때문에 동사원형을 쓰므로"), ("'be going to' 뒤의 'to'는 전치사가 아니라 부정사의 to이므로 뒤에 동사원형이 와야 하기 때문이다.", TOINF),
      ("'My brother'가 단수이므로 -ing 대신 -s를 붙여야 하기 때문이다.", "to 뒤에는 -s형이 아니라 동사원형을 쓰므로"), ("'is'가 이미 있으므로 동사를 한 번 더 -ing로 쓸 수 없기 때문이다.", "is going이 진행형이라서가 아니라 to 뒤라서 동사원형을 쓰므로"),
      ("'team' 앞에 'the'가 있으면 동사는 원형으로 써야 하기 때문이다.", "관사는 동사의 형태와 관계없으므로")], 2,
     "문장과 정답 설명이 원문항과 같았다. 문장을 새로 쓰고 " + S449[S449.index("원문항처럼"):])
f449("D", "playing", "play", "을", "로", "They are going to <u>playing</u> soccer after school.",
     [("'They'가 복수이므로 동사에 -ing를 붙이면 안 되기 때문이다.", "주어의 수는 -ing형과 관계없으므로"), ("'after school'은 미래를 나타내므로 동사원형만 쓸 수 있기 때문이다.", "때를 나타내는 말이 아니라 to 때문에 동사원형을 쓰므로"),
      ("'be going to'의 'to'는 부정사를 만드는 to이므로 동사원형 play가 와야 하기 때문이다.", TOINF), ("'soccer' 같은 운동 이름 앞에는 -ing형을 쓸 수 없기 때문이다.", "운동 이름 앞에도 -ing형을 쓸 수 있으므로"),
      ("'are' 뒤에는 반드시 과거분사가 와야 하기 때문이다.", "are 뒤에는 -ing형이나 형용사 등도 올 수 있으므로")], 3)
f449("E", "buying", "buy", "을", "로", "I am going to <u>buying</u> a new bag.",
     [("'I'가 1인칭이므로 -ing형을 쓸 수 없기 때문이다.", "주어의 인칭은 -ing형과 관계없으므로"), ("'buy'는 불규칙 동사라서 -ing를 붙일 수 없기 때문이다.", "buy도 buying으로 쓸 수 있으므로"),
      ("'a new bag'처럼 목적어가 있으면 동사는 원형으로만 써야 하기 때문이다.", "목적어가 있어도 -ing형을 쓸 수 있으므로"), ("'am' 뒤에는 동사원형이 와야 하기 때문이다.", "am 바로 뒤에는 동사원형을 쓸 수 없으므로"),
      ("'be going to'의 'to' 뒤에는 동사원형이 와서 미래의 계획을 나타내기 때문이다.", TOINF)], 5)
f449("F", "leaving", "leave", "을", "로", "We are going to <u>leaving</u> early tomorrow.",
     [("'be going to'의 'to'는 부정사를 만드는 to이므로 뒤에 동사원형 leave가 와야 하기 때문이다.", TOINF), ("'tomorrow'가 있으면 현재진행형을 쓸 수 없으므로 -ing를 빼야 하기 때문이다.", "tomorrow가 아니라 to 때문에 동사원형을 쓰므로"),
      ("'We'가 복수이므로 -ing 대신 -s를 붙여야 하기 때문이다.", "to 뒤에는 -s형이 아니라 동사원형을 쓰므로"), ("'leave'는 '떠나다'의 뜻일 때 동사원형으로만 쓰이기 때문이다.", "leave도 leaving으로 쓸 수 있으므로"),
      ("'early' 앞에서는 동사가 -ing형이 될 수 없기 때문이다.", "부사 early는 동사의 형태와 관계없으므로")], 1)

# 4-50 옳은 것만 묶은 것: 원문항 형식(<보기> 줄바꿈, 세 개 조합)
ST450 = "다음 <보기>의 문장 중 어법상 옳은 것만 묶은 것은?"
R450 = "will + 동사원형(부정 won't), be going to + 동사원형(부정 be not going to, 의문 Be동사 + 주어 + going to)으로 쓴다. be동사를 빼거나 -ing·-s형을 쓰면 틀린다."
S450 = "원문항은 옳은 문장 세 개의 조합을 고르는데, 변형은 ‘빠짐없이 모두’ 고르는 형식(2~4개 조합)으로 바뀌었고 <보기> 줄바꿈이 사라졌다. 원문항 발문과 형식(<보기> 줄바꿈, 세 개 조합)으로 되돌리고, 서너 낱말뿐이던 문장을 원문항 길이에 가깝게 늘렸다."
def f450(t, lines, judge, ok, c, s=S450):
    a = c.index(ok) + 1
    F(4, 50, t, st=ST450, p="<보기>\n" + "\n".join(lines), c=c, a=a, r=R450, pre=["문장별 판정: " + j for j in judge], k=f"어법상 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), okdup=True, s=s + ipos(a))
REF3 = ["(A), (B), (C)", "(B), (C), (D)", "(A), (D), (E)", "(B), (D), (E)", "(C), (D), (E)"]
f450("B", ["(A) She will study English after dinner.", "(B) Tom is going to play tennis this weekend.", "(C) We going to leave for Busan tomorrow.", "(D) Will they come to the party tonight?", "(E) Jane won't goes home before six."],
     ["(A) O. will + 동사원형이다.", "(B) O. be going to + 동사원형이다.", "(C) X. be going to의 be동사(are)가 빠졌다.", "(D) O. Will + 주어 + 동사원형 의문문이다.", "(E) X. won't 뒤에는 동사원형 go를 쓴다."], "(A), (B), (D)",
     ["(A), (B), (C)", "(A), (B), (D)", "(B), (C), (E)", "(B), (D), (E)", "(C), (D), (E)"])
f450("C", ["(A) Tom is going to be a teacher someday.", "(B) She will goes shopping with her mom.", "(C) Are they going to join us for lunch?", "(D) We won't be late for the meeting.", "(E) He is going to visiting Busan next week."],
     ["(A) O. be going to + 동사원형 be이다.", "(B) X. will 뒤에는 동사원형 go를 쓴다.", "(C) O. be going to 의문문이다.", "(D) O. won't + 동사원형이다.", "(E) X. going to 뒤에는 동사원형 visit을 쓴다."], "(A), (C), (D)",
     ["(A), (B), (C)", "(B), (C), (D)", "(A), (C), (D)", "(B), (D), (E)", "(C), (D), (E)"], S450 + " (A)(B)(E)가 원문항 문장과 거의 같고 정답 조합도 같아 문장을 새로 썼다.")
f450("D", ["(A) They will playing soccer after school.", "(B) Are Tom going to study in the library?", "(C) Is she going to cook dinner tonight?", "(D) We won't leave before the game ends.", "(E) I am going to buy it next month."],
     ["(A) X. will 뒤에는 동사원형 play를 쓴다.", "(B) X. 단수 주어 Tom에는 Is를 쓴다.", "(C) O. be going to 의문문이다.", "(D) O. won't + 동사원형이다.", "(E) O. be going to + 동사원형이다."], "(C), (D), (E)", REF3)
f450("E", ["(A) Tom will come to my house tomorrow.", "(B) They going to visit us this weekend.", "(C) She won't studies on Sunday.", "(D) Are you going to wash the car today?", "(E) We will be ready in ten minutes."],
     ["(A) O. will + 동사원형이다.", "(B) X. be going to의 be동사(are)가 빠졌다.", "(C) X. won't 뒤에는 동사원형 study를 쓴다.", "(D) O. be going to 의문문이다.", "(E) O. will + 동사원형 be이다."], "(A), (D), (E)", REF3)
f450("F", ["(A) Jane is going to read a book tonight.", "(B) Will he go to the concert with us?", "(C) They are not going to leave early.", "(D) Tom wills study for the test.", "(E) Are we going to eating out tonight?"],
     ["(A) O. be going to + 동사원형이다.", "(B) O. Will + 주어 + 동사원형 의문문이다.", "(C) O. be going to 부정문이다.", "(D) X. will에는 -s를 붙이지 않는다.", "(E) X. going to 뒤에는 동사원형 eat을 쓴다."], "(A), (B), (C)", REF3)


# ---- 2차 감수(2026-10) 추가 ----
# 4-42 B~F: 부정문이 아닌 보기(원래 문장 그대로)는 발문만 보고 지워짐 → 원문항처럼 not을 잘못 쓴 문장으로, 정답 위치도 원문항(③)과 다르게
S442N = S442 + " 부정문으로 바꾸지 않은 보기(원래 문장 그대로)는 발문만 보고 지워져, 원문항처럼 not을 잘못 쓴 문장으로 바꿨다."
def g442(t, sub, be, do, rest, order, s=S442N):
    FIX.pop((4, 42, t), None)
    its = {"ok": (f"{sub} {be} not going to {rest}.", f"be동사({be}) 뒤에 not을 바르게 넣었으므로"), "nogo": (f"{sub} {be} not go to {rest}.", "going을 go로 바꿔 틀렸으므로"),
           "do": (f"{sub} {do} not going to {rest}.", f"be going to는 do나 does로 부정하지 않으므로"), "notbe": (f"{sub} not {be} going to {rest}.", NOTBE),
           "will": (f"{sub} will {be} not going to {rest}.", "will과 be going to를 겹쳐 쓸 수 없으므로")}
    mk(4, 42, t, [its[k] for k in order], order.index("ok") + 1, R442, s, st="R", p=f"{sub} {be} going to {rest}.")
g442("B", "Tom", "is", "does", "visit his uncle", ["ok", "nogo", "notbe", "do", "will"])
g442("C", "Mina", "is", "does", "join the club", ["nogo", "do", "notbe", "will", "ok"], "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘Mina is going to join the club.’으로 바꾸고 원문항 발문으로 되돌렸으며, 오답은 원문항처럼 모두 not을 잘못 쓴 문장으로 썼다.")
g442("D", "They", "are", "do", "play soccer", ["do", "ok", "will", "nogo", "notbe"])
g442("E", "I", "am", "do", "buy a new bag", ["nogo", "will", "notbe", "ok", "do"], S442N + " 없는 형태(amn't)도 없앴다.")
g442("F", "We", "are", "do", "leave early", ["ok", "nogo", "notbe", "will", "do"])

# 4-48 D, E, F: B·D·E·F의 정답이 모두 (가), (나) → 문장 순서를 바꿔 정답 조합을 달리
R448 = "be going to 의문문은 주어에 맞는 be동사(I-Am, 3인칭 단수-Is, you·복수-Are)를 문장 앞에 둔다."
S448N = "보기 (가)~(라)의 줄바꿈이 사라져 한 줄로 이어졌고, B·D·E·F의 정답이 모두 (가), (나)로 같았다. 원문항처럼 한 줄에 한 문장씩 나누고, 문장 순서를 바꿔 유형마다 정답 조합을 달리했다."
C448R = ["(가), (나)", "(나), (다)", "(다), (라)", "(나), (라)", "(가), (라)"]
def f448(t, lines, judge, ok):
    FIX.pop((4, 48, t), None)
    F(4, 48, t, p="\n".join(lines), c=C448R, a=C448R.index(ok) + 1, r=R448, pre=["문장별 판정: " + j for j in judge], k=f"어법상 옳은 문장은 {ok}이다.", n=setnotes(C448R, ok, "옳은 문장"), okdup=True, s=S448N + ipos(C448R.index(ok) + 1))
f448("D", ["(가) Is they going to study?", "(나) Is Tom going to come?", "(다) Are Jane going to cook?", "(라) Are the boys going to play?"],
     ["(가) X. 주어 they에는 Are를 쓴다.", "(나) O. 단수 주어 Tom에 Is를 썼다.", "(다) X. 단수 주어 Jane에는 Is를 쓴다.", "(라) O. 복수 주어 the boys에 Are를 썼다."], "(나), (라)")
f448("E", ["(가) Is we going to leave?", "(나) Am I going to buy it?", "(다) Are you going to help?", "(라) Are Tom going to study?"],
     ["(가) X. 주어 we에는 Are를 쓴다.", "(나) O. 주어 I에 Am을 썼다.", "(다) O. 주어 you에 Are를 썼다.", "(라) X. 단수 주어 Tom에는 Is를 쓴다."], "(나), (다)")
f448("F", ["(가) Am you going to study?", "(나) Is the boys going to play?", "(다) Is she going to visit?", "(라) Are they going to come?"],
     ["(가) X. 주어 you에는 Are를 쓴다.", "(나) X. 복수 주어 the boys에는 Are를 쓴다.", "(다) O. 단수 주어 she에 Is를 썼다.", "(라) O. 주어 they에 Are를 썼다."], "(다), (라)")
