# 7급 CH7 일반동사 부정문·의문문 (61~70) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
R_DN = "일반동사 현재형의 부정문은 don't/doesn't + 동사원형, 의문문은 Do/Does + 주어 + 동사원형 ~?으로 쓴다. 3인칭 단수 주어에는 doesn't/Does, I·you·we·they와 복수 주어에는 don't/Do를 쓴다."

# 7-61 doesn't 앞에 알맞지 않은 주어: 옳은 주어를 원문항과 다르게
S761 = "옳은 오답 네 개(Jane, Your sister, The woman, My father)가 원문항 선택지 그대로였다. doesn't와 어울리는 3인칭 단수 주어를 유형마다 새로 썼다."
SG = lambda s_: f"{s_}: 3인칭 단수 주어라 doesn't와 어울려 들어갈 수 있으므로"
def f761(t, p, items, a, s=S761):
    mk(7, 61, t, items, a, R_DN, s, p=p)
f761("B", "_______ doesn't watch TV.", [("My grandma", SG("My grandma")), ("The baby", SG("The baby")), ("Tom and Ben", "Tom and Ben: 복수 주어라 doesn't가 아니라 don't를 써야 하므로"), ("Our teacher", SG("Our teacher")), ("He", SG("He"))], 3)
f761("C", "_______ doesn't read books.", [("Mina", SG("Mina")), ("You", "You: 주어 you에는 doesn't가 아니라 don't를 써야 하므로"), ("His brother", SG("His brother")), ("The girl", SG("The girl")), ("She", SG("She"))], 2)
f761("D", "_______ doesn't play soccer.", [("My cousin", SG("My cousin")), ("The new boy", SG("The new boy")), ("Mr. Kim", SG("Mr. Kim")), ("We", "We: 주어 we에는 doesn't가 아니라 don't를 써야 하므로"), ("Her son", SG("Her son"))], 4)
f761("E", "_______ doesn't like pizza.", [("They", "They: 주어 they에는 doesn't가 아니라 don't를 써야 하므로"), ("Minho", SG("Minho")), ("My aunt", SG("My aunt")), ("The child", SG("The child")), ("Your friend", SG("Your friend"))], 1)

# 7-63 Does가 들어갈 수 없는 것: 원문항 발문, 옳은 문장을 원문항과 다르게
S763 = "옳은 오답 서너 개가 원문항 선택지 그대로였고 발문에 ‘현재형 의문문을 만들 때’가 붙었다. 원문항 발문으로 되돌리고 옳은 문장을 유형마다 새로 썼다."
DS = lambda s_: f"주어({s_})가 3인칭 단수라 Does가 들어갈 수 있으므로"; DO = lambda s_: f"주어({s_})에는 Does가 아니라 Do를 써야 하므로"
def f763(t, items, a, s=S763):
    mk(7, 63, t, items, a, R_DN, s, st="R")
f763("B", [("_______ your mom cook dinner?", DS("your mom")), ("_______ Jiho play the drums?", DS("Jiho")), ("_______ the bus stop here?", DS("the bus")), ("_______ they like music?", DO("they")), ("_______ the store open early?", DS("the store"))], 4)
F(7, 63, "C", st="R", r=R_DN, n=[DO("your parents") + " 정답이다.", DS("Mina") + " 오답이다.", DS("your sister") + " 오답이다.", DS("Tom") + " 오답이다.", DS("the dog") + " 오답이다."],
  s="발문에 ‘현재형 의문문을 만들 때’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f763("D", [("_______ the baby sleep well?", DS("the baby")), ("_______ Tom and Ben play soccer?", DO("Tom and Ben")), ("_______ your uncle drive a truck?", DS("your uncle")), ("_______ the cat eat fish?", DS("the cat")), ("_______ Mina walk to school?", DS("Mina"))], 2)
f763("E", [("_______ Grandpa read the newspaper?", DS("Grandpa")), ("_______ the shop sell bread?", DS("the shop")), ("_______ your teacher speak Chinese?", DS("your teacher")), ("_______ the sun rise early?", DS("the sun")), ("_______ we need help?", DO("we"))], 5)
f763("F", [("_______ I look tired?", DO("I")), ("_______ Dad like coffee?", DS("Dad")), ("_______ the dog bark at night?", DS("the dog")), ("_______ your sister wear glasses?", DS("your sister")), ("_______ the train leave at six?", DS("the train"))], 1)

# 7-64 의문문으로 바꾸기: 원문항 발문
S764 = "발문이 ‘Do 또는 Does로 시작하는 기본 의문문으로’라고 정답 형식을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def q_note(o, subj, base, third):
    if o.endswith("?") and not o.startswith(("Do ", "Does ", "Is ", "Are ")): return "평서문 어순에 물음표만 붙였으므로"
    if o.startswith(("Is ", "Are ")): return "일반동사 의문문에는 be동사를 쓰지 않으므로"
    if o.startswith("Do ") and third: return f"3인칭 단수 주어({subj})에는 Do가 아니라 Does를 쓰므로"
    if o.startswith("Does ") and not third: return f"주어({subj})에는 Does가 아니라 Do를 쓰므로"
    if f" {base} " in f" {o[:-1]} ": return "Do/Does + 주어 + 동사원형으로 바르게 바꿨으므로"
    return "Do/Does 뒤에는 -s를 뗀 동사원형을 써야 하므로"
def fq(n, t, subj, base, third, s):
    V_ = V(7, n, t); a = int(V_["ans"])
    items = [(o, q_note(o, subj, base, third)) for o in V_["c"]]
    items[a-1] = (V_["c"][a-1], "Do/Does + 주어 + 동사원형으로 바르게 바꿨으므로")
    mk(7, n, t, items, a, R_DN, s, st="R")
for t, s_, b in [("B", "the dog", "eat"), ("C", "Tom", "like"), ("D", "my father", "watch"), ("E", "Jane", "study"), ("F", "Tom", "watch")]: fq(64, t, s_, b, True, S764)

# 7-65 우리말 → 영어: 원문항 발문
S765 = "발문이 ‘Do 또는 Does로 시작하는 기본 현재형 의문문으로’라고 정답 형식을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def q65(o, subj, base, third):
    if o.startswith(("Is ", "Are ")): return "일반동사 의문문에는 be동사를 쓰지 않으므로"
    if o.startswith("Does ") and not third: return f"주어({subj})에는 Does가 아니라 Do를 쓰므로"
    if o.endswith("ed " + o.split()[-1]) or re.search(r"\b\w+ed\b", o): return "현재의 일을 묻는데 과거형을 썼고, Do 뒤에는 동사원형을 쓰므로"
    if re.search(rf"\b{base}ing\b|\breading\b", o): return "Do 뒤에는 -ing형이 아니라 동사원형을 쓰므로"
    return "Do 뒤에는 -s를 뗀 동사원형을 써야 하므로"
for t, s_, b in [("B", "we", "study"), ("C", "you", "like"), ("D", "the students", "study"), ("E", "the boys", "play"), ("F", "they", "read")]:
    V_ = V(7, 65, t); a = int(V_["ans"])
    items = [(o, q65(o, s_, b, False)) for o in V_["c"]]; items[a-1] = (V_["c"][a-1], "우리말에 맞게 Do + 주어 + 동사원형으로 바르게 옮겼으므로")
    mk(7, 65, t, items, a, R_DN, S765, st="R")

# 7-66 부정 빈칸: 원문항 발문, F는 발문 설명과 우리말 삭제
S766 = "발문에 ‘현재형 부정문으로 완성할 때’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def f766(t, subj, good, p=None, s=S766):
    V_ = V(7, 66, t); a = int(V_["ans"]); items = []
    for o in V_["c"]:
        if o == good: w = f"주어({subj})에 맞는 부정형으로 일반동사 앞에 쓰므로"
        elif o in ("isn't", "aren't"): w = "일반동사의 부정문에는 be동사의 부정형을 쓰지 않으므로"
        elif o == "not": w = "not만으로는 일반동사를 부정할 수 없으므로"
        elif o == "doesn't": w = f"doesn't는 3인칭 단수 주어에 쓰므로"
        else: w = f"주어({subj})가 3인칭 단수라 don't가 아니라 doesn't를 쓰므로"
        items.append((o, w))
    kw = {"p": p} if p else {}
    mk(7, 66, t, items, a, R_DN, s, st="R", **kw)
f766("B", "I", "don't"); f766("C", "My cousins", "don't"); f766("D", "We", "don't"); f766("E", "Jane", "doesn't")
f766("F", "They", "don't", p="They _______ like milk.", s="발문에 ‘여기서 like는 좋아하다라는 일반동사입니다’라는 설명과 원문항에 없던 우리말이 붙었다. 설명과 우리말을 지워 원문항 발문과 형식으로 되돌렸다. 보기와 정답은 그대로다.")

# 7-67 짧은 대답: 원문항 발문, 원문항처럼 같은 주어의 틀린 대답
R767 = "Do/Does 의문문에는 Yes, 주어 + do/does. / No, 주어 + don't/doesn't.로 짧게 답한다. be동사나 일반동사를 그대로 쓰지 않고, 주어는 질문의 주어를 대명사로 받는다(you → I)."
S767 = "발문이 ‘생략된 일반동사를 do/does로 대신하는 짧은 대답’이라고 정답 형식을 알려 주었고, 오답이 질문 주어와 맞지 않아 바로 지워졌으며 유형마다 반복되었다. 원문항 발문으로 되돌리고, 원문항처럼 같은 주어의 틀린 대답으로 오답을 새로 썼다."
ST767 = lambda g="": "다음 질문에 대한 대답으로 가장 알맞은 것을 고르세요." + (f" (단, {g})" if g else "")
def f767(t, q, g, items, a, s=S767):
    mk(7, 67, t, items, a, R767, s, st=ST767(g), p=q)
BEQ = "Do/Does 질문에는 be동사로 답하지 않으므로"
f767("B", "Does Tom study English?", "Tom은 남자", [("Yes, he is.", BEQ), ("Yes, he studies.", "짧은 대답에는 일반동사 대신 does를 쓰므로"), ("Yes, he do.", "3인칭 단수 he에는 does를 쓰므로"), ("Yes, he does.", "Does 질문에 he does로 바르게 답했으므로"), ("Yes, it does.", "Tom은 it이 아니라 he로 받아야 하므로")], 4)
f767("C", "Do they play soccer?", "", [("Yes, they are.", BEQ), ("Yes, they do.", "Do 질문에 they do로 바르게 답했으므로"), ("Yes, they does.", "주어 they에는 does가 아니라 do를 쓰므로"), ("Yes, they plays.", "짧은 대답에는 일반동사 대신 do를 쓰므로"), ("Yes, we do.", "they에 대한 질문에는 they로 답하므로")], 2)
f767("D", "Does Mina need a ticket?", "Mina는 여자", [("No, she isn't.", BEQ), ("No, she don't.", "3인칭 단수 she에는 doesn't를 쓰므로"), ("No, Mina not.", "not만으로는 부정할 수 없고 짧은 대답은 대명사 she로 하므로"), ("No, her doesn't.", "대답의 주어는 목적격 her가 아니라 주격 she를 쓰므로"), ("No, she doesn't.", "Does 질문에 she doesn't로 바르게 답했으므로")], 5)
f767("E", "Do your parents like music?", "", [("No, they aren't.", BEQ), ("No, they doesn't.", "주어 they에는 don't를 쓰므로"), ("No, they don't.", "your parents를 they로 받아 don't로 바르게 답했으므로"), ("No, we don't.", "your parents에 대한 질문에는 we가 아니라 they로 답하므로"), ("No, they not.", "not만으로는 부정할 수 없고 don't를 써야 하므로")], 3)
f767("F", "Do you need help?", "", [("No, I don't.", "you에 대한 Do 질문에 I don't로 바르게 답했으므로"), ("Yes, you do.", "you에 대한 질문에는 I로 받아 답하므로"), ("No, I doesn't.", "주어 I에는 don't를 쓰므로"), ("Yes, I am.", BEQ), ("No, I not.", "not만으로는 부정할 수 없고 don't를 써야 하므로")], 1)

# 7-68 옳은 부정문: 원문항 발문, 짝 없이 유형마다 새로
S768 = "오답 서너 개가 원문항 선택지 그대로이거나 B와 같았고, 정답과 같은 문장의 틀린 형태가 함께 있어 대비 단서가 되었다. 원문항 발문으로 되돌리고 짝 없이 유형마다 새로 썼다."
OK68 = "주어에 맞는 don't/doesn't 뒤에 동사원형을 바르게 썼으므로"
def f768(t, items, a, s=S768):
    mk(7, 68, t, [(x, w or OK68) for x, w in items], a, R_DN, s, st="R")
f768("B", [("My brother doesn't likes milk.", "doesn't 뒤에는 동사원형 like를 써야 하므로"), ("He doesn't eat fish.", ""), ("We doesn't have time.", "주어 We에는 don't를 써야 하므로"), ("The girls doesn't dance.", "복수 주어 The girls에는 don't를 써야 하므로"), ("Mom don't drive.", "3인칭 단수 주어 Mom에는 doesn't를 써야 하므로")], 2)
f768("C", [("I don't have a bike.", ""), ("Jane doesn't plays tennis.", "doesn't 뒤에는 동사원형 play를 써야 하므로"), ("They doesn't know him.", "주어 They에는 don't를 써야 하므로"), ("My dad don't cook.", "3인칭 단수 주어 My dad에는 doesn't를 써야 하므로"), ("You doesn't need it.", "주어 You에는 don't를 써야 하므로")], 1)
f768("D", [("She don't wear glasses.", "3인칭 단수 주어 She에는 doesn't를 써야 하므로"), ("Tom doesn't swims.", "doesn't 뒤에는 동사원형 swim을 써야 하므로"), ("They don't have a rabbit.", ""), ("We doesn't go there.", "주어 We에는 don't를 써야 하므로"), ("The cat don't eat rice.", "3인칭 단수 주어 The cat에는 doesn't를 써야 하므로")], 3)
f768("E", [("The kids doesn't sleep early.", "복수 주어 The kids에는 don't를 써야 하므로"), ("He don't read comics.", "3인칭 단수 주어 He에는 doesn't를 써야 하므로"), ("I doesn't like carrots.", "주어 I에는 don't를 써야 하므로"), ("You don't have a pencil.", ""), ("My aunt doesn't lives here.", "doesn't 뒤에는 동사원형 live를 써야 하므로")], 4)
f768("F", [("We doesn't eat meat.", "주어 We에는 don't를 써야 하므로"), ("They are not eat meat.", "일반동사의 부정문에는 be동사 are not을 쓰지 않으므로"), ("Tom doesn't eats meat.", "doesn't 뒤에는 동사원형 eat을 써야 하므로"), ("She don't eat meat.", "3인칭 단수 주어 She에는 doesn't를 써야 하므로"), ("We don't eat meat.", "")], 5,
     "발문에 ‘현재형 부정문으로’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 7-69 Do/Does를 쓴 이유: 밑줄 복원, C·E·F는 그럴듯한 오해로 오답 새로
R769 = "일반동사가 있는 문장을 의문문으로 만들 때 주어 앞에 Do/Does를 쓴다. 3인칭 단수 주어에는 Does, 그 밖의 주어에는 Do를 쓴다. 뜻을 강조하거나 be동사를 줄이려는 것이 아니다."
UL = lambda p: re.sub(r"^(Do|Does) ", r"<u>\1</u> ", p)
F(7, 69, "B", p=UL(V(7, 69, "B")["passage"]), r=R769, n=["목적어가 있다고 Does를 쓰는 것이 아니므로 오답이다.", "3인칭 단수 주어 Tom과 일반동사 read가 있는 의문문이라 Does를 쓰므로 정답이다.", "강조하려고 Does를 쓰는 것이 아니므로 오답이다.", "be동사 문장을 줄인 것이 아니라 일반동사 의문문이므로 오답이다.", "물음표가 있어도 be동사 의문문에는 Does를 쓰지 않으므로 오답이다."],
  s="원문항의 밑줄이 사라졌다. 문장 맨 앞의 Does에 밑줄을 되살렸다. 보기와 정답은 그대로다.")
F(7, 69, "D", p=UL(V(7, 69, "D")["passage"]), r=R769, n=["3인칭 단수 주어 Tom과 일반동사 work가 있는 의문문이라 Does를 쓰므로 정답이다.", "현재시제라도 be동사 문장에는 Does를 쓰지 않으므로 오답이다.", "Tom은 사람 이름이고 장소와 관계없으므로 오답이다.", "주어가 3인칭 단수가 아니면 Do로 시작하므로 오답이다.", "목적어의 유무는 Does를 쓰는 이유가 아니므로 오답이다."],
  s="원문항의 밑줄이 사라졌다. 문장 맨 앞의 Does에 밑줄을 되살렸다. 보기와 정답은 그대로다.")
S769 = "오답 네 개가 B와 똑같았고 밑줄도 사라졌다. 밑줄을 되살리고, 원문항처럼 인칭·뜻·강조에 관한 그럴듯한 오해로 유형마다 오답을 새로 썼다."
def f769(t, p, items, a, s=S769):
    mk(7, 69, t, items, a, R769, s, p=p)
f769("C", "<u>Do</u> we study English?", [("we가 '우리'라는 뜻의 3인칭 단수이기 때문이다.", "we는 1인칭 복수이므로"), ("English가 과목 이름이라 Do를 쓰기 때문이다.", "목적어의 종류는 Do를 쓰는 이유가 아니므로"), ("be동사 are를 짧게 줄인 말이기 때문이다.", "Do는 be동사를 줄인 말이 아니므로"),
     ("우리가 영어를 정말로 공부한다고 강조하기 위해서이다.", "강조가 아니라 묻는 문장을 만들기 위해 Do를 쓰므로"), ("study라는 일반동사가 있는 문장을 의문문으로 만들기 위해서이다.", "일반동사 의문문은 Do로 시작하므로")], 5)
f769("E", "<u>Do</u> they play soccer?", [("they가 한 명이라서 Do를 쓰기 때문이다.", "they는 여러 명(복수)이므로"), ("soccer가 운동이라서 Do가 필요하기 때문이다.", "목적어의 종류는 Do를 쓰는 이유가 아니므로"), ("대답이 Yes일 때만 Do를 쓰기 때문이다.", "대답과 관계없이 일반동사 의문문은 Do/Does로 시작하므로"),
     ("play라는 일반동사가 있는 문장을 의문문으로 만들기 위해서이다.", "일반동사 의문문은 Do로 시작하므로"), ("Are를 쓰면 문장이 너무 길어지기 때문이다.", "문장의 길이가 아니라 일반동사가 있어서 Do를 쓰므로")], 4)
f769("F", "<u>Does</u> she like music?", [("she가 여자라서 Does를 쓰기 때문이다.", "성별이 아니라 3인칭 단수 주어라서 Does를 쓰므로"), ("music이 셀 수 없는 명사라서 Does를 쓰기 때문이다.", "목적어의 종류는 Does를 쓰는 이유가 아니므로"),
     ("주어 she가 3인칭 단수이고 like라는 일반동사가 있는 의문문이기 때문이다.", "3인칭 단수 주어의 일반동사 의문문은 Does로 시작하므로"), ("like가 '좋아하다'라는 뜻이라 Does와 어울리기 때문이다.", "동사의 뜻은 Does를 쓰는 이유가 아니므로"), ("be동사 is 대신 쓰는 말이라서 Does를 쓰기 때문이다.", "Does는 be동사 대신 쓰는 말이 아니므로")], 3)

# 7-70 옳은 문장으로만 짝: 원문항 발문
R770 = "주어가 3인칭 단수면 doesn't, I·you·we·they와 복수 주어면 don't를 쓰고, 그 뒤에는 동사원형을 쓴다."
S770 = "발문이 ‘옳은 문장을 모두 고른 것’으로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def f770(t, judge):
    V_ = V(7, 70, t); ok = V_["c"][int(V_["ans"]) - 1]
    F(7, 70, t, st="R", r=R770, pre=["문장별 판정: " + j for j in judge], k=f"옳은 문장은 {ok}이다.", n=setnotes(V_["c"], ok, "옳은 문장"), okdup=True, s=S770)
f770("B", ["ⓐ O. 주어 I에 don't를 썼다.", "ⓑ X. 3인칭 단수 주어 He에는 doesn't를 써야 한다.", "ⓒ O. 3인칭 단수 주어 Jane에 doesn't를 썼다.", "ⓓ X. 주어 We에는 don't를 써야 한다.", "ⓔ O. 주어 They에 don't를 썼다."])
f770("C", ["ⓐ O. 3인칭 단수 주어 She에 doesn't를 썼다.", "ⓑ X. 주어 They에는 don't를 써야 한다.", "ⓒ X. 3인칭 단수 주어 Tom에는 doesn't를 써야 한다.", "ⓓ O. 주어 We에 don't를 썼다.", "ⓔ X. doesn't 뒤에는 동사원형 bark를 써야 한다."])
f770("D", ["ⓐ O. 3인칭 단수 주어 He에 doesn't를 썼다.", "ⓑ X. 주어 We에는 don't를 써야 한다.", "ⓒ O. 주어 They에 don't를 썼다.", "ⓓ X. 3인칭 단수 주어 Jane에는 doesn't를 써야 한다.", "ⓔ O. 주어 I에 don't를 썼다."])
f770("E", ["ⓐ O. 3인칭 단수 주어 Tom에 doesn't를 썼다.", "ⓑ O. 3인칭 단수 주어 She에 doesn't를 썼다.", "ⓒ O. 주어 They에 don't를 썼다.", "ⓓ X. 주어 You에는 don't를 써야 한다.", "ⓔ X. 주어 I에는 don't를 써야 한다."])
f770("F", ["ⓐ X. 3인칭 단수 주어 She에는 doesn't를 써야 한다.", "ⓑ O. 3인칭 단수 주어 Tom에 doesn't를 썼다.", "ⓒ O. 주어 You에 don't를 썼다.", "ⓓ X. 주어 They에는 don't를 써야 한다.", "ⓔ O. 주어 We에 don't를 썼다."])

# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, r, s, **kw):
    FIX.pop((7, n, t), None)
    mk(7, n, t, items, a, r, s, **kw)
# 7-62 B: 다섯 보기가 모두 같은 서술어(need a map), 정답 위치가 원문항과 같은 ④
DN3 = lambda s_: f"주어({s_})가 3인칭 단수라 does not이 들어가므로"
mk(7, 62, "B", [("He _______ need a map.", DN3("He")), ("The driver _______ know the way.", DN3("The driver")), ("My friends _______ have a map.", "주어(My friends)가 복수라 do not이 들어가 나머지와 다르므로"), ("Jane _______ walk to school.", DN3("Jane")),
   ("My brother _______ drive a car.", DN3("My brother"))], 3, R_DN,
   "다섯 보기가 모두 같은 서술어(need a map)이고 주어만 달라, 서술어가 저마다 다른 원문항보다 보기의 수준이 낮았다. 정답 위치(④)도 원문항과 같았다. 서술어를 보기마다 다르게 쓰고 정답 위치를 옮겼다.")
# 7-64 D·E: 정답 위치가 C·D·E 모두 ⑤ → 보기 순서를 바꿈
S764B = "발문이 ‘Do 또는 Does로 시작하는 기본 의문문으로’라고 정답 형식을 알려 주었다. 원문항 발문으로 되돌렸다. 또 정답 위치가 C·D·E 모두 ⑤여서 보기 순서를 바꿨다."
def g764(t, subj, base, opts, a):
    items = [(o, q_note(o, subj, base, True)) for o in opts]; items[a-1] = (opts[a-1], "Do/Does + 주어 + 동사원형으로 바르게 바꿨으므로")
    redo(64, t, items, a, R_DN, S764B, st="R")
g764("D", "my father", "watch", ["Is my father watch TV?", "Does my father watch TV?", "My father watches TV?", "Do my father watch TV?", "Does my father watches TV?"], 2)
g764("E", "Jane", "study", ["Does Jane study English?", "Is Jane study English?", "Does Jane studies English?", "Jane studies English?", "Do Jane study English?"], 1)
# 7-65 D: 우리말이 B(우리는 영어를 공부하니?)와 주어만 다름, 정답 위치가 E와 같은 ⑤
redo(65, "D", [("Are the students walk to school?", "일반동사 의문문에는 be동사를 쓰지 않으므로"), ("Do the students walk to school?", "우리말에 맞게 Do + 주어 + 동사원형으로 바르게 옮겼으므로"), ("Does the students walk to school?", "주어(the students)에는 Does가 아니라 Do를 쓰므로"),
     ("Do the students walked to school?", "현재의 일을 묻는데 과거형을 썼고, Do 뒤에는 동사원형을 쓰므로"), ("Do the students walks to school?", "Do 뒤에는 -s를 뗀 동사원형을 써야 하므로")], 2, R_DN,
     "발문이 ‘Do 또는 Does로 시작하는 기본 현재형 의문문으로’라고 정답 형식을 알려 주었다. 원문항 발문으로 되돌렸다. 또 우리말(그 학생들은 영어를 공부하니?)이 B(우리는 영어를 공부하니?)와 주어만 달라 다른 문장으로 바꾸고, 정답 위치도 E(⑤)와 겹치지 않게 옮겼다.", st="R", p="그 학생들은 걸어서 학교에 가니?")
# 7-67 B·D: 필요 없는 조건 ‘(단, Tom은 남자)’ 삭제, B의 ②는 분명한 오답으로
FIX.pop((7, 67, "B"), None); FIX.pop((7, 67, "D"), None)
f767("B", "Does Tom study English?", "", [("Yes, he is.", BEQ), ("Yes, he doesn't.", "Yes 뒤에 부정형 doesn't를 쓸 수 없으므로"), ("Yes, he do.", "3인칭 단수 he에는 does를 쓰므로"), ("Yes, he does.", "Does 질문에 he does로 바르게 답했으므로"), ("Yes, it does.", "Tom은 사람이라 it이 아니라 he로 받아야 하므로")], 4,
     S767 + " 보기에 she가 없어 ‘Tom은 남학생입니다’라는 조건은 필요 없으므로 지웠다.")
f767("D", "Does Mina need a ticket?", "", [("No, she isn't.", BEQ), ("No, she don't.", "3인칭 단수 she에는 doesn't를 쓰므로"), ("No, Mina not.", "not만으로는 부정할 수 없고 짧은 대답은 대명사 she로 하므로"), ("No, her doesn't.", "대답의 주어는 목적격 her가 아니라 주격 she를 쓰므로"), ("No, she doesn't.", "Does 질문에 she doesn't로 바르게 답했으므로")], 5,
     S767 + " 보기에 he가 없어 ‘Mina는 여학생입니다’라는 조건은 필요 없으므로 지웠다.")
# 7-68 E: 정답 문장이 원문항 ④를 고친 꼴 / F: ①·⑤가 don't/doesn't만 다른 짝, 서술어가 모두 eat meat
FIX.pop((7, 68, "E"), None); FIX.pop((7, 68, "F"), None)
f768("E", [("The kids doesn't sleep early.", "복수 주어 The kids에는 don't를 써야 하므로"), ("He don't read comics.", "3인칭 단수 주어 He에는 doesn't를 써야 하므로"), ("I doesn't like carrots.", "주어 I에는 don't를 써야 하므로"), ("You don't need a ticket.", ""), ("My aunt doesn't lives here.", "doesn't 뒤에는 동사원형 live를 써야 하므로")], 4,
     S768 + " 정답 문장은 원문항 ④(You doesn't have a pencil.)를 고친 꼴이 되지 않게 다른 문장으로 바꿨다.")
f768("F", [("We doesn't walk to school.", "주어 We에는 don't를 써야 하므로"), ("They are not like fish.", "일반동사의 부정문에는 be동사 are not을 쓰지 않으므로"), ("Tom doesn't eats breakfast.", "doesn't 뒤에는 동사원형 eat을 써야 하므로"), ("My sisters don't eat meat.", ""), ("She don't drink milk.", "3인칭 단수 주어 She에는 doesn't를 써야 하므로")], 4,
     "발문에 ‘현재형 부정문으로’가 붙었다. 또 다섯 보기의 서술어가 모두 eat meat이고, ①(We doesn't eat meat.)과 ⑤(We don't eat meat.)는 don't/doesn't만 다른 짝이라 둘만 견주면 답이 나왔다. 원문항 발문으로 되돌리고 서술어를 보기마다 다르게 썼다.")
# 7-69 B: 오답이 짧은 일반론, 주어와 정답 문구가 D(Does Tom work here?)와 거의 같음
FIX.pop((7, 69, "B"), None)
f769("B", "<u>Does</u> your sister read books?", [("'books'가 여러 권(복수)이기 때문이다.", "목적어의 수는 Does를 쓰는 이유가 아니므로"), ("주어 'your sister'가 3인칭 단수이고 'read'라는 일반동사가 있는 의문문이기 때문이다.", "3인칭 단수 주어의 일반동사 의문문은 Does로 시작하므로"),
     ("'read(읽다)'가 be동사이기 때문이다.", "read는 be동사가 아니라 일반동사이므로"), ("'네 여동생이 책을 정말로 읽는다'고 강조하기 위해서이다.", "강조가 아니라 묻는 문장을 만들기 위해 Does를 쓰므로"),
     ("'your'가 '너의'라는 뜻이라 2인칭에 맞추기 때문이다.", "주어는 your가 아니라 your sister(3인칭 단수)이고, 2인칭이라면 Do를 쓰므로")], 2,
     "원문항의 밑줄이 사라졌다. 또 오답이 문장과 관계없는 짧은 일반론(‘목적어가 있기 때문이다’ 등)이고 정답만 길고 구체적이어서 길이만으로 답이 드러났으며, 문장(Does Tom read books?)의 주어와 정답 문구가 D(Does Tom work here?)와 거의 같았다. 밑줄을 되살리고 주어를 바꿨으며, 원문항처럼 문장 속 낱말을 두고 말하는 오해로 오답을 새로 썼다.")
# 7-70 D: 정답 조합(ⓐ, ⓒ, ⓔ)이 B와 같음 → 문장 순서를 바꿔 ⓒ, ⓓ, ⓔ
FIX.pop((7, 70, "D"), None)
C770D = ["ⓑ, ⓒ, ⓔ", "ⓐ, ⓓ", "ⓐ, ⓑ, ⓒ", "ⓒ, ⓓ, ⓔ", "ⓑ, ⓓ"]
F(7, 70, "D", st="R", p="ⓐ We doesn't play soccer.\nⓑ Jane don't study.\nⓒ He doesn't like milk.\nⓓ They don't read books.\nⓔ I don't need help.", c=C770D, a=4, r=R770,
  pre=["문장별 판정: " + j for j in ["ⓐ X. 주어 We에는 don't를 써야 한다.", "ⓑ X. 3인칭 단수 주어 Jane에는 doesn't를 써야 한다.", "ⓒ O. 3인칭 단수 주어 He에 doesn't를 썼다.", "ⓓ O. 주어 They에 don't를 썼다.", "ⓔ O. 주어 I에 don't를 썼다."]],
  k="옳은 문장은 ⓒ, ⓓ, ⓔ이다.", n=setnotes(C770D, "ⓒ, ⓓ, ⓔ", "옳은 문장"), okdup=True,
  s="발문이 ‘옳은 문장을 모두 고른 것’으로 바뀌었고, 정답 조합(ⓐ, ⓒ, ⓔ)이 B와 같았다. 원문항 발문으로 되돌리고, 문장 순서를 바꿔 정답 조합이 ⓒ, ⓓ, ⓔ가 되게 했다(보기 ④도 이에 맞게 바꿨다). 정답 위치 ④.")
