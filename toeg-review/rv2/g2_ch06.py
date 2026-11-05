# 2급 CH6 부정사 (51~60) 2차 감수
X(2, 51, r="‘의문사 + to부정사’는 ‘~할지’라는 뜻의 명사구다: who to ~(누구를 ~할지), what to ~(무엇을), when to ~(언제), where to ~(어디서), how to ~(어떻게).",
  n=["what to invite는 ‘무엇을 초대할지’라 우리말과 맞지 않으므로", "when to invite는 ‘언제 초대할지’이므로", "who to invite가 ‘누구를 초대할지’이므로", "where to invite는 ‘어디에 초대할지’이므로", "how to invite는 ‘어떻게 초대할지’이므로"],
  st="① 우리말에서 ‘~할지’ 앞에 놓인 의문사를 찾는다: ‘{0}’. → ② 빈칸 뒤가 to부정사이므로 ‘의문사 + to부정사’ 구문이다. 그 뜻의 의문사({1})를 고른다. → ③ 정답은 {n}.",
  R=("누구를", "who"), B=("어느 길을", "which, 뒤의 명사 path를 꾸민다"), C=("어디에", "where"), D=("언제", "when"), E=("누구에게", "who"), F=("어떻게", "how"))

X(2, 52, r="It is + 형용사 + (의미상 주어) + to부정사에서 kind, brave, thoughtful, careless처럼 사람의 성품을 평가하는 형용사 뒤에는 of + 목적격을, important, necessary, hard처럼 일 자체를 판단하는 형용사 뒤에는 for + 목적격을 쓴다.",
  n=["kind는 사람의 성품을 평가하므로 of가 들어간다.", "brave는 사람의 성품을 평가하므로 of가 들어간다.", "thoughtful은 사람의 성품을 평가하므로 of가 들어간다.", "careless는 사람의 성품을 평가하므로 of가 들어간다.",
     "important는 성품이 아니라 일 자체를 판단하는 말이라 for가 들어간다. of가 들어갈 수 없다."],
  st="① 빈칸 앞 형용사가 그 일을 한 ‘사람의 성품’을 평가하는 말인지 본다. 그렇다면 of + 사람이다. → ② 성품 형용사({0})가 있는 네 문장에는 of가 들어간다. → ③ {n}의 형용사({1})는 사람이 아니라 일 자체를 판단한다. for가 들어간다.",
  R=("kind, brave, thoughtful, careless", "important"), B=("generous, clever, rude, polite", "necessary"), C=("kind, silly, thoughtful, brave", "dangerous"), D=("careless, sweet, foolish, honest", "hard"),
  E=("stupid, polite, selfish, smart", "easy"), F=("thoughtless, mean, considerate, cruel", "impossible"))
RV(2, 52, "F", fx=True, why="수정 예시의 정답 문장 ‘It is important _____ us to …’가 원문항 정답 문장(It is important _____ us to protect the environment.)과 형용사·대명사까지 같아 ‘It is impossible _____ us to finish this in an hour.’로 바꿨다.")

X(2, 53, r="to부정사는 앞의 명사를 꾸미면 형용사적 용법, 주어·목적어·보어이면 명사적 용법, 목적·감정의 원인 등을 나타내면 부사적 용법이다.",
  n=["books를 꾸미는 형용사적 용법이므로", "someone을 꾸미는 형용사적 용법이므로", "pizza를 꾸미는 형용사적 용법이므로", "‘조언을 구하려고’라는 목적을 나타내는 부사적 용법이라 나머지와 다르므로", "umbrella를 꾸미는 형용사적 용법이므로"],
  st="① 밑줄 친 to부정사가 문장에서 하는 일을 본다. 앞의 명사를 꾸미면 형용사적, 주어·목적어·보어이면 명사적, 목적·감정의 원인을 나타내면 부사적 용법이다. → ② 네 문장은 {0}. → ③ {n}만 {1}.",
  R=("바로 앞의 명사(books, someone, pizza, umbrella)를 꾸미는 형용사적 용법이다", "‘조언을 구하려고’라는 목적을 나타내는 부사적 용법이다"),
  B=("앞의 명사(homework, nothing, something, person)를 꾸미는 형용사적 용법이다", "‘빵을 사려고’라는 목적을 나타내는 부사적 용법이다"),
  C=("동사(want, decided, hope, planned)의 목적어인 명사적 용법이다", "명사 time을 꾸미는 형용사적 용법이다"),
  D=("‘~하려고’라는 목적을 나타내는 부사적 용법이다", "be동사 뒤에서 주어(Her plan)를 설명하는 보어, 곧 명사적 용법이다"),
  E=("앞의 명사(friend, time, reason, places)를 꾸미는 형용사적 용법이다", "문장의 주어로 쓰인 명사적 용법이다"),
  F=("감정 형용사(glad, sad, surprised, happy) 뒤에서 그 감정의 원인을 나타내는 부사적 용법이다", "명사 question을 꾸미는 형용사적 용법이다"))

X(2, 54, r="too + 형용사 + (for + 목적격) + to부정사는 ‘너무 ~해서 …할 수 없다’, 형용사 + enough + (for + 목적격) + to부정사는 ‘…할 만큼 충분히 ~하다’는 뜻이다.",
  n=["too scary for me to watch로 ‘내가 보기에 너무 무서웠다’를 바르게 나타냈으므로", "to부정사의 의미상 주어는 of가 아니라 for + 목적격으로 쓰므로", "enough to는 ‘볼 만큼 무서웠다’는 다른 뜻이고 of도 틀렸으므로", "‘볼 수 있다’가 되어 뜻이 반대이므로",
     "‘볼 수 있을 만큼’이라는 뜻이 되어 맞지 않으므로"],
  st="① 우리말이 ‘너무 ~해서 …할 수 없다’인지 ‘…할 만큼 충분히 ~하다’인지 가른다. {0} → ② too는 형용사 앞에, enough는 형용사 뒤에 둔다. to부정사의 의미상 주어는 그 앞에 ‘for + 목적격’으로 쓴다. → ③ of를 쓴 것, -ing를 쓴 것, 뜻이 반대인 것을 지운다. 정답은 {n}.",
  R="‘보기에 너무 무서웠다’는 too ~ to다.", B="‘너무 무거워서 들 수 없었다’는 too ~ to다.", C="‘풀기에 충분히 쉬웠다’는 형용사 + enough to다.", D="‘쓰기에 충분히 크다’는 형용사 + enough to다.",
  E="‘너무 뜨거워서 마실 수 없었다’는 too ~ to다.", F="‘이해하기에 충분히 명확했다’는 형용사 + enough to다.")

X(2, 55, r="to부정사가 꾸미는 명사가 전치사의 목적어이면 전치사를 남긴다(paper to write on). -one, -thing은 형용사가 뒤에서 꾸민다. too ~ to는 so ~ that … can't로 바꾼다. to부정사는 보어로도, 결과(grew up to be)를 나타내는 데도 쓴다.",
  pre=["학생별 판정: Zoe O(write on paper이므로 on이 필요하다). Amy X(someone kind to help 어순이 맞다). Ben O(보어로 쓰인 to부정사). Clara X(so heavy that he can't carry it으로 바꿔야 한다). Dave O(결과의 to부정사)."],
  k="올바르게 설명한 학생은 Zoe, Ben, Dave다.", n=["올바르게 설명한 학생은 Zoe, Ben, Dave이므로"] * 5,
  st="① 학생마다 예문과 설명을 따로 따진다. → ② 기준: 명사가 전치사의 목적어이면 to부정사 뒤에 전치사를 남긴다. -one·-thing은 형용사가 뒤에 온다. 성품 형용사 뒤 의미상 주어는 of다. enough는 형용사 뒤에 온다. → ③ {0} 옳게 설명한 학생만 모으면 {a}이다.",
  R="Amy는 kind someone 어순을 옳다고 했고(someone kind), Clara는 too ~ to를 enough that으로 바꿨다(so heavy that he can't carry it). 둘 다 틀렸다.",
  B="Leo는 talk to의 to를 빼야 한다고 했고, Jane은 kind for you를 맞다고 했다(kind of you). 둘 다 틀렸다.",
  C="Amy는 cold something 어순을 옳다고 했고(something cold), Jin은 nice for you를 옳다고 했으며(of you), Mina는 enough hot을 옳다고 했다(hot enough). 셋 다 틀렸다.",
  D="Ben은 talk 뒤에 전치사가 없어도 된다고 했고(talk with), Amy는 for I를 옳다고 했다(for me). 둘 다 틀렸다.",
  E="Leo는 worry about의 about을 빼야 한다고 했고, Sora는 결과를 나타내는 woke up to find를 목적으로 풀었다. 둘 다 틀렸다.",
  F="Tom은 eat 뒤에 with가 필요 없다고 했고, Jin은 foolish for me를 옳다고 했으며(of me), Leo는 enough large를 옳다고 했다(large enough). 셋 다 틀렸다.")
RV(2, 55, "E", fx=True, why="수정 예시의 정답이 네 명(Mina, Leo, Jane, Ben)이라 원문항(두세 명 조합)과 보기 형태가 달랐다. Leo의 설명을 틀린 설명(about을 빼야 한다)으로 바꿔 정답을 세 명(Mina, Jane, Ben)으로 하고 네 명 보기를 없앴다.")

X(2, 56, r="to부정사가 꾸미는 명사가 전치사의 목적어이면 to부정사 뒤에 전치사를 남긴다: sit on a chair → a chair to sit on.",
  n=["sit on a chair이므로 전치사 on이 빠지면 안 되므로", "to가 빠져 명사를 꾸밀 수 없으므로", "‘앉을 의자’를 나타내는 to부정사가 아니고 전치사도 빠졌으므로", "의자 ‘위에’ 앉으므로 in이 아니고 it도 겹치므로", "a chair to sit on으로 전치사를 남겨 바르게 썼으므로"],
  st="① ‘명사 + to부정사’에서 명사를 동사 뒤로 옮겨 본다: {0}. 전치사({1})가 있어야 말이 된다. → ② 그 전치사를 to부정사 뒤에 그대로 남긴다. → ③ 전치사가 없는 것, to가 없는 것, to 뒤에 -ing를 쓴 것을 지운다. 정답은 {a}.",
  R=("sit on a chair", "on"), B=("write with a pen", "with"), C=("study in a room", "in"), D=("talk to someone", "to"), E=("keep the photos in a box", "in"), F=("rest on a bench", "on"))

X(2, 57, r="It is + 성품 형용사(kind, nice) + of + 목적격 + to부정사. Thank you for + 동명사, help + 사람 + with + 일, You're welcome도 함께 확인한다.",
  n=["전치사 for 뒤에는 동명사를 써서 for helping이 되어야 하므로", "help A with B이므로 with my homework가 되어야 하므로", "You're welcome이 맞는 표현이므로", "kind는 성품을 평가하므로 for you를 of you로 바르게 고쳤으므로", "to 뒤에는 동사원형 say를 써야 하므로"],
  st="① 밑줄마다 틀렸는지 보고, 틀렸다면 무엇으로 고쳐야 하는지 먼저 정한다. → ② 그 답을 같은 번호의 보기와 견준다. 보기는 대부분 틀린 곳을 또 틀리게 고쳤거나 맞는 곳을 틀리게 바꿨다. → ③ {n}만 바르게 고쳤다: {0}.",
  R="kind는 사람의 성품을 평가하므로 for you가 아니라 of you다", B="thoughtful은 성품을 평가하므로 for Mina가 아니라 of Mina다(④ am agree는 agree로 고쳐야 한다)", C="kind는 성품을 평가하므로 for her가 아니라 of her다",
  D="sweet는 성품을 평가하므로 for you가 아니라 of you다(② helping은 help로 고쳐야 한다)", E="nice는 성품을 평가하므로 for Tom이 아니라 of Tom이다(④ using은 use로 고쳐야 한다)", F="smart는 성품을 평가하므로 for you가 아니라 of you다(① to write는 to write with로 고쳐야 한다)")

X(2, 58, r="be동사 + to부정사(be to 용법)는 예정·의무·가능 등을 나타낸다. 주어가 동작을 받는 대상이면 to be + 과거분사로 쓴다.",
  n=["행복은 사지고 찾아지는 대상이라 to be + 과거분사가 알맞으므로", "be 뒤에 동사원형을 쓸 수 없으므로", "능동이라 ‘행복이 무엇을 산다’는 뜻이 되므로", "to 뒤에 being을 쓸 수 없으므로", "to 뒤에 과거형·과거분사를 바로 쓸 수 없으므로"],
  st="① 주어({0})와 빈칸 동사의 관계를 본다. {1} 대상이므로 수동이다. → ② is (not) 뒤의 to부정사를 수동으로 쓰면 to be + 과거분사다. ‘~될 수 있다’는 가능의 be to 용법이다. → ③ 능동(to + 동사원형), to be + 동사원형, to being을 지운다. 정답은 {a}.",
  R=("Happiness", "행복은 사지고 찾아지는"), B=("Knowledge", "지식은 얻어지고 길러지는"), C=("Trust", "신뢰는 사지고 얻어지는"), D=("A skill", "기술은 익혀지고 향상되는"), E=("Respect", "존경은 요구되고 얻어지는"), F=("Confidence", "자신감은 만들어지고 쌓이는"))

X(2, 59, r="형용사 + enough + for + 목적격 + to부정사는 ‘…가 ~할 만큼 충분히 ~하다’는 뜻이다. enough는 형용사 뒤에 오고, 의미상 주어는 for + 목적격으로 쓴다.",
  n=["enough 뒤에 that to see를 쓸 수 없으므로", "so와 enough를 함께 쓰고 enough도 형용사 앞에 놓였으므로", "의미상 주어는 for + 목적격(us)이어야 하므로", "enough는 형용사 뒤에 와야 하므로", "형용사 + enough + for + 목적격 + to부정사로 바르게 연결했으므로"],
  st="① 첫 문장의 형용사({0})와 둘째 문장의 주어·동사({1})를 뽑는다. → ② ‘형용사 + enough + for + 목적격 + to부정사’ 순서로 잇는다. → ③ enough가 형용사 앞에 온 것, of나 주격을 쓴 것, too로 뜻이 반대가 된 것을 지운다. 정답은 {n}.",
  R=("clear", "We could see → for us to see"), B=("shallow", "We could walk → for us to walk"), C=("quiet", "Mina could study → for Mina to study"), D=("light", "Tom could carry → for Tom to carry"),
  E=("clear", "We could follow → for us to follow"), F=("wide", "Two cars could pass → for two cars to pass"))

X(2, 60, r="be to 용법은 예정(~할 예정이다), 의무(~해야 한다), 의도(if절: ~하려면), 가능(주로 부정·수동: ~할 수 있다), 운명(~할 운명이다)을 나타낸다.",
  n=["(A)는 next week으로 정해진 예정이라 옳은 설명이므로", "(B)는 ‘끝내야 한다’는 의무라 옳은 설명이므로", "(C)는 if절에서 ‘~하려면’이라는 의도를 나타내 옳은 설명이므로", "(D)는 ‘들리지 않았다’는 가능이고 부정 주어와 쓰여 옳은 설명이므로",
     "(E)는 의도가 아니라 ‘~될 운명이었다’는 운명의 뜻이므로"],
  st="① be to의 다섯 뜻을 단서와 함께 떠올린다. 미래 시점 표현 → 예정, You are to → 의무, if절 → 의도, 부정어 + to be 과거분사 → 가능, was(were) (never) to → 운명. → ② (A)~(E)에 하나씩 대어 본다. → ③ {n}은 {0}.",
  R="(E)를 ‘의도’라고 했다. was to become은 ‘~될 운명이었다’는 뜻이다", B="(D) Nothing was to be seen을 ‘의도’라고 했다. ‘보이지 않았다’는 가능이다", C="(A)를 ‘의무’라고 했다. next week이 있는 예정이다",
  D="(C)를 ‘의무’라고 했다. if절의 be to는 ‘~하려면’이라는 의도다", E="(B)를 ‘가능’이라고 했다. You are to는 의무다", F="(E)를 ‘가까운 미래의 계획’이라고 했다. was never to는 ‘결코 ~하지 못할 운명이었다’는 뜻이다")
