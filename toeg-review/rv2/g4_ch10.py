# 4급 CH10 문장의 종류 (91~100) 2차 감수
X(4, 91, r="명령문 + and는 ‘~해라, 그러면 …’이라는 뜻으로 If you + 동사 ~로 바꿔 쓸 수 있다. 명령문은 동사원형으로 시작한다.",
  n=["명령문은 동사원형 Take로 시작하고 and 문장은 If절로 바꾸므로", "Or는 문장 앞에서 조건절을 이끌 수 없으므로", "명령문을 -ing형으로 시작할 수 없으므로", "Taking도 Or도 맞지 않으므로", "명령문을 과거형으로 시작할 수 없으므로"],
  st="① 첫 문장은 ‘명령문 + and’다. 명령문은 동사원형으로 시작한다: {0}. → ② ‘~해라, 그러면 …’은 ‘만약 ~하면 …’과 같은 뜻이므로 둘째 문장은 If로 시작한다. → ③ 정답은 {a}.",
  R="Take", B="Leave", C="Take", D="Study", E="Go", F="Be(형용사 careful 앞이므로 be동사의 원형)")

X(4, 92, r="감탄문: 명사가 있으면 What + (a/an) + 형용사 + 명사 ~!, 형용사·부사만 있으면 How + 형용사/부사 + 주어 + 동사!",
  n=["a big dog처럼 명사가 있어 What이 들어가므로", "a great idea처럼 명사가 있어 What이 들어가므로", "형용사 beautiful만 있고 명사가 없어 How가 들어가 나머지와 다르므로", "a fun game처럼 명사가 있어 What이 들어가므로", "a wonderful day처럼 명사가 있어 What이 들어가므로"],
  st="① 빈칸 바로 뒤를 본다. ‘a/an + 형용사 + 명사’(또는 형용사 + 복수명사)가 오면 What, 형용사·부사만 오고 바로 주어 + 동사가 이어지면 How다. → ② {0} → ③ 정답은 {n}.",
  R="③만 beautiful 뒤에 명사 없이 you are가 온다. How가 들어간다.", B="③만 interesting 뒤에 명사 없이 the book is가 온다. How가 들어간다.", C="②만 beautiful 뒤에 명사 없이 you are가 온다. How가 들어간다.",
  D="④만 beautiful 뒤에 명사 없이 the flower is가 온다. How가 들어간다.", E="④만 nice 뒤에 명사 없이 the weather is가 온다. How가 들어간다.", F="⑤만 부사 fast 뒤에 he runs가 온다. How가 들어간다.")
RV(4, 92, "C", fx=True, why="수정 예시의 정답 문장(_____ smart you are! ③)이 원문항 정답(_____ beautiful you are! ③)과 틀·위치가 같아, 다른 문장(_____ quiet the room is!)으로 바꾸고 위치를 ①로 옮겼다.")

X(4, 93, r="What(How) about 뒤에는 동명사(-ing)를 쓴다. Shall we, Let's, Don't, Never 뒤에는 동사원형을 쓴다.",
  n=["Shall we 뒤에 동사원형 go를 써서 옳으므로", "about은 전치사라 뒤에 wearing을 써야 하므로", "Never 뒤에 동사원형 swim을 써서 옳으므로", "Don't 뒤에 동사원형 be를 써서 옳으므로", "Let's 뒤에 동사원형 have를 써서 옳으므로"],
  st="① 밑줄 앞의 표현을 본다. What(How) about 뒤는 -ing, 그 밖의 제안·명령 표현 뒤는 동사원형이다. → ② {0} → ③ 정답은 {n}.",
  R="②는 What about 뒤에 동사원형 wear를 썼다. wearing으로 고친다.", B="④는 How about 뒤에 동사원형 play를 썼다. playing으로 고친다.", C="④는 What about 뒤에 동사원형 wear를 썼다. wearing으로 고친다.",
  D="①은 What about 뒤에 동사원형 go를 썼다. going으로 고친다.", E="④는 How about 뒤에 동사원형 watch를 썼다. watching으로 고친다.", F="⑤는 What about 뒤에 동사원형 eat을 썼다. eating으로 고친다.")

X(4, 94, r="명사가 있는 감탄문은 What + a/an + 형용사 + 명사 + 주어 + 동사!로 쓴다. How 뒤에는 a + 명사가 올 수 없다.",
  n=["Let's + 동사원형으로 옳으므로", "a beautiful day처럼 명사가 있으면 How가 아니라 What을 써야 하므로", "What + a + 형용사 + 명사 + 주어 + 동사로 옳으므로", "Don't + 동사원형으로 옳으므로", "Please + 동사원형으로 옳으므로"],
  st="① 감탄문은 What/How 바로 뒤를 본다. a/an + 형용사 + 명사가 오면 What, 형용사·부사만 오면 How다. → ② 명령문·제안문은 동사원형으로 시작하는지 본다. → ③ {0} 정답은 {n}.",
  R="②는 a beautiful day라는 명사구 앞에 How를 썼다. What a beautiful day it is!가 맞다.", B="②는 an interesting book 앞에 How를 썼다. What으로 고친다.", C="①은 a beautiful day 앞에 How를 썼다. What으로 고친다.",
  D="③은 명사 없이 형용사 beautiful만 있는데 What을 썼다. How로 고친다.", E="①은 명사 없이 형용사 cute만 있는데 What을 썼다. How로 고친다.", F="⑤는 명사 weather가 있는데 How a를 썼다. What nice weather it is!가 맞다.")
RV(4, 94, "F", fx=True, why="수정 예시의 ③(Please help me.)이 원문항 ⑤와 똑같은 문장이어서 다른 문장(Please wait here.)으로 바꿨다.")

X(4, 95, r="감탄문의 어순은 What + (a/an) + 형용사 + 명사 + 주어 + 동사!, How + 형용사/부사 + 주어 + 동사!다. 의문문처럼 동사를 주어 앞에 두지 않는다.",
  n=["What + a + 형용사 + 명사 + 주어 + 동사로 바르게 바꿨으므로", "How cute 뒤에 주어 + 동사(they are)가 아니라 are they가 와서 의문문 어순이 되었으므로", "How + 형용사 + 주어 + 동사로 바르게 바꿨으므로", "What + a + 형용사 + 명사 + 주어 + 동사로 바르게 바꿨으므로", "How + 부사 + 주어 + 동사로 바르게 바꿨으므로"],
  st="① 원래 문장에서 very가 꾸미는 말을 본다. 명사가 딸려 있으면 What, 형용사·부사뿐이면 How로 시작한다. → ② 감탄문의 끝이 ‘주어 + 동사’ 순서인지, a/an이 제자리에 있는지 본다. → ③ {0} 정답은 {n}.",
  R="②는 How cute they are!가 되어야 하는데 are they로 썼다.", B="⑤는 How bright the stars are!가 되어야 하는데 are the stars로 썼다.", C="⑤는 a beautiful flower라는 명사구가 있으므로 What a beautiful flower it is!가 되어야 한다.",
  D="③은 명사 없이 형용사 kind뿐이므로 How kind she is!가 되어야 한다.", E="②는 명사 없이 형용사 interesting뿐이므로 How interesting the book is!가 되어야 한다.", F="④는 부사 fast뿐이므로 How fast he runs!가 되어야 한다.")

X(4, 96, r="Let's 뒤에는 동사원형을 쓴다. 형용사(kind) 앞에는 be동사의 원형 be가 필요하다.",
  n=["Let's 뒤에 am을 쓸 수 없으므로", "Let's 뒤에 are를 쓸 수 없으므로", "Let's 뒤에 is를 쓸 수 없으므로", "Let's 뒤에 -ing형을 쓸 수 없으므로", "Let's + 동사원형 be이므로"],
  st="① Let's 뒤에는 동사원형이 온다. → ② {0} → ③ 정답은 {a}.",
  R="빈칸 뒤가 형용사 kind이므로 be동사가 필요하고, 그 원형은 be다.", B="‘축구를 하다’는 play soccer이고, 원형은 play다.", C="빈칸 뒤가 형용사 healthy이므로 be동사의 원형 be다.", D="빈칸 뒤가 형용사 quiet이므로 be동사의 원형 be다.",
  E="‘집에 가다’는 go home이고, 원형은 go다.", F="‘점심을 먹다’는 eat lunch이고, 원형은 eat이다.")
RV(4, 96, "D", v="수정(내용)", why="정답 확인. 다만 오답 bes는 영어에 없는 형태라 철자만 보고 지워진다. 원문항의 오답(am, are, is, being)은 모두 실제 형태다.", fix="bes를 is로")
RV(4, 96, "E", v="수정(내용)", why="정답 확인. 다만 오답 gos는 영어에 없는 형태라 철자만 보고 지워진다. 원문항의 오답은 모두 실제 형태다.", fix="gos를 goes로")

X(4, 97, r="a + 형용사 + 명사를 강조하면 What, 형용사·부사만 강조하면 How로 감탄문을 시작한다.",
  n=["a beautiful flower라는 명사구를 강조하는 What 감탄문이므로", "뒤에 명사구가 있어 How를 쓸 수 없으므로", "So로는 이 어순의 감탄문을 시작하지 않으므로", "Very로는 감탄문을 시작하지 않으므로", "Such로는 이 어순의 감탄문을 시작하지 않으므로"],
  st="① 빈칸 뒤를 본다: {0}. → ② {1} → ③ 정답은 {a}.",
  R=("a beautiful flower + it is", "a + 형용사 + 명사가 있으므로 What이다."), B=("kind + she is", "명사 없이 형용사뿐이므로 How다."), C=("a beautiful flower + it is", "a + 형용사 + 명사가 있으므로 What이다."),
  D=("an interesting book + it is", "an + 형용사 + 명사가 있으므로 What이다."), E=("fast + he runs", "명사 없이 부사뿐이므로 How다."), F=("a cute dog + it is", "a + 형용사 + 명사가 있으므로 What이다."))
RV(4, 97, "BCDE", fx=True, why="원문항 발문(선다형인데 ‘쓰시오’)을 ‘고르시오’로 고쳤다. 같은 발문을 쓰던 변형의 수정 예시도 고친 발문을 따르게 했다.")
RV(4, 97, "F", fx=True, why="수정 예시의 정답(What)과 위치(①)가 원문항과 같아 보기 순서를 바꿔 ②로 옮겼고, 발문도 고친 원문항 발문(‘고르시오’)을 따르게 했다.")

X(4, 98, r="명령문 + and는 ‘~해라, 그러면 …’, 명령문 + or는 ‘~해라, 그렇지 않으면 …’이다. 명령문은 동사원형으로 시작한다.",
  n=["두 빈칸 모두 동사원형으로 시작하는 명령문이므로", "명령문을 -ing형으로 시작할 수 없으므로", "뒤에 and가 있어 If절을 쓸 수 없으므로", "뒤에 or가 있어 If절을 쓸 수 없으므로", "명령문을 to부정사로 시작할 수 없으므로"],
  st="① 빈칸 뒤에 ‘, and’와 ‘, or’가 있다. 그 앞은 명령문이어야 한다. → ② 명령문은 주어 없이 동사원형으로 시작한다: {0}. → ③ 정답은 {n}.",
  R="Go straight / Hurry up", B="Study hard / Be careful", C="Go straight / Hurry up", D="Take a rest / Leave now", E="Clean the room / Start now", F="Run fast / Hurry up")

X(4, 99, r="Let's, Shall we, Why don't we 뒤에는 동사원형, How(What) about 뒤에는 동명사(-ing)를 쓴다.",
  n=["How about 뒤에 go가 아니라 going을 써야 하므로", "Why don't we 뒤에 dancing이 아니라 dance를 써야 하므로", "Let's 뒤에 reading이 아니라 read를 써야 하므로", "Let's + 동사원형, What about + -ing로 둘 다 옳으므로", "Shall we 뒤에 running이 아니라 run을 써야 하므로"],
  st="① 제안 표현을 둘로 가른다: 뒤에 동사원형이 오는 것(Let's, Shall we, Why don't we), 뒤에 -ing가 오는 것(How about, What about). → ② 짝마다 두 밑줄을 모두 확인한다. 하나라도 틀리면 지운다. → ③ {0} 정답은 {n}.",
  R="④만 Let's eat, What about eating으로 둘 다 맞다.", B="②만 Let's watch, How about watching으로 둘 다 맞다.", C="⑤만 Let's eat, What about eating으로 둘 다 맞다.", D="⑤만 Let's play, How about playing으로 둘 다 맞다.",
  E="③만 Let's go, What about going으로 둘 다 맞다.", F="②만 Let's study, What about studying으로 둘 다 맞다.")

X(4, 100, r="감탄문의 어순: How + 형용사/부사 + 주어 + 동사!, What + (a/an) + 형용사 + 명사 + 주어 + 동사! 복수명사 앞에는 a를 쓰지 않고, 동사는 주어에 맞춘다.",
  pre=["문장별 판정: (A) X. 의문문 어순이다(How cold it is today!). (B) X. 복수명사 flowers 앞에 a를 쓸 수 없다. (C) O. How + 부사 + 주어 + 동사. (D) O. What + an + 형용사 + 명사 + 주어 + 동사. (E) X. 주어 he에는 speaks."],
  n=["(C)는 옳은 문장이므로", "(C), (D) 모두 옳은 문장이므로", "틀린 문장 (A), (B), (E)만 묶었으므로", "(C)는 옳은 문장이므로", "(D)는 옳은 문장이므로"],
  st="① 문장마다 세 가지를 본다: What/How 뒤의 덩어리, ‘주어 + 동사’ 어순, 주어와 동사의 수. → ② {0} → ③ 틀린 문장만 묶은 {a}가 정답이다.",
  R="(A) is it(it is), (B) a ~ flowers(a를 뺀다), (E) he speak(speaks)가 틀렸다.", B="(C) What cute(How cute), (D) How a nice car(What a nice car)가 틀렸다.", C="(A) is it(it is), (B) a ~ flowers(a를 뺀다), (E) does he run(he runs)이 틀렸다.",
  D="(C) How a tall boy(What a tall boy), (D) What beautiful(How beautiful)이 틀렸다.", E="(C) What interesting book(an이 빠졌다), (D) How a beautiful day(What a beautiful day)가 틀렸다.", F="(C) How a kind girl(What a kind girl)만 틀렸다.")
RV(4, 100, "B", fx=True, why="수정 예시의 (E)(How loud she sing!)가 원문항 (E)(How loud he speak!)와 닮아 다른 문장(How well they sings!)으로 바꿨다.")
