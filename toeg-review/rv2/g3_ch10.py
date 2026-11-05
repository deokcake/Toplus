# 3급 CH10 형용사와 부사 (91~100) 2차 감수
X(3, 91, r="형용사는 꾸미는 명사 바로 앞에 온다(a difficult problem). -thing으로 끝나는 대명사는 형용사가 뒤에서 꾸민다(something warm).",
  n=["주어 I 앞은 형용사가 꾸밀 명사가 없는 자리이므로", "동사 have 앞에 형용사를 둘 수 없으므로", "관사 a 앞이 아니라 관사와 명사 사이에 와야 하므로", "형용사는 관사 a와 명사 problem 사이, 곧 problem 바로 앞에 오므로", "to solve 앞은 명사 problem 뒤라서 형용사 자리가 아니므로"],
  st="① 우리말에서 형용사가 꾸미는 말을 찾는다: {0}. → ② 영어 문장에서 그 말은 {1}이다. 형용사는 관사와 명사 사이, 곧 명사 바로 앞에 놓는다. → ③ 정답은 {a}의 앞자리({n})이다.",
  R=("‘어려운 문제’", "problem"), B=("‘어려운 문제’", "problem"), C=("‘재미있는 책’", "book"), D=("‘예쁜 드레스’", "dress"), E=("‘중요한 일’", "work"), F=("‘아름다운 장소’", "place"))
RV(3, 91, "C", v="수정(내용)", fx=True, why="정답(book) 확인. 다만 a book 사이에 interesting을 넣으면 a interesting book이 되어 관사가 맞지 않는다(an interesting book이어야 한다). 형식도 원문항(문장 속 위치 선택)과 다르다. 기존 수정 예시(Here is a book …)에도 같은 문제가 있어 관사가 없는 two books로 고쳤다.", fix="관사 a가 없는 문장으로, 원문항 형식으로")

X(3, 92, r="빈도부사(always, usually, often, rarely, never)는 be동사·조동사 뒤, 일반동사 앞에 놓는다.",
  n=["주어 앞은 빈도부사의 기본 자리가 아니므로", "be동사 앞이 아니라 뒤에 놓으므로", "be동사 is 뒤, 형용사 busy 앞이 빈도부사 자리이므로", "busy 뒤, 전치사구 앞은 빈도부사 자리가 아니므로", "문장 뒤쪽의 전치사구 사이에는 놓지 않으므로"],
  st="① 문장의 동사를 찾는다: {0}. → ② 빈도부사는 be동사 뒤, 일반동사 앞에 놓는다. 여기서는 {1}. → ③ 정답은 {n}.",
  R=("be동사 is", "is 뒤, busy 앞 자리(③)다"), B=("be동사 is", "be동사 is 뒤다"), C=("be동사 is", "be동사 is 뒤다"), D=("be동사 are", "be동사 are 뒤다"), E=("be동사 is", "be동사 is 뒤다"), F=("be동사 are", "be동사 are 뒤다"))

X(3, 93, r="find·make 뒤의 목적격보어와 look·smell·taste·feel·sound·become 뒤의 주격보어 자리에는 부사가 아니라 형용사를 쓴다.",
  n=["smell 뒤 보어 자리에 부사 sweetly를 쓸 수 없으므로", "목적격보어 자리에 명사 beauty를 쓰면 ‘음악 = 아름다움’이 되어 어색하므로", "목적격보어 beautiful, 주격보어 sweet으로 모두 형용사이므로", "두 자리 모두 부사를 쓸 수 없으므로", "명사 beauty도 부사 sweetly도 알맞지 않으므로"],
  st="① 첫 문장의 동사는 {0}. 빈칸은 {1} 자리다. → ② 둘째 문장의 동사는 {2}. 빈칸은 주어를 설명하는 보어 자리다. 우리말로는 ‘~하게’로 풀려도 보어 자리에는 형용사를 쓴다. → ③ 둘 다 형용사인 {a}가 정답이다.",
  R=("found", "목적어 the music을 설명하는 목적격보어", "smells"), B=("found", "목적어 the music을 설명하는 목적격보어", "smells"), C=("looks", "주어를 설명하는 보어", "tastes"), D=("became", "주어를 설명하는 보어", "smells"),
  E=("looks", "주어를 설명하는 보어", "feels"), F=("sounds", "주어를 설명하는 보어", "tastes"))
RV(3, 93, "CDEF", fx=True, why="수정 예시가 보기를 그대로 두어 영어에 없는 형태(to tired, to famous, to dark, to interesting)가 남아 있었다. 형태만으로 지워지므로 원문항(beauty - sweetly)처럼 명사가 든 짝으로 바꿨다. C의 tastily도 good의 짝인 well로 바꿨다.")

X(3, 94, r="a few·few는 셀 수 있는 명사의 복수형 앞, a little·little은 셀 수 없는 명사 앞에 쓴다. a가 있으면 ‘조금 있는’, 없으면 ‘거의 없는’이다.",
  n=["questions는 셀 수 있고 ‘조금 있다’이므로 a few, money는 셀 수 없고 ‘거의 없다’이므로 little이 알맞으므로", "few는 ‘거의 없는’, a little은 ‘조금 있는’이라 우리말과 반대이므로", "a little은 ‘조금 있는’이라 ‘돈이 거의 없다’와 맞지 않으므로", "few는 ‘거의 없는’이라 ‘질문이 조금 있다’와 맞지 않으므로", "셀 수 있는 questions에 a little, 셀 수 없는 money에 few를 쓸 수 없으므로"],
  st="① 명사가 셀 수 있는지 본다: {0}. 셀 수 있으면 (a) few, 셀 수 없으면 (a) little. → ② 우리말 뜻을 본다: ‘조금 있다’이면 a를 붙이고, ‘거의 없다’이면 a를 뺀다. → ③ {1}. 정답은 {a}.",
  R=("questions는 셀 수 있고 money는 셀 수 없다", "‘질문이 조금 있다’ a few, ‘돈이 거의 없다’ little"), B=("questions는 셀 수 있고 money는 셀 수 없다", "‘질문이 조금 있다’ a few, ‘돈이 거의 없다’ little"),
  C=("friends는 셀 수 있고 time은 셀 수 없다", "‘친구가 몇 명 있다’ a few, ‘시간이 거의 없다’ little"), D=("books는 셀 수 있고 water는 셀 수 없다", "‘책이 거의 없다’ few, ‘물이 거의 없다’ little"),
  E=("pencils는 셀 수 있고 money는 셀 수 없다", "‘연필이 몇 자루 있다’ a few, ‘돈이 거의 없다’ little"), F=("chairs는 셀 수 있고 information은 셀 수 없다", "‘의자가 거의 없다’ few, ‘정보가 거의 없다’ little"))

X(3, 95, r="asleep·alive·alone처럼 a-로 시작하는 형용사는 명사 앞에 쓰지 못하고 보어로만 쓴다. hard는 ‘열심히’, hardly는 ‘거의 ~않다’이다.",
  pre=["학생별 판정: Tom O. -thing 대명사는 형용사가 뒤에서 꾸민다. Lisa X. asleep은 명사 앞에 쓸 수 없다(the sleeping baby). Mark O. 목적격보어 자리의 형용사. Jane X. ‘열심히’는 hard다. Paul O. 빈도부사는 일반동사 앞."],
  n=["Tom의 설명은 옳으므로", "Lisa와 Jane의 설명이 모두 틀렸으므로", "Paul의 설명은 옳으므로", "Tom과 Mark의 설명은 옳으므로", "Paul의 설명은 옳으므로"],
  st="① 학생마다 예문이 옳은 문장인지 먼저 판단한다. 다섯 명 모두 ‘옳은 문장’이라고 했으므로 예문이 틀리면 설명도 틀린다. → ② {0} → ③ 잘못 설명한 학생은 {a}.",
  R="Lisa의 asleep은 명사 앞에 쓸 수 없고(the sleeping baby), Jane의 hardly는 ‘거의 ~않다’라 ‘열심히’(hard)가 아니다. 나머지 세 명의 설명은 옳다.",
  B="Lisa의 the beautifully flower는 명사를 부사로 꾸며 틀렸고(beautiful), Jane의 hardly는 ‘열심히’가 아니라 ‘거의 ~않다’다. Tom만 옳다.",
  C="happy는 look 뒤의 형용사, fast는 -ly 없는 부사, something interesting은 -thing 뒤의 형용사로 세 설명이 모두 옳다.",
  D="Lisa의 She sings beautiful은 동사를 형용사로 꾸며 틀렸다(beautifully). Tom, Jane의 설명은 옳다.",
  E="Jane의 politely는 동사 speaks를 꾸미는 부사인데 형용사라고 했다. Tom, Lisa의 설명은 옳다.",
  F="Lisa의 many homework는 셀 수 없는 명사에 many를 써서 틀렸다(much). Tom, Jane의 설명은 옳다.")
RV(3, 95, "E", fx=True, why="수정 예시의 한 예문(I studied hardly …)이 원문항 Jane의 예문과 같아 다른 예문(He can jump highly.)으로 바꿨다.")

X(3, 96, r="become, look, seem, smell, feel 뒤의 보어 자리에는 부사가 아니라 형용사를 쓴다.",
  n=["부사 famously를 그대로 두었으므로", "become 뒤 보어 자리에 형용사 famous를 썼으므로", "명사 fame을 쓰면 ‘그녀 = 명성’이 되어 어색하므로", "famouser라는 형태는 없으므로", "비교 대상이 없는데 most ~ than을 쓸 수 없으므로"],
  st="① 밑줄 앞의 동사를 본다: {0}. 뒤에 주어의 상태를 설명하는 보어가 온다. → ② 보어 자리에는 부사({1})가 아니라 형용사를 쓴다. → ③ 정답은 {a}.",
  R=("became", "famously"), B=("became", "famously"), C=("looks", "tiredly"), D=("smells", "nicely"), E=("seems", "happily"), F=("became", "darkly"))

X(3, 97, r="high(높이)/highly(매우), late(늦게)/lately(최근에), hard(열심히)/hardly(거의 ~않다)처럼 -ly가 붙으면 뜻이 달라지는 부사가 있다. fast, early는 -ly 없이 부사로 쓴다.",
  n=["highlier라는 형태는 없으므로", "highly는 ‘매우’라는 뜻이라 very를 붙여도 ‘높이’가 되지 않으므로", "highing이라는 형태는 없으므로", "최상급 highest는 우리말 뜻(높이)과 맞지 않으므로", "‘높이’는 high로 쓰므로"],
  st="① 밑줄 친 부사의 뜻을 확인한다: {0}. → ② ‘{1}’라는 뜻의 부사는 {2}다. → ③ 부사만 바르게 고치고 나머지는 그대로 둔 문장을 고른다. 정답은 {n}.",
  R=("highly는 ‘매우’", "높이", "형용사와 형태가 같은 high"), B=("highly는 ‘매우’", "높이", "형용사와 형태가 같은 high"), C=("fastly라는 말은 없다", "빨리", "형용사와 형태가 같은 fast"),
  D=("hardly는 ‘거의 ~않다’", "열심히", "형용사와 형태가 같은 hard"), E=("lately는 ‘최근에’", "늦게", "형용사와 형태가 같은 late"), F=("earlyly라는 말은 없다", "일찍", "형용사와 형태가 같은 early"))
RV(3, 97, "CF", v="수정(내용)", why="정답 확인. 다만 제시문이 서너 낱말뿐이라 원문항(일곱 낱말 + 우리말 뜻)의 절반 길이이고, 오답이 부사가 아니라 동사 형태나 어순을 바꾼 문장(does runs, Runs Tom, getted)이라 부사를 몰라도 형태만으로 지워진다. 발문에 조건이 붙은 점도 원문항과 다르다.", fix="제시문을 늘리고 오답을 부사 자리만 바꾼 문장으로")

X(3, 98, r="many·a few·few는 셀 수 있는 명사의 복수형, much·a little·little은 셀 수 없는 명사에 쓴다. a lot of는 둘 다에 쓴다. quite는 수량 표현이 아니다.",
  n=["셀 수 있는 things에 a little을 쓸 수 없으므로", "셀 수 있는 things에 a little을, 셀 수 없는 work에 many를 쓸 수 없으므로", "quite는 명사 앞에 쓰는 수량 표현이 아니고 work에 many를 쓸 수 없으므로", "things(셀 수 있음)에 a lot of, books(셀 수 있음)에 a few, work(셀 수 없음)에 much가 알맞으므로", "quite는 명사 앞에 쓸 수 없고 books에 little을 쓸 수 없으므로"],
  st="① 빈칸 뒤 명사가 셀 수 있는지 하나씩 본다: {0}. → ② 셀 수 있으면 many·a few·few, 셀 수 없으면 much·a little·little, a lot of는 둘 다 된다. → ③ 세 자리가 모두 맞는 {a}가 정답이다.",
  R="(A) things 셀 수 있음, (B) books 셀 수 있음, (C) work 셀 수 없음", B="(A) things 셀 수 있음, (B) exercises 셀 수 있음, (C) time 셀 수 없음", C="(A) books 셀 수 있음, (B) of them(책들) 셀 수 있음, (C) money 셀 수 없음",
  D="(A) friends 셀 수 있음, (B) of them(친구들) 셀 수 있음, (C) free time 셀 수 없음", E="(A) homework 셀 수 없음, (B) questions 셀 수 있음, (C) time 셀 수 없음", F="(A) apples 셀 수 있음, (B) of them(사과들) 셀 수 있음, (C) water 셀 수 없음")

X(3, 99, r="빈도부사는 be동사·조동사 뒤, 일반동사 앞에 놓는다. rarely·seldom은 ‘좀처럼 ~않다’로 그 자체에 부정의 뜻이 있다.",
  n=["rarely는 ‘좀처럼 ~않다’이고 빈도부사는 문장 맨 뒤가 원칙이 아니므로", "빈도부사의 위치는 주어의 수가 아니라 동사의 종류로 정해지므로", "be동사가 있으면 빈도부사는 그 뒤에 오므로", "rarely 자체에 부정의 뜻이 있어 not을 더하지 않으므로", "빈도부사는 be동사 뒤에 쓰는 것이 기본이므로"],
  st="① 밑줄 친 빈도부사 {0}의 뜻을 확인한다: {1}. → ② 위치를 확인한다: {2}. → ③ 뜻과 위치를 모두 바르게 말한 설명은 {n}.",
  R=("rarely", "‘좀처럼 ~않다’(부정의 뜻 포함)", "be동사 are 뒤"), B=("rarely", "‘좀처럼 ~않다’", "be동사 are 뒤"), C=("usually", "‘보통’", "일반동사 gets 앞"), D=("never", "‘한 번도 ~않다’", "완료형의 has 뒤, 과거분사 seen 앞"),
  E=("often", "‘자주’", "be동사 are 뒤"), F=("seldom", "‘좀처럼 ~않다’", "일반동사 eat 앞"))

X(3, 100, r="much는 셀 수 없는 명사에 쓴다. late(늦게)/lately(최근에)는 뜻이 다르다. 명사는 형용사로, 동사는 부사로 꾸민다.",
  pre=["문장별 판정: ⓐ X. time은 셀 수 없으므로 much. ⓑ O. 권유하는 의문문의 some. ⓒ X. ‘늦게’는 late. ⓓ X. 명사 job은 형용사 difficult로 꾸민다. ⓔ X. 동사 speaks는 부사 fluently로 꾸민다."],
  k="틀린 문장은 ⓐ, ⓒ, ⓓ, ⓔ 네 개다.", n=["틀린 문장은 ⓐ, ⓒ, ⓓ, ⓔ 네 개이므로"] * 5,
  st="① 문장마다 확인할 곳을 정한다: 수량 표현 뒤 명사가 셀 수 있는지, 꾸밈을 받는 말이 명사인지 동사인지, -ly가 붙어 뜻이 달라진 부사가 있는지. → ② {0} → ③ 틀린 문장은 {a}이다.",
  R="ⓐ many time(much), ⓒ lately(late), ⓓ difficulty job(difficult), ⓔ fluent(fluently)가 틀렸다. ⓑ만 옳다.", B="a many time(much), c lately(발문이 준 뜻 ‘늦게’는 late), d seems happily(happy)가 틀렸다. b, e는 옳다.",
  C="d만 틀렸다. homework는 셀 수 없으므로 much homework다.", D="d much books(many)와 e lately(괄호의 뜻 ‘늦게’는 late)가 틀렸다. a, b, c는 옳다.", E="c만 틀렸다. taste 뒤 보어 자리에는 형용사 nice를 쓴다.",
  F="a만 틀렸다. friends는 셀 수 있으므로 many friends다.")
RV(3, 100, "CF", v="수정(내용)", why="정답 확인(개수 판정 맞음). 다만 문장이 서너 낱말뿐이라 원문항(일고여덟 낱말)의 절반 길이다. 보기 기호(a~e)와 선택지 순서도 원문항과 다르다.", fix="문장을 원문항 수준으로 늘리고 형식을 되돌림")
RV(3, 100, "E", v="수정(내용)", why="정답 확인(1개). 다만 문장이 네 낱말 안팎이라 원문항의 절반 길이이고, 보기 기호(a~e)와 선택지 순서도 원문항과 다르다. 또 기존 수정 예시는 정답이 원문항과 같은 4개였다.", fix="문장을 늘리고 형식을 되돌림, 수정 예시는 3개로")
RV(3, 100, "D", fx=True, why="수정 예시의 문장이 서너 낱말뿐이라 원문항의 절반 길이였다. 문장을 원문항 수준으로 늘렸다.")
