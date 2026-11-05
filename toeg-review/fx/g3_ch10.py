# 3급 CH10 형용사·부사 (91~100) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]

# 3-91 형용사 위치: 원문항처럼 문장 속 단어 앞 번호 위치 선택형
R91 = "형용사는 보통 꾸미는 명사 바로 앞에 오지만, something·someone처럼 -thing·-one으로 끝나는 대명사는 형용사가 뒤에서 꾸민다."
S91 = "원문항은 문장 속 위치(①I ②have ③a ④problem ⑤to solve)를 고르는데, 변형은 단어를 뒤섞어 나열하고 ‘바로 앞에 넣어야 할 단어’를 고르게 해 형식이 바뀌었다. 원문항 발문과 위치 선택형으로 되돌렸다."
def f91(t, adj_st, ko, words, a, why_ok, s=S91):
    mk(3, 91, t, [(w, why_ok if i + 1 == a else f"{w} 앞 자리는 형용사가 꾸밀 말과 맞지 않는 위치이므로") for i, w in enumerate(words)], a, R91, s, st=f"다음 중 {adj_st} 들어갈 위치를 고르시오.", p=ko, okdup=True)
f91("B", "warm이", "나에게 먹을 따뜻한 것을 좀 줘.", ["Please", "give", "me", "something", "to eat."], 5, "-thing 대명사 something은 형용사가 뒤에서 꾸미므로 something 바로 뒤(to eat 앞)에 와야 하므로",
    "우리말·문장·정답(problem 앞)이 원문항과 같았고 형식도 바뀌었다. 원문항처럼 문장 속 위치 선택형으로 새로 쓰고, -thing 대명사 뒤에 오는 형용사를 묻게 했다.")
f91("C", "interesting이", "여기 읽을 재미있는 책이 한 권 있다.", ["Here", "is", "a", "book", "to read."], 4, "형용사는 꾸미는 명사 book 바로 앞에 오므로")
f91("D", "pretty가", "그녀는 파티에 입을 예쁜 드레스들이 있다.", ["She", "has", "dresses", "to wear", "for the party."], 3, "형용사는 꾸미는 명사 dresses 바로 앞에 오므로")
f91("E", "important가", "Tom은 오늘 해야 할 중요한 무언가가 있다.", ["Tom", "has", "something", "to do", "today."], 4, "-thing 대명사 something은 형용사가 뒤에서 꾸미므로 something 바로 뒤(to do 앞)에 와야 하므로")
f91("F", "beautiful이", "정원에 아름다운 꽃 몇 송이가 있다.", ["Some", "flowers", "are", "in", "the garden."], 2, "형용사는 꾸미는 명사 flowers 바로 앞에 오므로")

# 3-92 빈도부사 위치: 원문항 발문과 문장 속 번호 위치 선택형
R92 = "빈도부사(always, usually, often, never, rarely)는 일반동사 앞, be동사와 조동사 뒤에 두는 것이 기본이다."
S92 = "발문이 ‘usually를 be동사와 형용사 사이에 두는 기본 위치’라고 정답을 알려 주고, 선택지도 위치 번호 대신 ‘be동사 is 뒤’ 같은 설명으로 바뀌었다. 원문항 발문과 문장 속 번호 위치 선택형으로 되돌리고, 유형마다 빈도부사와 동사 종류를 바꿨다(usually처럼 문장 맨 앞에도 올 수 있는 부사는 피했다)."
def f92(t, adv, ko, chunks, a, why_ok, s=S92):
    p = ko + "\n" + " ".join(f"{'①②③④⑤'[i]} {c}" for i, c in enumerate(chunks))
    words = [c.split()[0] for c in chunks]
    mk(3, 92, t, [(w, why_ok if i + 1 == a else "빈도부사의 기본 위치(일반동사 앞, be동사·조동사 뒤)가 아니므로") for i, w in enumerate(words)], a, R92, s, st=f"다음 문장에서 {adv} 들어갈 위치를 고르시오.", p=p, okdup=True)
f92("B", "always가", "내 남동생과 여동생은 항상 걸어서 학교에 간다.", ["My", "younger brother", "and", "sister", "walk to school."], 5, "빈도부사 always는 일반동사 walk 앞에 오므로",
    "발문이 정답 위치를 알려 주고 선택지도 위치 설명으로 바뀌었다. 원문항 발문과 문장 속 번호 위치 선택형으로 새로 썼다.")
f92("C", "never가", "Tom은 일이 끝난 뒤에 결코 피곤해하지 않는다.", ["Tom", "is", "tired", "after", "work."], 3, "빈도부사 never는 be동사 is 뒤, 형용사 tired 앞에 오므로")
f92("D", "always가", "나와 내 남동생은 항상 방과 후에 축구를 한다.", ["My brother", "and", "I", "play", "soccer after school."], 4, "빈도부사 always는 일반동사 play 앞에 오므로")
f92("E", "never가", "우리는 주말에 절대 일찍 일어나지 않는다.", ["We", "get", "up", "early", "on weekends."], 2, "빈도부사 never는 일반동사 get 앞에 오므로")
f92("F", "rarely가", "그 식당은 월요일에는 좀처럼 붐비지 않는다.", ["The restaurant", "is", "crowded", "on", "Mondays."], 3, "빈도부사 rarely는 be동사 is 뒤, 형용사 crowded 앞에 오므로")

# 3-93 보어 자리 형용사: 원문항 발문, B는 문장을 새로
ST93 = "다음 빈칸에 들어갈 단어들을 알맞게 짝지은 것을 고르시오."
R93 = "look, smell, taste, feel, sound, become 뒤의 주격보어와 find, make 뒤의 목적격보어는 주어나 목적어의 상태를 설명하므로 부사가 아니라 형용사를 쓴다."
S93 = "발문이 ‘주어 또는 목적어의 성질을 설명하는 형용사 원급을 넣을 때’라고 정답을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
mk(3, 93, "B", [("happily - softly", "보어 자리에 부사 happily, softly를 쓸 수 없으므로"), ("happy - soft", "목적격보어 happy와 주격보어 soft로 형용사를 바르게 썼으므로"), ("happy - softly", "feel 뒤 보어 자리에 부사 softly를 쓸 수 없으므로"),
                ("happily - soft", "make의 목적격보어 자리에 부사 happily를 쓸 수 없으므로"), ("happiness - softly", "‘나를 행복하게’는 명사가 아니라 형용사로 나타내고, 보어 자리에 부사 softly를 쓸 수 없으므로")], 2, R93,
   "제시문과 정답이 원문항과 똑같았고 발문도 정답을 알려 주었다. 문장을 새로 쓰고 원문항 발문으로 되돌렸다.", st=ST93, p="The news made me _____.\nThis blanket feels _____.", okdup=True)
for t in "CDEF":
    ex = V(3, 93, t)["expl"]
    F(3, 93, t, st=ST93, xr=[x for x in [("형용사 원급을 넣을 때 ", ""), ("형용사 원급", "형용사")] if x[0] in ex], s=S93)

# 3-94 few/a few/little/a little: 유형마다 정답 조합을 새로, 오답도 원문항처럼 네 표현의 혼동
R94 = "a few·few는 셀 수 있는 명사의 복수형, a little·little은 셀 수 없는 명사에 쓴다. a few·a little은 ‘조금 있는’(긍정), few·little은 ‘거의 없는’(부정)이다."
S94 = "오답 조합 네 개(much - many, a little - few 등)가 유형마다 같았고, 원문항 오답(a few/few/a little/little의 혼동)과 성격이 달랐다. 유형마다 정답 조합을 원문항(a few - little)과 다르게 새로 쓰고, 오답도 원문항처럼 네 표현의 혼동으로 짰다."
KIND = {"a few": ("C", 1), "few": ("C", 0), "a little": ("U", 1), "little": ("U", 0)}
def n94(ch, good, nouns):
    xs = [x.strip() for x in re.split(r" [-–] ", ch)]; gs = [x.strip() for x in re.split(r" [-–] ", good)]
    if xs == gs: return "두 빈칸 모두 명사의 종류(셀 수 있는지)와 우리말 뜻(조금 있다/거의 없다)에 맞으므로"
    bits = []
    for i, (x, g, nn) in enumerate(zip(xs, gs, nouns)):
        if x == g: continue
        L = "첫째" if i == 0 else "둘째"
        if KIND[x][0] != KIND[g][0]: bits.append(f"{L} 빈칸 {x}: 셀 수 {'있는' if KIND[x][0] == 'C' else '없는'} 명사에 쓰는 말이라 {nn}에 맞지 않는다")
        else: bits.append(f"{L} 빈칸 {x}: ‘{'조금 있는' if KIND[x][1] else '거의 없는'}’의 뜻이라 우리말과 맞지 않는다")
    return ", ".join(bits) + ". 따라서"
def f94(t, p, c, a, nouns, s=S94):
    mk(3, 94, t, [(x, n94(x, c[a-1], nouns)) for x in c], a, R94, s, p=p, okdup=True)
f94("B", "There are _____ people in the park. (공원에 사람이 거의 없다.)\nI have _____ money. (나는 돈이 조금 있다.)", ["a few - little", "few - a little", "a few - a little", "few - little", "a little - few"], 2, ["people", "money"],
    "제시문과 정답(a few - little)이 원문항과 똑같았다. 문장을 새로 쓰고 정답 조합을 few - a little로 바꿨다.")
f94("C", "I need _____ sugar. (나는 설탕이 조금 필요하다.)\nShe has _____ friends here. (그녀는 여기에 친구가 몇 명 있다.)", ["a little - a few", "little - few", "a few - a little", "little - a few", "a little - few"], 1, ["sugar", "friends"])
f94("D", "There are _____ books on the shelf. (선반에 책이 거의 없다.)\nI have _____ water. (나는 물이 거의 없다.)", ["a few - a little", "few - a little", "little - few", "a few - little", "few - little"], 5, ["books", "water"])
f94("E", "There is _____ milk in the bottle. (병에 우유가 거의 없다.)\nTom has _____ pencils. (Tom은 연필이 몇 자루 있다.)", ["a little - a few", "little - few", "few - a little", "little - a few", "a little - few"], 4, ["milk", "pencils"])
f94("F", "We have _____ chairs. (우리에게 의자가 몇 개 있다.)\nThey have _____ information. (그들에게 정보가 조금 있다.)", ["few - little", "a little - a few", "a few - a little", "few - a little", "a few - little"], 3, ["chairs", "information"])

# 3-95 잘못 설명한 학생: 원문항처럼 학생 다섯 명, 유형마다 이름·설명을 새로
R95 = "형용사는 명사 앞이나 보어 자리, -thing 대명사 뒤에 쓴다. 부사는 동사를 꾸미며 fast·hard는 -ly 없이 부사로 쓴다(hardly는 ‘거의 ~않다’, lately는 ‘최근에’). 빈도부사는 일반동사 앞, be동사 뒤에 둔다. few·a few는 셀 수 있는 명사, little·a little은 셀 수 없는 명사에 쓴다."
S95 = "원문항은 학생 다섯 명인데 변형은 세 명이라 형식이 바뀌었다. 원문항처럼 학생 다섯 명으로 새로 쓰고 잘못 설명한 학생이 둘 이상이 되게 했다."
def f95(t, lines, judge, ok, c, a, s=S95):
    F(3, 95, t, p="\n".join(lines), c=c, a=a, r=R95, pre=["설명별 판정: " + j for j in judge], k=f"잘못 설명한 학생은 {ok}이다.", n=setnotes(c, ok, "잘못 설명한 학생"), okdup=True, s=s + ipos(a))
f95("B", ["Minho: 'She looks happy.'에서 look 뒤에 주어를 설명하는 형용사 happy가 와서 옳은 문장이야.", "Sora: 'He hardly works.'는 그가 열심히 일한다는 뜻의 옳은 문장이야.",
          "Jiwoo: 'I need something cold.'에서 형용사가 -thing 대명사 뒤에서 꾸며서 옳은 문장이야.", "Yuna: 'We have many homework.'에서 homework는 셀 수 있는 명사라 many를 써서 옳은 문장이야.",
          "Hana: 'She always is late.'에서 빈도부사는 be동사 앞에 오므로 옳은 문장이야."],
    ["Minho O. look 뒤 보어 자리에 형용사를 쓴다.", "Sora X. hardly는 ‘거의 ~않다’라는 뜻이라 거의 일하지 않는다는 뜻이다.", "Jiwoo O. -thing 대명사는 형용사가 뒤에서 꾸민다.",
     "Yuna X. homework는 셀 수 없는 명사라 much를 써야 하므로 틀린 문장이다.", "Hana X. 빈도부사는 be동사 뒤에 오므로 She is always late.가 옳다."], "Sora, Yuna, Hana",
    ["Minho, Sora", "Sora, Yuna", "Sora, Yuna, Hana", "Jiwoo, Yuna, Hana", "Minho, Jiwoo"], 3,
    "정답(Lisa, Jane)이 원문항과 이름까지 같았고 학생 수도 세 명이었다. 이름과 설명을 새로 쓰고 원문항처럼 학생 다섯 명으로 바꿨다.")
f95("C", ["Emma: 'He runs fast.'에서 fast는 -ly 없이 부사로 쓰여 옳은 문장이야.", "Leo: 'Look at the alive fish.'는 살아 있는 물고기를 보라는 옳은 문장이야.",
          "Mia: 'I found the box empty.'에서 목적격보어 자리에 형용사가 와서 옳은 문장이야.", "Olivia: 'There are a little apples.'에서 a little은 ‘조금 있는’이라는 뜻이라 옳은 문장이야.",
          "Zoe: 'She sings beautifully.'에서 부사가 동사를 꾸며서 옳은 문장이야."],
    ["Emma O. fast는 형용사와 부사의 형태가 같다.", "Leo X. alive는 명사 앞에 쓰지 않으므로 the living fish로 써야 한다.", "Mia O. find의 목적격보어 자리에 형용사를 쓴다.",
     "Olivia X. apples는 셀 수 있는 명사라 a few를 써야 한다.", "Zoe O. 부사 beautifully가 동사 sings를 꾸민다."], "Leo, Olivia",
    ["Emma, Leo", "Leo, Olivia", "Mia, Olivia", "Leo, Olivia, Zoe", "Emma, Mia, Zoe"], 2, S95 + " 틀린 설명이 없던 것도 고쳤다.")
f95("D", ["Jisu: 'The soup smells nicely.'에서 smell 뒤에 부사가 와서 옳은 문장이야.", "Minji: 'I have few friends.'는 친구가 거의 없다는 뜻의 옳은 문장이야.",
          "Sua: 'He often goes to the library.'에서 빈도부사가 일반동사 앞에 와서 옳은 문장이야.", "Haru: 'It's a lovely day.'에서 lovely는 -ly로 끝나지만 형용사라 명사 day를 꾸며서 옳은 문장이야.",
          "Yuri: 'I arrived lately.'는 내가 늦게 도착했다는 뜻의 옳은 문장이야."],
    ["Jisu X. smell 뒤 보어 자리에는 형용사 nice를 쓴다.", "Minji O. few는 ‘거의 없는’이라는 뜻이다.", "Sua O. 빈도부사는 일반동사 앞에 온다.", "Haru O. lovely는 형용사이다.",
     "Yuri X. lately는 ‘최근에’라는 뜻이라 ‘늦게’는 late로 써야 한다."], "Jisu, Yuri",
    ["Jisu, Minji", "Sua, Yuri", "Jisu, Haru, Yuri", "Jisu, Yuri", "Minji, Haru"], 4)
f95("E", ["Alice: 'Would you like something hot?'에서 형용사가 something 뒤에 와서 옳은 문장이야.", "Bella: 'She is a friendly girl.'에서 friendly는 부사라서 틀린 문장이야.",
          "Coco: 'Tom is rarely late.'에서 rarely가 be동사 뒤에 와서 옳은 문장이야.", "Diana: 'He can jump highly.'는 그가 높이 뛸 수 있다는 옳은 문장이야.",
          "Ella: 'We don't have much time.'에서 time은 셀 수 없는 명사라 much를 써서 옳은 문장이야."],
    ["Alice O. -thing 대명사는 형용사가 뒤에서 꾸민다.", "Bella X. friendly는 -ly로 끝나지만 형용사라 옳은 문장이다.", "Coco O. 빈도부사는 be동사 뒤에 온다.",
     "Diana X. ‘높이’는 high로 쓰고, highly는 ‘매우’라는 뜻이다.", "Ella O. 셀 수 없는 명사 time에 much를 쓴다."], "Bella, Diana",
    ["Bella, Coco", "Alice, Diana", "Coco, Ella", "Bella, Diana, Ella", "Bella, Diana"], 5)
f95("F", ["Nari: 'The music sounds beautiful.'에서 sound 뒤에 형용사가 와서 옳은 문장이야.", "Junho: 'He drives careful.'에서 형용사 careful이 동사를 꾸며서 옳은 문장이야.",
          "Mina: 'I have a little money.'는 돈이 조금 있다는 뜻의 옳은 문장이야.", "Dohee: 'They never are busy on Sundays.'에서 빈도부사는 be동사 앞에 오므로 옳은 문장이야.",
          "Taeho: 'Is there anything wrong?'에서 형용사가 anything 뒤에서 꾸며서 옳은 문장이야."],
    ["Nari O. sound 뒤 보어 자리에 형용사를 쓴다.", "Junho X. 동사를 꾸미는 말은 부사 carefully로 써야 한다.", "Mina O. a little은 ‘조금 있는’이라는 뜻이다.",
     "Dohee X. 빈도부사는 be동사 뒤에 오므로 They are never busy가 옳다.", "Taeho O. -thing 대명사는 형용사가 뒤에서 꾸민다."], "Junho, Dohee",
    ["Junho, Dohee", "Nari, Junho", "Mina, Dohee", "Junho, Mina, Dohee", "Dohee, Taeho"], 1)

# 3-96 보어 자리 형용사로 고치기: 원문항 발문, 밑줄, 실제로 있는 형태의 오답
ST96 = "다음 문장에서 밑줄 친 부분을 바르게 고친 것을 고르시오."
R96 = "become, look, smell, seem, feel 뒤에서 주어의 상태를 설명하는 보어 자리에는 부사가 아니라 형용사를 쓴다."
S96 = "발문이 ‘주어의 성질을 설명하도록 형용사 원급 한 단어로’라고 정답을 알려 주고 밑줄이 사라졌으며, 오답에 없는 형태(happyly, happyness)와 조건이 없으면 정답이 될 수 있는 비교급(more tired)이 있었다. 원문항 발문과 밑줄로 되돌리고 오답을 실제로 있는 틀린 형태로 바꿨다."
ADV = "보어 자리에 부사를 쓸 수 없으므로"
VADV = "very를 붙여도 부사라 보어 자리에 쓸 수 없으므로"
NOUN = "명사로는 주어의 상태를 설명하지 못해 뜻이 맞지 않으므로"
TOADJ = "to 뒤에는 동사원형을 쓰므로"
def f96(t, p, items, a, s=S96):
    mk(3, 96, t, items, a, R96, s, st=ST96, p=p, okdup=True)
f96("B", "This pillow feels <u>softly</u>.", [("soft", "feel 뒤 보어 자리에 형용사를 바르게 썼으므로"), ("softly", ADV), ("softness", NOUN), ("very softly", VADV), ("to soft", TOADJ)], 1,
    "제시문과 정답(famous)이 원문항과 똑같았고 발문도 정답을 알려 주었다. 제시문을 새로 쓰고 원문항 발문과 밑줄로 되돌렸다.")
f96("C", "Tom looks <u>tiredly</u>.", [("to tire", "보어 자리에 to부정사를 쓰면 뜻이 맞지 않으므로"), ("very tiredly", VADV), ("tired", "look 뒤 보어 자리에 형용사를 바르게 썼으므로"), ("tiredness", NOUN), ("tiredly", ADV)], 3)
f96("D", "The soup smells <u>nicely</u>.", [("very nicely", VADV), ("niceness", NOUN), ("nicely", ADV), ("nice", "smell 뒤 보어 자리에 형용사를 바르게 썼으므로"), ("to nice", TOADJ)], 4)
f96("E", "Jane seems <u>happily</u>.", [("happiness", NOUN), ("very happily", VADV), ("happily", ADV), ("to happy", TOADJ), ("happy", "seem 뒤 보어 자리에 형용사를 바르게 썼으므로")], 5)
f96("F", "The sky became <u>darkly</u>.", [("very darkly", VADV), ("darken", "become 뒤 보어 자리에 동사원형을 쓸 수 없으므로"), ("dark", "become 뒤 보어 자리에 형용사를 바르게 썼으므로"), ("darkly", ADV), ("darkness", NOUN)], 3)

# 3-97 형태·뜻이 다른 부사: 원문항 발문과 우리말 뜻 제시
ST97 = "R"  # 고친 원문항 발문(고른 것을 고르시오)
R97 = "high(높이)/highly(매우), late(늦게)/lately(최근에), hard(열심히)/hardly(거의 ~않다), wide(활짝)/widely(널리)처럼 -ly가 붙으면 뜻이 달라지는 부사가 있고, fast·early는 -ly 없이 부사로 쓴다."
S97 = "발문에 ‘원문의 주어·동작·시제를 유지하여’ 같은 조건이나 뜻 설명이 붙어 원문항과 달랐다. 원문항 발문으로 되돌리고, 원문항처럼 우리말 뜻을 제시문 아래에 붙였다."
def f97(t, p, ko, items, a, s=S97):
    mk(3, 97, t, items, a, R97, s, st=ST97, p=f"{p}\n({ko})")
f97("B", "Tom arrived at school <u>lately</u> today.", "Tom은 오늘 학교에 늦게 도착했다.",
    [("Tom arrived at school latelier today.", "latelier라는 형태는 없으므로"), ("Tom arrived at school very lately today.", "lately는 ‘최근에’라는 뜻이라 very를 붙여도 ‘늦게’가 되지 않으므로"),
     ("Tom arrived at school late today.", "‘늦게’는 late로 쓰므로"), ("Tom arrived at school too lating today.", "lating이라는 형태는 없으므로"), ("Tom arrived at school lately today.", "틀린 부분(lately, 최근에)을 그대로 두었으므로")], 3,
    "제시문과 정답(high)이 원문항과 똑같았다. 제시문을 late/lately로 새로 쓰고 원문항처럼 우리말 뜻을 붙였다.")
F(3, 97, "C", st=ST97, p=V(3, 97, "C")["passage"] + "\n(Tom은 빨리 달린다.)", s="발문에 ‘원문의 주어·동작·시제를 유지하여’ 조건이 붙어 원문항과 달랐다. 원문항 발문으로 되돌리고 원문항처럼 우리말 뜻을 붙였다. 보기와 정답은 그대로다.")
f97("D", "Jane studies <u>hardly</u> for the exam.", "Jane은 시험을 위해 열심히 공부한다.",
    [("Jane studies very hardly for the exam.", "hardly는 ‘거의 ~않다’라는 뜻이라 very를 붙여도 ‘열심히’가 되지 않으므로"), ("Jane studies hardlier for the exam.", "hardlier라는 형태는 없으므로"),
     ("Jane studies hardly for the exam.", "틀린 부분(hardly, 거의 ~않다)을 그대로 두었으므로"), ("Jane studies hard for the exam.", "‘열심히’는 hard로 쓰므로"), ("Jane studies too harding for the exam.", "harding이라는 형태는 없으므로")], 4,
    "발문의 뜻 설명(열심히 공부한다)에 기대야 답이 정해졌다. 원문항 발문으로 되돌리고, 원문항처럼 우리말 뜻을 제시문 아래에 붙여 뜻으로 정답이 정해지게 했다. 오답도 원문항처럼 없는 형태·뜻이 다른 형태로 바꿨다.")
f97("E", "Open your mouth <u>widely</u>.", "입을 활짝 벌려라.",
    [("Open your mouth wide.", "‘활짝’은 wide로 쓰므로"), ("Open your mouth widely.", "틀린 부분(widely, 널리)을 그대로 두었으므로"), ("Open your mouth very widely.", "widely는 ‘널리’라는 뜻이라 very를 붙여도 ‘활짝’이 되지 않으므로"),
     ("Open your mouth widelier.", "widelier라는 형태는 없으므로"), ("Open your mouth too widing.", "widing이라는 형태는 없으므로")], 1,
    "발문의 뜻 설명에 기대야 답이 정해졌고(lately도 쓰일 수 있음) 밑줄도 사라졌다. 원문항 발문과 밑줄로 되돌리고, 원문항처럼 우리말 뜻을 제시문 아래에 붙였으며 다른 유형과 겹치지 않게 wide/widely로 새로 썼다.")
F(3, 97, "F", st=ST97, p=V(3, 97, "F")["passage"] + "\n(나는 일찍 일어났다.)", s="발문에 ‘원문의 주어·동작·시제를 유지하여’ 조건이 붙어 원문항과 달랐다. 원문항 발문으로 되돌리고 원문항처럼 우리말 뜻을 붙였다. 보기와 정답은 그대로다.")

# 3-98 수량 표현 세 빈칸: 원문항 발문과 대화 형식, 정답 조합을 새로
ST98 = "R"  # 고친 원문항 발문(빈칸 (A)~(C))
R98 = "many·a few·few는 셀 수 있는 명사의 복수형, much·a little·little은 셀 수 없는 명사에 쓰고 a lot of는 둘 다에 쓴다. a few·a little은 ‘조금 있는’, few·little은 ‘거의 없는’이다."
S98 = "발문이 ‘세 빈칸에 들어갈 수량 표현이 모두 문법적으로 바른 것’으로 바뀌고 원문항의 대화가 짧은 문장으로 줄었으며, 정답 조합(a lot of - a few - much)이 원문항과 같았다. 원문항 발문과 대화 형식으로 되돌리고 유형마다 정답 조합을 새로 썼다."
QK = {"many": "C", "a few": "C", "few": "C", "much": "U", "a little": "U", "little": "U", "a lot of": "B"}
def n98(ch, good, spec):
    xs = [x.strip() for x in ch.split(" - ")]; gs = [x.strip() for x in good.split(" - ")]
    if xs == gs: return "(A)~(C) 모두 명사의 종류(셀 수 있는지)와 대화의 뜻에 맞으므로"
    bits = []
    for L, x, g, (noun, kind, why) in zip("ABC", xs, gs, spec):
        if x == g: continue
        k = QK[x.lower()]
        if k != "B" and k != kind: bits.append(f"({L}) {x}: 셀 수 {'있는' if k == 'C' else '없는'} 명사에 쓰는 말이라 {noun}에 맞지 않는다")
        else: bits.append(f"({L}) {x}: {why}")
    return ", ".join(bits) + ". 따라서"
def f98(t, p, c, a, spec, s=S98):
    mk(3, 98, t, [(x, n98(x, c[a-1], spec)) for x in c], a, R98, s, st=ST98, p=p, okdup=True)
f98("B", "Jina: How (A)________ students came to the meeting?\nTom: Only (B)________ students came. Most of them were sick.\nJina: That's too bad. Did you get any useful information?\nTom: I got (C)________ information, but not much.",
    ["much - a few - little", "many - a little - a few", "much - few - a little", "many - a few - a little", "many - few - much"], 4,
    [("students", "C", "학생 수를 묻는 How many가 알맞다"), ("students", "C", "Only 뒤에서 ‘몇 명’의 뜻은 a few로 나타낸다"), ("information", "U", "‘많지는 않지만 조금’이라는 뜻이라 a little이 알맞다")],
    "문장과 정답 조합(a lot of - a few - much)이 원문항과 같았고 대화가 짧은 문장으로 줄었다. 원문항처럼 대화로 새로 쓰고 원문항 발문으로 되돌렸다.")
f98("C", "Mom: How (A)________ milk is left in the fridge?\nSon: There's very (B)________. We need to buy some.\nMom: Okay. Do we need eggs, too?\nSon: Yes. We don't have (C)________ eggs.",
    ["many - little - much", "much - few - many", "much - little - many", "much - a little - much", "many - a few - many"], 3,
    [("milk", "U", "우유의 양을 묻는 How much가 알맞다"), ("milk", "U", "‘거의 없다’는 뜻이라 very little이 알맞다(very a little은 쓰지 않는다)"), ("eggs", "C", "부정문에서 달걀이 많지 않다는 뜻이라 many가 알맞다")])
f98("D", "Minji: There is (A)________ snow outside!\nSuho: Yes, it snowed all night. But there was very (B)________ snow last year.\nMinji: Let's make a snowman. Can you bring (C)________ buttons for its eyes?\nSuho: Sure. I have two.",
    ["many - little - a few", "a lot of - little - a few", "a lot of - few - a little", "much - a little - a few", "a lot of - a little - much"], 2,
    [("snow", "U", "밤새 눈이 와 많이 쌓였다는 뜻이라 a lot of가 알맞다"), ("snow", "U", "‘거의 없었다’는 뜻이라 very little이 알맞다(very a little은 쓰지 않는다)"), ("buttons", "C", "단추 두 개, 즉 ‘몇 개’의 뜻이라 a few가 알맞다")])
f98("E", "Teacher: Only five students came today. Why are there so (A)________ students?\nMina: There is a school festival. (B)________ students went there.\nTeacher: I see. Then we don't have (C)________ work to do today.",
    ["many - Much - much", "few - Much - many", "little - Many - many", "few - Many - much", "many - A few - much"], 4,
    [("students", "C", "다섯 명뿐이라 ‘거의 없는’ 뜻의 few가 알맞다"), ("students", "C", "많은 학생이 축제에 갔다는 뜻이라 Many가 알맞다"), ("work", "U", "셀 수 없는 명사 work의 부정문이라 much가 알맞다")])
f98("F", "Amy: Can I have (A)________ water, please? I'm thirsty.\nDad: Sure. Here you are.\nAmy: Thanks. Wow, there are (B)________ people in this park today!\nDad: Yes. Last week, there were very (C)________ people because of the rain.",
    ["a few - a lot of - few", "a little - much - few", "a little - a lot of - little", "little - many - a few", "a little - a lot of - few"], 5,
    [("water", "U", "목이 말라 물을 ‘조금’ 달라는 뜻이라 a little이 알맞다"), ("people", "C", "사람이 많다는 뜻이라 a lot of가 알맞다"), ("people", "C", "비 때문에 ‘거의 없었다’는 뜻이라 very few가 알맞다")])

# 3-99 빈도부사 설명: 원문항 발문과 밑줄, 그럴듯한 오개념 오답
ST99 = "다음 문장의 밑줄 친 부분에 대한 한국어 문법 설명으로 가장 적절한 것은?"
R99 = "빈도부사의 기본 위치는 일반동사 앞, be동사 뒤, 조동사나 완료형 have(has) 뒤이다. always(항상), usually(보통), often(자주), rarely·seldom(좀처럼 ~않다), never(결코 ~않다)는 부사라 동사의 형태를 바꾸지 않는다."
S99 = "발문이 원문항과 달랐고 밑줄이 사라졌으며, 오답 네 개(‘명사 앞에만 온다’, ‘언제나 문장 맨 끝’ 등)가 뻔하고 유형마다 같았다. 원문항 발문과 밑줄로 되돌리고, 원문항처럼 그럴듯한 오개념(뜻 오해, 주어 수에 따른 위치, 동사 형태 변화 등)으로 오답을 유형마다 새로 썼다."
def f99(t, p, items, a, s=S99):
    mk(3, 99, t, items, a, R99, s, st=ST99, p=p)
f99("B", "My dad <u>always</u> drinks coffee in the morning.",
    [("빈도부사 'always'는 ‘가끔’이라는 뜻이며, 문장 맨 뒤에 오는 것이 원칙이다.", "always는 ‘항상’이라는 뜻이고 기본 위치는 일반동사 앞이므로"), ("빈도부사는 주어의 인칭에 따라 위치가 결정되는데, 3인칭 단수 주어이므로 동사 앞에 왔다.", "빈도부사의 위치는 주어가 아니라 동사의 종류로 정해지므로"),
     ("'always'가 있으면 동사에 -s를 붙이지 않으므로 'drink'로 고쳐야 한다.", "부사는 동사의 형태를 바꾸지 않아 3인칭 단수 drinks가 옳으므로"), ("빈도부사는 일반동사가 있을 경우 그 앞에 위치한다는 규칙에 따라 'drinks' 앞에 쓰였다.", "일반동사 앞이라는 기본 위치를 바르게 설명했으므로"),
     ("일반동사와 빈도부사가 함께 쓰일 때는 반드시 빈도부사를 동사 뒤에 써야 강조가 된다.", "빈도부사는 일반동사 앞에 오므로")], 4,
    "문장과 정답 설명(be동사 뒤)이 원문항과 같았다. 문장을 일반동사 문장으로 새로 쓰고 원문항 발문과 밑줄로 되돌렸다.")
f99("C", "Tom <u>usually</u> gets up at six.",
    [("'usually'는 ‘절대 ~않다’는 뜻이라 Tom이 6시에 일어나지 않는다는 뜻이다.", "usually는 ‘보통’이라는 뜻이므로"), ("빈도부사는 일반동사 앞에 위치한다는 규칙에 따라 'gets' 앞에 쓰였다.", "일반동사 앞이라는 기본 위치를 바르게 설명했으므로"),
     ("빈도부사 뒤에 오는 동사는 동사원형이어야 하므로 'get'으로 고쳐야 한다.", "부사는 동사의 형태를 바꾸지 않아 3인칭 단수 gets가 옳으므로"), ("빈도부사는 주어가 사람일 때만 동사 앞에 오고, 사물일 때는 문장 끝에 온다.", "빈도부사의 위치는 주어의 종류와 관계없으므로"),
     ("'usually'는 시간 표현(at six)과 함께 쓸 수 없으므로 문장에서 빼야 한다.", "빈도부사는 시간 표현과 함께 쓸 수 있으므로")], 2)
f99("D", "Jane has <u>never</u> seen snow.",
    [("'never'는 부정의 뜻이 없으므로 'not'을 더해야 ‘본 적이 없다’는 뜻이 된다.", "never 자체가 부정의 뜻이라 not을 더하지 않으므로"), ("빈도부사는 문장에 동사가 둘 이상이면 항상 맨 뒤 동사 뒤에 온다.", "빈도부사는 완료형 has 뒤, 과거분사 앞에 오므로"),
     ("'never'는 ‘자주’라는 뜻으로, 눈을 자주 보았다는 뜻이다.", "never는 ‘결코 ~않다’라는 뜻이므로"), ("빈도부사는 has가 있어도 일반동사처럼 'has' 앞에 써야 옳다.", "완료형의 has는 조동사처럼 쓰여 빈도부사가 그 뒤에 오므로"),
     ("빈도부사는 조동사나 완료형의 have(has) 뒤에 위치한다는 규칙에 따라 'has' 다음에 쓰였다.", "완료형 has 뒤라는 기본 위치를 바르게 설명했으므로")], 5)
f99("E", "We are <u>often</u> busy on Mondays.",
    [("be동사가 있는 문장에서 빈도부사는 be동사 뒤에 온다는 규칙에 따라 'are' 뒤에 놓였다.", "be동사 뒤라는 기본 위치를 바르게 설명했으므로"), ("'often'은 ‘좀처럼 ~않다’는 뜻이므로 월요일에 거의 바쁘지 않다는 뜻이다.", "often은 ‘자주’라는 뜻이므로"),
     ("빈도부사는 주어가 복수일 때만 be동사 뒤에 오고, 단수일 때는 앞에 온다.", "빈도부사의 위치는 주어의 수와 관계없으므로"), ("be동사 문장에서는 빈도부사를 문장 맨 앞에만 쓸 수 있다.", "빈도부사의 기본 위치는 be동사 뒤이므로"),
     ("'often'이 있으면 be동사 대신 일반동사 do를 써야 한다.", "부사는 동사를 바꾸지 않으므로")], 1)
f99("F", "I will <u>always</u> remember your kindness.",
    [("'always'는 미래 시제와 함께 쓸 수 없으므로 'will'을 빼야 한다.", "빈도부사는 미래 시제와 함께 쓸 수 있으므로"), ("'always'는 ‘가끔’이라는 뜻으로, 친절을 가끔 기억할 것이라는 뜻이다.", "always는 ‘항상’이라는 뜻이므로"),
     ("빈도부사는 조동사가 있을 경우 그 뒤에 위치한다는 규칙에 따라 'will' 다음에 쓰였다.", "조동사 뒤라는 기본 위치를 바르게 설명했으므로"), ("빈도부사가 쓰이면 조동사 뒤에 to부정사를 써야 하므로 'will always to remember'로 고쳐야 한다.", "조동사 뒤에는 빈도부사가 있어도 동사원형을 쓰므로"),
     ("빈도부사의 위치는 동사의 시제에 따라 결정되는데, 미래 시제이므로 문장 맨 끝에 온다.", "빈도부사의 위치는 시제가 아니라 동사의 종류로 정해지므로")], 3)

# 3-100 틀린 문장 개수: 원문항 형식(ⓐ~ⓔ, 1개~5개)
R100 = "many·few는 셀 수 있는 명사, much·little은 셀 수 없는 명사에 쓴다. 주어의 상태를 설명하는 보어 자리에는 형용사, 동작을 꾸미는 자리에는 부사를 쓰며, 빈도부사는 be동사 뒤에 둔다."
S100 = "보기 기호 ⓐ~ⓔ가 a~e로 바뀌어 한 줄로 이어졌고 선택지 순서가 뒤섞였다. 원문항 형식(ⓐ~ⓔ 줄바꿈, 1개~5개)으로 되돌렸다."
def f100(t, lines, judge, bad, s=S100, **kw):
    n = len(bad.split(","))
    F(3, 100, t, p="\n".join(lines), c=CNT5, a=n, r=R100, pre=["문장별 판정: " + j for j in judge], k=f"어법상 틀린 문장은 {bad}로 {n}개이다.", n="cnt", s=s + ipos(n), **kw)
f100("B", ["ⓐ There are few cookies left.", "ⓑ She looked at me angry.", "ⓒ I always am tired after school.", "ⓓ Can I have a little water?", "ⓔ We need much eggs."],
     ["ⓐ O. 셀 수 있는 명사 cookies에 few를 썼다.", "ⓑ X. 동사 looked를 꾸미는 말은 부사 angrily로 쓴다.", "ⓒ X. 빈도부사는 be동사 뒤에 오므로 I am always tired로 쓴다.", "ⓓ O. 셀 수 없는 명사 water에 a little을 썼다.", "ⓔ X. 셀 수 있는 명사 eggs에는 many를 쓴다."],
     "ⓑ, ⓒ, ⓔ", "ⓐ~ⓒ가 원문항 문장과 같았고 발문에 뜻 설명이 붙었으며 기호·선택지 순서도 원본과 달랐다. 문장을 새로 쓰고 원문항 발문과 형식으로 되돌렸으며 정답 개수를 3개로 바꿨다.", st="R")
f100("C", ["ⓐ There isn't much time.", "ⓑ Tom runs fast.", "ⓒ She looks happy.", "ⓓ We have many homework.", "ⓔ Jane studies hard."],
     ["ⓐ O. 셀 수 없는 명사 time에 much를 썼다.", "ⓑ O. fast는 -ly 없이 부사로 쓴다.", "ⓒ O. look 뒤 보어 자리에 형용사를 썼다.", "ⓓ X. homework는 셀 수 없는 명사라 much를 쓴다.", "ⓔ O. ‘열심히’는 hard로 쓴다."], "ⓓ")
f100("D", ["ⓐ I have a little money.", "ⓑ She sings beautifully.", "ⓒ Tom seems tired.", "ⓓ They have much books.", "ⓔ They drove careful."],
     ["ⓐ O. 셀 수 없는 명사 money에 a little을 썼다.", "ⓑ O. 부사 beautifully가 동사를 꾸민다.", "ⓒ O. seem 뒤 보어 자리에 형용사를 썼다.", "ⓓ X. 셀 수 있는 명사 books에는 many를 쓴다.", "ⓔ X. 동사 drove를 꾸미는 말은 부사 carefully로 쓴다."], "ⓓ, ⓔ",
     "ⓔ(We arrive lately)가 발문의 뜻 설명에 기대야 틀린 문장이 되었고 발문도 원문항과 달랐으며 기호·선택지 순서도 원본과 달랐다. 원문항 발문으로 되돌리고 ⓔ를 뜻 설명 없이도 틀린 문장으로 바꿨으며 원문항 형식으로 되돌렸다.", st="R")
f100("E", ["ⓐ We have a little chairs.", "ⓑ Jane speaks English fluent.", "ⓒ The soup tastes nicely.", "ⓓ Tom has little time.", "ⓔ They have many information."],
     ["ⓐ X. 셀 수 있는 명사 chairs에는 a few를 쓴다.", "ⓑ X. 동사 speaks를 꾸미는 말은 부사 fluently로 쓴다.", "ⓒ X. taste 뒤 보어 자리에는 형용사 nice를 쓴다.", "ⓓ O. 셀 수 없는 명사 time에 little을 썼다.", "ⓔ X. information은 셀 수 없는 명사라 much를 쓴다."], "ⓐ, ⓑ, ⓒ, ⓔ",
     S100 + " 다른 유형과 정답 개수가 겹치지 않게 ⓐ·ⓑ·ⓔ를 틀린 문장으로 바꿨다.")
f100("F", ["ⓐ I have much friends.", "ⓑ She looks happily.", "ⓒ Tom runs fastly.", "ⓓ We have few money.", "ⓔ Jane got up earlily."],
     ["ⓐ X. 셀 수 있는 명사 friends에는 many를 쓴다.", "ⓑ X. look 뒤 보어 자리에는 형용사 happy를 쓴다.", "ⓒ X. fast는 -ly 없이 부사로 쓴다.", "ⓓ X. 셀 수 없는 명사 money에는 little을 쓴다.", "ⓔ X. early는 -ly 없이 부사로 쓰며 earlily라는 말은 없다."], "ⓐ, ⓑ, ⓒ, ⓓ, ⓔ",
     S100 + " 다른 유형과 정답 개수가 겹치지 않게 ⓑ~ⓔ를 틀린 문장으로 바꿔 모두 틀리게 했다.")


# ---- 2차 감수(2026-10) 추가 ----
# 3-91 C: a 뒤에 interesting을 넣으면 a interesting이 됨 → 관사 없는 복수 명사로
FIX.pop((3, 91, "C"), None)
f91("C", "interesting이", "나는 읽을 재미있는 책이 두 권 있다.", ["I", "have", "two", "books", "to read."], 4, "형용사는 꾸미는 명사 books 바로 앞에 오므로",
    S91 + " 또 a book에 interesting을 넣으면 a interesting book이 되어 관사가 맞지 않으므로, 관사가 없는 two books로 바꿨다.")

# 3-93 C~F: 없는 형태(to tired 등) 오답을 원문항처럼 명사로
S93N = "발문이 ‘주어 또는 목적어의 성질을 설명하는 형용사 원급을 넣을 때’라고 정답을 알려 주었고, 오답에 영어에 없는 형태(to tired 등)가 있어 형태만으로 지워졌다. 원문항 발문으로 되돌리고, 그 오답을 원문항처럼 명사가 든 짝으로 바꿨다."
def f93(t, p, a1, a2, b1, b2, noun, order):
    FIX.pop((3, 93, t), None)
    its = {"ok": (f"{a1} - {b1}", f"두 빈칸 모두 보어 자리이고 형용사({a1}, {b1})를 썼으므로"),
           "aa": (f"{a2} - {b2}", f"보어 자리에 부사({a2}, {b2})를 쓸 수 없으므로"),
           "oa": (f"{a1} - {b2}", f"둘째 빈칸 보어 자리에 부사({b2})를 쓸 수 없으므로"),
           "ao": (f"{a2} - {b1}", f"첫째 빈칸 보어 자리에 부사({a2})를 쓸 수 없으므로"),
           "na": (f"{noun} - {b2}", f"명사({noun})로는 주어의 상태를 설명하지 못하고, 둘째 빈칸에 부사({b2})도 쓸 수 없으므로")}
    mk(3, 93, t, [its[k] for k in order], order.index("ok") + 1, R93, S93N, st=ST93, p=p)
f93("C", "Tom looks _____.\nThe soup tastes _____.", "tired", "tiredly", "good", "well", "tiredness", ["oa", "na", "ok", "ao", "aa"])
f93("D", "Jane became _____.\nThe flower smells _____.", "famous", "famously", "nice", "nicely", "fame", ["ok", "aa", "oa", "ao", "na"])
f93("E", "The sky looks _____.\nThe room feels _____.", "dark", "darkly", "cold", "coldly", "darkness", ["aa", "oa", "ok", "na", "ao"])
f93("F", "The story sounds _____.\nThe bread tastes _____.", "interesting", "interestingly", "delicious", "deliciously", "interest", ["na", "oa", "ao", "ok", "aa"])

# 3-97 C, F: 서너 낱말짜리 문장, 동사·어순을 바꾼 오답 → 원문항 길이와 오답 방식으로
S97L = "발문에 ‘원문의 주어·동작·시제를 유지하여’ 조건이 붙어 원문항과 달랐고, 제시문이 서너 낱말뿐이었으며 오답이 부사가 아니라 동사 형태나 어순을 바꾼 문장이라 부사를 몰라도 지워졌다. 원문항 발문으로 되돌리고, 제시문을 원문항 길이로 늘려 우리말 뜻을 붙였으며 오답도 원문항처럼 부사 자리만 바꾼 문장으로 썼다."
FIX.pop((3, 97, "C"), None); FIX.pop((3, 97, "F"), None)
f97("C", "The train is running <u>fastly</u> along the river.", "기차가 강을 따라 빠르게 달리고 있다.",
    [("The train is running fastlier along the river.", "fastlier라는 형태는 없으므로"), ("The train is running fast along the river.", "fast는 -ly 없이 그대로 부사로 쓰므로"), ("The train is running very fastly along the river.", "fastly라는 말이 없어 very를 붙여도 틀리므로"),
     ("The train is running too fasting along the river.", "fasting은 ‘빠르게’라는 부사가 아니므로"), ("The train is running fastly along the river.", "틀린 부분(fastly)을 그대로 두었으므로")], 2, S97L)
f97("F", "I got up <u>earlyly</u> this morning to catch the first bus.", "나는 첫 버스를 타려고 오늘 아침 일찍 일어났다.",
    [("I got up earlyly this morning to catch the first bus.", "틀린 부분(earlyly)을 그대로 두었으므로"), ("I got up very earlyly this morning to catch the first bus.", "earlyly라는 말이 없어 very를 붙여도 틀리므로"), ("I got up earlily this morning to catch the first bus.", "earlily라는 말은 없으므로"),
     ("I got up early this morning to catch the first bus.", "early는 -ly를 더 붙이지 않고 그대로 부사로 쓰므로"), ("I got up too earlying this morning to catch the first bus.", "earlying이라는 형태는 없으므로")], 4, S97L)

# 3-100 C~F: 문장이 원문항의 절반 길이 → 원문항 수준으로, E는 원문항과 같은 4개 → 3개
S100L = "보기 기호 ⓐ~ⓔ가 a~e로 바뀌어 한 줄로 이어졌고 선택지 순서가 뒤섞였으며, 문장이 서너 낱말뿐이라 원문항(일고여덟 낱말)의 절반 길이였다. 원문항 형식(ⓐ~ⓔ 줄바꿈, 1개~5개)으로 되돌리고 문장을 원문항 수준으로 늘렸다."
for t in "CDEF": FIX.pop((3, 100, t), None)
f100("C", ["ⓐ There isn't much time left before the test.", "ⓑ Tom runs fast and never gets tired.", "ⓒ She looks happy with her new bike.", "ⓓ We have many homework to do this weekend.", "ⓔ Jane studies hard for the math exam."],
     ["ⓐ O. 셀 수 없는 명사 time에 much를 썼다.", "ⓑ O. fast는 -ly 없이 부사로 쓰고, 빈도부사 never는 일반동사 앞에 온다.", "ⓒ O. look 뒤 보어 자리에 형용사를 썼다.", "ⓓ X. homework는 셀 수 없는 명사라 much를 쓴다.", "ⓔ O. ‘열심히’는 hard로 쓴다."], "ⓓ", S100L)
f100("D", ["ⓐ I have a little money in my pocket.", "ⓑ She sings beautifully on the stage.", "ⓒ Tom seems tired after the long trip.", "ⓓ They have much books about animals.", "ⓔ My uncle drove careful on the icy road."],
     ["ⓐ O. 셀 수 없는 명사 money에 a little을 썼다.", "ⓑ O. 부사 beautifully가 동사를 꾸민다.", "ⓒ O. seem 뒤 보어 자리에 형용사를 썼다.", "ⓓ X. 셀 수 있는 명사 books에는 many를 쓴다.", "ⓔ X. 동사 drove를 꾸미는 말은 부사 carefully로 쓴다."], "ⓓ, ⓔ",
     "ⓔ(We arrive lately)가 발문의 뜻 설명에 기대야 틀린 문장이 되었고 발문도 원문항과 달랐으며 기호·선택지 순서도 원본과 달랐다. 원문항 발문과 형식으로 되돌리고 ⓔ를 뜻 설명 없이도 틀린 문장으로 바꿨으며, 서너 낱말뿐이던 문장을 원문항 수준으로 늘렸다.", st="R")
f100("E", ["ⓐ We have a little chairs in the classroom.", "ⓑ Jane speaks English fluent like a native speaker.", "ⓒ The soup tastes nicely with some salt.", "ⓓ Tom has little time for his hobbies.", "ⓔ My parents are rarely angry with me."],
     ["ⓐ X. 셀 수 있는 명사 chairs에는 a few를 쓴다.", "ⓑ X. 동사 speaks를 꾸미는 말은 부사 fluently로 쓴다.", "ⓒ X. taste 뒤 보어 자리에는 형용사 nice를 쓴다.", "ⓓ O. 셀 수 없는 명사 time에 little을 썼다.", "ⓔ O. 빈도부사 rarely가 be동사 뒤에 왔다."], "ⓐ, ⓑ, ⓒ",
     S100L + " 다른 유형과 정답 개수가 겹치지 않게 ⓐ·ⓑ를 틀린 문장으로 바꿨다.")
f100("F", ["ⓐ I have much friends in my new school.", "ⓑ She looks happily in the picture.", "ⓒ Tom runs fastly to catch the bus.", "ⓓ We have few money for the trip.", "ⓔ I want to drink cold something."],
     ["ⓐ X. 셀 수 있는 명사 friends에는 many를 쓴다.", "ⓑ X. look 뒤 보어 자리에는 형용사 happy를 쓴다.", "ⓒ X. fast는 -ly 없이 부사로 쓴다.", "ⓓ X. 셀 수 없는 명사 money에는 little을 쓴다.", "ⓔ X. -thing 대명사는 형용사가 뒤에서 꾸미므로 something cold로 쓴다."], "ⓐ, ⓑ, ⓒ, ⓓ, ⓔ",
     S100L + " 다른 유형과 정답 개수가 겹치지 않게 ⓑ~ⓔ를 틀린 문장으로 바꿔 모두 틀리게 했다.")
