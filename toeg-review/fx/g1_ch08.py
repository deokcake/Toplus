# 1급 CH8 비교 (71~80) 수정 예시

# 1-71 비교급 강조: 오답 네 문장을 유형마다 새로(틀린 문장과 짝 없애기)
R71 = "비교급은 much, far, even, still, a lot, a little 등으로 강조하고, very로 직접 강조하지 않는다."
def ok71(w): return f"비교급을 {w}로 강조했으므로 올바르다. 오답이다."
def bad71(fix): return f"very는 비교급을 직접 강조하지 못한다. {fix}로 고쳐야 하므로 정답이다."
S71 = "오답 네 문장이 B와 똑같고 틀린 문장이 같은 표현의 옳은 문장과 짝을 이뤄 대비 단서가 되었다. 옳은 문장 네 개를 유형마다 새로 썼다."
F(1, 71, "C", r=R71, a=5, c=["My new phone is much lighter than my old one.", "The river is even wider here.", "Today is a lot warmer than yesterday.", "This question is far more difficult than the last one.", "This solution is very more efficient than the old one."],
  n=[ok71("much"), ok71("even"), ok71("a lot"), ok71("far"), bad71("much more efficient")], s=S71)
F(1, 71, "D", r=R71, a=2, c=["The subway is much faster than the bus.", "Mina is very taller than her sister.", "This coffee is a little sweeter than usual.", "The test was even easier than I expected.", "His room is far cleaner than mine."],
  n=[ok71("much"), bad71("much taller"), ok71("a little"), ok71("even"), ok71("far")], s=S71)
F(1, 71, "E", r=R71, a=1, c=["The second route is very shorter than the first.", "Winter in Canada is much colder than in Korea.", "This chair is a lot more comfortable than that one.", "The movie was even better than the book.", "The new bridge is far longer than the old one."],
  n=[bad71("much shorter"), ok71("much"), ok71("a lot"), ok71("even"), ok71("far")], s=S71)
F(1, 71, "F", r=R71, a=1, c=["Tom ran very faster than Leo.", "She speaks English much better than before.", "This bag is a little cheaper than that one.", "Mountains are a lot cooler than cities in summer.", "Your plan is far better than mine."],
  n=[bad71("much faster"), ok71("much"), ok71("a little"), ok71("a lot"), ok71("far")], s=S71)

# 1-72 최상급 의미: 동률 가정 괄호 없이도 성립하는 문장으로, C~F는 비교 대상·문장을 새로
R72 = "최상급(the -est), 비교급 + than any other + 단수명사, 비교급 + than all the other + 복수명사, No other + 단수명사 + as ~ as는 모두 ‘가장 ~하다’는 뜻이다."
SAME = "‘가장 ~하다’는 최상급의 뜻이라 나머지와 같다. 오답이다."
def f72(t, c, a, diff, s):
    F(1, 72, t, st="R", c=c, a=a, r=R72, n=[(f"{diff} 뜻이 나머지와 다르므로 정답이다." if i + 1 == a else SAME) for i in range(5)], s=s)
f72("B", ["This lake is deeper than all the other lakes in the region.", "This lake is deeper than any other lake in the region.", "No other lake in the region is as deep as this one.", "This is the deepest lake in the region.", "Every other lake in the region is as deep as this one."], 5,
    "다른 호수들도 모두 이 호수만큼 깊다는 뜻이라", "발문의 ‘동률이 없다고 가정한다’ 괄호를 지워 원문항 발문으로 되돌렸다. 동률을 허용하는 ① ‘No lake … is deeper than this one’을 ‘deeper than all the other lakes’로 바꿔 괄호 없이도 정답이 하나가 되게 했다.")
S72 = "다섯 문장이 B와 똑같고 순서만 달랐다. 비교 대상을 바꿔 문장을 모두 새로 쓰고, 동률 가정 괄호를 지워 원문항 발문으로 되돌렸다."
f72("C", ["This mountain is higher than any other mountain in Korea.", "This is the highest mountain in Korea.", "Every other mountain in Korea is as high as this one.", "No other mountain in Korea is as high as this one.", "This mountain is higher than all the other mountains in Korea."], 3,
    "다른 산들도 모두 이 산만큼 높다는 뜻이라", S72 + " 정답 위치 ③.")
f72("D", ["Some rivers in the country are longer than this one.", "This river is longer than any other river in the country.", "This is the longest river in the country.", "No other river in the country is as long as this one.", "This river is longer than all the other rivers in the country."], 1,
    "이 강보다 긴 강이 있다는 뜻이라", S72 + " 정답 위치 ①.")
f72("E", ["This is the tallest tower in the city.", "This tower is not taller than the other towers in the city.", "No other tower in the city is as tall as this one.", "This tower is taller than any other tower in the city.", "This tower is taller than all the other towers in the city."], 2,
    "다른 탑들보다 높지 않다는 뜻이라", S72 + " 정답 위치 ②.")
f72("F", ["This bridge is older than all the other bridges in the city.", "No other bridge in the city is as old as this one.", "This is the oldest bridge in the city.", "This bridge is older than any other bridge in the city.", "This bridge is newer than any other bridge in the city."], 5,
    "가장 새 다리라는 반대의 뜻이라", S72 + " 정답 위치 ⑤.")

# 1-73 비교 구문 어법: 오답 네 문장을 여러 비교 구문으로 새로
R73 = "less는 원급과 결합하고(less heavy), -er이나 more를 겹쳐 쓰지 않는다. the + 비교급, the + 비교급 / one of the + 최상급 + 복수명사 / 비교급 + than any other + 단수명사 구문을 바르게 쓴다."
S73 = "오답 네 문장이 B와 똑같고 틀린 문장이 같은 표현의 옳은 문장과 짝을 이뤘다. 틀린 문장도 B와 겹치지 않는 새 문장으로 바꾸고, 원문항처럼 the + 비교급, one of the + 최상급, than any other 등 여러 비교 구문으로 옳은 문장을 새로 썼다."
def f73(t, items, a):
    F(1, 73, t, c=[x for x, _ in items], a=a, r=R73, n=[(w + (" 틀린 문장이므로 정답이다." if i + 1 == a else " 올바르므로 오답이다.")) for i, (_, w) in enumerate(items)], s=S73 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f73("C", [("The harder you study, the higher your grade will be.", "the + 비교급, the + 비교급 구문이다."), ("She is one of the kindest people I know.", "one of the + 최상급 + 복수명사이다."),
          ("This street is busier than any other street in town.", "비교급 + than any other + 단수명사이다."), ("Our house is less bigger than theirs.", "less 뒤에 비교급 bigger를 겹쳐 썼다. less big으로 고쳐야 한다."),
          ("My bike is less expensive than yours.", "less + 원급 expensive를 썼다.")], 4)
f73("D", [("Tom is less taller than Leo.", "less 뒤에 비교급 taller를 겹쳐 썼다. less tall로 고쳐야 한다."), ("The sooner we leave, the earlier we will arrive.", "the + 비교급, the + 비교급 구문이다."),
          ("Busan is one of the largest cities in Korea.", "one of the + 최상급 + 복수명사이다."), ("No other runner on the team is faster than Jiwoo.", "No other + 단수명사 + 비교급 than 구문이다."),
          ("Math is less difficult than science for me.", "less + 원급 difficult를 썼다.")], 1)
f73("E", [("This laptop is lighter than any other laptop in the store.", "비교급 + than any other + 단수명사이다."), ("The second movie was less funnier than the first.", "less 뒤에 비교급 funnier를 겹쳐 썼다. less funny로 고쳐야 한다."),
          ("The older he gets, the wiser he becomes.", "the + 비교급, the + 비교급 구문이다."), ("He is one of the best players in the league.", "one of the + 최상급 + 복수명사이다."),
          ("This soup is less spicy than the curry.", "less + 원급 spicy를 썼다.")], 2)
f73("F", [("Gold is more valuable than silver.", "비교급 more valuable + than이다."), ("The more you read, the more you learn.", "the + 비교급, the + 비교급 구문이다."),
          ("It was one of the most exciting games of the season.", "one of the + 최상급 + 복수명사이다."), ("This hotel is less crowded than the one downtown.", "less + 원급 crowded를 썼다."),
          ("Mina is less more experienced than Jane.", "less와 more를 겹쳐 썼다. less experienced로 고쳐야 한다.")], 5)

# 1-74 대화 속 비교 표현: 줄바꿈 복원
for t in "BCDEF":
    F(1, 74, t, p="BR", keepx=True, s="한 줄로 이어 쓴 대화를 원문항처럼 말하는 사람마다 줄을 바꿨다. 밑줄 표현과 정답은 그대로다.")

# 1-75 틀린 문장 개수: 원문항처럼 문장 6개, 1개~5개 정렬
R75 = "비교급을 겹쳐 쓰지 않고(more taller ×), very로 비교급을 강조하지 않는다. 원급 비교는 as + 원급 + as, 배수는 ~ times as + 원급 + as이며, 동사를 꾸밀 때는 부사를 쓴다."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]
def f75(t, lines, judge, wrong, s, **kw):
    F(1, 75, t, p="\n".join(lines), c=CNT5, a=wrong, r=R75, pre=["문장별 판정:"] + judge, k=f"어법상 틀린 문장은 {wrong}개이다.", n="cnt", s=s, **kw)
S75 = "원문항은 보기 문장이 6개인데 변형은 5개였고 개수 선택지 순서가 뒤섞여 있었다. 문장 F를 더해 6개로 맞추고, 선택지를 원문항처럼 1개~5개 순으로 정렬했다. 한 줄에 한 문장씩 나눴다."
f75("B", ["A) Tom is less patient than Jane.", "B) This road is twice as wide as that one.", "C) Mina is very more confident now.", "D) No other building is more taller than this one.", "E) This exam is far harder than the last one.", "F) The more careful you are, the fewer mistakes you make."],
    ["A) 옳음: less + 원급이다.", "B) 옳음: 배수 twice as + 원급 + as이다.", "C) 틀림: very로 비교급을 강조하지 않는다. much more confident.", "D) 틀림: more와 -er을 겹쳐 썼다. taller.",
     "E) 옳음: far로 비교급을 강조했다.", "F) 옳음: the + 비교급, the + 비교급이다."], 2, S75)
f75("C", ["A) This model is not as expensive as that one.", "B) Mina is far more experienced than Tom.", "C) This tank is three times as large as the old one.", "D) Jane is much more taller than Leo.", "E) No other route is as short as this one.", "F) This question is even more difficult than that one."],
    ["A) 옳음: not as + 원급 + as이다.", "B) 옳음: far로 비교급을 강조했다.", "C) 옳음: 배수 three times as + 원급 + as이다.", "D) 틀림: more와 -er을 겹쳐 썼다. much taller.",
     "E) 옳음: No other + as + 원급 + as이다.", "F) 옳음: even으로 비교급을 강조했다."], 1, S75)
f75("D", ["A) This train is much faster than the old one.", "B) Jane is as tall as Mina.", "C) This bag is two times more heavier than mine.", "D) Tom is less more careful than Leo.", "E) No runner is as fast as Mina.", "F) He speaks as fluent as a native speaker."],
    ["A) 옳음: much로 비교급을 강조했다.", "B) 옳음: as + 원급 + as이다.", "C) 틀림: more와 -er을 겹쳐 썼다. two times as heavy as(또는 twice as heavy as).", "D) 틀림: less와 more를 겹쳐 썼다. less careful.",
     "E) 옳음: No + as + 원급 + as이다.", "F) 틀림: 동사 speaks를 꾸미므로 부사 fluently를 써야 한다."], 3,
    S75 + " C의 뜻을 알려 주던 발문 괄호도 지웠다.", st="R")
f75("E", ["A) The new plan is far more practical.", "B) This room is three times as large as ours.", "C) Mina is more kinder than Jane.", "D) No other route is shorter than this one.", "E) Tom is not so patient as Leo.", "F) This car is much more cheaper than mine."],
    ["A) 옳음: far로 비교급을 강조했다.", "B) 옳음: 배수 three times as + 원급 + as이다.", "C) 틀림: more와 -er을 겹쳐 썼다. kinder.", "D) 옳음: No other + 비교급 than 구문이다.",
     "E) 옳음: not so + 원급 + as이다.", "F) 틀림: more와 -er을 겹쳐 썼다. much cheaper."], 2, S75)
f75("F", ["A) The second test is much easier.", "B) This tank is four times as large as that one.", "C) Jane is less experienced than Mina.", "D) Tom is very faster than Leo.", "E) No other book is more usefuler than this one.", "F) My dog is three times as older as yours."],
    ["A) 옳음: much로 비교급을 강조했다.", "B) 옳음: 배수 four times as + 원급 + as이다.", "C) 옳음: less + 원급이다.", "D) 틀림: very로 비교급을 강조하지 않는다. much faster.",
     "E) 틀림: more와 -er을 겹쳐 썼다. more useful.", "F) 틀림: 배수 표현에서 as와 as 사이에는 원급을 쓴다. as old as."], 3, S75)

# 1-76 비교급 강조 배열: 발문 조건 삭제, 오답을 제시어 어순만 바꾼 배열로
R76 = "much/far/even/a little은 비교급 바로 앞에서 정도를 나타낸다. 주어 + be동사 + 강조어 + 비교급 + than + 비교 대상(절) 어순으로 쓴다."
AFT = "강조어가 비교급 뒤로 갔다. 강조어는 비교급 바로 앞에 둔다. 오답이다."
BEF = "강조어가 be동사 앞으로 가 주어 + be동사 어순이 깨졌다. 오답이다."
SPL = "강조어·비교급의 짝이 흩어졌다. 강조어 + 비교급을 붙여 써야 한다. 오답이다."
THN = "than과 뒤의 말 순서가 뒤바뀌었다. than 뒤에 비교 대상(절)을 바른 어순으로 둔다. 오답이다."
OK76 = "주어 + be동사 + 강조어 + 비교급 + than 어순이 바르다. 정답이다."
S76 = "발문에 ‘형태 변화 없이 각각 한 번씩 사용’ 조건이 붙었고 오답이 제시어에 없는 낱말(more, as, are, very)을 더해 조건만으로 지워졌다. 발문을 원문항과 같게 하고, 오답을 제시어의 어순만 바꾼 배열로 새로 만들었다."
def f76(t, c, a, kinds):
    F(1, 76, t, st="R", c=c, a=a, r=R76, n=[(OK76 if i + 1 == a else kinds[i]) for i in range(5)], s=S76 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f76("B", ["The new system is far more efficient than the old one.", "The new system is more far efficient than the old one.", "The new system far is more efficient than the old one.", "The new system is far more efficient the old one than.", "The new system is more efficient far than the old one."], 1,
    [None, SPL, BEF, THN, AFT])
f76("C", ["This bridge is stronger much than it was ten years ago.", "This bridge much is stronger than it was ten years ago.", "This bridge is much stronger than it was ten years ago.", "This bridge is much stronger it than was ten years ago.", "This bridge is much stronger than was it ten years ago."], 3,
    [AFT, BEF, None, THN, THN])
f76("D", ["Mina is taller a little than Jane now.", "Mina a little is taller than Jane now.", "Mina is a taller little than Jane now.", "Mina is a little taller than Jane now.", "Mina is little a taller than Jane now."], 4,
    [AFT, BEF, SPL, None, SPL])
f76("E", ["This test is harder even than yesterday's test.", "This test even is harder than yesterday's test.", "This test is even than harder yesterday's test.", "This test is even harder yesterday's than test.", "This test is even harder than yesterday's test."], 5,
    [AFT, BEF, SPL, THN, None])
f76("F", ["The city is cleaner much than it used to be.", "The city is much cleaner than it used to be.", "The city much is cleaner than it used to be.", "The city is much cleaner than used it to be.", "The city cleaner is much than it used to be."], 2,
    [AFT, None, BEF, THN, SPL])

# 1-77 비교 지문 + 질문: 원문항처럼 영어 질문을 제시하고 대답을 고르게
R77 = "지문의 수치와 배수 표현(twice as ~ as)을 실제 값으로 바꾸고, 질문이 묻는 비교 방향(more/heavier/slower/larger)에 맞는 대상을 찾는다."
S77 = "원문항은 영어 질문에 맞는 대답을 고르는 형식인데 변형은 ‘내용상 옳은 것’을 고르는 형식이었다. 발문을 원문항과 같게 하고, 답이 하나뿐인 영어 질문을 지문 아래에 넣어 보기를 대답 문장으로 바꿨다."
def f77(t, q, c, a, notes):
    F(1, 77, t, st="R", p=V(1, 77, t)["passage"] + f"\n질문: {q}", c=c, a=a, r=R77, n=[(notes[i] + (" 질문에 맞는 대답이므로 정답이다." if i + 1 == a else " 오답이다.")) for i in range(5)], s=S77 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f77("B", "Which car uses more fuel than Car C?", ["Car A uses more fuel than Car C.", "Car B uses more fuel than Car C.", "Car D uses more fuel than Car C.", "Car C uses more fuel than Car B.", "Car A uses more fuel than Car B."], 2,
    ["A는 5 L로 C(7 L)보다 적게 쓴다.", "B는 A의 두 배인 10 L로 C(7 L)보다 많이 쓴다.", "D는 C보다 적게 쓴다.", "C(7 L)는 B(10 L)보다 적게 쓴다.", "A(5 L)는 B(10 L)보다 적게 쓴다."])
f77("C", "Which laptop is heavier than Model C?", ["Model A is heavier than Model C.", "Model D is heavier than Model C.", "Model B is heavier than Model C.", "Model C is heavier than Model B.", "Model B is lighter than Model C."], 3,
    ["A(1.2kg)는 C(1.5kg)보다 가볍다.", "D는 C보다 가볍다.", "B는 A의 두 배인 2.4kg으로 C(1.5kg)보다 무겁다.", "C(1.5kg)는 B(2.4kg)보다 가볍다.", "B(2.4kg)는 C보다 무겁다. 방향이 반대이다."])
f77("D", "Who ran slower than Jane?", ["Tom ran slower than Jane.", "Mina ran slower than Jane.", "Jane ran slower than Leo.", "Leo ran slower than Jane.", "Leo ran faster than Jane."], 4,
    ["Tom은 Jane보다 빨랐다.", "Mina(12초)는 Jane(13초)보다 빨랐다.", "Jane(13초)은 Leo(15초)보다 빨랐다.", "Leo는 15초로 Jane(13초)보다 느렸다.", "Leo(15초)는 Jane보다 느렸다. 방향이 반대이다."])
f77("E", "Which bottle holds more than Bottle C?", ["Bottle D holds more than Bottle C.", "Bottle A holds more than Bottle C.", "Bottle C holds more than Bottle B.", "Bottle B holds less than Bottle C.", "Bottle B holds more than Bottle C."], 5,
    ["D는 C보다 적게 담는다.", "A(500 mL)는 C(750 mL)보다 적게 담는다.", "C(750 mL)는 B(1,000 mL)보다 적게 담는다.", "B(1,000 mL)는 C보다 많이 담는다. 방향이 반대이다.", "B는 A의 두 배인 1,000 mL로 C(750 mL)보다 많이 담는다."])
f77("F", "Which room is larger than Room C?", ["Room B is larger than Room C.", "Room D is larger than Room C.", "Room A is larger than Room C.", "Room C is larger than Room B.", "Room B is smaller than Room C."], 1,
    ["B는 A의 1.5배인 30 m²로 C(25 m²)보다 넓다.", "D는 C보다 좁다.", "A(20 m²)는 C(25 m²)보다 좁다.", "C(25 m²)는 B(30 m²)보다 좁다.", "B(30 m²)는 C보다 넓다. 방향이 반대이다."])

# 1-78 문장의 전환(2차 감수에서 다시 씀): 원문항이 ‘전환 전 → 전환 후’ 짝으로 바뀌어 같은 형식으로
R78 = "‘No other + 단수명사 ~ 비교급 than A’, ‘No other ~ as + 원급 + as A’, ‘Nothing ~ 비교급 than A’는 모두 ‘A가 가장 ~하다’는 최상급의 뜻이다. 전환한 문장도 A가 가장 ~하다는 뜻이어야 한다."
S78 = "원문항이 ‘전환 전 → 전환 후’ 짝을 보여 주는 형식으로 고쳐져, 한 문장짜리 보기로는 원문항과 형식이 맞지 않았다. 원문항처럼 보기마다 전환 전·후 짝을 싣고 그중 하나만 뜻이 달라지게 새로 썼다. 발문도 원문항과 같게 했다."
def f78(t, items, a):
    """items = [(전환 전, 전환 후, 뜻 설명)]"""
    c = [f"{x} → {y}" for x, y, _ in items]
    n = [(f"앞 문장은 ‘{w}’는 뜻인데 뒤 문장은 그 반대의 뜻이 되어 전환이 바르지 않다. 정답이다." if i + 1 == a else f"앞뒤 문장이 모두 ‘{w}’는 뜻이라 바른 전환이다. 오답이다.") for i, (_, _, w) in enumerate(items)]
    F(1, 78, t, st="R", c=c, a=a, r=R78, n=n, okdup=True, s=S78 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f78("B", [("No other student in her class is as tall as Mina.", "Mina is the tallest student in her class.", "Mina가 반에서 키가 가장 크다"),
          ("No other sport is as popular as soccer in this town.", "Soccer is less popular than any other sport in this town.", "축구가 이 마을에서 가장 인기 있다"),
          ("No other month is hotter than August here.", "August is hotter than any other month here.", "8월이 이곳에서 가장 덥다"),
          ("Nothing is more valuable than friendship.", "Friendship is more valuable than anything else.", "우정이 가장 소중하다"),
          ("Nothing is as important as safety.", "Safety is the most important thing.", "안전이 가장 중요하다")], 2)
f78("C", [("No other laptop in the store is cheaper than this one.", "This laptop is cheaper than any other laptop in the store.", "이 노트북이 가게에서 가장 싸다"),
          ("Nothing is more exciting than traveling.", "Traveling is more exciting than anything else.", "여행이 가장 신난다"),
          ("No other river in Korea is as long as this river.", "This river is the longest in Korea.", "이 강이 한국에서 가장 길다"),
          ("No other city in the country is larger than this city.", "This city is the largest in the country.", "이 도시가 그 나라에서 가장 크다"),
          ("Nothing is more difficult than this puzzle.", "This puzzle is easier than anything else.", "이 퍼즐이 가장 어렵다")], 5)
f78("D", [("No other runner on the team is faster than Jane.", "Jane is slower than any other runner on the team.", "Jane이 팀에서 가장 빠르다"),
          ("Nothing is more refreshing than cold water.", "Cold water is more refreshing than anything else.", "찬물이 가장 상쾌하다"),
          ("No other mountain in Asia is as high as Mt. Everest.", "Mt. Everest is the highest mountain in Asia.", "에베레스트산이 아시아에서 가장 높다"),
          ("No other season is more beautiful than spring.", "Spring is more beautiful than any other season.", "봄이 가장 아름답다"),
          ("Nothing is as sweet as honey.", "Honey is the sweetest thing.", "꿀이 가장 달다")], 1)
f78("E", [("No other guide I have read is more useful than this one.", "This guide is more useful than any other guide I have read.", "이 안내서가 내가 읽은 것 중 가장 유용하다"),
          ("Nothing is more comfortable than my old sofa.", "My old sofa is more comfortable than anything else.", "내 낡은 소파가 가장 편하다"),
          ("No other animal on land is as big as the elephant.", "The elephant is smaller than any other animal on land.", "코끼리가 육지에서 가장 크다"),
          ("No other day of the week is busier than Monday.", "Monday is busier than any other day of the week.", "월요일이 가장 바쁘다"),
          ("Nothing is as precious as family.", "Family is the most precious thing.", "가족이 가장 소중하다")], 3)
f78("F", [("No other student in the group is as smart as Tom.", "Tom is the smartest student in the group.", "Tom이 모둠에서 가장 똑똑하다"),
          ("Nothing is more relaxing than a warm bath.", "A warm bath is more relaxing than anything else.", "따뜻한 목욕이 가장 편안하다"),
          ("No other planet in the solar system is larger than Jupiter.", "Jupiter is larger than any other planet in the solar system.", "목성이 태양계에서 가장 크다"),
          ("Nothing in the shop is cheaper than this pen.", "This pen is more expensive than anything else in the shop.", "이 펜이 가게에서 가장 싸다"),
          ("No other building in the town is as old as this church.", "This church is the oldest building in the town.", "이 교회가 마을에서 가장 오래되었다")], 4)

# 1-79 one of the + 최상급 + 복수명사 설명: 오답 설명을 유형마다 새로
R79 = "one of the + 최상급 + 복수명사는 ‘가장 ~한 것들 중 하나’라는 뜻이다. 여러 대상 가운데 하나를 가리키므로 명사는 복수형을 쓴다."
S79 = "오답 네 설명이 B와 똑같아서 유형마다 다른 그럴듯한 오개념으로 새로 썼다."
def f79(t, c, a, notes):
    F(1, 79, t, c=c, a=a, r=R79, n=[(notes[i] + (" 옳은 설명이므로 정답이다." if i + 1 == a else " 오답이다.")) for i in range(5)], s=S79)
f79("C", ["most creative는 비교급이므로 뒤에 than이 와야 한다.", "one of 뒤의 명사는 문장의 주어 Mina와 수를 맞춰 단수로 써야 한다.", "in the company가 뒤에 있으므로 creative 대신 부사 creatively를 써야 한다.",
          "the most 대신 a most를 써도 같은 뜻이다.", "designers가 복수인 이유는 여러 최고 수준의 디자이너들 중 한 명임을 나타내기 때문이다."], 5,
    ["most creative는 최상급이다.", "one of 뒤의 명사는 여러 대상이므로 주어와 관계없이 복수형이다.", "designers를 꾸미므로 형용사를 쓴다.", "a most creative는 ‘매우 창의적인’이라는 다른 뜻이다.", "여러 대상 중 하나라는 뜻을 바르게 설명했다."])
f79("D", ["useful은 1음절이라 most 대신 -est를 붙여야 한다.", "I own 앞에는 관계대명사 which를 반드시 써야 한다.", "books가 복수인 이유는 여러 유용한 책 중 하나를 뜻하기 때문이다.",
          "books 대신 book을 써도 ‘가장 유용한 책 한 권’이라는 같은 뜻이 된다.", "one은 숫자이므로 books와 함께 쓸 수 없다."], 3,
    ["useful은 2음절이라 most useful이 맞다.", "목적격 관계대명사는 생략할 수 있다.", "여러 대상 중 하나라는 뜻을 바르게 설명했다.", "one of 뒤에 단수명사를 쓰면 틀린 문장이 된다.", "one of + 복수명사는 ‘~ 중 하나’라는 바른 표현이다."])
f79("E", ["best는 good의 비교급이므로 the를 붙일 수 없다.", "students가 복수라서 동사도 are를 써야 한다.", "‘반에서 가장’이라는 뜻을 나타내려면 in class를 of class로 바꿔야 한다.",
          "students가 복수인 이유는 최고 수준의 여러 학생 가운데 한 명을 나타내기 때문이다.", "one of the best students는 ‘두 명의 우수한 학생 중 한 명’이라는 뜻이다."], 4,
    ["best는 good의 최상급이므로 the를 붙인다.", "주어는 one(Jane)이므로 동사는 is이다.", "장소·집단 안에서의 최상급에는 in을 쓸 수 있다.", "여러 대상 중 하나라는 뜻을 바르게 설명했다.", "one of는 두 명이 아니라 여러 명 중 한 명을 뜻한다."])
f79("F", ["largest는 최상급이므로 앞의 the를 생략해야 한다.", "cities가 복수인 이유는 큰 도시 여러 곳 중 하나임을 나타내기 때문이다.", "Asia가 대륙 이름이라 in 대신 of를 써야 한다.",
          "cities가 복수이므로 one 대신 ones를 써야 한다.", "one of 뒤에 최상급이 오면 명사는 셀 수 없는 명사여야 한다."], 2,
    ["최상급 앞에는 the를 쓴다.", "여러 대상 중 하나라는 뜻을 바르게 설명했다.", "장소 안에서의 최상급에는 in을 쓴다.", "주어 Seoul이 한 곳이므로 one을 쓴다.", "one of 뒤에는 셀 수 있는 명사의 복수형이 온다."])

# 1-80 as + 형용사/부사 오류 두 개, 선택지를 두 기호 조합으로
R80 = "as ~ as 안에서 동사를 꾸미면 부사를, be동사·연결동사(look, feel, seem, sound, become)의 보어이면 형용사를 쓴다."
S80 = "원문항은 as ~ as 안의 형용사/부사 구별 오류 두 개를 찾는데, 변형은 ‘more ~ as’ 오류 하나만 있고 선택지도 단일 기호였다. 원문항처럼 형용사/부사 오류 두 개를 넣고 선택지를 모두 두 기호 조합으로 새로 만들었다. 오류 위치는 유형마다 다르다."
L80B = " 또 검토 의견(원문항에 비해 지문이 너무 짧음)에 따라 문장마다 앞뒤 상황을 넣어 지문을 원문항 길이로 늘렸다."
L80 = " 또 B 검토 의견(원문항에 비해 지문이 너무 짧음)이 이 유형에도 해당해, 문장마다 앞뒤 상황을 넣어 지문을 원문항 길이로 늘렸다."
def f80(t, p, judge, bad, c, a):
    F(1, 80, t, p=p, c=c, a=a, r=R80, pre=["밑줄별 판정:"] + judge, k=f"어법상 틀린 것은 {bad}이다.", n=setnotes(c, bad, "틀린 것"), s=S80 + (L80B if t == "B" else L80) + f" 정답 {bad}.")
f80("B", "Before the city marathon, Tom trained (A)<u>as hard as</u> he could every morning. During the race, he tried to run (B)<u>as quick as</u> the experienced runners in front of him. His coach, waiting at the finish line, seemed (C)<u>as pleased as</u> ever with his effort. After the race, Tom felt (D)<u>as confidently as</u> a real champion. Thanks to all that training, he finally became (E)<u>as strong as</u> his older brother.",
    ["(A) 옳음: hard는 trained를 꾸미는 부사이다.", "(B) 틀림: run을 꾸미므로 부사 quickly를 써야 한다.", "(C) 옳음: seemed의 보어이므로 형용사 pleased이다.", "(D) 틀림: felt의 보어이므로 형용사 confident를 써야 한다.", "(E) 옳음: became의 보어이므로 형용사 strong이다."],
    "(B), (D)", ["(A), (B)", "(B), (D)", "(A), (C)", "(C), (E)", "(D), (E)"], 2)
f80("C", "On her first day at the call center, the new assistant answered calls (A)<u>as politely as</u> possible. Even when customers complained, she looked (B)<u>as calmly as</u> the manager sitting next to her. She typed customer notes (C)<u>as fast as</u> anyone in the office. By the afternoon, the customers seemed (D)<u>as happy as</u> they had been before the problem. Before leaving, she finished her daily reports (E)<u>as neat as</u> she could.",
    ["(A) 옳음: answered를 꾸미는 부사 politely이다.", "(B) 틀림: looked의 보어이므로 형용사 calm을 써야 한다.", "(C) 옳음: fast는 typed를 꾸미는 부사이다.", "(D) 옳음: seemed의 보어이므로 형용사 happy이다.", "(E) 틀림: finished를 꾸미므로 부사 neatly를 써야 한다."],
    "(B), (E)", ["(A), (C)", "(B), (D)", "(B), (E)", "(C), (D)", "(A), (E)"], 3)
f80("D", "Before the final exam, Mina studied (A)<u>as carefully as</u> possible for two weeks. When she opened the test paper, it looked (B)<u>as easy as</u> the practice test she had taken. She wrote her answers (C)<u>as clear as</u> she could so that the teacher could read them. When the scores came out, her teacher sounded (D)<u>as warmly as</u> usual. In the end, Mina's score was (E)<u>as high as</u> her best friend's.",
    ["(A) 옳음: studied를 꾸미는 부사 carefully이다.", "(B) 옳음: looked의 보어이므로 형용사 easy이다.", "(C) 틀림: wrote를 꾸미므로 부사 clearly를 써야 한다.", "(D) 틀림: sounded의 보어이므로 형용사 warm을 써야 한다.", "(E) 옳음: was의 보어이므로 형용사 high이다."],
    "(C), (D)", ["(A), (B)", "(B), (E)", "(A), (D)", "(C), (D)", "(C), (E)"], 4)
f80("E", "During the busy holiday season, the team worked (A)<u>as efficient as</u> possible to meet the deadline. At first, the plan seemed (B)<u>as simple as</u> they had hoped. Thanks to good teamwork, they finished the project (C)<u>as early as</u> expected. When the client approved it, everyone felt (D)<u>as relieved as</u> the team leader. At the final meeting, the leader spoke (E)<u>as polite as</u> possible to thank the client.",
    ["(A) 틀림: worked를 꾸미므로 부사 efficiently를 써야 한다.", "(B) 옳음: seemed의 보어이므로 형용사 simple이다.", "(C) 옳음: early는 finished를 꾸미는 부사이다.", "(D) 옳음: felt의 보어이므로 형용사 relieved이다.", "(E) 틀림: spoke를 꾸미므로 부사 politely를 써야 한다."],
    "(A), (E)", ["(A), (E)", "(B), (C)", "(A), (D)", "(C), (E)", "(B), (D)"], 1)
f80("F", "For the school talent show, Jane practiced (A)<u>as patiently as</u> possible every evening. On the stage, her voice sounded (B)<u>as sweetly as</u> a bird's song. Between the songs, she spoke to the audience (C)<u>as fluent as</u> a native speaker. The audience looked (D)<u>as excited as</u> she was at the end of the show. After that night, she became (E)<u>as famous as</u> her music teacher in town.",
    ["(A) 옳음: practiced를 꾸미는 부사 patiently이다.", "(B) 틀림: sounded의 보어이므로 형용사 sweet를 써야 한다.", "(C) 틀림: spoke를 꾸미므로 부사 fluently를 써야 한다.", "(D) 옳음: looked의 보어이므로 형용사 excited이다.", "(E) 옳음: became의 보어이므로 형용사 famous이다."],
    "(B), (C)", ["(A), (D)", "(C), (E)", "(B), (D)", "(A), (C)", "(B), (C)"], 5)


# ---- 2차 감수(2026-10) 추가 ----
# 1-73 B: 같은 문장이 옳은 형태(①)와 틀린 형태(④)로 함께 나오고, 보기가 모두 less 구문
f73("B", [("The earlier you start, the sooner you will finish.", "the + 비교급, the + 비교급 구문을 바르게 썼다."), ("He is one of the most popular singers in Korea.", "one of the + 최상급 + 복수명사를 바르게 썼다."),
          ("No other student in the class is taller than Tom.", "No other + 단수명사 + 비교급 than을 바르게 썼다."), ("The new policy is less stricter than the old one.", "less 뒤에는 원급을 쓴다. less strict로 고쳐야 한다."),
          ("This suitcase is heavier than any other bag here.", "비교급 + than any other + 단수명사를 바르게 썼다.")], 4)
FIX[(1, 73, "B")]["s"] = "① ‘The new policy is less strict …’와 ④ ‘The new policy is less stricter …’가 같은 문장의 옳은 형태·틀린 형태로 함께 나와 대비만으로 답이 드러났고, 보기가 모두 less 구문이었다. 원문항처럼 the + 비교급, one of the + 최상급, No other, than any other 구문을 섞은 새 문장으로 바꿨다. 정답은 그대로 ④."

# 1-79 B: 보기가 짧고 뻔한 일반 설명(1-60 B 검토 의견 ‘선택지 품질이 원문항보다 낮음’과 같은 문제)
f79("B", ["'runners'가 복수형인 것은 팀에서 가장 빠른 여러 선수들 가운데 한 명임을 나타내기 때문이다.", "'one of the' 뒤에 최상급 'fastest'가 왔으므로 뒤의 명사는 단수형 'runner'로 써야 한다.",
          "'fastest'는 'fast'의 비교급이므로 뒤에 'than'이 이어져야 한다.", "'on the team'이 범위를 나타내므로 최상급 앞의 'the'는 생략해야 한다.",
          "'one'이 주어 'Tom'과 같은 사람을 가리키므로 'runners' 대신 'runner'를 써서 수를 맞춰야 한다."], 1,
    ["여러 대상 가운데 하나를 가리키므로 복수명사를 쓴다.", "one of the + 최상급 뒤에는 복수명사를 쓴다.", "fastest는 비교급이 아니라 최상급이다.", "범위를 나타내는 말이 있어도 최상급 앞에는 the를 쓴다.", "one은 여러 선수 가운데 한 명을 뜻하므로 뒤의 명사는 복수여야 한다."])
FIX[(1, 79, "B")]["s"] = "보기가 ‘one of는 정확히 두 개 중 하나만 뜻한다’처럼 짧고 뻔한 일반 설명이어서 원문항보다 수준이 낮았다. 원문항처럼 밑줄 친 표현을 작은따옴표로 짚고 이유까지 밝힌 그럴듯한 설명으로 보기 다섯 개를 새로 썼다. 정답 위치 ①."
