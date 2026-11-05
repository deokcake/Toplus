# 2급 CH12 접속사 (111~120) 2차 감수
X(2, 111, r="상관접속사: both A and B(둘 다), either A or B(둘 중 하나), neither A nor B(둘 다 아님), not only A but also B(A뿐 아니라 B도), not A but B(A가 아니라 B), whether A or B(A이든 B이든).",
  n=["Either - or는 ‘둘 중 하나’라는 뜻이므로", "Both는 and와 짝을 이루므로", "Not - but은 ‘A가 아니라 B’라는 뜻이므로", "Not - also라는 짝은 없으므로", "Neither - nor가 ‘A도 B도 아니다’라는 뜻이므로"],
  st="① 우리말에서 두 대상의 관계를 읽는다: ‘{0}’. → ② 그 뜻의 상관접속사는 {1}. → ③ 짝이 맞지 않는 것(Both - but, Neither - and 등)과 뜻이 다른 것을 지운다. 정답은 {n}.",
  R=("Jane도 나도 ~않는다(둘 다 아님)", "Neither A nor B다"), B=("Tom이 오든 Mina가 오든(어느 쪽이든)", "Whether A or B다"), C=("Jane과 Leo 둘 다", "Both A and B다"), D=("너나 내가(둘 중 하나)", "Either A or B다"),
  E=("Tom뿐만 아니라 Mina도", "Not only A but also B다"), F=("Jane이 아니라 그녀의 친구들이", "Not A but B다"))

X(2, 112, r="although + 절(주어 + 동사)은 in spite of(despite) + 명사(구)로 바꿔 쓸 수 있다. 뜻은 ‘~에도 불구하고’(양보)다.",
  n=["Because of는 ‘~ 때문에’라는 원인이라 뜻이 반대이므로", "In spite of가 ‘~에도 불구하고’라는 양보의 전치사이므로", "Due to는 ‘~ 때문에’라는 원인이므로", "Thanks to는 ‘~ 덕분에’라는 뜻이므로", "Owing to는 ‘~ 때문에’라는 원인이므로"],
  st="① 첫 문장의 접속사 Although는 ‘~이지만’이라는 양보다. → ② 둘째 문장은 빈칸 뒤가 절이 아니라 명사구({0})다. 명사 앞에는 접속사가 아니라 전치사를 쓴다. → ③ 양보의 뜻을 지닌 전치사 {a}가 정답이다. 원인의 전치사(because of 등)는 뜻이 반대다.",
  R="the heavy rain", B="the icy roads", C="her tiredness", D="the rain", E="his nervousness", F="the heavy traffic")

X(2, 113, r="목적격 관계대명사 that은 생략할 수 있다. 진주어·보어·주어·동격절을 이끄는 접속사 that과 주격 관계대명사 that은 생략하지 않는다.",
  n=["It ~ that의 진주어절을 이끄는 접속사라 생략하지 않으므로", "보어절을 이끄는 접속사라 생략하지 않으므로", "It ~ that의 진주어절을 이끄는 접속사라 생략하지 않으므로", "built의 목적어 구실을 하는 목적격 관계대명사라 생략할 수 있으므로", "보어절을 이끄는 접속사라 생략하지 않으므로"],
  st="① 밑줄 친 that 뒤의 절이 완전한지 본다. 완전하면 접속사, 주어나 목적어가 빠져 있으면 관계대명사다. → ② 관계대명사라면 that 뒤에 ‘주어 + 동사’가 바로 오는지 본다. 그렇다면 목적격이라 생략할 수 있다. 동사가 바로 오면 주격이라 생략할 수 없다. → ③ {n}만 목적격 관계대명사다({0}).",
  R="the building (that) I built", B="the bag (that) I bought", C="The song (that) Mina sang", D="The cake (that) my mom made", E="The book (that) I read", F="the phone (that) you lost")

X(2, 114, r="when, if, until, after, before가 이끄는 시간·조건의 부사절에서는 미래의 일도 현재형으로 쓴다.",
  n=["so ~ that 구문으로 올바르므로", "조건의 if절에 현재완료를 써서 올바르므로", "since(~ 이래로)와 현재완료를 써서 올바르므로", "because로 이유를 바르게 나타냈으므로", "시간 부사절에는 will을 쓸 수 없다. when I arrive로 써야 하므로"],
  st="① 문장마다 접속사를 찾고 그 절의 시제를 본다. → ② 시간·조건의 부사절(when, if, until, after, before)에 will이 있으면 어색하다. 현재형으로 써야 한다. → ③ {n}: {0}.",
  R="when I will arrive → when I arrive", B="when I will reach → when I reach", C="If it will snow → If it snows", D="until the bus will come → until the bus comes", E="After the movie will end → After the movie ends",
  F="Before the sun will set → Before the sun sets")

X(2, 115, r="either A or B는 B에 수를 맞춘다. 목적어절의 that은 생략할 수 있다. so that은 목적(~하도록)이다. as + 명사는 ‘~로서’라는 전치사다. despite 뒤에는 명사만 온다. too ~ to는 so ~ that … can't로 바꾼다.",
  pre=["학생별 판정: Leo O(B인 she에 맞춰 is). Maya X(heard 뒤 목적어절의 that은 생략할 수 있어 옳은 문장이다). Nick O(so that은 목적). Olivia X(as a teacher의 as는 전치사다). Paul X(Despite 뒤에는 절이 올 수 없다). Quinn O(too ~ to = so ~ that … can't)."],
  k="올바르게 설명한 학생은 Leo, Nick, Quinn이다.", n=["올바르게 설명한 학생은 Leo, Nick, Quinn이므로"] * 5,
  st="① 학생마다 예문이 옳은지와 설명이 옳은지를 따로 본다. → ② 기준: 상관접속사는 B에 수 일치(both A and B는 복수), 목적어절 that은 생략 가능, despite·because of 뒤는 명사, although·because 뒤는 절, so that은 목적이다. → ③ {0} 옳게 설명한 학생만 모으면 {a}이다.",
  R="Maya는 생략할 수 있는 that을 생략할 수 없다고 했고, Olivia는 전치사 as를 접속사라고 했으며, Paul은 Despite 뒤에 절을 쓸 수 있다고 했다. 셋 다 틀렸다.",
  B="Ben은 that이 생략된 옳은 문장을 틀렸다고 했고, Dan은 despite 뒤에 절이 와도 된다고 했으며, Eva는 both A and B를 단수 취급한다고 했다. 셋 다 틀렸다.",
  C="Hank는 said 뒤에 that을 반드시 써야 한다고 했고, Jake는 because of 뒤에 절이 와도 된다고 했으며, Liam은 not only A but also B가 A에 수 일치한다고 했다. 셋 다 틀렸다.",
  D="Mia는 both A and B 뒤에 am을 쓴다고 했고, Owen은 so that을 ‘결과’라고 했으며, Pia는 Although 대신 Despite를 써도 된다고 했다. 셋 다 틀렸다.",
  E="Uma는 동격의 that을 생략할 수 있다고 했고, Vic은 unless 뒤에 not을 또 쓴다고 했으며, Will은 ‘~ 이래로’의 Since를 이유라고 했다. 셋 다 틀렸다.",
  F="Adam은 that man의 that(지시형용사)을 접속사라고 했고, Bella는 because 뒤에 명사가 와도 된다고 했으며, Eli는 both A and B를 단수 취급한다고 했다. 셋 다 틀렸다.")
RV(2, 115, "CD", fx=True, why="수정 예시의 정답이 네 명(C)이거나 두 명(D)이고 보기 조합의 인원도 섞여 있어, 원문항(모두 세 명 조합)과 달랐다. 학생 한 명의 설명을 바꿔 정답을 세 명으로 하고 보기를 모두 세 명 조합으로 맞췄다.")

X(2, 116, r="either A or B, neither A nor B, not only A but also B가 주어이면 동사는 B에 수를 맞춘다. both A and B는 복수 동사를 쓴다.",
  n=["Either A or B는 B(he)에 수를 맞추므로 is가 알맞으므로", "am은 주어가 I일 때 쓰므로", "B가 he(단수)라 are를 쓸 수 없으므로", "주어 뒤 동사 자리에 원형 be를 쓸 수 없으므로", "being은 문장의 동사가 될 수 없으므로"],
  st="① 주어의 상관접속사를 확인한다: {0}. → ② {1} → ③ 정답은 {a}. be, being은 문장의 동사가 될 수 없다.",
  R=("Either A or B", "동사는 가까운 B(he)에 맞춘다. 3인칭 단수다."), B=("Either A or B", "동사는 가까운 B(I)에 맞춘다."), C=("Neither A nor B", "동사는 가까운 B(his friends)에 맞춘다. 복수다."),
  D=("Not only A but also B", "동사는 B(the teacher)에 맞춘다. 단수다."), E=("Both A and B", "두 사람을 합친 복수이므로 복수 동사를 쓴다."), F=("Either A or B", "동사는 가까운 B(the coach)에 맞춘다. 단수다."))
RV(2, 116, "F", fx=True, why="수정 예시의 정답(is)과 위치(①)가 원문항과 같아, 보기 순서를 바꿔 정답 위치를 ②로 옮겼다.")

X(2, 117, r="so + 형용사/부사 + that + 주어 + 동사는 ‘너무 ~해서 …하다’는 결과를 나타낸다.",
  n=["so + 형용사(scary) + that + 주어 + 동사 순서로 바르게 배열했으므로", "so가 be동사 앞에 놓였으므로", "So가 문장 맨 앞에 놓였으므로", "scary so that은 ‘~하도록’이라는 목적의 뜻이 되어 맞지 않으므로", "that이 주어 I 뒤에 놓였으므로"],
  st="① 우리말 ‘너무 ~해서 …하다’는 so ~ that 구문이다. → ② ‘주어 + 동사’ 뒤에 so + {0}를 놓고, 이어서 that + 결과의 절({1})을 둔다. → ③ so와 that 사이에 형용사·부사만 있는 {n}을 고른다. ‘형용사 + so that’은 목적의 뜻이 되어 틀린다.",
  R=("형용사(scary)", "I couldn't sleep"), B=("형용사(difficult)", "many students couldn't finish it"), C=("부사(heavily)", "the game was canceled"), D=("형용사(tired)", "she fell asleep early"),
  E=("형용사(dark)", "I couldn't see anything"), F=("부사(quickly)", "I couldn't understand him"))

X(2, 118, r="A as well as B가 주어이면 동사는 A에 수를 맞춘다. not only A but also B는 B에 맞춘다.",
  n=["A as well as B는 A(My parents, 복수)에 수를 맞추므로 are가 알맞으므로", "A가 복수라 is를 쓸 수 없으므로", "am은 주어가 I일 때 쓰므로", "being은 문장의 동사가 될 수 없으므로", "tonight의 예정을 말하고 A도 복수라 was를 쓸 수 없으므로"],
  st="① 주어의 연결어를 확인한다: {0}. → ② {1} → ③ 정답은 {a}.",
  R=("A as well as B", "동사는 A(My parents)에 맞춘다. 복수다. 가까운 my brother에 속지 않는다."), B=("A as well as B", "동사는 A(Tom)에 맞춘다. 단수다. 가까운 his friends에 속지 않는다."),
  C=("Not only A but also B", "동사는 B(her parents)에 맞춘다. 복수다."), D=("A as well as B", "동사는 A(The teacher)에 맞춘다. 단수다. 가까운 the students에 속지 않는다."),
  E=("A as well as B", "동사는 A(My sister)에 맞춘다. 단수다. 가까운 I에 속지 않는다."), F=("Not only A but also B", "동사는 B(I)에 맞춘다."))

X(2, 119, r="‘언제 ~할지’라는 뜻의 when절(명사절)에는 미래의 일에 will을 쓴다. ‘~할 때’라는 뜻의 when절(시간 부사절)에는 미래의 일도 현재형으로 쓴다.",
  n=["(A)는 부사절이 아니라 know의 목적어인 명사절이므로", "(B)는 명사절이 아니라 시간의 부사절이므로", "(A)는 명사절이라 will을 쓸 수 있고 (B)는 부사절이라 현재형을 쓴다고 바르게 설명했으므로", "부사절인 (B)에는 will을 쓸 수 없으므로", "의지와 확정된 미래로 나뉘는 것이 아니므로"],
  st="① when절이 문장에서 하는 일을 본다. (A)는 동사({0})의 목적어다. ‘언제 ~할지’라는 명사절이다. → ② (B)의 when절은 없어도 문장이 성립한다. ‘~할 때’라는 시간 부사절이다. → ③ 명사절에는 will을 쓸 수 있고, 시간 부사절에는 현재형({1})을 쓴다. 이 둘을 바르게 말한 {n}을 고른다.",
  R=("know", "comes"), B=("wonder", "arrives"), C=("Tell", "arrives"), D=("know", "finishes"), E=("tell", "calls"), F=("knows", "stops"))
RV(2, 119, "B", v="수정(내용)", why="정답 ③ 확인. 정답만 (A)·(B)를 견주는 긴 설명이고 오답은 ‘when이 있으면 언제나 will을 생략한다.’ 같은 짧은 한 줄이라 형식으로 답이 드러난다(C4). 원문항의 보기는 다섯 개 모두 (A)·(B)를 짚는 긴 설명이다.", fix="오답도 (A)·(B)를 짚는 그럴듯한 설명으로")

X(2, 120, r="조건절(unless)의 주절에는 will을 쓰고 동사 형태를 맞춘다. 시제는 앞뒤가 맞아야 한다. because 뒤에는 절, because of 뒤에는 명사가 온다. 명령문은 동사원형으로 시작한다. neither A nor B는 B에 수를 맞춘다.",
  pre=["문장별 판정: ⓐ X. 주어 you에 passes를 쓸 수 없다(you won't pass). ⓑ X. 과거의 일이므로 finished. ⓒ X. 명사 앞이므로 because of. ⓓ X. 명령문은 동사원형 Do로 시작한다. ⓔ O. B(my sister)에 맞춰 is."],
  k="올바르지 않은 문장은 ⓐ, ⓑ, ⓒ, ⓓ 네 개다.", n=["올바르지 않은 문장은 ⓐ, ⓑ, ⓒ, ⓓ 네 개이므로"] * 5,
  st="① 문장마다 접속사를 찾아 그 뒤가 절인지 명사인지, 시제가 맞는지 본다. 시간·조건의 부사절에는 will을 쓰지 않는다. → ② 상관접속사 주어는 B에 수를 맞춘다(both A and B는 복수). → ③ {0} 올바르지 않은 문장은 {a}이다.",
  R="ⓐ는 passes, ⓑ는 finishes(시제), ⓒ는 because + 명사, ⓓ는 Does가 틀렸다. ⓔ만 옳다.", B="ⓒ는 when I arrive, ⓓ는 are coming으로 써야 한다.",
  C="ⓐ는 If it rains, ⓑ는 Although와 but을 함께 쓸 수 없고, ⓓ는 are absent로 써야 한다.", D="ⓒ는 until Tom comes, ⓔ는 are working으로 써야 한다.",
  E="ⓔ만 틀렸다. when Dad gets home으로 써야 한다.", F="ⓑ는 Although Tom was nervous, ⓒ는 are presenting, ⓔ는 after I arrive로 써야 한다.")
RV(2, 120, "D", fx=True, why="수정 예시의 정답(4개, ④)이 원문항의 정답 개수·위치와 같아, ⓐ·ⓓ를 옳은 문장으로 되돌려 2개(②)로 했다.")
