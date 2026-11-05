# 3급 CH1 be동사 (1~10) 2차 감수
X(3, 1, r="be동사는 주어에 따라 달라진다. 현재형: I - am, you·복수 - are, 3인칭 단수 - is. 과거형: I·3인칭 단수 - was, you·복수 - were.",
  n=["I에는 am, 복수 주어 My friends에는 are를 쓰므로", "I에 is를 쓸 수 없으므로", "My friends에 is를 쓸 수 없으므로", "두 빈칸 모두 주어와 맞지 않으므로", "두 빈칸 모두 주어와 맞지 않으므로"],
  st="① 빈칸 앞의 주어를 확인한다. 첫째는 {0}, 둘째는 {1}이다. → ② {2} → ③ 정답은 {a}.",
  R=("I", "My friends(복수)", "I에는 am, 복수 주어에는 are를 쓴다."), B=("You", "Mina(3인칭 단수)", "You에는 are, 3인칭 단수에는 is를 쓴다."), C=("She(3인칭 단수)", "The boys(복수)", "3인칭 단수에는 is, 복수에는 are를 쓴다."),
  D=("We(복수)", "Tom(3인칭 단수)", "복수에는 are, 3인칭 단수에는 is를 쓴다."), E=("I", "They(복수)", "yesterday가 있으므로 과거형이다. I에는 was, 복수에는 were를 쓴다."),
  F=("Jane(3인칭 단수)", "We(복수)", "last night, yesterday가 있으므로 과거형이다. 3인칭 단수에는 was, 복수에는 were를 쓴다."))
RV(3, 1, "BCD", v="수정(표기)", why="정답 확인. 다만 발문이 ‘현재형 be동사’로 원문항(‘알맞은 be동사’)과 다르다(3-2 E는 같은 까닭으로 ‘수정(표기)’였다). 보기에 과거형이 섞인 조합(were - is, was - are)이 있어 조건을 덧붙인 것인데, 조건이 없으면 B의 ⑤, C의 ②도 문법상 가능하다.", fix="발문을 원문항과 같게, 과거형이 섞인 보기는 현재형 조합으로")

X(3, 2, r="There is/are, There was/were의 be동사는 시제와 뒤에 오는 명사의 수에 맞춘다. 셀 수 없는 명사는 단수로 취급한다.",
  n=["과거의 일이고 뒤의 명사도 복수라 is를 쓸 수 없으므로", "Last year가 있어 현재형 are를 쓸 수 없으므로", "There am이라는 표현은 없으므로", "뒤의 명사 many students가 복수라 was를 쓸 수 없으므로", "과거이고 뒤의 명사가 복수이므로 There were가 알맞으므로"],
  st="① 문장 앞의 시간 표현으로 시제를 정한다({0}). → ② There 뒤 be동사는 뒤에 오는 명사에 수를 맞춘다({1}). → ③ 정답은 {a}.",
  R=("Last year → 과거", "many students, 복수"), B=("Right now → 현재", "a new message, 단수"), C=("Yesterday → 과거", "a cat, 단수"), D=("Now → 현재", "two books, 복수"), E=("Right now → 현재", "a lot of water, 셀 수 없는 명사라 단수"),
  F=("Last night → 과거", "many cars, 복수"))

X(3, 3, r="be동사 의문문은 ‘be동사 + 주어 ~?’이고, 대답은 ‘Yes, 주어 + be동사.’ / ‘No, 주어 + be동사 + not.’이다. 질문의 you는 I로, I는 you로 받는다.",
  n=["주어 you에는 Are, 대답은 I'm not이므로", "주어 you에 Is를 쓸 수 없으므로", "No, I not에는 be동사가 없으므로", "두 빈칸 모두 맞지 않으므로", "주어 you에 Am을 쓸 수 없으므로"],
  st="① (A)는 의문문 맨 앞의 be동사다. 주어에 맞춘다({0}). → ② (B)는 No 뒤의 짧은 대답이다. 질문의 주어를 대명사로 받아 ‘주어 + be동사’를 쓴다({1}). 뒤에 not이 있으므로 be동사가 꼭 들어가야 한다. → ③ 정답은 {n}.",
  R=("you → Are", "you로 물었으므로 I'm"), B=("Tom and Ben → Are", "they're"), C=("she → Is", "she's"), D=("they → Are", "they're"), E=("I → Am", "I로 물었으므로 you're"), F=("Tom → Is", "he's"))

X(3, 4, r="명사 앞에는 소유격(your)을 쓰고, ‘~의 것’은 소유대명사(yours)나 ‘이름 + 's’로 나타낸다.",
  n=["뒤의 Gary는 ‘Gary의 것’이 되지 못하므로", "yours 뒤에는 명사 book이 올 수 없으므로", "명사 book 앞에는 your, ‘Gary의 것’은 Gary's이므로", "yours 뒤에는 명사 book이 올 수 없으므로", "you는 명사를 꾸밀 수 없으므로"],
  st="① 첫째 빈칸 뒤에 명사({0})가 있다. 명사 앞에는 소유격 your를 쓴다. yours(너의 것)는 뒤에 명사가 올 수 없다. → ② 둘째 빈칸은 ‘~의 것’이라는 뜻이다. 사람 이름에 's를 붙인다({1}). → ③ 정답은 {n}.",
  R=("book", "Gary's"), B=("umbrella", "Amy's"), C=("bag", "Mina's"), D=("shoes", "Leo's"), E=("bike", "Tom's"), F=("pencils", "Jane's"))

X(3, 5, r="be동사는 주어의 인칭·수와 시제에 맞춘다. There is/are, was/were는 뒤의 명사에 맞춘다.",
  pre=["문장별 판정: ⓐ O. 복수 주어에 were. ⓑ X. She에는 isn't를 쓴다. ⓒ O. you에 Were. ⓓ X. many people이 복수이므로 There were. ⓔ O. I에 am."],
  k="밑줄 친 부분이 옳은 문장은 ⓐ, ⓒ, ⓔ 세 개다.", n=["밑줄 친 부분이 옳은 문장은 ⓐ, ⓒ, ⓔ 세 개이므로"] * 5,
  st="① 밑줄 친 be동사마다 주어를 찾는다. There로 시작하면 뒤의 명사가 주어다. → ② 주어의 수(단수·복수)와 인칭에 be동사가 맞는지 본다. → ③ {0} 옳은 문장은 {a}이다.",
  R="ⓑ는 She에 aren't를 썼고(isn't), ⓓ는 many people에 was를 썼다(were). 나머지 셋이 옳다.", B="ⓑ는 We에 was(were), ⓓ는 two apples에 is(are), ⓔ는 The movies에 wasn't(weren't)를 썼다. ⓐ, ⓒ만 옳다.",
  C="ⓑ는 They에 isn't(aren't), ⓓ는 two books에 is(are), ⓔ는 Jane에 were(was)를 썼다. ⓐ, ⓒ만 옳다.", D="ⓔ만 틀렸다. they에는 Was가 아니라 Were를 쓴다.", E="ⓓ만 틀렸다. news는 단수 취급하므로 is를 쓴다.",
  F="ⓑ는 They에 wasn't(weren't), ⓒ는 two cats에 was(were), ⓓ는 We에 isn't(aren't), ⓔ는 you에 Is(Are)를 썼다. ⓐ만 옳다.")
RV(3, 5, "CDF", fx=True, why="수정 예시의 정답(3개, ③)이 원문항의 정답 개수·위치와 같아, 문장을 바꿔 C는 2개, D는 4개, F는 1개로 했다.")

X(3, 6, r="There + be동사는 시제와 뒤에 오는 명사의 수에 맞춘다(단수 is/was, 복수 are/were).",
  n=["last year가 있어 현재형 is를 쓸 수 없으므로", "과거의 일이고 뒤의 명사도 단수라 are를 쓸 수 없으므로", "과거이고 뒤의 명사 a beautiful garden이 단수이므로", "뒤의 명사가 단수라 were를 쓸 수 없으므로", "원형 be는 문장의 동사로 쓸 수 없으므로"],
  st="① 문장 끝의 시간 표현으로 시제를 정한다({0}). → ② There 뒤 be동사는 뒤의 명사에 수를 맞춘다({1}). → ③ 정답은 {a}.",
  R=("last year → 과거", "a beautiful garden, 단수"), B=("last night → 과거", "two umbrellas, 복수"), C=("yesterday → 과거", "many students, 복수"), D=("now → 현재", "a new store, 단수"), E=("now → 현재", "two dogs, 복수"),
  F=("last winter → 과거", "a lot of snow, 셀 수 없는 명사라 단수"))

X(3, 7, r="be동사가 있는 문장의 의문문은 do/does/did 없이 be동사를 주어 앞으로 옮겨 만든다.",
  n=["yesterday가 있어 현재형 Are를 쓸 수 없으므로", "be동사 were를 주어 앞으로 옮겼으므로", "be동사 의문문에는 Do를 쓰지 않으므로", "Did를 쓰면 문장에 동사가 없어지므로", "주어 they에 Was를 쓸 수 없으므로"],
  st="① 문장의 동사가 be동사({0})다. be동사 의문문은 do/does/did 없이 be동사를 주어 앞으로 옮긴다. → ② 시제와 주어({1})에 맞는 형태는 그대로 둔다. → ③ ‘{2}’로 시작하고 be동사가 한 번만 나오는 {n}을 고른다.",
  R=("were", "They", "Were they"), B=("were", "The kids", "Were the kids"), C=("was", "Jane", "Was Jane"), D=("are", "We", "Are we"), E=("is", "Tom", "Is Tom"), F=("was", "I", "Was I"))

X(3, 8, r="be동사의 과거형은 단수 주어(I 포함)에 was, 복수 주어에 were를 쓴다.",
  n=["복수 The children에 was를 쓸 수 없으므로", "두 빈칸 모두 수가 맞지 않으므로", "단수 their mother에 were를 쓸 수 없으므로", "복수 The children에는 were, 단수 their mother에는 was를 쓰므로", "단수 their mother에 were를 쓸 수 없으므로"],
  st="① 두 빈칸 앞의 주어를 본다. (A)는 {0}, (B)는 {1}이다. → ② {2} 단수에는 was, 복수에는 were를 쓴다. → ③ 정답은 {n}.",
  R=("The children(복수)", "their mother(단수)", "보기에서 두 빈칸의 시제가 같은 것을 찾는다."), B=("My sister(단수)", "my parents(복수)", "yesterday가 있으므로 과거형이다."), C=("Tom(단수)", "his friends(복수)", "두 빈칸의 시제가 같아야 한다."),
  D=("I", "we(복수)", "두 빈칸의 시제가 같아야 한다."), E=("The dog(단수)", "the cats(복수)", "두 빈칸의 시제가 같아야 한다."), F=("Jane and Amy(복수)", "Tom(단수)", "두 빈칸의 시제가 같아야 한다."))

X(3, 9, r="There is/are 문장의 실제 주어는 be동사 뒤의 명사다. be동사는 그 명사에 수를 맞추고, 의문문은 be동사를 there 앞으로 옮긴다.",
  pre=["설명별 판정: 가 X. 실제 주어는 There가 아니라 a cat이다. 나 O. a cat이 단수라 Is를 쓴다. 다 O. is를 there 앞으로 옮긴 의문문이다. 라 X. 장소 부사구는 주어가 될 수 없다."],
  n=["가가 틀렸으므로", "나와 다가 옳은 설명이므로", "라가 틀렸으므로", "가가 틀렸으므로", "라가 틀렸으므로"],
  st="① There is/are 문장에서 실제 주어는 be동사 뒤의 명사({0})다. there는 주어가 아니다. → ② be동사는 그 명사의 수와 시제에 맞추고, 의문문은 be동사를 there 앞으로 옮긴다. 대답은 Yes, there is(are). / No, there isn't(aren't).다. → ③ 틀린 설명을 지운다: {1}. 남은 것을 묶은 {a}가 정답이다.",
  R=("a cat", "가(There를 주어로 봄), 라(부사구를 주어로 봄)"), B=("a bank", "나(there를 주어로 봄), 라(near here를 주어로 봄)"), C=("two books", "나(there에 수를 맞춘다고 함), 다(Yes, it is.로 답한다고 함)"),
  D=("a meeting", "가(there를 주어로 봄), 나(과거인데 Is를 쓴다고 함)"), E=("many people", "다(people을 단수로 봄)"), F=("any water", "다(there를 주어로 봄), 라(Yes, it is.로 답한다고 함)"))

X(3, 10, r="be동사의 과거형은 단수 주어(셀 수 없는 명사 포함)에 was, 복수 주어에 were를 쓴다. there was/were는 뒤의 명사에 맞춘다.",
  pre=["문장별 판정: 첫째 X. a heavy rain이 단수이므로 there was. 둘째 X. The streets가 복수이므로 were. 셋째 O. 넷째 X. My parents가 복수이므로 were."],
  k="틀린 문장은 첫째, 둘째, 넷째 세 개다.", n=["틀린 문장은 첫째, 둘째, 넷째 세 개이므로"] * 5,
  st="① 문장마다 주어를 찾는다. there was/were는 뒤의 명사가 주어다. → ② 단수 주어(셀 수 없는 명사 포함)에는 was, 복수 주어에는 were인지 확인한다. → ③ {0} 틀린 문장은 {a}이다.",
  R="첫째는 a heavy rain이 단수라 was, 둘째는 The streets가 복수라 were, 넷째는 My parents가 복수라 were여야 한다. 셋째만 옳다.", B="첫째는 a lot of people이 복수라 were, 둘째는 The bus가 단수라 was여야 한다.",
  C="첫째만 틀렸다. two accidents가 복수라 there were여야 한다.", D="둘째는 The museum이 단수라 was, 셋째는 two guides가 복수라 were여야 한다.",
  E="첫째는 snow가 셀 수 없는 명사라 was, 둘째는 The roads가 복수라 were, 셋째는 My brother가 단수라 was, 넷째는 I라서 was여야 한다. 네 문장 모두 틀렸다.",
  F="① 문장마다 주어를 찾는다. there was/were는 뒤의 명사가 주어다. → ② 단수 주어에는 was, 복수 주어에는 were인지 확인한다. → ③ 네 문장 모두 수가 맞는다(many clouds - were, The sky - was, a strong wind - was, The children - were). 틀린 문장이 없으므로 정답은 {n}이다.")
RV(3, 10, "D", fx=True, why="수정 예시의 정답(3개, ③)이 원문항의 정답 개수·위치와 같아, 넷째를 옳은 문장(We were tired.)으로 되돌려 2개(②)로 했다.")
