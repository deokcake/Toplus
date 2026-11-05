# 6급 CH10 과거진행형 (91~100) 2차 감수
X(6, 91, r="-ing형 만들기: 대부분 그대로 -ing, -e로 끝나면 e를 빼고, 단모음 + 단자음이면 자음을 겹쳐 쓴다(cut → cutting, win → winning). -ie는 y로 바꾼다.",
  n=["그대로 -ing를 붙인 옳은 형태이므로", "그대로 -ing를 붙인 옳은 형태이므로", "단모음 + 단자음이라 n을 겹쳐 쓴 옳은 형태이므로", "단모음 + 단자음이라 t를 겹쳐 cutting으로 써야 하므로", "그대로 -ing를 붙인 옳은 형태이므로"],
  st="① 동사의 끝을 본다: -e, -ie, 단모음 + 단자음 가운데 어느 것인지 가른다. → ② 규칙대로 되었는지 본다. {0} → ③ 정답은 {a}.",
  R="cut은 단모음 + 단자음이라 cutting이다.", B="drive는 -e로 끝나므로 driving이다.", C="swim은 단모음 + 단자음이라 swimming이다.", D="die는 -ie로 끝나므로 dying이다.", E="stop은 단모음 + 단자음이라 stopping이다.",
  F="come은 -e로 끝나므로 coming이다.")

X(6, 92, r="‘~하고 있었다’는 과거진행형 was/were + 동사원형-ing로 쓴다. 단수 주어에는 was를 쓴다.",
  n=["현재형이라 ‘짖고 있었다’가 아니므로", "현재진행형이라 ‘짖고 있다’이므로", "단수 주어 The dog에 was + barking을 바르게 썼으므로", "단수 주어에 were를 쓸 수 없으므로", "주어 The dog에 am을 쓸 수 없으므로"],
  st="① 우리말 ‘{0}’ → 과거에 진행 중이던 일이므로 was/were + -ing다. → ② 주어({1})는 단수이므로 was다. → ③ 현재형·현재진행형·단순 과거와 were를 쓴 문장을 지운다. 정답은 {n}.",
  R=("짖고 있었다", "The dog"), B=("자고 있었다", "The cat"), C=("쫓고 있었다", "The puppy"), D=("먹고 있었다", "The rabbit"), E=("날고 있었다", "The bird"), F=("달리고 있었다", "The horse"))

X(6, 93, r="과거진행형 부정문은 was/were + not + -ing, 의문문은 Was/Were + 주어 + -ing ~?이다. be동사는 주어에 맞춘다.",
  n=["Was she 뒤에는 play가 아니라 -ing형을 써야 하므로", "주어 I에 were를 쓸 수 없고 뒤에도 -ing형이 와야 하므로", "주어 I에는 weren't가 아니라 wasn't를 써야 하므로", "I에 wasn't, Was she 뒤에 playing이 알맞으므로", "being sleeping이라고 쓰지 않고 Was she 뒤에 played도 쓸 수 없으므로"],
  st="① 첫 문장: 빈칸 뒤에 -ing형이 있으므로 be동사 과거형(+ not)이 들어간다. 주어가 {0}. → ② 둘째 문장: Was/Were + 주어 뒤이므로 -ing형 {1}. → ③ 정답은 {a}.",
  R=("I이므로 wasn't", "playing"), B=("They이므로 weren't", "writing"), C=("Tom이므로 was not", "reading"), D=("We이므로 were not", "playing"), E=("Jane이므로 was not", "cooking"), F=("We이므로 were not", "studying"))
RV(6, 93, "F", fx=True, why="정답 위치가 원문항·B·D와 모두 ④였다. 수정 예시에서 F의 보기 순서를 바꿨다(②).")

X(6, 94, r="과거진행형은 was/were + -ing다. 의문문은 Was/Were + 주어 ~?이고, be동사는 각 문장의 주어에 맞춘다.",
  n=["둘째 문장의 주어 My brother는 단수라 was를 써야 하므로", "you에 Were, My brother에 was having이 알맞으므로", "주어 you에 Was를 쓸 수 없으므로", "you에 Was를 쓸 수 없고 둘째 문장도 과거가 아니므로", "둘째 문장의 My brother에 are를 쓸 수 없으므로"],
  st="① 첫 문장의 주어: {0}. → ② 둘째 문장의 주어: {1}. → ③ 정답은 {a}.",
  R=("you → Were", "My brother(단수) → was having"), B=("Mina(단수) → Was", "Her friends(복수) → were studying"), C=("the dog(단수) → Was", "The children(복수) → were waiting"), D=("Tom(단수) → Was", "Jane(단수) → was writing"),
  E=("the children(복수) → Were", "Their parents(복수) → were cooking"), F=("she(단수) → Was", "Her brother(단수) → was playing"))
RV(6, 94, "E", fx=True, why="정답 조합(Were - was cooking)이 원문항 정답(Were - was having)과 같은 짜임이었다. 수정 예시에서 둘째 문장의 주어를 복수로 바꿨다(Were - were cooking).")
RV(6, 94, "F", fx=True, why="정답 조합(Was - were playing)이 B·C와 같은 짜임이었다. 수정 예시에서 둘째 문장의 주어를 단수로 바꿨다(Was - was playing).")

X(6, 95, r="진행형의 be동사는 주어에 맞춘다. 단수 주어에는 is/was, 복수 주어에는 are/were가 들어간다.",
  n=["The baby는 단수라 is(was)가 들어가므로", "My sister는 단수라 is(was)가 들어가므로", "The teacher는 단수라 is(was)가 들어가므로", "The cats는 복수라 are(were)가 들어가 나머지와 다르므로", "My dad는 단수라 is(was)가 들어가므로"],
  st="① 문장마다 주어가 단수인지 복수인지만 가른다. 현재든 과거든 단수와 복수는 다른 be동사를 쓴다. → ② 하나만 다른 것을 찾는다. → ③ {0} 정답은 {n}.",
  R="④의 The cats만 복수다.", B="②의 We만 복수다.", C="③의 Mina만 단수다. You에도 are(were)를 쓴다.", D="①의 The boys만 복수다.", E="④의 Dad만 단수다.", F="⑤의 My friends만 복수다.")

X(6, 96, r="과거에 진행 중이던 일은 was/were + -ing로 쓴다. 단수 주어에는 was, 복수 주어에는 were다.",
  n=["am은 주어 I에 쓰는 현재형이므로", "우리말이 ‘~하고 있었다’라 현재형을 쓸 수 없으므로", "단수 주어 Grace에 맞는 과거형이므로", "단수 주어에 were를 쓸 수 없으므로", "be는 원형이라 그대로 쓸 수 없으므로"],
  st="① 우리말(‘~하고 있었다’)과 때를 나타내는 말({0})을 본다. 과거다. → ② 주어를 본다: {1}. → ③ 정답은 {a}.",
  R=("at that time", "Grace(단수) → was"), B=("at that time", "Tom(단수) → was"), C=("at that time", "Mina(단수) → was"), D=("at eight last night", "The twins(복수) → were"), E=("at that time", "The bird(단수) → was"),
  F=("then", "The puppy(단수) → was"))

X(6, 97, r="Was/Were ~ 질문에는 was/were로 답한다. 대답과 이어지는 문장의 be동사는 각각의 주어에 맞춘다.",
  n=["she에 wasn't, 이어지는 문장의 She에 was가 알맞으므로", "뒤 문장은 ‘놀고 있었다’는 긍정이어야 하므로", "she에 weren't를 쓸 수 없으므로", "Was 의문문에 didn't로 답할 수 없으므로", "과거의 질문에 현재형 isn't로 답할 수 없으므로"],
  st="① 첫 빈칸: 대답이 {0}. → ② 둘째 빈칸: 주어가 {1}. → ③ 정답은 {a}.",
  R=("No, she ~이므로 wasn't", "She이고 긍정문이므로 was"), B=("Yes, I ~이므로 was", "I이므로 was"), C=("No, he ~이므로 wasn't", "His sisters(복수)이므로 were"), D=("No, they ~이므로 weren't", "They이므로 were"),
  E=("Yes, he ~이므로 was", "my sisters(복수)이므로 were"), F=("Yes, they ~이므로 were", "Jane(단수)이므로 was"))
RV(6, 97, "E", v="수정(내용)", why="정답 ④ 유일 확인. 다만 대화의 짜임(Were they ~? — No, they ~. They ~.)과 정답 조합(weren't - were), 정답 위치(④)가 D와 모두 같다(유형 간 중복). 발문에도 조건이 붙었다.", fix="대화를 바꿔 정답 조합을 다르게, 발문을 원문항대로")

X(6, 98, r="과거진행형 의문문의 어순: Was/Were + 주어 + -ing + 나머지 ~?",
  n=["Was she writing a letter?의 네 번째 낱말이므로", "she는 두 번째 낱말이므로", "writing은 세 번째 낱말이므로", "was는 첫 번째 낱말이므로", "letter는 다섯 번째 낱말이므로"],
  st="① 의문문으로 배열한다: {0} → ② 앞에서부터 센다. → ③ 네 번째 낱말은 {a}. 정답은 {n}.",
  R="Was she writing a letter?", B="Were you studying English hard?", C="Were they playing soccer outside?", D="Was the girl singing loudly?", E="Was Jane cooking dinner then?", F="Was Tom playing the piano?")

X(6, 99, r="과거진행형 의문문과 대답: Was/Were + 주어 + -ing ~? — Yes, 주어 + was/were. / No, 주어 + wasn't/weren't. you로 물으면 I로 답한다.",
  n=["복수 주어 the boys와 they에는 was를 쓸 수 없으므로", "대답이 과거(were)인데 질문을 현재 Are로 할 수 없으므로", "복수 주어 the boys에는 Was를 쓸 수 없으므로", "대답의 주어 they에는 was를 쓸 수 없으므로", "the boys에 Were, they에 were가 알맞으므로"],
  st="① (A): 질문의 주어가 {0}. → ② (B): 대답이 {1}. → ③ 정답은 {a}.",
  R=("the boys(복수)이므로 Were", "Yes, they ~이므로 were"), B=("Mina(단수)이므로 Was", "Yes, she ~이므로 was"), C=("Tom and Ben(복수)이므로 Were", "No, they ~이므로 weren't"), D=("you이므로 Were", "Yes, I ~이므로 was"),
  E=("Jane(단수)이므로 Was", "No, she ~이므로 wasn't"), F=("you이므로 Were", "No, I ~이므로 wasn't"))
RV(6, 99, "D", fx=True, why="정답 조합(Was - was)과 정답 위치(⑤)가 B와 같고 원문항의 정답 위치와도 같았다. 수정 예시에서 주어를 you로 바꿔 정답 조합이 Were - was가 되게 했다.")
RV(6, 99, "F", fx=True, why="정답 위치가 원문항·B와 같은 ⑤였다. 수정 예시에서 보기 순서를 바꿨다(③).")

X(6, 100, r="과거진행형의 be동사는 주어에 맞춘다: I·3인칭 단수 주어 was, you·복수 주어 were. 의문문에서는 be동사 바로 뒤의 주어를 본다.",
  n=["단수 주어 he에 Was를 바르게 썼으므로", "복수 주어 the girls에 Were를 바르게 썼으므로", "단수 주어 Minho에 Was를 바르게 썼으므로", "주어 you에는 was가 아니라 were를 써야 하므로", "주어 We에 were를 바르게 썼으므로"],
  st="① 밑줄마다 주어를 찾는다. 의문문은 be동사 뒤, 평서문은 밑줄 앞에 있다. → ② was/were가 주어와 맞는지 본다. → ③ {0} 정답은 {n}.",
  R="④의 주어 you에는 were를 쓴다.", B="④의 주어 I에는 Was를 쓴다.", C="③의 주어 Tom은 단수라 Was다.", D="⑤의 주어 The music은 단수라 was다.", E="③의 주어 two boys는 복수라 Were다.", F="②의 주어 the kids는 복수라 Were다.")
RV(6, 100, "F", fx=True, why="수정 예시의 정답 위치가 원문항·B와 같은 ④였다. 틀린 곳을 ②로 옮겼다.")
