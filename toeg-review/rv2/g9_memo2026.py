# 2026-10-06 B유형 전급수 감수 메모 반영: 원문항이 바뀐 문항의 해설 기록(X)과, 수정 예시와 어긋나 있던 유형별 풀이 순서 칸을 고친다.
# (rv2build.load()가 g*.py를 이름순으로 읽으므로 이 파일이 마지막에 실행된다.)
def U(g_, n_, **kw): EX[(g_, n_)].update(kw)
def N(g_, n_, i, text): EX[(g_, n_)]["n"][i - 1] = text

# ---- 원형 문항이 바뀐 것 ----
N(1, 58, 1, "from이 동사 뒤에 왔고 eat을 eats로 바꿔 동명사도 아니므로")
N(1, 58, 4, "from 뒤에는 동명사 eating을 써야 하는데 3인칭 단수형 eats를 썼으므로")
U(1, 70, st="① 분사구문의 형태를 본다: 분사(-ing·과거분사)가 있어야 하고, 주절과 다른 주어는 분사 바로 앞에 밝힌다(‘주어 + 분사 ~, 주절’). → ② 분사의 모양이 틀렸거나, 분사구문 뒤에 접속사(so, and, but)를 붙였거나, 주어의 자리가 틀린 보기를 지운다. → ③ 남는 {n}은 {0}")
N(1, 98, 3, "주절의 어순이 would rich be로 틀렸으므로")
N(1, 98, 4, "if를 생략했으면 Had를 주어 앞으로 보내야 하는데 평서문 어순 그대로 두 절을 이었으므로")
N(1, 98, 5, "도치할 때는 Had + 주어 + 과거분사 순서인데 Had inherited he로 썼으므로")
U(1, 98, st="① 주어진 낱말에 if, had, 쉼표, would, now가 있다. ‘If + 주어 + had + 과거분사 ~, 주어 + would + 동사원형 ~ now’(혼합가정법)의 틀을 떠올린다. → ② if절({0})은 과거의 일, 주절({1})은 지금의 일이다. → ③ if·had의 자리가 틀렸거나 주절이 의문문 어순인 보기를 지운다. 정답은 {n}.",
  R="① 주어진 낱말에 if가 없고 had와 쉼표가 있다. if를 생략한 도치 문장(Had + 주어 + 과거분사 ~,)을 떠올린다. → ② 쉼표 뒤 주절은 now가 있으므로 would + 동사원형(would be rich now)이다. → ③ 도치하지 않은 보기와 어순이 틀린 보기를 지운다. 정답은 {n}.")
U(3, 91, st="① 우리말에서 형용사가 꾸미는 말을 찾는다: {0}. → ② 영어 문장에서 그 말은 {1}이다. 형용사는 관사와 명사 사이, 곧 명사 바로 앞에 놓는다. → ③ 정답은 {1} 바로 앞의 번호인 {n}이다.",
  B="① 우리말에서 형용사가 꾸미는 말을 찾는다: ‘따뜻한 것’. → ② 영어 문장에서 그 말은 something이다. -thing으로 끝나는 대명사는 형용사가 바로 뒤에서 꾸민다(something warm). → ③ 정답은 something 바로 뒤의 번호인 {n}이다.",
  C=("‘재미있는 책’", "books"), D=("‘예쁜 드레스’", "dresses"),
  E="① 우리말에서 형용사가 꾸미는 말을 찾는다: ‘중요한 무언가’. → ② 영어 문장에서 그 말은 something이다. -thing으로 끝나는 대명사는 형용사가 바로 뒤에서 꾸민다(something important). → ③ 정답은 something 바로 뒤의 번호인 {n}이다.",
  F=("‘아름다운 꽃’", "flowers"))
N(3, 108, 2, "도시 이름 Seoul 앞에 The를 쓰고 최상급 largest 앞의 the가 빠졌으므로")
N(3, 108, 4, "the가 one 앞에 와서 one of the + 최상급 어순이 깨졌으므로")
N(3, 108, 5, "‘가장 ~한 것 중 하나’는 비교급 larger가 아니라 최상급 largest를 쓰므로")
N(4, 92, 1, "big dogs처럼 형용사 + 복수명사가 있어 What이 들어가므로")
N(4, 92, 5, "wonderful weather처럼 형용사 + 명사가 있어 What이 들어가므로")
U(4, 92, B="③만 interesting 뒤에 명사 없이 the book is가 온다. How가 들어간다.", C="①만 quiet 뒤에 명사 없이 the room is가 온다. How가 들어간다.",
  D="③만 long bridges처럼 명사가 있어 What이 들어간다. 나머지는 형용사·부사 뒤에 바로 주어 + 동사가 와서 How다.", E="②만 delicious 뒤에 명사 없이 this cake is가 온다. How가 들어간다.",
  F="⑤만 nice shoes처럼 명사가 있어 What이 들어간다. 나머지는 How다.")
U(5, 82, st="① 우리말을 영어 어순으로 옮긴다: {0} → ② in은 ‘{1}’에 해당하므로 그 장소 표현의 맨 앞, 곧 장소 명사 바로 앞 번호에 넣는다. → ③ 정답은 {n}.")
N(6, 6, 3, "two 뒤에는 복수형 oranges가 와야 하므로"); N(6, 6, 4, "many 뒤에는 복수형 oranges가 와야 하므로"); N(6, 6, 5, "three 뒤에는 복수형 oranges가 와야 하므로")
U(6, 6, st="① 빈칸 뒤가 단수명사({0})이므로 a나 an이 필요하다. 둘 이상을 나타내는 말(two, three, many)을 지운다. → ② {0}의 첫소리는 {1}. → ③ 정답은 {a}.")
N(6, 16, 5, "isn't는 is의 부정형이라 주어 You에 맞지 않으므로")
U(6, 16, st="① 주어를 본다: {0}. → ② 그 주어에 맞는 현재형 be동사는 {1}. → ③ 원형 be와 주어에 맞지 않는 형태(부정형 포함)를 지운다. 정답은 {n}.")
U(6, 20, r="this/that은 한 개, these/those는 여러 개를 가리키고 be동사도 is/are로 맞춘다.",
  R=("Those are + socks(여러 개) / That is + hat(한 개)", "② Those는 멀리 있는 여러 개이고 are와 쓴다."))
N(6, 20, 2, "Those는 멀리 있는 여러 개를 가리키고 복수 be동사 are와 함께 쓰므로")
U(6, 21, r="be동사의 과거형은 was, were다. 주어가 I·3인칭 단수면 was, you·복수면 were를 쓴다.",
  n=["am은 현재형이므로", "3인칭 단수 주어 She에 맞는 과거형이므로", "were는 you·복수 주어에 쓰는 과거형이므로", "be는 원형이므로", "is는 현재형이므로"],
  st="① 주어를 본다: {0}. → ② 과거를 나타내는 말({1})이 있으므로 과거형 was/were 가운데 주어에 맞는 것을 고른다. → ③ 현재형·원형과 주어에 맞지 않는 과거형을 지운다. 정답은 {n}.",
  R=("She(3인칭 단수)", "yesterday"), B=("I", "yesterday"), C=("They(복수)", "last Sunday"), D=("We(복수)", "last week"), E=("The weather(단수)", "last night"), F=("you", "last night"))
U(6, 41, r="규칙 과거형: 대부분 -ed, 자음 + y는 y를 i로 바꾸고 -ed(cried), 단모음 + 단자음은 자음을 겹쳐 -ed(shopped), 모음 + y는 그대로 -ed(played).")
N(6, 41, 5, "-ed를 붙인 옳은 형태이므로")
U(6, 45, r="현재의 문장을 과거로 바꿀 때는 동사를 과거형으로 바꾼다. 규칙 동사는 -ed를 붙이되 자음 + y는 y를 i로 바꾸고(study - studied), 단모음 + 단자음은 자음을 겹친다(stop - stopped).",
  n=["study는 자음 + y라 y를 i로 바꿔 studied로 써야 하므로", "did와 과거형을 함께 쓰지 않으므로", "study의 과거형 studied를 바르게 썼으므로", "yesterday가 있는데 현재형 studies를 썼으므로", "과거형이 아니고 주어 He와도 맞지 않으므로"],
  R=("studies", "studied(y를 i로 바꾸고 -ed)"), B=("play", "played(모음 + y는 그대로 -ed)"), C=("wants", "wanted"), D=("watch", "watched"), E=("walks", "walked"), F=("stops", "stopped(자음을 겹쳐 -ed)"))

# ---- 수정 예시가 바뀌어 유형별 풀이 순서 칸을 맞춘 것 ----
U(1, 47, B=("35도가 넘는 날 마라톤을 했으니 지친 것은 당연한 결과다", "Needless to say(말할 필요도 없이)"))
U(2, 80, B="(B)의 bored를 학생들이 남을 지루하게 ‘만들었다’는 뜻으로 풀었다. 지루함을 ‘느낀’ 쪽이다", F="(A)의 disappointing을 disappointed로 바꿔도 뜻이 같다고 했다. 바꾸면 결과가 실망을 ‘느낀다’는 뜻이 된다")
U(2, 81, B="our school은 장소, all the guides는 복수의 구성원이다")
U(2, 82, st="① 빈칸 뒤가 비교급({0})이다. ‘훨씬’이라는 뜻으로 비교급을 강조하는 말은 much, even, far, still, a lot 등이다. → ② very, too, so, most는 원급을 꾸미는 말이라 비교급 앞에 쓸 수 없다. → ③ 들어갈 수 없는 것은 {n}({a})이다.")
U(3, 100, B="ⓑ looked at me angry(angrily), ⓒ always am(am always), ⓔ much eggs(many)가 틀렸다. ⓐ, ⓓ는 옳다.", D="ⓓ much books(many), ⓔ drove careful(carefully)이 틀렸다. ⓐ, ⓑ, ⓒ는 옳다.",
  E="ⓐ a little chairs(a few), ⓑ fluent(fluently), ⓒ tastes nicely(nice)가 틀렸다. ⓓ, ⓔ는 옳다.", F="ⓐ much friends(many), ⓑ looks happily(happy), ⓒ fastly(fast), ⓓ few money(little), ⓔ cold something(something cold)이 모두 틀렸다.")
U(4, 20, B="(B) their's(theirs), (C) The news are(is)가 틀렸다. (A), (D)는 옳다.", C="(B) are(is), (C) their(theirs), (D) my(mine)가 틀렸다. (A)는 옳다.",
  E="(A) Jane and I am(are), (C) Who's(Whose)가 틀렸다. (B), (D)는 옳다.", F="(A) The children is(are), (C) her's(hers), (D) my(mine)가 틀렸다. (B)는 옳다.")
U(4, 25, B=("don't 뒤이므로 watches를 동사원형 watch로 고친다.", "주어 they는 복수이므로 의문문은 Does가 아니라 Do로 시작한다."),
  C=("주어 Tom은 3인칭 단수이므로 don't 대신 doesn't를 쓴다.", "주어 They는 복수이므로 studies를 동사원형 study로 고친다."),
  D=("doesn't 뒤이므로 likes를 동사원형 like로 고친다.", "Does 뒤에도 동사원형이 오므로 plays를 play로 고친다."),
  F=("주어 she는 3인칭 단수이므로 의문문은 Does로 시작한다.", "주어 They는 복수이므로 doesn't 대신 don't를 쓴다."))
U(4, 28, B=("Do + your friends(복수) + play(동사원형) ~?", "소민만 Do 뒤의 동사를 plays로 써야 한다고 해서 틀렸다."),
  C=("Does + your sister(3인칭 단수) + walk(동사원형) ~?", "은우만 진행형 문장이라고 해서 틀렸다. Does + 동사원형은 현재의 습관을 묻는다."),
  D=("Does + Tom(3인칭 단수) + study(동사원형) ~?", "예은만 Does 뒤에 과거형을 써야 한다고 해서 틀렸다."),
  E=("Do + you + need(동사원형) ~?", "건우만 be동사를 함께 써야 한다고 해서 틀렸다. 일반동사 의문문에는 be동사를 쓰지 않는다."),
  F=("Does + Jane(3인칭 단수) + like(동사원형) ~?", "소율만 3인칭 단수 질문에 Do를 써야 한다고 해서 틀렸다."))
U(4, 53, B="①이 틀렸다. 능력의 can은 have to가 아니라 be able to로 바꿔 쓴다.")
U(4, 65, B="ⓑ many money(much money), ⓒ always is(is always)가 틀렸다. ⓐ, ⓓ는 옳다.", C="ⓐ much milks(much milk), ⓓ never is(is never)가 틀렸다. ⓑ, ⓒ는 옳다.",
  D="ⓐ sometimes plays(play), ⓑ many money(much money)가 틀렸다. ⓒ, ⓓ는 옳다.", E="ⓒ much pencils(many pencils), ⓓ goes always(always goes)가 틀렸다. ⓐ, ⓑ는 옳다.",
  F="ⓐ many water(much water), ⓒ seldom watch(watches)가 틀렸다. ⓑ, ⓓ는 옳다.")
U(4, 70, B="(c) many homework(much), (e) a little friends(a few)가 틀렸다.", C="(b) a few bread(a little), (d) much friends(many)가 틀렸다.", D="(c) a little books(a few), (d) few money(little)가 틀렸다.",
  E="(a) much apples(many), (c) a few water(a little)가 틀렸다.", F="(a) a little questions(a few), (e) a few rice(a little)가 틀렸다.")
U(4, 75, C="ⓐ more heavier(heavier), ⓒ the most tall(the tallest), ⓔ more fast(faster)가 틀렸다.", D="ⓑ more taller(taller), ⓒ the most prettiest(the prettiest), ⓔ worser(worse)가 틀렸다.",
  F="ⓑ more heavier(heavier), ⓒ the most kindest(the kindest), ⓓ the most fast(the fastest), ⓔ more better(better)가 틀렸다. ⓐ만 옳다.")
U(4, 80, B="(나) more taller, (마) the most smallest가 틀렸다.", C="(나) the most smallest, (라) more better가 틀렸다.", D="(다) more prettier, (마) more hotter가 틀렸다.",
  E="(가) more heavier, (다) gooder가 틀렸다.", F="(다) the most kindest, (라) more easier가 틀렸다.")
U(4, 109, B="(가) Tom laughed, (다) We went가 1형식이다.", C="(가) There is a bank, (라) Birds fly가 1형식이다.", D="(나) The baby sleeps, (라) The train arrived가 1형식이다.",
  E="(나) The dog ran, (다) There is a cat이 1형식이다.", F="(다) The train stopped, (라) The baby cried가 1형식이다.")
U(5, 22, B="speak는 불규칙 동사라 과거형이 spoke다. speaked는 없는 형태다.")
U(6, 2, B="butter는 물질이라 셀 수 없다(a piece of butter).")
U(6, 5, B="hour는 h를 발음하지 않아 모음 소리로 시작하므로 an hour다.")
U(6, 64, B="②의 cans는 없는 형태다. 주어가 Jane이어도 can이다.", C="①의 musts는 없는 형태다. 주어가 She여도 must다.", D="③의 shoulds는 없는 형태다. 주어가 Tom이어도 should다.",
  E="④의 mays는 없는 형태다. 주어가 She여도 may다.", F="⑤의 cans는 없는 형태다. 주어가 Tom이어도 can이다.")
U(6, 91, B="sit은 단모음 + 단자음이라 sitting이다.", D="put은 단모음 + 단자음이라 putting이다.", F="shop은 단모음 + 단자음이라 shopping이다.")
U(7, 85, B="⑤는 can 뒤에 is를 썼다(원형은 be).", C="④는 can 뒤에 is를 썼다(원형은 be).")

# ---- 검토 후 추가: 수정 예시와 어긋나 있던 풀이 순서 칸 ----
U(3, 92, B=("일반동사 walk", "일반동사 walk 앞이다"), C=("be동사 is", "be동사 is 뒤, tired 앞이다"), D=("일반동사 play", "일반동사 play 앞이다"), E=("일반동사 get", "일반동사 get 앞이다"), F=("be동사 is", "be동사 is 뒤, crowded 앞이다"))
U(3, 108, B="old → oldest, building → buildings", F="long → longest, river → rivers")
U(3, 102, B="⑤는 Minsu가 더 크다고 했는데 Minsu는 168cm, Jiho는 172cm다.")
U(3, 140, B="① (A): Let's ~ 뒤의 부가의문문은 shall we다. → ② (B): 뒤에 about + -ing가 있으므로 How about ~?(~하는 게 어때?)이다. → ③ (C): 형용사 exciting만 있고 명사가 없으므로 How다. 정답은 {a}.",
  C="① (A): 명령문(Please close ~) 뒤의 부가의문문은 will you다. → ② (B): 뒤에 don't we + 동사원형이 있으므로 Why don't we ~?다. → ③ (C): a great idea처럼 ‘a + 형용사 + 명사’가 있으므로 What이다. 정답은 {a}.",
  D="① (A): Let's ~ 뒤의 부가의문문은 shall we다. → ② (B): 뒤에 don't we + 동사원형이 있으므로 Why don't we ~?다. → ③ (C): 형용사 clean 뒤에 바로 they will look이 오므로 How다. 정답은 {a}.",
  E="① (A): 명령문(Pass me ~) 뒤의 부가의문문은 will you다. → ② (B): 뒤에 about + -ing가 있으므로 How about ~?이다. → ③ (C): a good cook처럼 ‘a + 형용사 + 명사’가 있으므로 What이다. 정답은 {a}.",
  F="① (A): Let's ~ 뒤의 부가의문문은 shall we다. → ② (B): 뒤에 about + -ing가 있으므로 What about ~?(~하는 게 어때?)이다. → ③ (C): 형용사 beautiful 뒤에 바로 the sunset is가 오므로 How다. 정답은 {a}.")
U(4, 22, C=("Mom and Dad는 복수이므로 are", "The weather는 단수이므로 is"))
U(4, 30, C="(A) My aunt 단수, (B) She 단수, (C) Her students 복수")
U(4, 45, B="ⓓ won't studies(study)만 틀렸다.", C="ⓑ not will(will not), ⓒ Tom going to(is going to), ⓓ wills(will), ⓔ visiting(visit)이 틀렸다. ⓐ만 옳다.",
  D="ⓑ Tom going to(is going to), ⓔ Does she going to(Is she going to)가 틀렸다.", E="ⓒ won't goes(go)만 틀렸다.", F="ⓒ wills(will), ⓓ not are(are not)가 틀렸다.")
U(4, 55, B="ⓐ can goes(go), ⓔ can reads(read)가 틀렸다. ⓑ, ⓒ, ⓓ는 옳다.", C="ⓐ cans(can), ⓑ must to wait(must wait), ⓒ coming(come), ⓔ studies(study)가 틀렸다. ⓓ만 옳다.",
  D="ⓔ can helps(help)만 틀렸다.", E="ⓑ must is(must be)만 틀렸다.", F="ⓒ must wears(wear), ⓓ can to help(can help)가 틀렸다. ⓐ, ⓑ, ⓔ는 옳다.")
U(4, 61, C=("rarely", "‘거의 ~하지 않는다’"))
U(4, 89, C="③만 ‘(개가) 아팠을 때’라는 접속사다. 나머지는 ‘언제’를 묻는 의문사다.", E="⑤만 ‘집에 오면’이라는 접속사다. 나머지는 ‘언제’를 묻는 의문사다.")
