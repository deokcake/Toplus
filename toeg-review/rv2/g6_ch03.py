# 6급 CH3 be동사 과거 (21~30) 2차 감수
X(6, 21, r="be동사의 현재형은 am, is, are이고 과거형은 was, were다. be는 원형이다.",
  n=["am은 현재형이므로", "am·is의 과거형이므로", "are는 현재형이므로", "be는 원형이므로", "is는 현재형이므로"],
  st="① 보기를 현재형(am, is, are), 원형(be), 과거형(was, were)으로 가른다. not이 붙거나 대문자로 시작해도 같은 방법으로 본다. → ② {0} → ③ 정답은 {n}.",
  R="과거형은 was뿐이다.", B="과거형은 were뿐이다.", C="과거형이 들어 있는 것은 wasn't(was not)뿐이다.", D="과거형이 들어 있는 것은 weren't(were not)뿐이다.", E="과거형이 들어 있는 것은 was not뿐이다. do not은 be동사가 아니다.",
  F="과거형은 Were뿐이다. Do는 be동사가 아니다.")

X(6, 22, r="‘저’는 that(한 개)/those(여러 개), ‘~였다/있었다’는 was(단수)/were(복수)로 나타낸다. 소유격(my, her 등)도 우리말과 맞춘다.",
  n=["‘저’가 아니라 This이고 ‘내’가 아니라 her이므로", "단수 주어 That lady에 were를 쓸 수 없으므로", "That, was, my가 모두 우리말과 맞으므로", "‘저’가 아니라 This이고 ‘내’가 아니라 his이므로", "‘저’가 아니라 This이고 ‘내’가 아니라 your이므로"],
  st="① 우리말을 부분으로 나눈다: {0}. → ② 각 부분에 맞는 영어를 정한다: {1}. → ③ 하나라도 다른 문장을 지운다. 정답은 {n}.",
  R=("저 여자분 / 내 선생님 / 이셨다", "That lady / my teacher / was"), B=("저 소년 / 내 친구 / 였다", "That boy / my friend / was"), C=("저 책들 / 책상 위에 / 있었다", "Those books / on the desk / were"),
  D=("우리 / 어제 / 집에 있었다", "We / yesterday / were at home"), E=("나 / 어제 / 피곤했다", "I / yesterday / was tired"), F=("저 사람들 / 우리 선생님들 / 이었다", "Those people / our teachers / were"))
RV(6, 22, "E", fx=True, why="원문항 발문(‘우리말과 같은 뜻이 되도록 알맞은 문장’)으로 되돌리면 ①(I was tired.)은 ‘어제’만 빠진 옳은 문장이라 정답과 헷갈릴 수 있다. 수정 예시에서 ①을 분명히 틀린 문장(I am tired yesterday.)으로 바꿨다.")

X(6, 23, r="be동사 과거 부정: I·3인칭 단수 주어는 wasn't(was not), you·we·they·복수 주어는 weren't(were not).",
  n=["I에 was not을 바르게 썼으므로", "They에 weren't를 바르게 썼으므로", "It은 3인칭 단수라 wasn't를 써야 하므로", "The movie에 wasn't를 바르게 썼으므로", "She에 wasn't를 바르게 썼으므로"],
  st="① 문장마다 주어가 단수(I, he, she, it, 단수 명사)인지 복수(we, you, they, 복수 명사)인지 가른다. → ② 단수면 wasn't, 복수면 weren't인지 본다. → ③ {0} 정답은 {n}.",
  R="③의 It은 단수인데 weren't를 썼다.", B="④의 They는 복수인데 wasn't를 썼다.", C="④의 We는 복수인데 wasn't를 썼다.", D="③의 We는 복수인데 wasn't를 썼다.", E="②의 Jane은 단수인데 weren't를 썼다.", F="⑤의 I에는 wasn't를 쓴다.")
RV(6, 23, "B", fx=True, why="수정 예시의 ②(It wasn't heavy.)는 원문항 정답(It weren't heavy.)을 바르게 고친 문장이고, ①(We weren't at home.)은 D의 틀린 문장(We wasn't at home.)과 짝이었다. 둘 다 다른 문장으로 바꿨다.")

X(6, 24, r="be동사 과거 의문문은 Was/Were + 주어 ~?이다. I로 물으면 you로, you로 물으면 I로 답하고, be동사는 대답의 주어에 맞춘다.",
  n=["주어 I에 Was, 대답의 you에 weren't가 알맞으므로", "대답의 주어 you에는 wasn't를 쓸 수 없으므로", "주어 I에는 Were를 쓸 수 없으므로", "주어 I에 Were, you에 wasn't를 쓸 수 없으므로", "No로 답했으므로 was를 쓸 수 없으므로"],
  st="① 질문의 주어를 본다: {0}. → ② 대답의 주어와 Yes/No를 본다: {1}. → ③ 정답은 {a}.",
  R=("I → Was", "No, you → weren't"), B=("Tom and Ben(복수) → Were", "Yes, they → were"), C=("you → Were", "Yes, I → was"), D=("they → Were", "No, they → weren't"), E=("the dog(단수) → Was", "No, it → wasn't"),
  F=("she → Was", "Yes, she → was"))

X(6, 25, r="Was/Were 의문문에는 Yes, 주어 + was/were. / No, 주어 + wasn't/weren't.로 답한다. 대답의 주어는 질문의 주어를 받는 대명사다.",
  n=["the cookies는 복수라 it으로 받을 수 없으므로", "the cookies를 they로 받고 were로 답했으므로", "they에 was를 쓸 수 없으므로", "과거의 질문에 현재형 are로 답할 수 없으므로", "the cookies를 it으로 받을 수 없고 it에 were도 쓸 수 없으므로"],
  st="① 질문의 주어를 대명사로 바꾼다: {0}. → ② 질문이 과거(Was/Were)이므로 대답도 was/were로 하고, 대명사에 맞춘다: {1}. → ③ 정답은 {n}.",
  R=("the cookies → they", "they were"), B=("Tom and Ben → they", "they weren't"), C=("you → I", "I was"), D=("the soup → it", "it wasn't"), E=("the cake → it", "it was"), F=("Jane → she", "she wasn't"))

X(6, 26, r="yesterday, last ~, ~ ago가 있으면 be동사 과거형을 쓴다. I·3인칭 단수 주어는 was, you·복수 주어는 were다.",
  n=["They에는 was를 쓸 수 없으므로", "복수 주어 They에 맞는 과거형이므로", "yesterday가 있어 현재형을 쓸 수 없으므로", "yesterday가 있어 현재형을 쓸 수 없고 주어와도 맞지 않으므로", "be는 원형이라 그대로 쓸 수 없으므로"],
  st="① 때를 나타내는 말을 찾는다: {0}. 과거이므로 was나 were다. → ② 주어를 본다: {1}. → ③ 정답은 {a}.",
  R=("yesterday", "They(복수) → were"), B=("last night", "The boys(복수) → were"), C=("last year", "We → were"), D=("two days ago", "She(단수) → was"), E=("last weekend", "My grandparents(복수) → were"),
  F=("yesterday morning", "Tom(단수) → was"))

X(6, 27, r="be동사 과거 의문문과 대답: Was/Were + 주어 ~? — Yes, 주어 + was/were. / No, 주어 + wasn't/weren't.",
  n=["단수 주어 your sister에는 Were를 쓸 수 없으므로", "your sister에 Was, No 대답의 she에 wasn't가 알맞으므로", "she에는 weren't를 쓸 수 없으므로", "your sister와 she 모두 단수라 Were, weren't를 쓸 수 없으므로", "Am은 주어 I에만 쓰는 현재형이므로"],
  st="① 첫 빈칸: 질문의 주어가 {0}. → ② 둘째 빈칸: 대답이 {1}. → ③ 정답은 {a}.",
  R=("your sister(단수)이므로 Was", "No, she ~이므로 wasn't"), B=("the books(복수)이므로 Were", "No, they ~이므로 weren't"), C=("Tom(단수)이므로 Was", "Yes, he ~이므로 was"), D=("you이므로 Were", "No, I ~이므로 wasn't"),
  E=("the boys(복수)이므로 Were", "Yes, they ~이므로 were"), F=("you이므로 Were", "Yes, I ~이므로 was"))
RV(6, 27, "EF", v="수정(내용)", why="정답 유일 확인. 다만 정답 조합(Were - weren't)이 B와 같고, E는 대화의 짜임(the boys ~ yesterday? — No, they ~. They were ~.)도 B와 같다(유형 간 중복). 발문에도 ‘과거형 be동사를 사용하여’가 붙었다.", fix="대화를 바꿔 정답 조합을 다르게, 발문을 원문항대로")

X(6, 28, r="be동사 과거 의문문의 어순은 Was/Were + 주어 + 나머지 ~?이다.",
  n=["Were + 주어 you + busy + this morning의 순서이므로", "평서문 어순에 물음표만 붙였으므로", "형용사 Busy가 맨 앞에 왔으므로", "주어 you가 Were 바로 뒤에 오지 않았으므로", "평서문 어순에 물음표만 붙였으므로"],
  st="① 의문문이므로 be동사({0})를 맨 앞에 둔다. → ② 바로 뒤에 주어({1}), 그 뒤에 나머지({2})를 둔다. → ③ 이 순서인 것은 {n}.",
  R=("Were", "you", "busy / this morning"), B=("Was", "Tom", "at school"), C=("Was", "Jane", "at the museum / yesterday"), D=("Were", "the boys", "tired"), E=("Was", "she", "at home / yesterday"),
  F=("Were", "the students", "in the library / yesterday"))

X(6, 29, r="be동사 과거형은 주어가 단수면 was, 복수(A and B 포함)면 were다.",
  n=["The sky는 단수라 was가 맞으므로", "My parents는 복수라 were가 맞으므로", "My little brother and I는 두 사람이라 were를 써야 하므로", "We에 were가 맞으므로", "It에 was가 맞으므로"],
  st="① 밑줄마다 바로 앞의 주어를 찾는다. → ② 주어가 한 사람·한 개면 was, 둘 이상이면 were인지 본다. → ③ {0} 정답은 {n}.",
  R="③의 주어 My little brother and I는 두 사람이라 were다.", B="①의 주어 My friends는 복수라 were다.", C="②의 주어 The old camera는 단수라 was다.", D="③의 주어 My cousins는 복수라 were다.",
  E="④의 주어 The cake는 단수라 was다.", F="⑤의 주어 The weather는 단수라 was다.")
RV(6, 29, "D", fx=True, why="틀린 문장의 주어(My brother and I)와 위치(③)가 원문항의 틀린 문장(My little brother and I ③was)과 같다. 수정 예시에서 주어를 My cousins로 바꿨다.")

X(6, 30, r="be동사 과거형: 주어가 단수(한 개)면 was, 복수(여러 개)면 were.",
  pre=["<보기> 판정: (가) O. 단수 The box + was. (나) O. 복수 The boxes + were. (다) X. 복수 The boxes에는 were를 써야 한다."],
  k="옳은 문장은 (가), (나) 2개이고, 이유는 단수 주어에 was, 복수 주어에 were를 쓰기 때문이다.",
  n=["(나)도 옳고 were도 쓰이므로 이유가 틀려", "(가)도 옳고 단수 주어에는 was를 쓰므로 이유가 틀려", "개수, 문장, 이유가 모두 맞아", "(다)는 틀린 문장이고 복수 주어에 was를 쓸 수 없어", "(다)는 틀린 문장이라"],
  st="① <보기>의 문장마다 주어의 수와 was/were가 맞는지 판정한다: {0} → ② 옳은 문장의 개수와 기호가 맞는 보기를 고른다. → ③ 그 보기의 이유까지 맞는지 확인한다. 정답은 {n}.",
  R="(가) O, (나) O, (다) X.", B="(가) O, (나) X(My brothers was), (다) O.", C="(가) O, (나) X(The dog were), (다) X(They was).", D="(가) X(You was), (나) O, (다) O.", E="(가) O, (나) O, (다) O.",
  F="(가) O, (나) X(The children was), (다) O.")
