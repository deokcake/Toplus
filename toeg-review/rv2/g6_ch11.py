# 6급 CH11 명령문과 제안문 (101~110) 2차 감수
X(6, 101, r="명령문은 주어(You) 없이 동사원형으로 시작한다.",
  n=["-ing형으로는 명령문을 시작할 수 없으므로", "-s형으로는 명령문을 시작할 수 없으므로", "동사원형 Tell로 시작하므로", "과거형으로는 명령문을 시작할 수 없으므로", "Telled라는 형태는 없으므로"],
  st="① 우리말이 ‘{0}’라고 시키는 말이다. 명령문이다. → ② 명령문의 첫 낱말은 동사원형이다. -s형, -ing형, to부정사, 과거형, Does를 붙인 것을 지운다. → ③ 정답은 {a}.",
  R="말해줘", B="보여 줘", C="따라와", D="전화해", E="도와줘", F="닫아라")
RV(6, 101, "BCDE", fx=True, why="변형의 보기에 ‘To Show’, ‘Does Show’처럼 둘째 낱말까지 대문자로 쓴 표기가 있다. 수정 예시에서 ‘To show’, ‘Does show’로 바로잡았다.")

X(6, 102, r="부정 명령문은 Don't + 동사원형이다. be동사도 원형 be를 쓴다(Don't be late).",
  n=["동사원형이라 Don't 뒤에 쓸 수 있으므로", "동사원형으로 시작해 Don't 뒤에 쓸 수 있으므로", "Don't 뒤에는 is가 아니라 be를 써야 하므로", "동사원형으로 시작해 Don't 뒤에 쓸 수 있으므로", "동사원형으로 시작해 Don't 뒤에 쓸 수 있으므로"],
  st="① Don't 뒤에는 동사원형만 온다. → ② 보기마다 첫 낱말이 동사원형인지 본다. → ③ {0} 정답은 {n}.",
  R="③의 is는 be의 현재형이다(Don't be late).", B="④의 forgets는 -s형이다(Don't forget ~).", C="②의 runs는 -s형이다(Don't run ~).", D="⑤의 are는 be의 현재형이다(Don't be noisy).", E="①의 to eat은 to부정사다(Don't eat ~).",
  F="③의 being은 -ing형이다(Don't be rude).")

X(6, 103, r="제안 표현마다 뒤의 형태가 다르다: How about/What about + -ing?, Shall we/Why don't we + 동사원형?, Let's + 동사원형.",
  n=["Let's 뒤에는 동사원형을 쓰므로", "Why don't 뒤에 주어 we가 있어야 하고 동사원형을 쓰므로", "Let's not 뒤에는 동사원형을 쓰므로", "How about + -ing로 제안을 나타내므로", "Shall we not 뒤에는 동사원형을 쓰므로"],
  st="① 빈칸 뒤의 형태를 본다: {0}. → ② 그 형태와 함께 쓰는 제안 표현은 {1}. → ③ 정답은 {a}.",
  R=("going(-ing형)과 물음표", "How about"), B=("opening(-ing형)과 물음표", "What about(How about)"), C=("take(동사원형)와 물음표, we가 없음", "Shall we"), D=("walk(동사원형)와 마침표", "Let's"),
  E=("we + play(동사원형)와 물음표", "Why don't"), F=("making(-ing형)과 물음표", "How about"))
RV(6, 103, "BCDE", v="수정(내용)", why="정답 유일 확인. 다만 B~F 다섯 유형의 정답이 모두 원문항과 같은 How about이다. 같은 단원 109번에서 고친 것과 같은 문제다(C4).", fix="제안 표현과 빈칸 뒤의 형태를 바꿔 정답을 유형마다 다르게")

X(6, 104, r="Let's/Shall we/Why don't we 뒤에는 동사원형, How about/What about 뒤에는 -ing형, Don't/Never 뒤에는 동사원형을 쓴다.",
  n=["Shall we + 동사원형으로 옳으므로", "What about 뒤에는 wear가 아니라 wearing을 써야 하므로", "Never + 동사원형으로 옳으므로", "Don't + be로 옳으므로", "Let's + 동사원형으로 옳으므로"],
  st="① 문장마다 첫머리의 표현을 본다. → ② 그 뒤가 동사원형이어야 하는지 -ing형이어야 하는지 맞춰 본다. → ③ {0} 정답은 {n}.",
  R="②는 What about 뒤에 동사원형 wear를 썼다.", B="③은 How about 뒤에 동사원형 play를 썼다.", C="②는 What about 뒤에 to eat을 썼다.", D="④는 Let's 뒤에 playing을 썼다.", E="⑤는 Shall we 뒤에 going을 썼다.",
  F="③은 Let's 뒤에 to take를 썼다.")
RV(6, 104, "B", v="수정(내용)", why="정답 ③ 유일 확인. 다만 정답 문장(How about play soccer?)과 내용이 같은 옳은 문장(② Let's play soccer.)이 함께 있고, ④(How about wearing this jacket?)는 원문항 정답(What about wear this jacket?)을 바르게 고친 문장이다. C~E가 이 오답을 되풀이한다.", fix="②·④를 다른 문장으로")

X(6, 105, r="‘~하지 말자’는 Let's not + 동사원형 + 나머지의 순서다. 명령문은 (Please) + 동사원형으로 시작한다.",
  n=["Let's는 첫 번째 낱말이므로", "not은 두 번째 낱말이므로", "Let's not 다음 세 번째에 동사원형 play가 오므로", "the는 네 번째 낱말이므로", "guitar는 다섯 번째 낱말이므로"],
  st="① 문장을 완성한다: {0} → ② 앞에서부터 센다. → ③ 세 번째 낱말은 {a}. 정답은 {n}.",
  R="Let's not play the guitar.", B="Let's not eat lunch here.", C="Let's not open the door.", D="Let's not take a taxi.", E="Please be quiet in class.", F="Let's not watch TV now.")
RV(6, 105, "D", v="수정(내용)", why="정답 ③ 유일 확인. 다만 정답 낱말(play)과 정답 위치(③)가 원문항과 똑같다. 발문도 첫 두 단어를 알려 준다.", fix="낱말을 새로, 발문을 원문항대로")

X(6, 106, r="be동사의 명령문은 원형 Be로 시작한다(Be + 형용사).",
  n=["be동사의 원형 Be로 시작하므로", "Is로는 명령문을 시작할 수 없으므로", "Am으로는 명령문을 시작할 수 없으므로", "Are로는 명령문을 시작할 수 없으므로", "-ing형으로는 명령문을 시작할 수 없으므로"],
  st="① 빈칸 뒤가 형용사({0})이고 주어가 없다. be동사의 명령문이다. → ② 명령문은 동사원형으로 시작하므로 am/is/are가 아니라 Be다. → ③ 정답은 {n}.",
  R="kind", B="quiet", C="polite", D="honest", E="careful", F="patient")

X(6, 107, r="부정 명령문은 Don't + 동사원형이다. Please가 붙어도 같다.",
  n=["don't 뒤에 동사원형 draw를 썼으므로", "don't 뒤에 -s형을 쓸 수 없으므로", "don't 뒤에 to부정사를 쓸 수 없으므로", "don't 뒤에 과거분사를 쓸 수 없으므로", "don't 뒤에 과거형을 쓸 수 없으므로"],
  st="① 밑줄 앞의 don't(Don't)를 본다. → ② don't 뒤는 동사원형이다. 밑줄 친 {0}의 원형을 찾는다. → ③ 정답은 {a}.",
  R="drawing", B="to open", C="running", D="shouts", E="to touch", F="throwing")
RV(6, 107, "F", v="수정(내용)", why="정답 ④ 유일 확인. 다만 정답 낱말(touch)이 E와 같고 문장(Please don't touching it. / Don't to touch the wet paint.)도 비슷하다(유형 간 중복).", fix="동사를 바꿈")

X(6, 108, r="Let's + 동사원형, Shall we + 동사원형 ~?, Why don't we + 동사원형 ~?, How about + -ing ~?",
  n=["Let's + 동사원형, Shall we ~?로 알맞으므로", "Shall eat이라고 쓸 수 없고 Let's we도 쓸 수 없으므로", "Do we have pizza?는 제안이 아니므로", "Are we have라고 쓸 수 없으므로", "Shall eat이라고 쓸 수 없으므로"],
  st="① (A) 뒤를 본다: {0}. → ② (B) 뒤를 본다: {1}. → ③ 정답은 {n}.",
  R=("eat(동사원형), 마침표 → Let's", "we have ~? → Shall"), B=("watching(-ing형), 물음표 → How about", "go(동사원형), 마침표 → Let's"), C=("go(동사원형), 물음표 → Why don't we", "take(동사원형), 마침표 → Let's"),
  D=("play(동사원형), 마침표 → Let's", "starting(-ing형), 물음표 → How about"), E=("we turn ~? → Shall", "open(동사원형), 마침표 → Let's"), F=("taking(-ing형), 물음표 → How about", "we sit ~? → Shall"))
RV(6, 108, "E", fx=True, why="수정 예시의 오답 ④((A) Do - (B) Let's)는 ‘Do we turn on the light?’가 문법으로는 옳은 문장이라 헷갈릴 수 있었다. 분명히 틀린 조합((A) Are)으로 바꿨다.")

X(6, 109, r="Let's + 동사원형 = How about/What about + -ing? = Shall we/Why don't we + 동사원형?",
  n=["Shall we 뒤에는 동사원형을 쓰므로", "Can we 뒤에는 동사원형을 쓰고 뜻도 다르므로", "How about + -ing로 Let's와 같은 제안이 되므로", "Why don't 뒤에는 we + 동사원형이 와야 하므로", "Do you 뒤에는 동사원형을 쓰고 뜻도 다르므로"],
  st="① Let's ~는 ‘~하자’는 제안이다. 같은 뜻의 제안 표현을 찾는다. → ② 빈칸 뒤의 형태를 본다: {0}. → ③ 그 형태와 맞는 것은 {a}.",
  R="playing(-ing형)", B="eating(-ing형)", C="take(동사원형)", D="go(동사원형)", E="we watch(주어 + 동사원형)", F="빈칸이 Why don't we 바로 뒤의 동사 자리")

X(6, 110, r="Let's + 동사원형, 부정은 Let's not + 동사원형. be동사도 원형 be를 쓴다. Let's 뒤의 동사에는 -s를 붙이지 않는다.",
  pre=["<보기> 판정: ㄱ O. Let's not be quiet처럼 not은 Let's와 be 사이에 온다. ㄴ O. be는 형용사 quiet 앞의 동사원형이다. ㄷ X. Let's 뒤에는 언제나 동사원형을 쓴다."],
  k="옳은 설명은 ㄱ, ㄴ이다.", n=["ㄴ도 옳은 설명이므로", "ㄱ도 옳은 설명이므로", "ㄷ은 틀린 설명이므로", "ㄷ은 틀린 설명이므로", "ㄱ, ㄴ이 옳은 설명이므로"],
  st="① <보기>의 설명마다 실제로 문장을 바꿔 써 본다. → ② {0} → ③ 옳은 것만 모으면 {a}이다.",
  R="ㄱ Let's not be quiet(O), ㄴ O, ㄷ Let's turns(X).", B="ㄱ O, ㄴ 부정은 Don't be careful(X), ㄷ O.", C="ㄱ 부정은 Let's not eat(X), ㄴ O, ㄷ O.", D="ㄱ O, ㄴ How about playing(X), ㄷ we가 주어(X).",
  E="ㄱ O, ㄴ O, ㄷ Don't be quiet(O).", F="ㄱ Let's 뒤는 동사원형(X), ㄴ O, ㄷ How about taking(X).")
RV(6, 110, "E", fx=True, why="수정 예시의 ㄷ(‘(B)와 반대 뜻의 명령은 Don't be noisy처럼 …’)은 Don't be noisy가 Be quiet와 같은 뜻이어서 설명이 맞지 않았다. ‘(B)를 부정 명령문으로 바꾸면 Don't be quiet.가 된다’로 고쳤다.")
