# 2급 CH1 문장의 형식 (1~10) 2차 감수
X(2, 1, r="2형식은 ‘주어 + 동사 + 주격 보어’다. become, turn, grow, seem, look, sound, smell, stay 같은 동사 뒤의 형용사가 주어의 상태를 설명한다.",
  n=["bought 뒤에 목적어(a new book)가 오는 3형식이므로", "seems 뒤의 형용사 interesting이 주어를 설명하는 2형식이므로", "arrived 뒤에 부사구만 오는 1형식이므로", "목적어(us)와 목적격 보어(happy)가 있는 5형식이므로", "간접목적어(me)와 직접목적어(a present)가 있는 4형식이므로"],
  st="① 주어진 문장의 동사({0}) 뒤에 오는 형용사({1})가 주어의 상태를 설명한다. 2형식이다. → ② 보기에서 동사 뒤의 말을 본다. 목적어(명사)가 오면 3·4·5형식이고, 부사(구)만 오면 1형식이다. → ③ {n}만 ‘동사 + 형용사 보어’({2}) 구조다.",
  R=("turn", "red", "seems interesting"), B=("smells", "delicious", "look beautiful"), C=("became", "dark", "turned cold"), D=("sounds", "reasonable", "seems practical"), E=("grew", "sleepy", "smells sour"), F=("stayed", "quiet", "remained silent"))

X(2, 2, r="5형식은 ‘주어 + 동사 + 목적어 + 목적격 보어’다. 목적격 보어(명사, 형용사, to부정사, 분사 등)는 목적어의 이름·상태·행동을 설명한다.",
  n=["him = president 관계의 5형식이므로", "her의 성질을 honest가 설명하는 5형식이므로", "me의 상태를 crazy가 설명하는 5형식이므로", "the wall의 상태를 blue가 설명하는 5형식이므로", "want 뒤에 목적어(some pizza)만 있는 3형식이므로"],
  st="① 문장마다 동사 뒤에 ‘목적어 + 목적어를 설명하는 말’이 이어지는지 본다. → ② 목적어 뒤의 말이 목적어의 이름·상태·행동을 나타내면 5형식이다. → ③ {n}은 {0}. 5형식이 아니다.",
  R="want 뒤에 목적어 some pizza만 있는 3형식이다", B="slept 뒤에 목적어 없이 부사 peacefully만 있는 1형식이다", C="arrived 뒤에 부사 early만 있는 1형식이다", D="rose 뒤에 부사 slowly만 있는 1형식이다",
  E="stopped 뒤에 부사 suddenly만 있는 1형식이다(③·⑤의 to부정사는 목적격 보어다)", F="live 뒤에 장소 부사구 in Busan만 있는 1형식이다")

X(2, 3, r="4형식을 3형식으로 바꿀 때 buy, make, cook, get, find 같은 동사는 사람 앞에 for를, ask는 of를 쓴다(give, send, show 등은 to).",
  n=["get + 사물 + for + 사람이다. 다른 보기와 같은 for가 들어간다.", "cook + 사물 + for + 사람이다. 다른 보기와 같은 for가 들어간다.", "make + 사물 + for + 사람이다. 다른 보기와 같은 for가 들어간다.", "buy + 사물 + for + 사람이다. 다른 보기와 같은 for가 들어간다.",
     "ask a favor of + 사람으로 of가 들어간다. 나머지 넷(for)과 다르다."],
  st="① 빈칸은 ‘동사 + 사물 + 전치사 + 사람’에서 사람 앞 전치사 자리다. 문장마다 동사를 찾는다. → ② 나머지 동사({0})는 ‘~을 위해 해 주는’ 동사라 for를 쓴다. → ③ {n}의 동사 ask만 of를 쓴다({1}).",
  R=("get, cook, make, buy", "ask a favor of you"), B=("find, buy, order, make", "ask a favor of your neighbor"), C=("buy, make, reserve, cook", "ask a question of the professor"), D=("make, save, buy, bake", "ask a favor of my coach"),
  E=("make, save, buy, order", "ask one thing of you"), F=("find, cook, make, buy", "ask permission of his parents"))

X(2, 4, r="목적격 보어의 형태는 동사가 정한다. 사역동사(make, have, let)는 동사원형, 지각동사는 동사원형·-ing, want·expect는 to부정사, keep·find는 형용사를 쓴다. 부사는 목적격 보어가 될 수 없다.",
  n=["지각동사 saw + 목적어 + 현재분사로 올바르므로", "사역동사 made 뒤에는 to clean이 아니라 동사원형 clean을 써야 하므로", "found + 목적어 + 형용사로 올바르므로", "want + 목적어 + to부정사로 올바르므로", "kept + 목적어 + 형용사로 올바르므로"],
  st="① 문장마다 동사를 보고 목적격 보어의 형태를 정한다. 사역동사(make, have, let)는 동사원형, 지각동사는 동사원형·-ing, want·expect는 to부정사, keep·find는 형용사다. → ② 목적어 뒤의 말이 그 형태인지 견준다. → ③ {n}은 {0}.",
  R="사역동사 made 뒤에 to clean을 썼다. clean이 맞다", B="사역동사 made 뒤에 to stay를 썼다. stay가 맞다", C="지각동사 heard 뒤에 to perform을 썼다. perform이나 performing이 맞다", D="사역동사 let 뒤에 to play를 썼다. play가 맞다",
  E="kept + 목적어 뒤에 부사 laughingly를 썼다. laughing이 맞다", F="made + 목적어 뒤에 부사 tiredly를 썼다. 형용사 tired가 맞다")

X(2, 5, r="give·send는 3형식에서 to를 쓴다. 사역동사 have + 목적어 + 동사원형이고, 목적어와 목적격 보어가 수동 관계이면 과거분사를 쓴다. 감각동사 뒤 보어는 형용사다.",
  pre=["학생별 판정: Mary O(give의 4형식). Tom X(원형부정사를 써야 한다면서 studying으로 고치라고 했다. study가 맞다). Bruce X(send는 to를 쓰므로 문장이 옳다). Cathy O(컴퓨터는 고쳐지는 대상이라 fixed). Dave O(tastes 뒤에는 형용사 delicious)."],
  k="옳게 설명한 학생은 Mary, Cathy, Dave다.",
  n=["옳게 설명한 학생은 Mary, Cathy, Dave이므로"] * 5,
  st="① 학생마다 ‘예문이 맞는 문장인가’와 ‘설명이 맞는가’를 따로 따진다. → ② {0} → ③ 옳게 설명한 학생만 모으면 {a}이다.",
  R="Tom은 원형부정사를 써야 한다면서 studying으로 고치라고 했고, Bruce는 send에 for를 쓴다고 했다(to가 맞다). 둘 다 틀렸다.",
  B="Minho는 사역동사 made 뒤의 to wash가 맞다고 했고, Hana는 tastes 뒤의 부사 deliciously가 맞다고 했다. 둘 다 틀렸다.",
  C="Jane은 send에 for가 맞다고 했고(to가 맞다), Sally는 smell 뒤의 부사 sweetly가 맞다고 했다. 둘 다 틀렸다.",
  D="Joon은 buy에 to가 맞다고 했고(for가 맞다), Leo는 tastes 뒤에 well이 맞다고 했다. 둘 다 틀렸다.",
  E="Sora는 make에 to가 맞다고 했고(for가 맞다), Hana는 smells 뒤의 부사 sourly가 맞다고 했다. 둘 다 틀렸다.",
  F="Jane은 buy에 to가 맞다고 했고(for가 맞다), Amy는 looks 뒤의 부사 quietly가 맞다고 했다. 둘 다 틀렸다.")

X(2, 6, r="4형식(동사 + 사람 + 사물)을 3형식으로 바꾸면 ‘동사 + 사물 + 전치사 + 사람’이 된다. give, send, show, teach는 to를, buy, make는 for를 쓴다.",
  n=["전치사 + 사람이 사물 앞에 와 어순이 틀렸으므로", "to가 사물 앞에 붙어 뜻이 통하지 않으므로", "사물 + to + 사람 순서로 바르게 바꿨으므로", "give는 for가 아니라 to를 쓰므로", "어순이 뒤섞여 문장이 되지 않으므로"],
  st="① 3형식은 ‘동사 + 사물 + 전치사 + 사람’이다. 사물({0})이 동사 바로 뒤로 와야 한다. → ② 동사({1})에 맞는 전치사는 {2}다. → ③ 어순과 전치사가 모두 맞는 {n}을 고른다.",
  R=("homework", "give", "to"), B=("a package", "send", "to"), C=("a bicycle", "buy", "for"), D=("the map", "show", "to"), E=("a cake", "make", "for"), F=("English", "teach", "to"))

X(2, 7, r="1형식은 ‘주어 + 동사’만으로 뜻이 완성되는 문장이다. 뒤에 부사(구)가 붙어도 형식은 바뀌지 않는다.",
  n=["She seems tired가 2형식이므로", "두 문장 모두 주어 + 동사만으로 이루어진 1형식이므로", "I have a dog이 3형식이므로", "It smells good이 2형식이므로", "You look great가 2형식이므로"],
  st="① 문장마다 동사 뒤의 말이 부사(구)인지, 보어·목적어인지 가른다. 부사(구)는 형식에 들어가지 않는다. → ② 한 쌍에서 한 문장이라도 보어나 목적어가 있으면 지운다: {0}. → ③ 두 문장 모두 ‘주어 + 동사(+ 부사)’인 {n}이 정답이다.",
  R="① seems tired, ③ have a dog, ④ smells good, ⑤ look great", B="① gave him a pen, ② became angry, ③ bought a bag, ⑤ tastes good", C="① has a bike, ② looks tired, ④ smells nice, ⑤ kept the door open",
  D="② became dark, ③ stayed quiet, ④ made him happy, ⑤ bought lunch", E="① became a teacher, ② need help, ③ gave her flowers, ⑤ looks happy", F="② smells good, ③ found it easy, ④ became tired, ⑤ bought a book")

X(2, 8, r="목적격 보어는 목적어 뒤에서 목적어의 상태를 설명한다(find, make, keep, leave, paint + 목적어 + 형용사). 주어를 설명하는 주격 보어, 동사를 꾸미는 부사와 구별한다.",
  n=["주어(This soup)를 설명하는 주격 보어이므로", "동사 shines를 꾸미는 부사이므로", "목적어 his parents의 상태를 설명하는 목적격 보어이므로", "want의 목적어인 to부정사이므로", "주어(She)를 설명하는 주격 보어이므로"],
  st="① <보기>의 밑줄({0})은 목적어({1}) 뒤에서 그 상태를 설명하는 목적격 보어다. → ② 보기마다 밑줄이 무엇을 설명하는지 본다. 주어를 설명하면 주격 보어, 동사를 꾸미면 부사, 동사 뒤 to부정사는 목적어다. → ③ {n}의 밑줄({2})만 목적어({3})를 설명한다.",
  R=("clear", "the explanation", "proud", "his parents"), B=("yellow", "the fence", "sleepy", "the baby"), C=("nervous", "everyone", "empty", "the classroom"), D=("confusing", "the instructions", "focused", "the players"),
  E=("awake", "us", "white", "her room"), F=("open", "the door", "risky", "the plan"))
RV(2, 8, "B", v="수정(표기)", why="정답 ④ 확인. 원문항은 본문에 <보기> 표시가 있고 발문도 ‘<보기>와 같은 것’을 묻는데, 변형 본문에는 <보기> 표시가 빠져 있다.", fix="본문에 <보기> 표시 넣기")
RV(2, 8, "CDEF", fx=True, why="수정 예시 본문에도 <보기> 표시가 빠져 있어 넣었다.")

X(2, 9, r="사역동사 make + 목적어 + 원형부정사는 ‘목적어가 ~하게 하다’라는 뜻이다. 시제나 주어·목적어의 수와 관계없이 목적격 보어는 원형이다.",
  n=["made는 여기서 상태 동사가 아니라 사역동사이므로", "목적격 보어 자리에 형용사만 오는 것은 아니므로", "사역동사 make + 목적어 + 원형부정사라는 규칙을 바르게 설명했으므로", "to부정사가 과거를 뜻하지 않고 made도 현재 시제가 아니므로", "목적격 보어는 주어와 수 일치를 하지 않으므로"],
  st="① 밑줄 앞의 동사 made와 목적어({0})를 본다. ‘~에게 …하게 하다’라는 사역의 뜻이다. → ② 사역동사 make의 목적격 보어는 원형부정사다. 밑줄에서 to를 뺀 동사원형({1})이 맞다. → ③ 이 이유를 말한 {n}을 고른다. 나머지는 {2}.",
  R=("me", "practice", "상태 동사·형용사·시제·수 일치 같은 관계없는 규칙을 댔다"), B=("the team", "run", "복수형·진행형·장소 표현·3형식 같은 관계없는 이유를 댔다"), C=("me", "apologize", "자동사·대명사·시제·수 일치 같은 관계없는 이유를 댔다"),
  D=("us", "rewrite", "접두사 re-·과거형·형용사·관사 같은 관계없는 이유를 댔다"), E=("everyone", "cry", "형용사·수 일치·명사 보어·부사적 용법 같은 관계없는 이유를 댔다"), F=("the staff", "work", "부사 overtime·집합명사·상태 동사·수 일치 같은 관계없는 이유를 댔다"))
RV(2, 9, "B", v="수정(내용)", why="정답 ② 확인. 정답만 ‘~때문이다’로 끝나는 긴 설명이고 오답 넷은 짧은 단정문이라 형식만으로 답이 드러난다(C4). 원문항은 다섯 보기가 모두 ‘~때문이다’로 끝나는 설명이다.", fix="오답도 ‘~때문이다’로 끝나는 그럴듯한 설명으로")

X(2, 10, r="have/get + 사물 + 과거분사는 ‘(남을 시켜) 사물이 ~되게 하다’라는 뜻이다. 사물은 그 일을 받는 쪽이므로 과거분사를 쓰고, 조동사나 to 뒤에는 have/get의 원형을 쓴다.",
  n=["자전거는 수리되는 대상이라 repair가 아니라 repaired를 써야 하므로", "fixing이 아니라 과거분사 fixed를 써야 하므로", "had it repaired, get my bike checked 모두 ‘사물 + 과거분사’ 구조에 맞으므로", "fix가 아니라 fixed를 써야 하고 should 뒤에 having도 쓸 수 없으므로",
     "직접 고친 것이 아니라는 앞의 No와 어긋나므로"],
  st="① (A)의 it이 가리키는 것과 상황을 본다. {0} → ② (A)는 ‘have/get + it + 과거분사’({1})다. 사물은 그 일을 받는 쪽이라 동사원형이나 -ing는 쓸 수 없다. → ③ (B)는 {2} 뒤이므로 have/get의 원형이 온다. 정답은 {n}.",
  R=("직접 고쳤느냐는 물음에 No라고 했으므로 자전거(it)는 남에게 맡겨 고친 것이다.", "had it repaired", "should also"), B=("화면(it)은 수리점에서(at a repair shop) 교체된 것이다.", "got it replaced", "should"),
  C=("재킷(it)은 양복점에서(at the tailor's) 줄여진 것이다.", "had it shortened", "need to"), D=("방(it)은 칠해지는 대상이다. ⑤의 painted it도 (A)에는 쓸 수 있지만 (B)에서 걸린다.", "had it painted", "want to"),
  E=("시계(it)는 고쳐지는 대상이다. ⑤의 fixed it도 (A)에는 쓸 수 있지만 (B)에서 걸린다.", "had it fixed", "should"), F=("사진(it)은 사진관에서(at a studio) 찍힌 것이다.", "had it taken", "want to"))
