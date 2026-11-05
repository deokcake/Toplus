# 7급 CH10 실용표현 (91~100) 2차 감수
X(7, 91, r="달 이름은 차례대로 외운다: January, February, March, April, May, June, July, August, September, October, November, December.",
  n=["July는 7월이므로", "September는 9월이므로", "October는 10월이므로", "December는 12월이므로", "August는 8월이므로"],
  st="① 우리말의 달을 영어로 떠올린다: {0} → {a}. → ② 철자나 순서가 가까운 달과 헷갈리지 않는지 확인한다: {1}. → ③ 정답은 {n}.",
  R=("9월", "October는 10월, August는 8월"), B=("5월", "March는 3월, June은 6월"), C=("11월", "October는 10월, September는 9월"), D=("12월", "November는 11월, October는 10월"), E=("2월", "January는 1월, April은 4월"),
  F=("3월", "May는 5월, April은 4월"))
RV(7, 91, "BF", v="수정(내용)", why="정답 유일 확인. 다만 오답 네 개(July, September, October, December)가 모두 원문항 선택지 그대로이고, 정답(May/March)과 헷갈릴 만한 달이 없어 원문항보다 쉽다. B는 정답 위치(②)도 원문항과 같다.", fix="헷갈리기 쉬운 달로 오답을 바꿔")
RV(7, 91, "D", v="수정(내용)", why="정답 ① 유일 확인. 다만 보기 다섯 개(December, September, October, August, July)가 원문항 선택지와 똑같고 순서만 다르다.", fix="12월과 헷갈리기 쉬운 달로 보기를 새로")

X(7, 92, r="대답이 알려 주는 정보(시각, 요일, 날짜, 달)와 시제(is/was)를 보고 질문을 고른다. What time은 시각, What day는 요일, What date는 날짜를 묻는다.",
  n=["시각을 묻는 말이고 현재형이므로", "날짜를 묻는 말이고 현재형이므로", "‘그것은 무엇이니?’라는 뜻이므로", "요일을 과거형으로 물어 It was Saturday.와 맞으므로", "날짜를 묻는 말이라 요일 대답과 맞지 않으므로"],
  st="① 대답이 알려 주는 정보를 본다: {0}. → ② 대답의 시제를 본다: {1}. → ③ 둘 다 맞는 질문은 {a}",
  R=("Saturday → 요일(What day)", "was → 과거"), B=("February → 달(What month)", "was → 과거"), C=("May 5th → 날짜(date)", "is → 현재"), D=("8 o'clock → 시각(What time)", "is → 현재"), E=("Monday → 요일(What day)", "is → 현재"),
  F=("June 3rd → 날짜(What date)", "was → 과거"))

X(7, 93, r="시각, 요일, 날짜, 계절, 날씨, 명암을 나타내는 It은 뜻이 없는 비인칭 주어이다. 앞에 나온 물건이나 동물을 가리키는 It은 ‘그것’이라는 뜻의 대명사이다.",
  n=["요일을 나타내는 비인칭 주어이므로", "‘그것은 네 컴퓨터이다’에서 It은 물건을 가리키는 대명사이므로", "시각을 나타내는 비인칭 주어이므로", "계절을 나타내는 비인칭 주어이므로", "날짜를 나타내는 비인칭 주어이므로"],
  st="① 문장마다 It을 ‘그것’으로 풀어 본다. → ② 시각·요일·날짜·계절·날씨를 말하는 문장은 ‘그것’으로 풀면 어색하다(비인칭 주어). → ③ ‘그것은 {0}’처럼 물건·동물을 가리키는 문장은 {n}.",
  R="네 컴퓨터이다", B="내 새 가방이다", C="귀여운 개다", D="그녀의 필통이다", E="내 낡은 배낭이다", F="Tom의 새 책이다")

X(7, 94, r="며칠인지 물을 때는 What date is it today?를 쓰고(What day는 요일), 날짜의 일은 서수(first, second, third, tenth …)로 말한다.",
  n=["day는 요일을 묻는 말이라 ‘며칠’과 맞지 않으므로", "day는 요일을 묻고 one은 기수이므로", "‘며칠’은 date, 날짜의 일은 서수 first가 알맞으므로", "날짜의 일은 one이 아니라 서수 first로 말하므로", "time은 시각을 묻는 말이므로"],
  st="① 우리말 ‘며칠이야?’는 날짜를 묻는 말이므로 첫 빈칸은 date다(day는 요일, time은 시각). → ② 날짜의 일은 서수로 말한다: {0}. → ③ 정답은 {a}.",
  R="1일 → first", B="10일 → tenth", C="3일 → third", D="2일 → second", E="5일 → fifth", F="12일 → twelfth")
RV(7, 94, "BCDEF", fx=True, why="변형과 수정 예시의 오답에 원문항의 핵심 함정인 day(요일) 대신 year가 들어 있어 쉽게 지워졌다. 수정 예시에서 year를 day로 바꿨다. D·E는 정답 위치도 옮겼다.")

X(7, 95, r="개수를 말할 때는 기수(one, two, three …), 순서를 말할 때는 서수(first, second, third …)를 쓴다. 우리말 뜻이 ‘~ 번째, 첫, ~층, ~등’이면 서수가 필요하다.",
  n=["‘첫 사랑’은 순서를 나타내므로 one이 아니라 first를 써야 하므로", "‘세 대’는 개수라 three가 알맞으므로", "‘넷째’는 순서라 fourth가 알맞으므로", "‘9층’은 순서라 ninth가 알맞으므로", "‘첫 차’는 순서라 first가 알맞으므로"],
  st="① 우리말 해석에서 밑줄 친 수가 개수인지 순서(~ 번째, ~층, 첫)인지 가른다. → ② 개수면 기수(one, two …), 순서면 서수(first, second …)여야 한다. → ③ {0} 정답은 {n}.",
  R="①의 ‘첫 사랑’은 순서인데 기수 one을 썼다.", B="④의 ‘셋째 아들’은 순서인데 기수 three를 썼다.", C="③의 ‘다섯 번째 책’은 순서인데 기수 five를 썼다.", D="②의 ‘6층’은 순서인데 기수 six를 썼다.",
  E="⑤의 ‘두 번째 방문’은 순서인데 기수 two를 썼다.", F="①의 ‘네 번째 주자’는 순서인데 기수 four를 썼다.")
RV(7, 95, "D", fx=True, why="수정 예시의 틀린 낱말(three)이 B와 같았고, ⑤(on the fourth floor)가 층을 서수로 쓰는 꼴을 보여 주어 정답 ②(the three floor)의 단서가 되었다. 틀린 낱말을 six로, ⑤를 다른 문장으로 바꿨다.")

X(7, 96, r="순서를 차례로 늘어놓은 서수 배열이므로 빈칸에도 서수가 들어간다. 기수나 철자가 비슷한 다른 낱말과 헷갈리지 않도록 한다.",
  n=["three는 기수이므로", "thin은 ‘얇은’이라는 다른 낱말이므로", "second 다음 순서의 서수이므로", "thirst는 ‘목마름’이라는 다른 낱말이므로", "thirty는 30이라는 기수이므로"],
  st="① 앞뒤 낱말이 모두 서수이므로 빈칸에도 서수가 온다. → ② 빈칸은 {0} 자리다. → ③ 기수와 철자가 비슷한 낱말을 지우면 {a}.",
  R="second(둘째)와 fourth(넷째) 사이, 곧 셋째", B="eighth(여덟째)와 tenth(열째) 사이, 곧 아홉째", C="seventh(일곱째)와 ninth(아홉째) 사이, 곧 여덟째", D="fifth(다섯째)와 seventh(일곱째) 사이, 곧 여섯째",
  E="third(셋째)와 fifth(다섯째) 사이, 곧 넷째", F="ninth(아홉째)와 eleventh(열한째) 사이, 곧 열째")

X(7, 97, r="어제(yesterday), 지난밤(last night)처럼 지난 일을 말할 때 be동사는 과거형 was/were를 쓴다. I·he·she·it과 단수 주어에는 was, you·we·they와 복수 주어에는 were를 쓴다.",
  n=["am은 현재형이고 I에만 쓰므로", "are는 현재형이므로", "is는 현재형이므로", "어제의 일이고 주어 Yesterday(하루)에 맞는 과거형이므로", "were는 복수 주어에 쓰는 과거형이므로"],
  st="① 때를 나타내는 말을 찾는다: {0}. 지난 일이므로 현재형(am, are, is)을 지운다. → ② 주어를 본다: {1}. → ③ 정답은 {a}.",
  R=("Yesterday", "Yesterday(하루) → was"), B=("Yesterday", "the boys(여럿) → were"), C=("last night", "It → was"), D=("Yesterday", "it → was"), E=("Yesterday", "my friends(여럿) → were"), F=("Yesterday", "Jane(한 사람) → was"))
RV(7, 97, "D", v="수정(내용)", why="정답 ③ 유일 확인. 다만 두 문장(Today is Friday. Yesterday ___ Thursday.)이 원문항(Today is Monday. Yesterday ___ Sunday.)에서 요일만 바꾼 것이고 정답(was)도 같다.", fix="다른 내용의 문장으로")

X(7, 98, r="시각은 It is + 시각으로 말한다. ‘~시 …분 지났다’는 분 + past + 시, ‘~시 …분 전’은 분 + to + 시로 쓰고, 30분은 half, 15분은 a quarter로 말한다.",
  n=["eight half past는 순서가 틀렸으므로", "half eight past는 순서가 틀렸으므로", "It is + half past + 시의 순서로 바르게 썼으므로", "It is로 시작하지 않아 어순이 틀렸으므로", "past half is eight는 순서가 틀렸으므로"],
  st="① 시각을 ‘분 + past/to + 시’로 바꾼다: {0} → {1}. → ② It is 뒤에 이 순서 그대로 쓴다. → ③ 정답은 {n}.",
  R=("8시 30분", "half past eight(8시에서 30분 지남)"), B=("6시 45분", "a quarter to seven(7시 15분 전)"), C=("7시 15분", "a quarter past seven(7시에서 15분 지남)"), D=("9시 10분", "ten past nine(9시에서 10분 지남)"),
  E=("4시 50분", "ten to five(5시 10분 전)"), F=("11시 5분", "five past eleven(11시에서 5분 지남)"))

X(7, 99, r="서수는 대부분 기수 + th로 만들지만, first, second, third는 따로 외우고 fifth(five), eighth(eight), ninth(nine), twelfth(twelve), twentieth(twenty)처럼 철자가 바뀌는 것에 주의한다.",
  n=["five의 서수 fifth를 바르게 썼으므로", "nine의 서수 ninth를 바르게 썼으므로", "ten의 서수 tenth를 바르게 썼으므로", "eight의 서수 eighth를 바르게 썼으므로", "twelve의 서수는 ve를 f로 바꾼 twelfth이므로"],
  st="① 밑줄 친 서수마다 바탕이 되는 기수를 떠올린다. → ② 그냥 th만 붙이면 안 되는 낱말(third, fifth, eighth, ninth, twelfth, twentieth 등)을 따로 확인한다. → ③ {0} 정답은 {n}.",
  R="twelve → twelfth(ve를 f로 바꾼다).", B="three → third.", C="nine → ninth(e를 뺀다).", D="five → fifth(ve를 f로 바꾼다).", E="forty → fortieth(u가 없다).", F="twenty → twentieth(y를 ie로 바꾼다).")
RV(7, 99, "F", fx=True, why="정답 위치(⑤)가 원문항·E와 같았다. 수정 예시에서 보기 순서를 바꿔 정답을 ①로 옮겼다.")

X(7, 100, r="What date는 날짜, What day는 요일을 묻는다. 날짜의 일은 서수로 말하고, 요일은 요일 이름으로 대답한다. 날짜·요일을 말할 때는 It을 주어로 쓴다.",
  pre=["설명별 판정: 가 O. What date는 날짜를 묻는다. 나 O. What day는 요일을 묻는다. 다 O. 날짜의 일은 서수로 말한다. 라 X. 요일은 숫자가 아니라 요일 이름(Monday 등)으로 대답한다."],
  k="옳은 설명은 가, 나, 다이다.", n=["다도 옳은 설명이므로", "라가 틀린 설명이므로", "라가 틀린 설명이므로", "라가 틀린 설명이므로", "가, 나, 다가 모두 옳은 설명이므로"],
  st="① 설명을 하나씩 실제로 묻고 답하는 말에 대어 본다. → ② {0} → ③ 옳은 것을 모두 모으면 {a}이다.",
  R="가 O, 나 O, 다 O, 라 X(요일은 요일 이름으로 대답한다).", B="가 X(What day에는 요일로 대답한다), 나 O, 다 O, 라 O.", C="가 X(What date는 날짜를 묻는다), 나 O, 다 O, 라 X(요일 이름은 늘 대문자로 시작한다).",
  D="가 O, 나 X(2nd는 second로 읽는다), 다 X(What time은 시각을 묻는다), 라 O.", E="가 O, 나 X(first, second, third는 서수다), 다 O, 라 O.", F="가 O, 나 O, 다 X(December는 달 이름이다), 라 O.")
RV(7, 100, "CD", v="수정(내용)", why="정답 유일 확인. 다만 설명이 ‘Monday는 요일이다’, ‘September는 월 이름이다’ 같은 낱말 뜻풀이여서 발문(날짜와 요일을 묻고 답하는 방법)과 맞지 않고 원문항보다 쉽다. C와 D의 정답 조합(가, 나, 다)과 위치(③)가 서로 같고 원문항의 정답 조합과도 같다. [보기]와 따옴표 표기도 원문항과 다르다.", fix="발문에 맞는 설명으로 새로 쓰고 정답 조합을 바꿔")
RV(7, 100, "EF", fx=True, why="정답 위치가 다섯 유형 모두 ③이었다. 수정 예시에서 E와 F의 보기 순서를 바꿔 정답을 ①과 ⑤로 옮겼다.")
