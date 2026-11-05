# 3급 CH13 접속사 (121~130) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
BL = "(<u>           </u>)"

# 3-121 if / unless: 원문항 발문, 우리말 해석은 문장 아래에, unless·if 구별 문장
ST121 = "다음 빈칸에 가장 적절한 것을 고르시오."
R121 = "if는 ‘만약 ~하면’, unless는 ‘~하지 않으면(= if ~ not)’이다. unless 뒤에 not을 또 쓰지 않는다. when은 ‘~할 때’, because는 ‘~ 때문에’, although는 ‘비록 ~이지만’이다."
S121 = "원문항은 unless(= if ~ not)와 if의 구별을 묻는데, 변형은 when·although·because 등 다른 접속사를 정답으로 삼았고 우리말 해석이 발문으로 옮겨졌다. 원문항 발문으로 되돌리고 우리말 해석을 문장 아래에 붙였으며, 원문항처럼 unless·if를 구별하는 문장으로 새로 썼다."
IFN = "‘만약 ~하면’이라 ‘~하지 않으면’의 뜻과 맞지 않으므로"
WHEN = "‘~할 때’라 조건의 뜻과 맞지 않으므로"; BEC = "‘~ 때문에’라 조건의 뜻과 맞지 않으므로"; ALT = "‘비록 ~이지만’이라 조건의 뜻과 맞지 않으므로"
UNL = "‘~하지 않으면’이라 우리말 해석과 맞으므로"
def f121(t, p, ko, items, a, s=S121):
    mk(3, 121, t, items, a, R121, s, st=ST121, p=f"{p}\n({ko})", okdup=True)
f121("B", "______ you wear a coat, you will catch a cold.", "코트를 입지 않으면, 감기에 걸릴 거야.", [("If", IFN), ("When", WHEN), ("Because", BEC), ("Unless", UNL), ("Although", ALT)], 4,
     "제시문과 정답이 원문항과 똑같았다. 제시문을 새로 쓰고 원문항처럼 우리말 해석을 문장 아래에 붙였다.")
f121("C", "______ it rains tomorrow, we will stay home.", "만약 내일 비가 오면, 우리는 집에 있을 것이다.", [("Although", ALT), ("Because", BEC), ("Unless", "‘~하지 않으면’이라 ‘만약 비가 오면’의 뜻과 맞지 않으므로"), ("When", "‘~할 때’라 ‘만약 ~하면’의 뜻과 맞지 않으므로"), ("If", "‘만약 ~하면’이라 우리말 해석과 맞으므로")], 5,
     "우리말 해석이 발문으로 옮겨졌다. 원문항 발문으로 되돌리고 우리말 해석을 문장 아래에 붙였다. 보기와 정답은 그대로다.")
f121("D", "______ you study harder, you won't pass the test.", "더 열심히 공부하지 않으면, 시험에 합격하지 못할 거야.", [("Unless", UNL), ("Although", ALT), ("Because", BEC), ("When", WHEN), ("If", IFN)], 1)
f121("E", "______ you don't like it, you can give it back.", "그것이 마음에 들지 않으면, 돌려줘도 돼.", [("When", WHEN), ("Because", BEC), ("If", "뒤에 don't가 있어 If ~ not(~하지 않으면)이 되므로"), ("Unless", "unless에 이미 not의 뜻이 있어 don't와 함께 쓰면 뜻이 반대가 되므로"), ("Although", ALT)], 3)
f121("F", "______ the store is closed, we can buy some milk there.", "가게가 문을 닫지 않았으면, 우리는 거기서 우유를 살 수 있다.", [("Because", BEC), ("Although", ALT), ("If", IFN), ("When", WHEN), ("Unless", UNL)], 5)

# 3-122 that의 쓰임: 유형마다 문장을 새로, 주어·목적어·보어·진주어 자리 that절 포함
R122 = "접속사 that은 뒤에 완전한 절(주어 + 동사)을 이끌어 문장의 주어·목적어·보어나 가주어 It의 진주어가 되고, 지시형용사 that은 뒤의 명사를 꾸며 ‘저 ~’라는 뜻이다."
S122 = "접속사 that 오답 네 문장이 B와 똑같았고, 원문항의 주어 자리 명사절(That she is kind is true)이 빠졌다. 유형마다 문장을 새로 쓰고 주어·목적어·보어·진주어 자리의 that절을 고루 넣었다."
def CJ(role): return f"접속사 that: 완전한 절을 이끌어 {role} 역할을 하므로"
def DM(noun): return f"지시형용사 that: 뒤의 명사({noun})를 꾸미므로"
def f122(t, items, a, s=S122):
    mk(3, 122, t, [(x, w + (" 나머지와 쓰임이 달라" if i + 1 == a else "")) for i, (x, w) in enumerate(items)], a, R122, s)
f122("B", [("I think <u>that</u> the answer is wrong.", CJ("think의 목적어")), ("<u>That</u> he won the race surprised everyone.", CJ("문장의 주어")), ("Look at <u>that</u> tall tree.", DM("tree")),
           ("The problem is <u>that</u> we have no time.", CJ("보어")), ("It is strange <u>that</u> she didn't come.", CJ("가주어 It의 진주어"))], 3,
     "정답(That book is interesting.)이 원문항과 똑같았다. 문장을 새로 쓰고 원문항처럼 주어 자리의 that절도 넣었다.")
f122("C", [("<u>That</u> Tom lied is clear.", CJ("문장의 주어")), ("We hope <u>that</u> you feel better.", CJ("hope의 목적어")), ("It is important <u>that</u> we try again.", CJ("가주어 It의 진주어")),
           ("Mom told me <u>that</u> dinner was ready.", CJ("told의 직접목적어")), ("<u>That</u> movie was exciting.", DM("movie"))], 5)
f122("D", [("She said <u>that</u> the store was closed.", "접속사 that: 완전한 절을 이끌어 said의 목적어 역할을 하므로"), ("Who is <u>that</u> girl?", DM("girl")), ("<u>That</u> car is very fast.", DM("car")),
           ("I don't like <u>that</u> color.", DM("color")), ("<u>That</u> answer is correct.", DM("answer"))], 1, S122 + " 지시형용사 넷 + 접속사 하나로 짜서 다른 유형과 구성을 달리했다.")
f122("E", [("The truth is <u>that</u> I forgot.", CJ("보어")), ("I'm sure <u>that</u> he will come.", CJ("sure 뒤에서 내용을 설명하는")), ("<u>That</u> she speaks three languages is amazing.", CJ("문장의 주어")),
           ("<u>That</u> student won the prize.", DM("student")), ("It is true <u>that</u> the earth is round.", CJ("가주어 It의 진주어"))], 4)
f122("F", [("<u>That</u> building is our library.", DM("building")), ("I know <u>that</u> you are busy.", "접속사 that: 완전한 절을 이끌어 know의 목적어 역할을 하므로"), ("Can you pass me <u>that</u> box?", DM("box")),
           ("<u>That</u> idea sounds good.", DM("idea")), ("I bought <u>that</u> hat yesterday.", DM("hat"))], 2, S122 + " 지시형용사 넷 + 접속사 하나로 짜서 다른 유형과 구성을 달리했다.")

# 3-123 B: 원문항과 같던 우리말을 새로
mk(3, 123, "B", [("He eats either meat and fish.", "either는 or와 짝을 이루고 뜻도 맞지 않으므로"), ("He eats neither meat nor fish.", "neither A nor B(A도 B도 아닌)로 바르게 옮겼으므로"), ("He eats both meat and fish.", "both A and B는 ‘둘 다’라 부정의 뜻과 맞지 않으므로"),
                 ("He eats not only meat but also fish.", "not only A but also B는 ‘A뿐 아니라 B도’라 부정의 뜻과 맞지 않으므로"), ("He eats either meat or fish.", "either A or B는 ‘둘 중 하나’라 뜻이 맞지 않으므로")], 2,
   "neither A nor B는 ‘A도 B도 아닌’, either A or B는 ‘A나 B 중 하나’, both A and B는 ‘A와 B 둘 다’라는 뜻이다.", "우리말과 선택지 네 개가 원문항과 똑같았다. 우리말을 ‘그는 고기도 생선도 먹지 않는다.’로 바꿨다.",
   p="그는 고기도 생선도 먹지 않는다.")

# 3-124 so / because: 원문항 발문, 원문항처럼 so·because 구별 두 문장
ST124 = "다음 빈칸에 들어갈 말이 바르게 짝지어진 것을 고르시오."
R124 = "because는 뒤에 이유를, so는 뒤에 결과를 이끈다. although는 ‘비록 ~이지만’의 양보를 나타낸다."
S124 = "발문이 빈칸마다 ‘결과’, ‘이유’, ‘대조’, ‘선택’이라고 관계를 알려 주었고, 선택지 다섯 개가 모든 유형에서 같았으며 일부 유형은 so·because 대신 but·or·when을 물었다. 원문항 발문으로 되돌리고 원문항처럼 so·because를 구별하는 두 문장으로 새로 썼으며 유형마다 정답 조합을 달리했다."
def n124(ch, good, why):
    xs = [x.strip() for x in ch.split(" - ")]; gs = [x.strip() for x in good.split(" - ")]
    if xs == gs: return f"첫째 빈칸은 {why[0]}, 둘째 빈칸은 {why[1]}이므로"
    bits = [f"{'첫째' if i == 0 else '둘째'} 빈칸 {x}: {w}이다" for i, (x, g, w) in enumerate(zip(xs, gs, why)) if x != g]
    return ", ".join(bits) + ". 따라서"
def f124(t, p, c, a, why, s=S124):
    mk(3, 124, t, [(x, n124(x, c[a-1], why)) for x in c], a, R124, s, st=ST124, p=p, okdup=True)
f124("B", "- Tom missed the bus _____ he got up late.\n- Tom got up late, _____ he missed the bus.", ["so - so", "so - because", "because - so", "because - because", "so - although"], 3,
     ["뒤 절(늦게 일어남)이 버스를 놓친 이유라 because", "뒤 절(버스를 놓침)이 늦게 일어난 결과라 so"],
     "제시문과 정답(so - because)이 원문항과 똑같았고 발문이 관계를 알려 주었다. 문장을 새로 쓰고 원문항 발문으로 되돌렸으며 정답을 because - so로 바꿨다.")
f124("C", "- The movie was boring, _____ I fell asleep.\n- It was very hot, _____ we went swimming.", ["because - so", "so - so", "so - because", "because - because", "although - so"], 2,
     ["뒤 절(잠이 듦)이 지루했던 결과라 so", "뒤 절(수영하러 감)이 더웠던 결과라 so"])
f124("D", "- Jane studied hard _____ she wanted to pass.\n- She was happy _____ she passed the test.", ["so - because", "because - so", "so - so", "because - because", "although - because"], 4,
     ["뒤 절(합격하고 싶었음)이 열심히 공부한 이유라 because", "뒤 절(시험에 합격함)이 기뻤던 이유라 because"], S124 + " 정답 조합(so - because)이 원문항과 같아 because - because로 바꿨다.")
f124("E", "- I called Tom, _____ he knows the news now.\n- Tom smiled _____ he heard the good news.", ["so - because", "because - so", "because - because", "so - so", "so - although"], 1,
     ["뒤 절(Tom이 소식을 앎)이 전화한 결과라 so", "뒤 절(좋은 소식을 들음)이 웃은 이유라 because"])
f124("F", "- We stayed home _____ it rained all day.\n- The road was icy, _____ we drove slowly.", ["so - because", "although - so", "so - so", "because - because", "because - so"], 5,
     ["뒤 절(하루 종일 비가 옴)이 집에 있었던 이유라 because", "뒤 절(천천히 운전함)이 길이 얼어 있던 결과라 so"])

# 3-125 상관접속사 전환: 밑줄 빈칸, B·C·F는 전환을 새로
R125 = "both A and B = not only A but also B(A뿐 아니라 B도) = B as well as A이다. neither A nor B(A도 B도 아닌)는 not ~ A or B로, either A or B는 ‘A나 B 중 하나’로 나타낸다."
S125 = "빈칸 밑줄이 괄호로 바뀌었다. 원문항처럼 밑줄 빈칸으로 되돌렸다. 보기와 정답은 그대로다."
def f125(t, p, items, a, s):
    mk(3, 125, t, items, a, R125, s, p=p.replace("( )", BL), okdup=True)
f125("B", "He is both smart and kind.\n= He is not only smart ( ) kind.", [("as well as", "as well as는 not only와 짝을 이루지 않으므로"), ("but also", "not only A but also B로 both A and B와 같은 뜻이 되므로"), ("and", "not only는 and가 아니라 but also와 짝을 이루므로"),
     ("nor", "nor는 neither와 짝을 이루므로"), ("or", "or는 either와 짝을 이루므로")], 2,
     "전환 구조(not only A but also B → B as well as A)와 정답(as well as)이 원문항과 같았다. both A and B → not only A but also B로 전환을 바꾸고 원문항처럼 밑줄 빈칸으로 제시했다.")
f125("C", "I don't like cats, and I don't like dogs.\n= I like neither cats ( ) dogs.", [("or", "neither는 or가 아니라 nor와 짝을 이루므로"), ("and", "neither는 and와 짝을 이루지 않으므로"), ("nor", "neither A nor B(A도 B도 아닌)로 두 부정문을 바르게 합쳤으므로"),
     ("but also", "but also는 not only와 짝을 이루므로"), ("as well as", "as well as는 ‘~뿐 아니라’라 부정의 뜻과 맞지 않으므로")], 3,
     "both A and B → A and B 전환이 너무 쉬웠고 오답 because·because of가 쉽게 지워졌다. 두 부정문을 neither A nor B로 합치는 전환으로 새로 쓰고 오답을 상관접속사 짝으로 바꿨다.")
F(3, 125, "D", p=V(3, 125, "D")["passage"].replace("( )", BL), s=S125)
F(3, 125, "E", p=V(3, 125, "E")["passage"].replace("( )", BL), s=S125)
f125("F", "Jane will go to the library, or she will go to the park.\n= Jane will go to either the library ( ) the park.", [("nor", "nor는 neither와 짝을 이루므로"), ("and", "either는 and가 아니라 or와 짝을 이루므로"), ("but also", "but also는 not only와 짝을 이루므로"),
     ("or", "either A or B(A나 B 중 하나)로 바르게 바꿨으므로"), ("as well as", "as well as는 ‘둘 다’의 뜻이라 ‘둘 중 하나’와 맞지 않으므로")], 4,
     "both A and B → A and B 전환이 너무 쉬웠고 오답 because·because of가 쉽게 지워졌다. 두 문장을 either A or B로 합치는 전환으로 새로 쓰고 오답을 상관접속사 짝으로 바꿨다.")

# 3-126 and/but/or/because/so: 원문항 발문, 우리말 해석을 문장 아래에
ST126 = "다음 빈칸에 알맞은 접속사를 고르시오."
S126 = "발문이 ‘두 사실의 첨가’, ‘대조’, ‘선택’처럼 관계를 알려 줘 정답이 드러났다. 원문항 발문으로 되돌리고 원문항처럼 우리말 해석을 문장 아래에 붙였다. 보기와 정답은 그대로다."
mk(3, 126, "B", [("but", "but은 대조라 ‘~했고’의 뜻과 맞지 않으므로"), ("and", "and는 두 사실을 이어 ‘~했고’의 뜻이 되므로"), ("because", "because는 이유라 뜻이 맞지 않으므로"), ("or", "or는 선택이라 뜻이 맞지 않으므로"), ("so", "so는 결과라 뜻이 맞지 않으므로")], 2,
   "and는 첨가, but은 대조, or는 선택, because는 이유, so는 결과를 나타낸다.", "제시문과 정답이 원문항과 똑같았고 발문이 관계를 알려 주었다. 제시문을 새로 쓰고 원문항 발문과 우리말 해석으로 되돌렸다.",
   st=ST126, p="Mom cooked dinner _____ Dad washed the dishes.\n(엄마는 저녁을 요리했고 아빠는 설거지를 했다.)", okdup=True)
for t, ko in [("C", "Tom은 피곤하지만 계속 일한다."), ("D", "차와 커피 중 어느 것을 원하니?"), ("E", "Jane은 아팠기 때문에 집에 머물렀다."), ("F", "비가 와서 우리는 소풍을 취소했다.")]:
    F(3, 126, t, st=ST126, p=V(3, 126, t)["passage"] + f"\n({ko})", s=S126)

# 3-127 B: 원문항과 같던 우리말을 새로
mk(3, 127, "B", [("I can either cook or clean.", "either A or B는 ‘둘 중 하나’라 뜻이 맞지 않으므로"), ("I can not only cook but also clean.", "‘~뿐 아니라 ~도 할 수 있다’라 부정의 뜻과 맞지 않으므로"), ("I can neither cook nor clean.", "neither A nor B로 ‘요리도 청소도 못한다’를 바르게 옮겼으므로"),
                 ("I can both cook and clean.", "‘둘 다 할 수 있다’라 부정의 뜻과 맞지 않으므로"), ("I can no cook and clean.", "조동사 뒤에 no를 써서 부정할 수 없으므로")], 3,
   "neither A nor B는 ‘A도 B도 아닌’이라는 뜻이며 A와 B를 같은 형태로 나란히 쓴다.", "우리말과 정답이 원문항과 똑같았다. 우리말을 ‘나는 요리도 청소도 할 수 없다.’로 바꿨다.", p="나는 요리도 청소도 할 수 없다.")

# 3-128 not only A but also B 배열: 원문항 발문과 배열할 단어, 어순 오류 오답
ST128 = "다음 단어들을 바르게 배열하여 문장을 완성한 것을 고르시오."
R128 = "not only A but also B는 ‘A뿐 아니라 B도’라는 뜻이며, not only와 but also를 떼지 않고 A와 B 바로 앞에 각각 둔다."
S128 = "원문항은 주어진 단어를 배열하는 문항인데, 변형은 배열할 단어 없이 우리말만 주고 발문이 ‘not only A but also B 표현으로’라고 정답 구조를 알려 주었으며, 주어가 빠진 오답은 형식만으로 지워졌다. 원문항 발문과 배열할 단어로 되돌리고 오답을 원문항처럼 어순 오류로 바꿨다."
OK128 = "not only A but also B 어순으로 바르게 배열했으므로"
NOTIS = "not이 be동사 앞에 와서 어순이 틀렸으므로"; ONLYNOT = "only not이 아니라 not only로 써야 하므로"; ALSOBUT = "also but이 아니라 but also로 써야 하므로"; NOTONLY_SPLIT = "not과 only를 떼어 쓸 수 없으므로"
def f128(t, ko, words, items, a, s=S128):
    mk(3, 128, t, items, a, R128, s, st=ST128, p=f"{ko}\n({words})")
f128("B", "이 책은 재미있을 뿐만 아니라 유용하다.", "not / useful / interesting / this book / is / but / also / only",
     [("This book not is only interesting but also useful.", NOTIS), ("This book is not only interesting but also useful.", OK128), ("This book is only not interesting but also useful.", ONLYNOT),
      ("This book is not interesting only but also useful.", NOTONLY_SPLIT), ("This book is not only interesting also but useful.", ALSOBUT)], 2,
     "우리말·단어·정답이 원문항과 똑같았고 발문이 정답 구조를 알려 주었다. 우리말과 단어를 새로 쓰고 원문항 발문으로 되돌렸다.")
f128("C", "Tom은 친절할 뿐만 아니라 재미있다.", "not / funny / kind / Tom / is / but / also / only",
     [("Tom is not kind only but also funny.", NOTONLY_SPLIT), ("Tom not is only kind but also funny.", NOTIS), ("Tom is not only kind also but funny.", ALSOBUT), ("Tom is only not kind but also funny.", ONLYNOT), ("Tom is not only kind but also funny.", OK128)], 5)
f128("D", "Jane은 영어뿐만 아니라 프랑스어도 말한다.", "not / French / English / Jane / speaks / but / also / only",
     [("Jane not speaks only English but also French.", "not이 일반동사 앞에 오고 only와 떨어져 어순이 틀렸으므로"), ("Jane speaks only not English but also French.", ONLYNOT), ("Jane speaks not only English but also French.", OK128),
      ("Jane speaks not English only but also French.", NOTONLY_SPLIT), ("Jane speaks not only English also but French.", ALSOBUT)], 3)
f128("E", "우리는 부산뿐만 아니라 서울도 방문했다.", "not / Seoul / Busan / we / visited / but / also / only",
     [("We visited not only Busan but also Seoul.", OK128), ("We visited only not Busan but also Seoul.", ONLYNOT), ("We visited not Busan only but also Seoul.", NOTONLY_SPLIT),
      ("We not visited only Busan but also Seoul.", "not이 일반동사 앞에 오고 only와 떨어져 어순이 틀렸으므로"), ("We visited not only Busan also but Seoul.", ALSOBUT)], 1)
f128("F", "그는 수영뿐만 아니라 달리기도 잘한다.", "not / running / swimming / he / is / good at / but / also / only",
     [("He is good at only not swimming but also running.", ONLYNOT), ("He not is good at only swimming but also running.", NOTIS), ("He is good at not swimming only but also running.", NOTONLY_SPLIT),
      ("He is good at not only swimming but also running.", OK128), ("He is good at not only swimming also but running.", ALSOBUT)], 4)

# 3-129 B: 원문항과 같던 제시문을 새로
mk(3, 129, "B", [("If you water the plant, it will die.", "not의 뜻이 빠져 ‘물을 주면 죽는다’가 되므로"), ("Unless you water the plant, it will die.", "If ~ not을 Unless로 바르게 바꿨으므로"), ("Unless you don't water the plant, it will die.", "unless에 not의 뜻이 있어 don't를 또 쓰면 안 되므로"),
                 ("When you water the plant, it will die.", "when은 ‘~할 때’라 조건 ‘~하지 않으면’의 뜻과 맞지 않으므로"), ("Unless you water the plant, it won't die.", "결과 부분의 뜻(죽을 것이다)을 반대로 바꿨으므로")], 2,
   "unless는 if ~ not(~하지 않으면)의 뜻이므로 unless절에 not을 또 쓰지 않고, 결과 부분의 뜻은 그대로 둔다.", "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘If you don't water the plant, it will die.’로 바꿨다.",
   p="If you don't water the plant, it will die.")

# 3-130 that절 옳은 문장 짝: 원문항 형식(㉠~㉣, 옳은 두 개의 짝), 오류 종류 다양화
ST130 = "다음 중 어법상 옳은 문장으로만 짝지어진 것은?"
R130 = "that절이 문장의 주어로 쓰이면 단수 동사를 쓴다. that절 안은 주어 + 동사의 평서문 어순이며, 가주어 It을 두고 that절을 뒤로 보낼 수 있다."
S130 = "원문항은 네 문장 중 옳은 두 개의 짝을 고르는데, 변형은 ‘모두 빠짐없이’ 고르는 형식(‘해당 없음’ 포함)으로 바뀌었고 기호도 ㄱ~ㅁ으로 바뀌었으며, 원문항의 어순 오류(that is he) 없이 수 일치 오류만 나왔다. 원문항 발문과 형식(㉠~㉣ 네 문장, 옳은 두 개의 짝)으로 되돌리고 어순 오류도 넣었다."
def f130(t, lines, judge, ok, c, s=S130):
    a = c.index(ok) + 1
    F(3, 130, t, st=ST130, p="\n".join(lines), c=c, a=a, r=R130, pre=["문장별 판정: " + j for j in judge], k=f"어법상 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), okdup=True, s=s + ipos(a))
f130("B", ["㉠ It is certain that she will win.", "㉡ That the students are late make the teacher angry.", "㉢ I think that is she right.", "㉣ That he told the truth is clear."],
     ["㉠ O. 가주어 It + 진주어 that절이다.", "㉡ X. that절 주어는 단수 취급하므로 makes를 쓴다.", "㉢ X. that절 안은 주어 + 동사 어순이라 that she is right로 쓴다.", "㉣ O. that절 주어 + 단수 동사 is이다."], "㉠, ㉣",
     ["㉠, ㉡", "㉡, ㉢", "㉡, ㉣", "㉠, ㉣", "㉢, ㉣"], "ㄱ~ㄷ이 원문항 문장과 같았고 형식도 원본과 달랐다. 문장을 새로 쓰고 원문항 발문과 형식(㉠~㉣ 네 문장, 옳은 두 개의 짝)으로 되돌렸다.")
f130("C", ["㉠ It is clear that Tom is busy.", "㉡ That he is late are strange.", "㉢ I believe that she is kind.", "㉣ She knows that is he honest."],
     ["㉠ O. 가주어 It + 진주어 that절이다.", "㉡ X. that절 주어는 단수 취급하므로 is를 쓴다.", "㉢ O. believe의 목적어 that절이다.", "㉣ X. that절 안은 주어 + 동사 어순이라 that he is honest로 쓴다."], "㉠, ㉢",
     ["㉠, ㉡", "㉠, ㉢", "㉡, ㉢", "㉡, ㉣", "㉢, ㉣"])
f130("D", ["㉠ We knows that Tom is busy.", "㉡ I think that she is kind.", "㉢ It is possible that will he come.", "㉣ That he is honest is clear."],
     ["㉠ X. 주어 We에는 know를 쓴다.", "㉡ O. think의 목적어 that절이다.", "㉢ X. that절 안은 주어 + 동사 어순이라 that he will come으로 쓴다.", "㉣ O. that절 주어 + 단수 동사 is이다."], "㉡, ㉣",
     ["㉠, ㉡", "㉠, ㉢", "㉡, ㉢", "㉡, ㉣", "㉢, ㉣"])
f130("E", ["㉠ It is true that she is a doctor.", "㉡ I know that he were tired.", "㉢ That the books are new are good news.", "㉣ That Tom likes music is obvious."],
     ["㉠ O. 가주어 It + 진주어 that절이다.", "㉡ X. that절의 주어 he에는 was를 쓴다.", "㉢ X. that절 주어는 단수 취급하므로 is를 쓴다.", "㉣ O. that절 주어 + 단수 동사 is이다."], "㉠, ㉣",
     ["㉠, ㉣", "㉠, ㉡", "㉡, ㉢", "㉡, ㉣", "㉢, ㉣"])
f130("F", ["㉠ We believe that is Jane right.", "㉡ That he is honest are important.", "㉢ It is clear that they are ready.", "㉣ Tom said that he was busy."],
     ["㉠ X. that절 안은 주어 + 동사 어순이라 that Jane is right로 쓴다.", "㉡ X. that절 주어는 단수 취급하므로 is를 쓴다.", "㉢ O. 가주어 It + 진주어 that절이다.", "㉣ O. said의 목적어 that절이다."], "㉢, ㉣",
     ["㉠, ㉡", "㉠, ㉢", "㉡, ㉢", "㉡, ㉣", "㉢, ㉣"])


# ---- 2차 감수(2026-10) 추가 ----
# 3-125 D: 명사 사이에 올 수 없는 접속사(unless, because, although) 오답 → 상관접속사 짝으로
FIX.pop((3, 125, "D"), None)
f125("D", "She likes neither coffee nor tea.\n= She doesn't like coffee ( ) tea.", [("nor", "not이 이미 있으므로 nor를 또 쓰면 부정이 겹치므로"), ("but", "not A but B는 ‘A가 아니라 B’라 차는 좋아한다는 뜻이 되므로"), ("but also", "but also는 not only와 짝을 이루므로"),
     ("or", "neither A nor B는 not ~ A or B로 바꿔 쓰므로"), ("either", "either는 두 명사를 잇는 접속사로 쓸 수 없으므로")], 4,
     "빈칸 밑줄이 괄호로 바뀌었고, 오답 unless·because·although는 두 명사 사이에 올 수 없어 형태만으로 지워졌다. 원문항처럼 밑줄 빈칸으로 되돌리고 오답을 상관접속사에 쓰이는 말로 바꿨다.")

# 3-126 B: 정답(and)과 위치(②)가 원문항과 같음 → 보기 순서를 바꿔 ④
FIX.pop((3, 126, "B"), None)
mk(3, 126, "B", [("so", "so는 결과라 뜻이 맞지 않으므로"), ("but", "but은 대조라 ‘~했고’의 뜻과 맞지 않으므로"), ("because", "because는 이유라 뜻이 맞지 않으므로"), ("and", "and는 두 사실을 이어 ‘~했고’의 뜻이 되므로"), ("or", "or는 선택이라 뜻이 맞지 않으므로")], 4,
   "and는 첨가, but은 대조, or는 선택, because는 이유, so는 결과를 나타낸다.", "제시문과 정답이 원문항과 똑같았고 발문이 관계를 알려 주었다. 제시문을 새로 쓰고 원문항 발문과 우리말 해석으로 되돌렸으며, 정답 위치도 원문항(②)과 겹치지 않게 했다.",
   st=ST126, p="Mom cooked dinner _____ Dad washed the dishes.\n(엄마는 저녁을 요리했고 아빠는 설거지를 했다.)", okdup=True)

# 3-127 C: 3-123 C와 우리말·정답 문장이 같음 → 새 문장, 원문항처럼 짝이 틀린 오답
mk(3, 127, "C", [("She can play neither the piano and the guitar.", "neither는 and가 아니라 nor와 짝을 이루므로"), ("She can play neither the piano nor the guitar.", "neither A nor B로 ‘피아노도 기타도 못 친다’를 바르게 옮겼으므로"),
                 ("She can play either the piano or the guitar.", "either A or B는 ‘둘 중 하나는 칠 수 있다’라 뜻이 맞지 않으므로"), ("She can play either the piano nor the guitar.", "either는 nor가 아니라 or와 짝을 이루므로"),
                 ("She can play neither the piano so the guitar.", "neither는 so와 짝을 이루지 않으므로")], 2,
   "neither A nor B는 ‘A도 B도 아닌’이라는 뜻이며 neither는 nor와, either는 or와 짝을 이룬다.", "우리말과 정답 문장(She can neither sing nor dance.)이 같은 단원 3-123의 C와 똑같았다. 우리말을 ‘그녀는 피아노도 기타도 칠 수 없다.’로 바꾸고, 오답을 원문항처럼 짝이 틀린 문장으로 썼다.",
   p="그녀는 피아노도 기타도 칠 수 없다.")

# 3-129 B~F: Unless로 시작하지 않는 오답(If/When/Because)은 발문만 보고 지워짐 → 원문항처럼 모두 Unless로 시작
R129 = "unless는 if ~ not(~하지 않으면)의 뜻이므로 unless절에 not을 또 쓰지 않고, 주절의 뜻은 그대로 둔다."
S129 = "발문이 ‘Unless를 사용하여’ 고치라고 했는데 오답 셋이 If·When·Because로 시작해 발문만 보고 지워졌다. 원문항처럼 다섯 보기를 모두 Unless로 시작하게 하고, not을 겹쳐 쓴 문장·주절의 뜻을 뒤집은 문장을 오답으로 썼다."
def f129(t, p, sub, v_ok, v_base, v_ing, main, main_neg, order, s=S129):
    FIX.pop((3, 129, t), None)
    dn = "doesn't" if v_ok != v_base else "don't"
    its = {"ok": (f"Unless {sub} {v_ok}, {main}.", "If ~ not을 Unless로 바꾸고 주절은 그대로 두었으므로"),
           "dbl": (f"Unless {sub} {dn} {v_base}, {main}.", f"unless에 not의 뜻이 있어 not({dn})을 또 쓰면 안 되므로"),
           "notneg": (f"Unless {sub} not {v_base}, {main_neg}.", "unless절에 not을 남겼고 주절의 뜻도 뒤집었으므로"),
           "neg": (f"Unless {sub} {v_ok}, {main_neg}.", "주절의 뜻을 반대로 뒤집었으므로"),
           "ing": (f"Unless {sub} {v_ing}, {main}.", "unless절에 동사가 없이 -ing형만 썼으므로")}
    mk(3, 129, t, [its[k] for k in order], order.index("ok") + 1, R129, s, p=p)
f129("B", "If you don't water the plant, it will die.", "you", "water the plant", "water the plant", "watering the plant", "it will die", "it won't die", ["dbl", "neg", "ok", "ing", "notneg"],
     "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘If you don't water the plant, it will die.’로 바꾸고, 원문항처럼 다섯 보기를 모두 Unless로 시작하게 했다.")
f129("C", "If you don't hurry up, you'll be late for school.", "you", "hurry up", "hurry up", "hurrying up", "you'll be late for school", "you won't be late for school", ["neg", "ing", "notneg", "dbl", "ok"])
f129("D", "If Tom doesn't call me, I won't know the answer.", "Tom", "calls me", "call me", "calling me", "I won't know the answer", "I will know the answer", ["ing", "dbl", "neg", "ok", "notneg"])
f129("E", "If it doesn't stop raining, we can't go on a picnic.", "it", "stops raining", "stop raining", "stopping raining", "we can't go on a picnic", "we can go on a picnic", ["ok", "notneg", "dbl", "neg", "ing"])
f129("F", "If Jane doesn't study hard, she won't pass the test.", "Jane", "studies hard", "study hard", "studying hard", "she won't pass the test", "she will pass the test", ["notneg", "dbl", "ok", "ing", "neg"])
