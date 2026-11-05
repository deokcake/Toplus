# 1급 CH3 조동사 (21~30)
OK, FXP, FXC, BAD = "적합", "수정(표기)", "수정(내용)", "부적합"
HINT_FIX = "발문을 원문항과 같게 되돌리고 괄호·설명 속 문법 용어를 삭제"
JUNK = "존재하지 않거나 문법적으로 성립할 수 없는 형태의 오답이 3개 이상이라 실제 경쟁 선택지가 두 개뿐이다(B3). 원문항 오답(visits, visited, is visiting, has visited)은 모두 실제 형태."

REVIEW = {
    (1, 21): {"*": (OK, "정답(must have p.p.) 유일 확인.", "")},
    (1, 22): {"*": (OK, "정답 유일 확인.", ""),
              "D": (FXC, "정답 ⑤ stay - go 확인. 문장이 원문항('stay at home than go to a crowded restaurant')과 거의 같고 정답 짝도 같다(C4).", "동사와 상황을 원문항과 다르게(예: walk - take a bus)")},
    (1, 23): {"*": (OK, "정답 유일 확인(be used to -ing / used to + 동사원형).", "")},
    (1, 24): {"B": (OK, "정답 ⑤ submits 확인(원문항과 같은 학교문법 기준).", ""),
              "*": (FXC, "정답 ⑤ 확인. 발문이 '원형가정법으로 표현한 문장'이라고 평가 문법을 알려 준다(C4).", HINT_FIX)},
    (1, 25): {"*": (OK, "정답 유일 확인. 발문이 '틀린 문장들로만 구성된 것'에서 '모두 고른 것'으로 바뀌었으나 과제는 같다.", ""),
              "C": (FXC, "정답 ① A, E, F 확인. 정답 조합이 원문항과 같고 A(than to drive)·F(musts)가 원문항 오류 문장과 거의 같다(C4).", "A·F를 다른 오류 유형으로 바꾸고 정답 조합을 원문항과 다르게"),
              "F": (OK, "정답 ③ F 확인. 'There used to being' 오류 문장이 B~E에 반복되지만 F는 해당 없음.", "")},
    (1, 26): {"B": (OK, "정답 ④ had to 유일 확인.", ""),
              "C": (FXC, "정답 ④ has to 확인. 원문항은 yesterday 단서로 시제를 판단하는데, 변형은 발문이 '현재 시제·단순현재형'을 알려 주고 수 일치만 남았다(B2·C4). 발문 조건이 없으면 will have to도 가능.", "문장에 시간 단서(every day 등)를 넣고 발문의 시제 조건 삭제"),
              "D": (FXC, "정답 ① have to 확인. 발문이 시제를 알려 준다(B2·C4). 조건이 없으면 will have to도 가능.", "시간 단서를 문장에 넣고 발문 조건 삭제"),
              "E": (FXC, "정답 ③ had to 확인. 문장에 last week 단서가 있는데 발문이 '과거 시제로'라고 다시 알려 준다(C4).", "발문을 원문항처럼 '빈칸에 들어갈 말로 가장 적절한 것'으로"),
              "F": (FXC, "정답 ① will have to 확인. 그러나 발문 조건('미래 시제로')이 없으면 ② have to도 'before the trip next month'와 자연스럽게 어울려 복수 정답이 된다. 조건에 기대야 답이 정해진다(C1 위험·C4).", "②를 'must to'처럼 명백히 틀린 형태로 바꾸고 발문 조건 삭제")},
    (1, 27): {"B": (OK, "정답 ① should - might 확인. 원문항 (B)는 might have p.p.(과거 가능성)인데 B는 might + 동사원형(현재 가능성)이라 하위 요소가 조금 다르다(허용 범위 안).", ""),
              "C": (FXC, "정답 ② should - might 확인. 발문 괄호가 (A)·(B)의 의미 기능을 직접 알려 준다(C4).", HINT_FIX),
              "*": (FXC, "정답 확인. 원문항은 should have p.p.(후회)와 might have p.p.(가능성)를 묻는데, 변형은 '과거 추측 + 현재 추측'으로 평가 요소가 바뀌었다(B1). 발문 조건('확신·의무·기대의 뜻 제외')이 없으면 must have p.p.(③⑤ 계열)도 자연스러워 답이 흔들린다. 오답 'should to'는 존재하지 않는 형태.", "원문항처럼 (A)에 후회(should have p.p.)가 들어가는 대화로 다시 쓰고 발문 조건 삭제"),
              "F": (FXC, "정답 ① may - might 확인. 선택지 다섯 개가 D와 순서까지 똑같다(C4). 발문 조건이 없으면 ③ 'They must have gone home already'가 가장 자연스럽다(C1 위험). 평가 요소도 원문항과 다르다(B1).", "원문항처럼 후회 + 가능성 대화로 다시 쓰고 선택지를 새로")},
    (1, 28): {"B": (OK, "정답 ④ 유일 확인. 우리말 뜻을 제시한 것은 허용 범위 안.", ""),
              "*": (FXC, "정답 확인. 발문이 'had better 부정문'이라고 구조를 알려 준다(C4). 오답이 would·to를 더하거나 not을 빼 '각각 한 번씩 사용' 조건만으로 지워진다(B3). 원문항 오답은 같은 낱말의 어순만 바꾼 것.", "발문을 원문항과 같게, 오답을 제시어 어순만 바꾼 배열(예: We'd not better…, Better we'd not…)로")},
    (1, 29): {"B": (FXC, "정답 ④ practice 확인. " + JUNK + " (practiceed, has practice, is practice)", "오답을 practices / practiced / is practicing / has practiced로"),
              "C": (FXC, "정답 ⑤ see 확인. 발문이 '원형가정법'을 알려 준다(C4). " + JUNK + " (seeed, is see, has see)", "발문 설명 삭제, 오답을 sees / saw / is seeing / has seen으로"),
              "D": (FXC, "정답 ③ be 확인. 오답은 실제 형태로 적절하나 발문이 '원형가정법'을 알려 준다(C4).", HINT_FIX),
              "E": (FXC, "정답 ② arrive 확인. 발문이 '원형가정법'을 알려 준다(C4). " + JUNK + " (is arrive, has arrive, arriveed)", "발문 설명 삭제, 오답을 arrives / arrived / is arriving / has arrived로"),
              "F": (FXC, "정답 ⑤ be submitted 확인. " + JUNK + " (has be submitted, is be submitted, be submitteded, be submitteds)", "오답을 is submitted / was submitted / has been submitted / submits로")},
    (1, 30): {"*": (OK, "정답(should have p.p.) 유일 확인. 오답이 원문항보다 단순하지만(could gone 등) 허용 범위 안.", "")},
}
