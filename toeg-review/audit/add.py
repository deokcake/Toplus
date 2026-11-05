# 사용: python3 audit/add.py <<'X' ... X  (줄마다: 문항|등급|유형|문제|수정 제안)
import json, sys, os
P = "audit/ref_audit.json"
d = json.load(open(P)) if os.path.exists(P) else {}
for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith("#"): continue
    k, lv, ty, prob, fix = [x.strip() for x in line.split("|", 4)]
    d.setdefault(k, [])
    if not any(x["problem"] == prob for x in d[k]): d[k].append({"level": lv, "type": ty, "problem": prob, "fix": fix})
json.dump(d, open(P, "w"), ensure_ascii=False, indent=1)
print("기록:", sum(len(v) for v in d.values()), "건 /", len(d), "문항")
