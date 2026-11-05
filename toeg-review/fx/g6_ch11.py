# 6급 CH11 명령문·제안문 (101~110) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
R_IM = "명령문은 동사원형으로 시작하고(be동사는 Be), 부정 명령문은 Don't/Never + 동사원형으로 쓴다. 제안은 Let's + 동사원형, Shall we + 동사원형?, Why don't we + 동사원형?, How/What about + -ing?로 나타낸다."

# 6-101 명령문 빈칸: 원문항 발문과 우리말 해석
S6101 = "발문이 ‘동사원형으로 시작하는 긍정 명령문’이라고 정답 형태를 알려 주었고 원문항의 우리말 해석이 빠졌다. 원문항 발문으로 되돌리고 우리말 해석을 붙였다. 보기와 정답은 그대로다."
for t, ko in [("B", "네 책을 나에게 보여 줘."), ("C", "나를 따라와."), ("D", "나중에 나에게 전화해."), ("E", "나를 도와줘."), ("F", "나가기 전에 문을 닫아라.")]:
    F(6, 101, t, st="R", p=V(6, 101, t)["passage"] + f"\n({ko})", s=S6101)

# 6-106 be 명령문: 원문항 발문, 우리말 해석이 없는 유형에 해석 추가
S6106 = "발문이 ‘be동사로 시작하는 긍정 명령문’이라고 정답을 알려 주었다. 원문항 발문으로 되돌렸다."
for t in "CDF": F(6, 106, t, st="R", s=S6106 + " 보기와 정답은 그대로다.")
F(6, 106, "B", st="R", p="_______ quiet, please.\n(조용히 해 주세요.)", s=S6106 + " 원문항처럼 우리말 해석을 붙였다. 보기와 정답은 그대로다.")
F(6, 106, "E", st="R", p="_______ careful near the stairs.\n(계단 근처에서 조심해라.)", s=S6106 + " 원문항처럼 우리말 해석을 붙였다. 보기와 정답은 그대로다.")

# 6-102 Don't 빈칸: 옳은 오답을 유형마다 새로
R6102 = "부정 명령문은 Don't + 동사원형으로 쓰고, be동사도 원형 be로 쓴다(Don't be late). -s형, -ing형, to부정사, is/are는 쓸 수 없다."
S6102 = "옳은 오답(run, shout, be late, touch it 또는 원문항의 take pictures 등)이 유형마다·원문항과 같았다. 유형마다 옳은 표현과 정답 오류를 새로 썼다."
OK02 = "Don't 뒤에 동사원형으로 시작하는 말이라 들어갈 수 있으므로"; OKB = "Don't 뒤에 be동사의 원형 be가 와서 들어갈 수 있으므로"
def f6102(t, items, a, s=S6102):
    mk(6, 102, t, [(x, w or OK02) for x, w in items], a, R6102, s)
f6102("B", [("eat in class", ""), ("be noisy", OKB), ("push the door", ""), ("forgets your bag", "Don't 뒤에는 -s형이 아니라 동사원형 forget을 써야 하므로"), ("worry about it", "")], 4)
f6102("C", [("be shy", OKB), ("runs in the hall", "Don't 뒤에는 -s형이 아니라 동사원형 run을 써야 하므로"), ("waste water", ""), ("feed the ducks", ""), ("sit on the grass", "")], 2)
f6102("D", [("touch the dog", ""), ("be sad", OKB), ("throw trash here", ""), ("park your car here", ""), ("are noisy", "Don't 뒤에는 are가 아니라 원형 be를 써야 하므로")], 5)
f6102("E", [("to eat snacks here", "Don't 뒤에는 to 없이 동사원형을 써야 하므로"), ("be afraid", OKB), ("use your phone", ""), ("close your eyes", ""), ("make noise", "")], 1)
f6102("F", [("climb the tree", ""), ("stay up late", ""), ("being rude", "Don't 뒤에는 -ing형이 아니라 원형 be를 써야 하므로"), ("lose your ticket", ""), ("be late again", OKB)], 3)

# 6-104 틀린 문장: 여러 명령·제안 표현을 섞어 유형마다 새로
S6104 = "제안문 오답 네 개가 B와 똑같았다. 원문항처럼 Let's, Shall we, How/What about, Don't, Never 문장을 섞어 유형마다 새로 썼다."
OKS = "명령·제안 표현 뒤에 알맞은 형태를 바르게 썼으므로"
def f6104(t, items, a, s=S6104):
    FIX.pop((6, 104, t), None)
    mk(6, 104, t, [(x, w or OKS) for x, w in items], a, R_IM, s)
f6104("C", [("Never give up.", ""), ("What about to eat pizza?", "What about 뒤에는 to부정사가 아니라 -ing형 eating을 써야 하므로"), ("Shall we dance?", ""), ("Don't forget your homework.", ""), ("Let's meet at the park.", "")], 2)
f6104("D", [("How about going camping?", ""), ("Never tell a lie.", ""), ("Shall we sing together?", ""), ("Let's playing tennis.", "Let's 뒤에는 -ing형이 아니라 동사원형 play를 써야 하므로"), ("Don't be sad.", "")], 4)
f6104("E", [("Let's clean the room.", ""), ("What about riding bikes?", ""), ("Never be late for class.", ""), ("Don't touch the stove.", ""), ("Shall we going home?", "Shall we 뒤에는 -ing형이 아니라 동사원형 go를 써야 하므로")], 5)

# 6-105 세 번째 단어: 원문항 발문, 유형마다 단어 새로
R6105 = "제안문은 Let's (not) + 동사원형 + 목적어, 명령문은 (Please) + 동사원형 + 보어·목적어의 순서로 배열한다."
S6105 = "발문이 ‘Let's not으로 시작하는 기본형 부정 제안문’이라고 첫 두 단어를 알려 주어 세 번째 단어가 바로 정해졌고, C와 E는 단어가 같았다. 원문항 발문으로 되돌리고 유형마다 단어를 새로 썼다."
def f6105(t, words, sent, opts, a, s=S6105):
    FIX.pop((6, 105, t), None)
    pos = {w.lower(): i + 1 for i, w in enumerate(sent.rstrip(".").split())}
    notes = [f"완성 문장 {sent}에서 단어({w})는 {pos[w.lower()]}번째에 오므로" for w in opts]
    F(6, 105, t, st="R", p=" / ".join(words), c=opts, a=a, r=R6105, k=f"완성 문장은 {sent}이고 세 번째 단어는 {opts[a-1]}이다.",
      n=[x + (" 정답이다." if i + 1 == a else " 오답이다.") for i, x in enumerate(notes)], okdup=True, s=s + ipos(a))
for t in "BD": F(6, 105, t, st="R", s="발문이 ‘Let's not으로 시작하는 기본형 부정 제안문’이라고 첫 두 단어를 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f6105("C", ["the", "door", "open", "not", "Let's"], "Let's not open the door.", ["not", "open", "door", "the", "Let's"], 2)
f6105("E", ["be", "Please", "in", "quiet", "class"], "Please be quiet in class.", ["Please", "be", "in", "class", "quiet"], 5, S6105 + " E는 C와 단어가 같아 Please로 시작하는 명령문으로 바꿨다.")
f6105("F", ["not", "Let's", "TV", "watch", "now"], "Let's not watch TV now.", ["watch", "Let's", "not", "TV", "now"], 1)

# 6-108 (A)(B) 제안 표현: 원문항 발문과 밑줄, 정답 조합을 유형마다 다르게
R6108 = "Let's와 Why don't we 뒤에는 동사원형, Shall we 뒤에도 동사원형을 쓰고, How about/What about 뒤에는 -ing형을 쓴다. Shall은 we와 함께 Shall we ~?로 쓴다."
S6108 = "모든 유형의 정답이 원문항과 같은 Let's - Shall이었고, 발문에 조건이 붙었으며 빈칸 밑줄이 사라졌다. 원문항 발문과 빈칸 밑줄을 되살리고, 제안 표현을 바꿔 정답 조합이 유형마다 다르게 했다."
BL = lambda x: f"(<u>   {x}   </u>)"
LB = lambda a_, b_: f"(A) {a_} - (B) {b_}"
def f6108(t, p, items, a, s=S6108):
    mk(6, 108, t, items, a, R6108, s, st="R", p=p, okdup=True)
f6108("B", f"A: I'm bored. {BL('A')} watching a movie?\nB: Good. {BL('B')} go now.", [(LB("Let's", "Shall"), "(A): Let's 뒤에는 -ing형이 아니라 동사원형을 쓰므로"), (LB("How about", "Let's"), "-ing형 앞에 How about, 동사원형 앞에 Let's를 바르게 썼으므로"),
     (LB("Shall", "How about"), "(A): Shall은 we 없이 쓸 수 없고, (B): How about 뒤에는 -ing형을 쓰므로"), (LB("How about", "Shall"), "(B): Shall은 we와 함께 Shall we ~?로 써야 하므로"), (LB("Let's", "Let's"), "(A): Let's 뒤에는 -ing형 watching을 쓸 수 없으므로")], 2)
f6108("C", f"A: It's sunny. {BL('A')} go outside?\nB: Okay. {BL('B')} take a ball.", [(LB("Why don't we", "Let's"), "동사원형 앞 의문문에 Why don't we, 평서문에 Let's를 바르게 썼으므로"), (LB("How about", "Let's"), "(A): How about 뒤에는 동사원형 go가 아니라 going을 쓰므로"),
     (LB("Let's", "Why don't we"), "(A): Let's 문장은 물음표로 끝나지 않고, (B): Why don't we 문장은 물음표로 끝나야 하므로"), (LB("Why don't we", "How about"), "(B): How about 뒤에는 -ing형 taking을 써야 하므로"), (LB("Shall", "Let's"), "(A): Shall은 we와 함께 Shall we ~?로 써야 하므로")], 1)
f6108("D", f"A: We're free. {BL('A')} play tennis.\nB: Nice. {BL('B')} starting now?", [(LB("How about", "Let's"), "(A): How about 뒤에는 -ing형을, (B): Let's 뒤에는 동사원형을 쓰므로"), (LB("Let's", "Shall"), "(B): Shall we 뒤에는 동사원형을 쓰고 Shall만으로는 쓸 수 없으므로"), (LB("Let's", "How about"), "동사원형 앞에 Let's, -ing형 앞에 How about을 바르게 썼으므로"),
     (LB("Shall we", "Let's"), "(A): Shall we 문장은 물음표로 끝나야 하고, (B): Let's 뒤에는 -ing형을 쓰지 않으므로"), (LB("Let's", "Why don't"), "(B): Why don't we 뒤에는 동사원형을 쓰고 we가 빠졌으므로")], 3)
f6108("E", f"A: The room is dark. {BL('A')} we turn on the light?\nB: Good idea. {BL('B')} open the curtains too.", [(LB("Let's", "Shall"), "(A): Let's 뒤에는 we를 쓰지 않고, (B): Shall은 we와 함께 써야 하므로"), (LB("How about", "Let's"), "(A): How about 뒤에는 we + 동사원형을 쓰지 않으므로"),
     (LB("Shall", "How about"), "(B): How about 뒤에는 -ing형 opening을 써야 하므로"), (LB("Are", "Let's"), "(A): be동사 Are와 동사원형 turn을 함께 쓸 수 없으므로"), (LB("Shall", "Let's"), "Shall we와 Let's + 동사원형을 바르게 썼으므로")], 5)
f6108("F", f"A: I'm tired. {BL('A')} taking a break?\nB: Sure. {BL('B')} we sit here?", [(LB("Let's", "Shall"), "(A): Let's 뒤에는 -ing형이 아니라 동사원형을 쓰므로"), (LB("Shall", "Let's"), "(A): Shall we 뒤에는 동사원형을 쓰고, (B): Let's 뒤에는 we를 쓰지 않으므로"), (LB("How about", "Let's"), "(B): Let's 뒤에는 we를 쓰지 않으므로"),
     (LB("How about", "Shall"), "-ing형 앞에 How about, we 앞에 Shall을 바르게 썼으므로"), (LB("Let's", "Do"), "(A): Let's 뒤에는 -ing형을 쓰지 않고, (B): Do we ~?는 제안이 아니므로")], 4)

# 6-109 같은 의미: 정답을 How about 하나로만 두지 않게
R6109 = "Let's + 동사원형은 Shall we + 동사원형?, Why don't we + 동사원형?, How about/What about + -ing?로 바꾸어 쓸 수 있다."
S6109 = "모든 유형의 정답이 원문항과 같은 How about이었다. 유형마다 What about, Shall we, Why don't we 등으로 정답을 바꾸고 빈칸 뒤의 형태(-ing형/동사원형)도 그에 맞췄다."
def f6109(t, s1, s2, items, a, s=S6109):
    mk(6, 109, t, items, a, R6109, s, p=f"{s1}\n= {s2}")
f6109("B", "Let's eat pizza.", "( __________ ) eating pizza?", [("Let's", "Let's 뒤에는 -ing형이 아니라 동사원형을 쓰므로"), ("Shall we", "Shall we 뒤에는 동사원형을 쓰므로"), ("Why", "Why 뒤에 -ing형을 바로 쓸 수 없으므로"), ("Do you", "Do you 뒤에는 동사원형을 쓰고 제안의 뜻도 아니므로"), ("What about", "What about + -ing로 Let's와 같은 제안의 뜻이 되므로")], 5)
f6109("C", "Let's take a break.", "( __________ ) take a break?", [("How about", "How about 뒤에는 -ing형 taking을 써야 하므로"), ("Shall we", "Shall we + 동사원형으로 Let's와 같은 제안의 뜻이 되므로"), ("Do you", "Do you ~?는 제안이 아니라 상대의 습관을 묻는 말이므로"), ("What about", "What about 뒤에는 -ing형 taking을 써야 하므로"), ("Are we", "be동사 뒤에 동사원형을 쓸 수 없으므로")], 2)
f6109("D", "Let's go for a walk.", "( __________ ) go for a walk?", [("Why don't we", "Why don't we + 동사원형으로 Let's와 같은 제안의 뜻이 되므로"), ("How about", "How about 뒤에는 -ing형 going을 써야 하므로"), ("Do we", "Do we ~?는 제안이 아니라 사실을 묻는 말이므로"), ("What about", "What about 뒤에는 -ing형 going을 써야 하므로"), ("Are we", "be동사 뒤에 동사원형을 쓸 수 없으므로")], 1)
f6109("E", "Let's watch a movie.", "( __________ ) we watch a movie?", [("Do", "Do we ~?는 제안이 아니라 사실을 묻는 말이므로"), ("Did", "Did we ~?는 과거의 일을 묻는 말이므로"), ("Shall", "Shall we + 동사원형으로 Let's와 같은 제안의 뜻이 되므로"), ("Are", "be동사 뒤에 동사원형을 쓸 수 없으므로"), ("Why", "Why we ~?는 의문문 어순이 아니므로")], 3)
f6109("F", "Let's visit the science museum.", "Why don't we ( __________ ) the science museum?", [("visiting", "Why don't we 뒤에는 -ing형이 아니라 동사원형을 쓰므로"), ("to visit", "Why don't we 뒤에는 to 없이 동사원형을 쓰므로"), ("visits", "Why don't we 뒤에는 -s형을 쓰지 않으므로"), ("visit", "Why don't we + 동사원형 visit로 Let's와 같은 제안의 뜻이 되므로"), ("visited", "제안에는 과거형을 쓰지 않으므로")], 4)

# 6-110 옳은 것을 모두: 원문항처럼 <보기> 세 개, 정답 조합을 원문항(ㄱ, ㄴ)과 다르게
R6110 = "명령문은 주어 you를 생략하고 동사원형으로 시작하며, 부정은 Don't + 동사원형(Don't be …)으로 쓴다. Let's의 부정은 Let's not + 동사원형이고, Let's + 동사원형은 Shall we/Why don't we + 동사원형?, How about + -ing?와 뜻이 비슷하다."
S6110 = "정답 조합이 원문항과 같은 ‘ㄱ, ㄴ’이었고, 틀린 보기가 ‘동사를 -s/-ed/-ing로 바꾸어야 한다’는 뻔한 내용이었다(C는 <보기>가 네 개). 원문항처럼 <보기> 세 개로 쓰고, 그럴듯한 오개념을 넣어 정답 조합을 유형마다 다르게 했다."
def f6110(t, p, lines, judge, ok, c, s=S6110):
    a = c.index(ok) + 1
    F(6, 110, t, p=p + "\n<보기>\n" + "\n".join(lines), c=c, a=a, r=R6110, pre=["설명별 판정: " + j for j in judge], k=f"옳은 설명은 {ok}이다.", n=setnotes(c, ok, "옳은 설명"), okdup=True, s=s + ipos(a))
C3 = ["ㄱ", "ㄴ", "ㄱ, ㄷ", "ㄴ, ㄷ", "ㄱ, ㄴ"]
f6110("B", "The floor is wet. (A)<u>Don't run</u> here. (B)<u>Be</u> careful.", ["ㄱ. (A)는 Don't + 동사원형의 부정 명령문이다.", "ㄴ. (B)를 부정 명령문으로 바꾸면 'Don't be careful.'이 아니라 'Be not careful.'이 된다.", "ㄷ. (B)의 Be는 형용사 careful 앞에 쓰인 동사원형이다."],
      ["ㄱ O. Don't + 동사원형 run의 부정 명령문이다.", "ㄴ X. be 명령문의 부정도 Don't를 앞에 써서 Don't be careless처럼 만든다.", "ㄷ O. 명령문의 Be는 동사원형이다."], "ㄱ, ㄷ", C3)
f6110("C", "It's lunch time. (A)<u>Let's eat</u> now. (B)<u>Shall we drink</u> water?", ["ㄱ. (A)를 부정 제안으로 바꾸면 'Let's don't eat now.'가 된다.", "ㄴ. (A)의 eat은 Let's 뒤에 오는 동사원형이다.", "ㄷ. (B)는 'Why don't we drink water?'와 뜻이 비슷한 제안문이다."],
      ["ㄱ X. Let's의 부정은 Let's not eat now.이다.", "ㄴ O. Let's 뒤에는 동사원형이 온다.", "ㄷ O. Shall we와 Why don't we는 모두 제안을 나타낸다."], "ㄴ, ㄷ", C3,
      "원문항 <보기>는 세 개인데 변형은 네 개였다. 원문항처럼 <보기>를 세 개로 줄이고, 그럴듯한 오개념(Let's don't)을 넣어 정답 조합을 원문항과 다르게 했다.")
f6110("D", "We have free time. (A)<u>Let's play</u> a game. (B)<u>Shall we invite</u> Mina?", ["ㄱ. (A)는 'Shall we play a game?'과 뜻이 비슷하다.", "ㄴ. (A)를 How about으로 바꾸면 'How about play a game?'이 된다.", "ㄷ. (B)의 주어는 Mina이므로 Shall we 대신 Does Mina를 써야 한다."],
      ["ㄱ O. Let's와 Shall we는 모두 함께 하자는 제안이다.", "ㄴ X. How about 뒤에는 -ing형을 써서 How about playing a game?이 된다.", "ㄷ X. Mina는 초대할 대상(목적어)이고 주어는 we이다."], "ㄱ", C3)
f6110("E", "The room is noisy. (A)<u>Let's not shout</u>. (B)<u>Be</u> quiet.", ["ㄱ. (A)의 not은 Let's와 shout 사이에 와서 부정 제안을 만든다.", "ㄴ. (B)는 주어 You가 생략된 명령문이다.", "ㄷ. (B)를 부정 명령문으로 바꾸면 'Don't be quiet.'가 된다."],
      ["ㄱ O. Let's not + 동사원형으로 부정 제안을 만든다.", "ㄴ O. 명령문은 주어 you를 생략한다.", "ㄷ O. be 명령문의 부정은 Don't be로 만든다."], "ㄱ, ㄴ, ㄷ", ["ㄱ", "ㄱ, ㄴ", "ㄴ, ㄷ", "ㄱ, ㄷ", "ㄱ, ㄴ, ㄷ"])
f6110("F", "It's cold outside. (A)<u>Let's wear</u> coats. (B)<u>Shall we take</u> umbrellas too?", ["ㄱ. (A)의 wear는 Let's(= Let us)의 us에 맞춰 wears로 써야 한다.", "ㄴ. (A)는 'Why don't we wear coats?'로 바꾸어 쓸 수 있다.", "ㄷ. (B)를 How about으로 바꾸면 'How about take umbrellas too?'가 된다."],
      ["ㄱ X. Let's 뒤에는 주어와 관계없이 동사원형을 쓴다.", "ㄴ O. Let's + 동사원형은 Why don't we + 동사원형?으로 바꿀 수 있다.", "ㄷ X. How about 뒤에는 -ing형을 써서 How about taking umbrellas too?가 된다."], "ㄴ", C3)


# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, s, r=R_IM, **kw):
    FIX.pop((6, n, t), None)
    mk(6, n, t, items, a, r, s, **kw)
# 6-101 B~E: 보기의 대문자 표기(To Show, Does Show)를 바로잡음
def f6101(t, ko, base, order, a):
    its = {"base": (base, "명령문은 동사원형으로 시작하므로"), "to": ("To " + base.lower(), "to부정사로는 명령문을 시작할 수 없으므로"), "does": ("Does " + base.lower(), "명령문에 Does를 쓰지 않으므로"),
           "ing": ((base[:-1] if base.endswith("e") else base) + "ing", "-ing형으로는 명령문을 시작할 수 없으므로"), "s": (base + "s", "-s형으로는 명령문을 시작할 수 없으므로")}
    redo(101, t, [its[k] for k in order], a, "발문이 ‘동사원형으로 시작하는 긍정 명령문’이라고 정답 형태를 알려 주었고 원문항의 우리말 해석이 빠졌다. 원문항 발문으로 되돌리고 우리말 해석을 붙였다. 보기의 대문자 표기(To Show 등)도 바로잡았다. 정답은 그대로다.",
         st="R", p=V(6, 101, t)["passage"] + f"\n({ko})")
f6101("B", "네 책을 나에게 보여 줘.", "Show", ["to", "does", "ing", "s", "base"], 5)
f6101("C", "나를 따라와.", "Follow", ["ing", "does", "base", "to", "s"], 3)
f6101("D", "나중에 나에게 전화해.", "Call", ["does", "base", "to", "ing", "s"], 2)
f6101("E", "나를 도와줘.", "Help", ["does", "ing", "to", "s", "base"], 5)
# 6-103 B~E: 정답이 모두 원문항과 같은 How about → 제안 표현을 유형마다 다르게
R6103 = "제안 표현: How about/What about + -ing?, Shall we + 동사원형?, Why don't we + 동사원형?, Let's + 동사원형."
S6103 = "모든 유형의 정답이 원문항과 같은 How about이었다. 제안 표현과 빈칸 뒤의 형태를 바꿔 정답이 유형마다 다르게 했다."
redo(103, "B", [("Why do", "Why do 뒤에 -ing형을 쓸 수 없으므로"), ("What about", "What about + -ing로 제안을 나타내므로"), ("Shall", "Shall 뒤에는 we + 동사원형이 와야 하므로"), ("Do", "Do 뒤에 -ing형을 쓸 수 없으므로"), ("Let's", "Let's 뒤에는 동사원형을 쓰므로")], 2, S6103 + " 대화는 그대로다.", r=R6103)
redo(103, "C", [("Shall we", "Shall we + 동사원형 ~?으로 제안을 나타내므로"), ("How about", "How about 뒤에는 -ing형을 쓰므로"), ("What about", "What about 뒤에는 -ing형을 쓰므로"), ("Why don't", "Why don't 뒤에 주어 we가 있어야 하므로"), ("Are we", "be동사와 동사원형 take를 함께 쓸 수 없으므로")], 1, S6103, r=R6103,
     p="A: I'm tired.\nB: ________ take a break?")
redo(103, "D", [("How about", "How about 뒤에는 -ing형을 쓰고 의문문이 되므로"), ("What about", "What about 뒤에는 -ing형을 쓰고 의문문이 되므로"), ("Shall", "Shall 뒤에는 we가 와야 하고 의문문이 되므로"), ("Let's", "Let's + 동사원형으로 제안을 나타내므로"), ("Why", "Why만으로는 제안문을 만들 수 없으므로")], 4, S6103, r=R6103,
     p="A: It's sunny.\nB: ________ walk in the park.")
redo(103, "E", [("How about", "How about 뒤에는 -ing형을 쓰고 we를 쓰지 않으므로"), ("Let's", "Let's 뒤에는 we를 쓰지 않으므로"), ("Why don't", "Why don't we + 동사원형 ~?으로 제안을 나타내므로"), ("What about", "What about 뒤에는 -ing형을 쓰고 we를 쓰지 않으므로"), ("Are", "be동사와 동사원형 play를 함께 쓸 수 없으므로")], 3, S6103, r=R6103,
     p="A: We are free.\nB: ________ we play tennis?")
# 6-104 B: 쌍둥이 문장(Let's play soccer. / How about play soccer?)과 원문항 정답을 바르게 고친 문장(How about wearing this jacket?)
f6104("B", [("Shall we go home?", ""), ("Let's ride our bikes.", ""), ("How about play soccer?", "How about 뒤에는 동사원형이 아니라 -ing형 playing을 써야 하므로"), ("Don't open the box.", ""), ("What about eating pizza?", "")], 3,
      "정답 문장(How about play soccer?)과 내용이 같은 옳은 문장(Let's play soccer.)이 함께 있었고, ④(How about wearing this jacket?)는 원문항 정답(What about wear this jacket?)을 바르게 고친 문장이었다. 두 문장을 다른 문장으로 바꿨다. 정답은 그대로다.")
# 6-105 D: 정답 낱말(play)과 위치(③)가 원문항과 같음
f6105("D", ["not", "Let's", "a", "taxi", "take"], "Let's not take a taxi.", ["not", "taxi", "take", "Let's", "a"], 3,
      "발문이 ‘Let's not으로 시작하는 기본형 부정 제안문’이라고 첫 두 단어를 알려 주었고, 정답 낱말(play)과 정답 위치가 원문항과 같았다. 원문항 발문으로 되돌리고 낱말을 새로 썼다.")
# 6-107 F: 정답 낱말(touch)이 E와 같음
redo(107, "F", [("throws", "don't 뒤에 -s형을 쓸 수 없으므로"), ("is throw", "don't 뒤에 be동사를 쓸 수 없으므로"), ("to throw", "don't 뒤에 to부정사를 쓸 수 없으므로"), ("throw", "don't 뒤에는 동사원형을 쓰므로"), ("throwing", "밑줄 친 형태 그대로라 고친 것이 아니므로")], 4,
     "정답 낱말(touch)이 E와 같았다. 동사를 바꿨다. 정답 위치는 그대로다.", r="부정 명령문은 Don't + 동사원형으로 쓴다. Please가 붙어도 don't 뒤는 동사원형이다.", p="Please don't <u>throwing</u> trash here.")
