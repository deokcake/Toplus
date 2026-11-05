# 2026-10-23 검토 페이지 ‘부적합’ 문항(26개 문항 번호) 반영.
# 부적합 문서는 메모대로 고치고, 같은 문항의 다른 유형은 확인 완료가 아닌 것만 같은 결함이 있으면 고친다. 확인 완료 문서(B 전부 등)는 건드리지 않는다.
MEMO3 = "감수 메모 반영(10-23): "
def OKS(items, a): return [w + OK(i + 1, a) for i, w in enumerate(items)]
def ADD(g_, n_, t_, more): return OLD(g_, n_, t_).get("s", "") + " " + more

# ---- 1-25: 문장을 원문항 길이(8~11 낱말)로 ----
_L25 = MEMO3 + "원문항보다 짧던 문장을 원문항 길이로 늘렸다. 틀린 문장의 자리와 정답은 그대로다."
RE(1, 25, "C", p="A) You had better to take a taxi to the airport now.\nB) Mina might have missed the last train to Busan last night.\nC) They must not to use their phones during the exam.\nD) There used to be a small pond behind our school.\nE) I am used to get up early on weekdays.\nF) Jane may be at the library with her friends now.", s=ADD(1, 25, "C", _L25))
RE(1, 25, "D", p="A) Tom would rather stay home than go out tonight.\nB) Jane may has forgotten the password to her email account.\nC) She should have call me earlier about the schedule change.\nD) I am used to taking the subway to work every day.\nE) There used to be a school here years ago.\nF) We would rather not to leave the party now.", s=ADD(1, 25, "D", _L25))
RE(1, 25, "E", p="A) We would rather leave now than waiting here for hours.\nB) Mina could have called us earlier about the delay.\nC) Tom can working at the new cafe this weekend.\nD) She is used to living alone in the big city.\nE) There used to be a theater here long ago.\nF) He will can finish the report by tomorrow morning.", s=ADD(1, 25, "E", _L25))
RE(1, 25, "F", p="A) Jane would rather read a novel than watch TV at night.\nB) Tom might have took the wrong bus to the stadium.\nC) He cannot have known everything about the plan.\nD) I used to getting up early when I was a child.\nE) There used to be a big factory near the river.\nF) Mina has to studies more for the final exam.", s=ADD(1, 25, "F", _L25))

# ---- 1-33: 능동문을 원문항 길이(10~12 낱말)로 늘리고 해설을 원문항 짜임으로 ----
R33 = "advise, tell, ask, encourage + 목적어 + to부정사 문장을 수동태로 바꾸면 ‘be + 과거분사 + to부정사’가 된다. to부정사는 그대로 남는다."
_L33 = MEMO3 + "원문항보다 짧던 문장을 원문항 길이로 늘리고, 해설을 원문항 짜임으로 다시 썼다. 정답은 그대로다."
def f33(t, act, subj, eun, be, base, pp, bad, good, rest, by):
    n = [f"주어 {subj}{eun} {'복수' if be == 'were' else '단수'}이고 과거의 일이라 {be}를 바르게 썼으므로", f"{base}의 과거분사 {pp}를 바르게 썼으므로",
         f"능동문의 {good}는 수동태에서도 to부정사로 남아야 하는데 {bad}으로 썼으므로", f"능동문의 부사구 {rest}를 그대로 썼으므로", "능동문의 주어를 by + 행위자로 바르게 나타냈으므로"]
    RE(1, 33, t, p=f"{act}\n→ {subj} ①<u>{be}</u> ②<u>{pp}</u> ③<u>{bad}</u> ④<u>{rest}</u> ⑤<u>{by}</u>.", c=[be, pp, bad, rest, by], a=3, r=R33, n=OKS(n, 3), k=n[2], s=ADD(1, 33, t, _L33))
f33("C", "The doctor advised the patient to rest at home for a week.", "The patient", "는", "was", "advise", "advised", "to resting", "to rest", "at home for a week", "by the doctor")
f33("D", "The teacher told the students to wait outside until the bell rang.", "The students", "는", "were", "tell", "told", "to waiting", "to wait", "outside until the bell rang", "by the teacher")
f33("E", "The manager asked Tom to stay late at the office on Friday.", "Tom", "은", "was", "ask", "asked", "to staying", "to stay", "late at the office on Friday", "by the manager")
f33("F", "The coach encouraged us to practice daily before the big game.", "We", "는", "were", "encourage", "encouraged", "to practicing", "to practice", "daily before the big game", "by the coach")

# ---- 1-35: 문장을 원문항보다 짧지 않게(8~11 낱말) ----
_L35 = MEMO3 + "원문항보다 짧던 문장을 늘렸다. 틀린 문장의 자리와 정답은 그대로다."
RE(1, 35, "C", p="a) My parents encouraged me to join the school art club.\n→ I was encouraged to join the school art club by my parents.\nb) The police looked for the missing child all night.\n→ The missing child was looked all night by the police.\nc) The teacher told us to be quiet during the test.\n→ We were told being quiet during the test by the teacher.\nd) They turned down my offer without any explanation.\n→ My offer was turned down without any explanation by them.\ne) The doctor ordered him to stay in bed for three days.\n→ He was ordered stay in bed for three days by the doctor.", s=ADD(1, 35, "C", _L35))
RE(1, 35, "D", p="a) The guide warned the tourists to stay together in the crowded market.\n→ The tourists were warned staying together in the crowded market by the guide.\nb) Grandma brought up three children on her own.\n→ Three children were brought up on her own by Grandma.\nc) The coach expected the team to win the final match.\n→ The team was expected to win the final match by the coach.\nd) The workers put out the fire in a few minutes.\n→ The fire was put in a few minutes by the workers.\ne) The students laughed at the joke about the teacher.\n→ The joke about the teacher was laughed by the students.", s=ADD(1, 35, "D", _L35))
RE(1, 35, "E", p="a) The manager allowed Tom to leave early for the dentist.\n→ Tom was allowed to leave early for the dentist by the manager.\nb) Everyone looked up to the old teacher in the village.\n→ The old teacher in the village was looked up to by everyone.\nc) The judge forced the man to pay the fine at once.\n→ The man was forced paying the fine at once by the judge.\nd) The students handed in their reports before the deadline.\n→ Their reports were handed before the deadline by the students.\ne) Mom asked me to buy some eggs on the way home.\n→ I was asked buy some eggs on the way home by Mom.", s=ADD(1, 35, "E", _L35))
RE(1, 35, "F", p="a) The librarian advised the kids to return the books on time.\n→ The kids were advised to returning the books on time by the librarian.\nb) The city carried out the plan for a new park.\n→ The plan for a new park was carried by the city.\nc) Our neighbors invited us to have dinner at their house.\n→ We were invited to have dinner at their house by our neighbors.\nd) The staff dealt with the complaint quickly and politely.\n→ The complaint was dealt quickly and politely by the staff.\ne) The police ordered the driver to stop at the corner.\n→ The driver was ordered to stop at the corner by the police.", s=ADD(1, 35, "F", _L35))

# ---- 1-47 C: ‘이유가 두 개’ → 첫째(To begin with) → Second로 흐름을 분명히 ----
RE(1, 47, "C", p="A: Why don't you want to join the camping trip?\nB: I have two reasons. (<u>         </u>), my grandmother is visiting us this weekend. Second, I have a big test on Monday.",
   n=["‘설상가상으로’는 나쁜 일이 겹칠 때 쓰므로 오답이다.", "이유가 두 개라고 말한 뒤 첫째 이유를 꺼내고 Second로 둘째 이유를 이으므로 ‘우선’이 알맞아 정답이다.", "‘이상한 말이지만’은 뜻밖의 일을 말할 때 쓰므로 오답이다.",
      "‘말하자면’은 다른 것에 빗대어 말할 때 쓰는데 빗댄 표현이 없으므로 오답이다.", "‘말할 필요도 없이’는 당연한 결과를 말할 때 쓰는데 할머니의 방문은 당연한 일이 아니므로 오답이다."],
   s=ADD(1, 47, "C", MEMO3 + "④ So to speak·⑤ Needless to say도 답처럼 읽힐 수 있어, ‘이유가 두 개’라고 밝힌 뒤 첫째 이유를 말하고 Second로 둘째 이유를 잇는 흐름으로 바꿔 To begin with만 들어가게 했다." + pos(2)))

# ---- 1-53·1-54: 오답에 to부정사가 맞는 문장을 섞어 ‘to부정사 = 틀림’으로 풀 수 없게 ----
R53 = "be worth, be busy, it is no use, spend + 시간, be good at, feel like, have difficulty, look forward to, succeed in, can't help 등의 뒤에는 동명사를 쓰고, want, hope, decide, plan, promise, need, agree 등은 to부정사를 목적어로 쓴다. 표현마다 뒤에 오는 형태를 구별한다."
_L53 = MEMO3 + "정답 빼고 모두 동명사라 to부정사만 찾으면 풀렸다. 옳은 문장 두 개를 to부정사를 바르게 쓴 문장으로 바꿔 표현마다 뒤의 형태를 알아야 풀리게 했다."
GER = "{} 뒤에 동명사를 바르게 썼다."; _J = {"plan": "plan은"}
def INF_(v): return f"{_J.get(v, v + '는')} to부정사를 목적어로 쓰므로 to부정사를 바르게 썼다."
class _I:
    def format(self, v): return INF_(v)
INF = _I()
RE(1, 53, "C", c=["Mina <u>is busy to prepare</u> for the interview.", "Tom <u>decided to study</u> abroad next year.", "This novel <u>is worth reading</u> twice.", "She <u>hopes to visit</u> her uncle in Busan.", "He <u>is good at remembering</u> names."], r=R53,
   n=OKS(["be busy 뒤에는 동명사를 쓴다. to prepare → preparing으로 고쳐야 하므로", INF.format("decide"), GER.format("be worth"), INF.format("hope"), GER.format("be good at")], 1), s=_L53 + pos(1))
RE(1, 53, "D", c=["I <u>feel like eating</u> something sweet.", "They <u>plan to visit</u> Jeju this summer.", "He <u>had difficulty finding</u> the address.", "She <u>wants to be</u> a doctor.", "We <u>look forward to hear</u> from you soon."], r=R53,
   n=OKS([GER.format("feel like"), INF.format("plan"), GER.format("have difficulty"), INF.format("want"), "look forward to의 to는 전치사라 동명사를 쓴다. hear → hearing으로 고쳐야 하므로"], 5), s=_L53 + pos(5))
RE(1, 53, "E", c=["My brother <u>is used to cooking</u> for himself.", "Jane <u>succeeded in solve</u> the puzzle.", "He <u>promised to call</u> me tonight.", "I <u>can't help laughing</u> at his jokes.", "She <u>needs to finish</u> her homework."], r=R53,
   n=OKS([GER.format("be used to"), "전치사 in 뒤에는 동명사를 쓴다. solve → solving으로 고쳐야 하므로", INF.format("promise"), GER.format("can't help"), INF.format("need")], 2), s=_L53 + pos(2))
RE(1, 53, "F", c=["<u>Keep practicing</u> and you will improve.", "Jane <u>agreed to help</u> us.", "We <u>were busy packing</u> for the trip.", "They <u>spent two hours to discuss</u> the problem.", "Tom <u>wants to buy</u> a new bike."], r=R53,
   n=OKS([GER.format("keep"), INF.format("agree"), GER.format("be busy"), "spend + 시간 뒤에는 동명사를 쓴다. to discuss → discussing으로 고쳐야 하므로", INF.format("want")], 4), s=_L53 + pos(4))

R54 = "avoid, postpone, consider, deny, finish, enjoy, mind, give up, quit, practice, admit, recommend, imagine 등은 동명사만 목적어로 쓰고, want, hope, decide, plan, promise, agree, need, learn 등은 to부정사를 목적어로 쓴다. continue, try는 둘 다 쓸 수 있다."
_L54 = MEMO3 + "정답 빼고 모두 동명사라 to부정사만 찾으면 풀렸다. 옳은 문장 두 개를 to부정사를 목적어로 쓰는 동사의 문장으로 바꿔 동사마다 목적어 형태를 알아야 풀리게 했다(원문항도 continue to, try to를 섞어 둠)."
G54 = "동사({})는 동명사를 목적어로 쓰므로 -ing형을 바르게 썼다."; I54 = "동사({})는 to부정사를 목적어로 쓰므로 to부정사를 바르게 썼다."; B54 = "동사({})는 동명사만 목적어로 쓰므로 to부정사를 쓸 수 없다. {}로 고쳐야 하므로"
RE(1, 54, "C", c=["My dad quit smoking last year.", "She wants to open the window.", "Mina avoided to answer the difficult question.", "The kids practiced singing the song.", "He decided to take a short break."], r=R54,
   n=OKS([G54.format("quit"), I54.format("want"), B54.format("avoid", "avoided answering"), G54.format("practice"), I54.format("decide")], 3), s=_L54 + pos(3))
RE(1, 54, "D", c=["She enjoys taking pictures of birds.", "They hope to win the game.", "He admitted breaking the window.", "Tom considered to move to another city.", "We planned to visit the museum."], r=R54,
   n=OKS([G54.format("enjoy"), I54.format("hope"), G54.format("admit"), B54.format("consider", "considered moving"), I54.format("plan")], 4), s=_L54 + pos(4))
RE(1, 54, "E", c=["The boy denied eating the cake.", "Jane postponed to make the decision.", "I promised to help my mom.", "She gave up learning the violin.", "They agreed to meet at noon."], r=R54,
   n=OKS([G54.format("deny"), B54.format("postpone", "postponed making"), I54.format("promise"), G54.format("give up"), I54.format("agree")], 2), s=_L54 + pos(2))
RE(1, 54, "F", c=["He recommended visiting the old palace.", "They need to leave early.", "Mina imagined living in Paris.", "We finished to clean the room.", "I learned to ride a bike."], r=R54,
   n=OKS([G54.format("recommend"), I54.format("need"), G54.format("imagine"), B54.format("finish", "finished cleaning"), I54.format("learn")], 4), s=_L54 + pos(4))

# ---- 1-76·1-98: 제시어 순서를 정답 어순과 다르게 ----
_L76 = MEMO3 + "제시어가 정답 어순 그대로였다. 순서를 섞었다. 보기와 정답은 그대로다."
RE(1, 76, "C", p="(stronger / it / this / than / much / years / was / bridge / ago / is / ten)", s=ADD(1, 76, "C", _L76))
RE(1, 76, "D", p="(taller / than / a / Mina / now / little / Jane / is)", s=ADD(1, 76, "D", _L76))
RE(1, 76, "E", p="(harder / test / than / this / even / is / yesterday's / test)", s=ADD(1, 76, "E", _L76))
RE(1, 76, "F", p="(cleaner / it / much / the / be / than / city / used / is / to)", s=ADD(1, 76, "F", _L76))
_L98 = MEMO3 + "제시어가 정답 어순에 가까웠다. 원문항처럼 더 무작위로 섞었다. 보기와 정답은 그대로다."
RE(1, 98, "C", p="(accepted / if / she / the / Mina / be / , / had / job / living / would / now / abroad / .)", s=ADD(1, 98, "C", _L98))
RE(1, 98, "D", p="(saved / he / if / money / Tom / a / , / own / had / more / would / now / car / .)", s=ADD(1, 98, "D", _L98))
RE(1, 98, "E", p="(chosen / we / the / if / route / had / , / be / other / we / there / would / now / .)", s=ADD(1, 98, "E", _L98))
RE(1, 98, "F", p="(moved / Leo / if / Seoul / he / , / had / live / to / would / us / now / near / .)", s=ADD(1, 98, "F", _L98))

# ---- 5-10 C: 핵심 규칙을 his 설명으로 ----
RE(5, 10, "C", r="his는 ‘그의’라는 소유격으로 명사 앞에 쓴다. he(주격), him(목적격), his(소유대명사: ‘그의 것’), he's(he is)와 구별한다.",
   n=OKS(["소유대명사 his는 명사 없이 홀로 쓰는데 뒤에 명사 bike가 있으므로", "‘그의’라는 뜻으로 명사 bike를 꾸미는 소유격이므로", "his는 사물을 가리키는 지시대명사가 아니므로", "주어는 Tom이고 주격은 he이므로", "목적격은 him이고 riding의 목적어는 his bike 전체이므로"], 2),
   k="‘그의’라는 뜻으로 명사 bike를 꾸미는 소유격이므로", s=MEMO3 + "their를 설명하던 핵심 규칙을 밑줄 친 his에 맞게 바꾸고 보기 해설을 다시 썼다. 보기와 정답은 그대로다." + pos(2))

# ---- 5-14: 정답을 원문항과 같은 개념(doesn't + -s)으로 ----
OK14 = "주어에 맞는 부정 형태를 바르게 썼으므로"
RE(5, 14, "D", c=["You aren't alone.", "They don't live here.", "Jane isn't a nurse.", "The kids aren't at school.", "Tom doesn't eats meat."],
   n=OKS([OK14, OK14, OK14, OK14, "doesn't 뒤에는 동사원형 eat을 써야 하므로"], 5), s=ADD(5, 14, "D", MEMO3 + "be동사 수 일치 오류였던 정답을 원문항과 같은 개념(doesn't 뒤의 -s형)으로 바꿨다."))
RE(5, 14, "E", c=["She doesn't watch TV.", "Jane doesn't plays the piano.", "I am not tired.", "It isn't cold today.", "We don't have class today."],
   n=OKS([OK14, "doesn't 뒤에는 동사원형 play를 써야 하므로", OK14, OK14, OK14], 2), s=ADD(5, 14, "E", MEMO3 + "don't/doesn't 수 일치 오류였던 정답을 원문항과 같은 개념(doesn't 뒤의 -s형)으로 바꿨다."))

# ---- 5-36 C: writing 대신 다른 동사 ----
RE(5, 36, "C", st="다음 빈칸에 '노래를 부르고 있다'라는 의미가 되도록 알맞은 단어를 고르세요.", p="Jane is ________ a song now.", c=["singing", "sings", "sing", "to sing", "sang"],
   n=["is와 함께 ‘부르고 있다’는 진행의 뜻이 되므로 정답이다.", "3인칭 단수 현재형이라 is 뒤에 쓸 수 없으므로 오답이다.", "is 뒤에 동사원형을 쓸 수 없으므로 오답이다.", "to부정사는 ‘부르고 있다’는 진행의 뜻이 되지 않으므로 오답이다.", "과거형이라 is 뒤에 쓸 수 없고 진행의 뜻도 되지 않으므로 오답이다."],
   s=ADD(5, 36, "C", MEMO3 + "여러 문항에 자주 나온 writing 대신 sing(노래를 부르고 있다)으로 바꿨다." + pos(1)))

# ---- 5-79 D: fast(형용사)를 설명하는 문제로 ----
RE(5, 79, "D", st="다음 문장에서 밑줄 친 'fast'의 역할에 대한 설명으로 옳은 것을 <보기>에서 고르시오.", p="Tom is a <u>fast</u> runner.\n<보기>\n(가) 명사 runner를 꾸미는 형용사이다.\n(나) 동사 is를 꾸미는 부사이다.\n(다) -ly를 붙여 fastly로 써야 부사가 된다.",
   c=["(가), (나)", "(나), (다)", "(가)", "(가), (나), (다)", "(다)"], a=3,
   pre=["설명별 판정: (가) O. 명사 runner 앞에서 runner를 꾸미는 형용사이다.", "설명별 판정: (나) X. 명사를 꾸미므로 부사가 아니고, is를 꾸미는 것도 아니다.", "설명별 판정: (다) X. fast는 -ly 없이 부사로도 쓰이며 fastly라는 낱말은 없다."],
   k="옳은 설명은 (가)이다.", n=["(나)는 옳은 설명이 아니다. 따라서 오답이다.", "(나), (다)는 옳은 설명이 아니고, 옳은 설명 (가)를 빠뜨렸다. 따라서 오답이다.", "옳은 설명 (가)를 빠짐없이 골랐으므로 정답이다.", "(나), (다)는 옳은 설명이 아니다. 따라서 오답이다.", "(다)는 옳은 설명이 아니고, 옳은 설명 (가)를 빠뜨렸다. 따라서 오답이다."],
   s=ADD(5, 79, "D", MEMO3 + "early 대신 fast를 설명하는 문제로 바꿨다. B(부사 fast)와 겹치지 않게 명사를 꾸미는 형용사 fast로 했다." + pos(3)))

# ---- 5-82 D: 주어 + 동사 + 전치사구 순서의 문장으로 ----
RE(5, 82, "D", p="우리 형은 은행에서 일한다.\n① My ② brother ③ works ④ a ⑤ bank.", a=4,
   n=["My 앞은 문장의 맨 앞이라 in이 올 자리가 아니므로 오답이다.", "brother는 주어의 일부라 그 앞에 in이 올 수 없으므로 오답이다.", "works는 동사라 그 앞에 in이 올 수 없으므로 오답이다.", "장소 표현 a bank 앞에 in을 넣으면 in a bank(은행에서)가 되므로 정답이다.", "a와 bank 사이에 in을 넣으면 a bank라는 덩어리가 끊어지므로 오답이다."],
   k="장소 표현 a bank 앞에 in을 넣어 in a bank(은행에서)가 되므로", s=ADD(5, 82, "D", MEMO3 + "주어 + 동사 + 전치사구 순서의 문장(우리 형은 은행에서 일한다)으로 바꿨다." + pos(4)))

# ---- 5-90 D: at의 쓰임에 관한 설명이 정답이 되게 ----
RE(5, 90, "D", c=["'at home'은 '집에'라는 뜻으로 자주 쓰는 표현이다.", "'at' 대신 'in'을 써서 'in home'이라고 하는 것은 어색하다.", "'at'은 장소를 넓은 공간으로 볼 때 쓰는 전치사이므로 'at home'은 집을 넓은 공간으로 본 표현이다.", "'She is at home.'은 그녀가 지금 있는 장소를 나타낸다.", "이 문장의 'at'은 시간이 아니라 장소를 나타내는 전치사이다."],
   n=["at home은 ‘집에’라는 뜻의 굳어진 표현이므로 옳은 설명이다. 따라서 오답이다.", "‘집에’는 in home이 아니라 at home으로 쓰므로 옳은 설명이다. 따라서 오답이다.", "at은 장소를 하나의 지점으로 볼 때 쓰고 넓은 공간은 in으로 나타내므로 옳지 않은 설명이다. 따라서 정답이다.", "at home이 그녀가 있는 장소를 나타내므로 옳은 설명이다. 따라서 오답이다.", "at 뒤에 장소 home이 왔으므로 옳은 설명이다. 따라서 오답이다."],
   k="at은 장소를 하나의 지점으로 볼 때 쓰고 넓은 공간은 in으로 나타내므로", s=ADD(5, 90, "D", MEMO3 + "the에 관한 설명이던 정답을 at의 쓰임(지점 ↔ 넓은 공간)에 관한 틀린 설명으로 바꿨다." + pos(3)))

# ---- 6-3 C: ③을 악기 이름 앞에 a를 쓴 오류로 ----
RE(6, 3, "C", c=["He opened <u>the</u> window.", "She has <u>an</u> uncle in Canada.", "She plays <u>a</u> piano after school.", "I want <u>a</u> glass of water.", "<u>The</u> boys are playing soccer."],
   r=OLD(6, 3, "C")["r"] + " 악기 이름 앞에도 the를 쓴다(play the piano).",
   n=OKS(["서로 알고 있는 특정 대상 앞에 the를 바르게 썼으므로", "처음 말하는 셀 수 있는 단수명사 앞에 첫소리에 맞는 a/an을 바르게 썼으므로", "악기 이름 앞에는 the를 써야 하므로(play the piano)", "처음 말하는 셀 수 있는 단수명사 앞에 첫소리에 맞는 a/an을 바르게 썼으므로", "서로 알고 있는 특정 대상 앞에 the를 바르게 썼으므로"], 3),
   s=ADD(6, 3, "C", MEMO3 + "③을 악기 이름 앞에 a를 쓴 오류(a piano)로 바꿨다." + pos(3)))

# ---- 6-5: 6급 범위 밖인 ‘유’ 소리 낱말(uniform, useful, university, unicorn) 제거, honest·hour로 ----
R65 = "a/an은 철자가 아니라 첫소리로 정한다. hour, honest처럼 h를 발음하지 않는 낱말은 모음 소리로 시작하므로 an을 쓴다."
_L65 = MEMO3 + "6급에서 배우지 않은 ‘유’ 소리 낱말(uniform, useful, university, unicorn)을 빼고, h를 발음하지 않는 honest·hour로 판단하는 문제로 바꿨다."
HOUR = "hour의 h는 발음하지 않아 모음 소리로 시작하므로 an을 바르게 썼으므로"
RE(6, 5, "C", c=["Let's wait for an hour.", "I saw an owl last night.", "Jane is a honest student.", "It is a big house.", "He has an old bike."], a=3, r=R65,
   n=OKS([HOUR, "owl은 모음 소리로 시작하므로 an을 바르게 썼으므로", "honest의 h는 발음하지 않아 모음 소리로 시작하므로 an honest로 써야 하므로", "big은 자음 소리로 시작하므로 a를 바르게 썼으므로", "old는 모음 소리로 시작하므로 an을 바르게 썼으므로"], 3), s=_L65 + pos(3))
RE(6, 5, "E", c=["That is an old tree.", "It takes a hour to get to school.", "She has a new bag.", "I ate an apple for lunch.", "We saw an elephant at the zoo."], a=2, r=R65,
   n=OKS(["old는 모음 소리로 시작하므로 an을 바르게 썼으므로", "hour의 h는 발음하지 않아 모음 소리로 시작하므로 an hour로 써야 하므로", "new는 자음 소리로 시작하므로 a를 바르게 썼으므로", "apple은 모음 소리로 시작하므로 an을 바르게 썼으므로", "elephant는 모음 소리로 시작하므로 an을 바르게 썼으므로"], 2), s=_L65 + pos(2))
RE(6, 5, "F", c=["Tom has an uncle in Busan.", "There is an ant on the desk.", "We have an English test today.", "I read an interesting book.", "Mr. Kim is a honest teacher."], a=5, r=R65,
   n=OKS(["uncle은 모음 소리로 시작하므로 an을 바르게 썼으므로", "ant는 모음 소리로 시작하므로 an을 바르게 썼으므로", "English는 모음 소리로 시작하므로 an을 바르게 썼으므로", "interesting은 모음 소리로 시작하므로 an을 바르게 썼으므로", "honest의 h는 발음하지 않아 모음 소리로 시작하므로 an honest로 써야 하므로"], 5), s=_L65 + pos(5))

# ---- 6-8: several → three ----
RE(6, 8, "C", p="The two desks are three _______ apart.", keepx=True, s=MEMO3 + "several을 three로 바꿨다. 보기와 정답은 그대로다.")
RE(6, 8, "E", p="Three _______ are swimming on the lake.", keepx=True, s=MEMO3 + "C와 같이 several을 Three로 바꿨다. 보기와 정답은 그대로다.")

# ---- 6-42: 불규칙 과거형 대신 규칙 변화(watch, cry) ----
R42 = "yesterday, last ~처럼 과거의 때를 나타내는 말이 있으면 동사의 과거형을 쓴다. 규칙동사는 -ed를 붙이고(자음 + y는 -ied), did와 과거형을 함께 쓰지 않는다."
RE(6, 42, "C", p="Mina _______ TV yesterday.", c=["watched", "watching", "did watched", "watch", "watches"], a=1, r=R42,
   n=["yesterday에 맞는 과거형이므로 정답이다.", "be동사 없이 -ing형만 쓸 수 없으므로 오답이다.", "did와 과거형을 함께 쓸 수 없으므로 오답이다.", "yesterday가 있어 현재형을 쓸 수 없으므로 오답이다.", "yesterday가 있어 현재형을 쓸 수 없으므로 오답이다."],
   s=ADD(6, 42, "C", MEMO3 + "6급에서 다루지 않는 불규칙 과거형(wrote) 대신 규칙 변화 watched로 바꿨다." + pos(1)))
RE(6, 42, "D", p="The baby _______ loudly yesterday.", c=["crying", "cries", "did cried", "cry", "cried"], a=5, r=R42,
   n=["be동사 없이 -ing형만 쓸 수 없으므로 오답이다.", "yesterday가 있어 현재형을 쓸 수 없으므로 오답이다.", "did와 과거형을 함께 쓸 수 없으므로 오답이다.", "yesterday가 있어 현재형을 쓸 수 없고 주어 The baby와도 맞지 않으므로 오답이다.", "yesterday에 맞는 과거형(자음 + y → -ied)이므로 정답이다."],
   s=ADD(6, 42, "D", MEMO3 + "앞 문항에 나온 study 대신 cry(cried)로 바꿨다." + pos(5)))

# ---- 6-88: ①을 be동사 단·복수 일치 오류로(원문항과 같은 개념) ----
R88 = "현재진행형은 주어 + am/is/are + 동사원형-ing로 쓴다. I에는 am, 3인칭 단수에는 is, you와 복수 주어에는 are를 쓴다."
_L88 = MEMO3 + "동사의 -ing형 오류였던 정답을 원문항과 같은 개념(be동사의 수 일치 오류)으로 바꾸고 ①이 정답이 되게 했다."
RE(6, 88, "D", p="My parents ①<u>is</u> ②<u>cooking</u> ③<u>dinner</u> ④<u>in</u> ⑤<u>the kitchen</u>.", c=["is", "cooking", "dinner", "in", "the kitchen"], a=1, r=R88,
   n=OKS(["복수 주어 My parents에는 is가 아니라 are를 써야 하므로", "be동사 뒤에 -ing형 cooking을 바르게 썼으므로", "cooking의 목적어 dinner를 바르게 썼으므로", "부엌 안을 나타내는 전치사 in을 바르게 썼으므로", "서로 아는 특정한 부엌이라 the kitchen을 바르게 썼으므로"], 1), s=ADD(6, 88, "D", _L88 + pos(1)))
RE(6, 88, "E", p="You ①<u>is</u> ②<u>wearing</u> ③<u>a</u> ④<u>new</u> ⑤<u>jacket</u>.", c=["is", "wearing", "a", "new", "jacket"], a=1, r=R88,
   n=OKS(["주어 You에는 is가 아니라 are를 써야 하므로", "be동사 뒤에 -ing형 wearing을 바르게 썼으므로", "셀 수 있는 단수명사 jacket 앞에 a를 바르게 썼으므로", "명사 jacket을 꾸미는 형용사 new를 바르게 썼으므로", "a new 뒤에 단수명사 jacket을 바르게 썼으므로"], 1), s=ADD(6, 88, "E", _L88 + pos(1)))

# ---- 6-103: 정답을 원문항과 같은 개념(How/What about + -ing)으로 ----
_L103 = MEMO3 + "정답을 원문항과 같은 개념(about + -ing 제안)으로 바꿨다."
RE(6, 103, "D", p="A: It's sunny.\nB: ________ taking a walk in the park?", c=["Let's", "Shall we", "What about", "Why don't", "Do you"], a=3,
   n=["Let's 뒤에는 동사원형을 쓰므로 오답이다.", "Shall we 뒤에는 동사원형을 쓰므로 오답이다.", "What about + -ing로 제안을 나타내므로 정답이다.", "Why don't 뒤에는 주어 we와 동사원형이 와야 하므로 오답이다.", "Do you 뒤에 -ing형을 바로 쓸 수 없으므로 오답이다."], s=ADD(6, 103, "D", _L103 + pos(3)))
RE(6, 103, "E", p="A: We are free.\nB: ________ playing tennis?", c=["Shall we", "Let's", "How about", "Why don't", "Are we"], a=3,
   n=["Shall we 뒤에는 동사원형을 쓰므로 오답이다.", "Let's 뒤에는 동사원형을 쓰므로 오답이다.", "How about + -ing로 제안을 나타내므로 정답이다.", "Why don't 뒤에는 주어 we와 동사원형이 와야 하므로 오답이다.", "Are we playing tennis?는 지금 하고 있는지 묻는 말이라 제안이 되지 않으므로 오답이다."], s=ADD(6, 103, "E", _L103 + pos(3)))

# ---- 6-104: 정답을 원문항과 같은 개념(How/What about 뒤 동사원형 오류)으로 ----
R104 = "명령문은 동사원형으로 시작하고(be동사는 Be), 부정 명령문은 Don't/Never + 동사원형으로 쓴다. 제안은 Let's + 동사원형, Shall we + 동사원형?, Why don't we + 동사원형?, How/What about + -ing?로 나타낸다."
OK104 = "명령·제안 표현 뒤에 알맞은 형태를 바르게 썼으므로 오답이다."
_L104 = MEMO3 + "정답을 원문항과 같은 개념(How/What about 뒤에 동사원형을 쓴 오류)으로 바꿨다."
RE(6, 104, "D", c=["Shall we sing together?", "Never tell a lie.", "Let's play tennis.", "How about go camping?", "Don't be sad."], n=[OK104, OK104, OK104, "How about 뒤에는 동사원형이 아니라 -ing형 going을 써야 하므로 정답이다.", OK104], s=ADD(6, 104, "D", _L104 + pos(4)))
RE(6, 104, "E", c=["What about ride bikes?", "Let's clean the room.", "Never be late for class.", "Don't touch the stove.", "Shall we sit here?"], a=1, n=["What about 뒤에는 동사원형이 아니라 -ing형 riding을 써야 하므로 정답이다.", OK104, OK104, OK104, OK104], s=ADD(6, 104, "E", _L104 + pos(1)))
RE(6, 104, "F", c=["Don't make noise.", "Let's take a short break.", "Never touch that switch.", "Shall we open the window?", "How about walk to school?"], a=5, r=R104, n=[OK104, OK104, OK104, OK104, "How about 뒤에는 동사원형이 아니라 -ing형 walking을 써야 하므로 정답이다."], s=_L104 + pos(5))

# ---- 7-2 D: 달 이름 대신 고유명사(도시) ----
RE(7, 2, "D", c=["busan", "boy", "dog", "rice", "room"], r="사람 이름, 나라·도시 이름, 요일 같은 고유명사는 문장 어디에서든 첫 글자를 대문자로 쓴다. 일반 명사는 문장 첫머리가 아니면 소문자로 쓴다.",
   n=["busan: 도시 이름이라 대문자로 시작해야 하므로 정답이다.", "boy: 일반 명사라 소문자로 써도 되므로 오답이다.", "dog: 일반 명사라 소문자로 써도 되므로 오답이다.", "rice: 일반 명사라 소문자로 써도 되므로 오답이다.", "room: 일반 명사라 소문자로 써도 되므로 오답이다."],
   s=ADD(7, 2, "D", MEMO3 + "7급에서 배우지 않은 달 이름(january) 대신 도시 이름 busan을 정답으로 했다." + pos(1)))

# ---- 7-3: 정답을 쉬운 물질명사(수를 붙인 오류)로 ----
R73 = "셀 수 없는 명사(water, milk, juice, bread, rice, paper)는 some과 함께 쓰고 수를 붙이거나 복수형으로 쓰지 않는다. 셀 수 있는 명사는 two, four, many 뒤에서 복수형으로 쓴다."
UNC = "셀 수 없는 명사({})를 some과 함께 바르게 썼으므로"; CNT = "셀 수 있는 명사를 복수형({})으로 바르게 썼으므로"
RE(7, 3, "D", c=["I need <u>two waters</u>.", "I drank <u>some juice</u>.", "She has <u>some paper</u>.", "They saw <u>many birds</u>.", "He bought <u>three notebooks</u>."], a=1, r=R73,
   n=OKS(["water는 셀 수 없는 명사라 two를 붙이거나 복수형으로 쓰지 않으므로", UNC.format("juice"), UNC.format("paper"), CNT.format("birds"), CNT.format("notebooks")], 1),
   s=ADD(7, 3, "D", MEMO3 + "어려운 정답(two homeworks)을 쉬운 물질명사 water에 수를 붙인 오류(two waters)로 바꿨다." + pos(1)))
RE(7, 3, "E", c=["They want <u>some soup</u>.", "She likes <u>oranges</u>.", "I drink <u>two milks</u> every morning.", "He has <u>four pencils</u>.", "I have <u>five pens</u>."], a=3, r=R73,
   n=OKS([UNC.format("soup"), CNT.format("oranges"), "milk는 셀 수 없는 명사라 two를 붙이거나 복수형으로 쓰지 않으므로", CNT.format("pencils"), CNT.format("pens")], 3),
   s=ADD(7, 3, "E", MEMO3 + "셀 수 있는 명사의 복수형 오류(four pencil)였던 정답을 원문항과 같은 개념인 물질명사 milk에 수를 붙인 오류(two milks)로 바꿨다." + pos(3)))
RE(7, 3, "F", c=["She has <u>three books</u>.", "He likes <u>bananas</u>.", "Mom buys <u>some cheese</u>.", "I eat <u>some rice</u>.", "She drinks <u>two juices</u>."], a=5, r=R73,
   n=OKS([CNT.format("books"), CNT.format("bananas"), UNC.format("cheese"), UNC.format("rice"), "juice는 셀 수 없는 명사라 two를 붙이거나 복수형으로 쓰지 않으므로"], 5),
   s=ADD(7, 3, "F", MEMO3 + "셀 수 있는 명사의 복수형 오류(many book)였던 정답을 원문항과 같은 개념인 물질명사 juice에 수를 붙인 오류(two juices)로 바꿨다." + pos(5)))

# ---- 7-32 D·7-34 D: children 대신 규칙 변화 복수형 ----
RE(7, 32, "D", c=["We <u>are</u> not late.", "The students <u>is</u> not tired.", "Jane <u>is</u> not here.", "The dogs <u>are</u> not hungry.", "I <u>am</u> not angry."],
   n=["주어(We)에 맞는 be동사(are)를 바르게 썼으므로 오답이다.", "복수 주어 The students에는 is가 아니라 are를 써야 하므로 정답이다.", "주어(Jane)에 맞는 be동사(is)를 바르게 썼으므로 오답이다.", "주어(The dogs)에 맞는 be동사(are)를 바르게 썼으므로 오답이다.", "주어(I)에 맞는 be동사(am)를 바르게 썼으므로 오답이다."],
   s=ADD(7, 32, "D", MEMO3 + "불규칙 복수형 children 대신 규칙 변화 복수형 students로 바꿨다." + pos(2)))
RE(7, 34, "D", c=["_______ the kids at the park?", "_______ you and Tom brothers?", "_______ these shoes new?", "_______ your bag heavy?", "_______ they in the library?"],
   n=["주어(the kids)에는 Are가 들어가므로 오답이다.", "주어(you and Tom)에는 Are가 들어가므로 오답이다.", "주어(these shoes)에는 Are가 들어가므로 오답이다.", "주어(your bag)에는 Are가 아니라 be동사(Is)가 들어가므로 정답이다.", "주어(they)에는 Are가 들어가므로 오답이다."],
   s=ADD(7, 34, "D", MEMO3 + "불규칙 복수형 children 대신 규칙 변화 복수형 kids로 바꿨다." + pos(4)))

# ---- 7-79 C·D: 의문사가 든 문장(do/does 오류)이 정답이 되게 ----
_L79 = MEMO3 + "대답 문장의 -s 오류였던 정답을 What 의문문의 do/does 오류로 바꿨다."
RE(7, 79, "C", p="Good morning, Mina! ①<u>What do you eat for breakfast</u>? ②<u>I eat toast</u>. ③<u>What do your brother drink</u>? ④<u>He drinks milk</u>. ⑤<u>What do your parents eat</u>? They eat rice.",
   c=["What do you eat for breakfast", "I eat toast", "What do your brother drink", "He drinks milk", "What do your parents eat"], a=3,
   n=OKS(["주어 you에 do와 동사원형 eat을 바르게 썼으므로", "주어 I에 동사원형 eat을 바르게 썼으므로", "3인칭 단수 주어 your brother에는 do가 아니라 does를 써야 하므로", "3인칭 단수 주어 He에 drinks를 바르게 썼으므로", "복수 주어 your parents에 do와 동사원형 eat을 바르게 썼으므로"], 3), s=ADD(7, 79, "C", _L79 + pos(3)))
RE(7, 79, "D", p="Look at the club list. ①<u>What do Tom do</u>? ②<u>He plays the guitar</u>. ③<u>What do Jane and Amy do</u>? ④<u>They dance</u>. ⑤<u>What do you do</u>? I sing songs.",
   c=["What do Tom do", "He plays the guitar", "What do Jane and Amy do", "They dance", "What do you do"], a=1,
   n=OKS(["3인칭 단수 주어 Tom에는 do가 아니라 does를 써야 하므로", "3인칭 단수 주어 He에 plays를 바르게 썼으므로", "복수 주어 Jane and Amy에 do를 바르게 썼으므로", "주어 They에 동사원형 dance를 바르게 썼으므로", "주어 you에 do와 동사원형 do를 바르게 썼으므로"], 1), s=ADD(7, 79, "D", _L79 + pos(1)))
