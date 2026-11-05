# 3급 CH7 의문사 (61~70) 2차 감수
X(3, 61, r="의문사는 묻는 정보에 따라 고른다: What(무엇), Who(누구), Where(어디), When(언제), Why(왜), How much(얼마).",
  n=["산 물건을 답했으므로 What(무엇)으로 물어야 하므로", "Who는 만난 사람을 묻는 말이므로", "Where는 간 곳을 묻는 말이므로", "When은 도착한 때를 묻는 말이므로", "How much는 쓴 돈을 묻는 말이므로"],
  st="① B의 대답이 알려 주는 정보가 무엇인지 본다: {0}. → ② 그 정보를 묻는 의문사는 {1}. → ③ 정답은 {n}.",
  R=("산 물건(a new laptop and a smartphone)", "What(무엇)이다"), B=("함께 점심을 먹은 사람(my cousin)", "Who(누구)다"), C=("간 곳(Busan)", "Where(어디)다"), D=("값(thirty dollars)", "How much(얼마)다"),
  E=("떠난 때(at nine)", "When(언제)이다"), F=("이유(Because ~)", "Why(왜)다"))

X(3, 62, r="의문사와 대답은 정보의 종류가 맞아야 한다. When - 때, Where - 장소, Why - 이유, How often - 횟수, What time - 시각.",
  n=["횟수를 묻고 횟수(Twice a week)로 답해 자연스러우므로", "산 곳을 묻고 online이라고 답해 자연스러우므로", "이유를 묻고 이유로 답해 자연스러우므로", "When으로 때를 물었는데 장소(on the third floor)로 답했으므로", "시각을 묻고 시각으로 답해 자연스러우므로"],
  st="① 대화마다 A의 의문사와 B가 답한 정보의 종류를 짝지어 본다. When - 때, Where - 장소, How long - 걸린 시간, How old - 나이, Why - 이유다. → ② 짝이 어긋난 대화를 찾는다. → ③ {n}: {0}",
  R="When(언제)으로 물었는데 장소(on the third floor)로 답했다.", B="How long(얼마나 오래)으로 물었는데 함께 본 사람을 답했다.", C="Why(왜)로 물었는데 시각(At six o'clock)을 답했다.",
  D="Where(어디)로 물었는데 때(Yesterday morning)를 답했다.", E="What time(몇 시)으로 물었는데 장소(At the bus stop)를 답했다.", F="How old(몇 살)로 물었는데 색깔을 답했다.")

X(3, 63, r="How many 뒤에는 셀 수 있는 복수 명사를, How much 뒤에는 셀 수 없는 명사를 쓴다.",
  n=["milk는 셀 수 없는 명사라 much가 들어간다.", "cookies는 셀 수 있는 복수 명사라 many가 들어간다. 나머지 넷(much)과 다르다.", "homework는 셀 수 없는 명사라 much가 들어간다.", "sugar는 셀 수 없는 명사라 much가 들어간다.", "water는 셀 수 없는 명사라 much가 들어간다."],
  st="① 빈칸 뒤 명사가 셀 수 있는지 본다. 셀 수 있는 복수 명사 앞은 How many, 셀 수 없는 명사 앞은 How much다. → ② 명사 끝의 복수형 -s가 단서다. {0} → ③ 나머지와 다른 것은 {n}이다.",
  R="cookies만 복수 명사라 many이고, milk, homework, sugar, water는 셀 수 없어 much다.", B="juice만 셀 수 없어 much이고, pencils, eggs, friends, pages는 복수 명사라 many다.",
  C="tickets만 복수 명사라 many이고, bread, salt, information, furniture는 셀 수 없어 much다.", D="classes만 복수 명사라 many이고, coffee, paper, advice, soup은 셀 수 없어 much다.",
  E="snow만 셀 수 없어 much이고, dogs, windows, songs, questions는 복수 명사라 many다.", F="letters만 복수 명사라 many이고, oil, cheese, tea, luggage는 셀 수 없어 much다.")

X(3, 64, r="How 뒤에는 형용사·부사가 와서 ‘얼마나 ~’를 묻고(How big, How far, How often), What 뒤에는 명사가 와서 ‘무슨 ~’를 묻는다(What size, What color).",
  n=["big은 형용사라 How가 들어간다.", "far는 형용사·부사라 How가 들어간다.", "often은 부사라 How가 들어간다.", "size는 명사라 What이 들어간다. 나머지 넷(How)과 다르다.", "long은 형용사·부사라 How가 들어간다."],
  st="① 빈칸 뒤의 말이 형용사·부사인지 명사인지 본다. How + 형용사·부사(얼마나 ~), What + 명사(무슨 ~)다. → ② {0} → ③ 나머지와 다른 것은 {n}이다.",
  R="size만 명사라 What이고, big, far, often, long은 형용사·부사라 How다.", B="long만 형용사라 How이고, color, kind, subject, time은 명사라 What이다.", C="sport만 명사라 What이고, heavy, often, deep, many는 형용사·부사라 How다.",
  D="wide만 형용사라 How이고, language, season, grade, animal은 명사라 What이다.", E="month만 명사라 What이고, hot, much, early, high는 형용사·부사라 How다.", F="well만 부사라 How이고, movie, floor, song, team은 명사라 What이다.")

X(3, 65, r="be동사의 과거형은 주어가 you·복수이면 were, I·3인칭 단수이면 was다. did로 만든 의문문에서 did 뒤의 동사는 동사원형이다.",
  n=["you에는 was가 아니라 were를 쓰고, did 뒤는 과거분사가 아니므로", "you의 be동사 과거형은 were, did 뒤에는 동사원형을 쓰므로", "are는 과거형이 아니고 did 뒤에 현재분사도 쓰지 않으므로", "did 뒤에 과거형을 쓸 수 없으므로", "be는 과거형이 아니므로"],
  st="① 문장 ⓐ의 주어({0})에 맞는 be동사 과거형을 정한다. {1} → ② 문장 ⓑ는 did로 만든 의문문이다. did 뒤의 동사는 과거형이 아니라 동사원형이다({2}). → ③ 정답은 {n}.",
  R=("you", "you에는 were를 쓴다.", "went → go"), B=("your sister", "3인칭 단수이므로 was를 쓴다.", "said → say"), C=("they", "복수이므로 were를 쓴다.", "bought → buy"), D=("Tom", "3인칭 단수이므로 was를 쓴다.", "came → come"),
  E=("we", "복수이므로 were를 쓴다.", "saw → see"), F=("Jane", "3인칭 단수이므로 was를 쓴다.", "ate → eat"))

X(3, 66, r="셀 수 없는 명사의 양은 How much로, 셀 수 있는 복수 명사의 수는 How many로 묻는다.",
  n=["many는 셀 수 있는 복수 명사 앞에 쓰므로", "money는 셀 수 없는 명사라 How much로 물으므로", "How a lot으로는 묻지 않으므로", "How lots로는 묻지 않으므로", "How few money라고 쓰지 않으므로"],
  st="① 빈칸 뒤 명사가 셀 수 있는지 본다({0}). → ② 셀 수 없는 명사의 양은 How much, 셀 수 있는 복수 명사의 수는 How many로 묻는다. → ③ 정답은 {a}.",
  R="money, 셀 수 없음", B="milk, 셀 수 없음", C="books, 복수 명사", D="water, 셀 수 없음", E="students, 복수 명사", F="time, 셀 수 없음")

X(3, 67, r="조동사 will이 있는 의문사 의문문은 ‘의문사 + will + 주어 + 동사원형 ~?’ 순서다. do/does를 덧붙이지 않는다.",
  n=["의문사 + will + 주어 + 동사원형으로 바르게 고쳤으므로", "어순이 그대로이고 will 뒤에 meets도 쓸 수 없으므로", "will이 있는 의문문에 do를 쓰지 않으므로", "주어 you가 동사 meet 뒤에 놓였으므로", "will이 있는 의문문에 are를 쓰지 않으므로"],
  st="① 조동사 will이 있는 의문문의 어순은 ‘의문사 + will + 주어 + 동사원형’이다. → ② 주어진 문장은 주어({0})가 will 앞에 있다. will을 주어 앞으로 옮긴다. → ③ do/does를 덧붙이거나 will be를 쓰거나 어순이 그대로인 것은 틀린다. 정답은 {n}.",
  R="you", B="you", C="she", D="they", E="Tom", F="we")

X(3, 68, r="의문사가 있는 일반동사 의문문은 ‘의문사 + do/does/did + 주어 + 동사원형 ~?’ 순서다.",
  n=["How + do + you + get 순서로 바르게 배열했으므로", "do가 주어 you 앞에 와야 하므로", "주어 you가 동사 get 앞에 와야 하므로", "do가 문장 끝에 놓였으므로", "주어 you와 do의 자리가 모두 틀렸으므로"],
  st="① 의문사({0})를 맨 앞에 둔다. → ② 그 뒤는 ‘{1} + 주어({2}) + 동사원형({3})’ 순서다. → ③ 이 순서인 {n}을 고른다.",
  R=("How", "do", "you", "get"), B=("How", "did", "you", "hear"), C=("How", "does", "she", "study"), D=("How", "do", "they", "get"), E=("How", "does", "Tom", "get"), F=("How", "do", "we", "get"))
RV(3, 68, "B", fx=True, why="수정 예시의 오답에 제시어에 없는 낱말(What, heard)이 섞여 있어, 원문항처럼 주어진 낱말의 순서만 바꾼 오답으로 다시 썼다.")
RV(3, 68, "CDEF", v="수정(내용)", why="정답 확인. 다만 오답에 제시어에 없는 낱말(What, do ↔ does)이 섞여 있어 주어진 낱말과 대조만 해도 두 개가 지워진다. 원문항의 오답은 모두 주어진 낱말의 순서만 바꾼 것이다.", fix="오답을 제시어의 순서만 바꾼 문장으로")

X(3, 69, r="How + 형용사·부사는 정도를 묻는다: How long(길이·시간), How far(거리), How often(횟수), How big(크기), How old(나이).",
  n=["ⓑ(얼마나 멀어요)에 쓰이므로", "ⓓ(얼마나 크니)에 쓰이므로", "ⓒ(얼마나 자주)에 쓰이므로", "나이를 묻는 문장이 없어 쓰이지 않으므로", "ⓐ(얼마나 길었나요)에 쓰이므로"],
  st="① 문장마다 우리말의 ‘얼마나 ~’에 맞는 How + 형용사·부사를 채운다. → ② {0}. → ③ 네 문장 어디에도 쓰이지 않은 {a}가 정답이다.",
  R="ⓐ How long(얼마나 긴), ⓑ How far(얼마나 먼), ⓒ How often(얼마나 자주), ⓓ How big(얼마나 큰)", B="ⓐ How wide, ⓑ How tall, ⓒ How early, ⓓ How heavy", C="ⓐ How tall, ⓑ How heavy, ⓒ How fast, ⓓ How old",
  D="ⓐ How many, ⓑ How much, ⓒ How long, ⓓ How often", E="ⓐ How old, ⓑ How far, ⓒ How often, ⓓ How long", F="ⓐ How interesting, ⓑ How quietly, ⓒ How much, ⓓ How big")
RV(3, 69, "CDEF", v="수정(표기)", why="정답 확인. 다만 원문항은 우리말과 영어 문장을 줄을 나누어 쓰고 빈칸이 두 칸(_____ _____)인데, 변형은 한 줄에 이어 쓰고 빈칸이 한 칸이다(같은 결함으로 다른 문항은 ‘수정(표기)’였다).", fix="줄을 나누고 빈칸을 두 칸으로")

X(3, 70, r="우리말 질문이 묻는 정보에 맞는 의문사를 고른다. 의문사가 주어일 때는 did 없이 ‘의문사 + 동사’로 쓴다(What caused the accident?).",
  n=["When은 ‘언제’를 묻는 질문이라 우리말과 맞지 않으므로", "Where는 ‘어디서’를 묻는 질문이라 우리말과 맞지 않으므로", "Who는 ‘누가 다쳤는지’를 묻는 질문이라 우리말과 맞지 않으므로", "‘무엇이 사고를 유발했니’를 What caused ~로 바르게 물었으므로", "Why는 ‘왜’를 묻는 질문이라 우리말과 맞지 않으므로"],
  st="① 우리말 질문(‘{0}’)에서 묻는 정보를 찾는다. → ② A의 대답({1})이 그 정보를 답하는지 확인한다. → ③ 그 정보를 묻는 의문사({2})로 시작하는 {n}이 정답이다.",
  R=("무엇이 그 사고를 유발했니?", "A student's careless behavior caused ~", "What, 주어를 묻기 때문에 did 없이 What caused ~"), B=("어디로 현장 학습을 갔니?", "We went to the science museum.", "Where"),
  C=("할머니께 무엇을 선물했니?", "We gave her a warm scarf.", "What"), D=("얼마나 오래 연습했니?", "She practiced for three hours.", "How long"), E=("왜 버스를 놓쳤니?", "Because his alarm clock didn't ring.", "Why"),
  F=("어떤 동물을 가장 좋아했니?", "She liked the baby giraffe the most.", "Which animal"))
