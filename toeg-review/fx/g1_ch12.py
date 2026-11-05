# 1급 CH12 일치와 화법 (111~120) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 1-111 시제 일치와 예외: 긴 조건 설명 삭제, 일반적 진리·역사적 사실 문장 포함
R111 = "주절이 과거이면 종속절도 과거·과거완료·would·could로 시제를 맞춘다. 단, 일반적 진리·속담·습관은 현재형, 역사적 사실은 과거형을 그대로 쓴다."
S111 = "발문이 세 줄에 걸친 시제 후퇴 조건으로 판단 기준을 알려 주었고, 원문항에 있던 시제 일치의 예외(일반적 진리·역사적 사실) 문장이 빠졌다. 발문을 원문항과 같게 하고, 예외 문장을 옳은 보기로 넣어 유형마다 새로 썼다."
TRUTH = "일반적 진리는 주절이 과거여도 현재형을 쓴다."
HIST = "역사적 사실은 주절과 관계없이 과거형을 쓴다."
BACK = "주절(과거)에 맞춰 시제를 바르게 맞췄다."
mk(1, 111, "B", [("Mina said that she is tired the previous night.", "the previous night의 일인데 현재형 is를 써서 틀렸다. was로 써야 한다."), ("The teacher said that the moon moves around the Earth.", TRUTH),
                 ("We learned that World War II ended in 1945.", HIST), ("Jane thought that the train had already gone.", BACK), ("Tom said that he would call me the next day.", BACK)], 1, R111, S111, st="R")
mk(1, 111, "C", [("My father told me that honesty is the best policy.", "속담은 주절이 과거여도 현재형을 쓴다."), ("Minho said that he had lost his wallet.", BACK), ("She knew that Columbus reached America in 1492.", HIST),
                 ("I believed that Mina can finish the task by herself.", "주절이 과거(believed)인데 can을 써서 틀렸다. could로 써야 한다."), ("They said that they were going to move.", BACK)], 4, R111, S111, st="R")
mk(1, 111, "D", [("Our teacher told us that light travels faster than sound.", TRUTH), ("I heard that the Korean War broke out in 1950.", HIST),
                 ("Sujin said that she will visit her aunt the next week.", "주절이 과거(said)인데 will을 써서 틀렸다. would로 써야 한다."), ("Jiwoo said that she had never seen snow.", BACK), ("We thought that the bus would come soon.", BACK)], 3, R111, S111, st="R")
mk(1, 111, "E", [("The scientist explained that water freezes at 0°C.", TRUTH), ("We learned that King Sejong created Hangeul.", HIST), ("I thought that the store is open at that time.", "at that time의 일인데 현재형 is를 써서 틀렸다. was로 써야 한다."),
                 ("Mina told me that she could speak three languages.", BACK), ("He said that he had met the singer before.", BACK)], 3, R111, S111, st="R")
mk(1, 111, "F", [("Grandma always said that time is money.", "속담은 주절이 과거여도 현재형을 쓴다."), ("We knew that Leo has moved to Busan.", "주절이 과거(knew)인데 현재완료를 써서 틀렸다. had moved로 써야 한다."),
                 ("The guide told us that the Titanic sank in 1912.", HIST), ("Tom said that he was going to the library.", BACK), ("Jina said that she would help me the next day.", BACK)], 2, R111, S111, st="R")

# 1-112 부분 표현 수 일치: 수 일치가 맞던 was - were를 틀린 조합으로, 발문 조건 삭제
R112 = "most·half·some·분수(two-thirds 등) of + 명사가 주어이면 of 뒤 명사에 동사의 수를 맞춘다. 셀 수 없는 명사·단수명사이면 단수, 복수명사이면 복수 동사를 쓴다."
S112 = "보기 ‘was - were’도 수 일치가 맞는 조합이라 발문의 ‘현재의 상태를 나타내도록’ 조건이 없으면 복수 정답이 되었다. 이 보기를 수 일치가 틀린 ‘was - was’로 바꾸고 발문 조건을 지웠다. 원문항처럼 • 두 줄로 나눴다."
def f112(t, c, a, n1, v1, n2, v2):
    a1, b1 = V(1, 112, t)["passage"].split(" / ")
    need = [f"첫째 빈칸은 of 뒤의 {n1}에 수를 맞춰 {v1}를 쓴다.", f"둘째 빈칸은 of 뒤의 {n2}에 수를 맞춰 {v2}를 쓴다."]
    F(1, 112, t, st="R", p=f"• {a1}\n• {b1}", c=c, a=a, r=R112, n=tnotes(c, a, need, plain=True), s=S112)
f112("B", ["is - is", "was - was", "are - are", "is - are", "are - is"], 4, "equipment(셀 수 없는 명사)", "is", "employees(복수)", "are")
f112("C", ["are - are", "is - is", "is - are", "are - is", "was - was"], 4, "students(복수)", "are", "money(셀 수 없는 명사)", "is")
f112("D", ["is - are", "was - was", "are - are", "are - is", "is - is"], 1, "land(셀 수 없는 명사)", "is", "houses(복수)", "are")
f112("E", ["is - is", "are - is", "is - are", "are - are", "was - was"], 2, "books(복수)", "are", "information(셀 수 없는 명사)", "is")
f112("F", ["is - are", "was - was", "are - is", "are - are", "is - is"], 1, "furniture(셀 수 없는 명사)", "is", "participants(복수)", "are")

# 1-113 의문문의 간접화법: 발문 조건 삭제, 물음표 오답을 원문항 유형(asked to me …)으로
R113 = "의문문을 간접화법으로 바꿀 때는 asked (+ 사람) + 의문사 + 주어 + 동사 어순으로 쓰고, 전달동사가 과거이면 시제를 한 단계 뒤로 옮긴다(과거 → 과거완료, will → would, now → then)."
def g113(x, good):
    if x == good: return "asked + 의문사 + 주어 + 동사 어순으로 시제를 한 단계 뒤로 옮겼다. 정답이다."
    if " said " in f" {x} " and ("said me" in x or "said us" in x or "said him" in x): return "said 뒤에는 사람을 바로 쓰지 않고, 질문을 전할 때는 asked를 쓴다. 오답이다."
    if " said why" in x: return "질문을 전할 때는 said가 아니라 asked를 쓴다. 오답이다."
    if "asked to" in x: return "asked 뒤에는 to 없이 사람을 쓰고, 간접의문문은 주어 + 동사 어순이어야 한다. 오답이다."
    if " did " in x: return "간접의문문에 did를 남겨 의문문 어순이 되었다. 오답이다."
    if "would arrived" in x: return "would 뒤에는 동사원형을 써야 한다. 오답이다."
    if " where you " in x: return "전달하는 사람의 처지에 맞게 you를 he로 바꾸지 않았다. 오답이다."
    if "cancels" in x or "solves" in x: return "지난 일을 물은 질문인데 현재형을 썼다. 오답이다."
    if " will " in x and "would" in x: return "간접의문문에 will을 남겨 의문문 어순이 되었다. 오답이다."
    return "전달 시점(asked)에 맞춰 시제를 한 단계 뒤로 옮기지 않았다. 오답이다."
S113 = "발문이 ‘시제를 한 단계 후퇴, this → that, now → then’ 같은 전환 규칙을 알려 주었고, 정답 끝에 물음표만 붙인 오답은 형식만으로 지워졌다. 발문을 원문항과 같게 하고, 물음표 오답을 원문항처럼 ‘asked to + 사람 + 의문문 어순’ 오류로 바꿨다. 시제만 옮기지 않은 오답(asked why Mina canceled 등)은 실제 영어에서 쓰이기도 해 분명히 틀린 형태로 바꿨다."
def f113(t, c, a):
    F(1, 113, t, st="R", c=c, a=a, r=R113, n=[g113(x, c[a - 1]) for x in c], s=S113 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f113("B", ["Tom said me why Mina had canceled the reservation.", "Tom asked me why Mina cancels the reservation.", "Tom asked me why Mina had canceled the reservation.", "Tom asked to me why had Mina canceled the reservation.", "Tom asked me why did Mina had canceled the reservation."], 3)
f113("C", ["Jane asked him where you had put the keys.", "Jane asked him where he had put the keys.", "Jane said him where he had put the keys.", "Jane asked to him where had he put the keys.", "Jane asked him where did he had put the keys."], 2)
f113("D", ["Mina asked us when the train would arrived.", "Mina asked us when will the train would arrive.", "Mina asked us when the train would arrive.", "Mina asked to us when would the train arrive.", "Mina said us when the train would arrive."], 3)
f113("E", ["Leo asked me how Tom solves the problem.", "Leo said me how Tom had solved the problem.", "Leo asked to me how had Tom solved the problem.", "Leo asked me how Tom had solved the problem.", "Leo asked me how did Tom had solved the problem."], 4)
f113("F", ["Jane asked why they were leaving then.", "Jane said why they were leaving then.", "Jane asked to them why were they leaving then.", "Jane asked why they are leaving then.", "Jane asked why did they were leaving then."], 1)

# 1-114 수 일치: 발문 조건 삭제, 오답을 유형마다 새로
R114 = "each·every·one of + 명사, 학과명(-ics), news·information·money 같은 셀 수 없는 명사는 단수 동사를 쓴다. neither/either A or B·not only A but also B는 B에, A as well as B는 A에 수를 맞춘다. the number of는 단수, a number of는 복수 동사를 쓴다."
S114 = "발문에 ‘격식 있는 문어 영어 기준’ 조건이 붙었고, 틀린 문장이 정답과 짝을 이뤄 대비 단서가 되었다. 발문을 원문항과 같게 하고 오답 네 문장을 유형마다 새로 썼다."
mk(1, 114, "B", [("Both of the answers is correct.", "both of + 복수명사는 복수 동사 are를 써야 해 틀렸다."), ("Every one of the machines needs regular maintenance.", "every one of + 복수명사에 단수 동사 needs를 써서 옳다."),
                 ("Each of the applicants have submitted their portfolio.", "each of + 복수명사는 단수 동사 has를 써야 해 틀렸다."), ("One of the students have forgotten their ID.", "one of + 복수명사는 단수 동사 has를 써야 해 틀렸다."),
                 ("Mathematics are difficult for many students.", "학과명 Mathematics는 단수 취급하므로 is를 써야 해 틀렸다.")], 2, R114, "⑤가 정답 ②에서 동사만 바꾼 문장이라 대비 단서가 되었다. ⑤를 다른 오류 문장으로 바꾸고 발문 조건을 지워 원문항 발문으로 되돌렸다.", st="R")
mk(1, 114, "C", [("The news about the storms were frightening.", "news는 단수 취급하므로 was를 써야 해 틀렸다."), ("Every boy and girl in the class have a locker.", "every A and B는 단수 취급하므로 has를 써야 해 틀렸다."), ("Physics are my brother's favorite subject.", "학과명 Physics는 단수 취급하므로 is를 써야 해 틀렸다."),
                 ("Neither the coach nor the players was ready.", "neither A nor B는 B(the players)에 맞춰 were를 써야 해 틀렸다."), ("Each of the applicants has submitted his or her portfolio.", "each of + 복수명사에 단수 동사 has를 써서 옳다.")], 5, R114, S114, st="R")
mk(1, 114, "D", [("Each student in the classes have a laptop.", "each + 단수명사는 단수 동사 has를 써야 해 틀렸다."), ("The information you gave me were very useful.", "information은 셀 수 없는 명사라 was를 써야 해 틀렸다."), ("Either my parents or my sister are coming.", "either A or B는 B(my sister)에 맞춰 is를 써야 해 틀렸다."),
                 ("Neither of the answers is completely correct.", "neither of + 복수명사에 단수 동사 is를 써서 옳다."), ("A number of students is absent today.", "a number of + 복수명사는 복수 동사 are를 써야 해 틀렸다.")], 4, R114, S114, st="R")
mk(1, 114, "E", [("Every teacher and parent were invited.", "every A and B는 단수 취급하므로 was를 써야 해 틀렸다."), ("The money in the box are missing.", "money는 셀 수 없는 명사라 is를 써야 해 틀렸다."), ("One of the students has forgotten his or her ID.", "one of + 복수명사에 단수 동사 has를 써서 옳다."),
                 ("Statistics are a difficult subject.", "학과명 Statistics는 단수 취급하므로 is를 써야 해 틀렸다."), ("Not only I but also my brother are tall.", "not only A but also B는 B(my brother)에 맞춰 is를 써야 해 틀렸다.")], 3, R114, S114, st="R")
mk(1, 114, "F", [("Each of the books has its own index.", "each of + 복수명사에 단수 동사 has를 써서 옳다."), ("Neither my friends nor my sister like fish.", "neither A nor B는 B(my sister)에 맞춰 likes를 써야 해 틀렸다."), ("The furniture in these rooms look old.", "furniture는 셀 수 없는 명사라 looks를 써야 해 틀렸다."),
                 ("Each of the rooms have a window.", "each of + 복수명사는 단수 동사 has를 써야 해 틀렸다."), ("The number of cars are increasing.", "the number of는 ‘~의 수’라 단수 동사 is를 써야 해 틀렸다.")], 1, R114, S114, st="R")

# 1-115 옳은 것 모두: 발문 조건 삭제, C·D는 정답 조합을 원문항과 다르게
R115 = "the + 형용사(the rich, the elderly)는 ‘~한 사람들’로 복수, police·cattle은 항상 복수, each/neither of는 단수 동사를 쓴다. say는 사람 목적어를 바로 쓰지 않고(said to me / told me), 간접의문문은 주어 + 동사 어순이다."
for t in "BE":
    F(1, 115, t, st="R", p="BR", okx=True, s="발문의 ‘격식 문어 기준, 영국 영어의 집합명사 복수 일치 허용’ 조건을 지워 원문항 발문으로 되돌렸다. 항상 복수인 police·cattle만 써서 조건 없이도 판단이 같다. 한 줄에 한 문장씩 나눴다.")
def f115(t, lines, judge, ok, c, a, s):
    F(1, 115, t, st="R", p="\n".join(lines), c=c, a=a, r=R115, pre=["문장별 판정:"] + judge, k=f"어법상 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f115("C", ["A) The rich are not always happy.", "B) Mina said that she has finished before noon.", "C) Tom told me that he was tired.", "D) Each of the machines needs repair.", "E) She asked where was the station.", "F) The police are investigating the case."],
     ["A) 옳음: the rich는 ‘부자들’로 복수 동사 are를 쓴다.", "B) 틀림: 주절이 과거이므로 had finished로 써야 한다.", "C) 옳음: told + 사람 + that절이다.", "D) 옳음: each of + 복수명사에 단수 동사 needs를 썼다.",
      "E) 틀림: 간접의문문은 where the station was 어순이다.", "F) 옳음: police는 항상 복수이다."],
     "A, C, D, F", ["A, B, C, E, F", "B, C, E", "A, C, D, F", "A, D, F", "A, B, D"], 3,
     "정답 조합이 원문항 정답(A, B, D, F)과 같았다. B를 틀린 문장, C를 옳은 문장으로 바꿔 정답을 A, C, D, F로 만들고, 발문 조건을 지웠다.")
f115("D", ["A) The elderly needs better access to healthcare.", "B) Tom said that he would arrive later.", "C) Jane asked me where did I live.", "D) Neither of the plans is perfect.", "E) Mina told me that she was busy.", "F) The police are discussing the issue."],
     ["A) 틀림: the elderly는 ‘노인들’로 복수 동사 need를 써야 한다.", "B) 옳음: 주절이 과거이므로 would를 썼다.", "C) 틀림: 간접의문문은 where I lived 어순이다.", "D) 옳음: neither of + 복수명사에 단수 동사 is를 썼다.",
      "E) 옳음: told + 사람 + that절이다.", "F) 옳음: police는 항상 복수이다."],
     "B, D, E, F", ["A, B, D, F", "A, B, D", "A, D, F", "B, D, E, F", "B, C, E"], 4,
     "정답 조합이 원문항과 같았고 ‘The staff are’는 영국 영어 허용 조건에 기대야 옳았다. A를 틀린 문장, E를 옳은 문장으로 바꾸고 staff 문장을 항상 복수인 police로 바꿨다. 발문 조건을 지웠다.")

# 1-118 요구·제안의 that절 동사원형: 발문 설명 삭제, 오답을 유형마다 새로
R118 = "요구·제안·명령·필요를 나타내는 동사(demand, suggest, request, recommend, order, propose, insist)나 형용사(necessary, important, essential) 뒤 that절에는 주어와 관계없이 (should +) 동사원형을 쓴다."
S118 = "발문이 원형가정법 규칙과 동사들의 뜻을 설명해 판단 근거를 알려 주었고, C~F는 오답 네 문장이 B와 같았다. 발문을 원문항과 같게 하고, 원문항처럼 It is necessary that 문장을 넣어 유형마다 새로 썼다."
OKB = "that절에 동사원형을 바르게 썼다."
mk(1, 118, "B", [("It is essential that every student wear a helmet.", OKB), ("The committee requested that the proposal be revised.", OKB), ("The coach demanded that the players not be late.", "that절 부정은 not + 동사원형으로 바르게 썼다."),
                 ("The doctor advised that the patient drinks more water.", "that절의 동사를 원형 drink로 써야 해 틀렸다."), ("The teacher suggested that Tom study harder.", OKB)], 4, R118,
   "발문이 원형가정법 규칙을 설명해 판단 근거를 알려 주었다. 발문을 원문항과 같게 했다. 발문이 없으면 ‘insisted that Mina apologized’는 ‘사과했다고 주장했다’로 옳을 수 있어, 틀린 문장을 뜻이 분명한 advise 문장으로 바꿨다.", st="R")
mk(1, 118, "C", [("The principal ordered that the gate is locked at night.", "that절의 동사를 원형 be locked로 써야 해 틀렸다."), ("It is important that he be on time.", OKB), ("My mom insisted that I wear a coat.", OKB),
                 ("They proposed that the meeting start at nine.", OKB), ("I recommend that she not eat too much sugar.", "that절 부정은 not + 동사원형으로 바르게 썼다.")], 1, R118, S118, st="R")
mk(1, 118, "D", [("It is necessary that the report be finished today.", OKB), ("The judge ordered that the man pay a fine.", OKB), ("The manager requested that every worker wears a name tag.", "that절의 동사를 원형 wear로 써야 해 틀렸다."),
                 ("We asked that the music be turned down.", OKB), ("She recommended that I not skip breakfast.", "that절 부정은 not + 동사원형으로 바르게 썼다.")], 3, R118, S118, st="R")
mk(1, 118, "E", [("It is vital that everyone follow the safety rules.", OKB), ("The doctor suggested that Dad walk every day.", OKB), ("The school required that all students be present.", OKB),
                 ("I proposed that we meet after lunch.", OKB), ("The manager demanded that the report was submitted today.", "that절의 동사를 원형 be submitted로 써야 해 틀렸다.")], 5, R118, S118, st="R")
mk(1, 118, "F", [("The doctor recommended that he takes a rest.", "that절의 동사를 원형 take로 써야 해 틀렸다."), ("It is desirable that the child get enough sleep.", OKB), ("The police demanded that the driver stop the car.", OKB),
                 ("The guide advised that we not touch the paintings.", "that절 부정은 not + 동사원형으로 바르게 썼다."), ("The club proposed that the fee be lowered.", OKB)], 1, R118, S118, st="R")

# 1-119 <보기> 설명 빈칸: B는 밑줄 복원, C~F는 (A)~(C) 항목을 새로 구성하고 그럴듯한 오답으로
U = lambda x: f"(<u>      {x}      </u>)"
F(1, 119, "B", st="R", p=V(1, 119, "B")["passage"].replace("(A)_____", U("A")).replace("(B)_____", U("B")).replace("(C)_____", U("C")), keepx=True,
  s="발문을 원문항과 같게 하고, 설명의 빈칸 (A)~(C)에 원문항처럼 밑줄을 넣었다.")
R119 = "요구·제안·필요를 나타내는 that절에는 주어와 관계없이 동사원형을 쓰며, should + 동사원형으로 바꿔 쓸 수 있다. insist가 ‘사실을 주장하다’는 뜻일 때는 직설법(시제 일치)을 쓴다."
S119 = "정답 조합(원형 가정법 - should - 동사원형)이 원문항과 같았고 오답 네 조합이 C~F 모두 같으며 뻔히 틀렸다. (A)~(C)가 묻는 내용을 유형마다 다르게 구성하고, 비슷한 용어끼리 헷갈리는 오답으로 새로 만들었다. 빈칸에 밑줄을 넣었다."
def f119(t, p, c, a, need):
    F(1, 119, t, p=p, c=c, a=a, r=R119, n=tnotes(c, a, need, labs=["(A)", "(B)", "(C)"]), s=S119 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f119("C", f"<보기>\n\"The doctor recommended that Tom rest for a week.\"\n설명: 권고를 나타내는 recommend 뒤 that절의 동사는 {U('A')}을(를) 쓴다. 이때 조동사 {U('B')}이(가) 생략된 것으로 볼 수 있으므로, 주어 Tom이 3인칭 단수여도 동사에 {U('C')}을(를) 붙이지 않는다.",
     ["(A) 동사원형 - (B) should - (C) -s", "(A) 3인칭 단수형 - (B) should - (C) -s", "(A) 동사원형 - (B) must - (C) -ed", "(A) 과거형 - (B) would - (C) -s", "(A) 동사원형 - (B) will - (C) -ing"], 1,
     ["(A)는 권고의 that절이므로 동사원형이다.", "(B)는 생략된 것으로 보는 조동사 should이다.", "(C)는 3인칭 단수 현재형에 붙는 -s이다."])
f119("D", f"<보기>\n\"They demanded that the door be locked.\"\n설명: 요구를 나타내는 demand 뒤 that절의 동사는 주어와 관계없이 {U('A')}을(를) 쓴다. 문이 잠기는 것이므로 be + {U('B')}의 수동 형태가 되고, be 앞에는 조동사 {U('C')}이(가) 생략된 것으로 볼 수 있다.",
     ["(A) 과거형 - (B) 과거분사 - (C) would", "(A) 동사원형 - (B) 현재분사 - (C) should", "(A) 3인칭 단수형 - (B) 과거분사 - (C) must", "(A) 동사원형 - (B) 과거분사 - (C) should", "(A) 동사원형 - (B) 과거분사 - (C) will"], 4,
     ["(A)는 요구의 that절이므로 동사원형이다.", "(B)는 수동이므로 과거분사이다.", "(C)는 생략된 것으로 보는 조동사 should이다."])
f119("E", f"<보기>\n\"Jane insisted that Leo apologize.\"\n설명: 이 문장의 insist는 {U('A')}의 뜻이므로 that절에 주어와 관계없이 {U('B')}을(를) 쓴다. 반면 insist가 ‘~라고 주장하다’는 뜻이면 that절에 {U('C')}을(를) 써서 Jane insisted that Leo had apologized.처럼 쓴다.",
     ["(A) 사실 주장 - (B) 동사원형 - (C) 직설법", "(A) 요구 - (B) 동사원형 - (C) 직설법", "(A) 요구 - (B) 3인칭 단수형 - (C) 원형 가정법", "(A) 사실 주장 - (B) 과거형 - (C) 원형 가정법", "(A) 요구 - (B) 과거형 - (C) 직설법"], 2,
     ["(A)는 that절에 동사원형 apologize가 왔으므로 요구의 뜻이다.", "(B)는 요구의 that절이므로 동사원형이다.", "(C)는 사실을 주장할 때 쓰는 직설법(시제 일치)이다."])
f119("F", f"<보기>\n\"The rule requires that every student wear an ID card.\"\n설명: 주어 every student가 단수인데도 동사를 {U('A')}인 wear로 썼다. 이 자리에는 {U('B')}을(를) 써도 같은 뜻이 되며, 이렇게 쓰는 것은 require가 {U('C')}을(를) 나타내기 때문이다.",
     ["(A) 동사원형 - (B) will + 동사원형 - (C) 필요·요구", "(A) 3인칭 단수형 - (B) should + 동사원형 - (C) 필요·요구", "(A) 동사원형 - (B) should + 동사원형 - (C) 사실 보고", "(A) 동사원형 - (B) should + 동사원형 - (C) 필요·요구", "(A) 과거형 - (B) would + 동사원형 - (C) 필요·요구"], 4,
     ["(A)는 wear가 동사원형이다.", "(B)는 같은 뜻의 should + 동사원형이다.", "(C)는 require가 나타내는 필요·요구이다."])

# 1-120 화법 전환 틀린 것으로만 묶인 것: 긴 조건 삭제, 틀린 항목 2~3개, 다른 조합은 모두 옳은 항목을 하나 이상 포함
R120 = "평서문은 said that/told + 사람 + that, 의문문은 asked + 의문사 + 주어 + 동사, 명령문은 told + 사람 + (not) to부정사로 바꾼다. 전달동사가 과거이면 시제를 한 단계 뒤로 옮기고 tomorrow → the next day, today → that day, now → then으로 바꾼다."
S120 = "발문에 ‘수일 뒤 다른 청자에게 전달, 전달자는 we 집단이 아님’ 같은 긴 조건이 붙었다. 발문을 원문항과 같게 하고, 원문항처럼 틀린 항목이 여럿인 조합형 선택지로 만들었다. 이 발문(‘틀린 문장으로만 묶인 것’)에서 답이 하나가 되도록 정답 외 조합에는 옳은 항목을 하나 이상 넣었다."
def f120(t, pairs, judge, bad, c, a, extra=""):
    p = "\n".join(f"({k}) {q}\n→ {r_}" for k, q, r_ in pairs)
    F(1, 120, t, st="R", p=p, c=c, a=a, r=R120, pre=["항목별 판정:"] + judge, k=f"화법 전환이 틀린 것은 {bad}이다.", n=setnotes(c, bad, "틀린 항목"), s=S120 + extra + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f120("B", [("가", "Mina said, \"I am busy.\"", "Mina said that she was busy."), ("나", "Tom asked me, \"When will you leave?\"", "Tom asked me when would I leave."), ("다", "Jane said, \"I have finished.\"", "Jane said that she had finished."),
           ("라", "Leo said, \"I met her yesterday.\"", "Leo said that he had met her the day before."), ("마", "The coach said to us, \"Practice harder.\"", "The coach told us practice harder.")],
     ["(가) 옳음: am → was.", "(나) 틀림: 간접의문문은 when I would leave 어순이다.", "(다) 옳음: have finished → had finished.", "(라) 옳음: met → had met, yesterday → the day before.", "(마) 틀림: 명령문은 told us to practice harder로 쓴다."],
     "(나), (마)", ["(가), (나)", "(나), (마)", "(다), (라)", "(나), (다), (마)", "(가), (라), (마)"], 2)
f120("C", [("가", "Mina said, \"I will finish tomorrow.\"", "Mina said that she would finish tomorrow."), ("나", "Tom said, \"I am tired now.\"", "Tom said that he was tired then."), ("다", "Jane asked me, \"Where do you live?\"", "Jane asked me where did I live."),
           ("라", "Leo said, \"I finished yesterday.\"", "Leo said that he had finished the day before."), ("마", "The teacher said to me, \"Open the window.\"", "The teacher said me to open the window.")],
     ["(가) 틀림: tomorrow는 the next day로 바꿔야 한다.", "(나) 옳음: am → was, now → then.", "(다) 틀림: 간접의문문은 where I lived 어순이다.", "(라) 옳음: finished → had finished, yesterday → the day before.", "(마) 틀림: 명령문은 told me to open으로 쓴다."],
     "(가), (다), (마)", ["(가), (나)", "(다), (라)", "(가), (다), (마)", "(나), (다), (마)", "(가), (라), (마)"], 3, " 정답 조합이 원문항((나), (다), (마))과 같아 틀린 항목을 바꿨다.")
f120("D", [("가", "Tom said, \"I can help.\"", "Tom said that he could help."), ("나", "Mina said to me, \"I will call you tomorrow.\"", "Mina said that she will call me tomorrow."), ("다", "Jane asked me, \"Why are you late?\"", "Jane asked me why was I late."),
           ("라", "Leo said, \"I saw him yesterday.\"", "Leo said that he had seen him the day before."), ("마", "Mom said to me, \"Do not run.\"", "Mom told me not to run.")],
     ["(가) 옳음: can → could.", "(나) 틀림: will → would, tomorrow → the next day로 바꿔야 한다.", "(다) 틀림: 간접의문문은 why I was late 어순이다.", "(라) 옳음: saw → had seen, yesterday → the day before.", "(마) 옳음: 부정 명령문은 told me not to run이다."],
     "(나), (다)", ["(가), (나)", "(다), (라)", "(나), (라), (마)", "(가), (다), (마)", "(나), (다)"], 5)
f120("E", [("가", "Tom said, \"I will be late.\"", "Tom said he will be late."), ("나", "Mina asked me, \"Where did you go?\"", "Mina asked me where I had gone."), ("다", "Jane said, \"I can drive.\"", "Jane said she could drive."),
           ("라", "Leo said, \"I finished today.\"", "Leo said he had finished today."), ("마", "Dad said to me, \"Do not touch it.\"", "Dad told me not to touch it.")],
     ["(가) 틀림: will → would로 바꿔야 한다.", "(나) 옳음: 간접의문문 어순이고 did go → had gone.", "(다) 옳음: can → could.", "(라) 틀림: today는 that day로 바꿔야 한다.", "(마) 옳음: 부정 명령문은 told me not to touch이다."],
     "(가), (라)", ["(가), (라)", "(나), (다)", "(가), (나), (라)", "(다), (마)", "(라), (마)"], 1, " 틀린 항목이 하나도 없어 ‘없음’이 정답이던 것을 고쳤다.")
f120("F", [("가", "Mina said, \"I have lost my key.\"", "Mina said she had lost her key."), ("나", "Tom asked, \"Why did Jane leave?\"", "Tom asked why Jane had left."), ("다", "Jane said, \"I will call tonight.\"", "Jane said she will call that night."),
           ("라", "Leo said to me, \"Close the door.\"", "Leo told me to close the door."), ("마", "Mom said to me, \"Do not be late.\"", "Mom said me not to be late.")],
     ["(가) 옳음: have lost → had lost.", "(나) 옳음: 간접의문문 어순이고 did leave → had left.", "(다) 틀림: will → would로 바꿔야 한다.", "(라) 옳음: 명령문은 told me to close이다.", "(마) 틀림: said 뒤에 사람을 바로 쓸 수 없다. told me not to be late."],
     "(다), (마)", ["(가), (다)", "(나), (라)", "(다), (마)", "(가), (나), (마)", "(라), (마)"], 3)


# ---- 2차 감수(2026-10) 추가 ----
# 1-115 F: 조건 없이는 옳고 그름이 갈리는 C(asked why Jane left)·D(Neither of … are)를 분명하게
f115("F", ["A) The disabled need accessible facilities.", "B) Tom said he had finished the work.", "C) Mina asked why Jane had left.", "D) Each of the answers are correct.", "E) Jane told me she would call.", "F) The police are searching the area."],
     ["A) 옳음: the disabled는 ‘장애가 있는 사람들’로 복수 동사 need를 쓴다.", "B) 옳음: 말한 때보다 앞선 일을 had finished로 나타냈다.", "C) 옳음: asked + why + 주어 + 동사 어순이고 시제도 had left로 옮겼다.",
      "D) 틀림: each of + 복수명사는 단수 동사 is를 쓴다.", "E) 옳음: told + 사람 뒤에 would call로 전달했다.", "F) 옳음: police는 항상 복수이다."],
     "A, B, C, E, F", V(1, 115, "F")["c"], 3,
     "발문의 ‘격식 문어 기준, 영국 영어 허용’ 조건을 지워 원문항 발문으로 되돌렸다. 조건이 없으면 C ‘asked why Jane left’(시제를 옮기지 않음)와 D ‘Neither of the answers are’(구어에서 쓰임)는 옳고 그름이 갈릴 수 있어, C는 had left로, D는 분명히 틀린 ‘Each of the answers are’로 바꿨다. 한 줄에 한 문장씩 나눴다.")
