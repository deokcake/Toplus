# 2급 CH5 대명사 (41~50) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 2-41 the other: 뜻을 풀어 주던 발문을 원문항대로
for t in "BCDEF":
    F(2, 41, t, st="R", xr=[("여기서는 둘 중 정해진 나머지 하나를 뜻하도록 요구했으므로 the other이다.", "여기서는 둘 중 정해진 나머지 하나이므로 the other이다.")],
      s="발문이 ‘두 대상 중 정해진 나머지 하나를 가리키도록’이라고 the other의 뜻을 풀어 주어, 원문항 발문 ‘빈칸에 들어갈 말로 알맞은 것’으로 되돌렸다. 앞에 ‘Two …’가 있어 조건 없이도 정답은 하나다.")

# 2-43 one / it: 원문항 발문, 유형마다 다른 문장 틀
R43 = "it은 앞서 말한 바로 그 대상을 다시 가리킨다. one은 앞의 단수 가산명사와 같은 종류의 다른 하나를 가리키며, a new one·the bigger one·this one처럼 수식어와 함께 쓸 수 있다."
S43 = "발문이 ‘one 또는 it을 넣을 때’라고 두 후보를 알려 주었고, 문장 틀(I lost my … / a spare … / a larger … / a blue …)이 유형마다 반복되었다. 원문항 발문으로 되돌리고 유형마다 다른 문장 틀로 새로 썼다."
def ONE(what): return f"빈칸: {what}와(과) 같은 종류의 다른 하나를 가리키므로 one이 들어간다. 나머지와 같으므로"
def IT(what): return f"빈칸: 앞에 나온 바로 그 {what}을(를) 가리키므로 it이 들어가 나머지 넷(one)과 다르므로"
mk(2, 43, "B", [("This cap is too tight. Do you have a looser _____?", ONE("모자")), ("I don't have an eraser. Can you lend me _____?", ONE("지우개")),
                ("Jane baked a pie and shared _____ with her neighbors.", IT("파이")), ("There are two parks near here. Let's go to the bigger _____.", ONE("공원")),
                ("Which bus should I take, this one or that _____?", ONE("버스"))], 3, R43, S43, st="R")
mk(2, 43, "C", [("My old laptop is too slow. I want a faster _____.", ONE("노트북")), ("I prefer the round table to the square _____.", ONE("탁자")),
                ("Mom needs a basket. Is there an extra _____ in the car?", ONE("바구니")), ("I've read many novels, but this is the best _____ so far.", ONE("소설")),
                ("Tom got a guitar for his birthday and plays _____ every day.", IT("기타"))], 5, R43, S43, st="R")
mk(2, 43, "D", [("My grandpa built a boat and sailed _____ across the lake.", IT("배")), ("This bag is too heavy. Do you have a lighter _____?", ONE("가방")),
                ("I have a black pen and a red _____.", ONE("펜")), ("If you need a charger, I can give you _____.", ONE("충전기")),
                ("The first test was easy, but the second _____ was hard.", ONE("시험"))], 1, R43, S43, st="R")
mk(2, 43, "E", [("We need a bigger tent. This _____ is too small.", ONE("텐트")), ("Is there a bank near here? — Yes, there's _____ across the street.", ONE("은행")),
                ("I don't want a window seat. I'd like an aisle _____.", ONE("좌석")), ("Grandma knitted a scarf, and I wear _____ every winter.", IT("목도리")),
                ("Every student got a card, and mine was the prettiest _____.", ONE("카드"))], 4, R43, S43, st="R")
mk(2, 43, "F", [("Should I buy a paper map or a digital _____?", ONE("지도")), ("We saw a rainbow and took a picture of _____.", IT("무지개")),
                ("My computer is old. I'm saving money for a better _____.", ONE("컴퓨터")), ("There are three bridges, and this is the longest _____.", ONE("다리")),
                ("I need a ruler. Is there _____ in your pencil case?", ONE("자"))], 2, R43, S43, st="R")

# 2-44 강조 용법: 재귀 용법 오답을 유형마다 새로
R44 = "재귀대명사가 동사·전치사의 목적어로 주어와 같은 대상을 가리키면 재귀 용법이라 뺄 수 없다. 주어를 강조해 ‘직접’의 뜻을 더하면 강조 용법이며 빼도 문장이 성립한다."
S44 = "재귀 용법 오답 네 문장이 B와 똑같아서 유형마다 새로 썼다."
def RF(v): return f"재귀 용법: {v}의 목적어로 주어 자신을 가리켜 뺄 수 없으므로"
EMP = "강조 용법: 주어를 강조해 ‘직접’의 뜻을 더하며 빼도 문장이 성립해 〈보기〉와 쓰임이 같으므로"
def P44(t): return "<보기>\n" + V(2, 44, t)["passage"]
S44B = "발문은 ‘(보기)와 같은 것’인데 본문에 <보기> 표시가 없었다(원문항에서 고친 결함과 같음). 본문 앞에 <보기>를 붙였다. 보기와 정답은 그대로다."
F(2, 44, "B", p=P44("B"), s=S44B)
mk(2, 44, "C", [("Help <u>yourself</u> to the cookies.", RF("동사 help")), ("He taught <u>himself</u> to play the guitar.", RF("동사 taught")), ("Jane <u>herself</u> repaired the bicycle.", EMP),
                ("The cat is washing <u>itself</u>.", RF("동사 washing")), ("We should take care of <u>ourselves</u>.", RF("전치사 of"))], 3, R44, S44 + " 본문 앞에 빠진 <보기> 표시를 붙였다.", p=P44("C"))
mk(2, 44, "D", [("She cut <u>herself</u> on the broken glass.", RF("동사 cut")), ("We <u>ourselves</u> prepared the meal.", EMP), ("I bought <u>myself</u> a new watch.", RF("동사 bought")),
                ("They talked about <u>themselves</u> for hours.", RF("전치사 about")), ("Make <u>yourself</u> at home.", RF("동사 make"))], 2, R44, S44 + " 본문 앞에 빠진 <보기> 표시를 붙였다.", p=P44("D"))
mk(2, 44, "E", [("She was talking to <u>herself</u>.", RF("전치사 to")), ("I told <u>myself</u> not to give up.", RF("동사 told")), ("They dried <u>themselves</u> with towels.", RF("동사 dried")),
                ("Be careful not to burn <u>yourself</u>.", RF("동사 burn")), ("Tom <u>himself</u> wrote the speech.", EMP)], 5, R44, S44 + " 본문 앞에 빠진 <보기> 표시를 붙였다.", p=P44("E"))
mk(2, 44, "F", [("You <u>yourself</u> said it was true.", EMP), ("He considers <u>himself</u> lucky.", RF("동사 considers")), ("We found <u>ourselves</u> in a strange town.", RF("동사 found")),
                ("She pushed <u>herself</u> to finish the race.", RF("동사 pushed")), ("Please behave <u>yourselves</u>.", RF("동사 behave"))], 1, R44, S44 + " 본문 앞에 빠진 <보기> 표시를 붙였다.", p=P44("F"))

# 2-45 학생 설명: 원문항처럼 대명사의 여러 용법을 섞고, 옳게 설명한 학생 수를 유형마다 다르게
R45 = "가목적어 it은 목적어 자리에 먼저 오고 진목적어(to부정사·that절)는 뒤에 온다. some은 긍정문·권유·부탁, any는 부정문·의문문에 주로 쓴다. each/every + 단수명사, each of + 복수명사는 단수 동사를 쓴다. 재귀 용법은 뺄 수 없고 강조 용법은 뺄 수 있다. others는 막연한 다른 몇몇, the others는 정해진 나머지 전부이다."
S45 = "원문항은 대명사의 여러 용법(가목적어 it, some/any, each, 재귀대명사, others)을 학생 설명으로 묻는데, 변형은 가목적어 it만 다뤄 범위가 좁았고 모든 유형에서 ‘비인칭 it을 가목적어라고 한 학생’ 하나만 틀려 정답 구조가 예측되었다. 원문항처럼 여러 용법을 섞어 학생 설명 다섯 개를 새로 쓰고, 옳게 설명한 학생 수를 유형마다 달리했다."
def f45(t, lines, judge, ok, c, a):
    F(2, 45, t, p="\n".join(lines), c=c, a=a, r=R45, pre=["학생별 판정:"] + judge, k=f"올바르게 설명한 학생은 {ok}이다.", n=setnotes(c, ok, "올바르게 설명한 학생"), s=S45 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f45("B", ["Mina: We found it impossible to finish in one day. 에서 it은 가목적어야.", "Leo: Would you like some tea? 에서 권유하는 의문문이라 some을 쓸 수 있어.",
          "Jane: Each of the boys have a locker. 는 맞는 문장이야.", "Ben: She hurt herself. 에서 herself는 생략해도 문장이 온전해.",
          "Sora: Some people like summer, and others like winter. 에서 others는 나머지 모든 사람을 뜻해."],
    ["Mina 옳음: it이 목적어 자리에 먼저 오고 진목적어 to finish in one day가 뒤에 왔다.", "Leo 옳음: 권유하는 의문문에는 some을 쓸 수 있다.", "Jane 틀림: each of + 복수명사는 단수 동사를 쓰므로 has가 맞다.",
     "Ben 틀림: hurt의 목적어인 재귀 용법이라 빼면 문장이 성립하지 않는다.", "Sora 틀림: others는 막연한 다른 몇몇이고, 나머지 전부는 the others이다."],
    "Mina, Leo", ["Mina, Jane", "Mina, Leo", "Leo, Ben", "Mina, Leo, Sora", "Jane, Ben, Sora"], 2)
f45("C", ["Tom: I think it strange that nobody called. 에서 it은 가목적어야.", "Amy: Do you have any brothers? 에서 any는 의문문이라 쓰였어.",
          "Jin: Each student have a different dream. 은 맞는 문장이야.", "Mia: I enjoyed myself at the party. 에서 myself는 강조 용법이라 생략해도 돼.",
          "Leo: I have three pens. One is black, and the others are red. 에서 the others는 나머지 두 자루 전부를 뜻해."],
    ["Tom 옳음: it이 목적어 자리에 먼저 오고 진목적어 that절이 뒤에 왔다.", "Amy 옳음: 의문문에는 any를 주로 쓴다.", "Jin 틀림: each + 단수명사는 단수 동사를 쓰므로 has로 고쳐야 한다.",
     "Mia 틀림: enjoy의 목적어인 재귀 용법이라 뺄 수 없다.", "Leo 옳음: 세 자루 중 하나를 뺀 정해진 나머지 전부이므로 the others이다."],
    "Tom, Amy, Leo", ["Tom, Amy", "Amy, Jin, Mia", "Tom, Jin, Leo", "Tom, Amy, Leo", "Jin, Mia, Leo"], 4)
f45("D", ["Jane: It takes an hour to get there. 에서 it은 가목적어야.", "Ben: I don't have some money. 는 부정문이라 some을 any로 고쳐야 해.",
          "Sora: Each of the players wear a helmet. 은 맞는 문장이야.", "Tom: He himself fixed the roof. 에서 himself는 생략해도 문장이 온전해.",
          "Amy: I have two sisters. One is a nurse, and the other is a teacher. 에서 the other는 나머지 한 명을 뜻해."],
    ["Jane 틀림: 문장 맨 앞의 it은 가주어(진주어 to get there)이며 가목적어가 아니다.", "Ben 옳음: 부정문에는 any를 주로 쓴다.", "Sora 틀림: each of + 복수명사는 단수 동사를 쓰므로 wears가 맞다.",
     "Tom 옳음: 주어를 강조하는 강조 용법이라 빼도 문장이 성립한다.", "Amy 옳음: 둘 중 하나를 뺀 정해진 나머지 하나이므로 the other이다."],
    "Ben, Tom, Amy", ["Ben, Tom", "Jane, Ben, Sora", "Jane, Tom, Amy", "Ben, Tom, Amy", "Sora, Amy"], 4)
f45("E", ["Mina: She made it clear that she disagreed. 에서 it은 가목적어야.", "Leo: Can I have any water? 는 부탁하는 말이라 any가 자연스러워.",
          "Jane: Every student have to wear a uniform. 은 맞는 문장이야.", "Ben: The door opened by itself. 에서 by itself는 ‘저절로’라는 뜻이야.",
          "Sora: Some of the cookies are gone, and the others are in the box. 에서 the others는 남은 쿠키 전부를 뜻해."],
    ["Mina 옳음: it이 목적어 자리에 먼저 오고 진목적어 that절이 뒤에 왔다.", "Leo 틀림: 부탁하는 의문문에는 some을 쓴다(Can I have some water?).", "Jane 틀림: every + 단수명사는 단수 동사를 쓰므로 has to가 맞다.",
     "Ben 옳음: by itself는 ‘저절로’라는 뜻이다.", "Sora 옳음: 일부를 뺀 정해진 나머지 전부이므로 the others이다."],
    "Mina, Ben, Sora", ["Mina, Ben, Sora", "Mina, Leo", "Leo, Jane, Ben", "Mina, Jane, Sora", "Ben, Sora"], 1)
f45("F", ["Tom: I found it hard to wake up early. 에서 진목적어는 to wake up early야.", "Amy: Would you like some cookies? 에서 some은 권유할 때 쓴 거야.",
          "Jin: Each of my friends has a bike. 는 맞는 문장이야.", "Mia: Kevin cut himself while cooking. 에서 himself를 빼도 문장이 온전해.",
          "Leo: Ten people came. Five stayed, and others left early. 에서 others는 남은 다섯 명 전부를 뜻해."],
    ["Tom 옳음: 가목적어 it의 진목적어는 뒤의 to wake up early이다.", "Amy 옳음: 권유하는 의문문에는 some을 쓸 수 있다.", "Jin 옳음: each of + 복수명사는 단수 동사(has)를 쓴다.",
     "Mia 틀림: cut의 목적어인 재귀 용법이라 뺄 수 없다.", "Leo 틀림: 남은 다섯 명 전부는 the others로 나타내며, others는 막연한 다른 몇몇이다."],
    "Tom, Amy, Jin", ["Tom, Amy", "Amy, Jin, Mia", "Tom, Amy, Jin", "Tom, Jin, Leo", "Tom, Amy, Jin, Mia"], 3)

# 2-47 another / the other(s): 원문항 발문, 해설 다시 쓰기
R47 = "one을 먼저 말한 뒤 또 다른 하나는 another로 나타낸다. 마지막에 정해진 하나만 남으면 the other, 정해진 나머지가 여럿이면 the others를 쓴다."
S47 = "발문이 ‘첫째 빈칸은 다른 하나, 둘째 빈칸은 정해진 나머지 전부’라고 정답의 뜻을 풀어 주어, 원문항 발문(빈칸에 들어갈 말이 순서대로 짝지어진 것)으로 되돌렸다."
FIRST = {"the other": "아직 남은 것이 둘 이상인데 ‘정해진 마지막 하나’를 뜻하는 말을 써서 맞지 않는다.", "the others": "복수여서 단수 동사와 맞지 않는다.",
         "other": "관사 없이 단수 대명사로 쓸 수 없다.", "others": "복수여서 단수 동사와 맞지 않는다."}
SEC1 = {"the others": "남은 것이 하나뿐이고 동사도 단수이므로 맞지 않는다.", "others": "복수여서 단수 동사와 맞지 않고, 정해진 나머지도 나타내지 못한다.",
        "another": "마지막으로 남은 정해진 하나는 the other로 나타내므로 맞지 않는다.", "the other": ""}
SECN = {"the other": "남은 것이 여럿이고 동사도 복수(are)이므로 단수인 the other는 맞지 않는다.", "another": "단수여서 복수 동사(are)와 맞지 않는다.",
        "others": "막연한 다른 몇몇을 뜻해 정해진 나머지 전부를 가리키지 못한다."}
def f47(t, c, a, total, rest, s="", **kw):
    plural = rest > 1; good2 = "the others" if plural else "the other"
    nn = []
    for i, ch in enumerate(c):
        x, y = [p.strip() for p in ch.split(" - ")]
        if i + 1 == a: nn.append(f"첫째 빈칸 another, 둘째 빈칸 {good2}로 모든 자리가 알맞으므로 정답이다."); continue
        bits = []
        if x != "another": bits.append(f"첫째 빈칸 {x}: {FIRST[x]}")
        if y != good2: bits.append(f"둘째 빈칸 {y}: {(SECN if plural else SEC1)[y]}")
        nn.append(" ".join(bits) + " 따라서 오답이다.")
    F(2, 47, t, st="R", c=c, a=a, r=R47, n=nn, k=f"전체 {total}개(명) 중 처음 하나는 one, 또 다른 하나는 another이고, 정해진 나머지 {rest}개(명)는 {good2}로 나타낸다.", s=S47 + s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
f47("B", V(2, 47, "B")["c"], 1, 3, 1)
f47("C", ["another - others", "the other - another", "another - the other", "other - the others", "the others - another"], 3, 3, 1, " 정답 위치가 B와 같아 보기 순서를 바꿨다.")
f47("D", ["other - the others", "the other - the others", "the others - another", "the other - another", "another - the others"], 5, 5, 3,
    " 남은 것이 여럿(are)인 문장이라 조건이 없으면 ‘another - others’도 답으로 볼 여지가 있어 그 보기를 ‘the other - the others’로 바꿨다.")
f47("E", V(2, 47, "E")["c"], 2, 3, 1)
f47("F", ["another - the other", "other - the others", "the others - another", "another - the others", "the other - another"], 4, 6, 4,
    " 남은 것이 여럿(are)인 문장이라 조건이 없으면 ‘another - others’도 답으로 볼 여지가 있어 그 보기를 ‘another - the other’로 바꾸고, 정답 위치가 D와 같아 순서를 바꿨다.")

# 2-49 재귀대명사 짝: 원문항 발문·밑줄, 조건 없이도 정답이 하나가 되도록 보기 조정
ST49 = "다음 문장의 빈칸 (A), (B)에 들어갈 재귀대명사가 바르게 연결된 것은?"
UA, UB = "(<u>     A     </u>)", "(<u>     B     </u>)"
R49 = "재귀대명사는 주어와 같은 대상을 가리키며 주어의 인칭·수에 맞춘다. by oneself는 ‘혼자서, 스스로’라는 뜻이다."
S49 = "발문이 ‘(A)는 단수 they에 대응하는 재귀대명사, (B)는 주어에 맞춘다’라고 판단 규칙을 알려 주었고 빈칸 밑줄이 없었다. 원문항 발문과 밑줄로 되돌렸다. 고친 원문항처럼 (A) 문장의 주어를 복수로 바꿔, himself도 맞다는 논란 없이 themselves만 답이 되게 했다."
def f49(t, p, c, a, needA, needB, badA, badB, s=""):
    nn = []
    for i, ch in enumerate(c):
        m = re.match(r"\(A\) (\S+) - \(B\) (\S+)", ch); x, y = m.group(1), m.group(2)
        if i + 1 == a: nn.append(f"{needA} {needB} 두 자리가 모두 알맞으므로 정답이다."); continue
        bits = []
        if x in badA: bits.append(f"(A) {x}: {badA[x]}")
        if y in badB: bits.append(f"(B) {y}: {badB[y]}")
        nn.append(" ".join(bits) + " 따라서 오답이다.")
    F(2, 49, t, st=ST49, p=p.replace("(A)", UA).replace("(B)", UB), c=c, a=a, r=R49, n=nn, k=f"{needA} {needB}", s=S49 + s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
GA = {"ourselves": "1인칭 복수라 3인칭 주어와 맞지 않는다.", "yourself": "2인칭이라 3인칭 주어와 맞지 않는다.", "yourselves": "2인칭이라 3인칭 주어와 맞지 않는다.",
      "myself": "1인칭이라 3인칭 주어와 맞지 않는다.", "herself": "한 사람을 가리키는 말이라 복수 주어와 맞지 않는다.", "himself": "한 사람을 가리키는 말이라 복수 주어와 맞지 않는다."}
f49("B", "All participants should prepare (A) before the interview.\nMina completed the entire design by (B). She worked alone.",
    ["(A) ourselves - (B) herself", "(A) himself - (B) themselves", "(A) themselves - (B) herself", "(A) themselves - (B) himself", "(A) yourself - (B) myself"], 3,
    "(A)는 복수 주어(All participants)와 같은 사람들을 가리키므로 themselves이다.", "(B)는 주어 Mina(She)와 같은 사람이므로 herself이다.",
    GA, {"themselves": "주어(Mina)가 한 사람이므로 맞지 않는다.", "himself": "주어(Mina)를 She로 받았으므로 맞지 않는다.", "myself": "1인칭이라 주어(Mina)와 맞지 않는다."})
f49("C", "All children should be proud of (A).\nMina, you should believe in (B).",
    ["(A) ourselves - (B) yourself", "(A) themselves - (B) myself", "(A) themselves - (B) yourselves", "(A) themselves - (B) yourself", "(A) himself - (B) ourselves"], 4,
    "(A)는 복수 주어(All children)와 같은 사람들을 가리키므로 themselves이다.", "(B)는 한 사람(Mina)에게 말하는 you이므로 yourself이다.",
    GA, {"myself": "1인칭이라 주어(you)와 맞지 않는다.", "yourselves": "여러 사람에게 말할 때 쓰므로 한 사람(Mina)에게는 맞지 않는다.", "ourselves": "1인칭 복수라 주어(you)와 맞지 않는다."},
    " (B) 문장의 you가 한 명인지 여러 명인지 발문 괄호로 알려 주던 것을 ‘Mina, you …’로 문장 안에서 드러냈다.")
f49("D", "People should not blame (A) for every small mistake.\nI completed the entire project by (B).",
    ["(A) ourselves - (B) myself", "(A) themselves - (B) myself", "(A) themselves - (B) ourselves", "(A) myself - (B) themselves", "(A) himself - (B) yourself"], 2,
    "(A)는 복수 주어(People)와 같은 사람들을 가리키므로 themselves이다.", "(B)는 주어 I와 같은 사람이므로 myself이다.",
    GA, {"ourselves": "1인칭 복수라 주어(I)와 맞지 않는다.", "themselves": "3인칭 복수라 주어(I)와 맞지 않는다.", "yourself": "2인칭이라 주어(I)와 맞지 않는다."})
f49("E", "All students need to challenge (A).\nMy sister and I cooked dinner by (B).",
    ["(A) themselves - (B) ourselves", "(A) ourselves - (B) themselves", "(A) himself - (B) themselves", "(A) themselves - (B) myself", "(A) yourselves - (B) ourselves"], 1,
    "(A)는 복수 주어(All students)와 같은 사람들을 가리키므로 themselves이다.", "(B)는 주어 My sister and I(우리)와 같은 사람들이므로 ourselves이다.",
    GA, {"themselves": "3인칭 복수라 나를 포함한 주어(My sister and I)와 맞지 않는다.", "myself": "한 사람이라 두 사람인 주어(My sister and I)와 맞지 않는다."},
    " (B)의 ‘They should support (B).’는 them(다른 사람들)도 들어갈 수 있어 ‘My sister and I cooked dinner by (B).’로 바꿨다.")
f49("F", "The participants introduced (A) before the discussion.\nThe machine turns off by (B) at night.",
    ["(A) ourselves - (B) itself", "(A) themselves - (B) themselves", "(A) himself - (B) herself", "(A) yourself - (B) ourselves", "(A) themselves - (B) itself"], 5,
    "(A)는 복수 주어(The participants)와 같은 사람들을 가리키므로 themselves이다.", "(B)는 주어 The machine(사물 하나)과 같은 대상이므로 itself이다.",
    GA, {"themselves": "복수라 사물 하나인 주어(The machine)와 맞지 않는다.", "herself": "사람을 가리키는 말이라 사물 주어(The machine)와 맞지 않는다.", "ourselves": "1인칭 복수라 주어(The machine)와 맞지 않는다."},
    " 다른 유형과 겹치지 않게 (B)를 ‘by itself(저절로)’ 문장으로 바꿨다.")

# 2-50 수 일치: 원문항처럼 all of / each of 등 + 명사 뒤 동사의 수 일치, 원문항 발문
ST50 = "다음 중 밑줄 친 부분이 어법상 옳은 문장으로만 묶인 것을 고르시오."
R50 = "all of / most of / some of + 명사 뒤의 동사는 of 뒤 명사에 수를 맞춘다(불가산명사 → 단수, 복수명사 → 복수). each of + 복수명사, one of + 복수명사, every + 단수명사는 단수 동사를 쓴다."
S50 = "원문항은 all of / each of 뒤의 수 일치를 묻는데, 변형은 불가산명사의 복수형과 단수 they로 평가 요소가 바뀌었고 발문에 괄호 조건이 붙었다. 원문항 발문으로 되돌리고, 원문항처럼 all of / each of 등 + 명사 뒤 동사의 수 일치 문장으로 다시 썼다. 문장마다 줄을 바꿨다."
def f50(t, lines, judge, ok, c, a):
    F(2, 50, t, st=ST50, p="\n".join(lines), c=c, a=a, r=R50, pre=["문장별 판정: " + j for j in judge], k=f"옳은 문장은 {ok}이고, 이 문장들로만 묶인 보기가 정답이다.",
      n=setnotes(c, ok, "옳은 문장"), s=S50 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f50("B", ["(A) All of the furniture <u>is</u> new.", "(B) Each of the girls <u>have</u> a phone.", "(C) Most of the students <u>walk</u> to school.", "(D) One of my friends <u>live</u> in Busan.", "(E) Some of the water <u>were</u> spilled."],
    ["(A) O. furniture는 불가산명사라 단수 동사(is)를 쓴다.", "(B) X. each of + 복수명사는 단수 동사를 쓴다. 교정: has", "(C) O. of 뒤 students가 복수라 복수 동사(walk)를 쓴다.",
     "(D) X. one of + 복수명사는 단수 동사를 쓴다. 교정: lives", "(E) X. water는 불가산명사라 단수 동사를 쓴다. 교정: was"],
    "(A), (C)", ["(A), (C)", "(A), (B)", "(C), (D)", "(A), (C), (E)", "(B), (D), (E)"], 1)
f50("C", ["(A) All of the money <u>was</u> stolen.", "(B) Each of the rooms <u>has</u> a window.", "(C) All of my classmates <u>likes</u> pizza.", "(D) Some of the cookies <u>was</u> burned.", "(E) Every student <u>need</u> a pencil."],
    ["(A) O. money는 불가산명사라 단수 동사(was)를 쓴다.", "(B) O. each of + 복수명사는 단수 동사(has)를 쓴다.", "(C) X. of 뒤 classmates가 복수라 복수 동사를 쓴다. 교정: like",
     "(D) X. of 뒤 cookies가 복수라 복수 동사를 쓴다. 교정: were", "(E) X. every + 단수명사는 단수 동사를 쓴다. 교정: needs"],
    "(A), (B)", ["(A), (C)", "(B), (D)", "(A), (B)", "(B), (C), (E)", "(A), (D), (E)"], 3)
f50("D", ["(A) All of the news <u>were</u> shocking.", "(B) Each of the players <u>wears</u> a number.", "(C) Most of the milk <u>has</u> gone bad.", "(D) All of the windows <u>was</u> open.", "(E) One of the teachers <u>is</u> from Canada."],
    ["(A) X. news는 불가산명사라 단수 동사를 쓴다. 교정: was", "(B) O. each of + 복수명사는 단수 동사(wears)를 쓴다.", "(C) O. milk는 불가산명사라 단수 동사(has)를 쓴다.",
     "(D) X. of 뒤 windows가 복수라 복수 동사를 쓴다. 교정: were", "(E) O. one of + 복수명사는 단수 동사(is)를 쓴다."],
    "(B), (C), (E)", ["(A), (B)", "(C), (D)", "(A), (C), (E)", "(B), (D), (E)", "(B), (C), (E)"], 5)
f50("E", ["(A) All of the homework <u>are</u> done.", "(B) Each of us <u>is</u> ready.", "(C) Some of the books <u>are</u> missing.", "(D) Most of the cake <u>were</u> eaten.", "(E) All of the students <u>was</u> tired."],
    ["(A) X. homework는 불가산명사라 단수 동사를 쓴다. 교정: is", "(B) O. each of + 복수 대명사도 단수 동사(is)를 쓴다.", "(C) O. of 뒤 books가 복수라 복수 동사(are)를 쓴다.",
     "(D) X. of 뒤 cake가 한 덩어리(단수)라 단수 동사를 쓴다. 교정: was", "(E) X. of 뒤 students가 복수라 복수 동사를 쓴다. 교정: were"],
    "(B), (C)", ["(A), (B)", "(B), (C)", "(C), (D)", "(A), (C), (E)", "(B), (D), (E)"], 2)
f50("F", ["(A) All of the luggage <u>was</u> lost.", "(B) Each of the classrooms <u>have</u> a projector.", "(C) One of the boys <u>plays</u> the violin.", "(D) All of my shoes <u>is</u> dirty.", "(E) Most of the people <u>agree</u> with you."],
    ["(A) O. luggage는 불가산명사라 단수 동사(was)를 쓴다.", "(B) X. each of + 복수명사는 단수 동사를 쓴다. 교정: has", "(C) O. one of + 복수명사는 단수 동사(plays)를 쓴다.",
     "(D) X. of 뒤 shoes가 복수라 복수 동사를 쓴다. 교정: are", "(E) O. of 뒤 people이 복수라 복수 동사(agree)를 쓴다."],
    "(A), (C), (E)", ["(A), (B)", "(C), (D)", "(B), (C), (E)", "(A), (C), (E)", "(A), (D), (E)"], 4)
