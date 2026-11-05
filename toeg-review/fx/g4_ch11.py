# 4급 CH11 문장의 형식·문장 성분 (101~110) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def talk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 옳지 않은 설명이다. 따라서 정답이다." if i + 1 == a else " 옳은 설명이다. 따라서 오답이다.")) if w.endswith("므로") else (w + (" 옳지 않은 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.")) for i, (_, w) in enumerate(items)], k=items[a-1][1], s=s + ipos(a), **kw)

# 4-101 목적어 찾기: 원문항 형식(문장 속 성분에 ①~⑤ 밑줄)
R4101 = "목적어는 동사의 동작 대상(~을/를)이 되는 명사구 전체이다. 주어, 동사, 시간·장소·방법을 나타내는 부사어와 구별한다."
S4101 = "원문항은 문장 속 밑줄 ①~⑤ 위치를 고르는데, 변형은 문장을 따로 주고 성분을 뒤섞어 선택지로 나열했다. 원문항처럼 문장 속 성분에 ①~⑤ 밑줄 번호를 붙였다."
def f4101(t, chunks, roles, a, s=S4101, tail="."):
    p = " ".join(f"{'①②③④⑤'[i]}<u>{c}</u>" for i, c in enumerate(chunks)) + tail
    mk(4, 101, t, [(c, r) for c, r in zip(chunks, roles)], a, R4101, s, st="R", p=p, okdup=True)
SUBJ = "문장의 주어이므로"; VERB = "문장의 동사이므로"; ADV = "시간·장소·방법을 나타내는 부사어이므로"
def OBJ(v): return f"동사 {v}의 대상(~을/를)이 되는 목적어이므로"
f4101("B", ["Every day", "Jane", "reads", "English books", "at home"], [ADV, SUBJ, VERB, OBJ("reads"), ADV], 4)
f4101("C", ["My brother", "cleaned", "his messy room", "with Dad", "last Sunday"], [SUBJ, VERB, OBJ("cleaned"), ADV, ADV], 3,
      "문장과 정답(some fresh bread and milk)이 원문항과 거의 같았고 형식도 원본과 달랐다. 문장을 새로 쓰고 원문항처럼 문장 속 성분에 밑줄 번호를 붙였다.")
f4101("D", ["Yesterday", "at the park", "Tom", "found", "a small puppy"], [ADV, ADV, SUBJ, VERB, OBJ("found")], 5, S4101 + " 목적어의 위치가 다른 유형과 겹치지 않게 부사어를 앞에 둔 문장으로 바꿨다.")
f4101("E", ["We", "visited", "our uncle", "in Seoul", "last week"], [SUBJ, VERB, OBJ("visited"), ADV, ADV], 3)
f4101("F", ["After school", "my sister and I", "always", "play", "badminton"], [ADV, SUBJ, "빈도를 나타내는 부사이므로", VERB, OBJ("play")], 5, S4101 + " 문장도 새로 써서 목적어가 맨 끝에 오게 했다.")

# 4-102 연결동사 뒤 보어로 알맞지 않은 것: 원문항 발문, 제시 문장을 새로, -ly 형용사 함정 포함
R4102 = "look, sound, seem, feel 같은 연결동사 뒤 보어 자리에는 형용사를 쓴다. lovely, friendly, lonely, silly처럼 -ly로 끝나는 형용사도 보어로 쓸 수 있지만, quickly·carefully 같은 부사는 쓸 수 없다."
S4102 = "제시 문장(Jerry looks ____)이 원문항과 같았고 발문이 ‘형용사 보어로 알맞지 않은 것’이라고 기준을 알려 주었으며, 오답이 유형마다 같고 원문항의 -ly 형용사 함정(lovely)이 없었다. 원문항 발문으로 되돌리고 제시 문장을 새로 썼으며 -ly 형용사를 오답에 넣었다."
LYADJ = "-ly로 끝나지만 형용사라 보어 자리에 쓸 수 있으므로"; ADJ = "형용사라 보어 자리에 쓸 수 있으므로"; ADVB = "부사라 보어 자리에 쓸 수 없으므로"
def f4102(t, p, items, a, s=S4102):
    mk(4, 102, t, items, a, R4102, s, st="R", p=p, okdup=True)
f4102("C", "The girl looks _______.", [("lonely", LYADJ), ("friendly", LYADJ), ("quickly", ADVB), ("lovely", LYADJ), ("happy", ADJ)], 3)
f4102("D", "Your idea sounds _______.", [("great", ADJ), ("silly", LYADJ), ("interesting", ADJ), ("strangely", ADVB), ("lovely", LYADJ)], 4)
f4102("E", "The old man seems _______.", [("friendly", LYADJ), ("lonely", LYADJ), ("tired", ADJ), ("kind", ADJ), ("carefully", ADVB)], 5)
f4102("F", "This blanket feels _______.", [("softly", ADVB), ("warm", ADJ), ("lovely", LYADJ), ("nice", ADJ), ("heavy", ADJ)], 1)

# 4-103 주어진 문장과 같은 형식: 제시 문장과 오답을 유형마다 새로
R4103 = "1형식은 주어 + 자동사(+ 부사어), 2형식은 주어 + 동사 + 보어, 3형식은 주어 + 동사 + 목적어, 4형식은 주어 + 동사 + 간접목적어 + 직접목적어, 5형식은 주어 + 동사 + 목적어 + 목적격보어이다. 부사어는 형식에 넣지 않는다."
S4103 = "제시 문장(They laughed loudly.)이 원문항과 같았고 오답 네 문장이 유형마다 같았다. 제시 문장과 오답을 유형마다 새로 썼다."
F1 = "주어 + 자동사(+ 부사어)의 1형식이라 주어진 문장과 같으므로"; F2 = "주어 + 동사 + 보어의 2형식이라 주어진 문장과 다르므로"; F3 = "주어 + 동사 + 목적어의 3형식이라 주어진 문장과 다르므로"
F4 = "주어 + 동사 + 간접목적어 + 직접목적어의 4형식이라 주어진 문장과 다르므로"; F5 = "주어 + 동사 + 목적어 + 목적격보어의 5형식이라 주어진 문장과 다르므로"
def f4103(t, p, items, a, s=S4103):
    mk(4, 103, t, items, a, R4103, s, p=p)
f4103("C", "The baby smiled happily.", [("My sister became a nurse.", F2), ("He sent me a letter.", F4), ("The leaves fell slowly.", F1), ("We painted the wall.", F3), ("The movie was boring.", F2)], 3)
f4103("D", "The sun rises in the east.", [("She made us happy.", F5), ("I know the answer.", F3), ("The milk went bad.", F2), ("He told me a secret.", F4), ("Birds fly in the sky.", F1)], 5)
f4103("E", "The children ran quickly.", [("The rain stopped at noon.", F1), ("The room smells nice.", F2), ("We found the key.", F3), ("Mom bought me a bag.", F4), ("They call him Max.", F5)], 1,
      "정답(Tom laughed loudly.)이 제시 문장과 주어만 달라 형식을 몰라도 고를 수 있었고 오답도 C와 같았다. 제시 문장과 정답을 다른 1형식 문장으로 새로 쓰고 오답도 새로 썼다.")
f4103("F", "A strange thing happened yesterday.", [("The flowers look beautiful.", F2), ("The bus came late.", F1), ("Tom wrote a letter.", F3), ("Jane showed us her photos.", F4), ("The news made me sad.", F5)], 2)

# 4-104 [ ] 표시를 밑줄로
S4104 = "원문항의 밑줄이 [ ] 표시로 바뀌고 발문도 달라졌다. 원문항 발문과 밑줄로 되돌렸다. 보기와 정답은 그대로다."
for t in "BDF":
    F(4, 104, t, st="R", c=[re.sub(r"\[(.+?)\]", r"<u>\1</u>", x) for x in V(4, 104, t)["c"]], keepx=True, s=S4104)
R4104 = "타동사 뒤에서 동작의 대상이 되는 목적어와, 연결동사(look, seem, become, taste) 뒤에서 주어의 상태를 설명하는 형용사 주격보어를 구별한다."
def C4104(adj, v): return f"{adj}: 연결동사 {v} 뒤에서 주어의 상태를 설명하는 주격보어이므로"
mk(4, 104, "C", [("Jane seems <u>kind</u>.", C4104("kind", "seems")), ("Tom reads <u>books</u>.", "books: reads의 대상인 목적어라 나머지(주격보어)와 역할이 달라"), ("The child looks <u>sleepy</u>.", C4104("sleepy", "looks")),
                 ("The lake became <u>calm</u>.", C4104("calm", "became")), ("The soup tastes <u>good</u>.", C4104("good", "tastes"))], 2, R4104,
   S4104.replace(" 보기와 정답은 그대로다.", "") + " 다른 유형과 같던 문장(The sky became dark.)은 바꿨다.", st="R")
mk(4, 104, "E", [("The baby looks <u>sleepy</u>.", C4104("sleepy", "looks")), ("The road became <u>icy</u>.", C4104("icy", "became")), ("Jane opened <u>the window</u>.", "the window: opened의 대상인 목적어라 나머지(주격보어)와 역할이 달라"),
                 ("Tom seems <u>busy</u>.", C4104("busy", "seems")), ("The soup tastes <u>delicious</u>.", C4104("delicious", "tastes"))], 3, R4104,
   S4104.replace(" 보기와 정답은 그대로다.", "") + " 다른 유형과 같던 문장(The sky became dark.)은 바꿨다.", st="R")

# 4-105 구조 설명이 어색한 것: 원문항처럼 여러 구조의 설명, 문체 통일, 유형마다 새로
R4105 = "be동사·become 뒤의 보어, 감각동사(look, smell, taste, sound, feel) 뒤의 형용사 보어, 타동사 뒤의 목적어, be + -ing 진행형, 자동사 뒤 부사를 구별한다. 감각동사 뒤에는 부사가 아니라 형용사를 쓴다."
S4105 = "옳은 설명 네 개가 유형마다 같았고 틀린 설명만 문체가 달라 눈에 띄었으며, 원문항의 다양한 구조 설명이 감각동사 하나로 좁아졌다. 원문항 발문으로 되돌리고 원문항처럼 여러 구조에 대한 설명을 같은 문체로 유형마다 새로 썼다."
def f4105(t, items, a, s=S4105):
    talk(4, 105, t, items, a, R4105, s, st="R")
f4105("B", [("The soup tastes nice. - 감각을 나타내는 동사 뒤에 형용사가 쓰였다.", "taste 뒤에 형용사 보어 nice가 쓰였으므로"), ("Mina became a nurse. - 주어를 보충 설명하는 보어가 있는 문장이다.", "a nurse가 주어 Mina를 보충 설명하므로"),
            ("They are playing soccer. - 지금 진행 중인 동작을 나타내는 문장이다.", "be + -ing의 현재진행형이므로"), ("The flower smells beautifully. - 부사 beautifully가 동사 smells를 바르게 수식하고 있다.", "감각동사 smell 뒤에는 형용사 beautiful을 써야 하므로"),
            ("The baby slept well. - 동사가 목적어를 필요로 하지 않는 문장이다.", "slept는 목적어 없이 쓰는 자동사이므로")], 4)
f4105("C", [("Tom bought a new bike. - 동사 뒤에 목적어가 있는 문장이다.", "a new bike가 bought의 목적어이므로"), ("The music sounds great. - 동사 뒤에 주어를 설명하는 형용사가 쓰였다.", "sound 뒤에 형용사 보어 great가 쓰였으므로"),
            ("I am reading a book. - 현재 진행 중인 동작을 나타내는 문장이다.", "be + -ing의 현재진행형이므로"), ("My uncle is a pilot. - 주어를 보충 설명하는 보어가 있는 문장이다.", "a pilot이 주어를 보충 설명하므로"),
            ("The cake looks deliciously. - 부사 deliciously가 동사 looks를 바르게 수식하고 있다.", "look 뒤 보어 자리에는 형용사 delicious를 써야 하므로")], 5, S4105 + " 정답 문장(The pizza smells so well.)이 원문항과 같아 새로 썼다.")
f4105("D", [("The bread smells nicely. - 부사 nicely가 동사 smells를 바르게 수식하고 있다.", "smell 뒤 보어 자리에는 형용사 nice를 써야 하므로"), ("Jane feels tired. - 주어의 상태를 설명하는 형용사 보어가 있다.", "feel 뒤에 형용사 보어 tired가 쓰였으므로"),
            ("We watched a movie. - 동사가 목적어를 필요로 하는 문장이다.", "a movie가 watched의 목적어이므로"), ("The train arrived late. - 동사가 목적어를 필요로 하지 않는 문장이다.", "arrived는 목적어 없이 쓰는 자동사이므로"),
            ("She was cooking dinner. - 과거에 진행 중이던 동작을 나타내는 문장이다.", "was + -ing의 과거진행형이므로")], 1)
f4105("E", [("He is a famous singer. - 주어를 보충 설명하는 보어가 있는 문장이다.", "a famous singer가 주어를 보충 설명하므로"), ("The kids are running fast. - 부사 fast가 동사 running을 수식하고 있다.", "fast가 running을 꾸미는 부사이므로"),
            ("Your voice sounds strangely. - 감각을 나타내는 동사 뒤에 부사가 와서 옳은 문장이다.", "sound 뒤 보어 자리에는 형용사 strange를 써야 하므로"), ("I like my new school. - 동사 뒤에 목적어가 있는 문장이다.", "my new school이 like의 목적어이므로"),
            ("The weather got cold. - 동사 뒤에 주어의 상태를 설명하는 형용사가 쓰였다.", "got 뒤에 형용사 보어 cold가 쓰였으므로")], 3,
     "발문에 ‘모든 감각·연결동사를 2형식으로 해석할 때’ 조건이 붙었고 오답도 다른 유형과 같았다. 원문항 발문으로 되돌리고 " + S4105[S4105.index("원문항처럼"):])
f4105("F", [("The lemon tastes sour. - 감각을 나타내는 동사 뒤에 형용사가 쓰였다.", "taste 뒤에 형용사 보어 sour가 쓰였으므로"), ("Tom seems quietly. - 부사 quietly가 동사 seems를 바르게 수식하고 있다.", "seem 뒤 보어 자리에는 형용사 quiet를 써야 하므로"),
            ("We are having lunch. - 지금 진행 중인 동작을 나타내는 문장이다.", "be + -ing의 현재진행형이므로"), ("My dog barked loudly. - 동사가 목적어를 필요로 하지 않는 문장이다.", "barked는 목적어 없이 쓰는 자동사이므로"),
            ("Jane has two cats. - 동사 뒤에 목적어가 있는 문장이다.", "two cats가 has의 목적어이므로")], 2)

# 4-106 C: 원문항과 같던 제시문을 새로
mk(4, 106, "C", [("My mom", "문장의 주어이므로"), ("pancakes", "동사 makes의 대상(~을)이 되는 목적어이므로"), ("makes", "문장의 동사이므로"), ("every Sunday", "시간을 나타내는 부사어이므로"), ("Sunday", "부사어 every Sunday의 일부이므로")], 2,
   "목적어는 동사의 동작 대상(~을/를)이 되는 명사구이다. 주어, 동사, 시간·장소 부사어와 구별한다.", "제시문과 정답(milk)이 원문항과 똑같았다. 제시문을 ‘My mom makes pancakes every Sunday.’로 바꾸고, 정답 위치도 원문항(⑤)과 겹치지 않게 했다.",
   p="My mom makes pancakes every Sunday.", okdup=True)

# 4-107 형식에 영향을 주지 않는 단어: 원문항 발문, C는 문장을 새로
S4107 = "발문에 ‘학교문법의 5형식 분류에 포함되는 주어·동사·목적어·목적격보어가 아닌 부사어’라고 정답의 성분을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
for t in "EF": F(4, 107, t, st="R", s=S4107)
mk(4, 107, "C", [("Happily", "문장 전체를 꾸미는 부사라 형식에 영향을 주지 않으므로"), ("my sister", "문장의 주어이므로"), ("kept", "문장의 동사이므로"), ("her room", "kept의 목적어이므로"), ("clean", "목적어 her room의 상태를 설명하는 목적격보어이므로")], 1,
   "주어 + 동사 + 목적어 + 목적격보어는 5형식이며, 부사(어)는 문장의 형식을 정하는 성분에 넣지 않는다.",
   "발문이 정답의 성분을 알려 주었고 문장 구조와 정답(beautifully)도 원문항과 같았다. 원문항 발문으로 되돌리고 문장을 ‘Happily, my sister kept her room clean.’으로 새로 썼다.",
   st="R", p="Happily, my sister kept her room clean.", okdup=True)

# 4-108 밑줄 친 형용사·부사의 쓰임: 원문항 발문과 밑줄, 동작동사 + 부사 문장 포함
ST4108 = "다음 중 밑줄 친 부분의 쓰임이 어법상 옳은 것을 고르시오."
R4108 = "감각·연결동사(look, smell, taste, feel, seem, sound, become) 뒤 보어 자리에는 형용사를, 동작을 꾸미는 자리(runs, sings, drives, speaks)에는 부사를 쓴다."
S4108 = "발문이 ‘2형식 연결동사로 해석할 때 형용사 보어를 바르게 사용한’이라고 기준을 알려 주었고 밑줄이 사라졌으며, 짝 문장과 같은 오답이 유형마다 반복되었다. 원문항 발문과 밑줄로 되돌리고, 원문항처럼 동작을 꾸미는 부사 자리의 문장도 섞어 유형마다 새로 썼다."
LV = "감각·연결동사 뒤 보어 자리에는 형용사를 써야 하므로"; AV = "동작을 꾸미는 자리에는 부사를 써야 하므로"
def f4108(t, items, a, s=S4108):
    mk(4, 108, t, items, a, R4108, s, st=ST4108)
f4108("B", [("The flower smells <u>sweetly</u>.", LV), ("Jane speaks <u>quiet</u>.", AV), ("Tom seems <u>tiredly</u>.", LV), ("The sky became <u>dark</u>.", "become 뒤 보어 자리에 형용사를 바르게 썼으므로"), ("This soup tastes <u>well</u>.", LV)], 4)
f4108("C", [("The baby looks <u>sleepily</u>.", LV), ("The girl sings <u>beautifully</u>.", "동사 sings를 꾸미는 부사를 바르게 썼으므로"), ("He drives <u>careful</u>.", AV), ("The music sounds <u>loudly</u>.", LV), ("The bread smells <u>freshly</u>.", LV)], 2,
      S4108 + " 정답(This soup tastes good.)이 원문항과 같아 새로 썼다.")
f4108("D", [("Jane looks <u>happy</u>.", "look 뒤 보어 자리에 형용사를 바르게 썼으므로"), ("She dances <u>good</u>.", AV), ("The milk tastes <u>sourly</u>.", LV), ("The room feels <u>warmly</u>.", LV), ("Tom runs <u>quick</u>.", AV)], 1)
f4108("E", [("The cake smells <u>deliciously</u>.", LV), ("He speaks English <u>fluent</u>.", AV), ("The water feels <u>coldly</u>.", LV), ("You look <u>sadly</u> today.", LV), ("The roses smell <u>sweet</u>.", "smell 뒤 보어 자리에 형용사를 바르게 썼으므로")], 5)
f4108("F", [("The kids played <u>happy</u>.", AV), ("Mina sounds <u>excitedly</u>.", LV), ("Tom seems <u>tired</u>.", "seem 뒤 보어 자리에 형용사를 바르게 썼으므로"), ("The teacher talks <u>slow</u>.", AV), ("The soup tastes <u>saltily</u>.", LV)], 3)

# 4-109 1형식 문장으로만 짝: 원문항 형식((가)~(라) 네 문장, 두 개의 짝)
ST4109 = "다음 <보기>의 문장 중 1형식 문장으로만 짝지어진 것은?"
R4109 = "1형식은 주어 + 자동사(+ 부사어)이다. There is/are 문장도 1형식이다. 보어가 있으면 2형식, 목적어가 있으면 3형식이다."
S4109 = "원문항은 네 문장 중 1형식 두 개의 짝을 고르는데, 변형은 다섯 문장 중 ‘빠짐없이 모두’ 고르는 형식으로 바뀌었고 정답이 유형마다 같았다. 원문항 발문과 형식(<보기> (가)~(라) 네 문장, 두 개의 짝)으로 되돌리고 유형마다 정답 조합을 달리했다."
REF109 = ["(가), (나)", "(나), (다)", "(다), (라)", "(가), (다)", "(나), (라)"]
def f4109(t, lines, judge, ok, c=REF109, s=S4109):
    a = c.index(ok) + 1
    F(4, 109, t, st=ST4109, p="<보기>\n" + "\n".join(lines), c=c, a=a, r=R4109, pre=["문장별 판정: " + j for j in judge], k=f"1형식 문장은 {ok}이다.", n=setnotes(c, ok, "1형식 문장"), okdup=True, s=s + ipos(a))
f4109("B", ["(가) Tom laughed.", "(나) The soup tastes good.", "(다) We went home.", "(라) Jane reads books."],
      ["(가) 1형식. 주어 + 자동사이다.", "(나) 2형식. good이 주어를 설명하는 보어이다.", "(다) 1형식. home은 부사어이다.", "(라) 3형식. books가 목적어이다."], "(가), (다)")
f4109("C", ["(가) There is a bank near my house.", "(나) Jane is happy.", "(다) Tom likes music.", "(라) Birds fly high."],
      ["(가) 1형식. There is 문장이다.", "(나) 2형식. happy가 보어이다.", "(다) 3형식. music이 목적어이다.", "(라) 1형식. high는 부사어이다."], "(가), (라)",
      ["(가), (나)", "(나), (다)", "(가), (라)", "(가), (다)", "(나), (라)"], S4109 + " (가)(나)가 원문항 문장과 같아 새로 썼다.")
f4109("D", ["(가) Jane became angry.", "(나) The baby sleeps.", "(다) I bought a book.", "(라) The train arrived."],
      ["(가) 2형식. angry가 보어이다.", "(나) 1형식. 주어 + 자동사이다.", "(다) 3형식. a book이 목적어이다.", "(라) 1형식. 주어 + 자동사이다."], "(나), (라)")
f4109("E", ["(가) Tom is tall.", "(나) The dog ran fast.", "(다) There is a cat outside.", "(라) We need help."],
      ["(가) 2형식. tall이 보어이다.", "(나) 1형식. fast는 부사어이다.", "(다) 1형식. There is 문장이다.", "(라) 3형식. help가 목적어이다."], "(나), (다)")
f4109("F", ["(가) Jane looks tired.", "(나) Tom bought a bag.", "(다) The train stopped.", "(라) The baby cried."],
      ["(가) 2형식. tired가 보어이다.", "(나) 3형식. a bag이 목적어이다.", "(다) 1형식. 주어 + 자동사이다.", "(라) 1형식. 주어 + 자동사이다."], "(다), (라)")

# 4-110 형식이 바르게 짝지어진 것: 원문항 형식(<보기> 줄바꿈, 세 개 조합, 틀린 짝 두 개)
ST4110 = "다음 <보기> 중 문장의 형식이 올바르게 짝지어진 것만 고른 것은?"
R4110 = "1형식은 주어 + 동사, 2형식은 주어 + 동사 + 보어(명사·형용사), 3형식은 주어 + 동사 + 목적어이다. 감각동사 뒤 형용사와 be동사 뒤 명사는 보어이다."
S4110 = "원문항은 다섯 항목 중 옳게 짝지은 세 개를 고르는데, 변형은 ‘빠짐없이 모두’ 고르는 형식으로 바뀌었고 일부 유형은 틀린 짝이 하나도 없었다. 원문항 발문과 형식(<보기> 줄바꿈, 세 개 조합)으로 되돌리고 틀린 짝 두 개를 넣었다."
REF110 = ["(A), (B), (C)", "(A), (B), (D)", "(B), (C), (E)", "(A), (C), (D)", "(C), (D), (E)"]
def f4110(t, lines, judge, ok, c=REF110, s=S4110):
    a = c.index(ok) + 1
    F(4, 110, t, st=ST4110, p="<보기>\n" + "\n".join(lines), c=c, a=a, r=R4110, pre=["항목별 판정: " + j for j in judge], k=f"형식이 올바르게 짝지어진 것은 {ok}이다.", n=setnotes(c, ok, "올바른 짝"), okdup=True, s=s + ipos(a))
f4110("B", ["(A) Birds sing. (1형식)", "(B) This soup smells nice. (1형식)", "(C) We visited Seoul. (3형식)", "(D) Tom looks busy. (2형식)", "(E) Jane has a bike. (2형식)"],
      ["(A) O. 주어 + 동사의 1형식이다.", "(B) X. nice가 보어인 2형식이다.", "(C) O. Seoul이 목적어인 3형식이다.", "(D) O. busy가 보어인 2형식이다.", "(E) X. a bike가 목적어인 3형식이다."], "(A), (C), (D)")
f4110("C", ["(A) My dad is a cook. (3형식)", "(B) The girl smiled. (1형식)", "(C) Tom likes music. (3형식)", "(D) She looks tired. (3형식)", "(E) The leaves turned red. (2형식)"],
      ["(A) X. a cook이 보어인 2형식이다.", "(B) O. 주어 + 동사의 1형식이다.", "(C) O. music이 목적어인 3형식이다.", "(D) X. tired가 보어인 2형식이다.", "(E) O. red가 보어인 2형식이다."], "(B), (C), (E)",
      s=S4110 + " (A)~(C)가 원문항 항목과 같고 정답 조합도 같아 항목을 새로 썼다.")
f4110("D", ["(A) Birds fly. (1형식)", "(B) The soup tastes good. (2형식)", "(C) Jane reads books. (2형식)", "(D) Tom became angry. (2형식)", "(E) We arrived home. (3형식)"],
      ["(A) O. 주어 + 동사의 1형식이다.", "(B) O. good이 보어인 2형식이다.", "(C) X. books가 목적어인 3형식이다.", "(D) O. angry가 보어인 2형식이다.", "(E) X. home은 부사어라 1형식이다."], "(A), (B), (D)")
f4110("E", ["(A) The bus arrived. (2형식)", "(B) Jane is happy. (1형식)", "(C) Tom bought a car. (3형식)", "(D) The dog seems tired. (2형식)", "(E) We need help. (3형식)"],
      ["(A) X. 주어 + 동사의 1형식이다.", "(B) X. happy가 보어인 2형식이다.", "(C) O. a car가 목적어인 3형식이다.", "(D) O. tired가 보어인 2형식이다.", "(E) O. help가 목적어인 3형식이다."], "(C), (D), (E)")
f4110("F", ["(A) The baby cried. (2형식)", "(B) The sky became dark. (2형식)", "(C) I like apples. (1형식)", "(D) Tom is a student. (2형식)", "(E) Jane saw him. (3형식)"],
      ["(A) X. 주어 + 동사의 1형식이다.", "(B) O. dark가 보어인 2형식이다.", "(C) X. apples가 목적어인 3형식이다.", "(D) O. a student가 보어인 2형식이다.", "(E) O. him이 목적어인 3형식이다."], "(B), (D), (E)",
      ["(B), (D), (E)", "(A), (B), (D)", "(B), (C), (E)", "(A), (C), (D)", "(C), (D), (E)"])
