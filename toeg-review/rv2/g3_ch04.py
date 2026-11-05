# 3급 CH4 시제 (31~40) 2차 감수
X(3, 31, r="현재의 습관이나 되풀이되는 일은 현재시제로 쓴다. always, usually, often, every ~ 같은 말과 자주 함께 쓰인다.",
  n=["yesterday의 일을 말하는 과거진행형이므로", "1918년의 일을 말하는 과거시제이므로", "tomorrow의 일을 말하는 미래시제이므로", "tonight의 계획을 말하는 be going to이므로", "always와 현재형 gets로 되풀이되는 습관을 나타내므로"],
  st="① 선생님 말의 핵심은 ‘현재의 습관·반복’이다. 보기에서 always, usually, often, every ~ 같은 빈도 표현을 찾는다. → ② 그 문장의 동사가 현재형인지 확인한다. → ③ {n}이 ‘{0}’와 현재형({1})으로 습관을 나타낸다. 나머지는 과거·진행·미래의 일이다.",
  R=("always", "gets"), B=("every morning", "reads"), C=("every day", "studies"), D=("on Sundays", "play"), E=("usually", "walks"), F=("often", "eat"))

X(3, 32, r="과거진행형(was/were + -ing)은 과거의 어느 때에 진행 중이던 일을 나타내며 ‘~하고 있었다’로 옮긴다.",
  n=["‘썼다’는 단순 과거라 진행의 뜻이 빠졌으므로", "‘쓰고 있다’는 현재진행이므로", "‘쓸 것이다’는 미래이므로", "was writing(과거진행)과 all morning(아침 내내)을 바르게 옮겼으므로", "‘쓴다’는 현재의 습관이므로"],
  st="① 밑줄 문장의 동사 형태를 본다. {0}는 ‘was/were + -ing’, 곧 과거진행형이다. → ② 과거진행형은 ‘~하고 있었다’로 옮긴다. → ③ ‘~했다’, ‘~하고 있다’, ‘~할 것이다’, ‘~한다’를 지운다. 정답은 {n}.",
  R="was writing", B="was watching", C="were studying", D="was cooking", E="was reading", F="was sleeping")

X(3, 33, r="belong, know, want, own, prefer, understand처럼 소유·인식·감정 상태를 나타내는 동사는 진행형으로 쓰지 않는다.",
  n=["jump는 동작을 나타내 진행형으로 쓸 수 있으므로", "dance는 동작을 나타내 진행형으로 쓸 수 있으므로", "belong(~에 속하다)은 상태를 나타내 진행형으로 쓰지 않으므로", "read는 동작을 나타내 진행형으로 쓸 수 있으므로", "write는 동작을 나타내 진행형으로 쓸 수 있으므로"],
  st="① 동사마다 ‘지금 ~하고 있는 중이다’로 말할 수 있는 동작인지 본다. → ② 소유·인식·감정처럼 이어지는 상태를 나타내는 동사는 진행형으로 쓰지 않는다. → ③ {n}의 {0}만 상태 동사다. 나머지는 모두 동작이다.",
  R="belong(~에 속하다)", B="prefer(더 좋아하다)", C="know(알다)", D="want(원하다)", E="own(소유하다)", F="understand(이해하다)")

X(3, 34, r="will 뒤에는 be동사의 원형 be를 쓴다. 과거진행형은 was/were + -ing, be going to는 주어에 맞춘 am/are/is + going to다.",
  n=["will 뒤에 be, 주어 I의 과거진행에 was, 주어 She에 is를 쓰므로", "주어 I에 were, She에 are를 쓸 수 없으므로", "will 뒤에 being을 쓸 수 없으므로", "주어 She에 are를 쓸 수 없으므로", "will 뒤에 been을 쓸 수 없으므로"],
  st="① 첫째 빈칸은 will 뒤다. 조동사 뒤이므로 원형 be가 온다. → ② 둘째 빈칸은 과거진행형(-ing, when ~)이다. 주어({0})에 맞춰 {1} → ③ 셋째 빈칸은 be going to다. 주어({2})에 맞춰 {3} 정답은 {n}.",
  R=("I", "was를 쓴다.", "She", "is를 쓴다."), B=("We", "were를 쓴다.", "My dad", "is를 쓴다."), C=("They", "were를 쓴다.", "We", "are를 쓴다."), D=("Jane", "was를 쓴다.", "I", "am을 쓴다."),
  E=("The boys", "were를 쓴다.", "I", "am을 쓴다."), F=("I", "was를 쓴다.", "They", "are를 쓴다."))

X(3, 35, r="‘~할 예정이다’는 ‘be동사 + going to + 동사원형’으로 나타낸다. be동사는 주어에 맞춘다.",
  n=["are going to + 동사원형으로 바르게 옮겼으므로", "be동사 are가 빠졌으므로", "going 뒤에 to가 빠졌으므로", "주어 They에 is를 쓸 수 없으므로", "going이 아니라 go를 써서 틀렸으므로"],
  st="① ‘~할 예정이다’는 be going to + 동사원형이다. → ② 세 조각을 차례로 확인한다. 주어({0})에 맞는 be동사({1}), going to, 동사원형({2}). → ③ 하나도 빠지거나 바뀌지 않은 {n}이 정답이다.",
  R=("They", "are", "watch"), B=("I", "am", "learn"), C=("Jane", "is", "study"), D=("I", "am", "buy"), E=("Tom", "is", "visit"), F=("We", "are", "eat"))

X(3, 36, r="will의 부정은 will not(won't) + 동사원형이다. be going to의 부정은 be동사 뒤에 not을 붙인다.",
  n=["willn't라는 줄임말은 없으므로", "will not의 줄임말 won't + 동사원형으로 바르게 바꿨으므로", "조동사 will의 부정에 don't를 쓰지 않으므로", "will이 없어지고 be동사 뒤에 동사원형이 왔으므로", "won't 뒤에 be come을 쓸 수 없으므로"],
  st="① 문장의 (조)동사를 찾는다: {0}. → ② {1} → ③ 정답은 {n}.",
  R=("will come", "will의 부정은 will not, 줄여서 won't다. 뒤에는 동사원형이 그대로 온다."), B=("are going to visit", "be going to의 부정은 be동사 뒤에 not을 붙인다(aren't going to). do/does는 쓰지 않는다."),
  C=("is going to study", "be going to의 부정은 be동사 뒤에 not을 붙인다(isn't going to). do/does는 쓰지 않는다."), D=("is going to buy", "be going to의 부정은 be동사 뒤에 not을 붙인다(isn't going to). do/does는 쓰지 않는다."),
  E=("are going to leave", "be going to의 부정은 be동사 뒤에 not을 붙인다(aren't going to). do/does는 쓰지 않는다."), F=("am going to be", "be going to의 부정은 be동사 뒤에 not을 붙인다(am not going to). do/does는 쓰지 않는다."))

X(3, 37, r="know, have(가지다), want, believe, own, understand 같은 상태 동사는 진행형으로 쓰지 않고 현재형으로 쓴다.",
  n=["be동사와 일반동사 현재형을 함께 쓸 수 없으므로", "과거진행형으로 바꿔도 상태 동사는 진행형으로 쓰지 않으므로", "상태 동사 know를 현재형으로 쓰고 주어 He에 맞춰 -s를 붙였으므로", "주어 He에는 knows를 써야 하므로", "be동사 뒤에 동사원형을 쓸 수 없으므로"],
  st="① 밑줄의 동사({0})는 상태를 나타낸다. 우리말이 ‘~하고 있다’여도 진행형으로 쓰지 않는다. → ② 진행형을 현재형으로 고친다. be동사는 빼고, 주어({1})에 수를 맞춘다. → ③ 정답은 {a}.",
  R=("know", "He, 3인칭 단수"), B=("have, ‘가지다’의 뜻", "My uncle, 3인칭 단수"), C=("want", "She, 3인칭 단수"), D=("believe", "I"), E=("own", "They, 복수"), F=("understand", "Tom, 3인칭 단수"))

X(3, 38, r="과거진행형의 의문문은 ‘Was/Were + 주어 + -ing ~?’이고, 대답은 ‘Yes, 주어 + was/were.’다.",
  n=["대답이 were이므로 Do로 물을 수 없으므로", "Are 뒤에 bake를 쓸 수 없고 대답의 시제와도 맞지 않으므로", "대답 they were에 맞는 과거진행 의문문이므로", "Did 뒤에 baked를 쓸 수 없고 대답과도 맞지 않으므로", "주어 they에 Was를 쓸 수 없으므로"],
  st="① 대답({0})의 동사가 질문의 첫 낱말을 정한다. 질문도 {1}로 시작한다. → ② be동사로 시작하는 진행형 의문문이므로 주어 뒤에는 -ing가 온다. → ③ 정답은 {a}.",
  R=("Yes, they were.", "Were"), B=("Yes, he was.", "Was"), C=("Yes, she was.", "Was"), D=("Yes, they were.", "Were"), E=("Yes, he was.", "Was"), F=("Yes, I was.", "Were(you로 물으면 I로 답한다)"))

X(3, 39, r="현재진행형은 ‘be동사 + 동사의 -ing형’이다. be동사는 주어에 맞추고, -ing를 붙일 때 철자에 주의한다(sit → sitting, have → having).",
  pre=["문장별 판정: (가) O. Is + 주어 + -ing의 의문문. (나) X. am not watching으로 써야 한다. (다) X. sit은 t를 한 번 더 써서 sitting. (라) O. are flying."],
  n=["(나)가 틀렸으므로", "(가)와 (라)가 모두 옳으므로", "(나)와 (다)가 모두 틀렸으므로", "(나)가 틀렸으므로", "(다)가 틀렸으므로"],
  st="① 문장마다 ‘be동사 + -ing’가 갖춰졌는지 본다. be동사가 주어에 맞는지, 뒤가 -ing인지 확인한다. → ② -ing의 철자(e를 빼는 동사, 끝 자음을 겹쳐 쓰는 동사)와 진행형으로 쓰지 않는 상태 동사도 확인한다. → ③ 틀린 문장을 지운다: {0}. 남은 두 문장을 묶은 {a}가 정답이다.",
  R="(나) am not watch, (다) siting", B="(나) haveing, (라) is knowing", C="(나) are study, (라) They is", D="(다) is know, (라) Tom are", E="(가) leaveing, (라) I is", F="(가) The dog are, (다) am want")
RV(3, 39, "C", fx=True, why="수정 예시의 정답 조합((가), (라))이 원문항과 같아, 문장을 바꿔 옳은 문장을 (가), (다)로 했다.")

X(3, 40, r="과거의 일은 과거형으로 쓰고(규칙동사는 -ed, 자음 + y는 -ied), did not 뒤에는 동사원형을 쓴다. 과거진행형은 was/were + -ing, 미래의 계획은 be going to + 동사원형이다.",
  n=["study의 y를 i로 바꾸고 -ed를 붙인 과거형이라 옳은 설명이므로", "did not 뒤에는 동사원형을 쓴다. see가 옳으므로 saw로 고칠 필요가 없으므로", "과거의 어느 때에 진행 중이던 동작이라 옳은 설명이므로", "-e로 끝나는 동사는 -d만 붙이므로 옳은 설명이므로", "be going to + 동사원형이라 옳은 설명이므로"],
  st="① 밑줄마다 형태가 옳은지 먼저 본다. 이 지문의 밑줄 다섯 개는 모두 옳은 표현이다. → ② 설명이 그 형태를 바르게 풀었는지 본다. 옳은 표현을 고쳐야 한다고 하거나 시제 이름을 틀리게 말하면 틀린 설명이다. → ③ {n}의 설명이 틀렸다. {0}",
  R="didn't 뒤에는 동사원형을 쓰므로 see가 옳다. saw로 고치면 안 된다.", B="was baking은 현재진행형이 아니라 과거진행형이다.", C="buy의 과거형은 buyed가 아니라 bought다.", D="eat은 불규칙동사라 과거형이 ate다.",
  E="주어 We는 복수이므로 과거형은 were다.", F="read는 과거형도 철자가 read다.")
RV(3, 40, "DEF", fx=True, why="수정 예시의 지문이 원문항(45단어 안팎)의 절반에 못 미쳐(17~22단어), 밑줄 친 표현은 그대로 두고 지문을 원문항 수준으로 늘렸다.")
