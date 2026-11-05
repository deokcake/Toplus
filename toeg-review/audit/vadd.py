# 사용: python3 audit/vadd.py <<'X' ... X  (줄마다: 문항|유형들(BCDEF 중)|등급|문제|수정 제안|처리)
# 처리: 예시적용(지금 Claude 수정 예시로 해결) / 예시다시적용(예시를 고쳤으니 다시 적용) / 직접수정(예시로 해결 안 됨)
import json, sys, os
P = "audit/variant_audit.json"
d = json.load(open(P)) if os.path.exists(P) else []
for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith("#"): continue
    k, ts, lv, prob, fix, how = [x.strip() for x in line.split("|", 5)]
    for t in ts:
        d = [x for x in d if not (x["key"] == k and x["type"] == t and x["problem"] == prob)]
        d.append({"key": k, "type": t, "level": lv, "problem": prob, "fix": fix, "how": how})
json.dump(d, open(P, "w"), ensure_ascii=False, indent=1)
print("기록:", len(d), "건")
