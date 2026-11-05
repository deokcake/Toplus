# 2026-10-26 전체 감수 반영 — 2급. 규칙은 z9a와 같다.
MEMO6 = "감수 메모 반영(10-26): "
def OKS(items, a): return [w + OK(i + 1, a) for i, w in enumerate(items)]
def ADD(g_, n_, t_, more): return (OLD(g_, n_, t_).get("s", "") + " " + more).strip()
def PJ(*lines): return ["문장별 판정: " + l for l in lines]
CNT = ["1개", "2개", "3개", "4개", "5개"]
LEN = MEMO6 + "원문항보다 짧던 문장을 원문항 길이 이상으로 늘렸다. 틀린 곳과 정답은 그대로다."
LENP = MEMO6 + "원문항보다 짧던 지문을 원문항 길이 이상으로 늘렸다. 보기와 정답은 그대로다."
LENC = MEMO6 + "원문항보다 짧던 보기 문장을 원문항 길이 이상으로 늘렸다. 정답 위치는 그대로다."
def L(g_, n_, t_, **kw): RE(g_, n_, t_, s=ADD(g_, n_, t_, kw.pop("why", LEN)), **kw)
def PRE(g_, n_, t_, rep): return [x if x not in rep else rep[x] for x in [rep.get(y, y) for y in OLD(g_, n_, t_)["pre"]]]
def PREs(g_, n_, t_, *pairs):
    out = []
    for x in OLD(g_, n_, t_)["pre"]:
        for a_, b_ in pairs: x = x.replace(a_, b_)
        out.append(x)
    return out

# 2-4 D·F
RE(2, 4, "D", c=["They wanted me to help with the school festival.", "The teacher let us leave early after the test.", "She found the book about space very useful.", "We let the children to play outside in the yard.", "I heard the baby crying in the next room."], a=4,
   n=OKS(["want + 목적어 + to부정사로 목적격 보어를 바르게 썼으므로", "사역동사 let + 목적어 + 동사원형으로 바르게 썼으므로", "find + 목적어 + 형용사 보어로 바르게 썼으므로", "사역동사 let 뒤 목적격 보어에는 to부정사가 아니라 동사원형(play)을 써야 하므로", "지각동사 hear + 목적어 + 현재분사로 바르게 썼으므로"], 4), s=ADD(2, 4, "D", LENC))
RE(2, 4, "F", c=["The long walk in the hot sun made us tiredly.", "I saw the boy dancing on the stage at the festival.", "She kept the window open all night long.", "We heard someone knocking on the front door.", "The teacher made us practice the song again."], a=1,
   n=OKS(["make + 목적어 뒤 목적격 보어 자리에는 부사가 아니라 형용사(tired)를 써야 하므로", "지각동사 see + 목적어 + 현재분사로 바르게 썼으므로", "keep + 목적어 + 형용사 보어로 바르게 썼으므로", "지각동사 hear + 목적어 + 현재분사로 바르게 썼으므로", "사역동사 make + 목적어 + 동사원형으로 바르게 썼으므로"], 1), s=ADD(2, 4, "F", LENC))

# 2-5 E·F
L(2, 5, "E", p="Jane: He showed me the photo of his family. 'show'가 간접목적어 'me'와 직접목적어 'the photo'를 취한 4형식 문장이에요.\nBen: I heard her sing a song in the hall. 지각동사 'hear' 뒤 목적격 보어 자리에 원형부정사 'sing'을 쓴 옳은 문장이에요.\nSora: We made lunch to the children at home. 'make'를 3형식으로 바꿀 때는 'to'를 쓰므로 옳은 문장이에요.\nMin: They elected Tom president of the class. 'president'는 목적어 'Tom'을 보충 설명하는 목적격 보어예요.\nHana: The milk in the fridge smells sourly. 감각동사 'smell' 뒤 보어 자리에는 부사 'sourly'를 쓰는 것이 맞아요.",
  pre=PREs(2, 5, "E", ("made lunch for the children)", "made lunch for the children at home)")), why=LENP)
L(2, 5, "F", p="Mina: She taught us English at the summer camp. 'teach'가 간접목적어 'us'와 직접목적어 'English'를 취한 4형식 문장이에요.\nLeo: The funny joke made me laugh. 사역동사 'make' 뒤 목적격 보어로 원형부정사 'laugh'를 쓴 옳은 문장이에요.\nJane: I bought flowers to my teacher on her birthday. 'buy'를 3형식으로 바꿀 때는 받는 사람 앞에 'to'를 쓰므로 옳은 문장이에요.\nTom: We found the window broken this morning. 창문이 깨진 수동의 관계이므로 목적격 보어로 과거분사 'broken'을 쓴 것이 맞아요.\nAmy: The room looks quietly at night. 감각동사 'look' 뒤에는 부사 'quietly'를 써야 하므로 옳은 문장이에요.",
  pre=PREs(2, 5, "F", ("bought flowers for my teacher)", "bought flowers for my teacher on her birthday)")), why=LENP)

# 2-9 D·F
L(2, 9, "D", p="Our report was full of mistakes. The teacher made us <u>to rewrite</u> the report by Friday.", why=LENP)
L(2, 9, "F", p="We had a lot of work this week. The manager made the staff <u>to work</u> overtime every day.", why=LENP)

# 2-10 D·E·F
L(2, 10, "D", p="A: Wow, your room looks different and much brighter than before. Did you paint it yourselves?\nB: No, we (<u>    A    </u>) last weekend by a professional painter.\nA: It's great! I want to (<u>    B    </u>) my room painted too.", why=LENP)
L(2, 10, "E", p="A: Your old watch is working again! Did you repair it by yourself?\nB: No, I (<u>    A    </u>) at the shop near the station yesterday.\nA: Great idea. My watch stopped last week, so I should also (<u>    B    </u>) mine fixed there soon.", why=LENP)
L(2, 10, "F", p="A: Your new profile photo looks really professional. Where did you take it?\nB: Thanks! I (<u>    A    </u>) at a studio downtown last month.\nA: I want to (<u>    B    </u>) my picture taken there for my job application.", why=LENP)

# 2-16 D·E·F
L(2, 16, "D", p="We <u>are owning</u> this apartment near the river.")
L(2, 16, "E", p="Tom <u>is resembling</u> his father in many ways.", k="‘닮다(resemble)’는 상태를 나타내는 동사라 진행형으로 쓰지 않는다. 3인칭 단수 주어에 맞춰 resembles로 고친다. 완성문: Tom resembles his father in many ways.")
L(2, 16, "F", p="They <u>are needing</u> more time to finish the project.")

# 2-17 E·F
L(2, 17, "E", p="Someone heard the baby crying upstairs late at night.\n→ The baby _____ _____ _____ upstairs late at night.", why=LENP)
L(2, 17, "F", p="They saw two students running away from the school gate.\n→ Two students _____ _____ _____ away from the school gate.", why=LENP)

# 2-18 D·E·F
L(2, 18, "D", p="(A) I'll tell you right away if I <u>find</u> your lost key.\n(B) We will leave for the airport when Tom <u>will get</u> here.\n(C) If it <u>will snow</u> heavily tomorrow morning, our school will close.\n(D) I'll stay in my seat quietly until the movie finally <u>ends</u>.")
L(2, 18, "E", p="(A) When Jane <u>finishes</u> her math homework, we'll go to the park together.\n(B) If the weather <u>is</u> good this weekend, we'll go hiking.\n(C) I'll call you right after I <u>will arrive</u> at the station.\n(D) We won't start the important meeting until everyone <u>will come</u> here.")
L(2, 18, "F", p="(A) If he <u>will be</u> late again, we'll start the game without him.\n(B) I'll text you when I <u>reach</u> the station near your house tonight.\n(C) We'll eat dinner together after Mom <u>gets</u> home from work.\n(D) Unless it <u>will rain</u> this afternoon, we'll play soccer outside.")

# 2-19 D·E·F: 보기를 원문항처럼 (A)와 (B)를 함께 견주는 설명으로(단조로움·짧음)
L19 = MEMO6 + "보기가 짧고 한쪽 문장만 말해 단조로웠다. 원문항처럼 한 보기에서 (A)와 (B)를 함께 견주는 설명으로 다시 썼고, <보기> 문장도 늘렸다. 정답 위치는 그대로다."
RE(2, 19, "D", p="<보기>\n(A) We missed the last train at 8 last night.\n(B) We have missed the last train.",
   c=["(A)는 과거의 사건이 현재까지 영향을 미치는 현재완료이고, (B)는 과거의 특정 시점에 중점을 두는 단순과거이다.", "(A)는 지금도 기차를 기다리고 있다는 뜻이고, (B)는 기차를 놓친 일이 이미 끝나 현재와 관계가 없다는 뜻이다.", "(A)는 어젯밤 8시라는 특정 과거 시점의 사건이고, (B)는 기차를 놓친 결과가 현재까지 이어지는 상황을 나타낸다.", "(A)는 'at 8 last night' 때문에 틀린 문장이고, (B)는 'have + 과거형'으로 이루어진 과거완료 시제이다.", "(A)와 (B)는 모두 현재완료 진행형으로, 기차를 놓친 동작이 지금도 계속되고 있음을 똑같이 나타낸다."], a=3,
   n=OKS(["(A)가 단순과거, (B)가 현재완료인데 거꾸로 설명했으므로", "(A)는 끝난 과거의 일이고, 현재와 관련된 결과를 나타내는 것은 (B)이므로", "(A)는 특정 과거 시점의 단순과거, (B)는 결과가 지금까지 이어지는 현재완료로 바르게 설명했으므로", "(A)는 과거 시점과 함께 쓴 옳은 단순과거이고, (B)는 have + 과거분사의 현재완료이므로", "두 문장 모두 진행형이 아니고 뜻도 서로 다르므로"], 3), s=ADD(2, 19, "D", L19))
RE(2, 19, "E", p="<보기>\n(A) Jane lost her house key last night.\n(B) Jane has lost her house key.",
   c=["(A)는 last night라는 과거 시점에 일어난 일만 말하고, (B)는 열쇠를 잃어버린 결과 지금도 열쇠가 없다는 점을 중심으로 한다.", "(A)는 열쇠를 이미 되찾았다는 뜻을 분명히 나타내고, (B)는 열쇠를 잃어버리는 동작이 지금도 진행 중임을 나타낸다.", "(A)는 현재완료의 결과 용법이고 (B)는 단순과거이므로, 두 문장의 뜻 차이는 전혀 없다.", "(A)의 lost를 had lost로 바꾸면 (B)와 같은 뜻이 되고, (B)의 has를 had로 바꿔도 시제가 달라지지 않는다.", "(A)는 과거 시점 표현이 있으므로 과거완료로 바꿔야 어법상 옳고, (B)만 올바른 문장이다."], a=1,
   n=OKS(["(A)는 과거 시점의 사건, (B)는 지금까지 이어지는 결과를 나타낸다고 바르게 설명했으므로", "(A)는 되찾았는지 말하지 않고, (B)는 진행이 아니라 결과를 나타내므로", "(A)가 단순과거, (B)가 현재완료이고 두 문장은 뜻이 다르므로", "had lost는 과거완료라 (B)와 뜻이 다르고, has를 had로 바꾸면 시제가 달라지므로", "(A)는 last night와 함께 쓴 옳은 단순과거이므로"], 1), s=ADD(2, 19, "E", L19))
RE(2, 19, "F", p="<보기>\n(A) The small bookstore closed at nine last night.\n(B) The small bookstore has already closed.",
   c=["(A)는 서점이 지금도 닫혀 있다는 사실을 분명히 알려 주고, (B)는 서점이 문을 닫은 정확한 시각을 알려 준다.", "(A)와 (B)의 동사는 모두 과거형이므로, 두 문장은 시제와 뜻이 완전히 같은 단순과거 문장이다.", "(A)는 '9시'라는 시간 표현 때문에 틀린 문장이고, (B)만 어법상 올바른 문장이다.", "(A)는 9시 이후 지금까지 계속 닫혀 있음을 나타내는 현재완료이고, (B)는 과거의 한 시점에 닫힌 일이다.", "(A)는 어젯밤 9시라는 과거 시점에 닫힌 사건을 말하고, (B)는 문을 닫은 결과 지금 닫혀 있는 상태를 나타낸다."], a=5,
   n=OKS(["(A)는 지금 상태를 말하지 않고, (B)에는 시각이 나오지 않으므로", "(B)는 has + 과거분사의 현재완료라 (A)와 시제가 다르므로", "(A)는 과거 시점과 함께 쓴 옳은 단순과거이므로", "(A)가 단순과거, (B)가 현재완료인데 거꾸로 설명했으므로", "(A)는 과거 시점의 사건, (B)는 지금까지 이어지는 결과를 나타낸다고 바르게 설명했으므로"], 5), s=ADD(2, 19, "F", L19 + " (같은 번호 D·E의 메모와 같은 문제)"))

# 2-20 D·F: 문장 늘리기(문장별 판정을 새로 씀)
ST20 = "다음 중 어법상 옳은 문장의 개수는?"
RE(2, 20, "D", st=ST20, p="(가) We have met Jane at the library two days ago.\n(나) Does he play tennis with his friends every weekend?\n(다) They have stayed in this hotel for a month.\n(라) Mina has lost her keys, so she can't open the door.\n(마) When did you see him at the station?",
   c=CNT, a=4, pre=PJ("(가) 틀림: two days ago 같은 끝난 과거 시점에는 현재완료를 쓰지 않는다. We met Jane at the library two days ago.", "(나) 옳음: Does + 주어 + 동사원형의 의문문이다.", "(다) 옳음: for와 함께 쓴 계속의 현재완료이다.", "(라) 옳음: 잃어버린 결과 지금 문을 열 수 없는 결과의 현재완료이다.", "(마) 옳음: when 의문문은 현재완료가 아니라 과거형으로 쓴다."),
   k="어법상 옳은 문장은 (나), (다), (라), (마)로 4개이다.", n="cnt", s=ADD(2, 20, "D", LEN))
RE(2, 20, "F", st=ST20, p="(가) Jane has called me about the party last night.\n(나) Does the first train leave at seven every morning?\n(다) He has studied English for ten years in Korea.\n(라) They have already finished their science project.\n(마) When did Tom arrive at the airport yesterday?",
   c=CNT, a=4, pre=PJ("(가) 틀림: last night 같은 끝난 과거 시점에는 현재완료를 쓰지 않는다. Jane called me about the party last night.", "(나) 옳음: Does + 주어 + 동사원형의 의문문이다.", "(다) 옳음: for와 함께 쓴 계속의 현재완료이다.", "(라) 옳음: already와 함께 쓴 완료의 현재완료이다.", "(마) 옳음: when 의문문은 과거형으로 쓴다."),
   k="어법상 옳은 문장은 (나), (다), (라), (마)로 4개이다.", n="cnt", s=ADD(2, 20, "F", LEN))

# 2-22 E·F
L(2, 22, "E", p="• There _____ be a small theater on this corner, but it closed ten years ago.\n• Dad _____ take us fishing at the lake on Sundays when we were little.", why=LENP)
L(2, 22, "F", p="• Mina _____ live in Busan with her grandparents, but now she lives in Seoul.\n• She _____ ride her bike to school every day when she was a middle school student.", why=LENP)

# 2-24 D·E·F
L(2, 24, "D", p="Amy: Ben says the old empty house on our street is full of people tonight.\nMina: <u>That can't be right.</u> Nobody has lived there for years.", why=LENP)
L(2, 24, "E", p="Leo: Did you hear that? Tom says the sun rose in the west this morning.\nJane: <u>It cannot be true.</u> The sun always rises in the east.", why=LENP)
L(2, 24, "F", p="Sora: Do you know Minsu? He says he never sleeps, even before big exams.\nMina: <u>That can't be true.</u> He always looks tired. Everyone needs sleep.", why=LENP)

# 2-28 D·E·F
L(2, 28, "D", c=["Tom may to come to the party a little later.", "You should wear a helmet when you ride a bike.", "She could solve the difficult math problem easily.", "I will be able to help you with your homework.", "We had to stay home all day because of the storm."], why=LENC)
L(2, 28, "E", c=["Do we have to bring our own lunch to school tomorrow?", "They should studies harder for the final exam next week.", "Mom might be at the store near our house now.", "You must not tell anyone about the surprise party.", "He was able to fix the old car by himself."], why=LENC)
L(2, 28, "F", c=["Can you help me move this heavy box to the second floor?", "She doesn't have to cook dinner for us tonight.", "We would often play soccer in the park after school.", "I could went there alone when I was ten.", "You had better take a taxi because it is late."], why=LENC)

# 2-29 D
L(2, 29, "D", p="Jane ⒜<u>would be</u> very shy as a child at school.\n→ ⒝<u>used to be</u>", why=LENP)

# 2-31 E·F
L(2, 31, "E", p="The important documents _____ before the meeting began this morning.", why=LENP)
L(2, 31, "F", p="The winners of the contest _____ at tomorrow's ceremony.", why=LENP)

# 2-32 D·E·F
L(2, 32, "D", p="A: Did Tom _____ this article about climate change?\nB: No, it _____ by Jane for the school newspaper last month.", why=LENP)
L(2, 32, "E", p="A: Did they _____ this meeting room? It looks very clean.\nB: No, it _____ by the staff early this morning.", why=LENP)
L(2, 32, "F", p="A: Did Mina _____ this beautiful photo of the sea?\nB: No, it _____ by her brother last summer.", why=LENP)

# 2-36 E·F
L(2, 36, "E", p="A: Who took this old photograph of our family?\nB: It _____ by my grandfather when he was young.", why=LENP)
L(2, 36, "F", p="A: Who designed this beautiful building near the river?\nB: It _____ by a young architect from Seoul in 2010.", why=LENP)

# 2-37 D·F: 문장과 보기를 원문항 길이로
N37 = lambda verb, part, subj: ["지각동사의 수동태에서 to 뒤에는 동사원형이 오므로 to + -ing는 쓸 수 없으므로", "과거의 일이므로 현재형 수동태를 쓸 수 없으므로", f"지각동사 {verb}의 현재분사 보어({part})는 수동태에서도 그대로 두므로", "원형부정사 보어는 수동태에서 to부정사가 되므로 동사원형을 그대로 쓸 수 없으므로", f"주어 {subj}가 동작을 받는 것이므로 진행형이 아니라 be동사 + 과거분사를 써야 하므로"]
RE(2, 37, "D", p="We heard Tom playing the guitar in his room last night.",
   c=["Tom was heard to playing the guitar in his room last night by us.", "Tom is heard playing the guitar in his room last night by us.", "Tom was heard playing the guitar in his room last night by us.", "Tom was heard play the guitar in his room last night by us.", "Tom was hearing playing the guitar in his room last night by us."], a=3,
   n=OKS(N37("hear", "playing", "Tom"), 3), s=ADD(2, 37, "D", LEN))
RE(2, 37, "F", p="They watched the dancer performing on the big stage at the festival.",
   c=["The dancer was watched perform on the big stage at the festival by them.", "The dancer was watched performing on the big stage at the festival by them.", "The dancer was watched to performing on the big stage at the festival by them.", "The dancer is watched performing on the big stage at the festival by them.", "The dancer was watching performing on the big stage at the festival by them."], a=2,
   n=OKS([N37("watch", "performing", "The dancer")[i] for i in (3, 2, 0, 1, 4)], 2), s=ADD(2, 37, "F", LEN))

# 2-41 E
L(2, 41, "E", p="I bought two notebooks at the store. One is for math, and _____ is for science.", why=LENP)

# 2-44 D·E·F: 정답만 주어 바로 뒤에 재귀대명사가 있어 위치로 정답이 드러남 → 강조 용법을 문장 끝에
L44 = MEMO6 + "정답 보기만 주어 바로 뒤에 재귀대명사가 있어 위치만 보고도 정답을 고를 수 있었다. 원문항처럼 강조 용법을 문장 끝에 두고, 보기 문장도 원문항 길이로 늘렸다. 정답 위치는 그대로다."
REFL = "재귀대명사가 {}의 목적어로 쓰인 재귀 용법이라 <보기>(강조 용법)와 다르므로"
EMPH = "완전한 문장 뒤에 붙어 ‘직접, 스스로’라는 뜻을 더하는 강조 용법이라 <보기>와 같으므로"
RE(2, 44, "D", c=["She cut <u>herself</u> on the broken glass yesterday.", "We prepared the whole meal for the party <u>ourselves</u>.", "I bought <u>myself</u> a new watch last week.", "They talked about <u>themselves</u> for hours at dinner.", "Make <u>yourself</u> at home and enjoy the food."], a=2,
   n=OKS([REFL.format("동사 cut"), EMPH, REFL.format("동사 bought(간접목적어)"), REFL.format("전치사 about"), "Make yourself at home은 관용 표현으로 make의 목적어 자리에 쓴 재귀 용법이라 <보기>와 다르므로"], 2), s=ADD(2, 44, "D", L44))
RE(2, 44, "E", c=["She was talking to <u>herself</u> in the empty classroom.", "I told <u>myself</u> not to give up on my dream.", "They dried <u>themselves</u> with towels after swimming.", "Be careful not to burn <u>yourself</u> on the stove.", "Tom wrote the whole graduation speech <u>himself</u>."], a=5,
   n=OKS([REFL.format("전치사 to"), REFL.format("동사 told"), REFL.format("동사 dried"), REFL.format("동사 burn"), EMPH], 5), s=ADD(2, 44, "E", L44))
RE(2, 44, "F", c=["You fixed the broken chair in the kitchen <u>yourself</u>.", "He considers <u>himself</u> lucky to have such good friends.", "We found <u>ourselves</u> in a strange town at midnight.", "She pushed <u>herself</u> hard to finish the race.", "Please behave <u>yourselves</u> in the museum, children."], a=1,
   n=OKS([EMPH, REFL.format("동사 considers"), REFL.format("동사 found"), REFL.format("동사 pushed"), "behave yourselves는 관용 표현으로 behave의 목적어 자리에 쓴 재귀 용법이라 <보기>와 다르므로"], 1), s=ADD(2, 44, "F", L44 + " (같은 번호 D·E의 메모와 같은 문제)"))

# 2-50 D·E·F
L(2, 50, "D", p="(A) All of the news about the accident <u>were</u> shocking.\n(B) Each of the players on the team <u>wears</u> a number.\n(C) Most of the milk in the bottle <u>has</u> gone bad.\n(D) All of the windows in the classroom <u>was</u> open.\n(E) One of the teachers at our school <u>is</u> from Canada.")
L(2, 50, "E", p="(A) All of the homework for today <u>are</u> done.\n(B) Each of us in the class <u>is</u> ready for the test.\n(C) Some of the books on the shelf <u>are</u> missing.\n(D) Most of the birthday cake <u>were</u> eaten by the children.\n(E) All of the students in my class <u>was</u> tired after the trip.")
L(2, 50, "F", p="(A) All of the luggage on the plane <u>was</u> lost.\n(B) Each of the classrooms in this building <u>have</u> a projector.\n(C) One of the boys in my class <u>plays</u> the violin.\n(D) All of my old shoes in the closet <u>is</u> dirty.\n(E) Most of the people in this town <u>agree</u> with you.")

# 2-55 D: ‘평가해서’ → ‘사람의 성격을 나타내는 형용사라서’, 예문 늘리기. F도 같은 낱말
RE(2, 55, "D", p="Jane: I need some paper to write on for the letter. 은 종이 위에 쓰는 것이라 on이 필요해요.\nBen: She has no friend to talk at school. 는 전치사 없이도 옳은 문장이에요.\nSora: It was careless of him to forget the key. 는 careless가 사람의 성격을 나타내는 형용사라서 of를 썼어요.\nTom: This book is easy enough for children to read alone. 에서 for children은 to read의 의미상 주어예요.\nAmy: The bag is too heavy for I to carry upstairs. 는 의미상 주어를 주격으로 써서 옳아요.",
   pre=PREs(2, 55, "D", ("성품 평가 형용사 careless", "사람의 성격을 나타내는 형용사 careless")),
   s=ADD(2, 55, "D", MEMO6 + "Sora의 설명에서 ‘평가해서’를 메모대로 ‘사람의 성격을 나타내는 형용사라서’로 고치고, 원문항보다 짧던 예문을 늘렸다. 정답은 그대로다."))
RE(2, 55, "F", pre=PREs(2, 55, "F", ("성품 평가 형용사라", "사람의 성격을 나타내는 형용사라")), s=ADD(2, 55, "F", MEMO6 + "같은 번호 D의 메모에 맞춰 해설의 ‘성품 평가 형용사’를 ‘사람의 성격을 나타내는 형용사’로 고쳤다."))

# 2-59 D·F
RE(2, 59, "D", p="<보기>\nThe box was very light.\nTom could carry it alone to his room.\n(‘be ~ enough to ~’구문을 활용할 것)", c=[x.replace("carry alone.", "carry alone to his room.").replace("carrying alone.", "carrying alone to his room.") for x in OLD(2, 59, "D")["c"]], s=ADD(2, 59, "D", LEN))
RE(2, 59, "F", p="<보기>\nThe road was very wide.\nTwo cars could pass each other safely.\n(‘be ~ enough to ~’구문을 활용할 것)", c=[x.replace("pass safely.", "pass each other safely.").replace("passing safely.", "passing each other safely.") for x in OLD(2, 59, "F")["c"]], s=ADD(2, 59, "F", LEN))

# 2-60 D·E·F
L(2, 60, "D", p="<보기>\n(A) The train is to leave the station at nine tomorrow morning.\n(B) You are to wear a helmet in this area at all times.\n(C) If she is to improve her skills, she must practice more.\n(D) No one was to be found in the building after midnight.\n(E) They were never to meet each other again.")
L(2, 60, "E", p="<보기>\n(A) The school concert is to be held in the main hall tomorrow.\n(B) You are to keep this secret from everyone.\n(C) If Tom is to win the race, he must train harder.\n(D) Her voice was not to be heard in the noise of the crowd.\n(E) The old ship was never to return to its home port.")
L(2, 60, "F", p="<보기>\n(A) The guests are to arrive at the hotel at six this evening.\n(B) We are to finish the project before lunch today.\n(C) If Jane is to pass the exam, she must study every day.\n(D) The key to the front door was nowhere to be found.\n(E) He was never to recover from the illness.")

# 2-63 D·F: 정답만 be동사 뒤 -ing라 쉽게 드러남 → be동사 뒤 동명사 보어를 오답에 넣음
L63 = MEMO6 + "정답 보기만 be동사 바로 뒤에 -ing가 있어 쉽게 고를 수 있었다. be동사 뒤에 있지만 ‘~하는 것’으로 풀리는 동명사 보어를 오답에 넣었다. 정답 위치는 그대로다."
GER = "{}로 쓰인 동명사라 나머지와 같으므로"; PART = "be동사와 함께 ‘~하고 있다’는 진행형을 만드는 현재분사라 나머지(동명사)와 쓰임이 다르므로"
RE(2, 63, "D", c=["I don't mind <u>waiting</u> here for a few minutes.", "My favorite hobby is <u>collecting</u> old coins from other countries.", "The children are <u>playing</u> outside in the yard now.", "<u>Keeping</u> a diary every day is a good habit.", "She is proud of <u>being</u> a nurse at the hospital."], a=3,
   n=OKS([GER.format("mind의 목적어"), "be동사 뒤에 있지만 ‘모으는 것’이라는 뜻의 보어로 쓰인 동명사라 나머지와 같으므로", PART, GER.format("문장의 주어"), GER.format("전치사 of의 목적어")], 3), s=ADD(2, 63, "D", L63))
RE(2, 63, "F", c=["He is interested in <u>learning</u> Spanish and French.", "<u>Taking</u> a walk after dinner is relaxing and healthy.", "His job is <u>teaching</u> science at a middle school.", "I'm tired of <u>hearing</u> the same song every morning.", "We are <u>watching</u> a movie in the living room now."], a=5,
   n=OKS([GER.format("전치사 in의 목적어"), GER.format("문장의 주어"), "be동사 뒤에 있지만 ‘가르치는 것’이라는 뜻의 보어로 쓰인 동명사라 나머지와 같으므로", GER.format("전치사 of의 목적어"), PART], 5), s=ADD(2, 63, "F", L63 + " (같은 번호 D의 메모와 같은 문제)"))

# 2-64 D·E·F: 정답만 -ing라 형태로 드러남 → 오답에도 -ing형을 넣되 앞의 전치사 to가 빠진 꼴로(밑줄에 포함)
L64 = MEMO6 + "정답 보기만 -ing형이라 형태만 보고 고를 수 있었다. 오답에도 -ing형을 넣고, look forward to·be used to의 전치사 to가 빠진 꼴로 밑줄 안에서 틀리게 했다. 정답 위치는 그대로다."
GOOD = "전치사 {} 뒤에 동명사 {}을(를) 바르게 썼으므로"
RE(2, 64, "D", c=["We talked about <u>go</u> camping by the lake this summer.", "We are interested in <u>learning</u> French at the community center.", "He is proud of <u>to win</u> the first prize in the contest.", "I'm looking <u>forward seeing</u> you again at the reunion.", "They are <u>used getting</u> up early on school days."], a=2,
   n=OKS(["전치사 about 뒤에는 동사원형이 아니라 동명사 going을 써야 하므로", "전치사 in 뒤에 동명사 learning을 바르게 썼으므로", "전치사 of 뒤에는 to부정사가 아니라 동명사 winning을 써야 하므로", "-ing형은 맞지만 look forward to의 전치사 to가 빠졌다. forward to seeing으로 써야 하므로", "-ing형은 맞지만 be used to의 전치사 to가 빠졌다. used to getting으로 써야 하므로"], 2), s=ADD(2, 64, "D", L64))
RE(2, 64, "E", c=["He left the room without <u>close</u> the door behind him.", "How about <u>to take</u> a taxi to the airport instead?", "Jane apologized for <u>being</u> late for the important meeting.", "I'm looking <u>forward hearing</u> from you very soon.", "She is <u>used reading</u> poems before going to bed."], a=3,
   n=OKS(["전치사 without 뒤에는 동사원형이 아니라 동명사 closing을 써야 하므로", "전치사 about 뒤에는 to부정사가 아니라 동명사 taking을 써야 하므로", "전치사 for 뒤에 동명사 being을 바르게 썼으므로", "-ing형은 맞지만 look forward to의 전치사 to가 빠졌다. forward to hearing으로 써야 하므로", "-ing형은 맞지만 be used to의 전치사 to가 빠졌다. used to reading으로 써야 하므로"], 3), s=ADD(2, 64, "E", L64))
RE(2, 64, "F", c=["He kept me from <u>making</u> a serious mistake on the test.", "Instead of <u>take</u> the bus, we walked to the station.", "I dream of <u>to become</u> a pilot someday.", "We are looking <u>forward visiting</u> our grandparents this winter.", "My dad is <u>used driving</u> long distances for work."], a=1,
   n=OKS(["전치사 from 뒤에 동명사 making을 바르게 썼으므로", "전치사 of 뒤에는 동사원형이 아니라 동명사 taking을 써야 하므로", "전치사 of 뒤에는 to부정사가 아니라 동명사 becoming을 써야 하므로", "-ing형은 맞지만 look forward to의 전치사 to가 빠졌다. forward to visiting으로 써야 하므로", "-ing형은 맞지만 be used to의 전치사 to가 빠졌다. used to driving으로 써야 하므로"], 1), s=ADD(2, 64, "F", L64 + " (같은 번호 D·E의 메모와 같은 문제)"))

# 2-65 E: ⓔ(need -ing의 수동 뜻)가 중2 수준을 넘는다 → 같은 판정(옳음)의 쉬운 문장으로
RE(2, 65, "E", p=OLD(2, 65, "E")["p"].replace("ⓔ The old problem needs solving as soon as possible.", "ⓔ My little brother is good at drawing animals and flowers."),
   pre=[x.replace("ⓔ O. need -ing은 ‘~될 필요가 있다’는 수동의 뜻이다.", "ⓔ O. 전치사(at) 뒤에 동명사 drawing을 썼다.") for x in OLD(2, 65, "E")["pre"]],
   s=ADD(2, 65, "E", MEMO6 + "ⓔ(need -ing의 수동 뜻)가 중학교 2학년 수준을 넘는다는 메모에 따라 같은 옳은 문장인 be good at -ing로 바꿨다. 정답은 그대로다."))

# 2-66 E·F
L(2, 66, "E", p="Do you mind ______ (move) your bag? I want to sit here.", why=LENP)
L(2, 66, "F", p="Would you mind ______ (help) me with this heavy box? It's too big.", why=LENP)

# 2-68 D·E·F
L(2, 68, "D", p="A: Are you hungry? We have been studying in the library for hours.\nB: Yes, I feel like (A)________ something warm and spicy.\nA: Then how about (B)________ soup together in the kitchen?", why=LENP)
L(2, 68, "E", p="A: What do you want to do this afternoon?\nB: I feel like (A)________ outside because the weather is nice.\nA: Good. I'm thinking of (B)________ along the river with you.", why=LENP)
L(2, 68, "F", p="A: What about this weekend? Do you have any plans?\nB: Not really. I feel like (A)________ at home all day.\nA: Me too. I prefer (B)________ a book on rainy days.", why=LENP)

# 2-70 D·E·F
L(2, 70, "D", p="<보기>\nⓐ I forgot meeting him before, but he remembered me at once.\nⓑ She stopped talk when the teacher entered the classroom.\nⓒ We regret to inform you that your application failed this time.\nⓓ He is used to work late at the office.\nⓔ They avoided to answer the reporter's difficult questions.",
  pre=PREs(2, 70, "D", ("She stopped talking when the teacher entered.", "She stopped talking when the teacher entered the classroom."), ("He is used to working late.", "He is used to working late at the office."), ("They avoided answering.", "They avoided answering the reporter's difficult questions.")))
L(2, 70, "E", p="<보기>\nⓐ Tom remembered call Mina yesterday about the party.\nⓑ I tried opening the window to cool the hot room.\nⓒ Jane stopped to rest for ten minutes during the hike.\nⓓ It is no good argue with him about the rules.\nⓔ We are looking forward to see you at the wedding.",
  pre=PREs(2, 70, "E", ("Tom remembered calling Mina yesterday.", "Tom remembered calling Mina yesterday about the party."), ("It is no good arguing with him.", "It is no good arguing with him about the rules."), ("We are looking forward to seeing you.", "We are looking forward to seeing you at the wedding.")))
L(2, 70, "F", p="<보기>\nⓐ She regrets saying those rude words to her friend.\nⓑ I forgot to turn off the oven before I left home.\nⓒ Tom stopped playing soccer because of his knee injury.\nⓓ We tried to use a different key, but the door stayed locked.\nⓔ This novel is worth to read twice.",
  pre=PREs(2, 70, "F", ("It is worth reading twice.", "This novel is worth reading twice.")))

# 2-72 D·E·F
L(2, 72, "D", p="• Mina looked ____ during the long history lecture this morning.\n• The lecture about old kings was really ____.")
L(2, 72, "E", p="• We were ____ by the sudden noise in the dark hallway.\n• It was a very ____ sound at midnight.")
L(2, 72, "F", p="• Tom felt ____ after the long trip to Busan.\n• The six-hour trip by bus was extremely ____.")

# 2-75 D
L(2, 75, "D", p=OLD(2, 75, "D")["p"].replace("to warm up.", "to warm up. It was her first visit, and the café was quieter than she had expected."), why=LENP)

# 2-82 D·F
L(2, 82, "D", p="이 가죽 가방은 내 배낭보다 훨씬 더 무겁다.\nThis leather bag is _____ heavier than my backpack.", why=LENP)
L(2, 82, "F", p="오늘 아침 날씨는 어제 아침보다 훨씬 더 춥다.\nThe weather this morning is _____ colder than yesterday morning.", why=LENP)

# 2-89 E·F
L(2, 89, "E", p="<보기>\n(A) One of the best <u>restaurants</u> in our city is near the station.\n(B) He is one of the richest <u>man</u> in our small town.\n(C) One of my <u>cousins</u> is a pilot for a big airline.\n(D) This is one of the easiest <u>question</u> on the math test.\n(E) She is one of the kindest <u>woman</u> I have ever met in my life.")
L(2, 89, "F", p="<보기>\n(A) One of the most interesting <u>story</u> in this book is about space.\n(B) Tom is one of the tallest <u>boys</u> in our class this year.\n(C) One of the <u>child</u> in the playground is crying loudly now.\n(D) Jeju is one of the most popular <u>island</u> in Korea for tourists.\n(E) One of my favorite <u>songs</u> is playing on the radio now.")

# 2-91 C·D·F: 원문항처럼 문장 앞에 • 표시, 문장 늘리기
L91 = MEMO6 + "원문항처럼 문장 앞에 • 표시를 넣고, 원문항보다 짧던 문장을 늘렸다. 보기와 정답은 그대로다."
L(2, 91, "C", p="• This is the small town _____ my father grew up as a child.\n• I still remember the day _____ we first met at school.", why=L91)
L(2, 91, "D", p="• Tell me the reason _____ Tom left the meeting so early.\n• This is the quiet cafe _____ we usually study after school.", why=L91)
L(2, 91, "F", p="• I understand the reason _____ the outdoor event was canceled.\n• Summer is the season _____ many people travel to the beach.", why=L91)

# 2-100 E·F
L(2, 100, "E", p="(가) I remember what Jane told me yesterday.\n(나) The song that he wrote for his mother is beautiful.\n(다) What Mina bought it at the mall was expensive.\n(라) The thing what I need now is time.\n(마) All that matters in this game is effort.")
L(2, 100, "F", p="(가) Tell me what did you see at the museum.\n(나) The place where we stayed last summer was crowded.\n(다) What he decided at the meeting was unexpected.\n(라) I know what that she really wants.\n(마) Everything that Tom owns is very old.",
  pre=PREs(2, 100, "F", ("what you saw로", "what you saw at the museum으로")))

# 2-102 D·E: 같은 동사를 두 번 쓰던 것을 서로 다른 동사로(더 다채롭게), 문장 늘리기
RE(2, 102, "D", p="Mina picked _____ the package at the post office.\nPlease turn _____ the volume a little; I can't hear it.",
   n=OKS(["pick up(찾아오다)과 turn up(소리를 키우다) 모두 up이 알맞으므로", "pick over·turn over는 ‘골라내다·뒤집다’라 문맥과 맞지 않으므로", "pick out·turn out은 ‘고르다·판명되다’라 문맥과 맞지 않으므로", "turn down은 소리를 줄이는 것이라 들리지 않는다는 말과 맞지 않으므로", "pick off·turn off는 소포를 찾거나 소리를 키우는 뜻이 아니므로"], 1),
   s=ADD(2, 102, "D", MEMO6 + "두 문장이 모두 pick up이라 단조로웠다. 메모대로 둘째 문장을 다른 동사(turn up)로 바꾸고 문장을 늘렸다. 정답 위치는 그대로다."))
RE(2, 102, "E", p="Tom turned _____ the job offer from the big company.\nPlease slow _____ ; you are driving too fast.",
   n=OKS(["turn out·slow out은 ‘판명되다’ 등으로 문맥과 맞지 않으므로", "turn over는 ‘뒤집다’라 제안을 거절하는 뜻이 아니므로", "turn off는 ‘끄다’라 제안을 거절하는 뜻이 아니므로", "turn up은 ‘나타나다·키우다’라 제안을 거절하는 뜻이 아니므로", "turn down(거절하다)과 slow down(속도를 줄이다) 모두 down이 알맞으므로"], 5),
   s=ADD(2, 102, "E", MEMO6 + "원문항보다 짧던 문장을 늘리고, 같은 번호 D의 메모(같은 동사를 되풀이함)에 맞춰 둘째 문장을 다른 동사(slow down)로 바꿨다. 정답 위치는 그대로다."))

# 2-103 D: 정답이 둘째 문장에 그대로 나옴 → 관계를 뒤집어야 답이 나오게. E: 길이
RE(2, 103, "D", p="The new school is _____ the big park.\n= The big park is behind the new school.", c=["behind", "under", "next to", "in front of", "across from"], a=4,
   n=OKS(["behind로 쓰면 학교가 공원 뒤에 있게 되어 뜻이 반대이므로", "under는 ‘아래에’라 두 건물의 위치 관계와 맞지 않으므로", "next to는 ‘옆에’라 앞뒤 관계를 나타내지 못하므로", "공원이 학교 뒤에 있으면 학교는 공원 앞에 있으므로", "across from은 ‘맞은편에’라 앞뒤 관계와 맞지 않으므로"], 4),
   s=ADD(2, 103, "D", MEMO6 + "정답(across from)이 둘째 문장에 그대로 나와 문항의 뜻이 없었다. 둘째 문장을 behind로 바꿔 관계를 뒤집어야 정답(in front of)이 나오게 했다." + pos(4)))
L(2, 103, "E", p="The little cat is sleeping _____ the bed.\n= The bed is above the little sleeping cat.", why=LENP)

# 2-104 E·F
L(2, 104, "E", c=["The lights went out <u>during we watched TV</u> last night.", "Our school was built <u>in 1995</u> by the city.", "I'll call you <u>at Tuesday</u> after school.", "The class ends <u>on 3:30</u> in the afternoon.", "Leaves turn red and yellow <u>at fall</u>."], why=LENC)
L(2, 104, "F", c=["Mina visited Paris with her family <u>on 2019</u>.", "We have lunch together <u>in noon</u> every day.", "I usually wake up <u>at dawn</u> on weekdays.", "They got married <u>at June</u> last year.", "The big game is <u>in Saturday afternoon</u> this week."], why=LENC)

# 2-107 D·E·F
L(2, 107, "D", p="A: This jigsaw puzzle is too hard for me. I want to stop now.\nB: Don't ____________! You're almost done. Just ten more pieces.", why=LENP)
L(2, 107, "E", p="A: It's freezing outside, and the wind is very strong today.\nB: You should ____________ your warm coat and gloves before you go out.", why=LENP)
L(2, 107, "F", p="A: The TV in the living room is still on, and nobody is watching it.\nB: Please ____________ the TV to save electricity.", why=LENP)

# 2-108 D·F
L(2, 108, "D", p="- Mina picked (<u>     A     </u>) the package at the post office this morning.\n- She is waiting (<u>     B     </u>) the bus at the stop now.", why=LENP)
L(2, 108, "F", p="- Please fill (<u>     A     </u>) this application form with a black pen.\n- Tom ran (<u>     B     </u>) of time and couldn't finish the math test.", why=LENP)

# 2-110 E(메모)·C·F: 밑줄을 원문항처럼 전치사 하나로(D는 확인 완료라 그대로)
L110 = MEMO6 + "밑줄이 원문항(전치사 하나)과 달리 뒤의 말까지 덮고 있어, 원문항처럼 전치사에만 밑줄을 쳤다. 정답은 그대로다."
def U110(p): return re.sub(r"<u>(\w+) ([^<]*)</u>", r"<u>\1</u> \2", p)
import re
for t_ in "CEF": RE(2, 110, t_, p=U110(OLD(2, 110, t_)["p"]), s=ADD(2, 110, t_, L110 + ("" if t_ == "E" else " (같은 번호 E의 메모와 같은 문제)")))

# 2-118 E·F
L(2, 118, "E", p="My older sister as well as I ________ very interested in modern art.", why=LENP)
L(2, 118, "F", p="Not only my brother but also I ________ going to the summer camp.", why=LENP)

# 2-120 D·E·F
L(2, 120, "D", p="<보기>\nⓐ Unless you study harder, you won't pass the final exam.\nⓑ Even though she was very tired, she continued working.\nⓒ I'll wait here at the station until Tom will come.\nⓓ Not only Mina but also her friends are here today.\nⓔ Both of my parents is working at the hospital.",
  pre=PREs(2, 120, "D", ("both parents는 복수이므로", "both of my parents는 복수이므로")))
L(2, 120, "E", p="<보기>\nⓐ If Jane finishes her work early, she will call you.\nⓑ Although it rained all day, we played soccer outside.\nⓒ Neither the boys nor Tom is ready for the trip.\nⓓ Both Mina and Jane are students at this school.\nⓔ We will eat dinner when Dad will get home from work.")
L(2, 120, "F", p="<보기>\nⓐ Unless it stops raining soon, we'll wait inside the house.\nⓑ Despite Tom was nervous, he spoke well in front of everyone.\nⓒ Either the teacher or the students is presenting the project today.\nⓓ Both of my brothers are tall and strong.\nⓔ I'll text you right after I will arrive at the airport.")

# 2-121 D
L(2, 121, "D", p="If I lived closer, I _____ to school with my friends every day.", why=LENP)

# 2-125 D·E·F
L(2, 125, "D", p="ⓐ Jane talks as if she were an expert on everything.\nⓑ If I were you, I will wait for a better chance.\nⓒ I wish I have seen the famous show last night.\nⓓ If Tom had called me, I would have answered the phone.\nⓔ Mina wishes she is a little taller than now.\nⓕ If he had asked me for help, I will help him.")
L(2, 125, "E", p="ⓐ He spends money as if he were very rich.\nⓑ If we have a car now, we would drive to the beach.\nⓒ I wish I knew the truth about the accident.\nⓓ If Jane had studied harder, she would have passed the exam.\nⓔ Tom wishes he had listened to his teacher.\nⓕ I wish it is Friday today, not Monday.")
L(2, 125, "F", p="ⓐ She acts as if she had seen the movie before.\nⓑ If I knew his phone number, I will call him now.\nⓒ I wish I am at home now with my family.\nⓓ If they had left earlier, they would arrive on time yesterday.\nⓔ Mina wishes she can fly like a bird.\nⓕ If it had snowed last night, we will make a snowman.",
  pre=PREs(2, 125, "F", ("I wish I were home now", "I wish I were at home now")))

# 2-130 D·E·F
RE(2, 130, "D", st="R", p="- I wish I had seen the concert with you last night.\n- She wishes she could drive her father's new car.\n- Tom speaks as if he were the boss of our team.\n- If they had left home earlier, they would have arrived on time.\n- Jane wishes she is at home with her family now.",
   c=CNT, a=4, pre=PJ("첫째 O. 지난 일에 대한 아쉬움을 I wish + had + 과거분사로 나타냈다.", "둘째 O. wish 뒤 현재 사실의 반대에 could를 썼다.", "셋째 O. as if + were로 현재 사실의 반대를 나타냈다.", "넷째 O. 가정법 과거완료이다.", "다섯째 X. wish 뒤 현재 사실의 반대에는 were를 쓴다(Jane wishes she were at home)."),
   k="어법상 옳은 문장은 첫째~넷째로 4개이다.", n="cnt", s=ADD(2, 130, "D", LEN))
L(2, 130, "E", p="- I wish I know his phone number right now.\n- Mina wishes she had brought an umbrella this morning.\n- Tom acts as if he had met the famous actor before.\n- If Jane were here with us, she will help.\n- We wish we can travel around the world more often.")
L(2, 130, "F", p="- I wish I have listened to your advice last year.\n- Jane wishes she is more patient with her brother.\n- Tom talks as if he knew everything about cars.\n- If we had booked the tickets earlier, we will pay less.\n- Mina wishes she can sing like a famous singer.")
