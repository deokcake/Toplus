import json,sys
items=json.load(open(sys.argv[1],encoding="utf-8")); inp={x["key"]:x for x in json.load(open(sys.argv[2],encoding="utf-8"))}
full = len(sys.argv)>3
C="①②③④⑤"
for it in items:
    r=inp[it["key"]]["ref"]
    print(f"######## {it['key']}  [원문항] {r['stem']} | {r['passage'][:120]!r} | {r['c']} → {C[r['ans']-1]}")
    print(f"형식: {it['ref_format']}  ⇒  {it['new_format']}")
    print("발문:", it["stem"])
    if it["passage"]: print("지문:\n"+it["passage"])
    for i,c in enumerate(it["c"]): print(f"  {C[i]}{'*' if i+1==it['ans'] else ' '} {c}")
    if full: print("해설:\n"+it["expl"])
    else:
        ex=it["expl"].split("\n"); print("  "+ex[0][:200]); print("  "+next((l for l in ex if l.startswith("정답 판단")),"")[:200])
    print()
