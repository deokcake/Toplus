# 7급 CH9 조동사 Can (81~90) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
R_CAN = "조동사 can은 주어가 무엇이든 모양이 바뀌지 않고(cans ×), 뒤에는 to나 -s, -ing 없이 동사원형을 쓴다. 부정은 can't(cannot), 의문문은 Can + 주어 + 동사원형 ~?이다."

# 7-81 can의 위치: 원문항 발문과 형식(번호 붙은 문장 하나)
ST781 = "다음 문장에서 ‘can’이 들어갈 위치를 고르시오."
R781 = "평서문에서 can은 주어 바로 뒤, 동사원형 바로 앞에 둔다."
S781 = "발문이 ‘번호가 붙은 말의 바로 앞에 can을 넣어 평서문을 만들려고 합니다’로 길어졌고, 원문항에 없던 제시문이 따로 붙어 같은 문장이 두 번 나왔다. 원문항 발문과 형식(번호 붙은 문장 하나)으로 되돌렸다. 보기와 정답은 그대로다."
def f781(t, subj, verb, done, c=None, s=S781):
    V_ = V(7, 81, t); c = c or V_["c"]; a = int(V_["ans"]); items = []
    for i, w in enumerate(c):
        if i + 1 == a: items.append((w, f"주어({subj}) 바로 뒤, 동사원형({verb}) 바로 앞이라 can이 들어갈 자리이므로"))
        elif i + 1 < a: items.append((w, f"can이 주어({subj})보다 앞에 오므로" if i == 0 else f"can이 주어({subj}) 가운데에 끼므로"))
        else: items.append((w, f"본동사({verb})보다 뒤라 can이 동사 앞에 오지 않으므로"))
    mk(7, 81, t, items, a, R781, s, st=ST781, p="", pre=[f"완성 문장: {done}"])
f781("B", "They", "play", "They can play soccer today.")
f781("C", "The twins", "swim", "The twins can swim very well.", c=["The", "twins", "swim", "very well", "."],
     s="발문이 ‘번호가 붙은 말의 바로 앞에 can을 넣어 평서문을 만들려고 합니다’로 길어졌고, 원문항에 없던 제시문이 붙었으며, 마침표 자리의 번호가 빠졌다. 원문항 발문과 형식으로 되돌리고 원문항처럼 마침표 앞에 ⑤를 두었다. 정답은 그대로다.")
f781("D", "Jane", "sing", "Jane can sing a song.")
f781("E", "We", "help", "We can help our teacher.")
f781("F", "Tom", "read", "Tom can read this book.")

# 7-82 알맞지 않은 것: 제시문과 옳은 오답을 유형마다 새로
S782 = "제시문(Can your dad ____?)과 옳은 오답 네 개(write, sing a song, cook well, drive a truck)가 원문항 그대로였다. 제시문의 주어와 옳은 오답을 유형마다 새로 쓰고, 틀린 보기도 원문항과 다른 실수로 바꿨다."
OK82 = lambda v: f"can 뒤에 동사원형({v})을 써서 알맞으므로"
def f782(t, p, items, a):
    mk(7, 82, t, items, a, R_CAN, S782, p=p)
f782("B", "Can your brother _______?", [("fix a bike", OK82("fix")), ("plays the drums", "can 뒤에는 동사원형 play를 써야 하는데 3인칭 단수형 plays를 썼으므로"), ("swim fast", OK82("swim")), ("make a kite", OK82("make")), ("speak Chinese", OK82("speak"))], 2)
f782("C", "Can your mom _______?", [("bake cookies", OK82("bake")), ("play tennis", OK82("play")), ("grow flowers", OK82("grow")), ("use a computer", OK82("use")), ("to drive a bus", "can 뒤에는 to 없이 동사원형 drive를 써야 하므로")], 5)
f782("D", "Can your teacher _______?", [("dance well", OK82("dance")), ("read Japanese", OK82("read")), ("climb a tree", OK82("climb")), ("playing the violin", "can 뒤에는 -ing형이 아니라 동사원형 play를 써야 하므로"), ("ride a horse", OK82("ride"))], 4)
f782("F", "Can your uncle _______?", [("draws cartoons", "can 뒤에는 동사원형 draw를 써야 하는데 3인칭 단수형 draws를 썼으므로"), ("fix a car", OK82("fix")), ("fly a drone", OK82("fly")), ("catch fish", OK82("catch")), ("build a house", OK82("build"))], 1)

# 7-83 우리말 → can 의문문: 원문항 발문
S783 = "발문이 ‘Can으로 시작하는 기본 의문문’이라고 정답의 형태를 알려 주어 평서문 어순 오답이 바로 지워졌다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def n783(o):
    if o.startswith("Cans "): return "can에는 주어와 관계없이 -s를 붙이지 않으므로"
    if o.startswith("Do "): return "can 의문문에는 Do를 함께 쓰지 않으므로"
    if not o.startswith("Can "): return "주어와 can의 자리를 바꾸지 않고 물음표만 붙였으므로"
    v = o.split()[2].rstrip("?.")
    if v.endswith("s") and v not in ("this",): return f"can 뒤에는 -s를 뺀 동사원형({v[:-1] if not v.endswith('ies') else v[:-3] + 'y'})을 써야 하므로"
    return "Can + 주어 + 동사원형 어순으로 바르게 옮겼으므로"
def f783(t):
    V_ = V(7, 83, t); a = int(V_["ans"])
    mk(7, 83, t, [(o, n783(o)) for o in V_["c"]], a, R_CAN, S783, st="R")
for t in "BCDEF": f783(t)

# 7-84 can 대답: 원문항 발문, 성별 설명 삭제, 오답을 유형마다 새로
R784 = "Can + 주어 ~? 질문에는 Yes, 대명사 + can. / No, 대명사 + can't.로 답한다. 질문의 주어를 알맞은 대명사로 바꾸고, Yes에는 can, No에는 can't를 짝지운다."
S784 = "발문이 ‘같은 대상으로 받아 can을 사용해 짧게 대답한 것’이라고 정답의 형태를 알려 주었고, 오답(No, he doesn't. / Yes, they are. / No, I can. / Yes, you can.)이 유형마다 똑같거나 원문항과 같았다. 원문항 발문으로 되돌리고, 대명사·Yes/No 짝·조동사를 잘못 쓴 대답으로 유형마다 오답을 새로 썼다."
PR = lambda q, w: f"질문의 주어({q})를 대명사({w})로 받아야 하므로"
YN = "Yes/No와 can/can't의 짝이 맞지 않으므로"
def f784(t, items, a, p=None, s=S784):
    mk(7, 84, t, items, a, R784, s, st="R", **({"p": p} if p else {}))
f784("B", [("No, she can't.", PR("your friends", "they")), ("Yes, they do.", "can으로 물었으므로 do가 아니라 can으로 답해야 하므로"), ("No, they can't.", "주어 your friends를 they로 받고 No에 can't를 바르게 짝지었으므로"), ("No, they can.", YN), ("Yes, he can.", PR("your friends", "they"))], 3)
f784("C", [("No, she can.", YN), ("Yes, she does.", "can으로 물었으므로 does가 아니라 can으로 답해야 하므로"), ("Yes, it can.", "질문의 주어 she를 it으로 바꿔 받았으므로"), ("Yes, you can.", "질문의 주어 she를 you로 바꿔 받았으므로"), ("Yes, she can.", "주어 she를 그대로 받고 Yes에 can을 바르게 짝지었으므로")], 5)
f784("D", [("Yes, he can.", "주어 Tom을 he로 받고 Yes에 can을 바르게 짝지었으므로"), ("Yes, she can.", PR("Tom", "he")), ("No, Tom can.", YN), ("Yes, he is.", "can으로 물었으므로 is가 아니라 can으로 답해야 하므로"), ("No, I can't.", PR("Tom", "he"))], 1, p="Can Tom sing?")
f784("E", [(o, w) for o, w in zip(V(7, 84, "E")["c"], ["can으로 물었으므로 does가 아니라 can으로 답해야 하므로", "주어 Mina를 she로 받고 Yes에 can을 바르게 짝지었으므로", "주어 자리에는 her가 아니라 she를 써야 하므로", "can으로 물었으므로 is가 아니라 can으로 답해야 하므로", YN])], 2, p="Can Mina lend me a pen?",
     s="발문이 ‘같은 대상으로 받아 can을 사용해 짧게 대답한 것’이라고 정답의 형태를 알려 주었고, 원문항에 없던 성별 설명(Mina는 여학생입니다.)이 붙었다. 원문항 발문으로 되돌리고 설명을 지웠다. 보기와 정답은 그대로다.")
f784("F", [("Yes, they are.", "can으로 물었으므로 are가 아니라 can으로 답해야 하므로"), ("Yes, he can.", "질문의 주어 they를 he로 바꿔 받았으므로"), ("Yes, they can't.", YN), ("Yes, they can.", "주어 they를 그대로 받고 Yes에 can을 바르게 짝지었으므로"), ("No, we can.", "주어 they를 we로 바꿨고 No와 can의 짝도 맞지 않으므로")], 4)

# 7-85 틀린 문장: 옳은 문장을 유형마다 새로
S785 = "옳은 오답 네 개(He can drive a car. / It can be hard. / They cannot speak Japanese. / The actor can't ride a horse.)가 원문항 선택지 그대로였다. 옳은 문장을 유형마다 새로 썼다."
OK85 = lambda m, v: f"{m} 뒤에 동사원형({v})을 바르게 썼으므로"
def f785(t, items, a):
    mk(7, 85, t, items, a, R_CAN, S785)
f785("C", [("My dad can cook spaghetti.", OK85("can", "cook")), ("We can't hear you well.", OK85("can't", "hear")), ("It can be cold at night.", OK85("can", "be")), ("She can to sing well.", "can 뒤에는 to 없이 동사원형 sing을 써야 하므로"), ("The boys cannot climb that tree.", OK85("cannot", "climb"))], 4)
f785("D", [("My sister can draw very well.", OK85("can", "draw")), ("They can't come to the party.", OK85("can't", "come")), ("He can plays soccer.", "can 뒤에는 plays가 아니라 동사원형 play를 써야 하므로"), ("You can use my pen.", OK85("can", "use")), ("This bird cannot fly.", OK85("cannot", "fly"))], 3)
f785("E", [("I can am quiet.", "can 뒤에는 am이 아니라 be동사의 원형 be를 써야 하므로"), ("Mina can play the flute.", OK85("can", "play")), ("We cannot stay long.", OK85("cannot", "stay")), ("Dogs can hear very well.", OK85("can", "hear")), ("You can't park here.", OK85("can't", "park"))], 1)
f785("F", [("Jiho can speak three languages.", OK85("can", "speak")), ("They cans run fast.", "can에는 주어와 관계없이 -s를 붙이지 않으므로"), ("The shop can't open today.", OK85("can't", "open")), ("He can be a good doctor.", OK85("can", "be")), ("We can see the stars tonight.", OK85("can", "see"))], 2)

# 7-86 can't 빈칸: 원문항 발문, 발문 없이도 답이 되는 보기(doesn't/don't) 교체
R786 = "뒤에 동사원형이 있고 둘째 문장이 할 수 없는 까닭을 말하면 can't(~할 수 없다)를 쓴다. be동사 부정(isn't, aren't, wasn't) 뒤에는 동사원형이 올 수 없고, doesn't/don't는 주어의 인칭·수에 맞춰야 한다."
def n786(o, subj):
    if o == "can't": return "뒤에 동사원형이 있고 둘째 문장이 할 수 없는 까닭을 말해 알맞으므로"
    if o in ("isn't", "aren't", "wasn't", "was", "am not", "were"): return f"be동사({o}) 뒤에는 동사원형이 올 수 없으므로"
    if o == "doesn't": return f"주어({subj})가 3인칭 단수가 아니라 doesn't를 쓸 수 없으므로"
    if o == "don't": return f"주어({subj})가 3인칭 단수라 don't를 쓸 수 없으므로"
def f786(t, subj, c=None, s=None):
    V_ = V(7, 86, t); c = c or V_["c"]; a = int(V_["ans"])
    mk(7, 86, t, [(o, n786(o, subj)) for o in c], a, R786, s or "발문이 ‘~할 수 없다라는 능력 부족이나 불가능을 나타내는 줄임말’이라고 정답(can't)을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.", st="R")
SD786 = "발문이 ‘~할 수 없다라는 능력 부족이나 불가능을 나타내는 줄임말’이라고 정답(can't)을 알려 주었다. 원문항 발문으로 되돌리면 {x}도 어법상 맞고 뜻도 통해 정답이 둘이 되므로, 그 보기를 주어와 맞지 않는 보기({y})로 바꿨다. 정답은 그대로다."
f786("B", "I")
f786("C", "Tom", c=["isn't", "don't", "can't", "wasn't", "aren't"], s=SD786.format(x="doesn't(Tom doesn't drive.)", y="don't"))
f786("D", "We", c=["isn't", "doesn't", "aren't", "can't", "wasn't"], s=SD786.format(x="don't(We don't see it.)", y="wasn't"))
f786("E", "The baby", c=["isn't", "can't", "was", "don't", "aren't"], s=SD786.format(x="doesn't(The baby doesn't lift this box.)", y="don't"))
f786("F", "She", c=["isn't", "wasn't", "can't", "aren't", "don't"], s=SD786.format(x="doesn't(She doesn't swim.)", y="don't"))

# 7-87 Can + 주어 + ___: 제시문을 유형마다 새로(주어·목적어)
S787 = "제시문(Can you ____ well?)이 원문항과 같고 동사만 바뀌었다. 원문항처럼 동사원형·-s·-ing·to·be동사 + 동사원형 오답을 두고, 제시문의 주어와 목적어를 유형마다 새로 썼다."
def f787(t, p, base, subj, order, a):
    forms = {"s": (base + "es" if base.endswith(("sh", "ch")) else base + "s"), "ing": (base[:-1] if base.endswith("e") else base) + "ing", "to": "to " + base, "be": ("are " if subj in ("they", "you") else "is ") + base, "base": base}
    why = {"s": "can 뒤에는 3인칭 단수형이 아니라 동사원형을 써야 하므로", "ing": "can 뒤에는 -ing형이 아니라 동사원형을 써야 하므로", "to": "can 뒤에는 to 없이 동사원형을 써야 하므로",
           "be": "can 뒤에 be동사와 동사원형을 겹쳐 쓸 수 없으므로", "base": f"Can + 주어({subj}) 뒤에 동사원형을 바르게 썼으므로"}
    mk(7, 87, t, [(forms[k], why[k]) for k in order], a, R_CAN, S787, p=p)
f787("B", "Can Tom _______ a kite?", "make", "Tom", ["s", "base", "ing", "to", "be"], 2)
f787("D", "Can your mom _______ Chinese food?", "cook", "your mom", ["s", "be", "to", "base", "ing"], 4)
f787("E", "Can they _______ the song together?", "sing", "they", ["base", "s", "ing", "to", "be"], 1)
f787("F", "Can Mina _______ her bike to school?", "ride", "Mina", ["ing", "s", "to", "be", "base"], 5)

# 7-89 s를 붙이지 않은 이유: 오답을 유형마다 새로, E·F는 3인칭 단수 주어로
R789 = "조동사 can 뒤에는 주어의 인칭·수와 관계없이 동사원형을 쓴다. 3인칭 단수 주어여도 can이 있으면 동사에 -s를 붙이지 않는다."
S789 = "오답 네 개가 B와 똑같았다. 원문항처럼 인칭·뜻·문장 부호에 관한 그럴듯한 오해로 유형마다 오답을 새로 썼다."
S789b = "오답 네 개가 B와 똑같았고, 주어({x})가 3인칭 단수가 아니어서 can이 없어도 동사에 s가 붙지 않아 ‘주어가 1인칭이다’ 같은 오답도 이유가 될 수 있었다. 원문항처럼 3인칭 단수 주어({y})로 바꾸고, 그럴듯한 오해로 오답을 새로 썼다."
def f789(t, items, a, p=None, s=S789):
    mk(7, 89, t, items, a, R789, s, **({"p": p} if p else {}))
f789("D", [("'She'가 여자를 가리키는 말이라서 동사에 s를 붙이지 않기 때문이다.", "성별은 동사 모양과 관계없으므로"), ("can은 조동사이므로, 주어가 She여도 뒤에 오는 동사는 원래 모양 sing을 쓰기 때문이다.", "조동사 can 뒤에는 동사원형을 쓰므로"),
           ("'well'처럼 꾸며 주는 말이 뒤에 오면 동사에 s를 붙이지 않기 때문이다.", "꾸며 주는 말은 동사 모양과 관계없으므로"), ("'노래하다'라는 뜻의 sing은 원래 s를 붙이지 않는 동사이기 때문이다.", "sing도 3인칭 단수 현재에서는 sings가 되므로"), ("주어 'She'를 여러 사람으로 보기 때문이다.", "She는 한 사람(3인칭 단수)이므로")], 2)
f789("E", [("help 앞에 조동사 can이 있어서, 주어가 3인칭 단수여도 동사원형을 쓰기 때문이다.", "조동사 can 뒤에는 동사원형을 쓰므로"), ("'you'가 목적어로 나오면 동사에 s를 붙이지 않기 때문이다.", "목적어는 동사 모양과 관계없으므로"), ("'돕다'라는 뜻의 help는 모양이 바뀌지 않는 동사이기 때문이다.", "help도 3인칭 단수 현재에서는 helps가 되므로"),
           ("'My brother'가 두 단어라서 복수로 보기 때문이다.", "My brother는 한 사람(3인칭 단수)이므로"), ("문장이 짧으면 동사에 s를 붙이지 않아도 되기 때문이다.", "문장의 길이는 동사 모양과 관계없으므로")], 1, p="My brother can help you.", s=S789b.format(x="We", y="My brother"))
f789("F", [("'dog'가 사람이 아니라 동물이기 때문이다.", "주어가 동물이어도 3인칭 단수이므로"), ("'fast'가 문장 맨 끝에 있기 때문이다.", "문장 끝의 말은 동사 모양과 관계없으므로"), ("'달리다'라는 뜻의 run은 짧은 동사라서 s를 붙이지 않기 때문이다.", "run도 3인칭 단수 현재에서는 runs가 되므로"),
           ("주어 'The dog' 앞에 the가 붙어 있기 때문이다.", "the는 동사 모양과 관계없으므로"), ("조동사 can 다음에 오는 동사는 s나 -ing를 붙이지 않은 원형으로 쓰기 때문이다.", "조동사 can 뒤에는 동사원형을 쓰므로")], 5, p="The dog can run fast.", s=S789b.format(x="They", y="The dog"))

# 7-90 밑줄 친 부분이 옳은 문장으로 짝: 원문항 발문·밑줄·줄바꿈, 세 개 조합 정답
ST790 = "다음 중 밑줄 친 부분이 문법적으로 옳은 문장으로 짝지어진 것을 고르시오."
R790 = "Can + 주어 + 동사원형 ~? 형태인지 본다. can에는 -s를 붙이지 않고(Cans ×), can 뒤의 동사는 -s나 to 없이 원형으로 쓴다."
def f790(t, lines, judge, c, a, s):
    ok = c[a - 1]
    F(7, 90, t, st=ST790, p="\n".join(lines), c=c, a=a, r=R790, pre=["문장별 판정: " + j for j in judge], k=f"밑줄 친 부분이 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), okdup=True, s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
S790 = "원문항은 세 개 조합이 정답인데 두 개 조합이 정답이었고, 밑줄과 줄바꿈이 사라졌으며 발문도 달랐다. 원문항 발문과 밑줄, 줄바꿈으로 되돌리고 옳은 문장이 세 개가 되도록 문장을 새로 썼다. 발문 끝의 물음표는 마침표로 바로잡았다."
S790b = "원문항 밑줄과 줄바꿈이 사라지고 발문이 ‘모두 고른 것’으로 바뀌었다. 원문항 발문과 밑줄, 줄바꿈으로 되돌렸다. 발문 끝의 물음표는 마침표로 바로잡았다."
f790("B", ["(A) Can Tom <u>reads</u> the letter?", "(B) Can Jane <u>play</u> the piano?", "(C) Can we <u>cook</u> dinner together?", "(D) <u>Cans</u> he sing a song?", "(E) Can they <u>be</u> quiet in class?"],
     ["(A) X. can 뒤에는 동사원형 read를 써야 한다.", "(B) O. can 뒤에 동사원형 play를 썼다.", "(C) O. can 뒤에 동사원형 cook을 썼다.", "(D) X. can에는 -s를 붙이지 않는다.", "(E) O. can 뒤에 be동사의 원형 be를 썼다."],
     ["(A), (B), (C)", "(B), (C), (E)", "(A), (C), (D)", "(B), (D), (E)", "(C), (D), (E)"], 2, S790)
f790("C", ["(A) Can she <u>dance</u>?", "(B) Can he <u>be</u> ready?", "(C) Can they <u>runs</u>?", "(D) <u>Cans</u> I help?", "(E) Can we <u>study</u>?"],
     ["(A) O. can 뒤에 동사원형 dance를 썼다.", "(B) O. can 뒤에 be동사의 원형 be를 썼다.", "(C) X. can 뒤에는 동사원형 run을 써야 한다.", "(D) X. can에는 -s를 붙이지 않는다.", "(E) O. can 뒤에 동사원형 study를 썼다."],
     ["(B), (C)", "(A), (D), (E)", "(A), (B), (E)", "(A), (C), (D)", "(A), (C)"], 3, S790b + " 보기와 정답은 그대로다.")
f790("D", ["(A) Can Jane <u>cook</u> pasta?", "(B) Can Tom <u>rides</u> a bike?", "(C) Can they <u>be</u> ready by noon?", "(D) <u>Cans</u> Leo swim?", "(E) Can we <u>open</u> the window?"],
     ["(A) O. can 뒤에 동사원형 cook을 썼다.", "(B) X. can 뒤에는 동사원형 ride를 써야 한다.", "(C) O. can 뒤에 be동사의 원형 be를 썼다.", "(D) X. can에는 -s를 붙이지 않는다.", "(E) O. can 뒤에 동사원형 open을 썼다."],
     ["(A), (C), (E)", "(B), (D), (E)", "(A), (B), (C)", "(B), (C), (D)", "(A), (D), (E)"], 1, S790b + " 보기와 정답은 그대로다.")
f790("E", ["(A) Can he <u>runs</u> fast?", "(B) Can we <u>play</u> outside?", "(C) <u>Cans</u> she sing this song?", "(D) Can they <u>go</u> there by bus?", "(E) Can Tom <u>read</u> this word?"],
     ["(A) X. can 뒤에는 동사원형 run을 써야 한다.", "(B) O. can 뒤에 동사원형 play를 썼다.", "(C) X. can에는 -s를 붙이지 않는다.", "(D) O. can 뒤에 동사원형 go를 썼다.", "(E) O. can 뒤에 동사원형 read를 썼다."],
     ["(A), (B), (D)", "(A), (C), (E)", "(B), (C), (D)", "(B), (D), (E)", "(C), (D), (E)"], 4, S790)
f790("F", ["(A) Can I <u>help</u>?", "(B) Can she <u>swims</u>?", "(C) Can they <u>go</u>?", "(D) Can he <u>be</u> kind?", "(E) <u>Cans</u> we run?"],
     ["(A) O. can 뒤에 동사원형 help를 썼다.", "(B) X. can 뒤에는 동사원형 swim을 써야 한다.", "(C) O. can 뒤에 동사원형 go를 썼다.", "(D) O. can 뒤에 be동사의 원형 be를 썼다.", "(E) X. can에는 -s를 붙이지 않는다."],
     ["(A), (C), (D)", "(A), (D), (E)", "(B), (C)", "(A), (B), (E)", "(C), (D), (E)"], 1,
     S790b + " 또 원문항 발문으로 되돌리면 옳은 문장 두 개만 고른 ⑤ (A), (C)도 ‘옳은 문장으로 짝지어진 것’이 되어 정답이 둘이므로, ⑤를 (C), (D), (E)로 바꿨다.")

# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, r, s, **kw):
    FIX.pop((7, n, t), None)
    mk(7, n, t, items, a, r, s, **kw)
# 7-81 D·F: 정답 위치가 B·D·E·F 모두 ② → 주어가 두세 낱말인 문장으로
def g781(t, c, a, subj, verb, done, s):
    items = []
    for i, w in enumerate(c):
        if i + 1 == a: items.append((w, f"주어({subj}) 바로 뒤, 동사원형({verb}) 바로 앞이라 can이 들어갈 자리이므로"))
        elif i + 1 < a: items.append((w, f"can이 주어({subj})보다 앞에 오므로" if i == 0 else f"can이 주어({subj}) 가운데에 끼므로"))
        else: items.append((w, f"본동사({verb})보다 뒤라 can이 동사 앞에 오지 않으므로"))
    redo(81, t, items, a, R781, s, st=ST781, p="", pre=[f"완성 문장: {done}"])
S781B = "발문이 ‘번호가 붙은 말의 바로 앞에 can을 넣어 평서문을 만들려고 합니다’로 길어졌고, 원문항에 없던 제시문이 따로 붙어 같은 문장이 두 번 나왔다. 또 정답 위치가 B·D·E·F 모두 ②였다. 원문항 발문과 형식(번호 붙은 문장 하나)으로 되돌리고, 주어의 낱말 수를 바꿔 정답 위치가 달라지게 했다."
g781("D", ["My", "little", "sister", "sing", "."], 4, "My little sister", "sing", "My little sister can sing.", S781B)
g781("F", ["His", "uncle", "fix", "bikes", "."], 3, "His uncle", "fix", "His uncle can fix bikes.", S781B)
# 7-83 D: 주어(they)가 B와 같음 / E: 정답 위치가 D·E 모두 원문항과 같은 ③
S783B = "발문이 ‘Can으로 시작하는 기본 의문문’이라고 정답의 형태를 알려 주어 평서문 어순 오답이 바로 지워졌다. 원문항 발문으로 되돌렸다."
def g783(t, opts, a, s, **kw):
    redo(83, t, [(o, n783(o)) for o in opts], a, R_CAN, s, st="R", **kw)
redo(83, "D", [("Cans your dog swim?", "can에는 주어와 관계없이 -s를 붙이지 않으므로"), ("Do your dog can swim?", "can 의문문에는 Do를 함께 쓰지 않으므로"), ("Can your dog swim?", "Can + 주어 + 동사원형 어순으로 바르게 옮겼으므로"),
     ("Your dog can swim?", "주어와 can의 자리를 바꾸지 않고 물음표만 붙였으므로"), ("Can your dog swims?", "can 뒤에는 -s를 뺀 동사원형(swim)을 써야 하므로")], 3, R_CAN, S783B + " 또 우리말의 주어(그들은)가 B와 같아 ‘너의 개는’으로 바꿨다.", st="R", p="너의 개는 수영할 수 있니?")
g783("E", ["Can she sings?", "Can she sing?", "Do she can sing?", "Cans she sing?", "She can sing?"], 2, S783B + " 또 정답 위치(③)가 원문항·D와 같아 ②와 ③의 순서를 바꿨다.")
# 7-84 D: ②(Yes, she can.)는 Tom이 남자 이름임을 알아야 지워짐(성별 설명을 지웠으므로)
FIX.pop((7, 84, "D"), None)
f784("D", [("Yes, he can.", "주어 Tom을 he로 받고 Yes에 can을 바르게 짝지었으므로"), ("Yes, they can.", PR("Tom", "he")), ("No, Tom can.", YN), ("Yes, he is.", "can으로 물었으므로 is가 아니라 can으로 답해야 하므로"), ("No, I can't.", PR("Tom", "he"))], 1, p="Can Tom sing?",
     s=S784 + " 원문항에 없던 성별 설명(Tom은 남학생입니다.)을 지웠고, 그 설명이 있어야 가를 수 있는 she 보기는 두지 않았다.")
# 7-88 E: 문장(be ready)과 정답 위치가 C와 같음 / F: 원문항 문장에서 주어만 바꿈(be quiet)
R788 = "‘~할 수 있니?’는 Can + 주어 + 동사원형 ~?으로 쓴다. be동사의 원형은 be이므로 can 뒤에는 is/are가 아니라 be를 쓴다. Do나 Are를 함께 쓰지 않는다."
def g788(t, ko, subj, adj, order, a, s):
    d = {"is": (f"Can {subj} is {adj}?", "can 뒤에는 is가 아니라 원형 be를 써야 하므로"), "are": (f"Can {subj} are {adj}?", "can 뒤에는 are가 아니라 원형 be를 써야 하므로"), "be": (f"Can {subj} be {adj}?", "Can + 주어 + be로 우리말을 바르게 옮겼으므로"),
         "do": (f"Do {subj} be {adj}?", "‘~할 수 있니’는 Do가 아니라 Can으로 물어야 하므로"), "bebe": (f"Are {subj} be {adj}?", "be동사 Are와 be를 함께 쓸 수 없고 ‘~할 수 있니’의 뜻도 없으므로")}
    mk(7, 88, t, [d[k] for k in order], a, R788, s, p=ko)
g788("E", "그녀는 행복해질 수 있니?", "she", "happy", ["be", "is", "do", "are", "bebe"], 1, "우리말과 문장(Can she be ready?)이 C(Can Mina be ready by six?)와 형용사가 같고 정답 위치(③)도 같았다(유형 간 중복). 형용사를 바꾸고 정답 위치를 옮겼다.")
g788("F", "그들은 친구가 될 수 있니?", "they", "friends", ["are", "be", "bebe", "is", "do"], 2, "우리말과 문장(Can they be quiet?)이 원문항(Can you be quiet?)에서 주어만 바꾼 것이었다. 다른 말(friends)로 바꾸고 정답 위치도 B(⑤)와 겹치지 않게 옮겼다.")
# 7-89 B: 오답이 짧은 일반론, 동사(read)가 C와 같음 / C: 오답이 짧고 정답만 긺, 용어가 원문항과 다름
ST789 = lambda v: f"다음 문장에서 '{v}' 뒤에 's'를 붙이지 않은 이유로 가장 적절한 설명을 고르세요."
mk(7, 89, "B", [("주어인 'Tom'이 여러 명(복수)이기 때문이다.", "Tom은 한 사람(3인칭 단수)이므로"), ("'English'가 언어 이름이라 동사의 모양을 바꿀 수 없기 때문이다.", "목적어는 동사 모양과 관계없으므로"),
   ("'can' 뒤에 오는 동사는 주어가 Tom이어도 s를 붙이지 않은 원래 모양으로 쓰기 때문이다.", "조동사 can 뒤에는 동사원형을 쓰므로"), ("'말하다'라는 뜻의 speak는 항상 s를 붙이지 않고 쓰기 때문이다.", "speak도 3인칭 단수 현재에서는 speaks가 되므로"),
   ("동사 뒤에 다른 낱말이 오면 동사에 s를 붙이지 않기 때문이다.", "뒤에 오는 낱말은 동사 모양과 관계없으므로")], 3, R789,
   "오답이 문장과 관계없는 짧은 일반론(‘마침표가 있기 때문이다’ 등)이고 정답만 길고 구체적이어서 길이만으로 답이 드러났다. 동사(read)도 C와 같았다. 동사를 speak로 바꾸고, 원문항처럼 문장 속 낱말을 두고 말하는 오해로 오답을 새로 썼다.", st=ST789("speak"), p="Tom can speak English.")
mk(7, 89, "C", [("'this'가 가까이 있는 것을 가리키는 말이라 동사에 s를 붙이지 않기 때문이다.", "this는 동사 모양과 관계없으므로"), ("'map'이 한 개(단수)이면 동사에도 s를 붙이지 않기 때문이다.", "목적어의 수는 동사 모양과 관계없으므로"),
   ("'읽다'라는 뜻의 read는 언제나 s를 붙이지 않고 쓰기 때문이다.", "read도 3인칭 단수 현재에서는 reads가 되므로"), ("'can'이 앞에 있으면 주어가 Mina여도 동사 read를 원래 모양 그대로 쓰기 때문이다.", "조동사 can 뒤에는 동사원형을 쓰므로"),
   ("'Mina'가 사람 이름이라 동사의 모양을 바꿀 수 없기 때문이다.", "사람 이름이 주어여도 can이 없으면 reads를 쓰므로")], 4, R789,
   "오답이 한 줄짜리 짧은 말이고 정답만 길어 길이만으로 답이 드러났고, 정답의 용어(본동사, 기본형)도 원문항(동사의 원래 모양)과 달랐다. 오답을 원문항처럼 이유를 갖춘 문장으로 늘리고 정답의 말을 원문항에 맞췄다. 정답은 그대로다.")
# 7-90 C·F: 문장이 원문항의 절반 길이, 보기에 두 개 조합이 섞임 → 문장을 늘리고 보기를 모두 세 개 조합으로
FIX.pop((7, 90, "C"), None); FIX.pop((7, 90, "F"), None)
S790c = " 또 문장이 원문항의 절반쯤으로 짧았고(Can she dance? 등) 보기에 두 개 조합이 섞여 있었다. 문장을 원문항 길이로 늘리고 보기를 원문항처럼 모두 세 개 조합으로 맞췄다."
f790("C", ["(A) Can she <u>dance</u> on the stage?", "(B) Can he <u>be</u> a good singer?", "(C) Can they <u>runs</u> to the park?", "(D) <u>Cans</u> I help you?", "(E) Can we <u>study</u> in the library?"],
     ["(A) O. can 뒤에 동사원형 dance를 썼다.", "(B) O. can 뒤에 be동사의 원형 be를 썼다.", "(C) X. can 뒤에는 동사원형 run을 써야 한다.", "(D) X. can에는 -s를 붙이지 않는다.", "(E) O. can 뒤에 동사원형 study를 썼다."],
     ["(B), (C), (D)", "(A), (D), (E)", "(A), (B), (E)", "(A), (C), (D)", "(A), (C), (E)"], 3, S790b + S790c + " 정답은 그대로다.")
f790("F", ["(A) Can I <u>help</u> you now?", "(B) Can she <u>swims</u> in the sea?", "(C) Can they <u>go</u> home early?", "(D) Can he <u>be</u> kind to animals?", "(E) <u>Cans</u> we run in the gym?"],
     ["(A) O. can 뒤에 동사원형 help를 썼다.", "(B) X. can 뒤에는 동사원형 swim을 써야 한다.", "(C) O. can 뒤에 동사원형 go를 썼다.", "(D) O. can 뒤에 be동사의 원형 be를 썼다.", "(E) X. can에는 -s를 붙이지 않는다."],
     ["(A), (B), (E)", "(A), (D), (E)", "(B), (C), (E)", "(C), (D), (E)", "(A), (C), (D)"], 5, S790b + S790c + " 정답 위치도 D(①)와 겹치지 않게 옮겼다.")
