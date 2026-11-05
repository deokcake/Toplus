# 6급 CH10 과거진행형 (91~100) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
R_PP = "과거진행형은 was/were + 동사원형-ing로 과거의 어느 때에 진행 중이던 동작을 나타낸다. I·3인칭 단수 주어에는 was, you·복수 주어에는 were를 쓰고, 부정문은 was/were 뒤에 not, 의문문은 Was/Were를 주어 앞에 둔다."

# 원문항 발문으로만 되돌리는 문항
for t in "BCDEF": F(6, 92, t, st="R", s="발문에 ‘“~하고 있었다”를 과거진행형으로’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "CEF": F(6, 96, t, st="R", s="발문에 ‘과거에 진행 중이던 동작을 나타내도록 … be동사’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "DE": F(6, 97, t, st="R", s="발문에 ‘부정으로 짧게 답한 뒤 … 두 빈칸을 과거형으로’가 붙었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
for t in "BCDE": F(6, 100, t, st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 6-91 -ing형 짝: 81번과 다른 동사로 유형마다 새로
R691 = "-ing형은 대부분 동사원형에 -ing를 붙인다. -e로 끝나면 e를 빼고, -ie로 끝나면 ie를 y로 바꾸며, 강세 있는 단모음 + 단자음으로 끝나면 자음을 한 번 더 쓴다. 모음이 두 개인 wait, -ee로 끝나는 see, y로 끝나는 enjoy·carry·fly는 그대로 -ing를 붙인다."
S691 = "옳은 짝 오답 네 개(sit, write, play, study)가 유형마다 같았고, 정답 짝(run, swim, lie, make)이 6급 81번 변형 정답과 겹쳤다. 81번과 다른 동사로 옳은 짝과 정답 짝을 유형마다 새로 썼다."
E_ = "-e로 끝나 e를 빼고 -ing를 바르게 붙였으므로"; DB = "단모음 + 단자음으로 끝나 자음을 한 번 더 쓰고 -ing를 바르게 붙였으므로"; PL = "그대로 -ing를 바르게 붙였으므로"; IE = "-ie로 끝나 ie를 y로 바꾸고 -ing를 바르게 붙였으므로"
def f691(t, items, a, s=S691):
    mk(6, 91, t, items, a, R691, s)
f691("B", [("hit - hitting", DB), ("smile - smiling", E_), ("drive - driveing", "-e로 끝나 e를 빼고 driving으로 써야 하므로"), ("sleep - sleeping", PL), ("plan - planning", DB)], 3)
f691("D", [("die - dieing", "-ie로 끝나 ie를 y로 바꾸고 dying으로 써야 하므로"), ("put - putting", DB), ("hope - hoping", E_), ("enjoy - enjoying", "모음 + y로 끝나 그대로 -ing를 바르게 붙였으므로"), ("get - getting", DB)], 1)
f691("E", [("wait - waiting", "모음 두 개 뒤의 자음이라 겹치지 않고 -ing를 바르게 붙였으므로"), ("ride - riding", E_), ("tie - tying", IE), ("fly - flying", "y로 끝나도 그대로 -ing를 바르게 붙였으므로"), ("stop - stoping", "단모음 + 단자음으로 끝나 p를 겹쳐 stopping으로 써야 하므로")], 5)
f691("F", [("begin - beginning", "강세 있는 단모음 + 단자음으로 끝나 n을 겹쳐 -ing를 바르게 붙였으므로"), ("carry - carrying", "y로 끝나도 그대로 -ing를 바르게 붙였으므로"), ("shop - shopping", DB), ("come - comeing", "-e로 끝나 e를 빼고 coming으로 써야 하므로"), ("see - seeing", "-ee로 끝나면 e를 빼지 않고 -ing를 바르게 붙였으므로")], 4)

# 6-93 두 빈칸: 원문항 발문, 괄호 동사 삭제, 조건 없이도 답이 하나로
S693 = "발문이 ‘첫 문장은 과거진행형 부정문, 둘째 문장은 과거진행형 긍정 의문문’이라고 정답 형태를 알려 주고 괄호로 동사까지 주었다. 원문항 발문으로 되돌리고 괄호 동사를 지웠다."
for t in "BDE":
    F(6, 93, t, st="R", p=re.sub(r" \([a-z]+\)", "", V(6, 93, t)["passage"]), s=S693 + " 보기와 정답은 그대로다.")
def f693(t, p, items, a, s=S693):
    mk(6, 93, t, items, a, R_PP, s, st="R", p=p, okdup=True)
f693("C", "- Tom _______ reading a book.\n- Was he ________ quietly?", [("was not - read", "둘째 빈칸: Was 뒤에는 -ing형 reading을 써야 하므로"), ("were not - reading", "첫째 빈칸: 3인칭 단수 주어 Tom에는 was not을 써야 하므로"), ("wasn't - reads", "둘째 빈칸: Was 뒤에는 -ing형 reading을 써야 하므로"),
     ("did not - reading", "첫째 빈칸: 진행형 부정문에는 did not이 아니라 was not을 써야 하므로"), ("was not - reading", "Tom에 was not, Was he 뒤에 reading을 바르게 썼으므로")], 5,
     S693 + " 괄호 없이는 문장과 관계없는 동사(play, playing)도 들어갈 수 있어, 오답을 read의 다른 형태로 바꿨다.")
f693("F", "- We _______ studying English.\n- Were they ________ together?", [("was not - studying", "첫째 빈칸: 주어 We에는 were not을 써야 하므로"), ("did not - studying", "첫째 빈칸: 진행형 부정문에는 did not이 아니라 were not을 써야 하므로"), ("was not - study", "주어 We에는 were not을 쓰고, Were 뒤에는 studying을 써야 하므로"),
     ("were not - studying", "We에 were not, Were they 뒤에 studying을 바르게 썼으므로"), ("wasn't - studies", "주어 We에는 weren't를 쓰고, Were 뒤에는 studying을 써야 하므로")], 4,
     S693 + " 괄호 없이는 ‘were not - playing’도 답이 될 수 있어, 이 보기를 ‘was not - studying’으로 바꿨다.")

# 6-94 두 빈칸: 원문항 발문, 괄호 동사 삭제, 과거 시간 표현 추가
S694 = "발문이 ‘두 문장을 모두 과거진행형으로’라고 시제를 알려 주고 괄호로 동사를 주었으며, 과거 시간 표현이 없는 문장은 조건이 없으면 현재형도 가능했다. 원문항 발문으로 되돌리고 괄호 동사를 지웠으며, 두 문장에 과거 시간 표현을 넣었다. 보기와 정답은 그대로다."
for t, p in [("B", "- _______ Mina waiting outside at noon yesterday?\n- Her friends ________ in the classroom then."), ("C", "- _______ the dog barking last night?\n- The children ________ near the gate then."),
             ("D", "- _______ Tom cooking at six yesterday?\n- Jane ________ a letter then."), ("E", "- _______ the children sleeping at nine last night?\n- Their father ________ dinner then."),
             ("F", "- _______ she reading when you called?\n- The boys ________ soccer at that time.")]:
    F(6, 94, t, st="R", p=p, s=S694)

# 6-95 다른 하나: 원문항 발문, 유형마다 문장 새로
R695 = "빈칸의 be동사는 주어에 따라 정한다. 3인칭 단수 주어에는 is(과거면 was), you·복수 주어에는 are(과거면 were)를 쓴다."
S695 = "선택지 네 개(Tom sleeping, The dog playing, My brother studying, Jane running)가 유형마다 같아 E는 B와, F는 C와 사실상 같은 문항이었고, 발문에 ‘과거진행형으로 완성할 때’가 붙었다. 원문항 발문으로 되돌리고 유형마다 문장을 새로 썼다."
SG = lambda s_: f"{s_}: 3인칭 단수 주어라 is(과거면 was)가 들어가므로"; PLR = lambda s_: f"{s_}: 복수 주어라 are(과거면 were)가 들어가므로"
def f695(t, items, a, s=S695):
    mk(6, 95, t, items, a, R695, s, st="R")
F(6, 95, "B", st="R", s="발문에 ‘과거진행형으로 완성할 때’가 붙었다. 원문항 발문으로 되돌렸다. 현재·과거 어느 쪽으로 보아도 We만 다른 be동사가 들어가므로 보기와 정답은 그대로다.")
f695("C", [("The girls ________ singing.", PLR("The girls") + " 나머지와 같으므로"), ("My parents ________ talking.", PLR("My parents") + " 나머지와 같으므로"), ("Mina ________ drawing.", SG("Mina") + " 나머지(are)와 다르므로"), ("The kids ________ laughing.", PLR("The kids") + " 나머지와 같으므로"), ("You ________ smiling.", "You: 주어 you에는 are(과거면 were)가 들어가 나머지와 같으므로")], 3,
     S695 + " 원문항과 반대로 복수 주어 네 개 속 단수 주어 하나를 찾게 했다.")
f695("D", [("The boys ________ swimming.", PLR("The boys") + " 나머지(is)와 다르므로"), ("The cat ________ sleeping.", SG("The cat") + " 나머지와 같으므로"), ("Your uncle ________ driving.", SG("Your uncle") + " 나머지와 같으므로"), ("My aunt ________ baking.", SG("My aunt") + " 나머지와 같으므로"), ("The phone ________ ringing.", SG("The phone") + " 나머지와 같으므로")], 1)
f695("E", [("We ________ dancing.", "We: 주어 we에는 are(과거면 were)가 들어가 나머지와 같으므로"), ("The students ________ writing.", PLR("The students") + " 나머지와 같으므로"), ("You and Jiho ________ walking.", PLR("You and Jiho") + " 나머지와 같으므로"), ("Dad ________ fixing the car.", SG("Dad") + " 나머지(are)와 다르므로"), ("The birds ________ singing.", PLR("The birds") + " 나머지와 같으므로")], 4,
     S695 + " 원문항과 반대로 복수 주어 네 개 속 단수 주어 하나를 찾게 했다.")
f695("F", [("The girl ________ reading.", SG("The girl") + " 나머지와 같으므로"), ("The train ________ coming.", SG("The train") + " 나머지와 같으므로"), ("Grandma ________ knitting.", SG("Grandma") + " 나머지와 같으므로"), ("The sun ________ shining.", SG("The sun") + " 나머지와 같으므로"), ("My friends ________ waiting.", PLR("My friends") + " 나머지(is)와 다르므로")], 5)

# 6-96 B·D: 원문항 발문, B는 문장 새로, D는 우리말 해석
F(6, 96, "B", st="R", p="Tom _______ riding his bike at that time.\n(Tom은 그때 자전거를 타고 있었다.)", c=["be", "were", "was", "is", "am"], a=3, r=R_PP,
  n=["be는 원형이라 주어 뒤에 그대로 쓸 수 없으므로 오답이다.", "were는 you·복수 주어에 쓰므로 오답이다.", "3인칭 단수 주어 Tom에 맞는 과거형 was이므로 정답이다.", "at that time(그때)은 과거라 현재형 is를 쓸 수 없으므로 오답이다.", "am은 주어 I에만 쓰는 현재형이므로 오답이다."],
  s="문장이 원문항(Grace ___ walking her dog …)과 명사 하나만 달랐고 발문에 조건이 붙었다. 원문항 발문으로 되돌리고 문장을 새로 썼다. 정답 위치 ③.")
F(6, 96, "D", st="R", p="The twins _______ watching TV at eight last night.\n(쌍둥이는 어젯밤 8시에 TV를 보고 있었다.)", s="발문에 조건이 붙었고, 원문항과 달리 우리말 해석이 없었다. 원문항 발문으로 되돌리고 우리말 해석을 붙였다. 보기와 정답은 그대로다.")

# 6-97 B·C·F: 원문항 발문, 정답 조합을 원문항(wasn't - was)과 다르게
S697 = "정답 조합(wasn't - was)이 원문항과 같았고 발문에 조건이 붙었다. 원문항 발문으로 되돌리고 대답이나 주어를 바꿔 정답 조합이 원문항과 다르게 했다."
def f697(t, p, items, a, s=S697):
    mk(6, 97, t, items, a, R_PP, s, st="R", p=p, okdup=True)
f697("B", "A: Were you studying?\nB: Yes, I ________. I ________ studying for the test.", [("weren't - was", "첫째 빈칸: Yes로 답했고 주어 I에는 was를 쓰므로"), ("was - were", "둘째 빈칸: 주어 I에는 was를 쓰므로"), ("was - was", "Yes, I was.와 I was studying을 바르게 썼으므로"), ("wasn't - was", "첫째 빈칸: Yes로 답했으므로 부정형 wasn't를 쓸 수 없으므로"), ("were - were", "주어 I에는 was를 쓰므로")], 3)
f697("C", "A: Was Tom reading?\nB: No, he ________. His sisters ________ reading.", [("wasn't - were", "he에 wasn't, 복수 주어 His sisters에 were를 바르게 썼으므로"), ("weren't - was", "he에는 wasn't, His sisters에는 were를 쓰므로"), ("wasn't - was", "둘째 빈칸: 복수 주어 His sisters에는 were를 쓰므로"),
     ("was - weren't", "No로 답했으므로 wasn't를 쓰고, 누나들은 읽고 있었으므로 were를 쓰므로"), ("didn't - were", "첫째 빈칸: be동사 과거진행형 질문에는 didn't로 답하지 않으므로")], 1)
f697("F", "A: Were the kids playing outside?\nB: Yes, they ________. Jane ________ playing with them, too.", [("was - were", "they에는 were, 3인칭 단수 Jane에는 was를 쓰므로"), ("weren't - was", "첫째 빈칸: Yes로 답했으므로 부정형 weren't를 쓸 수 없으므로"), ("were - were", "둘째 빈칸: 3인칭 단수 주어 Jane에는 was를 쓰므로"),
     ("did - was", "첫째 빈칸: be동사 과거진행형 질문에는 did로 답하지 않으므로"), ("were - was", "they에 were, Jane에 was를 바르게 썼으므로")], 5)

# 6-98 네 번째 단어: 원문항 발문, 선택지를 주어진 단어만으로
R698 = "과거진행형 의문문은 Was/Were + 주어 + 동사원형-ing + 목적어·부사의 순서로 배열한다."
S698 = "발문에 ‘be동사로 시작하는’, ‘(한 어구는 하나의 요소로 센다.)’가 붙었고, ‘were studying’, ‘?’ 같은 묶음·기호가 선택지에 들어갔다. 원문항 발문으로 되돌리고, 원문항처럼 낱단어 다섯 개와 물음표만 주어 선택지를 주어진 단어만으로 바꿨다."
def f698(t, words, sent, opts, a, pos, s=S698):
    notes = [f"단어({w})는 {pos[w.lower()]}번째에 오므로" if w != opts[a-1] else f"단어({w})가 네 번째에 오므로" for w in opts]
    notes = [f"완성 문장 {sent}에서 " + x for x in notes]
    F(6, 98, t, st="R", p=f"( {' / '.join(words)} / ? )", c=opts, a=a, r=R698, k=f"완성 문장은 {sent}이고 네 번째 단어는 {opts[a-1]}이다.",
      n=[x + (" 정답이다." if i + 1 == a else " 오답이다.") for i, x in enumerate(notes)], okdup=True, s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.")
ORD = lambda sent: {w.lower(): i + 1 for i, w in enumerate(sent.rstrip("?").split())}
s_ = "Were you studying English hard?"; f698("B", ["English", "you", "studying", "were", "hard"], s_, ["you", "studying", "were", "English", "hard"], 4, ORD(s_))
s_ = "Were they playing soccer outside?"; f698("C", ["soccer", "they", "playing", "were", "outside"], s_, ["soccer", "they", "were", "playing", "outside"], 1, ORD(s_))
s_ = "Was the girl singing loudly?"; f698("D", ["the", "singing", "was", "girl", "loudly"], s_, ["the", "singing", "was", "girl", "loudly"], 2, ORD(s_),
     S698 + " 문장 구조(Was + 주어 + -ing + a + 명사)와 정답 단어(a)가 원문항과 같아, 두 단어 주어(the girl) 문장으로 바꿨다.")
s_ = "Was Jane cooking dinner then?"; f698("E", ["dinner", "Jane", "cooking", "was", "then"], s_, ["then", "cooking", "was", "Jane", "dinner"], 5, ORD(s_))
s_ = "Was Tom playing the piano?"; f698("F", ["the", "Tom", "playing", "was", "piano"], s_, ["playing", "piano", "the", "Tom", "was"], 3, ORD(s_))

# 6-99 (A)(B): 원문항 발문, 빈칸 밑줄, E는 정답 조합을 새로
S699 = "발문이 ‘과거진행형 긍정 의문문과 그에 대한 직접적인 짧은 대답’이라고 정답 형태를 알려 주었고 빈칸 밑줄이 사라졌다. 원문항 발문으로 되돌리고 빈칸 밑줄을 살렸다."
UB = lambda p: p.replace("(A) ________", "(<u>     A     </u>)").replace("(B) ________", "(<u>     B     </u>)")
for t in "BCDF": F(6, 99, t, st="R", p=UB(V(6, 99, t)["passage"]), s=S699 + " 보기와 정답은 그대로다.")
F(6, 99, "E", st="R", p="A: (<u>     A     </u>) Jane studying with Amy?\nB: No, she (<u>     B     </u>).", c=["Were - weren't", "Was - wasn't", "Is - wasn't", "Was - was", "Were - wasn't"], a=2, r=R_PP,
  n=["3인칭 단수 주어 Jane에는 Was, she에는 wasn't를 쓰므로 오답이다.", "Jane에 Was, No 대답에 she wasn't를 바르게 썼으므로 정답이다.", "현재형 Is로 물으면 wasn't로 답할 수 없으므로 오답이다.", "No로 답했으므로 was가 아니라 wasn't를 써야 하므로 오답이다.", "3인칭 단수 주어 Jane에는 Were가 아니라 Was를 쓰므로 오답이다."],
  s=S699 + " 정답 조합(Were - were)과 문장 구조가 원문항과 같아, 단수 주어의 부정 대답으로 바꿔 정답 조합이 Was - wasn't가 되게 했다. 정답 위치 ②.")

# 6-100 F: B와 거의 같은 글을 새로
F(6, 100, "F", st="R", p="Last Saturday, we went to the beach. ①<u>Was the sun shining</u> brightly? Yes, it was. ②<u>Were the kids building</u> a sandcastle? Yes, they were. ③<u>Was your dad swimming</u> in the sea? No, he was sleeping under an umbrella. ④<u>Were Mom reading</u> a book? Yes, she was. We ⑤<u>were having</u> a great time.",
  c=["Was the sun shining", "Were the kids building", "Was your dad swimming", "Were Mom reading", "were having"], a=4,
  r="밑줄 밖의 주어도 본문에서 찾아 was/were의 수 일치를 확인한다. 3인칭 단수 주어에는 Was, 복수 주어에는 Were를 쓴다.",
  n=["단수 주어 the sun에 Was를 바르게 썼으므로 오답이다.", "복수 주어 the kids에 Were를 바르게 썼으므로 오답이다.", "단수 주어 your dad에 Was를 바르게 썼으므로 오답이다.", "단수 주어 Mom에는 Were가 아니라 Was를 써야 하므로 정답이다.", "주어 We에 were having을 바르게 썼으므로 오답이다."],
  s="글(가족이 부엌에서 일하는 장면)과 밑줄 문장이 B와 거의 같았고 발문이 원문항과 달랐다. 원문항 발문으로 되돌리고 해변에서의 하루로 글을 새로 썼다. 정답 위치 ④.")


# ---- 2차 감수(2026-10) 추가 ----
def redo(n, t, items, a, s, r=R_PP, **kw):
    FIX.pop((6, n, t), None)
    mk(6, n, t, items, a, r, s, **kw)
# 6-93 F: 정답 위치가 원문항·B·D와 모두 ④ → 보기 순서 변경
redo(93, "F", [("was not - studying", "첫째 빈칸: 주어 We에는 were not을 써야 하므로"), ("were not - studying", "We에 were not, Were they 뒤에 -ing형 studying을 바르게 썼으므로"), ("was not - study", "첫째 빈칸: We에는 were not을 쓰고, 둘째 빈칸: -ing형을 써야 하므로"),
     ("did not - studying", "첫째 빈칸: 뒤에 -ing형이 있어 did not을 쓸 수 없으므로"), ("wasn't - studies", "첫째 빈칸: We에는 weren't를 쓰고, 둘째 빈칸: -ing형을 써야 하므로")], 2,
     S693 + " 괄호 없이는 문장과 관계없는 동사가 든 보기를 바꾸고, 정답 위치가 원문항·B·D와 모두 ④여서 보기 순서도 바꿨다.", st="R", p="- We _______ studying English.\n- Were they ________ together?")
# 6-94 E: 정답 조합(Were - was ~)이 원문항과 같음 / F: B·C와 같음 → 주어를 바꿔 조합을 다르게
S694B = "발문이 ‘두 문장을 모두 과거진행형으로’라고 시제를 알려 주고 괄호로 동사를 주었다. 원문항 발문으로 되돌리고 괄호 동사를 지웠으며 과거 시간 표현을 넣었다. 정답 조합이 %s와 같아 둘째 문장의 주어를 바꿨다."
redo(94, "E", [("Did - cooked", "첫째: 뒤에 -ing형이 있어 Did를 쓸 수 없으므로"), ("Was - were cooking", "첫째: 복수 주어 the children에는 Were를 써야 하므로"), ("Were - were cooking", "the children에 Were, Their parents에 were cooking을 바르게 썼으므로"),
     ("Were - was cooking", "둘째: 복수 주어 Their parents에는 were를 써야 하므로"), ("Are - is cooking", "last night이 있어 현재형을 쓸 수 없으므로")], 3, S694B % "원문항(Were - was ~ing)",
     st="R", p="- _______ the children sleeping at nine last night?\n- Their parents ________ dinner then.")
redo(94, "F", [("Were - were playing", "첫째: 주어 she에는 Was를, 둘째: Her brother에는 was를 써야 하므로"), ("Were - is playing", "첫째: she에는 Was를 쓰고, 둘째: 과거의 일이라 is를 쓸 수 없으므로"), ("Do - was playing", "첫째: 뒤에 -ing형이 있어 Do를 쓸 수 없으므로"),
     ("Was - were playing", "둘째: 단수 주어 Her brother에는 was를 써야 하므로"), ("Was - was playing", "she에 Was, Her brother에 was playing을 바르게 썼으므로")], 5, S694B % "B·C(Was - were ~ing)",
     st="R", p="- _______ she reading when you called?\n- Her brother ________ soccer at that time.")
# 6-97 E: 대화의 짜임·정답 조합(weren't - were)·정답 위치가 D와 같음
redo(97, "E", [("wasn't - were", "Yes로 답했으므로 wasn't를 쓸 수 없으므로"), ("was - were", "Yes, he was로 답하고 복수 주어 my sisters에 were를 썼으므로"), ("was - was", "복수 주어 my sisters에는 were를 써야 하므로"), ("were - were", "주어 he에는 were를 쓸 수 없으므로"), ("did - were", "Was로 물었으므로 did로 답할 수 없으므로")], 2,
     "발문에 조건이 붙었고, 대화의 짜임(Were they ~? — No, they ~. They ~.)과 정답 조합(weren't - were), 정답 위치가 D와 같았다. 원문항 발문으로 되돌리고 대화를 바꿔 정답 조합이 다른 유형과 겹치지 않게 했다.",
     st="R", p="A: Was your dad waiting for the train?\nB: Yes, he ________. But my sisters ________ shopping nearby.", okdup=True)
# 6-99 D: 정답 조합(Was - was)·위치(⑤)가 B와 같음 / F: 정답 위치가 원문항·B와 같은 ⑤
redo(99, "D", [("Were - was", "you에 Were, 대답의 I에 was를 바르게 썼으므로"), ("Did - did", "뒤에 -ing형이 있어 Did로 물을 수 없으므로"), ("Was - were", "주어 you에는 Was가 아니라 Were를, I에는 was를 써야 하므로"), ("Is - was", "last night이 있어 현재형 Is를 쓸 수 없고 you와도 맞지 않으므로"), ("Was - was", "주어 you에는 Was가 아니라 Were를 써야 하므로")], 1,
     S699 + " 정답 조합(Was - was)과 정답 위치가 B와 같아, 주어를 you로 바꿔 정답 조합이 Were - was가 되게 했다.", st="R", p="A: (<u>     A     </u>) you sleeping at ten last night?\nB: Yes, I (<u>     B     </u>).")
redo(99, "F", [("Was - wasn't", "주어 you에는 Was가 아니라 Were를 써야 하므로"), ("Was - was", "you에는 Were를 쓰고, No로 답했으므로 wasn't를 써야 하므로"), ("Were - wasn't", "you에 Were, 부정 대답의 I에 wasn't를 바르게 썼으므로"), ("Were - were", "대답의 주어 I에는 were를 쓸 수 없고 No로 답했으므로"), ("Were - weren't", "대답의 주어 I에는 weren't가 아니라 wasn't를 써야 하므로")], 3,
     S699 + " 정답 위치가 원문항·B와 모두 ⑤여서 보기 순서를 바꿨다.", st="R", p=UB(V(6, 99, "F")["passage"]))
# 6-100 F: 정답 위치가 원문항·B와 같은 ④ → 틀린 곳을 ②로
FIX.pop((6, 100, "F"), None)
F(6, 100, "F", st="R", p="Last Saturday, we went to the beach. ①<u>Was the sun shining</u> brightly? Yes, it was. ②<u>Was the kids building</u> a sandcastle? Yes, they were. ③<u>Was your dad swimming</u> in the sea? No, he was sleeping under an umbrella. ④<u>Was Mom reading</u> a book? Yes, she was. We ⑤<u>were having</u> a great time.",
  c=["Was the sun shining", "Was the kids building", "Was your dad swimming", "Was Mom reading", "were having"], a=2, r=R_PP,
  n=["단수 주어 the sun에 Was를 바르게 썼으므로 오답이다.", "복수 주어 the kids에는 Were를 써야 하므로 정답이다.", "단수 주어 your dad에 Was를 바르게 썼으므로 오답이다.", "단수 주어 Mom에 Was를 바르게 썼으므로 오답이다.", "주어 We에 were를 바르게 썼으므로 오답이다."],
  s="글(가족이 부엌에서 일하는 장면)과 밑줄 문장이 B와 거의 같았고 발문이 원문항과 달랐다. 원문항 발문으로 되돌리고 해변에서의 하루로 글을 새로 썼다. 틀린 곳도 원문항·B(④)와 겹치지 않게 ②에 두었다. 정답 위치 ②.")
