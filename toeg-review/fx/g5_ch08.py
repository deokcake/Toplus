# 5급 CH8 형용사·부사·수량 형용사 (71~80) 수정 예시

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def ipos(a): return f" 정답 위치 {'①②③④⑤'[a-1]}."
R_AA = "형용사는 명사 앞에서 명사를 꾸미거나, be동사·연결동사(look, seem, smell, taste, sound, feel, become) 뒤에서 주어를 보충 설명한다. 부사는 동사·형용사·다른 부사를 꾸민다."

# 5-72 원문항 발문
F(5, 72, "B", st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")

# 5-71 선생님 설명: 원문항처럼 예문과 설명, 오답은 명사 수식 형용사 문장
S571 = "원문항 오답은 명사 앞에서 꾸미는 형용사 문장이라 형용사의 두 쓰임을 구별하게 하는데, 변형 오답은 부사 문장이라 형용사/부사 구별로 바뀌었고 유형마다 반복되었다. 원문항처럼 예문을 든 선생님 설명을 주고, 오답을 명사 수식 형용사 문장으로 유형마다 새로 썼다."
def f571(t, ex, adj, verb, subj, items, a, s=S571):
    p = f"선생님: 형용사는 명사 앞에서 명사를 수식하거나 동사 뒤에서 주어를 보충 설명할 수 있어요. \"{ex}\" 이 문장에서 {adj} 형용사는 동사 {verb} 뒤에서 {subj} 주어를 보충 설명하고 있어요."
    mk(5, 71, t, items, a, R_AA, s, st="R", p=p)
ATT = lambda adj, noun: f"형용사({adj})가 명사({noun}) 앞에서 명사를 꾸미는 문장이므로"
PRD = lambda adj, verb, subj: f"형용사({adj})가 동사({verb}) 뒤에서 주어({subj})를 보충 설명하는 문장이므로"
f571("B", "The soup smells delicious.", "delicious라는", "smells", "The soup라는",
     [("It is a delicious cake.", ATT("delicious", "cake")), ("Mina has a new bike.", ATT("new", "bike")), ("The baby looks sleepy.", PRD("sleepy", "looks", "The baby")), ("We saw a big whale.", ATT("big", "whale")), ("He is a kind teacher.", ATT("kind", "teacher"))], 3,
     "선생님 설명이 빠지고 발문이 ‘동사 뒤의 형용사가 주어의 상태를 설명하는 문장’이라고 정답을 알려 주었으며, 오답이 부사 문장으로 바뀌었다. 원문항 발문과 선생님 설명을 되살리고, 오답을 명사 수식 형용사 문장으로 새로 썼다.")
f571("C", "The sky is blue.", "blue라는", "is", "The sky라는",
     [("That is an old house.", ATT("old", "house")), ("The flowers are beautiful.", PRD("beautiful", "are", "The flowers")), ("She wears a red cap.", ATT("red", "cap")), ("I want a cold drink.", ATT("cold", "drink")), ("This is a funny movie.", ATT("funny", "movie"))], 2)
f571("D", "The dog looks happy.", "happy라는", "looks", "The dog라는",
     [("We have a smart dog.", ATT("smart", "dog")), ("Tom lives in a quiet town.", ATT("quiet", "town")), ("It was a long day.", ATT("long", "day")), ("The cake tastes sweet.", PRD("sweet", "tastes", "The cake")), ("I read an interesting book.", ATT("interesting", "book"))], 4)
f571("E", "This tea smells good.", "good이라는", "smells", "This tea라는",
     [("She has long hair.", ATT("long", "hair")), ("They built a tall tower.", ATT("tall", "tower")), ("He is a fast runner.", ATT("fast", "runner")), ("Look at the bright star.", ATT("bright", "star")), ("The room is quiet.", PRD("quiet", "is", "The room"))], 5, S571 + " 예문도 B(The soup smells delicious.)와 겹치지 않게 주어를 바꿨다.")
f571("F", "The boy seems tired.", "tired라는", "seems", "The boy라는",
     [("My uncle feels sick.", PRD("sick", "feels", "My uncle")), ("I have a heavy bag.", ATT("heavy", "bag")), ("This is a busy street.", ATT("busy", "street")), ("We met a friendly girl.", ATT("friendly", "girl")), ("She bought a pretty dress.", ATT("pretty", "dress"))], 1)

# 5-72 형용사 찾기: D~F는 부사 오답을 유형마다 새로
S572 = "부사 오답 네 문장이 C와 똑같았다. 유형마다 부사 오답을 새로 썼다."
ADV = lambda v: f"동사({v})를 꾸미는 부사이므로"; ADV0 = lambda w, v: f"-ly 없이 부사로 쓰여 동사({v})를 꾸미므로"
def f572(t, items, a, s=S572):
    FIX.pop((5, 72, t), None)
    mk(5, 72, t, items, a, R_AA, s)
f572("D", [("Mina sings <u>loudly</u>.", ADV("sings")), ("Dad drives <u>carefully</u>.", ADV("drives")), ("The soup smells <u>good</u>.", "연결동사 smells 뒤에서 주어를 보충 설명하는 형용사이므로"), ("The kids play <u>happily</u>.", ADV("play")), ("He answered <u>quickly</u>.", ADV("answered"))], 3)
f572("E", [("The train arrived <u>late</u>.", ADV0("late", "arrived")), ("Tom smiled <u>brightly</u>.", ADV("smiled")), ("We talked <u>quietly</u>.", ADV("talked")), ("She dances <u>well</u>.", "good의 부사형으로 동사 dances를 꾸미므로"), ("Jane looks <u>happy</u>.", "연결동사 looks 뒤에서 주어를 보충 설명하는 형용사이므로")], 5)
f572("F", [("I got up <u>early</u>.", ADV0("early", "got up")), ("The sky is <u>blue</u>.", "be동사 is 뒤에서 주어를 보충 설명하는 형용사이므로"), ("She speaks <u>softly</u>.", ADV("speaks")), ("The boy jumped <u>high</u>.", ADV0("high", "jumped")), ("They ate <u>slowly</u>.", ADV("ate"))], 2)

# 5-73 many/much: D~F는 much 오답을 유형마다 새로(부정문·의문문 위주)
R573 = "many는 셀 수 있는 명사의 복수형 앞에, much는 셀 수 없는 명사 앞에 쓴다. much는 주로 부정문과 의문문에 쓴다."
S573 = "much 오답 네 문장이 C와 똑같았다. 유형마다 much 문장을 새로 쓰고, 원문항처럼 부정문·의문문 위주로 썼다."
MU = lambda n: f"셀 수 없는 명사 {n} 앞이라 much가 들어가므로"; MA = lambda n: f"셀 수 있는 복수 명사 {n} 앞이라 many가 들어가므로"
def f573(t, items, a, s=S573):
    mk(5, 73, t, items, a, R573, s)
f573("D", [("We see _______ cars.", MA("cars")), ("She doesn't want _______ sugar.", MU("sugar")), ("Did you spend _______ time?", MU("time")), ("There isn't _______ milk.", MU("milk")), ("I don't drink _______ coffee.", MU("coffee"))], 1)
f573("E", [("Is there _______ juice in the bottle?", MU("juice")), ("We don't get _______ snow here.", MU("snow")), ("She doesn't need _______ help.", MU("help")), ("How _______ bread do you want?", MU("bread")), ("They have _______ pencils.", MA("pencils"))], 5)
f573("F", [("Don't put _______ butter on it.", MU("butter")), ("Tom has _______ apples.", MA("apples")), ("I don't have _______ news.", MU("news")), ("We don't use _______ paper.", MU("paper")), ("How _______ cheese is there?", MU("cheese"))], 2)

# 5-74 우리말-영어 짝: 같은 우리말 반복 없이 유형마다 새로
R574 = "fast, hard, late, early, high, near, straight는 -ly 없이 부사로 쓴다. hardly(거의 ~않다), lately(최근에), highly(매우), nearly(거의)는 뜻이 다른 말이다. 동사를 꾸밀 때는 형용사가 아니라 부사를 쓴다."
S574 = "같은 우리말을 옳게 옮긴 것과 틀리게 옮긴 것이 함께 있어 대비 단서가 되었고, 옳은 짝 문장이 유형마다 반복되었다. 같은 우리말이 두 번 나오지 않게 유형마다 새로 썼다."
OK74 = lambda w: f"‘~하게’를 부사({w})로 바르게 옮겼으므로"
def f574(t, items, a, s=S574):
    mk(5, 74, t, items, a, R574, s)
f574("C", [("그녀는 피아노를 잘 친다. - She plays the piano good.", "동사 plays를 꾸미는 말이라 형용사 good이 아니라 부사 well을 써야 하므로"), ("우리는 늦게까지 일했다. - We worked late.", OK74("late")), ("새가 높이 날았다. - The bird flew high.", OK74("high")),
           ("나는 일찍 잠자리에 든다. - I go to bed early.", OK74("early")), ("그들은 열심히 연습한다. - They practice hard.", OK74("hard"))], 1, S574 + " 틀린 짝도 영어에 없는 말(fastly) 대신 실제 낱말을 잘못 쓴 것(good)으로 바꿨다.")
f574("D", [("그녀는 곧장 학교로 갔다. - She went straight to school.", OK74("straight")), ("그녀는 열심히 공부한다. - She studies hardly.", "hardly는 ‘거의 ~않다’라는 뜻이라 ‘열심히’는 hard로 써야 하므로"), ("그 기차는 늦게 왔다. - The train came late.", OK74("late")),
           ("그는 높이 뛰었다. - He jumped high.", OK74("high")), ("우리는 빠르게 걸었다. - We walked fast.", OK74("fast"))], 2)
f574("E", [("Tom은 일찍 도착했다. - Tom arrived early.", OK74("early")), ("그 개는 빠르게 달린다. - The dog runs fast.", OK74("fast")), ("아빠는 열심히 일하신다. - Dad works hard.", OK74("hard")),
           ("그 고양이가 가까이 왔다. - The cat came nearly.", "nearly는 ‘거의’라는 뜻이라 ‘가까이’는 near로 써야 하므로"), ("우리는 늦게 일어났다. - We got up late.", OK74("late"))], 4)
f574("F", [("그들은 높이 올라갔다. - They climbed high.", OK74("high")), ("그녀는 빨리 말한다. - She speaks fast.", OK74("fast")), ("그는 그 문제를 쉽게 풀었다. - He solved the problem easy.", "동사 solved를 꾸미는 말이라 형용사 easy가 아니라 부사 easily를 써야 하므로"),
           ("우리는 늦게 저녁을 먹었다. - We had dinner late.", OK74("late")), ("나는 열심히 달렸다. - I ran hard.", OK74("hard"))], 3)

# 5-75 틀린 문장: 원문항 발문, 부사 문장과 연결동사 + 형용사 문장을 섞어 짝 없이
S575 = "발문이 ‘연결동사로 사용할 때 뒤의 보어가 잘못 쓰인 문장’이라고 정답 기준을 알려 주었고, 정답 문장과 같은 문장의 옳은 형태가 함께 있었으며 오답이 유형마다 반복되었다. 원문항 발문으로 되돌리고, 원문항처럼 부사가 동사를 꾸미는 문장과 연결동사 + 형용사 문장을 섞어 짝 문장 없이 유형마다 새로 썼다."
AD = lambda adv, v: f"부사({adv})가 동사({v})를 바르게 꾸몄으므로"; LK = lambda v, adj: f"연결동사({v}) 뒤에 형용사({adj})를 보어로 바르게 썼으므로"; BE = lambda adj: f"be동사 뒤에 형용사({adj})를 보어로 바르게 썼으므로"
def f575(t, items, a, s=S575):
    mk(5, 75, t, items, a, R_AA, s, st="R")
F(5, 75, "B", st="R", s="발문이 ‘연결동사로 사용할 때 뒤의 보어가 잘못 쓰인 문장’이라고 정답 기준을 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f575("C", [("She looks happily.", "연결동사 looks 뒤에는 부사가 아니라 형용사 happy를 써야 하므로"), ("The baby sleeps quietly.", AD("quietly", "sleeps")), ("This bread tastes sweet.", LK("tastes", "sweet")), ("He answered the question correctly.", AD("correctly", "answered")), ("The music is loud.", BE("loud"))], 1)
f575("D", [("Tom walked slowly to school.", AD("slowly", "walked")), ("The flowers smell sweet.", LK("smell", "sweet")), ("We finished the work quickly.", AD("quickly", "finished")), ("The movie was very excitingly.", "be동사 뒤에는 부사가 아니라 형용사 exciting을 보어로 써야 하므로"), ("You look tired today.", LK("look", "tired"))], 4)
f575("E", [("My grandma speaks kindly.", AD("kindly", "speaks")), ("Tom seems sadly.", "연결동사 seems 뒤에는 부사가 아니라 형용사 sad를 써야 하므로"), ("The test was easy.", BE("easy")), ("She closed the door gently.", AD("gently", "closed")), ("The milk tastes sour.", LK("tastes", "sour"))], 2)
f575("F", [("The kids played happily.", AD("happily", "played")), ("His voice sounds strange.", LK("sounds", "strange")), ("The flowers are beautifully.", "be동사 뒤에는 부사가 아니라 형용사 beautiful을 보어로 써야 하므로"), ("I wrote the letter carefully.", AD("carefully", "wrote")), ("The room became warm.", LK("became", "warm"))], 3)

# 5-76 단어 배열: 원문항 발문, 주어진 단어만으로 만든 어순 오류
R576 = "영어 문장은 주어 + 동사 + 목적어·보어의 어순으로 쓴다. 형용사는 명사 앞(a + 형용사 + 명사)이나 be동사 뒤에, very는 꾸미는 형용사·부사 바로 앞에, 동사를 꾸미는 부사는 보통 문장 끝에 둔다."
S576 = "발문이 ‘주어로 시작하고 마침표로 끝나는 평서문’이라고 형식을 알려 주었고, 주어가 빠지거나 물음표로 끝나거나 주어진 적 없는 단어가 들어간 오답은 어순 판단 없이 지워졌다. 원문항 발문으로 되돌리고 주어진 단어만 쓴 어순 오류로 오답을 바꿨다."
OK76 = "주어 + 동사 + 목적어·보어의 어순으로 바르게 배열했으므로"
def f576(t, items, a, s=S576, **kw):
    mk(5, 76, t, items, a, R576, s, st="R", **kw)
f576("B", [("The bird small sings beautifully.", "형용사 small은 명사 bird 앞에 와야 하므로"), ("The small bird sings beautifully.", OK76), ("The small sings bird beautifully.", "동사 sings가 명사 bird보다 앞에 와서 주어가 끊어졌으므로"), ("Sings the small bird beautifully.", "동사 sings로 문장을 시작해 주어 + 동사의 어순이 아니므로"), ("Small the bird sings beautifully.", "형용사 small은 the와 명사 사이에 와야 하므로")], 2, S576 + " 제시 단어도 원문항처럼 괄호 없이, 첫 낱말을 알려 주는 대문자(The) 없이 썼다.", p="small / bird / the / sings / beautifully / .")
f576("C", [("Very the dog is cute.", "very는 꾸미는 형용사 cute 바로 앞에 와야 하므로"), ("The dog very is cute.", "very는 동사 is가 아니라 형용사 cute 앞에 와야 하므로"), ("The dog is cute very.", "very는 꾸미는 형용사 cute 뒤가 아니라 앞에 와야 하므로"), ("The dog is very cute.", OK76), ("Is the dog very cute.", "be동사가 주어 앞에 와 의문문 어순인데 마침표로 끝나므로")], 4)
f576("D", [("Tom runs very fast.", "주어 + 동사 + very + 부사의 어순으로 바르게 배열했으므로"), ("Tom very runs fast.", "very는 동사가 아니라 부사 fast 앞에 와야 하므로"), ("Tom runs fast very.", "very는 꾸미는 부사 fast 앞에 와야 하므로"), ("Runs Tom very fast.", "동사 runs로 문장을 시작해 주어 + 동사의 어순이 아니므로"), ("Tom fast runs very.", "부사 fast는 동사 runs 뒤에, very는 fast 앞에 와야 하므로")], 1)
f576("E", [("She has beautiful a bag.", "a는 형용사 beautiful 앞에 와서 a beautiful bag이 되어야 하므로"), ("She has a bag beautiful.", "형용사 beautiful은 명사 bag 앞에 와야 하므로"), ("She a beautiful bag has.", "동사 has가 목적어 뒤로 밀려 주어 + 동사 + 목적어의 어순이 아니므로"), ("She beautiful has a bag.", "형용사 beautiful이 동사 앞에 끼어들었으므로"), ("She has a beautiful bag.", OK76)], 5)
f576("F", [("Walks the cat quietly.", "동사 walks로 문장을 시작해 주어 + 동사의 어순이 아니므로"), ("The walks cat quietly.", "동사 walks가 the와 명사 cat 사이에 끼어들었으므로"), ("The cat walks quietly.", "주어 + 동사 + 부사의 어순으로 바르게 배열했으므로"), ("Cat the walks quietly.", "the는 명사 cat 앞에 와야 하므로"), ("The quietly cat walks.", "부사 quietly는 명사 앞이 아니라 동사 walks를 꾸미는 자리에 와야 하므로")], 3)

# 5-77 부사 철자: 원문항 발문, y → i 철자 변화가 있는 형용사로
R577 = "형용사에 -ly를 붙여 부사를 만든다. 자음 + y로 끝나면 y를 i로 바꾸고 -ly를 붙이며(happy → happily, easy → easily), -ful로 끝나면 -ly만 붙인다(careful → carefully)."
S577 = "원문항은 y → i 철자 규칙(happily)을 묻는데, 변형은 -ly만 붙이면 되는 형용사였고 일부는 발문이 정답을 알려 주었다. 원문항 발문으로 되돌리고 y → i 철자 변화가 있는 형용사로 바꿨다."
YI = lambda adj, adv: f"자음 + y로 끝나는 형용사({adj})는 y를 i로 바꾸고 -ly를 붙여 부사({adv})가 되므로"
def f577(t, ko, sent, items, a, s=S577):
    mk(5, 77, t, items, a, R577, s, st="R", p=f"{ko}\n→ {sent}")
F(5, 77, "B", st="R", s="발문이 원문항과 달랐다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f577("C", "그는 그 문제를 쉽게 풀었다.", "He solved the problem ________.",
     [("easy", "형용사 easy로는 동사 solved를 꾸밀 수 없으므로"), ("easyly", YI("easy", "easily")), ("easiness", "‘쉬움’이라는 명사라 동사를 꾸밀 수 없으므로"), ("easilly", "-ly에 l을 한 번만 써서 easily가 되므로"), ("easily", "y를 i로 바꾸고 -ly를 붙인 부사 easily를 바르게 썼으므로")], 5)
f577("D", "그들은 바쁘게 일한다.", "They work ________.",
     [("busily", "y를 i로 바꾸고 -ly를 붙인 부사 busily를 바르게 썼으므로"), ("busyly", YI("busy", "busily")), ("busy", "형용사 busy로는 동사 work를 꾸밀 수 없으므로"), ("business", "‘사업’이라는 명사라 동사를 꾸밀 수 없으므로"), ("busies", "busy에 -es를 붙인 동사 형태라 부사가 아니므로")], 1)
f577("F", "그는 무겁게 숨을 쉬었다.", "He breathed ________.",
     [("heavyly", YI("heavy", "heavily")), ("heavily", "y를 i로 바꾸고 -ly를 붙인 부사 heavily를 바르게 썼으므로"), ("heavy", "형용사 heavy로는 동사 breathed를 꾸밀 수 없으므로"), ("heaviness", "‘무거움’이라는 명사라 동사를 꾸밀 수 없으므로"), ("heavilly", "-ly에 l을 한 번만 써서 heavily가 되므로")], 2)

# 5-78 many/much 밑줄: B 원문항 발문, C~F는 짝 없이 유형마다 새로
F(5, 78, "B", st="R", s="발문이 ‘밑줄 친 수량 형용사의 쓰임이 어색한 문장’으로 바뀌었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
S578 = "정답 문장과 같은 문장의 옳은 형태가 함께 있어 대비 단서가 되었고 오답 네 개가 C와 똑같았다. 원문항처럼 How many/much 의문문과 부정문을 섞어 짝 문장 없이 유형마다 새로 썼다."
OKMU = lambda n: f"셀 수 없는 명사 {n} 앞에 much를 바르게 썼으므로"; OKMA = lambda n: f"셀 수 있는 복수 명사 {n} 앞에 many를 바르게 썼으므로"
def f578(t, items, a, s=S578):
    mk(5, 78, t, items, a, R573, s)
f578("C", [("She doesn't drink <u>many</u> water.", "water는 셀 수 없는 명사라 much를 써야 하므로"), ("There are <u>many</u> stars in the sky.", OKMA("stars")), ("How <u>much</u> milk do you need?", OKMU("milk")), ("I have <u>many</u> friends.", OKMA("friends")), ("We don't have <u>much</u> time.", OKMU("time"))], 1)
f578("D", [("How <u>many</u> eggs do we need?", OKMA("eggs")), ("They don't eat <u>much</u> meat.", OKMU("meat")), ("There were <u>many</u> people at the party.", OKMA("people")), ("Tom doesn't read <u>much</u> books.", "books는 셀 수 있는 복수 명사라 many를 써야 하므로"), ("Is there <u>much</u> rain in summer?", OKMU("rain"))], 4)
f578("E", [("We didn't get <u>much</u> sleep.", OKMU("sleep")), ("How <u>much</u> dogs do you have?", "dogs는 셀 수 있는 복수 명사라 How many를 써야 하므로"), ("She has <u>many</u> dolls.", OKMA("dolls")), ("Did you buy <u>many</u> gifts?", OKMA("gifts")), ("There isn't <u>much</u> space.", OKMU("space"))], 2)
f578("F", [("I don't need <u>much</u> help.", OKMU("help")), ("He has <u>many</u> caps.", OKMA("caps")), ("There aren't <u>many</u> cars on the road.", OKMA("cars")), ("We don't have <u>much</u> snow.", OKMU("snow")), ("How <u>many</u> cheese do we have?", "cheese는 셀 수 없는 명사라 How much를 써야 하므로")], 5)

# 5-79 밑줄 친 말의 역할: 원문항처럼 <보기> 세 개, 원문항 발문
R579 = "형용사는 명사를 꾸미거나 be동사·연결동사 뒤에서 주어를 설명하고, 부사는 동사를 꾸민다. fast, hard, late, high, early는 -ly 없이 형용사와 부사로 모두 쓰이므로 문장 속 역할로 판단한다."
S579 = "원문항 <보기>는 세 개인데 변형은 네 개였고 발문이 ‘빠짐없이 모두’로 바뀌었다. 원문항 발문과 <보기> 세 개로 되돌리고, 정답 조합이 원문항((가), (다))과 겹치지 않게 썼다."
def f579(t, w, sent, lines, judge, ok, c, s=S579):
    a = c.index(ok) + 1
    F(5, 79, t, st=f"다음 문장에서 밑줄 친 '{w}'의 역할에 대한 설명으로 옳은 것을 <보기>에서 고르시오.", p=sent + "\n<보기>\n" + "\n".join(lines), c=c, a=a, r=R579,
      pre=["설명별 판정: " + j for j in judge], k=f"옳은 설명은 {ok}이다.", n=setnotes(c, ok, "옳은 설명"), okdup=True, s=s + ipos(a))
f579("B", "fast", "The express train moves <u>fast</u>.", ["(가) 명사 train을 꾸미는 형용사이다.", "(나) 동사 moves를 꾸미는 부사이다.", "(다) -ly 없이 '빠르게'라는 부사 뜻을 가진다."],
     ["(가) X. 동사 뒤에서 동사를 꾸미므로 형용사가 아니다.", "(나) O. 동사 moves를 꾸미는 부사이다.", "(다) O. fast는 -ly 없이 부사로 쓰인다."], "(나), (다)", ["(가)", "(가), (나)", "(가), (나), (다)", "(나), (다)", "(나)"])
f579("C", "late", "The bus came <u>late</u>.", ["(가) 동사 came을 꾸미는 부사이다.", "(나) 명사 bus를 꾸미는 형용사이다.", "(다) '최근에'라는 뜻의 부사이다."],
     ["(가) O. 동사 came을 꾸미는 부사이다.", "(나) X. 명사 앞이 아니라 동사 뒤에서 동사를 꾸민다.", "(다) X. ‘최근에’는 lately이고, late는 ‘늦게’라는 뜻이다."], "(가)", ["(나)", "(가)", "(가), (다)", "(나), (다)", "(가), (나), (다)"],
     S579 + " 밑줄 친 말도 B(fast)와 겹치지 않게 바꿨다.")
f579("D", "early", "Jane is <u>early</u>.", ["(가) 동사 is를 꾸미는 부사이다.", "(나) be동사 뒤에서 주어 Jane을 설명하는 형용사이다.", "(다) 명사 앞에서 명사를 꾸민다."],
     ["(가) X. be동사 뒤에서 주어의 상태를 설명하므로 부사가 아니다.", "(나) O. be동사 뒤에서 주어 Jane을 설명하는 형용사이다.", "(다) X. 명사 앞이 아니라 be동사 뒤에 있다."], "(나)", ["(가)", "(가), (나)", "(나)", "(나), (다)", "(가), (나), (다)"])
f579("E", "high", "He jumped <u>high</u>.", ["(가) 동사 jumped를 꾸미는 부사이다.", "(나) -ly 없이 '높이'라는 부사 뜻을 가진다.", "(다) 주어 He를 설명하는 형용사이다."],
     ["(가) O. 동사 jumped를 꾸미는 부사이다.", "(나) O. high는 -ly 없이 부사로 쓰인다.", "(다) X. 연결동사 뒤가 아니라 동작 동사 뒤에서 동사를 꾸민다."], "(가), (나)", ["(가)", "(다)", "(가), (다)", "(나), (다)", "(가), (나)"],
     S579 + " 밑줄 친 말도 C(late)와 겹치지 않게 바꿨다.")
f579("F", "hard", "This is a <u>hard</u> test.", ["(가) 명사 test를 꾸미는 형용사이다.", "(나) '어려운'이라는 뜻을 가진다.", "(다) 명사 앞에 위치한다."],
     ["(가) O. 명사 test를 꾸미는 형용사이다.", "(나) O. 명사 앞의 hard는 ‘어려운’이라는 뜻이다.", "(다) O. a와 명사 test 사이, 명사 앞에 있다."], "(가), (나), (다)", ["(가), (나), (다)", "(가)", "(가), (나)", "(나), (다)", "(다)"])

# 5-80 대화의 틀린 부분 모두: 원문항 발문, 2~4개 조합, 줄바꿈
S580 = "발문이 ‘smell(seem)은 연결동사로 쓰였다’처럼 정답의 근거를 알려 주거나 원문항과 달랐고, 원문항 선택지는 2~4개 조합인데 한 개짜리 선택지가 대부분이었으며 줄바꿈도 사라졌다. 원문항 발문으로 되돌리고 2~4개 조합 선택지와 줄바꿈을 살렸다."
def f580(t, lines, judge, ok, c, s=S580):
    a = c.index(ok) + 1
    F(5, 80, t, st="R", p="\n".join(lines), c=c, a=a, r=R_AA, pre=["부분별 판정: " + j for j in judge], k=f"어법상 틀린 부분은 {ok}이다.", n=setnotes(c, ok, "틀린 부분"), okdup=True, s=s + ipos(a))
f580("B", ["Mina: The cake (A)<u>smells wonderfully</u>.", "Tom: Yes, and Jane decorated it (B)<u>beautifully</u>.", "Mina: She is very (C)<u>creative</u>.", "Tom: She also speaks to customers (D)<u>polite</u>."],
     ["(A) X. 연결동사 smells 뒤에는 형용사 wonderful을 써야 한다.", "(B) O. 동사 decorated를 부사 beautifully가 꾸민다.", "(C) O. be동사 뒤에 형용사 creative를 썼다.", "(D) X. 동사 speaks를 꾸미므로 부사 politely를 써야 한다."], "(A), (D)",
     ["(A), (B)", "(A), (D)", "(A), (C)", "(B), (C)", "(C), (D)"], "발문이 ‘smell은 연결동사로 쓰였다’고 (A)의 정답 근거를 알려 주었다. 원문항 발문으로 되돌렸다. 보기와 정답은 그대로다.")
f580("C", ["Tom: The soup (A)<u>smells good</u>.", "Jane: Yes, Mom cooked it (B)<u>careful</u>.", "Tom: She always cooks (C)<u>well</u>.", "Jane: It tastes (D)<u>wonderfully</u>."],
     ["(A) O. 연결동사 smells 뒤에 형용사 good을 썼다.", "(B) X. 동사 cooked를 꾸미므로 부사 carefully를 써야 한다.", "(C) O. 동사 cooks를 부사 well이 꾸민다.", "(D) X. 연결동사 tastes 뒤에는 형용사 wonderful을 써야 한다."], "(B), (D)",
     ["(B), (D)", "(A), (C)", "(A), (B), (D)", "(B), (C), (D)", "(A), (B), (C), (D)"])
f580("D", ["Amy: You (A)<u>seem happily</u>.", "Ben: I won the race!", "Amy: You ran really (B)<u>fast</u>.", "Ben: I practiced (C)<u>hardly</u> every day.", "Amy: That sounds (D)<u>greatly</u>."],
     ["(A) X. 연결동사 seem 뒤에는 형용사 happy를 써야 한다.", "(B) O. fast는 -ly 없이 부사로 동사 ran을 꾸민다.", "(C) X. hardly는 ‘거의 ~않다’라는 뜻이라 ‘열심히’는 hard로 써야 한다.", "(D) X. 연결동사 sounds 뒤에는 형용사 great를 써야 한다."], "(A), (C), (D)",
     ["(A), (C)", "(B), (D)", "(A), (B), (C)", "(A), (C), (D)", "(A), (B), (C), (D)"], S580 + " 정답 조합이 원문항((A), (C))과 겹치지 않게 (D)도 틀린 부분으로 썼다.")
f580("E", ["Jane: The dog looks (A)<u>cutely</u>.", "Tom: It moves (B)<u>careful</u>.", "Jane: It is (C)<u>very small</u>.", "Tom: But it barks (D)<u>noisy</u>."],
     ["(A) X. 연결동사 looks 뒤에는 형용사 cute를 써야 한다.", "(B) X. 동사 moves를 꾸미므로 부사 carefully를 써야 한다.", "(C) O. be동사 뒤에 very + 형용사 small을 썼다.", "(D) X. 동사 barks를 꾸미므로 부사 noisily를 써야 한다."], "(A), (B), (D)",
     ["(A), (B)", "(B), (D)", "(A), (B), (D)", "(A), (C), (D)", "(A), (B), (C), (D)"], S580 + " 정답 조합이 C와 겹치지 않게 (A)도 틀린 부분으로 썼다.")
f580("F", ["Yuna: She sings (A)<u>beautifully</u>.", "Minsu: Yes, and she is (B)<u>kind</u>.", "Yuna: She speaks (C)<u>polite</u>.", "Minsu: And she works (D)<u>diligent</u>."],
     ["(A) O. 동사 sings를 부사 beautifully가 꾸민다.", "(B) O. be동사 뒤에 형용사 kind를 썼다.", "(C) X. 동사 speaks를 꾸미므로 부사 politely를 써야 한다.", "(D) X. 동사 works를 꾸미므로 부사 diligently를 써야 한다."], "(C), (D)",
     ["(A), (C)", "(B), (C)", "(A), (B), (D)", "(A), (C), (D)", "(C), (D)"])


# ---- 2차 감수(2026-10) 추가 ----
# 5-72 C: 원문항 ③과 같은 문장(They work hard.), 정답 위치도 원문항과 같음(④)
f572("C", [("The dog is <u>small</u>.", "be동사 is 뒤에서 주어를 보충 설명하는 형용사이므로"), ("We walk <u>slowly</u>.", ADV("walk")), ("She sings <u>beautifully</u>.", ADV("sings")), ("The farmers work <u>hard</u>.", ADV0("hard", "work")), ("He runs <u>quickly</u>.", ADV("runs"))], 1,
     "①(They work hard.)이 원문항 ③과 똑같은 문장이었고 정답 위치도 원문항과 같았다(④). 겹치는 문장을 바꾸고 정답 위치를 옮겼다.")
# 5-77 E: 정답 낱말(carefully)이 B와 같고 y → i 규칙이 아님 → y → i 낱말로
f577("E", "아이들이 시끄럽게 논다.", "The kids play ________.",
     [("noisyly", YI("noisy", "noisily")), ("noisy", "형용사 noisy로는 동사 play를 꾸밀 수 없으므로"), ("noise", "‘소음’이라는 명사라 동사를 꾸밀 수 없으므로"), ("noisily", "y를 i로 바꾸고 -ly를 붙인 부사 noisily를 바르게 썼으므로"), ("noisilly", "-ly에 l을 한 번만 써서 noisily가 되므로")], 4,
     "정답 낱말(carefully)과 오답(carefullly, careful)이 B와 같았고, -ly만 붙이면 되어 원문항의 y → i 철자 규칙(happily)을 묻지 않았다. y → i 철자 변화가 있는 낱말로 바꿨다.")
