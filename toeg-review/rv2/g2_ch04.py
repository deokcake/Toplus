# 2급 CH4 수동태 (31~40) 2차 감수
X(2, 31, r="주어가 동작을 받는 대상이면 수동태(be동사 + 과거분사)를 쓴다. be동사는 주어의 수와 시제에 맞춘다.",
  n=["콘서트는 관람되는 대상이라 능동태를 쓸 수 없으므로", "콘서트는 관람되는 대상이라 능동 진행형을 쓸 수 없으므로", "단수 주어와 last night에 맞는 과거 수동태이므로", "주어 The concert가 단수라 were를 쓸 수 없으므로", "능동태이고 last night과 현재완료도 함께 쓸 수 없으므로"],
  st="① 주어({0})가 동작을 하는 쪽인지 받는 쪽인지 본다. {1} 대상이므로 수동태다. 능동형 보기를 지운다. → ② 시간 표현({2})으로 시제를 정한다. → ③ 주어의 수까지 맞춘 {a}가 정답이다.",
  R=("The concert", "관람되는", "last night → 과거"), B=("The old bridge", "수리되는", "last year → 과거"), C=("Several new classrooms", "지어지는", "this semester → 현재완료"), D=("The road", "넓혀지는", "right now → 현재진행"),
  E=("The documents", "준비되는", "before the meeting began → 과거완료"), F=("The winners", "발표되는", "tomorrow → 미래"))
RV(2, 31, "CEF", v="수정(내용)", why="정답 확인. 다만 오답 하나가 영어에 없는 형태(C have build, E had being prepared, F will been announced)라 태·시제를 따지지 않고도 지워진다. 원문항의 오답은 모두 형태가 바른 능동형·수 불일치형이다.", fix="없는 형태의 오답을 형태가 바른 능동형으로")

X(2, 32, r="Did + 주어 뒤에는 동사원형을 쓴다. 주어가 동작을 받는 대상이면 수동태(be동사 + 과거분사)를 쓴다.",
  n=["Did 뒤에는 동사원형 make, by my mother가 있는 둘째 빈칸에는 수동태 was made를 쓰므로", "Did 뒤에 과거형 made를 쓸 수 없으므로", "두 빈칸 모두 맞지 않으므로", "두 빈칸 모두 맞지 않으므로", "두 빈칸 모두 맞지 않으므로"],
  st="① 첫째 빈칸은 Did + 주어 뒤다. 동사원형({0})이 온다. → ② 둘째 빈칸의 주어({1})는 동작을 받는 대상이고 뒤에 by ~가 있다. 수동태다. 과거의 일이므로 {2}. → ③ 정답은 {n}.",
  R=("make", "it = 케이크", "was made"), B=("design", "it = 포스터", "was designed"), C=("bake", "they = 쿠키", "were baked"), D=("write", "it = 기사", "was written"), E=("clean", "it = 방", "was cleaned"), F=("take", "it = 사진", "was taken"))
RV(2, 32, "BCDEF", v="수정(내용)", why="정답 확인. 다만 오답에 was design, were bake, was write, was take 같은 없는 형태와 Did ~ designing 같은 꼴이 섞여 형태만으로 지워진다. 원문항의 보기는 make, made, was made만 조합한다. 원문항에 없는 (A)·(B) 표시도 붙어 있다.", fix="보기를 동사원형·과거형·수동태 조합으로, (A)·(B) 삭제")

X(2, 33, r="4형식 문장의 직접목적어를 주어로 한 수동태에서 간접목적어 앞에는 전치사를 쓴다. give, send, teach, lend, offer, award는 to, buy, make, cook, find, reserve, prepare는 for를 쓴다.",
  n=["buy는 for를 쓰는 동사이므로", "reserve는 for를 쓰는 동사이므로", "give는 for가 아니라 to를 쓰는 동사이므로", "prepare는 for를 쓰는 동사이므로", "select는 for를 쓰는 동사이므로"],
  st="① 빈칸은 ‘사물 + be + 과거분사 + 전치사 + 사람’에서 사람 앞 전치사 자리다. 문장마다 과거분사의 원래 동사를 본다. → ② ‘~에게 건네주는’ 동사(give, send, teach, lend, offer, award)는 to, ‘~을 위해 해 주는’ 동사는 for를 쓴다. → ③ {n}의 동사({0})만 to를 쓴다. 나머지({1})는 for다.",
  R=("give", "buy, reserve, prepare, select"), B=("award", "buy, cook, find, make"), C=("lend", "book, choose, order, build"), D=("teach", "save, pour, bake, buy"), E=("give", "prepare, cook, call, pick out"), F=("offer", "reserve, buy, save, make"))

X(2, 34, r="사역동사 make + 목적어 + 동사원형을 수동태로 바꾸면 ‘be made to + 동사원형’이 된다. 동사원형 앞에 to가 살아난다.",
  n=["be동사 없이 made만 쓰면 수동태가 아니므로", "수동태에서는 동사원형 앞에 to를 써야 하므로", "be made to + 동사원형으로 바르게 바꿨으므로", "to + 동사원형 자리에 -ing를 쓸 수 없으므로", "to 뒤에 -ing를 쓸 수 없으므로"],
  st="① 능동태의 목적어({0})를 주어로 하고 동사를 ‘be동사 + made’로 바꾼다. → ② 능동태에서 동사원형이던 목적격 보어({1})는 수동태에서 to부정사가 된다. → ③ 행위자는 by로 나타낸다. be동사가 빠진 것, to가 없는 것, to + -ing는 모두 틀리다. 정답은 {n}.",
  R=("me → I", "clean → to clean"), B=("the players", "run → to run"), C=("me → I", "wash → to wash"), D=("us → We", "rewrite → to rewrite"), E=("Tom", "work → to work"), F=("everyone", "cry → to cry"))

X(2, 35, r="사역동사 make와 지각동사의 수동태에서는 목적격 보어였던 동사원형이 to부정사로 바뀐다(be made to V, be seen to V). 이 to는 생략할 수 없다. let과 have는 수동태로 잘 쓰지 않고 be allowed to, be asked to로 바꿔 쓴다.",
  n=["make의 수동태는 be made to + 동사원형이라 옳은 설명이므로", "지각동사의 수동태도 be seen to + 동사원형으로 쓸 수 있어 옳은 설명이므로", "let은 be allowed to로 바꿔 쓰므로 옳은 설명이므로", "have는 be asked to 등으로 바꿔 쓰므로 옳은 설명이므로",
     "be made to + 동사원형의 to는 생략할 수 없으므로"],
  st="① 학생마다 어느 동사(make, let, have, 지각동사)의 수동태를 말하는지 찾는다. → ② 기준과 견준다. make와 지각동사는 동사원형이 to부정사로 바뀌고(현재분사는 그대로), let은 be allowed to, have는 다른 표현으로 바꿔 쓴다. → ③ {n}은 {0}.",
  R="be made to의 to를 생략할 수 있다고 했다. 이 to는 생략할 수 없다", B="make의 수동태에서 동사원형을 그대로 둔다고 했다. to부정사로 바뀐다", C="지각동사의 수동태에서 동사원형을 그대로 쓴다고 했다. to cross나 crossing이 맞다",
  D="make의 수동태에 -ing만 쓴다고 했다. to + 동사원형을 쓴다", E="현재분사를 그대로 둔 수동태는 쓸 수 없다고 했다. was heard crying은 옳은 문장이다", F="be made to의 to를 전치사로 보았다. to부정사의 to라 뒤에 동사원형이 온다")

X(2, 36, r="주어가 동작을 받는 대상이면 수동태를 쓰고, 과거의 일이면 was/were + 과거분사로 쓴다(ride - rode - ridden).",
  n=["when he was young이라는 과거의 일에 현재 시제를 쓸 수 없으므로", "능동태이고 has rode는 형태도 틀렸으므로", "자전거(It)는 타는 쪽이 아니라 타지는 대상이라 능동태를 쓸 수 없으므로", "과거의 일이고 by ~가 있어 과거 수동태가 알맞으므로", "능동태 과거완료라 by ~와 맞지 않으므로"],
  st="① B의 주어 It({0})은 동작을 받는 대상이고 빈칸 뒤에 by ~가 있다. 수동태다. → ② A가 과거형({1})으로 물었으므로 과거의 일이다. → ③ 과거 수동태 {a}가 정답이다. 능동형과 진행형 보기는 지운다.",
  R=("자전거", "rode"), B=("그림", "painted"), C=("노래", "wrote"), D=("돌담", "built"), E=("사진", "took"), F=("건물", "designed"))

X(2, 37, r="지각동사 + 목적어 + 현재분사를 수동태로 바꾸면 ‘be동사 + 과거분사 + 현재분사’다. 현재분사는 그대로 둔다.",
  n=["to 뒤에 -ing를 쓸 수 없으므로", "heard가 과거이므로 is를 쓸 수 없고 to crying도 틀렸으므로", "was hearing은 능동 진행형이므로", "능동태에 없던 동사원형 cry로 바꿀 수 없으므로(to cry나 crying)", "was heard 뒤에 현재분사 crying을 그대로 두어 바르게 바꿨으므로"],
  st="① 능동태의 목적어({0})가 주어가 되고 동사는 ‘be동사 + 과거분사’가 된다. 능동태 동사({1})가 과거형이므로 {2}. → ② 목적격 보어였던 현재분사({3})는 그대로 둔다. to를 붙이거나 동사원형으로 바꾸지 않는다. → ③ 정답은 {n}.",
  R=("the baby", "heard", "was heard", "crying"), B=("the girl", "heard", "was heard", "singing"), C=("a dog", "saw", "was seen", "chasing"), D=("Tom", "heard", "was heard", "playing"),
  E=("the children", "saw", "were seen", "running"), F=("the dancer", "watched", "was watched", "performing"))

X(2, 38, r="진행형 수동태는 ‘be동사 + being + 과거분사’다. 주어가 동작을 받는 대상이면 being 뒤에 과거분사를 쓴다.",
  n=["Many 뒤의 복수 명사로 알맞으므로", "복수 주어 trees에 맞는 be동사이므로", "진행형 수동태의 being으로 알맞으므로", "나무는 심어지는 대상이다. being 뒤에는 과거분사 planted를 써야 하므로", "장소를 나타내는 전치사구로 알맞으므로"],
  st="① 문장의 뼈대는 진행형 수동태 ‘be동사 + being + 과거분사’다. 세 자리를 차례로 본다. → ② be동사는 주어의 수에 맞는지, 가운데는 being인지, 끝은 과거분사인지, by 뒤는 목적격인지 확인한다. → ③ {n}이 틀렸다: {0}.",
  R="나무는 심어지는 대상이므로 planting이 아니라 planted", B="가운데 자리는 been이 아니라 being", C="주어 These letters가 복수이므로 was가 아니라 were", D="방은 청소되는 대상이므로 clean이 아니라 cleaned",
  E="by 뒤에는 주격 they가 아니라 목적격 them", F="가운데 자리는 been이 아니라 being")

X(2, 39, r="진행형 수동태는 ‘be동사 + being + 과거분사’다. laugh at 같은 구동사는 한 덩어리로 움직이므로 전치사를 과거분사 바로 뒤에 두고 그 뒤에 by를 쓴다.",
  n=["being 뒤에는 과거분사 laughed를 써야 하므로", "is being laughed at 뒤에 by를 써서 바르게 바꿨으므로", "행위자 앞에는 with가 아니라 by를 쓰므로", "현재진행형을 과거로 바꿨고 at과 by의 순서도 틀렸으므로", "been이 아니라 being을 써야 하므로"],
  st="① 능동태가 현재진행형({0})이므로 수동태는 ‘{1} + being + 과거분사’다. → ② 구동사({2})는 한 덩어리다. 과거분사 바로 뒤에 전치사를 그대로 두고, 그 다음에 by를 쓴다. → ③ 정답은 {a}. 시제를 바꾼 것, 동사원형을 쓴 것, 전치사와 by의 순서를 바꾼 것은 지운다.",
  R=("are laughing", "is", "laugh at"), B=("are talking", "is", "talk about"), C=("are looking", "is", "look after"), D=("are pointing", "is", "point at"), E=("are dealing", "is", "deal with"), F=("is turning", "are", "turn off"))

X(2, 40, r="수동태는 시제에 따라 is being p.p.(진행), has been p.p.(완료)로 쓴다. be interested in처럼 by가 아닌 전치사를 쓰는 수동 표현도 있다.",
  pre=["문장별 판정: ⓐ O. 진행형 수동태. ⓑ O. 4형식의 수동태. ⓒ O. 지각동사의 수동태 + 현재분사. ⓓ X. 방은 꾸며지는 대상이므로 has been decorated. ⓔ X. be interested in. ⓕ O. 구동사 look after의 진행형 수동태."],
  k="틀린 문장은 ⓓ, ⓔ 두 개다.", n=["틀린 문장은 ⓓ, ⓔ 두 개이므로"] * 5,
  st="① 문장마다 주어가 동작을 받는 대상인지 보고 ‘be동사 + 과거분사’가 갖춰졌는지 확인한다. 진행은 being, 완료는 been이 들어간다. → ② 사역·지각동사의 수동태 뒤 형태(to부정사·현재분사)와 전치사도 본다. → ③ {0} 틀린 문장은 {a}이다.",
  R="ⓓ는 been이 빠졌고(has been decorated), ⓔ는 전치사가 틀렸다(interested in).",
  B="ⓒ는 been이 빠졌고(has been delivered), ⓓ는 원형을 그대로 썼으며(seen crossing 또는 to cross), ⓕ는 전치사가 틀렸다(interested in).",
  C="ⓓ만 틀렸다. being 뒤에는 과거분사 built를 쓴다.",
  D="ⓑ는 opened, ⓒ는 to sing(또는 singing), ⓓ는 written, ⓔ는 planted, ⓕ는 eaten으로 써야 한다. ⓐ만 옳다.",
  E="ⓑ는 widened, ⓒ는 made to clean으로 써야 하고, ⓕ는 after 뒤에 by가 빠졌다.",
  F="ⓑ는 repaired, ⓓ는 written, ⓔ는 will be completed, ⓕ는 to wait로 써야 한다.")
