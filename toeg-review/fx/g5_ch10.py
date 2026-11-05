# 5급 CH10 접속사 (91~100) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def talk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 옳지 않은 설명이다. 따라서 정답이다." if i + 1 == a else " 옳은 설명이다. 따라서 오답이다.")) if w.endswith("므로") else (w + (" 옳지 않은 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.")) for i, (_, w) in enumerate(items)], k=items[a-1][1], s=s + ipos(a), **kw)
R_CJ = "and는 나열(~와, 그리고), but은 대조(~지만), or는 선택(~ 또는, 아니면)을 나타낸다. when은 ‘~할 때’, before는 ‘~하기 전에’, after는 ‘~한 후에’라는 시간의 접속사로 뒤에 주어 + 동사를 이끈다."

# 5-91 원문항 발문, 우리말은 문장 위에
F(5, 91, "B", st="R", p="나는 경기에 참여하고 싶었지만 발목이 아팠다.\n" + V(5, 91, "B")["passage"], r=R_CJ, n=["‘~지만’이라는 대조를 나타내므로 정답이다.", "‘~할 때’라는 뜻이라 우리말과 맞지 않으므로 오답이다.", "선택을 나타내 ‘~지만’의 뜻이 되지 않으므로 오답이다.", "이유를 나타내 ‘~지만’의 뜻이 되지 않으므로 오답이다.", "나열을 나타내 ‘~지만’의 뜻이 되지 않으므로 오답이다."], s="발문이 ‘대조 관계를 직접 나타내는 등위접속사’라고 정답을 알려 주었다. 원문항 발문으로 되돌리고 우리말 해석은 원문항처럼 문장 위에 두었다. 보기와 정답은 그대로다.")

# 5-92 들어갈 수 없는 말: 제시 문장과 형용사를 유형마다 새로
R592 = "be동사 뒤에서 and로 이어지는 말은 주어를 설명하는 형용사여야 한다. -ly로 끝나는 부사는 이 자리에 올 수 없고, friendly처럼 -ly로 끝나는 형용사는 올 수 있다."
S592 = "제시 문장(It is cute and ____.)이 원문항과 똑같고 옳은 형용사 오답도 원문항·유형마다 같아, 부사 하나만 바뀐 문항이었다. 제시 문장과 형용사 오답을 유형마다 새로 썼다."
ADJ = "형용사라 be동사 뒤에서 and로 이어져 주어를 설명할 수 있으므로"; ADVX = "부사라 be동사 뒤에서 주어를 설명하는 형용사 자리에 올 수 없으므로"
def f592(t, p, items, a, s=S592):
    mk(5, 92, t, [(x, w or ADJ) for x, w in items], a, R592, s, p=p)
f592("C", "The park is big and _______.", [("green", ""), ("quietly", ADVX), ("clean", ""), ("beautiful", ""), ("peaceful", "")], 2)
f592("D", "My grandma is kind and _______.", [("wise", ""), ("gentle", ""), ("funny", ""), ("warmly", ADVX), ("healthy", "")], 4)
f592("E", "This cake is soft and _______.", [("sweet", ""), ("delicious", ""), ("fresh", ""), ("warm", ""), ("nicely", ADVX)], 5)
f592("F", "The new teacher is tall and _______.", [("politely", ADVX), ("friendly", "-ly로 끝나지만 형용사라 be동사 뒤에서 주어를 설명할 수 있으므로"), ("smart", ""), ("strong", ""), ("handsome", "")], 1,
     S592 + " -ly로 끝나는 형용사(friendly)를 오답에 넣어 끝 모양이 아니라 품사로 판단하게 했다.")

# 5-93 두 빈칸 짝: 원문항 발문, 문장 옆 우리말, 정답·오답 조합을 유형마다 새로
S593 = "발문에 우리말 해석과 ‘사건 순서를 그대로’가 붙었고, 정답이나 오답 조합이 원문항·유형마다 반복되었다. 원문항 발문으로 되돌리고 우리말 해석은 원문항처럼 문장 옆에 두었으며, 정답·오답 조합을 유형마다 새로 썼다."
def f593(t, p, good, chs, why, a, s=S593):
    items = []
    for ch in chs:
        xs = [x.strip() for x in ch.split(" - ")]; gs = [x.strip() for x in good.split(" - ")]
        if xs == gs: items.append((ch, "두 빈칸에 우리말 뜻에 맞는 접속사를 모두 바르게 골랐으므로")); continue
        bits = [f"{['첫째', '둘째'][i]} 빈칸 {x}: {why[i]}" for i, (x, g) in enumerate(zip(xs, gs)) if x != g]
        items.append((ch, ". ".join(bits) + ". 따라서"))
    mk(5, 93, t, items, a, R_CJ, s, st="R", p=p, okdup=True)
f593("B", "Tom was tired, ________ he finished the project. (Tom은 피곤했지만 프로젝트를 끝냈다.)\nI washed my face ________ I went to bed. (나는 잠자리에 들기 전에 세수를 했다.)", "but - before",
     ["but - before", "and - after", "but - after", "or - before", "so - when"], ["‘피곤했지만’은 대조이므로 but을 쓴다", "‘잠자리에 들기 전에’이므로 before를 쓴다"], 1,
     "정답 조합(but - when)이 원문항과 같았고 발문에 우리말과 ‘사건 순서를 그대로’가 붙었다. 원문항 발문으로 되돌리고, 둘째 문장을 바꿔 정답 조합이 but - before가 되게 했다.")
f593("C", "Do you want to walk _______ take a bus? (걸어갈래, 아니면 버스를 탈래?)\nI wash my hands _______ I eat. (나는 먹기 전에 손을 씻는다.)", "or - before",
     ["and - after", "but - before", "or - before", "or - when", "and - before"], ["‘아니면’은 선택이므로 or를 쓴다", "‘먹기 전에’이므로 before를 쓴다"], 3)
f593("D", "Tom ate dinner _______ he watched TV. (Tom은 TV를 보기 전에 저녁을 먹었다.)\nHe is young _______ very smart. (그는 어리지만 매우 영리하다.)", "before - but",
     ["after - but", "before - but", "before - and", "when - or", "after - so"], ["‘TV를 보기 전에’이므로 before를 쓴다", "‘어리지만’은 대조이므로 but을 쓴다"], 2)
f593("E", "I called Mom _______ I arrived. (나는 도착하고 나서 엄마에게 전화했다.)\nShe is small _______ strong. (그녀는 작지만 힘이 세다.)", "after - but",
     ["before - but", "after - and", "when - or", "after - but", "before - so"], ["‘도착하고 나서’이므로 after를 쓴다", "‘작지만’은 대조이므로 but을 쓴다"], 4)
f593("F", "We play soccer _______ school. (우리는 방과 후에 축구를 한다.)\nI was reading _______ Tom called. (Tom이 전화했을 때 나는 책을 읽고 있었다.)", "after - when",
     ["before - when", "after - but", "and - when", "after - before", "after - when"], ["‘방과 후에’이므로 after를 쓴다", "‘전화했을 때’이므로 when을 쓴다"], 5)

# 5-94 전치사 after: B 밑줄 복원, D~F는 접속사 after 오답을 유형마다 새로
R594 = "after 뒤에 명사(구)만 오면 전치사(after school, after lunch), 주어 + 동사가 오면 접속사(after I finish my homework)이다."
S594 = "접속사 after 오답 네 문장이 C와 똑같았다. 유형마다 접속사 after 문장을 새로 썼다."
CJ = lambda sv: f"after 뒤에 주어 + 동사({sv})가 와서 접속사로 쓰였으므로"; PR = lambda nn: f"after 뒤에 명사({nn})만 와서 전치사로 쓰였으므로"
def f594(t, items, a, s=S594):
    mk(5, 94, t, items, a, R594, s)
f594("B", [("Call me <u>after</u> you arrive.", CJ("you arrive")), ("Tom rested <u>after</u> he finished the work.", CJ("he finished")), ("Mina smiled <u>after</u> she heard the news.", CJ("she heard")), ("We left <u>after</u> the rain stopped.", CJ("the rain stopped")), ("The team practiced <u>after</u> lunch.", PR("lunch"))], 5,
     "밑줄이 사라졌다. 원문항처럼 after에 밑줄을 되살렸다. 보기와 정답은 그대로다.")
f594("D", [("Tom sleeps <u>after</u> lunch.", PR("lunch")), ("Dad reads the paper <u>after</u> he has breakfast.", CJ("he has")), ("We go out <u>after</u> the sun sets.", CJ("the sun sets")), ("Jane feels better <u>after</u> she takes a nap.", CJ("she takes")), ("I clean my room <u>after</u> I get up.", CJ("I get up"))], 1)
f594("E", [("The kids run outside <u>after</u> the bell rings.", CJ("the bell rings")), ("Jane studies <u>after</u> dinner.", PR("dinner")), ("He feels tired <u>after</u> he plays soccer.", CJ("he plays")), ("We will have pizza <u>after</u> Mom comes home.", CJ("Mom comes")), ("She checks her bag <u>after</u> she packs it.", CJ("she packs"))], 2)
f594("F", [("My dog sleeps <u>after</u> it eats.", CJ("it eats")), ("They cheered <u>after</u> their team scored.", CJ("their team scored")), ("Tom washes the dishes <u>after</u> we finish dinner.", CJ("we finish")), ("I go home <u>after</u> work.", PR("work")), ("Let's rest <u>after</u> we climb the hill.", CJ("we climb"))], 4)

# 5-95 when의 쓰임: B 원문항 발문, D~F는 접속사 when 오답을 유형마다 새로
F(5, 95, "B", st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
R595 = "when이 의문문 맨 앞에서 ‘언제’를 물으면 의문사, 뒤에 주어 + 동사를 이끌어 ‘~할 때’를 나타내면 접속사이다."
S595 = "접속사 when 오답 네 문장이 C와 똑같았다. 유형마다 접속사 when 문장을 새로 쓰고, 원문항처럼 When절이 문장 앞에 오는 문장도 넣었다."
WC = "뒤에 주어 + 동사를 이끌어 ‘~할 때’라는 접속사로 쓰였으므로"; WQ = "‘언제’를 묻는 의문사로 쓰였으므로"
def f595(t, items, a, s=S595):
    mk(5, 95, t, [(x, w or WC) for x, w in items], a, R595, s)
f595("D", [("My mom sings <u>when</u> she cooks.", ""), ("<u>When</u> it snows, we build a snowman.", ""), ("He was sleeping <u>when</u> I came in.", ""), ("I feel sleepy <u>when</u> I read.", ""), ("<u>When</u> is the party?", WQ)], 5)
f595("E", [("<u>When</u> does school start?", WQ), ("Take an umbrella <u>when</u> it rains.", ""), ("Tom laughed <u>when</u> he heard the joke.", ""), ("<u>When</u> I got home, Dad was cooking.", ""), ("We were playing <u>when</u> the bell rang.", "")], 1)
f595("F", [("The dog barks <u>when</u> someone knocks.", ""), ("<u>When</u> I was ten, I lived in Busan.", ""), ("She was surprised <u>when</u> she opened the box.", ""), ("<u>When</u> will Tom come?", WQ), ("I drink water <u>when</u> I am thirsty.", "")], 4)

# 5-96 빈칸 접속사: 원문항 발문(뜻 설명 없이), 문맥만으로 정답이 정해지게
S596 = "발문이 ‘단순히 나열하는’, ‘대조 관계’, ‘하나를 골라’처럼 필요한 접속사의 뜻을 알려 주었다. 원문항 발문으로 되돌리고, 뜻 설명 없이도 문맥으로 정답이 하나로 정해지도록 문장을 다듬었다."
def f596(t, p, items, a, s=S596):
    mk(5, 96, t, items, a, R_CJ, s, st="R", p=p)
f596("B", "Tom likes science ________ math. They are his favorite subjects.", [("and", "두 과목을 모두 좋아한다고 나열하므로"), ("when", "뒤에 주어 + 동사가 없어 when을 쓸 수 없으므로"), ("but", "두 과목이 서로 대조되는 내용이 아니므로"), ("after", "‘수학 후에 과학을 좋아한다’는 뜻이 되어 어색하므로"), ("or", "뒤 문장에서 둘 다 좋아하는 과목이라고 했으므로")], 1)
f596("C", "It was raining, ________ we played soccer outside.", [("or", "두 일 중 하나를 고르는 내용이 아니므로"), ("because", "비가 온 것이 밖에서 축구를 한 이유가 될 수 없으므로"), ("so", "비가 와서 밖에서 축구를 했다는 흐름이 어색하므로"), ("but", "비가 왔지만 밖에서 축구를 했다는 대조를 나타내므로"), ("with", "with 뒤에는 주어 + 동사를 쓸 수 없으므로")], 4)
f596("D", "Which do you want, juice _______ milk?", [("after", "두 음료 중 하나를 고르는 질문에 맞지 않으므로"), ("but", "두 음료가 대조되는 내용이 아니므로"), ("when", "뒤에 주어 + 동사가 없어 when을 쓸 수 없으므로"), ("and", "Which로 둘 중 하나를 묻고 있으므로"), ("or", "Which로 둘 중 하나를 고르게 하므로")], 5)
f596("E", "Mina is kind _______ friendly, so everyone likes her.", [("after", "뒤에 명사나 주어 + 동사가 오지 않아 쓸 수 없으므로"), ("and", "친절함과 다정함을 함께 나열하므로"), ("but", "두 성질이 대조되지 않고 둘 다 좋아하는 이유이므로"), ("when", "뒤에 주어 + 동사가 없어 when을 쓸 수 없으므로"), ("or", "두 성질을 모두 갖고 있어 모두가 좋아한다는 흐름이므로")], 2, S596 + " 문장도 같은 단원 91번 F(Jane is kind ___ smart.)와 겹치지 않게 바꿨다.")
f596("F", "Tom is only five years old, _______ he can swim well.", [("when", "‘수영을 잘할 수 있을 때 다섯 살이다’라는 어색한 뜻이 되므로"), ("or", "두 일 중 하나를 고르는 내용이 아니므로"), ("but", "어리지만 수영을 잘한다는 대조를 나타내므로"), ("after", "‘수영을 잘할 수 있은 후에’라는 어색한 뜻이 되므로"), ("because", "수영을 잘하는 것이 다섯 살인 이유가 될 수 없으므로")], 3)

# 5-97 접속사/전치사 구별: 고친 원문항(③ before만 명사 앞의 전치사)에 맞춤
R597 = "when, after, before, until, because, if 등이 뒤에 주어 + 동사를 이끌면 접속사이고, 명사(구)만 오면 전치사이다. after·before·until은 접속사와 전치사로 모두 쓰이므로 뒤에 오는 말을 보고 판단한다."
S597 = "원문항이 접속사 문항(③ before만 명사 앞의 전치사)으로 바뀌어 접속사/전치사 구별 문항으로 다시 썼다. 변형처럼 장소 전치사(on, behind 등)를 섞으면 단어만 보고도 정답이 드러나므로, 원문항처럼 접속사로도 쓰이는 after·before·until을 명사 앞에 쓴 문장을 정답으로 했다."
CJ = "뒤에 주어 + 동사를 이끄는 접속사이므로"
def PRP(w, nn): return f"나머지는 접속사인데 이것만 뒤에 {nn}만 오는 전치사 {w}이므로"
def f597(t, items, a, s=S597):
    mk(5, 97, t, items, a, R597, s, st="R")
f597("B", [("I was reading a book <u>when</u> Tom called me.", CJ), ("Wash your hands <u>before</u> you eat.", CJ), ("I stayed home <u>because</u> I was sick.", CJ), ("We played soccer <u>after</u> school.", PRP("after", "명사 school")), ("Let's wait <u>until</u> she comes back.", CJ)], 4)
f597("C", [("Call me <u>when</u> you get home.", CJ), ("He was late <u>because</u> he missed the bus.", CJ), ("I usually take a walk <u>before</u> dinner.", PRP("before", "명사 dinner")), ("She cleaned her room <u>after</u> her friends left.", CJ), ("Keep running <u>until</u> you see the gate.", CJ)], 3)
f597("D", [("Mina smiled <u>because</u> she got a gift.", CJ), ("Turn off the lights <u>when</u> you leave the room.", CJ), ("I will wait here <u>until</u> the bus comes.", CJ), ("We went to bed <u>after</u> the movie.", PRP("after", "명사 the movie")), ("Finish your homework <u>before</u> you watch TV.", CJ)], 4)
f597("E", [("I can't go out <u>because</u> it is raining.", CJ), ("He brushes his teeth <u>after</u> he eats.", CJ), ("We will go on a picnic <u>if</u> it is sunny.", CJ), ("I was taking a shower <u>when</u> the phone rang.", CJ), ("The shop is open <u>until</u> nine.", PRP("until", "시각 nine"))], 5)
f597("F", [("Let's go out <u>after</u> the rain stops.", CJ), ("I was watching TV <u>when</u> Dad came home.", CJ), ("We stayed at the park <u>until</u> sunset.", PRP("until", "명사 sunset")), ("He was tired <u>because</u> he worked all day.", CJ), ("Close the window <u>before</u> you go out.", CJ)], 3)

# 5-98 before로 연결: 원문항 발문, 순서를 뒤집은 문장·다른 접속사 오답
F(5, 98, "B", st="R", s="발문에 ‘사건 순서를 그대로’, ‘평서문으로’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
R598 = "A before B는 ‘B하기 전에 A한다’, 즉 A가 먼저 일어난다. Before B, A.처럼 before절을 앞에 둘 수도 있다. and before, but으로는 두 사건의 순서를 나타내지 못한다."
S598 = "원문항 오답은 순서를 뒤집은 문장이라 before의 의미를 판단해야 하는데, 변형 오답에는 물음표로 끝나거나 깨진 문장이 있어 형식만으로 지워졌고 발문에 ‘평서문으로’가 붙었다. 원문항 발문으로 되돌리고 순서를 뒤집은 문장·다른 접속사 문장으로 오답을 바꿨다."
REV = "순서가 뒤집혀 나중 일이 먼저 일어난 것이 되므로"; AB = "and before로는 두 문장을 바르게 연결할 수 없으므로"; BUT = "but은 대조를 나타내 순서를 알려 주지 못하므로"; AFT = "before를 쓰지 않았고 after로 순서도 뒤집혔으므로"; OR_ = "or는 선택을 나타내 순서를 알려 주지 못하므로"
def f598(t, ko, s1, s2, items, a, s=S598):
    mk(5, 98, t, items, a, R598, s, st="R", p=f"{ko}\n(1) {s1}\n(2) {s2}")
f598("C", "개에게 먹이를 주고 나서 집을 나선다.", "I feed my dog.", "I leave home.", [("I leave home before I feed my dog.", REV), ("I feed my dog before I leave home.", "먹이 주기가 먼저이고 before로 바르게 연결했으므로"), ("Before I feed my dog, I leave home.", REV), ("I feed my dog after I leave home.", AFT), ("I feed my dog and before I leave home.", AB)], 2,
     S598 + " 문장도 B(손 씻기)나 같은 단원 100번 원문항(이 닦기)과 겹치지 않게 바꿨다.")
f598("D", "책을 읽고 나서 잔다.", "I read a book.", "I sleep.", [("Before I read a book, I sleep.", REV), ("I sleep before I read a book.", REV), ("Before I sleep, I read a book.", "Before절을 앞에 두어 책 읽기가 먼저임을 바르게 나타냈으므로"), ("I read a book but I sleep.", BUT), ("I read a book and before I sleep.", AB)], 3,
     S598 + " before절이 문장 앞에 오는 형태를 정답으로 했다.")
f598("E", "학교에 가기 전에 아침을 먹는다.", "I eat breakfast.", "I go to school.", [("I go to school before I eat breakfast.", REV), ("Before I eat breakfast, I go to school.", REV), ("I eat breakfast after I go to school.", AFT), ("I eat breakfast or I go to school.", OR_), ("I eat breakfast before I go to school.", "아침 먹기가 먼저이고 before로 바르게 연결했으므로")], 5)
f598("F", "밖에 나가기 전에 숙제를 한다.", "I do homework.", "I go outside.", [("Before I go outside, I do homework.", "Before절을 앞에 두어 숙제가 먼저임을 바르게 나타냈으므로"), ("I go outside before I do homework.", REV), ("Before I do homework, I go outside.", REV), ("I do homework and before I go outside.", AB), ("I do homework after I go outside.", AFT)], 1)

# 5-99 (A)(B)(C): 원문항 선택지 형식, 그 우리말의 주어·동사로 오답
R599 = "‘~하고 있었을 때’는 When + 주어 + was/were + -ing로, 뒤의 주절은 과거형으로 쓴다. was/were는 주어에 맞추고(I·3인칭 단수 was, we·they were), 시간 순서에 맞는 접속사를 고른다."
S599 = "오답 네 개가 원문항의 말(they were, start 등)을 그대로 가져와 우리말과 맞지 않아, 우리말의 주어·동사가 들어간 선택지 하나만 남아 정답이 드러났다. 그 우리말의 주어·동사로 접속사, was/were, 시제만 바꾼 오답으로 새로 썼다."
def f599(t, items, a, s=S599):
    mk(5, 99, t, items, a, R599, s, okdup=True)
f599("B", [("(A) After (B) I were (C) rings", "(A) ‘~하고 있을 때’는 When을 쓰고, (B) 주어 I에는 was를, (C) 과거의 일이라 rang을 써야 하므로"), ("(A) When (B) I was (C) rang", "When, I was, rang을 모두 바르게 썼으므로"),
          ("(A) When (B) I was (C) ring", "(C) 과거의 일이라 ring이 아니라 rang을 써야 하므로"), ("(A) Before (B) I was (C) ringing", "(A) ‘~하고 있을 때’는 When을 쓰고, (C) -ing형만으로는 동사 자리에 쓸 수 없으므로"), ("(A) When (B) I am (C) rang", "(B) 과거의 일이라 I was를 써야 하므로")], 2,
     "선택지가 원문항의 형식과 달랐다. 원문항처럼 (A) (B) (C)를 차례로 적는 형식으로 바꿨다. 정답은 그대로다.")
f599("C", [("(A) When (B) I were (C) called", "(B) 주어 I에는 was를 써야 하므로"), ("(A) Before (B) I was (C) called", "(A) ‘공부하고 있었을 때’는 When을 써야 하므로"), ("(A) When (B) I was (C) call", "(C) 과거의 일이라 called를 써야 하므로"),
          ("(A) When (B) I am (C) called", "(B) 과거의 일이라 I was를 써야 하므로"), ("(A) When (B) I was (C) called", "When, I was, called를 모두 바르게 썼으므로")], 5)
f599("D", [("(A) When (B) Jane was (C) opened", "When, Jane was, opened를 모두 바르게 썼으므로"), ("(A) When (B) Jane were (C) opened", "(B) 3인칭 단수 Jane에는 was를 써야 하므로"), ("(A) After (B) Jane was (C) opened", "(A) ‘자고 있었을 때’는 When을 써야 하므로"),
          ("(A) When (B) Jane was (C) opens", "(C) 과거의 일이라 opened를 써야 하므로"), ("(A) When (B) Jane is (C) opened", "(B) 과거의 일이라 Jane was를 써야 하므로")], 1)
f599("E", [("(A) When (B) we was (C) started", "(B) 주어 we에는 were를 써야 하므로"), ("(A) When (B) we were (C) start", "(C) 과거의 일이라 started를 써야 하므로"), ("(A) Before (B) we were (C) started", "(A) ‘걷고 있었을 때’는 When을 써야 하므로"),
          ("(A) When (B) we were (C) started", "When, we were, started를 모두 바르게 썼으므로"), ("(A) When (B) we are (C) starting", "(B) 과거의 일이라 we were를 쓰고, (C) -ing형만으로는 동사 자리에 쓸 수 없으므로")], 4)
f599("F", [("(A) When (B) Tom were (C) came", "(B) 3인칭 단수 Tom에는 was를 써야 하므로"), ("(A) When (B) Tom was (C) comes", "(C) 과거의 일이라 came을 써야 하므로"), ("(A) When (B) Tom was (C) came", "When, Tom was, came을 모두 바르게 썼으므로"),
          ("(A) After (B) Tom was (C) came", "(A) ‘보고 있었을 때’는 When을 써야 하므로"), ("(A) When (B) Tom is (C) came", "(B) 과거의 일이라 Tom was를 써야 하므로")], 3)

# 5-100 after 설명: B 원문항 발문, D~F는 오답 설명을 유형마다 새로
ST5100 = "다음은 접속사 'after'를 사용한 두 문장입니다. 이에 대한 한국어 설명으로 틀린 것을 고르시오."
R5100 = "after는 뒤에 주어 + 동사를 이끌면 ‘~한 후에’라는 접속사로, 명사만 오면 전치사로 쓴다. after절은 문장 앞이나 뒤에 올 수 있고 앞에 오면 보통 쉼표로 구분하며, 위치가 바뀌어도 사건의 순서는 같다."
F(5, 100, "B", st=ST5100, s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
S5100 = "설명 오답 서너 개가 C와 같았다. 원문항처럼 접속사/전치사, 쉼표, 사건 순서에 대한 설명으로 유형마다 새로 썼다."
def f5100(t, items, a, s=S5100):
    FIX.pop((5, 100, t), None)
    talk(5, 100, t, items, a, R5100, s, st=ST5100)
f5100("D", [("(B)에서 After절이 앞에 왔으므로 쉬는 일이 공부보다 먼저 일어난다.", "after절의 위치와 관계없이 공부하는 일이 먼저 일어나므로"), ("(A)와 (B)의 after 뒤에는 주어 he와 동사 studies가 와서 after가 접속사로 쓰였다.", "after 뒤에 주어 + 동사가 왔으므로"),
            ("두 문장 모두 공부하는 일이 쉬는 일보다 먼저 일어난다.", "after가 이끄는 공부가 먼저 일어난 일이므로"), ("(B)처럼 After절이 앞에 오면 보통 절 끝에 쉼표를 찍어 뒷부분과 구분한다.", "after절이 앞에 오면 보통 쉼표로 구분하므로"),
            ("(A)의 after를 when으로 바꾸면 '공부할 때 쉰다'는 뜻이 되어 의미가 달라진다.", "when은 ‘~할 때’라는 뜻이므로")], 1)
f5100("E", [("after는 '~한 후에'라는 뜻으로 두 사건의 순서를 알려 준다.", "after는 ‘~한 후에’라는 뜻이므로"), ("(A)에서 'after she arrives'는 전화하는 때를 나타낸다.", "after절이 전화하는 때를 나타내므로"),
            ("after가 접속사로 쓰였으므로 뒤의 'she arrives'를 'arriving'으로 반드시 바꿔 써야 한다.", "접속사 after 뒤에는 주어 + 동사(she arrives)를 그대로 쓰므로"), ("(B)에서 After절 뒤에 쉼표를 쓴 것은 알맞다.", "after절이 앞에 오면 쉼표로 구분하므로"),
            ("'after lunch'처럼 명사 앞에 오면 after는 전치사로 쓰인다.", "after 뒤에 명사만 오면 전치사이므로")], 3)
f5100("F", [("'after school ends'에서 after 뒤에 주어 school과 동사 ends가 와서 접속사로 쓰였다.", "after 뒤에 주어 + 동사가 왔으므로"), ("(B)의 쉼표를 빼면 after가 전치사로 바뀌어 문장의 뜻이 달라진다.", "쉼표는 절을 구분할 뿐 after의 품사나 뜻을 바꾸지 않으므로"),
            ("'We play after school.'처럼 ends를 빼면 after는 명사 school 앞의 전치사가 된다.", "after 뒤에 명사만 오면 전치사이므로"), ("(A)와 (B)는 after절의 위치만 다르고 뜻은 같다.", "after절의 위치가 바뀌어도 뜻은 같으므로"),
            ("두 문장 모두 학교가 끝나는 일이 노는 일보다 먼저이다.", "after가 이끄는 일이 먼저 일어난 일이므로")], 2)


# ---- 2차 감수(2026-10) 추가 ----
# 5-99 B: 발문(‘짝지어진’)도 원문항(‘연결된’)으로
FIX[(5, 99, "B")]["st"] = "R"
FIX[(5, 99, "B")]["s"] = "발문과 선택지 형식이 원문항과 달랐다. 원문항 발문으로 되돌리고, 선택지를 원문항처럼 (A) (B) (C)를 차례로 적는 형식으로 바꿨다. 정답은 그대로다. 정답 위치 ②."
# 5-100 C: 보기가 문장과 관계없는 한 줄짜리 일반 규칙이고 틀린 설명이 뻔함 → 원문항처럼 두 문장에 대한 설명으로
f5100("C", [("(A)와 (B) 모두 손을 씻는 일이 먹는 일보다 먼저이다.", "after절의 위치와 관계없이 손을 씻는 일이 먼저이므로"), ("(A)의 'after I wash my hands'는 먹는 때를 알려 준다.", "after절이 먹는 때를 나타내므로"),
             ("(B)에서는 After가 이끄는 부분이 앞에 와서 그 끝에 쉼표를 썼다.", "after절이 앞에 오면 보통 쉼표로 구분하므로"), ("(A)를 'I wash my hands after I eat.'으로 바꿔 써도 두 일의 순서는 같다.", "after 앞뒤의 내용을 바꾸면 먹는 일이 먼저가 되어 순서가 반대가 되므로"),
             ("after 뒤에 주어 I와 동사 wash가 왔으므로 after는 접속사로 쓰였다.", "after 뒤에 주어 + 동사가 왔으므로")], 4,
      "보기가 두 문장과 관계없는 한 줄짜리 일반 규칙이어서 원문항 보기(두 문장을 짚어 설명하는 긴 문장)의 절반 길이가 안 되었고, 틀린 설명(before와 after는 항상 같은 시간 관계)이 뻔했다. 원문항처럼 (A)·(B) 문장에 대한 설명으로 새로 썼다. 정답 위치는 그대로다.")
