import re
# 1급 CH5 부정사 (41~50) 수정 예시

# 1-41 of/for 의미상 주어: for 문장 네 개를 유형마다 새로
R41 = "사람의 성품·태도를 평가하는 형용사(kind, brave, foolish, generous 등) 뒤에는 of + 목적격을, 일의 난이도·가능성·필요성을 나타내는 형용사(hard, easy, dangerous, important 등) 뒤에는 for + 목적격을 쓴다."
def of_for(sent, adj, of):
    if of: return f"형용사 {adj}: 사람의 성품을 평가하므로 of + 목적격을 쓴다. 나머지 넷(for)과 다르므로 정답이다."
    return f"형용사 {adj}: 일의 성격을 나타내므로 for + 목적격을 쓴다. 오답이다."
def f41(t, items, a, s, **kw):
    F(1, 41, t, c=[x[0] for x in items], a=a, r=R41, n=[of_for(x[0], x[1], i + 1 == a) for i, x in enumerate(items)], s=s, **kw)
S41 = "for를 쓰는 오답 네 문장이 B와 똑같아서 유형마다 새 문장으로 바꿨다."
f41("C", [("It is hard ___ children to sit still for an hour.", "hard"), ("It was easy ___ me to find the station.", "easy"), ("It was generous ___ Mina to donate the books.", "generous"),
          ("It is dangerous ___ kids to swim here alone.", "dangerous"), ("It will be possible ___ us to meet next week.", "possible")], 3, S41)
f41("D", [("It was kind ___ Jane to help the stranger.", "kind"), ("It is natural ___ babies to cry.", "natural"), ("It was hard ___ the team to accept the result.", "hard"),
          ("It is useful ___ travelers to learn a few words.", "useful"), ("It is common ___ teenagers to use smartphones.", "common")], 1, S41)
f41("E", [("It is fun ___ us to play board games.", "fun"), ("It was hard ___ Leo to wake up early.", "hard"), ("It was foolish ___ him to spend all the money.", "foolish"),
          ("It is safe ___ children to cross here.", "safe"), ("It was necessary ___ the students to wear helmets.", "necessary")], 3,
    "발문이 of/for를 고르는 기준을 통째로 설명해 답을 알려 주어 원문항 발문으로 되돌리고, B와 같던 for 문장 네 개도 새로 썼다.", st="R")
f41("F", [("It was brave ___ the child to speak up.", "brave"), ("It is easy ___ beginners to follow this recipe.", "easy"), ("It was impossible ___ them to hear the speaker.", "impossible"),
          ("It is important ___ drivers to wear seat belts.", "important"), ("It was difficult ___ Jiho to choose a gift.", "difficult")], 1, S41)

# 1-42 부사적 용법(목적): 명사적·형용사적 오답을 유형마다 새로
R42 = "to부정사가 문장의 주어·보어·목적어이면 명사적 용법, 앞의 명사를 꾸미면 형용사적 용법, 동작의 목적(~하기 위해)을 나타내면 부사적 용법이다."
U = {"s": "명사적 용법(주어)", "c": "명사적 용법(보어)", "o": "명사적 용법(목적어)", "j": "형용사적 용법(앞의 명사 수식)", "p": "부사적 용법(목적)"}
UTO = lambda x: re.sub(r"<u>([Tt]o) (.*?)</u>", r"<u>\1</u> \2", x)
S42 = "오답 네 문장(I have a report to finish 등)이 B와 똑같아서 명사적·형용사적 용법 오답을 유형마다 새로 썼다. 또 B 검토 의견(밑줄 범위가 원문항과 다름)이 이 유형에도 해당해, 원문항처럼 to에만 밑줄을 긋고 〈보기〉 다음에서 줄을 바꿨다."
def f42(t, items, a, s=S42):
    n = [(f"‘~하기 위해’라는 목적을 나타내는 {U['p']}으로 〈보기〉와 같다. 정답이다." if i + 1 == a else f"{U[k]}이라 〈보기〉의 목적을 나타내는 부사적 용법과 다르다.") for i, (x, k) in enumerate(items)]
    p = UTO(V(1, 42, t)["passage"]).replace("〈보기〉 ", "〈보기〉\n")
    F(1, 42, t, p=p, c=[UTO(x) for x, k in items], a=a, r=R42, n=n, s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f42("B", list(zip(V(1, 42, "B")["c"], ["j", "j", "p", "c", "s"])), 3,
    s="Claude 판정은 ‘적합’이었으나 검토 의견(밑줄 범위가 원문항과 다름)에 따라, 원문항처럼 to에만 밑줄을 긋고 〈보기〉 다음에서 줄을 바꿨다. 문장과 정답은 그대로다.")
f42("C", [("<u>To learn a new language</u> takes time.", "s"), ("She stayed late <u>to finish the report</u>.", "p"), ("My plan is <u>to visit Jeju this summer</u>.", "c"),
          ("There are many places <u>to see</u> in this city.", "j"), ("He wants <u>to join the soccer team</u>.", "o")], 2)
f42("D", [("We need someone <u>to fix the roof</u>.", "j"), ("I opened the window <u>to get some fresh air</u>.", "p"), ("His job is <u>to take care of animals</u>.", "c"),
          ("<u>To keep a diary</u> is a good habit.", "s"), ("She decided <u>to study abroad</u>.", "o")], 2)
f42("E", [("Do you have anything <u>to drink</u>?", "j"), ("They visited the bank <u>to exchange money</u>.", "p"), ("<u>To travel alone</u> can be exciting.", "s"),
          ("The goal of this class is <u>to improve writing skills</u>.", "c"), ("I hope <u>to see you again</u>.", "o")], 2)
f42("F", [("It is not easy <u>to make friends</u> in a new school.", "s"), ("Give me a pen <u>to write with</u>.", "j"), ("The best way is <u>to ask the teacher</u>.", "c"),
          ("Tom studied hard <u>to pass the exam</u>.", "p"), ("We planned <u>to leave at dawn</u>.", "o")], 4)

# 1-43 동명사 목적어 동사: 정답 동사를 유형마다 다르게, 동명사 동사도 다양하게
R43 = "enjoy, keep, finish, avoid, give up, mind, quit, stop, postpone, consider, dislike, hate는 동명사(-ing)를 목적어로 취할 수 있다. plan, hope, refuse, want, promise는 to부정사를 목적어로 취하므로 -ing형 앞에 쓸 수 없다."
def g43(x, bad, base):
    if x == bad: return f"{bad}: to부정사를 목적어로 취하는 동사({base})라 -ing형 앞에 쓸 수 없다. 들어갈 수 없는 말이므로 정답이다."
    return f"{x}: 동명사를 목적어로 취할 수 있으므로 빈칸에 들어갈 수 있다."
S43 = "정답이 다섯 유형 모두 원문항과 같은 decided이고 다른 보기도 원문항과 거의 같아 읽지 않고도 답할 수 있었다. 정답 동사를 {}로 바꾸고 동명사 동사도 새로 골랐다."
def f43(t, p, c, a, base):
    F(1, 43, t, p=p, c=c, a=a, r=R43, n=[g43(x, c[a - 1], base) for x in c], s=S43.format(c[a - 1]) + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f43("B", "Mina _______ studying at the café.", ["enjoyed", "planned", "kept", "gave up", "finished"], 2, "plan")
f43("C", "The interns _______ working late every Friday.", ["disliked", "avoided", "kept", "hoped", "stopped"], 4, "hope")
f43("D", "Tom _______ practicing the piano after dinner.", ["kept", "enjoyed", "finished", "quit", "refused"], 5, "refuse")
f43("E", "The engineers _______ testing the new system.", ["finished", "postponed", "wanted", "considered", "stopped"], 3, "want")
f43("F", "We _______ waiting outside in the rain.", ["promised", "didn't mind", "hated", "gave up", "avoided"], 1, "promise")

# 1-44 옳은 문장 모두: 원문항처럼 틀린 문장 두 개를 넣어 정답을 부분 조합으로
R44 = "부정사가 명사를 꾸밀 때 뒤에 필요한 전치사를 빠뜨리지 않고, -thing으로 끝나는 말은 형용사가 뒤에서 꾸민다. enough는 형용사 뒤에 오며, 성품 형용사 뒤에는 of + 목적격을 쓴다."
S44 = "다섯 문장이 모두 옳아 정답이 ‘전부’였고 여러 유형이 같은 답이라 예측할 수 있었다. 원문항처럼 틀린 문장 두 개를 넣어 정답을 부분 조합({})으로 만들고, 발문을 원문항 ‘밑줄 친 부분이 어법상 옳은 것’으로 되돌렸다. 문장마다 줄을 바꿨다."
def f44(t, lines, judge, ok, c, a):
    F(1, 44, t, st="R", p="\n".join(lines), c=c, a=a, r=R44, pre=["문장별 판정:"] + judge, k=f"어법상 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), s=S44.format(ok))
f44("B", ["a) Jane has a friend <u>to talk</u>.", "b) I found <u>something useful</u> to buy.", "c) The room is <u>large enough for us to use</u>.", "d) It was <u>generous of Mina to donate</u>.", "e) The bag is <u>too heavy for Leo to lift it</u>."],
    ["a) 틀림: ‘친구와 이야기하다’는 talk to a friend이므로 to talk to로 써야 한다.", "b) 옳음: -thing 뒤에서 형용사 useful이 꾸민다.", "c) 옳음: 형용사 + enough + for 의미상 주어 + to부정사 어순이다.",
     "d) 옳음: 성품 형용사 generous 뒤에 of + 목적격을 썼다.", "e) 틀림: to lift의 목적어가 문장의 주어 The bag이므로 it을 다시 쓰지 않는다."],
    "b, c, d", ["a, b", "b, c, d", "a, c, e", "c, d, e", "a, b, c, d"], 2)
f44("C", ["a) Mina needs a chair <u>to sit on</u>.", "b) I want <u>cold something</u> to drink.", "c) The box is <u>light enough for me to carry</u>.", "d) It was <u>kind for Tom to help</u> me.", "e) The water is <u>too hot for the child to drink</u>."],
    ["a) 옳음: ‘의자에 앉다’는 sit on a chair이므로 전치사 on을 썼다.", "b) 틀림: -thing으로 끝나는 말은 형용사가 뒤에서 꾸민다. cold something → something cold.", "c) 옳음: 형용사 + enough + for 의미상 주어 + to부정사 어순이다.",
     "d) 틀림: 성품 형용사 kind 뒤에는 of + 목적격을 쓴다. kind for Tom → kind of Tom.", "e) 옳음: too + 형용사 + for 의미상 주어 + to부정사 구문이다."],
    "a, c, e", ["b, d, e", "c, d, e", "a, c, e", "a, b, c", "a, d, e"], 3)
F(1, 44, "D", st="R", p="BR", s="a의 오류(전치사 in 누락)를 알려 주던 발문 괄호 ‘(a는 그 집 안에 거주하려 한다는 뜻이다.)’를 지우고 원문항 발문으로 되돌렸다. 문장마다 줄을 바꿨다.")
f44("E", ["a) Tom needs a pen <u>to write</u>.", "b) I have <u>something important</u> to tell you.", "c) The test is <u>enough easy</u> for children to solve.", "d) It was <u>nice of Jane to call</u> me.", "e) She was surprised <u>to hear</u> the news."],
    ["a) 틀림: ‘펜으로 쓰다’는 write with a pen이므로 to write with로 써야 한다.", "b) 옳음: -thing 뒤에서 형용사 important가 꾸민다.", "c) 틀림: enough는 형용사 뒤에 온다. enough easy → easy enough.",
     "d) 옳음: 성품 형용사 nice 뒤에 of + 목적격을 썼다.", "e) 옳음: 감정의 원인을 나타내는 부사적 용법이다."],
    "b, d, e", ["a, c, d", "c, d, e", "a, b", "a, b, e", "b, d, e"], 5)
f44("F", ["a) Mina wants a quiet room <u>to study in</u>.", "b) There is <u>exciting nothing</u> to watch.", "c) The bridge is <u>strong enough for trucks to cross</u>.", "d) It was <u>brave of Leo to act</u> quickly.", "e) Please tell me <u>what to doing</u> next."],
    ["a) 옳음: ‘방에서 공부하다’는 study in a room이므로 전치사 in을 썼다.", "b) 틀림: -thing으로 끝나는 말은 형용사가 뒤에서 꾸민다. exciting nothing → nothing exciting.", "c) 옳음: 형용사 + enough + for 의미상 주어 + to부정사 어순이다.",
     "d) 옳음: 성품 형용사 brave 뒤에 of + 목적격을 썼다.", "e) 틀림: 의문사 + to부정사이므로 what to do로 써야 한다."],
    "a, c, d", ["a, c, d", "b, c, e", "a, b, d", "c, d, e", "a, d, e"], 1)

# 1-45 seem/appear + 완료부정사
S45 = "발문을 원문항과 같게 하고 ‘선후 관계를 유지하도록’ 조건을 지웠다. ‘/’로 이어 쓴 네 문장을 원문항처럼 한 줄에 한 문장씩 나눴다."
for t in "BDEF":
    F(1, 45, t, st="R", p=V(1, 45, t)["passage"].replace(" / ", "\n"), s=S45)
c = ["lose - like", "have lost - have liked", "lost - like", "to have lost - to like", "have lost - like"]
NEED45 = ["(A)는 판단한 때(seemed)보다 먼저 일어난 일이므로 have + 과거분사를 쓴다.", "(B)는 판단한 때(seems)와 같은 때의 일이므로 동사원형을 쓴다."]
F(1, 45, "C", st="R", p="It seemed that the team had lost the game.\n= The team seemed to (A) ______ the game.\nIt seems that Jiho likes spicy food.\n= Jiho seems to (B) ______ spicy food.",
  c=c, a=5, k="팀이 진 일은 판단보다 먼저이므로 have lost, 좋아하는 것은 판단과 같은 때이므로 like가 알맞다.",
  n=tnotes(c, 5, NEED45, "팀이 진 일은 판단보다 먼저이므로 have lost, 좋아하는 것은 판단과 같은 때이므로 like가 알맞다.", labs=["(A)", "(B)"]),
  s="문장과 정답 짝(have left - understand)이 원문항과 거의 같아 동사와 상황을 lose·like로 바꿨다. 발문을 원문항과 같게 하고 줄을 나눴다.")

# 1-46 too … for … to 배열: 발문 조건 삭제, 오답을 제시어 어순만 바꾼 배열로
R46 = "too + 형용사 + for + 의미상 주어 + to부정사는 ‘(의미상 주어)가 ~하기에는 너무 …하다’는 뜻이다. 주어 + be동사 + too + 형용사 + for + 명사 + to + 동사원형 순서로 쓴다."
TOO = "too가 형용사 뒤로 갔다. too + 형용사 순서여야 하므로 오답이다."
BE = "be동사가 형용사 뒤로 갔다. 주어 + be동사 + too + 형용사 순서여야 하므로 오답이다."
FR = "too + 형용사를 문장 앞에 두어 평서문 어순(주어 + be동사)이 깨졌으므로 오답이다."
FOR = "의미상 주어 for + 명사가 to부정사 뒤로 갔다. for + 명사 + to부정사 순서여야 하므로 오답이다."
PR = "전치사가 to와 동사원형 사이로 들어갔다. to + 동사원형 뒤에 전치사를 두어야 하므로 오답이다."
S46 = "발문에 ‘형태 변화 없이 각각 한 번씩 사용’ 조건이 붙었고, 오답이 제시어에 없는 낱말(of, very, that)을 쓰거나 The를 빼서 조건만으로 지워졌다. 발문을 원문항과 같게 하고, 오답을 제시어의 어순만 바꾼 배열로 새로 만들었다."
def f46(t, c, a, notes):
    F(1, 46, t, st="R", c=c, a=a, r=R46, n=[("주어 + be동사 + too + 형용사 + for + 명사 + to부정사 어순이 바르다. 정답이다." if i + 1 == a else notes[i]) for i in range(5)], s=S46 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f46("B", ["The box too heavy is for Tom to lift.", "The box is heavy too for Tom to lift.", "Too heavy is the box for Tom to lift.", "The box is too heavy for Tom to lift.", "The box is too heavy to lift for Tom."], 4, [BE, TOO, FR, None, FOR])
f46("C", ["The jacket is too small for Mina to wear.", "The jacket too small is for Mina to wear.", "The jacket is small too for Mina to wear.", "Too small the jacket is for Mina to wear.", "The jacket is too small to wear for Mina."], 1, [None, BE, TOO, FR, FOR])
f46("D", ["The room is noisy too for us to study in.", "The room too noisy is for us to study in.", "The room is too noisy for us to study in.", "The room is too noisy for us in to study.", "Too noisy is the room for us to study in."], 3, [TOO, BE, None, PR, FR])
f46("E", ["The coffee too hot is for the child to drink.", "The coffee is hot too for the child to drink.", "Too hot is the coffee for the child to drink.", "The coffee is too hot to drink for the child.", "The coffee is too hot for the child to drink."], 5, [BE, TOO, FR, FOR, None])
f46("F", ["The road too narrow is for the truck to pass through.", "The road is too narrow for the truck to pass through.", "The road is narrow too for the truck to pass through.", "The road is too narrow for the truck through to pass.", "Too narrow the road is for the truck to pass through."], 2, [BE, None, TOO, PR, FR])

# 1-47 독립부정사: 정답 표현을 유형마다 다르게, 발문을 원문항대로
R47 = "독립부정사는 문장 전체를 꾸미는 관용 표현이다. To begin with(우선), Needless to say(말할 필요도 없이), Strange to say(이상한 말이지만), To be honest(솔직히 말하면), So to speak(말하자면), To make matters worse(설상가상으로), To be brief(간단히 말하면)를 흐름에 맞게 고른다."
MEAN = {"to begin with": "‘우선, 첫째로’", "needless to say": "‘말할 필요도 없이’", "strange to say": "‘이상한 말이지만’", "to be brief": "‘간단히 말하면’", "to be honest": "‘솔직히 말하면’",
        "to make matters worse": "‘설상가상으로’", "so to speak": "‘말하자면’", "speaking of which": "‘그 말이 나와서 말인데’"}
def f47(t, dia, c, a, why, s):
    n = [(f"{x}: {MEAN[x.lower()]}의 뜻으로 {why} 흐름에 맞는다. 정답이다." if i + 1 == a else f"{x}: {MEAN[x.lower()]}의 뜻이라 이 대화의 흐름에 맞지 않는다.") for i, x in enumerate(c)]
    F(1, 47, t, st="R", p=dia, c=c, a=a, r=R47, n=n, s=s, okdup=True)
BL = "(<u>         </u>)"
S47 = "발문이 정답의 뜻을 풀어 주었고 정답이 원문항과 같은 To make matters worse였다. 발문을 원문항과 같게 하고, 정답을 {}로 바꿔 대화도 그에 맞게 새로 썼다. 빈칸에 밑줄을 넣고 두 줄로 나눴다."
f47("B", f"A: How was the marathon yesterday? It was over 35 degrees!\nB: It was really hard. {BL}, I was completely exhausted at the end.",
    ["To begin with", "Strange to say", "Needless to say", "To be brief", "Speaking of which"], 3, "35도가 넘는 날 마라톤을 뛰고 지친 것은 당연하다는", S47.format("Needless to say"))
f47("C", f"A: Why don't you want to join the camping trip?\nB: Well, {BL}, I don't like sleeping outside. Also, I have a test on Monday.",
    ["To make matters worse", "To begin with", "Strange to say", "So to speak", "To be brief"], 2, "뒤에 Also로 이유를 하나 더 드는", S47.format("To begin with"))
f47("D", f"A: Did your cat get lost again?\nB: Yes, but {BL}, she came back home by herself after three days.",
    ["To begin with", "Needless to say", "Strange to say", "To make matters worse", "To be brief"], 3, "but 뒤에 뜻밖의 일을 말하는", S47.format("Strange to say"))
f47("E", f"A: Do you like the new haircut I got?\nB: {BL}, I liked your long hair better.",
    ["To make matters worse", "Needless to say", "To begin with", "Strange to say", "To be honest"], 5, "상대가 듣기 싫을 수 있는 생각을 털어놓는", S47.format("To be honest"))
f47("F", f"A: Your uncle knows everything about computers.\nB: Yes, he's a walking dictionary, {BL}.",
    ["to begin with", "strange to say", "needless to say", "so to speak", "to make matters worse"], 4, "‘걸어 다니는 사전’이라는 비유를 덧붙이는", S47.format("so to speak"))

# 1-48 B: 밑줄 복원
F(1, 48, "B", st="R", c=["(A) {} - (B) {}".format(*x.split(" - ")) for x in V(1, 48, "B")["c"]], p=V(1, 48, "B")["passage"].replace("(A)_____", "(<u>      A      </u>)").replace("(B)_____", "(<u>      B      </u>)"), keepx=True,
  s="원문항처럼 빈칸 (A)(B)에 밑줄을 넣고, 발문과 보기의 (A), (B) 표시를 원문항과 같게 했다. 문장과 정답은 그대로다.")

# 1-49 완료부정사를 쓰는 이유: 오답 설명을 유형마다 새로
def ST49(t): return R(1, 49)['stem'].replace("to have left", re.search(r'<u>(.+?)</u>', V(1, 49, t)['passage']).group(1))
R49 = "완료부정사 to have + 과거분사는 부정사의 일이 주절 동사(seem/appear)의 시점보다 먼저 일어났음을 나타낸다. have는 수 일치·의무·소유와 관계없다."
F(1, 49, "B", st=ST49("B"), s="발문을 원문항처럼 “밑줄 친 'to have forgotten'을 사용하는 이유에 대한 설명으로 가장 옳은 것은?”으로 고쳤다.")
S49 = "오답 네 개(3인칭 단수라 have, 항상 완료부정사만 가능 등)가 B와 똑같아서 유형마다 다른 그럴듯한 오개념으로 새로 썼다. 발문을 원문항과 같게 했다."
OK49 = "주절 동사보다 부정사의 일이 먼저 일어났음을 나타낸다는 설명이 정확하다. 정답이다."
F(1, 49, "C", st=ST49("C"), r=R49, a=3,
  c=["miss는 과거에 끝난 일이라 반드시 완료형만 쓸 수 있기 때문이다.", "seem 뒤의 to부정사는 수동태여야 하므로 have를 넣은 것이다.", "주절 seems보다 기차를 놓친 사건이 이전이므로 to have p.p.를 쓴다.",
     "Tom이 앞으로 기차를 놓칠 것이라는 미래의 추측을 나타내기 위해서이다.", "have가 ‘가지다’의 뜻으로 기차표를 가지고 있지 않음을 나타낸다."],
  n=["miss도 Tom seems to miss …처럼 단순부정사로 쓸 수 있다. 완료형은 시점 차이 때문이다.", "to have missed는 능동 완료부정사이다. 수동태와 관계없다.", OK49,
     "완료부정사는 미래가 아니라 이미 일어난 일을 나타낸다.", "여기서 have는 완료를 만드는 조동사이다. ‘가지다’의 뜻이 아니다."], s=S49)
F(1, 49, "D", st=ST49("D"), r=R49, a=5,
  c=["appear는 자동사라 뒤에 반드시 have를 써야 하기 때문이다.", "과제를 끝내는 중이라는 진행의 뜻을 나타내기 위해서이다.", "finished가 과거형이므로 앞에 have를 붙여 시제를 맞춘 것이다.",
     "과제를 끝내야 한다는 필요를 강조하기 위해서이다.", "완료부정사는 주절의 시점보다 앞선 완료 사건을 나타낸다."],
  n=["appear 뒤에도 단순부정사를 쓸 수 있다. 자동사라서 have를 쓰는 것이 아니다.", "완료부정사는 진행이 아니라 이미 끝난 일을 나타낸다.", "finished는 과거형이 아니라 과거분사로 have와 함께 완료부정사를 이룬다.",
     "필요·의무는 have to의 뜻이다. 완료부정사와 관계없다.", OK49], s=S49)
F(1, 49, "E", st=ST49("E"), r=R49, a=2,
  c=["already가 있으면 to부정사 대신 반드시 완료부정사를 써야 하기 때문이다.", "도착 사건이 현재의 추측보다 먼저 일어난 것을 나타낸다.", "소포가 사람에 의해 배달되었다는 수동의 뜻을 나타내기 위해서이다.",
     "seem은 현재형이므로 뒤에 과거형을 쓸 수 없어 have + 과거분사로 바꾼 것이다.", "도착이 앞으로 일어날 일이라는 예정을 나타내기 위해서이다."],
  n=["already는 먼저 일어났다는 뜻을 돕지만, 완료부정사를 쓰는 이유는 두 일의 시점 차이이다.", OK49, "to have arrived는 능동이다. 수동의 뜻이 아니다.",
     "부정사 안에는 원래 과거형을 쓰지 않는다. 앞선 시점을 나타내려고 완료부정사를 쓴다.", "완료부정사는 예정이 아니라 이미 일어난 일을 나타낸다."], s=S49)
F(1, 49, "F", st=ST49("F"), r=R49, a=5,
  c=["early가 과거를 나타내므로 동사를 과거분사로 바꾼 것이다.", "Leo가 떠나는 동작을 지금 반복하고 있음을 나타내기 위해서이다.", "appears가 3인칭 단수형이라 뒤에도 has 대신 have를 쓴 것이다.",
     "떠날 수 있는 능력이 있었음을 나타내기 위해서이다.", "떠난 사건이 현재의 appear보다 이전이어서 완료부정사를 쓴다."],
  n=["early는 이른 시각을 뜻할 뿐이다. 과거분사를 쓴 이유는 완료부정사를 만들기 위해서이다.", "완료부정사는 반복이 아니라 이미 끝난 일을 나타낸다.", "to 뒤에는 항상 동사원형이 오므로 have를 쓴다. 수 일치와 관계없다.",
     "능력은 can·be able to의 뜻이다. 완료부정사와 관계없다.", OK49], s=S49)

# 1-50 <조건> 문장 고르기
def cond50(x, good, v):
    if x == good: return "be + 과거분사(조건 1), to be + 과거분사(조건 2), 뜻(조건 3)을 모두 만족한다. 정답이다."
    w = x.split()
    if w[2] == "has": return "현재완료 능동형이라 조건 1(수동태)에 맞지 않는다."
    if w[2].endswith("ing") or (len(w) > 3 and w[3].endswith("ing") and w[2] == "is"): return "진행형 능동이라 조건 1(수동태)에 맞지 않는다."
    if w[2] != "is": return "사물 주어에 능동 동사를 써서 조건 1(수동태)에 맞지 않는다."
    return "부정사가 능동이라 조건 2(부정사의 수동 관계)에 맞지 않는다."
R50 = "보고·인식 동사를 수동태로 쓰고 부정사의 의미상 주어가 그 동작을 받으면 ‘주어 + be + thought/reported/known + to be + 과거분사’ 구조를 쓴다."
def f50(t, verb, pas, mean, c, a, s):
    p = f"<조건>\n'{verb}' 동사를 수동태 구조({pas})로 사용할 것.\n부정사의 의미상의 주어가 부정사의 동작을 받는 '수동'의 관계일 것.\n\"{mean}\"라는 의미일 것."
    F(1, 50, t, p=p, c=c, a=a, r=R50, n=[cond50(x, c[a - 1], verb) for x in c], s=s)
f50("C", "think", "be thought", "그 섬은 곧 개발될 것으로 생각된다.",
    ["The island thinks to be developed soon.", "The island is thought to be developed soon.", "The island is thought to develop soon.", "The island has thought to be developed soon.", "The island is thinking to be developed soon."], 2,
    "동사 expect와 조건 세 개, 정답 구조가 원문항과 똑같아 동사를 think로 바꾸고 새 뜻의 문장으로 만들었다. <조건>을 한 줄에 하나씩 나눴다.")
f50("E", "report", "be reported", "그 박물관은 다음 달에 다시 문을 열게 될 것이라고 보도된다.",
    ["The museum is reported to reopen next month.", "The museum reports to be reopened next month.", "The museum is reported to be reopened next month.", "The museum has reported to be reopened next month.", "The museum is reporting to be reopened next month."], 3,
    "원문항과 같은 동사 expect였고 ‘부정사의 수동 관계’ 조건이 빠져 있었다. 동사를 report로 바꾸고 원문항처럼 조건 세 개를 모두 넣었다.")
F(1, 50, "F", p="<조건>\n'know' 동사를 수동태 구조(be known)로 사용할 것.\n부정사의 의미상의 주어가 부정사의 동작을 받는 '수동'의 관계일 것.\n\"그 노래는 전 세계 사람들에게 사랑받는 것으로 알려져 있다.\"라는 의미일 것.",
  c=["The song is known to love by people all over the world.", "The song knows to be loved by people all over the world.", "The song has known to be loved by people all over the world.", "The song is known to be loved by people all over the world.", "The song is knowing to be loved by people all over the world."],
  a=4, r=R50,
  n=["부정사가 능동(to love)이라 조건 2를 어기고, 뒤의 by와도 맞지 않는다.", "사물 주어에 능동 동사 knows를 써서 조건 1(수동태)에 맞지 않는다.", "현재완료 능동형이라 조건 1(수동태)에 맞지 않는다.",
     "be known(조건 1), to be loved(조건 2), 뜻(조건 3)을 모두 만족한다. 정답이다.", "진행형 능동이라 조건 1(수동태)에 맞지 않는다."],
  s="‘부정사도 수동’ 조건이 빠지고 정답이 to be + 형용사(important)라 부정사 수동이라는 평가 요소가 사라졌다. 원문항처럼 조건 세 개를 넣고 정답을 to be + 과거분사 문장(to be loved)으로 바꿨다.")


# 1-50 B·D: B 검토 의견(조건이 원문항에 비해 명시적이지 않음) 반영, 원문항처럼 조건 세 개를 분명하게
def n50(x, good, pas):
    if x == good: return f"수동태 {pas}(조건 1), 부정사의 수동형 to be + 과거분사(조건 2), 뜻(조건 3)을 모두 만족한다. 정답이다."
    w = x.split()
    if "to being" in x: return "to 뒤에는 동사원형을 써야 하므로 to being이 아니라 to be + 과거분사가 되어야 한다. 조건 2(부정사의 수동형)에 맞지 않는다."
    if w[2] == "has": return "현재완료 능동형이라 조건 1(수동태)에 맞지 않는다."
    if w[2] != "is": return "사물 주어에 능동 동사를 써서 조건 1(수동태)에 맞지 않는다."
    return "to 뒤에 be 없이 과거분사를 바로 써서 부정사의 수동형(to be + 과거분사)이 아니다. 조건 2에 맞지 않는다."
def f50x(t, verb, pas, mean, s):
    V_ = V(1, 50, t); a = int(V_["ans"])
    p = f"<조건>\n'{verb}' 동사를 수동태 구조({pas})로 사용할 것.\n부정사의 의미상의 주어가 부정사의 동작을 받는 '수동'의 관계일 것.\n\"{mean}\"라는 의미일 것."
    r = f"보고·인식 동사를 수동태({pas})로 쓰고 부정사의 의미상 주어가 그 동작을 받으면 ‘주어 + {pas.replace('be ', 'be동사 + ')} + to be + 과거분사’ 구조를 쓴다. to 뒤에는 동사원형 be를 쓴다."
    F(1, 50, t, p=p, r=r, n=[n50(x, V_["c"][a - 1], pas) for x in V_["c"]], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f50x("B", "believe", "be believed", "그 계획은 승인될 것으로 믿어진다.",
     "검토 의견(조건이 원문항에 비해 명시적이지 않음)에 따라, ‘부정사도 수동일 것’처럼 짧게 줄인 조건을 원문항처럼 ‘부정사의 의미상의 주어가 부정사의 동작을 받는 수동의 관계일 것’으로 풀어 쓰고, 동사 조건과 뜻 조건도 ‘~로 사용할 것’, ‘~라는 의미일 것’으로 분명하게 썼다. ‘/’로 이어 쓴 조건은 한 줄에 하나씩 나눴다. 보기와 정답은 그대로다.")
f50x("D", "say", "be said", "그 다리는 곧 완공될 것이라고 한다.",
     "B 검토 의견(조건이 원문항에 비해 명시적이지 않음)이 이 유형에도 해당해, ‘부정사의 사건이 수동일 것’처럼 짧게 줄인 조건을 원문항처럼 ‘부정사의 의미상의 주어가 부정사의 동작을 받는 수동의 관계일 것’으로 풀어 쓰고, 동사 조건과 뜻 조건도 분명하게 썼다. ‘/’로 이어 쓴 조건은 한 줄에 하나씩 나눴다. 보기와 정답은 그대로다.")


# ---- 2차 감수(2026-10) 추가 ----
# 1-48: 빈칸을 원문항처럼 밑줄 표시로, ‘/’ 대신 줄바꿈. D·E는 정답 조합이 원문항과 같아 과거 문장을 앞에 둠
UA48, UB48 = "(<u>      A      </u>)", "(<u>      B      </u>)"
R48 = "to부정사가 나타내는 때가 seem/appear와 같으면 단순부정사(to be), 그보다 앞서면 완료부정사(to have been)를 쓴다."
def f48(t, p, a, k, s):
    c = V(1, 48, t)["c"]
    need = ["(A) 자리의 때에 맞는 부정사를 써야 한다.", "(B) 자리의 때에 맞는 부정사를 써야 한다."]
    F(1, 48, t, st="R", p=p, a=a, r=R48, k=k, n=tnotes(c, a, need, k, labs=["(A)", "(B)"], plain=True), s=s)
S48 = "‘/’로 이어 쓴 두 문장을 원문항처럼 두 줄로 나누고, 빈칸을 원문항처럼 밑줄 표시로 바꿨다."
f48("C", f"• Tom appears {UA48} healthy now.\n• Tom appears {UB48} sick last week.", 2, "(A)는 now가 있어 지금의 일이므로 to be, (B)는 last week가 있어 앞선 일이므로 to have been이 알맞다.", S48 + " 보기와 정답은 그대로다.")
f48("D", f"• The building seems {UA48} crowded years ago.\n• It seems {UB48} empty now.", 2, "(A)는 years ago가 있어 앞선 일이므로 to have been, (B)는 now가 있어 지금의 일이므로 to be가 알맞다.",
    S48 + " 정답 조합(to be - to have been)과 ‘지금 → 과거’ 순서가 원문항과 같아, 과거 문장을 앞에 두어 정답을 ② to have been - to be로 바꿨다.")
f48("E", f"• Jane appears {UA48} free earlier today.\n• She appears {UB48} busy now.", 3, "(A)는 earlier today가 있어 앞선 일이므로 to have been, (B)는 now가 있어 지금의 일이므로 to be가 알맞다.",
    S48 + " 정답 조합(to be - to have been)과 ‘지금 → 과거’ 순서가 원문항과 같아, 과거 문장을 앞에 두어 정답을 ③ to have been - to be로 바꿨다.")
f48("F", f"• Mina seems {UA48} confident during today's presentation.\n• Her classmates say she seems {UB48} very shy when she first joined the club.", 5,
    "(A)는 오늘 발표 때의 일이므로 to be, (B)는 처음 동아리에 들어왔을 때의 일이므로 to have been이 알맞다.", S48 + " 보기와 정답은 그대로다.")
