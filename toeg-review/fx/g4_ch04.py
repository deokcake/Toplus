# 4급 CH4 과거시제 (31~40) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def slotnote(ch, good, why, labs=("첫째", "둘째", "셋째"), sep=" - "):
    xs = [x.strip() for x in ch.split(sep)]; gs = [x.strip() for x in good.split(sep)]
    if xs == gs: return "모든 빈칸에 알맞은 말을 골랐으므로"
    bits = [f"{labs[i]} 빈칸 {x}: {w}" for i, (x, g, w) in enumerate(zip(xs, gs, why)) if x != g]
    return ", ".join(bits) + ". 따라서"

# 4-31 C: 정답 문장을 원문항과 다르게
mk(4, 31, "C", [("Minsu cleaned his room.", "과거형 cleaned를 쓴 과거 시제 문장이므로"), ("We were late for school.", "be동사 과거형 were를 쓴 과거 시제 문장이므로"), ("My dad cooks dinner on weekends.", "현재형 cooks로 현재의 습관을 나타내 과거 시제가 아니므로"),
                ("She took a picture.", "불규칙 과거형 took을 쓴 과거 시제 문장이므로"), ("They left an hour ago.", "불규칙 과거형 left를 쓴 과거 시제 문장이므로")], 3,
   "과거 시제는 이미 끝난 일을 나타내며 동사의 과거형(-ed, 불규칙 과거형, was/were)을 쓴다. 현재형은 현재의 상태·습관을 나타낸다.",
   "정답(He plays tennis every weekend.)이 원문항과 똑같았다. 문장을 모두 새로 쓰고 정답을 My dad cooks dinner on weekends.로 바꿨다.")

# 4-32 동사의 알맞은 형태: 원문항 발문, 실제로 있는 형태의 오답
R432 = "과거를 나타내는 말(yesterday, last ~, ~ ago)이 있으면 동사의 과거형을 쓴다. eat - ate, go - went, buy - bought, see - saw, write - wrote는 불규칙 과거형이다."
S432 = "발문에 ‘과거형’이 붙어 시제를 알려 주었고, 오답(ateed, did ate 등)이 없는 형태라 쉽게 지워졌다. 원문항 발문으로 되돌리고 오답을 원문항처럼 현재형·동사원형·-ing형·will + 동사원형 같은 실제 형태로 바꿨다."
def f432(t, v, p, forms, past, a, s=S432):
    why = {forms[0]: "3인칭 단수 현재형이라 과거의 일과 맞지 않으므로", forms[1]: "동사원형(현재형)이라 과거의 일과 맞지 않으므로", forms[2]: "-ing형만으로는 동사 자리에 쓸 수 없으므로",
           forms[3]: "will + 동사원형은 미래라 과거의 일과 맞지 않으므로", past: "과거를 나타내는 말과 어울리는 불규칙 과거형이므로"}
    order = {"B": [forms[0], forms[1], past, forms[2], forms[3]], "C": [forms[0], forms[1], forms[2], past, forms[3]], "D": [forms[0], forms[1], forms[2], forms[3], past],
             "E": [past, forms[0], forms[1], forms[2], forms[3]], "F": [forms[0], past, forms[1], forms[2], forms[3]]}[t]
    mk(4, 32, t, [(x, f"{x}: " + why[x]) for x in order], order.index(past) + 1, R432, s, st=f"빈칸에 들어갈 동사 ‘{v}’의 알맞은 형태를 고르시오.", p=p, okdup=True)
f432("B", "eat", "They _____ lunch at noon yesterday.", ["eats", "eat", "eating", "will eat"], "ate", 3)
f432("C", "go", "My family _____ to the beach last summer.", ["goes", "go", "going", "will go"], "went", 4,
     "제시문과 정답이 원문항과 똑같았고 오답도 없는 형태였다. 제시문을 새로 쓰고 " + S432[S432.index("원문항 발문으로"):])
f432("D", "buy", "She _____ a new bag yesterday.", ["buys", "buy", "buying", "will buy"], "bought", 5)
f432("E", "see", "Tom _____ the movie last night.", ["sees", "see", "seeing", "will see"], "saw", 1)
f432("F", "write", "I _____ a letter to my grandma two days ago.", ["writes", "write", "writing", "will write"], "wrote", 2)

# 4-33 과거 부정문: 원문항 발문, C는 문장을 새로
S433 = "발문에 ‘시점과 나머지 내용을 유지하면서 과거시제 부정문으로’ 조건이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
for t in "BDEF": F(4, 33, t, st="R", s=S433)
mk(4, 33, "C", [("Minho not caught a big fish at the lake.", "일반동사 과거 부정은 did not + 동사원형으로 만들므로"), ("Minho didn't caught a big fish at the lake.", "didn't 뒤에는 동사원형 catch를 쓰므로"), ("Minho was not catch a big fish at the lake.", "일반동사 부정에 was를 쓸 수 없으므로"),
                ("Minho did not catch a big fish at the lake.", "did not + 동사원형 catch로 바르게 바꿨으므로"), ("Minho does not catch a big fish at the lake.", "does not은 현재 부정이라 과거의 일과 맞지 않으므로")], 4,
   "일반동사 과거형의 부정문은 did not(didn't) + 동사원형이다. caught는 부정문에서 catch로 돌아간다.",
   "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘Minho caught a big fish at the lake.’로 바꾸고 원문항 발문으로 되돌렸다.", st="R", p="Minho caught a big fish at the lake.")

# 4-34 틀린 문장: 원문항 발문, 괄호 동사원형 삭제, 짝 없이 유형마다 새로
R434 = "불규칙 동사의 과거형은 따로 익힌다: write - wrote, hear - heard, go - went, buy - bought, see - saw, make - made, swim - swam, drive - drove, fly - flew."
S434 = "선택지마다 괄호로 동사원형을 붙였고, 정답 문장과 같은 문장의 옳은 형태가 함께 있어 대비 단서가 되었으며 오답이 유형마다 같았다. 원문항 발문으로 되돌리고 괄호를 뺐으며 짝 문장 없이 유형마다 새로 썼다."
def OKP(p): return f"불규칙 과거형({p})을 바르게 썼으므로"
def f434(t, items, a, s=S434):
    mk(4, 34, t, items, a, R434, s, st="R")
f434("B", [("I writed a letter.", "write의 과거형은 wrote이므로"), ("Tom went home.", OKP("went")), ("Jane bought a bag.", OKP("bought")), ("They saw the movie.", OKP("saw")), ("We met at the library.", OKP("met"))], 1,
     "발문이 바뀌고 선택지마다 괄호로 동사원형을 붙였다. 원문항 발문으로 되돌리고 괄호를 뺐다.")
f434("C", [("Mom made a cake.", OKP("made")), ("He sent me an email.", OKP("sent")), ("I heared a strange sound.", "hear의 과거형은 heard이므로"), ("The kids swam in the river.", OKP("swam")), ("She told me a story.", OKP("told"))], 3,
     S434 + " 정답(We meeted at the cafe.)이 원문항과 같아 새로 썼다.")
f434("D", [("Tom goed home early.", "go의 과거형은 went이므로"), ("We ate pizza for dinner.", OKP("ate")), ("They sang a song together.", OKP("sang")), ("He found his key.", OKP("found")), ("I drank some juice.", OKP("drank"))], 1)
f434("E", [("My dad drove to work.", OKP("drove")), ("Jane buyed a new dress.", "buy의 과거형은 bought이므로"), ("The bird flew away.", OKP("flew")), ("We sat on the bench.", OKP("sat")), ("He wore a blue cap.", OKP("wore"))], 2)
f434("F", [("I lost my umbrella.", OKP("lost")), ("The baby slept well.", OKP("slept")), ("She gave me a pen.", OKP("gave")), ("We took the bus.", OKP("took")), ("They seed a rainbow.", "see의 과거형은 saw이므로")], 5)

# 4-35 옳은 문장으로만 짝: 원문항 형식(ⓐ~ⓓ, 밑줄, 옳은 두 개의 짝), 정답 조합 다양화
ST435 = "다음 중 밑줄 친 부분이 어법상 옳은 문장으로만 짝지어진 것은?"
R435 = "규칙 과거형은 -ed를 붙이되, 자음 + y는 y를 i로 바꾸고(cry → cried), 단모음 + 단자음은 자음을 겹쳐 쓴다(stop → stopped, plan → planned). 불규칙 과거형(go → went, buy → bought)을 따로 익히고, Did 의문문에는 동사원형을 쓴다."
S435 = "원문항의 밑줄이 사라지고 기호 ⓐ~ⓓ가 a~d로 바뀌어 한 줄로 이어졌으며 ‘해당 없음’ 선택지가 들어갔고, 정답이 유형마다 같았다(a, c). 원문항 발문과 형식(ⓐ~ⓓ 줄바꿈, 밑줄, 옳은 두 개의 짝)으로 되돌리고 유형마다 정답 조합을 달리했으며, 서너 낱말뿐이던 문장도 원문항 길이에 가깝게 늘렸다."
CH435 = ["ⓐ, ⓑ", "ⓐ, ⓒ", "ⓑ, ⓒ", "ⓑ, ⓓ", "ⓒ, ⓓ"]
def f435(t, lines, judge, ok, s=S435):
    a = CH435.index(ok) + 1
    F(4, 35, t, st=ST435, p="\n".join(lines), c=CH435, a=a, r=R435, pre=["문장별 판정: " + j for j in judge], k=f"밑줄 친 부분이 옳은 문장은 {ok}이다.", n=setnotes(CH435, ok, "옳은 문장"), okdup=True, s=s + ipos(a))
f435("B", ["ⓐ He <u>made</u> a big box for his dog.", "ⓑ Jane <u>cryed</u> a lot after the movie.", "ⓒ We <u>cleaned</u> the room before dinner.", "ⓓ They <u>goed</u> out to play soccer."],
     ["ⓐ O. make의 불규칙 과거형 made이다.", "ⓑ X. 자음 + y는 y를 i로 바꿔 cried로 쓴다.", "ⓒ O. clean에 -ed를 붙였다.", "ⓓ X. go의 과거형은 went이다."], "ⓐ, ⓒ")
f435("C", ["ⓐ Did you <u>went</u> to the zoo last weekend?", "ⓑ I <u>planned</u> a trip with my family.", "ⓒ Tom <u>hurryed</u> to school this morning.", "ⓓ We <u>played</u> soccer in the park yesterday."],
     ["ⓐ X. Did 뒤에는 동사원형 go를 쓴다.", "ⓑ O. plan은 n을 겹쳐 쓰고 -ed를 붙인다.", "ⓒ X. 자음 + y는 y를 i로 바꿔 hurried로 쓴다.", "ⓓ O. 모음 + y는 그대로 -ed를 붙인다."], "ⓑ, ⓓ",
     "ⓐ·ⓑ가 원문항 문장과 같았고 정답 조합(ⓐ, ⓓ)도 같았으며 기호·밑줄도 원본과 달랐다. 문장을 새로 쓰고 원문항 형식으로 되돌렸다.")
f435("D", ["ⓐ Tom <u>buyed</u> a new bike last month.", "ⓑ They <u>stoped</u> the car in front of the bank.", "ⓒ Jane <u>studied</u> English for the test.", "ⓓ Did they <u>visit</u> Seoul last summer?"],
     ["ⓐ X. buy의 과거형은 bought이다.", "ⓑ X. stop은 p를 겹쳐 stopped로 쓴다.", "ⓒ O. 자음 + y는 y를 i로 바꿔 studied로 쓴다.", "ⓓ O. Did 뒤에 동사원형 visit을 썼다."], "ⓒ, ⓓ")
f435("E", ["ⓐ I <u>saw</u> a funny movie with my friends.", "ⓑ They <u>dropped</u> the ball on the floor.", "ⓒ She <u>carryed</u> a heavy bag to school.", "ⓓ Did Tom <u>wrote</u> a letter to his grandma?"],
     ["ⓐ O. see의 불규칙 과거형 saw이다.", "ⓑ O. drop은 p를 겹쳐 dropped로 쓴다.", "ⓒ X. 자음 + y는 y를 i로 바꿔 carried로 쓴다.", "ⓓ X. Did 뒤에는 동사원형 write를 쓴다."], "ⓐ, ⓑ")
f435("F", ["ⓐ I <u>buyed</u> a book at the bookstore.", "ⓑ Tom <u>ate</u> lunch with his classmates.", "ⓒ Did you <u>enjoy</u> the party last night?", "ⓓ We <u>runned</u> to the bus stop."],
     ["ⓐ X. buy의 과거형은 bought이다.", "ⓑ O. eat의 불규칙 과거형 ate이다.", "ⓒ O. Did 뒤에 동사원형 enjoy를 썼다.", "ⓓ X. run의 과거형은 ran이다."], "ⓑ, ⓒ")

# 4-36 C: 원문항과 같던 문장을 새로
mk(4, 36, "C", [("were", "과거(an hour ago)이고 뒤의 명사 two cats가 복수라 were를 쓰므로"), ("is", "현재형이라 과거의 일과 맞지 않으므로"), ("was", "뒤의 명사 two cats가 복수라 was를 쓸 수 없으므로"), ("are", "현재형이라 과거의 일과 맞지 않으므로"), ("be", "동사원형은 There 뒤 동사 자리에 쓸 수 없으므로")], 1,
   "There + be동사 구문에서 be동사는 뒤의 명사에 맞춘다. 과거에는 단수 명사 앞에 was, 복수 명사 앞에 were를 쓴다.", "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘There ___ two cats on the roof an hour ago.’로 바꿨다.",
   p="There ________ two cats on the roof an hour ago.", okdup=True)

# 4-37 현재형·과거형 짝: 원문항 발문, C는 문장을 새로
S437 = "발문이 ‘첫 문장은 현재의 반복 행동, 둘째 문장은 과거 행동’이라고 시제를 알려 주었다. 원문항 발문으로 되돌렸다. 문장 속 every ~와 yesterday·last night로 시제를 판단할 수 있다. 보기와 정답은 그대로다."
for t in "BDEF": F(4, 37, t, st="R", s=S437)
c437 = ["practices - practicing", "practices - practiced", "practiced - practiced", "practice - practiced", "practices - practices"]
mk(4, 37, "C", [(x, slotnote(x, c437[1], ["every morning(반복)이고 3인칭 단수 주어라 practices를 쓴다", "last night(과거)라 practiced를 쓴다"])) for x in c437], 2,
   "every ~는 현재의 반복을, yesterday·last night는 과거를 나타낸다. 3인칭 단수 주어의 현재형에는 -s/-es를 붙이고, 과거형은 주어와 관계없이 -ed형을 쓴다.",
   "제시문과 정답(plays - played)이 원문항과 똑같았고 발문이 시제를 알려 주었다. 문장을 새로 쓰고 원문항 발문으로 되돌렸다.", st="R",
   p="Mina ________ the piano every morning.\nMina ________ the piano last night.", okdup=True)

# 4-38 틀린 문장: 짝 없이 유형마다 새로
R438 = "과거를 나타내는 말(yesterday, last ~, ago)이 있으면 동사의 과거형을 쓴다. 과거형은 주어와 관계없이 같은 형태이며 -s를 붙이지 않는다."
S438 = "정답 문장과 같은 문장의 옳은 과거형이 함께 있어 대비 단서가 되었고 오답 네 개가 유형마다 같았다. 짝 문장 없이 유형마다 새로 썼다."
def OKT(p): return f"과거형 {p}를 바르게 썼으므로"
def f438(t, items, a, s=S438):
    mk(4, 38, t, items, a, R438, s)
f438("B", [("Jane bought a bag last week.", "과거형 bought를 바르게 썼으므로"), ("The kids ran to the playground.", "과거형 ran을 바르게 썼으므로"), ("We eat pizza last night.", "last night(과거)에는 과거형 ate를 써야 하므로"),
           ("Tom went home early.", "과거형 went를 바르게 썼으므로"), ("They saw a movie yesterday.", "과거형 saw를 바르게 썼으므로")], 3,
     "정답(She run to her teacher yesterday.)이 원문항과 똑같았고 옳은 짝 문장이 함께 있었다. 문장을 새로 쓰고 짝 문장을 없앴다.")
f438("C", [("She caught a cold last week.", "과거형 caught를 바르게 썼으므로"), ("My uncle came to visit us.", "과거형 came을 바르게 썼으므로"), ("We swam in the lake.", "과거형 swam을 바르게 썼으므로"),
           ("He sold his old car.", "과거형 sold를 바르게 썼으므로"), ("I leave home at seven yesterday.", "yesterday(과거)에는 과거형 left를 써야 하므로")], 5)
f438("D", [("They sees a movie yesterday.", "yesterday(과거)에는 과거형 saw를 써야 하므로"), ("I brought my lunch.", "과거형 brought를 바르게 썼으므로"), ("The dog bit my shoe.", "과거형 bit을 바르게 썼으므로"),
           ("She wrote a poem.", "과거형 wrote를 바르게 썼으므로"), ("Dad fixed the door.", "과거형 fixed를 바르게 썼으므로")], 1)
f438("E", [("The train arrived on time.", "과거형 arrived를 바르게 썼으므로"), ("Jane buy a bag last week.", "last week(과거)에는 과거형 bought를 써야 하므로"), ("We built a sandcastle.", "과거형 built를 바르게 썼으므로"),
           ("He felt tired after school.", "과거형 felt를 바르게 썼으므로"), ("I read the book twice.", "과거형 read(발음 [red])를 바르게 썼으므로")], 2)
f438("F", [("They won the game.", "과거형 won을 바르게 썼으므로"), ("She spent all her money.", "과거형 spent를 바르게 썼으므로"), ("Tom broke the window.", "과거형 broke를 바르게 썼으므로"),
           ("We eats lunch at noon yesterday.", "yesterday(과거)에는 과거형 ate를 써야 하므로"), ("I understood the question.", "과거형 understood를 바르게 썼으므로")], 4)

# 4-39 cannot help -ing = cannot but + 동사원형: 원문항 발문, 뜻이 다른 표현의 오답
R439 = "cannot help + 동명사는 ‘~하지 않을 수 없다’라는 뜻이며 cannot but + 동사원형과 같은 뜻이다. don't need to(~할 필요가 없다), shouldn't(~하면 안 된다), not ~ at all(전혀 ~않다)과 구별한다."
S439 = "발문이 ‘cannot but + 동사원형으로’라고 정답 구조를 알려 주었고, 오답도 형태 오류 위주로 바뀌었다. 원문항 발문으로 되돌리고 오답을 원문항처럼 뜻이 다른 표현으로 바꿨다."
SAME = "cannot but + 동사원형으로 ‘~하지 않을 수 없다’는 같은 뜻을 나타내므로"
def f439(t, p, items, a, s=S439):
    mk(4, 39, t, items, a, R439, s, st="R", p=p)
f439("B", "Tom cannot help thinking about the game.", [("Tom doesn't need to think about the game.", "‘생각할 필요가 없다’는 뜻이라 다르므로"), ("Tom shouldn't think about the game.", "‘생각하면 안 된다’는 뜻이라 다르므로"),
     ("Tom cannot but think about the game.", SAME), ("Tom doesn't think about the game at all.", "‘전혀 생각하지 않는다’는 뜻이라 반대이므로"), ("Tom can help me think about the game.", "‘내가 생각하는 것을 도울 수 있다’는 뜻이라 다르므로")], 3)
f439("C", "Mina cannot help crying at sad movies.", [("Mina cannot but cry at sad movies.", SAME), ("Mina doesn't have to cry at sad movies.", "‘울 필요가 없다’는 뜻이라 다르므로"), ("Mina never cries at sad movies.", "‘결코 울지 않는다’는 뜻이라 반대이므로"),
     ("Mina shouldn't cry at sad movies.", "‘울면 안 된다’는 뜻이라 다르므로"), ("Mina can help you cry at sad movies.", "‘네가 우는 것을 도울 수 있다’는 뜻이라 다르므로")], 1,
     "제시문과 정답이 원문항과 똑같았고 발문이 정답 구조를 알려 주었다. 제시문을 새로 쓰고 " + S439[S439.index("원문항 발문으로"):])
f439("D", "She cannot help smiling at the baby.", [("She doesn't want to smile at the baby.", "‘웃고 싶지 않다’는 뜻이라 다르므로"), ("She cannot but smile at the baby.", SAME), ("She must not smile at the baby.", "‘웃으면 안 된다’는 뜻이라 다르므로"),
     ("She rarely smiles at the baby.", "‘거의 웃지 않는다’는 뜻이라 반대이므로"), ("She can help the baby smile.", "‘아기가 웃도록 도울 수 있다’는 뜻이라 다르므로")], 2)
f439("E", "We cannot help laughing at the joke.", [("We don't need to laugh at the joke.", "‘웃을 필요가 없다’는 뜻이라 다르므로"), ("We didn't laugh at the joke at all.", "‘전혀 웃지 않았다’는 뜻이라 반대이므로"), ("We shouldn't laugh at the joke.", "‘웃으면 안 된다’는 뜻이라 다르므로"),
     ("We cannot but laugh at the joke.", SAME), ("We can help him laugh at the joke.", "‘그가 웃도록 도울 수 있다’는 뜻이라 다르므로")], 4)
f439("F", "They cannot help talking about the news.", [("They don't want to talk about the news.", "‘말하고 싶지 않다’는 뜻이라 다르므로"), ("They mustn't talk about the news.", "‘말하면 안 된다’는 뜻이라 다르므로"), ("They hardly talk about the news.", "‘거의 말하지 않는다’는 뜻이라 반대이므로"),
     ("They can help us talk about the news.", "‘우리가 말하도록 도울 수 있다’는 뜻이라 다르므로"), ("They cannot but talk about the news.", SAME)], 5)

# 4-40 바르게 설명한 학생: 원문항 형식(짧은 글 + 이름 붙은 다섯 설명)
ST440 = "다음 지문을 읽고 과거 시제 표현에 대해 바르게 설명한 사람을 고르시오."
R440 = "과거형은 주어와 관계없이 형태가 같다. 규칙 과거형은 -ed를 붙이되 자음 + y는 y를 i로 바꾸고(study → studied), 단모음 + 단자음은 자음을 겹쳐 쓴다(stop → stopped). 불규칙 과거형(go → went, run → ran, sing → sang)은 따로 익힌다."
S440 = "원문항은 다섯 학생의 설명을 판별하는데, 변형은 정답 선택지에만 학생 이름이 붙어 이름만 보고 정답을 고를 수 있었고 오답이 유형마다 같았으며 짧은 글도 한 문장으로 줄었다. 원문항처럼 세 문장 글과 이름 붙은 다섯 설명으로 유형마다 새로 썼다."
OK440 = "과거형에 대해 바르게 설명했으므로"
def f440(t, p, items, a, s=S440):
    mk(4, 40, t, items, a, R440, s, st=ST440, p=p)
f440("B", "Jane had a big test today. She studied English last night. Then she went to bed early.",
     [("도윤: 'last night'이 있으니까 studied 대신 현재형 studies를 써야 해.", "last night은 과거라 과거형 studied가 맞으므로"), ("지아: study는 자음 + y로 끝나서 y를 i로 바꾸고 -ed를 붙여 studied가 됐어.", OK440),
      ("현우: went는 go에 -ed를 붙인 규칙 과거형이야.", "went는 go의 불규칙 과거형이므로"), ("소민: had는 have의 현재완료 형태야.", "had는 have의 과거형이므로"), ("태오: 주어가 She라서 과거형에도 -s를 붙여 studieds로 써야 해.", "과거형에는 -s를 붙이지 않으므로")], 2)
f440("C", "Last weekend was my mom's birthday. Dad bought flowers for her. We made a cake together.",
     [("수아: bought는 buy에 -ed를 붙인 형태라 buyed로도 쓸 수 있어.", "buy의 과거형은 불규칙 bought뿐이므로"), ("준호: 주어가 Dad라서 bought 뒤에 -s를 붙여야 해.", "과거형에는 -s를 붙이지 않으므로"),
      ("하린: was는 be동사의 과거형으로, 주어가 단수라서 were가 아니라 was를 썼어.", OK440), ("은우: made는 make의 현재형이라 과거를 말하려면 maked로 고쳐야 해.", "made는 make의 불규칙 과거형이므로"),
      ("시윤: Last weekend가 문장 앞에 있으면 동사는 모두 현재형으로 써야 해.", "Last weekend는 과거라 과거형을 쓰므로")], 3,
     "글(Mom bought vegetables)과 정답 설명이 원문항과 같았고 정답에만 이름이 붙었다. 원문항처럼 세 문장 글로 새로 쓰고 모든 선택지에 이름을 붙였다.")
f440("D", "Yesterday, Tom got up late. He missed the bus. So he ran to school.",
     [("서진: ran은 run의 불규칙 과거형이야.", OK440), ("예은: missed는 miss의 현재완료 형태야.", "missed는 miss의 과거형이므로"), ("민재: got은 get에 -ed를 붙여 만든 규칙 과거형이야.", "got은 get의 불규칙 과거형이므로"),
      ("가은: 주어가 He라서 과거형도 runs처럼 -s를 붙여야 해.", "과거형에는 -s를 붙이지 않으므로"), ("주원: Yesterday가 있으니 동사 앞에 will을 써야 해.", "Yesterday는 과거라 will(미래)을 쓰지 않으므로")], 1)
f440("E", "We went to the park after lunch. The traffic light turned red, so we stopped at the corner. Then we crossed the street.",
     [("지호: went는 go의 현재형이라 과거를 나타내려면 goed로 써야 해.", "went는 go의 불규칙 과거형이므로"), ("유나: crossed는 cross에 -s를 붙인 현재형이야.", "crossed는 -ed를 붙인 과거형이므로"),
      ("건우: 주어가 We라서 과거형은 stopeds처럼 써야 해.", "과거형에는 -s를 붙이지 않고 p를 겹쳐 stopped로 쓰므로"), ("채원: stop은 단모음 + 단자음으로 끝나서 p를 한 번 더 쓰고 -ed를 붙여 stopped가 됐어.", OK440),
      ("다인: turned는 turn의 현재진행 형태야.", "turned는 turn의 과거형이므로")], 4)
f440("F", "My friends and I went camping last summer. At night, we saw many stars. We sang songs by the fire.",
     [("하은: saw는 see에 -ed를 붙인 seed와 같은 뜻의 규칙 과거형이야.", "saw는 see의 불규칙 과거형이고 seed라는 과거형은 없으므로"), ("소율: last summer가 있으니 went 대신 will go를 써야 해.", "last summer는 과거라 과거형 went가 맞으므로"),
      ("우진: 주어가 여러 명이라서 과거형 sang에 -s를 붙여 sangs로 써야 해.", "과거형에는 -s를 붙이지 않으므로"), ("서아: went는 go의 현재완료 형태라고 불러.", "went는 go의 과거형이므로"),
      ("도현: sang은 sing의 불규칙 과거형이고 주어와 관계없이 형태가 같아.", OK440)], 5)


# ---- 2차 감수(2026-10) 추가 ----
# 4-31 B, D, E, F: 같은 문장의 현재형·과거형이 함께 있어(쌍둥이 문장) 정답이 둘로 좁혀짐 → 짝 문장을 없앰
R431 = "과거 시제는 이미 끝난 일을 나타내며 동사의 과거형(-ed, 불규칙 과거형, was/were)을 쓴다. 현재형은 현재의 상태·습관을 나타낸다."
S431 = "정답 문장(현재형)과 같은 문장의 과거형이 다른 보기에 함께 있어 둘만 견주면 답이 나왔다. 짝이 되는 문장을 다른 문장으로 바꾸고 문장 길이도 원문항에 가깝게 늘렸다."
def PA(v): return f"과거형({v})을 쓴 과거 시제 문장이므로"
def PR(v): return f"현재형({v})으로 현재의 습관을 나타내 과거 시제가 아니므로"
def f431(t, items, a):
    mk(4, 31, t, items, a, R431, S431, st="R")
f431("B", [("They played soccer after school.", PA("played")), ("He cleaned his room yesterday.", PA("cleaned")), ("We were tired last night.", PA("were")), ("Tom went to school by bus.", PA("went")), ("She studies English every day.", PR("studies"))], 5)
f431("D", [("Tom played soccer with his friends.", PA("played")), ("They go to school by bus.", PR("go")), ("We studied math last night.", PA("studied")), ("Jane was at home yesterday.", PA("was")), ("I met my uncle last week.", PA("met"))], 2)
f431("E", [("I read a book yesterday.", "yesterday가 있어 read는 과거형이므로"), ("They were busy last week.", PA("were")), ("Jane went home early.", PA("went")), ("Tom watches TV at night.", PR("watches")), ("We had lunch at noon yesterday.", PA("had"))], 4)
f431("F", [("Jane bought a bag last month.", PA("bought")), ("They saw a movie yesterday.", PA("saw")), ("We visit grandma on Sundays.", PR("visit")), ("I called my friend last night.", PA("called")), ("Tom was tired after the game.", PA("was"))], 3)

# 4-33 B, D, E, F: 부정문이 아닌 보기(We write ~ 등)는 발문만 보고 지워짐 → 원문항처럼 not을 쓴 오답으로
S433N = "발문에 ‘시점과 나머지 내용을 유지하면서 과거시제 부정문으로’ 조건이 붙었고, 오답 하나는 부정문이 아니어서 발문만 보고 지워졌다. 원문항 발문으로 되돌리고, 그 오답을 원문항처럼 not을 잘못 쓴 문장으로 바꿨다."
def f433(t, sub, past, base, rest, order):
    FIX.pop((4, 33, t), None)
    its = {"ok": (f"{sub} did not {base} {rest}.", "did not + 동사원형으로 바르게 바꿨으므로"), "didpast": (f"{sub} did not {past} {rest}.", "did not 뒤에는 과거형이 아니라 동사원형을 쓰므로"),
           "notpast": (f"{sub} not {past} {rest}.", "not만으로는 일반동사를 부정할 수 없고 did가 필요하므로"), "does": (f"{sub} does not {base} {rest}.", "과거의 일에 현재형 does를 쓸 수 없으므로"),
           "were": (f"{sub} were not {base} {rest}.", "일반동사의 부정에 be동사를 쓸 수 없으므로")}
    mk(4, 33, t, [its[k] for k in order], order.index("ok") + 1, "일반동사 과거 부정문은 주어 + did not(didn't) + 동사원형이다.", S433N, st="R")
f433("B", "We", "wrote", "write", "a letter yesterday", ["didpast", "ok", "notpast", "does", "were"])
f433("D", "Tom", "bought", "buy", "a new bike", ["didpast", "ok", "were", "does", "notpast"])
f433("E", "They", "saw", "see", "a movie last night", ["didpast", "were", "notpast", "does", "ok"])
f433("F", "Jane", "ate", "eat", "lunch at noon", ["ok", "were", "does", "notpast", "didpast"])
