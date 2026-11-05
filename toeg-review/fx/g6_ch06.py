# 6급 CH6 의문사 의문문 (51~60) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
R_WH = "의문사 의문문은 의문사 + do/does + 주어 + 동사원형 ~?(일반동사) 또는 의문사 + be동사 + 주어 ~?로 쓴다. 3인칭 단수 주어에는 does를, 그 밖의 주어에는 do를 쓴다."

# 원문항 발문으로만 되돌리는 문항
for t in "BCDE": F(6, 52, t, st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
F(6, 60, "B", st="R", s="발문에 ‘단독으로 쓰는 기본형 직접 의문문’ 조건이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "CDEF": F(6, 58, t, st="R", s="발문이 ‘일반동사의 단순현재 긍정 의문문을 유지하여’라고 정답 형식을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDEF":
    F(6, 59, t, p=V(6, 59, t)["passage"].replace("(________)", "(<u>        </u>)"), s="원문항 빈칸의 밑줄이 사라졌다. 원문항처럼 빈칸에 밑줄을 되살렸다. 보기와 정답은 그대로다.")

# 6-52 F: E와 같은 Why 문항을 How로
F(6, 52, "F", st="R", p="_______ do you go to school?\n(너는 어떻게 학교에 가니?)", c=["What", "Who", "How", "Where", "When"], a=3, r="‘어떻게’라는 방법·수단은 How로, ‘무엇’은 What, ‘누구’는 Who, ‘어디’는 Where, ‘언제’는 When으로 묻는다.",
  n=["What은 ‘무엇’을 묻는 의문사이므로 오답이다.", "Who는 ‘누구’를 묻는 의문사이므로 오답이다.", "‘어떻게’라는 방법·수단을 묻는 의문사이므로 정답이다.", "Where는 ‘어디’를 묻는 의문사이므로 오답이다.", "When은 ‘언제’를 묻는 의문사이므로 오답이다."],
  s="발문이 원문항과 달랐고 정답(Why)과 문장 구조가 E와 거의 같았다. 원문항 발문으로 되돌리고 ‘어떻게’를 묻는 문장으로 바꿔 정답이 How가 되게 했다. 정답 위치 ③.")

# 6-53 How가 들어가지 않는 것: How 오답을 유형마다 새로
R653 = "How는 형용사·부사와 함께 정도를 묻거나(How often, How big, How deep) 단독으로 방법·상태를 묻는다. day, sport, subject처럼 명사 앞에서 종류를 물을 때는 What을 쓴다."
S653 = "How 오답 서너 개(How are you, How much, How old, How many books)가 C와 같아 C와 사실상 같은 문항이었다. How 오답을 유형마다 새로 썼다."
def f653(t, items, a, s=S653):
    mk(6, 53, t, items, a, R653, s)
f653("D", [("_______ often do you swim?", "How often으로 빈도를 묻는 말이라 How가 들어가므로"), ("_______ big is your house?", "How big으로 크기를 묻는 말이라 How가 들어가므로"), ("_______ heavy is the box?", "How heavy로 무게를 묻는 말이라 How가 들어가므로"),
           ("_______ day is it today?", "명사 day 앞에서 요일을 물으므로 How가 아니라 What이 들어가므로"), ("_______ do you spell your name?", "철자를 어떻게 쓰는지 방법을 묻는 How가 들어가므로")], 4)
f653("E", [("_______ deep is the lake?", "How deep으로 깊이를 묻는 말이라 How가 들어가므로"), ("_______ was your trip?", "여행이 어땠는지 상태를 묻는 How가 들어가므로"), ("_______ sport do you play?", "명사 sport 앞에서 종류를 물으므로 How가 아니라 What이 들어가므로"),
           ("_______ early do you get up?", "How early로 이른 정도를 묻는 말이라 How가 들어가므로"), ("_______ high can you jump?", "How high로 높이를 묻는 말이라 How가 들어가므로")], 3)
f653("F", [("_______ wide is the river?", "How wide로 폭을 묻는 말이라 How가 들어가므로"), ("_______ subject do you like best?", "명사 subject 앞에서 종류를 물으므로 How가 아니라 What이 들어가므로"), ("_______ well does he sing?", "How well로 잘하는 정도를 묻는 말이라 How가 들어가므로"),
           ("_______ late did you stay up?", "How late로 늦은 정도를 묻는 말이라 How가 들어가므로"), ("_______ can I get to the bank?", "가는 방법을 묻는 How가 들어가므로")], 2)

# 6-54 does/do 밑줄: 짝 없이 유형마다 새로
S654 = "정답 문장과 같은 문장의 옳은 형태가 함께 있어 대비 단서가 되었고 오답 네 개가 B와 똑같았다. 짝 문장 없이 유형마다 새로 썼다."
OK54 = "주어에 맞는 do/does를 바르게 썼으므로"
def f654(t, items, a, s=S654):
    mk(6, 54, t, [(x, w or OK54) for x, w in items], a, R_WH, s)
f654("B", [("Where <u>does</u> she live?", ""), ("Why <u>does</u> Tom run?", ""), ("How <u>do</u> you feel?", ""), ("What <u>does</u> you want?", "주어 you에는 does가 아니라 do를 써야 하므로"), ("When <u>do</u> they go?", "")], 4,
     "정답(What does you want?)과 짝을 이루는 옳은 문장(What do you want?)이 함께 있어 대비 단서가 되었다. 짝 문장을 다른 문장으로 바꿨다.")
f654("D", [("Why <u>do</u> Tom cry?", "3인칭 단수 주어 Tom에는 does를 써야 하므로"), ("Where <u>does</u> your aunt work?", ""), ("When <u>do</u> we eat lunch?", ""), ("What <u>do</u> your parents like?", ""), ("How <u>does</u> the bus get here?", "")], 1)
f654("E", [("What <u>does</u> your dog eat?", ""), ("Where <u>does</u> they play?", "복수 주어 they에는 does가 아니라 do를 써야 하므로"), ("How <u>do</u> I look?", ""), ("Why <u>do</u> you smile?", ""), ("When <u>does</u> Mina wake up?", "")], 2)
f654("F", [("What time <u>does</u> the class end?", ""), ("Who <u>do</u> you like?", ""), ("Where <u>do</u> the kids play?", ""), ("Why <u>does</u> she laugh?", ""), ("How <u>do</u> Jiho go home?", "3인칭 단수 주어 Jiho에는 does를 써야 하므로")], 5)

# 6-55 day/date/time 밑줄: 원문항 발문과 밑줄, 같은 질문 반복 없이
R655 = "What day는 요일, What date는 날짜, What time은 시각, What month는 달, What year는 연도, What season은 계절을 묻는다."
S655 = "원문항은 밑줄 친 day/date/time의 구별을 묻는데, 변형은 밑줄 없이 여러 질문과 대답의 짝을 판단하게 바뀌었고 같은 질문이 옳은 대답·틀린 대답으로 두 번 나와 대비 단서가 되었다. 원문항 발문으로 되돌리고 밑줄을 살려, 같은 질문이 반복되지 않게 유형마다 대화를 새로 썼다."
def f655(t, items, a, s=S655):
    mk(6, 55, t, items, a, R655, s, st="R")
f655("B", [("A: What <u>time</u> does the movie start? B: At seven.", "What time으로 시각을 묻고 알맞게 답했으므로"), ("A: What <u>day</u> is your piano lesson? B: It's on Monday.", "What day로 요일을 묻고 알맞게 답했으므로"), ("A: What <u>date</u> is your birthday? B: It's May 5th.", "What date로 날짜를 묻고 알맞게 답했으므로"),
           ("A: What <u>month</u> is it now? B: It's Tuesday.", "What month는 달을 묻는데 요일로 답했으므로"), ("A: What <u>year</u> did you move here? B: In 2020.", "What year로 연도를 묻고 알맞게 답했으므로")], 4,
     "원문항의 day/date 구별 대신 How old/How are you 구별을 물었고 짝을 이루는 대화가 있었으며 발문도 달랐다. 원문항 발문으로 되돌리고 밑줄 친 day/date/time 구별 대화로 새로 썼다.")
f655("C", [("A: What <u>date</u> is the school festival? B: It's Friday.", "What date는 날짜를 묻는데 요일로 답했으므로"), ("A: What <u>time</u> do you get up? B: At half past six.", "What time으로 시각을 묻고 알맞게 답했으므로"), ("A: What <u>day</u> do you play soccer? B: On Wednesdays.", "What day로 요일을 묻고 알맞게 답했으므로"),
           ("A: What <u>season</u> do you like? B: I like summer.", "What season으로 계절을 묻고 알맞게 답했으므로"), ("A: What <u>month</u> does school start? B: In March.", "What month로 달을 묻고 알맞게 답했으므로")], 1)
f655("D", [("A: What <u>day</u> comes after Sunday? B: Monday comes after Sunday.", "What day로 요일을 묻고 알맞게 답했으므로"), ("A: What <u>year</u> was your sister born in? B: In 2012.", "What year로 연도를 묻고 알맞게 답했으므로"), ("A: What <u>time</u> does the store close? B: It closes on Monday.", "What time은 시각을 묻는데 요일로 답했으므로"),
           ("A: What <u>date</u> is Christmas? B: It's December 25th.", "What date로 날짜를 묻고 알맞게 답했으므로"), ("A: What <u>season</u> is it in Korea now? B: It's winter.", "What season으로 계절을 묻고 알맞게 답했으므로")], 3)
f655("E", [("A: What <u>month</u> is your birthday in? B: It's in October.", "What month로 달을 묻고 알맞게 답했으므로"), ("A: What <u>date</u> is the concert? B: It's June 1st.", "What date로 날짜를 묻고 알맞게 답했으므로"), ("A: What <u>time</u> is lunch? B: It's at 12:30.", "What time으로 시각을 묻고 알맞게 답했으므로"),
           ("A: What <u>day</u> is it today? B: It's Sunday.", "What day로 요일을 묻고 알맞게 답했으므로"), ("A: What <u>season</u> comes after spring? B: It's 10 o'clock.", "What season은 계절을 묻는데 시각으로 답했으므로")], 5)
f655("F", [("A: What <u>time</u> is the meeting? B: It's at noon.", "What time으로 시각을 묻고 알맞게 답했으므로"), ("A: What <u>year</u> did you start school? B: In March.", "What year는 연도를 묻는데 달로 답했으므로"), ("A: What <u>date</u> is Halloween? B: It's October 31st.", "What date로 날짜를 묻고 알맞게 답했으므로"),
           ("A: What <u>day</u> do you go swimming? B: On Saturdays.", "What day로 요일을 묻고 알맞게 답했으므로"), ("A: What <u>month</u> do leaves turn red? B: In October.", "What month로 달을 묻고 알맞게 답했으므로")], 2)

# 6-56 How + 형용사: 원문항처럼 우리말 해석 없이 How + 형용사·부사
R656 = "How + 형용사·부사는 정도를 묻는다(How tall 키, How long 길이, How often 빈도, How far 거리, How heavy 무게). What, Who, Where, Why는 형용사 앞에서 정도를 묻지 못한다."
S656 = "원문항은 How + 형용사(How old)를 묻는데, 변형은 Where/What/When/Who 같은 기본 의문사를 묻고 우리말 해석을 붙여 쉬워졌다. 원문항 발문으로 되돌리고, 우리말 해석 없이 How + 형용사·부사를 묻는 문장으로 바꿨다."
NH = lambda w: f"{w}는 형용사·부사와 함께 정도를 묻지 못하므로"
def f656(t, p, items, a, s=S656):
    mk(6, 56, t, items, a, R656, s, st="R", p=p)
f656("B", "________ tall is your brother?", [("What", NH("What")), ("How", "How tall로 키를 묻는 말이 되므로"), ("Who", NH("Who")), ("Where", NH("Where")), ("Why", NH("Why"))], 2)
f656("C", "________ long is the river?", [("Which", NH("Which")), ("When", NH("When")), ("Who", NH("Who")), ("How", "How long으로 길이를 묻는 말이 되므로"), ("What", NH("What"))], 4)
f656("D", "________ often do you visit your grandma?", [("How", "How often으로 빈도를 묻는 말이 되므로"), ("Where", NH("Where")), ("Who", NH("Who")), ("What", NH("What")), ("Why", NH("Why"))], 1)
f656("E", "________ far is the nearest station?", [("Who", NH("Who")), ("Why", NH("Why")), ("What", NH("What")), ("Where", NH("Where")), ("How", "How far로 거리를 묻는 말이 되므로")], 5, "원문항에 없던 우리말 해석이 붙었다. 우리말 해석을 빼고 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f656("F", "________ heavy is your bag?", [("Why", NH("Why")), ("What", NH("What")), ("How", "How heavy로 무게를 묻는 말이 되므로"), ("Who", NH("Who")), ("When", NH("When"))], 3)

# 6-57 F: C와 같은 우리말을 새로
F(6, 57, "F", p="그는 어떻게 학교에 가니?", c=["How do he go to school?", "How does he goes to school?", "What does he go to school?", "How does he go to school?", "How is he go to school?"], a=4,
  n=["3인칭 단수 주어 he에는 does를 써야 하므로 오답이다.", "does 뒤에는 동사원형 go를 써야 하므로 오답이다.", "‘어떻게’는 What이 아니라 How로 물으므로 오답이다.", "How + does + 주어 + 동사원형으로 바르게 옮겼으므로 정답이다.", "일반동사 go의 의문문에는 be동사 is를 쓰지 않으므로 오답이다."],
  s="우리말(그녀는 어디에 사니?)과 선택지 네 개가 C와 같았다. 우리말을 새로 쓰고 선택지도 그에 맞게 바꿨다. 정답 위치 ④.")

# 6-58 B: 원문항 발문으로 되돌리면 문법적으로 가능한 진행형 보기를 형태 오류로
F(6, 58, "B", st="R", c=["does Tom runs", "do Tom run", "did Tom ran", "is Tom run", "does Tom run"], a=5,
  n=["does 뒤에는 동사원형 run을 써야 하므로 오답이다.", "3인칭 단수 주어 Tom에는 does를 써야 하므로 오답이다.", "did 뒤에도 동사원형을 써야 하고 현재의 습관을 묻는 문장이므로 오답이다.", "일반동사 run의 의문문에는 be동사 is를 쓰지 않으므로 오답이다.", "does + 주어 + 동사원형 run으로 바르게 고쳤으므로 정답이다."],
  s="발문이 ‘일반동사의 단순현재 긍정 의문문을 유지하여’라고 정답 형식을 알려 주었다. 원문항 발문으로 되돌리고, 조건이 없으면 문법적으로 가능한 진행형 보기(is Tom running)를 형태 오류(is Tom run)로 바꿨다. 정답 위치 ⑤.")

# 6-60 옳은 문장: 원문항처럼 한 틀에서 서로 다른 주어의 do/does 판별
S660 = "원문항은 Where do/does … live? 한 틀에서 서로 다른 주어의 do/does 수 일치를 묻는데, 변형은 한 문장을 다섯 가지로 바꾸거나 오답이 B와 같았고 발문 조건도 붙었다. 원문항 발문으로 되돌리고, 원문항처럼 한 틀에서 서로 다른 주어로 유형마다 새로 썼다."
def f660(t, items, a, s=S660):
    mk(6, 60, t, items, a, R_WH, s, st="R")
f660("C", [("When does the classes start?", "복수 주어 the classes에는 do를 써야 하므로"), ("When do the movie start?", "단수 주어 the movie에는 does를 써야 하므로"), ("When does your lessons start?", "복수 주어 your lessons에는 do를 써야 하므로"),
           ("When does the concert start?", "단수 주어 the concert에 does를 바르게 썼으므로"), ("When do the game start?", "단수 주어 the game에는 does를 써야 하므로")], 4)
f660("D", [("What do the pandas eat?", "복수 주어 the pandas에 do를 바르게 썼으므로"), ("What does the rabbits eat?", "복수 주어 the rabbits에는 do를 써야 하므로"), ("What do your cat eat?", "단수 주어 your cat에는 does를 써야 하므로"),
           ("What does the babies eat?", "복수 주어 the babies에는 do를 써야 하므로"), ("What do the bird eat?", "단수 주어 the bird에는 does를 써야 하므로")], 1)
f660("E", [("How does your sisters go to school?", "복수 주어 your sisters에는 do를 써야 하므로"), ("How do Tom go to school?", "단수 주어 Tom에는 does를 써야 하므로"), ("How do the students go to school?", "복수 주어 the students에 do를 바르게 썼으므로"),
           ("How does the twins go to school?", "복수 주어 the twins에는 do를 써야 하므로"), ("How do your brother go to school?", "단수 주어 your brother에는 does를 써야 하므로")], 3)
f660("F", [("Why does the babies cry?", "복수 주어 the babies에는 do를 써야 하므로"), ("Why does your little brother cry?", "단수 주어 your little brother에 does를 바르게 썼으므로"), ("Why do the girl cry?", "단수 주어 the girl에는 does를 써야 하므로"),
           ("Why does the children cry?", "복수 주어 the children에는 do를 써야 하므로"), ("Why do Mina cry?", "단수 주어 Mina에는 does를 써야 하므로")], 2)


# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, s, r=R_WH, **kw):
    FIX.pop((6, n, t), None)
    mk(6, n, t, items, a, r, s, **kw)
WHQ = "의문사로 시작하는 의문문이므로"
R651 = "의문사(who, what, when, where, why, how)로 시작하는 의문문과 be동사·do/does·조동사로 시작하는 의문문(Yes/No로 답하는 의문문)을 구별한다."
# 6-51 B: 원문항 ②와 똑같은 보기(Who is she?), 정답 위치도 같음 / E: 정답 문장이 D(Can Mina swim?)와 거의 같음
redo(51, "B", [("What color is it?", WHQ), ("How are you?", WHQ), ("Is she at home?", "be동사 Is로 시작하고 의문사가 없으므로"), ("Where are they?", WHQ), ("Who is that boy?", WHQ)], 3,
     "⑤(Who is she?)가 원문항 ②와 똑같은 문장이었고 정답 위치도 원문항과 같았다(①). 겹치는 문장을 바꾸고 정답 위치를 옮겼다.", r=R651)
redo(51, "E", [("What can he do?", WHQ), ("Can they speak English?", "조동사 Can으로 시작하고 의문사가 없으므로"), ("Why can she sing?", WHQ), ("How can you swim?", WHQ), ("Where can we go?", WHQ)], 2,
     "정답 문장(Can you swim?)이 D의 정답(Can Mina swim?)과 거의 같았다. 정답 문장을 바꾸고 정답 위치도 옮겼다.", r=R651)
# 6-52 F: 수정 예시 문장이 원문항 54번 ⑤(How does he go to school?)와 겹침
redo(52, "F", [("What", "‘무엇’을 묻는 말이므로"), ("Who", "‘누구’를 묻는 말이므로"), ("How", "‘어떻게’라는 방법을 묻는 말이므로"), ("Where", "‘어디’를 묻는 말이므로"), ("When", "‘언제’를 묻는 말이므로")], 3,
     "발문이 원문항과 달랐고 정답(Why)과 문장 구조가 E와 거의 같았다. 원문항 발문으로 되돌리고 ‘어떻게’를 묻는 문장으로 바꿔 정답이 How가 되게 했다.",
     r="‘어떻게’라는 방법·수단은 How로, ‘무엇’은 What, ‘누구’는 Who, ‘어디’는 Where, ‘언제’는 When으로 묻는다.", st="R", p="_______ do you make kimchi?\n(너는 김치를 어떻게 만드니?)")
# 6-57 F: 수정 예시의 정답(How does he go to school?)이 원문항 54번 ⑤와 똑같음
redo(57, "F", [("How do she get to work?", "3인칭 단수 주어 she에는 does를 써야 하므로"), ("How does she gets to work?", "does 뒤에는 동사원형 get을 써야 하므로"), ("What does she get to work?", "‘어떻게’는 What이 아니라 How로 물으므로"),
     ("How does she get to work?", "How + does + 주어 + 동사원형으로 바르게 옮겼으므로"), ("How is she get to work?", "일반동사 get의 의문문에 be동사 is를 쓸 수 없으므로")], 4,
     "우리말(그녀는 어디에 사니?)과 선택지 네 개가 C와 같았다. 우리말을 새로 쓰고 선택지도 그에 맞게 바꿨다.", p="그녀는 어떻게 회사에 가니?")
# 6-58 C·D: 고친 문장이 같은 유형 57번의 정답 문장과 같음(Where does she live? / Why do you run?)
S658 = "발문이 ‘일반동사의 단순현재 긍정 의문문을 유지하여’라고 정답 형식을 알려 주었고, 고친 문장(%s)이 같은 유형 57번의 정답 문장과 똑같아 한 문항이 다른 문항의 답을 알려 주었다. 원문항 발문으로 되돌리고 동사를 바꿨다."
redo(58, "C", [("does she works", "does 뒤에는 동사원형 work를 써야 하므로"), ("do she work", "3인칭 단수 주어 she에는 does를 써야 하므로"), ("does she work", "does + 주어 + 동사원형 work로 바르게 고쳤으므로"), ("does she worked", "does 뒤에 과거형을 쓸 수 없으므로"), ("does not she work", "not의 자리가 틀렸고 부정의 뜻으로 바뀌므로")], 3,
     S658 % "Where does she live?", st="R", p="Where <u>does she works</u>?")
redo(58, "D", [("do not you like", "not의 자리가 틀렸고 부정의 뜻으로 바뀌므로"), ("does you like", "주어 you에는 do를 써야 하므로"), ("do you liked", "do 뒤에 과거형을 쓸 수 없으므로"), ("do you like", "do + 주어 + 동사원형 like로 바르게 고쳤으므로"), ("do you likes", "do 뒤에는 동사원형 like를 써야 하므로")], 4,
     S658 % "Why do you run?", st="R", p="Why <u>do you likes</u> winter?")
# 6-59 D: 주어(he)와 정답(3인칭 단수)이 원문항과 같음 → 1인칭 단수 주어로
redo(59, "D", [("2인칭", "I는 말하는 사람 자신이므로"), ("3인칭 복수", "I는 말하는 사람 자신이고 한 명이므로"), ("3인칭 단수", "I는 3인칭이 아니고, 3인칭 단수라면 does를 써야 하므로"), ("1인칭 단수", "I는 말하는 사람 자신 한 명이라 1인칭 단수이고 do를 쓰므로"), ("1인칭 복수", "I는 한 명이므로")], 4,
     "주어(he)와 정답(3인칭 단수)이 원문항과 같았고 E의 정답도 3인칭 단수였다. 주어를 I로 바꿔 정답이 1인칭 단수가 되게 했다. 원문항처럼 빈칸에 밑줄도 되살렸다. 보기는 그대로다.",
     r="일반동사 의문문에서 주어가 3인칭 단수(he, she, it)이면 does를, 그 밖의 주어(I, you, we, they)이면 do를 쓴다. I는 1인칭 단수, we는 1인칭 복수, you는 2인칭, they는 3인칭 복수다.",
     p="<보기> Where do I sit?\n→ 이 문장에서 'do'를 사용한 이유는 주어가 (<u>        </u>)이기 때문입니다.")
# 6-60 B: 정답 문장의 틀린 짝(When does they study?)과 원문항 정답의 틀린 형태(Where does your uncle lives?)
redo(60, "B", [("What do Jane like?", "3인칭 단수 주어 Jane에는 does를 써야 하므로"), ("Why you do run?", "do가 주어 you 앞에 와야 하므로"), ("When do they study?", "복수 주어 they에 do + 동사원형 study를 바르게 썼으므로"),
     ("How does the buses run?", "복수 주어 the buses에는 do를 써야 하므로"), ("Where does your cousin works?", "does 뒤에는 동사원형 work를 써야 하므로")], 3,
     "발문에 ‘단독으로 쓰는 기본형 직접 의문문’ 조건이 붙었고, 정답 문장의 틀린 짝(When does they study?)과 원문항 정답을 틀리게 바꾼 문장(Where does your uncle lives?)이 있었으며 정답 위치도 원문항과 같았다. 원문항 발문으로 되돌리고 두 문장을 바꾸고 정답 위치를 옮겼다.", st="R")
