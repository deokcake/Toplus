# 6급 CH4 일반동사 (31~40) 2차 감수
X(6, 31, r="3인칭 단수 현재형: 대부분 -s, s·x·sh·ch·o로 끝나면 -es(pushes, fixes, does), 자음 + y는 -ies(studies), have는 has.",
  n=["-s를 붙인 옳은 형태이므로", "sh로 끝나 -es를 붙인 옳은 형태이므로", "x로 끝나면 -es를 붙여 fixes로 써야 하므로", "o로 끝나 -es를 붙인 옳은 형태이므로", "have의 3인칭 단수형 has로 옳으므로"],
  st="① 동사원형의 끝을 본다: s·x·sh·ch·o인지, 자음 + y인지, have인지. → ② 그 끝에 맞는 규칙(-es, -ies, has)대로 되었는지 본다. → ③ {0} 정답은 {a}.",
  R="fix는 x로 끝나므로 fixes다.", B="carry는 자음 + y이므로 carries다.", C="wash는 sh로 끝나므로 washes다.", D="go는 o로 끝나므로 goes다.", E="have의 3인칭 단수형은 has다.", F="study는 자음 + y이므로 studies다.")
RV(6, 31, "D", v="수정(내용)", why="정답 ② 유일 확인. 다만 보기 두 개(① like - likes, ⑤ do - does)가 원문항 ①·④와 똑같다.", fix="겹치는 짝을 다른 동사로")
RV(6, 31, "F", v="수정(내용)", why="정답 ④ 유일 확인. 다만 ②(have - has)는 원문항 ⑤와 똑같고, ③(fix - fixes)은 원문항 정답(fix - fixs)을 바르게 고친 짝이다.", fix="겹치는 짝을 다른 동사로")

X(6, 32, r="현재형 일반동사는 주어가 3인칭 단수일 때만 -s를 붙인다. I, you, we, they, 복수 주어에는 붙이지 않는다.",
  n=["My sister는 3인칭 단수라 likes가 되므로", "The sun은 3인칭 단수라 rises가 되므로", "주어 I에는 s를 붙이지 않으므로", "My cat은 3인칭 단수라 sleeps가 되므로", "She는 3인칭 단수라 speaks가 되므로"],
  st="① 문장마다 주어만 본다. he/she/it이나 한 사람·한 개를 가리키는 명사면 s가 붙는다. → ② I, you, we, they나 둘 이상(A and B, 복수 명사)이면 붙지 않는다. → ③ {0} 정답은 {n}.",
  R="③의 주어 I만 3인칭 단수가 아니다.", B="③의 주어 We만 3인칭 단수가 아니다.", C="②의 주어 Birds만 복수다.", D="④의 주어 Tom and Ben만 두 사람이다.", E="①의 주어 They만 복수다.", F="⑤의 주어 You만 3인칭 단수가 아니다.")

X(6, 33, r="일반동사 현재 부정: 3인칭 단수 주어 + doesn't, 그 밖의 주어(I, you, we, they, 복수) + don't.",
  n=["I에는 don't가 들어가므로", "You에는 don't가 들어가므로", "A cat은 3인칭 단수라 doesn't가 들어가 나머지와 다르므로", "We에는 don't가 들어가므로", "Birds는 복수라 don't가 들어가므로"],
  st="① 문장마다 주어가 3인칭 단수인지 가른다. → ② 3인칭 단수면 doesn't, 아니면 don't를 넣는다. → ③ {0} 정답은 {n}.",
  R="③만 doesn't이고 나머지는 don't다.", B="②만 don't이고 나머지는 doesn't다.", C="③만 don't이고 나머지는 doesn't다.", D="⑤만 don't이고 나머지는 doesn't다.", E="④만 doesn't이고 나머지는 don't다.", F="②만 doesn't이고 나머지는 don't다.")
RV(6, 33, "BDE", v="수정(내용)", why="정답 유일 확인. 다만 서술어가 같은 두 문장이 주어만 달리해 함께 나오고(B: We/Tom ___ need help, D: Tom/The boys ___ play soccer, E: They/Jane ___ read comics) 그 하나가 정답이어서, 두 문장만 견주면 답이 나온다. 원문항에는 이런 짝이 없다.", fix="정답이 아닌 쪽을 다른 문장으로")

X(6, 34, r="일반동사 현재 의문문: Do/Does + 주어 + 동사원형 ~? 주어가 3인칭 단수면 Does를 쓰고 동사의 -s를 뗀다.",
  n=["평서문 어순에 물음표만 붙였으므로", "3인칭 단수 주어 he에는 Does를 쓰고 동사원형을 써야 하므로", "Does 뒤에는 동사원형 walk를 써야 하므로", "Does + he + 동사원형 walk로 바르게 바꿨으므로", "현재의 문장을 과거 Did로 바꿀 수 없고 동사원형도 아니므로"],
  st="① 주어와 동사를 본다: {0}. → ② 주어에 맞는 조동사는 {1}, 그 뒤의 동사는 원형 {2}. → ③ {1} + 주어 + {2} ~?인 것을 고른다. 정답은 {n}.",
  R=("he / walks", "Does", "walk"), B=("she / likes", "Does", "like"), C=("they / play", "Do", "play"), D=("she / drinks", "Does", "drink"), E=("Tom / studies", "Does", "study"), F=("you / read", "Do", "read"))

X(6, 35, r="3인칭 단수 주어의 현재형에만 -s/-es를 붙인다(자음 + y는 -ies). Do/Does 뒤에는 동사원형을 쓰고, 3인칭 단수 주어의 의문문은 Does로 시작한다.",
  n=["주어 We에는 fixes가 아니라 fix를 써야 하므로", "study의 3인칭 단수형은 studies이므로", "주어 she에는 Does를 써야 하므로", "단수 주어 the store에 Does + 동사원형 sell을 바르게 썼으므로", "주어 I에는 arrives가 아니라 arrive를 써야 하므로"],
  st="① 평서문은 주어와 동사의 -s가 맞는지(철자 포함) 본다. → ② 의문문은 Do/Does가 주어와 맞는지, 뒤의 동사가 원형인지 본다. → ③ {0} 정답은 {n}.",
  R="④만 Does + 단수 주어 + 동사원형으로 바르다.", B="③만 Do + you + 동사원형으로 바르다.", C="②만 Does + 단수 주어 + 동사원형으로 바르다.", D="⑤만 Do + 복수 주어 + 동사원형으로 바르다.", E="①만 Does + Jane + 동사원형으로 바르다.",
  F="④만 Do + they + 동사원형으로 바르다.")
RV(6, 35, "B", fx=True, why="수정 예시의 ⑤(Does the store sells bread?)는 원문항 정답 문장(Does the store sell bread?)을 틀리게 바꾼 것이어서 다른 문장으로 바꿨다.")

X(6, 36, r="were는 you, we, they, 복수 주어에 쓴다. I와 3인칭 단수 주어(he, she, it, 한 사람·한 개)에는 was를 쓴다.",
  n=["You에는 were를 쓰므로", "They에는 were를 쓰므로", "We에는 were를 쓰므로", "Sue and James는 두 사람이라 were를 쓰므로", "He는 3인칭 단수라 was를 써야 하므로"],
  st="① 문장마다 주어가 한 사람·한 개인지, you이거나 둘 이상인지 가른다. → ② 한 사람·한 개(you 제외)면 were가 아니라 was다. → ③ {0} 정답은 {n}.",
  R="⑤의 He만 3인칭 단수다.", B="②의 Mina만 3인칭 단수다.", C="①의 Jane만 3인칭 단수다.", D="③의 The cat만 3인칭 단수다.", E="⑤의 She만 3인칭 단수다.", F="④의 Tom만 3인칭 단수다.")

X(6, 37, r="doesn't(does not) 뒤에는 동사원형을 쓴다.",
  n=["doesn't 뒤에 동사원형 have를 썼으므로", "doesn't 뒤에 has를 쓸 수 없으므로", "doesn't 뒤에 -ing형을 쓸 수 없으므로", "doesn't 뒤에 to부정사를 쓸 수 없으므로", "haves라는 형태는 없으므로"],
  st="① 빈칸 앞의 doesn't를 본다. 3인칭 단수의 -s는 이미 does에 들어 있다. → ② 그래서 뒤의 동사는 원형이다. {0} → ③ 남는 것은 {a}.",
  R="has(3인칭 단수형), having, to have를 지운다. haves는 없는 형태다.", B="liked(과거형), likes, liking, to like를 지운다.", C="watched(과거형), watches, watching, to watch를 지운다.", D="studied(과거형), to study, studying, studies를 지운다.",
  E="runs, to run, running, ran(과거형)을 지운다.", F="drinking, drinks, to drink, drank(과거형)를 지운다.")

X(6, 38, r="일반동사 의문문은 Do/Does + 주어 + 동사원형 ~?이다. 3인칭 단수 주어에는 Does, 그 밖에는 Do를 쓴다. be동사와 일반동사 원형을 함께 쓰지 않는다.",
  n=["Does 뒤에는 동사원형 like를 써야 하므로", "주어 she에는 Does를 써야 하므로", "you에 Do + 동사원형 have를 바르게 썼으므로", "주어 they에는 Do를 써야 하므로", "Does 뒤에는 동사원형 smell을 써야 하므로"],
  st="① 맨 앞의 Do/Does가 주어와 맞는지 본다(3인칭 단수 → Does). → ② 뒤의 동사가 원형인지 본다. Is/Are로 시작한 문장은 일반동사 의문문이 될 수 없다. → ③ {0} 정답은 {n}.",
  R="③만 Do + you + have로 두 가지가 모두 맞는다.", B="②만 Does + Tom + read로 두 가지가 모두 맞는다.", C="④만 Do + your cousins + live로 두 가지가 모두 맞는다.", D="⑤만 Do + we + need로 두 가지가 모두 맞는다.",
  E="③만 Do + your friends + live로 두 가지가 모두 맞는다.", F="①만 Does + your brother + drive로 두 가지가 모두 맞는다.")
RV(6, 38, "B", v="수정(내용)", why="정답 ② 유일 확인. 다만 정답 문장(Does Tom read books?)의 틀린 짝(④ Is Tom read books?)이 함께 있어 둘만 견주면 답이 나오고, ③(Do you has a pen?)은 원문항 정답(Do you have a pen?)을 틀리게 바꾼 문장이다. 발문에도 원문항에 없는 조건이 붙었다.", fix="③·④를 다른 문장으로, 발문을 원문항대로")

X(6, 39, r="일반동사 의문문에서 주어가 3인칭 단수면 Does, I·you·we·they·복수면 Do를 쓴다.",
  n=["(A) 단수 your friend에는 Does, (B) 복수 your friends에는 Do를 써야 하므로", "(B)의 복수 주어 your friends에는 Do를 써야 하므로", "단수 주어에 Does, 복수 주어에 Do를 바르게 짝지었으므로", "(A)의 단수 주어 your friend에는 Does를 써야 하므로", "일반동사 like의 의문문에는 be동사를 쓰지 않으므로"],
  st="① (A)의 주어: {0}. → ② (B)의 주어: {1}. → ③ 정답은 {a}.",
  R=("your friend(단수) → Does", "your friends(복수) → Do"), B=("your dog(단수) → Does", "your cat(단수) → Does"), C=("your parents(복수) → Do", "Tom(단수) → Does"), D=("your classmates(복수) → Do", "you → Do"),
  E=("they(복수) → Do", "Jane(단수) → Does"), F=("you → Do", "your sister(단수) → Does"))

X(6, 40, r="일반동사 의문문: 3인칭 단수 주어는 Does, 그 밖의 주어는 Do로 시작하고 뒤의 동사는 원형이다.",
  n=["she가 3인칭 단수라 Does를 쓴다는 옳은 설명이므로", "they는 복수라 Do를 써야 하는데 Does를 써야 한다고 했으므로", "Does 뒤에는 동사원형을 쓴다는 옳은 설명이므로", "일반동사 의문문은 Do/Does로 시작한다는 옳은 설명이므로", "your friends도 복수라 Do를 쓴다는 옳은 설명이므로"],
  st="① 두 문장의 주어와 조동사를 먼저 확인한다: {0}. → ② 학생의 말마다 어느 문장의 무엇을 말하는지 짚어 사실과 견준다. → ③ {1} 정답은 {n}.",
  R=("(가) she → Does, (나) they → Do", "지혜는 복수 주어 they에 Does를 써야 한다고 했다."), B=("(가) he → Does, (나) the boys → Do", "준호는 일반동사 의문문에 Are를 써야 한다고 했다."), C=("(가) she → Does, (나) we → Do", "민수는 she에 Do를 써야 한다고 했다."),
  D=("(가) your brother → Does, (나) Mina and Jane → Do", "태호는 Does 뒤에 plays를 써야 한다고 했다."), E=("(가) Tom → Does, (나) they → Do", "준서는 단수 주어 your sister에도 Do를 쓴다고 했다."),
  F=("(가) Mina → Does, (나) the twins → Do", "수빈은 복수 주어 the twins에 Does를 써야 한다고 했다."))
RV(6, 40, "B", v="수정(내용)", why="정답 ③ 유일 확인. 다만 설명이 두 문장과 관계없는 한 줄짜리 일반 규칙(‘3인칭 단수에는 Does를 써’ 등)이어서 원문항 보기(두 문장을 짚어 설명)의 절반 길이이고, C·E가 이 설명을 되풀이한다. 발문도 원문항과 다르다.", fix="(가)·(나)를 짚는 설명으로, 발문을 원문항대로")
RV(6, 40, "DF", v="수정(내용)", why="정답 유일 확인. 다만 틀린 설명과 정반대인 옳은 설명이 함께 있어 둘만 견주면 답이 나온다(D: ‘Do/Does 뒤에는 동사원형’ ↔ ‘Does 뒤는 plays’, F: ‘(나)의 복수 주어에는 Do’ ↔ ‘(나)의 twins에 Does’). 발문도 원문항과 다르다.", fix="정반대 짝이 되는 옳은 설명을 다른 설명으로")
RV(6, 40, "C", fx=True, why="수정 예시의 ①(she는 3인칭 단수라서 Does)이 틀린 설명 ②(she는 한 명이므로 Do)와 정반대 짝이어서 둘만 견주면 답이 나왔다. ①을 다른 설명으로 바꿨다.")
