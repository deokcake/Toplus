# 1급 CH2 시제 (11~20) 수정 예시

# 1-11 현재 습관 + 미래 의문문: 오답을 같은 동사의 다른 형태로
NEED11 = ["매일·요일마다 반복되는 습관은 3인칭 단수 현재형으로 쓴다.", "다음 주·내년의 일을 묻는 말은 Will + 주어 + 동사원형으로 쓴다."]
F(1, 11, "C", p="- Mina _____ the piano after dinner every day.\n- _____ she join the orchestra next semester?", keepx=True,
  s="‘/’로 이어 쓴 두 문장을 원문항처럼 ‘-’로 시작하는 두 줄로 나눴다.")
def f11(t, p, c, a, v3, fut, s):
    F(1, 11, t, p=p, c=c, a=a, k=f"반복 습관은 {v3}, 미래를 묻는 말은 Will이 알맞다.", n=tnotes(c, a, NEED11, f"반복 습관은 {v3}, 미래를 묻는 말은 Will이 알맞다."), s=s)
f11("D", "- Tom _____ to school by bike every morning.\n- _____ he take the bus next week?", ["rode - Did", "rides - Will", "rides - Are", "ride - Will", "ride - Do"], 2, "rides", "next week",
    "오답 네 개가 지문과 무관한 practice를 써서 정답만 문맥에 맞았다. 오답을 ride의 다른 형태(rode - Did / rides - Are / ride - Will / ride - Do)로 바꾸고 두 줄로 나눴다.")
f11("E", "- My dad _____ coffee every morning.\n- _____ he stop drinking it next month?", ["drinks - Are", "drank - Did", "drinks - Will", "drink - Will", "drink - Do"], 3, "drinks", "next month",
    "practice로 된 오답을 drink의 다른 형태(drinks - Are / drank - Did / drink - Will / drink - Do)로 바꿔 모든 보기가 경쟁하게 했다. 두 줄로 나눴다.")
f11("F", "- Jane _____ English on Tuesdays.\n- _____ she take French next year?", ["study - Will", "study - Do", "studies - Are", "studies - Will", "studied - Did"], 4, "studies", "next year",
    "practice로 된 오답을 study의 다른 형태(study - Will / study - Do / studies - Are / studied - Did)로 바꾸고 두 줄로 나눴다.")

# 1-12 단순과거 + 현재완료: 발문 설명 삭제, 오답을 같은 동사의 다른 시제로
NEED12 = ["last night·yesterday처럼 끝난 과거 시점에는 단순과거를 쓴다.", "recently가 나타내는 최근부터 지금까지의 결과는 have/has + 과거분사로 쓰고, 복수 주어에는 have를 쓴다."]
F(1, 12, "C", st="R", p="The storm _____ several trees last night.\nScientists _____ a new treatment recently.",
  xr=[("여기서 지정한 최근부터 현재까지의 성과에는", "recently가 나타내는 최근부터 현재까지의 성과에는"), ("명시된 끝난 과거 시점과", "last night라는 끝난 과거 시점과")],
  s="발문에 덧붙인 ‘첫 문장은 끝난 과거의 일, 둘째 문장은 … 성과’ 설명을 지워, 원문항처럼 last night·recently 단서로 판단하게 했다. 두 문장을 두 줄로 나눴다.")
def f12(t, p, c, a, k, s):
    F(1, 12, t, st="R", p=p, c=c, a=a, k=k, n=tnotes(c, a, NEED12, k), s=s)
f12("D", "We _____ the old bridge last summer.\nEngineers _____ a safer design recently.", ["repaired - create", "repaired - has created", "repaired - have created", "repairs - create", "has repaired - have created"], 3,
    "last summer에는 단순과거 repaired, recently와 복수 주어 Engineers에는 have created가 알맞다.",
    "damage/develop로 된 오답을 repair/create의 다른 시제로 바꿔 정답만 문맥에 맞던 문제를 없앴다. 발문 설명을 지우고 두 줄로 나눴다.")
f12("E", "Tom _____ his old bike yesterday morning.\nDoctors _____ a new vaccine recently.", ["sold - have tested", "sells - test", "has sold - have tested", "sold - test", "sold - has tested"], 1,
    "yesterday morning에는 단순과거 sold, recently와 복수 주어 Doctors에는 have tested가 알맞다.",
    "정답 짝 lost - have made가 원문항 정답과 같아서 문장과 동사를 sold - have tested로 바꾸고, 오답을 같은 동사의 다른 시제로 만들었다. 발문 설명을 지웠다.")
f12("F", "Jane _____ the application last week.\nThe team members _____ several improvements recently.", ["submits - introduce", "has submitted - have introduced", "submitted - introduce", "submitted - have introduced", "submitted - has introduced"], 4,
    "last week에는 단순과거 submitted, recently와 복수 주어 The team members에는 have introduced가 알맞다.",
    "damage/develop로 된 오답을 submit/introduce의 다른 시제로 바꾸고 발문 설명을 지웠다.")

# 1-14 우리말 + 두 빈칸 짝(주절 동사 - that절 과거완료)
# (1-14 B는 아래 f14 뒤에서 등록: 2차 감수에서 보기를 원문항처럼 바꿈)
R14 = "과거의 한 시점(알게 된 때)을 기준으로 그보다 먼저 끝난 일은 had + 과거분사로 나타내고, 기준 시점의 일은 단순과거로 쓴다."
def f14(t, p, c, a, main, sub, s):
    k = f"우리말에서 알게 된 일이 기준 시점이고 {sub[0]} 일은 그보다 먼저 끝났으므로 {main[0]} — had {sub[1]}가 알맞다."
    need = [f"기준 시점인 주절의 일은 단순과거 {main[0]}로 쓴다.", f"그보다 먼저 끝난 that절의 일은 과거완료 had {sub[1]}로 쓴다."]
    F(1, 14, t, st="R", p=p, c=c, a=a, r=R14, k=k, n=tnotes(c, a, need, k), s=s)
S14 = "발문이 ‘능동 과거완료로 명시할 때’라고 정답을 알려 주고 형식도 빈칸 하나로 바뀌었다. 원문항처럼 우리말 뜻을 주고 ‘주절 동사 — that절 동사’ 두 빈칸 짝을 고르는 형식으로 되돌렸다."
f14("C", "관리자는 팀이 보고서를 이미 끝내 놓았다는 것을 알았다.\nThe manager _____ that the team _____ the report already.",
    ["learned — finished", "learned — had finished", "had learned — finished", "had learned — had finished", "has learned — have finished"], 2, ("learned",), ("끝낸", "finished"), S14)
f14("D", "Mina는 누군가 창문을 이미 열어 두었다는 것을 알게 되었다.\nMina _____ that someone _____ the window already.",
    ["found — opened", "had found — had opened", "has found — has opened", "found — had opened", "had found — opened"], 4, ("found",), ("연", "opened"), S14 + " 정답 위치 ④.")
f14("E", "우리는 Tom이 표를 이미 사 두었다는 것을 알게 되었다.\nWe _____ that Tom _____ the tickets already.",
    ["discovered — bought", "has discovered — has bought", "had discovered — had bought", "had discovered — bought", "discovered — had bought"], 5, ("discovered",), ("표를 산", "bought"), S14 + " 정답 위치 ⑤.")
f14("F", "선생님은 학생들이 교실을 이미 청소해 두었다는 것을 알게 되었다.\nThe teacher _____ that the students _____ the classroom already.",
    ["realized — had cleaned", "realized — cleaned", "had realized — cleaned", "had realized — had cleaned", "has realized — have cleaned"], 1, ("realized",), ("청소한", "cleaned"), S14 + " 정답 위치 ①.")

# 1-15 틀린 문장 개수: 괄호 조건 삭제, d를 조건 없이도 틀린 상태동사 진행형으로, 선택지 정렬
F(1, 15, "B", op="sortc", s="개수 선택지를 1개~5개 순으로 정렬했다(정답 ④→②).")
S15 = "발문 괄호가 ‘b는…, d는…’이라고 판단할 문장을 지목해 답을 알려 주었다. 괄호를 지우고, d를 조건 없이도 틀린 상태동사 진행형({})으로 바꿨다. 개수 선택지를 1개~5개 순으로 정렬했다."
F(1, 15, "C", st="R", op="sortc", p=V(1, 15, "C")["passage"].replace("I <u>am understanding</u> the rule.", "This box <u>is containing</u> old photos."),
  xr=[("d) 틀림: 이 문항의 understand는 정적인 이해 상태이다. am understanding → understand.", "d) 틀림: contain은 ‘담고 있다’는 상태동사라 진행형으로 쓰지 않는다. is containing → contains.")],
  s=S15.format("This box is containing old photos."))
F(1, 15, "D", st="R", op="sortc", p=V(1, 15, "D")["passage"].replace("I <u>am believing</u> his story.", "This book <u>is belonging</u> to Jane."),
  xr=[("d) 틀림: 여기서는 지속적인 믿음 상태이다. am believing → believe.", "d) 틀림: belong은 소유 관계를 나타내는 상태동사라 진행형으로 쓰지 않는다. is belonging → belongs.")],
  s=S15.format("This book is belonging to Jane."))
F(1, 15, "E", st="R", op="sortc", s="판단할 문장을 지목하던 발문 괄호를 지우고, 개수 선택지를 1개~5개 순으로 정렬(정답 ①)했다.")
F(1, 15, "F", st="R", op="sortc", p=V(1, 15, "F")["passage"].replace("I <u>am needing</u> help.", "He <u>is preferring</u> tea to coffee."),
  xr=[("d) 틀림: 여기서 need는 지속적인 필요 상태이다. am needing → need.", "d) 틀림: prefer는 더 좋아하는 상태를 나타내는 상태동사라 진행형으로 쓰지 않는다. is preferring → prefers.")],
  s=S15.format("He is preferring tea to coffee"))

# 1-16 상태동사: B 검토 의견 반영 — 형태만 보고 답이 나오지 않게 여러 형태를 섞고, 현재형·진행형이 모두 가능해 애매한 오답 대신 시간 표현과 시제가 어긋난 오답을 쓴다
R16 = "own, know, belong, contain, seem, resemble 같은 상태동사는 보통 진행형으로 쓰지 않는다. 다만 have(먹다), taste(맛보다), think about(곰곰이 생각하다)처럼 동작을 나타낼 때는 진행형을 쓸 수 있다. 또 now, yesterday, last year, tomorrow 같은 시간 표현과 동사의 시제가 맞아야 한다."
def sv(sent, verb, meaning, fix):
    return f"‘{sent}’의 동사 {verb}: {meaning} 상태동사라 진행형으로 쓰지 않는다. ‘{fix}’로 고쳐야 하므로 오답이다."
def tn16(sent, cue, fix):
    return f"‘{sent}’은 시간 표현({cue})과 동사의 시제가 맞지 않는다. ‘{fix}’로 고쳐야 하므로 오답이다."
def ok16(sent, verb):
    return f"‘{sent}’은 상태동사({verb})를 단순현재형으로 바르게 썼으므로 정답이다."
def act16(sent, verb, meaning):
    return f"‘{sent}’의 동사({verb})는 {meaning}라는 동작을 나타내므로 진행형으로 쓸 수 있어 정답이다."
S16 = "발문이 ‘상태를 단순현재형으로 나타낸 문장’으로 바뀌어 단순현재형만 찾으면 되었다. 원문항 발문 ‘어법상 옳은 문장’으로 되돌렸다. 또 B 검토 의견이 이 유형에도 해당해 반영했다. 보기 네 개가 진행형이고 하나만 현재형이라 형태만 보고 답을 고를 수 있었으므로 현재형·진행형·과거형을 섞었고, 현재형과 진행형이 모두 가능해 애매할 수 있는 오답 대신 시간 표현과 시제가 어긋난 오답을 넣었다. 원문항도 같은 짜임이라 원문항보다 조금 어려워진다."
F(1, 16, "B", st="R", r=R16, a=3,
  c=["Look! The baby slept on the sofa now.", "This bag is belonging to my sister.", "We are having dinner with our grandparents now.", "I am knowing the answer to this riddle.", "Two years ago, Mr. Park owns a small bakery."],
  n=[tn16("Look! The baby slept on the sofa now.", "Look!, now", "Look! The baby is sleeping on the sofa now."), sv("This bag is belonging to my sister.", "belong", "소유 관계를 나타내는", "This bag belongs to my sister."),
     act16("We are having dinner with our grandparents now.", "have", "‘(식사를) 하다’"), sv("I am knowing the answer to this riddle.", "know", "‘알고 있다’는", "I know the answer to this riddle."),
     tn16("Two years ago, Mr. Park owns a small bakery.", "Two years ago", "Two years ago, Mr. Park owned a small bakery.")],
  s="Claude 판정은 ‘적합’이었으나 검토 의견에 따라 고쳤다. 보기 네 개가 진행형이고 하나만 현재형이라 형태만 보고 답을 고를 수 있었으므로 진행형·과거형·현재형을 섞고, 정답은 동작을 나타내는 have(먹다)의 진행형으로 두었다. 현재형과 진행형이 모두 가능해 애매할 수 있는 오답은 쓰지 않고, 시간 표현과 시제가 어긋난 오답(Look! … slept … now, Two years ago … owns)을 넣었다. 원문항도 같은 짜임이라 원문항보다 조금 어려워진다. 정답 위치 ③.")
F(1, 16, "C", st="R", r=R16, a=2,
  c=["The soup is tasting too salty.", "My uncle owns two restaurants in Busan.", "Look! The children played in the snow right now.", "The twins are resembling their father.", "Last year, my cousin belongs to the school band."],
  n=[sv("The soup is tasting too salty.", "taste", "‘~한 맛이 나다’는 뜻일 때", "The soup tastes too salty."), ok16("My uncle owns two restaurants in Busan.", "own"),
     tn16("Look! The children played in the snow right now.", "Look!, right now", "Look! The children are playing in the snow right now."), sv("The twins are resembling their father.", "resemble", "‘닮다’는", "The twins resemble their father."),
     tn16("Last year, my cousin belongs to the school band.", "Last year", "Last year, my cousin belonged to the school band.")], s=S16 + " 정답 위치 ②.")
F(1, 16, "D", st="R", r=R16, a=1,
  c=["The chef is tasting the sauce right now.", "This box is containing old family photos.", "Look! It snowed heavily outside now.", "My parents are owning a small café.", "Tomorrow, the students took a big test."],
  n=[act16("The chef is tasting the sauce right now.", "taste", "‘맛을 보다’"), sv("This box is containing old family photos.", "contain", "‘담고 있다’는", "This box contains old family photos."),
     tn16("Look! It snowed heavily outside now.", "Look!, now", "Look! It is snowing heavily outside now."), sv("My parents are owning a small café.", "own", "‘소유하다’는", "My parents own a small café."),
     tn16("Tomorrow, the students took a big test.", "Tomorrow", "Tomorrow, the students will take a big test.")], s=S16 + " 정답 위치 ①.")
F(1, 16, "E", st="R", r=R16, a=4,
  c=["Look! My dog chased a cat in the yard now.", "He is seeming very nervous today.", "She is having a lot of homework this week.", "This soup contains too much salt.", "Last night, we need more chairs for the party."],
  n=[tn16("Look! My dog chased a cat in the yard now.", "Look!, now", "Look! My dog is chasing a cat in the yard now."), sv("He is seeming very nervous today.", "seem", "‘~처럼 보이다’는", "He seems very nervous today."),
     sv("She is having a lot of homework this week.", "have", "‘가지고 있다’는 뜻일 때", "She has a lot of homework this week."), ok16("This soup contains too much salt.", "contain"),
     tn16("Last night, we need more chairs for the party.", "Last night", "Last night, we needed more chairs for the party.")], s=S16 + " 정답 위치 ④.")
F(1, 16, "F", st="R", r=R16, a=5,
  c=["Look! The kids built a snowman now.", "The suitcase is weighing about twenty kilograms.", "Yesterday, Dad talks on the phone for two hours.", "Mr. Kim is having three children.", "I am thinking about my summer plans."],
  n=[tn16("Look! The kids built a snowman now.", "Look!, now", "Look! The kids are building a snowman now."), sv("The suitcase is weighing about twenty kilograms.", "weigh", "‘무게가 ~이다’는 뜻일 때", "The suitcase weighs about twenty kilograms."),
     tn16("Yesterday, Dad talks on the phone for two hours.", "Yesterday", "Yesterday, Dad talked on the phone for two hours."), sv("Mr. Kim is having three children.", "have", "‘가지고 있다(두다)’는 뜻일 때", "Mr. Kim has three children."),
     act16("I am thinking about my summer plans.", "think about", "‘곰곰이 생각하다’")], s=S16 + " 정답 위치 ⑤.")

# 1-17 현재완료 + 특정 과거 시점: 오답 네 문장을 유형마다 새로
R17 = "현재완료(have/has + p.p.)는 현재와 연결된 경험·결과·계속을 나타내며, yesterday, last Monday, ago, in 2021처럼 끝난 특정 과거 시점과 함께 쓰지 않는다."
def pp_ok(sent, why): return f"‘{sent}’은 {why} 올바른 문장이므로 오답이다."
def pp_bad(sent, when, fix): return f"‘{sent}’은 끝난 과거 시점 {when}와 현재완료를 함께 썼다. {fix}로 고쳐야 하므로 정답이다."
F(1, 17, "C", r=R17, a=4,
  c=["My uncle has worked at this hospital for ten years.", "Have you ever eaten Thai food?", "I lost my phone on the subway yesterday.", "The bus has left ten minutes ago.", "We have just finished our homework."],
  n=[pp_ok("My uncle has worked at this hospital for ten years.", "for ten years와 현재완료로 계속을 나타낸"), pp_ok("Have you ever eaten Thai food?", "ever와 현재완료로 경험을 묻는"),
     pp_ok("I lost my phone on the subway yesterday.", "yesterday와 단순과거를 쓴"), pp_bad("The bus has left ten minutes ago.", "ten minutes ago", "The bus left ten minutes ago."),
     pp_ok("We have just finished our homework.", "just와 현재완료로 완료를 나타낸")],
  s="B와 같던 오답 네 문장과, 정답과 짝을 이루던 ⑤ ‘Mina finished the report yesterday.’를 모두 새 문장으로 바꿨다. 틀린 문장도 ‘The bus has left ten minutes ago.’로 새로 썼다.")
F(1, 17, "D", r=R17, a=2,
  c=["Sujin has already read this novel twice.", "Tom has met her last Monday.", "I visited my grandparents last weekend.", "They have lived in Busan since 2019.", "Has your brother ever ridden a horse?"],
  n=[pp_ok("Sujin has already read this novel twice.", "already·twice와 현재완료로 경험을 나타낸"), pp_bad("Tom has met her last Monday.", "last Monday", "Tom met her last Monday."),
     pp_ok("I visited my grandparents last weekend.", "last weekend와 단순과거를 쓴"), pp_ok("They have lived in Busan since 2019.", "since와 현재완료로 계속을 나타낸"),
     pp_ok("Has your brother ever ridden a horse?", "ever와 현재완료로 경험을 묻는")],
  s="B와 똑같던 오답 네 문장을 새로 쓰고, 틀린 문장 ‘Tom has met her last Monday.’만 남겼다.")
F(1, 17, "E", r=R17, a=5,
  c=["The rain has just stopped.", "My parents have been married for twenty years.", "Did you watch the game last night?", "I have never seen snow before.", "We have moved here in 2021."],
  n=[pp_ok("The rain has just stopped.", "just와 현재완료로 방금 끝난 일을 나타낸"), pp_ok("My parents have been married for twenty years.", "for와 현재완료로 계속된 상태를 나타낸"),
     pp_ok("Did you watch the game last night?", "last night와 단순과거 의문문을 쓴"), pp_ok("I have never seen snow before.", "never와 현재완료로 경험을 나타낸"),
     pp_bad("We have moved here in 2021.", "in 2021", "We moved here in 2021.")],
  s="B와 똑같던 오답 네 문장을 새로 쓰고, 틀린 문장 ‘We have moved here in 2021.’을 ⑤에 두었다.")
F(1, 17, "F", r=R17, a=3,
  c=["Our team has won three games so far.", "The movie started at seven o'clock.", "Jiwoo has called me two hours ago.", "Have you finished the book yet?", "He has been sick since Monday."],
  n=[pp_ok("Our team has won three games so far.", "so far와 현재완료로 지금까지의 결과를 나타낸"), pp_ok("The movie started at seven o'clock.", "특정 과거 시각에 단순과거를 쓴"),
     pp_bad("Jiwoo has called me two hours ago.", "two hours ago", "Jiwoo called me two hours ago."), pp_ok("Have you finished the book yet?", "yet과 현재완료로 완료 여부를 묻는"),
     pp_ok("He has been sick since Monday.", "since와 현재완료로 계속된 상태를 나타낸")],
  s="B와 같던 오답 네 문장과 짝을 이루던 ‘Jane has just called me’를 없애고 모두 새로 썼다. 틀린 문장도 이름을 바꿔 ‘Jiwoo has called me two hours ago.’로 했다.")

# 1-18 두 문장 종합: 발문과 두 문장 제시 형식을 원문항대로
S18 = "발문을 원문항 ‘두 문장을 종합한 의미가 같은 한 문장’으로 되돌리고, 한 문장으로 합쳐 쓴 제시문을 원문항처럼 ‘시작한 일 / 지금도 계속되는 일’ 두 문장으로 나눴다."
F(1, 18, "B", st="R", p="- Tom started working here in 2022.\n- He is still working here now.", s=S18)
F(1, 18, "C", st="R", p="- We started discussing the issue at 2 p.m.\n- We are still discussing it now.", s=S18)
F(1, 18, "D", st="R", p="- Mina started studying at noon.\n- She is still studying now.", s=S18)
F(1, 18, "E", st="R", p="- It started raining three hours ago.\n- It is still raining now.", s=S18)
F(1, 18, "F", st="R", p="- They started waiting forty minutes ago.\n- They are still waiting now.", s=S18)

# 1-19 (A)~(C) 빈칸: 원문항 발문·밑줄 빈칸·우리말 해석 복원, 괄호 조건 삭제
R19 = "과거의 기준 사건에는 단순과거를, 그보다 먼저 끝난 사건에는 had + 과거분사를 쓴다."
NEED19 = ["(A)는 기준이 되는 과거 사건이므로 단순과거를 쓴다.", "(B)는 그보다 먼저 끝난 일을 나타내는 과거완료의 had가 와야 한다.", "(C)는 had 뒤이므로 과거분사가 와야 한다."]
def f19(t, p, c, a, k, s):
    F(1, 19, t, st="R", p=p, c=c, a=a, r=R19, k=k, n=tnotes(c, a, NEED19, k, labs=["(A)", "(B)", "(C)"]), s=s)
U = "(<u>    {}    </u>)"
f19("B", f"When Tom {U.format('A')} the station, the train {U.format('B')} already {U.format('C')}.\n(Tom이 역에 도착했을 때, 기차는 이미 떠나고 없었다.)", V(1, 19, "B")["c"], 1,
    "도착한 일이 기준이고 기차가 떠난 일은 그보다 먼저이므로 reached - had - departed가 알맞다.",
    "발문을 원문항과 같게 하고, 원문항처럼 밑줄 빈칸 (A)(B)(C)와 우리말 해석 줄을 복원했다. 보기와 정답은 그대로다.")
f19("C", f"When Mina {U.format('A')} the theater, the show {U.format('B')} already {U.format('C')}.\n(Mina가 극장에 들어갔을 때, 공연은 이미 시작한 뒤였다.)", V(1, 19, "C")["c"][:4] + ["enters - has - begun"], 1,
    "극장에 들어간 일이 기준이고 공연이 시작한 일은 그보다 먼저이므로 entered - had - begun이 알맞다.",
    "발문 괄호의 ‘(A)는 단순과거, (B)(C)는 능동 과거완료’ 설명이 정답 구조를 알려 주어 지우고, 원문항처럼 밑줄 빈칸과 우리말 해석을 넣었다. 괄호가 없으면 ⑤ ‘the show was already begun’(수동)도 성립할 여지가 있어 ⑤를 ‘enters - has - begun’으로 바꿨다.")
f19("D", f"When we {U.format('A')} home, Dad {U.format('B')} already {U.format('C')}.\n(우리가 집에 도착했을 때, 아빠는 이미 나가고 없었다.)", V(1, 19, "D")["c"], 3,
    "집에 도착한 일이 기준이고 아빠가 나간 일은 그보다 먼저이므로 got - had - left가 알맞다.",
    "정답 구조를 알려 주던 발문 괄호를 지우고, 원문항처럼 밑줄 빈칸과 우리말 해석을 넣었다.")
f19("E", f"When Jane {U.format('A')} the office, the meeting {U.format('B')} already {U.format('C')}.\n(Jane이 사무실에 도착했을 때, 회의는 이미 시작한 뒤였다.)",
    ["arrived at - has - start", "arrived at - has - started", "had arrived at - had - started", "arrived at - had - started", "arrived at - had - start"], 4,
    "도착한 일이 기준이고 회의가 시작한 일은 그보다 먼저이므로 arrived at - had - started가 알맞다.",
    "발문 괄호를 지웠다. 괄호가 없으면 ① ‘the meeting was already started’(수동)도 성립할 수 있어 ①을 명백히 틀린 ‘arrived at - has - start’로 바꾸고, 밑줄 빈칸과 우리말 해석을 넣었다.")
f19("F", f"When I {U.format('A')} the store, it {U.format('B')} already {U.format('C')}.\n(내가 가게에 도착했을 때, 가게는 이미 문을 닫은 뒤였다.)",
    ["reached - has - close", "reached - has - closed", "reached - had - closed", "reached - had - close", "had reached - had - closed"], 3,
    "도착한 일이 기준이고 가게가 문을 닫은 일은 그보다 먼저이므로 reached - had - closed가 알맞다.",
    "발문 괄호를 지웠다. 괄호가 없으면 ① ‘it was already closed’도 자연스러워 복수 정답이 되므로 ①을 ‘reached - has - close’로 바꾸고, 밑줄 빈칸과 우리말 해석을 넣었다.")

# 1-20 과거완료진행 + 단순과거: 정답을 알려 주던 발문을 원문항대로
R20 = "과거의 한 사건이 일어날 때까지 계속 진행되던 동작은 had been + -ing으로, 그 기준 사건은 단순과거로 나타낸다."
NEED20 = ["과거의 기준 사건까지 계속된 동작에는 had been + -ing을 쓴다.", "기준이 되는 과거 사건은 단순과거로 쓴다."]
def f20(t, k, s):
    c = ["(A) {} - (B) {}".format(*x.split(" - ")) for x in V(1, 20, t)["c"]]; a = int(V(1, 20, t)["ans"])
    F(1, 20, t, st="R", c=c, r=R20, k=k, n=tnotes(c, a, NEED20, k, labs=["(A)", "(B)"]), s=s + " 보기에도 원문항처럼 (A), (B) 표시를 붙였다.")
S20 = "발문이 ‘(A)는 과거완료진행, (B)는 단순과거로 나타낼 때’라고 정답을 알려 주었다. 원문항 발문 ‘흐름상 빈칸 (A), (B)에 들어갈 말이 어법상 가장 바르게 짝지어진 것’으로 되돌리고 해설을 문맥 근거로 고쳤다."
f14("B", "Jane은 자신이 잘못된 파일을 보냈다는 것을 깨달았다.\nJane _____ that she _____ the wrong file.",
    ["realized — sent", "had realized — sent", "has realized — has sent", "had realized — had sent", "realized — had sent"], 5, ("realized",), ("잘못된 파일을 보낸", "sent"),
    "우리말의 오타 ‘개달았다’를 고치고 빈 줄을 지웠다. 또 오답 세 개가 현재형 realizes로 시작해 우리말 ‘깨달았다’만으로 지워졌으므로, 원문항처럼 과거·과거완료·현재완료를 엇바꾼 짝(과거 — 과거, 과거완료 — 과거 등)으로 보기를 바꿨다. 정답은 그대로 ⑤ realized — had sent.")
f20("B", "거의 한 시간 동안 기다리던 중에 버스가 도착했으므로 had been waiting - arrived가 알맞다.", "보기에 원문항의 (A), (B) 표시가 빠져 있었다.")
f20("C", "몇 시간 동안 걷고 있던 중에 불빛을 발견했으므로 had been walking - noticed가 알맞다.", S20)
f20("D", "아침 내내 공부하다가 마침내 쉬었으므로 had been studying - took가 알맞다.", S20)
f20("E", "몇 주 동안 일하다가 마침내 해결책을 찾았으므로 had been working - found가 알맞다.", S20)
f20("F", "이틀 동안 비가 내리다가 하늘이 갰으므로 had been raining - cleared가 알맞다.", S20)
