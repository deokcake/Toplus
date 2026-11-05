# 5급 CH7 수·서수·날짜·시각·금액 (61~70) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def slotnote(ch, good, why, labs=("첫째", "둘째", "셋째"), sep=" - "):
    xs = [x.strip() for x in ch.split(sep)]; gs = [x.strip() for x in good.split(sep)]
    if xs == gs: return "모든 빈칸에 알맞은 말을 골랐으므로"
    bits = [f"{labs[i]} 빈칸 {x}: {w}" for i, (x, g, w) in enumerate(zip(xs, gs, why)) if x != g]
    return ". ".join(bits) + ". 따라서"

# 5-65, 5-68 원문항 발문
F(5, 68, "B", st="R", s="발문이 ‘의문 표현’으로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 5-61 기수·서수 짝: B 원문항 발문, C~F는 그 문장의 수로 기수/서수만 바꾼 오답
R561 = "개수는 기수(one, two, three …)로, 순서·몇 번째·층·생일은 서수(first, second, third, fourth … twelfth)로 나타낸다."
F(5, 61, "B", st="R", s="발문에 ‘기수와 서수’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
S561 = "오답 네 개가 원문항의 수(four, twelve, three 등)를 그대로 가져와 문장과 맞지 않아, 새 수가 들어간 선택지 하나만 남아 정답이 드러났다. 그 문장의 수로 기수/서수만 바꾼 오답으로 새로 썼다."
def f561(t, p, good, chs, why, a, s=S561):
    items = [(ch, slotnote(ch, good, why)) for ch in chs]
    mk(5, 61, t, items, a, R561, s, p=p, okdup=True)
f561("C", "A spider has _______ legs.\nIt is my _______ birthday.\nHe lives on the _______ floor.", "eight - tenth - fifth",
     ["eighth - tenth - fifth", "eight - ten - fifth", "eight - tenth - five", "eight - tenth - fifth", "eighth - ten - five"],
     ["다리의 개수는 기수 eight로 나타낸다", "몇 번째 생일은 서수 tenth로 나타낸다", "층은 서수 fifth로 나타낸다"], 4)
f561("D", "A triangle has _______ sides.\nThis is my cousin's _______ birthday party.\nWe live on the _______ floor.", "three - ninth - sixth",
     ["three - ninth - sixth", "third - ninth - sixth", "three - nine - sixth", "three - ninth - six", "third - nine - six"],
     ["변의 개수는 기수 three로 나타낸다", "몇 번째 생일은 서수 ninth로 나타낸다", "층은 서수 sixth로 나타낸다"], 1)
f561("E", "A hand has _______ fingers.\nIt is Tom's _______ birthday.\nShe lives on the _______ floor.", "five - eleventh - fourth",
     ["fifth - eleventh - fourth", "five - eleven - fourth", "five - eleventh - four", "fifth - eleven - four", "five - eleventh - fourth"],
     ["손가락의 개수는 기수 five로 나타낸다", "몇 번째 생일은 서수 eleventh로 나타낸다", "층은 서수 fourth로 나타낸다"], 5)
f561("F", "A bicycle has _______ wheels.\nToday is Jane's _______ birthday.\nThey live on the _______ floor.", "two - thirteenth - eighth",
     ["second - thirteenth - eighth", "two - thirteen - eighth", "two - thirteenth - eighth", "two - thirteenth - eight", "second - thirteen - eight"],
     ["바퀴의 개수는 기수 two로 나타낸다", "몇 번째 생일은 서수 thirteenth로 나타낸다", "층은 서수 eighth로 나타낸다"], 3)

# 5-62 날짜 읽기: 원문항 발문, 날짜 읽기 오류 오답
R562 = "날짜의 ‘일’은 서수로 읽는다(3일 third, 12일 twelfth, 21일 twenty-first, 30일 thirtieth). 기수로 읽거나 비슷한 수(13일 thirteenth, 20일 twentieth)와 헷갈리지 않도록 한다."
S562 = "발문이 ‘날짜의 일을 서수로 읽는 방식을 사용한다’고 정답을 알려 주었고, 오답이 물음표·are·birthdays처럼 날짜와 관계없는 오류였다. 원문항 발문으로 되돌리고, 원문항처럼 기수·비슷한 서수 같은 날짜 읽기 오류로 오답을 바꿨다."
def f562(t, ko, items, a, s=S562):
    mk(5, 62, t, items, a, R562, s, st="R", p=ko)
f562("B", "3월 21일은 그녀의 생일이다.", [("March twenty-one is her birthday.", "날짜의 일은 기수 twenty-one이 아니라 서수로 읽으므로"), ("March twenty-first is her birthday.", "21일을 서수 twenty-first로 바르게 읽었으므로"), ("March twelfth is her birthday.", "twelfth는 12일이므로"),
     ("March twenty-third is her birthday.", "twenty-third는 23일이므로"), ("March first is her birthday.", "first는 1일이므로")], 2)
f562("C", "그녀의 생일은 5월 3일이다.", [("Her birthday is May three.", "날짜의 일은 기수 three가 아니라 서수로 읽으므로"), ("Her birthday is May thirteenth.", "thirteenth는 13일이므로"), ("Her birthday is May thirtieth.", "thirtieth는 30일이므로"),
     ("Her birthday is May third.", "3일을 서수 third로 바르게 읽었으므로"), ("Her birthday is May thirty.", "thirty는 30을 뜻하는 기수이므로")], 4)
f562("D", "내 생일은 8월 12일이다.", [("My birthday is August twelfth.", "12일을 서수 twelfth로 바르게 읽었으므로"), ("My birthday is August twelve.", "날짜의 일은 기수 twelve가 아니라 서수로 읽으므로"), ("My birthday is August twentieth.", "twentieth는 20일이므로"),
     ("My birthday is August twenty.", "twenty는 20을 뜻하는 기수이므로"), ("My birthday is August second.", "second는 2일이므로")], 1, S562 + " 날짜도 B(21일)와 겹치지 않게 12일로 바꿨다.")
f562("E", "Tom의 생일은 1월 2일이다.", [("Tom's birthday is January two.", "날짜의 일은 기수 two가 아니라 서수로 읽으므로"), ("Tom's birthday is January twelfth.", "twelfth는 12일이므로"), ("Tom's birthday is January twentieth.", "twentieth는 20일이므로"),
     ("Tom's birthday is January twenty-second.", "twenty-second는 22일이므로"), ("Tom's birthday is January second.", "2일을 서수 second로 바르게 읽었으므로")], 5)
f562("F", "Jane의 생일은 12월 15일이다.", [("Jane's birthday is December fifteen.", "날짜의 일은 기수 fifteen이 아니라 서수로 읽으므로"), ("Jane's birthday is December fiftieth.", "fiftieth는 50번째라 날짜가 될 수 없으므로"), ("Jane's birthday is December fifteenth.", "15일을 서수 fifteenth로 바르게 읽었으므로"),
     ("Jane's birthday is December fifth.", "fifth는 5일이므로"), ("Jane's birthday is December fifty.", "fifty는 50을 뜻하는 기수이므로")], 3)

# 5-63 연도 읽기: 같은 연도를 두 번 쓰지 않기
R563 = "연도는 보통 두 자리씩 끊어 읽는다(1980 nineteen eighty, 2021 twenty twenty-one). 2000~2009년은 two thousand + 나머지로 읽고, 1608처럼 가운데가 0이면 sixteen oh eight로 읽는다."
S563 = "같은 연도를 옳게 읽은 것과 틀리게 읽은 것이 함께 있어 대비 단서가 되었다. 같은 연도가 두 번 나오지 않게 유형마다 새로 썼다."
TWO = "두 자리씩 끊어 바르게 읽었으므로"; TH = "two thousand + 나머지로 바르게 읽었으므로"
def f563(t, items, a, s=S563):
    FIX.pop((5, 63, t), None)
    mk(5, 63, t, items, a, R563, s)
f563("D", [("2008 - twenty eighty", "2008은 two thousand eight(또는 twenty oh eight)로 읽어야 하는데 eighty(80)로 읽었으므로"), ("2021 - twenty twenty-one", TWO), ("1980 - nineteen eighty", TWO), ("2016 - two thousand sixteen", TH), ("2003 - two thousand three", TH)], 1)
f563("E", [("2012 - two thousand twelve", TH), ("1977 - nineteen seventy-seventh", "연도는 서수가 아니라 기수로 읽어 seventy-seven이라고 해야 하므로"), ("1840 - eighteen forty", TWO), ("1987 - nineteen eighty-seven", TWO), ("2000 - two thousand", "2000년을 two thousand로 바르게 읽었으므로")], 2, S563 + " 정답의 연도도 원문항 ③(1999)과 겹치지 않게 바꿨다.")
f563("F", [("2020 - twenty twenty", TWO), ("1995 - nineteen ninety-five", TWO), ("2015 - two thousand fifteen", TH), ("1608 - sixteen eighty", "가운데가 0이면 oh를 넣어 sixteen oh eight로 읽어야 하는데 eighty(80)로 읽었으므로"), ("2007 - two thousand seven", TH)], 4)

# 5-64 시각 읽기: 같은 시각을 두 번 쓰지 않기
R564 = "시각은 숫자대로 읽거나(2:05 two oh five), 30분은 half past, 15분은 a quarter after(past), 45분은 다음 시각을 기준으로 a quarter to로 읽는다. 정각은 o'clock이다."
S564 = "같은 시각을 옳게 읽은 것과 틀리게 읽은 것이 함께 있어 대비 단서가 되었다. 같은 시각이 두 번 나오지 않게 유형마다 새로 썼다."
Q_A = "15분을 a quarter after + 그 시각으로 바르게 읽었으므로"; Q_T = "45분을 a quarter to + 다음 시각으로 바르게 읽었으므로"; HP = "30분을 half past + 그 시각으로 바르게 읽었으므로"; OC = "정각을 o'clock으로 바르게 읽었으므로"; NUM = "시와 분을 숫자대로 바르게 읽었으므로"
def f564(t, items, a, s=S564):
    mk(5, 64, t, items, a, R564, s)
f564("C", [("9:30 - half past nine", HP), ("5:00 - five o'clock", OC), ("6:15 - a quarter after six", Q_A), ("2:45 - a quarter to three", Q_T), ("8:15 - a quarter after nine", "a quarter after 뒤에는 지나간 시각 eight를 써야 하므로")], 5)
f564("D", [("9:00 - nine o'clock", OC), ("3:45 - a quarter to three", "a quarter to 뒤에는 다가올 시각 four를 써야 하므로"), ("10:30 - half past ten", HP), ("12:15 - a quarter after twelve", Q_A), ("7:45 - a quarter to eight", Q_T)], 2)
f564("E", [("4:00 - four o'clock", OC), ("11:45 - a quarter to twelve", Q_T), ("6:15 - a quarter after six", Q_A), ("7:30 - half past six", "half past 뒤에는 지나간 시각 seven을 써야 하므로"), ("2:05 - two oh five", NUM)], 4)
f564("F", [("9:15 - a quarter after ten", "a quarter after 뒤에는 지나간 시각 nine을 써야 하므로"), ("8:30 - half past eight", HP), ("4:45 - a quarter to five", Q_T), ("3:00 - three o'clock", OC), ("10:20 - ten twenty", NUM)], 1)

# 5-65 어색한 대화: 원문항 발문, 유형마다 새 대화(같은 질문 반복 없이)
R565 = "How much는 값, How long은 걸리는 시간이나 길이, How far는 거리, How heavy는 무게, What time은 시각, What day는 요일, What's the date는 날짜를 묻는다."
S565 = "대화 오답 네 개가 C와 똑같았고, 같은 질문이 옳은 대답과 틀린 대답으로 두 번 나와 대비 단서가 되었으며 발문이 길게 바뀌었다. 원문항 발문으로 되돌리고 같은 질문이 반복되지 않게 유형마다 대화를 새로 썼다."
def f565(t, items, a, s=S565):
    mk(5, 65, t, items, a, R565, s, st="R")
F(5, 65, "B", st="R", s="발문이 ‘질문이 요구하는 정보와 대답이 직접 제공하는 정보가 서로 맞지 않는 대화’로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f565("C", [("A: How old is your sister? B: She is ten years old.", "나이를 묻는 질문에 나이로 알맞게 답했으므로"), ("A: What's the date today? B: It's July 7th.", "날짜를 묻는 질문에 날짜로 알맞게 답했으므로"), ("A: How tall is he? B: He is about 170 centimeters tall.", "키를 묻는 질문에 키로 알맞게 답했으므로"),
           ("A: What time does the movie start? B: It's rainy today.", "영화 시작 시각을 묻는데 날씨로 답했으므로"), ("A: How many pencils do you have? B: I have three.", "개수를 묻는 질문에 개수로 알맞게 답했으므로")], 4)
f565("D", [("A: When is your birthday? B: It's on May 5th.", "생일이 언제인지 묻는 질문에 날짜로 알맞게 답했으므로"), ("A: How much is this cap? B: It takes ten minutes.", "모자의 값을 묻는데 걸리는 시간으로 답했으므로"), ("A: What day is it today? B: It's Wednesday.", "요일을 묻는 질문에 요일로 알맞게 답했으므로"),
           ("A: How's the weather? B: It's snowing.", "날씨를 묻는 질문에 날씨로 알맞게 답했으므로"), ("A: How long is the bridge? B: It's about 300 meters long.", "다리의 길이를 묻는 질문에 길이로 알맞게 답했으므로")], 2)
f565("E", [("A: How heavy is your bag? B: It's about two meters long.", "가방의 무게를 묻는데 길이로 답했으므로"), ("A: What time is it now? B: It's half past four.", "시각을 묻는 질문에 시각으로 알맞게 답했으므로"), ("A: How far is the park? B: It's about one kilometer.", "거리를 묻는 질문에 거리로 알맞게 답했으므로"),
           ("A: What day of the week is it? B: It's Monday.", "요일을 묻는 질문에 요일로 알맞게 답했으므로"), ("A: How long does it take to get there? B: It takes twenty minutes.", "걸리는 시간을 묻는 질문에 시간으로 알맞게 답했으므로")], 1)
f565("F", [("A: How many students are there? B: There are twenty.", "학생 수를 묻는 질문에 수로 알맞게 답했으므로"), ("A: What's the weather like? B: It's windy.", "날씨를 묻는 질문에 날씨로 알맞게 답했으므로"), ("A: What's the date today? B: It's Friday.", "날짜를 묻는데 요일로 답했으므로"),
           ("A: How much are the shoes? B: They are 30 dollars.", "신발 값을 묻는 질문에 값으로 알맞게 답했으므로"), ("A: How old are you? B: I'm twelve.", "나이를 묻는 질문에 나이로 알맞게 답했으므로")], 3)

# 5-66 시각 표현 빈칸: 원문항처럼 우리말 뜻 제시, C·F는 시각을 새로
R566 = "30분은 half past + 그 시각, 15분은 a quarter after(past) + 그 시각, 45분·50분처럼 다음 시각이 가까우면 a quarter/ten to + 다음 시각으로 나타낸다."
S566 = "발문이 원문항과 달랐고 괄호로 시각을 주었다. 원문항처럼 우리말 시각을 발문에 제시하는 형식으로 바꿨다."
def f566(t, ko, p, items, a, s=S566 + " 보기와 정답은 그대로다."):
    mk(5, 66, t, items, a, R566, s, st=f"다음 빈칸에 '{ko}'이라는 의미가 되도록 알맞은 단어를 고르세요.", p=p)
f566("B", "9시 30분", "It's ________ past nine.", [("a quarter", "a quarter past nine은 9시 15분이므로"), ("thirty to", "thirty to nine은 8시 30분이므로"), ("ten", "ten past nine은 9시 10분이므로"), ("quarter", "quarter는 15분이고 앞에 a가 필요하므로"), ("half", "half past nine은 9시 30분이므로")], 5)
f566("C", "4시 30분", "It's half ________ four.", [("at", "at은 시각 앞에 쓰는 전치사라 half 뒤에 올 수 없으므로"), ("past", "half past four는 4시 30분이므로"), ("to", "half to four라는 표현은 쓰지 않으므로"), ("quarter", "half 뒤에 quarter를 쓸 수 없으므로"), ("o'clock", "o'clock은 정각에만 쓰므로")], 2,
     "제시문과 정답이 B와 똑같았다(9:30, half). 원문항처럼 우리말 시각을 발문에 제시하고, 시각(4시 30분)과 빈칸 위치를 바꿔 정답이 past가 되게 했다.")
f566("D", "9시 45분", "It's a quarter ________ ten.", [("five", "a quarter five라는 표현은 없으므로"), ("quarter", "a quarter 뒤에 quarter를 또 쓸 수 없으므로"), ("after", "a quarter after ten은 10시 15분이므로"), ("to", "a quarter to ten은 10시 15분 전인 9시 45분이므로"), ("half", "a quarter 뒤에 half를 쓸 수 없으므로")], 4)
f566("E", "7시 15분", "It's a quarter ________ seven.", [("after", "a quarter after seven은 7시 15분이므로"), ("to", "a quarter to seven은 6시 45분이므로"), ("half", "a quarter 뒤에 half를 쓸 수 없으므로"), ("quarter", "a quarter 뒤에 quarter를 또 쓸 수 없으므로"), ("five", "a quarter five라는 표현은 없으므로")], 1)
f566("F", "2시 50분", "It's ten ________ three.", [("past", "ten past three는 3시 10분이므로"), ("after", "ten after three는 3시 10분이므로"), ("to", "ten to three는 3시 10분 전인 2시 50분이므로"), ("half", "ten 뒤에 half를 쓸 수 없으므로"), ("quarter", "ten 뒤에 quarter를 쓸 수 없으므로")], 3,
     "‘It's ____ o'clock. (5:00)’은 숫자만 넣으면 되어 원문항보다 지나치게 쉬웠다. 원문항처럼 우리말 시각을 발문에 제시하고, past/to를 판단해야 하는 시각(2시 50분)으로 바꿨다.")

# 5-67 서수 옮기기: 원문항 발문(우리말을 발문에), 서수 형태 오류 오답
R567 = "‘~ 번째’는 서수로 나타낸다(first, second, third, fourth, fifth, ninth). 기수를 쓰거나 ’s·-th·-d를 잘못 붙이지 않도록 한다."
S567 = "원문항 오답은 모두 서수 형태 오류인데, 변형 오답은 be동사 수 일치·물음표처럼 관계없는 오류가 섞여 평가 초점이 흐려졌고 발문에 ‘평서문으로’가 붙었다. 원문항 발문으로 되돌리고 오답을 모두 서수 형태 오류로 바꿨다."
def f567(t, ko, items, a, s=S567):
    mk(5, 67, t, items, a, R567, s, st=f"다음 중 우리말 '{ko}'를 영어로 바르게 옮긴 것은?", p="")
CARD = lambda w: f"기수({w})로는 ‘~ 번째’를 나타낼 수 없으므로"; POS = "’s를 붙여도 서수가 되지 않으므로"
f567("B", "그는 네 번째 의자에 앉아 있다", [("He is sitting on the four chair.", CARD("four")), ("He is sitting on the fourth chair.", "‘네 번째’를 서수 fourth로 바르게 나타냈으므로"), ("He is sitting on the forth chair.", "four의 서수는 u가 있는 fourth이고 forth는 ‘앞으로’라는 다른 말이므로"),
     ("He is sitting on the four's chair.", POS), ("He is sitting on the fourd chair.", "fourd라는 말은 없고 서수는 fourth이므로")], 2)
f567("C", "그는 두 번째 문제를 풀고 있다", [("He is solving the two question.", CARD("two")), ("He is solving the twoth question.", "two의 서수는 second이고 twoth라는 말은 없으므로"), ("He is solving the two's question.", POS),
     ("He is solving the second question.", "‘두 번째’를 서수 second로 바르게 나타냈으므로"), ("He is solving the twond question.", "twond라는 말은 없고 서수는 second이므로")], 4, S567 + " 문장도 B(의자)와 겹치지 않게 바꿨다.")
f567("D", "나는 첫 번째 줄에 서 있다", [("I am standing in the first row.", "‘첫 번째’를 서수 first로 바르게 나타냈으므로"), ("I am standing in the one row.", CARD("one")), ("I am standing in the oneth row.", "one의 서수는 first이고 oneth라는 말은 없으므로"),
     ("I am standing in the fist row.", "fist는 ‘주먹’이라는 다른 말이고 서수는 first이므로"), ("I am standing in the one's row.", POS)], 1)
f567("E", "Tom은 다섯 번째 학생이다", [("Tom is the five student.", CARD("five")), ("Tom is the fiveth student.", "five의 서수는 ve를 f로 바꾼 fifth이므로"), ("Tom is the five's student.", POS),
     ("Tom is the fivth student.", "fivth라는 말은 없고 서수는 fifth이므로"), ("Tom is the fifth student.", "‘다섯 번째’를 서수 fifth로 바르게 나타냈으므로")], 5)
f567("F", "Jane은 아홉 번째 주자이다", [("Jane is the nine runner.", CARD("nine")), ("Jane is the nineth runner.", "nine의 서수는 e를 뺀 ninth이므로"), ("Jane is the ninth runner.", "‘아홉 번째’를 서수 ninth로 바르게 나타냈으므로"),
     ("Jane is the nine's runner.", POS), ("Jane is the nineteenth runner.", "nineteenth는 ‘열아홉 번째’이므로")], 3, S567 + " 수도 B(네 번째)와 겹치지 않게 바꿨다.")

# 5-69 큰 수 읽기: B 원문항 발문, C~F는 그 수에 맞춘 오답
R569 = "큰 수는 세 자리씩 끊어 읽는다. 34,200은 thirty-four thousand two hundred처럼 앞의 두 자리를 십 단위(twenty, forty, sixty …)로 읽고 thousand를 붙인다. hundred·thousand에는 -s를 붙이지 않는다."
S569 = "오답 네 개가 원문항의 수(three, thirty, thirteen 등)를 그대로 가져와 문장과 맞지 않아 새 수가 들어간 선택지 하나만 남았다. 오답을 그 수에 맞춰(twelve/twenty/two 등) 새로 썼다."
def f569(t, p, good, chs, why, a, s=S569, **kw):
    FIX.pop((5, 69, t), None)
    items = [(ch, slotnote(ch, good, why, labs=("(A)", "(B)"), sep=" — ").replace("(A) 빈칸", "(A)").replace("(B) 빈칸", "(B)")) for ch in chs]
    mk(5, 69, t, items, a, R569, s, p=p.replace("( A )", "(   A   )").replace("( B )", "(   B   )"), okdup=True, **kw)
f569("C", "21,500은 ( A )-one ( B ) five hundred라고 읽습니다.", "twenty — thousand",
     ["twelve — thousand", "twenty — hundred", "twenty — thousand", "two — thousand", "twenty — million"], ["21의 앞자리는 십 단위 twenty로 읽는다", "천 단위는 thousand로 읽는다"], 3)
f569("D", "48,300은 ( A )-eight ( B ) three hundred라고 읽습니다.", "forty — thousand",
     ["fourteen — thousand", "forty — thousand", "four — thousand", "forty — hundred", "forty — million"], ["48의 앞자리는 십 단위 forty로 읽는다", "천 단위는 thousand로 읽는다"], 2)
f569("E", "62,100은 ( A )-two ( B ) one hundred라고 읽습니다.", "sixty — thousand",
     ["sixty — thousand", "six — thousand", "sixteen — thousand", "sixty — hundred", "sixty — million"], ["62의 앞자리는 십 단위 sixty로 읽는다", "천 단위는 thousand로 읽는다"], 1)
f569("F", "15,400은 ( A ) ( B ) four hundred라고 읽습니다.", "fifteen — thousand",
     ["fifty — thousand", "fifteen — hundred", "five — thousand", "fifteen — million", "fifteen — thousand"], ["15는 fifteen으로 읽는다", "천 단위는 thousand로 읽는다"], 5)

# 5-70 금액 표현 고치기: 원문항 발문과 짧은 지문, 두 군데 오류, 그럴듯한 설명 오답
R570 = "금액은 1이면 단수(one dollar, one cent), 2 이상이면 복수(two dollars, fifty cents)로 쓴다. 달러와 센트 사이에는 and를 쓸 수 있다."
S570 = "원문항은 짧은 지문 속 두 군데 오류를 모두 고치는 설명을 고르는데, 변형 오답(‘cent는 항상 cents’, ‘금액에는 복수형을 절대 쓰지 않는다’ 등)은 뻔하고 유형마다 반복되었으며 일부는 오류가 하나뿐이었다. 원문항처럼 짧은 지문에 두 군데 오류를 두고, 한쪽만 고치거나 관계없는 곳을 고치는 그럴듯한 설명으로 유형마다 새로 썼다."
def f570(t, p, items, a, s=S570):
    FIX.pop((5, 70, t), None)
    mk(5, 70, t, items, a, R570, s, st="R", p=p)
f570("C", "Minho goes to the shop. He buys a pen. The pen is <u>four dollar and thirty cent</u>. He puts it in his bag.",
     [("'four dollar'만 'four dollars'로 고치면 된다.", "thirty cent도 30센트라 thirty cents로 고쳐야 하므로"), ("'thirty cent'만 'thirty cents'로 고치면 된다.", "four dollar도 4달러라 four dollars로 고쳐야 하므로"),
      ("'four dollar and thirty cent'는 'four dollars and thirty cents'로 둘 다 고쳐야 한다.", "4달러와 30센트는 모두 복수라 두 군데를 모두 바르게 고쳤으므로"), ("'thirty'는 큰 수이므로 'thirties'로 고치고 cent는 그대로 둔다.", "수를 나타내는 thirty에는 -s를 붙이지 않고, 복수형이 되어야 할 것은 cent이므로"),
      ("'pen'은 셀 수 있는 명사이므로 'a pen'을 'pens'로 고쳐야 한다.", "펜 한 자루를 사는 것이라 a pen이 맞고, 밑줄 친 부분과도 관계없으므로")], 3, S570 + " 금액도 B(two dollar and one cents)와 겹치지 않게 바꿨다.")
f570("D", "Jiwoo wants some juice. The juice is <u>one dollars and fifty cent</u>. She buys it for her brother.",
     [("'one dollars'만 'one dollar'로 고치면 된다.", "fifty cent도 50센트라 fifty cents로 고쳐야 하므로"), ("'one dollars'는 'one dollar'로, 'fifty cent'는 'fifty cents'로 고쳐야 한다.", "1달러는 단수 dollar, 50센트는 복수 cents로 두 군데를 모두 바르게 고쳤으므로"),
      ("'fifty'는 50이라는 큰 수이므로 'fifties'로 고쳐야 한다.", "수를 나타내는 fifty에는 -s를 붙이지 않고, 복수형이 되어야 할 것은 cent이므로"), ("'juice'는 셀 수 없는 명사이므로 'some juice'를 'a juice'로 고쳐야 한다.", "셀 수 없는 명사 juice에는 a를 쓰지 않아 some juice가 맞으므로"),
      ("'fifty cent'만 'fifty cents'로 고치면 된다.", "one dollars도 1달러라 one dollar로 고쳐야 하므로")], 2)
f570("E", "Tom finds a toy car in a store. It is <u>five dollar and twenty cent</u>. He really likes it.",
     [("'twenty cent'만 'twenty cents'로 고치면 된다.", "five dollar도 5달러라 five dollars로 고쳐야 하므로"), ("금액 사이의 and는 쓰지 않으므로 'five dollar, twenty cent'로 고쳐야 한다.", "달러와 센트 사이에 and를 쓸 수 있고, 틀린 곳은 dollar와 cent이므로"),
      ("'five dollar'만 'five dollars'로 고치면 된다.", "twenty cent도 20센트라 twenty cents로 고쳐야 하므로"), ("'five dollar and twenty cent'는 'five dollars and twenty cents'로 둘 다 고쳐야 한다.", "5달러와 20센트는 모두 복수라 두 군데를 모두 바르게 고쳤으므로"),
      ("'It'은 앞의 a toy car를 가리키므로 'They'로 고쳐야 한다.", "a toy car는 하나라 It이 맞으므로")], 4)
f570("F", "Mom buys two apples at the market. They are <u>one dollars and one cents</u>. She puts them in her basket.",
     [("'one cents' 한 곳만 'one cent'로 바꾸면 된다.", "one dollars도 1달러라 one dollar로 고쳐야 하므로"), ("'They'는 사과 값을 가리키므로 'It'으로 고쳐야 한다.", "They는 앞의 two apples를 가리켜 맞고, 밑줄 친 부분과도 관계없으므로"),
      ("앞의 'one dollars' 한 곳만 'one dollar'로 바꾸면 된다.", "one cents도 1센트라 one cent로 고쳐야 하므로"), ("같은 수가 두 번 나오므로 'one cents'를 빼고 'one dollars'라고만 써야 한다.", "1센트를 빼면 금액이 달라지고, one dollars도 틀린 표현이므로"),
      ("'one dollars'와 'one cents'를 'one dollar and one cent'로 모두 단수로 고쳐야 한다.", "1달러와 1센트는 모두 단수라 두 군데를 모두 바르게 고쳤으므로")], 5)


# ---- 2차 감수(2026-10) 추가 ----
# 5-63 C: 보기 두 개가 원문항과 겹침(1999 동일, 1550은 원문항 정답 연도) → 다른 연도로
f563("C", [("1620 - sixteen twenty", TWO), ("2010 - two thousand ten", TH), ("1905 - nineteen fifty", "가운데가 0이면 oh를 넣어 nineteen oh five로 읽어야 하는데 fifty(50)로 읽었으므로"), ("2005 - two thousand five", TH), ("1988 - nineteen eighty-eight", TWO)], 3,
     "보기 두 개가 원문항과 겹쳤다(1999 - nineteen ninety-nine은 원문항 ③과 같고, 1550은 원문항 정답의 연도를 바르게 읽은 것이다). 겹치는 연도를 다른 연도로 바꾸고 정답 위치도 원문항(②)과 다르게 했다. 정답 보기는 그대로다.")
# 5-69 B: 보기의 (A)·(B) 표지와 빈칸 표기를 원문항처럼
f569("B", "52,600은 ( A )-two ( B ) six hundred라고 읽습니다.", "fifty — thousand", ["fifty — hundred", "five — thousand", "fifteen — hundred", "fifty — thousand", "fifty — million"],
     ["52의 앞자리는 십 단위 fifty로 읽는다", "천 단위는 thousand로 읽는다"], 4, "발문이 원문항과 달랐고, 보기에 (A)·(B) 표지가 붙고 빈칸 모양도 원문항과 달랐다. 원문항 발문과 표기로 되돌렸다. 보기의 낱말과 정답은 그대로다.", st="R")
# 5-70 B: 한 문장뿐인 제시문과 뻔한 오답 → 원문항처럼 짧은 지문, 한쪽만 고치는 그럴듯한 오답
f570("B", "Jisu needs a notebook for school. She finds a nice one. It is <u>two dollar and one cents</u>. She buys it right away.",
     [("'two dollar'는 'two dollars'로, 'one cents'는 'one cent'로 둘 다 고쳐야 한다.", "2달러는 복수 dollars, 1센트는 단수 cent로 두 군데를 모두 바르게 고쳤으므로"), ("'two dollar'만 'two dollars'로 고치면 된다.", "one cents도 1센트라 one cent로 고쳐야 하므로"),
      ("'one cents'만 'one cent'로 고치면 된다.", "two dollar도 2달러라 two dollars로 고쳐야 하므로"), ("'It'은 값을 나타낼 수 없으므로 'The price'로만 써야 한다.", "It으로 앞의 공책을 받아 값을 말할 수 있고, 밑줄 친 부분과도 관계없으므로"),
      ("'one cents'는 아주 작은 돈이므로 빼고 'two dollar'라고만 써야 한다.", "1센트를 빼면 금액이 달라지고, two dollar도 틀린 표현이므로")], 1,
     "제시문이 한 문장뿐이어서 원문항(네 문장 지문)보다 짧았고, 오답(‘항상 단수로 쓴다’, ‘복수형을 전혀 쓰지 않는다’)이 뻔했으며 발문도 달랐다. 원문항처럼 짧은 지문에 넣고, 한쪽만 고치거나 관계없는 곳을 고치는 그럴듯한 설명으로 오답을 바꿨다. 밑줄 친 표현과 정답은 그대로다.")
# 5-61 B~F: 원문항처럼 문장 앞에 ‘·’ 표시
for _t in "BCDEF":
    _k = FIX[(5, 61, _t)]; _p = _k.get("p") or V(5, 61, _t)["passage"]
    _k["p"] = "\n".join("· " + x.strip() for x in _p.split("\n"))
    _k["s"] = (_k["s"].replace(" 정답 위치", " 원문항처럼 문장 앞에 ‘·’를 붙였다. 정답 위치") if " 정답 위치" in _k["s"] else _k["s"] + " 원문항처럼 문장 앞에 ‘·’를 붙였다.")
