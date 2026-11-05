# 5급 CH3 과거 시제 (21~30) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
R_PAST = "과거의 일은 동사의 과거형으로 쓴다. be동사 과거형은 I·3인칭 단수에 was, you·복수에 were를 쓰고, 일반동사는 -ed를 붙이거나 불규칙 과거형(go → went, buy → bought)을 쓴다."

# 5-21, 5-27 원문항 발문
F(5, 21, "B", st="R", s="발문이 ‘과거의 일을 나타내지 않는 문장’으로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
F(5, 27, "B", st="R", s="발문에 ‘과거 부정문’이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 5-23 빈칸 짝: 원문항 발문(시제·동사 안내 없이), 문장에 시간 표현
S523 = "발문에 ‘두 빈칸을 모두 과거형으로, 둘째 빈칸에는 ○○를 알맞게 바꾸어’가 붙어 시제와 동사를 알려 주었다. 원문항 발문으로 되돌리고, 문장에 과거를 나타내는 시간 표현을 넣어 정답이 하나로 정해지게 했다."
def f523(t, p, items, a, s=S523):
    mk(5, 23, t, items, a, R_PAST, s, st="R", p=p, okdup=True)
f523("B", "The road _______ icy last night, so Dad _______ very slowly.",
     [("was — drive", "둘째 빈칸: last night의 일이라 과거형 drove를 써야 하므로"), ("was — drived", "둘째 빈칸: drive의 과거형은 불규칙형 drove이므로"), ("is — drove", "첫째 빈칸: last night의 일이라 was를 써야 하므로"),
      ("were — drove", "첫째 빈칸: 단수 주어 The road에는 was를 써야 하므로"), ("was — drove", "단수 주어의 be동사 과거형 was와 drive의 과거형 drove를 바르게 짝지었으므로")], 5)
f523("C", "Tom and I _______ at the beach yesterday.\nWe _______ in the sea all day.",
     [("were — swam", "복수 주어의 be동사 과거형 were와 swim의 과거형 swam을 바르게 짝지었으므로"), ("was — swam", "첫째 빈칸: 복수 주어 Tom and I에는 were를 써야 하므로"), ("were — swimmed", "둘째 빈칸: swim의 과거형은 불규칙형 swam이므로"),
      ("are — swam", "첫째 빈칸: yesterday의 일이라 were를 써야 하므로"), ("were — swim", "둘째 빈칸: 어제의 일이라 과거형 swam을 써야 하므로")], 1,
     "정답 조합(was — bought)이 원문항과 같았고 발문이 시제와 동사를 알려 주었다. 원문항 발문으로 되돌리고, 정답 조합이 원문항과 다르도록(were — swam) 문장을 새로 썼다.")
f523("D", "They _______ busy last week.\nWe _______ the movie last Sunday.",
     [("was — saw", "첫째 빈칸: 복수 주어 They에는 were를 써야 하므로"), ("were — saw", "복수 주어의 be동사 과거형 were와 see의 과거형 saw를 바르게 짝지었으므로"), ("are — saw", "첫째 빈칸: last week의 일이라 were를 써야 하므로"),
      ("were — see", "둘째 빈칸: last Sunday의 일이라 과거형 saw를 써야 하므로"), ("were — seed", "둘째 빈칸: see의 과거형은 불규칙형 saw이므로")], 2)
f523("E", "I _______ tired yesterday.\nI _______ lunch at noon that day.",
     [("is — ate", "첫째 빈칸: 주어 I에는 am/was를 쓰고, yesterday의 일이라 was를 써야 하므로"), ("were — ate", "첫째 빈칸: 주어 I의 be동사 과거형은 was이므로"), ("was — ate", "주어 I의 be동사 과거형 was와 eat의 과거형 ate를 바르게 짝지었으므로"),
      ("was — eated", "둘째 빈칸: eat의 과거형은 불규칙형 ate이므로"), ("was — eat", "둘째 빈칸: that day(그날)의 일이라 과거형 ate를 써야 하므로")], 3)
f523("F", "Jane _______ happy last Sunday.\nShe _______ a cake for her friends.",
     [("was — maked", "둘째 빈칸: make의 과거형은 불규칙형 made이므로"), ("was — make", "둘째 빈칸: 지난 일요일의 일이라 과거형 made를 써야 하므로"), ("is — made", "첫째 빈칸: last Sunday의 일이라 was를 써야 하므로"),
      ("was — made", "단수 주어의 be동사 과거형 was와 make의 과거형 made를 바르게 짝지었으므로"), ("were — made", "첫째 빈칸: 단수 주어 Jane에는 was를 써야 하므로")], 4)

# 5-24 과거형 동사 형태가 잘못된 문장: 짝 없이 유형마다 새로
S524 = "정답 문장과 같은 문장의 옳은 과거형이 함께 있어 대비 단서가 되었고 오답 네 개가 유형마다 같았다. 짝 문장 없이 유형마다 새로 썼다."
def f524(t, items, a, s=S524):
    mk(5, 24, t, items, a, R_PAST, s)
f524("C", [("Mina sent me a card.", "send의 과거형 sent를 바르게 썼으므로"), ("We swam in the lake.", "swim의 과거형 swam을 바르게 썼으므로"), ("Dad cooked dinner for us.", "cook의 과거형 cooked를 바르게 썼으므로"),
           ("The dog runned to the door.", "run의 과거형은 불규칙형 ran이므로"), ("I lost my key yesterday.", "lose의 과거형 lost를 바르게 썼으므로")], 4)
f524("D", [("They built a tree house.", "build의 과거형 built를 바르게 썼으므로"), ("My sister cried at the movie.", "cry의 과거형 cried를 바르게 썼으므로"), ("We met our teacher at the mall.", "meet의 과거형 met을 바르게 썼으므로"),
           ("Tom dropped his phone.", "drop의 과거형 dropped를 바르게 썼으므로"), ("Jane thinked about her future.", "think의 과거형은 불규칙형 thought이므로")], 5)
f524("E", [("The bell rang at nine.", "ring의 과거형 rang을 바르게 썼으므로"), ("I planned a trip to Busan.", "plan의 과거형 planned를 바르게 썼으므로"), ("She sleeped late on Sunday.", "sleep의 과거형은 불규칙형 slept이므로"),
           ("Dad drove us to school.", "drive의 과거형 drove를 바르게 썼으므로"), ("They sold their old car.", "sell의 과거형 sold를 바르게 썼으므로")], 3)
f524("F", [("Tom kept the secret.", "keep의 과거형 kept를 바르게 썼으므로"), ("The baby holded my finger.", "hold의 과거형은 불규칙형 held이므로"), ("I heard a strange sound.", "hear의 과거형 heard를 바르게 썼으므로"),
           ("We tried a new dish.", "try의 과거형 tried를 바르게 썼으므로"), ("She paid for the tickets.", "pay의 과거형 paid를 바르게 썼으므로")], 2)

# 5-25 옳은 문장: B 원문항 발문, C~F는 원문항처럼 Did/didn't/Does + 과거형 오류로 유형마다 새로
F(5, 25, "B", st="R", s="발문이 ‘과거시제를 문법적으로 바르게 사용한 문장’으로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
R525 = "Did/didn't와 Does/doesn't 뒤에는 동사원형을 쓴다. 과거의 일을 긍정문으로 말할 때만 동사의 과거형을 쓴다."
S525 = "원문항은 Did/didn't/Does 뒤에 과거형을 쓴 오류를 판별하는데, 변형은 불규칙 과거형(goed, buyed, seed)과 was/were 오류 위주라 평가 초점이 달랐고, 짝 문장과 같은 오답이 반복되었다. 원문항처럼 Did/didn't/Does + 과거형 오류로 유형마다 새로 썼다."
def f525(t, items, a, s=S525):
    mk(5, 25, t, items, a, R525, s, st="R")
f525("C", [("Did you went to the library?", "Did 뒤에는 동사원형 go를 써야 하므로"), ("She didn't bought the ticket.", "didn't 뒤에는 동사원형 buy를 써야 하므로"), ("We ate pizza for lunch.", "과거의 일을 긍정문으로 말하며 과거형 ate를 썼으므로"),
           ("Does he watched TV every night?", "Does 뒤에는 동사원형 watch를 써야 하므로"), ("Did they came home late?", "Did 뒤에는 동사원형 come을 써야 하므로")], 3)
f525("D", [("I didn't knew the answer.", "didn't 뒤에는 동사원형 know를 써야 하므로"), ("Did you hear the news?", "Did 뒤에 동사원형 hear를 바르게 썼으므로"), ("Did she made the cake?", "Did 뒤에는 동사원형 make를 써야 하므로"),
           ("They didn't took the bus.", "didn't 뒤에는 동사원형 take를 써야 하므로"), ("Does Tom played the guitar?", "Does 뒤에는 동사원형 play를 써야 하므로")], 2)
f525("E", [("Did Jane lose her bag?", "Did 뒤에 동사원형 lose를 바르게 썼으므로"), ("He didn't said a word.", "didn't 뒤에는 동사원형 say를 써야 하므로"), ("Did you saw the rainbow?", "Did 뒤에는 동사원형 see를 써야 하므로"),
           ("We didn't went out yesterday.", "didn't 뒤에는 동사원형 go를 써야 하므로"), ("Does she cooked dinner?", "Does 뒤에는 동사원형 cook을 써야 하므로")], 1)
f525("F", [("Tom didn't drank the juice.", "didn't 뒤에는 동사원형 drink를 써야 하므로"), ("Did the kids slept well?", "Did 뒤에는 동사원형 sleep을 써야 하므로"), ("Does your mom worked here?", "Does 뒤에는 동사원형 work를 써야 하므로"),
           ("Did he gave you a present?", "Did 뒤에는 동사원형 give를 써야 하므로"), ("I didn't feel well yesterday.", "didn't 뒤에 동사원형 feel을 바르게 썼으므로")], 5)

# 5-26 우리말 뜻 제시: 원문항 발문, 실제 형태의 오답
S526 = "발문이 ‘동사 ○○의 올바른 과거형’이라고 시제를 알려 주었고 오답이 없는 형태(boughting, ateed 등)라 쉽게 지워졌다. 원문항처럼 우리말 뜻을 제시하고, 현재형·-ing형·과거분사 같은 실제 형태로 오답을 바꿨다."
R526 = "‘~했다’는 과거의 일이므로 동사의 과거형을 쓴다. 현재형은 지금의 습관·사실을, -ing형과 과거분사는 혼자서 동사 자리에 쓰지 못한다."
def st526(ko): return f"다음 빈칸에 '{ko}'라는 의미가 되도록 알맞은 단어를 고르세요."
def f526(t, ko, p, items, a, s=S526):
    mk(5, 26, t, items, a, R526, s, st=st526(ko), p=p)
f526("B", "Mina는 어제 사촌에게 긴 편지를 썼다", "Mina ________ a long letter to her cousin yesterday.",
     [("written", "과거분사만으로는 동사 자리에 쓸 수 없으므로"), ("write", "동사원형이고 3인칭 단수 주어와도 맞지 않으므로"), ("writing", "-ing형만으로는 동사 자리를 채울 수 없으므로"), ("writes", "현재형이라 ‘썼다’는 과거의 뜻이 되지 않으므로"), ("wrote", "write의 과거형으로 ‘썼다’는 뜻이 되므로")], 5,
     "발문이 ‘동사 write의 올바른 과거형’으로 바뀌어 시제를 알려 주었다. 원문항처럼 우리말 뜻을 제시하는 발문으로 바꿨다. 없는 형태(writed)는 실제 형태(writing)로 바꿨다.")
f526("C", "그녀는 어제 새 가방을 샀다", "She ________ a new bag yesterday.",
     [("buys", "현재형이라 ‘어제 샀다’는 뜻이 되지 않으므로"), ("buying", "-ing형만으로는 동사 자리에 쓸 수 없으므로"), ("buy", "동사원형이고 3인칭 단수 주어와도 맞지 않으므로"), ("bought", "buy의 과거형으로 ‘샀다’는 뜻이 되므로"), ("brought", "bring(가져오다)의 과거형이라 ‘샀다’는 뜻이 아니므로")], 4)
f526("D", "우리는 정오에 점심을 먹었다", "We ________ lunch at noon.",
     [("eat", "현재형이라 ‘먹었다’는 과거의 뜻이 되지 않으므로"), ("ate", "eat의 과거형으로 ‘먹었다’는 뜻이 되므로"), ("eaten", "과거분사만으로는 동사 자리에 쓸 수 없으므로"), ("eating", "-ing형만으로는 동사 자리에 쓸 수 없으므로"), ("eats", "3인칭 단수 현재형이라 주어 We와 맞지 않고 과거의 뜻도 아니므로")], 2)
f526("E", "Tom은 나무에서 새 한 마리를 보았다", "Tom ________ a bird in the tree.",
     [("saw", "see의 과거형으로 ‘보았다’는 뜻이 되므로"), ("sees", "현재형이라 ‘보았다’는 과거의 뜻이 되지 않으므로"), ("seen", "과거분사만으로는 동사 자리에 쓸 수 없으므로"), ("seeing", "-ing형만으로는 동사 자리에 쓸 수 없으므로"), ("see", "동사원형이고 3인칭 단수 주어와도 맞지 않으므로")], 1)
f526("F", "Jane은 어제 케이크를 만들었다", "Jane ________ a cake yesterday.",
     [("make", "동사원형이고 3인칭 단수 주어와도 맞지 않으므로"), ("makes", "현재형이라 ‘만들었다’는 과거의 뜻이 되지 않으므로"), ("made", "make의 과거형으로 ‘만들었다’는 뜻이 되므로"), ("making", "-ing형만으로는 동사 자리에 쓸 수 없으므로"), ("to make", "to부정사만으로는 동사 자리에 쓸 수 없으므로")], 3)

# 5-28 (A)(B) 짝: 원문항 발문, 과거 시간 표현을 문장 앞에
S528 = "발문에 ‘두 빈칸을 모두 과거형으로, 둘째 빈칸에는 ○○를 알맞게 바꾸어’가 붙어 시제와 동사를 알려 주었다. 원문항 발문으로 되돌리고, 두 빈칸 모두 과거로 정해지도록 문장 앞에 과거 시간 표현을 넣었다."
def f528(t, p, items, a, s=S528):
    mk(5, 28, t, items, a, R_PAST, s, st="R", p=p, okdup=True)
f528("B", "Last night, the children (A)________ excited, and they (B)________ loudly when the show began.",
     [("were — cheers", "(B): 지난밤의 일이고 주어가 they라 cheered를 써야 하므로"), ("are — cheered", "(A): 지난밤의 일이라 were를 써야 하므로"), ("were — cheered", "복수 주어의 be동사 과거형 were와 과거형 cheered를 바르게 짝지었으므로"),
      ("was — cheered", "(A): 복수 주어 the children에는 were를 써야 하므로"), ("were — cheer", "(B): 지난밤의 일이라 과거형 cheered를 써야 하므로")], 3)
f528("C", "Yesterday, the boys (A)________ hungry, so they (B)________ lunch early.",
     [("were — eat", "(B): 어제의 일이라 과거형 ate를 써야 하므로"), ("was — ate", "(A): 복수 주어 the boys에는 were를 써야 하므로"), ("are — ate", "(A): 어제의 일이라 were를 써야 하므로"),
      ("were — ate", "복수 주어의 be동사 과거형 were와 eat의 과거형 ate를 바르게 짝지었으므로"), ("were — eated", "(B): eat의 과거형은 불규칙형 ate이므로")], 4)
f528("D", "Last Friday, Jane (A)________ tired, so she (B)________ home early.",
     [("is — went", "(A): 지난 금요일의 일이라 was를 써야 하므로"), ("was — went", "단수 주어의 be동사 과거형 was와 go의 과거형 went를 바르게 짝지었으므로"), ("was — goed", "(B): go의 과거형은 불규칙형 went이므로"),
      ("were — went", "(A): 단수 주어 Jane에는 was를 써야 하므로"), ("was — go", "(B): 지난 금요일의 일이고 주어가 she라 went를 써야 하므로")], 2)
f528("E", "Last Christmas, we (A)________ happy because we (B)________ a big gift.",
     [("were — get", "(B): 지난 크리스마스의 일이라 과거형 got을 써야 하므로"), ("are — got", "(A): 지난 크리스마스의 일이라 were를 써야 하므로"), ("were — getted", "(B): get의 과거형은 불규칙형 got이므로"),
      ("was — got", "(A): 주어 we에는 were를 써야 하므로"), ("were — got", "주어 we의 be동사 과거형 were와 get의 과거형 got을 바르게 짝지었으므로")], 5)
f528("F", "Last weekend, Tom (A)________ busy because he (B)________ a new desk.",
     [("was — made", "단수 주어의 be동사 과거형 was와 make의 과거형 made를 바르게 짝지었으므로"), ("was — maked", "(B): make의 과거형은 불규칙형 made이므로"), ("is — made", "(A): 지난 주말의 일이라 was를 써야 하므로"),
      ("were — made", "(A): 단수 주어 Tom에는 was를 써야 하므로"), ("was — make", "(B): 지난 주말의 일이고 주어가 he라 made를 써야 하므로")], 1)

# 5-29 오류 고치는 과정: 원문항의 '그 이유는 (   )' 형식, 그럴듯한 오개념 오답을 유형마다 새로
R529 = "be동사 과거형은 주어가 I·3인칭 단수면 was, you·복수면 were를 쓴다. 의문사(Why, Where, How)나 형용사는 be동사의 형태를 정하지 않고, 일반동사가 없는 문장이므로 did로 바꾸지 않는다."
S529 = "원문항의 ‘그 이유는 (   )’ 빈칸 채우기 형식이 이유를 바로 고르는 발문으로 바뀌었고, 오답(‘주어의 수와 be동사는 관계가 없다’ 등)이 뻔하며 유형마다 반복되었다. 원문항 발문과 형식으로 되돌리고, 주어를 잘못 찾거나 시제를 놓치는 그럴듯한 오개념으로 유형마다 오답을 새로 썼다."
def f529(t, sent, wrong, items, a, s=S529):
    mk(5, 29, t, items, a, R529, s, st="R", p=f"{sent}\n위 문장에서 {wrong} 틀린 표현이다. 그 이유는 (                                    )")
f529("B", "Why <u>was</u> the students late for class yesterday?", "was는",
     [("이유를 묻는 Why가 문장 맨 앞에 와서 is로 고쳐야 한다.", "의문사는 be동사의 형태를 정하지 않고, yesterday의 일이라 과거형을 써야 하므로"), ("주어가 3인칭 단수인 class이기 때문에 is로 고쳐야 한다.", "주어는 class가 아니라 the students이고, yesterday가 있어 과거형을 써야 하므로"),
      ("late for class가 과거의 일이므로 일반동사 의문문처럼 did로 고쳐야 한다.", "일반동사가 없는 be동사 의문문이라 did를 쓰지 않으므로"), ("의문문에서는 be동사를 쓸 수 없으므로 do로 고쳐야 한다.", "late는 형용사라 be동사가 필요하고 의문문에도 be동사를 쓰므로"),
      ("주어 the students가 3인칭 복수이므로 were로 고쳐야 한다.", "복수 주어의 be동사 과거형은 were이므로")], 5,
     "원문항의 ‘그 이유는 (   )’ 빈칸 채우기 형식이 이유를 바로 묻는 발문으로 바뀌었다. 원문항 발문과 형식으로 되돌리고, 오답을 원문항처럼 그럴듯한 오개념으로 새로 썼다.")
f529("C", "Why <u>were</u> Tom late yesterday?", "were는",
     [("주어 Tom이 3인칭 단수이므로 was로 고쳐야 한다.", "3인칭 단수 주어의 be동사 과거형은 was이므로"), ("주어 Tom이 3인칭 단수이므로 현재형 is로 고쳐야 한다.", "yesterday의 일이라 현재형 is가 아니라 과거형 was를 써야 하므로"),
      ("yesterday가 있는 과거 의문문은 Did로 시작하므로 Did로 고쳐야 한다.", "일반동사가 없는 be동사 의문문이라 did를 쓰지 않으므로"), ("의문사 Why 뒤에는 조동사 do가 오므로 does로 고쳐야 한다.", "의문사 뒤에도 be동사 의문문은 be동사를 쓰고, 과거의 일이므로"),
      ("형용사 late 앞에는 be동사의 원형을 쓰므로 be로 고쳐야 한다.", "형용사 앞이라도 주어와 시제에 맞는 be동사를 써야 하므로")], 1)
f529("D", "Where <u>was</u> the boys yesterday?", "was는",
     [("Where 의문문에서는 be동사를 쓸 수 없으므로 did로 고쳐야 한다.", "Where 뒤에도 be동사를 쓸 수 있고, 일반동사가 없는 문장이라 did를 쓰지 않으므로"), ("the boys는 여러 명을 나타내는 복수 주어이므로 were로 고쳐야 한다.", "복수 주어의 be동사 과거형은 were이므로"),
      ("the boys가 3인칭 복수이므로 현재형 are로 고쳐야 한다.", "yesterday의 일이라 현재형 are가 아니라 과거형 were를 써야 하므로"), ("주어가 장소를 나타내는 Where이므로 is로 고쳐야 한다.", "Where는 주어가 아니고 주어는 the boys이므로"),
      ("주어 the boys가 복수이므로 동사원형 be로 고쳐야 한다.", "복수 주어라도 be동사는 원형이 아니라 주어와 시제에 맞춰 were를 써야 하므로")], 2)
f529("E", "How <u>were</u> Jane yesterday?", "were는",
     [("상태를 묻는 How 뒤에는 현재형을 쓰므로 is로 고쳐야 한다.", "의문사는 be동사의 형태를 정하지 않고, yesterday의 일이라 과거형을 써야 하므로"), ("How 의문문은 일반동사 의문문이므로 did로 고쳐야 한다.", "일반동사가 없는 be동사 의문문이라 did를 쓰지 않으므로"),
      ("Jane은 3인칭 단수 주어이므로 was로 고쳐야 한다.", "3인칭 단수 주어의 be동사 과거형은 was이므로"), ("주어가 yesterday이고 시간은 단수로 보므로 was로 고쳐야 한다.", "was로 고치는 것은 맞지만 주어는 yesterday가 아니라 Jane이므로"),
      ("Jane이 3인칭 단수이므로 현재형 is로 고쳐야 한다.", "yesterday의 일이라 현재형 is가 아니라 과거형 was를 써야 하므로")], 3)
f529("F", "Why <u>was</u> they tired yesterday?", "was는",
     [("tired가 -ed로 끝나 과거를 나타내므로 was를 did로 고쳐야 한다.", "tired는 상태를 나타내는 형용사이고, 일반동사가 없는 be동사 의문문이므로"), ("이유를 묻는 Why 뒤에는 are를 쓰므로 are로 고쳐야 한다.", "의문사는 be동사의 형태를 정하지 않고, yesterday의 일이라 과거형을 써야 하므로"),
      ("they가 한 무리를 가리키는 단수이므로 is로 고쳐야 한다.", "they는 복수 대명사이고, yesterday의 일이라 과거형을 써야 하므로"), ("they는 3인칭 복수 대명사이므로 were로 고쳐야 한다.", "복수 주어의 be동사 과거형은 were이므로"),
      ("they는 2인칭 복수이므로 are로 고쳐야 한다.", "they는 3인칭 복수이고, yesterday의 일이라 과거형 were를 써야 하므로")], 4)

# 5-30 틀린 문장 짝: 원문항처럼 (가)~(마) 다섯 문장, 틀린 두 개의 짝
R530 = "Did/didn't/Does 뒤에는 동사원형을 쓰고, be동사는 주어에 맞춰 was/were를 쓰며 일반동사와 함께 쓰지 않는다. 불규칙 동사는 정해진 과거형을 쓴다."
S530 = "원문항은 (가)~(마) 다섯 문장 중 틀린 두 문장의 짝을 고르는데, 변형은 네 문장에서 ‘빠짐없이 모두’ 고르는 형식이고 선택지 대부분이 한 개짜리여서 사실상 하나만 고르는 문항이 되었다. 원문항 발문과 형식(다섯 문장, 두 개 짝 선택지)으로 되돌렸다."
def f530(t, lines, judge, ok, c, s=S530):
    a = c.index(ok) + 1
    F(5, 30, t, st="R", p="\n".join(lines), c=c, a=a, r=R530, pre=["문장별 판정: " + j for j in judge], k=f"어법상 틀린 문장은 {ok}이다.", n=setnotes(c, ok, "틀린 문장"), okdup=True, s=s + ipos(a))
f530("B", ["(가) Did Mina bring her camera?", "(나) He did not ate lunch.", "(다) The boys was late.", "(라) Jane wrote a postcard.", "(마) We visited our grandma last Sunday."],
     ["(가) O. Did 뒤에 동사원형 bring을 썼다.", "(나) X. did not 뒤에는 동사원형 eat을 써야 한다.", "(다) X. 복수 주어 The boys에는 were를 써야 한다.", "(라) O. write의 과거형 wrote를 썼다.", "(마) O. visit의 과거형 visited를 썼다."], "(나), (다)",
     ["(가), (다)", "(다), (라)", "(가), (나)", "(나), (다)", "(나), (라)"], "원문항은 다섯 문장인데 변형은 네 문장이었다. 옳은 문장 (마)를 더해 다섯 문장으로 맞췄다. 선택지와 정답은 그대로다.")
f530("C", ["(가) Did she called you yesterday?", "(나) Tom doesn't like carrots.", "(다) We played tennis after school.", "(라) Jane were at the library last night.", "(마) Did they find the key?"],
     ["(가) X. Did 뒤에는 동사원형 call을 써야 한다.", "(나) O. doesn't 뒤에 동사원형 like를 썼다.", "(다) O. play의 과거형 played를 썼다.", "(라) X. 단수 주어 Jane에는 was를 써야 한다.", "(마) O. Did 뒤에 동사원형 find를 썼다."], "(가), (라)",
     ["(가), (라)", "(나), (다)", "(가), (마)", "(다), (라)", "(나), (마)"])
f530("D", ["(가) My mom baked cookies for us.", "(나) He didn't went to the party.", "(다) Do you walk to school?", "(라) The movie was very funny.", "(마) The boys was at the park yesterday."],
     ["(가) O. bake의 과거형 baked를 썼다.", "(나) X. didn't 뒤에는 동사원형 go를 써야 한다.", "(다) O. Do 뒤에 동사원형 walk를 썼다.", "(라) O. 단수 주어 The movie에 was를 썼다.", "(마) X. 복수 주어 The boys에는 were를 써야 한다."], "(나), (마)",
     ["(가), (나)", "(나), (다)", "(라), (마)", "(가), (라)", "(나), (마)"])
f530("E", ["(가) We stayed home last weekend.", "(나) Were you tired after the game?", "(다) I losed my umbrella yesterday.", "(라) She doesn't eat breakfast.", "(마) Did Tom fixed the bike?"],
     ["(가) O. stay의 과거형 stayed를 썼다.", "(나) O. 주어 you에 Were를 썼다.", "(다) X. lose의 과거형은 불규칙형 lost이다.", "(라) O. doesn't 뒤에 동사원형 eat을 썼다.", "(마) X. Did 뒤에는 동사원형 fix를 써야 한다."], "(다), (마)",
     ["(가), (다)", "(다), (마)", "(나), (라)", "(가), (마)", "(라), (마)"])
f530("F", ["(가) Mina and I was in the same class last year.", "(나) The baby cried all night.", "(다) They didn't cleaned the room.", "(라) Does your dad cook dinner?", "(마) I wasn't at school yesterday."],
     ["(가) X. 복수 주어 Mina and I에는 were를 써야 한다.", "(나) O. cry의 과거형 cried를 썼다.", "(다) X. didn't 뒤에는 동사원형 clean을 써야 한다.", "(라) O. Does 뒤에 동사원형 cook을 썼다.", "(마) O. 주어 I에 wasn't를 썼다."], "(가), (다)",
     ["(나), (라)", "(가), (나)", "(가), (다)", "(다), (마)", "(라), (마)"])


# ---- 2차 감수(2026-10) 추가 ----
# 5-21 C~F: 같은 문장의 현재형·과거형이 함께 있어(쌍둥이 문장) 정답이 둘로 좁혀짐 → 짝 문장을 없앰
R521 = "과거를 나타내는 문장은 동사의 과거형(-ed, 불규칙 과거형, was/were, didn't)을 쓴다. 현재형은 지금의 습관·사실을 나타낸다."
S521 = "정답 문장(현재형)과 같은 문장의 과거형이 다른 보기에 함께 있어 둘만 견주면 답이 나왔다. 짝이 되는 문장을 다른 문장으로 바꿨다."
def PA(v): return f"과거형({v})을 쓴 과거의 문장이므로"
def PR(v): return f"현재형({v})으로 지금의 습관을 나타내 과거가 아니므로"
def f521(t, items, a):
    mk(5, 21, t, items, a, R521, S521, st="R")
f521("C", [("Tom plays soccer every day.", PR("plays")), ("They studied yesterday.", PA("studied")), ("I went home an hour ago.", PA("went")), ("Jane was busy last night.", PA("was")), ("We watched a movie last weekend.", PA("watched"))], 1)
f521("D", [("We went to the park.", PA("went")), ("They studied last night.", PA("studied")), ("Tom was tired.", PA("was")), ("I lost my umbrella yesterday.", PA("lost")), ("Jane reads books now.", PR("reads"))], 5)
f521("E", [("We played soccer.", PA("played")), ("Mom made a cake yesterday.", PA("made")), ("They go to school every day.", PR("go")), ("He was home.", PA("was")), ("Jane studied last night.", PA("studied"))], 3)
f521("F", [("Jane played soccer.", PA("played")), ("My dad watches TV every night.", PR("watches")), ("Tom went to school.", PA("went")), ("We were at home.", PA("were")), ("I visited my uncle last night.", PA("visited"))], 2)

# 5-27 C~F: 부정문이 아닌 보기(Tom buy ~ 등)는 발문만 보고 지워짐 → 원문항처럼 not을 쓴 오답으로
S527 = "오답 하나는 부정문이 아니어서(동사만 원형으로 바꾼 문장) ‘부정문으로 고친 것’이라는 발문만 보고 지워졌다. 그 오답을 원문항처럼 not을 잘못 쓴 문장으로 바꿨다."
def f527(t, sub, past, base, rest, order):
    its = {"ok": (f"{sub} didn't {base} {rest}.", "didn't + 동사원형으로 바르게 고쳤으므로"), "didpast": (f"{sub} didn't {past} {rest}.", "didn't 뒤에는 과거형이 아니라 동사원형을 쓰므로"),
           "notpast": (f"{sub} not {past} {rest}.", "not만으로는 일반동사를 부정할 수 없고 did가 필요하므로"), "does": (f"{sub} doesn't {base} {rest}.", "과거의 일에 현재형 doesn't를 쓸 수 없으므로"),
           "were": (f"{sub} weren't {base} {rest}.", "일반동사의 부정에 be동사를 쓸 수 없으므로")}
    mk(5, 27, t, [its[k] for k in order], order.index("ok") + 1, "일반동사 과거 부정문은 주어 + didn't(did not) + 동사원형이다.", S527, st="R")
f527("C", "Tom", "bought", "buy", "a bag yesterday", ["notpast", "didpast", "does", "ok", "were"])
f527("D", "They", "saw", "see", "a movie last night", ["does", "notpast", "didpast", "were", "ok"])
f527("E", "Jane", "ate", "eat", "lunch at noon", ["were", "didpast", "ok", "does", "notpast"])
f527("F", "We", "made", "make", "a cake yesterday", ["ok", "does", "didpast", "were", "notpast"])
