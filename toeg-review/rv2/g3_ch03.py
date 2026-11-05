# 3급 CH3 명사와 관사 (21~30) 2차 감수
X(3, 21, r="셀 수 없는 명사는 단위 표현으로 센다: a loaf of bread(빵 한 덩어리), a glass of water(물 한 잔), a sheet of paper(종이 한 장), a bottle of milk(우유 한 병).",
  n=["a cup of는 ‘한 컵’이라 빵에 쓰지 않으므로", "‘빵 한 덩어리’는 a loaf of bread이므로", "a piece of는 ‘한 조각’이라 우리말과 맞지 않으므로", "a bottle of는 ‘한 병’이라 빵에 쓰지 않으므로", "a slice of는 얇게 썬 ‘한 조각’이라 우리말과 맞지 않으므로"],
  st="① 우리말에서 세는 단위를 찾는다: ‘{0}’. → ② 빈칸 뒤 명사({1})는 셀 수 없으므로 단위 표현으로 센다. 그 단위에 맞는 표현은 {2}. → ③ 정답은 {n}.",
  R=("한 덩어리", "bread", "a loaf of다"), B=("한 그릇", "soup", "a bowl of다"), C=("한 잔", "water", "a glass of다"), D=("한 장", "paper", "a sheet of다"), E=("한 조각", "cheese", "a piece of다"), F=("한 병", "milk", "a bottle of다"))
RV(3, 21, "CD", v="수정(내용)", why="정답 ⑤ 확인. 다만 오답 가운데 성립하지 않는 형태(C: a bottles of, D: a sheets of)가 있어 형태만으로 지워진다. 원문항의 오답은 모두 실제 단위 표현이다.", fix="성립하지 않는 형태의 오답을 실제 단위 표현으로")

X(3, 22, r="셀 수 있는 명사는 a/an을 붙이거나 복수형으로 쓸 수 있다. information, news, furniture, advice처럼 낱개로 나뉘지 않는 명사는 셀 수 없다.",
  n=["information은 셀 수 없는 명사이므로", "news는 -s로 끝나지만 셀 수 없는 명사이므로", "furniture는 셀 수 없는 명사이므로", "car는 a car, two cars처럼 셀 수 있으므로", "advice는 셀 수 없는 명사이므로"],
  st="① 낱말마다 a/an을 붙이거나 복수형(-s)으로 쓸 수 있는지 본다. → ② information, news, furniture, advice, homework, money처럼 낱개로 나뉘지 않는 것은 셀 수 없는 명사다. → ③ {n}만 셀 수 있다({0}).",
  R="a car, two cars", B="a pencil, two pencils", C="an apple, two apples", D="a book, two books", E="a chair, two chairs", F="a student, two students")

X(3, 23, r="명사의 복수형: 대부분 -s, -s·-x·-ch·-sh로 끝나면 -es, 자음 + y는 -ies, -f(e)는 -ves. child - children, mouse - mice처럼 불규칙하게 바뀌거나 sheep처럼 형태가 같은 명사도 있다.",
  n=["leaf의 복수형은 leaves이므로", "자음 + y로 끝나는 city는 y를 i로 바꾸고 -es를 붙이므로", "mouse의 복수형은 mice이므로", "sheep은 단수와 복수의 형태가 같으므로", "child의 복수형은 children이므로"],
  st="① 낱말 끝을 보고 규칙을 고른다. -s·-x·-ch·-sh는 -es, 자음 + y는 -ies, -f(e)는 -ves다. → ② 불규칙하게 바뀌는 명사(child - children, mouse - mice, foot - feet, tooth - teeth, man - men)와 형태가 같은 명사(sheep)는 따로 외운다. → ③ {n}만 옳다({0}).",
  R="city는 자음 + y라 cities", B="tooth는 불규칙으로 teeth", C="box는 -x로 끝나 boxes", D="shelf는 -f로 끝나 shelves", E="person의 복수는 people", F="goose는 불규칙으로 geese")
RV(3, 23, "DEF", fx=True, why="수정 예시의 정답(leaf - leaves, child - children, mouse - mice)이 원문항의 오답(leaf - leafs, child - childrens, mouse - mouses)을 바로잡은 꼴이라 원문항을 본 학생은 바로 고를 수 있었다. 정답을 다른 명사(shelf - shelves, person - people, goose - geese)로 바꿨다.")

X(3, 24, r="a/an은 뒤 낱말의 철자가 아니라 첫소리로 정한다. 모음 소리 앞에는 an(an honest boy, an hour), 자음 소리 앞에는 a(a hospital, a university)를 쓴다.",
  n=["honest는 모음 소리로 시작해 an, hospital은 자음 소리로 시작해 a이므로", "an과 a가 서로 바뀌었으므로", "hospital 앞에 an을 쓸 수 없으므로", "honest 앞에 a를 쓸 수 없으므로", "셀 수 있는 단수 명사 boy 앞에 some을 쓰지 않으므로"],
  st="① a/an은 뒤 낱말의 철자가 아니라 첫 ‘소리’로 정한다. 모음 소리 앞에는 an, 자음 소리 앞에는 a다. → ② (A) 뒤의 {0}. (B) 뒤의 {1}. → ③ 정답은 {n}.",
  R=("honest는 h가 소리 나지 않아 모음 소리로 시작한다(an)", "hospital은 자음 소리 /h/로 시작한다(a)"), B=("European은 /j/ 소리로 시작한다(a)", "empty는 모음 소리로 시작한다(an)"),
  C=("university는 /j/ 소리로 시작한다(a)", "apple은 모음 소리로 시작한다(an)"), D=("unusual은 모음 소리로 시작한다(an)", "book은 자음 소리로 시작한다(a)"),
  E=("hour는 h가 소리 나지 않아 모음 소리로 시작한다(an)", "bike는 자음 소리로 시작한다(a)"), F=("one-way는 /w/ 소리로 시작한다(a)", "umbrella는 모음 소리로 시작한다(an)"))

X(3, 25, r="식사·운동 이름과 by + 교통수단에는 관사를 쓰지 않는다. 셀 수 없는 명사 앞에는 a/an을 쓰지 않는다. 악기와 하나뿐인 것 앞에는 the를 쓴다.",
  pre=["문장별 판정: ⓐ X. 식사 이름 앞에는 관사를 쓰지 않는다(had breakfast). ⓑ O. expensive가 모음 소리로 시작하므로 an. ⓒ X. salt는 셀 수 없어 a를 쓰지 않는다. ⓓ O. 악기 앞에는 the를 쓴다."],
  n=["ⓐ가 틀렸으므로", "ⓐ와 ⓒ가 모두 틀렸으므로", "ⓑ와 ⓓ가 모두 옳으므로", "ⓒ가 틀렸으므로", "ⓒ가 틀렸으므로"],
  st="① 문장마다 명사 앞 관사를 본다. 식사·운동 이름, by + 교통수단, 셀 수 없는 명사 앞에는 a/an을 쓰지 않는다. → ② 악기와 하나뿐인 것(the sun, the moon) 앞에는 the를 쓰고, a/an은 뒤 낱말의 첫소리로 정한다. → ③ 틀린 문장을 지운다: {0}. 남은 두 문장을 묶은 {a}가 정답이다.",
  R="ⓐ a breakfast, ⓒ a salt", B="ⓑ a honest(an honest), ⓒ by the bus(by bus)", C="ⓒ an water, ⓓ the soccer", D="ⓐ by a bus, ⓓ an rice", E="ⓑ an one-way(a one-way), ⓓ an information", F="ⓐ a apple(an apple), ⓑ by a taxi(by taxi)")
RV(3, 25, "F", fx=True, why="수정 예시의 정답 조합·위치(ⓑ, ⓓ ③)가 원문항과 같아, 문장을 바꿔 옳은 문장을 ⓒ, ⓓ(⑤)로 했다.")

X(3, 26, r="주어를 복수형으로 바꾸면 be동사도 복수형(are)으로 바꾼다. tooth - teeth, foot - feet, child - children, mouse - mice, man - men, woman - women은 불규칙 복수형이다.",
  n=["tooth의 복수형은 tooths가 아니라 teeth이므로", "teeth are로 명사와 동사를 모두 복수로 바꿨으므로", "toothes라는 형태는 없고 is도 단수이므로", "toothes라는 형태는 없고 was는 단수 과거형이므로", "teeths라는 형태는 없고 am도 쓸 수 없으므로"],
  st="① 주어 명사({0})를 복수형으로 바꾼다. 불규칙 변화다({1}). → ② 주어가 복수가 되었으므로 be동사도 is에서 are로 바꾼다. → ③ 정답은 {a}.",
  R=("tooth", "tooth → teeth"), B=("foot", "foot → feet"), C=("child", "child → children"), D=("mouse", "mouse → mice"), E=("man", "man → men"), F=("woman", "woman → women"))

X(3, 27, r="셀 수 없는 명사의 수량은 ‘수량 + 단위 + of + 명사’로 나타낸다(a glass of water). 문장은 ‘주어 + 동사 + 목적어’ 순서로 쓴다.",
  n=["a가 glass 앞에 와야 하므로", "주어 + 동사 + a glass of water 순서로 바르게 배열했으므로", "a가 동사 need 앞에 놓였으므로", "water of a glass는 단위와 명사의 순서가 뒤바뀌었으므로", "평서문인데 동사가 주어 앞에 놓였으므로"],
  st="① 주어({0})와 동사({1})를 먼저 놓는다. → ② 목적어는 ‘수량 + 단위 + of + 명사’ 순서다: {2}. → ③ 이 순서대로 놓인 {n}을 고른다.",
  R=("I", "need", "a glass of water"), B=("I", "drank", "two glasses of juice"), C=("I", "need", "a piece of cheese"), D=("She", "bought", "a bottle of milk"), E=("We", "need", "two sheets of paper"), F=("Tom", "bought", "a loaf of bread"))

X(3, 28, r="breakfast, lunch, dinner 같은 식사 이름은 관사 없이 쓰고 복수형으로 만들지 않는다(have lunch).",
  n=["식사 이름은 복수형으로 쓰지 않으므로", "식사 이름 앞에는 the도 쓰지 않으므로", "식사 이름은 관사 없이 lunch로 쓰므로", "식사 이름은 복수형으로 쓰지 않으므로", "식사 이름은 복수형으로 쓰지 않으므로"],
  st="① 밑줄({0})의 명사는 식사 이름이다. → ② 식사 이름(breakfast, lunch, dinner)은 관사 없이, 복수형으로 만들지 않고 쓴다. → ③ 관사도 -s도 없는 {a}가 정답이다.",
  R="a lunch", B="a dinner", C="a breakfast", D="a dinner", E="the lunch", F="a breakfast")
RV(3, 28, "BCDEF", fx=True, why="수정 예시의 오답 가운데 영어에 없는 형태(an dinner, an breakfast, lunchs 등)가 있어, 원문항의 오답처럼 실제 형태(the ~, ~s, some ~s, any ~s)로 바꿨다.")

X(3, 29, r="수단을 나타내는 ‘by + 교통·통신 수단’에는 관사를 쓰지 않는다(by boat, by phone). 소유격이 붙으면 on her bike처럼 on을 쓴다.",
  pre=["문장별 판정: (가) X. by boat로 써야 한다. (나) O. by phone. (다) O. on her bike. (라) X. by truck으로 써야 한다."],
  n=["(가)가 틀렸으므로", "(가)가 틀렸으므로", "(나)와 (다)가 모두 옳으므로", "(라)가 틀렸으므로", "(라)가 틀렸으므로"],
  st="① 밑줄은 모두 수단을 나타낸다. ‘by + 교통·통신 수단’에는 관사를 쓰지 않는다(by bus, by phone). → ② ‘걸어서’는 on foot이고, 소유격이 붙으면 on her bike처럼 쓴다. → ③ 틀린 문장을 지운다: {0}. 남은 두 문장을 묶은 {a}가 정답이다.",
  R="(가) by a boat, (라) by the truck", B="(나) by the phone, (라) on a foot", C="(가) by the car, (나) by a taxi", D="(나) by the bus, (다) by a plane", E="(다) by a train, (라) on feet", F="(가) by the ship, (다) by an email")

X(3, 30, r="하나뿐인 것(the sun)과 악기 앞에는 the를 쓴다. 식사 이름과 by + 교통수단에는 관사를 쓰지 않는다. 하루의 시간대는 in the morning/afternoon/evening으로 쓴다.",
  n=["하나뿐인 sun 앞에 the를 쓴다는 옳은 설명이므로", "식사 이름 앞에는 관사를 쓰지 않는다는 옳은 설명이므로", "by + 교통수단에는 관사를 쓰지 않는다는 옳은 설명이므로", "악기 이름 앞에는 the를 쓴다는 옳은 설명이므로", "시간대는 in the evening으로 쓰고 a를 쓰지 않으므로"],
  st="① 밑줄마다 관사가 맞는지 본다. 하나뿐인 것·악기·시간대(in the morning)에는 the, 식사·운동 이름과 by + 교통수단에는 관사를 쓰지 않는다. → ② 설명이 이 규칙과 맞는지 견준다. → ③ {n}의 설명이 틀렸다. {0}",
  R="시간대 앞에는 a가 아니라 the를 쓴다(in the evening). 지문의 ⓔ In a evening도 틀린 표현이다.", B="sun은 하나뿐이라 a sun이 아니라 the sun이다.", C="식사 이름 dinner 앞에는 관사를 쓰지 않는다.",
  D="운동 이름 tennis 앞에는 the를 쓰지 않는다.", E="by + 교통수단에는 관사를 쓰지 않는다. by train이 맞다.", F="운동 이름 basketball 앞에는 the를 쓰지 않는다.")
RV(3, 30, "CEF", fx=True, why="수정 예시의 지문이 원문항(43단어)의 절반에 못 미쳐(17~19단어), 밑줄 친 표현은 그대로 두고 지문을 원문항 수준으로 늘렸다.")
