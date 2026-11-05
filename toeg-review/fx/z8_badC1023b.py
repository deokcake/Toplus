# 2026-10-23 C 유형 감수 2차 반영: 메모(‘원문항보다 짧다’)는 있었지만 판정 칸이 비어 있어 1차(z7)에서 빠진 3급 C 7문항(3-13·3-15·3-25·3-29·3-80·3-87·3-110),
# D 유형에 새로 달린 부적합 3문항(3-9·3-13·3-15), 보기가 아직 짧던 3-98 C·E. 같은 번호의 확인 완료가 아닌 유형(C~F)을 모두 원문항 낱말 수 이상으로 늘린다.
# 확인 완료 문서(B 전부, 3-9 C)는 건드리지 않는다.
MEMO5 = "감수 메모 반영(10-23 C 2차): "
def OKS(items, a): return [w + OK(i + 1, a) for i, w in enumerate(items)]
def ADD(g_, n_, t_, more): return (OLD(g_, n_, t_).get("s", "") + " " + more).strip()
def PJ(*lines): return ["문장별 판정: " + l for l in lines]
def HJ(*lines): return ["항목별 판정: " + l for l in lines]
LEN = MEMO5 + "원문항보다 짧던 문장을 원문항 길이 이상으로 늘렸다. 틀린 곳과 정답은 그대로다."
LENP = MEMO5 + "원문항보다 짧던 지문을 원문항 길이 이상으로 늘렸다. 보기와 정답은 그대로다."

# ---- 3-9 D·E·F: 설명 네 개를 원문항처럼 자세히, 문장도 원문항(7낱말) 이상으로 ----
L9 = MEMO5 + "원문항보다 짧고 단조롭던 <보기> 문장과 설명을 원문항처럼 자세히 늘렸다. 옳은 설명과 정답은 그대로다."
RE(3, 9, "D", p="<보기>\nWas there a big meeting in the classroom yesterday?\n\n가. 이 문장의 실제 주어는 'there'이므로 be동사도 'there'에 맞춘다.\n나. 'yesterday'가 있어도 'there' 뒤의 be동사는 항상 현재형 'Is'로 써야 한다.\n다. 실제 주어 'a big meeting'이 단수이고 어제의 일이므로 과거형 'Was'를 사용한다.\n라. 이 질문에 부정으로 답할 때는 'No, there wasn't.'처럼 'there'를 살려 답한다.",
   pre=HJ("가 X. 실제 주어는 there가 아니라 a big meeting이다.", "나 X. 과거 시점(yesterday)이므로 과거형 Was를 쓴다.", "다 O. 단수·과거라 Was이다.", "라 O. there를 살려 No, there wasn't.로 답한다."), s=ADD(3, 9, "D", L9))
RE(3, 9, "E", p="<보기>\nWere there many people at the bus stop this morning?\n\n가. 실제 주어 'many people'이 복수이므로 be동사의 과거형 'Were'를 썼다.\n나. 지금의 일을 묻는다면 'Are there many people at the bus stop?'처럼 'Are'를 쓴다.\n다. 'people'은 -s가 붙지 않았으므로 단수 명사로 보아 'Was'를 써야 한다.\n라. 이 질문에 긍정으로 답할 때는 'Yes, there were.'처럼 답한다.",
   pre=HJ("가 O. 실제 주어가 복수라 Were이다.", "나 O. 현재라면 Are를 쓴다.", "다 X. people은 -s가 없어도 복수 명사이다.", "라 O. Yes, there were.로 답한다."), s=ADD(3, 9, "E", L9))
RE(3, 9, "F", p="<보기>\nIs there any water in the bottle on the table?\n\n가. 'water'는 셀 수 없는 명사라 단수 취급하므로 be동사 'Is'를 썼다.\n나. 'any'는 의문문에서 '조금이라도'라는 뜻으로 쓰였다.\n다. 이 문장의 실제 주어는 'there'이므로 단수형 'Is'를 사용한 것이다.\n라. 이 질문에 긍정으로 답할 때는 'Yes, it is.'라고 답한다.",
   pre=HJ("가 O. 셀 수 없는 명사는 단수 취급한다.", "나 O. 의문문의 any는 ‘조금이라도’의 뜻이다.", "다 X. there는 주어가 아니다.", "라 X. Yes, there is.로 답한다."), s=ADD(3, 9, "F", L9))

# ---- 3-13 C~F: 보기 문장을 원문항 길이(5~7낱말) 이상으로 ----
R13 = "불규칙동사의 과거형은 -ed를 붙이지 않고 따로 외운 형태를 쓴다(go - went, buy - bought, see - saw, write - wrote)."
def G13(v, b): return f"{v}: {b}의 과거형을 바르게 썼으므로"
def B13(v, b, ok): return f"{v}: {b}의 과거형은 {ok}이다. 어법상 틀린 부분이므로"
RE(3, 13, "C", st="R", c=["They <u>ate</u> lunch at the new restaurant.", "He <u>ran</u> very fast in the race.", "She <u>goed</u> home early after school.", "Mina <u>bought</u> a new bag yesterday.", "We <u>saw</u> a funny movie last night."], a=3, r=R13,
   n=OKS([G13("ate", "eat"), G13("ran", "run"), B13("goed", "go", "went"), G13("bought", "buy"), G13("saw", "see")], 3), s=ADD(3, 13, "C", LEN))
RE(3, 13, "D", st="R", c=["I <u>took</u> a bus to the museum yesterday.", "We <u>drank</u> cold water after the game.", "Tom <u>buyed</u> a new bike last weekend.", "Dad <u>made</u> a wooden box for me.", "Jane <u>came</u> home late last night."], a=3, r=R13,
   n=OKS([G13("took", "take"), G13("drank", "drink"), B13("buyed", "buy", "bought"), G13("made", "make"), G13("came", "come")], 3), s=ADD(3, 13, "D", LEN))
RE(3, 13, "E", st="R", c=["We <u>went</u> home right after the concert.", "Jane <u>ate</u> lunch with her friends today.", "Tom <u>wrote</u> a letter to his grandmother.", "They <u>met</u> a famous singer at the mall.", "I <u>seed</u> the movie twice last month."], a=5, r=R13,
   n=OKS([G13("went", "go"), G13("ate", "eat"), G13("wrote", "write"), G13("met", "meet"), B13("seed", "see", "saw")], 5), s=ADD(3, 13, "E", LEN))
RE(3, 13, "F", st="R", c=["Jane <u>writed</u> a letter to her pen pal.", "I <u>made</u> dinner for my family last night.", "Tom <u>bought</u> a bike with his own money.", "Mom <u>told</u> a funny story at dinner.", "They <u>came</u> early to help the teacher."], a=1, r=R13,
   n=OKS([B13("writed", "write", "wrote"), G13("made", "make"), G13("bought", "buy"), G13("told", "tell"), G13("came", "come")], 1), s=ADD(3, 13, "F", LEN))

# ---- 3-15 C~F: ⓐ~ⓔ 문장을 원문항 길이(34낱말) 이상으로 ----
RE(3, 15, "C", p="ⓐ Jane <u>studies</u> English with her tutor every Saturday.\nⓑ They <u>doesn't play</u> soccer on rainy days.\nⓒ <u>Does</u> Tom <u>likes</u> chocolate milk for breakfast?\nⓓ We <u>watch</u> TV together after dinner.\nⓔ He <u>don't read</u> comic books at school.", s=ADD(3, 15, "C", LEN))
RE(3, 15, "D", p="ⓐ Tom <u>went</u> home early because he was tired.\nⓑ She <u>didn't buy</u> the dress at the store.\nⓒ <u>Did</u> they <u>go</u> out for dinner last night?\nⓓ We <u>saw</u> a movie at the theater yesterday.\nⓔ Jane <u>didn't ate</u> anything for breakfast today.", s=ADD(3, 15, "D", LEN))
RE(3, 15, "E", p="ⓐ I <u>read</u> the newspaper every morning before school.\nⓑ He <u>doesn't study</u> much on the weekend.\nⓒ <u>Do</u> she <u>play</u> tennis with her brother?\nⓓ They <u>work</u> here at the bakery every day.\nⓔ Tom <u>goes</u> home early on Fridays.", s=ADD(3, 15, "E", LEN))
RE(3, 15, "F", p="ⓐ We <u>ate</u> sandwiches on the bus to the zoo.\nⓑ She <u>didn't see</u> him at the library yesterday.\nⓒ <u>Did</u> Tom <u>write</u> a letter to his uncle?\nⓓ They <u>goed</u> home by bus after the game.\nⓔ I <u>made</u> dinner for my parents last night.", s=ADD(3, 15, "F", LEN))

# ---- 3-25 C~F: ⓐ~ⓓ 문장을 원문항 길이(27낱말) 이상으로 ----
RE(3, 25, "C", p="ⓐ I ate breakfast at 7 with my family.\nⓑ She bought an umbrella at the station yesterday.\nⓒ We need an water to make the soup.\nⓓ Tom plays the soccer with his friends after school.", s=ADD(3, 25, "C", LEN))
RE(3, 25, "D", p="ⓐ He goes to school by a bus every morning.\nⓑ Jane has an hour before her piano lesson.\nⓒ They play soccer in the park on Sundays.\nⓓ I need an rice for dinner tonight.", s=ADD(3, 25, "D", LEN))
RE(3, 25, "E", p="ⓐ We had dinner at six with our grandparents.\nⓑ Tom bought an one-way ticket to Busan yesterday.\nⓒ She plays the violin in the school orchestra.\nⓓ There is an information about the trip on the board.", s=ADD(3, 25, "E", LEN))
RE(3, 25, "F", p="ⓐ She eats a apple after lunch every day.\nⓑ They go home by a taxi when it rains.\nⓒ We play tennis after school on Fridays.\nⓓ The sun rises in the east every morning.", s=ADD(3, 25, "F", LEN))

# ---- 3-29 C~F: (가)~(라) 문장을 원문항 길이(32낱말) 이상으로 ----
RE(3, 29, "C", p="(가) Tom goes to work <u>by the car</u> every morning.\n(나) Jane came to the party <u>by a taxi</u> last night.\n(다) We usually travel to Busan <u>by train</u>.\n(라) They went home <u>on foot</u> after the concert.", s=ADD(3, 29, "C", LEN))
RE(3, 29, "D", p="(가) I sent the photos to my aunt <u>by email</u>.\n(나) We went there <u>by the bus</u> last Saturday.\n(다) Tom traveled to Jeju Island <u>by a plane</u>.\n(라) Jane came to school <u>on foot</u> today.", s=ADD(3, 29, "D", LEN))
RE(3, 29, "E", p="(가) We spoke <u>by phone</u> for an hour last night.\n(나) Tom came to the stadium <u>by bike</u> with his friends.\n(다) Jane went to her grandmother's house <u>by a train</u>.\n(라) I went there <u>on feet</u> because the bus was late.", s=ADD(3, 29, "E", LEN))
RE(3, 29, "F", p="(가) They traveled to the island <u>by the ship</u> last summer.\n(나) She went to the airport <u>by taxi</u> early in the morning.\n(다) I sent the file to my teacher <u>by an email</u>.\n(라) We came to the park <u>on foot</u> this afternoon.", s=ADD(3, 29, "F", LEN))

# ---- 3-80 C~F: (가)~(마) 문장을 원문항 길이(46낱말) 이상으로 ----
RE(3, 80, "C", p="(가) It is easy for me to use this new app on my phone.\n(나) It was kind of Jane to help me with my homework.\n(다) I need a book to reading on the train tomorrow.\n(라) Tom went out to buy some milk for his mother.\n(마) She wants learning English with a native speaker.", s=ADD(3, 80, "C", LEN))
RE(3, 80, "D", p="(가) It is hard for him to understand the long story.\n(나) It was nice of you to come to my birthday party.\n(다) We have a quiet room to studying in after school.\n(라) She decided going home early because of the rain.\n(마) Tom is too tired to work on the project tonight.", s=ADD(3, 80, "D", LEN))
RE(3, 80, "E", p="(가) It is important for students to sleep well before a test.\n(나) It was careless of Tom to lose the key to the classroom.\n(다) Jane has something to eat in her lunch box.\n(라) We went to the hospital for see him after the accident.\n(마) He is enough old to drive a car in this country.", s=ADD(3, 80, "E", LEN))
RE(3, 80, "F", p="(가) It was wise for her to wait for the next bus.\n(나) It is necessary for us to leave now to catch the train.\n(다) I have a pen to write with in my pencil case.\n(라) Tom wants to study science at a big university.\n(마) She is too young driving a car by herself.", s=ADD(3, 80, "F", LEN))

# ---- 3-87 C~F: 문장과 보기를 원문항 길이(9낱말, 보기 8낱말) 이상으로 ----
R87 = "avoid, finish, keep, mind, enjoy, consider는 동명사를 목적어로 쓴다. to부정사나 동사원형을 목적어로 쓸 수 없다."
L87 = MEMO5 + "원문항보다 짧던 문장과 보기를 원문항 길이 이상으로 늘렸다. 틀린 곳과 정답 위치는 그대로다."
RE(3, 87, "C", st="R", p="She always avoids to meet him at the school library.", c=["She always avoids to meet him at the school library.", "She always avoids meet to him at the school library.", "She always avoids to meeting him at the school library.", "She always avoids meeting him at the school library.", "She always avoids meet him at the school library."], a=4, r=R87,
   n=OKS(["틀린 부분(to meet)을 그대로 두었으므로", "avoid 뒤에 동사원형을 쓸 수 없고 to의 자리도 틀렸으므로", "to를 그대로 두고 -ing만 붙였으므로", "avoid + 동명사(meeting)로 바르게 고쳤으므로", "avoid 뒤에 동사원형을 쓸 수 없으므로"], 4), s=L87 + pos(4))
RE(3, 87, "D", st="R", p="Tom finished to clean the room before his mother came home.", c=["Tom finished clean to the room before his mother came home.", "Tom finished to cleaning the room before his mother came home.", "Tom finished clean the room before his mother came home.", "Tom finished to clean the room before his mother came home.", "Tom finished cleaning the room before his mother came home."], a=5, r=R87,
   n=OKS(["finish 뒤에 동사원형을 쓸 수 없고 to의 자리도 틀렸으므로", "to를 그대로 두고 -ing만 붙였으므로", "finish 뒤에 동사원형을 쓸 수 없으므로", "틀린 부분(to clean)을 그대로 두었으므로", "finish + 동명사(cleaning)로 바르게 고쳤으므로"], 5), s=L87 + pos(5))
RE(3, 87, "E", st="R", p="They keep to talk to each other during the math class.", c=["They keep talk to each other during the math class.", "They keep talked to each other during the math class.", "They keeps talking to each other during the math class.", "They keep to talk to each other during the math class.", "They keep talking to each other during the math class."], a=5, r=R87,
   n=OKS(["keep 뒤에 동사원형을 쓸 수 없으므로", "keep 뒤에 과거형을 쓸 수 없으므로", "복수 주어 They에 keeps를 쓸 수 없으므로", "틀린 부분(to talk)을 그대로 두었으므로", "keep + 동명사(talking)로 바르게 고쳤으므로"], 5), s=ADD(3, 87, "E", L87 + pos(5)))
RE(3, 87, "F", p="Would you mind to turn off the light in the hallway?", c=["Would you mind turn off the light in the hallway?", "Would you mind turning off the light in the hallway?", "Would you mind to turning off the light in the hallway?", "Would you minding turning off the light in the hallway?", "Would you mind to turn off the light in the hallway?"], a=2, r=R87,
   n=OKS(["mind 뒤에 동사원형을 쓸 수 없으므로", "mind + 동명사(turning)로 바르게 고쳤으므로", "to를 그대로 두고 -ing만 붙였으므로", "would 뒤에는 동사원형 mind를 써야 하므로", "틀린 부분(to turn)을 그대로 두었으므로"], 2), s=ADD(3, 87, "F", L87 + pos(2)))

# ---- 3-110 C~F: 글을 원문항 길이(48낱말, 다섯 문장) 이상으로, 보기도 원문항(10낱말) 이상으로 ----
L110 = MEMO5 + "원문항보다 짧던 글을 다섯 문장으로 늘리고 보기도 원문항 길이 이상으로 했다. 틀린 곳과 정답 위치는 그대로다."
RE(3, 110, "C", p="Our class had a running race on the school playground yesterday. Tom, Ben, and Mike ran very fast. <u>Tom was the most fastest runner of the three boys in the final race</u>. He won a gold medal from our teacher. All of his classmates clapped loudly for him.",
   c=["Tom was the faster runner of the three boys in the final race.", "Tom was the fastest runner of the three boys in the final race.", "Tom was the most fast runner of the three boys in the final race.", "Tom was the very fast runner of the three boys in the final race.", "Tom was faster runner of the three boys in the final race."], a=2,
   n=OKS(["셋 중 가장 빠른 사람은 비교급이 아니라 최상급으로 나타내므로", "fast의 최상급 fastest로 바르게 고쳤으므로", "fast는 짧은 단어라 most fast가 아니라 fastest로 쓰므로", "very fast는 최상급이 아니므로", "셋 중 가장 빠른 사람은 the + 최상급으로 나타내므로"], 2), s=ADD(3, 110, "C", L110))
RE(3, 110, "D", p="Jane and Amy got their math test results back from the teacher today. Amy's score was good, but Jane's score was even better than hers. <u>So Jane was more happier than Amy about the math test result</u>. She smiled all day long at school. Amy said that she would study harder next time.",
   c=["So Jane was happiest than Amy about the math test result.", "So Jane was very happy than Amy about the math test result.", "So Jane was happy than Amy about the math test result.", "So Jane was happier than Amy about the math test result.", "So Jane was happily than Amy about the math test result."], a=4,
   n=OKS(["than 앞에는 최상급이 아니라 비교급을 쓰므로", "than 앞에는 very + 원급이 아니라 비교급을 쓰므로", "than 앞에는 원급이 아니라 비교급을 쓰므로", "happy의 비교급 happier로 바르게 고쳤으므로", "be동사 뒤 보어 자리에 부사를 쓸 수 없으므로"], 4), s=ADD(3, 110, "D", L110))
RE(3, 110, "E", p="We took a math test in the second period this morning. There were twenty questions on the test paper. <u>Question 1 was the most easiest question of all twenty questions on the paper</u>. But the last question was very hard for everyone. Only two students in our class got it right.",
   c=["Question 1 was the easiest question of all twenty questions on the paper.", "Question 1 was the easier question of all twenty questions on the paper.", "Question 1 was the very easy question of all twenty questions on the paper.", "Question 1 was the most easy question of all twenty questions on the paper.", "Question 1 was easier question of all twenty questions on the paper."], a=1,
   n=OKS(["easy의 최상급 easiest로 바르게 고쳤으므로", "of all(모든 것 중)에는 비교급이 아니라 최상급을 쓰므로", "very easy는 최상급이 아니므로", "easy의 최상급은 most easy가 아니라 easiest이므로", "of all에는 the + 최상급을 쓰므로"], 1), s=ADD(3, 110, "E", L110))
RE(3, 110, "F", p="I packed my bag for the school trip last night. My friend Minsu packed his bag for the trip, too. <u>My bag was more heavier than his bag on the school bus</u>. I had too many clothes and snacks in it. Minsu laughed at me when he saw my bag.",
   c=["My bag was heaviest than his bag on the school bus.", "My bag was very heavy than his bag on the school bus.", "My bag was heavy than his bag on the school bus.", "My bag was more heavy than his bag on the school bus.", "My bag was heavier than his bag on the school bus."], a=5,
   n=OKS(["than 앞에는 최상급이 아니라 비교급을 쓰므로", "than 앞에는 very + 원급이 아니라 비교급을 쓰므로", "than 앞에는 원급이 아니라 비교급을 쓰므로", "heavy의 비교급은 more heavy가 아니라 heavier이므로", "heavy의 비교급 heavier로 바르게 고쳤으므로"], 5), s=ADD(3, 110, "F", L110))

# ---- 3-98 C·E: 보기를 원문항처럼 a lot of·a few·a little을 더 섞어 보기 길이를 원문항 이상으로 ----
L98 = MEMO5 + "보기 길이가 원문항보다 짧아 원문항처럼 두 낱말 이상의 수량 표현을 더 섞었다. 정답 위치는 그대로다."
RE(3, 98, "C", c=["many - little - a lot of", "much - a few - a lot of", "much - little - many", "a lot of - little - much", "much - a little - much"], a=3,
   n=OKS(["(A) many: 셀 수 없는 milk에는 much를 써야 하므로", "(B) a few: very 뒤에 쓸 수 없고 셀 수 없는 milk를 가리키므로 little을 써야 하므로", "(A) 셀 수 없는 milk에 much, (B) ‘거의 없다’는 뜻의 little, (C) 셀 수 있는 eggs에 many가 모두 알맞으므로", "(A) a lot of: How 뒤의 수량 의문에는 much를 쓰고, (C) much: 셀 수 있는 eggs에는 many를 써야 하므로", "(B) a little: very 뒤에 쓸 수 없고 ‘조금 있다’는 뜻이라 사야 한다는 흐름과 맞지 않으며, (C) much: 셀 수 있는 eggs에는 many를 써야 하므로"], 3), s=ADD(3, 98, "C", L98))
RE(3, 98, "E", c=["a few - Much - much", "few - Much - a lot of", "a little - A lot of - many", "few - Many - much", "many - A few - a lot of"], a=4,
   n=OKS(["(A) a few: ‘조금 있다’는 뜻이라 ‘다섯 명뿐’이라는 흐름과 맞지 않고, (B) Much: 셀 수 있는 students에는 Many를 써야 하므로", "(B) Much: 셀 수 있는 students에는 Many를 써야 하므로", "(A) a little: 셀 수 있는 students에 쓸 수 없고, (C) many: 셀 수 없는 work에는 much를 써야 하므로", "(A) 다섯 명뿐이라 ‘거의 없는’ few, (B) 셀 수 있는 students에 Many, (C) 셀 수 없는 work에 much가 모두 알맞으므로", "(A) many: 다섯 명뿐인데 ‘많다’는 뜻이라 맞지 않고, (B) A few: 대부분이 축제에 갔다는 흐름과 맞지 않으므로"], 4), s=ADD(3, 98, "E", L98))
