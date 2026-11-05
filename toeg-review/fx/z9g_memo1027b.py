# 2026-10-27 2차 감수 반영(사용자: 4-94 C 확인 완료 해제, 4급 D 1차 감수 완료, 확인 완료 문항은 그대로).
# 확인 완료가 아닌 4-94 C와 4급 D 메모 15건을 고치고, 같은 번호의 E·F(아직 감수 전, DB 문서 없음) 중 같은 결함이 있는 것도 함께 고친다.
def ADD(g_, n_, t_, more): return (OLD(g_, n_, t_).get("s", "") + " " + more).strip()
M = "감수 메모 반영(10-27 2차): "
SAME = "같은 번호 D 메모에 맞춘 수정(10-27 2차): "
SAMEC = "같은 번호 C 메모에 맞춘 수정(10-27 2차): "
LONG = "문장을 원문항 길이 이상으로 늘렸다."
LONGC = "보기 문장을 원문항 길이 이상으로 늘렸다."

# ---- 4-94 (C 메모: 문장이 짧음) ----
RE(4, 94, "C", s=ADD(4, 94, "C", M + LONGC + " 틀린 문장(⑤ Don't makes)은 그대로다."),
   c=["What a big house your uncle has!", "Let's not waste water at home.", "Please sit down on this chair.", "Don't be afraid of the dog.", "Don't makes noise in the library."])
RE(4, 94, "E", s=ADD(4, 94, "E", SAMEC + "C 메모(원문항보다 짧음)와 같은 결함이라 " + LONGC),
   c=["Be careful on the icy road!", "What a great idea it is!", "Don't open the door for strangers.", "Let's to eat lunch together.", "How fast the train goes!"])
RE(4, 94, "F", s=ADD(4, 94, "F", SAMEC + "C 메모(원문항보다 짧음)와 같은 결함이라 " + LONGC),
   c=["How a nice weather it is!", "Let's take a short break.", "Please wait here for a minute.", "Don't be sad about the game.", "What an honest boy he is!"])

# ---- 4-10 ----
RE(4, 10, "D", s=ADD(4, 10, "D", M + "(A)~(D) " + LONG + " 밑줄과 정답은 그대로다."),
   p="(A) We eat <u>some rice</u> for dinner.\n(B) I saw three <u>mouses</u> in the kitchen.\n(C) She goes to school <u>by the bus</u> every morning.\n(D) He has <u>an umbrella</u> in his bag.")
RE(4, 10, "E", s=ADD(4, 10, "E", SAME + "(A)~(D) " + LONG + " 밑줄과 정답은 그대로다."),
   p="(A) I need <u>some moneys</u> for the bus.\n(B) There are <u>two mans</u> at the door.\n(C) He plays <u>the soccer</u> after school.\n(D) She sees <u>an dog</u> in the park.")
RE(4, 10, "F", s=ADD(4, 10, "F", SAME + "(A)~(D) " + LONG + " 밑줄과 정답은 그대로다."),
   p="(A) Mom bought <u>some bread</u> at the bakery.\n(B) There are three <u>women</u> in the shop.\n(C) Jane goes to school <u>by a bike</u> every day.\n(D) He has <u>a egg</u> in his lunch box.")

# ---- 4-100 ----
RE(4, 100, "D", s=ADD(4, 100, "D", M + "<보기> " + LONG + " 틀린 문장의 자리((A)·(C)·(D))와 정답은 그대로다."),
   p="<보기>\n(A) How kind your sister are!\n(B) What a nice day it is today!\n(C) How a tall boy your brother is!\n(D) What beautiful the flowers are!\n(E) How quickly the rabbit runs!",
   pre=["문장별 판정: (A) X. 3인칭 단수 주어 your sister에는 is를 쓴다.", "문장별 판정: (B) O. What + a + 형용사 + 명사 + 주어 + 동사이다.",
        "문장별 판정: (C) X. 명사구(a tall boy)가 있으면 What을 쓴다.", "문장별 판정: (D) X. 명사 없이 형용사만 오면 How를 쓴다.", "문장별 판정: (E) O. How + 부사 + 주어 + 동사이다."])
RE(4, 100, "E", s=ADD(4, 100, "E", SAME + "<보기> " + LONG + " 틀린 문장의 자리((B)·(C)·(D))와 정답은 그대로다."),
   p="<보기>\n(A) What an old house your grandma has!\n(B) How cute your puppies is!\n(C) What interesting book you have!\n(D) How a beautiful day we have!\n(E) What a smart boy your cousin is!",
   pre=["문장별 판정: (A) O. What + an + 형용사 + 명사 + 주어 + 동사이다.", "문장별 판정: (B) X. 복수 주어 your puppies에는 are를 쓴다.",
        "문장별 판정: (C) X. 단수명사 book 앞에 an이 빠졌다.", "문장별 판정: (D) X. 명사구(a beautiful day)가 있으면 What을 쓴다.", "문장별 판정: (E) O. What + a + 형용사 + 명사 + 주어 + 동사이다."])
RE(4, 100, "F", s=ADD(4, 100, "F", SAME + "<보기> " + LONG + " 틀린 문장의 자리((A)·(C)·(E))와 정답은 그대로다."),
   p="<보기>\n(A) How fast Tom run in the race!\n(B) What a lovely dog Jane has!\n(C) How a kind girl Mina is!\n(D) What beautiful flowers you grow!\n(E) How nice the weather are today!",
   pre=["문장별 판정: (A) X. 3인칭 단수 주어 Tom에는 runs를 쓴다.", "문장별 판정: (B) O. What + a + 형용사 + 명사 + 주어 + 동사이다.",
        "문장별 판정: (C) X. 명사구(a kind girl)가 있으면 What을 쓴다.", "문장별 판정: (D) O. What + 형용사 + 복수명사 + 주어 + 동사이다.", "문장별 판정: (E) X. 셀 수 없는 명사 weather에는 is를 쓴다."])

# ---- 4-106 (D는 변형 그대로 쓰던 문항) ----
R106 = "목적어는 동사가 나타내는 행동·상태의 대상(~을/를)이 되는 명사구 전체이다. 주어, 동사, 때·정도를 나타내는 부사어, 목적어를 꾸미는 말만 떼어 낸 것과 구별한다."
RE(4, 106, "D", s=M + "문장을 원문항 길이 이상으로 늘리고(Tom likes rock music very much.), 원문항처럼 목적어의 일부(rock)만 떼어 낸 보기를 넣었다. 정답 위치 ⑤.",
   p="Tom likes rock music very much.", c=["likes", "Tom", "very much", "rock", "rock music"], a=5, r=R106,
   k="동사 likes에 ‘무엇을?’이라고 물으면 rock music이 답이 되므로 목적어는 rock music이다. 정답은 ⑤이다.",
   n=["likes는 ‘좋아하다’라는 동사라 목적어가 아니므로 오답이다.", "Tom은 문장의 주어라 목적어가 아니므로 오답이다.", "very much는 정도를 나타내는 부사어라 목적어가 아니므로 오답이다.",
      "rock은 music을 꾸미는 말로 목적어의 일부일 뿐이라 오답이다.", "rock music은 동사 likes의 대상(무엇을?)이 되는 명사구 전체이므로 정답이다."])
RE(4, 106, "F", s=SAME + "D 메모(원문항보다 짧음)와 같은 결함이라 " + LONG + " ②를 really need로 바꿔 정답 보기만 두 낱말이던 것을 없앴다. 정답 위치 ⑤.",
   p="They really need some help today.", c=["They", "really need", "some", "today", "some help"], a=5, r=R106,
   k="동사 need에 ‘무엇을?’이라고 물으면 some help가 답이 되므로 목적어는 some help이다. 정답은 ⑤이다.",
   n=["They는 문장의 주어라 목적어가 아니므로 오답이다.", "really need는 부사 really와 동사 need로, 목적어가 아니므로 오답이다.", "some은 help를 꾸미는 말로 목적어의 일부일 뿐이라 오답이다.",
      "today는 때를 나타내는 부사어라 목적어가 아니므로 오답이다.", "some help는 동사 need의 대상(무엇을?)이 되는 명사구 전체이므로 정답이다."])

# ---- 4-15 ----
RE(4, 15, "D", s=ADD(4, 15, "D", M + "ⓐ~ⓓ " + LONG + " 옳고 틀림과 정답은 그대로다."),
   p="ⓐ The news from my sister are really good.\nⓑ Those bag on the desk is hers.\nⓒ This is Tom's new science book.\nⓓ The legs of the old table are short.",
   pre=["문장별 판정: ⓐ X. news는 단수 취급해 is를 쓴다.", "문장별 판정: ⓑ X. Those 뒤에는 복수명사 bags와 are를 쓴다(That bag is로 고쳐도 된다).",
        "문장별 판정: ⓒ O. 사람의 소유를 's로 나타냈다.", "문장별 판정: ⓓ O. 사물의 소유를 of로 나타내고 복수 legs에 are를 썼다."])
RE(4, 15, "E", s=ADD(4, 15, "E", SAME + "ⓐ~ⓓ " + LONG + " 옳고 틀림과 정답은 그대로다."),
   p="ⓐ Those red cars over there are theirs.\nⓑ This bag on the chair is her.\nⓒ The childrens' toys are all over the floor.\nⓓ My best friend's house is near the school.")
RE(4, 15, "F", s=ADD(4, 15, "F", SAME + "ⓐ~ⓓ " + LONG + " 옳고 틀림과 정답은 그대로다."),
   p="ⓐ This English book in my bag is mine.\nⓑ That is my little sister's new bike.\nⓒ These car is very fast and expensive.\nⓓ The news about the game are interesting.")

# ---- 4-17 (E·F는 변형 그대로 쓰던 문항) ----
R17 = "앞에 나온 사람·사물을 대명사로 받을 때는 수(단수·복수)와 성(남·여)을 맞추고, 동사 뒤 목적어 자리에는 목적격(me, you, him, her, it, us, them)을 쓴다."
RE(4, 17, "D", s=ADD(4, 17, "D", M + "대화문을 원문항 길이 이상으로 늘렸다. 보기와 정답은 그대로다. 정답 위치 ①."),
   p="A: Did you call Jane about the class party?\nB: Yes, I called ________ after dinner last night.", r=R17,
   k="빈칸은 동사 called 뒤 목적어 자리이고 Jane(여자 한 명)을 받으므로 목적격 her가 들어간다. 정답은 ①이다.",
   n=["Jane(여자 한 명)을 받는 목적격이므로 정답이다.", "me는 B 자신을 가리켜 Jane을 받을 수 없으므로 오답이다.", "him은 남자 한 명을 받는 목적격이라 Jane을 받을 수 없으므로 오답이다.",
      "they는 주격이고 복수라 동사 뒤 목적어 자리에서 Jane을 받을 수 없으므로 오답이다.", "you는 상대방 A를 가리켜 Jane을 받을 수 없으므로 오답이다."])
RE(4, 17, "E", s=SAME + "D 메모(원문항보다 짧음)와 같은 결함이라 대화문을 원문항 길이 이상으로 늘렸다. 보기와 정답은 그대로다. 정답 위치 ⑤.",
   p="A: Do you remember my parents from the school festival?\nB: Of course, I remember ________ very well.", c=["me", "her", "him", "you", "them"], a=5, r=R17,
   k="빈칸은 동사 remember 뒤 목적어 자리이고 my parents(복수)를 받으므로 목적격 them이 들어간다. 정답은 ⑤이다.",
   n=["me는 B 자신을 가리켜 my parents를 받을 수 없으므로 오답이다.", "her는 여자 한 명을 받는 목적격이라 복수인 my parents를 받을 수 없으므로 오답이다.",
      "him은 남자 한 명을 받는 목적격이라 복수인 my parents를 받을 수 없으므로 오답이다.", "you는 상대방 A를 가리켜 my parents를 받을 수 없으므로 오답이다.",
      "my parents(복수)를 받는 목적격이므로 정답이다."])
RE(4, 17, "F", s=SAME + "D 메모(원문항보다 짧음)와 같은 결함이라 대화문을 원문항 길이 이상으로 늘렸다. 보기와 정답은 그대로다. 정답 위치 ④.",
   p="A: Can you help me with my math homework after school?\nB: Sure, I can help ________ in the library.", c=["him", "her", "me", "you", "them"], a=4, r=R17,
   k="A가 자신을 가리킨 me는 대답하는 B의 처지에서 상대방이므로, 동사 help 뒤 목적어 자리에 you를 쓴다. 정답은 ④이다.",
   n=["him은 다른 남자를 가리켜 A를 받을 수 없으므로 오답이다.", "her는 다른 여자를 가리켜 A를 받을 수 없으므로 오답이다.",
      "me는 대답하는 B 자신을 가리켜, B가 A를 도와준다는 뜻이 되지 않으므로 오답이다.", "A가 말한 me는 B의 처지에서 상대방이므로 목적격 you가 들어가 정답이다.",
      "them은 여러 사람을 가리켜 A 한 사람을 받을 수 없으므로 오답이다."])

# ---- 4-18 ----
def N18(he, He, His, his, hes, noun, *wrong):
    a = f"(A) 빈칸 {{}}: 뒤에 동사가 없어 ‘{he}는 ~이다’의 {He}를 쓴다"; b = f"(B) 빈칸 {hes}: 명사 {noun} 앞이라 소유격 {his}를 쓴다"
    return [("모든 빈칸에 알맞은 말을 골랐으므로 정답이다." if w is None else ", ".join(x for x in [a.format(w[0]) if w[0] else "", b if w[1] else ""] if x) + ". 따라서 오답이다.") for w in wrong]
RE(4, 18, "D", s=ADD(4, 18, "D", M + LONG + " 빈칸과 보기, 정답은 그대로다."),
   n=N18("그", "He's(He is)", "His", "his", "he's", "older brother", None, ("His", 0), (None, 1), ("His", 1), ("He", 0)),
   p="- (<u>    A    </u>) Tom, my new classmate from Busan.\n- I know (<u>    B    </u>) older brother very well.")
RE(4, 18, "E", s=ADD(4, 18, "E", SAME + LONG + " 빈칸과 보기, 정답은 그대로다."),
   n=N18("그녀", "She's(She is)", "Her", "her", "she's", "younger sister", ("Her", 0), ("She", 0), None, (None, 1), ("Her", 1)),
   p="- (<u>    A    </u>) Jane, the new English teacher.\n- I know (<u>    B    </u>) younger sister well.")

# ---- 4-27 ----
RE(4, 27, "D", s=ADD(4, 27, "D", M + "대답과 보기 문장을 원문항 길이 이상으로 늘렸다(Jane eats an apple for breakfast every day.). 오답의 형식(의문사·진행형·Do·과거)은 그대로다."),
   p="A: __________________________________\nB: Yes, Jane eats an apple for breakfast every day.",
   c=["What does Jane eat for breakfast every day?", "Is Jane eating an apple for breakfast now?", "Do Jane eat an apple for breakfast every day?",
      "Does Jane eat an apple for breakfast every day?", "Did Jane eat an apple for breakfast yesterday?"], a=4,
   k="대답이 Yes로 시작하고 일반동사 현재형 eats를 썼으며 주어가 3인칭 단수 Jane이므로 Does Jane eat ~?으로 묻는다. 정답은 ④이다.",
   n=["의문사 의문문은 Yes/No로 답하지 않으므로 오답이다.", "진행형 질문에는 Yes, she is로 답하고, now도 대답의 every day와 맞지 않으므로 오답이다.",
      "3인칭 단수 주어 Jane에는 Do가 아니라 Does를 쓰므로 오답이다.", "3인칭 단수 주어 + Does + 동사원형의 현재 의문문이라 대답과 맞으므로 정답이다.",
      "과거 질문에는 Yes, she did로 답하므로 오답이다."])
RE(4, 27, "E", s=ADD(4, 27, "E", SAME + "대답과 보기 문장을 원문항 길이 이상으로 늘렸다. 오답의 형식은 그대로다."),
   p="A: __________________________________\nB: Yes, they play soccer in the park after school.",
   c=["What do they play in the park after school?", "Do they play soccer in the park after school?", "Does they play soccer in the park after school?",
      "Are they playing soccer in the park now?", "Did they play soccer in the park yesterday?"])
RE(4, 27, "F", s=ADD(4, 27, "F", SAME + "대답과 보기 문장을 원문항 길이 이상으로 늘렸다. 오답의 형식은 그대로다."),
   p="A: __________________________________\nB: Yes, I study English with my sister every day.",
   c=["What do you study with your sister every day?", "Are you studying English with your sister now?", "Does you study English with your sister every day?",
      "Did you study English with your sister yesterday?", "Do you study English with your sister every day?"])

# ---- 4-32 ----
RE(4, 32, "D", s=ADD(4, 32, "D", M + LONG + " 보기와 정답은 그대로다."), p="She _____ a new bag at the mall yesterday.")
RE(4, 32, "E", s=ADD(4, 32, "E", SAME + LONG + " 보기와 정답은 그대로다."), p="Tom _____ a funny movie with his friends last night.")

# ---- 4-42 ----
RE(4, 42, "D", s=ADD(4, 42, "D", M + "제시 문장과 보기 문장을 원문항 길이 이상으로 늘렸다(after school). 오답의 형식은 그대로다."),
   p="They are going to play soccer after school.",
   c=["They do not going to play soccer after school.", "They are not going to play soccer after school.", "They will are not going to play soccer after school.",
      "They are not go to play soccer after school.", "They not are going to play soccer after school."])
RE(4, 42, "E", s=ADD(4, 42, "E", SAME + "제시 문장과 보기 문장을 원문항 길이 이상으로 늘렸다(for school). 오답의 형식은 그대로다."),
   p="I am going to buy a new bag for school.",
   c=["I am not go to buy a new bag for school.", "I will am not going to buy a new bag for school.", "I not am going to buy a new bag for school.",
      "I am not going to buy a new bag for school.", "I do not going to buy a new bag for school."])
RE(4, 42, "F", s=ADD(4, 42, "F", SAME + "제시 문장과 보기 문장을 원문항 길이 이상으로 늘렸다(home ~ tomorrow). 오답의 형식은 그대로다."),
   p="We are going to leave home early tomorrow.",
   c=["We are not going to leave home early tomorrow.", "We are not go to leave home early tomorrow.", "We not are going to leave home early tomorrow.",
      "We will are not going to leave home early tomorrow.", "We do not going to leave home early tomorrow."])

# ---- 4-66 (D 메모: 정답 보기만 길다) ----
RE(4, 66, "D", s=ADD(4, 66, "D", M + "정답 보기(④)만 길어 드러나던 것을 모든 보기가 비슷한 길이가 되도록 다른 보기를 늘렸다. 원문항 길이 이상이다."),
   c=["There is <u>few</u> juice in the bottle.", "I need <u>a little</u> pens for class.", "He has <u>much</u> toys in his room.",
      "She drinks <u>a little</u> milk every day.", "We saw <u>many</u> snow on the mountain."])
RE(4, 66, "E", s=ADD(4, 66, "E", SAME + "D 메모와 같은 결함(보기 길이·원문항보다 짧음)이라 보기를 비슷한 길이로 원문항 길이 이상 늘렸다."),
   c=["We need <u>much</u> water for the plants.", "He has <u>a few</u> bread for lunch.", "There are <u>little</u> trees in this park.",
      "I read <u>much</u> books during the vacation.", "She has <u>many</u> homework to do today."])
RE(4, 66, "F", s=ADD(4, 66, "F", SAME + "D 메모와 같은 결함(보기 길이·원문항보다 짧음)이라 보기를 비슷한 길이로 원문항 길이 이상 늘리고, ①의 명사를 cousins로 바꿔 ②와 겹치지 않게 했다."),
   c=["I have <u>a little</u> cousins in Seoul.", "Tom has <u>few</u> friends in his class.", "She drinks <u>many</u> coffee every morning.",
      "There is <u>a few</u> rice in the bowl.", "We have <u>much</u> chairs in the classroom."],
   n=["셀 수 있는 명사 cousins에는 a few를 쓰므로 오답이다.", "셀 수 있는 명사 friends에 few를 바르게 썼으므로 정답이다.", "셀 수 없는 명사 coffee에는 much를 쓰므로 오답이다.",
      "셀 수 없는 명사 rice에는 a little을 쓰므로 오답이다.", "셀 수 있는 명사 chairs에는 many를 쓰므로 오답이다."])

# ---- 4-78 (정답 보기만 길던 것도 함께 맞춘다) ----
RE(4, 78, "D", s=ADD(4, 78, "D", M + LONGC + " 정답 보기(④)만 길던 것도 다른 보기를 늘려 비슷한 길이로 맞췄다."),
   c=["Mina is <u>the most kindest</u> friend in our class.", "That was <u>the baddest</u> movie of the year.", "He is <u>more stronger</u> than his older brother.",
      "My dog is <u>the cutest</u> dog in the world.", "It is <u>the usefulest</u> book in the library."])
RE(4, 78, "E", s=ADD(4, 78, "E", SAME + "D 메모(원문항보다 짧음)와 같은 결함이라 " + LONGC),
   c=["He is <u>the most fastest</u> runner in our school.", "That was <u>the most boring</u> class of the day.", "This is <u>the goodest</u> cake in this bakery.",
      "She is <u>the carefulest</u> driver in my family.", "It is <u>the most biggest</u> room in the house."])
RE(4, 78, "F", s=ADD(4, 78, "F", SAME + "D 메모(원문항보다 짧음)와 같은 결함이라 " + LONGC + " 정답 보기(⑤)만 길던 것도 비슷한 길이로 맞췄다."),
   c=["It is <u>the most coldest</u> city in Korea.", "This is <u>the difficultest</u> question on the test.", "This is <u>the most wonderfulest</u> trip of my life.",
      "She is <u>more busier</u> than her mother today.", "He is <u>the best</u> player on the soccer team."],
   n=["-est와 most를 겹쳐 쓸 수 없으므로 오답이다.", "긴 단어 difficult는 the most difficult로 써야 하므로 오답이다.", "-est와 most를 겹쳐 쓸 수 없으므로 오답이다.",
      "busier에 more를 겹쳐 쓸 수 없으므로 오답이다.", "good의 최상급 best를 바르게 썼으므로 정답이다."])

# ---- 4-79 ----
RE(4, 79, "D", s=ADD(4, 79, "D", M + "제시 문장과 보기 설명을 원문항 길이 이상으로 늘렸다. 오개념의 종류와 정답은 그대로다."),
   p="Tom is <u>taller than</u> his older brother Mike.",
   c=["'taller'는 'tall'의 최상급으로 '가장 키가 큰'이라는 뜻이다.", "'than' 뒤에는 비교 대상이 아니라 반드시 동사가 와야 한다.", "'taller' 앞에 'more'를 붙여 'more taller'로 써야 옳다.",
      "'than'은 '그때'라는 뜻으로, 'then'과 바꿔 써도 된다.", "'taller'는 'tall'의 비교급이고, 'than' 뒤에 비교 대상이 온다."],
   n=["taller는 ‘더 키가 큰’이라는 비교급이고 최상급은 tallest이므로 오답이다.", "than 뒤에는 비교 대상(his older brother Mike)이 오므로 오답이다.",
      "-er 비교급에 more를 겹쳐 쓰지 않으므로 오답이다.", "‘그때’는 then이고 than은 ‘~보다’라서 바꿔 쓸 수 없으므로 오답이다.",
      "비교급의 형태와 than 뒤의 비교 대상을 바르게 설명했으므로 정답이다."])
RE(4, 79, "E", s=ADD(4, 79, "E", SAME + "D 메모(원문항보다 짧음)와 같은 결함이라 제시 문장과 보기 설명을 늘리고, 정답 보기(①)만 길던 것도 비슷한 길이로 맞췄다."),
   p="This school bag is <u>heavier than</u> that one.",
   c=["'heavier'는 'heavy'의 y를 i로 바꾸고 '-er'을 붙인 비교급이다.", "'heavier'는 'heavy'에 '-ier'만 붙여 만든 최상급 표현이다.", "'than' 뒤의 'that one'은 비교 대상이 아니라 문장의 주어이다.",
      "'heavier' 대신 'more heavy'를 써도 같은 뜻으로 옳다.", "'than'은 '그러므로'라는 뜻으로 앞뒤 문장을 이어 준다."])
RE(4, 79, "F", s=ADD(4, 79, "F", SAME + "D 메모(원문항보다 짧음)와 같은 결함이라 제시 문장과 보기 설명을 늘리고, 정답 보기(③)만 길던 것도 비슷한 길이로 맞췄다."),
   p="Jane runs <u>faster than</u> her friend Amy.",
   c=["'faster'는 형용사 'fast'의 원급으로 '빠른'이라는 뜻을 나타낸다.", "'fast'는 부사이므로 비교급은 반드시 'more fast'로 써야 옳다.", "'faster'는 부사 'fast'의 비교급이고, 'than'으로 Amy와 비교한다.",
      "'than' 뒤에는 'Amy runs'처럼 반드시 동사까지 함께 써야 한다.", "'faster'는 '가장 빠르게'라는 뜻을 나타내는 최상급 표현이다."])

# ---- 4-80 ----
RE(4, 80, "D", s=ADD(4, 80, "D", M + "<보기> " + LONG + " 옳고 틀림과 정답은 그대로다."),
   p="<보기>\n(가) Tom is taller than his friend Ben in our class.\n(나) This is the easiest math test of the whole year.\n(다) Jane is more prettier than her older sister Amy.\n"
     "(라) He is the best player on our school soccer team.\n(마) Today is more hotter than yesterday in Seoul.")
RE(4, 80, "E", s=ADD(4, 80, "E", SAME + "<보기> " + LONG + " 옳고 틀림과 정답은 그대로다."),
   p="<보기>\n(가) This blue bag is more heavier than that red one.\n(나) Jane is the most beautiful girl in the class picture.\n(다) Tom is gooder than his friend Ben at soccer.\n"
     "(라) This is the worst day of the whole week for me.\n(마) The dog is bigger than the cat in the yard.")
RE(4, 80, "F", s=ADD(4, 80, "F", SAME + "<보기> " + LONG + " 옳고 틀림과 정답은 그대로다."),
   p="<보기>\n(가) The city of Seoul is larger than Busan in population.\n(나) Tom is the fastest runner in our whole school.\n(다) Jane is the most kindest student in our class.\n"
     "(라) This math test is more easier than the last one.\n(마) He is much better than me at drawing animals.")

# ---- 4-87 (D·E는 변형 그대로 쓰던 문항) ----
R87 = "for는 기간의 길이(an hour, two hours), during은 특정한 때(the lesson, the movie, the test) 앞에 쓰고, while은 뒤에 주어 + 동사가 오는 절을 이끈다."
W87 = "while은 주어 + 동사가 있는 절 앞에 쓴다(→ while)"; D87 = "during은 특정한 때를 나타내는 명사 앞에 쓴다(→ during)"; F87 = "for는 기간의 길이 앞에 쓴다(→ for)"
RE(4, 87, "D", s=M + "두 문장을 원문항 길이 이상으로 늘렸다. 보기와 정답은 그대로다. 정답 위치 ③.",
   p="I stayed at the library ________ two hours.\nMy brother slept ________ the boring movie.", r=R87,
   k="첫째 빈칸 뒤 two hours는 기간의 길이라 for, 둘째 빈칸 뒤 the boring movie는 특정한 때를 나타내는 명사구라 during이 알맞다. 정답은 ③이다.",
   n=[f"첫째 빈칸 during: {F87}. 따라서 오답이다.", f"첫째 빈칸 during: {F87}, 둘째 빈칸 for: {D87}. 따라서 오답이다.", "모든 빈칸에 알맞은 말을 골랐으므로 정답이다.",
      f"첫째 빈칸 while: {F87}, 둘째 빈칸 for: {D87}. 따라서 오답이다.", f"둘째 빈칸 while: {D87}. 따라서 오답이다."])
RE(4, 87, "E", s=SAME + "D 메모(원문항보다 짧음)와 같은 결함이라 두 문장을 원문항 길이 이상으로 늘렸다. 보기와 정답은 그대로다. 정답 위치 ②.",
   p="Jane called me ________ I was eating dinner.\nWe waited at the bus stop ________ thirty minutes.", r=R87,
   k="첫째 빈칸 뒤 I was eating dinner는 주어 + 동사라 while, 둘째 빈칸 뒤 thirty minutes는 기간의 길이라 for가 알맞다. 정답은 ②이다.",
   n=[f"첫째 빈칸 for: {W87}, 둘째 빈칸 during: {F87}. 따라서 오답이다.", "모든 빈칸에 알맞은 말을 골랐으므로 정답이다.", f"첫째 빈칸 for: {W87}, 둘째 빈칸 while: {F87}. 따라서 오답이다.",
      f"첫째 빈칸 during: {W87}. 따라서 오답이다.", f"첫째 빈칸 during: {W87}, 둘째 빈칸 during: {F87}. 따라서 오답이다."])
RE(4, 87, "F", s=ADD(4, 87, "F", SAME + "D 메모(원문항보다 짧음)와 같은 결함이라 두 문장을 원문항 길이 이상으로 늘렸다. 보기와 정답은 그대로다."),
   p="My phone rang ________ I was sleeping on the sofa.\nNobody in our class talked ________ the test.")

# ---- 4-90 ----
RE(4, 90, "D", s=ADD(4, 90, "D", M + "제시 문장과 보기 설명을 원문항 길이 이상으로 늘렸다(Do you have a piano lesson in Monday?). 정답 위치는 그대로다."),
   p="Do you have a piano lesson <u>in</u> Monday?",
   c=["'Monday'는 요일이므로, 요일 앞에서는 'in' 대신 반드시 전치사 'on'을 써야 한다.", "'Monday'는 한 주가 시작되는 긴 기간이라서 'in' 대신 'on'을 써야 한다.",
      "동사 'have'가 현재형이므로 그 시제에 맞추어 'in' 대신 'on'을 써야 한다.", "의문문(Do you ~?)에서는 시간을 나타내는 전치사로 'in'을 쓸 수 없게 정해져 있기 때문이다.",
      "'piano lesson' 같은 수업 이름 뒤에는 시간 표현과 상관없이 'on'을 쓰기 때문이다."],
   n=["요일 앞에는 on을 쓴다는 규칙을 바르게 설명했으므로 정답이다.", "요일은 긴 기간이 아니고, 긴 기간(월·계절·연도)에는 오히려 in을 쓰므로 오답이다.",
      "동사의 시제는 전치사 선택과 관계없으므로 오답이다.", "의문문에서도 뒤의 시간 표현이 달·계절·연도이면 in을 쓰므로 오답이다.",
      "수업 이름은 전치사 선택과 관계없고, 뒤의 시간 표현(요일)이 on을 정하므로 오답이다."])
RE(4, 90, "E", s=ADD(4, 90, "E", SAME + "D 메모(원문항보다 짧음)와 같은 결함이라 제시 문장과 보기 설명을 원문항 길이 이상으로 늘렸다. 정답 위치는 그대로다."),
   p="Our school starts <u>on</u> 8 o'clock every morning.",
   c=["'8 o'clock'은 하루를 가리키는 날짜이므로 'on' 대신 'at'을 써야 한다.", "'Our school'이 장소를 나타내므로 장소 전치사 'at'을 써야 하기 때문이다.",
      "동사 'starts'가 3인칭 단수 현재형이므로 시간 전치사로 'at'을 써야 한다.", "'every morning'처럼 아침 시간 전체를 나타낼 때는 'at'을 쓰기 때문이다.",
      "'8 o'clock'은 구체적인 시각이므로 'on' 대신 전치사 'at'을 써야 한다."],
   n=["8 o'clock은 날짜가 아니라 시각이므로 오답이다.", "장소가 아니라 뒤의 시간 표현으로 전치사를 정하므로 오답이다.", "동사의 형태는 전치사 선택과 관계없으므로 오답이다.",
      "8 o'clock은 아침 전체가 아니라 한 시각이고, 아침 전체는 in the morning으로 쓰므로 오답이다.", "구체적인 시각 앞에는 at을 쓴다는 규칙을 바르게 설명했으므로 정답이다."])
RE(4, 90, "F", s=ADD(4, 90, "F", SAME + "D 메모(원문항보다 짧음)와 같은 결함이라 제시 문장과 보기 설명을 원문항 길이 이상으로 늘렸다. 정답 위치는 그대로다."),
   p="My little cousin Tom was born <u>on</u> 2015 in Busan.",
   c=["'2015'는 달력에서 어느 특정한 하루를 나타내므로 'on' 대신 'in'을 써야 한다.", "연도 '2015'는 일 년이라는 긴 기간이므로 'on' 대신 전치사 'in'을 써야 한다.",
      "'born'이 과거분사이므로 그 뒤에는 시간과 상관없이 항상 'in'이 와야 한다.", "'was born' 같은 수동태 문장에서는 시간 전치사로 'on'을 쓸 수 없기 때문이다.",
      "주어가 'My little cousin Tom'처럼 사람이면 'in'을 써야 하기 때문이다."],
   n=["2015는 하루가 아니라 연도이므로 오답이다.", "연도처럼 긴 기간 앞에는 in을 쓴다는 규칙을 바르게 설명했으므로 정답이다.", "동사의 형태는 전치사 선택과 관계없으므로 오답이다.",
      "수동태 문장도 날짜 앞에는 on을 쓰므로 오답이다.", "주어(사람)는 전치사 선택과 관계없으므로 오답이다."])
