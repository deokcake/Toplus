# 5급 CH8 형용사와 부사 (71~80) 2차 감수
X(5, 71, r="형용사의 두 쓰임: ① 명사 앞에서 명사를 꾸민다(a tall building). ② be동사·연결동사 뒤에서 주어를 보충 설명한다(They are cute).",
  n=["tall이 명사 building 앞에서 꾸미는 쓰임이므로", "great이 명사 plan 앞에서 꾸미는 쓰임이므로", "easy가 명사 question 앞에서 꾸미는 쓰임이므로", "cute가 are 뒤에서 주어 They를 보충 설명하므로", "great이 명사 book 앞에서 꾸미는 쓰임이므로"],
  st="① 선생님이 든 예문({0})은 형용사가 동사 뒤에서 주어를 설명하는 쓰임이다. → ② 보기마다 형용사 바로 뒤에 명사가 있는지 본다. 명사가 있으면 꾸미는 쓰임이다. → ③ {1} 정답은 {n}.",
  R=("These apples are sweet.", "④만 형용사 cute 뒤에 명사가 없고 are 뒤에서 주어를 설명한다."), B=("The soup smells delicious.", "③만 형용사 sleepy가 looks 뒤에서 주어를 설명한다."),
  C=("The sky is blue.", "②만 형용사 beautiful이 are 뒤에서 주어를 설명한다."), D=("The dog looks happy.", "④만 형용사 sweet이 tastes 뒤에서 주어를 설명한다."),
  E=("This tea smells good.", "⑤만 형용사 quiet이 is 뒤에서 주어를 설명한다."), F=("The boy seems tired.", "①만 형용사 sick이 feels 뒤에서 주어를 설명한다."))
RV(5, 71, "E", fx=True, why="수정 예시의 선생님 예문(This soup smells good.)이 B의 예문(The soup smells delicious.)과 거의 같아 주어를 바꿨다(This tea smells good.).")

X(5, 72, r="형용사는 be동사·연결동사 뒤에서 주어를 설명하거나 명사를 꾸미고, 부사는 동사를 꾸민다. fast, hard는 -ly 없이도 부사로 쓰인다.",
  n=["동사 runs를 꾸미는 부사이므로", "동사 speaks를 꾸미는 부사이므로", "동사 work를 꾸미는 부사이므로", "is 뒤에서 주어 The flower를 설명하는 형용사이므로", "동사 moves를 꾸미는 부사이므로"],
  st="① 밑줄 앞의 동사를 본다. 일반동사(동작)면 밑줄은 그 동작을 꾸미는 부사다. → ② be동사나 연결동사(look, smell, become)면 밑줄은 주어를 설명하는 형용사다. → ③ {0} 정답은 {n}.",
  R="④만 be동사 is 뒤다.", B="④만 연결동사 became 뒤다. ②의 quietly와 견주면 차이가 보인다.", C="①만 be동사 is 뒤다.", D="③만 연결동사 smells 뒤다.", E="⑤만 연결동사 looks 뒤다. ④의 well은 good의 부사다.", F="②만 be동사 is 뒤다.")
RV(5, 72, "C", v="수정(내용)", why="정답 ④ 유일 확인. 다만 ①(They work hard.)이 원문항 ③과 똑같은 문장이고, 정답 위치(④)와 정답 문장의 짜임(The dog is small. / The flower is beautiful.)도 원문항과 같다.", fix="겹치는 문장을 바꾸고 정답 위치를 옮김")

X(5, 73, r="many는 셀 수 있는 명사의 복수형 앞에, much는 셀 수 없는 명사 앞에 쓴다.",
  n=["friends는 셀 수 있는 복수 명사라 many가 들어가 나머지와 다르므로", "money는 셀 수 없어 much가 들어가므로", "homework는 셀 수 없어 much가 들어가므로", "rice는 셀 수 없어 much가 들어가므로", "salt는 셀 수 없어 much가 들어가므로"],
  st="① 빈칸 뒤의 명사만 본다. -s가 붙은 복수 명사면 many, 셀 수 없는 명사면 much다. → ② {0} → ③ 정답은 {n}.",
  R="friends만 복수 명사이고 money, homework, rice, salt는 셀 수 없다.", B="chairs만 복수 명사이고 information, water, time, homework는 셀 수 없다.", C="books만 복수 명사이고 homework, rice, money, water는 셀 수 없다.",
  D="cars만 복수 명사이고 sugar, time, milk, coffee는 셀 수 없다.", E="pencils만 복수 명사이고 juice, snow, help, bread는 셀 수 없다.", F="apples만 복수 명사이고 butter, news, paper, cheese는 셀 수 없다. news는 -s로 끝나도 셀 수 없다.")

X(5, 74, r="fast, hard, late, high는 -ly 없이 부사로 쓴다. highly(매우), hardly(거의 ~않다), lately(최근에)는 뜻이 다른 말이다.",
  n=["very가 형용사 pretty를 바르게 꾸미므로", "easily가 동사 finish를 바르게 꾸미므로", "peacefully가 동사 sleeps를 바르게 꾸미므로", "‘높게’는 high이고 highly는 ‘매우’라는 뜻이므로", "‘빠르게’를 fast로 바르게 옮겼으므로"],
  st="① 우리말의 ‘~하게’에 해당하는 영어 낱말을 짝마다 찾는다. → ② -ly가 붙으면 뜻이 달라지는 낱말(high/highly, hard/hardly, late/lately, near/nearly)과 형용사를 부사 자리에 쓴 것을 살핀다. → ③ {0} 정답은 {n}.",
  R="④의 highly는 ‘매우’다. ‘높게’는 high다.", B="⑤의 lately는 ‘최근에’다. ‘늦게’는 late다.", C="①의 good은 형용사다. ‘잘’은 부사 well이다.", D="②의 hardly는 ‘거의 ~않다’다. ‘열심히’는 hard다.",
  E="④의 nearly는 ‘거의’다. ‘가까이’는 near다.", F="③의 easy는 형용사다. ‘쉽게’는 부사 easily다.")
RV(5, 74, "C", fx=True, why="수정 예시의 틀린 짝(He runs fastly.)이 영어에 없는 말이었다. 원문항의 틀린 짝(highly)은 실제 낱말이므로, 실제 낱말을 잘못 쓴 짝(She plays the piano good.)으로 바꿨다.")

X(5, 75, r="be동사 뒤 보어 자리에는 형용사를 쓴다. 부사는 동사를 꾸민다.",
  n=["is 뒤 보어 자리라 부사 politely가 아니라 형용사 polite를 써야 하므로", "부사 joyfully가 동사 dances를 바르게 꾸미므로", "부사 slowly가 동사 drives를 바르게 꾸미므로", "부사 carefully가 동사 cross를 바르게 꾸미므로", "부사 fast가 동사 walked를 바르게 꾸미므로"],
  st="① 문장마다 동사를 본다. be동사·연결동사(look, seem, smell, taste, sound) 뒤는 형용사 자리다. → ② 일반동사 뒤에서 동작을 꾸미는 말은 부사다. → ③ {0} 정답은 {n}.",
  R="①은 is 뒤에 부사 politely를 썼다(polite).", B="⑤는 smells 뒤에 부사 wonderfully를 썼다(wonderful).", C="①은 looks 뒤에 부사 happily를 썼다(happy).", D="④는 was 뒤에 부사 excitingly를 썼다(exciting).",
  E="②는 seems 뒤에 부사 sadly를 썼다(sad).", F="③은 are 뒤에 부사 beautifully를 썼다(beautiful).")

X(5, 76, r="영어 문장의 어순은 주어 + 동사 + 목적어·보어다. 형용사는 the/a와 명사 사이에 온다(the red apple).",
  n=["동사 Like로 시작해 주어 + 동사의 순서가 아니므로", "주어 I + 동사 like + 목적어 the red apple의 순서이므로", "the 뒤에 명사가 없고 목적어가 주어 앞에 왔으므로", "동사 like가 목적어 뒤로 갔으므로", "낱말이 거꾸로 놓였으므로"],
  st="① 주어와 동사를 먼저 찾는다: {0}. → ② 나머지를 묶는다: {1}. → ③ 주어 + 동사 + 나머지의 순서로 놓는다. 정답은 {n}.",
  R=("I / like", "the + red + apple(형용사는 the와 명사 사이)"), B=("the small bird / sings", "부사 beautifully는 동사 뒤"), C=("the dog / is", "very + cute(very는 형용사 앞)"), D=("Tom / runs", "very + fast(very는 부사 앞)"),
  E=("she / has", "a + beautiful + bag(형용사는 a와 명사 사이)"), F=("the cat / walks", "부사 quietly는 동사 뒤"))
RV(5, 76, "B", fx=True, why="변형의 제시 단어가 괄호 안에 있고 The가 대문자여서 첫 낱말이 드러난다(원문항은 괄호가 없다). 수정 예시에서 원문항 표기로 맞췄다.")

X(5, 77, r="형용사 + -ly로 부사를 만든다. 자음 + y로 끝나는 형용사는 y를 i로 바꾸고 -ly를 붙인다(happy → happily).",
  n=["y를 i로 바꾸지 않았으므로", "y를 i로 바꾸고 -ly를 붙였으므로", "형용사라 동사 smiling을 꾸밀 수 없으므로", "‘행복’이라는 명사이므로", "happies라는 말은 없으므로"],
  st="① ‘{0}’는 동사를 꾸미므로 부사가 필요하다. 형용사와 명사를 지운다. → ② 형용사 {1}에 -ly를 붙인다. {2} → ③ 정답은 {a}.",
  R=("행복하게", "happy", "자음 + y로 끝나므로 y를 i로 바꾼다."), B=("조심스럽게", "careful", "-ful 뒤에 -ly를 그대로 붙여 l이 두 번 온다."), C=("쉽게", "easy", "자음 + y로 끝나므로 y를 i로 바꾼다."),
  D=("바쁘게", "busy", "자음 + y로 끝나므로 y를 i로 바꾼다."), E=("시끄럽게", "noisy", "자음 + y로 끝나므로 y를 i로 바꾼다."), F=("무겁게", "heavy", "자음 + y로 끝나므로 y를 i로 바꾼다."))
RV(5, 77, "E", v="수정(내용)", why="정답 ④ carefully 유일 확인. 다만 정답 낱말과 오답(carefullly, careful)이 B와 같고(유형 간 중복), -ly만 붙이면 되어 원문항의 y → i 철자 규칙(happily)을 묻지 않는다. C·D·F와 같은 문제다.", fix="y → i 철자 변화가 있는 낱말로")

X(5, 78, r="many + 셀 수 있는 명사의 복수형, much + 셀 수 없는 명사. How many/much도 뒤의 명사에 맞춘다.",
  n=["pencils는 복수 명사라 many가 맞으므로", "juice는 셀 수 없어 much가 맞으므로", "trees는 복수 명사라 many가 맞으므로", "homework는 셀 수 없어 much를 써야 하므로", "sugar는 셀 수 없어 much가 맞으므로"],
  st="① 밑줄 뒤의 명사가 셀 수 있는 복수 명사인지 셀 수 없는 명사인지 가른다. → ② many + 복수 명사, much + 셀 수 없는 명사인지 맞춰 본다. → ③ {0} 정답은 {n}.",
  R="④의 homework는 셀 수 없는데 many를 썼다.", B="③의 cousins는 복수 명사인데 much를 썼다.", C="①의 water는 셀 수 없는데 many를 썼다.", D="④의 books는 복수 명사인데 much를 썼다.",
  E="②의 dogs는 복수 명사인데 much를 썼다.", F="⑤의 cheese는 셀 수 없는데 many를 썼다.")

X(5, 79, r="같은 낱말이라도 동사를 꾸미면 부사, 명사를 꾸미거나 주어를 설명하면 형용사다. hard는 -ly 없이 ‘열심히’라는 부사로 쓰인다.",
  pre=["<보기> 판정: (가) O. hard가 동사 studies를 꾸민다. (나) X. 이 문장의 studies는 명사가 아니라 동사다. (다) O. hard는 -ly 없이 부사로 쓰인다(hardly는 다른 뜻)."],
  k="옳은 설명은 (가), (다)이다.", n=["(가), (다)가 옳은 설명이므로", "(나)가 틀린 설명이므로", "(다)도 옳은 설명이므로", "(나)가 틀린 설명이므로", "(나)가 틀린 설명이므로"],
  st="① 밑줄 친 말이 문장에서 무엇을 꾸미거나 설명하는지 먼저 정한다: {0}. → ② <보기>를 하나씩 이 판단에 대어 본다. → ③ {1} 정답은 {a}.",
  R=("동사 studies를 꾸미는 부사", "(가) O, (나) X, (다) O."), B=("동사 moves를 꾸미는 부사", "(가) X, (나) O, (다) O."), C=("동사 came을 꾸미는 부사(‘늦게’)", "(가) O, (나) X, (다) X(‘최근에’는 lately)."),
  D=("is 뒤에서 주어 Jane을 설명하는 형용사", "(가) X, (나) O, (다) X(명사 앞이 아니다)."), E=("동사 jumped를 꾸미는 부사", "(가) O, (나) O, (다) X."), F=("명사 test를 꾸미는 형용사(‘어려운’)", "(가) O, (나) O, (다) O."))

X(5, 80, r="look, sound, feel 같은 연결동사 뒤에는 부사가 아니라 형용사를 쓴다.",
  pre=["밑줄별 판정: (A) X. look 뒤에는 형용사 sad. (B) O. (C) X. sounds 뒤에는 형용사 bad. (D) O. feel 뒤에 형용사 sorry."],
  k="틀린 부분은 (A), (C)이다.", n=["(A), (C)가 틀린 부분이므로", "(B), (D)는 옳으므로", "(B)는 옳으므로", "(D)는 옳으므로", "(B), (D)는 옳으므로"],
  st="① 밑줄마다 동사의 종류를 가른다. 연결동사(look, sound, feel, smell, taste, seem) 뒤는 형용사, 동작을 나타내는 동사 뒤는 부사다. → ② {0} → ③ 틀린 것을 모두 모으면 {a}",
  R="(A) look sadly → sad, (C) sounds badly → bad. (D) feel sorry는 옳다.", B="(A) smells wonderfully → wonderful, (D) speaks ~ polite → politely. (B), (C)는 옳다.", C="(B) cooked it careful → carefully, (D) tastes wonderfully → wonderful. (A), (C)는 옳다.",
  D="(A) seem happily → happy, (C) practiced hardly → hard, (D) sounds greatly → great. (B) fast는 옳다.", E="(A) looks cutely → cute, (B) moves careful → carefully, (D) barks noisy → noisily. (C)는 옳다.",
  F="(C) speaks polite → politely, (D) works diligent → diligently. (A), (B)는 옳다.")
