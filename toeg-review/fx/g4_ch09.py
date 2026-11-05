# 4급 CH9 전치사·접속사 (81~90) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def slotnote(ch, good, why, labs=("첫째", "둘째", "셋째"), sep=" - "):
    xs = [x.strip() for x in ch.split(sep)]; gs = [x.strip() for x in good.split(sep)]
    if xs == gs: return "모든 빈칸에 알맞은 말을 골랐으므로"
    bits = [f"{labs[i]} 빈칸 {x}: {w}" for i, (x, g, w) in enumerate(zip(xs, gs, why)) if x != g]
    return ", ".join(bits) + ". 따라서"

# 4-81 C: 원문항과 같던 제시문을 새로
mk(4, 81, "C", [("during", "during은 ‘~ 동안’이라 시각 앞에 쓰지 않으므로"), ("for", "for는 기간의 길이에 쓰므로"), ("on", "on은 요일·날짜에 쓰므로"), ("in", "in은 월·연도·계절에 쓰므로"), ("at", "정오(noon) 같은 시각에는 at을 쓰므로")], 5,
   "정확한 시각과 정오·자정에는 at, 요일·날짜에는 on, 월·연도·계절에는 in을 쓴다.", "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘그 가게는 정오에 문을 연다. / The store opens ___ noon.’으로 바꿨다.",
   p="그 가게는 정오에 문을 연다.\nThe store opens _____ noon.", okdup=True)

# 4-82 밑줄 친 장소 전치사가 잘못된 것: 원문항 발문과 밑줄, 짝 없이 유형마다 새로
ST482 = "다음 밑줄 친 부분이 잘못된 것을 고르시오."
R482 = "장소는 at(한 지점·at home·at school), on(표면·층·벽·천장), in(공간 안·도시·나라·강), under(아래), next to(옆), between(둘 사이), across from(맞은편), in front of(앞)로 나타낸다."
S482 = "발문이 ‘시간·장소의 기본 관계에 맞지 않는 전치사’라고 볼 곳을 알려 주었고 밑줄이 사라졌으며, 정답 문장과 같은 문장의 옳은 형태가 함께 있어 대비 단서가 되고 오답이 유형마다 같았다. 원문항 발문과 밑줄로 되돌리고 원문항처럼 장소 전치사 문장으로 유형마다 새로 썼다."
OK82 = "위치 관계에 맞는 전치사를 바르게 썼으므로"
def f482(t, items, a, s=S482):
    mk(4, 82, t, [(x, w or OK82) for x, w in items], a, R482, s, st=ST482)
f482("B", [("We meet <u>on</u> Monday.", "요일 앞에 on을 바르게 썼으므로"), ("Jane was born <u>in</u> May 3rd.", "구체적인 날짜에는 on을 써야 하므로"), ("Tom lives <u>in</u> Seoul.", "도시 앞에 in을 바르게 썼으므로"),
           ("School starts <u>at</u> 9.", "시각 앞에 at을 바르게 썼으므로"), ("The bakery is <u>on</u> the second floor.", "층 앞에 on을 바르게 썼으므로")], 2,
     "발문이 바뀌고 밑줄이 사라졌다. 원문항 발문과 밑줄로 되돌렸다. 보기와 정답은 그대로다.")
f482("C", [("The children are <u>in</u> the classroom.", ""), ("There is a spider <u>on</u> the ceiling.", ""), ("My dad is <u>in</u> home now.", "‘집에’는 at home으로 써야 하므로"), ("The clock is <u>on</u> the wall.", ""), ("Tom is waiting <u>at</u> the bus stop.", "")], 3,
     S482 + " 정답(Her house is at the third floor.)이 원문항과 같아 새로 썼다.")
f482("D", [("The dog is sleeping <u>under</u> the table.", ""), ("We live <u>at</u> Busan.", "도시 앞에는 in을 써야 하므로"), ("My keys are <u>in</u> my bag.", ""), ("She is standing <u>next to</u> me.", ""), ("The cat is <u>on</u> the sofa.", "")], 2)
f482("E", [("The picture is <u>on</u> the wall.", ""), ("Jane is <u>at</u> school now.", ""), ("The milk is <u>in</u> the fridge.", ""), ("The post office is <u>between</u> the bank and the park.", ""), ("There are many fish <u>on</u> the river.", "강물 속은 in the river로 써야 하므로")], 5)
f482("F", [("The bird is sitting <u>on</u> the branch.", ""), ("The bank is <u>across from</u> the school.", ""), ("The kids are playing <u>at</u> the park.", ""), ("There is a big tree <u>in front</u> the house.", "‘~ 앞에’는 in front of로 써야 하므로"), ("My sister is <u>in</u> her room.", "")], 4)

# 4-83 on과 함께 쓰이는 것으로만 묶인 것: 원문항 발문, 유형마다 오답 묶음을 새로
R483 = "요일·날짜·특정한 날(생일, 공휴일)에는 on, 월·계절·연도·아침·오후·저녁에는 in, 시각·정오·자정·밤·식사 시간에는 at을 쓴다."
S483 = "발문이 길어지고 ‘추가 수식어를 넣지 않는다’ 조건이 붙었으며, 오답 묶음이 유형마다 같았다. 원문항 발문으로 되돌리고 유형마다 오답 묶음을 새로 썼다."
ON = "요일·날짜·특정한 날이라 모두 on과 함께 쓰므로"
def f483(t, items, a, s=S483):
    mk(4, 83, t, items, a, R483, s, st="R", okdup=True)
f483("B", [("Tuesday, my birthday, March 3rd", ON), ("the evening, June, spring", "the evening, June, spring은 in과 함께 쓰므로"), ("5 o'clock, noon, night", "시각·정오·밤은 at과 함께 쓰므로"),
           ("2019, summer, the morning", "연도·계절·아침은 in과 함께 쓰므로"), ("bedtime, midnight, December", "bedtime·midnight은 at, December는 in과 함께 쓰므로")], 1,
     "발문이 길어지고 조건이 붙었다. 원문항 발문으로 되돌리고 오답 묶음을 원문항처럼 in·at과 쓰는 말로 새로 썼다.")
f483("C", [("9:30 a.m., sunset, dawn", "시각·해 질 녘·새벽은 at과 함께 쓰므로"), ("Sunday, New Year's Day, April 1st", ON), ("October, 2010, the evening", "월·연도·저녁은 in과 함께 쓰므로"),
           ("the 1990s, March, winter", "연대·월·계절은 in과 함께 쓰므로"), ("lunchtime, 6 p.m., midnight", "식사 시간·시각·자정은 at과 함께 쓰므로")], 2)
f483("D", [("July, the afternoon, 2022", "월·오후·연도는 in과 함께 쓰므로"), ("noon, 3 o'clock, night", "정오·시각·밤은 at과 함께 쓰므로"), ("Friday, Children's Day, June 1st", ON),
           ("spring, September, the 21st century", "계절·월·세기는 in과 함께 쓰므로"), ("dinnertime, sunrise, 10:15", "식사 시간·해 뜰 녘·시각은 at과 함께 쓰므로")], 3)
f483("E", [("midnight, 7 p.m., bedtime", "자정·시각·잘 시간은 at과 함께 쓰므로"), ("the morning, November, autumn", "아침·월·계절은 in과 함께 쓰므로"), ("2008, winter, February", "연도·계절·월은 in과 함께 쓰므로"),
           ("Wednesday, Christmas Day, July 4th", ON), ("night, noon, 4:30", "밤·정오·시각은 at과 함께 쓰므로")], 4)
f483("F", [("the evening, May, summer", "저녁·월·계절은 in과 함께 쓰므로"), ("11 a.m., noon, lunchtime", "시각·정오·점심시간은 at과 함께 쓰므로"), ("2030, spring, January", "연도·계절·월은 in과 함께 쓰므로"),
           ("night, midnight, 8 o'clock", "밤·자정·시각은 at과 함께 쓰므로"), ("Thursday, New Year's Eve, August 15th", ON)], 5)

# 4-84 접속사: 원문항 발문, C는 문장을 새로
S484 = "발문이 ‘제시된 우리말의 논리 관계를 직접 나타내는 접속사로’로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
for t in "BDEF": F(4, 84, t, st="R", s=S484)
mk(4, 84, "C", [("and", "두 가지 일을 차례로 이어 ‘~하고’의 뜻을 나타내므로"), ("because", "because를 쓰면 ‘TV를 봤기 때문에 숙제를 끝냈다’가 되어 뜻이 맞지 않으므로"), ("or", "or는 선택이라 뜻이 맞지 않으므로"),
                ("but", "but은 대조라 뜻이 맞지 않으므로"), ("so", "so는 ‘그래서’라는 결과라 ‘끝내고’의 뜻과 맞지 않으므로")], 1,
   "and는 연결(~하고), so는 결과(그래서), because는 이유(~ 때문에), but은 대조, or는 선택을 나타낸다.", "제시문과 정답(so)이 원문항과 똑같았다. 제시문을 ‘나는 숙제를 끝내고 TV를 봤다.’로 바꿔 정답을 and로 하고 원문항 발문으로 되돌렸다.",
   st="R", p="나는 숙제를 끝내고 TV를 봤다.\nI finished my homework, _____ I watched TV.", okdup=True)

# 4-85 장소 전치사 옳은 짝: 원문항 형식(ⓐ~ⓓ, 두 개의 짝), on/in/at 혼동 오류
ST485 = "다음 중 장소 전치사의 쓰임이 어법상 옳은 문장으로만 짝지어진 것은?"
R485 = "장소는 on(표면·벽), in(공간 안·도시·강·하늘·물속), at(한 지점·at home·at school·at the gate), under(아래), between(둘 사이)으로 나타낸다."
S485 = "원문항은 네 문장 중 옳은 두 개의 짝을 고르는데, 변형은 ‘빠짐없이 모두’ 고르는 형식(‘해당 없음’ 포함)으로 바뀌었고 기호도 a~d로 바뀌었으며, 틀린 문장이 ‘under of’, ‘on home’처럼 쉽게 드러났고 정답도 유형마다 같았다. 원문항 발문과 형식(ⓐ~ⓓ, 두 개의 짝)으로 되돌리고 오류를 on/in/at 혼동으로 바꿨다."
def f485(t, lines, judge, ok, c, s=S485):
    a = c.index(ok) + 1
    F(4, 85, t, st=ST485, p="\n".join(lines), c=c, a=a, r=R485, pre=["문장별 판정: " + j for j in judge], k=f"장소 전치사가 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), okdup=True, s=s + ipos(a))
REF85 = ["ⓐ, ⓑ", "ⓐ, ⓓ", "ⓑ, ⓒ", "ⓑ, ⓓ", "ⓒ, ⓓ"]
f485("B", ["ⓐ The cat is sleeping on the sofa.", "ⓑ The book is in the box.", "ⓒ There are many stars on the sky.", "ⓓ Tom lives on Seoul."],
     ["ⓐ O. 소파 위에는 on을 쓴다.", "ⓑ O. 상자 안에는 in을 쓴다.", "ⓒ X. 하늘에는 in the sky로 쓴다.", "ⓓ X. 도시에는 in을 쓴다."], "ⓐ, ⓑ", REF85)
f485("C", ["ⓐ My mom is in the kitchen.", "ⓑ We had lunch on the restaurant.", "ⓒ The cat is under the table.", "ⓓ The kids are swimming on the pool."],
     ["ⓐ O. 부엌 안에는 in을 쓴다.", "ⓑ X. 식당 안이나 식당에서는 in(at) the restaurant로 쓴다.", "ⓒ O. 탁자 아래에는 under를 쓴다.", "ⓓ X. 수영장 물속은 in the pool로 쓴다."], "ⓐ, ⓒ",
     ["ⓐ, ⓑ", "ⓐ, ⓒ", "ⓑ, ⓒ", "ⓑ, ⓓ", "ⓒ, ⓓ"], S485 + " ⓐ가 원문항 문장과 같고 정답 조합도 같아 문장을 새로 썼다.")
f485("D", ["ⓐ Jane is on home.", "ⓑ The bag is between the two desks.", "ⓒ The fish are in the river.", "ⓓ He is waiting on the door."],
     ["ⓐ X. ‘집에’는 at home으로 쓴다.", "ⓑ O. 둘 사이에는 between을 쓴다.", "ⓒ O. 강물 속에는 in을 쓴다.", "ⓓ X. 문 앞 한 지점은 at the door로 쓴다."], "ⓑ, ⓒ", REF85)
f485("E", ["ⓐ The dog is next of the door.", "ⓑ The book is on the desk.", "ⓒ Tom lives at Seoul.", "ⓓ The shoes are under the bed."],
     ["ⓐ X. ‘~ 옆에’는 next to로 쓴다.", "ⓑ O. 책상 표면에는 on을 쓴다.", "ⓒ X. 도시에는 in을 쓴다.", "ⓓ O. 침대 아래에는 under를 쓴다."], "ⓑ, ⓓ", REF85)
f485("F", ["ⓐ The cat is in front to the box.", "ⓑ The boy is swimming on the sea.", "ⓒ A bird is sitting on the roof.", "ⓓ Tom is at school."],
     ["ⓐ X. ‘~ 앞에’는 in front of로 쓴다.", "ⓑ X. 바닷물 속은 in the sea로 쓴다.", "ⓒ O. 지붕 위에는 on을 쓴다.", "ⓓ O. ‘학교에’는 at school로 쓴다."], "ⓒ, ⓓ", REF85)

# 4-86 위치 전치사: 원문항 발문, C는 상황을 새로
S486 = "발문이 ‘우리말 상황의 위치 관계를 정확히 나타내는 전치사’로 바뀌었고 영어 문장 앞의 화살표(→)가 빠졌다. 원문항 발문과 화살표로 되돌렸다. 보기와 정답은 그대로다."
for t in "BDEF": F(4, 86, t, st="R", p=V(4, 86, t)["passage"].replace("\n", "\n→ ", 1), xr=[x for x in [("이 문항의 ", ""), ("전치사는 우리말이 지정한 위치 관계와 맞추어 선택한다.", "전치사는 우리말이 나타내는 위치 관계에 맞추어 고른다.")] if x[0] in V(4, 86, t)["expl"]], s=S486)
mk(4, 86, "C", [("on", "on은 ‘~ 위에’라 뜻이 맞지 않으므로"), ("behind", "‘~ 뒤에’는 behind로 나타내므로"), ("between", "between은 ‘둘 사이에’라 뜻이 맞지 않으므로"), ("in", "in은 ‘~ 안에’라 뜻이 맞지 않으므로"), ("across", "across는 ‘가로질러’라 뜻이 맞지 않으므로")], 2,
   "위치는 on(위), in(안), under(아래), behind(뒤), in front of(앞), between(둘 사이), next to(옆)로 나타낸다.", "제시문과 정답(in)이 원문항과 똑같았다. 상황을 ‘고양이가 소파 뒤에 있다.’로 바꿔 정답을 behind로 했다.",
   st="R", p="고양이가 소파 뒤에 있다.\n→ The cat is ________ the sofa.", okdup=True)

# 4-87 for / during / while: C·F를 새로
R487 = "for는 기간의 길이(an hour, two hours), during은 특정한 때(the lesson, the movie, the test) 앞에 쓰고, while은 뒤에 주어 + 동사가 오는 절을 이끈다."
W487 = {"for": "for는 기간의 길이(숫자 + 시간) 앞에 쓴다", "during": "during은 특정한 때를 나타내는 명사 앞에 쓴다", "while": "while은 주어 + 동사가 있는 절 앞에 쓴다"}
def f487(t, p, c, a, need, s):
    mk(4, 87, t, [(x, slotnote(x, c[a-1], [W487[n] + f"(→ {n})" for n in need])) for x in c], a, R487, s, p=p, okdup=True)
f487("C", "I studied English ________ two hours.\nShe cried ________ the sad movie.", ["for - during", "during - for", "while - during", "for - while", "during - during"], 1, ["for", "during"],
     "제시문과 정답(during - for)이 원문항과 똑같았다. 문장을 새로 쓰고 정답 순서를 for - during으로 바꿨다.")
f487("F", "My phone rang ________ I was sleeping.\nNobody talked ________ the test.", ["during - while", "while - during", "for - during", "while - for", "during - for"], 2, ["while", "during"],
     "정답 조합(during - for)이 원문항과 같았다. 문장을 새로 써서 정답 조합을 while - during으로 바꿨다.")

# 4-88 because / so 다른 하나: 원문항 발문, 뜻 설명 삭제, 유형마다 새로
ST488 = "다음 빈칸에 들어갈 말이 나머지 넷과 다른 하나는?"
R488 = "because는 뒤에 이유(~ 때문에)를, so는 뒤에 결과(그래서)를 이끈다."
S488 = "선택지마다 ‘[뜻: …때문에]’, ‘[뜻: … 그래서 …]’를 붙여 놓아 정답이 바로 드러났고 오답이 유형마다 같았으며, 발문에 because·so가 명시되었다. 원문항 발문으로 되돌리고 뜻 설명을 뺐으며 유형마다 새로 썼다. so가 들어가는 문장에만 쉼표를 찍으면 쉼표만 보고 답이 가려지므로 원문항처럼 쉼표 없이 썼다."
BEC = "뒤 절이 앞 일의 이유라 because가 들어가므로"; SO = "뒤 절이 앞 일의 결과라 so가 들어가므로"
def f488(t, items, a, s=S488):
    mk(4, 88, t, [(x, w + (" 나머지와 달라" if i + 1 == a else "")) for i, (x, w) in enumerate(items)], a, R488, s, st=ST488)
f488("B", [("I was happy ________ Tom came to my party.", BEC), ("She was late ________ she missed the bus.", BEC), ("We went home early ________ we were tired.", BEC), ("Mina cried ________ she lost her dog.", BEC),
           ("It was very hot ________ we went swimming.", SO)], 5, "정답 문장(I ate a lot ____ I am full.)이 원문항과 똑같았고 뜻 설명이 정답을 드러냈다. 원문항 발문으로 되돌리고 문장을 새로 썼다.")
f488("C", [("I was tired ________ I went to bed early.", SO), ("It was raining ________ we took a taxi.", SO), ("The store was closed ________ we went home.", SO), ("He studied hard ________ he wanted to pass the test.", BEC),
           ("She was hungry ________ she made some pasta.", SO)], 4, S488 + " so 넷 + because 하나로 짜서 다른 유형과 구성을 달리했다.")
f488("D", [("Tom stayed home ________ he had a cold.", BEC), ("I like her ________ she is kind.", BEC), ("The road was icy ________ we drove slowly.", SO), ("We were happy ________ our team won.", BEC), ("He didn't go out ________ it was too cold.", BEC)], 3)
f488("E", [("The movie was boring ________ I fell asleep.", SO), ("Jane smiled ________ she got a present.", BEC), ("My bag was heavy ________ Dad carried it.", SO), ("I lost my key ________ I couldn't open the door.", SO),
           ("The soup was hot ________ I waited a minute.", SO)], 2, S488 + " so 넷 + because 하나로 짜서 다른 유형과 구성을 달리했다.")
f488("F", [("I had a headache ________ I took some medicine.", SO), ("Mina was sad ________ her friend moved away.", BEC), ("I bought a new pen ________ I lost mine.", BEC), ("We cleaned the room ________ it was dirty.", BEC), ("He was angry ________ we were late.", BEC)], 1)

# 4-89 when의 쓰임: 원문항 발문과 밑줄, 유형마다 새로
ST489 = "다음 중 밑줄 친 'when'의 쓰임이 나머지 넷과 다른 하나는?"
R489 = "접속사 when은 ‘~할 때’라는 시간의 부사절(주어 + 동사)을 이끌고, 의문사 when은 ‘언제’라고 묻는 의문문을 이끈다."
S489 = "밑줄이 사라지고 발문이 바뀌었으며 접속사 when 오답 네 문장이 유형마다 같았다. 원문항 발문과 밑줄로 되돌리고 유형마다 새로 썼다."
CJ = "접속사 when: ‘~할 때’라는 시간의 부사절을 이끌므로"; QW = "의문사 when: ‘언제’라고 묻는 의문문을 이끌므로"
def f489(t, items, a, s=S489):
    mk(4, 89, t, [(x, w + (" 나머지와 달라" if i + 1 == a else "")) for i, (x, w) in enumerate(items)], a, R489, s, st=ST489)
f489("B", [("Call me <u>when</u> you arrive.", CJ), ("She smiled <u>when</u> she saw me.", CJ), ("I was studying <u>when</u> Tom called.", CJ), ("<u>When</u> does school start?", QW), ("We ate <u>when</u> we got home.", CJ)], 4,
     "밑줄이 사라지고 발문이 바뀌었다. 원문항 발문과 밑줄로 되돌렸다. 보기와 정답은 그대로다.")
f489("C", [("<u>When</u> did you get home?", QW), ("<u>When</u> is the concert?", QW), ("I felt sad <u>when</u> my dog was sick.", CJ), ("<u>When</u> will the bus come?", QW), ("<u>When</u> do you play soccer?", QW)], 3,
     "정답(When do you usually go to bed?)이 원문항과 같았고 오답도 B와 같았다. 원문항 발문과 밑줄로 되돌리고, 의문사 넷 + 접속사 하나로 새로 써서 구성을 달리했다.")
f489("D", [("<u>When</u> I was young, I lived in Busan.", CJ), ("<u>When</u> is your birthday?", QW), ("Turn off the light <u>when</u> you leave.", CJ), ("It was snowing <u>when</u> we woke up.", CJ), ("He laughed <u>when</u> he heard the joke.", CJ)], 2)
f489("E", [("<u>When</u> can you come?", QW), ("<u>When</u> did Jane call?", QW), ("<u>When</u> does the movie start?", QW), ("<u>When</u> is Mom coming back?", QW), ("Wash your hands <u>when</u> you get home.", CJ)], 5, S489 + " 의문사 넷 + 접속사 하나로 짜서 구성을 달리했다.")
f489("F", [("<u>When</u> did Jane arrive?", QW), ("We were happy <u>when</u> we won the game.", CJ), ("Say hello <u>when</u> you see him.", CJ), ("I fell down <u>when</u> I was running.", CJ), ("<u>When</u> it rains, we stay inside.", CJ)], 1)

# 4-90 시간 전치사 고치는 이유: 원문항 발문과 밑줄, 제시 문장에 맞춘 그럴듯한 오개념
R490 = "월·계절·연도에는 in, 요일·구체적인 날짜에는 on, 구체적인 시각에는 at을 쓴다. 주어·동사의 형태나 문장 종류는 전치사 선택과 관계없다."
S490 = "원문항 오답은 제시 문장에 대한 그럴듯한 오개념인데, 변형 오답(‘전치사는 아무거나 쓸 수 있다’ 등)은 뻔하고 유형마다 반복되었으며 정답만 제시 문장의 단어를 언급해 눈에 띄었다. 밑줄도 사라졌다. 원문항 발문과 밑줄로 되돌리고 제시 문장에 맞춘 그럴듯한 오개념으로 오답을 유형마다 새로 썼다."
OK90 = "시간 표현의 종류에 맞는 전치사를 바르게 설명했으므로"
def f490(t, a1, a2, j1, j2, p, items, a, s=S490):
    mk(4, 90, t, items, a, R490, s, st=f"주어진 지문에서 '{a1}'{j1} '{a2}'{j2} 고쳐야 하는 이유를 한국어로 가장 정확하게 설명한 것은?", p=p)
f490("B", "on", "in", "을", "으로", "We ski <u>on</u> winter.",
     [("'winter'는 요일처럼 하루를 가리키므로 'in'을 써야 한다.", "winter는 하루가 아니라 계절이므로"), ("'ski'는 운동을 나타내는 동사라 뒤에 항상 'in'이 와야 한다.", "전치사는 동사가 아니라 뒤의 시간 표현으로 정하므로"),
      ("'winter'는 계절이므로 'on' 대신 'in'을 써야 한다.", OK90), ("주어가 'We'이므로 'on' 대신 'in'을 써야 한다.", "주어는 전치사 선택과 관계없으므로"), ("'winter' 앞에 'the'가 없을 때만 'in'을 쓴다.", "계절에는 the가 있어도 in을 쓰므로")], 3)
f490("C", "in", "on", "을", "으로", "Let's meet <u>in</u> July 10th.",
     [("'July'는 달이므로 'on'으로 고쳐야 한다.", "달만 있으면 in을 쓰므로 고치는 이유가 되지 않으므로"), ("'10th'는 시각을 나타내므로 'at' 대신 'on'을 써야 한다.", "10th는 시각이 아니라 날짜이므로"), ("제안하는 문장(Let's)에서는 'in'을 쓸 수 없기 때문이다.", "문장의 종류는 전치사 선택과 관계없으므로"),
      ("'July'만 있으면 'in'을 쓰지만, 구체적인 날짜(July 10th)에는 'on'을 써야 한다.", OK90), ("'meet'라는 동사 뒤에는 항상 'on'을 써야 하기 때문이다.", "전치사는 동사가 아니라 뒤의 시간 표현으로 정하므로")], 4,
     "문장(Is your birthday in March 1st?)과 정답 설명이 원문항과 같았다. 문장을 새로 쓰고 " + S490[S490.index("원문항 발문과"):])
f490("D", "in", "on", "을", "으로", "We meet <u>in</u> Monday.",
     [("'Monday'는 요일이므로 'in' 대신 'on'을 써야 한다.", OK90), ("'Monday'는 한 주의 시작이라 긴 기간이므로 'on'을 쓴다.", "요일은 긴 기간이 아니고, 긴 기간에는 in을 쓰므로"), ("'meet'는 현재형이라 'on'과 함께 써야 한다.", "동사의 시제는 전치사 선택과 관계없으므로"),
      ("주어가 복수(We)일 때는 'on'을 써야 한다.", "주어는 전치사 선택과 관계없으므로"), ("요일에는 'at'을 써야 하지만 'on'도 허용된다.", "요일에는 at이 아니라 on을 쓰므로")], 1)
f490("E", "on", "at", "을", "으로", "School starts <u>on</u> 8 o'clock.",
     [("'8 o'clock'은 날짜이므로 'at'을 써야 한다.", "8 o'clock은 날짜가 아니라 시각이므로"), ("'School'이 장소이므로 'at'을 써야 한다.", "뒤의 시간 표현으로 전치사를 정하므로"), ("'starts'가 3인칭 단수 현재형이라 'at'을 써야 한다.", "동사의 형태는 전치사 선택과 관계없으므로"),
      ("아침 시간 전체를 나타낼 때는 'at'을 쓰기 때문이다.", "아침 전체는 in the morning이고 8 o'clock은 한 시각이므로"), ("'8 o'clock'은 구체적인 시각이므로 'at'을 써야 한다.", OK90)], 5)
f490("F", "on", "in", "을", "으로", "Tom was born <u>on</u> 2015.",
     [("'2015'는 특정한 하루를 나타내므로 'in'을 써야 한다.", "2015는 하루가 아니라 연도이므로"), ("연도 '2015'는 긴 기간이므로 'on' 대신 'in'을 써야 한다.", OK90), ("'born'이 과거분사이므로 뒤에는 항상 'in'이 와야 한다.", "동사의 형태는 전치사 선택과 관계없으므로"),
      ("수동태 문장에서는 'on'을 쓸 수 없기 때문이다.", "수동태도 날짜 앞에는 on을 쓰므로"), ("'Tom'이 사람 이름이므로 'in'을 써야 한다.", "주어는 전치사 선택과 관계없으므로")], 2)


# ---- 2차 감수(2026-10) 추가 ----
# 4-84 E: 원문항 문장(It rained, so we stayed at home.)의 앞뒤를 바꾼 문장 → 새 문장
FIX.pop((4, 84, "E"), None)
mk(4, 84, "E", [("because", "뒤 절(늦게 일어났다)이 버스를 놓친 이유이므로"), ("so", "so를 쓰면 ‘버스를 놓쳐서 늦게 일어났다’가 되어 뜻이 맞지 않으므로"), ("but", "but은 대조라 뜻이 맞지 않으므로"),
                ("and", "and는 단순히 이어 줄 뿐 이유를 나타내지 않으므로"), ("or", "or는 선택이라 뜻이 맞지 않으므로")], 1,
   "because는 이유(~ 때문에), so는 결과(그래서), but은 대조, or는 선택, and는 연결을 나타낸다.",
   "발문이 ‘제시된 우리말의 논리 관계를 직접 나타내는 접속사로’로 바뀌었고, 문장이 원문항 문장(It rained, so we stayed at home.)의 앞뒤만 바꾼 것(We stayed home because it rained.)이었다. 원문항 발문으로 되돌리고 문장을 새로 썼다.",
   st="R", p="나는 늦게 일어났기 때문에 버스를 놓쳤다.\nI missed the bus _____ I got up late.")
