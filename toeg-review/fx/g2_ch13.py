# 2급 CH13 가정법 (121~130) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."

# 2-121 가정법 과거 주절: 원문항 발문, 혼합 가정으로도 읽히는 would have p.p. 보기를 현재완료로
ST121 = "다음 빈칸에 들어갈 동사의 형태로 알맞은 것을 고르시오."
R121 = "현재 사실과 반대되는 조건은 if + 과거형, 그 결과는 would + 동사원형으로 나타낸다(가정법 과거). 주절에 will·현재형·과거형·현재완료를 쓰지 않는다."
S121 = "발문이 ‘현재 사실과 반대되는 조건 아래 현재 또는 앞으로의 행동을 가정할 때’라고 정답 형태를 알려 주어 원문항 발문으로 되돌렸다. 조건이 없으면 ‘would have + 과거분사’도 혼합 가정으로 읽힐 수 있어 그 보기를 현재완료로 바꿨다."
def n121(x, ok):
    if ok: return f"{x}: if절이 과거형인 가정법 과거이므로 주절에 would + 동사원형이 알맞으므로"
    if x.startswith("will"): return f"{x}: if절이 과거형(현재 사실 반대)이므로 주절에 will을 쓰지 않으므로"
    if x.startswith("has") or x.startswith("have"): return f"{x}: 현재완료는 가정법 과거의 결과를 나타내지 못하므로"
    if x.endswith("s"): return f"{x}: 현재형은 가정의 결과를 나타내지 못하므로"
    return f"{x}: 과거형만으로는 가정의 결과를 나타내지 못하므로"
def f121(t, c, a):
    mk(2, 121, t, [(x, n121(x, i + 1 == a)) for i, x in enumerate(c)], a, R121, S121, st=ST121)
f121("B", ["would take", "has taken", "takes", "will take", "took"], 1)
f121("C", ["will tell", "tells", "would tell", "told", "has told"], 3)
f121("D", ["has walked", "walked", "walks", "will walk", "would walk"], 5)
f121("E", ["will apply", "would apply", "applied", "applies", "has applied"], 2)
f121("F", ["cooked", "will cook", "has cooked", "would cook", "cook"], 4)

# 2-122 as if + had p.p.: 원문항 발문, 원문항처럼 가정법/직설법 대응 제시
ST122 = "다음 문장의 빈칸에 들어갈 말로 알맞은 것을 고르시오."
S122 = "발문이 ‘주절보다 앞선 과거의 상황을 사실과 반대로 가정하는 as if 표현’이라고 정답을 알려 주었고, 원문항의 ‘가정법/직설법’ 대응 제시 형식이 빠졌다. 원문항 발문으로 되돌리고, 원문항처럼 가정법 문장과 직설법 문장을 함께 제시했다. 보기와 정답은 그대로다."
XR122 = [("여기서는 사실과 반대되는 과거 상황을 격식 있게 가정하므로", "직설법 문장이 과거에 그러지 않았음을 밝히므로")]
for t, (g, d) in {"B": ("He describes the concert as if he _____ there.", "In fact, he didn't go to the concert."),
                  "C": ("Mina talks about the accident as if she _____ it herself.", "In fact, she didn't see it; she was abroad."),
                  "D": ("Tom explains the old city as if he _____ there before.", "In fact, he has never lived there."),
                  "E": ("Jane talks about the meeting as if she _____ it.", "In fact, she didn't attend it."),
                  "F": ("He speaks about the book as if he _____ it.", "In fact, he hasn't read it.")}.items():
    ex = V(2, 122, t)["expl"]
    F(2, 122, t, st=ST122, p=f"가정법: {g}\n직설법: {d}", xr=[x for x in XR122 if x[0] in ex], s=S122)

# 2-123 조건문 vs 가정법 과거: 두 빈칸 성격을 알려 주던 발문을 원문항대로
for t in "BCDEF":
    lines = V(2, 123, t)["passage"].split("\n")
    F(2, 123, t, st="R", p="\n".join("• " + x.lstrip("• ") for x in lines),
      s="발문이 ‘첫 문장은 실현 가능한 미래 조건, 둘째는 현재·미래의 가정’이라고 두 빈칸의 성격을 알려 주어, 원문항 발문(빈칸에 들어갈 말을 바르게 짝지은 것)으로 되돌리고 원문항처럼 • 표시를 붙였다. 둘째 문장의 if절이 과거형이라 조건 없이도 정답은 하나다.")

# 2-124 대화 속 가정법 밑줄 다섯 곳: 원문항 형식
ST124 = "다음 대화에서 사용된 가정법 표현 중 어법상 옳지 않은 것을 고르시오."
R124 = "현재 사실과 반대되는 조건·소망은 과거형(be동사는 were), 과거 사실과 반대되는 조건·후회는 had + 과거분사로 나타낸다. I wish, If only 뒤에는 will·can 같은 현재형 조동사를 쓰지 않는다."
S124 = "원문항은 대화 속 밑줄 다섯 곳 중 틀린 가정법 표현을 찾는 형식인데, 변형은 빈칸 하나에 형태를 고르는 형식으로 바뀌었고 발문이 뜻과 시간 관계를 길게 설명했다. 원문항 발문과 형식(대화 속 가정법 표현 밑줄 다섯 곳)으로 다시 썼다."
def f124(t, lines, items, a):
    mk(2, 124, t, items, a, R124, S124, st=ST124, p="\n".join(lines), k=items[a-1][1].split(" 어법상")[0])
f124("B", ["Mina: If ①<u>I were</u> taller, I would join the basketball team.", "Leo: I wish ②<u>I had been</u> at the tryouts last week. I missed them.",
           "Mina: If ③<u>you had come</u>, you would have made the team.", "Leo: Maybe. I wish ④<u>I can play</u> as well as you.", "Mina: If only ⑤<u>I had</u> more time to practice!"],
     [("I were", "현재 사실 반대의 가정에 were를 바르게 썼으므로"), ("I had been", "지난주 일에 대한 후회라 had + 과거분사가 알맞으므로"), ("you had come", "과거 사실 반대의 조건이라 had + 과거분사가 알맞으므로"),
      ("I can play", "I wish 뒤 현재 사실 반대의 소망에는 could play를 써야 한다. 어법상 옳지 않으므로"), ("I had", "If only 뒤 현재 사실 반대의 소망에 과거형을 바르게 썼으므로")], 4)
f124("C", ["Tom: I wish ①<u>I knew</u> the answer to this question.", "Amy: If ②<u>I have</u> the textbook, I would lend it to you.", "Tom: Thanks. If ③<u>I had studied</u> harder, I wouldn't be so worried now.",
           "Amy: I wish ④<u>you had asked</u> me earlier.", "Tom: If only ⑤<u>I were</u> as smart as you!"],
     [("I knew", "I wish 뒤 현재 사실 반대의 소망에 과거형을 바르게 썼으므로"), ("I have", "주절이 would lend인 가정법 과거이므로 if절에는 had를 써야 한다. 어법상 옳지 않으므로"),
      ("I had studied", "과거에 공부하지 않은 사실과 반대로 가정하고 현재의 결과(wouldn't be)를 이은 혼합 가정이라 알맞으므로"), ("you had asked", "이미 지난 일에 대한 아쉬움이라 had + 과거분사가 알맞으므로"), ("I were", "If only 뒤 현재 사실 반대의 소망에 were를 바르게 썼으므로")], 2)
f124("D", ["Jane: If ①<u>it had not rained</u> yesterday, we would have gone hiking.", "Ben: I know. I wish ②<u>the weather were</u> better today, too.", "Jane: If ③<u>I were</u> you, I would check the forecast first.",
           "Ben: Good idea. If only ④<u>I had checked</u> it yesterday!", "Jane: I wish ⑤<u>we will go</u> hiking next weekend."],
     [("it had not rained", "어제 일과 반대되는 조건이라 had + 과거분사가 알맞으므로"), ("the weather were", "오늘의 사실과 반대되는 소망에 were를 바르게 썼으므로"), ("I were", "현재 사실 반대의 가정에 were를 바르게 썼으므로"),
      ("I had checked", "어제 일에 대한 후회라 had + 과거분사가 알맞으므로"), ("we will go", "I wish 뒤에는 will을 쓰지 않는다(I hope we go 또는 I wish we could go). 어법상 옳지 않으므로")], 5)
f124("E", ["Sora: I wish ①<u>I had</u> a pet dog.", "Min: If ②<u>you had</u> a dog, you would have to walk it every day.", "Sora: I know. If ③<u>my mom allows</u> it, I would get one.",
           "Min: I wish ④<u>my apartment were</u> bigger, too.", "Sora: If only ⑤<u>we lived</u> in a house with a yard!"],
     [("I had", "I wish 뒤 현재 사실 반대의 소망에 과거형을 바르게 썼으므로"), ("you had", "현재 사실 반대의 조건에 과거형을 바르게 썼으므로"), ("my mom allows", "주절이 would get인 가정법 과거이므로 if절에는 allowed를 써야 한다. 어법상 옳지 않으므로"),
      ("my apartment were", "현재 사실 반대의 소망에 were를 바르게 썼으므로"), ("we lived", "If only 뒤 현재 사실 반대의 소망에 과거형을 바르게 썼으므로")], 3)
f124("F", ["Leo: If ①<u>I have known</u> about the sale, I would have bought the shoes.", "Amy: I wish ②<u>you had told</u> me. I would have gone with you.", "Leo: If ③<u>I had</u> more money now, I would buy them anyway.",
           "Amy: If only ④<u>they were</u> still on sale!", "Leo: I wish ⑤<u>I could go</u> back to that day."],
     [("I have known", "주절이 would have bought인 가정법 과거완료이므로 if절에는 had known을 써야 한다. 어법상 옳지 않으므로"), ("you had told", "이미 지난 일에 대한 아쉬움이라 had + 과거분사가 알맞으므로"),
      ("I had", "현재 사실 반대의 조건에 과거형을 바르게 썼으므로"), ("they were", "If only 뒤 현재 사실 반대의 소망에 were를 바르게 썼으므로"), ("I could go", "I wish 뒤 현재 사실 반대의 소망에 could + 동사원형을 바르게 썼으므로")], 1)

# 2-125 틀린 문장 개수: 원문항 발문, 여섯 문장, 1개~5개 보기, 정답 개수를 유형마다 다르게
ST125 = "다음 중 어법상 틀린 문장의 개수를 고르시오."
R125 = "현재의 가정은 과거형(be동사는 were), 과거의 가정은 had + 과거분사로 나타내며, 그 결과는 각각 would + 동사원형, would have + 과거분사이다. wish와 as if 뒤에도 가리키는 때에 맞는 가정법 형태를 쓰고 will·can·현재형을 쓰지 않는다."
CNT5 = ["1개", "2개", "3개", "4개", "5개"]
S125 = "발문이 ‘가정법 문장 중’, ‘과거 반대 사실의 표준 형태로 판단’이라고 조건을 덧붙였고, 보기 문장이 원문항(6개)보다 적은 5개였으며 선택지 순서가 뒤섞였다. 원문항 발문으로 되돌리고, 문장을 여섯 개로 해 선택지를 1개~5개 순으로 맞췄으며 문장마다 줄을 바꿨다."
def f125(t, lines, judge, wrong, s=""):
    n = len(wrong.split(","))
    F(2, 125, t, st=ST125, p="\n".join(lines), c=CNT5, a=n, r=R125, pre=["문장별 판정: " + j for j in judge], k=f"어법상 틀린 문장은 {wrong}로 {n}개이다.", n="cnt", s=S125 + s + ipos(n))
f125("B", ["ⓐ She speaks as if she were the manager.", "ⓑ If I had more money, I would travel more.", "ⓒ I wish I know the answer now.", "ⓓ If Tom had studied, he would have passed.", "ⓔ Jane wishes she were taller.", "ⓕ If I were you, I will take the bus."],
     ["ⓐ O. as if + were로 현재 사실의 반대를 나타냈다.", "ⓑ O. 가정법 과거(had … would travel)이다.", "ⓒ X. I wish 뒤 현재 사실 반대에는 과거형을 쓴다(I wish I knew).", "ⓓ O. 가정법 과거완료(had studied … would have passed)이다.",
      "ⓔ O. wish 뒤 현재 사실 반대에 were를 썼다.", "ⓕ X. 가정법 과거의 주절에는 would를 쓴다(I would take)."], "ⓒ, ⓕ", " 원문항과 정답 개수가 같지 않게 틀린 문장을 2개로 했다.")
f125("C", ["ⓐ He acts as if he knew everything.", "ⓑ If we lived closer, we would visit often.", "ⓒ I wish I have more time.", "ⓓ If Mina had left earlier, she will have caught the bus.", "ⓔ Tom wishes he could swim.", "ⓕ If I am you, I would apologize."],
     ["ⓐ O. as if + 과거형으로 현재 사실의 반대를 나타냈다.", "ⓑ O. 가정법 과거이다.", "ⓒ X. I wish 뒤 현재 사실 반대에는 과거형을 쓴다(I wish I had).", "ⓓ X. 가정법 과거완료의 주절은 would have + 과거분사이다(would have caught).",
      "ⓔ O. wish 뒤에 could + 동사원형을 썼다.", "ⓕ X. 주절이 would apologize인 가정법 과거이므로 If I were you로 쓴다."], "ⓒ, ⓓ, ⓕ", " 다른 유형과 정답 개수가 겹치지 않게 틀린 문장을 3개로 했다.")
f125("D", ["ⓐ Jane talks as if she were an expert.", "ⓑ If I were you, I will wait.", "ⓒ I wish I have seen the show.", "ⓓ If Tom had called, I would have answered.", "ⓔ Mina wishes she is taller.", "ⓕ If he had asked me, I will help him."],
     ["ⓐ O. as if + were로 현재 사실의 반대를 나타냈다.", "ⓑ X. 가정법 과거의 주절에는 would를 쓴다(I would wait).", "ⓒ X. 지난 일에 대한 아쉬움은 I wish + had + 과거분사로 쓴다(I wish I had seen).", "ⓓ O. 가정법 과거완료이다.",
      "ⓔ X. wish 뒤 현재 사실 반대에는 were를 쓴다.", "ⓕ X. 가정법 과거완료의 주절은 would have + 과거분사이다(I would have helped)."], "ⓑ, ⓒ, ⓔ, ⓕ", " 다른 유형과 정답 개수가 겹치지 않게 틀린 문장을 4개로 했다.")
f125("E", ["ⓐ He spends as if he were rich.", "ⓑ If we have a car, we would drive.", "ⓒ I wish I knew the truth.", "ⓓ If Jane had studied, she would have passed.", "ⓔ Tom wishes he had listened.", "ⓕ I wish it is Friday today."],
     ["ⓐ O. as if + were로 현재 사실의 반대를 나타냈다.", "ⓑ X. 주절이 would drive인 가정법 과거이므로 if절에는 had를 쓴다.", "ⓒ O. I wish 뒤 현재 사실 반대에 과거형을 썼다.", "ⓓ O. 가정법 과거완료이다.",
      "ⓔ O. 지난 일에 대한 아쉬움에 had + 과거분사를 썼다.", "ⓕ X. I wish 뒤 현재 사실의 반대에는 were를 쓴다."], "ⓑ, ⓕ", " 틀린 문장이 없어 원문항과 인지 과정이 달랐던 것을, ⓑ·ⓕ를 틀린 문장으로 바꿔 오류를 판별하게 했다(원문항의 정답 1개와 겹치지 않게 2개로 했다).")
f125("F", ["ⓐ She acts as if she had seen it before.", "ⓑ If I knew his number, I will call.", "ⓒ I wish I am home now.", "ⓓ If they had left earlier, they would arrive on time yesterday.", "ⓔ Mina wishes she can fly.", "ⓕ If it had snowed, we will make a snowman."],
     ["ⓐ O. as if + had + 과거분사로 과거 사실의 반대를 나타냈다.", "ⓑ X. 가정법 과거의 주절에는 would를 쓴다(I would call).", "ⓒ X. I wish 뒤 현재 사실 반대에는 were를 쓴다(I wish I were home now).",
      "ⓓ X. 어제의 가상 결과는 would have + 과거분사로 쓴다(would have arrived).", "ⓔ X. wish 뒤에는 could를 쓴다(she could fly).", "ⓕ X. 가정법 과거완료의 주절은 would have + 과거분사이다(would have made)."], "ⓑ, ⓒ, ⓓ, ⓔ, ⓕ",
     " 틀린 문장이 없어 원문항과 인지 과정이 달랐던 것을, 다른 유형과 정답 개수가 겹치지 않게 틀린 문장을 5개로 바꿔 오류를 판별하게 했다.")

# 2-127 as if + were: 원문항 발문, 원문항처럼 그럴듯한 오답
ST127 = "다음 빈칸에 들어갈 가장 알맞은 것을 고르시오."
R127 = "as if(as though) + 주어 + 과거형(be동사는 were)은 ‘마치 ~인 것처럼’이라는 현재 사실의 반대를 나타낸다. 실제로는 아니라는 내용이 뒤따르면 직설법(is)보다 가정법(were)을 쓴다."
S127 = "발문이 ‘실제로는 그 신분이 아닌 사람이 그런 것처럼 행동한다는 뜻의 가정법 표현’이라고 정답을 알려 주었고, 오답(as though her were, as if she had being)이 성립하지 않는 형태였으며 보기가 유형마다 거의 같았다. 원문항 발문으로 되돌리고, 원문항처럼 as if + is, as though + is, like + were 같은 그럴듯한 오답으로 바꿨다."
def n127(x, ok):
    if ok: return f"{x}: 실제로는 아닌 현재 상태를 가정하는 as if(as though) + were가 알맞으므로"
    if x.startswith("like"): return f"{x}: like는 구어에서 as if 대신 쓰기도 하지만, 가정법 표현의 바른 형태는 as if(as though) + were이므로"
    if x.startswith("as she") or x.startswith("as he"): return f"{x}: as만으로는 ‘마치 ~인 것처럼’이라는 가정을 나타내지 못하므로"
    return f"{x}: 직설법(is)은 실제로 그럴 수 있는 상황에 쓰므로, 실제로는 아니라는 뒷부분과 맞지 않으므로"
def f127(t, p, c, a):
    mk(2, 127, t, [(x, n127(x, i + 1 == a)) for i, x in enumerate(c)], a, R127, S127, st=ST127, p=p, okdup=True)
f127("B", "Mina gives instructions __________________ the project director, although she is only an intern.", ["as she were", "as if she is", "as though she is", "as if she were", "like she were"], 4)
f127("C", "Tom talks to everyone __________________ the owner of the restaurant, but he is only a customer.", ["as though he were", "as if he is", "like he were", "as he were", "as though he is"], 1)
f127("D", "Leo behaves __________________ a professional chef, but he isn't.", ["as if he is", "as he were", "as if he were", "like he were", "as though he is"], 3)
f127("E", "Jane speaks __________________ the principal, but she isn't.", ["as though she is", "as if she is", "like she were", "as she were", "as though she were"], 5)
f127("F", "He spends money __________________ a millionaire, but he isn't.", ["as though he is", "as if he were", "as he were", "like he were", "as if he is"], 2)

# 2-128 가정법 과거완료 대화: 시간 관계를 알려 주던 발문을 원문항대로
for t in "BCDEF":
    F(2, 128, t, st="R", s="발문이 가정법의 시간 관계(이미 끝난 과거의 조건과 결과)를 설명해 정답 형태를 알려 주어, 원문항 발문(대화의 흐름상 빈칸에 들어갈 적절한 말)으로 되돌렸다. 대화가 지난 일을 묻고 답하므로 조건 없이도 정답은 하나다. 보기와 정답은 그대로다.")

# 2-129 가정법 과거완료 설명 중 옳지 않은 것: 원문항 발문, 옳은 설명 넷 + 틀린 설명 하나
ST129 = "다음은 제시된 문장에 사용된 문법 요소에 대한 설명입니다. 옳지 않은 것은?"
R129 = "had + 과거분사와 would have + 과거분사는 과거 사실과 반대되는 조건과 그 가상 결과를 나타낸다(가정법 과거완료). had는 주어의 인칭·수와 관계없이 그대로 쓰며, 직설법으로 바꾸면 과거 시제의 반대(부정) 문장이 된다."
S129 = "원문항은 설명 중 ‘옳지 않은 것’을 찾는데 변형은 ‘옳은 것’을 고르게 뒤집혔고, 발문이 문장의 성격을 알려 주었으며, 뻔한 오답(if절에는 항상 will 등)이 유형마다 반복되었다. 원문항 발문으로 되돌리고, 그럴듯한 옳은 설명 네 개와 틀린 설명 하나로 유형마다 새로 썼다."
def f129(t, items, a):
    F(2, 129, t, st=ST129, c=[x for x, _ in items], a=a, r=R129,
      n=[w + (" 옳지 않은 설명이므로 정답이다." if i + 1 == a else " 옳은 설명이므로 오답이다.") for i, (_, w) in enumerate(items)], k=items[a-1][1], s=S129 + ipos(a))
f129("B", [("(A)의 had checked는 과거 사실과 반대되는 조건을 나타낸다.", "(A)는 가정법 과거완료의 조건절이다."), ("(B)의 would have found는 앞으로 건물을 찾게 될 것이라는 미래의 뜻이다.", "(B)는 미래가 아니라 과거에 일어날 수 있었던 가상의 결과이다."),
           ("이 문장은 실제로 미나가 주소를 확인하지 않았다는 뜻을 담고 있다.", "과거 사실과 반대로 가정했으므로 실제로는 확인하지 않았다."), ("(A)의 had는 주어의 인칭과 수에 관계없이 그대로 쓴다.", "과거완료의 had는 인칭·수에 따라 바뀌지 않는다."),
           ("직설법으로 바꾸면 As Mina didn't check the address, she didn't find the building.이 된다.", "가정법 과거완료는 과거 시제의 반대 문장으로 바꾼다.")], 2)
f129("C", [("(A)는 had + 과거분사 형태로 과거의 일을 사실과 반대로 가정한다.", "(A)는 가정법 과거완료의 조건절이다."), ("(B)는 would have + 과거분사 형태로 과거의 가상 결과를 나타낸다.", "(B)는 가정법 과거완료의 결과절이다."),
           ("실제로 톰은 일찍 떠나지 않아 기차를 놓쳤다.", "과거 사실과 반대로 가정했으므로 실제로는 늦게 떠나 기차를 놓쳤다."), ("(A)와 (B)는 모두 이미 지난 과거의 일에 대한 가정이다.", "조건과 결과 모두 과거의 일이다."),
           ("직설법으로 바꾸면 As Tom left earlier, he caught the train.이 된다.", "직설법은 사실을 그대로 말하므로 As Tom didn't leave earlier, he didn't catch the train.이 된다.")], 5)
f129("D", [("실제로 우리는 그 사실을 알지 못했다.", "과거 사실과 반대로 가정했으므로 실제로는 몰랐다."), ("(B)는 과거에 다르게 행동했을 가능성을 가정한 결과이다.", "(B)는 과거의 가상 결과이다."),
           ("(A)의 had known은 현재 사실과 반대되는 가정을 나타낸다.", "had + 과거분사는 현재가 아니라 과거 사실과 반대되는 가정을 나타낸다."), ("(A)를 직설법으로 바꾸면 we didn't know the truth가 된다.", "과거 사실과 반대되는 조건은 과거 시제의 부정문으로 바뀐다."),
           ("(B)의 would 대신 could를 쓰면 ‘다르게 행동할 수 있었을 텐데’라는 뜻이 된다.", "could have + 과거분사는 과거에 할 수 있었던 가상의 일을 나타낸다.")], 3)
f129("E", [("(A) 자리에 studied를 써도 뜻과 시제가 같다.", "studied를 쓰면 현재 사실의 반대(가정법 과거)가 되어 결과절(would have passed)과도 맞지 않는다."), ("(A)는 과거에 더 열심히 공부하지 않은 사실과 반대되는 가정이다.", "(A)는 가정법 과거완료의 조건절이다."),
           ("(B)는 과거에 합격했을 수도 있었던 가상의 결과이다.", "(B)는 가정법 과거완료의 결과절이다."), ("실제로 제인은 시험에 떨어졌다.", "합격했을 것이라는 가정의 반대가 사실이다."), ("이 문장은 가정법 과거완료 문장이다.", "had + 과거분사, would have + 과거분사의 짝이다.")], 1)
f129("F", [("(A)와 (B)가 함께 과거 사실과 반대되는 가정을 이룬다.", "가정법 과거완료의 조건절과 결과절이다."), ("(A)의 had taken에서 had는 주어가 달라져도 바뀌지 않는다.", "과거완료의 had는 인칭·수에 따라 바뀌지 않는다."),
           ("(B)는 더 일찍 도착했을 가상의 결과를 나타낸다.", "(B)는 과거의 가상 결과이다."), ("이 문장은 실제로 그들이 택시를 타서 일찍 도착했다는 뜻이다.", "과거 사실과 반대로 가정했으므로 실제로는 택시를 타지 않아 일찍 도착하지 못했다."),
           ("직설법으로 바꾸면 As they didn't take a taxi, they didn't arrive earlier.가 된다.", "과거 시제의 부정문으로 바르게 바꿨다.")], 4)

# 2-130 옳은 문장 개수: 보기 정렬, E·F는 틀린 문장을 넣어 개수를 다르게
for t, (o, nw) in {"B": ("②", "④"), "D": ("④", "④")}.items():
    F(2, 130, t, op="sortc", s=f"개수 선택지를 1개~5개 순으로 정렬(정답 {o}→{nw})했다.")
R130 = "현재 사실과 반대되는 소망·가정에는 과거형(be동사는 were), 이미 끝난 과거의 후회·가정에는 had + 과거분사를 쓴다. wish 뒤에는 will·can·현재형을 쓰지 않으며, 가정법 과거의 주절은 would + 동사원형이다."
def f130(t, lines, judge, ok, s):
    n = len(ok.split(","))
    F(2, 130, t, st="R", p="\n".join("- " + x for x in lines), c=CNT5, a=n, r=R130, pre=["문장별 판정: " + j for j in judge], k=f"어법상 옳은 문장은 {ok}로 {n}개이다.", n="cnt", s=s + ipos(n))
f130("E", ["I wish I know his number.", "Mina wishes she had brought an umbrella.", "Tom acts as if he had met the actor before.", "If Jane were here, she will help.", "We wish we can travel more."],
     ["첫째 X. I wish 뒤 현재 사실 반대에는 과거형을 쓴다(I wish I knew).", "둘째 O. 지난 일에 대한 아쉬움에 had + 과거분사를 썼다.", "셋째 O. as if + had + 과거분사로 과거 사실의 반대를 나타냈다.",
      "넷째 X. 가정법 과거의 주절에는 would를 쓴다(she would help).", "다섯째 X. wish 뒤에는 could를 쓴다(we could travel)."], "둘째, 셋째",
     "틀린 문장이 없어 원문항(옳은 문장 개수 판별)과 달랐던 것을, 세 문장을 틀린 문장으로 바꿔 옳은 문장이 2개가 되게 했다. 선택지를 1개~5개 순으로 정렬했다.")
f130("F", ["I wish I have listened to you.", "Jane wishes she is more patient.", "Tom talks as if he knew everything.", "If we had booked earlier, we will pay less.", "Mina wishes she can sing."],
     ["첫째 X. 지난 일에 대한 아쉬움은 had + 과거분사로 쓴다(I wish I had listened).", "둘째 X. wish 뒤 현재 사실 반대에는 were를 쓴다.", "셋째 O. as if + 과거형으로 현재 사실의 반대를 나타냈다.",
      "넷째 X. 가정법 과거완료의 주절은 would have + 과거분사이다(we would have paid).", "다섯째 X. wish 뒤에는 could를 쓴다(she could sing)."], "셋째",
     "틀린 문장이 없어 원문항과 달랐던 것을, 다른 유형과 정답 개수가 겹치지 않게 네 문장을 틀린 문장으로 바꿔 옳은 문장이 1개가 되게 했다. 선택지를 1개~5개 순으로 정렬했다.")
