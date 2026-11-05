
# 2026-10-27 2차 감수 반영(fx/z9g_memo1027b.py)에 맞춰 풀이 순서 칸을 고친다. (g9g 뒤에 읽힌다)
def U(g_, n_, **kw): EX[(g_, n_)].update(kw)
U(4, 100, D="(A) your sister are(is), (C) How a tall boy(What a tall boy), (D) What beautiful(How beautiful)이 틀렸다.",
          E="(B) your puppies is(are), (C) What interesting book(an이 빠졌다), (D) How a beautiful day(What a beautiful day)가 틀렸다.",
          F="(A) Tom run(runs), (C) How a kind girl(What a kind girl), (E) the weather are(is)가 틀렸다.")
U(4, 106, D=("likes", "좋아하는 것은 rock music"))
U(4, 15, F="ⓒ These car is(This car is), ⓓ The news ~ are(is)가 틀렸다.")
U(4, 18, F=("You're(= You are)", "your"))
U(4, 27, D=("eats", "Jane(3인칭 단수)이므로 Does"))
U(4, 79, D=("taller", "his older brother Mike"), F=("faster", "her friend Amy"))
U(4, 87, D="two hours는 기간의 길이이므로 for, the boring movie는 특정한 때를 나타내는 명사구이므로 during이다.",
         E="I was eating dinner는 주어 + 동사이므로 while, thirty minutes는 기간의 길이이므로 for다.")
