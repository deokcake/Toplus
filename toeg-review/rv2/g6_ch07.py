# 6급 CH7 조동사 can, may, must (61~70) 2차 감수
X(6, 61, r="must는 ‘~해야 한다’(의무), can은 ‘~할 수 있다’(능력), may는 ‘~해도 된다’(허락)·‘~일지도 모른다’(추측), will은 ‘~할 것이다’(미래)를 나타낸다.",
  n=["can은 ‘~할 수 있다’이므로", "may는 ‘~해도 된다’이므로", "must가 ‘~해야 한다’는 의무를 나타내므로", "are able to는 ‘~할 수 있다’이므로", "will은 ‘~할 것이다’이므로"],
  st="① 우리말의 끝을 본다: ‘{0}’. 의무를 나타낸다. → ② 의무의 조동사는 must다. 능력(can, be able to), 허락(may), 그 밖의 말을 지운다. → ③ 정답은 {n}.",
  R="청소해야 한다", B="따라야 한다", C="써야 한다", D="끝내야 한다", E="지켜야 한다", F="해야 한다")
RV(6, 61, "F", fx=True, why="변형은 우리말 해석이 영어 문장과 같은 줄에 있다(원문항은 다음 줄). 수정 예시에서 원문항처럼 줄을 나눴다.")

X(6, 62, r="‘~해도 된다’는 허락은 may(can) + 동사원형으로 나타낸다. must, have to는 의무, be able to는 능력이다.",
  n=["may + 동사원형으로 허락을 나타냈으므로", "must는 ‘마셔야 한다’는 의무이므로", "have to는 ‘마셔야 한다’는 의무이므로", "are able to는 ‘마실 수 있다’는 능력이므로", "can과 be able to를 겹쳐 쓸 수 없으므로"],
  st="① 우리말 ‘{0}’ → 허락이므로 may + 동사원형이 필요하다. → ② 의무(must, have to)의 문장과 may 뒤의 동사 형태가 틀린 문장을 지운다. → ③ may {1}인 문장은 {n}.",
  R=("마셔도 된다", "drink"), B=("사용해도 된다", "use"), C=("읽어도 된다", "read"), D=("타도 된다", "ride"), E=("들어가도 된다", "enter"), F=("열어도 된다", "open"))
RV(6, 62, "CF", fx=True, why="정답 위치가 원문항·B·C·F 모두 ①이었다. 수정 예시에서 C와 F의 보기 순서를 바꿨다(C ③, F ④).")

X(6, 63, r="must(~해야 한다)는 have to로 바꿔 쓸 수 있다. 주어가 3인칭 단수면 has to를 쓴다.",
  n=["can은 능력·허락이라 뜻이 다르므로", "3인칭 단수 주어 He에 맞는 has to이므로", "주어 He에는 have to가 아니라 has to를 써야 하므로", "is는 뒤의 동사원형 clean과 함께 쓸 수 없으므로", "may는 허락·추측이라 뜻이 다르므로"],
  st="① must는 의무다. 같은 뜻의 표현은 have to/has to다. → ② 주어를 본다: {0}. → ③ 정답은 {a}.",
  R="He는 3인칭 단수이므로 has to", B="They는 복수이므로 have to", C="She는 3인칭 단수이므로 has to", D="She는 3인칭 단수이므로 has to", E="I이므로 have to", F="Tom은 3인칭 단수이므로 has to")

X(6, 64, r="조동사(can, may, must, should)는 주어가 3인칭 단수여도 -s를 붙이지 않고, 뒤에는 동사원형을 쓴다.",
  n=["may를 바르게 썼으므로", "조동사 may에는 -s를 붙이지 않으므로", "can을 바르게 썼으므로", "must를 바르게 썼으므로", "should를 바르게 썼으므로"],
  st="① 문장마다 조동사와 그 뒤의 동사를 본다. → ② 조동사에 -s가 붙지 않았는지, 뒤의 동사가 원형인지 본다. → ③ {0} 정답은 {n}.",
  R="②의 mays는 없는 형태다. 주어가 My mom이어도 may다.", B="②는 may 뒤에 are를 썼다. be동사의 원형은 be다.", C="①은 must 뒤에 finishes를 썼다. 원형은 finish다.", D="③은 can 뒤에 plays를 썼다. 원형은 play다.",
  E="④는 should 뒤에 joining을 썼다. 원형은 join이다.", F="⑤는 may 뒤에 arrives를 썼다. 원형은 arrive다.")
RV(6, 64, "BCDE", fx=True, why="원문항은 밑줄이 한 단어(조동사)인데 변형과 수정 예시는 ‘조동사 + 동사’ 두 단어에 밑줄을 쳤고, C의 수정 예시는 정답만 한 단어(cans)여서 밑줄 길이로 답이 드러났다. 수정 예시의 밑줄을 모두 한 단어(조동사 뒤의 동사)로 맞췄다.")
RV(6, 64, "F", v="수정(표기)", why="정답 ⑤ 유일 확인. 여러 조동사를 섞어 원문항 설계와 같다. 다만 원문항은 밑줄이 한 단어인데 변형은 ‘조동사 + 동사’ 두 단어에 밑줄을 쳤다.", fix="밑줄을 한 단어로")

X(6, 65, r="can(~할 수 있다) = be able to. be동사는 주어에 맞춰 am/is/are를 쓴다.",
  n=["3인칭 단수 주어 She에 맞는 be동사이므로", "주어 She에는 are를 쓸 수 없으므로", "can able to라고 쓰지 않으므로", "be는 원형이라 주어 뒤에 그대로 쓸 수 없으므로", "does able to라고 쓰지 않으므로"],
  st="① can = be able to이므로 빈칸에는 be동사가 들어간다. → ② 주어를 본다: {0}. → ③ 정답은 {a}.",
  R="She는 3인칭 단수 → is", B="Tom은 3인칭 단수 → is", C="I → am", D="We → are", E="They → are", F="You and Tom은 두 사람 → are")

X(6, 66, r="조동사 may 뒤에는 동사원형을 쓴다.",
  n=["may 뒤에 -s형을 쓸 수 없으므로", "may 뒤에 동사원형 rain을 썼으므로", "may 뒤에 -ing형을 쓸 수 없으므로", "may 뒤에 to부정사를 쓸 수 없으므로", "may 뒤에 과거형을 쓸 수 없으므로"],
  st="① 빈칸 앞의 may를 본다. 주어가 {0}이어도 may 뒤는 동사원형이다. → ② -s형, -ing형, to부정사, 과거형, be를 덧붙인 것을 지운다. → ③ 정답은 {a}.",
  R="It(3인칭 단수)", B="My uncle(3인칭 단수)", C="Tom(3인칭 단수)", D="The package(3인칭 단수)", E="She(3인칭 단수)", F="They(복수)")

X(6, 67, r="must 뒤에는 동사원형을 쓴다. be동사의 원형은 be다. must be ~는 ‘~임이 틀림없다’는 강한 추측이다.",
  n=["must 뒤에 is를 쓸 수 없으므로", "must 뒤에 are를 쓸 수 없으므로", "must 뒤에 be동사의 원형 be를 썼으므로", "must 뒤에 am을 쓸 수 없으므로", "must 뒤에 -ing형을 쓸 수 없으므로"],
  st="① B의 말에서 추측의 근거를 찾는다: {0}. → ② 그래서 ‘~임이 틀림없다’는 must be가 된다. must 뒤는 주어와 관계없이 원형 be다. → ③ 정답은 {n}.",
  R="He knows a lot!", B="Her bag is here.", C="They know everyone.", D="He is carrying a guitar", E="불이 켜져 있다(Yes.)", F="His shoes are here.")
RV(6, 67, "D", v="수정(내용)", why="정답 ④ 유일 확인. 다만 빈칸이 든 문장(she must ___ a teacher)이 원문항(he must ___ a teacher)과 주어만 다르다.", fix="대화를 새로")

X(6, 68, r="be able to + 동사원형 = can + 동사원형. can 뒤에는 주어와 관계없이 동사원형을 쓰고, be동사와 함께 쓰지 않는다.",
  n=["can + 동사원형 draw로 알맞으므로", "can 뒤에 draws를 쓸 수 없으므로", "is와 can을 함께 쓸 수 없으므로", "be동사 없이 able to만 쓸 수 없으므로", "can 뒤에 -ing형을 쓸 수 없으므로"],
  st="① {0} able to를 can으로 바꾼다. be동사는 사라진다. → ② can 뒤에는 동사원형이 온다: can {1}. → ③ 정답은 {n}.",
  R=("is", "draw"), B=("are", "swim"), C=("is", "ride"), D=("is", "read"), E=("am", "run"), F=("are", "help"))

X(6, 69, r="have to의 의문문은 Do/Does + 주어 + have to + 동사원형 ~?이다. 3인칭 단수 주어에는 Does를 쓰고, 그 뒤는 has가 아니라 have to다.",
  n=["3인칭 단수 주어 he에는 Do를 쓸 수 없으므로", "Does 뒤에는 has to가 아니라 have to를 써야 하므로", "have to의 의문문은 Is가 아니라 Do/Does로 만들므로", "he에 Do를 쓸 수 없고 뒤에도 have to가 와야 하므로", "he에 Does, 그 뒤에 have to가 알맞으므로"],
  st="① 대답을 본다: {0}. 질문도 같은 조동사로 시작한다. → ② {1} → ③ 정답은 {n}.",
  R=("Yes, he does", "(A) Does, 그 뒤 (B)는 원형 have to다."), B=("Yes, I do", "(A) Do, (B) have to다."), C=("Yes, she ( ) to", "(A) 주어 Jane은 3인칭 단수라 Does, (B) 대답은 긍정문이라 has to다."),
  D=("Yes, they do", "(A) Do, (B) have to다."), E=("Yes, they do", "(A) Do, (B) have to다."), F=("대답 없이 평서문과 의문문이 이어진다", "(A) 평서문의 주어 Mina는 3인칭 단수라 has to, (B) 의문문은 Does she have to ~?다."))

X(6, 70, r="have to(~해야 한다)는 must와 비슷한 뜻이다. 주어가 3인칭 단수면 has to를 쓴다. 뒤에는 동사원형이 온다.",
  n=["have to가 must와 비슷한 뜻이라는 옳은 설명이므로", "주어 You에 have to를 쓴다는 옳은 설명이므로", "have to 뒤에 동사원형을 쓴다는 옳은 설명이므로", "목적어를 바르게 설명했으므로", "주어가 He이면 has to로 써야 하는데 have to라고 했으므로"],
  st="① <보기>를 주어 / have to / 동사원형 / 나머지로 나눈다: {0}. → ② 설명마다 이 문장에 대어 보고, 문장을 바꾸는 설명은 실제로 바꿔 써 본다. → ③ {1} 정답은 {n}.",
  R=("You / have to / wash / your hands", "⑤ 주어가 He이면 He has to wash his hands.다."), B=("He / doesn't have to / go", "② doesn't 뒤에는 has가 아니라 have to를 쓴다."), C=("We / have to / study / now", "③ 부정문은 We don't have to study now.다."),
  D=("She / has to / go / home", "④ 주어가 I이면 I have to go home.이다."), E=("Does / he / have to / work", "① 주어가 they이면 Do they have to work?다."), F=("Mina / has to / finish / her homework", "⑤ 의문문은 Does Mina have to finish ~?다."))
