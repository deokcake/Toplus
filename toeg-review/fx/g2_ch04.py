# 2급 CH4 수동태 (31~40) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 2-33 for가 들어갈 수 없는 문장: 원문항 발문, 오답을 모두 for + 사람으로 유형마다 새로
R33 = "4형식 동사의 수동태에서 직접목적어가 주어가 되면 간접목적어 앞에 전치사를 쓴다. give·send·show·teach·lend·offer·award는 받는 사람 앞에 to를, buy·make·cook·find·choose·save·reserve·bake는 위해 주는 대상 앞에 for를 쓴다."
S33 = "발문이 ‘give/award/send… 뒤의 사람은 수령인, 나머지는 수혜자·목적’이라고 판단 기준을 설명해 답을 알려 주었고, 오답 네 문장이 유형마다 같았다. 원문항 발문(전치사 for가 들어갈 수 없는 문장)으로 되돌리고, 원문항처럼 오답을 모두 ‘for + 사람’ 문장으로 유형마다 새로 썼다."
def FOR(v): return f"{v}: 위해 해 주는 대상 앞에는 for를 쓰므로 for가 들어간다. 따라서"
def TO(v): return f"{v}: 받는 사람(수령인) 앞에는 to를 쓰므로 for가 들어갈 수 없다. 따라서"
mk(2, 33, "B", [("A new coat was bought _____ my sister by Mom.", FOR("bought")), ("A scholarship was awarded _____ Mina by the foundation.", TO("awarded")), ("Dinner was cooked _____ the guests by Dad.", FOR("cooked")),
                ("A good seat was found _____ me by the usher.", FOR("found")), ("Some cookies were made _____ the kids by Grandma.", FOR("made"))], 2, R33, S33, st="R")
mk(2, 33, "C", [("A table was booked _____ us by the manager.", FOR("booked")), ("A present was chosen _____ Dad by my brother.", FOR("chosen")), ("A pizza was ordered _____ the team by the coach.", FOR("ordered")),
                ("A book was lent _____ me by my friend.", TO("lent")), ("A treehouse was built _____ the kids by their uncle.", FOR("built"))], 4, R33,
   S33 + " ‘sent for’가 ‘부르러 보내다’로 읽힐 수 있는 ‘A letter was sent _____ Tom’을 ‘A book was lent _____ me’로 바꿨다.", st="R")
mk(2, 33, "D", [("Math was taught _____ us by Ms. Park.", TO("taught")), ("A parking space was saved _____ Tom by his friend.", FOR("saved")), ("A cup of tea was poured _____ the guest by the host.", FOR("poured")),
                ("A birthday cake was baked _____ Jane by her aunt.", FOR("baked")), ("New shoes were bought _____ the boy by his father.", FOR("bought"))], 1, R33,
   S33 + " ‘우리 대신 배달되었다’로 for가 들어갈 여지가 있는 ‘delivered _____ us’를 ‘taught _____ us’로 바꿨다.", st="R")
mk(2, 33, "E", [("A room was prepared _____ the visitors by the hotel.", FOR("prepared")), ("A hot meal was cooked _____ the workers by the chef.", FOR("cooked")), ("A taxi was called _____ the old lady by the clerk.", FOR("called")),
                ("A nice gift was picked out _____ Mom by us.", FOR("picked out")), ("A medal was given _____ the winner by the mayor.", TO("given"))], 5, R33, S33, st="R")
mk(2, 33, "F", [("A room was reserved _____ the speaker by the staff.", FOR("reserved")), ("A bag of snacks was bought _____ the team by the captain.", FOR("bought")), ("Some advice was offered _____ me by my coach.", TO("offered")),
                ("The best seats were saved _____ our parents by my sister.", FOR("saved")), ("Lunch was made _____ the volunteers by the chef.", FOR("made"))], 3, R33, S33, st="R")

# 2-35 사역·지각동사 수동태 학생 설명: 설명 다섯 개를 유형마다 새로, 틀린 설명도 다른 오개념
R35 = "능동 make의 원형부정사 보어는 수동태에서 to부정사가 된다. see/hear의 원형부정사 보어도 수동태에서 to부정사로 바뀌며, 현재분사 보어는 그대로 둔다. let은 be allowed to로, have는 보통 수동태로 쓰지 않는다."
def f35(t, items, a, s, **kw):
    F(2, 35, t, c=[x for x, _ in items], a=a, r=R35, n=[w + (" 틀린 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.") for i, (_, w) in enumerate(items)],
      k=f"틀린 답변을 한 학생은 {items[a-1][0].split(':')[0]}이다. {items[a-1][1]}", s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
S35 = "옳은 설명 네 개(준·민지·수아·태호)가 B와 똑같았다. 유형마다 학생 이름과 옳은 설명 네 개를 새로 썼다."
f35("B", [("하람: 사역동사 make의 수동태에서는 원형부정사가 to부정사로 바뀌어요.", "make + 목적어 + 원형부정사는 수동태에서 be made + to부정사가 된다."),
          ("도현: 사역동사 make의 수동태는 능동태의 원형부정사를 그대로 두어 'was made clean'처럼 써요.", "make의 수동태에서는 원형부정사를 to부정사로 바꿔 was made to clean으로 쓴다."),
          ("가은: 'We saw him running.'은 'He was seen running by us.'처럼 현재분사를 그대로 둘 수 있어요.", "지각동사의 현재분사 보어는 수동태에서도 그대로 둔다."),
          ("지안: let은 수동태로 잘 쓰지 않고 'be allowed to'로 바꿔 표현해요.", "let의 수동태 대신 be allowed to를 쓴다."),
          ("로운: 'I heard her sing.'을 수동태로 바꾸면 'She was heard to sing by me.'가 돼요.", "지각동사의 원형부정사 보어는 수동태에서 to부정사가 된다.")], 2,
    "틀린 설명(수진: be made to-V의 to는 생략 가능)이 원문항 정답과 이름·내용까지 같았다. 학생 이름과 설명을 새로 쓰고, 틀린 설명을 ‘make 수동태에서 원형부정사를 그대로 둔다’는 다른 오개념으로 바꿨다.")
f35("C", [("서진: 'She made him wait.'를 수동태로 바꾸면 'He was made to wait by her.'예요.", "make의 원형부정사 보어는 수동태에서 to부정사가 된다."),
          ("윤아: 지각동사 hear의 목적격 보어가 원형부정사이면 수동태에서는 to부정사로 바꿔요.", "지각동사의 원형부정사 보어는 수동태에서 to부정사가 된다."),
          ("태민: 목적격 보어가 현재분사이면 수동태에서도 현재분사를 그대로 써요.", "현재분사 보어는 수동태에서도 그대로 둔다."),
          ("소율: 행위자가 누구인지 중요하지 않으면 'by + 목적격'을 생략할 수 있어요.", "행위자가 중요하지 않거나 분명하면 by + 목적격을 생략한다."),
          ("민호: 'He was seen cross the street.'처럼 수동태에서도 원형을 그대로 써야 해요.", "지각동사의 원형부정사 보어는 수동태에서 to부정사로 바꿔 was seen to cross로 쓴다(현재분사 crossing도 가능).")], 5, S35)
f35("D", [("예준: 사역동사 make의 수동태는 'be made + to부정사' 형태예요.", "make의 원형부정사 보어는 수동태에서 to부정사가 된다."),
          ("채아: 'Mom let me go out.'은 'I was allowed to go out by Mom.'으로 바꿔 쓸 수 있어요.", "let의 수동태는 be allowed to로 나타낸다."),
          ("지수: make 수동태에서는 'to + 동사원형' 대신 반드시 -ing만 써야 해요.", "make의 수동태에서는 -ing가 아니라 to부정사를 쓴다."),
          ("하율: 사역동사 have는 보통 수동태로 바꾸지 않아요.", "have + 목적어 + 원형부정사는 보통 수동태로 쓰지 않는다."),
          ("시안: 수동태의 be동사는 능동태의 시제에 맞춰 was, is 등으로 바꿔요.", "수동태의 be동사는 능동태 동사의 시제에 맞춘다.")], 3, S35)
f35("E", [("리나: 'He made me laugh.'의 수동태는 'I was made to laugh by him.'이에요.", "make의 원형부정사 보어는 수동태에서 to부정사가 된다."),
          ("주원: 지각동사 see 뒤의 원형부정사는 수동태에서 to부정사로 바뀌어요.", "지각동사의 원형부정사 보어는 수동태에서 to부정사가 된다."),
          ("다인: let의 수동태 대신 'be allowed to'를 써서 허락받은 뜻을 나타내요.", "let은 be allowed to로 수동의 뜻을 나타낸다."),
          ("유리: 'The cat was heard crying.'처럼 현재분사를 그대로 두는 수동태는 쓸 수 없어요.", "지각동사의 현재분사 보어는 수동태에서도 그대로 둘 수 있으므로 was heard crying은 옳다."),
          ("은우: 수동태 문장에서 행위자를 밝힐 때는 by 뒤에 목적격을 써요.", "행위자는 by + 목적격으로 나타낸다.")], 4,
    S35 + " 교사 질문이 분사만 다뤄 설명과 어긋나지 않도록 질문을 넓혔다.", p="교사: 사역동사와 지각동사를 수동태로 바꿀 때 주의할 점은 무엇인가요?")
f35("F", [("하준: 'was made to leave'에서 to는 전치사라 뒤에 -ing을 써야 해요.", "was made to leave의 to는 to부정사의 to이므로 뒤에 동사원형을 쓴다."),
          ("나은: 'The coach made the players run.'은 'The players were made to run by the coach.'가 돼요.", "make의 원형부정사 보어는 수동태에서 to부정사가 된다."),
          ("건: 지각동사의 목적격 보어가 원형부정사이면 수동태에서 to부정사가 돼요.", "지각동사의 원형부정사 보어는 수동태에서 to부정사가 된다."),
          ("아린: 'We heard the baby crying.'의 수동태는 'The baby was heard crying by us.'예요.", "현재분사 보어는 수동태에서도 그대로 둔다."),
          ("도윤: 사역동사 have와 let은 보통 수동태로 쓰지 않고 다른 표현으로 바꿔 써요.", "have는 보통 수동태로 쓰지 않고, let은 be allowed to로 바꿔 쓴다.")], 1, S35)

# 2-38 진행형 수동태 밑줄 오류: 원문항 발문·밑줄 복원, 진행형 수동태 문장으로
R38 = "진행형 수동태는 be동사 + being + 과거분사이다. be동사는 주어의 수와 시제에 맞추고, being 뒤에는 과거분사를 쓰며, 행위자는 by + 목적격으로 나타낸다."
S38 = "원문항은 밑줄 친 다섯 부분 중 틀린 곳을 고르는데 변형은 밑줄이 없고 발문이 바뀌었으며, 원문항의 진행형 수동태가 단순·조동사 수동태로 바뀌었다. 원문항 발문과 밑줄 형식으로 되돌리고 진행형 수동태 문장으로 다시 썼다."
def f38(t, parts, pre, post, notes, a):
    p = pre + " ".join(f"{'①②③④⑤'[i]}<u>{x}</u>" for i, x in enumerate(parts)) + post
    notes = [re.sub(r"알맞다\.$", "알맞으므로", re.sub(r"썼다\.$", "썼으므로", x)) for x in notes]
    mk(2, 38, t, list(zip(parts, notes)), a, R38, S38, st="R", p=p)
f38("B", ["is", "been", "baked", "in", "the oven"], "Right now, the cake ", ".",
    ["is: 단수 주어(the cake)의 현재진행에 맞으므로", "been: 진행형 수동태는 be동사 + being + 과거분사이므로 being으로 고쳐야 한다. 어법상 틀린 부분이므로", "baked: being 뒤에 과거분사를 바르게 썼다.", "in: ‘오븐 안에서’라는 장소를 나타내 알맞다.", "the oven: 전치사 뒤 명사로 알맞다."], 2)
f38("C", ["was", "being", "sorted", "when", "I arrived"], "These letters ", ".",
    ["was: 주어(These letters)가 복수이므로 were로 고쳐야 한다. 어법상 틀린 부분이므로", "being: 과거진행 수동태의 being으로 알맞다.", "sorted: being 뒤에 과거분사를 바르게 썼다.", "when: 때를 나타내는 접속사로 알맞다.", "I arrived: 과거의 한 시점을 나타내는 절로 알맞다."], 1)
f38("D", ["is", "being", "clean", "by", "the staff"], "Look! The room ", ".",
    ["is: 단수 주어(The room)의 현재진행에 맞으므로", "being: 진행형 수동태의 being으로 알맞다.", "clean: 방이 청소되는 수동 관계이므로 과거분사 cleaned로 고쳐야 한다. 어법상 틀린 부분이므로", "by: 행위자를 나타내는 전치사로 알맞다.", "the staff: by 뒤 행위자로 알맞다."], 3)
f38("E", ["is", "being", "discussed", "by", "they"], "The problem ", " now.",
    ["is: 단수 주어(The problem)의 현재진행에 맞으므로", "being: 진행형 수동태의 being으로 알맞다.", "discussed: being 뒤에 과거분사를 바르게 썼다.", "by: 행위자를 나타내는 전치사로 알맞다.", "they: 전치사 by 뒤에는 목적격을 써야 하므로 them으로 고쳐야 한다. 어법상 틀린 부분이므로"], 5)
f38("F", ["of", "the house", "are", "been", "painted"], "Look! The walls ", ".",
    ["of: ‘집의 벽’을 나타내는 전치사로 알맞다.", "the house: 전치사 뒤 명사로 알맞다.", "are: 복수 주어(The walls)의 현재진행에 맞으므로", "been: 진행형 수동태는 be동사 + being + 과거분사이므로 being으로 고쳐야 한다. 어법상 틀린 부분이므로", "painted: 벽이 칠해지는 수동 관계의 과거분사로 알맞다."], 4)

# 2-39 진행형 + 구동사 수동태: 원문항처럼 빈칸 다섯 개, 원문항 발문
R39 = "전치사·부사가 포함된 동사 표현(talk about, look after 등)을 수동태로 바꿀 때 그 전치사·부사를 동사 바로 뒤에 그대로 둔다. 현재진행 수동태는 am/is/are being + 과거분사이며, 행위자는 by + 목적격으로 나타낸다."
S39 = "원문항은 빈칸 다섯 개에 단어를 채우는 형식인데 변형은 긴 빈칸 하나였고 발문이 바뀌었다. 원문항처럼 빈칸을 단어 수만큼(다섯 개) 나누고 발문을 원문항과 같게 했다."
BL = " ".join(["________"] * 5)
def f39(t, act, subj, obj, items, a, s=""):
    mk(2, 39, t, items, a, R39, S39 + s, st="R", p=f"\"{act}\"\n→ {subj} {BL} {obj}.")
def n39(be, vpp, part, kind, tense):
    return {"ok": f"현재진행 수동태({be} being + 과거분사)에 {part}를 동사 바로 뒤에 두고 by를 이어 썼으므로",
            "base": "being 뒤에는 동사원형이 아니라 과거분사를 써야 하므로",
            "order": f"{kind} {part}는 과거분사 바로 뒤에 두어야 하는데 by 뒤로 옮겼으므로",
            "tense": f"능동문이 현재진행({tense})이므로 {be}를 써야 하는데 과거진행으로 바꿨으므로",
            "being": "being은 be동사 바로 뒤, 과거분사 앞에 와야 하므로"}
N = n39("is", "talked", "about", "전치사", "are talking")
f39("B", "People are talking about the new policy.", "The new policy", "people",
    [("is being talked about by", N["ok"]), ("is being talk about by", N["base"]), ("is being talked by about", N["order"]), ("is talked being about by", N["being"]), ("was being talked about by", N["tense"])], 1)
N = n39("is", "looked", "after", "전치사", "are looking")
f39("C", "They are looking after the injured dog.", "The injured dog", "them",
    [("is being looked by after", N["order"]), ("was being looked after by", N["tense"]), ("is being looked after by", N["ok"]), ("is looked being after by", N["being"]), ("is being look after by", N["base"])], 3)
N = n39("is", "pointed", "at", "전치사", "are pointing")
f39("D", "Many people are pointing at the strange sign.", "The strange sign", "many people",
    [("was being pointed at by", N["tense"]), ("is being pointed at by", N["ok"]), ("is being pointed by at", N["order"]), ("is being point at by", N["base"]), ("is pointed being at by", N["being"])], 2,
    " 원문항과 같은 동사(laugh at)를 쓴 문장을 ‘point at’ 문장으로 바꿨다.")
N = n39("is", "dealt", "with", "전치사", "are dealing")
f39("E", "The staff are dealing with the complaint.", "The complaint", "the staff",
    [("is being deal with by", N["base"]), ("is being dealt by with", N["order"]), ("was being dealt with by", N["tense"]), ("is being dealt with by", N["ok"]), ("is dealt being with by", N["being"])], 4,
    " 빈칸이 여섯 단어가 되는 ‘take care of’ 문장을 다섯 단어가 되는 ‘deal with’ 문장으로 바꿨다.")
N = n39("are", "turned", "off", "부사", "is turning")
f39("F", "Someone is turning off the lights.", "The lights", "someone",
    [("are being turn off by", N["base"]), ("are turned being off by", N["being"]), ("are being turned by off", N["order"]), ("were being turned off by", N["tense"]), ("are being turned off by", N["ok"])], 5,
    " 빈칸이 여섯 단어가 되는 ‘speak highly of’ 문장을 다섯 단어가 되는 ‘turn off’ 문장으로 바꿨다. 주어(The lights)가 복수이므로 are being을 쓴다.")

# 2-40 틀린 문장 개수: 원문항처럼 여섯 문장, 1개~5개 정렬, 정답 개수를 원문항(2개)과 다르게
R40 = "진행 수동태는 be being p.p., 완료 수동태는 have/has been p.p., 미래 수동태는 will be p.p.이다. make·지각동사의 원형부정사 보어는 수동태에서 to부정사가 되며 지각동사의 현재분사 보어는 그대로 둔다. be interested는 in과 함께 쓴다."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]
def f40(t, lines, judge, wrong, s):
    n = len(wrong.split(","))
    F(2, 40, t, p="\n".join(lines), c=CNT5, a=n, r=R40, pre=["문장별 판정: " + j for j in judge], k=f"어법상 틀린 문장은 {wrong}로 {n}개이다.", n="cnt", s=s + f" 정답 위치 {'①②③④⑤'[n-1]}.")
S40 = "보기 문장이 원문항(6개)보다 적은 5개였고 개수 선택지 순서가 원문항과 달랐다. 원문항처럼 문장을 여섯 개로 하고 선택지를 1개~5개 순으로 정렬했으며, 문장마다 줄을 바꿨다."
f40("B", ["ⓐ The road is being repaired right now.", "ⓑ The students were taught French last year.", "ⓒ The package has delivered already.", "ⓓ Mina was seen cross the street.", "ⓔ The windows have been cleaned.", "ⓕ He is interested at learning Chinese."],
    ["ⓐ O. 진행 수동태(is being repaired)이다.", "ⓑ O. 4형식 teach의 간접목적어를 주어로 한 수동태이다.", "ⓒ X. 소포는 배달되는 대상이므로 완료 수동태를 쓴다. 교정문: The package has been delivered already.",
     "ⓓ X. 지각동사의 원형부정사 보어는 수동태에서 to부정사가 된다. 교정문: Mina was seen to cross the street. (또는 crossing)", "ⓔ O. 완료 수동태(have been cleaned)이다.", "ⓕ X. be interested는 in과 함께 쓴다. 교정문: He is interested in learning Chinese."],
    "ⓒ, ⓓ, ⓕ", S40 + " 정답 개수·위치(② 2개)가 원문항과 같아 ⓕ를 더해 틀린 문장이 3개가 되게 했다.")
f40("C", ["ⓐ The room is being painted.", "ⓑ Tom was made to apologize.", "ⓒ The letters have been sent.", "ⓓ The bridge is being build.", "ⓔ Jane was seen dancing.", "ⓕ The meeting will be held tomorrow."],
    ["ⓐ O. 진행 수동태(is being painted)이다.", "ⓑ O. make의 원형부정사 보어가 수동태에서 to부정사(to apologize)가 되었다.", "ⓒ O. 완료 수동태(have been sent)이다.",
     "ⓓ X. being 뒤에는 과거분사를 쓴다. 교정문: The bridge is being built.", "ⓔ O. 지각동사의 현재분사 보어(dancing)를 수동태에서 그대로 두었다.", "ⓕ O. 미래 수동태(will be held)이다."],
    "ⓓ", "보기 문장이 5개이고 선택지 범위가 0개~4개로 원문항과 달랐다. 원문항처럼 문장을 여섯 개로 하고 선택지를 1개~5개로 맞췄으며, 문장마다 줄을 바꿨다.")
f40("D", ["ⓐ The car has been repaired.", "ⓑ The door was being open when I arrived.", "ⓒ The boy was heard sing.", "ⓓ These books were wrote by a famous author.", "ⓔ The trees are being plant.", "ⓕ The cake was ate by my brother."],
    ["ⓐ O. 완료 수동태(has been repaired)이다.", "ⓑ X. being 뒤에는 과거분사를 쓴다. 교정문: The door was being opened when I arrived.", "ⓒ X. 지각동사의 원형부정사 보어는 수동태에서 to부정사가 된다. 교정문: The boy was heard to sing.",
     "ⓓ X. 수동태에는 과거분사를 쓴다. 교정문: These books were written by a famous author.", "ⓔ X. being 뒤에는 과거분사를 쓴다. 교정문: The trees are being planted.", "ⓕ X. 수동태에는 과거분사를 쓴다. 교정문: The cake was eaten by my brother."],
    "ⓑ, ⓒ, ⓓ, ⓔ, ⓕ", S40 + " 다른 유형과 정답 개수가 겹치지 않게 틀린 문장을 5개로 했다.")
f40("E", ["ⓐ The report will be finished tomorrow.", "ⓑ The road is being widen.", "ⓒ The child was made clean the room.", "ⓓ The package has been delivered.", "ⓔ The song was sung by Mina.", "ⓕ The baby is being looked after her aunt."],
    ["ⓐ O. 미래 수동태(will be finished)이다.", "ⓑ X. being 뒤에는 과거분사를 쓴다. 교정문: The road is being widened.", "ⓒ X. make의 원형부정사 보어는 수동태에서 to부정사가 된다. 교정문: The child was made to clean the room.",
     "ⓓ O. 완료 수동태(has been delivered)이다.", "ⓔ O. 단순과거 수동태(was sung)이다.", "ⓕ X. look after의 after를 그대로 두고 행위자 앞에 by를 쓴다. 교정문: The baby is being looked after by her aunt."],
    "ⓑ, ⓒ, ⓕ", S40)
f40("F", ["ⓐ The house is being built.", "ⓑ The car was repair yesterday.", "ⓒ The student was seen running.", "ⓓ The letter has been wrote.", "ⓔ The work will completed soon.", "ⓕ Jane was made to waiting outside."],
    ["ⓐ O. 진행 수동태(is being built)이다.", "ⓑ X. 수동태에는 과거분사를 쓴다. 교정문: The car was repaired yesterday.", "ⓒ O. 지각동사의 현재분사 보어(running)를 수동태에서 그대로 두었다.",
     "ⓓ X. 완료 수동태에는 과거분사를 쓴다. 교정문: The letter has been written.", "ⓔ X. 미래 수동태는 will be + 과거분사이다. 교정문: The work will be completed soon.", "ⓕ X. to부정사의 to 뒤에는 동사원형을 쓴다. 교정문: Jane was made to wait outside."],
    "ⓑ, ⓓ, ⓔ, ⓕ", S40)

# ---- 2차 감수(2026-10) 추가 ----
# 2-31 C·E·F: 영어에 없는 형태의 오답(have build, had being prepared, will been announced)을 형태가 바른 능동형으로
R31 = "주어가 동작을 받는 대상이면 수동태(be동사 + 과거분사)를 쓴다. 시제는 be동사가 나타낸다: 현재완료 have/has been p.p., 과거완료 had been p.p., 미래 will be p.p."
S31 = "오답 가운데 영어에 없는 형태({})가 있어 형태만으로 지워졌다. 원문항처럼 형태는 바르지만 태가 틀린 능동형({})으로 바꿨다."
mk(2, 31, "C", [("have built", "교실은 지어지는 대상이라 능동태를 쓸 수 없으므로"), ("built", "교실은 지어지는 대상이라 능동태를 쓸 수 없으므로"), ("were building", "교실은 지어지는 대상이라 능동 진행형을 쓸 수 없으므로"),
                ("have been built", "복수 주어에 맞는 현재완료 수동태로 this semester와도 어울리므로"), ("has been built", "주어 Several new classrooms가 복수라 has를 쓸 수 없으므로")], 4, R31, S31.format("have build", "have built"))
mk(2, 31, "E", [("has been prepared", "주어 The documents가 복수이고, 회의 시작보다 먼저 끝난 일이라 has를 쓸 수 없으므로"), ("had been prepared", "회의가 시작된 과거보다 먼저 준비가 끝났음을 과거완료 수동태로 나타내므로"),
                ("prepared", "서류는 준비되는 대상이라 능동태를 쓸 수 없으므로"), ("were preparing", "서류는 준비되는 대상이라 능동 진행형을 쓸 수 없으므로"), ("had prepared", "서류는 준비되는 대상이라 능동 과거완료를 쓸 수 없으므로")], 2, R31, S31.format("had being prepared", "had prepared"))
mk(2, 31, "F", [("were announcing", "수상자는 발표되는 대상이고 tomorrow와 과거 시제도 맞지 않으므로"), ("will announce", "수상자는 발표되는 대상이라 능동태를 쓸 수 없으므로"), ("will be announced", "tomorrow에 맞는 미래 수동태이므로"),
                ("announced", "수상자는 발표되는 대상이고 tomorrow와 과거 시제도 맞지 않으므로"), ("has been announced", "주어 The winners가 복수이고 tomorrow와 현재완료도 맞지 않으므로")], 3, R31, S31.format("will been announced", "will announce"))

# 2-32 B~F: 없는 형태(was design, were bake)와 Did ~ -ing 오답 → 원문항처럼 원형·과거(분사)·수동태 조합으로, (A)(B) 표시 삭제, 기호 —
R32 = "Did + 주어 뒤에는 동사원형을 쓴다. 주어가 동작을 받는 대상이면 수동태(be동사 + 과거분사)를 쓰고, 과거의 일이면 be동사를 과거형으로 쓴다."
S32 = "오답에 영어에 없는 형태({})가 섞여 형태만으로 지워졌다. 원문항처럼 동사원형·과거형(과거분사)·수동태를 조합한 보기로 바꾸고, 원문항에 없는 (A)·(B) 표시를 지웠다."
def f32(t, c, a, base, passive, bad):
    v = V(2, 32, t)
    def note(x):
        l, r = x.split(" — ")
        if l == base and r == passive: return f"Did 뒤에는 동사원형({base}), by ~가 있는 둘째 빈칸에는 과거 수동태({passive})를 쓰므로"
        if l != base and r != passive: return "두 빈칸 모두 맞지 않으므로"
        if l != base: return f"Did + 주어 뒤에는 동사원형({base})을 써야 하므로"
        return f"둘째 빈칸의 주어는 동작을 받는 대상이라 수동태({passive})를 써야 하므로"
    mk(2, 32, t, [(x, note(x)) for x in c], a, R32, S32.format(bad), p=v["passage"].replace("(A) ", "").replace("(B) ", ""))
f32("B", ["designed — designed", "was designed — design", "designed — was designed", "design — was designed", "was designed — designed"], 4, "design", "was designed", "was design")
f32("C", ["baked — were baked", "were baked — baked", "bake — were baked", "baked — baked", "were baked — bake"], 3, "bake", "were baked", "were bake")
f32("D", ["wrote — wrote", "written — was written", "write — was written", "was written — wrote", "wrote — was written"], 3, "write", "was written", "was write")
f32("E", ["cleaned — cleaned", "was cleaned — clean", "clean — was cleaned", "cleaned — was cleaned", "was cleaned — cleaned"], 3, "clean", "was cleaned", "was clean")
f32("F", ["took — took", "taken — was taken", "take — was taken", "took — was taken", "was taken — took"], 3, "take", "was taken", "was take")
