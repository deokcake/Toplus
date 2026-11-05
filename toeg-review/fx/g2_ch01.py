# 2급 CH1 문장의 형식 (1~10) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 2-3 for/of: 판단 기준을 설명하던 발문을 원문항대로
S3 = "발문이 ‘ask 뒤의 사람은 질문·요청을 받는 사람… for 또는 of’라고 판단 기준을 설명해 답을 알려 주어, 원문항 발문 ‘들어가는 전치사가 다른 것’으로 되돌렸다."
XR3 = [("이 문항은 두 전치사 중 지정한 뜻에 맞는 것을 비교한다.", "각 문장의 뜻에 맞는 전치사를 비교한다."), ("상대에게 부탁하거나 질문한다는 지정된 뜻에서", "상대에게 부탁하거나 질문한다는 뜻이므로")]
for t in "BCEF":
    F(2, 3, t, st="R", xr=XR3, s=S3)
R3 = "ask a favor(question) of + 사람은 부탁·질문을 받는 사람을 of로, buy·make·save·bake + 사물 + for + 사람은 받는 사람을 for로 나타낸다."
mk(2, 3, "D", [("Tom made breakfast _____ us.", "make A for + 사람이므로 for가 들어간다."), ("She saved a ticket _____ me.", "save A for + 사람이므로 for가 들어간다."), ("Dad bought a gift _____ Mom.", "buy A for + 사람이므로 for가 들어간다."),
               ("I asked a favor _____ my coach.", "ask a favor of + 사람이므로 of가 들어가 나머지(for)와 다르다."), ("I baked cookies _____ my classmates.", "bake A for + 사람이므로 for가 들어간다.")], 4, R3,
   S3 + " 부자연스러운 ‘asked some advice of my coach’를 ‘asked a favor of my coach’로 바꿨다.", st="R")

# 2-4 F: 뜻을 알려 주던 괄호 삭제, ①을 조건 없이도 틀린 문장으로, ④ 짝 문장 교체
R4 = "5형식의 목적격보어는 목적어의 상태·행동을 설명한다. 상태는 형용사, 목적어가 하는 행동은 사역동사 뒤 원형부정사·지각동사 뒤 원형(-ing)으로 쓰고, 부사는 목적격보어가 될 수 없다."
mk(2, 4, "F", [("The long walk made us tiredly.", "make + 목적어 뒤 목적격보어 자리에 부사를 썼다. tired로 써야 해 틀렸다."), ("I saw the boy dancing.", "지각동사 saw + 목적어 + 현재분사로 옳다."),
               ("She kept the window open.", "keep + 목적어 + 형용사로 옳다."), ("We heard someone knocking on the door.", "지각동사 heard + 목적어 + 현재분사로 옳다."), ("The teacher made us practice.", "사역동사 made + 목적어 + 원형부정사로 옳다.")], 1, R4,
   "발문이 ①의 뜻을 알려 주었고, ④ ‘found the chair comfortable’이 ①과 짝을 이뤘다. 괄호가 없으면 ‘found the room comfortably’가 ‘방을 편하게 찾았다’로 읽힐 수 있어, ①을 조건 없이도 틀린 ‘made us tiredly’로 바꾸고 ④도 다른 문장으로 바꿨다. 발문을 원문항과 같게 했다.", st="R")

# 2-5 학생 설명: 원문항처럼 옳게 설명한 학생을 셋으로 맞춰 보기 형태를 같게
R5 = "4형식은 간접목적어 + 직접목적어, 3형식 전환 때 give·send류는 to, buy·make류는 for를 쓴다. 사역동사 뒤 원형부정사, 수동 관계는 과거분사, 감각동사 뒤 보어는 형용사이다."
def f5(t, lines, judge, ok, c, a):
    F(2, 5, t, p="\n".join(lines), c=c, a=a, r=R5, pre=["학생별 판정:"] + judge, k=f"올바르게 설명한 학생은 {ok}이다.", n=setnotes(c, ok, "올바르게 설명한 학생"),
      s="옳게 설명한 학생이 넷이라 정답이 네 이름이 되어 원문항(세 이름)과 보기 형태가 달랐다. 한 학생의 설명을 틀린 설명으로 바꿔 원문항처럼 세 명을 고르게 했다." + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f5("C", ["Mina: 'She gave me advice.'는 4형식이야.", "Leo: 'The coach had us run.'의 run은 원형부정사야.", "Jane: 'Tom sent a gift for Amy.'에서 Amy가 선물의 수령인이라는 뜻을 나타내려면 for가 맞아.", "Ben: 'I got my phone repaired.'에서 repaired는 수동 관계야.", "Sally: 'The flowers smell sweetly.'는 2형식 보어 자리라 sweetly가 맞아."],
   ["Mina 옳음: gave + 간접목적어 + 직접목적어의 4형식이다.", "Leo 옳음: 사역동사 had 뒤 원형부정사 run이다.", "Jane 틀림: 수령인은 to로 나타낸다. sent a gift to Amy.", "Ben 옳음: 휴대폰이 수리되는 수동 관계라 과거분사이다.", "Sally 틀림: 2형식 보어 자리에는 형용사 sweet를 쓴다."],
   "Mina, Leo, Ben", ["Mina, Jane", "Jane, Ben, Sally", "Leo, Ben", "Mina, Leo, Ben", "Mina, Leo, Sally"], 4)
f5("E", ["Jane: 'He showed me the photo.'는 4형식이야.", "Ben: 'I heard her sing.'은 지각동사 구조로 맞아.", "Sora: 'We made lunch to the children.'의 to가 맞아.", "Min: 'They elected Tom president.'의 president는 목적격 보어야.", "Hana: 'The milk smells sourly.'는 2형식이라 sourly가 맞아."],
   ["Jane 옳음: showed + 간접목적어 + 직접목적어의 4형식이다.", "Ben 옳음: 지각동사 heard + 목적어 + 원형이다.", "Sora 틀림: make는 수혜자를 for로 나타낸다.", "Min 옳음: president가 목적어 Tom을 설명하는 목적격 보어이다.", "Hana 틀림: 2형식 보어 자리에는 형용사 sour를 쓴다."],
   "Jane, Ben, Min", ["Ben, Min", "Jane, Ben, Hana", "Sora, Min, Hana", "Jane, Sora", "Jane, Ben, Min"], 5)

# 2-6 4형식 → 3형식: 발문을 원문항대로, 4형식 그대로인 보기를 뒤섞인 어순 오답으로
R6 = "4형식을 3형식으로 바꿀 때는 ‘주어 + 동사 + 직접목적어(사물) + 전치사 + 간접목적어(사람)’ 순서로 쓴다. give·send·show·teach는 to, buy·make는 for를 쓴다."
S6 = "발문이 ‘「주어+동사+사물+전치사+사람」의 어순으로’라고 구조를 알려 주었고, 원래 4형식 문장이 보기에 그대로 있었다. 발문을 원문항과 같게 하고, 그 보기를 원문항처럼 어순이 뒤섞인 오답으로 바꿨다."
def f6(t, c, a, notes):
    F(2, 6, t, st="R", c=c, a=a, r=R6, n=[(notes[i] + (" 정답이다." if i + 1 == a else " 오답이다.")) for i in range(5)], s=S6)
f6("B", ["My aunt sent a package me.", "My aunt sent a package to me.", "My aunt sent a package for me.", "My aunt sent to me a package.", "My aunt sent me to a package."], 2,
   ["사람 앞에 전치사가 없어 3형식이 되지 않는다.", "사물 + to + 사람 순서로 바르게 바꿨다.", "send는 받는 사람 앞에 to를 쓴다.", "전치사 + 사람을 사물 앞에 두어 어순이 틀렸다.", "사람과 사물 사이에 to를 잘못 넣어 뜻이 통하지 않는다."])
f6("C", ["Dad bought a bicycle me.", "Dad bought a bicycle for me.", "Dad bought for me a bicycle.", "Dad bought me for a bicycle.", "Dad bought a bicycle to me."], 2,
   ["사람 앞에 전치사가 없어 3형식이 되지 않는다.", "사물 + for + 사람 순서로 바르게 바꿨다.", "전치사 + 사람을 사물 앞에 두어 어순이 틀렸다.", "사람과 사물 사이에 for를 잘못 넣어 ‘자전거를 위해 나를 샀다’는 뜻이 되었다.", "buy는 받는 사람 앞에 for를 쓴다."])
f6("D", ["The guide showed to us the map.", "The guide showed the map to us.", "The guide showed us to the map.", "The guide showed the map for us.", "The guide showed the map us."], 2,
   ["전치사 + 사람을 사물 앞에 두어 어순이 틀렸다.", "사물 + to + 사람 순서로 바르게 바꿨다.", "‘우리를 지도로 안내했다’는 다른 뜻이 되었다.", "show는 보는 사람 앞에 to를 쓴다.", "사람 앞에 전치사가 없어 3형식이 되지 않는다."])
f6("E", ["Mina made for her friend a cake.", "Mina made a cake her friend.", "Mina made a cake to her friend.", "Mina made a cake for her friend.", "Mina made her friend for a cake."], 4,
   ["전치사 + 사람을 사물 앞에 두어 어순이 틀렸다.", "사람 앞에 전치사가 없어 3형식이 되지 않는다.", "make는 받는 사람 앞에 for를 쓴다.", "사물 + for + 사람 순서로 바르게 바꿨다.", "사람과 사물 사이에 for를 잘못 넣어 뜻이 통하지 않는다."])
f6("F", ["The teacher taught English for us.", "The teacher taught English us.", "The teacher taught English to us.", "The teacher taught to us English.", "The teacher taught us to English."], 3,
   ["teach는 배우는 사람 앞에 to를 쓴다.", "사람 앞에 전치사가 없어 3형식이 되지 않는다.", "사물 + to + 사람 순서로 바르게 바꿨다.", "전치사 + 사람을 사물 앞에 두어 어순이 틀렸다.", "사람과 사물 사이에 to를 잘못 넣어 뜻이 통하지 않는다."])

# 2-8 목적격 보어 쓰임: 오답 네 개를 유형마다 새로
R8 = "목적격 보어는 목적어의 상태를 설명하는 말이다(make/keep/find/leave/paint/consider + 목적어 + 형용사). 주어를 설명하는 주격 보어, 동사를 꾸미는 부사, 동사의 목적어인 to부정사와 구별한다."
OC = "목적어의 상태를 설명하는 목적격 보어로 〈보기〉와 쓰임이 같다."
SC = "주어의 상태를 설명하는 주격 보어라 〈보기〉와 다르다."
AD = "동사를 꾸미는 부사라 〈보기〉와 다르다."
TO = "동사의 목적어인 to부정사라 〈보기〉와 다르다."
S8 = "오답 네 개가 B와 똑같아서 주격 보어·부사·to부정사 목적어 오답을 유형마다 새로 썼다. 원문항처럼 본문에 <보기> 표시도 넣었다."
P8 = lambda t: "<보기>\n" + V(2, 8, t)["passage"]
mk(2, 8, "C", [("The sky turned <u>dark</u> suddenly.", SC), ("We found the classroom <u>empty</u>.", OC), ("He answered the question <u>correctly</u>.", AD), ("She hopes <u>to win</u> the race.", TO), ("The baby looks <u>happy</u>.", SC)], 2, R8, S8, p=P8("C"))
mk(2, 8, "D", [("The water got <u>cold</u> quickly.", SC), ("We need <u>to hurry</u>.", TO), ("The kids played <u>happily</u>.", AD), ("Her voice sounds <u>soft</u>.", SC), ("The coach kept the players <u>focused</u>.", OC)], 5, R8, S8, p=P8("D"))
mk(2, 8, "E", [("She painted her room <u>white</u>.", OC), ("The dog barked <u>loudly</u>.", AD), ("The leaves became <u>yellow</u>.", SC), ("He decided <u>to stay</u>.", TO), ("This bread smells <u>fresh</u>.", SC)], 1, R8, S8, p=P8("E"))
mk(2, 8, "F", [("The room remained <u>quiet</u>.", SC), ("She spoke <u>calmly</u>.", AD), ("They agreed <u>to help</u>.", TO), ("My uncle seems <u>busy</u>.", SC), ("I considered the plan <u>risky</u>.", OC)], 5, R8, S8, p=P8("F"))

# 2-9 사역동사 made + 원형부정사 이유: 오답 설명을 유형마다 새로
R9 = "사역동사 make + 목적어 + 원형부정사는 목적어가 그 행동을 하게 함을 뜻한다. made처럼 과거형이어도 목적격 보어는 원형부정사를 쓴다."
S9 = "오답 네 설명이 B와 똑같아서 유형마다 다른 그럴듯한 오개념으로 새로 썼다."
mk(2, 9, "C", [("apologize는 자동사라 목적격 보어 자리에 올 수 없기 때문이다.", "자동사도 원형부정사로 목적격 보어가 될 수 있다."), ("me가 목적격이므로 목적격 보어도 목적격 대명사여야 하기 때문이다.", "목적격 보어는 목적어의 행동·상태를 나타내는 말이지 대명사가 아니다."),
               ("사역동사 made 뒤에서 목적어 me가 행동하므로 to apologize가 아니라 apologize를 써야 하기 때문이다.", "사역동사 뒤 원형부정사를 쓴다는 바른 설명이다."), ("to apologize는 미래의 일을 나타내 과거형 made와 어울리지 않기 때문이다.", "시제와 관계없이 사역동사 뒤에는 원형부정사를 쓴다."),
               ("주어 My parents가 복수이므로 apologizes로 형태를 맞춰야 하기 때문이다.", "목적격 보어는 주어와 수 일치를 하지 않는다.")], 3, R9, S9)
mk(2, 9, "D", [("사역동사 made 뒤에서 목적어 us가 행동하므로 rewrite 같은 원형부정사를 써야 하기 때문이다.", "사역동사 뒤 원형부정사를 쓴다는 바른 설명이다."), ("rewrite는 ‘다시’라는 뜻의 re-가 붙어 앞에 to를 쓸 수 없기 때문이다.", "re-와 to의 쓰임은 관계없다."),
               ("made가 과거형이므로 목적격 보어도 과거형 rewrote로 써야 하기 때문이다.", "사역동사 뒤 목적격 보어는 시제와 관계없이 원형이다."), ("us가 목적어이므로 목적격 보어로는 형용사만 올 수 있기 때문이다.", "목적어의 행동을 나타낼 때는 원형부정사를 쓴다."),
               ("report 앞에 the가 있으므로 동명사 rewriting을 써야 하기 때문이다.", "관사는 보어 형태와 관계없다.")], 1, R9, S9)
mk(2, 9, "E", [("made는 사역 의미로 목적어 everyone 뒤에 원형부정사 cry를 요구하기 때문이다.", "사역동사 뒤 원형부정사를 쓴다는 바른 설명이다."), ("cry는 감정을 나타내므로 목적격 보어로 형용사 crying이 와야 하기 때문이다.", "목적어가 우는 행동을 하므로 원형부정사를 쓴다."),
               ("everyone은 단수이므로 cries로 써야 하기 때문이다.", "목적격 보어는 목적어와 수 일치를 하지 않고 원형을 쓴다."), ("made가 ‘만들다’의 뜻이므로 목적격 보어로 명사가 와야 하기 때문이다.", "여기서 made는 ‘~하게 하다’라는 사역의 뜻이다."),
               ("to cry는 목적을 나타내는 부사적 용법이라 문장 끝에 와야 하기 때문이다.", "to cry는 목적이 아니라 목적격 보어 자리에 잘못 쓰인 것이다.")], 1, R9, S9)
mk(2, 9, "F", [("overtime이 부사라서 앞에 to부정사를 쓸 수 없기 때문이다.", "뒤의 부사는 보어 형태와 관계없다."), ("사역동사 made 뒤 목적격 보어에는 to부정사가 아니라 동사원형 work가 와야 하기 때문이다.", "사역동사 뒤 원형부정사를 쓴다는 바른 설명이다."),
               ("the staff가 집합명사라 동사원형 대신 동명사를 써야 하기 때문이다.", "목적어가 집합명사여도 사역동사 뒤에는 원형부정사를 쓴다."), ("made는 상태를 나타내는 동사이므로 뒤에 형용사가 와야 하기 때문이다.", "여기서 made는 행동을 시키는 사역동사이다."),
               ("manager가 3인칭 단수이므로 works로 형태를 맞춰야 하기 때문이다.", "목적격 보어는 주어와 수 일치를 하지 않는다.")], 2, R9, S9)

# 2-10 have/get + 목적어 + 과거분사: 밑줄 복원, B는 선택지 형태를 원문항처럼
UA, UB = "(<u>    A    </u>)", "(<u>    B    </u>)"
R10 = "have/get + 사물 + 과거분사는 그 사물이 수리·손질 같은 일을 받게 함을 나타낸다. should·to 뒤에는 have/get의 원형을 쓴다."
NEED10 = ["(A)는 과거에 화면을 교체받은 일이므로 got(had) + it + 과거분사를 쓴다.", "(B)는 should 뒤이므로 동사원형 have(get)를 쓴다."]
c = ["(A) got it replace - (B) have", "(A) got it replacing - (B) had", "(A) got it replaced - (B) have", "(A) had it replace - (B) get", "(A) replaced it - (B) having"]
F(2, 10, "B", p=f"A: The cracked screen is gone!\nB: I {UA} at a repair shop on Saturday.\nA: Mine is damaged too. I should {UB} mine fixed before our trip.", c=c, a=3, r=R10,
  n=tnotes(c, 3, NEED10, labs=["(A)", "(B)"]),
  s="보기 (B)가 ‘have mine fixing’처럼 긴 구라 원문항(동사 하나)과 형태가 달랐다. 원문항처럼 (B) 빈칸 뒤에 ‘mine fixed’를 두고 보기를 동사 하나로 바꿨으며, 빈칸에 밑줄을 넣었다.")
for t in "CDEF":
    F(2, 10, t, p=V(2, 10, t)["passage"].replace("(A)", UA).replace("(B)", UB), keepx=True, s="원문항처럼 대화의 빈칸 (A)(B)에 밑줄을 넣었다. 보기와 정답은 그대로다.")

# ---- 2차 감수(2026-10) 추가 ----
# 2-8 B: 본문에 <보기> 표시
F(2, 8, "B", p=P8("B"), s="원문항은 본문에 <보기> 표시가 있는데 변형에는 빠져 있어 넣었다. 문장·보기·정답은 그대로다.")
# 2-9 B: 정답만 ‘~때문이다’로 끝나 형식으로 드러남 → 오답도 같은 꼴의 오개념으로
mk(2, 9, "B", [("the team이 여러 사람을 가리키므로 목적격 보어도 복수형으로 써야 하기 때문이다.", "목적격 보어인 동사에는 복수형이 없고 목적어와 수를 맞추지도 않는다."),
               ("사역동사 made 뒤에서 목적어가 직접 행동할 때 목적격 보어로 원형부정사 run을 써야 하기 때문이다.", "사역동사 뒤 원형부정사를 쓴다는 바른 설명이다."),
               ("run은 움직임을 나타내는 동사라 진행의 뜻인 running만 쓸 수 있기 때문이다.", "사역동사 make 뒤에는 -ing가 아니라 원형부정사를 쓴다."),
               ("up the hill이라는 장소 표현이 뒤에 있어 to를 쓸 수 없기 때문이다.", "뒤의 장소 표현은 보어 형태와 관계없다."),
               ("made는 ‘만들다’라는 뜻의 3형식 동사라 뒤에 동사가 올 수 없기 때문이다.", "여기서 made는 ‘~하게 하다’라는 사역동사로 5형식을 이룬다.")], 2, R9,
   "정답만 ‘~때문이다’로 끝나는 긴 설명이고 오답 넷은 짧은 단정문이라 형식만으로 답이 드러났다. 원문항처럼 다섯 보기를 모두 ‘~때문이다’로 끝나는 그럴듯한 설명으로 다시 썼다.")
