# 1급 CH1 문장의 구조 (1~10) 2차 감수
X(1, 1, r="smell, taste, sound, feel, look, seem처럼 주어의 상태를 설명하는 2형식 동사 뒤 보어 자리에는 부사가 아니라 형용사를 쓴다.",
  n=["smell 뒤에 형용사 sweet가 보어로 와서 올바르므로", "taste 뒤 보어 자리에 부사 deliciously를 썼다. 형용사 delicious로 고쳐야 하므로", "sound 뒤에 형용사 beautiful이 보어로 와서 올바르므로",
     "feel 뒤에 형용사 soft가 보어로 와서 올바르므로", "seem 뒤에 형용사 reasonable이 보어로 와서 올바르므로"],
  st="① 밑줄마다 동사가 smell·taste·sound·feel·look·seem 같은 2형식 동사임을 확인한다. → ② 그 뒤에 온 말이 형용사인지 -ly로 끝나는 부사인지 가른다. → ③ {n}만 부사({0})가 왔으므로 형용사({1})로 고쳐야 한다.",
  R=("deliciously", "delicious"), B=("badly", "bad"), C=("bitterly", "bitter"), D=("warmly", "warm"), E=("strangely", "strange"), F=("comfortably", "comfortable"))
RV(1, 1, "B", v="수정(내용)", why="정답 ④ 확인. 틀린 문장에만 수식어구(this morning)가 붙어 다섯 보기 중 가장 길다. 길이만 보고 정답을 고를 수 있다(C4). smell이 ④(틀림)와 ⑤(옳음)에 함께 나온다.", fix="원문항처럼 모든 보기에 수식어구를 붙여 길이를 고르게")
RV(1, 1, "CDEF", v="수정(내용)", why="정답 확인. 틀린 문장에만 수식어구가 붙어 가장 길어 길이만 보고 정답을 고를 수 있다(C4). 밑줄도 보어에만 있어 원문항(동사 + 보어)과 범위가 다르다(A3).", fix="모든 보기에 수식어구를 붙이고, 밑줄을 동사 + 보어로")

X(1, 2, r="수여동사 문장을 3형식으로 쓸 때 give, send, show, tell, pass처럼 상대에게 건네는 동사는 to를, make, buy, cook, get처럼 상대를 위해 해 주는 동사는 for를 쓴다.",
  n=["send A to B로 to를 쓰므로", "give A to B로 to를 쓰므로", "tell A to B로 to를 쓰므로", "show A to B로 to를 쓰므로", "make A for B로, 나머지와 달리 for를 쓰므로"],
  st="① 보기마다 빈칸 앞의 동사를 찾는다: {0}. → ② ‘~에게 건네는’ 동사는 to, ‘~을 위해 해 주는’ 동사는 for를 쓴다. → ③ {1}만 for를 쓰는 동사이므로 정답은 {n}.",
  R=("send, give, tell, show, make", "make"), B=("prepare, explain, hand, pass, send", "prepare"), C=("lend, buy, show, give, mail", "buy"),
  D=("read, offer, reserve, write, point out", "reserve"), E=("cook, send, show, give, deliver", "cook"), F=("pass, order, tell, return, send", "order"))

X(1, 3, r="사역동사 make, have, let은 목적어 뒤에 동사원형을 쓰고, help는 동사원형과 to부정사를 모두 쓴다. get은 목적어 뒤에 to부정사를 쓴다.",
  n=["made + 목적어 + 동사원형(study)으로 올바르므로", "had + 목적어 + 동사원형(wash)으로 올바르므로", "let + 목적어 + 동사원형(use)으로 올바르므로",
     "get은 목적어 뒤에 to부정사를 쓴다. got the children to clean으로 고쳐야 하므로", "help는 목적어 뒤에 to부정사도 쓸 수 있어 올바르므로"],
  st="① 문장마다 사역동사(make, have, let, help, get)와 목적어 뒤의 동사 형태를 짝짓는다. → ② make·have·let 뒤의 동사원형, help 뒤의 동사원형·to부정사는 모두 옳다. → ③ get만 to부정사가 필요한데 {n}은 got + 목적어 뒤에 동사원형({0})을 썼다. to부정사(to {0})로 고쳐야 한다.",
  R="clean", B="fix", C="join", D="stay", E="book", F="write")

X(1, 4, r="attend, discuss, resemble, reach, marry, enter, approach는 우리말로 ‘~에, ~에 대해, ~와’로 옮겨져도 전치사 없이 목적어를 바로 취하는 타동사이다.",
  n=["marry는 결혼 상대를 바로 목적어로 취한다. with가 필요 없으므로", "discuss는 논의 대상을 바로 목적어로 취한다. about이 필요 없으므로", "resemble은 닮은 대상을 바로 목적어로 취한다. to가 필요 없으므로",
     "reach는 도착하는 곳을 바로 목적어로 취한다. to가 필요 없으므로", "discuss가 목적어 the proposal을 전치사 없이 바로 취해 올바르므로"],
  st="① 문장마다 동사 바로 뒤에 전치사가 끼어 있는지 본다. → ② 오답 네 문장은 전치사 없이 목적어를 받는 타동사 뒤에 전치사를 붙였다({0}). → ③ {n}만 동사 뒤에 목적어가 바로 온다({1}).",
  R=("marry with, discussed about, resembles to, reached to", "discuss the proposal"), B=("reached at, entered to, resembles with, approached to", "discussed the article"),
  C=("approached to, reached to, resembles to, considered about", "considered the proposal"), D=("discussed about, reached at, married with, entered into", "approached the entrance"),
  E=("approached to, resembles to, discussed about, reached at", "resembles her aunt"), F=("reached to, discussed about, resembles with, entered into", "reached the shelter"))
RV(1, 4, "B", v="수정(내용)", why="정답 ② 확인. 다만 ④ ‘We attended to the ceremony.’는 attend to(~을 처리하다, 돌보다)로 읽으면 옳은 문장이 될 수 있어 정답 시비가 생긴다(C1 우려). E 유형에서 같은 문제로 괄호 조건을 붙였던 것과 같은 결함이다.", fix="④를 뜻과 상관없이 틀린 문장으로")

X(1, 5, r="감각동사 뒤 보어와 find·keep 뒤 목적격 보어 자리에는 형용사(분사)를 쓰고, reach·discuss·enter 같은 타동사는 전치사 없이 목적어를 받는다. sleep 같은 1형식 동사는 부사가 꾸민다.",
  pre=["문장별 판정: a) X. smells 뒤 보어는 형용사 wonderful이어야 한다. b) O. found + 목적어 + 형용사(entertaining). c) O. kept + 목적어 + 과거분사(closed). d) O. 부사 quietly가 sleeps를 꾸민다. e) O. inform A of B. f) X. reach는 전치사 없이 쓴다(reached the summit)."],
  k="틀린 문장은 a), f) 두 개다.",
  n=["틀린 문장은 a), f) 두 개이므로"] * 5,
  st="① 문장마다 동사의 종류부터 가른다. 감각동사 뒤와 find·keep·make·consider의 목적어 뒤는 형용사 자리이고, reach·discuss·enter·approach 뒤는 전치사 없는 목적어 자리다. → ② 형용사 자리에 부사가 왔거나 타동사 뒤에 전치사가 붙은 문장을 표시한다: {0}. → ③ 표시한 문장을 세면 {a}이다.",
  R="a) smells wonderfully, f) reached at", B="b) found the room comfortably, f) entered into", C="a) feels warmly, f) approached to",
  D="b) found the task difficultly, f) entered into", E="e) discussed about", F="a) looks beautifully")

X(1, 6, r="smell, taste, sound, feel, seem 같은 연결동사는 뒤에 형용사 보어를 받는다. 주어가 3인칭 단수이고 현재이면 동사에 -s를 붙인다.",
  n=["3인칭 단수 주어 The soup에 맞춘 smells 뒤에 형용사 보어 delicious가 와서 올바르므로", "-ing형은 혼자서 문장의 동사가 될 수 없으므로", "‘~한 냄새가 나다’라는 뜻의 smell은 수동태로 쓰지 않으므로",
     "to부정사는 문장의 동사 자리에 올 수 없으므로", "주어 The soup가 3인칭 단수라 smell이 아니라 smells를 써야 하므로"],
  st="① 빈칸 뒤에 형용사({0})만 있고 다른 동사가 없으므로, 빈칸은 형용사 보어를 받는 연결동사가 문장의 동사로 들어갈 자리다. → ② -ing형과 to부정사는 혼자 동사 자리에 올 수 없어 지운다. → ③ 주어({1})가 3인칭 단수이므로 원형이 아니라 -s가 붙은 {a}를 고른다.",
  R=("delicious", "The soup"), B=("loud", "The bell"), C=("fresh", "The bread"), D=("smooth", "The fabric"), E=("reasonable", "The explanation"), F=("too salty", "The sauce"))
RV(1, 6, "B", fx=True, why="수정 예시의 오답 is sounded는 ‘The bell is sounded loud(종을 크게 울린다)’로 읽을 수 있어 정답 시비가 생길 수 있었다. 부사 soundly로 바꿨다.")

X(1, 7, r="attend, discuss, reach, enter, approach, resemble은 전치사 없이 목적어를 바로 취하는 타동사이다. ask about처럼 원래 전치사와 함께 쓰는 동사와 구별한다.",
  n=["attend가 목적어 the meeting을 바로 취해 올바르므로", "discuss가 목적어 the new rules를 바로 취해 올바르므로", "reach 뒤에 전치사 없이 home이 와서 올바르므로",
     "장소에 들어간다는 뜻의 enter는 전치사 없이 쓴다. entered my room으로 고쳐야 하므로", "ask about은 ‘~에 대해 묻다’라는 뜻으로 about이 필요해 올바르므로"],
  st="① 밑줄 친 동사 가운데 전치사가 붙은 것부터 찾는다: {0}. → ② {1}. → ③ 따라서 {n}에서 전치사를 뺀 형태({2})가 바르다.",
  R=("④ entered into, ⑤ asked about", "ask about은 ‘~에 대해 묻다’라 about이 꼭 필요하지만, enter는 들어가는 장소를 바로 목적어로 받는다", "entered my room"),
  B=("④ entered into, ⑤ asked about", "ask about은 ‘~에 대해 묻다’라 about이 꼭 필요하지만, enter는 들어가는 장소를 바로 목적어로 받는다", "entered a quiet office"),
  C=("④ approached to, ⑤ asked about", "ask about은 about이 꼭 필요하지만, approach는 다가가는 대상을 바로 목적어로 받는다", "approached the manager"),
  D=("③ discussed about, ⑤ asked about", "ask about은 about이 꼭 필요하지만, discuss는 논의 대상을 바로 목적어로 받는다", "discussed the exhibit"),
  E=("④ resembles to, ⑤ asked about", "ask about은 about이 꼭 필요하지만, resemble은 닮은 대상을 바로 목적어로 받는다", "resembles him"),
  F=("⑤ reached to 하나뿐이다", "같은 동사를 쓴 ③ reached her seat처럼 reach는 목적어를 바로 받는다", "reached a decision"))

X(1, 8, r="ask a favor of + 사람, get·buy·make·prepare A for + 사람, hand·give·show·pass A to + 사람처럼 동사마다 사람 앞에 쓰는 전치사가 정해져 있다.",
  k="(A) ask a favor of, (B) get A for, (C) hand A to이므로 of - for - to가 맞다.",
  n=["(A)는 to가 아니라 of이므로", "(B)는 to가 아니라 for이므로", "(A)는 of, (B)는 for, (C)는 to여야 하는데 세 자리가 모두 다르므로", "(A) of, (B) for, (C) to가 모두 맞으므로", "(C)는 for가 아니라 to이므로"],
  st="① 빈칸 앞의 동사 세 개를 찾는다: {0}. → ② ask a favor 뒤에는 of, ‘~을 위해 해 주는’ 동사({1}) 뒤에는 for, ‘~에게 건네는’ 동사({2}) 뒤에는 to를 쓴다. → ③ 세 자리를 순서대로 맞춘 {a}를 고른다.",
  R=("(A) ask a favor, (B) get, (C) hand", "get", "hand"), B=("(A) explain, (B) prepare, (C) ask a favor", "prepare", "explain"), C=("(A) ask a favor, (B) buy, (C) show", "buy", "show"),
  D=("(A) ask a favor, (B) make, (C) give", "make", "give"), E=("(A) ask a favor, (B) reserve, (C) pass", "reserve", "pass"), F=("(A) ask a favor, (B) prepare, (C) pass", "prepare", "pass"))

X(1, 9, r="make, keep, find, leave + 목적어 뒤의 목적격 보어 자리에는 부사가 아니라 형용사(분사)를 쓴다.",
  pre=["문장별 판정: (a) O. leave + 목적어 + 형용사(open). (b) X. exhaustedly를 exhausted로 고친다. (c) O. kept + 목적어 + 형용사(hopeful). (d) O. found + 목적어 + 형용사(empty). (e) X. made + 목적어 뒤에 부사 luckily를 쓸 수 없다."],
  k="어색한 문장은 (b), (e) 두 개다.",
  n=["어색한 문장은 (b), (e) 두 개이므로"] * 5,
  st="① 문장마다 make·keep·find·leave + 목적어 뒤에 온 말(목적격 보어)을 찾는다. → ② 그 자리에 -ly 부사가 오면 어색한 문장이다: {0}. → ③ 세어 보면 {a}이다.",
  R="(b) exhaustedly, (e) luckily", B="(b) comfortably", C="(a) angrily, (e) impatiently", D="(b) beautifully", E="(b) confusingly", F="(a) inspiringly")

X(1, 10, r="동사 + 목적어 뒤에 부사가 오면 동사를 꾸며 동작의 방식을 나타내고(3형식), 형용사가 오면 목적어의 상태를 설명하는 목적격 보어가 된다(5형식).",
  n=["(A)와 (B)의 설명이 서로 바뀌었으므로", "(B)의 easy는 책의 내용이 쉽다는 뜻이라 두 문장의 뜻이 다르므로", "(A)의 easily는 found를 꾸미는 부사, (B)의 easy는 목적어 the book을 설명하는 목적격 보어라고 바르게 설명했으므로",
     "(A)가 3형식, (B)가 5형식이라 설명이 반대이므로", "(A)의 easily가 수식어, (B)의 easy가 목적격 보어라 설명이 반대이므로"],
  st="① 두 문장에서 다른 곳은 끝의 한 단어뿐이다: {0}. → ② 부사({1})는 동사를 꾸며 ‘어떻게 했는지’를, 형용사({2})는 목적어가 ‘어떠한지’를 나타낸다. 그래서 (A)는 3형식, (B)는 5형식이다. → ③ 품사, 문장 형식, 뜻을 서로 뒤바꾼 보기를 지운다. 정답은 {n}.",
  R=("(A) easily, (B) easy", "easily", "easy"), B=("(A) easily, (B) crowded", "easily", "crowded"), C=("(A) quietly, (B) empty", "quietly", "empty"),
  D=("(A) carefully, (B) white", "carefully", "white"), E=("(A) easily, (B) wet", "easily", "wet"), F=("(A) carefully, (B) creative", "carefully", "creative"))
