# 2026-10-26 전체 감수(4급 D·E·F, 1~3급 F 제외 완료) 반영 — 1급. 확인 완료가 아니면서 메모·부적합이 남은 문서와,
# 같은 번호의 확인 완료가 아닌 유형(감수 전인 F 포함) 가운데 같은 결함(대부분 ‘원문항보다 짧다’)이 있는 것을 고친다.
MEMO6 = "감수 메모 반영(10-26): "
def OKS(items, a): return [w + OK(i + 1, a) for i, w in enumerate(items)]
def ADD(g_, n_, t_, more): return (OLD(g_, n_, t_).get("s", "") + " " + more).strip()
def PJ(*lines): return ["문장별 판정: " + l for l in lines]
CNT = ["1개", "2개", "3개", "4개", "5개"]
LEN = MEMO6 + "원문항보다 짧던 문장을 원문항 길이 이상으로 늘렸다. 틀린 곳과 정답은 그대로다."
LENP = MEMO6 + "원문항보다 짧던 지문을 원문항 길이 이상으로 늘렸다. 보기와 정답은 그대로다."
LENC = MEMO6 + "원문항보다 짧던 보기 문장을 원문항 길이 이상으로 늘렸다. 정답 위치는 그대로다."
def L(g_, n_, t_, **kw): RE(g_, n_, t_, s=ADD(g_, n_, t_, kw.pop("why", LEN)), **kw)

# 1-4 D·F: 보기 문장 늘리기
RE(1, 4, "D", c=["We discussed about the problem with our teacher yesterday.", "He finally reached at the station after a long walk.", "She married with a doctor from her hometown last year.", "We approached the entrance of the old museum quietly.", "They entered into the hall before the concert started."], a=4,
   k="‘We approached the entrance of the old museum quietly.’만 approach가 목적어를 바로 취해 올바르다.",
   n=OKS(["discuss는 전치사 없이 목적어를 바로 취하므로 about을 빼야 하므로", "reach는 전치사 없이 목적어를 바로 취하므로 at을 빼야 하므로", "marry는 전치사 없이 목적어를 바로 취하므로 with를 빼야 하므로", "approach가 전치사 없이 목적어 the entrance를 바로 취해 올바르므로", "enter(들어가다)는 전치사 없이 목적어를 바로 취하므로 into를 빼야 하므로"], 4), s=ADD(1, 4, "D", LENC))
RE(1, 4, "F", c=["The group reached to the summit early in the morning.", "Mina discussed about the plan with her classmates.", "The hikers reached the shelter on the mountain before dark.", "She resembles with her older sister in many ways.", "He entered into the room without knocking on the door."], a=3,
   k="‘The hikers reached the shelter on the mountain before dark.’만 reach가 목적어를 바로 취해 올바르다.",
   n=OKS(["reach는 전치사 없이 목적어를 바로 취하므로 to를 빼야 하므로", "discuss는 전치사 없이 목적어를 바로 취하므로 about을 빼야 하므로", "reach가 전치사 없이 목적어 the shelter를 바로 취해 올바르므로", "resemble은 전치사 없이 목적어를 바로 취하므로 with를 빼야 하므로", "enter(들어가다)는 전치사 없이 목적어를 바로 취하므로 into를 빼야 하므로"], 3), s=ADD(1, 4, "F", LENC))

# 1-6 E·F
L(1, 6, "E", p="The explanation from our science teacher _________ reasonable to all of us.", why=LENP)
L(1, 6, "F", p="The tomato sauce in this pasta _________ too salty for me.", why=LENP)

# 1-7 D·F
L(1, 7, "D", p="Last Saturday, we ①<u>entered</u> the city museum and ②<u>attended</u> a lecture about old paintings. After the lecture, the class ③<u>discussed about</u> the exhibit for an hour. Then we ④<u>approached</u> the guide and ⑤<u>asked about</u> the artist's life.", why=LENP)
L(1, 7, "F", p="Jane ①<u>approached</u> the front desk of the hotel, ②<u>entered</u> the meeting room, and ③<u>reached</u> her seat in the back. She ④<u>discussed</u> the plan with her coworkers for a while, then ⑤<u>reached to</u> a decision.", why=LENP)

# 1-15 D·E·F: a)~f) 문장 늘리기(문장별 판정을 새로 씀)
ST15 = "다음 중 밑줄 친 부분이 어법상 틀린 문장의 개수를 고르시오."
RE(1, 15, "D", st=ST15, p="a) Tom <u>has seen</u> that action movie twice with his best friends.\nb) When Mina <u>will get</u> home from school, she will call you.\nc) They <u>are studying</u> for the final exam in the library now.\nd) This expensive book <u>is belonging</u> to my classmate Jane.\ne) We realized the last bus <u>had gone</u> when we reached the stop.\nf) By 2030, she <u>will have lived</u> in this city for twenty years.",
   c=CNT, a=2, pre=PJ("a) 옳음: 경험을 나타내는 현재완료이다.", "b) 틀림: 때를 나타내는 부사절에서는 미래의 일도 현재시제로 쓴다. When Mina gets home from school.", "c) 옳음: now와 함께 쓴 현재진행형이다.", "d) 틀림: belong은 상태동사라 진행형으로 쓰지 않는다. This expensive book belongs to my classmate Jane.", "e) 옳음: 정류장에 도착하기 전에 버스가 떠났으므로 과거완료이다.", "f) 옳음: 2030년까지 이어질 일을 미래완료로 나타냈다."),
   k="밑줄 친 부분이 어법상 틀린 문장은 b), d)로 2개이다.", n="cnt", s=ADD(1, 15, "D", LEN))
RE(1, 15, "E", st=ST15, p="a) We <u>have known</u> Jane since we were in elementary school together.\nb) If it <u>rains</u> tomorrow, we will stay home and watch movies.\nc) Tom <u>is working</u> on his science project in his room now.\nd) My rich uncle <u>is owning</u> two houses near the beach.\ne) I discovered that I <u>had forgotten</u> the key to the front door.\nf) By noon tomorrow, they <u>will have finished</u> painting the whole house.",
   c=CNT, a=1, pre=PJ("a) 옳음: since와 함께 쓴 계속의 현재완료이다.", "b) 옳음: 조건의 부사절에서는 미래의 일도 현재시제로 쓴다.", "c) 옳음: now와 함께 쓴 현재진행형이다.", "d) 틀림: own은 상태동사라 진행형으로 쓰지 않는다. My rich uncle owns two houses near the beach.", "e) 옳음: 알아차리기 전에 이미 잊고 있었으므로 과거완료이다.", "f) 옳음: 내일 정오까지 끝날 일을 미래완료로 나타냈다."),
   k="밑줄 친 부분이 어법상 틀린 문장은 d)로 1개이다.", n="cnt", s=ADD(1, 15, "E", LEN))
RE(1, 15, "F", st=ST15, p="a) Jane <u>has just arrived</u> at the airport with her parents.\nb) After Tom <u>will finish</u> his homework, we will leave for the park.\nc) Mina <u>is talking</u> on the phone with her grandmother right now.\nd) He <u>is preferring</u> hot green tea to coffee these days.\ne) We found that the small store <u>had closed</u> before we got there.\nf) By Friday, he <u>will have completed</u> the task for his manager.",
   c=CNT, a=2, pre=PJ("a) 옳음: just와 함께 쓴 완료의 현재완료이다.", "b) 틀림: 때를 나타내는 부사절에서는 미래의 일도 현재시제로 쓴다. After Tom finishes his homework.", "c) 옳음: right now와 함께 쓴 현재진행형이다.", "d) 틀림: prefer는 상태동사라 진행형으로 쓰지 않는다. He prefers hot green tea to coffee.", "e) 옳음: 도착하기 전에 가게가 문을 닫았으므로 과거완료이다.", "f) 옳음: 금요일까지 끝날 일을 미래완료로 나타냈다."),
   k="밑줄 친 부분이 어법상 틀린 문장은 b), d)로 2개이다.", n="cnt", s=ADD(1, 15, "F", LEN))

# 1-19 E: 원문항(사무실 도착·회의)과 너무 비슷해 장면을 바꿈. F: 길이
RE(1, 19, "E", p="When the police (<u>    A    </u>) the bank downtown, the two thieves (<u>    B    </u>) already (<u>    C    </u>) with the money.\n(경찰이 시내 은행에 도착했을 때, 두 도둑은 이미 돈을 가지고 달아난 뒤였다.)",
   c=["arrived at - have - escaped", "arrived at - have - escape", "had arrived at - had - escaped", "arrived at - had - escaped", "arrived at - had - escape"], a=4,
   k="도착한 일이 기준이고 도둑들이 달아난 일은 그보다 먼저이므로 arrived at - had - escaped가 알맞다.",
   n=OKS(["(B) have: 기준이 과거(도착한 때)이므로 현재완료를 쓸 수 없다. 그보다 먼저 끝난 일은 과거완료 had로 써야 하므로", "(B) have: 현재완료를 쓸 수 없고, (C) escape: had 뒤에는 과거분사 escaped를 써야 하므로", "(A) had arrived at: 기준이 되는 도착은 단순과거 arrived at으로 써야 하므로", "도착은 단순과거(arrived at), 그보다 먼저 일어난 도주는 과거완료(had escaped)로 모든 자리가 알맞으므로", "(C) escape: had 뒤에는 과거분사 escaped를 써야 하므로"], 4),
   s=ADD(1, 19, "E", MEMO6 + "원문항(사무실에 도착했을 때 회의가 이미 끝남)과 장면·낱말이 거의 같아, 경찰이 도착했을 때 도둑이 이미 달아난 장면으로 바꿨다." + pos(4)))
L(1, 19, "F", p="When I (<u>    A    </u>) the small bakery near my house, it (<u>    B    </u>) already (<u>    C    </u>) for the day.\n(내가 집 근처 작은 빵집에 도착했을 때, 빵집은 이미 그날 문을 닫은 뒤였다.)",
   k="도착한 일이 기준이고 빵집이 문을 닫은 일은 그보다 먼저이므로 reached - had - closed가 알맞다.",
   n=[x.replace("가게가 문을 닫은 일", "빵집이 문을 닫은 일") for x in OLD(1, 19, "F")["n"]], why=LENP)

# 1-20 D·E·F
L(1, 20, "D", p="Mina (A)_________ for her final exam all morning in the quiet school library when she finally (B)_________ a short break for lunch.", why=LENP)
L(1, 20, "E", p="The team (A)_________ on the difficult science project for weeks when they finally (B)_________ the solution to the main problem last Friday.", why=LENP)
L(1, 20, "F", p="It (A)_________ for two days without stopping in our small town when the dark sky finally (B)_________ early on Sunday morning.", why=LENP)

# 1-23 D·E·F
L(1, 23, "D", p="• We are used to _____ long distances to visit our grandparents.\n• People used to _____ paper maps instead of GPS on long trips.", why=LENP)
L(1, 23, "E", p="• Jane is used to _____ alone in her quiet office at night.\n• Children used to _____ outside until dark in the old days.", why=LENP)
L(1, 23, "F", p="• Mina still isn't used to _____ spicy food like kimchi stew.\n• People used to _____ film cameras before smartphones became popular.", why=LENP)

# 1-24 D·E·F
L(1, 24, "D", p="The doctor ①<u>insisted</u> that the patient ②<u>should</u> ③<u>be examined</u> again by a specialist and ④<u>that</u> the nurse ⑤<u>checks</u> the medical records carefully.")
L(1, 24, "E", p="The manager ①<u>demanded</u> that the sales report ②<u>should</u> ③<u>be completed</u> by today and ④<u>that</u> Tom ⑤<u>attends</u> the meeting with the clients.")
L(1, 24, "F", p="The committee ①<u>proposed</u> that the school budget ②<u>should</u> ③<u>be reduced</u> next year and ④<u>that</u> every department ⑤<u>uses</u> fewer office supplies.")

# 1-28 D: 제시어 순서를 더 무작위로
RE(1, 28, "D", p="(train / not / they'd / the / miss / better / .)", s=ADD(1, 28, "D", MEMO6 + "제시어가 정답 어순과 거의 같아 순서를 더 무작위로 섞었다. 보기와 정답은 그대로다."))

# 1-35 D: b) 수동태 문장의 뜻이 어색하다는 의문 → 뜻이 분명한 구동사 문장으로 교체
RE(1, 35, "D", p=OLD(1, 35, "D")["p"].replace("b) Grandma brought up three children on her own.\n→ Three children were brought up on her own by Grandma.", "b) Our neighbor took care of the puppy during our vacation.\n→ The puppy was taken care of by our neighbor during our vacation."),
   pre=[x.replace("b) 옳음: 구동사 bring up을 그대로 두었다.", "b) 옳음: 구동사 take care of의 of를 빠뜨리지 않고 그대로 두었다.") for x in OLD(1, 35, "D")["pre"]],
   s=ADD(1, 35, "D", MEMO6 + "b)의 수동태(Three children were brought up on her own by Grandma)는 her가 누구인지 헷갈려 옳은지 의문이 든다는 메모에 따라, 뜻이 분명한 구동사 문장(take care of)으로 바꿨다. 옳고 틀린 판정과 정답은 그대로다."))

# 1-42 D·F
L(1, 42, "D", p="〈보기〉\nTom left home early in the morning <u>to</u> avoid heavy traffic.",
  c=["We need someone <u>to</u> fix the roof before the rainy season.", "I opened the window <u>to</u> get some fresh air into the room.", "His job at the zoo is <u>to</u> take care of the animals.", "<u>To</u> keep a diary every day is a good habit for students.", "She decided <u>to</u> study abroad in Canada next year."])
L(1, 42, "F", p="〈보기〉\nWe went downtown early <u>to</u> meet the tour guide at the station.",
  c=["It is not easy <u>to</u> make new friends in a new school.", "Give me a pen <u>to</u> write with for the test.", "The best way is <u>to</u> ask the teacher for help.", "Tom studied very hard <u>to</u> pass the entrance exam.", "We planned <u>to</u> leave our hotel at dawn."])

# 1-43 E·F
L(1, 43, "E", p="The engineers _______ testing the new security system at the factory.", why=LENP)
L(1, 43, "F", p="We _______ waiting outside the stadium in the cold rain.", why=LENP)

# 1-44 D·F: 밑줄을 원문항처럼 두세 낱말로
RE(1, 44, "D", p="a) We are looking for a quiet house <u>to live</u>.\nb) There is <u>nothing strange</u> to report today.\nc) The road is <u>wide enough</u> for two cars to pass.\nd) It was <u>careless of him</u> to forget his passport.\ne) The coffee is <u>too bitter</u> for me to drink.",
   c=["b, c, d, e", "a, c, e", "b, c, d", "a, b, c", "c, d, e"], a=1,
   pre=PJ("a) 틀림: ‘집에서 살다’는 live in a house이므로 to live in으로 써야 한다.", "b) 옳음: -thing으로 끝나는 말은 형용사가 뒤에서 꾸민다.", "c) 옳음: 형용사 + enough 어순이다.", "d) 옳음: 성품 형용사 careless 뒤에 of + 목적격을 썼다.", "e) 옳음: too + 형용사 + to부정사(너무 ~해서 …할 수 없다) 구문이다."),
   k="어법상 옳은 문장은 b, c, d, e이다.", n=setnotes(["b, c, d, e", "a, c, e", "b, c, d", "a, b, c", "c, d, e"], "b, c, d, e", "옳은 문장"),
   s=ADD(1, 44, "D", MEMO6 + "밑줄이 원문항(두세 낱말)과 달리 구문 전체를 덮어 원문항처럼 판단할 부분만 짧게 밑줄 쳤다. 정답은 그대로다."))
RE(1, 44, "F", p="a) Mina wants a quiet room <u>to study in</u> after school every day.\nb) There is <u>exciting nothing</u> to watch on TV tonight.\nc) The old bridge is <u>strong enough</u> for heavy trucks to cross.\nd) It was <u>brave of Leo</u> to act so quickly in the fire.\ne) Please tell me <u>what to doing</u> next in this situation.",
   pre=PJ("a) 옳음: ‘방에서 공부하다’는 study in a room이므로 전치사 in을 썼다.", "b) 틀림: -thing으로 끝나는 말은 형용사가 뒤에서 꾸민다. exciting nothing → nothing exciting.", "c) 옳음: 형용사 + enough 어순이다.", "d) 옳음: 성품 형용사 brave 뒤에 of + 목적격을 썼다.", "e) 틀림: 의문사 + to부정사이므로 what to do로 써야 한다."),
   s=ADD(1, 44, "F", MEMO6 + "같은 번호 D의 메모(밑줄 범위가 원문항과 다름)와 같은 문제가 있어 밑줄을 두세 낱말로 줄이고, 원문항보다 짧던 문장을 늘렸다. 정답은 그대로다."))

# 1-45 E·F
L(1, 45, "E", p="It appeared that they had forgotten the key to the classroom.\n= They appeared to (A)_____ the key to the classroom.\nIt appears that Leo is tired after the long trip.\n= Leo appears to (B)_____ after the long trip.", why=LENP)
L(1, 45, "F", p="It appeared that Tom had been sick for a few days.\n= Tom appeared to (A)_____ for a few days.\nIt appears that Jane is ready for the big race.\n= Jane appears to (B)_____ for the big race.", why=LENP)

# 1-47 E·F
L(1, 47, "E", p="A: Do you like the new haircut I got yesterday at the salon?\nB: (<u>         </u>), I liked your long hair much better. It suited you more.", why=LENP)
L(1, 47, "F", p="A: Your uncle knows everything about computers and the internet.\nB: Yes, he can fix any problem in minutes. He's a walking dictionary, (<u>         </u>).", why=LENP)

# 1-48 D·E
L(1, 48, "D", p="• The old building seems (<u>      A      </u>) crowded with shoppers many years ago.\n• Sadly, it seems (<u>      B      </u>) almost empty and quiet now.", why=LENP)
L(1, 48, "E", p="• Jane appears (<u>      A      </u>) free for a few hours earlier today.\n• But she appears (<u>      B      </u>) very busy with her science homework now.", why=LENP)

# 1-52 E·F
L(1, 52, "E", p="They left the party early last night but denied it.\n= They denied _________ the party early last night.", why=LENP)
L(1, 52, "F", p="Leo told the secret to his friends but denied it later.\n= Leo denied _________ the secret to his friends.", why=LENP)

# 1-54 C·E·F: 보기 문장 늘리기(동사와 정답 위치는 그대로)
L(1, 54, "C", c=["My dad quit smoking for his health last year.", "She wants to open the window for some fresh air.", "Mina avoided to answer the difficult question in class.", "The kids practiced singing the song for the concert.", "He decided to take a short break after lunch."], why=LENC)
L(1, 54, "E", c=["The boy denied eating the chocolate cake in the fridge.", "Jane postponed to make the decision until next week.", "I promised to help my mom with the cooking tonight.", "She gave up learning the violin after two years.", "They agreed to meet at the library at noon."], why=LENC)
L(1, 54, "F", c=["He recommended visiting the old palace in the city.", "They need to leave early to catch the first train.", "Mina imagined living in Paris with her family.", "We finished to clean the room before dinner.", "I learned to ride a bike when I was seven."], why=LENC)

# 1-69 D·E·F: 서로 맞부딪치는 설명(한쪽이 맞으면 다른 쪽이 틀림)이 정답을 알려 주어, 정답 설명과 겹치지 않는 설명으로 바꿈
L69 = MEMO6 + "정답 설명과 서로 맞부딪치는 설명(한쪽이 옳으면 다른 쪽이 틀림)이 있어 정답을 쉽게 고를 수 있었다. 정답 설명과 겹치지 않는 다른 옳은 설명으로 바꿨다."
RE(1, 69, "D", c=["접속사 Since를 생략한다.", "no buses와 Mina는 주어가 다르므로 no buses를 남긴다.", "were running은 주절과 같은 때이므로 being running으로 바꾼다.", "부사절의 시제가 주절(called)과 같으므로 having + 과거분사를 쓰지 않는다.", "분사구문을 부정할 때는 분사 바로 앞에 not을 둔다."], a=3,
   k="진행형 were running은 분사구문에서 running만 남기므로",
   n=OKS(["분사구문에서는 접속사를 생략한다. 옳은 설명이므로", "부사절과 주절의 주어가 다르면 부사절의 주어를 남긴다. 옳은 설명이므로", "진행형 were running은 being running이 아니라 running만 남긴다(No buses running). 옳지 않은 설명이므로", "두 절의 때가 같으면 단순분사를 쓰고 having + 과거분사는 쓰지 않는다. 옳은 설명이므로", "분사구문의 부정은 not을 분사 앞에 둔다(not knowing ~). 옳은 설명이므로"], 3), s=ADD(1, 69, "D", L69 + pos(3)))
RE(1, 69, "E", c=["접속사 Since를 생략한다.", "부사절의 시제가 주절(sent)과 같으므로 단순분사를 쓴다.", "주어가 다르므로 no one을 빼고 Answering the phone, Tom sent an email.로 쓴다.", "진행형 was answering은 분사구문에서 answering만 남긴다.", "분사구문 뒤에는 쉼표를 찍고 주절을 이어 쓴다."], a=3,
   k="주어가 다르면 부사절의 주어 no one을 남겨야 하므로",
   n=OKS(["분사구문에서는 접속사를 생략한다. 옳은 설명이므로", "두 절의 때가 같으면 단순분사(-ing)를 쓴다. 옳은 설명이므로", "주어가 다르면 부사절의 주어 no one을 남겨야 한다(No one answering the phone, ~). 옳지 않은 설명이므로", "진행형의 be동사는 분사구문에서 사라지고 answering만 남는다. 옳은 설명이므로", "분사구문과 주절은 쉼표로 이어 쓴다. 옳은 설명이므로"], 3), s=ADD(1, 69, "E", L69 + pos(3)))
RE(1, 69, "F", c=["접속사 Since를 생략한다.", "no lights와 Jane은 주어가 다르므로 no lights를 남긴다.", "Since는 이유를 나타내므로 분사구문으로 바꿔도 이유의 뜻이 남는다.", "were는 주절(assumed)과 같은 때이므로 being으로 바꾼다.", "분사구문으로 바꾸면 주절의 동사 assumed도 assuming으로 바꿔야 한다."], a=5,
   k="분사구문으로 바꾸는 것은 부사절뿐이고 주절의 동사는 그대로 두므로",
   n=OKS(["분사구문에서는 접속사를 생략한다. 옳은 설명이므로", "부사절과 주절의 주어가 다르면 부사절의 주어를 남긴다. 옳은 설명이므로", "분사구문으로 바꿔도 문맥에 따라 이유의 뜻이 그대로 전해진다. 옳은 설명이므로", "두 절의 때가 같으므로 were를 단순분사 being으로 바꾼다. 옳은 설명이므로", "분사구문으로 바꾸는 것은 부사절뿐이고 주절의 동사 assumed는 그대로 둔다. 옳지 않은 설명이므로"], 5),
   s=ADD(1, 69, "F", L69 + " (같은 번호 D·E의 메모와 같은 문제: having been이 정답이던 설명과 being으로 바꾼다는 설명이 맞부딪쳤다.)" + pos(5)))

# 1-74 E·F
L(1, 74, "E", p="Leo: Which sport do you think is harder, tennis or swimming?\nJane: Tennis is ①<u>more demanding</u> for beginners.\nLeo: For me, swimming is ②<u>far more tiring</u>.\nJane: Running is ③<u>as simple as</u> walking, I guess.\nLeo: The new gym is ④<u>less crowded than</u> the old one.\nJane: But yoga is ⑤<u>more relaxing as</u> running.", why=LENP)
L(1, 74, "F", p="Tom: Which job do you think is harder, teaching or nursing?\nMina: Teaching is ①<u>more stressful</u> in many ways.\nTom: But nursing is ②<u>much more demanding</u>, I think.\nMina: Both are ③<u>as meaningful as</u> each other.\nTom: Office work is ④<u>less physical than</u> nursing.\nMina: Still, it can be ⑤<u>more tiring as</u> people think.", why=LENP)

# 1-75 D·E·F
L(1, 75, "D", p="A) This new train is much faster than the old one.\nB) Jane is as tall as her older sister Mina.\nC) This bag is two times more heavier than mine.\nD) Tom is less more careful than his friend Leo.\nE) No runner in our school is as fast as Mina.\nF) He speaks English as fluent as a native speaker.")
L(1, 75, "E", p="A) The new plan is far more practical than the old one.\nB) This room is three times as large as ours.\nC) Mina is more kinder than her sister Jane.\nD) No other route to the station is shorter than this one.\nE) Tom is not so patient as his brother Leo.\nF) This car is much more cheaper than mine.")
L(1, 75, "F", p="A) The second test was much easier than the first one.\nB) This fish tank is four times as large as that one.\nC) Jane is less experienced than Mina at teaching.\nD) Tom is very faster than Leo in the race.\nE) No other book in the library is more usefuler than this one.\nF) My dog is three times as older as yours.")

# 1-76 D
RE(1, 76, "D", p="(taller / than / a / Mina / her / little / sister / Jane / is / now)",
   c=["Mina is taller a little than her sister Jane now.", "Mina a little is taller than her sister Jane now.", "Mina is a taller little than her sister Jane now.", "Mina is a little taller than her sister Jane now.", "Mina is little a taller than her sister Jane now."], a=4,
   n=OKS(["a little은 비교급 taller 앞에 와야 하므로", "a little taller는 be동사 is 뒤에 와야 하므로", "a little은 한 덩어리로 비교급 앞에 와야 하므로", "be동사 + a little + 비교급 + than 어순이 바르므로", "a little의 두 낱말 순서가 뒤바뀌었으므로"], 4), s=ADD(1, 76, "D", LEN))

# 1-79 E·F: 보기를 원문항처럼 근거를 들어 설명하는 문장으로(단조로움)
L79 = MEMO6 + "보기가 짧고 단조로워 원문항처럼 근거를 들어 설명하는 문장으로 다시 썼다. 정답 위치는 그대로다."
RE(1, 79, "E", p="Jane is <u>one of the best students</u> in our English class this year.",
   c=["'best'는 'good'의 비교급이므로 앞에 'the'를 붙일 수 없고 'better'로 고쳐야 한다.", "'one of the' 뒤에 최상급이 왔으므로 뒤에 오는 명사 'students'는 단수형 'student'로 바꿔야 한다.", "'in our English class'는 비교의 범위를 나타내므로 'of our English class'로 바꿔야 문법적으로 맞다.", "'students'가 복수형인 이유는 '가장 뛰어난 여러 학생들' 가운데 한 명이라는 뜻을 나타내기 때문이다.", "'one'이 주어 'Jane'을 가리키지만 뒤의 'students'가 복수이므로, 동사 'is'는 'are'로 바꿔야 한다."], a=4,
   k="‘가장 뛰어난 학생들’ 가운데 한 명이라는 뜻이라 복수 students를 쓰므로",
   n=OKS(["best는 good의 최상급이므로 the와 함께 쓰는 것이 맞다. 옳지 않은 설명이므로", "one of the + 최상급 뒤에는 복수명사가 와야 한다. 옳지 않은 설명이므로", "최상급의 범위가 장소나 집단이면 in을 쓰므로 in our English class가 맞다. 옳지 않은 설명이므로", "‘가장 뛰어난 학생들’ 가운데 한 명이라는 뜻이라 복수 students를 쓴다. 옳은 설명이므로", "주어의 중심은 one(Jane)이므로 단수 동사 is가 맞다. 옳지 않은 설명이므로"], 4), s=ADD(1, 79, "E", L79))
RE(1, 79, "F", p="Seoul is <u>one of the largest cities</u> that I have ever visited in Asia.",
   c=["'largest'는 최상급이지만 'one of' 뒤에서는 'the'를 생략하고 'one of largest cities'로 써야 한다.", "'one of the + 최상급 + 복수명사'는 '가장 ~한 것들 중 하나'라는 뜻이므로 'cities'를 복수형으로 썼다.", "'that I have ever visited'가 'cities'를 꾸미므로, 앞의 최상급 'largest'는 원급 'large'로 바꿔야 한다.", "'cities'가 복수형이므로 그 앞의 'one'도 복수형 'ones'로 바꿔야 문법적으로 맞다.", "'one of' 뒤에 최상급이 오면 그 뒤의 명사는 반드시 셀 수 없는 명사여야 한다."], a=2,
   k="‘가장 큰 도시들’ 가운데 하나라는 뜻이라 복수 cities를 쓰므로",
   n=OKS(["one of 뒤에는 the + 최상급을 그대로 쓴다. 옳지 않은 설명이므로", "‘가장 큰 도시들’ 가운데 하나라는 뜻이라 복수 cities를 쓴다. 옳은 설명이므로", "have ever + 과거분사의 관계절은 최상급과 함께 자주 쓰이므로 largest가 맞다. 옳지 않은 설명이므로", "‘~ 중 하나’는 one of로 쓰고 ones로 바꾸지 않는다. 옳지 않은 설명이므로", "one of the + 최상급 뒤에는 셀 수 있는 명사의 복수형이 온다. 옳지 않은 설명이므로"], 2),
   s=ADD(1, 79, "F", L79 + " (같은 번호 E의 메모와 같은 문제)"))

# 1-83 D·E·F: 보기 문장을 원문항 길이(12낱말)로
L(1, 83, "D", c=["Friday is the day when we have music class at our school.", "This is the town when my father grew up as a little boy.", "Tell me how you fixed the old computer in your room yesterday.", "I know the reason why she is angry with her best friend.", "This is the way I usually cook rice for my whole family."], why=LENC)
L(1, 83, "E", c=["The hotel where we stayed last summer was very close to the beach.", "I'll never forget the moment when I heard the good news from my teacher.", "That is why I was late for the important meeting this morning.", "This is the way she solves difficult math problems so quickly.", "Please show me the way how you made this robot for the science fair."], why=LENC)
L(1, 83, "F", c=["I don't know the reason where he left the party so early last night.", "Winter is the season when many birds fly south to warmer places.", "This is the park where I walk my dog every evening after dinner.", "This is how the story about the old king finally ends.", "The way he talks to little children is really funny and kind."], why=LENC)

# 1-86 D·E·F: 문장과 보기를 원문항 길이로
RV86 = ["what은 선행사를 포함하므로 선행사 뒤에 쓸 수 없으므로", "which만 쓰면 원래 문장의 전치사가 빠져 맞지 않으므로"]
RE(1, 86, "D", p="I know the reason for which Mina left the party early last night.",
   c=["I know the reason what Mina left the party early last night.", "I know the reason why Mina left the party early last night.", "I know the reason which Mina left the party early last night.", "I know the reason where Mina left the party early last night.", "I know the reason how Mina left the party early last night."], a=2,
   n=OKS([RV86[0], "이유의 선행사 the reason 뒤에 관계부사 why를 써서 for which를 바르게 바꿨으므로", RV86[1], "where는 장소를 나타내므로 이유의 선행사와 맞지 않으므로", "how는 방법을 나타내므로 이유의 선행사와 맞지 않으므로"], 2), s=ADD(1, 86, "D", LEN))
RE(1, 86, "E", p="Friday is the day on which the club meets in the music room after school.",
   c=["Friday is the day when the club meets in the music room after school.", "Friday is the day where the club meets in the music room after school.", "Friday is the day why the club meets in the music room after school.", "Friday is the day what the club meets in the music room after school.", "Friday is the day which the club meets in the music room after school."], a=1,
   n=OKS(["때의 선행사 the day 뒤에 관계부사 when을 써서 on which를 바르게 바꿨으므로", "where는 장소를 나타내므로 때의 선행사와 맞지 않으므로", "why는 이유를 나타내므로 때의 선행사와 맞지 않으므로", RV86[0], RV86[1]], 1), s=ADD(1, 86, "E", LEN))
RE(1, 86, "F", p="This is the town in which Jane grew up with her grandparents as a child.",
   c=["This is the town that Jane grew up with her grandparents as a child.", "This is the town when Jane grew up with her grandparents as a child.", "This is the town what Jane grew up with her grandparents as a child.", "This is the town where Jane grew up with her grandparents as a child.", "This is the town which Jane grew up with her grandparents as a child."], a=4,
   n=OKS(["that만 쓰면 원래 문장의 전치사 in이 빠지고 관계부사도 아니므로", "when은 때를 나타내므로 장소의 선행사와 맞지 않으므로", RV86[0], "장소의 선행사 the town 뒤에 관계부사 where를 써서 in which를 바르게 바꿨으므로", RV86[1]], 4), s=ADD(1, 86, "F", LEN))

# 1-89 D·E·F: (B) ‘각각’과 ‘동시에’의 차이가 흐려 복수 정답처럼 보임 → 오답의 (B)를 분명히 틀린 ‘하나만’으로
L89 = MEMO6 + "‘각각’과 ‘동시에’의 차이가 분명하지 않아 정답과 (B)만 다른 보기가 정답처럼 보였다. 오답의 (B)를 분명히 틀린 ‘하나만’으로 바꿨다."
W89 = {"D": ("signed", "과거분사", "‘서명된’이라는 수동의 뜻으로 명사를 꾸미는 과거분사"), "E": ("standing", "현재분사", "-ing형으로 명사를 꾸미는 현재분사"), "F": ("wearing", "현재분사", "-ing형으로 명사를 꾸미는 현재분사")}
def F89(t, p=None):
    old = OLD(1, 89, t); c = [x.replace("각각", "하나만") for x in old.get("c", V(1, 89, t)["c"])]
    a = old.get("a") or int(V(1, 89, t)["ans"]); word, cv, cdesc = W89[t]; nn = []
    for i, ch in enumerate(c):
        A, B, C_ = [x.split(") ", 1)[1].strip() for x in ch.split(" - ")]
        if i + 1 == a: nn.append(f"관계대명사와 be동사를 동시에 생략하고 남은 말({word})이 {cdesc}이므로 모든 자리가 알맞다. 정답이다."); continue
        bits = []
        if A != "be동사": bits.append(f"(A) {A}: 주격 관계대명사와 함께 생략되는 것은 be동사이므로 맞지 않는다.")
        if B != "동시에": bits.append(f"(B) {B}: 관계대명사와 be동사는 한꺼번에(동시에) 생략하므로 맞지 않는다.")
        if C_ != cv: bits.append(f"(C) {C_}: 남는 말({word})은 {cdesc}이므로 맞지 않는다.")
        nn.append(" ".join(bits) + " 따라서 오답이다.")
    kw = dict(c=c, n=nn, k="주격 관계대명사와 be동사는 함께(동시에) 생략하고 남은 분사가 명사를 꾸민다.", s=ADD(1, 89, t, L89))
    if p: kw["p"] = p
    RE(1, 89, t, **kw)
F89("D", p=OLD(1, 89, "D")["p"].replace("The documents <u>which were signed</u> yesterday are ready.", "The documents <u>which were signed</u> by the manager yesterday are ready."))
F89("E"); F89("F")

# 1-90 D: 지문을 원문항보다 넉넉히
L(1, 90, "D", p="Tom lives in a quiet little town ①<u>where</u> many young artists live and work together. He knows ②<u>whoever</u> runs the small local gallery on Main Street. The bright studio ③<u>which</u> he rents above the old bakery is small but very cozy. He often remembers the year ④<u>when</u> he first moved there with his little dog. The wooden table ⑤<u>on that</u> he paints every morning is very old.", why=LENP)

# 1-91 E·F
L(1, 91, "E", p="직설법: We have this new software, so we can analyze the data quickly.\n가정법: _____ this new software, we could not analyze the data quickly.", why=LENP)
L(1, 91, "F", p="직설법: The team has enough funding, so it can continue the research.\n가정법: _____ enough funding, the team could not continue the research.", why=LENP)

# 1-95 D·E
L(1, 95, "D", p="A) Jane always acts as if she knew everything about the topic.\nB) If only Tom had called me earlier last night.\nC) If Mina had more free time, she would travel around the world.\nD) Without the map, we would have gotten lost in the forest.\nE) Had I saw the warning sign, I would have stopped the car.\nF) If it were not for music, our life would be boring.")
L(1, 95, "E", p="A) Tom talks as though he were the boss of our team.\nB) If only I had listened to my parents' advice.\nC) If Jane were taller, she would play basketball on the school team.\nD) But for the heavy rain, we would have gone out yesterday.\nE) Had Mina known the truth, she would have call me right away.\nF) If he had not helped me, I would fail the test last week.")

# 1-98 C·E·F: 낱말 하나씩 더해 원문항 길이(13낱말)로
NB98 = ["if의 위치가 틀려 조건절과 주절이 뒤바뀌었으므로", "if절은 If + 주어 + had 순서인데 had가 주어 앞에 왔으므로", "주절이 의문문 어순(would + 주어)이 되었으므로", "if + had + 과거분사(과거 조건), would + 동사원형 + now(현재 결과)의 혼합가정법을 바르게 배열했으므로", "if가 조건절 끝에 붙어 있고 낱말 순서가 크게 뒤섞였으므로"]
RE(1, 98, "C", p="(accepted / if / she / the / Mina / be / , / had / job / living / in / would / now / Japan / .)",
   c=["Mina had accepted the job if she would be living in Japan now.", "If had Mina accepted the job, she would be living in Japan now.", "If Mina had accepted the job, would she be living in Japan now.", "If Mina had accepted the job, she would be living in Japan now.", "Accepted Mina the job if had, she would be living in Japan now."], a=4,
   n=OKS([NB98[0], NB98[1], NB98[2], NB98[3], NB98[4]], 4), s=ADD(1, 98, "C", LEN))
RE(1, 98, "E", p="(chosen / we / the / if / route / had / , / be / other / we / there / would / by / now / .)",
   c=["If we had chosen the other route, would we be there by now.", "If we had chosen the other route, we would be there by now.", "We had chosen the other route if we would be there by now.", "If had we chosen the other route, we would be there by now.", "Had chosen we the other route if, we would be there by now."], a=2,
   n=OKS([NB98[2], NB98[3], NB98[0], NB98[1], NB98[4]], 2), s=ADD(1, 98, "E", LEN))
RE(1, 98, "F", p="(moved / Leo / if / last / Seoul / he / , / had / live / to / would / year / us / now / near / .)",
   c=["If had Leo moved to Seoul last year, he would live near us now.", "If Leo had moved to Seoul last year, would he live near us now.", "Leo had moved to Seoul last year if he would live near us now.", "Moved Leo to Seoul last year if had, he would live near us now.", "If Leo had moved to Seoul last year, he would live near us now."], a=5,
   n=OKS([NB98[1], NB98[2], NB98[0], NB98[4], NB98[3]], 5), s=ADD(1, 98, "F", LEN))

# 1-105 D·E·F
P105 = lambda t, rep: [x for x in OLD(1, 105, t)["pre"]] if not rep else [rep.get(x, x) for x in OLD(1, 105, t)["pre"]]
L(1, 105, "D", p="A) Despite it was raining heavily, we went out for a walk.\nB) Tom was so tired that he fell asleep on the sofa.\nC) Lest the child should fall, hold his hand tightly.\nD) Unless you hurry, you will be late for the concert.\nE) Whatever you decide, I will always support you.\nF) Do you know when will Mina come back home?\nG) However it is difficult, do not give up your dream.",
  pre=[x.replace("Although it was raining.", "Although it was raining heavily.").replace("when Mina will come.", "when Mina will come back home.") for x in OLD(1, 105, "D")["pre"]])
L(1, 105, "E", p="A) Because the heavy rain, the soccer match was canceled.\nB) Mina spoke so quietly that I could hardly hear her voice.\nC) Lest we be late for the train, we left home early.\nD) Unless Tom studies harder, he will not pass the exam.\nE) No matter how Jane is busy, she exercises every day.\nF) I wonder why did he leave the meeting so early.\nG) Whatever happens tomorrow, please call me first.",
  pre=[x.replace("why he left.", "why he left the meeting so early.") for x in OLD(1, 105, "E")["pre"]])
L(1, 105, "F", p="A) Although the long delay, we waited patiently at the gate.\nB) Jane was so nervous that she forgot her lines on stage.\nC) Lest Tom should miss the bus, he left home early.\nD) Unless it will rain tomorrow, we will play outside.\nE) No matter who calls me, do not answer the phone.\nF) I am not sure when the store closes on Sundays.\nG) However he drove carefully, the icy road was dangerous.",
  pre=[x.replace("Despite the delay.", "Despite the long delay.").replace("Unless it rains.", "Unless it rains tomorrow.") for x in OLD(1, 105, "F")["pre"]])

# 1-110 E·F
L(1, 110, "E", p="The team played (<u>      A      </u>) well in the final match that the crowd cheered loudly. (<u>      B      </u>) the loss of one key player, they won the game. It was (<u>      C      </u>) an exciting game that nobody left the stadium early.", why=LENP)
L(1, 110, "F", p="It was (<u>      A      </u>) an inspiring story about a brave girl that Mina cried. (<u>      B      </u>) the sad ending, she loved the book very much. The characters were (<u>      C      </u>) real that she felt she knew them well.", why=LENP)

# 1-112 D·F
L(1, 112, "D", p="• Three-quarters of the land in this area _____ protected by law.\n• Most of the houses on this street _____ empty now.")
L(1, 112, "F", p="• Most of the furniture in the new office _____ new.\n• A third of the participants in the contest _____ from abroad.")

# 1-115 E: 해설을 알기 쉽게 다시 씀(핵심 규칙에 문항에 없는 each/neither가 들어 있었다)
RE(1, 115, "E", r="주어의 실제 수에 동사를 맞춘다(the poor·cattle은 복수, every one of + 복수명사는 단수). 전달동사 say는 사람 목적어 없이 that절을 바로 쓰고, tell은 사람 목적어를 쓴 뒤 that절을 쓴다. 간접의문문은 의문사 + 주어 + 동사 어순이다.",
   pre=PJ("A) 옳음: the poor(가난한 사람들)는 복수이므로 deserve를 썼다.", "B) 옳음: 말한 때의 일을 could help로 전달했다.", "C) 옳음: asked me 뒤에 where + 주어 + 동사(had been) 어순으로 썼다.", "D) 옳음: every one of + 복수명사는 one이 중심이라 단수 동사 needs를 쓴다.", "E) 틀림: tell은 사람 목적어가 필요하다. Jane told me that ~ 또는 Jane said that ~으로 써야 한다.", "F) 옳음: cattle(소 떼)은 늘 복수로 쓰므로 are를 썼다."),
   k="어법상 옳은 문장은 A, B, C, D, F이다.", n=setnotes(V(1, 115, "E")["c"] if "c" not in OLD(1, 115, "E") else OLD(1, 115, "E")["c"], "A, B, C, D, F", "옳은 문장"),
   s=ADD(1, 115, "E", MEMO6 + "해설이 이해되지 않는다는 메모에 따라, 문항에 나오지 않는 each/neither를 말하던 핵심 규칙을 문항에 맞게 고치고 문장별 판정과 보기 해설을 알기 쉽게 다시 썼다. 문항은 그대로다."))

# 1-116 D·E·F
L(1, 116, "D", p="The number of applicants for the new job ________ growing rapidly this year.", why=LENP)
L(1, 116, "E", p="The number of car accidents on this road ________ decreasing this year.", why=LENP)
L(1, 116, "F", p="The number of complaints from our customers ________ falling every month.", why=LENP)

# 1-117 E: 문장 길이와 줄바꿈, 보기 길이
RE(1, 117, "E", p='Jane said to Leo, "Do not forget the key to the classroom."\n→ Jane ________ Leo ________ ________ forget the key to the classroom.',
   c=["said - not to", "told - not for", "asked - to not", "told - not to", "told - don't"], a=4,
   k="told + 사람 + not to + 동사원형으로 부정 명령을 전달하므로",
   n=OKS(["said는 사람 목적어 뒤에 to부정사를 바로 잇지 않으므로 told로 고쳐야 하므로", "부정 명령은 not to + 동사원형으로 전달하므로 not for는 쓸 수 없으므로", "asked도 쓸 수 있지만 부정은 to 앞에 not을 두어 not to로 써야 하므로", "told + 사람 + not to + 동사원형으로 부정 명령을 바르게 전달했으므로", "간접 화법에서는 명령문의 don't를 그대로 쓰지 않고 not to로 바꿔야 하므로"], 4),
   s=ADD(1, 117, "E", MEMO6 + "원문항보다 짧던 문장을 늘리고, 한 줄에 / 로 붙어 있던 두 문장을 원문항처럼 줄을 바꿔 제시했다. 보기도 원문항 길이로 맞췄다." + pos(4)))

# 1-119 D·E·F: 설명 글을 원문항 길이로
L(1, 119, "D", p='<보기>\n"The manager demanded that the door be locked every night."\n설명: 주절의 동사가 \'요구(demand)\'를 나타내고 that절의 내용이 \'~해야 한다\'는 당위성을 담고 있을 때, that절의 동사는 주어와 관계없이 (<u>      A      </u>)을(를) 쓴다. 이때 문이 \'잠기는\' 것이므로 be + (<u>      B      </u>)의 수동 형태가 되며, be 앞에는 조동사 (<u>      C      </u>)이(가) 생략된 것으로 볼 수 있다.', why=LENP)
L(1, 119, "E", p='<보기>\n"Jane insisted that Leo apologize to his classmates."\n설명: 이 문장에서 주절의 동사 insist는 \'~해야 한다고 강하게 요구하다\', 즉 (<u>      A      </u>)의 뜻으로 쓰였으므로 that절의 동사는 주어가 3인칭 단수(Leo)임에도 불구하고 (<u>      B      </u>)을(를) 쓴다. 반면 insist가 \'(이미 일어난 사실을) ~라고 주장하다\'는 뜻이면 that절에 (<u>      C      </u>)을(를) 써서 Jane insisted that Leo had apologized.처럼 쓴다.', why=LENP)
L(1, 119, "F", p='<보기>\n"The new school rule requires that every student wear an ID card."\n설명: 주어 every student가 3인칭 단수인데도 that절의 동사를 \'wears\'가 아닌 (<u>      A      </u>)인 wear로 썼다. 이 자리에는 (<u>      B      </u>)을(를) 써도 같은 뜻이 되며, 이렇게 쓰는 것은 주절의 동사 require가 \'~해야 한다\'는 (<u>      C      </u>)을(를) 나타내기 때문이다.', why=LENP)

# 1-120 E·F
RE(1, 120, "E", p='(가) Tom said, "I will be late for the meeting."\n→ Tom said that he will be late for the meeting.\n(나) Mina asked me, "Where did you go last weekend?"\n→ Mina asked me where I had gone the previous weekend.\n(다) Jane said, "I can drive my father\'s car."\n→ Jane said that she could drive her father\'s car.\n(라) Leo said, "I finished my homework today."\n→ Leo said that he had finished his homework today.\n(마) Dad said to me, "Do not touch the hot pan."\n→ Dad told me not to touch the hot pan.',
   pre=["항목별 판정:", "(가) 틀림: will을 would로 바꿔야 한다.", "(나) 옳음: 간접의문문 어순이고 did go → had gone, last weekend → the previous weekend로 바꿨다.", "(다) 옳음: can을 could로, my를 her로 바꿨다.", "(라) 틀림: today는 that day로 바꿔야 한다.", "(마) 옳음: 부정 명령문은 told me not to touch로 전달한다."], s=ADD(1, 120, "E", LEN))
RE(1, 120, "F", p='(가) Mina said, "I have lost my key to the house."\n→ Mina said that she had lost her key to the house.\n(나) Tom asked, "Why did Jane leave the party early?"\n→ Tom asked why Jane had left the party early.\n(다) Jane said, "I will call you tonight."\n→ Jane said that she will call me that night.\n(라) Leo said to me, "Close the door behind you."\n→ Leo told me to close the door behind me.\n(마) Mom said to me, "Do not be late for dinner."\n→ Mom said me not to be late for dinner.',
   pre=["항목별 판정:", "(가) 옳음: have lost → had lost, my → her로 바꿨다.", "(나) 옳음: 간접의문문 어순이고 did leave → had left로 바꿨다.", "(다) 틀림: will을 would로 바꿔야 한다.", "(라) 옳음: 명령문은 told me to close로 전달하고 you를 me로 바꿨다.", "(마) 틀림: said 뒤에 사람을 바로 쓸 수 없다. Mom told me not to be late for dinner."], s=ADD(1, 120, "F", LEN))

# 1-124 D·E·F
L(1, 124, "D", okdup=True, p="A: ①<u>I have never experienced such cold weather</u> in my whole life.\nB: ②<u>Neither have I</u>. Oh, look! ③<u>Here comes the bus</u> at last.\nA: ④<u>Seldom I have felt so tired</u> after a long day.\nB: ⑤<u>So strong is the wind</u> that we can hardly walk straight.", why=LENP)
L(1, 124, "E", okdup=True, p="A: ①<u>I have rarely tasted such spicy food</u> at a restaurant.\nB: ②<u>Neither have I</u>. ③<u>Here comes our order</u> right now.\nA: ④<u>Never I will eat this again</u> in my life.\nB: ⑤<u>So hot is the soup</u> that my eyes are watering already.", why=LENP)
L(1, 124, "F", p="A: ①<u>I have never seen such a long line</u> at this bus stop.\nB: ②<u>Neither have I</u>. ③<u>Here comes another bus</u> over there.\nA: ④<u>Rarely I have waited this long</u> for a bus.\nB: ⑤<u>So crowded is the street</u> that traffic has completely stopped.", why=LENP)

# 1-128 D·E·F
L(1, 128, "D", p="- On the hill near our village ________ an old castle.\n- There ________ many tourists near the main gate today.")
L(1, 128, "E", p="- At the end of this narrow road ________ a small cafe.\n- There ________ several cars parked outside the cafe.")
L(1, 128, "F", p="- Behind the tall office building ________ three delivery trucks.\n- There ________ a narrow alley right beside it.")

# 1-130 E: 보기 설명을 원문항처럼 길게, 정답 설명은 원문항 문장을 되풀이하지 않게 예를 들어
RE(1, 130, "E", c=["비교 구문(than, as ~ as)은 병렬구조와 관계가 없으므로, 비교 대상이 되는 두 요소의 형태는 자유롭게 쓸 수 있다.", "to부정사 두 개가 and로 이어질 때 두 번째 to는 반드시 반복해서 써야 하며, 생략하면 병렬구조가 깨진다.", "동명사와 to부정사는 뜻이 비슷하므로, 등위접속사 and로 둘을 섞어서 연결해도 병렬구조로 인정된다.", "상관접속사 not only A but also B에서 also는 반드시 생략해야 A와 B가 병렬을 이룬다.", "I like swimming more than to run.이 틀린 이유는 than 앞뒤의 비교 대상이 문법적으로 대등한 형태가 아니기 때문이다."], a=5,
   n=OKS(["비교 구문으로 이어진 두 요소도 같은 형태여야 한다. 옳지 않은 설명이므로", "to부정사가 이어질 때 두 번째 to는 생략할 수 있다. 옳지 않은 설명이므로", "동명사와 to부정사를 섞어 이으면 병렬구조가 깨진다. 옳지 않은 설명이므로", "not only A but also B의 also는 생략할 수 있을 뿐 반드시 생략하는 것은 아니다. 옳지 않은 설명이므로", "than 앞이 동명사(swimming)이므로 뒤도 running이어야 한다. 옳은 설명이므로"], 5),
   s=ADD(1, 130, "E", MEMO6 + "보기 설명이 원문항보다 짧아 원문항처럼 근거를 붙여 늘렸다. 정답 설명은 원문항 문장을 되풀이하지 않게 예문을 들어 썼다." + pos(5)))

# ---- 점검 뒤 보완: 아직 원문항보다 짧던 것 ----
RE(1, 69, "D", p="Since no buses were running late at night, Mina called a taxi.")
RE(1, 69, "F", p="Since no lights were on in the house, Jane assumed nobody was home.")
RE(1, 86, "D", p="I know the reason for which Mina left the birthday party so early last night.",
   c=[x.replace("left the party early last night", "left the birthday party so early last night") for x in OLD(1, 86, "D")["c"]])
RE(1, 86, "E", p="Friday is the day on which our book club meets in the music room after school.",
   c=[x.replace("the club meets", "our book club meets") for x in OLD(1, 86, "E")["c"]])
RE(1, 86, "F", p="This is the small town in which Jane grew up with her grandparents as a child.",
   c=[x.replace("the town", "the small town") for x in OLD(1, 86, "F")["c"]])
RE(1, 128, "F", p="- Behind the tall office building downtown ________ three delivery trucks.\n- There ________ a narrow alley right beside it.")
INV = "도치가 맞으므로"
def F124(t, c, p, ans_note, k):
    c0 = c[0]; first = "never" if "never" in c0 else "rarely"
    nn = [f"부정어 {first}가 문장 중간에 있어 도치하지 않는 일반 어순이 맞으므로", f"Neither + 조동사 + 주어(Neither have I)의 {INV}", f"Here comes + 명사 주어의 {INV}", ans_note, f"So + 형용사 + be동사 + 주어 + that 구문의 {INV}"]
    RE(1, 124, t, p=p, c=c, a=4, okdup=True, k=k, n=OKS(nn, 4), s=ADD(1, 124, t, MEMO6 + "원문항처럼 밑줄을 절 전체로 넓히고 대화를 원문항 길이 이상으로 늘렸다. 정답 위치는 그대로다."))
F124("D", ["I have never experienced such cold weather in my whole life", "Neither have I", "Here comes the bus at last", "Seldom I have felt so tired after a long day", "So strong is the wind that we can hardly walk"],
     "A: ①<u>I have never experienced such cold weather in my whole life</u>.\nB: ②<u>Neither have I</u>. Oh, look! ③<u>Here comes the bus at last</u>.\nA: ④<u>Seldom I have felt so tired after a long day</u>.\nB: ⑤<u>So strong is the wind that we can hardly walk</u> straight.",
     "부정어 Seldom이 문장 맨 앞에 오면 조동사를 주어 앞으로 보내야 한다. Seldom have I felt so tired로 고쳐야 하므로", "부정어 Seldom이 문장 맨 앞에 와서 조동사 have를 주어 I 앞으로 보내야 하므로")
F124("E", ["I have rarely tasted such spicy food at a restaurant", "Neither have I", "Here comes our order right now", "Never I will eat this again in my life", "So hot is the soup that my eyes are watering"],
     "A: ①<u>I have rarely tasted such spicy food at a restaurant</u>.\nB: ②<u>Neither have I</u>. ③<u>Here comes our order right now</u>.\nA: ④<u>Never I will eat this again in my life</u>.\nB: ⑤<u>So hot is the soup that my eyes are watering</u> already.",
     "부정어 Never가 문장 맨 앞에 오면 조동사를 주어 앞으로 보내야 한다. Never will I eat this again으로 고쳐야 하므로", "부정어 Never가 문장 맨 앞에 와서 조동사 will을 주어 I 앞으로 보내야 하므로")
F124("F", ["I have never seen such a long line at this bus stop", "Neither have I", "Here comes another bus over there", "Rarely I have waited this long for a bus", "So crowded is the street that traffic has stopped"],
     "A: ①<u>I have never seen such a long line at this bus stop</u>.\nB: ②<u>Neither have I</u>. ③<u>Here comes another bus over there</u>.\nA: ④<u>Rarely I have waited this long for a bus</u>.\nB: ⑤<u>So crowded is the street that traffic has stopped</u> completely.",
     "준부정어 Rarely가 문장 맨 앞에 오면 조동사를 주어 앞으로 보내야 한다. Rarely have I waited this long으로 고쳐야 하므로", "준부정어 Rarely가 문장 맨 앞에 와서 조동사 have를 주어 I 앞으로 보내야 하므로")
RE(1, 86, "D", p=OLD(1, 86, "D")["p"].replace("the reason", "the real reason"), c=[x.replace("the reason", "the real reason") for x in OLD(1, 86, "D")["c"]])
