# 5급 CH1 인칭대명사의 격 (1~10) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def slotnote(ch, good, why, labs=("첫째", "둘째", "셋째"), sep=" - "):
    xs = [x.strip() for x in ch.split(sep)]; gs = [x.strip() for x in good.split(sep)]
    if xs == gs: return "모든 빈칸에 알맞은 말을 골랐으므로"
    bits = [f"{labs[i]} 빈칸 {x}: {w}" for i, (x, g, w) in enumerate(zip(xs, gs, why)) if x != g]
    return ", ".join(bits) + ". 따라서"
RP = "인칭대명사는 자리에 따라 주격(I, you, he, she, it, we, they), 소유격(my, your, his, her, its, our, their), 목적격(me, you, him, her, it, us, them), 소유대명사(mine, yours, his, hers, ours, theirs)로 쓴다."

# 5-1 주격 대명사: 원문항 발문, 같은 인칭의 다른 격을 오답으로
S51 = "원문항은 주격을 같은 인칭의 다른 격(소유격·목적격·소유대명사)과 구별하게 하는데, 변형 오답은 인칭·수가 다른 주격대명사여서 격 구별이 아니라 인칭·수 판단 문항이 되었다. 원문항처럼 같은 인칭의 다른 격으로 오답을 바꿨다."
def f51(t, p, items, a, s=S51):
    mk(5, 1, t, items, a, RP, s, st="R", p=p, okdup=True)
SUBJ = "주어 자리라 주격을 쓰므로"
def NOT(x, kind): return f"{x}: {kind}이라 주어 자리에 쓸 수 없으므로"
f51("B", "Tom and his sister are in the science club. _______ are in the science club.", [("Their", NOT("Their", "소유격")), ("Them", NOT("Them", "목적격")), ("They", "Tom and his sister를 받는 주격 They이므로"), ("Theirs", NOT("Theirs", "소유대명사")), ("Its", "Its: 단수 사물의 소유격이라 맞지 않으므로")], 3,
    "발문이 ‘주격대명사’라고 정답의 격을 알려 주었고 정답(We)도 원문항과 같았다. 원문항 발문으로 되돌리고 문장을 새로 써서 정답을 They로 바꿨으며 " + S51[S51.index("원문항처럼"):])
f51("C", "Jane is my cousin. _______ is my cousin.", [("Her", NOT("Her", "소유격·목적격")), ("She", "Jane을 받는 주격 She이므로"), ("Hers", NOT("Hers", "소유대명사")), ("Herself", NOT("Herself", "재귀대명사")), ("Its", "Its: 사물의 소유격이라 맞지 않으므로")], 2)
f51("D", "My father is tall. _______ is tall.", [("His", NOT("His", "소유격")), ("Him", NOT("Him", "목적격")), ("Himself", NOT("Himself", "재귀대명사")), ("He's", "He's: He is의 줄임말이라 뒤의 is와 겹치므로"), ("He", "My father를 받는 주격 He이므로")], 5)
f51("E", "You and Tom are late. _______ are late.", [("You", "You and Tom을 받는 주격 You이므로"), ("Your", NOT("Your", "소유격")), ("Yours", NOT("Yours", "소유대명사")), ("Yourself", NOT("Yourself", "재귀대명사")), ("Them", "Them: 목적격이고 인칭도 맞지 않으므로")], 1)
f51("F", "The dog is cute. _______ is cute.", [("Its", NOT("Its", "소유격")), ("It's", "It's: It is의 줄임말이라 뒤의 is와 겹치므로"), ("Itself", NOT("Itself", "재귀대명사")), ("It", "The dog를 받는 주격 It이므로"), ("Them", "Them: 복수 목적격이라 맞지 않으므로")], 4,
    "발문이 원문항과 달랐고 " + S51[S51.index("원문항은"):])

# 5-2 관계가 다른 짝: B 원문항 발문, C 정답을 새로
F(5, 2, "B", st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
mk(5, 2, "C", [("I - my", "주격 - 소유격의 짝이므로"), ("we - our", "주격 - 소유격의 짝이므로"), ("they - them", "주격 - 목적격의 짝이라 나머지(주격 - 소유격)와 관계가 다르므로"), ("it - its", "주격 - 소유격의 짝이므로"), ("you - your", "주격 - 소유격의 짝이므로")], 3,
   RP, "정답(he - him)이 원문항과 같았다. 정답 짝을 they - them으로 바꿨다.", okdup=True)

# 5-3 This/That is 뒤에 올 수 없는 말: 원문항 발문, 소유대명사·명사's 오답 포함
R53 = "This/That is 뒤에는 단수 명사(구), 소유대명사(mine, yours, hers, ours, theirs), 명사's(Tom's)가 올 수 있지만 복수 명사는 올 수 없다."
S53 = "발문에 ‘This/That이 하나의 대상을 직접 가리킬 때’ 조건이 붙어 복수형이 정답임을 알려 주었고, 원문항 오답의 소유대명사·명사's가 빠졌다. 원문항 발문으로 되돌리고 소유대명사·명사's를 오답에 넣었다."
PL = "단수 This/That 뒤에 복수 명사를 쓸 수 없으므로"
def OK3(x, kind): return f"{x}: {kind}라 This/That is 뒤에 쓸 수 있으므로"
def f53(t, p, items, a, s=S53):
    mk(5, 3, t, items, a, R53, s, st="R", p=p, okdup=True)
f53("B", "This is _______.", [("hers", OK3("hers", "소유대명사")), ("my sister's", OK3("my sister's", "명사's(~의 것)")), ("our bicycles", PL), ("his new camera", OK3("his new camera", "단수 명사구")), ("theirs", OK3("theirs", "소유대명사"))], 3)
f53("C", "This is _______.", [("ours", OK3("ours", "소유대명사")), ("her books", PL), ("Tom's", OK3("Tom's", "명사's(~의 것)")), ("my notebook", OK3("my notebook", "단수 명사구")), ("yours", OK3("yours", "소유대명사"))], 2)
f53("D", "That is _______.", [("his", OK3("his", "소유대명사")), ("my parents' car", OK3("my parents' car", "단수 명사구")), ("mine", OK3("mine", "소유대명사")), ("their pencils", PL), ("the teacher's", OK3("the teacher's", "명사's(~의 것)"))], 4)
f53("E", "This is _______.", [("his shoes", PL), ("yours", OK3("yours", "소유대명사")), ("my uncle's", OK3("my uncle's", "명사's(~의 것)")), ("theirs", OK3("theirs", "소유대명사")), ("her bag", OK3("her bag", "단수 명사구"))], 1)
f53("F", "That is _______.", [("Jane's", OK3("Jane's", "명사's(~의 것)")), ("hers", OK3("hers", "소유대명사")), ("ours", OK3("ours", "소유대명사")), ("my brother's cap", OK3("my brother's cap", "단수 명사구")), ("her toys", PL)], 5)

# 5-4 ‘그/그녀’ 관련 대명사 성격이 다른 하나: 원문항 발문
S54 = "발문이 ‘필요한 문법적 기능이 나머지와 다른 하나’로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
F(5, 4, "B", st="다음 빈칸에 '그녀'와 관련된 대명사가 들어갈 때, 성격이 다른 하나를 고르시오.", s=S54, okx=True)
for t in "CDEF": F(5, 4, t, st="R", s=S54)

# 5-5 옳은 문장: 원문항 발문, 여러 격의 오류를 섞어 유형마다 새로
R55 = "명사 앞에는 소유격(my, our, his, its, their), 명사 없이 ‘~의 것’은 소유대명사(mine, ours, hers, yours, theirs), 주어 자리에는 주격, 목적어 자리에는 목적격을 쓴다. 소유격·소유대명사에는 '(아포스트로피)를 붙이지 않고, it's는 it is의 줄임말이다."
S55 = "원문항은 여러 대명사 오류(them songs, It's fur, mine friend, Us like 등)를 판별하는데, 변형은 소유대명사 자리에 소유격을 쓴 오류 하나만 반복했고 짝 문장이 함께 있었으며 발문도 달랐다. 원문항 발문으로 되돌리고 여러 격의 오류를 섞어 유형마다 새로 썼다."
def f55(t, items, a, s=S55):
    mk(5, 5, t, items, a, R55, s, st="R")
f55("B", [("We love ours teacher.", "명사 teacher 앞에는 소유격 our를 쓰므로"), ("Its tail is very long.", "명사 tail 앞에 소유격 Its를 바르게 썼으므로"), ("Me brother is a student.", "명사 앞에는 소유격 My를 쓰므로"),
          ("The red cap is his's.", "his는 소유대명사로도 쓰여 's를 붙이지 않으므로"), ("Them are my classmates.", "주어 자리에는 주격 They를 쓰므로")], 2)
f55("C", [("Him name is Tom.", "명사 name 앞에는 소유격 His를 쓰므로"), ("It's color is blue.", "It's는 It is의 줄임말이라 명사 앞에는 Its를 쓰므로"), ("They visited we yesterday.", "목적어 자리에는 목적격 us를 쓰므로"),
          ("This book is mine.", "명사 없이 ‘나의 것’을 소유대명사 mine으로 바르게 썼으므로"), ("Those are yours bags.", "명사 bags 앞에는 소유격 your를 쓰므로")], 4)
f55("D", [("Those bags are theirs.", "명사 없이 ‘그들의 것’을 소유대명사 theirs로 바르게 썼으므로"), ("She called I last night.", "목적어 자리에는 목적격 me를 쓰므로"), ("Our's house is near here.", "소유격 Our에는 's를 붙이지 않으므로"),
          ("Mina is hers friend.", "명사 friend 앞에는 소유격 her를 쓰므로"), ("The cat licked it's paw.", "명사 paw 앞에는 소유격 its를 쓰므로")], 1)
f55("E", [("The teacher gave they homework.", "목적어 자리에는 목적격 them을 쓰므로"), ("Your's bag is here.", "소유격 Your에는 's를 붙이지 않으므로"), ("The bike is hers.", "명사 없이 ‘그녀의 것’을 소유대명사 hers로 바르게 썼으므로"),
          ("Mine dog is small.", "명사 dog 앞에는 소유격 My를 쓰므로"), ("He is ours new friend.", "명사 friend 앞에는 소유격 our를 쓰므로")], 3)
f55("F", [("Us are hungry.", "주어 자리에는 주격 We를 쓰므로"), ("I know his's name.", "소유격 his에는 's를 붙이지 않으므로"), ("Their's house is big.", "소유격 Their에는 's를 붙이지 않으므로"),
          ("Please help my.", "목적어 자리에는 목적격 me를 쓰므로"), ("These shoes are yours.", "명사 없이 ‘너의 것’을 소유대명사 yours로 바르게 썼으므로")], 5)

# 5-6 B, 5-8 B: 원문항 발문
F(5, 6, "B", st="R", s="발문이 원문항과 조금 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
mk(5, 8, "B", [("the children", "‘~의’를 나타내려면 소유격 's가 필요하므로"), ("the children's", "-s로 끝나지 않는 복수명사 children의 소유격은 's를 붙이므로"), ("their children", "‘그들의 아이들’이라 뜻이 달라지므로"),
               ("the childrens'", "children은 이미 복수라 -s를 더 붙이지 않으므로"), ("the child's", "단수 child의 소유격이라 복수 children과 맞지 않으므로")], 2,
   "‘~의’는 명사's로 나타낸다. -s로 끝나지 않는 복수명사(children, men)는 's를, -s로 끝나는 복수명사(boys)는 '만 붙인다.",
   "발문에 ‘소유격 표현을’이 붙었고, 보기 ④·⑤(the childrens', the childrens)가 표기만 달라 사실상 겹쳤다. 원문항 발문으로 되돌리고 ⑤를 the child's로 바꿨다.", st="R", okdup=True)

# 5-7 C: B와 같던 우리말을 새로
mk(5, 7, "C", [("Those caps are her.", "명사 없이 ‘그녀의 것’은 소유대명사 hers로 쓰므로"), ("That caps are hers.", "복수 caps 앞에는 Those를 쓰므로"), ("Those caps are hers.", "‘저 ~들’ Those + 복수명사와 소유대명사 hers를 바르게 썼으므로"),
               ("These caps are hers.", "‘저’는 These가 아니라 Those이므로"), ("Those cap is hers.", "Those 뒤에는 복수명사 caps와 are를 쓰므로")], 3,
   "this/that은 단수, these/those는 복수 명사와 쓰고, 명사 없이 ‘~의 것’은 소유대명사(mine, hers, ours, theirs)로 나타낸다.", "우리말과 정답이 B와 똑같았다. 우리말을 ‘저 모자들은 그녀의 것이다.’로 바꿨다.", p="저 모자들은 그녀의 것이다.")

# 5-9 축약형 vs 소유격: 같은 인칭의 축약형/소유격 조합 오답, F는 대명사를 새로
R59 = "He's·She's·They're·We're·It's는 ‘주어 + be동사’의 줄임말이고, His·Her·Their·Our·Its는 명사 앞에 쓰는 소유격이다."
S59 = "원문항 오답은 모두 It's/Its 조합이라 줄임말과 소유격의 구별을 묻는데, 변형 오답은 인칭이 맞지 않는 대명사라 바로 지워졌고 유형마다 반복되었다. 오답을 정답과 같은 인칭의 줄임말/소유격 조합으로 바꿨다."
def f59(t, p, c, a, why, s=S59):
    L = lambda z: re.sub(r"\([AB]\) ", "", z)
    mk(5, 9, t, [(x, slotnote(L(x), L(c[a-1]), why, labs=("(A)", "(B)"), sep=" — ")) for x in c], a, R59, s, p=p, okdup=True)
f59("C", "You are my best friend. (A)________ always kind to me. (B)________ smile makes me happy.", ["(A) Your — (B) You're", "(A) You — (B) Your", "(A) You're — (B) Your", "(A) You're — (B) You're", "(A) Your — (B) Your"], 3,
    ["be동사가 없어 You are의 줄임말 You're를 쓴다", "명사 smile 앞이라 소유격 Your를 쓴다"],
    S59 + " 또 문장(Tom is my brother. He's ~ / His ~)이 B(Tom is my uncle. He's ~ / His ~)와 사실상 같아 You're/Your를 묻는 문장으로 새로 썼다.")
f59("D", "Jane is my sister. (A)________ tall. (B)________ bag is blue.", ["(A) Her — (B) She's", "(A) She's — (B) Her", "(A) She — (B) Her", "(A) She's — (B) She's", "(A) Her — (B) Her"], 2,
    ["be동사가 없어 She is의 줄임말 She's를 쓴다", "명사 bag 앞이라 소유격 Her를 쓴다"])
f59("E", "Tom and Ben are my friends. (A)________ funny. (B)________ room is big.", ["(A) Their — (B) They're", "(A) They — (B) Their", "(A) They're — (B) They're", "(A) Their — (B) Their", "(A) They're — (B) Their"], 5,
    ["be동사가 없어 They are의 줄임말 They're를 쓴다", "명사 room 앞이라 소유격 Their를 쓴다"])
f59("F", "My sister and I love music. (A)________ in the school band. (B)________ band plays every Friday.", ["(A) Our — (B) We're", "(A) We — (B) Our", "(A) We're — (B) We're", "(A) We're — (B) Our", "(A) Our — (B) Our"], 4,
    ["be동사가 없어 We are의 줄임말 We're를 쓴다", "명사 band 앞이라 소유격 Our를 쓴다"],
    "정답(It's - Its)이 원문항과 같았고 오답도 인칭이 맞지 않는 대명사였다. 대명사를 We're/Our로 바꿔 새로 쓰고 " + S59[S59.index("오답을 정답과"):])

# 5-10 소유격 설명: 유형마다 오답 설명을 새로
R510 = "소유격(my, our, her, his, their)은 ‘~의’라는 뜻으로 뒤의 명사를 꾸민다. 주격·목적격·소유대명사·재귀대명사, ‘주어 + be동사’ 줄임말과 구별한다."
S510 = "대명사 설명 오답 네 개가 C와 똑같았다. 유형마다 오답 설명을 새로 썼다."
POSS = "뒤의 명사를 꾸미는 소유격이라는 설명이 바르므로"
def f510(t, items, a, s=S510):
    mk(5, 10, t, items, a, R510, s)
f510("D", [("'그녀를'이라는 뜻으로 동사 reading의 목적어이다.", "reading의 목적어는 her book 전체이고 her는 book을 꾸미므로"), ("'she is'를 줄여 쓴 형태로 주어와 동사 역할을 한다.", "she is의 줄임말은 she's이므로"),
           ("'그녀의 것'이라는 뜻으로 뒤에 명사 없이 쓰인 소유대명사이다.", "뒤에 명사 book이 있고, ‘그녀의 것’은 hers이므로"), ("'그녀의'라는 뜻으로 뒤의 명사 book을 꾸미는 소유격이다.", POSS),
           ("문장의 주어 Jane과 같은 사람을 가리키는 재귀대명사이다.", "재귀대명사는 herself이므로")], 4)
f510("E", [("'우리의'라는 뜻으로 뒤의 명사 room을 꾸미는 소유격이다.", POSS), ("'우리는'이라는 뜻으로 문장의 주어 역할을 한다.", "주어는 We이므로"), ("'우리를'이라는 뜻으로 전치사 in의 목적어이다.", "in의 목적어는 our room 전체이고 our는 room을 꾸미므로"),
           ("'ours'와 같은 뜻이라 'ours room'으로 바꿔 써도 된다.", "소유대명사 ours는 명사 앞에 쓰지 않으므로"), ("'we are'를 줄여 쓴 형태이다.", "we are의 줄임말은 we're이므로")], 1)
f510("F", [("'나를'이라는 뜻으로 동사 lost의 목적어이다.", "lost의 목적어는 my pen 전체이고 my는 pen을 꾸미므로"), ("'나의 것'이라는 뜻이라 'mine pen'으로 바꿔 써도 된다.", "소유대명사 mine은 명사 앞에 쓰지 않으므로"),
           ("'나의'라는 뜻으로 뒤의 명사 pen을 꾸미는 소유격이다.", POSS), ("주어 I를 한 번 더 강조하는 주격대명사이다.", "주격은 I이고 my는 소유격이므로"), ("'I am'을 줄여 쓴 형태이다.", "I am의 줄임말은 I'm이므로")], 3)


# ---- 2차 감수(2026-10) 추가 ----
# 5-4 B~F: 문장이 두세 낱말뿐(원문항의 절반 이하) → 원문항 수준으로 늘림, 정답 위치도 유형마다 달리
R54 = "주어 자리에는 주격(he, she), 동사·전치사 뒤 목적어 자리에는 목적격(him, her), 명사 앞에는 소유격(his, her)을 쓴다."
S54L = "발문이 ‘필요한 문법적 기능이 나머지와 다른 하나’로 바뀌었고, 문장이 두세 낱말뿐이라 원문항(문장마다 예닐곱 낱말)의 절반에 못 미쳤다. 원문항 발문으로 되돌리고 문장을 원문항 수준으로 늘렸다."
def f54(t, st, items, a, s=S54L):
    FIX.pop((5, 4, t), None)
    mk(5, 4, t, items, a, R54, s, st=st)
OBJH = "동사나 전치사 뒤 목적어 자리라 목적격(%s)이 들어가므로"; SUBH = "주어 자리라 주격(%s)이 들어가므로"; POSH = "명사 앞이라 소유격(%s)이 들어가므로"
def odd(x): return x.replace("들어가므로", "들어가 나머지와 다르므로")
f54("B", "다음 빈칸에 '그녀'와 관련된 대명사가 들어갈 때, 성격이 다른 하나를 고르시오.",
    [("My sister was busy, so Dad helped _______.", OBJH % "her"), ("I have an aunt. _______ teaches science.", odd(SUBH % "She")), ("Mina was alone, so I spoke to _______.", OBJH % "her"),
     ("Jane wasn't at school, so Tom called _______.", OBJH % "her"), ("We met _______ at the park yesterday.", OBJH % "her")], 2)
f54("C", "R", [("She called _______ last night.", OBJH % "him"), ("Minho was tired, so we helped _______.", OBJH % "him"), ("I see _______ at the bus stop every day.", OBJH % "him"),
     ("They met _______ at the library.", OBJH % "him"), ("Look at that boy. This is _______ bag.", odd(POSH % "his"))], 5)
f54("D", "R", [("_______ is kind to everyone.", SUBH % "He"), ("_______ studies English every night.", SUBH % "He"), ("That is _______ new bike.", odd(POSH % "his")),
     ("_______ lives next to my house.", SUBH % "He"), ("_______ plays soccer after school.", SUBH % "He")], 3)
f54("E", "R", [("Tom is very funny. Everyone likes _______.", odd(OBJH % "him")), ("This is _______ favorite cap.", POSH % "his"), ("I like _______ blue jacket.", POSH % "his"),
     ("Those are _______ old shoes.", POSH % "his"), ("She sees _______ brother every morning.", POSH % "his")], 1)
f54("F", "R", [("We know _______ very well.", OBJH % "him"), ("They call _______ every weekend.", OBJH % "him"), ("She helps _______ with the homework.", OBJH % "him"),
     ("Look at that boy. _______ is my brother.", odd(SUBH % "He")), ("I see _______ on the bus every morning.", OBJH % "him")], 4)
