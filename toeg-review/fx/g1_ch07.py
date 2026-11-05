# 1급 CH7 분사 (61~70) 수정 예시

# 1-61 감정분사: 괄호 조건 대신 -ing가 성립하지 않는 felt ___ 문장으로, 줄바꿈 복원
R61 = "사람이 감정을 느끼는 상태는 -ed 분사, 감정을 일으키는 원인·성질은 -ing 분사로 나타낸다. felt(느꼈다) 뒤에는 느낀 감정 상태가 온다."
NEED61 = ["(A)는 주절의 주어가 소식에 놀란 상태이므로 -ed 분사를 쓴다.", "(B)는 felt 뒤에서 주어가 느낀 감정 상태이므로 -ed 분사를 쓴다."]
F(1, 61, "B", st="R", p="(A) _____ by the sudden news, we remained silent.\n(B) Leo felt _____ after losing the match.", r=R61,
  k="(A) 소식에 충격을 받은 상태, (B) Leo가 느낀 실망이므로 Shocked - disappointed가 알맞다.",
  n=["(A) Surprised는 놀란 상태라 맞지만, (B) disappointing은 ‘실망스러운’ 성질이라 felt 뒤 Leo가 느낀 감정과 맞지 않는다. 오답이다.",
     "(B) disappointing: felt 뒤에는 Leo가 느낀 감정 상태(-ed)가 와야 한다. 오답이다.",
     "(A) Shocked는 우리가 충격받은 상태, (B) disappointed는 Leo가 느낀 실망이다. 정답이다.",
     "(A) Shocking은 충격을 주는 성질이라 우리가 충격받은 상태와 맞지 않고, (B) disappointing도 느낀 감정이 아니다. 오답이다.",
     "(A) Shocking은 충격을 주는 성질이라 우리가 충격받은 상태와 맞지 않는다. 오답이다."],
  s="발문 괄호 ‘(B는 다른 사람에게 주는 인상을 말하는 것이 아니다)’가 -ed를 고르라는 단서였고, 괄호가 없으면 ‘looked disappointing’도 가능했다. (B)를 -ing가 성립하지 않는 ‘felt ___’로 바꾸고 괄호를 지웠다. 두 줄로 나눴다.")
for t in "CDF":
    F(1, 61, t, p=V(1, 61, t)["passage"].replace(" / ", "\n"), keepx=True, s="‘/’로 이어 쓴 (A)(B) 두 문장을 원문항처럼 두 줄로 나눴다.")
F(1, 61, "E", st="R", p="(A) _____ with the result, the coach praised the players.\n(B) The child felt _____ in the dark room.", r=R61,
  k="(A) 결과에 만족한 상태, (B) 아이가 느낀 두려움이므로 Pleased - frightened가 알맞다.",
  n=["(A) Pleasing은 기쁨을 주는 성질이라 코치가 만족한 상태와 맞지 않고, (B) frightening도 아이가 느낀 감정이 아니다. 오답이다.",
     "(A) Satisfied는 만족한 상태라 맞지만, (B) frightening은 ‘무서운’ 성질이라 felt 뒤 아이가 느낀 감정과 맞지 않는다. 오답이다.",
     "(A) Pleasing은 기쁨을 주는 성질이라 코치가 만족한 상태와 맞지 않는다. 오답이다.",
     "(A) Pleased는 코치가 만족한 상태, (B) frightened는 아이가 느낀 두려움이다. 정답이다.",
     "(B) frightening: felt 뒤에는 아이가 느낀 감정 상태(-ed)가 와야 한다. 오답이다."],
  s="괄호가 없으면 ‘became frightening’도 가능해 발문 조건에 기댔다. (B)를 ‘felt ___’로 바꾸고 괄호를 지웠다. 두 줄로 나눴다.")

# 1-62 with + 목적어 + 분사: 원문항처럼 제시문 + with 구 다섯 개, 옳은 -ing 용법 하나 포함
R62 = "with + 목적어 + 분사에서 목적어가 스스로 하는 동작이면 현재분사(-ing), 행동을 받은 뒤의 상태이면 과거분사(-ed)를 쓴다."
S62 = "원문항의 제시문이 사라지고 발문이 뜻을 길게 설명했으며, 정답만 완전한 문장이라 형태만 보고 고를 수 있었다. 원문항처럼 제시문 한 문장 + with 구 다섯 개로 바꾸고, 옳은 -ing 용법(목적어가 스스로 움직임)을 하나 넣었다. C~F와 겹치던 오답도 유형마다 새로 썼다."
def w62(x, obj, ok, why): return (f"‘{x}’: {why} 올바르다. 오답이다." if ok else f"‘{x}’: {why} 틀렸다. 정답이다.")
def f62(t, sent, items, a):
    F(1, 62, t, st="R", p=sent, c=[x[0] for x in items], a=a, r=R62, n=[w62(x[0], "", i + 1 != a, x[1]) for i, x in enumerate(items)], s=S62 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f62("B", "Mina was reading a book ___________.",
    [("with her feet crossed", "발이 꼬인 상태이므로 과거분사가"), ("with the TV turned off", "TV가 꺼진 상태이므로 과거분사가"), ("with her cat sleeping on her lap", "고양이가 스스로 자고 있으므로 현재분사가"),
     ("with her hair tying back", "머리가 묶인 상태이므로 과거분사 tied가 와야 하는데 현재분사를 써서"), ("with the curtains drawn", "커튼이 쳐진 상태이므로 과거분사가")], 4)
f62("C", "Tom sat on the bench ___________.",
    [("with his legs stretched out", "다리를 뻗은 상태이므로 과거분사가"), ("with his hands folding", "손이 모아진 상태이므로 과거분사 folded가 와야 하는데 현재분사를 써서"), ("with birds singing around him", "새들이 스스로 노래하므로 현재분사가"),
     ("with his cap pulled down", "모자가 눌러 쓰인 상태이므로 과거분사가"), ("with his phone switched off", "전화기가 꺼진 상태이므로 과거분사가")], 2)
f62("D", "The old man fell asleep ___________.",
    [("with the radio playing", "라디오가 스스로 소리를 내고 있으므로 현재분사가"), ("with his glasses left on", "안경이 씌워진 채 남은 상태이므로 과거분사가"), ("with a blanket covered him", "a blanket 뒤에 과거형 동사가 와서 분사 자리가 아니고, 담요가 덮은 뜻이면 covering이 와야 하므로"),
     ("with his hands resting on his stomach", "손이 배 위에 얹혀 있는 동작(rest)이므로 현재분사가"), ("with his book placed on his chest", "책이 놓인 상태이므로 과거분사가")], 3)
f62("E", "Jane listened to the lecture ___________.",
    [("with her bag hung on the chair", "가방이 의자에 걸린 상태이므로 과거분사가"), ("with her pen moving quickly", "펜이 빠르게 움직이고 있으므로 현재분사가"), ("with her phone put away", "전화기가 치워진 상태이므로 과거분사가"),
     ("with her eyes fixed on the speaker", "시선이 고정된 상태이므로 과거분사가"), ("with her arms crossing", "팔이 팔짱 낀 상태이므로 과거분사 crossed가 와야 하는데 현재분사를 써서")], 5)
f62("F", "The children waited for the bus ___________.",
    [("with their bags packed", "가방이 싸인 상태이므로 과거분사가"), ("with snow falling around them", "눈이 스스로 내리고 있으므로 현재분사가"), ("with their coats zipping up", "코트 지퍼가 올려진 상태이므로 과거분사 zipped가 와야 하는데 현재분사를 써서"),
     ("with their hats pulled over their ears", "모자가 귀까지 덮인 상태이므로 과거분사가"), ("with their parents watching them", "부모님이 스스로 지켜보고 있으므로 현재분사가")], 3)

# 1-63 완료 수동 분사구문: 발문을 원문항대로
R63 = "주절보다 먼저 일어났고 주어가 그 일을 당했으면 분사구문을 Having been + 과거분사로 쓴다."
def g63(x, pp):
    if x.startswith("Having been "): return "주절보다 먼저 일어났고 주어가 그 일을 당했으므로 Having been + 과거분사가 알맞다. 정답이다."
    if x.startswith("Having "): return f"Having + 과거분사는 능동이라 주어가 그 일을 당한 관계를 나타내지 못한다."
    if x.startswith("Being "): return "Being + 과거분사는 주절과 같은 때의 일로 읽혀, 먼저 일어난 일을 분명히 나타내지 못한다."
    if x.startswith("To be "): return "To be + 과거분사는 앞으로의 일이나 목적을 나타내 분사구문이 아니다."
    return "현재분사로 시작하면 주어가 그 일을 직접 했다는 능동의 뜻이 되어 맞지 않는다."
ING63 = {"B": "Destroying by the flood years ago", "C": "Hiding for decades", "D": "Damaging in the earthquake", "E": "Deleting accidentally", "F": "Stealing from the museum"}
def c63(t): return [ING63[t] if x.startswith("Been ") else x for x in V(1, 63, t)["c"]]
# B 검토 의견(뒷문장만 화살표로 제시해 오해의 소지, 원문항도 같음) 반영: 두 문장을 (1)·(2)로 각각 제시
def p63(t):
    a_, b_ = V(1, 63, t)["passage"].split(" / → ")
    return f"(1) {a_}\n(2) {b_}"
for t in "BCDEF":
    lead = ("검토 의견(뒷문장만 화살표로 제시해 바꾼 결과처럼 보여 오해의 소지가 있음)에 따라, 두 문장을 화살표 없이 (1)·(2)로 각각 제시했다. 원문항도 같은 방식이라 원문항과는 표기가 다르다. " if t == "B"
            else "B 검토 의견(뒷문장만 화살표로 제시해 오해의 소지가 있음)이 이 유형에도 해당해, 두 문장을 화살표 없이 (1)·(2)로 각각 제시했다. ")
    F(1, 63, t, st="R", p=p63(t), c=c63(t), r=R63, n=[g63(x, "") for x in c63(t)],
      s=lead + "또 발문이 ‘완료 수동 분사구문으로 나타낼 때’라고 정답 형태를 알려 주어 원문항 발문으로 되돌리고, 해설을 두 문장의 시간 관계 근거로 고쳤다. 영어에 없는 형태인 오답 ‘Been …’은 원문항처럼 현재분사(-ing) 오답으로 바꿨다.")

# 1-64 분사구문 → 부사절: 상황 설명 삭제, 문장 자체로 뜻이 분명하게, 정답을 원문항과 다른 유형으로
R64 = "분사구문을 부사절로 바꿀 때는 문맥에 맞는 접속사(because, after, while, if 등)와 주어·동사를 되살린다. 이유를 나타내는 분사구문을 although(양보)로 바꾸면 뜻이 달라진다."
S64 = "원문항에 없던 ‘상황’ 설명이 정답 번호의 뜻을 직접 알려 주었고, 선택지 문장이 유형마다 반복되었다. 상황 설명을 지우고 발문을 원문항과 같게 한 뒤, 문장 자체로 관계가 분명한 새 문장 다섯 개로 바꿨다."
def f64(t, items, a, extra=""):
    F(1, 64, t, st="R", p="", c=[x[0] for x in items], a=a, r=R64, n=[(x[1] if i + 1 != a else x[1] + " 정답이다.") for i, x in enumerate(items)], s=S64 + extra)
f64("B", [("<u>Having eaten too much</u>, Minho felt sick. → After Minho had eaten too much, he felt sick.", "먼저 한 일(과식)과 뒤의 일을 after로 바르게 바꿨다."),
          ("<u>Hearing the news</u>, Sora burst into tears. → When Sora heard the news, she burst into tears.", "소식을 들은 때를 when으로 바르게 바꿨다."),
          ("<u>Being short of money</u>, Jiho couldn't buy the shoes. → Although Jiho was short of money, he couldn't buy the shoes.", "돈이 부족한 것은 신발을 못 산 이유인데 양보의 although로 바꿔 뜻이 달라졌다."),
          ("<u>Turning left</u>, you will see the bank. → If you turn left, you will see the bank.", "조건을 if로 바르게 바꿨다."),
          ("<u>Sitting by the window</u>, she watched the rain. → While she was sitting by the window, she watched the rain.", "동시에 일어난 일을 while로 바르게 바꿨다.")], 3, " 정답 위치 ③.")
f64("C", [("<u>Not knowing what to say</u>, Tom kept silent. → Though Tom knew what to say, he kept silent.", "‘몰라서’ 조용히 있었다는 뜻인데 부정(not)을 빼고 양보의 though로 바꿔 뜻이 달라졌다."),
          ("<u>Arriving at the airport</u>, we checked in. → When we arrived at the airport, we checked in.", "도착한 때를 when으로 바르게 바꿨다."),
          ("<u>Having read the book before</u>, Mina knew the ending. → Because Mina had read the book before, she knew the ending.", "먼저 읽은 일이 결말을 안 이유이므로 because로 바르게 바꿨다."),
          ("<u>Listening to music</u>, Leo did his homework. → While Leo was listening to music, he did his homework.", "동시에 한 일을 while로 바르게 바꿨다."),
          ("<u>Pressing this button</u>, you can open the door. → If you press this button, you can open the door.", "조건을 if로 바르게 바꿨다.")], 1,
    " 정답(Being a nurse → Although)이 원문항 정답과 같아 ‘부정어를 빠뜨리고 양보로 바꾼’ 다른 유형의 잘못된 전환으로 만들었다. 정답 위치 ①.")
f64("D", [("<u>Finishing his homework</u>, Jun went out to play. → After Jun finished his homework, he went out to play.", "숙제를 끝낸 뒤의 일을 after로 바르게 바꿨다."),
          ("<u>Being very hungry</u>, the kids ate everything. → Because the kids were very hungry, they ate everything.", "배고픈 것이 다 먹은 이유이므로 because로 바르게 바꿨다."),
          ("<u>Opening the box</u>, Sara found a letter. → When Sara opened the box, she found a letter.", "상자를 연 때를 when으로 바르게 바꿨다."),
          ("<u>Walking along the river</u>, we talked about our plans. → Because we walked along the river, we talked about our plans.", "강을 따라 걸으며(동시 동작) 이야기했다는 뜻인데 because로 바꿔 이유 관계가 되었다."),
          ("<u>Taking this medicine</u>, you will feel better. → If you take this medicine, you will feel better.", "조건을 if로 바르게 바꿨다.")], 4, " 정답 위치 ④.")
f64("E", [("<u>Seeing the police</u>, the thief ran away. → When the thief saw the police, he ran away.", "경찰을 본 때를 when으로 바르게 바꿨다."),
          ("<u>Living near the school</u>, Yuna walks to class. → Because Yuna lives near the school, she walks to class.", "가까이 사는 것이 걸어가는 이유이므로 because로 바르게 바꿨다."),
          ("<u>Having lost his map</u>, the traveler asked for help. → Since the traveler had lost his map, he asked for help.", "지도를 잃어버린 일이 도움을 청한 이유이므로 since로 바르게 바꿨다."),
          ("<u>Smiling brightly</u>, the girl waved to us. → While the girl was smiling brightly, she waved to us.", "동시에 한 동작을 while로 바르게 바꿨다."),
          ("<u>Studying harder</u>, you will pass the test. → Although you study harder, you will pass the test.", "‘더 열심히 하면’이라는 조건인데 양보의 although로 바꿔 뜻이 달라졌다.")], 5, " 정답 위치 ⑤.")
f64("F", [("<u>Having saved enough money</u>, Dan bought a bike. → After Dan had saved enough money, he bought a bike.", "돈을 모은 뒤의 일을 after로 바르게 바꿨다."),
          ("<u>Knowing the answer</u>, Eunji raised her hand. → Before Eunji knew the answer, she raised her hand.", "답을 알아서 손을 들었다는 뜻인데 before로 바꿔 시간 순서가 거꾸로 되었다."),
          ("<u>Feeling cold</u>, he closed the window. → Because he felt cold, he closed the window.", "추운 것이 창문을 닫은 이유이므로 because로 바르게 바꿨다."),
          ("<u>Crossing the street</u>, be careful of cars. → When you cross the street, be careful of cars.", "길을 건널 때를 when으로 바르게 바꿨다."),
          ("<u>Left alone</u>, the baby started to cry. → When the baby was left alone, she started to cry.", "혼자 남겨졌을 때를 when과 수동으로 바르게 바꿨다.")], 2, " 정답 위치 ②.")

# 1-65 옳은 문장 개수: 오류 위치·개수를 원문항과 다르게, 괄호 삭제, 선택지 정렬
R65 = "분사구문의 의미상 주어가 주절의 주어와 같은지, 능동·수동 관계와 먼저 일어난 일(having + 과거분사)을 확인한다. with + 목적어 뒤에는 목적어가 한 동작이면 현재분사, 받은 상태면 과거분사를 쓴다."
CNT = ["2개", "3개", "4개", "5개", "6개"]
def f65(t, lines, judge, ok_n, s, **kw):
    a = CNT.index(f"{ok_n}개") + 1
    F(1, 65, t, st="R", p="\n".join(lines), c=CNT, a=a, r=R65, pre=["문장별 판정:"] + judge, k=f"문법적으로 옳은 문장은 {ok_n}개이다.", n="cnt", s=s, **kw)
f65("B", ["a) Not having enough money, Leo stayed home.", "b) Having selected for the team, Mina celebrated.", "c) I heard the baby crying.", "d) With the door locked, we felt safe.",
          "e) All things considered, the plan is reasonable.", "f) Driving to work, the traffic jam annoyed me."],
    ["a) 옳음: 부정 분사구문 Not having이 주어 Leo와 맞다.", "b) 틀림: Mina가 뽑힌 것이므로 Having been selected가 되어야 한다.", "c) 옳음: 지각동사 heard + 목적어 + 현재분사이다.",
     "d) 옳음: 문이 잠긴 상태이므로 with + 목적어 + 과거분사이다.", "e) 옳음: All things considered는 관용 독립분사구문이다.", "f) 틀림: 운전한 사람은 ‘나’인데 주절 주어가 the traffic jam이다. I was annoyed by the traffic jam으로 고쳐야 한다."],
    4, "오류 위치(d, f)·유형·개수가 원문항과 같고 발문 괄호가 d의 뜻을 알려 주었다. 괄호를 지우고 d를 옳은 문장으로 바꾼 대신 b를 완료 수동 오류로 만들어 오류 위치를 b, f로 옮겼다. 선택지를 2개~6개 순으로 정렬하고 줄을 나눴다.")
f65("C", ["a) Not knowing the way, the tourists asked a police officer.", "b) Having been painted yesterday, the wall is still wet.", "c) Tired from the long trip, my sister fell asleep on the sofa.",
          "d) With her eyes shining, the girl opened the gift.", "e) Leaving the house, I forgot to lock the door.", "f) Surprising at the news, Tom dropped his cup."],
    ["a) 옳음: 부정 분사구문 Not knowing이 주어 the tourists와 맞다.", "b) 옳음: 벽이 칠해진 것이 먼저이므로 Having been painted이다.", "c) 옳음: 누나가 피곤한 상태이므로 과거분사 Tired이다.",
     "d) 옳음: 눈이 스스로 반짝이므로 with + 목적어 + 현재분사이다.", "e) 옳음: 집을 나선 사람과 주절 주어 I가 같다.", "f) 틀림: Tom이 놀란 것이므로 Surprised at the news가 되어야 한다."],
    5, "여섯 문장이 원문항과 거의 같은 구조이고 오류 위치·개수도 같았다. 문장을 모두 새로 쓰고(오류는 f 하나, 옳은 문장 5개), 발문 괄호를 지웠다. 선택지를 2개~6개 순으로 정렬하고 줄을 나눴다.")
F(1, 65, "D", p="BR", op="sortc", s="개수 선택지를 2개~6개 순으로 정렬(정답 ④→④, 5개)했다. 한 줄로 이어 쓴 a)~f)를 한 줄에 한 문장씩 나눴다.")
f65("E", ["a) Feeling sick, Tom rested at home.", "b) Having lost her key, Jane called a locksmith.", "c) We saw the children played in the park.", "d) With the task completed, everyone relaxed.",
          "e) Weather permit, we will hike tomorrow.", "f) Walking to school, a rainbow appeared in the sky."],
    ["a) 옳음: 아픈 사람이 주절 주어 Tom과 같다.", "b) 옳음: 열쇠를 잃어버린 일이 먼저이므로 Having lost이다.", "c) 틀림: 아이들이 스스로 노는 모습이므로 지각동사 뒤에 playing(또는 play)을 쓴다.",
     "d) 옳음: 일이 끝난 상태이므로 with + 목적어 + 과거분사이다.", "e) 틀림: 독립분사구문이므로 Weather permitting으로 써야 한다.", "f) 틀림: 학교에 걸어간 사람과 주절 주어 a rainbow가 다르다. I saw a rainbow in the sky로 고쳐야 한다."],
    3, "여섯 문장이 모두 옳아 원문항(오류 판별)과 인지 과정이 달랐다. c를 지각동사 목적격 보어 오류, e를 독립분사구문 형태 오류, f를 현수분사 오류로 바꿔 틀린 문장을 넣고, 선택지를 2개~6개 순으로 정렬했다.")
F(1, 65, "F", p="BR", keepx=True, s="한 줄로 이어 쓴 a)~f)를 원문항처럼 한 줄에 한 문장씩 나눴다.")

# 1-66 분사구문으로 바꾸기: 발문 조건 삭제, 물음표·없는 형태 오답을 의미·형태 오류로
R66 = "부사절을 분사구문으로 바꿀 때는 접속사와 같은 주어를 빼고 동사를 분사로 바꾼다. 능동이면 -ing, 수동이면 과거분사, 먼저 일어난 일이면 Having + 과거분사를 쓰고, 뒤에 and를 붙이지 않는다."
S66 = "발문에 ‘평서문으로’ 조건을 붙이고 정답 끝에 물음표만 단 오답과 존재하지 않는 형태(Haved, Feeled, knowed) 오답이 있어 형식만으로 지워졌다. 발문을 원문항과 같게 하고, 오답을 원문항처럼 의미·형태 오류로 새로 만들었다."
def f66(t, c, a, notes):
    F(1, 66, t, st="R", c=c, a=a, r=R66, n=[(notes[i] + (" 정답이다." if i + 1 == a else " 오답이다.")) for i in range(5)], s=S66 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f66("B", ["Having finished the task, we left the office.", "Being finished the task, we left the office.", "Finished the task, we left the office.", "Because having finished the task, we left the office.", "Having finishing the task, we left the office."], 1,
    ["먼저 끝낸 일을 Having + 과거분사로 바르게 나타냈다.", "Being + 과거분사는 수동이라 우리가 끝낸 뜻이 아니고 목적어도 올 수 없다.", "과거분사만 쓰면 수동의 뜻이 되어 우리가 과제를 끝낸 뜻이 아니다.",
     "분사구문에서는 접속사 because를 남기지 않는다.", "Having 뒤에는 과거분사가 와야 한다. finishing은 틀린 형태이다."])
f66("C", ["Being felt exhausted, Mina went to bed early.", "Felt exhausted, Mina went to bed early.", "Feeling exhaustion, Mina went to bed early.", "Feeling exhausted, Mina went to bed early.", "Because feeling exhausted, Mina went to bed early."], 4,
    ["Mina가 스스로 느낀 것이므로 수동 Being felt는 맞지 않는다.", "과거형 felt만 쓰면 분사구문이 아니다. 능동이므로 Feeling을 쓴다.", "feel 뒤에는 상태를 나타내는 형용사(exhausted)가 온다. 명사 exhaustion은 뜻이 달라진다.",
     "능동 현재분사 Feeling으로 이유를 나타낸 분사구문이 바르다.", "분사구문에서는 접속사 because를 남기지 않는다."])
f66("D", ["Knowing not the answer, Tom stayed silent.", "Not knowing the answer, Tom stayed silent.", "Not known the answer, Tom stayed silent.", "Not being knowing the answer, Tom stayed silent.", "Not having know the answer, Tom stayed silent."], 2,
    ["부정어 not은 분사 앞에 둔다.", "not을 분사 앞에 두고 능동 knowing을 쓴 분사구문이 바르다.", "known은 수동이라 Tom이 답을 몰랐다는 뜻이 아니다.",
     "being knowing은 겹친 틀린 형태이다.", "having 뒤에는 과거분사가 와야 하고, 이미 모른 상태가 같은 때의 일이므로 단순형이 알맞다."])
F(1, 66, "E", st="R", s="발문에 불필요하게 붙은 ‘평서문으로’ 조건을 지워 원문항 발문으로 되돌렸다. 오답은 적절해 그대로 쓴다.")
f66("F", ["Being worried, Leo checked the message again.", "Worry, Leo checked the message again.", "To be worried, Leo checked the message again.", "Worried being, Leo checked the message again.", "Because being worried, Leo checked the message again."], 1,
    ["was worried를 분사구문으로 바꾸면 Being worried(Being 생략 가능)가 되어 바르다.", "동사원형 Worry로는 분사구문을 만들 수 없다.", "To be worried는 to부정사라 이유를 나타내는 분사구문이 아니다.",
     "어순이 뒤바뀐 틀린 형태이다.", "분사구문에서는 접속사 because를 남기지 않는다."])

# 1-67 분사 관용 표현: 정답을 유형마다 다른 분사 관용 표현으로, 우리말 뜻 제시
R67 = "분사 관용 표현: Frankly speaking(솔직히 말하면), Strictly speaking(엄밀히 말하면), Generally speaking(일반적으로 말하면), Judging from(~로 판단하건대), Considering(~을 고려하면), Speaking of(~ 이야기가 나와서 말인데)."
MEAN67 = {"frankly speaking": "솔직히 말하면", "strictly speaking": "엄밀히 말하면", "generally speaking": "일반적으로 말하면", "judging from": "~로 판단하건대", "considering": "~을 고려하면",
          "speaking of": "~ 이야기가 나와서 말인데", "to make matters worse": "설상가상으로", "needless to say": "말할 필요도 없이", "to be brief": "간단히 말하면"}
def f67(t, dia, c, a, s, st=True):
    n = [(f"{x}: ‘{MEAN67[x.lower()]}’의 뜻으로 빈칸의 우리말 뜻과 흐름에 맞는다. 정답이다." if i + 1 == a else f"{x}: ‘{MEAN67[x.lower()]}’의 뜻이라 빈칸의 뜻과 맞지 않는다.") for i, x in enumerate(c)]
    F(1, 67, t, p=dia, c=c, a=a, r=R67, n=n, s=s, okdup=True, **({"st": "R"} if st else {}))
f67("B", "A: Is it usually cold here in March?\nB: __________(일반적으로 말하면), it gets warm by the end of March.",
    ["Frankly speaking", "Generally speaking", "Judging from", "Speaking of", "Strictly speaking"], 2,
    "정답 To be brief는 독립부정사라 원문항이 묻는 분사 관용 표현이 아니었고, 우리말 뜻 제시도 빠졌다. 정답을 분사 관용 표현 Generally speaking으로 바꾸고 원문항처럼 빈칸 옆에 우리말 뜻을 넣었다.")
f67("C", "A: Did you hear that the concert was canceled?\nB: Yes. __________(~ 이야기가 나와서 말인데) concerts, are you going to the festival next week?",
    ["Frankly speaking", "Strictly speaking", "Speaking of", "Judging from", "Generally speaking"], 3,
    "정답 Frankly speaking이 원문항 정답과 같아서 Speaking of로 바꾸고 대화도 그에 맞게 새로 썼다. 원문항처럼 빈칸 옆에 우리말 뜻을 넣었다.")
F(1, 67, "D", p="A: Is that explanation scientifically exact?\nB: __________(엄밀히 말하면), the term is not completely accurate.", keepx=True, okdup=True,
  s="원문항처럼 빈칸 옆에 우리말 뜻 ‘(엄밀히 말하면)’을 넣었다. 두 줄로 나눴다.")
F(1, 67, "E", p="A: Do you think the project will succeed?\nB: __________(~로 판단하건대) the current results, it looks promising.", keepx=True, okdup=True,
  s="원문항처럼 빈칸 옆에 우리말 뜻 ‘(~로 판단하건대)’를 넣었다. 두 줄로 나눴다.")
F(1, 67, "F", p="A: Why did you choose the train?\nB: __________(~을 고려하면) the heavy traffic, it seemed safer.", keepx=True, okdup=True,
  s="원문항처럼 빈칸 옆에 우리말 뜻 ‘(~을 고려하면)’을 넣었다. 두 줄로 나눴다.")

# 1-68 get + 목적어 + 과거분사 / have + 사람 + 동사원형: 오답을 정답 동사의 다른 형태로
R68 = "get + 사물 목적어 + 과거분사는 그 사물이 어떤 처리를 받게 한다는 뜻이고, have + 사람 목적어 + 동사원형은 그 사람에게 어떤 일을 하게 한다는 뜻이다."
NEED68 = ["(A)는 사물이 처리를 받는 것이므로 get + 목적어 + 과거분사를 쓴다.", "(B)는 사람에게 일을 시키는 것이므로 have + 사람 + 동사원형을 쓴다."]
UA, UB = "(<u>      A      </u>)", "(<u>      B      </u>)"
def f68(t, dia, c, a, s):
    F(1, 68, t, p=dia, c=c, a=a, r=R68, n=tnotes(c, a, NEED68, labs=["(A)", "(B)"]), s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
S68 = "오답 네 개가 C 문항의 동사 repair/replace를 그대로 써서 대화에 맞는 보기는 정답뿐이었다. 오답을 정답 동사의 다른 형태로 바꾸고, 원문항처럼 밑줄 빈칸과 줄바꿈을 넣었다."
f68("B", f"A: Why are you at the salon?\nB: I want to get my hair {UA}. I will have the stylist {UB} it shorter.",
    ["(A) cutting - (B) make", "(A) cut - (B) make", "(A) to cut - (B) to make", "(A) cut - (B) made", "(A) cutting - (B) making"], 2, S68)
F(1, 68, "C", p=f"A: Why are you at the repair shop?\nB: I need to get my laptop {UA}. Then I will have the technician {UB} the battery.", keepx=True,
  s="원문항처럼 빈칸 (A)(B)에 밑줄을 넣고 대화를 두 줄로 나눴다.")
f68("D", f"A: Why are you at the tailor?\nB: I need to get this jacket {UA}. I will have the tailor {UB} the sleeves.",
    ["(A) shortening - (B) adjust", "(A) shortened - (B) adjusted", "(A) to shorten - (B) to adjust", "(A) shortened - (B) adjust", "(A) shorten - (B) adjusting"], 4, S68)
f68("E", f"A: Why are you at the garage?\nB: I need to get the brakes {UA}. I will have the mechanic {UB} the tires too.",
    ["(A) checked - (B) inspect", "(A) check - (B) inspected", "(A) checking - (B) to inspect", "(A) to check - (B) inspecting", "(A) checked - (B) inspected"], 1, S68)
f68("F", f"A: Why are you at the flower shop?\nB: I want to get these roses {UA}. I will have the florist {UB} them to my mom.",
    ["(A) wrapping - (B) deliver", "(A) wrapped - (B) delivered", "(A) wrap - (B) deliver", "(A) to wrap - (B) to deliver", "(A) wrapped - (B) deliver"], 5,
    "정답 짝 cleaned - finish가 원문항과 같았고 오답도 C 문항 동사를 그대로 썼다. 상황을 꽃집으로 바꿔 wrapped - deliver를 정답으로 하고, 오답을 같은 동사의 다른 형태로 만들었다. 밑줄 빈칸과 줄바꿈을 넣었다.")

# 1-69 분사구문 전환 과정 설명: 원문항처럼 제시문을 바꾸는 과정을 단계별로 설명하는 선택지로
R69 = "부사절을 분사구문으로 바꿀 때: 접속사를 생략하고, 두 절의 주어가 다르면 의미상 주어를 남기며, 동사를 분사로 바꾼다(주절과 같은 때이면 being, 먼저이면 having + 과거분사). 부정어는 분사 앞에 둔다."
S69 = "오답 네 개가 B와 똑같았고, 선택지가 제시문과 무관한 일반 규칙이었다. 원문항처럼 제시문을 분사구문으로 바꾸는 과정을 단계별로 설명하는 선택지로 새로 썼다."
def f69(t, c, a, notes):
    F(1, 69, t, c=c, a=a, r=R69, n=[(notes[i] + (" 옳지 않은 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.")) for i in range(5)], s=S69 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f69("C", ["접속사 Since를 생략한다.", "부사절의 주어 no seats와 주절의 주어 we가 다르므로 no seats를 남긴다.", "were는 주절(stood)과 같은 때이므로 being으로 바꾼다.",
          "완성된 분사구문은 No seats being available, we stood at the back.이다.", "주어가 복수(seats)이므로 being 대신 been을 쓴다."], 5,
    ["분사구문에서는 접속사를 생략한다.", "두 절의 주어가 다르면 의미상 주어를 남긴다.", "주절과 같은 때이므로 단순분사 being을 쓴다.", "과정을 거친 결과로 바르다.",
     "분사는 주어의 수와 관계없이 being이다. been은 과거분사라 분사구문의 시작이 될 수 없다."])
f69("D", ["접속사 Since를 생략한다.", "no buses와 Mina는 주어가 다르므로 no buses를 남긴다.", "were running은 주절과 같은 때이므로 being running으로 바꾼다.",
          "진행형 were running은 분사구문에서 running만 남긴다.", "완성된 분사구문은 No buses running, Mina called a taxi.이다."], 3,
    ["분사구문에서는 접속사를 생략한다.", "두 절의 주어가 다르면 의미상 주어를 남긴다.", "진행형의 be동사를 being으로 바꾸면 being running이 되는데, 이 겹친 형태는 쓰지 않고 running만 남긴다.",
     "진행형 분사구문에서는 being을 생략하고 -ing만 남긴다.", "과정을 거친 결과로 바르다."])
f69("E", ["접속사 Since를 생략한다.", "no one과 Tom은 주어가 다르므로 no one을 남긴다.", "주어가 다르므로 no one을 빼고 Answering the phone, Tom sent an email.로 쓴다.",
          "was answering은 answering만 남긴다.", "완성된 분사구문은 No one answering the phone, Tom sent an email.이다."], 3,
    ["분사구문에서는 접속사를 생략한다.", "두 절의 주어가 다르면 의미상 주어를 남긴다.", "주어가 다르면 의미상 주어를 남겨야 한다. 빼면 Tom이 전화를 받는 뜻이 된다.",
     "진행형 분사구문에서는 -ing만 남긴다.", "과정을 거친 결과로 바르다."])
f69("F", ["접속사 Since를 생략한다.", "no lights와 Jane은 주어가 다르므로 no lights를 남긴다.", "were는 주절(assumed)과 같은 때이므로 being으로 바꾼다.",
          "완성된 분사구문은 No lights being on, Jane assumed nobody was home.이다.", "빛이 켜지기 전의 일이므로 having been으로 바꿔야 한다."], 5,
    ["분사구문에서는 접속사를 생략한다.", "두 절의 주어가 다르면 의미상 주어를 남긴다.", "주절과 같은 때이므로 단순분사 being을 쓴다.", "과정을 거친 결과로 바르다.",
     "불이 꺼져 있던 것과 짐작한 것은 같은 때의 일이다. 먼저 일어난 일이 아니므로 having been을 쓰지 않는다."])

# 1-70 독립분사구문 조건: 오답 네 문장을 유형마다 새로
R70 = "독립분사구문은 주절과 다른 의미상 주어를 분사 앞에 밝혀 쓴다. being은 be의 분사, 완료는 having + 과거분사, 완료 수동은 having been + 과거분사이며, 분사구문 뒤에 so·and 같은 접속사를 붙이지 않는다."
S70 = "오답 네 문장이 B와 똑같아서 유형마다 새로 썼다. 원문항처럼 <조건>을 한 줄에 하나씩 나눴다."
P70 = "<조건>\n- 분사구문을 사용할 것\n- 주절의 주어와 다른 경우 주어를 명시할 것"
def f70(t, c, a, notes):
    F(1, 70, t, p=P70, c=c, a=a, r=R70, n=[(notes[i] + (" 두 조건을 모두 만족하므로 정답이다." if i + 1 == a else " 오답이다.")) for i in range(5)], s=S70 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f70("C", ["The sun set, we lit a fire.", "Having been finish the game, the players shook hands.", "The rain stopping, but we stayed inside.", "The weather having improved, we continued the hike.", "Being the store closed, we went home."], 4,
    ["set은 분사가 아니라 동사여서 분사구문이 아니다. The sun having set이 되어야 한다.", "having been 뒤에는 과거분사 finished가 와야 한다.", "분사구문 뒤에 but을 붙였다.",
     "주절과 다른 주어 The weather를 밝히고 먼저 일어난 일을 having improved로 나타냈다.", "의미상 주어는 분사 앞에 와야 한다. The store being closed가 되어야 한다."])
f70("D", ["There being no seats left, we stood.", "Being no seats left, we stood.", "The bus having leave, we took a taxi.", "It raining heavily and we stayed home.", "Having no money left, the trip was canceled."], 1,
    ["주절과 다른 주어 There를 밝힌 독립분사구문이다.", "there를 빼서 의미상 주어가 없어졌다.", "having 뒤에는 과거분사 left가 와야 한다.",
     "분사구문 뒤에 and를 붙였다.", "돈이 없는 사람과 주절 주어 the trip이 달라 주어를 밝혀야 한다."])
f70("E", ["The movie over, having we went out.", "The work having been completed, the team celebrated.", "Completed the work, the team celebrated.", "The lights turning off, so the room became dark.", "School finishing early, having the students gone home."], 2,
    ["having의 위치가 틀렸고 주절 어순도 깨졌다.", "주절과 다른 주어 The work를 밝히고 완료 수동 having been completed를 썼다.", "일을 끝낸 주체와 수동 관계가 맞지 않고 분사 형태도 틀렸다.",
     "분사구문 뒤에 so를 붙였다.", "주절이 have + 주어 + 과거분사 어순으로 깨졌다."])
f70("F", ["Mina being absent, Tom led the meeting.", "Being Mina absent, Tom led the meeting.", "Mina absent being, Tom led the meeting.", "Mina being absent, so Tom led the meeting.", "Because Mina being absent, Tom led the meeting."], 1,
    ["주절과 다른 주어 Mina를 분사 being 앞에 밝혔다.", "의미상 주어는 분사 앞에 와야 한다.", "분사 being이 문장 끝으로 가 어순이 틀렸다.",
     "분사구문 뒤에 접속사 so를 붙였다.", "분사구문에 접속사 because를 남겼다."])


# ---- 2차 감수(2026-10) 추가 ----
# 1-69 B: 보기가 제시문과 무관한 짧은 일반 규칙(C~F에서 고친 것과 같은 문제)
f69("B", ["접속사 Since를 생략한다.", "부사절의 there는 뜻이 없는 말이므로 주절의 주어와 달라도 생략한다.", "was는 주절(skipped)과 같은 때이므로 being으로 바꾼다.", "분사구문으로 바꾼 뒤에도 주절 we skipped lunch는 그대로 둔다.",
          "완성된 분사구문은 There being little time left, we skipped lunch.이다."], 2,
    ["분사구문에서는 접속사를 생략하므로", "there는 부사절의 주어 자리에 있고 주절의 주어 we와 다르므로 남겨야 한다. 그런데 생략한다고 했으므로", "부사절과 주절이 같은 때이면 동사를 being으로 바꾸므로", "분사구문은 부사절만 바꾸고 주절은 그대로 두므로",
     "접속사를 빼고 there를 남긴 채 was를 being으로 바꾼 형태가 맞으므로"])
FIX[(1, 69, "B")]["s"] = "보기가 ‘접속사는 생략할 수 있다’처럼 제시문과 무관한 짧은 일반 규칙이어서 원문항(제시문을 분사구문으로 바꾸는 과정 설명)보다 수준이 낮았다. 원문항처럼 제시문을 바꾸는 과정을 단계별로 설명하는 보기로 새로 썼다. 정답 위치 ②."

# 1-70 B: <조건>을 원문항처럼 한 줄에 하나씩
F(1, 70, "B", p=P70, s="‘/’로 이어 쓴 <조건>을 원문항처럼 한 줄에 하나씩 나눴다. 보기와 정답은 그대로다.")
