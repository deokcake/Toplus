# 1급 CH6 동명사 (51~60) 2차 감수
X(1, 51, r="동명사의 의미상 주어는 동명사 앞에 소유격(또는 목적격)으로 쓴다. 전치사 뒤에는 to부정사가 아니라 동명사가 온다.",
  n=["전치사 at 뒤 동명사의 의미상 주어를 주격 he로 쓸 수 없으므로", "소유격 뒤에 to winning이 올 수 없으므로", "전치사 at 뒤에 동명사 winning을 쓰고 그 앞에 의미상 주어를 소유격 his로 썼으므로", "전치사 뒤에 주격과 to부정사를 쓸 수 없으므로",
     "전치사 뒤에는 to부정사가 아니라 동명사가 와야 하므로"],
  st="① 빈칸 앞이 전치사({0})이므로 빈칸에는 명사 역할을 하는 동명사가 와야 한다. → ② 우리말 ‘{1}’에서 그 동작을 한 사람은 문장의 주어와 다르므로, 동명사 앞에 의미상 주어를 소유격으로 밝힌다. → ③ ‘소유격 + -ing’ 순서인 {a}를 고른다.",
  R=("at", "그가 우승한 것"), B=("to", "Jane이 그 결정을 한 것"), C=("at", "Mina가 통과한 것"), D=("at", "Tom이 도착한 것"), E=("of", "그 학생들이 상을 받은 것"), F=("at", "그가 거절한 것"))

X(1, 52, r="deny는 동명사를 목적어로 쓴다. 부인한 때보다 먼저 일어난 일은 완료동명사(having + 과거분사)로 나타낸다.",
  n=["having 뒤에는 breaking이 아니라 과거분사가 와야 하므로", "deny 뒤에 완료동명사 having broken을 써서 부인하기 전에 깬 일을 나타냈으므로", "deny는 to부정사를 목적어로 쓰지 않으므로", "deny는 to부정사를 목적어로 쓰지 않으므로",
     "deny 뒤에 to부정사를 쓸 수 없고 have 뒤에 breaking도 올 수 없으므로"],
  st="① 빈칸 앞의 동사 denied는 동명사만 목적어로 쓰므로 to로 시작하는 보기를 지운다. → ② 첫 문장에서 {0} 일이 부인한 일보다 먼저이므로 having + 과거분사({1})로 나타낸다. → ③ having 뒤가 과거분사가 아닌 보기 등 남은 틀린 형태를 지운다. 정답은 {n}.",
  R=("꽃병을 깬", "having broken"), B=("파일을 공유한", "having shared"), C=("파일을 복사한", "having copied"), D=("돈을 가져간", "having taken"), E=("일찍 떠난", "having left"), F=("비밀을 말한", "having told"))

X(1, 53, r="be worth -ing, it is no use -ing, be busy -ing, spend + 시간 + -ing, 전치사(on, in, at, to) + -ing처럼 뒤에 동명사를 쓰는 표현을 익힌다.",
  n=["be worth 뒤에 동명사 visiting을 바르게 썼으므로", "It is no use 뒤에 동명사 complaining을 바르게 썼으므로", "be busy 뒤에는 to부정사가 아니라 동명사를 쓴다. were busy preparing으로 고쳐야 하므로", "전치사 on 뒤에 동명사 achieving을 바르게 썼으므로",
     "spend + 시간 뒤에 동명사 practicing을 바르게 썼으므로"],
  st="① 밑줄마다 어떤 표현 뒤에 어떤 형태가 왔는지 본다. → ② 다섯 표현({0})은 모두 뒤에 동명사가 와야 한다. → ③ {n}만 동명사가 아니다({1}). 바른 형태는 {2}.",
  R=("be worth, it is no use, be busy, 전치사 on, spend + 시간", "were busy to prepare", "were busy preparing"), B=("be worth, look forward to, have trouble, succeed in, be busy", "is worth to meet", "is worth meeting"),
  C=("be busy, it is no use, be worth, spend + 시간, be good at", "is busy to prepare", "is busy preparing"), D=("feel like, have fun, have difficulty, how about, look forward to", "look forward to hear", "look forward to hearing"),
  E=("be used to, succeed in, there is no point, can't help, be interested in", "succeeded in solve", "succeeded in solving"), F=("keep, thank you for, be busy, spend + 시간, it's no good", "spent two hours to discuss", "spent two hours discussing"))
RV(1, 53, "B", v="수정(내용)", why="정답 ① 확인. 틀린 문장 ①만 길어 길이만 보고 고를 수 있고(C4), worth가 ①(틀림)과 ③(옳음)에 함께 나와 대비 단서가 된다. ③ ‘The museum is worth visiting.’은 원문항 ①과 같다. 밑줄도 원문항(표현 전체)보다 좁다(A3).", fix="옳은 문장 네 개를 원문항 길이의 새 문장으로, 밑줄을 표현 전체로")
RV(1, 53, "CDEF", fx=True, why="수정 예시의 밑줄이 동사 형태에만 있어 원문항(표현 + 동사 형태 전체)과 범위가 달랐다. 원문항처럼 고쳤다.")

X(1, 54, r="avoid, postpone, consider, deny, finish, enjoy, mind, give up 등은 동명사만 목적어로 쓴다. continue, try는 to부정사도 쓸 수 있고, 전치사 뒤에는 동명사를 쓴다.",
  n=["continue는 to부정사를 목적어로 쓸 수 있으므로", "전치사 about 뒤에 동명사 relocating을 바르게 썼으므로", "postpone 뒤에 동명사 voting을 바르게 썼으므로", "avoid는 동명사만 목적어로 쓴다. to avoid being caught로 고쳐야 하므로",
     "try to + 동사원형(~하려고 애쓰다)을 바르게 썼으므로"],
  st="① 문장마다 동사와 그 뒤 목적어의 형태(to부정사인지 -ing인지)를 짝짓는다. → ② {0} → ③ {n}은 {1} 뒤에 to부정사를 썼으므로 동명사({2})로 고쳐야 한다.",
  R=("continue to, think about -ing, postpone -ing, try to는 모두 옳다.", "avoid", "being caught"), B=("consider, avoid, postpone, finish 뒤의 동명사는 모두 옳다.", "deny", "taking"),
  C=("quit, mind, practice, suggest 뒤의 동명사는 모두 옳다.", "avoid", "answering"), D=("enjoy, delay, admit, keep 뒤의 동명사는 모두 옳다.", "consider", "moving"),
  E=("deny, mind, give up, stop 뒤의 동명사는 모두 옳다.", "postpone", "making"), F=("recommend, risk, imagine, miss 뒤의 동명사는 모두 옳다.", "finish", "cleaning"))
RV(1, 54, "B", v="수정(내용)", why="정답 ④ 확인. 문장이 서너 낱말(Tom considered moving. 등)로 원문항(7~10낱말)의 절반 길이라 난이도가 낮다(B4). 사용자가 1-55 B에 준 의견(문장이 짧고 단어 수가 적음)과 같은 문제다.", fix="문장마다 꾸미는 말을 붙여 원문항 길이로")

X(1, 55, r="refuse, hope, decide, promise, agree, expect, plan은 to부정사를, give up, consider, avoid, deny, finish, suggest, appreciate는 동명사를 목적어로 쓴다.",
  pre=["문장별 판정: A. X. refuse는 to부정사를 쓴다(to sign). B. X. give up은 동명사를 쓴다(finding). C. X. consider는 동명사를 쓴다(moving). D. O. hope + to부정사. E. O. appreciate + 동명사(수동형 being invited)."],
  k="틀린 문장은 A, B, C 세 개다.",
  n=["틀린 문장은 A, B, C 세 개이므로"] * 5,
  st="① 밑줄 앞의 동사를 to부정사를 쓰는 동사와 동명사를 쓰는 동사로 나눈다. → ② {0} → ③ 틀린 문장을 세면 {a}이다.",
  R="refuse, hope는 to부정사를, give up, consider, appreciate는 동명사를 쓴다. 따라서 A(refused signing), B(gave up to find), C(considering to move)가 틀렸다.",
  B="decide, promise는 to부정사를, deny, avoid, suggest는 동명사를 쓴다. 따라서 B(avoided to answer), E(promised helping)가 틀렸다.",
  C="agree, promise는 to부정사를, avoid, consider, enjoy는 동명사를 쓴다. 따라서 B(agreed signing)만 틀렸다.",
  D="refuse는 to부정사를, enjoy, postpone, finish는 동명사를 쓴다. regret + 동명사는 ‘~한 것을 후회하다’로 옳다. 따라서 D(finished to paint)만 틀렸다.",
  E="expect, decide는 to부정사를, admit, give up, deny는 동명사를 쓴다. 따라서 A(expects finishing), E(denied to copy)가 틀렸다.",
  F="want, plan은 to부정사를, avoid, finish, consider는 동명사를 쓴다. 따라서 E(planned visiting)만 틀렸다.")

X(1, 56, r="remember + 동명사는 ‘(전에) ~한 것을 기억하다’, remember + to부정사는 ‘(앞으로) ~할 것을 기억하다’라는 뜻이다.",
  n=["will read는 앞으로 읽을 것이라는 뜻이라 우리말과 맞지 않으므로", "remember 뒤에 had read를 바로 이어 쓸 수 없으므로", "주어진 낱말에 없는 now가 들어 있고 뜻도 어색하므로", "remembered to read는 ‘읽을 것을 기억했다’는 뜻이라 우리말과 맞지 않으므로",
     "‘읽은 것을 기억한다’를 remember + 동명사로 바르게 나타냈으므로"],
  st="① 우리말 ‘{0}’은 이미 한 일을 지금 기억한다는 뜻이다. → ② 이미 한 일을 기억할 때는 remember + 동명사를 쓰므로 주어진 동사({1})를 동명사({2})로 바꾼다. remember + to부정사는 ‘앞으로 할 일을 기억하다’라 뜻이 다르다. → ③ remember의 시제를 바꾸거나 낱말을 더한 보기를 지운다. 정답은 {a}",
  R=("읽은 것을 기억한다", "read", "reading"), B=("방문했던 것을 기억한다", "visit", "visiting"), C=("만났던 것을 기억한다", "meet", "meeting"), D=("잠갔던 것을 기억한다", "lock", "locking"),
  E=("말했던 것을 기억한다", "tell", "telling"), F=("봤던 것을 기억한다", "see", "seeing"))

X(1, 57, r="regret + 동명사는 ‘~한 것을 후회하다’라는 뜻이다. 후회하는 때보다 먼저 한 일은 완료동명사(having + 과거분사)로 나타낸다.",
  n=["being forgotten은 수동형이라 ‘그녀가 잊었다’는 뜻을 나타내지 못하므로", "regret + to부정사는 ‘~하게 되어 유감이다’라는 뜻이라 이미 한 일을 후회하는 뜻이 아니므로", "regrets 뒤에 동사원형을 이어 쓸 수 없으므로",
     "후회하기 전에 잊은 일을 완료동명사 having forgotten으로 나타냈으므로", "having 뒤에는 forget이 아니라 과거분사가 와야 하므로"],
  st="① 첫 문장에서 후회하는 것은 지금(regret), 후회하는 일은 과거({0})임을 확인한다. → ② regret 뒤에서 이미 한 일은 동명사로 나타내고, 앞선 때임을 분명히 하려면 having + 과거분사를 쓴다. → ③ to가 붙은 형태, 수동형(being + 과거분사), having + 동사원형을 지운다. 정답은 {a}.",
  R="forgot", B="left", C="ignored", D="missed", E="told", F="made")
RV(1, 57, "BCDEF", fx=True, why="수정 예시의 오답 ‘to have + 과거분사’(to have left 등)는 격식체에서 쓰이기도 해 정답 시비의 여지가 있었다. 분명히 틀린 ‘to + -ing’(to leaving 등)로 바꿨다. 원문항 ①도 같은 이유로 being forgotten으로 고쳤다.")

X(1, 58, r="prevent + 목적어 + from + 동명사는 ‘~가 …하지 못하게 하다’라는 뜻이다. 전치사 from 뒤이므로 동사를 -ing형으로 바꾼다.",
  n=["from이 동사 eat 뒤에 왔고 eat도 동명사가 아니므로", "목적어 their children이 from eating 뒤로 가서 어순이 틀렸으므로", "prevent + their children + from + eating의 어순과 형태가 바르므로", "children 뒤에 to eat을 쓰고 from을 그 뒤에 두어 틀렸으므로",
     "from이 eating 뒤에 와서 어순이 틀렸으므로"],
  st="① 낱말에 prevent와 from이 있으므로 ‘prevent + 목적어 + from + -ing’ 틀을 떠올린다. → ② 우리말에서 하지 못하게 되는 대상({0})을 목적어로, 하지 못하게 되는 행동({1})을 from 뒤에 둔다. from 뒤이므로 동사를 -ing형({2})으로 바꾼다. → ③ 완성하면 {a}",
  R=("their children", "eat junk food", "eating"), B=("dust", "enter the nose", "entering"), C=("students", "use phones", "using"), D=("people", "park here", "parking"), E=("us", "go outside", "going"),
  F=("children", "run onto the road", "running"))

X(1, 59, r="look forward to, object to, when it comes to, be used to, what do you say to의 to는 전치사이므로 뒤에 동명사를 쓴다.",
  pre=["문장별 판정: (A) X. look forward to 뒤에는 hearing을 쓴다. (B) O. object to + 동명사. (C) O. when it comes to + 동명사. (D) X. be used to 뒤에는 living을 쓴다. (E) O. What do you say to + 동명사(~하는 게 어때?)."],
  k="옳은 문장은 (B), (C), (E)이다.",
  n=["옳은 문장 (B), (C), (E)만 모았으므로", "(A), (D)가 틀린 문장이므로", "(D)가 틀린 문장이므로", "(A)가 틀린 문장이므로", "(D)가 틀린 문장이므로"],
  st="① 문장마다 관용 표현 뒤의 동사 형태를 본다. 전치사 to·in·on·from과 be busy, spend + 시간, feel like 뒤에는 동명사가 와야 한다. → ② {0} → ③ 옳은 세 문장만 모은 {a}를 고른다.",
  R="(A) look forward to hear, (D) is used to live는 동사원형을 써서 틀렸다. (B) objected to changing, (C) when it comes to playing, (E) what do you say to taking은 옳다.",
  B="(C) is busy to prepare, (E) from enter가 틀렸다. (A) objected to waiting, (B) are accustomed to working, (D) spent three hours practicing은 옳다.",
  C="(B) got used to drive, (C) the key to succeed가 틀렸다. (A) is devoted to helping, (D) in addition to singing, (E) contributes to saving은 옳다.",
  D="(A) are used to work, (C) looks forward to meet이 틀렸다. (B) insisted on paying, (D) succeeded in solving, (E) feel like taking은 옳다.",
  E="(B) is used to get up, (E) insisted on to pay가 틀렸다. (A) looking forward to seeing, (C) succeeded in passing, (D) feel like eating은 옳다.",
  F="(B) objected to change, (D) looks forward to hear가 틀렸다. (A) is busy preparing, (C) is accustomed to working, (E) feel like going은 옳다.")
RV(1, 59, "BDEF", fx=True, why="수정 예시의 문장이 서너 낱말로 원문항(8~11낱말)의 절반 길이여서 원문항 길이로 늘렸다. E는 네 문장 조합이던 보기 ②도 원문항처럼 세 문장 조합으로 바꿨다.")

X(1, 60, r="be likely to + 동사원형은 ‘~할 것 같다, ~할 가능성이 높다’라는 뜻이다. 이때 to는 전치사가 아니라 to부정사의 to이다.",
  n=["be likely to의 to는 전치사가 아니라 to부정사의 to라서 winning으로 고칠 수 없으므로", "be likely to는 ‘좋아하다’가 아니라 ‘~할 것 같다’라는 뜻이므로", "to는 전치사가 아니고 win도 명사가 아니라 동사원형이므로",
     "가능성·추측의 뜻과, to부정사의 to 뒤에 동사원형이 온다는 점을 바르게 설명했으므로", "미래를 나타내는 말이 있어도 be likely to로 앞일의 가능성을 나타낼 수 있으므로"],
  st="① 밑줄 친 부분을 ‘be likely + to + 동사원형({0})’으로 나눈다. → ② likely는 ‘~할 것 같은’이라는 형용사이고, 뒤의 to는 to부정사의 to라서 동사원형이 왔다. → ③ to를 전치사로 보거나, likely의 뜻을 다르게 풀거나, to부정사의 쓰임을 다르게 설명한 보기를 지운다. 정답은 {n}.",
  R="win", B="reduce", C="arrive", D="rise", E="miss", F="improve")
