# 6급 CH6 의문사 의문문 (51~60) 2차 감수
X(6, 51, r="의문사 의문문은 who, what, when, where, why, how로 시작한다. be동사·do/does·조동사로 시작하는 의문문은 Yes/No로 답하는 의문문이다.",
  n=["be동사 Are로 시작하고 의문사가 없으므로", "의문사 Who로 시작하므로", "의문사 What으로 시작하므로", "의문사 When으로 시작하므로", "의문사 Where로 시작하므로"],
  st="① 문장마다 첫 낱말만 본다. → ② who, what, when, where, why, how가 아닌 것을 찾는다. → ③ {0} 정답은 {n}.",
  R="①은 be동사 Are로 시작한다.", B="③은 be동사 Is로 시작한다.", C="①은 Do로 시작한다.", D="④는 조동사 Can으로 시작한다.", E="②는 조동사 Can으로 시작한다. 나머지는 의문사 뒤에 can이 온다.", F="⑤는 be동사 Was로 시작한다.")
RV(6, 51, "B", v="수정(내용)", why="정답 ① 유일 확인. 다만 ⑤(Who is she?)가 원문항 ②와 똑같은 문장이고 정답 위치도 원문항과 같다(①).", fix="겹치는 문장을 바꾸고 정답 위치를 옮김")
RV(6, 51, "E", v="수정(내용)", why="정답 ① 유일 확인. 다만 정답 문장(Can you swim?)이 D의 정답(Can Mina swim?)과 거의 같고(유형 간 중복), 정답 위치도 원문항·B·C와 같다(①).", fix="정답 문장을 바꾸고 위치를 옮김")

X(6, 52, r="의문사의 뜻: when 언제, where 어디, who 누구, what 무엇, why 왜, how 어떻게, which 어느 것.",
  n=["What은 ‘무엇’이므로", "Who는 ‘누구’이므로", "How는 ‘어떻게’이므로", "When이 ‘언제’이므로", "Which는 ‘어느 것’이므로"],
  st="① 우리말에서 묻는 말을 찾는다: ‘{0}’. → ② 그 뜻의 의문사는 {a}. → ③ 정답은 {n}.",
  R="언제", B="누구", C="어디에", D="무엇을", E="왜", F="어떻게")
RV(6, 52, "F", fx=True, why="수정 예시의 문장(How do you go to school?)이 같은 단원 54번 원문항 ⑤(How does he go to school?)와 거의 같아 다른 문장(How do you make kimchi?)으로 바꿨다.")

X(6, 53, r="How + 형용사/부사(long, fast, old, tall, often, much, many)는 ‘얼마나 ~’를 묻는다. 명사(color, time, day) 앞에서 ‘무슨 ~’을 물을 때는 What을 쓴다.",
  n=["How long(얼마나 오래)이므로", "How fast(얼마나 빠른)이므로", "명사 color 앞이라 What(Which)을 쓰므로", "How old(몇 살)이므로", "How tall(얼마나 큰)이므로"],
  st="① 빈칸 바로 뒤의 낱말을 본다. 형용사·부사면 How, 명사면 What이다. → ② {0} → ③ 정답은 {n}.",
  R="color만 명사다(What color).", B="language만 명사다(What language).", C="time만 명사다(What time). How are you?는 How만으로 상태를 묻는다.", D="day만 명사다(What day).", E="sport만 명사다(What sport).",
  F="subject만 명사다(What subject).")

X(6, 54, r="의문사 + do/does + 주어 + 동사원형 ~?에서 do/does는 뒤의 주어에 맞춘다. 3인칭 단수면 does, 그 밖에는 do다.",
  n=["she에 does를 바르게 썼으므로", "복수 주어 they에는 do를 써야 하므로", "your uncle에 does를 바르게 썼으므로", "the store에 does를 바르게 썼으므로", "he에 does를 바르게 썼으므로"],
  st="① 밑줄 바로 뒤의 주어를 본다. → ② 주어가 3인칭 단수면 does, 아니면 do인지 맞춰 본다. → ③ {0} 정답은 {n}.",
  R="②의 주어 they는 복수라 do다.", B="④의 주어 you에는 do를 쓴다.", C="③의 주어 Jane은 3인칭 단수라 does다.", D="①의 주어 Tom은 3인칭 단수라 does다.", E="②의 주어 they는 복수라 do다.", F="⑤의 주어 Jiho는 3인칭 단수라 does다.")

X(6, 55, r="What day는 요일, What date는 날짜, What time은 시각을 묻는다. month는 달, year는 연도, season은 계절이다.",
  n=["요일을 묻고 요일로 답했으므로", "날짜를 묻고 날짜로 답했으므로", "시각을 묻고 시각으로 답했으므로", "day는 요일을 묻는데 날짜(December 25th)로 답했으므로", "날짜를 묻고 날짜로 답했으므로"],
  st="① 밑줄 친 낱말이 무엇을 묻는지 적는다(day 요일, date 날짜, time 시각, month 달, year 연도, season 계절). → ② 대답이 같은 종류인지 견준다. → ③ {0} 정답은 {n}.",
  R="④는 요일을 묻는데 날짜로 답했다.", B="④는 달을 묻는데 요일(Tuesday)로 답했다.", C="①은 날짜를 묻는데 요일(Friday)로 답했다.", D="③은 시각을 묻는데 요일(on Monday)로 답했다.",
  E="⑤는 계절을 묻는데 시각(10 o'clock)으로 답했다.", F="②는 연도를 묻는데 달(In March)로 답했다.")

X(6, 56, r="형용사·부사 앞에서 ‘얼마나 ~’를 묻는 의문사는 How다(How old, How tall, How long, How often, How far, How heavy).",
  n=["What은 형용사 old 앞에서 정도를 묻지 못하므로", "Who는 ‘누구’를 묻는 말이므로", "How old로 나이를 물으므로", "Where는 ‘어디’를 묻는 말이므로", "Why는 ‘왜’를 묻는 말이므로"],
  st="① 빈칸 바로 뒤의 낱말을 본다: {0}. 형용사(부사)다. → ② 형용사·부사 앞에서 ‘얼마나’를 묻는 말은 How뿐이다: {1}. → ③ 정답은 {n}.",
  R=("old", "How old(몇 살)"), B=("tall", "How tall(키가 얼마나)"), C=("long", "How long(길이가 얼마나)"), D=("often", "How often(얼마나 자주)"), E=("far", "How far(얼마나 멀리)"), F=("heavy", "How heavy(얼마나 무거운)"))

X(6, 57, r="일반동사가 있는 의문사 의문문은 의문사 + do/does + 주어 + 동사원형 ~?이다.",
  n=["What + does + he + 동사원형 like로 바르게 옮겼으므로", "What is he like?는 ‘그는 어떤 사람이니?’라는 다른 뜻이므로", "does 없이 평서문 어순으로 썼으므로", "3인칭 단수 주어 he에는 does를 써야 하므로", "does 뒤에는 동사원형 like를 써야 하므로"],
  st="① 우리말에서 의문사를 정한다: {0}. → ② 주어({1})에 맞는 do/does와 동사원형을 정한다: {2}. → ③ 의문사 + {2}의 순서인 것을 고른다. 정답은 {n}.",
  R=("‘무엇을’ → What", "he", "does he like"), B=("‘무엇을’ → What", "Tom", "does Tom want"), C=("‘어디에’ → Where", "she", "does she live"), D=("‘왜’ → Why", "you", "do you run"),
  E=("‘언제’ → When", "they", "do they study"), F=("‘어떻게’ → How", "she", "does she get to work"))
RV(6, 57, "F", fx=True, why="수정 예시의 정답(How does he go to school?)이 같은 단원 54번 원문항 ⑤와 똑같은 문장이어서 다른 문장(How does she get to work?)으로 바꿨다.")

X(6, 58, r="의문사 + do/does + 주어 + 동사원형 ~? 3인칭 단수의 -s는 does에만 붙이고 뒤의 동사는 원형으로 쓴다.",
  n=["does 뒤에 -ing형을 쓸 수 없으므로", "단수 주어 the store에는 does를 써야 하므로", "does + the store + 동사원형 open으로 바르게 고쳤으므로", "뜻이 ‘가게가 열려 있니’로 달라지고 When과도 어울리지 않으므로", "does 뒤에 과거형을 쓸 수 없으므로"],
  st="① 주어를 본다: {0}. → ② 조동사는 {1}, 뒤의 동사는 원형 {2}. → ③ 정답은 {a}.",
  R=("the store(3인칭 단수)", "does", "open"), B=("Tom(3인칭 단수)", "does", "run"), C=("she(3인칭 단수)", "does", "work"), D=("you", "do", "like"), E=("Tom(3인칭 단수)", "does", "like"), F=("they(복수)", "do", "study"))
RV(6, 58, "CD", v="수정(내용)", why="정답 유일 확인. 다만 고친 문장(C: Where does she live? / D: Why do you run?)이 같은 유형 57번의 정답 문장과 똑같아, 두 문항을 함께 풀면 한 문항이 다른 문항의 답을 알려 준다(문항 간 단서). 발문에도 정답 형식을 알려 주는 말이 붙었다.", fix="동사를 바꾸고 발문을 원문항대로")

X(6, 59, r="일반동사 의문문에서 주어가 3인칭 단수(he, she, it)이면 does, 그 밖(I, you, we, they)이면 do를 쓴다.",
  n=["he는 말하는 사람(1인칭)이 아니므로", "he는 듣는 사람(2인칭)이 아니므로", "he는 1인칭이 아니므로", "he는 한 사람이라 복수가 아니므로", "he는 나와 너가 아닌 제3자 한 사람이라 3인칭 단수이므로"],
  st="① <보기>의 주어를 찾는다: {0}. → ② 인칭(나·우리 = 1인칭, 너 = 2인칭, 그 밖 = 3인칭)과 수(한 사람인지 여럿인지)를 정한다: {1}. → ③ 정답은 {n}.",
  R=("he", "3인칭 단수 → does"), B=("we", "1인칭 복수 → do"), C=("they", "3인칭 복수 → do"), D=("I", "1인칭 단수 → do"), E=("she", "3인칭 단수 → does"), F=("you", "2인칭 → do"))
RV(6, 59, "D", v="수정(내용)", why="정답 ③ 유일 확인. 다만 주어(he)와 정답(3인칭 단수)이 원문항과 똑같고, E의 정답도 3인칭 단수다. 빈칸의 밑줄도 빠져 있다.", fix="주어를 바꿔 정답이 겹치지 않게, 빈칸 밑줄을 되살림")

X(6, 60, r="의문사 + do/does + 주어 + 동사원형 ~? 주어가 3인칭 단수면 does, 복수면 do를 쓴다.",
  n=["단수 주어 the boy에는 does를 써야 하므로", "복수 주어 your friends에는 do를 써야 하므로", "단수 주어 your teacher에는 does를 써야 하므로", "복수 주어 the students에는 do를 써야 하므로", "단수 주어 your uncle에 does를 바르게 썼으므로"],
  st="① 문장마다 주어가 단수인지 복수인지 가른다(-s가 붙은 명사, they는 복수). → ② 단수면 does, 복수면 do인지, 뒤의 동사가 원형인지 본다. → ③ {0} 정답은 {n}.",
  R="⑤만 단수 주어 your uncle + does로 바르다.", B="③만 복수 주어 they + do + study로 바르다.", C="④만 단수 주어 the concert + does로 바르다.", D="①만 복수 주어 the pandas + do로 바르다.",
  E="③만 복수 주어 the students + do로 바르다.", F="②만 단수 주어 your little brother + does로 바르다.")
RV(6, 60, "B", v="수정(내용)", why="정답 ⑤ 유일 확인. 다만 정답 문장(When do they study?)의 틀린 짝(③ When does they study?)이 함께 있어 둘만 견주면 답이 나오고, ④(Where does your uncle lives?)는 원문항 정답(Where does your uncle live?)을 틀리게 바꾼 문장이다. 정답 위치도 원문항과 같고 발문에 조건이 붙었다.", fix="③·④를 다른 문장으로, 정답 위치와 발문 조정")
