# 4급 CH11 문장의 형식 (101~110) 2차 감수
X(4, 101, r="목적어는 동사의 동작을 받는 말(~을/를)로, 동사 바로 뒤에 오는 명사구다.",
  n=["I는 주어이므로", "bought는 동사이므로", "‘무엇을 샀는가’에 답하는 말이라 목적어이므로", "for breakfast는 ‘아침 식사로’라는 부사구이므로", "this morning은 때를 나타내는 부사구이므로"],
  st="① 동사를 찾는다: {0}. → ② 동사에 ‘무엇을?’이라고 물어 본다: {1}. → ③ 때·장소·목적을 나타내는 말은 부사구다. 정답은 {a}.",
  R=("bought", "산 것은 some fresh bread and milk"), B=("reads", "읽는 것은 English books"), C=("bought", "산 것은 some fresh bread and milk"), D=("likes", "좋아하는 것은 this movie"), E=("visited", "방문한 사람은 our uncle"),
  F=("need", "필요한 것은 some water"))

X(4, 102, r="look, smell, sound, feel, seem 뒤에는 주어를 설명하는 형용사가 온다. 부사나 명사는 올 수 없다. lovely, friendly, lonely는 -ly로 끝나도 형용사다.",
  n=["형용사 polite가 들어갈 수 있으므로", "형용사 pretty가 들어갈 수 있으므로", "lovely는 -ly로 끝나지만 형용사라 들어갈 수 있으므로", "kindness는 명사라 ‘~해 보인다’의 보어로 쓸 수 없으므로", "형용사 handsome이 들어갈 수 있으므로"],
  st="① 동사 {0} 뒤는 주어의 상태를 설명하는 보어 자리다. 형용사만 온다. → ② 보기를 형용사와 그렇지 않은 것으로 가른다. -ly로 끝나도 형용사인 말(lovely 등)에 주의한다. → ③ {1} 정답은 {a}.",
  R=("looks", "kindness만 명사다."), B=("smells", "wonderfully만 부사다."), C=("looks", "quickly만 부사다."), D=("looks", "beautifully만 부사다."), E=("looks", "carefully만 부사다."), F=("looks", "slowly만 부사다."))
RV(4, 102, "D", fx=True, why="수정 예시의 정답(wonderfully, ②)이 B 변형의 정답과 낱말·위치까지 같아, 정답을 strangely(④)로 바꿨다.")

X(4, 103, r="1형식은 주어 + 동사만으로 뜻이 완성되는 문장이다. 부사(loudly)나 전치사구(at the station)는 형식에 넣지 않는다.",
  n=["주어 + 동사 + 전치사구로 제시문과 같은 1형식이므로", "them이 목적어인 3형식이므로", "so good이 보어인 2형식이므로", "my favorite song이 보어인 2형식이므로", "me와 a present, 목적어가 둘인 4형식이므로"],
  st="① 제시문에서 부사·전치사구를 지우고 뼈대만 남긴다: {0}. 주어 + 동사뿐인 1형식이다. → ② 보기도 같은 방법으로 뼈대를 본다. 동사 뒤에 보어나 목적어가 남으면 1형식이 아니다. → ③ {1} 정답은 {n}.",
  R=("They laughed", "①만 The train arrived(주어 + 동사)로 1형식이다."), B=("The hikers disappeared", "⑤만 The audience cheered로 1형식이다."), C=("They laughed", "③만 The baby slept로 1형식이다."),
  D=("They laughed", "⑤만 Birds fly로 1형식이다."), E=("They laughed", "④만 Tom laughed로 1형식이다."), F=("They laughed", "②만 The bus came으로 1형식이다."))

X(4, 104, r="동사 뒤의 말이 동작의 대상(~을/를)이면 목적어, 주어의 상태를 설명하면 보어다. look, seem, become, smell, taste 뒤에는 보어가 온다.",
  n=["read의 대상(~을)인 목적어이므로", "finished의 대상인 목적어이므로", "teaches의 대상인 목적어이므로", "looks 뒤에서 주어 She를 설명하는 보어라 나머지와 다르므로", "bought의 대상인 목적어이므로"],
  st="① 밑줄 앞의 동사를 본다. 동작을 나타내는 동사(read, buy, open) 뒤는 목적어, 상태를 나타내는 동사(look, seem, become, smell, taste) 뒤는 보어다. → ② {0} → ③ 정답은 {n}.",
  R="④만 looks 뒤의 형용사 kind로 보어다. 나머지는 목적어다.", B="①만 reads 뒤의 books로 목적어다. 나머지는 보어다.", C="②만 reads 뒤의 books로 목적어다. 나머지는 보어다.", D="①만 bought 뒤의 a new desk로 목적어다. 나머지는 보어다.",
  E="③만 opened 뒤의 the window로 목적어다. 나머지는 보어다.", F="①만 bought 뒤의 a camera로 목적어다. 나머지는 보어다.")

X(4, 105, r="smell, look, sound, taste 같은 감각동사 뒤에는 부사가 아니라 형용사 보어를 쓴다(smells good).",
  n=["a doctor가 주어를 보충 설명하는 보어이므로", "looks 뒤의 interesting은 보어이고 목적어는 없으므로", "감각동사 sounded 뒤에 형용사 sad가 쓰였으므로", "be동사 + -ing로 진행 중인 동작을 나타내므로", "감각동사 smells 뒤에는 부사 well이 아니라 형용사 good을 써야 하므로"],
  st="① 보기마다 문장과 설명을 따로 본다. 문장이 틀렸는데 옳다고 설명한 것을 찾는다. → ② 감각동사(smell, look, sound, taste, seem) 뒤가 형용사인지 확인한다. 부사가 오면 틀린 문장이다. → ③ {0} 정답은 {n}.",
  R="⑤는 smells so well이 틀린 문장인데(smells so good) 바르다고 설명했다.", B="④는 smells beautifully가 틀린 문장이다. smells beautiful이 맞다.", C="④는 smells so well이 틀린 문장이다. smells so good이 맞다.",
  D="④는 tastes nicely가 틀린 문장이다. tastes nice가 맞다.", E="②는 looks happily가 틀린 문장이다. looks happy가 맞다.", F="②는 seems quietly가 틀린 문장이다. seems quiet가 맞다.")

X(4, 106, r="목적어는 동사의 동작을 받는 말(~을/를)이다.",
  n=["She는 주어이므로", "drinks는 동사이므로", "every는 morning을 꾸미는 말이므로", "morning은 때를 나타내는 부사구의 일부이므로", "‘무엇을 마시는가’에 답하는 말이라 목적어이므로"],
  st="① 동사를 찾는다: {0}. → ② 동사에 ‘무엇을?’이라고 물어 본다: {1}. 낱말 하나가 아니라 꾸미는 말까지 묶어 답한다. → ③ 정답은 {a}.",
  R=("drinks", "마시는 것은 milk"), B=("bought", "산 것은 a new car"), C=("drinks", "마시는 것은 milk"), D=("likes", "좋아하는 것은 music"), E=("reads", "읽는 것은 English books"), F=("need", "필요한 것은 some help"))
RV(4, 106, "C", fx=True, why="수정 예시의 정답 위치가 원문항과 같은 ⑤였다(D·F 변형도 ⑤). 보기 순서를 바꿔 ②로 옮겼다.")

X(4, 107, r="문장의 형식은 주어·동사·목적어·보어로 정한다. 부사(어)는 형식에 영향을 주지 않는다.",
  n=["I는 주어이므로", "beautifully는 부사라 형식에 영향을 주지 않으므로", "singing은 목적어 birds를 설명하는 목적격보어이므로", "birds는 목적어이므로", "saw는 동사이므로"],
  st="① 문장의 뼈대를 찾는다: {0}. → ② 뼈대에 들지 않는 말은 부사(어)다. 빼도 문장이 성립한다. → ③ 정답은 {a}.",
  R="I(주어) + saw(동사) + birds(목적어) + singing(목적격보어)", B="Tom(주어) + saw(동사) + the dog(목적어) + running(목적격보어)", C="We(주어) + heard(동사) + Mina(목적어) + singing(목적격보어)",
  D="Jane(주어) + watched(동사) + the children(목적어) + play(목적격보어)", E="We(주어) + found(동사) + the door(목적어) + closed(목적격보어)", F="They(주어) + kept(동사) + the baby(목적어) + calm(목적격보어)")

X(4, 108, r="smell, look, taste, feel 같은 감각동사 뒤에는 형용사를, run처럼 동작을 나타내는 동사 뒤에는 부사를 쓴다.",
  n=["smells 뒤에는 부사 freshly가 아니라 형용사 fresh를 쓰므로", "동사 runs를 꾸미는 말은 형용사 slow가 아니라 부사 slowly이므로", "looks 뒤에는 부사 hungrily가 아니라 형용사 hungry를 쓰므로", "tastes 뒤에 형용사 good을 썼으므로", "feel 뒤에는 부사 sadly가 아니라 형용사 sad를 쓰므로"],
  st="① 동사가 감각·상태 동사인지 동작 동사인지 가른다. → ② 감각·상태 동사 뒤는 형용사, 동작 동사 뒤는 부사다. → ③ {0} 정답은 {n}.",
  R="④만 tastes(감각동사) 뒤에 형용사 good을 썼다.", B="④만 became 뒤에 형용사 dark를 썼다.", C="③만 tastes 뒤에 형용사 good을 썼다.", D="②만 looks 뒤에 형용사 happy를 썼다.", E="①만 smells 뒤에 형용사 sweet를 썼다.",
  F="③만 seems 뒤에 형용사 tired를 썼다.")

X(4, 109, r="1형식은 주어 + 동사로 이루어진다. There + be동사 + 주어도 1형식이다. 부사·전치사구는 형식에 넣지 않는다.",
  pre=["문장별 판정: (가) 1형식. There are + 주어(many books). (나) 1형식. 주어 + 동사(late는 부사). (다) 2형식. delicious가 보어. (라) 3형식. lunch가 목적어."],
  n=["(가)와 (나)가 모두 1형식이므로", "(다)는 2형식이므로", "(다)는 2형식, (라)는 3형식이므로", "(다)는 2형식이므로", "(라)는 3형식이므로"],
  st="① 문장마다 부사·전치사구를 지우고 뼈대만 남긴다. → ② 동사 뒤에 보어나 목적어가 남지 않으면 1형식이다. There is/are 문장도 1형식이다. → ③ {0} 정답은 {a}.",
  R="(가) There are many books, (나) The bus arrived가 1형식이다.", B="(가) Tom laughed, (다) We went, (마) The bus came이 1형식이다.", C="(가) There are many books, (나) The bus arrived, (마) Birds fly가 1형식이다.",
  D="(가) The baby sleeps, (다) The train arrived, (마) Birds sing이 1형식이다.", E="(가) There is a cat, (다) The dog ran, (마) Birds fly가 1형식이다.", F="(가) The train stopped, (다) We arrived, (마) The baby cried가 1형식이다.")
RV(4, 109, "F", fx=True, why="수정 예시의 정답 조합과 위치((가), (나) ①)가 원문항과 같아, 문장 순서를 바꿔 정답을 (다), (라)(③)로 했다.")

X(4, 110, r="1형식: 주어 + 동사. 2형식: 주어 + 동사 + 보어(be, seem, look 뒤). 3형식: 주어 + 동사 + 목적어.",
  pre=["문장별 판정: (A) O. 주어 + 동사의 1형식. (B) O. quiet가 보어인 2형식. (C) O. some clothes가 목적어인 3형식. (D) X. large가 보어인 2형식. (E) X. nice가 보어인 2형식."],
  n=["(A), (B), (C)가 모두 옳게 짝지어졌으므로", "(D)는 2형식이므로", "(E)는 2형식이므로", "(D)는 2형식이므로", "(D), (E) 모두 2형식이므로"],
  st="① 문장마다 동사 뒤의 말이 보어(주어를 설명)인지 목적어(동작의 대상)인지, 아무것도 없는지 본다. → ② 보어면 2형식, 목적어면 3형식, 없으면 1형식이다. 괄호 속 형식과 견준다. → ③ {0} 정답은 {a}.",
  R="(D) is large와 (E) looks nice는 형용사 보어가 있는 2형식인데 3형식, 1형식으로 적혀 있다.", B="다섯 항목 모두 형식이 옳게 적혀 있다.", C="(D) is a teacher는 2형식, (E) likes music은 3형식인데 반대로 적혀 있다.",
  D="(E) arrived home은 home이 부사라 1형식인데 3형식으로 적혀 있다.", E="다섯 항목 모두 형식이 옳게 적혀 있다.", F="다섯 항목 모두 형식이 옳게 적혀 있다.")
RV(4, 110, "C", fx=True, why="수정 예시의 (D)(He seems quiet.)가 원문항 (B)(He seems very quiet.)와 닮아 다른 문장(She looks tired.)으로 바꿨다.")
