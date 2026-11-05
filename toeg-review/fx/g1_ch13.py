# 1급 CH13 특수 구문 (121~130) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 1-121 동격 that: 줄바꿈 복원
for t in "BCDEF":
    F(1, 121, t, p=V(1, 121, t)["passage"].replace(" / ", "\n"), keepx=True, s="‘/’로 이어 쓴 우리말과 영어 문장을 원문항처럼 두 줄로 나눴다.")

# 1-122 부분부정: 물음표 오답을 ‘All … didn't / Every … isn't’ 혼동 오답으로
R122 = "not all·not every는 ‘모두 ~한 것은 아니다’라는 부분부정, none·no는 ‘아무도(하나도) ~ 않다’라는 전체부정이다. every 뒤에는 단수 명사를 쓰고, 일반동사는 not만으로 부정하지 않는다."
def g122(x):
    if x.startswith("Not every") and x.split()[2].endswith("s"): return "every 뒤에는 단수 명사와 단수 동사를 쓴다. 틀린 형태이다. 오답이다."
    if " all not " in x: return "일반동사는 not만으로 부정하지 않고 do(did) not을 쓴다. 틀린 형태이다. 오답이다."
    if x.startswith("Not "): return "not all/every로 ‘모두 ~한 것은 아니다’라는 부분부정을 바르게 나타냈다. 정답이다."
    if x.startswith(("No all", "No every")): return "no는 all·every 앞에 쓰지 않는다. 틀린 형태이다. 오답이다."
    if x.startswith(("None", "No ")): return "‘아무도(하나도) ~ 않다’는 전체부정이라 우리말과 다르다. 오답이다."
    if "n't" in x: return "all/every … not은 전체부정으로 읽히기 쉬워 부분부정 ‘모두 ~한 것은 아니다’를 분명히 나타내지 못한다. 오답이다."
    return "부정어가 없어 ‘모두 ~했다’는 긍정의 뜻이다. 오답이다."
S122 = "정답과 물음표만 다른 오답이 있어 형식만으로 지워졌다. 물음표 오답을 원문항처럼 형태가 틀린 문장(… all not …, no all, not every + 복수)으로 바꿨다. all/every … not은 부분부정으로도 읽혀 정답이 둘이 될 수 있으므로 쓰지 않았다."
def f122(t, c, a):
    F(1, 122, t, c=c, a=a, r=R122, n=[g122(x) for x in c], s=S122 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f122("B", ["No all applicants passed the interview.", "The applicants all not passed the interview.", "Not all applicants passed the interview.", "None of the applicants passed the interview.", "All applicants passed the interview."], 3)
f122("C", ["Not every book is useful.", "Every book is useful.", "Not every books are useful.", "No every book is useful.", "No book is useful."], 1)
f122("D", ["The employees all not work from home.", "All employees work from home.", "Not all employees work from home.", "None of the employees work from home.", "No all employees work from home."], 3)
f122("E", ["Not every problems are difficult.", "Every problem is difficult.", "No problem is difficult.", "Not every problem is difficult.", "No every problem is difficult."], 4)
f122("F", ["The students all not agreed.", "No all students agreed.", "All students agreed.", "None of the students agreed.", "Not all students agreed."], 5)

# 1-123 상관접속사 수 일치·병렬: 오답을 유형마다 새로, 병렬 구조 오류 포함
R123 = "both A and B는 복수, either/neither A or/nor B·not only A but also B는 B에 수를 맞춘다. 접속사로 연결되는 요소는 같은 형태(명사-명사, 동명사-동명사, 동사-동사)로 병렬한다."
S123 = "오답 네 문장이 B와 똑같고 틀린 문장이 같은 내용의 옳은 문장과 짝을 이뤘다. 원문항처럼 병렬 구조 오류를 넣어 오답을 유형마다 새로 쓰고, B와 짝을 이루던 정답 문장도 바꿨다."
mk(1, 123, "C", [("She likes swimming, dancing, and to sing.", "동명사 둘과 to부정사를 섞어 병렬이 깨졌다. singing으로 써야 한다."), ("Both Tom and his sister is tall.", "both A and B는 복수이므로 are를 써야 한다."),
                 ("He not only plays the guitar but also singing well.", "not only 뒤 동사 plays와 병렬되도록 sings로 써야 한다."), ("Either my friends or my cousin are coming.", "either A or B는 B(my cousin)에 맞춰 is를 써야 한다."),
                 ("Either the students or the teacher has the key.", "either A or B는 B(the teacher)에 맞춰 단수 has를 써서 옳다.")], 5, R123, S123)
mk(1, 123, "D", [("Not only the kids but also their mother enjoys hiking.", "not only A but also B는 B(their mother)에 맞춰 단수 enjoys를 써서 옳다."), ("My hobbies are reading books and to play chess.", "동명사와 to부정사를 섞어 병렬이 깨졌다. playing chess로 써야 한다."),
                 ("Neither Jane nor her friends knows the answer.", "neither A nor B는 B(her friends)에 맞춰 know를 써야 한다."), ("The dog jumped over the fence and running away.", "jumped와 병렬되도록 ran away로 써야 한다."),
                 ("Both reading and to write are important.", "동명사와 to부정사를 섞어 병렬이 깨졌다. writing으로 써야 한다.")], 1, R123, S123)
mk(1, 123, "E", [("Both my parents and my aunt lives in Seoul.", "both A and B는 복수이므로 live를 써야 한다."), ("He likes to cook, to clean, and doing laundry.", "to부정사 둘과 동명사를 섞어 병렬이 깨졌다. to do laundry로 써야 한다."),
                 ("Mina came home, took a shower, and went to bed.", "과거형 동사 세 개를 같은 형태로 병렬해 옳다."), ("Either Tom or his classmates is lying.", "either A or B는 B(his classmates)에 맞춰 are를 써야 한다."),
                 ("Not only he is smart but also kind.", "not only 뒤에 절과 형용사가 병렬되지 않는다. He is not only smart but also kind.로 써야 한다.")], 3, R123, S123)
mk(1, 123, "F", [("Neither the manager nor the workers was happy.", "neither A nor B는 B(the workers)에 맞춰 were를 써야 한다."), ("She danced gracefully and beautiful.", "부사 gracefully와 병렬되도록 beautifully로 써야 한다."),
                 ("Either you or Mina have to go.", "either A or B는 B(Mina)에 맞춰 has를 써야 한다."), ("Jiho is good at not only math but also science.", "not only 명사 but also 명사로 병렬해 옳다."),
                 ("I enjoy hiking more than to swim.", "비교 대상 hiking과 병렬되도록 swimming으로 써야 한다.")], 4, R123, S123)

# 1-124 도치 대화: 줄바꿈 복원
for t in "BCDE":
    F(1, 124, t, p="BR", keepx=True, s="한 줄로 이어 쓴 대화를 원문항처럼 말하는 사람마다 줄을 바꿨다. 밑줄 표현과 정답은 그대로다.")

# 1-125 틀린 문장 개수(2차 감수에서 다시 씀): B 검토 의견(상관접속사의 수 일치라는 취지에서 벗어남) 반영 — 여섯 문장을 모두 주어·동사 수 일치 문장으로
CNT5 = ["1개", "2개", "3개", "4개", "5개"]
R125 = "A as well as B는 A에, either A or B·neither A nor B·not only A but also B는 B에 동사의 수를 맞춘다. both A and B는 복수, every·none of + 셀 수 없는 명사는 단수 동사를 쓴다."
S125 = "병렬·비교 문장이 섞여 있어 이 문항의 취지(상관접속사가 든 주어와 동사의 수 일치)에서 벗어났다(B 검토 의견). 여섯 문장을 모두 수 일치를 묻는 문장으로 바꾸고, 원문항처럼 문장 6개·선택지 1개~5개로 맞췄다."
def f125(t, lines, judge, wrong):
    F(1, 125, t, st="R", p="\n".join(lines), c=CNT5, a=wrong, r=R125, pre=["문장별 판정:"] + judge, k=f"어법상 틀린 문장은 {wrong}개이다.", n="cnt", s=S125 + f" 정답 위치 {'①②③④⑤'[wrong-1]}.")
f125("B", ["A) The teacher as well as the students is ready.", "B) Either Jane or her brothers are coming.", "C) Not only the players but also the coach were excited.", "D) Neither Tom nor his friends knows the answer.",
           "E) Both my father and my mother work at the hospital.", "F) Not every member of the club agrees with the plan."],
     ["A) 옳음: A as well as B는 A(The teacher)에 맞춰 is.", "B) 옳음: either A or B는 B(her brothers)에 맞춰 are.", "C) 틀림: not only A but also B는 B(the coach)에 맞춰 was.", "D) 틀림: neither A nor B는 B(his friends)에 맞춰 know.",
      "E) 옳음: both A and B는 복수라 work.", "F) 옳음: every member는 단수라 agrees."], 2)
f125("C", ["A) Mina as well as her friends is attending.", "B) Either Tom or his parents is responsible.", "C) Neither the manager nor the workers were informed.", "D) Both Jane and her sister likes hiking.",
           "E) Not only the students but also the teacher was surprised.", "F) None of the money were stolen."],
     ["A) 옳음: A as well as B는 A(Mina)에 맞춰 is.", "B) 틀림: either A or B는 B(his parents)에 맞춰 are.", "C) 옳음: neither A nor B는 B(the workers)에 맞춰 were.", "D) 틀림: both A and B는 복수라 like.",
      "E) 옳음: not only A but also B는 B(the teacher)에 맞춰 was.", "F) 틀림: money는 셀 수 없는 명사라 was."], 3)
f125("D", ["A) Mina as well as Tom is joining.", "B) Neither the teachers nor Jane is available.", "C) Not only my uncle but also my cousins lives in Busan.", "D) Either the dog or the cats are making that noise.",
           "E) Both the bus and the subway are crowded.", "F) Not all of the students were present."],
     ["A) 옳음: A as well as B는 A(Mina)에 맞춰 is.", "B) 옳음: neither A nor B는 B(Jane)에 맞춰 is.", "C) 틀림: not only A but also B는 B(my cousins)에 맞춰 live.", "D) 옳음: either A or B는 B(the cats)에 맞춰 are.",
      "E) 옳음: both A and B는 복수라 are.", "F) 옳음: all of the students는 복수라 were."], 1)
f125("E", ["A) The manager as well as the staff members are satisfied.", "B) Either the boys or Tom is responsible.", "C) Neither my parents nor my brother like spicy food.", "D) Not only Sora but also her sisters play the violin.",
           "E) Both the singer and the dancers were nervous.", "F) None of the water was clean."],
     ["A) 틀림: A as well as B는 A(The manager)에 맞춰 is.", "B) 옳음: either A or B는 B(Tom)에 맞춰 is.", "C) 틀림: neither A nor B는 B(my brother)에 맞춰 likes.", "D) 옳음: not only A but also B는 B(her sisters)에 맞춰 play.",
      "E) 옳음: both A and B는 복수라 were.", "F) 옳음: water는 셀 수 없는 명사라 was."], 2)
f125("F", ["A) Leo as well as his teammates is practicing.", "B) Neither Mina nor her parents is here.", "C) Either the coach or the players has the key.", "D) Not only the cats but also the dog were hungry.",
           "E) Both rain and snow are expected tonight.", "F) Every one of the answers are correct."],
     ["A) 옳음: A as well as B는 A(Leo)에 맞춰 is.", "B) 틀림: neither A nor B는 B(her parents)에 맞춰 are.", "C) 틀림: either A or B는 B(the players)에 맞춰 have.", "D) 틀림: not only A but also B는 B(the dog)에 맞춰 was.",
      "E) 옳음: both A and B는 복수라 are.", "F) 틀림: every one은 단수라 is."], 4)

# 1-126 강조의 do: 짝 문장 없애기, 오답을 유형마다 새로
R126 = "긍정문을 강조하는 do/does/did 뒤에는 항상 동사원형을 쓴다. 시제와 3인칭 단수는 do/does/did가 나타내므로 본동사에 -s나 과거형을 다시 붙이지 않는다."
def ok126(x): return "강조의 do/does/did 뒤에 동사원형을 바르게 썼다."
def bad126(fix): return f"강조의 do/does/did 뒤에는 동사원형을 써야 한다. {fix}로 고쳐야 한다."
S126 = "옳은 문장이 같은 내용의 틀린 문장(did submitted ↔ did submit 등)과 짝을 이뤘고 C~F는 오답 네 문장이 B와 똑같았다. 짝을 없애고 오답을 유형마다 새로 썼다."
mk(1, 126, "B", [("My sister does wants a new bike.", bad126("does want")), ("Tom does understands the system.", bad126("does understand")), ("Jane did called me last night.", bad126("did call")),
                 ("Mina did submit the application before the deadline.", ok126("")), ("I do appreciated your help.", bad126("do appreciate"))], 4, R126, "①이 정답 ④와 같은 내용의 틀린 문장(did submitted)이라 대비 단서가 되어 다른 틀린 문장으로 바꿨다.")
mk(1, 126, "C", [("The baby does look like her father.", ok126("")), ("We did finished the project on time.", bad126("did finish")), ("He does has a lot of friends.", bad126("does have")),
                 ("I did saw the movie yesterday.", bad126("did see")), ("She does loves animals.", bad126("does love"))], 1, R126, S126)
mk(1, 126, "D", [("Mom does cooks very well.", bad126("does cook")), ("We do enjoyed the concert.", bad126("did enjoy")), ("He did forgot his homework again.", bad126("did forget")),
                 ("The cat does sleeps all day.", bad126("does sleep")), ("They did win the game in the end.", ok126(""))], 5, R126, S126)
mk(1, 126, "E", [("Dad did fixed the car himself.", bad126("did fix")), ("You do look tired today.", ok126("")), ("My friends does like pizza.", "주어가 복수이므로 do like로 써야 한다."),
                 ("I do believes you.", bad126("do believe")), ("She did bought a new dress.", bad126("did buy"))], 2, R126, S126)
mk(1, 126, "F", [("Sora does writes in her diary every night.", bad126("does write")), ("They do need more time.", ok126("")), ("We did visited Jeju last summer.", bad126("did visit")),
                 ("The teacher do explain things clearly.", "주어가 3인칭 단수이므로 does explain으로 써야 한다."), ("Min did asked a lot of questions.", bad126("did ask"))], 2, R126, S126)

# 1-127 강조구문 연결어: 발문·밑줄을 원문항대로, 오답을 유형마다 새로
R127 = "It is/was + 강조 대상 + that 강조구문에서 that 대신 강조 대상에 맞춰 사람은 who(whom), 사물은 which, 장소는 where, 시간은 when을 쓸 수 있다."
def c127(kind, bad=None, fix=None):
    if bad: return f"강조 대상이 {kind}인데 {bad}를 써서 잘못 연결되었다. {fix}(또는 that)를 써야 한다."
    return {"사람": "사람을 강조하므로 who(whom)를 바르게 썼다.", "사물": "사물을 강조하므로 which를 바르게 썼다.", "장소": "장소를 강조하므로 where를 바르게 썼다.", "시간": "시간을 강조하므로 when을 바르게 썼다."}[kind]
S127 = "발문이 바뀌고 밑줄이 사라졌으며, C~F는 오답 네 문장이 B와 똑같았다. 발문을 원문항과 같게 하고, 원문항처럼 사람·사물·장소·시간 강조 문장의 연결어에 밑줄을 넣어 유형마다 새로 썼다."
mk(1, 127, "B", [("It was Mina <u>who</u> called me.", c127("사람")), ("It was the key <u>which</u> I lost at school.", c127("사물")), ("It was in the library <u>where</u> we studied together.", c127("장소")),
                 ("It was on Monday <u>when</u> the store opened.", c127("시간")), ("It was because of the rain <u>who</u> the match was canceled.", c127("이유(because of the rain)", "사람에게 쓰는 who", "that"))], 5, R127,
   "발문을 원문항과 같게 하고, 원문항처럼 사람·사물·장소·시간 강조 문장을 넣고 연결어에 밑줄을 넣었다.", st="R")
mk(1, 127, "C", [("It was at the station <u>who</u> I met Mina.", c127("장소", "who", "where")), ("It was my grandma <u>who</u> made this cake.", c127("사람")), ("It was the red bag <u>which</u> she wanted.", c127("사물")),
                 ("It was in 2010 <u>when</u> we moved here.", c127("시간")), ("It was at the park <u>where</u> Tom lost his wallet.", c127("장소"))], 1, R127, S127, st="R")
mk(1, 127, "D", [("It was the teacher <u>whom</u> we thanked.", c127("사람")), ("It was Tom <u>when</u> solved the problem.", c127("사람", "when", "who")), ("It was this song <u>which</u> made her famous.", c127("사물")),
                 ("It was in the kitchen <u>where</u> the fire started.", c127("장소")), ("It was last night <u>when</u> I heard the noise.", c127("시간"))], 2, R127, S127, st="R")
mk(1, 127, "E", [("It was yesterday <u>when</u> Jane arrived.", c127("시간")), ("It was my brother <u>who</u> broke the window.", c127("사람")), ("It was in the morning <u>who</u> I jogged.", c127("시간", "who", "when")),
                 ("It was the blue car <u>which</u> I rented.", c127("사물")), ("It was in Busan <u>where</u> they got married.", c127("장소"))], 3, R127, S127, st="R")
mk(1, 127, "F", [("It was at noon <u>when</u> the bell rang.", c127("시간")), ("It was the pizza <u>which</u> the kids loved.", c127("사물")), ("It was at the beach <u>where</u> we found the shell.", c127("장소")),
                 ("It was Leo <u>where</u> won the prize.", c127("사람", "where", "who")), ("It was my aunt <u>who</u> sent me the letter.", c127("사람"))], 4, R127, S127, st="R")

# 1-128 장소 도치·there 구문: 줄바꿈 복원
for t in "BCDF":
    F(1, 128, t, p=V(1, 128, t)["passage"].replace(" / ", "\n"), keepx=True, s="‘/’로 이어 쓴 두 문장을 원문항처럼 ‘-’로 시작하는 두 줄로 나눴다.")

# 1-129 병렬 빈칸: 발문 설명 삭제, 둘째 문장에 not only … but also 복원, 밑줄 빈칸
R129 = "등위접속사로 나열되는 동사는 같은 형태로 병렬한다. It is … not only to부정사 but also to부정사처럼 상관접속사 뒤의 두 요소도 같은 형태로 맞춘다."
UA, UB, UC = "(<u>      A      </u>)", "(<u>      B      </u>)", "(<u>      C      </u>)"
S129 = "발문이 ‘둘째 문장은 to부정사구 두 개를 병렬’이라고 정답을 알려 주었고, 원문항의 not only … but also 구문과 밑줄 빈칸이 빠졌다. 발문을 원문항과 같게 하고 둘째 문장을 It is … not only (B) but also (C) 구조로 되돌렸다."
def f129(t, p, c, a, verbs, s=S129):
    need = [f"(A)는 앞뒤 동사원형({verbs})과 나란히 쓰이므로 동사원형이다.", "(B)는 It is ~ 뒤에서 not only 다음에 오는 진주어이므로 to부정사이다.", "(C)는 but also 뒤에서 (B)와 병렬되므로 to부정사이다."]
    F(1, 129, t, st="R", p=p, c=c, a=a, r=R129, n=tnotes(c, a, need, labs=["(A)", "(B)", "(C)"]), s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f129("B", f"For a successful trip, pack lightly, {UA} ahead, and keep copies of documents. It is also wise not only {UB} your passport but also {UC} your valuables unattended.",
     ["(A) planning - (B) bringing - (C) avoiding leaving", "(A) plan - (B) bring - (C) avoid leaving", "(A) plan - (B) to bring - (C) to avoid leaving", "(A) plan - (B) to bring - (C) avoiding leaving", "(A) to plan - (B) bringing - (C) to avoid leaving"], 3, "pack, keep")
f129("C", f"To save money, you should cook at home, {UA} a budget, and compare prices. It is also helpful not only {UB} your spending but also {UC} impulse buying.",
     ["(A) make - (B) to track - (C) avoiding", "(A) make - (B) to track - (C) to avoid", "(A) making - (B) tracking - (C) avoiding", "(A) to make - (B) tracking - (C) to avoid", "(A) make - (B) track - (C) avoid"], 2, "cook, compare",
     s="글과 정답 조합(exercise - to eat - to avoid)이 원문항과 거의 같아, 돈을 아끼는 상황으로 바꿔 make - to track - to avoid를 정답으로 했다. " + S129)
f129("D", f"To improve your English, you should read daily, {UA} conversations, and review vocabulary. It is also useful not only {UB} every day but also {UC} translating every sentence.",
     ["(A) practice - (B) speak - (C) avoid", "(A) practicing - (B) speaking - (C) avoiding", "(A) to practice - (B) speaking - (C) to avoid", "(A) practice - (B) to speak - (C) to avoid", "(A) practice - (B) to speak - (C) avoiding"], 4, "read, review")
f129("E", f"To work efficiently, set priorities, {UA} distractions, and take breaks. It is also good not only {UB} a schedule but also {UC} multitasking.",
     ["(A) reduce - (B) to follow - (C) avoiding", "(A) reducing - (B) following - (C) avoiding", "(A) reduce - (B) follow - (C) avoid", "(A) to reduce - (B) following - (C) to avoid", "(A) reduce - (B) to follow - (C) to avoid"], 5, "set, take")
f129("F", f"For better sleep, avoid caffeine, {UA} the room dark, and follow a routine. It is also important not only {UB} to bed at the same time but also {UC} your phone late at night.",
     ["(A) keep - (B) to go - (C) to avoid using", "(A) keeping - (B) going - (C) avoiding using", "(A) keep - (B) go - (C) avoid using", "(A) to keep - (B) going - (C) to avoid using", "(A) keep - (B) to go - (C) avoiding using"], 1, "avoid, follow")

# 1-130 병렬구조 원칙 설명: 원문항처럼 그럴듯한 오개념 오답으로, 유형마다 다르게
R130 = "병렬구조는 등위접속사·상관접속사·비교구문으로 연결되는 요소를 문법적으로 대등한 형태와 기능으로 맞추는 원칙이다. 이를 어기면 어법 오류가 된다."
S130 = "오답이 ‘서로 다른 품사를 의도적으로 섞어야 한다’처럼 뻔히 틀렸고 C~F에서 반복되었으며 정답만 길었다. 원문항처럼 A as well as B의 수 일치, not A but B의 형태 허용 같은 그럴듯한 오개념으로 유형마다 새로 쓰고 발문을 원문항과 같게 했다."
mk(1, 130, "B", [("병렬구조는 단어끼리만 적용되고 구·절끼리는 적용되지 않는다.", "구·절끼리도 병렬해야 한다."), ("not only A but also B에서 A가 동사구이면 B는 명사구로 써도 된다.", "A와 B는 같은 형태여야 한다."),
                 ("A as well as B에서는 B에 동사의 수를 맞추는 것이 병렬의 핵심이다.", "A as well as B는 A에 수를 맞추며, 이는 병렬과 다른 수 일치 규칙이다."),
                 ("to부정사를 병렬할 때 반복되는 to를 생략할 수 있지만, 병렬 동명사는 각 동사의 -ing 형태를 유지해야 한다.", "옳은 설명이다."), ("병렬구조는 글을 보기 좋게 하는 장치일 뿐이라 지키지 않아도 문법 오류가 아니다.", "병렬을 어기면 어법 오류가 된다.")], 4, R130, S130, st="R")
mk(1, 130, "C", [("등위접속사나 비교구문으로 연결되는 각 요소는 문법적으로 대등한 형태와 기능을 가져야 한다.", "옳은 설명이다."), ("비교구문 than 뒤에는 앞의 요소와 형태가 달라도 뜻만 같으면 된다.", "비교 대상도 문법적으로 대등해야 한다."),
                 ("either A or B에서는 A와 B 중 먼저 나온 쪽에 동사의 수를 맞춘다.", "either A or B는 동사와 가까운 B에 수를 맞춘다."), ("병렬구조는 and에만 적용되고 or·but에는 적용되지 않는다.", "or·but으로 연결할 때도 병렬해야 한다."),
                 ("세 개 이상을 나열할 때는 마지막 요소만 형태를 바꿔 강조할 수 있다.", "나열되는 요소는 모두 같은 형태로 맞춘다.")], 1, R130, S130, st="R")
mk(1, 130, "D", [("상관접속사 both A and B에서 A와 B는 품사가 달라도 된다.", "A와 B는 같은 품사·형태여야 한다."), ("not A but B에서 A가 to부정사이면 B는 동명사로 쓰는 것이 원칙이다.", "A가 to부정사이면 B도 to부정사로 맞춘다."),
                 ("병렬구조에서는 각 요소가 해당 자리에서 허용되고 기능·의미가 대응해야 하며, 같은 형태로 맞추면 문장이 명료해진다.", "옳은 설명이다."), ("neither A nor B는 병렬구조가 아니므로 A와 B의 형태를 맞출 필요가 없다.", "neither A nor B도 병렬구조라 형태를 맞춘다."),
                 ("and 뒤의 요소는 앞의 요소보다 짧아야 병렬이 성립한다.", "길이가 아니라 문법 형태와 기능이 대등해야 한다.")], 3, R130, S130, st="R")
mk(1, 130, "E", [("비교구문은 병렬구조와 관계없으므로 비교 대상의 형태는 자유롭다.", "비교 대상도 대등한 형태로 맞춘다."), ("to부정사 병렬에서 두 번째 to는 반드시 반복해 써야 한다.", "반복되는 to는 생략할 수 있다."),
                 ("동명사와 to부정사는 뜻이 같으므로 and로 섞어 연결해도 된다.", "같은 형태로 맞춰야 하므로 섞어 쓰지 않는다."), ("not only A but also B에서 also는 반드시 생략해야 병렬이 된다.", "also는 생략할 수 있을 뿐, 병렬 여부와 관계없다."),
                 ("than이나 as ~ as 뒤의 비교 대상은 앞의 요소와 문법적으로 대등해야 한다.", "옳은 설명이다.")], 5, R130, S130, st="R")
mk(1, 130, "F", [("병렬구조는 명사와 명사 사이에서만 성립한다.", "동사·형용사·구·절 사이에서도 성립한다."), ("or로 연결된 요소 중 하나는 반드시 동명사여야 한다.", "or로 연결된 요소도 서로 같은 형태로 맞출 뿐 특정 형태를 요구하지 않는다."),
                 ("and·or·but으로 세 요소 이상을 연결할 때도 각 요소의 기능이 대응해야 하며, 일관된 형태로 쓰는 것이 원칙이다.", "옳은 설명이다."), ("병렬구조를 어기는 것은 문체의 문제일 뿐 어법 오류로 보지 않는다.", "병렬을 어기면 어법 오류가 된다."),
                 ("but 뒤에는 앞과 반대 뜻이 오므로 형태도 반대로 바꿔야 한다.", "뜻이 반대여도 형태는 같게 맞춘다.")], 3, R130, S130, st="R")


# ---- 2차 감수(2026-10) 추가 ----
# 1-123 B: 원문항의 병렬 구조 오류가 빠지고 수 일치만 남음
mk(1, 123, "B", [("She enjoys cooking, baking, and to decorate cakes.", "동명사 둘과 to부정사를 섞어 병렬이 깨졌다. decorating으로 써야 한다."), ("Both the coach and the players is ready.", "both A and B는 복수이므로 are를 써야 한다."),
                 ("He not only wrote the song but also singing it.", "not only 뒤 동사 wrote와 병렬되도록 sang으로 써야 한다."), ("Either the teachers or Tom are responsible.", "either A or B는 B(Tom)에 맞춰 is를 써야 한다."),
                 ("Neither the students nor the teacher was informed.", "neither A nor B는 B(the teacher)에 맞춰 단수 was를 써서 옳다.")], 5, R123,
   "원문항은 병렬 구조 오류(Both to read and writing 등)와 수 일치를 함께 묻는데, 변형은 다섯 문장이 모두 수 일치뿐이었고 Neither … nor 문장이 틀린 형태(①)와 옳은 형태(⑤)로 함께 나왔다. 원문항처럼 병렬 구조 오류 문장 둘을 넣었다.")

# 1-124 F: 틀린 표현이 원문항(hardly I can believe my eyes)과 거의 같음
F(1, 124, "F", p="A: ①<u>I have never seen such a long line</u>.\nB: ②<u>Neither have I</u>. ③<u>Here comes another bus</u>.\nA: ④<u>Rarely I have waited this long</u>.\nB: ⑤<u>So crowded is the street</u> that traffic has stopped.",
  c=["I have never seen such a long line", "Neither have I", "Here comes another bus", "Rarely I have waited this long", "So crowded is the street"], a=4, okdup=True,
  r="never, rarely, seldom, hardly 같은 부정어가 문장 맨 앞에 오면 ‘부정어 + 조동사 + 주어’로 도치한다. Neither + 조동사 + 주어, Here + 동사 + 주어, So + 형용사 + 동사 + 주어도 도치 구문이다.",
  n=["부정어 never가 문장 가운데 있어 도치하지 않는다. 올바르므로 오답이다.", "Neither + have + I로 바르게 도치했다. 오답이다.", "Here + comes + 주어로 바르게 도치했다. 오답이다.",
     "부정어 Rarely가 문장 맨 앞에 왔으므로 Rarely have I waited로 도치해야 한다. 정답이다.", "So + 형용사 + 동사 + 주어로 바르게 도치했다. 오답이다."],
  s="④ ‘Hardly I can believe this’가 원문항의 틀린 표현(hardly I can believe my eyes)과 거의 같아 ‘Rarely I have waited this long’으로 바꿨다. 한 줄로 이어 쓴 대화도 말하는 사람마다 줄을 바꿨다.")

# 1-128 E: 줄바꿈 복원, 없는 형태(ares) 오답 교체
F(1, 128, "E", p=V(1, 128, "E")["passage"].replace(" / ", "\n"), c=["stands - is", "are - are", "is - are", "is - is", "are - is"], a=3,
  r="장소의 부사구가 문장 앞에 오면 ‘부사구 + 동사 + 주어’로 도치하고, 동사는 뒤에 오는 주어에 수를 맞춘다. There is/are도 뒤의 주어에 수를 맞춘다.",
  n=["several cars는 복수라 둘째 빈칸에 is를 쓸 수 없으므로 오답이다.", "a small cafe는 단수라 첫째 빈칸에 are를 쓸 수 없으므로 오답이다.", "a small cafe는 단수라 is, several cars는 복수라 are가 알맞으므로 정답이다.",
     "several cars는 복수라 둘째 빈칸에 is를 쓸 수 없으므로 오답이다.", "두 빈칸의 수가 서로 바뀌었으므로 오답이다."],
  s="‘/’로 이어 쓴 두 문장을 원문항처럼 두 줄로 나누고, 영어에 없는 형태인 오답 ⑤ ‘is - ares’를 ‘are - is’로 바꿨다. 정답은 그대로 ③.")
