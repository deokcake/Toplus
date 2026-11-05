# 7급 CH3 be동사 (21~30) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
R_BE = "현재형 be동사는 주어가 I면 am, 3인칭 단수(he, she, it, 사람·사물 하나)면 is, you·we·they와 복수 주어(A and B 포함)면 are를 쓴다."

# 7-22 E: 원문항처럼 ‘알맞지 않은 것’을 고르도록
mk(7, 22, "E", [("We", "We: are와 어울리는 주어라 들어갈 수 있으므로"), ("The kids", "The kids: 복수 주어라 are와 어울려 들어갈 수 있으므로"), ("She", "She: 3인칭 단수 주어라 are가 아니라 is와 써야 하므로"), ("You", "You: are와 어울리는 주어라 들어갈 수 있으므로"), ("Tom and I", "Tom and I: 복수 주어라 are와 어울려 들어갈 수 있으므로")], 3, R_BE,
   "원문항은 빈칸에 ‘알맞지 않은 것’을 고르는데, 변형은 ‘알맞은 것’을 고르게 바뀌어 과제가 반대였다. 원문항 발문으로 되돌리고, are 앞에 올 수 있는 주어 넷과 올 수 없는 주어 하나로 선택지를 새로 썼다.", st="R", p="_______ are hungry.")

# 7-23 B: 정답 주어를 원문항(I)과 다르게
mk(7, 23, "B", [("The cats _______ small.", "The cats: 복수 주어라 are가 들어가 나머지와 같으므로"), ("We _______ ready.", "We: are가 들어가 나머지와 같으므로"), ("The baby _______ asleep.", "The baby: 3인칭 단수 주어라 is가 들어가 나머지(are)와 다르므로"), ("They _______ here.", "They: are가 들어가 나머지와 같으므로"), ("You _______ nice.", "You: are가 들어가 나머지와 같으므로")], 3, R_BE,
   "정답 문장의 주어(I)가 원문항 정답과 같았다. 정답 문장의 주어를 The baby로 바꿨다.")

# 7-24 장소 표현: 원문항 선택지를 되풀이하지 않고 유형마다 새로
R724 = "우리말의 장소를 영어로 옮길 때 ‘~ 위에’는 on, ‘~ 안에’는 in, 학교·집·정류장 같은 지점은 at으로 나타낸다."
S724 = "오답 서너 개(at the party, in the classroom, on the chair, at the bus stop)가 원문항 선택지를 그대로 썼다. 유형마다 장소 표현을 새로 썼다."
def f724(t, ko, en, items, a, s=S724):
    mk(7, 24, t, items, a, R724, s, p=f"{ko}\n{en}")
NO = lambda k: f"‘{k}’라는 뜻이라 우리말과 맞지 않으므로"
f724("B", "그 책은 책상 위에 있다.", "The book is ____________.", [("on the desk", "‘책상 위에’라는 우리말과 맞으므로"), ("under the bed", NO("침대 아래에")), ("in the bag", NO("가방 안에")), ("next to the lamp", NO("램프 옆에")), ("behind the door", NO("문 뒤에"))], 1)
f724("C", "Mina는 부엌에 있다.", "Mina is ____________.", [("at the station", NO("역에")), ("under the desk", NO("책상 아래에")), ("in the garden", NO("정원에")), ("on the playground", NO("운동장에")), ("in the kitchen", "‘부엌에’라는 우리말과 맞으므로")], 5,
     "선택지는 원문항과 같은 장소 표현이고 정답도 하나로 정해져 그대로 두었다. 해설만 우리말 뜻과 대조하는 방식으로 새로 썼다.")
f724("D", "Tom은 학교에 있다.", "Tom is ____________.", [("at the zoo", NO("동물원에")), ("at school", "‘학교에’라는 우리말과 맞으므로"), ("at the library", NO("도서관에")), ("at the hospital", NO("병원에")), ("at the beach", NO("해변에"))], 2)
f724("E", "우리는 공원에 있다.", "We are ____________.", [("in the car", NO("차 안에")), ("in the museum", NO("박물관에")), ("at the market", NO("시장에")), ("in the park", "‘공원에’라는 우리말과 맞으므로"), ("on the bridge", NO("다리 위에"))], 4)
f724("F", "그녀는 집에 있다.", "She is ____________.", [("at the store", NO("가게에")), ("in the gym", NO("체육관에")), ("at the theater", NO("극장에")), ("on the bus", NO("버스에")), ("at home", "‘집에’라는 우리말과 맞으므로")], 5)

# 7-25 F: 짝 문장 없애기
mk(7, 25, "F", [("We are ready.", "주어 We에 are를 바르게 썼으므로"), ("My books is new.", "복수 주어 My books에는 are를 써야 하므로"), ("The pencils are long.", "복수 주어 The pencils에 are를 바르게 썼으므로"), ("The cake is sweet.", "단수 주어 The cake에 is를 바르게 썼으므로"), ("Jane is kind.", "3인칭 단수 주어 Jane에 is를 바르게 썼으므로")], 2, R_BE,
   "정답(My books is new)과 짝을 이루는 옳은 문장(My book is new)이 있어 대비 단서가 되었다. 짝 문장을 The cake is sweet.로 바꿨다.")

# 7-26 be동사 빈칸: 원문항 발문, B는 주어를 새로
S726 = "발문에 ‘현재형 be동사’가 붙었다. 원문항 발문으로 되돌렸다."
BE0 = "be는 원형이라 주어 뒤에 그대로 쓸 수 없으므로"; CAN = "can 뒤에는 동사원형이 와야 해 형용사·장소 앞에 바로 쓸 수 없으므로"
def f726(t, p, subj, items, a, s=S726 + " 보기와 정답은 그대로다."):
    mk(7, 26, t, items, a, R_BE, s, st="R", p=p)
def o726(order, s_):
    d = {"am": "am은 주어 I에만 쓰므로", "is": "is는 3인칭 단수 주어에 쓰므로", "are": f"주어({s_})에 맞는 be동사이므로", "be": BE0, "can": CAN}
    return [(w, d[w]) for w in order]
f726("B", "The students _______ at school today.", "", o726(["am", "is", "are", "be", "can"], "The students"), 3, S726 + " 주어(They)와 정답이 원문항과 같아 주어를 The students로 바꿨다.")
f726("C", "We _______ very happy.", "", o726(["is", "are", "can", "am", "be"], "We"), 2)
f726("D", "You _______ very strong.", "", o726(["can", "is", "be", "am", "are"], "You"), 5)
f726("E", "My parents _______ very busy.", "", o726(["be", "are", "am", "is", "can"], "My parents"), 2)
f726("F", "We _______ at home.", "", o726(["are", "be", "can", "am", "is"], "We"), 1)

# 7-27 축약형: 원문항처럼 같은 주어의 틀린 축약형 오답
R727 = "be동사 축약형은 빠진 글자 자리에 아포스트로피(')를 찍어 I'm, you're, he's, she's, it's, we're, they're로 쓴다. your, its, his는 소유격이라 축약형이 아니다."
S727 = "원문항 오답은 같은 말의 틀린 축약형(Were, Weare, W're, We's)인데, 변형 오답은 다른 인칭의 축약형이라 주어만 보고 바로 지워졌다. 원문항처럼 같은 주어의 틀린 축약형으로 오답을 새로 썼다."
def f727(t, p, items, a, s=S727):
    mk(7, 27, t, items, a, R727, s, p=p)
f727("C", "You are nice. → _______ nice.", [("Your", "your는 ‘너의’라는 소유격이라 you are의 축약형이 아니므로"), ("Youre", "아포스트로피(')를 빠뜨렸으므로"), ("You's", "you are의 are를 's로 줄일 수 없으므로"), ("You're", "you are를 바르게 줄였으므로"), ("Yo're", "you의 글자를 빼고 줄였으므로")], 4)
f727("D", "It is cold. → _______ cold.", [("Its", "its는 ‘그것의’라는 소유격이라 it is의 축약형이 아니므로"), ("It's", "it is를 바르게 줄였으므로"), ("Itis", "it is를 아포스트로피 없이 붙여 썼으므로"), ("I's", "it의 t를 빼고 줄였으므로"), ("It'is", "is의 i를 빼지 않고 아포스트로피만 넣었으므로")], 2,
     S727 + " 주어도 B(They)와 겹치지 않게 It으로 바꿨다.")
f727("E", "She is kind. → _______ kind.", [("Shes", "아포스트로피(')를 빠뜨렸으므로"), ("She'is", "is의 i를 빼지 않고 아포스트로피만 넣었으므로"), ("She's", "she is를 바르게 줄였으므로"), ("Sh's", "she의 글자를 빼고 줄였으므로"), ("She'r", "is를 're처럼 잘못 줄였으므로")], 3)
f727("F", "He is tall. → _______ tall.", [("Hes", "아포스트로피(')를 빠뜨렸으므로"), ("He'is", "is의 i를 빼지 않고 아포스트로피만 넣었으므로"), ("H's", "he의 글자를 빼고 줄였으므로"), ("His", "his는 ‘그의’라는 소유격이라 he is의 축약형이 아니므로"), ("He's", "he is를 바르게 줄였으므로")], 5)

# 7-28 Where 대화: 원문항 발문, C는 정답 조합을 원문항(are - are)과 다르게
R728 = "Where + be동사 + 주어?에서 be동사는 주어에 맞추고, 대답의 be동사도 대답의 주어에 맞춘다."
S728 = "발문에 ‘현재형으로 대화를 완성할 때’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def f728(t, good, why, s=S728, p=None, c=None, a=None):
    V_ = V(7, 28, t); cs = c or V_["c"]; gs = [x.strip() for x in good.split(" - ")]; items = []
    for ch in cs:
        xs = [x.strip() for x in ch.split(" - ")]
        if xs == gs: items.append((ch, "질문과 대답의 주어에 맞는 be동사를 바르게 썼으므로")); continue
        bits = [f"{['첫째', '둘째'][i]} 빈칸 {x}: {why[i]}" for i, (x, g) in enumerate(zip(xs, gs)) if x != g]
        items.append((ch, ". ".join(bits) + ". 따라서"))
    kw = {"p": p} if p else {}
    mk(7, 28, t, items, a or int(V_["ans"]), R728, s, st="R", okdup=True, **kw)
f728("B", "are - am", ["주어 you에는 are를 쓴다", "주어 I에는 am을 쓴다"])
f728("D", "is - is", ["3인칭 단수 주어 Jane에는 is를 쓴다", "주어 She에는 is를 쓴다"])
f728("E", "is - is", ["단수 주어 your book에는 is를 쓴다", "주어 It에는 is를 쓴다"])
f728("F", "are - am", ["주어 you에는 are를 쓴다", "주어 I에는 am을 쓴다"])
f728("C", "are - is", ["복수 주어 Tom and Jane에는 are를 쓴다", "단수 주어 Tom에는 is를 쓴다"], p="A: Where ________ Tom and Jane?\nB: Tom ________ in the park.", c=["are - is", "is - are", "is - is", "are - am", "are - are"], a=1,
     s="정답 조합(are - are)과 대화 구조가 원문항과 같았고 발문에 조건이 붙었다. 원문항 발문으로 되돌리고, 두 사람을 묻고 한 사람에 대해 답하는 대화로 바꿔 정답 조합이 are - is가 되게 했다.")

# 7-29 be동사를 쓴 이유: 원문항 발문과 밑줄, 인칭·수에 관한 그럴듯한 오해로 오답
R729 = "be동사는 주어의 인칭과 수에 맞춘다. I(1인칭 단수)는 am, 나와 너가 아닌 한 명·한 개(3인칭 단수)는 is, you와 여러 명·여러 개(복수)는 are이다. 뒤에 오는 형용사나 장소 표현은 be동사를 정하지 않는다."
S729 = "원문항 오답은 인칭·수에 대한 그럴듯한 오해인데, 변형 오답(‘의문문이기 때문’, ‘문장 길이가 짧기 때문’ 등)은 뻔하고 유형마다 반복되었으며 밑줄도 사라졌다. 원문항 발문과 밑줄로 되돌리고, 인칭·수에 관한 그럴듯한 오해로 오답을 유형마다 새로 썼다."
ST729 = lambda v: f"다음 문장에서 be동사 '{v}'를 사용한 이유를 가장 정확하게 설명한 것을 고르세요."
def f729(t, v, p, items, a, s=S729):
    mk(7, 29, t, items, a, R729, s, st=ST729(v) if v != "am" else "다음 문장에서 be동사 'am'을 사용한 이유를 가장 정확하게 설명한 것을 고르세요.", p=p)
f729("B", "are", "The boys <u>are</u> happy.", [("The boys는 남자아이들이라 남자에는 are를 쓰기 때문이다.", "성별은 be동사를 정하지 않으므로"), ("happy가 형용사라 형용사 앞에는 항상 are를 쓰기 때문이다.", "뒤의 형용사는 be동사를 정하지 않으므로"), ("주어 The boys가 여러 명(복수)이기 때문이다.", "복수 주어에는 are를 쓰므로"),
     ("boys가 -s로 끝나는 단수 명사이기 때문이다.", "boys는 boy의 복수형이고, 단수라면 is를 쓰므로"), ("The로 시작하는 주어에는 항상 are를 쓰기 때문이다.", "The는 be동사를 정하지 않으므로")], 3)
f729("C", "is", "Jane <u>is</u> kind.", [("Jane이 여자라서 is를 쓰기 때문이다.", "성별은 be동사를 정하지 않으므로"), ("kind가 한 단어라서 is를 쓰기 때문이다.", "뒤에 오는 말의 길이는 be동사를 정하지 않으므로"), ("주어가 2인칭이라서 is를 쓰기 때문이다.", "Jane은 2인칭이 아니고, 2인칭 you에는 are를 쓰므로"),
     ("문장이 과거의 일을 나타내기 때문이다.", "is는 현재형이므로"), ("주어 Jane이 나도 너도 아닌 한 사람(3인칭 단수)이기 때문이다.", "3인칭 단수 주어에는 is를 쓰므로")], 5)
f729("D", "is", "The puppy <u>is</u> under the chair.", [("under the chair처럼 장소가 오면 항상 is를 쓰기 때문이다.", "장소 표현은 be동사를 정하지 않으므로"), ("주어 The puppy가 한 마리(3인칭 단수)이기 때문이다.", "3인칭 단수 주어에는 is를 쓰므로"), ("puppy가 동물이라 동물 주어에는 항상 is를 쓰기 때문이다.", "동물 주어도 여러 마리면 are를 쓰므로"),
     ("주어가 여러 마리(복수)를 나타내기 때문이다.", "The puppy는 한 마리이고, 복수라면 are를 쓰므로"), ("the가 붙은 주어는 1인칭이기 때문이다.", "the가 붙은 주어는 1인칭이 아니고, 1인칭 I에는 am을 쓰므로")], 2)
f729("E", "am", "I <u>am</u> hungry.", [("주어 I에는 am을 짝지어 쓰기 때문이다.", "주어 I에는 am을 쓰므로"), ("hungry처럼 배고픔을 나타낼 때는 am을 쓰기 때문이다.", "뒤의 형용사는 be동사를 정하지 않으므로"), ("I가 3인칭 단수라서 am을 쓰기 때문이다.", "I는 1인칭이고, 3인칭 단수에는 is를 쓰므로"),
     ("I는 대문자로 쓰는 말이라 am을 쓰기 때문이다.", "대문자는 be동사를 정하지 않으므로"), ("주어가 여러 명이라서 am을 쓰기 때문이다.", "I는 한 명이고, 여러 명이면 are를 쓰므로")], 1)
f729("F", "are", "We <u>are</u> ready.", [("We에는 나(I)가 들어 있어 I처럼 am을 써야 하는데 are로 바꿔 쓴 것이기 때문이다.", "we는 여러 명이라 처음부터 are를 쓰므로"), ("ready가 '준비된'이라는 뜻이라 are와 어울리기 때문이다.", "뒤의 형용사는 be동사를 정하지 않으므로"), ("We가 2인칭이기 때문이다.", "we는 1인칭 복수이므로"),
     ("주어 We가 나를 포함한 여러 명(복수)이기 때문이다.", "복수 주어 we에는 are를 쓰므로"), ("We가 짧은 단어라서 are를 쓰기 때문이다.", "단어의 길이는 be동사를 정하지 않으므로")], 4)

# 7-30 옳은 것 모두: 원문항 발문, be동사 밑줄과 (가)~(라) 기호
R730 = "각 문장의 주어를 보고 밑줄 친 be동사를 판단한다. 복수 주어에는 are, 3인칭 단수 주어에는 is, I에는 am을 쓴다."
S730 = "원문항의 be동사 밑줄이 사라지고 발문이 바뀌었으며, 일부는 기호 (가)가 ‘가.’로 바뀌었다. 원문항 발문과 밑줄, (가)~(라) 기호로 되돌렸다. 보기와 정답은 그대로다."
def f730(t, judge):
    V_ = V(7, 30, t); lines = V_["passage"].split("\n"); out = []
    for l in lines:
        l = re.sub(r"^([가나다라])\. ", r"(\1) ", l)
        l = re.sub(r"\b(am|is|are)\b", r"<u>\1</u>", l, count=1)
        out.append(l)
    ok = V_["c"][int(V_["ans"]) - 1]
    F(7, 30, t, st="R", p="\n".join(out), r=R730, pre=["문장별 판정: " + j for j in judge], k=f"밑줄 친 부분이 옳은 문장은 {ok}이다.", n=setnotes(V_["c"], ok, "옳은 문장"), okdup=True, s=S730)
f730("B", ["(가) O. 복수 주어 The girls에 are를 썼다.", "(나) O. 3인칭 단수 주어 He에 is를 썼다.", "(다) X. 주어 You에는 are를 써야 한다.", "(라) X. 복수 주어 Two dogs에는 are를 써야 한다."])
f730("C", ["(가) O. 복수 주어 My parents에 are를 썼다.", "(나) X. 단수 주어 The puppy에는 is를 써야 한다.", "(다) O. 주어 I에 am을 썼다.", "(라) X. 복수 주어 The books에는 are를 써야 한다."])
f730("D", ["(가) O. 단수 주어 The dog에 is를 썼다.", "(나) X. 복수 주어 The boys에는 are를 써야 한다.", "(다) O. 주어 I에 am을 썼다.", "(라) X. 주어 We에는 are를 써야 한다."])
f730("E", ["(가) O. 3인칭 단수 주어 Tom에 is를 썼다.", "(나) O. 주어 We에 are를 썼다.", "(다) X. 단수 주어 The cat에는 is를 써야 한다.", "(라) X. 주어 I에는 am을 써야 한다."])
f730("F", ["(가) O. 주어 They에 are를 썼다.", "(나) X. 3인칭 단수 주어 Jane에는 is를 써야 한다.", "(다) O. 복수 주어 The books에 are를 썼다.", "(라) X. 주어 I에는 am을 써야 한다."])


# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, r, s, **kw):
    FIX.pop((7, n, t), None)
    mk(7, n, t, items, a, r, s, **kw)
# 7-23 F: 정답 문장(Tom ___ ~)과 위치(⑤), 나머지 주어(We, They, You)가 D와 거의 같음
redo(23, "F", [("We _______ friends.", "We: are가 들어가 나머지와 같으므로"), ("The boys _______ busy.", "The boys: 복수 주어라 are가 들어가 나머지와 같으므로"), ("They _______ students.", "They: are가 들어가 나머지와 같으므로"),
     ("My uncle _______ a cook.", "My uncle: 3인칭 단수 주어라 is가 들어가 나머지(are)와 다르므로"), ("You _______ kind.", "You: are가 들어가 나머지와 같으므로")], 4, R_BE,
     "정답 문장의 주어(Tom)와 위치(⑤)가 D와 같고 나머지 주어(We, They, You)도 겹쳤다. 정답 문장을 바꾸고 위치를 옮겼다.")
# 7-25 E: 서술어가 같은 옳은 문장(The girl is happy.)과 틀린 문장(The boys is happy.)이 함께 있음
redo(25, "E", [("The dogs are big.", "복수 주어 The dogs에 are를 바르게 썼으므로"), ("Tom is here.", "3인칭 단수 주어 Tom에 is를 바르게 썼으므로"), ("The girl is my cousin.", "단수 주어 The girl에 is를 바르게 썼으므로"), ("They are busy.", "주어 They에 are를 바르게 썼으므로"),
     ("The boys is happy.", "복수 주어 The boys에는 are를 써야 하므로")], 5, R_BE,
     "서술어가 같은 옳은 문장(③ The girl is happy.)과 틀린 문장(⑤ The boys is happy.)이 함께 있어 둘만 견주면 답이 나왔다. ③을 다른 문장으로 바꿨다. 정답은 그대로다.")
# 7-26 C·D·E: 다섯 유형의 정답이 모두 원문항과 같은 are → 주어를 바꿔 is, am도 정답이 되게
S726B = "발문에 ‘현재형 be동사’가 붙었고, 다섯 유형의 정답이 모두 원문항과 같은 are였다. 원문항 발문으로 되돌리고 주어를 바꿔 정답이 %s가 되게 했다."
def o726b(order, subj, good):
    d = {"am": "am은 주어 I에만 쓰므로", "is": "is는 3인칭 단수 주어에 쓰므로", "are": "are는 you·복수 주어에 쓰므로", "be": BE0, "can": CAN}
    d[good] = f"주어({subj})에 맞는 be동사이므로"
    return [(w, d[w]) for w in order]
FIX.pop((7, 26, "C"), None); FIX.pop((7, 26, "D"), None); FIX.pop((7, 26, "E"), None)
f726("C", "My sister _______ very happy.", "", o726b(["is", "are", "can", "am", "be"], "My sister", "is"), 1, S726B % "is")
f726("D", "I _______ very strong.", "", o726b(["can", "is", "be", "am", "are"], "I", "am"), 4, S726B % "am")
f726("E", "My father _______ very busy.", "", o726b(["be", "is", "am", "are", "can"], "My father", "is"), 2, S726B % "is")
# 7-28 F: 대화(Where are you? — I am ~.)와 정답 조합(are - am)이 B와 같음
FIX.pop((7, 28, "F"), None)
f728("F", "am - are", ["주어 I에는 am을 쓴다", "주어 You에는 are를 쓴다"], p="A: Where ________ I?\nB: You ________ in the school library.", a=4,
     s="발문에 ‘현재형으로 대화를 완성할 때’가 붙었고, 대화(Where are you? — I am ~.)와 정답 조합(are - am)이 B와 같았다. 원문항 발문으로 되돌리고 대화를 바꿔 정답 조합이 am - are가 되게 했다. 보기는 그대로다.")
# 7-30 D·E·F: 정답 조합이 다른 유형과 같음(C·D·F (가),(다) / B·E (가),(나)) → 문장 순서를 바꿔 조합을 다르게
S730B = "원문항의 be동사 밑줄이 사라지고 발문이 바뀌었으며, 기호 (가)가 ‘가.’로 바뀌었다. 정답 조합도 %s와 같았다. 원문항 발문과 밑줄, (가)~(라) 기호로 되돌리고 문장 순서를 바꿔 정답 조합이 유형마다 다르게 했다."
def g730(t, lines, judge, ok, c, s):
    FIX.pop((7, 30, t), None)
    a = c.index(ok) + 1
    F(7, 30, t, st="R", p="\n".join(lines), c=c, a=a, r=R730, pre=["문장별 판정: " + j for j in judge], k=f"밑줄 친 부분이 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), okdup=True, s=s + ipos(a))
g730("D", ["(가) The boys <u>is</u> busy.", "(나) The dog <u>is</u> cute.", "(다) I <u>am</u> happy.", "(라) We <u>is</u> ready."],
     ["(가) X. 복수 주어 The boys에는 are를 써야 한다.", "(나) O. 단수 주어 The dog에 is를 썼다.", "(다) O. 주어 I에 am을 썼다.", "(라) X. 주어 We에는 are를 써야 한다."], "(나), (다)",
     ["(가), (다)", "(나), (다)", "(나), (라)", "(가), (라)", "(가), (나)"], S730B % "C((가), (다))" + " 보기는 그대로다.")
g730("E", ["(가) Tom <u>is</u> home.", "(나) The cat <u>are</u> small.", "(다) I <u>are</u> late.", "(라) We <u>are</u> friends."],
     ["(가) O. 3인칭 단수 주어 Tom에 is를 썼다.", "(나) X. 단수 주어 The cat에는 is를 써야 한다.", "(다) X. 주어 I에는 am을 써야 한다.", "(라) O. 주어 We에 are를 썼다."], "(가), (라)",
     ["(가), (다)", "(가), (라)", "(나), (다)", "(가), (나)", "(나), (라)"], S730B % "B((가), (나))" + " 보기는 그대로다.")
g730("F", ["(가) Jane <u>are</u> kind.", "(나) I <u>is</u> hungry.", "(다) They <u>are</u> students.", "(라) The books <u>are</u> new."],
     ["(가) X. 3인칭 단수 주어 Jane에는 is를 써야 한다.", "(나) X. 주어 I에는 am을 써야 한다.", "(다) O. 주어 They에 are를 썼다.", "(라) O. 복수 주어 The books에 are를 썼다."], "(다), (라)",
     ["(가), (라)", "(가), (다)", "(가), (나)", "(다), (라)", "(나), (다)"], S730B % "C((가), (다))" + " 보기 ④는 (다), (라)로 바꿨다.")
