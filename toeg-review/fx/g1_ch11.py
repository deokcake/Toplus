# 1급 CH11 접속사 (101~110) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    """items = [(문장, 해설)]; 정답 보기에 ‘정답이다’, 나머지에 ‘오답이다’를 붙인다."""
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 1-102 상관접속사 수 일치: 오답 네 문장을 유형마다 새로(짝 없애기)
R102 = "both A and B는 복수 동사, either A or B·neither A nor B·not only A but also B는 B에, A as well as B는 A에 동사의 수를 맞춘다."
S102 = "오답 네 문장이 B와 똑같고 틀린 문장이 같은 내용의 옳은 문장과 짝을 이뤘다. 여러 상관접속사로 문장을 유형마다 새로 썼다."
mk(1, 102, "C", [("Neither my cousins nor my brother were at home.", "neither A nor B는 B(my brother)에 맞춰 was를 써야 해 틀렸다."), ("Both Minji and her twin sister likes spicy food.", "both A and B는 복수이므로 like를 써야 해 틀렸다."),
                 ("Either Mina or her parents are attending the ceremony.", "either A or B는 B(her parents)에 맞춰 복수 are를 써서 옳다."), ("Not only the coach but also the players was tired.", "not only A but also B는 B(the players)에 맞춰 were를 써야 해 틀렸다."),
                 ("The teacher as well as the students are excited.", "A as well as B는 A(The teacher)에 맞춰 is를 써야 해 틀렸다.")], 3, R102, S102)
mk(1, 102, "D", [("Both the bus and the train is late today.", "both A and B는 복수이므로 are를 써야 해 틀렸다."), ("Neither the teachers nor Tom is available today.", "neither A nor B는 B(Tom)에 맞춰 단수 is를 써서 옳다."),
                 ("Not only my dad but also my uncles enjoys fishing.", "not only A but also B는 B(my uncles)에 맞춰 enjoy를 써야 해 틀렸다."), ("Either you or your sister have to clean the room.", "either A or B는 B(your sister)에 맞춰 has를 써야 해 틀렸다."),
                 ("My friends as well as Jina was invited to the party.", "A as well as B는 A(My friends)에 맞춰 were를 써야 해 틀렸다.")], 2, R102, S102)
mk(1, 102, "E", [("Either the manager or the workers is responsible.", "either A or B는 B(the workers)에 맞춰 are를 써야 해 틀렸다."), ("Both my mom and my aunt works at the hospital.", "both A and B는 복수이므로 work를 써야 해 틀렸다."),
                 ("The captain as well as the sailors were brave.", "A as well as B는 A(The captain)에 맞춰 was를 써야 해 틀렸다."), ("Neither the dog nor the cats was hungry.", "neither A nor B는 B(the cats)에 맞춰 were를 써야 해 틀렸다."),
                 ("Not only Jane but also her friends are joining us.", "not only A but also B는 B(her friends)에 맞춰 복수 are를 써서 옳다.")], 5, R102, S102)
mk(1, 102, "F", [("Not only the students but also the principal were surprised.", "not only A but also B는 B(the principal)에 맞춰 was를 써야 해 틀렸다."), ("Either my brothers or my sister are going to pick me up.", "either A or B는 B(my sister)에 맞춰 is를 써야 해 틀렸다."),
                 ("Neither Sora nor her friends knows the answer.", "neither A nor B는 B(her friends)에 맞춰 know를 써야 해 틀렸다."), ("Both Yuna and her brother are good at math.", "both A and B는 복수이므로 are를 써서 옳다."),
                 ("The singer as well as the dancers look nervous.", "A as well as B는 A(The singer)에 맞춰 looks를 써야 해 틀렸다.")], 4, R102, S102)

# 1-103 간접의문문 어순: 오답 네 문장을 유형마다 새로
R103 = "간접의문문은 ‘의문사 + 주어 + 동사’ 어순으로 쓴다. be동사·조동사의 도치를 풀고, do/does/did가 있으면 빼고 본동사에 시제·수를 표시한다."
S103 = "오답 네 문장이 B와 똑같고 틀린 문장이 같은 내용의 옳은 문장과 짝을 이뤘다. 간접의문문 문장을 유형마다 새로 썼다."
BADQ = "간접의문문인데 의문문 어순(동사 + 주어)을 그대로 두어 틀렸다."
mk(1, 103, "C", [("Do you know what time is it now?", BADQ + " what time it is로 써야 한다."), ("I wonder where did she buy that hat.", BADQ + " where she bought로 써야 한다."), ("Can you tell me how old is your brother?", BADQ + " how old your brother is로 써야 한다."),
                 ("Please tell me who will lead the team.", "의문사 who가 주어라 who + 동사 어순이 바르다."), ("I don't know why is the store closed.", BADQ + " why the store is closed로 써야 한다.")], 4, R103, S103)
mk(1, 103, "D", [("Could you tell me how much does this bag cost?", BADQ + " how much this bag costs로 써야 한다."), ("Do you know where Mina left the documents?", "의문사 + 주어 + 동사 어순이 바르다."),
                 ("I wonder who is that boy.", BADQ + " who that boy is로 써야 한다."), ("Tell me when will the concert begin.", BADQ + " when the concert will begin으로 써야 한다."), ("Do you remember what did the teacher say?", BADQ + " what the teacher said로 써야 한다.")], 2, R103, S103)
mk(1, 103, "E", [("I want to know where is the bus stop.", BADQ + " where the bus stop is로 써야 한다."), ("Do you know why did Jiho cry?", BADQ + " why Jiho cried로 써야 한다."), ("Can you explain how this machine works?", "의문사 + 주어 + 동사 어순이고 본동사에 수(works)를 표시했다."),
                 ("Tell me what are you doing.", BADQ + " what you are doing으로 써야 한다."), ("I'm not sure when does the library open.", BADQ + " when the library opens로 써야 한다.")], 3, R103, S103)
mk(1, 103, "F", [("Could you tell me where can I park my car?", BADQ + " where I can park로 써야 한다."), ("I wonder how did they finish so fast.", BADQ + " how they finished로 써야 한다."), ("Do you know whose is this umbrella?", BADQ + " whose umbrella this is로 써야 한다."),
                 ("I wonder when the next train will arrive.", "의문사 + 주어 + 조동사 + 동사 어순이 바르다."), ("Please tell me what does this word mean.", BADQ + " what this word means로 써야 한다.")], 4, R103, S103)

# 1-104 Do you think + 의문사 질문: 오답을 원문항처럼 어순 오류로
R104 = "think, guess, suppose, believe처럼 생각을 묻는 동사와 의문사 질문을 합치면 의문사를 맨 앞에 두고 ‘의문사 + do you think + 주어 + 동사?’ 어순으로 쓴다."
S104 = "원문항 오답은 어순 변형인데 변형 오답은 정답과 마침표만 다르거나 첫 의문사를 뺀 것이라 형식만으로 지워졌다. 오답을 원문항처럼 어순 오류로 새로 만들었다."
def f104(t, v, wh, clause_q, clause_s, c, a):
    kinds = {f"{wh} do you {v} {clause_q}?": "간접의문문 부분에 의문문 어순(동사 + 주어)을 그대로 두었다.",
             f"Do you {v} {wh.lower()} {clause_q}?": "think류 동사가 있으면 의문사를 맨 앞으로 보내야 하고, 뒤 절 어순도 틀렸다.",
             f"Do you {v} {wh.lower()} {clause_s}?": "think류 동사가 있으면 의문사를 문장 맨 앞으로 보내야 한다.",
             f"{wh} you {v} {clause_q}?": "do가 빠지고 뒤 절 어순도 틀렸다.",
             f"{wh} do you {v} {clause_s}?": "의문사 + do you + 동사 + 주어 + 동사 어순이 바르다."}
    F(1, 104, t, p=V(1, 104, t)["passage"].replace(" / ", "\n"), c=c, a=a, r=R104, n=[kinds[x] + (" 정답이다." if i + 1 == a else " 오답이다.") for i, x in enumerate(c)], s=S104 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
def opts(v, wh, q, st, order):
    base = {"A": f"{wh} do you {v} {q}?", "B": f"Do you {v} {wh.lower()} {q}?", "C": f"{wh} do you {v} {st}?", "D": f"Do you {v} {wh.lower()} {st}?", "E": f"{wh} you {v} {q}?"}
    return [base[k] for k in order]
c = opts("guess", "When", "will the store reopen", "the store will reopen", "CABDE"); f104("B", "guess", "When", "will the store reopen", "the store will reopen", c, 1)
c = opts("think", "Why", "did Tom leave early", "Tom left early", "ACBED"); f104("C", "think", "Why", "did Tom leave early", "Tom left early", c, 2)
c = opts("think", "Where", "will Mina stay", "Mina will stay", "BDCAE"); f104("D", "think", "Where", "will Mina stay", "Mina will stay", c, 3)
c = opts("suppose", "Why", "did Jane refuse", "Jane refused", "ABECD"); f104("E", "suppose", "Why", "did Jane refuse", "Jane refused", c, 4)
c = opts("believe", "How", "can we solve this", "we can solve this", "DABEC"); f104("F", "believe", "How", "can we solve this", "we can solve this", c, 5)

# 1-105 옳은 것 모두(2차 감수에서 다시 씀): 원문항처럼 옳은 문장 넷·틀린 문장 셋, 보기는 모두 네 문장 조합
R105 = "because of·despite·in spite of 뒤에는 명사(구), because·although 뒤에는 절이 온다. so ~ that은 결과, lest ~ (should)는 ‘~하지 않도록’을 나타내고, 간접의문문은 ‘의문사 + 주어 + 동사’ 어순이다. however(no matter how) 뒤에는 형용사·부사가 바로 온다."
S105 = "보기 조합의 길이가 서로 달랐고(세 개~여섯 개) 가장 긴 조합이 늘 정답이어서 길이만 보고 고를 수 있었다. 원문항처럼 옳은 문장 넷·틀린 문장 셋으로 맞추고 보기를 모두 네 문장 조합으로 바꿨다. 수 일치 오류(Unless you calls 등)는 접속사·전치사 오류로 바꾸고, 발문을 원문항과 같게 하고 한 줄에 한 문장씩 나눴다."
def f105(t, lines, judge, ok, c):
    a = c.index(ok) + 1
    F(1, 105, t, st="R", p="\n".join(lines), c=c, a=a, r=R105, pre=["문장별 판정:"] + judge, k=f"어법상 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), s=S105 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f105("B", ["A) In spite of the snow, the road was open.", "B) Tom ran so fast that nobody caught him.", "C) Lest Mina forget the key, she put it by the door.", "D) Despite he was tired, Leo kept walking.", "E) However expensive it is, I need it.",
           "F) Tell me where is the station.", "G) Because the noise, I couldn't sleep."],
     ["A) 옳음: in spite of + 명사.", "B) 옳음: so + 부사 + that(결과).", "C) 옳음: lest + 주어 + (should) + 동사원형.", "D) 틀림: despite 뒤에는 절이 올 수 없다. Although he was tired.", "E) 옳음: however + 형용사 + 주어 + 동사.",
      "F) 틀림: 간접의문문 어순은 where the station is.", "G) 틀림: 명사 앞에는 because of를 쓴다."],
     "A, B, C, E", ["A, B, C, E", "B, C, D, E", "A, C, F, G", "A, B, E, G", "B, D, E, F"])
f105("C", ["A) Because of the heavy traffic, we arrived late.", "B) Mina worked such hard that she finished early.", "C) Lest Tom forget, I sent him a reminder.", "D) Although the rain, they kept playing.", "E) However tired she was, Jane kept working.",
           "F) I wonder where did he go.", "G) No matter what happens, stay calm."],
     ["A) 옳음: because of + 명사.", "B) 틀림: 부사 hard 앞에는 such가 아니라 so를 쓴다.", "C) 옳음: lest + 주어 + (should) + 동사원형.", "D) 틀림: although 뒤에는 절이 와야 한다. Despite the rain.", "E) 옳음: however + 형용사 + 주어 + 동사.",
      "F) 틀림: 간접의문문 어순은 where he went.", "G) 옳음: no matter what + 동사."],
     "A, C, E, G", ["A, B, C, E", "A, C, E, G", "B, C, D, F", "A, C, F, G", "C, D, E, G"])
f105("D", ["A) Despite it was raining, we went out.", "B) Tom was so tired that he fell asleep.", "C) Lest the child should fall, hold his hand.", "D) Unless you hurry, you will be late.", "E) Whatever you decide, I will support you.",
           "F) Do you know when will Mina come?", "G) However it is difficult, do not give up."],
     ["A) 틀림: despite 뒤에는 절이 올 수 없다. Although it was raining.", "B) 옳음: so + 형용사 + that(결과).", "C) 옳음: lest + 주어 + should + 동사원형.", "D) 옳음: unless + 현재시제.", "E) 옳음: whatever가 양보절을 이끈다.",
      "F) 틀림: 간접의문문 어순은 when Mina will come.", "G) 틀림: however 바로 뒤에 형용사가 와야 한다. However difficult it is."],
     "B, C, D, E", ["A, B, C, D", "B, C, E, G", "B, C, D, E", "A, D, E, F", "C, D, F, G"])
f105("E", ["A) Because the rain, the match was canceled.", "B) Mina spoke so quietly that I could hardly hear her.", "C) Lest we be late, we left early.", "D) Unless Tom studies, he will not pass.", "E) No matter how Jane is busy, she exercises.",
           "F) I wonder why did he leave.", "G) Whatever happens, call me."],
     ["A) 틀림: 명사 앞에는 because of를 쓴다.", "B) 옳음: so + 부사 + that(결과).", "C) 옳음: lest + 주어 + (should) + 동사원형.", "D) 옳음: unless + 현재시제.", "E) 틀림: no matter how 바로 뒤에 형용사가 와야 한다. No matter how busy Jane is.",
      "F) 틀림: 간접의문문 어순은 why he left.", "G) 옳음: whatever가 양보절을 이끈다."],
     "B, C, D, G", ["A, B, C, D", "B, D, E, F", "A, C, E, G", "B, C, D, G", "C, D, F, G"])
f105("F", ["A) Although the delay, we waited.", "B) Jane was so nervous that she forgot her lines.", "C) Lest Tom should miss the bus, he left early.", "D) Unless it will rain, we will play outside.", "E) No matter who calls, do not answer.",
           "F) I am not sure when the store closes.", "G) However he drove carefully, the road was dangerous."],
     ["A) 틀림: although 뒤에는 절이 와야 한다. Despite the delay.", "B) 옳음: so + 형용사 + that(결과).", "C) 옳음: lest + 주어 + should + 동사원형.", "D) 틀림: 조건의 unless절에서는 미래의 일도 현재시제로 쓴다. Unless it rains.", "E) 옳음: no matter who가 양보절을 이끈다.",
      "F) 옳음: 간접의문문 어순(when + 주어 + 동사).", "G) 틀림: however 바로 뒤에 부사가 와야 한다. However carefully he drove."],
     "B, C, E, F", ["A, B, C, E", "B, D, F, G", "A, C, D, G", "C, E, F, G", "B, C, E, F"])

# 1-107 so that 배열: 발문 조건 삭제, 오답을 제시어 어순만 바꾼 배열로
R107 = "so that + 주어 + 조동사 + 동사원형은 ‘~하기 위해서, ~하도록’이라는 목적을 나타낸다. so that은 붙여 쓰고 주절 뒤에 둔다."
SPLIT = "so와 that이 떨어져 so that 구문이 깨졌다. 오답이다."
ORD = "주절이나 that절의 어순이 뒤섞였다. 오답이다."
FRONT = "so that 절 안의 주어와 조동사 순서가 틀렸다. 오답이다."
OK107 = "주절 + so that + 주어 + 조동사 + 동사원형 어순이 바르다. 정답이다."
S107 = "발문에 ‘행동과 그 목적을 연결, 주어로 시작, 부사는 동사 뒤’ 조건이 붙어 구조를 알려 주었고 오답이 제시어에 없는 낱말(such, because, will)을 쓰거나 주어를 빼서 조건만으로 지워졌다. 발문을 원문항과 같게 하고 오답을 제시어의 어순만 바꾼 배열로 새로 만들었다."
def f107(t, c, a, kinds):
    F(1, 107, t, st="R", c=c, a=a, r=R107, n=[(OK107 if i + 1 == a else kinds[i]) for i in range(5)], s=S107 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f107("B", ["We whispered that so the baby would not wake up.", "We so whispered that the baby would not wake up.", "We whispered so that would the baby not wake up.", "We whispered so that the baby would not wake up.", "So that we whispered the baby would not wake up."], 4, [SPLIT, SPLIT, FRONT, None, ORD])
f107("C", ["She took a taxi so that she would not miss the train.", "She took so that a taxi she would not miss the train.", "She took a taxi that so she would not miss the train.", "She took a taxi so that would she not miss the train.", "She so took a taxi that she would not miss the train."], 1, [None, ORD, SPLIT, FRONT, SPLIT])
f107("D", ["Tom saved money that so he could buy a laptop.", "Tom so saved money that he could buy a laptop.", "Tom saved money so that he could buy a laptop.", "Tom saved money so that could he buy a laptop.", "Money Tom saved so that he could buy a laptop."], 3, [SPLIT, SPLIT, None, FRONT, ORD])
f107("E", ["Mina wrote down it so that she would not forget.", "Mina wrote it down that so she would not forget.", "Mina so wrote it down that she would not forget.", "Mina wrote it down so that would she not forget.", "Mina wrote it down so that she would not forget."], 5,
     ["대명사 it은 wrote와 down 사이에 두어야 한다. 오답이다.", SPLIT, SPLIT, FRONT, None])
f107("F", ["They so left early that they could avoid traffic.", "They left early so that they could avoid traffic.", "They left early that so they could avoid traffic.", "Early they left so that could they avoid traffic.", "They left so that early they could avoid traffic."], 2, [SPLIT, None, SPLIT, FRONT, ORD])

# 1-108 간접의문문 밑줄: 발문을 원문항과 같게, 밑줄 복원, 오답을 유형마다 새로
R108 = "간접의문절은 의문사(또는 if/whether) + 주어 + 동사 어순으로 쓴다. 의문사(구)가 주어이면 바로 동사가 온다."
def f108(t, items, a, s):
    F(1, 108, t, st="R", c=[x for x, _ in items], a=a, r=R108, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
OKQ = "의문사 + 주어 + 동사 어순이 바르다."
f108("B", [("I am not sure <u>why Mina left so early</u>.", OKQ), ("I wonder <u>what Tom wants</u>.", OKQ), ("Do you know <u>when the results will be announced</u>?", OKQ), ("Can you tell me <u>where the nearest pharmacy is</u>?", OKQ),
           ("Please explain <u>how can I reset</u> the device.", "간접의문절에 의문문 어순(조동사 + 주어)을 그대로 두었다. how I can reset으로 써야 한다.")], 5,
    "발문을 원문항 ‘밑줄 친 부분의 어법상 형태가 어색한 것’으로 되돌리고, 원문항처럼 간접의문절에 밑줄을 넣었다.")
S108 = "오답 네 문장이 B와 똑같고 틀린 문장이 같은 내용의 옳은 문장과 짝을 이뤘으며 밑줄도 사라졌다. 발문을 원문항과 같게 하고 밑줄을 넣은 새 문장으로 바꿨다."
f108("C", [("She asked me <u>if I had ever been</u> to Japan.", "if + 주어 + 동사 어순이 바르다."), ("I don't know <u>who broke</u> the window.", "의문사 who가 주어라 바로 동사가 와서 바르다."), ("Tell me <u>how far the museum is</u>.", OKQ),
           ("I can't remember <u>where I put</u> my glasses.", OKQ), ("I am not sure <u>why did Mina leave</u> so early.", "간접의문절에 의문문 어순(did + 주어)을 그대로 두었다. why Mina left로 써야 한다.")], 5, S108)
f108("D", [("Could you tell me <u>where is the ticket office</u>?", "간접의문절에 의문문 어순(be동사 + 주어)을 그대로 두었다. where the ticket office is로 써야 한다."), ("We asked <u>whether the store was open</u>.", "whether + 주어 + 동사 어순이 바르다."),
           ("I wonder <u>how many students came</u> to the event.", "의문사구가 주어라 바로 동사가 와서 바르다."), ("Do you know <u>what she bought</u> for Dad?", OKQ), ("Nobody knows <u>when the singer will arrive</u>.", OKQ)], 1, S108)
f108("E", [("I want to know <u>what time the movie starts</u>.", OKQ), ("Please tell me <u>which bus goes</u> to the airport.", "의문사구가 주어라 바로 동사가 와서 바르다."), ("He asked me <u>if I could help</u> him.", "if + 주어 + 동사 어순이 바르다."),
           ("Do you remember <u>where we parked</u> the car?", OKQ), ("I wonder <u>what does Tom want</u>.", "간접의문절에 의문문 어순(does + 주어)을 그대로 두었다. what Tom wants로 써야 한다.")], 5, S108)
f108("F", [("I have no idea <u>how she got</u> the tickets.", OKQ), ("Tell me <u>who you met</u> yesterday.", OKQ), ("Do you know <u>when will the results be announced</u>?", "간접의문절에 의문문 어순(will + 주어)을 그대로 두었다. when the results will be announced로 써야 한다."),
           ("Let me know <u>whether you can come</u>.", "whether + 주어 + 동사 어순이 바르다."), ("I wonder <u>how long the trip will take</u>.", OKQ)], 3, S108)

# 1-109 unless: 원문항처럼 unless 용법 오류(부정어 중복 등)와 문맥 판단
R109 = "unless는 ‘~하지 않으면(= if ~ not)’이라는 뜻이라 뒤에 not을 겹쳐 쓰지 않는다. 조건절에는 미래 일이라도 현재형을 쓰고, 문맥상 뜻이 맞는지도 확인한다."
S109 = "원문항은 unless의 뜻·용법 오류와 문맥 판단을 묻는데 변형의 오류는 수 일치·동사 형태였고 발문에서 ‘문맥’ 기준도 빠졌다. 발문을 원문항과 같게 하고 unless 뒤 부정어 중복·뜻이 반대가 되는 문맥 오류로 다시 썼다. 옳은 문장 셋·틀린 문장 둘로 맞췄다."
def f109(t, lines, judge, ok, c, a, s=S109):
    F(1, 109, t, st="R", p="\n".join(lines), c=c, a=a, r=R109, pre=["문장별 판정:"] + judge, k=f"문맥과 어법이 모두 올바른 문장은 {ok}이다.", n=setnotes(c, ok, "올바른 문장"), s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f109("B", ["(A) Unless it doesn't rain, we will play outside.", "(B) You cannot enter unless you have a ticket.", "(C) Unless Mina calls me, I will leave at six.", "(D) I will wear a coat unless it is warm tomorrow.", "(E) Unless you study hard, you will pass the test easily."],
     ["(A) 틀림: unless에 이미 not의 뜻이 있어 doesn't를 겹쳐 쓸 수 없다. Unless it rains.", "(B) 옳음: 표가 없으면 들어갈 수 없다.", "(C) 옳음: Mina가 전화하지 않으면 6시에 떠난다.", "(D) 옳음: 따뜻하지 않으면 코트를 입겠다.",
      "(E) 틀림: ‘공부하지 않으면 쉽게 통과한다’는 문맥이 맞지 않는다. If you study hard로 써야 한다."],
     "(B), (C), (D)", ["(A), (B), (C)", "(B), (C), (D)", "(B), (D), (E)", "(A), (C), (E)", "(C), (D), (E)"], 2)
f109("C", ["(A) Unless Tom studies, he may fail the test.", "(B) I will call you unless I won't get home too late.", "(C) Unless the store is closed, we can buy the book there.", "(D) Unless you practice regularly, your skills will improve quickly.", "(E) We will have the picnic unless it rains."],
     ["(A) 옳음: 공부하지 않으면 떨어질 수 있다.", "(B) 틀림: unless 뒤에 won't를 겹쳐 썼고, 조건절에는 현재형을 쓴다. unless I get home too late.", "(C) 옳음: 가게가 닫지 않았으면 거기서 살 수 있다.",
      "(D) 틀림: ‘연습하지 않으면 실력이 빨리 는다’는 문맥이 맞지 않는다.", "(E) 옳음: 비가 오지 않으면 소풍을 간다."],
     "(A), (C), (E)", ["(A), (B), (C)", "(A), (C), (E)", "(B), (C), (D)", "(A), (D), (E)", "(C), (D), (E)"], 2,
     "다섯 문장이 모두 옳아 틀린 문장이 없었다. " + S109)
f109("D", ["(A) Unless the bus is late, we will arrive before noon.", "(B) You cannot use this room unless a teacher will be present.", "(C) Unless Jane feels better, she will stay home.", "(D) Unless he wears a helmet, he will be safe.", "(E) I will finish the report tonight unless the computer stops working."],
     ["(A) 옳음: 버스가 늦지 않으면 정오 전에 도착한다.", "(B) 틀림: 조건의 unless절에서는 미래의 일도 현재시제로 쓴다. unless a teacher is present.", "(C) 옳음: 몸이 나아지지 않으면 집에 있겠다.",
      "(D) 틀림: ‘헬멧을 쓰지 않으면 안전하다’는 문맥이 맞지 않는다.", "(E) 옳음: 컴퓨터가 멈추지 않으면 보고서를 끝낸다."],
     "(A), (C), (E)", ["(A), (B), (D)", "(B), (C), (E)", "(A), (C), (E)", "(C), (D), (E)", "(A), (B), (C)"], 3)
f109("E", ["(A) Unless you don't save your file, you may lose your work.", "(B) Unless the road is blocked, we will take this route.", "(C) You cannot borrow the car unless Dad agrees.", "(D) Unless Mina is busy, she will join us.", "(E) We will eat outside unless it is warm and sunny."],
     ["(A) 틀림: unless 뒤에 don't를 겹쳐 썼다. Unless you save your file.", "(B) 옳음: 길이 막히지 않으면 이 길로 간다.", "(C) 옳음: 아빠가 허락하지 않으면 차를 빌릴 수 없다.", "(D) 옳음: 바쁘지 않으면 함께한다.",
      "(E) 틀림: ‘따뜻하고 맑지 않으면 밖에서 먹는다’는 문맥이 맞지 않는다."],
     "(B), (C), (D)", ["(A), (B), (C)", "(C), (D), (E)", "(A), (D), (E)", "(B), (C), (D)", "(B), (D), (E)"], 4)
f109("F", ["(A) Unless the train is delayed, we will reach Busan by noon.", "(B) You cannot pass the course unless you complete the project.", "(C) Unless Leo won't call first, I will not change the plan.", "(D) Unless she forgets the key, she can open the door.", "(E) We will go swimming unless the pool is open."],
     ["(A) 옳음: 기차가 늦지 않으면 정오까지 부산에 도착한다.", "(B) 옳음: 과제를 끝내지 않으면 통과할 수 없다.", "(C) 틀림: unless 뒤에 won't를 겹쳐 썼고, 조건절에는 현재형을 쓴다. Unless Leo calls first.",
      "(D) 옳음: 열쇠를 잊지 않으면 문을 열 수 있다.", "(E) 틀림: ‘수영장이 열지 않으면 수영하러 간다’는 문맥이 맞지 않는다. unless the pool is closed."],
     "(A), (B), (D)", ["(A), (C), (E)", "(B), (C), (D)", "(A), (D), (E)", "(C), (D), (E)", "(A), (B), (D)"], 5)

# 1-110 so/such/despite 빈칸: 원문항처럼 (C)에 so/such 구별, 괄호 삭제, 밑줄 복원
R110 = "such + (a/an) + 형용사 + 명사 + that, so + 형용사/부사 + that으로 결과를 나타낸다. despite 뒤에는 명사(구), although·even though 뒤에는 절이 온다."
UA, UB, UC = "(<u>      A      </u>)", "(<u>      B      </u>)", "(<u>      C      </u>)"
NEED110 = ["(A)는 뒤에 형용사 + 명사가 오면 such, 형용사만 오면 so를 쓴다.", "(B)는 뒤에 명사구만 오므로 전치사 Despite를 쓴다.", "(C)는 뒤에 형용사/부사 + that절이 오면 so, (a/an) + 형용사 + 명사가 오면 such를 쓴다."]
S110 = "원문항 (C)는 so/such 구별인데 변형 (C)는 접속사(because/so) 자리로 바뀌었고, 발문 괄호가 (B)·(C)의 역할을 알려 주었다. 원문항처럼 (C)에 so/such 구별이 들어가는 문장으로 바꾸고, 발문 괄호를 지우고 밑줄 빈칸을 넣었다."
def f110(t, p, c, a, need=None):
    F(1, 110, t, st="R", p=p, c=c, a=a, r=R110, n=tnotes(c, a, need or NEED110, labs=["(A)", "(B)", "(C)"], plain=True), s=S110 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f110("B", f"It was {UA} a difficult exam that many students struggled. {UB} their preparation, some failed. The questions were {UC} tricky that even the teacher was surprised.",
     ["(A) so - (B) Although - (C) such", "(A) such - (B) Despite - (C) so", "(A) such - (B) Despite - (C) such", "(A) so - (B) Even though - (C) so", "(A) such - (B) Though - (C) so"], 2)
f110("C", f"The lecture was {UA} interesting that everyone stayed. {UB} the long duration, nobody complained. The speaker was {UC} a good storyteller that time flew by.",
     ["(A) such - (B) Despite - (C) such", "(A) so - (B) Although - (C) so", "(A) so - (B) Despite - (C) such", "(A) so - (B) Despite - (C) so", "(A) such - (B) Even though - (C) such"], 3)
f110("D", f"Mina is {UA} talented a musician that people expect her to win. {UB} her young age, she performs calmly. Her voice is {UC} beautiful that audiences are moved to tears.",
     ["(A) so - (B) Despite - (C) so", "(A) such - (B) Despite - (C) such", "(A) so - (B) Although - (C) such", "(A) such - (B) Though - (C) so", "(A) so - (B) Even though - (C) so"], 1,
     need=["(A)는 ‘so + 형용사 + a + 명사’ 어순이므로 so를 쓴다(such는 such a + 형용사 + 명사 어순).", NEED110[1], NEED110[2]])
f110("E", f"The team played {UA} well that the crowd cheered. {UB} the loss of one player, they won. It was {UC} an exciting game that nobody left early.",
     ["(A) such - (B) Despite - (C) so", "(A) so - (B) Although - (C) such", "(A) so - (B) Despite - (C) so", "(A) such - (B) Though - (C) such", "(A) so - (B) Despite - (C) such"], 5)
f110("F", f"It was {UA} an inspiring story that Mina cried. {UB} the sad ending, she loved it. The characters were {UC} real that she felt she knew them.",
     ["(A) so - (B) Despite - (C) so", "(A) such - (B) Although - (C) so", "(A) such - (B) Despite - (C) such", "(A) such - (B) Despite - (C) so", "(A) so - (B) Even though - (C) such"], 4)
