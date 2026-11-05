# 7급 CH1 명사의 종류·수 (1~10) 수정 예시
# 7급 변형 해설은 '판단 기준: 지정한 …'과 영어 단어 뒤 조사 오류가 있어, 발문만 되돌리는 문항도 해설을 새로 쓴다.

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 7-1 셀 수 없는 명사: 원문항 발문, 원문항처럼 뜻 괄호 없이
R701 = "셀 수 있는 명사는 a/an을 붙이거나 복수형으로 쓸 수 있다. 물질(bread, rice, milk, water, money)이나 추상적인 것(love)을 나타내는 명사는 셀 수 없어 a/an을 붙이지 않고 복수형도 쓰지 않는다."
S701 = "발문이 ‘괄호에 제시된 일반적인 뜻으로 쓸 때’로 바뀌고 선택지마다 우리말 뜻이 붙었다. 원문항 발문과 선택지 형식으로 되돌렸다."
CT = lambda w: f"{w}: 하나, 둘로 셀 수 있는 명사이므로"; UC = lambda w: f"{w}: 물질을 나타내는 셀 수 없는 명사이므로"
def f701(t, words, a, s=S701 + " 정답은 그대로다."):
    mk(7, 1, t, [(w, UC(w) if i + 1 == a else CT(w)) for i, w in enumerate(words)], a, R701, s, st="R")
f701("B", ["pen", "rabbit", "bread", "table", "egg"], 3)
f701("C", ["bag", "box", "rice", "banana", "bird"], 3)
f701("D", ["milk", "pencil", "orange", "chair", "dog"], 1)
f701("E", ["watch", "money", "teacher", "apple", "car"], 2)
f701("F", ["rabbit", "bicycle", "cookie", "water", "teacher"], 4, S701 + " 7급 수준에 어려운 furniture를 water로 바꿨다.")

# 7-2 대문자로 시작하는 말: 원문항 발문
R702 = "사람 이름, 나라·도시 이름, 요일, 달 이름 같은 고유명사는 문장 어디에서든 첫 글자를 대문자로 쓴다. 일반 명사는 문장 첫머리가 아니면 소문자로 쓴다."
S702 = "발문이 ‘문장 중간에서도 첫 글자를 대문자로 써야 하는 단어’로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
PR = lambda w, k: f"{w}: {k} 이름이라 대문자로 시작해야 하므로"; CM = lambda w: f"{w}: 일반 명사라 소문자로 써도 되므로"
def f702(t, words, a, kind):
    mk(7, 2, t, [(w, PR(w, kind) if i + 1 == a else CM(w)) for i, w in enumerate(words)], a, R702, S702, st="R")
f702("B", ["hospital", "river", "student", "music", "friday"], 5, "요일")
f702("C", ["milk", "bag", "girl", "park", "jane"], 5, "사람")
f702("D", ["january", "boy", "dog", "rice", "room"], 1, "달")
f702("E", ["book", "student", "korea", "water", "school"], 3, "나라")
f702("F", ["cat", "teacher", "desk", "music", "monday"], 5, "요일")

# 7-3 밑줄 수량 표현: 원문항 발문과 밑줄, 유형마다 서로 다른 오류
R703 = "셀 수 없는 명사(water, rice, bread, milk, homework)는 some과 함께 쓰고 복수형으로 쓰지 않는다. 셀 수 있는 명사는 two, four, many 뒤에서 복수형으로 쓴다."
S703 = "발문이 ‘명사의 수량 표현’으로 바뀌고 조건 ‘(음식·물질은 … 일반적인 뜻으로 판단합니다.)’가 붙었으며 원문항의 밑줄이 사라졌다. 원문항 발문과 밑줄로 되돌렸다."
UN = lambda w: f"셀 수 없는 명사({w})를 some과 함께 바르게 썼으므로"; PLN = lambda w: f"셀 수 있는 명사를 복수형({w})으로 바르게 썼으므로"
def f703(t, items, a, s=S703):
    mk(7, 3, t, items, a, R703, s, st="R")
f703("B", [("She needs <u>some water</u>.", UN("water")), ("He eats <u>some rice</u>.", UN("rice")), ("They have <u>two boxes</u>.", PLN("boxes")), ("I like <u>apples</u>.", PLN("apples")), ("He has <u>five rices</u>.", "rice는 셀 수 없는 명사라 복수형으로 쓰지 않으므로")], 5, S703 + " 보기와 정답은 그대로다.")
f703("C", [("He drinks <u>some milk</u>.", UN("milk")), ("We eat <u>some cheese</u>.", UN("cheese")), ("We eat <u>two breads</u>.", "bread는 셀 수 없는 명사라 복수형으로 쓰지 않으므로"), ("I have <u>four pencils</u>.", PLN("pencils")), ("They like <u>bananas</u>.", PLN("bananas"))], 3,
     S703 + " some bread와 two breads가 짝을 이뤄 대비 단서가 되지 않도록 한 문장을 cheese로 바꿨다.")
f703("D", [("I have <u>two homeworks</u> today.", "homework는 셀 수 없는 명사라 복수형으로 쓰지 않으므로"), ("I drank <u>some juice</u>.", UN("juice")), ("We need <u>some water</u>.", UN("water")), ("They saw <u>many birds</u>.", PLN("birds")), ("He bought <u>three notebooks</u>.", PLN("notebooks"))], 1,
     S703 + " 7급 수준을 넘는 advice·information을 homework·water로 바꿨다.")
f703("E", [("They want <u>some bread</u>.", UN("bread")), ("She likes <u>oranges</u>.", PLN("oranges")), ("They need <u>four pencil</u>.", "셀 수 있는 명사 pencil은 four 뒤에서 복수형 pencils로 써야 하므로"), ("We drink <u>some milk</u>.", UN("milk")), ("I have <u>five pens</u>.", PLN("pens"))], 3,
     S703 + " 정답(four moneys)이 원문항 정답(three moneys)과 사실상 같아, 셀 수 있는 명사의 복수형 오류로 바꿨다.")
f703("F", [("She has <u>three books</u>.", PLN("books")), ("He likes <u>oranges</u>.", PLN("oranges")), ("Mom buys <u>some cheese</u>.", UN("cheese")), ("I eat <u>some rice</u>.", UN("rice")), ("She has <u>many book</u>.", "셀 수 있는 명사 book은 many 뒤에서 복수형 books로 써야 하므로")], 5,
     S703 + " 조건 없이는 ‘우유 세 잔’으로도 읽히는 three milks를 셀 수 있는 명사의 복수형 오류로 바꿨다.")

# 7-4 복수형이 잘못된 것: B는 원문항과 다른 정답, C는 같은 명사 반복 없애기
R704 = "복수형은 대부분 -s를 붙이고, s·sh·ch·x로 끝나면 -es(buses, foxes), 자음 + y는 y를 i로 바꾸고 -es(ladies, babies)를 붙인다."
OKP = lambda w, why: f"{w}: {why} 바르게 썼으므로"
mk(7, 4, "B", [("bag - bags", OKP("bags", "-s를 붙여")), ("bus - buss", "bus는 s로 끝나 -es를 붙여 buses로 써야 하므로"), ("class - classes", OKP("classes", "s로 끝나 -es를 붙여")), ("apple - apples", OKP("apples", "-s를 붙여")), ("fox - foxes", OKP("foxes", "x로 끝나 -es를 붙여"))], 2, R704,
   "정답 짝(dish - dishs)과 위치(④), watch - watches가 원문항과 같았다. 원문항에 없는 명사로 정답과 오답을 바꾸고 정답 위치도 옮겼다.")
mk(7, 4, "C", [("city - cities", OKP("cities", "자음 + y라 y를 i로 바꾸고 -es를 붙여")), ("lady - ladies", OKP("ladies", "자음 + y라 y를 i로 바꾸고 -es를 붙여")), ("chair - chairs", OKP("chairs", "-s를 붙여")), ("dog - dogs", OKP("dogs", "-s를 붙여")), ("baby - babys", "baby는 자음 + y라 y를 i로 바꾸고 -es를 붙여 babies로 써야 하므로")], 5, R704,
   "baby가 ②와 ⑤에 두 번 나와 둘 중 하나가 답이라는 단서가 되었다. ②를 lady - ladies로 바꿨다.")

# 7-7 문법적으로 자연스러운 문장: 원문항 발문, D는 원문항과 다른 명사로
R707 = "셀 수 없는 명사는 a/an을 붙이지 않고 복수형으로도 쓰지 않는다. 일반적으로 말할 때는 명사만 쓴다(I like milk.)."
S707 = "발문이 ‘문맥에 가장 알맞은 문장’으로 바뀌고 ‘(특정 종류·개수·주문 단위가 아니라 … 일반적으로 말합니다.)’ 조건이 붙었다. 원문항 발문으로 되돌렸다."
def f707(t, w, forms, a, s=S707 + " 보기와 정답은 그대로다."):
    why = {f"I like {w}.": f"셀 수 없는 명사({w})를 a/an이나 복수형 없이 바르게 썼으므로"}
    items = []
    for f_ in forms:
        if f_ in why: items.append((f_, why[f_]))
        elif " a " in f_ or " an " in f_ or f_.startswith(("I like a ", "I like an ", "We need a ", "We need an ")): items.append((f_, f"셀 수 없는 명사({w}) 앞에는 a/an을 쓰지 않으므로"))
        else: items.append((f_, f"셀 수 없는 명사({w})는 복수형으로 쓰지 않으므로"))
    mk(7, 7, t, items, a, R707, s, st="R")
f707("B", "money", ["I like a money.", "I like an money.", "I like moneys.", "I like money.", "I like two moneys."], 4)
f707("E", "milk", ["I like an milk.", "I like milks.", "I like milk.", "I like a milk.", "I like two milks."], 3)
f707("F", "rice", ["I like an rice.", "I like rice.", "I like rices.", "I like two rices.", "I like a rice."], 2)
f707("D", "water", ["I like a water.", "I like water.", "I like waters.", "I like an water.", "I like two waters."], 2, S707 + " 선택지가 원문항(breads/a bread/an bread/bread)과 거의 같아 명사를 water로 바꾸고 정답 위치도 옮겼다.")
mk(7, 7, "C", [("We need informations.", "셀 수 없는 명사 information은 복수형으로 쓰지 않으므로"), ("We need two informations.", "셀 수 없는 명사 information은 복수형으로 쓰지 않으므로"), ("We need information.", "셀 수 없는 명사 information을 a/an이나 복수형 없이 바르게 썼으므로"),
     ("We need a informations.", "셀 수 없는 명사 앞에 a를 쓰지 않고 복수형으로도 쓰지 않으므로"), ("We need an information.", "셀 수 없는 명사 information 앞에는 an을 쓰지 않으므로")], 3, R707, S707 + " 보기와 정답은 그대로다.", st="R")

# 7-8 (A)(B) 복수형: 발문 조건 삭제
R708 = "two, four 같은 수 뒤의 셀 수 있는 명사는 복수형으로 쓴다. -s를 붙이되 s·sh·ch·x로 끝나면 -es, 자음 + y는 y를 i로 바꾸고 -es를 붙인다."
S708 = "발문에 ‘(A에는 …, B에는 …의 복수형을 씁니다.)’ 조건이 붙었다. 조건을 지워 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
def f708(t, ga, gb, wa, wb):
    V_ = V(7, 8, t); items = []
    for ch in V_["c"]:
        a_, b_ = [re.sub(r"\([AB]\) ", "", x).strip() for x in ch.split(" - ")]
        bits = []
        if a_ != ga: bits.append(f"(A): {wa}")
        if b_ != gb: bits.append(f"(B): {wb}")
        items.append((ch, (", ".join(bits) + "") if bits else f"(A)와 (B)에 알맞은 복수형을 바르게 썼으므로"))
    mk(7, 8, t, items, int(V_["ans"]), R708, S708, st="R", okdup=True)
import re
f708("B", "bags", "classes", "two 뒤에는 복수형 bags를 쓰므로", "class는 s로 끝나 -es를 붙여 classes로 쓰므로")
f708("C", "dogs", "watches", "two 뒤에는 복수형 dogs를 쓰므로", "watch는 ch로 끝나 -es를 붙여 watches로 쓰므로")
f708("D", "books", "dishes", "two 뒤에는 복수형 books를 쓰므로", "dish는 sh로 끝나 -es를 붙여 dishes로 쓰므로")
f708("E", "apples", "buses", "two 뒤에는 복수형 apples를 쓰므로", "bus는 s로 끝나 -es를 붙여 buses로 쓰므로")
f708("F", "babies", "watches", "three 뒤에는 복수형 babies를 쓰고, baby는 y를 i로 바꾸고 -es를 붙이므로", "watch는 ch로 끝나 -es를 붙여 watches로 쓰므로")


# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, r, s, **kw):
    FIX.pop((7, n, t), None)
    mk(7, n, t, items, a, r, s, **kw)
# 7-2 F: 정답의 종류(요일 이름)와 위치가 B와 같음 → 언어 이름으로
redo(2, "F", [("cat", CM("cat")), ("english", PR("english", "언어")), ("teacher", CM("teacher")), ("desk", CM("desk")), ("music", CM("music"))], 2, R702,
     "발문이 ‘문장 중간에서도 첫 글자를 대문자로 써야 하는 단어’로 바뀌었고, 정답의 종류(요일 이름)와 위치(⑤)가 B와 같았다. 원문항 발문으로 되돌리고 정답을 언어 이름으로 바꿨다.", st="R")
# 7-3 B: 보기 세 개가 원문항 문장에서 주어만 바꾼 것, some rice / five rices 쌍 / E: ①이 원문항 ⑤와 거의 같음
f703_ = lambda t, items, a, s: (FIX.pop((7, 3, t), None), f703(t, items, a, s))
f703_("B", [("She drinks <u>some tea</u>.", UN("tea")), ("He eats <u>some soup</u>.", UN("soup")), ("They have <u>two dogs</u>.", PLN("dogs")), ("I like <u>grapes</u>.", PLN("grapes")), ("He has <u>five rices</u>.", "rice는 셀 수 없는 명사라 복수형으로 쓰지 않으므로")], 5,
      S703 + " 보기 세 개(some water, two boxes, apples)가 원문항 문장에서 주어만 바꾼 것이었고, some rice와 five rices가 짝을 이뤄 대비 단서가 되어 다른 문장으로 바꿨다. 정답은 그대로다.")
f703_("E", [("They want <u>some soup</u>.", UN("soup")), ("She likes <u>oranges</u>.", PLN("oranges")), ("They need <u>four pencil</u>.", "셀 수 있는 명사 pencil은 four 뒤에서 복수형 pencils로 써야 하므로"), ("We drink <u>some milk</u>.", UN("milk")), ("I have <u>five pens</u>.", PLN("pens"))], 3,
      S703 + " 정답(four moneys)이 원문항 정답(three moneys)과 사실상 같아 셀 수 있는 명사의 복수형 오류로 바꾸고, 원문항 ⑤와 거의 같던 ①(They want some bread.)도 바꿨다.")
# 7-4 D·F: 정답이 원문항 보기의 틀린 꼴(box - boxs, watch - watchs)이고 원문항과 같은 짝이 있음
redo(4, "D", [("peach - peaches", OKP("peaches", "ch로 끝나 -es를 붙여")), ("book - books", OKP("books", "-s를 붙여")), ("bench - benchs", "bench는 ch로 끝나 -es를 붙여 benches로 써야 하므로"), ("girl - girls", OKP("girls", "-s를 붙여")), ("glass - glasses", OKP("glasses", "s로 끝나 -es를 붙여"))], 3, R704,
     "정답(box - boxs)이 원문항 ②(box - boxes)의 틀린 꼴이었고, watch - watches는 원문항 ①과 같으며 dish - dishes는 원문항 정답을 바르게 고친 짝이었다. 원문항에 없는 명사로 새로 썼다. 정답 위치는 그대로다.")
redo(4, "F", [("brush - brushs", "brush는 sh로 끝나 -es를 붙여 brushes로 써야 하므로"), ("toy - toys", OKP("toys", "모음 + y라 -s만 붙여")), ("dress - dresses", OKP("dresses", "s로 끝나 -es를 붙여")), ("pen - pens", OKP("pens", "-s를 붙여")), ("sandwich - sandwiches", OKP("sandwiches", "ch로 끝나 -es를 붙여"))], 1, R704,
     "정답(watch - watchs)이 원문항 ①(watch - watches)의 틀린 꼴이었고 box - boxes는 원문항 ②와 같았다. 원문항에 없는 명사로 새로 썼다. 정답 위치는 그대로다.")
# 7-5 B~F: 발문의 (A에는 …, B에는 …의 복수형을 씁니다.) 조건 삭제(7-8과 같게), 잘린 꼴 오답(fee, wome, me, fis) 교체
R705 = "불규칙 복수형: foot - feet, tooth - teeth, goose - geese, man - men, woman - women, child - children, mouse - mice, person - people. sheep, fish, deer는 단수와 복수가 같다."
S705 = "발문에 ‘(A에는 …, B에는 …의 복수형을 씁니다.)’가 붙어 있었다. 조건을 지워 원문항 발문으로 되돌렸다."
def f705(t, ga, gb, wa, wb, repl=None, extra=" 보기와 정답은 그대로다."):
    V_ = V(7, 5, t); items = []; cs = list(V_["c"])
    if repl: cs[repl[0]] = repl[1]
    for ch in cs:
        a_, b_ = [x.strip() for x in ch.split(" - ")]
        bits = []
        if a_ != ga: bits.append(f"(A): {wa}")
        if b_ != gb: bits.append(f"(B): {wb}")
        items.append((ch, ", ".join(bits) if bits else "(A)와 (B)에 알맞은 복수형을 바르게 썼으므로"))
    a = [i for i, ch in enumerate(cs) if ch.replace(" ", "") == f"{ga}-{gb}"][0] + 1
    redo(5, t, items, a, R705, S705 + extra, st="R", okdup=True)
f705("B", "feet", "mice", "foot의 복수형은 feet이므로", "mouse의 복수형은 mice이므로", (3, "foots - mice"), " 뜻이 통하지 않는 오답(fee)은 foots로 바꿨다. 정답은 그대로다.")
f705("C", "women", "teeth", "woman의 복수형은 women이므로", "tooth의 복수형은 teeth이므로", (2, "woman - teeth"), " 없는 형태의 오답(wome)은 단수형 woman으로 바꿨다. 정답은 그대로다.")
f705("D", "men", "children", "man의 복수형은 men이므로", "child의 복수형은 children이므로", (2, "man - children"), " 뜻이 통하지 않는 오답(me)은 단수형 man으로 바꿨다. 정답은 그대로다.")
f705("E", "fish", "people", "fish는 단수와 복수가 같으므로", "person의 복수형은 people이므로", (4, "fish - person"), " 없는 형태의 오답(fis)은 단수형 person을 쓴 보기로 바꿨다. 정답은 그대로다.")
f705("F", "mice", "deer", "mouse의 복수형은 mice이므로", "deer는 단수와 복수가 같으므로")
# 7-6 B·D·E·F: 제시 문장(I have two ____.)이 원문항과 똑같음 → 문장을 새로
R706 = "two, three, many처럼 둘 이상을 나타내는 말 뒤에는 명사의 복수형을 쓴다. 대부분 -s, s·sh·ch·x로 끝나면 -es, 자음 + y는 -ies를 붙인다."
S706 = "제시 문장(I have two ____.)이 원문항과 똑같았다. 제시 문장을 새로 썼다. 보기와 정답은 그대로다."
def f706(t, p, num, good, items, a):
    redo(6, t, [(w, why) for w, why in items], a, R706, S706, p=p)
f706("B", "There are three _______ on the desk.", "three", "books", [("books", "three 뒤에 복수형 books를 바르게 썼으므로"), ("bookses", "bookses라는 형태는 없으므로"), ("book", "three 뒤에 단수형을 쓸 수 없으므로"), ("bookes", "book에는 -s만 붙여 books로 쓰므로"), ("a book", "three 뒤에 a를 쓸 수 없으므로")], 1)
f706("D", "My dad has two _______.", "two", "watches", [("watch", "two 뒤에 단수형을 쓸 수 없으므로"), ("a watch", "two 뒤에 a를 쓸 수 없으므로"), ("watchies", "watchies라는 형태는 없으므로"), ("watchs", "watch는 ch로 끝나 -es를 붙여야 하므로"), ("watches", "ch로 끝나 -es를 붙인 복수형을 바르게 썼으므로")], 5)
f706("E", "I can see two _______ in the room.", "two", "babies", [("babys", "baby는 자음 + y라 y를 i로 바꾸고 -es를 붙여야 하므로"), ("baby", "two 뒤에 단수형을 쓸 수 없으므로"), ("babies", "y를 i로 바꾸고 -es를 붙인 복수형을 바르게 썼으므로"), ("babyes", "y를 i로 바꾸지 않았으므로"), ("a baby", "two 뒤에 a를 쓸 수 없으므로")], 3)
f706("F", "We need five _______.", "five", "boxes", [("box", "five 뒤에 단수형을 쓸 수 없으므로"), ("boxies", "boxies라는 형태는 없으므로"), ("boxes", "x로 끝나 -es를 붙인 복수형을 바르게 썼으므로"), ("a box", "five 뒤에 a를 쓸 수 없으므로"), ("boxs", "box는 x로 끝나 -es를 붙여야 하므로")], 3)
# 7-7 C: 7급 수준을 넘는 information → salt
redo(7, "C", [("We need salts.", "셀 수 없는 명사 salt는 복수형으로 쓰지 않으므로"), ("We need two salts.", "셀 수 없는 명사 salt는 복수형으로 쓰지 않으므로"), ("We need salt.", "셀 수 없는 명사 salt를 a/an이나 복수형 없이 바르게 썼으므로"),
     ("We need a salts.", "셀 수 없는 명사 앞에 a를 쓰지 않고 복수형으로도 쓰지 않으므로"), ("We need an salt.", "셀 수 없는 명사 salt 앞에는 an을 쓰지 않으므로")], 3, R707, S707 + " 7급 수준을 넘는 information을 salt로 바꿨다(7-3 D와 같은 기준).", st="R")
# 7-8 B~E: 제시 문장(I have two (A) and four (B).)이 원문항과 똑같음, B는 (A)의 낱말(bag)도 같음 / F: 보기에 (A)·(B) 표지 없음
S708B = "발문에 ‘(A에는 …, B에는 …의 복수형을 씁니다.)’ 조건이 붙었고, 제시 문장(I have two (A)___ and four (B)___.)이 원문항과 똑같았다. 조건을 지워 원문항 발문으로 되돌리고 제시 문장을 새로 썼다."
def g708(t, p, ga, gb, wa, wb, chs, a, s=S708B):
    items = []
    for ca, cb in chs:
        bits = []
        if ca != ga: bits.append(f"(A): {wa}")
        if cb != gb: bits.append(f"(B): {wb}")
        items.append((f"(A) {ca} - (B) {cb}", ", ".join(bits) if bits else "(A)와 (B)에 알맞은 복수형을 바르게 썼으므로"))
    redo(8, t, items, a, R708, s, st="R", p=p, okdup=True)
g708("B", "She has three (A)_______ and two (B)_______.", "pens", "classes", "three 뒤에는 복수형 pens를 쓰므로", "class는 s로 끝나 -es를 붙여 classes로 쓰므로",
     [("pen", "classes"), ("pens", "class"), ("pen", "class"), ("pens", "classes"), ("pens", "classs")], 4, S708B + " (A)의 낱말(bag)도 원문항과 같아 pen으로 바꿨다.")
g708("C", "My uncle has five (A)_______ and three (B)_______.", "dogs", "watches", "five 뒤에는 복수형 dogs를 쓰므로", "watch는 ch로 끝나 -es를 붙여 watches로 쓰므로",
     [("dog", "watches"), ("dog", "watch"), ("dogs", "watch"), ("dogs", "watchs"), ("dogs", "watches")], 5)
g708("D", "We need ten (A)_______ and six (B)_______.", "books", "dishes", "ten 뒤에는 복수형 books를 쓰므로", "dish는 sh로 끝나 -es를 붙여 dishes로 쓰므로",
     [("books", "dishs"), ("books", "dishes"), ("book", "dish"), ("book", "dishes"), ("books", "dish")], 2, S708B + " 정답 위치가 원문항·C와 같은 ⑤여서 보기 순서도 바꿨다.")
g708("E", "I can see four (A)_______ and two (B)_______.", "apples", "buses", "four 뒤에는 복수형 apples를 쓰므로", "bus는 s로 끝나 -es를 붙여 buses로 쓰므로",
     [("apples", "buss"), ("apple", "bus"), ("apples", "buses"), ("apples", "bus"), ("apple", "buses")], 3)
g708("F", "There are three (A)_______ and two (B)_______ in the room.", "babies", "watches", "three 뒤에는 복수형 babies를 쓰고, baby는 y를 i로 바꾸고 -es를 붙이므로", "watch는 ch로 끝나 -es를 붙여 watches로 쓰므로",
     [("babys", "watchs"), ("baby", "watches"), ("babies", "watchs"), ("babies", "watches"), ("baby", "watch")], 4,
     "발문에 ‘(A에는 …, B에는 …의 복수형을 씁니다.)’ 조건이 붙었고, 보기에 원문항의 (A)·(B) 표지가 없었다. 조건을 지워 원문항 발문으로 되돌리고 보기에 (A)·(B)를 붙였다. 정답은 그대로다.")
# 7-9 C~F: 제시 문장이 원문항 틀(Mina has (A) ~, (B) ~, and (C) ~.)에서 명사만 바꾼 것 → 문장을 새로
R709 = "a/an은 뒤에 오는 낱말의 첫소리로 정한다. 모음 소리(a, e, i, o, u 소리)로 시작하면 an, 자음 소리로 시작하면 a를 쓴다."
S709 = "제시 문장이 원문항의 틀(Mina has (A) ~, (B) ~, and (C) ~.)에서 명사만 바꾼 것이었다. 문장을 새로 썼다."
def f709(t, p, nouns, good, chs, a, s=S709):
    gs = good.split(" - "); items = []
    for ch in chs:
        xs = ch.split(" - ")
        bad = [i for i in range(3) if xs[i] != gs[i]]
        bits = [f"({'ABC'[i]}) {'모음' if gs[i] == 'an' else '자음'} 소리로 시작하는 낱말({nouns[i]}) 앞에는 {gs[i]}" for i in bad]
        items.append((ch, (", ".join(bits) + ("이" if gs[bad[-1]] == "an" else "가") + " 와야 하므로") if bits else "세 빈칸 모두 첫소리에 맞는 a/an을 골랐으므로"))
    redo(9, t, items, a, R709, s, p=p)
f709("C", "There is (A)_______ onion, (B)_______ carrot, and (C)_______ tomato in the basket.", ["onion", "carrot", "tomato"], "an - a - a",
     ["a - a - an", "an - an - a", "a - a - a", "an - a - a", "an - a - an"], 4, S709 + " 정답 조합(an - a - an)이 B와 같아 조합도 바꿨다.")
f709("D", "Tom draws (A)_______ ant, (B)_______ owl, and (C)_______ fox.", ["ant", "owl", "fox"], "an - an - a", ["a - a - a", "a - a - an", "a - an - a", "an - an - a", "an - a - an"], 4, S709 + " 보기와 정답은 그대로다.")
f709("E", "My sister needs (A)_______ notebook, (B)_______ ruler, and (C)_______ eraser.", ["notebook", "ruler", "eraser"], "a - a - an", ["an - a - an", "a - a - an", "a - a - a", "a - an - a", "an - an - a"], 2, S709 + " 정답 위치가 D와 겹치지 않게 보기 순서도 바꿨다.")
f709("F", "We saw (A)_______ tiger, (B)_______ elephant, and (C)_______ eagle at the zoo.", ["tiger", "elephant", "eagle"], "a - an - an", ["a - a - a", "an - a - an", "a - an - a", "an - an - a", "a - an - an"], 5, S709 + " 정답 위치도 옮겼다.")
# 7-10 B~F: 틀린 설명과 정반대인 옳은 설명이 함께 있고 진술이 원문항의 절반 길이 → 원문항 길이의 설명으로, 정반대 짝 없이
R710 = "주어가 I, you, 복수이면 have, 나나 너가 아닌 한 명(he, she, 사람 이름)이면 has를 쓴다. a/an은 뒤 낱말의 첫소리(자음 소리 a, 모음 소리 an)로 정하고, 둘 이상이면 복수형을 쓴다."
S710 = "틀린 설명과 정반대인 옳은 설명이 함께 있어 둘만 견주면 답이 나왔고, 진술이 원문항의 절반 길이였다. 원문항처럼 두 문장을 짚는 설명으로 새로 쓰고 정반대 짝을 없앴다."
def f710(t, items, a):
    FIX.pop((7, 10, t), None)
    F(7, 10, t, c=[x for x, _ in items], a=a, r=R710, k=items[a-1][1], n=[w + (" 틀린 설명이다. 따라서 정답이다." if i + 1 == a else " 옳은 설명이다. 따라서 오답이다.") for i, (_, w) in enumerate(items)], s=S710 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f710("B", [("지수: (가)의 주어 'She'를 'We'로 바꿔도 동사는 'has'를 그대로 써야 해.", "주어가 We이면 have를 써야 하므로"), ("성진: (나)에서 box는 x로 끝나기 때문에 복수형을 만들 때 -es를 붙여 boxes가 됐어.", "x로 끝나는 명사는 -es를 붙이므로"),
           ("준호: (가)에서 has를 쓴 것은 주어 'She'가 3인칭 단수이기 때문이야.", "3인칭 단수 주어에는 has를 쓰므로"), ("민아: (나)에서 two는 상자가 두 개라는 뜻이라서 뒤에 복수형이 왔어.", "둘 이상을 나타내는 말 뒤에는 복수형을 쓰므로"),
           ("민수: (가)의 umbrella는 모음 소리로 시작하기 때문에 a가 아닌 an을 썼어.", "모음 소리 앞에는 an을 쓰므로")], 1)
f710("C", [("지수: (나)의 주어 'Tom'은 나나 너가 아닌 한 명이라서 has를 썼어.", "3인칭 단수 주어에는 has를 쓰므로"), ("준호: (가)의 book은 자음 소리로 시작하기 때문에 앞에 a를 썼어.", "자음 소리 앞에는 a를 쓰므로"),
           ("민수: (나)의 orange를 banana로 바꿔도 앞의 an은 그대로 써야 해.", "banana는 자음 소리로 시작해 a banana로 써야 하므로"), ("민아: (가)에서 'a'는 책이 한 권이라는 뜻을 나타내.", "a/an은 ‘하나’를 나타내므로"),
           ("성진: (나)의 orange가 두 개라면 an 대신 two를 쓰고 oranges라고 써야 해.", "둘 이상이면 수를 나타내는 말과 복수형을 쓰므로")], 3)
f710("D", [("성진: (나)의 knives는 knife의 fe를 v로 바꾸고 -es를 붙인 복수형이야.", "fe로 끝나는 명사는 fe를 v로 바꾸고 -es를 붙이므로"), ("민아: (가)의 'She' 자리에 'My sister'가 와도 동사는 has를 써.", "My sister도 3인칭 단수 주어라 has를 쓰므로"),
           ("지수: (가)의 hour는 h가 소리 나지 않고 모음 소리로 시작해서 an을 썼어.", "모음 소리 앞에는 an을 쓰므로"), ("준호: (나)에서 two 뒤에는 복수형이 와야 해서 knife를 그대로 쓸 수 없어.", "둘 이상을 나타내는 말 뒤에는 복수형을 쓰므로"),
           ("민수: (나)의 주어 'They'를 'He'로 바꿔도 동사 'have'는 그대로 써야 문법에 맞아.", "주어가 He이면 has를 써야 하므로")], 5)
f710("E", [("성진: (나)의 water는 셀 수 없는 명사라서 앞에 a를 쓰지 않고 some을 썼어.", "셀 수 없는 명사에는 a/an을 쓰지 않으므로"), ("민아: (가)의 pencil이 두 자루가 되면 'a pencils'라고 쓰면 돼.", "둘 이상이면 a를 쓰지 않고 two pencils라고 써야 하므로"),
           ("준호: (가)의 주어 'He'를 'Tom'으로 바꿔도 has를 그대로 써.", "Tom도 3인칭 단수 주어라 has를 쓰므로"), ("민수: (가)의 pencil은 자음 소리로 시작하기 때문에 앞에 a를 썼어.", "자음 소리 앞에는 a를 쓰므로"),
           ("지수: (나)의 주어 'They'는 여러 명이라서 have를 썼어.", "복수 주어에는 have를 쓰므로")], 2)
f710("F", [("준호: (가)의 egg는 모음 소리로 시작하기 때문에 a가 아닌 an을 썼어.", "모음 소리 앞에는 an을 쓰므로"), ("지수: (나)에서 two 뒤에는 복수형이 와야 해서 book에 -s를 붙였어.", "둘 이상을 나타내는 말 뒤에는 복수형을 쓰므로"),
           ("민수: (나)에서는 주어가 'Jane' 한 명이라서 have가 아닌 has를 썼어.", "3인칭 단수 주어에는 has를 쓰므로"), ("성진: (나)의 주어 'Jane'을 'I'로 바꾸면 'I has two books.'라고 써야 해.", "주어가 I이면 have를 써야 하므로"),
           ("민아: (가)에서 'an'은 달걀이 하나라는 뜻을 나타내.", "a/an은 ‘하나’를 나타내므로")], 4)
