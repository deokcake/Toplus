import re
# 1급 CH9 관계사 (81~90) 수정 예시

# 1-82 what / 계속적 용법: 오답 네 문장을 유형마다 새로(틀린 문장과 짝 없애기)
R82 = "what은 선행사를 포함하므로 선행사 뒤에 쓰지 않는다(the thing what ×). 쉼표 뒤 계속적 용법에는 that을 쓰지 않고 사람은 who/whom, 사물은 which를 쓴다."
S82 = "오답 네 문장이 B와 똑같고 틀린 문장이 같은 표현의 옳은 문장과 짝을 이뤘다. 옳은 문장 네 개와 틀린 문장을 B와 겹치지 않게 새로 썼다."
def f82(t, items, a):
    F(1, 82, t, c=[x for x, _ in items], a=a, r=R82, n=[(w + (" 틀린 문장이므로 정답이다." if i + 1 == a else " 올바르므로 오답이다.")) for i, (_, w) in enumerate(items)], s=S82 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f82("C", [("What I need now is a long rest.", "what이 선행사를 포함해 주어 역할을 한다."), ("This is the bag which my aunt gave me.", "사물 선행사 뒤에 which를 썼다."),
          ("We cannot accept the explanation what he gave us.", "선행사 the explanation 뒤에 what을 겹쳐 썼다. that(which)으로 고쳐야 한다."), ("My brother, who lives in Busan, visited us.", "쉼표 뒤 계속적 용법에 who를 썼다."),
          ("She told me what she wanted for her birthday.", "what이 told의 목적어 역할을 한다.")], 3)
f82("D", [("What surprised me was his calm voice.", "what이 선행사를 포함해 주어 역할을 한다."), ("The movie that we saw last night was scary.", "선행사 뒤 제한적 용법에 that을 썼다."),
          ("I lost the watch what my dad bought me.", "선행사 the watch 뒤에 what을 겹쳐 썼다. that(which)으로 고쳐야 한다."), ("My grandmother, whom I love very much, is ninety.", "쉼표 뒤 계속적 용법에 whom을 썼다."),
          ("Show me what you have in your hand.", "what이 show의 목적어 역할을 한다.")], 3)
f82("E", [("I visited Paris, that is famous for its art.", "쉼표 뒤 계속적 용법에는 that을 쓰지 않는다. which로 고쳐야 한다."), ("What you said made me happy.", "what이 선행사를 포함해 주어 역할을 한다."),
          ("The boy who is singing on the stage is my cousin.", "사람 선행사 뒤에 who를 썼다."), ("This is exactly what I wanted.", "what이 보어 자리의 명사절을 이끈다."),
          ("Seoul, which is the capital of Korea, has many palaces.", "쉼표 뒤 계속적 용법에 which를 썼다.")], 1)
f82("F", [("What he does after school is a secret.", "what이 선행사를 포함해 주어 역할을 한다."), ("I have a friend whose father is a pilot.", "소유격 관계대명사 whose를 썼다."),
          ("The cake which she baked was delicious.", "사물 선행사 뒤에 which를 썼다."), ("We believed what the teacher told us.", "what이 believed의 목적어 역할을 한다."),
          ("The thing what matters most is honesty.", "선행사 The thing 뒤에 what을 겹쳐 썼다. that으로 고쳐야 한다.")], 5)

# 1-83 the way how / 관계부사: 오타형 오류를 실제 문법 오류로
R83 = "선행사에 맞춰 시간은 when, 장소는 where, 이유는 why를 쓴다. 방법은 the way 또는 how 중 하나만 쓰고 the way how로 겹쳐 쓰지 않는다."
def f83(t, items, a, s):
    F(1, 83, t, c=[x for x, _ in items], a=a, r=R83, n=[(w + (" 틀린 문장이므로 정답이다." if i + 1 == a else " 올바르므로 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f83("B", [("This is how Mina solved the puzzle.", "how 하나로 방법을 나타냈다."), ("That is the place where we met.", "장소 선행사 뒤에 where를 썼다."), ("Tell me the reason why Tom left.", "이유 선행사 뒤에 why를 썼다."),
          ("This is the way how Mina organized the files.", "the way와 how를 겹쳐 썼다. the way 또는 how 하나만 써야 한다."), ("Summer is the season when we go swimming.", "시간 선행사 뒤에 when을 썼다.")], 4,
    "⑤ ‘This is the way Mina organized the files.’가 정답 ④에서 how만 뺀 문장이라 둘 중 하나가 답이라는 단서가 되었다. ⑤를 다른 옳은 문장으로 바꿨다.")
S83 = "틀린 문장이 ‘why how’, ‘why why’처럼 낱말을 겹쳐 쓴 오타형이라 원문항이 묻는 문법(the way how 불가)이 아니었다. 틀린 문장을 실제 문법 오류({})로 다시 쓰고, B와 같던 옳은 문장 네 개도 새로 썼다."
f83("C", [("I remember the day when my brother was born.", "시간 선행사 뒤에 when을 썼다."), ("This is the restaurant where we had our first date.", "장소 선행사 뒤에 where를 썼다."),
          ("Nobody knows the reason why the bus was late.", "이유 선행사 뒤에 why를 썼다."), ("Do you know the way how this machine works?", "the way와 how를 겹쳐 썼다. the way 또는 how 하나만 써야 한다."),
          ("This is how I learned to swim.", "how 하나로 방법을 나타냈다.")], 4, S83.format("the way how"))
f83("D", [("Friday is the day when we have music class.", "시간 선행사 뒤에 when을 썼다."), ("This is the town when my father grew up.", "장소 선행사 the town 뒤에 when을 썼다. where로 고쳐야 한다."),
          ("Tell me how you fixed the computer.", "how 하나로 방법을 나타냈다."), ("I know the reason why she is angry.", "이유 선행사 뒤에 why를 썼다."), ("This is the way I cook rice.", "the way 하나로 방법을 나타냈다.")], 2,
    S83.format("선행사와 관계부사 불일치"))
f83("E", [("The hotel where we stayed was near the beach.", "장소 선행사 뒤에 where를 썼다."), ("I'll never forget the moment when I heard the news.", "시간 선행사 뒤에 when을 썼다."),
          ("That is why I was late.", "why 하나로 이유를 나타냈다."), ("This is the way she solves math problems.", "the way 하나로 방법을 나타냈다."),
          ("Please show me the way how you made this robot.", "the way와 how를 겹쳐 썼다. the way 또는 how 하나만 써야 한다.")], 5, S83.format("the way how"))
f83("F", [("I don't know the reason where he left so early.", "이유 선행사 the reason 뒤에 where를 썼다. why로 고쳐야 한다."), ("Winter is the season when many birds fly south.", "시간 선행사 뒤에 when을 썼다."),
          ("This is the park where I walk my dog.", "장소 선행사 뒤에 where를 썼다."), ("This is how the story ends.", "how 하나로 방법을 나타냈다."), ("The way he talks is funny.", "the way 하나로 방법을 나타냈다.")], 1,
    S83.format("선행사와 관계부사 불일치"))

# 1-84 생략할 수 있는 관계대명사: 밑줄 복원, 오답을 유형마다 새로(계속적 용법 포함)
R84 = "관계대명사는 제한적 용법의 목적격일 때만 생략할 수 있다. 주격이나, 쉼표 뒤 계속적 용법의 관계대명사는 생략할 수 없다."
F(1, 84, "B", c=["The dog (<u>that</u>) barked all night is tired.", "The man (<u>who</u>) called me is my uncle.", "The student (<u>who</u>) is waiting is Mina.", "The movie (<u>that</u>) we watched was excellent.", "The book (<u>which</u>) is on the desk is mine."],
  keepx=True, s="원문항처럼 괄호 속 관계대명사에 밑줄을 넣었다. 문장과 정답은 그대로다.")
OBJ = "제한적 용법의 목적격 관계대명사라 생략할 수 있다. 정답이다."
SUBJ = "주격 관계대명사라 생략할 수 없다. 오답이다."
NONR = "쉼표 뒤 계속적 용법이라 목적격이어도 생략할 수 없다. 오답이다."
NONRS = "쉼표 뒤 계속적 용법의 주격이라 생략할 수 없다. 오답이다."
S84 = "주격 관계대명사 오답 네 문장이 B와 똑같았다. 원문항처럼 쉼표 뒤 계속적 용법 문장을 넣어 오답을 유형마다 새로 썼다."
def f84(t, items, a):
    F(1, 84, t, c=[x for x, _ in items], a=a, r=R84, n=[k for _, k in items], s=S84 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f84("C", [("My uncle, (<u>who</u>) lives in Jeju, grows oranges.", NONRS), ("The girl (<u>who</u>) won the race is my classmate.", SUBJ), ("That is the consultant (<u>whom</u>) Mina recommended.", OBJ),
          ("This phone, (<u>which</u>) I bought last week, is already broken.", NONR), ("The bus (<u>that</u>) goes to the airport is late.", SUBJ)], 3)
f84("D", [("This is the book (<u>which</u>) Tom lent me.", OBJ), ("Paris, (<u>which</u>) I visited last year, is beautiful.", NONR), ("The man (<u>who</u>) fixed my bike is very kind.", SUBJ),
          ("My sister, (<u>who</u>) is a nurse, works at night.", NONRS), ("The river (<u>that</u>) flows through the city is clean.", SUBJ)], 1)
f84("E", [("Mr. Lee, (<u>whom</u>) everyone respects, is our principal.", NONR), ("The cat (<u>that</u>) is sleeping on the sofa is Tom's.", SUBJ), ("The dress, (<u>which</u>) was made in Italy, is expensive.", NONRS),
          ("The person (<u>whom</u>) I spoke to was helpful.", OBJ), ("The students (<u>who</u>) passed the test were happy.", SUBJ)], 4)
f84("F", [("Jeju Island, (<u>which</u>) many tourists visit, is famous for its beaches.", NONR), ("The problem (<u>which</u>) Jane solved was difficult.", OBJ), ("The teacher (<u>who</u>) teaches us science is funny.", SUBJ),
          ("My best friend, (<u>whom</u>) I met in kindergarten, moved away.", NONR), ("The train (<u>that</u>) leaves at noon is full.", SUBJ)], 2)

# 1-85 밑줄 친 관계사 틀린 문장 개수: 원문항처럼 문장 6개, 1개~5개 정렬, 틀린 문장 포함
R85 = "전치사 바로 뒤에는 that을 쓰지 않고(in which), what은 선행사 없이 쓴다. 관계부사·소유격(whose)을 선행사와 뒤 절에 맞게 쓰고, 복합관계사(whatever, whoever, whichever)는 명사절·양보절을 이끈다."
S85 = "원문항은 보기 문장 6개·선택지 1개~5개인데 변형은 5개·0개~4개였고 순서가 뒤섞였다. 문장 f를 더해 6개로 맞추고, 선택지를 1개~5개 순으로 정렬했으며 발문도 원문항과 같게 했다."
def f85(t, lines, judge, wrong, s):
    F(1, 85, t, st="R", p="\n".join(lines), c=CNT5, a=wrong, r=R85, pre=["문장별 판정:"] + judge, k=f"밑줄 친 부분이 어법상 틀린 문장은 {wrong}개이다.", n="cnt", s=s)
CNT5 = ["1개", "2개", "3개", "4개", "5개"]
f85("B", ["a) <u>Whatever</u> she says, I will listen.", "b) This is the reason for <u>that</u> he resigned.", "c) <u>Whoever</u> wins will receive a prize.", "d) Pick <u>whichever</u> color you like.", "e) The thing <u>what</u> happened was unexpected.", "f) We will hire <u>whoever</u> is qualified."],
    ["a) 옳음: 양보절을 이끄는 whatever이다.", "b) 틀림: 전치사 뒤에는 that을 쓰지 않는다. for which(= why).", "c) 옳음: 주어가 되는 명사절을 이끄는 whoever이다.", "d) 옳음: whichever + 명사가 목적어 명사절을 이끈다.",
     "e) 틀림: 선행사 The thing 뒤에는 what이 아니라 that을 쓴다.", "f) 옳음: 전치사·동사의 목적어가 되는 명사절을 이끄는 whoever이다."], 2, S85)
f85("C", ["a) <u>Whatever</u> you decide, I will support you.", "b) This is the room in <u>that</u> we met.", "c) <u>Whoever</u> calls, tell them I am busy.", "d) Take <u>whichever</u> seat is available.", "e) <u>What</u> he said surprised me.", "f) <u>Whichever</u> team wins, we will celebrate."],
    ["a) 옳음: 양보절을 이끄는 whatever이다.", "b) 틀림: 전치사 뒤에는 that을 쓰지 않는다. in which(= where).", "c) 옳음: 양보절을 이끄는 whoever이다.", "d) 옳음: whichever + 명사가 목적어 명사절을 이끈다.",
     "e) 옳음: 선행사를 포함한 what이 주어 명사절을 이끈다.", "f) 옳음: 양보절을 이끄는 whichever이다."], 1, S85)
f85("D", ["a) <u>Whoever</u> finishes first may leave.", "b) This is the town <u>which</u> Mina was born.", "c) <u>Whatever</u> happens, stay calm.", "d) Choose <u>whichever</u> option you prefer.", "e) <u>That</u> Tom needs is rest.", "f) I can't find the key <u>what</u> I put on the table."],
    ["a) 옳음: 주어가 되는 명사절을 이끄는 whoever이다.", "b) 틀림: 뒤 절에 빈자리가 없으므로 where(in which)를 써야 한다.", "c) 옳음: 양보절을 이끄는 whatever이다.", "d) 옳음: whichever + 명사가 목적어 명사절을 이끈다.",
     "e) 틀림: 선행사가 없으므로 That이 아니라 What을 써야 한다.", "f) 틀림: 선행사 the key가 있으므로 what이 아니라 which(that)를 써야 한다."], 3,
    S85 + " 틀린 문장이 하나도 없어 원문항과 달랐으므로 b, e, f에 관계사 오류를 넣었다.")
f85("E", ["a) <u>Whoever</u> arrives early can help.", "b) This is the desk <u>which</u> I left my bag.", "c) <u>Whatever</u> you choose is fine.", "d) Use <u>whichever</u> tool works.", "e) <u>What</u> matters is effort.", "f) The man <u>who</u> car was stolen called the police."],
    ["a) 옳음: 주어가 되는 명사절을 이끄는 whoever이다.", "b) 틀림: 뒤 절에 빈자리가 없으므로 where(on which)를 써야 한다.", "c) 옳음: 주어가 되는 명사절을 이끄는 whatever이다.", "d) 옳음: whichever + 명사가 목적어 명사절을 이끈다.",
     "e) 옳음: 선행사를 포함한 what이 주어 명사절을 이끈다.", "f) 틀림: ‘그 남자의 차’이므로 소유격 whose를 써야 한다."], 2,
    S85 + " 틀린 문장이 하나도 없어 원문항과 달랐으므로 b, f에 관계사 오류를 넣었다.")
f85("F", ["a) <u>Whatever</u> the result is, we will continue.", "b) This is the city in <u>that</u> he lives.", "c) <u>Whoever</u> told you was wrong.", "d) Choose <u>whichever</u> route is shorter.", "e) <u>What</u> she bought was expensive.", "f) She lives in a house <u>whose</u> roof is red."],
    ["a) 옳음: 양보절을 이끄는 whatever이다.", "b) 틀림: 전치사 뒤에는 that을 쓰지 않는다. in which(= where).", "c) 옳음: 주어가 되는 명사절을 이끄는 whoever이다.", "d) 옳음: whichever + 명사가 목적어 명사절을 이끈다.",
     "e) 옳음: 선행사를 포함한 what이 주어 명사절을 이끈다.", "f) 옳음: ‘집의 지붕’이므로 소유격 whose를 썼다."], 1, S85)

# 1-86 D: ⑤ the reason that(표준 영어에서 가능) → 명백히 틀린 문장으로
c = ["I know the reason what Mina left early.", "I know the reason why Mina left early.", "I know the reason which Mina left early.", "I know the reason where Mina left early.", "I know the reason how Mina left early."]
F(1, 86, "D", c=c, a=2,
  n=["what은 선행사를 포함하므로 the reason 뒤에 쓸 수 없다.", "이유의 선행사 the reason 뒤에 관계부사 why를 써서 for which를 바르게 바꿨다.", "which만 쓰면 뒤 절에 빠진 성분이 없어 맞지 않는다. for which로 써야 한다.",
     "where는 장소를 나타내므로 이유의 선행사와 맞지 않는다.", "how는 방법을 나타내므로 이유의 선행사와 맞지 않는다."],
  s="⑤ ‘the reason that Mina left early’는 표준 영어에서도 쓰여 복수 정답 시비가 생길 수 있었다. ⑤를 명백히 틀린 ‘the reason how Mina left early’로 바꿨다.")

# 1-87 <보기> 배열 여섯 번째 단어: 우리말·규칙 설명 없이도 답이 하나가 되게
R87 = "관계절은 수식하는 선행사 바로 뒤에 두고, 주어 + 동사 + 목적어 순서로 문장을 완성한 뒤 단어의 순서를 센다."
def f87(t, words, sent, c, s):
    ws = sent.rstrip(".").split(); sixth = ws[5]; a = c.index(sixth) + 1
    lines = [" / ".join(words[i:i + 4]) for i in range(0, len(words), 4)]
    blanks = " ".join(["_____"] * 5 + ["___★___"] + ["_____"] * (len(ws) - 6)) + " ."
    n = [(f"완성 문장 ‘{sent}’에서 여섯 번째 단어이다. 정답이다." if x == sixth else f"완성 문장에서 {ws.index(x) + 1 if x in ws else [w.lower() for w in ws].index(x.lower()) + 1}번째 단어이다. 오답이다.") for x in c]
    F(1, 87, t, st="R", p="<보기>\n" + "\n".join(lines) + "\n" + blanks, c=c, a=a, r=R87, k=f"완성 문장은 ‘{sent}’이고 여섯 번째 단어는 {sixth}이다.", n=n, s=s)
S87 = "원문항에 없던 우리말 뜻이 붙고 발문이 ‘관계절은 수식하는 명사 바로 뒤에’ 같은 배열 규칙을 알려 주었다. 발문을 원문항과 같게 하고 우리말을 뺐다. 대신 {}"
f87("B", ["the", "book", "that", "Mina", "bought", "is", "interesting"], "The book that Mina bought is interesting.", ["Mina", "bought", "is", "that", "interesting"],
    S87.format("시간 부사 yesterday를 빼서 위치 논란을 없앴다. ‘Mina bought the book that is interesting.’으로 배열해도 여섯 번째 단어가 is라 답이 하나다."))
f87("C", ["she", "met", "a", "boy", "whose", "sister", "is", "my", "friend"], "She met a boy whose sister is my friend.", ["whose", "is", "boy", "friend", "sister"],
    S87.format("우리말 없이도 한 가지로만 배열되도록 주격 대명사 she가 든 제시어로 바꿨다."))
f87("D", ["they", "thanked", "the", "man", "who", "found", "their", "dog"], "They thanked the man who found their dog.", ["who", "found", "man", "dog", "their"],
    S87.format("우리말 없이도 한 가지로만 배열되도록 주격 대명사 they가 든 제시어로 바꿨다."))
f87("E", ["he", "showed", "me", "the", "cafe", "where", "they", "met"], "He showed me the cafe where they met.", ["me", "cafe", "met", "where", "they"],
    S87.format("시간 부사 last year를 뺀 새 제시어로 바꿨다. he와 they의 자리를 바꿔 배열해도 여섯 번째 단어가 where라 답이 하나다."))
f87("F", ["the", "day", "when", "Tom", "arrived", "was", "rainy"], "The day when Tom arrived was rainy.", ["was", "rainy", "Tom", "when", "arrived"],
    S87.format("제시어만으로 한 가지로 배열되므로 우리말 없이 그대로 쓴다. 정답 위치 ①."))

# 1-88 밑줄 친 관계부사: 원문항처럼 the way how를 정답으로, 밑줄 복원, 오답을 유형마다 새로
R88 = "관계부사는 선행사에 맞춰 시간 when, 장소 where, 이유 why를 쓴다. 방법은 the way 또는 how 중 하나만 쓰며 the way how로 겹쳐 쓰지 않는다."
def ok88(k): return {"when": "시간 선행사 뒤에 when을 바르게 썼다. 오답이다.", "where": "장소 선행사 뒤에 where를 바르게 썼다. 오답이다.", "why": "이유 선행사 뒤에 why를 바르게 썼다. 오답이다."}[k]
BAD88 = "the way와 how는 함께 쓰지 않는다. the way 또는 how 하나만 써야 하므로 정답이다."
S88 = "원문항은 ‘the way how’를 쓸 수 없음을 묻는데 변형은 선행사와 관계부사의 뜻 불일치를 묻고 밑줄도 사라졌다. 원문항처럼 the way how 문장을 정답으로 하고 밑줄을 넣었으며, 옳은 문장 네 개를 유형마다 새로 썼다."
def f88(t, items, a):
    F(1, 88, t, st="R", c=[x for x, _ in items], a=a, r=R88, n=[(BAD88 if i + 1 == a else ok88(k)) for i, (_, k) in enumerate(items)], s=S88 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f88("B", [("The museum <u>where</u> we saw dinosaurs was huge.", "where"), ("Tell me the way <u>how</u> you solved this puzzle.", None), ("Monday is the day <u>when</u> I have piano lessons.", "when"),
          ("I know the reason <u>why</u> she smiled.", "why"), ("This is the village <u>where</u> my mom grew up.", "where")], 2)
f88("C", [("I miss the days <u>when</u> we played outside all day.", "when"), ("That is the reason <u>why</u> I called you.", "why"), ("Can you explain the way <u>how</u> this app works?", None),
          ("The shop <u>where</u> I bought this hat is closed.", "where"), ("Noon is the time <u>when</u> the store is busiest.", "when")], 3)
f88("D", [("This is the gym <u>where</u> I exercise.", "where"), ("Please tell me the reason <u>why</u> you cried.", "why"), ("Spring is the season <u>when</u> flowers bloom.", "when"),
          ("I like the way <u>how</u> she sings.", None), ("We visited the farm <u>where</u> cows are raised.", "where")], 4)
f88("E", [("The way <u>how</u> he spoke surprised everyone.", None), ("This is the pool <u>where</u> I learned to swim.", "where"), ("2020 was the year <u>when</u> I entered middle school.", "when"),
          ("Do you know the reason <u>why</u> the store closed?", "why"), ("The city <u>where</u> she lives is far away.", "where")], 1)
f88("F", [("I remember the night <u>when</u> it snowed a lot.", "when"), ("That is the house <u>where</u> the famous writer lived.", "where"), ("No one knew the reason <u>why</u> he quit.", "why"),
          ("This is the restaurant <u>where</u> we celebrated my birthday.", "where"), ("I don't understand the way <u>how</u> this machine works.", None)], 5)

# 1-89 관계대명사 + be동사 생략 용어: 그럴듯한 용어 오답을 유형마다 다르게, 밑줄 복원
R89 = "주격 관계대명사 + be동사 뒤에 분사가 오면 관계대명사와 be동사를 동시에 생략할 수 있고, 남은 분사(현재분사·과거분사)가 선행사를 직접 꾸민다."
UA, UB, UC = "(<u>      A      </u>)", "(<u>      B      </u>)", "(<u>      C      </u>)"
def f89(t, sent, rel, part, kind, ante, c, a):
    sent = re.sub(rf"\b({rel} (?:is|are|was|were) {part})\b", r"<u>\1</u>", sent); assert "<u>" in sent
    p = f"{sent}\n설명: 위 문장에서 '{rel}'는 주격 관계대명사이다. 주격 관계대명사가 {UA}와 함께 쓰일 때, 이 두 단어를 {UB} 생략할 수 있다. 생략 후에는 {UC}인 '{part}' 하나만 남아 선행사 '{ante}' 뒤에서 그 명사를 직접 수식하게 된다."
    need = ["관계대명사와 함께 생략되는 것은 be동사이다.", "관계대명사와 be동사는 동시에(한꺼번에) 생략한다.", f"남은 '{part}'는 {kind}이다."]
    F(1, 89, t, st="R", p=p, c=c, a=a, r=R89, n=tnotes(c, a, need, labs=["(A)", "(B)", "(C)"]),
      s="원문항 오답(일반동사/조동사, 각각/동시에, 동명사/과거분사)은 서로 헷갈리는 용어인데 변형 오답(전치사 - 명사 등)은 뻔히 틀렸고 B~F가 같았다. 발문과 설명 형식을 원문항과 같게 하고 밑줄 빈칸을 넣었으며, 비슷한 용어끼리 헷갈리는 오답을 유형마다 다르게 만들었다." + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f89("B", "The cars which are parked outside belong to Tom.", "which", "parked", "과거분사", "The cars",
    ["(A) 일반동사 - (B) 각각 - (C) 과거분사", "(A) be동사 - (B) 동시에 - (C) 과거분사", "(A) be동사 - (B) 각각 - (C) 현재분사", "(A) 조동사 - (B) 동시에 - (C) 동명사", "(A) be동사 - (B) 동시에 - (C) 현재분사"], 2)
f89("C", "The students who are waiting outside are from Class 1.", "who", "waiting", "현재분사", "The students",
    ["(A) be동사 - (B) 동시에 - (C) 현재분사", "(A) be동사 - (B) 각각 - (C) 동명사", "(A) 일반동사 - (B) 동시에 - (C) 현재분사", "(A) be동사 - (B) 동시에 - (C) 과거분사", "(A) 조동사 - (B) 각각 - (C) 현재분사"], 1)
f89("D", "The documents which were signed yesterday are ready.", "which", "signed", "과거분사", "The documents",
    ["(A) 조동사 - (B) 동시에 - (C) 과거분사", "(A) be동사 - (B) 각각 - (C) 과거분사", "(A) be동사 - (B) 동시에 - (C) 동명사", "(A) be동사 - (B) 동시에 - (C) 과거분사", "(A) 일반동사 - (B) 각각 - (C) 현재분사"], 4)
f89("E", "The man who is standing by the door is my uncle.", "who", "standing", "현재분사", "The man",
    ["(A) 일반동사 - (B) 동시에 - (C) 동명사", "(A) be동사 - (B) 각각 - (C) 현재분사", "(A) 조동사 - (B) 동시에 - (C) 현재분사", "(A) be동사 - (B) 동시에 - (C) 과거분사", "(A) be동사 - (B) 동시에 - (C) 현재분사"], 5)
f89("F", "The girl who is wearing a red coat is Mina.", "who", "wearing", "현재분사", "The girl",
    ["(A) be동사 - (B) 동시에 - (C) 동명사", "(A) 일반동사 - (B) 각각 - (C) 현재분사", "(A) be동사 - (B) 동시에 - (C) 현재분사", "(A) be동사 - (B) 각각 - (C) 과거분사", "(A) 조동사 - (B) 동시에 - (C) 현재분사"], 3)


# ---- 2차 감수(2026-10) 추가 ----
# 1-82 B: 같은 문장이 틀린 형태(①)와 옳은 형태(⑤)로 함께 나옴
f82("B", [("The laptop, that I bought last month, has already broken.", "쉼표 뒤 계속적 용법에는 that을 쓸 수 없다. which로 고쳐야 한다."), ("Mina showed me the thing that she found.", "선행사 the thing 뒤에 목적격 관계대명사 that을 썼다."),
          ("Tom met Jane, who lives next door.", "쉼표 뒤 계속적 용법에 who를 썼다."), ("We cannot accept what he said.", "선행사를 포함한 what이 accept의 목적어절을 이끈다."),
          ("What she cooked for us was delicious.", "선행사를 포함한 what이 주어절을 이끈다.")], 1)
FIX[(1, 82, "B")]["s"] = "① ‘The laptop, that I bought last month, …’와 ⑤ ‘The laptop, which I bought last month, …’가 같은 문장의 틀린 형태·옳은 형태로 함께 나와 대비만으로 답이 드러났다. ⑤를 다른 옳은 문장으로 바꿨다. 정답은 그대로 ①."
