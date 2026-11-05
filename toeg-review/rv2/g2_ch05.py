# 2급 CH5 대명사 (41~50) 2차 감수
X(2, 41, r="둘 중 하나는 one, 나머지 하나는 the other로 나타낸다. 정해진 나머지라 the가 붙고, 하나라서 단수다.",
  n=["other는 명사 없이 단독으로 쓸 수 없으므로", "any는 ‘나머지 하나’를 가리키지 못하므로", "anothers라는 형태는 없으므로", "둘 중 나머지 하나는 the other이므로", "the others는 복수라 was와 맞지 않으므로"],
  st="① 앞 문장에서 전체가 몇인지 본다({0}). 둘이다. → ② 하나를 One으로 말했으니 남은 것은 정해진 하나다. 정해져 있으므로 the가 붙고, 하나이므로 동사도 단수({1})다. → ③ 정답은 the other({n})다. another는 셋 이상에서 ‘또 다른 하나’, the others는 ‘나머지 여럿’이다.",
  R=("Two students", "was"), B=("Two jackets", "was"), C=("two doors", "goes"), D=("Two answers", "was"), E=("two notebooks", "is"), F=("Two teams", "was"))

X(2, 42, r="여럿 중 하나는 one, 나머지 전부는 the others로 나타낸다. 정해진 나머지 전부라 the가 붙고 복수다.",
  n=["another는 ‘또 다른 하나’라 복수 동사 were와 맞지 않으므로", "some은 ‘일부’라 ‘나머지 모두’가 아니므로", "ones는 꾸미는 말 없이 단독으로 쓰지 않으므로", "other는 명사 없이 단독으로 주어가 될 수 없으므로", "정해진 나머지 전부는 the others이므로"],
  st="① 전체 수에서 One으로 말한 하나를 뺀다. {0}. → ② 남은 것 ‘전부’이므로 the가 붙고, 여럿이므로 복수다. 빈칸 뒤 동사도 복수({1})다. → ③ 정답은 the others({n})다. others는 ‘다른 것들 일부’, the other는 ‘나머지 하나’다.",
  R=("넷 중 하나를 빼면 셋이 남는다", "were"), B=("다섯 중 하나를 빼면 넷이 남는다", "are"), C=("여섯 중 하나를 빼면 다섯이 남는다", "are"), D=("넷 중 하나를 빼면 셋이 남는다", "live"), E=("일곱 중 하나를 빼면 여섯이 남는다", "are"),
  F="① 전체 수에서 One으로 말한 하나를 뺀다. 여섯 중 하나를 빼면 다섯이 남는다. → ② 남은 것 ‘전부’이므로 the가 붙고, 여럿이므로 복수다. 우리말의 ‘나머지 다섯 권은 모두’가 단서다. → ③ 정답은 the others({n})다. others는 ‘다른 것들 일부’, the other는 ‘나머지 하나’다.")

X(2, 43, r="it은 앞에 나온 바로 그것을 가리키고, one은 같은 종류의 정해지지 않은 하나를 가리킨다. a/an + 형용사 뒤에서 명사를 대신할 때는 one을 쓴다.",
  n=["a new 뒤에서 pencil을 대신한다. 잃어버린 그 연필이 아니라 새것 하나이므로 one이 들어간다.", "a yellow 뒤에서 umbrella를 대신하므로 one이 들어간다.", "a smaller 뒤에서 shirt를 대신하므로 one이 들어간다.", "a hot 뒤에서 drink를 대신하므로 one이 들어간다.",
     "아빠가 사 준 바로 그 시계를 가리키므로 it이 들어간다. 나머지 넷(one)과 다르다."],
  st="① 빈칸이 앞에 나온 ‘바로 그것’을 가리키는지, ‘같은 종류의 다른 하나’를 가리키는지 가른다. → ② 빈칸 앞에 a/an/the + 형용사나 this, that이 있거나, 정해지지 않은 아무거나 하나를 뜻하면 one이다. → ③ {n}은 {0} 가리키므로 it이다.",
  R="아빠가 사 준 바로 그 시계를", B="Jane이 구운 바로 그 파이를", C="Tom이 생일에 받은 바로 그 기타를", D="할아버지가 만든 바로 그 배를", E="할머니가 떠 준 바로 그 목도리를", F="우리가 본 바로 그 무지개를")

X(2, 44, r="재귀대명사가 주어나 목적어를 강조할 때(강조 용법)는 생략해도 문장이 성립한다. 동사나 전치사의 목적어로 쓰일 때(재귀 용법)는 생략할 수 없다.",
  n=["calls의 목적어인 재귀 용법이므로", "주어 We를 강조하는 강조 용법이라 <보기>와 같으므로", "enjoyed의 목적어인 재귀 용법이므로", "asked의 목적어인 재귀 용법이므로", "전치사 of의 목적어인 재귀 용법이므로"],
  st="① <보기>의 재귀대명사({0})를 빼 본다. ‘{1}’만으로도 문장이 완전하다. 주어를 강조하는 강조 용법이다. → ② 보기마다 재귀대명사를 빼 본다. 동사나 전치사의 목적어가 사라져 문장이 깨지면 재귀 용법이다. → ③ {n}만 빼도 문장이 성립한다({2}).",
  R=("himself", "The principal attended the meeting.", "We built the treehouse."), B=("himself", "The chef served the final dish.", "The students organized the festival."), C=("herself", "The author answered every question.", "Jane repaired the bicycle."),
  D=("themselves", "The players cleaned the locker room.", "We prepared the meal."), E=("myself", "I checked the final numbers.", "Tom wrote the speech."), F=("himself", "The mayor opened the event.", "You said it was true."))
RV(2, 44, "B", v="수정(표기)", why="정답 ④ 확인. 발문은 ‘(보기)와 같은 것’을 묻는데 본문에 <보기> 표시가 없다(2-8, 2-19와 같은 결함). 수정 예시는 이미 <보기>를 붙인 상태다.", fix="본문에 <보기> 표시 넣기")

X(2, 45, r="가목적어 it은 뒤의 to부정사(진목적어)를 대신한다. some은 주로 긍정문에, any는 부정문·의문문에 쓴다. each는 단수 명사·단수 동사와 쓴다. 목적어인 재귀대명사는 생략할 수 없다. others는 ‘다른 일부’이고 ‘나머지 전부’는 the others다.",
  pre=["학생별 판정: Mary O(가목적어 it). Tom O(some은 긍정문). Bruce X(Each player wears가 맞다). Cathy X(saw의 목적어라 생략할 수 없다). Dave X(others는 나머지 전부가 아니다)."],
  k="올바르게 설명한 학생은 Mary, Tom이다.", n=["올바르게 설명한 학생은 Mary, Tom이므로"] * 5,
  st="① 학생마다 예문과 설명을 따로 따진다. 틀린 예문을 맞다고 하거나 용법을 잘못 말하면 틀린 설명이다. → ② {0} → ③ 옳게 설명한 학생만 모으면 {a}이다.",
  R="Bruce는 Each players wears를 맞다고 했고(Each player wears), Cathy는 saw의 목적어인 himself를 생략할 수 있다고 했으며, Dave는 others를 ‘나머지 전부’로 풀었다. 셋 다 틀렸다.",
  B="Jane은 Each of the boys have를 맞다고 했고(has), Ben은 hurt의 목적어인 herself를 생략할 수 있다고 했으며, Sora는 others를 ‘나머지 전부’로 풀었다. 셋 다 틀렸다.",
  C="Jin은 Each student have를 맞다고 했고(has), Mia는 enjoyed의 목적어인 myself를 강조 용법이라고 했다. 둘 다 틀렸다.",
  D="Jane은 시간을 나타내는 비인칭 It을 가목적어라고 했고, Sora는 Each of the players wear를 맞다고 했다(wears). 둘 다 틀렸다.",
  E="Leo는 부탁하는 말에 any가 자연스럽다고 했고(some), Jane은 Every student have를 맞다고 했다(has). 둘 다 틀렸다.",
  F="Mia는 cut의 목적어인 himself를 뺄 수 있다고 했고, Leo는 others를 ‘남은 전부’로 풀었다(전부는 the others). 둘 다 틀렸다.")
RV(2, 45, "C", fx=True, why="수정 예시의 정답이 네 명(Tom, Amy, Jin, Leo)이라 원문항(두세 명 조합)과 보기 형태가 달랐다. Jin의 설명을 틀린 설명(Each student have를 맞다고 함)으로 바꿔 정답을 세 명(Tom, Amy, Leo)으로 하고 네 명 보기를 없앴다.")

X(2, 46, r="consider, think, find의 목적어가 to부정사이면 그 자리에 가목적어 it을 두고 to부정사는 뒤로 보낸다: 동사 + it + 형용사 + to부정사.",
  n=["it과 easy의 순서가 바뀌었으므로", "to make가 it보다 앞에 놓였으므로", "make 앞에 to가 빠졌으므로", "considers + it + easy + to make ~ 순서로 바르게 배열했으므로", "to가 easy 앞에 놓였으므로"],
  st="① 우리말의 ‘{0}’이 목적어, ‘{1}’가 목적격 보어다. → ② 목적어가 to부정사이면 그 자리에 가목적어 it을 두고 to부정사는 뒤로 보낸다: 동사({2}) + it + 형용사({3}) + to부정사. → ③ 이 순서대로 놓인 {n}을 고른다.",
  R=("새로운 친구를 사귀는 것을", "쉽게", "considers", "easy"), B=("새로운 환경에 적응하는 것을", "어렵다고", "considers", "difficult"), C=("이 규칙을 기억하는 것을", "중요하다고", "think", "important"),
  D=("혼자 그 일을 하는 것을", "불가능하다고", "considers", "impossible"), E=("정시에 도착하는 것을", "필요하다고", "think", "necessary"), F=("그 설명을 이해하는 것을", "쉽다고", "considers", "easy"))

X(2, 47, r="셋을 차례로 말할 때는 one, another, the other를 쓴다. 넷 이상에서 마지막에 여럿이 남으면 the others를 쓴다.",
  n=["셋 중 두 번째는 another, 마지막 남은 하나는 the other이므로", "another와 the other의 순서가 바뀌었으므로", "둘 다 복수형이라 is와 맞지 않으므로", "others는 복수라 is와 맞지 않으므로", "두 번째에 the other를 쓰면 세 번째가 남지 않으므로"],
  st="① 전체가 몇인지 본다({0}). One 다음에도 둘 이상이 남았으므로 첫째 빈칸은 ‘또 다른 하나’인 another다. → ② 둘째 빈칸은 마지막으로 남은 것이다. 뒤의 동사({1})를 보면 {2}. → ③ 정답은 {a}.",
  R=("three apples", "is", "하나이므로 the other다"), B=("three tours", "goes", "하나이므로 the other다"), C=("three jackets", "is", "하나이므로 the other다"), D=("Five students", "are", "여럿이므로 the others다"),
  E=("three routes", "is", "하나이므로 the other다"), F=("six cups", "are", "여럿이므로 the others다"))

X(2, 48, r="전치사 + 재귀대명사 관용 표현: by oneself(혼자서), for oneself(스스로, 자신을 위해), beside oneself(제정신이 아닌).",
  n=["by herself는 ‘혼자서’라는 뜻이므로", "for herself는 ‘스스로, 자신을 위해’라는 뜻이므로", "in herself는 ‘제정신이 아닌’이라는 뜻이 아니므로", "on herself라는 관용 표현은 없으므로", "beside oneself가 ‘제정신이 아닌’이라는 뜻이므로"],
  st="① 우리말 ‘제정신이 아니었다’에 해당하는 ‘전치사 + 재귀대명사’ 표현을 떠올린다. → ② by oneself는 ‘혼자서’, for oneself는 ‘스스로’, to oneself는 ‘혼자 독차지하여’다. ‘제정신이 아닌’은 beside oneself다. {0} → ③ 정답은 {a}.",
  R="재귀대명사는 주어 She에 맞춰 herself를 쓴다.", B="뒤의 with grief(슬픔으로)가 그렇게 된 까닭이다.", C="뒤의 with joy(기쁨으로)가 그렇게 된 까닭이다.", D="뒤의 with anger(화가 나서)가 그렇게 된 까닭이다.",
  E="뒤의 with excitement(흥분해서)가 그렇게 된 까닭이다.", F="뒤의 with worry(걱정으로)가 그렇게 된 까닭이다.")

X(2, 49, r="재귀대명사는 그 문장의 주어와 같은 대상을 가리키며 주어의 인칭·수에 맞춘다(All students → themselves, We → ourselves).",
  n=["All students는 복수라 himself를 쓸 수 없으므로", "We에는 yourselves가 아니라 ourselves를 쓰므로", "(A)에 himself, (B)에 themselves 모두 맞지 않으므로", "All students → themselves, We → ourselves로 주어에 맞으므로", "We에 itself를 쓸 수 없으므로"],
  st="① 재귀대명사는 그 문장의 주어와 같은 대상을 가리킨다. 두 문장의 주어를 찾는다. → ② (A)의 주어({0})는 3인칭 복수이므로 themselves다. (B)의 주어({1})에 맞는 것은 {2}다. → ③ 정답은 {n}.",
  R=("All students", "We", "ourselves"), B=("All participants", "Mina", "herself"), C=("All children", "you = Mina 한 사람", "yourself"), D=("People", "I", "myself"), E=("All students", "My sister and I", "ourselves"), F=("The participants", "The machine", "itself"))
RV(2, 49, "BCDEF", fx=True, why="수정 예시의 (A) 문장 주어가 Each participant, No one 같은 단수라 himself도 맞다고 볼 여지가 있었다(원문항에서 고친 결함과 같음). 고친 원문항(All students)처럼 주어를 복수로 바꿔 themselves만 답이 되게 했다.")

X(2, 50, r="all/most/some of 뒤의 명사가 셀 수 없으면 단수 동사, 복수이면 복수 동사를 쓴다. each of ~, one of ~, every ~는 항상 단수 동사를 쓴다. any 뒤의 셀 수 있는 명사는 복수형으로 쓴다.",
  pre=["문장별 판정: (A) X. information은 셀 수 없으므로 is. (B) O. any + 복수 명사. (C) X. each of ~는 단수이므로 has. (D) X. 주어가 cakes이므로 smell. (E) O. family members가 복수이므로 were."],
  n=["(A)가 틀렸으므로", "(B)와 (E) 모두 옳으므로", "(C)와 (D) 모두 틀렸으므로", "(A)와 (C)가 틀렸으므로", "(D)가 틀렸으므로"],
  st="① 밑줄 동사의 수는 of 뒤 명사가 정한다. all/most/some of + 셀 수 없는 명사는 단수, + 복수 명사는 복수다. → ② each of ~, one of ~, every ~는 뒤에 복수 명사가 와도 항상 단수다. → ③ 틀린 문장을 지운다: {0}. 옳은 문장만 묶은 {a}가 정답이다.",
  R="(A) information은 셀 수 없으므로 is, (C) each of ~는 has, (D) cakes는 복수이므로 smell", B="(B) each of ~는 has, (D) one of ~는 lives, (E) water는 셀 수 없으므로 was",
  C="(C) classmates는 복수이므로 like, (D) cookies는 복수이므로 were, (E) every ~는 needs", D="(A) news는 셀 수 없으므로 was, (D) windows는 복수이므로 were",
  E="(A) homework는 셀 수 없으므로 is, (D) cake는 단수이므로 was, (E) students는 복수이므로 were", F="(B) each of ~는 has, (D) shoes는 복수이므로 are")
