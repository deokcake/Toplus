# 7급 CH5 지시대명사 this·that·these·those (41~50) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
R_DM = "this(이것)·that(저것)은 한 개를 가리켜 is와 쓰고, these(이것들)·those(저것들)는 여러 개를 가리켜 are와 쓴다. 대답에서는 this/that을 it으로, these/those를 they로 받는다."

# 7-42 This/That이 들어갈 수 없는 것: 원문항 발문, 원문항 문장을 되풀이하지 않고 새로
S742 = "발문에 ‘실제 사람이나 물건을 가리킬 때’가 붙었고, 옳은 오답 문장이 원문항 선택지 그대로였다. 원문항 발문으로 되돌리고 유형마다 문장을 새로 썼다."
OK42 = "is와 함께 한 사람·한 물건을 가리키므로 This/That이 들어갈 수 있으므로"; NO42 = "are와 복수 명사가 오므로 This/That이 아니라 These/Those가 들어가야 하므로"
def f742(t, items, a, s=S742):
    mk(7, 42, t, [(x, w or OK42) for x, w in items], a, R_DM, s, st="R")
f742("B", [("_______ is my aunt.", ""), ("_______ is a big tree.", ""), ("_______ is an egg.", ""), ("_______ is the school bus.", ""), ("_______ are our bags.", NO42)], 5)
f742("C", [("_______ is a red pen.", ""), ("_______ is our classroom.", ""), ("_______ is an eraser.", ""), ("_______ are apples.", NO42), ("_______ is my grandpa.", "")], 4)
f742("D", [("_______ is my father.", ""), ("_______ are my books.", NO42), ("_______ is the new comic.", ""), ("_______ is a river.", ""), ("_______ is an umbrella.", "")], 2)
f742("E", [("_______ are birds.", NO42), ("_______ is the small book.", ""), ("_______ is a cat.", ""), ("_______ is a banana.", ""), ("_______ is my sister.", "")], 1)
f742("F", [("_______ is a lamp.", ""), ("_______ is your ticket.", ""), ("_______ are my cousins.", NO42), ("_______ is an old bridge.", ""), ("_______ is my uncle.", "")], 3,
     "발문에 ‘실제 사람이나 물건을 가리킬 때’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 7-43 대답에 맞는 질문: B는 상황 설명 삭제, C~F는 오답 질문을 새로
R743 = "No, they aren't.는 these/those나 복수 명사를 they로 받은 대답이다. this/that/it(한 개)은 it으로, you는 I/we로, she는 she로 받는다."
T_ = "this·that으로 한 개를 물으면 대답에서 it으로 받으므로"; YOU = "you에 대한 질문에는 I나 we로 답하므로"; IT = "it에 대한 질문에는 it으로 답하므로"
def f743(t, items, a, s, **kw):
    mk(7, 43, t, items, a, R743, s, **kw)
f743("B", [("Is it your scarf?", IT), ("Are those your scarf?", "those 뒤에는 복수 명사 scarves를 써야 하므로"), ("Is this your scarf?", T_), ("Are those your scarves?", "those를 they로 받아 대답할 수 있으므로"), ("Is that his jacket?", T_)], 4,
     "원문항에 없던 상황 설명(At the lost-and-found desk …)이 붙었다. 상황 설명을 지웠다. 보기와 정답은 그대로다.", p="A: _______________________\nB: No, they aren't.")
S743 = "오답 네 개가 원문항 선택지 그대로였다. 원문항처럼 한 개를 묻는 질문과 you를 묻는 질문으로 오답을 유형마다 새로 썼다."
f743("C", [("Are these her shoes?", "these를 they로 받아 대답할 수 있으므로"), ("Is this your umbrella?", T_), ("Are you students?", YOU), ("Is that his cap?", T_), ("Is it a pencil?", IT)], 1, S743, p="A: _______________________\nB: Yes, they are.")
f743("D", [("Is it your notebook?", IT), ("Are you and Tom friends?", "you and Tom에 대한 질문에는 we로 답하므로"), ("Are those his cars?", "those를 they로 받아 대답할 수 있으므로"), ("Is this a lemon?", T_), ("Is that her bike?", T_)], 3, S743, p="A: _______________________\nB: No, they're my sister's.")
f743("E", [("Is that a bird?", T_), ("Are you tired?", YOU), ("Is this your desk?", T_), ("Are those your books?", "those를 they로 받아 대답할 수 있으므로"), ("Is it hot?", IT)], 4, S743, p="A: _______________________\nB: Yes, they're mine.")
f743("F", [("Is this your eraser?", T_), ("Are these my pencils?", "these를 they로 받아 대답할 수 있으므로"), ("Is she your sister?", "she에 대한 질문에는 she로 답하므로"), ("Are you ready?", YOU), ("Is that a cloud?", T_)], 2, S743, p="A: _______________________\nB: No, they're not.")

# 7-44 우리말 → 영어: 원문항 발문, 같은 우리말을 틀리게 옮긴 오답
R744 = "‘이것들은 ~이니?’는 Are these ~?, ‘저것들은 ~이니?’는 Are those ~?로 옮긴다. these/those 뒤에는 are와 복수 명사를 쓴다."
S744 = "오답이 우리말과 관계없는 문장이라 바로 지워졌고 유형마다 반복되었다. 원문항 발문으로 되돌리고, 원문항처럼 같은 우리말을 틀리게 옮긴 문장으로 오답을 새로 썼다."
def f744(t, ko, items, a, s=S744):
    mk(7, 44, t, items, a, R744, s, st="R", p=ko)
F(7, 44, "B", st="R", r=R744, n=["‘이것들’을 these, 복수 주어에 Are, 복수 명사 keys로 바르게 옮겼으므로 정답이다.", "‘이것들’은 those가 아니라 these이고 명사도 복수 keys로 써야 하므로 오답이다.", "복수 주어 these에는 Is가 아니라 Are를 쓰므로 오답이다.", "‘이것들’은 여러 개라 this와 key로 옮길 수 없으므로 오답이다.", "‘이것들’은 this가 아니라 these로 옮겨야 하므로 오답이다."],
  s="발문에 ‘일반적인 be동사 의문문으로’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f744("C", "이것들은 사과들이니?", [("Is this an apple?", "‘이것들’은 여러 개라 this와 an apple로 옮길 수 없으므로"), ("Are those apples?", "‘이것들’은 those가 아니라 these이므로"), ("Is these apples?", "복수 주어 these에는 Are를 쓰므로"), ("Are this apples?", "‘이것들’은 this가 아니라 these이므로"), ("Are these apples?", "‘이것들’을 these, 복수 주어에 Are로 바르게 옮겼으므로")], 5)
f744("D", "저것들은 네 책들이니?", [("Is that your book?", "‘저것들’은 여러 개라 that과 book으로 옮길 수 없으므로"), ("Are these your books?", "‘저것들’은 these가 아니라 those이므로"), ("Are those your books?", "‘저것들’을 those, 복수 주어에 Are로 바르게 옮겼으므로"), ("Is those your books?", "복수 주어 those에는 Are를 쓰므로"), ("Are that your books?", "‘저것들’은 that이 아니라 those이므로")], 3)
f744("E", "저것들은 자동차들이니?", [("Are that cars?", "‘저것들’은 that이 아니라 those이므로"), ("Is that a car?", "‘저것들’은 여러 개라 that과 a car로 옮길 수 없으므로"), ("Are these cars?", "‘저것들’은 these가 아니라 those이므로"), ("Are those cars?", "‘저것들’을 those, 복수 주어에 Are로 바르게 옮겼으므로"), ("Is those cars?", "복수 주어 those에는 Are를 쓰므로")], 4)
f744("F", "이것들은 그녀의 신발들이니?", [("Is these her shoes?", "복수 주어 these에는 Are를 쓰므로"), ("Are these her shoes?", "‘이것들’을 these, 복수 주어에 Are로 바르게 옮겼으므로"), ("Is this her shoe?", "‘이것들’은 여러 개라 this와 shoe로 옮길 수 없으므로"), ("Are those her shoes?", "‘이것들’은 those가 아니라 these이므로"), ("Are this her shoes?", "‘이것들’은 this가 아니라 these이므로")], 2)

# 7-45 지시어·대명사 짝: 원문항 발문(상황 설명 없이), 정답 조합을 유형마다 다르게
S745 = "발문이 ‘여러 물건을 가까이(멀리)에서 가리키며 묻고 … 대답’이라고 두 빈칸의 정답을 알려 주었다. 원문항 발문으로 되돌리고 상황 설명을 지웠다. 조건 없이도 답이 하나로 정해지도록, 원문항처럼 they와 짝을 이루는 지시어는 선택지에 하나만 두었다."
def f745(t, p, items, a, s=S745):
    mk(7, 45, t, items, a, R_DM, s, st="R", p=p, okdup=True)
IT1 = "여러 개를 가리키는 말은 대답에서 it이 아니라 they로 받으므로"; SG = "this/that은 한 개를 가리켜 Are와 함께 쓸 수 없으므로"
f745("B", "A: Are ________ our tickets?\nB: Yes, ________ are.", [("those - it", IT1), ("these - they", "여러 개를 가리키는 these와 대답의 they를 바르게 짝지었으므로"), ("these - it", IT1), ("that - it", SG), ("this - it", SG)], 2)
f745("C", "A: Are ________ my pencils?\nB: Yes, ________ are.", [("these - it", IT1), ("those - it", IT1), ("these - they", "여러 개를 가리키는 these와 대답의 they를 바르게 짝지었으므로"), ("this - it", SG), ("that - it", SG)], 3)
f745("D", "A: Is ________ your bag?\nB: Yes, ________ is.", [("this - it", "한 개를 가리키는 this와 대답의 it을 바르게 짝지었으므로"), ("these - they", "these는 여러 개를 가리켜 Is와 함께 쓸 수 없으므로"), ("this - they", "this가 가리키는 한 개는 대답에서 it으로 받으므로"), ("those - it", "those는 여러 개를 가리켜 Is와 함께 쓸 수 없으므로"), ("these - it", "these는 여러 개를 가리켜 Is와 함께 쓸 수 없으므로")], 1,
     S745 + " 정답 조합이 원문항(those - they)과 같지 않게 한 개를 묻는 대화로 바꿨다.")
f745("E", "A: Is ________ his car?\nB: No, ________ isn't.", [("those - they", "those는 여러 개를 가리켜 Is와 함께 쓸 수 없으므로"), ("that - they", "that이 가리키는 한 개는 대답에서 it으로 받으므로"), ("that - it", "한 개를 가리키는 that과 대답의 it을 바르게 짝지었으므로"), ("these - it", "these는 여러 개를 가리켜 Is와 함께 쓸 수 없으므로"), ("those - it", "those는 여러 개를 가리켜 Is와 함께 쓸 수 없으므로")], 3,
     S745 + " 정답 조합(those - they)이 원문항과 같아 한 개를 묻는 대화로 바꿨다.")
f745("F", "A: Are ________ her shoes?\nB: No, ________ aren't.", [("this - it", SG), ("that - they", SG), ("these - it", IT1), ("this - they", SG), ("these - they", "여러 개를 가리키는 these와 대답의 they를 바르게 짝지었으므로")], 5,
     S745 + " 정답 조합(those - they)이 원문항과 같아, 선택지에 those 대신 these를 두어 정답이 these - they가 되게 했다.")

# 7-47 No 대답: 원문항처럼 ‘No, ___ ___’ 두 빈칸 형식, 원문항 발문
R747 = "Is this/that ~?에는 No, it isn't.로, Are these/those ~?에는 No, they aren't.로 답한다. 부정 대답에는 be동사 + not을 쓴다."
S747 = "원문항은 ‘No, ___ ___’ 두 빈칸 형식인데 변형은 대답 문장 전체를 고르는 형식이거나 빈칸이 한 칸이었고, 발문 조건만으로 Yes 대답이 지워졌으며 오답이 유형마다 같았다. 원문항 발문과 두 빈칸 형식으로 되돌리고 유형마다 오답을 새로 썼다."
def f747(t, q, items, a, s=S747):
    mk(7, 47, t, items, a, R747, s, st="R", p=f"A: {q}\nB: No, _______ _______.")
TY = "these/those는 대답에서 they로 받으므로"; ITS = "this/that은 대답에서 it으로 받으므로"; NN = "No로 답했으므로 부정형을 써야 하므로"; NOT = "be동사 없이 not만 쓸 수 없으므로"
f747("B", "Is that his car?", [("it is", NN), ("they aren't", ITS), ("it isn't", "that을 it으로 받아 isn't로 바르게 답했으므로"), ("it not", NOT), ("they isn't", ITS)], 3)
f747("C", "Are these the team helmets?", [("it isn't", TY), ("they not", NOT), ("they are", NN), ("they aren't", "these를 they로 받아 aren't로 바르게 답했으므로"), ("it is", TY)], 4)
f747("D", "Are these her shoes?", [("they aren't", "these를 they로 받아 aren't로 바르게 답했으므로"), ("it isn't", TY), ("they are", NN), ("it not", NOT), ("they isn't", "주어 they에는 isn't가 아니라 aren't를 쓰므로")], 1)
f747("E", "Is this your bag?", [("it are", "주어 it에는 are가 아니라 is를 쓰고 No로 답했으므로"), ("it isn't", "this를 it으로 받아 isn't로 바르게 답했으므로"), ("it is", NN), ("they aren't", ITS), ("it not", NOT)], 2)
f747("F", "Are those your books?", [("they is", "주어 they에는 is를 쓰지 않고 No로 답했으므로"), ("it isn't", TY), ("they are", NN), ("they not", NOT), ("they aren't", "those를 they로 받아 aren't로 바르게 답했으므로")], 5)

# 7-48 세 번째 단어: 원문항 발문과 우리말 해석, 주어를 알려 주지 않도록 소문자로
R748 = "‘이것은/저것은 ~의 … 이다’는 This/That + is + 소유격 + 형용사 + 명사의 순서로 배열한다."
S748 = "발문이 ‘That(This)을 주어로 쓰고’라고 첫 단어를 알려 주었고 원문항의 우리말 해석이 빠졌다. 원문항 발문으로 되돌리고 우리말 해석을 붙였으며, 원문항처럼 제시어를 소문자로 주어 첫 단어를 알려 주지 않게 했다. 정답은 그대로다."
def f748(t, ko, words, sent):
    V_ = V(7, 48, t); a = int(V_["ans"]); opts = [o.lower() for o in V_["c"]]
    pos = {w.lower(): i + 1 for i, w in enumerate(sent.rstrip(".").split())}
    F(7, 48, t, st="R", p=f"{ko}\n( {' / '.join(words)} / . )", c=opts, a=a, r=R748, k=f"완성 문장은 {sent}이고 세 번째 단어는 {opts[a-1]}이다.",
      n=[f"완성 문장 {sent}에서 단어({o})는 {pos[o]}번째에 오므로" + (" 정답이다." if i + 1 == a else " 오답이다.") for i, o in enumerate(opts)], okdup=True, s=S748)
f748("B", "저것은 나의 새 배낭이다.", ["new", "backpack", "my", "that", "is"], "That is my new backpack.")
f748("C", "이것은 그의 빨간 차이다.", ["his", "this", "red", "is", "car"], "This is his red car.")
f748("D", "저것은 나의 새 책이다.", ["my", "that", "new", "is", "book"], "That is my new book.")
f748("E", "저것은 그녀의 작은 가방이다.", ["her", "that", "small", "is", "bag"], "That is her small bag.")
f748("F", "이것은 그들의 멋진 집이다.", ["their", "this", "nice", "is", "house"], "This is their nice house.")

# 7-49 <보기> 고쳐 쓰기: 원문항 발문, <보기> 문장을 틀리게 고친 오답
R749 = "지시어와 be동사, 명사의 수를 함께 맞춘다. this/that + is + a/an + 단수 명사, these/those + are + 복수 명사로 쓰고, a/an은 첫소리로 정한다."
S749 = "오답 대부분이 <보기> 문장과 관계없는 문장이라 바로 지워졌고 유형마다 반복되었으며, 발문에 조건이 붙었다. 원문항 발문으로 되돌리고, 원문항처럼 <보기> 문장을 틀리게 고친 것으로 오답을 새로 썼다."
def f749(t, bogi, items, a, s=S749):
    mk(7, 49, t, items, a, R749, s, st="R", p=f"<보기>\n{bogi}")
f749("B", "Is this two bags?", [("Is these two bags?", "복수 주어 these에는 Is가 아니라 Are를 쓰므로"), ("Are these two bags?", "여러 개를 가리키는 these, are, 복수 명사를 바르게 맞췄으므로"), ("Are this two bags?", "두 개를 가리키므로 this가 아니라 these를 써야 하므로"),
     ("Is this two bag?", "two 뒤에는 복수 명사 bags를 쓰고, 여러 개는 these와 are로 나타내므로"), ("Are these two bag?", "two 뒤에는 복수 명사 bags를 써야 하므로")], 2)
F(7, 49, "C", st="R", r=R749, n=["those, are, 복수 명사 cars를 바르게 맞췄으므로 정답이다.", "복수 주어 those에는 Is가 아니라 Are를 쓰므로 오답이다.", "that과 a car로 바꾸면 한 대를 가리키는데 Are를 썼으므로 오답이다.", "복수 명사 cars 앞에는 a를 쓰지 않으므로 오답이다.", "that은 한 개를 가리켜 복수 명사 cars와 쓸 수 없으므로 오답이다."],
  s="발문에 ‘실제 물건의 수에 맞는 기본 지시 표현으로’ 조건이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f749("D", "Is that an car?", [("Is that an cars?", "car는 자음 소리로 시작해 a를 쓰고 한 대라 단수 car를 쓰므로"), ("Are that cars?", "that은 한 개를 가리켜 Are, 복수 명사와 함께 쓸 수 없으므로"), ("Is those a car?", "한 대를 가리키므로 those가 아니라 that을 쓰므로"), ("Is that a car?", "자음 소리로 시작하는 car 앞에 a를 바르게 고쳤으므로"), ("Is that a cars?", "a 뒤에는 단수 명사 car를 써야 하므로")], 4)
f749("E", "Are those a apple?", [("Are those a apples?", "복수 명사 apples 앞에는 a를 쓰지 않으므로"), ("Is those apples?", "복수 주어 those에는 Is가 아니라 Are를 쓰므로"), ("Are that an apple?", "단수 주어 that에는 Are가 아니라 Is를 쓰므로"), ("Are those an apple?", "those는 여러 개라 an apple(한 개)과 쓸 수 없으므로"), ("Are those apples?", "those, are, 복수 명사 apples를 바르게 맞췄으므로")], 5)
f749("F", "Are these a books?", [("Are these a book?", "these는 여러 개라 a book(한 권)과 쓸 수 없으므로"), ("Is these books?", "복수 주어 these에는 Is가 아니라 Are를 쓰므로"), ("Are these books?", "these, are, 복수 명사 books를 바르게 맞췄으므로"), ("Are this books?", "여러 권을 가리키므로 this가 아니라 these를 쓰므로"), ("Is this a books?", "a 뒤에는 단수 명사를 쓰고, 여러 권은 these와 are로 나타내므로")], 3)

# 7-50 be동사가 앞으로 나온 이유: D~F는 원문항처럼 그럴듯한 오개념 오답을 새로
R750 = "be동사를 주어 앞으로 옮기면 ‘~이니?’라고 묻는 의문문이 된다. 강조, 명사의 수, 단어의 뜻 때문에 be동사가 앞으로 나오는 것이 아니다."
S750 = "오답 네 개가 B와 똑같았다. 원문항처럼 강조, 복수, 단어 뜻 같은 그럴듯한 오개념으로 유형마다 오답을 새로 썼다."
Q = "be동사를 주어 앞으로 옮겨 묻는 의문문을 만든 것이므로"
def f750(t, items, a, s=S750):
    mk(7, 50, t, items, a, R750, s)
f750("D", [("these가 '이것들'이라는 뜻이라서", "단어의 뜻 때문이 아니라 의문문을 만들기 위해서이므로"), ("\"~이니?\"라고 묻는 의문문을 만들기 위해서", Q), ("your를 강조하고 싶어서", "강조하려고 be동사를 앞으로 옮기지 않으므로"),
           ("books가 여러 권이라 복수임을 알리려고", "명사의 수는 be동사의 형태(are)로 나타낼 뿐 위치를 바꾸는 이유가 아니므로"), ("질문이든 아니든 be동사는 항상 맨 앞에 오기 때문에", "평서문에서는 주어가 be동사 앞에 오므로")], 2)
f750("E", [("those를 강조해 멀리 있는 것임을 알리려고", "강조하려고 be동사를 앞으로 옮기지 않으므로"), ("his가 소유격이라 be동사가 앞으로 나와야 해서", "소유격은 be동사의 위치와 관계없으므로"), ("\"저것들이 그의 차들이니?\"라고 묻는 의문문이 되도록", Q),
           ("cars가 복수라서 are가 항상 맨 앞에 와야 해서", "복수 주어라도 평서문에서는 are가 주어 뒤에 오므로"), ("대답을 준비하는 문장이라서", "대답이 아니라 묻는 문장이라 be동사가 앞에 오므로")], 3)
f750("F", [("bag이 한 개라서", "명사의 수는 be동사의 위치를 바꾸는 이유가 아니므로"), ("this가 '이것'이라는 뜻이라서", "단어의 뜻 때문이 아니라 의문문을 만들기 위해서이므로"), ("your를 강조하기 위해서", "강조하려고 be동사를 앞으로 옮기지 않으므로"),
           ("\"이것이 네 가방이니?\"라고 묻는 의문문을 만들기 위해서", Q), ("짧은 문장은 be동사로 시작하기 때문에", "문장의 길이는 be동사의 위치와 관계없으므로")], 4)

# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, r, s, **kw):
    FIX.pop((7, n, t), None)
    mk(7, n, t, items, a, r, s, **kw)
ONE = lambda w: f"{w}은(는) 한 개를 가리켜 are와 쓸 수 없으므로"
# 7-41 D: 원문항에 없는 문장(Look over there.)과 풀이식 우리말 → 원문항처럼 문장의 우리말 해석
F(7, 41, "D", p="_______ are mountains.\n(저것들은 산들이다.)", r=R_DM,
  n=["‘저것들’은 멀리 있는 여러 개를 가리키는 Those이고 are와도 어울리므로 정답이다.", "It은 한 개를 가리켜 are와 쓸 수 없으므로 오답이다.", "These는 ‘이것들’이라는 뜻이므로 오답이다.", "This는 한 개를 가리켜 are와 쓸 수 없으므로 오답이다.", "That은 한 개를 가리켜 are와 쓸 수 없으므로 오답이다."],
  s="원문항에 없는 문장(Look over there.)이 붙었고, 우리말 해석이 문장 전체가 아니라 ‘(저쪽에 있는 산들)’이라는 풀이로 바뀌었다. 같은 유형의 46번 변형(Look over there. ___ are horses.)과도 짜임이 똑같았다. 덧붙은 문장을 지우고 원문항처럼 문장의 우리말 해석을 붙였다. 보기와 정답은 그대로다. 정답 위치 ①.")
# 7-46 D: 원문항에 없는 문장(Look over there.)이 괄호 안의 설명과 같은 단서를 두 번 줌
R746 = "가까이 있는 것은 this(한 개)·these(여러 개), 멀리 있는 것은 that(한 개)·those(여러 개)로 가리킨다. these/those는 are와 쓴다."
F(7, 46, "D", p="_______ are horses.\n(멀리 있는 말들을 가리키며)", r=R746,
  n=["It은 한 마리를 가리켜 are와 쓸 수 없으므로 오답이다.", "멀리 있는 여럿을 가리키는 Those가 are와 어울리므로 정답이다.", "That은 한 마리를 가리켜 are와 쓸 수 없으므로 오답이다.", "This는 한 마리를 가리켜 are와 쓸 수 없으므로 오답이다.", "These는 가까이 있는 여럿을 가리키므로 오답이다."],
  s="원문항에 없는 문장(Look over there.)이 붙어 괄호 안의 설명과 같은 단서를 두 번 주었고, 같은 유형의 41번 변형(Look over there. ___ are mountains.)과도 짜임이 똑같았다. 덧붙은 문장을 지우고 원문항처럼 괄호 안의 상황 설명만 두었다. 보기와 정답은 그대로다. 정답 위치 ②.")
# 7-43 B: ②가 틀린 질문(Are those your scarf?), 정답 위치가 원문항과 같은 ④
redo(43, "B", [("Is it your scarf?", IT), ("Are you cold?", YOU), ("Is this your scarf?", T_), ("Is that his jacket?", T_), ("Are those your scarves?", "those를 they로 받아 대답할 수 있으므로")], 5, R743,
     "원문항에 없던 상황 설명(At the lost-and-found desk …)이 붙었다. 또 ②(Are those your scarf?)는 질문 자체가 틀린 문장이라 대답과 견주지 않아도 지워졌고(원문항의 보기는 모두 옳은 질문이다), 정답 위치(④)가 원문항과 같았다. 상황 설명을 지우고 ②를 옳은 질문으로 바꿨으며 정답을 ⑤로 옮겼다.",
     p="A: _______________________\nB: No, they aren't.")
# 7-48: 원문항처럼 제시어 순서 = 보기 순서 / D는 B와 명사만 다른 문장 → 새 문장
R748B = "‘이것(들)은/저것(들)은 ~의 … 이다’는 지시대명사 + be동사 + 소유격 + 형용사 + 명사의 순서로 배열한다. this/that에는 is, these/those에는 are를 쓴다."
S748B = "발문이 ‘That(This)을 주어로 쓰고’라고 첫 단어를 알려 주었고 원문항의 우리말 해석이 빠졌다. 원문항 발문으로 되돌리고 우리말 해석을 붙였으며, 원문항처럼 제시어를 소문자로, 보기와 같은 순서로 주어 첫 단어를 알려 주지 않게 했다."
def g748(t, ko, sent, opts, a, s):
    FIX.pop((7, 48, t), None)
    pos = {w.lower(): i + 1 for i, w in enumerate(sent.rstrip(".").split())}
    F(7, 48, t, st="R", p=f"{ko}\n( {' / '.join(opts)} / . )", c=opts, a=a, r=R748B, k=f"완성 문장은 {sent}이고 세 번째 단어는 {opts[a-1]}이다.",
      n=[f"완성 문장 {sent}에서 단어({o})는 {pos[o]}번째에 오므로" + (" 정답이다." if i + 1 == a else " 오답이다.") for i, o in enumerate(opts)], okdup=True, s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
g748("B", "저것은 나의 새 배낭이다.", "That is my new backpack.", ["is", "backpack", "new", "that", "my"], 5, S748B + " 정답은 그대로다.")
g748("C", "이것은 그의 빨간 차이다.", "This is his red car.", ["red", "this", "is", "his", "car"], 4, S748B + " 정답은 그대로다.")
g748("D", "저것들은 너의 새 신발들이다.", "Those are your new shoes.", ["shoes", "your", "are", "new", "those"], 2,
     S748B + " 또 문장(That is my new book.)이 B(That is my new backpack.)와 명사만 다르고 정답(my)과 그 위치(⑤)도 같아, 주어가 those인 문장으로 바꿨다.")
g748("E", "저것은 그녀의 작은 가방이다.", "That is her small bag.", ["her", "that", "is", "bag", "small"], 1, S748B + " 정답은 그대로다.")
g748("F", "이것은 그들의 멋진 집이다.", "This is their nice house.", ["house", "is", "their", "nice", "this"], 3, S748B + " 정답은 그대로다.")
# 7-49 E: <보기>와 고친 문장의 짜임이 C(Are those a car? → Are those cars?)와 같음
redo(49, "E", [("Is these an orange?", "한 개(an orange)를 가리키므로 these가 아니라 this를 써야 하므로"), ("Are this an orange?", "단수 주어 this에는 Are가 아니라 Is를 쓰므로"), ("Is this a orange?", "orange는 모음 소리로 시작해 a가 아니라 an을 쓰므로"),
     ("Are these an orange?", "these와 Are는 여러 개에 쓰는데 an orange는 한 개이므로"), ("Is this an orange?", "한 개를 가리키는 this, is, an orange를 바르게 맞췄으므로")], 5, R749,
     S749 + " 또 <보기>(Are those a apple?)와 고친 문장이 C(Are those a car? → Are those cars?)와 짜임이 같아, 지시어와 관사를 함께 고치는 문장으로 바꿨다.", st="R", p="<보기>\nIs these a orange?")
# 7-50 B: 오답이 짧은 일반론이고 정답만 길고 구체적 / D: 정답 문구가 원문항과 거의 같음
redo(50, "B", [("'teacher'가 한 명이라는 것을 알려 주기 위해서", "명사의 수는 be동사의 위치를 바꾸는 이유가 아니므로"), ("'her'가 '그녀의'라는 뜻이기 때문에", "단어의 뜻 때문이 아니라 의문문을 만들기 위해서이므로"),
     ("be동사는 주어보다 중요한 말이기 때문에", "평서문에서는 주어가 be동사 앞에 오며, 더 중요해서 앞에 오는 것이 아니므로"), ("'that'이 멀리 있는 사람을 가리키기 때문에", "that의 뜻은 be동사의 위치와 관계없으므로"),
     ("\"저분이 그녀의 선생님이니?\"라고 묻는 의문문을 만들기 위해서", Q)], 5, R750,
     "오답이 문장 속 낱말과 관계없는 짧은 일반론(‘명사를 강조하기 위해서이다’ 등)이고 정답만 길고 구체적이어서 길이만으로 답이 드러났다. 정답 위치(①)도 C와 같았다. 원문항처럼 문장 속 낱말을 두고 말하는 오개념으로 오답을 새로 쓰고, 보기의 말투도 원문항처럼 ‘~해서/~때문에’로 맞췄다.")
redo(50, "D", [("these가 '이것들'이라는 뜻이라서", "단어의 뜻 때문이 아니라 의문문을 만들기 위해서이므로"), ("주어 these 앞에 be동사를 두어 묻는 문장(의문문)을 만들기 위해서", Q), ("your를 강조하고 싶어서", "강조하려고 be동사를 앞으로 옮기지 않으므로"),
     ("books가 여러 권이라 복수임을 알리려고", "명사의 수는 be동사의 형태(are)로 나타낼 뿐 위치를 바꾸는 이유가 아니므로"), ("질문이든 아니든 be동사는 항상 맨 앞에 오기 때문에", "평서문에서는 주어가 be동사 앞에 오므로")], 2, R750,
     S750 + " 정답은 원문항의 정답 문구를 그대로 쓰지 않고 이 문장에 맞춰 썼다.")
