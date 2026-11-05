# 4급 CH9 전치사와 접속사 (81~90) 2차 감수
X(4, 81, r="시각 앞에는 at, 요일·날짜 앞에는 on, 달·계절·연도 앞에는 in을 쓴다.",
  n=["시각 seven o'clock 앞에는 at을 쓰므로", "in은 달·계절·연도 앞에 쓰므로", "on은 요일·날짜 앞에 쓰므로", "for는 기간의 길이 앞에 쓰므로", "by는 ‘~까지’라는 기한이라 ‘7시에’와 맞지 않으므로"],
  st="① 빈칸 뒤의 때를 나타내는 말이 무엇인지 본다: {0}. → ② 시각은 at, 요일·날짜는 on, 달·계절·연도는 in이다. → ③ 정답은 {a}.",
  R="seven o'clock은 시각", B="winter는 계절", C="seven o'clock은 시각", D="Monday는 요일", E="August는 달", F="May 3rd는 날짜")

X(4, 82, r="at은 한 지점(at home), on은 표면·층(on the third floor), in은 공간의 안, under는 아래, behind는 뒤를 나타낸다.",
  n=["at home(집에)으로 옳으므로", "침대 아래는 under로 옳으므로", "층 앞에는 at이 아니라 on을 쓰므로", "건물 뒤는 behind로 옳으므로", "탁자 위는 on으로 옳으므로"],
  st="① 밑줄 친 전치사와 뒤의 말을 짝지어 본다. → ② {0} → ③ 정답은 {n}.",
  R="층(floor)은 그 위에 있다는 뜻으로 on the third floor로 쓴다. ③의 at이 틀렸다.", B="날짜(May 3rd) 앞에는 on을 쓴다. ②의 in이 틀렸다.", C="층 앞에는 on을 쓴다. ②의 at이 틀렸다.", D="요일(Monday) 앞에는 on을 쓴다. ④의 in이 틀렸다.",
  E="시각(9 o'clock) 앞에는 at을 쓴다. ④의 on이 틀렸다.", F="도시(Seoul) 앞에는 in을 쓴다. ③의 at이 틀렸다.")
RV(4, 82, "B", fx=True, why="변형의 ⑤(Her house is on the third floor.)는 원문항의 틀린 문장(Her house is at the third floor.)을 고친 것이라 원문항의 정답을 그대로 알려 주는데 수정 예시가 그대로 두었다. 다른 문장(The bakery is on the second floor.)으로 바꿨다.")

X(4, 83, r="on은 요일(Monday), 날짜(May 5th), 특정한 날(Christmas, my birthday) 앞에 쓴다. 달·계절·연도·the morning은 in, 시각·night·noon은 at이다.",
  n=["the morning, May, winter는 모두 in과 쓰므로", "요일, 특정한 날, 날짜는 모두 on과 쓰므로", "7:00 p.m., night, noon은 모두 at과 쓰므로", "2024, autumn, the afternoon은 모두 in과 쓰므로", "lunch time, midnight은 at, January는 in과 쓰므로"],
  st="① 묶음마다 낱말이 무엇인지 가른다: 시각·한 시점(at), 요일·날짜·특정한 날(on), 달·계절·연도·하루의 한때(in). → ② 세 낱말이 모두 요일·날짜·특정한 날인 묶음을 찾는다: {0}. → ③ 정답은 {n}.",
  R="Monday(요일), Christmas(특정한 날), May 5th(날짜)", B="Tuesday(요일), my birthday(특정한 날), March 3rd(날짜)", C="Monday·Sunday(요일), May 5th(날짜)", D="Friday·Sunday(요일), June 1st(날짜)",
  E="Saturday(요일), Christmas Day(특정한 날), July 4th(날짜)", F="Thursday(요일), New Year's Day(특정한 날), August 15th(날짜)")

X(4, 84, r="so는 결과(그래서), because는 이유(~ 때문에), but은 대조, or는 선택, when은 때(~할 때)를 나타낸다.",
  n=["because를 쓰면 ‘집에 있었기 때문에 비가 왔다’가 되어 뜻이 맞지 않으므로", "‘비가 왔다’의 결과가 ‘집에 있었다’이므로", "when은 ‘~할 때’라 뜻이 맞지 않으므로", "but은 대조라 뜻이 맞지 않으므로", "or는 선택이라 뜻이 맞지 않으므로"],
  st="① 우리말에서 두 부분의 관계를 읽는다: {0}. → ② {1} → ③ 정답은 {a}.",
  R=("‘비가 와서’(원인) → ‘집에 있었다’(결과)", "빈칸 뒤가 결과이므로 so다. because는 뒤에 이유가 온다."), B=("‘차 또는 커피’(둘 중 하나)", "선택을 나타내는 접속사는 or다."), C=("‘비가 와서’(원인) → ‘집에 있었다’(결과)", "빈칸 뒤가 결과이므로 so다."),
  D=("‘피곤했지만’(앞뒤가 반대)", "대조를 나타내는 접속사는 but이다."), E=("‘왜냐하면 비가 왔기 때문이다’(이유)", "빈칸 뒤가 이유이므로 because다."), F=("‘Tom이 왔을 때’(때)", "때를 나타내는 접속사는 when이다."))
RV(4, 84, "C", fx=True, why="수정 예시의 정답(so)이 원문항과 같아, 문장을 바꿔 정답을 and로 했다. 이로써 다섯 유형의 정답 접속사가 모두 다르다.")
RV(4, 84, "E", v="수정(내용)", why="정답(because) 확인. 다만 문장(We stayed home because it rained.)이 원문항 문장(It rained, so we stayed at home.)의 앞뒤만 바꾼 것이라, 원문항을 푼 학생에게 내용이 그대로 드러난다. 발문이 바뀐 점도 원문항과 다르다.", fix="문장을 새로, 원문항 발문으로")

X(4, 85, r="표면에 닿아 있으면 on(벽·바닥·천장), 공간 안이면 in, 한 지점이면 at을 쓴다.",
  pre=["문장별 판정: ⓐ O. 벽에 붙어 있으므로 on the wall. ⓑ X. 바닥에 앉는 것은 on the floor. ⓒ X. 천장에 붙어 있으므로 on the ceiling. ⓓ O. 입구라는 한 지점이므로 at."],
  n=["ⓑ가 틀렸으므로", "ⓐ와 ⓓ가 모두 옳으므로", "ⓑ, ⓒ가 모두 틀렸으므로", "ⓑ가 틀렸으므로", "ⓒ가 틀렸으므로"],
  st="① 문장마다 전치사 뒤의 장소가 표면인지, 공간의 안인지, 한 지점인지 가른다. → ② {0} → ③ 옳은 문장만 고른 {a}가 정답이다.",
  R="ⓑ in the floor(on the floor), ⓒ in the ceiling(on the ceiling)이 틀렸다.", B="c under of the tree(under the tree)만 틀렸다.", C="b on of the chair(on the chair), c on of the ceiling(on the ceiling)이 틀렸다.", D="c on home(at home)만 틀렸다.",
  E="c on Seoul(in Seoul)만 틀렸다.", F="c on of the table top(on the table)만 틀렸다.")
RV(4, 85, "BF", fx=True, why="수정 예시 B의 ⓐ와 F의 ⓒ가 같은 문장(The picture is on the wall.)이었고 원문항 ⓐ(There is a clock on the wall.)와도 닮아, 서로 다른 문장으로 바꿨다.")

X(4, 86, r="in은 ‘~ 안에’, on은 ‘~ 위에’(닿아서), under는 ‘~ 아래에’, between은 ‘둘 사이에’, behind는 ‘~ 뒤에’다.",
  n=["on은 ‘~ 위에’라 뜻이 맞지 않으므로", "‘상자 안에’는 in으로 나타내므로", "above는 ‘~보다 위에’라 뜻이 맞지 않으므로", "between은 ‘둘 사이에’라 뜻이 맞지 않으므로", "across는 ‘가로질러’라 뜻이 맞지 않으므로"],
  st="① 우리말에서 위치를 나타내는 말을 찾는다: {0}. → ② 그 뜻의 전치사를 떠올린다: {1}. → ③ 정답은 {a}.",
  R=("‘안에’", "in"), B=("‘학교에’", "학교라는 한 지점은 at"), C=("‘안에’", "in"), D=("‘위에’", "책상에 닿아 있으므로 on"), E=("‘아래에’", "under"), F=("‘사이에’", "둘 사이는 between"))
RV(4, 86, "BDEF", fx=True, why="원문항에는 영어 문장 앞에 화살표(→)가 있는데 수정 예시에는 빠져 있었다. 화살표를 넣어 원문항과 같게 했다.")

X(4, 87, r="during 뒤에는 특정한 때를 나타내는 명사(the lesson), for 뒤에는 기간의 길이(an hour), while 뒤에는 주어 + 동사가 온다.",
  n=["두 자리를 반대로 썼으므로", "while 뒤에는 주어 + 동사가 와야 하므로", "for the lesson, while an hour 모두 맞지 않으므로", "the lesson 앞에 during, an hour 앞에 for가 알맞으므로", "while 뒤에는 주어 + 동사가 와야 하므로"],
  st="① 빈칸 뒤의 말을 본다. 숫자가 든 기간의 길이면 for, 특정한 때를 나타내는 명사면 during, 주어 + 동사면 while이다. → ② {0} → ③ 정답은 {a}.",
  R="the lesson은 명사이므로 during, an hour는 기간의 길이이므로 for다.", B="an hour는 기간의 길이이므로 for, the game은 명사이므로 during이다.", C="the lesson은 명사이므로 during, an hour는 기간의 길이이므로 for다.",
  D="two hours는 기간의 길이이므로 for, the movie는 명사이므로 during이다.", E="I was eating은 주어 + 동사이므로 while, thirty minutes는 기간의 길이이므로 for다.", F="the break는 명사이므로 during, three hours는 기간의 길이이므로 for다.")

X(4, 88, r="because 뒤에는 이유, so 뒤에는 결과가 온다.",
  n=["생일인 것이 기쁜 이유이므로 because가 들어가므로", "아픈 것이 집에 있은 이유이므로 because가 들어가므로", "비가 오기 시작한 것이 안으로 들어간 이유이므로 because가 들어가므로", "색이 마음에 든 것이 산 이유이므로 because가 들어가므로", "배가 부른 것은 많이 먹은 결과이므로 so가 들어가 나머지와 다르므로"],
  st="① 문장마다 빈칸 뒤가 앞일의 이유인지 결과인지 가른다. → ② 이유면 because, 결과면 so다. {0} → ③ 정답은 {n}.",
  R="⑤만 뒤(배가 부르다)가 앞(많이 먹었다)의 결과라 so가 들어간다. 나머지는 because다.", B="⑤만 뒤(배가 부르다)가 결과라 so가 들어간다. 나머지는 because다.", C="①만 뒤(잠자리에 들었다)가 결과라 so가 들어간다. 나머지는 because다.",
  D="③만 뒤(집에 있었다)가 결과라 so가 들어간다. 나머지는 because다.", E="④만 뒤(합격했다)가 결과라 so가 들어간다. 나머지는 because다.", F="⑤만 뒤(뛰었다)가 결과라 so가 들어간다. 나머지는 because다.")
RV(4, 88, "BCDEF", fx=True, why="수정 예시에서 so가 들어가는 문장에만 빈칸 앞에 쉼표가 있어 쉼표만 보고 정답이 가려졌다. 원문항처럼 모든 문장을 쉼표 없이 썼다.")

X(4, 89, r="when이 문장 맨 앞에서 ‘언제’를 묻고 뒤가 의문문 어순이면 의문사, ‘~할 때’라는 뜻으로 두 절을 이으면 접속사다.",
  n=["‘~했을 때’라는 접속사이므로", "‘언제’를 묻는 의문사이므로", "‘~했을 때’라는 접속사이므로", "‘~하면(할 때)’이라는 접속사이므로", "‘~할 때’라는 접속사이므로"],
  st="① 문장 끝에 물음표가 있고 when 뒤가 의문문 어순(do/does/did·be동사 + 주어)이면 ‘언제’를 묻는 의문사다. → ② 그렇지 않고 두 절을 이으면 ‘~할 때’라는 접속사다. → ③ {0} 정답은 {n}.",
  R="②만 ‘언제 자니?’라고 묻는 의문사다.", B="④만 ‘언제 시작하니?’라고 묻는 의문사다.", C="⑤만 ‘언제 자니?’라고 묻는 의문사다.", D="②만 ‘생일이 언제니?’라고 묻는 의문사다.", E="⑤만 ‘언제 오니?’라고 묻는 의문사다.", F="①만 ‘언제 도착했니?’라고 묻는 의문사다.")

X(4, 90, r="달 앞에는 in(in March), 날짜 앞에는 on(on March 1st)을 쓴다. 계절·연도는 in, 요일은 on, 시각은 at이다.",
  n=["달만 있으면 in을 쓰는 것이 맞으므로", "1st는 시각이 아니라 날짜를 나타내므로", "달만 있으면 in, 날짜가 붙으면 on을 쓰므로", "의문문인지는 전치사와 관계가 없으므로", "birthday라는 낱말 때문이 아니라 날짜 때문에 on을 쓰므로"],
  st="① 전치사 뒤의 말이 무엇인지 본다: {0}. → ② {1} → ③ 이 이유를 바르게 말한 것은 {n}.",
  R=("March 1st는 달이 아니라 날짜", "달만 있으면 in, 날짜에는 on을 쓴다."), B=("winter는 계절", "계절 앞에는 on이 아니라 in을 쓴다."), C=("March 1st는 날짜", "달만 있으면 in, 날짜에는 on을 쓴다."), D=("Monday는 요일", "요일 앞에는 in이 아니라 on을 쓴다."),
  E=("8 o'clock은 시각", "시각 앞에는 on이 아니라 at을 쓴다."), F=("2015는 연도", "연도 앞에는 on이 아니라 in을 쓴다."))
