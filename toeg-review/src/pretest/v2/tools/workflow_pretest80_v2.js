export const meta = {
  name: 'toeg-pretest-80-v2',
  description: 'Rewrite TOEG pretest items to match reference difficulty, with blind-solve and difficulty/rules review loops',
  phases: [
    { title: 'Write', detail: 'one writer per batch; check2.py self-check' },
    { title: 'Verify', detail: 'blind solver + difficulty/rules critic per batch' },
    { title: 'Revise', detail: 'fix flagged items, re-verify (max 2 rounds)' },
  ],
}

const P = args.dir
const RULES = `${P}/RULES2.md`
const CHECK = `${P}/tools/check2.py`
const LEVEL = {
  7: '7급 = Korean elementary grade 3-4. Present tense only; pronouns: subject and possessive only (no object pronouns); no to-infinitive, no -ing; no month names; regular plurals preferred.',
  6: '6급 = Korean elementary grade 4. Regular past forms only (no irregular past like bought/went); simple vocabulary.',
  5: '5급 = Korean elementary grade 5-6.',
  4: '4급 = Korean elementary grade 6 to middle school grade 1.',
  3: '3급 = Korean middle school grade 1.',
  2: '2급 = Korean middle school grade 2.',
  1: '1급 = Korean middle school grade 3 to high school grade 1.',
}
const ITEM = {
  type: 'object',
  properties: {
    key: { type: 'string' }, ref_format: { type: 'string' }, new_format: { type: 'string' }, design: { type: 'string' },
    stem: { type: 'string' }, passage: { type: 'string' },
    c: { type: 'array', items: { type: 'string' }, minItems: 5, maxItems: 5 },
    ans: { type: 'integer', minimum: 1, maximum: 5 }, expl: { type: 'string' },
  },
  required: ['key', 'ref_format', 'new_format', 'design', 'stem', 'passage', 'c', 'ans', 'expl'],
}
const GEN = { type: 'object', properties: { items: { type: 'array', items: ITEM }, check_output: { type: 'string' } }, required: ['items', 'check_output'] }
const SOLVE = { type: 'object', properties: { results: { type: 'array', items: { type: 'object', properties: {
  key: { type: 'string' }, solved: { type: 'integer' }, other_defensible: { type: 'array', items: { type: 'integer' } },
  confidence: { type: 'string', enum: ['high', 'medium', 'low'] }, english_issues: { type: 'array', items: { type: 'string' } }, notes: { type: 'string' } },
  required: ['key', 'solved', 'other_defensible', 'confidence', 'english_issues', 'notes'] } } }, required: ['results'] }
const CRIT = { type: 'object', properties: { results: { type: 'array', items: { type: 'object', properties: {
  key: { type: 'string' },
  difficulty_vs_reference: { type: 'string', enum: ['harder', 'same', 'easier'] },
  difficulty_reason: { type: 'string' },
  verdict: { type: 'string', enum: ['ok', 'fix'] },
  issues: { type: 'array', items: { type: 'object', properties: {
    severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, rule: { type: 'string' }, problem: { type: 'string' }, suggestion: { type: 'string' } },
    required: ['severity', 'rule', 'problem', 'suggestion'] } } },
  required: ['key', 'difficulty_vs_reference', 'difficulty_reason', 'verdict', 'issues'] } } }, required: ['results'] }

const CIRC = ['①', '②', '③', '④', '⑤']
const blindFmt = (it) => `[${it.key}]\n발문: ${it.stem}\n${it.passage ? '지문:\n' + it.passage + '\n' : ''}보기:\n` + it.c.map((x, i) => `${CIRC[i]} ${x}`).join('\n')
const fullFmt = (it) => `${blindFmt(it)}\n정답: ${CIRC[it.ans - 1]}\n원문항 형식: ${it.ref_format}\n프리테스트 형식: ${it.new_format}\n출제 의도: ${it.design}\n해설:\n${it.expl}`
const chapterCtx = (g) => Object.keys(args.chapters).filter(x => +x >= g).sort((a, b) => b - a).map(x => `${x}급: ${args.chapters[x].join(' / ')}`).join('\n')

const writerPrompt = (b) => `You are a senior writer of Korean school English-grammar test items. Teachers review every item.

Task (second edition): the first-edition "프리테스트" items were judged TOO HARD compared with their reference items (reviewer memos: "문제의 질은 좋지만 다소 어려움", "기준문항에 비해 난이도가 높음"). Rewrite the ${b.keys.length} items of batch ${b.id} (grade ${b.grade}급) so that each matches the DIFFICULTY of its reference item, while still testing the same grammar point in a slightly different (sideways) format.
1. Read the guidelines fully (Korean). Section "0. 난이도 맞추기" comes first: same number of judgments as the reference, no heavy formats (combination "모두 고른 것", counting "개수", 3-blank pairs, tables/long passages) unless the reference already uses that format, reading load between 1.0x and about 1.3x of the reference (max 1.5x, or +8 words for very short references), vocabulary/sentence complexity and number of traps no higher than the reference. ${RULES}
2. Read the input: ${b.file}. Each entry has the reference item (ref), confirmed variants B~F (do not reuse their sentences), target_answer_position, the first-edition item (v1_pretest), the automatic list of why v1 was too hard (v1_difficulty_problems), and for some items the reviewer's memo (reviewer_memo_on_v1).
3. Grade level: ${LEVEL[b.grade]}
   Scope chapters:
${chapterCtx(b.grade)}
4. For each item: (a) state the grammar rule that decides the reference answer and what a student must do to solve the reference (how many judgments, how much reading); (b) choose a sideways format with the SAME load (ask the opposite direction, word options ↔ very short sentence options, blank ↔ correct the underlined part, statement ↔ short dialogue, transformation ↔ Korean-to-English, etc.); the stem must differ from the reference stem; (c) write short, natural sentences at the reference's level; (d) solve it yourself and confirm exactly one answer and no surface cues; (e) honestly compare: would a student who just answered the reference correctly need about the same time and effort? If harder, simplify. If v1 already fully satisfies section 0 (no length/format problems and same load), you may keep it, but say so in design.
   Write the explanation in the exact required 5-part Korean format. design must say how difficulty was matched (판단 개수·읽을 양·어휘 수준).
5. Save the batch as a JSON list to ${P}/drafts/${b.id}.json (fields: key, ref_format, new_format, design, stem, passage, c, ans, expl) and run:
   python3 ${CHECK} ${P}/drafts/${b.id}.json ${b.file}
   Fix every ERR (shorter than the reference, too long, heavy format) and real WARNs. Re-run until there is no ERR.
6. Return the final items (identical to the saved file) and the last check output. Write files only under ${P}/drafts/.`

const solverPrompt = (b, items) => `You are an independent checker of Korean school English-grammar test items. ${LEVEL[b.grade]}
Solve each item below WITHOUT any answer key, as a careful teacher. For each: the option you find correct (solved; 0 if none or more than one is defensible), other options a careful teacher could defend (other_defensible), and unnatural/wrong English in sentences meant to be correct or any error other than the one being tested (english_issues). Report only real problems.

${items.map(blindFmt).join('\n\n')}`

const criticPrompt = (b, items, prior) => `You are the strict reviewer (감수자) of TOEG "프리테스트" items, second edition. The first edition was rejected as too hard; this edition must match the DIFFICULTY of each reference item. Read the guidelines fully, especially section "0. 난이도 맞추기": ${RULES}
Input data (reference items, B~F, first-edition items): ${b.file}. Grade ${b.grade}급. ${LEVEL[b.grade]}
Scope chapters:
${chapterCtx(b.grade)}

For every item below:
- difficulty_vs_reference: compare with the reference item on (1) number of judgments a student must make, (2) amount of English to read, (3) vocabulary and sentence complexity, (4) reasoning steps (combination/counting/multi-blank), (5) number and subtlety of traps. 'harder' if a student who can solve the reference would need noticeably more effort; 'easier' if the answer has become obvious. Explain briefly in difficulty_reason.
- Then check all other rules: same grammar point decides the answer; stem/format differs from the reference but is similar in kind; exactly one correct answer; no surface cues; scope/level; no reuse of reference/B~F sentences; length not shorter than the reference and within the upper bound (you may save the items as a JSON list to ${P}/review/${b.id}_${items.length}_${prior ? 'r' : 'f'}.json and run python3 ${CHECK} <that file> ${b.file}); explanation correct, specific, exact 5-part format; natural Korean and English.
severity: critical = wrong/multiple answer, a supposedly correct sentence is wrong, different grammar point, out-of-scope grammar decides the answer; major = harder than the reference, or any other violation a teacher would mark 부적합 (same stem/format as reference, too short or too long, heavy format, answer cue, reuse, wrong explanation, unnatural English); minor = polish, or slightly easier than the reference.
verdict='fix' if any critical or major issue. Do not invent problems.${prior ? `\n\nThese items were revised after earlier review. Earlier issues (confirm each is resolved and look for new problems):\n${prior}` : ''}

${items.map(fullFmt).join('\n\n')}`

const reviserPrompt = (b, items, feedback, round) => `You revise TOEG "프리테스트" second-edition items that reviewers flagged. Main goal: match the difficulty of the reference item. Read the guidelines fully (section 0 first): ${RULES}
Input data (reference, B~F, first edition): ${b.file}. Grade ${b.grade}급. ${LEVEL[b.grade]}
Scope chapters:
${chapterCtx(b.grade)}

Below are the flagged items with feedback from a blind solver and a strict reviewer. Fix every real problem; if an item is still harder than its reference, simplify it (fewer judgments, shorter sentences, a lighter format) while keeping the same grammar point and a stem different from the reference. Keep the answer position if possible. Re-solve each revised item yourself.
Save the revised items as a JSON list to ${P}/drafts/${b.id}_rev${round}.json and run python3 ${CHECK} ${P}/drafts/${b.id}_rev${round}.json ${b.file}; fix all ERR. Return ONLY the revised items (all fields) and the last check output.

${items.map(it => fullFmt(it) + '\n[피드백]\n' + feedback[it.key]).join('\n\n----\n\n')}`

function flagsFor(items, solve, crit) {
  const S = {}, C = {}
  for (const r of (solve && solve.results) || []) S[r.key] = r
  for (const r of (crit && crit.results) || []) C[r.key] = r
  const fb = {}
  for (const it of items) {
    const s = S[it.key], c = C[it.key]
    const lines = []
    if (!s) lines.push('- blind solver gave no result (re-check carefully)')
    else {
      if (s.solved !== it.ans) lines.push(`- blind solver chose ${s.solved === 0 ? 'no single answer' : CIRC[s.solved - 1]} (key ${CIRC[it.ans - 1]}): ${s.notes}`)
      if ((s.other_defensible || []).filter(x => x !== it.ans).length) lines.push(`- other defensible options: ${s.other_defensible.map(x => CIRC[x - 1]).join(', ')} — ${s.notes}`)
      for (const e of s.english_issues || []) lines.push(`- English: ${e}`)
    }
    if (!c) lines.push('- reviewer gave no result')
    else {
      if (c.difficulty_vs_reference !== 'same') lines.push(`- difficulty: ${c.difficulty_vs_reference} than the reference — ${c.difficulty_reason}`)
      for (const i of c.issues || []) lines.push(`- [${i.severity}] ${i.rule}: ${i.problem} → ${i.suggestion}`)
    }
    const serious = !s || !c || (s.solved !== it.ans) || (s.other_defensible || []).some(x => x !== it.ans) || (s.english_issues || []).length > 0 || c.verdict === 'fix' || c.difficulty_vs_reference === 'harder' || (c.issues || []).some(i => i.severity !== 'minor')
    const minorOnly = !serious && ((c.issues || []).length > 0 || c.difficulty_vs_reference === 'easier')
    if (serious || minorOnly) fb[it.key] = { text: lines.join('\n'), serious }
  }
  return fb
}

async function runBatch(b) {
  const gen = await agent(writerPrompt(b), { label: `write:${b.id}`, phase: 'Write', schema: GEN })
  if (!gen) return { id: b.id, items: [], history: [], unresolved: b.keys, error: 'writer failed' }
  const cur = {}
  for (const it of gen.items) cur[it.key] = it
  const order = b.keys.filter(k => cur[k])
  const history = []
  let toCheck = order.map(k => cur[k]); let prior = ''
  for (let round = 0; round <= 2; round++) {
    const [solve, crit] = await parallel([
      () => agent(solverPrompt(b, toCheck), { label: `solve:${b.id}:${round}`, phase: 'Verify', schema: SOLVE }),
      () => agent(criticPrompt(b, toCheck, prior), { label: `review:${b.id}:${round}`, phase: 'Verify', schema: CRIT }),
    ])
    const fb = flagsFor(toCheck, solve, crit)
    history.push({ round, checked: toCheck.map(x => x.key), solve: (solve && solve.results) || [], critic: (crit && crit.results) || [], flagged: Object.keys(fb).map(k => ({ key: k, serious: fb[k].serious, feedback: fb[k].text })) })
    const flagged = Object.keys(fb)
    if (!flagged.length || round === 2) break
    const targets = flagged.filter(k => fb[k].serious || round === 0)
    if (!targets.length) break
    const feedback = {}; targets.forEach(k => feedback[k] = fb[k].text)
    const rev = await agent(reviserPrompt(b, targets.map(k => cur[k]), feedback, round + 1), { label: `revise:${b.id}:${round + 1}`, phase: 'Revise', schema: GEN })
    if (!rev) break
    const changed = []
    for (const it of rev.items) if (cur[it.key]) { cur[it.key] = it; changed.push(it.key) }
    if (!changed.length) break
    toCheck = changed.map(k => cur[k])
    prior = changed.map(k => `[${k}]\n${feedback[k] || ''}`).join('\n')
  }
  const last = history[history.length - 1]
  const unresolved = last ? last.flagged.filter(f => f.serious).map(f => f.key) : []
  return { id: b.id, items: order.map(k => cur[k]), history, unresolved }
}

const results = await pipeline(args.batches, b => runBatch(b))
log(`done: ${results.filter(Boolean).map(r => `${r.id} ${r.items.length} items, unresolved ${r.unresolved.length}`).join(' | ')}`)
return results.filter(Boolean)