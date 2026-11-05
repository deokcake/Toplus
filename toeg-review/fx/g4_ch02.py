# 4급 CH2 대명사·명사의 수 (11~20) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def slotnote(ch, good, why, labs=("첫째", "둘째", "셋째"), sep=" - "):
    xs = [x.strip() for x in ch.split(sep)]; gs = [x.strip() for x in good.split(sep)]
    if xs == gs: return "모든 빈칸에 알맞은 말을 골랐으므로"
    bits = [f"{labs[i]} 빈칸 {x}: {w}" for i, (x, g, w) in enumerate(zip(xs, gs, why)) if x != g]
    return ", ".join(bits) + ". 따라서"

# 4-11 C: 정답 짝을 원문항과 다르게
OBJ = "주격 - 목적격의 짝이므로"
mk(4, 11, "C", [("he - him", OBJ), ("they - them", OBJ), ("she - her", OBJ), ("you - yours", "주격 - 소유대명사의 짝이라 나머지(주격 - 목적격)와 관계가 다르므로"), ("we - us", OBJ)], 4,
   "인칭대명사는 주격(I, you, he, she, we, they), 목적격(me, you, him, her, us, them), 소유대명사(mine, yours, his, hers, ours, theirs)로 형태가 바뀐다.",
   "정답(she - hers)이 원문항과 같았다. 정답 짝을 you - yours로 바꿨다.", okdup=True)

# 4-13 고치지 못한 것: 원문항 발문과 밑줄, 소유 형태 오류 포함, 같은 문장 반복 없앰
ST413 = "밑줄 친 부분을 바르게 고치지 못한 것을 고르시오."
R413 = "동사·전치사의 목적어 자리에는 목적격(me, him, her, us, them)을 쓴다. 명사 없이 ‘~의 것’은 소유대명사(mine, yours, hers, ours, theirs)로 쓰며 아포스트로피(')를 붙이지 않고, ‘누구의’는 Whose로 쓴다."
S413 = "발문에 ‘인물·소유 관계를 그대로 유지하여’ 조건이 붙고 밑줄이 사라졌으며, 같은 틀린 문장을 옳게 고친 것과 틀리게 고친 것이 함께 있거나 목적격만 물었다. 원문항 발문과 밑줄로 되돌리고, 원문항처럼 소유 형태 오류(their's, Who's 등)도 넣어 유형마다 새로 썼다."
def U(a, b): return re.sub(r"\[(.+?)\]", r"<u>\1</u>", a) + " → " + re.sub(r"\[(.+?)\]", r"<u>\1</u>", b)
def f413(t, items, a, s=S413):
    mk(4, 13, t, [(U(x, y), w.replace("므로 바르게 고쳤으므로", "고, 바르게 고쳤으므로")) for x, y, w in items], a, R413, s, st=ST413)
OKFIX = "바르게 고쳤으므로"
f413("B", [("These lockers are [their's].", "These lockers are [theirs].", "소유대명사 theirs에는 '를 붙이지 않으므로 " + OKFIX), ("That backpack is [my].", "That backpack is [mine].", "명사 없이 ‘내 것’은 mine이므로 " + OKFIX),
           ("We talked to [he].", "We talked to [his].", "전치사 to의 목적어는 목적격 him이어야 하는데 소유대명사 his로 고쳐 바르게 고치지 못했으므로"), ("[Who's] coat is on the chair?", "[Whose] coat is on the chair?", "‘누구의’는 Whose이므로 " + OKFIX),
           ("Mina invited [she].", "Mina invited [her].", "목적어 자리에는 목적격 her를 쓰므로 " + OKFIX)], 3,
     "발문에 ‘인물·소유 관계를 그대로 유지하여’ 조건이 붙고 밑줄이 사라졌다. 원문항 발문과 밑줄로 되돌렸다. 보기와 정답은 그대로다.")
f413("C", [("Tom helped [I].", "Tom helped [mine].", "목적어 자리는 목적격 me여야 하는데 소유대명사 mine으로 고쳐 바르게 고치지 못했으므로"), ("This pencil is [your's].", "This pencil is [yours].", "소유대명사 yours에는 '를 붙이지 않으므로 " + OKFIX),
           ("[Who's] umbrella is this?", "[Whose] umbrella is this?", "‘누구의’는 Whose이므로 " + OKFIX), ("She called [he].", "She called [him].", "목적어 자리에는 목적격 him을 쓰므로 " + OKFIX),
           ("These cookies are [our].", "These cookies are [ours].", "명사 없이 ‘우리 것’은 ours이므로 " + OKFIX)], 1)
f413("D", [("We saw [he].", "We saw [him].", "목적어 자리에는 목적격 him을 쓰므로 " + OKFIX), ("The red cap is [her's].", "The red cap is [hers].", "소유대명사 hers에는 '를 붙이지 않으므로 " + OKFIX),
           ("Is this [you] bag?", "Is this [your] bag?", "명사 앞에는 소유격 your를 쓰므로 " + OKFIX), ("That house is [their].", "That house is [theirs].", "명사 없이 ‘그들의 것’은 theirs이므로 " + OKFIX),
           ("Tom visited [they].", "Tom visited [their].", "목적어 자리는 목적격 them이어야 하는데 소유격 their로 고쳐 바르게 고치지 못했으므로")], 5,
     S413 + " 틀리게 고친 보기는 원문항(she → hers, ④)과 겹치지 않게 they → their로 썼다.")
f413("E", [("Mom made a cake for [we].", "Mom made a cake for [us].", "전치사 뒤에는 목적격 us를 쓰므로 " + OKFIX), ("This room is [my].", "This room is [mine].", "명사 없이 ‘내 것’은 mine이므로 " + OKFIX),
           ("Jane waited for [I].", "Jane waited for [mine].", "전치사 for의 목적어는 목적격 me여야 하는데 소유대명사 mine으로 고쳐 바르게 고치지 못했으므로"), ("[Who's] phone is ringing?", "[Whose] phone is ringing?", "‘누구의’는 Whose이므로 " + OKFIX),
           ("The blue pen is [his'].", "The blue pen is [his].", "his는 소유격과 소유대명사의 형태가 같아 '를 붙이지 않으므로 " + OKFIX)], 3)
f413("F", [("That dog is [their's].", "That dog is [theirs].", "소유대명사 theirs에는 '를 붙이지 않으므로 " + OKFIX), ("Please help [we].", "Please help [ours].", "목적어 자리는 목적격 us여야 하는데 소유대명사 ours로 고쳐 바르게 고치지 못했으므로"),
           ("Tom likes [she].", "Tom likes [her].", "목적어 자리에는 목적격 her를 쓰므로 " + OKFIX), ("Is this bag [your]?", "Is this bag [yours]?", "명사 없이 ‘네 것’은 yours이므로 " + OKFIX),
           ("[Who's] shoes are these?", "[Whose] shoes are these?", "‘누구의’는 Whose이므로 " + OKFIX)], 2)

# 4-14 명사의 수와 동사 일치: 원문항 발문과 밑줄, 짝 문장 없이 유형마다 새로
ST414 = "다음 중 밑줄 친 부분이 틀린 문장을 고르시오."
R414 = "news·information·advice·furniture와 학문 이름(mathematics, physics, economics)은 단수 취급하고, pants·jeans·scissors·glasses·socks처럼 짝을 이루는 물건과 police는 복수 취급한다."
S414 = "정답 문장과 같은 문장의 옳은 형태가 다른 선택지에 함께 있어 대비 단서가 되었고, 발문에 mathematics의 뜻 설명이 붙고 밑줄이 사라졌으며, 오답 네 개가 유형마다 같았다. 원문항 발문과 밑줄로 되돌리고 짝 문장 없이 유형마다 새로 썼다."
SG = "단수 취급하는 명사라 단수 동사가 맞으므로"; PL = "복수 취급하는 명사라 복수 동사가 맞으므로"
def f414(t, items, a, s=S414):
    mk(4, 14, t, items, a, R414, s, st=ST414)
f414("B", [("My glasses <u>are</u> on the table.", PL), ("Mathematics <u>are</u> my favorite subject.", "학문 이름 mathematics는 단수 취급해 is를 써야 하므로"), ("The shorts <u>look</u> too big.", PL),
           ("His advice <u>was</u> very helpful.", SG), ("The jeans <u>are</u> blue.", PL)], 2)
f414("C", [("The scissors <u>are</u> on the desk.", PL), ("This bread <u>is</u> fresh.", SG), ("Physics <u>is</u> hard for me.", SG), ("My pants <u>is</u> too long.", "pants는 복수 취급해 are를 써야 하므로"), ("The children <u>are</u> playing.", PL)], 4,
     S414 + " 정답(The news are interesting)이 원문항과 같아 새로 썼다.")
f414("D", [("Economics <u>is</u> interesting.", SG), ("These scissors <u>is</u> sharp.", "scissors는 복수 취급해 are를 써야 하므로"), ("The furniture <u>looks</u> old.", SG), ("Her jeans <u>are</u> new.", PL), ("The good news <u>is</u> that we won.", SG)], 2)
f414("E", [("The police <u>are</u> looking for him.", PL), ("Your advice <u>is</u> always useful.", SG), ("My sunglasses <u>is</u> in the car.", "sunglasses는 복수 취급해 are를 써야 하므로"), ("The news <u>was</u> surprising.", SG), ("Those socks <u>are</u> dirty.", PL)], 3)
f414("F", [("Mathematics <u>is</u> easy for Tom.", SG), ("The police <u>is</u> here.", "police는 복수 취급해 are를 써야 하므로"), ("The information <u>was</u> wrong.", SG), ("These glasses <u>are</u> new.", PL), ("The trousers <u>look</u> nice.", PL)], 2)

# 4-15 옳은 문장으로만 짝: 원문항 형식(ⓐ~ⓓ 네 문장, 옳은 두 개의 짝), 소유격 표현 포함
ST415 = "다음 중 어법상 옳은 문장으로만 짝지어진 것은?"
R415 = "지시어(this/that ↔ these/those)·명사·동사의 수를 맞춘다. 사람·동물의 소유는 's(복수 -s로 끝나면 '만), 사물의 소유는 of로 나타낸다."
S415 = "원문항은 네 문장 중 옳은 두 개의 짝을 고르는데, 변형은 다섯 문장에서 ‘빠짐없이 모두’ 고르는 형식으로 바뀌었고 기호도 a~e로 바뀌었으며 소유격 문장이 빠졌다. 원문항 발문과 형식(ⓐ~ⓓ 네 문장, 옳은 두 개의 짝)으로 되돌리고 소유격 표현을 넣었다."
def f415(t, lines, judge, ok, c, s=S415):
    a = c.index(ok) + 1
    F(4, 15, t, st=ST415, p="\n".join(lines), c=c, a=a, r=R415, pre=["문장별 판정: " + j for j in judge], k=f"어법상 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), okdup=True, s=s + ipos(a))
CH415 = ["ⓐ, ⓑ", "ⓐ, ⓒ", "ⓑ, ⓒ", "ⓑ, ⓓ", "ⓒ, ⓓ"]
f415("B", ["ⓐ That dog is cute.", "ⓑ Those shoes is mine.", "ⓒ The color of the car is red.", "ⓓ These two girl's bags are new."],
     ["ⓐ O. 단수 That dog + is이다.", "ⓑ X. 복수 Those shoes에는 are를 쓴다.", "ⓒ O. 사물의 소유를 of로 나타냈다.", "ⓓ X. 두 소녀의 가방은 girls' bags로 쓴다."], "ⓐ, ⓒ", CH415)
f415("C", ["ⓐ These jeans is too small for me.", "ⓑ The roof of the house is red.", "ⓒ I borrowed my brother bike.", "ⓓ My parents' car is white."],
     ["ⓐ X. jeans는 복수 취급해 are를 쓴다.", "ⓑ O. 사물(집)의 소유를 of로 나타냈다.", "ⓒ X. ‘형의 자전거’는 my brother's bike로 쓴다.", "ⓓ O. -s로 끝나는 복수명사의 소유격은 '만 붙인다."], "ⓑ, ⓓ", CH415,
     S415 + " ⓐ~ⓒ가 원문항 문장과 거의 같고 정답 조합도 같아 문장을 새로 썼다.")
f415("D", ["ⓐ The news are good.", "ⓑ Those bag is hers.", "ⓒ This is Tom's book.", "ⓓ The legs of the table are short."],
     ["ⓐ X. news는 단수 취급해 is를 쓴다.", "ⓑ X. Those 뒤에는 복수명사 bags와 are를 쓴다.", "ⓒ O. 사람의 소유를 's로 나타냈다.", "ⓓ O. 사물의 소유를 of로 나타내고 복수 legs에 are를 썼다."], "ⓒ, ⓓ", CH415)
f415("E", ["ⓐ Those cars are theirs.", "ⓑ This bag is her.", "ⓒ The childrens' toys are on the floor.", "ⓓ My friend's house is near here."],
     ["ⓐ O. 명사 없이 ‘그들의 것’은 theirs이다.", "ⓑ X. 명사 없이 ‘그녀의 것’은 hers로 쓴다.", "ⓒ X. -s로 끝나지 않는 복수명사 children의 소유격은 children's이다.", "ⓓ O. 사람의 소유를 's로 나타냈다."], "ⓐ, ⓓ",
     ["ⓐ, ⓓ", "ⓐ, ⓑ", "ⓑ, ⓒ", "ⓑ, ⓓ", "ⓒ, ⓓ"])
f415("F", ["ⓐ This book is mine.", "ⓑ That is my sister's bike.", "ⓒ These car is fast.", "ⓓ The news are interesting."],
     ["ⓐ O. 명사 없이 ‘내 것’은 mine이다.", "ⓑ O. 사람의 소유를 's로 나타냈다.", "ⓒ X. These 뒤에는 복수명사 cars와 are를 쓴다.", "ⓓ X. news는 단수 취급해 is를 쓴다."], "ⓐ, ⓑ",
     ["ⓐ, ⓒ", "ⓑ, ⓓ", "ⓐ, ⓑ", "ⓒ, ⓓ", "ⓑ, ⓒ"])

# 4-16 소유대명사 자리: 원문항 발문과 밑줄, 짝 문장 없이 유형마다 새로
ST416 = "다음 밑줄 친 부분의 쓰임이 옳지 않은 것을 고르시오."
R416 = "명사 없이 ‘~의 것’을 나타낼 때는 소유대명사(mine, yours, his, hers, ours, theirs)를 쓰고, 소유격(my, your, her, our, their)은 뒤에 명사가 있어야 한다."
S416 = "정답 문장과 같은 문장의 옳은 형태가 다른 선택지에 함께 있어 대비 단서가 되었고, 발문에 ‘소유대명사’라는 용어가 붙고 밑줄이 사라졌으며 오답이 유형마다 같았다. 원문항 발문과 밑줄로 되돌리고 짝 문장 없이 유형마다 새로 썼다."
POS = "명사 없이 ‘~의 것’을 나타내는 소유대명사를 바르게 썼으므로"
def f416(t, items, a, s=S416):
    mk(4, 16, t, [(x, w or POS) for x, w in items], a, R416, s, st=ST416)
f416("B", [("The small umbrella is <u>mine</u>.", ""), ("These shoes are <u>our</u>.", "소유격 our 뒤에 명사가 없으므로 ours로 써야 하므로"), ("The blue bike is <u>theirs</u>.", ""), ("The red cup is <u>his</u>.", ""), ("This seat is <u>yours</u>.", "")], 2)
f416("C", [("Those pens are <u>his</u>.", ""), ("This notebook is <u>hers</u>.", ""), ("The blue car is <u>theirs</u>.", ""), ("Is this bag <u>your</u>?", "소유격 your 뒤에 명사가 없으므로 yours로 써야 하므로"), ("These books are <u>ours</u>.", "")], 4,
     S416 + " 정답(Those pens are my)이 원문항과 같아 새로 썼다.")
f416("D", [("That jacket is <u>mine</u>.", ""), ("These gloves are <u>yours</u>.", ""), ("The house on the hill is <u>ours</u>.", ""), ("The toys are <u>theirs</u>.", ""), ("This book is <u>her</u>.", "소유격 her 뒤에 명사가 없으므로 hers로 써야 하므로")], 5)
f416("E", [("That bike is <u>their</u>.", "소유격 their 뒤에 명사가 없으므로 theirs로 써야 하므로"), ("This pencil case is <u>mine</u>.", ""), ("Those cookies are <u>hers</u>.", ""), ("The green bag is <u>yours</u>.", ""), ("This cap is <u>his</u>.", "")], 1)
f416("F", [("This desk is <u>ours</u>.", ""), ("The dog is <u>theirs</u>.", ""), ("Those bags are <u>your</u>.", "소유격 your 뒤에 명사가 없으므로 yours로 써야 하므로"), ("That coat is <u>his</u>.", ""), ("The white shoes are <u>mine</u>.", "")], 3)

# 4-17 목적격 대명사: 원문항 발문, C는 대화를 새로
S417 = "발문이 ‘Tom(Jane)을 he(she)로 받는다, 목적격대명사를 고르라’고 정답을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
for t in "BD": F(4, 17, t, st="R", s=S417)
mk(4, 17, "C", [("it", "keys는 복수라 it으로 받지 않으므로"), ("them", "복수명사 keys를 목적격 복수대명사 them으로 받으므로"), ("its", "its는 소유격이라 목적어 자리에 쓸 수 없으므로"), ("it's", "it's는 it is의 줄임말이라 목적어 자리에 쓸 수 없으므로"), ("this", "this는 단수라 복수 keys를 받지 않으므로")], 2,
   "앞에 나온 명사를 대명사로 받을 때는 수(단수·복수)와 자리(주어·목적어)에 맞춘다. 복수명사는 목적어 자리에서 them으로 받는다.",
   "제시문과 정답(glasses - them)이 원문항과 똑같았다. 대화를 ‘Where are your keys? - I left ___ on the table.’로 새로 쓰고 원문항처럼 it/its/it's 오답을 넣었다.",
   st="R", p="A: Where are your keys?\nB: I left ________ on the table.", okdup=True)

# 4-18 축약형 vs 소유격: 밑줄 빈칸, 같은 대명사의 축약형/소유격 조합 오답
R418 = "It's·They're·He's·She's·We're·You're는 ‘주어 + be동사’의 줄임말이고, its·their·his·her·our·your는 명사 앞에 쓰는 소유격이다."
S418 = "원문항 오답은 모두 Its/It's 조합이라 줄임말과 소유격의 구별을 묻는데, 변형 오답(They - them, He - him 등)은 문장과 관계없는 대명사라 바로 지워졌고 유형마다 반복되었으며 밑줄도 사라졌다. 원문항처럼 밑줄 빈칸으로 되돌리고 오답을 같은 대명사의 줄임말/소유격 조합으로 바꿨다."
def f418(t, s1, s2, c, a, why, s=S418):
    p = "- " + s1.replace("(A)", "(<u>    A    </u>)") + "\n- " + s2.replace("(B)", "(<u>    B    </u>)")
    L = lambda z: re.sub(r"\([AB]\) ", "", z)
    mk(4, 18, t, [(x, slotnote(L(x), L(c[a-1]), why, labs=("(A)", "(B)"))) for x in c], a, R418, s, p=p, okdup=True)
f418("B", "(A) my parents.", "I know (B) car.", ["(A) Their - (B) their", "(A) They're - (B) their", "(A) They're - (B) they're", "(A) Their - (B) they're", "(A) They - (B) their"], 2,
     ["뒤에 명사만 있어 ‘그들은 ~이다’의 They're(They are)를 쓴다", "명사 car 앞이라 소유격 their를 쓴다"])
f418("C", "(A) good friends.", "They know (B) teacher.", ["(A) Our - (B) our", "(A) We're - (B) we're", "(A) We - (B) our", "(A) Our - (B) we're", "(A) We're - (B) our"], 5,
     ["뒤에 명사만 있어 ‘우리는 ~이다’의 We're(We are)를 쓴다", "명사 teacher 앞이라 소유격 our를 쓴다"],
     "제시문과 정답(It's - its)이 원문항과 똑같았다. 문장을 We're/our로 새로 쓰고 " + S418[S418.index("원문항처럼"):])
f418("D", "(A) Tom.", "I know (B) brother.", ["(A) He's - (B) his", "(A) His - (B) his", "(A) He's - (B) he's", "(A) His - (B) he's", "(A) He - (B) his"], 1,
     ["뒤에 이름만 있어 ‘그는 ~이다’의 He's(He is)를 쓴다", "명사 brother 앞이라 소유격 his를 쓴다"])
f418("E", "(A) Jane.", "I know (B) sister.", ["(A) Her - (B) her", "(A) She - (B) her", "(A) She's - (B) her", "(A) She's - (B) she's", "(A) Her - (B) she's"], 3,
     ["뒤에 이름만 있어 ‘그녀는 ~이다’의 She's(She is)를 쓴다", "명사 sister 앞이라 소유격 her를 쓴다"])
f418("F", "(A) my best friend.", "I like (B) smile.", ["(A) Your - (B) your", "(A) You're - (B) you're", "(A) Your - (B) you're", "(A) You're - (B) your", "(A) You - (B) your"], 4,
     ["뒤에 명사만 있어 ‘너는 ~이다’의 You're(You are)를 쓴다", "명사 smile 앞이라 소유격 your를 쓴다"],
     "정답(It's - its)과 (B) 문장(I know its name)이 원문항과 같았다. 대명사를 You're/your로 바꿔 새로 쓰고 " + S418[S418.index("원문항처럼"):])

# 4-19 밑줄 중 틀린 것: 원문항 발문과 번호 밑줄, B는 선행사를 복수명사로
S419 = "원문항의 밑줄이 사라지고 발문에 ‘현재 시제를 유지할 것’ 조건이 붙었다. 원문항 발문과 번호 밑줄로 되돌렸다. 보기와 정답은 그대로다."
def UL(p): return re.sub(r"([①-⑤])([A-Za-z']+)", r"\1<u>\2</u>", p)
for t in "CDEF":
    ex = V(4, 19, t)["expl"]
    F(4, 19, t, st="R", p=UL(V(4, 19, t)["passage"]), xr=[x for x in [("현재 시제를 유지하면서 ", ""), ("현재 시제를 유지하여 ", ""), ("현재 시제를 유지할 때 ", ""), ("useful는", "useful은")] if x[0] in ex], s=S419)
mk(4, 19, "B", [("some", "복수명사 shoes 앞에 some을 쓸 수 있으므로"), ("shoes", "신발은 짝을 이루는 물건이라 복수형 shoes가 맞으므로"), ("It", "복수명사 shoes는 They로 받아야 하므로"), ("are", "They로 받으면 복수 동사 are가 맞으므로"), ("comfortable", "be동사 뒤 보어 자리에 형용사가 맞으므로")], 3,
   "shoes·pants·glasses처럼 짝을 이루는 물건은 복수 취급해 They로 받고 복수 동사를 쓴다.",
   "‘a pair of shoes’는 단수로도 받을 수 있어 ④ They를 It으로 고치는 답도 가능했고 밑줄도 사라졌다. 선행사를 some shoes로 바꾸고 원문항처럼 대명사가 틀린 문장으로 새로 썼으며 원문항 발문과 번호 밑줄로 되돌렸다.",
   st="R", p="Jane bought ①<u>some</u> new ②<u>shoes</u>. ③<u>It</u> ④<u>are</u> very ⑤<u>comfortable</u>.", okdup=True)

# 4-20 틀린 것 모두 고르기: 원문항 형식((A)~(D) 밑줄, 2~3개 조합)
ST420 = "다음 중 밑줄 친 부분이 어법상 틀린 문장을 모두 고른 것은?"
R420 = "복수 주어에는 복수 동사, 단수 주어에는 단수 동사를 쓴다. 소유대명사에는 '를 붙이지 않고, 명사 없이 ‘~의 것’은 소유대명사로 쓰며, ‘누구의’는 Whose이다."
S420 = "원문항은 밑줄 친 네 문장에서 틀린 것을 모두 고르는 조합형인데, 변형은 밑줄 없이 다섯 문장을 주고 한두 개만 틀리게 해 형식이 바뀌었다. 원문항 발문과 형식((A)~(D) 네 문장, 밑줄, 2~3개 조합)으로 되돌렸다."
def f420(t, lines, judge, ok, c, s=S420):
    a = c.index(ok) + 1
    F(4, 20, t, st=ST420, p="\n".join(lines), c=c, a=a, r=R420, pre=["문장별 판정: " + j for j in judge], k=f"밑줄 친 부분이 틀린 문장은 {ok}이다.", n=setnotes(c, ok, "틀린 문장"), okdup=True, s=s + ipos(a))
CH420 = ["(A), (B)", "(B), (C)", "(A), (C), (D)", "(B), (C), (D)", "(A), (B), (D)"]
f420("B", ["(A) The scissors <u>are</u> sharp.", "(B) This is <u>their's</u> house.", "(C) The news <u>are</u> bad.", "(D) We know <u>them</u>."],
     ["(A) O. scissors는 복수 취급한다.", "(B) X. 명사 house 앞에는 소유격 their를 쓴다.", "(C) X. news는 단수 취급해 is를 쓴다.", "(D) O. 목적어 자리에 목적격 them을 썼다."], "(B), (C)", CH420)
f420("C", ["(A) Jane and Mike <u>are</u> my cousins.", "(B) Their house <u>are</u> very big.", "(C) Those bags are <u>their</u>.", "(D) This book is <u>my</u>."],
     ["(A) O. 복수 주어에 are를 썼다.", "(B) X. 단수 주어 Their house에는 is를 쓴다.", "(C) X. 명사 없이 ‘그들의 것’은 theirs로 쓴다.", "(D) X. 명사 없이 ‘내 것’은 mine으로 쓴다."], "(B), (C), (D)", CH420,
     S420 + " (A)(B)가 원문항 문장과 같고 정답 조합도 같아 문장을 새로 썼다.")
f420("D", ["(A) These pants <u>is</u> new.", "(B) The news <u>is</u> good.", "(C) That car is <u>hers</u>.", "(D) Those books are <u>our</u>."],
     ["(A) X. pants는 복수 취급해 are를 쓴다.", "(B) O. news는 단수 취급한다.", "(C) O. 명사 없이 ‘그녀의 것’은 hers이다.", "(D) X. 명사 없이 ‘우리 것’은 ours로 쓴다."], "(A), (D)",
     ["(A), (D)", "(B), (C)", "(A), (C), (D)", "(B), (C), (D)", "(A), (B), (D)"])
f420("E", ["(A) Jane and I <u>am</u> friends.", "(B) This bag is <u>mine</u>.", "(C) <u>Who's</u> shoes are these?", "(D) The police <u>are</u> here."],
     ["(A) X. 복수 주어 Jane and I에는 are를 쓴다.", "(B) O. 명사 없이 ‘내 것’은 mine이다.", "(C) X. ‘누구의’는 Whose로 쓴다.", "(D) O. police는 복수 취급한다."], "(A), (C)",
     ["(A), (B)", "(A), (C)", "(B), (C), (D)", "(A), (C), (D)", "(A), (B), (D)"])
f420("F", ["(A) The children <u>is</u> in the playground.", "(B) Their room <u>is</u> big.", "(C) This bike is <u>her's</u>.", "(D) Those books are <u>my</u>."],
     ["(A) X. 복수 주어 The children에는 are를 쓴다.", "(B) O. 단수 주어 Their room에 is를 썼다.", "(C) X. 소유대명사 hers에는 '를 붙이지 않는다.", "(D) X. 명사 없이 ‘내 것’은 mine으로 쓴다."], "(A), (C), (D)",
     ["(A), (C)", "(B), (D)", "(A), (C), (D)", "(B), (C), (D)", "(A), (B), (D)"])


# ---- 2차 감수(2026-10) 추가 ----
# 4-12 B~F: 정답 문장이 모두 ‘_____ am ~’이라 am만 보고 고를 수 있음 → 원문항처럼 he/him 자리로
R412 = "his는 명사 앞의 소유격(his friend)이나 ‘그의 것’이라는 소유대명사(The book is his)로 쓴다. 주어 자리에는 He, 목적어 자리에는 him을 쓴다."
S412 = "정답 문장이 ‘_____ am ~’이어서 his를 몰라도 am만 보고 고를 수 있었고, 다섯 유형이 모두 같은 방식이었다. 원문항처럼 he나 him이 들어가야 하는 문장으로 바꿨다."
POSS = "명사 앞에 소유격 his가 들어가므로"; PRON = "‘그의 것’이라는 소유대명사 his가 들어가므로"
SUBJ = "주어 자리라 His가 아니라 He가 들어가야 하므로"; OBJ12 = "목적어 자리라 his가 아니라 him이 들어가야 하므로"
def f412(t, items, a, s=S412):
    mk(4, 12, t, items, a, R412, s, st="R")
f412("B", [("This is _____ desk.", POSS), ("_____ is very happy today.", SUBJ), ("I know _____ teacher.", POSS), ("That book is _____.", PRON), ("_____ hat is blue.", POSS)], 2)
f412("C", [("_____ book is red.", POSS), ("This is _____ bag.", POSS), ("That car is _____.", PRON), ("I like _____ new jacket.", POSS), ("We played soccer with _____ yesterday.", "전치사 뒤 목적어 자리라 his가 아니라 him이 들어가야 하므로")], 5)
f412("D", [("This is _____ watch.", POSS), ("The blue umbrella is _____.", PRON), ("I know _____ brother.", POSS), ("_____ dog is cute.", POSS), ("_____ likes to wear a cap.", SUBJ)], 5)
f412("E", [("My teacher helped _____ after class.", OBJ12), ("_____ sister is kind.", POSS), ("This is _____ pencil.", POSS), ("That bike is _____.", PRON), ("I like _____ car.", POSS)], 1)
f412("F", [("_____ father is tall.", POSS), ("_____ is a good student.", SUBJ), ("This is _____ room.", POSS), ("I like _____ school.", POSS), ("That bag is _____.", PRON)], 2)

# 4-19 C~F: 네 유형 모두 정답이 ④(원문항도 ④)이고 동사만 틀림 → 대명사·지시어 오류로, 정답 위치를 달리
R419 = "glasses·gloves·pants·shoes처럼 짝을 이루는 물건과 police는 복수 취급해 they/them으로 받는다. news는 단수 취급해 this/it으로 받는다."
S419N = "원문항의 밑줄이 사라지고 발문에 ‘현재 시제를 유지할 것’ 조건이 붙었으며, C~F 네 유형의 정답이 모두 ④(원문항도 ④)이고 원문항과 달리 대명사가 아니라 동사만 틀렸다. 원문항 발문과 번호 밑줄로 되돌리고, 대명사나 지시어가 틀린 문장으로 새로 써서 정답 위치를 유형마다 달리했다."
def f419(t, p, items, a):
    FIX.pop((4, 19, t), None)
    mk(4, 19, t, items, a, R419, S419N, st="R", p=p)
f419("C", "I can't find my ①<u>gloves</u>. Did you see ②<u>it</u>? ③<u>My</u> hands ④<u>are</u> very ⑤<u>cold</u>.",
     [("gloves", "장갑은 짝을 이루는 물건이라 복수형 gloves가 맞으므로"), ("it", "복수명사 gloves는 them으로 받아야 하므로"), ("My", "명사 hands 앞에 소유격 My가 맞으므로"), ("are", "복수 주어 My hands에 are가 맞으므로"), ("cold", "be동사 뒤 보어 자리에 형용사가 맞으므로")], 2)
f419("D", "I ①<u>bought</u> ②<u>some</u> pants ③<u>yesterday</u>. I ④<u>really</u> like ⑤<u>it</u>.",
     [("bought", "yesterday가 있어 과거형 bought가 맞으므로"), ("some", "복수 취급하는 pants 앞에 some을 쓸 수 있으므로"), ("yesterday", "과거의 때를 나타내는 말로 맞으므로"), ("really", "동사 like를 꾸미는 부사로 맞으므로"), ("it", "복수 취급하는 pants는 them으로 받아야 하므로")], 5)
f419("E", "①<u>These</u> news ②<u>is</u> very ③<u>surprising</u>. I heard ④<u>it</u> on ⑤<u>the</u> radio.",
     [("These", "news는 단수 취급하므로 These가 아니라 This를 써야 하므로"), ("is", "단수 취급하는 news에 is가 맞으므로"), ("surprising", "be동사 뒤 보어 자리에 형용사가 맞으므로"), ("it", "단수 취급하는 news를 it으로 받는 것이 맞으므로"), ("the", "on the radio로 the를 쓰는 것이 맞으므로")], 1)
f419("F", "The police ①<u>are</u> ②<u>here</u> now. I called ③<u>it</u> ten ④<u>minutes</u> ⑤<u>ago</u>.",
     [("are", "police는 복수 취급하므로 are가 맞으므로"), ("here", "장소를 나타내는 부사로 맞으므로"), ("it", "복수 취급하는 police는 them으로 받아야 하므로"), ("minutes", "ten 뒤이므로 복수형 minutes가 맞으므로"), ("ago", "‘~ 전에’라는 뜻으로 과거형 called와 맞으므로")], 3)
