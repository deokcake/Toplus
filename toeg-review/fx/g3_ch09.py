# 3급 CH9 동명사 (81~90) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]

# 3-81 -ing형 철자: 유형마다 동사 짝을 새로, 같은 동사 반복 없앰
R81 = "동사-ing형은 보통 -ing을 붙인다. -e로 끝나면 e를 빼고(make → making), -ie로 끝나면 ie를 y로 바꾸며(lie → lying), 단모음 + 단자음으로 끝나면 자음을 한 번 더 쓴다(run → running)."
S81 = "오답 짝(lie - lying, write - writing, run - running, read - reading)이 유형마다 반복되었고, 일부 유형은 같은 동사가 두 번 나와 단서가 되었다. 유형마다 동사 짝을 새로 쓰고 같은 동사가 두 번 나오지 않게 했다."
def why81(v, g):
    if v.endswith("ie") and g == v[:-2] + "ying": return "ie를 y로 바꾸고 -ing을 붙인 옳은 형태이므로"
    if v.endswith("e") and not v.endswith("ee") and g == v[:-1] + "ing": return "끝의 e를 빼고 -ing을 붙인 옳은 형태이므로"
    if g == v + v[-1] + "ing": return "단모음 + 단자음으로 끝나 자음을 한 번 더 쓰고 -ing을 붙인 옳은 형태이므로"
    return "-ing을 그대로 붙인 옳은 형태이므로"
def f81(t, pairs, a, bad, s=S81):
    mk(3, 81, t, [(f"{v} - {g}", bad if i + 1 == a else why81(v, g)) for i, (v, g) in enumerate(pairs)], a, R81, s)
f81("B", [("cut", "cutting"), ("come", "comeing"), ("die", "dying"), ("stop", "stopping"), ("study", "studying")], 2, "-e로 끝나는 come은 e를 빼고 coming으로 써야 하므로",
    "정답(write - writeing)이 원문항과 같았고 write가 두 번 나와 단서가 되었다. 동사 짝을 새로 쓰고 정답을 come - comeing으로 바꿨다.")
f81("C", [("jump", "jumping"), ("begin", "beginning"), ("make", "makeing"), ("tie", "tying"), ("put", "putting")], 3, "-e로 끝나는 make는 e를 빼고 making으로 써야 하므로")
f81("D", [("dance", "dancing"), ("get", "getting"), ("fly", "flying"), ("lie", "lying"), ("run", "runing")], 5, "단모음 + 단자음으로 끝나는 run은 n을 한 번 더 써 running으로 써야 하므로")
f81("E", [("shop", "shopping"), ("ride", "riding"), ("lie", "lieing"), ("plan", "planning"), ("see", "seeing")], 3, "-ie로 끝나는 lie는 ie를 y로 바꿔 lying으로 써야 하므로")
f81("F", [("have", "having"), ("drive", "driving"), ("win", "winning"), ("cry", "crying"), ("swim", "swiming")], 5, "단모음 + 단자음으로 끝나는 swim은 m을 한 번 더 써 swimming으로 써야 하므로")

# 3-82 동명사가 아닌 것: 유형마다 문장을 새로
R82 = "enjoy, finish, avoid, mind, keep, give up, practice, quit, consider, suggest, dislike는 동명사를 목적어로 쓰고, want, hope, plan, decide, promise, need는 to부정사를 목적어로 쓴다."
S82 = "동명사 오답 네 문장이 유형마다 같았다. 유형마다 문장을 새로 썼다."
def G(v, ing): return f"{v}: 동명사를 목적어로 쓰는 동사라 동명사({ing})가 들어가므로"
def T(v, base): return f"{v}: to부정사를 목적어로 쓰는 동사라 to부정사(to {base})가 들어가므로"
def f82(t, items, a, s=S82):
    mk(3, 82, t, items, a, R82, s)
f82("B", [("Mina gave up (eat)_____ fast food.", G("give up", "eating")), ("He promised (help)_____ me.", T("promise", "help")), ("Do you mind (close)_____ the door?", G("mind", "closing")),
          ("She kept (smile)_____ at me.", G("keep", "smiling")), ("I practice (speak)_____ English every day.", G("practice", "speaking"))], 2,
    "정답 문장(They decided (go) to the beach.)이 원문항과 똑같았다. 문장을 새로 쓰고 정답 동사를 promise로 바꿨다.")
f82("C", [("We enjoyed (dance)_____ at the party.", G("enjoy", "dancing")), ("He quit (drink)_____ soda.", G("quit", "drinking")), ("She plans (visit)_____ Busan.", T("plan", "visit")),
          ("They considered (buy)_____ a new car.", G("consider", "buying")), ("I finished (write)_____ the letter.", G("finish", "writing"))], 3)
f82("D", [("Tom hopes (meet)_____ Jane.", T("hope", "meet")), ("Mom suggested (take)_____ a taxi.", G("suggest", "taking")), ("We avoided (walk)_____ in the rain.", G("avoid", "walking")),
          ("He dislikes (wait)_____ in line.", G("dislike", "waiting")), ("I enjoy (listen)_____ to music.", G("enjoy", "listening"))], 1)
f82("E", [("He enjoys (fish)_____ on weekends.", G("enjoy", "fishing")), ("It kept (rain)_____ all day.", G("keep", "raining")), ("Don't give up (try)_____.", G("give up", "trying")),
          ("She avoids (drink)_____ coffee at night.", G("avoid", "drinking")), ("We want (buy)_____ a car.", T("want", "buy"))], 5)
f82("F", [("Did you consider (join)_____ the team?", G("consider", "joining")), ("She practices (sing)_____ every morning.", G("practice", "singing")), ("I need (finish)_____ this work.", T("need", "finish")),
          ("He finished (wash)_____ the dishes.", G("finish", "washing")), ("I don't mind (wait)_____ for you.", G("mind", "waiting"))], 3)

# 3-83 동명사 vs 현재분사: 유형마다 문장을 새로
R83 = "동명사와 현재분사는 모두 -ing형이다. 동명사는 명사 역할(주어, 목적어, 보어, 전치사의 목적어)을 하고, 현재분사는 be동사와 진행형을 만들거나 명사를 꾸미는 형용사 역할을 한다."
S83 = "동명사 오답 네 문장이 유형마다 같았다. 유형마다 문장을 새로 썼다."
def GER(role): return f"동명사: {role}로 쓰였으므로"
def PAR(role): return f"현재분사: {role}"
def f83(t, items, a, s=S83):
    mk(3, 83, t, [(x, w + (" 나머지와 쓰임이 달라" if i + 1 == a else "")) for i, (x, w) in enumerate(items)], a, R83, s)
f83("B", [("<u>Collecting</u> stamps is my hobby.", GER("문장의 주어")), ("He is good at <u>drawing</u>.", GER("전치사 at의 목적어")), ("I don't like <u>waiting</u> in line.", GER("like의 목적어")),
          ("The baby is <u>sleeping</u> now.", PAR("be동사와 함께 진행형을 만들어")), ("Thank you for <u>helping</u> me.", GER("전치사 for의 목적어"))], 4,
    "정답 문장(They are discussing the problem.)이 원문항과 똑같았다. 문장을 새로 썼다.")
f83("C", [("I stopped <u>eating</u> sweets.", GER("stop의 목적어")), ("Look at the <u>running</u> dog.", PAR("명사 dog를 꾸미는 형용사 역할을 해")), ("<u>Keeping</u> a pet is not easy.", GER("문장의 주어")),
          ("She is afraid of <u>flying</u>.", GER("전치사 of의 목적어")), ("His hobby is <u>fishing</u>.", GER("주어를 설명하는 보어"))], 2, S83 + " 정답도 진행형 대신 명사를 꾸미는 현재분사로 바꿔 다른 유형과 달리했다.")
f83("D", [("<u>Watching</u> movies is fun.", GER("문장의 주어")), ("We talked about <u>camping</u>.", GER("전치사 about의 목적어")), ("I love <u>baking</u> bread.", GER("love의 목적어")),
          ("Would you mind <u>opening</u> the door?", GER("mind의 목적어")), ("Tom was <u>playing</u> the guitar.", PAR("be동사와 함께 과거진행형을 만들어"))], 5)
f83("E", [("<u>Riding</u> a bike is fun.", "동명사: 문장의 주어로 쓰여"), ("The girl <u>singing</u> on the stage is my sister.", PAR("명사 girl을 뒤에서 꾸미므로")), ("They were <u>waiting</u> for the bus.", PAR("be동사와 함께 진행형을 만들므로")),
          ("Who is the man <u>standing</u> at the door?", PAR("명사 man을 뒤에서 꾸미므로")), ("The children are <u>laughing</u>.", PAR("be동사와 함께 진행형을 만들므로"))], 1,
    S83 + " 현재분사 넷 + 동명사 하나로 짜서 다른 유형과 구성을 달리했다.")
f83("F", [("He left without <u>saying</u> goodbye.", GER("전치사 without의 목적어")), ("<u>Getting</u> up early is hard.", GER("문장의 주어")), ("Jane is <u>writing</u> a letter.", PAR("be동사와 함께 진행형을 만들어")),
          ("They enjoyed <u>singing</u> together.", GER("enjoy의 목적어")), ("I'm interested in <u>learning</u> Chinese.", GER("전치사 in의 목적어"))], 3)

# 3-84 동명사 관용 표현 틀린 문장: 유형마다 새로, 짝 문장 없앰
R84 = "전치사(about, in, of, at, for, without) 뒤와 관용 표현(look forward to, feel like, be busy, can't help, How about, be used to, It's no use, have a hard time, spend + 시간) 뒤에는 동명사를 쓴다."
S84 = "오답 네 문장이 B와 똑같았고, 틀린 문장이 같은 내용의 옳은 문장과 짝을 이뤄 단서가 되었다. 유형마다 문장을 새로 쓰고 짝 문장을 없앴다."
OK84 = "동명사를 바르게 썼으므로"
def f84(t, items, a, s=S84):
    mk(3, 84, t, [(x, w or OK84) for x, w in items], a, R84, s)
f84("B", [("I can't help smiling at the baby.", "can't help + 동명사(~하지 않을 수 없다)를 바르게 썼으므로"), ("She is busy doing her homework.", "be busy + 동명사(~하느라 바쁘다)를 바르게 썼으므로"), ("He is used to getting up early.", "be used to + 동명사(~에 익숙하다)를 바르게 썼으므로"),
          ("How about go to the movies?", "How about 뒤에는 동명사(going)를 써야 하므로"), ("It's no use crying over it.", "It's no use + 동명사(~해도 소용없다)를 바르게 썼으므로")], 4,
    "틀린 문장(We're looking forward to meet you soon.)이 원문항과 똑같았고 옳은 짝 문장(to meeting)이 함께 있어 단서가 되었다. 문장을 새로 쓰고 짝 문장을 없앴다.")
f84("C", [("Thank you for inviting me.", "전치사 for 뒤에 동명사를 바르게 썼으므로"), ("She is interested in learn English.", "전치사 in 뒤에는 동명사(learning)를 써야 하므로"), ("I feel like eating pizza.", "feel like + 동명사(~하고 싶다)를 바르게 썼으므로"),
          ("He spent the day reading books.", "spend + 시간 + 동명사를 바르게 썼으므로"), ("They went fishing yesterday.", "go + 동명사(~하러 가다)를 바르게 썼으므로")], 2)
f84("D", [("My brother is good at cooking.", "전치사 at 뒤에 동명사를 바르게 썼으므로"), ("I'm sorry for being late.", "전치사 for 뒤에 동명사를 바르게 썼으므로"), ("She kept talking on the phone.", "keep + 동명사를 바르게 썼으므로"),
          ("Do you mind helping me?", "mind + 동명사를 바르게 썼으므로"), ("Tom is worried about fail the test.", "전치사 about 뒤에는 동명사(failing)를 써야 하므로")], 5)
f84("E", [("She left without saying a word.", "전치사 without 뒤에 동명사를 바르게 썼으므로"), ("He is proud of being a doctor.", "전치사 of 뒤에 동명사를 바르게 썼으므로"), ("I feel like to drink something cold.", "feel like 뒤에는 동명사(drinking)를 써야 하므로"),
          ("We had a hard time finding the house.", "have a hard time + 동명사(~하느라 고생하다)를 바르게 썼으므로"), ("Keep going straight.", "keep + 동명사를 바르게 썼으므로")], 3)
f84("F", [("They talked about move to Seoul.", "전치사 about 뒤에는 동명사(moving)를 써야 하므로"), ("Would you mind turning off the TV?", "mind + 동명사를 바르게 썼으므로"), ("I'm tired of waiting.", "전치사 of 뒤에 동명사를 바르게 썼으므로"),
          ("She is excited about going on a trip.", "전치사 about 뒤에 동명사를 바르게 썼으므로"), ("Instead of taking a bus, we walked.", "전치사 instead of 뒤에 동명사를 바르게 썼으므로")], 1)

# 3-85 어색한 것끼리 짝: 원문항 형식(ⓐ~ⓓ 네 문장, 밑줄, 틀린 두 개 조합)
ST85 = "다음 중 밑줄 친 부분의 쓰임이 어법상 어색한 것끼리 짝지어진 것은?"
R85 = "want, hope, plan, decide는 to부정사를, enjoy, finish, avoid, keep, consider, give up, suggest, mind는 동명사를 목적어로 쓴다."
S85 = "원문항은 네 문장 중 틀린 두 개의 조합을 고르는데, 변형은 다섯 문장 중 틀린 하나의 기호를 고르는 형식으로 바뀌었고 기호도 a~e로 바뀌어 한 줄로 이어졌다. 원문항 발문과 형식(ⓐ~ⓓ 네 문장, 밑줄, 틀린 두 개의 조합)으로 되돌렸다."
CH85 = ["ⓐ, ⓑ", "ⓐ, ⓒ", "ⓑ, ⓒ", "ⓑ, ⓓ", "ⓒ, ⓓ"]
def f85(t, lines, judge, ok, c=CH85, s=S85):
    a = c.index(ok) + 1
    F(3, 85, t, st=ST85, p="\n".join(lines), c=c, a=a, r=R85, pre=["문장별 판정: " + j for j in judge], k=f"어법상 어색한 것은 {ok}이다.", n=setnotes(c, ok, "어색한 것"), s=s + ipos(a))
f85("B", ["ⓐ Tom <u>enjoys to play</u> tennis.", "ⓑ She <u>hopes to become</u> a nurse.", "ⓒ We <u>finished to paint</u> the wall.", "ⓓ I <u>want to visit</u> Paris."],
    ["ⓐ X. enjoy는 동명사(playing)를 목적어로 쓴다.", "ⓑ O. hope + to부정사이다.", "ⓒ X. finish는 동명사(painting)를 목적어로 쓴다.", "ⓓ O. want + to부정사이다."], "ⓐ, ⓒ",
    s="ⓐ~ⓒ가 원문항 문장과 같았고 정답 조합(ⓑ, ⓓ)도 같았으며, 보기 수(4 → 5)·기호·발문도 원본과 달랐다. 문장을 새로 쓰고 원문항 발문과 형식(ⓐ~ⓓ 네 문장, 밑줄, 틀린 두 개의 조합)으로 되돌렸다.")
f85("C", ["ⓐ Jane <u>likes reading</u> novels.", "ⓑ We <u>hope to win</u> the game.", "ⓒ Tom <u>keeps to talk</u> in class.", "ⓓ I <u>considered to move</u> to a new city."],
    ["ⓐ O. like는 동명사를 목적어로 쓸 수 있다.", "ⓑ O. hope + to부정사이다.", "ⓒ X. keep은 동명사(talking)를 목적어로 쓴다.", "ⓓ X. consider는 동명사(moving)를 목적어로 쓴다."], "ⓒ, ⓓ")
f85("D", ["ⓐ Tom <u>finished to work</u> at six.", "ⓑ Jane <u>plans traveling</u> to Japan.", "ⓒ They <u>decided to leave</u> early.", "ⓓ I <u>enjoy swimming</u> in the sea."],
    ["ⓐ X. finish는 동명사(working)를 목적어로 쓴다.", "ⓑ X. plan은 to부정사(to travel)를 목적어로 쓴다.", "ⓒ O. decide + to부정사이다.", "ⓓ O. enjoy + 동명사이다."], "ⓐ, ⓑ")
f85("E", ["ⓐ He <u>suggested going</u> home.", "ⓑ She <u>wants learning</u> English.", "ⓒ They <u>avoid to drive</u> at night.", "ⓓ We <u>decided to stay</u> home."],
    ["ⓐ O. suggest + 동명사이다.", "ⓑ X. want는 to부정사(to learn)를 목적어로 쓴다.", "ⓒ X. avoid는 동명사(driving)를 목적어로 쓴다.", "ⓓ O. decide + to부정사이다."], "ⓑ, ⓒ")
f85("F", ["ⓐ Jane <u>plans visiting</u> Busan.", "ⓑ Tom <u>likes playing</u> soccer.", "ⓒ We <u>finished eating</u> lunch.", "ⓓ I <u>gave up to learn</u> the violin."],
    ["ⓐ X. plan은 to부정사(to visit)를 목적어로 쓴다.", "ⓑ O. like는 동명사를 목적어로 쓸 수 있다.", "ⓒ O. finish + 동명사이다.", "ⓓ X. give up은 동명사(learning)를 목적어로 쓴다."], "ⓐ, ⓓ",
    c=["ⓐ, ⓑ", "ⓐ, ⓒ", "ⓐ, ⓓ", "ⓑ, ⓒ", "ⓒ, ⓓ"], s=S85 + " 다른 유형과 정답 조합이 겹치지 않게 ⓐ, ⓓ 조합을 정답으로 넣었다.")

# 3-86 B: 원문항과 같던 대화를 새로
mk(3, 86, "B", [("help", "전치사 for 뒤에 동사원형을 쓸 수 없으므로"), ("is helping", "전치사 뒤에 be동사 + -ing를 쓸 수 없으므로"), ("helping", "전치사 for 뒤에는 동명사를 쓰므로"), ("helpings", "동명사에 -s를 붙이지 않으므로"), ("to help", "전치사 for 뒤에 to부정사를 쓸 수 없으므로")], 3,
   "전치사 뒤에는 동명사(-ing)를 쓴다.", "대화와 정답이 원문항과 똑같았다. 대화를 ‘Thank you for ___(help) me.’로 바꿨다.", p="Tom: Thank you for ______(help) me.\nJane: You're welcome.", okdup=True)

# 3-87 E 발문, F 새 문장
ST87 = "다음 문장에서 어법상 틀린 부분을 찾아 바르게 고친 문장을 고르시오."
F(3, 87, "E", st=ST87, s="발문이 ‘그들은 수업 중에 계속 이야기한다’는 뜻과 사용할 동사(keep)를 알려 주어 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
mk(3, 87, "F", [("Would you mind turn off the light?", "mind 뒤에 동사원형을 쓸 수 없으므로"), ("Would you mind turning off the light?", "mind + 동명사로 바르게 고쳤으므로"), ("Would you mind to turning off the light?", "to를 그대로 두었으므로"),
                ("Would you minding turning off the light?", "would 뒤에는 동사원형 mind를 쓰므로"), ("Would you mind to turn off the light?", "틀린 부분(to turn)을 그대로 두었으므로")], 2,
   "enjoy, finish, avoid, mind, consider 등은 목적어로 동명사(-ing)를 쓴다.", "제시문(I enjoy to read novels.)이 B(I enjoy to read books.)와 사실상 같았다. 동사를 mind로 바꿔 제시문을 새로 썼다.", p="Would you mind to turn off the light?")

# 3-88 B: 원문항과 같던 제시문을 새로
mk(3, 88, "B", [("Are you enjoy writing a diary in English?", "일반동사 enjoy의 의문문은 Are가 아니라 Do로 만들므로"), ("Do enjoy you writing a diary in English?", "Do + 주어 + 동사 순서가 아니므로"), ("Do you enjoy writing a diary in English?", "Do + 주어 + enjoy + 동명사로 바르게 배열했으므로"),
                ("Do you enjoy to write a diary in English?", "enjoy는 to부정사가 아니라 동명사를 목적어로 쓰므로"), ("Do you enjoy write a diary in English?", "write를 동명사(writing)로 바꿔야 하므로")], 3,
   "enjoy, mind 등은 동명사를 목적어로 쓴다. 일반동사 의문문은 Do + 주어 + 동사원형 순서이다.", "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘너는 영어로 일기 쓰는 것을 즐기니?’로 바꿨다.",
   p="너는 영어로 일기 쓰는 것을 즐기니?\n(you / enjoy / write / a diary / in English / do / ?)")

# 3-89 ⓐ 설명: 원문항 발문과 지문 속 밑줄, 그럴듯한 오개념 오답
ST89 = "다음 지문을 읽고 밑줄 친 ⓐ에 대한 설명으로 가장 적절한 것을 고르시오."
R89 = "keep, practice, give up, avoid, finish, enjoy 등은 동명사를 목적어로 쓴다. 이때 -ing는 진행형이나 명사를 꾸미는 현재분사가 아니라 동사의 목적어(명사 역할)이다."
S89 = "발문이 원문항과 달랐고 밑줄이 사라졌으며, 오답 네 개(‘과거시제라서’, ‘3인칭 단수라서’ 등)가 유형마다 같고 뻔했다. 원문항 발문과 지문 속 ⓐ 밑줄로 되돌리고, 원문항처럼 그럴듯한 오개념(진행형·현재분사로 오해, to부정사로 바꿔 씀, 뜻 오해)으로 오답을 새로 썼다."
PROG = "-ing가 진행형의 일부가 아니라 동사의 목적어(동명사)이므로"
PART = "-ing가 명사를 꾸미는 현재분사가 아니라 동사의 목적어(동명사)이므로"
TOINF = "이 동사는 to부정사를 목적어로 쓰지 않아 틀린 문장이 되므로"
def f89(t, story, items, a, s=S89):
    mk(3, 89, t, items, a, R89, s, st=ST89, p=story)
f89("B", "My sister loves music. She ⓐ<u>practices playing</u> the violin every evening. Someday she wants to be a violinist.",
    [("ⓐ의 'playing'은 진행형의 일부로, 지금 바이올린을 연주하는 중이라는 뜻이다.", PROG), ("ⓐ의 'practice'는 동명사를 목적어로 취하는 동사이므로 뒤에 'playing'이 왔다.", "practice는 동명사를 목적어로 쓰므로"),
     ("ⓐ의 'playing'은 뒤의 'the violin'을 꾸며 주는 현재분사(형용사 역할)이다.", PART), ("ⓐ는 'practices to play'로 바꿔도 같은 뜻의 옳은 문장이다.", TOINF),
     ("ⓐ는 주어가 3인칭 단수이므로 'playing' 대신 'plays'를 써야 옳다.", "3인칭 단수 -s는 이미 practices에 붙었고, 한 문장에 동사를 두 번 쓸 수 없으므로")], 2,
    "문장(used to keep hiding)과 정답 내용이 원문항과 같았고 오답이 뻔했다. 원문항처럼 지문 속 ⓐ 밑줄로 새로 쓰고, 그럴듯한 오개념으로 오답을 새로 썼다.")
f89("C", "Tom wanted to be healthy. So he ⓐ<u>gave up eating</u> fast food last year. Now he feels much better.",
    [("ⓐ의 'eating'은 과거진행형의 일부로, 과거에 먹고 있던 중이었다는 뜻이다.", PROG), ("ⓐ의 'gave up'은 ‘포기했다’는 뜻이므로 지금도 패스트푸드를 계속 먹고 있다는 뜻이다.", "‘먹는 것을 그만두었다’는 뜻이라 지금은 먹지 않으므로"),
     ("ⓐ는 'gave up to eat'으로 바꿔도 같은 뜻의 옳은 문장이다.", TOINF), ("ⓐ의 'give up'은 동명사를 목적어로 취하므로 뒤에 'eating'이 왔다.", "give up은 동명사를 목적어로 쓰므로"),
     ("ⓐ의 'eating'은 뒤의 'fast food'를 꾸며 주는 현재분사이다.", PART)], 4)
f89("D", "Jane is very shy. She ⓐ<u>avoids speaking</u> in front of many people. But she is trying to change.",
    [("ⓐ의 'avoid'는 동명사를 목적어로 취하는 동사이므로 뒤에 'speaking'이 왔다.", "avoid는 동명사를 목적어로 쓰므로"), ("ⓐ는 'avoids to speak'로 바꿔도 옳은 문장이다.", TOINF),
     ("ⓐ의 'speaking'은 지금 말하고 있는 중이라는 진행의 뜻이다.", PROG), ("ⓐ의 'speaking'은 앞의 'She'를 꾸며 주는 현재분사이다.", PART),
     ("ⓐ는 'avoid'가 ‘즐기다’라는 뜻이므로 사람들 앞에서 말하기를 좋아한다는 뜻이다.", "avoid는 ‘피하다’라는 뜻이라 말하기를 피한다는 뜻이므로")], 1)
f89("E", "Our class had a big test yesterday. After the test, we ⓐ<u>finished cleaning</u> the classroom together. Then we went home.",
    [("ⓐ의 'cleaning'은 뒤의 'the classroom'을 꾸며 주는 현재분사이다.", PART), ("ⓐ는 교실 청소를 아직 시작하지 않았다는 뜻이다.", "청소를 끝냈다는 뜻이므로"),
     ("ⓐ는 'finished to clean'으로 바꿔도 같은 뜻의 옳은 문장이다.", TOINF), ("ⓐ의 'finished'가 과거형이므로 뒤의 'cleaning'도 'cleaned'로 써야 옳다.", "목적어 자리의 동명사는 시제에 따라 바뀌지 않으므로"),
     ("ⓐ의 'finish'는 동명사를 목적어로 취하는 동사이므로 뒤에 'cleaning'이 왔다.", "finish는 동명사를 목적어로 쓰므로")], 5)
f89("F", "My brother and I love sports. We ⓐ<u>enjoy playing</u> soccer after school. We play almost every day.",
    [("ⓐ는 'enjoy to play'로 바꿔도 같은 뜻의 옳은 문장이다.", TOINF), ("ⓐ의 'playing'은 지금 축구를 하고 있는 중이라는 진행의 뜻이다.", PROG),
     ("ⓐ의 'enjoy'는 동명사를 목적어로 취하는 동사이므로 뒤에 'playing'이 왔다.", "enjoy는 동명사를 목적어로 쓰므로"), ("ⓐ의 'playing'은 뒤의 'soccer'를 꾸며 주는 현재분사이다.", PART),
     ("ⓐ는 'enjoy'가 조동사처럼 쓰였으므로 뒤에 동사원형 'play'를 써야 옳다.", "enjoy는 조동사가 아닌 일반동사로 동명사를 목적어로 쓰므로")], 3)

# 3-90 동명사 옳은 문장 개수: 원문항 형식(ⓐ~ⓔ, 1개~5개)
R90 = "동명사 주어는 단수 취급한다. 전치사 뒤와 enjoy·avoid·finish·keep·mind·consider·suggest 뒤에는 동명사를, want·hope·plan·decide 뒤에는 to부정사를 쓴다."
S90 = "보기 기호 ⓐ~ⓔ가 a~e로 바뀌어 한 줄로 이어졌고 선택지 순서가 뒤섞였다. 원문항 형식(ⓐ~ⓔ 줄바꿈, 1개~5개)으로 되돌렸다."
def f90(t, lines, judge, ok, s=S90):
    n = len(ok.split(","))
    F(3, 90, t, p="\n".join(lines), c=CNT5, a=n, r=R90, pre=["문장별 판정: " + j for j in judge], k=f"어법상 옳은 문장은 {ok}로 {n}개이다.", n="cnt", s=s + ipos(n))
f90("B", ["ⓐ Reading comic books is fun.", "ⓑ She is good at make friends.", "ⓒ I don't mind sitting here.", "ⓓ Walking in the rain make me happy.", "ⓔ Thank you for calling me."],
    ["ⓐ O. 동명사 주어 + is이다.", "ⓑ X. 전치사 at 뒤에는 동명사(making)를 쓴다.", "ⓒ O. mind + 동명사이다.", "ⓓ X. 동명사 주어는 단수 취급하므로 makes를 쓴다.", "ⓔ O. 전치사 for 뒤에 동명사를 썼다."], "ⓐ, ⓒ, ⓔ",
    "ⓐ~ⓒ가 원문항 문장과 같았고 정답 개수(2개)도 같았으며 기호·선택지 순서도 원본과 달랐다. 문장을 새로 쓰고 원문항 형식으로 되돌렸으며 정답 개수를 3개로 바꿨다.")
f90("C", ["ⓐ I enjoy reading.", "ⓑ Tom avoids meeting him.", "ⓒ Jane plans going home.", "ⓓ We finished cleaning.", "ⓔ They keep talking."],
    ["ⓐ O. enjoy + 동명사이다.", "ⓑ O. avoid + 동명사이다.", "ⓒ X. plan은 to부정사(to go)를 목적어로 쓴다.", "ⓓ O. finish + 동명사이다.", "ⓔ O. keep + 동명사이다."], "ⓐ, ⓑ, ⓓ, ⓔ")
f90("D", ["ⓐ Swimming is fun.", "ⓑ She wants learning English.", "ⓒ We don't mind waiting.", "ⓓ Tom decided leaving.", "ⓔ I look forward to meet you."],
    ["ⓐ O. 동명사 주어 + is이다.", "ⓑ X. want는 to부정사(to learn)를 목적어로 쓴다.", "ⓒ O. mind + 동명사이다.", "ⓓ X. decide는 to부정사(to leave)를 목적어로 쓴다.", "ⓔ X. look forward to 뒤에는 동명사(meeting)를 쓴다."], "ⓐ, ⓒ",
    S90 + " 다른 유형과 정답 개수가 겹치지 않게 ⓓ·ⓔ를 틀린 문장으로 바꿨다.")
f90("E", ["ⓐ He suggested going home.", "ⓑ Jane enjoys to sing.", "ⓒ They considered to move.", "ⓓ We finished to eat.", "ⓔ Tom hopes winning."],
    ["ⓐ O. suggest + 동명사이다.", "ⓑ X. enjoy는 동명사(singing)를 목적어로 쓴다.", "ⓒ X. consider는 동명사(moving)를 목적어로 쓴다.", "ⓓ X. finish는 동명사(eating)를 목적어로 쓴다.", "ⓔ X. hope는 to부정사(to win)를 목적어로 쓴다."], "ⓐ",
    S90 + " 다른 유형과 정답 개수가 겹치지 않게 ⓒ~ⓔ를 틀린 문장으로 바꿨다.")
f90("F", ["ⓐ I like reading.", "ⓑ She avoids to meet him.", "ⓒ We plan to travel.", "ⓓ Tom keeps practicing.", "ⓔ They finished the work."],
    ["ⓐ O. like는 동명사를 목적어로 쓸 수 있다.", "ⓑ X. avoid는 동명사(meeting)를 목적어로 쓴다.", "ⓒ O. plan + to부정사이다.", "ⓓ O. keep + 동명사이다.", "ⓔ O. finish + 명사 목적어이다."], "ⓐ, ⓒ, ⓓ, ⓔ",
    "틀린 문장이 없어 원문항(틀린 것 판별)과 달랐고 기호·선택지 순서도 원본과 달랐다. ⓑ를 틀린 문장으로 바꾸고 원문항 형식(ⓐ~ⓔ 줄바꿈, 1개~5개)으로 되돌렸다.")

# ---- 2차 감수(2026-10) 추가 ----
# 3-86 C~F: 대화가 한 줄뿐 → 두 줄 대화로, C의 learnings는 실제 낱말로
R86 = "전치사 뒤와 mind 뒤에는 동명사(-ing)를 쓴다. look forward to의 to도 전치사다."
S86 = "원문항은 두 사람이 주고받는 대화인데 변형은 한 사람의 말 한 줄뿐이었다. 대답을 한 줄 더해 대화로 만들었다."
def f86(t, p, items, a, s=S86):
    FIX.pop((3, 86, t), None)
    mk(3, 86, t, items, a, R86, s, p=p)
f86("C", "Jane: Are you interested in ______(learn) French?\nTom: Yes, I am. I want to visit Paris someday.",
    [("to learn", "전치사 in 뒤에 to부정사를 쓸 수 없으므로"), ("learned", "전치사 뒤에 과거형을 쓸 수 없으므로"), ("learning", "전치사 in 뒤에는 동명사를 쓰므로"), ("learn", "전치사 뒤에 동사원형을 쓸 수 없으므로"), ("is learning", "전치사 뒤에 be동사 + -ing를 쓸 수 없으므로")], 3,
    S86 + " 영어에 없는 말(learnings)은 과거형(learned)으로 바꿨다.")
f86("D", "Tom: What about ______(go) hiking this Saturday?\nMina: That's a good idea.",
    [("is going", "전치사 뒤에 be동사 + -ing를 쓸 수 없으므로"), ("go", "전치사 about 뒤에 동사원형을 쓸 수 없으므로"), ("to go", "전치사 뒤에 to부정사를 쓸 수 없으므로"), ("going", "전치사 about 뒤에는 동명사를 쓰므로"), ("goes", "전치사 뒤에 3인칭 단수 현재형을 쓸 수 없으므로")], 4,
    S86 + " 동사 형태가 아닌 goings도 goes로 바꿨다.")
f86("E", "Mina: Do you mind ______(open) the window?\nLeo: Not at all. It's hot in here.",
    [("open", "mind 뒤에 동사원형을 쓸 수 없으므로"), ("to open", "mind는 to부정사를 목적어로 쓰지 않으므로"), ("opened", "mind 뒤에 과거형을 쓸 수 없으므로"), ("is opening", "mind 뒤에 be동사 + -ing를 쓸 수 없으므로"), ("opening", "mind는 동명사를 목적어로 쓰므로")], 5,
    S86 + " 동사 형태가 아닌 openings도 opened로 바꿨다.")
f86("F", "Leo: I look forward to ______(meet) you in Seoul.\nAmy: Me, too. See you next week.",
    [("meet", "look forward to의 to는 전치사라 동사원형을 쓸 수 없으므로"), ("to meet", "전치사 to 뒤에 to부정사를 쓸 수 없으므로"), ("met", "전치사 뒤에 과거형을 쓸 수 없으므로"), ("meeting", "look forward to 뒤에는 동명사를 쓰므로"), ("is meeting", "전치사 뒤에 be동사 + -ing를 쓸 수 없으므로")], 4,
    S86 + " 동사 형태가 아닌 meetings도 met으로 바꿨다.")

# 3-88 B~F: 주어진 낱말에 없는 Is/Are 오답, 없는 철자(sitt, leav) → 주어진 낱말만으로 만든 오답
R88 = "mind, enjoy는 동명사를 목적어로 쓴다. 일반동사 의문문은 Do(Does) + 주어 + 동사원형 순서다."
S88 = "오답 가운데 주어진 낱말에 없는 be동사(Is, Are)로 시작하는 문장이 있어 낱말 목록만 보고 지울 수 있었다. 원문항처럼 주어진 낱말만으로 만든 오답(평서문 어순 + to부정사)으로 바꿨다."
def f88(t, p, sub, do, v, ing, rest, a, s=S88):
    FIX.pop((3, 88, t), None)
    D = do.capitalize(); r = (" " + rest) if rest else ""
    its = {"ok": (f"{D} {sub} {v} {ing}{r}?", f"{D} + 주어 + {v} + 동명사로 바르게 배열했으므로"),
           "to": (f"{D} {sub} {v} to {BASE[ing]}{r}?", f"{v}는 to부정사가 아니라 동명사를 목적어로 쓰므로"),
           "base": (f"{D} {sub} {v} {BASE[ing]}{r}?", f"동사원형({BASE[ing]})을 동명사({ing})로 바꿔야 하므로"),
           "inv": (f"{D} {v} {sub} {ing}{r}?", f"{D} + 주어 + 동사 순서가 아니므로"),
           "decl": (f"{sub[0].upper() + sub[1:]} {do} {v} to {BASE[ing]}{r}?", "의문문 어순(Do/Does + 주어)이 아니고 to부정사를 썼으므로")}
    order = ORD88[t]
    mk(3, 88, t, [its[k] for k in order], order.index("ok") + 1, R88, s, p=p)
BASE = {"writing": "write", "waiting": "wait", "sitting": "sit", "washing": "wash", "leaving": "leave"}
ORD88 = {"B": ["decl", "inv", "ok", "to", "base"], "C": ["base", "inv", "decl", "to", "ok"], "D": ["inv", "decl", "base", "ok", "to"], "E": ["decl", "inv", "base", "to", "ok"], "F": ["ok", "to", "decl", "base", "inv"]}
f88("B", "너는 영어로 편지 쓰는 것을 즐기니?\n(you / enjoy / write / letters / in English / do / ?)", "you", "do", "enjoy", "writing", "letters in English", 3,
    "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘너는 영어로 편지 쓰는 것을 즐기니?’로 바꾸고, 오답은 원문항처럼 주어진 낱말만으로 만들었다.")
f88("C", "그는 여기서 기다리는 것을 꺼리니?\n(he / mind / wait / here / does / ?)", "he", "does", "mind", "waiting", "here", 5)
f88("D", "너는 내 옆에 앉는 것을 꺼리니?\n(you / mind / sit / next to me / do / ?)", "you", "do", "mind", "sitting", "next to me", 4, S88 + " 영어에 없는 철자(sitt)도 없앴다.")
f88("E", "Jane은 설거지하는 것을 꺼리니?\n(Jane / mind / wash / the dishes / does / ?)", "Jane", "does", "mind", "washing", "the dishes", 5)
f88("F", "그들은 일찍 떠나는 것을 꺼리니?\n(they / mind / leave / early / do / ?)", "they", "do", "mind", "leaving", "early", 1, S88 + " 영어에 없는 철자(leav)도 없앴다.")

# 3-90 C~F: 문장이 원문항의 절반 길이 → 원문항 수준으로, D는 원문항과 같은 2개 → 3개
S90L = "보기 기호 ⓐ~ⓔ가 a~e로 바뀌어 한 줄로 이어졌고 선택지 순서가 뒤섞였으며, 문장이 서너 낱말뿐이라 원문항(일고여덟 낱말)의 절반 길이였다. 원문항 형식(ⓐ~ⓔ 줄바꿈, 1개~5개)으로 되돌리고 문장을 원문항 수준으로 늘렸다."
for t in "CDEF": FIX.pop((3, 90, t), None)
f90("C", ["ⓐ I enjoy reading books before I go to bed.", "ⓑ Tom avoids meeting him after school.", "ⓒ Jane plans going home early today.", "ⓓ We finished cleaning the classroom at five.", "ⓔ Riding a bike without a helmet is dangerous."],
    ["ⓐ O. enjoy + 동명사이다.", "ⓑ O. avoid + 동명사이다.", "ⓒ X. plan은 to부정사(to go)를 목적어로 쓴다.", "ⓓ O. finish + 동명사이다.", "ⓔ O. 동명사 주어 + is이다."], "ⓐ, ⓑ, ⓓ, ⓔ", S90L)
f90("D", ["ⓐ Swimming in the sea is a lot of fun.", "ⓑ She wants learning English this year.", "ⓒ We don't mind waiting for you here.", "ⓓ Tom decided to leave the town.", "ⓔ I look forward to meet you again."],
    ["ⓐ O. 동명사 주어 + is이다.", "ⓑ X. want는 to부정사(to learn)를 목적어로 쓴다.", "ⓒ O. mind + 동명사이다.", "ⓓ O. decide + to부정사이다.", "ⓔ X. look forward to 뒤에는 동명사(meeting)를 쓴다."], "ⓐ, ⓒ, ⓓ",
    S90L + " ⓔ를 틀린 문장으로 바꿨다.")
f90("E", ["ⓐ He suggested going home after the movie.", "ⓑ Jane enjoys to sing in front of people.", "ⓒ They considered to move to a bigger house.", "ⓓ We spent two hours to make the cake.", "ⓔ Tom hopes winning the first prize."],
    ["ⓐ O. suggest + 동명사이다.", "ⓑ X. enjoy는 동명사(singing)를 목적어로 쓴다.", "ⓒ X. consider는 동명사(moving)를 목적어로 쓴다.", "ⓓ X. spend + 시간 + -ing이므로 making을 쓴다.", "ⓔ X. hope는 to부정사(to win)를 목적어로 쓴다."], "ⓐ",
    S90L + " 다른 유형과 정답 개수가 겹치지 않게 ⓒ~ⓔ를 틀린 문장으로 바꿨다.")
f90("F", ["ⓐ I like reading books in the library.", "ⓑ She avoids to meet him at school.", "ⓒ We plan to travel to Jeju this summer.", "ⓓ Tom keeps practicing the piano every day.", "ⓔ They are busy preparing for the festival."],
    ["ⓐ O. like는 동명사를 목적어로 쓸 수 있다.", "ⓑ X. avoid는 동명사(meeting)를 목적어로 쓴다.", "ⓒ O. plan + to부정사이다.", "ⓓ O. keep + 동명사이다.", "ⓔ O. be busy + -ing이다."], "ⓐ, ⓒ, ⓓ, ⓔ",
    "틀린 문장이 없어 원문항(틀린 것 판별)과 달랐고 기호·선택지 순서도 원본과 달랐으며 문장도 서너 낱말뿐이었다. ⓑ를 틀린 문장으로 바꾸고 원문항 형식(ⓐ~ⓔ 줄바꿈, 1개~5개)과 문장 길이로 맞췄다.")
