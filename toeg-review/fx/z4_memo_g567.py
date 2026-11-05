# 2026-10-06 B유형 감수 메모 반영 — 5급·6급·7급
import re as _r

# 5-22 이 단계에서 다루지 않는 take - took 짝을 다른 동사로
R22m = "불규칙 동사는 -ed를 붙이지 않고 정해진 과거형을 쓴다(speak - spoke, teach - taught). 규칙 동사는 -ed를 붙인다."
def f22m(t, c, a, s):
    n = []
    for i, x in enumerate(c):
        b, p = [w.strip() for w in x.split("-")]
        n.append(f"{b}는 불규칙 동사라 과거형이 {p}다. {p}는 없는 형태이므로 정답이다." if i + 1 == a else f"{b}의 불규칙 과거형 {p}로 옳으므로 오답이다.")
    if a: n[a - 1] = n[a - 1]
    F(5, 22, t, c=c, a=a, r=R22m, n=n, s=s + pos(a))
_B22 = ["leave - left", "teach - taught", "write - wrote", "speak - speaked", "bring - brought"]
f22m("B", _B22, 4, MEMO + "이 단계의 수업에 나오지 않는 take - taked를 speak - speaked로 바꿨다.")
FIX[(5, 22, "B")]["n"][3] = "speak는 불규칙 동사라 과거형이 spoke다. speaked는 없는 형태이므로 정답이다."
f22m("D", ["speak - spoke", "buy - buyed", "make - made", "go - went", "see - saw"], 2, MEMO + "B와 같은 이유로 ① take - took을 speak - spoke로 바꿨다.")
FIX[(5, 22, "D")]["n"][1] = "buy는 불규칙 동사라 과거형이 bought다. buyed는 없는 형태이므로 정답이다."
f22m("F", ["come - came", "eat - ate", "make - maked", "see - saw", "teach - taught"], 3, MEMO + "B와 같은 이유로 ⑤ take - took을 teach - taught로 바꿨다.")
FIX[(5, 22, "F")]["n"][2] = "make는 불규칙 동사라 과거형이 made다. maked는 없는 형태이므로 정답이다."

# 5-82 위치 문항: 번호를 넣은 영어 문장을 제시하고 보기는 번호만
_S82 = MEMO + "영어 문장이 보이지 않고 보기에 낱말만 있던 형식을, 원문항과 함께 낱말 사이에 번호를 넣은 영어 문장을 제시하고 보기는 번호만 두는 형식으로 바꿨다. 정답은 그대로다."
def posm2(g_, n_, t, ko, words, a, s):
    o = OLD(g_, n_, t)
    RE(g_, n_, t, p=(ko + "\n" if ko else "") + numbered(words), c=numc(), a=a, n=o["n"], s=s + pos(a))
posm2(5, 82, "B", "우리 이모는 부산에서 일한다.", ["My", "aunt", "works", "Busan", "."], 4, _S82)
posm2(5, 82, "C", "Tom은 지금 대전에 있다.", ["Tom", "is", "Daejeon", "now", "."], 3, _S82)
posm2(5, 82, "D", "우리 반 학생들은 친절하다.", ["Students", "my", "class", "are", "kind."], 2, _S82)
posm2(5, 82, "E", "우리 조부모님은 제주에서 행복하게 사신다.", ["My", "grandparents", "live", "happily", "Jeju."], 5, _S82)
posm2(5, 82, "F", "그들은 방 안에서 조용히 공부한다.", ["They", "study", "quietly", "the", "room."], 4, _S82)

# ---------------- 6급 ----------------
# 6-2 이 단계에 없는 advice 대신 물질명사 butter
R2m = "a/an은 셀 수 있는 명사의 단수형 앞에만 쓴다. butter, water처럼 셀 수 없는 명사 앞에는 쓰지 않는다."
RE(6, 2, "B", c=["ticket", "coin", "butter", "key", "map"], a=3, r=R2m,
   n=["ticket은 셀 수 있는 명사라 a 뒤에 쓸 수 있으므로 오답이다.", "coin은 셀 수 있는 명사라 a 뒤에 쓸 수 있으므로 오답이다.", "butter는 일정한 모양이 없는 물질이라 셀 수 없어 a 뒤에 쓸 수 없으므로 정답이다.", "key는 셀 수 있는 명사라 a 뒤에 쓸 수 있으므로 오답이다.", "map은 셀 수 있는 명사라 a 뒤에 쓸 수 있으므로 오답이다."],
   s=OLD(6, 2, "B")["s"] + " " + MEMO + "이 단계에 나오지 않는 추상명사 advice를 셀 수 없는 물질명사 butter로 바꿨다. 정답 위치 ③.")

# 6-5 보기 문장의 낱말을 초등 4학년 수준으로
R5m6 = "a/an은 철자가 아니라 첫소리로 정한다. hour처럼 h를 발음하지 않는 낱말 앞에는 an, uniform·useful처럼 ‘유’ 소리로 시작하는 낱말 앞에는 a를 쓴다."
F(6, 5, "B", c=["I have an egg and a banana.", "We played soccer for a hour.", "She has a cute cat.", "He is an old man.", "Let's go to the park."], a=2, r=R5m6,
  n=["egg는 모음 소리로 시작해 an, banana는 자음 소리로 시작해 a가 맞으므로 오답이다.", "hour는 h를 발음하지 않아 모음 소리로 시작하므로 an hour로 써야 하므로 정답이다.", "cute는 자음 소리로 시작해 a가 맞으므로 오답이다.", "old는 모음 소리로 시작해 an이 맞으므로 오답이다.", "서로 아는 특정한 곳인 the park처럼 the를 바르게 썼으므로 오답이다."],
  s=MEMO + "honest, European, university, one-way처럼 이 단계보다 어려운 낱말이 들어 있던 보기 문장을 초등 4학년 수준의 낱말로 새로 썼다." + pos(2))
def f5m6(t, i, text, note, s):
    o = OLD(6, 5, t); c = list(o["c"]); n = list(o["n"]); c[i - 1] = text; n[i - 1] = note
    RE(6, 5, t, c=c, n=n, s=o["s"] + " " + MEMO + s)
f5m6("D", 1, "It is a sunny day.", "sunny는 자음 소리로 시작해 a가 맞으므로 오답이다.", "어려운 낱말(unique)이 든 ①을 쉬운 문장으로 바꿨다.")
f5m6("E", 2, "She has a new bike.", "new는 자음 소리로 시작해 a가 맞으므로 오답이다.", "어려운 낱말(one-dollar, honor)이 든 ②·⑤를 쉬운 문장으로 바꿨다.")
_o5e = OLD(6, 5, "E"); _c5e = list(_o5e["c"]); _n5e = list(_o5e["n"]); _c5e[4] = "I ate an apple for lunch."; _n5e[4] = "apple은 모음 소리로 시작해 an이 맞으므로 오답이다."
RE(6, 5, "E", c=_c5e, n=_n5e)
f5m6("F", 3, "We have an English test today.", "English는 모음 소리로 시작해 an이 맞으므로 오답이다.", "어려운 낱말(European)이 든 ③을 쉬운 문장으로 바꿨다.")

# 6-6 be동사 오답을 수와 관련된 오답으로
R6m = "셀 수 있는 단수명사 앞에 a/an을 쓴다. 뒤 낱말이 모음 소리로 시작하면 an, 자음 소리로 시작하면 a다. two, three, many 뒤에는 복수형을 쓴다."
_S6 = MEMO + "원문항과 함께 be동사 오답(is, are)을 수와 관련된 오답(two, three, many)으로 바꿨다."
def f6m(t, c, a, noun, sound):
    ok = c[a - 1]; bad = "an" if ok == "a" else "a"; pl = noun + ("es" if noun.endswith("ch") else "s")
    n = []
    for i, x in enumerate(c):
        if i + 1 == a: n.append(f"{sound} 소리로 시작하는 {noun} 앞에 {ok}을 쓰므로 정답이다." if ok == "an" else f"{sound} 소리로 시작하는 {noun} 앞에 {ok}를 쓰므로 정답이다.")
        elif x == bad: n.append(f"{noun}는 {sound} 소리로 시작해 {bad}{'을' if bad == 'an' else '를'} 쓸 수 없으므로 오답이다.")
        else: n.append(f"{x} 뒤에는 복수형 {pl}가 와야 하므로 오답이다.")
    RE(6, 6, t, c=c, a=a, r=R6m, n=n, s=OLD(6, 6, t)["s"] + " " + _S6 + pos(a))
f6m("B", ["an", "a", "two", "many", "three"], 2, "banana", "자음")
f6m("C", ["two", "a", "an", "many", "three"], 3, "apple", "모음")
f6m("D", ["many", "an", "two", "three", "a"], 5, "sandwich", "자음")
f6m("E", ["an", "two", "a", "many", "three"], 1, "egg", "모음")
f6m("F", ["two", "many", "three", "an", "a"], 4, "umbrella", "모음")

# 6-16 아직 배우지 않은 과거형(was) 대신 현재형의 부정형
R16m = "현재형 be동사: I am / you, we, they are / he, she, it is. be는 원형이라 그대로 쓸 수 없다."
_S16 = MEMO + "원문항과 함께, 아직 배우지 않은 be동사 과거형 was를 보기에서 빼고 현재형의 부정형(isn't/aren't)으로 바꿨다."
def f16m(t, c, a, S):
    n = []
    for i, x in enumerate(c):
        if i + 1 == a: n.append(f"주어 {S}에 맞는 be동사이므로 정답이다.")
        elif x == "am": n.append("am은 주어 I에만 쓰므로 오답이다.")
        elif x == "is": n.append("is는 3인칭 단수 주어에 쓰므로 오답이다.")
        elif x == "are": n.append("are는 you·복수 주어에 쓰므로 오답이다.")
        elif x == "be": n.append("be는 동사원형이라 주어 뒤에 그대로 쓸 수 없으므로 오답이다.")
        else: n.append(f"{x}는 {x[:-3]}의 부정형이라 주어 {S}에 맞지 않으므로 오답이다.")
    RE(6, 16, t, c=c, a=a, r=R16m, n=n, s=OLD(6, 16, t)["s"] + " " + _S16 + pos(a))
f16m("B", ["be", "am", "is", "aren't", "are"], 3, "Tom")
f16m("C", ["be", "is", "isn't", "am", "are"], 4, "I")
f16m("D", ["are", "aren't", "is", "be", "am"], 3, "She")
f16m("E", ["isn't", "are", "is", "be", "am"], 2, "We")
f16m("F", ["be", "isn't", "am", "are", "is"], 4, "My parents")

# 6-21 예시 문장의 빈칸에 알맞은 be동사 과거형 고르기(원문항과 같게)
ST21 = "다음 빈칸에 들어갈 알맞은 be동사의 과거형을 고르시오."
R21m = "be동사의 과거형은 was, were다. 주어가 I·3인칭 단수면 was, you·복수면 were를 쓴다."
_S21 = MEMO + "원문항과 함께, 문장 없이 형태만 고르던 문항을 예시 문장의 빈칸에 알맞은 be동사 과거형을 고르는 문항으로 바꿨다."
def f21m(t, p, c, a, S, time):
    n = []
    for i, x in enumerate(c):
        xl = x.lower()
        if i + 1 == a: n.append(f"주어 {S}에 맞는 과거형이므로 정답이다.")
        elif xl == "was": n.append(f"was는 I·3인칭 단수 주어에 쓰는 과거형이라 {S}에 맞지 않으므로 오답이다.")
        elif xl == "were": n.append(f"were는 you·복수 주어에 쓰는 과거형이라 {S}에 맞지 않으므로 오답이다.")
        elif xl == "be": n.append("be는 원형이라 주어 뒤에 그대로 쓸 수 없으므로 오답이다.")
        elif xl == "do": n.append("Do는 be동사가 아니므로 오답이다.")
        else: n.append(f"현재형({x})이라 과거의 일({time})에 쓸 수 없으므로 오답이다.")
    RE(6, 21, t, st=ST21, p=p, c=c, a=a, r=R21m, n=n, s=_S21 + pos(a))
f21m("B", "I _______ tired yesterday.", ["was", "were", "am", "is", "be"], 1, "I", "yesterday")
f21m("C", "They _______ in the park last Sunday.", ["are", "were", "was", "is", "be"], 2, "They", "last Sunday")
f21m("D", "We _______ very busy last week.", ["were", "was", "are", "am", "be"], 1, "We", "last week")
f21m("E", "The weather _______ cold last night.", ["are", "is", "am", "were", "was"], 5, "The weather", "last night")
f21m("F", "_______ you at home last night?", ["Are", "Is", "Were", "Was", "Am"], 3, "you", "last night")

# 6-29 보기를 밑줄 친 말로(번호만 있던 것)
for _t, _c in {"B": ["was excited", "was warm", "were near the bus", "was hungry", "were happy"], "C": ["were beautiful", "were in a glass case", "were interested", "was tired", "was a long day"],
               "D": ["were ready", "was cold", "was inside a tent", "was quiet", "were safe"], "E": ["were at her house", "were on the table", "was excited", "were delicious", "was happy"],
               "F": ["were asleep", "was noisy", "were excited", "was busy taking pictures", "were cool"]}.items():
    _o = OLD(6, 29, _t); RE(6, 29, _t, c=_c, s=_o["s"].replace("원문항처럼 밑줄 번호만 제시했다", "보기를 밑줄 친 말로 제시했다") + " " + MEMO + "원문항과 함께 번호만 있던 보기를 밑줄 친 be동사와 그 뒷말로 보였다(주어는 보기에 넣지 않았다).")

# 6-32 밑줄 친 동사 형식, 발문 ‘밑줄 친 동사에 s가 붙지 않는 것은?’
ST32 = "다음 중 밑줄 친 동사에 s가 붙지 않는 것은?"
for _t in "BCDEF":
    _o = OLD(6, 32, _t)
    RE(6, 32, _t, st=ST32, c=[_r.sub(r"(\w+)___", r"<u>\1</u>", x) for x in _o["c"]], s=_o["s"] + " " + MEMO + "원문항과 함께 동사 뒤 빈칸(read___) 형식을 밑줄 친 동사 형식으로 바꾸고 발문을 ‘밑줄 친 동사에 s가 붙지 않는 것은?’으로 고쳤다.")

# 6-41 C의 불규칙 짝(see - saw)을 규칙 짝으로
R41m = "규칙 과거형: 대부분 -ed, 자음 + y는 y를 i로 바꾸고 -ed(carried), 단모음 + 단자음은 자음을 겹쳐 -ed(hugged), 모음 + y는 그대로 -ed(played)."
F(6, 41, "C", c=["carry - carried", "plan - planed", "visit - visited", "watch - watched", "hug - hugged"], a=2, r=R41m,
  n=["자음 + y라 y를 i로 바꾼 옳은 형태이므로 오답이다.", "plan은 단모음 + 단자음이라 n을 겹쳐 planned로 써야 하므로 정답이다.", "-ed를 붙인 옳은 형태이므로 오답이다.", "-ed를 붙인 옳은 형태이므로 오답이다.", "단모음 + 단자음이라 g를 겹쳐 쓴 옳은 형태이므로 오답이다."],
  s=MEMO + "이 단계에서 다루지 않는 불규칙 과거형 ④ see - saw를 규칙 과거형 watch - watched로 바꿨다." + pos(2))

# 6-45 불규칙 동사를 규칙 동사로(원문항과 함께)
R45m = "현재의 문장을 과거로 바꿀 때는 동사를 과거형으로 바꾼다. 규칙 동사는 -ed를 붙이되 자음 + y는 y를 i로 바꾸고(study - studied), 단모음 + 단자음은 자음을 겹친다(stop - stopped)."
_S45 = MEMO + "원문항과 함께, 이 단계에서 다루지 않는 불규칙 동사(eat, have, see, go, take)를 규칙 동사로 바꿔 문장과 보기를 새로 썼다."
def f45m(t, p, c, a, n): RE(6, 45, t, st="R", p=p, c=c, a=a, r=R45m, n=n, s=_S45 + pos(a))
f45m("B", "I play the piano.", ["I play the piano.", "I play the piano yesterday.", "I plaied the piano this morning.", "I plays the piano this morning.", "I played the piano this morning."], 5,
     ["과거를 나타내는 문장이 아니므로 오답이다.", "yesterday가 있는데 현재형 play를 썼으므로 오답이다.", "play는 모음 + y라 그대로 -ed를 붙여 played로 쓰므로 오답이다.", "주어 I에 plays를 쓸 수 없고 과거형도 아니므로 오답이다.", "play의 과거형 played를 바르게 썼고 때도 과거이므로 정답이다."])
f45m("C", "Tom wants a bike.", ["Tom wanted a bike last year.", "Tom wantted a bike last year.", "Tom wants a bike last year.", "Tom wants a bike yesterday.", "Tom wants a bike."], 1,
     ["want의 과거형 wanted를 바르게 썼고 때도 과거이므로 정답이다.", "want는 끝이 -nt라 자음을 겹치지 않고 wanted로 쓰므로 오답이다.", "last year가 있는데 현재형 wants를 썼으므로 오답이다.", "yesterday가 있는데 현재형 wants를 썼으므로 오답이다.", "과거를 나타내는 문장이 아니므로 오답이다."])
f45m("D", "They watch a movie.", ["They watches a movie.", "They watched a movie yesterday.", "They watched a movie tomorrow.", "They watch a movie yesterday.", "They watch a movie."], 2,
     ["주어 They에 watches를 쓸 수 없고 과거형도 아니므로 오답이다.", "watch의 과거형 watched를 바르게 썼고 때도 과거이므로 정답이다.", "과거형 watched에 미래의 tomorrow를 함께 썼으므로 오답이다.", "yesterday가 있는데 현재형 watch를 썼으므로 오답이다.", "과거를 나타내는 문장이 아니므로 오답이다."])
f45m("E", "She walks to school.", ["She walked to school yesterday.", "She walks to school yesterday.", "She walkked to school yesterday.", "She walks to school.", "She walked to school tomorrow."], 1,
     ["walk의 과거형 walked를 바르게 썼고 때도 과거이므로 정답이다.", "yesterday가 있는데 현재형 walks를 썼으므로 오답이다.", "walk는 끝이 -lk라 자음을 겹치지 않고 walked로 쓰므로 오답이다.", "과거를 나타내는 문장이 아니므로 오답이다.", "과거형 walked에 미래의 tomorrow를 함께 썼으므로 오답이다."])
f45m("F", "She stops at the bakery.", ["She stops at the bakery yesterday.", "She did stopped at the bakery yesterday.", "She stoped at the bakery yesterday.", "She stop at the bakery yesterday.", "She stopped at the bakery yesterday."], 5,
     ["yesterday가 있는데 현재형 stops를 썼으므로 오답이다.", "did와 과거형을 함께 쓰지 않으므로 오답이다.", "stop은 단모음 + 단자음이라 p를 겹쳐 stopped로 쓰므로 오답이다.", "과거형이 아니고 주어 She와도 맞지 않으므로 오답이다.", "stop의 과거형 stopped를 바르게 썼고 때도 과거이므로 정답이다."])

# 6-64 원문항처럼 3인칭 단수 주어의 조동사에 -s를 붙인 오답(밑줄은 조동사 한 낱말)
R64m = "조동사(can, may, must, should)는 주어가 3인칭 단수여도 -s를 붙이지 않고, 뒤에는 동사원형을 쓴다."
_S64 = MEMO + "원문항처럼 3인칭 단수 주어 뒤의 조동사에 -s를 붙인 것(cans, musts 등)을 정답으로 하고, 밑줄은 조동사 한 낱말에만 그었다."
def f64m(t, c, a):
    n = []
    for i, x in enumerate(c):
        m = _r.search(r"<u>(\w+)</u>", x).group(1)
        n.append(f"조동사 {m[:-1]}에는 주어가 3인칭 단수여도 -s를 붙이지 않으므로 정답이다." if i + 1 == a else f"조동사 {m} 뒤에 동사원형을 쓴 바른 문장이므로 오답이다.")
    RE(6, 64, t, c=c, a=a, r=R64m, n=n, s=_S64 + pos(a))
f64m("B", ["You <u>may</u> sit here.", "Jane <u>cans</u> swim very well.", "We <u>must</u> wear a helmet.", "She <u>should</u> go to bed early.", "I <u>can</u> ride a bike."], 2)
f64m("C", ["She <u>musts</u> finish her homework.", "We <u>should</u> listen to our teacher.", "You <u>may</u> take a cookie.", "I <u>must</u> go now.", "He <u>can</u> ride a horse."], 1)
f64m("D", ["You <u>should</u> wash your hands.", "I <u>may</u> be late today.", "Tom <u>shoulds</u> practice the drums.", "We <u>must</u> stop at the red light.", "They <u>may</u> visit us."], 3)
f64m("E", ["My dad <u>can</u> fix the car.", "You <u>must</u> not run here.", "It <u>may</u> snow tonight.", "She <u>mays</u> join us.", "We <u>should</u> save water."], 4)
f64m("F", ["Mina <u>can</u> speak French.", "You <u>may</u> use this computer.", "They <u>should</u> bring water.", "We <u>must</u> leave now.", "Tom <u>cans</u> arrive after lunch."], 5)

# 6-91 원문항처럼 단모음 + 단자음 짝이 정답이 되게
R91m = "-ing형 만들기: 대부분 그대로 -ing, -e로 끝나면 e를 빼고, 단모음 + 단자음이면 자음을 겹쳐 쓴다(cut → cutting, sit → sitting). -ie는 y로 바꾼다."
_K91 = {"P": "그대로 -ing를 붙인 옳은 형태이므로 오답이다.", "E": "-e를 빼고 -ing를 붙인 옳은 형태이므로 오답이다.", "D": "단모음 + 단자음이라 {ch}{j} 겹쳐 쓴 옳은 형태이므로 오답이다.", "IE": "-ie를 y로 바꾼 옳은 형태이므로 오답이다.",
        "X": "단모음 + 단자음이라 {ch}{j} 겹쳐 {form}으로 써야 하므로 정답이다."}
def _j91(ch): return "을" if ch in "nm" else "를"
def f91m(t, c, kinds, ch, form):
    a = kinds.index("X") + 1
    RE(6, 91, t, c=c, a=a, r=R91m, n=[_K91[k].format(ch=(ch if k == "X" else c[i].split("-")[0].strip()[-1]), j=_j91(ch if k == "X" else c[i].split("-")[0].strip()[-1]), form=form) for i, k in enumerate(kinds)],
       s=MEMO + "원문항(cut - cuting)처럼 단모음 + 단자음 동사의 자음을 겹치지 않은 짝이 정답이 되게 보기를 다시 썼다. 6급 81번 변형의 정답 동사(make, run, lie, swim, jog)와 겹치지 않는 동사를 썼다." + pos(a))
f91m("B", ["hit - hitting", "smile - smiling", "sit - siting", "sleep - sleeping", "drive - driving"], ["D", "E", "X", "P", "E"], "t", "sitting")
f91m("D", ["put - puting", "die - dying", "hope - hoping", "enjoy - enjoying", "get - getting"], ["X", "IE", "E", "P", "D"], "t", "putting")
f91m("F", ["begin - beginning", "carry - carrying", "come - coming", "shop - shoping", "see - seeing"], ["D", "P", "E", "X", "P"], "p", "shopping")

# ---------------- 7급 ----------------
# 7-81 번호를 넣은 문장을 제시문에 보이고 보기는 번호만
_S81 = MEMO + "발문의 ‘다음 문장’이 보이지 않아, 원문항과 함께 낱말 사이에 번호를 넣은 문장을 제시문에 보이고 보기는 번호만 두었다. 정답은 그대로다."
posm2(7, 81, "B", "", ["They", "play", "soccer", "today", "."], 2, _S81)
posm2(7, 81, "C", "", ["The", "twins", "swim", "very well", "."], 3, _S81)
posm2(7, 81, "D", "", ["My", "little", "sister", "sing", "."], 4, _S81)
posm2(7, 81, "E", "", ["We", "help", "our", "teacher", "."], 2, _S81)
posm2(7, 81, "F", "", ["His", "uncle", "fix", "bikes", "."], 3, _S81)

# 7-85 어려운 ‘can + to부정사’ 오답을 원문항처럼 be동사 형태 오류로
R85m = "can, can't, cannot 뒤에는 동사원형을 쓴다(be동사는 be). can에는 -s를 붙이지 않고, 뒤에 -s가 붙은 동사를 쓰지 않는다."
F(7, 85, "B", c=["They cannot enter now.", "Jane can be patient.", "I can carry this box.", "We can wait outside.", "Tom can is a good swimmer."], a=5, r=R85m,
  n=["cannot 뒤에 동사원형 enter를 썼으므로 오답이다.", "can 뒤에 be동사의 원형 be를 썼으므로 오답이다.", "can 뒤에 동사원형 carry를 썼으므로 오답이다.", "can 뒤에 동사원형 wait를 썼으므로 오답이다.", "can 뒤에는 is가 아니라 원형 be를 써야 하므로 정답이다."],
  s=MEMO + "이 단계보다 어려운 ⑤ can to fix(to부정사)를 원문항(can are)처럼 can 뒤에 be동사의 활용형을 쓴 오답(can is)으로 바꿨다." + pos(5))
_o85 = OLD(7, 85, "C"); _c85 = list(_o85["c"]); _n85 = list(_o85["n"]); _c85[3] = "She can is a good singer."; _n85[3] = "can 뒤에는 is가 아니라 원형 be를 써야 하므로 정답이다."
RE(7, 85, "C", c=_c85, n=_n85, s=_o85["s"] + " " + MEMO + "B와 같은 이유로 ④ can to sing을 can is로 바꿨다.")
