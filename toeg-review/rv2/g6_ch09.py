# 6급 CH9 현재진행형 (81~90) 2차 감수
X(6, 81, r="-ing형 만들기: 대부분 그대로 -ing, -e로 끝나면 e를 빼고(give → giving), 단모음 + 단자음이면 자음을 겹쳐 쓰고(run → running), -ie는 y로 바꾼다(lie → lying).",
  n=["그대로 -ing를 붙인 옳은 형태이므로", "그대로 -ing를 붙인 옳은 형태이므로", "-e로 끝나 e를 빼고 giving으로 써야 하므로", "e를 빼고 -ing를 붙인 옳은 형태이므로", "그대로 -ing를 붙인 옳은 형태이므로"],
  st="① 동사의 끝을 본다: -e인지, 단모음 + 단자음인지, -ie인지. → ② 규칙대로 되었는지 본다. {0} → ③ 정답은 {a}.",
  R="give는 -e로 끝나므로 giving이다.", B="make는 -e로 끝나므로 making이다.", C="run은 단모음 + 단자음이므로 running이다.", D="lie는 -ie로 끝나므로 lying이다.", E="swim은 단모음 + 단자음이므로 swimming이다.",
  F="jog는 단모음 + 단자음이므로 jogging이다.")
RV(6, 81, "F", v="수정(내용)", why="정답 ③ 유일 확인. 다만 정답 짝(run - runing)이 C의 정답 짝과 똑같다(유형 간 중복).", fix="정답 짝을 다른 동사로")

X(6, 82, r="‘지금 ~하고 있다’는 현재진행형 am/is/are + 동사원형-ing로 쓴다.",
  n=["be동사와 -ing형이 없으므로", "is 뒤에 동사원형 read를 쓸 수 없으므로", "is + reading으로 바르게 옮겼으므로", "be동사가 빠졌으므로", "being이 아니라 is를 써야 하므로"],
  st="① ‘{0}’ → 지금 진행 중인 일이므로 be동사 + -ing형이 필요하다. → ② 주어({1})에 맞는 be동사는 {2}, -ing형은 {3}. → ③ 둘 다 갖춘 문장은 {n}.",
  R=("읽고 있다", "He", "is", "reading"), B=("요리하고 있다", "Mina", "is", "cooking"), C=("그리고 있다", "I", "am", "drawing"), D=("기다리고 있다", "They", "are", "waiting"),
  E=("뛰고 있다", "The children", "are", "running"), F=("쓰고 있다", "She", "is", "writing"))

X(6, 83, r="현재진행형 의문문은 be동사 + 주어 + -ing ~?이고(Do를 쓰지 않는다), be동사는 주어에 맞춘다(I am / 단수 is / 복수·you are).",
  n=["they에 Are, My mom에 is cutting이 알맞으므로", "둘째 문장에 be동사가 빠졌고 cuting은 철자도 틀리므로", "they에 Is를 쓸 수 없고 둘째 문장도 틀리므로", "주어 they에는 Is가 아니라 Are를 써야 하므로", "they에 Am을 쓸 수 없고 My mom에 are도 쓸 수 없으므로"],
  st="① 첫 문장: 뒤에 -ing형이 있으므로 be동사로 묻는다. 주어가 {0}. → ② 둘째 문장: 주어가 {1}. → ③ 정답은 {a}.",
  R=("they(복수)이므로 Are", "My mom(단수)이므로 is cutting"), B=("he(단수)이므로 Is", "Jane(단수)이므로 is cooking"), C=("the boys(복수)이므로 Are", "I이므로 am writing"), D=("he(단수)이므로 Is", "The boys(복수)이므로 are playing"),
  E=("she(단수)이므로 Is", "I이므로 am writing"), F=("you이므로 Are", "We이므로 are cleaning"))
RV(6, 83, "BC", fx=True, why="정답의 짜임(B: Are - is cooking, C: Are - is writing)이 원문항 정답(Are - is cutting)과 같고 B는 정답 위치도 같았다. 수정 예시에서 문장의 주어를 바꿔 정답 조합이 원문항과 다르게 했다(B: Is - is cooking, C: Are - am writing).")

X(6, 84, r="현재진행형 질문과 대답은 주어와 be동사가 짝을 이룬다: Are you ~? — I am / we are, Is he(she, it) ~? — he(she, it) is, Are they ~? — they are.",
  n=["Ben은 he로 받으므로", "the cats는 they로 받으므로", "it으로 받으므로", "you(너희)에 대한 질문이라 we로 답할 수 있으므로", "Were로 물으면 weren't로 답해야 하므로"],
  st="① 대답의 주어와 be동사를 본다: {0}. → ② 이 주어로 답하게 되는 질문의 주어를 거꾸로 찾는다: {1}. 시제도 현재여야 한다. → ③ 정답은 {n}.",
  R=("we aren't", "you(너희)"), B=("they aren't", "여럿을 가리키는 the kids"), C=("she isn't", "여자 한 명인 Mina"), D=("he is", "남자 한 명인 your brother"), E=("I am not", "you"), F=("it isn't", "사물인 the washing machine"))

X(6, 85, r="have(가지고 있다), know, like, own, belong처럼 상태를 나타내는 동사는 진행형으로 쓰지 않는다. have가 ‘먹다, 시간을 보내다’의 뜻이면 진행형으로 쓸 수 있다.",
  n=["동작을 진행형으로 바르게 썼으므로", "동작을 진행형으로 바르게 썼으므로", "have a good time(즐거운 시간을 보내다)은 동작이라 진행형이 가능하므로", "‘가지고 있다’는 상태의 have는 진행형으로 쓰지 않으므로(He has ~)", "진행형 의문문을 바르게 썼으므로"],
  st="① 문장마다 동사가 동작인지 상태인지 가른다. → ② 상태 동사(소유의 have, know, like, own, belong)를 be + -ing로 쓴 문장을 찾는다. → ③ {0} 정답은 {n}.",
  R="④의 have는 ‘가지고 있다’는 상태다. ③의 have는 ‘보내다’라는 동작이다.", B="③의 have는 ‘가지고 있다’는 상태다. ①·⑤의 have는 동작이다.", C="①의 know는 상태다. ⑤의 have는 ‘먹다’라는 동작이다.",
  D="②의 belong은 상태다. ①의 have는 ‘먹다’라는 동작이다.", E="⑤의 like는 상태다. ③의 have는 동작이다.", F="④의 own은 상태다. ②의 have는 ‘먹다’라는 동작이다.")
RV(6, 85, "C", fx=True, why="⑤(I am having a great time.)가 원문항 ③(I am having a good time.)과 거의 같다. 수정 예시에서 다른 문장(Dad is having breakfast.)으로 바꿨다.")

X(6, 86, r="현재진행형은 am/is/are + 동사원형-ing다. be동사 뒤에 동사원형, -s형, to부정사를 쓰지 않는다.",
  n=["am 뒤에 동사원형을 쓸 수 없으므로", "am 뒤에 -s형을 쓸 수 없으므로", "am + reading으로 ‘읽고 있다’가 되므로", "to부정사는 진행의 뜻이 되지 않으므로", "readed라는 형태는 없으므로"],
  st="① 빈칸 앞에 be동사({0})가 있다. → ② be동사 뒤에서 ‘~하고 있다’를 만드는 것은 -ing형뿐이다. be동사를 또 쓴 것(is ~ing)도 지운다. → ③ 정답은 {a}.",
  R="am", B="is", C="are", D="is", E="is", F="are")

X(6, 87, r="현재진행형 의문문은 be동사를 주어 앞으로 옮긴다: Am/Is/Are + 주어 + -ing ~? Do/Does는 쓰지 않는다.",
  n=["Are + we + drawing으로 바르게 바꿨으므로", "진행형 의문문에 Do를 쓰지 않으므로", "평서문 어순에 물음표만 붙였으므로", "주어 we에 Am을 쓸 수 없으므로", "주어 we에 Is를 쓸 수 없으므로"],
  st="① 문장의 be동사({0})를 주어({1}) 앞으로 옮긴다. → ② 나머지(-ing형부터)는 그대로 둔다. → ③ {0} {1} ~?의 꼴은 {n}.",
  R=("Are", "we"), B=("Am", "I"), C=("Is", "she"), D=("Is", "Mina"), E=("Are", "they"), F=("Is", "Tom"))

X(6, 88, r="현재진행형은 주어 + am/is/are + 동사원형-ing다. be동사는 주어에 맞춘다(복수 주어 → are).",
  n=["two 뒤의 복수형이라 옳으므로", "복수 주어 The two birds에는 are를 써야 하므로", "be동사 뒤의 -ing형이라 옳으므로", "위치를 나타내는 전치사라 옳으므로", "전치사 뒤의 명사구라 옳으므로"],
  st="① 주어를 본다: {0}. → ② be동사와 그 뒤의 동사 형태를 차례로 확인한다. {1} → ③ 정답은 {n}.",
  R=("The two birds(복수)", "복수 주어에 is를 썼다. are여야 한다."), B=("She(3인칭 단수)", "She에 are를 썼다. is여야 한다."), C=("I", "I에 is를 썼다. am이어야 한다."), D=("Mina", "is는 맞지만 그 뒤가 read다. reading이어야 한다."),
  E=("The girls(복수)", "are는 맞지만 그 뒤가 sing이다. singing이어야 한다."), F=("The dog(단수)", "단수 주어에 are를 썼다. is여야 한다."))

X(6, 89, r="What ~ doing?에는 현재진행형(be동사 + -ing)으로 답한다. be동사는 주어에 맞추고, -e로 끝나는 동사는 e를 빼고 -ing를 붙인다(move → moving).",
  n=["She에 is, move의 -ing형 moving이 알맞으므로", "주어 She에 are를 쓸 수 없으므로", "move의 -ing형은 e를 뺀 moving이므로", "She에 am을 쓸 수 없고 be동사 뒤에 move도 쓸 수 없으므로", "is 뒤에 moves를 쓸 수 없으므로"],
  st="① 질문이 진행형(What ~ doing?)이므로 대답도 be동사 + -ing다. → ② (A): 주어 {0}. (B): {1}. → ③ 정답은 {n}.",
  R=("She에 맞는 is", "move → moving"), B=("We에 맞는 are", "clean → cleaning"), C=("He에 맞는 is", "fix → fixing"), D=("They에 맞는 are", "decorate → decorating"), E=("They에 맞는 are", "play → playing"),
  F=("You에 맞는 are", "read → reading"))

X(6, 90, r="현재진행형 부정문은 be동사 + not + -ing다. not은 be동사 바로 뒤에 오고, is not은 isn't, are not은 aren't로 줄여 쓴다.",
  n=["not은 ‘~하고 있지 않다’는 부정의 뜻을 만들므로", "not이 are 뒤, listening 앞에 오고 aren't로 줄일 수 있으므로", "not은 문장 맨 앞이 아니라 be동사 뒤에 오므로", "진행형 부정문에 don't를 쓸 수 없으므로", "not 뒤에도 -ing형을 그대로 쓰므로"],
  st="① 문장에서 not의 자리를 확인한다: {0}. → ② 설명마다 뜻(부정), 자리(be동사 뒤), 줄임꼴, 다른 말로 바꿀 수 있는지를 대어 본다. → ③ {1} 정답은 {n}.",
  R=("are + not + listening", "② 자리와 줄임꼴(aren't)을 바르게 말했다."), B=("is + not + sleeping", "① 자리와 줄임꼴(isn't)을 바르게 말했다."), C=("is + not + reading", "② 자리, 뜻, 줄임꼴(isn't)을 바르게 말했다."),
  D=("are + not + playing", "③ 자리와 줄임꼴(aren't)을 바르게 말했다."), E=("is + not + watching", "④ 자리와 줄임꼴(isn't)을 바르게 말했다."), F=("am + not + studying", "⑤ 자리와 뜻을 바르게 말했다. am not은 amn't로 줄이지 않는다."))
RV(6, 90, "BC", v="수정(내용)", why="정답 유일 확인. 다만 오답이 문장과 관계없는 한 줄짜리 일반 규칙(‘not은 문장 맨 앞에만 온다’, ‘현재진행형 부정문에는 do not을 쓴다’ 등)이고 정답만 길게 문장을 짚어 설명해서, 길이만 보아도 답이 드러난다. B와 C의 오답도 서로 겹친다. 원문항의 오답은 문장을 짚는 설명이다.", fix="오답을 문장을 짚는 설명으로")
