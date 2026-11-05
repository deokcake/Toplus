# 4급 CH10 명령문·제안문·감탄문 (91~100) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def slotnote(ch, good, why, labs=("첫째", "둘째", "셋째"), sep=" - "):
    xs = [x.strip() for x in ch.split(sep)]; gs = [x.strip() for x in good.split(sep)]
    if xs == gs: return "모든 빈칸에 알맞은 말을 골랐으므로"
    bits = [f"{labs[i]} 빈칸 {x}: {w}" for i, (x, g, w) in enumerate(zip(xs, gs, why)) if x != g]
    return ", ".join(bits) + ". 따라서"

# 4-91 명령문 + and = If ~: 원문항 발문, 오답에 Or 포함
R491 = "명령문은 동사원형으로 시작한다. 명령문 + and(~해라, 그러면)는 If + 주어 + 동사(~하면)로 바꿀 수 있고, or는 ‘그렇지 않으면’이라 뜻이 반대이다."
S491 = "발문이 ‘명령문 + and를 만약 그 행동을 하면이라는 조건절로’라고 두 빈칸의 정답을 알려 주었고, 원문항 오답의 Or가 Because로 바뀌어 쉽게 지워졌다. 원문항 발문으로 되돌리고 원문항처럼 Or를 오답에 넣었다."
W491 = ["명령문은 동사원형으로 시작한다", "‘~하면’의 조건은 If로 나타낸다(Or는 ‘그렇지 않으면’)"]
def f491(t, p, c, a, s=S491):
    mk(4, 91, t, [(x, slotnote(x, c[a-1], W491)) for x in c], a, R491, s, st="R", p=p, okdup=True)
f491("B", "_____ early, and you will catch the bus.\n_____ you leave early, you will catch the bus.", ["Leaving - If", "Leave - If", "Leave - Or", "Left - If", "Leaving - Or"], 2)
f491("C", "_____ this book, and you will learn a lot.\n_____ you read this book, you will learn a lot.", ["Read - If", "Read - Or", "Reading - If", "To read - If", "Reading - Or"], 1,
     "제시문과 정답(Take - If)이 원문항과 똑같았고 발문이 정답을 알려 주었다. 제시문을 새로 쓰고 " + S491[S491.index("원문항 발문으로"):])
f491("D", "_____ hard, and you will pass the test.\n_____ you study hard, you will pass the test.", ["Study - Or", "To study - If", "Studying - If", "Study - If", "Studied - Or"], 4)
f491("E", "_____ now, and you will be on time.\n_____ you go now, you will be on time.", ["Going - If", "Go - Or", "Went - If", "Going - Or", "Go - If"], 5)
f491("F", "_____ careful, and you will be safe.\n_____ you are careful, you will be safe.", ["Be - Or", "Be - If", "Being - If", "Are - If", "Being - Or"], 2)

# 4-92 What / How 감탄문 다른 하나: 유형마다 새로
R492 = "명사가 있는 감탄문은 What + (a/an) + 형용사 + 명사 + (주어 + 동사)!, 명사 없이 형용사·부사를 강조하면 How + 형용사/부사 + 주어 + 동사!로 쓴다."
S492 = "What 감탄문 오답 네 문장이 B와 똑같았다. 유형마다 문장을 새로 썼다."
def WH(np): return f"뒤에 명사구({np})가 이어져 What이 들어가므로"
def HW(ad): return f"뒤에 형용사·부사({ad})만 이어져 How가 들어가므로"
def f492(t, items, a, s=S492):
    mk(4, 92, t, [(x, w + (" 나머지와 달라" if i + 1 == a else "")) for i, (x, w) in enumerate(items)], a, R492, s)
f492("C", [("_____ quiet the room is!", HW("quiet")), ("_____ a tall tree it is!", WH("a tall tree")), ("_____ an exciting game!", WH("an exciting game")), ("_____ a lovely song it is!", WH("a lovely song")), ("_____ big eyes she has!", WH("big eyes"))], 1,
     "정답(_____ beautiful you are!)이 원문항과 같았고 오답도 B와 같았다. 문장을 모두 새로 쓰고, 정답 문장의 틀과 위치도 원문항(_____ 형용사 you are!, ③)과 겹치지 않게 했다.")
f492("D", [("_____ fast the car is!", HW("fast")), ("_____ kind your mother is!", HW("kind")), ("_____ a long bridge it is!", WH("a long bridge")), ("_____ well she sings!", HW("well")), ("_____ tall you are!", HW("tall"))], 3,
     S492 + " How 넷 + What 하나로 짜서 구성을 달리했다.")
f492("E", [("_____ a funny joke!", WH("a funny joke")), ("_____ delicious this cake is!", HW("delicious")), ("_____ an honest boy he is!", WH("an honest boy")), ("_____ good friends they are!", WH("good friends")), ("_____ a strange dream I had!", WH("a strange dream"))], 2)
f492("F", [("_____ cold it is today!", HW("cold")), ("_____ hard he works!", HW("hard")), ("_____ slowly the turtle walks!", HW("slowly")), ("_____ happy they look!", HW("happy")), ("_____ nice shoes you have!", WH("nice shoes"))], 5,
     S492 + " How 넷 + What 하나로 짜서 구성을 달리했다.")

# 4-93 밑줄 친 동사 형태: 원문항 발문과 밑줄, 여러 제안·명령문을 섞어 유형마다 새로
ST493 = "다음 중 밑줄 친 부분이 틀린 문장을 고르시오."
R493 = "Let's, Shall we, Why don't we, 명령문(Please, Don't, Never)에는 동사원형을 쓰고, How about·What about 뒤에는 동명사(-ing)를 쓴다."
S493 = "원문항은 여러 문장 종류(Shall we, What about, Never, Don't be, Let's)에서 동사 형태를 판별하는데, 변형은 모두 How/What about 문장이라 평가 범위가 좁았고 짝 문장과 같은 오답이 반복되었으며 밑줄도 사라졌다. 원문항 발문과 밑줄로 되돌리고 여러 제안·명령문을 섞어 유형마다 새로 썼다."
OK93 = "문장 종류에 맞는 동사 형태를 바르게 썼으므로"
def f493(t, items, a, s=S493):
    mk(4, 93, t, [(x, w or OK93) for x, w in items], a, R493, s, st=ST493)
f493("B", [("Let's <u>take</u> a picture.", ""), ("Don't <u>be</u> late.", ""), ("How about <u>play</u> soccer?", "How about 뒤에는 동명사 playing을 쓰므로"), ("Shall we <u>sing</u> together?", ""), ("Please <u>close</u> the window.", "")], 3)
f493("C", [("Why don't we <u>eat</u> out?", ""), ("Never <u>tell</u> a lie.", ""), ("What about <u>visiting</u> the museum?", ""), ("Be <u>quiet</u>, please.", ""), ("Let's <u>going</u> to the park.", "Let's 뒤에는 동사원형 go를 쓰므로")], 5,
     S493 + " 정답(What about wear a necklace?)이 원문항과 같아 새로 썼다.")
f493("D", [("Shall we <u>to meet</u> at six?", "Shall we 뒤에는 to 없이 동사원형 meet을 쓰므로"), ("Don't <u>touch</u> the painting.", ""), ("How about <u>ordering</u> pizza?", ""), ("Let's <u>clean</u> the room.", ""), ("Please <u>be</u> kind to others.", "")], 1)
f493("E", [("Let's <u>ride</u> our bikes.", ""), ("Why don't we <u>go</u> camping?", ""), ("What about <u>taking</u> a taxi?", ""), ("Don't <u>running</u> in the hall.", "Don't 뒤에는 동사원형 run을 쓰므로"), ("Never <u>give</u> up.", "")], 4)
f493("F", [("Shall we <u>dance</u>?", ""), ("Please <u>sits</u> down.", "명령문은 동사원형 sit으로 시작하므로"), ("How about <u>making</u> cookies?", ""), ("Don't <u>forget</u> your umbrella.", ""), ("Let's <u>meet</u> tomorrow.", "")], 2)

# 4-94 잘못된 문장: 원문항처럼 여러 문장 종류를 섞어 유형마다 새로
R494 = "명령문은 동사원형으로, Let's 뒤에는 동사원형을 쓴다. 감탄문은 What + (a/an) + 형용사 + 명사 + 주어 + 동사!, How + 형용사/부사 + 주어 + 동사!이다."
S494 = "원문항은 여러 문장 종류(Let's, 감탄문, Don't, Please) 중 틀린 것을 찾는데, 변형은 모두 감탄문이라 평가 범위가 좁았고 짝 문장과 같은 오답이 반복되었다. 원문항처럼 여러 문장 종류를 섞어 유형마다 새로 썼다."
OK94 = "문장 종류에 맞게 바르게 썼으므로"
def f494(t, items, a, s=S494):
    mk(4, 94, t, [(x, w or OK94) for x, w in items], a, R494, s)
f494("B", [("Let's play outside.", ""), ("Please be quiet.", ""), ("How an interesting book it is!", "명사구가 있으면 How가 아니라 What을 써야 하므로"), ("Don't worry about it.", ""), ("What a cute puppy it is!", "")], 3)
f494("C", [("What a big house it is!", ""), ("Let's not waste water.", ""), ("Please sit down.", ""), ("Don't be afraid.", ""), ("Don't makes noise.", "Don't 뒤에는 동사원형 make를 써야 하므로")], 5,
     S494 + " 정답(How a beautiful day it is!)이 원문항과 같아 새로 썼다.")
f494("D", [("Never give up your dream.", ""), ("What beautiful the flower is!", "명사 없이 형용사만 오면 How를 써야 하므로"), ("Let's go to the library.", ""), ("How tall the tree is!", ""), ("Please call me later.", "")], 2)
f494("E", [("Be careful!", ""), ("What a great idea it is!", ""), ("Don't open the door.", ""), ("Let's to eat lunch.", "Let's 뒤에는 to 없이 동사원형을 써야 하므로"), ("How fast the train goes!", "")], 4)
f494("F", [("How a nice weather it is!", "weather는 셀 수 없는 명사라 a를 쓰지 않고, 명사가 있으면 What을 써야 하므로"), ("Let's take a break.", ""), ("Please wait here.", ""), ("Don't be sad.", ""), ("What an honest boy he is!", "")], 1)

# 4-95 감탄문 전환 중 어색한 것: 원문항 발문, 오류 유형을 다양하게
R495 = "명사가 있으면 What + (a/an) + 형용사 + 명사 + 주어 + 동사!, 명사 없이 형용사·부사를 강조하면 How + 형용사/부사 + 주어 + 동사!로 바꾼다. 모음 소리 앞에는 an을 쓰고 복수명사 앞에는 a/an을 쓰지 않는다."
S495 = "발문이 ‘주어 + 동사의 평서문 어순을 유지하는 기본 감탄문’이라고 정답 기준을 알려 주었고, 같은 문장을 두 가지로 바꾼 선택지가 함께 있거나 오류 유형(어순)이 원문항과 같았다. 원문항 발문으로 되돌리고 유형마다 오류 종류를 달리해 새로 썼다."
OK95 = "감탄문으로 바르게 바꿨으므로"
def f495(t, items, a, s=S495):
    mk(4, 95, t, [(x, w or OK95) for x, w in items], a, R495, s, st="R")
f495("B", [("The children laughed very loudly. → How loudly the children laughed!", ""), ("He is a very careful driver. → What a careful driver he is!", ""), ("It is a very cold night. → What a cold night it is!", ""),
           ("Mina is very patient. → How patient Mina is!", ""), ("The stars are very bright. → What bright the stars are!", "명사 없이 형용사만 오면 What이 아니라 How를 써야 하므로")], 5)
f495("C", [("It is a very old tree. → How an old tree it is!", "명사구(an old tree)가 있으면 How가 아니라 What을 써야 하므로"), ("You are very tall. → How tall you are!", ""), ("They are very nice people. → What nice people they are!", ""),
           ("He speaks very slowly. → How slowly he speaks!", ""), ("It was a very long day. → What a long day it was!", "")], 1)
f495("D", [("This soup is very hot. → How hot this soup is!", ""), ("She has very pretty eyes. → What pretty eyes she has!", ""), ("It is a very funny movie. → What funny movie it is!", "단수명사 movie 앞에 a가 빠졌으므로"),
           ("The boy is very brave. → How brave the boy is!", ""), ("You drive very carefully. → How carefully you drive!", "")], 3)
f495("E", [("He is a very honest man. → What an honest man he is!", ""), ("The water is very clear. → How clear the water is!", ""), ("The girls sing very well. → How well the girls sing!", ""),
           ("It is a very big elephant. → How big elephant it is!", "How 뒤에 형용사 + 명사를 쓸 수 없고 What a big elephant로 바꿔야 하므로"), ("These are very sweet apples. → What sweet apples these are!", "")], 4)
f495("F", [("The test was very easy. → How easy the test was!", ""), ("It is a very exciting game. → What a exciting game it is!", "모음 소리로 시작하는 exciting 앞에는 an을 써야 하므로"), ("My dad cooks very well. → How well my dad cooks!", ""),
           ("Those are very tall buildings. → What tall buildings those are!", ""), ("She is very smart. → How smart she is!", "")], 2)

# 4-97 감탄문 첫 단어: 오답을 원문항처럼 강조어(So, Very, Such)로
R497 = "명사구(a + 형용사 + 명사)를 강조하면 What, 형용사·부사를 강조하면 How로 감탄문을 시작한다. So, Very, Such로는 이 어순의 감탄문을 시작하지 않는다."
S497 = "원문항 오답은 강조어(So, Very, Such)라 그럴듯한데, 변형 오답(Which, Why, When)은 감탄문에 쓰이지 않는 의문사라 What/How 둘 중 하나만 고르면 되었다. 오답을 원문항처럼 강조어로 바꿨다."
EMP = "강조어라 감탄문을 이 어순으로 시작하지 못하므로"
def f497(t, p, items, a, s=S497):
    mk(4, 97, t, [(x, w or EMP) for x, w in items], a, R497, s, st="R", p=p, okdup=True)
f497("B", "She is very kind.\n= ________ kind she is!", [("What", "뒤에 명사 없이 형용사만 있어 What을 쓸 수 없으므로"), ("How", "형용사 kind를 강조하는 How 감탄문이므로"), ("So", ""), ("Very", ""), ("Such", "")], 2)
f497("C", "It is a very tall building.\n= ________ a tall building it is!", [("How", "뒤에 명사구(a tall building)가 있어 How를 쓸 수 없으므로"), ("So", ""), ("What", "명사구 a tall building을 강조하는 What 감탄문이므로"), ("Very", ""), ("Such", "")], 3,
     "제시문과 정답이 원문항과 똑같았고 오답도 쉽게 지워졌다. 제시문을 새로 쓰고 오답을 원문항처럼 강조어로 바꿨다.")
f497("D", "It is a very interesting book.\n= ________ an interesting book it is!", [("Such", ""), ("Very", ""), ("How", "뒤에 명사구(an interesting book)가 있어 How를 쓸 수 없으므로"), ("So", ""), ("What", "명사구 an interesting book을 강조하는 What 감탄문이므로")], 5)
f497("E", "He runs very fast.\n= ________ fast he runs!", [("So", ""), ("What", "뒤에 명사 없이 부사만 있어 What을 쓸 수 없으므로"), ("Very", ""), ("How", "부사 fast를 강조하는 How 감탄문이므로"), ("Such", "")], 4)
f497("F", "It is a very cute dog.\n= ________ a cute dog it is!", [("How", "뒤에 명사구(a cute dog)가 있어 How를 쓸 수 없으므로"), ("What", "명사구 a cute dog을 강조하는 What 감탄문이므로"), ("So", ""), ("Such", ""), ("Very", "")], 2)

# 4-98 명령문 + and / or 두 빈칸: 원문항 발문과 우리말 해석, If절 오답 포함
R498 = "명령문 + and는 ‘~해라, 그러면’, 명령문 + or는 ‘~해라, 그렇지 않으면’의 뜻이며 명령문은 동사원형으로 시작한다. If절은 and·or 없이 주절과 바로 이어진다."
S498 = "발문이 ‘동사원형으로 시작하는 명령문’이라고 정답을 알려 주었고 원문항의 우리말 해석이 빠졌으며, 원문항 오답의 If절이 없어졌다. 원문항 발문과 우리말 해석으로 되돌리고 If절을 오답에 넣었다."
W498 = ["and 앞은 동사원형으로 시작하는 명령문이어야 한다", "or 앞은 동사원형으로 시작하는 명령문이어야 한다"]
def f498(t, a1, k1, a2, k2, c, a, s=S498):
    p = f"(A)________, and {a1} ({k1})\n(B)________, or {a2} ({k2})"
    L = lambda z: z
    mk(4, 98, t, [(x, slotnote(x, c[a-1], W498, labs=("(A)", "(B)"))) for x in c], a, R498, s, st="R", p=p, okdup=True)
f498("B", "you will pass the test.", "열심히 공부해라, 그러면 시험에 합격할 것이다.", "you will be late.", "일찍 일어나라, 그렇지 않으면 늦을 것이다.",
     ["Studying hard - Getting up early", "Study hard - Get up early", "If you study hard - Get up early", "Study hard - If you don't get up early", "To study hard - To get up early"], 2)
f498("C", "you will find the bank.", "왼쪽으로 돌아라, 그러면 은행이 보일 것이다.", "you will catch a cold.", "코트를 입어라, 그렇지 않으면 감기에 걸릴 것이다.",
     ["Turning left - Wearing a coat", "If you turn left - Wear a coat", "Turn left - Wear a coat", "Turn left - If you don't wear a coat", "To turn left - To wear a coat"], 3,
     "제시문과 정답(Go straight - Hurry up)이 원문항과 똑같았고 발문이 정답을 알려 주었다. 문장을 새로 쓰고 " + S498[S498.index("원문항 발문과"):])
f498("D", "you will feel better.", "좀 쉬어라, 그러면 기분이 나아질 것이다.", "you will be late.", "지금 떠나라, 그렇지 않으면 늦을 것이다.",
     ["To take a rest - To leave now", "Take a rest - If you don't leave now", "Taking a rest - Leaving now", "Take a rest - Leave now", "If you take a rest - Leave now"], 4)
f498("E", "the room will be clean.", "방을 청소해라, 그러면 방이 깨끗해질 것이다.", "the plants will die.", "식물에 물을 줘라, 그렇지 않으면 식물이 죽을 것이다.",
     ["Clean the room - If you don't water the plants", "Cleaning the room - Watering the plants", "If you clean the room - Water the plants", "To clean the room - To water the plants", "Clean the room - Water the plants"], 5)
f498("F", "you will catch the train.", "빨리 달려라, 그러면 기차를 탈 것이다.", "you will get lost.", "지도를 봐라, 그렇지 않으면 길을 잃을 것이다.",
     ["Run fast - Look at the map", "If you run fast - Look at the map", "Running fast - Looking at the map", "Run fast - If you don't look at the map", "To run fast - To look at the map"], 1)

# 4-99 두 제안문이 모두 올바른 것: 원문항 발문과 밑줄, 한쪽만 틀린 짝 오답
ST499 = "다음 중 밑줄 친 부분이 모두 올바른 것을 고르시오."
R499 = "Let's, Shall we, Why don't we 뒤에는 동사원형을, How about·What about 뒤에는 동명사(-ing)를 쓴다."
S499 = "원문항 오답은 한쪽만 틀린 짝이라 두 문장을 모두 확인해야 하는데, 변형 오답은 두 문장이 모두 틀려 쉽게 지워졌고 유형마다 반복되었으며 밑줄도 사라졌다. 원문항 발문과 밑줄로 되돌리고 한쪽만 틀린 짝으로 오답을 유형마다 새로 썼다."
OK99 = "두 제안문 모두 뒤의 동사 형태가 바르므로"
def f499(t, items, a, s=S499):
    mk(4, 99, t, items, a, R499, s, st=ST499)
f499("B", [("Let's <u>watch</u> TV. - How about <u>watch</u> TV?", "How about 뒤에는 watching을 써야 하므로"), ("Shall we <u>play</u> tennis? - Why don't we <u>playing</u> tennis?", "Why don't we 뒤에는 동사원형 play를 써야 하므로"),
           ("How about <u>taking</u> a walk? - Let's <u>take</u> a walk.", OK99), ("Let's <u>eating</u> out. - What about <u>eating</u> out?", "Let's 뒤에는 동사원형 eat을 써야 하므로"), ("Why don't we <u>rest</u>? - Shall we <u>resting</u>?", "Shall we 뒤에는 동사원형 rest를 써야 하므로")], 3)
f499("C", [("Why don't we <u>swim</u>? - Shall we <u>swimming</u>?", "Shall we 뒤에는 동사원형 swim을 써야 하므로"), ("Let's <u>draw</u> pictures. - How about <u>draw</u> pictures?", "How about 뒤에는 drawing을 써야 하므로"),
           ("Shall we <u>cook</u>? - Let's <u>cooking</u>.", "Let's 뒤에는 동사원형 cook을 써야 하므로"), ("What about <u>visiting</u> Grandma? - Why don't we <u>visit</u> Grandma?", OK99), ("How about <u>running</u>? - Let's <u>running</u>.", "Let's 뒤에는 동사원형 run을 써야 하므로")], 4,
     "정답 짝(Let's eat. - What about eating?)이 원문항과 같았고 오답도 다른 유형과 같았다. " + S499[S499.index("원문항 발문과"):])
f499("D", [("Shall we <u>walked</u> home? - Let's <u>walk</u> home.", "Shall we 뒤에는 동사원형 walk를 써야 하므로"), ("How about <u>order</u> pizza? - Let's <u>order</u> pizza.", "How about 뒤에는 ordering을 써야 하므로"),
           ("Why don't we <u>studying</u>? - What about <u>studying</u>?", "Why don't we 뒤에는 동사원형 study를 써야 하므로"), ("Let's <u>went</u> out. - Shall we <u>go</u> out?", "Let's 뒤에는 동사원형 go를 써야 하므로"), ("Shall we <u>play</u> a game? - How about <u>playing</u> a game?", OK99)], 5)
f499("E", [("What about <u>going</u> to the beach? - Shall we <u>go</u> to the beach?", OK99), ("Let's <u>to dance</u>. - How about <u>dancing</u>?", "Let's 뒤에는 to 없이 동사원형을 써야 하므로"),
           ("Why don't we <u>take</u> a bus? - What about <u>take</u> a bus?", "What about 뒤에는 taking을 써야 하므로"), ("Shall we <u>meeting</u> at 5? - Let's <u>meet</u> at 5.", "Shall we 뒤에는 동사원형 meet을 써야 하므로"), ("How about <u>reading</u>? - Why don't we <u>reads</u>?", "Why don't we 뒤에는 동사원형 read를 써야 하므로")], 1)
f499("F", [("Let's <u>jump</u> rope. - What about <u>jump</u> rope?", "What about 뒤에는 jumping을 써야 하므로"), ("Why don't we <u>make</u> a snowman? - How about <u>making</u> a snowman?", OK99),
           ("Shall we <u>ate</u> lunch? - Let's <u>eat</u> lunch.", "Shall we 뒤에는 동사원형 eat을 써야 하므로"), ("How about <u>listen</u> to music? - Let's <u>listen</u> to music.", "How about 뒤에는 listening을 써야 하므로"), ("Let's <u>studying</u>. - Shall we <u>study</u>?", "Let's 뒤에는 동사원형 study를 써야 하므로")], 2)

# 4-100 틀린 문장으로만 짝: 원문항 발문과 형식(<보기> 줄바꿈, 세 개 조합), 오류 종류 다양화
ST4100 = "다음 <보기> 중 어법상 틀린 문장으로만 짝지어진 것은?"
R4100 = "감탄문은 What + (a/an) + 형용사 + 명사 + 주어 + 동사!, How + 형용사/부사 + 주어 + 동사!이다. 복수명사 앞에는 a/an을 쓰지 않고, 주어와 동사의 수를 일치시킨다."
S4100 = "발문이 ‘주어 + 동사의 평서문 어순을 유지하는 기본 감탄문’이라고 기준을 알려 주었고, 원문항은 틀린 문장 세 개의 조합을 고르는데 변형은 ‘빠짐없이 모두’ 고르는 형식(1~3개)으로 바뀌었으며 줄바꿈과 원문항의 수 일치 오류가 빠졌다. 원문항 발문과 형식(<보기> 줄바꿈, 세 개 조합)으로 되돌리고 수 일치 오류도 넣었다."
def f4100(t, lines, judge, ok, c, s=S4100):
    a = c.index(ok) + 1
    F(4, 100, t, st=ST4100, p="<보기>\n" + "\n".join(lines), c=c, a=a, r=R4100, pre=["문장별 판정: " + j for j in judge], k=f"어법상 틀린 문장은 {ok}이다.", n=setnotes(c, ok, "틀린 문장"), okdup=True, s=s + ipos(a))
f4100("B", ["(A) What an amazing story it is!", "(B) How interesting the book is!", "(C) What cute the cat is!", "(D) How a nice car it is!", "(E) How well they sings!"],
      ["(A) O. What + an + 형용사 + 명사 + 주어 + 동사이다.", "(B) O. How + 형용사 + 주어 + 동사이다.", "(C) X. 명사 없이 형용사만 오면 How를 쓴다.", "(D) X. 명사구가 있으면 What을 쓴다.", "(E) X. 복수 주어 they에는 sing을 쓴다."], "(C), (D), (E)",
      ["(A), (B), (C)", "(C), (D), (E)", "(A), (B), (E)", "(B), (C), (E)", "(A), (D), (E)"])
f4100("C", ["(A) What a tall trees they are!", "(B) How cute the dog is!", "(C) How fast he run!", "(D) What an interesting book it is!", "(E) What exciting the game was!"],
      ["(A) X. 복수명사 trees 앞에는 a를 쓰지 않는다.", "(B) O. How + 형용사 + 주어 + 동사이다.", "(C) X. 3인칭 단수 주어 he에는 runs를 쓴다.", "(D) O. What + an + 형용사 + 명사 + 주어 + 동사이다.", "(E) X. 명사 없이 형용사만 오면 How를 쓴다."], "(A), (C), (E)",
      ["(A), (C), (E)", "(B), (D)", "(A), (B), (C)", "(B), (C), (E)", "(A), (D), (E)"], S4100 + " (A)(B)가 원문항 문장과 같고 정답 조합도 같아 문장을 새로 썼다.")
f4100("D", ["(A) How kind she are!", "(B) What a nice day it is!", "(C) How a tall boy he is!", "(D) What beautiful the flower is!", "(E) How quickly he runs!"],
      ["(A) X. 주어 she에는 is를 쓴다.", "(B) O. What + a + 형용사 + 명사 + 주어 + 동사이다.", "(C) X. 명사구가 있으면 What을 쓴다.", "(D) X. 명사 없이 형용사만 오면 How를 쓴다.", "(E) O. How + 부사 + 주어 + 동사이다."], "(A), (C), (D)",
      ["(A), (B), (C)", "(C), (D)", "(A), (C), (D)", "(B), (C), (E)", "(A), (D), (E)"])
f4100("E", ["(A) What an old house it is!", "(B) How cute they is!", "(C) What interesting book it is!", "(D) How a beautiful day it is!", "(E) What a smart boy he is!"],
      ["(A) O. What + an + 형용사 + 명사 + 주어 + 동사이다.", "(B) X. 주어 they에는 are를 쓴다.", "(C) X. 단수명사 book 앞에 an이 빠졌다.", "(D) X. 명사구가 있으면 What을 쓴다.", "(E) O. What + a + 형용사 + 명사 + 주어 + 동사이다."], "(B), (C), (D)",
      ["(A), (B), (C)", "(C), (D), (E)", "(A), (B), (E)", "(B), (C), (D)", "(A), (D), (E)"])
f4100("F", ["(A) How fast Tom run!", "(B) What a lovely dog it is!", "(C) How a kind girl she is!", "(D) What beautiful flowers they are!", "(E) How nice the weather are!"],
      ["(A) X. 3인칭 단수 주어 Tom에는 runs를 쓴다.", "(B) O. What + a + 형용사 + 명사 + 주어 + 동사이다.", "(C) X. 명사구가 있으면 What을 쓴다.", "(D) O. What + 형용사 + 복수명사 + 주어 + 동사이다.", "(E) X. 셀 수 없는 명사 weather에는 is를 쓴다."], "(A), (C), (E)",
      ["(A), (B), (C)", "(C), (D)", "(A), (B), (E)", "(B), (C), (E)", "(A), (C), (E)"])


# ---- 2차 감수(2026-10) 추가 ----
# 4-96 D, E: 없는 형태(bes, gos) 오답 → 실제 형태로
R496 = "Let's 뒤에는 동사원형을 쓴다. be동사의 원형은 be다."
S496 = "오답에 영어에 없는 형태(%s)가 있어 철자만 보고 지워졌다. 원문항처럼 실제로 있는 형태(%s)로 바꿨다. 정답은 그대로다."
mk(4, 96, "D", [("being", "Let's 뒤에 -ing형을 쓸 수 없으므로"), ("is", "Let's 뒤에는 is가 아니라 원형 be를 쓰므로"), ("be", "Let's + 동사원형 be이므로"), ("are", "Let's 뒤에는 are가 아니라 원형 be를 쓰므로"), ("to be", "Let's 뒤에 to부정사를 쓸 수 없으므로")], 3,
   R496, S496 % ("bes", "is"), st="R")
mk(4, 96, "E", [("is go", "be동사와 일반동사를 함께 쓸 수 없으므로"), ("go", "Let's + 동사원형 go이므로"), ("to go", "Let's 뒤에 to부정사를 쓸 수 없으므로"), ("going", "Let's 뒤에 -ing형을 쓸 수 없으므로"), ("goes", "Let's 뒤에 -es가 붙은 형태를 쓸 수 없으므로")], 2,
   R496, S496 % ("gos", "goes"), st="R")
