# 2급 CH7 동명사 (61~70) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 2-61 부적합: 원문항처럼 동명사를 목적어로 쓰는 동사 고르기
R61 = "enjoy·finish·avoid·mind·keep·give up 등은 동명사를 목적어로 쓰고, want·hope·expect·agree·decide·plan·promise·refuse 등은 to부정사를 목적어로 쓴다."
S61 = "원문항은 동명사를 목적어로 쓰는 동사(enjoy)를 고르는 문항인데, 변형은 동명사 주어 뒤 단수 동사를 고르는 문항으로 평가 문법이 달랐고, 발문이 ‘단순현재로’라는 조건까지 알려 주었다. 원문항 발문과 형식(동명사 앞에 올 동사 고르기)으로 다시 썼다."
def TO(v): return f"{v}: to부정사를 목적어로 쓰는 동사라 뒤에 동명사가 올 수 없으므로"
def ING(v): return f"{v}: 동명사를 목적어로 쓰는 동사라 빈칸에 알맞으므로"
mk(2, 61, "B", [("wants", TO("wants")), ("hopes", TO("hopes")), ("enjoys", ING("enjoys")), ("decides", TO("decides")), ("promises", TO("promises"))], 3, R61, S61,
   st="R", p="My brother _____ playing online games after dinner.")
mk(2, 61, "C", [("finished", ING("finished")), ("planned", TO("planned")), ("refused", TO("refused")), ("wished", TO("wished")), ("agreed", TO("agreed"))], 1, R61, S61,
   st="R", p="She finally _____ writing her first novel last month.")
mk(2, 61, "D", [("decide", TO("decide")), ("avoid", ING("avoid")), ("expect", TO("expect")), ("hope", TO("hope")), ("want", TO("want"))], 2, R61, S61,
   st="R", p="You should _____ eating too much fast food.")
mk(2, 61, "E", [("want", TO("want")), ("agree", TO("agree")), ("plan", TO("plan")), ("hope", TO("hope")), ("mind", ING("mind"))], 5, R61, S61,
   st="R", p="Would you _____ waiting here for a few minutes?")
mk(2, 61, "F", [("hopes", TO("hopes")), ("refuses", TO("refuses")), ("expects", TO("expects")), ("keeps", ING("keeps")), ("learns", TO("learns"))], 4, R61, S61,
   st="R", p="Tom _____ practicing the piano every day.")

# 2-62 동명사 주어 수 일치: 원문항 형식(틀린 문장 + 'A → B' 보기)
R62 = "동명사(구)가 주어이면 단수로 취급해 단수 동사를 쓴다. 동명사구 안의 복수명사(games, videos 등)에 수를 맞추지 않는다."
S62 = "원문항은 틀린 문장을 주고 어색한 부분을 바르게 바꾼 것을 고르는 형식인데, 변형은 빈칸 채우기로 바뀌었고 발문이 ‘단순현재, and로 연결된 동명사구는 독립된 두 활동’ 같은 판단 근거를 알려 주었다. 원문항 발문과 형식(틀린 문장 + ‘A → B’ 보기)으로 다시 썼다."
def OKV(x, subj): return f"{x}: 동명사구 주어({subj})는 단수로 취급하므로 단수 동사로 바르게 바꿨으므로"
def BAD(x, why): return f"{x}: {why} 원래 표현이 옳고 바꾸면 틀리므로"
mk(2, 62, "B", [("Playing → Play", BAD("Playing → Play", "주어 자리에는 동사원형을 쓸 수 없다.")), ("games → game", BAD("games → game", "셀 수 있는 명사(game)는 관사 없이 단수로 쓸 수 없다.")),
                ("with → by", BAD("with → by", "‘친구들과 함께’는 with로 나타낸다.")), ("make → makes", OKV("make → makes", "Playing board games with friends")),
                ("happy → happily", BAD("happy → happily", "make + 목적어 뒤 목적격 보어 자리에는 형용사를 쓴다."))], 4, R62, S62,
   st="R", p="Playing board games with friends make me happy.")
mk(2, 62, "C", [("Learning → Learn", BAD("Learning → Learn", "주어 자리에는 동사원형을 쓸 수 없다.")), ("take → takes", OKV("take → takes", "Learning new words")),
                ("a lot of → many", BAD("a lot of → many", "셀 수 없는 명사(time) 앞에는 many를 쓸 수 없다.")), ("time → times", BAD("time → times", "‘시간’의 뜻에서는 셀 수 없는 명사이다.")),
                ("practice → practices", BAD("practice → practices", "‘연습’의 뜻에서는 셀 수 없는 명사로 쓴다."))], 2, R62, S62,
   st="R", p="Learning new words take a lot of time and practice.")
mk(2, 62, "D", [("Watching → Watched", BAD("Watching → Watched", "주어 자리에는 동명사를 쓴다.")), ("many → much", BAD("many → much", "셀 수 있는 복수명사(videos) 앞에는 many를 쓴다.")),
                ("videos → video", BAD("videos → video", "셀 수 있는 명사를 관사 없이 단수로 쓸 수 없다.")), ("bad → badly", BAD("bad → badly", "be동사 뒤 보어 자리에는 형용사를 쓴다.")),
                ("are → is", OKV("are → is", "Watching too many videos before bed"))], 5, R62, S62,
   st="R", p="Watching too many videos before bed are bad for your sleep.")
mk(2, 62, "E", [("keep → keeps", OKV("keep → keeps", "Walking to school every day")), ("Walking → Walk", BAD("Walking → Walk", "주어 자리에는 동사원형을 쓸 수 없다.")),
                ("every day → everyday", BAD("every day → everyday", "‘매일’이라는 부사는 every day로 띄어 쓴다.")), ("me → my", BAD("me → my", "keep의 목적어 자리에는 목적격을 쓴다.")),
                ("healthy → healthily", BAD("healthy → healthily", "keep + 목적어 뒤 목적격 보어 자리에는 형용사를 쓴다."))], 1, R62, S62,
   st="R", p="Walking to school every day keep me healthy.")
mk(2, 62, "F", [("Cooking → Cooked", BAD("Cooking → Cooked", "주어 자리에는 동명사를 쓴다.")), ("meals → meal", BAD("meals → meal", "셀 수 있는 명사를 관사 없이 단수로 쓸 수 없다.")),
                ("are → is", OKV("are → is", "Cooking meals for my family")), ("one → ones", BAD("one → ones", "‘~ 중 하나’는 one of를 쓴다.")),
                ("hobbies → hobby", BAD("hobbies → hobby", "one of 뒤에는 복수명사를 쓴다."))], 3, R62, S62,
   st="R", p="Cooking meals for my family are one of my hobbies.")

# 2-63 동명사 vs 현재분사: 동명사 오답 네 문장을 유형마다 새로
R63 = "동명사는 동사에 -ing을 붙여 명사 역할(주어·보어·동사나 전치사의 목적어)을 한다. be동사와 함께 진행형을 만드는 -ing은 현재분사이다."
S63 = "동명사 오답 네 문장이 B와 똑같아서 유형마다 새로 썼다."
def GER(role): return f"동명사: {role}로 쓰였다. 나머지와 쓰임이 같으므로"
PROG = "현재분사: be동사와 함께 진행형을 만든다. 나머지 넷(동명사)과 쓰임이 다르므로"
mk(2, 63, "C", [("My hobby is <u>collecting</u> stamps.", GER("be동사 뒤 보어")), ("He gave up <u>eating</u> fast food.", GER("give up의 목적어")), ("<u>Riding</u> a bike is fun.", GER("문장의 주어")),
                ("She left without <u>saying</u> goodbye.", GER("전치사 without의 목적어")), ("Tom is <u>writing</u> an email.", PROG)], 5, R63, S63)
mk(2, 63, "D", [("I don't mind <u>waiting</u> here.", GER("mind의 목적어")), ("We talked about <u>moving</u> to Busan.", GER("전치사 about의 목적어")), ("The children are <u>playing</u> outside.", PROG),
                ("<u>Keeping</u> a diary is a good habit.", GER("문장의 주어")), ("She is proud of <u>being</u> a nurse.", GER("전치사 of의 목적어"))], 3, R63, S63)
mk(2, 63, "E", [("Jane was <u>waiting</u> for the bus.", PROG), ("Would you mind <u>closing</u> the door?", GER("mind의 목적어")), ("<u>Exercising</u> regularly keeps you fit.", GER("문장의 주어")),
                ("I'm afraid of <u>making</u> mistakes.", GER("전치사 of의 목적어")), ("They practiced <u>singing</u> for the concert.", GER("practice의 목적어"))], 1, R63, S63)
mk(2, 63, "F", [("He is interested in <u>learning</u> Spanish.", GER("전치사 in의 목적어")), ("<u>Taking</u> a walk after dinner is relaxing.", GER("문장의 주어")), ("She kept <u>talking</u> during the movie.", GER("keep의 목적어")),
                ("I'm tired of <u>hearing</u> the same song.", GER("전치사 of의 목적어")), ("We are <u>watching</u> a movie.", PROG)], 5, R63, S63)

# 2-64 전치사 뒤 동명사: 원문항 발문·밑줄, 짝 문장 없애고 오답을 유형마다 새로
R64 = "전치사 뒤에는 명사나 동명사를 쓰며 동사원형이나 to부정사를 쓰지 않는다. look forward to·be used to의 to도 전치사이므로 뒤에 동명사를 쓴다."
S64 = "발문이 ‘전치사 뒤의 동사 형태’라고 평가 요소를 알려 주었고 밑줄이 없었으며, 옳은 문장이 같은 내용의 틀린 문장과 짝을 이루고(insisted on to pay ↔ insisted on paying 등) 오답 네 문장이 유형마다 같았다. 원문항 발문과 밑줄로 되돌리고, 짝 문장을 없애 오답을 유형마다 새로 썼다."
def PX(prep, ger): return f"전치사({prep}) 뒤에는 동명사({ger})를 써야 한다. 어법상 틀렸으므로"
def PO(prep, ger): return f"전치사({prep}) 뒤에 동명사({ger})를 바르게 썼으므로"
mk(2, 64, "B", [("He is good at <u>fix</u> computers.", PX("at", "fixing")), ("Mina is nervous about <u>give</u> a speech.", PX("about", "giving")), ("I'm bad at <u>remember</u> names.", PX("at", "remembering")),
                ("I'm thinking of <u>to change</u> my hairstyle.", PX("of", "changing")), ("She insisted on <u>paying</u> for dinner.", PO("on", "paying"))], 5, R64, S64, st="R")
mk(2, 64, "C", [("He is afraid of <u>fly</u>.", PX("of", "flying")), ("Thank you for <u>invite</u> me.", PX("for", "inviting")), ("She left without <u>to say</u> a word.", PX("without", "saying")),
                ("Tom succeeded in <u>solving</u> the puzzle.", PO("in", "solving")), ("I'm used to <u>get</u> up early.", PX("to", "getting"))], 4, R64, S64, st="R")
mk(2, 64, "D", [("We talked about <u>go</u> camping.", PX("about", "going")), ("We are interested in <u>learning</u> French.", PO("in", "learning")), ("He is proud of <u>win</u> the game.", PX("of", "winning")),
                ("I'm sorry for <u>to call</u> so late.", PX("for", "calling")), ("They are excited about <u>visit</u> Jeju.", PX("about", "visiting"))], 2, R64, S64, st="R")
mk(2, 64, "E", [("He left the room without <u>close</u> the door.", PX("without", "closing")), ("How about <u>to take</u> a taxi?", PX("about", "taking")), ("Jane apologized for <u>being</u> late.", PO("for", "being")),
                ("I'm worried about <u>lose</u> my job.", PX("about", "losing")), ("She is fond of <u>to read</u> poems.", PX("of", "reading"))], 3, R64, S64, st="R")
mk(2, 64, "F", [("He kept me from <u>making</u> a mistake.", PO("from", "making")), ("Instead of <u>take</u> the bus, we walked.", PX("of", "taking")), ("I dream of <u>to become</u> a pilot.", PX("of", "becoming")),
                ("She is capable of <u>run</u> a marathon.", PX("of", "running")), ("Before <u>eat</u>, wash your hands.", PX("before", "eating"))], 1, R64, S64, st="R")

# 2-65 틀린 문장 개수: 원문항처럼 여섯 문장, 2개~6개 보기
R65 = "deny·avoid·finish·enjoy·admit·keep·give up·mind·practice 등은 동명사를 목적어로 쓰고, 전치사(look forward to·be used to·object to의 to 포함) 뒤에도 동명사를 쓴다. be worth -ing, cannot help -ing, be busy -ing, spend + 시간 + -ing, feel like -ing도 동명사를 쓴다."
CNT26 = ["2개", "3개", "4개", "5개", "6개"]
def f65(t, lines, judge, wrong, s):
    n = len(wrong.split(","))
    F(2, 65, t, p="\n".join(lines), c=CNT26, a=n - 1, r=R65, pre=["문장별 판정: " + j for j in judge], k=f"어법상 틀린 문장은 {wrong}로 {n}개이다.", n="cnt", s=s + f" 정답 위치 {'①②③④⑤'[n-2]}.")
S65 = "보기 문장이 원문항(6개)보다 적은 5개였고 개수 선택지의 범위·순서가 원문항과 달랐다. 원문항처럼 문장을 여섯 개로 하고 선택지를 2개~6개 순으로 맞췄으며, 문장마다 줄을 바꿨다."
S65z = S65 + " 틀린 문장이 하나도 없어 원문항과 인지 과정이 달랐던 것을, 틀린 문장을 넣어 원문항처럼 오류를 판별하게 했다."
f65("B", ["ⓐ This old chair is worth repairing.", "ⓑ I cannot help to laugh at that scene.", "ⓒ Jane denied taking the money.", "ⓓ Tom is looking forward to meet you.", "ⓔ We spent the afternoon talking.", "ⓕ She finished writing the report."],
    ["ⓐ O. be worth -ing이다.", "ⓑ X. cannot help 뒤에는 동명사를 쓴다. 교정문: I cannot help laughing at that scene.", "ⓒ O. deny는 동명사를 목적어로 쓴다.",
     "ⓓ X. look forward to의 to는 전치사라 동명사를 쓴다. 교정문: Tom is looking forward to meeting you.", "ⓔ O. spend + 시간 + -ing이다.", "ⓕ O. finish는 동명사를 목적어로 쓴다."], "ⓑ, ⓓ", S65)
f65("C", ["ⓐ The book is worth to read again.", "ⓑ She avoided answering the question.", "ⓒ We finished to clean the room.", "ⓓ I object to pay extra.", "ⓔ Tom kept working.", "ⓕ He gave up to smoke."],
    ["ⓐ X. be worth 뒤에는 동명사를 쓴다. 교정문: The book is worth reading again.", "ⓑ O. avoid는 동명사를 목적어로 쓴다.", "ⓒ X. finish는 동명사를 목적어로 쓴다. 교정문: We finished cleaning the room.",
     "ⓓ X. object to의 to는 전치사라 동명사를 쓴다. 교정문: I object to paying extra.", "ⓔ O. keep은 동명사를 목적어로 쓴다.", "ⓕ X. give up은 동명사를 목적어로 쓴다. 교정문: He gave up smoking."], "ⓐ, ⓒ, ⓓ, ⓕ", S65z)
f65("D", ["ⓐ I cannot help laughing.", "ⓑ Jane admitted to break the vase.", "ⓒ The movie is worth to watch.", "ⓓ We are used to get up early.", "ⓔ He gave up smoke.", "ⓕ Would you mind to open the door?"],
    ["ⓐ O. cannot help -ing이다.", "ⓑ X. admit는 동명사를 목적어로 쓴다(admit to는 전치사 to + 동명사). 교정문: Jane admitted breaking the vase.", "ⓒ X. be worth 뒤에는 동명사를 쓴다. 교정문: The movie is worth watching.",
     "ⓓ X. be used to의 to는 전치사라 동명사를 쓴다. 교정문: We are used to getting up early.", "ⓔ X. give up은 동명사를 목적어로 쓴다. 교정문: He gave up smoking.", "ⓕ X. mind는 동명사를 목적어로 쓴다. 교정문: Would you mind opening the door?"],
    "ⓑ, ⓒ, ⓓ, ⓔ, ⓕ", S65 + " 다른 유형과 겹치지 않게 틀린 문장을 5개로 했다.")
f65("E", ["ⓐ Tom enjoys to cook.", "ⓑ She is busy preparing dinner.", "ⓒ We prevented him from leave.", "ⓓ I feel like to take a walk.", "ⓔ The problem needs solving.", "ⓕ They practiced to dance for hours."],
    ["ⓐ X. enjoy는 동명사를 목적어로 쓴다. 교정문: Tom enjoys cooking.", "ⓑ O. be busy -ing이다.", "ⓒ X. 전치사(from) 뒤에는 동명사를 쓴다. 교정문: We prevented him from leaving.",
     "ⓓ X. feel like 뒤에는 동명사를 쓴다. 교정문: I feel like taking a walk.", "ⓔ O. need -ing은 ‘~될 필요가 있다’는 수동의 뜻이다.", "ⓕ X. practice는 동명사를 목적어로 쓴다. 교정문: They practiced dancing for hours."], "ⓐ, ⓒ, ⓓ, ⓕ", S65z + " 정답 개수가 원문항(3개)과 같지 않게 틀린 문장을 넷으로 했다.")
f65("F", ["ⓐ Jane denied to cheat.", "ⓑ I am looking forward to seeing you.", "ⓒ Tom stopped smoking because it was unhealthy.", "ⓓ She succeeded in passing.", "ⓔ We cannot help smiling at the baby.", "ⓕ He suggested to go on a picnic."],
    ["ⓐ X. deny는 동명사를 목적어로 쓴다. 교정문: Jane denied cheating.", "ⓑ O. look forward to + 동명사이다.", "ⓒ O. stop -ing은 ‘~하던 것을 그만두다’이다.",
     "ⓓ O. 전치사(in) 뒤 동명사이다.", "ⓔ O. cannot help -ing이다.", "ⓕ X. suggest는 동명사를 목적어로 쓴다. 교정문: He suggested going on a picnic."], "ⓐ, ⓕ", S65z)

# 2-69 remember -ing / to-V: 답을 알려 주던 발문 설명 삭제, 문맥으로 과거·미래가 드러나게
ST69 = "다음 문장의 빈칸 (A)와 (B)에 들어갈 말이 바르게 연결된 것은?"
XR69 = ("지정된 의미에", "문맥의 의미에")
S69 = "발문이 ‘(A)는 이미 한 행동, (B)는 앞으로 할 행동’이라고 답을 알려 주어 원문항 발문으로 되돌렸다."
F(2, 69, "B", st=ST69, xr=[XR69], p="I clearly remember (A)________ the door last night, but please remember (B)________ it again tonight.", s=S69 + " (A)에 ‘last night’를 넣어 이미 한 일임이 문맥으로 드러나게 했다.")
F(2, 69, "C", st=ST69, xr=[XR69], s=S69 + " (A)의 ‘years ago’, (B)의 ‘today’로 과거·미래가 문맥에 드러나 있다.")
F(2, 69, "D", st=ST69, xr=[XR69], p="I remember (A)________ this museum as a child. Remember (B)________ tickets online before you go.", s=S69 + " (B)에 ‘before you go’를 넣어 앞으로 할 일임이 문맥으로 드러나게 했다.")
F(2, 69, "E", st=ST69, p="Tom remembers (A)________ the email yesterday. He must remember (B)________ the file next time.",
  xr=[XR69] + ([("the attachment", "the file")] if "the attachment" in V(2, 69, "E")["expl"] else []), s=S69 + " (A)에 ‘yesterday’를 넣어 이미 한 일임이 문맥으로 드러나게 했다.")
F(2, 69, "F", st=ST69, xr=[XR69], s=S69 + " (A)의 ‘before’, (B)의 ‘when you leave’로 과거·미래가 문맥에 드러나 있다.")

# 2-70 틀린 문장 개수: 원문항처럼 1개~5개 보기, 뜻이 모호한 문장 교체
R70 = "remember·forget·regret·stop은 -ing(이미 한 일)과 to부정사(앞으로 할 일, 목적)에 따라 뜻이 달라진다. try -ing은 시험 삼아 해 봄, try to-V는 하려고 애씀이다. be worth·It is no use(good) 뒤에는 동명사를, 전치사 뒤에도 동명사를 쓴다."
CNT15 = ["1개", "2개", "3개", "4개", "5개"]
def f70(t, lines, judge, wrong, s):
    n = len(wrong.split(","))
    F(2, 70, t, p="<보기>\n" + "\n".join(lines), c=CNT15, a=n, r=R70, pre=["문장별 판정: " + j for j in judge], k=f"어법상 올바르지 않은 문장은 {wrong}로 {n}개이다.", n="cnt", s=s + f" 정답 위치 {'①②③④⑤'[n-1]}.")
S70 = "개수 선택지 순서가 뒤섞여 원문항처럼 1개~5개 순으로 맞췄고, 문장마다 줄을 바꿨다."
f70("B", ["ⓐ I regret to tell you that the event is canceled.", "ⓑ It is no use complain now.", "ⓒ Jane stopped smoking last year.", "ⓓ Tom forgot to lock the door, so he went back to lock it.", "ⓔ We look forward to meet you."],
    ["ⓐ O. regret to-V는 ‘유감스럽게도 ~하다’이다.", "ⓑ X. It is no use 뒤에는 동명사를 쓴다. 교정문: It is no use complaining now.", "ⓒ O. stop -ing은 ‘~하던 것을 그만두다’이다.",
     "ⓓ O. forget to-V는 ‘해야 할 일을 잊다’이다.", "ⓔ X. look forward to의 to는 전치사라 동명사를 쓴다. 교정문: We look forward to meeting you."], "ⓑ, ⓔ",
    "‘Tom forgot locking the door, so he went back to check’가 옳게도 틀리게도 읽혀 정답 시비가 생길 수 있어 뜻이 분명한 ‘forgot to lock … went back to lock it’으로 바꿨다. 틀린 문장이 없어 원문항과 인지 과정이 달랐던 것을 ⓑ·ⓔ를 틀린 문장으로 바꿔 오류를 판별하게 했다. " + S70)
f70("C", ["ⓐ She remembered to send the file before leaving.", "ⓑ I tried restarting the computer, but it didn't work.", "ⓒ Tom stopped drink coffee because it was bad for him.", "ⓓ It is worth visiting the museum.", "ⓔ Jane admitted making a mistake."],
    ["ⓐ O. remember to-V는 ‘잊지 않고 ~하다’이다.", "ⓑ O. try -ing은 ‘시험 삼아 해 보다’이다.", "ⓒ X. stop 뒤에는 동명사(또는 목적의 to부정사)를 쓴다. 교정문: Tom stopped drinking coffee because it was bad for him.",
     "ⓓ O. be worth -ing이다.", "ⓔ O. admit는 동명사를 목적어로 쓴다."], "ⓒ", S70)
f70("D", ["ⓐ I forgot meeting him before, but he remembered me.", "ⓑ She stopped talk when the teacher entered.", "ⓒ We regret to inform you that your application failed.", "ⓓ He is used to work late.", "ⓔ They avoided to answer."],
    ["ⓐ O. forget -ing은 ‘이미 한 일을 잊다’이다.", "ⓑ X. stop 뒤에는 동명사를 쓴다. 교정문: She stopped talking when the teacher entered.", "ⓒ O. 유감스러운 소식을 전할 때는 regret to inform을 쓴다.",
     "ⓓ X. be used to의 to는 전치사라 동명사를 쓴다. 교정문: He is used to working late.", "ⓔ X. avoid는 동명사를 목적어로 쓴다. 교정문: They avoided answering."], "ⓑ, ⓓ, ⓔ",
    "해설은 ⓒ ‘We regret informing you that your application failed’를 옳다고 보았으나, 불합격 통보 문맥에서는 regret to inform이 맞아 정답이 흔들렸다. ⓒ를 ‘regret to inform’으로 바로잡고, ⓑ·ⓓ를 틀린 문장으로 바꿔 오류가 3개가 되게 했다. " + S70)
f70("E", ["ⓐ Tom remembered call Mina yesterday.", "ⓑ I tried opening the window to cool the room.", "ⓒ Jane stopped to rest for ten minutes.", "ⓓ It is no good argue with him.", "ⓔ We are looking forward to see you."],
    ["ⓐ X. 이미 한 일을 기억할 때는 remember -ing을 쓴다. 교정문: Tom remembered calling Mina yesterday.", "ⓑ O. try -ing은 ‘시험 삼아 ~해 보다’이다.",
     "ⓒ O. stop to-V는 ‘~하기 위해 멈추다’이다.", "ⓓ X. It is no good 뒤에는 동명사를 쓴다. 교정문: It is no good arguing with him.", "ⓔ X. look forward to의 to는 전치사라 동명사를 쓴다. 교정문: We are looking forward to seeing you."],
    "ⓐ, ⓓ, ⓔ", S70 + " ⓐ·ⓔ를 틀린 문장으로 바꿔 오류를 3개로 했다(원문항의 정답 4개와 겹치지 않게).")
f70("F", ["ⓐ She regrets saying those words.", "ⓑ I forgot to turn off the oven.", "ⓒ Tom stopped playing soccer because of his injury.", "ⓓ We tried to use a different key, but the door stayed locked.", "ⓔ It is worth to read twice."],
    ["ⓐ O. regret -ing은 ‘이미 한 일을 후회하다’이다.", "ⓑ O. forget to-V는 ‘해야 할 일을 잊다’이다.", "ⓒ O. stop -ing은 ‘~하던 것을 그만두다’이다.",
     "ⓓ O. try to-V는 ‘~하려고 애쓰다’이다.", "ⓔ X. be worth 뒤에는 동명사를 쓴다. 교정문: It is worth reading twice."], "ⓔ", S70)
