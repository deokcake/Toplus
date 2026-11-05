# 7급 CH5 지시 대명사 (41~50) 2차 감수
X(7, 41, r="this(이것)·that(저것)은 한 개, these(이것들)·those(저것들)는 여러 개를 가리킨다. these/those는 are와, this/that/it은 is와 쓴다.",
  n=["This는 한 개를 가리켜 are와 쓸 수 없으므로", "That은 한 개를 가리켜 are와 쓸 수 없으므로", "‘이것들’은 가까이 있는 여러 개를 가리키는 These이므로", "Those는 ‘저것들’이라는 뜻이므로", "It은 한 개를 가리켜 are와 쓸 수 없으므로"],
  st="① 빈칸 뒤가 are이므로 한 개를 가리키는 This, That, It을 지운다. → ② 우리말이 ‘{0}’이므로 {1} 여러 개를 가리킨다. → ③ 정답은 {a}.",
  R=("이것들", "가까이 있는"), B=("저것들", "멀리 있는"), C=("이것들", "가까이 있는"), D=("저것들", "멀리 있는"), E=("저것들", "멀리 있는"), F=("이것들", "가까이 있는"))
RV(7, 41, "D", v="수정(표기)", why="정답 ① Those 유일 확인. 다만 원문항에 없는 문장(Look over there.)이 붙었고, 우리말 해석이 문장 전체가 아니라 ‘(저쪽에 있는 산들)’이라는 풀이로 바뀌었다. 같은 유형의 46번 변형(Look over there. ___ are horses.)과도 짜임이 똑같다.", fix="덧붙은 문장을 지우고 원문항처럼 문장의 우리말 해석을")

X(7, 42, r="This/That은 한 사람·한 개를 가리켜 is와 쓴다. 뒤에 are와 복수 명사가 오면 These/Those를 써야 한다.",
  n=["is와 단수 명사(a house)가 와서 This/That이 들어갈 수 있으므로", "is와 단수 명사(an orange)가 와서 This/That이 들어갈 수 있으므로", "are와 복수 명사(dogs)가 와서 These/Those가 들어가야 하므로", "is와 한 사람(my brother)이 와서 This/That이 들어갈 수 있으므로",
     "is와 단수 명사(the new book)가 와서 This/That이 들어갈 수 있으므로"],
  st="① 빈칸 뒤의 be동사를 본다. is가 오면 This/That이 들어갈 수 있다. → ② are가 온 문장을 찾는다: {0} → ③ are 앞에는 These/Those를 써야 하므로 정답은 {n}.",
  R="③ ___ are dogs.", B="⑤ ___ are our bags.", C="④ ___ are apples.", D="② ___ are my books.", E="① ___ are birds.", F="③ ___ are my cousins.")
RV(7, 42, "DE", v="수정(내용)", why="정답 유일 확인. 다만 보기 다섯 가운데 둘이 원문항 선택지와 똑같다(D: is a house, is an orange / E: is a house, is my brother). 발문에도 ‘실제 사람이나 물건을 가리킬 때’가 붙었다.", fix="원문항과 같은 문장을 새 문장으로, 발문을 원문항대로")

X(7, 43, r="대답의 주어가 they이면 질문은 여러 개(these/those/복수 명사)를 물은 것이다. this/that/it으로 물으면 it으로, you로 물으면 I나 we로 답한다.",
  n=["this로 한 개를 물으면 it으로 답하므로", "that으로 한 개를 물으면 it으로 답하므로", "this로 한 개를 물으면 it으로 답하므로", "these로 여러 개를 물어 they로 답할 수 있으므로", "it으로 물으면 it으로 답하므로"],
  st="① 대답을 본다: {0}. 주어가 they다. → ② they로 받을 수 있는 것은 these/those로 물은 여러 개뿐이다. this/that/it이나 you, she로 물은 질문을 지운다. → ③ 남는 것은 {a}",
  R="No, they aren't.", B="No, they aren't.", C="Yes, they are.", D="No, they're my sister's.", E="Yes, they're mine.", F="No, they're not.")
RV(7, 43, "B", fx=True, why="변형의 ②(Are those your scarf?)는 질문 자체가 틀린 문장이라 대답과 견주지 않아도 지워진다(원문항의 보기는 모두 옳은 질문이다). 정답 위치(④)도 원문항과 같다. 수정 예시에서 ②를 옳은 질문으로 바꾸고 정답을 ⑤로 옮겼다.")

X(7, 44, r="‘이것들’은 these, ‘저것들’은 those다. 여러 개를 물을 때는 Are these/those + 복수 명사 ~?로 쓴다.",
  n=["‘저것들’은 여러 개라 that과 an airplane으로 옮길 수 없으므로", "this는 ‘이것’이고 한 개를 가리키므로", "that은 한 개를 가리켜 Are, 복수 명사와 쓸 수 없으므로", "‘저것들’을 those로, be동사를 Are로, 명사를 복수로 바르게 옮겼으므로", "these는 ‘이것들’이고 Is와도 쓸 수 없으므로"],
  st="① 우리말의 ‘{0}’에 맞는 지시대명사는 {1}. → ② 여러 개이므로 be동사는 Are, 명사는 복수형({2})이다. → ③ 셋을 다 갖춘 것은 {a}",
  R=("저것들", "those", "airplanes"), B=("이것들", "these", "keys"), C=("이것들", "these", "apples"), D=("저것들", "those", "books"), E=("저것들", "those", "cars"), F=("이것들", "these", "shoes"))

X(7, 45, r="these/those는 여러 개를 가리켜 Are와 쓰고 대답에서 they로 받는다. this/that은 한 개를 가리켜 Is와 쓰고 대답에서 it으로 받는다.",
  n=["this는 한 개를 가리켜 Are와 쓸 수 없으므로", "여러 개를 가리키는 those와 대답의 they를 바르게 짝지었으므로", "that은 한 개를 가리켜 Are와 쓸 수 없으므로", "여러 개는 대답에서 it이 아니라 they로 받으므로", "여러 개는 대답에서 it이 아니라 they로 받으므로"],
  st="① 질문의 be동사가 {0}이므로 첫 빈칸에는 {1} 지시대명사가 온다. → ② 대답의 be동사({2})에 맞는 대명사는 {3}. → ③ 둘을 갖춘 것은 {a}.",
  R=("Are", "여러 개를 가리키는", "aren't", "they"), B=("Are", "여러 개를 가리키는", "are", "they"), C=("Are", "여러 개를 가리키는", "are", "they"), D=("Is", "한 개를 가리키는", "is", "it"),
  E=("Is", "한 개를 가리키는", "isn't", "it"), F=("Are", "여러 개를 가리키는", "aren't", "they"))

X(7, 46, r="가까이 있는 것은 this(한 개)·these(여러 개), 멀리 있는 것은 that(한 개)·those(여러 개)로 가리킨다. these/those는 are와 쓴다.",
  n=["This는 한 사람을 가리켜 are와 쓸 수 없으므로", "He는 한 사람이라 are와 쓸 수 없으므로", "가까이 있는 여러 사람을 가리키는 These가 are와 어울리므로", "She는 한 사람이라 are와 쓸 수 없으므로", "It은 are와 쓸 수 없으므로"],
  st="① 빈칸 뒤가 are이고 명사({0})도 복수이므로 여럿을 가리키는 말이 필요하다. → ② 괄호 안의 설명을 본다. {1} → ③ 정답은 {n}.",
  R=("friends", "가까이 있는 친구들이므로 These다."), B=("books", "멀리 있는 책들이므로 Those다."), C=("pencils", "가까이 있는 연필들이므로 These다."), D=("horses", "멀리 있는 말들이므로 Those다."),
  E=("cats", "멀리 있는 고양이들이므로 Those다."), F=("balls", "가까이 있는 공들이므로 These다."))
RV(7, 46, "D", v="수정(표기)", why="정답 ② Those 유일 확인. 다만 원문항에 없는 문장(Look over there.)이 붙어 괄호 안의 설명과 같은 단서를 두 번 준다. 같은 유형의 41번 변형(Look over there. ___ are mountains.)과도 짜임이 똑같다.", fix="덧붙은 문장을 지우고 원문항처럼 괄호 안의 상황 설명만")

X(7, 47, r="Is this/that ~?에는 No, it isn't.로, Are these/those ~?에는 No, they aren't.로 답한다. No 뒤에는 be동사 + not을 쓴다.",
  n=["No로 답했으므로 부정형을 써야 하므로", "these는 대답에서 it이 아니라 they로 받으므로", "be동사 없이 not만 쓸 수 없으므로", "these는 they로 받고 No 뒤에는 부정형을 써야 하므로", "these를 they로 받아 aren't로 바르게 답했으므로"],
  st="① 질문의 주어를 본다: {0}. → ② No로 답하므로 be동사에 not을 붙인다: {1}. → ③ 정답은 {n}.",
  R=("these(여러 개) → 대답에서는 they", "they aren't"), B=("that(한 개) → 대답에서는 it", "it isn't"), C=("these(여러 개) → 대답에서는 they", "they aren't"), D=("these(여러 개) → 대답에서는 they", "they aren't"),
  E=("this(한 개) → 대답에서는 it", "it isn't"), F=("those(여러 개) → 대답에서는 they", "they aren't"))

X(7, 48, r="‘이분은/이것은 ~의 … 이다’는 지시대명사 + be동사 + 소유격 + 형용사 + 명사의 순서로 쓴다.",
  n=["is는 둘째 낱말이므로", "This is our beautiful teacher.에서 셋째 낱말이므로", "this는 첫째 낱말이므로", "teacher는 다섯째 낱말이므로", "beautiful은 넷째 낱말이므로"],
  st="① 우리말의 주어(‘{0}’)에 맞는 지시대명사와 be동사를 먼저 놓는다: {1}. → ② 그 뒤에 소유격 + 형용사 + 명사를 잇는다: {2}. → ③ 완성 문장 {3}의 셋째 낱말은 {a}.",
  R=("이 분은", "This is", "our beautiful teacher", "This is our beautiful teacher."), B=("저것은", "That is", "my new backpack", "That is my new backpack."), C=("이것은", "This is", "his red car", "This is his red car."),
  D=("저것들은", "Those are", "your new shoes", "Those are your new shoes."), E=("저것은", "That is", "her small bag", "That is her small bag."), F=("이것은", "This is", "their nice house", "This is their nice house."))
RV(7, 48, "BCEF", fx=True, why="수정 예시의 제시어 순서가 보기 순서와 달랐다. 원문항은 제시어와 보기의 순서가 같으므로, 제시어를 보기와 같은 순서로 맞췄다.")
RV(7, 48, "D", fx=True, why="변형과 수정 예시의 문장(That is my new book.)이 B(That is my new backpack.)와 명사만 다르고 정답(my)과 위치(⑤)도 같았다(유형 간 중복). 수정 예시를 주어가 those인 문장(Those are your new shoes.)으로 바꾸고, 제시어를 보기와 같은 순서로 맞췄다.")

X(7, 49, r="지시대명사와 be동사, 명사의 수를 함께 맞춘다. this/that + is + a/an + 단수 명사, these/those + are + 복수 명사. a/an은 뒤 낱말의 첫소리로 정한다.",
  n=["a 뒤에는 단수 명사 pencil을 써야 하므로", "한 개를 가리키므로 these가 아니라 this를 써야 하므로", "an을 a로, penciles를 pencil로 바르게 고쳤으므로", "단수 주어 this에는 Are가 아니라 Is를 쓰므로", "this에는 Is를 쓰고 pencil 앞에는 a를 쓰므로"],
  st="① <보기>에서 서로 맞지 않는 곳을 찾는다: {0} → ② 지시대명사·be동사·관사·명사의 수를 하나로 맞추면 {1} → ③ 정답은 {n}.",
  R=("Is this는 한 개인데 penciles는 복수 꼴이고, 자음 소리로 시작하는 pencil 앞에 an을 썼다.", "Is this a pencil?"), B=("Is this는 한 개인데 two bags는 두 개다.", "Are these two bags?"), C=("Are those는 여러 개인데 a car는 한 대다.", "Are those cars?"),
  D=("자음 소리로 시작하는 car 앞에 an을 썼다.", "Is that a car?"), E=("Is와 a orange는 한 개인데 these는 여러 개를 가리키고, 모음 소리로 시작하는 orange 앞에 a를 썼다.", "Is this an orange?"), F=("Are these는 여러 개인데 books 앞에 a를 썼다.", "Are these books?"))
RV(7, 49, "E", fx=True, why="변형과 수정 예시의 <보기>(Are those a apple?)가 C(Are those a car?)와 짜임이 같고 고친 문장도 같은 꼴(Are those + 복수 명사)이었다. 수정 예시를 지시어와 관사를 함께 고치는 문장(Is these a orange? → Is this an orange?)으로 바꿨다.")

X(7, 50, r="be동사를 주어 앞으로 옮기면 ‘~이니?’라고 묻는 의문문이 된다. 강조, 명사의 수, 낱말의 뜻 때문에 be동사가 앞으로 나오는 것이 아니다.",
  n=["강조하려고 be동사를 앞으로 옮기지 않으므로", "be동사를 주어 앞에 두면 묻는 문장이 되므로", "uncle은 한 명이고, 명사의 수는 be동사의 위치와 관계없으므로", "that의 뜻은 be동사의 위치와 관계없으므로", "평서문은 주어로 시작하므로"],
  st="① 평서문으로 바꿔 본다: {0} → ② be동사를 주어 앞으로 옮기고 물음표를 붙이면 ‘{1}’라고 묻는 문장이 된다. → ③ 이 이유를 말한 것은 {n}.",
  R=("That is your uncle.", "저분이 네 삼촌이니?"), B=("That is her teacher.", "저분이 그녀의 선생님이니?"), C=("This is your umbrella.", "이것이 네 우산이니?"), D=("These are your books.", "이것들이 네 책들이니?"),
  E=("Those are his cars.", "저것들이 그의 차들이니?"), F=("This is your bag.", "이것이 네 가방이니?"))
RV(7, 50, "B", v="수정(내용)", why="정답 ① 유일 확인. 다만 오답이 문장 속 낱말과 관계없는 짧은 일반론(‘명사를 강조하기 위해서이다’ 등)이고 정답만 길고 구체적이어서 길이만으로 답이 드러난다. 보기의 말투(‘~다.’)도 원문항(‘~해서/~때문에’)과 다르고, 정답 위치(①)가 C와 같다.", fix="오답을 문장 속 낱말을 두고 말하는 오개념으로, 말투를 원문항대로")
RV(7, 50, "D", fx=True, why="수정 예시의 정답(\"~이니?\"라고 묻는 의문문을 만들기 위해서)이 원문항 정답 문구와 거의 같았다. 이 문장에 맞춰 다시 썼다.")
