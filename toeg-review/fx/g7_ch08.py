# 7급 CH8 의문사 의문문 (71~80) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
R_WH = "Who는 사람, What은 사물·일, Where는 장소, When은 때, Why는 이유를 묻는다. 의문사 뒤에는 be동사나 do/does를 주어에 맞춰 쓴다."

# 7-71 의문사 빈칸: 정답을 알려 주는 상황 설명 삭제
S771 = "대화 아래에 ‘○○를 묻는 상황입니다’처럼 정답 의문사의 뜻을 적어 대답을 읽지 않아도 답이 나왔다. 원문항처럼 대화만 제시하도록 상황 설명을 지웠다. 보기와 정답은 그대로다."
WH = {"Who": "사람을 묻는 의문사", "What": "사물·일을 묻는 의문사", "Where": "장소를 묻는 의문사", "When": "때를 묻는 의문사", "Why": "이유를 묻는 의문사"}
def f771(t, ans_why):
    V_ = V(7, 71, t); a = int(V_["ans"]); p = "\n".join(V_["passage"].split("\n")[:2])
    items = [(o, f"{WH[o]}라 " + (ans_why.replace("말하므로", "말해 알맞으므로") if i + 1 == a else "대답과 맞지 않으므로")) for i, o in enumerate(V_["c"])]
    mk(7, 71, t, items, a, R_WH, S771, p=p)
f771("B", "대답(I lost my book.)이 슬픈 이유를 말하므로"); f771("C", "대답(On your desk.)이 장소를 말하므로"); f771("D", "대답(It is a pencil.)이 물건을 말하므로")
f771("E", "대답(It is on the chair.)이 장소를 말하므로"); f771("F", "대답(It is in May.)이 때를 말하므로")

# 7-73 What + 대답 동사: 원문항 발문과 문장별 우리말
S773 = "발문이 ‘무엇인지 묻고, 질문의 동사를 반복하여 현재형으로 직접 대답’이라고 두 빈칸의 정답 형태를 알려 주었고 원문항의 우리말 해석이 빠졌다. 원문항 발문으로 되돌리고 우리말 해석을 붙였다. 보기와 정답은 그대로다."
def f773(t, p, good, why):
    V_ = V(7, 73, t); gs = [x.strip() for x in good.split(" - ")]; items = []
    for ch in V_["c"]:
        xs = [x.strip() for x in ch.split(" - ")]
        if xs == gs: items.append((ch, "‘무엇’을 묻는 What과 주어에 맞는 현재형을 바르게 짝지었으므로")); continue
        bits = [f"{['첫째', '둘째'][i]} 빈칸 {x}: {why[i]}" for i, (x, g) in enumerate(zip(xs, gs)) if x != g]
        items.append((ch, ". ".join(bits) + ". 따라서"))
    mk(7, 73, t, items, int(V_["ans"]), R_WH, S773, st="R", p=p, okdup=True)
W1 = "‘무엇을’ 묻는 말이라 What을 쓴다"
f773("B", "A: _______ do they want? (그들은 무엇을 원하니?)\nB: They _______ water. (그들은 물을 원해.)", "What - want", [W1, "주어 They에는 동사원형 want를 쓴다"])
f773("C", "A: _______ does Tom eat? (Tom은 무엇을 먹니?)\nB: He _______ rice. (그는 밥을 먹어.)", "What - eats", [W1, "3인칭 단수 주어 He에는 eats를 쓴다"])
f773("D", "A: _______ does Tom need? (Tom은 무엇이 필요하니?)\nB: He _______ a pencil. (그는 연필이 필요해.)", "What - needs", [W1, "3인칭 단수 주어 He에는 needs를 쓴다"])
f773("E", "A: _______ do you read? (너는 무엇을 읽니?)\nB: I _______ books. (나는 책을 읽어.)", "What - read", [W1, "주어 I에는 동사원형 read를 쓴다"])
f773("F", "A: _______ does he play? (그는 무엇을 하니?)\nB: He _______ soccer. (그는 축구를 해.)", "What - plays", [W1, "3인칭 단수 주어 He에는 plays를 쓴다"])

# 7-74 밑줄 be동사: 원문항 발문과 밑줄, 짝 없이 새 문장
R774 = "의문사 의문문의 be동사는 뒤에 오는 주어에 맞춘다. 3인칭 단수(it, she, the hat)에는 is, you·복수(they, the shoes)에는 are를 쓴다."
S774 = "옳은 오답 세 개가 원문항 선택지 그대로였고, 정답과 같은 문장의 옳은 형태가 함께 있었으며 밑줄도 사라졌다. 원문항 발문과 밑줄로 되돌리고 짝 없이 유형마다 새로 썼다."
OK74 = lambda s_: f"주어({s_})에 맞는 be동사를 바르게 썼으므로"
def f774(t, items, a, s=S774):
    mk(7, 74, t, items, a, R774, s, st="R")
f774("B", [("How tall <u>is</u> your father?", OK74("your father")), ("How old <u>are</u> she?", "3인칭 단수 주어 she에는 are가 아니라 is를 써야 하므로"), ("Where <u>is</u> your school?", OK74("your school")), ("What <u>is</u> your name?", OK74("your name")), ("Who <u>are</u> those boys?", OK74("those boys"))], 2)
f774("C", [("When <u>is</u> your birthday?", OK74("your birthday")), ("Where <u>are</u> my socks?", OK74("my socks")), ("What day <u>are</u> it?", "주어 it에는 are가 아니라 is를 써야 하므로"), ("How <u>are</u> you?", OK74("you")), ("Who <u>is</u> that girl?", OK74("that girl"))], 3)
f774("D", [("What time <u>is</u> it?", OK74("it")), ("How old <u>are</u> your sister?", "3인칭 단수 주어 your sister에는 are가 아니라 is를 써야 하므로"), ("What color <u>are</u> the shoes?", OK74("the shoes")), ("How old <u>are</u> the twins?", OK74("the twins")), ("Where <u>is</u> Mina?", OK74("Mina"))], 2,
     "밑줄이 사라지고 발문이 원문항과 달랐다. 원문항 발문과 be동사 밑줄로 되돌렸다. 보기와 정답은 그대로다.")
f774("E", [("Where <u>is</u> the station?", OK74("the station")), ("Who <u>are</u> your friends?", OK74("your friends")), ("How much <u>is</u> this pen?", OK74("this pen")), ("What color <u>are</u> the hat?", "단수 주어 the hat에는 are가 아니라 is를 써야 하므로"), ("What <u>are</u> these?", OK74("these"))], 4)
f774("F", [("What time <u>are</u> it?", "주어 it에는 are가 아니라 is를 써야 하므로"), ("Where <u>are</u> the keys?", OK74("the keys")), ("How tall <u>is</u> the tree?", OK74("the tree")), ("Who <u>is</u> your teacher?", OK74("your teacher")), ("What <u>is</u> in the box?", "단수로 받는 What 뒤에 is를 바르게 썼으므로")], 1)

# 7-75 어색한 대화: 옳은 대화를 원문항과 다르게
R775 = "질문의 의문사가 묻는 정보(나이, 요일, 시각, 날씨, 장소, 직업 등)에 맞게 답했는지 확인한다."
S775 = "옳은 대화 서너 개가 원문항 그대로였다. 유형마다 옳은 대화를 새로 썼다."
def f775(t, items, a, s=S775):
    mk(7, 75, t, items, a, R775, s)
f775("B", [("A: Where is the cat? - B: It's under the bed.", "장소를 묻는 질문에 장소로 알맞게 답했으므로"), ("A: How old is your sister? - B: She is nine.", "나이를 묻는 질문에 나이로 알맞게 답했으므로"), ("A: What color is your bag? - B: It's blue.", "색을 묻는 질문에 색으로 알맞게 답했으므로"),
           ("A: How old is she? - B: It is Monday.", "나이를 묻는데 요일로 답했으므로"), ("A: Who is he? - B: He is my uncle.", "누구인지 묻는 질문에 알맞게 답했으므로")], 4)
f775("C", [("A: What day is it? - B: It is three o'clock.", "요일을 묻는데 시각으로 답했으므로"), ("A: How are you? - B: I'm fine, thanks.", "안부를 묻는 질문에 알맞게 답했으므로"), ("A: Where do you live? - B: I live in Seoul.", "사는 곳을 묻는 질문에 장소로 알맞게 답했으므로"),
           ("A: What is your name? - B: My name is Jiho.", "이름을 묻는 질문에 알맞게 답했으므로"), ("A: When is your birthday? - B: It's in June.", "때를 묻는 질문에 달로 알맞게 답했으므로")], 1)
f775("E", [("A: Who is that boy? - B: He is my brother.", "누구인지 묻는 질문에 알맞게 답했으므로"), ("A: What time is it now? - B: It's half past two.", "시각을 묻는 질문에 시각으로 알맞게 답했으므로"), ("A: How much is it? - B: It's five dollars.", "값을 묻는 질문에 값으로 알맞게 답했으므로"),
           ("A: What do you like? - B: I like cats.", "좋아하는 것을 묻는 질문에 알맞게 답했으므로"), ("A: Where is your bag? - B: I am ten.", "가방의 위치를 묻는데 나이로 답했으므로")], 5)
f775("F", [("A: How is your mom? - B: She is fine.", "안부를 묻는 질문에 알맞게 답했으므로"), ("A: What day is it today? - B: It's Tuesday.", "요일을 묻는 질문에 요일로 알맞게 답했으므로"), ("A: What time is it? - B: It is sunny.", "시각을 묻는데 날씨로 답했으므로"),
           ("A: Where is the park? - B: It's near my house.", "장소를 묻는 질문에 장소로 알맞게 답했으므로"), ("A: What does she do? - B: She is a nurse.", "직업을 묻는 질문에 직업으로 알맞게 답했으므로")], 3)

# 7-78 are가 들어가는 문장: 원문항 발문, 오답을 원문항과 다르게
R778 = "의문사 뒤 빈칸의 be동사는 뒤에 오는 주어에 맞춘다. 3인칭 단수 주어에는 is, you·복수 주어에는 are를 쓴다."
S778 = "오답 네 개(your cat, Eddie, it, she)가 원문항 선택지 그대로였고 발문에 ‘현재형’이 붙었다. 원문항 발문으로 되돌리고 오답을 유형마다 새로 썼다."
IS_ = lambda s_: f"주어({s_})가 3인칭 단수라 is가 들어가므로"; ARE = lambda s_: f"주어({s_})가 you·복수라 are가 들어가므로"
def f778(t, items, a, s=S778):
    mk(7, 78, t, items, a, R778, s, st="R")
f778("B", [("How tall _______ your brother?", IS_("your brother")), ("Where _______ the bus stop?", IS_("the bus stop")), ("How old _______ the boys?", ARE("the boys")), ("What _______ your name?", IS_("your name")), ("Who _______ that man?", IS_("that man"))], 3)
f778("C", [("Where _______ you?", ARE("you")), ("How nice _______ she?", IS_("she")), ("How nice _______ it?", IS_("it")), ("How nice _______ your cat?", IS_("your cat")), ("How nice _______ Eddie?", IS_("Eddie"))], 1, "발문에 ‘현재형’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f778("D", [("What _______ these?", ARE("these")), ("How much _______ this cap?", IS_("this cap")), ("Where _______ Tom?", IS_("Tom")), ("What color _______ the sky?", IS_("the sky")), ("Who _______ she?", IS_("she"))], 1)
f778("E", [("Where _______ the library?", IS_("the library")), ("How old _______ your grandpa?", IS_("your grandpa")), ("What time _______ it?", IS_("it")), ("Who _______ he?", IS_("he")), ("What color _______ the books?", ARE("the books"))], 5)
f778("F", [("Where _______ Tom?", IS_("Tom")), ("Where _______ the children?", ARE("the children")), ("How old _______ your cat?", IS_("your cat")), ("What color _______ the bag?", IS_("the bag")), ("How old _______ she?", IS_("she"))], 2, "발문에 ‘현재형’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 7-79 글 속 밑줄: 원문항처럼 짧은 글에 ①~⑤ 밑줄, C~F는 글을 새로
ST779 = "다음 지문을 읽고 밑줄 친 ①~⑤ 중 문법적으로 틀린 것을 고르세요."
R779 = "What 의문문은 What + do/does + 주어 + 동사원형 ~?으로, 대답은 주어에 맞는 현재형으로 쓴다. 3인칭 단수 주어에는 does와 -s형, 그 밖의 주어에는 do와 동사원형을 쓴다."
def f779(t, text, why, a, s):
    parts = re.findall(r"[①-⑤]<u>(.*?)</u>", text)
    F(7, 79, t, st=ST779, p=text, c=parts, a=a, r=R779, n=[w + (" 정답이다." if i + 1 == a else " 오답이다.") for i, w in enumerate(why)], okdup=True, s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
S779 = "글의 ①~④ 문장이 원문항과 똑같고 ⑤만 바꿨으며, 밑줄이 사라지고 발문도 달랐다. 원문항처럼 짧은 글에 ①~⑤ 밑줄을 두고 글을 새로 썼다. 발문은 원문항의 표기 오류(ⓐ~ⓔ)를 바로잡아 ①~⑤로 썼다."
f779("B", "Hi, Jiho! ①<u>What do you read</u>? ②<u>I read comic books</u>. ③<u>What does Mina draw</u>? ④<u>She draws flowers</u>. ⑤<u>What does they play</u>? They play badminton.",
     ["주어 you에 do와 동사원형 read를 바르게 썼으므로", "주어 I에 동사원형 read를 바르게 썼으므로", "3인칭 단수 주어 Mina에 does와 동사원형 draw를 바르게 썼으므로", "3인칭 단수 주어 She에 draws를 바르게 썼으므로", "주어 they에는 does가 아니라 do를 써야 하므로"], 5,
     "밑줄이 사라지고 선택지에 문장을 다시 적었으며 발문도 달랐다. 원문항처럼 짧은 글에 ①~⑤ 밑줄을 되살렸다. 발문은 원문항의 표기 오류(ⓐ~ⓔ)를 바로잡아 ①~⑤로 썼다. 정답은 그대로다.")
f779("C", "Good morning, Mina! ①<u>What do you eat for breakfast</u>? ②<u>I eat toast</u>. ③<u>What does your brother drink</u>? ④<u>He drink milk</u>. ⑤<u>What do your parents eat</u>? They eat rice.",
     ["주어 you에 do와 동사원형 eat을 바르게 썼으므로", "주어 I에 동사원형 eat을 바르게 썼으므로", "3인칭 단수 주어 your brother에 does와 동사원형 drink를 바르게 썼으므로", "3인칭 단수 주어 He에는 drinks를 써야 하므로", "복수 주어 your parents에 do와 동사원형 eat을 바르게 썼으므로"], 4, S779)
f779("D", "Look at the club list. ①<u>What does Tom do</u>? ②<u>He play the guitar</u>. ③<u>What do Jane and Amy do</u>? ④<u>They dance</u>. ⑤<u>What do you do</u>? I sing songs.",
     ["3인칭 단수 주어 Tom에 does와 동사원형 do를 바르게 썼으므로", "3인칭 단수 주어 He에는 plays를 써야 하므로", "복수 주어 Jane and Amy에 do를 바르게 썼으므로", "주어 They에 동사원형 dance를 바르게 썼으므로", "주어 you에 do와 동사원형 do를 바르게 썼으므로"], 2, S779)
f779("E", "Hello, Leo! ①<u>What does your dog eat</u>? ②<u>It eats meat</u>. ③<u>What do your cat eat</u>? ④<u>It eats fish</u>. ⑤<u>What do your birds eat</u>? They eat seeds.",
     ["3인칭 단수 주어 your dog에 does와 동사원형 eat을 바르게 썼으므로", "주어 It에 eats를 바르게 썼으므로", "3인칭 단수 주어 your cat에는 do가 아니라 does를 써야 하므로", "주어 It에 eats를 바르게 썼으므로", "복수 주어 your birds에 do와 동사원형 eat을 바르게 썼으므로"], 3, S779)
f779("F", "Hi, Sora! ①<u>What do your mom teach</u>? ②<u>She teaches math</u>. ③<u>What do your sisters study</u>? ④<u>They study art</u>. ⑤<u>What do you like</u>? I like music.",
     ["3인칭 단수 주어 your mom에는 do가 아니라 does를 써야 하므로", "3인칭 단수 주어 She에 teaches를 바르게 썼으므로", "복수 주어 your sisters에 do와 동사원형 study를 바르게 썼으므로", "주어 They에 동사원형 study를 바르게 썼으므로", "주어 you에 do와 동사원형 like를 바르게 썼으므로"], 1, S779)

# 7-80 is/are를 쓴 이유: 원문항 발문, C~E는 그럴듯한 오해로 오답 새로
R780 = "의문사 의문문에서 be동사는 의문사나 질문의 종류가 아니라 뒤에 오는 주어에 맞춘다. 3인칭 단수 주어에는 is, 복수 주어에는 are를 쓴다."
ST_IS = "다음 문장에서 동사로 are이 아닌 is를 쓴 이유를 가장 잘 설명한 것은?"; ST_ARE = "다음 문장에서 동사로 is가 아닌 are를 쓴 이유를 가장 잘 설명한 것은?"
def f780(t, st, items, a, s):
    mk(7, 80, t, items, a, R780, s, st=st)
F(7, 80, "B", st=ST_IS, r=R780, n=["주어 the bag은 음식이 아니고, 음식 이름이라고 is를 쓰는 것도 아니므로 오답이다.", "가격을 묻는 질문이 아니고, 가격을 물어도 주어에 따라 be동사가 달라지므로 오답이다.", "문장의 길이는 be동사를 정하지 않으므로 오답이다.", "주어 the bag이 3인칭 단수라 is를 쓰므로 정답이다.", "의문사 뒤에도 복수 주어면 are를 쓰므로 오답이다."],
  s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
S780 = "오답 네 개가 B와 똑같았다. 원문항처럼 의문사, 질문의 종류, 단어의 뜻에 관한 그럴듯한 오해로 유형마다 오답을 새로 썼다."
f780("C", ST_IS, [("주어 Tom이 3인칭 단수이므로 is를 써야 한다.", "3인칭 단수 주어에는 is를 쓰므로"), ("'How old' 뒤에는 무조건 is만 올 수 있기 때문이다.", "How old 뒤에도 복수 주어면 are를 쓰므로"), ("Tom이 남자 이름이라 is를 쓰기 때문이다.", "성별은 be동사를 정하지 않으므로"),
     ("나이를 묻는 질문에서는 주어와 상관없이 is를 쓰기 때문이다.", "나이를 물어도 주어가 복수면 are를 쓰므로"), ("old가 형용사라서 형용사 앞에는 is를 쓰기 때문이다.", "뒤의 형용사는 be동사를 정하지 않으므로")], 1, S780)
f780("D", ST_ARE, [("boys가 남자아이들이라 are를 쓰기 때문이다.", "성별은 be동사를 정하지 않으므로"), ("How old 뒤에는 항상 are를 쓰기 때문이다.", "How old 뒤에도 단수 주어면 is를 쓰므로"), ("the가 붙은 주어에는 are를 쓰기 때문이다.", "the가 붙어도 단수 주어면 is를 쓰므로"),
     ("나이를 물을 때는 주어와 상관없이 are를 쓰기 때문이다.", "나이를 물어도 주어가 단수면 is를 쓰므로"), ("주어 the boys가 여러 명(복수)이므로 are를 써야 한다.", "복수 주어에는 are를 쓰므로")], 5, S780 + " 발문도 are를 쓴 이유를 묻는 형태로 맞췄다.")
f780("E", ST_ARE, [("가격을 물을 때는 항상 are를 쓰기 때문이다.", "가격을 물어도 주어가 단수면 is를 쓰므로"), ("주어 the apples가 복수이므로 are를 써야 한다.", "복수 주어에는 are를 쓰므로"), ("apple이 과일이라 are를 쓰기 때문이다.", "과일이라서가 아니라 복수라서 are를 쓰므로"),
     ("How much 뒤에는 무조건 are가 오기 때문이다.", "How much is the cake?처럼 단수 주어면 is를 쓰므로"), ("much가 '많은'이라는 뜻이라 복수 are를 쓰기 때문이다.", "much의 뜻은 be동사를 정하지 않으므로")], 2, S780 + " 발문도 are를 쓴 이유를 묻는 형태로 맞췄다.")
F(7, 80, "F", st=ST_ARE, r=R780, n=["주어 the shoes가 복수라 are를 쓰므로 정답이다.", "물건 이름이라서 be동사가 정해지는 것이 아니므로 오답이다.", "What color 뒤에도 단수 주어면 is를 쓰므로 오답이다.", "의문문에도 단수 주어면 is를 쓰므로 오답이다.", "가격을 묻는 질문이 아니고, 가격을 물어도 주어에 따라 be동사가 달라지므로 오답이다."],
  s="발문이 원문항과 달랐다. 원문항 발문의 형태로 되돌렸다. 보기와 정답은 그대로다.")

# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, r, s, **kw):
    FIX.pop((7, n, t), None)
    mk(7, n, t, items, a, r, s, **kw)
WH2 = dict(WH, How="상태·방법을 묻는 의문사")
NOA = lambda w: f"{WH2[w]}라 대답과 맞지 않으므로"
# 7-71 E: 정답(Where)과 짜임이 C와 같음 → How를 묻는 대화로 / F: 정답 위치가 B·C·F 모두 ④
S771B = "대화 아래에 ‘○○를 묻는 상황입니다’처럼 정답 의문사의 뜻을 적어 대답을 읽지 않아도 답이 나왔다. 원문항처럼 대화만 제시하도록 상황 설명을 지웠다."
redo(71, "E", [("When", NOA("When")), ("Why", NOA("Why")), ("How", "상태를 묻는 의문사라 ‘아주 좋아’라는 대답과 맞으므로"), ("What", NOA("What")), ("Who", NOA("Who"))], 3, R_WH + " How는 상태나 방법을 묻는다.",
     S771B + " 또 정답(Where)과 대화의 짜임(물건이 있는 곳을 묻고 답함)이 C와 같아, 안부를 묻는 대화로 바꾸고 보기의 Where를 How로 바꿨다.", p="A: _______ are you today?\nB: I'm great, thanks.")
redo(71, "F", [("When", "때를 묻는 의문사라 ‘5월에’라는 대답과 맞으므로"), ("Why", NOA("Why")), ("Who", NOA("Who")), ("What", NOA("What")), ("Where", NOA("Where"))], 1, R_WH,
     S771B + " 또 정답 위치가 B·C·F 모두 ④여서 보기 순서를 바꿨다.", p="A: _______ is your birthday?\nB: It is in May.")
# 7-72 F: 정답(What do you want?)이 원문항 선택지 ②와 똑같음
R772 = "‘무엇을 ~하니?’는 What + do/does + 주어 + 동사원형 ~?으로 쓴다. 주어가 3인칭 단수면 does, 아니면 do를 쓴다."
mk(7, 72, "F", [("Who do you need?", "Who는 ‘누구를’이라는 뜻이라 우리말과 맞지 않으므로"), ("What do you need?", "What + do + you + 동사원형으로 우리말을 바르게 옮겼으므로"), ("Where do you live?", "‘너는 어디에 사니?’라는 뜻이라 우리말과 맞지 않으므로"),
   ("What do you needs?", "do 뒤에는 -s를 뗀 동사원형 need를 써야 하므로"), ("What does you need?", "주어 you에는 does가 아니라 do를 쓰므로")], 2, R772,
   "정답(What do you want?)이 원문항 선택지 ②와 똑같은 문장이었고 정답 위치(④)가 D와 같았다. 우리말과 동사를 바꾸고(원하니 → 필요하니) 정답 위치를 옮겼다.", p="너는 무엇이 필요하니?")
# 7-73 D: 주어(Tom)가 C와 같음 / E·F: 다섯 유형의 정답이 모두 What → Where, When도 묻게
def g773(t, p, cs, good, why, a, s):
    gs = [x.strip() for x in good.split(" - ")]; items = []
    for ch in cs:
        xs = [x.strip() for x in ch.split(" - ")]
        bad = [(i, x) for i, x in enumerate(xs) if x != gs[i]]
        if not bad: items.append((ch, "우리말에 맞는 의문사와 주어에 맞는 동사를 바르게 짝지었으므로")); continue
        items.append((ch, ". ".join(f"{['첫째', '둘째'][i]} 빈칸 {x}: {why[i]}" for i, x in bad) + ". 따라서"))
    FIX.pop((7, 73, t), None)
    mk(7, 73, t, items, a, R_WH, s, st="R", p=p, okdup=True)
S773B = "발문이 ‘무엇인지 묻고, 질문의 동사를 반복하여 현재형으로 직접 대답’이라고 두 빈칸의 정답 형태를 알려 주었고 원문항의 우리말 해석이 빠졌다. 원문항 발문으로 되돌리고 우리말 해석을 붙였다."
g773("D", "A: _______ does Mina need? (Mina는 무엇이 필요하니?)\nB: She _______ a pencil. (그녀는 연필이 필요해.)", V(7, 73, "D")["c"], "What - needs", [W1, "3인칭 단수 주어 She에는 needs를 쓴다"], 5,
     S773B + " 질문의 주어(Tom)가 C와 같아 Mina로 바꿨다. 보기와 정답은 그대로다.")
g773("E", "A: _______ do you live? (너는 어디에 사니?)\nB: I _______ in Busan. (나는 부산에 살아.)", ["Who - live", "When - lives", "What - live", "Where - live", "Where - lives"], "Where - live", ["‘어디에’를 묻는 말이라 Where를 쓴다", "주어 I에는 동사원형 live를 쓴다"], 4,
     S773B + " 또 다섯 유형의 정답이 모두 원문항과 같은 What이어서, 장소를 묻는 대화로 바꿔 정답이 Where - live가 되게 했다.")
g773("F", "A: _______ does he play soccer? (그는 언제 축구를 하니?)\nB: He _______ soccer after school. (그는 방과 후에 축구를 해.)", ["What - play", "When - plays", "Where - play", "Who - plays", "When - play"], "When - plays", ["‘언제’를 묻는 말이라 When을 쓴다", "3인칭 단수 주어 He에는 plays를 쓴다"], 2,
     S773B + " 또 다섯 유형의 정답이 모두 원문항과 같은 What이어서, 때를 묻는 대화로 바꿔 정답이 When - plays가 되게 했다.")
# 7-74 C·E·F: 정답이 원문항의 옳은 보기를 틀리게 쓴 꼴 / D: ②·④가 주어만 다른 짝, ①이 원문항과 같음
S774B = " 정답 문장은 원문항의 옳은 보기(%s)를 틀리게 쓴 꼴이 되지 않게 다른 문장으로 바꿨다."
FIX.pop((7, 74, "C"), None); FIX.pop((7, 74, "D"), None); FIX.pop((7, 74, "E"), None); FIX.pop((7, 74, "F"), None)
f774("C", [("When <u>is</u> your birthday?", OK74("your birthday")), ("Where <u>are</u> my socks?", OK74("my socks")), ("What <u>are</u> this?", "주어 this는 한 개를 가리키므로 are가 아니라 is를 써야 하므로"), ("How <u>are</u> you?", OK74("you")), ("Who <u>is</u> that girl?", OK74("that girl"))], 3,
     S774 + S774B % "What day is it?")
f774("D", [("When <u>is</u> the test?", OK74("the test")), ("How old <u>are</u> your sister?", "주어 your sister는 3인칭 단수라 are가 아니라 is를 써야 하므로"), ("What color <u>are</u> the shoes?", OK74("the shoes")), ("Who <u>are</u> the twins?", OK74("the twins")), ("Where <u>is</u> Mina?", OK74("Mina"))], 2,
     "밑줄이 사라지고 발문이 원문항과 달랐다. 또 ②(How old are your sister?)와 ④(How old are the twins?)는 주어만 다른 짝이라 둘만 견주면 답이 나왔고, ①(What time is it?)은 원문항 ②와 똑같았다. 원문항 발문과 be동사 밑줄로 되돌리고 ①과 ④를 다른 문장으로 바꿨다. 정답은 그대로다.")
f774("E", [("Where <u>is</u> the station?", OK74("the station")), ("Who <u>are</u> your friends?", OK74("your friends")), ("How old <u>is</u> your dog?", OK74("your dog")), ("How much <u>is</u> these pens?", "주어 these pens는 복수라 is가 아니라 are를 써야 하므로"), ("What <u>are</u> these?", OK74("these"))], 4,
     S774 + S774B % "What color is the hat?")
f774("F", [("Where <u>are</u> the keys?", OK74("the keys")), ("How tall <u>is</u> the tree?", OK74("the tree")), ("Who <u>is</u> your teacher?", OK74("your teacher")), ("What <u>is</u> in the box?", "의문사 What이 주어일 때는 단수로 다루어 is를 쓰므로"), ("When <u>are</u> the party?", "주어 the party는 3인칭 단수라 are가 아니라 is를 써야 하므로")], 5,
     S774 + S774B % "What time is it?" + " 정답 위치도 원문항(①)과 다르게 옮겼다.")
# 7-75 B: ②(How old ~? - She is nine.)가 정답 ④(How old is she?)의 단서 / D: 질문 넷이 원문항과 같음
OK75 = lambda k: f"{k}을(를) 묻는 말에 알맞게 답했으므로"
FIX.pop((7, 75, "B"), None)
f775("B", [("A: Where is the cat? - B: It's under the bed.", "장소를 묻는 말에 장소로 답했으므로"), ("A: When is the party? - B: It's on Saturday.", "때를 묻는 말에 요일로 답했으므로"), ("A: What color is your bag? - B: It's blue.", "색깔을 묻는 말에 색깔로 답했으므로"),
     ("A: How old is she? - B: It is Monday.", "나이를 묻는 말에 요일로 답해 어색하므로"), ("A: Who is he? - B: He is my uncle.", "누구인지 묻는 말에 사람으로 답했으므로")], 4,
     S775 + " 또 ②(How old is your sister? - She is nine.)가 나이를 묻는 말의 알맞은 대답을 보여 주어 정답 ④(How old is she? - It is Monday.)의 단서가 되었으므로 ②를 다른 대화로 바꿨다.")
mk(7, 75, "D", [("A: What is this? - B: It's a kite.", "무엇인지 묻는 말에 물건으로 답했으므로"), ("A: Who is that man? - B: He is in the kitchen.", "누구인지 묻는 말에 장소로 답해 어색하므로"), ("A: When is the test? - B: It's on Friday.", "때를 묻는 말에 요일로 답했으므로"),
   ("A: How are your parents? - B: They are fine.", "안부를 묻는 말에 상태로 답했으므로"), ("A: What color is your bike? - B: It's green.", "색깔을 묻는 말에 색깔로 답했으므로")], 2, R775,
   "옳은 대화 넷의 질문(How old ~? / What time is it? / How is the weather? / What day is it?)이 원문항과 같고 대답만 달랐다. ①(How old is Leo? - He is twelve.)은 나이를 답하는 꼴을 보여 주어 정답 ③(Where is Mina? - She is eleven.)의 단서도 되었고, 어색한 까닭(장소를 물었는데 나이로 답함)이 E와 같았다. 정답 위치(③)도 원문항과 같았다. 대화를 새로 쓰고 정답 위치를 옮겼다.")
# 7-76 C: 정답(Why)이 B와 같음 / E: 문장이 71번 원문항과 같음 / F: 문장과 정답이 같은 유형의 71번 변형과 같음
R776 = "Who는 사람, What은 사물·일, Where는 장소, When은 때, Why는 이유, How는 상태·방법을 묻는다. 우리말의 ‘누구, 무엇, 어디, 언제, 왜, 어떻게’에 맞춰 고른다."
N76 = {"What": "What은 ‘무엇’이라는 뜻이므로", "Who": "Who는 ‘누구’라는 뜻이므로", "Where": "Where는 ‘어디’라는 뜻이므로", "When": "When은 ‘언제’라는 뜻이므로", "Why": "Why는 ‘왜’라는 뜻이므로", "How": "How는 ‘어떻게, 어떠한’이라는 뜻이므로"}
def g776(t, p, opts, a, ko, s):
    mk(7, 76, t, [(o, f"우리말의 ‘{ko}’에 맞는 의문사이므로" if i + 1 == a else N76[o]) for i, o in enumerate(opts)], a, R776, s, p=p)
g776("C", "_______ is the weather today?\n(오늘 날씨가 어떠니?)", ["Why", "How", "Where", "Who", "What"], 2, "어떠니", "정답(Why)과 문장의 짜임(Why are you ~?)이 B와 같았다(유형 간 중복). 날씨를 묻는 문장으로 바꿔 정답이 How가 되게 했다.")
g776("E", "_______ are those boys?\n(저 소년들은 누구니?)", ["What", "Where", "Who", "When", "How"], 3, "누구", "문장(___ is she?)과 정답(Who)이 같은 단원 71번 원문항과 똑같았다. 주어를 바꾸고 정답 위치도 옮겼다.")
g776("F", "_______ is the test?\n(시험은 언제니?)", ["How", "What", "Who", "When", "Where"], 4, "언제", "문장(___ is your birthday?)과 정답(When)이 같은 유형의 71번 변형과 똑같아, 함께 출제하면 같은 문장이 두 번 나온다. 다른 문장으로 바꿨다. 보기와 정답은 그대로다.")
# 7-78 C: 오답의 주어 넷이 원문항 그대로이고 정답만 의문사가 다름 / F: 보기 둘이 원문항과 같고 ①·②가 짝
FIX.pop((7, 78, "C"), None); FIX.pop((7, 78, "F"), None)
f778("C", [("How _______ your mom?", IS_("your mom")), ("How much _______ it?", IS_("it")), ("Who _______ that girl?", IS_("that girl")), ("Where _______ you?", ARE("you")), ("What color _______ your bike?", IS_("your bike"))], 4,
     "발문에 ‘현재형’이 붙었다. 또 오답의 주어 넷(she, it, your cat, Eddie)이 원문항 그대로이고, 오답은 모두 How nice로 시작하는데 정답만 Where로 시작해 꼴만으로 답이 드러났다. 원문항 발문으로 되돌리고 보기를 새로 썼다.")
f778("F", [("What _______ your phone number?", IS_("your phone number")), ("Where _______ the children?", ARE("the children")), ("How much _______ this toy?", IS_("this toy")), ("What color _______ the bag?", IS_("the bag")), ("When _______ the concert?", IS_("the concert"))], 2,
     "발문에 ‘현재형’이 붙었다. 또 보기 둘(How old ___ your cat? / How old ___ she?)이 원문항 선택지 그대로이고, ①(Where ___ Tom?)과 ②(Where ___ the children?)는 주어만 다른 짝이라 둘만 견주면 답이 나왔다. 원문항 발문으로 되돌리고 ①·③·⑤를 새로 썼다. 정답은 그대로다.")
# 7-80 B: 오답이 문장과 관계없음(음식 이름, 가격 — 원문항 문장에 맞춘 오답을 그대로 가져옴)
FIX.pop((7, 80, "B"), None)
f780("B", ST_IS, [("'What color' 뒤에는 무조건 'is'만 올 수 있기 때문이다.", "What color 뒤에도 복수 주어면 are를 쓰므로"), ("색깔을 물어보는 질문에서는 주어와 상관없이 'is'를 쓰기 때문이다.", "질문의 종류가 아니라 주어에 따라 be동사가 정해지므로"),
     ("'bag'은 물건이라서 'are'를 쓸 수 없기 때문이다.", "물건이라도 여러 개(bags)면 are를 쓰므로"), ("주어인 'the bag'이 3인칭 단수이므로 be동사 'is'를 써야 한다.", "주어 the bag이 3인칭 단수라 is를 쓰므로"),
     ("'the'가 붙은 명사 앞에는 항상 'is'를 쓰기 때문이다.", "the가 붙어도 복수 명사면 are를 쓰므로")], 4,
     "발문이 원문항과 달랐다. 또 오답이 이 문장과 관계없는 말(‘음식 이름이라서’, ‘가격을 물으면’ — 원문항의 문장 How much is the cake?에 맞춘 오답을 그대로 가져왔다)이라 바로 지워지고 정답만 문장 속 낱말을 말했다. 원문항 발문으로 되돌리고, 이 문장을 두고 말하는 그럴듯한 오해로 오답을 새로 썼다.")
