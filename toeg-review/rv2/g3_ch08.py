# 3급 CH8 부정사 (71~80) 2차 감수
X(3, 71, r="to부정사가 꾸미는 명사가 전치사의 목적어이면 to부정사 뒤에 전치사를 남긴다: sit on chairs → chairs to sit on.",
  n=["sit with chairs라고는 하지 않으므로", "sit to chairs라고는 하지 않으므로", "sit at chairs라고는 하지 않으므로", "‘의자 위에 앉다’는 sit on chairs이므로", "sit for chairs라고는 하지 않으므로"],
  st="① 빈칸 앞의 to부정사가 꾸미는 명사({0})를 동사 뒤로 옮겨 본다: {1}. → ② 이때 필요한 전치사를 to부정사 뒤에 그대로 남긴다. → ③ 정답은 {a}.",
  R=("chairs", "sit on chairs(의자 위에 앉다)"), B=("a stool", "stand on a stool(발판 위에 서다)"), C=("a pen", "write with a pen(펜으로 쓰다)"), D=("a friend", "talk to a friend(친구에게 말하다)"), E=("a room", "study in a room(방 안에서 공부하다)"),
  F=("a bed", "sleep on a bed(침대 위에서 자다)"))

X(3, 72, r="‘의문사 + to + 동사원형’은 ‘~할지’라는 뜻의 명사구로 동사의 목적어가 된다(what to do: 무엇을 해야 할지).",
  n=["의문사 뒤에 -ing가 아니라 to부정사를 써야 하므로", "의문사 + to + 동사원형으로 ‘무엇을 해야 할지’를 나타내므로", "to가 빠졌으므로", "to 뒤에 -ing를 쓸 수 없으므로", "for doing은 쓸 수 없으므로"],
  st="① 빈칸은 동사({0})의 목적어 자리다. ‘의문사 + to부정사’가 ‘~할지’라는 뜻의 명사구로 목적어가 된다. → ② 형태는 ‘의문사 + to + 동사원형’이다. to가 없거나 -ing를 쓰거나 for를 쓰거나 that으로 시작하면 틀린다. → ③ 정답은 {a}.",
  R="know", B="decide", C="know", D="know", E="knows", F="know")

X(3, 73, r="too + 형용사 + to + 동사원형은 ‘너무 ~해서 …할 수 없다’는 뜻이다. 문장의 주어가 to부정사의 목적어이면 뒤에 목적어를 다시 쓰지 않는다.",
  n=["too의 위치가 틀렸고 very와 it도 남아 있으므로", "too + 형용사 + to + 동사원형으로 바르게 바꿨으므로", "too가 형용사 뒤에 놓였으므로", "so ~ to로는 쓸 수 없으므로", "very와 too를 함께 쓸 수 없으므로"],
  st="① ‘very + 형용사 … couldn't’를 ‘too + 형용사 + to + 동사원형’(너무 ~해서 …할 수 없다)으로 바꾼다. → ② too는 형용사({0}) 앞에 둔다. 문장의 주어({1})가 to부정사의 목적어이므로 뒤에 it(them)을 다시 쓰지 않는다. → ③ 정답은 {n}.",
  R=("heavy", "The box"), B=("small", "The shoes"), C=("hot", "The coffee"), D=("big", "The bag"), E=("difficult", "The problem"), F=("deep", "The river"))

X(3, 74, r="‘~하기 위해’라는 목적의 to부정사는 in order to로 바꿀 수 있다. 결과(grew up to be), 감정의 원인, 명사·형용사를 꾸미는 to부정사는 바꿀 수 없다.",
  n=["‘첫 기차를 타기 위해’라는 목적이라 바꿀 수 있으므로", "‘새 집을 사기 위해’라는 목적이라 바꿀 수 있으므로", "‘성공하기 위해’라는 목적이라 바꿀 수 있으므로", "‘자라서 변호사가 되었다’는 결과라 in order to로 바꿀 수 없으므로", "‘더 좋은 일자리를 찾기 위해’라는 목적이라 바꿀 수 있으므로"],
  st="① 밑줄 친 to부정사가 ‘~하기 위해’(목적)로 풀리는지 본다. 목적일 때만 in order to로 바꿀 수 있다. → ② 네 문장은 ‘~하기 위해’로 자연스럽게 풀린다. → ③ {n}은 {0}. in order to로 바꿀 수 없다.",
  R="‘자라서 변호사가 되었다’는 결과다", B="‘그를 보고 놀랐다’는 감정의 원인이다", C="‘아흔 살까지 살았다’는 결과다", D="‘깨어 보니 방이 비어 있었다’는 결과다", E="형용사 easy를 꾸며 ‘대답하기에 쉽다’는 뜻이다",
  F="명사 homework를 꾸며 ‘할 숙제’라는 뜻이다")
RV(3, 74, "BCDE", fx=True, why="수정 예시의 보기 가운데 ‘He went <u>to</u> the library to borrow …’처럼 전치사 to에 밑줄이 그어진 문장이 있었다. 전치사 to도 in order to로 바꿀 수 없으므로 정답이 둘 이상이 되었다(E는 셋). 밑줄을 뒤의 to부정사로 옮겨 정답을 하나로 했다.")

X(3, 75, r="to부정사는 ‘to + 동사원형’이다. want, hope, decide, promise는 to부정사를, enjoy는 동명사를 목적어로 쓴다. 보어 자리에도 to부정사를 쓴다(My goal is to become ~).",
  pre=["문장별 판정: ⓐ X. to 뒤에는 동사원형(to get). ⓑ X. enjoy는 동명사(playing)를 쓴다. ⓒ O. 의문사 + to부정사. ⓓ O. the book을 꾸미는 to부정사. ⓔ X. is to become으로 써야 한다."],
  k="옳은 문장은 ⓒ, ⓓ 두 개다.", n=["옳은 문장은 ⓒ, ⓓ 두 개이므로"] * 5,
  st="① 밑줄마다 to부정사의 형태가 ‘to + 동사원형’인지 본다. → ② 앞의 동사가 to부정사를 쓰는 동사(want, hope, decide, promise)인지 동명사를 쓰는 동사(enjoy)인지 확인한다. → ③ {0} 옳은 문장은 {a}이다.",
  R="ⓐ는 to getting(to get), ⓑ는 enjoys to play(playing), ⓔ는 is become(is to become)이 틀렸다. ⓒ, ⓓ만 옳다.", B="ⓑ는 to eating(to eat), ⓒ는 promised calling(to call), ⓓ는 play(to play), ⓔ는 to becoming(to become)이 틀렸다. ⓐ만 옳다.",
  C="ⓑ는 decided going(to go), ⓔ는 enjoys to swim(swimming)이 틀렸다. 나머지 셋이 옳다.", D="ⓒ만 틀렸다. want는 to부정사를 쓰므로 to learn이다.", E="ⓒ만 틀렸다. enjoy는 동명사를 쓰므로 reading이다.",
  F="ⓒ는 enough strong(strong enough), ⓔ는 finishing(to finish)이 틀렸다. 나머지 셋이 옳다.")
RV(3, 75, "EF", fx=True, why="수정 예시 E는 틀린 문장이 하나도 없는 5개여서 원래 변형의 틀린 문장(enjoy to read)을 되살려 4개로 했고, F는 정답(2개, ②)이 원문항의 정답 개수·위치와 같아 3개로 바꿨다.")

X(3, 76, r="want, promise, decide, hope, plan, need는 to부정사(to + 동사원형)를 목적어로 쓴다.",
  n=["want 뒤에 be learning을 쓸 수 없으므로", "to 뒤에 -ing를 쓸 수 없으므로", "want는 to부정사를 목적어로 쓰므로", "to가 빠졌으므로", "want 뒤에 과거형을 쓸 수 없으므로"],
  st="① 밑줄 앞의 동사({0})를 본다. to부정사를 목적어로 쓰는 동사다. → ② to부정사는 ‘to + 동사원형’이다. to 뒤에 -ing를 쓰거나 to를 빼거나 for를 쓰면 틀린다. → ③ 정답은 {a}.",
  R="want", B="promised", C="decided", D="hopes", E="plan", F="need")

X(3, 77, r="to부정사구가 주어일 때는 가주어 It을 주어 자리에 두고 to부정사구를 뒤로 보낸다: It is + 형용사 + to부정사.",
  n=["낱말 순서가 뒤섞였으므로", "solve 앞에 to가 빠졌으므로", "is가 형용사 뒤에 놓였으므로", "It is + 형용사 + to부정사 순서로 바르게 바꿨으므로", "형용사 difficult가 문장 끝에 놓였으므로"],
  st="① 주어가 to부정사구({0})다. 이것을 문장 뒤로 보내고 주어 자리에 가주어 It을 둔다. → ② 순서는 ‘It + is + 형용사({1}) + to부정사구’다. → ③ There·This로 시작한 것, to 대신 for를 쓴 것, 바꾸지 않은 문장은 지운다. 정답은 {n}.",
  R=("To solve this problem", "difficult"), B=("To swim in this river", "dangerous"), C=("To learn English", "useful"), D=("To get up early", "hard"), E=("To exercise every day", "important"), F=("To finish the work today", "necessary"))

X(3, 78, r="to부정사가 꾸미는 명사가 전치사의 목적어이면 전치사를 남긴다: a chair to sit on, a house to live in, a pen to write with.",
  n=["명사를 꾸미려면 to부정사가 필요하므로", "동사원형만으로는 명사를 꾸밀 수 없으므로", "to 뒤에 -ing를 쓸 수 없으므로", "sit on a chair이므로 to sit on이 알맞으므로", "to가 빠졌으므로"],
  st="① 밑줄 친 to부정사는 앞의 명사({0})를 꾸민다. 명사를 동사 뒤로 옮겨 본다: {1}. → ② 전치사가 있어야 말이 되므로 to부정사 뒤에 전치사를 남긴다. → ③ 정답은 {a}.",
  R=("a chair", "sit on a chair"), B=("a house", "live in a house"), C=("a pen", "write with a pen"), D=("a friend", "talk to a friend"), E=("a quiet room", "study in a room"), F=("a spoon", "eat with a spoon"))

X(3, 79, r="so + 형용사 + that + 주어 + can ~은 ‘형용사 + enough + to + 동사원형’으로 바꿀 수 있다. enough는 형용사 뒤에 쓴다.",
  n=["enough 뒤에 to가 빠졌으므로", "enough가 형용사 앞에 놓였으므로", "형용사 + enough + to + 동사원형으로 바르게 바꿨으므로", "to의 위치가 틀렸으므로", "be동사 is가 빠졌으므로"],
  st="① ‘so + 형용사 + that + 주어 + can’은 ‘형용사 + enough + to + 동사원형’으로 바꾼다. → ② enough는 형용사({0}) 뒤에 온다. 그 뒤에 to + 동사원형({1})이 이어진다. → ③ 정답은 {n}.",
  R=("strong", "to carry"), B=("smart", "to solve"), C=("tall", "to reach"), D=("old", "to drive"), E=("large", "to hold"), F=("fast", "to win"))
RV(3, 79, "B", fx=True, why="수정 예시의 오답에 영어에 없는 말(enoughly)이 있어, to가 빠진 오답(smart enough solve)으로 바꿨다.")
RV(3, 79, "CDEF", v="수정(내용)", why="정답 확인. 다만 오답 가운데 영어에 없는 말(enoughly)이 있어 형태만으로 지워진다. 원문항의 오답은 모두 실제 낱말로 된 문장이고, enough를 형용사 앞에 둔 오답(enough strong)이 핵심 함정인데 변형에는 빠져 있다.", fix="enoughly 오답을 enough + 형용사 오답으로")

X(3, 80, r="to부정사는 ‘to + 동사원형’이고 부정은 not to + 동사원형이다. 주어가 동작을 받으면 to be + 과거분사로 쓴다. 결과(woke up to find), 가주어 It ~ to 구문도 to부정사다.",
  pre=["문장별 판정: (가) X. to wear. (나) X. not to fail. (다) X. 초대받은 것이므로 to be invited. (라) O. ‘깨어 보니 ~였다’는 결과. (마) O. 가주어 It ~ to부정사."],
  n=["(가)와 (나)가 틀렸으므로", "(나)와 (다)가 틀렸으므로", "(다)가 틀렸으므로", "(라)와 (마)가 모두 옳으므로", "(나)가 틀렸으므로"],
  st="① 문장마다 to 뒤가 동사원형인지 본다. to + -ing, to + 과거형은 틀린다. → ② 의미상 주어(성품 형용사 뒤 of, 그 밖에는 for), 동사 뒤 목적어 형태(decide + to부정사), enough의 위치도 확인한다. → ③ 틀린 문장을 지운다: {0}. 옳은 문장만 묶은 {a}가 정답이다.",
  R="(가) to wearing, (나) not to failing, (다) to invited", B="(나) buy(to buy), (라) to hearing", C="(다) to reading, (마) wants learning", D="(다) to studying, (라) decided going", E="(라) for see, (마) enough old",
  F="(가) wise for her(of her), (마) too young driving")
RV(3, 80, "DEF", fx=True, why="수정 예시의 옳은 문장이 넷이라 보기에 네 문장 조합이 들어가 원문항(두세 문장 조합)과 형태가 달랐다. 한 문장을 틀린 문장으로 바꿔 옳은 문장을 셋으로 하고 보기를 두세 문장 조합으로 맞췄다.")
