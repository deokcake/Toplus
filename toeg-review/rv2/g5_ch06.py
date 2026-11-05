# 5급 CH6 미래시제 (51~60) 2차 감수
X(5, 51, r="조동사 will 뒤에는 주어와 관계없이 동사원형을 쓴다.",
  n=["will 뒤에 -s형을 쓸 수 없으므로", "will 뒤에 -ing형을 쓸 수 없으므로", "be와 go 두 동사원형을 겹쳐 쓸 수 없으므로", "will 뒤에 동사원형 go를 썼으므로", "will 뒤에 과거형을 쓸 수 없으므로"],
  st="① 빈칸 바로 앞의 will을 본다. → ② will 뒤는 주어가 {0}이어도 동사원형이다. -s, -ing, to부정사, 과거형, be를 덧붙인 것을 지운다. → ③ 정답은 {a}.",
  R="3인칭 단수 He", B="복수 They", C="3인칭 단수 She", D="복수 They", E="I", F="We")

X(5, 52, r="미래 표현 두 가지: be동사 + going to + 동사원형, will + 동사원형.",
  n=["are 뒤에는 go가 아니라 going이, will 뒤에는 starting이 아니라 start가 와야 하므로", "will 뒤에 -ing형 starting을 쓸 수 없으므로", "are 뒤에는 go가 아니라 going이 와야 하므로", "are gone to leave라고 쓰지 않고 will 뒤에 starts도 쓸 수 없으므로", "are going to + 동사원형, will + 동사원형 start로 알맞으므로"],
  st="① 첫 문장: be동사({0})와 to 사이의 빈칸이므로 be going to의 going이 들어간다. → ② 둘째 문장: will 뒤이므로 동사원형 {1}. → ③ 정답은 {a}.",
  R=("are", "start"), B=("is", "begin"), C=("is", "call"), D=("are", "rain"), E=("am", "go"), F=("is", "come"))
RV(5, 52, "B", fx=True, why="변형의 두 문장 앞에 원문항에 있는 ‘-’ 표시가 없다. 수정 예시에서 원문항처럼 ‘-’를 붙였다.")

X(5, 53, r="be going to + 동사원형은 ‘~할 것이다’(미래), be going to + 장소(명사)는 ‘~로 가고 있다’(go의 진행형 + 전치사 to)이다.",
  n=["to 뒤에 명사 the concert가 와서 ‘~로 가고 있다’의 뜻이므로", "to 뒤에 동사원형 meet이 와서 미래의 뜻이므로", "to 뒤에 동사원형 learn이 와서 미래의 뜻이므로", "to 뒤에 동사원형 bring이 와서 미래의 뜻이므로", "to 뒤에 동사원형 attend가 와서 미래의 뜻이므로"],
  st="① going to 바로 뒤의 말을 본다. → ② 동사원형이면 ‘~할 것이다’, 명사(장소)면 ‘~로 가고 있다’이다. → ③ {0} 정답은 {n}.",
  R="①만 뒤에 명사 the concert가 온다.", B="⑤만 뒤에 명사 the library가 온다.", C="⑤만 뒤에 명사 school이 온다.", D="③만 뒤에 명사 the bank가 온다.", E="②만 뒤에 명사 the airport가 온다.", F="④만 뒤에 명사 the hospital이 온다.")

X(5, 54, r="will/won't 뒤와 be going to 뒤에는 동사원형을 쓴다. be going to의 be동사는 주어에 맞춘다.",
  n=["won't 뒤에는 sees가 아니라 동사원형 see를 써야 하므로", "is going to + 동사원형으로 바르게 썼으므로", "Are you going to + 동사원형으로 바르게 물었으므로", "will + 동사원형 rain으로 바르게 썼으므로", "will + 동사원형 go로 바르게 썼으므로"],
  st="① 문장마다 미래 표현(will, won't, be going to)을 찾는다. → ② 그 뒤가 동사원형인지, be going to의 be동사가 주어와 맞는지 본다. → ③ {0} 정답은 {n}.",
  R="①은 won't 뒤에 sees를 썼다.", B="③은 won't 뒤에 과거형 arrived를 썼다.", C="④는 is going to 뒤에 takes를 썼다.", D="⑤는 will 뒤에 calls를 썼다.", E="①은 단수 주어 Jane에 Are를 썼다.", F="②는 won't 뒤에 to come을 썼다.")

X(5, 55, r="will/won't 뒤와 be going to 뒤에는 동사원형을 쓴다. Will 의문문에는 will/won't로 답한다.",
  n=["are you going to 뒤에 동사원형 do를 바르게 썼으므로", "주어 I에 am을 바르게 썼으므로", "미래의 일을 Will로 바르게 물었으므로", "Will 의문문에 won't로 바르게 답했으므로", "will 뒤에는 동사원형 stay를 써야 하므로"],
  st="① 밑줄마다 앞에 있는 말을 본다: will, won't, be going to 뒤는 동사원형이다. → ② be동사 밑줄은 주어와 맞는지, 대답은 질문의 조동사와 맞는지 본다. → ③ {0} 정답은 {n}.",
  R="⑤는 will 뒤인데 stays다.", B="④는 is going to 뒤인데 leaves다.", C="②는 will 뒤인데 goes다.", D="①은 are going to 뒤인데 watches다.", E="⑤는 will 뒤인데 drives다.", F="③은 주어가 we인데 is다.")
RV(5, 55, "CE", v="수정(표기)", why="정답 확인. 다만 원문항은 밑줄이 모두 한 단어인데 변형은 ‘will + 동사’ 두 단어씩(will goes, will stay)이고 첫 밑줄만 What 등으로 달라 밑줄 범위가 원문항과 다르다. 대화도 한 번 주고받는 것뿐이다(원문항은 네 차례).", fix="밑줄을 한 단어로, 대화를 네 차례로")
RV(5, 55, "D", fx=True, why="수정 예시의 대화가 한 번 주고받는 것뿐이어서 원문항(네 차례)과 달랐다. 네 차례 주고받는 대화로 바꿨다.")

X(5, 56, r="be going to 뒤에는 동사원형을 쓴다. to가 이미 있으므로 to를 또 쓰지 않는다.",
  n=["is going to 뒤에 동사원형 go를 썼으므로", "to 뒤에 -s형을 쓸 수 없으므로", "to 뒤에 -ing형을 쓸 수 없으므로", "to 뒤에 과거형을 쓸 수 없으므로", "to가 이미 있어 to를 겹쳐 쓸 수 없으므로"],
  st="① 빈칸 앞이 {0} going to다. ‘~할 것이다’의 be going to이다. → ② to 뒤에는 동사원형만 온다. → ③ ‘{1}’의 뜻이 되는 것은 {a}.",
  R=("is", "쇼핑하러 갈 것이다"), B=("is", "저녁을 요리할 것이다"), C=("is", "축구를 할 것이다"), D=("are", "TV를 볼 것이다"), E=("am", "책을 읽을 것이다"), F=("are", "저녁을 먹을 것이다"))

X(5, 57, r="won't(will not) 뒤에는 동사원형을 쓴다. be동사의 원형은 be다.",
  n=["won't 뒤에 동사원형 go를 썼으므로", "won't 뒤에 동사원형 get을 썼으므로", "won't 뒤에는 is가 아니라 동사원형 be를 써야 하므로", "won't 뒤에 동사원형 play를 썼으므로", "won't 뒤에 동사원형 eat을 썼으므로"],
  st="① 밑줄은 모두 won't 바로 뒤의 동사다. → ② 동사원형이 아닌 것을 찾는다. {0} → ③ 정답은 {n}.",
  R="is는 be의 현재형이다(won't be).", B="are는 be의 현재형이다(won't be).", C="arrives는 -s형이다(won't arrive).", D="answering은 -ing형이다(won't answer).", E="drove는 과거형이다(won't drive).", F="watches는 -es형이다(won't watch).")

X(5, 58, r="현재진행형(be동사 + -ing)은 가까운 미래의 정해진 계획도 나타낸다. 평서문 어순은 주어 + be동사 + -ing + 목적어 + 때를 나타내는 말이다.",
  n=["주어 + are + playing + soccer + this afternoon의 순서이므로", "are가 playing 뒤에 와서 어순이 틀렸으므로", "주어보다 are가 먼저 와서 평서문 어순이 아니므로", "Are로 시작한 의문문 어순에 마침표를 붙였으므로", "목적어 soccer가 맨 앞에 왔으므로"],
  st="① 마침표로 끝나므로 평서문이다. 주어({0})로 시작한다. → ② 주어 뒤에 be동사({1}) + -ing형({2})을 두고, 나머지({3})를 잇는다. → ③ 이 순서인 것은 {n}.",
  R=("We", "are", "playing", "soccer / this afternoon"), B=("Mina", "is", "meeting", "her cousin / tonight"), C=("Jane", "is", "meeting", "Tom / tomorrow"), D=("They", "are", "leaving", "tonight"),
  E=("I", "am", "visiting", "grandma / tomorrow"), F=("We", "are", "having", "dinner / at seven"))

X(5, 59, r="시간표·상영 시간·영업 시간처럼 정해진 일정은 현재시제로 미래의 일을 나타낼 수 있다.",
  n=["진행의 뜻은 is starting으로 나타내므로", "과거의 일은 started로 나타내므로", "정해진 일정은 현재시제로 미래를 나타내므로", "사물 주어에도 will을 쓸 수 있으므로(The movie will start ~)", "습관만이 아니라 정해진 미래 일정을 말하므로"],
  st="① 문장에서 때를 나타내는 말을 본다: {0}. 앞으로의 정해진 시각이다. → ② 그런데 동사는 현재형({1})이다. 시간표·일정에 따른 일이기 때문이다. → ③ 이 이유를 말한 것은 {n}.",
  R=("at 8 o'clock", "starts"), B=("at six tomorrow morning", "leaves"), C=("at 7 tomorrow", "leaves"), D=("at 9 tomorrow", "begins"), E=("at 6 tonight", "starts"), F=("at 10 tomorrow", "opens"))

X(5, 60, r="be going to의 be동사는 주어에 맞추고(you → are), going to 뒤와 will/won't 뒤에는 동사원형을 쓴다.",
  pre=["부분별 판정: (가) O. What are you going to do. (나) X. 주어 you에는 Are를 쓴다. (다) X. going to 뒤에는 doing이 아니라 do를 쓴다. (라) O. he에 is를 썼다."],
  k="틀린 부분은 (나), (다)로 2개이다.", n=["틀린 부분이 2개이므로"] * 5,
  st="① 밑줄마다 be동사·will이 주어와 맞게 쓰였는지 본다. → ② going to, will, won't 뒤가 동사원형인지 본다. 현재진행형·현재시제로 나타낸 정해진 계획은 옳은 표현이다. → ③ {0} 정답은 {a}.",
  R="(나) Is you, (다) going to doing이 틀렸다.", B="(나) will brings, (다) Are Tom이 틀렸다.", C="(나) will studies만 틀렸다. (가)의 현재진행형, (다)의 현재시제는 옳다.", D="(가) will watches, (나) going to plays, (다) won't goes가 틀렸다.",
  E="(가) will helps, (나) are going visit, (다) Are Tom, (라) won't comes가 모두 틀렸다.", F="네 부분 모두 옳다. (가)의 현재진행형, (다)의 현재시제도 정해진 일을 나타내는 옳은 표현이다.")
