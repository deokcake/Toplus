# 3급 CH6 조동사 (51~60) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]

# 3-51 B: 원문항과 같던 우리말을 새로
mk(3, 51, "B", [("You must to be quiet in class.", "must 뒤에는 to 없이 동사원형을 쓰므로"), ("You may be quiet in class.", "may는 허락·추측의 뜻이라 ‘~해야 한다’와 맞지 않으므로"), ("You must be quiet in class.", "의무의 must + 동사원형(be)으로 바르게 옮겼으므로"),
                ("You must being quiet in class.", "must 뒤에는 동사원형을 쓰므로"), ("You can be quiet in class.", "can은 능력·허락의 뜻이라 ‘~해야 한다’와 맞지 않으므로")], 3,
   "must·have to는 의무(~해야 한다)를 나타내며, 조동사 뒤에는 to 없이 동사원형을 쓴다.", "우리말과 정답이 원문항과 똑같았다. 우리말을 ‘너는 수업 중에 조용히 해야 한다.’로 바꿨다.", p="너는 수업 중에 조용히 해야 한다.")

# 3-52 must be / can't be 짝: B·F는 우리말을 새로
R52 = "강한 긍정 추측(~임에 틀림없다)은 must be, 강한 부정 추측(~일 리가 없다)은 can't be로 나타내며, 조동사 뒤에는 동사원형 be를 쓴다."
def n52(ch, good):
    a, b = [x.strip() for x in ch.split(" - ")]
    if ch == good: return "must be(틀림없다)와 can't be(~일 리 없다)로 두 문장을 모두 바르게 옮겼으므로"
    bits = []
    if " must be " not in " " + a + " ": bits.append("첫째 문장은 ‘틀림없다’이므로 must be를 써야 한다" + ("(be가 빠졌다)" if "must " in a and "must be" not in a else ""))
    if "can't be" not in b: bits.append("둘째 문장은 ‘~일 리가 없다’이므로 can't be를 써야 한다")
    return ", ".join(bits) + ". 따라서"
def f52(t, ko, c, a, s):
    mk(3, 52, t, [(x, n52(x, c[a-1])) for x in c], a, R52, s, p=ko, okdup=True)
f52("B", "그 식당은 인기가 있음에 틀림없다.\n그것이 비쌀 리가 없다.",
    ["The restaurant must be popular. - It can't be expensive.", "The restaurant may be popular. - It must be expensive.", "The restaurant must popular. - It can't be expensive.", "The restaurant can't be popular. - It must be expensive.", "The restaurant should be popular. - It may be expensive."], 1,
    "우리말과 정답이 원문항과 똑같았다. 우리말을 ‘그 식당은 인기가 있음에 틀림없다 / 그것이 비쌀 리가 없다’로 바꿨다.")
f52("F", "그 이야기는 진짜임에 틀림없다.\n그것이 거짓말일 리가 없다.",
    ["The story must not be real. - It can be a lie.", "The story must be real. - It can't be a lie.", "The story should be real. - It may be a lie.", "The story may be real. - It must be a lie.", "The story can't be real. - It must be a lie."], 2,
    "첫 문장(그 소식은 사실임에 틀림없다 / The news must be true)이 원문항과 같았다. 우리말을 ‘그 이야기는 진짜임에 틀림없다 / 그것이 거짓말일 리가 없다’로 바꿨다.")

# 3-53 had better 의미: 원문항 발문·밑줄, 원문항처럼 비슷한 조동사 뜻의 오답
ST53 = "밑줄 친 부분의 의미로 알맞은 것을 고르시오."
R53 = "had better + 동사원형은 ‘~하는 것이 좋겠다’는 강한 충고이다. can(~할 수 있다), must(~해야만 한다), must not(~하면 안 된다), may(~할지도 모른다)와 뜻을 구별한다."
S53 = "발문이 ‘B의 조언을’이라고 had better의 뜻을 알려 주었고 밑줄이 없었으며, 오답(‘예전에 좋아했다’, ‘금지되어 있다’)이 원문항 오답보다 뻔했다. 원문항 발문과 밑줄로 되돌리고, 원문항처럼 비슷한 조동사 뜻(할 수 있다, 해야만 한다, 하면 안 된다, 할지도 모른다)으로 오답을 새로 썼다."
M53 = {"수": "can(~할 수 있다)의 뜻이라 충고의 had better와 다르므로", "만": "must(~해야만 한다)의 뜻이라 ‘~하는 것이 좋겠다’는 충고와 다르므로", "면": "must not(~하면 안 된다)의 뜻이라 반대 의미이므로",
       "지": "may(~할지도 모른다)의 추측이라 충고와 다르므로", "좋": "had better(~하는 것이 좋겠다)의 충고를 바르게 옮겼으므로"}
def k53(x):
    if "좋겠다" in x: return "좋"
    if "안 된다" in x: return "면"
    if "해야만" in x or "야만" in x: return "만"
    if "지도 모른다" in x: return "지"
    return "수"
def f53(t, p, c, a, s=S53):
    mk(3, 53, t, [(x, M53[k53(x)]) for x in c], a, R53, s, st=ST53, p=p)
f53("B", "A: I left my phone at home.\nB: <u>You had better go back and get it</u>.", ["너는 돌아가서 그것을 가져올 수 있다.", "너는 돌아가서 그것을 가져오면 안 된다.", "너는 돌아가서 그것을 가져오는 것이 좋겠다.", "너는 돌아가서 그것을 가져올지도 모른다.", "너는 돌아가서 그것을 가져와야만 한다."], 3,
    "대화와 정답이 원문항과 거의 같았고 발문이 뜻을 알려 주었다. 대화를 새로 쓰고 " + S53[S53.index("원문항 발문과"):])
f53("C", "A: I have a headache.\nB: <u>You had better see a doctor</u>.", ["너는 의사의 진료를 받을지도 모른다.", "너는 의사의 진료를 받는 것이 좋겠다.", "너는 의사의 진료를 받을 수 있다.", "너는 의사의 진료를 받으면 안 된다.", "너는 의사의 진료를 받아야만 한다."], 2)
f53("D", "A: The road is icy.\nB: <u>You had better drive slowly</u>.", ["너는 천천히 운전하면 안 된다.", "너는 천천히 운전할지도 모른다.", "너는 천천히 운전할 수 있다.", "너는 천천히 운전해야만 한다.", "너는 천천히 운전하는 것이 좋겠다."], 5)
f53("E", "A: I have an exam tomorrow.\nB: <u>You had better study tonight</u>.", ["너는 오늘 밤 공부해야만 한다.", "너는 오늘 밤 공부할 수 있다.", "너는 오늘 밤 공부할지도 모른다.", "너는 오늘 밤 공부하는 것이 좋겠다.", "너는 오늘 밤 공부하면 안 된다."], 4)
f53("F", "A: It's raining.\nB: <u>You had better take an umbrella</u>.", ["너는 우산을 가져가는 것이 좋겠다.", "너는 우산을 가져갈 수 있다.", "너는 우산을 가져가야만 한다.", "너는 우산을 가져가면 안 된다.", "너는 우산을 가져갈지도 모른다."], 1)

# 3-54 might(가능성): 원문항 발문, B는 대화를 새로
S54 = "발문이 ‘확신이나 당위를 주장하지 않고 그럴 가능성도 있다는 뜻으로’라고 정답의 뜻을 알려 주어 원문항 발문으로 되돌렸다. 대화의 ‘I'm not sure’ 같은 단서로 조건 없이도 정답은 하나다."
mk(3, 54, "B", [("must", "must: ‘틀림없다’는 강한 확신이라 ‘잘 모르겠다’와 맞지 않으므로"), ("might", "might: ‘~일지도 모른다’는 가능성을 나타내 ‘잘 모르지만 그럴 수 있다’와 맞으므로"), ("can't", "can't: ‘~일 리 없다’는 강한 부정이라 ‘그럴 수 있다’와 맞지 않으므로"),
                ("should", "should: ‘~해야 한다’는 의무·충고라 추측과 맞지 않으므로"), ("won't", "won't: ‘~하지 않을 것이다’라 가능성의 뜻과 맞지 않으므로")], 2,
   "may/might는 확실하지 않은 가능성(~일지도 모른다)을, must는 강한 확신, can't는 강한 부정 추측을 나타낸다.",
   "대화가 원문항과 거의 같았고 발문이 정답의 뜻을 알려 주었다. 대화를 새로 쓰고 원문항 발문으로 되돌렸다.", st="R",
   p="A: Why isn't Tom answering his phone?\nB: He _____ be in the shower. I'm not sure, but it's possible.")
for t in "CDEF":
    ex = V(3, 54, t)["expl"]
    F(3, 54, t, st="R", xr=[x for x in [("확신이나 당위를 주장하지 않고 ", ""), ("발문의 조건", "대화의 단서"), ("여기서 요구한 ", "대화에 맞는 ")] if x[0] in ex], s=S54 + " 보기와 정답은 그대로다.")

# 3-55 조동사 표현 옳은 것의 개수: 원문항 형식(ⓐ~ⓔ, 밑줄, 1개~5개)
ST55 = "다음 중 밑줄 친 부분이 어법상 옳은 것의 개수를 고르시오."
R55 = "조동사(can, may, must, should, will) 뒤에는 동사원형을 쓰고 to를 붙이지 않는다. have to·be able to·would like to의 to 뒤에도 동사원형을 쓰며, had better 뒤에는 동사원형이 온다."
S55 = "원문항의 밑줄이 없고, 보기 기호 ⓐ~ⓔ가 a~e로 바뀌어 한 줄로 이어졌으며 선택지 순서가 뒤섞였다. 원문항 발문과 형식(ⓐ~ⓔ, 줄바꿈, 밑줄, 1개~5개)으로 되돌렸다."
def f55(t, lines, judge, ok, s=S55):
    n = len(ok.split(","))
    F(3, 55, t, st=ST55, p="\n".join(lines), c=CNT5, a=n, r=R55, pre=["문장별 판정: " + j for j in judge], k=f"밑줄 친 부분이 옳은 것은 {ok}로 {n}개이다.", n="cnt", s=s + ipos(n))
f55("B", ["ⓐ You <u>should wear</u> a helmet.", "ⓑ He <u>can plays</u> the guitar.", "ⓒ We <u>will be able to see</u> the stars tonight.", "ⓓ They <u>have to leaving</u> now.", "ⓔ I <u>would like order</u> a pizza."],
    ["ⓐ O. should + 동사원형이다.", "ⓑ X. can 뒤에는 동사원형(play)을 쓴다.", "ⓒ O. will be able to + 동사원형이다.", "ⓓ X. have to 뒤에는 동사원형(leave)을 쓴다.", "ⓔ X. would like 뒤에는 to부정사(to order)를 쓴다."],
    "ⓐ, ⓒ", "a·b가 원문항 문장과 같았고 정답 개수(3개)도 같았으며 기호·밑줄·선택지 순서도 원본과 달랐다. 문장을 새로 쓰고 원문항 형식으로 되돌렸으며 정답 개수를 2개로 바꿨다.")
f55("C", ["ⓐ She <u>should study</u>.", "ⓑ They <u>might come</u>.", "ⓒ We <u>must to leave</u>.", "ⓓ I <u>can help</u>.", "ⓔ Tom <u>has to work</u>."],
    ["ⓐ O. should + 동사원형이다.", "ⓑ O. might + 동사원형이다.", "ⓒ X. must 뒤에는 to 없이 동사원형을 쓴다.", "ⓓ O. can + 동사원형이다.", "ⓔ O. 3인칭 단수 주어에 has to를 썼다."], "ⓐ, ⓑ, ⓓ, ⓔ")
f55("D", ["ⓐ I <u>will have to go</u>.", "ⓑ Jane <u>can reads</u>.", "ⓒ They <u>may are</u> late.", "ⓓ You <u>had better rest</u>.", "ⓔ We <u>must studying</u>."],
    ["ⓐ O. will have to + 동사원형이다.", "ⓑ X. can 뒤에는 동사원형(read)을 쓴다.", "ⓒ X. may 뒤에는 동사원형(be)을 쓴다.", "ⓓ O. had better + 동사원형이다.", "ⓔ X. must 뒤에는 동사원형(study)을 쓴다."], "ⓐ, ⓓ",
    S55 + " 정답 개수가 원문항(3개)과 같지 않게 ⓒ·ⓔ를 틀린 문장으로 바꿔 2개로 했다.")
f55("E", ["ⓐ Tom <u>should goes</u>.", "ⓑ We <u>can play</u>.", "ⓒ Jane <u>might be</u> home.", "ⓓ They <u>have to leave</u>.", "ⓔ I <u>will be able to help</u>."],
    ["ⓐ X. should 뒤에는 동사원형(go)을 쓴다.", "ⓑ O. can + 동사원형이다.", "ⓒ O. might + 동사원형이다.", "ⓓ O. have to + 동사원형이다.", "ⓔ O. will be able to + 동사원형이다."], "ⓑ, ⓒ, ⓓ, ⓔ", S55)
f55("F", ["ⓐ She <u>must is</u> tired.", "ⓑ Tom <u>can't is</u> at home.", "ⓒ We <u>should study</u>.", "ⓓ I <u>may goes</u>.", "ⓔ They <u>can helps</u>."],
    ["ⓐ X. must 뒤에는 동사원형 be를 쓴다.", "ⓑ X. can't 뒤에는 동사원형 be를 쓴다.", "ⓒ O. should + 동사원형이다.", "ⓓ X. may 뒤에는 동사원형(go)을 쓴다.", "ⓔ X. can 뒤에는 동사원형(help)을 쓴다."], "ⓒ",
    S55 + " 다른 유형과 정답 개수가 겹치지 않게 틀린 문장을 늘려 옳은 것이 1개가 되게 했다.")

# 3-56 B: 원문항과 같던 제시문을 새로
mk(3, 56, "B", [("She doesn't call you tonight.", "미래 문장의 부정은 will not(won't)으로 만들므로"), ("She will not to call you tonight.", "will not 뒤에는 to 없이 동사원형을 쓰므로"), ("She won't call you tonight.", "won't + 동사원형으로 바르게 바꿨으므로"),
                ("She won't calls you tonight.", "won't 뒤에는 동사원형(call)을 쓰므로"), ("She isn't call you tonight.", "일반동사 앞에 isn't를 쓸 수 없으므로")], 3,
   "will의 부정은 will not(won't) + 동사원형이다.", "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘She will call you tonight.’로 바꿨다.", p="She will call you tonight.")

# 3-57 부적합: 원문항처럼 상태동사 진행형 넷 + 동작동사 진행형 하나
ST57 = "다음 중 밑줄 친 부분의 쓰임이 어법상 옳은 것은?"
R57 = "know, want, need, believe, own, belong, prefer, hate, have(가지고 있다) 같은 상태동사는 보통 진행형으로 쓰지 않는다. 동작동사는 be동사 + -ing로 진행형을 만든다."
S57 = "원문항은 진행형으로 쓸 수 없는 상태동사를 묻는데, 변형은 발문이 ‘진행형 또는 조동사 뒤의 동사 형태’로 바뀌어 동사 형태 오류를 물었고(평가 문법이 다름), 오답이 유형마다 같았다. 원문항 발문과 형식(상태동사 진행형 넷 + 동작동사 진행형 하나)으로 다시 썼다."
def ST(v): return f"상태동사({v})는 진행형으로 쓰지 않으므로"
ACT57 = "동작동사를 be동사 + -ing의 진행형으로 바르게 썼으므로"
mk(3, 57, "B", [("She <u>is owning</u> a big dog.", ST("own")), ("We <u>are wanting</u> more time.", ST("want")), ("Tom <u>is playing</u> the piano now.", ACT57), ("I <u>am believing</u> your story.", ST("believe")), ("They <u>are knowing</u> the answer.", ST("know"))], 3, R57, S57, st=ST57)
mk(3, 57, "C", [("He <u>is preferring</u> tea.", ST("prefer")), ("She <u>is watching</u> a movie.", ACT57), ("I <u>am needing</u> help.", ST("need")), ("This bag <u>is belonging</u> to me.", ST("belong")), ("We <u>are understanding</u> the rule.", ST("understand"))], 2, R57, S57, st=ST57)
mk(3, 57, "D", [("The box <u>is containing</u> old books.", ST("contain")), ("I <u>am seeming</u> tired.", ST("seem")), ("Mina <u>is resembling</u> her mom.", ST("resemble")), ("We <u>are recognizing</u> his voice.", ST("recognize")), ("Dad <u>is washing</u> the car.", ACT57)], 5, R57, S57, st=ST57)
mk(3, 57, "E", [("Jane <u>is running</u> in the park.", ACT57), ("I <u>am knowing</u> his secret.", ST("know")), ("He <u>is wanting</u> a new bike.", ST("want")), ("We <u>are believing</u> in you.", ST("believe")), ("This pen <u>is belonging</u> to Tom.", ST("belong"))], 1, R57, S57, st=ST57)
mk(3, 57, "F", [("I <u>am needing</u> a rest.", ST("need")), ("She <u>is having</u> long hair.", "‘가지고 있다’는 뜻의 상태동사(have)는 진행형으로 쓰지 않으므로"), ("The soup <u>is tasting</u> salty.", "‘~한 맛이 나다’는 뜻의 상태동사(taste)는 진행형으로 쓰지 않으므로"),
                ("They <u>are singing</u> a song.", ACT57), ("He <u>is hating</u> spiders.", ST("hate"))], 4, R57, S57, st=ST57)

# 3-58 현재분사(진행형) vs 동명사: 유형마다 <보기>와 오답을 새로
ST58 = "다음 중 밑줄 친 부분의 쓰임이 보기와 같은 것은?"
R58 = "be동사와 함께 진행형을 만드는 -ing는 현재분사이고, 주어·보어·동사나 전치사의 목적어로 쓰이는 -ing는 동명사이다."
S58 = "<보기> 문장이 원문항과 똑같았고, 동명사 오답 네 문장이 유형마다 같았다(B는 정답 문장도 원문항과 같았다). 유형마다 <보기> 문장과 오답을 새로 썼다."
PROG = "현재분사: be동사와 함께 진행형을 만들어 〈보기〉와 쓰임이 같으므로"
def GER(role): return f"동명사: {role}로 쓰여 〈보기〉와 쓰임이 다르므로"
def f58(t, bogi, items, a):
    mk(3, 58, t, items, a, R58, S58, st=ST58, p=f"<보기>\n{bogi}")
f58("B", "My sister is <u>singing</u> in her room.", [("<u>Singing</u> makes me happy.", GER("문장의 주어")), ("The baby was <u>crying</u> all night.", PROG), ("I'm good at <u>drawing</u>.", GER("전치사 at의 목적어")),
                                                  ("Stop <u>talking</u>, please.", GER("stop의 목적어")), ("We talked about <u>moving</u> to Busan.", GER("전치사 about의 목적어"))], 2)
f58("C", "Jane is <u>writing</u> an email now.", [("He finished <u>cleaning</u> his room.", GER("finish의 목적어")), ("<u>Walking</u> is good exercise.", GER("문장의 주어")), ("They were <u>playing</u> soccer at five.", PROG),
                                             ("I'm interested in <u>cooking</u>.", GER("전치사 in의 목적어")), ("She avoided <u>eating</u> sweets.", GER("avoid의 목적어"))], 3)
f58("D", "The dogs were <u>barking</u> loudly.", [("We enjoyed <u>dancing</u> at the party.", GER("enjoy의 목적어")), ("<u>Reading</u> books is fun.", GER("문장의 주어")), ("He is afraid of <u>flying</u>.", GER("전치사 of의 목적어")),
                                            ("Jane was <u>reading</u> when I called.", PROG), ("I gave up <u>eating</u> fast food.", GER("give up의 목적어"))], 4)
f58("E", "Mom is <u>making</u> lunch in the kitchen.", [("I love <u>swimming</u> in the sea.", GER("love의 목적어")), ("How about <u>going</u> out?", GER("전치사 about의 목적어")), ("<u>Keeping</u> a diary is helpful.", GER("문장의 주어")),
                                                   ("She kept <u>smiling</u>.", GER("keep의 목적어")), ("Tom was <u>sleeping</u> at ten.", PROG)], 5)
f58("F", "The children are <u>laughing</u> together.", [("We were <u>studying</u> all evening.", PROG), ("Would you mind <u>opening</u> the door?", GER("mind의 목적어")), ("<u>Learning</u> English is fun.", GER("문장의 주어")),
                                                   ("He left without <u>saying</u> goodbye.", GER("전치사 without의 목적어")), ("My job is <u>selling</u> cars.", GER("be동사 뒤 보어"))], 1)

# 3-59 진행형 문장 짝: 원문항 형식(㉠~㉣, 두 기호 조합), 옳은 문장이 둘이 되게
ST59 = "다음 중 어법상 옳은 문장으로만 짝지어진 것은?"
R59 = "진행형은 be동사 + 동사-ing로 만들며 be동사는 주어에 맞춘다. 단모음 + 단자음으로 끝나는 동사는 자음을 한 번 더 쓰고(swim → swimming, nap → napping, sit → sitting), -e로 끝나면 e를 뺀다(have → having, write → writing)."
S59 = "보기 기호 ㉠~㉣이 ㄱ~ㄹ로 바뀌어 한 줄로 이어졌고, 원문항에 없던 ‘해당 없음’ 선택지가 생겼으며 발문도 달랐다. 원문항 발문과 형식(㉠~㉣ 줄바꿈, 두 기호 조합)으로 되돌리고, 옳은 문장이 둘이 되게 조정했다."
CH59 = ["㉠, ㉡", "㉠, ㉢", "㉡, ㉢", "㉡, ㉣", "㉢, ㉣"]
def f59(t, lines, judge, ok, a, s=S59):
    F(3, 59, t, st=ST59, p="\n".join(lines), c=CH59, a=a, r=R59, pre=["문장별 판정: " + j for j in judge], k=f"옳은 문장은 {ok}이다.", n=setnotes(CH59, ok, "옳은 문장"), s=s + ipos(a))
f59("B", ["㉠ Mina is swiming in the pool.", "㉡ The students are writing essays.", "㉢ Is your dad washing the dishes?", "㉣ I am haveing breakfast."],
    ["㉠ X. swim은 m을 한 번 더 써 swimming이다.", "㉡ O. are + writing이다.", "㉢ O. 진행형 의문문(Is + 주어 + -ing)이다.", "㉣ X. have는 e를 빼고 having이다."], "㉡, ㉢", 3,
    "네 문장이 원문항을 줄인 것이었고 정답 조합도 같았으며 기호·선택지 형식도 원본과 달랐다. 문장을 새로 쓰고 원문항 발문과 형식으로 되돌렸다.")
f59("C", ["㉠ Jane is reading.", "㉡ Tom are sleeping.", "㉢ We are studying.", "㉣ The boys is playing."],
    ["㉠ O. is + reading이다.", "㉡ X. 단수 주어(Tom)에는 is를 쓴다.", "㉢ O. are + studying이다.", "㉣ X. 복수 주어(The boys)에는 are를 쓴다."], "㉠, ㉢", 2)
f59("D", ["㉠ I is cooking.", "㉡ She is know the answer.", "㉢ They are running.", "㉣ We are cleaning."],
    ["㉠ X. 주어 I에는 am을 쓴다.", "㉡ X. is 뒤에 원형을 쓸 수 없고, know는 진행형으로도 쓰지 않는다.", "㉢ O. are + running이다.", "㉣ O. are + cleaning이다."], "㉢, ㉣", 5)
f59("E", ["㉠ Tom is watching TV.", "㉡ They are sitting.", "㉢ Jane is writting.", "㉣ I am study."],
    ["㉠ O. is + watching이다.", "㉡ O. sit은 t를 한 번 더 써 sitting이다.", "㉢ X. write는 e를 빼고 writing이다(t는 한 번만 쓴다).", "㉣ X. am 뒤에는 studying을 쓴다."], "㉠, ㉡", 1)
f59("F", ["㉠ We are leaving.", "㉡ She is want a bag.", "㉢ The dog is barking.", "㉣ Tom are working."],
    ["㉠ O. are + leaving이다.", "㉡ X. want는 상태 동사라 진행형으로 쓰지 않고, is 뒤에 동사원형도 올 수 없다(She wants a bag).", "㉢ O. is + barking이다.", "㉣ X. 단수 주어(Tom)에는 is를 쓴다."], "㉠, ㉢", 2)

# 3-60 did / 조동사 뒤 동사원형 옳은 문장 개수: 원문항 형식(ⓐ~ⓔ, 1개~5개)
ST60 = "다음 중 어법상 옳은 문장의 개수는?"
R60 = "did/didn't와 조동사(can, may, must, should, might) 뒤에는 동사원형을 쓰며, to나 -ing·과거형·-s를 붙이지 않는다."
S60 = "보기 기호 ⓐ~ⓔ가 a~e로 바뀌어 한 줄로 이어졌고 선택지 순서가 뒤섞였다. 원문항 발문과 형식(ⓐ~ⓔ 줄바꿈, 1개~5개)으로 되돌렸다."
def f60(t, lines, judge, ok, s=S60):
    n = len(ok.split(","))
    F(3, 60, t, st=ST60, p="\n".join(lines), c=CNT5, a=n, r=R60, pre=["문장별 판정: " + j for j in judge], k=f"어법상 옳은 문장은 {ok}로 {n}개이다.", n="cnt", s=s + ipos(n))
f60("B", ["ⓐ We didn't watch the game.", "ⓑ Did your brother pass the test?", "ⓒ She didn't finished her homework.", "ⓓ Did you called me last night?", "ⓔ I didn't feel well yesterday."],
    ["ⓐ O. didn't + 동사원형이다.", "ⓑ O. Did + 주어 + 동사원형이다.", "ⓒ X. didn't 뒤에는 동사원형(finish)을 쓴다.", "ⓓ X. Did 뒤에는 동사원형(call)을 쓴다.", "ⓔ O. didn't + 동사원형이다."], "ⓐ, ⓑ, ⓔ",
    "a~d가 원문항 문장과 같았고 정답 개수(2개)도 같았으며 기호·선택지 순서도 원본과 달랐다. 문장을 새로 쓰고 원문항 형식으로 되돌렸으며 정답 개수를 3개로 바꿨다.")
f60("C", ["ⓐ Jane didn't go home.", "ⓑ Did Tom saw the movie?", "ⓒ We can help.", "ⓓ She must to study.", "ⓔ They might come."],
    ["ⓐ O. didn't + 동사원형이다.", "ⓑ X. Did 뒤에는 동사원형(see)을 쓴다.", "ⓒ O. can + 동사원형이다.", "ⓓ X. must 뒤에는 to 없이 동사원형을 쓴다.", "ⓔ O. might + 동사원형이다."], "ⓐ, ⓒ, ⓔ", S60)
f60("D", ["ⓐ I didn't eat lunch.", "ⓑ Did they go?", "ⓒ Tom can reads.", "ⓓ Jane should rest.", "ⓔ We must study."],
    ["ⓐ O. didn't + 동사원형이다.", "ⓑ O. Did + 주어 + 동사원형이다.", "ⓒ X. can 뒤에는 동사원형(read)을 쓴다.", "ⓓ O. should + 동사원형이다.", "ⓔ O. must + 동사원형이다."], "ⓐ, ⓑ, ⓓ, ⓔ")
f60("E", ["ⓐ They didn't see me.", "ⓑ Did Jane wrote a letter?", "ⓒ Tom might is at home.", "ⓓ We can plays.", "ⓔ I had better to go."],
    ["ⓐ O. didn't + 동사원형이다.", "ⓑ X. Did 뒤에는 동사원형(write)을 쓴다.", "ⓒ X. might 뒤에는 동사원형 be를 쓴다.", "ⓓ X. can 뒤에는 동사원형(play)을 쓴다.", "ⓔ X. had better 뒤에는 to 없이 동사원형을 쓴다."], "ⓐ",
    S60 + " 다른 유형과 정답 개수가 겹치지 않게 틀린 문장을 늘려 옳은 문장이 1개가 되게 했다.")
f60("F", ["ⓐ He didn't bought it.", "ⓑ Did they come?", "ⓒ We should leave.", "ⓓ Jane may be late.", "ⓔ Tom can help."],
    ["ⓐ X. didn't 뒤에는 동사원형(buy)을 쓴다.", "ⓑ O. Did + 주어 + 동사원형이다.", "ⓒ O. should + 동사원형이다.", "ⓓ O. may + 동사원형이다.", "ⓔ O. can + 동사원형이다."], "ⓑ, ⓒ, ⓓ, ⓔ",
    "틀린 문장이 없어 원문항(틀린 것 판별)과 달랐다. ⓐ를 틀린 문장으로 바꿔 오류를 판별하게 하고(정답 개수는 원문항의 2개와 겹치지 않게 4개), 원문항 형식(ⓐ~ⓔ, 1개~5개)으로 되돌렸다.")
