# 2026-10-28 감수 반영(사용자: 4급 F 1차 감수 완료). 확인 완료가 아닌 4급 F 메모 3건(4-12·4-54·4-85, 모두 ‘원문항보다 짧음’)을 고치고,
# 같은 번호에서 확인 완료가 아닌 4-12 C도 같은 결함(원문항보다 짧음)이라 함께 늘린다. 확인 완료 문서는 건드리지 않는다.
def ADD(g_, n_, t_, more): return (OLD(g_, n_, t_).get("s", "") + " " + more).strip()
M = "감수 메모 반영(10-28): "
SAME = "같은 번호 F 메모에 맞춘 수정(10-28): "

# ---- 4-12 ----
RE(4, 12, "F", s=ADD(4, 12, "F", M + "보기 문장을 원문항 길이 이상으로 늘렸다. 정답(② He 자리)은 그대로다. 풀이 순서가 예전 문항(빈칸 뒤 am)을 설명하던 것도 고쳤다."),
   c=["_____ father works at a hospital.", "_____ is a kind boy in my class.", "We visited _____ house last Sunday.", "I really like _____ new red cap.", "The blue bag on the chair is _____."],
   n=["명사 father 앞이라 소유격 His가 들어가므로 오답이다.", "빈칸 뒤에 명사가 없고 ‘그의 것’으로도 풀리지 않는 주어 자리(그는 우리 반의 친절한 소년이다)라 His가 아니라 주격 He가 들어가야 하므로 정답이다.",
      "명사 house 앞이라 소유격 his가 들어가므로 오답이다.", "명사구 new red cap 앞이라 소유격 his가 들어가므로 오답이다.", "‘의자 위의 파란 가방은 그의 것이다’라는 소유대명사 his가 들어가므로 오답이다."])
RE(4, 12, "C", s=ADD(4, 12, "C", SAME + "F 메모(원문항보다 짧음)와 같은 결함이라 보기 문장을 원문항 길이 이상으로 늘렸다. 정답(⑤ He 자리)과 보기 길이 균형은 그대로다."),
   c=["_____ book on the desk is red.", "This is _____ bag for the trip.", "That black car is _____.", "I like _____ new jacket a lot.", "_____ is my classmate now."])

# ---- 4-54 ----
RE(4, 54, "F", s=ADD(4, 54, "F", M + "보기 문장을 원문항 길이 이상으로 늘리고, 원문항처럼 옳은 be 보기(③ must be)를 넣어 정답만 be동사 꼴로 드러나지 않게 했다. 틀린 문장(① might are)은 그대로다. 풀이 순서가 조동사를 can으로 잘못 짚던 것도 고쳤다."),
   c=["My parents might <u>are</u> late tonight.", "He can <u>run</u> very fast.", "You must <u>be</u> quiet in the library.", "May I <u>sit</u> next to you?", "They have to <u>study</u> for the test."],
   n=["might 뒤에는 동사원형 be를 쓰므로 are를 be로 고쳐야 한다. 따라서 정답이다.", "조동사 can 뒤에 동사원형 run을 바르게 썼으므로 오답이다.", "조동사 must 뒤에 be동사의 원형 be를 바르게 썼으므로 오답이다.",
      "조동사 May 뒤에 동사원형 sit을 바르게 썼으므로 오답이다.", "have to 뒤에 동사원형 study를 바르게 썼으므로 오답이다."])

# ---- 4-85 ----
RE(4, 85, "F", s=ADD(4, 85, "F", M + "ⓐ~ⓓ 문장을 원문항 길이 이상으로 늘리고, 틀린 문장 두 개를 원문항처럼 in/on/at 혼동(in page 10, in the bus stop)으로 바꿨다(뜻에 따라 맞을 수도 있던 on the sea, 고정 표현 오류 in front to 대신). 옳은 문장에도 in을 하나 두어(in the tree) ‘in이면 틀림’으로 찍을 수 없게 했다. 옳은 문장의 자리와 정답은 그대로다."),
   p="ⓐ There is a picture of a lion in page 10.\nⓑ My mom met her friend in the bus stop yesterday.\nⓒ A little bird is sitting in the tree.\nⓓ Tom is at school with his friends now.",
   pre=["문장별 판정: ⓐ X. 책의 쪽(page)에는 on을 쓴다(on page 10).", "문장별 판정: ⓑ X. 버스 정류장 같은 한 지점에는 at을 쓴다(at the bus stop).",
        "문장별 판정: ⓒ O. 나무(가지 사이)에 앉아 있을 때는 in the tree로 쓴다.", "문장별 판정: ⓓ O. ‘학교에’는 at school로 쓴다."])

# ---- 4-6 C (사용자가 10-27 3차 보고 뒤 확인 완료를 풀었다: 풀이 순서가 다른 명사 sheep을 설명) ----
RE(4, 6, "C", s=ADD(4, 6, "C", "풀이 순서 정정(10-28): 풀이 순서가 다른 명사(sheep)를 설명하고 있어 지금 문항(goose - geese)에 맞게 고쳤다. 문항은 그대로다."))
