# 1급 CH10 가정법 (91~100) 수정 예시

# 1-91 Without / But for: 정답 뜻을 풀어 주던 발문을 원문항대로
for t in "BCDEF":
    F(1, 91, t, st="R", p=V(1, 91, t)["passage"].replace(" / ", "\n"),
      xr=[("발문이 요구하는 원인이 없다는 반대 조건은", "직설법의 원인을 반대로 가정한 ‘~이 없다면(없었다면)’은")],
      s="발문이 ‘직설법에서 제시한 원인이 없다는 반대 조건’이라고 정답의 뜻을 풀어 주어, 원문항 발문 ‘직설법 문장을 가정법으로 바꿀 때 빈칸에 알맞은 것’으로 되돌렸다. 두 문장을 두 줄로 나눴다.")

# 1-92 가정법 시제 어법: 오답을 유형마다 새로, 원문항처럼 혼합가정법 포함
R92 = "현재 사실의 반대는 if + 과거형, would + 동사원형 / 과거 사실의 반대는 if + had + 과거분사, would have + 과거분사 / 과거 조건과 현재 결과는 if + had + 과거분사, would + 동사원형(혼합가정법)으로 쓴다."
S92 = "틀린 문장이 같은 내용의 옳은 문장과 짝을 이뤄 단서가 되었고 C~F는 오답 네 개가 B와 같았다. 원문항처럼 혼합가정법·가정법 과거·과거완료 문장을 섞어 유형마다 새로 썼다."
def f92(t, items, a):
    F(1, 92, t, c=[x for x, _ in items], a=a, r=R92, n=[(w + (" 틀린 문장이므로 정답이다." if i + 1 == a else " 올바르므로 오답이다.")) for i, (_, w) in enumerate(items)], s=S92 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f92("B", [("If I had taken the medicine yesterday, I would feel better now.", "과거 조건 + 현재 결과(now)의 혼합가정법이다."), ("If you lived closer, we could meet more often.", "현재 사실의 반대인 가정법 과거이다."),
          ("If they had listened to the guide, they would not have gotten lost.", "과거 사실의 반대인 가정법 과거완료이다."), ("If she had known the answer, she would have told us.", "가정법 과거완료이다."),
          ("If we had left sooner, we would not miss the flight yesterday.", "yesterday의 과거 결과이므로 would not have missed로 써야 한다.")], 5)
f92("C", [("If it were sunny today, we would go hiking.", "현재 사실의 반대인 가정법 과거이다."), ("If Jiho had saved money last year, he could buy a bike now.", "과거 조건 + 현재 결과(now)의 혼합가정법이다."),
          ("If Mina had taken the earlier train, she would be at the office yesterday.", "yesterday의 과거 결과이므로 would have been으로 써야 한다."), ("If I were you, I would apologize first.", "가정법 과거이다."),
          ("If the team had practiced more, they might have won the game.", "과거 사실의 반대인 가정법 과거완료이다.")], 3)
f92("D", [("If my brother were here, he would fix the computer.", "가정법 과거이다."), ("If I had gone to bed early, I would not be so tired now.", "과거 조건 + 현재 결과(now)의 혼합가정법이다."),
          ("If she had studied abroad, she could have learned French.", "가정법 과거완료이다."), ("If Tom had studied harder, he would pass the exam last week.", "last week의 과거 결과이므로 would have passed로 써야 한다."),
          ("If we had more time, we could visit the museum.", "가정법 과거이다.")], 4)
f92("E", [("If Jane had brought an umbrella, she would not get wet last night.", "last night의 과거 결과이므로 would not have gotten wet으로 써야 한다."), ("If I knew his number, I would call him.", "가정법 과거이다."),
          ("If you had told me earlier, I could have helped you.", "가정법 과거완료이다."), ("If he had not broken his leg, he would be on the team now.", "과거 조건 + 현재 결과(now)의 혼합가정법이다."),
          ("If the store were open, we could buy some milk.", "가정법 과거이다.")], 1)
f92("F", [("If I had a car, I would drive you home.", "가정법 과거이다."), ("If they had checked the map, they would not be lost yesterday.", "yesterday의 과거 결과이므로 would not have gotten lost로 써야 한다."),
          ("If she had not missed the bus, she would be here now.", "과거 조건 + 현재 결과(now)의 혼합가정법이다."), ("If we had booked early, we would have gotten better seats.", "가정법 과거완료이다."),
          ("If it snowed tomorrow, the school would close.", "가정법 과거(미래의 가능성이 낮은 일)이다.")], 2)

# 1-93 I wish + 과거형: 오답을 유형마다 새로(짝 없애기)
R93 = "I wish + 과거형(be동사는 were)은 현재 사실의 반대 소망, I wish + had + 과거분사는 과거 사실의 반대 소망이다. If ~ 가정법과 함께 시점을 확인한다."
S93 = "틀린 문장이 같은 내용의 옳은 wish 문장과 짝을 이뤘고 C~F는 오답 네 개가 B와 같았다. 원문항처럼 wish·가정법 문장을 섞어 유형마다 새로 썼다."
def f93(t, items, a):
    F(1, 93, t, c=[x for x, _ in items], a=a, r=R93, n=[(w + (" 틀린 문장이므로 정답이다." if i + 1 == a else " 올바르므로 오답이다.")) for i, (_, w) in enumerate(items)], s=S93 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f93("B", [("I have no pet. I wish I had a puppy.", "현재 사실의 반대 소망에 과거형 had를 썼다."), ("If Mina had more time, she would learn to dance.", "가정법 과거이다."), ("I wish I had watched the game last night.", "과거 사실의 반대 소망에 had + 과거분사를 썼다."),
          ("Tom wishes he could fly.", "현재의 반대 소망에 could를 썼다."), ("The room is noisy. I wish it is quieter right now.", "현재 사실의 반대 소망이므로 were로 써야 한다.")], 5)
f93("C", [("I wish my grandparents lived near us.", "현재 사실의 반대 소망에 과거형 lived를 썼다."), ("If it stopped raining, we would go out.", "가정법 과거이다."), ("She wishes she had not said that yesterday.", "과거 사실의 반대 소망이다."),
          ("I wish I could play the guitar.", "현재의 반대 소망에 could를 썼다."), ("I do not know French. I wish I know it now.", "현재 사실의 반대 소망이므로 knew로 써야 한다.")], 5)
f93("D", [("I wish today were Saturday.", "현재 사실의 반대 소망에 were를 썼다."), ("Tom is not here. I wish he is with us.", "현재 사실의 반대 소망이므로 were로 써야 한다."), ("If I were taller, I could reach the shelf.", "가정법 과거이다."),
          ("We wish we had taken more photos on the trip.", "과거 사실의 반대 소망이다."), ("Jiwoo wishes she spoke Chinese.", "현재 사실의 반대 소망에 과거형 spoke를 썼다.")], 2)
f93("E", [("I wish I had a bigger room.", "현재 사실의 반대 소망이다."), ("If he had more money, he would travel the world.", "가정법 과거이다."), ("Mina cannot drive. She wishes she can drive.", "현재 사실의 반대 소망이므로 could로 써야 한다."),
          ("I wish I had brought my camera yesterday.", "과거 사실의 반대 소망이다."), ("My sister wishes she were older.", "현재 사실의 반대 소망에 were를 썼다.")], 3)
f93("F", [("I wish the weather were warmer.", "현재 사실의 반대 소망에 were를 썼다."), ("If I lived by the sea, I would swim every day.", "가정법 과거이다."), ("He wishes he had studied harder last year.", "과거 사실의 반대 소망이다."),
          ("We are busy today. I wish we are free.", "현재 사실의 반대 소망이므로 were로 써야 한다."), ("I wish I could meet my favorite singer.", "현재의 반대 소망에 could를 썼다.")], 4)

# 1-94 대화 속 가정법: 줄바꿈 복원
for t in "BCDEF":
    F(1, 94, t, p="BR", keepx=True, s="한 줄로 이어 쓴 대화를 원문항처럼 말하는 사람마다 줄을 바꿨다. 밑줄 표현과 정답은 그대로다.")

# 1-95 가정법 여러 형태 틀린 문장 개수: 6문장, 1개~5개 정렬
R95 = "as if/as though + 과거형은 현재 사실의 반대, If only는 소망, but for·without은 ‘~이 없다면(없었다면)’, 도치(Had + 주어 + 과거분사)는 if 생략 구문이다. 각 문장의 시점에 맞는 동사 형태를 확인한다."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]
S95 = "원문항은 보기 문장이 6개인데 변형은 5개였고 개수 선택지 순서가 뒤섞였다. 문장 F를 더해 6개로 맞추고 선택지를 1개~5개 순으로 정렬했다. 한 줄에 한 문장씩 나눴다."
def f95(t, lines, judge, wrong, s):
    F(1, 95, t, p="\n".join(lines), c=CNT5, a=wrong, r=R95, pre=["문장별 판정:"] + judge, k=f"어법상 틀린 문장은 {wrong}개이다.", n="cnt", s=s)
f95("B", ["A) Jane talks as if she had met him before.", "B) If only I were more patient.", "C) If Tom knew the truth, he would tell us.", "D) But for the traffic, we would have arrived earlier.", "E) Had Mina studied harder, she would pass yesterday.", "F) Without water, no plants could live."],
    ["A) 옳음: as if + had + 과거분사는 과거 사실의 반대이다.", "B) 옳음: If only + 과거형(were)은 현재의 반대 소망이다.", "C) 옳음: 가정법 과거이다.", "D) 옳음: but for + 과거완료 결과이다.",
     "E) 틀림: yesterday의 과거 결과이므로 would have passed로 써야 한다.", "F) 옳음: without + 가정법 과거 결과이다."], 1, S95)
f95("C", ["A) He looks as though he has seen a ghost.", "B) If only we had taken the earlier bus.", "C) If my dog were here yesterday, he would have barked.", "D) But for your advice, I would have failed.", "E) Had I known, I would have acted differently.", "F) Were I rich, I will buy a big house."],
    ["A) 옳음: as though + 현재완료는 실제일 수 있는 일을 나타낸다(직설법).", "B) 옳음: If only + had + 과거분사는 과거의 반대 소망이다.", "C) 틀림: yesterday의 과거 일이므로 If my dog had been here로 써야 한다.",
     "D) 옳음: but for + 과거완료 결과이다.", "E) 옳음: If I had known의 도치이다.", "F) 틀림: 가정법 과거의 결과는 would + 동사원형이다. will → would."], 2,
    "A·B·C가 원문항 문장과 거의 같아 새 문장으로 바꿨다. " + S95)
f95("D", ["A) Jane acts as if she knew everything.", "B) If only Tom had called earlier.", "C) If Mina had more time, she would travel.", "D) Without the map, we would have gotten lost.", "E) Had I saw the sign, I would have stopped.", "F) If it were not for music, life would be boring."],
    ["A) 옳음: as if + 과거형은 현재 사실의 반대이다.", "B) 옳음: If only + had + 과거분사는 과거의 반대 소망이다.", "C) 옳음: 가정법 과거이다.", "D) 옳음: without + 과거완료 결과이다.",
     "E) 틀림: 도치 구문에서도 had 뒤에는 과거분사 seen을 쓴다.", "F) 옳음: If it were not for는 ‘~이 없다면’이다."], 1, S95)
f95("E", ["A) Tom talks as though he were the boss.", "B) If only I had listened.", "C) If Jane were taller, she would play basketball.", "D) But for the rain, we would have gone out.", "E) Had Mina known, she would have call.", "F) If he had not helped me, I would fail the test last week."],
    ["A) 옳음: as though + were는 현재 사실의 반대이다.", "B) 옳음: If only + had + 과거분사는 과거의 반대 소망이다.", "C) 옳음: 가정법 과거이다.", "D) 옳음: but for + 과거완료 결과이다.",
     "E) 틀림: would have 뒤에는 과거분사 called를 쓴다.", "F) 틀림: last week의 과거 결과이므로 would have failed로 써야 한다."], 2, S95)
f95("F", ["A) Mina spends money as if she were rich.", "B) If only we could stay longer.", "C) If Tom had left earlier, he would have arrived on time.", "D) Without your help, I could not have finished.", "E) Had I know the answer, I would have told you.", "F) Had it not been for his help, we would fail the test last week."],
    ["A) 옳음: as if + were는 현재 사실의 반대이다.", "B) 옳음: If only + could는 현재의 반대 소망이다.", "C) 옳음: 가정법 과거완료이다.", "D) 옳음: without + 과거완료 결과이다.",
     "E) 틀림: 도치 구문에서도 had 뒤에는 과거분사 known을 쓴다.", "F) 틀림: last week의 과거 결과이므로 would have failed로 써야 한다."], 2,
    "틀린 문장이 하나도 없어 원문항(오류 판별)과 달랐다. E·F에 오류를 넣고 " + S95)

# 1-96 would not have + 과거분사: 발문을 원문항대로
for t in "BCDEF":
    F(1, 96, t, st="R", s="발문을 원문항 ‘괄호 안의 단어를 알맞은 형태로 바꿀 때 빈칸에 들어갈 말로 알맞은 것’과 같게 했다. 보기와 정답은 그대로다.")

# 1-97 가정법 과거완료: 원문항처럼 한 문장의 시제 변형 다섯 개로
R97 = "과거 사실의 반대는 If + 주어 + had + 과거분사, 주어 + would(could) have + 과거분사로 쓴다. if절에 would have를 쓰지 않고, 결과절의 have를 빠뜨리지 않는다."
S97 = "발문이 ‘조건과 결과를 모두 과거 사실의 반대로 가정한 문장’이라고 정답 구조를 알려 주었고, 서로 다른 문장을 섞은 데다 C~F는 오답이 B와 같았다. 원문항처럼 발문을 되돌리고 한 문장의 시제 변형 다섯 개로 새로 만들었다."
def f97(t, base, c, a, notes):
    F(1, 97, t, st="R", c=c, a=a, r=R97, n=[(notes[i] + (" 정답이다." if i + 1 == a else " 오답이다.")) for i in range(5)], s=S97 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f97("B", "", ["If Mina read the message, she would have replied.", "If Mina had read the message, she would has replied.", "If Mina had read the message, she would have replied.", "If Mina has read the message, she would have replied.", "If Mina had read the message, she would replied."], 3,
    ["if절이 과거형이라 결과절(would have replied)과 시점이 맞지 않는다.", "would 뒤에는 동사원형 have를 쓴다. has는 틀린 형태이다.", "if절 had read, 결과절 would have replied로 과거 사실의 반대를 바르게 나타냈다.",
     "가정법 if절에 현재완료 has read를 쓸 수 없다.", "would 뒤에 have가 빠졌다."])
f97("C", "", ["If Tom had known the truth, he would have told us.", "If Tom knew the truth, he would have told us.", "If Tom would have known the truth, he would have told us.", "If Tom had knew the truth, he would have told us.", "If Tom had known the truth, he will have told us."], 1,
    ["if절 had known, 결과절 would have told로 과거 사실의 반대를 바르게 나타냈다.", "if절이 과거형이라 결과절과 시점이 맞지 않는다.", "if절에는 would have를 쓰지 않는다.",
     "had 뒤에는 과거분사 known을 쓴다.", "결과절에 will have를 쓰면 가정법이 아니다."])
f97("D", "", ["If we booked earlier, we would have paid less.", "If we had booked earlier, we would pay less yesterday.", "If we have booked earlier, we would have paid less.", "If we had booked earlier, we would have paid less.", "If we had booked earlier, we would have pay less."], 4,
    ["if절이 과거형이라 결과절과 시점이 맞지 않는다.", "yesterday의 과거 결과인데 결과절이 would + 동사원형이다.", "가정법 if절에 현재완료를 쓸 수 없다.",
     "if절 had booked, 결과절 would have paid로 과거 사실의 반대를 바르게 나타냈다.", "have 뒤에는 과거분사 paid를 쓴다."])
f97("E", "", ["If Jane had brought her ID, she will have entered.", "If Jane would have brought her ID, she would have entered.", "If Jane brought her ID, she would have entered.", "If Jane had bring her ID, she would have entered.", "If Jane had brought her ID, she would have entered."], 5,
    ["결과절에 will have를 쓰면 가정법이 아니다.", "if절에는 would have를 쓰지 않는다.", "if절이 과거형이라 결과절과 시점이 맞지 않는다.",
     "had 뒤에는 과거분사 brought를 쓴다.", "if절 had brought, 결과절 would have entered로 과거 사실의 반대를 바르게 나타냈다."])
f97("F", "", ["If they had practiced more, they would win the final last month.", "If they had practiced more, they would have won the final.", "If they practiced more, they would have won the final.", "If they had practice more, they would have won the final.", "If they has practiced more, they would have won the final."], 2,
    ["last month의 과거 결과인데 결과절이 would + 동사원형이다.", "if절 had practiced, 결과절 would have won으로 과거 사실의 반대를 바르게 나타냈다.", "if절이 과거형이라 결과절과 시점이 맞지 않는다.",
     "had 뒤에는 과거분사 practiced를 쓴다.", "had 대신 has를 쓸 수 없다."])

# 1-98 혼합가정법 배열: 원문항은 제시어에 if가 없는데 정답이 If로 시작해 불완전 → 제시어에 if를 넣고 조건 설명 삭제
R98 = "과거에 하지 않은 일이 현재에 영향을 주는 혼합가정법은 If + 주어 + had + 과거분사, 주어 + would + 동사원형(+ now)으로 쓴다."
ST98 = "다음 주어진 단어를 바르게 배열한 문장을 고르시오."
NOTE98 = " 원문항은 제시어에 if가 없는데 정답이 If로 시작해 불완전하므로, 변형처럼 제시어에 if를 넣은 형태를 살렸다."
def f98(t, c, a, notes):
    F(1, 98, t, st=ST98, c=c, a=a, r=R98, n=[(notes[i] + (" 정답이다." if i + 1 == a else " 오답이다.")) for i in range(5)],
      s="발문이 ‘과거의 조건이 현재 결과에 미치는 영향을 반대로 가정, 조건절을 먼저’라고 혼합가정법 구조를 알려 주었고, 오답에 would have work처럼 성립하지 않는 형태가 있었다. 발문을 원문항처럼 간단히 하고 오답을 제시어로 만든 시제·어순 오류로 바꿨다." + NOTE98)
f98("B", ["If Jane had studied engineering, she would work at this company now.", "If Jane studied engineering, she would have worked at this company now.", "Jane had studied engineering if she would work at this company now.", "If Jane had studied engineering, she would have worked at this company now.", "Had Jane studied engineering if, she would work at this company now."], 1,
    ["if + had + 과거분사(과거 조건), would + 동사원형 + now(현재 결과)의 혼합가정법이다.", "now의 현재 결과인데 would have + 과거분사를 썼고 조건절도 과거형이다.", "if의 위치가 틀려 조건절과 주절이 뒤바뀌었다.",
     "now의 현재 결과에는 would + 동사원형을 쓴다.", "if가 조건절 끝으로 가 어순이 틀렸다."])
f98("C", ["Mina had accepted the job if she would be living abroad now.", "If Mina accepted the job, she would have been living abroad now.", "If Mina had accepted the job, she would have lived abroad now.", "If Mina had accepted the job, she would be living abroad now.", "Accepted Mina the job if had, she would be living abroad now."], 4,
    ["if의 위치가 틀려 조건절과 주절이 뒤바뀌었다.", "조건절이 과거형이고 결과절도 now와 맞지 않는다.", "now의 현재 결과에는 would + 동사원형(be living)을 쓴다.",
     "if + had + 과거분사, would be living + now의 혼합가정법이다.", "어순이 뒤섞여 문장이 되지 않는다."])
f98("D", ["If Tom saved more money, he would have owned a car now.", "Tom had saved more money if he would own a car now.", "If Tom had saved more money, he would own a car now.", "If Tom had saved more money, he would have owned a car now.", "Had saved Tom more money if, he would own a car now."], 3,
    ["조건절이 과거형이고 결과절도 now와 맞지 않는다.", "if의 위치가 틀려 조건절과 주절이 뒤바뀌었다.", "if + had + 과거분사, would own + now의 혼합가정법이다.",
     "now의 현재 결과에는 would + 동사원형을 쓴다.", "어순이 뒤섞여 문장이 되지 않는다."])
f98("E", ["If we had chosen the other route, we would have been there now.", "If we had chosen the other route, we would be there now.", "We had chosen the other route if we would be there now.", "If we chose the other route, we would have been there now.", "Had chosen we the other route if, we would be there now."], 2,
    ["now의 현재 결과에는 would + 동사원형(be)을 쓴다.", "if + had + 과거분사, would be + now의 혼합가정법이다.", "if의 위치가 틀려 조건절과 주절이 뒤바뀌었다.",
     "조건절이 과거형이고 결과절도 now와 맞지 않는다.", "어순이 뒤섞여 문장이 되지 않는다."])
f98("F", ["If Leo moved to Seoul, he would have lived near us now.", "If Leo had moved to Seoul, he would have lived near us now.", "Leo had moved to Seoul if he would live near us now.", "Moved Leo to Seoul if had, he would live near us now.", "If Leo had moved to Seoul, he would live near us now."], 5,
    ["조건절이 과거형이고 결과절도 now와 맞지 않는다.", "now의 현재 결과에는 would + 동사원형을 쓴다.", "if의 위치가 틀려 조건절과 주절이 뒤바뀌었다.",
     "어순이 뒤섞여 문장이 되지 않는다.", "if + had + 과거분사, would live + now의 혼합가정법이다."])

# 1-99 빈칸 밑줄·줄바꿈 복원
BL99 = "(<u>                </u>)"
for t in "BCDEF":
    F(1, 99, t, p=V(1, 99, t)["passage"].replace(" / ", "\n").replace("________", BL99), keepx=True,
      s="원문항처럼 대화를 두 줄로 나누고 빈칸에 밑줄을 넣었다. 보기와 정답은 그대로다.")

# 1-100 <조건>: 원문항처럼 조건 세 개, 한 줄에 하나씩
def cond100(t, meaning, s):
    F(1, 100, t, p=f"<조건>\n\"{meaning}\"라는 의미일 것.\n접속사 'If'를 생략한 도치 구문일 것.\n축약형을 사용하지 않을 것.", keepx=True, s=s)
cond100("C", "Mina의 도움이 없었더라면 나는 마감일을 지키지 못했을 것이다.", "‘/’로 이어 쓴 <조건>을 원문항처럼 한 줄에 하나씩 나누고, 우리말의 빠진 조사(도움 없었더라면 → 도움이 없었더라면)를 고쳤다.")
cond100("D", "그 지도가 없었더라면 우리는 길을 잃었을 것이다.", "원문항처럼 <조건> 세 개(의미, If 생략 도치, 축약형 금지)로 맞추고 한 줄에 하나씩 나눴다.")
cond100("E", "Jane의 조언이 없었더라면 나는 잘못된 선택을 했을 것이다.", "원문항처럼 <조건> 세 개(의미, If 생략 도치, 축약형 금지)로 맞추고 한 줄에 하나씩 나눴다.")
cond100("F", "그 백업 파일이 없었더라면 우리는 데이터를 복구하지 못했을 것이다.", "원문항처럼 <조건> 세 개(의미, If 생략 도치, 축약형 금지)로 맞추고 한 줄에 하나씩 나눴다.")


# ---- 2차 감수(2026-10) 추가 ----
# 1-100 B: <조건>을 원문항처럼 풀어 쓰고 한 줄에 하나씩(1-50 B 검토 의견 ‘조건이 원문항에 비해 명시적이지 않음’과 같은 문제)
cond100("B", "Tom의 경고가 없었더라면 우리는 위험을 몰랐을 것이다.", "<조건>이 ‘If 생략 도치’, ‘축약형 금지’처럼 줄여 쓰여 있고 ‘/’로 이어져 있었다. 원문항처럼 조건을 풀어 쓰고 한 줄에 하나씩 나눴다. 보기와 정답은 그대로다.")
