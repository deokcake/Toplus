# 3급 CH5 대명사 (41~50) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]

# 3-41 인칭대명사 격: 오답과 정답을 유형마다 새로
R41 = "대명사는 문장 속 자리에 맞는 격을 쓴다. 주어 자리에는 주격(I, he, they), 동사·전치사 뒤에는 목적격(me, him, them), 명사 앞에는 소유격(my, her, its), 뒤에 명사 없이 ‘~의 것’은 소유대명사(mine, hers, ours)를 쓴다."
S41 = "오답 네 문장이 유형마다 같았다(B는 정답 문장도 원문항과 똑같았다). 원문항처럼 목적격·소유격·소유대명사 오류를 섞어 유형마다 새로 썼다."
def W(bad, good, why): return f"{bad}: {why} {good}로 써야 하므로"
OK = "문장 속 자리에 맞는 격을 바르게 썼으므로"
mk(3, 41, "B", [("This bag is her.", W("her", "hers", "뒤에 명사 없이 ‘그녀의 것’이므로 소유대명사")), ("Mina lent me her pen.", OK), ("We met they at the park.", W("they", "them", "동사 뒤 목적어 자리이므로 목적격")),
                ("Their house is bigger than our.", W("our", "ours", "뒤에 명사 없이 ‘우리의 것’이므로 소유대명사")), ("Please give it to I.", W("I", "me", "전치사 뒤이므로 목적격"))], 2, R41, S41)
mk(3, 41, "C", [("Is this pencil your?", W("your", "yours", "뒤에 명사 없이 ‘너의 것’이므로 소유대명사")), ("He sent a letter to we.", W("we", "us", "전치사 뒤이므로 목적격")), ("Them are my friends.", W("Them", "They", "주어 자리이므로 주격")),
                ("These shoes are my.", W("my", "mine", "뒤에 명사 없이 ‘나의 것’이므로 소유대명사")), ("Tom helped me yesterday.", OK)], 5, R41, S41)
mk(3, 41, "D", [("Her is my best friend.", W("Her", "She", "주어 자리이므로 주격")), ("Our car is older than their.", W("their", "theirs", "뒤에 명사 없이 ‘그들의 것’이므로 소유대명사")), ("I called him last night.", OK),
                ("Can you help we?", W("we", "us", "동사 뒤 목적어 자리이므로 목적격")), ("That idea was her.", W("her", "hers", "뒤에 명사 없이 ‘그녀의 것’이므로 소유대명사"))], 3, R41, S41)
mk(3, 41, "E", [("They saw her at school.", OK), ("The dog wagged it tail.", W("it", "its", "명사(tail) 앞이므로 소유격")), ("Jane gave a card to he.", W("he", "him", "전치사 뒤이므로 목적격")),
                ("This room is our.", W("our", "ours", "뒤에 명사 없이 ‘우리의 것’이므로 소유대명사")), ("Us are in the same class.", W("Us", "We", "주어 자리이므로 주격"))], 1, R41, S41)
mk(3, 41, "F", [("The book on the desk is my.", W("my", "mine", "뒤에 명사 없이 ‘나의 것’이므로 소유대명사")), ("Mom made dinner for they.", W("they", "them", "전치사 뒤이므로 목적격")), ("His is my cousin.", W("His", "He", "주어 자리이므로 주격")),
                ("We know them well.", OK), ("Your house is bigger than mine house.", W("mine house", "my house(또는 mine)", "명사 앞에는 소유격을 쓰므로"))], 4, R41, S41)

# 3-42 this/these 수 일치: 짝 문장 없애고 유형마다 새로
R42 = "this/that은 단수명사와, these/those는 복수명사와 쓰고, 동사도 명사의 수에 맞춘다. pants·glasses·scissors처럼 짝을 이루는 물건은 복수로, information·furniture·news·advice는 단수로 취급한다."
S42 = "오답 네 문장이 유형마다 같았고(B는 정답 문장도 원문항과 같았다), 틀린 문장이 같은 명사의 옳은 문장과 짝을 이뤘다. 짝 문장을 없애고 유형마다 새로 썼다."
OK2 = "지시어·명사·동사의 수가 모두 맞으므로"
mk(3, 42, "B", [("This cake tastes sweet.", OK2), ("Those girls are my classmates.", OK2), ("That building is very tall.", OK2), ("These book is interesting.", "These 뒤에는 복수명사를 쓴다(This book is 또는 These books are). 수 일치가 틀렸으므로"), ("These cookies smell good.", OK2)], 4, R42, S42)
mk(3, 42, "C", [("This pants is too long.", "pants는 복수로 취급하므로 These pants are로 써야 한다. 수 일치가 틀렸으므로"), ("That dog is barking.", OK2), ("Those cars are fast.", OK2), ("This song is popular.", OK2), ("These oranges are fresh.", OK2)], 1, R42, S42)
mk(3, 42, "D", [("This water is cold.", OK2), ("Those trees are tall.", OK2), ("That man is my uncle.", OK2), ("These children are kind.", OK2), ("That glasses are mine.", "glasses(안경)는 복수로 취급하므로 Those glasses로 써야 한다. 수 일치가 틀렸으므로")], 5, R42, S42)
mk(3, 42, "E", [("This homework is difficult.", OK2), ("Those house are old.", "Those 뒤에는 복수명사를 쓴다(Those houses). 수 일치가 틀렸으므로"), ("That girl sings well.", OK2), ("These men are doctors.", OK2), ("This news is surprising.", OK2)], 2, R42, S42)
mk(3, 42, "F", [("These socks are warm.", OK2), ("That bag looks heavy.", OK2), ("This furniture are expensive.", "furniture는 셀 수 없는 명사라 단수로 취급하므로 is를 쓴다. 수 일치가 틀렸으므로"), ("Those students are busy.", OK2), ("This advice is helpful.", OK2)], 3, R42, S42)

# 3-43 B: 원문항과 같던 제시문을 새로
mk(3, 43, "B", [("himself", "himself: 명령문의 생략된 주어는 you이므로 맞지 않으므로"), ("yourselves", "yourselves: 한 사람(Mina)에게 하는 말이므로 맞지 않으므로"), ("herself", "herself: Mina에게 직접 말하는 명령문의 주어는 you이므로 맞지 않으므로"),
                ("yourself", "yourself: 한 사람에게 하는 말(주어 you)의 재귀대명사로 두 빈칸에 모두 알맞으므로"), ("themselves", "themselves: 3인칭 복수라 주어 you와 맞지 않으므로")], 4,
   "재귀대명사는 주어와 같은 대상을 가리킬 때 쓴다. 명령문의 생략된 주어는 you이며, 한 사람에게는 yourself, 여러 사람에게는 yourselves를 쓴다.",
   "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘Mina, don't blame ___. / You should be proud of ___.’로 바꿨다.", p="Mina, don't blame ________.\nYou should be proud of ________.")

# 3-44 B: 원문항과 거의 같던 문장을 새로
mk(3, 44, "B", [("one - them", "첫째 빈칸 one: 복수명사(socks)를 대신하므로 ones를 쓴다. 따라서"), ("ones - it", "둘째 빈칸 it: 장갑 한 켤레(my gloves)는 복수이므로 them을 쓴다. 따라서"),
                ("it - ones", "첫째 빈칸 it: 같은 종류의 다른 양말을 뜻하므로 ones를 쓴다. 둘째 빈칸 ones: 바로 그 장갑을 가리키므로 them을 쓴다. 따라서"), ("ones - them", "ones - them: 같은 종류의 복수 물건은 ones, 바로 그 장갑(복수)은 them으로 알맞으므로"),
                ("one - it", "첫째 빈칸 one: 복수명사(socks)를 대신하므로 ones를 쓴다. 둘째 빈칸 it: 복수인 장갑을 가리키므로 them을 쓴다. 따라서")], 4,
   "one/ones는 앞에 나온 명사와 같은 종류의 다른 것을 대신하고(복수는 ones), it/them은 앞에 나온 바로 그 대상을 가리킨다.",
   "두 문장과 정답이 원문항과 거의 같았다. 문장을 새로 쓰고, 정답 조합도 원문항(ones - it)과 다르게 ones - them이 되게 했다.", p="These socks are too small. I need bigger _____.\nMy gloves are by the door. Can you bring _____ to me?")

# 3-45 잘못 설명한 학생: 원문항처럼 학생 다섯 명, 여러 대명사 용법, 이름 조합 보기
ST45 = "다음 중 잘못 설명한 학생들을 모두 고르시오."
R45 = "재귀 용법(목적어)의 재귀대명사는 뺄 수 없고, 강조 용법은 빼도 된다. this/that은 단수, these/those는 복수와 쓰며, news는 단수 취급한다. 날씨·시간·거리를 나타내는 it은 비인칭 주어이고, hers·mine 같은 ‘~의 것’은 소유대명사이다."
S45 = "원문항은 학생 다섯 명 중 잘못 설명한 여러 명을 고르는데, 변형은 네 명으로 줄고 ‘없음’ 보기가 생겼으며 틀린 설명이 뻔하거나(B는 정답이 원문항과 이름까지 같았다) 없었다. 원문항처럼 학생 다섯 명과 여러 대명사 용법을 섞어 새로 쓰고, 보기를 이름 조합으로 했다."
def f45(t, lines, judge, wrong, c, a):
    F(3, 45, t, st=ST45, p="\n".join(lines), c=c, a=a, r=R45, pre=["학생별 판정:"] + judge, k=f"잘못 설명한 학생은 {wrong}이다.", n=setnotes(c, wrong, "잘못 설명한 학생"), s=S45 + ipos(a))
f45("B", ["Amy: She herself made the cake.에서 herself는 생략해도 문법적으로 옳아.", "Ben: We enjoyed ourselves.에서 ourselves를 생략해도 옳은 문장이야.", "Chloe: Those shoes is new.는 shoes가 복수이므로 is를 are로 고쳐야 해.",
          "Dan: It is cold today.의 It은 날씨를 나타내는 비인칭 주어야.", "Eve: This is hers.의 hers는 목적격 대명사야."],
    ["Amy 옳음: 강조 용법이라 빼도 된다.", "Ben 틀림: enjoy의 목적어인 재귀 용법이라 뺄 수 없다.", "Chloe 옳음: 복수 주어에는 are를 쓴다.", "Dan 옳음: 날씨의 비인칭 주어 it이다.", "Eve 틀림: hers는 ‘그녀의 것’이라는 소유대명사이다."],
    "Ben, Eve", ["Amy, Ben", "Ben, Eve", "Chloe, Dan", "Ben, Dan, Eve", "Amy, Chloe, Eve"], 2)
f45("C", ["Tom: I hurt myself.의 myself는 재귀 용법이라 생략할 수 없어.", "Jane: This news are good.은 news가 -s로 끝나서 옳은 문장이야.", "Amy: It's Sunday today.의 It과 It's my bag.의 It은 역할이 같아.",
          "Ben: by myself는 ‘혼자서’라는 뜻이야.", "Mia: These is my notebooks.는 옳은 문장이야."],
    ["Tom 옳음: hurt의 목적어인 재귀 용법이다.", "Jane 틀림: news는 단수 취급하므로 is를 쓴다.", "Amy 틀림: 앞의 It은 요일의 비인칭 주어, 뒤의 It은 ‘그것’을 가리키는 대명사이다.",
     "Ben 옳음: by oneself는 ‘혼자서’이다.", "Mia 틀림: 복수명사(notebooks)에는 These are를 쓴다."],
    "Jane, Amy, Mia", ["Tom, Jane", "Amy, Ben", "Jane, Mia", "Jane, Amy, Mia", "Tom, Ben, Mia"], 4)
f45("D", ["Leo: She herself did it.의 herself는 생략해도 옳아.", "Mina: Make yourself at home.은 ‘편하게 있어’라는 관용 표현이야.", "Sam: Help yourselves.는 한 사람에게만 쓰는 표현이야.",
          "Amy: He looked at himself.의 himself는 소유격이야.", "Kai: That is a nice bag, and I want one, too.의 one은 bag을 대신해."],
    ["Leo 옳음: 강조 용법이라 빼도 된다.", "Mina 옳음: 관용 표현이다.", "Sam 틀림: yourselves는 여러 사람에게 쓴다.", "Amy 틀림: himself는 재귀대명사이다.", "Kai 옳음: one은 같은 종류의 물건(bag)을 대신한다."],
    "Sam, Amy", ["Leo, Sam", "Mina, Kai", "Sam, Amy, Kai", "Leo, Mina, Amy", "Sam, Amy"], 5)
f45("E", ["Jane: I did it myself.의 myself는 강조 용법이라 생략해도 옳아.", "Tom: They talked to themselves.에서 themselves를 them으로 바꿔도 뜻이 같아.", "Ben: This scissors is sharp.은 옳은 문장이야.",
          "Mina: It's 7 o'clock.의 It은 시간을 나타내는 비인칭 주어야.", "Leo: The glasses on the table are my.는 옳은 문장이야."],
    ["Jane 옳음: 강조 용법이라 빼도 된다.", "Tom 틀림: them으로 바꾸면 다른 사람들에게 말했다는 뜻이 된다.", "Ben 틀림: scissors는 복수 취급하므로 These scissors are이다.",
     "Mina 옳음: 시간의 비인칭 주어 it이다.", "Leo 틀림: 뒤에 명사가 없으므로 소유대명사 mine을 쓴다."],
    "Tom, Ben, Leo", ["Tom, Ben, Leo", "Jane, Mina", "Tom, Ben", "Ben, Mina, Leo", "Jane, Tom, Leo"], 1)
f45("F", ["Sam: The boy hurt himself.는 주어와 목적어가 같은 대상이야.", "Amy: She herself called me.에서 herself를 빼면 틀린 문장이 돼.", "Tom: Help yourself to the cake.는 ‘케이크를 마음껏 먹어’라는 뜻이야.",
          "Jane: ourselves는 단수 재귀대명사야.", "Kai: It's far from here.의 It은 거리를 나타내는 비인칭 주어야."],
    ["Sam 옳음: 재귀 용법이다.", "Amy 틀림: 강조 용법이라 빼도 옳은 문장이다.", "Tom 옳음: 관용 표현이다.", "Jane 틀림: ourselves는 복수(우리 자신)이다.", "Kai 옳음: 거리의 비인칭 주어 it이다."],
    "Amy, Jane", ["Sam, Amy", "Amy, Tom, Jane", "Amy, Jane", "Jane, Kai", "Sam, Tom, Kai"], 3)

# 3-46 B: 원문항과 같던 요일을 다르게
mk(3, 46, "B", [("Tuesday", "Tuesday: 화요일이므로"), ("Thursday", "Thursday: 목요일이므로"), ("June", "June: 요일이 아니라 6월이므로"), ("Saturday", "Saturday: 토요일이므로"), ("January", "January: 요일이 아니라 1월이므로")], 2,
   "요일은 What day, 월은 What month로 묻고, 요일·월 이름은 대문자로 시작한다.", "대화와 우리말(수요일이야)·정답이 원문항과 같았다. 대화를 바꾸고 요일을 목요일로 바꿨다.",
   p="Kelly: What day is your soccer practice?\nTom: We practice on __________. (목요일에 연습해)")

# 3-47 목적격 고치기: 원문항 발문, 소유격·소유대명사·전치사 결합 오답을 섞음
ST47 = "다음 문장의 밑줄 친 부분을 바르게 고친 것을 고르시오."
R47 = "동사 뒤 목적어 자리에는 목적격(me, us, him, her, them)을 쓴다. 소유격(my, our, their)은 명사 앞에, 소유대명사(mine, ours, theirs)는 ‘~의 것’에 쓰며, 목적어를 바로 받는 동사 뒤에 to를 붙이지 않는다."
S47 = "발문이 ‘주격대명사를 기본 목적격 형태로’라고 정답을 알려 주었고, 보기가 모두 목적격이라 인칭만 맞추면 되었다. 원문항 발문으로 되돌리고, 원문항처럼 소유격·소유대명사·전치사 결합 형태를 오답으로 섞었다."
def n47(x, right, verb):
    if x == right: return f"{x}: 동사({verb}) 뒤 목적어 자리의 목적격으로 알맞으므로"
    if x.startswith("to "): return f"{x}: {verb}는 목적어를 바로 받으므로 to를 붙이지 않으므로"
    if x.endswith("'s"): return f"{x}: ‘주어 + be동사’의 줄임말이라 목적어 자리에 맞지 않으므로"
    if x in ("mine", "ours", "theirs", "hers", "his") and x != right: return f"{x}: ‘~의 것’을 뜻하는 소유대명사라 사람을 가리키는 목적어로 맞지 않으므로"
    return f"{x}: 명사 앞에 쓰는 소유격이라 목적어 자리에 맞지 않으므로"
def f47(t, p, c, a, verb, s=S47):
    mk(3, 47, t, [(x, n47(x, c[a-1], verb)) for x in c], a, R47, s, st=ST47, p=p, okdup=True)
f47("B", "Mr. Kim invited <u>they</u> to his house.", ["their", "them", "to them", "theirs", "to theirs"], 2, "invited", "제시문과 정답이 원문항과 똑같았고 발문이 정답을 알려 주었다. 제시문을 새로 쓰고 원문항 발문으로 되돌렸다.")
f47("C", "Tom called <u>she</u> yesterday.", ["her", "hers", "to her", "to hers", "she's"], 1, "called")
f47("D", "I saw <u>he</u> at school.", ["his", "to him", "he's", "him", "to his"], 4, "saw")
f47("E", "Jane helped <u>they</u> with their homework.", ["their", "theirs", "to them", "to their", "them"], 5, "helped")
f47("F", "Mom gave <u>I</u> a gift.", ["my", "mine", "me", "to my", "to mine"], 3, "gave")

# 3-48 B: 원문항과 같던 제시문을 새로
mk(3, 48, "B", [("The teacher told an interesting story us.", "4형식은 사람(us)을 사물 앞에 두어야 하므로"), ("The teacher us told an interesting story.", "목적어(us)가 동사 앞에 와 어순이 틀렸으므로"),
                ("Told the teacher us an interesting story.", "평서문인데 동사가 주어 앞에 와 어순이 틀렸으므로"), ("The teacher told us an interesting story.", "주어 + 동사 + 사람(목적격) + 사물의 바른 4형식 어순이므로"),
                ("The teacher told we an interesting story.", "동사 뒤 목적어 자리에는 목적격 us를 쓰므로")], 4,
   "4형식 문장은 주어 + 동사 + 간접목적어(사람, 목적격) + 직접목적어(사물) 순서이다.",
   "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘선생님이 우리에게 재미있는 이야기를 해 주셨다’로 바꿨다.",
   p="선생님이 우리에게 재미있는 이야기를 해 주셨다.\n(story / told / teacher / an / us / the / interesting / .)")

# 3-49 재귀 관용 표현: 원문항처럼 동사가 다른 재귀 표현 다섯 개, 발문 설명 삭제
ST49 = "다음 대화의 빈칸에 알맞은 말을 고르시오."
R49 = "Help yourself (to ~)는 ‘(~을) 마음껏 드세요’, Make yourself at home은 ‘편하게 있어요’, Enjoy yourself는 ‘즐거운 시간 보내요’, Behave yourself는 ‘얌전히 굴어라’라는 관용 표현이다. 한 명에게는 yourself, 여러 명에게는 yourselves를 쓴다."
S49 = "원문항은 뜻에 맞는 관용 표현을 동사가 다른 재귀 표현 중에서 고르는 문항인데, 변형은 발문이 ‘음식을 마음껏 먹으라고 권하는 말’이라고 알려 주었고 보기가 모두 help + 재귀대명사라 인칭·수만 맞추는 문항이 되었다. 원문항 발문과 형식(우리말 뜻 + 동사가 다른 재귀 표현 다섯 개)으로 다시 썼다."
MEAN = {"help": "‘마음껏 드세요’", "make": "‘편하게 있어요(at home과 함께)’", "enjoy": "‘즐거운 시간 보내요’", "take": "관용 표현으로 쓰이지 않는", "hurt": "‘다치다’", "teach": "‘독학하다’", "behave": "‘얌전히 굴다’", "eat": "관용 표현으로 쓰이지 않는"}
def f49(t, p, c, a, s=S49):
    items = []
    for i, x in enumerate(c):
        v = x.split()[0].lower()
        items.append((x, f"{x}: {MEAN[v]} 표현이라 우리말 뜻에 {'맞으므로' if i + 1 == a else '맞지 않으므로'}"))
    mk(3, 49, t, items, a, R49, s, st=ST49, p=p, okdup=True)
f49("B", "A: Welcome, Tom! Come in and sit down.\nB: Thanks!\nA: Please ____________ at home.\n(편하게 있어.)", ["help yourself", "enjoy yourself", "make yourself", "take yourself", "hurt yourself"], 3)
f49("C", "A: Kids, there is cake on the table.\nB: Great!\nA: Please ____________ to the cake.\n(케이크를 마음껏 먹으렴.)", ["make yourselves", "help yourselves", "enjoy yourselves", "take yourselves", "teach yourselves"], 2)
f49("D", "A: I'm going to the school festival tonight.\nB: Great! ____________!\n(즐거운 시간 보내!)", ["Help yourself", "Make yourself", "Hurt yourself", "Enjoy yourself", "Take yourself"], 4)
f49("E", "A: Tom and Jane, the museum is a quiet place.\nB: Okay.\nA: Please ____________ inside.\n(안에서는 얌전히 행동하렴.)", ["behave yourselves", "help yourselves", "enjoy yourselves", "make yourselves", "take yourselves"], 1)
f49("F", "A: Jane, there are sandwiches here.\nB: Thanks!\nA: Please ____________ to them.\n(마음껏 먹어.)", ["enjoy yourself", "make yourself", "eat yourself", "take yourself", "help yourself"], 5)

# 3-50 재귀대명사 옳은 문장 개수: 원문항 발문·형식(ⓐ~ⓔ, 1개~5개), 정답 개수를 유형마다 다르게
ST50 = "다음 중 어법상 옳은 문장의 개수는?"
R50 = "주어와 목적어가 같은 대상이면 목적어 자리에 재귀대명사(myself, yourself, himself, herself, ourselves, yourselves, themselves)를 쓴다. ourself·themself·theirselves·herselves 같은 형태는 쓰지 않는다."
S50 = "발문에 ‘밑줄 친 대명사만 그 절의 주어와 같은 대상’ 등 긴 조건이 붙었고, 원문항에 없던 밑줄이 생겼으며, 보기 기호가 a~e로 바뀌어 한 줄로 이어지고 선택지 순서가 뒤섞였다. 원문항 발문과 형식(ⓐ~ⓔ 줄바꿈, 1개~5개)으로 되돌렸다."
def f50(t, lines, judge, ok, s=S50):
    n = len(ok.split(","))
    F(3, 50, t, st=ST50, p="\n".join(lines), c=CNT5, a=n, r=R50, pre=["문장별 판정: " + j for j in judge], k=f"어법상 옳은 문장은 {ok}로 {n}개이다.", n="cnt", s=s + ipos(n))
f50("B", ["ⓐ He introduced himself to the class.", "ⓑ We should respect us.", "ⓒ Please help yourself to the pizza.", "ⓓ I burned me while cooking.", "ⓔ They taught themselfs English."],
    ["ⓐ O. 주어와 목적어가 같아 himself를 썼다.", "ⓑ X. 주어(We)와 목적어가 같으므로 ourselves를 쓴다.", "ⓒ O. Help yourself to ~는 관용 표현이다.", "ⓓ X. 주어(I)와 목적어가 같으므로 myself를 쓴다.", "ⓔ X. themselves로 쓴다."],
    "ⓐ, ⓒ", "문장이 원문항과 거의 같았고 정답 개수(3개)도 같았으며 발문 조건·기호·선택지 순서도 원본과 달랐다. 문장을 새로 쓰고 원문항 발문과 형식으로 되돌렸으며 정답 개수를 2개로 바꿨다.")
f50("C", ["ⓐ I did it myself.", "ⓑ Tom hurt himself.", "ⓒ Jane enjoyed herself.", "ⓓ We helped us to cake.", "ⓔ They saw themselves in the mirror."],
    ["ⓐ O. 강조 용법의 myself이다.", "ⓑ O. 주어와 목적어가 같아 himself를 썼다.", "ⓒ O. enjoy oneself이다.", "ⓓ X. 주어(We)와 목적어가 같으므로 ourselves를 쓴다.", "ⓔ O. 주어와 목적어가 같아 themselves를 썼다."], "ⓐ, ⓑ, ⓒ, ⓔ")
f50("D", ["ⓐ Help you to the cake, Tom.", "ⓑ My parents enjoyed theirselves at the party.", "ⓒ She herself called me.", "ⓓ I hurt myself.", "ⓔ We did it ourself."],
    ["ⓐ X. Help yourself to ~로 쓴다.", "ⓑ X. themselves로 쓴다.", "ⓒ O. 강조 용법의 herself이다.", "ⓓ O. 주어와 목적어가 같아 myself를 썼다.", "ⓔ X. 복수 주어(We)의 재귀대명사는 ourselves이다."], "ⓒ, ⓓ",
    S50 + " 정답 개수가 원문항(3개)과 같지 않게 ⓐ·ⓑ를 틀린 문장으로 바꿔 2개로 했다.")
f50("E", ["ⓐ Make yourselves at home, girls.", "ⓑ He did it by himself.", "ⓒ Jane looked at herself.", "ⓓ The boys enjoyed themself.", "ⓔ I myself finished it."],
    ["ⓐ O. 여러 사람에게 yourselves를 썼다.", "ⓑ O. by oneself(혼자서)이다.", "ⓒ O. 전치사 뒤 목적어가 주어와 같아 herself를 썼다.", "ⓓ X. 복수 주어(The boys)의 재귀대명사는 themselves이다.", "ⓔ O. 강조 용법의 myself이다."], "ⓐ, ⓑ, ⓒ, ⓔ", S50)
f50("F", ["ⓐ You should believe in you.", "ⓑ We enjoyed us.", "ⓒ Tom hurt himself.", "ⓓ Jane did it herselves.", "ⓔ The children helped themself."],
    ["ⓐ X. 주어(You)와 목적어가 같으므로 yourself를 쓴다.", "ⓑ X. 주어(We)와 목적어가 같으므로 ourselves를 쓴다.", "ⓒ O. 주어와 목적어가 같아 himself를 썼다.", "ⓓ X. herself로 쓴다.", "ⓔ X. themselves로 쓴다."], "ⓒ",
    S50 + " 다른 유형과 정답 개수가 겹치지 않게 틀린 문장을 늘려 옳은 문장이 1개가 되게 했다.")
