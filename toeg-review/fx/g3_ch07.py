import re
# 3급 CH7 의문사 의문문 (61~70) 수정 예시
import re

def jo(w, a, b):
    f = (ord(w[-1]) - 0xAC00) % 28 if "가" <= w[-1] <= "힣" else 0
    return b if f == 0 or (f == 8 and a == "으로") else a

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 3-61 대답에 맞는 질문: 형태는 모두 옳고 의문사만 다른 선택지
R61 = "의문사는 묻는 정보에 맞게 고른다: who(사람), what(사물·일), where(장소), when(때), why(이유), how(방법), how much(값·양), how long(기간). 일반동사 과거 의문문은 의문사 + did + 주어 + 동사원형이다."
S61 = "선택지 대부분이 같은 의문사의 형태 오류(did you went, do you go 등)여서 의문사 선택보다 did 의문문 형태를 묻게 됐다. 원문항처럼 형태는 모두 옳고 의문사만 다른 선택지 다섯 개로 바꿨다."
def f61(t, reply, items, a, s=S61):
    mk(3, 61, t, items, a, R61, s, p=f"A: ________________________\nB: {reply}")
f61("B", "I had lunch with my cousin.", [("Where did you have lunch?", "Where는 장소를 묻는데 B는 함께 먹은 사람을 말하므로"), ("What did you have for lunch?", "What은 먹은 음식을 묻는데 B는 함께 먹은 사람을 말하므로"),
     ("Who did you have lunch with?", "Who는 사람을 묻고 B가 함께 먹은 사람(my cousin)을 말하므로"), ("When did you have lunch?", "When은 때를 묻는데 B는 함께 먹은 사람을 말하므로"), ("How much did you pay for lunch?", "How much는 값을 묻는데 B는 함께 먹은 사람을 말하므로")], 3,
    "대답과 정답이 원문항과 똑같았고 선택지도 형태 오류 위주였다. 대답을 새로 쓰고 원문항처럼 의문사만 다른 선택지 다섯 개로 바꿨다.")
f61("C", "I went to Busan.", [("What did you eat last weekend?", "What은 먹은 것을 묻는데 B는 간 곳을 말하므로"), ("Where did you go last weekend?", "Where는 장소를 묻고 B가 간 곳(Busan)을 말하므로"), ("Who did you call last weekend?", "Who는 전화한 사람을 묻는데 B는 간 곳을 말하므로"),
     ("How long did you sleep last weekend?", "How long은 기간을 묻는데 B는 간 곳을 말하므로"), ("Why did you stay home last weekend?", "Why는 이유를 묻는데 B는 간 곳을 말하므로")], 2)
f61("D", "It cost thirty dollars.", [("Where did you buy the shirt?", "Where는 장소를 묻는데 B는 값을 말하므로"), ("When did you buy the shirt?", "When은 때를 묻는데 B는 값을 말하므로"), ("Who bought the shirt?", "Who는 산 사람을 묻는데 B는 값을 말하므로"),
     ("How much did the shirt cost?", "How much는 값을 묻고 B가 값(thirty dollars)을 말하므로"), ("Why did you buy the shirt?", "Why는 이유를 묻는데 B는 값을 말하므로")], 4)
f61("E", "I left at nine.", [("When did you leave the party?", "When은 때를 묻고 B가 떠난 시각(at nine)을 말하므로"), ("Why did you leave the party?", "Why는 이유를 묻는데 B는 떠난 시각을 말하므로"), ("Who did you leave with?", "Who는 함께 떠난 사람을 묻는데 B는 떠난 시각을 말하므로"),
     ("What did you bring to the party?", "What은 가져온 물건을 묻는데 B는 떠난 시각을 말하므로"), ("How many people came to the party?", "How many는 사람 수를 묻는데 B는 떠난 시각을 말하므로")], 1)
f61("F", "Because I was tired.", [("Where did you go after school?", "Where는 장소를 묻는데 B는 이유(Because ...)를 말하므로"), ("What did you do after school?", "What은 한 일을 묻는데 B는 이유를 말하므로"), ("When did you get home?", "When은 때를 묻는데 B는 이유를 말하므로"),
     ("Who took you home?", "Who는 데려다준 사람을 묻는데 B는 이유를 말하므로"), ("Why did you go home early?", "Why는 이유를 묻고 B가 Because로 이유를 말하므로")], 5)

# 3-62 어색한 대화: 유형마다 대화 다섯 개를 새로
R62 = "의문사가 묻는 정보(what 사물·일, who 사람, where 장소, when·what time 때, why 이유, how 방법·상태, how long 기간, how old 나이, how much 값)에 맞게 답해야 자연스러운 대화가 된다."
S62 = "오답 대화 네 개가 B와 똑같았다. 유형마다 대화 다섯 개를 새로 썼다."
OK62 = "묻는 정보에 맞게 답한 자연스러운 대화이므로"
def f62(t, items, a, s=S62):
    mk(3, 62, t, [(x, w or OK62) for x, w in items], a, R62, s)
f62("B", [("A: What do you want for dinner? B: I'd like some pasta.", ""), ("A: How long did the movie last? B: I watched it with my sister.", "How long은 기간을 묻는데 함께 본 사람을 답해 어색하므로"), ("A: Who is your favorite singer? B: I like IU the most.", ""),
          ("A: Where do you live? B: I live near the park.", ""), ("A: Why are you so happy? B: I passed the exam.", "")], 2,
    "어색한 대화(When is the meeting? - It's on the third floor.)가 원문항 정답과 똑같았다. 대화 다섯 개를 새로 쓰고 어색한 대화를 원문항과 다르게 했다.")
f62("C", [("A: How did you get here? B: I came by bus.", ""), ("A: When does the store open? B: It opens at nine.", ""), ("A: Whose bag is this? B: It's Mina's.", ""),
          ("A: How many brothers do you have? B: I have two.", ""), ("A: Why did you call me? B: At six o'clock.", "Why는 이유를 묻는데 시각을 답해 어색하므로")], 5)
f62("D", [("A: Where did you put my keys? B: Yesterday morning.", "Where는 장소를 묻는데 때를 답해 어색하므로"), ("A: What are you reading? B: A book about space.", ""), ("A: How tall is your brother? B: He's about 180 cm.", ""),
          ("A: When is your birthday? B: It's May 5th.", ""), ("A: Which color do you like, red or blue? B: I like blue.", "")], 1)
f62("E", [("A: How much is this cap? B: It's fifteen dollars.", ""), ("A: Who made this cake? B: My dad did.", ""), ("A: What time does the bus leave? B: At the bus stop.", "What time은 시각을 묻는데 장소를 답해 어색하므로"),
          ("A: How often do you go swimming? B: Once a week.", ""), ("A: Where is the nearest bank? B: It's next to the post office.", "")], 3)
f62("F", [("A: What's the weather like today? B: It's sunny and warm.", ""), ("A: When did you finish your homework? B: Just an hour ago.", ""), ("A: Who's that girl? B: She's my cousin.", ""),
          ("A: How old is your dog? B: It's brown and white.", "How old는 나이를 묻는데 색깔을 답해 어색하므로"), ("A: Why is Tom absent today? B: He has a cold.", "")], 4)

# 3-63 How many / How much: 유형마다 명사를 새로, 다른 하나의 종류도 바꿈
R63 = "How many + 셀 수 있는 명사의 복수형은 개수를, How much + 셀 수 없는 명사는 양을 묻는다. bread, salt, information, furniture, advice, paper, snow, luggage 등은 셀 수 없는 명사이다."
S63 = "셀 수 없는 명사 오답 네 문장(rice, time, money, water)이 B와 똑같았다. 유형마다 명사를 새로 썼다."
def MANY(w): return f"{w}: 셀 수 있는 명사의 복수형이라 many가 들어가므로"
def MUCH(w): return f"{w}: 셀 수 없는 명사라 much가 들어가므로"
def f63(t, items, a, s=S63):
    mk(3, 63, t, [(f"How _____ {x}", (w[:-2] + f"고, 나머지({'many' if 'much' in w else 'much'})와 달라") if i + 1 == a else w) for i, (x, w) in enumerate(items)], a, R63, s)
f63("B", [("pencils do you need?", MANY("pencils")), ("eggs are in the basket?", MANY("eggs")), ("juice did you drink?", MUCH("juice")), ("friends came to the party?", MANY("friends")), ("pages did you read?", MANY("pages"))], 3,
    "정답(How many cookies)이 원문항과 같았다. 문장을 새로 쓰고, many 넷 + much 하나로 바꿔 원문항과 반대로 짰다.")
f63("C", [("bread did you eat?", MUCH("bread")), ("salt should I add?", MUCH("salt")), ("information do you need?", MUCH("information")), ("tickets did you buy?", MANY("tickets")), ("furniture is in the room?", MUCH("furniture"))], 4)
f63("D", [("coffee do you drink a day?", MUCH("coffee")), ("paper do we need?", MUCH("paper")), ("advice did he give you?", MUCH("advice")), ("soup is in the pot?", MUCH("soup")), ("classes do you have today?", MANY("classes"))], 5)
f63("E", [("dogs does she have?", MANY("dogs")), ("snow fell last night?", MUCH("snow")), ("windows are in the house?", MANY("windows")), ("songs can you sing?", MANY("songs")), ("questions did he ask?", MANY("questions"))], 2,
    S63 + " many 넷 + much 하나로 짜서 다른 유형과 구성을 달리했다.")
f63("F", [("letters did you write?", MANY("letters")), ("oil do we need?", MUCH("oil")), ("cheese is on the pizza?", MUCH("cheese")), ("tea did you make?", MUCH("tea")), ("luggage do you have?", MUCH("luggage"))], 1)

# 3-64 What / How: 유형마다 문장을 새로
R64 = "How + 형용사·부사(long, heavy, often, well 등)는 ‘얼마나 ~’의 정도를 묻고, What + 명사(color, time, kind, size 등)는 ‘무슨 ~’를 묻는다."
S64 = "How 오답 네 문장(old, fast, far, tall)이 B와 똑같았다. 유형마다 문장을 새로 썼다."
def WH(w, ko): return f"{w}({ko}){jo(ko, '으로', '로')} 써야 해 What이 들어가"
def HW(w, ko): return f"{w}({ko}){jo(ko, '으로', '로')} 써야 해 How가 들어가"
def f64(t, items, a, s=S64):
    mk(3, 64, t, [(f"_____ {x}", w + ((f"고, 나머지({'What' if 'How가' in w else 'How'})와 달라") if i + 1 == a else "므로")) for i, (x, w) in enumerate(items)], a, R64, s)
f64("B", [("color is your bike?", WH("What color", "무슨 색")), ("long is the bridge?", HW("How long", "얼마나 긴")), ("kind of food do you like?", WH("What kind of", "어떤 종류의")),
          ("subject do you like best?", WH("What subject", "무슨 과목")), ("time does the class start?", WH("What time", "몇 시"))], 2,
    "정답(What size)이 원문항과 같았다. 문장을 새로 쓰고, What 넷 + How 하나로 바꿔 원문항과 반대로 짰다.")
f64("C", [("heavy is your bag?", HW("How heavy", "얼마나 무거운")), ("often does he cook?", HW("How often", "얼마나 자주")), ("deep is the lake?", HW("How deep", "얼마나 깊은")),
          ("many sisters do you have?", HW("How many", "몇 명의")), ("sport do you play?", WH("What sport", "무슨 운동"))], 5)
f64("D", [("language does she speak?", WH("What language", "무슨 언어")), ("season do you like?", WH("What season", "무슨 계절")), ("wide is the river?", HW("How wide", "얼마나 넓은")),
          ("grade are you in?", WH("What grade", "몇 학년")), ("animal is your favorite?", WH("What animal", "무슨 동물"))], 3, S64 + " What 넷 + How 하나로 짜서 다른 유형과 구성을 달리했다.")
f64("E", [("month is your birthday in?", WH("What month", "몇 월")), ("hot is it outside?", HW("How hot", "얼마나 더운")), ("much is this shirt?", HW("How much", "얼마")),
          ("early did you get up?", HW("How early", "얼마나 일찍")), ("high is the mountain?", HW("How high", "얼마나 높은"))], 1)
f64("F", [("movie did you watch?", WH("What movie", "무슨 영화")), ("floor do you live on?", WH("What floor", "몇 층")), ("song are you listening to?", WH("What song", "무슨 노래")),
          ("well does she swim?", HW("How well", "얼마나 잘")), ("team won the game?", WH("What team", "어느 팀"))], 4, S64 + " What 넷 + How 하나로 짜서 다른 유형과 구성을 달리했다.")

# 3-65 (A)·(B): 원문항 발문과 형식(ⓐ·ⓑ, 설명문)
ST65 = "빈칸 (A)와 (B)에 들어갈 말을 바르게 짝지은 것은?"
R65 = "과거 be동사는 주어가 I·3인칭 단수면 was, you·복수면 were를 쓴다. 의문문을 만드는 조동사 did 뒤에는 동사원형을 쓴다."
S65 = "보기 기호 ⓐ·ⓑ가 a·b로 바뀌고 발문과 설명 문구도 원문항과 달랐다. 원문항 발문과 형식(ⓐ·ⓑ, 밑줄 빈칸 (A)·(B)가 있는 설명문)으로 되돌렸다. 보기와 정답은 그대로다."
def n65(x, A, subj):
    a, b = [y.strip() for y in re.findall(r"\([AB]\) ([^,]+)", x)]
    if a == A and b == "동사원형": return f"(A) {a}는 주어 {subj}에 맞는 과거 be동사이고, (B) did 뒤에는 동사원형을 쓰므로"
    bits = []
    if a != A: bits.append(f"(A) {a}: " + ("현재형이라 과거 문장에 맞지 않는다" if a in ("is", "are") else "be동사 원형은 쓸 수 없다" if a == "be" else f"주어 {subj}에는 {A}를 쓴다"))
    if b != "동사원형": bits.append(f"(B) {b}: did 뒤에는 동사원형을 쓴다")
    return ", ".join(bits) + ". 따라서"
def f65(t, s1, s2, subj_sent, fix_sent, A, subj, s=S65, **kw):
    p = f"ⓐ {s1}\nⓑ {s2}\n문장 ⓐ에서 주어인 {subj_sent} be동사의 과거형 (<u>    A    </u>)를 써야 한다. 문장 ⓑ에서 의문문을 만들기 위해 사용된 조동사 'did' 뒤에는 (<u>    B    </u>)를 써야 하므로 {fix_sent} 고쳐야 한다."
    c = kw.pop("c", V(3, 65, t)["c"]); a = kw.pop("a", int(V(3, 65, t)["ans"]))
    mk(3, 65, t, [(x, n65(x, A, subj)) for x in c], a, R65, s, st=ST65, p=p, okdup=True, **kw)
f65("B", "Where were your sister last night?", "What did he said to you?", "'your sister'는 3인칭 단수이므로", "'said'를 'say'로", "was", "your sister",
    s="제시문과 정답이 원문항과 똑같았다. 두 문장을 새로 쓰고(정답 was) 원문항 발문과 형식으로 되돌렸다.",
    c=["(A) were, (B) 동사원형", "(A) is, (B) 동사원형", "(A) was, (B) 과거형", "(A) was, (B) 동사원형", "(A) are, (B) 현재분사"], a=4)
f65("C", "Where was they yesterday?", "What did she bought?", "'they'는 3인칭 복수이므로", "'bought'를 'buy'로", "were", "they")
f65("D", "How were Tom yesterday?", "When did he came?", "'Tom'은 3인칭 단수이므로", "'came'을 'come'으로", "was", "Tom")
f65("E", "Why was we so tired?", "Where did they saw him?", "'we'는 1인칭 복수이므로", "'saw'를 'see'로", "were", "we")
f65("F", "Where were Jane yesterday?", "What did Tom ate?", "'Jane'은 3인칭 단수이므로", "'ate'를 'eat'으로", "was", "Jane")

# 3-66 B: 원문항과 같던 제시문을 새로
F(3, 66, "B", p="How ______ milk do you drink every day?", xr=[(x, "milk") for x in ["money"] if x in V(3, 66, "B")["expl"]],
  s="제시문(How ___ money do you have in your wallet?)과 정답이 원문항과 똑같았다. 제시문을 ‘How ___ milk do you drink every day?’로 바꿨다. 보기와 정답(much)은 그대로다.")

# 3-67 의문사 + will 의문문 어순: 원문항 발문, 발문 조건 없이도 틀린 오답으로
ST67 = "다음 문장에서 어법상 틀린 부분을 찾아 바르게 고친 문장을 고르시오."
R67 = "will이 있는 의문사 의문문은 의문사 + will + 주어 + 동사원형 순서로 만든다. do나 be를 따로 덧붙이지 않고, will 뒤에는 동사원형을 쓴다."
S67 = "발문이 ‘will과 나머지 표현을 유지하면서 의문사를 맨 앞에 둔 기본 의문문 어순으로’라고 고치는 방법을 알려 주었다. 원문항 발문으로 되돌리고, 그 조건이 없으면 옳은 문장이 되는 오답(do를 쓴 현재 의문문)은 do와 will을 함께 쓴 틀린 문장으로 바꿨다."
OK67 = "의문사 + will + 주어 + 동사원형 어순으로 바르게 고쳤으므로"
KEEP = "틀린 어순(의문사 + 주어 + will)을 그대로 두었으므로"
WW = "will이 의문사 앞에 와서 어순이 틀렸으므로"
WB = "will 뒤에 be를 덧붙여 틀렸으므로"
DW = "will이 있는 의문문에 do를 덧붙일 수 없으므로"
def f67(t, p, items, a, s=S67):
    mk(3, 67, t, items, a, R67, s, st=ST67, p=p)
f67("B", "What time you will arrive at the station?", [("What time do you will arrive at the station?", DW), ("What time will you arrive at the station?", OK67), ("What time you will arrive at the station?", KEEP),
     ("What time will arrive you at the station?", "주어 you가 동사 뒤로 가서 어순이 틀렸으므로"), ("What time will you arrives at the station?", "will 뒤에는 동사원형(arrive)을 쓰므로")], 2,
    "제시문과 정답이 원문항과 똑같았고 발문도 고치는 방법을 알려 주었다. 제시문을 새로 쓰고 원문항 발문으로 되돌렸다.")
f67("C", "What she will buy?", [("What does she will buy?", DW), ("What will be she buy?", WB), ("Will what she buy?", WW), ("What will she buy?", OK67), ("What she will buy?", KEEP)], 4)
f67("D", "When they will leave?", [("When do they will leave?", DW), ("When will be they leave?", WB), ("Will when they leave?", WW), ("When they will leave?", KEEP), ("When will they leave?", OK67)], 5)
f67("E", "Why Tom will go there?", [("Why will Tom go there?", OK67), ("Why Tom will go there?", KEEP), ("Will why Tom go there?", WW), ("Why will be Tom go there?", WB), ("Why does Tom will go there?", DW)], 1)
f67("F", "How we will get home?", [("Will how we get home?", WW), ("How do we will get home?", DW), ("How we will get home?", KEEP), ("How will be we get home?", WB), ("How will we get home?", OK67)], 5)

# 3-68 B: 원문항과 같던 제시문을 새로
F(3, 68, "B", p="너는 어떻게 그 소식을 들었니?\n(how / hear / the news / did / you / ?)", c=["How did you heard the news?", "Did how you hear the news?", "What did you hear the news?", "How did you hear the news?", "How you did hear the news?"], a=4,
  r="의문사 의문문은 의문사 + did + 주어 + 동사원형 순서로 만든다. ‘어떻게’는 how로 묻는다.",
  n=["did 뒤에는 동사원형(hear)을 쓰고, 주어진 단어도 hear이므로 오답이다.", "의문사 how가 맨 앞에 와야 하므로 오답이다.", "‘어떻게’는 what이 아니라 how로 물으므로 오답이다.", "How + did + you + hear 순서로 바르게 배열했으므로 정답이다.", "did가 주어 you 앞에 와야 하므로 오답이다."],
  s="제시문과 정답이 원문항과 똑같았다. 제시문을 ‘너는 어떻게 그 소식을 들었니?’로 바꾸고 선택지를 새로 썼다. 정답 위치 ④.")

# 3-69 B: 네 문장과 정답이 원문항과 같아 새로
F(3, 69, "B", p="ⓐ 이 다리는 얼마나 넓니?\n→ _____ _____ is the bridge?\nⓑ 너의 형은 키가 얼마나 크니?\n→ _____ _____ is your brother?\nⓒ 너는 얼마나 일찍 일어나니?\n→ _____ _____ do you get up?\nⓓ 이 상자는 얼마나 무겁니?\n→ _____ _____ is the box?",
  c=["How tall", "How wide", "How long", "How early", "How heavy"], a=3, r="How + 형용사·부사는 정도를 묻는다: How wide(얼마나 넓은), How tall(얼마나 키가 큰), How early(얼마나 일찍), How heavy(얼마나 무거운), How long(얼마나 긴·오래).",
  n=["ⓑ(키가 얼마나 크니)에 쓰이므로 오답이다.", "ⓐ(얼마나 넓니)에 쓰이므로 오답이다.", "‘얼마나 긴·오래’를 묻는 문장이 없어 쓰이지 않으므로 정답이다.", "ⓒ(얼마나 일찍)에 쓰이므로 오답이다.", "ⓓ(얼마나 무겁니)에 쓰이므로 오답이다."], okdup=True,
  s="네 문장과 정답(How old)이 원문항과 같았다. 문장을 새로 쓰고 원문항처럼 줄마다 나누었다. 정답 위치 ③.")

# 3-70 글 읽고 우리말에 맞는 질문: 원문항처럼 네 문장 글
R70 = "우리말 질문이 묻는 정보에 맞는 의문사를 고른다: where(어디), what(무엇), how long(얼마나 오래), why(왜), which(어느·어떤). 일반동사 과거 의문문은 의문사 + did + 주어 + 동사원형으로 만든다."
S70 = "제시문이 한 문장으로 줄어 원문항(한 단락 글)과 형식·읽기 부담이 달랐다. 원문항처럼 네 문장 글로 새로 쓰고, 질문 보기도 원문항처럼 물음표 없이 제시했다."
def f70(t, story, ko, ans_line, items, a, s=S70):
    mk(3, 70, t, items, a, R70, s, p=f"{story}\nQ: ________________________?\n({ko})\nA: {ans_line}")
def NO(w, ko): return f"{w}({ko}){jo(ko, '을', '를')} 묻는 질문이라 우리말 해석과 맞지 않으므로"
f70("B", "Last Saturday, our class went on a field trip to the science museum. We saw many robots and watched a movie about space. Minho lost his cap on the bus, but the driver found it. Everyone had a great time.",
    "너희 반은 어디로 현장 학습을 갔니?", "We went to the science museum.",
    [("When did your class go on the field trip", NO("When", "때")), ("Where did your class go on the field trip", "Where(어디)로 현장 학습 장소를 물어 우리말 해석과 맞으므로"), ("What did Minho lose", NO("What", "잃어버린 물건")),
     ("Who found Minho's cap", NO("Who", "찾아 준 사람")), ("How did your class get there", NO("How", "가는 방법"))], 2,
    "글·질문·정답(What caused the accident)이 원문항과 같았고 글도 한 문장으로 줄었다. 원문항처럼 네 문장 글을 새로 쓰고 질문을 바꿨다.")
f70("C", "My grandmother's birthday was yesterday. My family made a cake for her in the morning. In the evening, we had dinner at a Chinese restaurant. She was very happy with our gift, a warm scarf.",
    "너희 가족은 할머니께 무엇을 선물했니?", "We gave her a warm scarf.",
    [("When was your grandmother's birthday", NO("When", "때")), ("Where did your family have dinner", NO("Where", "장소")), ("Who made the cake", NO("Who", "만든 사람")),
     ("Why was your grandmother happy", NO("Why", "이유")), ("What did your family give your grandmother", "What(무엇)으로 선물을 물어 우리말 해석과 맞으므로")], 5)
f70("D", "Jisu practiced the piano for three hours yesterday. She has a big contest next week. Her teacher said her playing was getting better. Jisu hopes to win first prize.",
    "지수는 어제 얼마나 오래 피아노를 연습했니?", "She practiced for three hours.",
    [("How long did Jisu practice the piano yesterday", "How long(얼마나 오래)로 연습 시간을 물어 우리말 해석과 맞으므로"), ("When is Jisu's contest", NO("When", "대회 날짜")), ("What did her teacher say", NO("What", "선생님이 한 말")),
     ("Why did Jisu practice the piano", NO("Why", "이유")), ("Who wants to win first prize", NO("Who", "사람"))], 1)
f70("E", "Tom was late for school this morning. He missed the bus because his alarm clock didn't ring. He ran all the way to school. His teacher told him to buy a new clock.",
    "Tom은 왜 버스를 놓쳤니?", "Because his alarm clock didn't ring.",
    [("When did Tom get to school", NO("When", "때")), ("How did Tom get to school", NO("How", "방법")), ("Why did Tom miss the bus", "Why(왜)로 버스를 놓친 이유를 물어 우리말 해석과 맞으므로"),
     ("Who told Tom to buy a clock", NO("Who", "사람")), ("Where did Tom run", NO("Where", "장소"))], 3)
f70("F", "Mina and her brother visited the zoo on Sunday. They saw lions, elephants, and a baby giraffe. Mina liked the baby giraffe the most. They took many pictures of it.",
    "미나는 어떤 동물을 가장 좋아했니?", "She liked the baby giraffe the most.",
    [("When did Mina visit the zoo", NO("When", "때")), ("Who went to the zoo with Mina", NO("Who", "함께 간 사람")), ("Where did Mina go on Sunday", NO("Where", "장소")),
     ("Which animal did Mina like the most", "Which animal(어떤 동물)로 가장 좋아한 동물을 물어 우리말 해석과 맞으므로"), ("How many animals did they see", NO("How many", "동물 수"))], 4)

# ---- 2차 감수(2026-10) 추가 ----
# 3-68 B~F: 제시어에 없는 낱말(What, does/do 바꿔치기, heard)이 든 오답 → 원문항처럼 제시어만 순서를 바꾼 오답으로
R68 = "의문사가 있는 일반동사 의문문은 ‘의문사 + do/does/did + 주어 + 동사원형 ~?’ 순서다."
S68 = "오답에 제시어에 없는 낱말(What, 다른 형태의 do/does 등)이 섞여 낱말만 대조해도 지워졌다. 원문항처럼 주어진 낱말의 순서만 바꾼 오답으로 다시 썼다."
def f68(t, wh, aux, subj, rest, a, order, s=S68):
    FIX.pop((3, 68, t), None)
    v, tail = rest.split(" ", 1)
    forms = {"ok": (f"How {aux} {subj} {v} {tail}?", f"How + {aux} + 주어 + 동사원형 순서로 바르게 배열했으므로"),
             "sa": (f"How {subj} {aux} {v} {tail}?", f"{aux}가 주어({subj}) 앞에 와야 하므로"),
             "vs": (f"How {aux} {v} {subj} {tail}?", f"주어({subj})가 동사({v}) 앞에 와야 하므로"),
             "end": (f"How {subj} {v} {tail} {aux}?", f"{aux}가 문장 끝에 놓여 의문문 어순이 아니므로"),
             "front": (f"{aux.capitalize()} how {subj} {v} {tail}?", "의문사 How가 문장 맨 앞에 와야 하므로")}
    kw = {"p": wh} if wh else {}
    mk(3, 68, t, [forms[k] for k in order], a, R68, s, **kw)
f68("B", "너는 어떻게 그 소식을 들었니?\n(how / hear / the news / did / you / ?)", "did", "you", "hear the news", 4, ["sa", "vs", "front", "ok", "end"],
    "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘너는 어떻게 그 소식을 들었니?’로 바꾸고, 원문항처럼 주어진 낱말의 순서만 바꾼 보기로 썼다.")
f68("C", None, "does", "she", "study English", 1, ["ok", "front", "sa", "vs", "end"])
f68("D", None, "do", "they", "get home", 1, ["ok", "vs", "end", "front", "sa"])
f68("E", None, "does", "Tom", "get to work", 2, ["sa", "ok", "vs", "end", "front"])
f68("F", None, "do", "we", "get there", 3, ["end", "sa", "ok", "vs", "front"])
# 3-69 C~F: 원문항처럼 우리말과 영어를 줄을 나누고 빈칸을 두 칸으로
for t in "CDEF":
    lines = []
    for ln in V(3, 69, t)["passage"].split("\n"):
        ko, en = ln.split(" → ")
        lines += [ko, "→ " + en.replace("_____", "_____ _____", 1)]
    F(3, 69, t, p="\n".join(lines), okdup=True, s="우리말과 영어 문장이 한 줄에 이어져 있고 빈칸이 한 칸이라, 원문항처럼 줄을 나누고 빈칸을 두 칸(_____ _____)으로 했다. 문장·보기·정답은 그대로다.")
