# 3급 CH2 일반동사 (11~20) 2차 감수
X(3, 11, r="일반동사의 과거 부정문은 주어와 관계없이 ‘didn't + 동사원형’이다.",
  n=["didn't 뒤에 과거형 went를 쓸 수 없으므로", "didn't + 동사원형 go로 바르게 바꿨으므로", "과거 부정문에 don't를 쓸 수 없고 went도 틀렸으므로", "not만으로는 일반동사를 부정할 수 없으므로", "didn't 뒤에 -ing를 쓸 수 없으므로"],
  st="① 과거 부정문은 ‘didn't + 동사원형’이다. 주어와 관계없이 didn't를 쓴다. → ② 과거형 동사({0})를 원형({1})으로 되돌린다. → ③ didn't 뒤에 과거형을 그대로 둔 것, don't·wasn't를 쓴 것은 지운다. 정답은 {n}.",
  R=("went", "go"), B=("cleaned", "clean"), C=("bought", "buy"), D=("saw", "see"), E=("ate", "eat"), F=("wrote", "write"))

X(3, 12, r="일반동사의 현재 의문문은 ‘Do/Does + 주어 + 동사원형 ~?’이다. 3인칭 단수 주어에는 Does를 쓰고 본동사에는 -s를 붙이지 않는다.",
  n=["Does 뒤에는 동사원형 play를 써야 하므로", "3인칭 단수 주어 he에는 Does를 써야 하므로", "Does + 주어 + 동사원형으로 바르게 바꿨으므로", "일반동사 의문문에 be동사를 쓰지 않으므로", "Does 뒤에 -ing를 쓸 수 없으므로"],
  st="① 주어({0})에 맞는 조동사를 고른다. {1} → ② Do/Does 뒤 본동사는 원형({2})으로 쓴다. → ③ 동사에 -s가 남은 것, -ing를 쓴 것, be동사로 시작한 것은 지운다. 정답은 {n}.",
  R=("he", "3인칭 단수이므로 Does다.", "play"), B=("she", "3인칭 단수이므로 Does다.", "walk"), C=("Jane", "3인칭 단수이므로 Does다.", "study"), D=("they", "복수이므로 Do다.", "watch"), E=("you", "you에는 Do를 쓴다.", "like"),
  F=("Tom", "3인칭 단수이므로 Does다.", "go"))
RV(3, 12, "BCDEF", fx=True, why="수정 예시의 오답 가운데 영어에 없는 형태(Englishs, musics)나 동사와 관계없는 명사 복수형(schools, TVs)이 있어, 원문항의 오답(Does he playing ~?)처럼 동사 형태 오답(Does + -ing)으로 바꿨다.")

X(3, 13, r="불규칙동사의 과거형은 -ed를 붙이지 않고 따로 외운 형태를 쓴다(eat - ate, fly - flew, sleep - slept, write - wrote, read - read).",
  n=["eat의 과거형은 eated가 아니라 ate이므로", "fly의 과거형 flew를 바르게 썼으므로", "read의 과거형은 철자가 같은 read이므로", "sleep의 과거형 slept를 바르게 썼으므로", "write의 과거형 wrote를 바르게 썼으므로"],
  st="① 밑줄 친 동사의 원형을 떠올려 과거형이 규칙(-ed)인지 불규칙인지 가른다. → ② 불규칙동사에 -ed를 붙인 것이 틀린 형태다. → ③ {n}의 {0}.",
  R="eated는 틀렸다. eat의 과거형은 ate다", B="catched는 틀렸다. catch의 과거형은 caught다", C="goed는 틀렸다. go의 과거형은 went다", D="buyed는 틀렸다. buy의 과거형은 bought다", E="seed는 틀렸다. see의 과거형은 saw다",
  F="writed는 틀렸다. write의 과거형은 wrote다")

X(3, 14, r="불규칙동사는 과거형을 따로 외운다. -ed를 붙이면 틀린다(give - gave, fly - flew, catch - caught, leave - left).",
  n=["run - ran, speak - spoke, take - took가 모두 옳으므로", "give의 과거형은 gave이므로", "fly의 과거형은 flew이므로", "catch의 과거형은 caught이므로", "leave의 과거형은 left이므로"],
  st="① 묶음마다 세 동사의 과거형을 하나씩 확인한다. 불규칙동사에 -ed를 붙인 것이 하나라도 있으면 지운다. → ② {0} → ③ 세 개가 모두 옳은 {n}이 정답이다.",
  R="gived(gave), flied(flew), catched(caught), leaved(left)가 틀렸다.", B="keeped(kept), drived(drove), losed(lost), heared(heard)가 틀렸다.", C="drawed(drew), feeded(fed), teached(taught), shutted(shut)가 틀렸다.",
  D="selled(sold), payed(paid), forgetted(forgot), sinked(sank)가 틀렸다.", E="hurted(hurt), lended(lent), sleeped(slept), slided(slid)가 틀렸다.", F="maked(made), raise의 과거형 rose(raised), eated(ate), understanded(understood)가 틀렸다.")

X(3, 15, r="현재 문장에서 3인칭 단수 주어는 동사에 -s를 붙이고 부정은 doesn't로 한다. do/does/did, don't/doesn't/didn't 뒤에는 동사원형을 쓴다.",
  pre=["문장별 판정: ⓐ O. 3인칭 단수 주어에 plays. ⓑ O. doesn't + 동사원형. ⓒ X. Did 뒤에는 동사원형 see. ⓓ O. 3인칭 단수 주어에 sleeps. ⓔ X. We에는 don't를 쓴다."],
  k="밑줄 친 부분이 옳은 문장은 ⓐ, ⓑ, ⓓ 세 개다.", n=["밑줄 친 부분이 옳은 문장은 ⓐ, ⓑ, ⓓ 세 개이므로"] * 5,
  st="① 현재 문장은 주어가 3인칭 단수인지 본다. 3인칭 단수이면 동사에 -s, 부정은 doesn't, 의문은 Does다. → ② do/does/did와 don't/doesn't/didn't 뒤의 동사는 원형이다. → ③ {0} 옳은 문장은 {a}이다.",
  R="ⓒ는 Did 뒤에 saw를 썼고(see), ⓔ는 We에 doesn't를 썼다(don't). 나머지 셋이 옳다.", B="ⓑ는 They에 doesn't(don't), ⓓ는 The baby에 cry(cries), ⓔ는 didn't 뒤에 went(go)를 썼다. ⓐ, ⓒ만 옳다.",
  C="ⓑ는 They에 doesn't(don't), ⓒ는 Does 뒤에 likes(like), ⓔ는 He에 don't(doesn't)를 썼다. ⓐ, ⓓ만 옳다.", D="ⓔ만 틀렸다. didn't 뒤에는 ate가 아니라 eat을 쓴다.", E="ⓒ만 틀렸다. she에는 Do가 아니라 Does를 쓴다.",
  F="ⓓ만 틀렸다. go의 과거형은 goed가 아니라 went다.")
RV(3, 15, "CD", fx=True, why="수정 예시의 정답(3개, ③)이 원문항의 정답 개수·위치와 같아, 한 문장씩 바꿔 C는 2개, D는 4개로 했다.")

X(3, 16, r="Do/Does와 don't/doesn't 뒤의 본동사는 원형으로 쓴다. Do/Does는 주어에 맞춘다(3인칭 단수 - Does).",
  n=["3인칭 단수 주어 she에 Does를 바르게 썼으므로", "Does 뒤에는 speaks가 아니라 동사원형 speak를 써야 하므로", "speak의 목적어로 알맞으므로", "well을 꾸미는 부사로 알맞으므로", "동사를 꾸미는 부사로 알맞으므로"],
  st="① 문장이 Do/Does로 시작하거나 don't/doesn't가 들어 있다. 그 뒤 본동사는 원형이어야 하고, Do/Does는 주어에 맞아야 한다. → ② {0} → ③ 틀린 부분은 {n}이다.",
  R="Does 뒤 본동사에 -s를 붙인 speaks가 틀렸다(speak).", B="doesn't 뒤의 likes가 틀렸다(like).", C="doesn't 뒤의 studies가 틀렸다(study).", D="Do 뒤 본동사 plays가 틀렸다(play).",
  E="Does 뒤 본동사 studies가 틀렸다(study). 사이에 낀 often에 속지 않는다.", F="본동사 watch는 원형이라 옳다. 주어 you에 Does를 쓴 것이 틀렸다(Do).")

X(3, 17, r="일반동사 현재형의 의문문은 ‘Do/Does + 주어 + 동사원형 ~?’이다. 복수 주어와 I, you에는 Do, 3인칭 단수 주어에는 Does를 쓴다.",
  n=["Do + 주어 + 동사원형으로 바르게 바꿨으므로", "복수 주어 they에 Does를 쓸 수 없으므로", "일반동사 의문문에 be동사를 쓰지 않고 plays도 틀렸으므로", "현재 문장을 과거로 바꿨고 Did 뒤에 played도 쓸 수 없으므로", "Do 뒤에는 동사원형 play를 써야 하므로"],
  st="① 동사({0})가 일반동사의 현재형이다. 의문문은 Do/Does + 주어 + 동사원형이다. → ② 주어({1})에 맞춰 {2} 본동사는 원형으로 쓴다. → ③ 정답은 {n}.",
  R=("play", "They, 복수", "Do를 쓴다."), B=("drink", "My parents, 복수", "Do를 쓴다."), C=("studies", "Jane, 3인칭 단수", "Does를 쓴다."), D=("watches", "Tom, 3인칭 단수", "Does를 쓴다."), E=("like", "You", "Do를 쓴다."), F=("need", "We, 복수", "Do를 쓴다."))
RV(3, 17, "CDEF", fx=True, why="수정 예시의 오답 가운데 동사와 관계없는 명사 복수형 오답(every days, at nights, this songs, more times)을 원문항의 오답처럼 동사 형태 오답으로 바꿨다. at nights, more times는 틀렸다고 단정하기도 어렵다.")

X(3, 18, r="일반동사 현재형의 부정문은 ‘do/does + not + 동사원형’이다. 3인칭 단수 주어에는 does not을 쓰고 본동사는 원형으로 되돌린다.",
  n=["not만으로는 일반동사를 부정할 수 없으므로", "does not 뒤에는 동사원형 watch를 써야 하므로", "doesn't 뒤에 -ing를 쓸 수 없으므로", "does not + 동사원형으로 바르게 바꿨으므로", "일반동사의 부정에 be동사를 쓰지 않으므로"],
  st="① 동사({0})가 일반동사의 현재형이다. 부정문은 do/does + not + 동사원형이다. → ② 주어({1})에 맞춰 {2} 본동사는 원형({3})으로 되돌린다. → ③ 정답은 {n}.",
  R=("watches", "He, 3인칭 단수", "does not을 쓴다.", "watch"), B=("drinks", "She, 3인칭 단수", "does not을 쓴다.", "drink"), C=("studies", "Jane, 3인칭 단수", "does not을 쓴다.", "study"), D=("play", "They, 복수", "do not을 쓴다.", "play"),
  E=("like", "I", "do not을 쓴다.", "like"), F=("goes", "Tom, 3인칭 단수", "does not을 쓴다.", "go"))

X(3, 19, r="과거의 일은 동사의 과거형으로 쓴다. 불규칙동사는 과거형을 따로 외우고(have - had, make - made, drink - drank, take - took), 과거형에는 3인칭 단수의 -s를 붙이지 않는다.",
  n=["had는 have의 불규칙 과거형이라 옳은 설명이므로", "과거형에는 3인칭 단수 -s를 붙이지 않는다. made가 옳으므로", "drink의 과거형은 drank라 옳은 설명이므로", "took는 take의 불규칙 과거형이라 옳은 설명이므로", "복수 주어 We에 were를 쓴 것이 맞아 옳은 설명이므로"],
  st="① 글머리의 시간 표현({0})을 보면 모두 과거의 일이다. 밑줄 친 동사가 과거형으로 바른지 하나씩 본다. → ② 지문에서 틀린 과거형은 {1} → ③ 설명마다 이 사실과 견준다. {n}의 설명이 틀렸다. {2}",
  R=("Last Sunday", "ⓒ drinked다(drank).", "과거형에는 3인칭 단수의 -s가 붙지 않는다. made가 맞다."), B=("Last Saturday", "ⓑ swimmed다(swam).", "sit의 과거형은 sitted가 아니라 sat이다. ⓓ는 옳다."),
  C=("Yesterday", "ⓑ buyed다(bought).", "eat의 과거형은 eated가 아니라 ate다. ⓓ는 옳다."), D=("Last night", "ⓑ goed다(went).", "read의 과거형은 철자가 같은 read다. ⓓ는 옳다."),
  E=("Last weekend", "ⓒ eated다(ate).", "make의 과거형은 maked가 아니라 made다. ⓑ는 옳다."), F=("Yesterday", "ⓑ falled다(fell).", "run의 과거형은 runned가 아니라 ran이다. ⓐ는 옳다."))

X(3, 20, r="과거 긍정문에는 동사의 과거형을 쓴다(불규칙: tell - told, spend - spent, see - saw, eat - ate). did/didn't 뒤에는 동사원형을 쓴다.",
  pre=["문장별 판정: 첫째 O. stopped. 둘째 X. tell의 과거형은 told. 셋째 O. spent. 넷째 X. didn't 뒤에는 동사원형 sing. 다섯째 O. saw, ate."],
  k="옳은 문장은 첫째, 셋째, 다섯째 세 개다.", n=["옳은 문장은 첫째, 셋째, 다섯째 세 개이므로"] * 5,
  st="① 문장마다 과거를 나타내는 동사를 찾는다. 긍정문은 과거형이 맞는지(불규칙동사에 -ed를 붙이지 않았는지) 본다. → ② did, didn't가 있으면 뒤의 동사가 원형인지 본다. → ③ {0} 옳은 문장은 {a}이다.",
  R="둘째는 telled(told), 넷째는 didn't sang(sing)이 틀렸다. 나머지 셋이 옳다.", B="둘째는 didn't went(go), 셋째는 teached(taught), 넷째는 losed(lost)가 틀렸다. 첫째와 다섯째만 옳다.",
  C="둘째는 buyed(bought), 셋째는 didn't saw(see), 넷째는 Did ~ ate(eat)가 틀렸다. 첫째와 다섯째만 옳다.", D="다섯째만 틀렸다. make의 과거형은 maked가 아니라 made다.",
  E="넷째만 틀렸다. Did 뒤에는 came이 아니라 come을 쓴다.", F="둘째는 didn't saw(see), 셋째는 writed(wrote), 넷째는 Did ~ went(go), 다섯째는 buyed(bought)가 틀렸다. 첫째만 옳다.")
RV(3, 20, "CD", fx=True, why="수정 예시의 정답(3개, ③)이 원문항의 정답 개수·위치와 같아, 한 문장씩 바꿔 C는 2개, D는 4개로 했다.")
