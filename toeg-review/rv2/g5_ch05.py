# 5급 CH5 과거진행형 (41~50) 2차 감수
X(5, 41, r="-ing형 만들기: 대부분 그대로 -ing, -e로 끝나면 e를 빼고, -ie는 y로 바꾸고, 단모음 + 단자음으로 끝나면 자음을 한 번 더 쓴다. y로 끝나는 동사는 y를 그대로 두고 -ing를 붙인다(study → studying).",
  n=["그대로 -ing를 붙인 옳은 형태이므로", "y를 빼지 않고 그대로 붙여 studying으로 써야 하므로", "그대로 -ing를 붙인 옳은 형태이므로", "e를 빼고 -ing를 붙인 옳은 형태이므로", "-ie를 y로 바꾸고 -ing를 붙인 옳은 형태이므로"],
  st="① 동사의 끝을 본다: -e, -ie, -y, 단모음 + 단자음 가운데 어느 것인지 가른다. → ② {0} → ③ 정답은 {a}.",
  R="study는 y로 끝나므로 y를 그대로 두고 studying이다. -ed를 붙일 때(studied)와 헷갈리지 않는다.", B="write는 -e로 끝나 e를 빼고 writing이다.", C="cry는 y를 그대로 두고 crying이다. y를 i로 바꾸는 것은 -ed, -es를 붙일 때다.",
  D="visit은 강세가 앞에 있어 t를 겹쳐 쓰지 않는다(visiting).", E="wait는 모음이 둘(ai)이라 t를 겹쳐 쓰지 않는다(waiting).", F="x로 끝나는 동사는 자음을 겹쳐 쓰지 않는다(fixing).")

X(5, 42, r="과거진행형은 was/were + 동사원형-ing다. am/is/are + -ing는 현재진행형이고, 동사의 과거형만 쓴 것은 단순 과거다.",
  n=["was + washing으로 과거진행형이므로", "were + playing으로 과거진행형이므로", "are + jumping은 현재진행형이므로", "was + cooking으로 과거진행형이므로", "were + walking으로 과거진행형이므로"],
  st="① 문장마다 -ing형 앞의 be동사만 본다. → ② was/were면 과거진행형, am/is/are면 현재진행형이다. be동사 없이 과거형만 있으면 단순 과거다. → ③ {0} 정답은 {n}.",
  R="③만 are를 썼다.", B="③만 is를 썼고 now도 현재를 나타낸다.", C="⑤만 is를 썼다.", D="②는 watched만 있고 was/were + -ing가 없다.", E="④만 are를 썼고 now도 현재를 나타낸다.", F="①만 are를 썼다.")

X(5, 43, r="‘~하고 있었다’는 과거진행형 was/were + 동사원형-ing로 쓴다. 주어가 I·3인칭 단수면 was, you·복수면 were다.",
  n=["단순 과거라 ‘가고 있었다’는 진행의 뜻이 없으므로", "현재형이라 과거의 뜻이 없으므로", "was 뒤에 goes를 쓸 수 없으므로", "was + going으로 ‘가고 있었다’를 바르게 나타냈으므로", "go shopping에 at을 쓰지 않고 with 뒤에는 목적격 him을 써야 하므로"],
  st="① 우리말 ‘{0}’ → 과거에 진행 중이던 일이므로 was/were + -ing를 쓴다. → ② 주어({1})에 맞는 be동사는 {2}, -ing형은 {3}. → ③ 시제(현재·단순 과거)나 be동사, 동사 형태가 틀린 문장을 지운다. 정답은 {n}.",
  R=("가고 있었다", "She", "was", "going"), B=("건너고 있었다", "They", "were", "crossing"), C=("뛰고 있었다", "They", "were", "running"), D=("공부하고 있었다", "I", "was", "studying"),
  E=("보고 있었다", "Tom", "was", "watching"), F=("먹고 있었다", "We", "were", "eating"))
RV(5, 43, "C", v="수정(내용)", why="정답 ② 유일 확인. 다만 오답 ④의 runn(They were runn in the park.)은 쓰이지 않는 형태라 그것만 보고 지워진다. 원문항의 오답은 모두 실제 형태(went, goes, was goes)다.", fix="④를 be동사 + 동사원형(were run)으로")

X(5, 44, r="과거진행형은 was/were + 동사원형-ing다. I·3인칭 단수에는 was, you·복수에는 were를 쓴다.",
  n=["She에 were를 쓸 수 없고 were 뒤에 swim도 쓸 수 없으므로", "She에는 was를 써야 하므로", "were 뒤에는 swimming을 써야 하므로", "She에 was + cleaning, You에 were + swimming이 알맞으므로", "과거의 일을 현재형으로 고쳤고 You에 is도 쓸 수 없으므로"],
  st="① 첫 문장: 주어가 {0}. → ② 둘째 문장: 주어가 {1}. → ③ 두 가지를 모두 갖춘 것은 {a}.",
  R=("She이므로 was, 뒤에는 -ing형 cleaning", "You이므로 were, swimming은 그대로"), B=("Tom(단수)이므로 was reading", "We(복수)이므로 were waiting"), C=("My brother(단수)이므로 was washing", "They(복수)이므로 were playing"),
  D=("I이므로 was studying", "Jane(단수)이므로 was는 그대로 두고 write를 writing으로"), E=("We(복수)이므로 were running", "He(단수)이므로 was watching"), F=("The boys(복수)이므로 were sleeping", "I이므로 was는 그대로 두고 cook을 cooking으로"))
RV(5, 44, "C", fx=True, why="첫째 문장(Tom were reading a book.)이 B(Tom were reading a comic book.)와 거의 같다(유형 간 중복). 수정 예시에서 다른 문장(My brother were washing his face.)으로 바꿨다.")

X(5, 45, r="과거진행형의 be동사는 주어에 맞춘다: I·3인칭 단수 was(wasn't), you·복수 were(weren't). 부정문은 was/were 뒤에 not을 둔다.",
  n=["단수 주어 The man에는 wasn't를 써야 하므로", "Tony에 was + walking을 바르게 썼으므로", "We에 weren't + having을 바르게 썼으므로", "The baby에 was + crying을 바르게 썼으므로", "She에 was + doing을 바르게 썼으므로"],
  st="① 문장마다 주어가 단수인지 복수인지 가른다. → ② was(n't)/were(n't)가 주어와 맞는지, not이 be동사 뒤에 있는지 본다. → ③ {0} 정답은 {n}.",
  R="①의 The man은 단수인데 weren't를 썼다.", B="③의 Jane은 단수인데 weren't를 썼다.", C="②의 The girls는 복수인데 wasn't를 썼다.", D="⑤의 주어 I에는 was를 쓴다.", E="④의 Mina and Jiho는 복수인데 was를 썼다.",
  F="①은 not이 was 앞에 있다(was not cooking).")

X(5, 46, r="be동사의 과거형은 주어가 I·3인칭 단수면 was, you·복수면 were다. am/is/are는 현재형이다.",
  n=["현재형이고 He와도 맞지 않으므로", "현재형이므로", "현재형이고 He와도 맞지 않으므로", "3인칭 단수 He에 맞는 과거형이므로", "과거형이지만 He와 맞지 않으므로"],
  st="① 현재형(am, is, are)을 먼저 지운다. 남는 것은 was와 were다. → ② 주어를 본다: {0}. → ③ 정답은 {a}.",
  R="He는 3인칭 단수", B="The children은 복수", C="They는 복수", D="I에는 was", E="We는 복수", F="Jane은 3인칭 단수")

X(5, 47, r="과거진행형 의문문(Was/Were + 주어 + -ing ~?)에는 was/were로 답한다: No, 주어 + wasn't/weren't.",
  n=["be동사 의문문에 do로 답할 수 없으므로", "Were they ~?에 they weren't로 바르게 답했으므로", "they에 wasn't를 쓸 수 없으므로", "be동사 의문문에 did로 답할 수 없으므로", "과거의 질문에 현재형으로 답할 수 없으므로"],
  st="① 질문이 be동사 과거형({0})으로 시작하므로 대답도 be동사 과거형으로 한다. do/did와 현재형을 지운다. → ② 대답의 주어가 {1}. → ③ 정답은 {a}.",
  R=("Were", "they이므로 weren't"), B=("Was", "she이므로 wasn't"), C=("Was", "she이므로 wasn't"), D=("Were", "I이므로 wasn't. 질문의 Were에 끌려 weren't를 고르지 않는다"), E=("Was", "he이므로 wasn't"), F=("Were", "we이므로 weren't"))
RV(5, 47, "F", v="수정(내용)", why="정답 ③ 유일 확인. 다만 대화(Were we late? — No, we weren't. We were early.)에 -ing형이 없어 과거진행형이 아니라 be동사 과거 의문문이다. 이 단원의 문법 요소(과거진행형 의문문의 대답)와 맞지 않는다.", fix="질문과 대답을 과거진행형 문장으로")

X(5, 48, r="과거진행형 의문문의 어순은 Was/Were + 주어 + 동사원형-ing + 나머지 ~?이다.",
  n=["평서문 어순에 물음표만 붙였으므로", "목적어 soccer가 playing 앞에 왔으므로", "Were + they + playing + soccer의 순서이므로", "be동사가 문장 맨 앞에 오지 않았으므로", "주어 they가 Were 바로 뒤에 오지 않았으므로"],
  st="① 의문문이므로 be동사({0})를 맨 앞에 둔다. → ② 바로 뒤에 주어({1}), 그 뒤에 -ing형({2}), 마지막에 나머지({3})를 둔다. → ③ 이 순서인 것은 {n}.",
  R=("Were", "they", "playing", "soccer"), B=("Was", "Tom", "sleeping", "at eight"), C=("Was", "she", "reading", "a book"), D=("Were", "you", "studying", "English"), E=("Was", "Tom", "watching", "TV"), F=("Were", "we", "eating", "dinner"))

X(5, 49, r="과거의 한 시점에 있던 곳은 was/were로, 그때 하고 있던 일은 was/were + -ing로 쓴다. be동사는 주어에 맞춘다.",
  n=["주어 I에 was, 그때 하던 일은 was studying이므로", "주어 I에 were를 쓸 수 없으므로", "어제의 일을 현재진행형 am studying으로 쓸 수 없으므로", "주어 I에 were를 쓸 수 없으므로", "과거의 일이고 주어가 I인데 studies를 쓸 수 없으므로"],
  st="① 때를 본다: {0}. 과거의 한 시점이다. → ② (A): 주어 {1}. → ③ (B): 그때 진행 중이던 일이므로 {2}. 정답은 {n}.",
  R=("At 3 o'clock yesterday", "I에는 was", "was studying"), B=("At nine last night", "Jane(단수)에는 was", "was writing. be동사 없이 writing만 쓸 수 없다"), C=("At 5 yesterday", "they(복수)에는 were", "were playing"),
  D=("At eight yesterday evening", "Jane(단수)에는 was", "was reading"), E=("At noon yesterday", "we(복수)에는 were", "were eating"), F=("At seven yesterday evening", "Tom(단수)에는 was", "was watching"))

X(5, 50, r="과거진행형 의문사 의문문은 의문사 + was/were + 주어 + 동사원형-ing ~?이다. you는 한 사람이어도 be동사 과거형으로 were를 쓴다.",
  n=["의문사 What은 문장 맨 앞에 두므로", "you에 맞는 be동사 과거형 were가 필요하므로", "시각 앞에는 전치사 at을 쓰므로", "you는 한 사람을 가리켜도 were를 쓰므로", "의문문은 be동사가 주어 앞에 오므로"],
  st="① 우리말을 영어 문장으로 먼저 써 본다: {0} → ② 설명을 하나씩 이 문장에 대어 본다. → ③ {1} 정답은 {n}.",
  R=("What were you doing at noon?", "you에는 was가 아니라 were를 쓴다."), B=("What were they doing at six?", "they는 복수이므로 was가 아니라 were를 쓴다."), C=("What was she doing at eight yesterday?", "진행형 의문문은 did가 아니라 be동사로 만든다."),
  D=("What were they doing yesterday?", "의문사 What은 문장 끝이 아니라 맨 앞에 둔다."), E=("What was Tom doing then?", "be동사 뒤에는 did가 아니라 doing을 쓴다."), F=("What were we doing then?", "we는 복수이므로 was가 아니라 were를 쓴다."))
RV(5, 50, "E", fx=True, why="수정 예시의 틀린 설명(‘그때’는 now로 쓴다)이 문법이 아니라 낱말 뜻을 묻는 내용이어서 원문항(주어와 be동사)보다 쉬웠다. 진행형의 형태(be동사 뒤에 did를 쓴다)를 묻는 설명으로 바꿨다.")
