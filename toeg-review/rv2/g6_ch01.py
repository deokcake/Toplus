# 6급 CH1 명사와 관사 (1~10) 2차 감수
X(6, 1, r="복수형 규칙: 자음 + y → -ies(babies), s·x·sh·ch → -es(dishes), f/fe → -ves(wolves). foot - feet, child - children처럼 불규칙형과 sheep처럼 단수·복수가 같은 명사도 있다.",
  n=["자음 + y라 y를 i로 바꾸고 -es를 붙인 옳은 형태이므로", "sh로 끝나 -es를 붙인 옳은 형태이므로", "f를 v로 바꾸고 -es를 붙인 옳은 형태이므로", "foot의 복수형은 불규칙형 feet이므로", "sheep은 단수와 복수가 같으므로"],
  st="① 규칙대로 변하는 짝(-s, -es, -ies, -ves)을 먼저 확인한다. → ② 남은 짝은 불규칙 명사다. 불규칙 명사에 -s를 붙인 것을 찾는다. → ③ {0} 정답은 {n}.",
  R="foot의 복수형은 feet이다.", B="child의 복수형은 children이다.", C="tooth의 복수형은 teeth다.", D="woman의 복수형은 women이다.", E="man의 복수형은 men이다.", F="mouse의 복수형은 mice다.")
RV(6, 1, "E", v="수정(내용)", why="정답 ⑤ 유일 확인. 다만 보기 두 개(③ dish - dishes, ④ baby - babies)가 원문항 ②·①과 똑같다. 발문에도 mouse의 뜻 설명이 붙었다.", fix="겹치는 보기를 다른 명사로, 발문을 원문항대로")
RV(6, 1, "F", fx=True, why="④ foot - feet은 원문항 정답(foot - foots)을 바르게 고친 짝이라 원문항과 겹친다. 수정 예시에서 다른 명사(goose - geese)로 바꿨다.")

X(6, 2, r="a/an은 셀 수 있는 명사의 단수형 앞에만 쓴다. water처럼 셀 수 없는 명사 앞에는 쓰지 않는다.",
  n=["셀 수 있는 명사라 a 뒤에 쓸 수 있으므로", "셀 수 있는 명사라 a 뒤에 쓸 수 있으므로", "셀 수 있는 명사라 a 뒤에 쓸 수 있으므로", "셀 수 없는 명사라 a 뒤에 쓸 수 없으므로", "셀 수 있는 명사라 a 뒤에 쓸 수 있으므로"],
  st="① 빈칸 앞에 a가 있으므로 빈칸에는 셀 수 있는 명사의 단수형만 들어간다. → ② 보기 가운데 하나, 둘 셀 수 없는 것(물질·추상 명사)을 찾는다. → ③ {0} 정답은 {n}.",
  R="water는 일정한 모양이 없는 물질이라 셀 수 없다.", B="advice는 추상적인 것이라 셀 수 없다(a piece of advice).", C="bread는 물질이라 셀 수 없다(a piece of bread).", D="money는 셀 수 없는 명사다.", E="rice는 물질이라 셀 수 없다.",
  F="milk는 물질이라 셀 수 없다(a glass of milk).")
RV(6, 2, "CDEF", v="수정(내용)", why="정답 확인. 다만 제시 문장(I need a ____.)이 원문항과 똑같고 F는 보기(box, pen)도 원문항과 겹친다. 정답 낱말만 바꾼 문항이다. 발문에도 원문항에 없는 말이 붙었다.", fix="제시 문장을 새로, 발문을 원문항대로")

X(6, 3, r="세상에 하나뿐인 것(the sun, the moon, the sky, the world) 앞에는 the를 쓴다. 처음 말하는 셀 수 있는 단수명사 앞에는 a/an, 서로 아는 대상 앞에는 the를 쓴다.",
  n=["달은 하나뿐이라 the moon으로 써야 하므로", "모음 소리로 시작하는 elephant 앞에 an을 바르게 썼으므로", "특정한 소녀들을 가리켜 The를 바르게 썼으므로", "특정한 자전거를 가리켜 The를 바르게 썼으므로", "셀 수 있는 단수명사 dog 앞에 a를 바르게 썼으므로"],
  st="① 밑줄 뒤의 명사를 본다. 세상에 하나뿐인 것이면 the여야 한다. → ② 그 밖에는 a/an이 첫소리와 맞는지 본다. → ③ {0} 정답은 {n}.",
  R="①의 moon은 하나뿐인데 a를 썼다.", B="④의 sun은 하나뿐인데 a를 썼다.", C="③의 world는 하나뿐인데 a를 썼다.", D="②의 sky는 하나뿐인데 a를 썼다.", E="⑤의 sun은 하나뿐인데 A를 썼다.", F="①의 sky는 하나뿐인데 a를 썼다.")

X(6, 4, r="처음 말하는 셀 수 있는 단수명사 앞에는 a/an(모음 소리 앞에서 an), 앞에서 말한 것을 다시 가리킬 때는 the를 쓴다.",
  n=["apple은 모음 소리로 시작해 A를 쓸 수 없고 둘째도 the여야 하므로", "apple은 모음 소리로 시작해 A를 쓸 수 없으므로", "처음 말하는 apple 앞에 An, 다시 가리키는 apple 앞에 The가 알맞으므로", "처음 말하는 사과에는 The를 쓰지 않으므로", "‘그 사과’는 앞에서 말한 것이라 The를 써야 하므로"],
  st="① 첫째 빈칸: {0}. → ② 둘째 빈칸: {1}. → ③ 정답은 {a}.",
  R=("처음 말하는 apple, 모음 소리 → An", "앞에서 말한 ‘그 사과’ → The"), B=("처음 말하는 girl, 자음 소리 → A", "처음 말하는 apple, 모음 소리 → an"), C=("hour는 h를 발음하지 않아 모음 소리 → an", "앞에서 말한 ‘그 책’ → The"),
  D=("처음 말하는 bird, 자음 소리 → a", "앞에서 말한 ‘그 새’ → The"), E=("처음 말하는 book, 자음 소리 → A", "앞에서 말한 ‘그 책’ → The"), F=("처음 말하는 dog, 자음 소리 → A", "앞에서 말한 ‘그 개’ → The"))

X(6, 5, r="a/an은 철자가 아니라 첫소리로 정한다. hour, honest는 h를 발음하지 않아 an, university, uniform, useful, European은 /j/ 소리로 시작해 a를 쓴다.",
  n=["igloo는 모음 소리로 시작해 an이 맞으므로", "hour는 h를 발음하지 않아 an hour로 써야 하므로", "하나뿐인 sky 앞에 the를 바르게 썼으므로", "악기 이름 앞에 the를 바르게 썼으므로", "second는 자음 소리로 시작해 a가 맞으므로"],
  st="① a/an 뒤 낱말의 첫 ‘소리’를 본다. 철자와 소리가 다른 낱말(h를 발음하지 않는 낱말, ‘유’로 소리 나는 u·eu)을 살핀다. → ② {0} → ③ 정답은 {n}.",
  R="hour는 ‘아워’로 모음 소리라 an hour다.", B="European은 ‘유’ 소리로 시작해 a European이다.", C="useful은 ‘유’ 소리로 시작해 a useful tool이다.", D="honest는 h를 발음하지 않아 an honest man이다.",
  E="university는 ‘유’ 소리로 시작해 a university다.", F="uniform은 ‘유’ 소리로 시작해 a uniform이다.")

X(6, 6, r="셀 수 있는 단수명사 앞에 a/an을 쓴다. 뒤 낱말이 모음 소리로 시작하면 an, 자음 소리로 시작하면 a다.",
  n=["orange는 모음 소리로 시작해 a를 쓸 수 없으므로", "모음 소리로 시작하는 orange 앞에 an을 쓰므로", "two 뒤에는 복수형 oranges가 와야 하므로", "be동사는 명사 앞 빈칸에 올 수 없으므로", "be동사는 명사 앞 빈칸에 올 수 없으므로"],
  st="① 빈칸 뒤가 단수명사({0})이므로 a나 an이 필요하다. be동사와 복수를 나타내는 말을 지운다. → ② {0}의 첫소리는 {1}. → ③ 정답은 {a}.",
  R=("orange", "모음 소리"), B=("banana", "자음 소리"), C=("apple", "모음 소리"), D=("sandwich", "자음 소리"), E=("egg", "모음 소리"), F=("umbrella", "모음 소리"))

X(6, 7, r="milk, water, bread, rice 같은 물질 명사는 셀 수 없으므로 a/an을 붙이지 않고 복수형으로도 쓰지 않는다.",
  n=["셀 수 없는 명사 milk 앞에 a를 쓰지 않으므로", "milk를 관사 없이 단수형으로 바르게 썼으므로", "milk는 자음 소리로 시작하고 셀 수도 없으므로", "셀 수 없는 명사는 복수형으로 쓰지 않으므로", "was와 일반동사 drink를 함께 쓸 수 없으므로"],
  st="① 우리말의 목적어({0})는 셀 수 없는 명사다. a/an이나 -s가 붙은 문장을 지운다. → ② 남은 문장에서 동사의 형태(주어와의 일치, be동사를 겹쳐 쓰지 않았는지)를 본다. → ③ 정답은 {n}.",
  R="우유 milk", B="밥 rice", C="빵 bread", D="물 water", E="주스 juice", F="음악 music")

X(6, 8, r="There are, ten, two처럼 둘 이상을 나타내는 말 뒤에는 복수형을 쓴다. child - children, woman - women, foot - feet처럼 불규칙 복수형에 주의한다.",
  n=["ten 뒤에 단수형을 쓸 수 없으므로", "ten 뒤에 단수형을 쓸 수 없으므로", "child의 복수형 children이므로", "childs라는 형태는 없으므로", "children에 -s를 또 붙이지 않으므로"],
  st="① 빈칸 앞뒤에서 수를 나타내는 말을 찾는다: {0}. 복수형이 필요하다. → ② 단수형과 a가 붙은 것을 지운다. → ③ {1} 정답은 {a}.",
  R=("There are ten", "child의 복수형은 children이다."), B=("Four ~ are", "woman의 복수형은 women이다."), C=("several", "foot의 복수형은 feet이다."), D=("Three ~ are", "man의 복수형은 men이다."),
  E=("Several ~ are", "goose의 복수형은 geese다."), F=("two", "tooth의 복수형은 teeth다."))

X(6, 9, r="복수형: f/fe → -ves(leaves, knives), 자음 + y → -ies(babies), s·x·sh·ch → -es(boxes), 자음 + o → -es(heroes, tomatoes). 불규칙형(children)도 있다.",
  n=["wolf의 복수형 wolves로 옳으므로", "knife의 복수형 knives로 옳으므로", "leaf는 f를 v로 바꾸고 -es를 붙여 leaves로 써야 하므로", "baby의 복수형 babies로 옳으므로", "box의 복수형 boxes로 옳으므로"],
  st="① 밑줄 친 복수형마다 단수형의 끝(f/fe, 자음 + y, s·x·sh·ch, 자음 + o)을 떠올린다. → ② 그 끝에 맞는 규칙대로 바뀌었는지 본다. → ③ {0} 정답은 {n}.",
  R="leaf → leaves.", B="knife → knives.", C="hero → heroes.", D="child → children(불규칙).", E="baby → babies.", F="tomato → tomatoes.")
RV(6, 9, "D", v="수정(내용)", why="정답 ③ childs 유일 확인. 다만 같은 낱말의 바른 복수형(⑤ The children are waiting outside.)이 함께 있어 둘만 견주면 답이 나온다.", fix="⑤를 다른 명사로")

X(6, 10, r="사람 이름 같은 고유명사는 문장 어디에서나 첫 글자를 대문자로 쓴다. 보통명사는 문장 중간에서 소문자로 쓰고, s·x·sh·ch로 끝나면 복수형에 -es를 붙인다.",
  n=["David는 사람 이름이라 문장 중간에서도 대문자로 써야 하므로", "고유명사는 문장 어디에서나 대문자로 시작하므로", "boxes는 보통명사라 소문자로 쓰므로", "(B)는 보통명사라 대문자로 쓰지 않으므로", "x로 끝나면 -es를 붙여 boxes로 쓰므로"],
  st="① (A)가 무엇의 이름인지 본다: {0}. 고유명사이므로 대문자로 시작한다. → ② (B)는 보통명사의 복수형이다: {1}. 소문자로 쓴다. → ③ 이 두 가지와 맞는 설명은 {n}.",
  R=("David, 사람 이름", "box + es"), B=("Monday, 요일 이름", "class + es"), C=("English, 언어 이름", "story → stories"), D=("Seoul, 도시 이름", "tourist + s"), E=("December, 달 이름", "box + es"), F=("Christmas, 기념일 이름", "dish + es"))
RV(6, 10, "C", v="수정(내용)", why="정답 ⑤ 유일 확인. 다만 밑줄 친 말(Friday)과 설명 틀(‘문장 중간이므로 friday로’, ‘four 뒤에 오므로 chair로’, ‘요일 이름인 고유명사이므로’)이 B(Monday)와 같고 정답 위치도 같다(유형 간 중복).", fix="고유명사의 종류와 설명을 새로")
RV(6, 10, "F", v="수정(내용)", why="정답 ⑤ 유일 확인. 다만 대화가 이어지지 않고(Is Busan far from here? — Yes. I see two buses.), 밑줄 친 말이 D(Seoul)와 같은 도시 이름이며 정답 위치도 B와 같다.", fix="대화와 고유명사의 종류를 새로")
