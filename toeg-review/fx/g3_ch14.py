# 3급 CH14 문장의 종류 (131~140) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."

def slotnote(ch, good, why, labs=("첫째", "둘째", "셋째"), sep=" - "):
    xs = [x.strip() for x in ch.split(sep)]; gs = [x.strip() for x in good.split(sep)]
    if xs == gs: return "모든 빈칸에 알맞은 말을 골랐으므로"
    bits = [f"{labs[i]} 빈칸 {x}: {w}" for i, (x, g, w) in enumerate(zip(xs, gs, why)) if x != g]
    return ", ".join(bits) + ". 따라서"

# 3-131 명령문·Let's + 동사원형: 원문항처럼 우리말 해석, 오답은 그 문항의 동사로 형태만 바꿈
R131 = "명령문은 주어 없이 동사원형으로 시작하고, Let's 뒤에도 동사원형을 쓴다."
S131 = "오답 네 개가 원문항의 동사(Brushing - watching 등)를 그대로 가져와 문장과 맞지 않아 새 동사가 들어간 선택지 하나만 남았고, 원문항의 문장별 우리말 해석도 빠졌다. 오답을 그 문항의 동사로 형태만 바꿔 쓰고 우리말 해석을 붙였다."
W131 = ["명령문은 동사원형으로 시작한다", "Let's 뒤에는 동사원형을 쓴다"]
def f131(t, p, c, a, s=S131):
    mk(3, 131, t, [(x, slotnote(x, c[a-1], W131)) for x in c], a, R131, s, p=p, okdup=True)
f131("B", "_____ the window, please.(창문 좀 열어 주세요.)\nLet's _____ lunch together.(함께 점심을 먹자.)", ["Opening - have", "Open - having", "To open - to have", "Open - have", "Opens - has"], 4,
     "제시문과 정답(Brush - watch)이 원문항과 똑같았고 우리말 해석도 빠졌다. 문장을 새로 쓰고 원문항처럼 우리말 해석을 붙였다.")
f131("C", "_____ the door, please.(문 좀 닫아 주세요.)\nLet's _____ soccer after school.(방과 후에 축구를 하자.)", ["Closing - playing", "Close - play", "To close - to play", "Close - playing", "Closes - plays"], 2)
f131("D", "_____ careful on the stairs.(계단에서 조심해라.)\nLet's _____ home now.(이제 집에 가자.)", ["Being - go", "Are - go", "Be - going", "To be - to go", "Be - go"], 5)
f131("E", "_____ your homework first.(먼저 숙제를 끝내라.)\nLet's _____ dinner after that.(그다음에 저녁을 먹자.)", ["Finish - eat", "Finishing - eat", "Finish - eating", "To finish - to eat", "Finishes - eats"], 1)
f131("F", "_____ quiet in the library.(도서관에서는 조용히 해라.)\nLet's _____ the teacher clean up.(선생님이 청소하시는 것을 돕자.)", ["Are - help", "Being - helping", "Be - help", "Be - helping", "To be - to help"], 3)

# 3-132 명령문 + and/or ↔ If: 원문항 발문, 유형마다 오답 조합을 새로
ST132 = "다음 두 문장을 같은 뜻이 되도록 하는 단어를 고르시오."
R132 = "명령문 + and는 ‘~해라, 그러면’(If you ~), 명령문 + or는 ‘~해라, 그렇지 않으면’(If you don't ~)의 뜻이다."
S132 = "원문항에 없던 우리말 뜻이 발문에 붙어 둘째 빈칸의 부정형을 알려 주었고, 오답 조합이 유형마다 같았다. 원문항 발문으로 되돌리고 유형마다 오답 조합을 새로 썼다."
def f132(t, p, c, a, why, s=S132):
    mk(3, 132, t, [(x, slotnote(x, c[a-1], why)) for x in c], a, R132, s, st=ST132, p=p, okdup=True)
f132("B", "Get up early, _____ you will catch the first train.\nIf you _____ up early, you will catch the first train.", ["or - get", "and - get", "and - don't get", "or - don't get", "but - get"], 2,
     ["‘일찍 일어나면’ 첫 기차를 탄다는 뜻이라 명령문 + and를 쓴다", "If절도 ‘일찍 일어나면’이라 긍정의 get을 쓴다"],
     "제시문과 정답(or - don't)이 원문항과 똑같았고 발문에 뜻도 붙었다. 원문항 발문으로 되돌리고, 명령문 + and ↔ If you ~로 바꾸는 문장으로 새로 썼다.")
f132("C", "Hurry up, _____ you will miss the bus.\nIf you _____ hurry, you will miss the bus.", ["and - do", "or - do", "and - don't", "or - don't", "but - do"], 4,
     ["‘서두르지 않으면’ 버스를 놓친다는 뜻이라 명령문 + or를 쓴다", "If절은 ‘서두르지 않으면’이라 don't를 쓴다"])
f132("D", "Take this medicine, _____ you will feel better.\nIf you _____ this medicine, you will feel better.", ["and - take", "or - take", "and - don't take", "or - don't take", "so - take"], 1,
     ["‘약을 먹으면’ 나아진다는 뜻이라 명령문 + and를 쓴다", "If절도 ‘약을 먹으면’이라 긍정의 take를 쓴다"], S132 + " 명령문 + and 문장으로 바꿔 다른 유형과 달리했다.")
f132("E", "Be careful, _____ you will make a mistake.\nIf you _____ careful, you will make a mistake.", ["or - are", "and - are", "and - aren't", "but - aren't", "or - aren't"], 5,
     ["‘조심하지 않으면’ 실수한다는 뜻이라 명령문 + or를 쓴다", "If절은 ‘조심하지 않으면’이고 be동사 문장이라 aren't를 쓴다"])
f132("F", "Take an umbrella, _____ you will get wet.\nIf you _____ take one, you will get wet.", ["and - do", "or - aren't", "or - don't", "and - don't", "but - do"], 3,
     ["‘우산을 가져가지 않으면’ 젖는다는 뜻이라 명령문 + or를 쓴다", "If절은 일반동사 take의 부정이라 don't를 쓴다"])

# 3-133 What/How 감탄문 전환: 발문의 괄호 조건 삭제
ST133 = "다음 두 문장을 같은 뜻이 되도록 하는 단어를 고르시오."
R133 = "감탄문은 What + a/an + 형용사 + 명사 + 주어 + 동사!, How + 형용사 + 주어 + 동사!의 어순이다."
S133 = "발문의 ‘(주어와 동사는 평서문 어순으로 쓸 것.)’이 첫 빈칸의 정답(주어 + 동사)을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
mk(3, 133, "B", [("this is - a delicious", "How 뒤에는 a 없이 형용사만 쓰므로"), ("is this - delicious", "감탄문은 주어 + 동사 어순이라 this is로 쓰므로"), ("this is - delicious", "What 감탄문의 주어 + 동사(this is)와 How 뒤 형용사(delicious)를 바르게 골랐으므로"),
                 ("this are - delicious", "단수 주어 this에는 is를 쓰므로"), ("this is - deliciously", "How 뒤에는 be동사의 보어인 형용사를 쓰므로")], 3, R133,
   "제시문과 정답이 원문항과 똑같았고 없는 형태(tallly)가 오답에 있었다. 문장을 새로 쓰고 원문항 발문으로 되돌렸으며 오답을 실제 형태로 바꿨다.", st=ST133, p="What a delicious cake ______!\nHow _____ the cake is!", okdup=True)
for t in "CDEF": F(3, 133, t, st=ST133, s=S133)

# 3-134 부가의문문 답의 뜻: 원문항 발문과 밑줄, 같은 문장의 부정·시제 변형 오답
ST134 = "다음 밑줄 친 부분의 의미로 알맞은 것을 고르시오."
R134 = "부가의문문에 답할 때는 사실이 긍정이면 Yes + 긍정, 부정이면 No + 부정으로 답한다. 답의 조동사·be동사로 시제를 확인한다."
S134 = "오답 세 개가 다른 유형의 대화 내용(Tom은 바쁘다 등)이라 바로 지워졌고 밑줄도 사라졌다. 원문항 발문과 밑줄로 되돌리고 오답을 원문항처럼 그 대화 문장의 부정·시제 변형으로 바꿨다."
def f134(t, p, items, a, s=S134):
    mk(3, 134, t, items, a, R134, s, st=ST134, p=p)
f134("B", "A: Minho plays the piano, doesn't he?\nB: <u>No, he doesn't</u>.",
     [("Minho는 피아노를 친다.", "No, he doesn't는 부정의 답이므로"), ("Minho는 피아노를 치지 않는다.", "No, he doesn't는 현재의 부정(치지 않는다)이므로"), ("Minho는 피아노를 쳤다.", "doesn't는 현재이고 부정이므로"),
      ("Minho는 피아노를 치지 않았다.", "doesn't는 과거가 아니라 현재이므로"), ("Minho는 피아노를 칠 것이다.", "doesn't는 미래가 아니라 현재의 부정이므로")], 2,
     "대화와 정답이 원문항과 똑같았고 오답 세 개가 관계없는 문장이었다. 대화를 새로 쓰고 원문항 발문과 밑줄로 되돌렸으며 오답을 같은 문장의 부정·시제 변형으로 바꿨다.")
f134("C", "A: Tom isn't busy, is he?\nB: <u>No, he isn't</u>.",
     [("Tom은 바쁘다.", "No, he isn't는 부정의 답이므로"), ("Tom은 바빴다.", "isn't는 현재이고 부정이므로"), ("Tom은 바쁘지 않았다.", "isn't는 과거가 아니라 현재이므로"),
      ("Tom은 바쁘지 않다.", "No, he isn't는 현재의 부정(바쁘지 않다)이므로"), ("Tom은 바쁠 것이다.", "isn't는 미래가 아니라 현재의 부정이므로")], 4)
f134("D", "A: They went home, didn't they?\nB: <u>Yes, they did</u>.",
     [("그들은 집에 갔다.", "Yes, they did는 과거의 긍정(갔다)이므로"), ("그들은 집에 가지 않았다.", "Yes, they did는 긍정의 답이므로"), ("그들은 집에 간다.", "did는 현재가 아니라 과거이므로"),
      ("그들은 집에 가지 않는다.", "did는 과거이고 긍정이므로"), ("그들은 집에 갈 것이다.", "did는 미래가 아니라 과거이므로")], 1)
f134("E", "A: Jane can swim, can't she?\nB: <u>No, she can't</u>.",
     [("Jane은 수영을 할 수 있다.", "No, she can't는 부정의 답이므로"), ("Jane은 수영을 했다.", "can't는 ‘할 수 없다’는 능력의 부정이므로"), ("Jane은 수영을 할 수 없다.", "No, she can't는 능력의 부정(할 수 없다)이므로"),
      ("Jane은 수영을 하지 않았다.", "can't는 과거의 행동이 아니라 능력의 부정이므로"), ("Jane은 수영을 할 것이다.", "can't는 미래가 아니라 능력의 부정이므로")], 3)
f134("F", "A: You are ready, aren't you?\nB: <u>Yes, I am</u>.",
     [("나는 준비가 되어 있지 않다.", "Yes, I am은 긍정의 답이므로"), ("나는 준비가 되어 있었다.", "am은 과거가 아니라 현재이므로"), ("나는 준비가 되어 있지 않았다.", "am은 현재이고 긍정이므로"),
      ("나는 준비가 될 것이다.", "am은 미래가 아니라 현재이므로"), ("나는 준비가 되어 있다.", "Yes, I am은 현재의 긍정(준비되어 있다)이므로")], 5)

# 3-135 감탄문 구조: 원문항 발문, 유형마다 다섯 문장을 새로(도치형 오답 제외)
ST135 = "다음 중 감탄문의 문장 구조가 어법상 옳은 것은?"
R135 = "감탄문은 What + (a/an) + 형용사 + 명사 + 주어 + 동사!, How + 형용사/부사 + 주어 + 동사!이다. 복수명사 앞에는 a/an을 쓰지 않고, How 바로 뒤에는 a/an + 명사를 쓰지 않는다."
S135 = "발문에 ‘주어와 동사는 평서문처럼 주어+동사 순서로’라는 조건이 붙어 어순을 알려 주었고, 오답 네 개가 B와 똑같았다. 원문항 발문으로 되돌리고 유형마다 다섯 문장을 새로 썼다(조건이 없으면 논란이 될 수 있는 도치형 오답은 뺐다)."
def f135(t, items, a, s=S135):
    mk(3, 135, t, items, a, R135, s, st=ST135)
f135("B", [("What a kind people they are!", "복수명사 people 앞에는 a를 쓰지 않으므로"), ("How kind your parents are!", "How + 형용사 + 주어 + 동사의 어순이므로"), ("What kind your parents are!", "명사 없이 형용사만 오면 What이 아니라 How를 쓰므로"),
           ("How a kind man he is!", "How 뒤에 a + 형용사 + 명사를 쓸 수 없으므로"), ("What kind man he is!", "단수명사 man 앞에 a가 빠졌으므로")], 2,
     "정답(What smart students they are!)이 원문항과 똑같았고 발문이 어순을 알려 주었다. 원문항 발문으로 되돌리고 다섯 문장을 새로 썼다.")
f135("C", [("What an old castle it is!", "What + an + 형용사 + 명사 + 주어 + 동사의 어순이므로"), ("How old castle it is!", "How 뒤에 형용사 + 명사를 쓸 수 없으므로"), ("What old the castle is!", "명사 없이 형용사만 오면 How를 쓰므로"),
           ("How an old castle it is!", "How 뒤에 an + 형용사 + 명사를 쓸 수 없으므로"), ("What a old castle it is!", "모음 소리로 시작하는 old 앞에는 an을 쓰므로")], 1)
f135("D", [("How a exciting game it was!", "How 뒤에 a + 형용사 + 명사를 쓸 수 없으므로"), ("What exciting the game was!", "명사 없이 형용사만 오면 How를 쓰므로"), ("What exciting game it was!", "단수명사 game 앞에 an이 빠졌으므로"),
           ("What an exciting game it was!", "What + an + 형용사 + 명사 + 주어 + 동사의 어순이므로"), ("How exciting game it was!", "How 뒤에 형용사 + 명사를 쓸 수 없으므로")], 4)
f135("E", [("How a fast runner she is!", "How 뒤에 a + 형용사 + 명사를 쓸 수 없으므로"), ("What fast she runs!", "명사 없이 부사만 오면 How를 쓰므로"), ("How fast she runs!", "How + 부사 + 주어 + 동사의 어순이므로"),
           ("What a fast she runs!", "a 뒤에 명사가 없고 부사 앞에는 How를 쓰므로"), ("How fastly she runs!", "fast는 -ly 없이 부사로 쓰므로")], 3)
f135("F", [("What a delicious cookies these are!", "복수명사 cookies 앞에는 a를 쓰지 않으므로"), ("How delicious cookies these are!", "How 뒤에 형용사 + 명사를 쓸 수 없으므로"), ("What delicious these cookies are!", "명사 없이 형용사만 오면 How를 쓰므로"),
           ("How a delicious cookie this is!", "How 뒤에 a + 형용사 + 명사를 쓸 수 없으므로"), ("What delicious cookies these are!", "What + 형용사 + 복수명사 + 주어 + 동사의 어순이므로")], 5)

# 3-136 부가의문문: 원문항 발문, B는 문장을 새로
ST136 = "다음 문장의 빈칸에 들어갈 알맞은 부가의문문을 고르시오."
R136 = "부가의문문은 앞 문장이 긍정이면 부정, 부정이면 긍정으로 쓰고, 앞 문장의 동사(be동사·조동사·do/does/did)와 시제에 맞추며 주어는 대명사로 받는다."
S136 = "발문의 ‘(긍정 진술에는 부정형, 부정 진술에는 긍정형을 붙일 것.)’이 부가의문문 규칙을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
mk(3, 136, "B", [("doesn't he", "긍정문의 일반동사 plays(3인칭 단수 현재)에 맞춰 doesn't he로 쓰므로"), ("does he", "긍정문 뒤에는 부정의 부가의문문을 쓰므로"), ("isn't he", "일반동사 문장이라 be동사로 받을 수 없으므로"),
                 ("didn't he", "현재 시제 plays이므로 과거형 didn't를 쓰지 않으므로"), ("don't he", "3인칭 단수 주어에는 doesn't를 쓰므로")], 1, R136,
   "제시문과 정답(doesn't she)이 원문항과 똑같았고 발문이 규칙을 알려 주었다. 제시문을 새로 쓰고 원문항 발문으로 되돌렸다.", st=ST136, p="Your brother plays soccer well, ______?", okdup=True)
for t in "CDEF": F(3, 136, t, st=ST136, s=S136)

# 3-137 How about -ing → Shall we: 원문항 형식(화살표 빈칸 + (Shall we))
ST137 = "다음 문장을 괄호 안의 표현을 사용하여 바꾼 것으로 옳은 것을 고르시오."
ARW = "\n→__________________________________ (Shall we)"
S137 = "원문항의 ‘→ ____ (Shall we)’ 제시가 발문 속 설명으로 바뀌었다. 원문항 발문과 형식(화살표 아래 빈칸, 괄호 (Shall we))으로 되돌렸다. 보기와 정답은 그대로다."
mk(3, 137, "B", [("Shall we riding bikes to school?", "Shall we 뒤에는 동명사가 아니라 동사원형을 쓰므로"), ("Shall we to ride bikes to school?", "Shall we 뒤에 to부정사를 쓰지 않으므로"), ("Shall ride we bikes to school?", "Shall + we + 동사원형의 어순이 아니므로"),
                 ("Shall we rode bikes to school?", "Shall we 뒤에 과거형을 쓰지 않으므로"), ("Shall we ride bikes to school?", "Shall we + 동사원형으로 바르게 바꿨으므로")], 5,
   "How about + 동명사로 한 제안은 Shall we + 동사원형 ~?으로 바꿀 수 있다.", "문장과 선택지 세 개가 원문항과 똑같았다. 문장을 새로 쓰고 원문항 발문과 형식으로 되돌렸다.",
   st=ST137, p="How about riding bikes to school?" + ARW)
for t in "CDEF": F(3, 137, t, st=ST137, p=V(3, 137, t)["passage"] + ARW, s=S137)

# 3-138 감탄문 영작: 원문항 발문, 도치형 오답을 다른 오류로
ST138 = "다음 우리말 문장을 올바르게 영작한 것을 고르시오."
R138 = "감탄문은 What + (a/an) + 형용사 + 명사 + 주어 + 동사!, How + 형용사/부사 + 주어 + 동사!이다."
S138 = "발문에 ‘주어와 동사는 평서문처럼 주어+동사 순서로’라는 조건이 붙어 어순을 알려 주었다. 원문항 발문으로 되돌리고, 조건이 없으면 논란이 될 수 있는 도치형 오답은 다른 오류로 바꿨다."
def f138(t, items, a, s=S138, **kw):
    mk(3, 138, t, items, a, R138, s, st=ST138, **kw)
f138("B", [("What nice car it is!", "단수명사 car 앞에 a가 빠졌으므로"), ("How a nice car it is!", "How 뒤에 a + 형용사 + 명사를 쓸 수 없으므로"), ("What a nice car it is!", "What + a + 형용사 + 명사 + 주어 + 동사의 어순이므로"),
           ("What a car nice it is!", "형용사는 명사 앞에 오므로"), ("How nice car it is!", "How 뒤에 형용사 + 명사를 쓸 수 없으므로")], 3,
     "우리말과 정답이 원문항과 똑같았고 발문이 어순을 알려 주었다. 우리말을 ‘얼마나 멋진 차인가!’로 바꾸고 원문항 발문으로 되돌렸다.", p="얼마나 멋진 차인가!")
f138("C", [("What a smart students they are!", "복수명사 students 앞에는 a를 쓰지 않으므로"), ("How smart students they are!", "How 뒤에 형용사 + 명사를 쓸 수 없으므로"), ("What smart students they are!", "What + 형용사 + 복수명사 + 주어 + 동사의 어순이므로"),
           ("What smart they students are!", "형용사 뒤에 명사가 바로 와야 하므로"), ("How a smart students they are!", "How 뒤에 a + 형용사 + 명사를 쓸 수 없으므로")], 3)
f138("E", [("What fast Tom runs!", "명사 없이 부사만 오면 How를 쓰므로"), ("What Tom runs fast!", "What 뒤에 주어가 바로 올 수 없으므로"), ("How a fast Tom runs!", "How 뒤에 a를 쓸 수 없으므로"),
           ("How fast Tom runs!", "How + 부사 + 주어 + 동사의 어순이므로"), ("How fastly Tom runs!", "fast는 -ly 없이 부사로 쓰므로")], 4)
f138("F", [("What a interesting book it is!", "모음 소리로 시작하는 interesting 앞에는 an을 쓰므로"), ("What interesting an book it is!", "an은 형용사 앞에 오므로"), ("How interesting book it is!", "How 뒤에 형용사 + 명사를 쓸 수 없으므로"),
           ("How an interesting book it is!", "How 뒤에 an + 형용사 + 명사를 쓸 수 없으므로"), ("What an interesting book it is!", "What + an + 형용사 + 명사 + 주어 + 동사의 어순이므로")], 5)

# 3-139 명령문 + and/or 설명: 원문항 형식(짧은 글 속 ⓐ 밑줄), 그럴듯한 오개념 오답
ST139 = "다음 지문의 밑줄 친 ⓐ에 대한 한국어 문법 설명으로 가장 적절한 것은?"
R139 = "명령문 + and는 ‘~해라, 그러면 …할 것이다’(If you ~), 명령문 + or는 ‘~해라, 그렇지 않으면 …할 것이다’(If you don't ~)의 뜻이다. 명령문은 주어 You를 생략하고 동사원형으로 시작한다."
S139 = "원문항은 글 속 밑줄 친 문장에 대한 그럴듯한 설명을 판별하는데, 변형은 글 없이 한 문장만 주었고 오답(‘명령문에는 접속사를 사용할 수 없다’ 등)이 뻔하며 유형마다 반복되었다. 원문항 발문과 형식(짧은 글 속 ⓐ 밑줄)으로 되돌리고, 원문항처럼 그럴듯한 오개념으로 오답을 새로 썼다."
def f139(t, p, items, a, s=S139):
    mk(3, 139, t, items, a, R139, s, st=ST139, p=p)
f139("B", "Tomorrow is our math test. My mom said, \"ⓐ<u>Go to bed early, or you will be tired during the test</u>.\" So I turned off my phone and went to bed.",
     [("ⓐ는 '~해라, 그러면 ~할 것이다'라는 뜻으로, 일찍 자면 피곤해질 것이라는 의미이다.", "or는 ‘그렇지 않으면’이라 일찍 자지 않으면 피곤할 것이라는 뜻이므로"),
      ("ⓐ는 명령문 뒤에 'or'가 와서 '일찍 자지 않으면 시험 중에 피곤할 것이다'라는 뜻을 나타낸다.", "명령문 + or의 뜻을 바르게 설명했으므로"),
      ("ⓐ를 'If'를 사용한 문장으로 바꾸면 'If you go to bed early, you will be tired during the test.'가 된다.", "명령문 + or는 If you don't ~로 바꿔야 하므로"),
      ("ⓐ의 'or'는 '또는'이라는 뜻으로 두 가지 중 하나를 고르라는 의미이다.", "명령문 뒤의 or는 ‘그렇지 않으면’이라는 뜻이므로"), ("ⓐ의 'Go'는 주어가 없으므로 'Going'으로 고쳐야 한다.", "명령문은 주어 없이 동사원형으로 시작하므로")], 2,
     "문장과 정답 설명이 원문항과 같았고 글과 밑줄이 빠졌으며 오답이 뻔했다. 원문항처럼 짧은 글 속 ⓐ 밑줄 문장을 명령문 + or로 새로 쓰고, 그럴듯한 오개념으로 오답을 새로 썼다.")
f139("C", "Our class will have a soccer game next week. Our coach told us, \"ⓐ<u>Practice every day, and you will win the game</u>.\" We are practicing hard now.",
     [("ⓐ의 'and'는 단순히 두 문장을 이어 주므로 생략해도 뜻이 같다.", "명령문 뒤의 and는 ‘그러면’의 뜻이라 생략할 수 없으므로"),
      ("ⓐ를 'If'를 사용한 문장으로 바꾸면 'If you don't practice every day, you will win the game.'이 된다.", "명령문 + and는 If you ~(긍정)로 바꿔야 하므로"),
      ("ⓐ는 '연습해라, 그렇지 않으면 질 것이다'라는 경고의 뜻이다.", "and는 ‘그러면’이라 경고가 아니라 조건의 결과를 나타내므로"), ("ⓐ의 'Practice'는 명사로 쓰여 '연습'이라는 뜻의 주어이다.", "Practice는 명령문을 이끄는 동사원형이므로"),
      ("ⓐ는 명령문 뒤에 'and'가 와서 '매일 연습하면 경기에서 이길 것이다'라는 뜻을 나타낸다.", "명령문 + and의 뜻을 바르게 설명했으므로")], 5)
f139("D", "It was raining hard this morning. Before I left home, Dad said, \"ⓐ<u>Take your umbrella, or you will get wet</u>.\" I took it with me.",
     [("ⓐ를 'If'를 사용한 문장으로 바꾸면 'If you don't take your umbrella, you will get wet.'이 된다.", "명령문 + or를 If you don't ~로 바르게 바꿨으므로"),
      ("ⓐ의 'or'는 '그러면'이라는 뜻이므로 우산을 가져가면 젖을 것이라는 의미이다.", "or는 ‘그렇지 않으면’이라는 뜻이므로"), ("ⓐ의 'Take'는 주어 'You'가 생략되었으므로 'Takes'로 고쳐야 한다.", "명령문은 동사원형으로 시작하므로"),
      ("ⓐ의 'or'를 'and'로 바꿔도 문장의 뜻이 같다.", "and로 바꾸면 ‘가져가면 젖을 것이다’가 되어 뜻이 반대가 되므로"), ("ⓐ는 과거의 일을 말하므로 'will get'을 'got'으로 고쳐야 한다.", "따옴표 안의 말은 그때 한 말 그대로라 will get이 옳으므로")], 1)
f139("E", "My sister wants to be healthy. The doctor told her, \"ⓐ<u>Eat more vegetables, and you will feel better</u>.\" Now she eats salad every day.",
     [("ⓐ는 '채소를 먹어라, 그렇지 않으면 몸이 나빠질 것이다'라는 경고의 뜻이다.", "and는 ‘그러면’이라 경고의 뜻이 아니므로"), ("ⓐ의 'and' 대신 'or'를 써도 같은 뜻이다.", "or로 바꾸면 ‘먹지 않으면’의 뜻이 되어 달라지므로"),
      ("ⓐ를 'If'를 사용한 문장으로 바꾸면 'If you eat more vegetables, you will feel better.'가 된다.", "명령문 + and를 If you ~로 바르게 바꿨으므로"), ("ⓐ의 'Eat'은 동명사 'Eating'으로 고쳐야 주어가 된다.", "Eat은 명령문을 이끄는 동사원형이므로"),
      ("ⓐ의 'you will feel better'는 명령문이므로 'feel better'로 고쳐야 한다.", "and 뒤는 명령문이 아니라 결과를 나타내는 평서문이므로")], 3)
f139("F", "We planned a trip to the beach. On the morning of the trip, my friend called me and said, \"ⓐ<u>Hurry up, or we will miss the train</u>.\" I ran to the station.",
     [("ⓐ의 'or'는 '또는'이라는 뜻으로 서두르거나 기차를 놓치거나 둘 중 하나라는 의미이다.", "명령문 뒤의 or는 ‘그렇지 않으면’이라는 뜻이므로"), ("ⓐ를 'If'를 사용한 문장으로 바꾸면 'If we hurry up, we will miss the train.'이 된다.", "명령문 + or는 부정의 If절로 바꿔야 하므로"),
      ("ⓐ의 'or'를 'and'로 바꾸면 '서두르면 기차를 놓칠 것이다'가 되어 같은 뜻이다.", "and로 바꾸면 뜻이 반대가 되어 같은 뜻이 아니므로"), ("ⓐ는 명령문 뒤에 'or'가 와서 '서두르지 않으면 기차를 놓칠 것이다'라는 뜻을 나타낸다.", "명령문 + or의 뜻을 바르게 설명했으므로"),
      ("ⓐ의 'Hurry up'은 과거의 일이므로 'Hurried up'으로 고쳐야 한다.", "명령문은 시제와 관계없이 동사원형으로 쓰므로")], 4)

# 3-140 부가의문문·제안·감탄문 세 빈칸: 원문항 발문과 표 머리, 유형마다 정답 조합을 새로
ST140 = "R"  # 고친 원문항 발문(빈칸 (A)~(C))
R140 = "Let's ~의 부가의문문은 shall we?, 명령문의 부가의문문은 will you?이다. 제안은 Why don't we + 동사원형 / How(What) about + -ing로 하고, 감탄문은 a/an + 명사 앞에 What, 형용사 앞에 How를 쓴다."
S140 = "오답 조합이 유형마다 같았고 원문항의 (A)(B)(C) 표 머리가 빠졌으며, 일부 유형은 정답 조합(shall - Why - What)이 원문항과 같았다. 원문항 발문과 표 머리로 되돌리고 유형마다 대화와 정답 조합을 새로 썼다."
HEAD = "\n(A)\t(B)\t(C)"
def f140(t, p, c, a, why, s=S140):
    mk(3, 140, t, [(x, slotnote(x, c[a-1], why, labs=("(A)", "(B)", "(C)"))) for x in c], a, R140, s, st=ST140, p=p + HEAD, okdup=True)
f140("B", "A: Let's go camping this weekend, (A)_____ we?\nB: Great! (B)_____ about bringing a tent?\nA: Good idea. (C)_____ exciting it will be!", ["shall - Why - What", "shall - How - How", "will - How - What", "shall - Why - Why", "don't - Why - How"], 2,
     ["Let's ~의 부가의문문은 shall we이다", "about + -ing로 제안하므로 How가 알맞다", "형용사 exciting 앞의 감탄문은 How이다"],
     "대화와 정답(shall - Why - What)이 원문항과 똑같았다. 대화를 새로 쓰고 원문항 발문과 표 머리로 되돌렸으며 정답 조합을 shall - How - How로 바꿨다.")
f140("C", "A: Please close the door, (A)_____ you?\nB: Sure. It's cold in here.\nA: (B)_____ don't we drink some hot tea?\nB: (C)_____ a great idea!", ["shall - Why - What", "will - Why - What", "will - How - How", "won't - What - What", "do - Why - How"], 2,
     ["명령문의 부가의문문은 will you이다", "don't we + 동사원형으로 제안하므로 Why가 알맞다", "a great idea(명사) 앞의 감탄문은 What이다"])
f140("D", "A: Let's clean the classroom, (A)_____ we?\nB: OK. (B)_____ don't we start with the windows?\nA: Good. (C)_____ clean they will look!", ["shall - Why - How", "shall - How - What", "will - Why - How", "do - What - How", "shall - Why - What"], 1,
     ["Let's ~의 부가의문문은 shall we이다", "don't we + 동사원형으로 제안하므로 Why가 알맞다", "형용사 clean 앞의 감탄문은 How이다"])
f140("E", "A: Pass me the salt, (A)_____ you?\nB: Here you are.\nA: Thanks. (B)_____ about adding some pepper, too?\nB: (C)_____ a good cook you are!", ["shall - How - What", "will - Why - How", "do - Why - What", "will - How - What", "will - How - How"], 4,
     ["명령문의 부가의문문은 will you이다", "about + -ing로 제안하므로 How가 알맞다", "a good cook(명사) 앞의 감탄문은 What이다"])
f140("F", "A: Let's take a walk, (A)_____ we?\nB: Sure. (B)_____ about going to the river?\nA: Great. (C)_____ beautiful the sunset is!", ["will - What - How", "shall - Why - How", "shall - What - What", "do - Why - How", "shall - What - How"], 5,
     ["Let's ~의 부가의문문은 shall we이다", "about + -ing로 제안할 때는 What(How)을 쓰고 Why는 쓰지 않는다", "형용사 beautiful 앞의 감탄문은 How이다"])

# ---- 2차 감수(2026-10) 추가 ----
# 3-135 E: 3-138 E(How fast Tom runs!)와 거의 같은 문장 → 다른 부사로
FIX.pop((3, 135, "E"), None)
f135("E", [("How a good singer she is!", "How 뒤에 a + 형용사 + 명사를 쓸 수 없으므로"), ("What well she sings!", "명사 없이 부사만 오면 How를 쓰므로"), ("How well she sings!", "How + 부사 + 주어 + 동사의 어순이므로"),
           ("What a well she sings!", "What a 뒤에는 형용사 + 명사가 와야 하므로"), ("How good she sings!", "동사 sings를 꾸미는 말은 형용사 good이 아니라 부사 well이므로")], 3,
     S135 + " 같은 유형의 3-138(How fast Tom runs!)과 문장이 겹치지 않게 부사를 well로 썼다.")

# 3-136 B~F: 형태가 틀린 꼬리말(don't he, isn't him 등) 오답 → 원문항처럼 모두 바른 꼴의 부가의문문으로
S136F = "발문의 ‘(긍정 진술에는 부정형, 부정 진술에는 긍정형을 붙일 것.)’이 부가의문문 규칙을 알려 주었고, 오답에 형태부터 틀린 말(isn't him, don't he 등)이 있어 규칙을 몰라도 지워졌다. 원문항 발문으로 되돌리고, 오답을 원문항처럼 꼴은 바르지만 긍정·부정이나 동사·시제가 맞지 않는 부가의문문으로 바꿨다."
def f136(t, items, a, s=S136F, **kw):
    FIX.pop((3, 136, t), None)
    mk(3, 136, t, items, a, R136, s, st=ST136, **kw)
f136("B", [("doesn't he", "긍정문의 일반동사 plays(3인칭 단수 현재)에 맞춰 doesn't he로 쓰므로"), ("does he", "긍정문 뒤에는 부정의 부가의문문을 쓰므로"), ("isn't he", "일반동사 문장이라 be동사로 받을 수 없으므로"),
           ("didn't he", "현재 시제 plays를 과거 did로 받을 수 없으므로"), ("is he", "일반동사 문장이라 be동사로 받을 수 없고 긍정형이기도 하므로")], 1,
     "제시문과 정답(doesn't she)이 원문항과 똑같았고 발문이 규칙을 알려 주었다. 제시문을 새로 쓰고 원문항 발문으로 되돌렸으며, 오답은 모두 꼴이 바른 부가의문문으로 썼다.", p="Your brother plays soccer well, ______?", okdup=True)
f136("C", [("doesn't he", "be동사 문장이라 does로 받을 수 없으므로"), ("isn't he", "긍정문의 be동사 is에 맞춰 isn't he로 쓰므로"), ("is he", "긍정문 뒤에는 부정의 부가의문문을 쓰므로"),
           ("wasn't he", "현재 시제 is를 과거 was로 받을 수 없으므로"), ("does he", "be동사 문장이라 does로 받을 수 없고 긍정형이기도 하므로")], 2)
f136("D", [("did they", "긍정문 뒤에는 부정의 부가의문문을 쓰므로"), ("don't they", "과거 시제 went를 현재 do로 받을 수 없으므로"), ("weren't they", "일반동사 문장이라 be동사로 받을 수 없으므로"),
           ("aren't they", "일반동사 문장이라 be동사로 받을 수 없으므로"), ("didn't they", "긍정문의 일반동사 과거형 went에 맞춰 didn't they로 쓰므로")], 5)
f136("E", [("can she", "긍정문 뒤에는 부정의 부가의문문을 쓰므로"), ("doesn't she", "조동사 can이 있는 문장은 can으로 받으므로"), ("can't she", "긍정문의 조동사 can에 맞춰 can't she로 쓰므로"),
           ("isn't she", "조동사 can이 있는 문장을 be동사로 받을 수 없으므로"), ("does she", "조동사 can이 있는 문장은 can으로 받고, 긍정형이기도 하므로")], 3)
f136("F", [("are you", "부정문의 be동사 aren't에 맞춰 긍정 are you로 쓰므로"), ("aren't you", "부정문 뒤에는 긍정의 부가의문문을 쓰므로"), ("do you", "be동사 문장이라 do로 받을 수 없으므로"),
           ("don't you", "be동사 문장이라 do로 받을 수 없고 부정형이기도 하므로"), ("were you", "현재 시제 aren't를 과거 were로 받을 수 없으므로")], 1)

# 3-137 C~F: Shall we로 시작하지 않는 오답(Do we ~?)은 발문만 보고 지워짐 → Shall we + 틀린 동사 형태로
S137F = "원문항의 ‘→ ____ (Shall we)’ 제시가 발문 속 설명으로 바뀌었고, 오답 하나(Do we ~?)는 Shall we를 쓰지 않아 괄호 안의 표현만 보고 지워졌다. 원문항 발문과 형식(화살표 아래 빈칸, 괄호 (Shall we))으로 되돌리고, 그 오답을 원문항처럼 Shall we 뒤의 동사 형태가 틀린 문장으로 바꿨다."
def f137(t, obj, base, ing, bad, badwhy, order):
    FIX.pop((3, 137, t), None)
    its = {"ok": (f"Shall we {base} {obj}?", "Shall we + 동사원형으로 바르게 바꿨으므로"), "ing": (f"Shall we {ing} {obj}?", "Shall we 뒤에는 동명사가 아니라 동사원형을 쓰므로"),
           "to": (f"Shall we to {base} {obj}?", "Shall we 뒤에 to부정사를 쓰지 않으므로"), "inv": (f"Shall {base} we {obj}?", "Shall + we + 동사원형의 어순이 아니므로"), "bad": (f"Shall we {bad} {obj}?", badwhy)}
    mk(3, 137, t, [its[k] for k in order], order.index("ok") + 1, "How about + -ing?는 Shall we + 동사원형 ~?으로 바꿔 쓸 수 있다.", S137F, st=ST137, p=V(3, 137, t)["passage"] + ARW)
f137("C", "to the park", "go", "going", "went", "Shall we 뒤에 과거형을 쓸 수 없으므로", ["ing", "to", "ok", "inv", "bad"])
f137("D", "a movie", "watch", "watching", "watched", "Shall we 뒤에 과거형을 쓸 수 없으므로", ["inv", "ok", "to", "ing", "bad"])
f137("E", "a break", "take", "taking", "takes", "Shall we 뒤에 -s가 붙은 형태를 쓸 수 없으므로", ["ing", "to", "bad", "ok", "inv"])
f137("F", "tennis", "play", "playing", "played", "Shall we 뒤에 과거형을 쓸 수 없으므로", ["ok", "to", "inv", "bad", "ing"])

# 3-138 C: 정답 문장(What smart students they are!)이 원문항 3-135의 정답 문장과 같음 → 새 문장
FIX.pop((3, 138, "C"), None)
f138("C", [("What a brave boys they are!", "복수명사 boys 앞에는 a를 쓰지 않으므로"), ("How brave boys they are!", "How 뒤에 형용사 + 명사를 쓸 수 없으므로"), ("What brave boys they are!", "What + 형용사 + 복수명사 + 주어 + 동사의 어순이므로"),
           ("What brave they boys are!", "명사 boys가 형용사 바로 뒤에 와야 하므로"), ("How a brave boys they are!", "How 뒤에 a + 형용사 + 명사를 쓸 수 없으므로")], 3,
     S138 + " 또 정답 문장(What smart students they are!)이 같은 단원 원문항 3-135의 정답 문장과 똑같아, 우리말을 ‘얼마나 용감한 소년들인가!’로 바꿨다.", p="얼마나 용감한 소년들인가!")
