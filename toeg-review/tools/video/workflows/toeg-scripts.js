export const meta = {
  name: 'toeg-scripts',
  description: 'Per item number: review the 6 explanations (A~F) and write 6 standalone chalkboard video scripts, then independently verify both',
  phases: [{ title: 'Write', detail: 'review explanations + write 6 scripts per number' }, { title: 'Verify', detail: 'independent check of review findings and scripts, fix in place' }],
}
const P = args.root
const LEVEL = { 7: 'Korean elementary grade 3-4 (present tense only)', 6: 'Korean elementary grade 4', 5: 'Korean elementary grade 5-6', 4: 'Korean elementary grade 6 to middle school 1', 3: 'Korean middle school 1', 2: 'Korean middle school 2', 1: 'Korean middle school 3 to high school 1' }
const T6 = ['A', 'B', 'C', 'D', 'E', 'F']
const ISSUE = { type: 'object', properties: { kind: { type: 'string', enum: ['정확성', '구체성', '눈높이', '일관성', '표기', '대본', '정답의심'] }, where: { type: 'string' }, detail: { type: 'string' } }, required: ['kind', 'where', 'detail'] }
const WRITE = { type: 'object', properties: { review: { type: 'array', items: { type: 'object', properties: { type: { type: 'string', enum: T6 }, verdict: { type: 'string', enum: ['이상 없음', '보완 권장', '수정 필요'] }, issues: { type: 'array', items: ISSUE }, proposed: { type: 'string' } }, required: ['type', 'verdict', 'issues', 'proposed'] } }, notes: { type: 'string' } }, required: ['review', 'notes'] }
const VERIFY = { type: 'object', properties: { review: { type: 'array', items: { type: 'object', properties: { type: { type: 'string', enum: T6 }, final_verdict: { type: 'string', enum: ['이상 없음', '보완 권장', '수정 필요'] }, issues: { type: 'array', items: ISSUE }, proposed: { type: 'string' }, verifier_note: { type: 'string' } }, required: ['type', 'final_verdict', 'issues', 'proposed', 'verifier_note'] } }, script_fixes: { type: 'array', items: { type: 'string' } }, remaining: { type: 'array', items: { type: 'string' } } }, required: ['review', 'script_fixes', 'remaining'] }
const g = k => k.split('-')[0]

const writerPrompt = k => `You are an expert Korean English-grammar teacher. For TOEG (a Korean school English grammar test) you will (1) review answer explanations and (2) write narration scripts for short, standalone explanation videos. Grade ${g(k)}급 = ${LEVEL[g(k)]}. Item number ${k} has six items: A (the reference item) and B~F (variants on the same grammar point). Each of the six items gets its OWN video.

Project root: ${P}
Read first:
- src/video/SCRIPT_SPEC.md — video/script spec (6 scenes, chalkboard handwriting, narration rules).
- src/expl_review/EXPL_RULES.md — explanation review standard.
- src/video/fill_example_7-56-A.json — one finished video fill (7급). Follow its format and tone, not its content.
- work/video/in/${k}.json — the six items (stem, passage, c = options ①~⑤, ans, expl) and prior_review (an earlier review of some explanations; "verified": true means it was already double-checked).

STEP 1 — Solve and review. For each item, first solve it yourself from the stem/passage/options (do not trust the key blindly). Then review its explanation against EXPL_RULES.md: accuracy against the actual option text, a specific reason for each distractor, grade-level wording, consistency across A~F, the fixed 5-part format and notation, suitability for narration. Give verdict 이상 없음 / 보완 권장 / 수정 필요, concrete issues in Korean (quote the wrong phrase, say what is right), and proposed = the full corrected explanation in the same 5-part format with minimal edits ("" when 이상 없음). Never change the item itself. If the answer key itself seems wrong, add an issue of kind 정답의심 and keep everything on the current key. If prior_review exists, start from it: keep what is right, drop what is wrong, add what it missed.

STEP 2 — Write all six video scripts as ONE fill file: work/video/fill/${k}.json = {"A": {...}, "B": {...}, "C": {...}, "D": {...}, "E": {...}, "F": {...}}, each entry in exactly the example's format (title, intro, problem_narration, rule{card, narration}, steps[{note, highlight, strike, narration}], check{lines, narration}, summary{card, narration}, captions[6], sec[6]). The tool adds item text, headings, answer marks and scene structure. Requirements:
- Correct and universally valid: correct for THIS item (follow your corrected explanation where the current one is wrong), and every grammar statement must be true of English in general, not only of this item. No overgeneralizations; if the grade needs a simplification, scope it explicitly (say "be동사와 동사원형을 나란히 쓰지 않아요", not "be동사와 일반동사를 함께 쓰지 않아요", which progressive/passive forms contradict). Stay within the grammar point of the explanation's 핵심 규칙. Overgeneralizations already caught in this project (do not repeat): '3인칭 단수 → 동사 + s/es' without 'have → has'; 'y → ies' without limiting it to 자음 + y (play → plays); 'be동사 + ing형이면 진행형' (My hobby is reading. is a gerund complement); 'be동사와 일반동사를 함께 쓰지 않는다' (progressive/passive) — say 'be동사와 동사원형을 나란히 쓰지 않는다'; calling is clean / is read / is run impossible forms (adjective, passive) — give the item-specific reason instead (e.g. 주어 We에는 is를 쓰지 않아요); '장소/때/이유 선행사 → where/when/why' without '뒤 절이 완전할 때' (the place which I visited).
- Standalone and complete: every video fully teaches the rule (form + meaning/use + one typical example with its Korean meaning), even though the six videos share a rule. Never mention other videos or items, "같은 원리", "오늘", "이번 시간", "원문항", "변형".
- intro: one sentence starting "이 문제는", stating what the item tests and the task (e.g. "이 문제는 주어 We 뒤에 오는 일반동사의 알맞은 형태를 고르는 문제예요."). Not a lesson opener.
- problem_narration: read the stem; read the sentence(s) aloud if short (빈칸 → "빈칸"; for a long passage say "지문을 읽어 보세요" instead); end with "먼저 풀어 보세요. 영상을 잠시 멈춰도 좋아요." Do not read the options.
- rule.card: 3–5 short board lines; last line "예) …" with an example sentence that is NOT the completed sentence of any of the six items A~F (no spoilers).
- steps: 2–4 steps following the item's real reasoning. highlight/strike are fragments copied exactly from the scene-2 board text (stem, passage, option lines like "② running"); use numbered option fragments ("⑤ run") when a word also occurs inside another option. Step narrations start with 첫째, / 둘째, / 셋째, / 넷째,.
- check.lines: exactly five lines in option order: "① <option text>  ✗  <short reason>" and "N <option text>  ✓  <short reason>" (two spaces around the mark), each reason specific to that option. check.narration: state the answer, then explain the 2–3 distractors a student would most plausibly choose (count/combination items: walk through the per-sentence judgments instead).
- summary: card = the rule in one board line; narration "정답은 N번이에요. 기억할 것, …".
- Narration (TTS): spoken polite Korean (~해요/~예요), short sentences, grade-${g(k)} vocabulary. English stays English (the voice reads it) and each English sentence is followed once by its Korean meaning. Never put ①-⑤, ⓐ-ⓔ, <u>, →, ______, -ing, -s, /, +, ~ in narration (say 1번, 에이 문장, 밑줄 친, 따라서, 빈칸, ing형, s형, 그리고/또는). ⓔ is read 이 문장, which can sound like 'this sentence', so always follow it at once with that sentence's English words (e.g. '이 문장 We will eat은 …'). Korean particles after English words follow pronunciation ("run이에요", "We는", "book을", "play를").
- sec: within the spec ranges (8–12 / 12–20 / 18–30 / 30–45 / 20–35 / 8–12), total 95–150; longer items get longer scenes. Scene 1 reads the heading plus the intro, so it needs about 10 seconds.
Then run: python3 tools/video/apply_fill.py ${k} — it writes 결과/영상대본/${g(k)}급/${k}-<T>.json and .md and prints ERR/WARN. Fix the fill until ERR is 0; address WARNs where reasonable. Do not edit any other file.

Return review (six entries, one per type A~F) and short notes (uncertainties, 정답의심, simplifications you scoped).`

const verifierPrompt = (k, w) => `You are the independent second checker for TOEG item number ${k} (grade ${g(k)}급 = ${LEVEL[g(k)]}). Another teacher reviewed the six explanations (A~F) and wrote six standalone chalkboard video scripts. Your job is to catch real mistakes, not to restyle.
Project root: ${P}. Read src/video/SCRIPT_SPEC.md, src/expl_review/EXPL_RULES.md, work/video/in/${k}.json (items, current explanations), the six scripts 결과/영상대본/${g(k)}급/${k}-A.md … ${k}-F.md, and the fill work/video/fill/${k}.json that generates them.

PART 1 — explanation review. The first reviewer's findings are below. For each type: solve the item yourself; try to REFUTE each issue and keep only real ones; check the proposed explanation line by line (every claim matches the option text, answer = current key, 5-part format and notation, grade-level wording, specific distractor reasons); amend it, or clear it ("") if nothing should change; add any real issue the reviewer missed. Decide final_verdict.

PART 2 — scripts. For each of the six scripts check: (a) correctness — every grammar statement true for this item AND true of English in general (flag overgeneralizations that progressive/passive/inverted/other common forms contradict); every step and option reason matches the actual option text; answer number right; (b) completeness — the video alone teaches the rule (form + use + an example with Korean meaning) and its steps really lead to the answer; no reference to other videos/items/"오늘"/"같은 원리"; the rule-card example is not the completed sentence of any of the six items; (c) the intro sentence accurately states what the item tests; (d) narration is natural spoken Korean for grade ${g(k)}, symbols spoken (no ①, ⓐ, <u>, →, -ing, /, +), correct particles after English words, English sentences followed by their Korean meaning; (e) highlight/strike fragments mark the right words. Fix problems by editing work/video/fill/${k}.json and re-running python3 tools/video/apply_fill.py ${k} until ERR is 0. Do not edit any other file.

First reviewer's findings:
${JSON.stringify(w.review)}
Reviewer notes: ${w.notes}

Return review (six entries: type, final_verdict, issues, proposed, verifier_note), script_fixes (one line per change), remaining (problems you could not resolve).`

const KEYS = args.keys || Array.from({ length: args.n }, (_, i) => `${args.grade}-${i + 1}`).filter(k => !(args.exclude || []).includes(k))
log(`grade ${args.grade || ''}: ${KEYS.length} numbers`)
const res = await pipeline(KEYS,
  k => agent(writerPrompt(k), { label: `write:${k}`, phase: 'Write', schema: WRITE }),
  (w, k) => w ? agent(verifierPrompt(k, w), { label: `verify:${k}`, phase: 'Verify', schema: VERIFY }).then(v => ({ key: k, write: w, verify: v })) : null)
const ok = res.filter(Boolean)
log(`numbers ${ok.length}/${KEYS.length} written, ${ok.filter(r => r.verify).length} verified`)
return ok