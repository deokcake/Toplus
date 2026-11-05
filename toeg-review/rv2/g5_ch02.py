# 5급 CH2 be동사와 일반동사 (11~20) 2차 감수
X(5, 11, r="주어가 3인칭 단수이면 일반동사 현재형에 -(e)s를 붙인다. be동사와 일반동사를 함께 쓰지 않는다.",
  n=["3인칭 단수 주어 She에 walks가 알맞으므로", "be동사와 동사원형을 함께 쓸 수 없으므로", "be동사와 일반동사를 함께 쓸 수 없으므로", "3인칭 단수 주어에는 -s를 붙여야 하므로", "walking만으로는 동사 자리를 채울 수 없으므로"],
  st="① 주어를 본다: {0}. 3인칭 단수다. → ② 일반동사 현재형에 -(e)s를 붙인다: {1}. → ③ 정답은 {a}.",
  R=("She", "walk → walks"), B=("The baby", "cry는 ‘자음 + y’로 끝나므로 y를 i로 바꾸고 -es를 붙여 cries"), C=("Tom", "study는 ‘자음 + y’로 끝나므로 studies"), D=("The boy", "watch는 -ch로 끝나므로 -es를 붙여 watches"),
  E=("Jane", "carry는 ‘자음 + y’로 끝나므로 carries"), F=("The dog", "run → runs"))

X(5, 12, r="be동사: I am, you/we/they are, he/she/it is. 의문문은 be동사를 주어 앞에 둔다.",
  n=["We에는 is가 아니라 are를 쓰므로", "We에 is, she에 Are 모두 맞지 않으므로", "We에는 are, she에는 Is가 알맞으므로", "she에는 Are가 아니라 Is를 쓰므로", "am은 주어가 I일 때만 쓰므로"],
  st="① 첫 문장의 주어를 본다: {0}. → ② 둘째 문장은 의문문이라 be동사가 주어 앞에 왔다. 주어를 본다: {1}. → ③ 정답은 {a}.",
  R=("We에는 are", "she에는 Is"), B=("I에는 am", "they에는 Are"), C=("I에는 am", "they에는 Are"), D=("Tom에는 is", "you에는 Are"), E=("They에는 are", "he에는 Is"), F=("Jane에는 is", "I에는 Am"))

X(5, 13, r="현재 시제에서 3인칭 단수 주어에는 동사 + -(e)s를 쓴다(have는 has). 복수 주어와 I, you에는 동사원형을 쓴다.",
  n=["복수 주어 They에 like가 맞으므로", "3인칭 단수 주어 She에 makes가 맞으므로", "3인칭 단수 주어 Jenny에 tries가 맞으므로", "3인칭 단수 주어 Peter에는 have가 아니라 has를 써야 하므로", "주어 We에 are가 맞으므로"],
  st="① 문장마다 주어가 3인칭 단수인지 본다. → ② 3인칭 단수면 동사에 -(e)s(have는 has), 아니면 동사원형이다. → ③ {0} 정답은 {n}.",
  R="④의 Peter는 3인칭 단수이므로 has를 써야 한다.", B="③의 My cousins는 복수이므로 live를 써야 한다.", C="②의 Jane은 3인칭 단수이므로 goes를 써야 한다.", D="④의 Tom은 3인칭 단수이므로 studies를 써야 한다.",
  E="②의 My dad는 3인칭 단수이므로 watches를 써야 한다.", F="③의 The dog은 3인칭 단수이므로 runs를 써야 한다.")

X(5, 14, r="be동사 부정은 am/are/is + not, 일반동사 부정은 don't/doesn't + 동사원형이다. 3인칭 단수 주어에는 doesn't를 쓴다.",
  n=["They + aren't로 옳으므로", "I + don't + 동사원형으로 옳으므로", "doesn't 뒤에는 washes가 아니라 동사원형 wash를 쓰므로", "Betty + isn't로 옳으므로", "Sam + doesn't + 동사원형으로 옳으므로"],
  st="① be동사 부정문은 주어와 be동사가 맞는지 본다. → ② 일반동사 부정문은 don't/doesn't가 주어와 맞는지, 뒤가 동사원형인지 본다. → ③ {0} 정답은 {n}.",
  R="③은 doesn't 뒤에 washes를 썼다. wash로 고친다.", B="③은 doesn't 뒤에 studies를 썼다. study로 고친다.", C="④는 doesn't 뒤에 likes를 썼다. like로 고친다.", D="④는 주어 Tom에 don't를 썼다. doesn't로 고친다.",
  E="⑤는 주어 They에 doesn't를 썼다. don't로 고친다.", F="⑤는 doesn't 뒤에 goes를 썼다. go로 고친다.")
RV(5, 14, "B", fx=True, why="수정 예시의 틀린 문장이 원문항과 같은 종류의 오류(doesn't + -s형)이고 위치도 ③으로 같아, 보기 순서를 바꿔 ⑤로 옮겼다.")

X(5, 15, r="be동사로 물으면 be동사로, Do/Does로 물으면 do/does로 답한다. 대답의 주어는 대명사로 받는다.",
  n=["Is it ~?에 Yes, it is로 바르게 답했으므로", "Do로 물으면 Yes, I do로 답해야 하므로", "Are로 물으면 No, they aren't로 답해야 하므로", "she에는 do가 아니라 does를 쓰므로", "Are you ~?에는 Yes, I am으로 답해야 하므로"],
  st="① 질문의 첫 낱말을 본다. be동사로 물으면 be동사로, Do/Does로 물으면 do/does로 답한다. → ② 대답의 주어와 동사가 서로 맞는지 본다. → ③ {0} 정답은 {n}.",
  R="①만 Is ~? - it is로 맞는다.", B="④만 Are the cookies ~? - they are로 맞는다. 나머지는 질문의 be동사가 주어와 맞지 않는다.", C="③만 Are they ~? - they aren't로 맞는다.", D="④만 Is Jane ~? - she is로 맞는다.",
  E="②만 Are you ~? - I am not으로 맞는다.", F="②만 Am I ~? - you aren't로 맞는다.")
RV(5, 15, "E", fx=True, why="수정 예시의 오답 ‘Does Tom walk to school? - Yes, he walks.’는 틀린 대답이라고 하기 어려워, 분명히 틀린 대답(Yes, he is.)으로 바꿨다.")

X(5, 16, r="Do/Does 의문문에는 Yes, 주어 + do/does. / No, 주어 + don't/doesn't.로 답한다.",
  n=["Does로 물으면 be동사로 답하지 않으므로", "she에는 do가 아니라 does를 쓰므로", "Does로 묻고 주어가 she이므로 does로 답하므로", "짧은 대답에는 일반동사가 아니라 does를 쓰므로", "Does로 물으면 can으로 답하지 않으므로"],
  st="① 질문의 첫 낱말({0})을 그대로 받아 답한다. → ② 주어를 대명사로 바꾼다: {1}. → ③ 정답은 {a}.",
  R=("Does", "your sister → she"), B=("Does", "your dog → it"), C=("Does", "Tom → he"), D=("Do", "your parents → they"), E=("Do", "you → I"), F=("Does", "the dog → it"))
RV(5, 16, "B", v="수정(내용)", why="정답 확인. 다만 오답 세 개(Yes, him does. / Yes, its does. / No, it not.)는 주어나 부정의 형태부터 틀려 대답의 규칙을 몰라도 지워진다. 원문항의 오답은 주어는 같고 동사만 다른 대답이다. 발문도 원문항과 다르다.", fix="오답을 같은 주어에 동사만 다른 대답으로, 원문항 발문으로")

X(5, 17, r="3인칭 단수 주어 뒤의 일반동사 현재형에는 -(e)s를 붙인다. -ch, -sh로 끝나면 -es를 붙인다.",
  n=["두 주어 모두 3인칭 단수라 -s가 필요하므로", "주어 my dad에 read를 쓸 수 없으므로", "주어 My mom에 watch를 쓸 수 없으므로", "-ing형만으로는 동사 자리를 채울 수 없으므로", "두 주어 모두 3인칭 단수라 watches, reads가 알맞으므로"],
  st="① 주어를 하나씩 본다: {0}. 둘 다 3인칭 단수다. → ② 동사에 -(e)s를 붙인다: {1}. → ③ 정답은 {a}.",
  R=("My mom, my dad", "watch는 -ch로 끝나 watches, read는 reads"), B=("The city bus, the last train", "arrives, leaves"), C=("Jane, Tom", "study는 ‘자음 + y’라 studies, play는 plays"),
  D=("My sister, my brother", "carry는 carries, go는 goes"), E=("The dog, the cat", "runs, sleeps"), F=("Dad, Mom", "wash는 -sh로 끝나 washes, cook은 cooks"))

X(5, 18, r="be동사의 줄임말: I'm, you're, he's, it's, isn't, aren't. am not은 줄임말이 없어 I'm not으로 쓴다.",
  n=["you are의 줄임말 you're로 옳으므로", "is not의 줄임말 isn't로 옳으므로", "am not은 amn't로 줄이지 않고 I'm not으로 쓰므로", "it is의 줄임말 it's로 옳으므로", "are not의 줄임말 aren't로 옳으므로"],
  st="① 밑줄 친 줄임말이 실제로 쓰는 꼴인지, 주어와 맞는지 본다. → ② {0} → ③ 정답은 {n}.",
  R="am not은 줄임말이 없다. I'm not으로 쓴다.", B="We에는 isn't가 아니라 aren't를 쓴다.", C="She에는 aren't가 아니라 isn't를 쓴다.", D="They에는 isn't가 아니라 aren't를 쓴다.", E="We에는 isn't가 아니라 aren't를 쓴다.", F="Tom에는 aren't가 아니라 isn't를 쓴다.")

X(5, 19, r="‘자음 + y’로 끝나는 동사는 y를 i로 바꾸고 -es를 붙인다(study → studies). ‘모음 + y’는 -s만 붙인다(play → plays).",
  n=["go, do는 -es를 붙이는 규칙이므로", "-sh, -ch로 끝나 -es를 붙이는 규칙이므로", "‘모음 + y’라 -s만 붙이므로(buys, says)", "‘자음 + y’라 y를 i로 바꾸고 -es를 붙이므로(flies, cries)", "-s만 붙이는 규칙이므로"],
  st="① <보기>의 동사 원형을 찾는다: study, carry. 둘 다 ‘자음 + y’로 끝나 y를 i로 바꾸고 -es를 붙였다. → ② 보기에서 두 동사가 모두 ‘자음 + y’로 끝나는 묶음을 찾는다. ‘모음 + y’(play, buy)는 -s만 붙이므로 다르다. → ③ 정답은 {a}.",
  R="", B="", C="", D="", E="", F="")

X(5, 20, r="일반동사가 있으면 Do/Does로, 일반동사 없이 명사·형용사가 오면 be동사로 의문문을 만든다.",
  n=["(A)는 일반동사 play가 있어 Do, (B)는 일반동사가 없어 Are를 쓰므로", "(A)에는 일반동사 play가 있어 Are를 쓸 수 없으므로", "(A)는 Do로 물을 수 있고 (B)의 주어 you에는 Is를 쓰지 않으므로", "주어 you에는 Is를 쓰지 않으므로", "(B)에는 일반동사가 없어 Do를 쓸 수 없으므로"],
  st="① (A) 뒤를 본다: {0}. 일반동사가 있으므로 Do/Does로 묻는다. → ② (B) 뒤를 본다: {1}. 일반동사가 없으므로 be동사로 묻는다. → ③ 주어에 맞추면 {2}다. 이를 말한 것은 {n}.",
  R=("you play", "you a good piano player", "Do, Are"), B=("Mina read", "Mina a careful reader", "Does, Is"), C=("she like", "she a singer", "Does, Is"), D=("they study", "they students", "Do, Are"), E=("Tom read", "Tom at home", "Does, Is"),
  F=("we need", "we ready", "Do, Are"))
RV(5, 20, "B", v="수정(내용)", why="정답 확인. 다만 정답만 (A)·(B)를 나누어 길게 설명하고 오답 네 개는 한 줄짜리 일반론(‘두 빈칸 모두 Do를 쓴다’ 등)이라 길이만으로 정답이 드러난다. 원문항의 오답은 모두 (A)·(B)에 대한 그럴듯한 설명이다. 발문도 원문항과 다르다.", fix="오답을 (A)·(B)에 대한 그럴듯한 오개념으로, 원문항 발문으로")
RV(5, 20, "C", v="수정(내용)", why="정답 확인. 다만 정답만 (A)·(B)를 나누어 길게 설명하고 오답 네 개는 한 줄짜리 일반론이라 길이만으로 정답이 드러난다. 같은 오답이 D~F에도 되풀이된다.", fix="오답을 (A)·(B)에 대한 그럴듯한 오개념으로")
