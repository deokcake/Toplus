# 7급 CH6 일반동사 현재형 (51~60) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
R_V = "일반동사 현재형은 3인칭 단수 주어(he, she, it, 사람·동물 한 명)에 -s/-es(자음 + y는 -ies, have는 has)를 붙이고, I·you·we·they와 복수 주어에는 동사원형을 쓴다. 부정문은 don't/doesn't + 동사원형으로 쓴다."

# 7-51 우리말에 맞는 문장: 같은 주어의 다른 동작 문장으로 오답
R751 = "우리말의 주어와 동작, 목적어가 모두 맞는 문장을 고른다."
S751 = "오답 서너 개가 원문항 선택지 그대로였고, 주어가 I라 우리말 주어와 바로 어긋나 정답이 드러났다. 원문항처럼 같은 주어로 동작이나 목적어만 다른 문장으로 오답을 새로 썼다."
MEAN = lambda k: f"‘{k}’라는 뜻이라 우리말과 맞지 않으므로"; OK51 = "우리말의 주어·동작·목적어와 모두 맞으므로"
def f751(t, ko, items, a, s=S751):
    mk(7, 51, t, [(x, w or OK51) for x, w in items], a, R751, s, p=ko)
f751("B", "그들은 축구를 한다.", [("They watch soccer.", MEAN("그들은 축구를 본다")), ("They play baseball.", MEAN("그들은 야구를 한다")), ("They love dancing.", MEAN("그들은 춤추는 것을 좋아한다")), ("They study math.", MEAN("그들은 수학을 공부한다")), ("They play soccer.", "")], 5)
f751("C", "그녀는 영어를 공부한다.", [("She teaches English.", MEAN("그녀는 영어를 가르친다")), ("She studies English.", ""), ("She studies math.", MEAN("그녀는 수학을 공부한다")), ("She speaks English.", MEAN("그녀는 영어를 말한다")), ("She likes English.", MEAN("그녀는 영어를 좋아한다"))], 2)
f751("D", "Tom은 책을 읽는다.", [("Tom reads a book.", ""), ("Tom buys a book.", MEAN("Tom은 책을 산다")), ("Tom writes a book.", MEAN("Tom은 책을 쓴다")), ("Tom reads a letter.", MEAN("Tom은 편지를 읽는다")), ("Tom sells a book.", MEAN("Tom은 책을 판다"))], 1)
f751("E", "우리는 TV를 본다.", [("We watch a movie.", MEAN("우리는 영화를 본다")), ("We fix the TV.", MEAN("우리는 TV를 고친다")), ("We buy a TV.", MEAN("우리는 TV를 산다")), ("We watch TV.", ""), ("We turn off the TV.", MEAN("우리는 TV를 끈다"))], 4)
f751("F", "우리는 방과 후에 체스를 둔다.", [("We play soccer after school.", MEAN("우리는 방과 후에 축구를 한다")), ("We watch TV after school.", MEAN("우리는 방과 후에 TV를 본다")), ("We play chess after school.", ""), ("We read books after school.", MEAN("우리는 방과 후에 책을 읽는다")), ("We play the piano after school.", MEAN("우리는 방과 후에 피아노를 친다"))], 3,
     "원문항은 같은 주어로 뜻이 다른 문장 중 우리말에 맞는 것을 고르는데, 변형은 동사 형태 오류를 찾는 선택지로 바뀌었다. 원문항처럼 같은 주어로 동작이나 목적어만 다른 문장으로 선택지를 바꿨다.")

# 7-53 두 빈칸: 원문항 발문과 문장별 우리말
S753 = "원문항의 문장별 우리말 해석이 빠지고 발문에 ‘현재형으로’가 붙었다. 원문항 발문으로 되돌리고 우리말 해석을 붙였다. 보기와 정답은 그대로다."
def f753(t, p, good, why):
    V_ = V(7, 53, t); gs = [x.strip() for x in good.split(" - ")]; items = []
    for ch in V_["c"]:
        xs = [x.strip() for x in ch.split(" - ")]
        if xs == gs: items.append((ch, "두 문장의 주어에 맞는 현재형을 바르게 짝지었으므로")); continue
        bits = [f"{['첫째', '둘째'][i]} 빈칸 {x}: {why[i]}" for i, (x, g) in enumerate(zip(xs, gs)) if x != g]
        items.append((ch, ". ".join(bits) + ". 따라서"))
    mk(7, 53, t, items, int(V_["ans"]), R_V, S753, st="R", p=p, okdup=True)
f753("B", "- The girls _______ comics. (그 소녀들은 만화책을 읽는다.)\n- Mina _______ novels. (Mina는 소설을 읽는다.)", "read - reads", ["복수 주어 The girls에는 동사원형 read를 쓴다", "3인칭 단수 주어 Mina에는 reads를 쓴다"])
f753("C", "We _______ books. (우리는 책을 읽는다.)\nTom _______ TV. (Tom은 TV를 본다.)", "read - watches", ["주어 We에는 동사원형 read를 쓴다", "3인칭 단수 주어 Tom에는 watches를 쓴다"])
f753("D", "They _______ home. (그들은 집에 간다.)\nShe _______ to school. (그녀는 학교에 간다.)", "go - goes", ["주어 They에는 동사원형 go를 쓴다", "3인칭 단수 주어 She에는 goes를 쓴다"])
f753("E", "I _______ apples. (나는 사과를 좋아한다.)\nMy brother _______ milk. (나의 형은 우유를 좋아한다.)", "like - likes", ["주어 I에는 동사원형 like를 쓴다", "3인칭 단수 주어 My brother에는 likes를 쓴다"])
f753("F", "The boys _______ soccer. (그 소년들은 축구를 한다.)\nJane _______ English. (Jane은 영어를 공부한다.)", "play - studies", ["복수 주어 The boys에는 동사원형 play를 쓴다", "3인칭 단수 주어 Jane에는 studies를 쓴다"])

# 7-55 틀린 문장: 원문항 발문, 짝 없이 유형마다 새로
S755 = "발문에 ‘일반동사의 현재형이’가 붙었고, 정답 문장과 같은 동사의 옳은 형태가 함께 있어 대비 단서가 되었으며 오답이 유형마다 같았다. 원문항 발문으로 되돌리고 짝 문장 없이 유형마다 새로 썼다."
OK55 = "주어에 맞는 현재형 동사를 바르게 썼으므로"
def f755(t, items, a, s=S755):
    mk(7, 55, t, [(x, w or OK55) for x, w in items], a, R_V, s, st="R")
f755("B", [("We study together.", ""), ("Jane carries a violin.", ""), ("Tom watches cartoons.", ""), ("The baby cries at night.", ""), ("My cousins lives nearby.", "복수 주어 My cousins에는 동사원형 live를 써야 하므로")], 5, "발문에 ‘일반동사의 현재형이’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f755("C", [("She has a new bike.", ""), ("We go to the park.", ""), ("The boys studies English.", "복수 주어 The boys에는 동사원형 study를 써야 하므로"), ("Mom makes cookies.", ""), ("I like games.", "")], 3)
f755("D", [("My sister reads a lot.", ""), ("They swim in the sea.", ""), ("Dad fixes the car.", ""), ("We eat breakfast at seven.", ""), ("I goes to school by bus.", "주어 I에는 동사원형 go를 써야 하므로")], 5)
f755("E", [("The cat sleeps all day.", ""), ("You speak English well.", ""), ("Jiho carries the box.", ""), ("We likes pizza.", "주어 We에는 동사원형 like를 써야 하므로"), ("My parents work hard.", "")], 4)
f755("F", [("You watches TV every night.", "주어 You에는 동사원형 watch를 써야 하므로"), ("The bird flies high.", ""), ("I brush my teeth.", ""), ("Tom washes his face.", ""), ("They sing together.", "")], 1)

# 7-56 빈칸: 원문항 발문
S756 = "발문에 ‘일반동사의 현재형으로’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def f756(t, subj, base):
    V_ = V(7, 56, t); a = int(V_["ans"]); items = []
    for o in V_["c"]:
        if o == base: items.append((o, f"주어({subj})에 맞는 동사원형이므로"))
        elif o.startswith("is "): items.append((o, "일반동사 앞에 be동사를 함께 쓸 수 없으므로"))
        elif o.startswith("to "): items.append((o, "to부정사만으로는 동사 자리를 채울 수 없으므로"))
        elif o.endswith("ing"): items.append((o, "-ing형만으로는 동사 자리를 채울 수 없으므로"))
        else: items.append((o, f"-s형은 3인칭 단수 주어에 쓰므로"))
    mk(7, 56, t, items, a, R_V, S756, st="R")
f756("B", "I", "read"); f756("C", "They", "play"); f756("D", "They", "clean"); f756("E", "You", "study"); f756("F", "We", "watch")

# 7-57 두 빈칸: 원문항 발문
S757 = "발문에 ‘현재형으로’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def f757(t, good, why):
    V_ = V(7, 57, t); gs = [x.strip() for x in good.split(" - ")]; items = []
    for ch in V_["c"]:
        xs = [x.strip() for x in ch.split(" - ")]
        if xs == gs: items.append((ch, "두 문장의 주어에 맞는 현재형을 바르게 짝지었으므로")); continue
        bits = [f"{['첫째', '둘째'][i]} 빈칸 {x}: {why[i]}" for i, (x, g) in enumerate(zip(xs, gs)) if x != g]
        items.append((ch, ". ".join(bits) + ". 따라서"))
    mk(7, 57, t, items, int(V_["ans"]), R_V, S757, st="R", okdup=True)
f757("B", "runs - run", ["3인칭 단수 주어 My dog에는 runs를 쓴다", "주어 I에는 동사원형 run을 쓴다"])
f757("C", "studies - study", ["3인칭 단수 주어 Tom에는 studies를 쓴다", "주어 We에는 동사원형 study를 쓴다"])
f757("D", "cooks - cook", ["3인칭 단수 주어 Dad에는 cooks를 쓴다", "주어 We에는 동사원형 cook을 쓴다"])
f757("E", "watches - watch", ["3인칭 단수 주어 Jane에는 watches를 쓴다", "주어 They에는 동사원형 watch를 쓴다"])
f757("F", "goes - go", ["3인칭 단수 주어 Dad에는 goes를 쓴다", "주어 You에는 동사원형 go를 쓴다"])

# 7-58 밑줄이 올바른 문장: 원문항 발문과 동사 밑줄, 오답을 원문항과 다르게
S758 = "오답이 원문항 선택지 그대로였거나 발문이 달랐고, 밑줄도 사라졌다. 원문항 발문과 동사 밑줄로 되돌리고 유형마다 오답을 새로 썼다."
def f758(t, items, a, s=S758):
    mk(7, 58, t, items, a, R_V, s, st="R")
f758("B", [("Mina <u>play</u> the piano.", "3인칭 단수 주어 Mina에는 plays를 써야 하므로"), ("We <u>goes</u> home early.", "주어 We에는 동사원형 go를 써야 하므로"), ("I <u>read</u> books.", "주어 I에 동사원형 read를 바르게 썼으므로"), ("He <u>have</u> a dog.", "3인칭 단수 주어 He에는 has를 써야 하므로"), ("The kids <u>runs</u> fast.", "복수 주어 The kids에는 동사원형 run을 써야 하므로")], 3)
f758("C", [("They <u>eats</u> lunch.", "주어 They에는 동사원형 eat을 써야 하므로"), ("She <u>watch</u> movies.", "3인칭 단수 주어 She에는 watches를 써야 하므로"), ("I <u>cleans</u> my room.", "주어 I에는 동사원형 clean을 써야 하므로"), ("Tom <u>likes</u> pizza.", "3인칭 단수 주어 Tom에 likes를 바르게 썼으므로"), ("My dad <u>drink</u> coffee.", "3인칭 단수 주어 My dad에는 drinks를 써야 하므로")], 4)
f758("D", [("I <u>reads</u> every day.", "주어 I에는 동사원형 read를 써야 하므로"), ("My friends <u>plays</u> chess.", "복수 주어 My friends에는 동사원형 play를 써야 하므로"), ("They <u>walks</u> home.", "주어 They에는 동사원형 walk를 써야 하므로"), ("The baby <u>cries</u> at night.", "3인칭 단수 주어에 cries를 바르게 썼으므로"), ("You <u>likes</u> music.", "주어 You에는 동사원형 like를 써야 하므로")], 4,
     "밑줄이 사라지고 발문이 원문항과 달랐다. 원문항 발문과 동사 밑줄로 되돌렸다. 보기와 정답은 그대로다.")
f758("E", [("Jane <u>goes</u> home.", "3인칭 단수 주어 Jane에 goes를 바르게 썼으므로"), ("The dogs <u>barks</u> loudly.", "복수 주어 The dogs에는 동사원형 bark를 써야 하므로"), ("You <u>sings</u> well.", "주어 You에는 동사원형 sing을 써야 하므로"), ("He <u>study</u> hard.", "3인칭 단수 주어 He에는 studies를 써야 하므로"), ("We <u>has</u> a cat.", "주어 We에는 have를 써야 하므로")], 1)
f758("F", [("My mom <u>teach</u> English.", "3인칭 단수 주어 My mom에는 teaches를 써야 하므로"), ("They <u>play</u> soccer.", "주어 They에 동사원형 play를 바르게 썼으므로"), ("I <u>plays</u> the guitar.", "주어 I에는 동사원형 play를 써야 하므로"), ("Jane <u>fly</u> a kite.", "3인칭 단수 주어 Jane에는 flies를 써야 하므로"), ("The birds <u>sings</u> in the tree.", "복수 주어 The birds에는 동사원형 sing을 써야 하므로")], 2)

# 7-59 s를 붙이지 않은 이유: C·E·F는 원문항처럼 그럴듯한 오해로 오답 새로
R759 = "일반동사에 -s/-es를 붙일지는 주어로 정한다. 주어가 I·you·we·they나 복수면 동사원형을 쓴다. 목적어의 수, 문장 부호, 거리는 관계없다."
S759 = "오답 네 개가 B와 똑같았다. 원문항처럼 목적어의 수, 동사의 뜻, 가까이 있는 말 같은 그럴듯한 오해로 유형마다 오답을 새로 썼다."
OBJ = "목적어의 수는 동사의 형태를 정하지 않으므로"
def f759(t, items, a, s=S759):
    mk(7, 59, t, items, a, R759, s)
f759("C", [("'this game'이 한 개이기 때문이다.", OBJ), ("like는 언제나 모양이 변하지 않는 동사이기 때문이다.", "3인칭 단수 주어에는 likes로 모양이 바뀌므로"), ("Ben이 동사 바로 앞에 있어 Ben에 맞췄기 때문이다.", "Ben에 맞췄다면 likes를 써야 하고, 주어는 Tom and Ben 전체이므로"),
           ("this가 가까운 것을 가리키기 때문이다.", "목적어의 거리는 동사의 형태와 관계없으므로"), ("주어 Tom and Ben이 두 사람(복수)이기 때문이다.", "복수 주어에는 동사원형을 쓰므로")], 5)
f759("E", [("play는 운동에 쓰는 동사라 s를 붙이지 않기 때문이다.", "3인칭 단수 주어에는 plays로 쓰므로"), ("this game이 가까이 있기 때문이다.", "목적어의 거리는 동사의 형태와 관계없으므로"), ("The가 붙은 주어 뒤에는 동사원형을 쓰기 때문이다.", "The boy처럼 단수 주어면 plays를 쓰므로"),
           ("주어 The boys가 여러 명(복수)이기 때문이다.", "복수 주어에는 동사원형을 쓰므로"), ("문장이 현재가 아니라 과거이기 때문이다.", "play는 현재형이므로")], 4)
f759("F", [("book이 한 권이라서", OBJ), ("read는 과거형과 모양이 같아서 s를 붙이지 않기 때문이다.", "3인칭 단수 주어에는 reads로 쓰므로"), ("주어 We가 나를 포함한 여러 명(복수)이기 때문이다.", "주어 We에는 동사원형을 쓰므로"),
           ("this가 붙은 목적어 앞의 동사는 원형이기 때문이다.", "목적어 앞의 this는 동사의 형태와 관계없으므로"), ("We가 짧은 단어라서", "주어의 길이는 동사의 형태와 관계없으므로")], 3)

# 7-60 부정문 바꾸기: 원문항 발문
R760 = "일반동사 현재형의 부정문은 don't/doesn't + 동사원형으로 만든다. 3인칭 단수 주어에는 doesn't를 쓰고, 그 뒤의 동사는 -s를 떼어 원형으로 쓴다."
S760 = "발문의 ‘부정문(..하지 않는다)으로’가 ‘현재형 부정문으로’로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def f760(t, subj):
    V_ = V(7, 60, t); a = int(V_["ans"]); items = []
    for o in V_["c"]:
        if " not " in o and "does not" not in o and "is not" not in o: w = "not만 넣지 않고 doesn't + 동사원형으로 부정문을 만들므로"
        elif "don't" in o: w = f"3인칭 단수 주어({subj})에는 don't가 아니라 doesn't를 쓰므로"
        elif "isn't" in o or "is not" in o: w = "일반동사의 부정문에는 be동사(is not, isn't)를 쓰지 않으므로"
        elif "does not" in o or ("doesn't" in o and not re.search(r"doesn't \w+ ", o + " ") ): w = "doesn't/does not 뒤에는 -s를 뗀 동사원형을 써야 하므로"
        else: w = "doesn't 뒤에 동사원형을 써서 부정문을 바르게 만들었으므로"
        items.append((o, w))
    items[a-1] = (V_["c"][a-1], "doesn't 뒤에 동사원형을 써서 부정문을 바르게 만들었으므로")
    for i, (o, w) in enumerate(items):
        if i + 1 != a and w.startswith("doesn't 뒤에 동사원형을 써서"): items[i] = (o, "doesn't/does not 뒤에는 -s를 뗀 동사원형을 써야 하므로")
    mk(7, 60, t, items, a, R760, S760, st="R")
for t, s_ in [("B", "Jane"), ("C", "Tom"), ("D", "Mina"), ("E", "She"), ("F", "My dog")]: f760(t, s_)

# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, r, s, **kw):
    FIX.pop((7, n, t), None)
    mk(7, n, t, items, a, r, s, **kw)
def pair2(cs, good, why, okmsg):
    gs = [x.strip() for x in good.split(" - ")]; items = []
    for ch in cs:
        xs = [x.strip() for x in ch.split(" - ")]
        bad = [(i, x) for i, x in enumerate(xs) if x != gs[i]]
        if not bad: items.append((ch, okmsg)); continue
        items.append((ch, ". ".join(f"{['첫째', '둘째'][i]} 빈칸 {x}: {why[i]}" for i, x in bad) + ". 따라서"))
    return items
# 7-52 B·C·D·F: 오답 네 개(play, read, like, speak)가 네 유형에서 모두 같고 -s만 붙이는 동사뿐
R752 = "3인칭 단수형은 대부분 동사원형에 -s를 붙인다. -s, -sh, -ch, -x, -o로 끝나면 -es를 붙이고, 자음 + y로 끝나면 y를 i로 바꾸고 -es를 붙인다(모음 + y는 -s만). have는 has가 된다."
S752 = "오답 네 개(play - plays, read - reads, like - likes, speak - speaks)가 B·C·D·F에서 모두 같았고 그중 둘은 원문항 선택지 그대로였다. 또 오답이 모두 -s만 붙이는 동사라 규칙이 다른 동사 하나가 바로 정답으로 드러났다. 원문항처럼 -s, -es, -ies가 섞이도록 유형마다 새 동사로 썼다."
PS = "동사원형에 -s를 바르게 붙였으므로"; VY = "모음 + y로 끝나 -s만 붙였으므로"; CY = "자음 + y로 끝나 y를 i로 바꾸고 -es를 붙였으므로"; ES = lambda e: f"-{e}로 끝나 -es를 바르게 붙였으므로"
mk(7, 52, "B", [("teach - teaches", ES("ch")), ("sing - sings", PS), ("mix - mixs", "-x로 끝나는 동사는 -es를 붙여 mixes로 써야 하므로"), ("cry - cries", CY), ("buy - buys", VY)], 3, R752,
   S752 + " 변형의 정답(wash - washs)도 원문항 ⑤(wash - washes)를 틀리게 쓴 것이고 위치(④)가 원문항과 같았다.", st="R")
mk(7, 52, "C", [("have - haves", "have의 3인칭 단수형은 has이므로"), ("run - runs", PS), ("pass - passes", ES("s")), ("stay - stays", VY), ("fly - flies", CY)], 1, R752, S752, st="R")
mk(7, 52, "D", [("watch - watches", ES("ch")), ("enjoy - enjoys", VY), ("come - comes", PS), ("make - makes", PS), ("study - studys", "자음 + y로 끝나는 동사는 y를 i로 바꾸고 -es를 붙여 studies로 써야 하므로")], 5, R752, S752, st="R")
mk(7, 52, "F", [("pay - pays", VY), ("push - pushs", "-sh로 끝나는 동사는 -es를 붙여 pushes로 써야 하므로"), ("open - opens", PS), ("dance - dances", PS), ("guess - guesses", ES("s"))], 2, R752,
   S752 + " 변형의 정답(go - gos)도 원문항 ②(go - goes)를 틀리게 쓴 것이고 위치(②)가 원문항과 같았다.", st="R")
# 7-53: 원문항처럼 ‘-’와 우리말 해석 줄, B·D·E는 정답 꼴이 유형마다 다르게
S753B = "원문항의 문장별 우리말 해석이 빠지고 발문에 ‘현재형으로’가 붙었다. 원문항 발문으로 되돌리고, 원문항처럼 문장 앞에 ‘-’를 붙이고 우리말 해석을 문장 아래 줄에 두었다."
S753C = " 또 다섯 유형의 정답이 모두 원문항과 같은 꼴(동사원형 - 3인칭 단수형)이어서, 주어를 바꿔 정답이 %s가 되게 했다. 보기는 그대로다."
def g753(t, lines, good, why, a, s):
    cs = V(7, 53, t)["c"]; assert cs[a-1] == good, (t, cs, good)
    redo(53, t, pair2(cs, good, why, "두 문장의 주어에 맞는 현재형을 바르게 짝지었으므로"), a, R_V, s, st="R", p="\n".join(lines), okdup=True)
g753("B", ["- Mina _______ comics.", "(Mina는 만화책을 읽는다.)", "- The girls _______ novels.", "(그 소녀들은 소설을 읽는다.)"], "reads - read", ["3인칭 단수 주어 Mina에는 reads를 쓴다", "복수 주어 The girls에는 동사원형 read를 쓴다"], 1, S753B + S753C % "reads - read")
g753("C", ["- We _______ books.", "(우리는 책을 읽는다.)", "- Tom _______ TV.", "(Tom은 TV를 본다.)"], "read - watches", ["주어 We에는 동사원형 read를 쓴다", "3인칭 단수 주어 Tom에는 watches를 쓴다"], 3, S753B + " 보기와 정답은 그대로다.")
g753("D", ["- He _______ home.", "(그는 집에 간다.)", "- She _______ to school.", "(그녀는 학교에 간다.)"], "goes - goes", ["3인칭 단수 주어 He에는 goes를 쓴다", "3인칭 단수 주어 She에는 goes를 쓴다"], 5, S753B + S753C % "goes - goes")
g753("E", ["- I _______ apples.", "(나는 사과를 좋아한다.)", "- My brothers _______ milk.", "(나의 형들은 우유를 좋아한다.)"], "like - like", ["주어 I에는 동사원형 like를 쓴다", "복수 주어 My brothers에는 동사원형 like를 쓴다"], 4, S753B + S753C % "like - like")
g753("F", ["- The boys _______ soccer.", "(그 소년들은 축구를 한다.)", "- Jane _______ English.", "(Jane은 영어를 공부한다.)"], "play - studies", ["복수 주어 The boys에는 동사원형 play를 쓴다", "3인칭 단수 주어 Jane에는 studies를 쓴다"], 2, S753B + " 보기와 정답은 그대로다.")
# 7-54 B·D·E·F: 오답 네 개(You, I, They, Kate and David)가 원문항 그대로이고 네 유형에서 같음
R754 = "동사에 -s/-es가 붙었거나 has이면 주어는 3인칭 단수(he, she, it, 한 사람·한 개)여야 한다. I, you, we, they와 복수 주어 뒤에는 동사원형을 쓴다."
S754 = "오답 네 개(You, I, They, Kate and David)가 원문항 선택지 그대로이고 B·D·E·F에서 모두 같았다. 유형마다 다른 주어로 오답을 새로 썼다."
def g754(t, verb, base, items, a):
    d = {"1": f"한 사람(3인칭 단수)이라 {verb}와 어울리므로", "p": f"여럿(복수)이라 동사원형 {base}를 써야 하므로", "x": f"뒤에 동사원형 {base}를 써야 하므로"}
    mk(7, 54, t, [(x, d[k]) for x, k in items], a, R754, S754)
g754("B", "studies", "study", [("We", "x"), ("My sister", "1"), ("Tom and I", "p"), ("The girls", "p"), ("You", "x")], 2)
g754("D", "goes", "go", [("My friends", "p"), ("I", "x"), ("Jane", "1"), ("We", "x"), ("Jane and Mina", "p")], 3)
g754("E", "watches", "watch", [("You", "x"), ("My parents", "p"), ("I", "x"), ("The boy", "1"), ("The children", "p")], 4)
g754("F", "likes", "like", [("Tom", "1"), ("They", "x"), ("I", "x"), ("Tom's friends", "p"), ("We", "x")], 1)
# 7-56 E·F: 보기에 없는 형태(studys, watchs) → 실제 3인칭 단수형
def g756(t, subj, items, a, bad, good):
    redo(56, t, items, a, R_V, f"발문에 ‘일반동사의 현재형으로’가 붙었고, 보기에 없는 형태({bad})가 있었다(원문항의 보기 runs는 실제로 쓰는 형태다). 원문항 발문으로 되돌리고 {bad}를 {good}로 바꿨다. 정답은 그대로다.", st="R")
g756("E", "You", [("studying", "-ing형만으로는 동사 자리를 채울 수 없으므로"), ("studies", "-ies형은 3인칭 단수 주어에 쓰므로"), ("is study", "일반동사 앞에 be동사를 함께 쓸 수 없으므로"), ("study", "주어(You)에 맞는 동사원형이므로"), ("to study", "to부정사만으로는 동사 자리를 채울 수 없으므로")], 4, "studys", "studies")
g756("F", "We", [("watch", "주어(We)에 맞는 동사원형이므로"), ("watches", "-es형은 3인칭 단수 주어에 쓰므로"), ("to watch", "to부정사만으로는 동사 자리를 채울 수 없으므로"), ("is watch", "일반동사 앞에 be동사를 함께 쓸 수 없으므로"), ("watching", "-ing형만으로는 동사 자리를 채울 수 없으므로")], 1, "watchs", "watches")
# 7-57: 원문항의 ‘-’ 기호, C·D·E는 문장 순서를 바꿔 정답 꼴을 다르게
S757B = "발문에 ‘현재형으로’가 붙었고, 원문항에 있는 문장 앞의 ‘-’ 기호가 빠졌다. 원문항 발문으로 되돌리고 ‘-’를 붙였다."
S757C = " 또 다섯 유형의 정답이 모두 원문항과 같은 꼴(3인칭 단수형 - 동사원형)이어서, 두 문장의 순서를 바꿔 정답이 %s가 되게 했다. 보기는 그대로다."
def g757(t, p, good, why, a, s):
    cs = V(7, 57, t)["c"]; assert cs[a-1] == good, (t, cs, good)
    redo(57, t, pair2(cs, good, why, "두 문장의 주어에 맞는 현재형을 바르게 짝지었으므로"), a, R_V, s, st="R", p=p, okdup=True)
g757("B", "- My dog _______ fast.\n- I _______ fast.", "runs - run", ["3인칭 단수 주어 My dog에는 runs를 쓴다", "주어 I에는 동사원형 run을 쓴다"], 5, S757B + " 보기와 정답은 그대로다.")
g757("C", "- We _______ English.\n- Tom _______ English.", "study - studies", ["주어 We에는 동사원형 study를 쓴다", "3인칭 단수 주어 Tom에는 studies를 쓴다"], 1, S757B + S757C % "study - studies")
g757("D", "- We _______ dinner.\n- Dad _______ dinner.", "cook - cooks", ["주어 We에는 동사원형 cook을 쓴다", "3인칭 단수 주어 Dad에는 cooks를 쓴다"], 4, "발문에 ‘현재형으로’가 붙었다. 원문항 발문으로 되돌렸다." + S757C % "cook - cooks")
g757("E", "- They _______ TV.\n- Jane _______ TV.", "watch - watches", ["주어 They에는 동사원형 watch를 쓴다", "3인칭 단수 주어 Jane에는 watches를 쓴다"], 2, S757B + S757C % "watch - watches")
g757("F", "- Mina _______ home.\n- You _______ home.", "goes - go", ["3인칭 단수 주어 Mina에는 goes를 쓴다", "주어 You에는 동사원형 go를 쓴다"], 3, S757B + " 주어 Dad가 D와 겹쳐 Mina로 바꿨다. 보기와 정답은 그대로다.")
# 7-58 C: 정답 문장(Tom likes pizza.)이 원문항 ①(I likes pizza.)과 서술어가 같고 위치(④)도 같음
redo(58, "C", [("They <u>eats</u> lunch.", "주어 They에는 동사원형 eat을 써야 하므로"), ("She <u>watch</u> movies.", "3인칭 단수 주어 She에는 watches를 써야 하므로"), ("I <u>cleans</u> my room.", "주어 I에는 동사원형 clean을 써야 하므로"),
     ("My dad <u>drink</u> coffee.", "3인칭 단수 주어 My dad에는 drinks를 써야 하므로"), ("Tom <u>likes</u> chicken.", "3인칭 단수 주어 Tom에 likes를 바르게 썼으므로")], 5, R_V,
     S758 + " 정답 문장은 원문항 ①(I likes pizza.)과 서술어가 겹치지 않게 바꾸고, 정답 위치도 원문항(④)과 다르게 옮겼다.", st="R")
# 7-59 B: 오답이 짧은 일반론, 정답만 길고 구체적 / D: ⑤ 문구 / F: 말투
redo(59, "B", [("'game'이 사람이 아니라 물건이기 때문이다.", "목적어가 사람인지 물건인지는 동사의 형태와 관계없으므로"), ("'watch'는 ch로 끝나 s를 붙일 수 없는 동사이기 때문이다.", "ch로 끝나는 동사도 3인칭 단수 주어에는 watches로 쓰므로"), ("'보다'라는 뜻의 동사는 언제나 모양이 변하지 않기 때문이다.", "3인칭 단수 주어에는 watches로 모양이 바뀌므로"),
     ("주어 'You'는 he, she, it처럼 동사에 s를 붙이는 주어가 아니기 때문이다.", "주어 You 뒤에는 동사원형을 쓰므로"), ("문장이 짧으면 동사에 s를 붙이지 않기 때문이다.", "문장의 길이는 동사의 형태와 관계없으므로")], 4, R759,
     "오답이 문장과 관계없는 짧은 일반론(‘마침표가 있기 때문이다’ 등)이고 정답만 길고 구체적이어서 길이만으로 답이 드러났다. 정답 문구(‘주어 You가 2인칭 you이므로’)도 어색했고 정답 위치(②)가 원문항과 같았다. 원문항처럼 문장 속 낱말을 두고 말하는 오해로 오답을 새로 쓰고 정답 문구를 다듬었다.")
mk(7, 59, "D", [("주어 The students가 복수이므로 현재형 동사 study를 쓰기 때문이다.", "복수 주어에는 동사원형을 쓰므로"), ("library가 장소이기 때문이다.", "장소를 나타내는 말은 동사의 형태와 관계없으므로"), ("students 앞에 The가 있기 때문이다.", "The가 붙어도 단수 주어(The student)면 studies를 쓰므로"),
   ("문장 끝에 마침표가 있기 때문이다.", "문장 부호는 동사의 형태와 관계없으므로"), ("study는 주어와 관계없이 항상 같은 모양으로 쓰는 동사이기 때문이다.", "3인칭 단수 주어에는 studies로 모양이 바뀌므로")], 1, R759,
   "⑤의 문구(‘항상 같은 형태라는 설명이기 때문이다’)가 말이 되지 않아 다듬었다. 나머지 보기와 정답은 그대로다.")
redo(59, "F", [("'this book'이 한 권이기 때문이다.", OBJ), ("read는 과거형과 모양이 같아서 s를 붙이지 않기 때문이다.", "3인칭 단수 주어에는 reads로 쓰므로"), ("주어 We가 나를 포함한 여러 명(복수)이기 때문이다.", "주어 We에는 동사원형을 쓰므로"),
     ("this가 붙은 목적어 앞의 동사는 원형이기 때문이다.", "목적어 앞의 this는 동사의 형태와 관계없으므로"), ("We가 짧은 낱말이기 때문이다.", "주어의 길이는 동사의 형태와 관계없으므로")], 3, R759, S759 + " 보기의 말투는 원문항처럼 ‘~때문이다.’로 맞췄다.")
# 7-60 C: 정답 위치가 B·C·E 모두 ② → ②와 ③의 순서를 바꿈
redo(60, "C", [("Tom not study English.", "not만 넣지 않고 doesn't + 동사원형으로 부정문을 만들므로"), ("Tom isn't study English.", "일반동사의 부정문에는 be동사(isn't)를 쓰지 않으므로"), ("Tom doesn't study English.", "doesn't 뒤에 동사원형을 써서 부정문을 바르게 만들었으므로"),
     ("Tom don't study English.", "3인칭 단수 주어(Tom)에는 don't가 아니라 doesn't를 쓰므로"), ("Tom does not studies English.", "doesn't/does not 뒤에는 -s를 뗀 동사원형을 써야 하므로")], 3, R760,
     "발문의 ‘부정문(..하지 않는다)으로’가 ‘현재형 부정문으로’로 바뀌었다. 원문항 발문으로 되돌렸다. 또 정답 위치가 B·C·E 모두 ②여서 ②와 ③의 순서를 바꿨다.", st="R")
