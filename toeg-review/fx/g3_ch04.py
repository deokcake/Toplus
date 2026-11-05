# 3급 CH4 시제 (31~40) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def talk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[w + (" 옳지 않은 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.") for i, (_, w) in enumerate(items)], k=items[a-1][1], s=s + ipos(a), **kw)

# 3-31 현재 습관: 오답 네 문장을 유형마다 새로
R31 = "현재의 습관·반복되는 일·일반적 사실은 현재시제로 나타낸다(always, usually, often, every day와 자주 쓰인다). 끝난 과거 일은 과거시제, 지금 진행 중인 일은 현재진행형, 앞으로의 일은 will·be going to로 나타낸다."
S31 = "오답 네 문장이 유형마다 같았다(B는 정답 문장도 원문항과 똑같았다). 유형마다 오답과 정답 문장을 새로 썼다."
PAST, PROG, FUT, PPROG = "끝난 과거의 일을 나타내는 과거시제라 현재의 습관이 아니므로", "지금 진행 중인 일을 나타내는 현재진행형이라 습관이 아니므로", "앞으로의 일을 나타내는 미래 표현이라 현재의 습관이 아니므로", "과거에 진행 중이던 일을 나타내는 과거진행형이라 현재의 습관이 아니므로"
HAB = "빈도·반복을 나타내는 말과 함께 현재의 습관을 현재시제로 나타냈으므로"
mk(3, 31, "B", [("We visited Jeju last summer.", PAST), ("My dad reads the newspaper every morning.", HAB), ("She is talking on the phone now.", PROG), ("I will call you tonight.", FUT), ("They were swimming at that time.", PPROG)], 2, R31, S31)
mk(3, 31, "C", [("Tom broke the window yesterday.", PAST), ("We are going to move next month.", FUT), ("The kids are playing outside right now.", PROG), ("Jane studies English every day.", HAB), ("I was sleeping when you called.", PPROG)], 4, R31, S31)
mk(3, 31, "D", [("She finished her homework an hour ago.", PAST), ("It will be sunny tomorrow.", FUT), ("My brother is taking a shower now.", PROG), ("We were watching TV at nine.", PPROG), ("They play soccer on Sundays.", HAB)], 5, R31, S31)
mk(3, 31, "E", [("Tom usually walks to school.", HAB), ("I met Mina at the mall last week.", PAST), ("He is going to buy a new bike.", FUT), ("The baby is crying loudly now.", PROG), ("They were having lunch then.", PPROG)], 1, R31, S31)
mk(3, 31, "F", [("Jane lost her wallet two days ago.", PAST), ("I'll help you with your homework.", FUT), ("We often eat dinner at seven.", HAB), ("Look! It is snowing outside.", PROG), ("He was reading a book at that time.", PPROG)], 3, R31, S31)

# 3-32 과거진행형 의미: 원문항 발문·밑줄, B는 대화를 새로
ST32 = "다음 대화에서 밑줄 친 부분의 의미로 알맞은 것을 고르시오."
S32 = "발문이 ‘주어·행동·시제와 진행의 의미를 가장 정확하게’라고 판단 기준을 알려 주었고 밑줄이 없었다. 원문항 발문과 밑줄로 되돌렸다."
mk(3, 32, "B", [("나는 가족과 함께 영화를 보고 있다.", "현재진행(보고 있다)으로 옮겨 과거(was)와 맞지 않으므로"), ("나는 가족과 함께 영화를 볼 것이다.", "미래로 옮겨 시제가 맞지 않으므로"), ("나는 가족과 함께 영화를 보고 있었다.", "was + -ing(과거진행)를 ‘보고 있었다’로 바르게 옮겼으므로"),
                ("나는 가족과 함께 영화를 자주 본다.", "현재의 습관으로 옮겨 시제와 진행의 뜻이 맞지 않으므로"), ("나는 가족과 함께 영화를 보지 않았다.", "부정의 뜻이 없는 문장을 부정으로 옮겼으므로")], 3,
   "was/were + -ing(과거진행형)는 과거의 어느 때에 진행 중이던 일을 나타낸다(~하고 있었다).",
   "제시문과 정답이 원문항과 똑같았고 발문도 판단 기준을 알려 주었다. 대화를 새로 쓰고 " + S32[S32.index("원문항 발문과"):], st=ST32,
   p="A: What were you doing last night?\nB: <u>I was watching a movie with my family</u>.")
for t in "CDEF":
    a_, b_ = V(3, 32, t)["passage"].split("\n")
    head, line = b_.split(": ", 1)
    F(3, 32, t, st=ST32, p=f"{a_}\n{head}: <u>{line}</u>", s=S32 + " 보기와 정답은 그대로다.")

# 3-33 진행형으로 쓰지 않는 동사: 원문항 발문, B는 정답 동사를 원문항과 다르게
ST33 = "다음 중 진행형으로 사용할 수 없는 동사를 고르시오."
S33 = "발문이 ‘기본 의미가 동작보다 상태를 나타내어’라고 정답의 성격을 설명해 주어 원문항 발문으로 되돌렸다."
def ACT(v): return f"{v}: 동작을 나타내는 동사라 진행형으로 쓸 수 있으므로"
mk(3, 33, "B", [("prefer", "prefer: ‘더 좋아하다’라는 상태를 나타내는 동사라 보통 진행형으로 쓰지 않으므로"), ("study", ACT("study")), ("write", ACT("write")), ("play", ACT("play")), ("run", ACT("run"))], 1,
   "진행형은 be동사 + -ing로 동작이 진행 중임을 나타낸다. know, want, believe, own, belong, prefer처럼 상태를 나타내는 동사는 보통 진행형으로 쓰지 않는다.",
   S33 + " 정답(belong)이 원문항과 같아 prefer로 바꿨다.", st=ST33)
for t in "CDEF":
    F(3, 33, t, st=ST33, s=S33 + " 보기와 정답은 그대로다.")

# 3-34 be / was·were / is·am·are: B는 문장을 새로, D는 주어를 바꿔 정답 조합을 다르게
AB3 = lambda x: [p.strip() for p in x.split(" - ")]
def f34(t, p, c, a, subj, s):
    good = AB3(c[a-1]); nn = []
    lab = ["첫째 빈칸", "둘째 빈칸", "셋째 빈칸"]
    why = [lambda x: "will 뒤에는 동사원형 be를 쓴다.", lambda x: f"과거진행형의 be동사는 주어({subj[1]})에 맞춰 {good[1]}를 쓴다.", lambda x: f"be going to의 be동사는 주어({subj[2]})에 맞춰 {good[2]}를 쓴다."]
    for i, ch in enumerate(c):
        parts = AB3(ch)
        if i + 1 == a: nn.append(f"{ch}: 세 빈칸이 모두 알맞으므로 정답이다."); continue
        nn.append(" ".join(f"{lab[j]} {x}: {why[j](x)}" for j, x in enumerate(parts) if x != good[j]) + " 따라서 오답이다.")
    F(3, 34, t, p=p, c=c, a=a, r="미래는 will + 동사원형 또는 be going to + 동사원형으로 나타내며, be going to와 과거진행형(was/were + -ing)의 be동사는 주어의 인칭·수에 맞춘다.",
      n=nn, k=f"will 뒤 원형 be, 주어({subj[1]})에 맞춘 {good[1]}, 주어({subj[2]})에 맞춘 {good[2]}이다.", s=s + ipos(a))
f34("B", "The kids will _____ excited about the trip.\nWe _____ having dinner when the phone rang.\nMy dad _____ going to wash the car tomorrow.",
    ["be - was - is", "being - were - is", "be - were - is", "be - were - are", "is - were - be"], 3, ["The kids", "We", "My dad"], "제시문과 정답이 원문항과 똑같아 문장을 새로 썼다.")
f34("D", "I will _____ busy tomorrow.\nJane _____ reading when I arrived.\nI _____ going to study tonight.",
    ["be - was - am", "be - was - is", "being - was - am", "is - was - be", "be - were - am"], 1, ["I", "Jane", "I"], "정답 조합(be - was - is)이 원문항과 같아 셋째 문장의 주어를 I로 바꿔 be - was - am이 되게 했다.")

# 3-35 B: 원문항과 같던 우리말 문장을 새로
mk(3, 35, "B", [("I am going learn to swim this summer.", "going 뒤에 to가 빠졌으므로"), ("I am will to learn to swim this summer.", "am과 will을 함께 쓸 수 없으므로"), ("I am going to learn to swim this summer.", "be going to + 동사원형으로 ‘~할 예정이다’를 바르게 나타냈으므로"),
                ("I going to learn to swim this summer.", "be동사(am)가 빠졌으므로"), ("I am going to be learn to swim this summer.", "to 뒤에 동사원형 learn만 써야 하므로")], 3,
   "be going to + 동사원형은 ‘~할 예정이다’라는 미래의 계획을 나타내며, be동사는 주어에 맞춘다.",
   "우리말과 정답이 원문항과 똑같았다. 우리말을 ‘나는 이번 여름에 수영을 배울 예정이다.’로 바꿨다.", p="나는 이번 여름에 수영을 배울 예정이다.")

# 3-37 상태동사 진행형 고치기: 원문항 발문·밑줄·우리말, 실제 형태의 오답으로
ST37 = "다음 밑줄 친 부분을 바르게 고친 것을 고르시오."
R37 = "상태를 나타내는 동사(know, want, believe, own, understand, have ‘가지고 있다’)는 보통 진행형으로 쓰지 않고 현재시제로 쓰며, 3인칭 단수 주어에는 -(e)s를 붙인다."
S37 = "발문이 ‘일반적인 현재 상태를 나타내는 현재 단순형으로 바꾼 것’이라고 정답을 알려 주었고 밑줄이 없었으며, 오답에 knowsed·believeing처럼 없는 형태가 많았다. 원문항 발문과 밑줄·우리말 뜻으로 되돌리고 오답을 실제 형태(was -ing, 원형, be + 원형 등)로 바꿨다."
def n37(x, right, subj):
    if x == right: return f"{x}: 상태동사를 현재시제로 쓰고 주어({subj})에 맞춘 알맞은 형태이므로"
    if x.startswith("was") or x.startswith("were"): return f"{x}: 과거진행형이라 현재의 상태를 나타내지 못하므로"
    if " " in x: return f"{x}: be동사와 일반동사를 함께 쓸 수 없으므로"
    return f"{x}: 주어({subj})와 수가 맞지 않으므로"
def f37(t, sent, ko, c, a, subj, s=S37):
    mk(3, 37, t, [(x, n37(x, c[a-1], subj)) for x in c], a, R37, s, st=ST37, p=f"{sent}\n({ko})")
f37("B", "My uncle <u>is having</u> a big house.", "우리 삼촌은 큰 집을 가지고 있다.", ["has", "have", "is have", "was having", "is has"], 1, "My uncle", S37 + " 제시문이 원문항과 똑같아 ‘My uncle is having a big house.’로 바꿨다.")
f37("C", "She <u>is wanting</u> a new phone.", "그녀는 새 휴대폰을 원한다.", ["was wanting", "want", "is want", "wants", "is wants"], 4, "She")
f37("D", "I <u>am believing</u> you.", "나는 너를 믿는다.", ["believes", "believe", "am believe", "was believing", "is believe"], 2, "I")
f37("E", "They <u>are owning</u> this house.", "그들은 이 집을 소유하고 있다.", ["owns", "are own", "were owning", "is own", "own"], 5, "They")
f37("F", "Tom <u>is understanding</u> the problem.", "톰은 그 문제를 이해한다.", ["understand", "is understand", "understands", "was understanding", "is understands"], 3, "Tom")

# 3-38 과거진행 의문문 세 빈칸: B는 대화를 새로, 네 단어 보기를 세 단어로
ST38 = "다음 대화에서 빈칸에 알맞은 표현을 고르시오."
R38 = "과거진행형 의문문은 Was/Were + 주어 + 동사-ing로 만들며, 대답(Yes, he was.)의 주어와 be동사에 맞춘다."
S38 = "빈칸은 세 개인데 네 단어로 된 보기(Was she is studying 등)가 섞여 원문항과 보기 형태가 달랐다. 원문항처럼 세 단어로 된 오답으로 바꿨다."
def n38(x, right, ans):
    if x == right: return f"{x}: 대답({ans})에 맞춘 과거진행형 의문문이므로"
    w = x.split()
    if w[0] in ("Is", "Are"): return f"{x}: 현재진행형이라 대답의 과거(was/were)와 맞지 않으므로"
    if w[0] in ("Did", "Do", "Does"): return f"{x}: do/does/did 의문문이라 대답의 be동사와 맞지 않으므로"
    if not w[2].endswith("ing"): return f"{x}: be동사 뒤에는 -ing 형태를 써야 하므로"
    return f"{x}: 주어와 be동사의 수가 맞지 않으므로"
def f38(t, p, c, a, ans, s=S38):
    mk(3, 38, t, [(x, n38(x, c[a-1], ans)) for x in c], a, R38, s, st=ST38, p=p, okdup=True)
f38("B", "Mina: ______ ______ ______ the dishes after dinner?\nJisu: Yes, he was.", ["Did he wash", "Is he washing", "Was he washing", "Was he wash", "Were he washing"], 3, "Yes, he was.",
    "대화와 정답이 원문항과 똑같아 대화를 새로 썼다.")
f38("C", "Jane: ______ ______ ______ English at 8?\nAmy: Yes, she was.", ["Is she studying", "Was she studying", "Was she study", "Does she study", "Did she studying"], 2, "Yes, she was.")
f38("D", "Tom: ______ ______ ______ soccer then?\nBen: Yes, they were.", ["Were they playing", "Did they playing", "Are they playing", "Do they play", "Were they play"], 1, "Yes, they were.")
f38("E", "Mina: ______ ______ ______ TV?\nLeo: Yes, he was.", ["Did he watching", "Does he watch", "Was he watch", "Was he watching", "Is he watching"], 4, "Yes, he was.")
f38("F", "Amy: ______ ______ ______ dinner?\nJane: Yes, I was.", ["Are you cooking", "Were you cook", "Did you cooking", "Do you cook", "Were you cooking"], 5, "Yes, I was.")

# 3-39 진행형 문장 짝: 원문항 발문·줄바꿈, 옳은 문장이 둘이 되게(두 기호 조합)
ST39 = "다음 중 어법상 옳은 문장으로만 짝지어진 것은?"
R39 = "현재진행형은 am/is/are + 동사-ing로 만들며 be동사는 주어에 맞춘다. -e로 끝나면 e를 빼고 -ing(write → writing), 단모음 + 단자음이면 자음을 한 번 더 쓴다(sit → sitting). know·want 같은 상태동사는 보통 진행형으로 쓰지 않는다."
S39 = "발문이 ‘모두 빠짐없이 고른 것’으로 원문항과 달랐고 줄바꿈이 없었다. 원문항 발문(옳은 문장으로만 짝지어진 것)과 줄바꿈으로 되돌리고, 옳은 문장이 둘인 두 기호 조합이 되게 조정했다."
CH39 = ["(가), (나)", "(가), (다)", "(나), (다)", "(나), (라)", "(다), (라)"]
def f39(t, lines, judge, ok, c, a, s=S39):
    F(3, 39, t, st=ST39, p="\n".join(lines), c=c, a=a, r=R39, pre=["문장별 판정: " + j for j in judge], k=f"옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), s=s + ipos(a))
f39("B", ["(가) My mom is cooking dinner now.", "(나) Tom is haveing lunch.", "(다) We are waiting for the bus.", "(라) She is knowing the answer."],
    ["(가) O. is + -ing의 현재진행형이다.", "(나) X. have는 e를 빼고 having으로 쓴다.", "(다) O. are + -ing의 현재진행형이다.", "(라) X. know는 상태동사라 보통 진행형으로 쓰지 않는다(She knows the answer)."],
    "(가), (다)", CH39, 2, "(가)~(다)가 원문항 문장과 같았고 정답 조합·위치도 같았다. 문장을 새로 쓰고 " + S39[S39.index("원문항 발문"):])
f39("C", ["(가) Tom is reading a book.", "(나) We are study English.", "(다) Jane is writing a letter.", "(라) They is playing soccer."],
    ["(가) O. is + -ing의 현재진행형이다.", "(나) X. are 뒤에는 studying을 쓴다.", "(다) O. is + -ing의 현재진행형이다.", "(라) X. 복수 주어(They)에는 are를 쓴다."],
    "(가), (다)", ["(가), (나)", "(나), (다)", "(나), (라)", "(다), (라)", "(가), (다)"], 5)
f39("D", ["(가) I am cooking dinner.", "(나) The boys are running.", "(다) She is know the answer.", "(라) Tom are watching TV."],
    ["(가) O. am + -ing의 현재진행형이다.", "(나) O. are + -ing이며 run은 n을 한 번 더 써 running이다.", "(다) X. is 뒤에 원형을 쓸 수 없고, know는 진행형으로도 쓰지 않는다.", "(라) X. 3인칭 단수 주어(Tom)에는 is를 쓴다."], "(가), (나)", CH39, 1)
f39("E", ["(가) We are leaveing now.", "(나) Jane is sleeping.", "(다) They are swimming in the pool.", "(라) I is reading."],
    ["(가) X. leave는 e를 빼고 leaving으로 쓴다.", "(나) O. is + -ing의 현재진행형이다.", "(다) O. are + -ing의 현재진행형이다.", "(라) X. 주어 I에는 am을 쓴다."], "(나), (다)", CH39, 3)
f39("F", ["(가) The dog are barking.", "(나) Tom is working.", "(다) I am want a bag.", "(라) We are cleaning."],
    ["(가) X. 단수 주어(The dog)에는 is를 쓴다.", "(나) O. is + -ing의 현재진행형이다.", "(다) X. am 뒤에 원형을 쓸 수 없고, want는 진행형으로도 쓰지 않는다.", "(라) O. are + -ing의 현재진행형이다."], "(나), (라)", CH39, 4)

# 3-40 지문 설명 중 옳지 않은 것: 원문항처럼 밑줄 표현은 모두 옳게, 틀린 설명 하나
ST40 = "다음 지문의 밑줄 친 ⓐ~ⓔ 중, 한국어 문법 설명이 옳지 않은 것은?"
R40 = "과거의 일은 과거형(규칙 -ed, 불규칙 변화), 과거에 진행 중이던 일은 was/were + -ing로 나타낸다. did not 뒤에는 동사원형을 쓰고, be going to + 동사원형은 미래의 계획을 나타낸다."
S40 = "원문항은 옳은 표현에 대한 잘못된 설명을 찾는 문항인데, 변형은 지문에 실제 오류를 넣고 ‘과거 문맥에서도 올바르다’는 설명을 찾게 해 판단 구조가 바뀌었고 발문도 판단 기준을 알려 주었다. 원문항 발문과 형식으로 되돌려, 지문의 밑줄 표현은 모두 옳게 두고 그중 하나에 대한 그럴듯한 틀린 설명을 넣었다."
talk(3, 40, "B", [("ⓐ는 visit의 규칙 과거형으로 -ed를 붙였다.", "visited는 규칙 과거형이다."), ("ⓑ: did not 뒤에는 동사원형을 쓰므로 go는 알맞다.", "didn't + 동사원형이다."),
                  ("ⓒ는 현재진행형이므로 과거 문맥에 맞지 않는다.", "was baking은 과거에 진행 중이던 일을 나타내는 과거진행형이다."), ("ⓓ: arrive는 -e로 끝나 -d만 붙여 과거형을 만들었다.", "arrived는 규칙 과거형이다."),
                  ("ⓔ는 미래의 계획을 나타내며 뒤에 동사원형이 온다.", "be going to + 동사원형이다.")], 3, R40, S40, st=ST40,
     p="Dear Diary,\nLast Saturday was fun. I ⓐ<u>visited</u> my grandparents. We ⓑ<u>didn't go</u> out because it rained. Grandma ⓒ<u>was baking</u> cookies when I ⓓ<u>arrived</u>. Tomorrow, I ⓔ<u>am going to</u> call them.")
talk(3, 40, "C", [("ⓐ went는 ‘가다(go)’의 과거형으로 불규칙하게 변한 것이다.", "went는 go의 과거형이다."), ("ⓑ는 과거의 특정 시점(정오)에 진행 중이던 동작을 나타낸다.", "was studying은 과거진행형이다."),
                  ("ⓓ는 복수 주어에 맞춰 were를 쓴 과거진행형이다.", "복수 주어의 과거진행형이다."), ("ⓔ: did not 뒤이므로 동사원형 come을 썼다.", "didn't + 동사원형이다."),
                  ("ⓒ: buy의 과거형은 buyed이므로 bought는 틀린 표현이다.", "buy의 과거형은 bought이므로 ⓒ는 옳고, 이 설명이 틀렸다.")], 5, R40, S40, st=ST40,
     p="Yesterday, Tom ⓐ<u>went</u> to school. He ⓑ<u>was studying</u> at noon. Later he ⓒ<u>bought</u> a snack. His friends ⓓ<u>were playing</u> soccer. He ⓔ<u>didn't come</u> home late.")
talk(3, 40, "D", [("ⓓ was는 3인칭 단수 주어(Jane)의 과거 상태를 나타낸다.", "단수 주어의 과거는 was이다."), ("ⓑ was cooking은 과거진행형이다.", "과거에 진행 중이던 일이다."), ("ⓐ visited는 규칙 과거형이다.", "visited는 규칙 과거형이다."),
                  ("ⓒ: eat은 규칙동사라 과거형은 ate가 아니라 eated이다.", "eat은 불규칙동사라 과거형은 ate이므로 ⓒ는 옳고, 이 설명이 틀렸다."), ("ⓔ: 집에 간 과거의 일을 go의 과거형으로 나타냈다.", "went는 go의 과거형이다.")], 4, R40, S40 + " 지문이 원문항의 절반에 못 미쳐, 밑줄 친 표현은 그대로 두고 지문을 원문항 수준으로 늘렸다.", st=ST40,
     p="Last Sunday, Jane ⓐ<u>visited</u> her aunt in the countryside. When she got there, her aunt ⓑ<u>was cooking</u> in the kitchen. They ⓒ<u>ate</u> dinner together and talked for a long time. Jane ⓓ<u>was</u> very happy and ⓔ<u>went</u> home late in the evening.")
talk(3, 40, "E", [("ⓐ played는 규칙 과거형이다.", "played는 규칙 과거형이다."), ("ⓔ: 주어 We가 복수이지만 과거이므로 was를 써야 한다.", "복수 주어의 과거는 were이므로 ⓔ는 옳고, 이 설명이 틀렸다."),
                  ("ⓒ는 fall의 과거형으로 불규칙 변화한 것이다.", "fell은 fall의 과거형이다."), ("ⓓ helped는 규칙 과거형이다.", "helped는 규칙 과거형이다."), ("ⓑ was running은 과거진행형이다.", "과거에 진행 중이던 일이다.")], 2, R40, S40 + " 지문이 원문항의 절반에 못 미쳐, 밑줄 친 표현은 그대로 두고 지문을 원문항 수준으로 늘렸다.", st=ST40,
     p="Yesterday, we ⓐ<u>played</u> soccer in the park after school. Tom ⓑ<u>was running</u> fast with the ball when Jane ⓒ<u>fell</u> down in front of him. We ⓓ<u>helped</u> her right away and ⓔ<u>were</u> very worried about her.")
talk(3, 40, "F", [("ⓐ: read는 현재형이므로 과거 문맥에서는 readed로 고쳐야 한다.", "read는 과거형도 철자가 read이므로 ⓐ는 옳고, 이 설명이 틀렸다."), ("ⓒ made는 make의 불규칙 과거형이다.", "made는 make의 과거형이다."),
                  ("ⓑ was watching은 과거진행형이다.", "과거에 진행 중이던 일이다."), ("ⓓ ate는 eat의 불규칙 과거형이다.", "ate는 eat의 과거형이다."), ("ⓔ: 잠자리에 든 과거의 일을 불규칙 과거형 went로 나타냈다.", "went는 go의 과거형이다.")], 1, R40, S40 + " 지문이 원문항의 절반에 못 미쳐, 밑줄 친 표현은 그대로 두고 지문을 원문항 수준으로 늘렸다.", st=ST40,
     p="Last night, I ⓐ<u>read</u> a book in my room for an hour. My sister ⓑ<u>was watching</u> TV in the living room. Mom ⓒ<u>made</u> dinner for us. We ⓓ<u>ate</u> together at seven and ⓔ<u>went</u> to bed early.")
