# 3급 CH11 비교 (101~110) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def talk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 옳지 않은 설명이다. 따라서 정답이다." if i + 1 == a else " 옳은 설명이다. 따라서 오답이다.")) if w.endswith("므로") else (w + (" 옳지 않은 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.")) for i, (_, w) in enumerate(items)], k=items[a-1][1], s=s + ipos(a), **kw)
BL = "(<u>                   </u>)"

# 3-101 원급·비교급·최상급: 원문항 발문, 같은 원급 반복 없이 유형마다 새 묶음
ST101 = "다음 단어의 원급, 비교급, 최상급이 잘못 연결된 것을 고르시오."
R101 = "비교급·최상급은 보통 -er·-est를 붙이고(단모음 + 단자음은 자음을 겹쳐 쓰고, 자음 + y는 y를 i로 바꾼다), 긴 단어는 more·most를 앞에 쓴다. good·well - better - best, bad - worse - worst, many·much - more - most, little - less - least는 불규칙 변화이다."
S101 = "발문에 ‘표준적인 기본 의미’와 little·bad의 뜻 설명이 붙었고, 같은 원급이 옳은 형태와 틀린 형태로 두 번 나와 단서가 되었으며, 옳은 묶음(little - less - least 등)이 유형마다 반복되었다. 원문항 발문으로 되돌리고, 같은 원급이 두 번 나오지 않게 유형마다 묶음을 새로 썼다."
REG = "규칙 변화(-er, -est)를 바르게 연결했으므로"
DBL = "단모음 + 단자음으로 끝나 자음을 겹쳐 쓴 형태로 바르게 연결했으므로"
YI = "자음 + y로 끝나 y를 i로 바꾸고 -er, -est를 붙인 형태로 바르게 연결했으므로"
MM = "긴 단어라 more, most를 앞에 쓴 형태로 바르게 연결했으므로"
IRR = "불규칙 변화를 바르게 연결했으므로"
def f101(t, items, a, s=S101):
    mk(3, 101, t, items, a, R101, s, st=ST101, okdup=True)
f101("B", [("happy - happier - happiest", YI), ("big - biger - bigest", "단모음 + 단자음으로 끝나는 big은 g를 겹쳐 bigger - biggest로 써야 하므로"), ("good - better - best", IRR),
           ("beautiful - more beautiful - most beautiful", MM), ("little - less - least", IRR)], 2)
f101("C", [("hot - hotter - hottest", DBL), ("useful - more useful - most useful", MM), ("bad - worse - worst", IRR), ("heavy - heavier - heaviest", YI), ("good - gooder - goodest", "good은 불규칙 변화라 better - best로 써야 하므로")], 5)
f101("D", [("busy - busyer - busyest", "자음 + y로 끝나는 busy는 y를 i로 바꿔 busier - busiest로 써야 하므로"), ("many - more - most", IRR), ("thin - thinner - thinnest", DBL),
           ("important - more important - most important", MM), ("large - larger - largest", "-e로 끝나 -r, -st만 붙인 형태로 바르게 연결했으므로")], 1)
f101("E", [("wet - wetter - wettest", DBL), ("much - more - most", IRR), ("well - weller - wellest", "well은 불규칙 변화라 better - best로 써야 하므로"), ("pretty - prettier - prettiest", YI),
           ("difficult - more difficult - most difficult", MM)], 3)
f101("F", [("sad - sadder - saddest", DBL), ("bad - worse - worst", IRR), ("nice - nicer - nicest", "-e로 끝나 -r, -st만 붙인 형태로 바르게 연결했으므로"),
           ("interesting - interestinger - interestingest", "긴 단어 interesting은 more interesting - most interesting으로 써야 하므로"), ("early - earlier - earliest", YI)], 4)

# 3-102 B: 원문항과 같던 표를 새로
mk(3, 102, "B", [("Minsu is as old as Jiho.", "두 사람 모두 15살이라 표와 일치하므로"), ("Jiho is taller than Minsu.", "Jiho(172cm)가 Minsu(168cm)보다 커서 표와 일치하므로"), ("Minsu is heavier than Jiho.", "Minsu(58kg)가 Jiho(52kg)보다 무거워 표와 일치하므로"),
                 ("Jiho is lighter than Minsu.", "Jiho(52kg)가 Minsu(58kg)보다 가벼워 표와 일치하므로"), ("Minsu is taller than Jiho.", "Minsu(168cm)는 Jiho(172cm)보다 작아 표와 일치하지 않으므로")], 5,
   "비교급 + than은 두 대상의 차이를, as + 원급 + as는 두 대상이 같음을 나타낸다.", "표(Tom, Jerry)와 정답이 원문항과 똑같았다. 인물과 수치를 새로 쓰고 정답을 키 비교로 바꿨다.",
   p="Name\tMinsu\tJiho\nAge\t15\t15\nWeight\t58kg\t52kg\nHeight\t168cm\t172cm")

# 3-104 one of the + 복수명사 / any other + 단수명사 / 수량 비교급: 원문항 발문
ST104 = "다음 빈칸에 들어갈 단어를 바르게 짝지은 것을 고르시오."
R104 = "one of the + 최상급 뒤에는 복수명사, 비교급 + than any other 뒤에는 단수명사를 쓴다. than 앞의 수량 비교급은 셀 수 없는 명사에 less, 셀 수 있는 명사에 fewer·more를 쓴다."
S104 = "발문이 ‘one of the 뒤에는 복수명사, any other 뒤에는 단수명사, 마지막은 수량의 비교급’이라고 세 빈칸의 규칙을 모두 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def n104(ch, good):
    xs = [x.strip() for x in ch.split(" - ")]; gs = [x.strip() for x in good.split(" - ")]
    if xs == gs: return "one of the 뒤 복수명사, any other 뒤 단수명사, than 앞 비교급을 모두 바르게 골랐으므로"
    bits = []
    if xs[0] != gs[0]: bits.append(f"첫째 빈칸: one of the 뒤에는 복수명사({gs[0]})를 쓴다")
    if xs[1] != gs[1]: bits.append(f"둘째 빈칸: any other 뒤에는 단수명사({gs[1]})를 쓴다")
    if xs[2] != gs[2]: bits.append(f"셋째 빈칸: fewer는 셀 수 있는 명사에 쓰는데 water는 셀 수 없는 명사라 {gs[2]}를 쓴다" if xs[2] in ("fewer",) else f"셋째 빈칸: than 앞에는 원급({xs[2]})이 아니라 비교급({gs[2]})을 쓴다")
    return ", ".join(bits) + ". 따라서"
c104 = ["runners - dress - less", "runner - dress - less", "runners - dresses - little", "runners - dresses - fewer", "runner - dresses - little"]
mk(3, 104, "B", [(x, n104(x, c104[0])) for x in c104], 1, R104, "앞의 두 문장이 원문항과 같았고 발문이 세 빈칸의 규칙을 알려 주었다. 문장을 새로 쓰고 원문항 발문으로 되돌렸다.", st=ST104,
   p="Minho is one of the fastest ______ in our school.\nThis dress is prettier than any other ____ in the shop.\nI drink ______ water than my sister.", okdup=True)
for t in "CDEF": F(3, 104, t, st=ST104, s=S104)

# 3-105 설명문 빈칸에 문법 용어: 원문항 형식(ⓐ·ⓑ 두 문장 + 설명문)
ST105 = "빈칸 (A)와 (B)에 들어갈 말을 바르게 짝지은 것은?"
R105 = "비교급은 much·even·far로 강조하고 very로는 강조하지 않는다. as ~ as 사이에는 원급, than 앞에는 비교급, the ~ in·of 구문에는 최상급을 쓰며, -er·-est에 more·most를 겹쳐 쓰지 않는다."
S105 = "원문항은 설명문 속 빈칸 (A)(B)에 문법 용어(원급·비교급·최상급)를 넣는 형식인데, 변형은 두 문장의 오류를 설명한 문장을 고르는 형식으로 바뀌었고 오답(‘둘 다 시제 오류’ 등)이 뻔하고 유형마다 반복되었다. 원문항 발문과 형식(ⓐ·ⓑ 두 문장 + 설명문 빈칸)으로 되돌리고, 유형마다 정답 조합을 달리했다."
BA, BB = "(<u>      A      </u>)", "(<u>      B      </u>)"
def n105(ch, good, why):
    xs = re.findall(r"\([AB]\) ([^,\s]+)", ch); gs = re.findall(r"\([AB]\) ([^,\s]+)", good)
    if xs == gs: return f"(A)는 {gs[0]}, (B)는 {gs[1]}이 들어가 설명이 바르게 완성되므로"
    bits = [f"({L})에는 {x}이 아니라 {g}이 들어간다({w})" for L, x, g, w in zip("AB", xs, gs, why) if x != g]
    return ", ".join(bits) + ". 따라서"
def f105(t, s1, s2, expl, c, a, why, s=S105):
    p = f"ⓐ {s1}\nⓑ {s2}\n[설명]\n{expl}"
    mk(3, 105, t, [(x, n105(x, c[a-1], why)) for x in c], a, R105, s, st=ST105, p=p, okdup=True)
f105("B", "This room is <u>very bigger</u> than mine.", "Jane is <u>the most kindest</u> girl in our class.",
     f"문장 ⓐ에서 'very'는 {BA}을/를 수식할 수 없으므로, 'much'나 'far' 등으로 고쳐야 한다. 문장 ⓑ에서 'kindest'는 이미 단어 자체에 {BB}의 의미가 포함되어 있으므로 'most'를 중복해서 사용하지 않아야 한다.",
     ["(A) 원급, (B) 비교급", "(A) 비교급, (B) 최상급", "(A) 최상급, (B) 원급", "(A) 비교급, (B) 비교급", "(A) 원급, (B) 최상급"], 2,
     ["very는 비교급 bigger를 꾸밀 수 없다", "kindest는 -est가 붙은 최상급이다"],
     "두 문장이 원문항과 같았고 형식도 바뀌었다. 문장을 새로 쓰고 원문항 발문과 형식(ⓐ·ⓑ 두 문장 + 설명문 빈칸)으로 되돌렸으며 정답 조합을 (A) 비교급, (B) 최상급으로 바꿨다.")
f105("C", "He is <u>as taller as</u> his father.", "This is <u>the most easiest</u> question.",
     f"문장 ⓐ에서 as ~ as 사이에는 {BA}을/를 써야 하므로 'taller'를 'tall'로 고쳐야 한다. 문장 ⓑ에서 'easiest'는 이미 단어 자체에 {BB}의 의미가 포함되어 있으므로 'most'를 중복해서 사용하지 않아야 한다.",
     ["(A) 비교급, (B) 비교급", "(A) 최상급, (B) 비교급", "(A) 비교급, (B) 원급", "(A) 원급, (B) 최상급", "(A) 최상급, (B) 최상급"], 4,
     ["as ~ as 사이에는 원급을 쓴다", "easiest는 -est가 붙은 최상급이다"])
f105("D", "He is <u>the tall</u> boy in his class.", "This book is <u>most interesting</u> than that one.",
     f"문장 ⓐ에서 'the'와 'in his class'가 있으므로 'tall'을 {BA} 형태인 'tallest'로 고쳐야 한다. 문장 ⓑ에서 뒤에 'than'이 있으므로 'most interesting'을 {BB} 형태인 'more interesting'으로 고쳐야 한다.",
     ["(A) 최상급, (B) 비교급", "(A) 비교급, (B) 최상급", "(A) 원급, (B) 비교급", "(A) 최상급, (B) 원급", "(A) 비교급, (B) 비교급"], 1,
     ["the ~ in his class에는 최상급을 쓴다", "than 앞에는 비교급을 쓴다"])
f105("E", "Tom runs <u>as faster as</u> Ben.", "My room is <u>more cleaner</u> than yours.",
     f"문장 ⓐ에서 as ~ as 사이에는 {BA}을/를 써야 하므로 'faster'를 'fast'로 고쳐야 한다. 문장 ⓑ에서 'cleaner'는 이미 단어 자체에 {BB}의 의미가 포함되어 있으므로 'more'를 중복해서 사용하지 않아야 한다.",
     ["(A) 비교급, (B) 원급", "(A) 최상급, (B) 비교급", "(A) 원급, (B) 최상급", "(A) 비교급, (B) 비교급", "(A) 원급, (B) 비교급"], 5,
     ["as ~ as 사이에는 원급을 쓴다", "cleaner는 -er이 붙은 비교급이다"])
f105("F", "Seoul is <u>the most big</u> city in Korea.", "Jane is not <u>so tallest as</u> Amy.",
     f"문장 ⓐ에서 'big'의 {BA}은/는 'most'를 붙이지 않고 'biggest'로 써야 한다. 문장 ⓑ에서 so ~ as 사이에는 {BB}을/를 써야 하므로 'tallest'를 'tall'로 고쳐야 한다.",
     ["(A) 원급, (B) 원급", "(A) 비교급, (B) 최상급", "(A) 최상급, (B) 원급", "(A) 원급, (B) 비교급", "(A) 최상급, (B) 비교급"], 3,
     ["the ~ in Korea에는 최상급 biggest를 쓴다", "so ~ as 사이에는 원급을 쓴다"])

# 3-106 비교급 형태: 원문항처럼 대화, 실제로 있는 형태의 오답
R106 = "than 앞에는 비교급을 쓴다. good - better, bad - worse, many·much - more, little - less, far - farther는 불규칙 변화이고, easy처럼 자음 + y로 끝나면 y를 i로 바꿔 -er을 붙인다."
S106 = "오답 네 개가 모두 없는 형태(betterer, moreer 등)여서 쉽게 지워졌고, 발문은 ‘대화’인데 제시문이 한 문장이었다. 원문항처럼 대화로 바꾸고, 오답을 원급·부사·최상급 같은 실제 형태로 바꿨다."
BASE = "than 앞에는 원급을 쓸 수 없으므로"; SUP = "than과 함께 최상급을 쓸 수 없으므로"
def f106(t, p, items, a, s=S106):
    mk(3, 106, t, items, a, R106, s, p=p, okdup=True)
f106("B", "A: How was the test?\nB: It was ______(easy) than I thought.", [("easy", BASE), ("easily", "be동사 뒤 보어 자리에 부사를 쓸 수 없고 비교급도 아니므로"), ("easiest", SUP), ("more easy", "easy의 비교급은 more easy가 아니라 easier이므로"), ("easier", "than 앞에 easy의 비교급 easier를 바르게 썼으므로")], 5,
     "대화와 정답(worse)이 원문항과 똑같았고 오답도 없는 형태였다. 대화를 새로 쓰고 오답을 실제로 있는 형태로 바꿨다.")
f106("C", "A: Which book do you like?\nB: This book is ______(good) than that one.", [("better", "than 앞에 good의 비교급 better를 바르게 썼으므로"), ("good", BASE), ("well", "well은 부사이고 비교급도 아니므로"), ("best", SUP), ("more good", "good은 불규칙 변화라 비교급이 better이므로")], 1)
f106("D", "A: Does Jane have a lot of friends?\nB: Yes. She has ______(many) friends than Tom.", [("many", BASE), ("much", "셀 수 있는 명사 friends에 much를 쓸 수 없고 비교급도 아니므로"), ("most", SUP), ("more", "than 앞에 many의 비교급 more를 바르게 썼으므로"), ("the most", SUP)], 4)
f106("E", "A: Are you busy today?\nB: Not really. I have ______(little) homework than yesterday.", [("little", BASE), ("less", "than 앞에 little의 비교급 less를 바르게 썼으므로"), ("least", SUP), ("a little", "a little은 비교급이 아니므로"), ("fewer", "fewer는 셀 수 있는 명사에 쓰는데 homework는 셀 수 없는 명사이므로")], 2)
f106("F", "A: How far is the new school?\nB: It is ______(far) than the old one.", [("far", BASE), ("farthest", SUP), ("farther", "than 앞에 far의 비교급 farther를 바르게 썼으므로"), ("more far", "far는 불규칙 변화라 비교급이 farther이므로"), ("the farthest", SUP)], 3)

# 3-107 빈칸 밑줄 복원
for t in "BCDEF":
    F(3, 107, t, p=re.sub(r"\(\s*\)", BL, V(3, 107, t)["passage"]), s="원문항의 빈칸 밑줄이 괄호로 바뀌었다. 원문항처럼 밑줄 빈칸으로 되돌렸다. 보기와 정답은 그대로다.")

# 3-108 one of the + 최상급 + 복수명사 배열: 원문항 발문, 주어 없는 오답을 형태 오류로
ST108 = "R"  # 고친 원문항 발문(형태 변화 조건 포함)
R108 = "‘가장 ~한 것 중 하나’는 one of the + 최상급 + 복수명사로 쓴다. 짧은 단어는 -est, 긴 단어는 most를 붙이며 둘을 겹쳐 쓰지 않는다."
S108 = "발문에 ‘필요한 경우 형용사의 비교 형태와 명사의 단복수 형태를 바꿀 수 있다’는 조건이 붙어 바꿀 곳을 짚어 주었고, 주어를 뺀 오답은 형식만으로 지워졌다. 원문항 발문(‘필요하면 단어의 형태를 바꿀 것’)으로 되돌리고 주어 없는 오답을 비교 형태 오류로 바꿨다."
OK108 = "one of the + 최상급 + 복수명사로 바르게 배열했으므로"; SG = "one of the 뒤에는 복수명사를 쓰므로"; CMP = "‘가장 ~한’은 비교급이 아니라 최상급으로 쓰므로"; THE1 = "the는 one 앞이 아니라 최상급 앞에 쓰므로"
def f108(t, items, a, s=S108, **kw):
    mk(3, 108, t, items, a, R108, s, st=ST108, **kw)
f108("B", [("This is one of the oldest building in our town.", SG), ("This is one of the older buildings in our town.", CMP), ("This is the one of oldest buildings in our town.", THE1),
           ("This is one of the oldest buildings in our town.", OK108), ("This is one of the most old buildings in our town.", "old는 짧은 단어라 most old가 아니라 oldest로 쓰므로")], 4,
     "우리말·단어·정답이 원문항과 똑같았고 발문 조건도 붙었다. 문장을 새로 쓰고 원문항 발문으로 되돌렸다.", p="이것은 우리 동네에서 가장 오래된 건물 중 하나이다.\n( this / is / one / of / the / old / building / in / our / town / . )")
f108("C", [("Tom is one of the tallest student in our class.", SG), ("Tom is one of the taller students in our class.", CMP), ("Tom is one of the tallest students in our class.", OK108),
           ("Tom is one of the most tall students in our class.", "tall은 짧은 단어라 most tall이 아니라 tallest로 쓰므로"), ("Tom is the one of tallest students in our class.", THE1)], 3)
f108("D", [("This is one of the most expensive bag in the store.", SG), ("This is one of the most expensive bags in the store.", OK108), ("This is one of the more expensive bags in the store.", CMP),
           ("This is one of the expensivest bags in the store.", "expensive는 긴 단어라 -est가 아니라 most를 붙이므로"), ("This is the one of most expensive bags in the store.", THE1)], 2)
f108("E", [("Jane is one of the faster players on the team.", CMP), ("Jane is the one of fastest players on the team.", THE1), ("Jane is one of the most fast players on the team.", "fast는 짧은 단어라 most fast가 아니라 fastest로 쓰므로"),
           ("Jane is one of the fastest player on the team.", SG), ("Jane is one of the fastest players on the team.", OK108)], 5)
f108("F", [("Busan is one of the largest city in Korea.", SG), ("Busan is one of the largest cities in Korea.", OK108), ("Busan is one of the larger cities in Korea.", CMP),
           ("Busan is the one of largest cities in Korea.", THE1), ("Busan is one of the most large cities in Korea.", "large는 짧은 단어라 most large가 아니라 largest로 쓰므로")], 2)

# 3-109 옳지 않은 설명: 원문항 밑줄, 유형마다 문장과 설명을 새로
ST109 = "다음 문장에 대한 설명으로 옳지 않은 것은?"
R109 = "비교급은 much·even·far·still·a lot·a little로 강조하거나 정도를 나타내고, very·so로는 비교급을 꾸미지 않는다. 짧은 단어는 -er, 긴 단어는 more를 붙이며 둘을 겹쳐 쓰지 않는다."
S109 = "옳은 설명(than은 비교 대상을 연결, very는 원급 강조 등)이 유형마다 반복되고, 틀린 설명이 그와 반대되는 설명과 함께 있어 단서가 되었으며 밑줄도 사라졌다. 원문항 발문과 밑줄로 되돌리고 유형마다 설명을 새로 썼다."
def f109(t, p, items, a, s=S109):
    talk(3, 109, t, items, a, R109, s, st=ST109, p=p)
f109("B", "My brother is <u>even stronger than</u> my father.",
     [("'stronger'는 'strong'에 '-er'을 붙인 비교급이다.", "짧은 단어 strong에 -er을 붙인 비교급이라"), ("'even'은 ‘훨씬’이라는 뜻으로 비교급 'stronger'를 강조한다.", "even은 비교급을 강조하므로"),
      ("'than' 뒤에는 비교하는 대상인 'my father'가 온다.", "than 뒤에 비교 대상이 오므로"), ("'stronger' 대신 'more strong'을 써도 같은 뜻의 옳은 문장이다.", "strong의 비교급은 stronger이고 more strong으로 쓰지 않으므로"),
      ("'even' 자리에 'a lot'을 써도 비교급을 강조할 수 있다.", "a lot도 비교급을 강조하므로")], 4,
     "문장과 틀린 설명(much 대신 very 가능)이 원문항과 같았다. 문장과 설명을 새로 쓰고 원문항처럼 밑줄을 넣었다.")
f109("C", "Tom is <u>far taller than</u> Ben.",
     [("'far'는 거리를 나타낼 뿐이라 비교급 'taller'를 강조할 수 없다.", "far는 비교급 앞에서 ‘훨씬’이라는 뜻으로 비교급을 강조하므로"), ("'taller'는 형용사 'tall'의 비교급으로 주어 Tom을 설명한다.", "taller는 주어를 설명하는 비교급이므로"),
      ("'far' 자리에 'much'를 써도 문법적으로 옳다.", "much도 비교급을 강조하므로"), ("이 문장은 Tom이 Ben보다 키가 훨씬 크다는 뜻이다.", "far taller는 ‘훨씬 더 큰’이라는 뜻이므로"), ("'than Ben'은 비교의 대상을 나타낸다.", "than 뒤에 비교 대상이 오므로")], 1)
f109("D", "This question is <u>a little more difficult than</u> the last one.",
     [("'a little'은 비교급 앞에서 ‘조금 더’라는 뜻을 나타낸다.", "a little은 비교급 앞에서 정도를 나타내므로"), ("'difficult'는 긴 단어라 '-er' 대신 앞에 'more'를 쓴다.", "긴 단어는 more를 앞에 쓰므로"),
      ("'a little' 대신 'very'를 써서 ‘매우 더 어렵다’는 뜻을 나타낼 수 있다.", "very는 비교급을 꾸미지 않으므로"), ("'the last one'의 'one'은 앞의 'question'을 대신한다.", "one은 앞에 나온 명사를 대신하므로"),
      ("'more difficult'를 'difficulter'로 쓸 수 없다.", "긴 단어 difficult에는 -er을 붙이지 않으므로")], 3)
f109("E", "This bag is <u>much heavier than</u> that one.",
     [("'heavier'는 'heavy'의 y를 i로 바꾸고 '-er'을 붙인 비교급이다.", "자음 + y로 끝나 y를 i로 바꾼 비교급이라"), ("'much'는 비교급을 강조하여 ‘훨씬’이라는 뜻을 나타낸다.", "much는 비교급을 강조하므로"),
      ("'that one'은 'that bag'을 뜻한다.", "one은 앞의 bag을 대신하므로"), ("'much' 자리에 'still'을 써도 비교급을 강조할 수 있다.", "still도 비교급을 강조하므로"),
      ("'much heavier'는 'more heavier'로 바꿔 써도 같은 뜻이다.", "-er 비교급에 more를 겹쳐 쓰지 않으므로")], 5)
f109("F", "The test was <u>even easier than</u> the last one.",
     [("'easier'는 'easy'의 비교급으로, 'more easy'로 쓰지 않는다.", "easy의 비교급은 easier이므로"), ("'even' 대신 'so'를 써도 비교급을 강조할 수 있다.", "so는 비교급을 꾸미지 않으므로"),
      ("'even'은 비교급 앞에서 ‘훨씬’이라는 뜻으로 쓰였다.", "even은 비교급을 강조하므로"), ("이 문장은 지난번 시험보다 이번 시험이 훨씬 더 쉬웠다는 뜻이다.", "even easier는 ‘훨씬 더 쉬운’이라는 뜻이므로"),
      ("'than' 뒤의 'the last one'은 지난번 시험을 가리킨다.", "one은 앞의 test를 대신하므로")], 2)

# 3-110 글 속 밑줄 문장 고치기: 원문항 형식(짧은 글 + 밑줄 문장)
ST110 = "다음 글에서 밑줄 친 문장을 어법상 올바르게 고친 것은?"
R110 = "than 앞에는 비교급, the ~ of 구문에는 최상급을 쓴다. 짧은 단어는 -er·-est를 붙이고 more·most를 겹쳐 쓰지 않으며, very는 비교급을 꾸미지 않는다."
S110 = "원문항은 글 속 밑줄 친 문장을 고치는 형식인데, 변형은 글 없이 한 문장만 주고 발문이 ‘비교급/최상급 의미를 유지하면서 어미를 변화시킨’이라고 고치는 방법을 알려 주었다. 원문항 발문과 형식(짧은 글 속 밑줄 문장)으로 되돌렸다."
def f110(t, p, items, a, s=S110):
    mk(3, 110, t, items, a, R110, s, st=ST110, p=p)
f110("B", "Last Sunday, I visited two libraries in my town. The old library was small and dark. <u>But the new library was more bigger than the old one</u>. It also had many new books.",
     [("But the new library was biggest than the old one.", "than 앞에는 최상급이 아니라 비교급을 쓰므로"), ("But the new library was very big than the old one.", "than 앞에는 원급이 아니라 비교급을 쓰므로"), ("But the new library was bigger than the old one.", "big의 비교급 bigger로 바르게 고쳤으므로"),
      ("But the new library was big than the old one.", "than 앞에는 원급이 아니라 비교급을 쓰므로"), ("But the new library was more big than the old one.", "big은 짧은 단어라 more big이 아니라 bigger로 쓰므로")], 3,
     "문장과 정답(cheaper than)이 원문항과 같았고 발문이 고치는 방법을 알려 주었다. 원문항처럼 짧은 글 속 밑줄 문장으로 새로 쓰고 원문항 발문으로 되돌렸다.")
f110("C", "Our class had a running race yesterday. Tom, Ben, and Mike ran very fast. <u>Tom was the most fastest runner of the three</u>. He won a gold medal.",
     [("Tom was the faster runner of the three.", "셋 중 가장 빠른 사람은 최상급으로 나타내므로"), ("Tom was the fastest runner of the three.", "fast의 최상급 fastest로 바르게 고쳤으므로"), ("Tom was the most fast runner of the three.", "fast는 짧은 단어라 most fast가 아니라 fastest로 쓰므로"),
      ("Tom was the very fast runner of the three.", "very fast는 최상급이 아니므로"), ("Tom was faster runner of the three.", "셋 중 가장 빠른 사람은 the + 최상급으로 나타내므로")], 2)
f110("D", "Jane and Amy got their test results today. Amy's score was good, but Jane's score was even better. <u>So Jane was more happier than Amy</u>. She smiled all day.",
     [("So Jane was happiest than Amy.", "than 앞에는 최상급이 아니라 비교급을 쓰므로"), ("So Jane was very happy than Amy.", "than 앞에는 원급이 아니라 비교급을 쓰므로"), ("So Jane was happy than Amy.", "than 앞에는 원급이 아니라 비교급을 쓰므로"),
      ("So Jane was happier than Amy.", "happy의 비교급 happier로 바르게 고쳤으므로"), ("So Jane was happily than Amy.", "be동사 뒤 보어 자리에 부사를 쓸 수 없으므로")], 4)
f110("E", "We took a math test this morning. There were twenty questions on it. <u>Question 1 was the most easiest question of all</u>. But the last one was very hard.",
     [("Question 1 was the easiest question of all.", "easy의 최상급 easiest로 바르게 고쳤으므로"), ("Question 1 was the easier question of all.", "of all(모든 것 중)에는 최상급을 쓰므로"), ("Question 1 was the very easy question of all.", "very easy는 최상급이 아니므로"),
      ("Question 1 was the most easy question of all.", "easy의 최상급은 most easy가 아니라 easiest이므로"), ("Question 1 was easier question of all.", "of all에는 the + 최상급을 쓰므로")], 1)
f110("F", "I packed my bag for the school trip. My friend Minsu packed his bag, too. <u>My bag was more heavier than his</u>. I had too many clothes in it.",
     [("My bag was heaviest than his.", "than 앞에는 최상급이 아니라 비교급을 쓰므로"), ("My bag was very heavy than his.", "than 앞에는 원급이 아니라 비교급을 쓰므로"), ("My bag was heavy than his.", "than 앞에는 원급이 아니라 비교급을 쓰므로"),
      ("My bag was more heavy than his.", "heavy의 비교급은 more heavy가 아니라 heavier이므로"), ("My bag was heavier than his.", "heavy의 비교급 heavier로 바르게 고쳤으므로")], 5)

# ---- 2차 감수(2026-10) 추가 ----
# 3-104 E: 둘째 문장이 원문항 문장(This computer is newer than any other ~ in the store)과 명사만 다름 → 새로
FIX.pop((3, 104, "E"), None)
c104e = V(3, 104, "E")["c"]
mk(3, 104, "E", [(x, n104(x, c104e[1])) for x in c104e], 2, R104, S104.replace(" 보기와 정답은 그대로다.", "") + " 둘째 문장이 원문항 문장에서 명사만 바꾼 것이어서(This computer/phone is newer than any other ~ in the store) 형용사를 바꿔 새로 썼다. 보기와 정답은 그대로다.",
   st=ST104, p="He is one of the tallest ______ on the team.\nThis phone is more expensive than any other ____ in the store.\nJane has ______ friends than Amy.")

# 3-108 D: 없는 낱말(expensivest) 오답 → the를 뺀 오답 / F: 원문항 문장과 도시 이름만 다름 → 새로
FIX.pop((3, 108, "D"), None); FIX.pop((3, 108, "F"), None)
NOTHE = "최상급 앞에 the가 빠졌으므로"
f108("D", [("This is one of the most expensive bag in the store.", SG), ("This is one of the most expensive bags in the store.", OK108), ("This is one of the more expensive bags in the store.", CMP),
           ("This is one of most expensive bags in the store.", NOTHE), ("This is the one of most expensive bags in the store.", THE1)], 2)
f108("F", [("The Han River is one of the longest river in Korea.", SG), ("The Han River is one of the longest rivers in Korea.", OK108), ("The Han River is one of the longer rivers in Korea.", CMP),
           ("The Han River is the one of longest rivers in Korea.", THE1), ("The Han River is one of the most long rivers in Korea.", "long은 짧은 단어라 most long이 아니라 longest로 쓰므로")], 2,
     S108 + " 또 문장이 원문항(서울은 세계에서 가장 큰 도시 중 하나이다)에서 도시 이름만 바꾼 것이어서 새 문장으로 썼다.", p="한강은 한국에서 가장 긴 강 중 하나이다.\n( the Han River / is / one / of / the / long / river / in / Korea / . )")
