# 2026-10-06 B유형 감수 메모 반영 — 2급·3급
import re as _r

# 2-5 학생들의 설명을 원문항처럼 예문 + 근거 문장으로
R5m = "give·send·tell·show·teach는 3형식에서 to를, buy·make는 for를 쓴다. 사역동사 make·have + 목적어 + 동사원형이고, 목적어와 목적격 보어가 수동 관계이면 과거분사를 쓴다. 감각동사 뒤 보어는 형용사다."
_S5 = MEMO + "학생들의 설명이 ‘~는 4형식이야’처럼 짧고 근거가 없어, 원문항처럼 예문 뒤에 문법 근거를 붙인 설명으로 늘렸다. 옳고 틀림과 정답은 그대로다."
def f5m(t, lines, judge, ok, a, new=False):
    kw = dict(p="\n".join(lines), pre=["학생별 판정:"] + judge, k=f"올바르게 설명한 학생은 {ok}이다.", r=R5m, s=_S5 + pos(a))
    if new:
        c = V(2, 5, t)["c"]; F(2, 5, t, c=c, a=a, n=setnotes(c, ok, "올바르게 설명한 학생"), **kw)
    else: RE(2, 5, t, **kw)
f5m("B", ["Yuna: I sent my cousin a postcard. 'send'가 간접목적어와 직접목적어를 차례로 취한 4형식 문장이에요.", "Minho: Dad made me to wash the car. 사역동사 'make' 뒤 목적격 보어 자리에는 to부정사를 쓰므로 'to wash'가 맞아요.",
          "Sora: I bought a scarf for Mom. 'buy'를 3형식으로 쓸 때는 간접목적어 앞에 전치사 'for'를 쓰므로 옳은 문장이에요.", "Jin: We found the door locked. 문이 잠긴 수동의 관계이므로 목적격 보어로 과거분사 'locked'를 쓴 것이 맞아요.",
          "Hana: The soup tastes deliciously. 감각동사 'taste' 뒤에는 부사가 와야 하므로 'deliciously'가 맞아요."],
     ["Yuna O(send의 4형식).", "Minho X(사역동사 made 뒤에는 원형부정사 wash를 쓴다).", "Sora O(buy는 for를 쓴다).", "Jin O(문이 잠기는 수동 관계라 locked).", "Hana X(tastes 뒤에는 형용사 delicious)."], "Yuna, Sora, Jin", 1, new=True)
f5m("C", ["Mina: She gave me advice. 'give'가 '~에게 …을'의 두 목적어를 취한 4형식 문장이에요.", "Leo: The coach had us run. 사역동사 'have' 뒤 목적격 보어 자리에 원형부정사 'run'을 쓴 옳은 문장이에요.",
          "Jane: Tom sent a gift for Amy. 'send'를 3형식으로 쓸 때는 받는 사람 앞에 'for'를 쓰므로 옳은 문장이에요.", "Ben: I got my phone repaired. 휴대폰이 수리되는 수동의 관계이므로 과거분사 'repaired'를 쓴 것이 맞아요.",
          "Sally: The flowers smell sweetly. 감각동사 'smell' 뒤 보어 자리에는 부사 'sweetly'를 써야 해요."],
     ["Mina O(give의 4형식).", "Leo O(사역동사 had 뒤 원형부정사 run).", "Jane X(send는 to를 쓴다. sent a gift to Amy).", "Ben O(휴대폰이 수리되는 수동 관계라 과거분사).", "Sally X(smell 뒤 보어 자리에는 형용사 sweet)."], "Mina, Leo, Ben", 4)
f5m("D", ["Tom: We told him the truth. 'tell'이 간접목적어 'him'과 직접목적어 'the truth'를 취한 4형식 문장이에요.", "Amy: Mom made me clean my room. 사역동사 'make' 뒤 목적격 보어로 원형부정사 'clean'을 쓴 옳은 문장이에요.",
          "Joon: Dad bought a ticket to me. 'buy'를 3형식으로 바꿀 때는 'to'를 쓰므로 옳은 문장이에요.", "Mina: She kept the door open. 'open'은 목적어 'the door'의 상태를 설명하는 목적격 보어로 쓰인 형용사예요.",
          "Leo: The soup tastes well. 감각동사 'taste' 뒤에는 부사 'well'을 써야 하므로 옳은 문장이에요."],
     ["Tom O(tell의 4형식).", "Amy O(사역동사 made 뒤 원형부정사 clean).", "Joon X(buy는 for를 쓴다. bought a ticket for me).", "Mina O(open은 형용사 목적격 보어).", "Leo X(tastes 뒤에는 형용사 good)."], "Tom, Amy, Mina", 4, new=True)
f5m("E", ["Jane: He showed me the photo. 'show'가 간접목적어 'me'와 직접목적어 'the photo'를 취한 4형식 문장이에요.", "Ben: I heard her sing. 지각동사 'hear' 뒤 목적격 보어 자리에 원형부정사 'sing'을 쓴 옳은 문장이에요.",
          "Sora: We made lunch to the children. 'make'를 3형식으로 바꿀 때는 'to'를 쓰므로 옳은 문장이에요.", "Min: They elected Tom president. 'president'는 목적어 'Tom'을 보충 설명하는 목적격 보어예요.",
          "Hana: The milk smells sourly. 감각동사 'smell' 뒤 보어 자리에는 부사 'sourly'를 쓰는 것이 맞아요."],
     ["Jane O(show의 4형식).", "Ben O(지각동사 heard 뒤 원형부정사 sing).", "Sora X(make는 for를 쓴다. made lunch for the children).", "Min O(president는 목적격 보어).", "Hana X(smells 뒤에는 형용사 sour)."], "Jane, Ben, Min", 5)
f5m("F", ["Mina: She taught us English. 'teach'가 간접목적어 'us'와 직접목적어 'English'를 취한 4형식 문장이에요.", "Leo: The joke made me laugh. 사역동사 'make' 뒤 목적격 보어로 원형부정사 'laugh'를 쓴 옳은 문장이에요.",
          "Jane: I bought flowers to my teacher. 'buy'를 3형식으로 바꿀 때는 받는 사람 앞에 'to'를 쓰므로 옳은 문장이에요.", "Tom: We found the window broken. 창문이 깨진 수동의 관계이므로 목적격 보어로 과거분사 'broken'을 쓴 것이 맞아요.",
          "Amy: The room looks quietly. 감각동사 'look' 뒤에는 부사 'quietly'를 써야 하므로 옳은 문장이에요."],
     ["Mina O(teach의 4형식).", "Leo O(사역동사 made 뒤 원형부정사 laugh).", "Jane X(buy는 for를 쓴다. bought flowers for my teacher).", "Tom O(창문이 깨진 수동 관계라 broken).", "Amy X(looks 뒤에는 형용사 quiet)."], "Mina, Leo, Tom", 2, new=True)

# 2-14 A·B 대화를 줄바꿈으로
for _t in "BCDEF":
    _o = OLD(2, 14, _t)
    RE(2, 14, _t, c=[x.replace(" B: ", "\nB: ", 1) for x in _o["c"]], s=_o["s"].replace(", 두 줄로 나뉜 대화를 원문항처럼 한 줄로 했다", "") + " " + MEMO + "A와 B의 대화를 줄을 바꿔 제시했다.")

# 2-55 B 설명을 원문항처럼 근거 있게
F(2, 55, "B", p="\n".join(["Mina: I need a pen to write with. 는 pen이 전치사 with의 목적어이므로 to부정사 뒤에 with를 남긴 옳은 문장이에요.", "Leo: I have nobody to talk to. 에서 talk 뒤의 to는 필요 없으므로 반드시 빼야 해요.",
                            "Jane: It was kind for you to help me. 는 사람의 성품을 평가하는 kind 뒤에 의미상 주어 for you를 쓴 옳은 표현이에요.", "Ben: This box is too heavy for me to lift. 는 too + 형용사 + for + 목적격 + to부정사로 ‘너무 ~해서 …할 수 없다’를 나타낸 옳은 문장이에요.",
                            "Sora: She is old enough to travel alone. 는 enough가 형용사 old 뒤에 온 옳은 문장이에요."]),
  c=V(2, 55, "B")["c"], a=5, r="to부정사가 꾸미는 명사가 전치사의 목적어이면 전치사를 남긴다(a pen to write with). 성품 형용사(kind) 뒤 의미상 주어는 of다. too ~ for + 목적격 + to부정사, 형용사 + enough + to부정사의 어순을 지킨다.",
  pre=["학생별 판정:", "Mina O(write with a pen이므로 with를 남긴다).", "Leo X(talk to somebody이므로 to를 남겨야 한다).", "Jane X(성품 형용사 kind 뒤 의미상 주어는 of you).", "Ben O(too ~ for + 목적격 + to부정사).", "Sora O(enough는 형용사 뒤에 온다)."],
  k="올바르게 설명한 학생은 Mina, Ben, Sora다.", n=setnotes(V(2, 55, "B")["c"], "Mina, Ben, Sora", "올바르게 설명한 학생"), s=MEMO + "학생들의 설명이 ‘~는 맞아’처럼 단조로워, 원문항처럼 예문 뒤에 문법 근거를 붙인 설명으로 늘렸다. 옳고 틀림과 정답은 그대로다." + pos(5))

# 2-63 보기 문장을 원문항 길이로
R63m = "동명사는 명사처럼 주어, 동사·전치사의 목적어, 보어로 쓰인다. be동사 뒤에서 ‘~하고 있다’는 진행형을 만드는 -ing는 현재분사다."
_K63 = {"V": "{v}의 목적어인 동명사이므로 오답이다.", "P": "전치사 {v}의 목적어인 동명사이므로 오답이다.", "S": "주어로 쓰인 동명사이므로 오답이다.", "C": "be동사 뒤에서 ‘~하는 것’으로 풀리는 보어 자리의 동명사이므로 오답이다.",
        "ING": "be동사와 함께 ‘{v}’는 진행형을 이루는 현재분사라 나머지와 다르므로 정답이다."}
def f63m(t, c, kinds, new=False):
    a = [k[0] for k in kinds].index("ING") + 1
    n = [_K63[k[0]].format(v=k[1] if len(k) > 1 else "") for k in kinds]
    kw = dict(c=c, a=a, n=n, r=R63m, s=MEMO + "원문항보다 짧던 보기 문장을 원문항 길이로 늘렸다. 밑줄 친 -ing의 쓰임과 정답은 그대로다." + pos(a))
    F(2, 63, t, **kw) if new else RE(2, 63, t, **kw)
f63m("B", ["He enjoys <u>swimming</u> in the sea every summer.", "Mina is <u>preparing</u> dinner for her family right now.", "She is good at <u>drawing</u> cartoon characters.", "<u>Reading</u> before bed helps me relax after a long day.", "Thank you for <u>coming</u> to my birthday party."],
     [("V", "enjoys"), ("ING", "준비하고 있다"), ("P", "at"), ("S",), ("P", "for")], new=True)
f63m("C", ["My favorite hobby is <u>collecting</u> old stamps from other countries.", "He gave up <u>eating</u> fast food for his health.", "<u>Riding</u> a bike along the river is a lot of fun.", "She left the room without <u>saying</u> goodbye to anyone.", "Tom is <u>writing</u> an email to his teacher now."],
     [("C",), ("V", "gave up"), ("S",), ("P", "without"), ("ING", "쓰고 있다")])
f63m("D", ["I don't mind <u>waiting</u> here for a few minutes.", "We talked about <u>moving</u> to Busan next year.", "The children are <u>playing</u> outside in the yard now.", "<u>Keeping</u> a diary every day is a good habit.", "She is proud of <u>being</u> a nurse at the hospital."],
     [("V", "mind"), ("P", "about"), ("ING", "놀고 있다"), ("S",), ("P", "of")])
f63m("E", ["Jane was <u>waiting</u> for the bus in the rain.", "Would you mind <u>closing</u> the door behind you?", "<u>Exercising</u> regularly keeps you healthy and fit.", "I'm afraid of <u>making</u> mistakes in front of others.", "They practiced <u>singing</u> for the school concert."],
     [("ING", "기다리고 있었다"), ("V", "mind"), ("S",), ("P", "of"), ("V", "practiced")])
f63m("F", ["He is interested in <u>learning</u> Spanish and French.", "<u>Taking</u> a walk after dinner is relaxing and healthy.", "She kept <u>talking</u> during the whole movie.", "I'm tired of <u>hearing</u> the same song every morning.", "We are <u>watching</u> a movie in the living room now."],
     [("P", "in"), ("S",), ("V", "kept"), ("P", "of"), ("ING", "보고 있다")])

# 2-75 지문을 원문항 길이로(밑줄·보기·정답 그대로)
_S75 = MEMO + "원문항보다 짧던 지문을 원문항 길이로 늘렸다. 밑줄 친 분사와 보기, 정답은 그대로다."
RE(2, 75, "B", p="Yesterday, Mina went hiking with her family for the first time this year. ①<u>Climbing</u> up the steep mountain path, she saw many colorful birds ②<u>flying</u> above the tall pine trees. At the top, there was a small bench ③<u>made</u> of old wood, and from there she could see the whole town. ④<u>Feeling</u> tired after the long climb, she sat on it for a while and drank some water. ⑤<u>Refreshing</u> by the cool wind, she walked down the mountain happily with her family.", s=_S75 + pos(5))
RE(2, 75, "C", p="Last Saturday, Tom visited a flea market in the old part of the city. ①<u>Walked</u> around the crowded stalls for an hour, he found an old film camera on a dusty table. The camera, ②<u>made</u> in Germany more than fifty years ago, still looked great. The seller ③<u>standing</u> behind the table smiled at him and told him its story. ④<u>Surprised</u> at the low price, Tom bought it right away without thinking twice. ⑤<u>Holding</u> the camera carefully in his hands, he took pictures all the way home.", s=_S75 + pos(1))
RE(2, 75, "D", p="On a cold afternoon, Jane entered a small café near the station to warm up. The smell of freshly ①<u>baked</u> bread filled the cozy room. She saw a gray cat ②<u>sleeping</u> peacefully by the window in the sunlight. ③<u>Sitting</u> at a table in the corner, she ordered a cup of hot chocolate. The drink ④<u>serving</u> in a big blue cup was sweet and warm. ⑤<u>Satisfied</u> with the café and its quiet mood, she decided to come back every weekend.", s=_S75 + pos(4))
RE(2, 75, "E", p="On a rainy Sunday, Leo stayed home all day. ①<u>Bored</u> with TV programs, he started reading a novel he had bought last month. The story ②<u>written</u> by a young author was more exciting than he had expected. ③<u>Turned</u> the pages quickly, he completely forgot about the time. Around seven, he heard his mom ④<u>calling</u> him for dinner from the kitchen. ⑤<u>Closing</u> the book with a smile, he went downstairs to join his family.", s=_S75 + pos(3))
RE(2, 75, "F", p="Last Friday, Sora went to a rock concert with her two best friends. ①<u>Excited</u> about the show, they arrived at the hall two hours early. A band ②<u>played</u> loud rock music came on stage, and the crowd began to cheer. ③<u>Surrounded</u> by cheering fans, Sora sang along to every song she knew. ④<u>Having</u> enjoyed the show from beginning to end, they went home late at night. On the way, she found a ticket ⑤<u>dropped</u> on the street and returned it to the hall.", s=_S75 + pos(2))

# 2-80 지문 밖 문장을 설명하던 보기를 지문의 (A)·(B)에 대한 설명으로
def f80m(t, i, text, note, s):
    o = OLD(2, 80, t); c = list(o["c"]); n = list(o["n"]); c[i - 1] = text; n[i - 1] = note
    RE(2, 80, t, c=c, n=n, s=o["s"] + " " + MEMO + s)
f80m("B", 2, "도현: (B)는 학생들이 다른 사람을 지루하게 만들었다는 뜻이야.", "(B)의 bored는 학생들이 지루함을 느꼈다는 뜻인데 남을 지루하게 만들었다고 풀었으므로 정답이다.", "지문 밖의 문장(The teacher was boring.)을 설명하던 ②를 지문의 (B)에 대한 틀린 설명으로 바꿨다. 정답 위치 ②.")
f80m("D", 4, "시안: (A)의 tiring은 여행이 피곤함을 일으키는 쪽임을 나타내.", "(A)의 tiring은 여행이 피곤함을 일으키는 쪽임을 바르게 말했으므로 오답이다.", "지문 밖의 표현(a tiring day)을 설명하던 ④를 지문의 (A)에 대한 옳은 설명으로 바꿨다.")
f80m("E", 5, "은우: (A)의 frightening을 frightened로 바꾸면 이야기가 겁을 먹었다는 어색한 뜻이 돼.", "(A)의 frightening을 frightened로 바꾸면 이야기가 겁을 먹었다는 뜻이 되어 어색하다고 바르게 말했으므로 오답이다.", "지문 밖의 표현(a frightening movie 등)을 설명하던 ⑤를 지문의 (A)에 대한 옳은 설명으로 바꿨다.")
f80m("F", 4, "준서: (A)를 'The result was disappointed.'로 바꿔도 뜻이 같아.", "(A)의 disappointing은 결과가 실망을 ‘주는’ 쪽인데 disappointed로 바꾸면 결과가 실망을 ‘느낀다’는 뜻이 되어 같지 않으므로 정답이다.", "지문 밖의 표현(a disappointed result)을 설명하던 ④를 지문의 (A)에 대한 틀린 설명으로 바꿨다. 정답 위치 ④.")

# 2-81 B 제시문을 자연스러운 문장으로
F(2, 81, "B", p="This library is the quietest place _____ our school.\nSora is the most experienced _____ all the guides.", c=V(2, 81, "B")["c"], a=1,
  r="최상급 뒤에서 범위를 나타낼 때 장소·단체(단수) 앞에는 in을, 복수 명사(구성원) 앞에는 of를 쓴다.",
  n=["our school은 장소라 in, all the guides는 복수의 구성원이라 of를 쓰므로 정답이다.", "our school 앞에는 of가 아니라 in을 써야 하므로 오답이다.", "all the guides 앞에는 in이 아니라 of를 써야 하므로 오답이다.",
     "among은 복수 명사 앞에 쓰는 말이라 장소 our school 앞에 올 수 없고, all the guides 앞에는 of를 써야 하므로 오답이다.", "in과 of가 서로 바뀌었으므로 오답이다."],
  s=MEMO + "지명이 낯설고 뜻이 어색하던 제시문(Lake Mira ~ the region, the six guides)을 원문항처럼 자연스러운 두 문장으로 바꿨다. 보기와 정답은 그대로다." + pos(1))

# 2-82 어려운 강조어(considerably, a great deal)를 일반적인 것으로
R82m = "비교급을 ‘훨씬’이라는 뜻으로 강조할 때는 much, even, far, still, a lot을 쓴다. very·so·too는 원급만 꾸민다."
_E82 = "{x}는 비교급을 강조하는 말이라 들어갈 수 있으므로 오답이다."
RE(2, 82, "B", c=["very", "far", "still", "a lot", "much"], a=1, r=R82m, n=["very는 원급만 꾸미고 비교급 앞에는 쓸 수 없으므로 정답이다."] + [_E82.format(x=x) for x in ["far", "still", "a lot", "much"]],
   s=OLD(2, 82, "B")["s"] + " " + MEMO + "중2 수준에 어려운 considerably·a great deal을 still·a lot으로 바꿨다. 정답 위치 ①.")
RE(2, 82, "F", c=["still", "much", "so", "a lot", "far"], a=3, r=R82m, n=[_E82.format(x="still"), _E82.format(x="much"), "so는 원급을 꾸미는 말이라 비교급(colder)을 직접 꾸밀 수 없어 들어갈 수 없으므로 정답이다.", _E82.format(x="a lot"), _E82.format(x="far")],
   s=OLD(2, 82, "F")["s"] + " " + MEMO + "중2 수준에 어려운 considerably·a great deal을 much·a lot으로 바꿨다. 정답 위치 ③.")

# 2-94 보기를 ‘(a)-ㄹ, (b)-ㄱ’ 형태로
R94m = "that은 지시대명사(저것), 관계대명사(선행사 뒤, 뒤에 불완전한 절), 접속사(뒤에 완전한 절: 명사절)로 쓰인다."
def lab94(c): return [_r.sub(r"^([ㄱ-ㄹ])-([ㄱ-ㄹ])$", r"(a)-\1, (b)-\2", x) for x in c]
_o94 = OLD(2, 94, "B"); RE(2, 94, "B", c=lab94(_o94["c"]), okdup=True, s=_o94["s"] + " " + MEMO + "보기를 (a)·(b)를 밝힌 형태로 바꿨다.")
def f94m(t, pre, n, a):
    o = OLD(2, 94, t)
    RE(2, 94, t, c=lab94(V(2, 94, t)["c"]), a=a, r=R94m, pre=[pre], okdup=True, n=[x + OK(i + 1, a) for i, x in enumerate(n)], s=o["s"] + " " + MEMO + "보기를 (a)·(b)를 밝힌 형태로 바꿨다." + pos(a))
f94m("C", "보기 판정: ㄱ 관계대명사(선행사 The song을 꾸밈), ㄴ 지시대명사(‘저것’), ㄷ 명사절 접속사(목적어 자리), ㄹ 명사절 접속사(주어 자리).",
     ["(a)는 접속사가 아니라 지시대명사이므로", "(a)는 ㄴ과 같은 지시대명사, (b)는 ㄱ과 같은 관계대명사이므로", "(a)는 접속사가 아니라 지시대명사이므로", "(b)는 접속사가 아니라 관계대명사이므로", "(a)는 접속사가 아니라 지시대명사이고 (b)는 지시대명사가 아니라 관계대명사이므로"], 2)
f94m("D", "보기 판정: ㄱ 명사절 접속사(목적어 자리), ㄴ 관계대명사(선행사 The bag을 꾸밈), ㄷ 지시대명사(‘저것’), ㄹ 명사절 접속사(주어 자리).",
     ["(b)는 관계대명사인데 접속사 ㄱ을 골랐으므로", "(a)는 지시대명사인데 관계대명사 ㄴ을 골랐으므로", "(a)는 관계대명사 ㄴ이 아니고 (b)도 접속사 ㄹ이 아니므로", "(a)는 ㄷ과 같은 지시대명사, (b)는 ㄴ과 같은 관계대명사이므로", "(a)는 접속사 ㄹ이 아니고 (b)도 지시대명사 ㄷ이 아니므로"], 4)
f94m("E", "보기 판정: ㄱ 관계대명사(선행사 The plan을 꾸밈), ㄴ 명사절 접속사(주어 자리), ㄷ 지시대명사(‘저것’), ㄹ 명사절 접속사(목적어 자리).",
     ["(a)는 ㄷ과 같은 지시대명사, (b)는 ㄱ과 같은 관계대명사이므로", "(a)는 접속사 ㄴ이 아니고 (b)도 접속사 ㄹ이 아니므로", "(a)는 접속사 ㄹ이 아니고 (b)도 지시대명사 ㄷ이 아니므로", "(b)는 관계대명사인데 접속사 ㄴ을 골랐으므로", "(a)는 지시대명사인데 접속사 ㄴ을 골랐으므로"], 1)
f94m("F", "보기 판정: ㄱ 명사절 접속사(목적어 자리), ㄴ 지시대명사(‘저것’), ㄷ 명사절 접속사(주어 자리), ㄹ 관계대명사(선행사 The house를 꾸밈).",
     ["(a)는 접속사 ㄷ이 아니고 (b)도 지시대명사 ㄴ이 아니므로", "(a)는 관계대명사 ㄹ이 아니고 (b)도 접속사 ㄷ이 아니므로", "(a)는 ㄴ과 같은 지시대명사, (b)는 ㄹ과 같은 관계대명사이므로", "(a)는 접속사 ㄷ이 아니고 (b)도 접속사 ㄱ이 아니므로", "(b)는 관계대명사인데 접속사 ㄱ을 골랐으므로"], 3)

# 2-124 대화를 원문항 길이로(밑줄·보기·정답 그대로)
_S124 = MEMO + "원문항보다 짧던 대화에 말을 더해 길이를 맞췄다. 밑줄 표현·보기·정답은 그대로다."
RE(2, 124, "B", p="Mina: If ①<u>I were</u> taller, I would join the basketball team. I'm the shortest girl in my class.\nLeo: You're still good at sports. I wish ②<u>I had been</u> at the tryouts last week. I missed them because I was sick.\nMina: That's too bad. If ③<u>you had come</u>, you would have made the team for sure.\nLeo: Maybe. I wish ④<u>I can play</u> as well as you. You practice every day.\nMina: Thanks. If only ⑤<u>I had</u> more time to practice with you!", s=_S124 + pos(4))
RE(2, 124, "C", p="Tom: I wish ①<u>I knew</u> the answer to this question. I've been thinking about it for an hour.\nAmy: If ②<u>I have</u> the textbook, I would lend it to you. I left it at school.\nTom: Thanks anyway. If ③<u>I had studied</u> harder last week, I wouldn't be so worried now.\nAmy: I wish ④<u>you had asked</u> me earlier. We could have studied together.\nTom: You're right. If only ⑤<u>I were</u> as smart as you!", s=_S124 + pos(2))
RE(2, 124, "D", p="Jane: If ①<u>it had not rained</u> yesterday, we would have gone hiking. I was really looking forward to it.\nBen: I know. I wish ②<u>the weather were</u> better today, too. Look at those clouds.\nJane: If ③<u>I were</u> you, I would check the forecast first before making plans.\nBen: Good idea. If only ④<u>I had checked</u> it yesterday! We wouldn't have wasted the whole day.\nJane: Don't worry. I wish ⑤<u>we will go</u> hiking next weekend.", s=_S124 + pos(5))
RE(2, 124, "E", p="Sora: I wish ①<u>I had</u> a pet dog. All my friends have one.\nMin: If ②<u>you had</u> a dog, you would have to walk it every day, even in winter.\nSora: I know. I wouldn't mind. If ③<u>my mom allows</u> it, I would get one right away.\nMin: I understand. I wish ④<u>my apartment were</u> bigger, too. Then I could keep a dog.\nSora: If only ⑤<u>we lived</u> in a house with a big yard!", s=_S124 + pos(3))
RE(2, 124, "F", p="Leo: If ①<u>I have known</u> about the sale, I would have bought the shoes. They were half price last weekend.\nAmy: I wish ②<u>you had told</u> me you wanted them. I would have gone with you.\nLeo: If ③<u>I had</u> more money now, I would buy them anyway. They're still nice.\nAmy: If only ④<u>they were</u> still on sale! The price went back up yesterday.\nLeo: I wish ⑤<u>I could go</u> back to that day.", s=_S124 + pos(1))

# ---------------- 3급 ----------------
# 3-9 <보기> 문장과 설명 가~라 사이에 빈 줄
for _t in "BCDEF":
    _o = OLD(3, 9, _t); _l = _o["p"].split("\n")
    RE(3, 9, _t, p="\n".join(_l[:2] + [""] + _l[2:]), s=_o["s"] + " " + MEMO + "<보기> 문장과 설명 가~라 사이에 빈 줄을 넣어 구분했다.")

# 3-10 문장을 원문항 길이로
_S10 = MEMO + "원문항보다 짧던 문장을 원문항 길이로 늘렸다. 틀린 곳과 정답은 그대로다."
def f10m(t, lines, a): RE(3, 10, t, p="<보기>\n" + "\n".join("- " + x for x in lines), s=_S10 + pos(a))
f10m("B", ["This morning, there was a lot of people waiting at the bus stop near my house.", "The bus were late because of the heavy rain.", "My friends and I were cold, but we talked and laughed together.", "The driver was very kind and said sorry to everyone."], 2)
f10m("C", ["Yesterday, there was two accidents on the road near our school.", "The road was busy with cars and buses all morning.", "The drivers were careful after the accidents.", "There were many police officers at the crossing until noon."], 1)
f10m("D", ["Last week, there were many visitors at the new museum downtown.", "The museum were crowded with students from other cities.", "There was two guides in the main hall for the visitors.", "We were tired after the long tour, but it was fun."], 2)
f10m("E", ["There were a lot of snow on the roads this morning.", "The roads was slippery and dangerous for cars.", "My brother were late for school because of the snow.", "I were worried about him until he called me."], 4)
f10m("F", ["There were many dark clouds in the sky yesterday afternoon.", "The sky was dark all day, so we turned on the lights early.", "There was a strong wind from the sea in the evening.", "The children were inside the house with their grandparents."], 5)

# 3-30 B·D 지문을 원문항 길이로
RE(3, 30, "B", p="<보기>\nYesterday morning, I woke up early to see ⓐ<u>the sun</u> rise over the river. After ⓑ<u>breakfast</u>, I went to the library ⓒ<u>by bus</u> with my sister. In ⓓ<u>the afternoon</u>, I played ⓔ<u>soccer</u> with my friends in the park until dinner.",
   s=OLD(3, 30, "B")["s"] + " " + MEMO + "원문항보다 짧던 지문을 원문항 길이로 늘렸다. 밑줄 표현·보기·정답은 그대로다.")
RE(3, 30, "D", p="<보기>\nThis morning, Jane ate ⓐ<u>breakfast</u> with her family and went to school ⓑ<u>by bus</u>. After class, she played ⓒ<u>tennis</u> with her friends and returned home in ⓓ<u>the afternoon</u>. On her way home, she looked up at ⓔ<u>the sky</u> and saw a beautiful rainbow.",
   s=OLD(3, 30, "D")["s"] + " " + MEMO + "원문항보다 짧던 지문을 원문항 길이로 늘렸다. 밑줄 표현·보기·정답은 그대로다.")

# 3-40 ‘Dear Diary,’ 삭제
_o40 = OLD(3, 40, "B"); RE(3, 40, "B", p=_o40["p"].replace("Dear Diary,\n", ""), s=_o40["s"] + " " + MEMO + "편지도 일기도 아닌 형식이 되던 첫 줄 ‘Dear Diary,’를 지웠다.")

# 3-62 질문(A)·대답(B)을 줄바꿈으로
for _t in "BCDEF":
    _o = OLD(3, 62, _t)
    RE(3, 62, _t, c=[x.replace(" B: ", "\nB: ", 1) for x in _o["c"]], s=_o["s"] + " " + MEMO + "질문(A)과 대답(B)을 줄을 바꿔 제시했다.")

# 3-70 지문을 원문항 길이로
_S70b = MEMO + "원문항보다 짧던 지문을 원문항 길이로 늘렸다. 질문·보기·정답은 그대로다."
RE(3, 70, "B", p="Last Saturday, our class went on a field trip to the science museum in the city. We left school at nine in the morning and arrived there by bus an hour later. At the museum, we saw many robots and watched a short movie about space travel. Minho lost his cap on the bus, but the kind driver found it and gave it back to him. Everyone had a great time and wanted to visit again.\nQ: ________________________?\n(너희 반은 어디로 현장 학습을 갔니?)\nA: We went to the science museum.", s=_S70b + pos(2))
RE(3, 70, "C", p="My grandmother's birthday was yesterday, so my family had a small party for her. In the morning, my sister and I made a chocolate cake for her in the kitchen. In the evening, we all had dinner together at a Chinese restaurant near her house. She was very happy with our gift, a warm wool scarf, and wore it right away.\nQ: ________________________?\n(너희 가족은 할머니께 무엇을 선물했니?)\nA: We gave her a warm scarf.", s=_S70b + pos(5))
RE(3, 70, "D", p="Jisu practiced the piano for three hours yesterday after school. She has a big piano contest next week, and she wants to do her best. Her teacher listened to her playing and said that it was getting much better. Jisu is a little nervous, but she hopes to win first prize this time.\nQ: ________________________?\n(지수는 어제 얼마나 오래 피아노를 연습했니?)\nA: She practiced for three hours.", s=_S70b + pos(1))
RE(3, 70, "E", p="Tom was late for school this morning for the first time this year. He missed the school bus because his alarm clock didn't ring. He ran all the way to school, but he still arrived ten minutes late. His teacher was not angry, but she told him to buy a new alarm clock soon.\nQ: ________________________?\n(Tom은 왜 버스를 놓쳤니?)\nA: Because his alarm clock didn't ring.", s=_S70b + pos(3))
RE(3, 70, "F", p="Mina and her little brother visited the zoo with their parents on Sunday. They saw lions, elephants, monkeys, and a baby giraffe that was born last month. Mina liked the baby giraffe the most because it had big, gentle eyes. They took many pictures of it and showed them to their grandmother that evening.\nQ: ________________________?\n(미나는 어떤 동물을 가장 좋아했니?)\nA: She liked the baby giraffe the most.", s=_S70b + pos(4))

# 3-91 위치 문항: 번호를 넣은 영어 문장을 제시하고 보기는 번호만
_S91 = MEMO + "영어 문장이 보이지 않고 보기에 낱말만 있던 형식을, 원문항과 함께 낱말 사이에 번호를 넣은 영어 문장을 제시하고 보기는 번호만 두는 형식으로 바꿨다. 정답은 그대로다."
def posm(g_, n_, t, ko, words, a, s):
    o = OLD(g_, n_, t)
    RE(g_, n_, t, p=(ko + "\n" if ko else "") + numbered(words), c=numc(), a=a, n=o["n"], s=s + pos(a))
posm(3, 91, "B", "나에게 먹을 따뜻한 것을 좀 줘.", ["Please", "give", "me", "something", "to eat."], 5, _S91)
posm(3, 91, "C", "나는 읽을 재미있는 책이 두 권 있다.", ["I", "have", "two", "books", "to read."], 4, _S91)
posm(3, 91, "D", "그녀는 파티에 입을 예쁜 드레스들이 있다.", ["She", "has", "dresses", "to wear", "for the party."], 3, _S91)
posm(3, 91, "E", "Tom은 오늘 해야 할 중요한 무언가가 있다.", ["Tom", "has", "something", "to do", "today."], 4, _S91)
posm(3, 91, "F", "정원에 아름다운 꽃 몇 송이가 있다.", ["Some", "flowers", "are", "in", "the garden."], 2, _S91)

# 3-92 위치 문항(전수 조사): 보기를 번호만으로
for _t in "BCDEF":
    _o = OLD(3, 92, _t)
    RE(3, 92, _t, c=numc(), s=_o["s"] + " " + MEMO + "(위치 문항 전수 조사) 뒤의 낱말까지 적혀 있던 보기를 번호만으로 바꿨다.")

# 3-100 B 문장을 원문항 길이로
RE(3, 100, "B", p="\n".join(["ⓐ There are few cookies left in the jar on the table.", "ⓑ She looked at me angry when I broke her cup.", "ⓒ I always am tired after school on Mondays.", "ⓓ Can I have a little water before the game starts?", "ⓔ We need much eggs for the cake this afternoon."]),
   s=OLD(3, 100, "B")["s"] + " " + MEMO + "원문항보다 짧던 문장을 원문항 길이로 늘렸다. 틀린 곳과 정답은 그대로다.")

# 3-102 표 형식: 칸을 탭으로 나눠 표로 보이게(B는 이미 탭)
_S102 = MEMO + "띄어쓰기로만 나뉘어 표로 읽기 어렵던 제시문의 칸을 탭으로 나눠 표로 보이게 했다. 보기와 정답은 그대로다."
F(3, 102, "C", p="Name\tJane\tAmy\nAge\t15\t15\nWeight\t50kg\t50kg\nHeight\t160cm\t165cm", s=_S102 + pos(4))
F(3, 102, "D", p="Name\tBen\tLeo\nAge\t13\t15\nWeight\t45kg\t55kg\nHeight\t150cm\t170cm", s=_S102 + pos(5))
F(3, 102, "E", p="Name\tMina\tSora\nAge\t14\t14\nWeight\t48kg\t52kg\nHeight\t158cm\t158cm", s=_S102 + pos(1))
F(3, 102, "F", p="Name\tTom\tBen\nAge\t16\t14\nWeight\t60kg\t60kg\nHeight\t175cm\t165cm", s=_S102 + pos(1))

# 3-108 모든 보기가 주어진 낱말만 쓰게
R108m = "‘가장 ~한 것 중 하나’는 one of the + 최상급 + 복수명사로 쓴다."
_K108 = {"OK": "one of the + 최상급({sup}) + 복수명사({pl})로 바르게 썼으므로 정답이다.", "SING": "최상급 뒤에 단수 {sg}를 썼으므로 복수형 {pl}이 되어야 하므로 오답이다.", "COMP": "‘가장 ~한 것 중 하나’는 비교급 {cmp}가 아니라 최상급 {sup}을 쓰므로 오답이다.",
         "THE1": "the가 one 앞에 와서 one of the + 최상급 어순이 깨졌으므로 오답이다.", "THE2": "the가 최상급 {sup} 뒤로 가서 one of the + 최상급 어순이 깨졨으므로 오답이다.", "MOSTTHE": "the가 most 뒤로 가서 one of the most + 원급 어순이 깨졌으므로 오답이다.", "MOST1": "the most가 one 앞에 와서 one of the most + 원급 어순이 깨졌으므로 오답이다."}
def f108m(t, c, kinds, w):
    a = kinds.index("OK") + 1
    RE(3, 108, t, c=c, a=a, r=R108m, n=[_K108[k].format(**w).replace("깨졨", "깨졌") for k in kinds], s=MEMO + "주어진 낱말에 없는 most를 쓰거나 the를 빼고 만든 오답을 주어진 낱말만 쓴 오답으로 바꿨다. 정답은 그대로다." + pos(a))
f108m("B", ["This is one of the oldest building in our town.", "This is one of the older buildings in our town.", "This is the one of oldest buildings in our town.", "This is one of the oldest buildings in our town.", "This is one of oldest the buildings in our town."],
      ["SING", "COMP", "THE1", "OK", "THE2"], dict(sup="oldest", pl="buildings", sg="building", cmp="older"))
f108m("C", ["Tom is one of the tallest student in our class.", "Tom is one of the taller students in our class.", "Tom is one of the tallest students in our class.", "Tom is one of tallest the students in our class.", "Tom is the one of tallest students in our class."],
      ["SING", "COMP", "OK", "THE2", "THE1"], dict(sup="tallest", pl="students", sg="student", cmp="taller"))
f108m("D", ["This is one of the most expensive bag in the store.", "This is one of the most expensive bags in the store.", "This is one of most the expensive bags in the store.", "This is the most one of expensive bags in the store.", "This is the one of most expensive bags in the store."],
      ["SING", "OK", "MOSTTHE", "MOST1", "THE1"], dict(sup="most expensive", pl="bags", sg="bag", cmp="more expensive"))
f108m("E", ["Jane is one of the faster players on the team.", "Jane is the one of fastest players on the team.", "Jane is one of fastest the players on the team.", "Jane is one of the fastest player on the team.", "Jane is one of the fastest players on the team."],
      ["COMP", "THE1", "THE2", "SING", "OK"], dict(sup="fastest", pl="players", sg="player", cmp="faster"))
f108m("F", ["The Han River is one of the longest river in Korea.", "The Han River is one of the longest rivers in Korea.", "The Han River is one of the longer rivers in Korea.", "The Han River is the one of longest rivers in Korea.", "The Han River is one of longest the rivers in Korea."],
      ["SING", "OK", "COMP", "THE1", "THE2"], dict(sup="longest", pl="rivers", sg="river", cmp="longer"))

# 3-140 지문 끝 ‘(A) (B) (C)’ 줄 삭제, 보기마다 (A)·(B)·(C)
def lab140(c): return [_r.sub(r"^(\S+) - (\S+) - (\S+)$", r"(A) \1 - (B) \2 - (C) \3", x) for x in c]
for _t in "BCDEF":
    _o = OLD(3, 140, _t)
    RE(3, 140, _t, p=_r.sub(r"\n\(A\)\t\(B\)\t\(C\)$", "", _o["p"]), c=lab140(_o["c"]), s=_o["s"].replace("원문항 발문과 표 머리로 되돌렸으며", "원문항 발문으로 되돌렸으며").replace("원문항 발문과 표 머리로 되돌리고", "원문항 발문으로 되돌리고") + " " + MEMO + "지문 끝의 ‘(A) (B) (C)’ 줄을 지우고 보기마다 (A)·(B)·(C)를 붙였다.")
