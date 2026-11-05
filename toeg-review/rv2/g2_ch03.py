# 2급 CH3 조동사 (21~30) 2차 감수
X(2, 21, r="may는 추측(~일지도 모른다), 허가(~해도 된다), 금지(may not: ~해서는 안 된다), 기원(May ~!)을 나타낸다. 같은 조동사라도 문맥으로 뜻을 가른다.",
  n=["허가를 구하는 May I ~?이므로", "‘들어가서는 안 된다’는 금지의 may not이므로", "‘사용해서는 안 된다’는 금지의 may not이므로", "‘가져가도 된다’는 허가이므로", "‘비가 올지도 모른다’는 추측으로 주어진 문장과 같으므로"],
  st="① 주어진 문장에서 밑줄 친 조동사의 뜻을 정한다. {0} → ② 보기마다 밑줄 친 조동사가 사실을 짐작하는 말인지, 허락·금지·요청·능력·기원을 말하는지 가른다. → ③ {1} 정답은 {n}.",
  R=("참석할 수 있을지 확실하지 않다는 추측이다.", "내일 비가 올지도 모른다는 ⑤만 추측이다. ①은 허가 요청, ②·③은 금지, ④는 허가다."),
  B=("불이 꺼진 것을 보고 자고 있을지도 모른다고 짐작하는 추측이다.", "차가 막혀 늦을지도 모른다는 ④만 추측이다. ①은 허가 요청, ②는 금지, ③은 허가, ⑤는 기원이다."),
  C=("숙제를 끝내면 써도 된다는 허가다.", "일찍 끝낸 사람은 나가도 된다는 ③만 허가다. ①·②·⑤는 추측, ④는 기원이다."),
  D=("전화를 받지 않는 것을 보고 바쁠지도 모른다고 짐작하는 추측이다.", "바람 소리일지도 모른다는 ①만 추측이다. ②·⑤는 과거의 능력, ③·④는 요청이다."),
  E=("일찍 떠난 것을 보고 집에 있을지도 모른다고 짐작하는 추측이다.", "답이 틀렸을지도 모른다는 ⑤만 추측이다. ①은 허가, ②는 허가 요청, ③은 금지, ④는 기원이다."),
  F=("길이 젖은 것을 보고 비가 왔을지도 모른다고 짐작하는 추측이다.", "열쇠가 주머니에 있을지도 모른다는 ②만 추측이다. ①은 허가 요청, ③은 금지, ④는 허가, ⑤는 기원이다."))
RV(2, 21, "F", fx=True, why="수정 예시의 정답 ②만 주어진 문장과 같은 ‘may have + 과거분사’ 꼴이라 형태로 답이 드러났다. 정답을 ‘The keys may be in your coat pocket.’으로 바꿨다.")

X(2, 22, r="used to + 동사원형은 지금은 그렇지 않은 과거의 상태와 과거의 반복 행동을 모두 나타낸다. would는 과거의 반복 행동에만 쓰고 상태에는 쓰지 않는다.",
  n=["may는 과거의 상태나 습관을 나타내지 못하므로", "과거의 상태(There used to be)와 과거의 습관(used to play)을 모두 나타내므로", "should는 과거의 상태나 습관을 나타내지 못하므로", "will은 과거의 상태나 습관을 나타내지 못하므로",
     "would는 과거의 습관에는 쓰지만 첫째 문장 같은 과거의 상태에는 쓰지 않으므로"],
  st="① 두 문장 모두 지금은 그렇지 않은 과거의 일이다. 단서는 {0}. → ② 첫째 문장의 동사({1})는 동작이 아니라 상태다. 과거의 상태에는 would를 쓸 수 없다. → ③ 과거의 상태와 반복 행동을 모두 나타내는 것은 used to뿐이다. {2} 정답은 {n}.",
  R=("but now와 when she was young", "be", "may, should, will은 과거의 일을 나타내지 못한다."),
  B=("but now와 when he was young", "be", "be used to는 ‘~에 익숙하다’는 뜻이라 뒤에 동사원형이 올 수 없다."),
  C=("before the new mall opened와 when she was in elementary school", "be", "be used to는 ‘~에 익숙하다’는 뜻이라 뒤에 동사원형이 올 수 없다."),
  D=("but now와 when we were children", "have", "be used to는 ‘~에 익숙하다’는 뜻이라 뒤에 동사원형이 올 수 없다."),
  E=("but it closed ten years ago와 when we were little", "be", "be used to는 ‘~에 익숙하다’는 뜻이라 뒤에 동사원형이 올 수 없다."),
  F=("but now와 when she was a student", "live", "be used to는 ‘~에 익숙하다’는 뜻이라 뒤에 동사원형이 올 수 없다."))
RV(2, 22, "BCDEF", fx=True, why="수정 예시의 오답 uses to는 영어에 없는 형태라 실제 조동사(should, will, may 등)로 바꿨다. C~F는 문장이 원문항보다 훨씬 짧고 과거임을 알려 주는 말이 없어 would·must 등도 들어갈 수 있었으므로, 원문항처럼 but now ~, when ~을 넣었다.")

X(2, 23, r="'d는 would 또는 had의 줄임말이다. 'd like to(~하고 싶다)의 'd는 would, 'd better(~하는 게 좋겠다)의 'd는 had다.",
  n=["(B)의 'd는 would가 아니라 had이므로", "would like to, had better이므로", "(A)는 would, (B)는 had인데 서로 바뀌었으므로", "(A)의 'd는 had가 아니라 would이므로", "(B)의 'd는 should가 아니라 had이므로"],
  st="① (A)에서 'd 뒤에 오는 말({0})을 본다. ‘~하고 싶다’, ‘~을 원하다’는 뜻의 would like(love)다. → ② (B)에서는 'd 뒤에 better + 동사원형({1})이 온다. ‘~하는 게 좋겠다’는 had better다. would better, should better라는 표현은 없다. → ③ 정답은 {n}.",
  R=("like to visit", "better finish"), B=("like to stay", "better bring"), C=("like some hot tea", "better apologize"), D=("love to join", "better hurry"), E=("like to walk", "better call"), F=("like to leave", "better check"))
RV(2, 23, "CE", v="수정(내용)", why="정답 확인. 다만 두 문장이 원문항(9단어·8단어)의 절반 이하로 짧고, Tom'd·Jane'd처럼 고유명사 뒤에 'd를 붙인 축약은 글에서 어색하다.", fix="문장 길이를 원문항 수준으로, 주어는 대명사로")
RV(2, 23, "D", v="수정(내용)", why="정답 확인. 다만 두 문장(‘We'd love to join you.’, ‘You'd better hurry.’)이 원문항(9단어·8단어)의 절반 이하로 짧다.", fix="문장 길이를 원문항 수준으로")

X(2, 24, r="cannot(can't) be ~는 ‘~일 리가 없다’는 강한 부정의 추측이다. must be ~(~임이 틀림없다)의 반대다.",
  n=["‘아마 사실일 것이다’는 긍정의 추측이라 뜻이 반대이므로", "cannot be true는 ‘사실일 리가 없다’는 강한 부정의 추측이므로", "‘~일지도 모른다’는 may의 뜻이므로", "소망을 나타내는 표현이 아니므로", "가능성을 인정하는 뜻이 아니므로"],
  st="① 밑줄 문장의 can't(cannot) be는 ‘~할 수 없다’는 능력이 아니라 추측이다. 화자는 상대가 전한 말({0})을 믿지 않는다. → ② can't be ~는 ‘~일 리가 없다’는 강한 부정의 추측이다. → ③ ‘틀림없다’, ‘~일지도 모른다’, 소망·금지로 옮긴 보기를 지운다. 정답은 {n}.",
  R="어제까지 아르바이트를 구하던 Jack이 복권에 당첨되어 저택을 샀다", B="외계인을 만났다", C="10분 만에 500쪽을 읽었다", D="빈집에 사람이 가득하다", E="해가 서쪽에서 떴다", F="전혀 잠을 자지 않는다")

X(2, 25, r="조동사 뒤에는 동사원형을 쓰고, 조동사 둘을 나란히 쓸 수 없다(will can → will be able to). do/does/did 의문문에서도 동사는 원형이다(Did she have to ~?).",
  pre=["문장별 판정: ⓐ O. might + 동사원형. ⓑ X. Will 뒤에는 원형이 와야 하므로 Will you be able to. ⓒ O. shouldn't + 동사원형. ⓓ O. be going to의 부정. ⓔ O. had to + 동사원형. ⓕ X. Did 뒤에는 원형이 와야 하므로 Did she have to."],
  n=["ⓐ는 옳은 문장이므로", "ⓓ는 옳은 문장이므로", "ⓑ와 ⓕ 모두 틀린 문장이므로", "ⓒ와 ⓓ 모두 옳은 문장이므로", "ⓒ는 옳은 문장이므로"],
  st="① 밑줄마다 조동사 뒤의 형태를 본다. 조동사와 do/does/did 뒤의 동사는 원형이고, 조동사 둘을 나란히 쓸 수 없다. → ② 틀린 곳을 찾는다: {0}. → ③ 틀린 두 문장을 묶은 {a}가 정답이다.",
  R="ⓑ는 Will 뒤에 are able to를 썼고(be able to), ⓕ는 Did 뒤에 had를 썼다(have)", B="ⓑ는 must 뒤에 finishes를 썼고(finish), ⓓ는 Do와 can을 함께 썼다(Can you swim)", C="ⓒ는 will과 can을 나란히 썼고(will be able to), ⓔ는 Does 뒤에 has to를 썼다(have to)",
  D="ⓑ는 has to 뒤에 leaves를 썼고(leave), ⓔ는 be going to 뒤에 moving을 썼다(move)", E="ⓐ는 Did와 could를 함께 썼고(Could you find), ⓓ는 should 뒤에 to call을 썼다(call)", F="ⓓ는 had to 뒤에 returned를 썼고(return), ⓔ는 will 뒤에 be를 빠뜨렸다(will be able to)")

X(2, 26, r="had better + 동사원형은 ‘~하는 게 좋겠다’는 충고다. had는 주어나 시제에 따라 바뀌지 않고, 부정은 had better not + 동사원형이다.",
  n=["had better + 동사원형의 바른 형태이므로", "have to와 better를 섞은 없는 표현이므로", "had와 better의 순서가 뒤바뀌었으므로", "had를 have로 바꿔 쓸 수 없으므로", "had to와 better를 섞은 없는 표현이므로"],
  st="① 앞 문장({0})을 보면 빈칸은 ‘~하는 게 좋겠다’는 충고다. → ② 이 뜻의 표현은 had better + 동사원형이다. had는 주어나 시제에 따라 바뀌지 않고, 순서를 바꾸거나 to를 붙일 수 없다. {1} → ③ 정답은 {n}.",
  R=("It's raining outside.", "have better, better had, have(had) to better는 모두 없는 형태다."), B=("The sidewalks are icy.", "has better, had better to, better had, have to better는 모두 틀린 형태다."),
  C=("You look exhausted.", "had to better, have better, better had to, having better는 모두 틀린 형태다."), D=("The deadline is tomorrow.", "better have, has to better, have better to, had better to는 모두 틀린 형태다."),
  E="① 앞 문장(That dog looks angry.)을 보면 빈칸은 ‘가까이 가지 않는 게 좋겠다’는 부정의 충고다. → ② had better의 부정은 had better not + 동사원형이다. not을 앞에 두거나(had not better, not had better) don't, not to를 쓸 수 없고, had를 have로 바꿀 수도 없다. → ③ 정답은 {n}.",
  F=("The last bus leaves soon.", "would better, should better라는 표현은 없고, had better to, better had도 틀린 형태다."))
RV(2, 26, "DE", fx=True, why="수정 예시의 오답 had not better는 일부 영어에서 쓰이기도 하는 형태라, 확실히 틀린 형태(D: have better to, E: had better not to)로 바꿨다.")

X(2, 27, r="동사를 강조할 때는 do/does/did + 동사원형을 쓴다. 시제와 인칭은 do가 나타내고 뒤의 동사는 원형이다.",
  n=["did + 동사원형 clean으로 과거의 동작을 바르게 강조했으므로", "did 뒤에 과거형 cleaned를 쓸 수 없으므로", "yesterday가 있는 과거 문장에 does를 쓸 수 없으므로", "did 뒤에 -ing를 쓸 수 없으므로", "did는 동사 앞에 두어야 하므로"],
  st="① 원래 문장의 동사({0})에서 시제와 주어를 확인한다. {1} → ② do/does/did를 동사 앞에 두고 동사는 원형({2})으로 바꾼다. → ③ 시제가 달라졌거나 동사가 원형이 아닌 보기를 지운다. 정답은 {n}.",
  R=("cleaned", "과거형이므로 did를 쓴다.", "clean"), B=("finished", "과거형이므로 did를 쓴다.", "finish"), C=("called", "과거형이므로 did를 쓴다.", "call"), D=("solve", "현재형이고 주어가 They이므로 do를 쓴다.", "solve"),
  E=("understands", "현재형이고 주어가 3인칭 단수(Jane)이므로 does를 쓴다.", "understand"), F=("want", "현재형이고 주어가 I이므로 do를 쓴다.", "want"))

X(2, 28, r="must에는 과거형이 없어 과거의 의무는 had to로 나타낸다. 의문문은 Did + 주어 + have to ~?, 부정문은 didn't have to(~할 필요가 없었다)다.",
  n=["didn't have to(~할 필요가 없었다)로 올바르므로", "Did + 주어 + have to ~? 의문문으로 올바르므로", "must에는 과거형 musted가 없다. had to로 써야 하므로", "had to로 과거의 의무를 바르게 나타냈으므로", "did you have to로 올바르므로"],
  st="① 문장마다 조동사와 그 뒤의 동사 형태를 본다. 조동사에는 -s, -ed가 붙지 않고, 뒤에는 to 없는 동사원형이 온다. → ② 과거의 의무는 must가 아니라 had to로 나타낸다. → ③ {n}은 {0}.",
  R="must에 -ed를 붙였다. had to study가 맞다", B="must에 -ed를 붙였다. had to leave가 맞다", C="must 뒤에 to를 썼다. must finish가 맞다", D="may 뒤에 to를 썼다. may come이 맞다",
  E="should 뒤에 studies를 썼다. should study가 맞다", F="could 뒤에 과거형 went를 썼다. could go가 맞다")

X(2, 29, r="would는 과거에 반복한 동작(~하곤 했다)에만 쓴다. ‘~이 있었다’, ‘~이었다’ 같은 과거의 상태는 used to로 나타낸다.",
  n=["would와 used to는 규칙적인지 불규칙적인지로 나뉘지 않으므로", "used to는 과거완료가 아니고 명사의 수와도 관계없으므로", "두 표현이 현재와의 관련성으로 나뉘는 것은 아니므로", "would가 반드시 빈도부사와 함께 쓰여야 하는 것은 아니므로",
     "would는 과거의 반복 동작에만 쓰고 과거의 상태에는 쓸 수 없다는 점을 바르게 설명했으므로"],
  st="① ⒜ 문장의 동사({0})가 반복한 동작인지, 이어진 상태인지 본다. {1} 것은 상태다. → ② would는 과거에 반복한 동작에만 쓰고, 과거의 상태에는 used to를 쓴다. → ③ ‘동작이 아니라 상태라서’라는 이유를 댄 {n}을 고른다.",
  R=("be", "서점이 ‘있었다’는"), B=("be", "분수대가 ‘있었다’는"), C=("have", "정류장이 하나뿐‘이었다’는"), D=("be", "어릴 때 수줍음을 ‘탔다’는"), E=("be", "길이 더 ‘좁았다’는"), F=("stand", "나무가 ‘서 있었다’는"))

X(2, 30, r="used to + 동사원형은 ‘~하곤 했다’(과거의 습관·상태), be used to + 동사원형은 ‘~하는 데 사용되다’(수동태 + 목적), be used to + (동)명사는 ‘~에 익숙하다’다.",
  n=["(A)의 used to + 동사원형은 지금은 하지 않는 과거의 습관을 나타내 옳은 설명이므로", "(B)는 use의 수동태(be used)라 옳은 설명이므로", "(C)의 be used to에서 to는 전치사라 옳은 설명이므로", "(A)는 ‘치곤 했다’, (C)는 ‘치는 데 익숙하다’로 뜻이 다르므로",
     "(B)의 to play는 ‘연주하기 위해’라는 목적을 나타내 옳은 설명이므로"],
  st="① 세 문장의 구조를 가른다. (A) used to + 동사원형은 ‘~하곤 했다’, (B) be used to + 동사원형은 ‘~하는 데 사용되다’, (C) be used to + -ing는 ‘~에 익숙하다’다. → ② 학생마다 어느 문장을 두고 말하는지 찾아 위 뜻·형태와 견준다. → ③ {n}은 {0}.",
  R="(A)와 (C)의 뜻이 같다고 했다. (C)는 ‘익숙하다’는 뜻이다", B="(B)를 ‘익숙하다’로 풀었다. (B)는 ‘사용된다’는 뜻이다", C="(C)의 working을 work로 바꿔도 된다고 했다. to가 전치사라 -ing만 온다",
  D="(B)의 used를 과거형으로 보았다. is used는 현재 시제의 수동태다", E="(C)에서 be동사를 빼도 뜻이 같다고 했다. be동사를 빼면 틀린 문장이 된다", F="(B)를 is used to making으로 바꿔도 된다고 했다. 그러면 ‘익숙하다’는 뜻이 되어 버린다")
