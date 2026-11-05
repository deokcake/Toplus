# 2급 CH6 to부정사 (51~60) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def talk(g, n, t, items, a, r, s, who="학생", **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[w + (" 틀린 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.") for i, (_, w) in enumerate(items)],
      k=f"설명이 틀린 {who}은 {items[a-1][0].split(':')[0]}이다. {items[a-1][1]}", s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 2-52 of가 들어갈 수 없는 것: 원문항 발문, 원문항처럼 of 문장 넷 + for 문장 하나
R52 = "kind·brave·generous·careless·rude처럼 그 행동을 한 사람의 성품을 평가하는 형용사 뒤에는 of + 목적격을, important·necessary·difficult·easy·dangerous처럼 행동 자체를 판단하는 형용사 뒤에는 for + 목적격을 의미상 주어로 쓴다."
def OF(adj): return f"{adj}: 행동한 사람의 성품을 평가하는 형용사라 of + 목적격을 쓴다. of가 들어가므로"
def FOR(adj): return f"{adj}: 행동 자체를 판단하는 형용사라 의미상 주어는 for + 목적격이다. of가 들어갈 수 없으므로"
S52 = "원문항 발문(of가 들어갈 수 없는 것)으로 되돌리고, 원문항처럼 of 문장 넷과 for 문장 하나로 새로 썼다."
mk(2, 52, "B", [("It was generous _____ Mina to donate all the books.", OF("generous")), ("It was clever _____ you to solve the puzzle so fast.", OF("clever")), ("It is necessary _____ everyone to register online.", FOR("necessary")),
                ("It was rude _____ him to leave without a word.", OF("rude")), ("It was polite _____ the boy to hold the door.", OF("polite"))], 3, R52,
   "발문이 ‘for가 아닌 of를 쓰는 문장’으로 원문항과 반대였다. " + S52, st="R")
S52b = "for를 쓰는 오답 네 문장이 B와 똑같았다. " + S52 + " 유형마다 문장을 달리했다."
mk(2, 52, "C", [("It was kind _____ Tom to help the stranger.", OF("kind")), ("It was silly _____ me to believe that rumor.", OF("silly")), ("It was thoughtful _____ Jane to send a card.", OF("thoughtful")),
                ("It was brave _____ the girl to jump into the water.", OF("brave")), ("It is dangerous _____ kids to swim here alone.", FOR("dangerous"))], 5, R52, S52b, st="R")
mk(2, 52, "D", [("It is hard _____ beginners to learn this song.", FOR("hard")), ("It was careless _____ him to leave the door open.", OF("careless")), ("It was sweet _____ you to bake cookies for us.", OF("sweet")),
                ("It was foolish _____ them to ignore the warning.", OF("foolish")), ("It was honest _____ Ben to admit his mistake.", OF("honest"))], 1, R52, S52b, st="R")
mk(2, 52, "E", [("It was stupid _____ me to forget my passport.", OF("stupid")), ("It is easy _____ me to wake up early.", FOR("easy")), ("It was polite _____ Leo to thank the driver.", OF("polite")),
                ("It was selfish _____ him to eat all the cake.", OF("selfish")), ("It was smart _____ Mina to find a shortcut.", OF("smart"))], 2, R52, S52b, st="R")
mk(2, 52, "F", [("It was thoughtless _____ them to interrupt the speaker.", OF("thoughtless")), ("It was mean _____ you to laugh at her.", OF("mean")), ("It was considerate _____ Amy to lower her voice.", OF("considerate")),
                ("It is impossible _____ us to finish this in an hour.", FOR("impossible")), ("It was cruel _____ him to lie to his friend.", OF("cruel"))], 4, R52, S52b, st="R")

# 2-53 to부정사 쓰임이 다른 것: 원문항 발문, 같은 용법 넷 + 다른 용법 하나를 유형마다
R53 = "to부정사는 주어·보어·목적어 자리의 명사적 용법, 명사를 뒤에서 꾸미는 형용사적 용법, 목적(~하기 위해)·감정의 원인(~해서) 등을 나타내는 부사적 용법으로 구별한다."
S53 = "발문이 ‘동작의 목적을 나타내는 부사적 용법’이라고 정답의 용법을 알려 주었고, 오답 네 문장이 유형마다 같았다. 원문항 발문(쓰임이 나머지 넷과 다른 것)으로 되돌리고, 원문항처럼 같은 용법 넷과 다른 용법 하나로 유형마다 새로 썼다."
def ADJ(nn, mean): return f"형용사적 용법: 앞의 명사({nn})를 꾸며 ‘{mean}’라는 뜻이다."
def SAME(x): return x + " 나머지와 쓰임이 같으므로"
def DIFF(x): return x + " 나머지 넷과 쓰임이 다르므로"
mk(2, 53, "B", [("I have a lot of homework <u>to do</u> tonight.", SAME(ADJ("homework", "해야 할 숙제"))), ("She went to the bakery <u>to buy</u> some bread.", DIFF("부사적 용법(목적): ‘빵을 사기 위해’ 빵집에 갔다는 뜻이다.")),
                ("There is nothing <u>to worry</u> about.", SAME(ADJ("nothing", "걱정할 것"))), ("Give me something cold <u>to drink</u>.", SAME(ADJ("something cold", "마실 차가운 것"))),
                ("He was the first person <u>to arrive</u> at the party.", SAME(ADJ("the first person", "처음 도착한 사람")))], 2, R53, S53, st="R")
def NOBJ(v, mean): return f"명사적 용법: 동사 {v}의 목적어로 ‘{mean}’라는 뜻이다."
mk(2, 53, "C", [("I want <u>to travel</u> around the world.", SAME(NOBJ("want", "여행하기를"))), ("She decided <u>to learn</u> Chinese.", SAME(NOBJ("decided", "배우기로"))),
                ("We hope <u>to see</u> you again.", SAME(NOBJ("hope", "보기를"))), ("They planned <u>to visit</u> the museum.", SAME(NOBJ("planned", "방문하기로"))),
                ("Do you have time <u>to talk</u> now?", DIFF(ADJ("time", "이야기할 시간")))], 5, R53, S53 + " 다른 유형과 겹치지 않게 명사적 용법(목적어) 넷과 형용사적 용법 하나로 짰다.", st="R")
def PURP(mean): return f"부사적 용법(목적): ‘{mean}’라는 뜻이다."
mk(2, 53, "D", [("I got up early <u>to catch</u> the first bus.", SAME(PURP("첫차를 타기 위해"))), ("He saved money <u>to buy</u> a new bike.", SAME(PURP("새 자전거를 사기 위해"))),
                ("Her plan is <u>to open</u> a small café.", DIFF("명사적 용법: be동사 뒤 보어로 ‘카페를 여는 것’이라는 뜻이다.")), ("We went to the park <u>to play</u> soccer.", SAME(PURP("축구를 하기 위해"))),
                ("She called me <u>to say</u> thank you.", SAME(PURP("고맙다고 말하기 위해")))], 3, R53, S53 + " 다른 유형과 겹치지 않게 부사적 용법(목적) 넷과 명사적 용법 하나로 짰다.", st="R")
mk(2, 53, "E", [("<u>To learn</u> a new language takes time.", DIFF("명사적 용법: 문장의 주어로 ‘새 언어를 배우는 것’이라는 뜻이다.")), ("I need a friend <u>to help</u> me.", SAME(ADJ("a friend", "나를 도와줄 친구"))),
                ("It is time <u>to go</u> to bed.", SAME(ADJ("time", "잘 시간"))), ("She has no reason <u>to be</u> angry.", SAME(ADJ("reason", "화낼 이유"))),
                ("There are many places <u>to visit</u> in Seoul.", SAME(ADJ("places", "방문할 곳")))], 1, R53, S53 + " 다른 유형과 겹치지 않게 형용사적 용법 넷과 명사적 용법(주어) 하나로 짰다.", st="R")
def FEEL(mean): return f"부사적 용법(감정의 원인): ‘{mean}’라는 뜻이다."
mk(2, 53, "F", [("I'm glad <u>to meet</u> you.", SAME(FEEL("만나서 기쁘다"))), ("She was sad <u>to hear</u> the news.", SAME(FEEL("소식을 듣고 슬펐다"))), ("We were surprised <u>to see</u> him there.", SAME(FEEL("그를 보고 놀랐다"))),
                ("I have a question <u>to ask</u> you.", DIFF(ADJ("a question", "물어볼 질문"))), ("He was happy <u>to win</u> the prize.", SAME(FEEL("상을 받아 행복했다")))], 4, R53,
   S53 + " 다른 유형과 겹치지 않게 부사적 용법(감정의 원인) 넷과 형용사적 용법 하나로 짰다.", st="R")

# 2-55 학생 설명: 이유를 곁들인 설명, 옳게 설명한 학생 수를 유형마다 다르게
R55 = "명사를 꾸미는 to부정사에서 명사가 전치사의 목적어이면 전치사를 남긴다(a chair to sit on). -thing/-one은 형용사가 뒤에서 꾸민다. 성품 평가 형용사 뒤 의미상 주어는 of, 판단 형용사 뒤는 for + 목적격이다. enough는 형용사 뒤에 오고, too ~ to는 so ~ that … can't로 바꿀 수 있다."
S55 = "원문항 학생 설명은 이유를 곁들이는데 변형은 ‘는 맞아’만 반복했고, C~F 모두 ‘네 명 옳음 + 한 명 틀림’ 구조라 정답이 예측되었다. 원문항처럼 이유를 포함한 설명으로 새로 쓰고, 옳게 설명한 학생 수를 유형마다 달리했다."
def f55(t, lines, judge, ok, c, a):
    F(2, 55, t, p="\n".join(lines), c=c, a=a, r=R55, pre=["학생별 판정:"] + judge, k=f"올바르게 설명한 학생은 {ok}이다.", n=setnotes(c, ok, "올바르게 설명한 학생"), s=S55 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f55("C", ["Tom: I need a chair to sit on. 은 의자 위에 앉는 것이라 on이 꼭 필요해요.", "Amy: I want cold something to drink. 는 <형용사 + -thing + to부정사> 어순이라 옳아요.",
          "Jin: It was nice for you to call me. 는 전화해 준 사람의 친절을 평가하므로 옳아요.", "Mina: The water is enough hot to drink. 는 enough가 형용사 앞에 와서 옳아요.",
          "Leo: He is too young to drive. 는 He is so young that he can't drive. 로 바꿀 수 있어요."],
    ["Tom 옳음: sit on a chair의 on을 남긴다.", "Amy 틀림: -thing은 형용사가 뒤에서 꾸미므로 something cold to drink가 맞다.", "Jin 틀림: 사람의 친절을 평가하므로 of you로 써야 한다.",
     "Mina 틀림: enough는 형용사 뒤에 오므로 hot enough to drink가 맞다.", "Leo 옳음: too ~ to는 so ~ that … can't로 바꿀 수 있다."],
    "Tom, Leo", ["Tom, Amy", "Tom, Leo", "Jin, Mina", "Tom, Jin, Leo", "Amy, Mina, Leo"], 2)
f55("D", ["Jane: I need some paper to write on. 은 종이 위에 쓰는 것이라 on이 필요해요.", "Ben: She has no friend to talk. 는 전치사 없이도 옳은 문장이에요.",
          "Sora: It was careless of him to forget. 는 그의 부주의함을 평가해서 of를 썼어요.", "Tom: This book is easy enough for children to read. 에서 for children은 to read의 의미상 주어예요.",
          "Amy: The bag is too heavy for I to carry. 는 의미상 주어를 주격으로 써서 옳아요."],
    ["Jane 옳음: write on paper의 on을 남긴다.", "Ben 틀림: talk to(with) a friend의 전치사를 남겨 to talk to(with)로 써야 한다.", "Sora 옳음: 성품 평가 형용사 careless 뒤에는 of + 목적격을 쓴다.",
     "Tom 옳음: for children이 읽는 주체인 의미상 주어이다.", "Amy 틀림: 의미상 주어는 for + 목적격이므로 for me가 맞다."],
    "Jane, Sora, Tom", ["Jane, Ben", "Sora, Tom, Amy", "Jane, Sora, Tom", "Ben, Tom", "Jane, Ben, Amy"], 3)
f55("E", ["Mina: I need a room to study in. 은 방 안에서 공부하는 것이라 in이 필요해요.", "Leo: He has nothing to worry about. 에서 마지막 about은 빼야 옳은 문장이 돼요.",
          "Jane: It was generous of her to donate. 는 그녀의 너그러움을 평가해서 of를 썼어요.", "Ben: My dream is to become a pilot. 의 to become은 보어 자리에 쓰였어요.",
          "Sora: She woke up to find herself famous. 는 ‘유명해지기 위해 잠에서 깼다’는 목적의 뜻이에요."],
    ["Mina 옳음: study in a room의 in을 남긴다.", "Leo 틀림: worry about의 about을 빼면 틀린 문장이 된다.", "Jane 옳음: 성품 평가 형용사 generous 뒤에는 of + 목적격을 쓴다.",
     "Ben 옳음: be동사 뒤 보어 자리의 명사적 용법이다.", "Sora 틀림: ‘깨어 보니 유명해져 있었다’는 결과의 부사적 용법이다."],
    "Mina, Jane, Ben", ["Mina, Leo", "Leo, Jane, Sora", "Mina, Jane, Ben", "Mina, Ben, Sora", "Leo, Ben, Sora"], 3)
f55("F", ["Tom: I need a spoon to eat. 은 숟가락으로 먹는 것이라 전치사가 필요 없어요.", "Amy: I'm looking for someone kind to help me. 는 <-one + 형용사 + to부정사> 어순이라 옳아요.",
          "Jin: It was foolish for me to ignore the warning. 은 행동 자체를 판단해서 for를 썼어요.", "Mina: The coffee is cool enough to drink. 는 The coffee is so cool that I can drink it. 으로 바꿀 수 있어요.",
          "Leo: The room is enough large for us to use. 는 enough의 위치가 옳아요."],
    ["Tom 틀림: eat with a spoon의 with를 남겨 a spoon to eat with로 써야 한다.", "Amy 옳음: -one은 형용사가 뒤에서 꾸미고 그 뒤에 to부정사가 온다.", "Jin 틀림: foolish는 성품 평가 형용사라 of me로 써야 한다.",
     "Mina 옳음: enough to는 so ~ that … can으로 바꿀 수 있다.", "Leo 틀림: enough는 형용사 뒤에 오므로 large enough가 맞다."],
    "Amy, Mina", ["Tom, Amy", "Amy, Jin, Leo", "Mina, Leo", "Tom, Jin", "Amy, Mina"], 5)

# 2-56 명사 + to부정사 + 전치사: 전치사를 알려 주던 괄호 삭제, 원문항 발문
XR56 = [("지정된 명사 수식 관계에서 ", ""), ("목적을 나타내는 별도 부사절로 읽는 과제는 아니다.", "전치사가 빠져 명사와의 관계가 드러나지 않는다."),
        ("현재분사로 시작한 구이며 발문이 요구하는 명사 수식 to부정사구가 아니다.", "현재분사로 시작한 구라 ‘~할’이라는 뜻으로 명사를 꾸미는 to부정사구가 되지 않는다.")]
for t in "BCDEF":
    F(2, 56, t, st="R", xr=[x for x in XR56 if x[0] in V(2, 56, t)["expl"]], s="발문 괄호가 ‘펜으로 글을 쓰다’, ‘방 안에서 공부하다’처럼 필요한 전치사를 알려 주어, 괄호를 지우고 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 2-57 밑줄 다섯 곳 중 틀린 곳을 바르게 고친 표현: 원문항 형식으로
R57 = "It is + 성품 형용사(kind, nice, generous, thoughtful, smart 등) + of + 목적격 + to부정사, It is + 판단 형용사(easy, hard, important 등) + for + 목적격 + to부정사로 의미상 주어를 나타낸다. 밑줄마다 원래 표현이 옳은지, 고친 표현이 옳은지를 함께 확인한다."
S57 = "원문항은 대화에 밑줄 다섯 곳을 두고 틀린 곳을 바르게 고친 표현을 고르는 형식인데, 변형은 밑줄 한 곳만 주고 고친 표현을 고르게 해 오류 위치를 찾는 과정이 빠졌다. 원문항 발문으로 되돌리고, 대화에 밑줄 다섯 곳을 두어 선택지를 각 밑줄의 고친 표현으로 새로 썼다."
def f57(t, p, items, a, k, s=""):
    mk(2, 57, t, items, a, R57, S57 + s, st="R", p=p, k=k)
f57("B", "A: It was thoughtful ①<u>for Mina</u> to bring extra water.\nB: Yes. The bottles were ②<u>light enough</u> for us ③<u>to carry</u>.\nA: I ④<u>am agree</u>. She always ⑤<u>thinks of</u> others.",
    [("of Mina", "of Mina: thoughtful은 행동한 사람의 성품을 평가하므로 for Mina를 of Mina로 바르게 고쳤으므로"), ("enough light", "enough light: enough는 형용사 뒤에 오므로 원래 표현(light enough)이 옳고 이 고침은 틀렸으므로"),
     ("carrying", "carrying: enough 뒤에는 to부정사를 쓰므로 원래 표현(to carry)이 옳고 이 고침은 틀렸으므로"), ("am agreed", "am agreed: agree는 일반동사이므로 I agree로 고쳐야 하며 이 고침도 틀렸으므로"),
     ("thinks to", "thinks to: ‘남을 생각하다’는 think of이므로 원래 표현이 옳고 이 고침은 틀렸으므로")], 1,
    "①의 for Mina는 성품 형용사(thoughtful) 뒤이므로 of Mina로 고쳐야 한다.")
f57("C", "A: I forgot my wallet, so Jina paid ①<u>to</u> my lunch.\nB: It was very kind ②<u>for her</u> ③<u>doing</u> that.\nA: I know. I need ④<u>to pay</u> her back. Is it easy ⑤<u>of me</u> to find her now?",
    [("on", "on: ‘~의 값을 내다’는 pay for이므로 이 고침은 틀렸으므로"), ("of her", "of her: kind는 행동한 사람의 성품을 평가하므로 for her를 of her로 바르게 고쳤으므로"),
     ("to doing", "to doing: It was kind of her 뒤에는 to부정사(to do)를 쓰므로 이 고침은 틀렸으므로"), ("paying", "paying: need 뒤에 목적어로 ‘갚아야 한다’는 뜻은 to pay로 나타내므로 원래 표현이 옳고 이 고침은 틀렸으므로"),
     ("by me", "by me: easy는 판단 형용사라 의미상 주어는 for me이므로 이 고침은 틀렸으므로")], 2,
    "②의 for her는 성품 형용사(kind) 뒤이므로 of her로 고쳐야 한다.")
f57("D", "A: This suitcase is too heavy ①<u>of me</u> to carry.\nB: Let me ②<u>helping</u> you.\nA: Thanks. It's really sweet ③<u>for you</u> ④<u>to offering</u>.\nB: No problem. It's ⑤<u>easy enough</u> for two people.",
    [("by me", "by me: too ~ to의 의미상 주어는 for me이므로 이 고침은 틀렸으므로"), ("to help", "to help: 사역동사 let 뒤에는 동사원형(help)을 쓰므로 이 고침은 틀렸으므로"),
     ("of you", "of you: sweet는 행동한 사람의 성품을 평가하므로 for you를 of you로 바르게 고쳤으므로"), ("offering", "offering: It's sweet of you 뒤에는 to부정사(to offer)를 쓰므로 이 고침은 틀렸으므로"),
     ("enough easy", "enough easy: enough는 형용사 뒤에 오므로 원래 표현(easy enough)이 옳고 이 고침은 틀렸으므로")], 3,
    "③의 for you는 성품 형용사(sweet) 뒤이므로 of you로 고쳐야 한다.", " 평가 요소(let + 동사원형)를 원문항과 같은 of + 의미상 주어로 맞췄다.")
f57("E", "A: It's hard ①<u>of us</u> to find a room ②<u>large enough</u> for our club.\nB: Tom found one. He ③<u>let</u> us ④<u>using</u> it every Friday.\nA: Really? It was nice ⑤<u>for Tom</u> to do that.",
    [("to us", "to us: hard는 판단 형용사라 의미상 주어는 for us이므로 이 고침은 틀렸으므로"), ("enough large", "enough large: enough는 형용사 뒤에 오므로 원래 표현(large enough)이 옳고 이 고침은 틀렸으므로"),
     ("let's", "let's: ‘그가 우리에게 쓰게 해 주었다’는 뜻이므로 원래 표현(let)이 옳고 이 고침은 틀렸으므로"), ("to use", "to use: 사역동사 let 뒤에는 동사원형(use)을 쓰므로 이 고침도 틀렸으므로"),
     ("of Tom", "of Tom: nice는 행동한 사람의 성품을 평가하므로 for Tom을 of Tom으로 바르게 고쳤으므로")], 5,
    "⑤의 for Tom은 성품 형용사(nice) 뒤이므로 of Tom으로 고쳐야 한다.", " 발문에 덧붙어 답을 알려 주던 문장(B는 Tom의 친절함을 평가하려고 한다)을 지웠다.")
f57("F", "A: I need a pen ①<u>to write</u>.\nB: Here. I always carry ②<u>extra ones</u>. It's important ③<u>to be</u> prepared.\nA: Thanks. It's smart ④<u>for you</u> ⑤<u>to think</u> ahead.",
    [("writing", "writing: 펜으로 쓰는 것이므로 to write with로 고쳐야 하며 이 고침은 틀렸으므로"), ("extra one", "extra one: 여러 개를 가리키므로 원래 표현(extra ones)이 옳고 이 고침은 틀렸으므로"),
     ("being", "being: It's important 뒤 진주어는 to부정사이므로 원래 표현(to be)이 옳고 이 고침은 틀렸으므로"), ("of you", "of you: smart는 행동한 사람의 성품을 평가하므로 for you를 of you로 바르게 고쳤으므로"),
     ("thinking", "thinking: It's smart of you 뒤에는 to부정사를 쓰므로 원래 표현(to think)이 옳고 이 고침은 틀렸으므로")], 4,
    "④의 for you는 성품 형용사(smart) 뒤이므로 of you로 고쳐야 한다.", " 평가 요소(write with)를 원문항과 같은 of + 의미상 주어로 맞췄다.")

# 2-58 be to + 수동: 원문항 발문, 조건 없이도 성립하는 being p.p. 보기를 to being p.p.로
R58 = "be to 구문에서 주어가 동작을 받는 관계이면 to be + 과거분사를 쓴다(~될 수 있다/~되어야 한다). to 뒤에는 동사원형 be를 쓰고, be 뒤에는 과거분사를 쓴다."
S58 = "발문이 ‘주어가 동작을 받는 관계의 be to 구문’이라고 정답 형태를 알려 주어 원문항 발문으로 되돌렸다. 조건이 없으면 진행 수동태 ‘being p.p.’도 문법적으로 성립할 수 있어, 그 보기를 원문항처럼 ‘to being p.p.’로 바꿨다."
def n58(ch, subj):
    x = ch.split(" - ")[0]
    if x.startswith("to have"): return f"완료 부정사(to have + 과거분사)는 능동이라 주어({subj})가 ‘~되는’ 수동 관계를 나타내지 못하므로"
    if x.startswith("to being"): return "to 뒤에는 동사원형 be를 써야 하므로 to being은 틀린 형태이므로"
    if x.startswith("to be "): return "to be 뒤에는 과거분사를 써야 하므로 동사원형은 틀린 형태이므로"
    return f"능동 to부정사라 주어({subj})가 스스로 ~한다는 뜻이 되어 맞지 않으므로"
def f58(t, p, c, a, subj, s=""):
    mk(2, 58, t, [(x, (f"주어({subj})가 ~되는 수동 관계이므로 to be + 과거분사가 두 빈칸에 모두 알맞으므로" if i + 1 == a else n58(x, subj))) for i, x in enumerate(c)], a, R58, S58 + s, st="R", p=p,
       k=f"주어({subj})는 동작을 받는 대상이므로 두 빈칸 모두 be to + 수동(to be + 과거분사)이다.")
BL = "____________________"
f58("B", f"Knowledge is not {BL} overnight. It is {BL} through steady practice.", ["to have gained - to have developed", "to gain - to develop", "to being gained - to being developed", "to be gain - to be develop", "to be gained - to be developed"], 5, "Knowledge")
f58("C", f"Trust is not {BL} by promises alone. It is {BL} over time.", ["to be buy - to be earn", "to being bought - to being earned", "to be bought - to be earned", "to buy - to earn", "to have bought - to have earned"], 3, "Trust",
    " 첫 문장이 원문항(… is not ___ with money)과 거의 같아 ‘by promises alone’으로 바꿨다.")
f58("D", f"A skill is not {BL} in a day. It is {BL} through repetition.", ["to master - to improve", "to be mastered - to be improved", "to have mastered - to have improved", "to being mastered - to being improved", "to be master - to be improve"], 2, "A skill")
f58("E", f"Respect is not {BL} by force. It is {BL} through actions.", ["to be demanded - to be won", "to demand - to win", "to be demand - to be win", "to being demanded - to being won", "to have demanded - to have won"], 1, "Respect",
    " 둘째 빈칸의 동사가 C와 같지 않게 earn을 win으로 바꿨다.")
f58("F", f"Confidence is not {BL} instantly. It is {BL} through experience.", ["to be create - to be build", "to have created - to have built", "to being created - to being built", "to be created - to be built", "to create - to build"], 4, "Confidence",
    " 정답 위치가 E와 같아 보기 순서를 바꿨다.")

# 2-59 enough to 연결: 원문항 발문과 <보기> 형식, enough 위치·의미상 주어 격 오류 오답
R59 = "‘매우 ~해서 …할 수 있다’는 형용사 + enough + for + 목적격 + to부정사로 나타낸다. enough는 형용사 뒤에 오고, 의미상 주어는 for + 목적격이며, 문장의 주어가 to부정사의 목적어이면 그 목적어(it, them)는 다시 쓰지 않는다."
S59 = "발문이 ‘「형용사+enough+for+의미상 주어+to부정사」 구조로’라고 정답 구조를 통째로 알려 주었고, 오답(shallow very for, shallow too for)이 성립하지 않는 배열이라 쉽게 지워졌다. 원문항 발문과 <보기> 형식으로 되돌리고, 원문항처럼 enough의 위치·의미상 주어의 격·to부정사 형태 오류로 오답을 새로 썼다."
E59 = {"case": "의미상 주어는 for + 목적격이어야 하는데 주격(소유격)을 썼으므로", "pos": "enough는 형용사 뒤에 와야 하는데 앞에 두었으므로", "so": "so와 enough를 함께 쓸 수 없고 enough는 형용사 뒤에 와야 하므로",
       "that": "enough 뒤에 that과 to부정사를 섞어 쓸 수 없으므로", "of": "판단의 의미상 주어는 of가 아니라 for + 목적격이므로", "ing": "enough ~ for 뒤에는 to부정사를 써야 하는데 -ing를 썼으므로",
       "too": "too ~ to는 ‘너무 ~해서 …할 수 없다’는 뜻이 되어 두 문장의 뜻과 반대이므로"}
def f59(t, s1, s2, items, a, s=""):
    mk(2, 59, t, [(x, ("형용사 + enough + for + 목적격 + to부정사로 두 문장의 뜻을 바르게 연결했으므로" if i + 1 == a else E59[e])) for i, (x, e) in enumerate(items)], a, R59, S59 + s, st="R",
       p=f"<보기>\n{s1}\n{s2}\n(‘be ~ enough to ~’구문을 활용할 것)")
f59("B", "The river was very shallow.", "We could walk across it.",
    [("The river was shallow enough for we to walk across.", "case"), ("The river was enough shallow for us to walk across.", "pos"), ("The river was too shallow for us to walk across.", "too"),
     ("The river was shallow enough for us to walk across.", ""), ("The river was shallow enough of us to walk across.", "of")], 4)
f59("C", "The room was very quiet.", "Mina could study in it.",
    [("The room was quiet enough for she to study in.", "case"), ("The room was quiet enough for Mina to study in.", ""), ("The room was enough quiet for Mina to study in.", "pos"),
     ("The room was so enough quiet for Mina to study in.", "so"), ("The room was quiet enough that Mina to study in.", "that")], 2, " 둘째 문장을 ‘Mina could study in it.’으로 바꿔 전치사를 남기는 연결이 드러나게 했다.")
f59("D", "The box was very light.", "Tom could carry it alone.",
    [("The box was light enough of Tom to carry alone.", "of"), ("The box was enough light for Tom to carry alone.", "pos"), ("The box was light enough for Tom carrying alone.", "ing"),
     ("The box was too light for Tom to carry alone.", "too"), ("The box was light enough for Tom to carry alone.", "")], 5)
f59("E", "The instructions were very clear.", "We could follow them easily.",
    [("The instructions were clear enough for us to follow easily.", ""), ("The instructions were clear enough that for us to follow easily.", "that"), ("The instructions were enough clear for us to follow easily.", "pos"),
     ("The instructions were clear enough for our to follow easily.", "case"), ("The instructions were so enough clear for us to follow easily.", "so")], 1)
f59("F", "The road was very wide.", "Two cars could pass safely.",
    [("The road was wide so enough for two cars to pass safely.", "so"), ("The road was enough wide for two cars to pass safely.", "pos"), ("The road was wide enough for two cars to pass safely.", ""),
     ("The road was wide enough of two cars to pass safely.", "of"), ("The road was wide enough for two cars passing safely.", "ing")], 3)

# 2-60 be to 용법 설명: 원문항처럼 다섯 문장(가능 포함), 괄호 삭제, 설명을 유형마다 새로
R60 = "be to는 문맥에 따라 예정(~할 예정이다), 의무(~해야 한다), 의도·조건(if절에서 ~하려면), 가능(주로 부정문의 be to be + 과거분사: ~할 수 있다), 운명(was/were (never) to: ~할 운명이었다)을 나타낸다."
S60 = "보기 문장이 5개에서 4개로 줄어 원문항의 ‘가능’ 용법이 빠졌고, 발문 괄호가 (D)의 뜻을 알려 주었다. 원문항 발문으로 되돌리고 ‘가능’ 용법을 넣어 보기 문장을 다섯 개로 했으며, 학생 설명 다섯 개와 틀린 설명을 유형마다 새로 썼다."
def f60(t, lines, items, a):
    talk(2, 60, t, items, a, R60, S60, st="R", p="<보기>\n" + "\n".join(lines))
f60("B", ["(A) The ceremony is to begin at noon.", "(B) You are to submit the form by Friday.", "(C) If you are to succeed, you must practice.", "(D) Nothing was to be seen in the dark.", "(E) The lost hikers were never to return."],
    [("준: (A)는 정오에 시작하기로 예정된 일을 나타내.", "(A)는 예정의 be to이다."), ("태호: (B)는 금요일까지 제출해야 한다는 의무를 나타내.", "(B)는 의무의 be to이다."),
     ("민지: (C)는 ‘성공하려면’이라는 의도·조건을 나타내.", "(C)는 if절의 의도·조건의 be to이다."), ("민아: (D)는 ‘아무것도 보려고 하지 않았다’는 의도의 뜻이야.", "(D)는 부정 주어와 함께 쓰인 가능의 be to로 ‘아무것도 보이지 않았다’는 뜻이다."),
     ("수아: (E)는 결국 돌아오지 못하게 된 운명을 나타내.", "(E)는 운명의 be to이다.")], 4)
f60("C", ["(A) The president is to visit Seoul next week.", "(B) Students are to remain seated.", "(C) If we are to finish on time, we must hurry.", "(D) Not a star was to be seen that night.", "(E) He was never to see his hometown again."],
    [("하린: (A)는 대통령이 서울을 방문해야 한다는 의무만 나타내.", "(A)는 다음 주의 계획을 나타내는 예정의 be to이다."), ("서준: (B)는 학생들이 자리에 앉아 있어야 한다는 의무를 나타내.", "(B)는 의무의 be to이다."),
     ("도윤: (C)는 ‘제시간에 끝내려면’이라는 의도·조건을 나타내.", "(C)는 if절의 의도·조건의 be to이다."), ("예린: (D)는 ‘별 하나 보이지 않았다’는 가능의 뜻이야.", "(D)는 부정문에 쓰인 가능의 be to이다."),
     ("시우: (E)는 다시는 고향을 보지 못할 운명이었다는 뜻이야.", "(E)는 운명의 be to이다.")], 1)
f60("D", ["(A) The train is to leave at nine.", "(B) You are to wear a helmet here.", "(C) If she is to improve, she must practice more.", "(D) No one was to be found in the building.", "(E) They were never to meet again."],
    [("지호: (A)는 기차가 9시에 떠날 예정이라는 뜻이야.", "(A)는 예정의 be to이다."), ("유나: (B)는 여기서 헬멧을 써야 한다는 의무를 나타내.", "(B)는 의무의 be to이다."),
     ("건우: (C)의 is to improve는 ‘향상되어야 한다’는 의무의 뜻이야.", "(C)는 if절에 쓰여 ‘향상되려면’이라는 의도·조건을 나타낸다."), ("소연: (D)는 건물 안에서 아무도 찾을 수 없었다는 가능의 뜻이야.", "(D)는 부정 주어와 함께 쓰인 가능의 be to이다."),
     ("현우: (E)는 다시는 만나지 못할 운명이었다는 뜻이야.", "(E)는 운명의 be to이다.")], 3)
f60("E", ["(A) The concert is to be held tomorrow.", "(B) You are to keep this secret.", "(C) If Tom is to win, he must train harder.", "(D) Her voice was not to be heard in the noise.", "(E) The ship was never to return."],
    [("은서: (A)는 내일 열릴 예정인 공연을 나타내.", "(A)는 예정의 be to이다."), ("민재: (B)는 비밀을 지킬 수 있다는 가능의 뜻이야.", "(B)는 ‘비밀을 지켜야 한다’는 의무의 be to이다."),
     ("채원: (C)는 ‘이기려면’이라는 의도·조건을 나타내.", "(C)는 if절의 의도·조건의 be to이다."), ("지훈: (D)는 소음 때문에 그녀의 목소리가 들리지 않았다는 가능의 뜻이야.", "(D)는 부정문에 쓰인 가능의 be to이다."),
     ("나연: (E)는 그 배가 다시는 돌아오지 못할 운명이었다는 뜻이야.", "(E)는 운명의 be to이다.")], 2)
f60("F", ["(A) The guests are to arrive at six.", "(B) We are to finish before lunch.", "(C) If Jane is to pass, she must study.", "(D) The key was nowhere to be found.", "(E) He was never to recover."],
    [("태윤: (A)는 손님들이 6시에 도착할 예정이라는 뜻이야.", "(A)는 예정의 be to이다."), ("서아: (B)는 점심 전에 끝내야 한다는 의무를 나타내.", "(B)는 의무의 be to이다."),
     ("준서: (C)는 ‘합격하려면’이라는 의도·조건을 나타내.", "(C)는 if절의 의도·조건의 be to이다."), ("하은: (D)는 열쇠를 어디서도 찾을 수 없었다는 가능의 뜻이야.", "(D)는 부정어(nowhere)와 함께 쓰인 가능의 be to이다."),
     ("우진: (E)는 그가 곧 회복할 예정이라는 가까운 미래의 계획이야.", "(E)는 ‘결코 회복하지 못할 운명이었다’는 운명의 be to이다.")], 5)
