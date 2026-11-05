# 4급 CH1 명사와 관사 (1~10) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def slotnote(ch, good, why, labs=("첫째", "둘째", "셋째"), sep=" - "):
    xs = [x.strip() for x in ch.split(sep)]; gs = [x.strip() for x in good.split(sep)]
    if xs == gs: return "모든 빈칸에 알맞은 말을 골랐으므로"
    bits = [f"{labs[i]} 빈칸 {x}: {w}" for i, (x, g, w) in enumerate(zip(xs, gs, why)) if x != g]
    return ", ".join(bits) + ". 따라서"

# 4-1 C: 정답 명사를 원문항과 다르게, 원문항 발문
mk(4, 1, "C", [("box - boxes", "-x로 끝나 -es를 붙인 옳은 복수형이므로"), ("knife - knifes", "-fe로 끝나는 knife는 f를 v로 바꿔 knives로 써야 하므로"), ("woman - women", "불규칙 복수형을 바르게 짝지었으므로"),
               ("book - books", "-s를 붙인 옳은 복수형이므로"), ("baby - babies", "자음 + y로 끝나 y를 i로 바꾸고 -es를 붙인 옳은 복수형이므로")], 2,
   "명사의 복수형은 보통 -s를 붙이고, -s·-x·-ch·-sh로 끝나면 -es, 자음 + y는 y를 i로 바꾸고 -es, -f(e)는 f를 v로 바꾸고 -es를 붙인다. man - men, child - children 같은 불규칙 변화도 있다.",
   "정답(mouse - mouses)이 원문항과 같았고 발문에 mouse의 뜻 설명이 붙었다. 원문항 발문으로 되돌리고 정답을 knife - knifes로 바꿨다.", st="R")

# 4-2 셀 수 있는 명사: 원문항 발문(조건 삭제), C는 정답 명사를 새로
S42 = "발문에 ‘기본 뜻에서 개체를 하나씩’, ‘물질은 단위로 바꾸어 해석하지 않는다’는 조건이 붙었다. 원문항 발문으로 되돌렸다. 보기의 다른 명사는 모두 기본적으로 셀 수 없는 명사라 조건 없이도 정답은 하나다. 보기와 정답은 그대로다."
for t in "BDEF": F(4, 2, t, st="R", xr=[x for x in [("제시된 기본 뜻에서 ", "기본적으로 ")] if x[0] in V(4, 2, t)["expl"]], s=S42)
mk(4, 2, "C", [("juice", "음료인 juice는 셀 수 없는 명사이므로"), ("sugar", "물질인 sugar는 셀 수 없는 명사이므로"), ("cookie", "하나씩 셀 수 있는 명사이므로(a cookie, two cookies)"), ("money", "money는 셀 수 없는 명사이므로"), ("water", "물질인 water는 셀 수 없는 명사이므로")], 3,
   "사람·동물·물건처럼 하나씩 셀 수 있는 명사는 a/an과 복수형을 쓰고, 물질(water, sugar)·추상 개념·돈(money) 등은 셀 수 없는 명사로 쓴다.",
   "정답(monkey)이 원문항과 같았고 발문 조건도 붙었다. 원문항 발문으로 되돌리고 정답을 cookie로 바꿨다.", st="R", okdup=True)

# 4-3 a/an이 들어갈 수 없는 것: 원문항처럼 관사 용법(식사, by + 교통수단, play the + 악기)
R43 = "a/an은 셀 수 있는 명사의 단수형 앞에 쓴다. 식사 이름(breakfast, lunch) 앞, by + 교통수단에는 관사를 쓰지 않고, 악기 앞에는 play the + 악기로 the를 쓴다."
A_ = "셀 수 있는 명사 단수형 앞이라 a/an이 들어갈 수 있으므로"
def f43(t, items, a, s):
    mk(4, 3, t, [(x, w or A_) for x, w in items], a, R43, s)
f43("C", [("I have _____ lunch at noon.", "식사 이름 lunch 앞에는 관사를 쓰지 않으므로"), ("She is _____ honest girl.", ""), ("There is _____ cat on the sofa.", ""), ("I bought _____ new bike.", ""), ("He ate _____ orange.", "")], 1,
    "정답(Can you play _____ drums?)이 원문항과 똑같았다. 정답 문장을 식사 이름 앞 무관사로 새로 썼다.")
f43("D", [("Tom is _____ good cook.", ""), ("I go to school by _____ bus.", "by + 교통수단에는 관사를 쓰지 않으므로"), ("She has _____ interesting book.", ""), ("He needs _____ hour to finish it.", ""), ("They live in _____ big house.", "")], 2,
    "‘We go to _____ schools’는 어색하고, 빈칸 뒤 복수명사만 보고 답을 고를 수 있어 원문항(관사 용법) 취지와 달랐다. 원문항처럼 by + 교통수단의 무관사 문장으로 새로 썼다.")
f43("E", [("My dad is _____ engineer.", ""), ("Jane wants _____ new phone.", ""), ("She plays _____ violin very well.", "악기 앞에는 play the + 악기로 the를 쓰므로"), ("I saw _____ owl last night.", ""), ("Tom has _____ uncle in Canada.", "")], 3,
    "‘cooks _____ breakfasts’는 어색하고 복수명사만 보고 답을 고를 수 있었다. 원문항처럼 관사 용법(play the + 악기) 문장으로 새로 썼다.")

# 4-4 반드시 the: 원문항 발문, C는 정답 문장을 새로
S44 = "발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
for t in "BDEF": F(4, 4, t, st="R", s=S44)
mk(4, 4, "C", [("________ banana is in the basket.", "A banana도 The banana도 쓸 수 있어 반드시 the는 아니므로"), ("We go to ________ school at eight.", "학교에 본래 목적(공부)으로 가면 관사를 쓰지 않으므로"),
               ("________ Han River flows through Seoul.", "강 이름 앞에는 반드시 the를 쓰므로"), ("________ bird is singing in the tree.", "A bird도 The bird도 쓸 수 있어 반드시 the는 아니므로"), ("He is ________ tall boy.", "처음 말하는 대상이라 a를 쓰므로")], 3,
   "강·바다 이름처럼 정해진 대상과 유일한 대상에는 the를 쓰고, 식사·운동·본래 목적의 장소(school, bed) 앞에는 보통 관사를 쓰지 않는다.",
   "정답(Sun is very bright today)이 원문항과 똑같았다. 원문항 발문으로 되돌리고 정답을 강 이름(the Han River)으로 바꿨다.", st="R")

# 4-5 a/an 고치기 + 이유: 원문항처럼 오답도 ‘고치는 방법 + 이유’의 그럴듯한 설명
R45 = "a/an은 철자가 아니라 뒤 단어의 첫소리로 정한다. 첫소리가 모음이면 an(an hour, an owl), 자음이면 a(a university, a one-way)를 쓴다."
S45 = "원문항 오답은 ‘무엇을 어떻게 고친다 + 이유’의 그럴듯한 설명인데, 변형 오답(‘첫 글자가 모음이면 항상 an’ 등)은 고치는 방법 없이 일반론만 말해 뻔하고 유형마다 반복되었다. 원문항처럼 오답도 ‘고치는 방법 + 이유’ 형식으로 유형마다 새로 썼다."
OK45 = "첫소리에 맞춰 관사를 바르게 고치고 이유도 바르게 설명했으므로"
def f45(t, p, items, a, s=S45):
    mk(4, 5, t, items, a, R45, s, p=p)
f45("B", "It was a honest answer.",
    [("a를 the로 고쳐야 한다. 정직한 대답은 세상에 하나뿐이기 때문이다.", "처음 말하는 대답이라 the가 필요하지 않으므로"), ("a를 an으로 고쳐야 한다. 'honest'의 'h'가 발음되지 않아 모음 소리로 시작하기 때문이다.", OK45),
     ("honest를 honesty로 고쳐야 한다. 관사 뒤에는 형용사가 올 수 없기 때문이다.", "관사 뒤에 형용사 + 명사가 올 수 있으므로"), ("a를 삭제해야 한다. answer는 셀 수 없는 명사이기 때문이다.", "answer는 셀 수 있는 명사이므로"),
     ("answer를 answers로 고쳐야 한다. 형용사 뒤의 명사는 항상 복수형이기 때문이다.", "형용사 뒤에도 단수명사를 쓸 수 있으므로")], 2)
f45("C", "I saw a owl in the tree.",
    [("a를 the로 고쳐야 한다. 나무 위의 부엉이는 정해진 것이기 때문이다.", "처음 말하는 부엉이라 the가 필요하지 않으므로"), ("owl을 owls로 고쳐야 한다. 나무에는 여러 마리가 있기 때문이다.", "a와 함께 단수명사를 쓰므로 틀린 곳은 관사이므로"),
     ("a를 an으로 고쳐야 한다. 'owl'이 모음 소리로 시작하기 때문이다.", OK45), ("a를 삭제해야 한다. 동물 이름 앞에는 관사를 쓰지 않기 때문이다.", "셀 수 있는 동물 이름 앞에도 관사를 쓰므로"),
     ("in을 on으로 고쳐야 한다. 나무에는 항상 on을 쓰기 때문이다.", "나뭇가지 사이의 새는 in the tree로 쓸 수 있으므로")], 3,
    "문장(It is a unusual story.)과 정답이 원문항과 똑같았고 오답도 일반론이었다. 문장을 새로 쓰고 오답도 ‘고치는 방법 + 이유’ 형식으로 바꿨다.")
f45("D", "He is an university student.",
    [("an을 a로 고쳐야 한다. 'university'는 자음 소리 /j/로 시작하기 때문이다.", OK45), ("an을 the로 고쳐야 한다. 대학교는 하나뿐이기 때문이다.", "처음 말하는 대학생이라 the가 필요하지 않으므로"),
     ("an은 옳다. 'university'의 첫 글자 u가 모음이기 때문이다.", "관사는 첫 글자가 아니라 첫소리(/j/)로 정하므로"), ("student를 students로 고쳐야 한다. university가 여러 학생을 뜻하기 때문이다.", "주어 He는 한 사람이라 단수명사가 맞으므로"),
     ("an을 삭제해야 한다. 직업 앞에는 관사를 쓰지 않기 때문이다.", "직업·신분 앞에도 a/an을 쓰므로")], 1)
f45("E", "She waited for a hour.",
    [("hour를 hours로 고쳐야 한다. 기다린 시간은 항상 복수형으로 쓰기 때문이다.", "한 시간이라 단수 hour가 맞으므로"), ("a를 삭제해야 한다. for 뒤에는 관사를 쓰지 않기 때문이다.", "for 뒤에도 관사를 쓸 수 있으므로"),
     ("a를 the로 고쳐야 한다. 정해진 한 시간이기 때문이다.", "정해진 한 시간이 아니라 ‘한 시간 동안’이므로"), ("waited를 waits로 고쳐야 한다. 주어가 3인칭 단수이기 때문이다.", "과거의 일이라 waited가 맞으므로"),
     ("a를 an으로 고쳐야 한다. 'hour'는 첫 글자 h를 읽지 않고 모음 [aʊ]로 소리 나기 때문이다.", OK45)], 5)
f45("F", "Tom bought an one-way ticket.",
    [("an은 옳다. 'one'의 첫 글자 o가 모음이기 때문이다.", "관사는 첫 글자가 아니라 첫소리(/w/)로 정하므로"), ("ticket을 tickets로 고쳐야 한다. one-way는 여러 장을 뜻하기 때문이다.", "one-way는 ‘편도’라는 뜻이고 한 장이라 단수가 맞으므로"),
     ("an을 the로 고쳐야 한다. 편도표는 한 가지뿐이기 때문이다.", "처음 말하는 표라 the가 필요하지 않으므로"), ("an을 a로 고쳐야 한다. 'one'은 자음 소리 /w/로 시작하기 때문이다.", OK45),
     ("bought를 buyed로 고쳐야 한다. 과거형은 -ed를 붙이기 때문이다.", "buy의 과거형은 불규칙 bought이므로")], 4)

# 4-6 불규칙 복수형 빈칸: 원문항 발문, 유형마다 명사를 새로
R46 = "명사에 따라 단수와 복수가 같은 형태(sheep, deer, fish)이거나 불규칙하게 바뀐다(goose - geese, mouse - mice, wolf - wolves). How many 뒤와 수량 표현 뒤에는 복수형을 쓴다."
def f46(t, p, items, a, s):
    mk(4, 6, t, items, a, R46, s, st="R", p=p, okdup=True)
f46("B", "A: How many ________ are there?\nB: There are five.", [("a deer", "How many 뒤에 a + 단수명사를 쓸 수 없으므로"), ("deeries", "없는 형태이므로"), ("deer", "deer는 단수와 복수의 형태가 같으므로"), ("deeres", "없는 형태이므로"), ("deer's", "소유격이라 How many 뒤에 쓸 수 없으므로")], 3,
    "발문이 ‘단수형과 철자가 같은 형태’라고 정답을 알려 주었다. 원문항 발문으로 되돌리고, 조건이 없으면 논란이 되는 deers를 소유격 deer's로 바꿨다.")
f46("C", "A: How many ________ are there on the farm?\nB: There are twenty.", [("gooses", "goose의 복수형은 불규칙 geese이므로"), ("geese", "goose의 불규칙 복수형이므로"), ("a goose", "How many 뒤에 a + 단수명사를 쓸 수 없으므로"), ("geeses", "geese에 -s를 또 붙이지 않으므로"), ("goose", "How many 뒤에는 복수형을 쓰므로")], 2,
    "정답(sheep)과 대화(I see ten.)가 원문항과 거의 같았다. 명사를 goose로 바꿔 대화를 새로 썼다.")
f46("E", "A: How many ________ did the cat catch?\nB: Two.", [("mouses", "mouse의 복수형은 불규칙 mice이므로"), ("a mouse", "How many 뒤에 a + 단수명사를 쓸 수 없으므로"), ("mices", "mice에 -s를 또 붙이지 않으므로"), ("mice", "mouse의 불규칙 복수형이므로"), ("mouse", "How many 뒤에는 복수형을 쓰므로")], 4,
    "정답(sheep)이 원문항과 같았다. 명사를 mouse로 바꿔 대화를 새로 썼다.")
f46("F", "A: How many ________ are in the forest?\nB: Three.", [("wolves", "-f로 끝나는 wolf는 f를 v로 바꿔 wolves로 쓰므로"), ("wolfs", "wolf의 복수형은 wolves이므로"), ("a wolf", "How many 뒤에 a + 단수명사를 쓸 수 없으므로"), ("wolfes", "f를 v로 바꿔야 하므로"), ("wolve", "없는 형태이므로")], 1,
    "발문이 ‘단수형과 철자가 같은 형태’라고 정답을 알려 주었고 명사(deer)가 B와 같았다. 원문항 발문으로 되돌리고 명사를 wolf로 바꿨다.")

# 4-7 some + 셀 수 없는 명사 영작: 원문항 발문(조건 삭제), C는 우리말을 새로
S47 = "발문에 ‘물질·돈의 양을 말하며 단위로 바꾸어 해석하지 않는다’가 붙어 셀 수 없는 명사라는 정답 근거를 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
for t in "BDEF": F(4, 7, t, st="R", s=S47)
mk(4, 7, "C", [("I put two sugar in my tea.", "셀 수 없는 명사 sugar 앞에 two를 쓸 수 없으므로"), ("I put many sugar in my tea.", "many는 셀 수 있는 명사에 쓰므로"), ("I put an sugar in my tea.", "셀 수 없는 명사 앞에 an을 쓸 수 없으므로"),
               ("I put some sugar in my tea.", "‘약간의 설탕’을 some + 셀 수 없는 명사로 바르게 옮겼으므로"), ("I put a sugar in my tea.", "셀 수 없는 명사 앞에 a를 쓸 수 없으므로")], 4,
   "sugar, butter, water, bread, money 같은 셀 수 없는 명사는 a/an이나 수를 붙이지 않고, ‘약간’은 some으로 나타낸다.",
   "우리말과 정답(some butter)이 원문항과 똑같았고 발문도 근거를 알려 주었다. 우리말을 ‘나는 차에 설탕을 약간 넣는다.’로 바꾸고 원문항 발문으로 되돌렸다.", st="R", p="나는 차에 설탕을 약간 넣는다.")

# 4-8 전치사 + 관사 두 빈칸: 원문항 형식, 정답 조합을 원문항(in, the)과 다르게
ST48 = "다음 빈칸에 들어갈 단어가 순서대로 짝지어진 것은?"
R48 = "at the moment(지금), for an hour(한 시간 동안), at the end of(~의 끝에), on the first of(~일에), in a minute(곧)처럼 전치사와 관사가 짝을 이루는 표현을 익힌다."
def f48(t, p, c, a, why, s):
    mk(4, 8, t, [(x, slotnote(x, c[a-1], why, sep=", ")) for x in c], a, R48, s, st=ST48, p=p, okdup=True)
f48("B", "She is busy ______ ______ moment.", ["in, the", "at, a", "on, the", "at, the", "in, a"], 4, ["‘지금’은 at the moment로 at을 쓴다", "at the moment로 the를 쓴다"],
    "정답 조합(in - the)과 문장 구조(in the + 하루 때)가 원문항과 같았다. 정답 조합을 at the moment(at, the)로 바꿔 새로 썼다.")
f48("C", "We waited ______ ______ hour.", ["for, a", "in, an", "for, an", "at, an", "on, a"], 3, ["‘~ 동안’의 기간은 for로 나타낸다", "hour는 모음 소리로 시작해 an을 쓴다"],
    "제시문과 정답이 원문항과 똑같았다. 제시문을 새로 쓰고 정답 조합을 for, an으로 바꿨다.")
f48("D", "Let's meet ______ ______ end of the month.", ["in, the", "at, the", "on, an", "at, an", "by, a"], 2, ["‘~의 끝에’는 at the end of로 at을 쓴다", "end of the month는 정해진 때라 the를 쓴다"],
    "원문항은 전치사와 관사 두 빈칸을 묻는데 변형은 빈칸이 하나여서 관사를 평가하지 않았다. 원문항처럼 전치사 + 관사 두 빈칸으로 새로 썼다.")
f48("E", "My birthday is ______ ______ first of May.", ["on, the", "in, the", "at, a", "on, a", "in, a"], 1, ["날짜 앞에는 on을 쓴다", "서수(first) 앞에는 the를 쓴다"],
    "원문항은 전치사와 관사 두 빈칸을 묻는데 변형은 빈칸이 하나여서 관사를 평가하지 않았다. 원문항처럼 전치사 + 관사 두 빈칸으로 새로 썼다.")
f48("F", "It will be ready ______ ______ minute.", ["at, a", "on, a", "in, the", "for, the", "in, a"], 5, ["‘곧(1분 뒤에)’은 in a minute로 in을 쓴다", "in a minute로 a를 쓴다"],
    "빈칸이 하나로 줄었고 발문에 우리말 뜻이 붙었다. 원문항 발문과 전치사 + 관사 두 빈칸으로 되돌렸다.")

# 4-9 by + 교통수단 무관사: 유형마다 문장을 새로
R49 = "by + 교통수단(bus, train, taxi, plane, ship, bike)에는 관사를 쓰지 않는다."
BAD49 = "by + 교통수단에는 관사를 쓰지 않으므로"; OK49 = "by + 교통수단에 관사 없이 바르게 썼으므로"
def f49(t, items, a, s):
    mk(4, 9, t, [(x, OK49 if i + 1 == a else BAD49) for i, x in enumerate(items)], a, R49, s)
f49("C", ["She went to Busan by the train.", "He comes to school by a bicycle.", "We traveled to Japan by ship.", "They go to work by the subway.", "I came here by an airplane."], 3,
    "정답(He goes to the office by taxi.)이 원문항과 똑같았고 오답이 B와 같았다. 정답과 오답을 새로 썼다.")
f49("D", ["Mom goes to the market by a car.", "My uncle travels by the bus.", "I go to the library by the bike.", "We went to the museum by a subway.", "They went to the island by boat."], 5,
    "정답(We go home on foot)이 by + 교통수단의 무관사가 아니라 go home을 물었고 오답이 B와 같았다. by + 교통수단 문장을 정답으로 새로 쓰고 오답도 새로 썼다.")
f49("E", ["Dad goes to the office by train.", "Jane goes to school by the bicycle.", "We went to Jeju by a plane.", "He came home by the taxi.", "They go to the zoo by a bus."], 1,
    "오답 네 개가 B와 똑같았다. 유형마다 오답을 새로 썼다.")
f49("F", ["My sister goes to work by a subway.", "They travel by plane.", "He goes to school by the bike.", "We went to Seoul by the train.", "She comes home by a taxi."], 2,
    "오답 네 개가 B와 똑같았다. 유형마다 오답을 새로 썼다.")

# 4-10 틀린 것 모두 고르기: 원문항 형식((A)~(D) 밑줄, 2~4개 조합)
ST410 = "다음 중 밑줄 친 부분이 어법상 틀린 문장을 모두 고른 것은?"
R410 = "셀 수 없는 명사는 복수형을 쓰지 않고, 불규칙 복수형(feet, children, mice, men, women)을 따로 익힌다. by + 교통수단과 운동 이름 앞에는 관사를 쓰지 않고, 악기 앞에는 the를 쓰며, a/an은 첫소리로 정한다."
S410 = "원문항은 밑줄 친 네 문장에서 틀린 것을 모두 고르는 조합형인데, 변형은 밑줄 없이 다섯 문장을 주고 선택지 대부분이 한 개짜리여서 사실상 하나만 고르는 문항이 되었다. 원문항 발문과 형식((A)~(D) 네 문장, 밑줄, 2~4개 조합)으로 되돌렸다."
def f410(t, lines, judge, ok, c, s=S410):
    a = c.index(ok) + 1
    F(4, 10, t, st=ST410, p="\n".join(lines), c=c, a=a, r=R410, pre=["문장별 판정: " + j for j in judge], k=f"밑줄 친 부분이 틀린 문장은 {ok}이다.", n=setnotes(c, ok, "틀린 문장"), okdup=True, s=s + ipos(a))
f410("B", ["(A) She drinks <u>some milks</u>.", "(B) I see <u>two feet</u>.", "(C) Tom plays <u>the drums</u>.", "(D) They go <u>to home</u>."],
     ["(A) X. milk는 셀 수 없는 명사라 복수형을 쓰지 않는다.", "(B) O. foot의 불규칙 복수형 feet이다.", "(C) O. 악기 앞에 the를 썼다.", "(D) X. ‘집에 가다’는 go home으로 to를 쓰지 않는다."], "(A), (D)",
     ["(A), (D)", "(B), (C)", "(A), (B), (D)", "(B), (C), (D)", "(A), (B), (C), (D)"])
f410("C", ["(A) I need <u>some breads</u>.", "(B) There are <u>two children</u>.", "(C) He plays <u>a piano</u> every day.", "(D) She lives in <u>a old house</u>."],
     ["(A) X. bread는 셀 수 없는 명사라 복수형을 쓰지 않는다.", "(B) O. child의 불규칙 복수형 children이다.", "(C) X. 악기 앞에는 the를 써서 play the piano로 쓴다.", "(D) X. old는 모음 소리로 시작해 an old house로 쓴다."], "(A), (C), (D)",
     ["(A), (C)", "(B), (D)", "(A), (C), (D)", "(A), (B), (C)", "(A), (B), (C), (D)"], S410 + " (A)(B)가 원문항 문장과 같고 정답 조합도 같아 문장을 새로 썼다.")
f410("D", ["(A) We eat <u>some rice</u>.", "(B) I saw three <u>mouses</u>.", "(C) She goes to school <u>by the bus</u>.", "(D) He has <u>an umbrella</u>."],
     ["(A) O. 셀 수 없는 명사 rice에 some을 썼다.", "(B) X. mouse의 복수형은 mice이다.", "(C) X. by + 교통수단에는 관사를 쓰지 않는다.", "(D) O. umbrella는 모음 소리로 시작해 an을 쓴다."], "(B), (C)",
     ["(A), (B)", "(B), (C)", "(B), (C), (D)", "(A), (C), (D)", "(A), (B), (C), (D)"], S410 + " 발문에 붙었던 mouse의 뜻 설명도 뺐다.")
f410("E", ["(A) I need <u>some moneys</u>.", "(B) There are <u>two mans</u>.", "(C) He plays <u>the soccer</u>.", "(D) She sees <u>an dog</u>."],
     ["(A) X. money는 셀 수 없는 명사라 복수형을 쓰지 않는다.", "(B) X. man의 복수형은 men이다.", "(C) X. 운동 이름 앞에는 관사를 쓰지 않는다.", "(D) X. dog는 자음 소리로 시작해 a를 쓴다."], "(A), (B), (C), (D)",
     ["(A), (B)", "(C), (D)", "(A), (B), (C)", "(B), (C), (D)", "(A), (B), (C), (D)"])
f410("F", ["(A) We eat <u>some bread</u>.", "(B) There are three <u>women</u>.", "(C) Jane goes to school <u>by a bike</u>.", "(D) He has <u>a egg</u>."],
     ["(A) O. 셀 수 없는 명사 bread에 some을 썼다.", "(B) O. woman의 불규칙 복수형 women이다.", "(C) X. by + 교통수단에는 관사를 쓰지 않는다.", "(D) X. egg는 모음 소리로 시작해 an을 쓴다."], "(C), (D)",
     ["(A), (C)", "(B), (D)", "(A), (C), (D)", "(C), (D)", "(B), (C), (D)"])
