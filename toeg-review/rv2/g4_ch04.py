# 4급 CH4 시제Ⅰ (31~40) 2차 감수
X(4, 31, r="과거 시제 문장은 동사의 과거형(-ed, 불규칙 과거형, was/were)을 쓴다. 현재형(동사원형, -(e)s)은 현재의 상태·습관을 나타낸다.",
  n=["plays는 현재형이고 every weekend도 현재의 습관을 나타내므로", "walked는 과거형이므로", "were는 be동사의 과거형이므로", "watched는 과거형이므로", "went는 go의 과거형이므로"],
  st="① 문장마다 동사의 형태만 본다. → ② 과거형(-ed, 불규칙 과거형, was/were)인 문장을 지운다. → ③ {0} 정답은 {n}.",
  R="plays는 현재형이다. every weekend(주말마다)도 현재의 습관을 나타낸다.", B="studies는 현재형이다. every day도 현재의 습관을 나타낸다.", C="plays는 현재형이다. every weekend도 현재의 습관을 나타낸다.",
  D="go는 현재형이다. ⑤의 went와 견주면 알 수 있다.", E="watches는 현재형이다. ④의 watched와 견주면 알 수 있다.", F="visit는 현재형이다. on Sundays(일요일마다)도 현재의 습관을 나타낸다.")
RV(4, 31, "BDEF", v="수정(내용)", why="정답 확인. 다만 정답 문장(현재형)과 같은 문장의 과거형이 다른 보기에 함께 있어(She studied / She studies, They go / They went, Tom watched / Tom watches, We visit / We visited) 둘만 견주면 답이 나온다. 원문항에는 이런 짝 문장이 없다.", fix="짝이 되는 문장을 다른 문장으로")

X(4, 32, r="last Friday, yesterday, ~ ago처럼 과거의 때를 나타내는 말이 있으면 동사를 과거형으로 쓴다. go - went, eat - ate, buy - bought, see - saw, write - wrote.",
  n=["goes는 현재형이므로", "last Friday가 있어 go의 과거형 went가 알맞으므로", "go는 현재형이므로", "going만으로는 동사 자리를 채울 수 없으므로", "will go는 미래이므로"],
  st="① 문장에서 때를 나타내는 말을 찾는다: {0}. → ② 과거의 일이므로 동사의 과거형을 쓴다: {1}. → ③ 정답은 {a}.",
  R=("last Friday(지난 금요일)", "go의 과거형은 went"), B=("없음. 발문이 과거형을 고르라고 했다", "eat의 과거형은 ate"), C=("last Friday(지난 금요일)", "go의 과거형은 went"), D=("yesterday(어제)", "buy의 과거형은 bought"),
  E=("last night(어젯밤)", "see의 과거형은 saw"), F=("yesterday(어제)", "write의 과거형은 wrote"))

X(4, 33, r="일반동사 과거 부정문은 주어 + did not(didn't) + 동사원형이다.",
  n=["not만으로는 일반동사를 부정할 수 없으므로", "일반동사의 부정에 was를 쓸 수 없으므로", "did가 빠졌으므로", "didn't 뒤에는 과거형 went가 아니라 동사원형 go를 쓰므로", "did not + 동사원형 go로 바르게 바꿨으므로"],
  st="① 동사를 본다: {0}. 일반동사의 과거형이다. → ② 일반동사 과거 부정은 did not을 쓰고, 뒤의 동사는 원형으로 돌린다: did not {1}. → ③ 정답은 {n}.",
  R=("went", "go"), B=("wrote", "write"), C=("went", "go"), D=("bought", "buy"), E=("saw", "see"), F=("ate", "eat"))
RV(4, 33, "BDEF", v="수정(내용)", why="정답 확인. 다만 오답 하나(We write ~, Tom buy ~, They see ~, Jane eat ~)는 부정문이 아니어서 ‘부정문으로 바꾼 것’이라는 발문만 보고 지워진다. 원문항의 오답은 모두 not을 잘못 쓴 문장이다. 발문에 조건이 붙은 점도 원문항과 다르다.", fix="그 오답을 not을 잘못 쓴 문장으로, 원문항 발문으로")

X(4, 34, r="불규칙 동사의 과거형은 -ed를 붙이지 않는다: meet - met, write - wrote, go - went, buy - bought, see - saw, come - came.",
  n=["go의 과거형 went로 옳으므로", "복수 주어에 were를 써서 옳으므로", "meet의 과거형은 meeted가 아니라 met이므로", "write의 과거형 wrote로 옳으므로", "come의 과거형 came으로 옳으므로"],
  st="① 문장마다 동사의 과거형이 바른지 본다. 불규칙 동사에 -ed를 붙인 것을 찾는다. → ② {0} → ③ 정답은 {n}.",
  R="meet는 불규칙 동사라 과거형이 met이다. meeted는 없는 형태다.", B="write는 불규칙 동사라 과거형이 wrote다. writed는 없는 형태다.", C="meet의 과거형은 met이다. ②의 met과 견주어도 ③이 틀렸다.",
  D="go의 과거형은 went다. goed는 없는 형태다.", E="buy의 과거형은 bought다. buyed는 없는 형태다.", F="see의 과거형은 saw다. seed는 없는 형태다.")

X(4, 35, r="규칙 과거형: -ed를 붙인다. 단모음 + 단자음은 자음을 겹치고(stop → stopped), 자음 + y는 y를 i로 바꾼다(study → studied). Did 의문문에는 동사원형을 쓴다.",
  pre=["문장별 판정: ⓐ O. stop은 p를 겹쳐 stopped. ⓑ X. 자음 + y이므로 studied. ⓒ X. Did 뒤에는 동사원형 buy. ⓓ O. make의 과거형 made."],
  n=["ⓑ가 틀렸으므로", "ⓐ와 ⓓ가 모두 옳으므로", "ⓑ, ⓒ가 모두 틀렸으므로", "ⓑ가 틀렸으므로", "ⓒ가 틀렸으므로"],
  st="① 밑줄 친 동사가 규칙 동사인지 불규칙 동사인지 가른다. 규칙 동사는 철자 규칙(자음 겹치기, y → i)을, 불규칙 동사는 외운 형태를 확인한다. → ② Did가 있으면 뒤가 동사원형인지 본다. → ③ {0} 옳은 문장만 고른 {a}가 정답이다.",
  R="ⓑ studyed(studied), ⓒ Did ~ bought(buy)가 틀렸다.", B="b cryed(cried), d goed(went)가 틀렸다.", C="b studyed(studied), c goed(went)가 틀렸다.", D="b buyed(bought), d stoped(stopped)가 틀렸다.", E="b carryed(carried), d writed(wrote)가 틀렸다.",
  F="b plannned(planned), d buyed(bought)가 틀렸다.")
RV(4, 35, "BDEF", fx=True, why="수정 예시의 문장이 서너 낱말뿐이라 원문항(일고여덟 낱말)의 절반 길이였다. 문장을 원문항 길이에 가깝게 늘렸다. F의 watchd는 run의 틀린 과거형(runned)으로 바꿨다.")
RV(4, 35, "C", fx=True, why="수정 예시의 문장이 서너 낱말뿐이라 원문항의 절반 길이였다. 문장을 원문항 길이에 가깝게 늘렸다.")

X(4, 36, r="There + be동사 구문에서 be동사는 뒤의 명사에 맞춘다. 과거의 일이면 단수 명사 앞에 was, 복수 명사 앞에 were를 쓴다.",
  n=["is는 현재형이고 단수에 쓰므로", "was는 단수 명사 앞에 쓰므로", "are는 현재형이므로", "yesterday가 있어 과거이고 many cookies가 복수라 were가 알맞으므로", "being은 There 뒤 동사 자리에 쓸 수 없으므로"],
  st="① 때를 나타내는 말을 찾는다: {0}. 과거이므로 was나 were다. → ② be동사 뒤의 명사를 본다: {1}. → ③ 정답은 {a}.",
  R=("yesterday", "many cookies는 복수이므로 were"), B=("yesterday", "many students는 복수이므로 were"), C=("yesterday", "many cookies는 복수이므로 were"), D=("yesterday", "a book은 단수이므로 was"), E=("last year", "a big tree는 단수이므로 was"),
  F=("last night", "many people은 복수이므로 were"))
RV(4, 36, "C", fx=True, why="수정 예시의 this morning은 아직 아침이면 현재형 are도 쓸 수 있어 정답이 둘이 될 수 있었다. 과거가 분명한 an hour ago로 바꿨다.")

X(4, 37, r="every Sunday처럼 되풀이되는 일은 현재형으로, yesterday처럼 끝난 일은 과거형으로 쓴다. 현재형은 3인칭 단수 주어일 때 -(e)s를 붙인다.",
  n=["every Sunday는 현재의 습관이라 plays, yesterday는 과거라 played가 알맞으므로", "주어 He는 3인칭 단수라 play가 아니라 plays를 써야 하므로", "yesterday가 있는데 현재형 plays를 쓸 수 없으므로", "두 자리를 반대로 썼으므로", "주어 He에 play를 쓸 수 없고 yesterday에 현재형도 쓸 수 없으므로"],
  st="① 첫 문장의 때를 나타내는 말({0})은 되풀이되는 일이다. 현재형을 쓰되 주어에 맞춘다: {1}. → ② 둘째 문장의 {2}는 끝난 일이다. 과거형을 쓴다: {3}. → ③ 정답은 {a}.",
  R=("every Sunday", "He는 3인칭 단수이므로 plays", "yesterday", "played"), B=("every night", "They는 복수이므로 watch", "yesterday", "watched"), C=("every Sunday", "He는 3인칭 단수이므로 plays", "yesterday", "played"),
  D=("every day", "Jane은 3인칭 단수이므로 studies", "last night", "studied"), E=("every day", "Tom은 3인칭 단수이므로 goes", "yesterday", "went"), F=("every day", "We는 복수이므로 eat", "yesterday", "ate"))

X(4, 38, r="yesterday, last night처럼 과거의 때를 나타내는 말이 있으면 동사는 과거형이어야 한다. run의 과거형은 ran이다.",
  n=["run의 과거형 ran으로 옳으므로", "yesterday가 있는데 과거형 ran이 아니라 run을 썼으므로", "run의 과거형 ran으로 옳으므로", "run의 과거형 ran으로 옳으므로", "과거형 ran, hugged로 옳으므로"],
  st="① 문장마다 동사가 과거형인지 본다. → ② 과거의 때를 나타내는 말이 있는데 동사가 현재형·원형인 문장을 찾는다. → ③ {0} 정답은 {n}.",
  R="②는 yesterday가 있는데 run을 썼다. ran으로 고친다.", B="③은 yesterday가 있는데 run을 썼다. ②의 ran과 견주어도 알 수 있다.", C="⑤는 last night이 있는데 go를 썼다. went로 고친다.", D="②는 yesterday가 있는데 sees를 썼다. saw로 고친다.",
  E="⑤는 last week이 있는데 buy를 썼다. bought로 고친다.", F="②는 yesterday가 있는데 eats를 썼다. ate로 고친다.")

X(4, 39, r="cannot help + -ing = cannot but + 동사원형: ‘~하지 않을 수 없다’.",
  n=["‘걱정할 필요가 없다’는 뜻이라 반대이므로", "cannot but + 동사원형이 cannot help -ing와 같은 뜻이므로", "‘걱정해서는 안 된다’는 뜻이므로", "‘전혀 걱정하지 않는다’는 뜻이므로", "‘네가 걱정하도록 도울 수 있다’는 다른 뜻이므로"],
  st="① 제시문의 뜻을 푼다: cannot help -ing는 ‘~하지 않을 수 없다’. {0} → ② 같은 뜻의 표현은 cannot but + 동사원형이다. → ③ 정답은 {n}.",
  R="걱정하지 않을 수 없다는 뜻이다.", B="경기를 생각하지 않을 수 없다는 뜻이다. but 뒤에는 동사원형 think를 쓴다.", C="걱정하지 않을 수 없다는 뜻이다. but 뒤에는 동사원형 worry를 쓴다.", D="아기를 보고 웃지 않을 수 없다는 뜻이다. but 뒤에는 동사원형 smile을 쓴다.",
  E="그 농담에 웃지 않을 수 없다는 뜻이다. but 뒤에는 동사원형 laugh를 쓴다.", F="그 소식을 이야기하지 않을 수 없다는 뜻이다. but 뒤에는 동사원형 talk를 쓴다.")

X(4, 40, r="과거형은 주어의 인칭·수에 따라 변하지 않는다(be동사 was/were만 예외). 불규칙 동사는 과거형을 따로 익힌다: go - went, buy - bought.",
  n=["Last weekend는 과거의 때라 동사는 과거형으로 써야 하므로", "bought는 주어가 무엇이든 형태가 같으므로", "불규칙 동사는 -d를 붙이지 않고 저마다 다른 형태를 쓰므로", "went와 bought는 현재완료가 아니라 과거형이므로", "busy는 형용사라 -es를 붙이지 않으므로"],
  st="① 글의 동사를 확인한다: {0}. → ② 설명마다 과거형의 규칙과 맞는지 본다. 과거형은 주어에 따라 변하지 않고, 불규칙 동사는 형태를 외워야 한다. → ③ {1} 정답은 {n}.",
  R=("was, went, bought(모두 과거형)", "수현만 bought가 주어와 관계없이 같은 형태라고 바르게 말했다."), B=("studied(study의 과거형)", "유리만 자음 + y는 y를 i로 바꾸고 -ed를 붙인다고 바르게 말했다."),
  C=("bought(buy의 과거형)", "수현만 bought가 주어와 관계없이 같은 형태라고 바르게 말했다."), D=("went(go의 과거형)", "민지만 went가 주어가 바뀌어도 같은 형태라고 바르게 말했다."),
  E=("stopped(stop의 과거형)", "준호만 마지막 자음을 한 번 더 쓰고 -ed를 붙인다고 바르게 말했다."), F=("saw(see의 과거형)", "하나만 see의 과거형이 불규칙하게 saw라고 바르게 말했다."))
