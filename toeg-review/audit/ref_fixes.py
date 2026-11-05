# 기준 문항(원문항) 수정 내역: 원문항 점검(audit/ref_audit.json)에서 찾은 결함을 고친다.
# stem 발문 / passage 본문 전체 / psub 본문 부분 바꾸기 [(옛, 새)] / c {보기 번호(0~4): 새 보기} / ans 새 정답 / sum 수정 내용
# 수정 전 원문항은 apply_ref_fixes.py가 ref.json의 orig에 남기고, 내려받기용 엑셀(data/ref_changes.xlsx)로도 만든다.

FIXES = {
 # ---------- 1급 ----------
 "1-1": {"c": {0: "The flowers <u>smell sweet</u> in the garden."}, "sum": "보기 ① 끝에 마침표를 붙였다."},
 "1-6": {"c": {3: "to smell"}, "sum": "영어에 없는 철자 오류형 오답 ④ smalls를 to smell로 바꿨다."},
 "1-8": {"psub": [("• Could you ask a question (A)_________ the speaker?", "• May I ask a favor (A)_________ you?")],
         "sum": "ask a question to도 쓰여 정답 시비가 있던 (A) 문장을 of만 가능한 ‘May I ask a favor (A)___ you?’로 바꿨다. 정답은 그대로(④)."},
 "1-9": {"psub": [("(a) Don't leave the baby lonely.", "(a) Don't leave the door open.")],
         "sum": "뜻이 어색해 판단이 갈리던 (a)를 뜻과 어법이 분명한 ‘Don't leave the door open.’으로 바꿨다. 정답은 그대로(② 2개)."},
 "1-15": {"psub": [("a) She <u>has missed</u> her train this morning.", "a) She <u>has missed</u> her train yesterday morning.")],
          "sum": "오전이면 옳을 수 있던 a)의 this morning을 yesterday morning으로 바꿔 틀린 문장임을 분명히 했다. 정답은 그대로(③ 4개)."},
 "1-16": {"c": {2: "Yesterday, they like the pizza very much.", 4: "Look! The dog drank some water now."},
          "sum": "보기 넷이 진행형이라 형태만 보고 답이 나오던 것을, ③·⑤를 시간 표현과 시제가 어긋난 오답으로 바꿔 현재형·진행형·과거형이 섞이게 했다. 정답은 그대로(①)."},
 "1-19": {"stem": "다음 우리말과 같도록 빈칸 (A)~(C)에 들어갈 말이 바르게 짝지어진 것을 고르시오.",
          "sum": "선다형인데 ‘주어진 단어를 알맞은 형태로 빈칸에 쓰시오’였고 주어진 단어도 없던 발문을 고쳤다."},
 "1-39": {"psub": [("지문: The students were heard to sing loudly in the classroom.", "지문: <u>The students were heard to sing loudly in the classroom.</u>"),
                   ("이는 영어에서 본동사와 보어 동사가 원형으로 충돌하는 것을 피하기 위함이다.", "즉, 능동태에서 생략되었던 to가 수동태에서 다시 나타나는 것이다.")],
          "sum": "발문이 말하는 ‘밑줄 친 문장’에 밑줄을 긋고, 근거가 약한 설명(본동사와 보어 동사의 충돌을 피하기 위함)을 ‘생략되었던 to가 수동태에서 다시 나타난다’로 바꿨다."},
 "1-56": {"stem": "다음 중 주어진 단어를 활용하여 우리말 문장에 맞도록 영작한 것을 고르시오. (단, 주어진 단어 중 한 단어의 형태를 알맞게 바꾸어 사용할 것.)",
          "psub": [("( remember / that / read / to / I / book / . )", "( remember / that / read / I / book / . )")],
          "sum": "발문에 형태를 바꾸라는 조건을 붙이고, 정답에 쓰지 않는 to를 제시어에서 뺐다."},
 "1-57": {"c": {0: "being forgotten"}, "sum": "정답 ④ 외에 regret + 동명사로도 옳던 ① forgetting을 being forgotten으로 바꿔 정답을 하나로 했다."},
 "1-61": {"c": {4: "Pleased - frustrate"}, "sum": "①과 똑같던 보기 ⑤를 Pleased - frustrate로 바꿨다."},
 "1-63": {"passage": "(1) <u>The artwork was damaged in the fire last week</u>.\n(2) It is now being restored by experts.",
          "c": {0: "Damaging in the fire last week"},
          "sum": "Having been을 생략해도 옳던 ① Damaged …를 Damaging …으로 바꿔 정답을 하나로 하고, 뒷문장만 화살표로 보이던 두 문장을 (1)·(2)로 각각 제시했다."},
 "1-78": {"c": {0: "Nothing is more precious than time. → Time is more precious than anything else.",
                1: "No other boy in the village is as smart as he. → He is the smartest boy in the village.",
                2: "No other subject is easier than English for me. → English is easier than any other subject for me.",
                3: "Nothing is more important than health. → Health is less important than anything else.",
                4: "No other lake in this area is deeper than this lake. → This lake is deeper than any other lake in this area."},
          "sum": "전환 전 문장이 없어 정답 근거가 없던 보기를 ‘전환 전 → 전환 후’ 짝으로 바꾸고, ④만 뜻이 반대로 바뀌게 했다. 정답은 그대로(④)."},
 "1-89": {"psub": [("The man who is standing over there is my uncle.", "The man <u>who is standing</u> over there is my uncle.")],
          "sum": "발문이 말하는 ‘지문의 밑줄 친 부분’에 밑줄(who is standing)을 그었다."},
 "1-91": {"stem": "다음 직설법 문장을 가정법으로 바꿀 때 빈칸에 알맞은 것을 고르시오.", "sum": "서술형처럼 읽히던 발문(‘바꾸시오’)을 선다형 발문으로 고쳤다."},
 "1-96": {"stem": "괄호 안의 단어를 알맞은 형태로 바꿀 때 빈칸에 들어갈 말로 알맞은 것을 고르시오.", "sum": "선다형인데 ‘빈칸에 쓰시오’였던 발문을 고쳤다."},
 "1-97": {"c": {1: "If he had spoken the truth, there won’t be any problems."},
          "sum": "혼합가정법으로 옳던 ②를 there won’t be any problems로 바꿔 정답을 하나로 했다."},
 "1-98": {"c": {1: "Had he inherited much money from his mother, he would be rich now."}, "ans": "2",
          "sum": "제시어에 if가 없는데 정답이 If로 시작하던 것을 고쳤다. ②를 제시어로 만든 도치 문장(Had he inherited …)으로 바꾸고 정답을 ②로 고쳤다."},
 "1-100": {"c": {0: "Were it not for his courage, he could not save the child."},
           "sum": "우리말 조건과 다르다고 단정하기 어렵던 ①을 시제가 분명히 어긋나는 오답(Were it not for …, could not save)으로 바꿨다."},
 "1-108": {"c": {1: "She asked me <u>if I had seen</u> her keys."}, "sum": "보기 ②의 겹친 밑줄 태그를 하나로 고쳤다."},
 "1-122": {"c": {0: "None of the teachers attended the meeting.", 1: "No teacher attended the meeting.", 3: "All the teachers attended the meeting."},
           "sum": "all/every + not도 부분부정으로 읽혀 정답이 여럿이 될 수 있던 ①②④를 전체부정·긍정 문장으로 바꿨다. 정답은 그대로(③)."},
 "1-125": {"psub": [("D) None of the data were accurate.", "D) None of the information were accurate."),
                    ("F) When necessary, please contact the emergency services.", "F) When necessary, please contacting the emergency services.")],
           "sum": "틀린 문장이 1개뿐이라 정답 3개의 근거가 없던 것을, D·F를 분명히 틀린 문장으로 바꿔 틀린 문장을 A, D, F 3개로 맞췄다. 정답은 그대로(③)."},
 # ---------- 2급 ----------
 "2-10": {"c": {1: "(A) had it fixing - (B) have"}, "sum": "보기 ②의 띄어쓰기를 고쳤다."},
 "2-14": {"c": {0: "A: Have you ever been to Paris? B: Yes, I have been there twice."},
          "sum": "정답 ④ 외에 틀린 표현(for two times)이 있던 ①을 twice로 고쳐 틀린 대화를 하나로 했다."},
 "2-25": {"stem": "다음 중 밑줄 친 부분이 어법상 틀린 문장으로만 짝지어진 것은?",
          "sum": "발문(옳은 문장)과 정답 ③(ⓑ, ⓕ: 틀린 문장)이 어긋나 발문을 ‘틀린 문장으로만 짝지어진 것’으로 고치고 물음표를 붙였다. 정답은 그대로(③)."},
 "2-37": {"passage": "We heard the baby crying in the next room.",
          "c": {0: "The baby was heard to crying in the next room by us.", 1: "The baby is heard to crying in the next room by us.",
                2: "The baby was hearing cry in the next room by us.", 3: "The baby was heard cry in the next room by us.",
                4: "The baby was heard crying in the next room by us."},
          "sum": "2급 17번과 같던 제시 문장을 ‘We heard the baby crying in the next room.’으로 바꾸고 보기를 그에 맞췄다. 정답은 그대로(⑤)."},
 "2-44": {"passage": "<보기>\nThe principal <u>himself</u> attended the meeting.", "sum": "발문의 (보기)에 맞게 본문에 <보기> 표시를 붙였다."},
 "2-49": {"psub": [("Every student should believe in", "All students should believe in")],
          "sum": "himself도 옳다고 볼 수 있던 (A) 문장의 주어를 All students로 바꿔 themselves만 맞게 했다. 정답은 그대로(④)."},
 "2-56": {"c": {3: "a chair to sit in it"}, "sum": "①과 똑같던 보기 ④를 a chair to sit in it으로 바꿨다."},
 "2-75": {"stem": "다음 글의 밑줄 친 부분 중 어법상 틀린 것을 고르시오.", "sum": "선다형인데 ‘번호를 쓰시오’였던 발문을 고쳤다."},
 "2-89": {"psub": [("(D) One of the <u>boxes</u> in the room is empty.", "(D) One of the <u>box</u> in the room is empty.")],
          "sum": "옳은 문장이 셋이라 ⑤도 정답이 되던 것을, (D)를 틀린 문장(One of the box …)으로 바꿔 정답을 하나로 했다. 정답은 그대로(②)."},
 "2-99": {"passage": "I know a teacher <u>whose</u> class is very popular.", "sum": "class에 그어져 있던 밑줄을 발문대로 whose로 옮겼다."},
 "2-106": {"stem": "다음 빈칸에 들어갈 말로 가장 적절한 것을 고르시오.", "sum": "본문에 밑줄이 아니라 빈칸이 있어 발문의 ‘밑줄 친 부분’을 ‘빈칸’으로 고쳤다."},
 "2-110": {"psub": [("The cat jumped <u>across</u> the fence quickly.", "The cat jumped <u>over</u> the fence quickly.")],
           "sum": "옳은 문장으로 보기 어렵던 jumped across the fence를 jumped over the fence로 바꿔 정답(1개)의 근거를 분명히 했다."},
 "2-124": {"psub": [("if ⑤<u>you had been</u> more attentive", "if ⑤<u>you had paid</u> more attention")], "c": {4: "you had paid"},
           "sum": "②와 글자가 똑같던 ⑤의 밑줄 표현을 you had paid (more attention)로 바꿨다."},
 # ---------- 3급 ----------
 "3-9": {"psub": [("<보 기>", "<보기>")], "sum": "‘<보 기>’를 ‘<보기>’로 붙여 썼다."},
 "3-10": {"passage": "<보기>\n- Last night, there were a heavy rain.\n- The streets was very wet.\n- My shoes were dirty, but I was happy to get home.\n- My parents was worried about me, so they were waiting in the living room.",
          "sum": "발문의 <보기>에 맞게 본문에 <보기> 표시를 붙였다."},
 "3-19": {"psub": [("We ⓓtook many", "We ⓓ<u>took</u> many")], "sum": "ⓓ took에 빠진 밑줄을 그었다."},
 "3-36": {"c": {0: "They willn’t come to the party tomorrow.", 1: "They won’t come to the party tomorrow.", 2: "They don’t will come to the party tomorrow.", 3: "They aren’t come to the party tomorrow."},
          "sum": "줄임말의 억음 부호(`)를 아포스트로피(’)로 고쳤다."},
 "3-48": {"psub": [("(shoes / of / bought / my /\na / me / pair / mother / .)", "(shoes / of / bought / my / a / me / pair / mother / .)")], "sum": "제시어를 한 줄로 이어 썼다."},
 "3-54": {"stem": "빈칸에 들어갈 조동사로 가장 적절한 것을 고르시오.", "sum": "본문에 없는 (A) 표시를 발문에서 뺐다."},
 "3-56": {"passage": "She will join the club next month.",
          "c": {0: "She willn’t join the club next month.", 1: "She won’t join the club next month.", 2: "She doesn’t will join the club next month.",
                3: "She isn’t join the club next month.", 4: "She won’t joins the club next month."},
          "sum": "3급 36번과 같던 제시문을 ‘She will join the club next month.’로 바꾸고 보기를 맞췄다(억음 부호도 아포스트로피로). 정답은 그대로(②)."},
 "3-80": {"psub": [("(나) She studied very hard to not fail the exam.", "(나) She studied very hard not to failing the exam.")],
          "sum": "옳다고 볼 수도 있던 (나) to not fail을 분명히 틀린 not to failing으로 바꿔 정답을 하나로 했다. 정답은 그대로(④)."},
 "3-95": {"psub": [("Paul: He seldom visit us.", "Paul: He seldom visits us.")],
          "sum": "Paul의 예문(He seldom visit us)이 틀려 Paul의 설명도 틀렸던 것을, 예문을 He seldom visits us로 고쳐 정답 ②(Lisa, Jane)를 살렸다."},
 "3-97": {"stem": "다음 문장에서 밑줄 친 부분을 바르게 고친 것을 고르시오.", "sum": "선다형인데 ‘고치시오’였던 발문을 고쳤다."},
 "3-98": {"stem": "다음 대화의 빈칸 (A)~(C)에 들어갈 말로 알맞은 것을 고르시오.", "sum": "본문에 밑줄이 아니라 빈칸 (A)~(C)가 있어 발문을 고쳤다."},
 "3-102": {"c": {0: "Tom is older than Jerry."}, "sum": "표와 일치하지 않아 정답이 둘이던 ① Tom is as old as Jerry를 Tom is older than Jerry로 바꿨다. 정답은 그대로(④)."},
 "3-105": {"psub": [("ⓔ My sister", "ⓑ My sister"), ("문장 ⓔ에서", "문장 ⓑ에서")], "sum": "건너뛰던 기호 ⓐ, ⓔ를 ⓐ, ⓑ로 고쳤다."},
 "3-106": {"stem": "다음 대화에서 괄호 안의 단어를 알맞은 형태로 바꾼 것을 고르시오.", "sum": "조사가 어색하던 발문을 고쳤다."},
 "3-107": {"stem": "다음 두 문장의 의미가 같도록 빈칸에 알맞은 말을 고르시오.", "sum": "선다형인데 ‘쓰시오’였던 발문을 고쳤다."},
 "3-108": {"stem": "다음 단어들을 바르게 배열하여 문장을 완성한 것을 고르시오. (필요하면 단어의 형태를 바꿀 것)",
           "psub": [("( the / Seoul / one / of / large /\ncity / is / world / in / the / . )", "( the / Seoul / one / of / large / city / is / world / in / the / . )")],
           "sum": "정답에 필요한 형태 변화(largest, cities) 조건을 발문에 붙이고, 제시어를 한 줄로 썼다."},
 "3-125": {"stem": "다음 두 문장이 같은 의미가 되도록 빈칸에 알맞은 말을 고르시오.", "sum": "선다형인데 ‘쓰시오’였던 발문을 고쳤다."},
 "3-140": {"stem": "다음 대화의 빈칸 (A)~(C)에 들어갈 표현으로 알맞게 짝지어진 것을 고르시오.", "sum": "본문에 밑줄이 아니라 빈칸 (A)~(C)가 있어 발문을 고쳤다."},
 # ---------- 4급 ----------
 "4-28": {"stem": "다음 문장을 읽고 문법적으로 잘못된 설명을 한 학생을 고르시오.", "c": {1: "지혜: need가 일반동사라서 Does로 묻는 일반동사 의문문이야."},
          "sum": "근거가 틀려 잘못된 설명으로도 볼 수 있던 ②를 바른 근거(need가 일반동사)로 고치고, 제시문이 한 문장이라 발문의 ‘대화’를 ‘문장’으로 고쳤다. 정답은 그대로(③)."},
 "4-53": {"c": {1: "‘must’는 ‘may’보다 더 강한 확신을 나타낸다."}, "sum": "틀린 설명이라 정답이 둘이던 ②를 ‘must는 may보다 더 강한 확신’으로 고쳤다. 정답은 그대로(④)."},
 "4-59": {"c": {1: "(A) could not / (B) went"}, "sum": "보기 ②의 첫 기호 오타 (B)를 (A)로 고쳤다."},
 "4-85": {"psub": [("ⓑ Please sit in the chair.", "ⓑ Please sit in the floor.")],
          "sum": "옳은 표현으로 볼 수 있던 ⓑ sit in the chair를 분명히 틀린 sit in the floor로 바꿔 정답을 하나로 했다. 정답은 그대로(②)."},
 "4-86": {"stem": "다음 우리말과 같도록 빈칸에 알맞은 단어는?", "sum": "그림이 없는데 ‘그림의 상황’이라던 발문을 고쳤다."},
 "4-102": {"c": {3: "kindness"}, "sum": "형용사(상냥한)로도 쓰여 오답이 분명하지 않던 ④ kindly를 kindness로 바꿨다. 정답은 그대로(④)."},
 # ---------- 5급 ----------
 "5-50": {"passage": "<보기>\n너는 정오에 뭐하고 있었니?", "sum": "발문의 <보기>에 맞게 본문에 <보기> 표시를 붙였다."},
 "5-70": {"stem": "다음 지문에서 밑줄 친 부분의 어법상 틀린 점을 모두 찾아 바르게 고쳐 설명한 것을 고르세요.",
          "sum": "①·②도 틀린 설명은 아니라서, 정답 ③만 맞도록 발문에 ‘모두’를 넣었다."},
 "5-88": {"psub": [("(the / between / is / The / and /\ncat / dog / the / at / bird)", "(the / between / is / The / and / cat / dog / the / bird)")],
          "sum": "정답에 쓰지 않는 at을 제시어에서 빼고 한 줄로 썼다."},
 "5-96": {"passage": "I have a pencil _______ an eraser.\n(나는 연필 한 자루와 지우개 하나를 가지고 있다.)", "c": {4: "because"},
          "sum": "with도 들어갈 수 있어 정답이 둘이던 것을, 우리말 뜻을 붙이고 ⑤를 because로 바꿔 정답을 하나로 했다. 정답은 그대로(④)."},
 "5-97": {"c": {0: "<u>When</u> I got home, my mom was cooking.", 1: "I'll call you <u>after</u> I finish my homework.", 2: "He left <u>before</u> the meeting.",
                3: "We waited <u>until</u> the rain stopped.", 4: "I was happy <u>because</u> I passed the test."},
          "sum": "5급 CH10(접속사) 문항인데 형용사/부사를 묻던 보기를 접속사 문항으로 바꿨다. ③ before만 명사 앞의 전치사이고 나머지는 절을 이끄는 접속사다. 정답은 그대로(③)."},
 "5-100": {"c": {1: "(B)처럼 'After'로 시작하는 문장이 앞에 올 때는 보통 쉼표(,)를 사용하여 뒷부분과 구분한다."},
           "sum": "‘반드시 쉼표’라는 지나친 일반화로 틀린 설명이 될 수 있던 ②를 ‘보통 쉼표로 구분한다’로 고쳤다. 정답은 그대로(④)."},
 # ---------- 6급 ----------
 "6-20": {"stem": "다음 지문을 읽고, 밑줄 친 (A)~(D)에 대한 설명으로 문법적으로 옳은 것을 고르세요.", "sum": "본문의 기호 (A)~(D)와 다르던 발문(①~⑤)을 고쳤다."},
 "6-27": {"psub": [("B: No, she ________ in the library.", "B: No, she ________. She was in the library.")],
          "sum": "정답을 넣으면 ‘No, she wasn’t in the library.’가 되어 뜻이 어긋나던 B의 말을 ‘No, she ___. She was in the library.’로 바꿨다. 정답은 그대로(②)."},
 "6-59": {"c": {2: "1인칭 복수"}, "ans": "5", "sum": "he(3인칭 단수)인데 정답이 ④(3인칭 복수)로 되어 있던 것을 ⑤로 고치고, ②와 똑같던 ③을 ‘1인칭 복수’로 바꿨다."},
 "6-88": {"psub": [("The ①<u>birds</u> ②<u>is</u>", "The two ①<u>birds</u> ②<u>is</u>")],
          "sum": "birds를 고쳐도 is를 고쳐도 옳은 문장이 되던 것을, 주어를 The two birds로 바꿔 ② is만 틀린 것이 되게 했다. 정답은 그대로(②)."},
 "6-93": {"ans": "4", "sum": "정답 ①(was not – play)을 넣으면 ‘Was she play the flute?’가 되던 정답 오류를 ④(wasn't - playing)로 고쳤다."},
 "6-110": {"psub": [("<보 기>", "<보기>")], "sum": "‘<보 기>’를 ‘<보기>’로 붙여 썼다."},
 # ---------- 7급 ----------
 "7-79": {"stem": "다음 지문을 읽고 밑줄 친 ①~⑤ 중 문법적으로 틀린 것을 고르세요.", "sum": "글의 번호(①~⑤)와 다르던 발문(ⓐ~ⓔ)을 고쳤다."},
 "7-81": {"stem": "다음 문장에서 ‘can’이 들어갈 위치를 고르시오.", "sum": "발문의 따옴표 짝을 고쳤다."},
 "7-90": {"stem": "다음 중 밑줄 친 부분이 문법적으로 옳은 문장으로 짝지어진 것을 고르시오.", "sum": "발문 끝의 잘못된 물음표를 지웠다."},
 "7-95": {"c": {3: "We live on the <u>ninth</u> floor.(우리는 9층에 산다.)"}, "sum": "층 앞의 전치사가 틀려(in the ninth floor) 학생이 고를 수 있던 ④를 on으로 고쳤다. 정답은 그대로(①)."},
}

# 보기 구분 기호 통일(- 와 – 가 섞인 문항): 보기 안의 – 를 - 로 바꾼다
DASH = ["1-112", "2-111", "3-1", "3-4", "3-14", "3-23", "3-44", "3-93", "3-94", "3-101", "3-104", "3-114", "3-124", "3-133",
        "4-1", "4-11", "4-22", "4-87", "4-91", "5-2", "5-44", "5-52", "5-61", "5-63", "5-64", "5-74",
        "6-1", "6-31", "6-44", "6-81", "6-83", "6-93", "6-94", "6-97", "7-9", "7-11", "7-12", "7-33", "7-35", "7-38", "7-52", "7-53", "7-94"]
DASH_P = ["7-96"]   # 본문에 섞인 것

# ---------- 2차 감수(2026-10)에서 추가한 수정 ----------
def _add(key, **kw):
    cur = FIXES.setdefault(key, {})
    for f in ("stem", "passage", "ans"):
        if f in kw: cur[f] = kw[f]
    if "c" in kw: cur.setdefault("c", {}).update(kw["c"])
    if "psub" in kw: cur.setdefault("psub", []).extend(kw["psub"])
    cur["sum"] = (cur["sum"] + " / " if cur.get("sum") else "") + kw["sum"]

_add("1-4", c={0: "My cousin will marry with a pilot next month."},
     sum="① ‘attend to the meeting’은 attend to(~을 처리하다)로 읽으면 옳은 문장이 될 수 있어, 뜻과 상관없이 틀린 ‘marry with’ 문장으로 바꿨다. 정답은 그대로(⑤).")
_add("1-19", c={4: "arrived - had - finish"},
     sum="⑤ arrived - was - finished는 ‘the meeting was already finished(회의가 이미 끝난 상태였다)’로 옳은 문장이 되어 정답이 둘이 될 수 있었다. 분명히 틀린 ‘arrived - had - finish’로 바꿨다. 정답은 그대로(④).")
_add("1-117", c={1: "talked - not to"},
     sum="② asked - not to는 ‘The doctor asked him not to smoke too much.’로 옳은 문장이 되어 정답이 둘이 될 수 있었다. 분명히 틀린 ‘talked - not to’로 바꿨다. 정답은 그대로(③).")
_add("1-120", c={1: "(가), (다)"},
     sum="발문이 ‘틀린 문장으로만 묶인 것’인데 ② (나), (다)도 틀린 문장으로만 묶여 정답 ④와 함께 조건을 만족했다. ②를 옳은 문장이 섞인 ‘(가), (다)’로 바꿨다. 정답은 그대로(④).")
_add("2-60", c={4: "수진: (E)는 '의도'의 의미로, 그가 위대한 예술가가 되려고 마음먹었다는 뜻이에요."},
     sum="⑤ 수진의 설명은 ‘숙명이나 의도’라고 하면서도 뒷부분(‘원했든 아니든 그렇게 될 운명이었다’)은 (E)의 뜻을 바르게 말해, 틀린 설명이 없다고 볼 수 있었다. ⑤를 분명히 틀린 설명((E)를 ‘의도’로 풂)으로 바꿨다. 정답은 그대로(⑤).")
_add("3-117", passage="Please finish your work <u>until</u> 5 p.m.\n(오후 5시까지 일을 끝내 주세요.)",
     sum="② at을 넣은 ‘Please finish your work at 5 p.m.’(5시에 일을 끝내라)도 옳은 문장이라 고친 것이 둘로 보일 수 있었다. 같은 단원의 다른 문항처럼 제시문 아래에 우리말 뜻(오후 5시까지)을 붙여 기한의 뜻이 드러나게 했다. 정답은 그대로(①).")
for _k in ("4-58", "4-97", "6-65", "6-68"):
    _add(_k, stem="다음 두 문장의 의미가 같도록 빈칸에 알맞은 말을 고르시오.", sum="선다형인데 ‘쓰시오’였던 발문을 고쳤다.")
_add("5-34", c={4: "No, they wasn’t."}, sum="⑤에 마침표가 빠져 있어 넣었다. 정답은 그대로(②).")
_add("6-6", c={2: "two"}, sum="③ the를 넣은 ‘He is eating the orange.’도 옳은 문장이라 정답이 둘이 될 수 있었다. ③을 two로 바꿨다. 정답은 그대로(②).")
_add("6-102", c={4: "take off your shoes"}, sum="⑤에만 붙어 있던 마침표를 지웠다(본문 Don't ___. 에 이미 마침표가 있다). 정답은 그대로(③).")

# ---------- 2026-10-06 B유형 전급수 감수 메모 반영(원형 문항 수정) ----------
_add("1-38", passage="The committee awarded her the prize for her outstanding research.\n→ The prize (<u>        </u>) for her outstanding research by the committee.",
     sum="감수 메모 반영: 앞 문장을 뒷 문장으로 바꾼다는 뜻이 드러나도록 두 문장 앞의 ‘-’를 지우고 둘째 문장 앞에 ‘→’를 붙였다.")
_add("1-56", stem="다음 중 주어진 단어를 활용하여 우리말 문장에 맞도록 영작한 것을 고르시오. (단, 단어의 형태는 필요에 따라 바꿀 수 있다.)",
     sum="감수 메모 반영: ‘한 단어의 형태를 바꾸어’라는 조건과 달리 두 단어의 형태가 바뀐 보기(remembered to read)가 있어, 조건을 ‘단어의 형태는 필요에 따라 바꿀 수 있다’로 고쳤다.")
_add("1-58", c={0: "Parents prevent their children eats from junk food.", 3: "Parents prevent their children from eats junk food."},
     sum="감수 메모 반영: 조건(한 단어의 형태를 바꾸어)과 달리 바뀐 형태가 없던 ①·④를 eat의 형태를 바꾼 오답(eats)으로 고쳤다. 정답은 그대로(③).")
_add("1-70", stem="다음 중 분사구문의 쓰임이 어법상 옳은 문장을 고르시오.", passage="",
     sum="감수 메모 반영: <조건>(분사구문 사용, 다른 주어 명시)이 너무 단순해 조건 없이 분사구문이 어법상 옳은 문장을 고르는 발문으로 바꾸고 <조건>을 지웠다. 보기와 정답은 그대로(②).")
_add("1-98", c={2: "Had he inherited much money from his mother, he would rich be now.", 3: "He had inherited much money from his mother, he would be rich now.", 4: "Had inherited he much money from his mother, he would be rich now."},
     sum="감수 메모 반영: 주어진 낱말을 다 쓰지 않거나(③ had 빠짐) 없는 낱말(If)을 쓴 ④·⑤를, 주어진 낱말만으로 어순이 틀린 오답으로 바꿨다. 정답은 그대로(②).")
_add("2-14", c={0: "A: Have you ever been to Paris?\nB: Yes, I have been there twice.", 1: "A: How long have you lived here?\nB: I have lived here for 5 years.", 2: "A: What are you doing now?\nB: I am reading a book.",
                3: "A: When did you finish your homework?\nB: I have finished it an hour ago.", 4: "A: Will you go to the party tonight?\nB: Yes, I will. I'm looking forward to it."},
     sum="감수 메모 반영: A와 B의 대화를 줄을 바꿔 제시했다.")
_add("2-94", c={0: "(a)-ㄱ, (b)-ㄴ", 1: "(a)-ㄴ, (b)-ㄷ", 2: "(a)-ㄹ, (b)-ㄷ", 3: "(a)-ㄹ, (b)-ㄴ", 4: "(a)-ㄱ, (b)-ㄷ"},
     sum="감수 메모 반영: 보기를 ‘(a)-ㄹ, (b)-ㄷ’처럼 (a)·(b)를 밝힌 형태로 바꿨다. 정답은 그대로(③).")
_add("3-9", psub=[("Is there a cat in the room?\n가. ", "Is there a cat in the room?\n\n가. ")], sum="감수 메모 반영: <보기> 문장과 설명 가~라 사이에 빈 줄을 넣어 구분했다.")
_add("3-40", psub=[("Dear Diary,\n", "")], sum="감수 메모 반영: 편지도 일기도 아닌 형식이 되던 첫 줄 ‘Dear Diary,’를 지웠다.")
_add("3-62", c={0: "A: How often do you exercise?\nB: Twice a week.", 1: "A: Where did you buy that shirt?\nB: I bought it online.", 2: "A: Why were you late?\nB: The traffic was heavy.",
                3: "A: When is the meeting?\nB: It's on the third floor.", 4: "A: What time do you usually wake up?\nB: Around 7 AM."},
     sum="감수 메모 반영: 질문(A)과 대답(B)을 줄을 바꿔 제시했다.")
_add("3-91", passage="나는 풀어야 할 어려운 문제가 하나 있다.\n① I ② have ③ a ④ problem ⑤ to solve.", c={0: "①", 1: "②", 2: "③", 3: "④", 4: "⑤"},
     sum="감수 메모 반영: 영어 문장을 제시문에 보이고 낱말 사이에 번호를 넣었다. 보기는 번호만 두었다. 정답은 그대로(④).")
_add("3-92", c={0: "①", 1: "②", 2: "③", 3: "④", 4: "⑤"},
     sum="감수 메모 반영(위치 문항 전수 조사): 뒤에 오는 낱말까지 적혀 있던 보기를 번호만으로 바꿨다. 정답은 그대로(③).")
_add("3-108", c={1: "The Seoul is one of largest cities in the world.", 3: "Seoul is the one of largest cities in the world.", 4: "Seoul is one of the larger cities in the world."},
     sum="감수 메모 반영: 주어진 낱말을 다 쓰지 않거나 없는 낱말(most)을 쓴 ②·④·⑤를 주어진 낱말만 쓴 오답으로 바꿨다. 정답은 그대로(③).")
_add("3-140", psub=[("\n(A)\t(B)\t(C)", "")], c={0: "(A) don’t - (B) How - (C) How", 1: "(A) don’t - (B) Why - (C) How", 2: "(A) shall - (B) Why - (C) What", 3: "(A) shall - (B) Why - (C) How", 4: "(A) shall - (B) How - (C) What"},
     sum="감수 메모 반영: 지문 끝의 ‘(A) (B) (C)’ 줄을 지우고 보기마다 (A)·(B)·(C)를 붙였다. 정답은 그대로(③).")
_add("4-30", psub=[("(A)________(live)", "(A)____(live)"), ("(B)________(have)", "(B)____(have)"), ("(C)________(visit)", "(C)____(visit)")],
     sum="감수 메모 반영: 긴 빈칸 때문에 줄바꿈이 어색해 빈칸을 변형 문항과 같은 길이(____)로 줄였다.")
_add("4-41", c={0: "①", 1: "②", 2: "③", 3: "④", 4: "⑤"},
     sum="감수 메모 반영: 뒤에 오는 낱말까지 적혀 있던 보기를 번호만으로 바꿨다. 정답은 그대로(②).")
_add("4-51", c={0: "She <u>is able to</u> swim very well.", 1: "She <u>may</u> swim very well.", 2: "She <u>must</u> swim very well.", 3: "She <u>has to</u> swim very well.", 4: "She <u>might</u> swim very well."},
     sum="감수 메모 반영: 제시문의 can에만 있던 밑줄을 보기의 해당 부분에도 그어 밑줄을 통일했다.")
_add("4-92", c={0: "_____ big dogs they are!", 4: "_____ wonderful weather it is!"},
     sum="감수 메모 반영: 빈칸 뒤의 a/an만 보고 답을 찾을 수 있어, ①·⑤를 a/an 없이 ‘형용사 + 명사’가 오는 What 감탄문으로 바꿨다. 정답은 그대로(③).")
_add("5-82", passage="내 사촌은 서울에 산다.\n① My ② cousin ③ lives ④ Seoul ⑤.", c={0: "①", 1: "②", 2: "③", 3: "④", 4: "⑤"},
     sum="감수 메모 반영: 영어 문장을 제시문에 보이고 낱말 사이에 번호를 넣었다. 보기는 번호만 두었다. 정답은 그대로(④).")
_add("6-6", c={2: "two", 3: "many", 4: "three"},
     sum="감수 메모 반영: be동사 오답(is, are)을 수와 관련된 오답(many, three)으로 바꿨다. 정답은 그대로(②).")
_add("6-16", c={4: "isn't"}, sum="감수 메모 반영: 아직 배우지 않은 be동사 과거형 was를 보기에서 빼고 현재형의 부정형 isn't로 바꿨다. 정답은 그대로(③).")
_add("6-20", c={1: "(A)의 Those는 멀리 있는 여러 개를 가리키며 복수 be동사 are와 함께 쓴다."},
     sum="감수 메모 반영: 이 단계에서 설명하지 않는 ‘짝을 이루는 물건은 복수형’ 내용의 ②를 지시어와 be동사의 수 일치에 대한 옳은 설명으로 바꿨다. 정답은 그대로(②).")
_add("6-21", stem="다음 빈칸에 들어갈 알맞은 be동사의 과거형을 고르시오.", passage="She _______ happy yesterday.", c={0: "am", 1: "was", 2: "were", 3: "be", 4: "is"},
     sum="감수 메모 반영: 문장 없이 형태만 고르던 문항을, 변형 문항처럼 예시 문장의 빈칸에 알맞은 be동사 과거형을 고르는 문항으로 바꿨다. 정답은 그대로(②).")
_add("6-29", c={0: "was very blue", 1: "were under the umbrella", 2: "was in the water", 3: "were very excited", 4: "was a wonderful day"},
     sum="감수 메모 반영: 번호만 있던 보기를 변형 문항처럼 밑줄 친 be동사와 그 뒷말로 보였다(주어는 보기에 넣지 않았다). 정답은 그대로(③).")
_add("6-32", stem="다음 중 밑줄 친 동사에 s가 붙지 않는 것은?",
     c={0: "My sister <u>like</u> apples.", 1: "The sun <u>rise</u> in the east.", 2: "I <u>eat</u> breakfast at eight.", 3: "My cat <u>sleep</u> on the bed.", 4: "She <u>speak</u> English well."},
     sum="감수 메모 반영: 동사 뒤 빈칸(like___) 형식을 밑줄 친 동사 형식으로 바꾸고 발문을 ‘밑줄 친 동사에 s가 붙지 않는 것은?’으로 고쳤다. 정답은 그대로(③).")
_add("6-41", c={4: "open - opened"}, sum="감수 메모 반영: 이 단계에서 다루지 않는 불규칙 과거형 ⑤ buy - bought를 규칙 과거형 open - opened로 바꿨다. 정답은 그대로(③).")
_add("6-45", passage="He studies English.",
     c={0: "He studyed English yesterday.", 1: "He did studied English yesterday.", 2: "He studied English yesterday.", 3: "He studies English yesterday.", 4: "He study English yesterday."},
     sum="감수 메모 반영: 이 단계에서 다루지 않는 불규칙 동사(make - made)를 규칙 동사(study - studied)로 바꿔 문장과 보기를 새로 썼다. 정답은 그대로(③).")
_add("7-81", passage="① My ② mom ③ bake ④ bread ⑤.", c={0: "①", 1: "②", 2: "③", 3: "④", 4: "⑤"},
     sum="감수 메모 반영: 발문의 ‘다음 문장’이 보이지 않아 번호를 넣은 문장을 제시문에 보이고, 보기는 번호만 두었다. 정답은 그대로(③).")

# ---- 2026-10-21 검토 페이지 ‘부적합’ 메모 반영 ----
_add("1-56", stem="다음 우리말을 영어로 바르게 옮긴 것을 고르시오.", passage="나는 그 책을 읽은 것을 기억한다.",
     c={0: "I remember to read that book.", 1: "I remembered reading that book.", 2: "I remember that I will read that book.", 3: "I remember read that book."},
     sum="감수 메모 반영: 제시어 조건 때문에 오류가 되풀이되어, 제시어 없이 우리말 문장만 주고 알맞은 영어 문장을 고르는 유형으로 바꿨다(변형 B~F도 같게). 오답은 remember to / remembered -ing / will / 동사원형으로 다시 짰다. 정답은 그대로(⑤).")
_add("7-12", passage="<보기>\nI - my", c={0: "he - his", 1: "her - she", 2: "they - their", 3: "you - your", 4: "it - its"},
     sum="감수 메모 반영: 7급에서 배우지 않은 목적격 대신 주격 - 소유격 관계(I - my)로 바꿨다. 관계가 다른 짝은 순서가 거꾸로인 her - she. 정답은 그대로(②).")
_add("7-97", passage="Today ______ Monday. Tomorrow is Tuesday.", c={0: "am", 1: "are", 2: "is", 3: "do", 4: "does"}, ans=3,
     sum="감수 메모 반영: 7급에서 배우지 않은 과거형(was/were) 대신 현재형 be동사(am/is/are)와 do/does 가운데 고르는 문항으로 바꿨다. 정답 ③ is.")
FIXES["1-56"].pop("psub", None)  # 본문을 통째로 바꿨으므로 옛 제시어 치환은 더 쓰지 않는다

# ---- 2026-11-05 사용자 요청: 1-81 원문항 정답 유일성 ----
_add("1-81", c={1: "which"},
     sum="감수 메모 반영(2026-11-05): ② whose는 ‘a place whose biodiversity thrives’로도 문법상 성립해 복수 정답 소지가 있어, 확실한 오답인 관계대명사 which로 바꿨다(뒤 절 biodiversity thrives는 빠진 성분이 없는 완전한 절이라 which가 들어갈 수 없다). 정답은 그대로(① where).")
