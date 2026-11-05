# 2026-10-23 C 유형 감수(1·2·3·5·6·7급) 반영: 검토 페이지 ‘부적합’ C 문항 44개(2급 12·3급 32)와 같은 문항의 D·E·F.
# 규칙: 확인 완료 문서는 건드리지 않는다(2-64·3-95 C는 확인 완료지만 부적합 판정이라 고침). 메모 대부분이 ‘원문항보다 짧다’라서 C뿐 아니라
# D·E·F도 원문항 길이 이상으로 늘렸고, 메모가 가리킨 다른 결함(강조 어구, 밑줄 범위, 복수 정답, 선택지 순서, be + -ing 단서)도 같은 문항의 다른 유형까지 살폈다.
MEMO4 = "감수 메모 반영(10-23 C): "
def OKS(items, a): return [w + OK(i + 1, a) for i, w in enumerate(items)]
def ADD(g_, n_, t_, more): return (OLD(g_, n_, t_).get("s", "") + " " + more).strip()
def PJ(*lines): return ["문장별 판정: " + l for l in lines]
CNT = ["1개", "2개", "3개", "4개", "5개"]; CNT2 = ["2개", "3개", "4개", "5개", "6개"]
LEN = MEMO4 + "원문항보다 짧던 문장을 원문항 길이 이상으로 늘렸다. 틀린 곳과 정답은 그대로다."
LENP = MEMO4 + "원문항보다 짧던 지문을 원문항 길이 이상으로 늘렸다. 보기와 정답은 그대로다."

# ---- 2-13: 보기 문장을 원문항 길이(8~11 낱말)로 ----
R13 = "현재완료·과거완료는 have/has/had + 과거분사(p.p.)로 만든다. 불규칙동사는 과거형과 과거분사형이 다를 수 있으므로 각각 확인한다."
def G13(aux, b, pa, pp): return f"{aux} {pp}: 과거분사를 바르게 썼다({b}-{pa}-{pp}). 어색하지 않으므로"
def B13(aux, b, pa, pp): return f"{aux} {pa}: 과거분사 자리에 과거형을 썼다({b}-{pa}-{pp}). {aux} {pp}(으)로 고쳐야 하는 어색한 곳이므로"
RE(2, 13, "C", c=["I have <u>broken</u> the school rule only once this year.", "They have <u>spoken</u> to the new teacher about the problem.", "Tom has <u>driven</u> this old car since he was twenty.", "I have <u>wrote</u> to her several times since last spring.", "We have <u>thrown</u> away all the old boxes in the garage."], a=4, r=R13,
   n=OKS([G13("have", "break", "broke", "broken"), G13("have", "speak", "spoke", "spoken"), G13("has", "drive", "drove", "driven"), B13("have", "write", "wrote", "written"), G13("have", "throw", "threw", "thrown")], 4), s=ADD(2, 13, "C", LEN))
RE(2, 13, "D", c=["We have <u>made</u> great progress on the science project this month.", "Jane has <u>lent</u> me a book about famous Korean painters.", "She has <u>gave</u> me useful advice about my future career.", "He has <u>known</u> her since they were in elementary school.", "They have <u>taken</u> the same test twice this semester."], a=3, r=R13,
   n=OKS([G13("have", "make", "made", "made"), G13("has", "lend", "lent", "lent"), B13("has", "give", "gave", "given"), G13("has", "know", "knew", "known"), G13("have", "take", "took", "taken")], 3), s=ADD(2, 13, "D", LEN))
RE(2, 13, "E", c=["Tom has <u>come</u> to school early every day this week.", "They have <u>chosen</u> a new leader for the student council.", "She has <u>drawn</u> a picture of her grandmother's old house.", "I have <u>ridden</u> a horse only once in my whole life.", "We have <u>took</u> the same bus to school for three years."], a=5, r=R13,
   n=OKS([G13("has", "come", "came", "come"), G13("have", "choose", "chose", "chosen"), G13("has", "draw", "drew", "drawn"), G13("have", "ride", "rode", "ridden"), B13("have", "take", "took", "taken")], 5), s=ADD(2, 13, "E", LEN))
RE(2, 13, "F", c=["Tom has <u>chose</u> a different topic for his science report.", "She has <u>drunk</u> enough water during the long race today.", "They have <u>done</u> all the work before the deadline.", "We have <u>grown</u> tomatoes in our garden this year.", "I have <u>found</u> my keys under the sofa in the living room."], a=1, r=R13,
   n=OKS([B13("has", "choose", "chose", "chosen"), G13("has", "drink", "drank", "drunk"), G13("have", "do", "did", "done"), G13("have", "grow", "grew", "grown"), G13("have", "find", "found", "found")], 1), s=ADD(2, 13, "F", LEN))

# ---- 2-15: a)~f) 문장을 원문항 길이(52낱말) 이상으로, 선택지 2개~6개 ----
R15 = "will 뒤에는 동사원형을 쓰고, 현재완료(have/has + 과거분사)는 yesterday, last night처럼 끝난 과거 시점을 나타내는 말과 함께 쓰지 않는다. 과거의 어느 때보다 먼저 일어난 일은 과거완료(had + 과거분사)로 쓰고, 복수 주어의 현재완료는 have로 쓴다."
L15 = MEMO4 + "원문항보다 짧던 문장을 원문항 길이 이상으로 늘리고 선택지를 2개~6개 순으로 두었다. 틀린 곳과 정답 개수는 그대로다."
RE(2, 15, "C", p="a) We <u>are leaving</u> for the airport early tonight.\nb) I <u>have seen</u> that famous movie three times with my friends.\nc) Tom <u>had eaten</u> all the sandwiches before the class began.\nd) She <u>will studies</u> abroad in Canada after she graduates.\ne) They <u>have lived</u> in this small town since 2021.\nf) Jane <u>has called</u> me about the homework last night.",
   c=CNT2, a=3, r=R15, pre=PJ("a) O. 가까운 예정을 나타내는 현재진행형이다.", "b) O. three times와 함께 쓴 경험의 현재완료이다.", "c) O. 수업이 시작된 것보다 먼저 먹었으므로 과거완료이다.", "d) X. will 뒤에는 동사원형을 쓴다. 교정문: She will study abroad in Canada after she graduates.", "e) O. since 2021과 함께 쓴 계속의 현재완료이다.", "f) X. last night이라는 끝난 과거 시점에는 과거형을 쓴다. 교정문: Jane called me about the homework last night."),
   k="밑줄 친 부분이 옳은 문장은 a), b), c), e)로 4개이다.", n="cnt", s=ADD(2, 15, "C", L15))
RE(2, 15, "D", p="a) He <u>is flying</u> to Busan to see his grandparents tomorrow.\nb) We <u>have finished</u> the group project for our history class.\nc) Jane <u>had gone</u> home before I called her last night.\nd) Tom <u>will be</u> late for the meeting because of the traffic.\ne) They <u>has lived</u> in this apartment for ten years.\nf) I <u>met</u> him at the bus stop yesterday morning.",
   c=CNT2, a=4, r=R15, pre=PJ("a) O. tomorrow의 예정된 이동을 나타내는 현재진행형이다.", "b) O. 끝낸 결과를 나타내는 현재완료이다.", "c) O. 전화한 것보다 먼저 집에 갔으므로 과거완료이다.", "d) O. will 뒤에 동사원형 be를 썼다.", "e) X. 복수 주어 They에는 have를 쓴다. 교정문: They have lived in this apartment for ten years.", "f) O. yesterday morning이라는 과거 시점에 과거형 met을 썼다."),
   k="밑줄 친 부분이 옳은 문장은 a), b), c), d), f)로 5개이다.", n="cnt", s=ADD(2, 15, "D", L15))
RE(2, 15, "E", p="a) I <u>am having</u> lunch with Mina at the new restaurant tomorrow.\nb) She <u>has been</u> to Rome once with her parents.\nc) We <u>had started</u> the meeting before he arrived at the office.\nd) Tom <u>will comes</u> to the party later with his cousin.\ne) Jane <u>has worked</u> at this bakery since last May.\nf) They <u>saw</u> the school play in the gym last week.",
   c=CNT2, a=4, r=R15, pre=PJ("a) O. tomorrow의 잡혀 있는 약속을 나타내는 현재진행형이다.", "b) O. once와 함께 쓴 경험의 현재완료이다.", "c) O. 그가 도착한 것보다 먼저 시작했으므로 과거완료이다.", "d) X. will 뒤에는 동사원형을 쓴다. 교정문: Tom will come to the party later with his cousin.", "e) O. since last May와 함께 쓴 계속의 현재완료이다.", "f) O. last week이라는 과거 시점에 과거형 saw를 썼다."),
   k="밑줄 친 부분이 옳은 문장은 a), b), c), e), f)로 5개이다.", n="cnt", s=ADD(2, 15, "E", L15))
RE(2, 15, "F", p="a) They <u>are visiting</u> us at our new house this weekend.\nb) I <u>have lost</u> my keys somewhere in the school library.\nc) Tom <u>had finished</u> his lunch before noon on Saturday.\nd) Jane <u>will call</u> you tonight about the science homework.\ne) We <u>have lived</u> in this city for ten years.\nf) He <u>has met</u> me at the museum yesterday.",
   c=CNT2, a=4, r=R15, pre=PJ("a) O. this weekend의 예정된 방문을 나타내는 현재진행형이다.", "b) O. 잃어버려 지금도 없는 결과를 나타내는 현재완료이다.", "c) O. 정오라는 과거 기준보다 먼저 끝냈으므로 과거완료이다.", "d) O. will 뒤에 동사원형 call을 썼다.", "e) O. for ten years와 함께 쓴 계속의 현재완료이다.", "f) X. yesterday라는 끝난 과거 시점에는 과거형을 쓴다. 교정문: He met me at the museum yesterday."),
   k="밑줄 친 부분이 옳은 문장은 a), b), c), d), e)로 5개이다.", n="cnt", s=ADD(2, 15, "F", L15))

# ---- 2-27: 강조 어구(actually·really·truly)가 없는 문장으로 ----
R27 = "동사를 강조할 때는 do/does/did + 동사원형을 쓴다. 시제와 인칭은 do/does/did가 나타내고 뒤의 동사는 원형으로 쓴다."
L27 = MEMO4 + "원래 문장에 actually·really·truly 같은 강조 어구가 있어 이미 강조된 느낌이었다. 강조 어구가 없는 문장으로 바꿨다."
RE(2, 27, "C", p="Tom called me last night.", c=["Tom did call me last night.", "Tom had call me last night.", "Tom was call me last night.", "Tom did called me last night.", "Tom does call me last night."], a=1, r=R27,
   n=OKS(["did + 동사원형 call로 과거의 동작을 바르게 강조했으므로", "had는 동사를 강조하는 조동사가 아니고 뒤에 동사원형도 올 수 없으므로", "was는 동사를 강조하지 못하고 뒤에 동사원형도 올 수 없으므로", "did 뒤에 과거형 called를 쓸 수 없으므로", "last night이 있는 과거 문장에 does를 쓸 수 없으므로"], 1), s=L27 + pos(1))
RE(2, 27, "D", p="They solve difficult problems quickly.", c=["They are solve difficult problems quickly.", "They does solve difficult problems quickly.", "They do solve difficult problems quickly.", "They do solves difficult problems quickly.", "They did solve difficult problems quickly."], a=3, r=R27,
   n=OKS(["are는 동사를 강조하지 못하고 뒤에 동사원형도 올 수 없으므로", "주어 They에는 does를 쓸 수 없으므로", "do + 동사원형 solve로 현재의 동작을 바르게 강조했으므로", "do 뒤에 solves를 쓸 수 없으므로", "현재형 문장을 과거의 did로 강조하면 시제가 달라지므로"], 3), s=L27 + pos(3))
RE(2, 27, "E", p="Jane understands the whole issue.", c=["Jane is understand the whole issue.", "Jane do understand the whole issue.", "Jane does understand the whole issue.", "Jane does understands the whole issue.", "Jane did understand the whole issue."], a=3, r=R27,
   n=OKS(["is는 동사를 강조하지 못하고 뒤에 동사원형도 올 수 없으므로", "3인칭 단수 주어 Jane에는 does를 써야 하므로", "does + 동사원형 understand로 현재의 동작을 바르게 강조했으므로", "does 뒤에 understands를 쓸 수 없으므로", "현재형 문장을 과거의 did로 강조하면 시제가 달라지므로"], 3), s=L27 + pos(3))
RE(2, 27, "F", p="I want to help you.", c=["I did want to help you.", "I does want to help you.", "I do want to help you.", "I am want to help you.", "I do wants to help you."], a=3, r=R27,
   n=OKS(["현재형 문장을 과거의 did로 강조하면 시제가 달라지므로", "주어 I에는 does를 쓸 수 없으므로", "do + 동사원형 want로 현재의 동작을 바르게 강조했으므로", "am은 동사를 강조하지 못하고 뒤에 동사원형도 올 수 없으므로", "do 뒤에 wants를 쓸 수 없으므로"], 3), s=L27 + pos(3))

# ---- 2-40: ⓐ~ⓕ 문장을 원문항 길이(52낱말) 이상으로 ----
L40 = MEMO4 + "원문항보다 짧고 단조롭던 문장을 원문항 길이 이상으로 늘렸다. 틀린 곳과 정답 개수는 그대로다."
RE(2, 40, "C", p="ⓐ The room is being painted by two workers right now.\nⓑ Tom was made to apologize to his sister by his mother.\nⓒ The letters have been sent to all the members already.\nⓓ The new bridge is being build across the wide river.\nⓔ Jane was seen dancing on the stage by her classmates.\nⓕ The meeting will be held in the main hall tomorrow.",
   pre=PJ("ⓐ O. 진행 수동태(is being painted)이다.", "ⓑ O. make의 원형부정사 보어가 수동태에서 to부정사(to apologize)가 되었다.", "ⓒ O. 완료 수동태(have been sent)이다.", "ⓓ X. being 뒤에는 과거분사를 쓴다. 교정문: The new bridge is being built across the wide river.", "ⓔ O. 지각동사의 현재분사 보어(dancing)를 수동태에서 그대로 두었다.", "ⓕ O. 미래 수동태(will be held)이다."), s=ADD(2, 40, "C", L40))
RE(2, 40, "D", p="ⓐ The old car has been repaired by my uncle this week.\nⓑ The front door was being open when I arrived home.\nⓒ The little boy was heard sing in the next room.\nⓓ These books were wrote by a famous writer from Busan.\nⓔ The trees are being plant along the river by students.\nⓕ The chocolate cake was ate by my little brother.",
   pre=PJ("ⓐ O. 완료 수동태(has been repaired)이다.", "ⓑ X. being 뒤에는 과거분사를 쓴다. 교정문: The front door was being opened when I arrived home.", "ⓒ X. 지각동사의 원형부정사 보어는 수동태에서 to부정사가 된다. 교정문: The little boy was heard to sing in the next room.", "ⓓ X. 수동태에는 과거분사를 쓴다. 교정문: These books were written by a famous writer from Busan.", "ⓔ X. being 뒤에는 과거분사를 쓴다. 교정문: The trees are being planted along the river by students.", "ⓕ X. 수동태에는 과거분사를 쓴다. 교정문: The chocolate cake was eaten by my little brother."), s=ADD(2, 40, "D", L40))
RE(2, 40, "E", p="ⓐ The final report will be finished by our team tomorrow.\nⓑ The narrow road is being widen for the new buses.\nⓒ The child was made clean the messy room by his father.\nⓓ The package has been delivered to the wrong address again.\nⓔ This beautiful song was sung by Mina at the concert.\nⓕ The baby is being looked after her aunt this week.",
   pre=PJ("ⓐ O. 미래 수동태(will be finished)이다.", "ⓑ X. being 뒤에는 과거분사를 쓴다. 교정문: The narrow road is being widened for the new buses.", "ⓒ X. make의 원형부정사 보어는 수동태에서 to부정사가 된다. 교정문: The child was made to clean the messy room by his father.", "ⓓ O. 완료 수동태(has been delivered)이다.", "ⓔ O. 단순과거 수동태(was sung)이다.", "ⓕ X. look after의 after를 그대로 두고 행위자 앞에 by를 쓴다. 교정문: The baby is being looked after by her aunt this week."), s=ADD(2, 40, "E", L40))
RE(2, 40, "F", p="ⓐ A new house is being built next to the old church.\nⓑ My father's car was repair at the garage yesterday.\nⓒ The student was seen running across the playground after school.\nⓓ The thank-you letter has been wrote by the whole class.\nⓔ The repair work will completed before the winter comes.\nⓕ Jane was made to waiting outside in the cold.",
   pre=PJ("ⓐ O. 진행 수동태(is being built)이다.", "ⓑ X. 수동태에는 과거분사를 쓴다. 교정문: My father's car was repaired at the garage yesterday.", "ⓒ O. 지각동사의 현재분사 보어(running)를 수동태에서 그대로 두었다.", "ⓓ X. 완료 수동태에는 과거분사를 쓴다. 교정문: The thank-you letter has been written by the whole class.", "ⓔ X. 미래 수동태는 will be + 과거분사이다. 교정문: The repair work will be completed before the winter comes.", "ⓕ X. to부정사의 to 뒤에는 동사원형을 쓴다. 교정문: Jane was made to wait outside in the cold."), s=ADD(2, 40, "F", L40))

# ---- 2-64: 밑줄 범위를 원문항처럼 ‘to + 동사’까지로 통일(오답은 모두 to부정사), 문장 길이도 ----
R64 = "전치사 뒤에는 명사나 동명사를 쓰며 to부정사를 쓰지 않는다. look forward to·be used to의 to도 전치사이므로 뒤에 동명사를 쓴다."
L64 = MEMO4 + "밑줄 범위를 원문항처럼 ‘to + 동사’까지로 통일하고(오답은 모두 to부정사), 원문항보다 짧던 문장을 늘렸다. 정답 위치는 그대로다."
RE(2, 64, "C", c=["He is afraid of <u>to fly</u> alone at night.", "Thank you for <u>to invite</u> me to your birthday party.", "She left the room without <u>to say</u> a single word.", "Tom succeeded in <u>solving</u> the difficult puzzle at last.", "I'm used <u>to get</u> up early in the morning."], a=4, r=R64,
   n=OKS(["전치사 of 뒤에는 to부정사가 아니라 동명사 flying을 써야 하므로", "전치사 for 뒤에는 동명사 inviting을 써야 하므로", "전치사 without 뒤에는 동명사 saying을 써야 하므로", "전치사 in 뒤에 동명사 solving을 바르게 썼으므로", "be used to의 to는 전치사라 동명사 getting을 써야 하므로"], 4), s=ADD(2, 64, "C", L64))
RE(2, 64, "D", c=["We talked about <u>to go</u> camping by the lake this summer.", "We are interested in <u>learning</u> French at the community center.", "He is proud of <u>to win</u> the first prize in the contest.", "I'm sorry for <u>to call</u> you so late last night.", "They are excited about <u>to visit</u> Jeju Island next month."], a=2, r=R64,
   n=OKS(["전치사 about 뒤에는 동명사 going을 써야 하므로", "전치사 in 뒤에 동명사 learning을 바르게 썼으므로", "전치사 of 뒤에는 동명사 winning을 써야 하므로", "전치사 for 뒤에는 동명사 calling을 써야 하므로", "전치사 about 뒤에는 동명사 visiting을 써야 하므로"], 2), s=ADD(2, 64, "D", L64))
RE(2, 64, "E", c=["He left the room without <u>to close</u> the door behind him.", "How about <u>to take</u> a taxi to the airport instead?", "Jane apologized for <u>being</u> late for the important meeting.", "I'm worried about <u>to lose</u> my part-time job next month.", "She is fond of <u>to read</u> poems before going to bed."], a=3, r=R64,
   n=OKS(["전치사 without 뒤에는 동명사 closing을 써야 하므로", "전치사 about 뒤에는 동명사 taking을 써야 하므로", "전치사 for 뒤에 동명사 being을 바르게 썼으므로", "전치사 about 뒤에는 동명사 losing을 써야 하므로", "전치사 of 뒤에는 동명사 reading을 써야 하므로"], 3), s=ADD(2, 64, "E", L64))
RE(2, 64, "F", c=["He kept me from <u>making</u> a serious mistake on the test.", "Instead of <u>to take</u> the bus, we walked to the station.", "I dream of <u>to become</u> a pilot and flying around the world.", "She is capable of <u>to run</u> a full marathon in four hours.", "Before <u>to eat</u> dinner, wash your hands with soap."], a=1, r=R64,
   n=OKS(["전치사 from 뒤에 동명사 making을 바르게 썼으므로", "전치사 of 뒤에는 동명사 taking을 써야 하므로", "전치사 of 뒤에는 동명사 becoming을 써야 하므로", "전치사 of 뒤에는 동명사 running을 써야 하므로", "전치사 before 뒤에는 동명사 eating을 써야 하므로"], 1), s=ADD(2, 64, "F", L64))

# ---- 2-65: ⓐ~ⓕ 문장을 원문항 길이(46낱말) 이상으로 ----
RE(2, 65, "C", p="ⓐ This book is worth to read again during the winter holidays.\nⓑ She avoided answering the question about her new job.\nⓒ We finished to clean the classroom before the bell rang.\nⓓ I object to pay extra money for the late delivery.\nⓔ Tom kept working on his essay until late at night.\nⓕ He gave up to smoke after he became a father.",
   pre=PJ("ⓐ X. be worth 뒤에는 동명사를 쓴다. 교정문: This book is worth reading again during the winter holidays.", "ⓑ O. avoid는 동명사를 목적어로 쓴다.", "ⓒ X. finish는 동명사를 목적어로 쓴다. 교정문: We finished cleaning the classroom before the bell rang.", "ⓓ X. object to의 to는 전치사라 동명사를 쓴다. 교정문: I object to paying extra money for the late delivery.", "ⓔ O. keep은 동명사를 목적어로 쓴다.", "ⓕ X. give up은 동명사를 목적어로 쓴다. 교정문: He gave up smoking after he became a father."), s=ADD(2, 65, "C", LEN))
RE(2, 65, "D", p="ⓐ I cannot help laughing whenever I watch that funny show.\nⓑ Jane admitted to break the vase in the living room.\nⓒ The new movie is worth to watch more than once.\nⓓ We are used to get up early on school days.\nⓔ He gave up smoke for the sake of his children.\nⓕ Would you mind to open the window for a minute?",
   pre=PJ("ⓐ O. cannot help -ing이다.", "ⓑ X. admit는 동명사를 목적어로 쓴다(admit to는 전치사 to + 동명사). 교정문: Jane admitted breaking the vase in the living room.", "ⓒ X. be worth 뒤에는 동명사를 쓴다. 교정문: The new movie is worth watching more than once.", "ⓓ X. be used to의 to는 전치사라 동명사를 쓴다. 교정문: We are used to getting up early on school days.", "ⓔ X. give up은 동명사를 목적어로 쓴다. 교정문: He gave up smoking for the sake of his children.", "ⓕ X. mind는 동명사를 목적어로 쓴다. 교정문: Would you mind opening the window for a minute?"), s=ADD(2, 65, "D", LEN))
RE(2, 65, "E", p="ⓐ Tom enjoys to cook Italian food for his family on weekends.\nⓑ She is busy preparing dinner for the guests tonight.\nⓒ We prevented him from leave the party too early.\nⓓ I feel like to take a long walk along the river.\nⓔ The old problem needs solving as soon as possible.\nⓕ They practiced to dance for hours before the school festival.",
   pre=PJ("ⓐ X. enjoy는 동명사를 목적어로 쓴다. 교정문: Tom enjoys cooking Italian food for his family on weekends.", "ⓑ O. be busy -ing이다.", "ⓒ X. 전치사(from) 뒤에는 동명사를 쓴다. 교정문: We prevented him from leaving the party too early.", "ⓓ X. feel like 뒤에는 동명사를 쓴다. 교정문: I feel like taking a long walk along the river.", "ⓔ O. need -ing은 ‘~될 필요가 있다’는 수동의 뜻이다.", "ⓕ X. practice는 동명사를 목적어로 쓴다. 교정문: They practiced dancing for hours before the school festival."), s=ADD(2, 65, "E", LEN))
RE(2, 65, "F", p="ⓐ Jane denied to cheat on the final exam last week.\nⓑ I am looking forward to seeing you at the party.\nⓒ Tom stopped smoking because it was bad for his health.\nⓓ She succeeded in passing the difficult driving test.\nⓔ We cannot help smiling at the cute little baby.\nⓕ He suggested to go on a picnic by the river.",
   pre=PJ("ⓐ X. deny는 동명사를 목적어로 쓴다. 교정문: Jane denied cheating on the final exam last week.", "ⓑ O. look forward to + 동명사이다.", "ⓒ O. stop -ing은 ‘~하던 것을 그만두다’이다.", "ⓓ O. 전치사(in) 뒤 동명사이다.", "ⓔ O. cannot help -ing이다.", "ⓕ X. suggest는 동명사를 목적어로 쓴다. 교정문: He suggested going on a picnic by the river."), s=ADD(2, 65, "F", LEN))

# ---- 2-69: 문장을 원문항 길이(22낱말)로, 보기도 원문항처럼 긴 동사구로 ----
R69 = "remember(forget) + 동명사는 ‘이미 한 일을 기억하다(잊다)’, remember(forget) + to부정사는 ‘앞으로 할 일을 기억하다(잊다)’는 뜻이다."
L69 = MEMO4 + "원문항보다 짧던 문장을 원문항 길이 이상으로 늘리고 보기도 원문항처럼 긴 동사구로 했다. 정답 위치는 그대로다."
RE(2, 69, "C", p="Jane clearly remembers (A)________ Tom at the airport years ago, but she has forgotten his phone number.\nPlease don't forget (B)________ today, Jane, because he is waiting for your answer.",
   c=["(A) to meet - (B) calling him back", "(A) met - (B) call him back", "(A) meeting - (B) calling him back", "(A) to meet - (B) to call him back", "(A) meeting - (B) to call him back"], a=5, r=R69,
   k="(A)는 years ago가 있어 이미 한 일, (B)는 today가 있어 앞으로 할 일이다.",
   n=OKS(["(A) to meet: 이미 한 일(years ago)이라 동명사 meeting을 써야 하므로", "(A) met, (B) call him back: remember·forget 뒤에 과거형이나 동사원형을 쓸 수 없으므로", "(B) calling him back: 앞으로 할 일(today)이라 to부정사 to call him back을 써야 하므로", "(A) to meet: 이미 한 일이라 동명사 meeting을 써야 하므로", "(A)는 이미 한 일이라 동명사 meeting, (B)는 앞으로 할 일이라 to부정사 to call him back이 알맞으므로"], 5), s=ADD(2, 69, "C", L69))
RE(2, 69, "D", p="I still remember (A)________ this museum with my grandfather when I was a child.\nRemember (B)________ before you go there, because the line is always very long.",
   c=["(A) visited - (B) book the tickets", "(A) to visit - (B) to book the tickets", "(A) visiting - (B) to book the tickets", "(A) to visit - (B) booking the tickets", "(A) visiting - (B) booking the tickets"], a=3, r=R69,
   k="(A)는 when I was a child가 있어 이미 한 일, (B)는 before you go there가 있어 앞으로 할 일이다.",
   n=OKS(["(A) visited, (B) book the tickets: remember 뒤에 과거형이나 동사원형을 쓸 수 없으므로", "(A) to visit: 이미 한 일(when I was a child)이라 동명사 visiting을 써야 하므로", "(A)는 이미 한 일이라 동명사 visiting, (B)는 앞으로 할 일이라 to부정사 to book the tickets가 알맞으므로", "(A) to visit: 이미 한 일이라 동명사 visiting을, (B) booking the tickets: 앞으로 할 일이라 to부정사를 써야 하므로", "(B) booking the tickets: 앞으로 할 일(before you go there)이라 to부정사 to book the tickets를 써야 하므로"], 3), s=ADD(2, 69, "D", L69))
RE(2, 69, "E", p="Tom clearly remembers (A)________ the email to his teacher yesterday afternoon, but he forgot the attachment.\nHe must remember (B)________ next time, or his teacher will not get the file.",
   c=["(A) sending - (B) including the file", "(A) to send - (B) to include the file", "(A) sending - (B) to include the file", "(A) to send - (B) including the file", "(A) sent - (B) include the file"], a=3, r=R69,
   k="(A)는 yesterday afternoon이 있어 이미 한 일, (B)는 next time이 있어 앞으로 할 일이다.",
   n=OKS(["(B) including the file: 앞으로 할 일(next time)이라 to부정사 to include the file을 써야 하므로", "(A) to send: 이미 한 일(yesterday afternoon)이라 동명사 sending을 써야 하므로", "(A)는 이미 한 일이라 동명사 sending, (B)는 앞으로 할 일이라 to부정사 to include the file이 알맞으므로", "(A) to send: 이미 한 일이라 동명사 sending을, (B) including the file: 앞으로 할 일이라 to부정사를 써야 하므로", "(A) sent, (B) include the file: remember 뒤에 과거형이나 동사원형을 쓸 수 없으므로"], 3), s=ADD(2, 69, "E", L69))
RE(2, 69, "F", p="We clearly remember (A)________ here with our parents before, so we know the way.\nRemember (B)________ and lock the door when you leave the room tonight.",
   c=["(A) coming - (B) turning off the lights", "(A) came - (B) turn off the lights", "(A) to come - (B) turning off the lights", "(A) coming - (B) to turn off the lights", "(A) to come - (B) to turn off the lights"], a=4, r=R69,
   k="(A)는 before가 있어 이미 한 일, (B)는 when you leave가 있어 앞으로 할 일이다.",
   n=OKS(["(B) turning off the lights: 앞으로 할 일(when you leave)이라 to부정사를 써야 하므로", "(A) came, (B) turn off the lights: remember 뒤에 과거형이나 동사원형을 쓸 수 없으므로", "(A) to come: 이미 한 일(before)이라 동명사 coming을, (B) turning off the lights: 앞으로 할 일이라 to부정사를 써야 하므로", "(A)는 이미 한 일이라 동명사 coming, (B)는 앞으로 할 일이라 to부정사 to turn off the lights가 알맞으므로", "(A) to come: 이미 한 일이라 동명사 coming을 써야 하므로"], 4), s=ADD(2, 69, "F", L69))

# ---- 2-85: 대화와 밑줄 표현을 원문항 길이(61낱말, 밑줄 평균 7낱말)로 ----
L85 = MEMO4 + "원문항보다 짧던 대화와 밑줄 표현을 원문항 길이 이상으로 늘렸다. 정답 위치는 그대로다."
RE(2, 85, "C", p="A: Mina is ①<u>the most diligent student in our class</u>, isn't she?\nB: I agree. She studies ②<u>harder than anyone else in the whole school</u>.\nA: She is also ③<u>much kinder than most of her classmates</u>, I think.\nB: That's true. ④<u>No other student is as kind as Mina</u> in our grade.\nA: And she's ⑤<u>the most smartest girl I have ever met</u>, too.",
   c=["the most diligent student in our class", "harder than anyone else in the whole school", "much kinder than most of her classmates", "No other student is as kind as Mina", "the most smartest girl I have ever met"], a=5,
   n=OKS(["the most + 원급의 바른 최상급이므로", "비교급 + than anyone else(최상급의 뜻)의 바른 형태이므로", "much로 강조한 비교급 kinder than의 바른 형태이므로", "No other + 단수명사 + as + 원급 + as(최상급의 뜻)의 바른 형태이므로", "smart의 최상급은 the smartest다. most와 -est를 겹쳐 쓸 수 없으므로"], 5), k="the smartest로 써야 하는데 most와 -est를 겹쳐 썼다.", s=ADD(2, 85, "C", L85))
RE(2, 85, "D", p="A: Of the three bags on the table, which one is ①<u>the heaviest of all three</u>?\nB: The black one, I think. It's ②<u>twice as heavy as the red one</u>.\nA: Really? The red one looks ③<u>more heavier than the black one</u> to me.\nB: No, it's ④<u>much lighter than it looks</u>. Try lifting it yourself.\nA: You're right. Then I'll take ⑤<u>the lightest one of the three</u> for the trip.",
   c=["the heaviest of all three", "twice as heavy as the red one", "more heavier than the black one", "much lighter than it looks", "the lightest one of the three"], a=3,
   n=OKS(["셋 중 가장 무거운 것이라 the + -est의 바른 최상급이므로", "배수 + as + 원급 + as의 바른 형태이므로", "heavier로 써야 하는데 more를 겹쳐 썼으므로", "much로 강조한 비교급의 바른 형태이므로", "셋 중 가장 가벼운 것이라 the + -est의 바른 최상급이므로"], 3), k="heavier로 써야 하는데 more를 겹쳐 썼다.", s=ADD(2, 85, "D", L85))
RE(2, 85, "E", p="A: How was your vacation at the beach last week?\nB: It was ①<u>the worst vacation I have ever had</u>. Everything went wrong.\nA: Why? Was the weather ②<u>more bad than you expected</u>?\nB: Yes. It rained ③<u>more heavily than last year</u>, and the hotel was noisy.\nA: That's too bad. Next time, check the weather ④<u>as carefully as you can</u> before you leave.\nB: I will. ⑤<u>Nothing is more important than good weather</u> on a beach trip.",
   c=["the worst vacation I have ever had", "more bad than you expected", "more heavily than last year", "as carefully as you can", "Nothing is more important than good weather"], a=2,
   n=OKS(["bad의 최상급 worst를 바르게 썼으므로", "bad의 비교급은 worse이므로 worse than으로 써야 하므로", "부사 heavily의 비교급 more heavily의 바른 형태이므로", "as + 원급 + as의 바른 형태이므로", "Nothing is + 비교급 + than(최상급의 뜻)의 바른 형태이므로"], 2), k="bad의 비교급은 worse이므로 worse than으로 써야 한다.", s=ADD(2, 85, "E", L85))
RE(2, 85, "F", p="A: Is the Nakdong River ①<u>more long than the Han River</u>?\nB: Yes, it is. It's ②<u>the longest river in Korea</u>, as far as I know.\nA: Is it really ③<u>longer than any other river in the country</u>?\nB: Of course. ④<u>No other river in Korea is as long as the Nakdong River</u>.\nA: Interesting. I'd like to visit it ⑤<u>as soon as I can</u> this summer vacation with my family.",
   c=["more long than the Han River", "the longest river in Korea", "longer than any other river in the country", "No other river in Korea is as long as the Nakdong River", "as soon as I can"], a=1,
   n=OKS(["long의 비교급은 longer이므로 more long은 쓰지 않으므로", "the + -est의 바른 최상급이므로", "비교급 + than any other + 단수명사(최상급의 뜻)의 바른 형태이므로", "No other + 단수명사 + as + 원급 + as(최상급의 뜻)의 바른 형태이므로", "as + 원급 + as의 바른 형태이므로"], 1), k="long의 비교급은 longer이므로 more long은 쓰지 않는다.", s=ADD(2, 85, "F", L85))

# ---- 2-94: 문장과 <보기>를 원문항 길이(45낱말)로 ----
RE(2, 94, "C", p="(a)<u>That</u> is my old school (b)<u>that</u> I attended for three years.\n<보기>\nㄱ. The song that we heard on the radio was really beautiful.\nㄴ. That is mine, so please don't touch it.\nㄷ. She said that she was too tired to go out.\nㄹ. That Tom won the race was surprising to everyone.", s=ADD(2, 94, "C", LENP))
RE(2, 94, "D", p="(a)<u>That</u> is the expensive bag (b)<u>that</u> Mina chose at the mall yesterday.\n<보기>\nㄱ. I think that he is right about the new plan.\nㄴ. The bag that Jane bought last week is dark blue.\nㄷ. That is a new camera for my trip.\nㄹ. That he left early worried all of us.", s=ADD(2, 94, "D", LENP))
RE(2, 94, "E", p="(a)<u>That</u> was the only answer (b)<u>that</u> worked for the difficult problem.\n<보기>\nㄱ. The plan that worked in the end was very simple.\nㄴ. That she came to the party surprised me a lot.\nㄷ. That is the answer to the last question.\nㄹ. I know that he called you this morning.", s=ADD(2, 94, "E", LENP))
RE(2, 94, "F", p="(a)<u>That</u> is the house (b)<u>that</u> we sold to a young couple last year.\n<보기>\nㄱ. She believes that he is kind to everyone.\nㄴ. That is our house on the hill.\nㄷ. That he apologized at once mattered to her.\nㄹ. The house that we sold was very old.", s=ADD(2, 94, "F", LENP))

# ---- 2-105: ⓐ~ⓔ 문장을 원문항 길이(44낱말) 이상으로, 선택지 1개~5개 ----
R105 = "at + 시각, around + 대략의 시각, for + 숫자로 된 기간, during + 특정 기간(명사), by + 기한(그때까지 끝냄), until + 그때까지 계속을 구별한다. 절(주어 + 동사) 앞에는 during이 아니라 while을 쓴다."
L105 = MEMO4 + "원문항보다 짧던 문장을 원문항 길이 이상으로 늘리고 선택지를 1개~5개 순으로 두었다."
RE(2, 105, "C", p="ⓐ The school bus arrives at the front gate at 8 sharp.\nⓑ I usually exercise around 6 a.m. before I go to work.\nⓒ We talked for two hours about our plans for the summer.\nⓓ She stayed in the waiting room during she waited for the doctor.\nⓔ Please finish this report by Monday and send it to me.",
   c=CNT, a=4, r=R105, pre=PJ("ⓐ O. 시각 앞에 at을 썼다.", "ⓑ O. 대략의 시각 앞에 around를 썼다.", "ⓒ O. 숫자로 된 기간 앞에 for를 썼다.", "ⓓ X. 절(she waited) 앞에는 during이 아니라 while을 쓴다. 교정문: She stayed in the waiting room while she waited for the doctor.", "ⓔ O. 끝내는 기한 앞에 by를 썼다."),
   k="어법상 옳은 문장은 ⓐ, ⓑ, ⓒ, ⓔ로 4개이다.", n="cnt", s=ADD(2, 105, "C", L105))
RE(2, 105, "D", p="ⓐ The first class starts at 9 sharp every morning.\nⓑ Mina called me around midnight to ask about the homework.\nⓒ They traveled around Europe during the winter vacation.\nⓓ Tom waited during an hour for the bus in the rain.\nⓔ Submit the application form by Friday if you want to join.",
   c=CNT, a=4, r=R105, pre=PJ("ⓐ O. 시각 앞에 at을 썼다.", "ⓑ O. 대략의 시각 앞에 around를 썼다.", "ⓒ O. 특정 기간(the winter vacation) 앞에 during을 썼다.", "ⓓ X. 숫자로 된 기간 앞에는 for를 쓴다. 교정문: Tom waited for an hour for the bus in the rain.", "ⓔ O. 끝내는 기한 앞에 by를 썼다."),
   k="어법상 옳은 문장은 ⓐ, ⓑ, ⓒ, ⓔ로 4개이다.", n="cnt", s=ADD(2, 105, "D", L105))
RE(2, 105, "E", p="ⓐ The last train leaves at 7 sharp, so don't be late.\nⓑ We usually meet around lunchtime at the cafe near school.\nⓒ Jane studied for three hours in the library last night.\nⓓ He lived there during five years before he moved to Seoul.\nⓔ Please arrive by six because the concert starts right after.",
   c=CNT, a=4, r=R105, pre=PJ("ⓐ O. 시각 앞에 at을 썼다.", "ⓑ O. 대략의 시각 앞에 around를 썼다.", "ⓒ O. 숫자로 된 기간 앞에 for를 썼다.", "ⓓ X. 숫자로 된 기간 앞에는 for를 쓴다. 교정문: He lived there for five years before he moved to Seoul.", "ⓔ O. 끝내는 기한 앞에 by를 썼다."),
   k="어법상 옳은 문장은 ⓐ, ⓑ, ⓒ, ⓔ로 4개이다.", n="cnt", s=ADD(2, 105, "E", L105))
RE(2, 105, "F", p="ⓐ Dinner starts at 6 sharp, so wash your hands now.\nⓑ Tom usually gets home around 8 after soccer practice.\nⓒ We stayed inside the house while the terrible storm.\nⓓ Jane worked for two hours on her science homework.\nⓔ Keep waiting here by noon, and I will come back.",
   c=CNT, a=3, r=R105, pre=PJ("ⓐ O. 시각 앞에 at을 썼다.", "ⓑ O. 대략의 시각 앞에 around를 썼다.", "ⓒ X. 명사(the terrible storm) 앞에는 while이 아니라 during을 쓴다. 교정문: We stayed inside the house during the terrible storm.", "ⓓ O. 숫자로 된 기간 앞에 for를 썼다.", "ⓔ X. 정오까지 계속 기다리는 것이므로 by가 아니라 until을 쓴다. 교정문: Keep waiting here until noon, and I will come back."),
   k="어법상 옳은 문장은 ⓐ, ⓑ, ⓓ로 3개이다.", n="cnt", s=ADD(2, 105, "F", L105 + " 다른 유형과 정답 개수가 겹치지 않게 ⓒ도 틀린 문장으로 했다."))

# ---- 2-110: <보기> 문장을 원문항 길이(38낱말) 이상으로 ----
R110 = OLD(2, 110, "C")["r"]
RE(2, 110, "C", p="<보기>\n- Stay here <u>until six</u>, and then we can leave together.\n- Finish all the work <u>until Friday</u>, or you will be in trouble.\n- We talked <u>during two hours</u> about the new science project.\n- The lights went out <u>during the storm</u> last night.\n- Tom came to my house <u>around noon</u> with his little brother.", s=ADD(2, 110, "C", LEN))
RE(2, 110, "D", p="<보기>\n- I waited for her call <u>until midnight</u>, but she never called.\n- Submit this report <u>until Monday</u> if you want full credit.\n- Jane lived there <u>for five years</u> before she moved to Busan.\n- Tom slept <u>while the flight</u> to London because he was tired.\n- The bus finally came <u>on seven sharp</u>, just as the sign said.", s=ADD(2, 110, "D", LEN))
RE(2, 110, "E", p="<보기>\n- We stayed at the party <u>until the end</u> of the fireworks show.\n- Finish it <u>by tomorrow</u> if you want to take the trip.\n- Mina studied <u>for an hour</u> after dinner every night.\n- Jane read a magazine <u>during she waited</u> for the dentist this morning.\n- The first class starts <u>at nine</u> every morning except Monday.",
   c=CNT, a=4, r=R110, pre=PJ("첫째 O. 끝까지 머무는 상태가 이어지므로 until이다.", "둘째 O. 끝내야 하는 기한이므로 by를 썼다.", "셋째 O. 숫자로 나타낸 기간 앞에 for를 썼다.", "넷째 X. 절(she waited) 앞에는 during이 아니라 while을 쓴다.", "다섯째 O. 시각 앞에 at을 썼다."),
   k="밑줄 친 부분이 올바른 문장은 첫째, 둘째, 셋째, 다섯째로 4개이다.", n="cnt", s=ADD(2, 110, "E", LEN + " 선택지는 1개~5개 순으로 두었다."))
RE(2, 110, "F", p="<보기>\n- The store is open <u>until ten</u> on Fridays and Saturdays.\n- Send the file <u>until noon</u> so that I can check it today.\n- We worked <u>for three hours</u> to finish the group project.\n- Jane rested in the shade <u>while the break</u> between the games.\n- Tom arrived at the station <u>on six</u> and waited for us.", s=ADD(2, 110, "F", LEN))

# ---- 2-124: 대화를 원문항 길이(88낱말) 이상으로, 밑줄도 원문항처럼 서너 낱말로 ----
L124 = MEMO4 + "원문항보다 짧던 대화를 원문항 길이 이상으로 늘리고 밑줄 범위를 원문항처럼 서너 낱말로 했다. 정답 위치는 그대로다."
RE(2, 124, "C", p="Tom: I wish ①<u>I knew the answer</u> to this question. I've been thinking about it for almost an hour, and I'm still stuck.\nAmy: If ②<u>I have the textbook</u> with me, I would lend it to you right now. Unfortunately, I left it at school.\nTom: Thanks anyway. If ③<u>I had studied harder</u> last week, I wouldn't be so worried about the test now.\nAmy: I wish ④<u>you had asked me</u> earlier. We could have studied together at the library after school.\nTom: You're right. If only ⑤<u>I were as smart</u> and well organized as you are!",
   c=["I knew the answer", "I have the textbook", "I had studied harder", "you had asked me", "I were as smart"], a=2,
   n=OKS(["I wish 뒤 현재 사실 반대의 소망에 과거형 knew를 바르게 썼으므로", "주절이 would lend인 가정법 과거이므로 if절에는 had를 써야 하므로", "과거 사실과 반대되는 조건에 had + 과거분사를 바르게 썼으므로", "I wish + had + 과거분사로 지난 일의 아쉬움을 바르게 나타냈으므로", "If only 뒤 현재 사실 반대의 소망에 were를 바르게 썼으므로"], 2), s=ADD(2, 124, "C", L124))
RE(2, 124, "D", p="Jane: If ①<u>it had not rained</u> yesterday, we would have gone hiking in the mountains. I was really looking forward to it all week.\nBen: I know. I wish ②<u>the weather were</u> better today, too. Look at those dark clouds over there.\nJane: If ③<u>I were you</u>, I would check the forecast first before making any plans.\nBen: Good idea. If only ④<u>I had checked it</u> yesterday! We wouldn't have wasted the whole day waiting.\nJane: Don't worry about it. I wish ⑤<u>we will go hiking</u> together next weekend.",
   c=["it had not rained", "the weather were", "I were you", "I had checked it", "we will go hiking"], a=5,
   n=OKS(["어제 일과 반대되는 조건이라 had + 과거분사를 바르게 썼으므로", "오늘의 사실과 반대되는 소망에 were를 바르게 썼으므로", "현재 사실과 반대되는 조건에 were를 바르게 썼으므로", "If only + had + 과거분사로 지난 일의 아쉬움을 바르게 나타냈으므로", "I wish 뒤에는 will을 쓸 수 없다. could go로 써야 하므로"], 5), s=ADD(2, 124, "D", L124))
RE(2, 124, "E", p="Sora: I wish ①<u>I had a pet dog</u>. All my friends have one, and they always talk about their dogs.\nMin: If ②<u>you had a dog</u>, you would have to walk it every single day, even in the cold winter.\nSora: I know that. I wouldn't mind at all. If ③<u>my mom allows it</u>, I would get one right away.\nMin: I understand. I wish ④<u>my apartment were bigger</u>, too. Then I could keep a big dog myself.\nSora: If only ⑤<u>we lived in a house</u> with a big yard and a garden!",
   c=["I had a pet dog", "you had a dog", "my mom allows it", "my apartment were bigger", "we lived in a house"], a=3,
   n=OKS(["I wish 뒤 현재 사실 반대의 소망에 과거형 had를 바르게 썼으므로", "현재 사실과 반대되는 조건에 과거형 had를 바르게 썼으므로", "주절이 would get인 가정법 과거이므로 if절에는 allowed를 써야 하므로", "I wish 뒤 현재 사실 반대의 소망에 were를 바르게 썼으므로", "If only 뒤 현재 사실 반대의 소망에 과거형 lived를 바르게 썼으므로"], 3), s=ADD(2, 124, "E", L124))
RE(2, 124, "F", p="Leo: If ①<u>I have known about the sale</u>, I would have bought the shoes. They were half price last weekend, and now they are gone.\nAmy: I wish ②<u>you had told me</u> you wanted them so much. I would have gone to the store with you right away.\nLeo: If ③<u>I had more money</u> now, I would buy them anyway, because they are still really nice.\nAmy: If only ④<u>they were still on sale</u>! The price went back up yesterday morning.\nLeo: I wish ⑤<u>I could go back</u> to that day and buy them.",
   c=["I have known about the sale", "you had told me", "I had more money", "they were still on sale", "I could go back"], a=1,
   n=OKS(["주절이 would have bought인 가정법 과거완료이므로 if절에는 had known을 써야 하므로", "이미 지난 일에 대한 아쉬움이라 had + 과거분사를 바르게 썼으므로", "현재 사실과 반대되는 조건에 과거형 had를 바르게 썼으므로", "If only 뒤 현재 사실 반대의 소망에 were를 바르게 썼으므로", "I wish 뒤 현재 사실 반대의 소망에 could를 바르게 썼으므로"], 1), s=ADD(2, 124, "F", L124))

# ======================= 3급 =======================
# ---- 3-3: 대화를 원문항 길이(13낱말) 이상으로 ----
RE(3, 3, "C", p="Tom: (A) _____ she at home now? I want to talk to her.\nJane: No, (B) _____ not. She's at the library with Mina.", s=LENP)
RE(3, 3, "D", p="Amy: (A) _____ they ready for the school trip tomorrow?\nBen: No, (B) _____ not. They still need to pack their bags.", s=LENP)
RE(3, 3, "E", p="Leo: (A) _____ I late for the meeting again?\nMina: No, (B) _____ not. It starts in ten minutes.", s=LENP)
RE(3, 3, "F", p="Jane: (A) _____ Tom at school today? I can't find him.\nAmy: No, (B) _____ not. He is sick at home.", s=LENP)

# ---- 3-5: ⓐ~ⓔ 문장을 원문항 길이(32낱말) 이상으로 ----
RE(3, 5, "C", p="ⓐ Tom <u>is</u> busy with his homework right now.\nⓑ They <u>isn't</u> ready for the big game yet.\nⓒ <u>Are</u> we late for the first class?\nⓓ There <u>is</u> two books on the teacher's desk.\nⓔ Jane <u>were</u> at home all day yesterday.", s=ADD(3, 5, "C", LEN))
RE(3, 5, "D", p="ⓐ I <u>was</u> very tired after the long trip.\nⓑ The boys <u>were</u> happy with their new bikes.\nⓒ There <u>was</u> a small dog outside the gate.\nⓓ She <u>isn't</u> busy on Sunday mornings.\nⓔ <u>Was</u> they late for the concert last night?", s=ADD(3, 5, "D", LEN))
RE(3, 5, "E", p="ⓐ We <u>are</u> students at the same middle school.\nⓑ Tom <u>wasn't</u> at home when I called him.\nⓒ There <u>is</u> some water in the bottle.\nⓓ The news about the game <u>are</u> good.\nⓔ <u>Am</u> I late for the meeting today?", s=ADD(3, 5, "E", LEN))
RE(3, 5, "F", p="ⓐ Jane <u>is</u> kind to everyone in her class.\nⓑ They <u>wasn't</u> busy last weekend.\nⓒ There <u>was</u> two cats under the table.\nⓓ We <u>isn't</u> late for school today.\nⓔ <u>Is</u> you ready for the test tomorrow?", s=ADD(3, 5, "F", LEN))

# ---- 3-8: 문장을 원문항 길이(13낱말) 이상으로 ----
RE(3, 8, "C", p="Tom (<u>    A    </u>) at home all afternoon, but his friends (<u>    B    </u>) at the soccer field.", s=ADD(3, 8, "C", LEN))
RE(3, 8, "D", p="I (<u>    A    </u>) tired after the long hike, but we (<u>    B    </u>) happy about the beautiful view.", s=ADD(3, 8, "D", LEN))
RE(3, 8, "E", p="The dog (<u>    A    </u>) hungry after the walk, but the cats (<u>    B    </u>) fine in the warm house.", s=ADD(3, 8, "E", LEN))
RE(3, 8, "F", p="Jane and Amy (<u>    A    </u>) busy with the school play, but Tom (<u>    B    </u>) free all weekend.", s=ADD(3, 8, "F", LEN))

# ---- 3-19: <보기> 지문을 원문항 길이(26낱말) 이상으로, 설명도 원문항처럼 자세히 ----
R19 = OLD(3, 19, "C")["r"]
L19 = MEMO4 + "원문항보다 짧던 지문을 원문항 길이 이상으로 늘리고 설명을 원문항처럼 자세히 썼다. 정답 위치는 그대로다."
RE(3, 19, "C", p="<보기>\nYesterday, Tom ⓐ<u>went</u> home early after school. He ⓑ<u>buyed</u> a snack at the store near his house. His sister ⓒ<u>came</u> home later in the evening. They ⓓ<u>ate</u> dinner together and ⓔ<u>were</u> very tired.",
   c=["ⓒ: 'come'의 불규칙 과거형으로, 여동생이 나중에 온 일을 나타낸다.", "ⓑ: 'buy'의 과거형은 불규칙 변화인 'bought'이므로 ⓑ는 틀린 표현이다.", "ⓔ: 주어가 'They'인 복수형이므로 be동사의 과거형 'were'를 쓴 것은 적절하다.", "ⓓ: 'eat'은 규칙 변화하는 동사이므로 과거형은 'eated'로 써야 한다.", "ⓐ: 'go'의 불규칙 과거형으로, 어제 집에 간 일을 나타낸다."], a=4, r=R19,
   n=OKS(["came은 come의 불규칙 과거형이라 옳은 설명이므로", "buy의 과거형은 bought라 옳은 설명이므로", "복수 주어 They에 were를 쓴 것이 맞아 옳은 설명이므로", "eat은 불규칙동사라 과거형이 ate이므로 ⓓ는 알맞고 이 설명이 틀렸다. 옳지 않은 설명이므로", "went는 go의 불규칙 과거형이라 옳은 설명이므로"], 4), s=ADD(3, 19, "C", L19))
RE(3, 19, "D", p="<보기>\nLast night, Jane ⓐ<u>wrote</u> a long letter to her best friend. She ⓑ<u>goed</u> to bed late because of the letter. Her parents ⓒ<u>were</u> already asleep in their room. She ⓓ<u>read</u> a book for a while and ⓔ<u>slept</u> well.",
   c=["ⓑ: 'go'의 과거형은 불규칙 변화인 'went'이므로 ⓑ는 'went'로 고쳐야 한다.", "ⓒ: 주어 'Her parents'가 복수이므로 be동사의 과거형 'were'를 쓴 것은 적절하다.", "ⓐ: 'write'의 불규칙 과거형으로, 어젯밤에 편지를 쓴 일을 나타낸다.", "ⓔ: 'sleep'의 불규칙 과거형으로, 잘 잤다는 뜻으로 쓰였다.", "ⓓ: 'read'는 규칙 변화하는 동사이므로 과거형은 반드시 'readed'로 써야 한다."], a=5, r=R19,
   k="read의 과거형은 철자가 같은 read이므로 ⓓ는 알맞고, 이 설명이 틀렸다.",
   n=OKS(["go의 과거형은 went라 옳은 설명이므로", "복수 주어에 were를 쓴 것이 맞아 옳은 설명이므로", "wrote는 write의 불규칙 과거형이라 옳은 설명이므로", "slept는 sleep의 불규칙 과거형이라 옳은 설명이므로", "read의 과거형은 철자가 같은 read이므로 ⓓ는 알맞고 이 설명이 틀렸다. 옳지 않은 설명이므로"], 5), s=ADD(3, 19, "D", L19))
RE(3, 19, "E", p="<보기>\nLast weekend, we ⓐ<u>saw</u> a funny movie at Tom's house. Tom ⓑ<u>made</u> a big bowl of popcorn for us. I ⓒ<u>eated</u> too much and felt sick. We ⓓ<u>had</u> a lot of fun and ⓔ<u>went</u> home late.",
   c=["ⓐ: 'see'의 불규칙 과거형으로, 지난 주말에 영화를 본 일을 나타낸다.", "ⓓ: 'have'의 불규칙 과거형으로, 재미있게 보냈다는 뜻으로 쓰였다.", "ⓑ: 'make'는 규칙 변화하는 동사이므로 과거형은 'maked'로 써야 한다.", "ⓔ: 'went'는 'go'의 과거형이며 여기서는 '집에 갔다'는 뜻이다.", "ⓒ: 'eat'의 과거형은 불규칙 변화인 'ate'이므로 ⓒ는 틀린 표현이다."], a=3, r=R19,
   n=OKS(["saw는 see의 불규칙 과거형이라 옳은 설명이므로", "had는 have의 불규칙 과거형이라 옳은 설명이므로", "make의 과거형은 made이므로 ⓑ는 알맞고 이 설명이 틀렸다. 옳지 않은 설명이므로", "went는 go의 불규칙 과거형이라 옳은 설명이므로", "eat의 과거형은 ate라 옳은 설명이므로"], 3), s=ADD(3, 19, "E", L19))
RE(3, 19, "F", p="<보기>\nYesterday, the boys ⓐ<u>ran</u> around the park after lunch. One boy ⓑ<u>falled</u> down on the wet grass. His friends ⓒ<u>came</u> over to him right away. They ⓓ<u>helped</u> him up and ⓔ<u>were</u> worried about his knee.",
   c=["ⓑ: 'fall'의 과거형은 불규칙 변화인 'fell'이므로 ⓑ는 틀린 표현이다.", "ⓐ: 'run'은 규칙 변화하는 동사이므로 과거형은 'runned'로 써야 한다.", "ⓒ: 'come'의 불규칙 과거형으로, 친구들이 다가온 일을 나타낸다.", "ⓓ: 'help'는 규칙 동사이므로 과거형을 만들 때 '-ed'를 붙인 것은 적절하다.", "ⓔ: 복수 주어 'They' 뒤에 be동사의 과거형으로 'were'를 쓴 것은 알맞다."], a=2, r=R19,
   n=OKS(["fall의 과거형은 fell이라 옳은 설명이므로", "run의 과거형은 ran이므로 ⓐ는 알맞고 이 설명이 틀렸다. 옳지 않은 설명이므로", "came은 come의 불규칙 과거형이라 옳은 설명이므로", "규칙동사 help에 -ed를 붙인 것이 맞아 옳은 설명이므로", "복수 주어 They에 were를 쓴 것이 맞아 옳은 설명이므로"], 2), s=ADD(3, 19, "F", L19))

# ---- 3-20: 문장을 원문항 길이(35낱말) 이상으로 ----
R20 = OLD(3, 20, "C")["r"]
RE(3, 20, "C", p="- Tom went home early because he had a headache.\n- Jane buyed a new bag at the mall last Saturday.\n- We didn't saw him at the bus stop this morning.\n- Did they ate lunch at the new restaurant yesterday?\n- I wrote a long letter to my grandmother last night.", s=ADD(3, 20, "C", LEN))
RE(3, 20, "D", p="- They came early to help us set up the tables.\n- He didn't go home until the game was over.\n- Jane saw the movie with her cousins last weekend.\n- Did Tom write this report by himself?\n- We maked dinner for the whole family on Sunday.", s=ADD(3, 20, "D", LEN))
RE(3, 20, "E", p="- I read the whole book in just two days.\n- She didn't buy the dress because it was too expensive.\n- They took a bus to the stadium instead of the subway.\n- Did Jane came to the party with her brother?\n- Tom was tired after the long soccer practice.",
   c=CNT, a=4, r=R20, pre=PJ("첫째 O. read의 과거형은 철자가 같은 read이다.", "둘째 O. didn't + 동사원형이다.", "셋째 O. take의 과거형 took이다.", "넷째 X. Did 뒤에는 동사원형(come)을 쓴다.", "다섯째 O. be동사의 과거형 was이다."),
   k="어법상 옳은 문장은 첫째, 둘째, 셋째, 다섯째로 4개이다.", n="cnt", s=ADD(3, 20, "E", LEN + " 선택지는 1개~5개 순으로 두었다."))
RE(3, 20, "F", p="- We ate lunch together in the school cafeteria.\n- He didn't saw me at the library yesterday afternoon.\n- Jane writed a short note to her teacher.\n- Did they went home right after the concert?\n- Tom buyed a used car from his neighbor last month.", s=ADD(3, 20, "F", LEN))

# ---- 3-21: 복수 정답이 될 수 있는 오답(a bottle of water, a cup of milk) 교체 ----
R21 = OLD(3, 21, "C")["r"]
L21 = MEMO4 + "우리말과 달라도 영어로는 자연스러운 단위 표현이 오답에 있어 정답이 둘이 될 수 있었다. 그 오답을 뜻이 맞지 않는 단위 표현으로 바꿨다."
RE(3, 21, "C", c=["a slice of", "a loaf of", "a piece of", "a sheet of", "a glass of"], a=5, r=R21,
   n=OKS(["a slice of는 얇게 썬 ‘한 조각’이라 물에 쓰지 않으므로", "a loaf of는 빵 같은 ‘한 덩어리’에 쓰므로", "a piece of는 ‘한 조각’이라 물에 쓰지 않으므로", "a sheet of는 종이 같은 ‘한 장’에 쓰므로", "‘물 한 잔’은 a glass of water이므로"], 5), s=ADD(3, 21, "C", L21 + "(a bottle of → a slice of)" + pos(5)))
RE(3, 21, "F", c=["a slice of", "a sheet of", "a piece of", "a loaf of", "a bottle of"], a=5, r=R21,
   n=OKS(["a slice of는 얇게 썬 ‘한 조각’이라 우유에 쓰지 않으므로", "a sheet of는 종이 같은 ‘한 장’에 쓰므로", "a piece of는 ‘한 조각’이라 우유에 쓰지 않으므로", "a loaf of는 빵 같은 ‘한 덩어리’에 쓰므로", "‘우유 한 병’은 a bottle of milk이므로"], 5), s=L21 + "(a cup of → a slice of)" + pos(5))

# ---- 3-30: 설명 선택지를 ⓐ~ⓔ 순서로, 원문항처럼 자세히 ----
R30 = "하나뿐인 것(the sun, the moon, the sky)과 악기 앞에는 the를 쓴다. 식사 이름, 운동 이름, by + 교통·통신 수단, on foot에는 관사를 쓰지 않는다. 하루의 시간대는 in the morning/afternoon/evening으로 쓴다."
L30 = MEMO4 + "설명 선택지를 ⓐ~ⓔ 순서로 두고 원문항처럼 자세히 썼으며, 지문도 원문항 길이 이상으로 늘렸다."
RE(3, 30, "C", p="<보기>\nLast night, we went up the hill and saw ⓐ<u>the moon</u> shining over the town. After ⓑ<u>dinner</u>, we talked with our cousins ⓒ<u>by phone</u> for a long time. In ⓓ<u>the evening</u>, Tom played ⓔ<u>the guitar</u> for us, and everyone sang along happily.", c=["ⓐ: 'moon'은 하나뿐인 천체라서 앞에 정관사 'the'를 쓴다.", "ⓑ: '저녁 식사'와 같은 식사 이름 앞에는 언제나 부정관사 'a'를 써야 한다.", "ⓒ: 통신 수단을 나타내는 'by' 뒤에는 관사를 쓰지 않고 명사만 쓴다.", "ⓓ: 하루의 시간대를 나타내는 'evening' 앞에는 'in the'를 써서 'in the evening'으로 쓴다.", "ⓔ: 'play the guitar'처럼 악기를 연주한다고 할 때 악기 이름 앞에는 'the'를 쓴다."], a=2, r=R30,
   k="식사 이름 dinner 앞에는 관사를 쓰지 않으므로",
   n=OKS(["하나뿐인 moon 앞에 the를 쓴다는 옳은 설명이므로", "식사 이름 dinner 앞에는 관사를 쓰지 않는다. 옳지 않은 설명이므로", "by + 통신 수단에는 관사를 쓰지 않는다는 옳은 설명이므로", "시간대는 in the evening으로 쓴다는 옳은 설명이므로", "악기 이름 앞에는 the를 쓴다는 옳은 설명이므로"], 2), s=ADD(3, 30, "C", L30 + pos(2)))
RE(3, 30, "D", c=["ⓐ: 'breakfast' 같은 식사 이름 앞에는 보통 관사를 쓰지 않는다.", "ⓑ: 'by bus'처럼 교통수단 앞에는 관사 없이 명사만 쓴다.", "ⓒ: 운동 경기 이름인 'tennis' 앞에는 항상 정관사 'the'를 써야 한다.", "ⓓ: 'afternoon'처럼 하루의 시간대를 말할 때는 'in the afternoon'으로 쓴다.", "ⓔ: '하늘(sky)'은 하나뿐인 것으로 보아 정관사 'the'를 붙이는 것이 옳다."], a=3, r=R30,
   k="운동 이름 tennis 앞에는 the를 쓰지 않으므로",
   n=OKS(["식사 이름 앞에는 관사를 쓰지 않는다는 옳은 설명이므로", "by + 교통수단에는 관사를 쓰지 않는다는 옳은 설명이므로", "운동 이름 tennis 앞에는 the를 쓰지 않는다. 옳지 않은 설명이므로", "시간대는 in the afternoon으로 쓴다는 옳은 설명이므로", "하나뿐인 sky 앞에 the를 쓴다는 옳은 설명이므로"], 3), s=ADD(3, 30, "D", L30 + pos(3)))
RE(3, 30, "E", p="<보기>\nLast weekend, Tom traveled to his grandparents' house ⓐ<u>by train</u> with his little sister. After ⓑ<u>lunch</u>, he played ⓒ<u>the piano</u> for his family. The next day, in ⓓ<u>the morning</u>, he got up early and saw ⓔ<u>the sun</u> rise slowly over the sea.", c=["ⓐ: 교통수단을 나타내는 'by' 뒤에는 반드시 부정관사를 넣어 'by a train'으로 써야 한다.", "ⓑ: 'lunch' 같은 식사 이름은 보통 관사 없이 쓴다.", "ⓒ: 'play the piano'처럼 악기 이름 앞에는 정관사 'the'를 쓴다.", "ⓓ: 'in the morning'은 하루의 시간대를 나타내는 올바른 표현이다.", "ⓔ: '해(sun)'처럼 세상에 하나뿐인 것 앞에는 정관사 'the'를 쓰는 것이 옳다."], a=1, r=R30,
   k="by + 교통수단에는 관사를 쓰지 않으므로 by train이 맞다.",
   n=OKS(["by + 교통수단에는 관사를 쓰지 않으므로 by train이 맞다. 옳지 않은 설명이므로", "식사 이름 앞에는 관사를 쓰지 않는다는 옳은 설명이므로", "악기 이름 앞에는 the를 쓴다는 옳은 설명이므로", "시간대는 in the morning으로 쓴다는 옳은 설명이므로", "하나뿐인 sun 앞에 the를 쓴다는 옳은 설명이므로"], 1), s=ADD(3, 30, "E", L30 + pos(1)))
RE(3, 30, "F", p="<보기>\nAfter school, we had ⓐ<u>dinner</u> at a small restaurant near the station and went home ⓑ<u>on foot</u>. Then we played ⓒ<u>basketball</u> in the park for an hour. We read books in ⓓ<u>the evening</u> and took a short walk under ⓔ<u>the moon</u>.", c=["ⓐ: 'dinner'처럼 식사를 나타내는 명사 앞에는 관사를 쓰지 않는 것이 원칙이다.", "ⓑ: '걸어서'라는 뜻의 'on foot'은 관사 없이 쓰는 이동 수단 표현이다.", "ⓒ: 'basketball' 같은 운동 이름 앞에는 반드시 'the'를 붙여야 한다.", "ⓓ: 저녁 시간대를 나타낼 때는 'the'를 넣어 'in the evening'으로 쓴다.", "ⓔ: 'moon'은 유일한 천체이므로 앞에 정관사 'the'를 붙인다."], a=3, r=R30,
   k="운동 이름 basketball 앞에는 the를 쓰지 않으므로",
   n=OKS(["식사 이름 앞에는 관사를 쓰지 않는다는 옳은 설명이므로", "on foot은 관사 없이 쓴다는 옳은 설명이므로", "운동 이름 basketball 앞에는 the를 쓰지 않는다. 옳지 않은 설명이므로", "시간대는 in the evening으로 쓴다는 옳은 설명이므로", "하나뿐인 moon 앞에 the를 쓴다는 옳은 설명이므로"], 3), s=ADD(3, 30, "F", L30 + pos(3)))

# ---- 3-39: (가)~(라) 문장을 원문항 길이(26낱말) 이상으로 ----
RE(3, 39, "C", p="(가) Tom is reading a comic book in his room.\n(나) We are study English with our new teacher.\n(다) Jane is writing a letter to her grandmother.\n(라) They is playing soccer in the schoolyard now.", s=ADD(3, 39, "C", LEN))
RE(3, 39, "D", p="(가) I am cooking dinner for my family tonight.\n(나) The boys are running around the playground.\n(다) She is know the answer to the question.\n(라) Tom are watching TV in the living room.", s=ADD(3, 39, "D", LEN))
RE(3, 39, "E", p="(가) We are leaveing for the airport right now.\n(나) Jane is sleeping on the sofa after lunch.\n(다) They are swimming in the pool near the hotel.\n(라) I is reading a book about dinosaurs.", s=ADD(3, 39, "E", LEN))
RE(3, 39, "F", p="(가) The dog are barking at the mailman again.\n(나) Tom is working at the cafe this afternoon.\n(다) I am want a new bag for school.\n(라) We are cleaning the classroom after school.", s=ADD(3, 39, "F", LEN))

# ---- 3-40: 지문을 원문항 길이(41낱말) 이상으로, 설명 선택지를 ⓐ~ⓔ 순서로 ----
L40b = MEMO4 + "원문항보다 짧던 지문을 원문항 길이 이상으로 늘리고 설명 선택지를 ⓐ~ⓔ 순서로 두었다."
RE(3, 40, "C", p="Yesterday, Tom ⓐ<u>went</u> to school early to finish his science project. He ⓑ<u>was studying</u> in the library at noon when his friends called him. Later, he ⓒ<u>bought</u> a snack at the store across the street. His friends ⓓ<u>were playing</u> soccer on the field after school. He ⓔ<u>didn't come</u> home late because he had to help his mother.",
   c=["ⓐ went는 ‘가다(go)’의 과거형으로 불규칙하게 변한 것이다.", "ⓑ는 과거의 특정 시점(정오)에 진행 중이던 동작을 나타내는 과거진행형이다.", "ⓒ: buy의 과거형은 buyed이므로 bought는 틀린 표현이다.", "ⓓ는 복수 주어에 맞춰 were를 쓴 과거진행형이다.", "ⓔ: did not 뒤이므로 동사원형 come을 썼다."], a=3,
   n=OKS(["went는 go의 불규칙 과거형이라 옳은 설명이므로", "was studying은 과거의 특정 시점에 진행 중이던 과거진행형이라 옳은 설명이므로", "buy의 과거형은 bought이므로 ⓒ는 옳고 이 설명이 틀렸다. 옳지 않은 설명이므로", "복수 주어에 were를 쓴 과거진행형이라 옳은 설명이므로", "didn't 뒤에 동사원형 come을 쓴 것이 맞아 옳은 설명이므로"], 3), s=ADD(3, 40, "C", L40b + pos(3)))
RE(3, 40, "D", p="Last Sunday, Jane ⓐ<u>visited</u> her aunt in the countryside with her parents. When she got there, her aunt ⓑ<u>was cooking</u> in the kitchen. They ⓒ<u>ate</u> dinner together and talked for a long time about school. Jane ⓓ<u>was</u> very happy and ⓔ<u>went</u> home late in the evening.",
   c=["ⓐ visited는 규칙 과거형이다.", "ⓑ was cooking은 과거진행형이다.", "ⓒ: eat은 규칙동사라 과거형은 ate가 아니라 eated이다.", "ⓓ was는 3인칭 단수 주어(Jane)의 과거 상태를 나타낸다.", "ⓔ: 집에 간 과거의 일을 go의 과거형으로 나타냈다."], a=3,
   n=OKS(["visited는 규칙 과거형이라 옳은 설명이므로", "was cooking은 과거진행형이라 옳은 설명이므로", "eat은 불규칙동사라 과거형은 ate이므로 ⓒ는 옳고 이 설명이 틀렸다. 옳지 않은 설명이므로", "단수 주어의 과거는 was라 옳은 설명이므로", "went는 go의 과거형이라 옳은 설명이므로"], 3), s=ADD(3, 40, "D", L40b + pos(3)))
RE(3, 40, "E", p="Yesterday, we ⓐ<u>played</u> soccer in the park after school with some new friends. Tom ⓑ<u>was running</u> fast with the ball when Jane ⓒ<u>fell</u> down right in front of him. We ⓓ<u>helped</u> her up right away and ⓔ<u>were</u> very worried about her injured knee.",
   c=["ⓐ played는 규칙 과거형이다.", "ⓑ was running은 과거진행형이다.", "ⓒ는 fall의 과거형으로 불규칙 변화한 것이다.", "ⓓ helped는 규칙 과거형이다.", "ⓔ: 주어 We가 복수이지만 과거이므로 was를 써야 한다."], a=5,
   n=OKS(["played는 규칙 과거형이라 옳은 설명이므로", "was running은 과거진행형이라 옳은 설명이므로", "fell은 fall의 불규칙 과거형이라 옳은 설명이므로", "helped는 규칙 과거형이라 옳은 설명이므로", "복수 주어의 과거는 were이므로 ⓔ는 옳고 이 설명이 틀렸다. 옳지 않은 설명이므로"], 5), s=ADD(3, 40, "E", L40b + pos(5)))
RE(3, 40, "F", p="Last night, I ⓐ<u>read</u> a book about space in my room for an hour. My sister ⓑ<u>was watching</u> TV in the living room with our dog. Mom ⓒ<u>made</u> dinner for us while Dad was still at work. We ⓓ<u>ate</u> together at seven and ⓔ<u>went</u> to bed early.",
   c=["ⓐ: read는 현재형이므로 과거 문맥에서는 readed로 고쳐야 한다.", "ⓑ was watching은 과거진행형이다.", "ⓒ made는 make의 불규칙 과거형이다.", "ⓓ ate는 eat의 불규칙 과거형이다.", "ⓔ: 잠자리에 든 과거의 일을 불규칙 과거형 went로 나타냈다."], a=1,
   n=OKS(["read는 과거형도 철자가 read이므로 ⓐ는 옳고 이 설명이 틀렸다. 옳지 않은 설명이므로", "was watching은 과거진행형이라 옳은 설명이므로", "made는 make의 불규칙 과거형이라 옳은 설명이므로", "ate는 eat의 불규칙 과거형이라 옳은 설명이므로", "went는 go의 불규칙 과거형이라 옳은 설명이므로"], 1), s=ADD(3, 40, "F", L40b + pos(1)))

# ---- 3-44: 지문을 원문항 길이(30낱말) 이상으로 ----
RE(3, 44, "C", p="I really like this red bag, but it is too expensive for me. The blue _____ next to it is much cheaper.\nMy books are on the desk in my room. Can you bring _____ to the living room for me?", s=LENP)
RE(3, 44, "D", p="Those apples on the table look really sweet and fresh. Give me two big _____, please.\nMy keys are here on the counter. Please take _____ with you when you go out.", s=LENP)
RE(3, 44, "E", p="This phone is too old and slow for my games. I want a new _____ for my birthday next month.\nThe laptop is upstairs on my desk in my room. Bring _____ down to me, please.", s=LENP)
RE(3, 44, "F", p="These wooden chairs are too hard to sit on for long. The soft _____ in the corner are much better.\nMy coat and bag are over there by the door. Bring _____ to me, please.", s=LENP)

# ---- 3-45: 학생들의 예문을 원문항 길이(40낱말) 이상으로 ----
L45 = MEMO4 + "원문항보다 짧고 단조롭던 예문을 원문항 길이 이상으로 늘렸다. 판정과 정답은 그대로다."
RE(3, 45, "C", p="Tom: I hurt myself while I was cooking dinner.의 myself는 재귀 용법이라 생략할 수 없어.\nJane: This news about the test are good for us.은 news가 -s로 끝나서 옳은 문장이야.\nAmy: It's Sunday today.의 It과 It's my bag on the chair.의 It은 문법적으로 하는 역할이 같아.\nBen: I finished the whole project by myself.에서 by myself는 ‘혼자서’라는 뜻이야.\nMia: These is my notebooks for math class.는 옳은 문장이야.", s=ADD(3, 45, "C", L45))
RE(3, 45, "D", p="Leo: She herself did all the homework last night.의 herself는 생략해도 옳아.\nMina: Make yourself at home while I get some tea.는 ‘편하게 있어’라는 관용 표현이야.\nSam: Help yourselves to the cookies on the table.은 한 사람에게만 쓰는 표현이야.\nAmy: He looked at himself in the mirror for a long time.의 himself는 소유격이야.\nKai: That is a nice bag, and I want one, too.의 one은 bag을 대신해.", s=ADD(3, 45, "D", L45))
RE(3, 45, "E", p="Jane: I did it myself without any help from my parents.의 myself는 강조 용법이라 생략해도 옳아.\nTom: They talked to themselves quietly in the corner.에서 themselves를 them으로 바꿔도 뜻이 같아.\nBen: This scissors is sharp, so be careful with it.은 옳은 문장이야.\nMina: It's 7 o'clock now, so we should leave.의 It은 시간을 나타내는 비인칭 주어야.\nLeo: The glasses on the table are my, not yours.는 옳은 문장이야.", s=ADD(3, 45, "E", L45))
RE(3, 45, "F", p="Sam: The boy hurt himself when he fell off the bike.는 주어와 목적어가 같은 대상이야.\nAmy: She herself called me late last night.에서 herself를 빼면 틀린 문장이 돼.\nTom: Help yourself to the cake on the table.는 ‘케이크를 마음껏 먹어’라는 뜻이야.\nJane: We enjoyed ourselves at the beach last weekend.에서 ourselves는 단수 재귀대명사야.\nKai: It's far from here to the station.의 It은 거리를 나타내는 비인칭 주어야.", s=ADD(3, 45, "F", L45))

# ---- 3-47: 문장을 원문항 길이(9낱말) 이상으로 ----
RE(3, 47, "C", p="Tom called <u>she</u> yesterday to ask about the homework.", s=ADD(3, 47, "C", LEN))
RE(3, 47, "D", p="I saw <u>he</u> at the bus stop in front of the school.", s=ADD(3, 47, "D", LEN))
RE(3, 47, "E", p="Jane helped <u>they</u> with their science homework after school.", s=ADD(3, 47, "E", LEN))
RE(3, 47, "F", p="Mom gave <u>I</u> a gift for my birthday last Sunday.", s=ADD(3, 47, "F", LEN))

# ---- 3-49: 대화를 원문항 길이(24낱말) 이상으로 ----
RE(3, 49, "C", p="A: Kids, welcome! There is a big chocolate cake on the table.\nB: Wow, it looks really delicious!\nA: Please ____________ to the cake and some juice.\n(케이크를 마음껏 먹으렴.)", s=ADD(3, 49, "C", LENP))
RE(3, 49, "D", p="A: I'm going to the school festival with my friends tonight. We will watch the dance show.\nB: That sounds like fun! ____________! Don't come home too late.\n(즐거운 시간 보내!)", s=ADD(3, 49, "D", LENP))
RE(3, 49, "E", p="A: Tom and Jane, the museum is a very quiet place.\nB: Okay, we understand. We will be careful.\nA: Please ____________ inside and don't run around the exhibits.\n(안에서는 얌전히 행동하렴.)", s=ADD(3, 49, "E", LENP))
RE(3, 49, "F", p="A: Jane, there are some sandwiches and fruit on the kitchen table.\nB: Thanks! I'm really hungry after the game.\nA: Please ____________ to them. There is plenty for everyone.\n(마음껏 먹어.)", s=ADD(3, 49, "F", LENP))

# ---- 3-50: ⓐ~ⓔ 문장을 원문항 길이(30낱말) 이상으로 ----
RE(3, 50, "C", p="ⓐ I did all the homework myself without any help.\nⓑ Tom hurt himself while he was playing basketball.\nⓒ Jane enjoyed herself at the party last night.\nⓓ We helped us to some cake after the meeting.\nⓔ They saw themselves in the mirror and laughed.", s=ADD(3, 50, "C", LEN))
RE(3, 50, "D", p="ⓐ Help you to the cake on the table, Tom.\nⓑ My parents enjoyed theirselves at the party last weekend.\nⓒ She herself called me to say sorry.\nⓓ I hurt myself when I fell off my bike.\nⓔ We did it ourself without asking anyone for help.", s=ADD(3, 50, "D", LEN))
RE(3, 50, "E", p="ⓐ Make yourselves at home while I get some drinks, girls.\nⓑ He did it by himself in just one hour.\nⓒ Jane looked at herself in the new mirror.\nⓓ The boys enjoyed themself at the amusement park.\nⓔ I myself finished the whole report last night.", s=ADD(3, 50, "E", LEN))
RE(3, 50, "F", p="ⓐ You should believe in you when things get hard.\nⓑ We enjoyed us at the beach last summer.\nⓒ Tom cut himself while he was chopping the onions.\nⓓ Jane did it herselves without any help from her brother.\nⓔ The children helped themself to the cookies on the plate.", s=ADD(3, 50, "F", LEN))

# ---- 3-54: 대화를 원문항 길이(20낱말) 이상으로 ----
RE(3, 54, "C", p="A: Do you think it will rain this afternoon?\nB: It _____ rain later in the evening. I'm not sure, but the sky looks dark.", s=ADD(3, 54, "C", LENP))
RE(3, 54, "D", p="A: Where is Tom? I haven't seen him since lunch.\nB: He _____ be at the library, but I'm not certain about it.", s=ADD(3, 54, "D", LENP))
RE(3, 54, "E", p="A: Can Jane come to the party tonight?\nB: She _____ come after work. It's possible, but she hasn't decided yet.", s=ADD(3, 54, "E", LENP))
RE(3, 54, "F", p="A: Is the store near the station open on holidays?\nB: It _____ be closed today. I'm not sure, so let's call first.", s=ADD(3, 54, "F", LENP))

# ---- 3-55: ⓐ~ⓔ 문장을 원문항 길이(42낱말) 이상으로 ----
RE(3, 55, "C", p="ⓐ She <u>should study</u> harder for the final exam.\nⓑ They <u>might come</u> to the party a little late.\nⓒ We <u>must to leave</u> the house before seven.\nⓓ I <u>can help</u> you with your math homework.\nⓔ Tom <u>has to work</u> at the restaurant this weekend.", s=ADD(3, 55, "C", LEN))
RE(3, 55, "D", p="ⓐ I <u>will have to go</u> to the dentist tomorrow morning.\nⓑ Jane <u>can reads</u> English books without a dictionary.\nⓒ They <u>may are</u> late because of the heavy traffic.\nⓓ You <u>had better rest</u> at home for a few days.\nⓔ We <u>must studying</u> for the science test tonight.", s=ADD(3, 55, "D", LEN))
RE(3, 55, "E", p="ⓐ Tom <u>should goes</u> to bed early tonight because of the test.\nⓑ We <u>can play</u> basketball after school today.\nⓒ Jane <u>might be</u> home by six o'clock.\nⓓ They <u>have to leave</u> for the airport soon.\nⓔ I <u>will be able to help</u> you with the project next week.", s=ADD(3, 55, "E", LEN))
RE(3, 55, "F", p="ⓐ She <u>must is</u> tired after the long trip.\nⓑ Tom <u>can't is</u> at home at this time.\nⓒ We <u>should study</u> together for the history test.\nⓓ I <u>may goes</u> to the concert with my sister.\nⓔ They <u>can helps</u> us move the heavy boxes tomorrow.", s=ADD(3, 55, "F", LEN))

# ---- 3-56: 문장과 보기를 원문항 길이(7낱말, 보기 7낱말) 이상으로 ----
R56 = "will의 부정은 will not(won't) + 동사원형이다. do/does나 be동사로 부정하지 않고, won't 뒤의 동사에 -s를 붙이거나 to를 넣지 않는다."
RE(3, 56, "C", p="Jane will study at the library tonight.", c=["Jane isn't study at the library tonight.", "Jane won't study at the library tonight.", "Jane don't study at the library tonight.", "Jane won't studies at the library tonight.", "Jane will not to study at the library tonight."], a=2, r=R56,
   n=OKS(["will의 부정에 be동사 isn't를 쓸 수 없으므로", "will not(won't) + 동사원형으로 바르게 바꿨으므로", "조동사 will의 부정에 don't를 쓰지 않으므로", "won't 뒤에는 동사원형 study를 써야 하므로", "will not 뒤에 to를 넣을 수 없으므로"], 2), s=LEN + pos(2))
RE(3, 56, "D", p="Tom will be busy with his homework tomorrow.", c=["Tom won't is busy with his homework tomorrow.", "Tom will not to be busy with his homework tomorrow.", "Tom isn't be busy with his homework tomorrow.", "Tom don't be busy with his homework tomorrow.", "Tom won't be busy with his homework tomorrow."], a=5, r=R56,
   n=OKS(["won't 뒤에는 동사원형 be를 써야 하므로", "will not 뒤에 to를 넣을 수 없으므로", "will이 사라지고 be동사 뒤에 동사원형이 왔으므로", "조동사 will의 부정에 don't를 쓰지 않으므로", "won't + 동사원형 be로 바르게 바꿨으므로"], 5), s=LEN + pos(5))
RE(3, 56, "E", p="We will leave for the station early tomorrow.", c=["We isn't leave for the station early tomorrow.", "We won't leave for the station early tomorrow.", "We will not to leave for the station early tomorrow.", "We won't leaves for the station early tomorrow.", "We don't leave for the station early tomorrow."], a=2, r=R56,
   n=OKS(["will의 부정에 be동사 isn't를 쓸 수 없으므로", "won't + 동사원형으로 바르게 바꿨으므로", "will not 뒤에 to를 넣을 수 없으므로", "won't 뒤에는 동사원형 leave를 써야 하므로", "조동사 will의 부정에 don't를 쓰지 않으므로"], 2), s=LEN + pos(2))
RE(3, 56, "F", p="I will help you with the dishes after dinner.", c=["I isn't help you with the dishes after dinner.", "I won't help you with the dishes after dinner.", "I won't helps you with the dishes after dinner.", "I will not to help you with the dishes after dinner.", "I don't help you with the dishes after dinner."], a=2, r=R56,
   n=OKS(["will의 부정에 be동사 isn't를 쓸 수 없으므로", "won't + 동사원형으로 바르게 바꿨으므로", "won't 뒤에는 동사원형 help를 써야 하므로", "will not 뒤에 to를 넣을 수 없으므로", "조동사 will의 부정에 don't를 쓰지 않으므로"], 2), s=LEN + pos(2))

# ---- 3-57: 보기 문장을 원문항 길이(평균 6낱말) 이상으로 ----
R57 = OLD(3, 57, "C")["r"]
STV = "상태동사({})는 진행형으로 쓰지 않으므로"; ACT = "동작동사를 be동사 + -ing의 진행형으로 바르게 썼으므로"
RE(3, 57, "C", c=["He <u>is preferring</u> tea to coffee in the morning.", "She <u>is watching</u> a movie with her friends now.", "I <u>am needing</u> some help with this problem.", "This bag <u>is belonging</u> to my older sister.", "We <u>are understanding</u> the rule of the game now."], a=2, r=R57,
   n=OKS([STV.format("prefer"), ACT, STV.format("need"), STV.format("belong"), STV.format("understand")], 2), s=ADD(3, 57, "C", LEN))
RE(3, 57, "D", c=["The box <u>is containing</u> old books and letters.", "I <u>am seeming</u> tired after the long meeting.", "Mina <u>is resembling</u> her mom more and more.", "We <u>are recognizing</u> his voice on the phone.", "Dad <u>is washing</u> the car in the driveway now."], a=5, r=R57,
   n=OKS([STV.format("contain"), STV.format("seem"), STV.format("resemble"), STV.format("recognize"), ACT], 5), s=ADD(3, 57, "D", LEN))
RE(3, 57, "E", c=["Jane <u>is running</u> in the park with her dog.", "I <u>am knowing</u> his secret about the test.", "He <u>is wanting</u> a new bike for his birthday.", "We <u>are believing</u> in you no matter what.", "This pen <u>is belonging</u> to Tom, not to me."], a=1, r=R57,
   n=OKS([ACT, STV.format("know"), STV.format("want"), STV.format("believe"), STV.format("belong")], 1), s=ADD(3, 57, "E", LEN))
RE(3, 57, "F", c=["I <u>am needing</u> a rest after the long game.", "She <u>is having</u> long hair and brown eyes.", "The soup <u>is tasting</u> too salty for me.", "They <u>are singing</u> a song on the school stage.", "He <u>is hating</u> spiders and other small bugs."], a=4, r=R57,
   n=OKS([STV.format("need"), "‘가지고 있다’는 뜻의 상태동사(have)는 진행형으로 쓰지 않으므로", "‘~한 맛이 나다’는 뜻의 상태동사(taste)는 진행형으로 쓰지 않으므로", ACT, STV.format("hate")], 4), s=ADD(3, 57, "F", LEN))

# ---- 3-58: 문장 길이 + ‘be동사 뒤 -ing = 정답’ 단서 차단(be동사 뒤 동명사 보어, 명사를 꾸미는 현재분사를 오답에) ----
R58 = "be동사 뒤에서 ‘~하고 있다’는 진행형을 만드는 -ing는 현재분사다. be동사 뒤에 있어도 ‘~하는 것’으로 풀리면 보어로 쓰인 동명사이고, 주어·목적어·전치사의 목적어로 쓰인 -ing도 동명사다. 명사를 꾸미는 -ing는 현재분사지만 진행형은 아니다."
L58 = MEMO4 + "원문항보다 짧던 문장을 늘리고, be동사 뒤의 -ing만 찾으면 풀리지 않게 원문항처럼 be동사 뒤 동명사 보어(My hobby is collecting ~ 식)와 명사를 꾸미는 현재분사를 오답에 넣었다."
GER = "{}의 목적어로 쓰인 동명사라 <보기>와 쓰임이 다르므로"; SUBJ = "문장의 주어로 쓰인 동명사라 <보기>와 쓰임이 다르므로"
def CMP(v): return f"be동사 뒤에 있지만 ‘{v}’이라는 뜻의 보어(동명사)라 진행형이 아니므로"
def PRT(nn): return f"명사 {nn}을 꾸미는 현재분사지만 진행형은 아니므로"
def PRG(be, v, kr): return f"{be} + {v}로 ‘{kr}’는 진행형을 만드는 현재분사라 <보기>와 쓰임이 같으므로"
RE(3, 58, "C", p="<보기>\nJane is <u>writing</u> an email to her teacher now.",
   c=["He finished <u>cleaning</u> his room before his mom came home.", "My favorite hobby is <u>collecting</u> old stamps from many countries.", "They were <u>playing</u> soccer in the rain at five o'clock.", "The girl <u>talking</u> to the teacher is my younger sister.", "She avoided <u>eating</u> sweets before going to bed at night."], a=3, r=R58,
   n=OKS([GER.format("finish"), CMP("모으는 것"), PRG("were", "playing", "하고 있었다"), PRT("The girl"), GER.format("avoid")], 3), s=ADD(3, 58, "C", L58 + pos(3)))
RE(3, 58, "D", p="<보기>\nThe dogs were <u>barking</u> loudly at the stranger last night.",
   c=["We enjoyed <u>dancing</u> at the party until late at night.", "<u>Reading</u> comic books is my favorite way to relax.", "His job is <u>selling</u> used cars at a small shop.", "Jane was <u>reading</u> a novel when I called her last night.", "The man <u>waiting</u> at the door is my uncle."], a=4, r=R58,
   n=OKS([GER.format("enjoy"), SUBJ, CMP("파는 것"), PRG("was", "reading", "읽고 있었다"), PRT("The man")], 4), s=ADD(3, 58, "D", L58 + pos(4)))
RE(3, 58, "E", p="<보기>\nMom is <u>making</u> lunch for us in the kitchen right now.",
   c=["I love <u>swimming</u> in the sea with my cousins.", "How about <u>going</u> out for a walk after dinner?", "Her dream is <u>becoming</u> a famous pianist someday.", "The boy <u>sitting</u> on the bench is my classmate.", "Tom was <u>sleeping</u> on the sofa at ten last night."], a=5, r=R58,
   n=OKS([GER.format("love"), "전치사 about의 목적어로 쓰인 동명사라 <보기>와 쓰임이 다르므로", CMP("되는 것"), PRT("The boy"), PRG("was", "sleeping", "자고 있었다")], 5), s=ADD(3, 58, "E", L58 + pos(5)))
RE(3, 58, "F", p="<보기>\nThe children are <u>laughing</u> together at the funny clown.",
   c=["We were <u>studying</u> for the exam all evening at home.", "Would you mind <u>opening</u> the window for a minute?", "<u>Learning</u> a new language takes a lot of time.", "My plan is <u>visiting</u> my grandparents this winter.", "The woman <u>wearing</u> a red hat is our teacher."], a=1, r=R58,
   n=OKS([PRG("were", "studying", "공부하고 있었다"), GER.format("mind"), SUBJ, CMP("방문하는 것"), PRT("The woman")], 1), s=ADD(3, 58, "F", L58 + pos(1)))

# ---- 3-59: ㉠~㉣ 문장을 원문항 길이(27낱말) 이상으로 ----
RE(3, 59, "C", p="㉠ Jane is reading a book under the tree.\n㉡ Tom are sleeping on the sofa right now.\n㉢ We are studying for the math test together.\n㉣ The boys is playing basketball in the gym.", s=ADD(3, 59, "C", LEN))
RE(3, 59, "D", p="㉠ I is making a sandwich for my lunch.\n㉡ She is know the answer to this question.\n㉢ They are running to the bus stop now.\n㉣ We are cleaning the classroom after school today.", s=ADD(3, 59, "D", LEN))
RE(3, 59, "E", p="㉠ Tom is watching TV with his little brother.\n㉡ They are sitting on the bench in the park.\n㉢ Jane is writting a letter to her pen pal.\n㉣ I am study for the English test now.", s=ADD(3, 59, "E", LEN))
RE(3, 59, "F", p="㉠ We are leaving for the airport in an hour.\n㉡ She is want a new bag for the trip.\n㉢ The dog is barking at the cat next door.\n㉣ Tom are working at his uncle's store today.", s=ADD(3, 59, "F", LEN))

# ---- 3-60: ⓐ~ⓔ 문장을 원문항 길이(28낱말) 이상으로 ----
RE(3, 60, "C", p="ⓐ Jane didn't go home right after school today.\nⓑ Did Tom saw the movie with his friends last night?\nⓒ We can help you carry the heavy boxes.\nⓓ She must to study for the test tonight.\nⓔ They might visit their grandparents this weekend.", s=ADD(3, 60, "C", LEN))
RE(3, 60, "D", p="ⓐ I didn't eat lunch because I wasn't hungry.\nⓑ Did they go to the beach last weekend?\nⓒ Tom can reads very fast for his age.\nⓓ Jane should rest before the big game tomorrow.\nⓔ We must study hard for the final exam.", s=ADD(3, 60, "D", LEN))
RE(3, 60, "E", p="ⓐ They didn't see me at the station yesterday.\nⓑ Did Jane wrote a letter to her grandmother?\nⓒ Tom might is at home with his brother now.\nⓓ We can plays the piano and the violin.\nⓔ I had better to go to bed early tonight.", s=ADD(3, 60, "E", LEN))
RE(3, 60, "F", p="ⓐ He didn't bought the ticket for the concert.\nⓑ Did they come to the meeting on time?\nⓒ We should leave now to catch the last bus.\nⓓ Jane may be late because of the traffic.\nⓔ Tom can help us paint the fence this weekend.", s=ADD(3, 60, "F", LEN))

# ---- 3-67: 문장과 보기를 원문항 길이(7낱말, 보기 7낱말) 이상으로 ----
RE(3, 67, "C", p="What she will buy at the mall tomorrow?", c=["What does she will buy at the mall tomorrow?", "What will be she buy at the mall tomorrow?", "Will what she buy at the mall tomorrow?", "What will she buy at the mall tomorrow?", "What she will buy at the mall tomorrow?"], s=ADD(3, 67, "C", LEN))
RE(3, 67, "D", p="When they will leave for the airport?", c=["When do they will leave for the airport?", "When will be they leave for the airport?", "Will when they leave for the airport?", "When they will leave for the airport?", "When will they leave for the airport?"], s=ADD(3, 67, "D", LEN))
RE(3, 67, "E", p="Why Tom will go there again next week?", c=["Why will Tom go there again next week?", "Why Tom will go there again next week?", "Will why Tom go there again next week?", "Why will be Tom go there again next week?", "Why does Tom will go there again next week?"], s=ADD(3, 67, "E", LEN))
RE(3, 67, "F", p="How we will get home after the concert?", c=["Will how we get home after the concert?", "How do we will get home after the concert?", "How we will get home after the concert?", "How will be we get home after the concert?", "How will we get home after the concert?"], s=ADD(3, 67, "F", LEN))

# ---- 3-75: ⓐ~ⓔ 문장을 원문항 길이(35낱말) 이상으로 ----
RE(3, 75, "C", p="ⓐ I want <u>to learn</u> English from a native speaker.\nⓑ She decided <u>going</u> home early because of the rain.\nⓒ We need something <u>to eat</u> before the long trip.\nⓓ It is easy <u>to use</u> this new phone.\nⓔ Tom enjoys <u>to swim</u> in the river every summer.", s=ADD(3, 75, "C", LEN))
RE(3, 75, "D", p="ⓐ I have a book <u>to read</u> on the train.\nⓑ She is too tired <u>to work</u> on the project tonight.\nⓒ He wants <u>learning</u> English to travel abroad.\nⓓ We know <u>how to get</u> to the museum from here.\nⓔ It is fun <u>to travel</u> with good friends.", s=ADD(3, 75, "D", LEN))
RE(3, 75, "E", p="ⓐ Jane has a lot of homework <u>to do</u> tonight.\nⓑ Tom decided <u>to leave</u> the club last month.\nⓒ I enjoy <u>to read</u> mystery novels in my free time.\nⓓ We need a pen <u>to write with</u> for the test.\nⓔ It is hard <u>to understand</u> his strong accent.", s=ADD(3, 75, "E", LEN))
RE(3, 75, "F", p="ⓐ I want <u>to go</u> to the concert with you.\nⓑ She has a comfortable chair <u>to sit on</u> in her room.\nⓒ They are <u>enough strong</u> to lift the heavy table.\nⓓ He knows <u>what to say</u> in this situation.\nⓔ We need more time <u>finishing</u> the group project.", s=ADD(3, 75, "F", LEN))

# ---- 3-83: 보기 문장을 원문항 길이(평균 5낱말) 이상으로 ----
RE(3, 83, "C", c=["I stopped <u>eating</u> sweets after my visit to the dentist.", "Look at the <u>running</u> dog over there by the fence.", "<u>Keeping</u> a pet is not easy for a busy student.", "She is afraid of <u>flying</u> in a small plane.", "His favorite hobby is <u>fishing</u> at the lake on weekends."], s=ADD(3, 83, "C", LEN))
RE(3, 83, "D", c=["<u>Watching</u> old movies is fun on a rainy day.", "We talked about <u>camping</u> by the lake this summer.", "I love <u>baking</u> bread for my family on Sundays.", "Would you mind <u>opening</u> the window a little?", "Tom was <u>playing</u> the guitar on the stage last night."], s=ADD(3, 83, "D", LEN))
RE(3, 83, "E", c=["<u>Riding</u> a bike along the river is really fun.", "The girl <u>singing</u> on the stage is my sister.", "They were <u>waiting</u> for the bus in the rain.", "Who is the man <u>standing</u> at the front door?", "The children are <u>laughing</u> loudly in the backyard."], s=ADD(3, 83, "E", LEN))
RE(3, 83, "F", c=["He left the room without <u>saying</u> goodbye to anyone.", "<u>Getting</u> up early every day is hard for me.", "Jane is <u>writing</u> a report about her trip to Canada.", "They enjoyed <u>singing</u> together at the school festival.", "I'm interested in <u>learning</u> Chinese and Japanese."], s=ADD(3, 83, "F", LEN))

# ---- 3-95 C: 원문항의 판정 포인트(a- 형용사의 한정 용법, 목적격보어)를 그대로 따르던 두 학생을 다른 포인트로, 예문도 원문항 길이 이상으로 ----
RE(3, 95, "C", p="Emma: 'He runs fast in every race.'에서 fast는 -ly 없이 부사로 쓰여 옳은 문장이야.\nLeo: 'He plays the piano very good.'는 그가 피아노를 매우 잘 친다는 옳은 문장이야.\nMia: 'Jane is a careful driver.'에서 형용사 careful이 명사 driver를 꾸며서 옳은 문장이야.\nOlivia: 'There are a little apples in the basket.'에서 a little은 ‘조금 있는’이라는 뜻이라 옳은 문장이야.\nZoe: 'She sings beautifully at the school festival.'에서 부사가 동사를 꾸며서 옳은 문장이야.",
   r=OLD(3, 95, "C")["r"] + " good은 형용사, well은 부사다.",
   pre=["설명별 판정: Emma O. fast는 형용사와 부사의 형태가 같다.", "설명별 판정: Leo X. 동사 plays를 꾸미는 말은 부사 well이다(good은 형용사).", "설명별 판정: Mia O. 형용사가 명사 driver를 꾸민다.", "설명별 판정: Olivia X. apples는 셀 수 있는 명사라 a few를 써야 한다.", "설명별 판정: Zoe O. 부사 beautifully가 동사 sings를 꾸민다."],
   s=ADD(3, 95, "C", MEMO4 + "원문항의 판정 포인트(asleep·alive 같은 a- 형용사, 목적격보어 자리의 형용사)를 그대로 따르던 Leo·Mia의 예문을 다른 포인트(good/well, 명사를 꾸미는 형용사)로 바꾸고 예문을 원문항 길이 이상으로 늘렸다. 보기와 정답은 그대로다."))

# ---- 3-96: 문장을 원문항 길이(6낱말) 이상으로 ----
RE(3, 96, "C", p="Tom looks <u>tiredly</u> after the long trip.", s=ADD(3, 96, "C", LEN))
RE(3, 96, "D", p="The soup smells <u>nicely</u> with fresh herbs.", s=ADD(3, 96, "D", LEN))
RE(3, 96, "E", p="Jane seems <u>happily</u> with her new school.", s=ADD(3, 96, "E", LEN))
RE(3, 96, "F", p="The sky became <u>darkly</u> before the storm.", s=ADD(3, 96, "F", LEN))

# ---- 3-98: 대화를 원문항 길이(42낱말) 이상으로 ----
RE(3, 98, "C", p="Mom: How (A)________ milk is left in the fridge? I want to make some pancakes.\nSon: There's very (B)________. Only half a cup, I think. We need to buy some.\nMom: Okay, I'll go to the store. Do we need eggs, too?\nSon: Yes. We don't have (C)________ eggs, either. There are only two left.", s=ADD(3, 98, "C", LENP))
RE(3, 98, "D", p="Minji: There is (A)________ snow outside! The whole street is white.\nSuho: Yes, it snowed all night. But there was very (B)________ snow last year, right?\nMinji: Right. Let's make a snowman before it melts. Can you bring (C)________ buttons for its eyes?\nSuho: Sure. I have two black ones in my room.", s=ADD(3, 98, "D", LENP))
RE(3, 98, "E", p="Teacher: Only five students came to class today. Why are there so (A)________ students?\nMina: There is a school festival in the gym. (B)________ students went there to watch the show.\nTeacher: I see. Then we don't have (C)________ work to do today. Let's just review the last lesson.", s=ADD(3, 98, "E", LENP))
RE(3, 98, "F", p="Amy: Can I have (A)________ water, please? I'm really thirsty after the long walk.\nDad: Sure. Here you are. Drink slowly.\nAmy: Thanks. Wow, there are (B)________ people in this park today! Is there a festival?\nDad: Maybe. Last week, there were very (C)________ people here because of the heavy rain.", s=ADD(3, 98, "F", LENP))

# ---- 3-109: 문장을 원문항 길이(9낱말) 이상으로 ----
RE(3, 109, "C", p="Tom is <u>far taller than</u> his older brother Ben.", s=ADD(3, 109, "C", LEN))
RE(3, 109, "E", p="This leather bag is <u>much heavier than</u> that one.", s=ADD(3, 109, "E", LEN))

# ---- 3-115: ⓐ~ⓓ 문장을 원문항 길이(25낱말) 이상으로 ----
RE(3, 115, "C", p="ⓐ We meet on Monday for our weekly club activity.\nⓑ Tom lives at Seoul with his aunt and uncle.\nⓒ The book is on the desk next to the lamp.\nⓓ I arrived in 8 o'clock, but the store was closed.", s=ADD(3, 115, "C", LEN))
RE(3, 115, "D", p="ⓐ We meet at Friday after the last class.\nⓑ Jane was born in 2012 in a small town.\nⓒ Tom waits at the gate for his sister every day.\nⓓ The cat is sleeping in the table in the kitchen.", s=ADD(3, 115, "D", LEN))
RE(3, 115, "E", p="ⓐ School starts on nine every weekday morning.\nⓑ We travel in summer with our grandparents.\nⓒ I was born at 2011 in Busan.\nⓓ We meet on May 5th at the park.", s=ADD(3, 115, "E", LEN))
RE(3, 115, "F", p="ⓐ I was born on 2015 in a big city.\nⓑ The bag is among the two chairs by the window.\nⓒ Jane is at home with her little sister today.\nⓓ We meet at noon in front of the library.", s=ADD(3, 115, "F", LEN))

# ---- 3-116: 문장을 원문항 길이(6낱말) 이상으로 ----
RE(3, 116, "C", p="We usually meet at the library _____ Monday.\n(우리는 보통 월요일에 도서관에서 만난다.)", s=ADD(3, 116, "C", LEN))
RE(3, 116, "D", p="My cousin Tom was born _____ 2010, two years after me.\n(내 사촌 Tom은 나보다 2년 뒤인 2010년에 태어났다.)", s=ADD(3, 116, "D", LEN))
RE(3, 116, "E", p="Jane usually travels abroad with her family _____ August.\n(Jane은 보통 8월에 가족과 해외여행을 한다.)", s=ADD(3, 116, "E", LEN))
RE(3, 116, "F", p="The birthday party for my sister is _____ May 5th.\n(내 여동생의 생일 파티는 5월 5일에 열린다.)", s=ADD(3, 116, "F", LEN))

# ---- 3-119: 대화와 보기를 원문항 길이(13낱말, 보기 7낱말) 이상으로 ----
L119 = MEMO4 + "원문항보다 짧던 대화와 보기 문장을 원문항 길이 이상으로 늘렸다. 정답 위치는 그대로다."
RE(3, 119, "C", p="A: Excuse me. Where is the new cafe around here?\nB: <u>그것은 큰 학교 정문 바로 옆에 있어</u>.\nA: Thanks. I'll go there right now.",
   c=["It's right next to the big school gate.", "It's right behind the big school gate.", "It's right next of the big school gate.", "It's right in front of the big school gate.", "It's right across from the big school gate."], s=ADD(3, 119, "C", L119))
RE(3, 119, "D", p="A: Excuse me. Where is the city park?\nB: <u>그것은 시립 중앙 도서관 바로 맞은편에 있어</u>.\nA: Thanks a lot. Have a nice day.",
   c=["It's right next to the main city library.", "It's right across of the main city library.", "It's right behind the main city library.", "It's right in front of the main city library.", "It's right across from the main city library."], s=ADD(3, 119, "D", L119))
RE(3, 119, "E", p="A: Mom, where is my school bag?\nB: <u>그것은 낡은 부엌 의자 바로 아래에 있어</u>.\nA: Oh, I see it. Thank you.",
   c=["It's right on the old kitchen chair.", "It's right next to the old kitchen chair.", "It's right under the old kitchen chair.", "It's right under of the old kitchen chair.", "It's right behind the old kitchen chair."], s=ADD(3, 119, "E", L119))
RE(3, 119, "F", p="A: Excuse me. Where is the flower store?\nB: <u>그것은 큰 은행 바로 앞에 있어</u>.\nA: Thank you very much for your help.",
   c=["It's right in front the big bank.", "It's right in front of the big bank.", "It's right behind the big bank.", "It's right across from the big bank.", "It's right in the front of the big bank."], s=ADD(3, 119, "F", L119))

# ---- 3-120: <보기> 문장을 원문항 길이(37낱말) 이상으로 ----
RE(3, 120, "C", p="<보기>\nⓐ Tom was born on 2010 in a small village.\nⓑ We meet at seven in front of the station.\nⓒ Jane lives in Seoul with her grandparents.\nⓓ I waited by two hours for the late bus.\nⓔ The book is on the desk in my room.", s=ADD(3, 120, "C", LEN))
RE(3, 120, "D", p="<보기>\nⓐ The first class starts on eight every morning.\nⓑ We traveled during summer vacation with our cousins.\nⓒ Tom lives at Korea with his parents now.\nⓓ Finish it until Friday, or you will lose points.\nⓔ The bag is among two chairs in the hall.", s=ADD(3, 120, "D", LEN))
RE(3, 120, "E", p="<보기>\nⓐ I was born on May in a small town near Busan.\nⓑ We meet in Monday at the library after school.\nⓒ I have waited since two hours for his call.\nⓓ It rained during two hours this afternoon.\nⓔ We have a party at Christmas Day every year.", s=ADD(3, 120, "E", LEN))
RE(3, 120, "F", p="<보기>\nⓐ Jane is at home because she has a cold.\nⓑ Tom was born on May 3rd in Jeju.\nⓒ We stayed there by three hours after the show.\nⓓ Finish the work by five, and then we can go.\nⓔ The cat is on the table near the window.", s=ADD(3, 120, "F", LEN))

# ---- 3-98 C·E: 보기도 원문항처럼 a lot of·a few·a little을 섞어 길이를 맞춤 ----
RE(3, 98, "C", c=["many - little - much", "much - a few - many", "much - little - many", "much - a little - much", "a lot of - few - many"], a=3,
   n=OKS(["(A) many와 (C) much: milk는 셀 수 없어 much, eggs는 셀 수 있어 many를 써야 하므로", "(B) a few: 셀 수 없는 milk를 가리키므로 little을 써야 하므로", "(A) 셀 수 없는 milk에 much, (B) ‘거의 없다’는 뜻의 little, (C) 셀 수 있는 eggs에 many가 모두 알맞으므로", "(B) a little: very 뒤에 쓸 수 없고 ‘조금 있다’는 뜻이라 사야 한다는 흐름과 맞지 않으며, (C) much: 셀 수 있는 eggs에는 many를 써야 하므로", "(A) a lot of: How 뒤의 수량 의문에는 much를 쓰고, (B) few: 셀 수 없는 milk에는 little을 써야 하므로"], 3),
   s=ADD(3, 98, "C", MEMO4 + "보기도 원문항처럼 a lot of·a few·a little을 섞어 길이를 맞췄다. 정답 위치는 그대로다."))
RE(3, 98, "E", c=["a few - Much - much", "few - Much - many", "little - A lot of - many", "few - Many - much", "many - A few - a lot of"], a=4,
   n=OKS(["(A) a few: ‘다섯 명뿐’이라 ‘거의 없는’ few가 알맞고, (B) Much: 셀 수 있는 students에는 Many를 써야 하므로", "(B) Much: 셀 수 있는 students에는 Many를, (C) many: 셀 수 없는 work에는 much를 써야 하므로", "(A) little: 셀 수 있는 students에는 few를, (C) many: 셀 수 없는 work에는 much를 써야 하므로", "(A) 다섯 명뿐이라 ‘거의 없는’ few, (B) 셀 수 있는 students에 Many, (C) 셀 수 없는 work에 much가 모두 알맞으므로", "(A) many: 다섯 명뿐인데 ‘많다’는 뜻이라 맞지 않고, (B) A few: 대부분이 축제에 갔다는 흐름과 맞지 않으므로"], 4),
   s=ADD(3, 98, "E", MEMO4 + "보기도 원문항처럼 a lot of·a few·a little을 섞어 길이를 맞췄다. 정답 위치는 그대로다."))
