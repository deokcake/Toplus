# 2026-10-06 B유형 감수 메모 반영 — 1급
# 1-38 두 문장을 ‘문장 → 바꾼 문장’으로, B·E 제시문 늘림
def f38m(t, act, pas, s):
    RE(1, 38, t, p=f"{act}\n→ {pas}", s=s)
_B38 = "(<u>        </u>)"
f38m("B", "The teacher sent Jane a certificate for her perfect attendance.", f"The certificate {_B38} for her perfect attendance by the teacher.",
     MEMO + "원문항보다 짧던 제시문에 for her perfect attendance를 더해 길이를 맞추고, 앞 문장을 뒷 문장으로 바꾼다는 뜻이 드러나게 둘째 문장 앞에 ‘→’를 붙였다. 보기와 정답은 그대로다(③).")
f38m("C", "The university offered Mina a scholarship for academic excellence.", f"The scholarship {_B38} for academic excellence by the university.", MEMO + "둘째 문장 앞에 ‘→’를 붙여 능동문을 수동문으로 바꾼다는 뜻이 드러나게 했다. 보기와 정답은 그대로다(①).")
f38m("D", "The company gave Tom an award for his service.", f"The award {_B38} for his service by the company.", MEMO + "둘째 문장 앞에 ‘→’를 붙여 능동문을 수동문으로 바꾼다는 뜻이 드러나게 했다. 보기와 정답은 그대로다(⑤).")
f38m("E", "The museum showed us a rare painting from the Joseon period.", f"The rare painting from the Joseon period {_B38} by the museum.",
     MEMO + "원문항보다 짧던 제시문에 from the Joseon period를 더해 길이를 맞추고, 둘째 문장 앞에 ‘→’를 붙였다. 보기와 정답은 그대로다(②).")
f38m("F", "The committee granted Leo permission to enter the lab.", f"Permission {_B38} to enter the lab by the committee.", MEMO + "둘째 문장 앞에 ‘→’를 붙여 능동문을 수동문으로 바꾼다는 뜻이 드러나게 했다. 보기와 정답은 그대로다(④).")

# 1-47 문맥상 답이 될 수 있던 To be brief 를 모든 유형에서 뺌
_M47 = {"To begin with": "‘우선’은 여러 가지를 차례로 말할 때 쓰므로", "Strange to say": "‘이상한 말이지만’은 뜻밖의 일을 말할 때 쓰므로", "Needless to say": "‘말할 필요도 없이’는 당연한 결과를 말할 때 쓰므로",
        "So to speak": "‘말하자면’은 다른 것에 빗대어 말할 때 쓰므로", "Speaking of which": "‘말이 나왔으니 말인데’는 화제를 이어 갈 때 쓰므로", "To make matters worse": "‘설상가상으로’는 나쁜 일이 겹칠 때 쓰므로",
        "To be honest": "‘솔직히 말해서’는 듣기 좋지 않을 속마음을 말할 때 쓰므로", "To be brief": "‘간단히 말해서’는 앞의 내용을 줄여 말할 때 쓰므로"}
def f47m(t, c, a, right, s):
    n = [(right if i + 1 == a else _M47[x[0].upper() + x[1:]] + " 오답이다.") for i, x in enumerate(c)]
    RE(1, 47, t, c=c, a=a, n=n, s=s)
f47m("B", ["To begin with", "Strange to say", "Needless to say", "So to speak", "Speaking of which"], 3, "35도가 넘는 날 마라톤을 했으니 지친 것은 당연한 결과라 ‘말할 필요도 없이’가 알맞으므로 정답이다.",
     MEMO + "‘간단히 말해서, 완전히 지쳤다’로도 읽혀 답이 될 수 있던 ④ To be brief를 So to speak로 바꿨다. 정답 위치 ③.")
f47m("C", ["To make matters worse", "To begin with", "Strange to say", "So to speak", "Needless to say"], 2, "가기 싫은 이유를 하나 말한 뒤 Also로 또 하나를 덧붙이므로 ‘우선’이 알맞으므로 정답이다.",
     MEMO + "B처럼 ‘간단히 말해서’로 읽어도 어색하지 않던 ⑤ To be brief를 Needless to say로 바꿨다. 정답 위치 ②.")
f47m("D", ["To begin with", "Needless to say", "Strange to say", "To make matters worse", "So to speak"], 3, "잃어버린 고양이가 사흘 뒤 제 발로 돌아온 뜻밖의 일이라 ‘이상한 말이지만’이 알맞으므로 정답이다.",
     MEMO + "B처럼 문맥상 답이 될 수 있던 ⑤ To be brief를 So to speak로 바꿨다. 정답 위치 ③.")
f47m("E", ["To make matters worse", "So to speak", "To begin with", "Strange to say", "To be honest"], 5, "듣기 좋지 않을 속마음을 말하므로 ‘솔직히 말해서’가 알맞으므로 정답이다.",
     MEMO + "‘말할 필요도 없이 긴 머리가 더 좋았다’로도 읽힐 수 있던 ② Needless to say를 So to speak로 바꿨다. 정답 위치 ⑤.")
f47m("F", ["to begin with", "strange to say", "to be brief", "so to speak", "to make matters worse"], 4, "삼촌을 실제 사전이 아니라 ‘걸어 다니는 사전’에 빗대어 말하므로 ‘말하자면’이 알맞으므로 정답이다.",
     MEMO + "문장 끝에 붙여도 뜻이 통하던 ③ needless to say를 to be brief로 바꿨다. 정답 위치 ④.")

# 1-56 발문 조건을 ‘단어의 형태는 필요에 따라 바꿀 수 있다’로(원문항과 같게)
ST56 = "다음 중 주어진 단어를 활용하여 우리말 문장에 맞도록 영작한 것을 고르시오. (단, 단어의 형태는 필요에 따라 바꿀 수 있다.)"
for _t in "BCDEF":
    RE(1, 56, _t, st=ST56, s=OLD(1, 56, _t).get("s", "") + " " + MEMO + "‘한 단어의 형태를 바꾸어’라는 조건과 달리 두 단어의 형태가 바뀐 보기가 있어, 원문항과 함께 조건을 ‘단어의 형태는 필요에 따라 바꿀 수 있다’로 고쳤다.")

# 1-58 모든 보기에 바뀐 형태가 정확히 하나씩 있게
def f58m(t, c, a, n, s):
    RE(1, 58, t, c=c, a=a, n=[x + OK(i + 1, a) for i, x in enumerate(n)], s=s)
_S58 = MEMO + "조건(한 단어의 형태를 바꾸어)과 달리 바뀐 형태가 없던 보기를, 동사의 형태를 바꾼 오답으로 고쳤다. 정답은 그대로다."
f58m("B", ["The mask prevents dust enters from the nose.", "The mask prevents from entering dust the nose.", "The mask prevents dust from enters the nose.", "The mask prevents dust from entering the nose.", "The mask prevents the nose from entering dust."], 4,
     ["from이 동사 뒤에 왔고 enter를 enters로 바꿔 동명사도 아니므로", "목적어 dust가 from entering 뒤로 가서 어순이 틀렸으므로", "from 뒤에는 동명사 entering을 써야 하는데 3인칭 단수형 enters를 썼으므로", "prevent + dust + from + entering의 어순과 형태가 바르므로", "the nose와 dust의 자리가 바뀌어 ‘코가 먼지에 들어간다’는 뜻이 되므로"], _S58 + pos(4))
f58m("C", ["The teacher prevents students from using phones.", "The teacher prevents students uses from phones.", "The teacher prevents from using students phones.", "The teacher prevents students from uses phones.", "The teacher prevents phones from using students."], 1,
     ["prevent + students + from + using의 어순과 형태가 바르므로", "from이 동사 뒤에 왔고 use를 uses로 바꿔 동명사도 아니므로", "목적어 students가 from using 뒤로 가서 어순이 틀렸으므로", "from 뒤에는 동명사 using을 써야 하는데 3인칭 단수형 uses를 썼으므로", "phones와 students의 자리가 바뀌어 뜻이 맞지 않으므로"], _S58 + pos(1))
f58m("D", ["The rule prevents people parks from here.", "The rule prevents from parking people here.", "The rule prevents people from parking here.", "The rule prevents people from parks here.", "The rule prevents here from parking people."], 3,
     ["from이 동사 뒤에 왔고 park를 parks로 바꿔 동명사도 아니므로", "목적어 people이 from parking 뒤로 가서 어순이 틀렸으므로", "prevent + people + from + parking의 어순과 형태가 바르므로", "from 뒤에는 동명사 parking을 써야 하는데 3인칭 단수형 parks를 썼으므로", "here와 people의 자리가 바뀌어 뜻이 맞지 않으므로"], _S58 + pos(3))
f58m("E", ["The rain prevented us goes from outside.", "The rain prevented from going us outside.", "The rain prevented us from went outside.", "The rain prevented outside from going us.", "The rain prevented us from going outside."], 5,
     ["from이 동사 뒤에 왔고 go를 goes로 바꿔 동명사도 아니므로", "목적어 us가 from going 뒤로 가서 어순이 틀렸으므로", "from 뒤에는 동명사 going을 써야 하는데 과거형 went를 썼으므로", "outside와 us의 자리가 바뀌어 뜻이 맞지 않으므로", "prevent + us + from + going의 어순과 형태가 바르므로"], _S58 + pos(5))
f58m("F", ["The gate prevents children runs from onto the road.", "The gate prevents children from running onto the road.", "The gate prevents from running children onto the road.", "The gate prevents children from ran onto the road.", "The gate prevents children running from onto the road."], 2,
     ["from이 동사 뒤에 왔고 run을 runs로 바꿔 동명사도 아니므로", "prevent + children + from + running의 어순과 형태가 바르므로", "목적어 children이 from running 뒤로 가서 어순이 틀렸으므로", "from 뒤에는 동명사 running을 써야 하는데 과거형 ran을 썼으므로", "from이 running 뒤에 와서 어순이 틀렸으므로"], _S58 + pos(2))

# 1-65 문장 길이를 원문항 수준으로
_L65 = MEMO + "원문항보다 짧던 문장을 원문항 길이로 늘렸다. 분사의 옳고 틀림과 정답은 그대로다."
RE(1, 65, "B", p="\n".join(["a) Not having enough money for the concert ticket, Leo stayed home that night.", "b) Having selected for the national team, Mina celebrated with her family.", "c) I heard the baby crying loudly in the next room.",
                            "d) With the front door locked, we felt safe in the old house.", "e) All things considered, the new plan is reasonable and realistic.", "f) Driving to work in the morning, the traffic jam annoyed me."]),
   pre=["문장별 판정:", "a) 옳음: 부정 분사구문 Not having이 주어 Leo와 맞다.", "b) 틀림: Mina가 뽑힌 것이므로 Having been selected가 되어야 한다.", "c) 옳음: 지각동사 heard + 목적어 + 현재분사이다.", "d) 옳음: 문이 잠긴 것이므로 with + 명사 + 과거분사이다.",
        "e) 옳음: All things considered는 관용 표현이다.", "f) 틀림: Driving의 주어가 the traffic jam이 되어 맞지 않는다."], s=_L65 + " (b, f가 틀려 옳은 문장은 4개, ③)")
RE(1, 65, "D", p="\n".join(["a) Being tired after the long trip, Jane went home early.", "b) Having finished the report, Mina emailed it to her boss.", "c) We saw the dog running away across the field.", "d) With the window break, the room became cold at night.",
                            "e) Time permitting, we will visit the science museum.", "f) Walking downtown, Tom saw an old friend from school."]), s=_L65 + " 개수 선택지는 2개~6개 순으로 정렬했다(정답 5개, ④).")
RE(1, 65, "E", p="\n".join(["a) Feeling sick after lunch, Tom rested at home all afternoon.", "b) Having lost her key on the bus, Jane called a locksmith.", "c) We saw the children played in the park near our house.", "d) With the task completed, everyone relaxed on the sofa.",
                            "e) Weather permit, we will hike up the mountain tomorrow.", "f) Walking to school, a rainbow appeared in the sky."]), s=_L65 + " (c, e, f가 틀려 옳은 문장은 3개, ②)")
RE(1, 65, "F", p="\n".join(["a) Not understanding the question, I asked the teacher again.", "b) Having been invited to the party, Leo attended with his sister.", "c) I watched the sun setting slowly behind the hills.", "d) With the lights turned off, the room was completely dark.",
                            "e) Time permitting, we will continue the discussion tomorrow.", "f) Running to the bus stop, the bus left without me."]), s=_L65 + " (f만 틀려 옳은 문장은 5개, ④)")

# 1-70 <조건> 없이 ‘분사구문의 쓰임이 어법상 옳은 문장’을 고르는 발문으로(원문항과 같게)
ST70 = "다음 중 분사구문의 쓰임이 어법상 옳은 문장을 고르시오."
R70m = "주절과 주어가 다른 분사구문(독립분사구문)은 의미상 주어를 분사 앞에 밝혀 쓴다. 완료형은 having + 과거분사, 완료 수동은 having been + 과거분사이며, 분사구문 뒤에 so 같은 접속사를 붙이지 않는다."
_S70 = MEMO + "<조건>이 너무 단순해, 원문항과 함께 조건 없이 분사구문이 어법상 옳은 문장을 고르는 발문으로 바꾸고 <조건>을 지웠다. 보기와 정답은 그대로다."
RE(1, 70, "B", st=ST70, p="", r=R70m, a=5, c=OLD(1, 70, "B").get("c") or V(1, 70, "B")["c"],
   n=["Having 뒤에는 과거분사 finished를 써야 하는데 finish를 썼으므로 오답이다.", "be over(끝나다)이므로 The meeting being over가 되어야 하는데 having over라고 썼으므로 오답이다.", "분사구문 뒤에 접속사 so를 붙였으므로 오답이다.",
      "There being no seats가 되어야 하는데 having을 썼으므로 오답이다.", "주절의 주어 dinner와 다른 All the guests를 밝히고 완료의 분사 having arrived를 바르게 썼으므로 정답이다."], s=_S70 + pos(5))
for _t in "CDEF":
    _o = OLD(1, 70, _t)
    RE(1, 70, _t, st=ST70, p="", r=R70m, n=[x.replace(" 두 조건을 모두 만족하므로 정답이다.", " 분사구문의 쓰임이 바르므로 정답이다.") for x in _o["n"]], s=_S70 + pos(_o["a"]))

# 1-77 지문을 원문항 길이로
_S77 = MEMO + "원문항보다 짧던 지문을 원문항 길이로 늘렸다. 수치·질문·보기·정답은 그대로다."
RE(1, 77, "B", p="Four cars are being compared over the same 100 km road. Car A uses 5 L of fuel, so it is the most economical of the four. Car B uses twice as much fuel as Car A. Car C uses 7 L of fuel, which is more than Car A but less than Car B. Car D uses less fuel than Car C but more than Car A.\n질문: Which car uses more fuel than Car C?", s=_S77 + pos(2))
RE(1, 77, "C", p="Four laptops are being compared at the store. Model A weighs 1.2 kg and is the lightest of the four. Model B is twice as heavy as Model A. Model C weighs 1.5 kg, which is heavier than Model A but lighter than Model B. Model D is lighter than Model C but heavier than Model A.\n질문: Which laptop is heavier than Model C?", s=_S77 + pos(3))
RE(1, 77, "D", p="Four runners finished the same 100-meter race yesterday. Mina finished in 12 seconds and won the race. Jane finished in 13 seconds, and Leo finished in 15 seconds. Tom ran faster than Jane but slower than Mina, so he came in second.\n질문: Who ran slower than Jane?", s=_S77 + pos(4))
RE(1, 77, "E", p="Four water bottles are being compared in the shop. Bottle A holds 500 mL and is the smallest of the four. Bottle B holds twice as much water as Bottle A. Bottle C holds 750 mL, which is more than Bottle A but less than Bottle B. Bottle D holds less than Bottle C but more than Bottle A.\n질문: Which bottle holds more than Bottle C?", s=_S77 + pos(5))
RE(1, 77, "F", p="Four rooms in the new building are being compared. Room A is 20 m² and is the smallest of the four. Room B is 1.5 times as large as Room A. Room C is 25 m², which is larger than Room A but smaller than Room B. Room D is smaller than Room C but larger than Room A.\n질문: Which room is larger than Room C?", s=_S77 + pos(1))

# 1-85 예문을 원문항 길이로(밑줄·판정·정답 그대로)
_S85 = MEMO + "원문항보다 짧던 예문을 원문항 길이로 늘렸다. 밑줄 친 관계사와 판정, 정답은 그대로다."
RE(1, 85, "B", p="\n".join(["a) <u>Whatever</u> she says about the plan, I will listen carefully.", "b) This is the reason for <u>that</u> he resigned from the company last month.", "c) <u>Whoever</u> wins the final game will receive a special prize.",
                            "d) Pick <u>whichever</u> color you like for your new room.", "e) The thing <u>what</u> happened at the meeting was unexpected.", "f) We will hire <u>whoever</u> is qualified for the position."]), s=_S85 + pos(2))
RE(1, 85, "C", p="\n".join(["a) <u>Whatever</u> you decide about the trip, I will support you.", "b) This is the room in <u>that</u> we met for the first time.", "c) <u>Whoever</u> calls while I am out, tell them I am busy.",
                            "d) Take <u>whichever</u> seat is available near the window.", "e) <u>What</u> he said at the party surprised everyone.", "f) <u>Whichever</u> team wins the match, we will celebrate together."]), s=_S85 + pos(1))
RE(1, 85, "D", p="\n".join(["a) <u>Whoever</u> finishes the test first may leave the room.", "b) This is the small town <u>which</u> Mina was born in 2010.", "c) <u>Whatever</u> happens during the storm, stay calm and wait inside.",
                            "d) Choose <u>whichever</u> option you prefer for the project.", "e) <u>That</u> Tom needs after the long trip is some rest.", "f) I can't find the key <u>what</u> I put on the kitchen table."]), s=_S85 + pos(3))
RE(1, 85, "E", p="\n".join(["a) <u>Whoever</u> arrives early can help set up the tables.", "b) This is the desk <u>which</u> I left my bag this morning.", "c) <u>Whatever</u> you choose from the menu is fine with me.",
                            "d) Use <u>whichever</u> tool works best for the job.", "e) <u>What</u> matters most in this class is effort.", "f) The man <u>who</u> car was stolen called the police right away."]), s=_S85 + pos(2))
RE(1, 85, "F", p="\n".join(["a) <u>Whatever</u> the result is, we will continue the project.", "b) This is the city in <u>that</u> he lives with his family.", "c) <u>Whoever</u> told you that story was wrong.",
                            "d) Choose <u>whichever</u> route is shorter to the station.", "e) <u>What</u> she bought at the mall was quite expensive.", "f) She lives in a house <u>whose</u> roof is painted red."]), s=_S85 + pos(1))

# 1-87 <보기> 낱말 순서를 섞음(제시 순서대로 읽으면 답이 되던 것)
def f87m(t, rows, s):
    old = OLD(1, 87, t); blanks = old["p"].split("\n")[-1]
    RE(1, 87, t, p="<보기>\n" + "\n".join(rows) + "\n" + blanks, s=s)
_S87 = MEMO + "<보기>의 낱말이 완성 문장의 순서대로 놓여 있어 그대로 읽으면 답이 되었다. 낱말 순서를 섞었다. 정답은 그대로다."
f87m("B", ["interesting / Mina / that / the", "is / bought / book"], _S87 + pos(3))
f87m("C", ["whose / a / friend / met / boy", "she / is / my / sister"], _S87 + pos(5))
f87m("D", ["found / the / who / dog", "they / their / man / thanked"], _S87 + pos(2))
f87m("E", ["where / the / met / he", "they / showed / cafe / me"], _S87 + pos(4))
f87m("F", ["rainy / when / arrived / the", "was / Tom / day"], _S87 + pos(1))

# 1-90 지문을 원문항 길이로(밑줄 표현·보기·정답 그대로)
_S90 = MEMO + "원문항보다 짧던 지문을 원문항 길이로 늘렸다. 밑줄 표현·보기·정답은 그대로다."
F(1, 90, "B", p="Mina volunteers at a community center ①<u>which</u> supports children from low-income families. Every Saturday, she helps ②<u>whoever</u> needs assistance with homework or reading. The room ③<u>where</u> she teaches is bright and full of books. She still remembers the day ④<u>when</u> she began volunteering two years ago. The old shelf ⑤<u>on that</u> she keeps the children's books is always full.", s=_S90 + pos(5))
F(1, 90, "C", p="Mina works at a design company ①<u>which</u> has offices in more than ten countries. She can choose ②<u>whatever</u> project interests her the most each season. The office ③<u>where</u> she works is located downtown near the river. She clearly remembers the day ④<u>when</u> she started her first project there. Her desk is beside a sunny windowsill ⑤<u>on that</u> she keeps several small plants.", s=_S90 + pos(5))
F(1, 90, "D", p="Tom lives in a quiet town ①<u>where</u> many young artists live and work. He knows ②<u>whoever</u> runs the local gallery on Main Street. The studio ③<u>which</u> he rents above the bakery is small but bright. He often remembers the year ④<u>when</u> he first moved there with his dog. The wooden table ⑤<u>on that</u> he paints every morning is very old.", s=_S90 + pos(5))
F(1, 90, "E", p="Jane studies at a university ①<u>which</u> has one of the most famous libraries in the country. In her free time, she reads ②<u>whatever</u> she can find about ancient history. The reading room ③<u>where</u> she studies every evening is quiet and warm. She remembers the day ④<u>when</u> her first classes began last spring. The desk ⑤<u>at that</u> she usually sits is near the big window by the door.", s=_S90 + pos(5))
F(1, 90, "F", p="Leo works in a research lab ①<u>where</u> new building materials are tested every day. He uses ②<u>whichever</u> tool is available when he starts an experiment. The equipment ③<u>which</u> he needs for his work is very expensive. He still remembers the month ④<u>when</u> he joined the team three years ago. The long bench ⑤<u>on that</u> he works with his colleagues is large and clean.", s=_S90 + pos(5))

# 1-94 대화를 원문항 길이로(밑줄 표현·보기·정답 그대로)
_S94 = MEMO + "원문항보다 짧던 대화에 말을 더해 길이를 맞추고, 말하는 사람마다 줄을 바꿨다. 밑줄 표현·보기·정답은 그대로다."
RE(1, 94, "B", p="Leo: ①<u>If I had saved the file</u>, ②<u>I would not lose my work last night</u>. I had to type the whole report again.\nTom: That sounds terrible. ③<u>If you had backed it up</u>, ④<u>you would have been safe</u>.\nLeo: I know. ⑤<u>I wish I had remembered</u>. I will never make the same mistake again.", s=_S94 + pos(2))
RE(1, 94, "C", p="Mina: ①<u>If I had left home earlier</u>, ②<u>I would catch the train yesterday</u>. I was late for the meeting.\nLeo: That's too bad. ③<u>If you had checked the schedule</u>, ④<u>you would have known the time</u>.\nMina: I know. ⑤<u>I wish I had been more careful</u>. Next time I will set an alarm.", s=_S94 + pos(2))
RE(1, 94, "D", p="Tom: ①<u>If I had practiced more</u>, ②<u>I would win the match last week</u>. I lost in the final set.\nJane: Don't be too hard on yourself. ③<u>If you had trained regularly</u>, ④<u>you would have improved</u>.\nTom: You're right. ⑤<u>I wish I had listened</u> to my coach's advice.", s=_S94 + pos(2))
RE(1, 94, "E", p="Jane: ①<u>If I had brought my umbrella</u>, ②<u>I would not get wet yesterday</u>. I caught a cold because of the rain.\nMina: Oh no. ③<u>If you had read the forecast</u>, ④<u>you would have prepared</u> for it.\nJane: I know. ⑤<u>I wish I had checked it</u> before I left home.", s=_S94 + pos(2))
RE(1, 94, "F", p="Mina: ①<u>If I had studied harder</u>, ②<u>I would pass the test yesterday</u>. I missed the passing score by two points.\nJane: I'm sorry to hear that. ③<u>If you had reviewed the notes</u>, ④<u>you would have done better</u>.\nMina: You're right. ⑤<u>I wish I had prepared more</u> for it.", s=_S94 + pos(2))

# 1-98 오답을 주어진 낱말만으로 만든 어순 오류로
_K98 = {"OK": "if + had + 과거분사(과거 조건), would + 동사원형 + now(현재 결과)의 혼합가정법을 바르게 배열했으므로 정답이다.", "HAD": "if절은 If + 주어 + had 순서인데 had가 주어 앞에 왔으므로 오답이다.",
        "MID": "if의 위치가 틀려 조건절과 주절이 뒤바뀌었으므로 오답이다.", "Q": "주절이 의문문 어순(would + 주어)이 되었으므로 오답이다.", "END": "if가 조건절 끝에 붙어 있고 Had로 시작하는 도치와 if를 겹쳐 썼으므로 오답이다."}
def f98m(t, c, kinds, s):
    a = kinds.index("OK") + 1
    RE(1, 98, t, c=c, a=a, n=[_K98[k] for k in kinds], s=s + pos(a))
_S98 = MEMO + "주어진 낱말에 없는 have·worked를 쓰거나 낱말을 빼고 만든 오답을, 주어진 낱말만으로 if·had의 자리나 주절의 어순이 틀린 오답으로 바꿨다."
f98m("B", ["If Jane had studied engineering, she would work at this company now.", "If had Jane studied engineering, she would work at this company now.", "Jane had studied engineering if she would work at this company now.", "If Jane had studied engineering, would she work at this company now.", "Had Jane studied engineering if, she would work at this company now."], ["OK", "HAD", "MID", "Q", "END"], _S98)
f98m("C", ["Mina had accepted the job if she would be living abroad now.", "If had Mina accepted the job, she would be living abroad now.", "If Mina had accepted the job, would she be living abroad now.", "If Mina had accepted the job, she would be living abroad now.", "Accepted Mina the job if had, she would be living abroad now."], ["MID", "HAD", "Q", "OK", "END"], _S98)
f98m("D", ["If had Tom saved more money, he would own a car now.", "Tom had saved more money if he would own a car now.", "If Tom had saved more money, he would own a car now.", "If Tom had saved more money, would he own a car now.", "Had saved Tom more money if, he would own a car now."], ["HAD", "MID", "OK", "Q", "END"], _S98)
f98m("E", ["If we had chosen the other route, would we be there now.", "If we had chosen the other route, we would be there now.", "We had chosen the other route if we would be there now.", "If had we chosen the other route, we would be there now.", "Had chosen we the other route if, we would be there now."], ["Q", "OK", "MID", "HAD", "END"], _S98)
f98m("F", ["If had Leo moved to Seoul, he would live near us now.", "If Leo had moved to Seoul, would he live near us now.", "Leo had moved to Seoul if he would live near us now.", "Moved Leo to Seoul if had, he would live near us now.", "If Leo had moved to Seoul, he would live near us now."], ["HAD", "Q", "MID", "END", "OK"], _S98)

# 1-107 제시 낱말 순서를 섞음
_S107 = MEMO + "주어진 낱말이 정답 문장의 순서대로 놓여 있어 그대로 읽으면 답이 되었다. 낱말 순서를 섞었다. 보기와 정답은 그대로다."
RE(1, 107, "B", p="(not / the / so / whispered / baby / up / that / we / would / wake / .)", s=_S107 + pos(4))
RE(1, 107, "C", p="(miss / so / she / the / a / would / that / took / train / she / not / taxi / .)", s=_S107 + pos(1))
RE(1, 107, "D", p="(could / so / a / Tom / that / laptop / buy / money / he / saved / .)", s=_S107 + pos(3))
RE(1, 107, "E", p="(that / forget / Mina / down / so / not / it / would / wrote / she / .)", s=_S107 + pos(5))
RE(1, 107, "F", p="(so / avoid / they / early / that / could / traffic / left / they / .)", s=_S107 + pos(2))

# 1-115 문장을 원문항 길이로(판정·보기·정답 그대로)
_S115 = MEMO + "원문항보다 짧던 문장을 원문항 길이로 늘렸다. 판정·보기·정답은 그대로다."
RE(1, 115, "B", p="\n".join(["A) The young often adapt quickly to new technology and social change.", "B) Jane said she had lost the key to her apartment on the way home.", "C) Tom asked when the meeting would start the next morning.",
                             "D) Each of the students have a locker in the hallway near the gym.", "E) Mina told me that she was tired after the long day at school.", "F) The police are here to investigate the accident on the main road."]), s=_S115 + pos(2))
RE(1, 115, "C", p="\n".join(["A) The rich are not always happy with their lives.", "B) Mina said that she has finished the report before noon.", "C) Tom told me that he was tired after the trip.",
                             "D) Each of the machines in the factory needs regular repair.", "E) She asked where was the station when she got off the bus.", "F) The police are investigating the case of the missing bicycle."]), s=_S115 + pos(3))
RE(1, 115, "D", p="\n".join(["A) The elderly needs better access to healthcare in rural areas.", "B) Tom said that he would arrive later because of the heavy traffic.", "C) Jane asked me where did I live when we first met.",
                             "D) Neither of the plans is perfect, but we must choose one.", "E) Mina told me that she was busy with her science project.", "F) The police are discussing the issue with the local residents."]), s=_S115 + pos(4))
RE(1, 115, "E", p="\n".join(["A) The poor deserve support from the government and the community.", "B) Mina said that she could help us with the school festival.", "C) Tom asked me where I had been during the summer vacation.",
                             "D) Every one of the computers in the lab needs an update this week.", "E) Jane told that she was late because of the traffic jam.", "F) The cattle are grazing peacefully on the green hill."]), s=_S115 + pos(5))
RE(1, 115, "F", p="\n".join(["A) The disabled need accessible facilities in every public building.", "B) Tom said he had finished the work before the deadline.", "C) Mina asked why Jane had left the party so early.",
                             "D) Each of the answers on the test are correct.", "E) Jane told me she would call after dinner.", "F) The police are searching the area for the lost child."]), s=_S115 + pos(3))
