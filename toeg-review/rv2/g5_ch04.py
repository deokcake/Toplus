# 5급 CH4 현재진행형 (31~40) 2차 감수
X(5, 31, r="-ing형 만들기: 대부분 그대로 -ing, -e로 끝나면 e를 빼고(make → making), -ie는 y로 바꾸고(tie → tying), 단모음 + 단자음으로 끝나면 자음을 한 번 더 쓴다(sit → sitting).",
  n=["-ie를 y로 바꾸고 -ing를 붙인 옳은 형태이므로", "단모음 + 단자음으로 끝나 t를 한 번 더 써서 sitting으로 써야 하므로", "m을 한 번 더 쓴 옳은 형태이므로", "y로 끝나면 그대로 -ing를 붙이므로", "t를 한 번 더 쓴 옳은 형태이므로"],
  st="① 동사의 끝소리를 본다: -e, -ie, 단모음 + 단자음 가운데 어느 것인지 가른다. → ② {0} → ③ 정답은 {a}.",
  R="sit은 단모음 + 단자음이라 sitting이다. 나머지는 규칙대로다.", B="lie는 -ie로 끝나 lying이다. 나머지는 규칙대로다.", C="run은 단모음 + 단자음이라 running이다. 나머지는 규칙대로다.", D="make는 -e로 끝나 making이다. 나머지는 규칙대로다.",
  E="come은 -e로 끝나 e만 빼므로 coming이다. m을 겹쳐 쓰지 않는다.", F="swim은 단모음 + 단자음이라 swimming이다. 나머지는 규칙대로다.")

X(5, 32, r="‘~하고 있다’는 현재진행형 am/is/are + 동사원형-ing로 쓴다. be동사는 주어에 맞춘다.",
  n=["is + winning으로 ‘이기고 있다’를 바르게 나타냈으므로", "is 뒤에 동사원형 win을 쓸 수 없으므로", "win의 -ing형은 n을 한 번 더 써서 winning이므로", "be동사가 빠졌으므로", "현재형이라 ‘이기고 있다’는 뜻이 되지 않고 3인칭 단수 -s도 없으므로"],
  st="① 우리말 ‘{0}’ → 지금 진행 중인 일이므로 be동사 + -ing형을 쓴다. → ② 주어({1})에 맞는 be동사는 {2}, -ing형은 {3}. → ③ be동사가 빠지거나 동사 형태·철자·시제가 틀린 문장을 지운다. 정답은 {n}.",
  R=("이기고 있다", "His team", "is", "winning"), B=("달리고 있다", "The children", "are", "running"), C=("쓰고 있다", "Jane", "is", "writing"), D=("하고 있다", "They", "are", "playing"),
  E=("읽고 있다", "I", "am", "reading"), F=("청소하고 있다", "We", "are", "cleaning"))
RV(5, 32, "C", v="수정(내용)", why="정답 확인. 다만 오답 ④의 writ(Jane is writ a letter.)는 쓰이지 않는 형태라 그것만 보고 지워진다. 원문항의 철자 오답은 -ing형을 잘못 쓴 것(wining)이다.", fix="④를 -ing형 철자 오류(writeing)로")

X(5, 33, r="현재진행형의 be동사는 주어에 맞춘다(I am / 단수 is / 복수·you are). 부정문은 be동사 뒤에 not, 의문문은 be동사를 주어 앞에 둔다.",
  n=["Scott(단수)에 is not + -ing를 바르게 썼으므로", "주어 the kids가 복수라 Are를 써야 하므로", "you에 Are를 바르게 썼으므로", "He에 isn't + -ing를 바르게 썼으므로", "They에 are + -ing를 바르게 썼으므로"],
  st="① 문장마다 주어를 찾아 be동사(am/is/are)가 맞는지 본다. 의문문의 주어는 be동사 뒤에 있다. → ② not의 자리, -ing형, be동사 대신 do/does를 쓰지 않았는지도 본다. → ③ {0} 정답은 {n}.",
  R="②의 주어 the kids는 복수인데 Is를 썼다.", B="④의 주어 Mina는 단수인데 Are를 썼다.", C="⑤의 주어 My brother는 단수인데 are를 썼다.", D="③은 not이 be동사 앞에 있다(is not singing).",
  E="①의 주어 Mina and Tom은 복수인데 is를 썼다.", F="②는 진행형 의문문을 Does로 시작했다(Is Jane cooking ~?).")

X(5, 34, r="진행형 의문문(Be동사 + 주어 + -ing ~?)에는 be동사로 답한다: Yes, 주어 + be동사. / No, 주어 + be동사 + not. 대답의 주어는 질문의 주어를 대명사로 받는다.",
  n=["be동사 의문문에 do로 답할 수 없으므로", "the kids를 they로 받고 are로 답했으므로", "the kids는 he로 받을 수 없으므로", "현재의 질문에 과거형 weren't로 답할 수 없으므로", "they에 was를 쓸 수 없고 시제도 맞지 않으므로"],
  st="① 질문의 be동사와 주어를 본다: {0}. → ② 대답의 주어는 {1}, 동사는 질문과 같은 현재형 be동사다. do/does나 was/were로 답한 것을 지운다. → ③ 정답은 {a}",
  R=("Are the kids ~?", "they"), B=("Is Tom ~?", "he"), C=("Is Jane ~?", "she"), D=("Are you ~?", "I"), E=("Is Tom ~?", "he"), F=("Are we ~?", "we"))
RV(5, 34, "F", fx=True, why="질문 ‘Are we late?’는 진행형이 아니라 be동사 의문문이어서 이 단원(현재진행형)과 맞지 않는다. 수정 예시의 질문도 그대로였으므로 진행형 질문(Are we walking too fast?)으로 바꿨다.")

X(5, 35, r="현재진행형은 am/is/are + 동사원형-ing다. 부정문은 be동사 + not + -ing, 의문문은 be동사 + 주어 + -ing ~?이다.",
  n=["dance의 -ing형은 e를 빼고 dancing이므로", "He에 isn't + walking을 바르게 썼으므로", "Is he 뒤에는 play가 아니라 playing을 써야 하므로", "not은 be동사 뒤에 두어 am not으로 써야 하므로", "주어 We에는 are를 써야 하고 partners도 복수로 써야 하므로"],
  st="① 문장마다 세 가지를 본다: 주어와 be동사의 짝, be동사 뒤가 -ing형인지(철자 포함), not의 자리. → ② 하나라도 어긋난 문장을 지운다. → ③ {0} 정답은 {n}.",
  R="②만 isn't + walking으로 바르다.", B="②만 aren't + waiting으로 바르다.", C="⑤만 aren't + playing으로 바르다.", D="③만 is + washing으로 바르다.", E="④만 Is + 주어 + sleeping으로 바르다.", F="①만 am not + wearing으로 바르다.")
RV(5, 35, "B", v="수정(내용)", why="정답 ② 유일 확인. 다만 정답 문장(We aren't waiting for the bus.)과 같은 문장의 틀린 형태(③ We don't waiting for the bus.)가 함께 있어 둘만 견주면 답이 나온다. 발문도 원문항과 다르다.", fix="③을 다른 문장으로, 발문을 원문항대로")
RV(5, 35, "C", v="수정(내용)", why="정답 ⑤ 유일 확인. 다만 정답 문장(They aren't playing soccer.)과 거의 같은 문장의 틀린 형태(④ They isn't playing.)가 함께 있고, 오답이 두세 단어짜리 문장이라 원문항(네 단어~일곱 단어)보다 짧다. D~F와 같은 문제다.", fix="짝 문장을 없애고 문장을 원문항 길이로")

X(5, 36, r="‘~하고 있다’는 be동사 + 동사원형-ing로 쓴다. be동사 뒤에 동사원형·현재형·과거형을 쓸 수 없다.",
  n=["is 뒤에 동사원형을 쓸 수 없으므로", "is 뒤에 현재형 sleeps를 쓸 수 없으므로", "is + sleeping이 ‘자고 있다’의 뜻이 되므로", "sleepes라는 형태는 없으므로", "과거형이라 is 뒤에 쓸 수 없으므로"],
  st="① 빈칸 앞에 be동사({0})가 있고, 우리말은 ‘{1}’이다. → ② be동사 뒤에서 진행의 뜻을 만드는 것은 -ing형뿐이다. → ③ 정답은 {a}.",
  R=("is", "잠을 자고 있다"), B=("is", "그림을 그리고 있다"), C=("is", "편지를 쓰고 있다"), D=("are", "축구를 하고 있다"), E=("am", "책을 읽고 있다"), F=("are", "방을 청소하고 있다"))

X(5, 37, r="진행형 의문문은 be동사 + 주어 + -ing ~?이고, 대답도 be동사로 한다. be동사는 각 문장의 주어에 맞춘다.",
  n=["the bus(단수)에 Is, 대답의 it에도 is가 알맞으므로", "the bus는 단수라 Are를 쓸 수 없으므로", "be동사 의문문에 does로 답할 수 없으므로", "the bus는 단수라 Are를 쓸 수 없으므로", "뒤에 -ing형 coming이 있어 Does로 시작할 수 없으므로"],
  st="① 첫 빈칸: 뒤에 -ing형이 있으므로 be동사가 필요하다. 주어가 {0}. → ② 둘째 빈칸: 대답의 주어가 {1}. → ③ 정답은 {a}.",
  R=("the bus(단수)이므로 Is", "it이므로 is"), B=("the girls(복수)이므로 Are", "they이므로 are"), C=("the boys(복수)이므로 Are", "they이므로 are"), D=("Jane(단수)이므로 Is", "she이고 No로 답했으므로 isn't"),
  E=("you이므로 Are", "I이므로 am"), F=("we이므로 Are", "we이고 No로 답했으므로 aren't"))

X(5, 38, r="현재진행형 의문문은 Am/Is/Are + 주어 + 동사원형-ing ~?이다. Do/Does로 시작하지 않고, 평서문 어순에 물음표만 붙이지 않는다.",
  n=["진행형 의문문은 Do가 아니라 be동사로 시작하므로", "Are they 뒤에는 play가 아니라 playing을 써야 하므로", "Are + they + playing으로 바르게 썼으므로", "주어 they에는 Are를 써야 하므로", "평서문 어순에 물음표만 붙였으므로"],
  st="① ‘~하고 있니?’ → 진행형 의문문이므로 be동사로 시작한다. → ② 주어 {0}에 맞는 be동사는 {1}, 뒤의 동사는 {2}. → ③ {1} {0} {2} ~?의 순서인 것을 고른다. 정답은 {n}.",
  R=("they", "Are", "playing"), B=("she", "Is", "writing"), C=("Jane", "Is", "reading"), D=("you", "Are", "studying"), E=("Tom", "Is", "watching"), F=("we", "Are", "cleaning"))

X(5, 39, r="현재진행형(be동사 + -ing)은 지금 진행 중인 일을 나타낸다. 날씨를 말할 때의 it은 뜻이 없는 비인칭 주어다. 의문문은 be동사를 주어 앞에 둔다.",
  n=["날씨를 나타내는 비인칭 주어 it을 바르게 설명했으므로", "at the moment의 뜻과 쓰임을 바르게 설명했으므로", "rain은 날씨에만 쓰는 동사라 사람(I)을 주어로 쓸 수 없으므로", "진행형의 구조와 뜻을 바르게 설명했으므로", "be동사를 앞에 둔 의문문을 바르게 만들었으므로"],
  st="① 제시문의 주어·be동사·-ing형을 먼저 확인한다: {0}. → ② 설명을 하나씩 문장에 대어 본다. 문장을 바꾸는 설명은 실제로 바꿔 써 본다. → ③ {1} 정답은 {n}.",
  R=("It / is / raining", "‘I am raining’은 뜻이 통하지 않는다. rain의 주어는 비인칭 it이어야 한다."), B=("It / is / snowing", "의문문은 be동사를 앞에 두어 Is it snowing ~?이다. Does를 쓰지 않는다."),
  C=("The wind / is / blowing", "blowing은 과거형이 아니라 -ing형이다(과거형은 blew)."), D=("Jane / is / reading", "be동사 없이 -ing형만으로는 진행형이 되지 않는다."),
  E=("They / are / playing", "주어를 Tom으로 바꾸면 be동사도 is로 바꿔야 한다."), F=("I / am / studying", "지난 일은 am을 was로 바꿔 was studying으로 쓴다."))
RV(5, 39, "B", v="수정(내용)", why="정답 ④ 유일 확인. 다만 정답 설명만 다른 보기의 두 배쯤 길고, ②(날씨를 나타내는 비인칭주어 it)와 서로 어긋나는 내용이라 둘만 견주면 답이 나온다. 원문항은 다섯 설명의 길이가 고르다.", fix="④를 길이가 비슷한 틀린 설명으로")
RV(5, 39, "C", v="수정(내용)", why="정답 ③ 유일 확인. 다만 제시문(It is snowing now.)이 B(It is snowing heavily outside.)와 거의 같은 문장이고 원문항(It is raining ~)과도 같은 짜임이다(유형 간 중복).", fix="제시문을 다른 문장으로")
RV(5, 39, "EF", v="수정(내용)", why="정답 확인. 다만 틀린 설명이 ‘They is playing now.는 올바른 문장이다’, ‘I is studying now.는 올바른 문장이다’여서 바로 옆 보기(They는 복수 주어이므로 are / I와 함께는 am)만 보아도 답이 나오고, E와 F가 같은 꼴이다. 원문항의 틀린 설명은 문장을 바꿔 생각해 보아야 가려진다.", fix="틀린 설명을 주어·시제를 바꾸는 내용으로")

X(5, 40, r="현재진행형은 am/is/are + 동사원형-ing다. be동사 뒤에 동사원형이나 -s형을 쓰지 않는다.",
  pre=["문장별 판정: (가) O. are + singing. (나) X. is 뒤에는 comes가 아니라 coming. (다) X. am 뒤에는 study가 아니라 studying. (라) O. is + making."],
  k="어법상 옳은 문장은 (가), (라)이다.", n=["(나)가 틀린 문장이므로", "(나), (다) 모두 틀린 문장이므로", "(다)가 틀린 문장이므로", "(가), (라)가 모두 옳은 문장이므로", "(나)가 틀린 문장이므로"],
  st="① 문장마다 be동사가 주어와 맞는지 본다. → ② be동사 뒤가 -ing형인지 본다. 동사원형이나 -s형이면 틀린 문장이다. → ③ {0} 옳은 문장은 {a}이다.",
  R="(나) is comes, (다) am study가 틀렸다.", B="(나) is sings, (라) The dog are가 틀렸다.", C="(나) is brushes, (라) are wait가 틀렸다.", D="(가)는 be동사가 없고, (라)는 I is가 틀렸다.",
  E="(가) are studies, (나) He are가 틀렸다.", F="(다) are clean, (라) The girls is가 틀렸다.")
RV(5, 40, "CDEF", v="수정(내용)", why="정답 확인. 다만 문장이 대부분 세 단어(I am studying. / We is cleaning.)로 원문항(다섯~일곱 단어)보다 짧고, 틀린 문장이 주로 be동사 수 일치여서 원문항(is comes, am study처럼 be동사 뒤의 동사 형태)과 다르다. D·E·F는 정답 조합이 모두 (가), (나)다.", fix="문장을 원문항 길이로, 오류 종류와 정답 조합을 고르게")
