# 2급 CH8 분사 (71~80) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def talk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[w + (" 틀린 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.") for i, (_, w) in enumerate(items)],
      k=f"틀린 설명을 한 학생은 {items[a-1][0].split(':')[0]}이다. {items[a-1][1]}", s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def pair(c, a, good, why):
    """'x — y' 짝 보기 해설: 정답과 다른 자리만 짚는다. why[j][form] = 그 형태가 틀린 까닭"""
    out = []
    for i, ch in enumerate(c):
        parts = [p.strip() for p in re.split(r"\s+[—-]\s+", ch)]
        if i + 1 == a: out.append(f"{' — '.join(good)}: 두 자리가 모두 알맞으므로 정답이다."); continue
        bits = [f"{['첫째', '둘째', '셋째'][j]} 자리 {x}: {why[j][x]}" for j, x in enumerate(parts) if x != good[j]]
        out.append(" ".join(bits) + " 따라서 오답이다.")
    return out

# 2-71 밑줄 친 동사 두 개의 알맞은 형태: 원문항 형식
ST71 = "다음 밑줄 친 동사의 알맞은 형태를 바르게 짝지은 것을 고르시오."
R71 = "명사가 직접 하는 동작은 현재분사(-ing)로, 동작을 받는 명사는 과거분사로 꾸민다. 문장의 동사 자리는 주어와의 관계에 따라 진행형(be + -ing)이나 수동태(be + 과거분사)로 쓴다."
S71 = "원문항은 문장 속 밑줄 친 동사 두 개를 알맞은 형태로 고친 짝을 고르는 형식인데, 변형은 명사 앞 빈칸 하나에 현재분사를 넣는 형식으로 바뀌었고 발문이 뜻까지 알려 주었다. 원문항 발문과 형식으로 다시 썼다."
def f71(t, p, c, a, good, why, k):
    F(2, 71, t, st=ST71, p=p, c=c, a=a, r=R71, n=pair(c, a, good, why), k=k, s=S71 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f71("B", "The boy <u>ride</u> a bike is <u>wave</u> at us.", ["ridden — waving", "riding — waving", "riding — waved", "ridden — waved", "rides — waving"], 2, ["riding", "waving"],
    [{"ridden": "소년이 직접 자전거를 타는 능동 관계라 과거분사는 맞지 않는다.", "rides": "문장의 동사(is)가 따로 있어 명사를 꾸미는 자리에 동사 형태를 쓸 수 없다."},
     {"waved": "소년이 손을 흔드는 중이므로 be동사 뒤에 현재분사로 진행형을 만든다."}],
    "소년이 자전거를 타는 능동 관계라 riding이 명사를 꾸미고, 손을 흔드는 중이므로 is waving의 진행형이 된다.")
f71("C", "The window <u>break</u> by the ball was <u>fix</u> yesterday.", ["breaking — fixing", "broken — fixing", "broken — fixed", "breaking — fixed", "broke — fixed"], 3, ["broken", "fixed"],
    [{"breaking": "창문이 공에 깨진 수동 관계라 현재분사는 맞지 않는다.", "broke": "과거형은 명사를 꾸미지 못하며 과거분사(broken)를 써야 한다."},
     {"fixing": "창문이 고쳐진 수동 관계이므로 was 뒤에 과거분사를 쓴다."}],
    "창문이 공에 깨진 수동 관계라 broken이 명사를 꾸미고, 창문이 고쳐졌으므로 was fixed의 수동태가 된다.")
f71("D", "The man <u>wear</u> glasses was <u>arrest</u> by the police.", ["wearing — arrested", "wearing — arresting", "worn — arrested", "worn — arresting", "wears — arrested"], 1, ["wearing", "arrested"],
    [{"worn": "남자가 직접 안경을 쓴 능동 관계라 과거분사는 맞지 않는다.", "wears": "문장의 동사(was)가 따로 있어 명사를 꾸미는 자리에 동사 형태를 쓸 수 없다."},
     {"arresting": "남자가 경찰에게 체포된 수동 관계이므로 was 뒤에 과거분사를 쓴다."}],
    "남자가 안경을 쓴 능동 관계라 wearing이 명사를 꾸미고, 남자가 체포되었으므로 was arrested의 수동태가 된다.")
f71("E", "The cat <u>sleep</u> on the sofa was <u>wake</u> up by the noise.", ["slept — woken", "sleeping — woke", "sleeps — woken", "sleeping — woken", "slept — waking"], 4, ["sleeping", "woken"],
    [{"slept": "고양이가 스스로 자고 있던 능동 관계라 과거형(과거분사)은 맞지 않는다.", "sleeps": "문장의 동사(was)가 따로 있어 명사를 꾸미는 자리에 동사 형태를 쓸 수 없다."},
     {"woke": "was 뒤 수동태에는 과거형이 아니라 과거분사(woken)를 쓴다.", "waking": "고양이가 소음에 깨워진 수동 관계이므로 was 뒤에 과거분사를 쓴다."}],
    "고양이가 자고 있던 능동 관계라 sleeping이 명사를 꾸미고, 고양이가 소음에 깨워졌으므로 was woken up의 수동태가 된다.")
f71("F", "The girl <u>sit</u> next to me was <u>invite</u> to the party.", ["sat — invited", "sitting — inviting", "sits — invited", "sat — inviting", "sitting — invited"], 5, ["sitting", "invited"],
    [{"sat": "소녀가 직접 앉아 있는 능동 관계라 과거형(과거분사)은 맞지 않는다.", "sits": "문장의 동사는 was invited이므로 명사를 꾸미는 자리에 동사 sits를 쓸 수 없다."},
     {"inviting": "소녀가 파티에 초대받은 수동 관계이므로 was 뒤에 과거분사를 쓴다."}],
    "소녀가 앉아 있는 능동 관계라 sitting이 명사를 꾸미고, 소녀가 초대받았으므로 was invited의 수동태가 된다.")

# 2-72 감정 분사 짝: 구별 기준을 알려 주던 발문을 원문항대로
for t, v in {"B": "shock", "C": "amaze", "D": "bore", "E": "frighten", "F": "tire"}.items():
    ex = V(2, 72, t)["expl"]
    F(2, 72, t, st=f"다음 각 빈칸에 알맞은 {v}의 형태를 바르게 짝지은 것을 고르시오.",
      xr=[x for x in [("발문의 역할을 따른다", "문장 속 역할을 따진다"), ("첫째에 지정된", "첫째 빈칸의"), ("둘째에 지정된", "둘째 빈칸의")] if x[0] in ex],
      s=f"발문이 ‘첫째는 사람이 느끼는 감정, 둘째는 감정을 일으키는 원인’이라고 -ed/-ing 구별 기준을 알려 주어, 원문항 발문(각 빈칸에 알맞은 {v}의 형태)으로 되돌렸다. 보기와 정답은 그대로다.")

# 2-73 분사 수식 오류: 짝 문장을 없애고 유형마다 오답을 새로
R73 = "명사가 직접 하는 동작은 현재분사로, 동작을 받거나 그 결과 상태에 있는 명사는 과거분사로 꾸민다."
S73 = "틀린 문장이 같은 내용의 옳은 문장과 짝을 이뤄(sending ↔ sent 등) 대비 단서가 되었고, 오답 네 문장이 유형마다 같았다. 짝 문장을 없애고 유형마다 오답을 새로 썼다."
def ACT(nn, mean): return f"현재분사: 명사({nn})가 직접 {mean} 능동 관계라 알맞으므로"
def PAS(nn, mean): return f"과거분사: 명사({nn})가 {mean} 수동 관계라 알맞으므로"
def WRONG(nn, mean, fix): return f"명사({nn})는 {mean} 대상이므로 과거분사({fix})로 써야 한다. 어색한 부분이므로"
mk(2, 73, "B", [("The documents <u>sending</u> yesterday have arrived.", WRONG("The documents", "보내진", "sent")), ("The bicycle <u>stolen</u> last week was found.", PAS("The bicycle", "도난당한")),
                ("The player <u>injured</u> during the game left early.", PAS("The player", "다친")), ("The cake <u>baked</u> by Mina smells great.", PAS("The cake", "구워진")),
                ("Look at the dog <u>chasing</u> its tail.", ACT("the dog", "꼬리를 쫓는"))], 1, R73, S73)
mk(2, 73, "C", [("The girl <u>singing</u> on the stage is my cousin.", ACT("The girl", "노래하는")), ("I found a <u>broken</u> vase on the floor.", PAS("vase", "깨진")),
                ("The man <u>talking</u> to Jane is our coach.", ACT("The man", "말하는")), ("The bridge <u>building</u> in 1990 is still strong.", WRONG("The bridge", "지어진", "built")),
                ("Do you know the woman <u>wearing</u> a hat?", ACT("the woman", "모자를 쓴"))], 4, R73, S73)
mk(2, 73, "D", [("The <u>crying</u> baby needs some milk.", ACT("baby", "우는")), ("The letter <u>writing</u> by my grandma made me cry.", WRONG("The letter", "쓰인", "written")),
                ("The students <u>waiting</u> outside look cold.", ACT("The students", "기다리는")), ("We ate some <u>fried</u> rice.", PAS("rice", "볶아진")),
                ("This is a picture <u>painted</u> by Picasso.", PAS("a picture", "그려진"))], 2, R73, S73)
mk(2, 73, "E", [("The man <u>fixing</u> the roof is my uncle.", ACT("The man", "지붕을 고치는")), ("I like the song <u>played</u> on the radio.", PAS("the song", "틀어진")),
                ("There are <u>fallen</u> leaves on the ground.", "과거분사: 이미 떨어진(완료) 상태의 잎을 꾸며 알맞으므로"), ("The boy <u>running</u> fast is my brother.", ACT("The boy", "달리는")),
                ("The window <u>breaking</u> in the storm was replaced.", "창문은 깨진 대상이라 수동의 과거분사 broken을 써야 한다. 어색한 부분이므로")], 5, R73, S73)
mk(2, 73, "F", [("Who is the girl <u>dancing</u> with Tom?", ACT("the girl", "춤추는")), ("He showed me a photo <u>taken</u> in Paris.", PAS("a photo", "찍힌")),
                ("The car <u>parking</u> in front of my house is not mine.", WRONG("The car", "주차된", "parked")), ("The <u>smiling</u> girl waved at me.", ACT("girl", "웃는")),
                ("English is a language <u>spoken</u> all over the world.", PAS("a language", "쓰이는"))], 3, R73, S73)

# 2-74 현수 분사구문: 원문항 발문, 옳은 분사구문 넷 + 의미상 주어가 어긋난 문장 하나
R74 = "별도의 의미상 주어를 쓰지 않은 분사구문은 주절의 주어가 그 동작·상태의 주체이다. 주체가 다르면 접속사와 주어를 갖춘 절로 풀어 쓴다."
S74 = "원문항은 옳은 분사구문 넷 가운데 의미상 주어가 어긋난 문장 하나를 찾는데, 변형은 틀린 문장 넷 가운데 옳은 하나를 고르게 뒤집혔고 발문이 판단 규칙을 알려 주었다. 원문항 발문(어법상 어색한 것)으로 되돌리고, 옳은 분사구문 넷과 의미상 주어가 어긋난 문장 하나로 다시 썼다."
ST74 = "다음 문장 중 어법상 어색한 것을 고르시오."
def OKS(subj): return f"분사구문의 주체가 주절 주어({subj})와 같아 알맞으므로"
def OKP(subj, rel): return f"분사구문의 주체가 주절 주어({subj})와 같고, {rel} 수동 관계라 알맞으므로"
def DANG(subj, fix): return f"주절 주어({subj})가 그 동작을 할 수 없어 의미상 주어가 어긋난다({fix}). 어색한 문장이므로"
mk(2, 74, "B", [("Feeling tired, Mina went to bed early.", OKS("Mina")), ("Hearing the news, he started to cry.", OKS("he")), ("Not knowing what to do, I called my mom.", OKS("I")),
                ("Opening the box, a surprise appeared.", DANG("a surprise", "When I opened the box, a surprise appeared.")), ("Left alone, the baby began to cry.", OKP("the baby", "아기가 혼자 남겨진"))], 4, R74, S74, st=ST74)
mk(2, 74, "C", [("Having finished the report, Joon sent it to his manager.", OKS("Joon")), ("Looking at the map, the road seemed confusing.", DANG("the road", "When I looked at the map, the road seemed confusing.")),
                ("Seen from the hill, the town looks beautiful.", OKP("the town", "마을이 언덕에서 보이는")), ("Smiling brightly, she welcomed the guests.", OKS("she")), ("Tired of waiting, we went home.", OKS("we"))], 2, R74, S74, st=ST74)
mk(2, 74, "D", [("Not knowing the answer, Amy remained silent.", OKS("Amy")), ("Made in Italy, this bag is very expensive.", OKP("this bag", "가방이 이탈리아에서 만들어진")), ("Walking along the river, I saw a turtle.", OKS("I")),
                ("Surprised at the price, he didn't buy the shoes.", OKS("he")), ("Crossing the bridge, the temperature dropped.", DANG("the temperature", "As we crossed the bridge, the temperature dropped."))], 5, R74, S74, st=ST74)
mk(2, 74, "E", [("Reading the book, the ending was surprising.", DANG("the ending", "When I read the book, the ending was surprising.")), ("Surprised by the news, the students asked many questions.", OKS("the students")),
                ("Having lost his key, Tom couldn't get in.", OKS("Tom")), ("Turning left, you will find the bank.", OKS("you")), ("Listening to music, she did her homework.", OKS("she"))], 1, R74, S74, st=ST74)
mk(2, 74, "F", [("Born in Canada, Eric speaks both English and French.", OKS("Eric")), ("Running to school, I dropped my phone.", OKS("I")),
                ("Driving through the tunnel, the lights looked dim.", DANG("the lights", "As we drove through the tunnel, the lights looked dim.")), ("Covered with snow, the mountain looked white.", OKP("the mountain", "산이 눈에 덮인")),
                ("Feeling hungry, we ordered pizza.", OKS("we"))], 3, R74, S74, st=ST74)

# 2-75 글 속 분사 밑줄 다섯 곳: 원문항 형식
ST75 = "R"  # 고친 원문항 발문(선다형)
R75 = "분사구문과 명사를 꾸미는 분사는 의미상 주어(꾸밈을 받는 명사)와의 관계가 능동이면 현재분사, 수동이면 과거분사를 쓴다. 앞선 일이 끝난 뒤를 나타내면 Having + 과거분사를 쓴다."
S75 = "원문항은 짧은 글에 밑줄 친 분사 다섯 곳을 두고 틀린 곳을 찾는데, 변형은 한 문장을 다섯 부분으로 나눈 형식이었고 밑줄도 없었다(B·C는 오류가 분사가 아닌 형용사·부사 구별이었다). 원문항 발문과 형식(짧은 글 + 분사 밑줄 다섯 곳)으로 다시 썼다."
def f75(t, p, items, a):
    mk(2, 75, t, items, a, R75, S75, st=ST75, p=p, k=f"{items[a-1][1].split('. 어법상')[0]}.")
f75("B", "Yesterday, Mina went hiking with her family. ①<u>Climbing</u> up the mountain, she saw many birds ②<u>flying</u> above the trees. At the top, there was a small bench ③<u>made</u> of wood. ④<u>Feeling</u> tired, she sat on it for a while. ⑤<u>Refreshing</u> by the cool wind, she walked down happily.",
    [("Climbing", "Climbing: 주어(she)가 직접 오르는 능동 관계라 알맞으므로"), ("flying", "flying: 새들이 직접 나는 능동 관계라 알맞으므로"), ("made", "made: 벤치가 나무로 만들어진 수동 관계라 알맞으므로"),
     ("Feeling", "Feeling: 주어(she)가 피곤함을 느끼는 능동 관계라 알맞으므로"), ("Refreshing", "Refreshing: 주어(she)가 시원한 바람에 기운을 되찾게 된 수동 관계이므로 Refreshed로 고쳐야 한다. 어법상 틀린 부분이므로")], 5)
f75("C", "Last Saturday, Tom visited a flea market. ①<u>Walked</u> around the stalls, he found an old camera. The camera, ②<u>made</u> in Germany, looked great. The seller ③<u>standing</u> behind the table smiled at him. ④<u>Surprised</u> at the low price, Tom bought it right away. ⑤<u>Holding</u> the camera, he took pictures all the way home.",
    [("Walked", "Walked: 주어(he)가 직접 걷는 능동 관계이므로 Walking으로 고쳐야 한다. 어법상 틀린 부분이므로"), ("made", "made: 카메라가 독일에서 만들어진 수동 관계라 알맞으므로"), ("standing", "standing: 판매자가 직접 서 있는 능동 관계라 알맞으므로"),
     ("Surprised", "Surprised: 주어(Tom)가 싼 가격에 놀라게 된 수동 관계라 알맞으므로"), ("Holding", "Holding: 주어(he)가 직접 카메라를 드는 능동 관계라 알맞으므로")], 1)
f75("D", "Jane entered a small café. The smell of freshly ①<u>baked</u> bread filled the room. She saw a cat ②<u>sleeping</u> by the window. ③<u>Sitting</u> at a table, she ordered hot chocolate. The drink ④<u>serving</u> in a big cup was sweet. ⑤<u>Satisfied</u> with the café, she decided to come back.",
    [("baked", "baked: 빵이 구워진 수동 관계라 알맞으므로"), ("sleeping", "sleeping: 고양이가 직접 자는 능동 관계라 알맞으므로"), ("Sitting", "Sitting: 주어(she)가 직접 앉는 능동 관계라 알맞으므로"),
     ("serving", "serving: 음료가 큰 컵에 담겨 나온 수동 관계이므로 served로 고쳐야 한다. 어법상 틀린 부분이므로"), ("Satisfied", "Satisfied: 주어(she)가 카페에 만족하게 된 수동 관계라 알맞으므로")], 4)
f75("E", "On a rainy day, Leo stayed home. ①<u>Bored</u> with TV, he started reading a novel. The story ②<u>written</u> by a young author was exciting. ③<u>Turned</u> the pages quickly, he forgot about the time. He heard his mom ④<u>calling</u> him for dinner. ⑤<u>Closing</u> the book, he went to the kitchen.",
    [("Bored", "Bored: 주어(he)가 TV에 싫증 난 수동 관계라 알맞으므로"), ("written", "written: 이야기가 작가에게 쓰인 수동 관계라 알맞으므로"),
     ("Turned", "Turned: 주어(he)가 직접 책장을 넘기는 능동 관계이므로 Turning으로 고쳐야 한다. 어법상 틀린 부분이므로"), ("calling", "calling: 엄마가 직접 부르는 능동 관계라 알맞으므로"), ("Closing", "Closing: 주어(he)가 직접 책을 덮는 능동 관계라 알맞으므로")], 3)
f75("F", "Sora went to a concert with her friends. ①<u>Excited</u> about the show, they arrived early. A band ②<u>played</u> rock music came on stage. ③<u>Surrounded</u> by cheering fans, Sora sang along. ④<u>Having</u> enjoyed the show, they went home. On the way, she found a ticket ⑤<u>dropped</u> on the street.",
    [("Excited", "Excited: 주어(they)가 공연에 들뜬 수동 관계라 알맞으므로"), ("played", "played: 밴드가 직접 연주하는 능동 관계이므로 playing으로 고쳐야 한다(문장의 동사는 came). 어법상 틀린 부분이므로"),
     ("Surrounded", "Surrounded: 주어(Sora)가 팬들에게 둘러싸인 수동 관계라 알맞으므로"), ("Having", "Having: 공연을 즐긴 일이 먼저 끝났으므로 Having + 과거분사가 알맞으므로"), ("dropped", "dropped: 표가 떨어뜨려진 수동 관계라 알맞으므로")], 2)

# 2-76 과거분사 수식: 답을 알려 주던 발문을 원문항대로(우리말 뜻 + 괄호 속 동사)
ST76 = "다음 우리말에 맞게 주어진 단어의 알맞은 형태를 고르시오."
S76 = "발문이 ‘명사가 행위의 대상이 되는 수동 관계를 나타내도록’이라고 정답을 알려 주어, 원문항처럼 우리말 뜻과 괄호 속 동사를 주는 발문·형식으로 되돌렸다. 보기와 정답은 그대로다."
for t, (ko, en) in {"B": ("나는 위원회가 작성한 보고서를 읽었다.", "I read the report ______ by the committee. (write)"),
                     "C": ("경찰은 어젯밤 도난당한 자전거를 찾았다.", "The police found the bike ______ last night. (steal)"),
                     "D": ("부상당한 선수가 경기장을 떠났다.", "The ______ player left the field. (injure)"),
                     "E": ("오늘 아침에 구운 빵에서 좋은 냄새가 난다.", "The bread ______ this morning smells wonderful. (bake)"),
                     "F": ("그녀는 책상 밑에서 발견된 열쇠를 돌려주었다.", "She returned the key ______ under the desk. (find)")}.items():
    ex = V(2, 76, t)["expl"]
    xr76 = [x for x in [("이 문항은 명사가 동작을 하는 능동 관계가 아니라 동작을 당한 상태를 요구하므로", "명사가 동작을 하는 능동 관계가 아니라 동작을 당한 상태이므로"),
                        ("다 구워졌다는 조건에 맞지 않는다", "우리말(오늘 아침에 구운 빵)의 뜻에 맞지 않는다"), ("이미 구워졌다는 조건과 다르다", "이미 구운 빵이라는 우리말의 뜻과 다르다")] if x[0] in ex]
    F(2, 76, t, st=ST76, p=f"주어진 문장: {ko}\n{en}", xr=xr76, s=S76 if t != "E" else "발문이 원문항과 달라 원문항 발문으로 되돌리고, 원문항처럼 괄호 속 동사원형(bake)을 넣었다. 보기와 정답은 그대로다.")

# 2-77 분사구문 전환: 물음표·없는 형태 오답을 의미·형태 오류로
R77 = "부사절의 주어가 주절과 같으면 접속사와 주어를 생략하고 동사를 분사로 바꾼다. 부정어(not)는 분사 앞에 두고, 수동이면 과거분사, 주절보다 앞선 일이면 Having + 과거분사를 쓰며, 접속사의 뜻(이유·양보)을 바꾸지 않는다."
S77 = "정답 끝에 물음표만 붙인 오답과 ‘Feeled, Haved, Beed, nothed’처럼 존재하지 않는 형태가 섞여 형식만으로 지워졌다. 원문항처럼 의미(접속사·부정)와 형태(능동·수동, 완료) 오류로 오답을 새로 썼다."
OK77 = "주어가 같아 접속사와 주어를 생략하고 동사를 분사로 바꾼 알맞은 분사구문이다."
mk(2, 77, "B", [("Felt sick, she stayed home.", "Felt: 능동의 분사구문은 현재분사(Feeling)로 시작하므로"), ("Though feeling sick, she stayed home.", "Though: ‘~에도 불구하고’라는 양보의 뜻이 되어 원래의 이유(Because)와 뜻이 달라지므로"),
                ("Feeling sick, she stayed home.", OK77 + " 따라서"), ("Being felt sick, she stayed home.", "Being felt: 그녀가 느끼는 능동 관계인데 수동 형태를 써서 맞지 않으므로"),
                ("Not feeling sick, she stayed home.", "Not: 부정어가 붙어 ‘아프지 않아서’라는 반대 뜻이 되므로")], 3, R77, S77)
mk(2, 77, "C", [("Not knowing the answer, Tom remained silent.", OK77 + " 부정어(not)도 분사 앞에 바르게 두었다. 따라서"), ("Knowing not the answer, Tom remained silent.", "Knowing not: 부정어는 분사 앞에 두어야 하므로"),
                ("Knowing the answer, Tom remained silent.", "부정어가 빠져 ‘답을 알아서’라는 반대 뜻이 되므로"), ("Not known the answer, Tom remained silent.", "Not known: Tom이 답을 아는 능동 관계인데 과거분사를 써서 맞지 않으므로"),
                ("Unless knowing the answer, Tom remained silent.", "Unless: ‘~하지 않는다면’이라는 조건의 뜻이 되어 원래의 이유(As)와 뜻이 달라지므로")], 1, R77, S77)
mk(2, 77, "D", [("Surprising by the news, we said nothing.", "Surprising: 우리가 소식에 놀라게 된 수동 관계이므로 과거분사(Surprised)를 써야 하므로"), ("Surprised the news, we said nothing.", "by가 빠져 소식이 놀라게 한 원인이라는 관계가 드러나지 않으므로"),
                ("Although surprised by the news, we said nothing.", "Although: 양보의 뜻이 되어 원래의 이유(Because)와 뜻이 달라지므로"), ("Having surprised by the news, we said nothing.", "Having surprised: 능동의 완료형이라 ‘우리가 놀라게 했다’는 뜻이 되어 맞지 않으므로"),
                ("Surprised by the news, we said nothing.", OK77 + " 수동이므로 Being을 생략한 과거분사로 시작했다. 따라서")], 5, R77, S77)
mk(2, 77, "E", [("Having finishing her work, Jane left early.", "Having 뒤에는 과거분사(finished)를 써야 하므로"), ("Having finished her work, Jane left early.", OK77 + " 일을 끝낸 것이 떠난 것보다 앞서 Having + 과거분사를 썼다. 따라서"),
                ("Being finished her work, Jane left early.", "Being finished: 그녀가 일을 끝낸 능동 관계인데 수동 형태를 써서 맞지 않으므로"), ("Having been finished her work, Jane left early.", "Having been finished: 수동의 완료형이라 능동 관계와 맞지 않으므로"),
                ("Having not finished her work, Jane left early.", "not이 붙어 ‘일을 끝내지 못해서’라는 반대 뜻이 되고, 부정어의 위치도 Having 앞이어야 하므로")], 2, R77, S77)
mk(2, 77, "F", [("Been tired, he went to bed immediately.", "Been: 분사구문은 Being(또는 Having been)으로 시작하며 Been만으로는 쓸 수 없으므로"), ("Being tiring, he went to bed immediately.", "tiring: 그가 피곤함을 느끼는 상태이므로 tired를 써야 하므로"),
                ("Though being tired, he went to bed immediately.", "Though: 양보의 뜻이 되어 원래의 이유(Because)와 뜻이 달라지므로"), ("Being tired, he went to bed immediately.", OK77 + " 따라서"),
                ("Having tired, he went to bed immediately.", "Having tired: ‘누군가를 피곤하게 했다’는 능동의 완료형이 되어 맞지 않으므로")], 4, R77, S77)

# 2-79 D: -ed도 가능해 괄호에 기대던 (B)를 바꾸고 괄호 삭제
c = ["hear - bored - sitting", "heard - bored - sat", "hear - boring - sitting", "hear - boring - sat", "heard - boring - sitting"]
F(2, 79, "D", st="다음 빈칸에 들어갈 말로 알맞게 짝지어진 것을 고르시오.", p="A: Did you (A)_____(hear) the speech?\nB: Yes. But it was so (B)______(bore) that the students (C)______(sit) in the back fell asleep.",
  c=c, a=3, r="Did 의문문의 본동사는 원형이다. 감정을 일으키는 쪽에는 -ing, 느끼는 쪽에는 -ed를 쓰고, 명사를 꾸미는 분사는 그 명사와의 능동·수동 관계로 정한다.",
  n=pair(c, 3, ["hear", "boring", "sitting"], [{"heard": "Did 뒤에는 동사원형을 쓴다."}, {"bored": "연설이 지루함을 일으키는 쪽이므로 -ing를 쓴다."}, {"sat": "학생들이 직접 앉아 있는 능동 관계라 현재분사로 꾸미며, 문장의 동사(fell)가 따로 있다."}]),
  k="Did 뒤 원형 hear, 연설이 지루함을 일으키므로 boring, 학생들이 앉아 있는 능동 관계이므로 sitting이다.",
  s="발문 괄호가 (B)의 뜻(의욕을 불어넣는)을 알려 주었고, 괄호가 없으면 ‘It was inspired’도 가능해 조건에 기댔다. (B)를 -ed가 성립하지 않는 ‘so boring that …’ 문장으로 바꾸고 괄호를 지워 다른 유형과 같은 발문으로 맞췄다. 정답 위치 ③.")

# 2-80 감정 분사 설명: 설명 다섯 개와 틀린 설명을 유형마다 새로
R80 = "감정 동사에서 나온 -ing 형용사는 감정을 일으키는 성질을, -ed 형용사는 감정을 느끼는 상태를 나타낸다. 사람도 감정을 일으키는 쪽이면 -ing를 쓸 수 있다."
S80 = "옳은 설명 네 개(태호·수아·준·민지)가 B와 똑같았다. 유형마다 학생 이름과 설명 다섯 개를 새로 쓰고, 틀린 설명의 오개념도 유형마다 다르게 했다."
talk(2, 80, "B", [("하람: (A)는 강의가 듣는 사람을 지루하게 만드는 성질을 가졌다는 뜻이야.", "(A)의 boring은 지루함을 일으키는 성질이다."),
                  ("도현: 사람 주어에는 항상 -ed만 쓰므로 ‘The teacher was boring.’은 틀린 문장이야.", "사람도 지루함을 일으키는 쪽이면 boring을 쓸 수 있으므로 ‘The teacher was boring.’은 옳은 문장이다."),
                  ("가은: (B)는 학생들이 지루함을 느낀 상태였다는 뜻이야.", "(B)의 bored는 느끼는 상태이다."),
                  ("지안: (A)를 ‘The lecture was bored.’로 바꾸면 강의가 지루함을 느꼈다는 어색한 뜻이 돼.", "강의는 감정을 느낄 수 없으므로 bored를 쓰면 어색하다."),
                  ("로운: 감정을 일으키는 쪽에는 -ing, 감정을 느끼는 쪽에는 -ed를 써.", "감정 분사의 기본 구별이다.")], 2, R80,
     "틀린 설명(서윤: (A)는 진행 중, (B)는 끝남)이 원문항 정답과 이름·내용까지 같았다. 학생 이름과 설명을 새로 쓰고, 틀린 설명을 ‘사람 주어에는 항상 -ed’라는 다른 오개념으로 바꿨다.")
talk(2, 80, "C", [("민호: (A)의 surprising은 소식이 놀라는 감정을 느낀다는 뜻이야.", "surprising은 소식이 사람을 놀라게 하는 성질을 나타낸다."), ("서진: (B)는 미나가 놀란 상태였다는 뜻이야.", "(B)의 surprised는 느끼는 상태이다."),
                  ("윤아: (A)는 소식이 사람들을 놀라게 하는 성질을 지녔다는 뜻이야.", "(A)의 surprising은 놀라움을 일으키는 성질이다."), ("태민: (B)를 ‘Mina was surprising.’으로 바꾸면 미나가 남을 놀라게 하는 사람이라는 뜻이 돼.", "사람도 놀라움을 일으키는 쪽이면 -ing를 쓴다."),
                  ("소율: surprise는 ‘놀라게 하다’라는 뜻이라 -ing는 놀라게 하는 쪽, -ed는 놀란 쪽을 나타내.", "감정 동사의 뜻에서 나온 구별이다.")], 1, R80, S80)
talk(2, 80, "D", [("예준: (A)는 여행이 사람을 피곤하게 만들었다는 뜻이야.", "(A)의 tiring은 피곤함을 일으키는 성질이다."), ("채아: (B)는 우리가 피곤함을 느꼈다는 뜻이야.", "(B)의 tired는 느끼는 상태이다."),
                  ("하율: tiring과 tired는 ‘피곤하게 하다’라는 뜻의 동사(tire)에서 나온 분사야.", "두 형용사 모두 tire에서 나왔다."), ("시안: ‘a tiring day’는 사람을 피곤하게 만든 하루라는 뜻이야.", "-ing가 명사를 꾸며 피곤함을 일으키는 성질을 나타낸다."),
                  ("지수: (B)의 tired는 우리가 다른 사람을 피곤하게 만든다는 뜻이야.", "tired는 우리가 피곤함을 느끼는 상태이다.")], 5, R80, S80)
talk(2, 80, "E", [("리나: (A)는 이야기가 무서움을 느끼게 하는 성질을 가졌다는 뜻이야.", "(A)의 frightening은 두려움을 일으키는 성질이다."), ("주원: (B)는 아이들이 무서워한 상태라는 뜻이야.", "(B)의 frightened는 느끼는 상태이다."),
                  ("유리: (B)를 ‘The children were frightening.’으로 바꿔도 뜻이 같아.", "frightening으로 바꾸면 아이들이 남을 무섭게 한다는 전혀 다른 뜻이 된다."),
                  ("다인: frightened는 아이들이 이야기 때문에 겁을 먹게 된 수동의 관계를 나타내.", "-ed는 감정을 받는 수동의 관계이다."), ("은우: ‘a frightening movie’는 무서운 영화, ‘frightened people’은 겁먹은 사람들이야.", "-ing와 -ed가 명사를 꾸밀 때의 차이이다.")], 3, R80, S80)
talk(2, 80, "F", [("태윤: (A)는 결과가 실망을 안겨 주었다는 뜻이야.", "(A)의 disappointing은 실망을 일으키는 성질이다."), ("서아: (B)는 톰이 실망한 상태였다는 뜻이야.", "(B)의 disappointed는 느끼는 상태이다."),
                  ("하은: disappoint는 ‘실망시키다’라는 뜻이라 -ing는 실망을 주는 쪽을 꾸며.", "감정 동사의 뜻에서 나온 구별이다."), ("준서: ‘실망스러운 결과’를 영어로 하면 ‘a disappointed result’야.", "실망을 일으키는 결과이므로 a disappointing result이다."),
                  ("우진: (B)를 ‘Tom was disappointing.’으로 바꾸면 톰이 남을 실망시켰다는 뜻이 돼.", "사람도 실망을 일으키는 쪽이면 -ing를 쓴다.")], 4, R80, S80)
