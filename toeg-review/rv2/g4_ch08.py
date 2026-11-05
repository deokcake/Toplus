# 4급 CH8 비교 구문 (71~80) 2차 감수
X(4, 71, r="비교급·최상급: 짧은 단어는 -er/-est, 자음 + y는 y를 i로(easier), 단모음 + 단자음은 자음을 겹치고(hotter), 긴 단어는 more/most. good - better - best는 불규칙이다.",
  n=["-er, -est를 붙인 옳은 형태이므로", "y를 i로 바꾸고 -er, -est를 붙인 옳은 형태이므로", "t를 겹쳐 쓰고 -er, -est를 붙인 옳은 형태이므로", "긴 단어라 more, most를 붙인 옳은 형태이므로", "good은 불규칙 변화라 better, best로 써야 하므로"],
  st="① 불규칙으로 변하는 낱말(good, bad, many, little, far)이 있는지 먼저 본다. → ② 나머지는 규칙(-er/-est, y → i, 자음 겹치기, more/most)대로인지 본다. → ③ {0} 정답은 {n}.",
  R="good - better - best인데 gooder, goodest로 썼다.", B="good - better - best인데 ④는 gooder, goodest로 썼다.", C="bad - worse - worst인데 ④는 badder, baddest로 썼다.", D="many - more - most인데 ①은 manyer, manyest로 썼다.",
  E="양을 나타내는 little은 less - least인데 ①은 littler, littlest로 썼다.", F="far - farther - farthest인데 ④는 farer, farest로 썼다.")

X(4, 72, r="than 앞에는 비교급을 쓴다. 양을 나타내는 little의 비교급은 less다(little - less - least).",
  n=["양을 나타내는 little의 비교급은 littler가 아니라 less이므로", "little의 불규칙 비교급 less가 알맞으므로", "lesser는 ‘덜 중요한’이라는 뜻의 형용사로 양의 비교에 쓰지 않으므로", "least는 최상급이라 than과 함께 쓸 수 없으므로", "little의 비교급은 more little이 아니라 less이므로"],
  st="① 빈칸 뒤의 than을 본다. than 앞에는 비교급이 온다. → ② 괄호 안 낱말의 비교급을 떠올린다: {0}. → ③ 정답은 {a}.",
  R="little(양이 적은) - less - least", B="bad - worse - worst", C="little - less - least", D="many - more - most", E="good - better - best", F="fast - faster - fastest")
RV(4, 72, "C", fx=True, why="수정 예시의 정답 낱말(little → less)이 원문항과 같아, 낱말을 far로 바꿔(far → farther) 새로 썼다.")

X(4, 73, r="비교급은 much, even, far, a lot, a little로 꾸민다. very, so, too는 비교급 앞에 쓰지 않는다.",
  n=["much는 비교급을 강조할 수 있으므로", "even은 비교급을 강조할 수 있으므로", "very는 원급을 꾸미고 비교급 앞에는 쓰지 않으므로", "a lot은 비교급을 강조할 수 있으므로", "far는 비교급을 강조할 수 있으므로"],
  st="① 빈칸 뒤가 비교급({0})이다. → ② 비교급 앞에 쓸 수 있는 말(much, even, far, a lot, a little)을 지운다. → ③ 남는 {a}는 비교급 앞에 쓸 수 없다.",
  R="taller", B="younger", C="taller", D="faster", E="heavier", F="bigger")
RV(4, 73, "C", fx=True, why="수정 예시의 정답 낱말(very)이 원문항과 같아, 정답을 more(older 앞에 겹쳐 쓸 수 없음)로 바꿨다.")

X(4, 74, r="-er/-est와 more/most를 겹쳐 쓰지 않는다. fat의 최상급은 fattest다.",
  n=["긴 단어 interesting에 more를 쓴 옳은 문장이므로", "funny의 최상급 funniest를 쓴 옳은 문장이므로", "most와 -est를 겹쳐 썼고 철자도 fattest가 되어야 하므로", "young의 최상급 youngest를 쓴 옳은 문장이므로", "tall의 비교급 taller를 쓴 옳은 문장이므로"],
  st="① 문장마다 비교급·최상급의 형태를 본다. → ② more/most와 -er/-est가 겹쳤는지, 불규칙 변화를 규칙형으로 쓰지 않았는지 확인한다. → ③ {0} 정답은 {n}.",
  R="③은 most와 -est를 겹쳐 썼다. the fattest가 맞다.", B="⑤의 beautiful은 긴 단어라 -est를 붙이지 않는다. the most beautiful이 맞다.", C="⑤는 most와 -est를 겹쳐 썼다. the fattest가 맞다.", D="①은 more와 -er을 겹쳐 썼다. taller가 맞다.",
  E="④는 most와 -est를 겹쳐 썼다. the easiest가 맞다.", F="④의 good은 불규칙 변화다. better가 맞다.")
RV(4, 74, "C", fx=True, why="수정 예시의 틀린 문장(My bag is more heavy than yours.)이 원문항 4-75의 ⓐ(This bag is more heavy than that bag.)와 닮아 다른 문장(This puzzle is more easy than that one.)으로 바꿨다.")

X(4, 75, r="heavy의 비교급은 heavier, hard의 최상급은 hardest다(more/most를 쓰지 않는다). 긴 단어는 more/most를 쓰고, 비교급은 much로 강조한다.",
  pre=["문장별 판정: ⓐ X. heavy의 비교급은 heavier. ⓑ O. cold의 비교급 colder. ⓒ O. much + more expensive. ⓓ O. young의 최상급 youngest. ⓔ X. hard의 최상급은 the hardest."],
  k="옳은 문장은 ⓑ, ⓒ, ⓓ 세 개다.", n=["옳은 문장은 ⓑ, ⓒ, ⓓ 세 개이므로"] * 5,
  st="① 밑줄마다 낱말의 길이를 본다. 짧은 낱말(1음절, -y로 끝나는 2음절)은 -er/-est, 긴 낱말은 more/most다. → ② 둘을 겹쳐 쓰지 않았는지, 불규칙 변화를 바르게 썼는지 본다. → ③ {0} 옳은 문장은 {a}이다.",
  R="ⓐ more heavy(heavier), ⓔ the most hard(the hardest)가 틀렸다.", B="b the most cheapest(the cheapest)만 틀렸다.", C="a more heavier(heavier), e gooder(better)가 틀렸다.", D="b more taller(taller), e worser(worse)가 틀렸다.",
  E="d more happier(happier)만 틀렸다.", F="c the most kindest(the kindest)만 틀렸다.")
RV(4, 75, "D", fx=True, why="수정 예시의 정답이 원문항과 같은 3개(③)여서, ⓒ를 틀린 문장(the most prettiest)으로 바꿔 2개로 했다.")
RV(4, 75, "E", fx=True, why="수정 예시가 ⓓ를 옳은 문장으로 바꿔 틀린 문장이 하나도 없는 5개가 되어 있었다. ⓓ를 원래의 틀린 문장(more happier)으로 되돌려 4개로 했다.")

X(4, 76, r="than 앞에는 비교급을 쓴다. bad의 비교급은 worse다(bad - worse - worst).",
  n=["원급 bad는 than과 함께 쓸 수 없으므로", "bad는 불규칙 변화라 badder로 쓰지 않으므로", "baddest라는 형태는 없으므로", "bad의 불규칙 비교급 worse가 알맞으므로", "worst는 최상급이라 than과 함께 쓸 수 없으므로"],
  st="① 괄호 속 우리말이 ‘더 ~한’이고 뒤에 than이 있으므로 비교급 자리다. → ② {0} → ③ 정답은 {a}.",
  R="‘나쁜’은 bad, 비교급은 불규칙 변화 worse다.", B="‘(양이) 적은’은 little, 비교급은 불규칙 변화 less다.", C="‘나쁜’은 bad, 비교급은 불규칙 변화 worse다.", D="‘좋은’은 good, 비교급은 불규칙 변화 better다.",
  E="‘많은’은 much, 비교급은 불규칙 변화 more다.", F="‘먼’은 far, 비교급은 불규칙 변화 farther다.")

X(4, 77, r="‘단모음 + 단자음’으로 끝나는 형용사는 끝 자음을 겹쳐 쓰고 -er/-est를 붙인다(hot - hotter - hottest). 자음 + y는 y를 i로 바꾼다.",
  n=["비교급의 철자가 hoter가 아니라 hotter이므로", "최상급의 철자가 hotest가 아니라 hottest이므로", "than 앞에 비교급 hotter, the 뒤에 최상급 hottest가 알맞으므로", "비교급과 최상급의 자리를 바꿔 썼으므로", "than 앞에 원급 hot을 쓸 수 없으므로"],
  st="① 첫 빈칸은 than 앞이므로 비교급, 둘째 빈칸은 the 뒤이므로 최상급이다. → ② 철자 규칙을 확인한다: {0}. → ③ 정답은 {a}.",
  R="hot은 단모음 + 단자음이라 t를 겹쳐 hotter, hottest", B="happy는 자음 + y라 y를 i로 바꿔 happier, happiest", C="hot은 t를 겹쳐 hotter, hottest", D="big은 단모음 + 단자음이라 g를 겹쳐 bigger, biggest",
  E="heavy는 자음 + y라 y를 i로 바꿔 heavier, heaviest", F="easy는 자음 + y라 y를 i로 바꿔 easier, easiest")

X(4, 78, r="최상급: 짧은 단어는 the + -est, 긴 단어는 the most + 원급. most와 -est를 겹쳐 쓰지 않는다. bad의 최상급은 worst다.",
  n=["most와 -est를 겹쳐 쓸 수 없으므로", "difficult는 긴 단어라 the most difficult로 써야 하므로", "긴 단어 interesting에 the most를 쓴 옳은 형태이므로", "most와 -est를 겹쳐 쓸 수 없으므로", "bad의 최상급은 the worst이므로"],
  st="① 밑줄마다 형용사가 짧은 낱말인지 긴 낱말인지 가른다. → ② 짧으면 -er/-est만, 길면 more/most만 쓴다. 둘을 겹치거나 긴 낱말에 -est를 붙인 것을 지운다. → ③ {0} 정답은 {n}.",
  R="③만 긴 낱말 interesting에 the most를 써서 맞다.", B="①만 pretty의 최상급 the prettiest로 맞다.", C="①만 긴 낱말 interesting에 the most를 써서 맞다.", D="⑤만 tall의 비교급 taller로 맞다.", E="③만 easy의 비교급 easier로 맞다.",
  F="③만 good의 최상급 the best로 맞다.")

X(4, 79, r="비교급 + than: ‘~보다 더 …한(하게)’. than은 비교의 대상을 잇는다. early의 비교급은 y를 i로 바꾼 earlier다.",
  n=["earlier는 원급이 아니라 비교급이므로", "than은 ‘~보다’라는 뜻으로 비교의 대상을 잇는 것이 맞으므로", "y를 i로 바꾸고 -er을 붙였으므로", "then은 ‘그때’라는 다른 낱말이므로", "earlier는 최상급이 아니라 비교급이므로"],
  st="① 밑줄을 둘로 나눈다: 비교급({0}) + than. → ② 비교급은 ‘더 ~한(하게)’, than은 ‘~보다’로 뒤에 비교 대상({1})이 온다. → ③ 이를 바르게 말한 것은 {n}.",
  R=("earlier", "my friend"), B=("easier", "the last one"), C=("earlier", "my friend"), D=("taller", "Ben"), E=("heavier", "that one"), F=("faster", "Amy"))
RV(4, 79, "C", fx=True, why="수정 예시의 정답 설명(than은 ‘~보다’라는 뜻으로 비교의 대상을 연결한다)이 원문항의 정답 설명과 같고 위치도 ②로 같았다. 정답 설명을 비교급의 형태(later는 late에 -r을 붙인 비교급)로 바꿨다.")

X(4, 80, r="최상급에 most와 -est를 겹쳐 쓰지 않는다. bad의 최상급은 worst, 긴 단어는 the most + 원급이다.",
  pre=["문장별 판정: (가) X. the cheapest. (나) O. old의 최상급 oldest. (다) O. big의 최상급 biggest. (라) X. the worst. (마) O. 긴 단어 popular에 the most."],
  n=["(나), (다), (마)가 모두 옳으므로", "(가)가 틀렸으므로", "(라)가 틀렸으므로", "(가)가 틀렸으므로", "(라)가 틀렸으므로"],
  st="① 문장마다 비교급·최상급의 형태만 본다. → ② more/most와 -er/-est를 겹쳐 쓴 문장, 불규칙 변화를 규칙형으로 쓴 문장을 지운다. → ③ {0} 옳은 문장만 묶은 {a}가 정답이다.",
  R="(가) the most cheapest, (라) the most baddest가 틀렸다.", B="(나) more taller만 틀렸다.", C="(가) the most cheapest, (라) more better가 틀렸다.", D="(다) more prettier만 틀렸다.", E="(다) gooder, (마) more bigger가 틀렸다.",
  F="(다) the most kindest만 틀렸다.")
RV(4, 80, "C", fx=True, why="수정 예시의 (나)(It is the most cheapest bag.)가 원문항 (가)(It is the most cheapest shirt in the store.)와 닮아 다른 문장(This is the most smallest room.)으로 바꿨다.")
