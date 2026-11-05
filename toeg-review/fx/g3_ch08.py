import re
# 3급 CH8 to부정사 (71~80) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]
BL = "(<u>          </u>)"

# 3-71 to부정사 뒤 전치사: 원문항 발문과 밑줄 빈칸, 우리말 설명 삭제
ST71 = "다음 빈칸에 들어갈 전치사로 알맞은 것은?"
R71 = "형용사적 to부정사가 앞의 명사를 꾸밀 때, 그 명사가 전치사의 목적어이면(stand on a stool, write with a pen) 전치사를 to부정사 뒤에 남긴다."
S71 = "발문이 ‘앞 명사를 수식하는 to부정사를 완성할 전치사’라고 구조를 알려 주고, 발문에 붙은 우리말(‘위에 올라설’, ‘도구로 사용할’ 등)이 필요한 전치사를 드러냈으며 빈칸 밑줄도 사라졌다. 원문항 발문과 밑줄 빈칸으로 되돌리고 우리말을 뺐다. 우리말 없이도 보기 중 뜻이 통하는 전치사는 하나다."
def f71(t, p, vp, obj, ok, ko):
    c = V(3, 71, t)["c"]; a = int(V(3, 71, t)["ans"])
    mk(3, 71, t, [(x, f"{vp} {x} {obj}({ko}): 명사가 전치사 {x}의 목적어가 되어 뜻이 통하므로" if x == ok else f"{vp} {x} {obj}: 뜻이 통하지 않으므로") for x in c], a, R71, S71, st=ST71, p=p.replace("( )", BL))
f71("B", "The child needs a stool to stand ( ).", "stand", "a stool", "on", "발판 위에 서다")
f71("C", "I need a pen to write ( ).", "write", "a pen", "with", "펜으로 쓰다")
f71("D", "She has a friend to talk ( ).", "talk", "a friend", "to", "친구에게 말하다")
f71("E", "We need a room to study ( ).", "study", "a room", "in", "방 안에서 공부하다")
f71("F", "He found a bed to sleep ( ).", "sleep", "a bed", "on", "침대 위에서 자다")

# 3-72 B: 원문항과 같던 제시문을 새로
mk(3, 72, "B", [("what to eat", "what to + 동사원형(무엇을 먹을지)이 decide의 목적어가 되므로"), ("what to eating", "to 뒤에는 동사원형(eat)을 쓰므로"), ("that to eat", "that은 to부정사와 함께 명사구를 만들지 않으므로"),
                ("what for eat", "의문사 뒤에는 for가 아니라 to + 동사원형을 쓰므로"), ("what eat", "의문사 뒤에 to 없이 동사원형만 쓸 수 없으므로")], 1,
   "의문사 + to부정사(what to do, how to open, where to go)는 명사구로 쓰여 know, decide 등의 목적어가 된다.",
   "제시문과 정답(what to do)이 원문항과 똑같았다. 제시문을 ‘I can't decide ___ for dinner.’로 바꿨다.", p="I can't decide ________ for dinner.", okdup=True)

# 3-73 B: 원문항과 같던 제시문을 새로
mk(3, 73, "B", [("The shoes were very small for him to wear.", "‘너무 ~해서 ~할 수 없다’는 very가 아니라 too로 나타내므로"), ("The shoes were too small for him to wear them.", "주어 The shoes가 wear의 목적어이므로 them을 다시 쓰지 않으므로"),
                ("The shoes were too small for him to wear.", "too + 형용사 + for + 목적격 + to + 동사원형으로 바르게 바꿨으므로"), ("The shoes were too small for him for wear.", "for 뒤가 아니라 to 뒤에 동사원형을 쓰므로"),
                ("The shoes were enough small for him to wear.", "enough는 뜻(충분히)도 맞지 않고 형용사 뒤에 쓰므로")], 3,
   "too + 형용사 + for + 목적격 + to + 동사원형은 ‘너무 ~해서 …가 ~할 수 없다’는 뜻이다. 주어가 to부정사 동사의 목적어이면 목적어를 다시 쓰지 않는다.",
   "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘The shoes were very small. He couldn't wear them.’으로 바꿨다.", p="The shoes were very small. He couldn't wear them.")

# 3-74 in order to로 바꿀 수 없는 to: 원문항 발문, 밑줄 복원, 유형마다 오답을 새로
ST74 = "다음 밑줄 친 ‘to’를 ‘in order to’로 바꿀 수 없는 문장을 고르시오."
R74 = "목적(~하기 위해)의 to부정사만 in order to로 바꿀 수 있다. 감정의 원인(~해서), 결과(live to, grow up to, only to), 형용사 수식(easy to answer), 명사 수식(homework to do)의 to부정사는 in order to로 바꿀 수 없다."
S74 = "발문이 ‘목적이 아니라 뒤에 일어난 결과를 나타내는 문장’이라고 정답의 용법을 알려 주었고 밑줄이 사라졌으며, 목적 용법 오답 네 문장이 유형마다 같았다. 원문항 발문과 밑줄로 되돌리고 유형마다 오답을 새로 썼다."
PUR = "목적(~하기 위해)의 to부정사라 in order to로 바꿀 수 있으므로"
def f74(t, items, a, s=S74):
    mk(3, 74, t, [(" <u>to</u> ".join(x.rsplit(" to ", 1)) if "<u>" not in x else x, w or PUR) for x, w in items], a, R74, s, st=ST74)
f74("B", [("She saved money to buy a bike.", ""), ("We got up early to watch the sunrise.", ""), ("I was surprised to see him there.", "감정(surprised)의 원인(~해서)을 나타내 in order to로 바꿀 수 없으므로"),
          ("He went to the library to borrow some books.", ""), ("They practiced every day to win the game.", "")], 3,
    "정답(He grew up to be a lawyer.)이 원문항과 똑같았고 발문이 정답의 용법을 알려 주었다. 원문항 발문과 밑줄로 되돌리고, 감정의 원인을 나타내는 문장을 정답으로 새로 썼다.")
f74("C", [("I turned on the light to read a book.", ""), ("Mom went to the market to buy some fruit.", ""), ("He ran fast to catch the bus.", ""), ("Jane called her friend to say sorry.", ""),
          ("She lived to be ninety.", "‘살아서 90세가 되었다’는 결과를 나타내 in order to로 바꿀 수 없으므로")], 5)
f74("D", [("He woke up only <u>to</u> find the room empty.", "only to는 ‘~했지만 결국 …했다’는 뜻밖의 결과라 in order to로 바꿀 수 없으므로"), ("Tom studied hard to pass the exam.", ""), ("We went to the park to play soccer.", ""),
          ("She wore a coat to keep warm.", ""), ("I opened the window to let in fresh air.", "")], 1)
f74("E", [("Dad went to the bank to get some money.", ""), ("This question is easy <u>to</u> answer.", "형용사 easy를 꾸며 ‘답하기 쉽다’는 뜻이라 in order to로 바꿀 수 없으므로"), ("I set the alarm to wake up early.", ""),
          ("They came to Seoul to see the festival.", ""), ("She uses a map to find the way.", "")], 2, S74 + " 정답도 결과 용법 대신 형용사를 꾸미는 to부정사로 바꿔 다른 유형과 달리했다.")
f74("F", [("I wrote a letter to thank my teacher.", ""), ("He exercises every morning to stay healthy.", ""), ("We stood in line to buy tickets.", ""),
          ("Tom has a lot of homework <u>to</u> do.", "명사 homework를 꾸며 ‘해야 할 숙제’라는 뜻이라 in order to로 바꿀 수 없으므로"), ("She turned off the TV to study.", "")], 4, S74 + " 정답도 결과 용법 대신 명사를 꾸미는 to부정사로 바꿔 다른 유형과 달리했다.")

# 3-75 to부정사 옳은 것 개수: 원문항 형식(ⓐ~ⓔ, 밑줄, 1개~5개)
ST75 = "다음 밑줄 친 부분 중 어법상 옳은 문장의 개수를 고르시오."
R75 = "to부정사는 to + 동사원형이다. want, hope, decide, promise는 to부정사를, enjoy는 동명사를 목적어로 쓴다. 명사를 꾸미는 to부정사에서 명사가 전치사의 목적어이면 전치사를 남기고, enough는 형용사 뒤에 쓴다."
S75 = "원문항의 밑줄이 없고, 보기 기호 ⓐ~ⓔ가 a~e로 바뀌어 한 줄로 이어졌으며 선택지 순서가 뒤섞였다. 원문항 발문과 형식(ⓐ~ⓔ 줄바꿈, 밑줄, 1개~5개)으로 되돌렸다."
def f75(t, lines, judge, ok, s=S75):
    n = len(ok.split(","))
    F(3, 75, t, st=ST75, p="\n".join(lines), c=CNT5, a=n, r=R75, pre=["문장별 판정: " + j for j in judge], k=f"어법상 옳은 문장은 {ok}로 {n}개이다.", n="cnt", s=s + ipos(n))
f75("B", ["ⓐ He hopes <u>to win</u> the contest.", "ⓑ I have nothing <u>to eating</u>.", "ⓒ She promised <u>calling</u> me.", "ⓓ It is fun <u>play</u> soccer.", "ⓔ My dream is <u>to becoming</u> a pilot."],
    ["ⓐ O. hope + to부정사이다.", "ⓑ X. to 뒤에는 동사원형(eat)을 쓴다.", "ⓒ X. promise는 to부정사(to call)를 목적어로 쓴다.", "ⓓ X. 진주어는 to부정사(to play)로 쓴다.", "ⓔ X. to 뒤에는 동사원형(become)을 쓴다."], "ⓐ",
    "ⓐ~ⓒ가 원문항 문장과 같았고 기호·밑줄·선택지 순서도 원본과 달랐다. 문장을 새로 쓰고 원문항 형식으로 되돌렸으며 정답 개수를 1개로 바꿨다.")
f75("C", ["ⓐ I want <u>to learn</u> English.", "ⓑ She decided <u>going</u> home.", "ⓒ We need something <u>to eat</u>.", "ⓓ It is easy <u>to use</u>.", "ⓔ Tom enjoys <u>to swim</u>."],
    ["ⓐ O. want + to부정사이다.", "ⓑ X. decide는 to부정사(to go)를 목적어로 쓴다.", "ⓒ O. something을 꾸미는 to부정사이다.", "ⓓ O. 형용사 easy를 꾸미는 to부정사이다.", "ⓔ X. enjoy는 동명사(swimming)를 목적어로 쓴다."], "ⓐ, ⓒ, ⓓ")
f75("D", ["ⓐ I have a book <u>to read</u>.", "ⓑ She is too tired <u>to work</u>.", "ⓒ He wants <u>learning</u> English.", "ⓓ We know <u>how to get</u> there.", "ⓔ It is fun <u>to travel</u>."],
    ["ⓐ O. a book을 꾸미는 to부정사이다.", "ⓑ O. too ~ to 구문이다.", "ⓒ X. want는 to부정사(to learn)를 목적어로 쓴다.", "ⓓ O. 의문사 + to부정사이다.", "ⓔ O. 가주어 It의 진주어 to부정사이다."], "ⓐ, ⓑ, ⓓ, ⓔ")
f75("E", ["ⓐ Jane has homework <u>to do</u>.", "ⓑ Tom decided <u>to leave</u>.", "ⓒ I enjoy <u>to read</u>.", "ⓓ We need a pen <u>to write with</u>.", "ⓔ It is hard <u>to understand</u>."],
    ["ⓐ O. homework를 꾸미는 to부정사이다.", "ⓑ O. decide + to부정사이다.", "ⓒ X. enjoy는 동명사(reading)를 목적어로 쓴다.", "ⓓ O. write with a pen이므로 with를 남겼다.", "ⓔ O. 형용사 hard를 꾸미는 to부정사이다."], "ⓐ, ⓑ, ⓓ, ⓔ", S75)
f75("F", ["ⓐ I want <u>to go</u>.", "ⓑ She has a chair <u>to sit on</u>.", "ⓒ They are <u>enough strong</u> to lift it.", "ⓓ He knows <u>what to say</u>.", "ⓔ We need time <u>finishing</u> it."],
    ["ⓐ O. want + to부정사이다.", "ⓑ O. sit on a chair이므로 on을 남겼다.", "ⓒ X. enough는 형용사 뒤에 써서 strong enough로 쓴다.", "ⓓ O. 의문사 + to부정사이다.", "ⓔ X. time을 꾸미는 말은 to부정사(to finish)로 쓴다."], "ⓐ, ⓑ, ⓓ",
    S75 + " 정답 개수가 원문항(2개)과 같지 않게 ⓔ만 틀린 문장으로 바꿔 3개로 했다.")

# 3-76 B: 원문항과 같던 제시문을 새로
mk(3, 76, "B", [("to call", "promise는 to부정사를 목적어로 쓰므로"), ("to calling", "to 뒤에는 동사원형(call)을 쓰므로"), ("call", "promise 뒤에 동사원형만 쓸 수 없으므로"), ("to be call", "to be 뒤에 동사원형을 쓸 수 없으므로"), ("for call", "for 뒤에 동사원형을 쓸 수 없으므로")], 1,
   "want, hope, plan, decide, promise 등은 목적어로 to부정사를 쓴다.", "제시문(I want learning English.)과 정답이 원문항과 똑같았다. 제시문을 ‘He promised calling me back.’으로 바꿨다.", p="He promised <u>calling</u> me back.", okdup=True)

# 3-77 B: 원문항과 같던 제시문을 새로
mk(3, 77, "B", [("There is dangerous to swim in this river.", "가주어로는 There가 아니라 It을 쓰므로"), ("It is dangerous for swim in this river.", "진주어는 for가 아니라 to + 동사원형으로 쓰므로"), ("It is dangerous to swim in this river.", "가주어 It + is + 형용사 + 진주어 to부정사로 바르게 바꿨으므로"),
                ("To swim in this river is dangerous.", "제시문을 그대로 둔 것이라 가주어·진주어 구문이 아니므로"), ("This is dangerous to swim in this river.", "가주어로는 This가 아니라 It을 쓰므로")], 3,
   "to부정사 주어는 가주어 It을 앞에 두고 진주어 to부정사를 뒤로 보내 It + be동사 + 형용사 + to부정사로 쓴다.",
   "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘To swim in this river is dangerous.’로 바꿨다.", p="To swim in this river is dangerous.")

# 3-78 to부정사 + 전치사: 원문항 발문과 대화 속 밑줄, 실제로 있는 형태의 오답
ST78 = "다음 밑줄 친 부분을 바르게 고친 것을 고르시오."
R78 = "형용사적 to부정사가 앞의 명사를 꾸밀 때, 그 명사가 전치사의 목적어이면(live in a house, write with a pen) 전치사를 to부정사 뒤에 남긴다."
S78 = "발문이 ‘명사가 전치사의 목적어에 해당하는 형용사적 to부정사로’라고 정답 구조를 알려 주었고, 원문항의 대화 형식이 한 문장으로 줄었으며, 오답에 ‘to sit oning’처럼 없는 형태가 있었다. 원문항 발문과 대화 속 밑줄로 되돌리고 오답을 원문항처럼 실제로 있는 형태(-ing + 전치사, 동사원형, to + -ing 등)로 바꿨다."
def f78(t, p, v, prep, noun, order, a, s=S78):
    ing = {"live": "living", "write": "writing", "eat": "eating", "talk": "talking", "study": "studying"}[v]
    base = {f"to {v} {prep}": f"명사가 전치사의 목적어이므로(‘{v} {prep} {noun}’) to부정사 뒤에 전치사를 남긴 형태로 바르게 고쳤으므로",
            f"{ing} {prep}": "명사를 뒤에서 꾸미는 말은 -ing가 아니라 to부정사로 써야 하므로",
            v: "to와 전치사가 모두 빠졌으므로", f"to {ing}": "to 뒤에는 동사원형을 쓰고, 전치사도 빠졌으므로", f"{v} {prep}": "to 없이 동사원형으로는 명사를 꾸밀 수 없으므로"}
    mk(3, 78, t, [(x, base[x]) for x in order], a, R78, s, st=ST78, p=p)
f78("B", "Minsu: My family is moving to Seoul next month.\nJane: Really? Did you find a house <u>to live</u>?\nMinsu: Yes, we found a nice one.", "live", "in", "a house",
    ["living in", "to live in", "live", "to living", "live in"], 2, "문장과 정답(to sit on)이 원문항과 같았고 발문이 정답 구조를 알려 주었다. 원문항처럼 대화 속 밑줄로 새로 쓰고 원문항 발문으로 되돌렸다.")
f78("C", "Tom: I have to fill out this form.\nMs. Lee: Do you have a pen <u>to write</u>?\nTom: No. Can I borrow one?", "write", "with", "a pen", ["writing with", "write", "to write with", "write with", "to writing"], 3)
f78("D", "Mina: I feel lonely at my new school.\nMom: Don't worry. You'll soon find a friend <u>to talk</u>.\nMina: I hope so.", "talk", "to", "a friend", ["talk to", "to talking", "talking to", "talk", "to talk to"], 5)
f78("E", "Jisu: It's too noisy at home.\nDad: You need a quiet room <u>to study</u>.\nJisu: Then I'll go to the library.", "study", "in", "a room", ["to study in", "studying in", "study", "to studying", "study in"], 1)
f78("F", "Kevin: This soup looks delicious!\nWaiter: Oh, you don't have a spoon <u>to eat</u>.\nKevin: Can you bring me one, please?", "eat", "with", "a spoon", ["eat", "eating with", "eat with", "to eat with", "to eating"], 4)

# 3-79 B: 원문항과 같던 제시문을 새로
mk(3, 79, "B", [("Mina is smart very to solve the puzzle.", "very로는 ‘~할 만큼 충분히’를 나타낼 수 없으므로"), ("Mina is enough smart to solve the puzzle.", "enough는 형용사 뒤에 쓰므로"), ("Mina is smart enough to solve the puzzle.", "형용사 + enough + to + 동사원형으로 바르게 바꿨으므로"),
                ("Mina is smart enough solve the puzzle.", "enough 뒤에 to가 빠졌으므로"), ("Mina is smart enough for solve the puzzle.", "enough 뒤에는 for가 아니라 to + 동사원형을 쓰므로")], 3,
   "so + 형용사 + that + 주어 + can ~은 형용사 + enough + to + 동사원형(~할 만큼 충분히 …하다)으로 바꿀 수 있다. enough는 형용사 뒤에 쓴다.",
   "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘Mina is so smart that she can solve the puzzle.’로 바꾸고, 원문항처럼 enough의 위치를 묻는 오답을 넣었다.", p="Mina is so smart that she can solve the puzzle.")

# 3-80 옳은 문장으로만 짝지은 것: 원문항 발문, 줄바꿈, 옳은 문장의 부분집합 선택지 제거
ST80 = "다음 중 어법상 옳은 문장으로만 짝지어진 것은?"
R80 = "to부정사는 to + 동사원형이다. 사람의 성격을 나타내는 형용사(kind, careless, wise, nice) 뒤에는 of + 목적격을, 그 밖의 형용사 뒤에는 for + 목적격을 의미상 주어로 쓴다. decide·want는 to부정사를 목적어로 쓴다."
S80 = "발문이 ‘옳은 문장을 모두 빠짐없이 고른 것’으로 바뀌고 (가)~(마)가 한 줄로 이어졌다. 원문항 발문과 줄바꿈으로 되돌렸다. 원문항 발문에서는 옳은 문장 일부만 고른 선택지도 정답이 되므로, 그런 선택지는 틀린 문장이 섞인 조합으로 바꿨다."
S80X = S80 + " 옳은 문장이 넷이라 보기가 네 문장 조합이 되던 것을, 한 문장을 틀린 문장으로 바꿔 원문항처럼 두세 문장 조합으로 맞췄다."
def f80(t, lines, judge, ok, c, a, s=S80):
    F(3, 80, t, st=ST80, p="\n".join(lines), c=c, a=a, r=R80, pre=["문장별 판정: " + j for j in judge], k=f"어법상 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), okdup=True, s=s + ipos(a))
f80("B", ["(가) I need some water to drink.", "(나) She went to the store buy some milk.", "(다) It was kind of you to help me.", "(라) He was sad to hearing the news.", "(마) We have no time to waste."],
    ["(가) O. water를 꾸미는 to부정사이다.", "(나) X. 목적은 to + 동사원형(to buy)으로 쓴다.", "(다) O. 성격 형용사 kind 뒤에 of + 목적격을 썼다.", "(라) X. to 뒤에는 동사원형(hear)을 쓴다.", "(마) O. time을 꾸미는 to부정사이다."], "(가), (다), (마)",
    ["(가), (나), (다)", "(가), (다), (마)", "(다), (라), (마)", "(나), (마)", "(가), (라), (마)"], 2,
    "(가)가 원문항 문장과 같았고 정답 조합((라), (마))도 원문항과 같았다. 문장을 새로 쓰고 원문항 발문과 줄바꿈으로 되돌렸으며 정답 조합을 (가), (다), (마)로 바꿨다.")
f80("C", ["(가) It is easy for me to use this app.", "(나) It was kind of Jane to help me.", "(다) I need a book to reading.", "(라) Tom went out to buy milk.", "(마) She wants learning English."],
    ["(가) O. easy 뒤에 for + 목적격을 썼다.", "(나) O. 성격 형용사 kind 뒤에 of + 목적격을 썼다.", "(다) X. to 뒤에는 동사원형(read)을 쓴다.", "(라) O. 목적의 to부정사이다.", "(마) X. want는 to부정사(to learn)를 목적어로 쓴다."], "(가), (나), (라)",
    ["(가), (나), (라)", "(나), (다)", "(라), (마)", "(가), (나), (다), (마)", "(가), (나), (다)"], 1, S80 + " ②를 (나), (다)로 바꿨다.")
f80("D", ["(가) It is hard for him to understand.", "(나) It was nice of you to come.", "(다) We have a room to studying in.", "(라) She decided going home.", "(마) Tom is too tired to work."],
    ["(가) O. hard 뒤에 for + 목적격을 썼다.", "(나) O. 성격 형용사 nice 뒤에 of + 목적격을 썼다.", "(다) X. to 뒤에는 동사원형(study)을 쓴다.", "(라) X. decide는 to부정사(to go)를 목적어로 쓴다.", "(마) O. too ~ to 구문이다."], "(가), (나), (마)",
    ["(가), (라)", "(가), (나), (다)", "(가), (나), (마)", "(라), (마)", "(나), (다), (마)"], 3, S80X)
f80("E", ["(가) It is important for students to sleep well.", "(나) It was careless of Tom to lose the key.", "(다) Jane has something to eat.", "(라) We went there for see him.", "(마) He is enough old to drive."],
    ["(가) O. important 뒤에 for + 목적격을 썼다.", "(나) O. 성격 형용사 careless 뒤에 of + 목적격을 썼다.", "(다) O. something을 꾸미는 to부정사이다.", "(라) X. 목적은 to + 동사원형(to see)으로 쓴다.", "(마) X. enough는 형용사 뒤에 써서 old enough로 쓴다."], "(가), (나), (다)",
    ["(가), (나), (라)", "(가), (라), (마)", "(라), (마)", "(가), (나), (다)", "(나), (다), (라)"], 4, S80X)
f80("F", ["(가) It was wise for her to wait.", "(나) It is necessary for us to leave now.", "(다) I have a pen to write with.", "(라) Tom wants to study.", "(마) She is too young driving."],
    ["(가) X. 성격 형용사 wise 뒤에는 of + 목적격을 쓴다.", "(나) O. necessary 뒤에 for + 목적격을 썼다.", "(다) O. write with a pen이므로 with를 남겼다.", "(라) O. want + to부정사이다.", "(마) X. too ~ to 구문이므로 to drive로 쓴다."], "(나), (다), (라)",
    ["(가), (마)", "(나), (다), (라)", "(가), (나), (다)", "(나), (다), (마)", "(라), (마)"], 2, S80X)

# ---- 2차 감수(2026-10) 추가 ----
# 3-79 C~F: 영어에 없는 말 enoughly가 든 오답 → 원문항의 오답처럼 enough가 형용사 앞에 온 문장으로
R79 = "so + 형용사 + that + 주어 + can ~은 ‘형용사 + enough + to + 동사원형’(~할 만큼 충분히 …하다)으로 바꿀 수 있다. enough는 형용사 뒤에 쓴다."
for t in "CDEF":
    v = V(3, 79, t); a = int(v["ans"]); items = []
    for i, x in enumerate(v["c"]):
        if "enoughly" in x:
            m = re.match(r"(.+ (?:is|are)) (\w+) enoughly (to .+)", x)
            x = f"{m.group(1)} enough {m.group(2)} {m.group(3)}"; w = "enough는 형용사 뒤에 써야 하므로"
        elif i + 1 == a: w = "형용사 + enough + to + 동사원형으로 바르게 바꿨으므로"
        elif " very to " in x: w = "very로는 ‘~할 만큼 충분히’를 나타낼 수 없으므로"
        elif " too to " in x: w = "too는 형용사 앞에 쓰고 뜻도 ‘너무 ~해서 할 수 없다’로 반대이므로"
        else: w = "enough 뒤에는 for가 아니라 to + 동사원형을 쓰므로"
        items.append((x, w))
    mk(3, 79, t, items, a, R79, "오답 가운데 영어에 없는 말(enoughly)이 있어 형태만으로 지워졌다. 원문항의 오답처럼 enough를 형용사 앞에 둔 문장으로 바꿨다. 나머지 보기와 정답은 그대로다.")
