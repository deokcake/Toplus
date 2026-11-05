# 7급 CH1 명사 (1~10) 2차 감수
X(7, 1, r="하나, 둘 셀 수 있는 것은 셀 수 있는 명사다. 물질(water, bread, milk, rice, money)이나 눈에 보이지 않는 것(love)은 셀 수 없는 명사다.",
  n=["한 마리, 두 마리 셀 수 있으므로", "한 개, 두 개 셀 수 있으므로", "눈에 보이지 않는 감정이라 셀 수 없으므로", "한 개, 두 개 셀 수 있으므로", "한 권, 두 권 셀 수 있으므로"],
  st="① 보기마다 앞에 ‘한 개, 두 개’를 붙여 본다. → ② 붙일 수 없는 것을 찾는다. {0} → ③ 정답은 {a}.",
  R="love(사랑)는 형태가 없어 셀 수 없다.", B="bread(빵)는 덩어리로 된 물질이라 셀 수 없다.", C="rice(쌀·밥)는 물질이라 셀 수 없다.", D="milk(우유)는 액체라 셀 수 없다.", E="money(돈)는 셀 수 없는 명사다(동전·지폐를 센다).",
  F="water(물)는 액체라 셀 수 없다.")

X(7, 2, r="사람·도시·나라 이름, 요일, 달, 언어 이름 같은 고유명사는 언제나 대문자로 시작한다.",
  n=["일반 명사라 소문자로 쓰므로", "일반 명사라 소문자로 쓰므로", "도시 이름이라 Seoul로 써야 하므로", "일반 명사라 소문자로 쓰므로", "일반 명사라 소문자로 쓰므로"],
  st="① 보기마다 ‘세상에 하나뿐인 이름’인지 본다(사람, 도시, 나라, 요일, 달, 언어). → ② {0} → ③ 정답은 {a}.",
  R="seoul은 도시 이름이다(Seoul).", B="friday는 요일 이름이다(Friday).", C="jane은 사람 이름이다(Jane).", D="january는 달 이름이다(January).", E="korea는 나라 이름이다(Korea).", F="english는 언어 이름이다(English).")
RV(7, 2, "F", v="수정(내용)", why="정답 ⑤ monday 유일 확인. 다만 정답의 종류(요일 이름)와 정답 위치(⑤)가 B(friday)와 같다(유형 간 중복). 발문도 원문항과 다르다.", fix="정답을 다른 종류의 고유명사로, 발문을 원문항대로")

X(7, 3, r="셀 수 없는 명사(water, bread, money, rice)는 복수형으로 쓰지 않고 수를 붙이지 않는다(some water). 셀 수 있는 명사는 둘 이상일 때 복수형으로 쓴다.",
  n=["셀 수 없는 명사 water를 some과 바르게 썼으므로", "셀 수 있는 명사를 복수형 boxes로 바르게 썼으므로", "셀 수 있는 명사를 복수형으로 바르게 썼으므로", "money는 셀 수 없는 명사라 three를 붙이거나 복수형으로 쓰지 않으므로", "셀 수 없는 명사 bread를 some과 바르게 썼으므로"],
  st="① 밑줄 친 명사가 셀 수 있는지 없는지 가른다. → ② 셀 수 없는 명사에 수나 -s가 붙었는지, 셀 수 있는 명사가 수 뒤에서 복수형인지 본다. → ③ {0} 정답은 {n}.",
  R="④ money는 셀 수 없다(some money).", B="⑤ rice는 셀 수 없다(some rice).", C="③ bread는 셀 수 없다(some bread).", D="① homework는 셀 수 없다(some homework).", E="③ pencil은 four 뒤에서 pencils여야 한다.",
  F="⑤ book은 many 뒤에서 books여야 한다.")
RV(7, 3, "B", v="수정(내용)", why="정답 ⑤ 유일 확인. 다만 보기 세 개(some water, two boxes, apples)가 원문항 문장에서 주어만 바꾼 것이고, ②(some rice)와 정답 ⑤(five rices)가 같은 명사의 옳은 꼴·틀린 꼴이어서 둘만 견주면 답이 나온다. 발문도 달라지고 밑줄이 없다.", fix="겹치는 문장과 짝 문장을 바꾸고, 발문·밑줄을 원문항대로")
RV(7, 3, "E", fx=True, why="수정 예시의 ①(They want some bread.)이 원문항 ⑤(We want some bread.)와 거의 같아 다른 명사(soup)로 바꿨다.")

X(7, 4, r="복수형: 대부분 -s, s·sh·ch·x로 끝나면 -es(watches, boxes, dishes), 자음 + y는 y를 i로 바꾸고 -es(babies).",
  n=["ch로 끝나 -es를 붙인 옳은 형태이므로", "x로 끝나 -es를 붙인 옳은 형태이므로", "-s를 붙인 옳은 형태이므로", "sh로 끝나 -es를 붙여 dishes로 써야 하므로", "-s를 붙인 옳은 형태이므로"],
  st="① 명사의 끝 글자를 본다: s, sh, ch, x인지, 자음 + y인지. → ② 그 끝에 맞게 -es나 -ies가 붙었는지 본다. → ③ {0} 정답은 {a}.",
  R="dish는 sh로 끝나므로 dishes다.", B="bus는 s로 끝나므로 buses다.", C="baby는 자음 + y이므로 babies다.", D="bench는 ch로 끝나므로 benches다.", E="city는 자음 + y이므로 cities다.", F="brush는 sh로 끝나므로 brushes다.")
RV(7, 4, "D", v="수정(내용)", why="정답 ③ 유일 확인. 다만 정답(box - boxs)이 원문항 ②(box - boxes)의 틀린 꼴이고, ①(watch - watches)은 원문항 ①과 똑같으며 ⑤(dish - dishes)는 원문항 정답을 바르게 고친 짝이다.", fix="원문항에 없는 명사로 새로")
RV(7, 4, "F", v="수정(내용)", why="정답 ① 유일 확인. 다만 정답(watch - watchs)이 원문항 ①(watch - watches)의 틀린 꼴이고, ⑤(box - boxes)는 원문항 ②와 똑같다.", fix="원문항에 없는 명사로 새로")

X(7, 5, r="불규칙 복수형은 따로 외운다: goose - geese, foot - feet, tooth - teeth, man - men, woman - women, child - children, mouse - mice. sheep, fish, deer는 단수와 복수가 같다.",
  n=["(B) goose의 복수형은 geese이므로", "(A) sheep은 복수도 sheep이므로", "sheep은 그대로, goose는 geese로 알맞으므로", "(A) sheep은 복수도 sheep이고 (B) gooses라는 형태는 없으므로", "(B) gooses라는 형태는 없으므로"],
  st="① two, three 뒤이므로 두 빈칸 모두 복수형이 필요하다. → ② (A): {0}. (B): {1}. → ③ 정답은 {a}.",
  R=("sheep은 복수도 sheep", "goose → geese"), B=("foot → feet", "mouse → mice"), C=("woman → women", "tooth → teeth"), D=("man → men", "child → children"), E=("fish는 복수도 fish", "person → people"),
  F=("mouse → mice", "deer는 복수도 deer"))
RV(7, 5, "BCDEF", v="수정(표기)", why="정답 유일 확인. 다만 발문에 원문항에 없는 ‘(A에는 …, B에는 …의 복수형을 씁니다.)’가 붙었다. 보기만으로 어떤 낱말인지 알 수 있어 필요 없는 조건이다(같은 단원 8번과 같은 기준). B~E의 오답 fee, wome, me, fis는 낱말을 자른 꼴이라 오답 구실을 하지 못한다.", fix="조건을 지워 원문항 발문으로, 잘린 꼴 오답은 그럴듯한 형태로")

X(7, 6, r="two, many처럼 둘 이상을 나타내는 말 뒤에는 복수형을 쓴다. 대부분 -s를 붙인다(cat → cats).",
  n=["two 뒤에 단수형을 쓸 수 없으므로", "two 뒤에 복수형 cats를 바르게 썼으므로", "cat에는 -s만 붙이므로", "two 뒤에 a를 쓸 수 없으므로", "cattes라는 형태는 없으므로"],
  st="① 빈칸 앞의 {0}를 본다. 둘 이상이므로 복수형이 필요하다. → ② 단수형과 a가 붙은 것을 지우고, 복수형 철자를 확인한다: {1}. → ③ 정답은 {a}.",
  R=("two", "cat + s"), B=("three", "book + s"), C=("many", "leaf → leaves(f를 v로 바꾸고 -es)"), D=("two", "watch + es(ch로 끝남)"), E=("two", "baby → babies(자음 + y)"), F=("five", "box + es(x로 끝남)"))
RV(7, 6, "BDEF", v="수정(내용)", why="정답 유일 확인. 다만 제시 문장(I have two ____.)이 원문항과 글자까지 똑같다. 명사만 바꾼 문항이다.", fix="제시 문장을 새로")

X(7, 7, r="셀 수 없는 명사(bread, milk, water, rice, money)는 a/an을 붙이지 않고 복수형으로도 쓰지 않는다.",
  n=["bread는 셀 수 없어 복수형으로 쓰지 않으므로", "bread 앞에 an을 쓸 수 없으므로", "bread는 복수형으로 쓰지 않으므로", "bread를 a/an이나 -s 없이 바르게 썼으므로", "bread 앞에 a를 쓸 수 없고 복수형도 아니므로"],
  st="① 목적어({0})는 셀 수 없는 명사다. → ② a/an이 붙은 문장과 -s가 붙은 문장을 모두 지운다. → ③ 명사만 쓴 문장은 {n}.",
  R="bread", B="money", C="salt", D="water", E="milk", F="rice")
RV(7, 7, "C", v="수정(내용)", why="정답 ③ 유일 확인. 다만 information은 7급 수준을 넘는 낱말이다(같은 단원 3번 D에서 advice·information을 지적한 것과 같은 기준). 발문에도 원문항에 없는 조건이 붙었다.", fix="7급 수준의 명사로, 발문을 원문항대로")

X(7, 8, r="two, four 같은 수 뒤의 명사는 복수형으로 쓴다. 대부분 -s, s·sh·ch·x로 끝나면 -es를 붙인다(box → boxes).",
  n=["two와 four 뒤에 단수형을 쓸 수 없으므로", "(B) box는 x로 끝나 boxes로 써야 하므로", "(A) two 뒤에 단수형 bag을 쓸 수 없으므로", "(A) bag에는 -s만 붙이고 (B) boxes로 써야 하므로", "bags, boxes 모두 바른 복수형이므로"],
  st="① 두 빈칸 모두 수를 나타내는 말 뒤이므로 복수형이 필요하다. → ② (A): {0}. (B): {1}. → ③ 정답은 {n}.",
  R=("bag + s", "box + es(x로 끝남)"), B=("pen + s", "class + es(s로 끝남)"), C=("dog + s", "watch + es(ch로 끝남)"), D=("book + s", "dish + es(sh로 끝남)"), E=("apple + s", "bus + es(s로 끝남)"),
  F=("baby → babies(자음 + y)", "watch + es(ch로 끝남)"))
RV(7, 8, "BCDE", v="수정(내용)", why="정답 유일 확인. 다만 제시 문장(I have two (A)___ and four (B)___.)이 원문항과 글자까지 똑같고, B는 (A)의 낱말(bag)도 원문항과 같다. 발문에도 원문항에 없는 조건이 붙었다.", fix="제시 문장을 새로, 발문을 원문항대로")
RV(7, 8, "F", fx=True, why="변형의 보기에 원문항의 (A)·(B) 표지가 없다. 수정 예시에서 ‘(A) babies - (B) watches’처럼 표지를 붙였다.")

X(7, 9, r="a/an은 뒤 낱말의 첫소리로 정한다. 모음 소리(a, e, i, o, u)로 시작하면 an, 자음 소리로 시작하면 a다.",
  n=["apple은 모음 소리로 시작해 an을 써야 하므로", "ruler는 자음 소리로 시작해 a를 써야 하므로", "pencil, ruler에는 a, apple에는 an이 알맞으므로", "pencil에는 a, apple에는 an, ruler에는 a를 써야 하므로", "pencil은 자음 소리로 시작해 a를 써야 하므로"],
  st="① 빈칸마다 뒤 낱말의 첫소리를 본다: {0}. → ② 모음 소리면 an, 자음 소리면 a를 넣는다. → ③ 정답은 {a}.",
  R="pencil(자음), apple(모음), ruler(자음)", B="egg(모음), uniform(‘유’ 소리, 자음), hour(h가 소리 나지 않아 모음)", C="onion(모음), carrot(자음), tomato(자음)", D="ant(모음), owl(모음), fox(자음)",
  E="notebook(자음), ruler(자음), eraser(모음)", F="tiger(자음), elephant(모음), eagle(모음)")
RV(7, 9, "CDEF", v="수정(내용)", why="정답 유일 확인. 다만 제시 문장이 원문항의 틀(Mina has (A) ~, (B) ~, and (C) ~.)에서 명사만 바꾼 것이고, D와 F에는 원문항의 명사(apple)도 그대로 있다. C는 정답 조합(an - a - an)이 B와 같다.", fix="제시 문장을 새로")

X(7, 10, r="주어가 I·you·복수이면 have, 나나 너가 아닌 한 명(he, she, 사람 이름, my brother)이면 has를 쓴다. a/an은 첫소리로 정한다.",
  n=["an이 ‘하나’를 나타낸다는 옳은 설명이므로", "모음 소리 앞에 an을 쓴다는 옳은 설명이므로", "3인칭 단수 주어에 has를 쓴다는 옳은 설명이므로", "주어가 He이면 have가 아니라 has를 써야 하므로", "자음 소리 앞에 a를 쓴다는 옳은 설명이므로"],
  st="① <보기> 두 문장의 주어·동사·관사를 먼저 확인한다: {0}. → ② 학생의 말마다 실제로 바꿔 써 보거나 규칙에 대어 본다. → ③ {1} 정답은 {n}.",
  R=("(가) I have an ~, (나) My brother has a ~", "준호: 주어가 He이면 has다."), B=("(가) She has an ~, (나) We have two ~", "지수: 주어가 We이면 have다."), C=("(가) I have a ~, (나) Tom has an ~", "민수: banana 앞에는 a를 쓴다."),
  D=("(가) She has an ~, (나) They have two ~", "민수: 주어가 He이면 has다."), E=("(가) He has a ~, (나) They have some ~", "민아: 두 자루면 two pencils다."), F=("(가) I have an ~, (나) Jane has two ~", "성진: 주어가 I이면 have다."))
RV(7, 10, "BCDEF", v="수정(내용)", why="정답 유일 확인. 다만 틀린 설명과 정반대인 옳은 설명이 함께 있어 둘만 견주면 답이 나온다(B: an을 써 ↔ a를 써야 해, C: has를 써 ↔ have를 써야 해, D: They는 have ↔ They로 바꿔도 has, E: 셀 수 없는 ↔ 셀 수 있으므로, F: 복수형 books ↔ 단수형으로). 진술도 원문항의 절반 길이다.", fix="원문항 길이의 설명으로, 정반대 짝 없이")
