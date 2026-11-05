# 5급 CH5 -ing형·과거진행형 (41~50) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def talk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 옳지 않은 설명이다. 따라서 정답이다." if i + 1 == a else " 옳은 설명이다. 따라서 오답이다.")) if w.endswith("므로") else (w + (" 옳지 않은 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.")) for i, (_, w) in enumerate(items)], k=items[a-1][1], s=s + ipos(a), **kw)
R_PPR = "과거진행형은 was/were + 동사원형-ing로 과거의 어느 때에 진행 중이던 일을 나타낸다. 주어가 I·3인칭 단수면 was, you·복수면 were를 쓰고, 부정문은 was/were 뒤에 not을, 의문문은 was/were를 주어 앞에 둔다."

# 5-43 원문항 발문
F(5, 43, "B", st="R", s="발문에 ‘과거진행형으로’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 5-41 -ing형 짝: 31번과 다른 동사, 유형마다 새로
R541 = "-ing형은 대부분 동사원형에 -ing를 붙인다. -e로 끝나면 e를 빼고, 강세 있는 단모음 + 단자음으로 끝나면 자음을 한 번 더 쓴다. 모음이 두 개이거나(wait), 강세가 앞 음절에 있거나(visit), x로 끝나면 자음을 겹쳐 쓰지 않으며, y로 끝나면 그대로 -ing를 붙인다."
S541 = "옳은 짝 오답 네 개가 유형마다 같았고, 정답 짝(run, make, lie, swim)이 같은 유형의 31번 정답과 겹쳤다. 31번과 다른 동사로 옳은 짝과 정답 짝을 유형마다 새로 썼다."
E_ = "-e로 끝나 e를 빼고 -ing를 바르게 붙였으므로"; DBL = "단모음 + 단자음으로 끝나 자음을 한 번 더 쓰고 -ing를 바르게 붙였으므로"; Y = "y로 끝나도 그대로 -ing를 바르게 붙였으므로"
def f541(t, items, a, s=S541):
    mk(5, 41, t, items, a, R541, s)
f541("C", [("close - closing", E_), ("hug - hugging", DBL), ("buy - buying", Y), ("jog - jogging", DBL), ("cry - criing", "y로 끝나는 동사는 y를 그대로 두고 crying으로 써야 하므로")], 5)
f541("D", [("win - winning", DBL), ("smile - smiling", E_), ("stay - staying", Y), ("visit - visitting", "강세가 앞 음절에 있어 t를 겹쳐 쓰지 않고 visiting으로 써야 하므로"), ("hope - hoping", E_)], 4)
f541("E", [("drive - driving", E_), ("wait - waitting", "모음 두 개(ai) 뒤의 자음은 겹쳐 쓰지 않으므로 waiting으로 써야 하므로"), ("dig - digging", DBL), ("say - saying", Y), ("live - living", E_)], 2)
f541("F", [("bake - baking", E_), ("pay - paying", Y), ("fix - fixxing", "x는 겹쳐 쓰지 않으므로 fixing으로 써야 하므로"), ("shut - shutting", DBL), ("lose - losing", E_)], 3)

# 5-42 과거진행형이 아닌 문장: 짝 없이 유형마다 새로
S542 = "정답 문장과 같은 문장의 과거진행형이 함께 있어 대비 단서가 되었고 오답 네 개가 C와 똑같았다. 짝 문장 없이 유형마다 새로 썼다."
PP = "was/were + -ing로 된 과거진행형 문장이므로"
def f542(t, items, a, s=S542):
    mk(5, 42, t, [(x, w or PP) for x, w in items], a, R_PPR, s)
f542("C", [("My dad was driving to work.", ""), ("The girls were singing a song.", ""), ("I was waiting for the bus.", ""), ("We were talking on the phone.", ""), ("Tom is brushing his teeth.", "is + -ing로 된 현재진행형 문장이므로")], 5)
f542("D", [("The cat was sleeping on the bed.", ""), ("He watched a movie last night.", "과거형 watched만 쓴 단순 과거 문장이므로"), ("They were cleaning the classroom.", ""), ("You were laughing loudly.", ""), ("She was taking a shower.", "")], 2,
     S542 + " 정답을 단순 과거 문장으로 하여 과거형과 과거진행형을 구별하게 했다.")
f542("E", [("I was riding my bike.", ""), ("The kids were building a sandcastle.", ""), ("Jane was baking cookies.", ""), ("We are having lunch now.", "are + -ing로 된 현재진행형 문장이므로"), ("It was snowing in the morning.", "")], 4)
f542("F", [("They are swimming in the pool.", "are + -ing로 된 현재진행형 문장이므로"), ("Dad was reading the newspaper.", ""), ("The students were running on the track.", ""), ("I was listening to music.", ""), ("My mom was making soup.", "")], 1)

# 5-44 밑줄 고치기: 원문항 발문, 고쳐 쓴 말이 하나로 정해지게
S544 = "발문에 ‘원래 동사의 뜻을 유지하면서 과거진행형으로’가 붙어 고칠 형태를 알려 주었다. 원문항 발문으로 되돌리고, 그 조건 없이도 답이 하나로 정해지도록 오답을 주어-be동사 일치·be + 동사원형 오류로 바꿨다."
def f544(t, p, items, a, s=S544):
    mk(5, 44, t, items, a, R_PPR, s, st="R", p=p, okdup=True)
f544("B", "- Tom <u>were reading</u> a comic book.\n- We <u>was waiting</u> for the train.",
     [("was reading - were waiting", "Tom에 was, We에 were를 쓰고 -ing형을 바르게 썼으므로"), ("were read - was wait", "Tom에 were, We에 was를 썼고 be동사 뒤에 동사원형을 썼으므로"), ("was read - were wait", "be동사 뒤에 동사원형 read, wait를 썼으므로"),
      ("were reading - were waiting", "첫째 문장: 3인칭 단수 Tom에는 was를 써야 하므로"), ("was reading - was waiting", "둘째 문장: 주어 We에는 were를 써야 하므로")], 1,
     "발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f544("C", "- My brother <u>were washing</u> his face.\n- They <u>was playing</u> soccer.",
     [("were washing - were playing", "첫째 문장: 3인칭 단수 My brother에는 was를 써야 하므로"), ("was washing - were playing", "My brother에 was, They에 were를 쓰고 -ing형을 바르게 썼으므로"), ("was washing - were play", "둘째 문장: be동사 뒤에는 -ing형 playing을 써야 하므로"),
      ("was washing - was playing", "둘째 문장: 복수 주어 They에는 were를 써야 하므로"), ("is washing - was playing", "둘째 문장: 복수 주어 They에는 were를 써야 하므로")], 2,
     S544 + " 첫째 문장이 B(Tom were reading a comic book.)와 거의 같아 다른 문장으로 바꿨다.")
f544("D", "- I <u>were studying</u> English.\n- Jane <u>was write</u> a letter.",
     [("were studying - was writing", "첫째 문장: 주어 I에는 was를 써야 하므로"), ("was studying - were writing", "둘째 문장: 3인칭 단수 Jane에는 was를 써야 하므로"), ("was study - was writing", "첫째 문장: be동사 뒤에는 -ing형 studying을 써야 하므로"),
      ("was studying - was writing", "I와 Jane에 was를 쓰고 -ing형을 바르게 썼으므로"), ("was studying - was write", "둘째 문장: be동사 뒤에는 -ing형 writing을 써야 하므로")], 4, "발문이 ‘원래 동사의 뜻을 유지하면서 과거진행형으로’라고 고칠 형태를 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f544("E", "- We <u>was running</u>.\n- He <u>were watching</u> TV.",
     [("were running - were watching", "둘째 문장: 3인칭 단수 He에는 was를 써야 하므로"), ("were run - was watching", "첫째 문장: be동사 뒤에는 -ing형 running을 써야 하므로"), ("were running - was watch", "둘째 문장: be동사 뒤에는 -ing형 watching을 써야 하므로"),
      ("was running - was watching", "첫째 문장: 주어 We에는 were를 써야 하므로"), ("were running - was watching", "We에 were, He에 was를 쓰고 -ing형을 바르게 썼으므로")], 5, "발문이 ‘원래 동사의 뜻을 유지하면서 과거진행형으로’라고 고칠 형태를 알려 주었다. 원문항 발문으로 되돌리고, 보기 순서를 바꿔 정답 위치가 D와 겹치지 않게 했다.")
f544("F", "- The boys <u>was sleeping</u>.\n- I <u>was cook</u> dinner.",
     [("was sleeping - was cooking", "첫째 문장: 복수 주어 The boys에는 were를 써야 하므로"), ("were sleep - was cooking", "첫째 문장: be동사 뒤에는 -ing형 sleeping을 써야 하므로"), ("were sleeping - was cooking", "The boys에 were, I에 was를 쓰고 -ing형을 바르게 썼으므로"),
      ("were sleeping - were cooking", "둘째 문장: 주어 I에는 was를 써야 하므로"), ("were sleeping - was cook", "둘째 문장: be동사 뒤에는 -ing형 cooking을 써야 하므로")], 3, "발문이 ‘원래 동사의 뜻을 유지하면서 과거진행형으로’라고 고칠 형태를 알려 주었다. 원문항 발문으로 되돌리고, 보기 순서를 바꿔 정답 위치가 D와 겹치지 않게 했다.")

# 5-45 틀린 문장: 원문항 발문, 긍정·부정문을 섞어 짝 없이
S545 = "원문항은 긍정·부정 과거진행형을 섞어 판별하는데, 변형은 모두 부정문이라 범위가 좁았고 짝 문장과 같은 오답이 반복되었다. 긍정·부정문을 섞어 짝 문장 없이 유형마다 새로 썼다."
OK45 = "주어에 맞는 was/were와 -ing형으로 바르게 썼으므로"
def f545(t, items, a, s=S545):
    mk(5, 45, t, [(x, w or OK45) for x, w in items], a, R_PPR, s, st="R")
f545("B", [("The boys were shouting in the hall.", ""), ("I wasn't sleeping at midnight.", ""), ("Jane weren't listening to the guide.", "3인칭 단수 주어 Jane에는 wasn't를 써야 하므로"), ("We were using the computer.", ""), ("Mom wasn't driving fast.", "")], 3,
     "발문이 ‘과거진행형 부정문이 틀린 것’으로 범위를 알려 주었고, 정답과 짝을 이루는 옳은 문장(Jane wasn't listening …)이 있었다. 원문항 발문으로 되돌리고 짝 문장을 빼고 긍정문을 섞었다.")
f545("C", [("Tom was playing the piano.", ""), ("The girls wasn't dancing.", "복수 주어 The girls에는 weren't를 써야 하므로"), ("I wasn't watching TV.", ""), ("You were running fast.", ""), ("It was raining hard.", "")], 2)
f545("D", [("We weren't eating lunch.", ""), ("My sister was talking on the phone.", ""), ("They were swimming in the sea.", ""), ("The dog wasn't barking.", ""), ("I were drawing a picture.", "주어 I에는 was를 써야 하므로")], 5)
f545("E", [("He was not wearing a cap.", ""), ("The baby wasn't crying.", ""), ("We were walking home.", ""), ("Mina and Jiho was studying together.", "복수 주어 Mina and Jiho에는 were를 써야 하므로"), ("You weren't listening to me.", "")], 4)
f545("F", [("She not was cooking dinner.", "부정문은 was 뒤에 not을 두어 was not cooking으로 써야 하므로"), ("The kids weren't sleeping.", ""), ("I was reading a novel.", ""), ("They were cleaning the room.", ""), ("Dad wasn't working late.", "")], 1)

# 5-46 원문항 발문: 빈칸 주어와 어울리는 be동사 과거형
R546 = "be동사 과거형은 주어가 I·3인칭 단수면 was, you·복수면 were를 쓴다. am, is, are는 현재형이다."
S546 = "발문이 원문항과 달랐다. 원문항처럼 빈칸 앞 주어를 밝혀 묻는 발문으로 바꿨다. 보기와 정답은 그대로다."
def f546(t, subj, items, a):
    mk(5, 46, t, items, a, R546, S546, st=f"다음 빈칸에 {subj} 어울리는 be동사의 과거형을 고르세요.", okdup=True)
PR = "현재형이라 과거형을 묻는 조건에 맞지 않으므로"
f546("B", "'The children'과", [("were", "복수 주어 The children의 be동사 과거형이므로"), ("is", PR), ("was", "was는 I·3인칭 단수 주어에 쓰므로"), ("am", PR), ("are", PR)], 1)
f546("C", "'They'와", [("were", "복수 주어 They의 be동사 과거형이므로"), ("is", PR), ("was", "was는 I·3인칭 단수 주어에 쓰므로"), ("are", PR), ("am", PR)], 1)
f546("D", "'I'와", [("was", "주어 I의 be동사 과거형이므로"), ("are", PR), ("were", "were는 you·복수 주어에 쓰므로"), ("is", PR), ("am", PR)], 1)
f546("E", "'We'와", [("was", "was는 I·3인칭 단수 주어에 쓰므로"), ("am", PR), ("is", PR), ("were", "복수 주어 We의 be동사 과거형이므로"), ("are", PR)], 4)
f546("F", "'Jane'과", [("is", PR), ("were", "were는 you·복수 주어에 쓰므로"), ("are", PR), ("was", "3인칭 단수 주어 Jane의 be동사 과거형이므로"), ("am", PR)], 4)

# 5-48 단어 배열: 원문항 발문, 주어진 단어만으로 만든 어순 오류 오답
R548 = "과거진행형 의문문은 Was/Were + 주어 + 동사원형-ing ~?의 어순으로 쓴다. 평서문 어순에 물음표만 붙이거나 -ing형을 주어 앞이나 목적어 뒤에 두지 않는다."
S548 = "발문이 ‘Was 또는 Were로 시작하는 기본 어순의 과거진행형 의문문’이라고 정답 형식을 알려 주었고, 소문자·마침표 오답은 어순 판단 없이 지워졌다. 원문항 발문으로 되돌리고, 원문항처럼 주어진 단어만으로 만든 어순 오류로 오답을 바꿨다."
DECL = "평서문 어순에 물음표만 붙였으므로"; OK48 = "Was/Were + 주어 + -ing의 어순으로 바르게 배열했으므로"
def f548(t, items, a, s=S548):
    mk(5, 48, t, items, a, R548, s, st="R")
f548("B", [("Tom was sleeping at eight?", DECL), ("Was Tom sleeping at eight?", OK48), ("Was sleeping Tom at eight?", "-ing형 sleeping이 주어 Tom보다 앞에 왔으므로"), ("At eight Tom was sleeping?", DECL), ("Was Tom at eight sleeping?", "-ing형 sleeping이 at eight 뒤로 밀려났으므로")], 2,
     "발문이 ‘Was 또는 Were로 시작하는 기본 어순의 과거진행형 의문문’이라고 정답 형식을 알려 주었고, 주어진 단어에 없는 Were, Did로 만든 오답이 있었다. 원문항 발문으로 되돌리고 주어진 단어만으로 만든 어순 오류로 오답을 바꿨다.")
f548("C", [("She was reading a book?", DECL), ("Was reading she a book?", "-ing형 reading이 주어 she보다 앞에 왔으므로"), ("Was she a book reading?", "-ing형 reading이 목적어 a book 뒤에 왔으므로"), ("Was she reading a book?", OK48), ("Reading was she a book?", "-ing형 reading으로 문장을 시작했으므로")], 4)
f548("D", [("You were studying English?", DECL), ("Were studying you English?", "-ing형 studying이 주어 you보다 앞에 왔으므로"), ("Were you English studying?", "-ing형 studying이 목적어 English 뒤에 왔으므로"), ("Studying were you English?", "-ing형 studying으로 문장을 시작했으므로"), ("Were you studying English?", OK48)], 5)
f548("E", [("Was Tom watching TV?", OK48), ("Tom was watching TV?", DECL), ("Was watching Tom TV?", "-ing형 watching이 주어 Tom보다 앞에 왔으므로"), ("Was Tom TV watching?", "-ing형 watching이 목적어 TV 뒤에 왔으므로"), ("Watching Tom was TV?", "-ing형 watching으로 문장을 시작했으므로")], 1)
f548("F", [("Were we dinner eating?", "-ing형 eating이 목적어 dinner 뒤에 왔으므로"), ("We were eating dinner?", DECL), ("Were we eating dinner?", OK48), ("Were eating we dinner?", "-ing형 eating이 주어 we보다 앞에 왔으므로"), ("Eating were we dinner?", "-ing형 eating으로 문장을 시작했으므로")], 3)

# 5-49 (A)(B) 연결: 원문항 발문, 단순 과거 오답 대신 수 일치·시제·be동사 누락 오답
S549 = "발문이 ‘(A)에는 과거 be동사, (B)에는 ○○를 사용하여 과거진행형을 넣으시오’라고 두 빈칸의 정답 형태를 알려 주었다. 원문항 발문으로 되돌리고, 그 조건 없이는 정답이 될 수 있는 단순 과거 오답을 수 일치 오류로 바꿨다."
def f549(t, p, items, a, s=S549):
    mk(5, 49, t, items, a, R_PPR, s, st="R", p=p, okdup=True)
f549("B", "At nine last night, Jane (A)________ at home. She (B)________ a report for school.",
     [("was — were writing", "(B): 3인칭 단수 She에는 was writing을 써야 하므로"), ("is — is writing", "at nine last night의 일이므로 현재형 is를 쓸 수 없으므로"), ("was — was writing", "(A)에 was, (B)에 과거진행형 was writing을 바르게 썼으므로"),
      ("were — was writing", "(A): 3인칭 단수 Jane에는 was를 써야 하므로"), ("was — writing", "(B): be동사 없이 -ing형만으로는 동사 자리에 쓸 수 없으므로")], 3)
f549("C", "At 5 yesterday, they (A)________ at the park. They (B)________ soccer.",
     [("are — are playing", "yesterday의 일이므로 현재형 are를 쓸 수 없으므로"), ("was — were playing", "(A): 복수 주어 they에는 were를 써야 하므로"), ("were — playing", "(B): be동사 없이 -ing형만으로는 동사 자리에 쓸 수 없으므로"),
      ("were — was playing", "(B): 복수 주어 They에는 were playing을 써야 하므로"), ("were — were playing", "(A)에 were, (B)에 과거진행형 were playing을 바르게 썼으므로")], 5)
f549("D", "At eight yesterday evening, Jane (A)________ at home. She (B)________ a book.",
     [("was — was reading", "(A)에 was, (B)에 과거진행형 was reading을 바르게 썼으므로"), ("were — was reading", "(A): 3인칭 단수 Jane에는 was를 써야 하므로"), ("was — reading", "(B): be동사 없이 -ing형만으로는 동사 자리에 쓸 수 없으므로"),
      ("was — were reading", "(B): 3인칭 단수 She에는 was reading을 써야 하므로"), ("is — is reading", "yesterday evening의 일이므로 현재형 is를 쓸 수 없으므로")], 1)
f549("E", "At noon yesterday, we (A)________ in the kitchen. We (B)________ lunch.",
     [("was — were eating", "(A): 주어 we에는 were를 써야 하므로"), ("were — were eating", "(A)에 were, (B)에 과거진행형 were eating을 바르게 썼으므로"), ("were — eating", "(B): be동사 없이 -ing형만으로는 동사 자리에 쓸 수 없으므로"),
      ("are — are eating", "yesterday의 일이므로 현재형 are를 쓸 수 없으므로"), ("were — was eating", "(B): 주어 We에는 were eating을 써야 하므로")], 2)
f549("F", "At seven yesterday evening, Tom (A)________ in his room. He (B)________ TV.",
     [("is — is watching", "yesterday evening의 일이므로 현재형 is를 쓸 수 없으므로"), ("were — was watching", "(A): 3인칭 단수 Tom에는 was를 써야 하므로"), ("was — watching", "(B): be동사 없이 -ing형만으로는 동사 자리에 쓸 수 없으므로"),
      ("was — was watching", "(A)에 was, (B)에 과거진행형 was watching을 바르게 썼으므로"), ("was — were watching", "(B): 3인칭 단수 He에는 was watching을 써야 하므로")], 4)

# 5-50 작문 과정 설명: 원문항 발문, 완성 문장·반대 짝 없이 서로 독립된 설명
R550 = "과거진행형 의문사 의문문은 의문사 + was/were + 주어 + 동사원형-ing ~?의 어순으로 쓴다. 시각 앞에는 at을 쓰고, be동사는 주어에 맞춰 was/were를 고른다."
S550 = "선택지에 완성 문장이나 틀린 설명과 정반대인 옳은 설명(‘복수 주어이므로 were’ 등)이 있어 정답이 바로 드러났다. 원문항 발문으로 되돌리고, 완성 문장과 반대 짝 없이 서로 독립된 설명 다섯 개로 유형마다 새로 썼다."
def f550(t, ko, items, a, s=S550):
    talk(5, 50, t, items, a, R550, s, st="R", p="<보기>\n" + ko)
f550("B", "그들은 여섯 시에 무엇을 하고 있었니?",
     [("'무엇'을 묻는 질문이므로 의문사 What을 문장 맨 앞에 둔다.", "무엇을 묻는 의문사 What은 문장 맨 앞에 오므로"), ("'하고 있었니'의 '하다'는 do로 나타내고, 진행의 뜻이므로 doing으로 쓴다.", "진행 중이던 동작은 do의 -ing형 doing으로 나타내므로"),
      ("they는 한 무리를 가리키므로 단수로 보아 be동사 was를 쓴다.", "they는 복수 대명사라 be동사 과거형 were를 써야 하므로"), ("'여섯 시에'는 시각 앞에 쓰는 전치사 at을 써서 at six로 나타낸다.", "시각 앞에는 전치사 at을 쓰므로"),
      ("의문문이므로 be동사를 주어 they 앞에 둔다.", "진행형 의문문은 be동사가 주어 앞에 오므로")], 3,
     "제시문에 완성 문장(→ What were they doing at six?)이 있었고, 틀린 설명(3인칭 단수이므로 was)과 정반대인 옳은 설명(복수이므로 were)이 함께 있었으며 발문도 달랐다. 원문항 발문으로 되돌리고, 완성 문장과 반대 짝을 빼 서로 독립된 설명으로 새로 썼다.")
f550("C", "그녀는 어제 8시에 무엇을 하고 있었니?",
     [("의문사 What으로 문장을 시작해 '무엇'을 묻는다.", "무엇을 묻는 의문사 What은 문장 맨 앞에 오므로"), ("'어제'는 yesterday로 나타내며 보통 문장 끝에 둔다.", "yesterday는 과거의 때를 나타내며 보통 문장 끝에 오므로"),
      ("'8시에'는 전치사 at을 써서 at eight로 나타낸다.", "시각 앞에는 전치사 at을 쓰므로"), ("'어제'라는 과거 표현이 있으므로 be동사 없이 did로 의문문을 만든다.", "‘하고 있었니’는 진행 중이던 일이라 did가 아니라 be동사 과거형 was로 의문문을 만들어야 하므로"),
      ("'하다'는 do이므로 진행의 뜻을 살려 doing으로 쓴다.", "진행 중이던 동작은 do의 -ing형 doing으로 나타내므로")], 4)
f550("D", "그들은 어제 무엇을 하고 있었니?",
     [("주어 they는 복수이므로 be동사 과거형 were를 쓴다.", "복수 주어의 be동사 과거형은 were이므로"), ("'무엇'은 목적어이므로 doing 뒤인 문장 끝에 What을 둔다.", "의문사 What은 목적어를 묻더라도 문장 맨 앞에 와야 하므로"),
      ("'하고 있었니'는 진행의 뜻이므로 do에 -ing를 붙인 doing을 쓴다.", "진행 중이던 동작은 do의 -ing형 doing으로 나타내므로"), ("'어제'는 yesterday로 나타내며 과거의 때를 알려 준다.", "yesterday는 과거의 때를 나타내므로"),
      ("의문문이므로 be동사가 주어 they보다 앞에 온다.", "진행형 의문문은 be동사가 주어 앞에 오므로")], 2)
f550("E", "Tom은 그때 무엇을 하고 있었니?",
     [("'하고 있었니'는 지난 일이므로 be동사 뒤에 do의 과거형 did를 쓴다.", "be동사 뒤에는 과거형 did가 아니라 -ing형 doing을 써야 진행의 뜻이 되므로"), ("'무엇'을 물으므로 의문사 What이 문장 첫머리에 온다.", "무엇을 묻는 의문사 What은 문장 맨 앞에 오므로"),
      ("Tom은 3인칭 단수이므로 be동사 과거형 was를 쓴다.", "3인칭 단수 주어의 be동사 과거형은 was이므로"), ("'그때'는 then으로 나타내며 과거의 한 시점을 가리킨다.", "then은 과거의 한때를 가리키는 말이므로"),
      ("be동사를 주어 Tom 앞에 두어 의문문을 만든다.", "진행형 의문문은 be동사가 주어 앞에 오므로")], 1)
f550("F", "우리는 그때 무엇을 하고 있었니?",
     [("then은 과거의 그때를 나타내는 시간 표현으로 문장 끝에 둔다.", "then은 과거의 한때를 나타내며 보통 문장 끝에 오므로"), ("의문사 What이 문장 첫머리에 와서 '무엇'을 묻는다.", "무엇을 묻는 의문사 What은 문장 맨 앞에 오므로"),
      ("진행 중이던 동작이므로 do에 -ing를 붙여 doing으로 쓴다.", "진행 중이던 동작은 do의 -ing형 doing으로 나타내므로"), ("의문문이므로 be동사를 주어 we 앞에 둔다.", "진행형 의문문은 be동사가 주어 앞에 오므로"),
      ("'우리'에는 '나'가 들어 있으므로 주어 I에 맞춰 be동사 was를 쓴다.", "주어 we는 복수이므로 be동사 과거형 were를 써야 하므로")], 5)


# ---- 2차 감수(2026-10) 추가 ----
# 5-43 C: 없는 형태(runn) → be + 동사원형 오류로
mk(5, 43, "C", [("They was running in the park.", "복수 주어 They에는 were를 써야 하므로"), ("They were running in the park.", "They에 were + running으로 ‘뛰고 있었다’를 바르게 나타냈으므로"), ("They did running in the park.", "진행형은 did가 아니라 be동사와 함께 쓰므로"),
    ("They were run in the park.", "were 뒤에는 동사원형이 아니라 -ing형 running을 써야 하므로"), ("They are running in the park.", "현재진행형이라 ‘뛰고 있었다’의 뜻이 되지 않으므로")], 2, R_PPR,
   "오답 ④의 runn은 쓰이지 않는 형태였다. 원문항의 오답(was goes)처럼 be동사 뒤의 동사 형태를 틀린 문장(were run)으로 바꿨다. 정답은 그대로다.")
# 5-47 F: 진행형이 아닌 질문(Were we late?) → 과거진행형 질문으로
mk(5, 47, "F", [("aren't", "과거의 일을 묻는 질문에 현재형으로 답할 수 없으므로"), ("didn't", "be동사 의문문에 did로 답할 수 없으므로"), ("weren't", "Were we ~?에 we weren't로 바르게 답했으므로"), ("isn't", "주어 we와 맞지 않고 시제도 현재이므로"), ("wasn't", "주어 we에는 was를 쓸 수 없으므로")], 3, R_PPR,
   "질문(Were we late?)이 과거진행형이 아니라 be동사 의문문이어서 이 단원과 맞지 않았다. 과거진행형 질문과 대답으로 바꿨다. 보기와 정답은 그대로다.",
   p="A: Were we making too much noise?\nB: No, we ________. We were talking quietly.")
