# 2급 CH11 전치사 (101~110) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def slots(c, a, why, labs, sep=r"\s+-\s+"):
    """짝 보기 해설: 정답과 다른 자리만 짚는다. why[j][x] = 그 자리에 x가 틀린 까닭"""
    sp = (lambda x: re.findall(r"\([AB]\) (\S+)", x)) if sep == "AB" else (lambda x: [p.strip() for p in re.split(sep, x)])
    good = sp(c[a-1]); out = []
    for i, ch in enumerate(c):
        parts = sp(ch)
        if i + 1 == a: out.append(f"{c[a-1]}: 모든 자리가 알맞으므로 정답이다."); continue
        out.append(" ".join(f"{labs[j]} {x}: {why[j][x]}" for j, x in enumerate(parts) if x != good[j]) + " 따라서 오답이다.")
    return out

# 2-101 이동 전치사: 원문항 발문, 길게 풀어 쓴 우리말 줄이기
ST101 = "다음 문장의 빈칸에 들어갈 가장 적절한 전치사를 고르시오."
S101 = "발문이 원문항과 달라(‘우리말의 이동 경로를 나타내도록’) 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
F(2, 101, "B", st=ST101, p="자전거를 탄 사람은 좁은 터널을 지나 반대편으로 나왔다.\nThe cyclist rode _____ the narrow tunnel and emerged on the other side.", s=S101 + " 우리말이 원문항보다 길고 자세해 짧게 줄였다.")
F(2, 101, "C", st=ST101, s=S101)
F(2, 101, "D", st=ST101, p="아이들은 들판을 가로질러 달려 문에 닿았다.\nThe children ran _____ the field to reach the gate.", s=S101 + " 우리말이 원문항보다 길고 자세해 짧게 줄였다.")
F(2, 101, "E", st=ST101, s=S101)
F(2, 101, "F", st=ST101, s=S101)

# 2-102 B: 원문항과 같던 공통어(off)·문장을 바꿈
R102 = "동사 + 부사(전치사)가 합쳐 새 뜻을 만든다. think ~ over는 ‘곰곰이 생각하다’, look over는 ‘훑어보다·검토하다’라는 뜻이다."
mk(2, 102, "B", [("up", "up: look up my essay는 ‘내 글을 찾아보다’라는 뜻이 되어 둘째 문장의 ‘검토하다’와 맞지 않으므로"), ("out", "out: look out my essay라는 표현은 없어 둘째 문장에 맞지 않으므로"),
                 ("over", "over: think it over(곰곰이 생각하다), look over(검토하다)에 공통으로 들어가므로"), ("off", "off: think it off, look off라는 표현이 없어 맞지 않으므로"),
                 ("down", "down: think it down, look down my essay는 뜻이 통하지 않아 맞지 않으므로")], 3, R102,
   "두 문장(the afternoon off / 40% off)과 정답(off)이 원문항(a day off / 30% off)과 사실상 같았다. 공통어를 over로, 문장을 think it over / look over로 바꿨다.",
   p="Let's think it _____ before we decide.\nCan you look _____ my essay before I hand it in?", k="think it over(곰곰이 생각하다)와 look over(검토하다)에 공통으로 over가 들어간다.")

# 2-103 위치 관계: 유형마다 다른 위치 관계로 정답을 다르게
R103 = "위치 전치사는 두 대상의 관계를 나타낸다. A가 B 앞(in front of)이면 B는 A 뒤(behind), A가 B 위(above)면 B는 A 아래(under/below), 맞은편(across from)과 옆(next to, beside)은 서로 같은 관계이다."
S103 = "원문항과 B~F가 모두 ‘X is ___ Y. = Y is next to X.’라는 같은 틀이고 정답도 모두 beside였다. 유형마다 다른 위치 관계로 바꿔 정답을 달리했다."
def f103(t, p, items, a):
    mk(2, 103, t, items, a, R103, S103, p=p)
f103("B", "The pharmacy is _____ the bakery.\n= The bakery is behind the pharmacy.",
     [("behind", "behind: 약국이 빵집 뒤에 있으면 빵집은 약국 앞에 있게 되어 뜻이 반대이므로"), ("in front of", "in front of: 빵집이 약국 뒤에 있으면 약국은 빵집 앞에 있으므로"),
      ("next to", "next to: 옆의 관계라 앞뒤 관계와 맞지 않으므로"), ("across from", "across from: 맞은편의 관계라 앞뒤 관계와 맞지 않으므로"), ("between", "between: 두 대상 사이를 나타내며 뒤에 대상이 둘 필요하므로")], 2)
f103("C", "The lamp is _____ the table.\n= The table is under the lamp.",
     [("below", "below: 전등이 탁자 아래에 있다는 반대 뜻이 되므로"), ("beside", "beside: 옆의 관계라 위아래 관계와 맞지 않으므로"), ("above", "above: 탁자가 전등 아래에 있으면 전등은 탁자 위에 있으므로"),
      ("behind", "behind: 뒤의 관계라 위아래 관계와 맞지 않으므로"), ("across from", "across from: 맞은편의 관계라 위아래 관계와 맞지 않으므로")], 3)
f103("D", "The school is _____ the park.\n= The park is across from the school.",
     [("behind", "behind: 뒤의 관계라 맞은편 관계와 맞지 않으므로"), ("under", "under: 아래의 관계라 맞은편 관계와 맞지 않으므로"), ("next to", "next to: 바로 옆의 관계라 맞은편 관계와 다르므로"),
      ("across from", "across from: 공원이 학교 맞은편에 있으면 학교도 공원 맞은편에 있으므로"), ("in front of", "in front of: 앞의 관계라 맞은편 관계와 다르므로")], 4)
f103("E", "The cat is _____ the bed.\n= The bed is above the cat.",
     [("on", "on: 고양이가 침대 위에 있다는 반대 뜻이 되므로"), ("above", "above: 고양이가 침대보다 위에 있다는 반대 뜻이 되므로"), ("beside", "beside: 옆의 관계라 위아래 관계와 맞지 않으므로"),
      ("in front of", "in front of: 앞의 관계라 위아래 관계와 맞지 않으므로"), ("under", "under: 침대가 고양이 위에 있으면 고양이는 침대 아래에 있으므로")], 5)
f103("F", "The bus stop is _____ the post office.\n= The post office is in front of the bus stop.",
     [("behind", "behind: 우체국이 정류장 앞에 있으면 정류장은 우체국 뒤에 있으므로"), ("in front of", "in front of: 정류장이 우체국 앞에 있다는 반대 뜻이 되므로"),
      ("under", "under: 아래의 관계라 앞뒤 관계와 맞지 않으므로"), ("between", "between: 두 대상 사이를 나타내며 뒤에 대상이 둘 필요하므로"), ("above", "above: 위의 관계라 앞뒤 관계와 맞지 않으므로")], 1)

# 2-104 at/on/in/during 밑줄: 원문항 발문·형식
ST104 = "다음 밑줄 친 부분이 어법상 옳은 문장을 고르시오."
R104 = "시각·정오·새벽 같은 한 시점은 at, 요일·날짜·특정한 날은 on, 월·계절·연도·아침/저녁은 in을 쓴다. during 뒤에는 명사(구)가, while 뒤에는 주어 + 동사가 온다."
S104 = "원문항은 시간 전치사 at/on/in/during의 구별을 밑줄로 묻는데, 변형은 during과 while의 구별로 평가 요소가 바뀌었고 밑줄이 없었으며, 옳은 문장이 같은 내용의 틀린 문장과 짝을 이루고 오답이 유형마다 같았다. 원문항 발문과 형식으로 되돌려 at/on/in/during 밑줄 문장 다섯 개로 유형마다 새로 썼다."
def W(what, fix): return f"{what}에는 {fix}을(를) 써야 하므로"
mk(2, 104, "B", [("We stayed indoors <u>during the storm</u>.", "during + 명사(the storm)로 특정 기간을 바르게 나타냈으므로"), ("The party starts <u>on 7 p.m.</u>", W("시각", "at")), ("I was born <u>at 2010</u>.", W("연도", "in")),
                 ("See you <u>in Monday</u>.", W("요일", "on")), ("We go skiing <u>on winter</u>.", W("계절", "in"))], 1, R104, S104, st=ST104)
mk(2, 104, "C", [("The store opens <u>in 9 a.m.</u>", W("시각", "at")), ("My birthday is <u>at May 3rd</u>.", W("날짜", "on")), ("We have a test <u>in Friday</u>.", W("요일", "on")),
                 ("The movie starts <u>at 8 o'clock</u>.", "시각 앞에 at을 바르게 썼으므로"), ("It often snows <u>on December</u>.", W("월", "in"))], 4, R104, S104, st=ST104)
mk(2, 104, "D", [("Let's meet <u>on noon</u>.", W("정오(noon)", "at")), ("The festival is held <u>at October</u>.", W("월", "in")), ("We watched fireworks <u>in New Year's Eve</u>.", W("특정한 날", "on")),
                 ("He fell asleep <u>while the movie</u>.", "명사(the movie) 앞에는 while이 아니라 during을 써야 하므로"), ("The shop is closed <u>on Sundays</u>.", "요일 앞에 on을 바르게 썼으므로")], 5, R104, S104, st=ST104)
mk(2, 104, "E", [("The lights went out <u>during we watched TV</u>.", "주어 + 동사 앞에는 during이 아니라 while을 써야 하므로"), ("Our school was built <u>in 1995</u>.", "연도 앞에 in을 바르게 썼으므로"),
                 ("I'll call you <u>at Tuesday</u>.", W("요일", "on")), ("The class ends <u>on 3:30</u>.", W("시각", "at")), ("Leaves turn red <u>at fall</u>.", W("계절", "in"))], 2, R104, S104, st=ST104)
mk(2, 104, "F", [("Mina visited Paris <u>on 2019</u>.", W("연도", "in")), ("We have lunch <u>in noon</u>.", W("정오(noon)", "at")), ("I usually wake up <u>at dawn</u>.", "새벽(dawn) 같은 한 시점 앞에 at을 바르게 썼으므로"),
                 ("They got married <u>at June</u>.", W("월", "in")), ("The game is <u>in Saturday afternoon</u>.", "특정 요일의 오후(Saturday afternoon)에는 on을 써야 하므로")], 3, R104, S104, st=ST104)

# 2-105 개수 보기 정렬 + 줄바꿈
for t, (o, nw) in {"B": ("⑤", "③"), "C": ("①", "④"), "D": ("③", "④"), "E": ("⑤", "④"), "F": ("②", "④")}.items():
    F(2, 105, t, p="BR", op="sortc", s=f"개수 선택지를 1개~5개 순으로 정렬(정답 {o}→{nw})하고, 한 줄로 이어 쓴 ⓐ~ⓔ를 한 줄에 한 문장씩 나눴다.")

# 2-106 for/since: 판단 기준을 알려 주던 발문을 원문항대로
for t in "BCDEF":
    F(2, 106, t, st="R", s="발문이 ‘과거에 시작해 지금까지 이어지는 상황, 기간 또는 시작 시점으로 해석할 때’라고 판단 기준을 알려 주어 원문항 발문으로 되돌렸다. 현재완료 문장이라 조건 없이도 정답은 하나다. 보기와 정답은 그대로다.")

# 2-107 구동사: 원문항 발문, 유형마다 정답 구동사를 다르게
ST107 = "다음 대화의 빈칸에 들어갈 가장 적절한 표현을 고르시오."
R107 = "구동사는 동사 + 부사(전치사)가 합쳐 새 뜻을 만든다: put off(미루다), look after(돌보다), turn down(거절하다), give up(포기하다), put on(입다), take off(벗다·이륙하다), turn off(끄다). 대화의 상황에 맞는 뜻을 고른다."
S107 = "발문이 ‘미루지 말라고 조언하도록’이라고 정답의 뜻을 알려 주었고, 정답이 원문항과 같은 put off였다. 원문항 발문으로 되돌리고, 유형마다 정답 구동사를 달리해 대화를 새로 썼다."
def PV(v, m, ok): return f"{v}: ‘{m}’라는 뜻이라 대화의 상황에 {'맞으므로' if ok else '맞지 않으므로'}"
mk(2, 107, "B", [("put off", PV("put off", "미루다", 0)), ("look after", PV("look after", "돌보다", 1)), ("turn down", PV("turn down", "거절하다", 0)), ("give up", PV("give up", "포기하다", 0)), ("take off", PV("take off", "벗다·이륙하다", 0))], 2, R107, S107,
   st=ST107, p="A: I'm going on a trip. Who will feed my dog?\nB: Don't worry. I'll ____________ your dog while you're away.")
mk(2, 107, "C", [("put on", PV("put on", "입다", 0)), ("looked after", PV("looked after", "돌보았다", 0)), ("turned down", PV("turned down", "거절했다", 1)), ("took off", PV("took off", "벗었다·이륙했다", 0)), ("got on", PV("got on", "탔다", 0))], 3, R107, S107,
   st=ST107, p="A: Did you accept the job offer?\nB: No, I ____________ the offer because the pay was too low.")
mk(2, 107, "D", [("turn down", PV("turn down", "거절하다", 0)), ("look after", PV("look after", "돌보다", 0)), ("put on", PV("put on", "입다", 0)), ("give up", PV("give up", "포기하다", 1)), ("get off", PV("get off", "내리다", 0))], 4, R107, S107,
   st=ST107, p="A: This puzzle is too hard. I want to stop.\nB: Don't ____________! You're almost done.")
mk(2, 107, "E", [("take off", "take off: ‘벗다’라는 뜻이라 추운 날씨에 외투를 벗으라는 반대 뜻이 되므로"), ("turn down", PV("turn down", "거절하다", 0)), ("look after", PV("look after", "돌보다", 0)), ("give up", PV("give up", "포기하다", 0)), ("put on", PV("put on", "입다", 1))], 5, R107, S107,
   st=ST107, p="A: It's freezing outside.\nB: You should ____________ your coat before you go out.")
mk(2, 107, "F", [("turn off", PV("turn off", "끄다", 1)), ("turn on", PV("turn on", "켜다", 0)), ("put on", PV("put on", "입다", 0)), ("look for", PV("look for", "찾다", 0)), ("give up", PV("give up", "포기하다", 0))], 1, R107, S107,
   st=ST107, p="A: The TV is still on, and nobody is watching it.\nB: Please ____________ the TV to save electricity.")

# 2-108 (A)(B) 전치사: 원문항 발문·밑줄, 우리말 설명 삭제, B·E는 구동사를 원문항과 다르게
ST108 = "다음 문장의 빈칸 (A), (B)에 들어갈 전치사가 바르게 짝지어진 것은?"
UA, UB = "(<u>     A     </u>)", "(<u>     B     </u>)"
def p108(a, b): return f"- {a.replace('(A)', UA)}\n- {b.replace('(B)', UB)}"
S108 = "원문항에 없던 우리말 상황 설명이 붙고 빈칸 밑줄이 없었다. 원문항 발문과 형식(밑줄 친 빈칸, - 문장)으로 되돌렸다."
c = ["(A) on - (B) up", "(A) off - (B) out", "(A) in - (B) down", "(A) up - (B) on", "(A) out - (B) for"]
F(2, 108, "B", st=ST108, p=p108("Please put (A) your helmet before riding.", "Never give (B) on your dreams."), c=c, a=1,
  r="put on은 ‘입다·쓰다’, give up on은 ‘~을 포기하다’라는 뜻이다.",
  n=slots(c, 1, [{"off": "put off는 ‘미루다’라는 뜻이라 헬멧을 쓴다는 뜻과 맞지 않는다.", "in": "put in은 ‘넣다’라는 뜻이라 맞지 않는다.", "up": "put up은 ‘세우다·걸다’라는 뜻이라 맞지 않는다.", "out": "put out은 ‘(불을) 끄다’라는 뜻이라 맞지 않는다."},
                  {"out": "give out은 ‘나눠 주다’라는 뜻이라 맞지 않는다.", "down": "give down이라는 표현은 없다.", "on": "give on on이라는 표현은 없다.", "for": "give for on이라는 표현은 없다."}], ["(A)", "(B)"], sep="AB"),
  k="헬멧을 ‘쓰다’는 put on, 꿈을 ‘포기하다’는 give up (on)이다.", s=S108 + " 구동사(take off, look for)와 정답 조합이 원문항과 똑같아 put on / give up으로 바꿨다. 정답 위치 ①.")
for t in "CDF":
    F(2, 108, t, st=ST108, p=p108(*[re.sub(r"\((A|B)\)", r"(\1)", x) for x in V(2, 108, t)["passage"].split("\n")[1:3]]), s=S108 + " 보기와 정답은 그대로다.")
c = ["(A) out - (B) into", "(A) off - (B) up", "(A) up - (B) after", "(A) down - (B) at", "(A) on - (B) over"]
F(2, 108, "E", st=ST108, p=p108("The meeting was put (A) until Friday.", "Jane is looking (B) the word in the dictionary."), c=c, a=2,
  r="put off는 ‘미루다·연기하다’, look up은 ‘(사전 등에서) 찾아보다’라는 뜻이다.",
  n=slots(c, 2, [{"out": "put out은 ‘(불을) 끄다’라는 뜻이라 회의를 연기했다는 뜻과 맞지 않는다.", "up": "put up은 ‘세우다·걸다’라는 뜻이라 맞지 않는다.", "down": "put down은 ‘내려놓다’라는 뜻이라 맞지 않는다.", "on": "put on은 ‘입다·(공연을) 올리다’라는 뜻이라 맞지 않는다."},
                  {"into": "look into는 ‘조사하다’라는 뜻이라 사전에서 단어를 찾는다는 뜻과 맞지 않는다.", "after": "look after는 ‘돌보다’라는 뜻이라 맞지 않는다.", "at": "look at은 ‘보다’라는 뜻이라 사전에서 찾는다는 뜻이 드러나지 않는다.", "over": "look over는 ‘훑어보다’라는 뜻이라 맞지 않는다."}], ["(A)", "(B)"], sep="AB"),
  k="회의가 ‘연기되었다’는 was put off, 사전에서 ‘찾아보다’는 look up이다.", s=S108 + " 정답 조합(off - for)과 (B)의 look for가 원문항과 같아 (B)를 look up 문장으로 바꿨다. 정답 위치 ②.")

# 2-109 세 이동 경로: 원문항 발문, 우리말 삭제, 경로·오답 조합을 유형마다 새로
ST109 = "다음 문장의 빈칸에 들어갈 전치사가 순서대로 짝지어진 것을 고르시오."
R109 = "이동 전치사는 out of(밖으로), into(안으로), across(가로질러), along(따라), over(넘어), up/down(위로/아래로), under(아래로), between(둘 사이), among(여럿 사이)을 구별한다. 세 자리가 모두 문장의 뜻과 맞아야 한다."
S109 = "원문항에 없던 우리말 뜻이 붙고 발문이 달랐으며, 정답 조합이 원문항(out of - across - into)과 같거나 오답 조합 네 개가 유형마다 같았다. 원문항 발문으로 되돌리고 우리말을 지웠으며, 유형마다 이동 경로와 오답 조합을 새로 썼다."
LAB = ["첫째 빈칸", "둘째 빈칸", "셋째 빈칸"]
F(2, 109, "B", st=ST109, p="The cat jumped ________ the box, ran ________ the room, and hid ________ the bed.",
  s="원문항에 없던 우리말 뜻이 붙고 발문이 달라, 원문항 발문으로 되돌리고 우리말을 지웠다. 보기와 정답은 그대로다.")
def f109(t, p, c, a, why, k, s=""):
    F(2, 109, t, st=ST109, p=p, c=c, a=a, r=R109, n=slots(c, a, why, LAB), k=k, s=S109 + s + ipos(a))
f109("C", "The child climbed ________ the fence, walked ________ the river, and sat ________ two big trees.",
     ["over - along - among", "into - along - between", "over - along - between", "over - onto - between", "over - between - along"], 3,
     [{"into": "울타리 ‘안으로’ 올라간다는 뜻은 통하지 않는다."}, {"onto": "강 ‘위로’ 걸어 올라간다는 뜻은 통하지 않는다.", "between": "강 ‘사이’를 걷는다는 뜻은 통하지 않는다."},
      {"among": "among은 셋 이상 사이에 쓰며, 두 나무 사이는 between이다.", "along": "두 나무를 ‘따라’ 앉는다는 뜻은 통하지 않는다."}],
     "울타리를 ‘넘어’ over, 강을 ‘따라’ along, 두 나무 ‘사이에’ between이다.", " C는 경로를 ‘넘어 - 따라 - 둘 사이’로 바꿨다.")
f109("D", "The bird flew ________ the cage, passed ________ the yard, and disappeared ________ the trees.",
     ["out of - among - across", "at - across - among", "out of - to - among", "out of - across - among", "under - across - to"], 4,
     [{"at": "새장 ‘을 향해’ 날아서는 새장에서 빠져나가는 뜻이 되지 않는다.", "under": "새장 ‘아래로’ 날아간다는 뜻은 뒤의 흐름과 맞지 않는다."}, {"among": "마당은 여럿이 아니므로 among을 쓸 수 없다.", "to": "마당을 ‘지나간다(passed)’는 뜻에 to는 맞지 않는다."},
      {"across": "나무들 ‘을 가로질러’ 사라진다는 뜻은 통하지 않는다.", "to": "disappeared to the trees라는 표현은 쓰지 않는다."}],
     "새장 ‘밖으로’ out of, 마당을 ‘가로질러’ across, 여러 나무 ‘사이로’ among이다.")
f109("E", "Tom walked ________ the stairs, went ________ the hallway, and stopped ________ the door.",
     ["into - down - at", "up - among - at", "up - down - among", "at - down - into", "up - down - at"], 5,
     [{"into": "계단 ‘안으로’ 걷는다는 뜻은 통하지 않는다.", "at": "walked at the stairs라는 표현은 쓰지 않는다."}, {"among": "복도는 여럿이 아니므로 among을 쓸 수 없다."},
      {"among": "문 하나 앞에 멈추는 것이므로 among은 맞지 않는다.", "into": "문 ‘안으로’ 멈춘다는 뜻은 통하지 않는다."}],
     "계단을 ‘올라’ up, 복도를 ‘따라 쭉’ down, 문 ‘앞에(한 지점)’ at이다.", " E는 경로를 ‘계단 위로 - 복도를 따라 - 문 앞에서’로 바꿨다.")
f109("F", "The ball rolled ________ the bag, bounced ________ the floor, and went ________ the sofa.",
     ["out of - across - under", "out of - among - under", "at - across - under", "out of - across - among", "into - between - under"], 1,
     [{"at": "rolled at the bag이라는 표현은 쓰지 않는다.", "into": "공이 가방 ‘안으로’ 굴러 들어간 뒤 바닥을 튀어 간다는 흐름과 맞지 않는다."}, {"among": "바닥은 여럿이 아니므로 among을 쓸 수 없다.", "between": "바닥 ‘사이’를 튀어 간다는 뜻은 통하지 않는다."},
      {"among": "소파 하나 아래로 들어가는 것이므로 among은 맞지 않는다."}],
     "가방 ‘밖으로’ out of, 바닥을 ‘가로질러’ across, 소파 ‘아래로’ under이다.")

# 2-110 올바른 문장 개수: 보기 정렬·줄바꿈, 정답 개수를 유형마다 다르게
R110 = "by는 ‘~까지’ 끝내야 하는 완료 기한, until은 ‘~까지’ 계속되는 상태의 끝을 나타낸다. for + 숫자 기간, during + 특정 기간·사건 명사, while + 주어 + 동사, at + 시각을 구별한다."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]
def br110(p): return re.sub(r"\s*-\s(?=[A-Z])", "\n- ", p).replace("<보기>\n- ", "<보기>\n- ", 1)
for t, (o, nw) in {"B": ("④", "④"), "E": ("③", "④")}.items():
    F(2, 110, t, p=br110(V(2, 110, t)["passage"]), op="sortc", s=f"개수 선택지를 1개~5개 순으로 정렬(정답 {o}→{nw})하고, 한 줄로 이어 쓴 문장을 한 줄에 하나씩 나눴다.")
def f110(t, lines, judge, ok, s):
    n = len(ok.split(","))
    F(2, 110, t, p="<보기>\n" + "\n".join("- " + x for x in lines), c=CNT5, a=n, r=R110, pre=["문장별 판정: " + j for j in judge], k=f"밑줄 친 부분이 올바른 문장은 {ok}로 {n}개이다.", n="cnt", s=s + ipos(n))
f110("C", ["Stay here <u>until six</u>.", "Finish the work <u>until Friday</u>.", "We talked <u>during two hours</u>.", "The lights went out <u>during the storm</u>.", "Tom came <u>around noon</u>."],
     ["첫째 O. 머무는 상태가 6시까지 이어지므로 until이다.", "둘째 X. 금요일까지 끝내야 하는 기한이므로 by를 쓴다.", "셋째 X. 숫자로 나타낸 기간은 for를 쓴다(for two hours).", "넷째 O. 특정 사건(the storm) 동안이므로 during이다.", "다섯째 O. 대략의 시각은 around이다."],
     "첫째, 넷째, 다섯째", "개수 선택지 순서가 뒤섞여 1개~5개 순으로 정렬하고 줄을 바꿨다. B~E 모두 틀린 문장이 하나뿐이라 정답(4개)이 같아, 둘째 문장을 ‘until Friday’(틀림)로 바꿔 올바른 문장이 3개가 되게 했다.")
f110("D", ["I waited <u>until midnight</u>.", "Submit this <u>until Monday</u>.", "Jane lived there <u>for five years</u>.", "Tom slept <u>while the flight</u>.", "The bus came <u>on seven sharp</u>."],
     ["첫째 O. 기다리는 상태가 자정까지 이어지므로 until이다.", "둘째 X. 월요일까지 내야 하는 기한이므로 by를 쓴다.", "셋째 O. 숫자로 나타낸 기간이므로 for이다.", "넷째 X. 명사(the flight) 앞에는 during을 쓴다.", "다섯째 X. 시각 앞에는 at을 쓴다(at seven sharp)."],
     "첫째, 셋째", "개수 선택지 순서가 뒤섞여 1개~5개 순으로 정렬하고 줄을 바꿨다. B~E 모두 정답(4개)이 같아, 둘째·다섯째 문장을 틀린 문장으로 바꿔 올바른 문장이 2개가 되게 했다.")
f110("F", ["The store is open <u>until ten</u>.", "Send the file <u>until noon</u>.", "We worked <u>for three hours</u>.", "Jane rested <u>while the break</u>.", "Tom arrived <u>on six</u>."],
     ["첫째 O. 문을 연 상태가 10시까지 이어지므로 until이다.", "둘째 X. 정오까지 보내야 하는 기한이므로 by를 쓴다.", "셋째 O. 숫자로 나타낸 기간 앞에 for를 썼다.", "넷째 X. 명사(the break) 앞에는 during을 쓴다.", "다섯째 X. 시각 앞에는 at을 쓴다(at six)."],
     "첫째, 셋째", "틀린 문장이 없어 원문항(틀린 것을 판별)과 인지 과정이 달랐다. 둘째·넷째·다섯째를 틀린 문장으로 바꿔 올바른 문장이 2개가 되게 하고(원문항의 정답 1개와 겹치지 않게), 선택지를 1개~5개 순으로 정렬해 줄을 바꿨다.")

# ---- 2차 감수(2026-10) 추가 ----
# 2-102 F: C와 정답(out)·둘째 문장(The lights went out)이 겹침 → 공통어 on으로
mk(2, 102, "F", [("on", "on: turn on(켜다), try on(입어 보다)에 공통으로 들어가므로"), ("down", "down: turn down은 되지만 try down이라는 표현은 없으므로"), ("off", "off: turn off는 되지만 try off라는 표현은 없으므로"),
                 ("up", "up: turn up은 되지만 try up이라는 표현은 없으므로"), ("over", "over: turn over the light, try over this jacket은 뜻이 통하지 않으므로")], 1,
   "동사 + 부사(전치사)가 합쳐 새 뜻을 만든다. turn on은 ‘켜다’, try on은 ‘입어 보다’라는 뜻이다.",
   "정답(out)과 둘째 문장(The lights went out …)이 C유형과 겹쳤다. 공통어를 on으로, 문장을 turn on / try on으로 바꿨다.",
   p="Please turn _____ the light; it's getting dark.\nYou should try _____ this jacket before you buy it.")
# 2-105 B: 정답 개수·위치(3개, ③)가 원문항과 같음 → ⓓ를 틀린 문장으로 바꿔 2개
FIX.pop((2, 105, "B"), None)
F(2, 105, "B", p="ⓐ The meeting begins at 2 p.m. sharp.\nⓑ We usually eat around noon.\nⓒ Jane stayed there during three hours.\nⓓ The shop closes on 9 p.m.\nⓔ Tom finished the work until Friday.", c=CNT5, a=2,
  r="시각 앞에는 at, 대략의 시각 앞에는 around를 쓴다. 숫자로 나타낸 기간 앞에는 for를 쓰고(during은 the vacation 같은 특정 기간 앞), 기한은 by, 그때까지 계속되는 일은 until로 나타낸다.",
  pre=["문장별 판정: ⓐ O. 시각 앞에 at을 썼다.", "문장별 판정: ⓑ O. 대략의 시각 앞에 around를 썼다.", "문장별 판정: ⓒ X. 숫자로 나타낸 기간은 for를 쓴다(for three hours).", "문장별 판정: ⓓ X. 시각 앞에는 at을 쓴다(at 9 p.m.).",
       "문장별 판정: ⓔ X. 금요일까지 끝냈다는 기한이므로 by를 쓴다(by Friday)."],
  k="어법상 옳은 문장은 ⓐ, ⓑ로 2개이다.", n="cnt", s="개수 선택지를 1개~5개 순으로 정렬하고, 한 줄로 이어 쓴 ⓐ~ⓔ를 한 줄에 한 문장씩 나눴다. 정답 개수·위치(3개, ③)가 원문항과 같아 ⓓ를 틀린 문장(on 9 p.m.)으로 바꿔 2개가 되게 했다. 정답 위치 ②.")
# 2-108 C: 우리말을 지우면 (B)에 for(동생을 찾다)도 가능 → after만 맞는 문장으로
FIX.pop((2, 108, "C"), None)
mk(2, 108, "C", [("(A) down - (B) at", "turn down the lights는 ‘불빛을 줄이다’라 떠나기 전에 할 일로 맞지 않고, look at은 ‘바라보다’라 뒤의 이유와 맞지 않으므로"),
                 ("(A) out - (B) into", "turn out the lights는 되지만 look into는 ‘조사하다’라 뒤의 이유와 맞지 않으므로"),
                 ("(A) off - (B) for", "turn off는 맞지만 look for는 ‘찾다’라 ‘혼자 있기엔 너무 어려서’라는 이유와 맞지 않으므로"),
                 ("(A) off - (B) after", "turn off(끄다), look after(돌보다)가 두 문장의 뜻에 모두 맞으므로"),
                 ("(A) up - (B) after", "look after는 맞지만 turn up the lights는 ‘불을 더 밝게 하다’라 떠나기 전에 할 일로 맞지 않으므로")], 4,
   "turn off는 ‘끄다’, look after는 ‘돌보다’, look for는 ‘찾다’, look into는 ‘조사하다’라는 뜻이다. 문장의 뜻에 맞는 구동사를 고른다.",
   S108 + " 우리말을 지우면 (B)에 for(동생을 찾고 있다)도 들어갈 수 있어, after만 맞도록 (B) 문장을 ‘Tom has to look (B) his baby sister because she is too young to stay alone.’으로 바꿨다. 보기는 그대로다.",
   st=ST108, p=p108("Please turn (A) the lights before you leave.", "Tom has to look (B) his baby sister because she is too young to stay alone."))
