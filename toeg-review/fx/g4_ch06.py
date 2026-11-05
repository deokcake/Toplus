# 4급 CH6 조동사 (51~60) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
def talk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 옳지 않은 설명이다. 따라서 정답이다." if i + 1 == a else " 옳은 설명이다. 따라서 오답이다.")) if w.endswith("므로") else (w + (" 옳지 않은 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.")) for i, (_, w) in enumerate(items)], k=items[a-1][1], s=s + ipos(a), **kw)
CNT5 = ["1개", "2개", "3개", "4개", "5개"]

# 4-51 can = be able to: 원문항처럼 뜻이 다른 조동사 오답, 밑줄
R451 = "능력의 can(~할 수 있다)은 be able to + 동사원형으로 바꿔 쓸 수 있다. may(~해도 된다, ~일지도 모른다), must·have to(~해야 한다), might(~일지도 모른다)는 뜻이 다르다."
S451 = "원문항은 can과 뜻이 같은 표현을 여러 조동사 중에서 고르는 의미 문항인데, 변형은 선택지가 모두 be able to의 형태 변형이라 형태 판별 문항이 되었고 밑줄도 사라졌다. 원문항처럼 뜻이 다른 조동사 표현으로 오답을 바꾸고 밑줄을 넣었다."
ABLE = "능력의 can을 be able to로 바꿔 같은 뜻이므로"; MAY = "may는 허락·추측의 뜻이라 능력의 can과 다르므로"; MUST = "must는 ‘~해야 한다’는 의무라 뜻이 다르므로"; HAVE = "have to는 ‘~해야 한다’는 의무라 뜻이 다르므로"; MIGHT = "might는 ‘~일지도 모른다’는 추측이라 뜻이 다르므로"
def f451(t, p, items, a, s=S451):
    mk(4, 51, t, items, a, R451, s, st="R", p=p)
f451("B", "They <u>can</u> play soccer well.", [("They may play soccer well.", MAY), ("They must play soccer well.", MUST), ("They have to play soccer well.", HAVE), ("They might play soccer well.", MIGHT), ("They are able to play soccer well.", ABLE)], 5)
f451("C", "Jane <u>can</u> play the piano.", [("Jane may play the piano.", MAY), ("Jane is able to play the piano.", ABLE), ("Jane has to play the piano.", HAVE), ("Jane must play the piano.", MUST), ("Jane might play the piano.", MIGHT)], 2)
f451("D", "Tom <u>can</u> read English.", [("Tom must read English.", MUST), ("Tom might read English.", MIGHT), ("Tom is able to read English.", ABLE), ("Tom has to read English.", HAVE), ("Tom may read English.", MAY)], 3)
f451("E", "I <u>can</u> help you.", [("I have to help you.", HAVE), ("I may help you.", MAY), ("I must help you.", MUST), ("I am able to help you.", ABLE), ("I might help you.", MIGHT)], 4)
f451("F", "We <u>can</u> finish the work today.", [("We are able to finish the work today.", ABLE), ("We must finish the work today.", MUST), ("We have to finish the work today.", HAVE), ("We might finish the work today.", MIGHT), ("We may finish the work today.", MAY)], 1)

# 4-52 우리말 뜻에 맞는 조동사: 원문항 발문과 형식, 유형마다 정답 조동사를 달리
R452 = "must(~해야 한다), must not(~하면 안 된다), can(~할 수 있다), might(~일지도 모른다), will(~할 것이다)처럼 우리말 뜻에 맞는 조동사를 고른다."
S452 = "원문항은 우리말 뜻에 맞는 조동사를 여러 조동사 중에서 고르는데, 변형 발문이 ‘have to의 알맞은 형태’를 고르라고 해 has/have 수 일치 문항으로 바뀌었다. 원문항 발문과 형식(우리말 뜻에 맞는 조동사 고르기)으로 되돌리고 유형마다 정답 조동사를 달리했다."
MOD = {"can": "can은 ‘~할 수 있다’는 뜻이므로", "may": "may는 ‘~해도 된다, ~일지도 모른다’는 뜻이므로", "must": "must는 ‘~해야 한다’는 뜻이므로", "might": "might는 ‘~일지도 모른다’는 뜻이므로",
       "will": "will은 ‘~할 것이다’는 뜻이므로", "should": "should는 ‘~하는 것이 좋다’는 뜻이므로", "has to": "has to는 ‘~해야 한다’는 뜻이므로", "must not": "must not은 ‘~하면 안 된다’는 금지이므로",
       "don't have to": "don't have to는 ‘~할 필요가 없다’는 뜻이므로", "might not": "might not은 ‘~하지 않을지도 모른다’는 뜻이므로"}
def f452(t, ko, en, c, ok, s=S452):
    a = c.index(ok) + 1
    mk(4, 52, t, [(x, MOD[x] + (" 우리말과 맞아" if x == ok else " 우리말과 맞지 않아")) for x in c], a, R452, s, st="R", p=f"{ko}\n{en}", okdup=True)
f452("B", "Jane은 학교에서 반드시 교복을 입어야 한다.", "Jane _____ wear a uniform at school.", ["may", "must", "can", "will", "might"], "must")
f452("C", "내일은 비가 올지도 모른다.", "It _____ rain tomorrow.", ["must", "will", "might", "should", "has to"], "might",
     "우리말과 문장이 원문항과 같았고 발문이 ‘강한 의무를 직접 나타내는 조동사’라고 정답을 알려 주었다. 원문항 발문으로 되돌리고 우리말을 새로 써서 정답을 might로 바꿨다.")
f452("D", "우리 형은 세 가지 언어를 말할 수 있다.", "My brother _____ speak three languages.", ["must", "may", "should", "can", "will"], "can")
f452("E", "우리는 지금 반드시 출발해야 한다.", "We _____ leave now.", ["must", "can", "may", "might", "will"], "must")
f452("F", "학생들은 도서관에서 떠들면 안 된다.", "Students _____ make noise in the library.", ["don't have to", "can", "will", "might not", "must not"], "must not")

# 4-53 옳지 않은 설명: 유형마다 설명을 새로
R453 = "조동사 뒤에는 동사원형을 쓰고 조동사에 -s를 붙이지 않으며 두 개를 겹쳐 쓰지 않는다. must not은 금지, don't have to는 불필요를 나타내고, must는 의무와 강한 추측, may·might는 허락과 추측을 나타낸다."
S453 = "옳은 설명 오답 네 개가 B와 똑같았다. 유형마다 설명을 새로 썼다."
def f453(t, items, a, s=S453):
    talk(4, 53, t, items, a, R453, s)
f453("C", [("‘should’는 충고나 권유를 나타낸다.", "should는 ‘~하는 것이 좋다’는 충고를 나타내므로"), ("‘may’는 추측의 의미로도 쓰인다.", "may는 ‘~일지도 모른다’는 추측으로도 쓰이므로"),
           ("‘have to’의 부정은 ‘don't have to’이며 ‘~할 필요가 없다’는 뜻이다.", "don't have to는 불필요를 나타내므로"), ("‘must’의 과거형은 ‘musted’이다.", "must에는 과거형이 따로 없어 과거의 의무는 had to로 나타내므로"),
           ("‘will’은 미래의 일이나 의지를 나타낸다.", "will은 미래·의지를 나타내므로")], 4, "정답 설명(must not과 don't have to는 같은 의미이다)이 원문항과 똑같았고 오답도 B와 같았다. 설명을 모두 새로 썼다.")
f453("D", [("조동사 뒤에 ‘-s’를 붙여 주어와 수를 맞춘다.", "조동사는 주어와 관계없이 형태가 같아 -s를 붙이지 않으므로"), ("‘can’의 과거형은 ‘could’이다.", "can의 과거형은 could이므로"), ("‘must not’은 강한 금지를 나타낸다.", "must not은 금지를 나타내므로"),
           ("‘Can I ~?’는 허락을 구할 때 쓸 수 있다.", "Can I ~?는 허락을 구하는 표현이므로"), ("‘be able to’의 과거형은 ‘was/were able to’이다.", "be동사를 과거형으로 바꿔 나타내므로")], 1)
f453("E", [("‘should not’은 ‘~하지 않는 것이 좋다’는 뜻이다.", "should not은 충고의 부정이므로"), ("‘might’는 ‘may’보다 약한 추측을 나타낼 수 있다.", "might는 가능성이 더 낮은 추측에 쓰이므로"),
           ("조동사 두 개를 연달아 써서 ‘will can’처럼 쓸 수 있다.", "조동사는 두 개를 겹쳐 쓰지 않고 will be able to로 쓰므로"), ("‘have to’는 주어가 3인칭 단수이면 ‘has to’가 된다.", "3인칭 단수 주어에는 has to를 쓰므로"),
           ("‘May I ~?’는 공손하게 허락을 구하는 표현이다.", "May I ~?는 공손한 허락 요청이므로")], 3)
f453("F", [("‘must’는 강한 추측(~임에 틀림없다)의 뜻으로도 쓰인다.", "must는 강한 추측으로도 쓰이므로"), ("‘cannot’은 줄여서 ‘can't’로도 쓴다.", "cannot의 축약형은 can't이므로"), ("‘will not’의 줄임말은 ‘won't’이다.", "will not은 won't로 줄여 쓰므로"),
           ("‘should’는 조동사라 뒤에 동사원형을 쓴다.", "조동사 뒤에는 동사원형을 쓰므로"), ("‘be able to’ 뒤에는 동사의 -ing형을 쓴다.", "be able to 뒤에는 동사원형을 쓰므로")], 5,
     S453 + " 틀린 설명은 원문항의 정답(must not과 don't have to)과 겹치지 않는 내용으로 썼다.")

# 4-54 조동사 뒤 동사 형태: 원문항 발문과 밑줄, 조동사를 다양하게
ST454 = "다음 중 밑줄 친 부분이 어법상 틀린 문장을 고르시오."
R454 = "조동사(can, may, must, might, will, should)와 have to 뒤에는 to나 -s·-ing·과거형 없이 동사원형을 쓴다. be동사도 원형 be를 쓴다."
S454 = "원문항은 여러 조동사 뒤 동사 형태를 판별하는데, 변형 발문이 ‘can 뒤의 동사 형태’라고 오류 위치를 알려 주고 선택지도 모두 can 문장이었으며 밑줄이 사라지고 오답이 유형마다 같았다. 원문항 발문과 밑줄로 되돌리고 조동사를 다양하게 해 유형마다 새로 썼다."
OKB = "조동사 뒤에 동사원형을 바르게 썼으므로"
def f454(t, items, a, s=S454):
    mk(4, 54, t, [(x, w or OKB) for x, w in items], a, R454, s, st=ST454)
f454("B", [("You should <u>eat</u> more vegetables.", ""), ("They can <u>playing</u> soccer.", "can 뒤에는 동사원형 play를 쓰므로"), ("We must <u>be</u> quiet here.", ""), ("He might <u>come</u> late.", ""), ("Will you <u>help</u> me?", "")], 2)
f454("C", [("She will <u>visit</u> us soon.", ""), ("I have to <u>wear</u> glasses.", ""), ("May I <u>open</u> the window?", ""), ("Tom should <u>goes</u> to bed early.", "should 뒤에는 동사원형 go를 쓰므로"), ("You must <u>stop</u> here.", "")], 4,
     S454 + " 정답(She can sings very well.)이 원문항과 같아 새로 썼다.")
f454("D", [("We can <u>speak</u> English.", ""), ("Jane may <u>be</u> at home.", ""), ("He must <u>to leave</u> now.", "must 뒤에는 to 없이 동사원형 leave를 쓰므로"), ("You don't have to <u>hurry</u>.", ""), ("They will <u>arrive</u> soon.", "")], 3)
f454("E", [("It might <u>snow</u> tonight.", ""), ("Can you <u>swim</u>?", ""), ("She has to <u>finish</u> it.", ""), ("You should <u>see</u> a doctor.", ""), ("I will <u>called</u> you later.", "will 뒤에는 동사원형 call을 쓰므로")], 5)
f454("F", [("We might <u>are</u> late.", "might 뒤에는 동사원형 be를 쓰므로"), ("He can <u>run</u> fast.", ""), ("You must <u>keep</u> quiet.", ""), ("May I <u>sit</u> here?", ""), ("They have to <u>study</u>.", "")], 1)

# 4-55 옳은 문장 개수: 원문항 형식(ⓐ~ⓔ, 밑줄, 1개~5개)
ST455 = "다음 중 밑줄 친 부분이 어법상 옳은 문장의 개수를 고르시오."
R455 = "조동사 뒤에는 동사원형을 쓰고 조동사에 -s를 붙이지 않는다. must 뒤에 to를 쓰지 않으며, 조동사 의문문도 조동사 + 주어 + 동사원형이다."
S455 = "보기 기호 ⓐ~ⓔ가 a~e로 바뀌어 한 줄로 이어졌고 밑줄이 사라졌으며 선택지 순서가 뒤섞였다. 원문항 발문과 형식(ⓐ~ⓔ 줄바꿈, 밑줄, 1개~5개)으로 되돌렸다."
def f455(t, lines, judge, ok, s=S455):
    n = len(ok.split(","))
    F(4, 55, t, st=ST455, p="\n".join(lines), c=CNT5, a=n, r=R455, pre=["문장별 판정: " + j for j in judge], k=f"밑줄 친 부분이 옳은 문장은 {ok}로 {n}개이다.", n="cnt", s=s + ipos(n))
f455("B", ["ⓐ They <u>can goes</u>.", "ⓑ Jane <u>might be</u> home.", "ⓒ Tom <u>must go</u>.", "ⓓ We <u>can work</u>.", "ⓔ He <u>can reads</u>."],
     ["ⓐ X. can 뒤에는 동사원형 go를 쓴다.", "ⓑ O. might + 동사원형 be이다.", "ⓒ O. must + 동사원형이다.", "ⓓ O. can + 동사원형이다.", "ⓔ X. can 뒤에는 동사원형 read를 쓴다."], "ⓑ, ⓒ, ⓓ")
f455("C", ["ⓐ He <u>cans swim</u> well.", "ⓑ You <u>must to wait</u> here.", "ⓒ <u>May</u> I <u>coming</u> in?", "ⓓ She <u>might not be</u> busy.", "ⓔ They <u>should studies</u> more."],
     ["ⓐ X. 조동사 can에는 -s를 붙이지 않는다.", "ⓑ X. must 뒤에는 to 없이 동사원형을 쓴다.", "ⓒ X. May I 뒤에는 동사원형 come을 쓴다.", "ⓓ O. might not + 동사원형 be이다.", "ⓔ X. should 뒤에는 동사원형 study를 쓴다."], "ⓓ",
     "ⓐ·ⓑ가 원문항 문장과 같았고 기호·밑줄·선택지 순서도 원본과 달랐다. 문장을 새로 쓰고 원문항 형식으로 되돌렸으며 정답 개수를 1개로 바꿨다.")
f455("D", ["ⓐ She <u>can sing</u>.", "ⓑ Tom <u>might come</u>.", "ⓒ We <u>must study</u>.", "ⓓ They <u>can play</u>.", "ⓔ I <u>can helps</u>."],
     ["ⓐ O. can + 동사원형이다.", "ⓑ O. might + 동사원형이다.", "ⓒ O. must + 동사원형이다.", "ⓓ O. can + 동사원형이다.", "ⓔ X. can 뒤에는 동사원형 help를 쓴다."], "ⓐ, ⓑ, ⓒ, ⓓ")
f455("E", ["ⓐ I <u>can swim</u>.", "ⓑ She <u>must is</u> quiet.", "ⓒ They <u>might not come</u>.", "ⓓ Tom <u>can sing</u>.", "ⓔ We <u>must leave</u>."],
     ["ⓐ O. can + 동사원형이다.", "ⓑ X. must 뒤에는 동사원형 be를 쓴다.", "ⓒ O. might not + 동사원형이다.", "ⓓ O. can + 동사원형이다.", "ⓔ O. must + 동사원형이다."], "ⓐ, ⓒ, ⓓ, ⓔ",
     "틀린 문장이 없어 원문항(틀린 것 판별)과 달랐고 기호·밑줄·선택지 순서도 원본과 달랐다. ⓑ를 틀린 문장으로 바꾸고 원문항 형식으로 되돌렸다.")
f455("F", ["ⓐ Tom <u>can read</u>.", "ⓑ Jane <u>might be</u> late.", "ⓒ They <u>must wears</u> helmets.", "ⓓ We <u>can to help</u>.", "ⓔ I <u>can be</u> ready."],
     ["ⓐ O. can + 동사원형이다.", "ⓑ O. might + 동사원형 be이다.", "ⓒ X. must 뒤에는 동사원형 wear를 쓴다.", "ⓓ X. can 뒤에는 to 없이 동사원형을 쓴다.", "ⓔ O. can + 동사원형 be이다."], "ⓐ, ⓑ, ⓔ")

# 4-56 have to 형태: 원문항 발문, 문법상 옳은 be to와 없는 형태(musts)를 틀린 형태로
R456 = "have to는 주어가 3인칭 단수이면 has to, 그 밖에는 have to를 쓴다. be동사와 함께 쓰거나 -ing형으로 쓰지 않는다."
S456 = "발문이 ‘have to의 형태’로 바뀌었고, 오답에 없는 형태(musts)나 문법상 옳은 be to가 섞여 발문 조건에 기대야 했다. 원문항 발문으로 되돌리고 그 오답을 분명히 틀린 형태로 바꿨다."
W = {"has to": "3인칭 단수 주어에만 has to를 쓰므로", "have to": "3인칭 단수 주어에는 has to를 쓰므로", "does have": "‘~해야 한다’는 have to로 나타내고 to가 빠졌으므로",
     "having to": "-ing형만으로는 동사 자리에 쓸 수 없으므로", "are have to": "have to 앞에 be동사를 쓸 수 없으므로", "am have to": "have to 앞에 be동사를 쓸 수 없으므로",
     "is have to": "have to 앞에 be동사를 쓸 수 없으므로", "has": "has 뒤에 to가 빠졌으므로", "does to": "does to라는 표현은 없으므로"}
def f456(t, p, c, ok, s=S456):
    a = c.index(ok) + 1
    mk(4, 56, t, [(x, ("주어에 맞는 " + ok + "를 바르게 썼으므로") if x == ok else W[x]) for x in c], a, R456, s, st="R", p=p, okdup=True)
f456("B", "We ________ study tonight.", ["has to", "does have", "having to", "have to", "are have to"], "have to")
f456("C", "My sister ________ walk the dog every morning.", ["have to", "has to", "has", "having to", "is have to"], "has to", "제시문과 정답이 원문항과 똑같았고 문법상 옳은 is to가 오답에 섞여 있었다. 제시문을 새로 쓰고 원문항 발문으로 되돌렸으며 오답을 분명히 틀린 형태로 바꿨다.")
f456("D", "They ________ leave early.", ["does have", "having to", "has to", "have to", "are have to"], "have to")
f456("E", "I ________ finish this work.", ["have to", "does have", "am have to", "having to", "has to"], "have to")
f456("F", "Jane ________ wear a uniform.", ["does have", "has to", "does to", "having to", "have to"], "has to")

# 4-57 추측의 must: 원문항 발문과 밑줄, 선택지의 뜻 표시 삭제, 유형마다 새로
ST457 = "다음 문장의 밑줄 친 'must'의 의미와 같은 것은?"
R457 = "must는 규칙·의무(~해야 한다)와, 근거에 따른 강한 추측(~임에 틀림없다)으로 쓰인다. 앞 문장이나 because 뒤의 근거로 추측의 뜻을 구별한다."
S457 = "오답 네 개에 ‘[반드시 해야 할 일]’, ‘[지켜야 할 규칙]’처럼 must의 뜻을 붙여 놓아 표시가 없는 선택지가 바로 정답이 되었고, 오답이 유형마다 같았으며 밑줄도 사라졌다. 원문항 발문과 밑줄로 되돌리고 뜻 표시를 뺐으며 유형마다 오답을 새로 썼다."
OBL = "의무(~해야 한다)의 must라 본문의 추측과 다르므로"; INF = "근거에 따른 강한 추측(~임에 틀림없다)이라 본문의 must와 같으므로"; PRO = "금지(~하면 안 된다)의 must not이라 본문의 추측과 다르므로"
def f457(t, p, items, a, s=S457):
    mk(4, 57, t, items, a, R457, s, st=ST457, p=p)
f457("B", "The ground is wet. It <u>must</u> have rained.", [("I <u>must</u> finish this report today.", OBL), ("Students <u>must</u> be quiet in the library.", OBL), ("He <u>must</u> be sick because he looks pale.", INF),
     ("You <u>must</u> wear a seat belt.", OBL), ("We <u>must</u> leave now.", OBL)], 3)
f457("C", "Minho ran ten kilometers this morning. He <u>must</u> be hungry now.", [("You <u>must</u> not touch the paintings.", PRO), ("Jane <u>must</u> be at the library because her bag is gone.", INF), ("We <u>must</u> save water.", OBL),
     ("I <u>must</u> call my mom now.", OBL), ("Drivers <u>must</u> stop at a red light.", OBL)], 2, "본문과 정답이 원문항과 똑같았고 오답에 뜻 표시가 붙어 있었다. 본문과 정답을 새로 쓰고 " + S457[S457.index("원문항 발문과"):])
f457("D", "Tom studied all night. He <u>must</u> be sleepy.", [("Jane <u>must</u> be busy because she isn't answering.", INF), ("You <u>must</u> brush your teeth.", OBL), ("We <u>must</u> be kind to others.", OBL),
     ("I <u>must</u> return this book today.", OBL), ("Visitors <u>must</u> show their tickets.", OBL)], 1)
f457("E", "The door is open. Someone <u>must</u> be inside.", [("You <u>must</u> wash your hands first.", OBL), ("Players <u>must</u> follow the rules.", OBL), ("I <u>must</u> go to the dentist.", OBL),
     ("Tom <u>must</u> be home because his car is here.", INF), ("We <u>must</u> not run in the hall.", PRO)], 4)
f457("F", "She won the race. She <u>must</u> be happy.", [("Everyone <u>must</u> wear a mask here.", OBL), ("You <u>must</u> finish your meal.", OBL), ("I <u>must</u> clean my room today.", OBL),
     ("Children <u>must</u> go to bed early.", OBL), ("They <u>must</u> be excited because they are smiling.", INF)], 5)

# 4-58 Must ~? = Do/Does ~ have to ~?: 원문항 발문, 주어를 복수·1인칭으로 바꿔 정답 조합을 원문항과 다르게
S458 = "발문에 ‘have to를 사용하여’ 조건이 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다."
R458 = "Must ~?는 Do/Does + 주어 + have to + 동사원형 ~?으로 바꿀 수 있다. 3인칭 단수 주어에는 Does, 그 밖의 주어에는 Do를 쓰고, 뒤의 have는 원형이다."
for t in "DF": F(4, 58, t, st="R", s=S458)
W458 = {"Does - has": "Does 뒤에는 원형 have를 쓰고 주어도 3인칭 단수가 아니므로", "Does - have": "주어가 3인칭 단수가 아니라 Does를 쓸 수 없으므로", "Do - has": "Do 뒤에는 원형 have를 쓰므로",
        "Are - have": "have to 의문문은 be동사로 만들지 않으므로", "Is - have": "have to 의문문은 be동사로 만들지 않으므로", "Am - have": "have to 의문문은 be동사로 만들지 않으므로"}
def f458(t, p, c, s):
    a = c.index("Do - have") + 1
    mk(4, 58, t, [(x, "3인칭 단수가 아닌 주어에 Do를 쓰고 뒤에 원형 have를 바르게 썼으므로" if x == "Do - have" else W458[x]) for x in c], a, R458, s, st="R", p=p, okdup=True)
f458("B", "Must your parents work on Sundays?\n= ________ your parents ________ to work on Sundays?", ["Does - has", "Do - have", "Does - have", "Are - have", "Do - has"],
     "정답(Does - have)이 원문항과 같았다. 주어를 복수(your parents)로 바꿔 정답 조합을 Do - have로 바꾸고 원문항 발문으로 되돌렸다.")
f458("C", "Must I bring my lunch?\n= ________ I ________ to bring my lunch?", ["Am - have", "Does - have", "Do - has", "Do - have", "Does - has"],
     "제시문과 정답이 원문항과 똑같았다. 주어를 I로 바꿔 제시문을 새로 쓰고 원문항 발문으로 되돌렸다.")
f458("E", "Must Jane and Tom study now?\n= ________ Jane and Tom ________ to study now?", ["Does - has", "Are - have", "Do - has", "Is - have", "Do - have"],
     "정답(Does - have)이 원문항과 같았다. 주어를 Jane and Tom으로 바꿔 정답 조합을 Do - have로 바꾸고 원문항 발문으로 되돌렸다.")

# 4-60 might를 쓰는 이유: 원문항 형식([상황]/[문장], 밑줄), 유형마다 오답을 새로
ST460 = "다음 상황에서 'will' 대신 'might'를 사용하는 이유를 한국어로 가장 바르게 설명한 것은?"
R460 = "might는 현재나 미래의 일에 대해 가능성은 있지만 확실하지 않은 추측을 나타낸다. 확실한 예측의 will, 의무의 must, 허락의 may와 구별하며, 주어에 따라 will을 might로 바꾸는 규칙은 없다."
S460 = "오답 네 개(‘강한 의무’, ‘허락’, ‘100% 확실한 미래’, ‘과거의 습관’)가 유형마다 같았고 원문항의 [상황]/[문장] 구분과 밑줄이 사라졌다. 원문항 발문과 형식([상황]/[문장], 밑줄)으로 되돌리고 유형마다 오답을 새로 썼다."
OK460 = "확실하지 않은 가능성의 추측이라는 might의 뜻을 바르게 설명했으므로"
def f460(t, sit, sent, items, a, s=S460):
    mk(4, 60, t, items, a, R460, s, st=ST460, p=f"[상황] {sit}\n[문장] {sent}")
F(4, 60, "B", st=ST460, p="[상황] Tom didn't answer my call.\n[문장] He <u>might</u> be busy now.", s="원문항의 [상황]/[문장] 구분과 밑줄이 사라지고 발문이 바뀌었다. 원문항 발문과 형식으로 되돌렸다. 보기와 정답은 그대로다.")
f460("C", "Mina usually gets home at 5. But she is still at school at 6.", "Mina <u>might</u> miss dinner today.",
     [("저녁을 놓칠 것이 100% 확실하다는 것을 강조하기 위해서이다.", "might는 확실하지 않은 추측이라 100% 확실함과 반대이므로"), ("저녁을 놓치지 말라고 미나에게 강하게 명령하기 위해서이다.", "might는 명령을 나타내지 않으므로"),
      ("저녁을 놓칠 가능성은 있지만 아직 확실하지 않은 추측을 나타내기 위해서이다.", OK460), ("주어가 3인칭 단수일 때는 will 대신 might를 쓰는 규칙이 있기 때문이다.", "주어에 따라 will을 might로 바꾸는 규칙은 없으므로"),
      ("미나가 예전에 저녁을 자주 놓쳤다는 것을 설명하기 위해서이다.", "might는 과거의 경험을 나타내지 않으므로")], 3,
     "상황과 정답 설명이 원문항과 같았고 오답도 B와 같았다. 상황을 새로 쓰고 " + S460[S460.index("원문항 발문과"):])
f460("D", "Dark clouds are coming over the city.", "It <u>might</u> rain this afternoon.",
     [("비가 오도록 허락하는 뜻을 나타내기 위해서이다.", "might는 이 문장에서 허락이 아니라 추측을 나타내므로"), ("비가 올 가능성이 있지만 확실하지는 않다는 뜻을 나타내기 위해서이다.", OK460),
      ("비가 이미 내렸다는 과거의 사실을 나타내기 위해서이다.", "might + 동사원형은 과거의 사실을 나타내지 않으므로"), ("날씨를 말할 때는 반드시 might를 써야 하는 규칙이 있기 때문이다.", "날씨에도 will 등을 쓸 수 있어 그런 규칙은 없으므로"),
      ("비가 반드시 온다는 강한 확신을 나타내기 위해서이다.", "might는 약한 추측이라 강한 확신과 반대이므로")], 2)
f460("E", "Jane is not at home, and her bag is gone.", "She <u>might</u> be at school.",
     [("그녀가 학교에 있어야 한다는 의무를 나타내기 위해서이다.", "might는 의무를 나타내지 않으므로"), ("그녀가 학교에 있는 것이 틀림없다는 강한 확신을 나타내기 위해서이다.", "강한 확신은 must로 나타내고 might는 약한 추측이므로"),
      ("그녀가 매일 학교에 간다는 습관을 나타내기 위해서이다.", "might는 습관을 나타내지 않으므로"), ("그녀가 학교에 가도 된다는 허락을 나타내기 위해서이다.", "might는 이 문장에서 허락이 아니라 추측을 나타내므로"),
      ("그녀가 학교에 있을 가능성이 있지만 확실하지 않은 추측을 나타내기 위해서이다.", OK460)], 5)
f460("F", "The bus is moving very slowly because of heavy traffic.", "We <u>might</u> arrive late for the movie.",
     [("늦게 도착할 가능성이 있지만 아직 확실하지 않다는 추측을 나타내기 위해서이다.", OK460), ("늦게 도착하겠다는 우리의 강한 의지를 나타내기 위해서이다.", "의지는 will로 나타내고 might는 추측이므로"),
      ("늦게 도착해도 된다는 허락을 나타내기 위해서이다.", "might는 이 문장에서 허락이 아니라 추측을 나타내므로"), ("주어가 We일 때는 will 대신 might를 쓰는 규칙이 있기 때문이다.", "주어에 따라 will을 might로 바꾸는 규칙은 없으므로"),
      ("늦게 도착한 것이 이미 끝난 과거의 일이기 때문이다.", "아직 도착하지 않은 앞으로의 일이므로")], 1)


# ---- 2차 감수(2026-10) 추가 ----
# 4-60 B: 정답만 문장 내용(바쁠 가능성)을 말하고 오답은 일반론이라 눈에 띔 → 원문항처럼 상황에 맞춘 오개념 오답으로
FIX.pop((4, 60, "B"), None)
f460("B", "Tom didn't answer my call.", "He <u>might</u> be busy now.",
     [("그가 바쁜 것이 100% 확실하다는 것을 나타내기 위해서이다.", "might는 확실하지 않은 추측을 나타내므로"), ("그에게 바쁘게 지내라고 명령하기 위해서이다.", "might에는 명령의 뜻이 없으므로"),
      ("그가 예전에 자주 바빴다는 것을 설명하기 위해서이다.", "이 might는 과거의 경험이 아니라 지금에 대한 추측이므로"), ("그가 바쁠 가능성이 있지만 확실하지 않은 추측을 나타내기 위해서이다.", "전화를 받지 않은 까닭을 확실하지 않게 짐작하는 말이므로"),
      ("now(지금)라는 말이 있으면 will을 쓸 수 없기 때문이다.", "now가 있다고 will을 못 쓰는 것은 아니므로")], 4,
     "원문항의 [상황]/[문장] 구분과 밑줄이 사라지고 발문이 바뀌었으며, 정답만 문장 내용(바쁠 가능성)을 말하고 오답 네 개는 일반론(‘강한 의무’, ‘허락’ 등)이라 정답이 눈에 띄었다. 원문항 발문과 형식으로 되돌리고, 오답을 원문항처럼 그 상황에 맞춘 그럴듯한 오개념으로 썼다.")
