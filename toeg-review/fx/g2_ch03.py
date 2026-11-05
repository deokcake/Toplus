# 2급 CH3 조동사 (21~30) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)

# 2-21 같은 의미의 조동사: 보기를 모두 같은 조동사로, 뜻만 다르게
RMAY = "조동사 may: ‘~일지도 모른다’(추측), ‘~해도 된다’(허락), ‘May I …?’(허락 요청), ‘may not’(금지), ‘May + 주어 + 동사원형 …!’(기원)처럼 여러 뜻으로 쓰이므로 문맥으로 구별한다."
S21 = "원문항은 같은 조동사의 여러 뜻을 구별하는 문항인데, 변형은 서로 다른 조동사(can, should, must, may) 문장 가운데 추측을 고르게 해 쉬워졌고, 보기 밑줄이 없었으며 오답 네 문장이 유형마다 같았다. 원문항처럼 보기를 모두 같은 조동사로 쓰고 뜻만 다르게 했으며 밑줄을 넣었다."
GUESS, PERM, ASK, BAN, WISH = "추측(~일지도 모른다)", "허락(~해도 된다)", "허락 요청(~해도 될까요?)", "금지(~해서는 안 된다)", "기원(~하기를 빈다)"
def m21(kind, same): return f"{kind}의 뜻으로, 주어진 문장과 {'같은 뜻이므로' if same else '뜻이 다르므로'}"
mk(2, 21, "B", [("<u>May</u> I borrow your pen?", m21(ASK, 0)), ("You <u>may</u> not park your car here.", m21(BAN, 0)), ("Visitors <u>may</u> take photos in the lobby.", m21(PERM, 0)),
                ("Jane <u>may</u> be late because of the traffic.", m21(GUESS, 1)), ("<u>May</u> you have a wonderful trip!", m21(WISH, 0))], 4, RMAY, S21,
   k="주어진 문장은 불이 꺼져 있는 것을 근거로 ‘자고 있을지도 모른다’고 추측한다. ④도 교통 체증 때문에 ‘늦을지도 모른다’는 추측이다.")
mk(2, 21, "C", [("It <u>may</u> snow a lot this weekend.", m21(GUESS, 0)), ("He <u>may</u> not know my phone number.", m21(GUESS, 0)), ("Anyone who finishes early <u>may</u> leave the room.", m21(PERM, 1)),
                ("<u>May</u> all your dreams come true!", m21(WISH, 0)), ("The rumor <u>may</u> not be true.", m21(GUESS, 0))], 3, RMAY,
   S21 + " 다른 유형과 겹치지 않게 주어진 문장을 허락의 뜻(‘숙제를 마치면 컴퓨터를 써도 된다’)으로 바꿨다.",
   p="You <u>may</u> use my computer after you finish your homework.", k="주어진 문장은 숙제를 마친 뒤 컴퓨터를 ‘써도 된다’는 허락이다. ③도 일찍 끝낸 사람은 ‘나가도 된다’는 허락이다.")
RCOULD = "조동사 could: 과거의 능력(~할 수 있었다), 공손한 요청(Could you …?), 허락 요청(Could I …?), 현재·미래의 추측(~일 수도 있다)을 나타내므로 문맥으로 구별한다."
mk(2, 21, "D", [("That noise <u>could</u> be the wind.", "추측(~일 수도 있다)의 뜻으로, 주어진 문장과 같은 뜻이므로"), ("I <u>could</u> read when I was four.", "과거의 능력(~할 수 있었다)의 뜻으로, 주어진 문장과 뜻이 다르므로"),
                ("<u>Could</u> you pass me the salt?", "공손한 요청(~해 주시겠어요?)의 뜻으로, 주어진 문장과 뜻이 다르므로"), ("<u>Could</u> I use your bathroom?", "허락 요청(~해도 될까요?)의 뜻으로, 주어진 문장과 뜻이 다르므로"),
                ("My grandma <u>could</u> speak three languages.", "과거의 능력(~할 수 있었다)의 뜻으로, 주어진 문장과 뜻이 다르므로")], 1, RCOULD,
   S21 + " 주어진 문장의 조동사(could)에 맞춰 보기를 모두 could로 썼다.", k="주어진 문장은 전화를 받지 않는 것을 근거로 ‘바쁠 수도 있다’고 추측한다. ①도 그 소리가 ‘바람 소리일 수도 있다’는 추측이다.")
mk(2, 21, "E", [("You <u>may</u> sit anywhere you like.", m21(PERM, 0)), ("<u>May</u> I see your ticket, please?", m21(ASK, 0)), ("Swimmers <u>may</u> not dive into the shallow pool.", m21(BAN, 0)),
                ("<u>May</u> you both be very happy together!", m21(WISH, 0)), ("This answer <u>may</u> be wrong, so check it again.", m21(GUESS, 1))], 5, RMAY, S21,
   k="주어진 문장은 일찍 떠난 것을 근거로 ‘집에 있을지도 모른다’고 추측한다. ⑤도 답이 ‘틀렸을지도 모른다’는 추측이다.")
mk(2, 21, "F", [("<u>May</u> I leave a message for her?", m21(ASK, 0)), ("The keys <u>may</u> be in your coat pocket.", "‘~일지도 모른다’는 추측을 나타내 주어진 문장과 같은 뜻이므로"),
                ("Children under 12 <u>may</u> not enter without an adult.", m21(BAN, 0)), ("You <u>may</u> borrow up to five books at a time.", m21(PERM, 0)), ("<u>May</u> peace be with you.", m21(WISH, 0))], 2,
   RMAY + " may have + 과거분사는 과거 일에 대한 추측(~했을지도 모른다)이다.",
   S21 + " 주어진 문장의 might를 보기와 같은 may로 바꿨다.", p="The road is wet. It <u>may</u> have rained last night.",
   k="주어진 문장은 길이 젖은 것을 근거로 ‘비가 왔을지도 모른다’고 과거 일을 추측한다. ②도 ‘버스를 놓쳤을지도 모른다’는 과거 일의 추측이다.")

# 2-22 used to: 쓰임을 알려 주던 발문을 원문항대로, 원문항처럼 • 표시
for t in "BCDEF":
    lines = V(2, 22, t)["passage"].split("\n")
    F(2, 22, t, st="R", p="\n".join("• " + x for x in lines), s="발문이 ‘첫째는 지금과 다른 과거의 지속적인 상태, 둘째는 과거의 반복 행동’이라고 used to의 쓰임을 알려 주어, 원문항 발문 ‘빈칸에 공통으로 들어갈 말’로 되돌리고 원문항처럼 문장 앞에 • 표시를 붙였다. 첫째 문장이 과거의 상태라 would는 들어갈 수 없으므로 조건이 없어도 정답은 하나다.")

# 2-24 can't be: 원문항처럼 확신 정도가 다른 해석을 보기로
R24 = "조동사 표현 can't(cannot) be: ‘~일 리가 없다’는 강한 부정 추측이다. must be(틀림없이 ~이다), may be(~일지도 모른다)와 확신의 정도가 다르고, 금지·바람의 뜻과도 구별한다."
S24 = "원문항 보기는 같은 문장을 확신 정도만 달리해 해석한 것인데, 변형 오답은 ‘허락 요청’, ‘과거 습관’, ‘금지’처럼 무관한 설명이라 대화 내용을 언급한 보기만 골라도 풀렸고, 오답 네 개가 유형마다 같았다. 원문항처럼 확신 정도가 다른 해석으로 보기를 새로 썼다."
MUST, MAYB, CANT, WANT = "강한 긍정 추측(must be)으로, 강한 부정 추측과 반대이므로", "약한 추측(may be)으로, ‘~일 리 없다’는 강한 부정과 확신의 정도가 다르므로", "‘~일 리가 없다’는 강한 부정 추측(can't be)을 바르게 해석했으므로", "바람을 나타내는 해석으로, 추측의 뜻이 아니므로"
mk(2, 24, "B", [("외계인을 만났다는 말은 틀림없이 사실이다.", MUST), ("외계인을 만났다는 말은 사실일지도 모른다.", MAYB), ("외계인을 만났다는 말은 사실일 리가 없다.", CANT),
                ("외계인을 만났다는 말이 사실이었으면 좋겠다.", WANT), ("외계인을 만났다는 말은 사실일 가능성이 꽤 높다.", "사실일 가능성이 높다는 긍정 쪽 추측(probably)으로, 강한 부정 추측과 다르므로")], 3, R24, S24,
   k="밑줄 친 That can't be true.는 ‘그건 사실일 리가 없다’는 강한 부정 추측이다.")
mk(2, 24, "C", [("그가 진지하게 한 말일 수도 있다.", "가능성을 인정하는 추측(could be)으로, 강한 부정 추측과 다르므로"), ("그는 틀림없이 진지하게 말하고 있다.", MUST),
                ("그가 진지하게 말해서는 안 된다.", "금지(must not)의 해석으로, 추측의 뜻이 아니므로"), ("그가 진지하게 말하고 있는지 알고 싶다.", "궁금함을 나타내는 해석으로, 추측의 뜻이 아니므로"),
                ("그가 진지하게 말하고 있을 리가 없다.", "‘진지할 리가 없다(농담이겠지)’는 강한 부정 추측(can't be)을 바르게 해석했으므로")], 5, R24,
   S24 + " 어색한 ‘It cannot be possible.’을 ‘He can't be serious.’로 바꿨다.",
   p="Tom: Leo says he finished 500 pages in ten minutes.\nJane: <u>He can't be serious.</u>", k="밑줄 친 He can't be serious.는 ‘그가 진지할 리가 없다(농담이겠지)’는 강한 부정 추측이다.")
mk(2, 24, "D", [("빈집에 사람이 가득하다는 말은 맞을 리가 없다.", CANT), ("빈집에 사람이 가득하다는 말은 맞는 것이 분명하다.", MUST), ("빈집에 사람이 가득하다는 말이 맞았으면 좋겠다.", WANT),
                ("빈집에 사람이 가득하다는 말은 맞을 수도 있다.", "가능성을 인정하는 추측(could be)으로, 강한 부정 추측과 다르므로"), ("빈집에 사람이 가득한지 확인할 필요가 없다.", "불필요(don't have to)의 해석으로, 추측의 뜻이 아니므로")], 1, R24, S24,
   k="밑줄 친 That can't be right.는 ‘그 말이 맞을 리가 없다’는 강한 부정 추측이다.")
mk(2, 24, "E", [("해가 서쪽에서 떴다는 것은 아마 사실일 것이다.", "긍정 쪽 추측(probably)으로, 강한 부정 추측과 반대이므로"), ("해가 서쪽에서 떴다는 것은 결코 사실일 수 없다.", CANT),
                ("해가 서쪽에서 떴다는 말을 믿어서는 안 된다.", "금지(must not)의 해석으로, 추측의 뜻이 아니므로"), ("해가 서쪽에서 떴는지 궁금하다.", "궁금함을 나타내는 해석으로, 추측의 뜻이 아니므로"),
                ("해가 서쪽에서 떴을 가능성도 조금은 있다.", "약한 가능성을 인정하는 해석으로, ‘~일 리 없다’는 강한 부정과 확신의 정도가 다르므로")], 2, R24, S24,
   k="밑줄 친 It cannot be true.는 ‘그것은 사실일 리가 없다’는 강한 부정 추측이다.")
mk(2, 24, "F", [("그가 전혀 잠을 자지 않는다는 말은 사실일지도 모른다.", MAYB), ("그가 전혀 잠을 자지 않는다는 말은 틀림없이 사실이다.", MUST), ("그가 전혀 잠을 자지 않았으면 좋겠다.", WANT),
                ("그가 전혀 잠을 자지 않는다는 말은 사실일 리가 없다.", CANT), ("그가 잠을 자지 않아도 된다는 뜻이다.", "불필요(don't have to)의 해석으로, 추측의 뜻이 아니므로")], 4, R24, S24,
   k="밑줄 친 That can't be true.는 ‘그 말은 사실일 리가 없다’는 강한 부정 추측이다.")

# 2-25 부적합: 원문항 형식(ⓐ~ⓕ 여섯 문장 + 조합)으로 다시 쓰기, 원문항 발문 오류는 '틀린 문장으로만'으로 바로잡음
ST25 = "다음 중 밑줄 친 부분이 어법상 틀린 문장으로만 짝지어진 것은?"
R25 = "조동사(can, may, must, should, will) 뒤에는 동사원형을 쓰고, 조동사 두 개를 겹쳐 쓰지 않는다(will can → will be able to). have to·be going to·be able to의 to 뒤에도 동사원형을 쓰며, do/does/did 의문문의 본동사도 원형이다."
S25 = "원문항은 밑줄 친 조동사 표현 여섯 문장에서 조합을 고르는 문항인데, 변형은 발문이 뜻을 알려 주는 빈칸 하나 채우기로 형식이 바뀌었다. 원문항과 같은 형식(ⓐ~ⓕ 여섯 문장, 조합 보기 다섯 개)으로 다시 썼다. 원문항은 발문(옳은 문장으로만)과 정답(틀린 문장 ⓑ, ⓕ)이 어긋나므로, 원문항 정답에 맞춰 발문을 ‘틀린 문장으로만 짝지어진 것’으로 바로잡았다."
def f25(t, lines, judge, wrong, c, a):
    F(2, 25, t, st=ST25, p="\n".join(lines), c=c, a=a, r=R25, pre=["문장별 판정: " + j for j in judge], k=f"틀린 문장은 {wrong}이고, 이 둘로만 짝지어진 보기가 정답이다.",
      n=setnotes(c, wrong, "틀린 문장"), s=S25 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f25("B", ["ⓐ You <u>don't have to bring</u> your own towel.", "ⓑ She <u>must finishes</u> the report by noon.", "ⓒ We <u>were able to catch</u> the last train.",
          "ⓓ <u>Do</u> you <u>can swim</u> across the river?", "ⓔ He <u>is going to visit</u> his uncle this weekend.", "ⓕ You <u>had better not stay</u> up late."],
    ["ⓐ O. 불필요를 나타내는 don't have to + 동사원형이다.", "ⓑ X. 조동사(must) 뒤에는 동사원형을 쓴다. 교정문: She must finish the report by noon.", "ⓒ O. 과거의 능력을 나타내는 were able to + 동사원형이다.",
     "ⓓ X. 조동사(can)가 있는 의문문은 조동사를 주어 앞에 두며 do를 함께 쓰지 않는다. 교정문: Can you swim across the river?", "ⓔ O. 예정을 나타내는 be going to + 동사원형이다.", "ⓕ O. had better의 부정은 had better not + 동사원형이다."],
    "ⓑ, ⓓ", ["ⓐ, ⓒ", "ⓑ, ⓓ", "ⓑ, ⓔ", "ⓒ, ⓕ", "ⓓ, ⓕ"], 2)
f25("C", ["ⓐ It <u>may snow</u> tonight.", "ⓑ All passengers <u>must wear</u> a seat belt.", "ⓒ I <u>will can help</u> you tomorrow.",
          "ⓓ They <u>didn't have to wait</u> long.", "ⓔ <u>Does</u> he <u>has to</u> work this Sunday?", "ⓕ We <u>are going to have</u> a party."],
    ["ⓐ O. 추측을 나타내는 may + 동사원형이다.", "ⓑ O. 의무를 나타내는 must + 동사원형이다.", "ⓒ X. 조동사 두 개를 겹쳐 쓸 수 없다. 교정문: I will be able to help you tomorrow.",
     "ⓓ O. 과거의 불필요를 나타내는 didn't have to + 동사원형이다.", "ⓔ X. 조동사(Does) 뒤에는 원형(have)을 쓴다. 교정문: Does he have to work this Sunday?", "ⓕ O. 예정을 나타내는 be going to + 동사원형이다."],
    "ⓒ, ⓔ", ["ⓐ, ⓒ", "ⓑ, ⓓ", "ⓒ, ⓕ", "ⓓ, ⓔ", "ⓒ, ⓔ"], 5)
f25("D", ["ⓐ <u>May</u> I <u>use</u> your phone for a moment?", "ⓑ He <u>has to leaves</u> early today.", "ⓒ You <u>should not touch</u> the paintings.",
          "ⓓ She <u>could speak</u> French when she was ten.", "ⓔ We <u>are going to moving</u> next month.", "ⓕ Tom <u>was able to solve</u> the puzzle."],
    ["ⓐ O. 허락 요청을 나타내는 May I + 동사원형이다.", "ⓑ X. have to 뒤에는 동사원형을 쓴다. 교정문: He has to leave early today.", "ⓒ O. 충고를 나타내는 should not + 동사원형이다.",
     "ⓓ O. 과거의 능력을 나타내는 could + 동사원형이다.", "ⓔ X. be going to 뒤에는 동사원형을 쓴다. 교정문: We are going to move next month.", "ⓕ O. 과거의 능력을 나타내는 was able to + 동사원형이다."],
    "ⓑ, ⓔ", ["ⓑ, ⓔ", "ⓐ, ⓑ", "ⓒ, ⓔ", "ⓓ, ⓕ", "ⓑ, ⓒ"], 1)
f25("E", ["ⓐ <u>Did</u> you <u>could find</u> the key?", "ⓑ You <u>have to show</u> your ticket at the gate.", "ⓒ You <u>must not run</u> in the hallway.",
          "ⓓ She <u>should to call</u> her mom tonight.", "ⓔ It <u>might be</u> cold tomorrow morning.", "ⓕ We <u>won't be able to come</u> to the party."],
    ["ⓐ X. 조동사(could)가 있는 의문문에는 did를 함께 쓰지 않는다. 교정문: Could you find the key? (또는 Were you able to find the key?)", "ⓑ O. 의무를 나타내는 have to + 동사원형이다.",
     "ⓒ O. 금지를 나타내는 must not + 동사원형이다.", "ⓓ X. 조동사(should) 뒤에는 to 없이 동사원형을 쓴다. 교정문: She should call her mom tonight.",
     "ⓔ O. 추측을 나타내는 might + 동사원형이다.", "ⓕ O. 미래의 불가능을 나타내는 won't be able to + 동사원형이다."],
    "ⓐ, ⓓ", ["ⓑ, ⓒ", "ⓐ, ⓔ", "ⓐ, ⓓ", "ⓓ, ⓕ", "ⓒ, ⓔ"], 3)
f25("F", ["ⓐ When my father was young, he <u>could run</u> very fast.", "ⓑ You <u>must be</u> tired after the long trip.", "ⓒ <u>Are</u> you <u>going to join</u> the club?",
          "ⓓ Jane <u>had to returned</u> the book.", "ⓔ We <u>will able to finish</u> it soon.", "ⓕ You <u>don't need to worry</u> about it."],
    ["ⓐ O. 과거의 능력을 나타내는 could + 동사원형이다.", "ⓑ O. 강한 추측을 나타내는 must be이다.", "ⓒ O. 예정을 묻는 be going to 의문문이다.",
     "ⓓ X. had to 뒤에는 동사원형을 쓴다. 교정문: Jane had to return the book.", "ⓔ X. will 뒤에 able을 바로 쓸 수 없고 be able to로 쓴다. 교정문: We will be able to finish it soon.", "ⓕ O. 불필요를 나타내는 don't need to + 동사원형이다."],
    "ⓓ, ⓔ", ["ⓐ, ⓓ", "ⓒ, ⓔ", "ⓑ, ⓕ", "ⓓ, ⓔ", "ⓐ, ⓔ"], 4)

# 2-26 had better: 원문항처럼 형태 오류를 오답으로
R26 = "had better + 동사원형은 ‘~하는 편이 좋겠다’는 강한 충고이다. had를 have·has로 바꾸거나 better와 순서를 바꾸지 않고, 뒤에 to를 붙이지 않는다. 부정은 had better not + 동사원형이다."
S26 = "발문이 ‘좋지 않은 결과를 피하려면 … 하는 것이 좋겠다’고 뜻을 알려 주고, 오답이 뜻이 다른 표현(used to, would like to)이라 평가 요소가 형태에서 의미로 바뀌었다. 발문을 원문항과 같게 하고, 원문항처럼 had better의 형태 오류를 오답으로 썼다."
OK26 = "had better + 동사원형의 바른 형태로 충고를 나타내므로"
mk(2, 26, "B", [("has better", "has better: had better의 had는 주어와 관계없이 형태가 바뀌지 않으므로"), ("had better", OK26), ("had better to", "had better to: had better 뒤에는 to 없이 동사원형을 쓰므로"),
                ("better had", "better had: had와 better의 순서가 바뀌었으므로"), ("have to better", "have to better: have to와 better를 섞은 틀린 형태이므로")], 2, R26, S26, st="R")
mk(2, 26, "C", [("had to better", "had to better: had to와 better를 섞은 틀린 형태이므로"), ("have better", "have better: had better의 had를 현재형으로 바꿀 수 없으므로"), ("better had to", "better had to: 순서가 바뀌고 to까지 붙은 틀린 형태이므로"),
                ("had better", OK26), ("having better", "having better: had better는 -ing 형태로 쓰지 않으므로")], 4, R26, S26, st="R")
mk(2, 26, "D", [("had better", OK26), ("better have", "better have: had better의 순서를 바꾸고 had를 현재형으로 써 틀렸으므로"), ("has to better", "has to better: has to와 better를 섞은 틀린 형태이므로"),
                ("have better to", "have better to: had를 현재형으로 바꾸고 to까지 붙인 틀린 형태이므로"), ("had better to", "had better to: had better 뒤에는 to 없이 동사원형을 쓰므로")], 1, R26, S26, st="R")
mk(2, 26, "E", [("had better not to", "had better not to: not 뒤에는 to 없이 동사원형을 쓰므로"), ("not had better", "not had better: not을 맨 앞에 둘 수 없으므로"), ("had better don't", "had better don't: had better 뒤 부정은 not + 동사원형으로 쓰므로"),
                ("have better not", "have better not: had better의 had를 현재형으로 바꿀 수 없으므로"), ("had better not", "had better not + 동사원형의 바른 부정 형태로 ‘가까이 가지 않는 편이 좋겠다’는 충고를 나타내므로")], 5, R26,
   S26 + " 다른 유형과 겹치지 않게 부정형 had better not을 묻도록 빈칸 뒤를 ‘go near it’으로 바꿨다.", st="R", p="That dog looks angry. You ________ go near it.")
mk(2, 26, "F", [("would better", "would better: had better의 had를 would로 바꿀 수 없으므로"), ("should better", "should better: should와 better를 이어 쓰는 표현은 없으므로"), ("had better", OK26),
                ("had better to", "had better to: had better 뒤에는 to 없이 동사원형을 쓰므로"), ("better had", "better had: had와 better의 순서가 바뀌었으므로")], 3, R26, S26, st="R")

# 2-28 과거의 의무·조동사 + 원형: 짝 문장을 없애고 유형마다 오답 새로
R28 = "조동사는 가능성·허가·의무·금지·추측을 나타내며, 조동사 뒤에는 동사원형을 쓴다. must는 과거형이 없으므로 과거의 의무는 had to로 나타낸다."
S28 = "틀린 문장과 같은 내용의 옳은 문장이 짝을 이뤄(musted submit ↔ had to submit 등) 대비 단서가 되었고, 오답 네 문장이 유형마다 같았다. 짝 문장을 없애고 유형마다 오답 문장을 새로 썼다."
mk(2, 28, "B", [("I had to wait an hour for the doctor.", "과거의 의무를 had to + 동사원형으로 바르게 나타냈으므로"), ("We didn't have to wear school uniforms last year.", "과거의 불필요를 didn't have to + 동사원형으로 바르게 나타냈으므로"),
                ("They musted leave before sunset.", "must는 과거형이 없다. 과거의 의무는 had to로 나타내야 한다(They had to leave before sunset). 어법상 틀린 문장이므로"),
                ("You will have to show your passport.", "미래의 의무를 will have to + 동사원형으로 바르게 나타냈으므로"), ("Why did she have to go home early?", "did 의문문에서 have to를 원형으로 바르게 썼으므로")], 3, R28, S28)
mk(2, 28, "C", [("Jane can sing beautifully.", "능력을 나타내는 can + 동사원형이 바르므로"), ("He must see a doctor now.", "의무를 나타내는 must + 동사원형이 바르므로"), ("Mina has to practice every day.", "3인칭 단수 주어에 맞춘 has to + 동사원형이 바르므로"),
                ("They may come to the party.", "추측을 나타내는 may + 동사원형이 바르므로"), ("We must to finish the project today.", "조동사(must) 뒤에는 to 없이 동사원형을 쓴다(We must finish …). 어법상 틀린 문장이므로")], 5, R28, S28)
mk(2, 28, "D", [("Tom may to come later.", "조동사(may) 뒤에는 to 없이 동사원형을 쓴다(Tom may come later). 어법상 틀린 문장이므로"), ("You should wear a helmet.", "충고를 나타내는 should + 동사원형이 바르므로"),
                ("She could solve the problem easily.", "과거의 능력을 나타내는 could + 동사원형이 바르므로"), ("I will be able to help you.", "미래의 능력을 will be able to + 동사원형으로 바르게 나타냈으므로"),
                ("We had to stay home because of the storm.", "과거의 의무를 had to + 동사원형으로 바르게 나타냈으므로")], 1, R28, S28)
mk(2, 28, "E", [("Do we have to bring our lunch?", "do 의문문에서 have to + 동사원형을 바르게 썼으므로"), ("They should studies harder.", "조동사(should) 뒤에는 동사원형을 쓴다(They should study harder). 어법상 틀린 문장이므로"),
                ("Mom might be at the store.", "추측을 나타내는 might + 동사원형이 바르므로"), ("You must not tell anyone.", "금지를 나타내는 must not + 동사원형이 바르므로"), ("He was able to fix the car.", "과거의 능력을 was able to + 동사원형으로 바르게 나타냈으므로")], 2, R28, S28)
mk(2, 28, "F", [("Can you help me with this box?", "요청을 나타내는 Can you + 동사원형이 바르므로"), ("She doesn't have to cook tonight.", "불필요를 나타내는 doesn't have to + 동사원형이 바르므로"), ("We would often play in the park.", "과거의 반복 행동을 나타내는 would + 동사원형이 바르므로"),
                ("I could went there alone.", "조동사(could) 뒤에는 동사원형을 쓴다(I could go there alone). 어법상 틀린 문장이므로"), ("You had better take a taxi.", "충고를 나타내는 had better + 동사원형이 바르므로")], 4, R28, S28)

# 2-29 would → used to 근거: 원문항 발문, 그럴듯한 오개념 오답을 유형마다 새로
R29 = "used to + 동사원형은 지금과 다른 과거의 상태나 습관을 나타낸다. 과거 습관의 would는 반복된 동작에만 쓰고 과거의 상태(be, have, stand 등)에는 쓰지 않는다. would에는 가정·미래 등 다른 용법도 있으므로 문맥 없이 언제나 비문이라고 단정하지 않는다."
S29 = "발문이 ‘지금과 다른 과거의 지속적인 상태를 회상할 때’라고 판단 근거를 알려 주었고, 오답(used to 뒤 -ing, 미래 계획 등)이 뻔했으며 선택지 다섯 개가 유형마다 같았다. 발문을 원문항과 같게 하고, 원문항처럼 would와 used to의 차이에 대한 그럴듯한 오개념으로 오답을 유형마다 새로 썼다. 과거 문맥이 드러나도록 시점 표현을 덧붙였다."
OKW = "과거의 상태에는 과거 습관의 would를 쓸 수 없다는 핵심 근거를 정확히 설명했으므로"
mk(2, 29, "B", [("과거 습관의 조동사(would)는 사람이 주어일 때만 쓰고, 사물이 주어인 문장에는 쓸 수 없기 때문이다.", "과거 습관의 would는 사물 주어에도 쓸 수 있고, 고쳐야 하는 까닭은 주어가 아니라 ‘상태’라는 점이므로"),
                ("과거 습관의 조동사(would)는 과거에 반복된 동작에 쓰고, 분수대가 있었던 것과 같은 과거의 상태에는 쓰지 않기 때문이다.", OKW),
                ("used to 구문은 지금도 그 상태가 이어지고 있음을 나타내 더 정확하기 때문이다.", "used to 구문은 오히려 지금은 그렇지 않은 과거의 상태를 나타내므로"),
                ("There로 시작하는 문장에는 조동사를 쓸 수 없기 때문이다.", "There will be …처럼 There 구문에도 조동사를 쓸 수 있으므로"),
                ("과거 습관의 조동사(would)는 먼 과거에, used to 구문은 가까운 과거에만 쓰기 때문이다.", "두 표현은 과거가 먼지 가까운지로 구별하지 않으므로")], 2, R29, S29,
   st="R", p="There ⒜<u>would be</u> a fountain in this square years ago.\n→ ⒝<u>used to be</u>")
mk(2, 29, "C", [("소유를 뜻하는 동사(have)는 조동사와 함께 쓸 수 없기 때문이다.", "소유의 have도 조동사 뒤에 쓸 수 있으므로(will have, must have 등)"),
                ("주어(My town)가 3인칭 단수이므로 would 대신 used to 구문을 써야 하기 때문이다.", "would와 used to 구문은 주어의 인칭·수와 관계없이 형태가 같으므로"),
                ("조동사(would)는 부정문과 의문문에서만 과거 습관을 나타내기 때문이다.", "과거 습관의 would는 긍정문에도 쓰이므로"),
                ("정류장이 하나뿐이었던 것은 과거의 상태이고, 과거의 상태는 조동사(would)가 아니라 used to 구문으로 나타내기 때문이다.", OKW),
                ("used to 구문은 과거에 딱 한 번 일어난 일을 나타내기 때문이다.", "used to 구문은 한 번의 일이 아니라 과거에 지속된 상태나 반복된 습관을 나타내므로")], 4, R29, S29,
   st="R", p="My town ⒜<u>would have</u> only one bus stop in the 1990s.\n→ ⒝<u>used to have</u>")
mk(2, 29, "D", [("조동사(would) 뒤에는 be동사가 올 수 없기 때문이다.", "would be처럼 조동사 뒤에 be동사를 쓸 수 있으므로"),
                ("조동사(would)는 미래 조동사(will)의 과거형이라 과거의 일에는 쓸 수 없기 때문이다.", "would는 과거의 반복된 동작에 쓸 수 있으므로"),
                ("be동사의 과거 상태는 used to 구문으로, 일반동사의 과거 상태는 조동사(would)로 나타내기 때문이다.", "일반동사가 나타내는 과거 상태(have, live 등)도 would가 아니라 used to 구문으로 나타내므로"),
                ("주어가 사람이면 과거 습관을 반드시 used to 구문으로 나타내야 하기 때문이다.", "사람 주어의 과거 습관에도 would를 쓸 수 있으므로"),
                ("수줍음을 많이 탔던 것은 반복된 동작이 아니라 과거의 상태이므로, 상태까지 나타낼 수 있는 used to 구문을 써야 하기 때문이다.", OKW)], 5, R29, S29, st="R")
mk(2, 29, "E", [("길이 더 좁았던 것은 과거의 상태이고, 조동사(would)는 과거에 반복된 행동에만 쓰기 때문이다.", OKW),
                ("비교급(narrower)이 있는 문장에는 조동사를 쓸 수 없기 때문이다.", "비교급이 있어도 조동사를 쓸 수 있으므로"),
                ("조동사(would)는 공손한 요청에만 쓰여 평서문에는 쓸 수 없기 때문이다.", "would는 과거 습관·가정 등 평서문에도 널리 쓰이므로"),
                ("과거 시점 표현(ten years ago)이 있으면 조동사를 쓰지 않고 used to 구문만 써야 하기 때문이다.", "과거 시점 표현이 있어도 과거의 반복 동작에는 would를 쓸 수 있고, 고쳐야 하는 까닭은 ‘상태’라는 점이므로"),
                ("조동사(would)를 사물 주어와 함께 쓰면 수동의 뜻이 되기 때문이다.", "would는 주어에 따라 수동의 뜻이 되지 않으므로")], 1, R29, S29,
   st="R", p="This road ⒜<u>would be</u> much narrower ten years ago.\n→ ⒝<u>used to be</u>")
mk(2, 29, "F", [("자동사(stand)는 조동사(would) 뒤에 올 수 없기 때문이다.", "자동사도 조동사 뒤에 동사원형으로 쓸 수 있으므로"),
                ("There 구문은 과거완료 시제로만 과거의 상태를 나타내기 때문이다.", "There 구문의 과거 상태는 There was/were나 There used to be로 나타내므로"),
                ("나무가 서 있었던 것은 과거에 지속된 상태이므로, 과거의 반복 동작에 쓰는 조동사(would)로는 나타낼 수 없기 때문이다.", OKW),
                ("used to 구문 뒤에는 동사원형이 아닌 과거형이 와야 과거의 뜻이 되기 때문이다.", "used to 뒤에는 언제나 동사원형을 쓰므로"),
                ("조동사(would)는 상상이나 가정을 나타낼 때만 쓰이고 과거의 일에는 전혀 쓰이지 않기 때문이다.", "would는 과거의 반복된 동작에도 쓰이므로")], 3, R29,
   S29 + " ⒜와 ⒝의 동사가 달랐던(would stand → used to be) 것을 같은 동사(stand)로 맞췄다.",
   st="R", p="There ⒜<u>would stand</u> an old tree here long ago.\n→ ⒝<u>used to stand</u>")

# 2-30 used to 세 구조: 학생 설명 다섯 개를 유형마다 새로, 틀린 설명의 오개념도 다르게
R30 = "used to + 동사원형은 과거의 상태·습관(지금은 아님)이다. be used + to부정사는 ‘~하는 데 사용되다’라는 수동태와 목적이며, be used to + 명사/동명사는 ‘~에 익숙하다’이다."
def f30(t, items, a, s):
    F(2, 30, t, c=[x for x, _ in items], a=a, r=R30, n=[w + (" 틀린 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.") for i, (_, w) in enumerate(items)],
      k=f"설명이 틀린 학생은 {items[a-1][0].split(':')[0]}이다. {items[a-1][1]}", s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
S30 = "옳은 설명 네 개(준·민지·태호·수아)가 B와 똑같았다. 유형마다 학생 이름과 설명 다섯 개를 새로 쓰고, 틀린 설명도 다른 오개념으로 바꿨다."
f30("B", [("준: (A)는 예전에는 자전거로 등교했지만 지금은 그렇지 않다는 뜻이야.", "(A)는 과거의 습관을 나타내며 지금은 그렇지 않음을 뜻한다."),
          ("태호: (C)의 to는 전치사라서 뒤에 동명사(getting)가 왔어.", "(C)는 be used to + 동명사이며, 이때 to는 전치사이다."),
          ("민지: (B)는 ‘빵을 자르는 데 익숙하다’는 뜻이야.", "(B)는 be used + to부정사로 ‘빵을 자르는 데 사용된다’는 뜻이다. ‘익숙하다’는 be used to + 명사/동명사일 때의 뜻이다."),
          ("수아: (B)의 to cut은 ‘~하기 위해’라는 목적을 나타내.", "(B)의 to부정사는 칼이 사용되는 목적(용도)을 나타낸다."),
          ("다은: (C)는 일찍 일어나는 것이 익숙하다는 뜻이야.", "(C)는 be used to + 동명사로 익숙함을 나타낸다.")], 3,
    "틀린 설명(‘(A)와 (C)는 둘 다 ~하곤 했다’)이 원문항 정답(④ (A)와 (C)는 같은 의미)과 같은 내용이었다. 학생 설명을 새로 쓰고, 틀린 설명을 ‘(B)를 익숙함으로 해석’하는 다른 오개념으로 바꿨다.")
f30("C", [("서준: (A)는 과거에는 대구에 살았지만 지금은 살지 않는다는 뜻이야.", "(A)는 지금과 다른 과거의 상태를 나타낸다."),
          ("하린: (B)는 ‘사용되다’라는 뜻의 수동태 문장이야.", "(B)는 be used(수동태) + to부정사 구조이다."),
          ("도윤: (C)는 밤에 일하는 것에 익숙하다는 뜻이야.", "(C)는 be used to + 동명사로 익숙함을 나타낸다."),
          ("예린: (B)의 to부정사는 방이 어떤 용도로 쓰이는지를 나타내.", "(B)의 to부정사는 방이 사용되는 목적(용도)을 나타낸다."),
          ("시우: (C)의 working을 work로 바꿔도 뜻이 같아.", "(C)의 to는 전치사이므로 뒤에 동사원형을 쓸 수 없다. work로 바꾸면 어법상 틀린 문장이 된다.")], 5, S30)
f30("D", [("지호: (B)에 쓰인 동사 형태(used)는 과거형이라서 (B)는 과거의 일을 말하고 있어.", "(B)의 used는 수동태(is used)의 과거분사이며, (B)는 현재의 용도를 말한다."),
          ("유나: (A)는 과거에 밖에서 자주 놀았던 습관을 나타내.", "(A)는 used to + 동사원형으로 과거의 습관을 나타낸다."),
          ("건우: (B)는 ‘이 솔은 병을 씻는 데 사용된다’는 뜻이야.", "(B)는 be used + to부정사로 사용되는 목적을 나타낸다."),
          ("소연: (C)의 to 뒤에는 명사나 동명사가 와야 해.", "(C)의 to는 전치사이므로 명사나 동명사가 온다."),
          ("현우: (A)의 used to 대신 would를 써도 뜻이 크게 달라지지 않아.", "(A)는 반복된 동작(밖에서 놀기)이므로 과거 습관의 would로도 나타낼 수 있다.")], 1, S30)
f30("E", [("은서: (A)를 보면 미나는 지금은 머리가 길지 않다고 짐작할 수 있어.", "used to는 지금과 다른 과거의 상태를 나타내므로 지금은 머리가 길지 않다고 짐작할 수 있다."),
          ("민재: (A)는 과거의 상태를 나타내는 문장이야.", "(A)의 have long hair는 과거의 상태이다."),
          ("채원: (B)는 사진을 편집하는 데 이 앱이 쓰인다는 뜻이야.", "(B)는 be used + to부정사로 사용되는 목적을 나타낸다."),
          ("지훈: (C)는 be동사 없이 ‘I used to taking the subway.’로 써도 같은 뜻이야.", "be동사를 빼면 used to + 동사원형 구조가 되어야 하므로 taking을 쓸 수 없고, 뜻도 ‘지하철을 타곤 했다’로 달라진다."),
          ("나연: (C)는 지하철을 타는 것이 익숙한 상황이야.", "(C)는 be used to + 동명사로 익숙함을 나타낸다.")], 4, S30)
f30("F", [("태윤: (A)를 보면 아빠는 지금은 담배를 피우지 않는다고 볼 수 있어.", "used to는 지금은 하지 않는 과거의 습관을 나타낸다."),
          ("서아: (B)에서 to부정사를 동명사로 바꿔 ‘is used to making ice’로 써도 뜻이 같아.", "be used to + 동명사는 ‘~에 익숙하다’는 뜻이 되어 ‘얼음을 만드는 데 사용된다’는 뜻과 달라진다."),
          ("준서: (C)는 늦게 먹는 것에 익숙하다는 뜻이야.", "(C)는 be used to + 동명사로 익숙함을 나타낸다."),
          ("하은: (B)는 ‘이 기계는 얼음을 만드는 데 사용된다’는 뜻이야.", "(B)는 be used + to부정사로 사용되는 목적을 나타낸다."),
          ("우진: (A)와 (B)는 같은 단어(used)가 들어 있지만 쓰임이 서로 달라.", "(A)는 과거 습관의 used to, (B)는 수동태 be used + to부정사이다.")], 2, S30)

# ---- 2차 감수(2026-10) 추가 ----
# 2-22 B~F: 없는 형태(uses to) 오답을 실제 조동사로, D~F는 원문항처럼 문맥(but now ~, when ~)을 넣어 문장 길이를 맞춤
R22 = "used to + 동사원형은 지금은 그렇지 않은 과거의 상태와 과거의 반복 행동을 모두 나타낸다. would는 과거의 반복 행동에만 쓰고 상태(be, have, live)에는 쓰지 않는다. be used to + (동)명사는 ‘~에 익숙하다’는 뜻이다."
S22 = "발문이 used to의 쓰임을 알려 주어 원문항 발문으로 되돌리고 문장 앞에 • 표시를 붙였다. 영어에 없는 형태인 오답 uses to는 실제 조동사로 바꿨다."
N22 = {"used to": "첫째 문장의 과거 상태와 둘째 문장의 과거 반복 행동을 모두 나타낼 수 있으므로", "would": "둘째 문장에는 쓸 수 있지만 첫째 문장처럼 과거의 상태를 나타낼 수는 없으므로",
       "was used to": "be used to는 ‘~에 익숙하다’는 뜻이고 뒤에 동사원형이 올 수 없으므로", "is used to": "be used to는 ‘~에 익숙하다’는 뜻이고 뒤에 동사원형이 올 수 없으므로"}
def f22(t, c, a, lines=None, extra=""):
    FIX.pop((2, 22, t), None)
    lines = lines or V(2, 22, t)["passage"].split("\n")
    mk(2, 22, t, [(x, N22.get(x, f"조동사({x})는 과거의 상태나 습관을 나타내지 못해 두 문장의 뜻에 맞지 않으므로")) for x in c], a, R22, S22 + extra, st="R", p="\n".join("• " + x for x in lines))
X22 = " 원문항처럼 과거임을 알려 주는 말(but now ~, when ~)을 넣어 문장 길이를 맞췄다."
f22("B", ["was used to", "would", "used to", "is used to", "should"], 3)
f22("C", ["will", "was used to", "is used to", "would", "used to"], 5, ["This street _____ be very quiet before the new mall opened.", "Jane _____ visit her aunt every summer when she was in elementary school."], X22)
f22("D", ["would", "may", "is used to", "used to", "was used to"], 4, ["Tom _____ have long hair in high school, but now he keeps it short.", "We _____ play outside until dark when we were children."], X22)
f22("E", ["must", "was used to", "would", "used to", "is used to"], 4, ["There _____ be a small theater here, but it closed ten years ago.", "Dad _____ take us fishing on Sundays when we were little."], X22)
f22("F", ["might", "would", "used to", "is used to", "was used to"], 3, ["Mina _____ live in Busan, but now she lives in Seoul.", "She _____ ride her bike to school every day when she was a student."], X22)

# 2-23 C·D·E: 문장이 원문항의 절반 이하로 짧고 Tom'd, Jane'd처럼 어색한 축약 → 길이를 맞추고 대명사 주어로
R23 = "'d는 would 또는 had의 줄임말이다. 'd like to(~하고 싶다)의 'd는 would, 'd better(~하는 게 좋겠다)의 'd는 had다."
S23 = "문장이 원문항의 절반 이하로 짧았고, 고유명사 뒤의 축약(Tom'd, Jane'd)이 어색했다. 문장 길이를 원문항 수준으로 늘리고 주어를 대명사로 바꿨다. 보기와 정답은 그대로다."
S23D = "문장이 원문항의 절반 이하로 짧아 원문항 수준으로 늘렸다. 보기와 정답은 그대로다."
def f23(t, a_line, b_line, s=None):
    v = V(2, 23, t); ans = v["c"][int(v["ans"]) - 1]
    def note(x):
        if x == ans: return "would like(love) to의 'd는 would, had better의 'd는 had이므로"
        return ("(A)의 'd는 would이므로" if "(A) would" not in x else "") + ("" if "(A) would" not in x or "(B) had" in x else "(B)의 'd는 had이므로") if not ("(A) would" not in x and "(B) had" not in x) else "(A)의 'd는 would, (B)의 'd는 had이므로"
    mk(2, 23, t, [(x, note(x)) for x in v["c"]], int(v["ans"]), R23, s or S23, p=f"(A) {a_line}\n(B) {b_line}")
f23("C", "She<u>'d</u> like some hot tea after the long walk.", "He<u>'d</u> better apologize to his sister right now.")
f23("D", "We<u>'d</u> love to join you for dinner tonight.", "You<u>'d</u> better hurry to catch the last bus.", S23D)
f23("E", "He<u>'d</u> like to walk to school with his friends.", "She<u>'d</u> better call the restaurant before leaving.")
