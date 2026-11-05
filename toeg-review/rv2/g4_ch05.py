# 4급 CH5 시제Ⅱ (41~50) 2차 감수
X(4, 41, r="will의 부정은 will not + 동사원형, be going to의 부정은 be동사 + not + going to + 동사원형이다.",
  n=["not은 will 앞이 아니라 뒤에 오므로", "will 뒤, 동사원형 bake 앞에 not을 넣어 will not bake가 되므로", "동사 bake 뒤에는 not을 넣을 수 없으므로", "목적어 a pie 뒤에는 not을 넣을 수 없으므로", "문장 끝에는 not을 넣을 수 없으므로"],
  st="① 미래의 부정문을 만든다. will이 있으면 will 바로 뒤에, be going to이면 be동사 바로 뒤에 not을 넣는다. → ② {0} → ③ 정답은 {n}.",
  R="will 뒤, bake 앞이 not의 자리다: will not bake.", B="be going to 문장이므로 be동사 뒤에 not을 넣는다: is not going (to visit).", C="will 뒤에 not을 넣고 동사원형을 쓴다: will not cook.", D="will 뒤에 not을 넣고 동사원형을 쓴다: will not be.",
  E="be going to 문장이므로 be동사 뒤에 not을 넣는다: is not going (to study).", F="be going to 문장이므로 be동사 뒤에 not을 넣는다: are not going (to leave).")

X(4, 42, r="be going to의 부정문은 be동사 바로 뒤에 not을 넣는다: be + not + going to + 동사원형.",
  n=["be동사 is가 빠졌으므로", "be going to는 does로 부정하지 않으므로", "be동사 is 뒤에 not을 바르게 넣었으므로", "will과 be going to를 겹쳐 쓸 수 없으므로", "going을 go로 바꿀 수 없으므로"],
  st="① be going to 문장의 부정은 be동사({0}) 바로 뒤에 not을 넣는다. → ② 나머지(going to + 동사원형)는 그대로 둔다: {1}. → ③ 정답은 {n}.",
  R=("is", "is not going to study"), B=("is", "is not going to visit"), C=("is", "is not going to study"), D=("are", "are not going to play"), E=("am", "am not going to buy"), F=("are", "are not going to leave"))
RV(4, 42, "BDEF", v="수정(내용)", why="정답 확인. 다만 오답 하나는 부정문으로 바꾸지 않은 원래 문장 그대로여서 발문만 보고 지워지고, 또 하나는 옳은 축약형(isn't going to 등)이라 발문의 조건으로 걸러야 한다(E의 amn't는 없는 형태). 원문항의 오답은 모두 not을 잘못 쓴 문장이다. 정답 위치도 D·E·F가 원문항과 같은 ③이다.", fix="오답을 not을 잘못 쓴 문장으로, 원문항 발문으로, 정답 위치를 달리")
RV(4, 42, "C", fx=True, why="수정 예시의 오답 하나가 부정문으로 바꾸지 않은 원래 문장 그대로여서 발문만 보고 지워졌다. 원문항처럼 not을 잘못 쓴 문장(will is not going to)으로 바꿨다.")

X(4, 43, r="be going to + 동사원형은 ‘~할 것이다’라는 미래 표현이다. be going to + 장소는 go의 진행형으로 ‘~에 가고 있다’는 뜻이다.",
  n=["to 뒤에 동사원형 see가 와서 미래를 나타내므로", "to 뒤에 동사원형 cook이 와서 미래를 나타내므로", "to 뒤에 동사원형 travel이 와서 미래를 나타내므로", "to 뒤에 장소 the park가 와서 ‘가고 있다’는 현재진행이므로", "to 뒤에 동사원형 call이 와서 미래를 나타내므로"],
  st="① going to 바로 뒤를 본다. 동사원형이면 미래 표현, 명사(장소)이면 ‘~에 가고 있다’는 진행형이다. → ② {0} → ③ 정답은 {n}.",
  R="④만 to 뒤에 장소 the park가 온다. now도 지금 하고 있는 일임을 알려 준다.", B="④만 to 뒤에 장소 the park가 온다.", C="⑤만 to 뒤에 장소 school이 온다.", D="⑤만 to 뒤에 장소 Busan이 온다.", E="②만 to 뒤에 장소 the library가 온다.",
  F="②만 to 뒤에 장소 the store가 온다.")

X(4, 44, r="will + 동사원형, be동사 + going to + 동사원형. when·after처럼 때를 나타내는 절에서는 미래의 일도 현재형으로 쓴다.",
  n=["will + 동사원형 call이고 when절에 현재형 arrive를 썼으므로", "be동사 is가 빠졌으므로", "will 뒤에 과거형 finished를 쓸 수 없으므로", "going to 뒤에 -ing형을 쓸 수 없으므로", "will 뒤에 going을 쓸 수 없으므로"],
  st="① 미래 표현의 꼴을 확인한다: will + 동사원형, be동사 + going to + 동사원형. → ② when·after가 이끄는 절은 미래의 일이라도 현재형으로 쓴다. → ③ {0} 정답은 {n}.",
  R="①만 will call + when I arrive로 맞다.", B="②만 after절에 현재형 finish를 써서 맞다. 나머지는 when·after절에 will을 썼다.", C="①만 when절에 현재형 arrive를 써서 맞다.", D="②만 when절에 현재형 gets를 써서 맞다.",
  E="⑤만 when절에 현재형 stops를 써서 맞다.", F="④만 when절에 현재형 comes를 써서 맞다.")

X(4, 45, r="will + 동사원형(부정은 will not). will에는 -s를 붙이지 않는다. be going to + 동사원형.",
  pre=["문장별 판정: ⓐ X. not은 will 뒤에 온다(will not snow). ⓑ O. be going to + 동사원형. ⓒ X. will에는 -s를 붙이지 않는다. ⓓ O. be going to 의문문. ⓔ X. will 뒤에는 동사원형 build."],
  k="옳은 문장은 ⓑ, ⓓ 두 개다.", n=["옳은 문장은 ⓑ, ⓓ 두 개이므로"] * 5,
  st="① will 문장은 세 가지를 본다: will에 -s가 없는지, 뒤가 동사원형인지, not이 will 뒤에 있는지. → ② be going to 문장은 be동사가 있는지, to 뒤가 동사원형인지 본다. → ③ {0} 옳은 문장은 {a}이다.",
  R="ⓐ not will(will not), ⓒ wills(will), ⓔ He'll builds(build)가 틀렸다. ⓑ, ⓓ만 옳다.", B="d won't studies(study)만 틀렸다.", C="a not will(will not), c wills(will)가 틀렸다. b, d, e는 옳다.",
  D="b Tom going to(is going to), e Does she going to(Is she going to)가 틀렸다.", E="c won't goes(go)만 틀렸다.", F="c wills(will)만 틀렸다.")
RV(4, 45, "E", fx=True, why="수정 예시가 ⓒ를 옳은 문장으로 바꿔 틀린 문장이 하나도 없는 5개가 되어 있었다. ⓒ를 원래의 틀린 문장(won't goes)으로 되돌려 4개로 했다.")
RV(4, 45, "F", fx=True, why="수정 예시의 정답이 원문항과 같은 2개(②)여서, ⓔ를 옳은 문장으로 되돌려 3개로 했다.")

X(4, 46, r="will 뒤에는 주어가 무엇이든 동사원형을 쓴다.",
  n=["will 뒤에 -s가 붙은 형태를 쓸 수 없으므로", "will 뒤에 -ing형을 쓸 수 없으므로", "will 뒤에는 is가 아니라 be를 쓰고, at home 앞에 stay도 필요하므로", "be와 stay를 함께 쓸 수 없으므로", "will + 동사원형 stay로 알맞으므로"],
  st="① 조동사 will 뒤에는 주어가 무엇이든 동사원형이 온다. → ② {0} → ③ 정답은 {a}.",
  R="주어가 She여도 stays가 아니라 stay다.", B="will buy다. to나 -s를 붙이지 않는다.", C="주어가 She여도 will stay다.", D="주어가 Tom이어도 will visit이다.", E="will play다. to나 -s를 붙이지 않는다.", F="will leave다. to나 -s를 붙이지 않는다.")

X(4, 47, r="will 의문문의 어순: Will + 주어 + 동사원형 ~?",
  n=["dinner는 주어라 둘째에 오므로", "will은 맨 앞에 오므로", "be는 셋째에 오므로", "Will dinner be ready soon?에서 넷째는 ready이므로", "soon은 맨 끝에 오므로"],
  st="① 의문문이므로 Will을 맨 앞에 둔다. → ② 그 뒤에 주어 + 동사원형 + 나머지를 놓는다: {0} → ③ 넷째 단어는 {a}.",
  R="Will / dinner / be / ready / soon?", B="Will / Tom / come / home / tonight?", C="Will / Jane / be / ready / tomorrow?", D="Will / they / play / soccer / tomorrow?", E="Will / Jane / buy / a / bag?", F="Will / we / leave / home / early?")

X(4, 48, r="be going to 의문문은 주어에 맞는 be동사를 문장 앞에 둔다: Am I ~?, Is he/she/it ~?, Are you/we/they ~?",
  pre=["문장별 판정: (가) O. 주어 I에 Am. (나) X. 주어 they에는 Are. (다) X. 주어 she에는 Is. (라) O. 주어 it에 Is."],
  n=["(나)가 틀렸으므로", "(나), (다)가 모두 틀렸으므로", "(다)가 틀렸으므로", "(나)가 틀렸으므로", "(가)와 (라)가 모두 옳으므로"],
  st="① be going to 의문문은 be동사로 시작한다. 문장마다 맨 앞 be동사와 주어를 짝지어 본다(I - Am, 단수 - Is, you·복수 - Are). → ② {0} → ③ 옳은 문장만 고른 {a}가 정답이다.",
  R="(나) Is they(Are they), (다) Are she(Is she)가 틀렸다.", B="(다) Am we(Are we), (라) Is you(Are you)가 틀렸다.", C="(나) Is they(Are they), (다) Are she(Is she)가 틀렸다.", D="(다) Is they(Are they), (라) Are Jane(Is Jane)이 틀렸다.",
  E="(다) Is we(Are we), (라) Are Tom(Is Tom)이 틀렸다.", F="(다) Am you(Are you), (라) Is the boys(Are the boys)가 틀렸다.")
RV(4, 48, "DEF", fx=True, why="B·D·E·F의 정답이 모두 (가), (나)로 같은데 수정 예시가 그대로 두었다. D·E·F는 문장 순서를 바꿔 정답 조합을 (나), (라) / (나), (다) / (다), (라)로 달리했다.")

X(4, 49, r="be going to + 동사원형: to 뒤에는 동사원형이 온다.",
  n=["주어의 인칭은 -ing형을 쓰는지와 관계가 없으므로", "가까운 미래의 일에도 진행형을 쓸 수 있어 이유가 되지 않으므로", "isn't 뒤에 going이 왔듯이 부정어 뒤에 동사원형만 오는 것은 아니므로", "visit은 -ing형으로도 쓰이므로", "be going to의 to 뒤에는 동사원형이 와야 하므로"],
  st="① 밑줄 바로 앞을 본다: be going to의 to다. → ② ‘be going to + 동사원형’이 ‘~할 것이다’라는 미래 표현이다. to 뒤라서 {0}. → ③ 이 이유를 말한 것은 {n}.",
  R="visiting이 아니라 visit을 쓴다", B="studying이 아니라 study를 쓴다", C="visiting이 아니라 visit을 쓴다", D="playing이 아니라 play를 쓴다", E="buying이 아니라 buy를 쓴다", F="leaving이 아니라 leave를 쓴다")

X(4, 50, r="be going to + 동사원형. 부정은 be동사 + not + going to, 의문은 be동사 + 주어 + going to ~?",
  pre=["문장별 판정: (A) X. going to 뒤에는 동사원형 meet. (B) O. be going to 의문문. (C) X. not은 be동사 뒤에 온다(are not going to). (D) O. be going to + 동사원형 go. (E) O. be going to 의문문."],
  n=["(A), (C)가 틀렸으므로", "(C)가 틀렸으므로", "(A)가 틀렸으므로", "(B), (D), (E)가 모두 옳으므로", "(C)가 틀렸으므로"],
  st="① be going to 문장은 be동사가 있는지, not이 be동사 바로 뒤에 있는지, to 뒤가 동사원형인지 본다. will 문장은 will + 동사원형인지 본다. → ② {0} → ③ 옳은 문장만 묶은 {a}가 정답이다.",
  R="(A) to meeting(to meet), (C) going to not(not going to)이 틀렸다.", B="(C) We going to(are going to), (E) won't goes(go)가 틀렸다.", C="(A) to meeting(to meet), (C) will goes(go)가 틀렸다.", D="(C) will playing(play), (E) Are Tom(Is Tom)이 틀렸다.",
  E="(C) won't studies(study)만 틀렸다.", F="(D) wills(will)만 틀렸다.")
RV(4, 50, "BCDF", fx=True, why="수정 예시의 문장이 서너 낱말뿐이라 원문항(여덟 낱말 안팎)의 절반 길이였다. 문장을 원문항 길이에 가깝게 늘렸다.")
RV(4, 50, "E", fx=True, why="수정 예시의 문장이 서너 낱말뿐이라 원문항의 절반 길이였고, (D)(Are you going to help?)는 원문항 (E)와 닮아 있었다. 문장을 늘리고 (D)를 다른 문장으로 바꿨다.")
