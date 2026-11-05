# 7급 CH10 날짜·요일·시각과 서수 (91~100) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 7-92 대답에 맞는 질문: 원문항 발문, 오답 질문을 유형마다 새로
R792 = "대답이 알려 주는 정보(시각, 요일, 날짜, 월)와 시제(is/was)를 보고 질문을 고른다. What time은 시각, What day는 요일, What date는 날짜를 묻는다."
S792 = "발문에 ‘정보 종류와 시제가 모두 일치하는’ 조건이 붙었고, 오답 서너 개(What day was it? / What is it? / What date is it? / What time is it?)가 원문항 선택지 그대로였다. 원문항 발문으로 되돌리고 오답 질문을 유형마다 새로 썼다."
TNS = "현재를 묻는 질문이라 과거형 대답(It was ~.)과 맞지 않으므로"; TNS2 = "과거를 묻는 질문이라 현재형 대답(It is ~.)과 맞지 않으므로"
def f792(t, p, items, a, s=S792):
    mk(7, 92, t, items, a, R792, s, st="R", p=p)
f792("B", "A: _______________________\nB: It was February.", [("What year was it?", "월이 아니라 연도를 묻는 질문이므로"), ("How was the weather?", "월이 아니라 날씨를 묻는 질문이므로"), ("What month was it?", "과거의 월을 묻는 질문이라 대답(It was February.)과 정보·시제가 모두 맞으므로"),
     ("What month is it now?", TNS), ("What date was it then?", "월이 아니라 며칠인지 날짜를 묻는 질문이므로")], 3,
     s=S792 + " 원문항에 없던 상황 설명(The old calendar only shows the month.)도 지웠다.")
f792("C", "A: _______________________\nB: It is May 5th.", [("What is the date today?", "오늘 날짜를 묻는 질문이라 대답(It is May 5th.)과 정보·시제가 모두 맞으므로"), ("What date was it last week?", TNS2), ("What time is it now?", "날짜가 아니라 시각을 묻는 질문이므로"),
     ("What season is it?", "날짜가 아니라 계절을 묻는 질문이므로"), ("How old are you?", "날짜가 아니라 나이를 묻는 질문이므로")], 1)
f792("D", "A: _______________________\nB: It is 8 o'clock.", [("What day is today?", "시각이 아니라 요일을 묻는 질문이므로"), ("What time was it then?", TNS2), ("How is the weather now?", "시각이 아니라 날씨를 묻는 질문이므로"),
     ("What time is it right now?", "지금 시각을 묻는 질문이라 대답(It is 8 o'clock.)과 정보·시제가 모두 맞으므로"), ("Where is the clock?", "시각이 아니라 시계가 있는 곳을 묻는 질문이므로")], 4)
f792("E", "A: _______________________\nB: It is Monday.", [("What day was the party?", TNS2), ("What day is it today?", "오늘 요일을 묻는 질문이라 대답(It is Monday.)과 정보·시제가 모두 맞으므로"), ("What date is it now?", "요일이 아니라 며칠인지 날짜를 묻는 질문이므로"),
     ("What season is it now?", "요일이 아니라 계절을 묻는 질문이므로"), ("What time is it in Seoul?", "요일이 아니라 시각을 묻는 질문이므로")], 2)
f792("F", "A: _______________________\nB: It was June 3rd.", [("What month is it?", "현재의 월을 묻는 질문이라 과거형 날짜 대답과 맞지 않으므로"), ("What is the date now?", TNS), ("What time was it?", "날짜가 아니라 시각을 묻는 질문이므로"),
     ("What day of the week was it?", "날짜가 아니라 요일을 묻는 질문이므로"), ("What date was it yesterday?", "어제 날짜를 묻는 질문이라 대답(It was June 3rd.)과 정보·시제가 모두 맞으므로")], 5)

# 7-93 비인칭 주어가 아닌 It: 비인칭 it 문장을 유형마다 새로
R793 = "시각, 요일, 날짜, 계절, 날씨, 명암을 나타내는 It은 뜻이 없는 비인칭 주어이다. 앞에 나온 물건이나 동물을 가리키는 It은 ‘그것’이라는 뜻의 대명사이다."
S793 = "비인칭 it 오답 네 문장(It is Tuesday / April 28th / summer / 5 o'clock)이 원문항 선택지 그대로였다. 날씨·명암·시각·요일·날짜·계절을 섞어 비인칭 it 문장을 유형마다 새로 썼다."
JO = lambda k: k + ("을" if (ord(k[-1]) - 0xAC00) % 28 else "를")
IMP = lambda k: f"{JO(k)} 나타내는 비인칭 주어 It이므로"; PRN = lambda k: f"It이 ‘그것’이라는 뜻으로 {JO(k)} 가리키는 대명사라 비인칭 주어가 아니므로"
def f793(t, items, a):
    mk(7, 93, t, items, a, R793, S793)
f793("B", [("It is windy today.", IMP("날씨")), ("It is ten o'clock now.", IMP("시각")), ("It is my new bag.", PRN("가방")), ("It is Friday today.", IMP("요일")), ("It is spring now.", IMP("계절"))], 3)
f793("C", [("It is dark outside.", IMP("명암")), ("It is very hot today.", IMP("날씨")), ("It is Sunday.", IMP("요일")), ("It is a cute dog.", PRN("개")), ("It is October 9th.", IMP("날짜"))], 4)
f793("D", [("It is snowing now.", IMP("날씨")), ("It is noon.", IMP("시각")), ("It is July 4th.", IMP("날짜")), ("It is Wednesday.", IMP("요일")), ("It is her pencil case.", PRN("필통"))], 5)
f793("F", [("It is cold in winter.", IMP("날씨")), ("It is Tom's new book.", PRN("책")), ("It is 3 p.m.", IMP("시각")), ("It is Thursday.", IMP("요일")), ("It is foggy this morning.", IMP("날씨"))], 2)

# 7-94 What date - 서수: 원문항 발문과 대화별 우리말
S794 = "발문이 ‘월과 일을 묻고, 날짜의 일을 서수로 읽어 대답할 때’라고 두 빈칸의 정답(date, 서수)을 알려 주었다. 원문항 발문으로 되돌리고, 원문항처럼 대화마다 우리말을 붙였다. 보기와 정답은 그대로다."
R794 = "며칠인지 물을 때는 What date is it today?를 쓰고, 날짜의 일은 서수(first, second, third, tenth …)로 말한다."
W94 = {"year": "연도를 묻는 말이라 월·일 대답과 맞지 않는다", "time": "시각을 묻는 말이라 날짜 대답과 맞지 않는다"}
def f794(t, mon_en, mon_ko, day_ko, good):
    V_ = V(7, 94, t); gs = [x.strip() for x in good.split(" - ")]; items = []
    for ch in V_["c"]:
        xs = [x.strip() for x in re.split(r" [-–] ", ch)]
        if xs == gs: items.append((ch, "며칠인지 묻는 date와 날짜의 일을 나타내는 서수를 바르게 짝지었으므로")); continue
        bits = []
        if xs[0] != gs[0]: bits.append(f"첫째 빈칸 {xs[0]}: {W94[xs[0]]}")
        if xs[1] != gs[1]: bits.append(f"둘째 빈칸 {xs[1]}: 날짜의 일은 기수가 아니라 서수({gs[1]})로 말한다")
        items.append((ch, ". ".join(bits) + ". 따라서"))
    p = f"A: What _______ is it today?(오늘 며칠이야?)\nB: It is {mon_en} _______.({mon_ko} {day_ko}이야.)"
    mk(7, 94, t, items, int(V_["ans"]), R794, S794, st="R", p=p, okdup=True)
f794("B", "April", "4월", "10일", "date - tenth"); f794("C", "March", "3월", "3일", "date - third"); f794("D", "July", "7월", "2일", "date - second")
f794("E", "May", "5월", "5일", "date - fifth"); f794("F", "December", "12월", "12일", "date - twelfth")

# 7-95 밑줄 친 수 표현이 틀린 문장: 원문항 발문·밑줄·우리말, 옳은 문장을 새로
R795 = "개수를 말할 때는 기수(one, two, three …), 순서를 말할 때는 서수(first, second, third …)를 쓴다. 우리말 뜻이 ‘~ 번째, 첫째, ~층, ~등’이면 서수가 필요하다."
S795 = "옳은 오답 네 문장(my fourth daughter, my first car, three cars, the ninth floor)이 원문항 문장 그대로였고, 밑줄과 문장별 우리말 해석이 사라졌으며 발문도 바뀌었다. 원문항 발문과 밑줄·우리말 해석으로 되돌리고 문장을 유형마다 새로 썼다. 원문항 ④(in the ninth floor)는 층 앞에 on을 써야 해 정답이 둘이 될 수 있으므로 층은 on으로 썼다."
CARD = lambda w: f"개수를 나타내므로 기수({w})를 바르게 썼으므로"; ORD = lambda w: f"순서를 나타내므로 서수({w})를 바르게 썼으므로"
def f795(t, items, a, s=S795):
    mk(7, 95, t, items, a, R795, s, st="R")
f795("B", [("I have <u>two</u> brothers.(나는 남자 형제가 두 명 있다.)", CARD("two")), ("Today is my <u>tenth</u> birthday.(오늘은 나의 열 번째 생일이다.)", ORD("tenth")), ("There are <u>seven</u> days in a week.(일주일은 7일이다.)", CARD("seven")),
           ("He is my <u>three</u> son.(그는 나의 셋째 아들이다.)", "‘셋째’라는 순서를 나타내므로 기수 three가 아니라 서수 third를 써야 하므로"), ("She lives on the <u>fifth</u> floor.(그녀는 5층에 산다.)", ORD("fifth"))], 4)
f795("C", [("We need <u>four</u> chairs.(우리는 의자 네 개가 필요하다.)", CARD("four")), ("This is my <u>second</u> visit to Jeju.(이번이 나의 두 번째 제주 방문이다.)", ORD("second")), ("It is my <u>five</u> book.(그것은 나의 다섯 번째 책이다.)", "‘다섯 번째’라는 순서를 나타내므로 기수 five가 아니라 서수 fifth를 써야 하므로"),
           ("He came in <u>first</u> in the race.(그는 경주에서 1등으로 들어왔다.)", ORD("first")), ("There are <u>twelve</u> months in a year.(1년은 12달이다.)", CARD("twelve"))], 3)
f795("D", [("My sister is <u>eight</u> years old.(내 여동생은 여덟 살이다.)", CARD("eight")), ("This is the <u>three</u> floor.(여기는 3층이다.)", "‘3층’은 순서를 나타내므로 기수 three가 아니라 서수 third를 써야 하므로"), ("Take the <u>first</u> bus.(첫 번째 버스를 타라.)", ORD("first")),
           ("I read <u>two</u> books a week.(나는 일주일에 책 두 권을 읽는다.)", CARD("two")), ("Our class is on the <u>fourth</u> floor.(우리 반은 4층에 있다.)", ORD("fourth"))], 2)
f795("E", [("Sit in the <u>fifth</u> chair.(다섯 번째 의자에 앉아라.)", ORD("fifth")), ("We live on the <u>third</u> floor.(우리는 3층에 산다.)", ORD("third")), ("Tom won <u>first</u> prize.(Tom은 1등 상을 탔다.)", ORD("first")),
           ("She has <u>four</u> notebooks.(그녀는 공책이 네 권 있다.)", CARD("four")), ("This is my <u>two</u> visit to the museum.(이번이 나의 두 번째 박물관 방문이다.)", "‘두 번째’라는 순서를 나타내므로 기수 two가 아니라 서수 second를 써야 하므로")], 5,
     s="밑줄과 문장별 우리말 해석이 사라지고 발문이 바뀌었다. 원문항 발문과 밑줄·우리말 해석으로 되돌렸다. 보기와 정답은 그대로다.")
f795("F", [("Tom is the <u>four</u> runner.(Tom은 네 번째 주자이다.)", "‘네 번째’라는 순서를 나타내므로 기수 four가 아니라 서수 fourth를 써야 하므로"), ("I have <u>three</u> cousins.(나는 사촌이 세 명 있다.)", CARD("three")), ("January is the <u>first</u> month of the year.(1월은 한 해의 첫 번째 달이다.)", ORD("first")),
           ("We have <u>six</u> classes today.(우리는 오늘 수업이 여섯 개 있다.)", CARD("six")), ("He is in the <u>second</u> grade.(그는 2학년이다.)", ORD("second"))], 1)

# 7-96 서수 배열 빈칸: 원문항 발문, 원문항처럼 철자가 비슷한 단어를 오답으로
R796 = "순서를 차례로 늘어놓은 서수 배열이므로 빈칸에도 서수가 들어간다. 기수(nine)나 철자가 비슷한 다른 단어와 헷갈리지 않도록 한다."
S796 = "발문에 ‘작은 순서부터 이어지는 서수 배열의’가 붙었고, 오답이 앞뒤 서수와 기수뿐이라 원문항(thin, thirst, thirty처럼 철자가 비슷한 단어)보다 쉬웠다. 원문항 발문으로 되돌리고 원문항처럼 철자가 비슷한 단어를 오답에 넣었다."
def f796(t, items, a):
    mk(7, 96, t, items, a, R796, S796, st="R")
f796("B", [("nine", "기수(9)라 서수 배열에 들어갈 수 없으므로"), ("night", "‘밤’이라는 뜻으로 철자만 비슷한 단어이므로"), ("ninth", "eighth와 tenth 사이의 서수(아홉 번째)이므로"), ("ninety", "기수 90이라 서수 배열에 들어갈 수 없으므로"), ("nineteen", "기수 19라 서수 배열에 들어갈 수 없으므로")], 3)
f796("C", [("eight", "기수(8)라 서수 배열에 들어갈 수 없으므로"), ("eighth", "seventh와 ninth 사이의 서수(여덟 번째)이므로"), ("eighty", "기수 80이라 서수 배열에 들어갈 수 없으므로"), ("eighteen", "기수 18이라 서수 배열에 들어갈 수 없으므로"), ("height", "‘높이’라는 뜻으로 철자만 비슷한 단어이므로")], 2)
f796("D", [("sixth", "fifth와 seventh 사이의 서수(여섯 번째)이므로"), ("six", "기수(6)라 서수 배열에 들어갈 수 없으므로"), ("sixty", "기수 60이라 서수 배열에 들어갈 수 없으므로"), ("sixteenth", "열여섯 번째라는 서수라 fifth와 seventh 사이에 올 수 없으므로"), ("sixteen", "기수 16이라 서수 배열에 들어갈 수 없으므로")], 1)
f796("E", [("forty", "기수 40이라 서수 배열에 들어갈 수 없으므로"), ("fourth", "third와 fifth 사이의 서수(네 번째)이므로"), ("four", "기수(4)라 서수 배열에 들어갈 수 없으므로"), ("fourteen", "기수 14라 서수 배열에 들어갈 수 없으므로"), ("forth", "‘앞으로’라는 뜻으로 철자만 비슷한 단어이므로")], 2)
f796("F", [("ten", "기수(10)라 서수 배열에 들어갈 수 없으므로"), ("tent", "‘천막’이라는 뜻으로 철자만 비슷한 단어이므로"), ("twenty", "기수 20이라 서수 배열에 들어갈 수 없으므로"), ("tenth", "ninth와 eleventh 사이의 서수(열 번째)이므로"), ("tennis", "‘테니스’라는 뜻으로 철자만 비슷한 단어이므로")], 4)

# 7-98 시각 영작: 원문항 발문과 <보기>, C~F는 30분이 아닌 시각으로
R798 = "시각은 It is + 시각으로 말한다. ‘~시 …분 지났다’는 분 + past + 시, ‘~시 …분 전’은 분 + to + 시로 쓰고, 30분은 half, 15분은 a quarter로 말한다."
S798 = "발문이 ‘It is로 시작하는 기본 시간 표현’이라고 알려 주어 어순 오답이 바로 지워졌고, 정답이 원문항과 같은 ‘half past + 시’에 오답 틀도 원문항과 같았으며 <보기> 표시도 빠졌다. 원문항 발문과 <보기>로 되돌리고, 30분이 아닌 시각(past·to, quarter)으로 문장을 새로 썼다."
ORDR = "It is + 시각의 어순이 아니므로"
def f798(t, ko, items, a, s=S798):
    mk(7, 98, t, items, a, R798, s, st="R", p=f"<보기>\n{ko}")
V98B = V(7, 98, "B")
mk(7, 98, "B", list(zip(V98B["c"], ["6시 45분(7시 15분 전)을 a quarter to seven으로 바르게 나타냈으므로", "6시 30분을 나타내므로", "분·past/to·시의 어순이 아니므로", "7시 15분을 나타내므로", ORDR])), int(V98B["ans"]), R798,
   "발문이 ‘It is로 시작하는 기본 시간 표현’이라고 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.", st="R")
f798("C", "지금은 7시 15분이야.", [("It is a quarter to eight.", "7시 45분(8시 15분 전)을 나타내므로"), ("It is seven a quarter past.", "분 + past + 시의 어순이 아니므로"), ("It is a quarter past seven.", "7시 15분을 a quarter past seven으로 바르게 나타냈으므로"),
     ("It is half past seven.", "7시 30분을 나타내므로"), ("Past a quarter seven it is.", ORDR)], 3)
f798("D", "지금은 9시 10분이야.", [("It is ten to nine.", "8시 50분(9시 10분 전)을 나타내므로"), ("It is nine past ten.", "10시 9분을 나타내므로"), ("Ten past nine is it.", ORDR),
     ("It is past ten nine.", "분 + past + 시의 어순이 아니므로"), ("It is ten past nine.", "9시 10분을 ten past nine으로 바르게 나타냈으므로")], 5)
f798("E", "지금은 4시 50분이야.", [("It is ten past four.", "4시 10분을 나타내므로"), ("It is ten to five.", "4시 50분(5시 10분 전)을 ten to five로 바르게 나타냈으므로"), ("It is five to ten.", "9시 55분을 나타내므로"),
     ("Ten to five is it.", ORDR), ("It is to ten five.", "분 + to + 시의 어순이 아니므로")], 2)
f798("F", "지금은 11시 5분이야.", [("It is five to eleven.", "10시 55분(11시 5분 전)을 나타내므로"), ("It is eleven past five.", "5시 11분을 나타내므로"), ("Five past eleven is it.", ORDR),
     ("It is five past eleven.", "11시 5분을 five past eleven으로 바르게 나타냈으므로"), ("It is eleven five past.", "분 + past + 시의 어순이 아니므로")], 4)

# 7-99 서수 철자: 원문항처럼 문장 속 밑줄 서수, 서수를 새로
R799 = "서수는 대부분 기수 + th로 만들지만, first, second, third는 따로 외우고 fifth(five), ninth(nine), twelfth(twelve), eighth(eight), twentieth(twenty)처럼 철자가 바뀌는 것에 주의한다."
S799 = "원문항은 문장 속 밑줄 친 서수를 판별하는데 ‘월 + 서수’ 구만 나열했고, 서수(fifth, ninth, twelfth, eighth)가 원문항 그대로였으며, 같은 서수의 옳은 철자와 틀린 철자가 함께 있어 비교만으로 답이 나왔다. 원문항 발문과 문장 속 밑줄로 되돌리고, 서수가 겹치지 않게 문장을 새로 썼다."
OKS = lambda w: f"서수({w})의 철자가 바르므로"
def f799(t, items, a, s=S799):
    mk(7, 99, t, items, a, R799, s, st="R")
f799("B", [("My brother is in the <u>fourth</u> grade.", OKS("fourth")), ("She came <u>second</u> in the race.", OKS("second")), ("Today is April <u>threeth</u>.", "three의 서수는 threeth가 아니라 third이므로"),
           ("It is the <u>eleventh</u> day of the trip.", OKS("eleventh")), ("Our festival is on October <u>twentieth</u>.", OKS("twentieth"))], 3)
f799("C", [("Christmas is December <u>twenty-fifth</u>.", OKS("twenty-fifth")), ("My birthday is July <u>nineth</u>.", "nine의 서수는 e를 빼고 ninth로 쓰므로"), ("I sat in the <u>sixth</u> row.", OKS("sixth")),
           ("He is the <u>first</u> student in line.", OKS("first")), ("This is her <u>thirteenth</u> birthday.", OKS("thirteenth"))], 2)
f799("D", [("We are in the <u>seventh</u> grade.", OKS("seventh")), ("Turn left at the <u>third</u> corner.", OKS("third")), ("It was her <u>fortieth</u> birthday.", OKS("fortieth")),
           ("The test is on June <u>fiveth</u>.", "five의 서수는 ve를 f로 바꿔 fifth로 쓰므로"), ("He finished <u>fourteenth</u> in the race.", OKS("fourteenth"))], 4)
mk(7, 99, "E", list(zip(["He finished <u>second</u>.", "June <u>twelfth</u> is Saturday.", "My room is on the <u>eighth</u> floor.", "She is the <u>thirtieth</u> visitor.", "Today is the <u>fourtieth</u> day of school."],
   [OKS("second"), OKS("twelfth"), OKS("eighth"), OKS("thirtieth"), "forty의 서수는 u 없이 fortieth로 쓰므로"])), 5, R799, "밑줄이 사라지고 발문이 바뀌었다. 원문항 발문과 서수 밑줄로 되돌렸다. 보기와 정답은 그대로다.", st="R")
f799("F", [("She won <u>third</u> place.", OKS("third")), ("It is his <u>sixteenth</u> birthday.", OKS("sixteenth")), ("This is my <u>hundredth</u> day at school.", OKS("hundredth")),
           ("Turn to the <u>tenth</u> page.", OKS("tenth")), ("The party is on May <u>twentyth</u>.", "twenty의 서수는 y를 ie로 바꿔 twentieth로 쓰므로")], 5)

# 7-100 날짜·요일 묻고 답하기 설명: 원문항 발문, E·F는 틀린 설명 하나
R7100 = "What date는 날짜, What day는 요일을 묻는다. 날짜의 일은 서수로 말하고, 날짜·요일을 말할 때는 비인칭 주어 It을 쓴다."
def f7100(t, lines, judge, c, a, s):
    ok = c[a - 1]
    F(7, 100, t, st="R", p="[ 보기 ]\n" + "\n".join(lines), c=c, a=a, r=R7100, pre=["설명별 판정: " + j for j in judge], k=f"옳은 설명은 {ok}이다.", n=setnotes(c, ok, "옳은 설명"), okdup=True, s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f7100("B", ["가. 'What day is it today?'에는 'It is May 5th.'로 대답한다.", "나. 'What is the date today?'는 오늘 날짜를 묻는 표현이다.", "다. 요일을 말할 때는 'It is Friday.'처럼 It을 주어로 쓴다.", "라. 'June 1st'의 1st는 first로 읽는다."],
      ["가 X. What day는 요일을 묻으므로 May 5th가 아니라 요일로 대답한다.", "나 O. What is the date today?는 날짜를 묻는다.", "다 O. 요일은 비인칭 주어 It으로 말한다.", "라 O. 1st는 서수 first이다."],
      V(7, 100, "B")["c"], 3, "발문이 ‘시간·날짜·순서’로 넓어졌다. 원문항 발문으로 되돌리고, 발문에 맞게 날짜와 요일을 묻고 답하는 설명으로 [ 보기 ]를 새로 썼다. 보기와 정답은 그대로다.")
f7100("E", ["가. 'What day was it?'은 지난 요일을 묻는 표현이다.", "나. first, second, third는 기수이다.", "다. June은 달(월)의 이름이다.", "라. 'It is Sunday.'의 It은 요일을 나타내는 비인칭 주어이다."],
      ["가 O. was를 써서 지난 요일을 묻는다.", "나 X. first, second, third는 순서를 나타내는 서수이다.", "다 O. June은 6월이다.", "라 O. 요일을 나타내는 It은 비인칭 주어이다."],
      ["가, 나", "나, 다, 라", "가, 다, 라", "가, 다", "가, 나, 다, 라"], 3, "틀린 설명이 하나도 없어 네 개를 모두 고르는 것이 정답이라, 틀린 설명을 가려내는 원문항과 정답 구조가 달랐다. 원문항처럼 틀린 설명 하나(나)를 넣었다.")
f7100("F", ["가. 'When is your birthday?'에는 'It is May 3rd.'처럼 날짜로 답할 수 있다.", "나. 'What day is it?'은 요일을 묻는 질문이다.", "다. December는 요일의 이름이다.", "라. third는 서수이다."],
      ["가 O. 생일이 언제인지 물으면 날짜로 답한다.", "나 O. What day는 요일을 묻는다.", "다 X. December는 12월, 달(월)의 이름이다.", "라 O. third는 세 번째라는 서수이다."],
      ["가, 나", "나, 다, 라", "가, 나, 라", "가, 다", "가, 나, 다"], 3, "틀린 설명이 하나도 없어 네 개를 모두 고르는 것이 정답이라, 틀린 설명을 가려내는 원문항과 정답 구조가 달랐다. 원문항처럼 틀린 설명 하나(다)를 넣고 날짜로 답하는 설명을 새로 썼다.")

# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, r, s, **kw):
    FIX.pop((7, n, t), None)
    mk(7, n, t, items, a, r, s, **kw)
# 7-91 B·F: 오답 네 개가 원문항 선택지 그대로, 정답과 헷갈릴 달이 없음 / D: 보기 다섯이 원문항과 같음
R791 = "달 이름: January(1월), February(2월), March(3월), April(4월), May(5월), June(6월), July(7월), August(8월), September(9월), October(10월), November(11월), December(12월)."
MON = {"January": "1월", "February": "2월", "March": "3월", "April": "4월", "May": "5월", "June": "6월", "July": "7월", "August": "8월", "September": "9월", "October": "10월", "November": "11월", "December": "12월"}
def g791(t, opts, a, s):
    mk(7, 91, t, [(m, f"‘{MON[m]}’을 뜻하는 낱말이므로") for m in opts], a, R791, s)
g791("B", ["March", "June", "April", "May", "July"], 4, "오답 네 개(July, September, December, October)가 모두 원문항 선택지 그대로이고 May와 헷갈릴 만한 달이 없어 원문항보다 쉬웠다. 정답 위치(②)도 원문항과 같았다. 원문항처럼 철자나 순서가 가까워 헷갈리기 쉬운 달로 오답을 바꾸고 정답 위치를 옮겼다.")
g791("D", ["December", "November", "October", "February", "January"], 1, "보기 다섯 개(December, September, October, August, July)가 원문항 선택지와 똑같고 순서만 달랐다. 12월과 헷갈리기 쉬운 달(November, October, January, February)로 보기를 새로 썼다. 정답은 그대로다.")
g791("F", ["May", "March", "April", "January", "June"], 2, "오답 네 개(September, July, October, December)가 모두 원문항 선택지 그대로이고 March와 헷갈릴 만한 달이 없어 원문항보다 쉬웠다. 헷갈리기 쉬운 달(May, April 등)로 오답을 바꾸고 정답 위치를 옮겼다.")
# 7-94: 오답의 year → 원문항의 핵심 함정인 day로, D·E는 정답 위치를 옮김
W94B = dict(W94, day="요일을 묻는 말이라 ‘며칠이야?’라는 우리말과 맞지 않는다")
S794B = "발문이 ‘월과 일을 묻고, 날짜의 일을 서수로 읽어 대답할 때’라고 두 빈칸의 정답(date, 서수)을 알려 주었다. 원문항 발문으로 되돌리고, 원문항처럼 대화마다 우리말을 붙였다. 또 오답에 원문항의 핵심 함정인 day(요일) 대신 year가 들어 있어 쉽게 지워졌으므로 year를 day로 바꿨다."
def g794(t, mon_en, mon_ko, day_ko, opts, a, s=S794B + " 정답은 그대로다."):
    gs = opts[a-1].split(" - "); items = []
    for ch in opts:
        xs = ch.split(" - ")
        if xs == gs: items.append((ch, "며칠인지 묻는 date와 날짜의 일을 나타내는 서수를 바르게 짝지었으므로")); continue
        bits = []
        if xs[0] != gs[0]: bits.append(f"첫째 빈칸 {xs[0]}: {W94B[xs[0]]}")
        if xs[1] != gs[1]: bits.append(f"둘째 빈칸 {xs[1]}: 날짜의 일은 기수가 아니라 서수({gs[1]})로 말한다")
        items.append((ch, ". ".join(bits) + ". 따라서"))
    redo(94, t, items, a, R794, s, st="R", p=f"A: What _______ is it today?(오늘 며칠이야?)\nB: It is {mon_en} _______.({mon_ko} {day_ko}이야.)", okdup=True)
g794("B", "April", "4월", "10일", ["day - tenth", "date - tenth", "date - ten", "time - tenth", "day - ten"], 2)
g794("C", "March", "3월", "3일", ["date - three", "day - third", "date - third", "time - third", "day - three"], 3)
g794("D", "July", "7월", "2일", ["day - two", "time - second", "date - two", "date - second", "day - second"], 4, S794B + " 정답 위치도 B(②)와 겹치지 않게 옮겼다.")
g794("E", "May", "5월", "5일", ["day - five", "time - fifth", "day - fifth", "date - five", "date - fifth"], 5, S794B + " 정답 위치도 원문항·C(③)와 겹치지 않게 옮겼다.")
g794("F", "December", "12월", "12일", ["date - twelfth", "date - twelve", "time - twelfth", "day - twelve", "day - twelfth"], 1)
# 7-95 D: 틀린 낱말(three)이 B와 같고, ⑤(on the fourth floor)가 정답 ②(the three floor)의 단서
FIX.pop((7, 95, "D"), None)
f795("D", [("My sister is <u>eight</u> years old.(내 여동생은 여덟 살이다.)", CARD("eight")), ("This is the <u>six</u> floor.(여기는 6층이다.)", "‘6층’은 순서를 나타내므로 기수 six가 아니라 서수 sixth를 써야 하므로"), ("Take the <u>first</u> bus.(첫 번째 버스를 타라.)", ORD("first")),
           ("I read <u>two</u> books a week.(나는 일주일에 책 두 권을 읽는다.)", CARD("two")), ("He is the <u>fourth</u> boy in line.(그는 줄에서 네 번째 소년이다.)", ORD("fourth"))], 2,
     S795 + " 틀린 낱말(three)이 B와 겹치지 않게 six로 바꾸고, 층을 서수로 쓰는 꼴을 보여 주는 문장은 정답의 단서가 되므로 넣지 않았다.")
# 7-97 D: 원문항에서 요일만 바꾼 문장
R797 = "어제(yesterday), 지난밤(last night)처럼 지난 일을 말할 때 be동사는 과거형 was/were를 쓴다. I·he·she·it과 단수 주어에는 was, you·we·they와 복수 주어에는 were를 쓴다."
mk(7, 97, "D", [("are", "are는 현재형이므로"), ("is", "is는 현재형이므로"), ("was", "어제의 일이고 주어 it에 맞는 과거형이므로"), ("am", "am은 현재형이고 I에만 쓰므로"), ("were", "were는 you·복수 주어에 쓰는 과거형이므로")], 3, R797,
   "두 문장(Today is Friday. Yesterday ___ Thursday.)이 원문항(Today is Monday. Yesterday ___ Sunday.)에서 요일만 바꾼 것이고 정답(was)도 같았다. 날씨를 말하는 문장으로 바꿨다. 보기와 정답은 그대로다.", p="Today is sunny. Yesterday it ______ rainy.")
# 7-99 F: 정답 위치가 원문항·E와 같은 ⑤
redo(99, "F", [("The party is on May <u>twentyth</u>.", "twenty의 서수는 y를 ie로 바꿔 twentieth로 쓰므로"), ("She won <u>third</u> place.", OKS("third")), ("It is his <u>sixteenth</u> birthday.", OKS("sixteenth")), ("This is my <u>hundredth</u> day at school.", OKS("hundredth")),
     ("Turn to the <u>tenth</u> page.", OKS("tenth"))], 1, R799, S799 + " 정답 위치도 원문항·E(⑤)와 겹치지 않게 옮겼다.", st="R")
# 7-100 C·D: 낱말 뜻풀이 설명, 정답 조합·위치가 서로 같고 원문항과도 같음 / E·F: 정답 위치가 모두 ③
S7100B = "설명이 ‘%s’ 같은 낱말 뜻풀이여서 발문(날짜와 요일을 묻고 답하는 방법)과 맞지 않고 원문항보다 쉬웠다. 정답 조합(가, 나, 다)과 위치(③)도 %s와 같았고, [ 보기 ]와 따옴표 표기도 원문항과 달랐다. 발문에 맞는 설명으로 새로 쓰고 정답 조합을 바꿨다."
f7100("C", ["가. 'What date is it?'은 요일을 묻는 표현이다.", "나. 'What day is it?'이라고 물으면 'It is Monday.'처럼 대답한다.", "다. 날짜의 '3rd'는 three가 아니라 third로 읽는다.", "라. 요일 이름은 문장 가운데에 오면 소문자로 시작한다."],
      ["가 X. What date는 날짜를 묻는다.", "나 O. What day는 요일을 묻고 요일로 대답한다.", "다 O. 날짜의 일은 서수로 읽는다.", "라 X. 요일 이름은 어디에 오든 대문자로 시작한다."],
      ["가, 나", "나, 다", "가, 다, 라", "나, 다, 라", "가, 나, 다"], 2, S7100B % ("Monday는 요일이다", "원문항·D"))
f7100("D", ["가. 'What date is it today?'라고 물으면 'It is June 2nd.'처럼 대답한다.", "나. 날짜의 '2nd'는 two로 읽는다.", "다. 요일을 물을 때는 'What time is it?'이라고 한다.", "라. 'It is Friday.'는 요일을 묻는 말에 알맞은 대답이다."],
      ["가 O. What date는 날짜를 묻고 날짜로 대답한다.", "나 X. 2nd는 서수 second로 읽는다.", "다 X. What time은 시각을 묻고, 요일은 What day로 묻는다.", "라 O. 요일은 It is + 요일로 대답한다."],
      ["가, 나", "다, 라", "가, 다, 라", "가, 라", "나, 다, 라"], 4, S7100B % ("Sunday는 요일이다", "원문항·C"))
FIX.pop((7, 100, "E"), None); FIX.pop((7, 100, "F"), None)
f7100("E", ["가. 'What day was it?'은 지난 요일을 묻는 표현이다.", "나. first, second, third는 기수이다.", "다. June은 달(월)의 이름이다.", "라. 'It is Sunday.'의 It은 요일을 나타내는 비인칭 주어이다."],
      ["가 O. was를 써서 지난 요일을 묻는다.", "나 X. first, second, third는 순서를 나타내는 서수이다.", "다 O. June은 6월이다.", "라 O. 요일을 나타내는 It은 비인칭 주어이다."],
      ["가, 다, 라", "나, 다, 라", "가, 나", "가, 다", "가, 나, 다, 라"], 1, "틀린 설명이 하나도 없어 네 개를 모두 고르는 것이 정답이라, 틀린 설명을 가려내는 원문항과 정답 구조가 달랐다. 원문항처럼 틀린 설명 하나(나)를 넣었다. 정답 위치도 다른 유형(③)과 겹치지 않게 옮겼다.")
f7100("F", ["가. 'When is your birthday?'에는 'It is May 3rd.'처럼 날짜로 답할 수 있다.", "나. 'What day is it?'은 요일을 묻는 질문이다.", "다. December는 요일의 이름이다.", "라. third는 서수이다."],
      ["가 O. 생일이 언제인지 물으면 날짜로 답한다.", "나 O. What day는 요일을 묻는다.", "다 X. December는 12월, 달(월)의 이름이다.", "라 O. third는 세 번째라는 서수이다."],
      ["가, 나", "나, 다, 라", "가, 다", "가, 나, 다", "가, 나, 라"], 5, "틀린 설명이 하나도 없어 네 개를 모두 고르는 것이 정답이라, 틀린 설명을 가려내는 원문항과 정답 구조가 달랐다. 원문항처럼 틀린 설명 하나(다)를 넣고 날짜로 답하는 설명을 새로 썼다. 정답 위치도 다른 유형(③)과 겹치지 않게 옮겼다.")
