# 4급 CH3 현재시제·be동사·일반동사 (21~30) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def talk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 잘못된 설명이다. 따라서 정답이다." if i + 1 == a else " 옳은 설명이다. 따라서 오답이다.")) if w.endswith("므로") else (w + (" 잘못된 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.")) for i, (_, w) in enumerate(items)], k=items[a-1][1], s=s + ipos(a), **kw)
def slotnote(ch, good, why, labs=("첫째", "둘째", "셋째"), sep=" - "):
    xs = [x.strip() for x in ch.split(sep)]; gs = [x.strip() for x in good.split(sep)]
    if xs == gs: return "모든 빈칸에 알맞은 말을 골랐으므로"
    bits = [f"{labs[i]} 빈칸 {x}: {w}" for i, (x, g, w) in enumerate(zip(xs, gs, why)) if x != g]
    return ", ".join(bits) + ". 따라서"

# 4-21 현재 시제가 아닌 문장: 유형마다 문장을 새로
R421 = "현재 시제는 현재의 상태·습관·일반적 사실을 나타내며 동사원형이나 -s/-es형, am/is/are를 쓴다. 과거형(bought, studied, played, visited)은 이미 끝난 일을 나타낸다."
S421 = "현재 시제 오답 네 문장이 B와 똑같았다. 유형마다 문장을 새로 썼다."
def PR(v): return f"현재형({v})으로 현재의 상태·습관을 나타내므로"
def PA(v): return f"과거형({v})을 쓴 과거 시제 문장이라 현재 시제가 아니므로"
def f421(t, items, a, s=S421):
    mk(4, 21, t, items, a, R421, s)
f421("C", [("My brother likes pizza.", PR("likes")), ("Birds fly south in winter.", PR("fly")), ("Mina bought a new bag.", PA("bought")), ("I am thirsty now.", PR("am")), ("The store opens at nine.", PR("opens"))], 3,
     "정답(He went to school.)이 원문항과 똑같았고 오답도 B와 같았다. 문장을 모두 새로 썼다.")
f421("D", [("Tom has two cats.", PR("has")), ("The sun rises in the east.", PR("rises")), ("We are in the same class.", PR("are")), ("She studied yesterday.", PA("studied")), ("My mom works at a bank.", PR("works"))], 4)
f421("E", [("They played soccer last night.", PA("played")), ("Jane speaks Chinese well.", PR("speaks")), ("It is cold today.", PR("is")), ("You look tired.", PR("look")), ("He drinks milk every morning.", PR("drinks"))], 1)
f421("F", [("The bus leaves at eight.", PR("leaves")), ("I have a headache.", PR("have")), ("Minho and I are friends.", PR("are")), ("Dad washes the car on Sundays.", PR("washes")), ("We visited grandma last week.", PA("visited"))], 5)

# 4-22 C: 원문항과 같던 문장을 새로
mk(4, 22, "C", [("is - is", "복수 주어 Mom and Dad에는 are를 쓰므로"), ("are - is", "복수 주어 Mom and Dad에 are, 단수 주어 The weather에 is를 바르게 썼으므로"), ("are - are", "단수 주어 The weather에는 is를 쓰므로"),
                ("am - is", "am은 주어 I에만 쓰므로"), ("is - are", "복수 주어에 is, 단수 주어에 are를 써서 둘 다 틀렸으므로")], 2,
   "현재형 be동사는 I에 am, 3인칭 단수 주어에 is, you와 복수 주어에 are를 쓴다.", "제시문과 정답(is - are)이 원문항과 똑같았다. 문장을 새로 쓰고 정답 순서를 are - is로 바꿨다.",
   p="Mom and Dad _____ in the kitchen.\nThe weather _____ nice today.", okdup=True)

# 4-23 수일치가 올바른 문장: 짝 문장 없이 유형마다 새로
R423 = "현재 시제에서 3인칭 단수 주어의 일반동사에는 -s/-es를 붙이고(have → has), 복수 주어에는 동사원형을 쓴다. 3인칭 단수 주어의 부정은 doesn't + 동사원형이다."
S423 = "정답 문장과 같은 문장의 틀린 형태가 함께 있어 대비 단서가 되었고, 오답 네 개가 유형마다 같았다. 짝 문장 없이 유형마다 새로 썼다."
def f423(t, items, a, s=S423):
    mk(4, 23, t, items, a, R423, s)
f423("B", [("My dog run very fast.", "3인칭 단수 주어 My dog에는 runs를 쓰므로"), ("The children plays in the park.", "복수 주어 The children에는 play를 쓰므로"), ("The news is interesting.", "단수 취급하는 news에 is를 바르게 썼으므로"),
           ("She don't eat meat.", "3인칭 단수 주어 She의 부정은 doesn't이므로"), ("My parents works hard.", "복수 주어 My parents에는 work를 쓰므로")], 3)
f423("C", [("Tom watch TV every night.", "3인칭 단수 주어 Tom에는 watches를 쓰므로"), ("The girls sings well.", "복수 주어 The girls에는 sing을 쓰므로"), ("It rain a lot in July.", "3인칭 단수 주어 It에는 rains를 쓰므로"),
           ("He don't know the answer.", "3인칭 단수 주어 He의 부정은 doesn't이므로"), ("My uncle teaches math.", "3인칭 단수 주어 My uncle에 teaches를 바르게 썼으므로")], 5,
     S423 + " 정답(Water boils at 100°C.)이 원문항과 같아 새로 썼다.")
f423("D", [("The boys play soccer.", "복수 주어 The boys에 play를 바르게 썼으므로"), ("Jane cry easily.", "3인칭 단수 주어 Jane에는 cries를 쓰므로"), ("Our teacher have a car.", "3인칭 단수 주어 Our teacher에는 has를 쓰므로"),
           ("The birds sings in the morning.", "복수 주어 The birds에는 sing을 쓰므로"), ("Mina don't like carrots.", "3인칭 단수 주어 Mina의 부정은 doesn't이므로")], 1)
f423("E", [("The baby cry at night.", "3인칭 단수 주어 The baby에는 cries를 쓰므로"), ("Jane studies English.", "3인칭 단수 주어 Jane에 studies를 바르게 썼으므로"), ("My friends lives near here.", "복수 주어 My friends에는 live를 쓰므로"),
           ("Tom go to bed at ten.", "3인칭 단수 주어 Tom에는 goes를 쓰므로"), ("She have long hair.", "3인칭 단수 주어 She에는 has를 쓰므로")], 2)
f423("F", [("The students is in the gym.", "복수 주어 The students에는 are를 쓰므로"), ("My cat sleep all day.", "3인칭 단수 주어 My cat에는 sleeps를 쓰므로"), ("He fix cars.", "3인칭 단수 주어 He에는 fixes를 쓰므로"),
           ("These pants are new.", "복수 취급하는 pants에 are를 바르게 썼으므로"), ("Dad don't drink coffee.", "3인칭 단수 주어 Dad의 부정은 doesn't이므로")], 4)

# 4-24 대답에 맞는 질문: 원문항 발문, 원문항처럼 문법은 옳지만 대답과 맞지 않는 오답
R424 = "Do/Does 의문문에는 do/does로, be동사 의문문에는 am/is/are로, 과거 의문문에는 did로, 조동사 의문문에는 그 조동사로 답한다. 대답의 대명사는 질문의 주어에 맞춘다."
S424 = "발문에 ‘같은 대상을 받아 현재형으로 직접 대답’ 조건이 붙었고, 원문항 오답은 문법은 옳지만 대답과 맞지 않는 질문인데 변형 오답은 형태가 틀린 질문(Do Jane likes 등)이라 인지 과정이 달랐으며 유형마다 반복되었다. 원문항 발문으로 되돌리고 오답을 문법은 옳지만 대답과 맞지 않는 질문으로 유형마다 새로 썼다."
def f424(t, reply, items, a, s=S424):
    mk(4, 24, t, items, a, R424, s, st="R", p=f"A: _____________________\nB: {reply}", okdup=True)
f424("B", "No, they don't have a dog. They have a cat.", [("Are your neighbors at home?", "be동사 질문이라 No, they aren't로 답하므로"), ("Are they your neighbors?", "be동사 질문이라 No, they aren't로 답하므로"),
     ("Does your neighbor have a dog?", "단수 주어라 No, he(she) doesn't로 답하므로"), ("Do your neighbors have a dog?", "복수 주어 + Do 의문문이라 No, they don't로 답하므로"), ("Is the dog outside?", "be동사 질문이고 주어가 단수라 No, it isn't로 답하므로")], 4,
     "발문에 ‘현재형으로 직접 대답’ 조건이 붙어 시제를 알려 주었고 오답에 형태 오류(has)가 섞였다. 원문항 발문으로 되돌리고 오답을 문법은 옳지만 대답과 맞지 않는 질문으로 바꿨다.")
f424("C", "No, she doesn't.", [("Is Jane your sister?", "be동사 질문이라 No, she isn't로 답하므로"), ("Does Tom like milk?", "주어 Tom은 he로 받으므로"), ("Do Jane and Amy like milk?", "복수 주어라 No, they don't로 답하므로"),
     ("Does Jane like milk?", "3인칭 단수 여성 주어 + Does 의문문이라 No, she doesn't로 답하므로"), ("Can Jane swim?", "조동사 can 질문이라 No, she can't로 답하므로")], 4)
f424("D", "No, he doesn't.", [("Does Tom play soccer?", "3인칭 단수 남성 주어 + Does 의문문이라 No, he doesn't로 답하므로"), ("Is Tom a soccer player?", "be동사 질문이라 No, he isn't로 답하므로"), ("Do they play soccer?", "복수 주어라 No, they don't로 답하므로"),
     ("Does Jane play soccer?", "주어 Jane은 she로 받으므로"), ("Did Tom play soccer?", "과거 질문이라 No, he didn't로 답하므로")], 1)
f424("E", "No, we don't.", [("Are you and your brother students?", "be동사 질문이라 No, we aren't로 답하므로"), ("Do they study English?", "주어 they는 they로 받으므로"), ("Do you and your brother study English?", "you and your brother를 we로 받는 Do 의문문이라 No, we don't로 답하므로"),
     ("Did you study English?", "과거 질문이라 didn't로 답하므로"), ("Does your brother study English?", "단수 주어라 No, he doesn't로 답하므로")], 3)
f424("F", "No, I don't.", [("Are you tired?", "be동사 질문이라 No, I'm not으로 답하므로"), ("Do you watch TV every day?", "you에 대한 Do 의문문이라 No, I don't로 답하므로"), ("Does she watch TV every day?", "주어 she는 she로 받으므로"),
     ("Did you watch TV yesterday?", "과거 질문이라 No, I didn't로 답하므로"), ("Can you watch TV now?", "조동사 can 질문이라 No, I can't로 답하므로")], 2)

# 4-25 [설명] 빈칸에 문법 용어·형태: 원문항 형식(㉠㉡ + 설명 글)
R425 = "don't/doesn't와 Do/Does 뒤에는 동사원형을 쓴다. 3인칭 단수 주어에는 does·doesn't와 -s/-es형을, 그 밖의 주어에는 do·don't와 동사원형을 쓴다."
S425 = "원문항은 [설명] 글의 빈칸 (A)(B)에 문법 용어를 넣는 형식인데, 변형은 설명 글 없이 고칠 형태를 바로 고르는 형식으로 바뀌었고 기호 ㉠㉡이 ᄀᄂ으로 바뀌었다. 원문항 발문과 형식(㉠㉡ + [설명] 글 속 빈칸)으로 되돌리고 유형마다 정답 조합을 달리했다."
BA, BB = "(<u>    A    </u>)", "(<u>    B    </u>)"
def f425(t, s1, s2, e1, e2, c, a, why, s=S425):
    p = f"㉠ {s1}\n㉡ {s2}\n[설명]\n- {e1}\n- {e2}"
    L = lambda z: re.sub(r"\([AB]\) ", "", z)
    mk(4, 25, t, [(x, slotnote(L(x), L(c[a-1]), why, labs=("(A)", "(B)"), sep=", ")) for x in c], a, R425, s, st="R", p=p, okdup=True)
f425("B", "We don't watches TV.", "Does they like pizza?", f"문장 ㉠에서 'don't' 뒤에는 반드시 {BA} 형태가 와야 한다. 따라서 'watches'를 'watch'로 고쳐야 한다.",
     f"문장 ㉡에서 주어 'they'는 복수이므로 'Does' 대신 {BB}를 써야 한다.", ["(A) 동사원형, (B) Do", "(A) 과거형, (B) Does", "(A) 동사원형, (B) Does", "(A) -ing형, (B) Do", "(A) to부정사, (B) Did"], 1,
     ["don't 뒤에는 동사원형이 온다", "복수 주어의 의문문은 Do로 시작한다"], "설명 글 없이 고칠 형태를 바로 고르는 형식으로 바뀌었다. " + S425[S425.index("원문항 발문과"):])
f425("C", "Tom don't like carrots.", "They studies hard.", f"문장 ㉠에서 주어 'Tom'은 3인칭 단수이므로 'don't' 대신 {BA}를 써야 한다.",
     f"문장 ㉡에서 주어 'They'는 복수이므로 'studies'를 {BB} 형태인 'study'로 고쳐야 한다.", ["(A) doesn't, (B) -s나 -es", "(A) doesn't, (B) 동사원형", "(A) isn't, (B) 동사원형", "(A) didn't, (B) -ing형", "(A) aren't, (B) 과거형"], 2,
     ["3인칭 단수 주어의 부정은 doesn't이다", "복수 주어에는 동사원형을 쓴다"], "두 문장이 원문항과 같았고 형식도 원본과 달랐다. 문장을 새로 쓰고 " + S425[S425.index("원문항 발문과"):])
f425("D", "Tom doesn't likes milk.", "Does Jane plays the piano?", f"문장 ㉠에서 'doesn't' 뒤에는 반드시 {BA} 형태가 와야 한다. 따라서 'likes'를 'like'로 고쳐야 한다.",
     f"문장 ㉡에서 'Does' 뒤에도 {BB} 형태가 와야 하므로 'plays'를 'play'로 고쳐야 한다.", ["(A) 동사원형, (B) -s나 -es", "(A) -ing형, (B) 동사원형", "(A) 과거형, (B) 3인칭 단수형", "(A) to부정사, (B) 과거형", "(A) 동사원형, (B) 동사원형"], 5,
     ["doesn't 뒤에는 동사원형이 온다", "Does 뒤에도 동사원형이 온다"])
f425("E", "Jane doesn't studies English.", "He go to school by bus.", f"문장 ㉠에서 'doesn't' 뒤에는 반드시 {BA} 형태가 와야 한다. 따라서 'studies'를 'study'로 고쳐야 한다.",
     f"문장 ㉡에서 주어 'He'는 3인칭 단수이므로 'go'를 {BB} 형태인 'goes'로 고쳐야 한다.", ["(A) -ing형, (B) 과거형", "(A) to부정사, (B) -ing형", "(A) 3인칭 단수형, (B) 동사원형", "(A) 과거형, (B) 동사원형", "(A) 동사원형, (B) 3인칭 단수형"], 5,
     ["doesn't 뒤에는 동사원형이 온다", "3인칭 단수 주어에는 3인칭 단수형(goes)을 쓴다"])
f425("F", "Do she have a pet?", "They doesn't eat meat.", f"문장 ㉠에서 주어 'she'는 3인칭 단수이므로 'Do' 대신 {BA}를 써야 한다.",
     f"문장 ㉡에서 주어 'They'는 복수이므로 'doesn't' 대신 {BB}를 써야 한다.", ["(A) Did, (B) don't", "(A) Does, (B) doesn't", "(A) Is, (B) aren't", "(A) Does, (B) don't", "(A) Are, (B) didn't"], 4,
     ["3인칭 단수 주어의 의문문은 Does로 시작한다", "복수 주어의 부정은 don't이다"])

# 4-26 질문과 응답: 원문항 발문, 원문항처럼 대답의 형태·인칭을 판별
R426 = "be동사 짧은 대답은 주어에 맞춰 I am, you/we/they are, he/she/it is로 쓰고, 질문의 I는 대답에서 you로, you는 I(또는 we)로 바뀐다. this/that은 대답에서 it으로 받는다."
S426 = "정답 대화와 같은 질문의 틀린 대답이 함께 있어 대비 단서가 되었고, 선택지가 유형마다 같았으며, 발문의 조건(we는 두 화자를 모두 포함)은 불필요했다. 원문항 발문으로 되돌리고, 원문항처럼 대답의 인칭·형태를 판별하는 대화로 유형마다 새로 썼다."
F(4, 26, "B", st="R", s="발문에 ‘두 화자가 주고받는 기본적인 짧은 질문·응답’과 we의 뜻 조건이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
def f426(t, items, a, s=S426):
    mk(4, 26, t, items, a, R426, s, st="R")
f426("C", [("Are you hungry? - Yes, you are.", "you에 대한 질문에는 I로 답해 Yes, I am이므로"), ("Is he your brother? - No, he aren't.", "he에는 isn't를 쓰므로"), ("Are we late? - No, you aren't.", "우리(we)에 대한 질문에 상대가 you로 받아 바르게 답했으므로"),
           ("Is it cold? - Yes, it are.", "it에는 is를 쓰므로"), ("Are they students? - Yes, they aren't.", "Yes 뒤에는 긍정 they are를 쓰므로")], 3)
f426("D", [("Am I right? - Yes, I am.", "I에 대한 질문에는 you로 답해 Yes, you are이므로"), ("Is Jane busy? - Yes, she are.", "she에는 is를 쓰므로"), ("Are they ready? - No, they isn't.", "they에는 aren't를 쓰므로"),
           ("Is this your bag? - Yes, this is.", "대답에서 this는 it으로 받아 Yes, it is이므로"), ("Are you a student? - Yes, I am.", "you에 대한 질문에 I로 받아 바르게 답했으므로")], 5)
f426("E", [("Are you and Tom friends? - Yes, you are.", "you and Tom에 대한 질문에는 we로 답해 Yes, we are이므로"), ("Is the dog hungry? - Yes, it is.", "the dog을 it으로 받아 바르게 답했으므로"), ("Am I tall? - No, I'm not.", "I에 대한 질문에는 you로 답해 No, you aren't이므로"),
           ("Are your parents home? - No, they isn't.", "they에는 aren't를 쓰므로"), ("Is Mina sick? - Yes, he is.", "Mina는 she로 받으므로")], 2)
f426("F", [("Is that your pen? - No, that isn't.", "대답에서 that은 it으로 받아 No, it isn't이므로"), ("Are we in the same class? - Yes, you is.", "you에는 are를 쓰므로"), ("Am I wrong? - No, you aren't.", "I에 대한 질문에 you로 받아 바르게 답했으므로"),
           ("Are you busy? - Yes, you are.", "you에 대한 질문에는 I로 답해 Yes, I am이므로"), ("Is Tom tired? - No, he aren't.", "he에는 isn't를 쓰므로")], 3,
     S426 + " 정답 대화는 원문항(Am I late? - Yes, you are. ④)과 겹치지 않게 질문과 위치를 달리했다.")

# 4-27 Yes 대답에 맞는 질문: 원문항 발문, 실제로 있는 형태의 오답(의문사·진행형·과거 등)
R427 = "Yes/No로 답하는 일반동사 현재 의문문은 Do/Does + 주어 + 동사원형이다. 의문사 의문문은 Yes/No로 답하지 않고, 진행형·과거 의문문에는 is/did로 답한다."
S427 = "발문이 ‘일반동사 현재형의 예/아니요 질문’이라고 정답 형식을 알려 주었고 오답에 없는 형태(Doeses, appless 등)가 있었다. 원문항 발문으로 되돌리고, 원문항처럼 의문사 의문문·진행형·과거 의문문 같은 실제 형태로 오답을 바꿨다."
WH = "의문사 의문문은 Yes/No로 답하지 않으므로"
def f427(t, reply, items, a, s=S427):
    mk(4, 27, t, items, a, R427, s, st="R", p=f"A: __________________________________\nB: {reply}")
f427("B", "Yes, my father works in Seoul.", [("Where does your father work?", WH), ("Is your father working in Seoul now?", "진행형 질문에는 Yes, he is로 답하므로"), ("Does your father work in Seoul?", "3인칭 단수 주어 + Does + 동사원형의 현재 의문문이므로"),
     ("Do your father work in Seoul?", "3인칭 단수 주어에는 Does를 쓰므로"), ("Did your father work in Seoul?", "과거 질문에는 Yes, he did로 답하므로")], 3)
f427("C", "Yes, my sister walks to school every day.", [("Does your sister walk to school every day?", "3인칭 단수 주어 + Does + 동사원형의 현재 의문문이므로"), ("How does your sister go to school?", WH), ("Is your sister walking to school?", "진행형 질문에는 Yes, she is로 답하므로"),
     ("Do your sister walk to school every day?", "3인칭 단수 주어에는 Does를 쓰므로"), ("Did your sister walk to school yesterday?", "과거 질문에는 Yes, she did로 답하므로")], 1,
     "제시문과 정답이 원문항과 똑같았고 발문이 정답 형식을 알려 주었다. 대화를 새로 쓰고 " + S427[S427.index("원문항 발문으로"):])
f427("D", "Yes, Jane likes apples.", [("What does Jane like?", WH), ("Is Jane liking apples?", "like는 진행형으로 쓰지 않고, 진행형 질문에는 is로 답하므로"), ("Do Jane like apples?", "3인칭 단수 주어에는 Does를 쓰므로"),
     ("Does Jane like apples?", "3인칭 단수 주어 + Does + 동사원형의 현재 의문문이므로"), ("Did Jane like apples?", "과거 질문에는 Yes, she did로 답하므로")], 4)
f427("F", "Yes, I study English every day.", [("What do you study every day?", WH), ("Are you studying English now?", "진행형 질문에는 Yes, I am으로 답하므로"), ("Does you study English every day?", "주어 you에는 Do를 쓰므로"),
     ("Did you study English yesterday?", "과거 질문에는 Yes, I did로 답하므로"), ("Do you study English every day?", "you + Do + 동사원형의 현재 의문문이므로")], 5)

# 4-28 잘못 설명한 학생: 모든 선택지에 학생 이름, 제시 문장에 맞춘 설명
R428 = "일반동사 현재 의문문은 Do/Does + 주어 + 동사원형이다. 3인칭 단수 주어에는 Does, 그 밖의 주어에는 Do를 쓰고, 대답은 Yes, 주어 + do/does. / No, 주어 + don't/doesn't.로 한다."
S428 = "원문항은 다섯 학생의 설명을 판별하는데, 변형은 정답 선택지에만 학생 이름이 붙고 나머지는 이름 없는 일반 규칙이어서 이름만 보고 정답을 고를 수 있었고 오답이 유형마다 같았다. 모든 선택지에 학생 이름을 붙이고 제시 문장에 맞춘 설명으로 유형마다 새로 썼다."
def f428(t, p, items, a, s=S428):
    talk(4, 28, t, items, a, R428, s, st="R", p=p)
f428("B", "Do they play soccer?", [("도윤: 주어 they가 복수라서 문장 앞에 Do를 썼어.", "복수 주어의 의문문은 Do로 시작하므로"), ("지아: 운동 이름 soccer 앞에는 관사를 쓰지 않았어.", "운동 이름 앞에는 관사를 쓰지 않으므로"),
     ("현우: 대답은 Yes, they do.라고 할 수 있어.", "Do 의문문에는 do로 답하므로"), ("소민: Do 뒤의 동사는 plays로 써야 해.", "Do 뒤에는 동사원형 play를 쓰므로"), ("태오: 일반동사 play가 있어서 be동사 Are가 아니라 Do로 물었어.", "일반동사 의문문은 Do/Does로 만들므로")], 4)
f428("C", "Does your sister walk to school?", [("수아: 주어 your sister가 3인칭 단수라서 Does를 썼어.", "3인칭 단수 주어의 의문문은 Does로 시작하므로"), ("은우: 동생이 지금 걷고 있는지 묻는 진행형 문장이야.", "Does + 동사원형은 현재의 습관을 묻는 현재 시제이므로"),
     ("준호: Does가 있으니 walk에는 -s를 붙이지 않아.", "Does 뒤에는 동사원형을 쓰므로"), ("하린: 대답은 No, she doesn't.라고 할 수 있어.", "Does 의문문에는 doesn't로 답하므로"), ("시윤: 주어가 your sister라서 대답할 때 she로 받아.", "여성 단수 주어는 she로 받으므로")], 2,
     "문장(Does Amy need help …)과 정답 설명이 원문항과 같았고 정답에만 이름이 붙었다. 문장을 새로 쓰고 모든 선택지에 학생 이름을 붙였다.")
f428("D", "Does Tom study English?", [("서진: 주어 Tom이 3인칭 단수라서 Does를 썼어.", "3인칭 단수 주어의 의문문은 Does로 시작하므로"), ("민재: 대답은 Yes, he does.라고 할 수 있어.", "Does 의문문에는 does로 답하므로"),
     ("가은: study는 동사원형이라 Does 뒤에 바르게 쓰였어.", "Does 뒤에는 동사원형을 쓰므로"), ("주원: 일반동사 의문문이라 be동사 Is를 쓰지 않았어.", "일반동사 의문문은 Do/Does로 만들므로"), ("예은: Does 뒤에는 과거형 동사를 써야 해.", "Does 뒤에는 동사원형을 쓰므로")], 5)
f428("E", "Do you need help?", [("건우: Do 의문문에는 be동사 are를 함께 써서 Do are you need help?라고 해야 해.", "일반동사 의문문에 be동사를 함께 쓰지 않으므로"), ("채원: 주어 you에는 Do를 써서 물어.", "you의 의문문은 Do로 시작하므로"),
     ("지호: need는 일반동사라서 Do로 의문문을 만들어.", "일반동사 의문문은 Do/Does로 만들므로"), ("유나: 대답은 Yes, I do.라고 할 수 있어.", "you에 대한 질문에는 I로 받아 do로 답하므로"), ("다인: Do 뒤에 동사원형 need를 바르게 썼어.", "Do 뒤에는 동사원형을 쓰므로")], 1)
f428("F", "Does Jane like milk?", [("하은: 주어 Jane이 3인칭 단수라서 Does를 썼어.", "3인칭 단수 주어의 의문문은 Does로 시작하므로"), ("도현: 우유를 좋아한다면 Yes, she does.처럼 does를 써서 대답해.", "Does 의문문에는 does로 답하므로"),
     ("소율: 3인칭 단수 질문에는 Do를 써야 해.", "3인칭 단수 주어에는 Does를 쓰므로"), ("우진: like는 동사원형이라 Does 뒤에 바르게 쓰였어.", "Does 뒤에는 동사원형을 쓰므로"), ("서아: milk는 셀 수 없는 명사라 a를 붙이지 않았어.", "셀 수 없는 명사에는 a를 붙이지 않으므로")], 3)

# 4-29 C: 원문항과 같던 대화를 새로
mk(4, 29, "C", [("doesn't walks", "doesn't 뒤에는 동사원형을 쓰므로"), ("doesn't walk", "3인칭 단수 주어 she의 부정 doesn't + 동사원형으로 바르게 고쳤으므로"), ("don't walk", "3인칭 단수 주어에는 don't가 아니라 doesn't를 쓰므로"),
                ("doesn't walking", "doesn't 뒤에 -ing형을 쓸 수 없으므로"), ("doesn't walked", "doesn't 뒤에 과거형을 쓸 수 없으므로")], 2,
   "일반동사 현재 부정문은 3인칭 단수 주어에 doesn't + 동사원형, 그 밖의 주어에 don't + 동사원형을 쓴다.", "대화와 정답(doesn't like)이 원문항과 똑같았다. 대화를 새로 썼다.",
   p="A: Does Mina walk to school?\nB: No, she <u>don't walk</u> to school. She takes the bus.", okdup=True)

# 4-30 세 빈칸 동사 형태: 원문항 발문, C는 글을 새로
S430 = "발문이 ‘현재의 일반적 상태·반복 행동을 나타내려고 한다’고 시제를 알려 주었다. 원문항 발문으로 되돌렸다. 보기에는 현재형만 있어 발문 조건 없이도 정답은 하나다. 보기와 정답은 그대로다."
for t in "BDEF": F(4, 30, t, st="R", s=S430)
W430 = ["3인칭 단수 주어 My aunt에는 teaches를 쓴다", "3인칭 단수 주어 She에는 has를 쓴다", "복수 주어 Her students에는 동사원형 come을 쓴다"]
c430 = ["teaches - has - come", "teaches - have - come", "teach - has - comes", "teaches - has - comes", "teach - have - come"]
mk(4, 30, "C", [(x, slotnote(x, c430[0], W430, labs=("(A)", "(B)", "(C)"))) for x in c430], 1,
   "현재 시제에서 3인칭 단수 주어의 동사에는 -s/-es를 붙이고(teach → teaches, have → has), 복수 주어에는 동사원형을 쓴다.",
   "글과 정답(lives - has - visit)이 원문항과 거의 같았다. 글을 새로 썼다.", p="My aunt (A)________(teach) music. She (B)________(have) a piano at home. Her students (C)________(come) every Saturday.", okdup=True)


# ---- 2차 감수(2026-10) 추가 ----
# 4-26 B: 정답만 길고(for the presentation) 오답은 질문의 형태 오류, 정답 위치도 원문항과 같은 ④ → 원문항처럼 대답을 판별하게
FIX.pop((4, 26, "B"), None)
f426("B", [("Is Tom ready? - Yes, he are.", "he에는 is를 쓰므로"), ("Are you ready? - Yes, I am.", "you에 대한 질문에 I로 받아 바르게 답했으므로"), ("Are your friends ready? - No, they isn't.", "they에는 aren't를 쓰므로"),
           ("Is she ready? - Yes, she isn't.", "Yes 뒤에는 긍정(she is)이 와야 하므로"), ("Are we ready? - Yes, we is.", "we에는 are를 쓰므로")], 2,
     "발문에 조건이 붙었고, 정답 보기만 길어(for the presentation) 형태만으로 눈에 띄었으며, 오답은 대답이 아니라 질문의 형태가 틀린 것(Are Tom, Is they 등)이었고 정답 위치도 원문항과 같은 ④였다. 원문항 발문으로 되돌리고, 원문항처럼 대답의 인칭·형태를 판별하는 대화로 새로 썼다.")

# 4-27 E: 오답이 형태 오류뿐이고 after schools는 틀렸다고 하기 어려움 → 원문항처럼 의문사·진행형·과거 의문문 오답으로
f427("E", "Yes, they play soccer after school.", [("What do they play after school?", WH), ("Do they play soccer after school?", "복수 주어 + Do + 동사원형의 현재 의문문이므로"), ("Does they play soccer after school?", "주어 they에는 Do를 쓰므로"),
     ("Are they playing soccer now?", "진행형 질문에는 Yes, they are로 답하므로"), ("Did they play soccer yesterday?", "과거 질문에는 Yes, they did로 답하므로")], 2,
     "오답이 형태가 틀린 질문(Does they, Are they play, Do they plays)뿐이었고, ②(after schools)는 문법상 틀렸다고 하기 어려웠다. 원문항처럼 의문사 의문문·진행형·과거 의문문 같은 실제 형태의 질문을 오답으로 썼다.")

# 4-29 B: 없는 형태(studys) 오답 → 실제 형태로
mk(4, 29, "B", [("isn't study", "일반동사의 부정에 be동사를 쓸 수 없으므로"), ("doesn't study", "3인칭 단수 주어 she의 부정 doesn't + 동사원형으로 바르게 고쳤으므로"), ("doesn't studies", "doesn't 뒤에는 동사원형을 쓰므로"),
                ("don't study", "틀린 부분(don't)을 그대로 두었으므로"), ("doesn't studied", "doesn't 뒤에 과거형을 쓸 수 없으므로")], 2,
   "일반동사 현재 부정문은 3인칭 단수 주어에 doesn't + 동사원형, 그 밖의 주어에 don't + 동사원형을 쓴다.", "오답에 영어에 없는 형태(studys)가 있어 실제 형태(studies)로 바꿨다. 대화와 정답은 그대로다.")
