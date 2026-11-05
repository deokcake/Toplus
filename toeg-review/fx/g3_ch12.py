# 3급 CH12 전치사 (111~120) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]
BA, BB = "(<u>    A    </u>)", "(<u>    B    </u>)"

# 3-111 공통 전치사: 원문항처럼 장소 한 문장 + 시간 한 문장, 발문의 뜻 설명 삭제
ST111 = "다음 빈칸에 공통으로 들어갈 전치사를 고르시오."
R111 = "장소는 at(한 지점), on(표면에 닿은 곳), in(공간 안·도시·나라)으로, 시간은 at(시각), on(요일·날짜), in(월·연도·계절)으로 나타낸다."
S111 = "발문에 빈칸의 뜻(‘가방 안’, ‘월요일’ 등)을 풀어 주어 필요한 전치사가 드러났고, 원문항은 장소와 시간에 같은 전치사를 쓰는데 변형은 두 빈칸이 모두 시간 표현이었다. 원문항 발문으로 되돌리고 한 문장은 장소, 한 문장은 시간으로 새로 썼다."
def f111(t, p, c, ok, why, s=S111):
    a = c.index(ok) + 1
    mk(3, 111, t, [(x, why if x == ok else f"{x}: 두 빈칸 중 적어도 한 곳에 맞지 않으므로") for x in c], a, R111, s, st=ST111, p=p, okdup=True)
f111("B", "- There is a picture _____ the wall.\n- We have no school _____ Sunday.", ["in", "on", "at", "during", "under"], "on", "벽 표면(on the wall)과 요일(on Sunday)에 모두 on을 쓰므로",
     "발문이 두 빈칸의 뜻을 풀어 주었고 정답(in)도 원문항과 같았다. 원문항 발문으로 되돌리고 장소·시간 문장을 새로 써서 정답을 on으로 바꿨다.")
f111("C", "- Let's meet _____ the bus stop.\n- The movie starts _____ seven o'clock.", ["on", "in", "at", "for", "by"], "at", "한 지점(at the bus stop)과 시각(at seven o'clock)에 모두 at을 쓰므로")
f111("D", "- Your phone is _____ the table.\n- My birthday is _____ June 10th.", ["on", "at", "in", "during", "for"], "on", "표면(on the table)과 날짜(on June 10th)에 모두 on을 쓰므로")
f111("E", "- He is waiting for you _____ the door.\n- I usually go to bed _____ midnight.", ["in", "on", "for", "during", "at"], "at", "한 지점(at the door)과 시각(at midnight)에 모두 at을 쓰므로")
f111("F", "- My sister lives _____ Canada.\n- It often snows _____ December.", ["at", "on", "for", "in", "by"], "in", "나라(in Canada)와 월(in December)에 모두 in을 쓰므로")

# 3-112 장소 전치사 두 빈칸: 원문항 발문과 밑줄 빈칸, 정답 조합을 원문항과 다르게
ST112 = "다음 대화의 빈칸에 들어갈 전치사가 바르게 짝지어진 것은?"
R112 = "장소 전치사는 at the end of, at the corner of, in front of, on the top shelf, at home, in the room처럼 명사와 어울리는 짝으로 쓴다."
S112 = "발문이 위치의 뜻(‘책상 윗면 위’, ‘은행 앞’ 등)을 풀어 주었고 빈칸 밑줄이 사라졌다. 원문항 발문과 밑줄 빈칸으로 되돌렸다."
def n112(ch, good, why):
    xs = re.findall(r"\([AB]\) (\w+)", ch); gs = re.findall(r"\([AB]\) (\w+)", good)
    if xs == gs: return f"{why[0]}, {why[1]}이므로"
    bits = [f"({L}) {x}: {w}이다" for L, x, g, w in zip("AB", xs, gs, why) if x != g]
    return ", ".join(bits) + ". 따라서"
def f112(t, p, c, a, why, s=S112):
    mk(3, 112, t, [(x, n112(x, c[a-1], why)) for x in c], a, R112, s, st=ST112, p=p.replace("(A)", BA).replace("(B)", BB), okdup=True)
f112("B", "A: Where is the museum?\nB: It is (A) the end (B) this street.", ["(A) in / (B) on", "(A) at / (B) of", "(A) on / (B) in", "(A) at / (B) in", "(A) in / (B) of"], 2,
     ["‘~의 끝에’는 at the end of로 나타내 (A)에는 at", "(B)에는 ‘~의’를 뜻하는 of"],
     "대화와 정답(on - of)이 원문항과 똑같았고 발문이 뜻을 풀어 주었다. 대화를 새로 쓰고 원문항 발문과 밑줄 빈칸으로 되돌렸다.")
f112("C", "A: Where is the cafe?\nB: It is (A) the corner (B) Main Street and King Street.", ["(A) at / (B) of", "(A) in / (B) from", "(A) at / (B) from", "(A) under / (B) of", "(A) in / (B) on"], 1,
     ["‘모퉁이에’는 at the corner로 나타내 (A)에는 at", "(B)에는 ‘~의’를 뜻하는 of"])
f112("D", "A: Where is the sugar?\nB: It is (A) the top shelf (B) the kitchen.", ["(A) in / (B) on", "(A) on / (B) in", "(A) at / (B) of", "(A) at / (B) on", "(A) in / (B) at"], 2,
     ["선반 표면 위에 놓여 있으므로 (A)에는 on", "부엌이라는 공간 안이므로 (B)에는 in"], S112 + " 정답 조합(on - of)이 원문항과 같아 문장을 새로 써서 on - in으로 바꿨다.")
f112("E", "A: Where is the station?\nB: It is (A) front (B) the bank.", ["(A) in / (B) on", "(A) at / (B) in", "(A) on / (B) in", "(A) at / (B) of", "(A) in / (B) of"], 5,
     ["‘~ 앞에’는 in front of로 나타내 (A)에는 in", "(B)에는 of"])
f112("F", "A: Where is Minsu?\nB: He is (A) home. He's reading (B) his room.", ["(A) in / (B) at", "(A) on / (B) in", "(A) at / (B) on", "(A) at / (B) in", "(A) in / (B) on"], 4,
     ["‘집에’는 at home으로 나타내 (A)에는 at", "방이라는 공간 안이므로 (B)에는 in"], S112 + " 정답 조합(in - of)이 E와 같아 문장을 새로 써서 at - in으로 바꿨다.")

# 3-113 by / until: 원문항 발문, 원문항처럼 by·until 구별 두 문장
ST113 = "다음 빈칸에 들어갈 가장 적절한 전치사를 고르시오."
R113 = "by는 ‘~까지’ 한 번 끝내야 하는 완료 기한(submit, return, finish, be back)을, until은 ‘~까지’ 계속되는 상태·동작의 끝(stay, wait, be open, last)을 나타낸다."
S113 = "원문항은 by(완료 기한)와 until(계속)의 구별을 묻는데, 변형은 for/during, at/on, in/on 등 다른 전치사를 묻고 발문이 ‘세 시간 동안’, ‘월요일에’처럼 뜻을 풀어 주었다. 원문항 발문으로 되돌리고 원문항처럼 by·until을 구별하는 두 문장으로 새로 썼다."
def n113(ch, good, why):
    xs = [x.strip() for x in ch.split(" - ")]; gs = [x.strip() for x in good.split(" - ")]
    if xs == gs: return f"첫째 문장은 {why[0]}, 둘째 문장은 {why[1]}이므로"
    bits = [f"{'첫째' if i == 0 else '둘째'} 빈칸 {x}: {w}이다" for i, (x, g, w) in enumerate(zip(xs, gs, why)) if x != g]
    return ", ".join(bits) + ". 따라서"
def f113(t, p, c, a, why, s=S113):
    mk(3, 113, t, [(x, n113(x, c[a-1], why)) for x in c], a, R113, s, st=ST113, p=p, okdup=True)
f113("B", "- You can stay here _____ ten o'clock.\n- Please send me the file _____ Wednesday.", ["by - until", "until - by", "for - by", "until - at", "on - to"], 2,
     ["머무는 상태가 10시까지 계속되므로 until", "파일을 수요일까지 보내 끝내야 하는 기한이므로 by"],
     "정답(by - until)과 문장 구조가 원문항과 같았고 발문이 뜻을 풀어 주었다. 문장을 새로 쓰고 원문항 발문으로 되돌렸으며 정답 순서를 until - by로 바꿨다.")
f113("C", "- You have to come home _____ nine.\n- The store is open _____ ten p.m.", ["until - by", "for - until", "by - until", "at - by", "in - to"], 3,
     ["9시까지 집에 와야 하는 기한이므로 by", "가게 문이 밤 10시까지 계속 열려 있으므로 until"])
f113("D", "- It kept raining _____ evening.\n- I'll be back _____ five o'clock.", ["by - until", "until - on", "for - by", "until - by", "in - at"], 4,
     ["비가 저녁까지 계속 내렸으므로 until", "5시까지 돌아오는 기한이므로 by"])
f113("E", "- We need to leave _____ 7 a.m. to catch the train.\n- Let's play soccer _____ sunset.", ["until - by", "at - for", "during - until", "by - until", "by - on"], 4,
     ["기차를 타려면 오전 7시까지 떠나야 하는 기한이므로 by", "해 질 녘까지 축구를 계속하므로 until"])
f113("F", "- The museum is closed _____ next Monday.\n- Please pay the fee _____ the end of this month.", ["for - by", "by - until", "until - in", "on - by", "until - by"], 5,
     ["박물관이 다음 주 월요일까지 계속 닫혀 있으므로 until", "이달 말까지 요금을 내야 하는 기한이므로 by"])

# 3-114 before/after, on/under/in, during: 원문항처럼 문장마다 우리말 해석
ST114 = "다음 빈칸에 들어갈 단어를 바르게 짝지은 것을 고르시오."
R114 = "before는 ‘~ 전에’, after는 ‘~ 후에’, on은 표면 위, under는 아래, in은 안을 나타낸다. during은 ‘~ 동안’으로 뒤에 명사가 오고, while은 뒤에 주어 + 동사가 온다."
S114 = "원문항은 문장마다 우리말 해석을 붙였는데 변형은 발문에 뜻을 몰아 적었고, 오답 조합 네 개가 유형마다 같았다. 원문항 발문과 문장별 우리말 해석으로 되돌리고 유형마다 오답 조합을 새로 썼다."
def n114(ch, good, kos):
    xs = [x.strip() for x in ch.split(" - ")]; gs = [x.strip() for x in good.split(" - ")]
    if xs == gs: return "세 빈칸 모두 우리말 해석에 맞는 전치사를 골랐으므로"
    bits = []
    for i, (x, g, ko) in enumerate(zip(xs, gs, kos)):
        if x == g: continue
        L = ["첫째", "둘째", "셋째"][i]
        bits.append(f"{L} 빈칸 {x}: " + ("while은 뒤에 주어 + 동사가 와야 해 명사 앞에 쓸 수 없다" if x == "while" else f"‘{ko}’의 뜻에 맞지 않는다(→ {g})"))
    return ", ".join(bits) + ". 따라서"
def f114(t, p, c, a, kos, s=S114):
    mk(3, 114, t, [(x, n114(x, c[a-1], kos)) for x in c], a, R114, s, st=ST114, p=p, okdup=True)
f114("B", "I brush my teeth _____ breakfast.(나는 아침 식사 후에 이를 닦는다.)\nThe lamp is _____ the table.(그 램프는 탁자 위에 있다.)\nI visited my aunt _____ the holidays.(나는 휴일 동안 이모를 방문했다.)",
     ["before - on - during", "after - on - during", "after - under - while", "before - in - for", "after - on - while"], 2, ["아침 식사 후에", "탁자 위에", "휴일 동안"],
     "문장과 정답(before - on - during)이 원문항과 같았다. 문장을 새로 쓰고 원문항처럼 문장마다 우리말 해석을 붙였으며 정답을 after - on - during으로 바꿨다.")
f114("C", "Wash your hands _____ dinner.(저녁 식사 전에 손을 씻어라.)\nThe dog is sleeping _____ the bed.(개가 침대 밑에서 자고 있다.)\nNobody talked _____ the movie.(영화 상영 중에 아무도 말하지 않았다.)",
     ["before - under - during", "after - under - while", "before - on - for", "after - in - during", "before - under - while"], 1, ["저녁 식사 전에", "침대 밑에서", "영화 상영 중에"],
     S114 + " 정답 조합(before - on - during)이 원문항과 같아 둘째 문장을 under로 바꿨다.")
f114("D", "Jane called me _____ lunch.(Jane은 점심 식사 후에 나에게 전화했다.)\nThe keys are _____ the drawer.(열쇠는 서랍 안에 있다.)\nI fell asleep _____ the class.(나는 수업 중에 잠이 들었다.)",
     ["before - in - while", "after - on - during", "after - in - during", "before - under - during", "after - in - while"], 3, ["점심 식사 후에", "서랍 안에", "수업 중에"])
f114("E", "We met _____ class.(우리는 수업 후에 만났다.)\nThe cat is _____ the table.(고양이가 탁자 아래에 있다.)\nIt snowed a lot _____ the winter.(겨울 동안 눈이 많이 왔다.)",
     ["after - on - while", "before - under - during", "after - in - for", "after - under - during", "before - on - during"], 4, ["수업 후에", "탁자 아래에", "겨울 동안"])
f114("F", "I studied _____ dinner.(나는 저녁 식사 전에 공부했다.)\nThe book is _____ the box.(그 책은 상자 안에 있다.)\nWe stayed inside _____ the storm.(우리는 폭풍우 동안 안에 머물렀다.)",
     ["after - in - during", "before - on - while", "before - under - for", "after - on - during", "before - in - during"], 5, ["저녁 식사 전에", "상자 안에", "폭풍우 동안"])

# 3-115 옳은 문장으로만 짝: 원문항 형식(ⓐ~ⓓ 네 문장, 옳은 두 개의 짝)
ST115 = "다음 중 어법상 옳은 문장으로만 짝지어진 것은?"
R115 = "시간은 at + 시각, on + 요일·날짜, in + 월·연도·계절로, 장소는 at + 한 지점, on + 표면, in + 공간·도시·나라로 나타낸다. between은 둘 사이, among은 셋 이상 사이이다."
S115 = "원문항은 네 문장 중 옳은 두 개의 짝을 고르는데, 변형은 다섯 문장에서 ‘모두 빠짐없이’ 고르는 형식(‘해당 없음’ 포함)으로 바뀌었고 기호도 a~e로 바뀌었으며 발문에 괄호 조건이 붙었다. 원문항 발문과 형식(ⓐ~ⓓ 네 문장, 옳은 두 개의 짝)으로 되돌렸다."
CH115 = ["ⓐ, ⓑ", "ⓐ, ⓓ", "ⓑ, ⓒ", "ⓑ, ⓓ", "ⓒ, ⓓ"]
def f115(t, lines, judge, ok, c=None, s=S115):
    c = c or (CH115 if ok in CH115 else ["ⓐ, ⓑ", "ⓐ, ⓒ", "ⓑ, ⓒ", "ⓑ, ⓓ", "ⓒ, ⓓ"])
    a = c.index(ok) + 1
    F(3, 115, t, st=ST115, p="\n".join(lines), c=c, a=a, r=R115, pre=["문장별 판정: " + j for j in judge], k=f"어법상 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), s=s + ipos(a))
f115("B", ["ⓐ The concert starts at 7 p.m.", "ⓑ We go skiing in winter.", "ⓒ My cousin lives on Busan.", "ⓓ I'll see you in Friday."],
     ["ⓐ O. 시각에는 at을 쓴다.", "ⓑ O. 계절에는 in을 쓴다.", "ⓒ X. 도시에는 in을 쓴다(in Busan).", "ⓓ X. 요일에는 on을 쓴다(on Friday)."], "ⓐ, ⓑ",
     s="ⓐ~ⓒ가 원문항 문장과 같았고 형식도 원본과 달랐다. 문장을 새로 쓰고 원문항 발문과 형식(ⓐ~ⓓ 네 문장, 옳은 두 개의 짝)으로 되돌렸다.")
f115("C", ["ⓐ We meet on Monday.", "ⓑ Tom lives at Seoul.", "ⓒ The book is on the desk.", "ⓓ I arrived in 8 o'clock."],
     ["ⓐ O. 요일에는 on을 쓴다.", "ⓑ X. 도시에는 in을 쓴다(in Seoul).", "ⓒ O. 표면 위에는 on을 쓴다.", "ⓓ X. 시각에는 at을 쓴다(at 8 o'clock)."], "ⓐ, ⓒ")
f115("D", ["ⓐ We meet at Friday.", "ⓑ Jane was born in 2012.", "ⓒ Tom waits at the gate.", "ⓓ The cat is sleeping in the table."],
     ["ⓐ X. 요일에는 on을 쓴다(on Friday).", "ⓑ O. 연도에는 in을 쓴다.", "ⓒ O. 한 지점에는 at을 쓴다.", "ⓓ X. 탁자 위는 on the table로 쓴다."], "ⓑ, ⓒ")
f115("E", ["ⓐ School starts on nine.", "ⓑ We travel in summer.", "ⓒ I was born at 2011.", "ⓓ We meet on May 5th."],
     ["ⓐ X. 시각에는 at을 쓴다(at nine).", "ⓑ O. 계절에는 in을 쓴다.", "ⓒ X. 연도에는 in을 쓴다(in 2011).", "ⓓ O. 날짜에는 on을 쓴다."], "ⓑ, ⓓ",
     s=S115 + " 괄호 속 뜻 설명에 기대야 틀린 문장이 되던 것(The picture is in the wall)은 뜻 설명 없이도 틀린 문장으로 바꿨다.")
f115("F", ["ⓐ I was born on 2015.", "ⓑ The bag is among the two chairs.", "ⓒ Jane is at home.", "ⓓ We meet at noon."],
     ["ⓐ X. 연도에는 in을 쓴다(in 2015).", "ⓑ X. 둘 사이는 between을 쓴다.", "ⓒ O. ‘집에’는 at home이다.", "ⓓ O. 정오(noon)에는 at을 쓴다."], "ⓒ, ⓓ")

# 3-116 at/on/in: 원문항 발문, 원문항처럼 우리말 해석만 제시
ST116 = "다음 빈칸에 알맞은 전치사를 고르시오."
S116 = "발문이 ‘정확한 시각에’, ‘요일에’, ‘연도에’처럼 at/on/in을 고르는 기준을 그대로 알려 주었다. 원문항 발문으로 되돌리고 원문항처럼 우리말 해석만 붙였다. 보기와 정답은 그대로다."
mk(3, 116, "B", [("on", "on은 요일·날짜에 쓰므로"), ("during", "during은 ‘~ 동안’이라 시각에 쓰지 않으므로"), ("for", "for는 기간의 길이에 쓰므로"), ("in", "in은 월·연도·계절에 쓰므로"), ("at", "정오(noon) 같은 시각에는 at을 쓰므로")], 5,
   "정확한 시각에는 at, 요일·날짜에는 on, 월·연도·계절에는 in을 쓴다.", "제시문과 정답이 원문항과 똑같았고 발문이 기준을 알려 주었다. 제시문을 새로 쓰고 원문항 발문과 우리말 해석으로 되돌렸다.",
   st=ST116, p="Let's meet _____ noon.\n(정오에 만나자.)", okdup=True)
for t, ko in [("C", "우리는 월요일에 만난다."), ("D", "Tom은 2010년에 태어났다."), ("E", "Jane은 8월에 여행한다."), ("F", "파티는 5월 5일에 열린다.")]:
    ex = V(3, 116, t)["expl"]
    F(3, 116, t, st=ST116, p=V(3, 116, t)["passage"] + f"\n({ko})", s=S116)

# 3-117 until → by 등 기한/계속 혼동: 원문항 발문과 밑줄
ST117 = "다음 문장에서 밑줄 친 부분을 바르게 고친 것을 고르시오."
R117 = "by는 ‘~까지’ 한 번 끝내야 하는 완료 기한을, until은 ‘~까지’ 계속되는 상태·동작의 끝을 나타낸다."
S117 = "원문항은 until과 by(완료 기한·계속)의 혼동을 고치는데, 변형은 by → for, on → in 등 다른 전치사를 묻고 발문이 문장 뜻과 고칠 전치사를 알려 주었으며 밑줄이 사라졌다. 원문항 발문과 밑줄로 되돌리고 원문항처럼 by·until 혼동 문장으로 새로 쓰고 우리말 뜻을 붙였다."
BY = "‘~까지’ 한 번 끝내야 하는 기한은 by로 나타내므로"; UNTIL = "‘~까지’ 계속되는 동작의 끝은 until로 나타내므로"
def f117(t, p, items, a, s=S117):
    mk(3, 117, t, items, a, R117, s, st=ST117, p=p, okdup=True)
f117("B", "You must return the book <u>until</u> Friday.\n(너는 금요일까지 그 책을 반납해야 한다.)", [("in", "요일 앞에 in을 쓰지 않고 뜻도 맞지 않으므로"), ("by", "책 반납은 금요일까지 끝내야 하는 기한이라 " + BY[BY.index("by"):]), ("for", "for는 기간의 길이를 나타내므로"),
                                                     ("since", "since는 ‘~ 이래로’라 뜻이 맞지 않으므로"), ("at", "요일 앞에 at을 쓰지 않으므로")], 2,
     "제시문과 정답이 원문항과 똑같았고 발문이 뜻을 풀어 주었다. 제시문을 새로 쓰고 원문항 발문과 밑줄로 되돌렸다.")
f117("C", "I waited for him <u>by</u> midnight.\n(나는 자정까지 그를 기다렸다.)", [("until", "기다리는 동작이 자정까지 계속되었으므로 until로 고쳐야 하므로"), ("in", "시각 앞에 in을 쓰지 않으므로"), ("on", "시각 앞에 on을 쓰지 않으므로"),
                                              ("during", "during 뒤에는 기간을 나타내는 명사가 오므로"), ("since", "since는 과거 시제 waited와 어울리지 않으므로")], 1)
f117("D", "The report has to be done <u>until</u> tomorrow morning.\n(그 보고서는 내일 아침까지 끝내야 한다.)", [("on", "tomorrow 앞에 on을 쓰지 않으므로"), ("at", "tomorrow morning 앞에 at을 쓰지 않으므로"), ("during", "during은 ‘~ 동안’이라 기한을 나타내지 못하므로"),
                                                                  ("by", "보고서는 내일 아침까지 끝내야 하는 기한이라 by로 고쳐야 하므로"), ("since", "since는 ‘~ 이래로’라 뜻이 맞지 않으므로")], 4)
f117("E", "We stayed at the party <u>by</u> ten o'clock.\n(우리는 10시까지 파티에 머물렀다.)", [("since", "since는 과거 시제 stayed와 어울리지 않으므로"), ("for", "for 뒤에는 시각이 아니라 기간의 길이가 오므로"), ("until", "파티에 머무는 동작이 10시까지 계속되었으므로 until로 고쳐야 하므로"),
                                                        ("in", "시각 앞에 in을 쓰지 않으므로"), ("on", "시각 앞에 on을 쓰지 않으므로")], 3)
f117("F", "You should come home <u>until</u> 9 p.m.\n(너는 오후 9시까지 집에 와야 한다.)", [("for", "for 뒤에는 시각이 아니라 기간의 길이가 오므로"), ("during", "during은 ‘~ 동안’이라 기한을 나타내지 못하므로"), ("in", "시각 앞에 in을 쓰지 않으므로"),
                                                   ("since", "since는 ‘~ 이래로’라 뜻이 맞지 않으므로"), ("by", "집에 오는 것은 9시까지 끝내야 하는 기한이라 by로 고쳐야 하므로")], 5)

# 3-118 B: 원문항과 같던 우리말·제시어를 새로
mk(3, 118, "B", [("The concert was held on July.", "월 앞에는 on이 아니라 in을 쓰므로"), ("The concert is held in July.", "과거의 일이므로 was held로 써야 하므로"), ("The concert was held in July.", "과거 수동태 was held와 월 앞의 in을 바르게 썼으므로"),
                 ("The concert held in July.", "‘열리다’는 be held로 써야 하므로"), ("The concert were held in July.", "단수 주어 The concert에는 was를 쓰므로")], 3,
   "과거에 열렸다는 뜻은 was/were held로 나타낸다. 연도·월에는 in, 날짜·요일에는 on, 시각에는 at을 쓴다.", "우리말·제시어·선택지 네 개가 원문항과 똑같았다. 우리말과 제시어를 ‘그 콘서트는 7월에 열렸다. (be held, July)’로 바꿨다.",
   p="그 콘서트는 7월에 열렸다. (be held, July)")

# 3-119 밑줄 친 우리말 영작: 원문항 발문, 대화 속 밑줄, 전치사 혼동 오답
ST119 = "다음 밑줄 친 우리말 문장을 올바르게 영작한 것을 고르시오."
R119 = "장소는 It is + 장소 표현으로 나타낸다. behind는 뒤, next to는 옆, across from은 맞은편, under는 아래, in front of는 앞이다."
S119 = "원문항의 밑줄 친 우리말이 밑줄 없이 제시되고 발문이 바뀌었으며, 동사가 빠진 문장이나 어순을 뒤집은 오답은 전치사를 몰라도 지워졌다. 원문항 발문과 대화 속 밑줄로 되돌리고 오답을 전치사 혼동 위주로 바꿨다."
def f119(t, p, items, a, s=S119):
    mk(3, 119, t, items, a, R119, s, st=ST119, p=p)
f119("B", "A: Where is the bank?\nB: <u>그것은 꽃집 뒤에 있어요</u>.\nA: Oh, I see. Thanks.",
     [("It's in front of the flower shop.", "in front of는 ‘앞’이라 뜻이 맞지 않으므로"), ("It's next to the flower shop.", "next to는 ‘옆’이라 뜻이 맞지 않으므로"), ("It's behind of the flower shop.", "behind 뒤에는 of를 쓰지 않으므로"),
      ("It's behind the flower shop.", "‘뒤에’를 behind로 바르게 옮겼으므로"), ("It's across from the flower shop.", "across from은 ‘맞은편’이라 뜻이 맞지 않으므로")], 4,
     "대화와 정답(between the bank and the hospital)이 원문항과 똑같았고 밑줄도 사라졌다. 대화를 새로 쓰고 원문항 발문과 밑줄로 되돌렸다.")
f119("C", "A: Where is the cafe?\nB: <u>그것은 학교 옆에 있어</u>.\nA: Thank you.",
     [("It's next to the school.", "‘옆에’를 next to로 바르게 옮겼으므로"), ("It's behind the school.", "behind는 ‘뒤’라 뜻이 맞지 않으므로"), ("It's next of the school.", "‘옆에’는 next of가 아니라 next to로 쓰므로"),
      ("It's in front of the school.", "in front of는 ‘앞’이라 뜻이 맞지 않으므로"), ("It's across from the school.", "across from은 ‘맞은편’이라 뜻이 맞지 않으므로")], 1)
f119("D", "A: Where is the park?\nB: <u>그것은 도서관 맞은편에 있어</u>.\nA: Thanks.",
     [("It's next to the library.", "next to는 ‘옆’이라 뜻이 맞지 않으므로"), ("It's across of the library.", "‘맞은편에’는 across of가 아니라 across from으로 쓰므로"), ("It's behind the library.", "behind는 ‘뒤’라 뜻이 맞지 않으므로"),
      ("It's in front of the library.", "in front of는 ‘앞’이라 뜻이 맞지 않으므로"), ("It's across from the library.", "‘맞은편에’를 across from으로 바르게 옮겼으므로")], 5)
f119("E", "A: Where is my bag?\nB: <u>그것은 의자 아래에 있어</u>.\nA: Oh, thank you.",
     [("It's on the chair.", "on은 ‘위’라 뜻이 맞지 않으므로"), ("It's next to the chair.", "next to는 ‘옆’이라 뜻이 맞지 않으므로"), ("It's under the chair.", "‘아래에’를 under로 바르게 옮겼으므로"),
      ("It's under of the chair.", "under 뒤에는 of를 쓰지 않으므로"), ("It's behind the chair.", "behind는 ‘뒤’라 뜻이 맞지 않으므로")], 3)
f119("F", "A: Where is the store?\nB: <u>그것은 은행 앞에 있어</u>.\nA: Thank you very much.",
     [("It's in front the bank.", "‘앞에’는 in front of로 써야 해 of가 빠졌으므로"), ("It's in front of the bank.", "‘앞에’를 in front of로 바르게 옮겼으므로"), ("It's behind the bank.", "behind는 ‘뒤’라 뜻이 맞지 않으므로"),
      ("It's across from the bank.", "across from은 ‘맞은편’이라 뜻이 맞지 않으므로"), ("It's in the front of the bank.", "in the front of는 ‘(건물) 안의 앞쪽’이라 뜻이 맞지 않으므로")], 2)

# 3-120 틀린 문장 개수: 원문항 발문과 형식(<보기>, ⓐ~ⓔ, 1개~5개)
ST120 = "다음 <보기>의 문장 중 어법상 올바르지 않은 문장은 몇 개인가?"
R120 = "시간은 at + 시각, on + 요일·날짜, in + 월·연도·계절로 나타내고, for는 기간의 길이, by는 완료 기한, until은 계속의 끝, during은 ‘~ 동안’(+ 명사)을 나타낸다. 장소는 at + 지점, on + 표면, in + 공간·도시·나라, between은 둘 사이이다."
S120 = "보기 기호 ⓐ~ⓔ가 a~e로 바뀌었고 선택지 순서가 뒤섞였으며, 발문에 괄호 조건이 붙었지만 괄호가 없는 유형도 있었다. 원문항 발문과 형식(<보기>, ⓐ~ⓔ 줄바꿈, 1개~5개)으로 되돌렸다."
def f120(t, lines, judge, bad, s=S120):
    n = len(bad.split(","))
    F(3, 120, t, st=ST120, p="<보기>\n" + "\n".join(lines), c=CNT5, a=n, r=R120, pre=["문장별 판정: " + j for j in judge], k=f"어법상 올바르지 않은 문장은 {bad}로 {n}개이다.", n="cnt", s=s + ipos(n))
f120("B", ["ⓐ I go jogging in the morning.", "ⓑ Tom has lived here for three years.", "ⓒ Put the vase at the table.", "ⓓ The meeting is on Tuesday.", "ⓔ She was born in May 3rd."],
     ["ⓐ O. 아침·오후·저녁에는 in the morning처럼 in을 쓴다.", "ⓑ O. 기간의 길이에는 for를 쓴다.", "ⓒ X. 탁자 위는 on the table로 쓴다.", "ⓓ O. 요일에는 on을 쓴다.", "ⓔ X. 날짜에는 on을 쓴다(on May 3rd)."], "ⓒ, ⓔ",
     "ⓐ·ⓑ가 원문항 문장(at winter, by five years)과 거의 같았고 형식도 원본과 달랐다. 문장을 새로 쓰고 원문항 발문과 형식으로 되돌렸다.")
f120("C", ["ⓐ Tom was born on 2010.", "ⓑ We meet at seven.", "ⓒ Jane lives in Seoul.", "ⓓ I waited by two hours.", "ⓔ The book is on the desk."],
     ["ⓐ X. 연도에는 in을 쓴다(in 2010).", "ⓑ O. 시각에는 at을 쓴다.", "ⓒ O. 도시에는 in을 쓴다.", "ⓓ X. 기간의 길이에는 for를 쓴다(for two hours).", "ⓔ O. 표면 위에는 on을 쓴다."], "ⓐ, ⓓ",
     S120)
f120("D", ["ⓐ School starts on eight.", "ⓑ We traveled during summer.", "ⓒ Tom lives at Korea.", "ⓓ Finish it until Friday.", "ⓔ The bag is among two chairs."],
     ["ⓐ X. 시각에는 at을 쓴다(at eight).", "ⓑ O. during + 기간 명사이다.", "ⓒ X. 나라에는 in을 쓴다(in Korea).", "ⓓ X. 끝내야 하는 기한에는 by를 쓴다(by Friday).", "ⓔ X. 둘 사이는 between을 쓴다."], "ⓐ, ⓒ, ⓓ, ⓔ",
     S120 + " 다른 유형과 정답 개수가 겹치지 않게 ⓐ·ⓔ를 틀린 문장으로 바꿨다.")
f120("E", ["ⓐ I was born on May.", "ⓑ We meet in Monday.", "ⓒ I have waited since two hours.", "ⓓ It rained during two hours.", "ⓔ We have a party at Christmas Day."],
     ["ⓐ X. 월에는 in을 쓴다(in May).", "ⓑ X. 요일에는 on을 쓴다(on Monday).", "ⓒ X. 기간의 길이에는 for를 쓴다(for two hours).", "ⓓ X. 기간의 길이(two hours)에는 during이 아니라 for를 쓴다.", "ⓔ X. 특정한 날에는 on을 쓴다(on Christmas Day)."], "ⓐ, ⓑ, ⓒ, ⓓ, ⓔ",
     "ⓒ(The picture is in the wall)가 괄호 속 뜻 설명에 기대야 틀린 문장이 되었고 형식도 원본과 달랐다. 뜻 설명 없이도 판정되는 문장으로 새로 쓰고 원문항 발문과 형식으로 되돌렸으며 정답 개수를 5개로 바꿨다.")
f120("F", ["ⓐ Jane is at home.", "ⓑ Tom was born on May 3rd.", "ⓒ We stayed there by three hours.", "ⓓ Finish the work by five.", "ⓔ The cat is on the table."],
     ["ⓐ O. ‘집에’는 at home이다.", "ⓑ O. 날짜에는 on을 쓴다.", "ⓒ X. 기간의 길이에는 for를 쓴다(for three hours).", "ⓓ O. 끝내야 하는 기한에는 by를 쓴다.", "ⓔ O. 표면 위에는 on을 쓴다."], "ⓒ")
