# 2급 CH12 접속사 (111~120) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."

# 2-111 상관접속사: 원문항과 같던 정답(Neither - nor)을 다른 짝으로
R111 = "both A and B(둘 다), either A or B(둘 중 하나), neither A nor B(둘 다 아님), not only A but also B(A뿐 아니라 B도), not A but B(A가 아니라 B), whether A or B(A이든 B이든)는 짝과 뜻이 모두 맞아야 한다."
def CJ(pair, mean, ok): return f"{pair}: ‘{mean}’라는 뜻이라 우리말과 {'같으므로' if ok else '다르므로'}"
mk(2, 111, "B", [("Either - or", CJ("Either - or", "둘 중 하나", 0)), ("Whether - or", CJ("Whether - or", "~이든 ~이든", 1)),
                 ("Both - and", CJ("Both - and", "둘 다", 0)), ("Not only - but also", CJ("Not only - but also", "~뿐 아니라 ~도", 0)), ("Neither - nor", CJ("Neither - nor", "둘 다 아님", 0))], 2, R111,
   "우리말 뜻(‘~도 ~도 않는다’)과 정답(Neither - nor)이 원문항과 같았다. 우리말을 ‘~이든 ~이든’으로 바꿔 정답이 Whether - or가 되게 했다.",
   p="Tom이 오든 Mina가 오든 나는 상관없다.\n= _____ Tom _____ Mina comes, I don't care.")
mk(2, 111, "F", [("Whether - or", CJ("Whether - or", "~이든 ~이든", 0)), ("Neither - nor", CJ("Neither - nor", "둘 다 아님", 0)), ("Both - and", CJ("Both - and", "둘 다", 0)),
                 ("Not - but", CJ("Not - but", "A가 아니라 B", 1)), ("Either - or", CJ("Either - or", "둘 중 하나", 0))], 4, R111,
   "우리말 뜻과 정답(Neither - nor)이 원문항과 같았다. 우리말을 ‘A가 아니라 B’로 바꿔 정답이 Not - but이 되게 했다.",
   p="Jane이 아니라 그녀의 친구들이 그 소식을 알았다.\n= _____ Jane _____ her friends knew the news.")

# 2-113 that 생략: 원문항처럼 목적격 관계대명사 that이 정답
ST113 = "다음 문장 중 밑줄 친 that을 생략할 수 있는 것을 고르시오."
R113 = "목적격 관계대명사 that은 생략할 수 있다. 주격 관계대명사 that, 문장 맨 앞 주어절의 That, 진주어·보어·동격절을 이끄는 that은 생략하지 않는다."
S113 = "원문항은 목적격 관계대명사 that의 생략을 묻는데, 변형은 명사절(목적어절) that의 생략을 물었고 발문에 ‘표준 문어영어에서’ 조건이 붙었으며, 주격 관계대명사 오답 네 문장이 유형마다 같았다. 원문항 발문으로 되돌리고, 원문항처럼 목적격 관계대명사 that이 정답이 되도록 유형마다 새로 썼다."
OBJ = "목적격 관계대명사: 관계절 동사의 목적어 역할을 하므로 생략할 수 있으므로"
SUBJ = "주격 관계대명사: 관계절의 주어 역할을 하므로 생략할 수 없으므로"
REAL = "진주어절을 이끄는 접속사라 생략하지 않으므로"
COMP = "be동사 뒤 보어절을 이끄는 접속사라 생략하지 않으므로"
APPO = "앞 명사의 내용을 설명하는 동격절 접속사라 생략할 수 없으므로"
HEAD = "문장 맨 앞 주어절을 이끄는 접속사라 생략할 수 없으므로"
mk(2, 113, "B", [("The student <u>that</u> called me is Tom.", SUBJ), ("It is surprising <u>that</u> he failed the test.", REAL), ("This is the bag <u>that</u> I bought yesterday.", OBJ),
                 ("The problem is <u>that</u> we have no time.", COMP), ("<u>That</u> she is honest is clear to everyone.", HEAD)], 3, R113, S113, st=ST113)
mk(2, 113, "C", [("The movie <u>that</u> won the prize was great.", SUBJ), ("I heard the news <u>that</u> he had won.", APPO), ("It is strange <u>that</u> nobody came.", REAL),
                 ("My hope is <u>that</u> you will get better soon.", COMP), ("The song <u>that</u> Mina sang was beautiful.", OBJ)], 5, R113, S113, st=ST113)
mk(2, 113, "D", [("That is the house <u>that</u> stood here for a century.", SUBJ), ("The cake <u>that</u> my mom made was delicious.", OBJ), ("It is true <u>that</u> he moved to Busan.", REAL),
                 ("The fact <u>that</u> she lied surprised us.", APPO), ("<u>That</u> Tom won the race is amazing.", HEAD)], 2, R113, S113, st=ST113)
mk(2, 113, "E", [("This is the bag <u>that</u> was stolen.", SUBJ), ("The reason is <u>that</u> I was sick.", COMP), ("It is important <u>that</u> we save water.", REAL),
                 ("The book <u>that</u> I read last week was boring.", OBJ), ("There is a rumor <u>that</u> the store will close.", APPO)], 4, R113, S113, st=ST113)
mk(2, 113, "F", [("Is this the phone <u>that</u> you lost?", OBJ), ("The dog <u>that</u> barks loudly is Max.", SUBJ), ("It is clear <u>that</u> she is right.", REAL),
                 ("The good news is <u>that</u> we won.", COMP), ("<u>That</u> he forgot my name hurt me.", HEAD)], 1, R113, S113, st=ST113)

# 2-114 시간·조건 부사절의 will: 조건 삭제, 짝 문장 없애고 유형마다 새로
ST114 = "다음 중 어법상 어색한 것을 고르시오."
R114 = "미래의 일을 나타내는 시간·조건 부사절(when, until, after, before, if 등)에서는 will 대신 현재형을 쓴다. so ~ that(결과), since(~ 이후로/~이므로), because(이유), although(양보), unless(~하지 않으면)의 쓰임도 구별한다."
S114 = "발문에 ‘시간·조건 부사절의 will은 단순 미래 의미로만 판단’ 조건이 붙었고, 옳은 문장이 같은 내용의 틀린 문장과 짝을 이루며 오답이 유형마다 같았다. 조건을 지우고 원문항 발문으로 되돌렸으며, 의지로 읽힐 수 없는 틀린 문장과 여러 접속사 문장으로 유형마다 새로 썼다."
def WILL(cj, fix): return f"미래의 일을 나타내는 {cj} 부사절에는 현재형을 쓴다({fix}). 어색한 문장이므로"
mk(2, 114, "B", [("The soup was so hot that I couldn't eat it.", "so ~ that(너무 ~해서 …하다)의 결과 구문으로 알맞으므로"), ("You may leave early if you feel sick.", "조건 부사절에 현재형(feel)을 바르게 썼으므로"),
                 ("I'll send you a message when I will reach the hotel.", WILL("시간(when)", "when I reach")), ("I have lived here since I was ten.", "since(~ 이후로)와 현재완료가 바르게 어울리므로"),
                 ("We stayed inside because it was cold.", "because(이유) 뒤에 절이 바르게 왔으므로")], 3, R114, S114, st=ST114)
mk(2, 114, "C", [("Although it was late, she kept working.", "although(양보) 뒤에 절이 바르게 왔으므로"), ("Tom was so tired that he fell asleep.", "so ~ that의 결과 구문으로 알맞으므로"),
                 ("Since you are here, let's start.", "since(~이므로)가 이유를 바르게 나타내므로"), ("If it will snow tomorrow, the school will close.", WILL("조건(if)", "If it snows")),
                 ("I read a book while I waited.", "while(~하는 동안) 뒤에 절이 바르게 왔으므로")], 4, R114, S114, st=ST114)
mk(2, 114, "D", [("Unless you hurry, you will miss the train.", "unless(~하지 않으면) 조건 부사절에 현재형을 바르게 썼으므로"), ("We'll wait here until the bus will come.", WILL("시간(until)", "until the bus comes")),
                 ("She has been happy since she met him.", "since(~ 이후로)와 현재완료가 바르게 어울리므로"), ("I stayed home because I had a cold.", "because(이유) 뒤에 절이 바르게 왔으므로"),
                 ("The box was so heavy that I couldn't lift it.", "so ~ that의 결과 구문으로 알맞으므로")], 2, R114, S114, st=ST114)
mk(2, 114, "E", [("Call me as soon as you get home.", "as soon as 시간 부사절에 현재형을 바르게 썼으므로"), ("Though he is young, he is wise.", "though(양보) 뒤에 절이 바르게 왔으므로"),
                 ("I'll lend you my book if you need it.", "조건 부사절에 현재형(need)을 바르게 썼으므로"), ("We left early so that we could get good seats.", "so that(~하기 위해)이 목적을 바르게 나타내므로"),
                 ("After the movie will end, we'll have dinner.", WILL("시간(after)", "After the movie ends"))], 5, R114, S114, st=ST114)
mk(2, 114, "F", [("Before the sun will set, we will reach the camp.", WILL("시간(before)", "Before the sun sets")), ("It has rained a lot since we arrived.", "since(~ 이후로)와 현재완료가 바르게 어울리므로"),
                 ("As it was sunny, we went to the beach.", "as(~이므로)가 이유를 바르게 나타내므로"), ("I'll tell him when he comes back.", "시간 부사절에 현재형(comes)을 바르게 썼으므로"),
                 ("She was so kind that everyone liked her.", "so ~ that의 결과 구문으로 알맞으므로")], 1, R114, S114, st=ST114)

# 2-115 여러 접속사 용법 학생 여섯 명: 원문항 형식, 옳은 학생 수를 유형마다 다르게
ST115 = "다음 중 해당 문장을 올바르게 설명한 학생들을 모두 고르시오."
R115 = "either A or B·neither A nor B·not only A but also B는 B에, both A and B는 복수 동사에 맞춘다. 목적어 명사절의 that은 생략할 수 있지만 동격의 that은 생략하지 않는다. so that은 목적, so ~ that은 결과를 나타내고, although·because 뒤에는 절, despite·because of 뒤에는 명사가 온다. too ~ to는 so ~ that … can't로 바꿀 수 있다."
S115 = "원문항은 학생 여섯 명이 여러 접속사(Either A or B, that 생략, so that, as, although/despite, too ~ to)를 설명하는데, 변형은 다섯 명이 상관접속사 수 일치만 설명해 범위가 좁았고 모든 유형이 ‘네 명 옳음 + 한 명 틀림’ 구조라 정답이 예측되었다. 원문항처럼 여러 접속사 용법을 섞어 학생 여섯 명으로 새로 쓰고, 옳게 설명한 학생 수와 이름을 유형마다 달리했다."
def f115(t, lines, judge, ok, c, a):
    F(2, 115, t, st=ST115, p="\n".join(lines), c=c, a=a, r=R115, pre=["학생별 판정:"] + judge, k=f"올바르게 설명한 학생은 {ok}이다.", n=setnotes(c, ok, "올바르게 설명한 학생"), s=S115 + ipos(a))
f115("B", ["Ann: Either Mina or Tom is responsible. Either A or B는 B에 수일치하므로 맞는 문장이야.", "Ben: I think he is right. 명사절 접속사 that이 빠져서 틀린 문장이야.",
           "Cara: She saved money so that she could buy a bike. 여기서 so that은 '목적'의 뜻이야.", "Dan: Despite it was cold, we went out. despite 뒤에 절이 와도 되므로 옳은 문장이야.",
           "Eva: Both Jane and Leo is ready. both A and B는 단수 취급해서 맞아.", "Finn: Unless you hurry, you'll be late. Unless는 If ~ not의 뜻이야."],
     ["Ann 옳음: B(Tom)에 맞춰 is를 썼다.", "Ben 틀림: think 뒤 목적어 명사절의 that은 생략할 수 있어 옳은 문장이다.", "Cara 옳음: so that은 ‘~하기 위해’라는 목적을 나타낸다.",
      "Dan 틀림: despite 뒤에는 명사가 오므로 Although it was cold로 써야 한다.", "Eva 틀림: both A and B는 복수 동사(are)를 쓴다.", "Finn 옳음: unless는 if ~ not의 뜻이다."],
     "Ann, Cara, Finn", ["Ann, Ben, Cara", "Ann, Cara, Finn", "Ben, Dan, Eva", "Cara, Dan, Finn", "Ann, Eva, Finn"], 2)
f115("C", ["Gina: Neither Tom nor his parents are home. B(parents)에 수일치해서 맞는 문장이야.", "Hank: She said she was tired. said 뒤에는 접속사 that을 반드시 써야 하므로 틀린 문장이야.",
           "Ivy: He works as a waiter. 여기서 as는 '~로서'라는 뜻의 전치사야.", "Jake: Because of it rained, the game was canceled. because of 뒤에 절이 와도 돼.",
           "Kate: The soup is too hot for me to eat. 는 The soup is so hot that I can't eat it.으로 바꿀 수 있어.", "Liam: Not only Mina but also her friends is coming. not only A but also B는 A에 수일치하므로 맞아."],
     ["Gina 옳음: B(his parents)에 맞춰 are를 썼다.", "Hank 틀림: said 뒤 목적어 명사절의 that은 생략할 수 있어 옳은 문장이다.", "Ivy 옳음: as + 명사는 ‘~로서’라는 전치사이다.",
      "Jake 틀림: because of 뒤에는 명사가 오므로 Because it rained로 써야 한다.", "Kate 옳음: too ~ for 목적격 to부정사는 so ~ that + 주어 + can't로 바꿀 수 있다.", "Liam 틀림: not only A but also B는 B(friends)에 맞춰 are를 쓴다."],
     "Gina, Ivy, Kate", ["Gina, Ivy, Kate", "Gina, Jake, Liam", "Hank, Ivy, Jake", "Gina, Hank, Liam", "Hank, Jake, Kate"], 1)
f115("D", ["Mia: Both my sister and I am students. both A and B 뒤에는 가까운 I에 맞춰 am을 써.", "Noah: I hope you will come. hope 뒤 목적어 명사절의 that이 생략된 옳은 문장이야.",
           "Owen: He spoke loudly so that everyone could hear him. 여기서 so that은 '결과'의 뜻이야.", "Pia: Although he was sick, he went to school. Although 대신 Despite를 써도 옳아.",
           "Ray: As it was raining, we stayed home. 여기서 As는 '이유'를 나타내는 접속사야.", "Sue: This box is too heavy to lift. 는 This box is so heavy that I can't lift it.으로 바꿀 수 있어."],
     ["Mia 틀림: both A and B는 복수 동사(are)를 쓴다.", "Noah 옳음: hope 뒤 목적어 명사절의 that이 생략되었다.", "Owen 틀림: so that은 ‘~하도록’이라는 목적을 나타낸다.",
      "Pia 틀림: despite 뒤에는 명사가 오므로 절 앞에 쓸 수 없다.", "Ray 옳음: as가 ‘~이므로’라는 이유를 나타낸다.", "Sue 옳음: too ~ to는 so ~ that + 주어 + can't로 바꿀 수 있다."],
     "Noah, Ray, Sue", ["Mia, Noah, Ray", "Noah, Owen, Sue", "Noah, Ray, Sue", "Pia, Ray, Sue", "Mia, Owen, Pia"], 3)
f115("E", ["Tina: Either you or I am wrong. Either A or B는 B(I)에 수일치하므로 맞아.", "Uma: The fact she lied surprised me. 동격의 that이 생략된 옳은 문장이야.",
           "Vic: Unless you don't study, you will fail. Unless 뒤에 not을 한 번 더 써야 뜻이 통해.", "Will: Since he was a child, he has loved music. 여기서 Since는 '이유'를 나타내.",
           "Xena: I was so tired that I went to bed early. 는 결과를 나타내는 so ~ that 구문이야.", "Yuri: Despite the rain, we played soccer. Despite 뒤에 명사가 와서 옳은 문장이야."],
     ["Tina 옳음: B(I)에 맞춰 am을 썼다.", "Uma 틀림: 동격의 that은 생략할 수 없다(The fact that she lied).", "Vic 틀림: unless에 이미 not의 뜻이 있어 Unless you study로 써야 한다.",
      "Will 틀림: 현재완료와 함께 쓰인 since는 ‘~ 이후로’라는 뜻이다.", "Xena 옳음: so ~ that은 ‘너무 ~해서 …하다’라는 결과를 나타낸다.", "Yuri 옳음: despite 뒤에 명사(the rain)가 왔다."],
     "Tina, Xena, Yuri", ["Tina, Uma, Xena", "Uma, Vic, Will", "Vic, Xena, Yuri", "Tina, Will, Yuri", "Tina, Xena, Yuri"], 5)
f115("F", ["Zoe: Not only Tom but also his sisters like music. B(sisters)에 수일치해서 like를 쓴 옳은 문장이야.", "Adam: I know that man who is standing there. 에서 that은 명사절 접속사야.",
           "Bella: I was late because the traffic jam. because 뒤에 명사가 와도 돼.", "Chris: The water is warm enough to swim in. 은 The water is so warm that we can swim in it.으로 바꿀 수 있어.",
           "Dora: He runs every morning so that he can stay healthy. so that은 '목적'을 나타내.", "Eli: Both Jane and Mina likes cats. both A and B는 단수 취급하므로 맞아."],
     ["Zoe 옳음: B(his sisters)에 맞춰 like를 썼다.", "Adam 틀림: that은 명사(man)를 꾸미는 지시형용사(저)이다.", "Bella 틀림: because 뒤에는 절이 오므로 because of the traffic jam으로 써야 한다.",
      "Chris 옳음: enough to는 so ~ that + 주어 + can으로 바꿀 수 있다.", "Dora 옳음: so that은 ‘~하기 위해’라는 목적을 나타낸다.", "Eli 틀림: both A and B는 복수 동사(like)를 쓴다."],
     "Zoe, Chris, Dora", ["Zoe, Adam, Bella", "Chris, Dora, Eli", "Adam, Chris, Dora", "Zoe, Chris, Dora", "Zoe, Bella, Eli"], 4)

# 2-116 부적합: 원문항처럼 상관접속사 주어 뒤 be동사 형태
ST116 = "다음 빈칸에 들어갈 가장 적절한 단어는?"
R116 = "either A or B, neither A nor B, not only A but also B가 주어이면 동사는 B에 수를 맞추고, both A and B는 복수 동사를 쓴다."
S116 = "원문항은 상관접속사 주어 뒤 동사의 수 일치를 묻는데, 변형은 우리말 뜻에 맞는 접속사(because, so, when, unless, while)를 고르는 문항으로 평가 문법이 달랐고 발문도 달랐다. 원문항 발문과 형식(상관접속사 주어 뒤 빈칸에 알맞은 be동사 형태)으로 다시 썼다."
def BE(x, why): return f"{x}: {why}"
NONFIN = {"be": BE("be", "주어 뒤 동사 자리에 원형을 쓸 수 없으므로"), "being": BE("being", "-ing만으로는 문장의 동사가 될 수 없으므로")}
mk(2, 116, "B", [("is", BE("is", "동사는 B(I)에 맞추므로 3인칭 단수형은 맞지 않으므로")), ("am", BE("am", "Either A or B는 B(I)에 수를 맞추므로")), ("are", BE("are", "동사는 B(I)에 맞추므로 맞지 않으므로")),
                 ("be", NONFIN["be"]), ("being", NONFIN["being"])], 2, R116, S116, st=ST116, p="- Either my sister or I ________ going to cook dinner tonight.")
mk(2, 116, "C", [("is", BE("is", "동사는 B(his friends)에 맞추므로 단수형은 맞지 않으므로")), ("am", BE("am", "주어가 I가 아니므로")), ("be", NONFIN["be"]),
                 ("are", BE("are", "Neither A nor B는 B(his friends, 복수)에 수를 맞추므로")), ("being", NONFIN["being"])], 4, R116, S116, st=ST116, p="- Neither Tom nor his friends ________ interested in the game.")
mk(2, 116, "D", [("are", BE("are", "동사는 B(the teacher, 단수)에 맞추므로 맞지 않으므로")), ("am", BE("am", "주어가 I가 아니므로")), ("being", NONFIN["being"]), ("be", NONFIN["be"]),
                 ("is", BE("is", "Not only A but also B는 B(the teacher, 단수)에 수를 맞추므로"))], 5, R116, S116, st=ST116, p="- Not only the students but also the teacher ________ excited about the trip.")
mk(2, 116, "E", [("is", BE("is", "Both A and B는 복수이므로 단수형은 맞지 않으므로")), ("am", BE("am", "주어가 I가 아니므로")), ("are", BE("are", "Both A and B는 복수 동사를 쓰므로")),
                 ("being", NONFIN["being"]), ("be", NONFIN["be"])], 3, R116, S116, st=ST116, p="- Both Mina and her brother ________ good at swimming.")
mk(2, 116, "F", [("are", BE("are", "동사는 B(the coach, 단수)에 맞추므로 맞지 않으므로")), ("is", BE("is", "Either A or B는 B(the coach, 단수)에 수를 맞추므로")), ("am", BE("am", "주어가 I가 아니므로")),
                 ("be", NONFIN["be"]), ("being", NONFIN["being"])], 2, R116, S116, st=ST116, p="- Either the players or the coach ________ going to speak first.")

# 2-118 부적합: 원문항처럼 A as well as B / not only A but also B 주어 뒤 동사 형태
ST118 = "다음 문장의 빈칸에 들어갈 동사의 형태가 가장 적절한 것은?"
R118 = "A as well as B가 주어이면 동사는 A에, not only A but also B는 B에 수를 맞춘다."
S118 = "원문항은 ‘A as well as B’ 주어 뒤 동사의 수 일치를 동사 형태 중에서 고르는 문항인데, 변형은 우리말 뜻에 맞는 상관접속사 짝을 고르는 문항으로 평가 요소와 선택지 형태가 모두 달랐다. 원문항 발문과 형식(상관접속사 주어 뒤 빈칸에 동사 형태)으로 다시 썼다."
mk(2, 118, "B", [("are", BE("are", "A as well as B는 A(Tom, 단수)에 맞추므로 맞지 않으므로")), ("is", BE("is", "A as well as B는 A(Tom, 단수)에 수를 맞추므로")), ("am", BE("am", "주어가 I가 아니므로")),
                 ("being", NONFIN["being"]), ("were", BE("were", "now가 있어 현재이고, 주어(Tom)도 단수이므로"))], 2, R118, S118, st=ST118, p="Tom as well as his friends ________ playing soccer now.")
mk(2, 118, "C", [("is", BE("is", "not only A but also B는 B(her parents, 복수)에 맞추므로 맞지 않으므로")), ("am", BE("am", "주어가 I가 아니므로")), ("was", BE("was", "B(her parents)가 복수라 단수형은 맞지 않으므로")),
                 ("are", BE("are", "not only A but also B는 B(her parents, 복수)에 수를 맞추므로")), ("being", NONFIN["being"])], 4, R118, S118, st=ST118, p="Not only Mina but also her parents ________ coming to the party.")
mk(2, 118, "D", [("are", BE("are", "A as well as B는 A(The teacher, 단수)에 맞추므로 맞지 않으므로")), ("were", BE("were", "A(The teacher)가 단수라 복수형은 맞지 않으므로")), ("am", BE("am", "주어가 I가 아니므로")),
                 ("being", NONFIN["being"]), ("is", BE("is", "A as well as B는 A(The teacher, 단수)에 수를 맞추므로"))], 5, R118, S118, st=ST118, p="The teacher as well as the students ________ excited about the field trip.")
mk(2, 118, "E", [("am", BE("am", "A as well as B는 A(My sister)에 맞추므로 B(I)에 맞춘 am은 맞지 않으므로")), ("are", BE("are", "A(My sister)가 단수라 복수형은 맞지 않으므로")),
                 ("is", BE("is", "A as well as B는 A(My sister, 단수)에 수를 맞추므로")), ("be", NONFIN["be"]), ("being", NONFIN["being"])], 3, R118, S118, st=ST118, p="My sister as well as I ________ interested in art.")
mk(2, 118, "F", [("am", BE("am", "not only A but also B는 B(I)에 수를 맞추므로")), ("is", BE("is", "동사는 B(I)에 맞추므로 3인칭 단수형은 맞지 않으므로")), ("are", BE("are", "동사는 B(I)에 맞추므로 맞지 않으므로")),
                 ("be", NONFIN["be"]), ("were", BE("were", "B(I)와 맞지 않는 형태이므로"))], 1, R118, S118, st=ST118, p="Not only my brother but also I ________ going to the camp.")

# 2-119 when 명사절 vs 부사절: 오답 설명을 유형마다 새로
R119 = "언제인지를 나타내는 when절(간접의문문)은 명사절로 미래의 일에 will을 쓸 수 있다. ‘~할 때’라는 시간 부사절 when절은 미래의 일도 현재형으로 나타낸다."
S119 = "오답 설명 세 개 이상이 B와 똑같아서 유형마다 새로 썼다."
OK119 = "명사절과 부사절의 차이와 그에 따른 시제를 바르게 설명했으므로"
mk(2, 119, "C", [("(A)의 when은 ‘~할 때’라는 뜻의 부사절이므로 will leave를 leaves로 고쳐야 한다.", "(A)는 tell의 목적어인 명사절(언제 떠날지)이라 will leave가 옳으므로"),
                 ("(B)의 when절은 tell의 목적어 역할을 한다.", "(B)의 when절은 board를 꾸미는 시간 부사절이므로"), ("(A)와 (B) 모두 when 대신 if를 써도 뜻이 같다.", "if로 바꾸면 ‘~인지’, ‘만약 ~하면’으로 뜻이 달라지므로"),
                 ("(A)는 명사절 when이라 미래시제가 가능하고, (B)는 부사절 when이라 현재시제를 쓴다.", OK119), ("(B)의 arrives는 현재의 습관을 나타낸다.", "(B)의 arrives는 시간 부사절에서 미래의 일을 나타내므로")], 4, R119, S119)
mk(2, 119, "D", [("(A)의 when절은 know의 목적어가 아니라 시간을 나타내는 부사절이다.", "(A)의 when절은 know의 목적어인 명사절이므로"), ("(A)는 know의 목적어인 명사절, (B)는 시간 부사절이므로 시제 사용이 다르다.", OK119),
                 ("(B)는 명사절이므로 finishes를 will finish로 고쳐야 한다.", "(B)는 eat을 꾸미는 시간 부사절이라 현재형 finishes가 옳으므로"), ("(A)의 will finish는 Jane의 강한 의지를 나타낸다.", "(A)의 will은 끝나는 때에 대한 단순한 미래를 나타내므로"),
                 ("(A)와 (B) 모두 when을 생략해도 문장이 성립한다.", "when을 빼면 두 문장 모두 절이 이어지지 않아 성립하지 않으므로")], 2, R119, S119)
mk(2, 119, "E", [("(A)의 when절은 문장의 주어 역할을 한다.", "(A)의 when절은 tell의 직접목적어 역할을 하므로"), ("(B)의 calls는 과거의 일을 나타낸다.", "(B)의 calls는 시간 부사절에서 미래의 일을 나타내므로"),
                 ("(A)는 부사절이므로 will call을 calls로 바꿔야 한다.", "(A)는 명사절이라 will call이 옳으므로"), ("(B)의 when은 ‘언제’라는 뜻의 의문사이다.", "(B)의 when은 ‘~할 때’라는 뜻의 접속사이므로"),
                 ("(A)는 명사절이므로 will을 쓸 수 있고, (B)는 시간 부사절이므로 현재형으로 미래를 나타낸다.", OK119)], 5, R119, S119)
mk(2, 119, "F", [("(A)의 when절은 명사절이라 will 가능, (B)는 부사절이라 현재시제를 쓴다.", OK119), ("(A)의 when절은 knows의 목적어이므로 현재시제 stops만 쓸 수 있다.", "명사절에서는 미래의 일에 will을 쓸 수 있으므로"),
                 ("(B)는 시간 부사절이지만 미래의 일이므로 will stop을 써야 한다.", "시간 부사절에서는 미래의 일도 현재형으로 나타내므로"), ("(A)와 (B)의 when은 둘 다 ‘~할 때’라는 뜻이다.", "(A)의 when은 ‘언제’라는 뜻이므로"),
                 ("(B)의 when절은 leave의 목적어 역할을 한다.", "(B)의 when절은 leave를 꾸미는 시간 부사절이므로")], 1, R119, S119)

# 2-120 올바르지 않은 문장 개수: 조건 삭제, 원문항처럼 1개~5개 보기, 정답 개수를 유형마다 다르게
ST120 = "다음 <보기> 중 어법상 올바르지 않은 문장은 몇 개인가?"
R120 = "미래의 시간·조건 부사절은 현재형을 쓴다. although(though)와 but은 함께 쓰지 않고, despite·because of 뒤에는 명사, although·because 뒤에는 절이 온다. unless에는 not의 뜻이 들어 있다. 상관접속사 주어는 B에(both A and B는 복수로) 동사를 맞춘다."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]
S120 = "발문에 ‘미래 시간·조건절은 단순 미래로 판단’ 조건이 붙었고 개수 선택지 순서가 뒤섞였다. 조건을 지우고 원문항 발문으로 되돌렸으며, 원문항처럼 1개~5개 순으로 선택지를 맞추고 문장마다 줄을 바꿨다."
def f120(t, lines, judge, wrong, s=""):
    n = len(wrong.split(","))
    F(2, 120, t, st=ST120, p="<보기>\n" + "\n".join(lines), c=CNT5, a=n, r=R120, pre=["문장별 판정: " + j for j in judge], k=f"어법상 올바르지 않은 문장은 {wrong}로 {n}개이다.", n="cnt", s=S120 + s + ipos(n))
f120("B", ["ⓐ Unless you hurry, you will miss the bus.", "ⓑ Even though Mina was tired, she finished the work.", "ⓒ I'll call you when I will arrive.", "ⓓ Neither Tom nor his friends is coming.", "ⓔ Both Jane and Leo are ready."],
     ["ⓐ O. unless 조건절에 현재형을 썼다.", "ⓑ O. even though(양보) 뒤에 절이 왔다.", "ⓒ X. 시간 부사절에는 현재형을 쓴다(when I arrive).", "ⓓ X. B(his friends)에 맞춰 are를 쓴다.", "ⓔ O. both A and B는 복수 동사를 쓴다."], "ⓒ, ⓓ")
f120("C", ["ⓐ If it will rain tomorrow, we'll stay home.", "ⓑ Although he was busy, but he helped me.", "ⓒ Either Mina or her parents are coming.", "ⓓ Both Tom and Jane is absent.", "ⓔ We will leave after the bus arrives."],
     ["ⓐ X. 조건 부사절에는 현재형을 쓴다(If it rains).", "ⓑ X. although와 but은 함께 쓰지 않는다.", "ⓒ O. B(her parents)에 맞춰 are를 썼다.", "ⓓ X. both A and B는 복수 동사(are)를 쓴다.", "ⓔ O. 시간 부사절에 현재형을 썼다."], "ⓐ, ⓑ, ⓓ",
     " 다른 유형과 정답 개수가 겹치지 않게 ⓐ·ⓑ를 틀린 문장으로 바꿨다.")
f120("D", ["ⓐ Unless you study, you won't pass.", "ⓑ Even though she was tired, she continued.", "ⓒ I'll wait until Tom will come.", "ⓓ Not only Mina but also her friends are here.", "ⓔ Both parents is working."],
     ["ⓐ O. unless 조건절에 현재형을 썼다.", "ⓑ O. even though(양보) 뒤에 절이 왔다.", "ⓒ X. 시간 부사절에는 현재형을 쓴다(until Tom comes).", "ⓓ O. B(her friends)에 맞춰 are를 썼다.", "ⓔ X. both parents는 복수이므로 are를 쓴다."], "ⓒ, ⓔ")
f120("E", ["ⓐ If Jane finishes early, she will call.", "ⓑ Although it rained, we played.", "ⓒ Neither the boys nor Tom is ready.", "ⓓ Both Mina and Jane are students.", "ⓔ We will eat when Dad will get home."],
     ["ⓐ O. 조건 부사절에 현재형을 썼다.", "ⓑ O. although(양보) 뒤에 절이 왔다.", "ⓒ O. B(Tom)에 맞춰 is를 썼다.", "ⓓ O. both A and B는 복수 동사를 쓴다.", "ⓔ X. 시간 부사절에는 현재형을 쓴다(when Dad gets home)."], "ⓔ")
f120("F", ["ⓐ Unless it stops raining, we'll wait.", "ⓑ Despite Tom was nervous, he spoke well.", "ⓒ Either the teacher or the students is presenting.", "ⓓ Both my brothers are tall.", "ⓔ I'll text you after I will arrive."],
     ["ⓐ O. unless 조건절에 현재형을 썼다.", "ⓑ X. despite 뒤에는 명사가 오므로 Although Tom was nervous로 쓴다.", "ⓒ X. B(the students)에 맞춰 are를 쓴다.", "ⓓ O. both + 복수명사는 복수 동사를 쓴다.", "ⓔ X. 시간 부사절에는 현재형을 쓴다(after I arrive)."], "ⓑ, ⓒ, ⓔ",
     " 틀린 문장이 하나도 없어 원문항과 인지 과정이 달랐던 것을, ⓑ·ⓒ·ⓔ를 틀린 문장으로 바꿔 오류를 판별하게 했다.")

# ---- 2차 감수(2026-10) 추가 ----
# 2-119 B: 정답만 길고 오답은 짧은 한 줄 → 원문항처럼 (A)·(B)를 짚는 그럴듯한 오개념으로
mk(2, 119, "B", [("(A)의 when절은 시간의 부사절이므로 will arrive를 arrives로 고쳐야 한다.", "(A)는 wonder의 목적어인 명사절(언제 올지)이라 will arrive가 옳으므로"),
                 ("(B)의 when절은 call의 목적어인 명사절이므로 arrives를 will arrive로 고쳐야 한다.", "(B)는 ‘~할 때’라는 시간 부사절이라 현재형 arrives가 옳으므로"),
                 ("(A)는 '언제 올지'를 나타내는 명사절이라 미래 will이 가능하고, (B)는 시간 부사절이라 현재시제로 미래를 나타낸다.", OK119),
                 ("(A)와 (B)의 when절은 둘 다 미래의 일을 말하므로 두 곳 모두 will arrive로 써야 한다.", "시간 부사절인 (B)에는 will을 쓸 수 없으므로"),
                 ("(A)와 (B)의 when은 둘 다 ‘~할 때’라는 뜻의 접속사이므로 두 곳 모두 현재시제를 써야 한다.", "(A)의 when은 ‘언제’라는 뜻의 의문사이고 will을 쓸 수 있으므로")], 3, R119,
   "정답만 두 문장을 견주는 긴 설명이고 오답은 짧은 한 줄이라 형식으로 답이 드러났다. 원문항처럼 오답도 (A)·(B)를 짚는 그럴듯한 설명으로 다시 썼다.")
