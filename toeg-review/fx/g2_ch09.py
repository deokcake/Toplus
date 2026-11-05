# 2급 CH9 비교 (81~90) 수정 예시
import re

def mk(g, n, t, items, a, r, s, **kw):
    F(g, n, t, c=[x for x, _ in items], a=a, r=r, n=[(w + (" 정답이다." if i + 1 == a else " 오답이다.")) for i, (_, w) in enumerate(items)], s=s + f" 정답 위치 {'①②③④⑤'[a-1]}.", **kw)
def pair(c, a, good, why, labs=("첫째", "둘째", "셋째")):
    out = []
    for i, ch in enumerate(c):
        parts = [p.strip() for p in re.split(r"\s+[—-]\s+", ch)]
        if i + 1 == a: out.append(f"{' - '.join(good)}: 세 자리가 모두 알맞으므로 정답이다." if len(good) == 3 else f"{' - '.join(good)}: 모든 자리가 알맞으므로 정답이다."); continue
        bits = [f"{labs[j]} 빈칸 {x}: {why[j][x]}" for j, x in enumerate(parts) if x != good[j]]
        out.append(" ".join(bits) + " 따라서 오답이다.")
    return out

# 2-82 비교급 강조어: 원문항 발문(우리말 + 들어갈 수 없는 말), F는 보기를 원문항과 다르게
ST82 = "주어진 우리말과 같도록 할 때 빈칸에 들어갈 수 없는 말을 고르시오."
S82 = "발문이 원문항과 달랐고 우리말 뜻이 빠졌다. 원문항 발문으로 되돌리고 원문항처럼 우리말 문장을 넣었다. 보기와 정답은 그대로다."
for t, ko in {"B": "새 소프트웨어는 옛 버전보다 훨씬 더 믿을 만하다.", "C": "새 길은 옛 길보다 훨씬 더 짧다.", "D": "이 가방은 내 것보다 훨씬 더 무겁다.", "E": "두 번째 문제는 첫 번째 문제보다 훨씬 더 쉬웠다."}.items():
    F(2, 82, t, st=ST82, p=f"{ko}\n{V(2, 82, t)['passage']}", s=S82)
R82 = "much·far·a lot·even·still·considerably·a great deal은 비교급 앞에서 ‘훨씬’의 뜻으로 비교급을 강조한다. very·so·too는 원급을 꾸미며 비교급을 직접 꾸미지 않는다."
EMP = "비교급(colder)을 강조해 ‘훨씬 더’의 뜻을 나타내므로 빈칸에 들어갈 수 있으므로"
mk(2, 82, "F", [("still", "still: " + EMP), ("considerably", "considerably: " + EMP), ("so", "so: 원급을 꾸미는 말이라 비교급(colder)을 직접 꾸밀 수 없어 들어갈 수 없으므로"),
                ("a great deal", "a great deal: " + EMP), ("far", "far: " + EMP)], 3, R82,
   "보기 다섯 개(very, a lot, much, far, even)와 정답(very)이 원문항과 똑같았다. 원문항 발문과 우리말을 넣고, 강조어 목록을 still·considerably·a great deal로 바꾸고 정답을 so로 바꿨다.",
   st=ST82, p="오늘 날씨는 어제보다 훨씬 더 춥다.\nToday's weather is _____ colder than yesterday's.")

# 2-83 비교급 중복 오류: 짝 문장 없애고 유형마다 새로
R83 = "-er형 비교급(taller, shorter, heavier 등) 앞에 more를 겹쳐 쓰지 않는다. the + 비교급, the + 비교급(~할수록 더 …), 비교급 + and + 비교급(점점 더), less + 원급 + than, 배수 + as + 원급 + as도 구별한다."
S83 = "틀린 문장이 같은 내용의 옳은 문장과 짝을 이뤄 대비 단서가 되었고, 오답 네 문장이 유형마다 같았다. 짝 문장을 없애고 유형마다 오답과 정답 문장을 새로 썼다."
def DBL(er): return f"비교급({er}) 앞에 more를 겹쳐 썼다. 어법상 틀린 문장이므로"
mk(2, 83, "B", [("The harder you practice, the better you play.", "the + 비교급, the + 비교급(~할수록 더 …)의 바른 형태이므로"), ("This is one of the oldest temples in Korea.", "one of the + 최상급 + 복수명사의 바른 형태이므로"),
                ("My room is less tidy than yours.", "less + 원급 + than의 바른 형태이므로"), ("This route is more shorter than the highway.", DBL("shorter")), ("It is getting darker and darker.", "비교급 + and + 비교급(점점 더)의 바른 형태이므로")], 4, R83, S83)
mk(2, 83, "C", [("He is not as tall as his brother.", "not as + 원급 + as의 바른 형태이므로"), ("This book is twice as thick as that one.", "배수 + as + 원급 + as의 바른 형태이므로"), ("Prices are getting higher and higher.", "비교급 + and + 비교급의 바른 형태이므로"),
                ("She sings better than I do.", "well의 비교급 better를 바르게 썼으므로"), ("My bag is more heavier than yours.", DBL("heavier"))], 5, R83, S83)
mk(2, 83, "D", [("Seoul is bigger than any other city in Korea.", "비교급 + than any other + 단수명사의 바른 형태이므로"), ("Today is more hotter than yesterday.", DBL("hotter")),
                ("The sooner we leave, the earlier we'll arrive.", "the + 비교급, the + 비교급의 바른 형태이므로"), ("This phone is much more expensive than that one.", "much가 비교급(more expensive)을 바르게 강조했으므로"),
                ("Tom is the funniest boy in our class.", "the + 최상급의 바른 형태이므로")], 2, R83, S83)
mk(2, 83, "E", [("Jane looks more happier than before.", DBL("happier")), ("Your idea is better than mine.", "good의 비교급 better를 바르게 썼으므로"), ("This river is three times as long as that one.", "배수 + as + 원급 + as의 바른 형태이므로"),
                ("Nothing is more important than health.", "Nothing + 비교급 + than(최상급의 뜻)의 바른 형태이므로"), ("He became more and more famous.", "more and more + 원급(점점 더)의 바른 형태이므로")], 1, R83, S83)
mk(2, 83, "F", [("The older he gets, the wiser he becomes.", "the + 비교급, the + 비교급의 바른 형태이므로"), ("Mina is one of the kindest girls I know.", "one of the + 최상급 + 복수명사의 바른 형태이므로"),
                ("This shirt is more cheaper than that one.", DBL("cheaper")), ("Air is lighter than water.", "-er형 비교급 + than의 바른 형태이므로"), ("I can run as fast as you.", "as + 원급 + as의 바른 형태이므로")], 3, R83,
   S83 + " 정답 문장이 원문항 정답(This problem is more easier …)과 똑같아 바꿨다.")

# 2-84 최상급 앞 the: 원문항 발문·밑줄, 짝 문장 없애고 오답 새로
ST84 = "다음 문장 중 밑줄 친 부분이 어법상 완전하지 않은 것을 고르시오."
R84 = "명사를 꾸미는 최상급 앞에는 the를 쓴다(the tallest boy, the most useful tool). one of the + 최상급 + 복수명사에서도 the를 빠뜨리지 않는다."
S84 = "발문이 ‘최상급 앞의 정관사가 빠져’라고 오류 유형을 알려 주었고 밑줄이 없었으며, 틀린 문장이 같은 내용의 옳은 문장과 짝을 이루고 오답 네 문장이 유형마다 같았다. 원문항 발문과 밑줄로 되돌리고, 짝 문장을 없애 오답을 유형마다 새로 썼다."
OKT = "최상급 앞에 the를 바르게 써서 완전하므로"
def NOT(sup): return f"명사를 꾸미는 최상급 앞에 the가 빠졌다(the {sup}). 완전하지 않은 부분이므로"
mk(2, 84, "B", [("Leo is <u>the tallest</u> student in our school.", OKT), ("This is <u>the best</u> answer of all.", OKT), ("Mina is <u>most patient</u> student in our class.", NOT("most patient")),
                ("Busan is one of <u>the biggest</u> cities in Korea.", OKT), ("It was <u>the happiest</u> day of my life.", OKT)], 3, R84, S84, st=ST84)
mk(2, 84, "C", [("This is <u>the most delicious</u> pizza I've ever had.", OKT), ("This is <u>most useful</u> tool in the workshop.", NOT("most useful")), ("Who is <u>the youngest</u> member of the team?", OKT),
                ("January is <u>the coldest</u> month of the year.", OKT), ("She is one of <u>the most famous</u> singers in the world.", OKT)], 2, R84, S84, st=ST84)
mk(2, 84, "D", [("Mt. Everest is <u>the highest</u> mountain in the world.", OKT), ("He is <u>the most careful</u> driver I know.", OKT), ("Today is <u>the shortest</u> day of the year.", OKT),
                ("This is one of <u>the oldest</u> trees in the park.", OKT), ("Tom is <u>tallest</u> boy on the team.", NOT("tallest"))], 5, R84, S84, st=ST84)
mk(2, 84, "E", [("What is <u>the fastest</u> animal on land?", OKT), ("That was <u>the worst</u> movie I've ever seen.", OKT), ("Jane is <u>the smartest</u> of the three sisters.", OKT),
                ("That was <u>most exciting</u> game this year.", NOT("most exciting")), ("This is <u>the cheapest</u> hotel in town.", OKT)], 4, R84, S84, st=ST84)
mk(2, 84, "F", [("It was <u>biggest</u> fish I've ever caught.", NOT("biggest")), ("Summer is <u>the hottest</u> season in Korea.", OKT), ("She is <u>the most popular</u> student in school.", OKT),
                ("He is one of <u>the richest</u> men in the country.", OKT), ("This is <u>the most beautiful</u> beach I've visited.", OKT)], 1, R84, S84, st=ST84)

# 2-85 대화 속 비교 표현 밑줄 다섯 곳: 원문항 형식
ST85 = "다음 대화에서 사용된 표현 중 어법상 옳지 않은 것을 고르시오."
R85 = "최상급은 the + -est/most + 원급으로, 비교급은 -er/more + 원급 + than으로 쓰며 more와 -er, most와 -est를 겹쳐 쓰지 않는다. bad-worse-worst 같은 불규칙 변화도 확인한다. No other + 단수명사 + 비교급 than(as + 원급 + as)은 최상급의 뜻을 나타낸다."
S85 = "원문항은 대화 속 밑줄 다섯 곳 중 틀린 표현을 찾는 형식인데, 변형은 빈칸 하나에 최상급을 넣는 형식으로 바뀌었고 발문이 답을 알려 주었다. 원문항 발문과 형식(대화 속 비교 표현 밑줄 다섯 곳)으로 다시 썼다."
def f85(t, lines, items, a):
    mk(2, 85, t, items, a, R85, S85, st=ST85, p="\n".join(lines), k=items[a-1][1].split(" 어법상")[0])
f85("B", ["A: ①<u>No other movie is as exciting as this one</u>, right?", "B: Yes. It's ②<u>the most exciting movie</u> I have ever seen.", "A: The actors were ③<u>much better than</u> I expected.",
          "B: And the music was ④<u>more beautifuler than</u> the last film's.", "A: I want to see it again ⑤<u>as soon as possible</u>."],
    [("No other movie is as exciting as this one", "No other + 단수명사 + as 원급 as로 최상급의 뜻을 바르게 나타냈으므로"), ("the most exciting movie", "the most + 원급의 바른 최상급이므로"),
     ("much better than", "much가 비교급(better)을 바르게 강조했으므로"), ("more beautifuler than", "more beautiful로 써야 하는데 -er을 겹쳐 붙였다. 어법상 옳지 않으므로"), ("as soon as possible", "as + 원급 + as possible의 바른 형태이므로")], 4)
f85("C", ["A: Mina is ①<u>the most diligent student</u> in our class.", "B: I agree. She studies ②<u>harder than anyone else</u>.", "A: She is also ③<u>kinder than</u> most people.",
          "B: Yes, ④<u>no other student is as kind as</u> Mina.", "A: She's ⑤<u>the most smartest</u> girl I know, too."],
    [("the most diligent student", "the most + 원급의 바른 최상급이므로"), ("harder than anyone else", "비교급 + than anyone else(최상급의 뜻)의 바른 형태이므로"), ("kinder than", "-er형 비교급 + than의 바른 형태이므로"),
     ("no other student is as kind as", "No other + 단수명사 + as 원급 as의 바른 형태이므로"), ("the most smartest", "the smartest로 써야 하는데 most와 -est를 겹쳐 썼다. 어법상 옳지 않으므로")], 5)
f85("D", ["A: Of the three bags, which one is ①<u>the heaviest</u>?", "B: The black one. It's ②<u>twice as heavy as</u> the red one.", "A: Really? The red one looks ③<u>more heavier</u> to me.",
          "B: No, it's ④<u>much lighter than</u> it looks.", "A: OK. I'll take ⑤<u>the lightest one</u>."],
    [("the heaviest", "셋 중 최상급이므로 the + -est가 알맞으므로"), ("twice as heavy as", "배수 + as + 원급 + as의 바른 형태이므로"), ("more heavier", "heavier로 써야 하는데 more를 겹쳐 썼다. 어법상 옳지 않으므로"),
     ("much lighter than", "much가 비교급(lighter)을 바르게 강조했으므로"), ("the lightest one", "the + -est의 바른 최상급이므로")], 3)
f85("E", ["A: How was your vacation?", "B: It was ①<u>the worst vacation</u> I've ever had.", "A: Why? Was the weather ②<u>more bad than</u> you expected?",
          "B: Yes. It rained ③<u>more heavily than</u> last year.", "A: That's too bad. Next time, check the weather ④<u>as carefully as</u> you can.", "B: I will. ⑤<u>Nothing is more important than</u> good weather on a trip."],
    [("the worst vacation", "bad의 최상급 worst를 바르게 썼으므로"), ("more bad than", "bad의 비교급은 worse이므로 worse than으로 써야 한다. 어법상 옳지 않으므로"), ("more heavily than", "부사 heavily의 비교급 more heavily를 바르게 썼으므로"),
     ("as carefully as", "동사(check)를 꾸미는 부사를 as ~ as 사이에 바르게 썼으므로"), ("Nothing is more important than", "Nothing + 비교급 + than(최상급의 뜻)의 바른 형태이므로")], 2)
f85("F", ["A: Which is ①<u>more long</u>, the Han River or the Nakdong River?", "B: The Nakdong River. It's ②<u>the longest river</u> in Korea.", "A: Is it ③<u>longer than any other river</u> in Korea?",
          "B: Yes. ④<u>No other river in Korea is as long as</u> it.", "A: I'd like to visit it ⑤<u>as soon as I can</u>."],
    [("more long", "long의 비교급은 longer이므로 more long은 쓰지 않는다. 어법상 옳지 않으므로"), ("the longest river", "the + -est의 바른 최상급이므로"), ("longer than any other river", "비교급 + than any other + 단수명사의 바른 형태이므로"),
     ("No other river in Korea is as long as", "No other + 단수명사 + as 원급 as의 바른 형태이므로"), ("as soon as I can", "as + 원급 + as + 주어 + can의 바른 형태이므로")], 1)

# 2-87 배수 비교: 구조를 알려 주던 발문을 원문항대로
for t in "BCDEF":
    F(2, 87, t, st="R", s="발문이 ‘as ... as 구문으로 나타낼 때’라고 구조를 알려 주어, 원문항 발문(우리말에 맞게 빈칸에 들어갈 가장 알맞은 것)으로 되돌렸다. 보기와 정답은 그대로다.")

# 2-89 one of + 복수명사: 원문항 발문, 다섯 문장 모두 one of 뒤 명사 형태
ST89 = "<보기>의 문장 중 밑줄 친 부분이 어법상 옳은 것만으로 묶인 것을 고르시오."
R89 = "one of + (the + 최상급 / 소유격) + 복수명사로 ‘~ 중 하나’를 나타낸다. people·men·women·children 같은 불규칙 복수형도 확인한다."
S89 = "원문항은 one of + 최상급 + 복수명사의 명사 형태를 묻는데, 변형은 비교급 중복·원급 비교 등 여러 요소를 섞어 평가 요소가 달라졌고 발문도 달랐다. 원문항 발문으로 되돌리고 다섯 문장 모두 one of 뒤 명사의 형태를 묻게 다시 썼다. 원문항은 (D)도 옳아 ②와 ⑤가 모두 답이 될 수 있으므로, 예시는 옳은 문장을 모두 담은 조합만 답이 되게 짰다."
def f89(t, lines, judge, ok, c, a):
    F(2, 89, t, st=ST89, p="<보기>\n" + "\n".join(lines), c=c, a=a, r=R89, pre=["문장별 판정: " + j for j in judge], k=f"옳은 문장은 {ok}이고, 이 문장들로만 묶인 보기가 정답이다.",
      n=setnotes(c, ok, "옳은 문장"), s=S89 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f89("B", ["(A) One of my favorite <u>hobbies</u> is hiking.", "(B) Mina is one of the smartest <u>student</u> in class.", "(C) This is one of the oldest <u>building</u> in Seoul.", "(D) One of the <u>windows</u> in my room is broken.", "(E) He is one of the best <u>player</u> on the team."],
    ["(A) O. one of + 복수명사(hobbies)이다.", "(B) X. one of 뒤에는 복수명사(students)를 쓴다.", "(C) X. one of 뒤에는 복수명사(buildings)를 쓴다.", "(D) O. one of + 복수명사(windows)이다.", "(E) X. one of 뒤에는 복수명사(players)를 쓴다."],
    "(A), (D)", ["(A), (B)", "(A), (D)", "(C), (D)", "(A), (D), (E)", "(B), (C), (E)"], 2)
f89("C", ["(A) One of the tallest <u>buildings</u> is downtown.", "(B) She is one of the most famous <u>singer</u> in Korea.", "(C) One of my <u>friend</u> lives in Canada.", "(D) This is one of the most useful <u>apps</u> I know.", "(E) One of the <u>students</u> was late today."],
    ["(A) O. one of + 복수명사(buildings)이다.", "(B) X. one of 뒤에는 복수명사(singers)를 쓴다.", "(C) X. one of 뒤에는 복수명사(friends)를 쓴다.", "(D) O. one of + 복수명사(apps)이다.", "(E) O. one of + 복수명사(students)이다."],
    "(A), (D), (E)", ["(A), (B)", "(C), (D)", "(A), (D), (E)", "(B), (C), (E)", "(A), (C), (D)"], 3)
f89("D", ["(A) One of my favorite <u>book</u> is missing.", "(B) Leo is one of the fastest <u>runners</u> in our school.", "(C) One of the <u>cars</u> in the parking lot is red.", "(D) It is one of the most beautiful <u>place</u> in the world.", "(E) One of the <u>teacher</u> is from Canada."],
    ["(A) X. one of 뒤에는 복수명사(books)를 쓴다.", "(B) O. one of + 복수명사(runners)이다.", "(C) O. one of + 복수명사(cars)이다.", "(D) X. one of 뒤에는 복수명사(places)를 쓴다.", "(E) X. one of 뒤에는 복수명사(teachers)를 쓴다."],
    "(B), (C)", ["(A), (B)", "(C), (D)", "(A), (C), (E)", "(B), (C)", "(B), (D), (E)"], 4)
f89("E", ["(A) One of the best <u>restaurants</u> is nearby.", "(B) He is one of the richest <u>man</u> in town.", "(C) One of my <u>cousins</u> is a pilot.", "(D) This is one of the easiest <u>question</u> on the test.", "(E) She is one of the kindest <u>women</u> I have ever met."],
    ["(A) O. one of + 복수명사(restaurants)이다.", "(B) X. one of 뒤에는 복수명사(men)를 쓴다.", "(C) O. one of + 복수명사(cousins)이다.", "(D) X. one of 뒤에는 복수명사(questions)를 쓴다.", "(E) O. one of + 불규칙 복수명사(women)이다."],
    "(A), (C), (E)", ["(A), (B)", "(B), (D)", "(C), (D), (E)", "(A), (B), (E)", "(A), (C), (E)"], 5)
f89("F", ["(A) One of the most interesting <u>story</u> is about space.", "(B) Tom is one of the tallest <u>boys</u> in class.", "(C) One of the <u>child</u> is crying.", "(D) Jeju is one of the most popular <u>islands</u> in Korea.", "(E) One of my favorite <u>songs</u> is on the radio."],
    ["(A) X. one of 뒤에는 복수명사(stories)를 쓴다.", "(B) O. one of + 복수명사(boys)이다.", "(C) X. one of 뒤에는 복수명사(children)를 쓴다.", "(D) O. one of + 복수명사(islands)이다.", "(E) O. one of + 복수명사(songs)이다."],
    "(B), (D), (E)", ["(B), (D), (E)", "(A), (B)", "(C), (D)", "(A), (C), (E)", "(B), (C), (D)"], 1)

# 2-90 the + 비교급 / as ~ as possible / No other … 비교급 than: 원문항 형식
ST90 = "다음 빈칸에 들어갈 가장 알맞은 표현을 고르시오."
R90 = "두 대상 가운데 ‘더 ~한 쪽’은 the + 비교급으로, ‘가능한 한 ~하게’는 as + 원급 부사 + as possible로, ‘다른 어떤 …도 ~보다 더 …하지 않다’는 No other + 명사 + 비교급 + than으로 나타낸다. 동사를 꾸미는 자리에는 부사를, be동사 뒤에는 형용사를 쓴다."
S90 = "원문항 대화의 ‘as ~ as possible’, ‘No other … 비교급 than’ 구문이 빠지고 비교급 형용사·부사 구별만 남아 평가 요소가 줄었고, 발문도 달랐다. 원문항 발문으로 되돌리고, 원문항처럼 the + 비교급, as + 부사 + as possible, No other … 비교급 than을 빈칸으로 두어 다시 썼다."
TB = {"better than": "두 대상 중 더 나은 쪽은 the + 비교급으로 쓰며, better than 뒤에는 비교 대상이 와야 한다.", "safer than": "두 대상 중 더 안전한 쪽은 the + 비교급으로 쓰며, safer than 뒤에는 비교 대상이 와야 한다.",
      "simpler than": "두 대상 중 더 간단한 쪽은 the + 비교급으로 쓰며, simpler than 뒤에는 비교 대상이 와야 한다."}
ADV = "동사를 꾸미는 자리이므로 형용사가 아니라 부사를 쓴다."
def f90(t, lines, c, a, good, why, k):
    F(2, 90, t, st=ST90, p="\n".join(lines), c=c, a=a, r=R90, n=pair(c, a, good, why), k=k, s=S90 + f" 정답 위치 {'①②③④⑤'[a-1]}.")
f90("B", ["A: Who is __________ candidate, Mina or Jane?", "B: Mina, but she should speak as __________ as possible.", "A: I think so, too. No other candidate is __________ than Mina."],
    ["the better - clear - more confident", "better than - clearly - more confident", "the better - clearly - more confident", "the better - clearly - confidenter", "better than - clear - more confidently"], 3,
    ["the better", "clearly", "more confident"], [TB, {"clear": ADV}, {"confidenter": "confident의 비교급은 more confident이다.", "more confidently": "be동사 뒤 보어 자리이므로 부사가 아니라 형용사를 쓴다."}],
    "둘 중 더 나은 쪽이므로 the better, speak를 꾸미는 부사 clearly, be동사 뒤 형용사의 비교급 more confident이다.")
f90("C", ["A: Which route is __________, A or B?", "B: B. But walk as __________ as possible there.", "A: OK. No other route is __________ than B."],
    ["the safer - quietly - shorter", "safer than - quietly - more short", "the safer - quiet - shorter", "safer than - quietly - shorter", "the safer - quietly - more short"], 1,
    ["the safer", "quietly", "shorter"], [TB, {"quiet": ADV}, {"more short": "short의 비교급은 shorter이다."}],
    "둘 중 더 안전한 쪽이므로 the safer, walk를 꾸미는 부사 quietly, -er형 비교급 shorter이다.")
f90("D", ["A: Who is __________ speaker, Tom or Leo?", "B: Tom. But he should speak as __________ as possible.", "A: True. No other speaker is __________ than Tom."],
    ["better than - slowly - funnier", "the better - slow - more funny", "the better - slowly - more funnier", "the better - slow - funnier", "the better - slowly - funnier"], 5,
    ["the better", "slowly", "funnier"], [TB, {"slow": ADV}, {"more funny": "funny의 비교급은 funnier이다.", "more funnier": "funnier 앞에 more를 겹쳐 쓸 수 없다."}],
    "둘 중 더 나은 쪽이므로 the better, speak를 꾸미는 부사 slowly, -er형 비교급 funnier이다.")
f90("E", ["A: Which plan is __________, the first or the second?", "B: The second. We should start it as __________ as possible.", "A: Right. No other plan is __________ than this one."],
    ["the simpler - quick - cheaper", "the simpler - quickly - cheaper", "simpler than - quickly - more cheap", "the simpler - quickly - more cheaper", "simpler than - quick - cheaper"], 2,
    ["the simpler", "quickly", "cheaper"], [TB, {"quick": ADV}, {"more cheap": "cheap의 비교급은 cheaper이다.", "more cheaper": "cheaper 앞에 more를 겹쳐 쓸 수 없다."}],
    "둘 중 더 간단한 쪽이므로 the simpler, start를 꾸미는 부사 quickly, -er형 비교급 cheaper이다.")
f90("F", ["A: Who is __________ cook, your mom or your dad?", "B: My dad. He cooks as __________ as possible on weekends.", "A: Wow. No other cook is __________ than him."],
    ["better than - often - creativer", "the better - oftenly - more creative", "the better - often - creativer", "the better - often - more creative", "better than - oftenly - more creative"], 4,
    ["the better", "often", "more creative"], [TB, {"oftenly": "often은 그 자체로 부사이며 oftenly라는 형태는 없다."}, {"creativer": "creative의 비교급은 more creative이다."}],
    "둘 중 더 나은 쪽이므로 the better, cooks를 꾸미는 부사 often, 긴 형용사의 비교급 more creative이다.")

# ---- 2차 감수(2026-10) 추가 ----
# 2-88 C·D: 영어에 없는 형태(expensiveest, talliest) 오답 → 원문항처럼 실제 단어로 된 오답으로
R88 = "최상급은 the + -est 또는 the most + 원급으로 쓰고, 범위는 in + 장소·집단, of + 복수명사로 나타낸다. most와 -est를 겹쳐 쓰지 않는다."
S88 = "오답 가운데 영어에 없는 형태({})가 있어 형태만으로 지워졌다. 원문항의 오답처럼 실제 단어로 된 틀린 문장으로 바꿨다. 나머지 보기와 정답은 그대로다."
mk(2, 88, "C", [("This is the most expensive bag than this store.", "최상급의 범위는 than이 아니라 in으로 나타내므로"), ("This is more expensive bag in this store.", "‘가장 비싼’은 비교급이 아니라 최상급으로 써야 하므로"),
                ("This is a most expensive bag in this store.", "최상급 앞에는 a가 아니라 the를 쓰므로"), ("This is most expensive the bag in this store.", "the가 most expensive 앞에 와야 하므로"),
                ("This is the most expensive bag in this store.", "the most expensive + 명사 + in + 장소로 바르게 썼으므로")], 5, R88, S88.format("expensiveest"))
mk(2, 88, "D", [("Tom is the most tallest of the three brothers.", "most와 -est를 겹쳐 쓸 수 없으므로"), ("Tom is the tallest than the three brothers.", "최상급의 범위는 than이 아니라 of로 나타내므로"),
                ("Tom is the taller of the three brothers.", "셋 중 가장 큰 것은 비교급이 아니라 최상급으로 써야 하므로"), ("Tom is the more tall of the three brothers.", "tall의 최상급은 the tallest이므로"),
                ("Tom is the tallest of the three brothers.", "the tallest + of + 복수명사로 바르게 썼으므로")], 5, R88, S88.format("talliest"))

# 2-89 B~F: 원문항처럼 옳은 문장 둘 + 모두 두 문장 조합 보기
S89 = "원문항은 one of + 최상급 + 복수명사의 명사 형태를 묻는데, 변형은 비교급 중복·원급 비교 등 여러 요소를 섞어 평가 요소가 달라졌고 발문도 달랐다. 원문항 발문으로 되돌리고 다섯 문장 모두 one of 뒤 명사의 형태를 묻게 다시 썼다. 고친 원문항처럼 옳은 문장을 둘로 하고 보기를 모두 두 문장 조합으로 맞췄다."
def g89(t, sents, c, a):
    FIX.pop((2, 89, t), None)
    L = "ABCDE"; lines, judge, ok = [], [], []
    for i, (pre, noun, plural, post) in enumerate(sents):
        good = noun == plural
        lines.append(f"({L[i]}) {pre} <u>{noun}</u>{post}")
        judge.append(f"({L[i]}) O. one of + 복수명사({plural})이다." if good else f"({L[i]}) X. one of 뒤에는 복수명사({plural})를 쓴다.")
        if good: ok.append(f"({L[i]})")
    assert len(ok) == 2 and c[a - 1] == ", ".join(ok), (t, ok)
    f89(t, lines, judge, ", ".join(ok), c, a)
g89("B", [("One of my favorite", "hobbies", "hobbies", " is hiking."), ("Mina is one of the smartest", "student", "students", " in class."), ("This is one of the oldest", "building", "buildings", " in Seoul."),
          ("One of the", "windows", "windows", " in my room is broken."), ("He is one of the best", "player", "players", " on the team.")], ["(A), (B)", "(A), (D)", "(C), (D)", "(A), (E)", "(B), (E)"], 2)
g89("C", [("One of the tallest", "building", "buildings", " is downtown."), ("She is one of the most famous", "singer", "singers", " in Korea."), ("One of my", "friend", "friends", " lives in Canada."),
          ("This is one of the most useful", "apps", "apps", " I know."), ("One of the", "students", "students", " was late today.")], ["(A), (B)", "(C), (D)", "(A), (E)", "(B), (D)", "(D), (E)"], 5)
g89("D", [("One of my favorite", "book", "books", " is missing."), ("Leo is one of the fastest", "runners", "runners", " in our school."), ("One of the", "cars", "cars", " in the parking lot is red."),
          ("It is one of the most beautiful", "place", "places", " in the world."), ("One of the", "teacher", "teachers", " is from Canada.")], ["(A), (B)", "(C), (D)", "(A), (E)", "(B), (C)", "(B), (E)"], 4)
g89("E", [("One of the best", "restaurants", "restaurants", " is nearby."), ("He is one of the richest", "man", "men", " in town."), ("One of my", "cousins", "cousins", " is a pilot."),
          ("This is one of the easiest", "question", "questions", " on the test."), ("She is one of the kindest", "woman", "women", " I have ever met.")], ["(A), (B)", "(B), (D)", "(C), (D)", "(A), (E)", "(A), (C)"], 5)
g89("F", [("One of the most interesting", "story", "stories", " is about space."), ("Tom is one of the tallest", "boys", "boys", " in class."), ("One of the", "child", "children", " is crying."),
          ("Jeju is one of the most popular", "island", "islands", " in Korea."), ("One of my favorite", "songs", "songs", " is on the radio.")], ["(B), (E)", "(A), (B)", "(C), (D)", "(A), (E)", "(B), (D)"], 1)
