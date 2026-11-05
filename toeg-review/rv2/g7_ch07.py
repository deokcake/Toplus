# 7급 CH7 일반동사 부정문과 의문문 (61~70) 2차 감수
X(7, 61, r="doesn't는 3인칭 단수 주어(he, she, it, 한 사람·한 개)와 쓴다. I, you, we, they와 복수 주어에는 don't를 쓴다.",
  n=["I에는 doesn't가 아니라 don't를 쓰므로", "Jane은 한 사람이라 doesn't와 어울리므로", "My father는 한 사람이라 doesn't와 어울리므로", "The woman은 한 사람이라 doesn't와 어울리므로", "Your sister는 한 사람이라 doesn't와 어울리므로"],
  st="① 빈칸 뒤가 doesn't이므로 빈칸에는 한 사람·한 개인 주어(3인칭 단수)만 올 수 있다. → ② 보기에서 I, you, we, they나 여럿인 주어를 찾는다: {0}. → ③ 들어갈 수 없는 것은 {n}.",
  R="I", B="Tom and Ben(두 사람)", C="You", D="We", E="They", F="My neighbors(여럿)")

X(7, 62, r="일반동사의 부정은 주어가 3인칭 단수면 does not, I·you·we·they나 복수면 do not을 쓴다.",
  n=["He는 3인칭 단수라 does not이 들어가므로", "She는 3인칭 단수라 does not이 들어가므로", "Bill은 한 사람이라 does not이 들어가므로", "I에는 do not이 들어가 나머지와 다르므로", "The student는 한 사람이라 does not이 들어가므로"],
  st="① 문장마다 주어가 3인칭 단수(한 사람·한 개)인지 본다. 그렇다면 does not, 아니면 do not이다. → ② {0} → ③ 정답은 {n}.",
  R="④의 I만 do not이고 나머지는 모두 does not이다.", B="③의 My friends(여럿)만 do not이고 나머지는 모두 does not이다.", C="②의 We만 do not이고 나머지는 모두 does not이다.", D="④의 You만 do not이고 나머지는 모두 does not이다.",
  E="⑤의 They만 do not이고 나머지는 모두 does not이다.", F="①의 I만 do not이고 나머지는 모두 does not이다.")
RV(7, 62, "B", v="수정(내용)", why="정답 ④ 유일 확인. 다만 다섯 보기가 모두 같은 서술어(need a map)이고 주어만 달라, 서술어가 저마다 다른 원문항보다 보기의 수준이 낮다. 정답 위치(④)도 원문항과 같다.", fix="서술어를 보기마다 다르게, 정답 위치를 옮겨")

X(7, 63, r="일반동사 의문문은 주어가 3인칭 단수면 Does, I·you·we·they나 복수면 Do로 시작한다.",
  n=["she는 3인칭 단수라 Does가 들어가므로", "you에는 Does가 아니라 Do를 쓰므로", "he는 3인칭 단수라 Does가 들어가므로", "Tina는 한 사람이라 Does가 들어가므로", "it은 3인칭 단수라 Does가 들어가므로"],
  st="① 빈칸 바로 뒤의 주어를 본다. 한 사람·한 개(3인칭 단수)면 Does가 들어간다. → ② 그렇지 않은 주어를 찾는다: {0}. → ③ 이 문장에는 Do를 써야 하므로 정답은 {n}.",
  R="you", B="they", C="your parents(여럿)", D="Tom and Ben(두 사람)", E="we", F="I")

X(7, 64, r="일반동사 문장의 의문문은 Do/Does + 주어 + 동사원형 ~?이다. 주어가 3인칭 단수면 Does를 쓰고, 동사는 -s를 뗀 원형(has → have)으로 쓴다.",
  n=["평서문에 물음표만 붙였으므로", "she에는 Do가 아니라 Does를 쓰고 has도 원형이 아니므로", "Does 뒤에는 has가 아니라 원형 have를 써야 하므로", "Does + 주어 + 동사원형으로 바르게 바꿨으므로", "she에는 Do가 아니라 Does를 쓰므로"],
  st="① 동사({0})가 일반동사이므로 Do/Does를 주어 앞에 둔다. be동사를 쓴 것과 물음표만 붙인 것을 지운다. → ② 주어({1})가 3인칭 단수라 Does를 고른다. → ③ Does 뒤의 동사는 원형({2})이어야 하므로 정답은 {n}.",
  R=("has", "she", "have"), B=("eats", "the dog", "eat"), C=("likes", "Tom", "like"), D=("watches", "my father", "watch"), E=("studies", "Jane", "study"), F=("watches", "Tom", "watch"))
RV(7, 64, "DE", fx=True, why="정답 위치가 C·D·E 모두 ⑤였다. 수정 예시에서 D와 E의 보기 순서를 바꿔 정답을 ②와 ①로 옮겼다.")

X(7, 65, r="‘~하니?’라고 일반동사로 물을 때는 Do/Does + 주어 + 동사원형 ~?으로 쓴다. 주어가 you나 복수면 Do를 쓴다.",
  n=["your parents는 두 분(복수)이라 Does가 아니라 Do를 쓰므로", "Do 뒤에는 loves가 아니라 원형 love를 쓰므로", "Do + 복수 주어 + 동사원형으로 바르게 옮겼으므로", "일반동사 의문문에 be동사 Are를 쓰지 않으므로", "지금의 일을 묻는데 과거형 loved를 썼으므로"],
  st="① 우리말의 주어를 본다: ‘{0}’ → {1}. 3인칭 단수가 아니므로 Do로 시작한다. → ② Do + 주어 뒤에는 동사원형({2})을 쓴다. → ③ 정답은 {n}.",
  R=("너의 부모님은", "your parents(여럿)", "love"), B=("우리는", "we", "study"), C=("너는", "you", "like"), D=("그 학생들은", "the students(여럿)", "walk"), E=("그 소년들은", "the boys(여럿)", "play"), F=("그들은", "they", "read"))
RV(7, 65, "D", fx=True, why="변형과 수정 예시의 우리말(그 학생들은 영어를 공부하니?)이 B(우리는 영어를 공부하니?)와 주어만 달랐고 정답 위치(⑤)도 E와 같았다. 수정 예시를 다른 문장(그 학생들은 걸어서 학교에 가니?)으로 바꾸고 정답을 ②로 옮겼다.")

X(7, 66, r="일반동사의 부정은 don't/doesn't + 동사원형이다. 주어가 3인칭 단수면 doesn't, 아니면 don't를 쓴다. be동사 부정(isn't, aren't)이나 not만으로는 일반동사를 부정할 수 없다.",
  n=["He는 3인칭 단수라 don't가 아니라 doesn't를 쓰므로", "He에 맞는 doesn't이므로", "일반동사 play 앞에 be동사 부정을 쓸 수 없으므로", "일반동사 play 앞에 be동사 부정을 쓸 수 없으므로", "not만으로는 일반동사를 부정할 수 없으므로"],
  st="① 빈칸 뒤에 일반동사 원형({0})이 있으므로 be동사 부정(isn't, aren't)과 not을 지운다. → ② 주어({1})를 본다: {2}. → ③ 정답은 {a}.",
  R=("play", "He", "3인칭 단수 → doesn't"), B=("read", "I", "3인칭 단수가 아님 → don't"), C=("live", "My cousins", "여럿 → don't"), D=("need", "We", "3인칭 단수가 아님 → don't"),
  E=("watch", "Jane", "한 사람(3인칭 단수) → doesn't"), F=("like", "They", "3인칭 단수가 아님 → don't"))

X(7, 67, r="Do/Does로 물으면 Yes, 주어 + do/does. / No, 주어 + don't/doesn't.로 답한다. be동사로 답하지 않으며, 대답의 주어는 질문의 주어를 대명사로 받는다(you → I).",
  n=["it에는 do가 아니라 does를 쓰므로", "it에는 don't가 아니라 doesn't를 쓰므로", "Does로 물었으므로 be동사로 답하지 않으므로", "Does로 물었으므로 be동사로 답하지 않으므로", "Does로 묻고 it does로 답했으므로"],
  st="① 질문이 {0}(으)로 시작하므로 대답에도 be동사가 아니라 do/does를 쓴다. → ② 대답의 주어는 {1}. → ③ 정답은 {a}",
  R=("Does", "it이고 it에는 does를 쓴다"), B=("Does", "Tom을 받는 he이고 he에는 does를 쓴다"), C=("Do", "they이고 they에는 do를 쓴다"), D=("Does", "Mina를 받는 she이고, No이므로 doesn't를 쓴다"),
  E=("Do", "your parents를 받는 they이고, No이므로 don't를 쓴다"), F=("Do", "you로 물었으니 I이고, No이므로 don't를 쓴다"))
RV(7, 67, "BD", fx=True, why="수정 예시의 발문에 ‘(단, Tom은 남자)’, ‘(단, Mina는 여자)’ 조건이 붙어 있었다. 보기에 다른 성별의 대명사가 없어 조건이 필요 없으므로 지워 원문항 발문과 같게 했다. B의 ②(Yes, he studies.)는 틀렸다고 잘라 말하기 어려워 분명한 오답(Yes, he doesn't.)으로 바꿨다.")

X(7, 68, r="don't/doesn't 뒤에는 동사원형을 쓴다. 주어가 3인칭 단수면 doesn't, I·you·we·they나 복수면 don't다.",
  n=["doesn't 뒤에는 has가 아니라 원형 have를 써야 하므로", "They에는 don't를 써야 하므로", "I에는 don't를 써야 하므로", "You에는 don't를 써야 하므로", "She에 doesn't, 그 뒤에 원형 have를 바르게 썼으므로"],
  st="① 문장마다 주어와 don't/doesn't가 맞는지 본다(3인칭 단수 → doesn't). → ② 그 뒤의 동사가 원형인지 본다. → ③ {0} 정답은 {n}.",
  R="둘 다 맞는 것은 ⑤(She + doesn't + have)뿐이다.", B="둘 다 맞는 것은 ②(He + doesn't + eat)뿐이다.", C="둘 다 맞는 것은 ①(I + don't + have)뿐이다.", D="둘 다 맞는 것은 ③(They + don't + have)뿐이다.",
  E="둘 다 맞는 것은 ④(You + don't + need)뿐이다.", F="둘 다 맞는 것은 ④(My sisters + don't + eat)뿐이다.")
RV(7, 68, "E", fx=True, why="수정 예시의 정답 문장(You don't have a pencil.)이 원문항 ④(You doesn't have a pencil.)를 고친 꼴이었다. 다른 문장(You don't need a ticket.)으로 바꿨다.")
RV(7, 68, "F", v="수정(내용)", why="정답 ⑤ 유일 확인. 다만 ①(We doesn't eat meat.)과 ⑤(We don't eat meat.)는 don't/doesn't만 다른 짝이라 둘만 견주면 답이 나온다. 다섯 보기의 서술어도 모두 eat meat이다. 정답 위치(⑤)가 원문항과 같고 발문에 조건이 붙었다.", fix="서술어를 보기마다 다르게, 짝 문장 없이, 발문을 원문항대로")

X(7, 69, r="일반동사가 있는 문장을 의문문으로 만들 때 주어 앞에 Do/Does를 쓴다. 3인칭 단수 주어에는 Does, 그 밖의 주어에는 Do를 쓴다. 뜻을 강조하거나 be동사를 줄이려는 것이 아니다.",
  n=["you는 2인칭이고, 3인칭 단수라면 Does를 쓰므로", "낱말의 위치는 Do를 쓰는 이유가 아니므로", "일반동사 문장을 의문문으로 만들 때 Do를 쓰므로", "be동사 문장에는 Do를 쓰지 않으므로", "강조가 아니라 묻는 문장을 만들기 위해 Do를 쓰므로"],
  st="① 문장의 동사를 찾는다: {0}. be동사가 아니라 일반동사다. → ② 일반동사 문장을 의문문으로 만들 때는 주어 앞에 Do/Does를 둔다. {1} → ③ 이 이유를 말한 것은 {n}.",
  R=("need", "주어 you에는 Do를 쓴다."), B=("read", "주어 your sister는 3인칭 단수라 Does를 쓴다."), C=("study", "주어 we에는 Do를 쓴다."), D=("work", "주어 Tom은 3인칭 단수라 Does를 쓴다."), E=("play", "주어 they에는 Do를 쓴다."),
  F=("like", "주어 she는 3인칭 단수라 Does를 쓴다."))
RV(7, 69, "B", v="수정(내용)", why="정답 ② 유일 확인. 다만 오답이 문장과 관계없는 짧은 일반론(‘목적어가 있기 때문이다’ 등)이고 정답만 길고 구체적이어서 길이만으로 답이 드러난다. 문장(Does Tom read books?)의 주어와 정답 문구도 D(Does Tom work here?)와 거의 같다. 밑줄도 사라졌다.", fix="오답을 문장 속 낱말을 두고 말하는 오해로, 주어를 바꾸고 밑줄을 원문항대로")

X(7, 70, r="주어가 3인칭 단수면 doesn't, I·you·we·they와 복수 주어면 don't를 쓰고, 그 뒤에는 동사원형을 쓴다.",
  pre=["문장별 판정: ⓐ X. I에는 don't를 쓴다. ⓑ O. They + don't + have. ⓒ X. don't 뒤에는 원형 work를 쓴다. ⓓ O. You + don't + need. ⓔ X. She에는 doesn't를 쓴다."],
  k="올바른 문장은 ⓑ, ⓓ이다.", n=["ⓐ가 틀린 문장이므로", "ⓑ, ⓓ가 모두 올바른 문장이므로", "ⓒ, ⓔ 모두 틀린 문장이므로", "ⓐ, ⓒ, ⓔ 모두 틀린 문장이므로", "ⓔ가 틀린 문장이므로"],
  st="① 문장마다 주어와 don't/doesn't가 맞는지 본다(3인칭 단수 → doesn't). → ② 그 뒤의 동사가 원형인지 본다. {0} → ③ 올바른 것만 모으면 {a}이다.",
  R="ⓐ I + doesn't(X), ⓑ O, ⓒ don't + works(X), ⓓ O, ⓔ She + don't(X).", B="ⓐ O, ⓑ He + don't(X), ⓒ O, ⓓ We + doesn't(X), ⓔ O.", C="ⓐ O, ⓑ They + doesn't(X), ⓒ Tom + don't(X), ⓓ O, ⓔ doesn't + barks(X).",
  D="ⓐ We + doesn't(X), ⓑ Jane + don't(X), ⓒ O, ⓓ O, ⓔ O.", E="ⓐ O, ⓑ O, ⓒ O, ⓓ You + doesn't(X), ⓔ I + doesn't(X).", F="ⓐ She + don't(X), ⓑ O, ⓒ O, ⓓ They + doesn't(X), ⓔ O.")
RV(7, 70, "D", v="수정(내용)", why="정답 ④ 유일 확인. 다만 정답 조합(ⓐ, ⓒ, ⓔ)이 B와 같다(유형 간 중복). 발문도 ‘옳은 문장을 모두 고른 것’으로 바뀌었다.", fix="문장 순서를 바꿔 정답 조합을 다르게, 발문을 원문항대로")
