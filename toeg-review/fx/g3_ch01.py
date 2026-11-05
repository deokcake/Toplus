# 3급 CH1 be동사 (1~10) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def slots(c, a, why, labs, sp):
    good = sp(c[a-1]); out = []
    for i, ch in enumerate(c):
        parts = sp(ch)
        if i + 1 == a: out.append(f"{c[a-1]}: 모든 자리가 알맞으므로 정답이다."); continue
        out.append(" ".join(f"{labs[j]} {x}: {why[j][x]}" for j, x in enumerate(parts) if x != good[j]) + " 따라서 오답이다.")
    return out
DASH = lambda x: [p.strip() for p in re.split(r"\s+-\s+", x)]
AB = lambda x: re.findall(r"\([AB]\) (\S+)", x)

# 3-2 E: 발문을 원문항대로
F(3, 2, "E", st="R", xr=[("현재형을 쓰라는 조건에 맞지 않는다", "Right now(지금)와 시제가 맞지 않는다")], s="발문이 ‘be동사의 현재형을 고르시오’로 원문항과 달라 원문항 발문으로 되돌렸다. Right now가 있어 조건 없이도 정답은 하나다. 보기와 정답은 그대로다.")

# 3-4 소유격/소유대명사: 오답도 정답과 같은 이름으로
ST34 = "다음 대화의 빈칸에 들어갈 단어를 바르게 짝지은 것을 고르시오."
R34 = "명사 앞에서는 소유격(your)을 쓰고, 뒤에 명사 없이 ‘~의 것’을 나타낼 때는 소유대명사(yours)나 명사의 소유격(Mina's)을 쓴다."
S34 = "오답 네 개는 원문항의 이름(Gary)을 그대로 쓰고 정답만 다른 이름이라 이름만 보고 정답을 고를 수 있었다. 오답도 정답과 같은 이름으로 바꾸고 정답 위치를 옮겼다."
def f34(t, nn, noun, c, a):
    why = [{"yours": f"명사({noun}) 앞에는 소유대명사가 아니라 소유격 your를 쓴다.", "you": f"you는 명사({noun}) 앞에서 소유를 나타내지 못한다."},
           {nn: f"뒤에 명사 없이 ‘{nn}의 것’을 나타내려면 소유격 {nn}'s를 쓴다."}]
    F(3, 34 // 10 * 0 + 4, t, st=ST34, c=c, a=a, r=R34, n=slots(c, a, why, ["첫째 빈칸", "둘째 빈칸"], DASH),
      k=f"명사({noun}) 앞이므로 소유격 your, 뒤에 명사 없이 ‘{nn}의 것’이므로 {nn}'s이다.", s=S34 + ipos(a))
f34("C", "Mina", "bag", ["yours - Mina", "your - Mina's", "you - Mina's", "your - Mina", "yours - Mina's"], 2)
f34("D", "Leo", "shoes", ["your - Leo", "yours - Leo's", "you - Leo", "your - Leo's", "yours - Leo"], 4)
f34("E", "Tom", "bike", ["you - Tom's", "yours - Tom", "your - Tom", "yours - Tom's", "your - Tom's"], 5)
f34("F", "Jane", "pencils", ["your - Jane", "you - Jane's", "your - Jane's", "yours - Jane's", "yours - Jane"], 3)

# 3-5 옳은 문장 개수: 원문항 형식(ⓐ~ⓔ, 줄바꿈, 밑줄, 1개~5개)
ST5 = "다음 중 밑줄 친 부분이 어법상 옳은 문장의 개수를 고르시오."
R5 = "be동사는 주어의 인칭·수와 시제에 맞춘다(I am, 단수 is/was, 복수·you are/were). 부정문은 be동사 뒤에 not을, 의문문은 be동사를 주어 앞에 둔다. There + be동사는 뒤의 명사에 수를 맞추고, news처럼 -s로 끝나도 단수인 명사에 주의한다."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]
def f5(t, lines, judge, ok, s):
    n = len(ok.split(","))
    F(3, 5, t, st=ST5, p="\n".join(lines), c=CNT5, a=n, r=R5, pre=["문장별 판정: " + j for j in judge], k=f"밑줄 친 부분이 옳은 문장은 {ok}로 {n}개이다.", n="cnt", s=s + ipos(n))
S5 = "원문항의 밑줄이 없고, 보기 기호 ⓐ~ⓔ가 a~e로 바뀌어 한 줄로 이어졌으며 개수 선택지 순서가 뒤섞였다. 원문항 발문과 형식(ⓐ~ⓔ, 줄바꿈, 밑줄, 1개~5개)으로 되돌렸다."
f5("B", ["ⓐ My brother <u>is</u> in the kitchen.", "ⓑ We <u>was</u> at the library yesterday.", "ⓒ <u>Are</u> your parents at home?", "ⓓ There <u>is</u> two apples on the plate.", "ⓔ The movies <u>wasn't</u> very long."],
   ["ⓐ O. 3인칭 단수 주어에 is를 썼다.", "ⓑ X. 복수 주어(We)의 과거는 were이다.", "ⓒ O. 복수 주어(your parents)의 의문문에 Are를 썼다.", "ⓓ X. 뒤의 명사(two apples)가 복수이므로 There are이다.", "ⓔ X. 복수 주어(The movies)의 과거 부정은 weren't이다."],
   "ⓐ, ⓒ", "다섯 문장이 원문항 문장을 줄인 것이었고 정답 개수(3개)도 같았으며, 기호·줄바꿈·밑줄·선택지 순서도 원본과 달랐다. 문장을 새로 쓰고 원문항 형식으로 되돌렸으며 정답 개수를 2개로 바꿨다.")
f5("C", ["ⓐ Tom <u>is</u> busy.", "ⓑ They <u>isn't</u> ready.", "ⓒ <u>Are</u> we late?", "ⓓ There <u>is</u> two books.", "ⓔ Jane <u>were</u> at home."],
   ["ⓐ O. 3인칭 단수 주어에 is를 썼다.", "ⓑ X. 복수 주어(They)의 부정은 aren't이다.", "ⓒ O. 주어 we의 의문문에 Are를 썼다.", "ⓓ X. 뒤의 명사(two books)가 복수이므로 There are이다.", "ⓔ X. 단수 주어(Jane)의 과거는 was이다."], "ⓐ, ⓒ", S5 + " 정답 개수·위치(3개, ③)가 원문항과 같지 않게 한 문장을 바꿨다.")
f5("D", ["ⓐ I <u>was</u> tired.", "ⓑ The boys <u>were</u> happy.", "ⓒ There <u>was</u> a dog outside.", "ⓓ She <u>isn't</u> busy.", "ⓔ <u>Was</u> they late?"],
   ["ⓐ O. 주어 I의 과거는 was이다.", "ⓑ O. 복수 주어의 과거는 were이다.", "ⓒ O. 뒤의 명사(a dog)가 단수이므로 There was이다.", "ⓓ O. 3인칭 단수 주어의 부정에 isn't를 썼다.", "ⓔ X. 복수 주어(they)의 과거 의문문은 Were이다."], "ⓐ, ⓑ, ⓒ, ⓓ", S5 + " 정답 개수·위치(3개, ③)가 원문항과 같지 않게 한 문장을 바꿨다.")
f5("E", ["ⓐ We <u>are</u> students.", "ⓑ Tom <u>wasn't</u> at home.", "ⓒ There <u>is</u> some water.", "ⓓ The news <u>are</u> good.", "ⓔ <u>Am</u> I late?"],
   ["ⓐ O. 복수 주어에 are를 썼다.", "ⓑ O. 단수 주어의 과거 부정에 wasn't를 썼다.", "ⓒ O. 셀 수 없는 명사(water)는 단수 취급하므로 There is이다.", "ⓓ X. news는 -s로 끝나도 단수 취급하므로 is를 쓴다.", "ⓔ O. 주어 I의 의문문에 Am을 썼다."], "ⓐ, ⓑ, ⓒ, ⓔ", S5)
f5("F", ["ⓐ Jane <u>is</u> kind.", "ⓑ They <u>wasn't</u> busy.", "ⓒ There <u>was</u> two cats.", "ⓓ We <u>isn't</u> late.", "ⓔ <u>Is</u> you ready?"],
   ["ⓐ O. 3인칭 단수 주어에 is를 썼다.", "ⓑ X. 복수 주어(They)의 과거 부정은 weren't이다.", "ⓒ X. 뒤의 명사(two cats)가 복수이므로 There were이다.", "ⓓ X. 복수 주어(We)의 부정은 aren't이다.", "ⓔ X. 주어 you의 의문문은 Are이다."], "ⓐ", S5 + " 정답 개수·위치(3개, ③)가 원문항과 같지 않게 두 문장을 바꿨다.")

# 3-7 be동사 의문문: B는 제시문을 새로, D·E는 발문을 원문항대로 하고 구어로 성립하는 보기 교체
ST7 = "다음 문장을 의문문으로 바꾼 것을 고르시오."
R7 = "be동사 문장의 의문문은 be동사를 주어 앞으로 보내고 나머지는 그대로 둔다. 주어의 인칭·수와 시제에 맞는 be동사를 쓰고, do/did를 쓰거나 be동사를 두 번 쓰지 않는다."
OK7 = "be동사를 주어 앞으로 보내고 시제·수를 그대로 둔 바른 의문문이므로"
mk(3, 7, "B", [("Was the kids hungry after class?", "복수 주어(the kids)의 과거는 Were이므로"), ("Did the kids were hungry after class?", "be동사 문장에는 did를 쓰지 않으므로"),
               ("Were the kids hungry after class?", OK7), ("Are the kids hungry after class?", "과거(were)를 현재로 바꿔 시제가 맞지 않으므로"), ("Were the kids were hungry after class?", "be동사를 두 번 썼으므로")], 3, R7,
   "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘The kids were hungry after class.’로 바꿨다.", p="The kids were hungry after class.")
S7 = "발문이 ‘be동사를 주어 앞으로 옮겨 만드는 기본 yes/no 의문문’이라고 만드는 방법을 알려 주어 원문항 발문으로 되돌렸다. 조건이 없으면 평서문 어순 + 물음표 보기도 구어에서 쓰여 답이 흔들리므로 다른 오답으로 바꿨다."
mk(3, 7, "D", [("Are we is ready now?", "be동사를 두 번 썼으므로"), ("Do we are ready now?", "be동사 문장에는 do를 쓰지 않으므로"), ("Is we ready now?", "주어 we에는 Are를 써야 하므로"),
               ("Are we be ready now?", "be동사 뒤에 원형 be를 한 번 더 썼으므로"), ("Are we ready now?", OK7)], 5, R7, S7, st=ST7)
mk(3, 7, "E", [("Does Tom a student?", "be동사 문장에는 does를 쓰지 않으므로"), ("Is Tom a student?", OK7), ("Are Tom a student?", "3인칭 단수 주어(Tom)에는 Is를 써야 하므로"),
               ("Is Tom student?", "셀 수 있는 명사(student) 앞의 관사 a가 빠졌으므로"), ("Is Tom is a student?", "be동사를 두 번 썼으므로")], 2, R7, S7 + " 정답 위치를 D와 다르게 옮겼다.", st=ST7)

# 3-8 was/were 짝: 원문항 발문·밑줄, 조건 없이도 답이 하나가 되게 보기 조정
ST8 = "다음 문장의 빈칸 (A), (B)에 들어갈 말이 바르게 짝지어진 것은?"
UA, UB = "(<u>    A    </u>)", "(<u>    B    </u>)"
R8 = "be동사의 과거형은 단수 주어(I, he, she, it, 단수명사)에 was, 복수 주어와 you에 were를 쓴다."
def f8(t, p, c, a, subjA, subjB, s):
    why = [{"was": f"주어({subjA})에 맞지 않는 형태이다.", "were": f"주어({subjA})에 맞지 않는 형태이다.", "is": f"주어({subjA})와 수가 맞더라도 was/were와 짝이 맞지 않는 현재형이다.",
            "am": f"주어({subjA})와 짝이 맞지 않는 현재형이다.", "are": f"주어({subjA})와 짝이 맞지 않는 현재형이다."},
           {"was": f"주어({subjB})에 맞지 않는 형태이다.", "were": f"주어({subjB})에 맞지 않는 형태이다."}]
    good = AB(c[a-1])
    for j, sub in enumerate([subjA, subjB]):
        for k in list(why[j]):
            if k == good[j]: continue
    F(3, 8, t, st=ST8, p=p.replace("(A)", UA).replace("(B)", UB), c=c, a=a, r=R8, n=slots(c, a, why, ["(A)", "(B)"], AB),
      k=f"(A)의 주어({subjA})에는 {good[0]}, (B)의 주어({subjB})에는 {good[1]}를 쓴다.", s=s + ipos(a))
S8 = "발문에 ‘두 빈칸에 모두 be동사의 과거형을 써서’ 조건이 붙었고 빈칸 밑줄이 없었다. 조건을 지우고 원문항 발문과 밑줄로 되돌렸다. 현재형이 섞인 보기는 시제가 섞여도 수 일치만 맞으면 성립할 수 있어, 수 일치가 틀린 보기로 바꿨다."
f8("B", "My sister (A) at the library yesterday, but my parents (B) at the museum.", ["(A) were - (B) was", "(A) was - (B) was", "(A) was - (B) were", "(A) were - (B) were", "(A) is - (B) was"], 3, "My sister", "my parents",
   "제시문과 정답이 원문항과 똑같았고 발문 조건도 붙었다. 제시문을 새로 쓰고(yesterday로 과거를 드러냄) 원문항 발문과 밑줄로 되돌렸다.")
f8("C", "Tom (A) at home, but his friends (B) at school.", ["(A) is - (B) was", "(A) were - (B) was", "(A) was - (B) was", "(A) was - (B) were", "(A) were - (B) were"], 4, "Tom", "his friends", S8)
f8("D", "I (A) tired, but we (B) happy.", ["(A) was - (B) was", "(A) was - (B) were", "(A) were - (B) were", "(A) were - (B) was", "(A) am - (B) was"], 2, "I", "we", S8)
f8("E", "The dog (A) hungry, but the cats (B) fine.", ["(A) was - (B) was", "(A) is - (B) was", "(A) were - (B) was", "(A) were - (B) were", "(A) was - (B) were"], 5, "The dog", "the cats", S8 + " 정답 위치를 옮겼다.")
f8("F", "Jane and Amy (A) busy, but Tom (B) free.", ["(A) were - (B) was", "(A) are - (B) were", "(A) were - (B) were", "(A) was - (B) were", "(A) was - (B) was"], 1, "Jane and Amy", "Tom", S8 + " 정답 위치를 옮겼다.")

# 3-9 there 구문 설명: 원문항 발문·형식, 옳은 설명과 그럴듯한 틀린 설명을 섞음
ST9 = "다음 중 <보기> 문장에 대한 설명 중 옳은 것을 모두 고르시오."
R9 = "There + be동사 구문에서 there는 형식상 앞에 오는 유도부사이고 실제 주어는 be동사 뒤의 명사이다. be동사의 수·시제는 실제 주어와 때에 맞추며, 의문문은 be동사를 there 앞에 두고 Yes, there is./No, there isn't.처럼 답한다."
S9 = "원문항은 옳은 설명과 틀린 설명이 섞여 있는데, 변형은 네 설명이 모두 옳거나 모두 ‘라’만 틀린 같은 구조라 정답이 예측되었고 발문도 달랐다. 원문항 발문과 <보기> 형식으로 되돌리고, 옳은 설명과 그럴듯한 틀린 설명을 섞어 유형마다 새로 썼다."
def f9(t, sent, items, judge, ok, c, a, s=""):
    F(3, 9, t, st=ST9, p="<보기>\n" + sent + "\n" + "\n".join(items), c=c, a=a, r=R9, pre=["항목별 판정: " + j for j in judge], k=f"옳은 설명은 {ok}이다.", n=setnotes(c, ok, "옳은 설명"), s=S9 + s + ipos(a))
f9("B", "Is there a bank near here?", ["가. 이 문장의 실제 주어는 a bank이다.", "나. there가 주어이므로 동사는 항상 is를 쓴다.", "다. 평서문 There is a bank near here.의 is를 there 앞으로 옮겨 만든 의문문이다.", "라. near here는 문장의 주어 역할을 한다."],
   ["가 O. be동사 뒤의 a bank가 실제 주어이다.", "나 X. there는 주어가 아니며 be동사는 실제 주어의 수에 맞춘다.", "다 O. be동사를 there 앞으로 옮겨 의문문을 만든다.", "라 X. near here는 장소를 나타내는 부사구이다."],
   "가, 다", ["가, 다", "나, 다", "가, 라", "가, 나, 다", "다, 라"], 1, " 원문항과 같은 문장(Is there a cat in the room?)을 다른 문장으로 바꿨다.")
f9("C", "Are there two books on the desk?", ["가. 실제 주어 two books가 복수라 Are를 썼다.", "나. there가 문장의 주어이므로 there에 수를 맞춘다.", "다. 이 질문에는 Yes, it is.로 답한다.", "라. 평서문으로 바꾸면 There are two books on the desk.가 된다."],
   ["가 O. 실제 주어가 복수라 Are이다.", "나 X. there는 주어가 아니다.", "다 X. Yes, there are.로 답한다.", "라 O. be동사를 there 뒤로 돌리면 평서문이 된다."],
   "가, 라", ["가, 나", "나, 다", "가, 라", "가, 다, 라", "나, 라"], 3)
f9("D", "Was there a meeting yesterday?", ["가. there가 실제 주어이다.", "나. yesterday가 있어도 현재형 Is를 써야 한다.", "다. 실제 주어 a meeting이 단수이고 과거라 Was를 썼다.", "라. 이 질문에 부정으로 답하면 No, there wasn't.이다."],
   ["가 X. 실제 주어는 a meeting이다.", "나 X. 과거 시점(yesterday)이므로 과거형 Was를 쓴다.", "다 O. 단수·과거라 Was이다.", "라 O. there를 살려 No, there wasn't.로 답한다."],
   "다, 라", ["가, 다", "다, 라", "나, 라", "가, 나, 다", "나, 다, 라"], 2)
f9("E", "Were there many people outside?", ["가. 실제 주어 many people이 복수이므로 Were를 썼다.", "나. 현재의 일이라면 Are there many people outside?가 된다.", "다. people은 -s가 없으므로 단수 취급해 Was를 써야 한다.", "라. 이 질문에 긍정으로 답하면 Yes, there were.이다."],
   ["가 O. 실제 주어가 복수라 Were이다.", "나 O. 현재라면 Are를 쓴다.", "다 X. people은 -s가 없어도 복수 명사이다.", "라 O. Yes, there were.로 답한다."],
   "가, 나, 라", ["가, 나", "나, 다", "가, 다, 라", "나, 다, 라", "가, 나, 라"], 5)
f9("F", "Is there any water in the bottle?", ["가. water는 셀 수 없는 명사라 단수 취급해 Is를 썼다.", "나. any는 의문문에서 ‘조금이라도’의 뜻으로 쓰였다.", "다. there가 주어이므로 Is를 썼다.", "라. 이 질문에 긍정으로 답하면 Yes, it is.이다."],
   ["가 O. 셀 수 없는 명사는 단수 취급한다.", "나 O. 의문문의 any는 ‘조금이라도’의 뜻이다.", "다 X. there는 주어가 아니다.", "라 X. Yes, there is.로 답한다."],
   "가, 나", ["가, 다", "나, 라", "가, 나, 라", "가, 나", "다, 라"], 4)

# 3-10 틀린 문장 개수: 원문항처럼 1개~4개·없음 순, 정답 개수를 유형마다 다르게
ST10 = "다음 <보기> 중 어법상 틀린 문장의 개수는?"
R10 = "there 구문은 뒤의 실제 명사의 수와 문장의 시제에 맞춰 there is/are/was/were를 고른다. 주어가 있는 문장은 주어의 수·시제에 맞춰 was/were를 쓴다(a lot of + 셀 수 없는 명사는 단수, 복수명사는 복수)."
CNT10 = ["1개", "2개", "3개", "4개", "없음"]
def f10(t, lines, judge, wrong, s):
    n = len(wrong.split(",")) if wrong else 0
    a = n if n else 5
    F(3, 10, t, st=ST10, p="<보기>\n" + "\n".join("- " + x for x in lines), c=CNT10, a=a, r=R10, pre=["문장별 판정: " + j for j in judge],
      k=(f"어법상 틀린 문장은 {wrong}로 {n}개이다." if n else "네 문장 모두 옳아 틀린 문장이 없다."), n="cnt", s=s + ipos(a))
S10 = "개수 선택지 순서가 뒤섞여 원문항처럼 1개~4개, 없음 순으로 맞췄다."
f10("B", ["This morning, there was a lot of people at the bus stop.", "The bus were late.", "My friends and I were cold.", "But the driver was very kind."],
    ["첫째 X. 뒤의 명사(a lot of people)가 복수이므로 there were이다.", "둘째 X. 단수 주어(The bus)의 과거는 was이다.", "셋째 O. 복수 주어(My friends and I)의 과거는 were이다.", "넷째 O. 단수 주어(the driver)의 과거는 was이다."],
    "첫째, 둘째", "제시문과 정답이 원문항과 똑같았다. 문장을 새로 쓰고 정답 개수를 2개로 바꿨으며, " + S10)
f10("C", ["Yesterday, there was two accidents.", "The road was busy.", "The drivers were careful.", "There were many police officers."],
    ["첫째 X. 뒤의 명사(two accidents)가 복수이므로 there were이다.", "둘째 O. 단수 주어의 과거는 was이다.", "셋째 O. 복수 주어의 과거는 were이다.", "넷째 O. 뒤의 명사가 복수이므로 there were이다."], "첫째", S10)
f10("D", ["Last week, there were many visitors.", "The museum were crowded.", "There was two guides.", "We were tired."],
    ["첫째 O. 뒤의 명사(many visitors)가 복수이므로 there were이다.", "둘째 X. 단수 주어(The museum)의 과거는 was이다.", "셋째 X. 뒤의 명사(two guides)가 복수이므로 there were이다.", "넷째 O. 복수 주어(We)의 과거는 were이다."],
    "둘째, 셋째", S10 + " 둘째를 틀린 문장으로 바꿔 틀린 문장을 2개로 했다(원문항의 정답 3개와 겹치지 않게).")
f10("E", ["There were a lot of snow.", "The roads was slippery.", "My brother were late.", "I were worried."],
    ["첫째 X. a lot of + 셀 수 없는 명사(snow)는 단수이므로 there was이다.", "둘째 X. 복수 주어(The roads)의 과거는 were이다.", "셋째 X. 단수 주어(My brother)의 과거는 was이다.", "넷째 X. 주어 I의 과거는 was이다."],
    "첫째, 둘째, 셋째, 넷째", S10 + " 다른 유형과 정답 개수가 겹치지 않게 네 문장을 모두 틀린 문장으로 바꿨다.")
f10("F", ["There were many clouds.", "The sky was dark.", "There was a strong wind.", "The children were inside."],
    ["첫째 O. 뒤의 명사가 복수이므로 there were이다.", "둘째 O. 단수 주어의 과거는 was이다.", "셋째 O. 뒤의 명사가 단수이므로 there was이다.", "넷째 O. children은 복수이므로 were이다."],
    "", S10 + " 다른 유형과 정답 개수가 겹치지 않게 넷째를 옳은 문장으로 바꿔 틀린 문장이 없게(없음) 했다.")

# ---- 2차 감수(2026-10) 추가 ----
# 3-1 B·C·D: 발문 ‘현재형 be동사’ → 원문항 발문, 과거형이 섞인 보기는 현재형 조합으로
R1 = "be동사의 현재형은 주어에 따라 달라진다. I는 am, you와 복수 주어는 are, 3인칭 단수 주어는 is를 쓴다."
S1 = "발문이 ‘현재형 be동사’로 원문항(‘알맞은 be동사’)과 달랐다. 원문항 발문으로 되돌리고, 조건이 없어도 답이 하나가 되도록 과거형이 섞인 보기({})를 현재형 조합({})으로 바꿨다."
def f1(t, c, a, s1, s2, old, new):
    ans = c[a - 1].split(" - ")
    def note(x):
        l, r = x.split(" - ")
        if [l, r] == ans: return f"주어 {s1}에는 {ans[0]}, 주어 {s2}에는 {ans[1]}를 쓰므로"
        if l != ans[0] and r != ans[1]: return "두 빈칸 모두 주어와 맞지 않으므로"
        if l != ans[0]: return f"주어 {s1}에 {l}를 쓸 수 없으므로"
        return f"주어 {s2}에 {r}를 쓸 수 없으므로"
    mk(3, 1, t, [(x, note(x)) for x in c], a, R1, S1.format(old, new), st="R", p=V(3, 1, t)["passage"])
f1("B", ["are - are", "are - is", "is - are", "am - is", "is - is"], 2, "You", "Mina", "were - is", "is - is")
f1("C", ["are - are", "is - is", "is - are", "am - is", "are - is"], 3, "She", "The boys", "was - are", "is - is")
f1("D", ["are - are", "am - is", "is - are", "are - is", "is - is"], 4, "We", "Tom", "was - are", "are - are")
