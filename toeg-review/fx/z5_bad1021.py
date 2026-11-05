# 2026-10-21 검토 페이지 ‘부적합’ 문항(10개) 반영 — 모든 유형(B~F)을 다시 보고 필요한 것만 고친다.
MEMO2 = "감수 메모 반영(10-21): "
def OKS(items, a): return [w + OK(i + 1, a) for i, w in enumerate(items)]

# ---- 1-5·1-9: 원문항보다 짧던 문장을 원문항 길이(7~10 낱말)로 ----
_L = MEMO2 + "원문항보다 짧던 문장을 원문항 길이로 늘렸다. 틀린 문장의 자리와 정답은 그대로다."
RE(1, 5, "B", p="a) The coffee tastes bitter without any sugar.\nb) They found the hotel room comfortably after the trip.\nc) The teacher kept us busy with extra homework.\nd) The train arrived late because of the heavy snow.\ne) We discussed the proposal for a long time.\nf) Tom entered into the office without knocking.", s=_L)
RE(1, 5, "C", p="a) This wool blanket feels warmly on cold nights.\nb) We found the instructions clear and easy to follow.\nc) The guard kept the gate locked during the night.\nd) The baby slept peacefully in her mother's arms.\ne) She informed us of the change in the schedule.\nf) We approached to the old castle slowly in the fog.", s=OLD(1, 5, "C").get("s", "") + " " + _L)
RE(1, 5, "D", p="a) The soup tastes delicious with a little salt.\nb) We found the math task difficultly at first.\nc) The cold weather kept the lake frozen all winter.\nd) Birds flew quietly overhead in the evening sky.\ne) She informed me of the result by email.\nf) We entered into the hall through the side door.", s=OLD(1, 5, "D").get("s", "") + " " + _L)
RE(1, 5, "E", p="a) The flowers smell sweet in the spring garden.\nb) They considered the new plan practical and safe.\nc) We kept the lights on during the storm.\nd) The dog sleeps soundly next to the fireplace.\ne) He discussed about the issue with his teammates.\nf) Mina reached the station just before noon.", s=OLD(1, 5, "E").get("s", "") + " " + _L)
RE(1, 5, "F", p="a) The sky looks beautifully after the summer rain.\nb) I found the book useful for my science report.\nc) The news made us anxious about the trip.\nd) The child slept quietly in the back seat.\ne) Jane informed Tom of the decision this morning.\nf) We reached home safely before the storm.", s=OLD(1, 5, "F").get("s", "") + " " + _L)
RE(1, 9, "B", p="(a) The smell of fresh bread made me hungry.\n(b) We found the new chair comfortably after a long day.\n(c) The teacher kept us focused during the lesson.\n(d) She left the engine running in the parking lot.\n(e) The heavy rain made the road dangerous at night.", s=OLD(1, 9, "B").get("s", "") + " " + _L)
RE(1, 9, "C", p="(a) The joke about his hat made everyone angrily.\n(b) We found the hotel room empty at midnight.\n(c) The soft music kept the baby calm for an hour.\n(d) I left the kitchen door open by mistake.\n(e) The long wait at the airport made us impatiently.", s=OLD(1, 9, "C").get("s", "") + " " + _L)
RE(1, 9, "D", p="(a) The news about the test made Mina nervous.\n(b) They found the old wall beautifully in the morning light.\n(c) We found the wooden box heavy to carry.\n(d) The teacher kept the class quiet during the exam.\n(e) The cold weather made the road slippery this morning.", s=OLD(1, 9, "D").get("s", "") + " " + _L)
RE(1, 9, "E", p="(a) The long movie made us bored by the end.\n(b) I found the instructions confusingly at first.\n(c) We kept the windows closed during the storm.\n(d) They left the lights on in the empty room.\n(e) The result of the match made Tom proud.", s=OLD(1, 9, "E").get("s", "") + " " + _L)
RE(1, 9, "F", p="(a) The speech about courage made everyone inspiringly.\n(b) They found the science task difficult at first.\n(c) We kept the front door locked all night.\n(d) The loud noise kept the baby awake for hours.\n(e) I found the movie entertaining from start to finish.", s=OLD(1, 9, "F").get("s", "") + " " + _L)

# ---- 1-56: 제시어 없이 우리말 문장만(원문항과 같게) ----
ST56N = "다음 우리말을 영어로 바르게 옮긴 것을 고르시오."
for _t, _ko in [("B", "나는 그 박물관을 방문했던 것을 기억한다."), ("C", "나는 Mina를 만났던 것을 기억한다."), ("D", "나는 문을 잠갔던 것을 기억한다."), ("E", "나는 그 비밀을 말했던 것을 기억한다."), ("F", "나는 그 영화를 봤던 것을 기억한다.")]:
    RE(1, 56, _t, st=ST56N, p=_ko, s=MEMO2 + "원문항과 함께 제시어를 없애고 우리말 문장만 주어 알맞은 영어 문장을 고르는 유형으로 바꿨다. 보기와 정답은 그대로다.")

# ---- 3-108: 제시어 순서를 정답 어순과 다르게(B·F), 괄호 표기 통일 ----
RE(3, 108, "B", p="이것은 우리 동네에서 가장 오래된 건물 중 하나이다.\n( one / this / old / of / in / is / building / the / our / town / . )", s=OLD(3, 108, "B").get("s", "") + " " + MEMO2 + "제시어가 정답 어순 그대로였다. 순서를 섞었다.")
RE(3, 108, "C", p="Tom은 우리 반에서 가장 키 큰 학생 중 하나이다.\n( Tom / one / of / tall / student / is / class / in / our / the / . )", s=OLD(3, 108, "C").get("s", "") + " 괄호 표기를 원문항과 같게 했다.")
RE(3, 108, "D", p="이것은 가게에서 가장 비싼 가방 중 하나이다.\n( this / one / of / expensive / bag / is / store / in / the / most / the / . )", s=OLD(3, 108, "D").get("s", "") + " 괄호 표기를 원문항과 같게 했다.")
RE(3, 108, "E", p="Jane은 팀에서 가장 빠른 선수 중 하나이다.\n( Jane / one / of / fast / player / is / team / on / the / the / . )", s=OLD(3, 108, "E").get("s", "") + " 괄호 표기를 원문항과 같게 했다.")
RE(3, 108, "F", p="한강은 한국에서 가장 긴 강 중 하나이다.\n( river / one / is / of / the Han River / long / in / the / Korea / . )", s=OLD(3, 108, "F").get("s", "") + " " + MEMO2 + "제시어가 정답 어순 그대로였다. 순서를 섞었다.")

# ---- 4-20 B: 문장별 판정 (B)의 설명 오류 ----
RE(4, 20, "B", pre=["문장별 판정: (A) O. scissors는 복수 취급한다.", "문장별 판정: (B) X. 명사 없이 ‘그들의 것’은 소유대명사 theirs로 쓴다. 소유대명사에는 '를 붙이지 않는다.", "문장별 판정: (C) X. news는 단수 취급해 is를 쓴다.", "문장별 판정: (D) O. 목적어 자리에 목적격 them을 썼다."],
   s=OLD(4, 20, "B").get("s", "") + " " + MEMO2 + "(B)의 해설이 ‘명사 앞 소유격 their’라고 잘못 설명한 것을 ‘소유대명사 theirs’로 바로잡았다.")

# ---- 7-11: 7급은 주격·소유격만(목적격 me·them·us·him 제거) ----
R711 = "대명사의 뜻: 주격(I, you, he, she, it, we, they)은 ‘~은/는’, 소유격(my, your, his, her, its, our, their)은 ‘~의’로 옮긴다."
S711 = MEMO2 + "7급에서 배우지 않은 목적격 보기를 주격·소유격 보기로 바꿨다."
def f711(t, items, a, s=S711):
    RE(7, 11, t, c=[x for x, _ in items], a=a, r=R711, n=OKS([w for _, w in items], a), k=items[a - 1][1], s=s + pos(a))
f711("B", [("your - 너의", "your: ‘너의’로 바르게 옮겼으므로"), ("she - 그녀는", "she: ‘그녀는’으로 바르게 옮겼으므로"), ("his - 그의", "his: ‘그의’로 바르게 옮겼으므로"), ("my - 나는", "my는 소유격이라 ‘나의’로 옮겨야 하므로"), ("they - 그들은", "they: ‘그들은’으로 바르게 옮겼으므로")], 4)
f711("C", [("my - 나의", "my: ‘나의’로 바르게 옮겼으므로"), ("we - 우리는", "we: ‘우리는’으로 바르게 옮겼으므로"), ("she - 그녀는", "she: ‘그녀는’으로 바르게 옮겼으므로"), ("his - 그는", "his는 소유격이라 ‘그의’로 옮겨야 하므로"), ("their - 그들의", "their: ‘그들의’로 바르게 옮겼으므로")], 4, MEMO2 + "보기는 그대로 두고 해설의 핵심 규칙에서 목적격 설명을 뺐다.")
f711("D", [("our - 우리의", "our: ‘우리의’로 바르게 옮겼으므로"), ("your - 너는", "your는 소유격이라 ‘너의’로 옮겨야 하므로"), ("she - 그녀는", "she: ‘그녀는’으로 바르게 옮겼으므로"), ("we - 우리는", "we: ‘우리는’으로 바르게 옮겼으므로"), ("his - 그의", "his: ‘그의’로 바르게 옮겼으므로")], 2)
f711("E", [("your - 너의", "your: ‘너의’로 바르게 옮겼으므로"), ("its - 그것의", "its: ‘그것의’로 바르게 옮겼으므로"), ("our - 우리는", "our는 소유격이라 ‘우리의’로 옮겨야 하므로"), ("she - 그녀는", "she: ‘그녀는’으로 바르게 옮겼으므로"), ("they - 그들은", "they: ‘그들은’으로 바르게 옮겼으므로")], 3)
f711("F", [("their - 그들은", "their는 소유격이라 ‘그들의’로 옮겨야 하므로"), ("he - 그는", "he: ‘그는’으로 바르게 옮겼으므로"), ("we - 우리는", "we: ‘우리는’으로 바르게 옮겼으므로"), ("my - 나의", "my: ‘나의’로 바르게 옮겼으므로"), ("our - 우리의", "our: ‘우리의’로 바르게 옮겼으므로")], 1)

# ---- 7-12: 주격 - 소유격 관계로(원문항과 함께) ----
R712N = "I - my는 주격 - 소유격(‘~는’ - ‘~의’)의 짝이다. 주격: I, you, he, she, it, we, they / 소유격: my, your, his, her, its, our, their."
SAME712 = "주격 - 소유격 관계라 <보기>와 같으므로"
def f712n(t, bogi, pairs, a):
    def jo(w): return w + ("은" if w == "it" else "는")
    items = [(x, SAME712 if i + 1 != a else f"{jo(x.split(' - ')[0])} 소유격, {jo(x.split(' - ')[1])} 주격이라 순서가 <보기>와 반대이므로") for i, x in enumerate(pairs)]
    RE(7, 12, t, st="R", p=f"<보기>\n{bogi}", c=pairs, a=a, r=R712N, n=OKS([w for _, w in items], a), k=items[a - 1][1],
       s=MEMO2 + "7급에서 배우지 않은 목적격 관계(I - me) 대신 주격 - 소유격 관계로 바꿨다(원문항도 같게). 관계가 다른 짝은 순서가 거꾸로인 것 하나다." + pos(a))
f712n("B", "we - our", ["he - his", "you - your", "it - its", "their - they", "she - her"], 4)
f712n("C", "he - his", ["I - my", "you - your", "they - their", "we - our", "its - it"], 5)
f712n("D", "she - her", ["it - its", "we - our", "my - I", "they - their", "he - his"], 3)
f712n("E", "they - their", ["our - we", "you - your", "I - my", "he - his", "it - its"], 1)
f712n("F", "it - its", ["I - my", "his - he", "we - our", "you - your", "they - their"], 2)

# ---- 7-14 B·C: his가 정답이 되게 ----
RE(7, 14, "B", p="This is <u>my father's</u> car.", c=["their", "his", "our", "my", "her"], a=2,
   n=OKS(["their는 여럿의 소유이므로", "my father(남자 한 명)의 소유는 his로 바꾸므로", "our는 나를 포함한 여럿의 소유이므로", "my는 나의 소유라 아버지의 소유를 나타내지 못하므로", "her는 여자 한 명의 소유이므로"], 2),
   k="my father(남자 한 명)의 소유는 his로 바꾸므로", s=MEMO2 + "정답이 his가 되도록 밑줄 친 말을 my father's로 바꿨다." + pos(2))
RE(7, 14, "C", p="The dog is <u>my brother's</u> pet.", c=["our", "their", "his", "her", "my"], a=3,
   n=OKS(["our는 나를 포함한 여럿의 소유이므로", "their는 여럿의 소유이므로", "my brother(남자 한 명)의 소유는 his로 바꾸므로", "her는 여자 한 명의 소유이므로", "my는 나의 소유라 형(오빠)의 소유를 나타내지 못하므로"], 3),
   k="my brother(남자 한 명)의 소유는 his로 바꾸므로", s=MEMO2 + "정답이 his가 되도록 밑줄 친 말을 my brother's로 바꿨다." + pos(3))

# ---- 7-35 C: 쉬운 낱말로(book, pens), 소유대명사(yours/mine)도 뺌 ----
RE(7, 35, "C", p="_______ this book new? (이 책은 새것이니?)\nThe pens _______ long. (그 펜들은 길지 않아.)", xr=[("this jacket", "this book"), ("The gloves", "The pens")],
   s=OLD(7, 35, "C").get("s", "") + " " + MEMO2 + "jacket·gloves와 7급에서 배우지 않은 yours·mine을 쉬운 낱말(book, pens, new, long)로 바꿨다. 보기와 정답은 그대로다.")

# ---- 7-82 C·D: to부정사·-ing 오답을 3인칭 단수형 오답으로 ----
OK82 = "can 뒤에 동사원형({})을 써서 알맞으므로"
RE(7, 82, "C", c=["bake cookies", "play tennis", "grow flowers", "use a computer", "drives a bus"], a=5,
   n=OKS([OK82.format("bake"), OK82.format("play"), OK82.format("grow"), OK82.format("use"), "can 뒤에는 동사원형 drive를 써야 하는데 3인칭 단수형 drives를 썼으므로"], 5),
   k="can 뒤에는 동사원형 drive를 써야 하는데 3인칭 단수형 drives를 썼으므로", s=OLD(7, 82, "C").get("s", "") + " " + MEMO2 + "7급에 어려운 to부정사 오답(to drive a bus)을 3인칭 단수형 오답(drives a bus)으로 바꿨다.")
RE(7, 82, "D", c=["dance well", "read Japanese", "climb a tree", "plays the violin", "ride a horse"], a=4,
   n=OKS([OK82.format("dance"), OK82.format("read"), OK82.format("climb"), "can 뒤에는 동사원형 play를 써야 하는데 3인칭 단수형 plays를 썼으므로", OK82.format("ride")], 4),
   k="can 뒤에는 동사원형 play를 써야 하는데 3인칭 단수형 plays를 썼으므로", s=OLD(7, 82, "D").get("s", "") + " " + MEMO2 + "7급에서 배우지 않은 -ing형 오답(playing the violin)을 3인칭 단수형 오답(plays the violin)으로 바꿨다.")

# ---- 7-97: 과거형 대신 현재형 be동사 + do/does (원문항과 함께) ----
R797 = "be동사는 주어에 맞춘다: I → am, 한 사람·한 개(he, she, it, Today, Jane 등) → is, you·we·they·여럿 → are. ‘~이다’, ‘~하다(상태)’를 나타낼 때는 do/does가 아니라 be동사를 쓴다."
W797 = {"am": "am은 주어 I에만 쓰므로", "is": "is는 한 사람·한 개인 주어에 쓰므로", "are": "are는 you·we·they와 여럿인 주어에 쓰므로",
        "do": "do는 일반동사의 부정문·의문문에 쓰는 말이라 be동사 자리에 올 수 없으므로", "does": "does는 일반동사의 부정문·의문문에 쓰는 말이라 be동사 자리에 올 수 없으므로"}
def f797(t, p, c, a, subj):
    good = f"주어 {subj}에 맞는 be동사이므로"
    RE(7, 97, t, p=p, c=c, a=a, r=R797, n=OKS([good if i + 1 == a else W797[x] for i, x in enumerate(c)], a), k=f"주어 {subj}에 맞는 be동사는 {c[a-1]}이므로",
       s=MEMO2 + "7급에서 배우지 않은 과거형(was/were) 대신 현재형 be동사와 do/does 가운데 고르는 문항으로 바꿨다(원문항도 같게)." + pos(a))
f797("B", "Today is Sunday. The boys ______ busy.", ["is", "am", "are", "do", "does"], 3, "The boys(여럿)")
f797("C", "It ______ windy today.", ["do", "is", "does", "am", "are"], 2, "It(한 개)")
f797("D", "Today is sunny. It ______ hot.", ["are", "does", "am", "is", "do"], 4, "It(한 개)")
f797("E", "Today is Tuesday. My friends ______ here.", ["is", "are", "am", "does", "do"], 2, "My friends(여럿)")
f797("F", "Today is Thursday. Jane ______ at home.", ["is", "does", "are", "am", "do"], 1, "Jane(한 사람)")
