# 5급 CH6 미래 표현 (51~60) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
R_FUT = "미래의 일은 will + 동사원형 또는 be going to + 동사원형으로 나타낸다. 부정은 won't(will not) + 동사원형, be동사 + not going to로 쓰고, be동사는 주어에 맞춰 am/is/are를 쓴다."

# 5-51 원문항 발문
F(5, 51, "B", st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 5-52 빈칸 짝: 원문항 발문(미래·동사 안내 없이)
S552 = "발문에 ‘미래의 계획이나 일을 나타내도록, 둘째 빈칸에는 동사 ○○를 알맞게 바꾸어 넣으시오’가 붙어 넣을 말을 알려 주었다. 원문항 발문으로 되돌렸다."
def f552(t, items, a, s=S552 + " 보기와 정답은 그대로다.", **kw):
    mk(5, 52, t, items, a, R_FUT, s, st="R", okdup=True, **kw)
f552("B", [("go — begins", "첫째 빈칸: be동사 뒤 going to 자리이고, 둘째 빈칸: will 뒤에는 동사원형 begin을 쓰므로"), ("gone — begin", "첫째 빈칸: be동사 뒤 미래 표현은 going to이므로"), ("going — begin", "is going to와 will + 동사원형 begin을 바르게 짝지었으므로"),
           ("going — beginning", "둘째 빈칸: will 뒤에는 동사원형 begin을 써야 하므로"), ("going — begins", "둘째 빈칸: will 뒤에는 동사원형 begin을 써야 하므로")], 3, S552 + " 원문항처럼 두 문장 앞에 ‘-’를 붙였다. 보기와 정답은 그대로다.",
     p="- Tom is ________ to call his uncle tonight.\n- The class will ________ at nine tomorrow.")
f552("C", [("go — calls", "첫째 빈칸: be동사 뒤 미래 표현은 going to이고, 둘째 빈칸: will 뒤에는 동사원형을 쓰므로"), ("going — call", "is going to와 will + 동사원형 call을 바르게 짝지었으므로"), ("going — calls", "둘째 빈칸: will 뒤에는 동사원형 call을 써야 하므로"),
           ("going — calling", "둘째 빈칸: will 뒤에는 동사원형 call을 써야 하므로"), ("gone — call", "첫째 빈칸: be동사 뒤 미래 표현은 going to이므로")], 2)
f552("D", [("going — rain", "are going to와 will + 동사원형 rain을 바르게 짝지었으므로"), ("going — raining", "둘째 빈칸: will 뒤에는 동사원형 rain을 써야 하므로"), ("going — rains", "둘째 빈칸: will 뒤에는 동사원형 rain을 써야 하므로"),
           ("gone — rain", "첫째 빈칸: be동사 뒤 미래 표현은 going to이므로"), ("go — rains", "첫째 빈칸: be동사 뒤 미래 표현은 going to이고, 둘째 빈칸: will 뒤에는 동사원형을 쓰므로")], 1)
f552("E", [("going — going", "둘째 빈칸: will 뒤에는 동사원형 go를 써야 하므로"), ("gone — go", "첫째 빈칸: be동사 뒤 미래 표현은 going to이므로"), ("go — goes", "첫째 빈칸: be동사 뒤 미래 표현은 going to이고, 둘째 빈칸: will 뒤에는 동사원형을 쓰므로"),
           ("going — go", "am going to와 will + 동사원형 go를 바르게 짝지었으므로"), ("going — goes", "둘째 빈칸: will 뒤에는 동사원형 go를 써야 하므로")], 4)
f552("F", [("going — comes", "둘째 빈칸: will 뒤에는 동사원형 come을 써야 하므로"), ("gone — come", "첫째 빈칸: be동사 뒤 미래 표현은 going to이므로"), ("go — comes", "첫째 빈칸: be동사 뒤 미래 표현은 going to이고, 둘째 빈칸: will 뒤에는 동사원형을 쓰므로"),
           ("going — coming", "둘째 빈칸: will 뒤에는 동사원형 come을 써야 하므로"), ("going — come", "is going to와 will + 동사원형 come을 바르게 짝지었으므로")], 5,
     S552 + " 보기 순서를 바꿔 정답 위치가 C와 겹치지 않게 했다.")

# 5-53 going to의 의미: B 원문항 발문, D~F는 미래 문장을 유형마다 새로
F(5, 53, "B", st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
R553 = "be going to + 동사원형은 ‘~할 것이다’라는 미래를 나타낸다. be going to 뒤에 장소 명사가 오면 go의 진행형으로 ‘~에 가고 있다’는 뜻이다."
S553 = "be going to 미래 오답 네 문장이 C와 똑같았다. 유형마다 미래 문장과 정답 문장을 새로 썼다."
FUT = "be going to + 동사원형으로 ‘~할 것이다’라는 미래의 뜻이므로"
def f553(t, items, a, s=S553):
    mk(5, 53, t, [(x, w or FUT) for x, w in items], a, R553, s)
f553("D", [("Jiho is <u>going to</u> wash the car.", ""), ("We are <u>going to</u> visit the zoo.", ""), ("My parents are <u>going to</u> the bank.", "going to 뒤에 장소 the bank가 와서 ‘은행에 가고 있다’는 진행의 뜻이므로"), ("I am <u>going to</u> write a diary.", ""), ("The kids are <u>going to</u> sing together.", "")], 3)
f553("E", [("Mina is <u>going to</u> bake a pie.", ""), ("Dad is <u>going to</u> the airport now.", "going to 뒤에 장소 the airport가 와서 ‘공항에 가고 있다’는 진행의 뜻이므로"), ("They are <u>going to</u> watch a play.", ""), ("You are <u>going to</u> love this song.", ""), ("It is <u>going to</u> snow tonight.", "")], 2)
f553("F", [("He is <u>going to</u> fix the door.", ""), ("I am <u>going to</u> take a bus.", ""), ("We are <u>going to</u> join the club.", ""), ("Grandma is <u>going to</u> the hospital.", "going to 뒤에 장소 the hospital이 와서 ‘병원에 가고 있다’는 진행의 뜻이므로"), ("She is <u>going to</u> wear a dress.", "")], 4)

# 5-54 틀린 문장: 원문항 발문, will/won't/be going to/의문문을 섞어 짝 없이
S554 = "원문항은 will/won't/be going to 문장을 섞어 판별하는데, 변형은 모두 won't 문장이라 범위가 좁았고 짝 문장과 같은 오답이 반복되었다. 여러 미래 표현을 섞어 짝 문장 없이 유형마다 새로 썼다."
OK54 = "미래 표현 뒤에 동사원형을 바르게 썼으므로"
def f554(t, items, a, s=S554):
    mk(5, 54, t, [(x, w or OK54) for x, w in items], a, R_FUT, s, st="R")
f554("B", [("They won't take the early bus.", ""), ("Tom is going to be at school tomorrow.", ""), ("We won't arrived late for the meeting.", "won't 뒤에는 동사원형 arrive를 써야 하므로"), ("Will you tell your mom?", ""), ("Mina won't forget your birthday.", "")], 3,
     "발문이 ‘미래시제 부정문이 틀린 것’으로 범위를 알려 주었고 모두 won't 문장이었다. 원문항 발문으로 되돌리고 be going to 문장과 의문문을 섞었다. 정답은 그대로다.")
f554("C", [("It will be sunny tomorrow.", ""), ("Are they going to move next month?", "주어 they에 Are를 쓰고 going to 뒤에 동사원형을 바르게 썼으므로"), ("I won't be late again.", ""), ("He is going to takes a test.", "be going to 뒤에는 동사원형 take를 써야 하므로"), ("We will meet at the station.", "")], 4)
f554("D", [("Will your sister come to the party?", ""), ("They are going to buy a new car.", ""), ("She won't eat the cake.", ""), ("We are going to stay home.", ""), ("I will calls you tonight.", "will 뒤에는 동사원형 call을 써야 하므로")], 5)
f554("E", [("Are Jane going to join us?", "3인칭 단수 주어 Jane에는 Is를 써야 하므로"), ("My dad will cook dinner.", ""), ("You won't believe this story.", ""), ("It is going to rain soon.", ""), ("Will they win the game?", "")], 1)
f554("F", [("The kids will be happy.", ""), ("Tom won't to come today.", "won't 뒤에는 to 없이 동사원형 come을 써야 하므로"), ("I'm going to learn the guitar.", ""), ("Will you help me?", ""), ("We aren't going to go out.", "")], 2)

# 5-55 대화 밑줄: D·F는 원문항처럼 한 단어씩 밑줄
S555 = "다른 밑줄은 모두 ‘be going to + 동사’ 구인데 정답만 한 단어에 밑줄이 있어 형식만 보고 고를 수 있었다. 원문항처럼 모두 한 단어에 밑줄을 쳐 단위를 통일했다."
def f555(t, p, items, a, s=S555):
    mk(5, 55, t, items, a, R_FUT, s, p=p)
f555("D", "A: What are they going to do tonight?\nB: They are going to ①<u>watches</u> TV.\nA: ②<u>Is</u> Tom going to make popcorn?\nB: Yes. He ③<u>loves</u> popcorn. And Jane ④<u>will</u> bring some juice. They are going to ⑤<u>have</u> fun.",
     [("watches", "be going to 뒤에는 동사원형 watch를 써야 하므로"), ("Is", "3인칭 단수 주어 Tom에 Is를 바르게 썼으므로"), ("loves", "3인칭 단수 주어 He에 맞는 현재형을 바르게 썼으므로"), ("will", "will 뒤에 동사원형 bring을 바르게 썼으므로"), ("have", "are going to 뒤에 동사원형 have를 바르게 썼으므로")], 1,
     S555 + " 대화도 원문항처럼 네 차례 주고받게 했다.")
f555("F", "A: What are you going to do tomorrow?\nB: I ①<u>am</u> going to study English. Then I will ②<u>meet</u> Mina, and we ③<u>is</u> going to play tennis.\nA: ④<u>Will</u> you read a book, too?\nB: No, I ⑤<u>won't</u>.",
     [("am", "주어 I에 am을 바르게 썼으므로"), ("meet", "will 뒤에 동사원형 meet을 바르게 썼으므로"), ("is", "주어 we에는 are를 써야 하므로"), ("Will", "미래의 일을 묻는 의문문을 Will로 바르게 시작했으므로"), ("won't", "Will 의문문에 won't로 바르게 답했으므로")], 3)

# 5-56 우리말 뜻 제시: 원문항 발문
R556 = "be going to 뒤에는 동사원형을 써서 ‘~할 것이다’라는 미래를 나타낸다. -ing형, to부정사, 과거형, 3인칭 단수 현재형은 쓰지 않는다."
S556 = "발문이 ‘알맞은 동사원형을 고르시오’라고 정답 형태를 알려 주었다. 원문항처럼 우리말 뜻을 제시하는 발문으로 바꿨다."
def f556(t, ko, items, a, s=S556 + " 보기와 정답은 그대로다.", **kw):
    mk(5, 56, t, items, a, R556, s, st=f"다음 빈칸에 '{ko}'라는 의미가 되도록 알맞은 단어를 고르세요.", **kw)
ING = "be going to 뒤에는 -ing형이 아니라 동사원형을 쓰므로"; TO = "going to의 to 뒤에 to를 한 번 더 쓸 수 없으므로"; PAST = "과거형이라 be going to 뒤에 쓸 수 없고 미래의 뜻도 되지 않으므로"; S3 = "3인칭 단수 현재형이라 be going to 뒤에 쓸 수 없으므로"
f556("B", "저녁을 요리할 것이다", [("cooking", ING), ("to cook", TO), ("cook", "be going to 뒤에 동사원형 cook을 써서 ‘요리할 것이다’는 뜻이 되므로"), ("cooked", PAST), ("cooks", S3)], 3)
f556("C", "축구를 할 것이다", [("to play", TO), ("play", "be going to 뒤에 동사원형 play를 써서 ‘축구를 할 것이다’는 뜻이 되므로"), ("playing", ING), ("played", PAST), ("plays", S3)], 2)
f556("D", "TV를 볼 것이다", [("watched", PAST), ("watching", ING), ("watches", S3), ("watch", "be going to 뒤에 동사원형 watch를 써서 ‘볼 것이다’는 뜻이 되므로"), ("to watch", TO)], 4, S556 + " 보기 순서를 바꿔 정답 위치가 B와 겹치지 않게 했다.")
f556("E", "책을 읽을 것이다", [("read", "be going to 뒤에 동사원형 read를 써서 ‘읽을 것이다’는 뜻이 되므로"), ("to read", TO), ("reads", S3), ("reader", "‘읽는 사람’이라는 명사라 동사 자리에 쓸 수 없으므로"), ("reading", ING)], 1)
f556("F", "저녁을 먹을 것이다", [("having", ING), ("has", S3), ("to have", TO), ("had", PAST), ("have", "be going to 뒤에 동사원형 have를 써서 ‘먹을 것이다’는 뜻이 되므로")], 5,
     S556 + " 동사가 B(cook)와 겹쳐 have로 바꾸고 정답 위치도 옮겼다.", p="We are going to ________ dinner.")

# 5-57 won't + 밑줄: 짝 없이 유형마다 새로(-s형, -ing형, 과거형 오류)
R557 = "won't(will not) 뒤에는 동사원형을 쓴다. be동사는 won't be로 쓰고, -s형·-ing형·과거형이나 am/is/are는 쓰지 않는다."
S557 = "정답 문장과 같은 문장의 옳은 형태가 함께 있어 대비 단서가 되었고 오답 네 개가 C와 똑같았다. 짝 문장 없이 유형마다 새로 썼다."
OK57 = "won't 뒤에 동사원형을 바르게 썼으므로"
def f557(t, items, a, s=S557):
    mk(5, 57, t, [(x, w or OK57) for x, w in items], a, R557, s)
f557("C", [("My mom won't <u>buy</u> a new phone.", ""), ("The bus won't <u>arrives</u> on time.", "won't 뒤에는 -s형이 아니라 동사원형 arrive를 써야 하므로"), ("We won't <u>be</u> at home tonight.", ""), ("I won't <u>cry</u> again.", ""), ("They won't <u>move</u> to Seoul.", "")], 2)
f557("D", [("Jane won't <u>wear</u> the red dress.", ""), ("You won't <u>need</u> an umbrella.", ""), ("It won't <u>be</u> cold tomorrow.", ""), ("We won't <u>waste</u> water.", ""), ("He won't <u>answering</u> the phone.", "won't 뒤에는 -ing형이 아니라 동사원형 answer를 써야 하므로")], 5)
f557("E", [("The shop won't <u>open</u> on Sunday.", ""), ("I won't <u>lose</u> my key.", ""), ("Dad won't <u>drove</u> today.", "won't 뒤에는 과거형이 아니라 동사원형 drive를 써야 하므로"), ("Mina won't <u>be</u> angry.", ""), ("They won't <u>sell</u> the house.", "")], 3)
f557("F", [("The baby won't <u>sleep</u> well tonight.", ""), ("We won't <u>forget</u> you.", ""), ("My friends won't <u>be</u> there.", ""), ("Tom won't <u>watches</u> the game.", "won't 뒤에는 -s형이 아니라 동사원형 watch를 써야 하므로"), ("It won't <u>take</u> long.", "")], 4)

# 5-58 단어 배열: 원문항 발문, 주어진 단어만으로 만든 어순 오류
R558 = "가까운 미래의 정해진 계획은 현재진행형(am/is/are + -ing)으로 나타낼 수 있다. 평서문은 주어 + be동사 + -ing + 목적어 + 시간 표현의 어순으로 쓰고 마침표로 끝낸다."
S558 = "발문이 ‘주어로 시작하고 마침표로 끝나는 평서문, 현재진행형으로’라고 정답 형식을 알려 주었고, 주어가 빠지거나 물음표로 끝나는 오답은 형식만으로 지워졌다. 원문항 발문으로 되돌리고, 원문항처럼 주어진 단어만으로 만든 어순 오류로 오답을 바꿨다."
Q = "be동사가 주어 앞에 와 의문문 어순인데 마침표로 끝나므로"; INGF = "-ing형이 be동사보다 앞에 왔으므로"; TIME = "시간 표현을 앞에 두면서 주어와 be동사의 순서가 바뀌었으므로"; OBJ = "목적어가 be동사와 -ing형 사이에 끼어들었으므로"; OK58 = "주어 + be동사 + -ing + 목적어 + 시간 표현의 어순으로 바르게 배열했으므로"
def f558(t, items, a, s=S558):
    mk(5, 58, t, items, a, R558, s, st="R")
f558("B", [("Mina is meeting her cousin tonight.", OK58), ("Mina meeting is her cousin tonight.", INGF), ("Is Mina meeting her cousin tonight.", Q), ("Tonight is Mina meeting her cousin.", TIME), ("Mina is her cousin meeting tonight.", OBJ)], 1)
f558("C", [("Jane meeting is Tom tomorrow.", INGF), ("Is Jane meeting Tom tomorrow.", Q), ("Jane is meeting Tom tomorrow.", OK58), ("Tomorrow is Jane meeting Tom.", TIME), ("Jane is Tom meeting tomorrow.", OBJ)], 3)
f558("D", [("They leaving are tonight.", INGF), ("Are they leaving tonight.", Q), ("Tonight are they leaving.", TIME), ("They are tonight leaving.", "시간 표현 tonight이 be동사와 -ing형 사이에 끼어들었으므로"), ("They are leaving tonight.", "주어 + be동사 + -ing + 시간 표현의 어순으로 바르게 배열했으므로")], 5)
f558("E", [("Am I visiting grandma tomorrow.", Q), ("I am visiting grandma tomorrow.", OK58), ("I visiting am grandma tomorrow.", INGF), ("Tomorrow am I visiting grandma.", TIME), ("I am grandma visiting tomorrow.", OBJ)], 2)
f558("F", [("We having are dinner at seven.", INGF), ("At seven are we having dinner.", TIME), ("We are dinner having at seven.", OBJ), ("We are having dinner at seven.", OK58), ("Are we having dinner at seven.", Q)], 4)

# 5-59 현재시제가 쓰인 이유: B 원문항 발문, C~F는 그럴듯한 시제 오개념 오답
R559 = "시간표·일정처럼 이미 정해진 미래의 일은 현재시제로 나타낼 수 있다(The train leaves at 7 tomorrow.). 이때 현재시제는 진행이나 과거를 뜻하지 않으며, will을 써서 말할 수도 있다."
F(5, 59, "B", st="다음 문장에서 'leaves'라는 현재시제가 쓰인 이유를 한국어로 가장 바르게 설명한 것을 고르세요.", s="발문이 원문항과 달랐다. 원문항 발문의 형식으로 되돌렸다. 보기와 정답은 그대로다.")
S559 = "원문항 오답은 진행·완료·습관 같은 그럴듯한 시제 오개념인데, 변형 오답(‘현재시제는 절대 미래를 나타낼 수 없다’ 등)은 뻔하고 유형마다 반복되었다. 원문항처럼 그럴듯한 시제 오개념으로 유형마다 오답을 새로 썼다."
def f559(t, items, a, s=S559):
    mk(5, 59, t, items, a, R559, s)
f559("C", [("기차가 지금 역을 떠나고 있는 중이라는 진행의 뜻을 나타내기 위해서이다.", "leaves는 진행형이 아니라 현재시제라 지금 진행 중인 동작을 나타내지 않으므로"), ("기차가 이미 떠났다는 과거의 사실을 알려 주기 위해서이다.", "tomorrow가 있어 앞으로의 일을 말하는 문장이므로"),
           ("교통편처럼 정해진 일정의 미래는 현재시제로 표현할 수 있기 때문이다.", "정해진 기차 시간표에 따른 미래의 일을 현재시제로 나타낸 것이므로"), ("tomorrow가 미래를 나타내면 동사에는 시제를 붙이지 않아도 되기 때문이다.", "leaves는 시제가 없는 형태가 아니라 현재시제이므로"),
           ("기차가 매일 7시에 떠난다는 습관만을 나타내기 위해서이다.", "tomorrow가 있어 내일 한 번의 일정을 말하는 문장이므로")], 3)
f559("D", [("begins가 3인칭 단수 현재형이라 주어가 하나임을 강조하기 위해서이다.", "-s는 주어와의 수 일치일 뿐 현재시제를 쓴 이유가 아니므로"), ("내일 수업이 시작될지 확실하지 않다는 추측을 나타내기 위해서이다.", "현재시제는 오히려 이미 정해진 확실한 일정을 나타내므로"),
           ("School처럼 사람이 아닌 주어에는 will을 쓸 수 없기 때문이다.", "School will begin at 9 tomorrow.처럼 사물 주어에도 will을 쓸 수 있으므로"), ("수업이 이미 시작되어 진행되고 있다는 뜻을 나타내기 위해서이다.", "tomorrow가 있어 아직 일어나지 않은 앞으로의 일이므로"),
           ("학교 수업은 정해진 시간표에 따른 일이라 현재시제로 미래를 나타낼 수 있기 때문이다.", "정해진 수업 시간표에 따른 미래의 일을 현재시제로 나타낸 것이므로")], 5)
f559("E", [("경기가 지금 막 시작되고 있는 중이라는 진행의 뜻을 나타내기 위해서이다.", "starts는 진행형이 아니라 현재시제이고, tonight 6시의 일이므로"), ("tonight은 오늘에 속하는 시간이라 현재시제만 쓸 수 있기 때문이다.", "The game will start at 6 tonight.처럼 will도 쓸 수 있으므로"),
           ("경기가 매번 6시에 시작한다는 반복적인 습관만을 나타내기 위해서이다.", "tonight이 있어 오늘 밤 한 번의 일정을 말하는 문장이므로"), ("정해진 경기 일정처럼 확정된 미래의 일은 현재시제로 표현할 수 있기 때문이다.", "정해진 경기 일정에 따른 미래의 일을 현재시제로 나타낸 것이므로"),
           ("경기를 꼭 하겠다는 말하는 사람의 의지를 나타내기 위해서이다.", "의지는 will로 나타내고, 이 문장은 정해진 일정을 말할 뿐이므로")], 4)
f559("F", [("정해진 영업 시간처럼 일정에 따른 미래의 일은 현재시제로 나타낼 수 있기 때문이다.", "정해진 영업 일정에 따른 미래의 일을 현재시제로 나타낸 것이므로"), ("가게가 어제 10시에 문을 열었다는 과거의 일을 알려 주기 위해서이다.", "opens는 과거형이 아니고, tomorrow가 있어 앞으로의 일이므로"),
           ("tomorrow가 있으면 will 대신 반드시 현재시제를 써야 하기 때문이다.", "The store will open at 10 tomorrow.처럼 will도 쓸 수 있으므로"), ("가게가 지금 문을 열고 있는 중이라는 동작의 진행을 나타내기 위해서이다.", "opens는 진행형이 아니라 현재시제라 진행 중인 동작을 나타내지 않으므로"),
           ("주어 The store가 3인칭 단수라 동사에 -s를 붙이면 미래의 뜻이 되기 때문이다.", "-s는 주어와의 수 일치일 뿐 미래의 뜻을 만들지 않으므로")], 1)

# 5-60 틀린 부분 개수: 원문항처럼 짧은 글 속 밑줄 (가)~(라), 보기 1개→4개, 0개
R560 = "will과 be going to 뒤에는 동사원형을 쓰고, be going to의 be동사는 주어에 맞춰 am/is/are를 쓴다. 정해진 일정은 현재시제로, 가까운 미래의 계획은 현재진행형으로도 나타낸다."
CNT = ["1개", "2개", "3개", "4개", "0개"]
S560 = "원문항은 짧은 글 속에 밑줄 친 (가)~(라)의 틀린 개수를 묻는데, 변형은 글 흐름 없이 문장을 나열하고 밑줄이 없었으며 보기 순서가 뒤섞였다. 원문항처럼 짧은 글 속 밑줄로 바꾸고 보기를 1개→4개, 0개 순서로 맞췄다."
def f560(t, text, judge, bad, s=S560):
    n = len(bad); a = n if n else 5
    k = f"어법상 틀린 부분은 {', '.join(bad)}로 {n}개이다." if n else "어법상 틀린 부분이 없으므로 0개이다."
    F(5, 60, t, st="R", p=text, c=CNT, a=a, r=R560, pre=["부분별 판정: " + j for j in judge], k=k, n="cnt", okdup=True, s=s + ipos(a))
f560("B", "Next Saturday is our school festival. (가)<u>We are going to decorate</u> the hall in the morning. (나)<u>Mina will brings</u> the posters. (다)<u>Are Tom going to help</u> us? (라)<u>The program starts</u> at two.",
     ["(가) O. are going to 뒤에 동사원형 decorate를 썼다.", "(나) X. will 뒤에는 동사원형 bring을 써야 한다.", "(다) X. 3인칭 단수 주어 Tom에는 Is를 써야 한다.", "(라) O. 정해진 일정을 현재시제로 나타냈다."], ["(나)", "(다)"],
     "밑줄 부분이 다섯 개로 늘고 보기 순서가 뒤섞였다. 원문항처럼 밑줄을 (가)~(라) 네 개로 줄이고 보기를 1개→4개, 0개 순서로 맞췄다.")
f560("C", "Tomorrow is Saturday. (가)<u>I am meeting Tom</u> at the park in the morning. (나)<u>Jane will studies</u> English at home. (다)<u>The train leaves</u> at eight, so we will get up early. (라)<u>We are going to eat</u> dinner together.",
     ["(가) O. 정해진 계획을 현재진행형으로 나타냈다.", "(나) X. will 뒤에는 동사원형 study를 써야 한다.", "(다) O. 기차 시간표를 현재시제로 나타냈다.", "(라) O. are going to 뒤에 동사원형 eat을 썼다."], ["(나)"])
f560("D", "Tonight is a special night. (가)<u>We will watches</u> a movie at home. (나)<u>Tom is going to plays</u> soccer before dinner. (다)<u>Jane won't goes</u> out. (라)<u>The movie starts</u> at nine.",
     ["(가) X. will 뒤에는 동사원형 watch를 써야 한다.", "(나) X. be going to 뒤에는 동사원형 play를 써야 한다.", "(다) X. won't 뒤에는 동사원형 go를 써야 한다.", "(라) O. 정해진 상영 일정을 현재시제로 나타냈다."], ["(가)", "(나)", "(다)"])
f560("E", "Tomorrow is Mom's birthday. (가)<u>I will helps</u> Dad in the kitchen. (나)<u>We are going visit</u> the flower shop. (다)<u>Are Tom going to bake</u> a cake? (라)<u>Jane won't comes</u> home late.",
     ["(가) X. will 뒤에는 동사원형 help를 써야 한다.", "(나) X. be going 뒤에 to를 넣어 are going to visit으로 써야 한다.", "(다) X. 3인칭 단수 주어 Tom에는 Is를 써야 한다.", "(라) X. won't 뒤에는 동사원형 come을 써야 한다."], ["(가)", "(나)", "(다)", "(라)"],
     S560 + " 틀린 개수가 원문항(2개)과 같지 않도록 네 곳 모두 서로 다른 오류로 썼다.")
f560("F", "This afternoon, we have a soccer game. (가)<u>They are playing</u> against our school at three. (나)<u>Tom will go</u> home after the game. (다)<u>The bus leaves</u> at five. (라)<u>We won't be</u> late.",
     ["(가) O. 정해진 계획을 현재진행형으로 나타냈다.", "(나) O. will 뒤에 동사원형 go를 썼다.", "(다) O. 버스 시간표를 현재시제로 나타냈다.", "(라) O. won't 뒤에 be를 썼다."], [],
     S560 + " 틀린 곳이 없는 0개를 정답으로 하여 C와 개수가 겹치지 않게 했다.")


# ---- 2차 감수(2026-10) 추가 ----
# 5-55 C·E: 밑줄이 두 단어(will + 동사)이고 대화가 한 번 주고받는 것뿐 → 원문항처럼 한 단어 밑줄, 네 차례 대화
S555B = "밑줄이 모두 ‘will + 동사’ 두 단어였고 대화도 한 번 주고받는 것뿐이었다. 원문항처럼 한 단어에 밑줄을 치고 네 차례 주고받는 대화로 바꿨다."
f555("C", "A: What will Tom ①<u>do</u> after school?\nB: He will ②<u>goes</u> home early.\nA: ③<u>Will</u> his sister go with him?\nB: No, she ④<u>won't</u>. She is going to ⑤<u>stay</u> at school.",
     [("do", "will + 주어 뒤에 동사원형 do를 바르게 썼으므로"), ("goes", "will 뒤에는 동사원형 go를 써야 하므로"), ("Will", "미래의 일을 묻는 의문문을 Will로 바르게 시작했으므로"), ("won't", "Will 의문문에 won't로 바르게 답했으므로"), ("stay", "is going to 뒤에 동사원형 stay를 바르게 썼으므로")], 2, S555B)
f555("E", "A: What ①<u>will</u> Jane do tomorrow?\nB: She is ②<u>going</u> to visit her aunt.\nA: ③<u>Is</u> she going to take a bus?\nB: No, she ④<u>isn't</u>. Her dad will ⑤<u>drives</u> her there.",
     [("will", "의문사 뒤에 will + 주어 + 동사원형을 바르게 썼으므로"), ("going", "is going to + 동사원형으로 미래를 바르게 나타냈으므로"), ("Is", "3인칭 단수 주어 she에 Is를 바르게 썼으므로"), ("isn't", "Is she ~?에 she isn't로 바르게 답했으므로"), ("drives", "will 뒤에는 동사원형 drive를 써야 하므로")], 5, S555B)
