#!/usr/bin/env python3
"""대본 JSON(src/video/SCRIPT_SPEC.md 규격) → MP4 + SRT.
사용: python3 tools/video/render.py <대본.json> [<대본.json> ...] [--out 결과/영상/파일럿] [--ko Yuna] [--en Samantha]
- 화면: PIL로 1920×1080 장면 그림(제목 줄, 본문, 강조·지움·✓✗, 자막 띠). 풀이 순서 장면은 단계마다 그림을 바꾼다.
- 소리: 내레이션을 문장으로 나누고, 문장 안의 한국어/영어 덩어리를 각각 macOS `say`(한국어 Yuna, 영어 Samantha)로 합성해 이어 붙인다.
- 조립: 문장마다 (그림 + 자막, 그 문장 소리) 조각을 만들고 ffmpeg(imageio-ffmpeg 내장)로 이어 붙인다. 장면 길이는 대본의 초와 소리 길이 중 긴 쪽."""
import sys, os, re, json, wave, subprocess, shutil, tempfile, argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
W, H = 1920, 1080
FONT = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
C = {"bg": (247, 248, 250), "ink": (28, 31, 38), "muted": (105, 112, 125), "bar": (36, 52, 84), "bar_ink": (255, 255, 255),
     "hl": (255, 236, 150), "strike": (214, 69, 69), "ok": (31, 143, 94), "bad": (214, 69, 69), "sub_bg": (20, 24, 32, 215), "sub_ink": (255, 255, 255),
     "card": (255, 255, 255), "line": (222, 226, 232), "accent": (46, 94, 170)}
SR = 22050

def font(size, bold=False):
    # AppleSDGothicNeo.ttc: 0 Regular … 6 Bold (환경마다 다를 수 있어 이름으로 찾는다)
    for idx in range(0, 12):
        try:
            f = ImageFont.truetype(FONT, size, index=idx)
            name = " ".join(f.getname())
            if (bold and "Bold" in name and "Semi" not in name and "Extra" not in name) or (not bold and "Regular" in name): return f
        except Exception: break
    return ImageFont.truetype(FONT, size, index=0)

# ---------- 글 ----------
def wrap(draw, text, f, width):
    """문단을 폭에 맞춰 줄로 나눈다(낱말 단위, 긴 낱말은 글자 단위)."""
    out = []
    for para in text.split("\n"):
        if not para.strip(): out.append(""); continue
        line = ""
        for tok in re.findall(r"\S+\s*", para):
            if draw.textlength(line + tok, font=f) <= width or not line: line += tok
            else: out.append(line.rstrip()); line = tok
            while draw.textlength(line, font=f) > width and len(line) > 1:   # 한 낱말이 폭보다 길면 글자 단위로
                cut = max(1, int(len(line) * width / draw.textlength(line, font=f)) - 1)
                out.append(line[:cut]); line = line[cut:]
        out.append(line.rstrip())
    return out

def spans(line, needles):
    """줄 안에서 강조할 조각들의 (시작, 끝) 목록. 영어 낱말은 낱말 경계로 찾는다."""
    res = []
    for n in needles:
        if not n: continue
        if re.fullmatch(r"[A-Za-z'’ -]+", n): pat = r"(?<![A-Za-z])" + re.escape(n) + r"(?![A-Za-z])"   # 영어 낱말(’ 포함)은 낱말 경계로
        else: pat = re.escape(n)
        for m in re.finditer(pat, line): res.append((m.start(), m.end()))
    return res

def draw_text_block(img, draw, lines, x, y, f, lh, width, hl=(), strike=(), marks=None, color=None):
    """줄 목록을 그린다. 강조는 노란 바탕, 지움은 붉은 줄, 보기 줄 끝에는 ✓/✗."""
    color = color or C["ink"]
    for line in lines:
        struck = bool(spans(line, strike))
        for s, e in ([] if struck else spans(line, hl)):   # 지운 줄 안의 낱말은 강조하지 않는다
            x0 = x + draw.textlength(line[:s], font=f); x1 = x + draw.textlength(line[:e], font=f)
            draw.rounded_rectangle([x0 - 6, y - 4, x1 + 6, y + lh - 10], radius=8, fill=C["hl"])
        draw.text((x, y), line, font=f, fill=color)
        for s, e in spans(line, strike):
            x0 = x + draw.textlength(line[:s], font=f); x1 = x + draw.textlength(line[:e], font=f)
            draw.line([x0, y + lh * 0.46, x1, y + lh * 0.46], fill=C["strike"], width=5)
        if marks:
            m = re.match(r"\s*([①②③④⑤])", line)
            if m and marks.get(m[1]) and not re.search(r"[✓✗]", line):
                sym = marks[m[1]]; fx = x + width - 70
                draw.text((fx, y - 6), "✓" if sym == "✓" else "×", font=font(int(lh * 0.95), True), fill=C["ok"] if sym == "✓" else C["bad"])
        y += lh
    return y

def colorize_marks(draw, lines, x, y, f, lh):
    """화면 글 안에 이미 ✓/✗가 있으면 그 기호만 색을 입힌다."""
    for line in lines:
        for m in re.finditer(r"[✓✗]", line):
            x0 = x + draw.textlength(line[:m.start()], font=f)
            draw.rectangle([x0, y, x0 + draw.textlength(m[0], font=f), y + lh - 8], fill=C["bg"])
            draw.text((x0, y), "✓" if m[0] == "✓" else "×", font=font(f.size, True), fill=C["ok"] if m[0] == "✓" else C["bad"])
        y += lh

def render_frame(doc, scene, step=None, subtitle="", path=None):
    img = Image.new("RGB", (W, H), C["bg"]); d = ImageDraw.Draw(img, "RGBA")
    # 제목 줄
    d.rectangle([0, 0, W, 96], fill=C["bar"])
    d.text((56, 24), f"{doc['grade']}급 · {doc['chapter']} · {doc['key'].split('-')[1]}번", font=font(38, True), fill=C["bar_ink"])
    tag = scene["name"] if step is None else f"{scene['name']} · {step['step']}단계"
    tw = d.textlength(tag, font=font(32)); d.text((W - 56 - tw, 30), tag, font=font(32), fill=(200, 212, 235))
    if doc.get("title"): d.text((56, 112), doc["title"], font=font(28), fill=C["muted"])
    sc = scene["screen"]; text = sc.get("text", "")
    hl = list(sc.get("highlight", [])); strike = []; note = ""
    if step is not None:
        hl = list(step.get("highlight", []))
        for st in sc.get("steps", []):        # 앞 단계의 지움은 그대로 둔다
            if st["step"] <= step["step"]: strike += st.get("strike", [])
        note = step.get("note", "")
    has_marks = bool(sc.get("marks")) and scene["no"] == 5
    big = scene["no"] in (1, 6)
    size = 60 if big else (48 if len(text) < 260 else 40)
    f = font(size, big); lh = int(size * 1.55)
    body_w = W - 112 - (560 if note else 0)
    lines = wrap(d, text, f, body_w - (90 if has_marks else 0))
    while len(lines) * lh > H - 160 - 170 and size > 26:
        size -= 4; f = font(size, big); lh = int(size * 1.5); lines = wrap(d, text, f, body_w - (90 if has_marks else 0))
    y0 = 170 if not big else max(170, (H - 170 - len(lines) * lh) // 2 - 40)
    draw_text_block(img, d, lines, 56, y0, f, lh, body_w, hl=hl, strike=strike, marks=sc.get("marks") if has_marks else None)
    colorize_marks(d, lines, 56, y0, f, lh)
    if note:   # 단계 설명 칸(풀이 순서)
        nx = W - 56 - 500; d.rounded_rectangle([nx, 170, W - 56, 170 + 300], radius=16, fill=C["card"], outline=C["line"], width=2)
        d.text((nx + 24, 186), f"{step['step']}단계", font=font(30, True), fill=C["accent"])
        nf = font(30); nl = wrap(d, note, nf, 500 - 48)
        yy = 240
        for l in nl: d.text((nx + 24, yy), l, font=nf, fill=C["ink"]); yy += 44
    if subtitle:   # 자막 띠
        sf = font(40); sl = wrap(d, subtitle, sf, W - 240)[:3]; bh = 40 + 56 * len(sl)
        d.rectangle([0, H - bh - 24, W, H], fill=C["sub_bg"])
        yy = H - bh - 4
        for l in sl:
            tw = d.textlength(l, font=sf); d.text(((W - tw) / 2, yy), l, font=sf, fill=C["sub_ink"]); yy += 56
    if path: img.save(path)
    return img

# ---------- 소리 ----------
def sentences(text):
    text = re.sub(r"\s+", " ", text.strip())
    parts = re.split(r"(?<=[.?!])\s+(?=[^\s])", text)
    return [p.strip() for p in parts if p.strip()]

EN = re.compile(r"[A-Za-z][A-Za-z0-9'’\-]*(?:[ ,]+[A-Za-z0-9'’\-]+)*[?!.]?")
def runs(sentence):
    """문장을 (언어, 글) 덩어리로 나눈다. 영어는 두 낱말 이상이거나 문장 부호를 가진 덩어리만 영어 음성으로."""
    out = []; pos = 0
    for m in EN.finditer(sentence):
        seg = m.group(0)
        if len(re.findall(r"[A-Za-z]+", seg)) >= 2 or re.search(r"[?!.]$", seg):
            if m.start() > pos: out.append(("ko", sentence[pos:m.start()]))
            out.append(("en", seg)); pos = m.end()
    if pos < len(sentence): out.append(("ko", sentence[pos:]))
    return [(l, t) for l, t in out if t.strip()]

def say(text, voice, path, rate=None):
    """macOS 내장 음성(say). 신경망 음성(이름에 Neural)은 edge-tts로 만든다."""
    if "Neural" in voice:
        mp3 = path[:-4] + ".mp3"
        for attempt in range(4):
            try:
                subprocess.run([sys.executable, "-m", "edge_tts", "--voice", voice, "--rate=-4%", "--text", text, "--write-media", mp3], check=True, capture_output=True, timeout=120)
                break
            except Exception as e:
                if attempt == 3: raise
        subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", mp3, "-ar", str(SR), "-ac", "1", "-c:a", "pcm_s16le", path], check=True)
        return
    cmd = ["say", "-v", voice, "-o", path, "--data-format=LEI16@22050"]
    if rate: cmd += ["-r", str(rate)]
    subprocess.run(cmd + [text], check=True)

def wav_frames(path):
    with wave.open(path, "rb") as w: return w.readframes(w.getnframes())

def silence(sec): return b"\x00\x00" * int(SR * sec)

def synth_sentence(sent, ko, en, tmp, i):
    """문장 하나 → PCM 바이트. 내장 음성은 한국어/영어 덩어리를 나눠 두 음성으로, 신경망 한국어 음성은 문장 통째로(영어도 스스로 읽는다)."""
    pcm = b""
    parts = [("ko", sent)] if "Neural" in ko else runs(sent)
    for j, (lang, t) in enumerate(parts):
        t = t.replace("_", " ").strip()
        if not t or not re.search(r"[가-힣A-Za-z0-9]", t): continue
        p = os.path.join(tmp, f"s{i}_{j}.wav")
        say(t, ko if lang == "ko" else en, p, rate=175 if lang == "ko" else 165)
        if pcm: pcm += silence(0.15)
        pcm += wav_frames(p)
    return pcm

def write_wav(path, pcm):
    with wave.open(path, "wb") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm)

# ---------- 조립 ----------
STEP_WORDS = ["첫째", "둘째", "셋째", "넷째", "다섯째"]
def build(doc_path, out_dir, ko, en):
    doc = json.load(open(doc_path, encoding="utf-8")); key = doc["key"]
    out_dir = Path(out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    tmp = tempfile.mkdtemp(prefix=f"toeg_{key}_")
    segs = []   # (png, wav, dur)
    srt = []; t = 0.0
    for scene in doc["scenes"]:
        sents = sentences(scene.get("narration", ""))
        steps = scene["screen"].get("steps") or []
        step_i = -1; total = 0.0
        for i, s in enumerate(sents):
            if steps and any(s.startswith(w) for w in STEP_WORDS): step_i = min(step_i + 1, len(steps) - 1)
            step = steps[step_i] if steps and step_i >= 0 else (steps[0] if steps and i == 0 else None)
            pcm = synth_sentence(s, ko, en, tmp, f"{scene['no']}_{i}") + silence(0.45)
            dur = len(pcm) / 2 / SR
            png = os.path.join(tmp, f"f{scene['no']}_{i}.png"); wav = os.path.join(tmp, f"a{scene['no']}_{i}.wav")
            render_frame(doc, scene, step=step, subtitle=s, path=png); write_wav(wav, pcm)
            segs.append((png, wav, dur)); srt.append((t, t + dur - 0.3, s)); t += dur; total += dur
        hold = max(0.6, float(scene.get("sec", 0)) - total)   # 대본의 초만큼은 화면을 유지(문제 풀 시간)
        png = os.path.join(tmp, f"f{scene['no']}_hold.png"); wav = os.path.join(tmp, f"a{scene['no']}_hold.wav")
        last_step = steps[-1] if steps else None
        render_frame(doc, scene, step=last_step, subtitle="", path=png); write_wav(wav, silence(hold))
        segs.append((png, wav, hold)); t += hold
    # 조각 → mp4
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as L:
        for i, (png, wav, dur) in enumerate(segs):
            mp4 = os.path.join(tmp, f"seg{i:03d}.mp4")
            subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-loop", "1", "-framerate", "30", "-i", png, "-i", wav, "-t", f"{dur:.3f}",
                            "-c:v", "libx264", "-preset", "veryfast", "-tune", "stillimage", "-pix_fmt", "yuv420p", "-r", "30",
                            "-c:a", "aac", "-b:a", "160k", "-ar", str(SR), "-ac", "1", "-shortest", mp4], check=True)
            L.write(f"file '{mp4}'\n")
    out = out_dir / f"{key}.mp4"
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", "-movflags", "+faststart", str(out)], check=True)
    def ts(x): h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60; return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")
    with open(out_dir / f"{key}.srt", "w", encoding="utf-8") as S:
        for i, (a, b, s) in enumerate(srt, 1): S.write(f"{i}\n{ts(a)} --> {ts(b)}\n{s}\n\n")
    # 장면 대표 그림(확인용)
    (out_dir / "frames").mkdir(exist_ok=True)
    for scene in doc["scenes"]:
        st = (scene["screen"].get("steps") or [None])[-1]
        render_frame(doc, scene, step=st, subtitle=sentences(scene.get("narration", ""))[:1][0] if scene.get("narration") else "", path=str(out_dir / "frames" / f"{key}_s{scene['no']}.png"))
    shutil.rmtree(tmp, ignore_errors=True)
    return out, t

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("docs", nargs="+"); ap.add_argument("--out", default="결과/영상/파일럿"); ap.add_argument("--ko", default="ko-KR-SunHiNeural"); ap.add_argument("--en", default="en-US-JennyNeural")
    a = ap.parse_args()
    for d in a.docs:
        out, dur = build(d, a.out, a.ko, a.en); print(out, f"{dur:.1f}초")
