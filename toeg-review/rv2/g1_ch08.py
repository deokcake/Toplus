# 1급 CH8 비교 (71~80) 2차 감수
X(1, 71, r="비교급을 강조할 때는 much, far, even, a lot, still을 쓴다. very는 원급을 꾸미며 비교급 앞에는 쓸 수 없다. a little은 ‘조금 더’라는 뜻으로 비교급 앞에 쓸 수 있다.",
  n=["much가 비교급 more interesting을 바르게 강조하므로", "very는 비교급을 강조할 수 없다. much more creative로 고쳐야 하므로", "far가 비교급 faster를 바르게 강조하므로", "even이 비교급 colder를 바르게 강조하므로", "a lot이 비교급 more difficult를 바르게 강조하므로"],
  st="① 문장마다 비교급 바로 앞에 놓인 말을 찾는다: {0}. → ② much, far, even, a lot, a little은 비교급 앞에 쓸 수 있지만 very는 원급만 꾸민다. → ③ {n}은 very 뒤에 비교급({1})이 왔으므로 틀렸다.",
  R=("much, very, far, even, a lot", "more creative"), B=("a little, much, far, much, very", "more reliable"), C=("much, even, a lot, far, very", "more efficient"), D=("much, very, a little, even, far", "taller"),
  E=("very, much, a lot, even, far", "shorter"), F=("very, much, a little, a lot, far", "faster"))

X(1, 72, r="‘the + 최상급’, ‘비교급 + than any other + 단수명사’, ‘비교급 + than all the other + 복수명사’, ‘No other + 단수명사 ~ 비교급 than / as + 원급 + as’는 모두 최상급의 뜻을 나타낸다.",
  n=["최상급으로 ‘이 건물이 가장 높다’는 뜻이므로", "비교급 + than any other + 단수명사로 ‘가장 높다’는 뜻이므로", "비교급 + than all the other + 복수명사로 ‘가장 높다’는 뜻이므로", "No other ~ 비교급 than으로 ‘가장 높다’는 뜻이므로",
     "‘다른 어떤 건물도 이 건물만큼 높다’는 뜻이라 최상급의 뜻이 아니므로"],
  st="① 보기 가운데 최상급 문장을 기준으로 뜻을 잡는다: {0}. → ② 나머지 문장이 같은 뜻인지 하나씩 옮겨 본다. than any other, than all the other, No other ~ as … as는 모두 같은 뜻이다. → ③ {n}만 뜻이 다르다: {1}.",
  R=("이 건물이 도시에서 가장 높다", "‘다른 어떤 건물도 이 건물만큼 높다’"), B=("이 호수가 그 지역에서 가장 깊다", "‘다른 모든 호수가 이 호수만큼 깊다’"), C=("이 산이 한국에서 가장 높다", "‘다른 모든 산이 이 산만큼 높다’"),
  D=("이 강이 그 나라에서 가장 길다", "‘이 강보다 긴 강이 몇 개 있다’"), E=("이 탑이 도시에서 가장 높다", "‘이 탑이 다른 탑들보다 높지 않다’"), F=("이 다리가 도시에서 가장 오래되었다", "‘이 다리가 다른 어떤 다리보다 새것이다’"))

X(1, 73, r="the + 비교급, the + 비교급 / one of the + 최상급 + 복수명사 / No other ~ 비교급 than / 비교급 + than any other + 단수명사는 바른 비교 구문이다. less 뒤에는 원급을 쓰며 -er이나 more를 겹쳐 쓰지 않는다.",
  n=["the + 비교급, the + 비교급 구문을 바르게 썼으므로", "one of the + 최상급 + 복수명사를 바르게 썼으므로", "No other + 단수명사 + 비교급 than을 바르게 썼으므로", "비교급 + than any other + 단수명사를 바르게 썼으므로",
     "less 뒤에 비교급 heavier를 겹쳐 썼다. less heavy로 고쳐야 하므로"],
  st="① 문장마다 어떤 비교 구문인지 확인한다. → ② {0} → ③ {n}은 비교 표시를 두 번 겹쳐 썼다({1}). 바른 형태는 {2}.",
  R=("the + 비교급 ~, the + 비교급(①), one of the + 최상급 + 복수명사(②), No other ~ 비교급 than(③), 비교급 + than any other + 단수명사(④)는 모두 바르다.", "less heavier", "less heavy"),
  B=("the + 비교급 ~, the + 비교급(①), one of the + 최상급 + 복수명사(②), No other ~ 비교급 than(③), 비교급 + than any other + 단수명사(⑤)는 모두 바르다.", "less stricter", "less strict"),
  C=("the + 비교급 ~, the + 비교급(①), one of the + 최상급 + 복수명사(②), 비교급 + than any other + 단수명사(③), less + 원급(⑤)은 모두 바르다.", "less bigger", "less big"),
  D=("the + 비교급 ~, the + 비교급(②), one of the + 최상급 + 복수명사(③), No other ~ 비교급 than(④), less + 원급(⑤)은 모두 바르다.", "less taller", "less tall"),
  E=("비교급 + than any other + 단수명사(①), the + 비교급 ~, the + 비교급(③), one of the + 최상급 + 복수명사(④), less + 원급(⑤)은 모두 바르다.", "less funnier", "less funny"),
  F=("more + 원급 + than(①), the + 비교급 ~, the + 비교급(②), one of the + 최상급 + 복수명사(③), less + 원급(④)은 모두 바르다.", "less more experienced", "less experienced"))
RV(1, 73, "B", v="수정(내용)", why="정답 ④ 확인. ① ‘The new policy is less strict than the old one.’과 ④ ‘The new policy is less stricter than the old one.’이 같은 문장의 옳은 형태·틀린 형태로 함께 나와 대비만으로 답이 드러난다(C4). C~F에서 지적한 결함이 B에도 있다. 보기도 모두 less 구문이라 원문항(여러 비교 구문)보다 단조롭다.", fix="옳은 문장을 원문항처럼 여러 비교 구문의 새 문장으로")

X(1, 74, r="비교급 뒤에서 비교 대상을 이끄는 말은 than이다. as는 as + 원급 + as에서 쓴다.",
  n=["둘을 비교하는 비교급 more talented를 바르게 썼으므로", "비교급 뒤에 than으로 비교 대상을 바르게 이끌었으므로", "‘어느 것을 더 좋아하니’라는 비교급 의문문으로 바르므로", "비교급 more relaxing을 바르게 썼으므로",
     "비교급 more challenging 뒤에는 as가 아니라 than을 써야 하므로"],
  st="① 밑줄마다 비교의 짝을 확인한다. 비교급(more ~, -er, less ~) 뒤에는 than, as + 원급 뒤에는 as가 온다. → ② {0} → ③ {n}은 비교급 뒤에 as를 썼다({1}). as를 than으로 고쳐야 한다.",
  R=("① more talented, ② than Jack, ③ enjoy more, ④ more relaxing은 바르다.", "more challenging as"), B=("① much busier, ② less crowded than, ③ as convenient as, ④ more expensive than은 짝이 맞는다.", "more tiring as"),
  C=("① more difficult, ② far more challenging, ③ as important as, ④ more useful than은 짝이 맞는다.", "more challenging as"),
  D="① 밑줄마다 비교의 짝을 확인한다. 비교급(more ~, -er, less ~) 뒤에는 than, as + 원급 뒤에는 as가 온다. → ② ① far more difficult, ② less difficult than, ③ as important as, ④ much clearer than은 짝이 맞는다. → ③ {n}은 비교급 뒤에 as를 썼고, long의 비교급도 more long이 아니라 longer다. longer than으로 고쳐야 한다.",
  E=("① more demanding, ② far more tiring, ③ as simple as, ④ less crowded than은 짝이 맞는다.", "more relaxing as"), F=("① more stressful, ② much more demanding, ③ as meaningful as, ④ less physical than은 짝이 맞는다.", "more tiring as"))

X(1, 75, r="배수 표현은 ‘배수 + as + 원급 + as’로 쓰고, as ~ as 사이에는 원급을 쓰되 be동사 뒤에는 형용사를 쓴다. 비교급 강조는 far·even·much로 하며, more와 -er을 겹쳐 쓰지 않는다.",
  pre=["문장별 판정: A) O. not so + 원급 + as. B) O. far + 비교급. C) X. as ~ as 사이에는 원급을 쓴다(three times as costly as). D) O. the + 비교급, the + 비교급. E) X. is 뒤에는 부사 quickly가 아니라 형용사 quick을 쓴다. F) O. even + 비교급."],
  k="틀린 문장은 C), E) 두 개다.",
  n=["틀린 문장은 C), E) 두 개이므로"] * 5,
  st="① 문장마다 비교 구문의 틀(as + 원급 + as, 비교급 + than, 강조어 + 비교급, 배수 표현)을 확인한다. → ② {0} → ③ 틀린 문장을 세면 {a}이다.",
  R="C)는 as ~ as 사이에 more를 넣었고, E)는 be동사 뒤에 부사 quickly를 썼다. 나머지 네 문장은 옳다.",
  B="C)는 very로 비교급을 강조했고, D)는 more와 -er을 겹쳐 썼다(more taller). 나머지 네 문장은 옳다.",
  C="D)만 틀렸다. more와 -er을 겹쳐 썼다(much more taller). 나머지 다섯 문장은 옳다.",
  D="C)는 more와 -er을 겹쳐 썼고(more heavier), D)는 less와 more를 겹쳐 썼으며(less more careful), F)는 동사 speaks를 꾸미는 자리에 형용사 fluent를 썼다. 나머지 세 문장은 옳다.",
  E="C)와 F)가 more와 -er을 겹쳐 썼다(more kinder, more cheaper). 나머지 네 문장은 옳다.",
  F="D)는 very로 비교급을 강조했고, E)는 more와 -er을 겹쳐 썼으며(more usefuler), F)는 as ~ as 사이에 비교급 older를 썼다. 나머지 세 문장은 옳다.")

X(1, 76, r="비교급을 강조하는 much, far, even, a little은 비교급 바로 앞에 둔다. 어순은 ‘주어 + 동사 + 강조어 + 비교급 + than + 비교 대상’이다.",
  n=["much가 비교급 cleaner 뒤에 와서 어순이 틀렸으므로", "much가 동사 is 앞에 와서 어순이 틀렸으므로", "is + much + cleaner + than + it was last year의 어순이 바르므로", "than이 it 뒤로 가서 어순이 틀렸으므로", "cleaner가 동사 is 앞에 와서 어순이 틀렸으므로"],
  st="① 주어({0})와 동사({1})를 먼저 세운다. → ② 비교급({2}) 바로 앞에 강조어({3})를 놓고, 그 뒤에 than을 붙인다. → ③ than 뒤에 비교 대상({4})을 이으면 {a}",
  R=("this city", "is", "cleaner", "much", "it was last year"), B=("the new system", "is", "more efficient", "far", "the old one"), C=("this bridge", "is", "stronger", "much", "it was ten years ago"),
  D=("Mina", "is", "taller", "a little", "Jane"), E=("this test", "is", "harder", "even", "yesterday's test"), F=("the city", "is", "cleaner", "much", "it used to be"))

X(1, 77, r="twice as + 원급 + as는 ‘두 배만큼 ~한’, not as + 원급 + as는 ‘~만큼 …하지 않은’이라는 뜻이다. 글에 나온 수치와 비교 표현을 차례로 정리해 크기를 견준다.",
  n=["Sarah의 가방은 Tom의 두 배(4kg)라 더 무거우므로", "Tom의 가방(2kg)이 Mike의 가방(1.5kg)보다 무거우므로", "Sarah의 가방(4kg)이 Mike의 가방(1.5kg)보다 무거우므로", "Mike의 가방(1.5kg)이 Tom의 가방(2kg)보다 가벼우므로",
     "Mike의 가방은 Tom의 가방만큼 무겁지 않다고 했으므로"],
  st="① 글의 수치와 비교 표현을 숫자로 정리한다: {0}. → ② 질문이 묻는 것({1})에 맞는 대상을 찾는다. → ③ {2} 정답은 {n}.",
  R=("Tom 2kg, Sarah는 그 두 배인 4kg, Mike 1.5kg", "Tom의 가방보다 가벼운 것", "2kg보다 가벼운 것은 Mike의 가방뿐이다."),
  B=("A 5L, B는 그 두 배인 10L, C 7L, D는 5L와 7L 사이", "C보다 연료를 많이 쓰는 차", "7L보다 많이 쓰는 것은 B뿐이다."),
  C=("A 1.2kg, B는 그 두 배인 2.4kg, C 1.5kg, D는 1.2kg과 1.5kg 사이", "C보다 무거운 노트북", "1.5kg보다 무거운 것은 B뿐이다."),
  D=("Mina 12초, Jane 13초, Leo 15초, Tom은 12초와 13초 사이", "Jane보다 느리게 달린 사람", "13초보다 오래 걸린 사람은 Leo뿐이다."),
  E=("A 500mL, B는 그 두 배인 1,000mL, C 750mL, D는 500mL와 750mL 사이", "C보다 많이 담는 병", "750mL보다 많이 담는 것은 B뿐이다."),
  F=("A 20m², B는 그 1.5배인 30m², C 25m², D는 20m²와 25m² 사이", "C보다 큰 방", "25m²보다 큰 것은 B뿐이다."))

X(1, 78, r="‘No other + 단수명사 ~ 비교급 than A’, ‘No other ~ as + 원급 + as A’, ‘Nothing ~ 비교급 than A’는 모두 ‘A가 가장 ~하다’는 최상급의 뜻이다. 전환한 문장도 A가 가장 ~하다는 뜻이어야 한다.",
  n=["앞뒤 문장이 모두 ‘시간이 가장 소중하다’는 뜻이라 바른 전환이므로", "앞뒤 문장이 모두 ‘그가 마을에서 가장 똑똑하다’는 뜻이라 바른 전환이므로", "앞뒤 문장이 모두 ‘영어가 내게 가장 쉬운 과목이다’는 뜻이라 바른 전환이므로",
     "앞 문장은 ‘건강이 가장 중요하다’는 뜻인데 뒤 문장은 ‘건강이 가장 덜 중요하다’는 뜻이 되므로", "앞뒤 문장이 모두 ‘이 호수가 이 지역에서 가장 깊다’는 뜻이라 바른 전환이므로"],
  st="① 화살표 앞 문장(No other ~, Nothing ~)을 ‘A가 가장 ~하다’로 옮긴다. → ② 화살표 뒤 문장도 같은 뜻인지 본다. 최상급이거나 ‘비교급 + than any other(anything else)’이면 같은 뜻이다. → ③ {n}은 뒤 문장의 표현({0}) 때문에 뜻이 반대가 된다.",
  R="less important", B="less popular", C="easier", D="slower", E="smaller", F="more expensive")
RV(1, 78, "BCDEF", v="수정(내용)", fx=True, why="원문항이 ‘전환 전 → 전환 후’ 짝을 보여 주는 형식으로 고쳐져, 최상급과 같은 뜻의 한 문장을 고르는 변형은 발문과 보기 형식이 원문항과 다르다(A1·A2). Claude 수정 예시도 옛 형식이라 원문항 형식(전환 전·후 짝 다섯 개, 하나만 뜻이 반대)으로 다시 썼다.", fix="원문항처럼 보기마다 전환 전·후 짝을 싣기")

X(1, 79, r="one of the + 최상급 + 복수명사는 ‘가장 ~한 것들 가운데 하나’라는 뜻이다. 여러 대상 가운데 하나를 가리키므로 명사는 복수형을 쓴다.",
  n=["one of the + 최상급 뒤에는 단수가 아니라 복수명사를 쓰므로", "여러 명의 똑똑한 학생들 가운데 한 명이라는 뜻이라 복수형을 쓴다고 바르게 설명했으므로", "I have ever taught는 부사구가 아니라 students를 꾸미는 관계사절이고, 생략된 것은 목적격 관계대명사이므로",
     "one은 ‘~ 가운데 하나’를 뜻하는 대명사이고 보어는 one of ~ students 전체이므로", "최상급 앞의 the는 생략하지 않으며 smart의 최상급은 smartest가 맞으므로"],
  st="① 밑줄을 ‘one + of + the 최상급({0}) + 복수명사({1})’로 나눈다. → ② ‘가장 ~한 여럿 가운데 하나’라는 뜻이므로 of 뒤의 명사는 복수여야 한다. → ③ 명사를 단수로 써야 한다거나 최상급·the·one을 다르게 설명한 보기를 지운다. 정답은 {n}.",
  R=("smartest", "students"), B=("fastest", "runners"), C=("most creative", "designers"), D=("most useful", "books"), E=("best", "students"), F=("largest", "cities"))
RV(1, 79, "B", v="수정(내용)", why="정답 ⑤ 확인. 보기가 ‘one of는 정확히 두 개 중 하나만 뜻한다’처럼 짧고 뻔한 일반 설명이어서, 밑줄 친 표현을 짚어 이유까지 설명하는 원문항보다 보기 수준이 낮다(B3). 사용자가 1-60 B에 준 의견(선택지 품질이 원문항보다 낮음)과 같은 문제다.", fix="원문항처럼 표현을 짚고 이유를 밝힌 그럴듯한 설명으로")

X(1, 80, r="as ~ as 사이에는 원급을 쓰되, 그 자리가 형용사 자리인지 부사 자리인지 따져야 한다. look, feel, seem, sound, become, be 뒤는 형용사 자리이고, 일반동사를 꾸미는 자리는 부사 자리이다.",
  pre=["밑줄별 판정: (A) X. worked를 꾸미므로 부사 carefully를 써야 한다. (B) O. solve를 꾸미는 부사 quickly. (C) O. looked 뒤의 형용사 satisfied. (D) X. felt 뒤에는 형용사 proud를 써야 한다. (E) O. became 뒤의 형용사 valuable."],
  k="틀린 것은 (A), (D)이다.",
  n=["(B)는 옳으므로", "(B), (C) 모두 옳으므로", "틀린 (A), (D)만 골랐으므로", "(C)는 옳으므로", "(E)는 옳으므로"],
  st="① 밑줄마다 as ~ as 앞의 동사를 본다. 일반동사를 꾸미면 부사 자리, look·feel·seem·sound·become 뒤면 형용사 자리다. → ② {0} → ③ 틀린 두 곳을 모은 {a}를 고른다.",
  R="(A) worked 뒤는 부사 자리인데 형용사 careful을, (D) felt 뒤는 형용사 자리인데 부사 proudly를 썼다.",
  B="(B) run 뒤는 부사 자리인데 형용사 quick을, (D) felt 뒤는 형용사 자리인데 부사 confidently를 썼다.",
  C="(B) looked 뒤는 형용사 자리인데 부사 calmly를, (E) finished her daily reports 뒤는 부사 자리인데 형용사 neat를 썼다.",
  D="(C) wrote her answers 뒤는 부사 자리인데 형용사 clear를, (D) sounded 뒤는 형용사 자리인데 부사 warmly를 썼다.",
  E="(A) worked 뒤는 부사 자리인데 형용사 efficient를, (E) spoke 뒤는 부사 자리인데 형용사 polite를 썼다.",
  F="(B) sounded 뒤는 형용사 자리인데 부사 sweetly를, (C) spoke 뒤는 부사 자리인데 형용사 fluent를 썼다.")
