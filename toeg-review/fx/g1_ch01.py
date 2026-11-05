# 1급 CH1 문장의 구조 (1~10) 수정 예시
import re
OKM = "구조로 쓰여 올바르다. 잘못된 용법이 아니므로 오답이다."

# 1-3 사역동사: 유형마다 네 문장을 새로, 틀린 get 문장도 새로
F(1, 3, "C", c=["The nurse made the patient lie down.", "My parents let me stay up late on Fridays.", "Ben helped his grandma to cross the street.", "The manager had the staff check the stock.", "Jenny got her friends join the club."], a=5,
  k="‘Jenny got her friends join the club.’은 get + 목적어 뒤에 동사원형을 두었다. get은 목적어 뒤에 to부정사를 쓰므로 to join으로 고쳐야 한다.",
  n=["‘The nurse made the patient lie down.’은 made + 목적어 + 동사원형 " + OKM, "‘My parents let me stay up late on Fridays.’은 let + 목적어 + 동사원형 " + OKM,
     "help는 목적어 뒤에 to부정사도 쓸 수 있으므로 ‘helped his grandma to cross’는 올바르다. 오답이다.", "‘The manager had the staff check the stock.’은 had + 목적어 + 동사원형 " + OKM,
     "get + 목적어 뒤에 동사원형 join을 두었다. got her friends to join으로 고쳐야 하므로 정답이다."],
  s="B와 겹치던 made·had·helped·let 네 문장을 새 문장으로 바꾸고, 틀린 get 문장도 새로 썼다. 정답 위치 ⑤.")
F(1, 3, "D", c=["The teacher got the class stay after school.", "Mom made me clean the bathroom.", "He let his sister ride his new bike.", "The captain had the crew raise the flag.", "Sora helped her dad cook dinner."], a=1,
  k="‘The teacher got the class stay after school.’은 get + 목적어 뒤에 동사원형 stay를 두었다. got the class to stay로 고쳐야 한다.",
  n=["get + 목적어 뒤에 동사원형 stay를 두었다. got the class to stay로 고쳐야 하므로 정답이다.", "‘Mom made me clean the bathroom.’은 made + 목적어 + 동사원형 " + OKM,
     "‘He let his sister ride his new bike.’은 let + 목적어 + 동사원형 " + OKM, "‘The captain had the crew raise the flag.’은 had + 목적어 + 동사원형 " + OKM,
     "help는 목적어 뒤에 동사원형도 쓸 수 있으므로 ‘helped her dad cook’은 올바르다. 오답이다."],
  s="네 문장을 다른 유형과 겹치지 않는 새 문장으로 바꾸고, 틀린 get 문장을 ①에 새로 넣었다.")
F(1, 3, "E", c=["Our coach made us practice every morning.", "The doctor had the nurse take my temperature.", "The kind man helped us to find the bus stop.", "The boss got his assistant book a hotel room.", "The guard let the visitors take photos."], a=4,
  k="‘The boss got his assistant book a hotel room.’은 get + 목적어 뒤에 동사원형 book을 두었다. got his assistant to book으로 고쳐야 한다.",
  n=["‘Our coach made us practice every morning.’은 made + 목적어 + 동사원형 " + OKM, "‘The doctor had the nurse take my temperature.’은 had + 목적어 + 동사원형 " + OKM,
     "help는 목적어 뒤에 to부정사도 쓸 수 있으므로 ‘helped us to find’는 올바르다. 오답이다.", "get + 목적어 뒤에 동사원형 book을 두었다. got his assistant to book으로 고쳐야 하므로 정답이다.",
     "‘The guard let the visitors take photos.’은 let + 목적어 + 동사원형 " + OKM],
  s="다른 유형과 같던 네 문장을 모두 새로 쓰고, 틀린 get 문장도 새 상황으로 바꿨다.")
F(1, 3, "F", c=["The funny movie made everyone laugh.", "Mr. Kim got the students write their names on the board.", "Grandpa let us pick apples in his garden.", "The librarian had the students return the books by Friday.", "My brother helped me fix my bike."], a=2,
  k="‘Mr. Kim got the students write their names on the board.’은 get + 목적어 뒤에 동사원형 write를 두었다. got the students to write로 고쳐야 한다.",
  n=["‘The funny movie made everyone laugh.’은 made + 목적어 + 동사원형 " + OKM, "get + 목적어 뒤에 동사원형 write를 두었다. got the students to write로 고쳐야 하므로 정답이다.",
     "‘Grandpa let us pick apples in his garden.’은 let + 목적어 + 동사원형 " + OKM, "‘The librarian had the students return the books by Friday.’은 had + 목적어 + 동사원형 " + OKM,
     "help는 목적어 뒤에 동사원형도 쓸 수 있으므로 ‘helped me fix’는 올바르다. 오답이다."],
  s="네 문장을 새로 쓰고 틀린 get 문장을 ②에 두어 유형마다 정답 위치와 문장이 모두 다르게 했다.")

# 1-4 완전타동사: 규칙을 알려 주는 발문을 원문항대로
TV = "‘{}’: 동사 {} 뒤에는 {} 바로 목적어로 온다. 전치사 {} 없이 써야 하므로 오답이다."
F(1, 4, "D", st="R",
  r="discuss, reach, marry, approach, enter는 이 문장들의 뜻에서 목적어를 전치사 없이 바로 취하는 타동사이다.",
  k="‘We approached the entrance quietly.’만 approach가 목적어를 바로 취해 올바르다.",
  n=[TV.format("We discussed about the problem.", "discuss", "논의 대상이", "about"), TV.format("He reached at the station.", "reach", "도착 장소가", "at"),
     TV.format("She married with a doctor.", "marry", "결혼 상대가", "with"), "approach가 목적어 the entrance를 전치사 없이 바로 취해 올바르므로 정답이다.",
     "건물·장소에 들어간다는 뜻의 enter는 장소를 바로 목적어로 취한다. They entered the hall.로 고쳐야 하므로 오답이다."],
  s="발문 ‘목적어를 전치사 없이 직접 취한 문장’이 평가 규칙을 알려 주므로 원문항 발문 ‘동사가 올바르게 사용된 문장’으로 되돌렸다. 보기는 그대로 쓴다.")
F(1, 4, "E", st="R", okx=True, c=["They approached to the desk.", "She resembles to her father.", "We discussed about the issue.", "We reached at the airport on time.", "She resembles her aunt in many ways."], keepx=True,
  xr=[("attend를 참석하다의 뜻으로 쓰면 행사 이름을 직접 목적어로 받는다. 이 조건에서는 to를 빼서 “Tom attended the lecture.”로 고친다. attend to 자체는 주의를 기울이다·처리하다의 뜻으로 사용할 수 있지만, 여기서 지정한 참석 의미와 다르다.",
       "reach는 도착 장소를 바로 목적어로 받는다. at을 빼서 “We reached the airport on time.”으로 고쳐야 한다.")],
  s="발문 괄호 조건을 지워 원문항 발문과 같게 했다. 조건이 없으면 ④ ‘Tom attended to the lecture.’가 ‘강의에 집중했다’로 옳을 수 있어 복수 정답이 되므로, ④를 조건 없이도 틀린 ‘We reached at the airport on time.’으로 바꿨다.")
F(1, 4, "F", st="R",
  r="reach, discuss, resemble, enter는 이 문장들의 뜻에서 목적어를 전치사 없이 바로 취하는 타동사이다.",
  k="‘The hikers reached the shelter before dark.’만 reach가 목적어를 바로 취해 올바르다.",
  n=[TV.format("The group reached to the summit.", "reach", "도착 장소가", "to"), TV.format("Mina discussed about the plan.", "discuss", "논의 대상이", "about"),
     "reach가 목적어 the shelter를 전치사 없이 바로 취해 올바르므로 정답이다.", TV.format("She resembles with her sister.", "resemble", "닮은 사람이", "with"),
     "방에 들어간다는 뜻의 enter는 장소를 바로 목적어로 취한다. He entered the room.으로 고쳐야 하므로 오답이다."],
  s="D와 같이 규칙을 알려 주던 발문을 원문항 발문으로 되돌렸다. 보기는 그대로 쓴다.")

# 1-5 틀린 문장 개수: 괄호 조건 삭제, 개수 선택지 정렬, 줄바꿈 복원
F(1, 5, "C", st="R", p="a) This blanket feels warmly.\nb) We found the instructions clear.\nc) The guard kept the gate locked.\nd) The baby slept peacefully.\ne) She informed us of the change.\nf) We approached to the old castle slowly.",
  c=["1개", "2개", "3개", "4개", "5개"], a=2,
  pre=["문장별 판정:", "a) 틀림: feel 뒤에는 blanket의 상태를 나타내는 형용사 보어가 온다. warmly → warm.", "b) 옳음: clear가 목적어 instructions의 상태를 설명한다.",
       "c) 옳음: locked가 gate가 잠긴 상태를 설명한다.", "d) 옳음: slept는 목적어 없이 쓰이고 peacefully가 동작을 꾸민다.", "e) 옳음: inform + 사람 + of + 내용 구조이다.",
       "f) 틀림: approach는 다가가는 대상을 바로 목적어로 취한다. approached to → approached."],
  k="어법상 틀린 문장은 a, f의 2개이다.", n="cnt",
  s="발문 괄호 조건(본문에 없는 enter 설명)을 지우고, 원문항과 거의 같던 a·f를 새 문장으로 바꿨다. 개수 선택지를 1개~5개 순으로 정렬하고 줄바꿈을 복원했다.")
F(1, 5, "D", st="R", p="BR", op="sortc", xr=[("이 문항에서는 enter가 hall을 직접 목적어로 받는 구조를 요구한다.", "건물·장소에 들어간다는 뜻의 enter는 장소를 바로 목적어로 받는다.")],
  s="정답 근거를 알려 주던 괄호 조건을 지워 원문항 발문으로 되돌리고, 개수 선택지를 1개~5개 순으로 정렬(정답 ⑤→②)했다. 문장마다 줄을 바꿨다.")
F(1, 5, "E", st="R", p="BR", op="sortc",
  s="본문에 없는 find·enter를 설명하던 괄호 조건을 지우고, 개수 선택지를 1개~5개 순으로 정렬(정답 ③→①)했다. 문장마다 줄을 바꿨다.")
F(1, 5, "F", st="R", p="BR", op="sortc",
  s="괄호 조건을 지우고 개수 선택지를 1개~5개 순으로 정렬(정답 ④→①)했다. 문장마다 줄을 바꿨다.")

# 1-6 연결동사 빈칸: 없는 형태(-sing, -sly, is -sed)를 실제 형태 오답으로
def lv(subj, v3, v, ing, pas, to, adj):
    d = {v3: f"3인칭 단수 주어 {subj}에 맞춘 연결동사 {v3} 뒤에 형용사 보어 {adj}가 와서 올바르다.",
         v: f"주어({subj})는 3인칭 단수이므로 {v}가 아니라 {v3}를 써야 한다.",
         ing: f"{ing}은 -ing형이라 혼자서 문장의 동사가 될 수 없다.",
         pas: f"{v}가 주어의 상태를 나타내는 연결동사(~하게 들리다·느껴지다·보이다)로 쓰일 때는 수동태로 만들지 않는다.",
         to: f"{to}는 to부정사라 문장의 동사 자리에 올 수 없다."}
    return d
def lvF(g, n, t, c, a, d, s):
    F(g, n, t, c=c, a=a, n=[d[x] for x in c], s=s)
S16 = "존재하지 않는 형태(-sing, -sly, is -sed) 오답을 실제로 쓰이는 형태({})로 바꿔 오답이 모두 경쟁하게 했다."
d = lv("The bell", "sounds", "sound", "sounding", "is sounded", "to sound", "loud")
d["soundly"] = "soundly는 ‘깊이, 푹’이라는 뜻의 부사라 문장의 동사가 될 수 없다."
lvF(1, 6, "B", ["sounding", "sound", "soundly", "to sound", "sounds"], 5, d, S16.format("-ing형·원형·부사·to부정사") + " 수동형 is sounded는 ‘The bell is sounded loud(종을 크게 울린다)’로 읽힐 수 있어 오답으로 쓰지 않았다.")
d = lv("The bread", "smells", "smell", "smelling", "is smelled", "to smell", "fresh")
lvF(1, 6, "C", ["smelling", "smells", "is smelled", "smell", "to smell"], 2, d, S16.format("-ing형·원형·수동형·to부정사") + " 정답 위치 ②.")
d = lv("The fabric", "feels", "feel", "feeling", "is felt", "to feel", "smooth")
lvF(1, 6, "D", ["feel", "is felt", "feels", "feeling", "to feel"], 3, d, S16.format("원형·수동형·-ing형·to부정사") + " 정답 위치 ③.")
d = lv("The explanation", "seems", "seem", "seeming", "is seemed", "to seem", "reasonable")
lvF(1, 6, "E", ["is seemed", "seeming", "to seem", "seems", "seem"], 4, d, S16.format("수동형·-ing형·to부정사·원형") + " 정답 위치 ④.")
d = lv("The sauce", "tastes", "taste", "tasting", "is tasted", "to taste", "too salty")
lvF(1, 6, "F", ["tastes", "taste", "is tasted", "tasting", "to taste"], 1, d, S16.format("원형·수동형·-ing형·to부정사") + " 정답 위치 ①.")

# 1-7 E: 조건이 있어야 성립하던 attended to 대신 조건 없이 틀린 resembles to
F(1, 7, "E", st="R",
  p="Tom ①<u>reached</u> home late. He ②<u>entered</u> the kitchen and ③<u>discussed</u> the problem with Dad. His little sister, who ④<u>resembles to</u> him a lot, ⑤<u>asked about</u> his day.",
  c=["reached", "entered", "discussed", "resembles to", "asked about"], a=4,
  r="reach, enter, discuss, resemble은 목적어를 전치사 없이 바로 취하는 타동사이다. ask about은 물어보는 주제를 about 뒤에 연결한다.",
  k="“resembles to”는 resemble 뒤에 불필요한 to를 넣었다. “resembles him”으로 고쳐야 한다.",
  n=["“reached”는 도착 장소 home을 바로 받는다. 올바른 부분이므로 오답이다.", "“entered”는 들어간 장소 the kitchen을 바로 목적어로 받는다. 올바른 부분이므로 오답이다.",
     "“discussed”는 논의 대상 the problem을 바로 목적어로 받는다. 올바른 부분이므로 오답이다.", "resemble은 닮은 대상을 바로 목적어로 받는 타동사이다. to를 빼고 “resembles him”으로 고쳐야 하므로 정답이다.",
     "“asked about”는 about 뒤에 물어본 주제 his day가 온다. 올바른 부분이므로 오답이다."],
  s="‘attended to’는 ‘처리하다’ 뜻으로 맞을 수 있어 괄호 조건이 있어야 답이 성립했다. 조건 없이도 틀린 ‘resembles to’로 바꾸고 발문을 원문항과 같게 했다.")

# 1-8 전치사 짝짓기
F(1, 8, "B", st="R", p="• The guide explained the safety rule (A)_____ the visitors.\n• The chef prepared a vegetarian meal (B)_____ Mina.\n• The reporter asked a favor (C)_____ the scientist.",
  c=["(A) to - (B) for - (C) to", "(A) of - (B) for - (C) to", "(A) for - (B) to - (C) of", "(A) to - (B) of - (C) for", "(A) to - (B) for - (C) of"],
  r="explain A to + 사람, prepare A for + 사람, ask a favor of + 사람처럼 동사마다 사람 앞 전치사가 정해져 있다.",
  k="(A) explain A to, (B) prepare A for, (C) ask a favor of이므로 to - for - of가 맞다.", n="combo",
  s="발문을 원문항과 같게 하고, 선택지에 빠진 (A)(B)(C) 표시를 넣었다. (C) ‘asked several questions ___ the scientist’는 of와 to가 모두 쓰여 정답 시비가 있어(원문항에서 고친 결함과 같음) of만 쓰는 ‘asked a favor (C)___ the scientist’로 바꿨다. 정답 ⑤ to - for - of는 그대로다.")
F(1, 8, "C", st="R", p="• Mina asked a favor (A)_____ her teacher.\n• Dad bought a jacket (B)_____ me.\n• I showed my new phone (C)_____ Tom.",
  r="ask a favor of + 사람, buy A for + 사람, show A to + 사람처럼 동사마다 사람 앞 전치사가 정해져 있다.",
  k="(A) ask a favor of, (B) buy A for, (C) show A to이므로 of - for - to가 맞다.", n="combo",
  s="발문 끝의 조건 문장을 지워 원문항 발문으로 되돌렸다. 조건 없이는 send A for도 가능해 답이 흔들리므로 (C)를 show A to만 가능한 문장으로 바꾸고 문장 앞 • 표시를 넣었다.")
F(1, 8, "D", p="• We asked a favor (A)_____ the guide.\n• She made lunch (B)_____ the children.\n• The nurse gave the medicine (C)_____ the patient.",
  r="ask a favor of + 사람, make A for + 사람, give A to + 사람처럼 동사마다 사람 앞 전치사가 정해져 있다.",
  k="(A) ask a favor of, (B) make A for, (C) give A to이므로 of - for - to가 맞다.", n="combo",
  s="부자연스러운 ‘asked advice of the guide’를 ‘asked a favor of the guide’로 바꾸고 문장 앞 • 표시를 넣었다.")
F(1, 8, "E", p="• At the workshop, Leo asked a favor (A)_____ his supervisor.\n• He reserved a laptop (B)_____ Mina.\n• He passed the access card (C)_____ the technician.", keepx=True,
  s="한 문장에 이어 쓴 세 빈칸을 원문항처럼 • 세 줄로 나눴다. 문장 내용과 정답은 그대로다.")

# 1-9 어색한 문장 개수: 괄호 설명 삭제, 선택지 정렬, 줄바꿈 복원
F(1, 9, "B", op="sortc", s="개수 선택지를 1개~5개 순으로 정렬했다(정답 ⑤→①).")
for t, a in [("C", "②"), ("D", "①"), ("E", "①")]:
    F(1, 9, t, st="R", p="BR", op="sortc", s=f"판단 근거를 알려 주던 발문 괄호 설명(find/make/keep/leave의 뜻)을 지워 원문항 발문으로 되돌리고, 개수 선택지를 1개~5개 순으로 정렬(정답 {a})했다. 문장마다 줄을 바꿨다.")
F(1, 9, "F", st="R", p="(a) The speech made everyone inspiringly.\n(b) They found the task difficult.\n(c) We kept the door locked.\n(d) The noise kept the baby awake.\n(e) I found the movie entertaining.",
  op="sortc", xr=[("(d) 옳음: awake는 깨어 있는 상태를 나타내는 형용사 목적격보어이다.", "(d) 옳음: awake는 baby가 깨어 있는 상태를 유지함을 나타내는 형용사 목적격보어이다.")],
  s="괄호 설명과 (a)의 뜻 풀이를 지워 원문항 발문으로 되돌렸다. 부자연스러운 (d) ‘made the baby awake’를 ‘kept the baby awake’로 바꾸고, 개수 선택지를 정렬(정답 ①)했다.")

# 1-10 부사/형용사 보어 의미 차이: 같은 동사·같은 목적어로 부사/형용사만 대비, 오답도 유형마다 새로
F(1, 10, "B", st="R", p="(A) Jiho found the café easily.\n(B) Jiho found the café crowded.",
  c=["(A)와 (B)는 모두 ‘카페를 쉽게 찾았다’는 같은 뜻이다.", "(A)는 카페가 붐볐다는 뜻이고, (B)는 카페를 찾는 과정이 쉬웠다는 뜻이다.",
     "(A)의 easily는 목적격 보어이고, (B)의 crowded는 동사를 꾸미는 부사이다.",
     "(A)는 easily가 found를 꾸며 카페를 쉽게 찾았다는 뜻이고, (B)는 crowded가 목적어 the café의 상태를 설명해 가 보니 카페가 붐볐다는 뜻이다.",
     "(A)는 목적격 보어가 있는 5형식이고 (B)는 목적어만 있는 3형식이다."], a=4,
  r="부사는 동작 방식을 꾸미는 부가어이고, 목적격보어인 형용사는 목적어의 상태·성질을 설명한다. (A)는 3형식, (B)는 5형식이다.",
  n=["(B)의 crowded는 찾는 방법이 아니라 카페의 상태를 설명하므로 두 문장의 뜻이 다르다.", "두 문장의 뜻을 서로 바꿔 설명했다.",
     "easily는 found를 꾸미는 부사이고, crowded가 목적어의 상태를 설명하는 목적격 보어이다. 기능을 거꾸로 설명했다.",
     "부사 easily는 찾는 방식을, 형용사 crowded는 목적어의 상태를 나타낸다는 차이를 바르게 설명했다.", "(A)가 3형식, (B)가 5형식이다. 형식을 거꾸로 설명했다."],
  s="동사가 다른 두 문장 대신 원문항처럼 같은 동사 find·같은 목적어로 부사(easily)와 형용사(crowded)만 대비했다. 발문을 원문항과 같게 하고, 오답 네 개도 이 문장에 맞게 새로 썼다.")
F(1, 10, "C", st="R", p="(A) Tom left the classroom quietly.\n(B) Tom left the classroom empty.",
  c=["(A)는 교실이 조용한 상태로 남았다는 뜻이고, (B)는 교실을 비우며 나간 동작 방식을 나타낸다.",
     "(A)의 quietly는 동사 left를 꾸며 조용히 교실을 나갔다는 뜻이고, (B)의 empty는 목적어 the classroom의 상태를 설명해 교실을 빈 채로 두었다는 뜻이다.",
     "두 문장 모두 Tom이 교실을 떠난 방식만 설명하므로 뜻 차이가 없다.", "(A)의 quietly가 목적격 보어이므로 (A)가 5형식 문장이다.",
     "(B)의 empty는 주어 Tom의 상태를 설명하는 주격 보어이다."], a=2,
  r="부사는 동작 방식을 꾸미는 부가어이고, 목적격보어인 형용사는 목적어의 상태를 설명한다. (A)는 3형식, (B)는 5형식이다.",
  n=["두 문장의 뜻을 서로 바꿔 설명했다.", "부사 quietly는 나가는 방식을, 형용사 empty는 목적어 the classroom의 상태를 나타낸다는 차이를 바르게 설명했다.",
     "(B)의 empty는 떠난 방식이 아니라 교실의 상태를 설명하므로 뜻이 다르다.", "quietly는 left를 꾸미는 부사라 목적격 보어가 아니다. 5형식은 (B)이다.",
     "empty는 Tom이 아니라 목적어 the classroom의 상태를 설명하는 목적격 보어이다."],
  s="같은 동사 leave·같은 목적어로 부사(quietly)와 형용사(empty)만 대비하는 두 문장으로 바꾸고, 발문과 오답 네 개를 새로 썼다. 정답 위치 ②.")
F(1, 10, "D", st="R", p="(A) Dad painted the fence carefully.\n(B) Dad painted the fence white.",
  c=["(A)의 carefully와 (B)의 white는 모두 울타리의 상태를 나타내는 목적격 보어이다.", "(B)는 아빠가 흰옷을 입고 울타리를 칠했다는 뜻이다.",
     "(A)는 부사 carefully가 painted를 꾸며 칠하는 방식을 나타내고, (B)는 형용사 white가 목적어 the fence가 칠해진 결과 상태를 나타낸다.",
     "(A)와 (B) 모두 목적어 뒤에 보어가 있는 5형식 문장이다.", "(B)의 white는 명사 fence를 앞에서 꾸미는 말과 역할이 같으므로 (B)는 3형식이다."], a=3,
  r="부사는 동작 방식을 꾸미는 부가어이고, paint + 목적어 + 형용사는 칠한 결과 목적어가 어떤 상태가 되었는지를 나타낸다. (A)는 3형식, (B)는 5형식이다.",
  n=["carefully는 painted를 꾸미는 부사이므로 목적격 보어가 아니다.", "white는 주어 Dad가 아니라 목적어 the fence의 결과 상태를 나타낸다.",
     "부사 carefully는 칠하는 방식을, 형용사 white는 칠한 뒤 울타리의 상태를 나타낸다는 차이를 바르게 설명했다.", "(A)의 carefully는 부가어이므로 (A)는 3형식이다.",
     "white는 목적어 뒤에서 목적어의 상태를 설명하는 목적격 보어이므로 (B)는 5형식이다."],
  s="같은 동사 paint·같은 목적어로 부사(carefully)와 형용사(white)만 대비하는 두 문장으로 바꾸고, 발문과 오답 네 개를 새로 썼다. 정답 위치 ③.")
F(1, 10, "E", st="R", p="(A) He got the ticket easily.\n(B) He got the ticket wet.",
  c=["(A)의 easily는 목적어 the ticket의 상태를 설명하는 목적격 보어이다.", "(A)와 (B) 모두 표를 구한 방법을 설명한다.", "(B)의 wet은 주어 He가 젖었다는 뜻이다.",
     "(A)는 목적격 보어가 있는 5형식이고 (B)는 3형식이다.",
     "(A)는 easily가 got을 꾸며 표를 쉽게 구했다는 뜻이고, (B)는 wet이 목적어 the ticket의 상태를 설명해 표를 젖게 만들었다는 뜻이다."], a=5,
  r="부사는 동작 방식을 꾸미는 부가어이고, get + 목적어 + 형용사는 목적어를 어떤 상태로 만든다는 뜻이다. (A)는 3형식, (B)는 5형식이다.",
  n=["easily는 got을 꾸미는 부사이므로 목적격 보어가 아니다.", "(B)는 표를 구한 방법이 아니라 표를 젖게 만든 결과를 나타낸다.",
     "wet은 주어가 아니라 목적어 the ticket의 상태를 설명한다.", "(A)가 3형식, (B)가 5형식이다. 형식을 거꾸로 설명했다.",
     "부사 easily는 구하는 방식을, 형용사 wet은 목적어의 상태를 나타낸다는 차이를 바르게 설명했다."],
  s="같은 동사 get·같은 목적어로 부사(easily)와 형용사(wet)만 대비하는 두 문장으로 바꾸고, 발문과 오답 네 개를 새로 썼다. 정답 위치 ⑤.")
F(1, 10, "F", st="R", p="(A) The teacher considered the idea carefully.\n(B) The teacher considered the idea creative.",
  c=["(A)의 carefully는 considered를 꾸며 그 생각을 신중하게 검토했다는 뜻이고, (B)의 creative는 목적어 the idea를 설명해 그 생각을 창의적이라고 여겼다는 뜻이다.",
     "두 문장은 모두 5형식이며 carefully와 creative가 목적격 보어이다.", "(B)의 creative는 주어 The teacher가 창의적이라는 뜻이다.",
     "(A)는 그 생각을 창의적이라고 여겼다는 뜻이고, (B)는 그 생각을 신중히 검토했다는 뜻이다.", "(A)의 carefully는 명사 idea를 꾸미는 형용사 역할을 한다."], a=1,
  r="부사는 동작 방식을 꾸미는 부가어이고, consider + 목적어 + 형용사는 목적어를 어떠하다고 여긴다는 뜻이다. (A)는 3형식, (B)는 5형식이다.",
  n=["부사 carefully는 검토하는 방식을, 형용사 creative는 목적어에 대한 판단을 나타낸다는 차이를 바르게 설명했다.", "carefully는 부사라 목적격 보어가 아니다. 5형식은 (B)뿐이다.",
     "creative는 주어가 아니라 목적어 the idea를 설명한다.", "두 문장의 뜻을 서로 바꿔 설명했다.", "carefully는 명사가 아니라 동사 considered를 꾸미는 부사이다."],
  s="같은 동사 consider·같은 목적어로 부사(carefully)와 형용사(creative)만 대비하는 두 문장으로 바꾸고, 발문과 오답 네 개를 새로 썼다. 정답 위치 ①.")


# ---- 2차 감수(2026-10) 추가 ----
# 1-1 감각동사 + 형용사 보어: 정답 문장만 길던 것을 고르게, 밑줄 범위를 원문항처럼 ‘동사 + 보어’로
R11 = "smell, taste, sound, feel, look, seem처럼 주어의 상태를 설명하는 2형식 동사 뒤 보어 자리에는 부사가 아니라 형용사를 쓴다."
def f11(t, c, a, bad, good, s):
    def nt(i, x):
        w = re.search(r"<u>(\w+) (\w+)</u>", x)
        if i + 1 == a: return f"{w.group(1)} 뒤 보어 자리에 부사({bad})를 썼다. 형용사({good})로 고쳐야 하므로 정답이다."
        return f"{w.group(1)} 뒤에 형용사({w.group(2)})가 보어로 와서 올바르므로 오답이다."
    F(1, 1, t, c=c, a=a, r=R11, n=[nt(i, x) for i, x in enumerate(c)], s=s)
S11 = "틀린 문장에만 수식어구가 붙어 가장 길어서 길이만 보고 정답을 고를 수 있었다. 원문항처럼 모든 보기에 수식어구를 붙여 길이를 고르게 했다."
S11U = " 밑줄도 원문항처럼 ‘동사 + 보어’에 그었다."
f11("B", ["The cloth <u>feels rough</u> on my hands.", "The proposal <u>sounds sensible</u> to us.", "The student <u>looks nervous</u> before the test.", "The milk <u>smells badly</u> this morning.", "The bread <u>tastes wonderful</u> with butter."], 4, "badly", "bad",
    S11 + " smell이 옳은 문장과 틀린 문장에 함께 나오던 ⑤는 taste 문장으로 바꿨다.")
f11("C", ["The coffee <u>tastes bitterly</u> without sugar.", "The pillow <u>feels soft</u> under my head.", "The tea <u>smells fresh</u> in the morning.", "The melody <u>sounds calm</u> in the evening.", "The plan <u>seems practical</u> to everyone."], 1, "bitterly", "bitter",
    S11 + S11U + " bitter가 옳은 형태(③)와 틀린 형태(①)로 함께 나오던 것도 없앴다.")
f11("D", ["The idea <u>sounds reasonable</u> to me.", "The soup <u>smells good</u> in the kitchen.", "The sky <u>looks clear</u> after the rain.", "The blanket <u>feels warmly</u> against my skin.", "The lemonade <u>tastes sour</u> to the kids."], 4, "warmly", "warm",
    S11 + S11U + " feel이 두 번 나오던 ⑤는 taste 문장으로 바꿨다.")
f11("E", ["The idea <u>sounds strangely</u> to everyone.", "The child <u>looks sleepy</u> after lunch.", "The weather <u>seems fine</u> for a picnic.", "The cake <u>tastes sweet</u> with cream.", "The sand <u>feels warm</u> under my feet."], 1, "strangely", "strange",
    S11 + S11U + " sound가 두 번 나오던 ⑤는 feel 문장으로 바꿨다.")
f11("F", ["The roses <u>smell fresh</u> in the vase.", "The song <u>sounds beautiful</u> on the radio.", "The room <u>looks comfortably</u> after the renovation.", "The water <u>feels cold</u> in winter.", "The answer <u>seems correct</u> at first glance."], 3, "comfortably", "comfortable",
    S11 + S11U)

# 1-4 B: attend to는 옳은 문장으로도 읽힘 → 뜻과 상관없이 틀린 문장으로
F(1, 4, "B", c=["Tom reached at home.", "The class discussed the article in detail.", "The students entered to the classroom quietly.", "He resembles with his father.", "They approached to the gate."],
  r="attend, discuss, resemble, reach, approach, enter는 우리말로 ‘~에, ~에 대해, ~와’로 옮겨져도 전치사 없이 목적어를 바로 취하는 타동사이다.",
  k="‘The class discussed the article in detail.’만 discuss가 목적어를 전치사 없이 바로 취해 올바르다.",
  n=["reach 뒤에는 전치사 없이 도착하는 곳을 쓴다(reached home). at이 필요 없으므로 오답이다.", "discuss가 목적어 the article을 전치사 없이 바로 취해 올바르므로 정답이다.",
     "장소에 들어간다는 뜻의 enter는 장소를 바로 목적어로 취한다. to가 필요 없으므로 오답이다.", "resemble은 닮은 대상을 바로 목적어로 취한다. with가 필요 없으므로 오답이다.",
     "approach는 다가가는 대상을 바로 목적어로 취한다. to가 필요 없으므로 오답이다."],
  s="④ ‘We attended to the ceremony.’는 attend to(~을 처리하다, 돌보다)로 읽으면 옳은 문장이 될 수 있어 정답이 둘이 될 수 있었다. 뜻과 상관없이 틀린 ‘He resembles with his father.’로 바꿨다.")
