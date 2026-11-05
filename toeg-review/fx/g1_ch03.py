# 1급 CH3 조동사 (21~30) 수정 예시

# 1-22 D: 원문항과 거의 같은 문장 → 다른 동사·상황
c = ["walk - to take", "to walk - take", "walks - takes", "walking - take", "walk - take"]
F(1, 22, "D", p="Tom would rather _____ to work than _____ a crowded bus.", c=c, a=5,
  k="would rather와 than 뒤의 두 동작 모두 동사원형이므로 walk - take가 알맞다.",
  n=tnotes(c, 5, ["would rather 뒤에는 동사원형을 쓴다.", "than 뒤의 동작도 would rather에 이어지므로 동사원형을 쓴다."], "would rather와 than 뒤의 두 동작 모두 동사원형이므로 walk - take가 알맞다."),
  s="원문항 ‘stay at home than go to a crowded restaurant’와 거의 같던 문장을 ‘walk to work than take a crowded bus’로 바꾸고, 오답을 같은 동사의 다른 형태로 만들었다.")

# 1-23 줄바꿈 복원
S23 = "‘/’로 이어 쓴 두 문장을 원문항처럼 • 두 줄로 나눴다. 문장과 정답은 그대로다."
for t in "CDEF":
    a, b = V(1, 23, t)["passage"].split(" / ")
    F(1, 23, t, p=f"• {a}\n• {b}", keepx=True, s=S23)

# 1-24 원형가정법: 평가 문법을 알려 주던 발문을 원문항대로
for t in "CDEF":
    F(1, 24, t, st="R", xr=[("이 문항에서 지정한 원형가정법에서는", "요구·제안을 나타내는 that절에서는")], s="발문이 ‘원형가정법으로 표현한 문장’이라고 평가 문법을 알려 주어, 원문항 발문 ‘밑줄 친 부분 중 어법상 옳지 않은 것’으로 되돌렸다. 본문과 보기는 그대로다.")

# 1-25 틀린 문장 조합
c = ["A, B, C", "A, C, E", "B, D, F", "A, E, F", "C, D, E"]
F(1, 25, "C", st="R", p="A) You had better to take a taxi.\nB) Mina might have missed the train.\nC) They must not to use their phones here.\nD) There used to be a pond here.\nE) I am used to get up early.\nF) Jane may be at the library now.",
  c=c, a=2,
  pre=["문장별 판정:", "A) 틀림: had better 뒤에는 동사원형을 쓴다. had better to take → had better take.", "B) 옳음: might have missed는 과거에 대한 불확실한 추측이다.",
       "C) 틀림: 조동사 must not 뒤에는 동사원형을 쓴다. must not to use → must not use.", "D) 옳음: used to be는 과거에 있었던 상태를 나타낸다.",
       "E) 틀림: be used to의 to는 전치사라 뒤에 동명사가 온다. am used to get → am used to getting.", "F) 옳음: may be는 현재에 대한 추측이다."],
  k="어법상 틀린 문장은 A, C, E이다.", n=setnotes(c, "A, C, E"),
  s="원문항과 거의 같던 A(than to drive)·F(musts)와 여러 유형에 반복된 E(There used to being)를 다른 오류(had better to / must not to / be used to + 원형)로 바꿔, 정답 조합을 원문항(A, E, F)과 다른 A, C, E로 만들었다. 발문을 원문항과 같게 하고 줄을 바꿨다.")
# 1-25 B·D·E·F: B 검토 의견(각 선택지를 세 문장 조합으로) 반영, 원문항처럼 틀린 문장 셋·보기 모두 세 문장 조합
def f25(t, lines, judge, c, ok, s):
    a = c.index(ok) + 1
    F(1, 25, t, st="R", p="\n".join(lines), c=c, a=a, pre=["문장별 판정:"] + judge, k=f"어법상 틀린 문장은 {ok}이다.", n=setnotes(c, ok), s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
S25 = "발문이 원문항과 달랐고, 정답이 {x} 조합이라 세 문장 조합을 고르는 원문항과 짜임이 달랐다(B 검토 의견과 같은 문제). 원문항 발문으로 되돌리고, 틀린 문장이 세 개가 되도록 문장을 고쳐 보기를 모두 세 문장 조합으로 바꿨다. 여러 유형에 반복되던 오류(There used to being)는 다른 오류로 바꾸고, 한 줄에 한 문장씩 나눴다."
f25("B", ["A) Mina would rather travel than staying home.", "B) Tom may have left already.", "C) He cannot be joking.", "D) We are used to study together.", "E) There used to being an old bridge here.", "F) Jane must finish the work."],
    ["A) 틀림: would rather A than B에서 than 뒤에도 동사원형을 쓴다. than staying → than stay.", "B) 옳음: may have left는 이미 떠났을 가능성을 나타낸다.", "C) 옳음: cannot be joking은 농담일 가능성을 강하게 부정한다.",
     "D) 틀림: be used to의 to는 전치사라 뒤에 동명사가 온다. are used to study → are used to studying.", "E) 틀림: 과거의 상태를 나타내는 used to 뒤에는 원형 be가 필요하다. used to being → used to be.", "F) 옳음: must 뒤에 동사원형 finish를 썼다."],
    ["A, B, C", "B, C, F", "A, D, E", "A, C, E", "B, D, F"], "A, D, E",
    "검토 의견(각 선택지를 세 문장 조합으로)에 따라, 원문항처럼 틀린 문장을 세 개로 만들고(D를 be used to + 동사원형 오류로 바꿈) 보기를 모두 세 문장 조합으로 바꿨다. 정답 조합은 원문항(A, E, F)과 다르게 했다. 발문도 원문항 ‘어법상 틀린 문장들로만 구성된 것’으로 되돌렸다.")
f25("D", ["A) Tom would rather stay home than go out.", "B) Jane may has forgotten the password.", "C) She should have call me earlier.", "D) I am used to taking the subway.", "E) There used to be a school here years ago.", "F) We would rather not to leave now."],
    ["A) 옳음: would rather stay than go에서 stay와 go가 모두 동사원형이다.", "B) 틀림: 조동사 may 뒤에는 원형 have를 쓴다. may has forgotten → may have forgotten.", "C) 틀림: should have 뒤에는 과거분사를 쓴다. should have call → should have called.",
     "D) 옳음: be used to에서 to는 전치사이며 동명사 taking이 이어져 익숙함을 나타낸다.", "E) 옳음: used to be가 과거에 학교가 있었다는 상태를 나타낸다.", "F) 틀림: would rather의 부정은 would rather not + 동사원형이다. would rather not to leave → would rather not leave."],
    ["A, B, C", "A, D, E", "B, D, F", "B, C, F", "C, E, F"], "B, C, F", S25.format(x="두 문장(A, E)"))
f25("E", ["A) We would rather leave now than waiting here.", "B) Mina could have called earlier.", "C) Tom can working now.", "D) She is used to living alone.", "E) There used to be a theater here long ago.", "F) He will can finish the report today."],
    ["A) 틀림: would rather A than B에서 than 뒤에도 동사원형을 쓴다. than waiting → than wait.", "B) 옳음: could have called는 더 일찍 전화할 수 있었다는 뜻을 나타낸다.", "C) 틀림: 조동사 can 뒤에는 동사원형을 쓴다. can working → can work.",
     "D) 옳음: be used to에서 to는 전치사이며 동명사 living이 이어져 익숙함을 나타낸다.", "E) 옳음: used to be가 과거에 극장이 있었다는 상태를 나타낸다.", "F) 틀림: 조동사 두 개를 이어 쓸 수 없다. will can finish → will be able to finish."],
    ["A, B, C", "B, D, E", "C, D, F", "A, E, F", "A, C, F"], "A, C, F", S25.format(x="두 문장(C, E)"))
f25("F", ["A) Jane would rather read than watch TV.", "B) Tom might have took the wrong bus.", "C) He cannot have known everything.", "D) I used to getting up early.", "E) There used to be a factory here.", "F) Mina has to studies more."],
    ["A) 옳음: would rather read than watch에서 read와 watch가 모두 동사원형이다.", "B) 틀림: might have 뒤에는 과거분사를 쓴다. might have took → might have taken.", "C) 옳음: cannot have known은 과거에 모든 것을 알았을 가능성을 강하게 부정한다.",
     "D) 틀림: 과거의 습관을 나타내는 used to 뒤에는 동사원형을 쓴다. used to getting up → used to get up(익숙함이라면 am used to getting up).", "E) 옳음: used to be가 과거에 공장이 있었다는 상태를 나타낸다.", "F) 틀림: has to 뒤에는 동사원형을 쓴다. has to studies → has to study."],
    ["B, D, F", "A, B, C", "C, D, E", "A, E, F", "B, C, D"], "B, D, F", S25.format(x="한 문장(F)").replace(" 여러 유형에 반복되던 오류(There used to being)는 다른 오류로 바꾸고,", " 원문항과 같던 오류(musts)는 다른 오류로 바꾸고,"))

# 1-26 have to의 시제: 발문의 시제 조건 대신 문장 속 시간 단서로 판단
R26 = "현재의 의무는 주어에 따라 have to/has to, 과거의 의무는 had to, 미래의 의무는 will have to로 나타낸다. must 뒤에는 to 없이 동사원형을 쓴다."
def ht(x, subj, when, good):
    if x == good: return f"{when}의 의무를 주어에 맞게 {good}로 바르게 나타냈다. 정답이다."
    if x == "must to": return "must 뒤에는 to 없이 동사원형을 쓰므로 must to는 틀린 형태이다."
    if x == "will has to": return "will 뒤에는 동사원형을 쓰므로 will has to는 틀린 형태이다."
    if x == "had to": return f"had to는 과거의 의무라 {when}에 맞지 않는다."
    if x == "will have to": return f"will have to는 미래의 의무라 {when}에 맞지 않는다."
    if good in ("have to", "has to"):
        return f"주어({subj})에 맞추면 {x}가 아니라 {good}를 써야 한다."
    if x == "has to" and subj == "I": return "주어 I에는 has to를 쓰지 않는다."
    return f"{x}는 현재의 의무라 {when}에 맞지 않는다."
F(1, 26, "C", st="R", p="These days, Mina ________ submit a report every Friday.", r=R26,
  n=[ht(x, "Mina", "These days(요즘)", "has to") for x in V(1, 26, "C")["c"]],
  s="발문이 ‘현재 시제·단순현재형’을 알려 주어 수 일치만 남았다. 발문을 원문항과 같게 하고, 문장에 These days·every Friday라는 현재 습관 단서를 넣어 시제를 스스로 판단하게 했다.")
F(1, 26, "D", st="R", p="Nowadays, all visitors ________ wear a badge inside the laboratory.", r=R26,
  n=[ht(x, "all visitors", "Nowadays(요즘)", "have to") for x in V(1, 26, "D")["c"]],
  s="발문의 시제 조건을 지워 원문항 발문으로 되돌리고, 문장에 Nowadays라는 현재 단서를 넣었다. 조건 없이도 will have to가 답이 되지 않는다.")
F(1, 26, "E", st="R", r=R26, n=[ht(x, "Tom", "last week(지난주)", "had to") for x in V(1, 26, "E")["c"]],
  s="문장에 last week 단서가 있는데 발문이 ‘과거 시제로’라고 다시 알려 주었다. 원문항 발문 ‘빈칸에 들어갈 말로 가장 적절한 것’으로 되돌렸다.")
c = ["will have to", "will has to", "must to", "has to", "had to"]
F(1, 26, "F", st="R", c=c, r=R26, n=[ht(x, "I", "next month(다음 달) 여행 전", "will have to") for x in c],
  s="발문 조건(‘미래 시제로’)이 없으면 ② have to도 여행 전의 의무로 자연스러워 복수 정답이 되었다. ②를 명백히 틀린 ‘will has to’로 바꾸고 발문을 원문항과 같게 했다.")

# 1-27 should have p.p.(후회) + might have p.p.(가능성)
U = "(<u>    {}    </u>)"
F(1, 27, "B", p=f"A: I missed the deadline by one day.\nB: You {U.format('A')} have checked the date. The office {U.format('B')} accept a late submission if you ask.", keepx=True,
  c=["(A) {} - (B) {}".format(*x.split(" - ")) for x in V(1, 27, "B")["c"]],
  s="원문항처럼 빈칸 (A)(B)에 밑줄을 넣고, 보기에도 (A), (B) 표시를 붙였다. 대화와 정답은 그대로다.")
F(1, 27, "C", st="R", p=f"A: I sent the file without checking it.\nB: You {U.format('A')} have reviewed it first. The wrong version {U.format('B')} have caused confusion.",
  c=["(A) {} - (B) {}".format(*x.split(" - ")) for x in V(1, 27, "C")["c"]],
  r="should have + 과거분사는 하지 않은 과거 행동에 대한 후회·비판을, might have + 과거분사는 과거 일에 대한 불확실한 추측을 나타낸다.",
  k="(A)는 파일을 확인하지 않은 일에 대한 후회, (B)는 잘못된 파일이 혼란을 일으켰을지도 모른다는 추측이므로 should - might가 알맞다.",
  n=mnotes(V(1, 27, "C")["c"], 2, ["파일을 확인하지 않은 일을 아쉬워하는 흐름", "혼란이 생겼을지도 모른다고 추측하는 흐름"], "(A)는 파일을 확인하지 않은 일에 대한 후회, (B)는 혼란이 생겼을지도 모른다는 추측이므로 should - might가 알맞다."),
  s="발문 괄호가 (A)·(B)의 뜻을 직접 알려 주어 원문항 발문으로 되돌리고 빈칸에 밑줄을 넣었다. 괄호가 없어도 (A)는 파일을 확인하지 않은 일에 대한 후회라 should만 맞아 정답이 하나다. 보기에도 (A), (B) 표시를 붙였다.")
R27 = "should have + 과거분사는 하지 않은 과거 행동에 대한 후회·비판을, might have + 과거분사는 과거 일에 대한 불확실한 추측을 나타낸다."
S27 = "원문항은 should have p.p.(후회)와 might have p.p.(가능성)를 묻는데 변형은 ‘과거 추측 + 현재 추측’으로 평가 요소가 바뀌었고, 조건이 없으면 must have p.p.도 맞아 답이 흔들렸다. 원문항처럼 후회 + ‘Or,’로 여는 다른 가능성 대화로 새로 쓰고 선택지도 새로 만들었다."
def f27(t, dia, c, a, ctx, k, extra):
    F(1, 27, t, st="R", p=dia, c=c, a=a, r=R27, k=k, n=mnotes(c, a, ctx, k), s=S27 + extra)
f27("D", f"A: I lost my wallet somewhere today.\nB: You {U.format('A')} have kept it in your bag. Or, someone {U.format('B')} have picked it up at the café.",
    ["(A) must - (B) cannot", "(A) should - (B) might", "(A) might - (B) should", "(A) cannot - (B) must", "(A) should - (B) must not"], 2,
    ["지갑을 가방에 넣지 않은 일을 아쉬워하는 흐름", "Or로 다른 가능성을 떠올리는 흐름"], "(A)는 지갑을 가방에 넣지 않은 일에 대한 아쉬움, (B)는 Or로 여는 다른 가능성이므로 should - might가 알맞다.", " 정답 위치 ②.")
f27("E", f"A: I failed the test because I didn't study.\nB: You {U.format('A')} have studied harder. Or, the questions {U.format('B')} have been harder than usual.",
    ["(A) should - (B) must not", "(A) might - (B) cannot", "(A) must - (B) should", "(A) cannot - (B) must", "(A) should - (B) might"], 5,
    ["공부하지 않은 일을 아쉬워하는 흐름", "Or로 다른 가능성을 떠올리는 흐름"], "(A)는 공부하지 않은 일에 대한 비판, (B)는 Or로 여는 다른 가능성이므로 should - might가 알맞다.", " 정답 위치 ⑤.")
f27("F", f"A: My plant died while I was on vacation.\nB: You {U.format('A')} have asked someone to water it. Or, it {U.format('B')} have gotten too much sun by the window.",
    ["(A) might - (B) must", "(A) must - (B) cannot", "(A) should - (B) must not", "(A) should - (B) might", "(A) cannot - (B) should"], 4,
    ["물을 부탁하지 않은 일을 아쉬워하는 흐름", "Or로 다른 가능성을 떠올리는 흐름"], "(A)는 물을 부탁하지 않은 일에 대한 아쉬움, (B)는 Or로 여는 다른 가능성이므로 should - might가 알맞다.", " 정답 위치 ④.")

# 1-28 had better not 배열: 오답을 제시어 어순만 바꾼 배열로
F(1, 28, "B", st="R", p="(not / decision / you'd / the / better / postpone / .)", s="발문을 원문항 ‘단어들을 바르게 배열하여 문장을 완성한 것’으로 되돌리고, 원문항에 없는 우리말 뜻 줄을 지웠다. 보기는 그대로다.")
R28 = "had better의 부정은 had better not + 동사원형 어순이다. 주어 + ’d(had)가 먼저 오고, 목적어는 동사 뒤에 둔다."
NOTB = "not은 had better 뒤에 와야 한다. had better not + 동사원형 어순이 아니므로 오답이다."
BEFORE = "주어 + ’d가 문장 맨 앞에 와야 하는데 어순이 뒤바뀌었으므로 오답이다."
OBJ = "목적어가 동사 앞에 왔다. 동사 뒤에 목적어를 두어야 하므로 오답이다."
NOTV = "not이 동사 뒤로 갔다. not은 동사원형 앞, had better 바로 뒤에 와야 하므로 오답이다."
S28 = "발문이 ‘had better 부정문’이라고 구조를 알려 주고, 오답이 would·to를 더하거나 not을 빼서 ‘한 번씩 사용’ 조건만으로 지워졌다. 발문을 원문항과 같게 하고, 오답을 원문항처럼 제시어의 어순만 바꾼 배열로 새로 만들었다."
def f28(t, c, a, notes, extra):
    F(1, 28, t, st="R", c=c, a=a, r=R28, n=[("주어 + ’d + better not + 동사원형 + 목적어 어순이 바르다. 정답이다." if i + 1 == a else notes[i]) for i in range(5)], s=S28 + extra)
f28("C", ["We'd better not ignore the warning.", "We'd not better ignore the warning.", "We'd better ignore not the warning.", "Better not we'd ignore the warning.", "We'd better not the warning ignore."], 1,
    [None, NOTB, NOTV, BEFORE, OBJ], "")
f28("D", ["They'd not better miss the train.", "They'd better the train not miss.", "They'd better not miss the train.", "Not they'd better miss the train.", "They'd better miss not the train."], 3,
    [NOTB, OBJ, None, BEFORE, NOTV], " 정답 위치 ③.")
f28("E", ["She'd not better forget the key.", "Better she'd not forget the key.", "She'd better forget not the key.", "She'd better not the key forget.", "She'd better not forget the key."], 5,
    [NOTB, BEFORE, NOTV, OBJ, None], " 정답 위치 ⑤.")
f28("F", ["He'd not better drive so fast.", "He'd better not drive so fast.", "Better he'd not drive so fast.", "He'd better not so fast drive.", "Not he'd better drive so fast."], 2,
    [NOTB, None, BEFORE, "so fast가 동사 앞에 왔다. 동사 drive 뒤에 두어야 하므로 오답이다.", BEFORE], " 정답 위치 ②.")

# 1-29 제안·요구의 that절 동사원형: 없는 형태 오답을 실제 형태로
R29 = "suggest·recommend·insist·demand가 ‘~해야 한다고 제안·요구하다’의 뜻일 때 that절의 동사는 주어의 인칭·수·시제와 관계없이 (should +) 동사원형을 쓴다. 수동이면 be + 과거분사를 쓴다."
def sub(x, good, verb):
    if x == good: return f"{verb}의 that절에 주어와 관계없이 동사원형({good})을 바르게 썼다. 정답이다."
    return f"{x}: {vform(x)}이어서 맞지 않는다. {verb}의 that절에는 동사원형을 쓴다. 오답이다."
def f29(t, c, a, good, verb, stem, s):
    kw = dict(st="R") if stem else {}
    F(1, 29, t, c=c, a=a, r=R29, n=[sub(x, good, verb) for x in c], s=s, **kw)
f29("B", ["practices", "practiced", "has practiced", "practice", "is practicing"], 4, "practice", "suggested", False,
    "존재하지 않는 형태(practiceed, has practice, is practice) 오답을 실제 형태(practices / practiced / has practiced / is practicing)로 바꿔 모든 보기가 경쟁하게 했다.")
f29("C", ["sees", "saw", "is seeing", "has seen", "see"], 5, "see", "recommended", True,
    "발문의 ‘원형가정법’ 설명을 지워 원문항 발문으로 되돌리고, 없는 형태(seeed, is see, has see) 오답을 sees / saw / is seeing / has seen으로 바꿨다.")
F(1, 29, "D", st="R", r=R29, n=[sub(x, "be", "proposed") if x != "be" else "proposed의 that절에 동사원형 be를 써서 규칙이 개정되는 수동(be revised)을 바르게 나타냈다. 정답이다." for x in V(1, 29, "D")["c"]], s="발문의 ‘원형가정법으로 나타내려고 한다’ 설명을 지워 원문항 발문으로 되돌렸다. 보기는 모두 실제 형태라 그대로 쓴다.")
f29("E", ["is arriving", "arrive", "has arrived", "arrives", "arrived"], 2, "arrive", "insisted", True,
    "발문의 요구 내용·‘원형가정법’ 설명을 지워 원문항 발문으로 되돌리고, 없는 형태 오답을 is arriving / has arrived / arrives / arrived로 바꿨다.")
c = ["has been submitted", "is submitted", "was submitted", "submits", "be submitted"]
F(1, 29, "F", c=c, a=5, r=R29,
  n=[f"{x}: {vform(x) if x != 'is submitted' else '현재 수동태'}이어서 맞지 않는다. demanded의 that절에는 (should +) 동사원형을 쓰고, 보고서가 제출되는 것이므로 be submitted가 된다. 오답이다." if x != "be submitted" else "demanded의 that절에 동사원형 수동 be submitted를 바르게 썼다. 정답이다." for x in c],
  s="존재하지 않는 형태(has be submitted, be submitteded 등) 오답을 실제 형태(has been submitted / is submitted / was submitted / submits)로 바꿨다.")

# 1-30 B 검토 의견(지문이 너무 짧음) 반영: 원문항처럼 상황 두 문장 + 후회를 드러내는 말, ‘Looking back,’ 앞 줄바꿈
R30 = "과거에 했어야 했지만 하지 않은 일을 후회할 때는 should have + 과거분사를 쓴다. must have + 과거분사는 과거 일에 대한 강한 추측이라 후회의 뜻이 아니다. 조동사 뒤에는 have를 빼거나(should gone) to를 넣을(should have to gone) 수 없다."
def n30(o, verb):
    if o.split()[1:3] == ["should", "have"] and o.split()[3] != "to": return f"‘{o}’는 하지 않은 일을 후회하는 should have + 과거분사라 문맥에 맞으므로 정답이다."
    if "must have" in o: return f"‘{o}’의 must have + 과거분사는 과거 일에 대한 강한 추측이라, 하지 않은 일을 후회하는 문맥에 맞지 않으므로 오답이다."
    if "should have to" in o: return f"‘{o}’는 should have 뒤에 to를 넣어 형태가 틀렸으므로 오답이다."
    if " could " in f" {o} ": return f"‘{o}’는 could 뒤에 have가 빠져 형태가 틀렸으므로 오답이다."
    return f"‘{o}’는 should 뒤에 have가 빠져 형태가 틀렸으므로 오답이다."
S30 = "원문항보다 지문이 한참 짧아 상황을 읽고 판단할 거리가 적었다(B 검토 의견과 같은 문제). 원문항처럼 상황을 설명하는 문장 두 개와 후회를 드러내는 말을 넣어 지문을 원문항 길이로 늘리고, ‘Looking back,’ 앞에서 줄을 바꿨다. 밑줄과 보기, 정답은 그대로다."
P30 = {
 "B": "Tom had an important exam this morning, but he stayed up all night playing online games. During the exam, he felt so tired that he could not focus on the questions.\nLooking back, <u>he thinks he must have gone to bed earlier</u>, and he regrets it now.",
 "C": "Mina saw the weather forecast on the news, but she ignored the warning about heavy rain. On her way home from school, she got soaked from head to toe.\nLooking back, <u>she thinks she must have taken an umbrella</u>, and she feels sorry that she did not listen.",
 "D": "Jane had two weeks to write her science report, but she waited until the night before the deadline to start. She could not finish it in time and lost points.\nLooking back, <u>she thinks she must have begun sooner</u>, and she wishes she had planned better.",
 "E": "Last Saturday, our family drove to a new beach without looking at the map. We took a wrong turn and spent two hours on the road instead of thirty minutes.\nLooking back, <u>we think we must have checked the route first</u>, and we are sorry about the lost time.",
 "F": "Leo got his allowance at the start of the month, but he spent almost all of it on snacks and games in the first week. When his best friend's birthday came, he could not buy a present.\nLooking back, <u>he thinks he must have saved more</u>, and he regrets it now."}
for t in "BCDEF":
    V_ = V(1, 30, t); a = int(V_["ans"])
    F(1, 30, t, p=P30[t], r=R30, k=f"지문은 이미 지나간 일을 후회하는 상황이므로 should have + 과거분사인 ‘{V_['c'][a-1]}’가 알맞다.", n=[n30(o, None) for o in V_["c"]],
      s=("검토 의견(지문이 너무 짧음)에 따라, 원문항처럼 상황을 설명하는 문장 두 개와 후회를 드러내는 말을 넣어 지문을 원문항 길이로 늘리고, ‘Looking back,’ 앞에서 줄을 바꿨다. 밑줄과 보기, 정답은 그대로다." if t == "B" else S30) + f" 정답 위치 {'①②③④⑤'[a-1]}.")
