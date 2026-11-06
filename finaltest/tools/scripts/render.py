#!/usr/bin/env python3
"""문제 JSON을 Typst 템플릿으로 조판해 PDF로 뽑는다.

사용법:
    python3 scripts/render.py 문제.json -o 출력폴더 --mode both

--mode student : 문제지만
--mode key     : 정답·해설지만
--mode both    : 둘 다 (기본값)
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# 본문으로 취급해 Typst 마크업으로 해석할 필드
TEXT_KEYS = {
    "title", "description", "prompt", "explanation", "text",
    "instructions", "choices", "left", "right", "note", "box", "table",
}
# 마크업 충돌을 일으키는 문자만 막고, $수식$ / *굵게* 는 살려 둔다
ESCAPES = {"#": r"\#", "@": r"\@", "<": r"\<", ">": r"\>", "~": r"\~"}
BLANK = "#box(width: 3.5em, baseline: 0.15em, line(length: 100%, stroke: 0.6pt))"


def prep(s):
    """문자열을 Typst 마크업으로 안전하게 변환."""
    if not isinstance(s, str):
        return s
    out = "".join(ESCAPES.get(c, c) for c in s)
    out = re.sub(r"_{2,}", BLANK, out)  # ___ → 빈칸 밑줄
    out = re.sub(r"⟪(.+?)⟫", r"#underline[\1]", out)  # ⟪word⟫ → 밑줄 친 단어
    return out


def walk(node, inside_text=False):
    if isinstance(node, dict):
        return {k: walk(v, k in TEXT_KEYS) for k, v in node.items()}
    if isinstance(node, list):
        return [walk(v, inside_text) for v in node]
    if isinstance(node, str) and inside_text:
        return prep(node)
    return node


def slugify(title, fallback="worksheet"):
    s = re.sub(r"[^\w가-힣 \-]", "", title or "").strip()
    s = re.sub(r"\s+", "_", s)
    return s[:60] or fallback


def compile_one(workdir, data, mode, out_path, template):
    (workdir / "data.json").write_text(
        json.dumps(data, ensure_ascii=False), encoding="utf-8")
    (workdir / "template.typ").write_text(
        template.read_text(encoding="utf-8"), encoding="utf-8")
    main = workdir / "main.typ"
    main.write_text(
        f'#import "template.typ": exam\n#exam(json("data.json"), mode: "{mode}")\n',
        encoding="utf-8")
    try:
        import typst
        typst.compile(str(main), output=str(out_path),
                      root=str(workdir), font_paths=["/usr/share/fonts"])
    except ImportError:
        subprocess.run(["typst", "compile", "--root", str(workdir),
                        str(main), str(out_path)], check=True)
    return out_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="문제 JSON 경로")
    ap.add_argument("-o", "--outdir", default="/mnt/user-data/outputs")
    ap.add_argument("--mode", choices=["student", "key", "both"], default="both")
    ap.add_argument("--keep-typ", action="store_true", help=".typ 소스도 남긴다")
    args = ap.parse_args()

    src = Path(args.input)
    data = walk(json.loads(src.read_text(encoding="utf-8")))
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    template = Path(__file__).resolve().parent.parent / "assets" / "template.typ"

    stem = slugify(json.loads(src.read_text(encoding="utf-8")).get("title", ""), src.stem)
    modes = ["student", "key"] if args.mode == "both" else [args.mode]
    if args.mode == "both" and not data.get("layout", {}).get("answer_key", True):
        modes = ["student"]

    made = []
    with tempfile.TemporaryDirectory() as td:
        wd = Path(td)
        for m in modes:
            suffix = "문제지" if m == "student" else "정답해설"
            out = outdir / f"{stem}_{suffix}.pdf"
            try:
                compile_one(wd, data, m, out, template)
            except Exception as e:
                print(f"[실패] {suffix}: {e}", file=sys.stderr)
                sys.exit(1)
            made.append(out)
        if args.keep_typ:
            shutil.copy(wd / "main.typ", outdir / f"{stem}.typ")
            shutil.copy(wd / "data.json", outdir / f"{stem}_data.json")

    for p in made:
        print(p)


if __name__ == "__main__":
    main()
