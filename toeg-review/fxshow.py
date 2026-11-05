#!/usr/bin/env python3
"""변형 문항 전체 보기: python3 fxshow.py 1-4D 1-9F ..."""
import json, sys
rows = {t: {f'{r["g"]}-{r["n"]}': r for r in json.load(open(f"page/data/{t}.json", encoding="utf-8"))} for t in "BCDEF"}
for a in sys.argv[1:]:
    k, t = a[:-1], a[-1]; r = rows[t][k]
    print(f"=== {k}{t}\nSTEM: {r['stem']}\nPASS: {r['passage']}\nC: {r['c']} ANS {r['ans']}\n{r['expl']}\n")
