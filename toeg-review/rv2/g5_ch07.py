# 5급 CH7 숫자 표현과 비인칭주어 it (61~70) 2차 감수
X(5, 61, r="개수는 기수(four)로, 몇 번째 생일·몇 층 같은 순서는 서수(twelfth, third)로 나타낸다.",
  n=["개수는 기수 four, 생일과 층은 서수 twelfth, third로 알맞으므로", "층은 three가 아니라 서수 third로 나타내므로", "몇 번째 생일은 twelve가 아니라 서수 twelfth로 나타내므로", "개수는 fourth가 아니라 기수 four로 나타내고 나머지도 서수여야 하므로", "개수는 fourth가 아니라 기수 four로 나타내므로"],
  st="① 첫 문장은 개수를 말한다 → 기수 {0}. → ② 둘째 문장은 몇 번째 생일인지 말한다 → 서수 {1}. → ③ 셋째 문장은 몇 층인지 말한다 → 서수 {2}. 정답은 {n}.",
  R=("four", "twelfth", "third"), B=("seven", "fifteenth", "second"), C=("eight", "tenth", "fifth"), D=("three", "ninth", "sixth"), E=("five", "eleventh", "fourth"), F=("two", "thirteenth", "eighth"))
RV(5, 61, "BCDEF", fx=True, why="원문항은 세 문장 앞에 ‘·’ 표시가 있는데 변형에는 없다. 수정 예시에서 원문항처럼 ‘·’를 붙였다.")

X(5, 62, r="날짜의 ‘일’은 서수로 읽는다. 30일은 thirtieth다. thirty(기수), third(3일), thirteenth(13일)와 구별한다.",
  n=["third는 3일이므로", "thirty는 기수라 날짜를 읽을 때 쓰지 않으므로", "30일을 서수 thirtieth로 바르게 읽었으므로", "thirteenth는 13일이므로", "Thirteen은 13을 뜻하는 기수이므로"],
  st="① 날짜의 ‘일’을 확인한다: {0}. → ② 날짜는 서수로 읽으므로 {1}. → ③ 기수로 읽은 것과 비슷하게 생긴 다른 날짜를 지운다. 정답은 {n}.",
  R=("30일", "thirtieth"), B=("21일", "twenty-first"), C=("3일", "third"), D=("12일", "twelfth"), E=("2일", "second"), F=("15일", "fifteenth"))
RV(5, 62, "CDEF", fx=True, why="수정 예시의 오답에 영어에 없는 형태(threeth, twelveth, twoth, fiveteenth)가 있었다. 원문항의 오답은 모두 실제 낱말이므로 기수(thirty, twenty, fifty)나 다른 날짜(twenty-second)로 바꿨다.")

X(5, 63, r="연도는 두 자리씩 끊어 읽는다(1550 fifteen fifty). 뒤 두 자리가 00이면 hundred, 2000년대는 two thousand ~로도 읽는다.",
  n=["13 / 00으로 끊어 thirteen hundred로 바르게 읽었으므로", "15 / 50이므로 fifteen fifty로 읽어야 하는데 순서가 바뀌었으므로", "19 / 99로 끊어 바르게 읽었으므로", "20 / 25로 끊어 바르게 읽었으므로", "23 / 00으로 끊어 twenty-three hundred로 바르게 읽었으므로"],
  st="① 연도를 앞 두 자리와 뒤 두 자리로 끊는다. → ② 각 부분을 수로 읽어 보기와 견준다. 뒤가 05처럼 0으로 시작하면 oh five로 읽는다. → ③ {0} 정답은 {n}.",
  R="1550은 fifteen / fifty인데 fifty fifteen으로 거꾸로 읽었다.", B="1705는 seventeen oh five인데 fifty(50)로 읽었다.", C="1905는 nineteen oh five인데 fifty(50)로 읽었다.", D="2008은 two thousand eight인데 eighty(80)로 읽었다.",
  E="1977은 nineteen seventy-seven이다. 연도는 서수(seventy-seventh)로 읽지 않는다.", F="1608은 sixteen oh eight인데 eighty(80)로 읽었다.")
RV(5, 63, "C", v="수정(내용)", why="정답 ② 유일 확인. 다만 보기 두 개가 원문항과 겹친다: ⑤ 1999 - nineteen ninety-nine은 원문항 ③과 똑같고, ① 1550 - fifteen fifty는 원문항 정답의 연도를 바르게 읽은 것이다. 정답 위치도 원문항과 같다(②).", fix="①·⑤를 다른 연도로, 정답 위치 변경")
RV(5, 63, "E", fx=True, why="수정 예시 정답의 연도(1999)가 원문항 ③(1999 - nineteen ninety-nine)과 같아 다른 연도(1977)로 바꿨다.")

X(5, 64, r="시각 읽기: 30분은 half past + 지난 시, 15분은 a quarter after(past) + 지난 시, 45분은 a quarter to + 다가올 시. 숫자 그대로 읽어도 된다(8:05 eight oh five).",
  n=["시와 분을 숫자대로 바르게 읽었으므로", "11시 30분은 half past eleven인데 twelve로 읽었으므로", "시와 분을 숫자대로 바르게 읽었으므로", "2시 30분을 half past two로 바르게 읽었으므로", "시와 분을 숫자대로 바르게 읽었으므로"],
  st="① past(after)는 ‘지난 시’, to는 ‘다가올 시’를 뒤에 쓴다는 점을 떠올린다. → ② 보기마다 시각과 읽은 말의 ‘시’를 견준다. → ③ {0} 정답은 {n}.",
  R="11:30은 11시에서 30분 지난 것이므로 half past eleven이다.", B="2:45는 3시 15분 전이므로 a quarter to three다.", C="8:15는 8시에서 15분 지난 것이므로 a quarter after eight다.",
  D="3:45는 4시 15분 전이므로 a quarter to four다.", E="7:30은 7시에서 30분 지난 것이므로 half past seven이다.", F="9:15는 9시에서 15분 지난 것이므로 a quarter after nine이다.")

X(5, 65, r="의문사구가 묻는 것: How much 값, How long 걸리는 시간·길이, How far 거리, How heavy 무게. 날씨·값·시간·거리를 말할 때 주어는 비인칭 it이다.",
  n=["날씨를 묻고 날씨로 답했으므로", "값을 묻고 값으로 답했으므로", "걸리는 시간을 묻는데 값으로 답했으므로", "거리를 묻고 거리로 답했으므로", "무게를 묻고 무게로 답했으므로"],
  st="① 질문마다 의문사구가 무엇을 묻는지 적는다(값, 시간, 거리, 날짜, 요일 …). → ② 대답이 같은 종류의 정보인지 견준다. → ③ {0} 정답은 {n}.",
  R="③은 How long(걸리는 시간)에 10 dollars(값)로 답했다.", B="⑤는 How far(거리)에 값으로 답했다.", C="④는 What time(시각)에 날씨로 답했다.", D="②는 How much(값)에 걸리는 시간으로 답했다.",
  E="①은 How heavy(무게)에 길이로 답했다.", F="③은 the date(날짜)에 요일로 답했다.")

X(5, 66, r="15분은 a quarter, 30분은 half로 나타낸다. after/past는 ‘~ 지난’, to는 ‘~ 전’이다.",
  n=["fifty는 50이라 15분이 되지 않으므로", "half는 30분이고 앞에 a를 쓰지 않으므로", "a quarter after eight이 8시 15분이므로", "past는 after와 같은 뜻의 말이라 a 뒤에 올 수 없으므로", "clock은 a ~ after eight 자리에 올 수 없으므로"],
  st="① 우리말 시각을 본다: {0}. → ② 주어진 틀에 맞춰 본다: {1}. → ③ 정답은 {a}.",
  R=("8시 15분", "8시에서 15분 지남 → a quarter after eight"), B=("9시 30분", "9시에서 30분 지남 → half past nine"), C=("4시 30분", "4시에서 30분 지남 → half past four"),
  D=("9시 45분", "10시 15분 전 → a quarter to ten"), E=("7시 15분", "7시에서 15분 지남 → a quarter after seven"), F=("2시 50분", "3시 10분 전 → ten to three"))

X(5, 67, r="‘~ 번째’는 서수로 나타낸다. 서수는 대개 기수 + th이지만 first, second, third는 따로 외운다.",
  n=["기수 three로는 ‘세 번째’를 나타낼 수 없으므로", "thirth라는 말은 없으므로", "‘세 번째’를 서수 third로 바르게 나타냈으므로", "’s를 붙여도 서수가 되지 않으므로", "threed라는 말은 없으므로"],
  st="① 우리말에서 ‘~ 번째’를 찾는다: {0}. 서수가 필요하다. → ② 그 서수의 바른 철자는 {1}. → ③ 기수를 그대로 쓴 것과 철자를 잘못 만든 것을 지운다. 정답은 {n}.",
  R=("세 번째", "third"), B=("네 번째", "fourth(u가 들어간다)"), C=("두 번째", "second"), D=("첫 번째", "first"), E=("다섯 번째", "fifth(ve를 f로 바꾼다)"), F=("아홉 번째", "ninth(e를 뺀다)"))
RV(5, 67, "C", fx=True, why="수정 예시의 우리말(‘그는 두 번째 층에 산다’)이 어색했다(보통 ‘2층에 산다’). ‘그는 두 번째 문제를 풀고 있다’로 바꿨다.")

X(5, 68, r="요일은 What day is it?, 날짜는 What date is it?(What's the date?), 시각은 What time is it?으로 묻는다.",
  n=["요일로 답한 첫 질문에 date를 쓸 수 없으므로", "요일로 답한 첫 질문에 time을 쓸 수 없으므로", "날짜로 답한 둘째 질문에 time을 쓸 수 없으므로", "요일은 day, 날짜는 date로 물으므로", "첫 질문과 둘째 질문 모두 대답과 맞지 않으므로"],
  st="① 빈칸은 질문에 있으므로 대답을 먼저 본다. → ② 첫 대답은 {0}, 둘째 대답은 {1}. → ③ 정답은 {a}.",
  R=("Friday(요일) → day", "December 24th(날짜) → date"), B=("a quarter past five(시각) → What time", "windy(날씨) → How"), C=("8:30(시각) → time", "Monday(요일) → day"),
  D=("June 3rd(날짜) → date", "Tuesday(요일) → day"), E=("10 dollars(값) → much", "Ten minutes(걸리는 시간) → long"), F=("sunny(날씨) → weather", "Sunday(요일) → day"))

X(5, 69, r="큰 수는 쉼표에서 끊어 읽는다. 쉼표 앞은 thousand(천) 단위이고, 30은 thirty, 13은 thirteen이다. thousand, hundred에는 -s를 붙이지 않는다.",
  n=["34는 thirty-four, 쉼표 자리는 thousand이므로", "thirteen은 13이고 쉼표 자리는 hundred가 아니므로", "쉼표 자리는 thousand이고 hundreds처럼 -s도 붙이지 않으므로", "thirteen은 13이므로", "three-four라고 읽지 않으므로"],
  st="① 쉼표에서 끊는다: {0}. → ② 쉼표 앞의 수를 읽는다: {1}. → ③ 쉼표 자리는 천 단위이므로 thousand다. 정답은 {a}.",
  R=("34 / 200", "34는 thirty-four"), B=("52 / 600", "52는 fifty-two"), C=("21 / 500", "21은 twenty-one"), D=("48 / 300", "48은 forty-eight"), E=("62 / 100", "62는 sixty-two"), F=("15 / 400", "15는 fifteen"))
RV(5, 69, "B", fx=True, why="변형의 보기에 ‘(A) fifty — (B) thousand’처럼 원문항에 없는 (A)·(B) 표지가 붙었고 빈칸 모양((A)________)도 원문항(( A ))과 다르다. 수정 예시에서 원문항 표기로 맞췄다.")

X(5, 70, r="금액의 단위는 수에 맞춘다: 1이면 단수(one dollar, one cent), 2 이상이면 복수(five dollars, five cents).",
  n=["one dollars만 고치면 five cent가 틀린 채로 남으므로", "five cent만 고치면 one dollars가 틀린 채로 남으므로", "one dollar, five cents로 두 군데를 모두 바르게 고쳤으므로", "a chocolate은 초콜릿 한 개를 뜻하는 옳은 표현이고 밑줄 친 부분도 아니므로", "and를 빼도 five cent는 틀린 표현이므로"],
  st="① 밑줄 친 부분을 수와 단위로 나눈다: {0}. → ② 수가 1이면 단수, 2 이상이면 복수인지 하나씩 본다. {1} → ③ 발문이 ‘모두’ 찾으라고 했으므로 틀린 곳을 빠짐없이 고친 것을 고른다. 정답은 {n}.",
  R=("one + dollars / five + cent", "one dollars → one dollar, five cent → five cents."), B=("two + dollar / one + cents", "two dollar → two dollars, one cents → one cent."),
  C=("four + dollar / thirty + cent", "four dollar → four dollars, thirty cent → thirty cents."), D=("one + dollars / fifty + cent", "one dollars → one dollar, fifty cent → fifty cents."),
  E=("five + dollar / twenty + cent", "five dollar → five dollars, twenty cent → twenty cents."), F=("one + dollars / one + cents", "one dollars → one dollar, one cents → one cent."))
RV(5, 70, "B", v="수정(내용)", why="정답 ① 유일 확인. 다만 제시문이 한 문장(The notebook is ~.)뿐이라 원문항(네 문장 지문)의 절반이 안 되고, 오답(‘수에 관계없이 항상 단수로 쓴다’, ‘복수형을 전혀 쓰지 않는다’)이 C~F에서 지적한 것과 같은 뻔한 설명이다. 밑줄 친 표현도 C와 똑같다(two dollar and one cents). 발문도 원문항과 다르다.", fix="짧은 지문에 넣고 오답을 한쪽만 고치는 설명으로")
RV(5, 70, "C", fx=True, why="수정 예시의 밑줄 친 금액(two dollar and one cents)이 B와 똑같아 다른 금액(four dollar and thirty cent)으로 바꿨다.")
