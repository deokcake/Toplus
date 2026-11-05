# 4급 CH2 대명사 (11~20) 2차 감수
X(4, 11, r="인칭대명사의 주격 - 목적격: I - me, you - you, he - him, she - her, it - it, we - us, they - them. mine, yours, hers, ours, theirs는 ‘~의 것’이라는 소유대명사다.",
  n=["주격 - 목적격의 짝이므로", "주격 - 목적격의 짝이므로", "주격 - 목적격의 짝이므로", "주격 - 목적격의 짝이므로", "hers는 목적격이 아니라 소유대명사이므로"],
  st="① 짝의 앞은 모두 주격이다. 뒤가 목적격인지 확인한다. → ② {0} → ③ 정답은 {a}.",
  R="she의 목적격은 her다. hers는 ‘그녀의 것’이라는 소유대명사다.", B="we의 목적격은 us다. ours는 소유대명사다.", C="she의 목적격은 her다. hers는 소유대명사다.", D="he의 목적격은 him이다. his는 소유격·소유대명사다.",
  E="they의 목적격은 them이다. theirs는 소유대명사다.", F="I의 목적격은 me다. mine은 소유대명사다.")

X(4, 12, r="his는 명사 앞의 소유격(his friend)이나 ‘그의 것’이라는 소유대명사(The book is his)로 쓴다. 주어 자리에는 He를 쓴다.",
  n=["주어 자리라 His가 아니라 He가 들어가야 하므로", "명사 friend 앞에 소유격 his가 들어가므로", "명사 parents 앞에 소유격 His가 들어가므로", "명사 birthday 앞에 소유격 his가 들어가므로", "‘그의 것’이라는 소유대명사 his가 들어가므로"],
  st="① his가 들어가는 자리는 둘이다: 명사 앞(소유격), 명사 없이 ‘그의 것’(소유대명사). → ② 빈칸 뒤에 명사가 있거나 ‘~의 것’으로 풀리는 문장을 지운다. → ③ {0} 정답은 {n}.",
  R="①은 빈칸 뒤가 동사 is라 주어 자리다. ‘그는 내 가장 친한 친구다’이므로 He가 들어간다.", B="②는 빈칸 뒤가 am이라 주어 I만 들어갈 수 있다.", C="⑤는 빈칸 뒤가 am이라 주어 I만 들어갈 수 있다.", D="⑤는 빈칸 뒤가 am이라 주어 I만 들어갈 수 있다.",
  E="①은 빈칸 뒤가 am이라 주어 I만 들어갈 수 있다.", F="②는 빈칸 뒤가 am이라 주어 I만 들어갈 수 있다.")
RV(4, 12, "BCDEF", v="수정(내용)", why="정답 확인. 다만 정답 문장이 ‘_____ am ~’이라 his를 몰라도 am만 보고 고를 수 있고, 다섯 유형이 모두 같은 방식이다. 원문항의 정답 문장(_____ is my best friend.)은 동사만으로는 가려지지 않는다.", fix="정답 문장을 he나 him이 들어가는 문장으로")

X(4, 13, r="동사·전치사 뒤 목적어 자리에는 목적격(me, him, her, us, them)을 쓴다. 명사 없이 ‘~의 것’은 소유대명사로 쓰며 '를 붙이지 않는다. ‘누구의’는 Whose다.",
  n=["my's라는 형태는 없고 ‘내 것’은 mine이라 바르게 고쳤으므로", "소유대명사 theirs에는 '를 붙이지 않아 바르게 고쳤으므로", "‘누구의’는 Who's(= Who is)가 아니라 Whose라 바르게 고쳤으므로", "전치사 to 뒤에는 목적격 her를 써야 하는데 소유대명사 hers로 고쳤으므로", "명사 없이 ‘내 것’은 mine이라 바르게 고쳤으므로"],
  st="① 고친 말이 그 자리에 맞는지 본다: 명사 앞이면 소유격, 명사가 없으면 소유대명사, 동사·전치사 뒤면 목적격. → ② {0} → ③ 정답은 {n}.",
  R="④는 전치사 to 뒤라 목적격 her가 와야 하는데 소유대명사 hers로 고쳤다.", B="③은 전치사 to 뒤라 목적격 him이 와야 하는데 his로 고쳤다.", C="①은 동사 helped 뒤라 목적격 me가 와야 하는데 mine으로 고쳤다.",
  D="④는 동사 called 뒤라 목적격 him이 와야 하는데 his로 고쳤다.", E="③은 동사 saw 뒤라 목적격 them이 와야 하는데 theirs로 고쳤다.", F="②는 전치사 to 뒤라 목적격 us가 와야 하는데 ours로 고쳤다.")
RV(4, 13, "D", fx=True, why="수정 예시의 틀리게 고친 보기(she → hers, ④)가 원문항의 정답 보기와 내용·위치까지 같아, they → their(⑤)로 바꿨다.")

X(4, 14, r="news, information, advice와 학문 이름(mathematics)은 단수 취급한다. pants, scissors, glasses처럼 짝을 이루는 물건과 police는 복수 취급한다.",
  n=["information은 셀 수 없는 명사라 is가 맞으므로", "news는 -s로 끝나지만 단수 취급해 is를 써야 하므로", "pants는 복수 취급해 look이 맞으므로", "advice는 셀 수 없는 명사라 is가 맞으므로", "scissors는 복수 취급해 are가 맞으므로"],
  st="① 주어 명사를 둘로 가른다: 단수 취급(news, information, advice, 학문 이름), 복수 취급(짝을 이루는 물건, police). → ② 밑줄 친 동사가 그에 맞는지 본다. {0} → ③ 정답은 {n}.",
  R="news는 -s로 끝나도 단수 취급하므로 are가 아니라 is다.", B="mathematics는 학문 이름이라 단수 취급한다. ④의 are가 틀렸다.", C="news는 단수 취급한다. ③의 are가 틀렸다.", D="scissors는 복수 취급한다. ④의 is가 틀렸다.",
  E="pants는 복수 취급한다. ③의 is가 틀렸다.", F="police는 복수 취급한다. ②의 is가 틀렸다.")

X(4, 15, r="pants는 복수 취급한다. 소유는 사람이면 's(-s로 끝나는 복수명사는 '만), 사물이면 of로 나타낸다.",
  pre=["문장별 판정: ⓐ X. pants는 복수 취급하므로 look. ⓑ O. of로 소유를 나타냈다. ⓒ O. my uncle's house. ⓓ X. 버스 두 대의 문이므로 buses' doors."],
  n=["ⓑ와 ⓒ가 모두 옳으므로", "ⓐ가 틀렸으므로", "ⓐ, ⓓ가 모두 틀렸으므로", "ⓓ가 틀렸으므로", "ⓓ가 틀렸으므로"],
  st="① 주어와 동사의 수가 맞는지 본다(pants·shoes는 복수, news는 단수, this/that + 단수, these/those + 복수). → ② 소유 표현을 본다(사람은 's, -s로 끝나는 복수명사는 ', 사물은 of). → ③ {0} 옳은 문장만 고른 {a}가 정답이다.",
  R="ⓐ looks(look), ⓓ bus's(buses')가 틀렸다.", B="c Those shoes is(are), d This pants(These pants)가 틀렸다.", C="a looks(look), d These book is(This book is), e This shoes(These shoes)가 틀렸다.",
  D="b The news are(is), d Those bag is(That bag is)가 틀렸다.", E="b her(hers), d That shoes(Those shoes)가 틀렸다.", F="c These car is(This car is), e The news are(is)가 틀렸다.")
RV(4, 15, "C", fx=True, why="수정 예시의 ⓐ~ⓒ가 원문항 문장과 거의 같은 채로 남아 있어(Those pants looks ~, The name of the ~, I stay at my aunt ~) 세 문장을 새로 썼다.")

X(4, 16, r="명사 없이 ‘~의 것’은 소유대명사(mine, yours, his, hers, ours, theirs)로 쓴다. 소유격(my, your, her, our, their)은 뒤에 명사가 있어야 한다.",
  n=["‘그녀의 것’이라는 소유대명사 hers로 옳으므로", "‘그들의 것’이라는 소유대명사 theirs로 옳으므로", "‘너의 것’이라는 소유대명사 yours로 옳으므로", "‘그의 것’이라는 소유대명사 his로 옳으므로", "명사 없이 ‘내 것’은 my가 아니라 mine이므로"],
  st="① 밑줄 뒤에 명사가 없다. ‘~의 것’이라는 소유대명사 자리다. → ② 소유격(my, your, her, our, their)은 뒤에 명사가 있어야 하므로 이 자리에 올 수 없다. {0} → ③ 정답은 {n}.",
  R="⑤의 my는 mine으로 써야 한다.", B="②의 our는 ours로 써야 한다.", C="②의 my는 mine으로 써야 한다.", D="⑤의 her는 hers로 써야 한다.", E="⑤의 their는 theirs로 써야 한다.", F="③의 your는 yours로 써야 한다.")

X(4, 17, r="앞에 나온 명사를 대명사로 받을 때는 수와 자리를 맞춘다. glasses처럼 복수 취급하는 명사가 목적어 자리에 오면 them으로 받는다.",
  n=["복수 취급하는 glasses를 받는 목적격 them이므로", "glasses는 복수라 it으로 받을 수 없으므로", "it's는 it is의 줄임말이므로", "its는 소유격이라 목적어 자리에 쓸 수 없으므로", "this는 단수를 가리키므로"],
  st="① 빈칸이 가리키는 말을 앞에서 찾는다: {0}. → ② 빈칸은 동사 뒤 목적어 자리이므로 목적격을 쓴다: {1}. → ③ 정답은 {a}.",
  R=("your glasses(복수)", "복수를 받는 목적격은 them"), B=("Tom(남자 한 명)", "him"), C=("your glasses(복수)", "복수를 받는 목적격은 them"), D=("Jane(여자 한 명)", "her"), E=("my parents(복수)", "them"),
  F=("A가 말한 me. B의 처지에서는 상대방이다", "you"))

X(4, 18, r="It's는 It is의 줄임말이고, its는 명사 앞에 쓰는 소유격(그것의)이다.",
  n=["(A)는 ‘그것은 ~이다’라 동사가 든 It's가 필요하므로", "It's(= It is) a cute dog, its name(그것의 이름)이므로", "명사 name 앞에는 소유격 its를 쓰므로", "두 자리를 반대로 썼으므로", "(A)에 동사가 없어 문장이 되지 않으므로"],
  st="① (A) 뒤에 동사가 없다. ‘주어 + be동사’의 줄임말이 들어가야 문장이 된다: {0}. → ② (B) 뒤에는 명사가 있다. 소유격이 들어간다: {1}. → ③ 정답은 {n}.",
  R=("It's(= It is)", "its"), B=("They're(= They are)", "their"), C=("It's(= It is)", "its"), D=("He's(= He is)", "his"), E=("She's(= She is)", "her"), F=("It's(= It is)", "its"))

X(4, 19, r="scissors, glasses, pants, shoes처럼 짝을 이루는 물건은 복수 취급해 They(them)로 받는다. news는 단수 취급해 It으로 받는다.",
  n=["복수 취급하는 scissors 앞에 some을 쓸 수 있으므로", "가위는 짝을 이루는 물건이라 복수형 scissors가 맞으므로", "명사 desk 앞에 소유격 my가 맞으므로", "scissors는 복수 취급하므로 It이 아니라 They로 받아야 하므로", "be동사 뒤 보어 자리에 형용사 sharp가 맞으므로"],
  st="① 뒤 문장의 주어와 동사를 맞춰 본다: {0}. → ② 앞 문장에서 가리키는 명사를 찾아 어느 쪽이 틀렸는지 정한다: {1}. → ③ 정답은 {n}.",
  R=("It are는 수가 맞지 않는다", "scissors는 복수 취급하므로 They are가 되어야 한다. 틀린 것은 It이다"), B=("They is는 수가 맞지 않는다", "shoes는 복수이므로 They are가 되어야 한다. 틀린 것은 is다"),
  C=("They is는 수가 맞지 않는다", "glasses는 복수 취급하므로 They are가 되어야 한다. 틀린 것은 is다"), D=("They is는 수가 맞지 않는다", "pants는 복수 취급하므로 They are가 되어야 한다. 틀린 것은 is다"),
  E=("It are는 수가 맞지 않는다", "news는 단수 취급하므로 It is가 되어야 한다. 틀린 것은 are다"), F=("They is는 수가 맞지 않는다", "police는 복수 취급하므로 They are가 되어야 한다. 틀린 것은 is다"))
RV(4, 19, "CDEF", v="수정(내용)", why="정답 확인. 다만 네 유형의 정답이 모두 ④이고 원문항의 정답도 ④여서 위치만으로 맞힐 수 있다. 또 원문항은 대명사(It)를 고르는데 변형은 모두 동사(is/are)가 틀려 묻는 내용이 다르다. 밑줄이 사라지고 발문에 조건이 붙은 점도 원문항과 다르다.", fix="대명사·지시어가 틀린 문장으로 새로, 정답 위치를 달리")

X(4, 20, r="A and B는 복수 주어다. 단수 주어에는 단수 동사를 쓴다. 명사 앞에는 소유격(her)을 쓰며 소유대명사에는 '를 붙이지 않는다.",
  pre=["문장별 판정: (A) X. 복수 주어 Tom and Sarah에는 are. (B) X. 단수 주어 friendship에는 is. (C) O. Those two + are. (D) X. books 앞에는 소유격 her를 쓴다."],
  n=["(D)가 빠졌으므로", "(C)는 옳은 문장이고 (A), (D)가 빠졌으므로", "(C)는 옳은 문장이고 (B)가 빠졌으므로", "(C)는 옳은 문장이고 (A)가 빠졌으므로", "틀린 문장 (A), (B), (D)를 모두 골랐으므로"],
  st="① 밑줄이 동사이면 주어의 수와 맞는지, 대명사이면 자리에 맞는지(명사 앞: 소유격, 명사 없음: 소유대명사) 본다. → ② {0} → ③ 틀린 것을 빠짐없이 고른 {a}가 정답이다.",
  R="(A) is(are), (B) are(is), (D) her's(her)가 틀렸다. (C)만 옳다.", B="(D) The news are(is)만 틀렸다. 나머지는 옳다.", C="(A) is(are), (B) are(is), (D) their(theirs)가 틀렸다.", D="(A) These pants is(are), (D) our(ours)가 틀렸다.",
  E="(B) my(mine), (D) The police is(are)가 틀렸다.", F="(A) Tom and Ben is(are), (D) my(mine)가 틀렸다.")
RV(4, 20, "F", fx=True, why="수정 예시의 (A)(Tom and Ben is ~)가 원문항 (A)(Tom and Sarah is ~)와 닮아 다른 문장(The children is ~)으로 바꿨다.")
