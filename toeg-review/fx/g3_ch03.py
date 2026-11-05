# 3급 CH3 명사와 관사 (21~30) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def talk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[w + (" 옳지 않은 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.") for i, (_, w) in enumerate(items)], k=items[a-1][1], s=s + ipos(a), **kw)

# 3-21 B: 원문항과 같던 정답(a loaf of)을 다른 명사·단위로
mk(3, 21, "B", [("a loaf of", "a loaf of: 빵 덩어리를 세는 말이라 수프와 맞지 않으므로"), ("a bowl of", "a bowl of: 수프 한 그릇을 나타내므로"), ("a sheet of", "a sheet of: 종이처럼 얇은 것을 세는 말이라 맞지 않으므로"),
                ("a slice of", "a slice of: 얇게 썬 조각을 세는 말이라 수프와 맞지 않으므로"), ("a pair of", "a pair of: 짝을 이루는 물건을 세는 말이라 맞지 않으므로")], 2,
   "셀 수 없는 명사는 a/an이나 숫자를 바로 붙이지 않고 a bowl of, a glass of, a loaf of 같은 단위 표현으로 수량을 나타낸다.",
   "정답(a loaf of)과 선택지 네 개가 원문항과 같았다. 명사와 단위를 ‘수프 한 그릇(a bowl of soup)’으로 바꿨다.", p="수프 한 그릇을 원해요.\nI'd like _____ soup, please.")

# 3-22 셀 수 있는 명사: 원문항 발문, 조건 없이도 판단되는 명사로
ST22 = "다음 중 셀 수 있는 명사를 고르시오."
R22 = "셀 수 있는 명사는 a/an·숫자와 함께 쓰고 복수형을 만들 수 있다. information, news, furniture, advice, homework, luggage, weather 같은 명사는 셀 수 없는 명사라 a/an이나 -s를 붙이지 않는다."
def U(nn): return f"{nn}: 셀 수 없는 명사라 a/an이나 복수형을 쓰지 않으므로"
def C(nn): return f"{nn}: a/an과 함께 쓰고 복수형을 만들 수 있는 셀 수 있는 명사이므로"
S22 = "발문에 ‘기본 의미, 물질명사는 물질 자체’ 등 긴 조건이 붙었다. 원문항 발문으로 되돌리고, 조건 없이도 판단되도록 water·bread·juice처럼 뜻에 따라 셀 수도 있는 물질명사를 늘 셀 수 없는 명사로 바꿨다."
mk(3, 22, "B", [("homework", U("homework")), ("luggage", U("luggage")), ("pencil", C("pencil")), ("weather", U("weather")), ("knowledge", U("knowledge"))], 3, R22,
   S22 + " 정답(car)이 원문항과 같아 pencil로 바꿨다.", st=ST22)
mk(3, 22, "C", [("music", U("music")), ("homework", U("homework")), ("traffic", U("traffic")), ("equipment", U("equipment")), ("apple", C("apple"))], 5, R22, S22, st=ST22)
mk(3, 22, "D", [("information", U("information")), ("baggage", U("baggage")), ("advice", U("advice")), ("book", C("book")), ("money", U("money"))], 4, R22, S22, st=ST22)
mk(3, 22, "E", [("weather", U("weather")), ("chair", C("chair")), ("news", U("news")), ("furniture", U("furniture")), ("knowledge", U("knowledge"))], 2, R22, S22, st=ST22)
mk(3, 22, "F", [("student", C("student")), ("furniture", U("furniture")), ("traffic", U("traffic")), ("information", U("information")), ("money", U("money"))], 1, R22, S22 + " 정답 위치를 D와 다르게 옮겼다.", st=ST22)

# 3-23 복수형: 유형마다 오답 짝을 새로
ST23 = "다음 중 복수형이 올바르게 만들어진 것을 고르시오."
R23 = "복수형은 대부분 -s, -s·-x·-ch·-sh·자음+o로 끝나면 -es, 자음+y는 -ies, -f(e)는 -ves로 만든다. child-children, man-men, woman-women, foot-feet, tooth-teeth, mouse-mice, goose-geese는 불규칙하게 바뀐다."
def WR(pair, right): return f"{pair}: 바른 복수형은 {right}이므로"
OKP = "바르게 만든 복수형이므로"
S23 = "오답 네 개(knife - knifes, child - childs, watch - watchs, baby - babys)가 유형마다 반복되었다. 유형마다 오답 짝을 새로 썼다."
mk(3, 23, "B", [("wolf - wolfs", WR("wolf - wolfs", "wolves")), ("foot - foots", WR("foot - foots", "feet")), ("bus - buss", WR("bus - buss", "buses")), ("party - partys", WR("party - partys", "parties")), ("tooth - teeth", "tooth - teeth: " + OKP)], 5, R23,
   S23 + " 정답(city - cities)이 원문항과 같아 tooth - teeth로 바꿨다.", st=ST23)
mk(3, 23, "C", [("box - boxes", "box - boxes: " + OKP), ("goose - gooses", WR("goose - gooses", "geese")), ("dish - dishs", WR("dish - dishs", "dishes")), ("lady - ladys", WR("lady - ladys", "ladies")), ("wife - wifes", WR("wife - wifes", "wives"))], 1, R23, S23, st=ST23)
mk(3, 23, "D", [("potato - potatos", WR("potato - potatos", "potatoes")), ("man - mans", WR("man - mans", "men")), ("shelf - shelves", "shelf - shelves: " + OKP), ("fox - foxs", WR("fox - foxs", "foxes")), ("story - storys", WR("story - storys", "stories"))], 3, R23, S23, st=ST23)
mk(3, 23, "E", [("toy - toies", WR("toy - toies", "toys(모음+y는 -s만 붙임)")), ("person - people", "person - people: " + OKP), ("half - halfs", WR("half - halfs", "halves")), ("glass - glasss", WR("glass - glasss", "glasses")), ("woman - womans", WR("woman - womans", "women"))], 2, R23,
   S23 + " child가 두 번 나와 둘 중 하나가 답이라는 단서가 되던 것도 없앴다.", st=ST23)
mk(3, 23, "F", [("tomato - tomatos", WR("tomato - tomatos", "tomatoes")), ("family - familys", WR("family - familys", "families")), ("knife - knifes", WR("knife - knifes", "knives")), ("goose - geese", "goose - geese: " + OKP), ("brush - brushs", WR("brush - brushs", "brushes"))], 4, R23, S23, st=ST23)

# 3-24 a/an: 원문항 발문·밑줄·• 표시, B는 문장을 새로, the 보기를 명백한 오답으로
ST24 = "다음 빈칸 (A)와 (B)에 들어갈 말이 바르게 짝지어진 것은?"
UA, UB = "(<u>    A    </u>)", "(<u>    B    </u>)"
R24 = "a/an은 철자가 아니라 바로 뒤 단어의 첫소리로 정한다. 모음 소리 앞에는 an(an hour, an honest), 자음 소리 앞에는 a(a university, a one-way, a European)를 쓴다."
AB = lambda x: re.findall(r"\([AB]\) (\S+)", x)
def f24(t, l1, l2, c, a, wA, wB, s):
    good = AB(c[a-1]); nn = []
    for i, ch in enumerate(c):
        x, y = AB(ch)
        if i + 1 == a: nn.append(f"{c[a-1]}: 두 자리가 모두 첫소리에 맞으므로 정답이다."); continue
        bits = []
        if x != good[0]: bits.append(f"(A) {x}: " + ("any는 단수 명사 보어 앞에 쓰지 않는다." if x == "any" else wA))
        if y != good[1]: bits.append(f"(B) {y}: " + wB)
        nn.append(" ".join(bits) + " 따라서 오답이다.")
    F(3, 24, t, st=ST24, p=f"• {l1.replace('(A)', UA)}\n• {l2.replace('(B)', UB)}", c=c, a=a, r=R24, n=nn, k=f"(A)는 {good[0]}, (B)는 {good[1]}이다.", s=s + ipos(a))
S24 = "발문이 ‘첫소리에 맞게’라고 판단 규칙을 알려 주었고 빈칸 밑줄이 없었다. 원문항 발문과 밑줄·• 표시로 되돌렸으며, 조건이 없으면 the도 들어갈 수 있는 ‘the’ 보기를 명백한 오답(any)으로 바꿨다."
f24("B", "He is (A) European tourist.", "Is there (B) empty seat?", ["(A) an - (B) an", "(A) a - (B) an", "(A) an - (B) a", "(A) a - (B) a", "(A) any - (B) an"], 2,
    "European은 자음 소리 /j/로 시작하므로 a를 쓴다.", "empty는 모음 소리로 시작하므로 an을 쓴다.",
    "제시문과 정답이 원문항과 똑같았고 발문도 판단 규칙을 알려 주었다. 제시문을 새로 쓰고 원문항 발문과 밑줄·• 표시로 되돌렸다.")
f24("C", "Tom is (A) university student.", "She ate (B) apple.", ["(A) a - (B) a", "(A) an - (B) a", "(A) an - (B) an", "(A) a - (B) an", "(A) any - (B) an"], 4,
    "university는 자음 소리 /j/로 시작하므로 a를 쓴다.", "apple은 모음 소리로 시작하므로 an을 쓴다.", S24)
f24("D", "It was (A) unusual story.", "He bought (B) book.", ["(A) an - (B) a", "(A) a - (B) a", "(A) any - (B) a", "(A) a - (B) an", "(A) an - (B) an"], 1,
    "unusual은 모음 소리로 시작하므로 an을 쓴다.", "book은 자음 소리로 시작하므로 a를 쓴다.", S24)
f24("E", "She waited for (A) hour.", "Tom has (B) bike.", ["(A) any - (B) a", "(A) an - (B) an", "(A) an - (B) a", "(A) a - (B) an", "(A) a - (B) a"], 3,
    "hour는 h가 소리 나지 않아 모음 소리로 시작하므로 an을 쓴다.", "bike는 자음 소리로 시작하므로 a를 쓴다.", S24)
f24("F", "He bought (A) one-way ticket.", "Jane has (B) umbrella.", ["(A) a - (B) a", "(A) an - (B) a", "(A) any - (B) an", "(A) an - (B) an", "(A) a - (B) an"], 5,
    "one은 자음 소리 /w/로 시작하므로 a를 쓴다.", "umbrella는 모음 소리로 시작하므로 an을 쓴다.", S24 + " 정답 위치를 옮겼다.")

# 3-25 관사 문장 짝: 원문항 형식(ⓐ~ⓓ, 두 기호 조합), 옳은 문장이 둘이 되게
ST25 = "다음 중 어법상 옳은 문장으로만 짝지어진 것은?"
R25 = "a/an은 불특정한 셀 수 있는 단수명사 앞에, the는 특정하거나 하나뿐인 대상(the sun, the moon)과 악기 앞에 쓴다. 식사·운동 이름과 by + 교통수단, 셀 수 없는 명사 앞에는 a/an을 쓰지 않는다."
S25 = "보기 기호 ⓐ~ⓓ가 a~d로 바뀌어 한 줄로 이어졌고, 원문항에 없던 ‘해당 없음’ 선택지가 생겼으며 발문도 달랐다. 원문항 발문과 형식(ⓐ~ⓓ 줄바꿈, 두 기호 조합)으로 되돌리고, 옳은 문장이 두 개가 되게 조정했다."
def f25(t, lines, judge, ok, c, a, s=S25):
    F(3, 25, t, st=ST25, p="\n".join(lines), c=c, a=a, r=R25, pre=["문장별 판정: " + j for j in judge], k=f"옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), s=s + ipos(a))
f25("B", ["ⓐ We had lunch at noon.", "ⓑ She is a honest girl.", "ⓒ I go to school by the bus.", "ⓓ The moon is bright tonight."],
    ["ⓐ O. 식사 이름 앞에는 관사를 쓰지 않는다.", "ⓑ X. honest는 모음 소리로 시작하므로 an honest이다.", "ⓒ X. by + 교통수단에는 관사를 쓰지 않는다(by bus).", "ⓓ O. 하나뿐인 moon 앞에 the를 썼다."],
    "ⓐ, ⓓ", ["ⓐ, ⓑ", "ⓐ, ⓓ", "ⓑ, ⓒ", "ⓑ, ⓓ", "ⓒ, ⓓ"], 2, "네 문장이 원문항 문장을 거의 그대로 썼고 정답 조합(ⓑ, ⓓ)도 같았으며 형식도 달랐다. 문장을 새로 쓰고 원문항 발문과 형식으로 되돌렸다.")
f25("C", ["ⓐ I ate breakfast at 7.", "ⓑ She bought an umbrella.", "ⓒ We need an water.", "ⓓ Tom plays the soccer."],
    ["ⓐ O. 식사 이름 앞에는 관사를 쓰지 않는다.", "ⓑ O. umbrella는 모음 소리로 시작하므로 an이다.", "ⓒ X. 셀 수 없는 명사(water) 앞에는 an을 쓰지 않는다.", "ⓓ X. 운동 이름 앞에는 관사를 쓰지 않는다(play soccer)."],
    "ⓐ, ⓑ", ["ⓐ, ⓑ", "ⓐ, ⓒ", "ⓑ, ⓓ", "ⓑ, ⓒ", "ⓒ, ⓓ"], 1)
f25("D", ["ⓐ He goes to school by a bus.", "ⓑ Jane has an hour.", "ⓒ They play soccer.", "ⓓ I need an rice."],
    ["ⓐ X. by + 교통수단에는 관사를 쓰지 않는다(by bus).", "ⓑ O. hour는 모음 소리로 시작하므로 an이다.", "ⓒ O. 운동 이름 앞에는 관사를 쓰지 않는다.", "ⓓ X. 셀 수 없는 명사(rice) 앞에는 an을 쓰지 않는다."],
    "ⓑ, ⓒ", ["ⓐ, ⓑ", "ⓐ, ⓒ", "ⓑ, ⓓ", "ⓑ, ⓒ", "ⓒ, ⓓ"], 4)
f25("E", ["ⓐ We had dinner at six.", "ⓑ Tom bought an one-way ticket.", "ⓒ She plays the violin.", "ⓓ There is an information."],
    ["ⓐ O. 식사 이름 앞에는 관사를 쓰지 않는다.", "ⓑ X. one은 자음 소리 /w/로 시작하므로 a one-way이다.", "ⓒ O. 악기 앞에는 the를 쓴다.", "ⓓ X. 셀 수 없는 명사(information) 앞에는 an을 쓰지 않는다."],
    "ⓐ, ⓒ", ["ⓐ, ⓑ", "ⓑ, ⓓ", "ⓑ, ⓒ", "ⓒ, ⓓ", "ⓐ, ⓒ"], 5, S25 + " 발문의 information 뜻 설명도 지웠다.")
f25("F", ["ⓐ She eats a apple.", "ⓑ They go home by a taxi.", "ⓒ We play tennis after school.", "ⓓ The sun rises in the east."],
    ["ⓐ X. apple은 모음 소리로 시작하므로 an apple이다.", "ⓑ X. by + 교통수단에는 관사를 쓰지 않는다(by taxi).", "ⓒ O. 운동 이름 앞에 관사를 쓰지 않았다.", "ⓓ O. 하나뿐인 sun과 방향(the east) 앞에 the를 썼다."],
    "ⓒ, ⓓ", ["ⓐ, ⓑ", "ⓐ, ⓒ", "ⓑ, ⓓ", "ⓑ, ⓒ", "ⓒ, ⓓ"], 5, S25 + " 정답 조합·위치(ⓑ, ⓓ ③)가 원문항과 같지 않게 옳은 문장을 ⓒ, ⓓ로 했다.")

# 3-26 불규칙 복수형 + be동사: B는 명사를 새로, 오답을 제시문 명사의 다른 형태로
R26 = "불규칙 복수형(foot-feet, child-children, mouse-mice, man-men, woman-women)은 -s를 붙이지 않고 모양이 바뀌며, 복수 주어에는 be동사 are를 쓴다."
S26 = "제시문 명사와 달리 오답 네 개가 원문항의 tooth/teeth를 그대로 써서, 제시문 명사가 들어간 보기는 정답뿐이었다. 오답을 제시문 명사의 다른 형태로 바꿨다."
def f26(t, sent, c, a, right, s=S26):
    subj = sent.split()[1]
    nn = []
    for i, ch in enumerate(c):
        w, v = ch.split()
        if i + 1 == a: nn.append(f"{ch}: 복수형({right})과 복수 동사(are)가 모두 알맞으므로"); continue
        bits = []
        if w != right: bits.append(f"{w}: {subj}의 복수형은 {right}이다.")
        if v != "are": bits.append(f"{v}: 복수 주어에는 are를 쓴다.")
        nn.append(" ".join(bits) + " 따라서")
    mk(3, 26, t, list(zip(c, nn)), a, R26, s, p=f"{sent}\n→ The ______ _____ {sent.split()[-1]}")
f26("B", "The foot is cold.", ["foots are", "feet is", "feet are", "foot are", "feets are"], 3, "feet", "제시문과 정답이 원문항과 똑같았다. 제시문 명사를 foot으로 바꿨다.")
f26("C", "The child is happy.", ["childs are", "children is", "child are", "children are", "childrens are"], 4, "children")
f26("D", "The mouse is small.", ["mouses are", "mice is", "mouse are", "mices are", "mice are"], 5, "mice")
f26("E", "The man is busy.", ["men are", "mans are", "men is", "man are", "mens are"], 1, "men")
f26("F", "The woman is kind.", ["womans are", "women are", "women is", "woman are", "womens are"], 2, "women")

# 3-27 단위 표현 배열: 원문항 발문, B는 명사·단위를 새로
ST27 = "다음 단어들을 바르게 배열하여 문장을 완성한 것을 고르시오."
mk(3, 27, "B", [("I two glasses of juice drank.", "동사(drank)가 목적어 뒤에 와 어순이 틀렸으므로"), ("I drank two glasses juice of.", "of가 단위와 내용 명사 사이에 오지 않아 틀렸으므로"), ("I drank two glasses of juice.", "주어 + 동사 + 수사 + 단위 + of + 명사의 바른 어순이므로"),
                ("I drank glasses two of juice.", "수사(two)가 단위(glasses) 앞에 와야 하므로"), ("Drank I two glasses of juice.", "평서문인데 동사가 주어 앞에 와 어순이 틀렸으므로")], 3,
   "평서문은 주어 + 동사 + 목적어 순서이고, 단위 표현은 수사 + 단위명사(복수형) + of + 내용명사로 쓴다.",
   "제시문과 정답이 원문항과 똑같았고 발문 조건도 붙었다. 제시문을 ‘주스 두 잔(two glasses of juice)’으로 바꾸고 원문항 발문으로 되돌렸다.", st=ST27,
   p="나는 주스 두 잔을 마셨어요.\n(juice / of / glasses / I / two / drank / .)")
for t in "CDEF":
    F(3, 27, t, st=ST27, xr=[x for x in [("조건에 맞는 문장은", "바르게 배열한 문장은"), ("이 보기의 어순은 기본 주어", "이 보기는 평서문의 주어")] if x[0] in V(3, 27, t)["expl"]], s="발문에 ‘주어진 단어를 모두 한 번씩, 기본 주어–동사–목적어 어순의 평서문’ 조건이 붙어 배열 구조를 알려 주어 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 3-28 식사 이름 앞 관사: 원문항 발문·밑줄, B는 대화를 새로
ST28 = "다음 밑줄 친 부분을 바르게 고친 것을 고르시오."
S28 = "발문이 ‘일상적인 식사명으로, 관사와 복수형 없이’라고 정답을 알려 주었고 밑줄이 없었다. 원문항 발문과 밑줄로 되돌렸다. 보기와 정답은 그대로다."
R28 = "breakfast, lunch, dinner 같은 식사 이름은 보통 관사 없이 쓰고 복수형으로 쓰지 않는다."
S28b = " 영어에 없는 형태의 오답(an dinner, lunchs 등)은 원문항의 오답처럼 실제 형태(the ~, ~s, some ~s, any ~s)로 바꿨다."
N28 = {"the": "식사 이름 앞에는 the도 쓰지 않으므로", "a": "식사 이름 앞에는 a를 쓰지 않으므로", "s": "식사 이름은 복수형으로 쓰지 않으므로", "ok": "일상적인 식사 이름은 관사 없이 단수로 쓰므로"}
def f28(t, meal, c, a, p, s):
    def note(x):
        if x == meal: return N28["ok"]
        if x.endswith("s") and not x.endswith("ss"): return N28["s"]
        return N28["the"] if x.startswith("the ") else N28["a"]
    mk(3, 28, t, [(x, f"{x}: " + note(x)) for x in c], a, R28, s + S28b, st=ST28, p=p)
f28("B", "dinner", ["dinners", "the dinner", "any dinners", "dinner", "some dinners"], 4, "Tom: What time do you usually have <u>a dinner</u>?\nJane: At seven.", "대화와 정답이 원문항과 같았고 발문이 정답을 알려 주었다. 대화를 새로 쓰고 원문항 발문과 밑줄로 되돌렸다.")
S28c = "발문이 ‘일상적인 식사명으로, 관사와 복수형 없이’라고 정답을 알려 주었고 밑줄이 없었다. 원문항 발문과 밑줄로 되돌렸다."
f28("C", "breakfast", ["any breakfasts", "the breakfast", "breakfasts", "some breakfasts", "breakfast"], 5, "Tom: Did you eat <u>a breakfast</u>?\nJane: Yes.", S28c)
f28("D", "dinner", ["dinner", "the dinner", "some dinners", "dinners", "any dinners"], 1, "Amy: Let's have <u>a dinner</u> together.", S28c)
f28("E", "lunch", ["lunch", "a lunch", "lunches", "some lunches", "the lunches"], 1, "Ben: I had <u>the lunch</u> at noon as usual.", S28c)
f28("F", "breakfast", ["breakfast", "the breakfast", "some breakfasts", "breakfasts", "any breakfasts"], 1, "Mina: We usually have <u>a breakfast</u> at seven.", S28c)

# 3-29 by + 교통수단: 원문항 발문·밑줄·줄바꿈, 옳은 문장이 둘이 되게(두 기호 조합)
ST29 = "다음 중 밑줄 친 부분이 어법상 옳은 문장으로만 짝지어진 것은?"
R29 = "수단을 나타내는 by + 교통·통신 수단(by bus, by phone, by email)에는 관사를 쓰지 않는다. 걸어서는 on foot이며, on a foot·on feet로 쓰지 않는다."
S29 = "발문에 ‘이동·연락·운송 수단을 나타낼 때’ 조건이 붙고 ‘모두 빠짐없이’로 바뀌었으며 밑줄이 없었다. 원문항 발문과 밑줄·줄바꿈으로 되돌리고, 원문항처럼 옳은 문장이 둘인 두 기호 조합이 되게 조정했다."
CH29 = ["(가), (나)", "(가), (다)", "(나), (다)", "(나), (라)", "(다), (라)"]
def f29(t, lines, judge, ok, c, a, s=S29):
    F(3, 29, t, st=ST29, p="\n".join(lines), c=c, a=a, r=R29, pre=["문장별 판정: " + j for j in judge], k=f"옳은 문장은 {ok}이다.", n=setnotes(c, ok, "옳은 문장"), s=s + ipos(a))
f29("B", ["(가) We went to the museum <u>by subway</u>.", "(나) She called me <u>by the phone</u>.", "(다) My sister went to school <u>by bus</u>.", "(라) He came here <u>on a foot</u>."],
    ["(가) O. by + 교통수단에 관사를 쓰지 않았다.", "(나) X. by + 통신 수단에는 관사를 쓰지 않는다(by phone).", "(다) O. by + 교통수단에 관사를 쓰지 않았다.", "(라) X. 걸어서는 on foot이다."],
    "(가), (다)", CH29, 2, "(가)·(나)가 원문항 문장과 같았고 발문·밑줄도 원본과 달랐다. 문장을 새로 쓰고 " + S29[S29.index("원문항 발문과"):])
f29("C", ["(가) Tom goes to work <u>by the car</u>.", "(나) Jane came <u>by a taxi</u>.", "(다) We travel <u>by train</u>.", "(라) They went home <u>on foot</u>."],
    ["(가) X. by + 교통수단에는 관사를 쓰지 않는다(by car).", "(나) X. by + 교통수단에는 관사를 쓰지 않는다(by taxi).", "(다) O. by + 교통수단이다.", "(라) O. 걸어서는 on foot이다."], "(다), (라)", CH29, 5)
f29("D", ["(가) I sent it <u>by email</u>.", "(나) We went there <u>by the bus</u>.", "(다) Tom traveled <u>by a plane</u>.", "(라) Jane came <u>on foot</u>."],
    ["(가) O. by + 통신 수단이다.", "(나) X. by + 교통수단에는 관사를 쓰지 않는다(by bus).", "(다) X. by + 교통수단에는 관사를 쓰지 않는다(by plane).", "(라) O. 걸어서는 on foot이다."],
    "(가), (라)", ["(가), (나)", "(나), (다)", "(가), (라)", "(나), (라)", "(다), (라)"], 3)
f29("E", ["(가) We spoke <u>by phone</u>.", "(나) Tom came <u>by bike</u>.", "(다) Jane went <u>by a train</u>.", "(라) I went there <u>on feet</u>."],
    ["(가) O. by + 통신 수단이다.", "(나) O. by + 교통수단이다.", "(다) X. by + 교통수단에는 관사를 쓰지 않는다(by train).", "(라) X. 걸어서는 on foot이다."], "(가), (나)", CH29, 1)
f29("F", ["(가) They traveled <u>by the ship</u>.", "(나) She went <u>by taxi</u>.", "(다) I sent the file <u>by an email</u>.", "(라) We came <u>on foot</u>."],
    ["(가) X. by + 교통수단에는 관사를 쓰지 않는다(by ship).", "(나) O. by + 교통수단이다.", "(다) X. by + 통신 수단에는 관사를 쓰지 않는다(by email).", "(라) O. 걸어서는 on foot이다."], "(나), (라)", CH29, 4)

# 3-30 관사 설명 중 옳지 않은 것: 원문항 발문·<보기>, B는 틀린 설명을 원문항과 다르게, E는 반대 짝 설명 교체
ST30 = "다음 <보기> 지문의 밑줄 친 ⓐ~ⓔ에 대한 설명으로 옳지 않은 것은?"
R30 = "하나뿐인 대상(the sun, the moon)과 악기 앞에는 the를, 식사·운동 이름과 by + 교통수단에는 관사를 쓰지 않는다. 하루의 시간대는 in the morning/afternoon/evening으로 쓴다."
talk(3, 30, "B", [("ⓐ: sun은 여러 개일 수 있으므로 a sun으로 써야 한다.", "sun은 하나뿐인 천체라 the sun으로 쓴다."), ("ⓒ: by bus에서는 교통수단 앞 관사를 쓰지 않는다.", "by + 교통수단에는 관사를 쓰지 않는다."),
                  ("ⓔ: 운동 종목 soccer 앞에는 관사를 쓰지 않는다.", "운동 이름 앞에는 관사를 쓰지 않는다."), ("ⓑ: 식사 이름 breakfast는 보통 관사 없이 쓴다.", "식사 이름 앞에는 관사를 쓰지 않는다."),
                  ("ⓓ: in the afternoon은 하루의 시간대를 나타내는 올바른 표현이다.", "시간대는 in the afternoon으로 쓴다.")], 1, R30,
     "틀린 설명이 원문항 정답과 같은 내용(시간대 앞 부정관사)이었다. 틀린 설명을 ‘sun 앞에 a’라는 다른 오개념으로 바꾸고 원문항 발문과 <보기> 형식으로 되돌렸다.", st=ST30,
     p="<보기>\nYesterday I woke up early to see ⓐ<u>the sun</u>. After ⓑ<u>breakfast</u>, I went out ⓒ<u>by bus</u>. In ⓓ<u>the afternoon</u>, I played ⓔ<u>soccer</u>.")
P30 = {"C": "Last night, we went up the hill and saw ⓐ<u>the moon</u> shining over the town. After ⓑ<u>dinner</u>, we talked with our cousins ⓒ<u>by phone</u> for a long time. In ⓓ<u>the evening</u>, Tom played ⓔ<u>the guitar</u> for us.",
       "E": "Last weekend, Tom traveled to his grandparents' house ⓐ<u>by train</u>. After ⓑ<u>lunch</u>, he played ⓒ<u>the piano</u> for his family. In ⓓ<u>the morning</u>, he got up early and saw ⓔ<u>the sun</u> rise over the sea.",
       "F": "After school, we had ⓐ<u>dinner</u> at a small restaurant and went home ⓑ<u>on foot</u>. Then we played ⓒ<u>basketball</u> in the park. We read books in ⓓ<u>the evening</u> and took a walk under ⓔ<u>the moon</u>."}
L30 = " 지문이 원문항의 절반에 못 미쳐, 밑줄 친 표현은 그대로 두고 지문을 원문항 수준으로 늘렸다."
F(3, 30, "D", st=ST30, p="<보기>\n" + V(3, 30, "D")["passage"], okdup=True, s="발문이 원문항과 달라 원문항 발문과 <보기> 형식으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "CF":
    F(3, 30, t, st=ST30, p="<보기>\n" + P30[t], okdup=True, s="발문이 원문항과 달라 원문항 발문과 <보기> 형식으로 되돌렸다. 보기와 정답은 그대로다." + L30)
talk(3, 30, "E", [("ⓔ: sun은 유일한 천체를 가리켜 the를 쓴다.", "하나뿐인 천체라 the를 쓴다."), ("ⓑ: 일반적인 lunch 앞에는 관사를 쓰지 않는다.", "식사 이름 앞에는 관사를 쓰지 않는다."),
                  ("ⓐ: by train은 반드시 by a train으로 써야 한다.", "by + 교통수단에는 관사를 쓰지 않으므로 by train이 맞다."), ("ⓓ: in the morning은 하루의 시간대를 나타내는 올바른 표현이다.", "시간대는 in the morning으로 쓴다."),
                  ("ⓒ: 이 문장의 played the piano는 올바른 악기 연주 표현이다.", "악기 앞에는 the를 쓴다.")], 3, R30,
     "같은 ⓐ(by train)에 대해 ‘반드시 by a train / 관사를 쓰지 않는다’처럼 반대되는 설명 두 개가 함께 있어 단서가 되었다. ④를 ⓓ에 대한 설명으로 바꾸고 원문항 발문과 <보기> 형식으로 되돌렸다." + L30, st=ST30,
     p="<보기>\n" + P30["E"])

# ---- 2차 감수(2026-10) 추가 ----
# 3-21 C·D: 성립하지 않는 형태의 오답(a bottles of, a sheets of) → 실제 단위 표현으로
R21 = "셀 수 없는 명사는 단위 표현으로 센다: a glass of water, a sheet of paper, a loaf of bread, a bottle of milk, a piece of cheese."
S21 = "오답 가운데 성립하지 않는 형태({})가 있어 형태만으로 지워졌다. 원문항의 오답처럼 실제 단위 표현({})으로 바꿨다. 나머지 보기와 정답은 그대로다."
mk(3, 21, "C", [("a bottle of", "a bottle of는 ‘한 병’이라 우리말 ‘한 잔’과 맞지 않으므로"), ("a loaf of", "a loaf of는 빵 같은 ‘한 덩어리’에 쓰므로"), ("a piece of", "a piece of는 ‘한 조각’이라 물에 쓰지 않으므로"),
                ("a sheet of", "a sheet of는 종이 같은 ‘한 장’에 쓰므로"), ("a glass of", "‘물 한 잔’은 a glass of water이므로")], 5, R21, S21.format("a bottles of", "a bottle of"))
mk(3, 21, "D", [("a loaf of", "a loaf of는 빵 같은 ‘한 덩어리’에 쓰므로"), ("a bottle of", "a bottle of는 ‘한 병’이라 종이에 쓰지 않으므로"), ("a slice of", "a slice of는 얇게 썬 ‘한 조각’이라 종이에 쓰지 않으므로"),
                ("a cup of", "a cup of는 ‘한 컵’이라 종이에 쓰지 않으므로"), ("a sheet of", "‘종이 한 장’은 a sheet of paper이므로")], 5, R21, S21.format("a sheets of", "a slice of"))
