# 2026-10-26 전체 감수 반영 — 3급. 규칙은 z9a와 같다.
MEMO6 = "감수 메모 반영(10-26): "
def OKS(items, a): return [w + OK(i + 1, a) for i, w in enumerate(items)]
def ADD(g_, n_, t_, more): return (OLD(g_, n_, t_).get("s", "") + " " + more).strip()
CNT = ["1개", "2개", "3개", "4개", "5개"]
LEN = MEMO6 + "원문항보다 짧던 문장을 원문항 길이 이상으로 늘렸다. 틀린 곳과 정답은 그대로다."
LENP = MEMO6 + "원문항보다 짧던 지문을 원문항 길이 이상으로 늘렸다. 보기와 정답은 그대로다."
LENC = MEMO6 + "원문항보다 짧던 보기 문장을 원문항 길이 이상으로 늘렸다. 정답 위치는 그대로다."
SIB = " (같은 번호 다른 유형의 메모와 같은 문제)"
STEP = "풀이 순서 정정(10-26): 풀이 순서가 예전 문항 내용을 설명하고 있어 지금 문항에 맞게 고쳤다."
def L(g_, n_, t_, **kw): RE(g_, n_, t_, s=ADD(g_, n_, t_, kw.pop("why", LEN)), **kw)
def P(g_, n_, t_): return OLD(g_, n_, t_).get("p") or V(g_, n_, t_)["passage"]
def C_(g_, n_, t_): return list(OLD(g_, n_, t_).get("c") or V(g_, n_, t_)["c"])
def REP(s_, *pairs):
    for a_, b_ in pairs:
        assert a_ in s_, (a_, s_); s_ = s_.replace(a_, b_)
    return s_

# 3-6 E·F
L(3, 6, "E", p="There ______ two big dogs playing in the park near my house now.")
L(3, 6, "F", p="There ______ a lot of snow on the mountains near our town last winter.", why=LEN + SIB)

# 3-17 E·F
L(3, 17, "E", p="You like this song very much.", c=[x.replace(" song?", " song very much?") for x in C_(3, 17, "E")], why=LEN)
L(3, 17, "F", p="We need more time for the project.", c=[x.replace(" time?", " time for the project?") for x in C_(3, 17, "F")], why=LEN + SIB)

# 3-18 E
RE(3, 18, "E", p="I like coffee with milk in the morning.", c=[x.replace("coffee.", "coffee with milk in the morning.") for x in C_(3, 18, "E")], a=4,
   n=OKS(["do not 뒤에는 동사원형 like를 써야 하므로", "not만으로는 일반동사를 부정할 수 없으므로", "일반동사의 부정에 be동사를 쓰지 않으므로", "do not + 동사원형으로 바르게 바꿨으므로", "주어 I에는 does가 아니라 do를 쓰므로"], 4), s=ADD(3, 18, "E", LEN))

# 3-19 C·D·F: 설명 보기를 ⓐ~ⓔ 순서로(D 메모). E는 확인 완료라 그대로
def SORT19(t_, why):
    old = OLD(3, 19, t_); c = list(old["c"]); nn = list(old["n"]); a = old["a"]
    order = sorted(range(5), key=lambda i: "ⓐⓑⓒⓓⓔ".index(c[i][0]))
    na = order.index(a - 1) + 1
    RE(3, 19, t_, c=[c[i] for i in order], n=[nn[i] for i in order], a=na, s=ADD(3, 19, t_, why + pos(na)))
SORT19("D", MEMO6 + "설명 보기를 메모대로 ⓐ~ⓔ 순서에 맞춰 ①~⑤에 놓았다.")
SORT19("C", MEMO6 + "같은 번호 D의 메모에 맞춰 설명 보기를 ⓐ~ⓔ 순서로 놓았다.")
SORT19("F", MEMO6 + "같은 번호 D의 메모에 맞춰 설명 보기를 ⓐ~ⓔ 순서로 놓았다.")

# 3-24 D·E·F
L(3, 24, "D", p=REP(P(3, 24, "D"), ("unusual story.", "unusual story about my grandfather."), (" book.", " book about animals yesterday.")))
L(3, 24, "E", p=REP(P(3, 24, "E"), (" hour.", " hour at the bus stop."), (" bike.", " bike, and he rides it every day.")))
L(3, 24, "F", p=REP(P(3, 24, "F"), ("one-way ticket.", "one-way ticket to Busan yesterday."), (" umbrella.", " umbrella in her bag today.")), why=LEN + SIB)

# 3-28 D·E·F: 원문항처럼 두 사람의 대화(묻고 답하기)로
L28 = MEMO6 + "원문항은 두 사람이 묻고 답하는 대화인데 변형은 한 사람의 말이라 유형이 달랐다. 원문항처럼 대화로 바꾸고 문장을 늘렸다. 정답 위치는 그대로다."
RE(3, 28, "D", p="Amy: What did you have for <u>a dinner</u> last night?\nBen: I had spaghetti with my family.", s=ADD(3, 28, "D", L28))
RE(3, 28, "E", p="Mina: What time do you usually eat <u>a lunch</u> at school?\nLeo: We usually eat at twelve thirty.", c=["lunch", "the lunch", "lunches", "some lunches", "any lunches"], a=1,
   n=["lunch: 일상적인 식사 이름은 관사 없이 단수로 쓰므로 정답이다.", "the lunch: 식사 이름 앞에는 the도 쓰지 않으므로 오답이다.", "lunches: 식사 이름은 복수형으로 쓰지 않으므로 오답이다.", "some lunches: 식사 이름은 복수형으로 쓰지 않으므로 오답이다.", "any lunches: 식사 이름은 복수형으로 쓰지 않으므로 오답이다."], s=ADD(3, 28, "E", L28))
RE(3, 28, "F", p="Jane: Did you eat <u>a breakfast</u> before you came to school?\nTom: No, I got up too late this morning.", s=ADD(3, 28, "F", L28 + SIB))

# 3-32 D·E·F: 대화와 밑줄 문장을 함께 늘림(보기도 그에 맞춤)
RE(3, 32, "D", p="A: What was Jane doing in the kitchen an hour ago?\nB: <u>She was cooking dinner for her family.</u>",
   c=["그녀는 가족을 위해 저녁을 만들고 있었다.", "그녀는 가족을 위해 저녁을 만들지 않았다.", "그녀는 가족을 위해 저녁을 다 만들었다.", "그녀는 가족을 위해 저녁을 자주 만든다.", "그녀는 가족을 위해 저녁을 만들 것이다."], a=1,
   n=OKS(["was cooking(과거진행)을 ‘만들고 있었다’로 바르게 옮겼으므로", "‘만들지 않았다’는 부정이라 뜻이 반대이므로", "‘다 만들었다’는 끝난 일이라 진행의 뜻이 빠졌으므로", "‘자주 만든다’는 현재의 습관이므로", "‘만들 것이다’는 미래이므로"], 1), s=ADD(3, 32, "D", LEN))
RE(3, 32, "E", p="A: I called you at nine last night. What were you doing then?\nB: <u>I was reading a book in my room.</u>",
   c=["나는 그때 내 방에서 책을 읽을 것이다.", "나는 그때 내 방에서 책을 읽고 있었다.", "나는 그때 내 방에서 책을 다 읽었다.", "나는 그때 내 방에서 책을 읽지 않았다.", "나는 그때 내 방에서 책을 자주 읽는다."], a=2,
   n=OKS(["‘읽을 것이다’는 미래이므로", "was reading(과거진행)을 ‘읽고 있었다’로 바르게 옮겼으므로", "‘다 읽었다’는 끝난 일이라 진행의 뜻이 빠졌으므로", "‘읽지 않았다’는 부정이라 뜻이 반대이므로", "‘자주 읽는다’는 현재의 습관이므로"], 2), s=ADD(3, 32, "E", LEN))
RE(3, 32, "F", p="A: What was your dog doing when you came home from school?\nB: <u>It was sleeping on the sofa.</u>",
   c=["그 개는 소파에서 자지 않았다.", "그 개는 소파에서 잠에서 깼다.", "그 개는 소파에서 자고 있었다.", "그 개는 소파에서 잘 것이다.", "그 개는 소파에서 자주 잔다."], a=3,
   n=OKS(["‘자지 않았다’는 부정이라 뜻이 반대이므로", "‘잠에서 깼다’는 다른 동작이므로", "was sleeping(과거진행)을 ‘자고 있었다’로 바르게 옮겼으므로", "‘잘 것이다’는 미래이므로", "‘자주 잔다’는 현재의 습관이므로"], 3), s=ADD(3, 32, "F", LEN + SIB))

# 3-34 D·E·F
L(3, 34, "D", p="I will _____ busy with my homework tomorrow.\nJane _____ reading a book when I arrived home.\nI _____ going to study math tonight.")
L(3, 34, "E", p="We will _____ ready for the trip soon.\nThe boys _____ running in the park then.\nI _____ going to buy a new bag tomorrow.")
L(3, 34, "F", p="She will _____ fine after a good rest.\nI _____ sleeping in my room at 10 last night.\nThey _____ going to visit us next weekend.", why=LEN + SIB)

# 3-38 E·F
L(3, 38, "E", p="Mina: ______ ______ ______ TV in the living room after dinner?\nLeo: Yes, he was.")
L(3, 38, "F", p="Amy: ______ ______ ______ dinner when I called you last night?\nJane: Yes, I was.", why=LEN + SIB)

# 3-43 D·F
L(3, 43, "D", p="Children, please help ________ to some chocolate cake.\nYou can finish the project by ________.")
L(3, 43, "F", p="Boys, please make ________ at home tonight.\nTake good care of ________ on the camping trip.", why=LEN + SIB)

# 3-46 D·E·F: 보기를 한 갈래(달끼리, 요일끼리)로
L46 = MEMO6 + "보기에 요일과 달이 섞여 있어 질문과 다른 갈래는 바로 지워졌다. 질문에 맞춰 보기를 모두 {}(으)로 바꿨다."
RE(3, 46, "D", p="Kelly: What month is it now?\nTom: It's __________. (5월이야)", c=["March", "April", "May", "June", "July"], a=3,
   n=["March는 3월이라 5월과 다르므로 오답이다.", "April은 4월이라 5월과 다르므로 오답이다.", "May가 5월이므로 정답이다.", "June은 6월이라 5월과 다르므로 오답이다.", "July는 7월이라 5월과 다르므로 오답이다."], s=ADD(3, 46, "D", L46.format("달 이름") + pos(3)))
RE(3, 46, "E", c=["Sunday", "Tuesday", "Wednesday", "Monday", "Thursday"], a=4,
   n=["Sunday는 일요일이라 월요일과 다르므로 오답이다.", "Tuesday는 화요일이라 월요일과 다르므로 오답이다.", "Wednesday는 수요일이라 월요일과 다르므로 오답이다.", "Monday가 월요일이므로 정답이다.", "Thursday는 목요일이라 월요일과 다르므로 오답이다."], s=ADD(3, 46, "E", L46.format("요일 이름") + pos(4)))
RE(3, 46, "F", c=["November", "December", "January", "June", "October"], a=2,
   n=["November는 11월이라 12월과 다르므로 오답이다.", "December가 12월이므로 정답이다.", "January는 1월이라 12월과 다르므로 오답이다.", "June은 6월이라 12월과 다르므로 오답이다.", "October는 10월이라 12월과 다르므로 오답이다."], s=ADD(3, 46, "F", L46.format("달 이름") + pos(2) + SIB))

# 3-48 E·F
RE(3, 48, "E", p="Tom이 우리에게 그의 가족 사진 한 장을 보여주었다.\n(picture / Tom / showed / us / a / of his family / .)",
   c=["Tom showed a picture of his family us.", "Tom us showed a picture of his family.", "Showed Tom us a picture of his family.", "Tom showed us a picture of his family.", "Tom showed we a picture of his family."], a=4,
   n=OKS(["사람(us)이 사물 뒤에 놓였는데 전치사가 없으므로", "동사 showed가 사람(us) 뒤에 놓였으므로", "주어 Tom보다 동사가 먼저 나와 평서문 어순이 아니므로", "동사 + 사람(us) + 사물(a picture of his family) 순서로 바르게 배열했으므로", "사람 자리에 주격 we를 썼으므로"], 4), s=ADD(3, 48, "E", LEN))
RE(3, 48, "F", p="선생님이 그들에게 많은 수학 숙제를 주셨다.\n(teacher / gave / them / homework / the / a lot of / math / .)",
   c=["The teacher gave they a lot of math homework.", "The teacher them gave a lot of math homework.", "The teacher gave them a lot of math homework.", "The teacher gave a lot of math homework them.", "Gave the teacher them a lot of math homework."], a=3,
   n=OKS(["사람 자리에 주격 they를 썼으므로", "동사 gave가 사람(them) 뒤에 놓였으므로", "동사 + 사람(them) + 사물(a lot of math homework) 순서로 바르게 배열했으므로", "사람(them)이 사물 뒤에 놓였는데 전치사가 없으므로", "주어보다 동사가 먼저 나와 평서문 어순이 아니므로"], 3), s=ADD(3, 48, "F", LEN + SIB))

# 3-53 D·F
L(3, 53, "D", p="A: The road is icy this morning.\nB: <u>You had better drive slowly</u> to stay safe.", why=LENP)
L(3, 53, "F", p="A: It's raining hard outside now.\nB: <u>You had better take an umbrella</u> with you today.", why=LENP + SIB)

# 3-66 E·F
L(3, 66, "E", p="How ______ students are there in your class this year?")
L(3, 66, "F", p="How ______ time do you have before the next class?", why=LEN + SIB)

# 3-68 D·E·F
L(3, 68, "D", p="그들은 방과 후에 어떻게 집에 가니?\n(how / get / home / do / they / after school / ?)",
  c=["How do they get home after school?", "How do get they home after school?", "How they get home after school do?", "Do how they get home after school?", "How they do get home after school?"])
L(3, 68, "E", p="Tom은 매일 아침 어떻게 일하러 가니?\n(how / get / to work / does / Tom / every morning / ?)",
  c=["How Tom does get to work every morning?", "How does Tom get to work every morning?", "How does get Tom to work every morning?", "How Tom get to work every morning does?", "Does how Tom get to work every morning?"])
L(3, 68, "F", p="우리는 기차역에서 어떻게 거기에 가니?\n(how / get / there / do / we / from the station / ?)",
  c=["How we get there from the station do?", "How we do get there from the station?", "How do we get there from the station?", "How do get we there from the station?", "Do how we get there from the station?"], why=LEN + SIB)

# 3-71 D·E·F
L(3, 71, "D", p=REP(P(3, 71, "D"), ("a friend to talk", "a close friend to talk"), ("</u>).", "</u>) about her problems.")))
L(3, 71, "E", p=REP(P(3, 71, "E"), ("a room to study", "a quiet room to study"), ("</u>).", "</u>) during the exam week.")))
L(3, 71, "F", p=REP(P(3, 71, "F"), ("He found a bed to sleep", "After the long trip, he finally found a soft bed to sleep")), why=LEN + SIB)

# 3-72 E·F
L(3, 72, "E", p="Jane knows ________ the bus to the museum on Saturday.")
L(3, 72, "F", p="We don't know ________ for help with this difficult problem.", why=LEN + SIB)

# 3-84 D·F: 정답만 동명사가 없어 쉽게 드러남 → to부정사를 쓴 옳은 문장을 오답에 넣음(원문항의 expect to처럼)
L84 = MEMO6 + "정답 보기만 동명사가 없어 쉽게 고를 수 있었다. 원문항의 expect to처럼 to부정사를 바르게 쓴 문장을 오답에 넣고, 보기 문장도 원문항 길이 이상으로 늘렸다. 정답 위치는 그대로다."
RE(3, 84, "D", c=["My brother is good at cooking Italian food.", "I want to visit my grandmother this weekend.", "She kept talking on the phone for an hour.", "Do you mind helping me with this box?", "Tom is worried about fail the math test."], a=5,
   n=["전치사 at 뒤에 동명사를 바르게 썼으므로 오답이다.", "want는 to부정사를 목적어로 쓰므로 to visit이 바르다. 따라서 오답이다.", "keep + 동명사를 바르게 썼으므로 오답이다.", "mind + 동명사를 바르게 썼으므로 오답이다.", "전치사 about 뒤에는 동명사(failing)를 써야 하므로 정답이다."], s=ADD(3, 84, "D", L84))
RE(3, 84, "F", c=["They talked about move to Seoul next year.", "Would you mind turning off the TV?", "We decided to stay at home all day.", "She is excited about going on a trip.", "Instead of taking a bus, we walked to school."], a=1,
   n=["전치사 about 뒤에는 동명사(moving)를 써야 하므로 정답이다.", "mind + 동명사를 바르게 썼으므로 오답이다.", "decide는 to부정사를 목적어로 쓰므로 to stay가 바르다. 따라서 오답이다.", "전치사 about 뒤에 동명사를 바르게 썼으므로 오답이다.", "전치사 instead of 뒤에 동명사를 바르게 썼으므로 오답이다."], s=ADD(3, 84, "F", L84 + SIB))

# 3-85 E·F
L(3, 85, "E", p="ⓐ He <u>suggested going</u> home early after the party.\nⓑ She <u>wants learning</u> English in Canada.\nⓒ They <u>avoid to drive</u> at night in winter.\nⓓ We <u>decided to stay</u> home this weekend.")
L(3, 85, "F", p="ⓐ Jane <u>plans visiting</u> Busan with her friends this summer.\nⓑ Tom <u>likes playing</u> soccer after school.\nⓒ We <u>finished eating</u> lunch at noon.\nⓓ I <u>gave up to learn</u> the violin last year.", why=LEN + SIB)

# 3-88 E(메모: the dishes를 나눔)·F(길이)
RE(3, 88, "E", p="Jane은 설거지하는 것을 꺼리니?\n(Jane / mind / wash / the / dishes / does / ?)", s=ADD(3, 88, "E", MEMO6 + "메모대로 the dishes를 the / dishes로 나눠 원문항처럼 한 낱말씩 늘어놓았다. 보기와 정답은 그대로다."))
L(3, 88, "F", p="그들은 내일 일찍 떠나는 것을 꺼리니?\n(they / mind / leave / early / tomorrow / do / ?)",
  c=["Do they mind leaving early tomorrow?", "Do they mind to leave early tomorrow?", "They do mind to leave early tomorrow?", "Do they mind leave early tomorrow?", "Do mind they leaving early tomorrow?"], why=LEN + SIB)

# 3-97 E
L(3, 97, "E", p="Open your mouth <u>widely</u> so the dentist can check your teeth.\n(치과 의사가 이를 볼 수 있도록 입을 활짝 벌려라.)",
  c=[x[:-1] + " so the dentist can check your teeth." for x in C_(3, 97, "E")], why=LEN + " 풀이 순서도 이 문항(widely/wide)에 맞게 고쳤다.")

# 3-100 D·F
L(3, 100, "D", p="ⓐ I have a little money in my pocket for the bus.\nⓑ She sings beautifully on the stage at the school festival.\nⓒ Tom seems tired after the long trip to Jeju Island.\nⓓ They have much books about animals in their library.\nⓔ My uncle drove careful on the icy road last night.")
L(3, 100, "F", p="ⓐ I have much friends in my new school in Seoul.\nⓑ She looks happily in the picture with her dog.\nⓒ Tom runs fastly every morning to catch the bus.\nⓓ We have few money for the family trip this summer.\nⓔ I want to drink cold something after the soccer game.", why=LEN + SIB)

# 3-103 E·F
L(3, 103, "E", p="Our classroom has as ______ chairs as the library on the second floor.")
L(3, 103, "F", p="Tom drinks as ______ water as his older brother every day.", why=LEN + SIB)

# 3-111 D·F
L(3, 111, "D", p=REP(P(3, 111, "D"), ("the table.", "the kitchen table next to the cups."), ("My birthday is", "My birthday party is"), ("June 10th.", "June 10th this year.")), why=LEN + " 풀이 순서도 이 문항에 맞게 고쳤다.")
L(3, 111, "F", p=REP(P(3, 111, "F"), ("My sister lives", "My older sister lives"), ("Canada.", "Canada with her husband."), ("It often snows", "It often snows a lot"), ("December.", "December in that city.")), why=LEN + SIB + " 풀이 순서도 이 문항에 맞게 고쳤다.")

# 3-112 E·F
L(3, 112, "E", p=REP(P(3, 112, "E"), ("Where is the station?", "Where is the subway station?"), ("the bank.", "the bank on Main Street.")))
L(3, 112, "F", p=REP(P(3, 112, "F"), ("Where is Minsu?", "Where is Minsu now?"), ("He's reading (", "He's reading a book (")), why=LEN + SIB + " 풀이 순서도 이 문항(at home, in his room)에 맞게 고쳤다.")

# 3-113 D
L(3, 113, "D", p=REP(P(3, 113, "D"), ("It kept raining", "It kept raining all day"), ("I'll be back", "I'll be back home"), ("five o'clock.", "five o'clock today.")), why=LEN + " 풀이 순서도 이 문항에 맞게 고쳤다.")

# 3-125 D: neither A nor B → not ~ A or B는 부정 범위의 문제라 원문항(상관접속사 바꿔 쓰기)과 겨냥이 다르고 오해를 낳음 → 상관접속사 자체를 묻게
RE(3, 125, "D", p=REP(P(3, 125, "D"), ("She likes neither coffee nor tea.", "Tom can't swim in the sea, and Jane can't swim there either."), ("= She doesn't like coffee", "= Neither Tom"), (" tea.", " Jane can swim in the sea.")),
   c=["or", "and", "but also", "nor", "as well as"], a=4,
   n=["Neither는 nor와 짝을 이룬다. or를 쓰면 짝이 맞지 않으므로 오답이다.", "Neither는 and와 짝을 이루지 않으므로 오답이다.", "but also는 not only와 짝을 이루므로 오답이다.", "두 사람 모두 못한다는 뜻이라 neither A nor B(A도 B도 아닌)로 바꿔 쓰므로 정답이다.", "as well as는 ‘~뿐 아니라 …도’라는 긍정의 뜻이라 맞지 않으므로 오답이다."],
   s=ADD(3, 125, "D", MEMO6 + "neither A nor B를 not ~ A or B로 바꾸는 것은 부정의 범위 문제라 원문항(상관접속사끼리 바꿔 쓰기)과 겨냥이 다르고 오해를 낳았다. ‘A도 B도 못한다’를 Neither A nor B로 바꿔 쓰게 하여 상관접속사의 짝을 직접 묻도록 고쳤다." + pos(4)))

# 3-140 D·F
L(3, 140, "D", p="A: The classroom is so dirty after the party. Let's clean it, (A)_____ we?\nB: OK. (B)_____ don't we start with the windows first?\nA: Good idea. (C)_____ clean they will look after we wash them!")
L(3, 140, "F", p="A: The weather is so nice this evening. Let's take a walk, (A)_____ we?\nB: Sure. (B)_____ about going to the river near our house?\nA: Great. (C)_____ beautiful the sunset is over the water!", why=LEN + SIB)

# 3급 F·D 풀이 순서만 바로잡은 문항(보기·정답은 그대로)
for g_, n_, t_ in [(3, 90, "F"), (3, 99, "F"), (3, 101, "F"), (3, 105, "F"), (3, 109, "F"), (3, 113, "F"), (3, 117, "F"), (3, 122, "F"), (3, 125, "F"), (3, 135, "F"), (3, 139, "F"), (3, 97, "F")]:
    RE(g_, n_, t_, s=ADD(g_, n_, t_, STEP))
