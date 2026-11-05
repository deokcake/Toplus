# 6급 CH2 대명사와 be동사 (11~20) 2차 감수
X(6, 11, r="여럿을 대명사로 받을 때: ‘나’가 들어 있으면 we, ‘나’ 없이 ‘너’가 들어 있으면 you, 둘 다 없으면 they다. 한 사람은 he/she, 사물 하나는 it이다.",
  n=["여자 한 명이라 she가 맞으므로", "남자 한 명이라 he가 맞으므로", "나(I)가 들어 있어 we로 받아야 하므로", "나와 너가 없는 두 사람이라 they가 맞으므로", "나(I)가 들어 있어 we가 맞으므로"],
  st="① 짝마다 왼쪽 말에 I(나)가 들어 있는지 먼저 본다. 있으면 we다. → ② I가 없고 you가 있으면 you, 둘 다 없으면 수와 성별로 he/she/it/they를 정한다. → ③ {0} 정답은 {n}.",
  R="you and I에는 I가 있어 we다.", B="my sister and I에는 I가 있어 we다.", C="you and Jane에는 I가 없고 you가 있어 you다.", D="my parents는 두 사람이라 they다.", E="Jisu and her sister는 두 사람이라 they다.",
  F="the books는 여러 권이라 they다.")
RV(6, 11, "CDE", v="수정(내용)", why="정답 유일 확인. 다만 보기가 원문항 보기를 이름만 바꾼 것이다: her brother - he는 원문항 ②와 똑같고, Sophie and ~ - they, my mother(grandma) - she, Tom and I - we도 원문항 ④·①·⑤와 같은 짜임이다. C와 E는 틀린 짝도 같은 꼴이다(you and Jane/Mina - she).", fix="원문항과 다른 명사로 새로")

X(6, 12, r="현재형 be동사: I am / he, she, it, 단수 주어 is / you, we, they, 복수 주어(A and B) are.",
  n=["You에는 are가 들어가므로", "They에는 are가 들어가므로", "It에는 is가 들어가 나머지(are)와 다르므로", "We에는 are가 들어가므로", "I and my mother는 두 사람이라 are가 들어가므로"],
  st="① 문장마다 주어의 인칭과 수를 가른다. A and B는 복수다. → ② 빈칸에 am/is/are를 넣어 본다. → ③ {0} 정답은 {n}.",
  R="③만 is이고 나머지는 are다.", B="③ Mr. Brown만 is이고 나머지는 are다.", C="④ Mina and Sumi만 are이고 나머지는 is다.", D="① I만 am이고 나머지는 are다.", E="⑤ Your glasses만 are이고 나머지는 is다. glasses는 복수로 쓴다.",
  F="② The baby만 is이고 나머지는 are다.")

X(6, 13, r="be동사 의문문은 be동사 + 주어 ~?이고 be동사는 주어에 맞춘다. 대답은 Yes, 주어 + be동사. / No, 주어 + be동사 + not.이다.",
  n=["복수 주어 those에 Are, they에 are가 알맞으므로", "Yes로 답했으므로 aren't를 쓸 수 없으므로", "복수 주어 those에 Is를 쓸 수 없으므로", "복수 주어 those에 Is를 쓸 수 없으므로", "현재의 질문에 과거형 were로 답할 수 없으므로"],
  st="① 질문의 주어를 본다: {0}. → ② 대답의 주어와 Yes/No를 본다: {1}. → ③ 정답은 {a}.",
  R=("those(복수) → Are", "Yes, they → are"), B=("you → Are", "Yes, I → am"), C=("that(단수) → Is", "No, it → isn't"), D=("these(복수) → Are", "No, they → aren't"), E=("this(단수) → Is", "Yes, it → is"), F=("I → Am", "No, you → aren't"))
RV(6, 13, "F", v="수정(내용)", why="정답 ① 유일 확인. 다만 정답 조합(Are - aren't)과 대화의 짜임(those/these ~? — No, they ~.)이 D와 같다(유형 간 중복). 발문에도 ‘현재형 be동사를 사용하여’가 붙었다.", fix="주어가 다른 대화로 바꿔 정답 조합을 다르게")

X(6, 14, r="명사 앞에서 ‘~의’를 나타낼 때는 소유격(my, your, his, her, its, our, their)이나 명사 + ’s를 쓴다. 주격(he, she, we, they, I)은 명사 앞에 쓸 수 없다.",
  n=["명사 car 앞이라 주격 he가 아니라 소유격 his를 써야 하므로", "명사 + ’s로 소유를 바르게 나타냈으므로", "명사 + ’s로 소유를 바르게 나타냈으므로", "소유격 her를 명사 앞에 바르게 썼으므로", "소유격 my를 명사 앞에 바르게 썼으므로"],
  st="① 밑줄 뒤에 명사가 있는지 본다. 명사 앞은 소유격 자리다. → ② 밑줄 친 말이 소유격이나 명사 + ’s인지 본다. → ③ {0} 정답은 {n}.",
  R="①의 he는 주격이다. his car로 써야 한다.", B="④의 she는 주격이다. her bike로 써야 한다.", C="②의 him은 목적격이다. his jacket으로 써야 한다.", D="①의 We는 주격이다. Our classroom으로 써야 한다.",
  E="③의 They는 주격이다. Their car로 써야 한다.", F="⑤의 I는 주격이다. my notebook으로 써야 한다.")

X(6, 15, r="be동사는 주어에 맞춘다: I am, you/we/they are, he/she/it is. 의문문에서도 뒤에 오는 주어에 맞춘다.",
  n=["She에 is를 바르게 썼으므로", "They에 aren't를 바르게 썼으므로", "주어 you에는 Is가 아니라 Are를 써야 하므로", "Those에 are를 바르게 썼으므로", "he에 Is를 바르게 썼으므로"],
  st="① 문장마다 주어를 찾는다. 의문문의 주어는 be동사 바로 뒤에 있다. → ② be동사가 주어의 인칭·수와 맞는지 본다. → ③ {0} 정답은 {n}.",
  R="③의 주어 you에는 Are를 쓴다.", B="④의 주어 they에는 Are를 쓴다.", C="③의 주어 she에는 Is를 쓴다.", D="⑤의 주어 he에는 Is를 쓴다.", E="⑤의 주어 your father는 단수라 Is를 쓴다.", F="②의 주어 The girls는 복수라 are를 쓴다.")
RV(6, 15, "E", v="수정(내용)", why="정답 ⑤ 유일 확인. 다만 틀린 문장(Is they in the classroom?)이 B의 틀린 문장(Is they your friends?)과 거의 같다(유형 간 중복).", fix="틀린 문장을 다른 문장으로")
RV(6, 15, "F", v="수정(내용)", why="정답 ② 유일 확인. 다만 틀린 문장(Are she your teacher?)이 C의 틀린 문장(Are she your cousin?)과 거의 같다(유형 간 중복).", fix="틀린 문장을 다른 문장으로")

X(6, 16, r="현재형 be동사: I am / you, we, they are / he, she, it is. be는 원형이라 그대로 쓸 수 없다.",
  n=["am은 주어 I에만 쓰므로", "is는 3인칭 단수 주어에 쓰므로", "주어 You에 맞는 be동사이므로", "be는 동사원형이라 주어 뒤에 그대로 쓸 수 없으므로", "주어 You에는 was가 아니라 were를 쓰므로"],
  st="① 주어를 본다: {0}. → ② 그 주어에 맞는 현재형 be동사는 {1}. → ③ 원형 be와 주어에 맞지 않는 형태를 지운다. 정답은 {n}.",
  R=("You", "are"), B=("Tom(3인칭 단수)", "is"), C=("I", "am"), D=("She(3인칭 단수)", "is"), E=("We", "are"), F=("My parents(복수)", "are"))
RV(6, 16, "E", fx=True, why="수정 예시의 문장(We ___ in the same class.)이 같은 단원 12번 F의 수정 예시 문장과 똑같아 다른 문장(We ___ on the playground now.)으로 바꿨다.")

X(6, 17, r="가까이 있는 것은 this(한 개)/these(여러 개), 멀리 있는 것은 that(한 개)/those(여러 개)다. 명사 앞에서도, 혼자 주어로도 쓴다.",
  n=["This는 가까이 있는 한 개라 stars, are와 맞지 않으므로", "These는 ‘이 ~들’이라 우리말 ‘저’와 맞지 않으므로", "That은 한 개를 가리켜 stars, are와 맞지 않으므로", "They는 명사 stars 앞에 쓸 수 없으므로", "‘저 별들’, ‘저것들’처럼 멀리 있는 여러 개를 가리키므로"],
  st="① 우리말에서 거리를 본다: {0}. → ② 수를 본다: {1}. → ③ 두 조건에 맞는 말은 {a}. 명사 앞과 주어 자리에 모두 들어가는지 확인한다.",
  R=("‘저’ → 멀리", "stars, are → 여러 개"), B=("‘이’ → 가까이", "books, are → 여러 개"), C=("‘이’ → 가까이", "bag, is → 한 개"), D=("‘저’ → 멀리", "shoes, are → 여러 개"), E=("‘저’ → 멀리", "mountain, is → 한 개"),
  F=("‘저’ → 멀리", "car, is → 한 개"))

X(6, 18, r="be동사 의문문은 be동사 + 주어 ~?이다. be동사는 주어에 맞춘다(I → Am, 단수 → Is, you·복수 → Are).",
  n=["단수 주어 his brother에 Is를 바르게 썼으므로", "you에 Are를 바르게 썼으므로", "I에 Am을 바르게 썼으므로", "복수 주어 the apples에는 Are를 써야 하므로", "they에 Are를 바르게 썼으므로"],
  st="① be동사 바로 뒤의 주어를 본다. -s가 붙은 복수 명사인지, 한 사람·한 개인지 가른다. → ② 맨 앞의 be동사가 그 주어와 맞는지 본다. → ③ {0} 정답은 {n}.",
  R="④의 the apples는 복수라 Are다.", B="④의 the puppy는 단수라 Is다.", C="⑤의 Jane은 단수라 Is다.", D="①의 the boys는 복수라 Are다.", E="⑤의 your uncle은 단수라 Is다.", F="⑤의 the books는 복수라 Are다. Am은 I에만 쓴다.")
RV(6, 18, "E", v="수정(내용)", why="정답 ⑤ 유일 확인. 다만 틀린 문장(Are the dog hungry?)이 B의 틀린 문장(Are the puppy hungry?)과 거의 같다(유형 간 중복).", fix="틀린 문장을 다른 문장으로")

X(6, 19, r="be동사는 주어의 수와 인칭에 맞춘다. 주어가 복수(they, 복수 명사, A and B)이면 are를 쓴다.",
  n=["they는 ‘나’를 포함하지 않으므로", "they가 3인칭 복수 주어라 are를 써야 하므로", "be동사는 뒤에 오는 낱말의 첫소리와 관계없으므로", "의문문도 주어에 따라 Am/Is/Are를 쓰므로", "be동사는 성별이 아니라 수와 인칭으로 정하므로"],
  st="① be동사를 정하는 것은 주어다. 이 질문의 주어는 {0}. → ② {1} → ③ 주어의 수를 이유로 든 설명을 고른다. 정답은 {n}.",
  R=("they", "they는 3인칭 복수이므로 Are를 쓴다."), B=("the girls", "복수 명사이므로 Are를 쓴다."), C=("you and Mina", "두 사람이므로 Are를 쓴다."), D=("these books", "복수 명사이므로 Are를 쓴다."), E=("Tom and I", "두 사람(we)이므로 Are를 쓴다."),
  F=("your parents", "두 사람을 가리키는 복수 명사이므로 Are를 쓴다. your(2인칭) 때문이 아니다."))
RV(6, 19, "F", v="수정(내용)", why="정답 ② 유일 확인. 다만 대화(Is the boys in the music room?)와 틀린 설명 네 개가 B(Is the girls in the gym?)와 거의 같다(유형 간 중복). 발문에도 원문항의 ‘한국어로’가 빠져 있다.", fix="대화와 설명을 새로, 발문을 원문항대로")

X(6, 20, r="this/that은 한 개, these/those는 여러 개를 가리키고 be동사도 is/are로 맞춘다. 양말·신발·장갑처럼 짝을 이루는 물건은 복수형으로 쓴다.",
  n=["this는 한 개를 가리켜 are와 어울리지 않으므로", "양말은 두 짝이 한 켤레라 복수형 socks로 쓰므로", "That은 멀리 있는 한 개를 가리키므로", "That is와 함께 쓰여 하나를 가리키므로 hat이 맞으므로", "are는 복수, is는 단수 주어에 써서 바꿔 쓸 수 없으므로"],
  st="① 지문을 두 쌍으로 본다: {0}. → ② 설명마다 지시어의 거리·수, be동사, 명사의 수가 서로 맞는지 대어 본다. → ③ {1} 정답은 {n}.",
  R=("Those are + socks(여러 개) / That is + hat(한 개)", "② 양말은 짝을 이루므로 복수형으로 쓴다."), B=("These are + gloves(여러 개) / This is + scarf(한 개)", "③ These는 가까이 있는 여러 개이고 are와 쓴다."),
  C=("These are + books(여러 개) / This is + notebook(한 개)", "⑤ This는 가까이 있는 한 개이고 is와 쓴다."), D=("Those are + shoes(여러 개) / That is + bag(한 개)", "④ That은 멀리 있는 한 개이고 is와 쓴다."),
  E=("These are + pencils(여러 개) / This is + eraser(한 개)", "③ eraser는 This is와 함께 쓰인 단수형이 맞다."), F=("Those are + buses(여러 개) / That is + car(한 개)", "③ bus의 복수형은 -es를 붙인 buses다."))
RV(6, 20, "C", v="수정(내용)", why="정답 ② 유일 확인. 다만 정답 설명((A)의 These는 가까이 있는 여러 개를 가리키므로 are와 함께 쓴다)이 B의 정답 설명과 같고 지문의 짜임(These are ~. This is ~.)도 같다(유형 간 중복). 발문도 원문항과 다르다.", fix="정답 설명을 다른 밑줄에 대한 것으로")
