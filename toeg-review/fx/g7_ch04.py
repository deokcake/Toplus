# 7급 CH4 be동사 부정문·의문문 (31~40) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
R_BN = "be동사 부정문은 be동사 뒤에 not을 붙인다(am not, is not/isn't, are not/aren't). 의문문은 be동사를 주어 앞에 두고, 대답의 be동사도 주어에 맞춘다. be동사는 I에 am, 3인칭 단수에 is, you·복수에 are를 쓴다."
BEX = {"am": "주어 I에 쓰는", "is": "3인칭 단수 주어에 쓰는", "are": "you·복수 주어에 쓰는"}

# 7-31 부정형 빈칸: 원문항 발문, E는 우리말 다듬기
S731 = "발문에 ‘현재형 be동사의 부정형을’이 붙어 긍정형 오답이 바로 지워졌다. 원문항 발문으로 되돌렸다."
def f731(t, subj, good, p=None, s=S731 + " 보기와 정답은 그대로다."):
    V_ = V(7, 31, t); items = []
    for o in V_["c"]:
        if o == good: items.append((o, f"주어({subj})에 맞는 부정형이라 우리말과 맞으므로"))
        elif o in ("is", "are", "am"): items.append((o, "긍정형이라 ‘~이 아니다/~에 있지 않다’는 우리말과 맞지 않으므로"))
        elif o == "not": items.append((o, "be동사 없이 not만으로는 동사 자리를 채울 수 없으므로"))
        else:
            b = o.replace("n't", "").replace(" not", "")
            items.append((o, f"be동사({b})는 {BEX.get(b, '')} 말이라 주어({subj})와 맞지 않으므로"))
    kw = {"p": p} if p else {}
    mk(7, 31, t, items, int(V_["ans"]), R_BN, s, st="R", **kw)
f731("B", "Jane", "is not"); f731("C", "They", "are not"); f731("D", "Mina", "isn't"); f731("F", "I", "am not")
f731("E", "We", "are not", p="We _______ late.\n(우리는 늦지 않았다.)", s=S731 + " 어색한 우리말(늦지 않은 상태이다)도 다듬었다. 보기와 정답은 그대로다.")

# 7-32 밑줄 틀린 것: 원문항 발문과 be동사 밑줄
R732 = "be동사 부정문에서도 be동사는 주어에 맞춘다. 복수 주어에는 are, 3인칭 단수 주어에는 is, I에는 am을 쓴다."
S732 = "원문항의 be동사 밑줄이 사라지고 발문이 바뀌었다. 원문항 발문과 밑줄로 되돌렸다. 보기와 정답은 그대로다."
def f732(t, why):
    V_ = V(7, 32, t); c = [re.sub(r"\b(am|is|are)\b", r"<u>\1</u>", x, count=1) for x in V_["c"]]
    a = int(V_["ans"])
    F(7, 32, t, st="R", c=c, a=a, r=R732, n=[w + (" 정답이다." if i + 1 == a else " 오답이다.") for i, w in enumerate(why)], s=S732 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
OKS = lambda s_, b: f"주어({s_})에 맞는 be동사({b})를 바르게 썼으므로"
f732("B", ["복수 주어 The boys에는 is가 아니라 are를 써야 하므로", OKS("The cats", "are"), OKS("They", "are"), OKS("I", "am"), OKS("Tom", "is")])
f732("C", [OKS("I", "am"), OKS("They", "are"), OKS("We", "are"), "3인칭 단수 주어 Jane에는 are가 아니라 is를 써야 하므로", OKS("The dog", "is")])
f732("D", [OKS("We", "are"), "복수 주어 The children에는 is가 아니라 are를 써야 하므로", OKS("Jane", "is"), OKS("The dogs", "are"), OKS("I", "am")])
f732("E", [OKS("The books", "are"), OKS("I", "am"), "주어 We에는 is가 아니라 are를 써야 하므로", OKS("You", "are"), OKS("Jane", "is")])
f732("F", [OKS("She", "is"), OKS("You", "are"), OKS("We", "are"), OKS("Tom", "is"), "주어 I에는 are가 아니라 am을 써야 하므로"])

# 7-33 부정형 짝: 원문항 발문
S733 = "발문에 ‘현재형 부정문으로’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def f733(t, good, why):
    V_ = V(7, 33, t); gs = [x.strip() for x in good.split(" - ")]; items = []
    for ch in V_["c"]:
        xs = [x.strip() for x in ch.split(" - ")]
        if xs == gs: items.append((ch, "두 문장의 주어에 맞는 부정형을 바르게 짝지었으므로")); continue
        bits = [f"{['첫째', '둘째'][i]} 빈칸 {x}: {why[i]}" for i, (x, g) in enumerate(zip(xs, gs)) if x != g]
        items.append((ch, ". ".join(bits) + ". 따라서"))
    mk(7, 33, t, items, int(V_["ans"]), R_BN, S733, st="R", okdup=True)
f733("B", "aren't - isn't", ["주어 We에는 aren't(are not)를 쓴다", "단수 주어 The dog에는 isn't(is not)를 쓴다"])
f733("C", "am not - aren't", ["주어 I에는 am not을 쓴다", "주어 They에는 aren't(are not)를 쓴다"])
f733("D", "isn't - aren't", ["단수 주어 The soup에는 isn't(is not)를 쓴다", "복수 주어 The plates에는 aren't(are not)를 쓴다"])
f733("E", "isn't - aren't", ["3인칭 단수 주어 Jane에는 isn't(is not)를 쓴다", "주어 You에는 aren't(are not)를 쓴다"])
f733("F", "aren't - isn't", ["복수 주어 The boys에는 aren't(are not)를 쓴다", "주어 She에는 isn't(is not)를 쓴다"])

# 7-34 Are가 아닌 것: 원문항 발문
S734 = "발문에 ‘현재형 의문문을 만들 때’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def f734(t, subjects, odd):
    V_ = V(7, 34, t); a = int(V_["ans"]); items = []
    for i, (x, s_) in enumerate(zip(V_["c"], subjects)):
        items.append((x, f"주어({s_})에는 Are가 아니라 be동사({odd})가 들어가므로" if i + 1 == a else f"주어({s_})에는 Are가 들어가므로"))
    mk(7, 34, t, items, a, R_BN, S734, st="R")
f734("B", ["the books", "we", "Jane", "you", "they"], "Is"); f734("C", ["we", "the boys", "these books", "you", "I"], "Am")
f734("D", ["Tom", "we", "you", "the boys", "the pencils"], "Is"); f734("E", ["the books", "they", "the dog", "we", "you"], "Is"); f734("F", ["the girls", "I", "the cats", "you", "we"], "Am")

# 7-35 의문문·부정문 짝: 원문항 발문과 문장별 우리말, F는 정답 조합 새로
S735 = "원문항의 문장별 우리말 해석이 빠지고 그 정보가 발문(‘첫 문장은 의문문, 둘째 문장은 부정문’)으로 옮겨졌다. 원문항 발문으로 되돌리고 우리말 해석을 붙였다."
def f735(t, p, good, why, c=None, a=None, s=S735 + " 보기와 정답은 그대로다."):
    V_ = V(7, 35, t); cs = c or V_["c"]; gs = [x.strip() for x in good.split(" - ")]; items = []
    for ch in cs:
        xs = [x.strip() for x in ch.split(" - ")]
        if xs == gs: items.append((ch, "의문문과 부정문의 be동사를 주어에 맞게 바르게 짝지었으므로")); continue
        bits = [f"{['첫째', '둘째'][i]} 빈칸 {x}: {why[i]}" for i, (x, g) in enumerate(zip(xs, gs)) if x != g]
        items.append((ch, ". ".join(bits) + ". 따라서"))
    mk(7, 35, t, items, a or int(V_["ans"]), R_BN, s, st="R", p=p, okdup=True)
f735("B", "_______ you ready? (너는 준비됐니?)\nI _______ tired. (나는 피곤하지 않아.)", "Are - am not", ["주어 you의 의문문은 Are로 시작한다", "주어 I의 부정은 am not이다"])
f735("C", "_______ this jacket yours? (이 재킷은 네 것이니?)\nThe gloves _______ mine. (그 장갑은 내 것이 아니야.)", "Is - aren't", ["단수 주어 this jacket의 의문문은 Is로 시작한다", "복수 주어 The gloves의 부정은 aren't이다"])
f735("D", "_______ Tom at home? (Tom은 집에 있니?)\nHe _______ busy. (그는 바쁘지 않아.)", "Is - isn't", ["3인칭 단수 주어 Tom의 의문문은 Is로 시작한다", "주어 He의 부정은 isn't이다"])
f735("E", "_______ Jane a student? (Jane은 학생이니?)\nShe _______ a teacher. (그녀는 선생님이 아니야.)", "Is - isn't", ["3인칭 단수 주어 Jane의 의문문은 Is로 시작한다", "주어 She의 부정은 isn't이다"])
f735("F", "_______ the book new? (그 책은 새것이니?)\nIt _______ old. (그것은 오래되지 않았어.)", "Is - isn't", ["단수 주어 the book의 의문문은 Is로 시작한다", "주어 It의 부정은 isn't이다"],
     c=["Is - aren't", "Is - isn't", "Are - am not", "Are - aren't", "Are - is not"], a=2, s=S735 + " 정답 조합(Are - aren't)이 원문항과 같아, 단수 주어로 바꿔 정답 조합이 Is - isn't가 되게 했다.")

# 7-36 줄임말: 원문항 발문, B는 앞 문장을 긍정문으로, C는 줄임말이 정답이 되게
R736 = "be동사 부정의 줄임말은 is not → isn't, are not → aren't이다. am not은 줄임말이 없고, not만으로는 동사 자리를 채울 수 없다."
S736 = "발문에 ‘뒤 문장을 현재형 부정문으로’가 붙었다. 원문항 발문으로 되돌렸다."
def f736(t, p, items, a, s):
    mk(7, 36, t, items, a, R736, s, st="R", p=p)
NC = lambda w: f"{w}: 줄임말이 아니므로"
f736("B", "She is my friend. She _______ my cousin.", [("not", "be동사 없이 not만으로는 동사 자리를 채울 수 없으므로"), ("isn't", "주어 She에 맞는 is not의 줄임말이므로"), ("aren't", "aren't는 you·복수 주어에 쓰므로"), ("I'm not", "주어 She 뒤에 I'm not을 쓸 수 없으므로"), ("be not", "be not은 올바른 부정 형태가 아니므로")], 2,
     S736 + " 앞 문장(She is not my cousin.)이 빈칸의 답을 그대로 보여 주어, 긍정문(She is my friend.)으로 바꿨다.")
f736("C", "He is a student. He _______ a teacher.", [("are not", "are not은 you·복수 주어에 쓰고 줄임말도 아니므로"), ("aren't", "aren't는 you·복수 주어에 쓰므로"), ("isn't", "주어 He에 맞는 is not의 줄임말이므로"), ("is not", NC("is not")), ("am not", "am not은 주어 I에 쓰고 줄임말도 아니므로")], 3,
     S736 + " 정답(am not)이 줄임말이 아니어서, 주어를 He로 바꿔 줄임말 isn't가 정답이 되게 했다.")
f736("D", "We are friends. We _______ brothers.", [("isn't", "isn't는 3인칭 단수 주어에 쓰므로"), ("aren't", "주어 We에 맞는 are not의 줄임말이므로"), ("am not", "am not은 주어 I에 쓰므로"), ("is not", "is not은 3인칭 단수 주어에 쓰고 줄임말도 아니므로"), ("are not", NC("are not"))], 2, S736 + " 보기와 정답은 그대로다.")
f736("E", "They are Jane's shoes. They _______ my shoes.", [("am not", "am not은 주어 I에 쓰므로"), ("is not", "is not은 3인칭 단수 주어에 쓰고 줄임말도 아니므로"), ("are not", NC("are not")), ("aren't", "주어 They에 맞는 are not의 줄임말이므로"), ("isn't", "isn't는 3인칭 단수 주어에 쓰므로")], 4, S736 + " 보기와 정답은 그대로다.")
f736("F", "She is Ben's sister. She _______ my sister.", [("aren't", "aren't는 you·복수 주어에 쓰므로"), ("am not", "am not은 주어 I에 쓰므로"), ("is not", NC("is not")), ("isn't", "주어 She에 맞는 is not의 줄임말이므로"), ("are not", "are not은 you·복수 주어에 쓰고 줄임말도 아니므로")], 4, S736 + " 보기와 정답은 그대로다.")

# 7-37 질문과 대답: 원문항 발문, 오답을 유형마다 새로
R737 = "be동사 의문문에는 Yes, 주어 + be동사. / No, 주어 + be동사 + not.으로 답한다. 대답의 주어는 질문의 주어를 대명사로 받고(you → I, I → you, Tom → he, the door → it), be동사도 그 주어에 맞춘다."
S737 = "발문에 ‘질문의 대상을 대명사로 받아 짧게 대답할 때’ 조건이 붙었고, 오답이 B와 같거나 원문항 선택지를 그대로 썼다. 원문항 발문으로 되돌리고 유형마다 오답을 새로 썼다."
def f737(t, items, a, s=S737):
    mk(7, 37, t, items, a, R737, s, st="R")
f737("B", [("Are you at home? - Yes, I am.", "you에 대한 질문에 I am으로 바르게 답했으므로"), ("Is he a student? - Yes, he are.", "대답의 주어 he에는 is를 써야 하므로"), ("Is Tom home? - Yes, he are.", "대답의 주어 he에는 is를 써야 하므로"), ("Are they friends? - No, they isn't.", "대답의 주어 they에는 aren't를 써야 하므로"),
           ("Am I late? - No, you isn't.", "대답의 주어 you에는 aren't를 써야 하므로")], 1, "발문에 조건이 붙었고 ⑤가 원문항 선택지 ②와 같았다. 원문항 발문으로 되돌리고 ⑤를 새로 썼다.")
f737("C", [("Is it your bag? - Yes, it are.", "대답의 주어 it에는 is를 써야 하므로"), ("Are the kids at school? - Yes, it is.", "the kids는 it이 아니라 they로 받아야 하므로"), ("Is Tom at school? - No, he isn't.", "Tom을 he로 받아 isn't로 바르게 답했으므로"),
           ("Am I right? - Yes, I am.", "I에 대한 질문에는 you로 받아 Yes, you are로 답하므로"), ("Is she your aunt? - No, she aren't.", "대답의 주어 she에는 isn't를 써야 하므로")], 3)
f737("D", [("Are you hungry? - Yes, you are.", "you에 대한 질문에는 I로 받아 Yes, I am으로 답하므로"), ("Are they friends? - No, they aren't.", "they에 대한 질문에 aren't로 바르게 답했으므로"), ("Is the door open? - No, they isn't.", "the door는 it으로 받아 No, it isn't로 답하므로"),
           ("Is Mina tall? - Yes, he is.", "Mina는 he가 아니라 she로 받아야 하므로"), ("Are we late? - Yes, we is.", "대답의 주어 we에는 are를 써야 하므로")], 2)
f737("F", [("Is your dad a cook? - Yes, she is.", "your dad는 she가 아니라 he로 받아야 하므로"), ("Are the cats hungry? - No, they isn't.", "대답의 주어 they에는 aren't를 써야 하므로"), ("Are we late? - No, we aren't.", "we에 대한 질문에 aren't로 바르게 답했으므로"),
           ("Is it cold? - Yes, it are.", "대답의 주어 it에는 is를 써야 하므로"), ("Am I tall? - Yes, I are.", "I에 대한 질문에는 you로 받아 Yes, you are로 답하므로")], 3)
F(7, 37, "E", st="R", r=R737, n=["복수 주어 the windows를 they로 받아 aren't로 바르게 답했으므로 정답이다.", "the windows는 it이 아니라 they로 받아야 하므로 오답이다.", "the window(단수)는 they가 아니라 it으로 받아야 하므로 오답이다.", "복수 주어 the windows의 의문문은 Is가 아니라 Are로 시작하므로 오답이다.", "대답의 주어 they에는 are를 써야 하므로 오답이다."],
  s="발문에 ‘질문의 대상을 대명사로 받아 짧게 대답할 때’ 조건이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 7-38 대화 짝: 원문항 발문
S738 = "발문에 ‘현재형으로’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def f738(t, good, why):
    V_ = V(7, 38, t); gs = [x.strip() for x in good.split(" - ")]; items = []
    for ch in V_["c"]:
        xs = [x.strip() for x in ch.split(" - ")]
        if xs == gs: items.append((ch, "질문과 대답의 주어에 맞는 be동사를 바르게 짝지었으므로")); continue
        bits = [f"{['첫째', '둘째'][i]} 빈칸 {x}: {why[i]}" for i, (x, g) in enumerate(zip(xs, gs)) if x != g]
        items.append((ch, ". ".join(bits) + ". 따라서"))
    mk(7, 38, t, items, int(V_["ans"]), R_BN, S738, st="R", okdup=True)
f738("B", "Is - isn't", ["3인칭 단수 주어 Jane에는 Is를 쓴다", "No 대답의 she에는 isn't를 쓴다"])
f738("C", "Are - am", ["주어 you에는 Are를 쓴다", "Yes 대답의 I에는 am을 쓴다"])
f738("D", "Is - is", ["3인칭 단수 주어 Mina에는 Is를 쓴다", "Yes 대답의 she에는 is를 쓴다"])
f738("E", "Is - is", ["3인칭 단수 주어 Tom에는 Is를 쓴다", "Yes 대답의 he에는 is를 쓴다"])
f738("F", "Are - aren't", ["복수 주어 the books에는 Are를 쓴다", "No 대답의 they에는 aren't를 쓴다"])

# 7-39 글 속 밑줄: 원문항 발문과 밑줄
R739 = "글 속의 각 be동사를 그 주어와 맞춰 본다. I에는 am, 3인칭 단수(he, she, it)에는 is, you·we·they와 복수 주어에는 are를 쓴다."
S739 = "원문항 밑줄이 사라지고 번호만 남았으며 발문도 달랐다. 원문항 발문으로 되돌리고 번호 뒤의 부분에 밑줄을 되살렸다. 보기와 정답은 그대로다."
MK = "①②③④⑤"
def f739(t, why):
    V_ = V(7, 39, t); p = V_["passage"]
    for m, o in zip(MK, V_["c"]): p = p.replace(f"{m}{o}", f"{m}<u>{o}</u>", 1)
    a = int(V_["ans"])
    F(7, 39, t, st="R", p=p, r=R739, n=[w + (" 정답이다." if i + 1 == a else " 오답이다.") for i, w in enumerate(why)], s=S739)
f739("B", ["주어 She를 바르게 썼으므로", "주어 She에 is를 바르게 썼으므로", "주어 she 앞에 Is를 두어 의문문을 바르게 만들었으므로", "대답의 주어 she에는 aren't가 아니라 isn't를 써야 하므로", "주어 She에 is를 바르게 썼으므로"])
f739("C", ["복수 주어 These pencils에 are를 바르게 썼으므로", "주어 they 앞에 Are를 두어 의문문을 바르게 만들었으므로", "대답의 주어 they에 aren't를 바르게 썼으므로", "주어 They에는 is가 아니라 are를 써야 하므로", "단수 주어 The blue one에 is를 바르게 썼으므로"])
f739("D", ["주어 We에 are를 바르게 썼으므로", "주어 we 앞에 Are를 두어 의문문을 바르게 만들었으므로", "대답의 주어 we에 aren't를 바르게 썼으므로", "3인칭 단수 주어 Tom에 is를 바르게 썼으므로", "주어 He에는 are가 아니라 is를 써야 하므로"])
f739("E", ["주어 They에 are를 바르게 썼으므로", "주어 they 앞에 Are를 두어 의문문을 바르게 만들었으므로", "대답의 주어 they에 are를 바르게 썼으므로", "주어 They에는 is가 아니라 are를 써야 하므로", "단수 주어 The desk에 is를 바르게 썼으므로"])
f739("F", ["주어 I에는 are가 아니라 am을 써야 하므로", "주어 I 앞에 Am을 두어 의문문을 바르게 만들었으므로", "대답의 주어 I에 am not을 바르게 썼으므로", "복수 주어 My parents에 are를 바르게 썼으므로", "단수 주어 The door에 is를 바르게 썼으므로"])

# 7-40 두 문장의 차이: 원문항처럼 우리말 해석, D~F는 그럴듯한 오개념 오답을 새로
R740 = "be동사 평서문은 주어 + be동사 순서이고, 의문문은 be동사를 주어 앞으로 옮기고 물음표를 붙인다. 순서가 바뀌어도 주어와 be동사의 뜻은 그대로다."
S740 = "원문항의 우리말 해석이 빠졌다. 원문항처럼 두 문장에 우리말 해석을 붙였다."
def f740(t, p, items, a, s):
    mk(7, 40, t, items, a, R740, s, p=p)
f740("B", "(A) The dog is outside. (그 개는 밖에 있다.)\n(B) Is the dog outside? (그 개는 밖에 있니?)",
     [("(A)와 (B)는 모두 의문문이다.", "(A)는 평서문이므로"), ("dog가 동물이므로 Is가 앞에 온다.", "주어가 동물이라서가 아니라 의문문이라서 Is가 앞에 오므로"), ("(A)는 주어+be동사의 평서문이고, (B)는 be동사+주어의 의문문이다.", "평서문과 의문문의 순서 차이를 바르게 설명했으므로"),
      ("두 문장의 뜻과 어순은 완전히 같다.", "(B)는 묻는 문장이라 뜻과 어순이 다르므로"), ("outside가 있어서 Is가 앞으로 갔다.", "outside와 관계없이 의문문이라서 Is가 앞으로 가므로")], 3, S740 + " 보기와 정답은 그대로다.")
f740("C", "(A) Tom is busy. (Tom은 바쁘다.)\n(B) Is Tom busy? (Tom은 바쁘니?)",
     [("의문문은 항상 Are로 시작한다.", "주어 Tom에 맞춰 Is로 시작하므로"), ("평서문을 의문문으로 바꿀 때 is를 Tom 앞으로 보낸다.", "평서문을 의문문으로 바꾸는 방법을 바르게 설명했으므로"), ("주어가 사라져서 순서가 바뀐다.", "주어 Tom은 그대로 있으므로"),
      ("장소 명사 때문에 순서가 바뀐다.", "장소 명사가 없고, 의문문이라서 순서가 바뀌므로"), ("두 문장은 의미가 완전히 같다.", "(B)는 묻는 문장이라 뜻이 다르므로")], 2, S740 + " 보기와 정답은 그대로다.")
S740b = S740 + " 설명 오답 네 개가 C와 똑같아, 원문항처럼 그럴듯한 오개념으로 유형마다 새로 썼다."
f740("D", "(A) They are at home. (그들은 집에 있다.)\n(B) Are they at home? (그들은 집에 있니?)",
     [("(A)는 대답하는 문장이고 (B)는 그 대답을 부정하는 문장이다.", "(B)는 부정문이 아니라 묻는 문장이므로"), ("(B)에서 Are가 앞에 온 것은 home이 장소를 나타내는 말이기 때문이다.", "장소 표현과 관계없이 의문문이라서 Are가 앞에 오므로"),
      ("(B)의 Are는 (A)의 are와 달리 '있다'가 아니라 '~이다'라는 뜻이다.", "두 are는 같은 be동사로 모두 ‘있다’라는 뜻이므로"), ("(A)와 (B)는 be동사와 주어의 순서가 달라 (A)는 평서문, (B)는 의문문이다.", "평서문과 의문문의 순서 차이를 바르게 설명했으므로"),
      ("(B)는 주어가 they에서 home으로 바뀌어 순서가 변했다.", "주어는 그대로 they이므로")], 4, S740b)
f740("E", "(A) We are ready. (우리는 준비됐다.)\n(B) Are we ready? (우리는 준비됐니?)",
     [("(B)는 be동사 Are를 주어 we 앞으로 옮기고 물음표를 붙인 의문문이다.", "의문문을 만드는 방법을 바르게 설명했으므로"), ("(A)는 묻는 문장이고 (B)는 대답하는 문장이다.", "(A)가 평서문, (B)가 묻는 문장이므로"), ("(B)에서 Are가 앞에 온 것은 ready가 형용사이기 때문이다.", "형용사와 관계없이 의문문이라서 Are가 앞에 오므로"),
      ("(A)의 are는 '~이다', (B)의 Are는 '~하니'라는 전혀 다른 단어이다.", "두 are는 같은 be동사이므로"), ("(B)는 주어가 we에서 ready로 바뀌었다.", "주어는 그대로 we이므로")], 1, S740b)
f740("F", "(A) She is happy. (그녀는 행복하다.)\n(B) Is she happy? (그녀는 행복하니?)",
     [("(A)는 주어 She가 한 명이라 평서문, (B)는 두 명이라 의문문이다.", "두 문장의 주어는 모두 한 명이고, 순서 때문에 평서문과 의문문이 나뉘므로"), ("(B)에서 Is가 앞에 온 것은 happy가 기분을 나타내는 말이기 때문이다.", "기분을 나타내는 말과 관계없이 의문문이라서 Is가 앞에 오므로"),
      ("(A)의 is와 (B)의 Is는 모양만 같고 서로 다른 동사이다.", "두 is는 같은 be동사이므로"), ("(B)는 주어가 she에서 happy로 바뀌어 순서가 변했다.", "주어는 그대로 she이므로"), ("(A)는 주어 + be동사 순서의 평서문이고, (B)는 be동사 + 주어 순서의 의문문이다.", "평서문과 의문문의 순서 차이를 바르게 설명했으므로")], 5, S740b)

# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, r, s, **kw):
    FIX.pop((7, n, t), None)
    mk(7, n, t, items, a, r, s, **kw)
NRM = lambda x: x.strip().replace("isn't", "is not").replace("aren't", "are not").replace("’", "'")
def pair(cs, good, why, okmsg):
    # 줄임말과 풀어 쓴 형태(isn't = is not)는 같은 것으로 본다
    gs = [NRM(x) for x in good.split(" - ")]; items = []
    for ch in cs:
        xs = [x.strip() for x in ch.split(" - ")]
        bad = [(i, x) for i, x in enumerate(xs) if NRM(x) != gs[i]]
        if not bad: items.append((ch, okmsg)); continue
        items.append((ch, ". ".join(f"{['첫째', '둘째'][i]} 빈칸 {x}: {why[i]}" for i, x in bad) + ". 따라서"))
    return items
# 7-32 E: ③(We is not late.)·④(You are not late.)가 서술어가 같은 쌍, ⑤(Jane is not here.)는 D의 ③과 같음
FIX.pop((7, 32, "E"), None)
F(7, 32, "E", st="R", c=["The books <u>are</u> not old.", "I <u>am</u> not tired.", "We <u>is</u> not at school.", "You <u>are</u> not alone.", "My mom <u>is</u> not angry."], a=3, r=R732,
  n=[OKS("The books", "are") + " 오답이다.", OKS("I", "am") + " 오답이다.", "주어 We에는 is가 아니라 are를 써야 하므로 정답이다.", OKS("You", "are") + " 오답이다.", OKS("My mom", "is") + " 오답이다."],
  s="원문항의 be동사 밑줄이 사라지고 발문이 바뀌었다. 또 ③(We is not late.)과 ④(You are not late.)는 서술어가 같아 둘만 견주면 답이 나왔고, ⑤(Jane is not here.)는 D의 ③과 같았다. 원문항 발문과 밑줄로 되돌리고 ③·④·⑤를 새 문장으로 바꿨다. 정답 위치 ③.")
# 7-33: 원문항의 ‘-’ 기호, 정답 조합이 유형마다 다르게(D·E는 원문항과 같은 단수-복수 조합, F는 B와 같음)
OK733 = "두 문장의 주어에 맞는 부정형을 바르게 짝지었으므로"
def g733(t, p, good, why, a, s):
    redo(33, t, pair(V(7, 33, t)["c"], good, why, OK733), a, R_BN, s, st="R", p=p, okdup=True)
g733("B", "- We _______ students.\n- The dog _______ big.", "aren't - isn't", ["주어 We에는 aren't(are not)를 쓴다", "단수 주어 The dog에는 isn't(is not)를 쓴다"], 4,
     "발문에 ‘현재형 부정문으로’가 붙었고, 원문항에 있는 문장 앞의 ‘-’ 기호가 빠졌다. 원문항 발문으로 되돌리고 ‘-’를 붙였다. 보기와 정답은 그대로다.")
g733("C", "- I _______ hungry.\n- They _______ ready.", "am not - aren't", ["주어 I에는 am not을 쓴다", "주어 They에는 aren't(are not)를 쓴다"], 1,
     "발문에 ‘현재형 부정문으로’가 붙었고, 원문항에 있는 문장 앞의 ‘-’ 기호가 빠졌다. 원문항 발문으로 되돌리고 ‘-’를 붙였다. 보기와 정답은 그대로다.")
g733("D", "- The soup _______ hot.\n- The plate _______ clean.", "is not - is not", ["단수 주어 The soup에는 is not(isn't)을 쓴다", "단수 주어 The plate에는 is not(isn't)을 쓴다"], 4,
     "발문에 ‘현재형 부정문으로’가 붙었고, 정답(isn't - aren't)이 원문항 정답(isn't - are not)과 같은 조합이었다. 원문항 발문으로 되돌리고 둘째 문장의 주어를 단수(The plate)로 바꿔 정답이 is not - is not이 되게 했다. 보기는 그대로다.")
g733("E", "- My parents _______ home.\n- You _______ late.", "are not - are not", ["복수 주어 My parents에는 are not(aren't)을 쓴다", "주어 You에는 are not(aren't)을 쓴다"], 3,
     "발문에 ‘현재형 부정문으로’가 붙었고 ‘-’ 기호가 빠졌으며, 정답(isn't - aren't)이 D·원문항과 같은 조합이었다. 원문항 발문으로 되돌리고 ‘-’를 붙였으며, 첫 문장의 주어를 복수(My parents)로 바꿔 정답이 are not - are not이 되게 했다. 보기는 그대로다.")
g733("F", "- I _______ busy.\n- She _______ tired.", "am not - is not", ["주어 I에는 am not을 쓴다", "주어 She에는 is not(isn't)을 쓴다"], 3,
     "발문에 ‘현재형 부정문으로’가 붙었고 ‘-’ 기호가 빠졌으며, 정답(aren't - isn't)과 그 위치(④)가 B와 같았다. 원문항 발문으로 되돌리고 ‘-’를 붙였으며, 첫 문장의 주어를 I로 바꿔 정답이 am not - is not이 되게 했다. 보기는 그대로다.")
# 7-34 D·E: 보기가 C·B·원문항과 겹침 → 새 문장으로
def g734(t, rows, a, odd, s):
    items = [(f"_______ {x}", f"주어({s_})에는 Are가 아니라 be동사({odd})가 들어가므로" if i + 1 == a else f"주어({s_})에는 Are가 들어가므로") for i, (x, s_) in enumerate(rows)]
    redo(34, t, items, a, R_BN, s, st="R")
g734("D", [("the children at the park?", "the children"), ("you and Tom brothers?", "you and Tom"), ("these shoes new?", "these shoes"), ("your bag heavy?", "your bag"), ("they in the library?", "they")], 4, "Is",
     "발문에 ‘현재형 의문문을 만들 때’가 붙었고, 보기 셋(we late / you ready / the boys outside)이 C와 같으며 ⑤는 원문항 ④와 같았다. 정답 위치(①)도 원문항과 같았다. 원문항 발문으로 되돌리고 보기를 새로 썼다.")
g734("E", [("those your pencils?", "those"), ("it your umbrella?", "it"), ("the students in the gym?", "the students"), ("you thirsty?", "you"), ("we on the right bus?", "we")], 2, "Is",
     "발문에 ‘현재형 의문문을 만들 때’가 붙었고, 보기 둘(the books new / we ready)과 정답 위치(③)가 B와 같으며 ⑤는 원문항 ②와 같았다. 원문항 발문으로 되돌리고 보기를 새로 썼다.")
# 7-35 C: 해설 바로잡기(are not = aren't) / E·F: 정답 조합이 D(Is - isn't)와 같음
OK735 = "의문문과 부정문의 be동사를 주어에 맞게 바르게 짝지었으므로"
def g735(t, p, good, why, a, s, c=None):
    kw = {"c": c} if c else {}
    cs = c or V(7, 35, t)["c"]
    FIX.pop((7, 35, t), None)
    items = pair(cs, good, why, OK735)
    F(7, 35, t, st="R", p=p, a=a, r=R_BN, n=[w + (" 정답이다." if i + 1 == a else " 오답이다.") for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", okdup=True, **kw)
g735("C", "_______ this jacket yours? (이 재킷은 네 것이니?)\nThe gloves _______ mine. (그 장갑은 내 것이 아니야.)", "Is - aren't", ["단수 주어 this jacket의 의문문은 Is로 시작한다", "복수 주어 The gloves의 부정은 aren't(are not)이다"], 2, S735 + " 보기와 정답은 그대로다.")
g735("E", "_______ the boys students? (그 소년들은 학생이니?)\nTheir sister _______ a student. (그들의 누나는 학생이 아니야.)", "Are - isn't", ["복수 주어 the boys의 의문문은 Are로 시작한다", "단수 주어 Their sister의 부정은 isn't이다"], 4,
     S735 + " 정답 조합(Is - isn't)이 D와 같아, 첫 문장의 주어를 복수(the boys)로 바꿔 정답 조합이 Are - isn't가 되게 했다. 보기는 그대로다.")
g735("F", "_______ I late? (내가 늦었니?)\nYou _______ late. (너는 늦지 않았어.)", "Am - aren't", ["주어 I의 의문문은 Am으로 시작한다", "주어 You의 부정은 aren't이다"], 5,
     S735 + " 정답 조합(Are - aren't)이 원문항과 같아, 주어를 I와 You로 바꿔 정답 조합이 Am - aren't가 되게 했다.", c=["Is - aren't", "Am - isn't", "Are - am not", "Are - aren't", "Am - aren't"])
# 7-36 C·D: 정답과 뜻이 같은 풀어 쓴 형태(is not, are not)가 보기에 함께 있음 / E: 원문항과 구조가 같음 / F: B와 거의 같음
S736X = " 또 정답 줄임말과 뜻이 같은 풀어 쓴 형태(%s)가 보기에 함께 있어 ‘줄임말’이라는 조건만으로 갈렸다. 원문항 보기에도 없는 형태라 %s로 바꿨다."
FIX.pop((7, 36, "C"), None); FIX.pop((7, 36, "D"), None); FIX.pop((7, 36, "E"), None); FIX.pop((7, 36, "F"), None)
BENOT = "be not은 올바른 부정 형태가 아니므로"; NOT1 = "be동사 없이 not만으로는 동사 자리를 채울 수 없으므로"
f736("C", "He is a student. He _______ a teacher.", [("are not", "are not은 you·복수 주어에 쓰고 줄임말도 아니므로"), ("aren't", "aren't는 you·복수 주어에 쓰므로"), ("isn't", "주어 He에 맞는 is not의 줄임말이므로"), ("be not", BENOT), ("am not", "am not은 주어 I에 쓰고 줄임말도 아니므로")], 3,
     S736 + " 정답(am not)이 줄임말이 아니어서, 주어를 He로 바꿔 줄임말 isn't가 정답이 되게 했다." + S736X % ("is not", "④를 be not으"))
f736("D", "We are friends. We _______ brothers.", [("isn't", "isn't는 3인칭 단수 주어에 쓰므로"), ("aren't", "주어 We에 맞는 are not의 줄임말이므로"), ("am not", "am not은 주어 I에 쓰므로"), ("is not", "is not은 3인칭 단수 주어에 쓰고 줄임말도 아니므로"), ("not", NOT1)], 2,
     S736 + S736X % ("are not", "⑤를 not으") + " 정답은 그대로다.")
f736("E", "The boys are in the gym. They _______ in the classroom.", [("am not", "am not은 주어 I에 쓰므로"), ("is not", "is not은 3인칭 단수 주어에 쓰고 줄임말도 아니므로"), ("be not", BENOT), ("aren't", "주어 They에 맞는 are not의 줄임말이므로"), ("isn't", "isn't는 3인칭 단수 주어에 쓰므로")], 4,
     S736 + " 두 문장(They are Jane's shoes. They ___ my shoes.)이 원문항(They are my friend's cats. They ___ my cats.)과 구조가 같고 낱말만 달라, 장소를 말하는 문장으로 바꿨다." + S736X % ("are not", "③을 be not으"))
f736("F", "This is my dad's car. It _______ my uncle's car.", [("aren't", "aren't는 you·복수 주어에 쓰므로"), ("am not", "am not은 주어 I에 쓰므로"), ("not", NOT1), ("isn't", "주어 It에 맞는 is not의 줄임말이므로"), ("are not", "are not은 you·복수 주어에 쓰고 줄임말도 아니므로")], 4,
     S736 + " 두 문장(She is Ben's sister. She ___ my sister.)이 B(She is ~. She ___ my cousin.)와 주어·구조가 같아, 주어가 It인 문장으로 바꿨다." + S736X % ("is not", "③을 not으"))
# 7-37 B: 정답 위치가 원문항·E와 같은 ①, ②·③의 오류(he are)가 같음
FIX.pop((7, 37, "B"), None)
f737("B", [("Is he a student? - Yes, he are.", "대답의 주어 he에는 is를 써야 하므로"), ("Is Tom home? - No, he aren't.", "대답의 주어 he에는 isn't를 써야 하므로"), ("Are they friends? - No, they isn't.", "대답의 주어 they에는 aren't를 써야 하므로"),
           ("Am I late? - No, you isn't.", "대답의 주어 you에는 aren't를 써야 하므로"), ("Are you at home? - Yes, I am.", "you에 대한 질문에 I am으로 바르게 답했으므로")], 5,
     "발문에 조건이 붙었고 ⑤가 원문항 선택지 ②와 같았다. 정답 위치(①)도 원문항·E와 같았고, ②·③의 대답이 똑같은 오류(Yes, he are.)였다. 원문항 발문으로 되돌리고, 원문항과 같은 보기를 새로 쓰고 순서를 바꿨으며, Tom의 대답은 No, he aren't로 바꿨다.")
# 7-38 E: 정답 조합(Is - is)과 위치(②)가 D와 같음
FIX.pop((7, 38, "E"), None)
mk(7, 38, "E", pair(["Are - am", "Is - is", "Am - are", "Are - aren't", "Am - is"], "Am - are", ["주어 I의 의문문은 Am으로 시작한다", "Yes 대답의 you에는 are를 쓴다"], "질문과 대답의 주어에 맞는 be동사를 바르게 짝지었으므로"), 3, R_BN,
   "발문에 ‘현재형으로’가 붙었고, 정답 조합(Is - is)과 위치(②)가 D와 같았다. 원문항 발문으로 되돌리고 대화의 주어를 I로 바꿔 정답 조합이 Am - are가 되게 했다.", st="R", p="A: _______ I late?\nB: Yes, you _______.", okdup=True)
# 7-39 B: 틀린 곳이 원문항과 같은 ④ / E: 틀린 곳(④ They is)이 C와 같음
def g739(t, p, c, a, why, s):
    FIX.pop((7, 39, t), None)
    F(7, 39, t, st="R", p=p, c=c, a=a, r=R739, n=[w + (" 정답이다." if i + 1 == a else " 오답이다.") for i, w in enumerate(why)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
g739("B", "①<u>She</u> ②<u>is my sister</u>. ③<u>Are she</u> at home? No, ④<u>she isn't</u>. She ⑤<u>is at school</u>.", ["She", "is my sister", "Are she", "she isn't", "is at school"], 3,
     ["주어 She를 바르게 썼으므로", "주어 She에 is를 바르게 썼으므로", "주어 she의 의문문은 Are가 아니라 Is로 시작해야 하므로", "대답의 주어 she에 isn't를 바르게 썼으므로", "주어 She에 is를 바르게 썼으므로"],
     "원문항 밑줄이 사라지고 번호만 남았으며 발문도 달랐다. 틀린 곳의 위치(④)도 원문항과 같았다. 원문항 발문으로 되돌리고 밑줄을 되살렸으며, 틀린 곳을 ③(Are she)으로 옮겼다.")
g739("E", "I have two bags. ①<u>They are new</u>. ②<u>Is they</u> in the room? Yes, ③<u>they are in the room</u>. ④<u>They are</u> near the desk. The desk ⑤<u>is brown</u>.", ["They are new", "Is they", "they are in the room", "They are", "is brown"], 2,
     ["주어 They에 are를 바르게 썼으므로", "주어 they의 의문문은 Is가 아니라 Are로 시작해야 하므로", "대답의 주어 they에 are를 바르게 썼으므로", "주어 They에 are를 바르게 썼으므로", "단수 주어 The desk에 is를 바르게 썼으므로"],
     "원문항 밑줄이 사라지고 번호만 남았으며 발문도 달랐다. 틀린 곳(④ They is)과 그 위치가 C와 같았다. 원문항 발문으로 되돌리고 밑줄을 되살렸으며, 틀린 곳을 ②(Is they)로 옮겼다.")
# 7-40 C: 오답이 문장과 관계없는 한 줄짜리 일반론이고 정답만 문장 속 낱말(Tom)을 말함
FIX.pop((7, 40, "C"), None)
f740("C", "(A) Tom is busy. (Tom은 바쁘다.)\n(B) Is Tom busy? (Tom은 바쁘니?)",
     [("(A)는 Tom에게 묻는 문장이고, (B)는 Tom이 대답하는 문장이다.", "(A)는 Tom에 대해 말하는 평서문이고 (B)가 묻는 문장이므로"), ("(B)에서 Is가 앞에 온 것은 Tom이 사람 이름이기 때문이다.", "주어가 사람 이름이라서가 아니라 의문문이라서 Is가 앞에 오므로"),
      ("(A)의 is를 주어 Tom 앞으로 보내고 물음표를 붙이면 (B)와 같은 의문문이 된다.", "평서문을 의문문으로 바꾸는 방법을 바르게 설명했으므로"), ("(B)는 busy가 문장 끝에 있어서 묻는 문장이 되었다.", "busy는 (A)에서도 문장 끝에 있고, be동사가 주어 앞에 와서 묻는 문장이 되므로"),
      ("(A)와 (B)는 낱말이 같으므로 뜻도 완전히 같다.", "낱말은 같아도 (A)는 말하는 문장, (B)는 묻는 문장이라 뜻이 다르므로")], 3,
     S740 + " 또 오답 넷이 두 문장과 관계없는 한 줄짜리 일반론(‘의문문은 항상 Are로 시작한다’ 등)이고 정답만 문장 속 낱말(Tom)을 말해 길이와 내용만으로 답이 드러났다. 원문항처럼 두 문장을 두고 말하는 그럴듯한 오개념으로 오답을 새로 썼다.")
