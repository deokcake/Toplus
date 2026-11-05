# 3급 CH12 전치사 (111~120) 2차 감수
X(3, 111, r="in은 공간의 안(in the park)과 하루의 한때·달·연도·계절(in the afternoon, in July) 앞에 쓴다.",
  n=["around the park는 되지만 around the afternoon은 ‘오후쯤’이라 회의가 열리는 때로 어색하므로", "the park, the afternoon 앞에 on을 쓰지 않으므로", "공원 안(in the park), 오후에(in the afternoon) 모두 in을 쓰므로", "for는 장소나 때를 나타내지 못하므로", "to는 방향을 나타내 두 문장 모두 맞지 않으므로"],
  st="① 두 문장을 따로 본다. 첫 문장: {0}. → ② 둘째 문장: {1}. → ③ 두 자리에 모두 맞는 전치사는 {a}.",
  R=("공원 ‘안’이라는 공간이므로 in", "the afternoon처럼 하루의 한때 앞에는 in"), B=("가방 ‘안’이므로 in", "달(July) 앞에는 in"), C=("요일(Monday) 앞에는 on", "날짜(May 5th) 앞에도 on"), D=("시각(eight) 앞에는 at", "noon(정오)도 한 시점이라 at"),
  E=("two hours처럼 기간의 길이 앞에는 for", "an hour도 기간의 길이라 for"), F=("the game처럼 일이 벌어진 때를 나타내는 명사 앞에는 during", "the break도 같은 경우라 during"))

X(3, 112, r="층은 on(on the fifth floor), ‘~의’라는 소속은 of로 나타낸다. 한 지점은 at(at the corner), in front of·in the middle of는 굳어진 표현이다.",
  n=["층 앞에는 at이 아니라 on을 쓰므로", "‘그 건물의 5층’은 at이 아니라 of로 이으므로", "on the fifth floor(5층에) of that building(그 건물의)으로 알맞으므로", "층 앞에는 in이 아니라 on을 쓰므로", "층 앞에는 at을 쓰지 않고 on that building은 ‘건물 위에’가 되므로"],
  st="① (A)를 정한다: {0} → ② (B)를 정한다: {1} → ③ 정답은 {n}.",
  R=("층(floor)은 건물의 한 면으로 보아 on the fifth floor로 쓴다.", "‘그 건물의 5층’이므로 소속을 나타내는 of를 쓴다."), B=("층(floor)은 on the fifth floor로 쓴다.", "‘그 건물의 5층’이므로 of를 쓴다."),
  C=("모퉁이는 한 지점이므로 at the corner로 쓴다.", "‘두 길의 모퉁이’이므로 of를 쓴다."), D=("꼭대기 면 위이므로 on the top으로 쓴다.", "‘책상의 윗면’이므로 of를 쓴다."),
  E=("‘~ 앞에’는 in front of로 굳어진 표현이다. (A)는 in이다.", "(B)는 of다."), F=("‘~ 한가운데에’는 in the middle of로 굳어진 표현이다. (A)는 in이다.", "(B)는 of다."))

X(3, 113, r="by는 ‘~까지’ 끝내야 하는 기한, until은 ‘~까지’ 계속되는 동작·상태의 끝을 나타낸다.",
  n=["제출은 월요일까지 끝내는 기한이라 by, 파티는 자정까지 계속되므로 until이 알맞으므로", "by와 until을 반대로 썼으므로", "for 뒤에는 기간의 길이가 오므로", "submit은 계속되는 동작이 아니라 until과 어울리지 않고, last(계속되다)의 끝은 at이 아니라 until로 나타내므로", "last(계속되다)의 끝은 to가 아니라 until로 나타내므로"],
  st="① 동사가 한 번에 끝나는 동작인지, 계속되는 동작·상태인지 본다. → ② {0} → ③ 정답은 {a}.",
  R="submit(제출하다)은 한 번에 끝나는 동작이라 기한의 by, last(계속되다)는 이어지는 상태라 until을 쓴다.", B="return(반납하다)은 한 번에 끝나는 동작이라 기한의 by, stay open(열려 있다)은 이어지는 상태라 until을 쓴다.",
  C="① 빈칸 뒤의 말을 본다: three hours는 기간의 길이, the game은 일이 벌어진 때를 나타내는 명사다. → ② 기간의 길이 앞에는 for, 그런 명사 앞에는 during을 쓴다. → ③ 정답은 {a}.",
  D="① 빈칸 뒤의 말을 본다: nine은 시각, Monday는 요일이다. → ② 시각 앞에는 at, 요일 앞에는 on을 쓴다. → ③ 정답은 {a}.",
  E="① 빈칸 뒤의 말을 본다: 2010은 연도, May 5th는 날짜다. → ② 연도 앞에는 in, 날짜 앞에는 on을 쓴다. → ③ 정답은 {a}.",
  F="finish(끝내다)는 한 번에 끝나는 동작이라 기한의 by를 쓴다. an hour는 기간의 길이라 for를 쓴다.")
RV(3, 113, "E", fx=True, why="수정 예시의 정답 조합과 위치(by - until, ①)가 원문항과 같아, 보기 순서를 바꿔 정답 위치를 ④로 옮겼다.")

X(3, 114, r="before(~ 전에), after(~ 후에), on(표면에 닿은 위), under(아래), in(안), during + 특정한 때를 나타내는 명사(~ 동안). for 뒤에는 기간의 길이, while 뒤에는 주어 + 동사가 온다.",
  n=["‘전에’ before, ‘위에’ on, ‘휴가 기간 동안’ during이 모두 알맞으므로", "after는 ‘후에’이고 over는 떨어진 위이며 for 뒤에는 기간의 길이가 오므로", "over와 for가 알맞지 않으므로", "after는 ‘수업 전에’와 맞지 않으므로", "the summer vacation은 기간의 길이가 아니라 for를 쓸 수 없으므로"],
  st="① {2}에서 전치사에 해당하는 말을 찾는다: {0}. → ② 차례로 옮긴다: {1}. → ③ 정답은 {a}.",
  R=("‘전에’, ‘위에’, ‘동안’", "‘전에’ before, 책상에 닿은 ‘위에’ on, the summer vacation처럼 특정한 때를 나타내는 명사 앞의 ‘동안’ during", "괄호 속 우리말"),
  B=("‘전에’, ‘표면 위에’, ‘중에’", "before, on, during(while 뒤에는 주어 + 동사가 온다)", "발문의 우리말 뜻"), C=("‘전에’, ‘벽 표면 위에’, ‘경기 중에’", "before, on, during(while 뒤에는 주어 + 동사가 온다)", "발문의 우리말 뜻"),
  D=("‘전에’, ‘아래에’, ‘휴식 시간 중에’", "before, under, during", "발문의 우리말 뜻"), E=("‘후에’, ‘아래에’, ‘겨울 중에’", "after, under, during", "발문의 우리말 뜻"), F=("‘후에’, ‘안에’, ‘폭풍이 치는 동안’", "after, in, during", "발문의 우리말 뜻"))

X(3, 115, r="시각·night 앞은 at, 요일·날짜 앞은 on, 달·연도·계절 앞은 in. 표면에 닿은 위는 on, 한 지점은 at, 공간의 안은 in.",
  pre=["문장별 판정: ⓐ O. at night. ⓑ X. 연도 앞에는 in(in 2010). ⓒ X. 소파 위이므로 on the sofa. ⓓ O. 입구라는 한 지점이므로 at."],
  n=["ⓑ가 틀렸으므로", "ⓐ와 ⓓ가 모두 옳으므로", "ⓑ, ⓒ가 모두 틀렸으므로", "ⓑ가 틀렸으므로", "ⓒ가 틀렸으므로"],
  st="① 문장마다 전치사와 그 뒤의 말을 짝지어 본다(때: at 시각, on 요일·날짜, in 달·연도 / 곳: on 표면, at 지점, in 안). → ② {0} → ③ 옳은 문장만 고른 {a}가 정답이다.",
  R="ⓑ on 2010은 in 2010으로, ⓒ in the sofa는 on the sofa로 써야 한다. ⓐ, ⓓ는 옳다.", B="b on 2010(in 2010), c in the sofa(괄호의 뜻대로면 on the sofa)가 틀렸다. a, d, e는 옳다.",
  C="b at Seoul(in Seoul), e in 8 o'clock(at 8 o'clock)이 틀렸다. a, c, d는 옳다.", D="c at Friday(on Friday)만 틀렸다. 나머지 넷은 옳다.", E="c in the wall(괄호의 뜻대로면 on the wall)만 틀렸다. 나머지 넷은 옳다.",
  F="c on 2015(in 2015)만 틀렸다. 나머지 넷은 옳다.")

X(3, 116, r="시각 앞에는 at, 요일·날짜 앞에는 on, 달·연도·계절 앞에는 in을 쓴다.",
  n=["in은 달·연도·계절이나 아침·오후 앞에 쓰므로", "시각 앞에는 at을 쓰므로", "on은 요일·날짜 앞에 쓰므로", "by 6 a.m.은 ‘6시까지’라 우리말(6시에)과 맞지 않으므로", "for 뒤에는 기간의 길이가 오므로"],
  st="① 빈칸 뒤의 때를 나타내는 말이 무엇인지 본다: {0}. → ② 시각은 at, 요일·날짜는 on, 달·연도·계절은 in을 쓴다. → ③ 정답은 {a}.",
  R="6 a.m.은 시각", B="6 a.m.은 시각", C="Monday는 요일", D="2010은 연도", E="August는 달", F="May 5th는 날짜")

X(3, 117, r="by는 ‘~까지’ 끝내야 하는 기한, until은 ‘~까지’ 계속되는 동작·상태의 끝을 나타낸다.",
  n=["finish는 한 번에 끝나는 동작이라 기한을 나타내는 by가 알맞으므로", "at 5 p.m.은 ‘5시에’라 우리말(5시까지)과 맞지 않으므로", "시각 앞에 in을 쓰지 않으므로", "during 뒤에는 시각이 아니라 기간을 나타내는 명사가 오므로", "for 뒤에는 기간의 길이가 오므로"],
  st="① {0} → ② {1} → ③ 정답은 {a}.",
  R=("동사 finish(끝내다)는 계속되는 동작이 아니라 한 번에 끝나는 동작이다.", "‘~까지’가 기한이면 by, 계속이면 until이다. 여기서는 기한이므로 until을 by로 고친다."),
  B=("동사 finish(끝내다)는 계속되는 동작이 아니라 한 번에 끝나는 동작이다.", "‘~까지’가 기한이면 by, 계속이면 until이다. 여기서는 기한이므로 until을 by로 고친다."),
  C=("발문의 뜻은 ‘두 시간 동안’이다. two hours는 기간의 길이다.", "기간의 길이 앞에는 for를 쓴다. by를 for로 고친다."), D=("발문의 뜻은 ‘2010년에’다. 2010은 연도다.", "연도 앞에는 in을 쓴다. on을 in으로 고친다."),
  E=("발문의 뜻은 ‘월요일에’다. Monday는 요일이다.", "요일 앞에는 on을 쓴다. in을 on으로 고친다."), F=("발문의 뜻은 ‘8시에’다. eight는 시각이다.", "시각 앞에는 at을 쓴다. on을 at으로 고친다."))
RV(3, 117, "BCDEF", fx=True, why="원문항 제시문에 우리말 뜻을 붙인 데 맞춰(at도 옳은 문장이 되는 문제를 막기 위함), 수정 예시에도 제시문 아래에 우리말 뜻을 붙였다.")

X(3, 118, r="be born은 과거형(was/were born)으로 쓴다. 연도·달 앞에는 in, 날짜·요일 앞에는 on, 시각 앞에는 at을 쓴다.",
  n=["태어난 것은 과거의 일이라 am이 아니라 was를 쓰므로", "연도 앞에는 at이 아니라 in을 쓰므로", "was born + in + 연도로 바르게 썼으므로", "주어 I에는 were가 아니라 was를 쓰므로", "연도 앞에는 on이 아니라 in을 쓰므로"],
  st="① 동사부터 정한다: {0}. → ② 때를 나타내는 말 앞의 전치사를 정한다: {1}. → ③ 정답은 {n}.",
  R=("‘태어났다’는 과거이고 주어가 I이므로 was born", "2019는 연도이므로 in"), B=("‘태어났다’는 과거이고 주어가 I이므로 was born", "2019는 연도이므로 in"), C=("‘태어났다’는 과거이고 주어가 Jane이므로 was born", "May는 달이므로 in"),
  D=("‘태어났다’는 과거이고 주어가 Tom이므로 was born", "May 3rd는 날짜이므로 on"), E=("‘만났다’는 과거이므로 met", "Monday는 요일이므로 on"), F=("‘시작한다’는 현재이고 주어 School이 3인칭 단수이므로 starts", "8 o'clock은 시각이므로 at"))

X(3, 119, r="둘 사이는 between A and B, 셋 이상 사이는 among이다. next to(~ 옆에), behind(~ 뒤에), in front of(~ 앞에), across from(~ 맞은편에).",
  n=["next to는 ‘~ 옆에’이므로", "between A and B(A와 B 사이에)로 바르게 썼으므로", "among은 셋 이상 사이에 쓰고 or로 잇지 않으므로", "between 뒤의 둘은 or가 아니라 and로 이으므로", "at에는 ‘사이에’라는 뜻이 없으므로"],
  st="① 우리말에서 위치를 나타내는 말을 찾는다: {0}. → ② 영어 표현을 떠올린다: {1}. → ③ 정답은 {n}.",
  R=("‘은행과 병원 사이에’", "둘 사이는 between A and B"), B=("‘은행과 병원 사이에’", "둘 사이는 between A and B"), C=("‘학교 옆에’", "next to + 명사(of를 붙이지 않는다)"), D=("‘도서관 맞은편에’", "across from + 명사(from이 빠지면 ‘가로질러’가 된다)"),
  E=("‘의자 아래에’", "under the chair(관사를 빠뜨리지 않는다)"), F=("‘은행 앞에’", "in front of + 명사(of를 빠뜨리지 않는다)"))

X(3, 120, r="기간의 길이 앞에는 for, 특정한 때를 나타내는 명사 앞에는 during, 한 지점은 at, 셋 이상 사이는 among을 쓴다. 3인칭 단수 주어의 현재형 동사에는 -s를 붙인다.",
  pre=["문장별 판정: ⓐ X. 주어 It이 3인칭 단수이므로 snows. ⓑ X. 기간의 길이 앞에는 for(for five years). ⓒ O. during + 특정한 때. ⓓ X. 정류장은 한 지점이므로 at the bus stop. ⓔ O. 여럿 사이는 among."],
  k="올바르지 않은 문장은 ⓐ, ⓑ, ⓓ 세 개다.", n=["올바르지 않은 문장은 ⓐ, ⓑ, ⓓ 세 개이므로"] * 5,
  st="① 문장마다 전치사와 뒤의 말을 짝지어 본다. 전치사만 보지 말고 동사의 형태도 함께 확인한다. → ② {0} → ③ 올바르지 않은 문장은 {a}이다.",
  R="ⓐ는 전치사가 아니라 동사가 틀렸다(It snows). ⓑ by five years(for), ⓓ on the bus stop(at)도 틀렸다. ⓒ, ⓔ는 옳다.", B="a at winter(in winter), b by five years(for five years)가 틀렸다. c, d, e는 옳다.",
  C="a on 2010(in 2010), d by two hours(for two hours)가 틀렸다. b, c, e는 옳다.", D="c at Korea(in Korea), d until Friday(끝내는 기한이므로 by Friday)가 틀렸다. a, b, e는 옳다.",
  E="c in the wall(괄호의 뜻대로면 on the wall), e until noon(돌아오는 기한이므로 by noon)이 틀렸다. a, b, d는 옳다.", F="c by three hours(for three hours)만 틀렸다. 나머지 넷은 옳다.")
RV(3, 120, "C", fx=True, why="수정 예시의 정답이 원문항과 같은 3개(③)여서, 틀린 문장으로 바꿨던 ⓒ를 원래 문장으로 되돌려 2개로 했다.")
