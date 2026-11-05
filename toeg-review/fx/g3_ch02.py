# 3급 CH2 일반동사 (11~20) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]

# 3-11 B: 원문항과 같던 제시문을 새로
R11 = "일반동사의 과거 부정문은 did not(didn't) + 동사원형으로 만든다. don't/doesn't는 현재, was(n't)는 be동사 문장에 쓴다."
mk(3, 11, "B", [("Mina didn't cleaned her room.", "didn't 뒤에는 동사원형(clean)을 써야 하므로"), ("Mina doesn't clean her room.", "doesn't는 현재 부정이라 과거 문장과 시제가 맞지 않으므로"),
                ("Mina didn't clean her room.", "didn't + 동사원형으로 바르게 바꿨으므로"), ("Mina wasn't clean her room.", "일반동사 문장에는 wasn't를 쓰지 않으므로"), ("Mina not cleaned her room.", "not만 넣어서는 부정문이 되지 않으므로")], 3, R11,
   "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘Mina cleaned her room.’으로 바꿨다.", p="Mina cleaned her room.")

# 3-12 현재 의문문: 원문항 발문, B는 제시문을 새로
S12 = "발문이 ‘do 또는 does로 시작하는 기본 yes/no 의문문’이라고 만드는 방법을 알려 주어 원문항 발문(현재 의문문으로 올바르게 바꾼 것)으로 되돌렸다."
R12 = "현재 일반동사 의문문은 Do/Does + 주어 + 동사원형으로 만든다. 3인칭 단수 주어에는 Does를 쓰고, 본동사에는 -s를 붙이지 않는다."
mk(3, 12, "B", [("Is she walk to school?", "일반동사 문장에는 be동사로 의문문을 만들지 않으므로"), ("Does she walking to school?", "Does 뒤에는 -ing가 아니라 동사원형(walk)을 쓰므로"), ("Do she walk to school?", "3인칭 단수 주어(she)에는 Does를 쓰므로"),
                ("Does she walks to school?", "Does 뒤 본동사는 동사원형(walk)이므로"), ("Does she walk to school?", "Does + 주어 + 동사원형으로 바르게 바꿨으므로")], 5, R12,
   S12 + " 제시문이 원문항과 똑같아 ‘She walks to school.’로 바꿨다.", st="R", p="She walks to school.")
S12b = S12 + " 영어에 없는 형태이거나 동사와 관계없는 명사 복수형 오답({})은 원문항의 오답처럼 동사 형태 오답으로 바꿨다."
BEQ = "일반동사 문장에는 be동사로 의문문을 만들지 않으므로"
mk(3, 12, "C", [("Does Jane study English?", "Does + 주어 + 동사원형으로 바르게 바꿨으므로"), ("Does Jane studies English?", "Does 뒤 본동사는 동사원형(study)이므로"), ("Do Jane study English?", "3인칭 단수 주어(Jane)에는 Does를 쓰므로"),
                ("Is Jane study English?", BEQ), ("Does Jane studying English?", "Does 뒤에는 -ing가 아니라 동사원형(study)을 쓰므로")], 1, R12, S12b.format("Englishs"), st="R")
mk(3, 12, "D", [("Do they watching TV?", "Do 뒤에는 -ing가 아니라 동사원형(watch)을 쓰므로"), ("Does they watch TV?", "복수 주어(they)에는 Do를 쓰므로"), ("Do they watch TV?", "Do + 주어 + 동사원형으로 바르게 바꿨으므로"),
                ("Are they watch TV?", BEQ), ("Do they watches TV?", "Do 뒤 본동사는 동사원형(watch)이므로")], 3, R12, S12b.format("TVs"), st="R")
mk(3, 12, "E", [("Do you likes music?", "Do 뒤 본동사는 동사원형(like)이므로"), ("Do you liking music?", "Do 뒤에는 -ing가 아니라 동사원형(like)을 쓰므로"), ("Does you like music?", "주어 you에는 Do를 쓰므로"),
                ("Do you like music?", "Do + 주어 + 동사원형으로 바르게 바꿨으므로"), ("Are you like music?", BEQ)], 4, R12, S12b.format("musics"), st="R")
mk(3, 12, "F", [("Does Tom going to school?", "Does 뒤에는 -ing가 아니라 동사원형(go)을 쓰므로"), ("Does Tom go to school?", "Does + 주어 + 동사원형으로 바르게 바꿨으므로"), ("Is Tom go to school?", BEQ),
                ("Do Tom go to school?", "3인칭 단수 주어(Tom)에는 Does를 쓰므로"), ("Does Tom goes to school?", "Does 뒤 본동사는 동사원형(go)이므로")], 2, R12, S12b.format("schools"), st="R")

# 3-13 불규칙 과거형 오류: B는 문장·오류 동사를 새로, C·E·F는 짝 문장 교체, D는 발문 복원
ST13 = "다음 중 밑줄 친 부분이 어법상 틀린 것을 고르시오."
R13 = "불규칙동사는 -ed를 붙이지 않고 정해진 과거형을 쓴다(go-went, see-saw, write-wrote, buy-bought, catch-caught)."
def OK(v, base): return f"{v}: {base}의 과거형을 바르게 썼으므로"
def BAD(v, base, right): return f"{v}: {base}의 과거형은 {right}이다. 어법상 틀린 부분이므로"
S13 = "틀린 과거형이 같은 동사의 옳은 과거형 문장과 짝을 이뤄 대비 단서가 되었다. 짝이 되는 옳은 문장을 다른 동사로 바꾸고 발문을 원문항과 같게 했다."
mk(3, 13, "B", [("We <u>swam</u> in the river.", OK("swam", "swim")), ("She <u>brought</u> her lunch.", OK("brought", "bring")), ("He <u>catched</u> the ball.", BAD("catched", "catch", "caught")),
                ("They <u>sang</u> together.", OK("sang", "sing")), ("I <u>found</u> my keys.", OK("found", "find"))], 3, R13,
   "다섯 문장이 원문항 문장을 줄인 것이었고 오류(eated)도 같았다. 문장과 오류 동사(catched)를 새로 쓰고 발문을 원문항과 같게 했다.", st=ST13)
mk(3, 13, "C", [("They <u>ate</u> lunch.", OK("ate", "eat")), ("He <u>ran</u> fast.", OK("ran", "run")), ("She <u>goed</u> home early.", BAD("goed", "go", "went")),
                ("She <u>bought</u> a bag.", OK("bought", "buy")), ("We <u>saw</u> a movie.", OK("saw", "see"))], 3, R13, S13 + " (went 문장 → ran 문장)", st=ST13)
F(3, 13, "D", st=ST13, s="발문이 원문항과 달라(‘밑줄 친 동사의 과거형이 틀린 것’) 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
mk(3, 13, "E", [("We <u>went</u> home.", OK("went", "go")), ("Jane <u>ate</u> lunch.", OK("ate", "eat")), ("Tom <u>wrote</u> a letter.", OK("wrote", "write")),
                ("They <u>met</u> a friend.", OK("met", "meet")), ("They <u>seed</u> the movie.", BAD("seed", "see", "saw"))], 5, R13, S13 + " (saw 문장 → met 문장)", st=ST13)
mk(3, 13, "F", [("Jane <u>writed</u> a letter.", BAD("writed", "write", "wrote")), ("I <u>made</u> dinner.", OK("made", "make")), ("Tom <u>bought</u> a bike.", OK("bought", "buy")),
                ("Jane <u>told</u> a story.", OK("told", "tell")), ("They <u>came</u> early.", OK("came", "come"))], 1, R13, S13 + " (wrote 문장 → told 문장)", st=ST13)

# 3-14 과거형 묶음: 원문항 발문, 유형마다 동사 묶음을 새로
ST14 = "다음 동사의 과거형이 모두 올바른 것을 고르시오."
R14 = "불규칙동사는 -ed를 붙이지 않고 정해진 과거형을 쓴다. 규칙동사(help, smell, dream 등)는 -ed를 붙이고, cut·put·hit·cost처럼 원형과 과거형이 같은 동사도 있다."
S14 = "오답 네 개가 원문항의 오답 묶음을 그대로 썼고, 정답은 원문항 오답 하나를 바로잡은 것이라 원문항을 본 학생은 바로 고를 수 있었으며, 발문에 fly·leave의 뜻을 덧붙였다. 원문항 발문으로 되돌리고 유형마다 동사 묶음을 새로 구성했다."
def B14(wrong, right): return f"{wrong}이 틀렸다(바른 과거형 {right}). 따라서"
OKB = "세 동사의 과거형이 모두 알맞으므로"
mk(3, 14, "B", [("hold - held / keep - keeped / feel - felt", B14("keep - keeped", "kept")), ("sit - sat / win - won / sell - sold", OKB), ("sing - sang / drive - drived / ride - rode", B14("drive - drived", "drove")),
                ("lose - losed / send - sent / spend - spent", B14("lose - losed", "lost")), ("wear - wore / tell - told / hear - heared", B14("hear - heared", "heard"))], 2, R14, S14, st=ST14, okdup=True)
mk(3, 14, "C", [("draw - drawed / know - knew / throw - threw", B14("draw - drawed", "drew")), ("meet - met / feed - feeded / lead - led", B14("feed - feeded", "fed")), ("think - thought / fight - fought / teach - teached", B14("teach - teached", "taught")),
                ("choose - chose / freeze - froze / steal - stole", OKB), ("shut - shutted / cut - cut / put - put", B14("shut - shutted", "shut"))], 4, R14, S14, st=ST14, okdup=True)
mk(3, 14, "D", [("stand - stood / understand - understood / sell - selled", B14("sell - selled", "sold")), ("pay - payed / say - said / lay - laid", B14("pay - payed", "paid")), ("blow - blew / grow - grew / know - knew", OKB),
                ("get - got / forget - forgetted / shoot - shot", B14("forget - forgetted", "forgot")), ("drink - drank / sink - sinked / ring - rang", B14("sink - sinked", "sank"))], 3, R14, S14, st=ST14, okdup=True)
mk(3, 14, "E", [("hit - hit / hurt - hurted / cost - cost", B14("hurt - hurted", "hurt")), ("lend - lended / bend - bent / spend - spent", B14("lend - lended", "lent")), ("feel - felt / smell - smelled / sleep - sleeped", B14("sleep - sleeped", "slept")),
                ("bite - bit / hide - hid / slide - slided", B14("slide - slided", "slid")), ("mean - meant / deal - dealt / dream - dreamed", OKB)], 5, R14, S14, st=ST14, okdup=True)
mk(3, 14, "F", [("become - became / come - came / overcome - overcame", OKB), ("make - maked / shake - shook / take - took", B14("make - maked", "made")), ("rise - rose / arise - arose / raise - rose", B14("raise - rose", "raised")),
                ("beat - beat / eat - eated / seat - seated", B14("eat - eated", "ate")), ("mistake - mistook / forgive - forgave / understand - understanded", B14("understand - understanded", "understood"))], 1, R14, S14, st=ST14, okdup=True)

# 3-15 옳은 문장 개수: 원문항 형식(ⓐ~ⓔ, 줄바꿈, 밑줄, 1개~5개)
ST15 = "다음 중 밑줄 친 부분이 어법상 옳은 문장의 개수를 고르시오."
R15 = "현재 평서문에서 3인칭 단수 주어에는 동사에 -(e)s를 붙인다. do/does/did 뒤에는 동사원형을 쓰고, 3인칭 단수 주어의 부정·의문에는 does를 쓴다."
S15 = "원문항의 밑줄이 없고, 보기 기호 ⓐ~ⓔ가 a~e로 바뀌어 한 줄로 이어졌으며 개수 선택지 순서가 뒤섞였다. 원문항 발문과 형식(ⓐ~ⓔ, 줄바꿈, 밑줄, 1개~5개)으로 되돌렸다."
def f15(t, lines, judge, ok, s=S15):
    n = len(ok.split(","))
    F(3, 15, t, st=ST15, p="\n".join(lines), c=CNT5, a=n, r=R15, pre=["문장별 판정: " + j for j in judge], k=f"밑줄 친 부분이 옳은 문장은 {ok}로 {n}개이다.", n="cnt", s=s + ipos(n))
f15("B", ["ⓐ My dad <u>washes</u> his car every Sunday.", "ⓑ They <u>doesn't</u> eat meat.", "ⓒ <u>Did</u> she <u>call</u> you last night?", "ⓓ The baby <u>cry</u> at night.", "ⓔ Tom <u>didn't went</u> to the gym."],
    ["ⓐ O. 3인칭 단수 주어에 washes를 썼다.", "ⓑ X. 복수 주어(They)의 부정은 don't이다.", "ⓒ O. Did + 주어 + 동사원형이다.", "ⓓ X. 3인칭 단수 주어(The baby)에는 cries를 쓴다.", "ⓔ X. didn't 뒤에는 동사원형(go)을 쓴다."],
    "ⓐ, ⓒ", "다섯 문장이 원문항을 줄인 것이었고 정답 개수(3개)도 같았으며, 기호·밑줄·선택지 순서도 원본과 달랐다. 문장을 새로 쓰고 원문항 형식으로 되돌렸으며 정답 개수를 2개로 바꿨다.")
f15("C", ["ⓐ Jane <u>studies</u> English.", "ⓑ They <u>doesn't play</u> soccer.", "ⓒ <u>Does</u> Tom <u>likes</u> milk?", "ⓓ We <u>watch</u> TV.", "ⓔ He <u>don't read</u> books."],
    ["ⓐ O. 3인칭 단수 주어에 studies를 썼다.", "ⓑ X. 복수 주어(They)의 부정은 don't이다.", "ⓒ X. Does 뒤에는 동사원형(like)을 쓴다.", "ⓓ O. 복수 주어에 watch를 썼다.", "ⓔ X. 3인칭 단수 주어(He)의 부정은 doesn't이다."], "ⓐ, ⓓ", S15 + " 정답 개수·위치(3개, ③)가 원문항과 같지 않게 ⓑ를 틀린 문장으로 바꿨다.")
f15("D", ["ⓐ Tom <u>went</u> home.", "ⓑ She <u>didn't buy</u> it.", "ⓒ <u>Did</u> they <u>go</u> out?", "ⓓ We <u>saw</u> a movie.", "ⓔ Jane <u>didn't ate</u>."],
    ["ⓐ O. go의 과거형 went를 썼다.", "ⓑ O. didn't + 동사원형이다.", "ⓒ O. Did + 주어 + 동사원형이다.", "ⓓ O. see의 과거형 saw를 썼다.", "ⓔ X. didn't 뒤에는 동사원형(eat)을 쓴다."], "ⓐ, ⓑ, ⓒ, ⓓ", S15 + " 정답 개수·위치(3개, ③)가 원문항과 같지 않게 ⓒ를 옳은 문장으로 바꿨다.")
f15("E", ["ⓐ I <u>read</u> every day.", "ⓑ He <u>doesn't study</u> much.", "ⓒ <u>Do</u> she <u>play</u> tennis?", "ⓓ They <u>work</u> here.", "ⓔ Tom <u>goes</u> home early."],
    ["ⓐ O. 주어 I에 동사원형 read를 썼다.", "ⓑ O. doesn't + 동사원형이다.", "ⓒ X. 3인칭 단수 주어(she)에는 Does를 쓴다.", "ⓓ O. 복수 주어에 work를 썼다.", "ⓔ O. 3인칭 단수 주어에 goes를 썼다."], "ⓐ, ⓑ, ⓓ, ⓔ")
f15("F", ["ⓐ We <u>ate</u> lunch.", "ⓑ She <u>didn't see</u> him.", "ⓒ <u>Did</u> Tom <u>write</u> a letter?", "ⓓ They <u>goed</u> home.", "ⓔ I <u>made</u> dinner."],
    ["ⓐ O. eat의 과거형 ate를 썼다.", "ⓑ O. didn't + 동사원형이다.", "ⓒ O. Did + 주어 + 동사원형이다.", "ⓓ X. go의 과거형은 went이다.", "ⓔ O. make의 과거형 made를 썼다."], "ⓐ, ⓑ, ⓒ, ⓔ")

# 3-16 do/does 뒤 동사원형: 밑줄 복원, 오류 위치를 유형마다 다르게
ST16 = "다음 문장에서 어법상 틀린 부분을 고르시오."
R16 = "현재 일반동사의 의문문·부정문은 do/does + 동사원형으로 만든다. 3인칭 단수 주어에는 does, 그 밖의 주어에는 do를 쓰고, 본동사에는 -s를 붙이지 않는다."
def f16(t, pre, parts, post, notes, a, s):
    p = pre + " ".join(f"{'①②③④⑤'[i]}<u>{x}</u>" for i, x in enumerate(parts)) + post
    mk(3, 16, t, list(zip(parts, notes)), a, R16, s, st=ST16, p=p)
S16 = "원문항의 밑줄이 없어 밑줄을 넣었다."
f16("B", "Tom ", ["doesn't", "likes", "music", "very", "much"], ".", ["doesn't: 3인칭 단수 주어의 부정에 알맞으므로", "likes: doesn't 뒤에는 동사원형(like)을 써야 한다. 틀린 부분이므로", "music: 동사의 목적어로 알맞으므로", "very: much를 꾸미는 부사로 알맞으므로", "much: ‘매우’라는 부사로 알맞으므로"], 2, S16)
f16("C", "Jane ", ["doesn't", "studies", "English", "every", "day"], ".", ["doesn't: 3인칭 단수 주어의 부정에 알맞으므로", "studies: doesn't 뒤에는 동사원형(study)을 써야 한다. 틀린 부분이므로", "English: 동사의 목적어로 알맞으므로", "every: 단수명사 앞의 every로 알맞으므로", "day: every 뒤 단수명사로 알맞으므로"], 2, S16)
f16("D", "", ["Do", "your sisters", "plays", "soccer", "after school"], "?", ["Do: 복수 주어(your sisters)의 의문문에 알맞으므로", "your sisters: 의문문의 주어로 알맞으므로", "plays: Do 뒤에는 동사원형(play)을 써야 한다. 틀린 부분이므로", "soccer: 동사의 목적어로 알맞으므로", "after school: 때를 나타내는 말로 알맞으므로"], 3,
    S16 + " 원문항과 B~F의 오류 위치가 모두 ②로 같아, 문장을 바꿔 오류 위치를 ③으로 옮겼다.")
f16("E", "", ["Does", "your brother", "often", "studies", "at night"], "?", ["Does: 3인칭 단수 주어(your brother)의 의문문에 알맞으므로", "your brother: 의문문의 주어로 알맞으므로", "often: 빈도부사로 동사 앞에 알맞으므로", "studies: Does 뒤에는 동사원형(study)을 써야 한다. 틀린 부분이므로", "at night: 때를 나타내는 말로 알맞으므로"], 4,
    S16 + " 원문항과 B~F의 오류 위치가 모두 ②로 같아, 문장을 바꿔 오류 위치를 ④로 옮겼다.")
f16("F", "", ["Does", "you", "watch", "TV", "at night"], "?", ["Does: 주어 you의 의문문에는 Do를 써야 한다. 틀린 부분이므로", "you: 의문문의 주어로 알맞으므로", "watch: 조동사 뒤 동사원형으로 알맞으므로", "TV: 동사의 목적어로 알맞으므로", "at night: 때를 나타내는 말로 알맞으므로"], 1,
    S16 + " 원문항과 B~F의 오류 위치가 모두 ②로 같아, 오류를 Do/Does 선택(①)으로 바꿨다.")

# 3-17 의문문 전환: 원문항 발문, 평서문 + 물음표 보기를 다른 오답으로, B는 제시문을 새로
ST17 = "다음 문장을 의문문으로 바꾼 것을 고르시오."
R17 = "현재 일반동사 의문문은 Do/Does + 주어 + 동사원형으로 만든다. 3인칭 단수 주어에는 Does를 쓰고, be동사나 did·과거형을 섞지 않는다."
S17 = "발문이 ‘do 또는 does로 시작하는 기본 yes/no 의문문’이라고 만드는 방법을 알려 주어 원문항 발문으로 되돌렸다. 조건이 없으면 평서문 어순 + 물음표 보기도 구어에서 쓰여 답이 흔들리므로 다른 오답으로 바꿨다."
OKQ = "Do/Does + 주어 + 동사원형으로 바르게 바꿨으므로"
mk(3, 17, "B", [("Does my parents drink coffee every morning?", "복수 주어(my parents)에는 Do를 쓰므로"), ("Are my parents drink coffee every morning?", "일반동사 문장에는 be동사로 의문문을 만들지 않으므로"),
                ("Do my parents drinks coffee every morning?", "Do 뒤에는 동사원형(drink)을 쓰므로"), ("Did my parents drank coffee every morning?", "현재 문장을 과거로 바꿨고, Did 뒤에도 동사원형을 쓰므로"),
                ("Do my parents drink coffee every morning?", OKQ)], 5, R17, S17 + " 제시문이 원문항과 똑같아 ‘My parents drink coffee every morning.’으로 바꿨다.", st=ST17, p="My parents drink coffee every morning.")
mk(3, 17, "C", [("Does Jane study English every day?", OKQ), ("Does Jane studies English every day?", "Does 뒤에는 동사원형(study)을 쓰므로"), ("Is Jane study English every day?", "일반동사 문장에는 be동사로 의문문을 만들지 않으므로"),
                ("Did Jane studied English every day?", "현재의 일이고 Did 뒤에도 동사원형을 써야 하므로"), ("Do Jane study English every day?", "3인칭 단수 주어(Jane)에는 Does를 쓰므로")], 1, R17, S17, st=ST17)
mk(3, 17, "D", [("Does Tom watches TV at night?", "Does 뒤에는 동사원형(watch)을 쓰므로"), ("Do Tom watch TV at night?", "3인칭 단수 주어(Tom)에는 Does를 쓰므로"), ("Does Tom watch TV at night?", OKQ),
                ("Is Tom watch TV at night?", "일반동사 문장에는 be동사로 의문문을 만들지 않으므로"), ("Did Tom watched TV at night?", "현재 문장을 과거로 바꿨고, Did 뒤에도 동사원형을 쓰므로")], 3, R17, S17, st=ST17)
mk(3, 17, "E", [("Does you like this song?", "주어 you에는 Do를 쓰므로"), ("Do you liked this song?", "Do 뒤에는 동사원형(like)을 쓰므로"), ("Are you like this song?", "일반동사 문장에는 be동사로 의문문을 만들지 않으므로"),
                ("Do you like this song?", OKQ), ("Do you likes this song?", "Do 뒤에는 동사원형(like)을 쓰므로")], 4, R17, S17, st=ST17)
mk(3, 17, "F", [("Does we need more time?", "주어 we에는 Do를 쓰므로"), ("Do we need more time?", OKQ), ("Do we needing more time?", "Do 뒤에는 -ing가 아니라 동사원형(need)을 쓰므로"),
                ("Are we need more time?", "일반동사 문장에는 be동사로 의문문을 만들지 않으므로"), ("Do we needs more time?", "Do 뒤에는 동사원형(need)을 쓰므로")], 2, R17, S17, st=ST17)

# 3-18 B: 원문항과 같던 제시문을 새로
R18 = "3인칭 단수 주어의 현재 부정문은 does not(doesn't) + 동사원형으로 만든다."
mk(3, 18, "B", [("She do not drink milk every morning.", "3인칭 단수 주어(She)에는 does not을 쓰므로"), ("She does not drinks milk every morning.", "does not 뒤에는 동사원형(drink)을 쓰므로"), ("She is not drink milk every morning.", "일반동사 문장에는 be동사로 부정문을 만들지 않으므로"),
                ("She not drinks milk every morning.", "not만 넣어서는 부정문이 되지 않으므로"), ("She does not drink milk every morning.", "does not + 동사원형으로 바르게 바꿨으므로")], 5, R18,
   "제시문과 정답이 원문항과 똑같았다. 제시문을 ‘She drinks milk every morning.’으로 바꿨다.", p="She drinks milk every morning.")

# 3-19 지문 설명 중 옳지 않은 것: 원문항 형식(ⓐ~ⓔ 밑줄), 반대되는 짝 설명 없애기
ST19 = "다음 <보기> 지문에 대한 설명으로 옳지 않은 것은?"
R19 = "불규칙동사는 -ed를 붙이지 않고 정해진 과거형을 쓰며, 과거형은 주어의 인칭·수에 따라 바뀌지 않는다. be동사의 과거형은 복수 주어에 were를 쓴다."
def f19(t, p, items, a, s):
    F(3, 19, t, st=ST19, p="<보기>\n" + p, c=[x for x, _ in items], a=a, r=R19,
      n=[w + (" 옳지 않은 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.") for i, (_, w) in enumerate(items)], k=items[a-1][1], s=s + ipos(a))
S19 = "보기 기호 ⓐ~ⓔ와 밑줄이 사라져 기호가 단어에 붙었고(예: ahad), 같은 밑줄에 대해 서로 반대되는 설명 두 개가 함께 있어 둘 중 하나가 답이라는 단서가 되었다. 원문항 발문과 형식(ⓐ~ⓔ 밑줄)으로 되돌리고, 반대되는 짝 설명을 없앴다."
f19("B", "Last Saturday, my friends and I ⓐ<u>went</u> to the beach. We ⓑ<u>swimmed</u> in the sea. My friend Mina ⓒ<u>brought</u> some snacks. We ⓓ<u>sat</u> on the sand and ⓔ<u>were</u> very happy.",
    [("ⓓ: sit의 과거형은 sitted이므로 ⓓ는 sitted로 써야 한다.", "sit의 과거형은 sat이므로 ⓓ는 알맞다."), ("ⓐ: go의 불규칙 과거형으로, 지난 토요일의 일을 나타낸다.", "went는 go의 과거형이다."),
     ("ⓑ: swim의 과거형은 swam이므로 ⓑ는 틀린 표현이다.", "swimmed는 swam으로 고쳐야 한다."), ("ⓒ: bring의 불규칙 과거형으로 ‘가져왔다’는 뜻이다.", "brought는 bring의 과거형이다."),
     ("ⓔ: 주어 We가 복수이므로 be동사의 과거형 were를 쓴 것은 알맞다.", "복수 주어의 과거는 were이다.")], 1,
    "지문과 틀린 설명(주어가 3인칭 단수이므로 makes)이 원문항과 같았고 보기 기호와 밑줄이 사라졌다. 지문과 설명을 새로 쓰고 원문항 발문과 형식으로 되돌렸다.")
f19("C", "Yesterday, Tom ⓐ<u>went</u> home. He ⓑ<u>buyed</u> a snack. His sister ⓒ<u>came</u> later. They ⓓ<u>ate</u> dinner and ⓔ<u>were</u> tired.",
    [("ⓒ: come의 불규칙 과거형이다.", "came은 come의 과거형이다."), ("ⓑ: buy의 과거형은 bought이므로 고쳐야 한다.", "buyed는 bought로 고쳐야 한다."), ("ⓔ: 주어 They에는 were가 맞다.", "복수 주어의 과거는 were이다."),
     ("ⓓ: eat의 과거형은 eated이다.", "eat의 과거형은 ate이므로 ⓓ는 알맞고, 이 설명이 틀렸다."), ("ⓐ: go의 불규칙 과거형이다.", "went는 go의 과거형이다.")], 4, S19)
F(3, 19, "D", st=ST19, p="<보기>\nLast night, Jane ⓐ<u>wrote</u> a letter. She ⓑ<u>goed</u> to bed late. Her parents ⓒ<u>were</u> asleep. She ⓓ<u>read</u> a book and ⓔ<u>slept</u> well.",
  s="보기 기호 ⓐ~ⓔ와 밑줄이 사라져 기호가 단어에 붙었다(예: awrote). 원문항 발문과 형식(ⓐ~ⓔ 밑줄)으로 되돌렸다. 보기와 정답은 그대로다.")
f19("E", "Last weekend, we ⓐ<u>saw</u> a movie. Tom ⓑ<u>made</u> popcorn. I ⓒ<u>eated</u> too much. We ⓓ<u>had</u> fun and ⓔ<u>went</u> home.",
    [("ⓐ: see의 불규칙 과거형이다.", "saw는 see의 과거형이다."), ("ⓓ: have의 불규칙 과거형이다.", "had는 have의 과거형이다."), ("ⓑ: make의 과거형은 maked로 써야 한다.", "make의 과거형은 made이므로 ⓑ는 알맞고, 이 설명이 틀렸다."),
     ("ⓔ: go의 불규칙 과거형이다.", "went는 go의 과거형이다."), ("ⓒ: eat의 과거형은 ate이므로 고쳐야 한다.", "eated는 ate로 고쳐야 한다.")], 3, S19)
f19("F", "Yesterday, the boys ⓐ<u>ran</u> in the park. One boy ⓑ<u>falled</u>. His friends ⓒ<u>came</u> over. They ⓓ<u>helped</u> him and ⓔ<u>were</u> worried.",
    [("ⓑ: fall의 과거형은 fell이므로 고쳐야 한다.", "falled는 fell로 고쳐야 한다."), ("ⓐ: run의 과거형은 runned이다.", "run의 과거형은 ran이므로 ⓐ는 알맞고, 이 설명이 틀렸다."), ("ⓒ: come의 불규칙 과거형이다.", "came은 come의 과거형이다."),
     ("ⓓ: help는 규칙동사라 -ed를 붙였다.", "helped는 규칙 과거형이다."), ("ⓔ: 복수 주어(They)에 맞춰 be동사 과거형 were를 썼다.", "복수 주어의 과거는 were이다.")], 2, S19)

# 3-20 옳은 문장 개수: B는 문장을 새로, C~E는 보기 정렬, F는 틀린 문장을 넣음
ST20 = "다음 중 어법상 옳은 문장의 개수를 고르시오."
R20 = "과거 긍정문에는 동사의 알맞은 과거형(불규칙동사 포함)을 쓰고, did/didn't 뒤에는 동사원형을 쓴다."
def f20(t, lines, judge, ok, s):
    n = len(ok.split(","))
    F(3, 20, t, st=ST20, p="\n".join("- " + x for x in lines), c=CNT5, a=n, r=R20, pre=["문장별 판정: " + j for j in judge], k=f"어법상 옳은 문장은 {ok}로 {n}개이다.", n="cnt", s=s + ipos(n))
f20("B", ["My mom baked cookies yesterday.", "We didn't went to the zoo.", "He teached us English.", "I losed my umbrella on the bus.", "Did she call you last night?"],
    ["첫째 O. 규칙동사 bake의 과거형 baked이다.", "둘째 X. didn't 뒤에는 동사원형(go)을 쓴다.", "셋째 X. teach의 과거형은 taught이다.", "넷째 X. lose의 과거형은 lost이다.", "다섯째 O. Did + 주어 + 동사원형이다."], "첫째, 다섯째",
    "제시문과 정답이 원문항과 똑같았고 선택지 순서도 뒤섞였다. 문장을 새로 쓰고 선택지를 1개~5개 순으로 정렬했으며 정답 개수를 2개로 바꿨다.")
S20 = "개수 선택지를 1개~5개 순으로 정렬하고 발문을 원문항과 같게 했다. 정답 개수·위치(3개, ③)가 원문항과 같지 않게 한 문장을 바꿨다."
f20("C", ["Tom went home.", "Jane buyed a bag.", "We didn't saw him.", "Did they ate lunch?", "I wrote a letter."],
    ["첫째 O. go의 과거형 went이다.", "둘째 X. buy의 과거형은 bought이다.", "셋째 X. didn't 뒤에는 동사원형(see)을 쓴다.", "넷째 X. Did 뒤에는 동사원형(eat)을 쓴다.", "다섯째 O. write의 과거형 wrote이다."], "첫째, 다섯째", S20)
f20("D", ["They came early.", "He didn't go home.", "Jane saw the movie.", "Did Tom write it?", "We maked dinner."],
    ["첫째 O. come의 과거형 came이다.", "둘째 O. didn't + 동사원형이다.", "셋째 O. see의 과거형 saw이다.", "넷째 O. Did + 주어 + 동사원형이다.", "다섯째 X. make의 과거형은 made이다."], "첫째, 둘째, 셋째, 넷째", S20)
for t, (o, nw) in {"E": ("②", "④")}.items():
    F(3, 20, t, st=ST20, op="sortc", s=f"개수 선택지를 1개~5개 순으로 정렬(정답 {o}→{nw})하고 발문을 원문항과 같게 했다.")
f20("F", ["We ate lunch.", "He didn't saw me.", "Jane writed a note.", "Did they went home?", "Tom buyed a car."],
    ["첫째 O. eat의 과거형 ate를 썼다.", "둘째 X. didn't 뒤에는 동사원형(see)을 쓴다.", "셋째 X. write의 과거형은 wrote이다.", "넷째 X. Did 뒤에는 동사원형(go)을 쓴다.", "다섯째 X. buy의 과거형은 bought이다."], "첫째",
    "틀린 문장이 없어 원문항(틀린 것 판별)과 달랐다. 네 문장을 틀린 문장으로 바꿔 옳은 문장이 1개가 되게 하고, 선택지를 1개~5개 순으로 정렬했다.")
