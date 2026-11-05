# 5급 CH9 장소·시간 전치사 (81~90) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def talk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 옳지 않은 설명이다. 따라서 정답이다." if i + 1 == a else " 옳은 설명이다. 따라서 오답이다.")) if w.endswith("므로") else (w + (" 옳지 않은 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.")) for i, (_, w) in enumerate(items)], k=items[a-1][1], s=s + ipos(a), **kw)
R_TIME = "시각·정오·밤 앞에는 at, 요일·날짜 앞에는 on, 월·계절·연도·오전/오후/저녁 앞에는 in을 쓴다. 장소는 특정 지점에 at, 표면 위에 on, 안쪽이나 도시·나라에 in을 쓴다."

# 5-81 위치 전치사: D는 원문항처럼 같은 명사에 서로 다른 위치 전치사
F(5, 81, "D", p="공이 상자 뒤에 있다.", c=["The ball is in the box.", "The ball is on the box.", "The ball is behind the box.", "The ball is next to the box.", "The ball is under the box."], a=3,
  r="위치를 나타내는 전치사는 in(~ 안에), on(~ 위에), under(~ 아래에), behind(~ 뒤에), in front of(~ 앞에), next to(~ 옆에), between(~ 사이에)이다.",
  n=["in은 ‘~ 안에’라는 뜻이므로 오답이다.", "on은 ‘~ 위에’라는 뜻이므로 오답이다.", "behind는 ‘~ 뒤에’라는 뜻이라 ‘상자 뒤에’가 되므로 정답이다.", "next to는 ‘~ 옆에’라는 뜻이므로 오답이다.", "under는 ‘~ 아래에’라는 뜻이므로 오답이다."],
  s="선택지가 모두 ‘at + 장소’이고 장소 명사만 달라 전치사가 아니라 어휘를 묻는 문항이 되었다. 원문항처럼 같은 명사(the box)에 서로 다른 위치 전치사를 붙인 선택지로 바꿨다. 정답 위치 ③.")

# 5-82 in의 위치: 원문항처럼 우리말과 문장 속 ①~⑤ 위치 선택형
ST582 = "다음 문장에서 in이 들어갈 위치를 고르시오."
R582 = "in은 도시·나라·건물 안처럼 장소를 나타내는 명사 앞에 와서 ‘~에(서)’라는 뜻을 나타낸다. 전치사는 뒤에 오는 명사와 한 덩어리가 된다."
S582 = "원문항은 우리말을 보고 문장 속에서 in이 들어갈 위치를 고르는 형식인데, 변형은 빈칸에 알맞은 전치사를 고르는 형식으로 바뀌었다. 원문항처럼 문장 속 위치를 고르는 형식으로 되돌리고, 정답 위치가 원문항과 겹치지 않게 문장을 새로 썼다."
def f582(t, ko, words, a, place, s=S582):
    n = []
    for i, w in enumerate(words):
        if i + 1 == a: n.append(f"{w} 앞에 in을 넣으면 ‘{place}’라는 장소 표현이 되므로 정답이다.")
        else: n.append(f"{w} 앞은 in이 장소 명사와 이어지는 자리가 아니므로 오답이다.")
    F(5, 82, t, st=ST582, p=ko, c=words, a=a, r=R582, n=n, okdup=True, s=s + ipos(a))
f582("B", "우리 이모는 부산에서 일한다.", ["My", "aunt", "works", "Busan", "."], 4, "in Busan(부산에서)",
     "위치 번호 대신 ‘바로 뒤에 오게 될 단어’를 고르게 바뀌었다. 원문항처럼 문장 속 위치를 고르는 형식으로 되돌렸다.")
f582("C", "Tom은 지금 대전에 있다.", ["Tom", "is", "Daejeon", "now", "."], 3, "in Daejeon(대전에)", S582 + " 문장의 낱말이 선택지에 모두 나오도록 다섯 칸에 맞는 문장으로 썼다.")
f582("D", "우리 반 학생들은 친절하다.", ["Students", "my", "class", "are", "kind"], 2, "in my class(우리 반의)")
f582("E", "우리 조부모님은 제주에서 행복하게 사신다.", ["My", "grandparents", "live", "happily", "Jeju"], 5, "in Jeju(제주에서)")
f582("F", "그들은 방 안에서 조용히 공부한다.", ["They", "study", "quietly", "the", "room"], 4, "in the room(방 안에서)")

# 5-83 밑줄이 잘못된 것: B 원문항 발문, C~F는 짝 없이 시간·장소를 섞어 새로
F(5, 83, "B", st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
S583 = "정답 문장과 같은 문장의 옳은 전치사가 함께 있어 대비 단서가 되었고 오답 네 개가 C와 똑같았다. 원문항처럼 시간·장소 전치사를 섞어 짝 문장 없이 유형마다 새로 썼다."
IN_ = lambda w: f"{w} 앞에 in을 바르게 썼으므로"; ON_ = lambda w: f"{w} 앞에 on을 바르게 썼으므로"; AT_ = lambda w: f"{w} 앞에 at을 바르게 썼으므로"
def f583(t, items, a, s=S583):
    mk(5, 83, t, items, a, R_TIME, s)
f583("C", [("We go swimming <u>in</u> summer.", IN_("계절")), ("My birthday is <u>in</u> May 5th.", "날짜 앞에는 on을 써야 하므로"), ("He studies <u>at</u> night.", AT_("night")), ("The cat is <u>on</u> the sofa.", ON_("표면 위를 나타내는 the sofa")), ("We have music class <u>on</u> Wednesday.", ON_("요일"))], 2)
f583("D", [("School starts <u>on</u> 9 o'clock.", "시각 앞에는 at을 써야 하므로"), ("I was born <u>in</u> 2014.", IN_("연도")), ("They play tennis <u>on</u> Saturday.", ON_("요일")), ("She lives <u>in</u> Canada.", IN_("나라")), ("We eat lunch <u>at</u> noon.", AT_("noon"))], 1)
f583("E", [("Christmas is <u>in</u> December.", IN_("월")), ("My dad works <u>at</u> a bank.", AT_("일하는 지점인 a bank")), ("The festival is <u>at</u> Friday.", "요일 앞에는 on을 써야 하므로"), ("I read books <u>in</u> the evening.", IN_("the evening")), ("The picture is <u>on</u> the wall.", ON_("벽 표면을 나타내는 the wall"))], 3)
f583("F", [("Leaves fall <u>in</u> autumn.", IN_("계절")), ("We have a test <u>on</u> Thursday.", ON_("요일")), ("The bus leaves <u>at</u> 7:30.", AT_("시각")), ("He was born <u>at</u> 2012.", "연도 앞에는 in을 써야 하므로"), ("Mom is <u>in</u> the kitchen.", IN_("안쪽 공간인 the kitchen"))], 4)

# 5-84 빈칸 대답: B 원문항 발문, C~F는 원문항처럼 같은 주제의 다른 정보 대답
F(5, 84, "B", st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
R584 = "질문의 의문사가 묻는 정보에 맞춰 답한다. What year는 연도, What month는 달, What season은 계절, What day는 요일, What time은 시각, Where는 장소를 묻는다."
S584 = "원문항 오답은 모두 같은 주어·동사로 질문과 다른 정보(계절, 달, 요일, 장소)를 답해 질문 이해를 묻는데, 변형 오답은 다른 질문에 대한 대답이라 바로 지워졌고 유형마다 반복되었다. 원문항처럼 같은 주제의 다른 정보 대답으로 오답을 새로 썼다."
def f584(t, q, items, a, s=S584):
    mk(5, 84, t, items, a, R584, s, p=f"A: {q}\nB: _______________________")
f584("C", "What season were you born in?", [("I was born in April.", "달을 답해 계절을 묻는 질문에 맞지 않으므로"), ("I was born at night.", "하루 중 때를 답해 계절을 묻는 질문에 맞지 않으므로"), ("I was born on Monday.", "요일을 답해 계절을 묻는 질문에 맞지 않으므로"),
     ("I was born in spring.", "계절을 묻는 질문에 계절로 알맞게 답했으므로"), ("I was born in Seoul.", "장소를 답해 계절을 묻는 질문에 맞지 않으므로")], 4, S584 + " 질문도 B(What month)와 겹치지 않게 바꿨다.")
f584("D", "What day do you have English class?", [("I have English in the morning.", "때(오전)를 답해 요일을 묻는 질문에 맞지 않으므로"), ("I have English at 10 o'clock.", "시각을 답해 요일을 묻는 질문에 맞지 않으므로"), ("I have English on Monday.", "요일을 묻는 질문에 요일로 알맞게 답했으므로"),
     ("I have English in Room 3.", "장소를 답해 요일을 묻는 질문에 맞지 않으므로"), ("I have English in March.", "달을 답해 요일을 묻는 질문에 맞지 않으므로")], 3)
f584("E", "What time does school start?", [("It starts on Monday.", "요일을 답해 시각을 묻는 질문에 맞지 않으므로"), ("It starts in March.", "달을 답해 시각을 묻는 질문에 맞지 않으므로"), ("It starts at the main gate.", "장소를 답해 시각을 묻는 질문에 맞지 않으므로"),
     ("It starts in 2025.", "연도를 답해 시각을 묻는 질문에 맞지 않으므로"), ("It starts at 9 o'clock.", "시각을 묻는 질문에 시각으로 알맞게 답했으므로")], 5)
f584("F", "Where do you live?", [("I live with my parents.", "함께 사는 사람을 답해 장소를 묻는 질문에 맞지 않으므로"), ("I live in Ulsan.", "장소를 묻는 질문에 사는 곳으로 알맞게 답했으므로"), ("I moved here in 2019.", "이사 온 해를 답해 장소를 묻는 질문에 맞지 않으므로"),
     ("I live a happy life.", "사는 모습을 답해 장소를 묻는 질문에 맞지 않으므로"), ("I go home at five.", "집에 가는 시각을 답해 장소를 묻는 질문에 맞지 않으므로")], 2)

# 5-85 밑줄이 옳은 문장: B 원문항 발문, C~F는 짝 없이 유형마다 새로
F(5, 85, "B", st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
S585 = "정답 문장과 같은 문장의 틀린 전치사가 함께 있어 대비 단서가 되었고 오답 네 개가 C와 똑같았다. 짝 문장 없이 유형마다 새로 썼다."
def f585(t, items, a, s=S585):
    mk(5, 85, t, items, a, R_TIME, s)
f585("C", [("The party is <u>at</u> Saturday.", "요일 앞에는 on을 써야 하므로"), ("I get up <u>in</u> six.", "시각 앞에는 at을 써야 하므로"), ("We go camping <u>on</u> summer.", "계절 앞에는 in을 써야 하므로"), ("We live <u>in</u> Korea.", IN_("나라")), ("She is <u>in</u> home now.", "‘집에’는 at home으로 써야 하므로")], 4)
f585("D", [("The movie starts <u>on</u> seven.", "시각 앞에는 at을 써야 하므로"), ("I was born <u>at</u> 2013.", "연도 앞에는 in을 써야 하므로"), ("They are <u>at</u> the park.", AT_("특정 장소인 the park")), ("We have a test <u>in</u> Friday.", "요일 앞에는 on을 써야 하므로"), ("It snows a lot <u>on</u> winter.", "계절 앞에는 in을 써야 하므로")], 3)
f585("E", [("He lives <u>at</u> Japan.", "나라 앞에는 in을 써야 하므로"), ("My birthday is <u>on</u> June 10th.", ON_("날짜")), ("Class ends <u>in</u> noon.", "정오 앞에는 at을 써야 하므로"), ("We swim <u>at</u> July.", "월 앞에는 in을 써야 하므로"), ("Tom studies <u>on</u> night.", "‘밤에’는 at night으로 써야 하므로")], 2)
f585("F", [("The store opens <u>on</u> ten.", "시각 앞에는 at을 써야 하므로"), ("I play games <u>in</u> Sunday.", "요일 앞에는 on을 써야 하므로"), ("We met <u>at</u> 2020.", "연도 앞에는 in을 써야 하므로"), ("She is <u>on</u> school.", "‘학교에’는 at school로 써야 하므로"), ("The keys are <u>in</u> my bag.", IN_("안쪽 공간인 my bag"))], 5)

# 5-86 F: 원문항 발문, 원문항처럼 시간 표현 문장
F(5, 86, "F", st="R", p="We have a school trip ________ Friday.", c=["on", "in", "at", "under", "between"], a=1, r=R_TIME,
  n=["요일 Friday 앞에는 on을 쓰므로 정답이다.", "in은 월·계절·연도 앞에 쓰므로 오답이다.", "at은 시각 앞에 쓰므로 오답이다.", "under는 ‘~ 아래에’라는 장소 전치사이므로 오답이다.", "between은 ‘~ 사이에’라는 뜻이므로 오답이다."],
  s="발문에 ‘책은 책상 표면 위에 놓여 있다’는 뜻을 붙여 정답을 알려 주었고, 원문항(시각 전치사)과 달리 장소 전치사를 물었다. 원문항 발문으로 되돌리고 시간 표현 문장으로 바꿨다. 정답 위치 ①.")

# 5-87 밑줄이 옳은 문장: 짝 없이 유형마다 새로
S587 = "정답 문장과 같은 문장의 틀린 전치사가 함께 있어 대비 단서가 되었고 오답 네 개가 C와 똑같았다. 원문항처럼 시간 전치사 문장으로 짝 없이 유형마다 새로 썼다."
def f587(t, items, a, s=S587):
    mk(5, 87, t, items, a, R_TIME, s)
f587("C", [("We go to the beach <u>on</u> July.", "월 앞에는 in을 써야 하므로"), ("I brush my teeth <u>at</u> the evening.", "‘저녁에’는 in the evening으로 써야 하므로"), ("The concert is <u>in</u> Saturday.", "요일 앞에는 on을 써야 하므로"), ("Tom was born <u>on</u> 2016.", "연도 앞에는 in을 써야 하므로"), ("Let's meet <u>at</u> 5 o'clock.", AT_("시각"))], 5)
f587("D", [("We have lunch <u>at</u> 12:30.", AT_("시각")), ("It is cold <u>on</u> January.", "월 앞에는 in을 써야 하므로"), ("I play soccer <u>in</u> Friday.", "요일 앞에는 on을 써야 하므로"), ("The leaves turn red <u>at</u> fall.", "계절 앞에는 in을 써야 하므로"), ("They moved here <u>on</u> 2019.", "연도 앞에는 in을 써야 하므로")], 1)
f587("E", [("My sister visits us <u>in</u> Wednesday.", "요일 앞에는 on을 써야 하므로"), ("Birds come back <u>in</u> spring.", IN_("계절")), ("The class starts <u>on</u> 8:50.", "시각 앞에는 at을 써야 하므로"), ("I was born <u>at</u> March.", "월 앞에는 in을 써야 하므로"), ("We watch TV <u>on</u> the evening.", "‘저녁에’는 in the evening으로 써야 하므로")], 2)
f587("F", [("The game is <u>at</u> Tuesday.", "요일 앞에는 on을 써야 하므로"), ("He came home <u>in</u> midnight.", "‘자정에’는 at midnight으로 써야 하므로"), ("Summer vacation starts <u>in</u> July.", IN_("월")), ("We went to Jeju <u>on</u> 2021.", "연도 앞에는 in을 써야 하므로"), ("I wake up <u>on</u> 7 a.m.", "시각 앞에는 at을 써야 하므로")], 3)

# 5-88 세 번째 단어: 원문항 발문, 필요 없는 단어 하나를 섞고 세 번째 단어가 be동사로 바로 정해지지 않게
ST588 = "주어진 단어들을 바르게 배열할 때, 세 번째에 오는 단어는 무엇입니까?"
R588 = "우리말 뜻에 맞게 주어 + 동사 + (목적어) + 전치사 + 명사의 어순으로 배열한다. There is/are 문장은 There + be동사 + 주어로 시작하고, 명령문은 동사원형으로 시작한다."
S588 = "변형은 단어를 정답 순서대로 주고 발문이 ‘주어로 시작하는 기본 어순의 평서문’이라고 알려 주어 세 번째 단어가 대부분 be동사로 바로 정해졌다. 원문항 발문으로 되돌리고 원문항처럼 단어 순서를 섞었으며, There 구문·명령문 등으로 세 번째 단어가 유형마다 달라지게 했다. 원문항에서 뺀 at처럼 필요 없는 단어는 넣지 않았다."
def f588(t, ko, words, sent, opts, a, notes, s=S588):
    F(5, 88, t, st=ST588, p=f"{ko}\n({' / '.join(words)})", c=opts, a=a, r=R588, k=f"완성 문장은 {sent}이고, 세 번째 단어는 {opts[a-1]}이다.",
      n=[w + (" 정답이다." if i + 1 == a else " 오답이다.") for i, w in enumerate(notes)], okdup=True, s=s + ipos(a))
f588("B", "선반 위에 책들이 있다.", ["on", "There", "books", "the", "are", "shelf"], "There are books on the shelf.", ["on", "There", "books", "are", "shelf"], 3,
     ["on은 네 번째에 오므로", "There는 첫 번째에 오므로", "books는 세 번째에 오므로", "are는 두 번째에 오므로", "shelf는 여섯 번째에 오므로"])
f588("C", "그것은 의자 아래에 있다.", ["is", "the", "under", "It", "chair"], "It is under the chair.", ["is", "the", "It", "under", "chair"], 4,
     ["is는 두 번째에 오므로", "the는 네 번째에 오므로", "It은 첫 번째에 오므로", "under는 세 번째에 오므로", "chair는 다섯 번째에 오므로"])
f588("D", "네 가방을 문 옆에 두어라.", ["next", "your", "Put", "door", "to", "bag", "the"], "Put your bag next to the door.", ["your", "next", "to", "the", "bag"], 5,
     ["your는 두 번째에 오므로", "next는 네 번째에 오므로", "to는 다섯 번째에 오므로", "the는 여섯 번째에 오므로", "명령문은 동사 Put으로 시작해 bag이 세 번째에 오므로"])
f588("E", "Jane은 나무 아래에 앉아 있다.", ["sitting", "under", "Jane", "the", "is", "tree"], "Jane is sitting under the tree.", ["under", "sitting", "is", "tree", "Jane"], 2,
     ["under는 네 번째에 오므로", "sitting은 세 번째에 오므로", "is는 두 번째에 오므로", "tree는 여섯 번째에 오므로", "Jane은 첫 번째에 오므로"])
f588("F", "상자 안에 연필이 한 자루 있다.", ["a", "is", "in", "There", "box", "pencil", "the"], "There is a pencil in the box.", ["a", "is", "pencil", "in", "box"], 1,
     ["There is 뒤에 오는 a가 세 번째에 오므로", "is는 두 번째에 오므로", "pencil은 네 번째에 오므로", "in은 다섯 번째에 오므로", "box는 일곱 번째에 오므로"])

# 5-89 (A)(B) 전치사 짝: 정답 조합을 원문항(on - at)과 다르게
S589 = "정답 조합(on - at)이 원문항과 같았다. 문장을 바꿔 정답 조합이 원문항과 다르게 했다."
def f589(t, p, items, a, s=S589, **kw):
    mk(5, 89, t, items, a, R_TIME, s, p=p, okdup=True, **kw)
f589("B", "The school fair starts (A)_______ Saturday morning and ends (B)_______ the afternoon.",
     [("(A) on - (B) on", "(B): ‘오후에’는 in the afternoon으로 쓰므로"), ("(A) at - (B) in", "(A): 특정 요일의 아침(Saturday morning) 앞에는 on을 쓰므로"), ("(A) on - (B) in", "특정 요일의 아침 앞에 on, the afternoon 앞에 in을 바르게 짝지었으므로"),
      ("(A) on - (B) at", "(B): ‘오후에’는 in the afternoon으로 쓰므로"), ("(A) in - (B) at", "(A): 특정 요일의 아침 앞에는 on을, (B): the afternoon 앞에는 in을 쓰므로")], 3,
     "정답 조합(on - at)이 원문항과 같았고 발문에 ‘시간 전치사’가 붙었다. 원문항 발문으로 되돌리고, 문장을 바꿔 정답 조합이 원문항과 다르게 했다.", st="R")
f589("C", "We meet (A)_______ 3 p.m. (B)_______ Monday.",
     [("(A) on - (B) at", "(A): 시각 앞에는 at을, (B): 요일 앞에는 on을 쓰므로"), ("(A) at - (B) on", "시각 앞에 at, 요일 앞에 on을 바르게 짝지었으므로"), ("(A) at - (B) in", "(B): 요일 앞에는 on을 쓰므로"),
      ("(A) in - (B) on", "(A): 시각 앞에는 at을 쓰므로"), ("(A) in - (B) at", "(A): 시각 앞에는 at을, (B): 요일 앞에는 on을 쓰므로")], 2)
f589("E", "We have dinner (A)_______ 7 o'clock (B)_______ the evening.",
     [("(A) at - (B) in", "시각 앞에 at, the evening 앞에 in을 바르게 짝지었으므로"), ("(A) in - (B) at", "(A): 시각 앞에는 at을, (B): the evening 앞에는 in을 쓰므로"), ("(A) at - (B) on", "(B): ‘저녁에’는 in the evening으로 쓰므로"),
      ("(A) on - (B) in", "(A): 시각 앞에는 at을 쓰므로"), ("(A) in - (B) in", "(A): 시각 앞에는 at을 쓰므로")], 1)

# 5-90 <보기> 문장의 at에 대한 설명: 원문항 발문, <보기> 문장의 at에 대한 설명으로 유형마다 새로
R590 = "at은 장소를 하나의 지점으로 볼 때 쓰고(at the door, at the station, at home), 안쪽 공간을 강조하면 in, 표면 위를 나타내면 on을 쓴다. at은 시각 앞에도 쓴다."
S590 = "발문이 ‘시간과 장소를 나타내는 전치사의 쓰임에 대한 설명’으로 넓어져 <보기>와 관계없는 일반 규칙이 선택지 대부분을 차지했고, 설명이 유형마다 반복되었다. 원문항 발문으로 되돌리고 <보기> 문장의 at에 대한 설명으로 유형마다 새로 썼다."
ST590 = "다음 <보기>의 문장에서 쓰인 전치사 'at'의 성격에 대한 설명으로 틀린 것을 고르시오."
def f590(t, sent, items, a, s=S590):
    talk(5, 90, t, items, a, R590, s, st=ST590, p=f"<보기>\n{sent}")
f590("C", "We had lunch <u>at</u> the restaurant.",
     [("'at'은 식당이라는 특정한 장소를 하나의 지점으로 나타낸다.", "at은 장소를 하나의 지점으로 나타내므로"), ("'at'은 시각 앞에만 쓰이므로 이 문장의 'at'은 시간을 나타낸다.", "at은 장소 앞에도 쓰며, 이 문장의 at은 식당이라는 장소를 나타내므로"),
      ("식당 '안'에서 먹었다는 점을 강조하려면 'in the restaurant'로 쓸 수도 있다.", "안쪽 공간을 강조하면 in을 쓰므로"), ("'at the restaurant'는 어디에서 점심을 먹었는지 알려 주는 장소 표현이다.", "at the restaurant가 점심을 먹은 장소를 나타내므로"),
      ("'at' 대신 'on'을 쓰면 식당 건물 '위에서' 먹었다는 뜻이 된다.", "on은 표면 위를 나타내므로")], 2)
f590("D", "She is <u>at</u> home.",
     [("'at home'은 '집에'라는 뜻으로 자주 쓰는 표현이다.", "at home은 ‘집에’라는 뜻의 굳어진 표현이므로"), ("'at' 대신 'in'을 써서 'in home'이라고 하는 것은 어색하다.", "‘집에’는 in home이 아니라 at home으로 쓰므로"),
      ("'at home'에서는 home 앞에 the를 꼭 넣어 'at the home'으로 써야 한다.", "‘집에’는 the 없이 at home으로 쓰므로"), ("'She is at home.'은 그녀가 지금 있는 장소를 나타낸다.", "at home이 그녀가 있는 장소를 나타내므로"),
      ("이 문장의 'at'은 시간이 아니라 장소를 나타내는 전치사이다.", "at 뒤에 장소 home이 왔으므로")], 3)
f590("E", "We meet <u>at</u> the door.",
     [("'at the door'는 문이라는 특정 지점, 즉 문 앞이나 문가를 나타낸다.", "at은 장소를 하나의 지점으로 나타내므로"), ("'at' 대신 'on'을 쓰면 문 표면에 붙어 있다는 뜻이 된다.", "on은 표면에 붙어 있는 것을 나타내므로"),
      ("'at the door'는 만나는 장소를 알려 주는 표현이다.", "at the door가 만나는 장소를 나타내므로"), ("'at'은 '~ 위에'라는 뜻이므로 문 위에 올라가서 만난다는 뜻이다.", "at은 ‘~ 위에’가 아니라 특정 지점을 나타내므로"),
      ("'at'은 장소뿐 아니라 'at seven'처럼 시각 앞에도 쓴다.", "at은 시각 앞에도 쓰므로")], 4)
f590("F", "Tom waits <u>at</u> the station.",
     [("'at'은 station처럼 건물을 나타내는 명사 앞에는 쓸 수 없다.", "at the station, at the bank처럼 건물 명사 앞에도 at을 쓰므로"), ("'at the station'은 역을 넓은 공간이 아니라 기다리는 한 곳으로 보는 표현이다.", "at은 장소를 하나의 지점으로 나타내므로"),
      ("역 건물 안에서 기다린다는 점을 강조하면 'in the station'도 쓸 수 있다.", "안쪽 공간을 강조하면 in을 쓰므로"), ("'at the station'은 동사 waits 뒤에서 기다리는 장소를 알려 준다.", "at the station이 기다리는 장소를 나타내므로"),
      ("'at' 대신 'on'을 쓰면 역 건물 위라는 어색한 뜻이 된다.", "on은 표면 위를 나타내므로")], 1)


# ---- 2차 감수(2026-10) 추가 ----
# 5-89 D: 어색한 문장(in 2015 in May) → 두 문장으로 / F: 어색한 문장(in summer in August), 정답 조합이 D와 같음(in - in)
f589("D", "My sister was born (A)_______ 2015. Her birthday is (B)_______ May.",
     [("(A) at - (B) on", "(A): 연도 앞에는 in을, (B): 달 앞에는 in을 쓰므로"), ("(A) in - (B) on", "(B): 달 앞에는 in을 쓰므로"), ("(A) in - (B) in", "연도 앞에 in, 달 앞에 in을 바르게 짝지었으므로"),
      ("(A) at - (B) in", "(A): 연도 앞에는 in을 쓰므로"), ("(A) on - (B) in", "(A): 연도 앞에는 in을 쓰므로")], 3,
     "‘I was born in 2015 in May.’는 연도와 달을 거꾸로 나열해 어색한 문장이었다(보통 in May 2015). 두 빈칸을 자연스러운 두 문장으로 나누었다. 선택지와 정답은 그대로다.")
f589("F", "I get up late (A)_______ the morning (B)_______ Sundays.",
     [("(A) on - (B) in", "(A): the morning 앞에는 in을, (B): 요일 앞에는 on을 쓰므로"), ("(A) at - (B) in", "(A): the morning 앞에는 in을, (B): 요일 앞에는 on을 쓰므로"), ("(A) at - (B) on", "(A): ‘아침에’는 in the morning으로 쓰므로"),
      ("(A) in - (B) on", "the morning 앞에 in, 요일 앞에 on을 바르게 짝지었으므로"), ("(A) in - (B) in", "(B): 요일 앞에는 on을 쓰므로")], 4,
     "‘We travel in summer in August.’는 뜻이 겹쳐 어색한 문장이었고 정답 조합(in - in)이 D와 같았다. 문장을 바꿔 정답 조합이 다른 유형과 겹치지 않게 했다.")
