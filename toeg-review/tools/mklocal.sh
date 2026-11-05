#!/bin/sh
# 로컬 시험용 페이지: 가짜 공유 런타임 + 상태 노출
cd "$(dirname "$0")/.."
{ echo '<meta charset="utf-8">'; echo '<script>'; cat tools/mock.js; echo '</script>'; cat page/index.html; } | python3 -c "import sys; s=sys.stdin.read(); a='const \$ = s => document.querySelector(s);'; assert s.count(a)==1; sys.stdout.write(s.replace(a, a+' window.__S = S;'))" > page/_local.html
echo "page/_local.html"
