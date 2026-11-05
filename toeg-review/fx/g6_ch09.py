# 6급 CH9 현재진행형 (81~90) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
R_PR = "현재진행형은 am/is/are + 동사원형-ing로 지금 하고 있는 동작을 나타낸다. 의문문은 be동사를 주어 앞에, 부정문은 be동사 뒤에 not을 둔다. be동사는 주어에 맞춰 I am, 3인칭 단수 is, you·복수 are를 쓴다."

# 원문항 발문으로만 되돌리는 문항
for t in "CDF": F(6, 82, t, st="R", s="발문에 ‘“지금 ~하고 있다”를 현재진행형으로’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BDEF": F(6, 83, t, st="R", s="발문에 ‘현재진행형과 원래의 동작을 유지하면서’가 붙어 정답 형태를 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
F(6, 84, "C", st="R", xr=[("No, she isn't.로 답하는 조건과 맞지 않는다", "No, she isn't.라는 대답과 맞지 않는다")], s="발문이 ‘대답에 맞는 현재진행형 질문’이라고 정답 형식을 알려 주었다. 원문항 발문으로 되돌렸다. 오답은 원문항처럼 문법은 옳고 대답과 맞지 않는 질문이라 그대로다.")
F(6, 85, "C", st="R", s="발문이 ‘상태동사 용법에 맞지 않는 문장’, ‘(소유·지식은 … 상태를 뜻한다.)’라고 정답 기준을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDEF": F(6, 86, t, st="R", s="발문이 ‘현재진행형으로 지금 하고 있는 동작을 나타내도록’이라고 정답 형태를 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
F(6, 87, "D", st="R", xr=[("평서문 어순의 확인 질문은 대화에서 가능하지만, be동사로 시작하는 기본형 의문문이라는 조건과 다르다.", "평서문 어순에 물음표만 붙인 것은 의문문으로 바르게 바꾼 것이 아니다.")], s="발문이 ‘현재진행형을 유지하여, be동사로 시작하고 물음표로 끝나는 기본형 의문문’이라고 정답 형식을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "DEF": F(6, 88, t, st="R", s="발문에 ‘주어의 형태는 옳다고 할 때, 현재진행형 문장의’가 붙었다. 주어에 밑줄이 없어 복수 정답이 생기지 않으므로 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 6-82 B·E: 원문항과 명사만 다른 문장을 새로
R682 = "‘지금 ~하고 있다’는 am/is/are + 동사원형-ing로 옮긴다. be동사 없이 -ing형만 쓰거나 be동사 뒤에 동사원형을 쓰지 않는다."
S682 = "우리말·문장·오답이 원문항(그는 지금 책을 읽고 있다)과 명사만 달랐고 발문에 조건이 붙었다. 원문항 발문으로 되돌리고 우리말과 문장을 새로 썼다."
def f682(t, ko, items, a, s=S682):
    mk(6, 82, t, items, a, R682, s, st="R", p=ko)
f682("B", "Mina는 지금 부엌에서 요리하고 있다.", [("Mina cooks in the kitchen now.", "현재형이라 지금 하고 있는 동작을 나타내지 못하므로"), ("Mina is cook in the kitchen now.", "is 뒤에는 동사원형이 아니라 cooking을 써야 하므로"), ("Mina cooking in the kitchen now.", "be동사 없이 -ing형만으로는 동사 자리를 채울 수 없으므로"),
     ("Mina is cooking in the kitchen now.", "3인칭 단수 주어에 is + cooking으로 바르게 옮겼으므로"), ("Mina being cooking in the kitchen now.", "being이 아니라 주어에 맞는 is를 써야 하므로")], 4)
f682("E", "아이들은 지금 공원에서 뛰고 있다.", [("The children are running in the park now.", "복수 주어 The children에 are + running으로 바르게 옮겼으므로"), ("The children runs in the park now.", "현재형이고 복수 주어에 -s를 붙였으므로"), ("The children is running in the park now.", "복수 주어 The children에는 are를 써야 하므로"),
     ("The children running in the park now.", "be동사 없이 -ing형만으로는 동사 자리를 채울 수 없으므로"), ("The children are run in the park now.", "are 뒤에는 동사원형이 아니라 running을 써야 하므로")], 1)

# 6-83 C: 원문항 발문으로 되돌리면 과거진행형도 답이 되는 보기를 형태 오류로
F(6, 83, "C", st="R", c=["Are - are writing", "Do - is write", "Are - is writing", "Are - is write", "Is - are writing"], a=3, r=R_PR,
  n=["둘째 문장: 3인칭 단수 주어 Jane에는 is writing을 써야 하므로 오답이다.", "첫째 문장: 진행형 의문문은 Do가 아니라 be동사로 시작하고, 둘째 문장: is 뒤에는 writing을 써야 하므로 오답이다.", "복수 주어 the boys에 Are, 단수 주어 Jane에 is writing을 바르게 썼으므로 정답이다.",
     "둘째 문장: is 뒤에는 동사원형이 아니라 writing을 써야 하므로 오답이다.", "첫째 문장: 복수 주어 the boys에는 Are를, 둘째 문장: Jane에는 is를 써야 하므로 오답이다."],
  s="발문에 ‘현재진행형과 원래의 동작을 유지하면서’가 붙었다. 원문항 발문으로 되돌리면 과거진행형 보기(Were - was writing)도 답이 될 수 있어, 이 보기를 형태 오류(Are - is write)로 바꿨다. 정답 위치 ③.")

# 6-84 대답에 맞는 질문: 원문항 발문, 원문항처럼 문법은 옳고 대답과 맞지 않는 질문
R684 = "짧은 대답의 주어와 be동사를 보고 질문을 찾는다. you에 대한 질문에는 I/we, 한 남자는 he, 한 여자는 she, 사물·날씨는 it, 여럿은 they로 답하고, 과거 질문(Was/Were)에는 wasn't/weren't로 답한다."
S684 = "발문이 ‘대답에 맞는 현재진행형 질문’이라고 정답 형식을 알려 주었고, 원문항 오답은 문법이 옳지만 대답과 맞지 않는 질문인데 변형 오답은 형태가 틀린 질문이라 인지 과정이 바뀌었으며 오답이 B와 같았다. 원문항 발문으로 되돌리고, 원문항처럼 문법은 옳고 대답과 맞지 않는 질문으로 유형마다 새로 썼다."
def f684(t, ans, items, a, s=S684):
    mk(6, 84, t, items, a, R684, s, st="R", p=f"A: _______________________\nB: {ans}")
f684("B", "No, they aren't.", [("Are you watching TV?", "you에 대한 질문에는 I나 we로 답하므로"), ("Is Tom reading a book?", "Tom에 대한 질문에는 he로 답하므로"), ("Are the kids sleeping?", "the kids를 they로 받아 aren't로 답할 수 있으므로"), ("Were they swimming?", "과거 질문에는 weren't로 답하므로"), ("Is it raining?", "날씨의 it에 대한 질문에는 it으로 답하므로")], 3)
f684("D", "Yes, he is.", [("Are your parents cooking?", "your parents에 대한 질문에는 they로 답하므로"), ("Is your brother taking a shower?", "your brother를 he로 받아 Yes, he is로 답할 수 있으므로"), ("Was he sleeping then?", "과거 질문에는 was로 답하므로"), ("Is the computer working?", "사물 the computer에 대한 질문에는 it으로 답하므로"), ("Are you drawing a picture?", "you에 대한 질문에는 I로 답하므로")], 2)
f684("E", "No, I am not.", [("Is she writing a letter?", "she에 대한 질문에는 she로 답하므로"), ("Are they dancing?", "they에 대한 질문에는 they로 답하므로"), ("Were you sleeping?", "과거 질문에는 wasn't로 답하므로"), ("Is the baby crying?", "the baby에 대한 질문에는 he나 she로 답하므로"), ("Are you listening to me?", "you에 대한 질문에 I am not으로 답할 수 있으므로")], 5)
f684("F", "No, it isn't.", [("Are the girls singing?", "the girls에 대한 질문에는 they로 답하므로"), ("Was it raining then?", "과거 질문에는 wasn't로 답하므로"), ("Is your dad driving?", "your dad에 대한 질문에는 he로 답하므로"), ("Is the washing machine working?", "사물 the washing machine을 it으로 받아 isn't로 답할 수 있으므로"), ("Are you eating lunch?", "you에 대한 질문에는 I로 답하므로")], 4)

# 6-85 틀린 문장: 원문항 발문, 상태동사 오류와 동작의 have를 섞어 유형마다 새로
R685 = "have(가지다), know, like, own, belong처럼 상태를 나타내는 동사는 보통 진행형으로 쓰지 않는다. 다만 have가 ‘먹다, 보내다’처럼 동작을 나타내면 진행형으로 쓸 수 있다(have lunch, have fun)."
S685 = "발문이 ‘상태동사 용법에 맞지 않는 문장’, ‘(소유·지식은 … 상태를 뜻한다.)’라고 정답 기준을 알려 주었고 오답이 B와 같았다. 원문항 발문으로 되돌리고, 원문항처럼 동작의 have(have lunch 등)를 섞어 유형마다 새로 썼다."
ACT = "동작을 나타내는 동사를 진행형으로 바르게 썼으므로"; HV = "have가 ‘먹다·보내다’라는 동작의 뜻이라 진행형으로 쓸 수 있으므로"
def f685(t, items, a, s=S685):
    mk(6, 85, t, [(x, w or ACT) for x, w in items], a, R685, s, st="R")
f685("B", [("We are having lunch now.", HV), ("The baby is sleeping in the crib.", ""), ("Tom is having a blue bag.", "‘가지고 있다’는 상태의 have는 진행형으로 쓰지 않고 Tom has로 써야 하므로"), ("They are playing tag.", ""), ("I am having fun with my friends.", HV)], 3)
f685("D", [("We are having dinner together.", HV), ("This bicycle is belonging to me.", "belong은 소유를 나타내는 상태동사라 belongs로 써야 하므로"), ("My dad is fixing the roof.", ""), ("The girls are dancing on the stage.", ""), ("The sun is shining brightly.", "")], 2)
f685("E", [("The dog is chasing a ball.", ""), ("Mom is watering the plants.", ""), ("We are having a picnic.", HV), ("Tom is washing his hands.", ""), ("I am liking this song.", "like는 좋아하는 상태를 나타내 진행형으로 쓰지 않고 I like로 써야 하므로")], 5)
f685("F", [("Jiho is brushing his teeth.", ""), ("The kids are having a snack.", HV), ("Dad is reading the news.", ""), ("They are owning a car.", "own은 소유를 나타내는 상태동사라 They own으로 써야 하므로"), ("It is getting dark.", "")], 4)

# 6-87 의문문 바꾸기: 원문항 발문, 마침표 오답 대신 원문항처럼 be동사 수 일치 오답
R687 = "현재진행형 의문문은 be동사를 주어 앞으로 옮기고 -ing형을 그대로 두어 Am/Is/Are + 주어 + -ing ~?로 쓴다. Do/Does는 쓰지 않는다."
S687 = "발문이 ‘현재진행형을 유지하여, be동사로 시작하고 물음표로 끝나는 기본형 의문문’이라고 정답 형식을 알려 주어 평서문 어순·마침표 오답이 바로 지워졌다. 원문항 발문으로 되돌리고, 마침표 오답은 원문항처럼 주어와 맞지 않는 be동사 오답으로 바꿨다."
DECL = "평서문 어순에 물음표만 붙였으므로"; DOX = "진행형 의문문은 Do가 아니라 be동사로 시작하므로"
def f687(t, items, a, s=S687):
    mk(6, 87, t, items, a, R687, s, st="R")
f687("B", [("Am I study English?", "Am 뒤에는 -ing형 studying을 그대로 써야 하므로"), ("Am I studying English?", "Am을 주어 앞으로 옮기고 studying을 그대로 두었으므로"), ("Is I studying English?", "주어 I에는 Am을 써야 하므로"), ("I am studying English?", DECL), ("Do I studying English?", DOX)], 2)
f687("C", [("Are she reading a book?", "3인칭 단수 주어 she에는 Is를 써야 하므로"), ("She is reading a book?", DECL), ("Is she reading a book?", "Is를 주어 앞으로 옮기고 reading을 그대로 두었으므로"), ("Do she reading a book?", DOX), ("Is she read a book?", "Is 뒤에는 -ing형 reading을 그대로 써야 하므로")], 3)
f687("E", [("Do they playing soccer?", DOX), ("They are playing soccer?", DECL), ("Is they playing soccer?", "복수 주어 they에는 Are를 써야 하므로"), ("Are they playing soccer?", "Are를 주어 앞으로 옮기고 playing을 그대로 두었으므로"), ("Are they play soccer?", "Are 뒤에는 -ing형 playing을 그대로 써야 하므로")], 4)
f687("F", [("Is Tom watching TV?", "Is를 주어 앞으로 옮기고 watching을 그대로 두었으므로"), ("Is Tom watch TV?", "Is 뒤에는 -ing형 watching을 그대로 써야 하므로"), ("Are Tom watching TV?", "3인칭 단수 주어 Tom에는 Is를 써야 하므로"), ("Do Tom watching TV?", DOX), ("Tom is watching TV?", DECL)], 1)

# 6-88 B·C: 원문항 발문, 주어에 밑줄이 없는 문장으로 복수 정답 방지
R688 = "현재진행형은 주어 + am/is/are + 동사원형-ing로 쓴다. I에는 am, 3인칭 단수에는 is, you와 복수 주어에는 are를 쓴다."
F(6, 88, "B", st="R", p="She ①<u>are</u> ②<u>studying</u> ③<u>in</u> ④<u>her</u> ⑤<u>room</u>.", c=["are", "studying", "in", "her", "room"], a=1, r=R688,
  n=["3인칭 단수 주어 She에는 are가 아니라 is를 써야 하므로 정답이다.", "be동사 뒤에 -ing형 studying을 바르게 썼으므로 오답이다.", "방 안을 나타내는 전치사 in을 바르게 썼으므로 오답이다.", "She를 받는 소유격 her를 바르게 썼으므로 오답이다.", "명사 room을 바르게 썼으므로 오답이다."],
  s="발문에 ‘주어의 형태는 옳다고 할 때’가 붙었다. 원문항 발문으로 되돌리고, 주어를 밑줄 없는 대명사 She로 바꿔 주어를 고치는 답이 생기지 않게 했다. 정답 위치 ①.")
F(6, 88, "C", st="R", p="I ①<u>is</u> ②<u>making</u> ③<u>a</u> ④<u>sandwich</u> ⑤<u>now</u>.", c=["is", "making", "a", "sandwich", "now"], a=1, r=R688,
  n=["주어 I에는 is가 아니라 am을 써야 하므로 정답이다.", "be동사 뒤에 -ing형 making을 바르게 썼으므로 오답이다.", "셀 수 있는 단수명사 sandwich 앞에 a를 바르게 썼으므로 오답이다.", "a 뒤에 단수명사 sandwich를 바르게 썼으므로 오답이다.", "진행형과 어울리는 now를 바르게 썼으므로 오답이다."],
  s="문장 구조(The + 복수명사 + is + -ing …)와 정답 위치가 원문항과 같았고 발문에 조건이 붙었다. 원문항 발문으로 되돌리고, 주어를 밑줄 없는 I로 바꿔 구조를 달리했다. 정답 위치 ①.")

# 6-89 (A)(B): 원문항 발문, 빈칸 밑줄과 (A)/(B) 표기
R689 = "현재진행형은 주어에 맞는 be동사와 동사원형-ing가 모두 있어야 한다."
S689 = "빈칸 밑줄이 사라지고 발문에 ‘현재진행형으로’가 붙었으며 선택지 표기가 원문항과 달랐다. 원문항 발문과 빈칸 밑줄, (A)/(B) 표기를 되살렸다. 정답은 그대로다."
BE_OK = {"I": "am", "he": "is", "she": "is", "it": "is", "we": "are", "you": "are", "they": "are"}
def f689(t, subj, verb_ing):
    V_ = V(6, 89, t)
    p = V_["passage"].replace("(A) ________ (B) ________", "(<u>    A    </u>) (<u>    B    </u>)")
    good_be = BE_OK[subj.lower()]
    c, n = [], []
    for ch in V_["c"]:
        b, v = [x.strip() for x in ch.split(" - ")]
        c.append(f"(A) {b} - (B) {v}")
        bits = []
        if b != good_be: bits.append(f"(A): 주어({subj})에 맞는 be동사({good_be})를 써야 하므로" if b in ("am", "is", "are", "were") else f"(A): 진행형에는 조동사·일반동사({b})가 아니라 be동사({good_be})를 써야 하므로")
        if v != verb_ing: bits.append(f"(B): be동사 뒤에는 -ing형({verb_ing})을 써야 하므로")
        n.append((", ".join(bits) + " 오답이다.") if bits else f"주어({subj})에 맞는 be동사({good_be})와 -ing형({verb_ing})을 바르게 짝지었으므로 정답이다.")
    F(6, 89, t, st="R", p=p, c=c, a=int(V_["ans"]), r=R689, n=n, okdup=True, s=S689)
f689("B", "We", "cleaning"); f689("C", "He", "fixing"); f689("D", "They", "decorating"); f689("E", "They", "playing"); f689("F", "You", "reading")

# 6-90 not의 역할: D~F는 오답 설명을 유형마다 새로
R690 = "현재진행형 부정문은 주어 + am/is/are + not + 동사원형-ing로 쓴다. is not은 isn't, are not은 aren't로 줄일 수 있지만 am not은 줄이지 않는다(I'm not)."
S690 = "설명 오답 네 개가 C와 똑같았다. 원문항처럼 not의 뜻·위치·축약과 don't로 바꾸는 오개념 등으로 유형마다 오답 설명을 새로 썼다."
def f690(t, items, a, s=S690):
    FIX.pop((6, 90, t), None)
    mk(6, 90, t, items, a, R690, s)
f690("D", [("not이 들어가면 playing을 play로 바꾸어 'They are not play soccer.'로 써야 한다.", "not이 있어도 be동사 뒤에는 -ing형 playing을 그대로 쓰므로"), ("주어가 They이므로 are not 대신 don't를 써서 'They don't playing soccer.'로 써도 된다.", "진행형 부정문에는 don't가 아니라 be동사 + not을 쓰므로"),
           ("'not'은 are 뒤, playing 앞에 오며 are not은 aren't로 줄여 쓸 수 있다.", "not의 위치와 축약형을 바르게 설명했으므로"), ("'not'은 '지금 ~하고 있다'는 진행의 뜻을 나타낸다.", "진행의 뜻은 are playing이 나타내고 not은 부정의 뜻이므로"),
           ("'not'은 주어 They 앞에 와서 'Not they are playing soccer.'가 된다.", "not은 주어 앞이 아니라 be동사 뒤에 오므로")], 3)
f690("E", [("'not'은 watching 뒤에 와서 'Tom is watching not TV.'로 써야 한다.", "not은 -ing형 뒤가 아니라 be동사 뒤에 오므로"), ("Tom이 3인칭 단수이므로 is not 대신 doesn't를 써도 뜻이 같다.", "진행형 부정문에는 doesn't를 쓰지 않으므로"),
           ("not을 쓰면 is를 빼고 'Tom not watching TV.'라고 써야 한다.", "진행형 부정문에서도 be동사 is는 빠지지 않으므로"), ("'not'이 is 뒤에 와서 'Tom is not watching TV.'가 되고, is not은 isn't로 줄일 수 있다.", "not의 위치와 축약형을 바르게 설명했으므로"),
           ("'not'은 TV를 부정하여 'TV가 아닌 다른 것을 보고 있다'는 뜻이다.", "not은 is watching을 부정해 ‘보고 있지 않다’는 뜻이므로")], 4)
f690("F", [("주어가 I이므로 am not은 amn't로 줄여 쓴다.", "am not은 amn't로 줄이지 않고 I'm not으로 줄이므로"), ("now가 있으므로 not은 문장 끝 now 뒤에 와야 한다.", "now가 있어도 not은 be동사 am 뒤에 오므로"),
           ("I 뒤에는 not 대신 don't를 써서 'I don't studying now.'로 써야 한다.", "진행형 부정문에는 don't가 아니라 am not을 쓰므로"), ("not 뒤에는 studying 대신 study를 써야 한다.", "not 뒤에도 진행형의 -ing형 studying을 그대로 쓰므로"),
           ("'not'은 am 뒤, studying 앞에 와서 '지금 공부하고 있지 않다'는 뜻이 된다.", "not의 위치와 뜻을 바르게 설명했으므로")], 5)


# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, s, r=R_PR, **kw):
    FIX.pop((6, n, t), None)
    mk(6, n, t, items, a, r, s, **kw)
# 6-81 F: 정답 짝(run - runing)이 C와 같음
redo(81, "F", [("write - writing", "-e로 끝나 e를 빼고 -ing를 붙인 옳은 형태이므로"), ("study - studying", "y로 끝나도 그대로 -ing를 붙인 옳은 형태이므로"), ("jog - joging", "단모음 + 단자음이라 g를 겹쳐 jogging으로 써야 하므로"), ("make - making", "-e로 끝나 e를 빼고 -ing를 붙인 옳은 형태이므로"), ("sit - sitting", "단모음 + 단자음이라 t를 겹쳐 쓴 옳은 형태이므로")], 3,
     "정답 짝(run - runing)이 C의 정답 짝과 똑같았다. 정답 짝을 다른 동사로 바꿨다. 정답 위치는 그대로다.",
     r="-ing형은 대부분 그대로 -ing를 붙이고, -e로 끝나면 e를 빼고(make → making), 단모음 + 단자음으로 끝나면 자음을 겹쳐 쓰며(cut → cutting), -ie는 y로 바꾼다(lie → lying).")
# 6-83 B·C: 정답의 짜임(Are - is ~ing)이 원문항과 같음 → 문장을 바꿔 다른 조합으로
S683 = "발문에 ‘현재진행형과 원래의 동작을 유지하면서’가 붙었고, 정답의 짜임(Are - is ~ing)이 원문항 정답(Are - is cutting)과 같았다. 원문항 발문으로 되돌리고 문장의 주어를 바꿔 정답 조합이 원문항과 다르게 했다."
redo(83, "B", [("Are - is cooking", "첫째: 주어 he에는 Is를 써야 하므로"), ("Is - is cooking", "he에 Is, Jane에 is cooking을 바르게 썼으므로"), ("Do - are cooking", "첫째: 진행형 의문문은 Do가 아니라 be동사로 시작하고, 둘째: Jane에는 is를 써야 하므로"),
     ("Is - are cooking", "둘째: 3인칭 단수 주어 Jane에는 is를 써야 하므로"), ("Are - am cooking", "첫째: he에는 Is를, 둘째: Jane에는 is를 써야 하므로")], 2, S683, st="R", p="- <u>Are</u> he running?\n- Jane <u>are cooking</u>.")
redo(83, "C", [("Are - are writing", "둘째: 주어 I에는 am을 써야 하므로"), ("Do - is write", "첫째: 진행형 의문문은 be동사로 시작하고, 둘째: am + -ing형을 써야 하므로"), ("Are - is writing", "둘째: 주어 I에는 am을 써야 하므로"),
     ("Are - am write", "둘째: be동사 뒤에는 -ing형 writing을 써야 하므로"), ("Are - am writing", "the boys에 Are, I에 am writing을 바르게 썼으므로")], 5, S683, st="R", p="- <u>Is</u> the boys playing outside?\n- I <u>is writing</u> an email.")
# 6-85 C: ⑤(I am having a great time.)가 원문항 ③(I am having a good time.)과 거의 같음
FIX.pop((6, 85, "C"), None)
mk(6, 85, "C", [("Jane is knowing the answer.", "know는 상태를 나타내는 동사라 진행형으로 쓰지 않으므로(Jane knows the answer.)"), ("Mina is preparing lunch.", "동작을 나타내는 동사를 진행형으로 바르게 썼으므로"), ("Tom is carrying a box.", "동작을 나타내는 동사를 진행형으로 바르게 썼으므로"),
    ("The children are laughing.", "동작을 나타내는 동사를 진행형으로 바르게 썼으므로"), ("Dad is having breakfast.", "have가 ‘먹다’라는 동작의 뜻이라 진행형으로 쓸 수 있으므로")], 1, R685,
   "발문이 ‘상태동사 용법에 맞지 않는 문장’, ‘(소유·지식은 … 상태를 뜻한다.)’라고 정답 기준을 알려 주었고, ⑤(I am having a great time.)가 원문항 ③(I am having a good time.)과 거의 같았다. 원문항 발문으로 되돌리고 ⑤를 다른 문장으로 바꿨다. 정답은 그대로다.", st="R")
# 6-90 B·C: 오답이 한 줄짜리 일반 규칙이고 정답만 길고 문장을 짚음 → 문장을 짚는 설명으로
S690B = "오답이 문장과 관계없는 한 줄짜리 일반 규칙이고 정답만 길게 문장을 짚어 설명해서, 길이만 보아도 답이 드러났다. 원문항처럼 not의 뜻·위치·축약에 대한, 문장을 짚는 설명으로 새로 썼다."
f690("B", [("'not'은 is 뒤, sleeping 앞에 오며 is not은 isn't로 줄여 쓸 수 있다.", "not은 be동사 뒤에 오고 is not은 isn't로 줄일 수 있으므로"), ("'not'은 now를 부정하므로 문장 끝의 now 바로 앞으로 옮겨 써야 한다.", "not은 be동사 is 뒤에 와서 문장 전체를 부정하므로"),
            ("not이 있으므로 sleeping을 과거형 slept로 바꿔야 한다.", "not이 있어도 be동사 뒤에는 -ing형을 그대로 쓰므로"), ("'not'은 '지금 ~하고 있다'는 뜻을 더 강하게 해 준다.", "not은 ‘~하고 있지 않다’는 부정의 뜻을 만들므로"),
            ("is와 not은 줄여 쓸 수 없어서 항상 'is not'으로만 써야 한다.", "is not은 isn't로 줄여 쓸 수 있으므로")], 1, S690B)
f690("C", [("'not'을 빼도 문장의 뜻은 달라지지 않는다.", "not을 빼면 ‘읽고 있다’는 긍정문이 되어 뜻이 반대가 되므로"), ("'not'은 is 뒤, reading 앞에 와서 '읽고 있지 않다'는 뜻을 만들며, is not은 isn't로 줄일 수 있다.", "not은 be동사 뒤에 오고 is not은 isn't로 줄일 수 있으므로"),
            ("'not'은 a book 앞에 와서 'She is reading not a book.'으로 써야 한다.", "not은 목적어 앞이 아니라 be동사 뒤에 오므로"), ("주어가 She이므로 not 대신 no를 써서 'She is no reading a book.'으로 쓴다.", "동사를 부정할 때는 no가 아니라 not을 쓰므로"),
            ("부정문이므로 is를 does로 바꿔 'She does not reading a book.'으로 써야 한다.", "진행형 부정문에는 does가 아니라 be동사 + not을 쓰므로")], 2, S690B)
