# 6급 CH1 명사의 수·관사 (1~10) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."

# 원문항 발문으로만 되돌리는 문항
for t in "EF": F(6, 1, t, st="R", s="발문에 mouse의 뜻 설명이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDEF": F(6, 2, t, st="R", xr=[("종류·주문 단위를 세는 특수 용법은 이 문항의 범위에서 제외한다.", "a coffee처럼 주문 단위를 세는 특수한 쓰임은 따로 익힌다."), ("이 문항에서 불가산명사이다", "셀 수 없는 명사이다")], s="발문에 ‘(물질·추상명사는 일반적인 불가산 용법으로 판단한다.)’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDF": F(6, 7, t, st="R", s="발문에 ‘(음식·물질·음악은 … 일반적인 뜻으로 쓴다.)’가 붙어 셀 수 없는 명사라는 정답 근거를 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
F(6, 8, "D", st="R", s="발문에 ‘man의 복수형을 넣어’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 6-3 관사가 잘못된 것: 원문항 발문, 세상에 하나뿐인 대상 + 같은 명사 반복 없이
R603 = "세상에 하나뿐인 대상(the sun, the moon, the sky, the world, the Earth)과 서로 알고 있는 특정 대상 앞에는 the를 쓴다. 처음 말하는 셀 수 있는 단수명사 앞에는 첫소리에 따라 a/an을 쓴다."
S603 = "발문에 ‘(sun, moon, Earth는 … 가리킨다.)’가 붙어 정답이 들어 있는 문장을 알려 주었고, 같은 명사가 옳은 관사와 틀린 관사로 두 번 나오기도 했다. 원문항 발문으로 되돌리고, 같은 명사가 반복되지 않게 유형마다 새로 썼다."
UNI = lambda w: f"세상에 하나뿐인 {w} 앞에는 the를 써야 하므로"
A_ = "처음 말하는 셀 수 있는 단수명사 앞에 첫소리에 맞는 a/an을 바르게 썼으므로"; THE_ = "서로 알고 있는 특정 대상 앞에 the를 바르게 썼으므로"
def f603(t, items, a, s=S603):
    mk(6, 3, t, items, a, R603, s, st="R")
F(6, 3, "B", st="R", r=R603, n=[A_ + " 오답이다.", THE_ + " 오답이다.", "하늘에 떠 있는 특정한 별들을 가리켜 the를 바르게 썼으므로 오답이다.", UNI("태양(sun)") + " 정답이다.", A_ + " 오답이다."],
  s="발문에 ‘(sun, moon, Earth는 … 가리킨다.)’가 붙어 정답이 들어 있는 문장을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f603("C", [("He opened <u>the</u> window.", THE_), ("She has <u>an</u> uncle in Canada.", A_), ("He traveled around <u>a</u> world.", UNI("세계(world)")), ("I want <u>a</u> glass of water.", A_), ("<u>The</u> boys are playing soccer.", THE_)], 3)
f603("D", [("I found <u>a</u> coin on the street.", A_), ("We looked up at <u>a</u> sky.", UNI("하늘(sky)")), ("<u>The</u> sun rises in the east.", "세상에 하나뿐인 태양 앞에 the를 바르게 썼으므로"), ("Tom ate <u>an</u> apple.", A_), ("<u>The</u> cat on the sofa is mine.", THE_)], 2)
f603("E", [("My dad is <u>a</u> teacher.", A_), ("Look at <u>the</u> moon! It's so bright.", "세상에 하나뿐인 달 앞에 the를 바르게 썼으므로"), ("I need <u>an</u> eraser.", A_), ("<u>The</u> flowers in the vase are pretty.", THE_), ("<u>A</u> sun is very hot today.", UNI("태양(sun)"))], 5)
f603("F", [("Many stars are shining in <u>a</u> sky.", UNI("하늘(sky)")), ("She plays <u>the</u> piano well.", "악기 이름 앞에 the를 바르게 썼으므로"), ("I have <u>a</u> sister.", A_), ("<u>An</u> owl is sitting on the branch.", A_), ("I read <u>an</u> interesting book.", A_)], 1)

# 6-4 관사 짝: 원문항 발문, 정답 조합을 원문항(An - The)과 다르게
R604 = "처음 소개하는 셀 수 있는 단수명사 앞에는 a/an(첫소리가 모음 소리면 an)을 쓰고, 앞에서 말한 같은 대상은 the로 나타낸다."
S604 = "정답 조합(An - The)이 원문항과 같았고, 발문이 ‘처음 소개하는 대상에는 부정관사를, 다시 가리키는 대상에는 정관사를’이라고 정답 규칙을 알려 주었다. 원문항 발문으로 되돌리고 정답 조합이 원문항과 다르게 새로 썼다."
def f604(t, p, good, chs, why, a, s=S604):
    items = []
    gs = [x.strip() for x in good.split(" - ")]
    for ch in chs:
        xs = [x.strip() for x in ch.split(" - ")]
        if xs == gs: items.append((ch, "두 빈칸 모두 알맞은 관사를 골랐으므로")); continue
        bits = [f"{['첫째', '둘째'][i]} 빈칸 {x}: {why[i]}" for i, (x, g) in enumerate(zip(xs, gs)) if x != g]
        items.append((ch, ". ".join(bits) + ". 따라서"))
    mk(6, 4, t, items, a, R604, s, st="R", p=p, okdup=True)
f604("B", "소녀 하나가 공원에 있다.\n→ _______ girl is in the park.\n그 소녀는 사과 하나를 먹고 있다.\n→ The girl is eating _______ apple.", "A - an",
     ["A - a", "An - an", "A - an", "The - an", "A - the"], ["처음 소개하는 girl은 자음 소리로 시작하므로 A를 쓴다", "처음 말하는 apple은 모음 소리로 시작하므로 an을 쓴다"], 3)
f604("C", "나는 한 시간 동안 책을 읽었다.\n→ I read a book for _______ hour.\n그 책은 재미있었다.\n→ _______ book was fun.", "an - The",
     ["a - The", "an - A", "the - The", "a - A", "an - The"], ["hour는 h를 발음하지 않고 모음 소리로 시작하므로 an을 쓴다", "앞에서 말한 그 책을 다시 가리키므로 The를 쓴다"], 5,
     S604 + " 철자가 아니라 발음으로 판단하는 hour를 넣었다.")
f604("D", "Tom은 어제 새 한 마리를 보았다.\n→ Tom saw _______ bird yesterday.\n그 새는 아주 작았다.\n→ _______ bird was very small.", "a - The",
     ["a - The", "the - The", "an - The", "a - A", "the - A"], ["처음 소개하는 bird는 자음 소리로 시작하므로 a를 쓴다", "앞에서 말한 그 새를 다시 가리키므로 The를 쓴다"], 1)
for t in "EF": F(6, 4, t, st="R", s="발문이 ‘처음 소개하는 하나의 대상에는 부정관사를, 다시 가리키는 대상에는 정관사를’이라고 정답 규칙을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 6-5 틀린 문장: 원문항처럼 철자가 아니라 발음으로 판단하는 a/an
R605 = "a/an은 철자가 아니라 첫소리로 정한다. hour, honest, honor의 h는 발음하지 않아 an을 쓰고, university, uniform, useful, unique, European은 /j/ 소리로 시작해 a를 쓴다."
S605 = "원문항은 철자는 자음이지만 발음이 모음인 hour(a hour)를 판별하는데, 변형은 an book, a orange처럼 첫 글자만 보고 판단할 수 있었고 짝 문장도 있었다. 원문항처럼 발음으로 판단해야 하는 단어로 유형마다 새로 썼다."
def f605(t, items, a, s=S605):
    mk(6, 5, t, items, a, R605, s)
f605("C", [("She wears a uniform to school.", "uniform은 /j/ 소리로 시작하므로 a를 바르게 썼으므로"), ("It takes an hour to get there.", "hour의 h는 발음하지 않아 모음 소리로 시작하므로 an을 바르게 썼으므로"), ("He has an useful tool.", "useful은 /j/ 소리로 시작하므로 a를 써야 하므로"),
           ("I saw an owl last night.", "owl은 모음 소리로 시작하므로 an을 바르게 썼으므로"), ("It is a big house.", "big은 자음 소리로 시작하므로 a를 바르게 썼으므로")], 3)
f605("D", [("This is a unique idea.", "unique는 /j/ 소리로 시작하므로 a를 바르게 썼으므로"), ("She ate an egg for breakfast.", "egg는 모음 소리로 시작하므로 an을 바르게 썼으므로"), ("We visited a museum.", "museum은 자음 소리로 시작하므로 a를 바르게 썼으므로"),
           ("He is a honest man.", "honest의 h는 발음하지 않아 모음 소리로 시작하므로 an을 써야 하므로"), ("I waited for an hour.", "hour의 h는 발음하지 않아 an을 바르게 썼으므로")], 4)
f605("E", [("He goes to an university in Seoul.", "university는 /j/ 소리로 시작하므로 a를 써야 하므로"), ("She has a one-dollar bill.", "one은 /w/ 소리로 시작하므로 a를 바르게 썼으므로"), ("That is an old tree.", "old는 모음 소리로 시작하므로 an을 바르게 썼으므로"),
           ("I have a useful map.", "useful은 /j/ 소리로 시작하므로 a를 바르게 썼으므로"), ("It was an honor to meet you.", "honor의 h는 발음하지 않아 an을 바르게 썼으므로")], 1)
f605("F", [("Tom has an uncle in Busan.", "uncle은 모음 소리로 시작하므로 an을 바르게 썼으므로"), ("There is a unicorn in the story.", "unicorn은 /j/ 소리로 시작하므로 a를 바르게 썼으므로"), ("I met a European friend.", "European은 /j/ 소리로 시작하므로 a를 바르게 썼으므로"),
           ("I read an interesting book.", "interesting은 모음 소리로 시작하므로 an을 바르게 썼으므로"), ("This is an uniform for our team.", "uniform은 /j/ 소리로 시작하므로 a를 써야 하므로")], 5)

# 6-6 빈칸 관사: 원문항 발문(우리말·규칙 설명 없이), 원문항처럼 be동사 오답
R606 = "셀 수 있는 단수명사 앞에는 a/an을 쓰며, 뒤에 오는 말이 자음 소리로 시작하면 a, 모음 소리로 시작하면 an을 쓴다. 명사 앞 빈칸에 be동사는 올 수 없고, two·many 뒤에는 복수형이 온다."
S606 = "발문이 ‘특정하지 않은 한 개의 대상, 부정관사를 고르시오’라고 알려 주었고, 오답 some·two는 우리말(한 개)과 바로 어긋나 a/an 둘 중 하나만 고르면 되었다. 원문항 발문으로 되돌리고, 원문항처럼 is·are 같은 오답을 넣었다. 우리말 없이도 답이 하나로 정해지도록 the는 보기에서 뺐다."
BE = "be동사라 명사 앞 빈칸에 올 수 없으므로"; PL = lambda w: f"two·many 뒤에는 복수형({w})이 와야 하므로"
def f606(t, p, items, a, s=S606):
    mk(6, 6, t, items, a, R606, s, st="R", p=p)
f606("B", "She is eating _______ banana.", [("an", "banana는 자음 소리로 시작하므로 an을 쓸 수 없으므로"), ("a", "자음 소리로 시작하는 단수명사 banana 앞에 a를 쓰므로"), ("is", BE), ("two", PL("bananas")), ("are", BE)], 2)
f606("C", "I am eating _______ apple.", [("are", BE), ("a", "apple은 모음 소리로 시작하므로 a를 쓸 수 없으므로"), ("an", "모음 소리로 시작하는 단수명사 apple 앞에 an을 쓰므로"), ("is", BE), ("many", PL("apples"))], 3)
f606("D", "Tom is making _______ sandwich.", [("is", BE), ("an", "sandwich는 자음 소리로 시작하므로 an을 쓸 수 없으므로"), ("two", PL("sandwiches")), ("are", BE), ("a", "자음 소리로 시작하는 단수명사 sandwich 앞에 a를 쓰므로")], 5)
f606("E", "Mina is eating _______ egg.", [("an", "모음 소리로 시작하는 단수명사 egg 앞에 an을 쓰므로"), ("is", BE), ("a", "egg는 모음 소리로 시작하므로 a를 쓸 수 없으므로"), ("many", PL("eggs")), ("are", BE)], 1)
f606("F", "The boy has _______ umbrella.", [("two", PL("umbrellas")), ("are", BE), ("is", BE), ("an", "모음 소리로 시작하는 단수명사 umbrella 앞에 an을 쓰므로"), ("a", "umbrella는 모음 소리로 시작하므로 a를 쓸 수 없으므로")], 4)

# 6-7 E: C와 겹치는 명사(bread)를 juice로
F(6, 7, "E", st="R", p="우리는 매일 아침 주스를 마신다.", c=["We drink a juice every morning.", "We drink juice every morning.", "We drinks juice every morning.", "We drink juices every morning.", "We are drink juice every morning."], a=2,
  n=["셀 수 없는 명사 juice 앞에 a를 쓰지 않으므로 오답이다.", "juice를 셀 수 없는 명사로 쓰고 주어 We에 맞게 drink를 바르게 썼으므로 정답이다.", "주어 We에는 drinks가 아니라 drink를 쓰므로 오답이다.", "셀 수 없는 명사 juice에는 복수형을 쓰지 않으므로 오답이다.", "일반동사 drink 앞에 be동사 are를 함께 쓸 수 없으므로 오답이다."],
  s="발문에 ‘(음식·물질·음악은 … 일반적인 뜻으로 쓴다.)’가 붙어 정답 근거를 알려 주었고, 우리말과 정답이 C(빵을 먹는다)와 거의 같았다. 원문항 발문으로 되돌리고 명사를 juice로 바꿨다. 정답 위치 ②.")

# 6-8 B: 원문항과 같은 제시 문장을 새로
F(6, 8, "B", p="Four _______ are working in the kitchen.", s="제시 문장(There are ten ____ in the classroom.)이 원문항과 똑같았다. 제시 문장을 새로 썼다. 보기와 정답은 그대로다.")

# 6-9 밑줄 복수형: 원문항 문장을 되풀이하지 않고 유형마다 새로
R609 = "복수형은 대부분 -s, s·sh·ch·x·자음 + o로 끝나면 -es(heroes, tomatoes), 자음 + y는 y를 i로 바꾸고 -es, f/fe는 v로 바꾸고 -es(knives, calves)를 붙인다. child → children, mouse → mice처럼 불규칙형과 deer·sheep처럼 단복수가 같은 명사도 있다."
S609 = "나머지 문장이 원문항 문장(wolves, knives, babies, boxes 등)을 거의 그대로 썼다. 원문항과 다른 문장으로 유형마다 새로 썼다."
OKP = lambda w, why: f"{w}: {why} 바르게 썼으므로"
def f609(t, items, a, s=S609):
    FIX.pop((6, 9, t), None)
    mk(6, 9, t, items, a, R609, s)
f609("B", [("We need five <u>knifes</u> for dinner.", "knife는 fe를 v로 바꾸고 -es를 붙여 knives로 써야 하므로"), ("Two <u>buses</u> stopped at the corner.", OKP("buses", "s로 끝나 -es를 붙여")), ("The <u>ladies</u> are singing together.", OKP("ladies", "자음 + y라 y를 i로 바꾸고 -es를 붙여")),
           ("Put the <u>potatoes</u> in the basket.", OKP("potatoes", "자음 + o라 -es를 붙여")), ("I saw two <u>deer</u> in the field.", OKP("deer", "단수와 복수가 같은 명사라 그대로"))], 1)
f609("C", [("Our city has many <u>parks</u>.", OKP("parks", "-s를 붙여")), ("The <u>thieves</u> ran away.", OKP("thieves", "f를 v로 바꾸고 -es를 붙여")), ("Please wash the <u>dishes</u>.", OKP("dishes", "sh로 끝나 -es를 붙여")),
           ("We picked some <u>cherries</u>.", OKP("cherries", "자음 + y라 y를 i로 바꾸고 -es를 붙여")), ("The <u>heros</u> saved the town.", "hero는 자음 + o라 -es를 붙여 heroes로 써야 하므로")], 5,
     S609 + " 정답도 D(childs)와 겹치지 않게 heros로 바꿨다.")
f609("E", [("The <u>churches</u> are very old.", OKP("churches", "ch로 끝나 -es를 붙여")), ("Two <u>babys</u> are crying loudly.", "baby는 자음 + y라 y를 i로 바꾸고 -es를 붙여 babies로 써야 하므로"), ("I have two <u>scarves</u>.", OKP("scarves", "f를 v로 바꾸고 -es를 붙여")),
           ("Both of my <u>feet</u> are cold.", OKP("feet", "foot의 불규칙 복수형으로")), ("Look at those <u>sheep</u>.", OKP("sheep", "단수와 복수가 같은 명사라 그대로"))], 2)
f609("F", [("The <u>women</u> are talking.", OKP("women", "woman의 불규칙 복수형으로")), ("There are many <u>stories</u> in this book.", OKP("stories", "자음 + y라 y를 i로 바꾸고 -es를 붙여")), ("The <u>calves</u> are drinking milk.", OKP("calves", "f를 v로 바꾸고 -es를 붙여")),
           ("Mom bought some <u>tomatos</u>.", "tomato는 자음 + o라 -es를 붙여 tomatoes로 써야 하므로"), ("We saw two <u>mice</u> in the kitchen.", OKP("mice", "mouse의 불규칙 복수형으로"))], 4,
     S609 + " 정답도 원문항(leafs)과 겹치지 않게 tomatos로 바꿨다.")


# ---- 2차 감수(2026-10) 추가 ----
R601 = "복수형은 대부분 -s를 붙이고, s·x·sh·ch로 끝나면 -es, 자음 + y는 y를 i로 바꾸고 -es를 붙인다. man - men, child - children, mouse - mice, foot - feet, goose - geese처럼 불규칙하게 변하는 명사는 따로 익힌다."
# 6-1 E: 보기 두 개(dish - dishes, baby - babies)가 원문항과 같음 / F: foot - feet은 원문항 정답(foot - foots)을 바르게 고친 것
FIX.pop((6, 1, "E"), None); FIX.pop((6, 1, "F"), None)
mk(6, 1, "E", [("child - children", "child의 불규칙 복수형을 바르게 썼으므로"), ("mouse - mice", "mouse의 불규칙 복수형을 바르게 썼으므로"), ("bus - buses", "s로 끝나 -es를 붙인 옳은 형태이므로"), ("lady - ladies", "자음 + y라 y를 i로 바꾸고 -es를 붙인 옳은 형태이므로"), ("man - mans", "man의 복수형은 불규칙형 men이므로")], 5, R601,
   "발문에 mouse의 뜻 설명이 붙었고, 보기 두 개(dish - dishes, baby - babies)가 원문항과 똑같았다. 원문항 발문으로 되돌리고 겹치는 보기를 다른 명사로 바꿨다. 정답은 그대로다.", st="R")
mk(6, 1, "F", [("city - cities", "자음 + y라 y를 i로 바꾸고 -es를 붙인 옳은 형태이므로"), ("box - boxes", "x로 끝나 -es를 붙인 옳은 형태이므로"), ("tooth - teeth", "tooth의 불규칙 복수형을 바르게 썼으므로"), ("goose - geese", "goose의 불규칙 복수형을 바르게 썼으므로"), ("mouse - mouses", "mouse의 복수형은 불규칙형 mice이므로")], 5, R601,
   "발문에 mouse의 뜻 설명이 붙었고, ④ foot - feet은 원문항 정답(foot - foots)을 바르게 고친 짝이었다. 원문항 발문으로 되돌리고 ④를 다른 명사로 바꿨다. 정답은 그대로다.", st="R")
# 6-2 C~F: 제시 문장(I need a ____.)이 원문항과 똑같음 → 문장을 새로, 정답 위치도 고르게
R602 = "a/an은 셀 수 있는 명사의 단수형 앞에만 쓴다. water, bread, money, rice, milk처럼 셀 수 없는 명사 앞에는 a/an을 쓰지 않는다."
S602 = "발문에 ‘(물질·추상명사는 일반적인 불가산 용법으로 판단한다.)’가 붙었고, 제시 문장(I need a ____.)이 원문항과 똑같았다. 원문항 발문으로 되돌리고 제시 문장을 새로 썼다."
CN = "셀 수 있는 명사라 a 뒤에 쓸 수 있으므로"; UN = lambda w: f"셀 수 없는 명사({w})라 a 뒤에 쓸 수 없으므로"
def f602(t, p, items, a, s=S602):
    FIX.pop((6, 2, t), None)
    mk(6, 2, t, [(w, why or CN) for w, why in items], a, R602, s, st="R", p=p)
f602("C", "There is a _______ on the table.", [("bread", UN("bread")), ("cup", ""), ("bag", ""), ("lamp", ""), ("pencil", "")], 1, S602 + " 보기 ②는 문장의 table과 겹치지 않게 cup으로 바꿨다. 정답은 그대로다.")
f602("D", "My brother wants a _______.", [("book", ""), ("chair", ""), ("bike", ""), ("money", UN("money")), ("desk", "")], 4, S602 + " 보기와 정답은 그대로다.")
f602("E", "He bought a _______ yesterday.", [("car", ""), ("rice", UN("rice")), ("pencil", ""), ("book", ""), ("watch", "")], 2, S602 + " 보기와 정답은 그대로다.")
f602("F", "Please bring me a _______.", [("fork", ""), ("chair", ""), ("blanket", ""), ("spoon", ""), ("milk", UN("milk"))], 5, S602 + " 원문항과 같은 보기(box, pen)도 바꾸고 정답 위치를 옮겼다.")
# 6-9 D: 정답(childs)과 같은 낱말의 바른 형태(children)가 함께 있음
f609("D", [("My uncle bought four <u>watches</u>.", OKP("watches", "ch로 끝나 -es를 붙여")), ("We saw two <u>mice</u> near the barn.", OKP("mice", "mouse의 불규칙 복수형으로")), ("Three <u>childs</u> crossed the road.", "child의 복수형은 불규칙형 children이므로"),
           ("There are many <u>cities</u> on the map.", OKP("cities", "자음 + y라 y를 i로 바꾸고 -es를 붙여")), ("The <u>geese</u> are swimming in the pond.", OKP("geese", "goose의 불규칙 복수형으로"))], 3,
     "정답(③ childs)과 같은 낱말의 바른 복수형(⑤ children)이 함께 있어 둘만 견주면 답이 나왔다. ⑤를 다른 명사로 바꿨다. 정답은 그대로다.")
# 6-10 C: B와 같은 짜임(요일 이름) / F: 대화가 이어지지 않고 D와 같은 종류(도시 이름)
R610 = "사람·도시·나라·요일·달·언어·기념일의 이름 같은 고유명사는 문장 어디에서나 첫 글자를 대문자로 쓴다. 보통명사는 문장 중간에서 소문자로 쓰고, 둘 이상이면 복수형(-s/-es, 자음 + y → -ies)으로 쓴다."
def f610(t, p, items, a, s):
    mk(6, 10, t, items, a, R610, s, p=p)
f610("C", "Sora: Is (A)<u>English</u> your favorite subject?\nBen: Yes. I read two English (B)<u>stories</u> every week.",
     [("(A)는 과목 이름이므로 english처럼 소문자로 써야 한다.", "English는 언어 이름인 고유명사라 대문자로 써야 하므로"), ("(B)는 two 뒤에 오므로 story로 써야 한다.", "two 뒤에는 복수형을 써야 하므로"), ("(A)와 (B)는 모두 고유명사이므로 대문자로 시작해야 한다.", "stories는 보통명사라 소문자로 쓰므로"),
      ("(A)의 English는 언어 이름인 고유명사이므로 문장 어디에서나 대문자로 시작한다.", "언어 이름은 고유명사라 대문자로 시작하므로"), ("(B)는 y로 끝나는 명사이므로 storys로 써야 한다.", "자음 + y로 끝나면 y를 i로 바꾸고 -es를 붙여 stories로 쓰므로")], 4,
     "밑줄 친 말(Friday)과 설명 틀이 B(Monday)와 같았다(둘 다 요일 이름). 고유명사의 종류를 언어 이름으로 바꾸고 설명을 새로 썼다.")
f610("F", "Mina: Is (A)<u>Christmas</u> coming soon?\nJane: Yes. I'm making five (B)<u>dishes</u> for the party.",
     [("(A)는 문장 중간에 있으므로 christmas로 써야 한다.", "Christmas는 기념일 이름인 고유명사라 대문자로 써야 하므로"), ("(A)의 Christmas는 기념일 이름인 고유명사이므로 대문자로 시작한다.", "기념일 이름은 고유명사라 대문자로 시작하므로"), ("(B)는 five 뒤에 오지만 dish로 써야 한다.", "five 뒤에는 복수형을 써야 하므로"),
      ("(B)는 셀 수 없는 명사이므로 복수형으로 쓸 수 없다.", "dish는 셀 수 있는 명사이므로"), ("(B)는 sh로 끝나므로 dishs로 써야 한다.", "sh로 끝나면 -es를 붙여 dishes로 쓰므로")], 2,
     "대화가 자연스럽게 이어지지 않았고(Is Busan far from here? — Yes. I see two buses.), 밑줄 친 말이 D와 같은 종류(도시 이름)였다. 고유명사의 종류를 기념일 이름으로 바꾸고 대화와 설명을 새로 썼다.")
