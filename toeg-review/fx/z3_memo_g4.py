# 2026-10-06 B유형 감수 메모 반영 — 4급
import re as _r
_LONG = MEMO + "원문항보다 짧던 문장을 원문항 길이로 늘렸다. 밑줄 표현의 옳고 틀림과 보기, 정답은 그대로다."

# 4-20
RE(4, 20, "B", p="(A) The new scissors on the desk <u>are</u> very sharp.\n(B) This big house near the park is <u>their's</u>.\n(C) The news about the test <u>are</u> really bad.\n(D) We know <u>them</u> from our old school.", s=_LONG + pos(2))
RE(4, 20, "C", p="(A) Jane and Mike <u>are</u> my cousins from Busan.\n(B) Their house near the beach <u>are</u> very big.\n(C) Those bags on the chair are <u>their</u>.\n(D) This book about dinosaurs is <u>my</u>.", s=_LONG + pos(4))
RE(4, 20, "D", p="(A) These pants <u>is</u> new, but they are too long.\n(B) The news on TV <u>is</u> good today.\n(C) That red car over there is <u>hers</u>.\n(D) Those books on the shelf are <u>our</u>.", s=_LONG + pos(1))
RE(4, 20, "E", p="(A) Jane and I <u>am</u> good friends from kindergarten.\n(B) This bag with the blue ribbon is <u>mine</u>.\n(C) <u>Who's</u> shoes are these by the door?\n(D) The police <u>are</u> here to help the lost child.", s=_LONG + pos(2))
RE(4, 20, "F", p="(A) The children <u>is</u> in the playground after lunch.\n(B) Their room on the second floor <u>is</u> big.\n(C) This bike with the basket is <u>her's</u>.\n(D) Those books on the table are <u>my</u>.", s=_LONG + pos(3))

# 4-22 두 문장을 원문항처럼 길게, ‘- ’ 표시
_S22 = MEMO + "원문항보다 짧던 두 문장을 원문항 길이로 늘리고 원문항처럼 ‘- ’를 붙였다. 보기와 정답은 그대로다."
F(4, 22, "B", p="- I _____ very hungry after the long soccer practice.\n- Tom _____ at home with his little brother now.", s=_S22 + pos(5))
RE(4, 22, "C", p="- Mom and Dad _____ in the kitchen right now.\n- The weather _____ nice today for a picnic.", s=_S22 + pos(2))
F(4, 22, "D", p="- They _____ new students in our class.\n- The dog in the garden _____ very cute.", s=_S22 + pos(3))
F(4, 22, "E", p="- We _____ ready for the big test tomorrow.\n- Jane _____ busy with her homework now.", s=_S22 + pos(3))
F(4, 22, "F", p="- You _____ always kind to your classmates.\n- The boys on the playground _____ happy.", s=_S22 + pos(1))

# 4-25 ‘Does 대신 Does’처럼 읽히는 설명을 고침
RE(4, 25, "B", p="㉠ We don't watches TV.\n㉡ Does they like pizza?\n[설명]\n- 문장 ㉠에서 'don't' 뒤에는 반드시 (<u>    A    </u>) 형태가 와야 한다. 따라서 'watches'를 'watch'로 고쳐야 한다.\n- 문장 ㉡에서 주어 'they'는 복수이므로 의문문은 (<u>    B    </u>)로 시작해야 한다.",
   s=OLD(4, 25, "B")["s"] + " " + MEMO + "㉡의 설명 ‘Does 대신 (B)’는 (B)에 Does를 넣은 보기와 어긋나 어색해, ‘의문문은 (B)로 시작해야 한다’로 고쳤다.")
RE(4, 25, "F", p="㉠ Do she have a pet?\n㉡ They doesn't eat meat.\n[설명]\n- 문장 ㉠에서 주어 'she'는 3인칭 단수이므로 의문문은 (<u>    A    </u>)로 시작해야 한다.\n- 문장 ㉡에서 주어 'They'는 복수이므로 부정문에는 (<u>    B    </u>)를 써야 한다.",
   s=OLD(4, 25, "F")["s"] + " " + MEMO + "B와 같은 문제(‘Do 대신 (A)’, ‘doesn't 대신 (B)’)가 있어 설명을 고쳤다.")

# 4-28 제시 문장과 설명을 원문항처럼 길게
R28m = "일반동사 현재 의문문: Do/Does + 주어 + 동사원형 ~? Does가 이미 3인칭 단수를 나타내므로 뒤의 동사에는 -s를 붙이지 않는다."
def f28m(t, p, c, n, a, k):
    RE(4, 28, t, p=p, c=c, a=a, k=k, r=R28m, n=[x + OK(i + 1, a) for i, x in enumerate(n)], s=MEMO + "원문항보다 짧고 단조롭던 제시 문장을 늘리고 학생들의 설명도 그에 맞게 고쳤다. 틀린 설명의 내용과 정답은 그대로다." + pos(a))
f28m("B", "Do your friends play soccer in the park after school?", ["도윤: 주어 your friends가 복수라서 문장 앞에 Do를 썼어.", "지아: 운동 이름 soccer 앞에는 관사를 쓰지 않았어.", "현우: 대답은 Yes, they do.라고 할 수 있어.", "소민: Do 뒤의 동사는 plays로 써야 해.", "태오: 일반동사 play가 있어서 be동사 Are가 아니라 Do로 물었어."],
     ["복수 주어 your friends라 Do를 쓴 것이 맞으므로", "운동 이름 앞에는 관사를 쓰지 않는 것이 맞으므로", "Do로 물으면 Yes, they do.로 답할 수 있으므로", "Do 뒤에는 plays가 아니라 동사원형 play를 쓰므로", "일반동사가 있어 be동사가 아니라 Do로 묻는 것이 맞으므로"], 4, "Do 뒤에는 plays가 아니라 동사원형 play를 쓴다.")
f28m("C", "Does your sister walk to school with her friends every morning?", ["수아: 주어 your sister가 3인칭 단수라서 Does를 썼어.", "은우: 동생이 지금 걷고 있는지 묻는 진행형 문장이야.", "준호: Does가 있으니 walk에는 -s를 붙이지 않아.", "하린: 대답은 No, she doesn't.라고 할 수 있어.", "시윤: 주어가 your sister라서 대답할 때 she로 받아."],
     ["3인칭 단수 주어라 Does를 쓴 것이 맞으므로", "Does + 동사원형은 현재의 습관을 묻는 일반동사 의문문이고 진행형이 아니므로", "Does가 있으면 동사원형 walk를 쓰는 것이 맞으므로", "Does로 물으면 No, she doesn't.로 답할 수 있으므로", "your sister를 she로 받는 것이 맞으므로"], 2, "Does + 동사원형은 진행형이 아니라 현재의 습관을 묻는 의문문이다.")
f28m("D", "Does Tom study English at the library on weekends?", ["서진: 주어 Tom이 3인칭 단수라서 Does를 썼어.", "민재: 대답은 Yes, he does.라고 할 수 있어.", "가은: study는 동사원형이라 Does 뒤에 바르게 쓰였어.", "주원: 일반동사 의문문이라 be동사 Is를 쓰지 않았어.", "예은: Does 뒤에는 과거형 동사를 써야 해."],
     ["3인칭 단수 주어라 Does를 쓴 것이 맞으므로", "Does로 물으면 Yes, he does.로 답할 수 있으므로", "Does 뒤에 동사원형 study를 쓴 것이 맞으므로", "일반동사가 있어 be동사를 쓰지 않는 것이 맞으므로", "Does 뒤에는 과거형이 아니라 동사원형을 쓰므로"], 5, "Does 뒤에는 과거형이 아니라 동사원형을 쓴다.")
f28m("E", "Do you need help with your science project?", ["건우: Do 의문문에는 be동사 are를 함께 써서 Do are you need help ~?라고 해야 해.", "채원: 주어 you에는 Do를 써서 물어.", "지호: need는 일반동사라서 Do로 의문문을 만들어.", "유나: 대답은 Yes, I do.라고 할 수 있어.", "다인: Do 뒤에 동사원형 need를 바르게 썼어."],
     ["일반동사 의문문에는 be동사를 함께 쓰지 않으므로", "주어 you에 Do를 쓰는 것이 맞으므로", "일반동사라 Do로 의문문을 만드는 것이 맞으므로", "Do로 물으면 Yes, I do.로 답할 수 있으므로", "Do 뒤에 동사원형 need를 쓴 것이 맞으므로"], 1, "일반동사 의문문에는 be동사를 함께 쓰지 않는다.")
f28m("F", "Does Jane like milk with her breakfast every day?", ["하은: 주어 Jane이 3인칭 단수라서 Does를 썼어.", "도현: 우유를 좋아한다면 Yes, she does.처럼 does를 써서 대답해.", "소율: 3인칭 단수 질문에는 Do를 써야 해.", "우진: like는 동사원형이라 Does 뒤에 바르게 쓰였어.", "서아: milk는 셀 수 없는 명사라 a를 붙이지 않았어."],
     ["3인칭 단수 주어라 Does를 쓴 것이 맞으므로", "Does로 물으면 Yes, she does.로 답하는 것이 맞으므로", "3인칭 단수 주어에는 Do가 아니라 Does를 쓰므로", "Does 뒤에 동사원형 like를 쓴 것이 맞으므로", "milk는 셀 수 없는 명사라 a를 붙이지 않는 것이 맞으므로"], 3, "3인칭 단수 주어에는 Do가 아니라 Does를 쓴다.")

# 4-30 C의 긴 빈칸을 원문항과 같은 길이로
_o30 = OLD(4, 30, "C"); RE(4, 30, "C", p=_o30["p"].replace("________", "____"), s=_o30["s"] + " " + MEMO + "줄바꿈이 어색하던 긴 빈칸을 원문항과 같은 길이(____)로 줄였다.")

# 4-41 위치 문항: 보기를 번호만으로
for _t in "BCDEF":
    _o = OLD(4, 41, _t)
    RE(4, 41, _t, c=numc(), s=_o["s"] + " " + MEMO + "뒤에 오는 낱말까지 적혀 있던 보기를 번호만으로 바꿨다.")

# 4-45 문장을 원문항 길이로, ‘Tom will be home’ → ‘at home’
RE(4, 45, "B", p="\n".join(["ⓐ Tom will be at home this evening.", "ⓑ Are they going to visit their grandmother?", "ⓒ I am not going to go to the party tonight.", "ⓓ She won't studies math tonight.", "ⓔ We will eat dinner later."]),
   s=MEMO + "원문항보다 짧던 문장을 늘리고, 뜻이 흐릿하던 ⓐ Tom will be home을 Tom will be at home ~으로 고쳤다. 옳고 틀림과 정답은 그대로다." + pos(4))
RE(4, 45, "C", p="\n".join(["ⓐ It will be sunny in Busan tomorrow.", "ⓑ She not will come to the meeting.", "ⓒ Tom going to call you after lunch.", "ⓓ They wills arrive at the station soon.", "ⓔ Are you going to visiting him this weekend?"]), s=_LONG + pos(1))
RE(4, 45, "D", p="\n".join(["ⓐ She will study for the exam tonight.", "ⓑ Tom going to play soccer with us.", "ⓒ We are going to leave at seven.", "ⓓ I won't be late for class again.", "ⓔ Does she going to come to the party?"]), s=_LONG + pos(3))
RE(4, 45, "E", p="\n".join(["ⓐ They will come to my house tomorrow.", "ⓑ She is going to study at the library.", "ⓒ Tom won't goes home before six.", "ⓓ Are you going to play tennis after school?", "ⓔ We will not be late for the movie."]), s=_LONG + pos(4))
RE(4, 45, "F", p="\n".join(["ⓐ I am going to buy a new bag this weekend.", "ⓑ Will he come to the concert with us?", "ⓒ She wills study hard for the test.", "ⓓ We not are going to leave early today.", "ⓔ They will help us with the boxes."]), s=_LONG + pos(3))

# 4-51 보기의 조동사 부분에도 밑줄
def ul51(c): return [_r.sub(r"\b(is able to|are able to|am able to|has to|have to|may|must|might)\b", r"<u>\1</u>", x, count=1) for x in c]
for _t in "BCDEF":
    _o = OLD(4, 51, _t)
    RE(4, 51, _t, c=ul51(_o["c"]), s=_o["s"] + " " + MEMO + "제시문의 can처럼 보기의 해당 부분에도 밑줄을 그어 밑줄을 통일했다.")

# 4-53 서로 충돌하던 ①·②를 고쳐 보기를 새로
F(4, 53, "B", c=["‘can’은 능력의 의미일 때 ‘have to’와 바꿔 쓸 수 있다.", "‘might’는 ‘may’보다 가능성이 낮은 추측을 나타낼 수 있다.", "‘must not’은 ‘~해서는 안 된다’는 금지를 나타낸다.", "조동사 ‘can’ 뒤에는 동사원형이 온다.", "‘don't have to’는 ‘~할 필요가 없다’는 뜻이다."], a=1,
  r="능력의 can은 be able to로 바꿔 쓴다. must not은 금지, don't have to는 불필요다. might는 may보다 약한 추측이고, 조동사 뒤에는 동사원형이 온다.", k="능력의 can은 have to가 아니라 be able to로 바꿔 쓴다.",
  n=["능력의 can은 have to가 아니라 be able to로 바꿔 쓰므로 옳지 않은 설명이다. 따라서 정답이다.", "might가 may보다 약한 추측을 나타낼 수 있는 것이 맞으므로 오답이다.", "must not이 금지를 나타내는 것이 맞으므로 오답이다.", "조동사 뒤에 동사원형이 오는 것이 맞으므로 오답이다.", "don't have to가 불필요를 나타내는 것이 맞으므로 오답이다."],
  s=MEMO + "①(might는 확실한 미래만)과 ②(might는 낮은 추측)가 서로 반대라 둘 중 하나가 답임이 드러났다. ①을 다른 내용의 틀린 설명으로 바꾸고 보기를 원문항처럼 ‘’ 표시로 다듬었다." + pos(1))

# 4-55 문장을 원문항 길이로
RE(4, 55, "B", p="\n".join(["ⓐ They <u>can goes</u> to the park after lunch.", "ⓑ Jane <u>might be</u> at home this afternoon.", "ⓒ Tom <u>must go</u> to bed before ten.", "ⓓ We <u>can work</u> together on the project.", "ⓔ He <u>can reads</u> English books very well."]), s=_LONG + pos(3))
RE(4, 55, "D", p="\n".join(["ⓐ She <u>can sing</u> very well on stage.", "ⓑ Tom <u>might come</u> to the party tonight.", "ⓒ We <u>must study</u> hard for the test.", "ⓓ They <u>can play</u> the piano and the violin.", "ⓔ I <u>can helps</u> you with your homework."]), s=_LONG + pos(4))
RE(4, 55, "E", p="\n".join(["ⓐ I <u>can swim</u> across the river.", "ⓑ She <u>must is</u> quiet in the library.", "ⓒ They <u>might not come</u> back tonight.", "ⓓ Tom <u>can sing</u> many Korean songs.", "ⓔ We <u>must leave</u> for school before eight."]), s=_LONG + pos(4))
RE(4, 55, "F", p="\n".join(["ⓐ Tom <u>can read</u> difficult English books.", "ⓑ Jane <u>might be</u> late for the meeting.", "ⓒ They <u>must wears</u> helmets on their bikes.", "ⓓ We <u>can to help</u> you with the boxes.", "ⓔ I <u>can be</u> ready in ten minutes."]), s=_LONG + pos(3))

# 4-61 가끔/자주처럼 헷갈리는 오답을 분명한 오답으로
R61m = "빈도부사의 뜻: always(항상) > usually(보통) > often(자주) > sometimes(가끔) > seldom·rarely(거의 ~않다) > never(전혀 ~않다)."
RE(4, 61, "B", c=["그들은 거의 축구를 하지 않는다.", "그들은 항상 축구를 한다.", "그들은 축구를 잘 한다.", "그들은 전혀 축구를 하지 않는다.", "그들은 자주 축구를 한다."], a=5, r=R61m,
   n=["‘거의 ~않는다’는 seldom·rarely이므로 오답이다.", "‘항상’은 always이므로 오답이다.", "‘잘’은 빈도가 아니라 정도를 나타내는 well이므로 오답이다.", "‘전혀 ~않는다’는 never이므로 오답이다.", "often은 ‘자주’라는 뜻이므로 정답이다."],
   s=OLD(4, 61, "B")["s"] + " " + MEMO + "정답 ‘자주’와 헷갈릴 수 있던 ③ ‘가끔’을 분명한 오답(‘잘 한다’)으로 바꿨다. 정답 위치 ⑤.")
RE(4, 61, "F", c=["우리는 거의 외식하지 않는다.", "우리는 항상 외식한다.", "우리는 지금 외식하고 있다.", "우리는 전혀 외식하지 않는다.", "우리는 가끔 외식한다."], a=5, r=R61m,
   n=["‘거의 ~않는다’는 seldom·rarely이므로 오답이다.", "‘항상’은 always이므로 오답이다.", "‘지금 ~하고 있다’는 현재진행형의 뜻이고 sometimes의 뜻이 아니므로 오답이다.", "‘전혀 ~않는다’는 never이므로 오답이다.", "sometimes는 ‘가끔’이라는 뜻이므로 정답이다."],
   s=OLD(4, 61, "F")["s"] + " " + MEMO + "정답 ‘가끔’과 헷갈릴 수 있던 ③ ‘자주’를 분명한 오답(‘지금 외식하고 있다’)으로 바꿨다. 정답 위치 ⑤.")

# 4-65
RE(4, 65, "B", p="\n".join(["ⓐ I have <u>few books</u> about Korean history.", "ⓑ Jane has <u>many money</u> in her piggy bank.", "ⓒ He <u>always is</u> late for the first class.", "ⓓ We <u>often go</u> hiking on sunny weekends."]), s=_LONG + pos(2))
RE(4, 65, "C", p="\n".join(["ⓐ She drinks <u>much milks</u> every morning.", "ⓑ Minsu <u>usually walks</u> to school with his sister.", "ⓒ We have <u>a few eggs</u> in the fridge.", "ⓓ They <u>never is</u> late for school."]), s=_LONG + pos(3))
RE(4, 65, "D", p="\n".join(["ⓐ I <u>sometimes plays</u> tennis with my dad.", "ⓑ We need <u>many money</u> for the trip.", "ⓒ There are <u>a few chairs</u> in the hall.", "ⓓ She <u>is often</u> busy after school."]), s=_LONG + pos(5))
RE(4, 65, "E", p="\n".join(["ⓐ Tom <u>rarely eats</u> fast food for lunch.", "ⓑ We have <u>a little homework</u> this weekend.", "ⓒ Jane has <u>much pencils</u> in her bag.", "ⓓ He <u>goes always</u> to bed early."]), s=_LONG + pos(1))
RE(4, 65, "F", p="\n".join(["ⓐ We drink <u>many water</u> after the game.", "ⓑ She has <u>little money</u> in her pocket.", "ⓒ He <u>seldom watch</u> TV on weekdays.", "ⓓ They <u>are always</u> kind to new students."]), s=_LONG + pos(4))

# 4-70
RE(4, 70, "B", p="\n".join(["(a) I have <u>few</u> pencils in my pencil case.", "(b) She drinks <u>much</u> milk every morning.", "(c) We have <u>many</u> homework to do tonight.", "(d) Tom has <u>a little</u> money in his wallet.", "(e) They have <u>a little</u> friends in their new school."]), s=_LONG + pos(2))
RE(4, 70, "C", p="\n".join(["(a) She bought <u>a few</u> oranges at the market.", "(b) He ate <u>a few</u> bread for breakfast.", "(c) We have <u>a little</u> time before the bus comes.", "(d) He has <u>much</u> friends in his class.", "(e) There are <u>many</u> books on the shelf."]), s=_LONG + pos(4))
RE(4, 70, "D", p="\n".join(["(a) There are <u>a few</u> cars in the parking lot.", "(b) We need <u>much</u> water for the plants.", "(c) Jane has <u>a little</u> books about animals.", "(d) I have <u>few</u> money in my pocket.", "(e) Tom eats <u>a little</u> rice for dinner."]), s=_LONG + pos(1))
RE(4, 70, "E", p="\n".join(["(a) She has <u>much</u> apples in her basket.", "(b) We have <u>little</u> time for lunch today.", "(c) I need <u>a few</u> water for the soup.", "(d) They have <u>much</u> money for the trip.", "(e) Tom has <u>few</u> books in his bag."]), s=_LONG + pos(5))
RE(4, 70, "F", p="\n".join(["(a) I have <u>a little</u> questions about the test.", "(b) Jane has <u>little</u> money for the trip.", "(c) We drink <u>much</u> milk every day.", "(d) They have <u>many</u> books in their room.", "(e) Tom has <u>a few</u> rice in his bowl."]), s=_LONG + pos(3))

# 4-75
RE(4, 75, "B", p="\n".join(["ⓐ Tom is <u>taller than</u> his older brother Ben.", "ⓑ This is <u>the most cheapest</u> shirt in the store.", "ⓒ Jane is <u>more beautiful than</u> her sister Amy.", "ⓓ Today is <u>hotter than</u> yesterday in Daegu.", "ⓔ He is <u>the best</u> player on our soccer team."]), s=_LONG + pos(4))
RE(4, 75, "D", p="\n".join(["ⓐ This test is <u>easier than</u> the last one.", "ⓑ Tom is <u>more taller than</u> his cousin Ben.", "ⓒ Jane is <u>the most prettiest</u> girl in her class.", "ⓓ This book is <u>the most interesting</u> of all.", "ⓔ He is <u>worser than</u> me at math."]), s=_LONG + pos(2))
RE(4, 75, "E", p="\n".join(["ⓐ The dog is <u>bigger than</u> the cat next door.", "ⓑ This is <u>the easiest</u> question on the test.", "ⓒ Tom is <u>better than</u> Ben at singing.", "ⓓ Jane is <u>more happier than</u> Amy today.", "ⓔ It is <u>the worst</u> day of my life."]), s=_LONG + pos(4))
RE(4, 75, "F", p="\n".join(["ⓐ Seoul is <u>larger than</u> Busan in size.", "ⓑ This bag is <u>more heavier than</u> that one.", "ⓒ Jane is <u>the most kindest</u> girl in our class.", "ⓓ Tom is <u>the most fast</u> runner on the team.", "ⓔ This movie is <u>more better than</u> that one."]), s=_LONG + pos(1))

# 4-80
RE(4, 80, "B", p="<보기>\n" + "\n".join(["(가) This is the most expensive bag in the shop.", "(나) Tom is more taller than his brother Ben.", "(다) Jane is happier than Amy about the trip.", "(라) It is the worst movie of the year.", "(마) The cat is the most smallest animal in the house."]), s=_LONG + pos(2))
RE(4, 80, "C", p="<보기>\n" + "\n".join(["(가) Mina is the youngest in her family.", "(나) This is the most smallest room in the hotel.", "(다) Jane is taller than Amy by five centimeters.", "(라) Tom is more better at math than I am.", "(마) This is the most interesting book in the library."]), s=_LONG + pos(4))
RE(4, 80, "D", p="<보기>\n" + "\n".join(["(가) Tom is taller than Ben in our class.", "(나) This is the easiest test of the year.", "(다) Jane is more prettier than her sister.", "(라) He is the best player on the team.", "(마) Today is more hotter than yesterday."]), s=_LONG + pos(1))
RE(4, 80, "E", p="<보기>\n" + "\n".join(["(가) This bag is more heavier than that one.", "(나) Jane is the most beautiful girl in the picture.", "(다) Tom is gooder than Ben at soccer.", "(라) This is the worst day of the week.", "(마) The dog is bigger than the cat in the yard."]), s=_LONG + pos(3))
RE(4, 80, "F", p="<보기>\n" + "\n".join(["(가) Seoul is larger than Busan in population.", "(나) Tom is the fastest runner in our school.", "(다) Jane is the most kindest student in class.", "(라) This test is more easier than the last one.", "(마) He is better than me at drawing."]), s=_LONG + pos(5))

# 4-89 when의 위치만으로 답이 드러나지 않게
def f89m(t, i, text, s):
    o = OLD(4, 89, t); c = list(o["c"]); c[i - 1] = text
    RE(4, 89, t, c=c, s=o["s"] + " " + MEMO + s)
f89m("B", 2, "<u>When</u> she saw me, she smiled.", "문장 맨 앞의 When이 정답 하나뿐이라 위치만으로 답이 드러났다. ②를 When으로 시작하는 접속사 문장으로 바꿨다.")
f89m("C", 3, "<u>When</u> my dog was sick, I felt sad.", "정답만 when이 문장 가운데에 있어 위치만으로 답이 드러났다. ③을 When으로 시작하는 접속사 문장으로 바꿔 다섯 문장이 모두 When으로 시작하게 했다.")
f89m("E", 5, "<u>When</u> you get home, wash your hands.", "정답만 when이 문장 가운데에 있어 위치만으로 답이 드러났다. ⑤를 When으로 시작하는 접속사 문장으로 바꿔 다섯 문장이 모두 When으로 시작하게 했다.")

# 4-92 빈칸 뒤 a/an만으로 답이 나오지 않게
R92m = "감탄문: 명사가 있으면 What + (a/an) + 형용사 + 명사 ~!, 형용사·부사만 있으면 How + 형용사/부사 + 주어 + 동사!"
F(4, 92, "B", c=["_____ cute puppies they are!", "_____ a great idea it is!", "_____ interesting the book is!", "_____ nice weather it is!", "_____ an old house it is!"], a=3, r=R92m,
  n=["cute puppies처럼 형용사 + 복수명사가 있어 What이 들어가므로 오답이다.", "a great idea처럼 명사가 있어 What이 들어가므로 오답이다.", "형용사 interesting 뒤에 명사 없이 the book is가 이어져 How가 들어가 나머지와 다르므로 정답이다.", "nice weather처럼 형용사 + 명사가 있어 What이 들어가므로 오답이다.", "an old house처럼 명사가 있어 What이 들어가므로 오답이다."],
  s=MEMO + "빈칸 뒤의 a/an만 보고 답을 찾을 수 있어, ①·④를 a/an 없이 ‘형용사 + 명사’가 오는 What 감탄문으로 바꿨다." + pos(3))
def f92m(t, i, text, note, s):
    o = OLD(4, 92, t); c = list(o["c"]); n = list(o["n"]); c[i - 1] = text; n[i - 1] = note
    RE(4, 92, t, c=c, n=n, s=o["s"] + " " + MEMO + s)
f92m("C", 4, "_____ lovely music this is!", "lovely music처럼 형용사 + 명사가 있어 What이 들어가므로 오답이다.", "a/an 없이 명사가 오는 What 감탄문을 하나 더 넣었다.")
f92m("D", 3, "_____ long bridges these are!", "long bridges처럼 형용사 + 복수명사가 있어 What이 들어가 나머지와 다르므로 정답이다.", "정답에만 a가 있어 답이 드러나던 것을, a 없이 복수명사가 오는 What 감탄문으로 바꿨다.")
f92m("E", 5, "_____ strange dreams I had!", "strange dreams처럼 형용사 + 복수명사가 있어 What이 들어가므로 오답이다.", "a/an 없이 명사가 오는 What 감탄문을 하나 더 넣었다.")

# 4-109 문장을 원문항 길이로
RE(4, 109, "B", p="<보기>\n" + "\n".join(["(가) Tom laughed loudly at the funny joke.", "(나) The soup on the table tastes really good.", "(다) We went home after the soccer game.", "(라) Jane reads comic books in her room."]), s=_LONG + pos(4))
RE(4, 109, "C", p="<보기>\n" + "\n".join(["(가) There is a bank near my house.", "(나) Jane is happy with her new bike.", "(다) Tom likes pop music very much.", "(라) Birds fly high in the blue sky."]), s=_LONG + pos(3))
RE(4, 109, "D", p="<보기>\n" + "\n".join(["(가) Jane became angry at her brother.", "(나) The baby sleeps in the small bed.", "(다) I bought a book at the store.", "(라) The train arrived at the station on time."]), s=_LONG + pos(5))
RE(4, 109, "E", p="<보기>\n" + "\n".join(["(가) Tom is tall for his age.", "(나) The dog ran fast across the field.", "(다) There is a cat outside the window.", "(라) We need help with the heavy boxes."]), s=_LONG + pos(2))
RE(4, 109, "F", p="<보기>\n" + "\n".join(["(가) Jane looks tired after the long trip.", "(나) Tom bought a bag at the mall.", "(다) The train stopped at the small station.", "(라) The baby cried all night long."]), s=_LONG + pos(3))
