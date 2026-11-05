# 2급 CH10 관계사 (91~100) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."

# 2-92 우리말 → what/the thing that: 조건 삭제, All/Everything 문장 대신 다른 문장, 정답 조합을 원문항과 다르게
ST92 = "다음 우리말을 영어로 바르게 옮긴 문장을 모두 고르시오."
R92 = "what은 선행사를 포함한 관계대명사로 ‘~하는 것’이라는 뜻이며 관계절 안에서 목적어 역할을 하므로 뒤에 목적어를 다시 쓰지 않는다. 선행사(the thing)가 있으면 that·which를 쓰거나 목적격 관계대명사를 생략하며, 선행사 뒤에 what을 쓰지 않는다."
S92 = "발문에 ‘all 또는 everything으로 강조한 표현도 허용’ 조건이 붙어 있었고, 조건이 없으면 All/Everything that 문장이 답을 흔들었다. 원문항 발문으로 되돌리고 All/Everything 문장 대신 ‘The thing (that/which) …’, ‘What … it’ 같은 문장으로 바꿔, 정답 조합이 원문항(a, c, e)과 다르게 했다."
def f92(t, ko, lines, judge, ok, c, a):
    F(2, 92, t, st=ST92, p=f"\"{ko}\"\n" + "\n".join(lines), c=c, a=a, r=R92, pre=["문장별 판정: " + j for j in judge], k=f"바르게 옮긴 문장은 {ok}이다.",
      n=setnotes(c, ok, "바르게 옮긴 문장"), s=S92 + ipos(a))
f92("B", "네가 말한 것이 사실이다.", ["a. What you said is true.", "b. The thing what you said is true.", "c. The thing you said is true.", "d. That you said is true.", "e. You said is true."],
    ["a O. what이 ‘~한 것’을 나타내며 said의 목적어 역할을 한다.", "b X. 선행사(the thing) 뒤에는 what을 쓰지 않는다.", "c O. 선행사 뒤 목적격 관계대명사가 생략되었다.",
     "d X. 접속사 that 뒤에는 완전한 절이 와야 하는데 said의 목적어가 없다.", "e X. 주어 자리에 절을 이끄는 말(what)이 없어 동사가 두 개 겹친다."], "a, c", ["a, c", "a, b", "a, c, e", "b, d", "a, b, c"], 1)
f92("C", "우리가 원하는 것은 평화이다.", ["a. What we want is peace.", "b. The thing that we want is peace.", "c. The thing what we want is peace.", "d. What we want it is peace.", "e. The thing which we want is peace."],
    ["a O. what이 ‘~한 것’을 나타낸다.", "b O. 선행사(the thing) + 목적격 관계대명사 that이다.", "c X. 선행사(the thing) 뒤에는 what을 쓰지 않는다.",
     "d X. what이 이미 want의 목적어이므로 it을 다시 쓰지 않는다.", "e O. 선행사(the thing) + 목적격 관계대명사 which이다."], "a, b, e", ["a, b", "a, c, e", "b, d", "a, b, e", "a, b, c, e"], 4)
f92("D", "그녀가 산 것은 비쌌다.", ["a. She bought was expensive.", "b. What she bought was expensive.", "c. The thing what she bought was expensive.", "d. The thing that she bought was expensive.", "e. The thing she bought was expensive."],
    ["a X. 주어 자리에 절을 이끄는 말(what)이 없어 동사가 두 개 겹친다.", "b O. what이 ‘~한 것’을 나타낸다.", "c X. 선행사(the thing) 뒤에는 what을 쓰지 않는다.",
     "d O. 선행사(the thing) + 목적격 관계대명사 that이다.", "e O. 선행사 뒤 목적격 관계대명사가 생략되었다."], "b, d, e", ["b, d", "b, d, e", "a, b, d", "c, d, e", "b, c"], 2)
f92("E", "내가 필요한 것은 시간이다.", ["a. What I need is time.", "b. The thing that I need is time.", "c. The thing I need is time.", "d. What I need it is time.", "e. The thing what I need is time."],
    ["a O. what이 ‘~한 것’을 나타낸다.", "b O. 선행사(the thing) + 목적격 관계대명사 that이다.", "c O. 선행사 뒤 목적격 관계대명사가 생략되었다.",
     "d X. what이 이미 need의 목적어이므로 it을 다시 쓰지 않는다.", "e X. 선행사(the thing) 뒤에는 what을 쓰지 않는다."], "a, b, c", ["a, b", "b, c, d", "a, b, c", "a, c, e", "a, b, c, e"], 3)
f92("F", "그가 말한 것은 놀라웠다.", ["a. The thing what he said was surprising.", "b. What he said was surprising.", "c. That he said was surprising.", "d. What he said it was surprising.", "e. The thing which he said was surprising."],
    ["a X. 선행사(the thing) 뒤에는 what을 쓰지 않는다.", "b O. what이 ‘~한 것’을 나타낸다.", "c X. 접속사 that 뒤에는 완전한 절이 와야 하는데 said의 목적어가 없다.",
     "d X. what이 이미 said의 목적어이므로 it을 다시 쓰지 않는다.", "e O. 선행사(the thing) + 목적격 관계대명사 which이다."], "b, e", ["a, b", "b, c, e", "d, e", "a, b, e", "b, e"], 5)

# 2-93 전치사 + which 세 개: 원문항 형식
ST93 = "다음 빈칸에 들어갈 말이 바르게 짝지어진 것을 고르시오."
R93 = "전치사 + which의 전치사는 관계절을 원래 문장으로 풀었을 때 선행사 앞에 오는 전치사이다(I was born in the house → the house in which I was born)."
S93 = "원문항은 ‘전치사 + which’의 전치사 세 개를 짝으로 고르는 문항인데, 변형은 빈칸 하나에 관계사를 고르는 문항으로 형식과 평가 요소가 바뀌었다. 원문항 발문과 형식(전치사 + which 빈칸 세 개)으로 다시 썼다."
def f93(t, lines, orig, c, a):
    good = [p.strip() for p in c[a-1].split(" - ")]
    nn = []
    for i, ch in enumerate(c):
        parts = [p.strip() for p in ch.split(" - ")]
        if i + 1 == a: nn.append(f"{c[a-1]}: 세 빈칸이 모두 알맞으므로 정답이다."); continue
        nn.append(" ".join(f"{'ABC'[j]} 빈칸 {x}: 관계절을 풀면 ‘{orig[j]}’이므로 {good[j]}가 알맞다." for j, x in enumerate(parts) if x != good[j]) + " 따라서 오답이다.")
    F(2, 93, t, st=ST93, p="\n".join(lines), c=c, a=a, r=R93, n=nn, k="관계절을 원래 문장으로 풀면 " + ", ".join(f"‘{o}’" for o in orig) + f"이므로 {c[a-1]}이다.", s=S93 + ipos(a))
f93("B", ["A. This is the house _____ which I was born.", "B. That's the reason _____ which she left early.", "C. I remember the day _____ which we graduated."],
    ["I was born in the house", "she left early for the reason", "we graduated on the day"], ["at - by - in", "on - of - at", "in - for - on", "in - with - for", "by - for - in"], 3)
f93("C", ["A. 2020 was the year _____ which we moved here.", "B. This is the pen _____ which I signed the contract.", "C. Tell me the way _____ which you solved it."],
    ["we moved here in the year", "I signed the contract with the pen", "you solved it in the way"], ["in - with - in", "at - by - on", "on - for - in", "in - by - at", "for - with - on"], 1)
f93("D", ["A. Friday is the day _____ which the store closes early.", "B. The box _____ which I keep my letters is old.", "C. The reason _____ which he was late is unknown."],
    ["the store closes early on the day", "I keep my letters in the box", "he was late for the reason"], ["in - at - for", "on - on - of", "at - in - by", "on - in - for", "for - in - on"], 4)
f93("E", ["A. The speed _____ which the car was moving was dangerous.", "B. The topic _____ which we talked was interesting.", "C. The time _____ which the train leaves is six."],
    ["the car was moving at the speed", "we talked about the topic", "the train leaves at the time"], ["in - of - on", "by - on - in", "at - for - in", "on - about - by", "at - about - at"], 5)
f93("F", ["A. The knife _____ which she cut the bread was sharp.", "B. This is the town _____ which my father grew up.", "C. Sunday is the day _____ which we go to church."],
    ["she cut the bread with the knife", "my father grew up in the town", "we go to church on the day"], ["by - at - in", "with - in - on", "for - of - at", "with - on - in", "in - in - on"], 2)

# 2-94 B: <보기> 순서를 바꿔 정답 기호를 원문항과 다르게
F(2, 94, "B", p="(a)<u>That</u> was the first cafe (b)<u>that</u> we visited.\n<보기>\nㄱ. The book that I bought is new.\nㄴ. That he passed surprised me.\nㄷ. I know that she is honest.\nㄹ. That is my seat.",
  c=["ㄷ-ㄱ", "ㄹ-ㄴ", "ㄹ-ㄱ", "ㄴ-ㄷ", "ㄷ-ㄹ"], a=3,
  r="지시대명사 that은 그 자체로 주어 등이 된다. 명사절 접속사 that은 완전한 절을 이끌며 절 안의 성분이 아니다. 관계대명사 that은 선행사를 꾸미는 절 안에서 주어·목적어 역할을 한다.",
  pre=["보기 판정: ㄱ 관계대명사(선행사 The book을 꾸밈), ㄴ 명사절 접속사(주어 자리), ㄷ 명사절 접속사(목적어 자리), ㄹ 지시대명사(‘저것’)."],
  k="(a) That은 뒤에 명사 없이 주어로 쓰인 지시대명사라 ㄹ과 같고, (b) that은 선행사(the first cafe)를 꾸미며 visited의 목적어 역할을 하는 관계대명사라 ㄱ과 같다.",
  n=["(a)는 지시대명사인데 ㄷ은 명사절 접속사이다. 따라서 오답이다.", "(b)는 관계대명사인데 ㄴ은 명사절 접속사이다. 따라서 오답이다.", "(a) 지시대명사 = ㄹ, (b) 관계대명사 = ㄱ으로 모두 알맞으므로 정답이다.",
     "(a)는 지시대명사인데 ㄴ은 명사절 접속사이고, (b)는 관계대명사인데 ㄷ은 명사절 접속사이다. 따라서 오답이다.", "(a)는 지시대명사인데 ㄷ은 명사절 접속사이고, (b)는 관계대명사인데 ㄹ은 지시대명사이다. 따라서 오답이다."],
  s="<보기>의 배열(ㄱ 명사절 주어, ㄴ 목적어절, ㄷ 관계대명사, ㄹ 지시대명사)과 정답 기호(ㄹ-ㄷ)가 원문항과 같았다. <보기> 순서를 바꿔 정답 기호를 ㄹ-ㄱ으로 하고, 줄을 바꿨다. 정답 위치 ③.")

# 2-95 관계사 설명 학생 네 명: 조건 삭제, 옳고 틀린 위치를 유형마다 다르게
ST95 = "다음 중 해당 문장을 올바르게 설명한 학생들을 모두 고르시오."
R95 = "목적격 관계대명사는 생략할 수 있지만 주격·소유격은 생략하지 않는다(주격 관계대명사 + be동사는 함께 생략할 수 있다). 관계부사는 전치사 + which로 바꿀 수 있고, the way와 how는 함께 쓰지 않으며, 전치사 뒤에는 that을 쓰지 않는다. what은 선행사를 포함한다."
S95 = "발문에 ‘관계대명사 생략은 그 단어만 생략하는 경우’라는 조건이 붙었고, 원문항(학생 네 명)과 달리 다섯 명이었으며, 모든 유형이 같은 옳음·틀림 순서라 정답이 예측되었다. 원문항 발문과 학생 네 명 형식으로 되돌리고, 조건 없이 판단되는 설명으로 새로 써 옳고 틀린 위치를 유형마다 달리했다."
def f95(t, lines, judge, ok, c, a):
    F(2, 95, t, st=ST95, p="\n".join(lines), c=c, a=a, r=R95, pre=["학생별 판정:"] + judge, k=f"올바르게 설명한 학생은 {ok}이다.", n=setnotes(c, ok, "올바르게 설명한 학생"), s=S95 + ipos(a))
f95("B", ["Mina: The book that I borrowed is useful. 에서 that은 생략할 수 있어.", "Leo: Jane is the girl who won the prize. 에서 who는 생략할 수 있어.",
          "Tom: This is the way how I solved it. 은 옳은 문장이야.", "Amy: This is the house in which I lived. 에서 in which는 where로 바꿀 수 있어."],
    ["Mina 옳음: borrowed의 목적어 역할을 하는 목적격 관계대명사라 생략할 수 있다.", "Leo 틀림: won의 주어 역할을 하는 주격 관계대명사라 생략할 수 없다.",
     "Tom 틀림: the way와 how는 함께 쓰지 않는다(the way I solved it 또는 how I solved it).", "Amy 옳음: 장소 선행사 뒤 in which는 관계부사 where로 바꿀 수 있다."],
    "Mina, Amy", ["Mina, Leo", "Mina, Amy", "Leo, Tom", "Mina, Tom, Amy", "Leo, Amy"], 2)
f95("C", ["Jane: The movie we watched was exciting. 은 목적격 관계대명사가 생략된 문장이야.", "Tom: The man lives next door is a doctor. 는 who가 생략된 옳은 문장이야.",
          "Mina: Monday is the day on which the shop is closed. 에서 on which는 when으로 바꿀 수 있어.", "Amy: What she said surprised me. 에서 what은 선행사를 포함해."],
    ["Jane 옳음: watched의 목적어 역할을 하는 관계대명사가 생략되었다.", "Tom 틀림: 주격 관계대명사(who)는 생략할 수 없어 동사가 두 개 겹친다.",
     "Mina 옳음: 시간 선행사 뒤 on which는 관계부사 when으로 바꿀 수 있다.", "Amy 옳음: what은 ‘~한 것’으로 선행사를 포함한다."],
    "Jane, Mina, Amy", ["Jane, Tom", "Tom, Mina, Amy", "Jane, Mina", "Jane, Mina, Amy", "Jane, Tom, Amy"], 4)
f95("D", ["Tom: The song which I like is old. 에서 which는 생략할 수 없어.", "Amy: The boy whose bike was stolen called the police. 에서 whose는 생략할 수 없어.",
          "Mina: Tell me the reason why you were late. 에서 why는 for which로 바꿀 수 있어.", "Leo: This is the town in that I grew up. 은 옳은 문장이야."],
    ["Tom 틀림: like의 목적어 역할을 하는 목적격 관계대명사라 생략할 수 있다.", "Amy 옳음: 소유격 관계대명사(whose)는 생략할 수 없다.",
     "Mina 옳음: 이유 선행사 뒤 why는 for which로 바꿀 수 있다.", "Leo 틀림: 전치사 뒤에는 that을 쓰지 않으므로 in which로 써야 한다."],
    "Amy, Mina", ["Tom, Amy", "Mina, Leo", "Amy, Mina", "Tom, Amy, Mina", "Amy, Mina, Leo"], 3)
f95("E", ["Mina: The phone I bought is expensive. 는 옳은 문장이야.", "Leo: The boy who is running is Tom. 에서 who is를 함께 생략해 The boy running is Tom.으로 쓸 수 있어.",
          "Jane: I know the reason why she cried. 에서 the reason과 why는 함께 쓸 수 없어.", "Tom: What he wants is clear. 에서 What은 The thing which로 바꿀 수 있어."],
    ["Mina 옳음: bought의 목적어 역할을 하는 관계대명사가 생략된 옳은 문장이다.", "Leo 옳음: 주격 관계대명사 + be동사는 함께 생략할 수 있다.",
     "Jane 틀림: the reason why는 함께 쓸 수 있다(둘 중 하나를 생략해도 된다).", "Tom 옳음: what은 the thing which(that)로 바꿀 수 있다."],
    "Mina, Leo, Tom", ["Mina, Leo", "Leo, Jane, Tom", "Mina, Jane", "Jane, Tom", "Mina, Leo, Tom"], 5)
f95("F", ["Amy: The cake that we made was good. 에서 that은 which로 바꿀 수 있어.", "Tom: The teacher who helped me is kind. 에서 who 대신 that을 쓸 수 있어.",
          "Jane: This is the house where she lives. 에서 where는 which로 바꿀 수 있어.", "Mina: I don't like the way he talks. 는 옳은 문장이야."],
    ["Amy 옳음: 사물 선행사 뒤 목적격 관계대명사 that은 which로 바꿀 수 있다.", "Tom 옳음: 사람 선행사 뒤 주격 관계대명사 who는 that으로 바꿀 수 있다.",
     "Jane 틀림: where는 in which로 바꿔야 하며 which만으로는 lives 뒤 장소를 나타내지 못한다.", "Mina 옳음: the way 뒤에 how 없이 절이 온 옳은 문장이다."],
    "Amy, Tom, Mina", ["Amy, Tom, Mina", "Tom, Jane", "Amy, Jane, Mina", "Amy, Tom", "Tom, Jane, Mina"], 1)

# 2-96 관계절·주절 동사 수 일치 + 소유대명사: 원문항 형식(한 문장의 변형 다섯 개)
ST96 = "다음 중 어법상 올바른 문장을 고르시오."
R96 = "주격 관계대명사 뒤 동사는 선행사에, 주절의 동사는 문장의 주어에 수를 맞춘다. be동사 뒤 ‘~의 것’은 소유대명사(mine, ours, hers)로 쓰고, 명사 앞에는 소유격(my, our, her)을 쓴다."
S96 = "원문항은 관계절 동사와 주절 동사의 수 일치·소유대명사를 묻는데, 변형은 선행사에 따른 who/which 선택을 물었고 오답 네 문장이 유형마다 같았다. 원문항처럼 한 문장의 수 일치·소유대명사를 바꾼 다섯 문장으로 다시 썼다."
def f96(t, items, a):
    mk(2, 96, t, items, a, R96, S96, st=ST96)
f96("B", [("The shoes which is by the door are mine.", "관계절 동사는 복수 선행사(The shoes)에 맞춰 are로 써야 하므로"), ("The shoes which are by the door is mine.", "주절 동사는 복수 주어(The shoes)에 맞춰 are로 써야 하므로"),
          ("The shoes which is by the door is my.", "두 동사가 모두 단수이고, be동사 뒤에는 소유대명사(mine)를 써야 하므로"), ("The shoes which are by the door are my.", "be동사 뒤에는 소유격(my)이 아니라 소유대명사(mine)를 써야 하므로"),
          ("The shoes which are by the door are mine.", "관계절 동사(are)와 주절 동사(are)가 복수 선행사·주어에 맞고, 소유대명사(mine)도 바르므로")], 5)
f96("C", [("The girl who live next door is my cousin.", "관계절 동사는 단수 선행사(The girl)에 맞춰 lives로 써야 하므로"), ("The girl who lives next door are my cousin.", "주절 동사는 단수 주어(The girl)에 맞춰 is로 써야 하므로"),
          ("The girl who lives next door is my cousin.", "관계절 동사(lives)와 주절 동사(is)가 단수 선행사·주어에 맞고, 명사 앞 소유격(my)도 바르므로"), ("The girl who live next door are my cousin.", "두 동사가 모두 단수 주어(The girl)와 맞지 않으므로"),
          ("The girl who lives next door is mine cousin.", "명사(cousin) 앞에는 소유대명사가 아니라 소유격(my)을 써야 하므로")], 3)
f96("D", [("The cookies that is in the jar are ours.", "관계절 동사는 복수 선행사(The cookies)에 맞춰 are로 써야 하므로"), ("The cookies that are in the jar are ours.", "관계절 동사(are)와 주절 동사(are)가 복수 선행사·주어에 맞고, 소유대명사(ours)도 바르므로"),
          ("The cookies that are in the jar is ours.", "주절 동사는 복수 주어(The cookies)에 맞춰 are로 써야 하므로"), ("The cookies that are in the jar are our.", "be동사 뒤에는 소유격(our)이 아니라 소유대명사(ours)를 써야 하므로"),
          ("The cookies that is in the jar is our.", "두 동사가 모두 단수이고, be동사 뒤에는 소유대명사(ours)를 써야 하므로")], 2)
f96("E", [("The man who have two dogs lives near my house.", "관계절 동사는 단수 선행사(The man)에 맞춰 has로 써야 하므로"), ("The man who has two dogs live near my house.", "주절 동사는 단수 주어(The man)에 맞춰 lives로 써야 하므로"),
          ("The man who have two dogs live near my house.", "두 동사가 모두 단수 주어(The man)와 맞지 않으므로"), ("The man who has two dogs lives near my house.", "관계절 동사(has)와 주절 동사(lives)가 단수 선행사·주어에 맞고, 명사 앞 소유격(my)도 바르므로"),
          ("The man who has two dogs lives near mine house.", "명사(house) 앞에는 소유대명사가 아니라 소유격(my)을 써야 하므로")], 4)
f96("F", [("The bag which belongs to Jane is hers.", "관계절 동사(belongs)와 주절 동사(is)가 단수 선행사·주어에 맞고, 소유대명사(hers)도 바르므로"), ("The bag which belong to Jane is hers.", "관계절 동사는 단수 선행사(The bag)에 맞춰 belongs로 써야 하므로"),
          ("The bag which belongs to Jane are hers.", "주절 동사는 단수 주어(The bag)에 맞춰 is로 써야 하므로"), ("The bag which belongs to Jane is her.", "be동사 뒤 ‘그녀의 것’은 소유대명사(hers)로 써야 하므로"),
          ("The bag which belong to Jane is her.", "관계절 동사가 선행사와 맞지 않고, be동사 뒤에는 소유대명사(hers)를 써야 하므로")], 1)

# 2-98 주격 관계대명사 + be동사 생략: 원문항 형식(제시문 줄여 쓰기)
ST98 = "다음 문장에서 생략 가능한 부분을 생략하여 다시 쓴 문장으로 옳은 것은?"
R98 = "주격 관계대명사 + be동사는 함께 생략할 수 있고, 남은 분사(-ing, 과거분사)나 전치사구가 앞의 명사를 꾸민다. 관계대명사나 be동사 하나만 생략하지 않으며, 문장의 동사는 그대로 둔다."
S98 = "원문항은 ‘주격 관계대명사 + be동사’를 생략해 다시 쓴 문장을 고르는 형식인데, 변형은 제시문 없이 괄호 안 관계대명사(목적격)를 생략할 수 있는 문장을 고르는 형식으로 바뀌었다. 원문항 발문과 형식(관계대명사 + be동사가 두 번 나오는 문장을 줄여 쓰기)으로 다시 썼다."
W98 = {"ok": "관계대명사 + be동사를 두 곳 모두 함께 생략하고 문장의 동사를 그대로 두었으므로", "rel": "관계대명사를 남기고 be동사만 생략해 관계절에 동사가 없으므로",
       "be": "관계대명사만 생략하고 be동사를 남겨 동사가 여러 개 겹치므로", "half": "둘째 관계절에서 관계대명사만 남기고 be동사를 생략했으므로",
       "verb": "문장의 동사까지 -ing로 바꿔 문장에 동사가 없으므로", "act": "수동 관계인데 현재분사를 써서 뜻이 맞지 않으므로"}
def f98(t, p, items, a):
    mk(2, 98, t, [(x, W98[e]) for x, e in items], a, R98, S98, st=ST98, p=p)
f98("B", "The cake which was baked by Mina and the cookies which are on the plate look delicious.",
    [("The cake which baked by Mina and the cookies on the plate look delicious.", "rel"), ("The cake baked by Mina and the cookies which on the plate look delicious.", "half"),
     ("The cake baked by Mina and the cookies on the plate look delicious.", "ok"), ("The cake was baked by Mina and the cookies are on the plate look delicious.", "be"),
     ("The cake baked by Mina and the cookies on the plate looking delicious.", "verb")], 3)
f98("C", "The man who is standing at the door and the woman who is sitting on the bench are my parents.",
    [("The man standing at the door and the woman sitting on the bench are my parents.", "ok"), ("The man is standing at the door and the woman is sitting on the bench are my parents.", "be"),
     ("The man who standing at the door and the woman sitting on the bench are my parents.", "rel"), ("The man standing at the door and the woman who sitting on the bench are my parents.", "half"),
     ("The man standing at the door and the woman sitting on the bench being my parents.", "verb")], 1)
f98("D", "The letters which were written by my grandpa and the photos which are in this box are precious.",
    [("The letters writing by my grandpa and the photos in this box are precious.", "act"), ("The letters which written by my grandpa and the photos in this box are precious.", "rel"),
     ("The letters were written by my grandpa and the photos are in this box are precious.", "be"), ("The letters written by my grandpa and the photos in this box being precious.", "verb"),
     ("The letters written by my grandpa and the photos in this box are precious.", "ok")], 5)
f98("E", "The girl who is singing on the stage and the boy who is playing the guitar are twins.",
    [("The girl who singing on the stage and the boy playing the guitar are twins.", "rel"), ("The girl singing on the stage and the boy playing the guitar are twins.", "ok"),
     ("The girl is singing on the stage and the boy is playing the guitar are twins.", "be"), ("The girl singing on the stage and the boy who playing the guitar are twins.", "half"),
     ("The girl singing on the stage and the boy playing the guitar being twins.", "verb")], 2)
f98("F", "The bridge which was built in 1900 and the tower which is next to it are famous.",
    [("The bridge was built in 1900 and the tower is next to it are famous.", "be"), ("The bridge building in 1900 and the tower next to it are famous.", "act"),
     ("The bridge built in 1900 and the tower which next to it are famous.", "half"), ("The bridge built in 1900 and the tower next to it are famous.", "ok"),
     ("The bridge which built in 1900 and the tower next to it are famous.", "rel")], 4)

# 2-99 whose 설명: 오답 네 개를 유형마다 새로
R99 = "관계대명사 whose는 선행사와 뒤 명사의 소유 관계를 나타내며, 사람·사물 선행사 모두에 쓴다. whose + 명사 전체가 관계절에서 주어·목적어 등의 성분이 되고, 생략하거나 who·which·that으로 바꿀 수 없다."
S99 = "오답 네 개가 C와 똑같아서 유형마다 새로 썼다."
mk(2, 99, "D", [("whose는 ‘누구의 것’을 묻는 의문사로 쓰였다.", "선행사(a neighbor)를 꾸미는 관계대명사이며 의문사가 아니므로"), ("neighbor와 dog의 소유 관계를 연결하는 관계대명사 whose이다.", "선행사와 뒤 명사의 소유 관계를 바르게 설명했으므로"),
                ("whose 대신 who를 써도 뜻과 어법이 같다.", "who는 소유 관계를 나타내지 못해 ‘a neighbor who dog barks’는 틀린 문장이 되므로"), ("whose dog 전체가 관계절에서 동사 barks의 목적어이다.", "whose dog은 barks의 주어이므로"),
                ("whose는 선행사가 사물일 때만 쓸 수 있다.", "whose는 사람·사물 선행사 모두에 쓰며 여기서도 사람 선행사에 쓰였으므로")], 2, R99, S99)
mk(2, 99, "E", [("whose는 사람 선행사에만 쓰므로 company 뒤에는 쓸 수 없다.", "whose는 사물 선행사에도 쓸 수 있으므로"), ("whose 대신 which를 써도 문장이 성립한다.", "which는 소유 관계를 나타내지 못해 ‘the company which products …’는 틀린 문장이 되므로"),
                ("whose는 목적격이므로 생략할 수 있다.", "whose는 소유격 관계대명사라 생략할 수 없으므로"), ("company와 products의 소유 관계를 나타내는 whose가 명사를 수식한다.", "선행사와 뒤 명사의 소유 관계를 바르게 설명했으므로"),
                ("products 앞에 their를 더 넣어야 어법상 옳다.", "whose가 이미 소유 관계를 나타내므로 their를 더 쓰지 않으므로")], 4, R99, S99)
mk(2, 99, "F", [("whose는 앞 문장 전체를 받는 계속적 용법으로 쓰였다.", "쉼표 없이 선행사(a teacher)를 바로 꾸미는 제한적 용법이므로"), ("teacher와 classes의 소유 관계를 나타내며 whose는 소유격 관계대명사이다.", "선행사와 뒤 명사의 소유 관계를 바르게 설명했으므로"),
                ("whose 대신 that을 쓸 수 있다.", "that은 소유 관계를 나타내지 못하므로"), ("whose는 teacher를 가리키므로 뒤의 동사는 단수형 is로 맞춰야 한다.", "관계절의 주어는 whose classes이므로 동사는 복수형 are가 맞으므로"),
                ("whose는 주격 관계대명사이므로 뒤에 바로 동사가 와야 한다.", "whose 뒤에는 명사(classes)가 먼저 오므로")], 2, R99, S99)

# 2-100 what 문장 조합: 원문항 발문(옳은 문장으로만), 줄바꿈, 정답이 하나가 되게 보기 조정
ST100 = "다음 중 어법상 옳은 문장으로만 묶인 것을 고르시오."
R100 = "what은 선행사를 포함해 ‘~하는 것’의 뜻으로 관계절 안에서 주어·목적어가 된다. 선행사(the thing, everything, all 등)가 있으면 what 대신 that·which를 쓰고, what 뒤 절에는 목적어를 다시 쓰지 않는다."
S100 = "발문에 ‘표준 영어에서’, ‘모두 빠짐없이’가 덧붙었고 줄바꿈이 없었다. 원문항 발문(옳은 문장으로만 묶인 것)으로 되돌리고 줄을 바꿨다. 옳은 문장이 넷이면 그 일부만 묶은 보기도 답이 되므로, 한 문장을 틀린 문장으로 바꿔 옳은 문장을 셋으로 하고 보기를 원문항처럼 모두 세 문장 조합으로 짰다."
def f100(t, lines, judge, ok, c, a, s=S100):
    F(2, 100, t, st=ST100, p="\n".join(lines), c=c, a=a, r=R100, pre=["문장별 판정: " + j for j in judge], k=f"옳은 문장은 {ok}이고, 이 문장들로만 묶인 보기가 정답이다.",
      n=setnotes(c, ok, "옳은 문장"), s=s + ipos(a))
f100("B", ["(가) What the witness described matched the video.", "(나) The detail what she mentioned was important.", "(다) What we discovered it changed the plan.", "(라) I understood what he meant.", "(마) Everything that the report contained was checked."],
     ["(가) O. what이 ‘~한 것’으로 described의 목적어 역할을 한다.", "(나) X. 선행사(The detail) 뒤에는 what을 쓰지 않는다.", "(다) X. what이 이미 discovered의 목적어이므로 it을 다시 쓰지 않는다.",
      "(라) O. what이 meant의 목적어 역할을 한다.", "(마) O. 선행사(Everything) + 관계대명사 that이다."], "(가), (라), (마)", ["(가), (나), (다)", "(나), (다), (라)", "(가), (다), (마)", "(가), (라), (마)", "(나), (라), (마)"], 4,
     "정답 조합과 위치가 원문항과 같았다. 원문항 발문으로 되돌리고, 원문항처럼 옳은 문장을 셋으로 하되 조합을 (가), (라), (마)로 바꿨다. 보기는 모두 세 문장 조합이다. 문장마다 줄을 바꿨다.")
f100("C", ["(가) I understand what you mean.", "(나) The movie which we saw was boring.", "(다) What Tom needs is rest.", "(라) The thing what she lost was valuable.", "(마) All what I know is this."],
     ["(가) O. what이 mean의 목적어 역할을 한다.", "(나) O. 선행사(The movie) + 관계대명사 which이다.", "(다) O. what이 needs의 목적어 역할을 한다.", "(라) X. 선행사(The thing) 뒤에는 what을 쓰지 않는다.", "(마) X. 선행사(All) 뒤에는 what이 아니라 that을 쓴다."],
     "(가), (나), (다)", ["(가), (나), (다)", "(가), (라), (마)", "(나), (다), (라)", "(가), (다), (마)", "(나), (라), (마)"], 1)
f100("D", ["(가) She gave me what I asked for.", "(나) The car what Tom drives is new.", "(다) What happened surprised everyone.", "(라) The thing that he said was rude.", "(마) Everything what we need is here."],
     ["(가) O. what이 전치사 for의 목적어 역할을 한다.", "(나) X. 선행사(The car) 뒤에는 what을 쓰지 않는다.", "(다) O. what이 happened의 주어 역할을 한다.", "(라) O. 선행사(The thing) + 관계대명사 that이다.", "(마) X. 선행사(Everything) 뒤에는 what이 아니라 that을 쓴다."],
     "(가), (다), (라)", ["(가), (나), (다)", "(가), (다), (라)", "(나), (라), (마)", "(가), (라), (마)", "(나), (다), (마)"], 2)
f100("E", ["(가) I remember what Jane told me.", "(나) The song that he wrote is beautiful.", "(다) What Mina bought it was expensive.", "(라) The thing what I need is time.", "(마) All that matters is effort."],
     ["(가) O. what이 told의 직접목적어 역할을 한다.", "(나) O. 선행사(The song) + 관계대명사 that이다.", "(다) X. what이 이미 bought의 목적어이므로 it을 다시 쓰지 않는다.", "(라) X. 선행사(The thing) 뒤에는 what을 쓰지 않는다.", "(마) O. 선행사(All) + 관계대명사 that이다."],
     "(가), (나), (마)", ["(가), (다), (마)", "(나), (다), (라)", "(가), (나), (라)", "(다), (라), (마)", "(가), (나), (마)"], 5)
f100("F", ["(가) Tell me what did you see.", "(나) The place where we stayed was crowded.", "(다) What he decided was unexpected.", "(라) I know what that she wants.", "(마) Everything that Tom owns is old."],
     ["(가) X. what 뒤 절은 ‘주어 + 동사’ 어순이므로 what you saw로 써야 한다.", "(나) O. 장소 선행사 + 관계부사 where이다.", "(다) O. what이 decided의 목적어 역할을 한다.", "(라) X. what과 that을 겹쳐 쓸 수 없다.", "(마) O. 선행사(Everything) + 관계대명사 that이다."],
     "(나), (다), (마)", ["(가), (나), (다)", "(가), (다), (라)", "(나), (다), (마)", "(나), (라), (마)", "(가), (다), (마)"], 3)

# ---- 2차 감수(2026-10) 추가 ----
# 2-94 C~F: 한 줄로 이어 쓴 <보기>를 원문항처럼 한 줄에 하나씩
for t in "CDEF":
    F(2, 94, t, p=re.sub(r" (?=[ㄱ-ㄹ]\. )", "\n", V(2, 94, t)["passage"].replace("<보기> ", "<보기>\n")), s="<보기>의 ㄱ~ㄹ이 한 줄로 이어져 있어 원문항처럼 한 줄에 하나씩 나눴다. 문장·보기·정답은 그대로다.")
