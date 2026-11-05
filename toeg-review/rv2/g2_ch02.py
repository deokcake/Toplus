# 2급 CH2 시제 (11~20) 2차 감수
X(2, 11, r="yesterday처럼 끝난 과거 시점에는 과거형을 쓰고, since ~처럼 과거부터 지금까지 이어지는 기간에는 현재완료(have/has + 과거분사)를 쓴다.",
  n=["since last summer와 과거형 saw를 함께 쓸 수 없으므로", "yesterday에는 과거형 met, since last summer에는 현재완료 haven't seen을 쓰므로", "since last summer와 과거형 didn't see를 함께 쓸 수 없으므로", "yesterday와 현재완료 have met을 함께 쓸 수 없으므로",
     "yesterday와 현재완료 have met을 함께 쓸 수 없으므로"],
  st="① 첫째 빈칸 문장의 시간 표현({0})은 끝난 과거 시점이다. 과거형({1})을 쓰고 현재완료는 쓸 수 없다. → ② 둘째 빈칸 문장의 시간 표현({2})은 과거부터 지금까지 이어지는 기간이다. 현재완료({3})를 쓴다. → ③ 정답은 {n}.",
  R=("yesterday", "met", "since last summer", "haven't seen"), B=("last Monday", "ran into", "since last winter", "haven't talked to"), C=("yesterday", "lost", "since middle school", "has used"),
  D=("last April", "visited", "since I moved here", "have been"), E=("last month", "started", "for four weeks now", "has worked"), F=("during the last vacation", "finished", "since I was in middle school", "have loved"))
RV(2, 11, "BCDEF", v="수정(내용)", why="정답 확인. 다만 오답이 haven't talk, has use, have was, has work, haven't reading처럼 없는 형태이거나 주어와 수가 맞지 않아(I hasn't, She have) 시제를 따지지 않고도 지워진다. 원문항의 오답은 모두 형태가 바르고 시제만 틀린 것(saw, didn't see, have met)이다.", fix="오답을 형태는 바르고 시제만 틀린 것으로")

X(2, 12, r="현재완료의 계속 용법에서 for 뒤에는 기간(25 years)을, since 뒤에는 시작 시점(명사나 절)을 쓴다.",
  n=["25 years는 기간이라 since를 쓸 수 없으므로", "she was 11 years old는 시작 시점이라 for를 쓸 수 없으므로", "기간(25 years) 앞에 for, 시작 시점(she was 11 years old) 앞에 since를 썼으므로", "for와 since가 서로 바뀌었으므로", "현재완료의 시작 시점은 when이 아니라 since로 나타내므로"],
  st="① 빈칸 뒤의 말이 ‘얼마 동안’(기간)인지 ‘언제부터’(시작 시점)인지 가른다. → ② (A) 뒤의 {0}, (B) 뒤의 {1}. → ③ 기간 앞에는 for, 시작 시점 앞에는 since를 쓴다. 정답은 {n}.",
  R=("25 years는 기간이다", "she was 11 years old는 시작 시점이다"), B=("1998은 시작 시점이다", "more than a decade는 기간이다"), C=("2022는 시작 시점이다", "six years는 기간이다"), D=("two hours는 기간이다", "last spring은 시작 시점이다"),
  E=("five years는 기간이다", "she was a child는 시작 시점이다"), F=("8 a.m.은 시작 시점이다", "a long time은 기간이다"))

X(2, 13, r="완료 시제는 have/has/had + 과거분사로 쓴다. 불규칙동사는 과거형과 과거분사가 다를 수 있다(break - broke - broken).",
  n=["become의 과거분사 become을 바르게 썼으므로", "make의 과거분사 made를 바르게 썼으므로", "feel의 과거분사 felt를 바르게 썼으므로", "have 뒤에 과거형 broke를 썼다. 과거분사 broken으로 고쳐야 하므로", "see의 과거분사 seen을 바르게 썼으므로"],
  st="① 밑줄은 모두 have/has/had 뒤, 곧 과거분사 자리다. → ② 밑줄 친 동사의 ‘원형 - 과거형 - 과거분사’를 떠올려 과거분사가 맞는지 본다. 과거형과 과거분사가 다른 불규칙동사가 함정이다. → ③ {n}의 {0}.",
  R="broke는 과거형이다. break - broke - broken이므로 broken이 맞다", B="winned는 없는 형태다. win - won - won이므로 won이 맞다", C="wrote는 과거형이다. write - wrote - written이므로 written이 맞다",
  D="gave는 과거형이다. give - gave - given이므로 given이 맞다", E="took은 과거형이다. take - took - taken이므로 taken이 맞다", F="chose는 과거형이다. choose - chose - chosen이므로 chosen이 맞다")

X(2, 14, r="현재완료는 ago, yesterday, last night처럼 끝난 과거 시점을 나타내는 말과 함께 쓸 수 없다. When did ~?에 대한 대답도 과거형으로 한다.",
  n=["경험을 현재완료로 묻고 답해 올바르므로", "지금까지의 기간을 현재완료와 for로 묻고 답해 올바르므로", "지금 하는 일을 현재진행형으로 묻고 답해 올바르므로", "an hour ago라는 과거 시점과 현재완료를 함께 쓸 수 없다. I finished it an hour ago.로 써야 하므로", "앞으로의 일을 will로 묻고 답해 올바르므로"],
  st="① 대화마다 A가 묻는 시제와 B가 답하는 시제가 맞는지, 대답 속 시간 표현과 어울리는지 본다. → ② 대답에 ago, yesterday, last night 같은 끝난 과거 시점이 있으면 과거형이어야 한다. → ③ {n}의 B는 과거 시점 표현({0})이 있는데 현재완료({1})를 썼다. 과거형({2})이 맞다.",
  R=("an hour ago", "have finished", "finished"), B=("two hours ago", "have submitted", "submitted"), C=("at noon", "has left", "left"), D=("last night", "have seen", "saw"), E=("yesterday", "has called", "called"), F=("on Monday", "have arrived", "arrived"))
RV(2, 14, "BCDEF", v="수정(내용)", why="정답 확인. 다만 오답 대화의 대답이 ‘At nine.’, ‘Yes.’, ‘For years.’ 같은 토막이라 시제를 따질 수 있는 완전한 문장 대답이 사실상 정답뿐이어서 답이 드러난다(C4). 원문항은 다섯 대화 모두 완전한 문장으로 대답한다. 대화도 원문항(한 줄)과 달리 두 줄로 나뉘어 있다.", fix="모든 대답을 완전한 문장으로, 대화는 한 줄로")

X(2, 15, r="be going to는 ‘be동사 + going’, will 뒤에는 동사원형을 쓴다. 현재완료는 경험·계속을 나타내며 when I was ~ 같은 끝난 과거 시점과 함께 쓰지 않는다.",
  pre=["문장별 판정: a) X. Are you going으로 써야 한다. b) O. 경험의 현재완료. c) O. 도착한 것보다 먼저 떠났으므로 과거완료. d) X. will 뒤에는 동사원형 attend. e) O. since와 함께 쓴 현재완료. f) X. when I was in high school은 과거 시점이라 met을 쓴다."],
  k="옳은 문장은 b), c), e) 세 개다.", n=["옳은 문장은 b), c), e) 세 개이므로"] * 5,
  st="① 밑줄마다 시간 표현과 동사 형태를 견준다. will 뒤는 동사원형이고, 끝난 과거 시점에는 과거형을 쓴다. → ② {0} → ③ 옳은 문장을 세면 {a}이다.",
  R="a)는 Are ~ go가 틀렸고(going), d)는 will attends가 틀렸으며(attend), f)는 과거 시점(when I was in high school)에 현재완료를 썼다(met). b), c), e)가 옳다.",
  B="d)는 will goes가 틀렸고(go), f)는 yesterday에 현재완료를 썼다(arrived). 나머지 넷이 옳다.", C="d)는 will studies가 틀렸고(study), f)는 last night에 현재완료를 썼다(called). 나머지 넷이 옳다.",
  D="e)만 틀렸다. 주어 They에는 has가 아니라 have를 쓴다. 나머지 다섯이 옳다.", E="d)만 틀렸다. will 뒤에는 동사원형 come을 쓴다. 나머지 다섯이 옳다.", F="f)만 틀렸다. yesterday에는 현재완료가 아니라 과거형 met을 쓴다. 나머지 다섯이 옳다.")

X(2, 16, r="love, know, believe, own, need, resemble처럼 감정·인식·소유·상태를 나타내는 동사는 진행형으로 쓰지 않고 단순현재로 쓴다.",
  n=["am loved는 ‘사랑받는다’는 수동태라 뜻이 달라지므로", "상태 동사 love를 단순현재로 쓰고 주어 I에도 맞으므로", "be동사 없이 loving만으로는 동사가 될 수 없으므로", "be동사와 동사원형을 함께 쓸 수 없으므로", "주어 I에 loves를 쓸 수 없으므로"],
  st="① 밑줄의 동사({0})가 동작인지 상태인지 본다. ‘{1}’는 상태를 나타내므로 진행형으로 쓰지 않는다. → ② 진행형을 단순현재로 고친다. be동사 + 동사원형, 수동태, -ing만 남긴 보기는 지운다. → ③ 주어({2})에 수를 맞추면 {a}이다.",
  R=("love", "좋아하다", "I"), B=("know", "알다", "I"), C=("believe", "믿다", "She"), D=("own", "소유하다", "We"), E=("resemble", "닮다", "Tom"), F=("need", "필요하다", "They"))

X(2, 17, r="지각동사(see, hear, watch) + 목적어 + 현재분사를 수동태로 바꾸면 ‘be동사 + 과거분사 + 현재분사’가 된다. 현재분사는 그대로 남는다.",
  n=["were seeing은 능동 진행형이고 play도 쓸 수 없으므로", "saw가 과거이므로 are가 아니라 were를 써야 하고 played도 쓸 수 없으므로", "were seen 뒤에 현재분사 playing을 그대로 두어 바르게 바꿨으므로", "지각동사의 과거분사 seen이 빠졌으므로", "be동사의 과거형 없이 been으로 시작할 수 없으므로"],
  st="① 능동태의 목적어({0})가 주어가 되었으므로 동사는 ‘be동사 + 과거분사’다. 능동태 동사({1})가 과거형이므로 be동사도 과거형으로 쓴다({2}). → ② 목적격 보어였던 현재분사({3})는 바꾸지 않고 그대로 뒤에 둔다. → ③ 정답은 {a}.",
  R=("the children", "saw", "were seen", "playing"), B=("the singer", "heard", "was heard", "practicing"), C=("a man", "saw", "was seen", "crossing"), D=("the children", "watched", "were watched", "dancing"),
  E=("the baby", "heard", "was heard", "crying"), F=("two students", "saw", "were seen", "running"))

X(2, 18, r="when, after, until, if, unless가 이끄는 시간·조건의 부사절에서는 미래의 일도 현재형으로 쓴다.",
  pre=["문장별 판정: (A) O. 시간 부사절(when)에서 현재형 see. (B) X. 조건 부사절이므로 will be → is. (C) O. 조건 부사절(if)에서 현재형 is. (D) X. 시간 부사절이므로 will be → is."],
  n=["(B)가 틀렸으므로", "(B)가 틀렸으므로", "(A)와 (C)만 부사절에 현재형을 바르게 썼으므로", "(B)와 (D) 모두 틀렸으므로", "(D)가 틀렸으므로"],
  st="① 밑줄은 모두 when, if, after, until, unless가 이끄는 부사절 안의 동사다. → ② 시간·조건의 부사절에서는 미래의 일도 현재형으로 쓴다. 밑줄에 will이 있으면 틀린 것이다: {0}. → ③ 남은 두 문장을 묶은 {a}가 정답이다.",
  R="(B) will be, (D) will be", B="(A) will rain, (C) will finish", C="(A) will be, (B) will end", D="(B) will get, (C) will snow", E="(C) will arrive, (D) will come", F="(A) will be, (D) will rain")
RV(2, 18, "BCDEF", fx=True, why="수정 예시의 발문이 ‘모두 빠짐없이 묶은 것’이고 보기에 세 문장 조합이 섞여 있어 원문항(‘옳은 문장으로만 짝지어진 것’, 모두 두 문장 조합)과 달랐다. 옳은 문장이 둘이 되도록 문장을 고치고 보기를 모두 두 문장 조합으로 맞춰 발문을 원문항과 같게 했다.")

X(2, 19, r="단순과거는 과거에 일어난 사건만 말하고 지금 상태는 알려 주지 않는다. 현재완료(결과)는 과거의 일이 낳은 결과가 지금도 이어짐을 나타낸다.",
  n=["(A)가 과거형이고 (B)가 현재완료인데 거꾸로 설명했으므로", "(A)는 과거 사건만 말해 지금은 찾았을 수도 있고, (B)는 지금도 시계가 없다는 결과를 나타내므로", "(A)는 현재완료가 아니고 두 문장의 뜻도 다르므로", "yesterday는 과거형과 함께 쓰는 올바른 표현이므로",
     "(A)는 현재완료 진행형이 아니라 단순과거이므로"],
  st="① 두 문장의 동사 형태를 본다. (A)는 과거형({0})이고 (B)는 현재완료({1})다. → ② 과거형은 {2} 일어난 사건만 말하고 지금 상태는 말하지 않는다. 현재완료는 그 결과가 지금도 이어진다는 뜻이다({3}). → ③ 이 차이를 말한 {n}을 고른다.",
  R=("lost", "have lost", "어제", "지금도 시계가 없다"), B=("left", "has left", "오늘 아침에", "지금 우산이 없다"), C=("broke", "has broken", "어제", "지금도 안경이 깨져 있다"), D=("missed", "have missed", "8시에", "지금 기차를 놓친 상태다"),
  E=("lost", "has lost", "어젯밤에", "지금 열쇠가 없다"), F=("closed", "has closed", "9시에", "지금 가게가 닫혀 있다"))
RV(2, 19, "B", v="수정(내용)", why="정답 ② 확인. 정답만 ‘(A)는 …, (B)는 …’ 꼴의 긴 설명이고 오답은 짧은 한 줄이라 형식으로 답이 드러난다(C4). ④는 지문에 없는 yesterday를 말한다. 본문의 <보기> 표시도 빠졌다.", fix="오답도 두 문장을 견주는 설명으로, <보기> 표시 넣기")
RV(2, 19, "CDEF", fx=True, why="수정 예시 본문에 <보기> 표시가 빠져 있어 넣었다.")

X(2, 20, r="현재완료는 yesterday 같은 끝난 과거 시점이나 때를 묻는 When과 함께 쓸 수 없다. Do/Does 의문문에서는 주어 뒤 동사를 원형으로 쓴다.",
  pre=["문장별 판정: (가) X. yesterday가 있으므로 saw. (나) X. Does 뒤이므로 take. (다) O. for + 기간의 현재완료. (라) O. 잃어버린 결과가 지금 이어지는 현재완료. (마) X. When으로 과거의 때를 물으므로 When did you meet."],
  k="옳은 문장은 (다), (라) 두 개다.", n=["옳은 문장은 (다), (라) 두 개이므로"] * 5,
  st="① 문장마다 시간 표현과 시제를 견준다. yesterday, ago, last night 같은 끝난 과거 시점이나 When 의문문에는 현재완료를 쓰지 않는다. → ② Do/Does 의문문은 주어 뒤 동사가 원형인지 본다. → ③ {0} 옳은 문장은 {a}이다.",
  R="(가)는 yesterday, (마)는 When 때문에 현재완료를 쓸 수 없고, (나)는 Does 뒤에 takes를 썼다. (다), (라)만 옳다.",
  B="(가)는 yesterday, (마)는 When과 last night 때문에 현재완료를 쓸 수 없다. (나), (다), (라)가 옳다.",
  C="(가)는 last Monday, (마)는 When과 yesterday 때문에 현재완료를 쓸 수 없고, (나)는 Does 뒤에 walks를 썼다. (다), (라)만 옳다.",
  D="(가)만 틀렸다. two days ago에는 과거형 met을 쓴다. 나머지 넷이 옳다.",
  E="(가)는 yesterday, (라)는 an hour ago, (마)는 When 때문에 현재완료를 쓸 수 없고, (나)는 Does 뒤에 works를 썼다. (다)만 옳다.",
  F="(가)만 틀렸다. last night에는 과거형 called를 쓴다. 나머지 넷이 옳다.")
