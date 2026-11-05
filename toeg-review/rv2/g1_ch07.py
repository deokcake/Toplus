# 1급 CH7 분사 (61~70) 2차 감수
X(1, 61, r="감정을 나타내는 분사는 감정을 느끼는 대상을 설명하면 과거분사(-ed), 감정을 일으키는 대상을 설명하면 현재분사(-ing)를 쓴다.",
  n=["(A)는 교사들이 기쁨을 느낀 것이므로 Pleasing이 아니라 Pleased를 써야 하므로", "(B)는 아이가 좌절감을 느낀 것이므로 frustrating이 아니라 frustrated를 써야 하므로", "교사들이 기쁨을 느끼고(Pleased) 아이가 좌절감을 느낀(frustrated) 것이므로",
     "두 빈칸 모두 감정을 느끼는 쪽이라 -ing가 아니라 -ed를 써야 하므로", "felt 뒤에는 동사원형 frustrate가 아니라 분사가 와야 하므로"],
  st="① 빈칸의 분사가 설명하는 대상을 찾는다. (A)는 주절의 주어({0}), (B)는 문장의 주어({1})다. → ② 둘 다 감정을 일으키는 쪽이 아니라 느끼는 쪽이므로 과거분사(-ed)를 쓴다. → ③ 두 빈칸이 모두 -ed인 {a}를 고른다.",
  R=("the teachers", "The child"), B=("we", "Leo"), C=("Mina", "Tom"), D=("the team", "Jane"), E=("the coach", "The child"), F=("passengers", "Mina"))

X(1, 62, r="‘with + 목적어 + 분사’는 ‘~가 …한 채로’라는 뜻이다. 목적어가 동작을 스스로 하면 현재분사(-ing), 동작을 당하면 과거분사를 쓴다. 분사 자리에 형용사(open)도 올 수 있다.",
  n=["눈은 감기는 대상이라 과거분사 closed가 알맞으므로", "창문이 열려 있는 상태를 형용사 open으로 나타냈으므로", "개가 스스로 누워 있으므로 현재분사 lying이 알맞으므로", "다리는 꼬이는 대상이라 과거분사 crossed가 알맞으므로",
     "팔은 접히는 대상이라 folding이 아니라 과거분사 folded를 써야 하므로"],
  st="① 보기마다 with 뒤의 명사와 분사의 관계를 따진다. 명사가 그 동작을 스스로 하면 -ing, 당하면 과거분사다. → ② {0} → ③ 따라서 {n}은 과거분사({1})로 고쳐야 한다.",
  R=("눈·다리·팔은 사람이 감고 꼬고 접는 대상이고, 개는 스스로 눕는다. 그런데 ⑤만 당하는 대상인 arms 뒤에 folding을 썼다.", "folded"),
  B=("발·TV·머리·커튼은 동작을 당하는 대상이고, 고양이는 스스로 잔다. 그런데 ④만 당하는 대상인 hair 뒤에 tying을 썼다.", "tied"),
  C=("다리·손·모자·전화기는 동작을 당하는 대상이고, 새들은 스스로 노래한다. 그런데 ②만 당하는 대상인 hands 뒤에 folding을 썼다.", "folded"),
  D="① 보기마다 with 뒤의 명사와 분사의 관계를 따진다. 명사가 그 동작을 스스로 하면 -ing, 당하면 과거분사다. → ② 라디오는 스스로 소리를 내고 손은 스스로 놓여 있으며, 안경과 책은 놓인 대상이다. 그런데 ③은 담요가 그를 덮고 있는데 covered를 썼다. → ③ 따라서 {n}은 현재분사(covering)로 고쳐야 한다.",
  E=("가방·전화기·눈은 동작을 당하는 대상이고, 펜은 스스로 움직인다. 그런데 ⑤만 당하는 대상인 arms 뒤에 crossing을 썼다.", "crossed"),
  F=("가방·코트·모자는 동작을 당하는 대상이고, 눈은 스스로 내리며 부모님은 스스로 지켜본다. 그런데 ③만 당하는 대상인 coats 뒤에 zipping을 썼다.", "zipped up"))
RV(1, 62, "E", fx=True, why="수정 예시의 ① with her notebook opened는 보통 open(형용사)으로 써서 틀린 표현으로 볼 여지가 있었다. 분명한 과거분사 표현(with her bag hung on the chair)으로 바꿨다.")

X(1, 63, r="분사구문의 일이 주절보다 먼저 일어났으면 Having + 과거분사, 거기에 주어가 그 일을 당했으면 Having been + 과거분사를 쓴다.",
  n=["Damaging은 능동이라 ‘작품이 손상을 입혔다’는 뜻이 되므로", "Having damaged는 능동의 완료형이라 수동의 뜻을 나타내지 못하므로", "Being damaged는 주절과 같은 때의 일로 읽혀, 지난주에 먼저 일어난 일을 나타내지 못하므로",
     "지난주에 먼저 일어났고 작품이 손상을 당한 것이므로 Having been damaged가 알맞으므로", "To be damaged는 to부정사라 분사구문이 아니므로"],
  st="① (1)과 (2)의 때를 견준다. (1)({0})이 (2)({1})보다 먼저 일어난 일이다. → ② (1)의 주어는 동작을 당한 쪽({2})이다. 먼저 일어난 수동의 일이므로 Having been + 과거분사를 쓴다. → ③ 능동형(-ing, Having + 과거분사)과 Being + 과거분사, to부정사를 지운다. 정답은 {n}.",
  R=("was damaged ~ last week", "is now being restored", "손상된 작품"), B=("was destroyed ~ years ago", "is being rebuilt now", "파괴된 다리"), C=("was hidden for decades", "was recently discovered", "숨겨져 있던 원고"),
  D=("was damaged in the earthquake", "is now under repair", "손상된 건물"), E=("were deleted", "were later recovered", "삭제된 파일"), F=("was stolen", "has finally been returned", "도난당한 그림"))
RV(1, 63, "BCDEF", fx=True, why="수정 예시에 영어에 없는 형태의 오답 ‘Been + 과거분사 …’가 남아 있었다. 원문항처럼 현재분사(-ing) 오답(Destroying by … 등)으로 바꿨다.")

X(1, 64, r="분사구문을 부사절로 바꿀 때는 두 일의 관계(때, 이유, 조건, 동시 동작)에 맞는 접속사를 고른다. 이유를 나타내는 분사구문을 although(양보)로 바꾸면 뜻이 달라진다.",
  n=["숙제를 끝낸 뒤 잠자리에 든 것이므로 After로 바르게 바꿨으므로", "피곤해서 낮잠을 자기로 한 것이므로 Because로 바르게 바꿨으므로", "길을 걷던 중에 친구를 본 것이므로 While로 바르게 바꿨으므로",
     "의사이기 때문에 건강에 대해 많이 아는 것인데 Although(~이지만)로 바꿔 뜻이 달라졌으므로", "지갑을 잃어버려서 돈을 낼 수 없었던 것이므로 Since로 바르게 바꿨으므로"],
  st="① 보기마다 분사구문과 주절이 어떤 관계인지(먼저 일어난 일, 이유, 동시에 일어난 일, 조건) 가른다. → ② 화살표 뒤의 접속사가 그 관계와 맞는지 본다. → ③ {n}은 {0}",
  R="‘의사라서 건강에 대해 잘 안다’는 이유의 관계인데 Although(~이지만)를 써서 뜻이 달라졌다.",
  B="‘돈이 모자라서 신발을 살 수 없었다’는 이유의 관계인데 Although(~이지만)를 써서 뜻이 달라졌다.",
  C="‘무슨 말을 할지 몰라서 잠자코 있었다’는 뜻인데 Not을 빼고 Though를 써서 ‘알았지만 잠자코 있었다’로 뜻이 바뀌었다.",
  D="‘강가를 걸으면서 이야기했다’는 동시 동작인데 Because(~ 때문에)를 써서 뜻이 달라졌다.",
  E="‘더 열심히 공부하면 합격할 것이다’는 조건의 관계인데 Although(~이지만)를 써서 뜻이 달라졌다.",
  F="‘답을 알아서 손을 들었다’는 이유의 관계인데 Before(~하기 전에)를 써서 뜻이 달라졌다.")

X(1, 65, r="분사구문의 부정은 분사 앞에 not을 두고, 먼저 일어난 수동의 일은 Having been + 과거분사로 쓴다. ‘with + 명사 + 분사’에서 명사가 동작을 당하면 과거분사를 쓴다. 분사구문의 숨은 주어는 주절의 주어와 같아야 한다.",
  pre=["문장별 판정: a) O. Not + 분사. b) O. Having been + 과거분사. c) O. 지각동사 + 목적어 + 현재분사. d) X. 일이 끝난 것이므로 completed를 써야 한다. e) O. Weather permitting(날씨가 허락하면). f) X. 학교에 걸어가는 것은 the heavy rain이 아니므로 주어가 맞지 않는다."],
  k="옳은 문장은 a), b), c), e) 네 개다.",
  n=["옳은 문장은 a), b), c), e) 네 개이므로"] * 5,
  st="① 문장마다 분사와 그 의미상 주어의 관계(능동·수동)를 확인하고, 분사구문의 숨은 주어가 주절의 주어와 같은지 본다. → ② {0} → ③ 옳은 문장을 세면 {a}이다.",
  R="d)는 task가 끝내지는 대상이라 completed여야 하고, f)는 Walking의 주어가 the heavy rain이 되어 틀렸다. 나머지 네 문장은 옳다.",
  B="b)는 Mina가 선발된 것이므로 Having been selected여야 하고, f)는 Driving의 주어가 the traffic jam이 되어 틀렸다. 나머지 네 문장은 옳다.",
  C="f)만 틀렸다. Tom이 놀란 것이므로 Surprising이 아니라 Surprised여야 한다. 나머지 다섯 문장은 옳다.",
  D="d)만 틀렸다. 창문이 깨진 상태이므로 break가 아니라 broken이어야 한다. 나머지 다섯 문장은 옳다.",
  E="c)는 지각동사 saw의 목적격 보어로 played가 아니라 play(playing)가 와야 하고, e)는 Weather permitting이어야 하며, f)는 Walking의 주어가 a rainbow가 되어 틀렸다. 옳은 문장은 a), b), d) 셋이다.",
  F="f)만 틀렸다. Running의 주어가 the bus가 되어 맞지 않는다. 나머지 다섯 문장은 옳다.")

X(1, 66, r="부사절을 분사구문으로 바꿀 때는 접속사와 (주절과 같은) 주어를 지우고 동사를 -ing형으로 바꾼다. 진행형의 being은 생략해 -ing형만 남긴다.",
  n=["feel은 ‘느끼다’라는 능동의 뜻이라 수동형 Being felt를 쓸 수 없으므로", "접속사와 주어를 지우고 was feeling을 Feeling으로 바르게 바꿨으므로", "과거분사 Felt는 수동의 뜻이라 맞지 않으므로", "접속사 Because를 남긴 채 being feeling이라는 틀린 형태를 썼으므로",
     "형용사 ill을 명사 illness로 바꿔 뜻이 달라졌으므로"],
  st="① 부사절에서 접속사(Because)와 주절과 같은 주어를 지운다. → ② 남은 동사({0})를 분사로 바꾼다. {1}. → ③ 주절은 그대로 둔다. 접속사가 남았거나 분사의 모양이 다른 보기를 지우면 정답은 {n}.",
  R=("was feeling", "진행형의 was(being)는 생략하고 Feeling만 남긴다"), B=("had finished", "주절보다 앞선 때이므로 Having finished가 된다"), C=("felt", "능동이므로 Feeling이 된다"),
  D=("did not know", "부정어 Not을 분사 앞에 두어 Not knowing이 된다"), E=("was surprised", "수동이므로 (Being) surprised가 되고 Being은 생략할 수 있다"), F=("was worried", "be동사를 Being으로 바꿔 Being worried가 된다"))
RV(1, 66, "F", fx=True, why="수정 예시의 오답 ③ ‘Been worried, …’는 영어에 없는 형태라 ‘To be worried, …’로 바꿨다.")

X(1, 67, r="분사로 된 관용 표현은 뜻과 함께 익힌다: frankly speaking(솔직히 말하면), generally speaking(일반적으로 말하면), strictly speaking(엄밀히 말하면), speaking of(~ 이야기가 나와서 말인데), judging from(~로 판단하건대), considering (that)(~을 고려하면).",
  n=["Speaking of는 ‘~ 이야기가 나와서 말인데’라는 뜻이므로", "Strictly speaking은 ‘엄밀히 말하면’이라는 뜻이므로", "Judging from은 ‘~로 판단하건대’라는 뜻이므로", "Considering that은 ‘~을 고려하면’이라는 뜻이므로", "Frankly speaking이 ‘솔직히 말하면’이라는 뜻이므로"],
  st="① 빈칸 옆의 우리말 뜻({0})을 확인한다. → ② 그 뜻의 분사 관용 표현을 고른다: {1}. → ③ 빈칸 뒤와 이어 읽어 확인한다. {2}",
  R=("솔직히 말하면", "Frankly speaking", "‘솔직히 말하면, 꽤 지루했다.’로 자연스럽다."), B=("일반적으로 말하면", "Generally speaking", "‘일반적으로 말하면, 3월 말에는 따뜻해진다.’로 자연스럽다."),
  C=("~ 이야기가 나와서 말인데", "Speaking of", "뒤에 명사 concerts가 이어져 ‘콘서트 이야기가 나와서 말인데’가 된다."), D=("엄밀히 말하면", "Strictly speaking", "‘엄밀히 말하면, 그 용어는 완전히 정확하지는 않다.’로 자연스럽다."),
  E=("~로 판단하건대", "Judging from", "뒤에 명사구 the current results가 이어져 ‘현재 결과로 판단하건대’가 된다."), F=("~을 고려하면", "Considering", "뒤에 명사구 the heavy traffic이 이어져 ‘교통 체증을 고려하면’이 된다."))

X(1, 68, r="get + 목적어 + 과거분사는 ‘(남을 시켜) ~이 …되게 하다’라는 뜻이고, 사역동사 have + 사람 + 동사원형은 ‘~에게 …하게 하다’라는 뜻이다. 목적어가 동작을 당하면 과거분사, 스스로 하면 동사원형을 쓴다.",
  n=["(A)는 양복이 세탁되는 것이므로 clean이 아니라 cleaned를 써야 하므로", "(B)는 점원이 직접 끝내는 것이므로 finished가 아니라 finish를 써야 하므로", "(A)는 양복이 세탁되는 것이므로 cleaning을 쓸 수 없으므로",
     "get + 사물 뒤와 have + 사람 뒤에 to부정사를 쓰지 않으므로", "양복은 세탁되므로 cleaned, 점원은 직접 끝내므로 finish가 알맞으므로"],
  st="① (A) 앞의 목적어({0})는 동작을 당하는 사물이므로 get + 목적어 뒤에 과거분사를 쓴다. → ② (B) 앞의 목적어({1})는 동작을 직접 하는 사람이고 앞의 동사가 사역동사 have이므로 동사원형을 쓴다. → ③ ‘과거분사 - 동사원형’ 순서인 {a}를 고른다.",
  R=("my suit", "the clerk"), B=("my hair", "the stylist"), C=("my laptop", "the technician"), D=("this jacket", "the tailor"), E=("the brakes", "the mechanic"), F=("these roses", "the florist"))

X(1, 69, r="부사절을 분사구문으로 바꿀 때는 접속사를 생략하고, 두 절의 주어가 다르면 부사절의 주어를 남기며, 동사를 분사로 바꾼다. 부정어 not은 분사 앞에 둔다.",
  n=["접속사를 생략하는 것은 옳은 설명이므로", "부사절의 주어 자리에 있는 there가 주절의 주어 we와 달라 남긴다는 것은 옳은 설명이므로", "was가 주절의 decided와 같은 때라 being으로 바꾼다는 것은 옳은 설명이므로",
     "there가 분사구문의 주어 자리를 지켜 생략하지 않는다는 것은 옳은 설명이므로", "부정어 not은 분사 앞에 두어 There not being으로 써야 하는데 There being not이라고 했으므로"],
  st="① 부사절을 분사구문으로 바꾸는 차례를 떠올린다. 접속사를 생략하고, 주어가 다르면 남기고, 동사를 분사로 바꾼다. → ② 제시문에 적용하면 다음과 같다. {0} → ③ 이 결과나 규칙과 어긋나는 설명은 {n}이다. {1}",
  R=("There being no taxi available, we decided to walk home.", "부정어 not은 분사 앞에 두므로 There not being이 옳은 순서다."),
  B=("There being little time left, we skipped lunch.", "there는 부사절의 주어 자리에 있고 주절의 주어 we와 다르므로 생략할 수 없다."),
  C=("No seats being available, we stood at the back.", "being은 주어의 수와 관계없이 쓰며, been은 혼자서 분사구문을 만들지 못한다."),
  D=("No buses running, Mina called a taxi.", "진행형 were running은 being을 생략하고 running만 남긴다. being running이라고 쓰지 않는다."),
  E=("No one answering the phone, Tom sent an email.", "주어가 다른데 no one을 빼면 Tom이 전화를 받았다는 뜻이 되어 버린다."),
  F=("No lights being on, Jane assumed nobody was home.", "불이 꺼져 있던 것은 주절(assumed)과 같은 때이므로 having been이 아니라 being을 쓴다."))
RV(1, 69, "B", v="수정(내용)", why="정답 ② 확인. 보기가 ‘접속사는 생략할 수 있다’처럼 제시문과 무관한 짧은 일반 규칙이어서, 제시문을 분사구문으로 바꾸는 과정을 설명하는 원문항보다 보기 수준이 낮다(B3). C~F에서 지적한 것과 같은 문제다.", fix="제시문을 바꾸는 과정을 단계별로 설명하는 보기로")

X(1, 70, r="주절과 주어가 다른 분사구문(독립분사구문)은 의미상 주어를 분사 앞에 밝혀 쓴다. 완료 수동은 ‘주어 + having been + 과거분사’이며, 분사구문 뒤에 so 같은 접속사를 붙이지 않는다.",
  n=["Being 뒤에 finish를 쓸 수 없고 주어도 밝히지 않았으므로", "주절의 주어 we와 다른 All the tasks를 밝히고 having been completed를 바르게 썼으므로", "분사구문 뒤에 접속사 so를 붙였으므로", "There being no more questions가 되어야 하는데 having을 썼으므로",
     "be over(끝나다)이므로 The movie being over가 되어야 하는데 having over라고 썼으므로"],
  st="① 조건 두 가지를 형태로 바꾼다. 분사가 있어야 하고, 주절과 다른 주어는 분사 바로 앞에 와야 한다(‘주어 + 분사 ~, 주절’). → ② 분사의 모양이 틀렸거나, 분사구문 뒤에 접속사(so, and, but)를 붙였거나, 주어의 자리가 틀린 보기를 지운다. → ③ 남는 {n}은 {0}",
  R="주어 All the tasks 뒤에 완료 수동의 분사 having been completed를 바르게 썼다.", B="주어 All the guests 뒤에 완료의 분사 having arrived를 바르게 썼다.", C="주어 The weather 뒤에 완료의 분사 having improved를 바르게 썼다.",
  D="There being ~으로 ‘~이 있어서’를 나타내는 독립분사구문을 바르게 썼다.", E="주어 The work 뒤에 완료 수동의 분사 having been completed를 바르게 썼다.", F="주어 Mina 뒤에 분사 being을 바르게 썼다.")
RV(1, 70, "B", v="수정(표기)", why="정답 ⑤ 확인. <조건>을 ‘/’로 이어 써서 원문항(한 줄에 하나씩, ‘-’ 표시)과 표기가 다르다.", fix="<조건>을 한 줄에 하나씩")
RV(1, 70, "F", fx=True, why="수정 예시의 오답 ④ ‘Mina was absent, Tom leading the meeting.’은 독립분사구문으로 성립하는 옳은 문장이라 조건을 만족해 정답이 둘이 될 수 있었다. ‘Mina being absent, so Tom led the meeting.’으로 바꿨다.")
