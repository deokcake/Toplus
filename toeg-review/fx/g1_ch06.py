# 1급 CH6 동명사 (51~60) 수정 예시
import re

# 1-51 동명사의 의미상 주어: 정답 형태를 알려 주던 발문을 원문항대로
for t in "BCDEF":
    F(1, 51, t, st="R", p=V(1, 51, t)["passage"].replace(" / ", "\n"),
      s="발문의 ‘동명사의 의미상 주어를 소유격으로 나타내어’가 정답 형태를 알려 주어 원문항 발문으로 되돌리고, 우리말과 영어 문장을 두 줄로 나눴다.")

# 1-52 deny + 완료동명사: 단순동명사 오답을 명백히 틀린 형태로, 발문 조건 삭제
R52 = "deny는 동명사를 목적어로 취한다. 부정한 때보다 먼저 한 일은 완료동명사 having + 과거분사로 분명하게 나타낸다."
def g52(x, pp):
    if x == f"having {pp}": return f"deny 뒤에 동명사를 쓰고, 부정하기 전에 한 일이므로 완료동명사 having {pp}가 알맞다. 정답이다."
    if x.startswith("to "): return f"{x}: deny는 to부정사를 목적어로 취하지 않는다. 오답이다."
    if x.startswith("being "): return f"{x}: 수동동명사라 주어가 직접 한 일을 나타내지 못한다. 오답이다."
    return f"{x}: having 뒤에는 과거분사가 와야 하므로 틀린 형태이다. 오답이다."
S52 = "오답의 단순동명사({})는 deny + -ing로 과거 행위를 나타낼 수 있어 정답이 될 수 있었고, 발문의 ‘완료동명사를 사용하여’ 조건이 답을 정해 주었다. 단순동명사를 명백히 틀린 ‘{}’로 바꾸고 발문 조건을 지웠다."
def f52(t, c, a, pp, simple, s_extra=""):
    F(1, 52, t, st="R", p=V(1, 52, t)["passage"].replace(" / ", "\n"), c=c, a=a, r=R52, n=[g52(x, pp) for x in c],
      s=S52.format(simple, [x for x in c if x.startswith("to be ")][0]) + s_extra)
f52("B", ["having shared", "to share", "to have shared", "to be sharing", "having sharing"], 1, "shared", "sharing")
f52("C", ["to be copying", "to copied", "to have copied", "having copied", "being copied"], 4, "copied", "copying")
f52("D", ["to have taken", "being taken", "having taken", "to be taking", "to taken"], 3, "taken", "taking")
f52("E", ["having left", "being left", "to left", "to be leaving", "to have left"], 1, "left", "leaving")
f52("F", ["to be telling", "to told", "having told", "being told", "to have told"], 3, "told", "telling")

# 1-53 동명사 관용 표현: 오답 네 문장을 유형마다 새로(틀린 문장과 짝 없애기)
R53 = "worth, busy, no use, spend + 시간, be good at, look forward to, succeed in, feel like, have difficulty 등의 뒤에는 동명사(-ing)를 쓴다."
def ok53(expr): return f"{expr} 뒤에 동명사를 바르게 썼다. 오답이다."
S53 = "오답 네 문장이 B와 똑같고, 틀린 문장이 같은 표현의 옳은 문장과 짝을 이뤄 대비 단서가 되었다. 옳은 문장 네 개를 유형마다 다른 동명사 표현으로 새로 썼다. 밑줄도 원문항처럼 ‘표현 + 동사 형태’ 전체에 그었다."
F(1, 53, "C", r=R53, a=1,
  c=["Mina <u>is busy to prepare</u> for the interview.", "It <u>is no use crying</u> over spilled milk.", "This novel <u>is worth reading</u> twice.", "She <u>spent all day cleaning</u> the garage.", "He <u>is good at remembering</u> names."],
  n=["be busy 뒤에는 동명사를 쓴다. to prepare → preparing으로 고쳐야 하므로 정답이다.", ok53("It is no use"), ok53("be worth"), ok53("spend + 시간"), ok53("be good at")], s=S53)
F(1, 53, "D", r=R53, a=5,
  c=["I <u>feel like eating</u> something sweet.", "The kids <u>had fun playing</u> in the snow.", "He <u>had difficulty finding</u> the address.", "<u>How about going</u> to the beach?", "We <u>look forward to hear</u> from you soon."],
  n=[ok53("feel like"), ok53("have fun"), ok53("have difficulty"), ok53("How about"), "look forward to의 to는 전치사라 동명사를 쓴다. hear → hearing으로 고쳐야 하므로 정답이다."], s=S53)
F(1, 53, "E", r=R53, a=2,
  c=["My brother <u>is used to cooking</u> for himself.", "Jane <u>succeeded in solve</u> the puzzle.", "<u>There is no point arguing</u> about it.", "I <u>can't help laughing</u> at his jokes.", "She <u>is interested in learning</u> Spanish."],
  n=[ok53("be used to"), "전치사 in 뒤에는 동명사를 쓴다. solve → solving으로 고쳐야 하므로 정답이다.", ok53("There is no point"), ok53("can't help"), ok53("be interested in")], s=S53 + " 정답 위치 ②.")
F(1, 53, "F", r=R53, a=4,
  c=["<u>Keep practicing</u> and you will improve.", "<u>Thank you for helping</u> me.", "We <u>were busy packing</u> for the trip.", "They <u>spent two hours to discuss</u> the problem.", "<u>It's no good worrying</u> about the past."],
  n=[ok53("keep"), ok53("전치사 for"), ok53("be busy"), "spend + 시간 뒤에는 동명사를 쓴다. to discuss → discussing으로 고쳐야 하므로 정답이다.", ok53("It's no good")], s=S53 + " 정답 위치 ④.")

# 1-54 동명사 목적어 동사: 오답 네 문장을 유형마다 새로
R54 = "avoid, consider, postpone, finish, quit, mind, practice, suggest, enjoy, delay, admit, keep, deny, give up, stop, recommend, risk, imagine, miss는 동명사를 목적어로 취한다."
def ok54(v): return f"동사({v})는 동명사를 목적어로 취하므로 -ing형을 바르게 썼다. 오답이다."
def bad54(v, fix): return f"동사({v})는 동명사를 목적어로 취하므로 to부정사를 쓸 수 없다. {fix}로 고쳐야 하므로 정답이다."
S54 = "오답 네 문장이 B와 똑같고 틀린 문장이 같은 동사의 옳은 문장과 짝을 이뤘다. 옳은 문장 네 개를 다른 동사로 새로 썼다."
F(1, 54, "C", r=R54, a=3,
  c=["My dad quit smoking last year.", "Would you mind opening the window?", "Mina avoided to answer the difficult question.", "The kids practiced singing the song.", "I suggested taking a short break."],
  n=[ok54("quit"), ok54("mind"), bad54("avoid", "avoided answering"), ok54("practice"), ok54("suggest")], s=S54)
F(1, 54, "D", r=R54, a=4,
  c=["She enjoys taking pictures of birds.", "They delayed starting the game.", "He admitted breaking the window.", "Tom considered to move to another city.", "We kept walking in the rain."],
  n=[ok54("enjoy"), ok54("delay"), ok54("admit"), bad54("consider", "considered moving"), ok54("keep")], s=S54)
F(1, 54, "E", r=R54, a=2,
  c=["The boy denied eating the cake.", "Jane postponed to make the decision.", "I don't mind waiting for you.", "She gave up learning the violin.", "Stop making so much noise."],
  n=[ok54("deny"), bad54("postpone", "postponed making"), ok54("mind"), ok54("give up"), ok54("stop")], s=S54)
F(1, 54, "F", r=R54, a=4,
  c=["He recommended visiting the old palace.", "They risked losing everything.", "Mina imagined living in Paris.", "We finished to clean the room.", "I missed seeing the sunrise."],
  n=[ok54("recommend"), ok54("risk"), ok54("imagine"), bad54("finish", "finished cleaning"), ok54("miss")], s=S54)

# 1-55 틀린 문장 개수: 발문을 원문항과 같게, 0개~4개 정렬, 줄바꿈
# B 검토 의견(원문항에 비해 문장이 짧고 단어 수가 적음) 반영: 문장마다 원문항 길이(9~11단어)로
R55 = "동사마다 목적어로 동명사를 쓰는지 to부정사를 쓰는지 확인한다. deny, avoid, suggest, consider, finish, enjoy, postpone, admit, give up 등은 동명사를, decide, promise, want, agree, expect, plan, refuse 등은 to부정사를 목적어로 쓴다."
S55 = "발문에 빠진 ‘밑줄 친 부분이’를 넣어 원문항 발문으로 되돌리고, 개수 선택지를 0개~4개 순으로 정렬했다. 또 B 검토 의견(원문항에 비해 문장이 짧고 단어 수가 적음)이 이 유형에도 해당해, 문장마다 꾸며 주는 말을 붙여 원문항 길이로 늘리고 한 줄에 한 문장씩 나눴다."
def f55(t, lines, judge, wrong, s=S55):
    n_ = len(wrong); a = n_ + 1; c = ["0개", "1개", "2개", "3개", "4개"]; w = ", ".join(wrong)
    F(1, 55, t, st="R", p="\n".join(lines), c=c, a=a, r=R55, pre=["문장별 판정:"] + judge, k=f"어법상 틀린 문장은 {w}의 {n_}개이다.",
      n=[f"어법상 틀린 문장은 {w}의 {n_}개이다. 이 보기의 {x}는 실제 개수와 {'일치하므로 정답이다' if i + 1 == a else '일치하지 않으므로 오답이다'}." for i, x in enumerate(c)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f55("B", ["A. Tom denied <u>taking</u> the important file from the teacher's desk.", "B. Jane avoided <u>to answer</u> the reporter's difficult questions after the game.", "C. We decided <u>to leave</u> the party early because of the heavy rain.",
          "D. Leo suggested <u>going</u> to Busan by train instead of by car.", "E. Mina promised <u>helping</u> us with the science project this weekend."],
    ["A. 옳음: deny는 동명사를 목적어로 쓴다(denied taking).", "B. 틀림: avoid는 동명사를 목적어로 쓴다. avoided to answer → avoided answering.", "C. 옳음: decide는 to부정사를 목적어로 쓴다(decided to leave).",
     "D. 옳음: suggest는 동명사를 목적어로 쓴다(suggested going).", "E. 틀림: promise는 to부정사를 목적어로 쓴다. promised helping → promised to help."], ["B", "E"],
    "검토 의견(원문항에 비해 문장이 짧고 단어 수가 적음)에 따라, 문장마다 꾸며 주는 말을 붙여 원문항 길이로 늘렸다. 발문에 빠진 ‘밑줄 친 부분이’를 넣어 원문항 발문으로 되돌리고, 개수 선택지를 0개~4개 순으로 정렬했으며, 한 줄에 한 문장씩 나눴다.")
f55("C", ["A. Mina avoided <u>answering</u> the question about her weekend plans.", "B. Tom agreed <u>signing</u> the new rental agreement without any questions.", "C. We considered <u>moving</u> the meeting to next Friday afternoon.",
          "D. Jane promised <u>to call</u> her grandmother later in the evening.", "E. Leo enjoys <u>being included</u> in the school's leadership program."],
    ["A. 옳음: avoid는 동명사를 목적어로 쓴다(avoided answering).", "B. 틀림: agree는 to부정사를 목적어로 쓴다. agreed signing → agreed to sign.", "C. 옳음: consider는 동명사를 목적어로 쓴다(considered moving).",
     "D. 옳음: promise는 to부정사를 목적어로 쓴다(promised to call).", "E. 옳음: enjoy는 동명사를 목적어로 쓰고, 포함되는 쪽이므로 수동동명사 being included가 알맞다."], ["B"],
    S55 + " 원문항 A와 거의 같던 ‘refused signing the agreement’는 ‘agreed signing’ 오류로 바꿨다.")
f55("D", ["A. I enjoy <u>reading</u> mystery novels on quiet Sunday afternoons.", "B. She postponed <u>meeting</u> him until the end of the month.", "C. Tom refused <u>to lend</u> his new bike to his little brother.",
          "D. We finished <u>to paint</u> the old fence before it started to rain.", "E. They regret <u>telling</u> their friends the secret so easily."],
    ["A. 옳음: enjoy는 동명사를 목적어로 쓴다(enjoy reading).", "B. 옳음: postpone은 동명사를 목적어로 쓴다(postponed meeting).", "C. 옳음: refuse는 to부정사를 목적어로 쓴다(refused to lend).",
     "D. 틀림: finish는 동명사를 목적어로 쓴다. finished to paint → finished painting.", "E. 옳음: regret + 동명사는 이미 한 일을 후회한다는 뜻이다(regret telling)."], ["D"],
    S55 + " 원문항 C와 거의 같던 ‘considered to move’는 ‘finished to paint’ 오류로 바꿨다.")
f55("E", ["A. Jane expects <u>finishing</u> her history report by this Friday.", "B. Tom admitted <u>making</u> the mistake in front of the whole class.", "C. We gave up <u>searching</u> for the lost key after two hours.",
          "D. Mina decided <u>to stay</u> at home and study for the exam.", "E. Leo denied <u>to copy</u> his friend's answers during the test."],
    ["A. 틀림: expect는 to부정사를 목적어로 쓴다. expects finishing → expects to finish.", "B. 옳음: admit은 동명사를 목적어로 쓴다(admitted making).", "C. 옳음: give up은 동명사를 목적어로 쓴다(gave up searching).",
     "D. 옳음: decide는 to부정사를 목적어로 쓴다(decided to stay).", "E. 틀림: deny는 동명사를 목적어로 쓴다. denied to copy → denied copying."], ["A", "E"],
    S55 + " 원문항 D와 비슷하던 ‘hopes finishing’은 ‘expects finishing’으로 바꿨다.")
f55("F", ["A. They avoided <u>talking</u> about the problem in front of the kids.", "B. Mina wants <u>to travel</u> around Europe after her graduation.", "C. Tom finished <u>writing</u> his long history essay late last night.",
          "D. Jane considered <u>changing</u> jobs to spend more time with her family.", "E. We planned <u>visiting</u> our grandparents during the long holiday."],
    ["A. 옳음: avoid는 동명사를 목적어로 쓴다(avoided talking).", "B. 옳음: want는 to부정사를 목적어로 쓴다(wants to travel).", "C. 옳음: finish는 동명사를 목적어로 쓴다(finished writing).",
     "D. 옳음: consider는 동명사를 목적어로 쓴다(considered changing).", "E. 틀림: plan은 to부정사를 목적어로 쓴다. planned visiting → planned to visit."], ["E"],
    S55 + " 원문항 A와 거의 같던 ‘refused signing the contract’는 ‘planned visiting’ 오류로 바꿨다.")

# 1-56 remember + 동명사/to부정사 영작: 발문 조건 삭제, 오답을 의미 차이로 구별되게
R56 = "remember + 동명사는 ‘(과거에) ~한 것을 기억하다’, remember + to부정사는 ‘(앞으로) ~할 것을 기억하다’라는 뜻이다. 주절의 시제도 우리말(기억한다/기억했다)에 맞춘다."
def g56(x, a_ok):
    if x == a_ok: return "remember + 동명사로 과거에 한 일을 지금 기억한다는 우리말 뜻에 맞는다. 정답이다."
    if x.startswith("I remembered to "): return "remembered + to부정사는 ‘할 일을 잊지 않고 했다’는 뜻이라 우리말과 다르다."
    if x.startswith("I remembered "): return "remembered는 과거에 기억했다는 뜻이라 우리말 ‘기억한다’와 시제가 다르다."
    if x.startswith("I remember to "): return "remember + to부정사는 앞으로 할 일을 기억한다는 뜻이라 우리말과 다르다."
    if x.split()[2] in ("visit", "meet", "lock", "tell", "see"): return "remember 뒤에 동사원형을 바로 쓸 수 없다. 과거에 한 일을 기억한다는 뜻이면 동명사를 써야 한다."
    return "I will …은 앞으로 할 일을 나타내 우리말 ‘~했던 것’과 맞지 않는다."
S56 = "발문에 ‘동사 한 개만 -ing형으로, 목록에 없는 단어는 추가하지 않는다’ 조건이 붙어 정답 형태를 알려 주었고, 정답과 오답이 now 하나로만 갈렸다. 발문을 원문항과 같게 하고, remember to / remembered -ing처럼 뜻 차이로 구별하는 오답을 만들었다. B 검토 의견(주어진 단어에 불필요한 to가 들어 있음)에 따라 제시어에는 정답에 쓰는 단어만 두었다."
def f56(t, words, ko, c, a):
    F(1, 56, t, st="R", p=f"( {words} )\n({ko})", c=c, a=a, r=R56, n=[g56(x, c[a - 1]) for x in c], s=S56 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f56("B", "remember / visit / that / museum / I / .", "나는 그 박물관을 방문했던 것을 기억한다.",
    ["I remember to visit that museum.", "I remembered visiting that museum.", "I remember visiting that museum.", "I remember I will visit that museum.", "I remember visit that museum."], 3)
f56("C", "remember / meet / Mina / I / .", "나는 Mina를 만났던 것을 기억한다.",
    ["I remember meeting Mina.", "I remember to meet Mina.", "I remembered meeting Mina.", "I remember I will meet Mina.", "I remember meet Mina."], 1)
f56("D", "remember / lock / the / door / I / .", "나는 문을 잠갔던 것을 기억한다.",
    ["I remember to lock the door.", "I remembered locking the door.", "I remember I will lock the door.", "I remember locking the door.", "I remember lock the door."], 4)
f56("E", "remember / tell / the / secret / I / .", "나는 그 비밀을 말했던 것을 기억한다.",
    ["I remember tell the secret.", "I remember to tell the secret.", "I remembered telling the secret.", "I remember I will tell the secret.", "I remember telling the secret."], 5)
f56("F", "remember / see / that / movie / I / .", "나는 그 영화를 봤던 것을 기억한다.",
    ["I remembered seeing that movie.", "I remember seeing that movie.", "I remember to see that movie.", "I remember see that movie.", "I remember I will see that movie."], 2)

# 1-57 regret + 완료동명사: 발문 조건 삭제, 없는 형태(hav …)를 원문항 같은 오답(having + 원형)으로
R57 = "regret 뒤의 동명사로 후회하는 때보다 먼저 한 일을 나타낼 때는 완료동명사 having + 과거분사를 쓴다."
def g57(x, pp):
    if x == f"having {pp}": return f"후회하기 전에 한 일이므로 완료동명사 having {pp}가 알맞다. 정답이다."
    if x.startswith("having "): return f"{x}: having 뒤에는 과거분사가 와야 하므로 틀린 형태이다."
    if x.startswith("to ") and x.endswith("ing"): return f"{x}: regret 뒤에 ‘to + -ing’ 형태는 쓸 수 없다."
    if x.startswith("to have "): return f"{x}: regret + to부정사는 ‘~하게 되어 유감이다’라는 뜻이고, 이미 한 일을 후회하는 뜻과 다르다."
    if x.startswith("being "): return f"{x}: 수동동명사라 주어가 직접 한 일을 나타내지 못한다."
    return f"{x}: regret 뒤 목적어 자리에 과거형·과거분사만 쓸 수 없다."
S57 = "발문이 ‘완료동명사를 사용하여’라고 정답을 알려 주었고 오답 ‘hav …’는 존재하지 않는 형태였다. 발문 조건을 지우고, ‘hav …’를 원문항처럼 ‘having + 동사원형’ 오답으로 바꿨다. 격식체에서 쓰이기도 하는 ‘to have + 과거분사’ 오답은 분명히 틀린 ‘to + -ing’로 바꿨다. 두 문장을 두 줄로 나눴다."
S57b = "B 검토 의견(원문항에 비해 문장이 짧고 단어 수가 적음)이 이 유형에도 해당해, 원문항 길이로 문장을 늘렸다."
P57 = {"B": "We regret that we left the concert early last night.\n→ We regret __________ the concert early last night.",
       "C": "She regrets that she ignored the doctor's warning about her health.\n→ She regrets __________ the doctor's warning about her health.",
       "D": "Tom regrets that he missed the dentist appointment yesterday.\n→ Tom regrets __________ the dentist appointment yesterday.",
       "E": "Mina regrets that she told the secret to her classmates.\n→ Mina regrets __________ the secret to her classmates.",
       "F": "Leo regrets that he made such a hasty decision last year.\n→ Leo regrets __________ such a hasty decision last year."}
def f57(t, c, a, pp, extra=""):
    lead = "검토 의견(원문항에 비해 문장이 짧고 단어 수가 적음)에 따라 원문항 길이로 문장을 늘렸다. " if t == "B" else ""
    F(1, 57, t, st="R", p=P57[t], c=c, a=a, r=R57, n=[g57(x, pp) for x in c], s=lead + S57 + ("" if t == "B" else " " + S57b) + extra + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f57("B", ["left", "to leaving", "being left", "having leave", "having left"], 5, "left")
f57("C", ["having ignore", "having ignored", "ignored", "being ignored", "to ignoring"], 2, "ignored")
f57("D", ["having miss", "missed", "to missing", "having missed", "being missed"], 4, "missed", " 원문항과 같던 동사 forget은 miss로 바꿨다.")
f57("E", ["having told", "told", "having tell", "being told", "to telling"], 1, "told")
f57("F", ["made", "having make", "having made", "to making", "being made"], 3, "made")

# 1-58 prevent … from -ing 배열: 발문을 원문항대로, 오답을 제시어로 만든 어순·형태 오류로
R58 = "prevent + 목적어 + from + 동명사는 ‘(목적어)가 ~하지 못하게 하다’라는 뜻이다. from 바로 뒤에 동명사를 둔다."
BASE = "동사를 -ing형으로 바꾸지 않았고 from의 위치도 틀렸다. 오답이다."
FRONT = "from + 동명사가 목적어 앞으로 가서 prevent + 목적어 + from + 동명사 어순이 깨졌다. 오답이다."
TO = "from 대신 to부정사를 쓰고 from을 엉뚱한 곳에 두었다. 오답이다."
SWAP = "목적어와 다른 말의 자리가 바뀌어 우리말과 뜻이 달라졌다. 오답이다."
OK58 = "prevent + 목적어 + from + 동명사 어순이고 동사 하나만 -ing형으로 바꿨다. 정답이다."
S58 = "발문에 ‘동사 한 개만 -ing형으로’ 조건이 붙어 정답 형태를 알려 주었고, 오답 일부가 prevent(수 일치 변경)나 us·runn 같은 오타형 낱말을 썼다. 발문을 원문항과 같게 하고, 오답을 제시어로 만든 어순·형태 오류로 새로 만들었다."
def f58(t, ko, words, c, a, kinds):
    F(1, 58, t, st="R", p=f"{ko}\n({words})", c=c, a=a, r=R58, n=[(OK58 if i + 1 == a else kinds[i]) for i in range(5)], s=S58 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f58("B", "마스크는 먼지가 코로 들어오는 것을 막는다.", "prevents / from / dust / enter / the nose / the mask",
    ["The mask prevents dust enter from the nose.", "The mask prevents from entering dust the nose.", "The mask prevents dust to enter from the nose.", "The mask prevents dust from entering the nose.", "The mask prevents the nose from entering dust."], 4,
    [BASE, FRONT, TO, None, SWAP])
f58("C", "교사는 학생들이 휴대폰을 사용하지 못하게 한다.", "prevents / from / students / use / phones / the teacher",
    ["The teacher prevents students from using phones.", "The teacher prevents students use from phones.", "The teacher prevents from using students phones.", "The teacher prevents students to use from phones.", "The teacher prevents phones from using students."], 1,
    [None, BASE, FRONT, TO, SWAP])
f58("D", "규칙은 사람들이 여기 주차하지 못하게 한다.", "prevents / from / people / park / here / the rule",
    ["The rule prevents people park from here.", "The rule prevents from parking people here.", "The rule prevents people from parking here.", "The rule prevents people to park from here.", "The rule prevents here from parking people."], 3,
    [BASE, FRONT, None, TO, SWAP])
f58("E", "비는 우리가 밖에 나가지 못하게 했다.", "prevented / from / us / go / outside / the rain",
    ["The rain prevented us go from outside.", "The rain prevented from going us outside.", "The rain prevented us to go from outside.", "The rain prevented outside from going us.", "The rain prevented us from going outside."], 5,
    [BASE, FRONT, TO, SWAP, None])
f58("F", "안전문은 아이들이 도로로 뛰어가지 못하게 한다.", "prevents / from / children / run / onto the road / the gate",
    ["The gate prevents children run from onto the road.", "The gate prevents children from running onto the road.", "The gate prevents from running children onto the road.", "The gate prevents children to run from onto the road.", "The gate prevents children running from onto the road."], 2,
    [BASE, None, FRONT, TO, "from이 동명사 뒤로 가서 from onto라는 틀린 연결이 되었다. 오답이다."])

# 1-59 옳은 문장으로만 짝지어진 것: 원문항 발문이면 부분집합도 답이 되므로 옳은 문장을 셋으로 맞춤
R59 = "look forward to, object to, be used to, be accustomed to, be devoted to, contribute to, in addition to, the key to의 to는 전치사라 뒤에 명사·동명사를 쓴다. be busy, spend + 시간, feel like, insist on, succeed in 뒤에도 동명사를 쓴다."
def f59(t, lines, judge, ok, c, a, s):
    F(1, 59, t, st="R", p="\n".join(lines), c=c, a=a, r=R59, pre=["문장별 판정:"] + judge, k=f"어법상 옳은 문장은 {ok}뿐이고, 이 세 문장으로만 짝지어진 것은 하나다.",
      n=setnotes(c, ok, "옳은 문장"), s=s)
S59L = " 문장도 원문항 길이로 늘렸다."
S59 = "발문을 원문항 ‘어법상 옳은 문장으로만 짝지어진 것’으로 되돌렸다. 이 발문에서는 옳은 문장만으로 된 조합이 여럿이면 정답이 여러 개가 되므로, 원문항처럼 옳은 문장 셋·틀린 문장 둘로 맞추고 보기 조합을 새로 만들었다. 한 줄에 한 문장씩 나눴다."
f59("B", ["(A) Jane objected to waiting any longer for the late bus.", "(B) We are accustomed to working together on group projects.", "(C) Tom is busy to prepare dinner for his family tonight.", "(D) Mina spent three hours practicing for the piano contest.", "(E) They prevented us from enter the building after six."],
    ["(A) 옳음: object to 뒤에 동명사를 썼다.", "(B) 옳음: be accustomed to 뒤에 동명사를 썼다.", "(C) 틀림: be busy 뒤에는 동명사를 쓴다. to prepare → preparing.", "(D) 옳음: spend + 시간 뒤에 동명사를 썼다.", "(E) 틀림: from 뒤에는 동명사를 쓴다. enter → entering."],
    "(A), (B), (D)", ["(A), (B), (D)", "(A), (C), (E)", "(B), (C), (D)", "(A), (D), (E)", "(B), (D), (E)"], 1, S59 + S59L)
f59("C", ["(A) She is devoted to helping others.", "(B) He got used to drive on the left.", "(C) The key to succeed is patience.", "(D) In addition to singing, she dances well.", "(E) This tool contributes to saving time."],
    ["(A) 옳음: be devoted to 뒤에 동명사를 썼다.", "(B) 틀림: get used to의 to는 전치사라 동명사를 쓴다. drive → driving.", "(C) 틀림: the key to의 to는 전치사라 명사·동명사를 쓴다. succeed → success(succeeding).",
     "(D) 옳음: in addition to 뒤에 동명사를 썼다.", "(E) 옳음: contribute to 뒤에 동명사를 썼다."],
    "(A), (D), (E)", ["(A), (B), (C)", "(A), (D), (E)", "(B), (C), (E)", "(A), (C), (D)", "(B), (D), (E)"], 2,
    "다섯 문장이 원문항과 같은 구문(look forward to, object to, when it comes to …)을 고쳐 쓴 수준이었고 발문 괄호가 used to 문장을 짚어 주었다. be devoted to, get used to, the key to, in addition to, contribute to로 구문을 바꾸고 괄호를 지웠다. 발문을 원문항과 같게 하고 옳은 문장을 셋으로 맞췄다.")
f59("D", ["(A) We are used to work late during the busy season.", "(B) Leo insisted on paying for everyone's lunch yesterday.", "(C) Mina looks forward to meet you at the party.", "(D) Tom finally succeeded in solving the difficult math problem.", "(E) I feel like taking a short break after this class."],
    ["(A) 틀림: be used to의 to는 전치사라 동명사를 쓴다. work → working.", "(B) 옳음: insist on 뒤에 동명사를 썼다.", "(C) 틀림: look forward to 뒤에는 동명사를 쓴다. meet → meeting.",
     "(D) 옳음: succeed in 뒤에 동명사를 썼다.", "(E) 옳음: feel like 뒤에 동명사를 썼다."],
    "(B), (D), (E)", ["(A), (B), (D)", "(B), (C), (E)", "(B), (D), (E)", "(A), (D), (E)", "(C), (D), (E)"], 3, S59 + " 발문 괄호도 지웠다." + S59L)
f59("E", ["(A) I am looking forward to seeing you at the festival.", "(B) Tom is used to get up early on school days.", "(C) Jane succeeded in passing the driving test last week.", "(D) We feel like eating out at the new Italian restaurant.", "(E) Mina insisted on to pay for the movie tickets."],
    ["(A) 옳음: look forward to 뒤에 동명사를 썼다.", "(B) 틀림: be used to의 to는 전치사라 동명사를 쓴다. get up → getting up.", "(C) 옳음: succeed in 뒤에 동명사를 썼다.", "(D) 옳음: feel like 뒤에 동명사를 썼다.", "(E) 틀림: 전치사 on 뒤에는 동명사를 쓴다. to pay → paying."],
    "(A), (C), (D)", ["(A), (B), (C)", "(A), (B), (D)", "(B), (C), (D)", "(A), (C), (D)", "(A), (C), (E)"], 4,
    "불필요한 발문 괄호를 지우고 원문항 발문 ‘어법상 옳은 문장으로만 짝지어진 것’으로 되돌렸다. 네 문장 조합이던 보기 ②를 원문항처럼 세 문장 조합으로 바꾸고, 문장을 원문항 길이로 늘렸다. 정답은 그대로 ④.")
f59("F", ["(A) Leo is busy preparing dinner for his grandparents tonight.", "(B) We objected to change the date of the school festival.", "(C) Jane is accustomed to working alone in a quiet room.", "(D) Tom looks forward to hear from you about the result.", "(E) I feel like going home early because of this headache."],
    ["(A) 옳음: be busy 뒤에 동명사를 썼다.", "(B) 틀림: object to의 to는 전치사라 동명사를 쓴다. change → changing.", "(C) 옳음: be accustomed to 뒤에 동명사를 썼다.",
     "(D) 틀림: look forward to 뒤에는 동명사를 쓴다. hear → hearing.", "(E) 옳음: feel like 뒤에 동명사를 썼다."],
    "(A), (C), (E)", ["(A), (B), (D)", "(B), (C), (E)", "(A), (C), (E)", "(C), (D), (E)", "(A), (B), (C)"], 3, S59 + S59L)

# 1-60 be likely to 설명: B 검토 의견(선택지 품질이 원문항보다 낮음) 반영 — 원문항처럼 밑줄 친 표현을 짚고 이유까지 밝힌 그럴듯한 설명으로
R60 = "be likely to + 동사원형은 ‘~할 것 같다, ~할 가능성이 높다’는 뜻이다. 이 to는 전치사가 아니라 to부정사의 to이므로 뒤에 동사원형이 온다."
S60 = "오답 네 설명이 B와 똑같았다. 또 B 검토 의견(선택지 품질이 원문항보다 낮음)이 이 유형에도 해당해, 원문항처럼 밑줄 친 표현을 작은따옴표로 짚고 이유까지 밝힌 그럴듯한 오개념으로 보기 다섯 개를 새로 썼다. 원문항처럼 ‘지문:’ 표시도 붙였다."
def f60(t, p, items, a, s=S60):
    F(1, 60, t, p="지문: " + p, c=[x for x, _ in items], a=a, r=R60, n=[w + (" 정답이다." if i + 1 == a else " 오답이다.") for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f60("B", "The new medication <u>is likely to reduce</u> the symptoms within a week.", [
    ("'to reduce'는 뒤의 'the symptoms'를 꾸미는 형용사적 용법의 to부정사로, '줄여 줄 증상'이라는 뜻이다.", "to reduce는 명사를 꾸미는 말이 아니라 be likely에 이어져 ‘줄일 것 같다’는 뜻을 이루고, the symptoms는 reduce의 목적어이므로"),
    ("'be likely to'는 가능성이 높다는 추측을 나타내는 표현으로, 여기서 'to'는 to부정사를 이끄는 'to'이므로 뒤에 동사원형 'reduce'가 쓰였다.", "be likely to의 to는 부정사의 to라 뒤에 동사원형이 오고 가능성을 나타낸다는 설명이 옳으므로"),
    ("'likely'는 '비슷한'이라는 뜻의 형용사이므로, 이 문장은 '그 약은 증상을 줄이는 것과 비슷하다'라는 뜻이다.", "likely는 ‘~할 것 같은’이라는 뜻이며 ‘비슷한’(alike, similar)이라는 뜻이 아니므로"),
    ("'to'는 전치사이므로 뒤에 동명사가 와야 하며, 'is likely to reducing'으로 고쳐야 한다.", "be likely to의 to는 전치사가 아니라 부정사의 to라 동사원형 reduce가 맞으므로"),
    ("'within a week'라는 기간 표현이 있으므로 'is likely to reduce' 대신 현재완료 'has reduced'로 써야 한다.", "within a week는 앞으로의 기간을 말하며, 앞으로 일어날 가능성은 is likely to로 나타내므로")], 2,
    "Claude 판정은 ‘적합’이었으나 검토 의견(선택지 품질이 원문항보다 낮음)에 따라 고쳤다. ‘to 뒤에는 명사만 올 수 있다’처럼 짧고 뻔한 오답 대신, 원문항처럼 밑줄 친 표현을 작은따옴표로 짚고 이유까지 밝힌 그럴듯한 오개념(형용사적 용법, likely의 뜻, to를 전치사로 봄, 시간 표현과 시제)으로 보기를 새로 썼다. 원문항처럼 ‘지문:’ 표시를 붙이고 문장을 조금 늘렸다.")
f60("C", "Mina <u>is likely to arrive</u> before noon.", [
    ("'be likely to' 뒤의 'to'는 전치사가 아니라 부정사 표지이므로, 동사원형 'arrive'를 써서 '도착할 가능성이 높다'는 뜻을 나타낸다.", "be likely to의 to는 부정사의 to라 뒤에 동사원형이 오고 가능성을 나타낸다는 설명이 옳으므로"),
    ("'is likely to'는 '~하고 싶어 하다'라는 소망을 나타내므로, 이 문장은 '미나가 정오 전에 도착하고 싶어 한다'라는 뜻이다.", "be likely to는 소망이 아니라 가능성을 나타내므로"),
    ("'likely'는 '-ly'로 끝나는 부사이므로 동사 'arrive'를 꾸며 '그럴듯하게 도착하다'라는 뜻을 만든다.", "likely는 -ly로 끝나도 be동사 뒤에 쓰인 형용사이므로"),
    ("'arrive'는 목적어를 갖지 않는 자동사이므로, 'to'를 빼고 'is likely arrive'로 써야 한다.", "arrive가 자동사여도 be likely 뒤에는 to부정사가 와야 하므로"),
    ("'to arrive'는 '도착하기 위해서'라는 목적을 나타내는 부사적 용법이므로, 문장 뒤에 목적을 이루는 주절이 더 필요하다.", "to arrive는 목적이 아니라 be likely에 이어져 ‘도착할 것 같다’는 뜻을 이루므로")], 1)
f60("D", "The price <u>is likely to rise</u> next month.", [
    ("'likely'는 '가능성'이라는 뜻의 명사이고, 'to rise'는 그 명사를 꾸미는 형용사적 용법이다.", "likely는 명사가 아니라 형용사이고(명사는 likelihood), to rise는 be likely에 이어지는 말이므로"),
    ("'next month'가 미래를 나타내므로, 시제를 맞추려면 'is likely to'를 'was likely to'로 바꿔야 한다.", "next month는 오를 시점이고, 가능성을 판단하는 지금은 현재형 is가 맞으므로"),
    ("'to rise'는 '오르기 위해서'라는 목적을 나타내므로, 이 문장은 '가격이 오르기 위해 그럴듯하다'라는 뜻이다.", "to rise는 목적이 아니라 be likely에 이어져 ‘오를 것 같다’는 뜻을 이루므로"),
    ("'be likely to'는 앞으로 일어날 가능성이 크다는 추측을 나타내고, 이때 'to' 뒤에는 동사원형 'rise'가 온다.", "be likely to의 to는 부정사의 to라 뒤에 동사원형이 오고 가능성을 나타낸다는 설명이 옳으므로"),
    ("'rise'는 자동사이므로, '가격이 올려진다'는 수동의 뜻을 살리려면 'is likely to be risen'으로 써야 한다.", "rise는 자동사라 수동태로 쓸 수 없고, 가격이 스스로 오르는 뜻이므로")], 4)
f60("E", "Tom <u>is likely to miss</u> the last bus tonight.", [
    ("'be likely to'는 과거에 자주 하던 일을 나타내므로, 이 문장은 'Tom이 막차를 놓치곤 했다'라는 뜻이다.", "과거의 습관은 used to로 나타내며, be likely to는 앞으로의 가능성을 나타내므로"),
    ("'to miss'는 뒤의 'the last bus'를 꾸미는 형용사적 용법이므로 '놓칠 막차'라는 뜻이다.", "to miss는 명사를 꾸미는 말이 아니라 be likely에 이어지고, the last bus는 miss의 목적어이므로"),
    ("'likely to'의 'to'는 to부정사의 'to'이므로 뒤에 동사원형 'miss'가 쓰였고, 문장은 '놓칠 가능성이 높다'는 뜻이다.", "be likely to의 to는 부정사의 to라 뒤에 동사원형이 오고 가능성을 나타낸다는 설명이 옳으므로"),
    ("'likely'가 형용사이므로 그 뒤에는 동명사가 와야 하며, 'is likely missing'으로 고쳐야 한다.", "be likely 뒤에는 동명사가 아니라 to부정사가 오므로"),
    ("'be likely to'는 의무를 나타내므로, 이 문장은 'Tom이 막차를 놓쳐야 한다'라는 뜻이다.", "의무는 must나 have to로 나타내며, be likely to는 가능성을 나타내므로")], 3,
    S60 + " 원문항과 거의 같던 문장(… is likely to win …)은 is likely to miss the last bus로 바꿨다.")
f60("F", "The weather <u>is likely to improve</u> tomorrow.", [
    ("'tomorrow'가 있으므로 미래의 일을 나타내려면 'to improve' 대신 동명사 'improving'을 써야 한다.", "시간 표현은 to부정사의 형태와 관계없고, be likely to 뒤에는 동사원형이 오므로"),
    ("'likely to'의 'to'는 방향을 나타내는 전치사라서, 'improve'는 '개선'이라는 뜻의 명사로 쓰였다.", "이 to는 전치사가 아니고 improve는 명사가 아닌 동사원형이므로(명사는 improvement)"),
    ("'be likely to'는 '~하기를 원하다'라는 뜻이라서, 사람이 아닌 'The weather'를 주어로 쓸 수 없다.", "be likely to는 바람이 아니라 가능성을 나타내므로 사물 주어와도 쓰므로"),
    ("'to improve'는 '좋아지기 위해서'라는 목적을 나타내는 부사적 용법이다.", "to improve는 목적이 아니라 be likely에 이어져 ‘좋아질 것 같다’는 뜻을 이루므로"),
    ("'be likely to + 동사원형'은 어떤 일이 일어날 가능성이 높음을 나타내며, 'improve'는 'to' 뒤에 온 동사원형이다.", "be likely to의 to는 부정사의 to라 뒤에 동사원형이 오고 가능성을 나타낸다는 설명이 옳으므로")], 5)


# ---- 2차 감수(2026-10) 추가 ----
# 1-53 B: 틀린 문장만 길고 worth가 옳은 문장·틀린 문장에 함께 나옴, 밑줄 범위가 원문항보다 좁음
F(1, 53, "B", r=R53, a=1,
  c=["Tom <u>is worth to meet</u> if you visit the city.", "I <u>am looking forward to seeing</u> the new movie.", "The team <u>had trouble finding</u> the stadium.", "Leo <u>succeeded in fixing</u> the old radio.", "Mina <u>is busy preparing</u> for the school festival."],
  n=["be worth 뒤에는 동명사를 쓴다. is worth meeting으로 고쳐야 하므로 정답이다.", ok53("look forward to"), ok53("have trouble"), ok53("succeed in"), ok53("be busy")],
  s="틀린 문장 ①만 길어 길이만 보고 고를 수 있었고, worth가 틀린 문장(①)과 옳은 문장(③)에 함께 나와 대비 단서가 되었다. ③ ‘The museum is worth visiting.’은 원문항 ①과도 같았다. 옳은 문장 네 개를 원문항 길이의 새 문장으로 바꾸고, 밑줄을 원문항처럼 ‘표현 + 동사 형태’ 전체에 그었다.")

# 1-54 B: 문장이 원문항의 절반 길이
F(1, 54, "B", r=R54, a=4,
  c=["Tom considered moving to a smaller town near the sea.", "Mina avoided answering the reporter's question about her plans.", "Jane postponed making the final decision until Friday.", "Leo denied to take the money from the drawer.", "We finished cleaning the room before our parents came home."],
  n=[ok54("consider"), ok54("avoid"), ok54("postpone"), bad54("deny", "denied taking"), ok54("finish")],
  s="문장이 서너 낱말로 원문항(7~10낱말)의 절반 길이였다. 같은 동사와 정답을 유지하면서 문장마다 꾸미는 말을 붙여 원문항 길이로 늘렸다.")
