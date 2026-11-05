# 6급 CH5 일반동사 과거 (41~50) 2차 감수
X(6, 41, r="규칙 과거형: 대부분 -ed, 자음 + y는 y를 i로 바꾸고 -ed(cried), 단모음 + 단자음은 자음을 겹쳐 -ed(shopped). buy - bought처럼 불규칙형도 있다.",
  n=["-ed를 붙인 옳은 형태이므로", "-ed를 붙인 옳은 형태이므로", "자음 + y라 y를 i로 바꿔 cried로 써야 하므로", "단모음 + 단자음이라 p를 겹쳐 쓴 옳은 형태이므로", "buy의 불규칙 과거형으로 옳으므로"],
  st="① 동사의 끝을 본다: 자음 + y인지, 단모음 + 단자음인지, 모음 + y인지. → ② 그 끝에 맞는 규칙(-ied, 자음 겹치기, 그대로 -ed)대로 되었는지 본다. → ③ {0} 정답은 {a}.",
  R="cry는 자음 + y이므로 cried다.", B="stop은 단모음 + 단자음이므로 stopped다.", C="plan은 단모음 + 단자음이므로 planned다.", D="study는 자음 + y이므로 studied다.", E="carry는 자음 + y이므로 carried다.",
  F="skip은 단모음 + 단자음이므로 skipped다.")
RV(6, 41, "F", v="수정(내용)", why="정답 ③ 유일 확인. 다만 정답 짝(plan - planed)이 C의 정답 짝과 똑같고(유형 간 중복), ④(cry - cried)는 원문항 정답(cry - cryed)을 바르게 고친 짝이다.", fix="정답 짝과 ④를 다른 동사로")

X(6, 42, r="yesterday, last ~처럼 과거의 때를 나타내는 말이 있으면 동사의 과거형을 쓴다. did와 과거형을 함께 쓰지 않는다.",
  n=["yesterday에 맞는 과거형이므로", "yesterday가 있어 현재형을 쓸 수 없으므로", "yesterday가 있어 현재형을 쓸 수 없고 주어 I와도 맞지 않으므로", "be동사 없이 -ing형만 쓸 수 없으므로", "plaies라는 형태는 없으므로"],
  st="① 때를 나타내는 말을 찾는다: {0}. 과거다. → ② 동사의 과거형을 만든다: {1}. → ③ 현재형, -ing형, did + 과거형을 지운다. 정답은 {a}.",
  R=("yesterday", "play → played(모음 + y는 그대로 -ed)"), B=("yesterday", "clean → cleaned"), C=("yesterday", "write → wrote(불규칙)"), D=("yesterday", "study → studied(자음 + y)"), E=("last night", "cook → cooked"),
  F=("last week", "visit → visited"))
RV(6, 42, "E", v="수정(내용)", why="정답 ③ 유일 확인. 다만 문장과 정답(She ___ TV last night. — watched)이 같은 단원 46번 원문항(She ___ a movie last night. — watched)과 거의 같다. 발문에도 ‘과거의 일을 나타내도록’이 붙었다.", fix="동사를 바꾸고 발문을 원문항대로")

X(6, 43, r="과거 부정문은 didn't + 동사원형, 과거 긍정문은 동사의 과거형으로 쓴다. last night, last week 같은 말이 과거임을 알려 준다.",
  n=["last week가 있어 현재형 starts를 쓸 수 없으므로", "last night이 있어 don't를 쓸 수 없으므로", "didn't + sleep, 과거형 started로 알맞으므로", "두 문장 모두 과거인데 현재형을 썼으므로", "last night이 있어 doesn't를 쓸 수 없고 startes라는 형태도 없으므로"],
  st="① 첫 문장: {0}이 있고 뒤에 동사원형이 있으므로 didn't가 들어간다. → ② 둘째 문장: {1}이 있고 빈칸이 동사 자리이므로 과거형 {2}. → ③ 정답은 {a}.",
  R=("last night", "last week", "started"), B=("yesterday", "yesterday", "opened"), C=("yesterday", "last night", "cleaned"), D=("last night", "an hour ago", "closed"), E=("last week", "last Sunday", "cooked"),
  F=("yesterday", "last night", "washed"))
RV(6, 43, "DF", v="수정(내용)", why="정답 유일 확인. 다만 정답(didn't - opened)이 B와 똑같다(유형 간 중복). 발문에도 원문항에 없는 조건이 붙었고, F는 원문항에 있는 문장 앞 ‘-’ 표시도 없다.", fix="둘째 문장의 동사를 바꿔 정답이 겹치지 않게, 발문·표기를 원문항대로")
RV(6, 43, "CE", fx=True, why="변형에는 원문항에 있는 문장 앞 ‘-’ 표시가 없다. 수정 예시에서 원문항처럼 ‘-’를 붙였다.")

X(6, 44, r="일반동사 과거 부정문은 주어 + didn't(did not) + 동사원형이다.",
  n=["didn't + 동사원형 jump로 알맞으므로", "didn't 뒤에 과거형 jumped를 쓸 수 없으므로", "과거의 문장을 don't로 부정할 수 없으므로", "과거의 문장을 doesn't로 부정할 수 없으므로", "일반동사의 부정에 wasn't를 쓸 수 없으므로"],
  st="① 동사를 본다: {0}. 일반동사의 과거형이다. → ② 과거 부정은 didn't를 쓰고, 뒤의 동사는 원형으로 돌린다: didn't {1}. → ③ 정답은 {a}.",
  R=("jumped", "jump"), B=("cleaned", "clean"), C=("watched", "watch"), D=("carried", "carry(carried → carry)"), E=("opened", "open"), F=("played", "play"))

X(6, 45, r="현재의 문장을 과거로 바꿀 때는 동사를 과거형으로 바꾼다. 불규칙 동사는 정해진 과거형을 쓴다(make - made, eat - ate, go - went).",
  n=["make의 과거형은 maked가 아니라 made이므로", "did와 과거형을 함께 쓰지 않으므로", "make의 과거형 made를 바르게 썼으므로", "yesterday가 있는데 현재형 makes를 썼으므로", "과거형이 아니고 주어 He와도 맞지 않으므로"],
  st="① 원래 문장의 동사를 찾는다: {0}. → ② 그 과거형은 {1}. → ③ 과거형을 바르게 쓰고 때를 나타내는 말도 과거인 문장을 고른다. 정답은 {n}.",
  R=("makes", "made(불규칙)"), B=("eat", "ate(불규칙)"), C=("has", "had(불규칙)"), D=("see", "saw(불규칙)"), E=("goes", "went(불규칙)"), F=("takes", "took(불규칙)"))
RV(6, 45, "F", v="수정(내용)", why="정답 ⑤ 유일 확인. 다만 오답 네 개에는 원문에 있는 to work가 빠져 있고 정답에만 들어 있어, 문장이 온전한 것만 골라도 답이 된다. 발문도 원문항과 다르다.", fix="모든 보기에 to work를 넣고 발문을 원문항대로")

X(6, 46, r="last night, yesterday처럼 과거의 때를 나타내는 말이 있으면 동사의 과거형을 쓴다. 규칙동사는 -ed를 붙인다.",
  n=["last night에 맞는 과거형이므로", "watchd라는 형태는 없으므로(-ed를 붙인다)", "last night이 있어 현재형을 쓸 수 없으므로", "be동사 없이 -ing형만 쓸 수 없으므로", "to부정사는 동사 자리에 쓸 수 없으므로"],
  st="① 빈칸은 주어 바로 뒤의 동사 자리다. -ing형과 to부정사를 지운다. → ② {0}. → ③ 과거형은 {a}.",
  R="last night이 있으므로 과거형이 필요하다", B="주어 They에 cleans는 맞지 않고, 철자가 바른 과거형은 하나뿐이다", C="last night이 있으므로 과거형이 필요하다", D="yesterday가 있으므로 과거형이 필요하다", E="yesterday가 있으므로 과거형이 필요하다",
  F="last week가 있으므로 과거형이 필요하다")
RV(6, 46, "CDEF", v="수정(내용)", why="정답 유일 확인. 다만 문장과 정답이 같은 단원 42번과 겹친다: C(They ___ English — studied)는 42번 D와, D(visited)는 42번 F와, E(Tom ___ soccer yesterday — played)는 42번 원문항(I ___ the violin yesterday — played)과, F(We ___ the room — cleaned)는 42번 B와 거의 같고 46번 B의 정답도 cleaned다. 발문에도 원문항에 없는 말이 붙었다.", fix="동사를 바꾸고 발문을 원문항대로")

X(6, 47, r="‘~하지 않았다’는 didn't + 동사원형으로 쓴다. didn't 뒤에 과거형을 쓰지 않고, 일반동사를 wasn't/weren't로 부정하지 않는다.",
  n=["didn't + 동사원형 clean으로 바르게 옮겼으므로", "didn't 뒤에 과거형 cleaned를 쓸 수 없으므로", "yesterday가 있어 doesn't를 쓸 수 없으므로", "일반동사 clean의 부정에 wasn't를 쓸 수 없으므로", "not만으로는 일반동사를 부정할 수 없으므로"],
  st="① 우리말 ‘{0}’ → 과거의 부정이므로 didn't가 필요하다. → ② didn't 뒤의 동사는 원형이다: didn't {1}. → ③ doesn't, wasn't/weren't, didn't + 과거형을 지운다. 정답은 {n}.",
  R=("청소하지 않았다", "clean"), B=("보지 않았다", "watch"), C=("가지 않았다", "go"), D=("공부하지 않았다", "study"), E=("(축구를) 하지 않았다", "play"), F=("방문하지 않았다", "visit"))
RV(6, 47, "CDE", fx=True, why="원문항 발문(‘우리말을 영어로 바르게 옮긴 문장’)으로 되돌리면, 때를 나타내는 말만 빠진 옳은 문장(Jane didn't go to school. 등)이 정답과 헷갈릴 수 있다. 수정 예시에서 이 보기를 분명히 틀린 문장(didn't + 과거형)으로 바꿨다.")
RV(6, 47, "F", v="수정(내용)", why="정답 ④ 유일 확인. 다만 우리말과 정답(우리는 어젯밤 TV를 보지 않았다 — We didn't watch TV last night.)이 B(Tom은 어젯밤 TV를 보지 않았다)와 주어만 다르다(유형 간 중복). 발문도 원문항과 다르다.", fix="문장을 새로, 발문을 원문항대로")

X(6, 48, r="일반동사 과거 의문문은 Did + 주어 + 동사원형 ~?이다. Did 뒤에 과거형을 쓰지 않는다.",
  n=["Yes, I did로 답했으므로 과거의 질문이어야 하므로", "Did + you + 동사원형 finish로 바르게 고쳤으므로", "Did 뒤에 finishes를 쓸 수 없으므로", "주어 you에 Does를 쓸 수 없고 대답의 did와도 맞지 않으므로", "Did 뒤에 -ing형을 쓸 수 없으므로"],
  st="① 대답이 {0}이므로 질문은 Did로 시작하는 과거 의문문이다. → ② Did 뒤의 동사는 원형이다: {1}. → ③ 정답은 {a}.",
  R=("Yes, I did", "finished → finish"), B=("Yes, she did", "watched → watch"), C=("Yes, they did", "visited → visit"), D=("Yes, she did", "wrote → write"), E=("Yes, he did", "played → play"),
  F=("Yes, she did", "studied → study"))

X(6, 49, r="[단모음 + 단자음]으로 끝나는 1음절 동사는 마지막 자음을 한 번 더 쓰고 -ed를 붙인다(stop → stopped).",
  n=["첫 글자는 과거형 철자와 관계없으므로", "주어는 과거형 철자와 관계없으므로", "단모음 + 단자음으로 끝나는 1음절 동사라 자음을 겹쳐 쓰므로", "마침표는 과거형 철자와 관계없으므로", "모든 과거형이 자음을 겹쳐 쓰는 것은 아니므로(played, wanted)"],
  st="① 동사원형을 본다: {0}. → ② 끝이 단모음 하나 + 자음 하나이고 한 음절이다: {1}. → ③ 이 까닭을 말한 것을 고른다. 정답은 {n}.",
  R=("stop", "o + p"), B=("clap", "a + p"), C=("drop", "o + p"), D=("hug", "u + g"), E=("rob", "o + b"), F=("plan", "a + n"))

X(6, 50, r="규칙 과거형 철자: 자음 + y → -ied(studied, carried), 단모음 + 단자음 → 자음 겹치기(hugged, dropped), 모음 두 개 + 자음은 겹치지 않는다(rained).",
  n=["study는 자음 + y라 studied로 써야 하므로", "hug는 단모음 + 단자음이라 g를 겹쳐 hugged로 바르게 썼으므로", "drop은 단모음 + 단자음이라 dropped로 써야 하므로", "carry는 자음 + y라 carried로 써야 하므로", "rain은 모음이 둘(ai)이라 n을 겹치지 않고 rained로 써야 하므로"],
  st="① 문장마다 과거형의 원형을 떠올리고 끝(자음 + y, 단모음 + 단자음, -e, 모음 두 개 + 자음)을 본다. → ② 규칙에 맞게 바뀌었는지 본다. → ③ {0} 정답은 {n}.",
  R="②의 hugged만 바르다(hug + g + ed).", B="④의 clapped만 바르다(clap + p + ed).", C="①의 hoped만 바르다(hope + d).", D="③의 worried만 바르다(worry → worried).", E="⑤의 chased만 바르다(chase + d).",
  F="②의 smiled만 바르다(smile + d).")
