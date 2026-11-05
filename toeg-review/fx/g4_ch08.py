# 4급 CH8 비교급·최상급 (71~80) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]

# 4-71 비교급·최상급 연결: 원문항 발문, 같은 원급 반복 없이 유형마다 새로
R471 = "비교급·최상급은 보통 -er·-est(단모음 + 단자음은 자음을 겹쳐 쓰고, 자음 + y는 y를 i로)나 more·most(긴 단어)로 만들며, good·well - better - best, bad - worse - worst, many·much - more - most는 불규칙 변화이다."
S471 = "발문에 bad·little의 뜻 설명이 붙었고, 같은 원급이 옳은 변화와 틀린 변화로 두 번 나와 대비 단서가 되었다. 원문항 발문으로 되돌리고 같은 원급이 두 번 나오지 않게 유형마다 새로 썼다."
REG = "규칙 변화를 바르게 연결했으므로"; DBL = "단모음 + 단자음이라 자음을 겹쳐 쓴 형태로 바르게 연결했으므로"; YI = "자음 + y라 y를 i로 바꾼 형태로 바르게 연결했으므로"; MM = "긴 단어라 more, most를 쓴 형태로 바르게 연결했으므로"; IRR = "불규칙 변화를 바르게 연결했으므로"
def f471(t, items, a, s=S471):
    mk(4, 71, t, items, a, R471, s, st="R", okdup=True)
f471("B", [("small - smaller - smallest", REG), ("fat - fatter - fattest", DBL), ("bad - badder - baddest", "bad는 불규칙 변화라 worse - worst로 써야 하므로"), ("careful - more careful - most careful", MM), ("funny - funnier - funniest", YI)], 3,
     "정답(good - gooder - goodest)이 원문항과 같았고 good이 두 번 나와 단서가 되었다. 원문항 발문으로 되돌리고 묶음을 새로 썼다.")
f471("C", [("nice - nicer - nicest", "-e로 끝나 -r, -st만 붙인 형태로 바르게 연결했으므로"), ("hot - hoter - hotest", "단모음 + 단자음으로 끝나는 hot은 t를 겹쳐 hotter - hottest로 써야 하므로"), ("expensive - more expensive - most expensive", MM), ("many - more - most", IRR), ("early - earlier - earliest", YI)], 2)
f471("D", [("easy - easier - easiest", YI), ("tall - taller - tallest", REG), ("thin - thinner - thinnest", DBL), ("much - more - most", IRR), ("famous - famouser - famousest", "긴 단어 famous는 more famous - most famous로 써야 하므로")], 5)
f471("E", [("wide - wider - widest", "-e로 끝나 -r, -st만 붙인 형태로 바르게 연결했으므로"), ("heavy - heavier - heaviest", YI), ("good - better - best", IRR), ("busy - more busy - most busy", "자음 + y로 끝나는 busy는 busier - busiest로 써야 하므로"), ("popular - more popular - most popular", MM)], 4)
f471("F", [("sad - sader - sadest", "단모음 + 단자음으로 끝나는 sad는 d를 겹쳐 sadder - saddest로 써야 하므로"), ("far - farther - farthest", IRR), ("wet - wetter - wettest", DBL), ("pretty - prettier - prettiest", YI), ("dry - drier - driest", YI)], 1)

# 4-72 비교급 형태: 원문항 발문, 없는 형태 대신 그럴듯한 실제 형태의 오답
R472 = "than 앞에는 비교급을 쓴다. bad - worse, little - less, many - more, good - better, far - farther는 불규칙 변화이고 fast는 faster로 쓴다."
S472 = "오답에 없는 형태(worseest, moreer 등)가 섞여 쉽게 지워졌다. 원문항처럼 원급·최상급·잘못된 규칙형 같은 그럴듯한 형태로 오답을 바꿨다."
BASE = "원급이라 than과 함께 쓸 수 없으므로"; SUP = "최상급이라 than과 함께 쓸 수 없으므로"
def f472(t, p, items, a, s=S472):
    mk(4, 72, t, items, a, R472, s, st="R", p=p, okdup=True)
f472("B", "Today is _______(bad) than yesterday.", [("worse", "bad의 불규칙 비교급이므로"), ("bad", BASE), ("worst", SUP), ("badder", "bad는 불규칙 변화라 badder로 쓰지 않으므로"), ("more bad", "bad의 비교급은 more bad가 아니라 worse이므로")], 1)
f472("C", "The station is _______(far) than the school.", [("farther", "far의 불규칙 비교급이므로"), ("far", BASE), ("farthest", SUP), ("farer", "far는 불규칙 변화라 farer로 쓰지 않으므로"), ("more far", "far의 비교급은 more far가 아니라 farther이므로")], 1,
     "제시문과 정답(less)이 원문항과 똑같았고 오답도 없는 형태였다. 낱말을 far로 바꿔 제시문을 새로 쓰고 " + S472[S472.index("원문항처럼"):])
f472("D", "Tom has _______(many) books than I do.", [("many", BASE), ("more", "many의 불규칙 비교급이므로"), ("most", SUP), ("manier", "many는 불규칙 변화라 manier로 쓰지 않으므로"), ("much", "much는 셀 수 없는 명사에 쓰는 원급이므로")], 2)
f472("E", "This test is _______(good) than that one.", [("good", BASE), ("best", SUP), ("better", "good의 불규칙 비교급이므로"), ("gooder", "good은 불규칙 변화라 gooder로 쓰지 않으므로"), ("well", "well은 부사이고 비교급도 아니므로")], 3)
f472("F", "Jane runs _______(fast) than Amy.", [("fast", BASE), ("fastest", SUP), ("more fast", "짧은 단어 fast는 more가 아니라 -er을 붙이므로"), ("faster", "fast에 -er을 붙인 비교급이므로"), ("fastly", "fastly라는 말은 없으므로")], 4)

# 4-73 C: 원문항과 같던 제시문을 새로
mk(4, 73, "C", [("far", "far는 비교급을 강조할 수 있으므로"), ("more", "older가 이미 비교급이라 more를 겹쳐 쓸 수 없으므로"), ("much", "much는 비교급을 강조할 수 있으므로"), ("even", "even은 비교급을 강조할 수 있으므로"), ("a little", "a little은 비교급 앞에서 ‘조금 더’를 나타낼 수 있으므로")], 2,
   "비교급 앞에는 much·far·even·a lot·a little을 쓸 수 있다. very는 쓰지 않으며, -er 비교급 앞에 more를 겹쳐 쓰지도 않는다.", "제시문과 정답(very)이 원문항과 똑같았다. 제시문을 ‘My brother is ___ older than me.’로 바꾸고 정답을 more로 바꿨다.", p="My brother is _______ older than me.", okdup=True)

# 4-74 틀린 문장: 원문항 발문, 짝 없이 유형마다 새로
R474 = "짧은 단어는 -er·-est, 긴 단어는 more·most를 붙이며 둘을 겹쳐 쓰지 않는다. good - better - best, bad - worse - worst는 불규칙 변화이다."
S474 = "발문에 ‘표준적인 비교급·최상급 형태를 기준으로’가 붙었고, 정답 문장과 같은 문장의 옳은 형태가 함께 있어 대비 단서가 되었으며 오답이 유형마다 같았다. 원문항 발문으로 되돌리고 짝 문장 없이 유형마다 새로 썼다."
OK74 = "비교급·최상급을 바르게 썼으므로"
def f474(t, items, a, s=S474):
    mk(4, 74, t, [(x, w or OK74) for x, w in items], a, R474, s, st="R")
f474("B", [("Tom is taller than Ben.", ""), ("This is the easiest test.", ""), ("Seoul is bigger than Busan.", ""), ("Jane is the beautifullest girl here.", "긴 단어 beautiful은 the most beautiful로 써야 하므로"), ("My room is cleaner than yours.", "")], 4)
f474("C", [("The Nile is the longest river in the world.", ""), ("This puzzle is more easy than that one.", "easy의 비교급은 easier이므로"), ("This is the best pizza in town.", ""), ("Jane is more careful than Tom.", ""), ("It is the coldest day of the year.", "")], 2,
     S474 + " 정답(the most fatest animal)이 원문항과 같아 새로 썼다.")
f474("D", [("Tom is more taller than Ben.", "taller에 more를 겹쳐 쓸 수 없으므로"), ("Minho is the shortest boy in class.", ""), ("This question is more difficult than that one.", ""), ("Summer is hotter than spring.", ""), ("She is the kindest person I know.", "")], 1)
f474("E", [("Today is warmer than yesterday.", ""), ("Your idea is better than mine.", ""), ("This is the most easiest test.", "easiest에 most를 겹쳐 쓸 수 없으므로"), ("He is the richest man in town.", ""), ("The movie was more exciting than the book.", "")], 3)
f474("F", [("Jane sings better than me.", ""), ("Busan is smaller than Seoul.", ""), ("This is the worst day of my life.", ""), ("Math is the most difficult subject for me.", ""), ("He is gooder than me at math.", "good의 비교급은 불규칙 better이므로")], 5)

# 4-75 옳은 것 개수: 원문항 형식(ⓐ~ⓔ, 밑줄, 1개~5개)
ST475 = "다음 중 밑줄 친 부분이 어법상 옳은 문장의 개수를 고르시오."
R475 = "비교급·최상급에는 -er·-est와 more·most를 겹쳐 쓰지 않는다. heavy - heavier, fast - faster, tall - tallest, good - better - best, bad - worse - worst처럼 알맞은 형태를 쓴다."
S475 = "보기 기호 ⓐ~ⓔ가 a~e로 바뀌어 한 줄로 이어졌고 밑줄이 사라졌으며 선택지 순서가 뒤섞였고, 발문에 ‘표준적인 형태를 기준으로’가 붙었다. 원문항 발문과 형식(ⓐ~ⓔ 줄바꿈, 밑줄, 1개~5개)으로 되돌렸다."
def f475(t, lines, judge, ok, s=S475):
    n = len(ok.split(","))
    F(4, 75, t, st=ST475, p="\n".join(lines), c=CNT5, a=n, r=R475, pre=["문장별 판정: " + j for j in judge], k=f"밑줄 친 부분이 옳은 문장은 {ok}로 {n}개이다.", n="cnt", s=s + ipos(n))
f475("B", ["ⓐ Tom is <u>taller than</u> Ben.", "ⓑ This is <u>the most cheapest</u> shirt.", "ⓒ Jane is <u>more beautiful than</u> Amy.", "ⓓ Today is <u>hotter than</u> yesterday.", "ⓔ He is <u>the best</u> player."],
     ["ⓐ O. tall의 비교급 taller이다.", "ⓑ X. cheapest에 most를 겹쳐 쓸 수 없다.", "ⓒ O. 긴 단어 beautiful에 more를 썼다.", "ⓓ O. hot의 비교급 hotter이다.", "ⓔ O. good의 최상급 best이다."], "ⓐ, ⓒ, ⓓ, ⓔ")
f475("C", ["ⓐ This box is <u>more heavier than</u> that box.", "ⓑ Jeju is <u>warmer than</u> Seoul in winter.", "ⓒ Tom is <u>the most tall</u> in his class.", "ⓓ This is <u>the best</u> movie of the year.", "ⓔ She runs <u>more fast than</u> me."],
     ["ⓐ X. heavier에 more를 겹쳐 쓸 수 없다.", "ⓑ O. warm의 비교급 warmer이다.", "ⓒ X. tall의 최상급은 the tallest이다.", "ⓓ O. good의 최상급 best이다.", "ⓔ X. fast의 비교급은 faster이다."], "ⓑ, ⓓ",
     "ⓐ·ⓑ가 원문항 문장과 거의 같았고 기호·밑줄·선택지 순서도 원본과 달랐다. 문장을 새로 쓰고 원문항 형식으로 되돌렸으며 정답 개수를 2개로 바꿨다.")
f475("D", ["ⓐ This test is <u>easier than</u> that one.", "ⓑ Tom is <u>more taller than</u> Ben.", "ⓒ Jane is <u>the most prettiest</u>.", "ⓓ This book is <u>the most interesting</u>.", "ⓔ He is <u>worser than</u> me."],
     ["ⓐ O. easy의 비교급 easier이다.", "ⓑ X. taller에 more를 겹쳐 쓸 수 없다.", "ⓒ X. prettiest에 most를 겹쳐 쓸 수 없다.", "ⓓ O. 긴 단어 interesting에 most를 썼다.", "ⓔ X. bad의 비교급은 worse이고 worser라는 말은 없다."], "ⓐ, ⓓ",
     S475 + " 정답 개수가 원문항(3개)과 겹치지 않게 ⓒ를 틀린 문장으로 바꿨다.")
f475("E", ["ⓐ The dog is <u>bigger than</u> the cat.", "ⓑ This is <u>the easiest</u> question.", "ⓒ Tom is <u>better than</u> Ben.", "ⓓ Jane is <u>more happier than</u> Amy.", "ⓔ It is <u>the worst</u> day."],
     ["ⓐ O. big의 비교급 bigger이다.", "ⓑ O. easy의 최상급 easiest이다.", "ⓒ O. good의 비교급 better이다.", "ⓓ X. happier에 more를 겹쳐 쓸 수 없다.", "ⓔ O. bad의 최상급 worst이다."], "ⓐ, ⓑ, ⓒ, ⓔ",
     S475)
f475("F", ["ⓐ Seoul is <u>larger than</u> Busan.", "ⓑ This bag is <u>more heavier than</u> that one.", "ⓒ Jane is <u>the most kindest</u>.", "ⓓ Tom is <u>the most fast</u> runner.", "ⓔ This movie is <u>more better than</u> that one."],
     ["ⓐ O. large의 비교급 larger이다.", "ⓑ X. heavier에 more를 겹쳐 쓸 수 없다.", "ⓒ X. kindest에 most를 겹쳐 쓸 수 없다.", "ⓓ X. fast의 최상급은 the fastest이다.", "ⓔ X. better에 more를 겹쳐 쓸 수 없다."], "ⓐ",
     S475 + " 다른 유형과 정답 개수가 겹치지 않게 ⓑ·ⓓ·ⓔ를 틀린 문장으로 바꿨다.")

# 4-76 우리말에 맞는 비교급: 원문항 발문, 원급·최상급 같은 실제 형태의 오답
R476 = "than 앞에는 비교급을 쓴다. little - less, good - better, much - more, far - farther는 불규칙 변화이고, 긴 단어 delicious는 more delicious로 쓴다."
S476 = "오답이 없는 형태(betterest, moreest 등)와 이중 비교급 위주여서 쉽게 지워졌다. 원문항처럼 원급·최상급 같은 실제 형태를 오답에 넣었다."
def f476(t, p, items, a, s=S476):
    mk(4, 76, t, items, a, R476, s, st="R", p=p, okdup=True)
f476("B", "Tom has ________(더 적은) money than Ben.", [("little", BASE), ("less", "양의 little의 불규칙 비교급이므로"), ("least", SUP), ("littler", "양의 little은 littler로 쓰지 않으므로"), ("a little", "a little은 ‘조금 있는’이라 비교급이 아니므로")], 2)
f476("C", "This pizza is ________(더 맛있는) than that one.", [("delicious", BASE), ("deliciouser", "긴 단어 delicious에는 -er을 붙이지 않으므로"), ("most delicious", SUP), ("more delicious", "긴 단어 delicious의 비교급이므로"), ("the most delicious", SUP)], 4,
     "제시문과 정답(worse)이 원문항과 똑같았고 오답도 없는 형태였다. 제시문을 새로 써서 정답을 more delicious로 바꾸고 " + S476[S476.index("원문항처럼"):])
f476("D", "This book is ________(더 좋은) than that one.", [("good", BASE), ("gooder", "good은 불규칙 변화라 gooder로 쓰지 않으므로"), ("better", "good의 불규칙 비교급이므로"), ("best", SUP), ("more good", "good의 비교급은 more good이 아니라 better이므로")], 3)
f476("E", "Jane has ________(더 많은) time than me.", [("much", BASE), ("many", "many는 셀 수 있는 명사에 쓰는 원급이므로"), ("most", SUP), ("the most", SUP), ("more", "much의 불규칙 비교급이므로")], 5)
f476("F", "This road is ________(더 먼) than that one.", [("farther", "far의 불규칙 비교급이므로"), ("far", BASE), ("farthest", SUP), ("farer", "far는 불규칙 변화라 farer로 쓰지 않으므로"), ("more far", "far의 비교급은 more far가 아니라 farther이므로")], 1)

# 4-77 C: 원문항과 같던 문장을 새로
mk(4, 77, "C", [("cold - colder", "첫 빈칸은 than 앞이라 비교급 colder, 둘째 빈칸은 the 뒤라 최상급 coldest를 쓰므로"), ("colder - coldest", "비교급 colder와 최상급 coldest를 바르게 골랐으므로"), ("coldest - colder", "비교급과 최상급의 자리가 바뀌었으므로"),
                ("more cold - most cold", "짧은 단어 cold에는 more, most가 아니라 -er, -est를 붙이므로"), ("colder - most cold", "cold의 최상급은 coldest이므로")], 2,
   "than 앞에는 비교급, the + ~ 자리에는 최상급을 쓴다. 짧은 단어 cold는 colder - coldest로 바뀐다.", "제시문과 정답(hotter - hottest)이 원문항과 똑같았다. 문장을 새로 써서 cold의 비교급·최상급을 묻게 했다.",
   p="Winter is ________(더 추운) than fall.\nJanuary is the ________(가장 추운) month.", okdup=True)

# 4-78 옳은 형태: 원문항 발문과 밑줄, 유형마다 새로
ST478 = "다음 중 밑줄 친 부분의 형태가 어법상 옳은 것을 고르시오."
R478 = "최상급은 짧은 단어에 -est, 긴 단어에 most를 붙이며 둘을 겹쳐 쓰지 않는다. good - best, bad - worst처럼 불규칙 변화도 있다."
S478 = "발문에 ‘표준적인 비교급·최상급 형태를 기준으로’가 붙었고 밑줄이 사라졌으며 오답이 유형마다 같았다. 원문항 발문과 밑줄로 되돌리고 유형마다 새로 썼다."
DOUBLE = "-est와 most를 겹쳐 쓸 수 없으므로"
def f478(t, items, a, s=S478):
    mk(4, 78, t, items, a, R478, s, st=ST478)
f478("B", [("Jane is <u>the prettiest</u> girl here.", "pretty의 최상급 prettiest를 바르게 썼으므로"), ("Tom is <u>more taller</u> than Ben.", "taller에 more를 겹쳐 쓸 수 없으므로"), ("She is <u>the most prettiest</u> singer.", DOUBLE),
           ("He is <u>the goodest</u> player.", "good의 최상급은 불규칙 best이므로"), ("This is <u>the interestingest</u> book.", "긴 단어 interesting은 the most interesting으로 써야 하므로")], 1,
     "발문에 조건이 붙고 밑줄이 사라졌다. 원문항 발문과 밑줄로 되돌렸다. 보기와 정답은 그대로다.")
f478("C", [("This is <u>the most expensivest</u> car.", DOUBLE), ("He is <u>the famousest</u> actor.", "긴 단어 famous는 the most famous로 써야 하므로"), ("Today is <u>the happiest</u> day of my life.", "happy의 최상급 happiest를 바르게 썼으므로"),
           ("She is <u>the most smartest</u> girl.", DOUBLE), ("It was <u>the most hottest</u> day.", DOUBLE)], 3, S478 + " 정답(the most interesting)이 원문항과 같아 새로 썼다.")
f478("D", [("Mina is <u>the most kindest</u> friend.", DOUBLE), ("This is <u>the baddest</u> idea.", "bad의 최상급은 불규칙 worst이므로"), ("He is <u>more stronger</u> than me.", "stronger에 more를 겹쳐 쓸 수 없으므로"),
           ("My dog is <u>the cutest</u> dog in the world.", "cute의 최상급 cutest를 바르게 썼으므로"), ("It is <u>the usefulest</u> book.", "긴 단어 useful은 the most useful로 써야 하므로")], 4)
f478("E", [("He is <u>the most fastest</u> runner.", DOUBLE), ("That was <u>the most boring</u> class.", "긴 단어 boring에 most를 바르게 썼으므로"), ("This is <u>the goodest</u> cake.", "good의 최상급은 불규칙 best이므로"),
           ("She is <u>the carefulest</u> driver.", "긴 단어 careful은 the most careful로 써야 하므로"), ("It is <u>the most biggest</u> room.", DOUBLE)], 2)
f478("F", [("It is <u>the most coldest</u> city.", DOUBLE), ("He is <u>the difficultest</u> teacher.", "긴 단어 difficult는 the most difficult로 써야 하므로"), ("This is <u>the most wonderfulest</u> trip.", DOUBLE),
           ("She is <u>more busier</u> than me.", "busier에 more를 겹쳐 쓸 수 없으므로"), ("He is <u>the best</u> player on the team.", "good의 최상급 best를 바르게 썼으므로")], 5)

# 4-79 비교급과 than 설명: 원문항 발문과 밑줄, 그럴듯한 오개념 오답
R479 = "비교급은 짧은 단어에 -er을 붙이고(late → later, tall → taller), 자음 + y는 y를 i로 바꾼다(easy → easier). than은 ‘~보다’라는 뜻으로 비교의 대상을 연결하며 then(그때)과 다르다."
S479 = "원문항 오답은 그럴듯한 오개념(원급 부사로 오해, r만 붙인 비교급, then과 혼동)인데, 변형 오답(‘than은 ~때문에’ 등)은 뻔하고 유형마다 반복되었으며 정답만 제시 문장의 단어를 언급해 눈에 띄었다. 밑줄도 사라졌다. 원문항 발문과 밑줄로 되돌리고 제시 문장에 맞춘 그럴듯한 오개념으로 오답을 유형마다 새로 썼다."
OK79 = "비교급의 형태와 than의 쓰임을 바르게 설명했으므로"
def f479(t, w, p, items, a, s=S479):
    mk(4, 79, t, items, a, R479, s, st=f"다음 문장에서 '{w}'와 'than'의 쓰임에 대한 설명으로 가장 올바른 것은?", p=p)
f479("B", "easier", "This test is <u>easier than</u> the last one.",
     [("'easier'는 'easy'에 단순히 '-er'만 붙여 만든 형태이다.", "자음 + y라 y를 i로 바꾸고 -er을 붙였으므로"), ("'easier'는 '가장 쉬운'이라는 뜻의 최상급이다.", "easier는 ‘더 쉬운’이라는 비교급이므로"), ("'than' 대신 'then'을 써도 뜻이 같다.", "then은 ‘그때’라는 뜻이라 than과 다르므로"),
      ("'easier'는 'easy'의 y를 i로 바꾸고 '-er'을 붙인 비교급이며, 'than'은 비교 대상을 연결한다.", OK79), ("'than' 뒤에는 반드시 사람이 와야 한다.", "than 뒤에는 사물(the last one)도 올 수 있으므로")], 4)
f479("C", "later", "My brother woke up <u>later than</u> me.",
     [("'later'는 'late'의 최상급으로 '가장 늦게'라는 뜻이다.", "later는 ‘더 늦게’라는 비교급이므로"), ("'later'는 'late'에 '-r'을 붙인 비교급으로 '더 늦게'라는 뜻이다.", "-e로 끝나는 late에 -r을 붙인 비교급이 맞으므로"), ("'than'은 '그러고 나서'라는 뜻으로 일의 순서를 나타낸다.", "than은 ‘~보다’라는 뜻이고 ‘그러고 나서’는 then이므로"),
      ("'than' 대신 'that'을 써도 뜻이 같다.", "that은 비교의 대상을 연결하지 못하므로"), ("'later'는 원급 부사로 '늦게'라는 뜻이다.", "later는 late의 비교급이므로")], 2,
     "문장과 정답 설명이 원문항과 같았다. 문장을 새로 쓰고 정답 설명도 원문항(than의 뜻)과 겹치지 않게 비교급의 형태로 바꿨으며, " + S479[S479.index("원문항 발문과"):])
f479("D", "taller", "Tom is <u>taller than</u> Ben.",
     [("'taller'는 'tall'의 최상급이다.", "taller는 비교급이므로"), ("'than' 뒤에는 비교 대상 대신 동사가 와야 한다.", "than 뒤에는 비교 대상(Ben)이 오므로"), ("'taller' 앞에 'more'를 붙여 'more taller'로 써야 더 정확하다.", "-er 비교급에 more를 겹쳐 쓰지 않으므로"),
      ("'than'은 '그때'라는 뜻으로 시간을 나타낸다.", "‘그때’는 then이고 than은 ‘~보다’이므로"), ("'taller'는 'tall'에 '-er'을 붙인 비교급이고, 'than' 뒤의 Ben이 비교 대상이다.", OK79)], 5)
f479("E", "heavier", "This bag is <u>heavier than</u> that one.",
     [("'heavier'는 'heavy'의 y를 i로 바꾸고 '-er'을 붙인 비교급이다.", OK79), ("'heavier'는 'heavy'에 '-ier'만 붙인 최상급이다.", "heavier는 비교급이므로"), ("'than' 뒤의 'that one'은 비교 대상이 아니라 주어이다.", "that one은 비교의 대상이므로"),
      ("'heavier' 대신 'more heavy'를 써도 옳다.", "heavy의 비교급은 heavier이므로"), ("'than'은 '그러므로'라는 뜻이다.", "than은 ‘~보다’라는 뜻이므로")], 1)
f479("F", "faster", "Jane runs <u>faster than</u> Amy.",
     [("'faster'는 형용사 'fast'의 원급이다.", "faster는 비교급이므로"), ("'fast'는 부사이므로 비교급을 'more fast'로 써야 한다.", "부사 fast도 -er을 붙여 faster로 쓰므로"), ("'faster'는 부사 'fast'의 비교급이며, 'than'으로 Amy와 비교한다.", OK79),
      ("'than' 뒤에는 'Amy runs'처럼 반드시 동사까지 써야 한다.", "than 뒤에 비교 대상만 써도 되므로"), ("'faster'는 '가장 빠르게'라는 최상급 표현이다.", "faster는 ‘더 빠르게’라는 비교급이므로")], 3)

# 4-80 옳은 문장으로만 짝: 원문항 형식(<보기> 줄바꿈, 세 개 조합)
ST480 = "다음 <보기> 중 어법상 옳은 문장으로만 짝지어진 것은?"
R480 = "비교급·최상급에는 -er·-est와 more·most를 겹쳐 쓰지 않고, good - better - best, bad - worse - worst 같은 불규칙 변화를 바르게 쓴다."
S480 = "원문항은 옳은 문장 세 개의 조합을 고르는데, 변형은 ‘빠짐없이 모두’ 고르는 형식(2~4개 조합)으로 바뀌었고 <보기> 줄바꿈이 사라졌다. 원문항 발문과 형식(<보기> 줄바꿈, 세 개 조합)으로 되돌렸다."
def f480(t, lines, judge, ok, c, s=S480):
    a = c.index(ok) + 1
    F(4, 80, t, st=ST480, p="<보기>\n" + "\n".join(lines), c=c, a=a, r=R480, pre=["문장별 판정: " + j for j in judge], k=f"어법상 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), okdup=True, s=s + ipos(a))
REF80 = ["(나), (다), (마)", "(가), (나), (다)", "(나), (라), (마)", "(가), (다), (마)", "(다), (라), (마)"]
f480("B", ["(가) This is the most expensive bag.", "(나) Tom is more taller than Ben.", "(다) Jane is happier than Amy.", "(라) It is the worst movie.", "(마) The cat is the most smallest."],
     ["(가) O. 긴 단어 expensive에 most를 썼다.", "(나) X. taller에 more를 겹쳐 쓸 수 없다.", "(다) O. happy의 비교급 happier이다.", "(라) O. bad의 최상급 worst이다.", "(마) X. smallest에 most를 겹쳐 쓸 수 없다."], "(가), (다), (라)",
     ["(가), (나), (다)", "(가), (다), (라)", "(나), (라), (마)", "(가), (다), (마)", "(다), (라), (마)"])
f480("C", ["(가) Mina is the youngest in her family.", "(나) This is the most smallest room.", "(다) Jane is taller than Amy.", "(라) Tom is more better at math.", "(마) This is the most interesting book."],
     ["(가) O. young의 최상급 youngest이다.", "(나) X. smallest에 most를 겹쳐 쓸 수 없다.", "(다) O. tall의 비교급 taller이다.", "(라) X. better에 more를 겹쳐 쓸 수 없다.", "(마) O. 긴 단어 interesting에 most를 썼다."], "(가), (다), (마)", REF80,
     S480 + " (가)(나)가 원문항 문장과 같고 정답 조합도 같아 문장을 새로 썼다.")
f480("D", ["(가) Tom is taller than Ben.", "(나) This is the easiest test.", "(다) Jane is more prettier.", "(라) He is the best player.", "(마) Today is more hotter than yesterday."],
     ["(가) O. tall의 비교급 taller이다.", "(나) O. easy의 최상급 easiest이다.", "(다) X. prettier에 more를 겹쳐 쓸 수 없다.", "(라) O. good의 최상급 best이다.", "(마) X. hotter에 more를 겹쳐 쓸 수 없다."], "(가), (나), (라)",
     ["(가), (나), (라)", "(가), (다), (마)", "(나), (다), (마)", "(나), (라), (마)", "(다), (라), (마)"])
f480("E", ["(가) This bag is more heavier than that one.", "(나) Jane is the most beautiful.", "(다) Tom is gooder than Ben.", "(라) This is the worst day.", "(마) The dog is bigger than the cat."],
     ["(가) X. heavier에 more를 겹쳐 쓸 수 없다.", "(나) O. 긴 단어 beautiful에 most를 썼다.", "(다) X. good의 비교급은 better이다.", "(라) O. bad의 최상급 worst이다.", "(마) O. big의 비교급 bigger이다."], "(나), (라), (마)", REF80)
f480("F", ["(가) Seoul is larger than Busan.", "(나) Tom is the fastest.", "(다) Jane is the most kindest.", "(라) This test is more easier.", "(마) He is better than me."],
     ["(가) O. large의 비교급 larger이다.", "(나) O. fast의 최상급 fastest이다.", "(다) X. kindest에 most를 겹쳐 쓸 수 없다.", "(라) X. easier에 more를 겹쳐 쓸 수 없다.", "(마) O. good의 비교급 better이다."], "(가), (나), (마)",
     ["(나), (다), (마)", "(가), (나), (다)", "(나), (라), (마)", "(가), (다), (마)", "(가), (나), (마)"])
