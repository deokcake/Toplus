# 4급 CH7 형용사·부사·수량 표현·빈도부사 (61~70) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def slotnote(ch, good, why, labs=("첫째", "둘째", "셋째"), sep=" - "):
    xs = [x.strip() for x in ch.split(sep)]; gs = [x.strip() for x in good.split(sep)]
    if xs == gs: return "모든 빈칸에 알맞은 말을 골랐으므로"
    bits = [f"{labs[i]} 빈칸 {x}: {w}" for i, (x, g, w) in enumerate(zip(xs, gs, why)) if x != g]
    return ", ".join(bits) + ". 따라서"
LAB = lambda z: re.sub(r"\([AB]\) ", "", z)

# 4-61 C: 원문항과 같던 문장을 새로
mk(4, 61, "C", [("그녀는 아침을 전혀 먹지 않는다.", "‘전혀 ~않다’는 never이므로"), ("그녀는 아침을 거의 먹지 않는다.", "rarely(거의 ~않다)의 뜻을 바르게 옮겼으므로"), ("그녀는 가끔 아침을 먹는다.", "‘가끔’은 sometimes이므로"),
                ("그녀는 항상 아침을 먹는다.", "‘항상’은 always이므로"), ("그녀는 자주 아침을 먹는다.", "‘자주’는 often이므로")], 2,
   "빈도부사는 always(항상), usually(보통), often(자주), sometimes(가끔), rarely·seldom(거의 ~않다), never(전혀 ~않다)의 뜻을 구별한다.",
   "문장(He seldom forgets his keys.)과 정답 뜻이 원문항과 같았다. 문장을 ‘She rarely eats breakfast.’로 바꾸고, never와 구별하도록 ‘전혀 먹지 않는다’를 오답에 넣었다.", p="She rarely eats breakfast.")

# 4-62 형용사의 두 쓰임: 원문항 발문, 서술 용법 형용사 오답, 유형마다 선생님 예문을 달리
R462 = "형용사는 명사 앞에서 명사를 꾸미거나(a nice bike), be동사·look·smell·taste·sound·become·feel 같은 동사 뒤에서 주어를 보충 설명한다(The soup tastes salty)."
S462 = "원문항 오답은 동사 뒤에서 주어를 설명하는 형용사라 형용사의 두 쓰임을 구별하게 하는데, 변형 오답은 부사 문장이라 형용사/부사 구별로 바뀌었고 유형마다 반복되었다. 원문항 발문으로 되돌리고, 원문항처럼 형용사의 다른 쓰임을 오답으로 하여 유형마다 새로 썼다."
def ATT(adj, noun): return f"{adj}: 명사 {noun} 앞에서 명사를 꾸미는 형용사이므로"
def PRE(adj, v): return f"{adj}: 동사 {v} 뒤에서 주어를 보충 설명하는 형용사이므로"
def f462(t, ex, what, items, a, s=S462):
    p = f"선생님: 형용사는 명사 앞에서 명사를 수식하거나 동사 뒤에서 주어를 보충 설명할 수 있어요. \"{ex}\"에서는 {what}"
    mk(4, 62, t, [(x, w + (" 선생님 설명과 같아" if i + 1 == a else " 선생님 설명과 달라")) for i, (x, w) in enumerate(items)], a, R462, s, st="R", p=p)
f462("B", "Mina has a cute puppy.", "형용사 cute가 명사 puppy 앞에서 명사를 수식하고 있어요.",
     [("The water is warm.", PRE("warm", "is")), ("He looks tired.", PRE("tired", "looks")), ("He has an old car.", ATT("old", "car")), ("The cake smells sweet.", PRE("sweet", "smells")), ("The room became quiet.", PRE("quiet", "became"))], 3)
f462("C", "The soup tastes salty.", "형용사 salty가 동사 tastes 뒤에서 주어 the soup을 보충 설명하고 있어요.",
     [("I bought a red umbrella.", ATT("red", "umbrella")), ("Your idea sounds great.", PRE("great", "sounds")), ("She is a smart girl.", ATT("smart", "girl")), ("We live in a small town.", ATT("small", "town")), ("He found an interesting book.", ATT("interesting", "book"))], 2,
     "정답(I bought an expensive watch.)이 원문항과 똑같았고 오답도 B와 같았다. 선생님 설명의 예문을 서술 용법으로 바꿔 정답을 ‘Your idea sounds great.’로 새로 쓰고, 원문항처럼 형용사의 다른 쓰임을 오답으로 넣었다.")
f462("D", "We saw a tall tree.", "형용사 tall이 명사 tree 앞에서 명사를 수식하고 있어요.",
     [("The sky got dark.", PRE("dark", "got")), ("Jane seems busy.", PRE("busy", "seems")), ("The music is loud.", PRE("loud", "is")), ("The baby looks sleepy.", PRE("sleepy", "looks")), ("She has a beautiful dress.", ATT("beautiful", "dress"))], 5)
f462("E", "My brother became famous.", "형용사 famous가 동사 became 뒤에서 주어 my brother를 보충 설명하고 있어요.",
     [("Tom feels hungry.", PRE("hungry", "feels")), ("I have a new phone.", ATT("new", "phone")), ("They live in a big house.", ATT("big", "house")), ("She wore a long skirt.", ATT("long", "skirt")), ("We need a quiet place.", ATT("quiet", "place"))], 1,
     S462 + " 선생님 예문을 서술 용법으로 바꿔 정답의 쓰임도 다른 유형과 달리했다.")
f462("F", "Tom wants a fast car.", "형용사 fast가 명사 car 앞에서 명사를 수식하고 있어요.",
     [("The flowers smell nice.", PRE("nice", "smell")), ("The test was easy.", PRE("easy", "was")), ("Jane bought a new bag.", ATT("new", "bag")), ("You look happy today.", PRE("happy", "look")), ("The milk went bad.", PRE("bad", "went"))], 3)

# 4-63 many / much 짝: 원문항 발문, 정답 조합을 원문항(much - many)과 다르게
R463 = "many는 셀 수 있는 명사의 복수형, much는 셀 수 없는 명사와 함께 쓴다."
S463 = "발문에 ‘명사의 수량을 묻거나 나타내도록’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
for t in "BD": F(4, 63, t, st="R", s=S463)
def f463(t, p, c, a, why, s):
    mk(4, 63, t, [(x, slotnote(LAB(x), LAB(c[a-1]), why, labs=("(A)", "(B)"))) for x in c], a, R463, s, st="R", p=p, okdup=True)
f463("C", "(A) How ________ sugar do you want?\n(B) We don't have ________ time.", ["many - much", "much - much", "much - many", "many - many", "few - little"], 2,
     ["sugar는 셀 수 없는 명사라 much를 쓴다", "time은 셀 수 없는 명사라 much를 쓴다"], "제시문과 정답(much - many)이 원문항과 똑같았다. 문장을 새로 쓰고 정답 조합을 much - much로 바꿨다.")
f463("E", "(A) How ________ pencils do you have?\n(B) There are ________ cars on the road.", ["much - many", "many - much", "much - much", "many - many", "few - little"], 4,
     ["pencils는 셀 수 있는 명사의 복수형이라 many를 쓴다", "cars는 셀 수 있는 명사의 복수형이라 many를 쓴다"], "정답 조합(much - many)이 원문항과 같았다. 문장을 새로 써서 정답 조합을 many - many로 바꿨다.")
f463("F", "(A) How ________ eggs do we need?\n(B) I don't drink ________ coffee.", ["much - much", "many - many", "few - little", "much - many", "many - much"], 5,
     ["eggs는 셀 수 있는 명사의 복수형이라 many를 쓴다", "coffee는 셀 수 없는 명사라 much를 쓴다"], "정답 조합(much - many)이 원문항과 같았다. 문장을 새로 써서 정답 조합을 many - much로 바꿨다.")

# 4-64 틀린 문장: 짝 없이 유형마다 새로
R464 = "few·a few·many는 셀 수 있는 명사의 복수형, little·a little·much는 셀 수 없는 명사와 쓴다. a lot of·lots of는 둘 다에 쓴다."
S464 = "정답 문장과 같은 문장의 옳은/틀린 형태가 함께 있어 대비 단서가 되었고 오답 네 개가 유형마다 같았다. 짝 문장 없이 유형마다 새로 썼다."
OK64 = "명사의 종류에 맞는 수량 표현을 바르게 썼으므로"
def f464(t, items, a, s=S464):
    mk(4, 64, t, [(x, w or OK64) for x, w in items], a, R464, s)
f464("B", [("Tom has a little books.", "셀 수 있는 명사 books에는 a few를 써야 하므로"), ("I have little time today.", ""), ("We need much water.", ""), ("Mina has a few pencils.", ""), ("She has many friends.", "")], 1)
f464("C", [("There is a little juice in the glass.", ""), ("I have a few coins.", ""), ("He has little patience.", ""), ("We saw a lot of birds.", ""), ("She made few mistake.", "few 뒤에는 셀 수 있는 명사의 복수형 mistakes를 써야 하므로")], 5,
     S464 + " 정답(I have few time…)이 원문항과 거의 같아 새로 썼다.")
f464("D", [("There are a few cookies left.", ""), ("I have little money now.", ""), ("She has much friends.", "셀 수 있는 명사 friends에는 many를 써야 하므로"), ("They need a lot of help.", ""), ("He drank a little tea.", "")], 3)
f464("E", [("We need many water.", "셀 수 없는 명사 water에는 much를 써야 하므로"), ("Jane has a few cousins.", ""), ("There is little snow this year.", ""), ("He read a lot of books.", ""), ("I have a little free time.", "")], 1)
f464("F", [("She gave me a little advice.", ""), ("There is a few milk.", "셀 수 없는 명사 milk에는 a little을 써야 하므로"), ("I know a few words in Chinese.", ""), ("We have little homework today.", ""), ("They have lots of toys.", "")], 2)

# 4-65 옳은 문장으로만 짝: 원문항 형식(ⓐ~ⓓ, 밑줄, 두 개의 짝), 빈도부사·동사 문장 포함
ST465 = "다음 중 밑줄 친 부분이 어법상 옳은 문장으로만 짝지어진 것은?"
R465 = "many·(a) few는 셀 수 있는 명사, much·(a) little은 셀 수 없는 명사와 쓴다. 빈도부사는 일반동사 앞, be동사 뒤에 두고, 3인칭 단수 주어의 동사에는 -s/-es를 붙인다."
S465 = "원문항은 밑줄 친 네 문장 중 옳은 두 개의 짝을 고르는데, 변형은 밑줄 없이 ‘빠짐없이 모두’ 고르는 형식(‘해당 없음’ 포함)으로 바뀌었고 기호도 a~d로 바뀌었으며, 발문이 볼 곳(수량 표현)을 알려 주고 원문항의 빈도부사·동사 문장이 빠졌다. 원문항 발문과 형식(ⓐ~ⓓ, 밑줄, 두 개의 짝)으로 되돌리고 빈도부사 문장도 넣었다."
def f465(t, lines, judge, ok, c, s=S465):
    a = c.index(ok) + 1
    F(4, 65, t, st=ST465, p="\n".join(lines), c=c, a=a, r=R465, pre=["문장별 판정: " + j for j in judge], k=f"밑줄 친 부분이 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), okdup=True, s=s + ipos(a))
REF65 = ["ⓐ, ⓑ", "ⓐ, ⓒ", "ⓑ, ⓒ", "ⓑ, ⓓ", "ⓒ, ⓓ"]
f465("B", ["ⓐ I have <u>few books</u>.", "ⓑ Jane has <u>many money</u>.", "ⓒ He <u>always is</u> late.", "ⓓ We <u>often go</u> hiking."],
     ["ⓐ O. 셀 수 있는 명사 books에 few를 썼다.", "ⓑ X. 셀 수 없는 명사 money에는 much를 쓴다.", "ⓒ X. 빈도부사는 be동사 뒤에 와서 is always로 쓴다.", "ⓓ O. 빈도부사가 일반동사 앞에 왔다."], "ⓐ, ⓓ",
     ["ⓐ, ⓑ", "ⓐ, ⓓ", "ⓑ, ⓒ", "ⓑ, ⓓ", "ⓒ, ⓓ"])
f465("C", ["ⓐ She drinks <u>much milks</u>.", "ⓑ Minsu <u>usually walks</u> to school.", "ⓒ We have <u>a few eggs</u>.", "ⓓ They <u>never is</u> late."],
     ["ⓐ X. milk는 셀 수 없는 명사라 복수형을 쓰지 않는다.", "ⓑ O. 빈도부사가 일반동사 앞에 오고 3인칭 단수형 walks를 썼다.", "ⓒ O. 셀 수 있는 명사 eggs에 a few를 썼다.", "ⓓ X. 주어 They에는 are를 쓰고 빈도부사는 그 뒤에 온다."], "ⓑ, ⓒ", REF65,
     S465 + " 정답 조합(ⓐ, ⓒ)이 원문항과 같아 문장을 새로 썼다.")
f465("D", ["ⓐ I <u>sometimes plays</u> tennis.", "ⓑ We need <u>many money</u>.", "ⓒ There are <u>a few chairs</u>.", "ⓓ She <u>is often</u> busy."],
     ["ⓐ X. 주어 I에는 동사원형 play를 쓴다.", "ⓑ X. 셀 수 없는 명사 money에는 much를 쓴다.", "ⓒ O. 셀 수 있는 명사 chairs에 a few를 썼다.", "ⓓ O. 빈도부사가 be동사 뒤에 왔다."], "ⓒ, ⓓ", REF65)
f465("E", ["ⓐ Tom <u>rarely eats</u> fast food.", "ⓑ We have <u>a little homework</u>.", "ⓒ Jane has <u>much pencils</u>.", "ⓓ He <u>goes always</u> to bed early."],
     ["ⓐ O. 빈도부사가 일반동사 앞에 왔다.", "ⓑ O. 셀 수 없는 명사 homework에 a little을 썼다.", "ⓒ X. 셀 수 있는 명사 pencils에는 many를 쓴다.", "ⓓ X. 빈도부사는 일반동사 앞에 와서 always goes로 쓴다."], "ⓐ, ⓑ", REF65)
f465("F", ["ⓐ We drink <u>many water</u>.", "ⓑ She has <u>little money</u>.", "ⓒ He <u>seldom watch</u> TV.", "ⓓ They <u>are always</u> kind."],
     ["ⓐ X. 셀 수 없는 명사 water에는 much를 쓴다.", "ⓑ O. 셀 수 없는 명사 money에 little을 썼다.", "ⓒ X. 3인칭 단수 주어 He에는 watches를 쓴다.", "ⓓ O. 빈도부사가 be동사 뒤에 왔다."], "ⓑ, ⓓ", REF65)

# 4-66 옳은 수량 표현: 원문항 발문과 밑줄, 유형마다 새로
ST466 = "다음 중 밑줄 친 부분의 쓰임이 어법상 옳은 것은?"
R466 = "many·(a) few는 셀 수 있는 명사의 복수형, much·(a) little은 셀 수 없는 명사와 함께 쓴다."
S466 = "발문에 little의 뜻 조건이 붙고 밑줄이 사라졌으며 오답 네 개가 유형마다 같았다. 원문항 발문과 밑줄로 되돌리고 유형마다 새로 썼다."
def f466(t, items, a, s=S466):
    mk(4, 66, t, items, a, R466, s, st=ST466)
F(4, 66, "B", st=ST466, c=["She has <u>much</u> friends.", "We need <u>many</u> rice.", "There is <u>a few</u> water.", "I have <u>a little</u> books.", "I have <u>a little</u> money."], keepx=True,
  s="발문이 바뀌어 little의 뜻 조건이 붙고 밑줄이 사라졌다. 원문항 발문과 밑줄로 되돌렸다. 보기와 정답은 그대로다.")
f466("C", [("He has <u>a few</u> money.", "셀 수 없는 명사 money에는 a little을 쓰므로"), ("There are <u>little</u> apples.", "셀 수 있는 명사 apples에는 few를 쓰므로"), ("She bought <u>a few</u> eggs.", "셀 수 있는 명사 eggs에 a few를 바르게 썼으므로"),
           ("I need <u>many</u> sugar.", "셀 수 없는 명사 sugar에는 much를 쓰므로"), ("We have <u>much</u> classes today.", "셀 수 있는 명사 classes에는 many를 쓰므로")], 3,
     S466 + " 정답(There are a few students in the room.)이 원문항과 같아 새로 썼다.")
f466("D", [("There is <u>few</u> juice.", "셀 수 없는 명사 juice에는 little을 쓰므로"), ("I have <u>a little</u> pens.", "셀 수 있는 명사 pens에는 a few를 쓰므로"), ("He has <u>much</u> toys.", "셀 수 있는 명사 toys에는 many를 쓰므로"),
           ("She drinks <u>a little</u> milk every day.", "셀 수 없는 명사 milk에 a little을 바르게 썼으므로"), ("We saw <u>many</u> snow.", "셀 수 없는 명사 snow에는 much를 쓰므로")], 4)
f466("E", [("We need <u>much</u> water.", "셀 수 없는 명사 water에 much를 바르게 썼으므로"), ("He has <u>a few</u> bread.", "셀 수 없는 명사 bread에는 a little을 쓰므로"), ("There are <u>little</u> trees here.", "셀 수 있는 명사 trees에는 few를 쓰므로"),
           ("I read <u>much</u> books.", "셀 수 있는 명사 books에는 many를 쓰므로"), ("She has <u>many</u> homework.", "셀 수 없는 명사 homework에는 much를 쓰므로")], 1)
f466("F", [("I have <u>a little</u> friends.", "셀 수 있는 명사 friends에는 a few를 쓰므로"), ("Tom has <u>few</u> friends.", "셀 수 있는 명사 friends에 few를 바르게 썼으므로"), ("She drinks <u>many</u> coffee.", "셀 수 없는 명사 coffee에는 much를 쓰므로"),
           ("There is <u>a few</u> rice.", "셀 수 없는 명사 rice에는 a little을 쓰므로"), ("We have <u>much</u> chairs.", "셀 수 있는 명사 chairs에는 many를 쓰므로")], 2)

# 4-67 상황에 맞는 빈도부사: 원문항 발문, 상황만으로 판단(뜻 설명 삭제), 헷갈리는 두 부사는 함께 넣지 않음
R467 = "always(항상), usually(보통, 대개), often(자주), sometimes(가끔), seldom·hardly ever(거의 ~않다), never(전혀 ~않다)를 상황의 빈도에 맞게 고른다."
S467 = "발문이 ‘“항상”이라는 빈도로’처럼 정답의 뜻을 알려 주었다. 원문항 발문으로 되돌리고 상황만으로 빈도를 판단하게 했으며, 헷갈릴 수 있는 두 부사(often/sometimes)는 한 문항에 함께 넣지 않았다."
ADV = {"always": "always는 ‘항상’이라", "usually": "usually는 ‘보통, 대개’라", "often": "often은 ‘자주’라", "sometimes": "sometimes는 ‘가끔’이라", "seldom": "seldom은 ‘거의 ~않다’라",
       "never": "never는 ‘전혀 ~않다’라", "hardly ever": "hardly ever는 ‘거의 ~않다’라"}
def f467(t, sit, frame, c, ok, s=S467):
    a = c.index(ok) + 1
    mk(4, 67, t, [(x, ADV[x] + (" 상황과 맞으므로" if x == ok else " 상황과 맞지 않으므로")) for x in c], a, R467, s, st="R", p=f"{sit}\n→ {frame}", okdup=True)
f467("B", "Jane exercises every single day, even on holidays.", "Jane ________ exercises.", ["always", "often", "sometimes", "never", "seldom"], "always")
f467("C", "Minsu hates carrots. He has not eaten them even once in his life.", "Minsu ________ eats carrots.", ["often", "seldom", "always", "sometimes", "never"], "never",
     "제시문과 정답(seldom)이 원문항과 똑같았고 발문도 뜻을 알려 주었다. 상황을 새로 써서 정답을 never로 바꾸고 원문항 발문으로 되돌렸다.")
f467("D", "Tom loves movies. He watches movies three or four times every week.", "Tom ________ watches movies.", ["always", "never", "seldom", "often", "hardly ever"], "often")
f467("E", "Jane takes the bus to school on most days, but she walks once in a while.", "Jane ________ takes the bus to school.", ["always", "seldom", "usually", "never", "hardly ever"], "usually",
     S467 + " 정답을 usually로 바꿔 다른 유형과 달리했다.")
f467("F", "We eat out once in a while, but not often.", "We ________ eat out.", ["always", "often", "never", "sometimes", "usually"], "sometimes")

# 4-68 빈도·방식 부사 두 빈칸: 원문항 형식(대화 속 밑줄 빈칸), 모든 선택지 같은 표시, 정답 조합을 새로
ST468 = "다음 대화의 빈칸에 들어갈 말이 순서대로 짝지어진 것은?"
R468 = "hard는 ‘열심히’, hardly는 ‘거의 ~않다’로 뜻이 다르다. fast는 -ly 없이 부사로 쓰고(fastly는 없다), quiet는 형용사, quietly는 부사이다. 빈도는 always, often, sometimes, seldom, rarely로 나타낸다."
S468 = "정답 선택지에만 (A)(B) 표시가 붙어 정답이 드러났고, 대화 속 ‘almost never …, so he (A) …’가 빈칸의 뜻을 풀어 주었으며 밑줄과 줄바꿈도 사라졌다. 원문항처럼 대화 속 밑줄 빈칸으로 새로 쓰고 모든 선택지에 같은 표시를 붙였으며 유형마다 정답 조합을 달리했다."
BA, BB = "(<u>    A    </u>)", "(<u>    B    </u>)"
def f468(t, p, c, a, why, s=S468):
    mk(4, 68, t, [(x, slotnote(LAB(x), LAB(c[a-1]), why, labs=("(A)", "(B)"))) for x in c], a, R468, s, st=ST468, p=p.replace("(A)", BA).replace("(B)", BB), okdup=True)
f468("B", "A: Does Tom work (A) at his job?\nB: Yes, he always does his best.\nA: But he looks tired. Does he sleep well?\nB: No, he (B) sleeps these days.",
     ["(A) hardly - (B) hard", "(A) hard - (B) hardly", "(A) hard - (B) hard", "(A) hardly - (B) hardly", "(A) fast - (B) fastly"], 2,
     ["최선을 다한다는 대답에 맞게 ‘열심히’의 hard를 쓴다", "No라는 대답에 맞게 ‘거의 ~않다’의 hardly를 쓴다"], "정답(hardly - hard)이 원문항과 같았고 정답에만 (A)(B) 표시가 붙어 있었다. " + S468[S468.index("원문항처럼"):])
f468("C", "A: Is Jina a good runner?\nB: Yes. She runs very (A).\nA: Does she get tired after running?\nB: No, she (B) gets tired.",
     ["(A) fastly - (B) hard", "(A) fast - (B) hard", "(A) fast - (B) hardly", "(A) fastly - (B) hardly", "(A) hardly - (B) fast"], 3,
     ["‘빠르게’는 -ly 없이 fast로 쓴다", "No라는 대답에 맞게 ‘거의 ~않다’의 hardly를 쓴다"], "대화 인물·상황과 정답이 원문항과 같았다. " + S468[S468.index("원문항처럼"):])
f468("D", "A: Is Jane often late for school?\nB: No, she (A) comes late.\nA: But she was almost late today.\nB: Yes, so she ran (B) to be on time.",
     ["(A) seldom - (B) fast", "(A) often - (B) fast", "(A) seldom - (B) fastly", "(A) hard - (B) fast", "(A) often - (B) hardly"], 1,
     ["No라는 대답에 맞게 ‘거의 ~않다’의 seldom을 쓴다", "‘빠르게’는 -ly 없이 fast로 쓴다"])
f468("E", "A: Does your brother speak loudly?\nB: No, he (A) speaks loudly.\nA: How does he usually speak?\nB: He speaks very (B).",
     ["(A) often - (B) quiet", "(A) rarely - (B) quiet", "(A) often - (B) quietly", "(A) rarely - (B) quietly", "(A) always - (B) quietly"], 4,
     ["No라는 대답에 맞게 ‘거의 ~않다’의 rarely를 쓴다", "동사 speaks를 꾸미는 부사 quietly를 쓴다"])
f468("F", "A: Does Mina study every day?\nB: No, she (A) studies. She studies only once or twice a week.\nA: Does she study well?\nB: Yes. When she studies, she studies (B).",
     ["(A) always - (B) hard", "(A) sometimes - (B) hardly", "(A) never - (B) hard", "(A) always - (B) hardly", "(A) sometimes - (B) hard"], 5,
     ["일주일에 한두 번이라 ‘가끔’의 sometimes를 쓴다", "공부를 잘한다는 흐름이라 ‘열심히’의 hard를 쓴다"])

# 4-69 틀린 이유 설명: 원문항 발문과 밑줄, 제시 문장에 맞춘 그럴듯한 오개념
ST469 = "다음 대화의 밑줄 친 문장이 어법상 틀린 이유를 한국어로 가장 바르게 설명한 것은?"
R469 = "일반동사를 현재 시제로 쓸 때는 be동사를 덧붙이지 않는다. 빈도부사는 일반동사 앞에 두고, 3인칭 단수 주어의 동사에는 -s/-es를 붙인다."
S469 = "원문항 오답은 그럴듯한 오개념인데, 변형 오답(‘빈도부사는 문장 맨 끝에만 온다’ 등)은 뻔하고 유형마다 반복되었으며 밑줄도 사라졌다. 원문항 발문과 밑줄로 되돌리고 제시 문장에 맞춘 그럴듯한 오개념으로 오답을 유형마다 새로 썼다."
OK69 = "일반동사가 본동사라 불필요한 be동사를 빼야 한다는 이유를 바르게 설명했으므로"
def f469(t, p, items, a, s=S469):
    mk(4, 69, t, items, a, R469, s, st=ST469, p=p)
f469("B", "A: Do they often play soccer?\nB: Yes. <u>They are often play soccer</u>.",
     [("'often'은 긍정문에서 쓸 수 없는 단어이기 때문이다.", "often은 긍정문에서도 쓰므로"), ("'play'가 본동사이므로 불필요한 be동사 'are'를 빼고 'They often play soccer.'로 써야 하기 때문이다.", OK69),
      ("주어가 'They'이므로 'play'에 -s를 붙여 'plays'로 써야 하기 때문이다.", "복수 주어 They에는 동사원형 play를 쓰므로"), ("'often'은 반드시 문장 맨 끝에 와야 하기 때문이다.", "빈도부사는 일반동사 앞에 오므로"),
      ("'soccer' 앞에 관사 'the'가 빠졌기 때문이다.", "운동 이름 앞에는 관사를 쓰지 않으므로")], 2)
f469("C", "A: Does your dad cook on weekends?\nB: Yes. <u>He is always cook dinner on Sundays</u>.",
     [("'cook'은 '요리사'라는 명사이므로 앞에 관사 'a'를 넣어야 하기 때문이다.", "여기서 cook은 ‘요리하다’라는 동사이므로"), ("'always'는 be동사 앞에만 올 수 있기 때문이다.", "빈도부사는 be동사 뒤, 일반동사 앞에 오므로"),
      ("'on Sundays'가 있으면 과거형 'cooked'를 써야 하기 때문이다.", "on Sundays는 반복되는 습관이라 현재형을 쓰므로"), ("'cook'이 본동사이므로 불필요한 'is'를 빼고 3인칭 단수형 'cooks'로 써서 'He always cooks'로 고쳐야 하기 때문이다.", OK69),
      ("'always'는 부정문에서만 쓰이기 때문이다.", "always는 긍정문에서도 쓰므로")], 4,
     "대화와 정답 설명이 원문항과 같았다. 대화를 새로 쓰고 " + S469[S469.index("원문항 발문과"):])
f469("D", "A: Does Tom always study after school?\nB: No. <u>He is seldom study</u>.",
     [("'study'가 본동사이므로 불필요한 'is'를 빼고 'He seldom studies.'로 써야 하기 때문이다.", OK69), ("'seldom'은 부정의 뜻이 있으므로 'not'을 함께 써야 하기 때문이다.", "seldom에는 이미 부정의 뜻이 있어 not을 쓰지 않으므로"),
      ("'seldom'은 문장 맨 앞에만 올 수 있기 때문이다.", "빈도부사는 일반동사 앞에 오므로"), ("'Tom'이 3인칭이라 'is' 대신 'are'를 써야 하기 때문이다.", "be동사 자체가 필요 없고 Tom에는 are를 쓰지 않으므로"),
      ("'after school'이 없으면 'seldom'을 쓸 수 없기 때문이다.", "seldom은 때를 나타내는 말과 관계없이 쓰므로")], 1)
f469("E", "A: Does Jane usually read at night?\nB: Yes. <u>She is usually reads before bed</u>.",
     [("'usually'는 의문문에서만 쓸 수 있기 때문이다.", "usually는 평서문에서도 쓰므로"), ("'before bed'가 있으면 동사를 -ing형으로 써야 하기 때문이다.", "before bed는 동사의 형태와 관계없으므로"),
      ("'reads'가 본동사이므로 불필요한 'is'를 삭제하여 'She usually reads before bed.'로 써야 하기 때문이다.", OK69), ("'is' 뒤에는 동사원형 'read'가 와야 하므로 'She is usually read'로 고쳐야 하기 때문이다.", "is 뒤에 동사원형을 쓸 수 없고 is 자체를 빼야 하므로"),
      ("'usually'는 'reads' 뒤에 와야 하기 때문이다.", "빈도부사는 일반동사 앞에 오므로")], 3)
f469("F", "A: Do you always eat breakfast?\nB: No. <u>I am sometimes eat breakfast</u>.",
     [("주어 'I'에는 be동사 'is'를 써야 하기 때문이다.", "be동사 자체가 필요 없고 I에는 is를 쓰지 않으므로"), ("'sometimes'는 부정의 뜻이라 'eat' 뒤에 'not'을 써야 하기 때문이다.", "sometimes는 ‘가끔’이라 부정의 뜻이 없으므로"),
      ("'breakfast' 앞에 관사 'a'가 빠졌기 때문이다.", "식사 이름 앞에는 관사를 쓰지 않으므로"), ("'sometimes'는 과거 시제에서만 쓰이기 때문이다.", "sometimes는 현재 시제에도 쓰므로"),
      ("'eat'이 본동사이므로 불필요한 'am'을 빼고 'I sometimes eat breakfast.'로 써야 하기 때문이다.", OK69)], 5)

# 4-70 옳은 것만 묶인 것: 원문항 형식((a)~(e) 밑줄, 세 개 조합)
ST470 = "다음 중 밑줄 친 부분의 쓰임이 어법상 옳은 것만 묶인 것은?"
R470 = "few·a few·many는 셀 수 있는 명사의 복수형, little·a little·much는 셀 수 없는 명사와 함께 쓴다."
S470 = "원문항은 밑줄 친 다섯 문장 중 옳은 세 개의 조합을 고르는데, 변형은 밑줄 없이 ‘빠짐없이 모두’ 고르는 형식(3~4개 조합)으로 바뀌었고 줄바꿈이 사라졌다. 원문항 발문과 형식((a)~(e) 줄바꿈, 밑줄, 세 개 조합)으로 되돌렸다."
def f470(t, lines, judge, ok, c, s=S470):
    a = c.index(ok) + 1
    F(4, 70, t, st=ST470, p="\n".join(lines), c=c, a=a, r=R470, pre=["문장별 판정: " + j for j in judge], k=f"밑줄 친 부분의 쓰임이 옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), okdup=True, s=s + ipos(a))
REF70 = ["(a), (b), (c)", "(a), (d), (e)", "(b), (c), (d)", "(a), (c), (e)", "(b), (d), (e)"]
f470("B", ["(a) I have <u>few</u> pencils.", "(b) She drinks <u>much</u> milk.", "(c) We have <u>many</u> homework.", "(d) Tom has <u>a little</u> money.", "(e) They have <u>a little</u> friends."],
     ["(a) O. 셀 수 있는 명사 pencils에 few를 썼다.", "(b) O. 셀 수 없는 명사 milk에 much를 썼다.", "(c) X. 셀 수 없는 명사 homework에는 much를 쓴다.", "(d) O. 셀 수 없는 명사 money에 a little을 썼다.", "(e) X. 셀 수 있는 명사 friends에는 a few를 쓴다."], "(a), (b), (d)",
     ["(a), (b), (c)", "(a), (b), (d)", "(b), (c), (e)", "(a), (d), (e)", "(c), (d), (e)"])
f470("C", ["(a) She bought <u>a few</u> oranges.", "(b) He ate <u>a few</u> bread.", "(c) We have <u>a little</u> time.", "(d) He has <u>much</u> friends.", "(e) There are <u>many</u> books."],
     ["(a) O. 셀 수 있는 명사 oranges에 a few를 썼다.", "(b) X. 셀 수 없는 명사 bread에는 a little을 쓴다.", "(c) O. 셀 수 없는 명사 time에 a little을 썼다.", "(d) X. 셀 수 있는 명사 friends에는 many를 쓴다.", "(e) O. 셀 수 있는 명사 books에 many를 썼다."], "(a), (c), (e)", REF70,
     S470 + " (a)(b)가 원문항 문장과 같고 정답 조합도 같아 문장을 새로 썼다.")
f470("D", ["(a) There are <u>a few</u> cars.", "(b) We need <u>much</u> water.", "(c) Jane has <u>a little</u> books.", "(d) I have <u>few</u> money.", "(e) Tom eats <u>a little</u> rice."],
     ["(a) O. 셀 수 있는 명사 cars에 a few를 썼다.", "(b) O. 셀 수 없는 명사 water에 much를 썼다.", "(c) X. 셀 수 있는 명사 books에는 a few를 쓴다.", "(d) X. 셀 수 없는 명사 money에는 little을 쓴다.", "(e) O. 셀 수 없는 명사 rice에 a little을 썼다."], "(a), (b), (e)",
     ["(a), (b), (e)", "(a), (c), (d)", "(b), (c), (d)", "(a), (d), (e)", "(b), (d), (e)"])
f470("E", ["(a) She has <u>much</u> apples.", "(b) We have <u>little</u> time.", "(c) I need <u>a few</u> water.", "(d) They have <u>much</u> money.", "(e) Tom has <u>few</u> books."],
     ["(a) X. 셀 수 있는 명사 apples에는 many를 쓴다.", "(b) O. 셀 수 없는 명사 time에 little을 썼다.", "(c) X. 셀 수 없는 명사 water에는 a little을 쓴다.", "(d) O. 셀 수 없는 명사 money에 much를 썼다.", "(e) O. 셀 수 있는 명사 books에 few를 썼다."], "(b), (d), (e)", REF70)
f470("F", ["(a) I have <u>a little</u> questions.", "(b) Jane has <u>little</u> money.", "(c) We drink <u>much</u> milk.", "(d) They have <u>many</u> books.", "(e) Tom has <u>a few</u> rice."],
     ["(a) X. 셀 수 있는 명사 questions에는 a few를 쓴다.", "(b) O. 셀 수 없는 명사 money에 little을 썼다.", "(c) O. 셀 수 없는 명사 milk에 much를 썼다.", "(d) O. 셀 수 있는 명사 books에 many를 썼다.", "(e) X. 셀 수 없는 명사 rice에는 a little을 쓴다."], "(b), (c), (d)", REF70)


# ---- 2차 감수(2026-10) 추가 ----
# 4-61 B, D, F: 부정의 뜻인 보기 두 개만 끝 마침표가 빠짐 → 마침표를 붙여 원문항과 같게
R461 = "빈도부사의 뜻: always(항상), usually(보통), often(자주), sometimes(가끔), seldom·rarely(거의 ~않다), never(전혀 ~않다)."
S461 = "다섯 보기 가운데 두 개(‘~하지 않는다’로 끝나는 보기)만 끝 마침표가 빠져 있었다. 원문항처럼 모든 보기에 마침표를 붙였다. 보기와 정답은 그대로다."
W461 = {"거의": "‘거의 ~않다’는 seldom·rarely이므로", "항상": "‘항상’은 always이므로", "가끔": "‘가끔’은 sometimes이므로", "전혀": "‘전혀 ~않다’는 never이므로", "자주": "‘자주’는 often이므로"}
for t, adv in (("B", "often"), ("D", "always"), ("F", "sometimes")):
    v = V(4, 61, t); a = "①②③④⑤".index(v["ans"]) + 1 if str(v["ans"]) in "①②③④⑤" else int(v["ans"])
    items = []
    for i_, x in enumerate(v["c"]):
        key = next(k for k in W461 if k in x)
        items.append((x if x.endswith(".") else x + ".", f"{adv}의 뜻을 바르게 옮겼으므로" if i_ + 1 == a else W461[key]))
    mk(4, 61, t, items, a, R461, S461, st="R")
