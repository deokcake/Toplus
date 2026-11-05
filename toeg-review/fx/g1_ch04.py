# 1급 CH4 수동태 (31~40) 수정 예시

# 1-31 B 검토 의견(본문이 기준 문항에 비해 너무 짧음) 반영: 두 문장을 원문항 길이로, 한 줄에 한 문장
def f31(t, lines, c, a, pair, r, s, **kw):
    F(1, 31, t, st="R", p="\n".join(lines), c=c, a=a, r=r, k=f"{pair}이므로 {c[a-1]}가 알맞다.", n="combo", s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
f31("B", ["Jane is known _____ her honesty and kindness among her classmates.", "The small kitchen was filled _____ smoke after the toast burned."],
    ["for - with", "about - of", "for - of", "with - in", "in - with"], 1, "be known for(~으로 알려져 있다), be filled with(~로 가득 차다)",
    "be known for는 무엇으로 알려져 있는지를, be filled with는 무엇으로 가득 찼는지를 나타낸다.",
    "Claude 판정은 ‘적합’이었으나 검토 의견(본문이 기준 문항에 비해 너무 짧음)에 따라, 원문항처럼 두 문장에 꾸며 주는 말을 붙여 원문항 길이로 늘리고 줄 앞의 ‘-’ 표시를 지웠다. 보기와 정답은 그대로다.")
f31("C", ["Many residents in this area are worried _____ the rising rent.", "The narrow hallway was crowded _____ visitors on the opening day."],
    ["in - with", "with - in", "for - of", "about - of", "about - with"], 5, "be worried about(~을 걱정하다), be crowded with(~로 붐비다)",
    "be worried about은 걱정하는 대상을, be crowded with는 무엇으로 붐비는지를 나타낸다.",
    "B 검토 의견(본문이 기준 문항에 비해 너무 짧음)이 이 유형에도 해당해, 두 문장을 원문항 길이로 늘리고 ‘/’로 이어 쓴 두 문장을 두 줄로 나눴다. 보기와 정답은 그대로다.")
f31("D", ["Mina is very proud _____ her brother, who won the national science contest.", "The stadium was packed _____ excited fans before the final match."],
    ["of - with", "for - of", "about - of", "of - of", "with - in"], 1, "be proud of(~을 자랑스러워하다), be packed with(~로 가득 차다)",
    "be proud of는 자랑스러워하는 대상을, be packed with는 무엇으로 가득 찼는지를 나타낸다.",
    "첫 문장 ‘interested in’이 원문항과 같고 정답 짝(in - with)도 같아서, 첫 문장을 ‘proud of’로 바꿔 정답을 of - with로 만들었다. B 검토 의견(본문이 너무 짧음)도 이 유형에 해당해 두 문장을 원문항 길이로 늘리고 두 줄로 나눴다.")
f31("E", ["Tom is not satisfied _____ the result of his final exam.", "The main street was lined _____ tall trees on both sides."],
    ["for - by", "with - with", "in - with", "about - by", "with - in"], 2, "be satisfied with(~에 만족하다), be lined with(~이 줄지어 있다)",
    "be satisfied with는 만족하는 대상을, be lined with는 무엇이 줄지어 있는지를 나타낸다.",
    "발문에 붙은 ‘첫 문장은 Tom이 결과에 만족한다는 뜻이다’를 지워 원문항 발문으로 되돌렸다. B 검토 의견(본문이 너무 짧음)도 이 유형에 해당해 두 문장을 원문항 길이로 늘리고(둘째 문장은 B와 겹치지 않게 lined with로 바꿈) 두 줄로 나눴다. 보기와 정답은 그대로다.")
f31("F", ["The kids were surprised _____ the size of the huge whale.", "The old wooden shelf was loaded _____ dusty books and magazines."],
    ["with - in", "in - with", "at - with", "for - of", "at - of"], 3, "be surprised at(~에 놀라다), be loaded with(~이 가득 실려 있다)",
    "be surprised at은 놀란 대상을, be loaded with는 무엇이 가득 실려 있는지를 나타낸다.",
    "둘째 문장(The train was crowded with commuters)이 원문항 문장과 거의 같았고, B 검토 의견(본문이 너무 짧음)도 이 유형에 해당해 두 문장을 원문항 길이로 새로 썼다. 정답 짝은 at - with로 바뀌었다.")

# 1-32 조동사 수동태: 발문 조건 삭제
for t in "CDEF":
    F(1, 32, t, st="R", s="발문의 ‘원문의 의미와 시제·상(단순/진행)을 그대로 유지하여’ 조건을 지워 원문항 발문으로 되돌렸다. 문장과 보기는 그대로다.")

# 1-33 줄바꿈 복원
for t in "CDEF":
    F(1, 33, t, p=V(1, 33, t)["passage"].replace(" → ", "\n→ "), keepx=True, s="원문항처럼 능동문과 ‘→ 수동문’을 두 줄로 나눴다. 문장과 정답은 그대로다.")

# 1-34 is said/believed + 완료 수동 부정사
R34 = "주어 + is said/believed/thought + to부정사는 ‘주어가 ~한다고 여겨진다’는 뜻이다. 전해지는 일이 말하는 시점보다 먼저 일어났으면 완료부정사를, 주어가 그 일을 당했으면 to have been + 과거분사를 쓴다."
F(1, 34, "B", p="Experts say that the species was discovered recently.\n= The species is said _____ discovered recently.",
  c=["was", "having", "to have been", "will be", "that is"], a=3, r=R34,
  n=["is said 뒤에 다시 동사 was가 올 수 없다. is said 뒤에는 to부정사가 온다.", "is said 뒤에는 분사가 아니라 to부정사가 온다.",
     "발견된 일이 말하는 시점보다 먼저이고 주어가 발견된 것이므로 to have been + discovered가 알맞다. 정답이다.", "will be는 미래를 나타내 과거에 발견된 일과 맞지 않고, is said 뒤에 올 수도 없다.",
     "is said 뒤에 that절을 이으면 주어 The species와 구조가 맞지 않는다."],
  s="보기 다섯 개가 과거분사까지 포함한 긴 구로 바뀌어 원문항(빈칸 뒤에 과거분사가 있고 조동사 부분만 고름)과 형태가 달랐다. 원문항처럼 빈칸 뒤에 discovered를 두고 보기를 짧은 형태로 바꿨으며, 어색한 ‘by experts’ 위치도 없앴다.")
F(1, 34, "C", p="People say that the manuscript was written in the 15th century.\n= The manuscript is said _____ written in the 15th century.",
  c=["to be", "to have been", "being", "had been", "that was"], a=2, r=R34,
  n=["to be written은 말하는 지금의 상태로 읽혀 15세기에 쓰인 과거의 일과 시점이 맞지 않는다.", "쓰인 일이 말하는 시점보다 먼저이고 원고가 쓰인 것이므로 to have been + written이 알맞다. 정답이다.",
     "is said 뒤에는 -ing형이 아니라 to부정사가 온다.", "is said 뒤에 다시 동사 had been이 올 수 없다.", "is said 뒤에 that절을 이으면 주어 The manuscript와 구조가 맞지 않는다."],
  s="보기를 원문항처럼 빈칸 뒤 과거분사(written) 앞에 들어갈 짧은 형태로 바꿨다. 정답 to have been은 그대로다.")
def inf34(x, pp, when):
    if x == f"to have been {pp}": return f"{when} 일어난 일이고 주어가 그 일을 당했으므로 완료 수동 부정사 to have been {pp}가 알맞다. 정답이다."
    if x == f"to have {pp}": return f"to have {pp}: 완료부정사이지만 능동이라 주어가 그 일을 당한 관계를 나타내지 못한다."
    if x == f"to be {pp}": return f"to be {pp}: 단순 수동 부정사라 믿는 지금과 같은 때의 일로 읽힌다. 과거의 일에는 완료부정사가 필요하다."
    if x == f"having been {pp}": return f"having been {pp}: is believed/thought 뒤에는 분사구가 아니라 to부정사가 와야 한다."
    return f"{x}: 진행 능동 부정사라 수동 관계와 과거 시점을 모두 나타내지 못한다."
S34 = "오답 네 개가 C 문항의 동사 write를 그대로 써서 지문 동사와 맞는 보기는 정답뿐이었다. 오답을 지문 동사 {}의 다른 형태로 바꿨다."
for t, c, a, pp, when, v in [
    ("D", ["to have built", "to have been built", "having been built", "to be built", "to be building"], 2, "built", "로마인이 지은 것은 믿는 지금보다 먼저", "build"),
    ("E", ["to be stealing", "having been stolen", "to have stolen", "to have been stolen", "to be stolen"], 4, "stolen", "그림을 도둑맞은 것은 몇 년 전에", "steal"),
    ("F", ["having been destroyed", "to have destroyed", "to have been destroyed", "to be destroyed", "to be destroying"], 3, "destroyed", "마을이 불탄 것은 믿는 지금보다 먼저", "destroy")]:
    F(1, 34, t, c=c, a=a, r=R34, n=[inf34(x, pp, when) for x in c], s=S34.format(v) + (f" 정답 위치 {'①②③④⑤'[a-1]}." if a != 2 else ""))

# 1-35 능동 → 수동 전환 쌍에서 틀린 문장 고르기
R35 = "ask·tell·advise·order·allow + 목적어 + to부정사를 수동태로 바꾸면 be + 과거분사 뒤에 to부정사를 그대로 둔다. call off, look into, take care of 같은 구동사는 수동태에서도 전치사·부사를 빠뜨리지 않는다."
def pair(a, b): return f"{a}\n→ {b}"
c = ["a, b, c", "b, d, e", "a, c, d", "c, d, e", "a, b, e"]
F(1, 35, "B", r=R35, c=c, a=2,
  p="a) " + pair("The librarian permitted us to use the meeting room.", "We were permitted to use the meeting room by the librarian.") + "\nb) " + pair("The teacher asked us to submit the reports.", "We were asked to submitting the reports by the teacher.")
    + "\nc) " + pair("The organizers put off the outdoor concert.", "The outdoor concert was put off by the organizers.") + "\nd) " + pair("The coach instructed the players to warm up.", "The players were instructed warming up by the coach.")
    + "\ne) " + pair("The nurse took care of the patient.", "The patient was taken care by the nurse."),
  pre=["문장별 판정:", "a) 옳음: were permitted 뒤에 to use를 그대로 두었다.", "b) 틀림: were asked 뒤에는 to + 동사원형이 온다. to submitting → to submit.",
       "c) 옳음: 구동사 put off를 그대로 두었다.", "d) 틀림: were instructed 뒤에는 to부정사가 온다. warming up → to warm up.", "e) 틀림: take care of의 of를 빠뜨렸다. taken care → taken care of."],
  k="어법상 틀린 문장은 b, d, e이다.", n=setnotes(c, "b, d, e"),
  s="문장 구성·오류 위치(a, c, e)·선택지·정답 위치(⑤)가 원문항과 똑같아 읽지 않고도 답할 수 있었다. 문장 순서를 바꿔 틀린 문장을 b, d, e로 옮기고, 선택지 조합도 새로 만들었다.")
S35 = "원문항은 각 항목을 ‘능동문 → 수동문’ 두 줄로 제시하는데 변형은 수동문만 주었고, 평가 요소도 사역·지각동사로 바뀌었다. 원문항처럼 5형식 to부정사·구동사 수동태를 능동문 → 수동문 쌍으로 새로 쓰고, 정답 조합을 원문항(a, c, e)과 다르게 했다."
c = ["a, b, c", "b, c, e", "a, d, e", "b, d, e", "a, c, d"]
F(1, 35, "C", r=R35, c=c, a=2,
  p="a) " + pair("My parents encouraged me to join the club.", "I was encouraged to join the club by my parents.") + "\nb) " + pair("The police looked for the missing child.", "The missing child was looked by the police.")
    + "\nc) " + pair("The teacher told us to be quiet.", "We were told being quiet by the teacher.") + "\nd) " + pair("They turned down my offer.", "My offer was turned down by them.")
    + "\ne) " + pair("The doctor ordered him to stay in bed.", "He was ordered stay in bed by the doctor."),
  pre=["문장별 판정:", "a) 옳음: was encouraged 뒤에 to join을 그대로 두었다.", "b) 틀림: look for의 for를 빠뜨렸다. was looked → was looked for.",
       "c) 틀림: were told 뒤에는 to부정사가 온다. being quiet → to be quiet.", "d) 옳음: 구동사 turn down을 그대로 두었다.", "e) 틀림: was ordered 뒤에는 to부정사가 온다. stay → to stay."],
  k="어법상 틀린 문장은 b, c, e이다.", n=setnotes(c, "b, c, e"), s=S35 + " 정답 b, c, e.")
c = ["b, c, d", "a, b, e", "c, d, e", "a, d, e", "a, b, c"]
F(1, 35, "D", r=R35, c=c, a=4,
  p="a) " + pair("The guide warned the tourists to stay together.", "The tourists were warned staying together by the guide.") + "\nb) " + pair("Grandma brought up three children.", "Three children were brought up by Grandma.")
    + "\nc) " + pair("The coach expected the team to win.", "The team was expected to win by the coach.") + "\nd) " + pair("The workers put out the fire.", "The fire was put by the workers.")
    + "\ne) " + pair("The students laughed at the joke.", "The joke was laughed by the students."),
  pre=["문장별 판정:", "a) 틀림: were warned 뒤에는 to부정사가 온다. staying → to stay.", "b) 옳음: 구동사 bring up을 그대로 두었다.",
       "c) 옳음: was expected 뒤에 to win을 그대로 두었다.", "d) 틀림: put out의 out을 빠뜨렸다. was put → was put out.", "e) 틀림: laugh at의 at을 빠뜨렸다. was laughed → was laughed at."],
  k="어법상 틀린 문장은 a, d, e이다.", n=setnotes(c, "a, d, e"), s=S35 + " 정답 a, d, e(정답 위치 ④).")
c = ["a, b, c", "b, c, d", "c, d, e", "a, c, e", "b, d, e"]
F(1, 35, "E", r=R35, c=c, a=3,
  p="a) " + pair("The manager allowed Tom to leave early.", "Tom was allowed to leave early by the manager.") + "\nb) " + pair("Everyone looked up to the old teacher.", "The old teacher was looked up to by everyone.")
    + "\nc) " + pair("The judge forced the man to pay the fine.", "The man was forced paying the fine by the judge.") + "\nd) " + pair("The students handed in their reports.", "Their reports were handed by the students.")
    + "\ne) " + pair("Mom asked me to buy some eggs.", "I was asked buy some eggs by Mom."),
  pre=["문장별 판정:", "a) 옳음: was allowed 뒤에 to leave를 그대로 두었다.", "b) 옳음: 구동사 look up to를 그대로 두었다.",
       "c) 틀림: was forced 뒤에는 to부정사가 온다. paying → to pay.", "d) 틀림: hand in의 in을 빠뜨렸다. were handed → were handed in.", "e) 틀림: was asked 뒤에는 to부정사가 온다. buy → to buy."],
  k="어법상 틀린 문장은 c, d, e이다.", n=setnotes(c, "c, d, e"), s=S35 + " 정답 c, d, e(정답 위치 ③).")
c = ["a, b, d", "a, c, e", "b, c, d", "b, d, e", "a, b, c"]
F(1, 35, "F", r=R35, c=c, a=1,
  p="a) " + pair("The librarian advised the kids to return the books on time.", "The kids were advised to returning the books on time by the librarian.") + "\nb) " + pair("The city carried out the plan.", "The plan was carried by the city.")
    + "\nc) " + pair("Our neighbors invited us to have dinner.", "We were invited to have dinner by our neighbors.") + "\nd) " + pair("The staff dealt with the complaint quickly.", "The complaint was dealt quickly by the staff.")
    + "\ne) " + pair("The police ordered the driver to stop.", "The driver was ordered to stop by the police."),
  pre=["문장별 판정:", "a) 틀림: were advised 뒤에는 to + 동사원형이 온다. to returning → to return.", "b) 틀림: carry out의 out을 빠뜨렸다. was carried → was carried out.",
       "c) 옳음: were invited 뒤에 to have를 그대로 두었다.", "d) 틀림: deal with의 with를 빠뜨렸다. was dealt → was dealt with.", "e) 옳음: was ordered 뒤에 to stop을 그대로 두었다."],
  k="어법상 틀린 문장은 a, b, d이다.", n=setnotes(c, "a, b, d"), s=S35 + " 정답 a, b, d(정답 위치 ①).")

# 1-36 배열: 발문 조건 삭제, 오답을 제시어 어순만 바꾼 배열로
R36 = "주어 + be동사 + 과거분사 + 전치사구(with/for + 명사) 어순으로 쓴다."
BEV = "be동사와 과거분사의 순서가 뒤바뀌었다. 주어 + be동사 + 과거분사 어순이어야 하므로 오답이다."
PREP = "전치사가 목적어 뒤로 갔다. 전치사 + 명사 순서여야 하므로 오답이다."
PPEND = "과거분사가 문장 끝으로 갔다. be동사 바로 뒤에 과거분사가 와야 하므로 오답이다."
FRONT = "문장 앞에 과거분사를 두어 평서문 어순(주어 + 동사)이 깨졌으므로 오답이다."
S36 = "발문에 ‘형태 변화 없이 각각 한 번씩, 주어 + be동사 순서의 기본 평서문’ 조건이 붙었고, 오답이 제시어에 없는 낱말(by, -ing형 등)을 써서 조건만으로 지워졌다. 발문을 원문항과 같게 하고, 오답을 원문항처럼 제시어의 어순만 바꾼 배열로 새로 만들었다."
def f36(t, c, a, notes, extra=""):
    F(1, 36, t, st="R", c=c, a=a, r=R36, n=[("주어 + be동사 + 과거분사 + 전치사구 어순이 바르다. 정답이다." if i + 1 == a else notes[i]) for i in range(5)], s=S36 + extra)
f36("B", ["They satisfied were with the result.", "They were the result satisfied with.", "Satisfied with they were the result.", "They were satisfied with the result.", "They were satisfied the result with."], 4,
    [BEV, PPEND, FRONT, None, PREP], " 정답 위치 ④.")
f36("C", ["The room was filled with excitement.", "The room filled was with excitement.", "The room was filled excitement with.", "Filled with excitement the room was.", "The room with excitement was filled."], 1,
    [None, BEV, PREP, FRONT, PPEND])
f36("D", ["The mountain covered was with snow.", "The mountain was with snow covered.", "The mountain was covered with snow.", "Covered the mountain was with snow.", "The mountain was covered snow with."], 3,
    [BEV, PPEND, None, FRONT, PREP], " 정답 위치 ③.")
f36("E", ["She known is for her kindness.", "She is for her kindness known.", "Known is she for her kindness.", "She is known her kindness for.", "She is known for her kindness."], 5,
    [BEV, PPEND, FRONT, PREP, None], " 정답 위치 ⑤.")
f36("F", ["The station crowded was with passengers.", "The station was crowded with passengers.", "The station was crowded passengers with.", "The station was with passengers crowded.", "Crowded was the station with passengers."], 2,
    [BEV, None, PREP, PPEND, FRONT], " 정답 위치 ②.")

# 1-37 과거 수동태로 바꾸기
R37 = "단순과거 능동문을 수동태로 바꿀 때 목적어를 주어로 옮기고 was/were + 과거분사를 쓴다. 능동문에 드러난 행위자는 by + 행위자로 남기고, 없던 행위자를 새로 넣지 않는다."
F(1, 37, "B", c=["The old pier destroyed last night.", "The old pier was destroyed by a storm last night.", "The old pier was destroying last night.", "The old pier is destroyed last night.", "The old pier was destroyed by someone last night."], a=2, r=R37,
  n=["be동사가 없어 부두가 스스로 파괴한 능동문이 되었다. 오답이다.", "was destroyed로 과거 수동을 만들고 행위자 by a storm도 살려 원래 문장과 뜻이 같다. 정답이다.",
     "was destroying은 과거진행 능동형이라 부두가 파괴를 당한 뜻이 아니다. 오답이다.", "is destroyed는 현재형이라 last night와 맞지 않는다. 오답이다.",
     "행위자가 폭풍(a storm)인데 by someone으로 바꿔 뜻이 달라졌다. 오답이다."],
  s="능동문 주어가 ‘A storm’인데 정답이 행위자를 빼서 ‘뜻이 같은 문장’이라 하기 어려웠다. 정답을 ‘was destroyed by a storm last night’으로 바꾸고, 행위자를 someone으로 바꾼 오답을 넣었다.")
F(1, 37, "D", p="Someone locked the gate after the concert.",
  c=["The gate locked after the concert.", "The gate is locked after the concert.", "The gate was locked after the concert.", "The gate was locking after the concert.", "The gate had locked after the concert."], a=3, r=R37,
  n=["be동사가 없어 문이 스스로 잠근 능동문이 되었다. 오답이다.", "is locked는 현재형이라 과거에 일어난 일과 시제가 맞지 않는다. 오답이다.",
     "행위자 Someone은 생략하고 was locked로 과거 수동을 바르게 만들었다. 정답이다.", "was locking은 과거진행 능동형이라 문이 잠긴 뜻이 아니다. 오답이다.",
     "had locked는 과거완료 능동형이라 수동 관계를 나타내지 못한다. 오답이다."],
  s="동사(stole)와 정답 문장이 원문항(My wallet was stolen …)과 거의 같아 ‘Someone locked the gate after the concert.’로 동사와 상황을 바꿨다.")
for t in "EF":
    F(1, 37, t, st="R", okx=True, s="발문의 ‘시제와 행위자 정보를 모두 유지하여’ 조건을 지워 원문항 발문으로 되돌렸다. 조건이 없어도 행위자가 드러난 능동문이라 정답은 같다.")

# 1-38 사물 목적어를 주어로 하는 수동태
R38 = "4형식 문장의 사물 목적어를 주어로 수동태를 만들면 be + 과거분사 뒤 사람 앞에 전치사(to)를 쓴다. 과거 문장이면 was/were를 쓴다."
def dat(x, pp, person, subj):
    if x == f"was {pp} to {person}": return f"과거 능동문이므로 was {pp}, 사람 앞에는 to를 붙인 was {pp} to {person}가 알맞다. 정답이다."
    if x.startswith("has "): return f"{x}: 현재완료 능동형이라 주어({subj})가 받은 것이 되는 수동 관계를 나타내지 못한다."
    if x.startswith("had "): return f"{x}: 과거완료 능동형이라 수동 관계를 나타내지 못한다."
    if x.startswith("was ") and x.split()[1].endswith("ing"): return f"{x}: 과거진행 능동형이라 수동 관계를 나타내지 못한다."
    return f"{x}: 현재 수동이라 과거 문장의 시제와 맞지 않는다."
S38 = "발문이 길게 바뀌고 빈칸 밑줄이 사라졌으며, 보기에서 사람이 빠져 원본 형식과 달랐다. 원문항처럼 “‘{}’{} 주어로 하는 수동태 문장으로 바꿀 때”로 발문을 고치고, 밑줄 빈칸과 사람이 들어간 보기로 되돌렸다. 없는 형태(was send to 등) 오답도 실제 형태로 바꿨다."
def f38(t, subj, act, pas, pp, person, c, a):
    jo = "를" if subj in ("The award",) else "을"  # 영어 낱말의 끝소리에 맞춘 조사
    st = f"다음 문장을 ‘{subj}’{jo} 주어로 하는 수동태 문장으로 바꿀 때, 빈칸에 들어갈 말로 가장 알맞은 것을 고르시오."
    F(1, 38, t, st=st, p=f"- {act}\n- {pas}", c=c, a=a, r=R38, n=[dat(x, pp, person, subj) for x in c], s=S38.format(subj, jo) + f" 정답 위치 {'①②③④⑤'[a-1]}.")
B_ = "(<u>        </u>)"
f38("B", "The certificate", "The teacher sent Jane a certificate.", f"The certificate {B_} by the teacher.", "sent", "Jane", ["has sent Jane", "was sending Jane", "was sent to Jane", "had sent Jane", "is sent Jane"], 3)
f38("C", "The scholarship", "The university offered Mina a scholarship for academic excellence.", f"The scholarship {B_} for academic excellence by the university.", "offered", "Mina",
    ["was offered to Mina", "has offered Mina", "was offering Mina", "is offered Mina", "had offered Mina"], 1)
f38("D", "The award", "The company gave Tom an award for his service.", f"The award {B_} for his service by the company.", "given", "Tom",
    ["had given Tom", "is given Tom", "was giving Tom", "has given Tom", "was given to Tom"], 5)
f38("E", "The rare painting", "The museum showed us a rare painting.", f"The rare painting {B_} by the museum.", "shown", "us",
    ["was showing us", "was shown to us", "has shown us", "is shown us", "had shown us"], 2)
f38("F", "Permission", "The committee granted Leo permission to enter the lab.", f"Permission {B_} to enter the lab by the committee.", "granted", "Leo",
    ["is granted Leo", "had granted Leo", "was granting Leo", "was granted to Leo", "has granted Leo"], 4)

# 1-39 지각동사 수동태 용어: 발문 복원, 오답 (A)를 지문 동사의 다른 형태로
NEED39 = ["능동태에서 지각동사 뒤 목적격 보어로는 동사원형을 쓴다.", "수동태가 되면 동사원형이 to부정사로 바뀐다.", "진행 중인 장면이면 현재분사를 그대로 쓸 수 있다."]
S39 = "오답 네 개가 C 문항의 동사 cheer를 그대로 써서 지문 동사와 맞는 보기는 정답뿐이었다. 오답의 (A)를 지문 동사 {}의 다른 형태로 바꾸고, 발문을 원문항과 같게 했다."
U3 = lambda x: f"(<u>    {x}    </u>)"
P39 = {
 "B": f"지문: <u>The dog was seen to jump over the fence.</u>\n설명: 위 문장은 능동태 문장 'Tom saw the dog {U3('A')} over the fence'를 수동태로 바꾼 것이다. 능동태에서 지각동사 see의 목적격 보어 자리에 ( A )가 오면, 수동태 문장에서는 이 보어가 {U3('B')}의 형태로 바뀌어 be seen 뒤에 놓인다. 능동태에서 보이지 않던 to가 수동태에서 드러나는 것이 이 구문의 핵심이다. 한편 개가 울타리를 뛰어넘고 있는 순간을 생생하게 묘사하려고 능동태에서 {U3('C')}를 보어로 썼다면, 수동태에서도 그 형태를 바꾸지 않고 그대로 쓴다.",
 "C": f"지문: <u>The audience was heard to cheer loudly.</u>\n설명: 위 문장의 능동태는 'The reporter heard the audience {U3('A')} loudly'이다. 지각동사 hear가 목적격 보어로 ( A )를 취한 문장을 수동태로 만들면, 그 보어는 be heard 뒤에서 {U3('B')}로 형태가 달라진다. 수동태 문장만 보고 능동태의 보어를 되살릴 때는 to를 떼어 내면 된다. 다만 관중이 환호하고 있던 장면 자체를 전하려고 능동태에서 {U3('C')}를 보어로 쓴 경우라면, 수동태로 바꾸어도 그 형태가 그대로 남는다.",
 "D": f"지문: <u>The child was seen to cross the road.</u>\n설명: 이 문장은 'Someone saw the child {U3('A')} the road'라는 능동태 문장에서 출발한다. 능동태에서 지각동사 see 뒤의 목적어를 설명하는 보어로 ( A )가 쓰였다면, 목적어 the child가 주어로 나간 수동태에서는 그 보어를 {U3('B')}로 써야 한다. 그래서 수동태 문장에는 능동태에 없던 to가 보이게 된다. 아이가 길을 건너는 중이었다는 진행의 느낌을 살리려고 능동태에서 {U3('C')}를 썼다면, 수동태에서도 형태를 바꿀 필요가 없다.",
 "E": f"지문: <u>Mina was heard to sing in the hall.</u>\n설명: 능동태로 되돌리면 'We heard Mina {U3('A')} in the hall'이 된다. 지각동사 hear는 능동태에서 목적격 보어로 ( A )를 쓸 수 있지만, 이 문장을 수동태로 바꾸면 보어는 {U3('B')}의 모양을 갖추어야 한다. 곧, 능동태에서 생략되어 있던 to가 수동태에서 되살아나는 셈이다. 그러나 미나가 노래를 부르고 있는 도중이었다는 점을 강조하려고 능동태에서 {U3('C')}를 보어로 골랐다면, 수동태에서도 그 보어는 그대로 유지된다.",
 "F": f"지문: <u>The students were heard to laugh loudly during the break.</u>\n설명: 위 문장에 해당하는 능동태 문장은 'The teacher heard the students {U3('A')} loudly during the break'이다. 능동태에서 지각동사 hear 다음의 목적격 보어가 ( A )였다면, 학생들이 주어가 되는 수동태에서는 이 보어를 반드시 {U3('B')}로 바꾸어 써야 한다. 이 차이 때문에 수동태 문장에서는 were heard 바로 뒤에 to가 붙은 형태가 나타난다. 다만 학생들이 웃고 있는 모습을 진행 중인 장면으로 그리려고 능동태에서 {U3('C')}를 보어로 썼다면, 수동태로 바꾸어도 그 형태를 그대로 둔다."}
L39B = "검토 의견(원문항에 비해 지문이 너무 짧음)에 따라 설명을 원문항처럼 네 문장으로 늘리고, 빈칸을 원문항처럼 밑줄 표시로 바꿨다. "
L39 = "B 검토 의견(원문항에 비해 지문이 너무 짧음)이 이 유형에도 해당해, 설명을 원문항처럼 네 문장으로 늘리고 빈칸을 원문항처럼 밑줄 표시로 바꿨다. "
def f39(t, c, a, v, s=None):
    F(1, 39, t, st="R", p=P39[t], c=c, a=a, n=tnotes(c, a, NEED39, labs=["(A)", "(B)", "(C)"]), s=(L39B if t == "B" else L39) + (s or S39.format(v)) + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f39("B", ["(A) jump - (B) to부정사 - (C) 현재분사", "(A) jumping - (B) 동명사 - (C) 과거분사", "(A) to jump - (B) 과거분사 - (C) 동명사", "(A) jumped - (B) to부정사 - (C) 과거분사", "(A) jump - (B) 원형부정사 - (C) 형용사"], 1, "jump")
f39("C", V(1, 39, "C")["c"], int(V(1, 39, "C")["ans"]), "cheer", s="발문도 원문항 ‘지각동사의 수동태에 대한 문법 설명이다. 밑줄 친 문장에 근거하여 (A)~(C)에 들어갈 용어를 바르게 나열한 것’으로 되돌렸다. 보기와 정답은 그대로다.")
f39("D", ["(A) to cross - (B) 원형부정사 - (C) 형용사", "(A) cross - (B) 과거분사 - (C) 동명사", "(A) crossed - (B) to부정사 - (C) 과거분사", "(A) crossing - (B) 동명사 - (C) 과거분사", "(A) cross - (B) to부정사 - (C) 현재분사"], 5, "cross")
f39("E", ["(A) sing - (B) to부정사 - (C) 현재분사", "(A) sang - (B) to부정사 - (C) 과거분사", "(A) sing - (B) 과거분사 - (C) 동명사", "(A) to sing - (B) 원형부정사 - (C) 형용사", "(A) singing - (B) 동명사 - (C) 과거분사"], 1, "sing")
f39("F", ["(A) to laugh - (B) 원형부정사 - (C) 형용사", "(A) laughed - (B) to부정사 - (C) 과거분사", "(A) laughing - (B) 동명사 - (C) 과거분사", "(A) laugh - (B) to부정사 - (C) 현재분사", "(A) laugh - (B) 과거분사 - (C) 동명사"], 4, "laugh")

# 1-40 사역동사 make 능동/수동 보어 차이: 그럴듯한 오개념 오답을 유형마다 새로
R40 = "사역동사 make + 목적어 + 원형부정사를 수동태로 바꾸면 be made + to부정사가 된다. to의 유무는 시제·목적어의 종류·동사의 자타가 아니라 능동과 수동 구조의 차이에서 생긴다."
S40 = "오답이 ‘make는 수동태로 전환할 수 없다’처럼 뻔히 틀려 변별력이 낮았고 C~F가 B와 오답 네 개를 공유했다. 원문항처럼 시제·목적어의 종류·부사적 용법·자동사/타동사 같은 그럴듯한 오개념으로 유형마다 오답을 새로 썼다."
L40 = ' B 검토 의견(지문이 너무 짧음)이 이 유형에도 해당해 원문항처럼 앞뒤 상황을 넣어 두 문장을 원문항 길이로 늘렸다.'
OKN = "능동의 make + 목적어 + 원형부정사가 수동태 be made가 되면서 to가 다시 나타난다는 설명이 정확하다. 정답이다."
F(1, 40, "B", r=R40, a=2, p='At the busy restaurant, the manager (A)<u>made Mina stay late</u> to clean the kitchen. The next weekend, Mina (B)<u>was made to stay late</u> again because two workers were sick.',
  c=["(A)는 과거 시제라 원형부정사를 쓰고, (B)는 수동태라 시제를 나타내려고 to부정사를 썼다.",
     "(A)는 ‘make + 목적어 + 원형부정사’ 구조의 능동태이고, (B)는 이 구조가 수동태가 되면서 목적격 보어 앞에 to가 다시 나타난 것이다.",
     "(B)의 to stay는 ‘머물기 위해’라는 목적을 나타내는 부사적 용법이라 (A)의 stay와 기능이 다르다.",
     "(A)의 목적어 Mina는 사람이라 원형부정사를 쓰고, (B)는 Mina가 주어가 되었으므로 to부정사를 쓴다.",
     "stay는 자동사라 능동태에서는 원형을 쓰지만, 수동태가 되면 타동사처럼 쓰여 to부정사를 취한다."],
  n=["(A)와 (B) 모두 과거 시제이며, to는 시제가 아니라 수동 구조 때문에 나타난다.", OKN, "to stay는 목적이 아니라 be made의 보어이다. ‘머물게 되었다’는 뜻이다.",
     "목적어가 사람이든 사물이든 make의 능동 보어는 원형부정사이다. 주어가 된 것이 이유가 아니다.", "stay의 자동사·타동사 성질은 바뀌지 않는다. to는 수동 구조 때문에 나타난다."], s=S40 + " 또 검토 의견(원문항에 비해 지문이 너무 짧음)에 따라 원문항처럼 앞뒤 상황을 넣어 두 문장을 원문항 길이로 늘렸다. 정답 위치 ②.")
F(1, 40, "C", r=R40, a=1, p='During practice, the coach (A)<u>made the player repeat the drill</u> ten times. Later that week, the player (B)<u>was made to repeat it again</u> before the big game.',
  c=["(A)는 make + 목적어 + 원형부정사의 능동태이고, (B)는 수동태로 바뀌면서 원형부정사 앞에 to가 붙은 것이다.",
     "(B)에는 again이 있어 반복되는 행동을 나타내므로 to부정사를 쓴다.",
     "(A)의 repeat는 목적어 the drill을 가진 타동사라 원형으로 쓰고, (B)의 repeat는 목적어가 대명사 it으로 바뀌어 to부정사를 쓴다.",
     "(B)의 to repeat는 ‘반복하기 위해서’라는 목적을 나타내는 부사적 용법이다.",
     "(A)는 코치가 직접 한 일이라 원형을, (B)는 나중에 일어난 일이라 미래를 나타내는 to부정사를 쓴다."],
  n=[OKN, "again은 to의 유무와 관계없다. to는 수동 구조 때문에 나타난다.", "목적어가 명사든 대명사든 보어 형태는 바뀌지 않는다. to는 be made 뒤라서 나타난다.",
     "to repeat는 목적이 아니라 be made의 보어이다. ‘반복하게 되었다’는 뜻이다.", "to부정사가 미래를 나타내서가 아니라, 수동태 be made 뒤라서 to가 나타난다."], s=S40 + L40 + " 정답 위치 ①.")
F(1, 40, "D", r=R40, a=2, p="When Tom broke the neighbor's window, Mom (A)<u>made Tom apologize</u> to the neighbor. At school the next day, Tom (B)<u>was made to apologize immediately</u> for being late again.",
  c=["(B)에는 immediately가 있어 동작을 강조하려고 to부정사를 썼다.",
     "(A)는 make + 목적어 + 원형부정사의 능동태이고, (B)는 수동태 be made 뒤에서 생략되었던 to가 다시 나타난 것이다.",
     "apologize는 자동사라 (A)에서는 원형을 쓰고, (B)에서는 수동태 동사 뒤라 동명사 대신 to부정사를 썼다.",
     "(A)는 억지로 시킨다는 사역의 뜻이고, (B)는 허락한다는 뜻이라 보어 형태가 다르다.",
     "(B)의 to apologize는 ‘사과하기 위해’라는 목적을 나타내는 부사적 용법이다."],
  n=["immediately는 to의 유무와 관계없다. to는 수동 구조 때문에 나타난다.", OKN, "apologize의 자동사 성질과는 관계없다. 수동태 be made 뒤라서 to가 나타난다.",
     "(A)와 (B) 모두 억지로 시킨다는 make의 뜻이다. 허락의 뜻은 let이나 allow이다.", "to apologize는 목적이 아니라 be made의 보어이다. ‘사과하게 되었다’는 뜻이다."], s=S40 + L40 + " 정답 위치 ②.")
F(1, 40, "E", r=R40, a=5, p='Our group essay had too many spelling mistakes, so the teacher (A)<u>made us rewrite the essay</u> over the weekend. We (B)<u>were made to rewrite it</u> once more on Monday because we found new errors.',
  c=["(B)의 주어 We가 복수라서 to부정사를 쓴다.", "(A)의 rewrite는 목적어 the essay가 있어 원형이고, (B)는 목적어가 대명사 it이라 to부정사를 쓴다.",
     "(A)는 현재 시제, (B)는 과거 시제라 보어의 형태가 달라졌다.", "(B)의 to rewrite는 ‘다시 쓰기 위해’라는 목적을 나타내는 부사적 용법이다.",
     "(A)는 make + 목적어 + 원형부정사의 능동태이고, (B)는 수동태로 바뀌면서 목적격 보어 앞에 to가 다시 나타난 것이다."],
  n=["주어의 수는 보어 형태와 관계없다. to는 수동 구조 때문에 나타난다.", "목적어가 명사든 대명사든 보어 형태는 바뀌지 않는다.", "(A)의 made도 과거 시제이다. 시제 차이가 아니다.",
     "to rewrite는 목적이 아니라 be made의 보어이다. ‘다시 쓰게 되었다’는 뜻이다.", OKN], s=S40 + L40 + " 정답 위치 ⑤.")
F(1, 40, "F", r=R40, a=4, p="The loud thunder (A)<u>made the dog hide</u> under the bed. The next morning, the dog (B)<u>was made to come out</u> by the smell of food.",
  c=["(A)의 hide는 자동사라 원형을 쓰고, (B)의 come out은 구동사라 to부정사를 쓴다.", "(A)는 개가 스스로 한 행동이라 원형을, (B)는 억지로 한 행동이라 to부정사를 쓴다.",
     "(B)의 to come out은 ‘나오기 위해’라는 목적을 나타내는 부사적 용법이다.",
     "(A)는 make + 목적어 + 원형부정사의 능동태이고, (B)는 수동태 be made 뒤에서 목적격 보어 앞에 to가 다시 나타난 것이다.",
     "(A)는 밤의 일, (B)는 다음 날 아침의 일이라 시제 차이 때문에 보어 형태가 달라졌다."],
  n=["구동사인지 아닌지는 to의 유무와 관계없다. to는 수동 구조 때문에 나타난다.", "(A)도 천둥 때문에 억지로 숨은 것이다. 행동의 성격이 아니라 능동·수동 차이다.",
     "to come out은 목적이 아니라 be made의 보어이다. ‘나오게 되었다’는 뜻이다.", OKN, "두 문장 모두 과거 시제이다. 시제 차이가 아니다."],
  s=S40 + " 어색한 ‘The baby was made to wake’ 대신 천둥과 음식 냄새 장면으로 지문을 바꿨다. 정답 위치 ④.")
