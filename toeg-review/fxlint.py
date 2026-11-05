# 새로 쓴 해설·요지에서 영어 단어 바로 뒤 조사 찾기: python3 fxlint.py fx/g2_ch03.py
import sys, re
PAT = re.compile(r"[A-Za-z'’](?:은|는|이|가|을|를|과|와|의|로|으로|에서|에게|에|도|만|이다|이며|이고|이므로|라서|라는)(?=[\s.,)?!:·]|$)")
OK = re.compile(r"be동사|to부정사|-ing|p\.p\.")
for f in sys.argv[1:]:
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        for m in PAT.finditer(line):
            ctx = line[max(0, m.start() - 25): m.end() + 3]
            if OK.search(ctx[-12:]): continue
            print(f"{f}:{i}: …{ctx.strip()}…")
