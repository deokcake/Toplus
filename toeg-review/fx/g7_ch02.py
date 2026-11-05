# 7급 CH2 인칭대명사·be동사·지시대명사 (11~20) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 7-12 <보기>와 관계가 다른 짝: 원문항 발문, <보기> 짝을 선택지에서 빼기
R712 = "I - me처럼 주격과 목적격을 짝지은 관계를 찾는다. he - him, she - her, we - us, they - them, you - you, it - it은 주격 - 목적격이고, mine, his, hers, ours, theirs는 소유대명사, my, its는 소유격이다."
S712 = "발문이 ‘주격과 목적격이 바르게 연결된 짝이 아닌 것’이라고 관계를 알려 주었고, <보기>와 같은 짝이 선택지에 그대로 있었다. 원문항 발문으로 되돌리고 <보기> 짝을 선택지에서 뺐다."
SO = "주격 - 목적격 관계라 <보기>와 같으므로"
def f712(t, items, a, s=S712):
    mk(7, 12, t, [(x, w or SO) for x, w in items], a, R712, s, st="R")
f712("B", [("he - him", ""), ("they - theirs", "theirs는 소유대명사라 주격 - 목적격 관계가 아니므로"), ("she - her", ""), ("we - us", ""), ("you - you", "")], 2)
f712("C", [("she - her", ""), ("you - you", ""), ("they - them", ""), ("he - his", "his는 소유격(소유대명사)이라 주격 - 목적격 관계가 아니므로"), ("we - us", "")], 4)
f712("D", [("she - her", ""), ("he - him", ""), ("it - it", ""), ("they - them", ""), ("we - ours", "ours는 소유대명사라 주격 - 목적격 관계가 아니므로")], 5)
f712("E", [("we - us", ""), ("she - her", ""), ("he - him", ""), ("it - its", "its는 소유격이라 주격 - 목적격 관계가 아니므로"), ("they - them", "")], 4)
f712("F", [("you - you", ""), ("I - mine", "mine은 소유대명사라 주격 - 목적격 관계가 아니므로"), ("we - us", ""), ("she - her", ""), ("he - him", "")], 2,
     "발문이 ‘주격과 목적격이 바르게 연결된 짝이 아닌 것’이라고 관계를 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 7-13 대명사로 바꿔 쓰기: 원문항 발문과 밑줄, 성별은 발문 괄호로
R713 = "나를 포함한 여럿은 we, 나를 포함하지 않은 여럿은 they, 남자 한 명은 he, 여자 한 명은 she로 바꾸고, 소유를 나타내는 Tom's는 his, Kelly's는 her로 바꾼다."
S713 = "원문항의 밑줄이 사라지고, 발문에 ‘말하는 사람이 바뀌지 않을 때’ 조건과 ‘등장인물 설정’ 제시문이 붙었다. 원문항 발문과 밑줄로 되돌리고, 성별 정보는 원문항처럼 발문 괄호에 넣었다. 보기와 정답은 그대로다."
ST713 = lambda g: f"밑줄 친 부분을 대명사를 사용해 바꿔 쓴 문장이 옳지 않은 것을 고르시오. (단, {g})"
def f713(t, g, items, a):
    mk(7, 13, t, items, a, R713, S713, st=ST713(g), p="")
U = lambda a_, b_, rest: f"<u>{a_}</u> {rest} → <u>{b_}</u> {rest}"
f713("B", "Tom은 남자, Amy·Jane·Kelly는 여자", [(U("My brother and I", "They", "are students."), "나를 포함한 여럿은 They가 아니라 We로 바꿔야 하므로"), (U("Tom", "He", "is tall."), "남자 한 명 Tom을 He로 바르게 바꿨으므로"), (U("My sister and I", "We", "are happy."), "나를 포함한 여럿을 We로 바르게 바꿨으므로"),
     (U("Jane and Amy", "They", "are friends."), "나를 포함하지 않은 여럿을 They로 바르게 바꿨으므로"), ("<u>Kelly's</u> pen is new. → <u>Her</u> pen is new.", "여자 Kelly의 소유를 Her로 바르게 바꿨으므로")], 1)
f713("C", "Ben·Leo·Tom은 남자, Jane은 여자", [(U("Ben and Leo", "They", "are here."), "나를 포함하지 않은 여럿을 They로 바르게 바꿨으므로"), ("<u>Jane's</u> cat is small. → <u>Her</u> cat is small.", "여자 Jane의 소유를 Her로 바르게 바꿨으므로"), (U("Tom", "He", "is my friend."), "남자 한 명 Tom을 He로 바르게 바꿨으므로"),
     ("<u>Ben's</u> dog is cute. → <u>Her</u> dog is cute.", "남자 Ben의 소유는 Her가 아니라 His로 바꿔야 하므로"), (U("My cousin and I", "We", "are hungry."), "나를 포함한 여럿을 We로 바르게 바꿨으므로")], 4)
f713("D", "Ben·Leo·Tom은 남자, Jane·Kelly·Mina는 여자", [("<u>Leo's</u> cap is red. → <u>His</u> cap is red.", "남자 Leo의 소유를 His로 바르게 바꿨으므로"), (U("Jane and Mina", "We", "are sisters."), "나를 포함하지 않은 여럿은 We가 아니라 They로 바꿔야 하므로"), (U("Tom and Ben", "They", "are friends."), "나를 포함하지 않은 여럿을 They로 바르게 바꿨으므로"),
     (U("Kelly", "She", "is a nurse."), "여자 한 명 Kelly를 She로 바르게 바꿨으므로"), (U("My dad and I", "We", "are here."), "나를 포함한 여럿을 We로 바르게 바꿨으므로")], 2)
f713("E", "Ben·Sam·Tom은 남자, Jane은 여자", [(U("My father", "She", "is tall."), "남자 한 명인 My father는 She가 아니라 He로 바꿔야 하므로"), (U("My mother", "She", "is nice."), "여자 한 명인 My mother를 She로 바르게 바꿨으므로"), ("<u>Jane's</u> book is new. → <u>Her</u> book is new.", "여자 Jane의 소유를 Her로 바르게 바꿨으므로"),
     (U("Ben and Sam", "They", "are brothers."), "나를 포함하지 않은 여럿을 They로 바르게 바꿨으므로"), (U("Tom and I", "We", "are students."), "나를 포함한 여럿을 We로 바르게 바꿨으므로")], 1)
f713("F", "Ben·David·Leo는 남자, Jane·Mina는 여자", [(U("Jane and I", "They", "are partners."), "나를 포함한 여럿은 They가 아니라 We로 바꿔야 하므로"), (U("My sister and I", "We", "are ready."), "나를 포함한 여럿을 We로 바르게 바꿨으므로"), ("<u>David's</u> bike is blue. → <u>His</u> bike is blue.", "남자 David의 소유를 His로 바르게 바꿨으므로"),
     (U("Leo and Ben", "They", "are cousins."), "나를 포함하지 않은 여럿을 They로 바르게 바꿨으므로"), (U("Mina", "She", "is my aunt."), "여자 한 명 Mina를 She로 바르게 바꿨으므로")], 1)

# 7-14 소유격으로 대신하기: 원문항 발문과 밑줄
R714 = "명사 + ’s는 소유격 대명사로 바꾼다. 남자 한 명은 his, 여자 한 명은 her, 여럿은 their, 나를 포함한 여럿은 our이다."
S714 = "원문항 밑줄이 사라지고 발문이 ‘○○를 대신할 소유격’, ‘(○○를 가리킵니다.)’로 길어졌다. 원문항 발문과 밑줄로 되돌렸다. 보기와 정답은 그대로다."
ST714 = lambda g="": "다음 밑줄 친 부분을 대신할 말로 알맞은 것을 고르시오." + (f" (단, {g})" if g else "")
def f714(t, p, g, items, a):
    mk(7, 14, t, items, a, R714, S714, st=ST714(g), p=p)
f714("B", "This is <u>my parents'</u> car.", "", [("their", "부모님 두 분의 소유는 their로 바꾸므로"), ("his", "his는 남자 한 명의 소유이므로"), ("our", "our는 나를 포함한 여럿의 소유이므로"), ("my", "my는 나의 소유이므로"), ("her", "her는 여자 한 명의 소유이므로")], 1)
f714("C", "The dog is <u>Tom and Jane's</u> pet.", "", [("our", "our는 나를 포함한 여럿의 소유이므로"), ("his", "his는 남자 한 명의 소유이므로"), ("their", "Tom과 Jane 두 사람의 소유는 their로 바꾸므로"), ("her", "her는 여자 한 명의 소유이므로"), ("my", "my는 나의 소유이므로")], 3)
f714("D", "Mina is <u>Leo's</u> sister.", "Leo는 남자, Mina는 여자", [("its", "its는 사물·동물의 소유이므로"), ("our", "our는 나를 포함한 여럿의 소유이므로"), ("her", "Leo는 남자라 her로 바꿀 수 없으므로"), ("his", "남자 Leo의 소유는 his로 바꾸므로"), ("their", "their는 여럿의 소유이므로")], 4)
f714("E", "Jane is <u>Ben's</u> friend.", "Ben은 남자, Jane은 여자", [("her", "Ben은 남자라 her로 바꿀 수 없으므로"), ("his", "남자 Ben의 소유는 his로 바꾸므로"), ("our", "our는 나를 포함한 여럿의 소유이므로"), ("their", "their는 여럿의 소유이므로"), ("my", "my는 나의 소유이므로")], 2)
f714("F", "That is <u>my sister's</u> bag.", "", [("his", "his는 남자 한 명의 소유이므로"), ("my", "my는 나의 소유라 누나(언니)의 소유를 나타내지 못하므로"), ("our", "our는 나를 포함한 여럿의 소유이므로"), ("their", "their는 여럿의 소유이므로"), ("her", "여자 한 명인 my sister의 소유는 her로 바꾸므로")], 5)

# 7-15 (A)(B) 주격·소유격: 원문항처럼 문장별 우리말 해석
R715 = "문장의 주어 자리에는 주격(I, we, she, they)을, 명사 앞에는 소유격(my, our, her, their)을 쓴다."
S715 = "원문항의 문장별 우리말 해석이 빠졌다. 원문항처럼 우리말 해석을 붙였다. 보기와 정답은 그대로다."
def f715(t, p, subj, poss):
    V_ = V(7, 15, t); items = []
    for ch in V_["c"]:
        a_, b_ = [x.split(") ", 1)[1].strip() for x in ch.split(" - ")]
        bits = []
        if a_ != subj: bits.append(f"(A): 주어 자리에는 주격({subj})을 쓰므로")
        if b_ != poss: bits.append(f"(B): 명사 앞에는 소유격({poss})을 쓰므로")
        items.append((ch, ", ".join(bits) if bits else "(A)에 주격, (B)에 소유격을 바르게 썼으므로"))
    mk(7, 15, t, items, int(V_["ans"]), R715, S715, p=p, okdup=True)
f715("B", "(A) ________ are friends. (우리는 친구이다.)\n(B) ________ room is nice. (우리의 방은 멋지다.)", "We", "Our")
f715("C", "(A) ________ am a student. (나는 학생이다.)\n(B) ________ pencil is nice. (나의 연필은 멋지다.)", "I", "My")
f715("E", "(A) ________ is a teacher. (그녀는 선생님이다.)\n(B) ________ book is nice. (그녀의 책은 멋지다.)", "She", "Her")
f715("F", "(A) ________ are students. (그들은 학생이다.)\n(B) ________ bags are nice. (그들의 가방은 멋지다.)", "They", "Their")

# 7-16 be동사 빈칸: 원문항 발문, 원문항처럼 현재임을 알려 주는 둘째 문장
R716 = "현재형 be동사는 주어가 I면 am, 3인칭 단수(he, she, 사람 한 명)면 is, you·we·they면 are를 쓴다. 뒤 문장이 현재형이면 과거형 was는 쓰지 않는다."
S716 = "발문에 ‘현재형 be동사’가 붙었다. 원문항 발문으로 되돌리고, 원문항처럼 현재임을 알려 주는 둘째 문장을 붙였다."
def f716(t, p, items, a, s=S716 + " 보기와 정답은 그대로다."):
    mk(7, 16, t, items, a, R716, s, st="R", p=p)
WAS = "was는 과거형이라 현재의 일을 말하는 둘째 문장과 맞지 않으므로"; BE0 = "be는 원형이라 주어 뒤에 그대로 쓸 수 없으므로"
f716("B", "Tom _______ tired. He wants to sleep now.", [("is", "3인칭 단수 주어 Tom에 맞는 현재형이므로"), ("are", "are는 you·복수 주어에 쓰므로"), ("be", BE0), ("am", "am은 주어 I에만 쓰므로"), ("was", WAS)], 1)
f716("C", "She _______ happy. She likes her new bag.", [("am", "am은 주어 I에만 쓰므로"), ("is", "3인칭 단수 주어 She에 맞는 현재형이므로"), ("are", "are는 you·복수 주어에 쓰므로"), ("be", BE0), ("was", WAS)], 2)
f716("D", "Mina _______ ready for the science class. She has her book now.", [("are", "are는 you·복수 주어에 쓰므로"), ("were", "were는 과거형이고 복수 주어에 쓰므로"), ("is", "3인칭 단수 주어 Mina에 맞는 현재형이므로"), ("be", BE0), ("am", "am은 주어 I에만 쓰므로")], 3,
     S716 + " 주어(I)와 정답(am)이 원문항과 같아 주어를 Mina로 바꿨다.")
f716("E", "They _______ hungry. They want some pizza.", [("be", BE0), ("are", "주어 They에 맞는 현재형이므로"), ("was", WAS), ("is", "is는 3인칭 단수 주어에 쓰므로"), ("am", "am은 주어 I에만 쓰므로")], 2)
f716("F", "We _______ ready. Let's go now.", [("are", "주어 We에 맞는 현재형이므로"), ("is", "is는 3인칭 단수 주어에 쓰므로"), ("be", BE0), ("am", "am은 주어 I에만 쓰므로"), ("was", WAS)], 1)

# 7-17 지시대명사·인칭대명사: C·E는 설명 삭제, D는 원문항과 다른 정답
R717 = "‘이것들(가까운 여럿)’은 these, ‘저것들(먼 여럿)’은 those, ‘그것들(앞에서 말한 여럿)’은 they, ‘이것(가까운 하나)’은 this, ‘저것(먼 하나)’은 that으로 쓴다."
def f717(t, p, items, a, s):
    mk(7, 17, t, items, a, R717, s, p=p)
TH = {"This": "‘이것(가까운 하나)’을 가리키므로", "That": "‘저것(먼 하나)’을 가리키므로", "These": "‘이것들(가까운 여럿)’을 가리키므로", "Those": "‘저것들(먼 여럿)’을 가리키므로", "They": "‘그것들’을 가리키므로"}
def opts717(order, ans_word):
    return [(w, TH[w] + (" 우리말과 맞으므로" if w == ans_word else " 우리말과 맞지 않으므로")) for w in order]
f717("C", "그것들은 내 장난감들이 아니야.\n→ _______ aren't my toys.", opts717(["They", "That", "This", "These", "Those"], "They"), 1, "제시문에 ‘※ 앞에서 말한 사물들을 인칭대명사로 받으며 …’ 설명이 붙었다. 우리말 ‘그것들’만으로 충분하므로 설명을 지웠다. 보기와 정답은 그대로다.")
f717("E", "그것들은 내 신발들이 아니야.\n→ _______ aren't my shoes.", opts717(["Those", "They", "This", "That", "These"], "They"), 2, "제시문에 ‘※ …’ 설명이 붙었다. 우리말 ‘그것들’만으로 충분하므로 설명을 지웠다. 보기와 정답은 그대로다.")
f717("D", "이것은 내 사과가 아니야.\n→ _______ isn't my apple.", opts717(["These", "This", "They", "Those", "That"], "This"), 2, "정답(These)과 우리말 구조(이것들은 내 ○○들이 아니야)가 원문항과 같았다. 가까운 하나를 가리키는 문장으로 바꿔 정답이 This가 되게 했다.")

# 7-18 be동사 대화: 원문항 발문, D는 C와 다른 대화
R718 = "be동사 의문문은 Am/Is/Are + 주어 ~?로 묻고, 대답의 be동사도 대답의 주어에 맞춘다(you → I am, I → you are)."
S718 = "발문에 ‘현재형으로 대화를 완성할 때’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def f718(t, good, why, a=None, p=None, c=None, s=S718):
    V_ = V(7, 18, t); cs = c or V_["c"]; gs = [x.strip() for x in good.split(" - ")]
    items = []
    for ch in cs:
        xs = [x.strip() for x in ch.split(" - ")]
        if xs == gs: items.append((ch, "질문과 대답의 주어에 맞는 be동사를 바르게 썼으므로")); continue
        bits = [f"{['첫째', '둘째'][i]} 빈칸 {x}: {why[i]}" for i, (x, g) in enumerate(zip(xs, gs)) if x != g]
        items.append((ch, ". ".join(bits) + ". 따라서"))
    kw = {"p": p} if p else {}
    mk(7, 18, t, items, a or int(V_["ans"]), R718, s, st="R", okdup=True, **kw)
f718("B", "Are - are", ["복수 주어 the books에는 Are를 쓴다", "Yes 대답의 they에는 are를 쓴다"])
f718("C", "Are - am", ["주어 you에는 Are를 쓴다", "Yes 대답의 I에는 am을 쓴다"])
f718("E", "Are - aren't", ["복수 주어 the boys에는 Are를 쓴다", "No 대답의 they에는 aren't를 쓴다"])
f718("F", "Is - is", ["3인칭 단수 주어 Jane에는 Is를 쓴다", "Yes 대답의 she에는 is를 쓴다"])
f718("D", "Am - aren't", ["주어 I에는 Am을 쓴다", "No 대답의 you에는 aren't를 쓴다"], a=1, p="A: _______ I late?\nB: No, you _______.", c=["Am - aren't", "Is - isn't", "Are - am not", "Am - am not", "Are - aren't"],
     s="대화(Are you ready …? - Yes, I am.)가 C와 거의 같았고 발문에 조건이 붙었다. 원문항 발문으로 되돌리고 주어 I를 묻는 대화로 바꿨다.")

# 7-19 고쳐야 하는 이유: 밑줄 복원, C·E·F는 학생 수준의 그럴듯한 오해로 오답 새로
R719 = "be동사는 주어에 맞춰 고른다. I는 am, 3인칭 단수(he, she, 사람 한 명)는 is, you·we·they와 A and B 같은 복수 주어는 are를 쓴다."
UL = lambda p, w: p.replace(f"민수: {w} ", f"민수: <u>{w}</u> ", 1)
N719 = {"B": ["be동사는 뒤의 형용사가 아니라 주어에 맞춰 고르므로 오답이다.", "3인칭 단수 주어 she에는 Is를 쓰므로 정답이다.", "대문자 규칙은 be동사를 고르는 기준이 아니므로 오답이다.", "의문문도 주어에 따라 Am/Is/Are를 고르므로 오답이다.", "의문문에서도 주어를 보고 be동사를 고르므로 오답이다."],
        "D": ["의문문도 주어에 따라 Am/Is/Are를 고르므로 오답이다.", "be동사는 뒤의 장소가 아니라 주어에 맞춰 고르므로 오답이다.", "복수 주어 the children에는 Are를 쓰므로 정답이다.", "첫소리는 be동사를 고르는 기준이 아니므로 오답이다.", "문장의 길이는 be동사를 고르는 기준이 아니므로 오답이다."]}
for t, w in [("B", "Are"), ("D", "Is")]:
    F(7, 19, t, p=UL(V(7, 19, t)["passage"], w), s="원문항의 밑줄이 사라졌다. 고칠 be동사에 밑줄을 되살렸다. 보기와 정답은 그대로다.", r=R719, n=N719[t])
S719 = "원문항 오답은 학생 수준의 그럴듯한 오해인데, 변형 오답(‘의문문은 항상 Are로 시작’, ‘뒤에 형용사가 오면 정해지는 규칙’ 등)이 B와 똑같았고 밑줄도 사라졌다. 밑줄을 되살리고 유형마다 그럴듯한 오해로 오답을 새로 썼다."
def f719(t, p, items, a, s=S719, **kw):
    mk(7, 19, t, items, a, R719, s, p=p, **kw)
f719("C", "민수: <u>Is</u> Tom and Ben ready?\n지수: Is를 Are로 바꿔야 해.", [("Tom과 Ben이 모두 사람 이름이라 Are를 써야 하기 때문이다.", "사람 이름이라서가 아니라 두 사람(복수)이라서 Are를 쓰므로"), ("ready가 형용사라서 형용사 앞에는 Are를 써야 하기 때문이다.", "be동사는 뒤의 형용사가 아니라 주어에 맞춰 고르므로"),
     ("and로 두 사람을 이어 여러 명(복수)이 되었으므로 주어에 맞는 Are를 써야 하기 때문이다.", "A and B 주어는 복수라 Are를 쓰므로"), ("Is 뒤에는 한 사람 이름만 올 수 있기 때문이다.", "Is는 3인칭 단수 주어와 쓰는 것이지 ‘이름 하나’로 정해지는 규칙이 아니므로"),
     ("묻는 문장에서는 첫 글자를 A로 시작해야 하기 때문이다.", "의문문도 주어에 따라 Am/Is/Are 중에서 고르므로")], 3)
f719("E", "민수: <u>Is</u> we ready?\n지수: Is를 Are로 바꿔야 해.", [("we는 '우리'라는 여러 명을 나타내는 주어이므로 짝꿍인 Are를 써야 하기 때문이다.", "주어 we는 복수라 Are를 쓰므로"), ("we가 소문자로 시작하기 때문이다.", "대소문자는 be동사를 고르는 기준이 아니므로"),
     ("ready 뒤에 물음표가 있기 때문이다.", "물음표는 be동사를 고르는 기준이 아니므로"), ("'우리'에는 나(I)가 들어 있어서 I와 같은 Are를 쓰기 때문이다.", "I에는 Are가 아니라 am을 쓰고, we는 복수라 Are를 쓰므로"),
     ("Is는 과거형이라 현재 문장에는 쓸 수 없기 때문이다.", "Is는 과거형이 아니라 현재형이므로")], 1)
f719("F", "민수: <u>Is</u> I ready?\n지수: Is를 Am으로 바꿔야 해.", [("I는 대문자로 쓰는 단어라 Am을 써야 하기 때문이다.", "대문자로 쓰는 것은 be동사를 고르는 기준이 아니므로"), ("의문문에서는 주어가 한 명이면 항상 Am을 쓰기 때문이다.", "한 명이라도 he, she에는 Is를 쓰므로"),
     ("ready가 '준비된'이라는 뜻이라 Am과 어울리기 때문이다.", "be동사는 뒤의 말이 아니라 주어에 맞춰 고르므로"), ("주어 I에 짝이 맞는 be동사는 Am이기 때문이다.", "주어 I에는 am을 쓰므로"), ("Is는 3인칭 복수 주어에만 쓰기 때문이다.", "Is는 3인칭 단수 주어에 쓰므로")], 4)

# 7-20 틀린 문장을 말한 학생: 원문항 발문과 학생 대사 형식, 유형마다 새로
R720 = "this·that은 한 개, these·those는 여러 개를 가리킨다. these/those 뒤에는 are와 복수 명사를, this/that 뒤에는 is와 단수 명사를 쓴다."
S720 = "원문항의 학생 이름 대사 형식이 이름 없는 문장 나열로 바뀌었고 오답 네 개가 B와 똑같았으며 발문도 달랐다. 원문항 발문과 학생 대사 형식으로 되돌리고 유형마다 새로 썼다."
OK20 = "지시 표현, be동사, 명사의 수가 모두 맞으므로"; TEA = "선생님의 칭찬으로 어법상 틀린 곳이 없으므로"
def f720(t, items, a, s=S720, **kw):
    mk(7, 20, t, [(x, w or OK20) for x, w in items], a, R720, s, st="R", **kw)
f720("B", [("수아: These are her dolls.", ""), ("민호: These are my box.", "These 뒤에는 복수 명사 boxes를 써야 하므로"), ("지우: Those are my boxes.", ""), ("태호: Those are his cars.", ""), ("선생님: Good! You know 'these' and 'those' well.", TEA)], 2)
f720("C", [("유리: This is my pencil case.", ""), ("민아: Those are our chairs.", ""), ("지호: These is my books.", "These 뒤에는 is가 아니라 are를 써야 하므로"), ("준수: That is her bike.", ""), ("선생님: Well done, everyone!", TEA)], 3)
f720("D", [("하린: These are new shoes.", ""), ("서준: That is my cat.", ""), ("예은: This is his umbrella.", ""), ("도윤: Those are her doll.", "Those 뒤에는 복수 명사 dolls를 써야 하므로"), ("선생님: Nice work!", TEA)], 4)
f720("E", [("수아: These are our tickets.", ""), ("태호: Those are tall buildings.", ""), ("준: Those are her gloves.", ""), ("유나: These are fresh strawberries.", ""), ("민지: These is my notebooks.", "These 뒤에는 is가 아니라 are를 써야 하므로")], 5,
     "발문이 ‘지시 표현과 수가 맞지 않는 문장’으로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f720("F", [("현우: Those am your cars.", "Those 뒤에는 am이 아니라 are를 써야 하므로"), ("소연: This is my room.", ""), ("재민: These are big apples.", ""), ("다은: That is our teacher.", ""), ("선생님: Very good!", TEA)], 1)


# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, r, s, **kw):
    FIX.pop((7, n, t), None)
    mk(7, n, t, items, a, r, s, **kw)
# 7-11 B·C·E·F: 같은 우리말 뜻이 두 보기에 나와 둘 중 하나가 답이 됨(B 그녀는, C 그는, E 우리를, F 그들은), B·F는 원문항과 같은 짝도 있음
R711 = "주격(I, he, she, we, they)은 ‘~은/는’, 소유격(my, his, her, our, their, its)은 ‘~의’, 목적격(me, him, her, us, them)은 ‘~을/를’로 옮긴다."
OK11 = lambda en, ko: f"{en}: ‘{ko}’로 바르게 옮겼으므로"
def f711(t, items, a, s):
    redo(11, t, [(f"{en} - {ko}", why or OK11(en, ko)) for en, ko, why in items], a, R711, s)
f711("B", [("your", "너의", ""), ("she", "그녀는", ""), ("his", "그의", ""), ("me", "나는", "me는 목적격이라 ‘나를’로 옮겨야 하므로"), ("they", "그들은", "")], 4,
     "‘그녀는’이 ②와 ④에 두 번 나와 둘 중 하나가 답이라는 단서가 되었고, 정답(her - 그녀는)은 원문항 ④(her - 그녀의)의 틀린 꼴, ①(our - 우리의)은 원문항 ①과 똑같았다. 정답 짝과 겹치는 짝을 바꿨다. 정답 위치는 그대로다.")
f711("C", [("my", "나의", ""), ("we", "우리는", ""), ("she", "그녀는", ""), ("his", "그는", "his는 소유격이라 ‘그의’로 옮겨야 하므로"), ("their", "그들의", "")], 4,
     "‘그는’이 ③(he - 그는)과 ④(his - 그는)에 두 번 나와 둘 중 하나가 답이라는 단서가 되었다. ③을 다른 대명사로 바꿨다. 정답은 그대로다.")
f711("E", [("your", "너의", ""), ("its", "그것의", ""), ("our", "우리를", "our는 소유격이라 ‘우리의’로 옮겨야 하므로"), ("she", "그녀는", ""), ("them", "그들을", "")], 3,
     "‘우리를’이 ③(our - 우리를)과 ⑤(us - 우리를)에 두 번 나와 둘 중 하나가 답이라는 단서가 되었다. ⑤를 다른 대명사로 바꿨다. 정답은 그대로다.")
f711("F", [("their", "그들은", "their는 소유격이라 ‘그들의’로 옮겨야 하므로"), ("him", "그를", ""), ("we", "우리는", ""), ("my", "나의", ""), ("us", "우리를", "")], 1,
     "‘그들은’이 ①(their - 그들은)과 ③(they - 그들은)에 두 번 나와 둘 중 하나가 답이라는 단서가 되었고, ④·⑤(her - 그녀의, our - 우리의)는 원문항과 똑같은 짝이었다. 세 짝을 다른 대명사로 바꿨다. 정답은 그대로다.")
# 7-13 B·E·F: 같은 짜임의 옳은 문장·틀린 문장이 함께 있음(My brother/sister and I, My father/mother, Jane/My sister and I), B·F는 틀린 꼴이 원문항과 같은 종류·위치
S713B = "원문항의 밑줄이 사라지고 발문과 제시문이 달라졌으며, 틀린 문장과 짜임이 같은 옳은 문장(%s)이 함께 있어 둘만 견주면 답이 나왔다. 원문항 발문과 밑줄로 되돌리고 짝 문장을 다른 문장으로 바꿨다."
def g713(t, g, items, a, s):
    FIX.pop((7, 13, t), None)
    mk(7, 13, t, items, a, R713, s, st=ST713(g), p="")
g713("B", "Tom은 남자, Amy·Jane·Kelly는 여자", [(U("Tom", "He", "is tall."), "남자 한 명 Tom을 He로 바르게 바꿨으므로"), (U("My dog", "It", "is cute."), "동물 한 마리를 It으로 바르게 바꿨으므로"), (U("My brother and I", "They", "are students."), "나를 포함한 여럿은 They가 아니라 We로 바꿔야 하므로"),
     (U("Jane and Amy", "They", "are friends."), "나를 포함하지 않은 여럿을 They로 바르게 바꿨으므로"), ("<u>Kelly's</u> pen is new. → <u>Her</u> pen is new.", "여자 Kelly의 소유를 Her로 바르게 바꿨으므로")], 3,
     S713B % "My sister and I → We" + " 정답 위치도 원문항(①)과 다르게 옮겼다.")
g713("E", "Ben·Sam·Tom은 남자, Jane은 여자", [(U("My father", "She", "is tall."), "아버지는 남자라 She가 아니라 He로 바꿔야 하므로"), (U("My puppy", "It", "is small."), "동물 한 마리를 It으로 바르게 바꿨으므로"), ("<u>Jane's</u> book is new. → <u>Her</u> book is new.", "여자 Jane의 소유를 Her로 바르게 바꿨으므로"),
     (U("Ben and Sam", "They", "are brothers."), "나를 포함하지 않은 여럿을 They로 바르게 바꿨으므로"), (U("Tom and I", "We", "are students."), "나를 포함한 여럿을 We로 바르게 바꿨으므로")], 1, S713B % "My mother → She")
g713("F", "Ben·David·Leo는 남자, Jane·Mina는 여자", [(U("Jane and I", "We", "are partners."), "나를 포함한 여럿을 We로 바르게 바꿨으므로"), ("<u>David's</u> bike is blue. → <u>His</u> bike is blue.", "남자 David의 소유를 His로 바르게 바꿨으므로"), (U("Leo and Ben", "They", "are cousins."), "나를 포함하지 않은 여럿을 They로 바르게 바꿨으므로"),
     (U("Mina", "She", "is my aunt."), "여자 한 명 Mina를 She로 바르게 바꿨으므로"), (U("You and your brother", "They", "are late."), "너를 포함한 여럿은 They가 아니라 You로 바꿔야 하므로")], 5,
     S713B % "My sister and I → We" + " 틀린 꼴(~ and I → They)과 위치(①)가 B와 같아 다른 종류의 오류로 바꿨다.")
# 7-14 E: 문장의 짜임(X is Y's Z)과 정답(his)이 D와 같음 → its
FIX.pop((7, 14, "E"), None)
mk(7, 14, "E", [("her", "her는 여자 한 명의 소유이므로"), ("its", "동물 한 마리(the bird)의 소유는 its로 바꾸므로"), ("our", "our는 나를 포함한 여럿의 소유이므로"), ("their", "their는 여럿의 소유이므로"), ("my", "my는 나의 소유이므로")], 2, R714 + " 사물·동물 하나는 its다.",
   "원문항 밑줄이 사라지고 발문이 길어졌으며, 문장의 짜임(Jane is Ben's friend.)과 정답(his)이 D(Mina is Leo's sister. — his)와 같았다. 원문항 발문과 밑줄로 되돌리고 문장을 바꿔 정답이 its가 되게 했다.", st=ST714(), p="The <u>bird's</u> nest is in the tree.")
# 7-15 E: 정답(She - Her)이 D와 같음 → You - Your
FIX.pop((7, 15, "E"), None)
mk(7, 15, "E", [("(A) Your - (B) Your", "(A): 주어 자리에는 주격(You)을 쓰므로"), ("(A) You - (B) Your", "주어 자리에 주격 You, 명사 앞에 소유격 Your를 바르게 썼으므로"), ("(A) Your - (B) You", "(A): 주어 자리에는 주격(You)을, (B): 명사 앞에는 소유격(Your)을 쓰므로"),
    ("(A) You - (B) You", "(B): 명사 앞에는 소유격(Your)을 쓰므로"), ("(A) Him - (B) Your", "(A): 주어 자리에는 주격(You)을 쓰므로")], 2, R715,
   "원문항의 문장별 우리말 해석이 빠졌고, 정답(She - Her)이 D와 같았다. 우리말 해석을 붙이고 대명사를 바꿔 정답이 You - Your가 되게 했다.", st="R",
   p="(A) ________ are my friend. (너는 내 친구이다.)\n(B) ________ bag is nice. (너의 가방은 멋지다.)")
# 7-17 E: 정답(They)이 C와 같음 → That / F: 정답(Those)이 B와 같음 → It
TH2 = dict(TH); TH2["It"] = "‘그것(앞에서 말한 하나)’을 가리키므로"
def o717(order, ans_word): return [(w, TH2[w] + (" 우리말과 맞으므로" if w == ans_word else " 우리말과 맞지 않으므로")) for w in order]
FIX.pop((7, 17, "E"), None); FIX.pop((7, 17, "F"), None)
f717("E", "저것은 내 우산이 아니야.\n→ _______ isn't my umbrella.", o717(["Those", "They", "This", "That", "These"], "That"), 4, "제시문에 ‘※ …’ 설명이 붙었고, 우리말(그것들은 내 ○○들이 아니야)과 정답(They)이 C와 같았다. 설명을 지우고 먼 하나를 가리키는 문장으로 바꿔 정답이 That이 되게 했다.")
f717("F", "그것은 내 가방이 아니야.\n→ _______ isn't my bag.", o717(["That", "It", "These", "This", "They"], "It"), 2, "우리말(저것들은 내 ○○들이 아니야)과 정답(Those)이 B와 같았다. 앞에서 말한 하나를 가리키는 문장으로 바꿔 정답이 It이 되게 했다.")
# 7-19 B: 오답이 한 줄짜리 일반 규칙이고 정답만 문장의 주어(she)를 말함 → 학생 수준의 그럴듯한 오해로
FIX.pop((7, 19, "B"), None)
f719("B", "민수: <u>Are</u> she ready?\n지수: Are를 Is로 바꿔야 해.", [("she는 여자를 가리키는 말이라 Is를 써야 하기 때문이다.", "be동사는 성별이 아니라 인칭과 수로 정하므로"), ("묻는 문장에서는 Are를 쓸 수 없기 때문이다.", "의문문에서도 주어에 따라 Are를 쓰므로"),
     ("Are는 문장 가운데에만 쓸 수 있기 때문이다.", "Are도 의문문의 맨 앞에 올 수 있으므로"), ("주어 she는 나나 너가 아닌 한 사람이라 짝이 맞는 Is를 써야 하기 때문이다.", "3인칭 단수 주어 she에는 Is를 쓰므로"),
     ("ready라는 말은 Is와만 함께 쓸 수 있기 때문이다.", "be동사는 뒤의 말이 아니라 주어에 맞춰 고르므로")], 4,
     "원문항의 밑줄이 사라졌고, 오답이 문장과 관계없는 일반 규칙이어서 정답만 문장의 주어(she)를 말해 눈에 띄었으며 C·E·F가 이 오답을 되풀이했다. 밑줄을 되살리고 학생 수준의 그럴듯한 오해로 오답을 새로 썼다.")
# 7-20 B: 두 문장이 원문항과 똑같음(Those are my boxes. / Those are his cars.) / C: 틀린 문장(These is my books)이 E와 거의 같음
FIX.pop((7, 20, "B"), None); FIX.pop((7, 20, "C"), None)
f720("B", [("수아: These are my crayons.", ""), ("민호: These are my box.", "These 뒤에는 복수 명사 boxes를 써야 하므로"), ("지우: Those are your shoes.", ""), ("태호: Those are our kites.", ""), ("선생님: Good! You know 'these' and 'those' well.", TEA)], 2,
     S720 + " 원문항과 똑같던 문장(Those are my boxes. / Those are his cars.)도 바꿨다.")
f720("C", [("유리: This is my pencil case.", ""), ("민아: Those are our chairs.", ""), ("지호: This are my books.", "여러 권(books)이므로 This가 아니라 These를 써야 하므로"), ("준수: That is her bike.", ""), ("선생님: Well done, everyone!", TEA)], 3,
     S720 + " 틀린 문장도 E(These is my notebooks.)와 겹치지 않게 바꿨다.")
