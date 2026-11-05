# 조립된 수정 예시 보기: python3 fxpeek.py 2-15B 2-20C
import sys, re
import fxbuild as B
raw = B.load()
for a in sys.argv[1:]:
    m = re.match(r"(\d+)-(\d+)([B-F])", a); key = (int(m[1]), int(m[2]), m[3])
    it = B.build(key, raw[key])
    print("===", a, "| 요지:", it["sum"]); print("S:", it["stem"]); print("P:", it["passage"])
    print("C:", " / ".join(f"{i+1}){x}" for i, x in enumerate(it["c"])), "| 답", it["ans"]); print(it["expl"]); print()
