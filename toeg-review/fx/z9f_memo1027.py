# 2026-10-27 감수 반영(사용자: 4급 D·E·F를 빼고 1차 감수 완료, 확인 완료 문항은 그대로). 확인 완료가 아닌 문서에 10-26 이후 새로 달린 메모(F 1~3급, C 4급, 3-96 B~F)를 반영하고,
# 같은 번호의 아직 감수하지 않은 4급 D·E·F 중 같은 결함(원문항보다 짧음)이 있는 것도 함께 늘린다.
def ADD(g_, n_, t_, more): return (OLD(g_, n_, t_).get("s", "") + " " + more).strip()
M = "감수 메모 반영(10-27): "
SAME = "같은 번호 메모에 맞춘 수정(10-27): "
U_ = lambda s: s.replace("_U_", "<u>").replace("_u_", "</u>")

# ---- 1급 F ----
RE(1, 4, "F", s=ADD(1, 4, "F", M + "①과 ③이 같은 동사 reach라 정답이 드러나던 것을 ①을 marry with로 바꿨다."),
   c=["My aunt married with a famous pianist last spring.", "Mina discussed about the plan with her classmates.", "The hikers reached the shelter on the mountain before dark.",
      "She resembles with her older sister in many ways.", "He entered into the room without knocking on the door."], a=3,
   k="reach는 전치사 없이 목적어를 바로 받는 타동사이고 ③은 reached the shelter로 바르게 썼으므로 정답은 ③이다.",
   n=["marry는 전치사 없이 목적어를 바로 받는 타동사라 married with가 아니라 married a famous pianist로 써야 하므로 오답이다.",
      "discuss는 타동사라 discussed about이 아니라 discussed the plan으로 써야 하므로 오답이다.",
      "reach는 전치사 없이 목적어를 바로 받는 타동사인데 reached the shelter로 바르게 썼으므로 정답이다.",
      "resemble은 타동사라 resembles with가 아니라 resembles her older sister로 써야 하므로 오답이다.",
      "enter는 ‘들어가다’의 뜻일 때 전치사 없이 목적어를 받으므로 entered into가 아니라 entered the room으로 써야 하므로 오답이다."])
RE(1, 47, "F", s=ADD(1, 47, "F", M + "③ to be brief도 답이 될 수 있어 보이던 것을 뜻이 분명히 다른 sad to say로 바꿨다."),
   c=["to begin with", "strange to say", "sad to say", "so to speak", "to make matters worse"], a=4,
   r="독립부정사는 문장 전체를 꾸미는 관용 표현이다. To begin with(우선), Needless to say(말할 필요도 없이), Strange to say(이상한 말이지만), Sad to say(유감스럽게도), So to speak(말하자면), To make matters worse(설상가상으로)를 흐름에 맞게 고른다.",
   k="삼촌을 실제 사전이 아니라 ‘걸어 다니는 사전’에 빗대어 말하므로 ‘말하자면’의 so to speak가 알맞다. 정답은 ④이다.",
   n=["‘우선’은 여러 가지를 차례로 말할 때 쓰므로 오답이다.", "‘이상한 말이지만’은 뜻밖의 일을 말할 때 쓰므로 오답이다.",
      "‘유감스럽게도’는 안타까운 일을 말할 때 쓰는데, 삼촌을 칭찬하는 흐름과 맞지 않으므로 오답이다.",
      "삼촌을 실제 사전이 아니라 ‘걸어 다니는 사전’에 빗대어 말하므로 ‘말하자면’이 알맞아 정답이다.", "‘설상가상으로’는 나쁜 일이 겹칠 때 쓰므로 오답이다."])
RE(1, 99, "F", s=ADD(1, 99, "F", M + "대화문을 원문항 길이 이상으로 늘렸다."),
   p="Tom: I got soaked in the heavy rain on my way home yesterday. I'm still cold.\nJane: That's awful. (<u>                </u>)")
RE(1, 122, "F", s=ADD(1, 122, "F", M + "우리말과 보기 문장을 원문항 길이 이상으로 늘렸다."),
   p="모든 학생들이 그 계획에 동의한 것은 아니다.",
   c=["The students all not agreed with the plan.", "No all students agreed with the plan.", "All students agreed with the plan.", "None of the students agreed with the plan.", "Not all students agreed with the plan."], a=5,
   k="‘모든 학생들이 그 계획에 동의한 것은 아니다’는 일부만 동의했다는 부분부정이므로 Not all students agreed with the plan.이 알맞다. 정답은 ⑤이다.",
   n=["all not은 부분부정의 바른 형태가 아니므로 오답이다(Not all students …).", "No all이라는 표현은 쓰지 않으므로 오답이다.",
      "부정어가 없어 ‘모든 학생이 동의했다’는 전체 긍정이 되므로 오답이다.", "None of는 ‘아무도 동의하지 않았다’는 전체부정이므로 오답이다.",
      "Not all + 명사로 ‘모두가 ~한 것은 아니다’라는 부분부정을 바르게 나타냈으므로 정답이다."])
RE(1, 125, "F", s=ADD(1, 125, "F", M + "A)~F) 문장을 원문항 길이 이상으로 늘렸다. 틀린 문장(B·C·D·F)은 그대로다."),
   p="A) Leo as well as his teammates is practicing hard for the final match.\nB) Neither Mina nor her parents is at home this evening.\nC) Either the coach or the players has the key to the locker room.\n"
     "D) Not only the cats but also the dog were hungry after the long walk.\nE) Both rain and snow are expected in the mountains tonight.\nF) Every one of the answers on the test paper are correct.")

# ---- 2급 F ----
RE(2, 8, "F", s=ADD(2, 8, "F", M + "<보기>와 보기 문장을 원문항 길이 이상으로 늘렸다."),
   p="<보기>\nThey left the classroom door <u>open</u> all night.",
   c=["The room remained <u>quiet</u> during the test.", "She spoke <u>calmly</u> to the angry customer.", "They agreed <u>to help</u> their new neighbor.",
      "My uncle seems <u>busy</u> with his work these days.", "I considered the plan <u>risky</u> for our small team."], a=5,
   k="<보기>의 open과 ⑤의 risky는 모두 목적어(the classroom door, the plan)의 상태를 설명하는 목적격 보어이므로 정답은 ⑤이다.",
   n=["remained 뒤에서 주어 The room의 상태를 설명하는 주격 보어라 <보기>와 다르므로 오답이다.", "동사 spoke를 꾸미는 부사라 <보기>와 다르므로 오답이다.",
      "동사 agreed의 목적어인 to부정사라 <보기>와 다르므로 오답이다.", "seems 뒤에서 주어 My uncle의 상태를 설명하는 주격 보어라 <보기>와 다르므로 오답이다.",
      "목적어 the plan의 상태를 설명하는 목적격 보어라 <보기>와 같으므로 정답이다."])
RE(2, 23, "F", s=ADD(2, 23, "F", M + "(A)·(B) 문장을 원문항 길이 이상으로 늘렸다."),
   p="(A) They<u>'d</u> like to leave early tomorrow morning.\n(B) We<u>'d</u> better check the map before we start.")
RE(2, 27, "F", s=ADD(2, 27, "F", M + "제시문과 보기 문장을 원문항 길이 이상으로 늘렸다."),
   p="I want to help you with your science project.",
   c=["I did want to help you with your science project.", "I does want to help you with your science project.", "I do want to help you with your science project.",
      "I am want to help you with your science project.", "I do wants to help you with your science project."], a=3,
   k="현재형 want를 강조하므로 주어 I에 맞는 do를 동사 앞에 두고 동사는 원형 want로 쓴다. 정답은 ③이다.",
   n=["did는 과거라 현재형 문장의 시제가 바뀌므로 오답이다.", "주어 I에는 does를 쓰지 않으므로 오답이다.",
      "현재형이고 주어가 I이므로 do + 동사원형 want로 바르게 강조했으므로 정답이다.", "be동사 am으로는 일반동사를 강조할 수 없으므로 오답이다.",
      "do 뒤에는 동사원형을 써야 하는데 wants를 썼으므로 오답이다."])
RE(2, 35, "F", s=ADD(2, 35, "F", M + "교사의 질문(지문)을 원문항 길이 이상으로 늘렸다."),
   p="교사: 사역동사(make, let, have)와 지각동사(see, hear)가 들어간 문장을 수동태로 바꿀 때 목적격 보어가 어떻게 바뀌는지 말해볼까요?")
RE(2, 44, "D", s=ADD(2, 44, "D", M + "정답만 재귀대명사가 문장 끝에 있어 위치로 정답이 드러나던 것을, 오답 두 개도 재귀대명사가 문장 끝에 오도록 바꿨다."),
   c=["She cut <u>herself</u> on the broken glass yesterday.", "We prepared the whole meal for the party <u>ourselves</u>.", "Last week, I bought a new watch for <u>myself</u>.",
      "At dinner, they talked for hours about <u>themselves</u>.", "Please help <u>yourself</u> to the food on the table."], a=2,
   n=["재귀대명사가 동사 cut의 목적어로 쓰인 재귀 용법이라 <보기>(강조 용법)와 다르므로 오답이다.",
      "완전한 문장 뒤에 붙어 ‘직접, 스스로’라는 뜻을 더하는 강조 용법이라 <보기>와 같으므로 정답이다.",
      "재귀대명사가 전치사 for의 목적어로 쓰인 재귀 용법이라 <보기>와 다르므로 오답이다.",
      "재귀대명사가 전치사 about의 목적어로 쓰인 재귀 용법이라 <보기>와 다르므로 오답이다.",
      "help yourself to는 ‘~을 마음껏 먹다’라는 관용 표현으로, help의 목적어 자리에 쓴 재귀 용법이라 <보기>와 다르므로 오답이다."])
RE(2, 44, "E", s=ADD(2, 44, "E", M + "정답만 재귀대명사가 문장 끝에 있어 위치로 정답이 드러나던 것을, 오답 두 개도 재귀대명사가 문장 끝에 오도록 바꿨다."),
   c=["In the empty classroom, she was talking to <u>herself</u>.", "I told <u>myself</u> not to give up on my dream.", "After swimming, the kids quickly dried <u>themselves</u>.",
      "Be careful not to burn <u>yourself</u> on the stove.", "Tom wrote the whole graduation speech <u>himself</u>."], a=5,
   n=["재귀대명사가 전치사 to의 목적어로 쓰인 재귀 용법이라 <보기>(강조 용법)와 다르므로 오답이다.",
      "재귀대명사가 동사 told의 목적어로 쓰인 재귀 용법이라 <보기>와 다르므로 오답이다.",
      "재귀대명사가 동사 dried의 목적어로 쓰인 재귀 용법이라 <보기>와 다르므로 오답이다.",
      "재귀대명사가 동사 burn의 목적어로 쓰인 재귀 용법이라 <보기>와 다르므로 오답이다.",
      "완전한 문장 뒤에 붙어 ‘직접, 스스로’라는 뜻을 더하는 강조 용법이라 <보기>와 같으므로 정답이다."])
RE(2, 44, "F", s=ADD(2, 44, "F", M + "재귀대명사의 위치로 정답이 드러나던 것을, 오답 두 개도 재귀대명사가 문장 끝에 오도록 바꿨다."),
   c=["You fixed the broken chair in the kitchen <u>yourself</u>.", "He considers <u>himself</u> lucky to have such good friends.", "At the party last night, the children enjoyed <u>themselves</u>.",
      "She looked at <u>herself</u> in the mirror before the show.", "The little boy is too young to dress <u>himself</u>."], a=1,
   n=["완전한 문장 뒤에 붙어 ‘직접, 스스로’라는 뜻을 더하는 강조 용법이라 <보기>와 같으므로 정답이다.",
      "재귀대명사가 동사 considers의 목적어로 쓰인 재귀 용법이라 <보기>(강조 용법)와 다르므로 오답이다.",
      "재귀대명사가 동사 enjoyed의 목적어로 쓰인 재귀 용법(enjoy oneself ‘즐겁게 지내다’)이라 <보기>와 다르므로 오답이다.",
      "재귀대명사가 전치사 at의 목적어로 쓰인 재귀 용법이라 <보기>와 다르므로 오답이다.",
      "재귀대명사가 동사 dress의 목적어로 쓰인 재귀 용법이라 <보기>와 다르므로 오답이다."])
RE(2, 53, "F", s=ADD(2, 53, "F", M + "보기 문장을 원문항 길이 이상으로 늘렸다."),
   c=["I'm glad <u>to meet</u> you here at the party.", "She was sad <u>to hear</u> the news about her old friend.", "We were surprised <u>to see</u> him at the station so early.",
      "I have an important question <u>to ask</u> you after class.", "He was very happy <u>to win</u> the prize in the contest."], a=4,
   n=["감정 형용사 glad 뒤에서 그 감정의 원인을 나타내는 부사적 용법이므로 오답이다.", "감정 형용사 sad 뒤에서 그 감정의 원인을 나타내는 부사적 용법이므로 오답이다.",
      "감정 형용사 surprised 뒤에서 그 감정의 원인을 나타내는 부사적 용법이므로 오답이다.", "명사 question을 꾸미는 형용사적 용법이라 나머지 넷과 다르므로 정답이다.",
      "감정 형용사 happy 뒤에서 그 감정의 원인을 나타내는 부사적 용법이므로 오답이다."])
RE(2, 84, "F", s=ADD(2, 84, "F", M + "정답만 the가 없어 바로 드러나던 것을, 오답 두 개를 소유격 + 최상급(my best, our oldest)으로 바꿔 the가 없는 바른 문장도 섞었다."),
   c=["It was <u>biggest</u> fish I've ever caught in this lake.", "She is <u>my best</u> friend in our class.", "This is <u>our oldest</u> photo of our grandmother.",
      "He is one of <u>the richest</u> men in the country.", "This is <u>the most beautiful</u> beach I've ever visited."], a=1,
   r="형용사의 최상급이 명사를 꾸밀 때는 앞에 the를 쓴다. 소유격(my, our 등)이 있으면 the를 쓰지 않는다.",
   k="명사를 꾸미는 최상급 앞에는 the나 소유격이 와야 하는데 ①은 biggest 앞에 아무것도 없다. the biggest로 고쳐야 하므로 정답은 ①이다.",
   n=["형용사 최상급 biggest 앞에 the가 빠져 어법상 완전하지 않으므로 정답이다.", "최상급 best 앞에 소유격 my를 썼으므로 the가 없어도 맞다. 오답이다.",
      "최상급 oldest 앞에 소유격 our를 썼으므로 the 없이도 맞다. 오답이다.", "one of the + 최상급 + 복수명사를 바르게 썼으므로 오답이다.",
      "긴 형용사의 최상급 the most beautiful을 바르게 썼으므로 오답이다."])

# ---- 3급 ----
RE(3, 10, "F", s=ADD(3, 10, "F", M + "‘없음’이 정답이던 것을 틀린 문장 3개(정답 ③)로 바꿨다."),
   p="<보기>\n- There was many dark clouds in the sky yesterday afternoon.\n- The sky were dark all day, so we turned on the lights early.\n- There was a strong wind from the sea in the evening.\n- The children was inside the house with their grandparents.",
   a=3, k="틀린 문장은 첫째, 둘째, 넷째로 3개이다.", n="cnt",
   pre=["문장별 판정: 첫째 X. 뒤의 명사 many dark clouds가 복수이므로 there were여야 한다.", "문장별 판정: 둘째 X. 단수 주어 The sky에는 was를 쓴다.",
        "문장별 판정: 셋째 O. 뒤의 명사 a strong wind가 단수이므로 there was가 맞다.", "문장별 판정: 넷째 X. 복수 주어 The children에는 were를 쓴다."])
RE(3, 36, "F", s=ADD(3, 36, "F", M + "제시문과 보기 문장을 원문항 길이 이상으로 늘리고, 형태가 없는 am nots 대신 어순이 틀린 not am을 넣었다."),
   p="I am going to be late for the meeting tomorrow.",
   c=["I am not go to be late for the meeting tomorrow.", "I not am going to be late for the meeting tomorrow.", "I isn't going to be late for the meeting tomorrow.",
      "I don't going to be late for the meeting tomorrow.", "I am not going to be late for the meeting tomorrow."], a=5,
   k="be going to의 부정은 be동사 뒤에 not을 붙이므로 I am not going to be late for the meeting tomorrow.가 알맞다. 정답은 ⑤이다.",
   n=["going을 go로 바꾸면 be going to의 형태가 깨지므로 오답이다.", "not은 be동사 뒤에 써야 하는데 am 앞에 썼으므로 오답이다.",
      "주어 I에는 isn't가 아니라 am not을 쓰므로 오답이다.", "be going to의 부정에는 don't를 쓰지 않으므로 오답이다.",
      "be동사 am 뒤에 not을 붙인 am not going to로 바르게 바꿨으므로 정답이다."])
RE(3, 51, "F", s=ADD(3, 51, "F", M + "‘~하는 것이 좋겠다’에 더 맞는 had better로 정답을 바꿨다."),
   p="Tom은 일찍 자는 것이 좋겠다.",
   c=["Tom had better to go to bed early.", "Tom had better going to bed early.", "Tom had better go to bed early.", "Tom may go to bed early.", "Tom can go to bed early."], a=3,
   r="조동사(must, should, may, can)와 had better 뒤에는 동사원형을 쓴다. had better는 ‘~하는 것이 좋겠다’는 충고를 나타낸다.",
   k="‘~하는 것이 좋겠다’는 충고의 had better이고 뒤에는 동사원형을 쓰므로 정답은 ③이다.",
   n=["had better 뒤에는 동사원형을 쓰므로 to를 붙인 to go는 오답이다.", "had better 뒤에는 동사원형을 쓰므로 -ing형 going은 오답이다.",
      "‘~하는 것이 좋겠다’를 had better + 동사원형으로 바르게 옮겼으므로 정답이다.", "may는 ‘~해도 된다’는 허락이라 우리말 뜻과 맞지 않으므로 오답이다.",
      "can은 ‘~할 수 있다’는 능력이라 우리말 뜻과 맞지 않으므로 오답이다."])
RE(3, 89, "F", s=ADD(3, 89, "F", M + "지문을 원문항 길이 이상으로 늘렸다."),
   p="My brother and I love sports very much. Every day after school, we ⓐ<u>enjoy playing</u> soccer in the park near our house. We play almost every day, even in winter.")
_96 = M + "밑줄 친 틀린 낱말(-ly 부사)이 보기에도 그대로 있어 어색하던 것을 빼고, 다른 형태의 오답으로 바꿨다."
RE(3, 96, "B", s=ADD(3, 96, "B", _96), p="This new pillow on my bed feels <u>softly</u>.", c=["soft", "softness", "soften", "more softer", "to soft"], a=1,
   k="feel 뒤 보어 자리에는 형용사를 쓰므로 softly를 soft로 고친다. 정답은 ①이다.",
   n=["feel 뒤 보어 자리에 형용사를 바르게 썼으므로 정답이다.", "명사로는 주어의 상태를 설명하지 못해 뜻이 맞지 않으므로 오답이다.",
      "soften은 ‘부드럽게 하다’라는 동사라 보어 자리에 쓸 수 없으므로 오답이다.", "more와 -er을 겹쳐 쓸 수 없고 비교할 대상도 없으므로 오답이다.",
      "to 뒤에는 동사원형을 쓰므로 오답이다."])
RE(3, 96, "C", s=ADD(3, 96, "C", _96), c=["to tire", "the tireder", "tired", "tiredness", "most tired than"], a=3,
   k="look 뒤 보어 자리에는 형용사를 쓰므로 tiredly를 tired로 고친다. 정답은 ③이다.",
   n=["look 뒤 보어 자리에 to부정사를 쓸 수 없으므로 오답이다.", "tireder라는 비교급은 없고 비교할 대상도 없으므로 오답이다.",
      "look 뒤 보어 자리에 형용사 tired를 바르게 썼으므로 정답이다.", "명사 tiredness로는 주어의 상태를 설명하지 못하므로 오답이다.",
      "비교할 대상이 없는데 최상급과 than을 섞어 썼으므로 오답이다."])
RE(3, 96, "D", s=ADD(3, 96, "D", _96), c=["niceness", "to nice", "more nicer", "nice", "most nice than"], a=4,
   k="smell 뒤 보어 자리에는 형용사를 쓰므로 nicely를 nice로 고친다. 정답은 ④이다.",
   n=["명사로는 냄새의 상태를 설명하지 못하므로 오답이다.", "to 뒤에는 동사원형을 쓰는데 nice는 형용사라 오답이다.",
      "more와 -er을 겹쳐 쓸 수 없고 비교할 대상도 없으므로 오답이다.", "smell 뒤 보어 자리에 형용사 nice를 바르게 썼으므로 정답이다.",
      "최상급과 than을 섞어 쓸 수 없으므로 오답이다."])
RE(3, 96, "E", s=ADD(3, 96, "E", _96), c=["happiness", "to happy", "the happier", "more happier", "happy"], a=5,
   k="seem 뒤 보어 자리에는 형용사를 쓰므로 happily를 happy로 고친다. 정답은 ⑤이다.",
   n=["명사로는 주어의 상태를 설명하지 못하므로 오답이다.", "to 뒤에는 동사원형을 쓰는데 happy는 형용사라 오답이다.",
      "비교할 대상이 없는데 the + 비교급을 썼으므로 오답이다.", "more와 -er을 겹쳐 쓸 수 없으므로 오답이다.",
      "seem 뒤 보어 자리에 형용사 happy를 바르게 썼으므로 정답이다."])
RE(3, 96, "F", s=ADD(3, 96, "F", _96), c=["darken", "darkness", "dark", "the darker", "most dark than"], a=3,
   k="become 뒤 보어 자리에는 형용사를 쓰므로 darkly를 dark로 고친다. 정답은 ③이다.",
   n=["darken은 ‘어두워지다’라는 동사라 became 뒤 보어 자리에 쓸 수 없으므로 오답이다.", "명사 darkness로는 하늘의 상태를 설명하지 못해 뜻이 맞지 않으므로 오답이다.",
      "become 뒤 보어 자리에 형용사 dark를 바르게 썼으므로 정답이다.", "비교할 대상이 없는데 the + 비교급을 썼으므로 오답이다.",
      "최상급과 than을 섞어 쓸 수 없으므로 오답이다."])
RE(3, 100, "F", s=ADD(3, 100, "F", M + "다섯 문장이 모두 틀리던 것을 ⓐ를 옳은 문장으로 바꿔 틀린 문장 4개(정답 ④)로 했다."),
   p="ⓐ I have many friends in my new school in Seoul.\nⓑ She looks happily in the picture with her dog.\nⓒ Tom runs fastly every morning to catch the bus.\nⓓ We have few money for the family trip this summer.\nⓔ I want to drink cold something after the soccer game.",
   a=4, k="어법상 틀린 문장은 ⓑ, ⓒ, ⓓ, ⓔ로 4개이다.", n="cnt",
   pre=["문장별 판정: ⓐ O. 셀 수 있는 명사 friends에 many를 바르게 썼다.", "문장별 판정: ⓑ X. look 뒤 보어 자리에는 형용사 happy를 쓴다.",
        "문장별 판정: ⓒ X. fast는 -ly 없이 부사로 쓴다.", "문장별 판정: ⓓ X. 셀 수 없는 명사 money에는 little을 쓴다.",
        "문장별 판정: ⓔ X. -thing 대명사는 형용사가 뒤에서 꾸미므로 something cold로 쓴다."])
RE(3, 108, "F", s=ADD(3, 108, "F", M + "제시어 the Han River를 the / Han / River로 하나씩 나눠 섞었다."),
   p="한강은 한국에서 가장 긴 강 중 하나이다.\n( river / one / Han / is / of / the / long / River / in / the / Korea / . )")
RE(3, 110, "F", s=ADD(3, 110, "F", M + "지문을 원문항 길이 이상으로 늘렸다(밑줄 문장과 보기는 그대로)."),
   p="Last Friday, our class went on a two-day school trip to Gyeongju. I packed my bag for the trip the night before, and my friend Minsu packed his bag, too. <u>My bag was more heavier than his bag on the school bus</u>. I had too many clothes and snacks in it. Minsu laughed at me when he saw my bag, but he helped me carry it.")

# ---- 4급 C(메모) + 같은 번호 D·E·F(같은 결함) ----
def SALT(t, n, ok):  # 4-7 공통: 셀 수 없는 명사 보기 해설
    return {"two": f"셀 수 없는 명사 {n} 앞에 수(two)를 쓸 수 없으므로 오답이다.", "many": f"many는 셀 수 있는 명사의 복수형에 쓰므로 셀 수 없는 {n}에는 쓸 수 없어 오답이다.",
            "an": f"셀 수 없는 명사 {n} 앞에 an을 쓸 수 없으므로 오답이다.", "a": f"셀 수 없는 명사 {n} 앞에 a를 쓸 수 없으므로 오답이다.",
            "some": f"‘약간의 {ok}’를 some + 셀 수 없는 명사로 바르게 옮겼으므로 정답이다."}[t]
def ITEMS7(head, tail, order, n, ok):
    return [f"{head} {w} {n} {tail}".replace("  ", " ") for w in order], [SALT(w, n, ok) for w in order]
c_, n_ = ITEMS7("I put", "in my warm tea every morning.", ["two", "many", "an", "some", "a"], "sugar", "설탕")
RE(4, 7, "C", s=ADD(4, 7, "C", M + "우리말과 보기 문장을 원문항 길이 이상으로 늘렸다."), p="나는 매일 아침 따뜻한 차에 설탕을 약간 넣는다.", c=c_, a=4, n=n_)
c_, n_ = ITEMS7("We need", "for the vegetable soup this evening.", ["an", "many", "some", "a", "two"], "water", "물")
RE(4, 7, "D", st="R", s=ADD(4, 7, "D", SAME + "C 메모(원문항보다 짧음)와 같은 결함이라 우리말과 보기 문장을 원문항 길이 이상으로 늘렸다."), p="우리는 오늘 저녁 채소 수프를 위해 물을 약간 필요로 한다.", c=c_, a=3, n=n_)
c_, n_ = ITEMS7("She eats", "with milk before school every morning.", ["many", "some", "an", "two", "a"], "bread", "빵")
RE(4, 7, "E", st="R", s=ADD(4, 7, "E", SAME + "C 메모(원문항보다 짧음)와 같은 결함이라 우리말과 보기 문장을 원문항 길이 이상으로 늘렸다."), p="그녀는 매일 아침 학교에 가기 전에 우유와 함께 빵을 약간 먹는다.", c=c_, a=2, n=n_)
c_, n_ = ITEMS7("They need", "for their new science project at school.", ["some", "two", "a", "many", "an"], "money", "돈")
RE(4, 7, "F", st="R", s=ADD(4, 7, "F", SAME + "C 메모(원문항보다 짧음)와 같은 결함이라 우리말과 보기 문장을 원문항 길이 이상으로 늘렸다."), p="그들은 학교의 새 과학 프로젝트를 위해 돈을 약간 필요로 한다.", c=c_, a=1, n=n_)

RE(4, 12, "C", s=ADD(4, 12, "C", M + "정답 보기만 길어 드러나던 것을 다른 보기와 비슷한 길이(빈칸 뒤 is, 주어 자리)로 바꿨다."),
   c=["_____ book is red.", "This is _____ bag.", "That car is _____.", "I like _____ new jacket a lot.", "_____ is my classmate."], a=5,
   k="⑤는 빈칸 뒤가 동사 is라 주어 자리다. ‘그는 내 반 친구다’이므로 He가 들어가고 his는 들어갈 수 없다. 정답은 ⑤이다.",
   n=["명사 book 앞이라 소유격 His가 들어가므로 오답이다.", "명사 bag 앞이라 소유격 his가 들어가므로 오답이다.", "‘저 차는 그의 것이다’라는 소유대명사 his가 들어가므로 오답이다.",
      "명사 jacket 앞이라 소유격 his가 들어가므로 오답이다.", "빈칸 뒤가 동사 is인 주어 자리라 주격 He가 들어가고 his는 들어갈 수 없으므로 정답이다."])
RE(4, 12, "E", s=ADD(4, 12, "E", SAME + "C 메모(정답 보기만 길다)와 같은 결함이라 다른 보기도 비슷한 길이로 늘렸다."),
   c=["My teacher helped _____ after class.", "_____ sister is kind to everyone.", "This is _____ new pencil.", "That bike in the yard is _____.", "I really like _____ car."], a=1,
   n=["동사 helped 뒤 목적어 자리라 목적격 him이 들어가고 his는 들어갈 수 없으므로 정답이다.", "명사 sister 앞이라 소유격 His가 들어가므로 오답이다.",
      "명사 pencil 앞이라 소유격 his가 들어가므로 오답이다.", "‘그 자전거는 그의 것이다’라는 소유대명사 his가 들어가므로 오답이다.", "명사 car 앞이라 소유격 his가 들어가므로 오답이다."])

RE(4, 31, "C", s=ADD(4, 31, "C", M + "정답 보기만 길던 것을 모든 보기가 비슷한 길이가 되도록 다른 보기를 늘렸다."),
   c=["Minsu cleaned his room last Sunday.", "We were late for school yesterday.", "My dad cooks dinner on weekends.", "She took a picture of the sea.", "They left the house an hour ago."], a=3,
   n=["cleaned는 clean의 과거형이라 과거 시제 문장이므로 오답이다.", "were는 be동사의 과거형이라 과거 시제 문장이므로 오답이다.",
      "cooks는 현재형이고 on weekends(주말마다)도 현재의 습관을 나타내 과거 시제가 아니므로 정답이다.", "took은 take의 과거형이라 과거 시제 문장이므로 오답이다.",
      "left는 leave의 과거형이라 과거 시제 문장이므로 오답이다."])
RE(4, 31, "E", s=ADD(4, 31, "E", SAME + "C 메모와 같은 결함(보기 길이 차이·원문항보다 짧음)이라 보기를 비슷한 길이로 늘렸다."),
   c=["I read an interesting book yesterday.", "They were very busy last week.", "Jane went home early after school.", "Tom watches TV after dinner every night.", "We had lunch at noon yesterday."], a=4,
   n=["yesterday가 있어 read는 과거형(read)이다. 과거 시제 문장이므로 오답이다.", "were는 be동사의 과거형이라 과거 시제 문장이므로 오답이다.",
      "went는 go의 과거형이라 과거 시제 문장이므로 오답이다.", "watches는 현재형이고 every night도 현재의 습관을 나타내 과거 시제가 아니므로 정답이다.",
      "had는 have의 과거형이라 과거 시제 문장이므로 오답이다."])

RE(4, 38, "C", s=ADD(4, 38, "C", M + "보기 문장을 원문항 길이 이상으로 늘렸다."),
   c=["She caught a bad cold last week.", "My uncle came to visit us last Sunday.", "We swam in the lake near our house.", "He sold his old car to his friend.", "I leave home at seven yesterday morning."], a=5,
   n=["catch의 과거형 caught를 바르게 썼으므로 오답이다.", "come의 과거형 came을 바르게 썼으므로 오답이다.", "swim의 과거형 swam을 바르게 썼으므로 오답이다.",
      "sell의 과거형 sold를 바르게 썼으므로 오답이다.", "yesterday morning이 있는데 현재형 leave를 썼다. left로 고쳐야 하므로 정답이다."])
_38 = SAME + "C 메모(원문항보다 짧음)와 같은 결함이라 보기 문장을 원문항 길이 이상으로 늘렸다."
RE(4, 38, "D", s=ADD(4, 38, "D", _38),
   c=["They sees a movie at the theater yesterday.", "I brought my lunch to school today.", "The dog bit my new shoe this morning.", "She wrote a poem for her mother.", "Dad fixed the broken door last night."], a=1,
   n=["yesterday가 있는데 sees를 썼다. saw로 고쳐야 하므로 정답이다.", "bring의 과거형 brought를 바르게 썼으므로 오답이다.", "bite의 과거형 bit을 바르게 썼으므로 오답이다.",
      "write의 과거형 wrote를 바르게 썼으므로 오답이다.", "fix의 과거형 fixed를 바르게 썼으므로 오답이다."])
RE(4, 38, "E", s=ADD(4, 38, "E", _38),
   c=["The train arrived at the station on time.", "Jane buy a new bag at the mall last week.", "We built a big sandcastle at the beach.", "He felt very tired after school yesterday.", "I read the book about dinosaurs twice."], a=2,
   n=["arrive의 과거형 arrived를 바르게 썼으므로 오답이다.", "last week이 있는데 buy를 썼다. bought로 고쳐야 하므로 정답이다.", "build의 과거형 built를 바르게 썼으므로 오답이다.",
      "feel의 과거형 felt를 바르게 썼으므로 오답이다.", "read의 과거형도 read라 바르게 썼으므로 오답이다."])
RE(4, 38, "F", s=ADD(4, 38, "F", _38),
   c=["They won the soccer game last Saturday.", "She spent all her money on new clothes.", "Tom broke the kitchen window by mistake.", "We eats lunch together at noon yesterday.", "I understood the question on the math test."], a=4,
   n=["win의 과거형 won을 바르게 썼으므로 오답이다.", "spend의 과거형 spent를 바르게 썼으므로 오답이다.", "break의 과거형 broke를 바르게 썼으므로 오답이다.",
      "yesterday가 있는데 eats를 썼다. ate로 고쳐야 하므로 정답이다.", "understand의 과거형 understood를 바르게 썼으므로 오답이다."])

RE(4, 52, "C", s=ADD(4, 52, "C", M + "우리말과 문장을 원문항 길이 이상으로 늘렸다."), p="내일 오후에는 비가 올지도 모르니 우산을 챙겨라.\nIt _____ rain tomorrow afternoon, so take your umbrella.")
RE(4, 52, "D", s=ADD(4, 52, "D", SAME + "C 메모(원문항보다 짧음)와 같은 결함이라 우리말과 문장을 늘렸다."), p="우리 형은 영어를 포함해서 세 가지 언어를 할 수 있다.\nMy brother _____ speak three languages, including English.")
RE(4, 52, "E", s=ADD(4, 52, "E", SAME + "C 메모(원문항보다 짧음)와 같은 결함이라 우리말과 문장을 늘렸다."), p="우리는 지금 반드시 출발해야 한다. 그렇지 않으면 기차를 놓칠 것이다.\nWe _____ leave now, or we will miss the train.")

RE(4, 59, "C", s=ADD(4, 59, "C", M + "우리말과 영어 문장을 원문항 길이 이상으로 늘렸다."), p="Jane은 어제 다리를 다쳐서 수영할 수 없었다.\n→ Jane (A)________ ________ (B)________ in the pool yesterday because she hurt her leg.")
_59 = SAME + "C 메모(원문항보다 짧음)와 같은 결함이라 우리말과 영어 문장을 늘렸다."
RE(4, 59, "D", s=ADD(4, 59, "D", _59), p="그들은 어제 너무 바빠서 우리를 도울 수 없었다.\n→ They (A)________ ________ (B)________ us yesterday because they were too busy.")
RE(4, 59, "E", s=ADD(4, 59, "E", _59), p="나는 어제 늦잠을 자서 버스를 탈 수 없었다.\n→ I (A)________ ________ (B)________ the bus yesterday because I got up late.")
RE(4, 59, "F", s=ADD(4, 59, "F", _59), p="Tom은 어제 안경을 잃어버려서 영어책을 읽을 수 없었다.\n→ Tom (A)________ ________ (B)________ his English book yesterday because he lost his glasses.")

RE(4, 64, "C", s=ADD(4, 64, "C", M + "보기 문장을 원문항 길이 이상으로 늘렸다."),
   c=["There is a little juice in the glass on the table.", "I have a few coins in my pocket.", "He has little patience with noisy children.", "We saw a lot of birds in the park.", "She made few mistake on the math test."], a=5,
   n=["셀 수 없는 juice에 a little을 바르게 썼으므로 오답이다.", "셀 수 있는 coins(복수)에 a few를 바르게 썼으므로 오답이다.", "셀 수 없는 patience에 little을 바르게 썼으므로 오답이다.",
      "a lot of는 셀 수 있는 명사와 셀 수 없는 명사 모두에 쓰므로 오답이다.", "few 뒤에는 셀 수 있는 명사의 복수형이 와야 하는데 단수 mistake를 썼으므로 정답이다."])
_64 = SAME + "C 메모(원문항보다 짧음)와 같은 결함이라 보기 문장을 원문항 길이 이상으로 늘렸다."
RE(4, 64, "D", s=ADD(4, 64, "D", _64),
   c=["There are only a few cookies left in the jar.", "I have little money in my wallet now.", "She has much friends at her new school.", "They need a lot of help with the move.", "He drank a little green tea after dinner."], a=3,
   n=["셀 수 있는 cookies(복수)에 a few를 바르게 썼으므로 오답이다.", "셀 수 없는 money에 little을 바르게 썼으므로 오답이다.",
      "셀 수 있는 friends에는 much가 아니라 many를 써야 하므로 정답이다.", "a lot of는 셀 수 없는 help에도 쓰므로 오답이다.", "셀 수 없는 tea에 a little을 바르게 썼으므로 오답이다."])
RE(4, 64, "E", s=ADD(4, 64, "E", _64),
   c=["We need many water for the garden today.", "Jane has a few cousins in Busan.", "There is little snow in the high mountains this year.", "He read a lot of books during the vacation.", "I have a little free time after lunch today."], a=1,
   n=["셀 수 없는 water에는 many가 아니라 much를 써야 하므로 정답이다.", "셀 수 있는 cousins(복수)에 a few를 바르게 썼으므로 오답이다.",
      "셀 수 없는 snow에 little을 바르게 썼으므로 오답이다.", "a lot of는 셀 수 있는 books에도 쓰므로 오답이다.", "셀 수 없는 time에 a little을 바르게 썼으므로 오답이다."])
RE(4, 64, "F", s=ADD(4, 64, "F", _64),
   c=["She gave me a little advice about my test.", "There is a few milk left in the bottle.", "I know a few words in Chinese and Japanese.", "We have little homework for the weekend.", "They have lots of toys in their small room."], a=2,
   n=["셀 수 없는 advice에 a little을 바르게 썼으므로 오답이다.", "셀 수 없는 milk에는 a few가 아니라 a little을 써야 하므로 정답이다.",
      "셀 수 있는 words(복수)에 a few를 바르게 썼으므로 오답이다.", "셀 수 없는 homework에 little을 바르게 썼으므로 오답이다.", "lots of는 셀 수 있는 toys에도 쓰므로 오답이다."])

RE(4, 81, "C", s=ADD(4, 81, "C", M + "우리말과 문장을 원문항 길이 이상으로 늘렸다."), p="우리 동네 빵집은 매일 정오에 문을 연다.\nThe bakery on our street opens _____ noon every day.")
RE(4, 81, "D", s=ADD(4, 81, "D", SAME + "C 메모(원문항보다 짧음)와 같은 결함이라 문장을 늘렸다."), p="우리 독서 동아리는 항상 월요일에 모인다.\nOur book club always meets _____ Monday.")
RE(4, 81, "E", s=ADD(4, 81, "E", SAME + "C 메모(원문항보다 짧음)와 같은 결함이라 문장을 늘렸다."), p="Tom은 매년 8월에 가족과 여행을 간다.\nTom travels with his family _____ August every year.")

_89c = ["<u>When</u> did you get home last night?", "<u>When</u> is the school concert this year?", "<u>When</u> my dog was sick, I felt very sad.", "<u>When</u> will the next bus come here?", "<u>When</u> do you usually play soccer with your friends?"]
Q = "의문사 when: ‘언제’라고 묻는 의문문을 이끌므로 오답이다."; CJ = "접속사 when: ‘~할 때’라는 시간의 부사절을 이끌므로 오답이다."
RE(4, 89, "C", s=ADD(4, 89, "C", M + "보기 문장을 원문항 길이 이상으로 늘렸다."), c=_89c, a=3,
   n=[Q, Q, "접속사 when: ‘~할 때’라는 시간의 부사절을 이끌므로 나머지와 달라 정답이다.", Q, Q])
_89 = SAME + "C 메모(보기가 원문항보다 짧음)와 같은 결함이라 보기 문장을 늘렸다."
RE(4, 89, "D", s=ADD(4, 89, "D", _89),
   c=["<u>When</u> I was young, I lived in Busan.", "<u>When</u> is your sister's birthday party?", "Please turn off the light <u>when</u> you leave the room.",
      "It was snowing <u>when</u> we woke up this morning.", "He laughed loudly <u>when</u> he heard the joke."], a=2,
   n=[CJ, "의문사 when: ‘언제’라고 묻는 의문문을 이끌므로 나머지와 달라 정답이다.", CJ, CJ, CJ])
RE(4, 89, "E", s=ADD(4, 89, "E", _89),
   c=["<u>When</u> can you come to my house?", "<u>When</u> did Jane call you last night?", "<u>When</u> does the movie start at the theater tonight?", "<u>When</u> is Mom coming back from work?", "<u>When</u> you get home, wash your hands first."], a=5,
   n=[Q, Q, Q, Q, "접속사 when: ‘~할 때’라는 시간의 부사절을 이끌므로 나머지와 달라 정답이다."])
RE(4, 89, "F", s=ADD(4, 89, "F", _89),
   c=["<u>When</u> did Jane arrive at the airport?", "We were happy <u>when</u> we won the game.", "Say hello to him <u>when</u> you see him.", "I fell down <u>when</u> I was running in the park.", "<u>When</u> it rains, we stay inside and read."], a=1,
   n=["의문사 when: ‘언제’라고 묻는 의문문을 이끌므로 나머지와 달라 정답이다.", CJ, CJ, CJ, CJ])

RE(4, 96, "C", s=ADD(4, 96, "C", M + "우리말과 문장을 원문항 길이 이상으로 늘렸다."), p="올해에는 모두 건강하게 지내자.\n→ Let's all ________ healthy this year.")
RE(4, 96, "D", s=ADD(4, 96, "D", SAME + "C 메모(원문항보다 짧음)와 같은 결함이라 우리말과 문장을 늘렸다."), p="도서관에서는 조용히 하자.\n→ Let's ________ quiet in the library.")
