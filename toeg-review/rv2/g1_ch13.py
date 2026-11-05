# 1급 CH13 특수구문 (121~130) 2차 감수
X(1, 121, r="the fact, the news, the idea, the possibility 같은 명사 뒤에서 그 내용을 풀어 주는 절은 접속사 that으로 이끈다(동격의 that). that 뒤에는 빠진 성분이 없는 완전한 절이 온다.",
  n=["which 뒤에는 주어나 목적어가 빠진 절이 와야 하므로", "what은 선행사 뒤에 쓸 수 없으므로", "The fact의 내용을 풀어 주는 완전한 절(he resigned)을 동격의 that이 이끄므로", "of 뒤에는 절이 올 수 없으므로", "when은 때를 나타내는 선행사 뒤에 쓰므로"],
  st="① 빈칸 앞의 명사({0})와 뒤의 절({1})의 관계를 본다. 뒤의 절이 그 명사의 내용을 풀어 준다(‘~라는 {2}’). → ② 뒤의 절에 빠진 성분이 없으므로 관계대명사(which, what)가 아니라 접속사 자리다. → ③ 명사의 내용을 풀어 주는 동격절은 that이 이끈다. 정답은 {n}.",
  R=("The fact", "he resigned", "사실"), B=("The possibility", "we will succeed", "가능성"), C=("The fact", "she kept her promise", "사실"), D=("The news", "he rejected the offer", "소식"),
  E=("The idea", "Tom would move", "생각"), F=("The fact", "the plan failed", "사실"))

X(1, 122, r="not all·not every는 ‘모두 ~한 것은 아니다’라는 부분부정이고, none·no는 ‘아무도(하나도) ~ 않다’라는 전체부정이다.",
  n=["None of ~는 ‘아무도 참석하지 않았다’는 전체부정이므로", "No teacher는 ‘어떤 교사도 참석하지 않았다’는 전체부정이므로", "Not all로 ‘모두 참석한 것은 아니다’라는 부분부정을 바르게 나타냈으므로", "부정어가 없어 ‘모두 참석했다’는 뜻이므로",
     "일반동사를 not만으로 부정할 수 없는 틀린 형태이므로"],
  st="① 우리말 ‘모든 ~이 …한 것은 아니다’는 일부만 그렇다는 부분부정이다. → ② 부분부정은 Not all(every) ~로 나타낸다. None·No는 전체부정, 부정어가 없으면 전체 긍정이다. → ③ 형태가 틀린 보기({0})도 지운다. 정답은 {n}.",
  R="The teachers all not attended", B="No all ~, all not passed", C="Not every books are, No every book", D="all not work, No all ~", E="Not every problems are, No every problem", F="all not agreed, No all ~")

X(1, 123, r="등위접속사·상관접속사로 이어지는 말은 같은 형태로 병렬한다. both A and B는 복수 취급하고, either A or B, neither A nor B는 B에 동사의 수를 맞춘다.",
  n=["Both A and B에서 to read와 writing의 형태가 달라 병렬이 깨졌으므로", "neither A nor B는 B(the child)에 수를 맞춰 was가 알맞으므로", "Not only가 문장 앞에 오면 도치해야 하고 works와 performs도 병렬되지 않았으므로", "flew와 병렬되도록 sang으로 써야 하므로",
     "either A or B는 B(my brother)에 수를 맞춰 has를 써야 하므로"],
  st="① 문장마다 접속사(and, or, not only ~ but also 등)로 이어진 두 말의 형태가 같은지 본다. → ② 상관접속사가 주어이면 동사의 수도 확인한다. both는 복수, either·neither·not only는 B에 맞춘다. → ③ {n}만 옳다: {0}.",
  R="neither A nor B의 B(the child)에 맞춰 was를 썼다", B="neither A nor B의 B(the teacher)에 맞춰 was를 썼다", C="either A or B의 B(the teacher)에 맞춰 has를 썼다", D="not only A but also B의 B(their mother)에 맞춰 enjoys를 썼다",
  E="came, took, went 세 동사가 같은 과거형으로 병렬되었다", F="not only math but also science로 명사끼리 병렬되었다")
RV(1, 123, "B", v="수정(내용)", why="정답 ⑤ 확인. 원문항은 병렬 구조 오류(Both to read and writing 등)와 수 일치를 함께 묻는데 변형은 다섯 문장이 모두 수 일치뿐이라 평가 요소가 줄었고(B1 부분), Neither … nor 문장이 틀린 형태(①)와 옳은 형태(⑤)로 함께 나온다(C4).", fix="원문항처럼 병렬 구조 오류 문장을 넣기")

X(1, 124, r="never, hardly, seldom, not only 같은 부정어가 문장 맨 앞에 오면 ‘부정어 + 조동사 + 주어’로 도치한다. Neither + 조동사 + 주어, Here + 동사 + 주어도 도치 구문이다.",
  n=["부정어 never가 문장 가운데 있어 도치하지 않는다. 올바르므로", "Neither + have + I로 바르게 도치했으므로", "Here + comes + 주어로 바르게 도치했으므로", "not only가 앞에 와서 is it으로 바르게 도치했으므로",
     "부정어 hardly가 앞에 왔으므로 hardly can I believe로 도치해야 하므로"],
  st="① 밑줄마다 문장(절)의 맨 앞에 부정어나 Neither·Here·So가 있는지 본다. → ② 있으면 그 뒤가 ‘(조)동사 + 주어’ 순서인지 확인한다. → ③ {n}은 부정어({0}) 뒤가 ‘주어 + 동사’ 순서 그대로다. 바른 어순은 {1}.",
  R=("hardly", "hardly can I believe"), B=("Seldom", "Seldom do I go"), C=("Hardly", "Hardly can I hear"), D=("Seldom", "Seldom have I felt"), E=("Never", "Never will I eat"), F=("Rarely", "Rarely have I waited"))
RV(1, 124, "F", fx=True, why="수정 예시의 틀린 표현 ④ ‘Hardly I can believe this’가 원문항의 틀린 표현(hardly I can believe my eyes)과 거의 같아 ‘Rarely I have waited this long’으로 바꿨다.")

X(1, 125, r="A as well as B는 A에, either A or B는 B에 동사의 수를 맞춘다. none of + 셀 수 없는 명사는 단수 동사를 쓰고, please 뒤의 명령문은 동사원형으로 쓴다. It was ~ who …는 강조구문이다.",
  pre=["문장별 판정: A) X. A as well as B는 A(His colleagues)에 맞춰 are를 쓴다. B) O. either A or B는 B(your partner)에 맞춰 is. C) O. Not every(부분부정). D) X. information은 셀 수 없는 명사라 was를 쓴다. E) O. It was ~ who 강조구문. F) X. please 뒤에는 동사원형 contact를 쓴다."],
  k="틀린 문장은 A), D), F) 세 개다.",
  n=["틀린 문장은 A), D), F) 세 개이므로"] * 5,
  st="① 문장마다 주어의 중심이 되는 말을 정한다. A as well as B는 A, either·neither·not only는 B, both는 복수다. → ② 동사의 수와 견준다. {0} → ③ 틀린 문장을 세면 {a}이다.",
  R="A)는 His colleagues에 맞춰 are여야 하고, D)는 셀 수 없는 information이라 was여야 하며, F)는 명령문이라 contact여야 한다.",
  B="C)는 the coach에 맞춰 was여야 하고, D)는 his friends에 맞춰 know여야 한다. 나머지 넷은 옳다.",
  C="B)는 his parents에 맞춰 are, D)는 both ~ and라 like, F)는 셀 수 없는 money라 was여야 한다. 나머지 셋은 옳다.",
  D="C)만 틀렸다. my cousins에 맞춰 live여야 한다. 나머지 다섯은 옳다.",
  E="A)는 The manager에 맞춰 is여야 하고, C)는 my brother에 맞춰 likes여야 한다. 나머지 넷은 옳다.",
  F="B)는 her parents에 맞춰 are, C)는 the players에 맞춰 have, D)는 the dog에 맞춰 was, F)는 every one이라 is여야 한다. A)와 E)만 옳다.")
RV(1, 125, "BCDEF", fx=True, why="사용자 검토 의견(B: 상관접속사의 수 일치라는 취지에서 벗어남)에 따라, 병렬·비교 문장이 섞여 있던 수정 예시를 여섯 문장 모두 주어·동사 수 일치를 묻는 문장으로 다시 썼다. C~F도 같은 문제라 함께 고쳤다.")

X(1, 126, r="동사를 강조할 때는 ‘do/does/did + 동사원형’을 쓴다. 인칭·시제는 do가 나타내고 뒤의 동사는 반드시 원형이다.",
  n=["주어 I에는 do가 맞지만 뒤에 원형 play를 써야 하므로", "does 뒤에는 원형 know를 써야 하므로", "did 뒤에는 원형 go를 써야 하므로", "did + 동사원형 enjoy로 과거의 동작을 바르게 강조했으므로", "does 뒤에는 원형 like를 써야 하므로"],
  st="① 문장마다 강조의 do/does/did 바로 뒤 동사가 원형인지 본다. -s가 붙었거나 과거형이면 틀린 것이다. → ② do/does/did가 주어와 시제에 맞는지도 확인한다. → ③ {n}만 옳다: {0}.",
  R="did + enjoy", B="did + submit", C="does + look", D="did + win", E="do + look", F="do + need")

X(1, 127, r="It is/was ~ that 강조구문에서 강조하는 말이 사람이면 who(m), 사물이면 which, 장소이면 where, 때이면 when을 that 대신 쓸 수 있다. 형용사는 이 구문으로 강조하지 않으며 how도 쓰지 않는다.",
  n=["강조하는 말 Jane이 사람이라 who를 쓸 수 있으므로", "강조하는 말 the book이 사물이라 which를 쓸 수 있으므로", "강조하는 말 in Seoul이 장소라 where를 쓸 수 있으므로", "강조하는 말 at 10 o'clock이 때라 when을 쓸 수 있으므로",
     "형용사 very happy는 강조구문으로 강조할 수 없고 how도 that 대신 쓸 수 없으므로"],
  st="① It was와 밑줄 사이에 놓인 강조하는 말이 사람·사물·장소·때 가운데 무엇인지 가른다. → ② 사람 - who(m), 사물 - which, 장소 - where, 때 - when이 맞는 짝이다. → ③ {n}은 짝이 맞지 않는다: {0}.",
  R="형용사 very happy는 강조할 수 없고 how도 쓸 수 없다", B="because of the rain(이유) 뒤에 who를 썼다", C="at the station(장소) 뒤에 who를 썼다", D="Tom(사람) 뒤에 when을 썼다", E="in the morning(때) 뒤에 who를 썼다", F="Leo(사람) 뒤에 where를 썼다")

X(1, 128, r="장소의 부사구가 문장 앞에 오면 ‘부사구 + 동사 + 주어’로 도치하고, 동사는 뒤에 오는 주어에 수를 맞춘다. There is/are도 뒤의 주어에 수를 맞추며, a number of + 복수명사는 복수 취급한다.",
  n=["a number of students는 복수라 둘째 빈칸에 is를 쓸 수 없으므로", "a small, peaceful village는 단수라 첫째 빈칸에 are를 쓸 수 없으므로", "뒤의 주어 a small, peaceful village는 단수라 is, a number of students는 복수라 are가 알맞으므로",
     "두 빈칸의 수가 서로 바뀌었으므로", "둘째 빈칸에 is를 쓸 수 없고 첫째 빈칸의 시제도 어울리지 않으므로"],
  st="① 두 문장 모두 주어가 동사 뒤에 있다. 빈칸 뒤에서 진짜 주어를 찾는다. → ② 첫째 문장의 주어({0})와 둘째 문장의 주어({1})의 수를 가른다. → ③ 순서대로 맞춘 {a}를 고른다.",
  R=("a small, peaceful village - 단수", "a number of students - 복수"), B=("two sleeping cats - 복수", "a notebook - 단수"), C=("several small farms - 복수", "a large tree - 단수"), D=("an old castle - 단수", "many tourists - 복수"),
  E=("a small cafe - 단수", "several cars - 복수"), F=("three delivery trucks - 복수", "a narrow alley - 단수"))
RV(1, 128, "E", v="수정(표기)", why="정답 ③ 확인. 두 문장을 ‘/’로 이어 써서 원문항(두 줄)과 표기가 다르고, 오답 ⑤ ‘is - ares’는 영어에 없는 형태다. B·C·D·F에서 같은 이유로 ‘수정(표기)’였던 것과 맞췄다.", fix="두 줄로 나누고 ⑤를 실제 형태로")

X(1, 129, r="and로 나열되는 동사들은 같은 형태로 병렬하고(should eat, exercise, and get), not only A but also B의 A와 B도 같은 형태(to부정사 - to부정사)로 맞춘다.",
  n=["should 뒤의 eat, get과 나란히 exercise, 진주어 자리의 to eat과 to avoid가 병렬되므로", "should 뒤에는 exercising을 쓸 수 없으므로", "It is important 뒤 진주어 자리에 동사원형 eat, avoid를 쓸 수 없으므로", "to eat과 avoiding의 형태가 달라 병렬이 깨지므로",
     "should 뒤에 to exercise를 쓸 수 없고 eating과 to avoid도 형태가 다르므로"],
  st="① (A)는 앞뒤의 동사({0})와 and로 나열되어 있으므로 같은 형태인 동사원형이다. → ② (B)와 (C)는 not only ~ but also로 이어지므로 형태가 같아야 한다. 앞의 It is ~ 뒤에서 진주어 노릇을 하므로 둘 다 to부정사다. → ③ 정답은 {a}.",
  R="eat, get", B="pack, keep", C="cook, compare", D="read, review", E="set, take", F="avoid, follow")

X(1, 130, r="등위접속사(and, but, or), 상관접속사, 비교 구문(than, as ~ as)으로 이어지는 두 요소는 문법적으로 대등한 형태여야 한다. A as well as B가 주어이면 동사는 A에 수를 맞춘다.",
  n=["병렬구조는 단어뿐 아니라 구와 구, 절과 절 사이에도 성립하므로", "A as well as B에서 동사는 B가 아니라 A에 수를 맞추므로", "등위접속사뿐 아니라 비교 구문에서도 두 요소가 대등해야 한다고 바르게 설명했으므로", "not A but B에서도 A와 B는 같은 형태여야 하므로",
     "병렬구조를 지키지 않으면 어법상 틀린 문장이 되므로"],
  st="① 보기마다 병렬구조의 범위, 수 일치, 형태에 대해 무엇을 말하는지 간추린다. → ② 병렬은 단어·구·절 모두에 적용되고, 접속사와 비교 구문으로 이어진 요소는 같은 형태여야 하며, 어기면 어법 오류라는 기준에 견준다. → ③ {0} 정답은 {n}.",
  R="①은 범위를 좁혔고, ②는 수 일치를 거꾸로 말했으며, ④·⑤는 형태가 달라도 된다고 했다.",
  B="①은 범위를 좁혔고, ②는 형태가 달라도 된다고 했으며, ③은 수 일치를 거꾸로 말했고, ⑤는 어겨도 오류가 아니라고 했다.",
  C="②는 형태가 달라도 된다고 했고, ③은 수 일치를 거꾸로 말했으며, ④는 범위를 and로 좁혔고, ⑤는 마지막 요소의 형태를 바꿔도 된다고 했다.",
  D="①·②는 형태가 달라도 된다고 했고, ④는 neither ~ nor를 병렬에서 뺐으며, ⑤는 길이를 기준으로 삼았다.",
  E="①은 비교 구문을 병렬에서 뺐고, ②·④는 없는 규칙을 말했으며, ③은 동명사와 to부정사를 섞어도 된다고 했다.",
  F="①은 범위를 좁혔고, ②·⑤는 없는 규칙을 말했으며, ④는 어겨도 오류가 아니라고 했다.")
