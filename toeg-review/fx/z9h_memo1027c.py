# 2026-10-27 3차 감수 반영(사용자: 4급 E 1차 감수 완료). 확인 완료가 아닌 4급 E 부적합 8건을 고치고,
# 같은 번호의 F(아직 감수 전, DB 문서 없음) 중 같은 결함이 있는 것도 함께 고친다. 확인 완료 문서는 건드리지 않는다.
def ADD(g_, n_, t_, more): return (OLD(g_, n_, t_).get("s", "") + " " + more).strip()
M = "감수 메모 반영(10-27 3차): "
SAME = "같은 번호 E 메모에 맞춘 수정(10-27 3차): "
STEP = "풀이 순서 정정(10-27): 풀이 순서가 예전 문항의 낱말을 설명하고 있어 지금 문항에 맞게 고쳤다."

# ---- 4-6 (E 메모: 대답 Two.가 성의 없다) ----
RE(4, 6, "E", s=ADD(4, 6, "E", M + "대답을 한 낱말(Two.)이 아니라 원문항처럼 완전한 문장으로 쓰고 대화를 원문항 길이 이상으로 늘렸다. 풀이 순서가 다른 명사(sheep)를 설명하던 것도 고쳤다."),
   p="A: How many ________ did your cat catch last night?\nB: It caught two in the kitchen.")
RE(4, 6, "F", s=ADD(4, 6, "F", SAME + "대답이 한 낱말(Three.)이던 것을 완전한 문장으로 쓰고 대화를 원문항 길이 이상으로 늘렸다. 풀이 순서가 다른 명사(deer)를 설명하던 것도 고쳤다."),
   p="A: How many ________ live in this forest?\nB: I think there are three near the river.")

# ---- 4-10 (E 메모: 문장이 짧음 — 10-27 2차에서 늘린 것보다 조금 더 늘린다) ----
RE(4, 10, "E", s=ADD(4, 10, "E", M + "(A)~(D) 문장을 원문항 길이 이상으로 늘렸다. 밑줄과 정답은 그대로다."),
   p="(A) I need <u>some moneys</u> for the bus ride.\n(B) There are <u>two mans</u> at the front door.\n(C) He plays <u>the soccer</u> after school every day.\n(D) She sees <u>an dog</u> in the park.")

# ---- 4-36 (E는 원안 그대로 쓰던 문항) ----
RE(4, 36, "E", s=M + "문장을 원문항 길이 이상으로 늘렸다(There ___ a big old tree in front of our school last year.). 보기와 정답은 그대로다. 정답 위치 ④.",
   p="There ________ a big old tree in front of our school last year.", c=["be", "are", "is", "was", "were"], a=4,
   r="There is/are 구문의 be동사는 뒤에 오는 명사의 수에 맞추고, 과거를 나타내는 말(yesterday, last ~, ~ ago)이 있으면 was/were를 쓴다.",
   k="last year가 있어 과거이고 뒤의 명사 a big old tree가 단수이므로 was가 들어간다. 정답은 ④이다.",
   n=["be는 동사원형이라 There 뒤 동사 자리에 그대로 쓸 수 없으므로 오답이다.", "are는 현재형이고 복수명사에 쓰므로 last year(과거)와 단수 a big old tree에 맞지 않아 오답이다.",
      "is는 현재형이라 last year(과거)와 맞지 않으므로 오답이다.", "과거(last year)이고 뒤의 명사 a big old tree가 단수이므로 was가 알맞아 정답이다.",
      "were는 복수명사에 쓰는 과거형이라 단수 a big old tree와 맞지 않으므로 오답이다."])

# ---- 4-39 ----
RE(4, 39, "E", s=ADD(4, 39, "E", M + "제시 문장과 보기 문장을 원문항 길이 이상으로 늘렸다(Tom's funny joke in class). 오답의 뜻(필요 없음·전혀 안 함·금지·도와줌)은 그대로다."),
   p="We cannot help laughing at Tom's funny joke in class.",
   c=["We don't need to laugh at Tom's funny joke in class.", "We didn't laugh at Tom's funny joke in class at all.", "We shouldn't laugh at Tom's funny joke in class.",
      "We cannot but laugh at Tom's funny joke in class.", "We can help you laugh at Tom's funny joke in class."],
   n=["‘웃을 필요가 없다’는 뜻이라 다르므로 오답이다.", "‘전혀 웃지 않았다’는 뜻이라 반대이므로 오답이다.", "‘웃으면 안 된다’는 뜻이라 다르므로 오답이다.",
      "cannot but + 동사원형으로 ‘~하지 않을 수 없다’는 같은 뜻을 나타내므로 정답이다.", "‘네가 웃도록 도울 수 있다’는 뜻이라 다르므로 오답이다."])
RE(4, 39, "F", s=ADD(4, 39, "F", SAME + "E 메모(원문항보다 짧음)와 같은 결함이라 제시 문장과 보기 문장을 원문항 길이 이상으로 늘렸다(the news from school)."),
   p="They cannot help talking about the news from school.",
   c=["They don't want to talk about the news from school.", "They mustn't talk about the news from school.", "They hardly talk about the news from school.",
      "They can help us talk about the news from school.", "They cannot but talk about the news from school."])

# ---- 4-46 (E·F는 원안 보기를 쓰던 문항) ----
R46 = "조동사 will 뒤에는 주어의 인칭·수와 관계없이 동사원형을 쓴다. will 뒤에 to, -s, be동사를 붙이지 않는다."
RE(4, 46, "E", s=ADD(4, 46, "E", M + "문장을 원문항 길이 이상으로 늘렸다(They ___ soccer with their friends in the park tonight.). 보기와 정답은 그대로다."),
   p="They ________________ soccer with their friends in the park tonight.", r=R46,
   k="tonight는 미래이고 will 뒤에는 동사원형을 쓰므로 will play가 알맞다. 정답은 ③이다.",
   n=["does + 동사원형은 미래를 나타내지 못하고, 주어 They에는 does를 쓰지 않으므로 오답이다.", "be동사와 일반동사 원형을 함께 쓸 수 없으므로 오답이다.",
      "will + 동사원형으로 tonight(오늘 밤)의 일을 나타내므로 정답이다.", "will 뒤에 to를 쓰지 않으므로 오답이다.", "will 뒤에는 -s를 붙이지 않은 동사원형을 쓰므로 오답이다."])
RE(4, 46, "F", s=ADD(4, 46, "F", SAME + "E 메모(원문항보다 짧음)와 같은 결함이라 문장을 원문항 길이 이상으로 늘렸다(We ___ home early tomorrow morning for the trip.). 보기와 정답은 그대로다."),
   p="We ________________ home early tomorrow morning for the trip.", r=R46,
   k="tomorrow morning은 미래이고 will 뒤에는 동사원형을 쓰므로 will leave가 알맞다. 정답은 ③이다.",
   n=["will 뒤에 to를 쓰지 않으므로 오답이다.", "will 뒤에는 -s를 붙이지 않은 동사원형을 쓰므로 오답이다.", "will + 동사원형으로 tomorrow morning(내일 아침)의 일을 나타내므로 정답이다.",
      "does + 동사원형은 미래를 나타내지 못하고, 주어 We에는 does를 쓰지 않으므로 오답이다.", "be동사와 일반동사 원형을 함께 쓸 수 없으므로 오답이다."])

# ---- 4-74 ----
RE(4, 74, "E", s=ADD(4, 74, "E", M + "보기 문장을 원문항 길이 이상으로 늘렸다. 틀린 문장(③ the most easiest)은 그대로다."),
   c=["Today is much warmer than yesterday morning.", "Your idea is better than mine for the project.", "This is the most easiest test of this semester.",
      "He is the richest man in our small town.", "The movie was more exciting than the book."])
RE(4, 74, "F", s=ADD(4, 74, "F", SAME + "E 메모(원문항보다 짧음)와 같은 결함이라 보기 문장을 원문항 길이 이상으로 늘렸다. 틀린 문장(⑤ gooder)은 그대로다."),
   c=["Jane sings much better than me at school.", "Busan is smaller than Seoul in population.", "This is the worst day of my whole life.",
      "Math is the most difficult subject for me this year.", "He is gooder than me at math and science."])

# ---- 4-96 (F는 원안 그대로 쓰던 문항) ----
RE(4, 96, "E", s=ADD(4, 96, "E", M + "우리말과 문장을 원문항 길이 이상으로 늘렸다(Let's ___ home early today.). 보기와 정답은 그대로다."),
   p="오늘은 일찍 집에 가자.\n→ Let's ________ home early today.")
RE(4, 96, "F", s=SAME + "E 메모(원문항보다 짧음)와 같은 결함이라 우리말과 문장을 원문항 길이 이상으로 늘렸다(Let's ___ lunch together in the park.). 보기와 정답은 그대로다. 정답 위치 ③.",
   p="공원에서 같이 점심을 먹자.\n→ Let's ________ lunch together in the park.", c=["to eat", "eating", "eat", "eats", "is eat"], a=3,
   r="Let's 뒤에는 동사원형을 쓴다. be동사의 원형은 be다.",
   k="Let's 뒤에는 동사원형을 쓰므로 ‘점심을 먹다’의 eat이 알맞다. 정답은 ③이다.",
   n=["Let's 뒤에 to부정사를 쓸 수 없으므로 오답이다.", "Let's 뒤에 -ing형을 쓸 수 없으므로 오답이다.", "Let's + 동사원형 eat이므로 정답이다.",
      "Let's 뒤에 -s가 붙은 형태를 쓸 수 없으므로 오답이다.", "be동사와 일반동사를 함께 쓸 수 없으므로 오답이다."])

# ---- 4-97 ----
RE(4, 97, "E", s=ADD(4, 97, "E", M + "두 문장을 원문항 길이 이상으로 늘렸다(My little brother Tom runs very fast.). 보기와 정답은 그대로다."),
   p="My little brother Tom runs very fast.\n= ________ fast my little brother Tom runs!")
RE(4, 97, "F", s=ADD(4, 97, "F", SAME + "E 메모(원문항보다 짧음)와 같은 결함이라 두 문장을 원문항 길이 이상으로 늘렸다(That is a very cute little puppy.). 보기와 정답은 그대로다."),
   p="That is a very cute little puppy.\n= ________ a cute little puppy that is!",
   n=["뒤에 명사구(a cute little puppy)가 있어 How를 쓸 수 없으므로 오답이다.", "명사구 a cute little puppy를 강조하는 What 감탄문이므로 정답이다.",
      "강조어라 감탄문을 이 어순으로 시작하지 못하므로 오답이다.", "강조어라 감탄문을 이 어순으로 시작하지 못하므로 오답이다.", "강조어라 감탄문을 이 어순으로 시작하지 못하므로 오답이다."])

# ---- F 풀이 순서만 예전 문항을 설명하던 것(rv2/g9i_memo1027c.py에서 칸을 고침) ----
for n_ in (9, 32, 62):
    RE(4, n_, "F", s=ADD(4, n_, "F", STEP))
