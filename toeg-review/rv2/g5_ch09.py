# 5급 CH9 전치사 (81~90) 2차 감수
X(5, 81, r="위치 전치사: in(~ 안에), on(~ 위에), under(~ 아래에), behind(~ 뒤에), in front of(~ 앞에), next to(~ 옆에), between(~ 사이에).",
  n=["in front of는 ‘~ 앞에’이므로", "in이 ‘~ 안에’이므로", "next to는 ‘~ 옆에’이므로", "behind는 ‘~ 뒤에’이므로", "between은 ‘~ 사이에’이므로"],
  st="① 우리말에서 위치를 나타내는 말을 찾는다: ‘{0}’. → ② 그 뜻의 전치사는 {1}. → ③ 문장은 전치사만 다르므로 전치사만 견준다. 정답은 {n}.",
  R=("안에", "in"), B=("아래에", "under"), C=("위에", "on"), D=("뒤에", "behind"), E=("아래에", "under"), F=("옆에", "next to"))

X(5, 82, r="전치사는 명사 앞에 온다. ‘~에(서)’라는 장소는 in + 장소 명사로 나타낸다.",
  n=["My 앞은 문장의 맨 앞이라 in이 올 자리가 아니므로", "cousin은 주어의 일부이므로", "lives는 동사라 그 앞에 in이 올 수 없으므로", "장소 명사 Seoul 앞에 in을 넣어 in Seoul이 되므로", "문장 끝에 전치사만 남길 수 없으므로"],
  st="① 우리말을 영어 어순으로 옮긴다: {0} → ② in은 ‘{1}’에 해당하므로 그 장소 표현의 맨 앞에 넣는다. → ③ in 바로 뒤에 오는 낱말은 {a}. 정답은 {n}.",
  R=("My cousin lives (in) Seoul.", "서울에"), B=("My aunt works (in) Busan.", "부산에서"), C=("Tom is (in) Daejeon now.", "대전에"), D=("Students (in) my class are kind.", "우리 반(의)"),
  E=("My grandparents live happily (in) Jeju.", "제주에서"), F=("They study quietly (in) the room.", "방 안에서"))
RV(5, 82, "C", fx=True, why="수정 예시의 문장(Tom lives in Seoul with his family.)은 여섯 낱말인데 선택지에 다섯 낱말만 나와 마지막 낱말(family)이 빠져 있었고, 도시도 원문항(Seoul)과 같았다. 다섯 칸에 다 들어가는 문장(Tom is in Daejeon now.)으로 바꿨다.")

X(5, 83, r="시간 전치사: at + 시각·night, on + 요일·날짜, in + 달·계절·연도·the morning. 장소는 in(안), on(표면 위), at(지점)이다.",
  n=["계절 앞에는 on이 아니라 in을 쓰므로", "the morning 앞에 in을 바르게 썼으므로", "요일 앞에 on을 바르게 썼으므로", "night 앞에 at을 바르게 썼으므로", "교실 안이라는 장소에 in을 바르게 썼으므로"],
  st="① 밑줄 뒤의 말이 시각·요일·날짜·달·계절·연도·장소 가운데 무엇인지 가른다. → ② 그 종류에 맞는 전치사인지 본다. → ③ {0} 정답은 {n}.",
  R="① winter는 계절이라 in winter다.", B="⑤ Friday afternoon은 특정 요일의 오후라 on을 쓴다.", C="② May 5th는 날짜라 on을 쓴다.", D="① 9 o'clock은 시각이라 at을 쓴다.", E="③ Friday는 요일이라 on을 쓴다.",
  F="④ 2012는 연도라 in을 쓴다.")

X(5, 84, r="What year에는 연도로, What month에는 달로, What day에는 요일로, What time에는 시각으로 답한다. 연도·달·계절은 in, 요일은 on, 시각은 at과 쓴다.",
  n=["summer는 계절이라 연도를 묻는 말의 답이 아니므로", "December는 달이므로", "연도(2016)로 답했으므로", "Tuesday는 요일이므로", "Ulsan은 장소이므로"],
  st="① 질문이 묻는 정보를 본다: {0}. → ② 보기는 문장의 앞부분이 같고 뒤의 정보만 다르다. 그 정보의 종류를 하나씩 가른다. → ③ {1} 정답은 {n}.",
  R=("What year(연도)", "연도는 2016뿐이다."), B=("What month(달)", "달은 October뿐이다."), C=("What season(계절)", "계절은 spring뿐이다."), D=("What day(요일)", "요일은 Monday뿐이다."),
  E=("What time(시각)", "시각은 9 o'clock뿐이다."), F=("Where(장소)", "사는 곳을 말한 것은 in Ulsan뿐이다."))

X(5, 85, r="at + 시각·night·home(지점), on + 요일·날짜, in + 달·계절·연도·the morning·나라/도시.",
  n=["달 앞에는 in을 쓰므로", "at home은 ‘집에’라는 옳은 표현이므로", "the morning 앞에는 in을 쓰므로", "요일 앞에는 on을 쓰므로", "night 앞에는 at을 쓰므로"],
  st="① 밑줄 뒤의 말을 종류별로 가른다(시각, 요일·날짜, 달·계절·연도, 장소). → ② 맞는 전치사를 떠올려 밑줄과 견준다. → ③ {0} 정답은 {n}.",
  R="②만 옳다(at home). ① in December, ③ in the morning, ④ on Sunday, ⑤ at night.", B="①만 옳다(on the table). ② in Canada, ③ at seven o'clock, ④ in October, ⑤ on Sunday.", C="④만 옳다(in Korea). ① on Saturday, ② at six, ③ in summer, ⑤ at home.",
  D="③만 옳다(at the park). ① at seven, ② in 2013, ④ on Friday, ⑤ in winter.", E="②만 옳다(on June 10th). ① in Japan, ③ at noon, ④ in July, ⑤ at night.", F="⑤만 옳다(in my bag). ① at ten, ② on Sunday, ③ in 2020, ④ at school.")

X(5, 86, r="시각 앞에는 at, 요일·날짜 앞에는 on, 달·계절·연도 앞에는 in을 쓴다.",
  n=["시각 8:40 앞에는 at을 쓰므로", "in은 달·계절·연도 앞에 쓰므로", "on은 요일·날짜 앞에 쓰므로", "for는 ‘~ 동안’이라 시작하는 시각을 나타내지 않으므로", "to는 ‘~까지’라 시작하는 시각을 나타내지 않으므로"],
  st="① 빈칸 뒤의 말을 본다: {0}. → ② 그 앞에 쓰는 전치사는 {1}. → ③ 정답은 {n}.",
  R=("8:40(시각)", "at"), B=("noon(정오, 시각)", "at"), C=("May 3rd(날짜)", "on"), D=("August(달)", "in"), E=("Busan(도시)", "in"), F=("Friday(요일)", "on"))

X(5, 87, r="at + 시각, on + 요일·날짜, in + 달·계절·연도·the morning/evening.",
  n=["요일 앞에는 on을 쓰므로", "계절 앞에는 in을 쓰므로", "시각 앞에는 at을 쓰므로", "달 August 앞에 in을 바르게 썼으므로", "the morning 앞에는 in을 쓰므로"],
  st="① 밑줄 뒤의 때를 나타내는 말을 시각 / 요일·날짜 / 달·계절·연도로 가른다. → ② at / on / in과 맞는지 하나씩 본다. → ③ {0} 정답은 {n}.",
  R="④만 옳다(in August). ① on Sunday, ② in spring, ③ at 12:30, ⑤ in the morning.", B="②만 옳다(in October). ① on Monday, ③ in 2015, ④ in the evening, ⑤ at six thirty.", C="⑤만 옳다(at 5 o'clock). ① in July, ② in the evening, ③ on Saturday, ④ in 2016.",
  D="①만 옳다(at 12:30). ② in January, ③ on Friday, ④ in fall, ⑤ in 2019.", E="②만 옳다(in spring). ① on Wednesday, ③ at 8:50, ④ in March, ⑤ in the evening.", F="③만 옳다(in July). ① on Tuesday, ② at midnight, ④ in 2021, ⑤ at 7 a.m.")

X(5, 88, r="문장의 어순은 주어 + 동사 + 나머지다. 전치사는 명사 앞에 오고, between A and B는 ‘A와 B 사이에’다.",
  n=["the는 명사 앞에 오는 말이라 세 번째 자리가 아니므로", "The dog 다음에 동사 is가 세 번째로 오므로", "dog는 두 번째 낱말이므로", "bird는 문장의 마지막 낱말이므로", "and는 cat과 the bird 사이에 오므로"],
  st="① 우리말에 맞게 문장을 완성한다: {0} → ② 앞에서부터 센다. → ③ 세 번째 낱말은 {a}. 정답은 {n}.",
  R="The dog is between the cat and the bird.", B="There are books on the shelf.", C="It is under the chair.", D="Put your bag next to the door.", E="Jane is sitting under the tree.", F="There is a pencil in the box.")

X(5, 89, r="on + 특정한 날(요일, 날짜, New Year's Day), at + 시각(midnight, noon, 3 p.m.), in + 달·연도·the morning/afternoon/evening.",
  n=["특정한 날 앞에 on, midnight 앞에 at을 바르게 짝지었으므로", "특정한 날 앞에는 on을, midnight 앞에는 at을 쓰므로", "(A)와 (B)가 서로 바뀌었으므로", "midnight 앞에는 at을 쓰므로", "특정한 날 앞에는 on을 쓰므로"],
  st="① (A) 뒤의 말: {0}. → ② (B) 뒤의 말: {1}. → ③ 정답은 {n}.",
  R=("New Year's Day(특정한 날) → on", "midnight(시각) → at"), B=("Saturday morning(특정 요일의 아침) → on", "the afternoon → in"), C=("3 p.m.(시각) → at", "Monday(요일) → on"),
  D=("2015(연도) → in", "May(달) → in"), E=("7 o'clock(시각) → at", "the evening → in"), F=("the morning → in", "Sundays(요일) → on"))
RV(5, 89, "B", fx=True, why="변형 발문에 ‘시간 전치사’가 붙어 원문항 발문과 다른데 수정 예시가 변형 발문을 그대로 썼다. 원문항 발문으로 되돌렸다.")
RV(5, 89, "D", v="수정(내용)", why="정답 ③ in - in 유일 확인. 다만 ‘I was born in 2015 in May.’는 연도와 달을 거꾸로 나열해 어색한 문장이다(보통 in May 2015).", fix="두 빈칸을 자연스러운 두 문장으로")
RV(5, 89, "F", v="수정(내용)", why="정답 ⑤ in - in 유일 확인. 다만 ‘We travel in summer in August.’는 뜻이 겹쳐 어색한 문장이고, 정답 조합(in - in)이 D와 같다(유형 간 중복).", fix="문장을 바꿔 정답 조합을 다르게")

X(5, 90, r="at은 장소를 하나의 ‘지점’으로 볼 때 쓴다(at the gate, at the bus stop). 도시·나라처럼 넓은 곳이나 안쪽 공간은 in, 표면 위는 on이다.",
  n=["at이 ‘특정한 지점’을 나타낸다는 옳은 설명이므로", "안쪽 공간은 in으로 나타낸다는 옳은 설명이므로", "on은 ‘~ 위에’를 나타낸다는 옳은 설명이므로", "at + 명사가 장소 정보를 준다는 옳은 설명이므로", "넓은 도시나 국가에는 at이 아니라 in을 쓰므로"],
  st="① <보기>의 at 뒤를 본다: {0}. 장소를 하나의 지점으로 본 표현이다. → ② 설명마다 at / in / on의 쓰임(지점 / 안·넓은 곳 / 표면 위)에 대어 본다. → ③ {1} 정답은 {n}.",
  R=("the school gate", "⑤ 넓은 도시나 국가에는 in을 쓴다(in Seoul)."), B=("the bus stop", "① 나라나 도시의 내부는 in으로 나타낸다."), C=("the restaurant", "② at은 시각뿐 아니라 장소 앞에도 쓰며, 여기서는 장소를 나타낸다."),
  D=("home", "③ at home에는 the를 넣지 않는다."), E=("the door", "④ ‘~ 위에’는 on이고, at the door는 ‘문가에서’다."), F=("the station", "① at은 건물을 나타내는 명사 앞에도 쓴다."))
