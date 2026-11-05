export const meta = {
  name: 'toeg-pretest-80',
  description: 'Write 80 TOEG pretest items (new format, same grammar point) with blind-solve and quality review loops',
  phases: [
    { title: 'Write', detail: 'one writer per batch; self-check with check.py' },
    { title: 'Verify', detail: 'blind solver + rules critic per batch' },
    { title: 'Revise', detail: 'fix flagged items, re-verify (max 2 rounds)' },
  ],
}

const P = args.dir
const RULES = `${P}/RULES.md`
const CHECK = `${P}/tools/check.py`
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
    key: { type: 'string' },
    ref_format: { type: 'string' },
    new_format: { type: 'string' },
    design: { type: 'string' },
    stem: { type: 'string' },
    passage: { type: 'string' },
    c: { type: 'array', items: { type: 'string' }, minItems: 5, maxItems: 5 },
    ans: { type: 'integer', minimum: 1, maximum: 5 },
    expl: { type: 'string' },
  },
  required: ['key', 'ref_format', 'new_format', 'design', 'stem', 'passage', 'c', 'ans', 'expl'],
}
const GEN = { type: 'object', properties: { items: { type: 'array', items: ITEM }, check_output: { type: 'string', description: 'last output of check.py' } }, required: ['items', 'check_output'] }
const SOLVE = {
  type: 'object',
  properties: { results: { type: 'array', items: { type: 'object', properties: {
    key: { type: 'string' },
    solved: { type: 'integer', description: 'option you find correct (1-5); 0 if none or more than one is defensible' },
    other_defensible: { type: 'array', items: { type: 'integer' }, description: 'other options a careful teacher could defend as correct' },
    confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
    english_issues: { type: 'array', items: { type: 'string' }, description: 'unnatural or wrong English in sentences meant to be correct, or errors other than the tested one' },
    notes: { type: 'string' },
  }, required: ['key', 'solved', 'other_defensible', 'confidence', 'english_issues', 'notes'] } } },
  required: ['results'],
}
const CRIT = {
  type: 'object',
  properties: { results: { type: 'array', items: { type: 'object', properties: {
    key: { type: 'string' },
    verdict: { type: 'string', enum: ['ok', 'fix'] },
    issues: { type: 'array', items: { type: 'object', properties: {
      severity: { type: 'string', enum: ['critical', 'major', 'minor'] },
      rule: { type: 'string' }, problem: { type: 'string' }, suggestion: { type: 'string' } },
      required: ['severity', 'rule', 'problem', 'suggestion'] } },
  }, required: ['key', 'verdict', 'issues'] } } },
  required: ['results'],
}

const CIRC = ['①', '②', '③', '④', '⑤']
const blindFmt = (it) => `[${it.key}]\n발문: ${it.stem}\n${it.passage ? '지문:\n' + it.passage + '\n' : ''}보기:\n` + it.c.map((x, i) => `${CIRC[i]} ${x}`).join('\n')
const fullFmt = (it) => `${blindFmt(it)}\n정답: ${CIRC[it.ans - 1]}\n원문항 형식: ${it.ref_format}\n프리테스트 형식: ${it.new_format}\n출제 의도: ${it.design}\n해설:\n${it.expl}`
const chapterCtx = (g) => Object.keys(args.chapters).filter(x => +x >= g).sort((a, b) => b - a).map(x => `${x}급: ${args.chapters[x].join(' / ')}`).join('\n')

const writerPrompt = (b) => `You are a senior writer of Korean school English-grammar test items. Your output will be reviewed item by item by experienced Korean English teachers, so quality must be excellent.

Task: write one new "프리테스트" item for each reference item in batch ${b.id} (${b.keys.length} items, grade ${b.grade}급).
1. Read the guidelines (Korean) fully and follow every rule: ${RULES}
2. Read the input: ${b.file}. Each entry has the reference item (ref: stem, passage, c, ans, expl), the five existing confirmed variants B~F (same format as the reference — do not reuse their sentences), and target_answer_position.
3. Grade level: ${LEVEL[b.grade]}
   Chapters of this grade and easier grades (scope):
${chapterCtx(b.grade)}
4. For each item: (a) state precisely which grammar rule decides the reference answer; (b) choose a new but similar 5-option format that still makes that same rule decide the answer (vary formats across the batch); (c) write natural sentences at the same level, new vocabulary/characters; (d) solve your own item as a strong student and then as a skeptical teacher, checking every option for a second defensible answer, unintended errors, or surface cues; (e) write the explanation exactly in the required 5-part Korean format.
5. Save the whole batch as a JSON list to ${P}/drafts/${b.id}.json (fields: key, ref_format, new_format, design, stem, passage, c, ans, expl) and run:
   python3 ${CHECK} ${P}/drafts/${b.id}.json ${b.file}
   Fix every ERR and every WARN that is a real problem (length shorter than the reference is an ERR: lengthen the passage/sentences). Re-run until there is no ERR.
6. Return the final items (identical to the saved file) and the last check output. Write files only under ${P}/drafts/. Do not modify anything else.`

const solverPrompt = (b, items) => `You are an independent checker of Korean school English-grammar test items. ${LEVEL[b.grade]}
Solve each item below WITHOUT any answer key. Use standard school grammar as taught in Korea, but judge English naturalness like a careful native-speaker teacher.
For each item: give the option you find correct (solved; 0 if none or more than one option is defensible), list any other option a careful teacher could defend as correct (other_defensible), and list any unnatural/wrong English in sentences that are meant to be correct, or any error in a sentence other than the error the item is clearly testing (english_issues). For count items ("…의 개수"), judge each listed sentence O/X yourself and count. Be precise; report only real problems.

${items.map(blindFmt).join('\n\n')}`

const criticPrompt = (b, items, prior) => `You are the strict reviewer (감수자) of new TOEG "프리테스트" items. Read the guidelines fully: ${RULES}
Input data (reference items + existing B~F variants): ${b.file}. Grade: ${b.grade}급. ${LEVEL[b.grade]}
Scope chapters:
${chapterCtx(b.grade)}

Review every item below against ALL guideline rules: same grammar point as the reference decides the answer; format is different from the reference but similar in kind and difficulty; exactly one correct answer; no surface cues; plausible distractors; scope/level; no reuse of reference/B~F sentences; length not shorter than the reference (you may save the items to ${P}/review/${b.id}_${items.length}_${prior ? 'r' : 'f'}.json as a JSON list and run python3 ${CHECK} <that file> ${b.file}); explanation correct, specific, and in the exact 5-part format; Korean and English natural.
severity: critical = wrong/multiple answer, a supposedly correct sentence is wrong, out-of-scope grammar decides the answer, tests a different grammar point; major = any other guideline violation a teacher would mark 부적합 (same format as reference, shorter than reference, answer cue, reuse, wrong/misleading explanation, unnatural English); minor = polish.
verdict='fix' if any critical or major issue. Do not invent problems.${prior ? `\n\nThese items were revised after earlier review. Earlier issues (confirm each is resolved and look for new problems):\n${prior}` : ''}

${items.map(fullFmt).join('\n\n')}`

const reviserPrompt = (b, items, feedback, round) => `You revise TOEG "프리테스트" items that reviewers flagged. Read the guidelines fully: ${RULES}
Input data (reference + B~F): ${b.file}. Grade ${b.grade}급. ${LEVEL[b.grade]}
Scope chapters:
${chapterCtx(b.grade)}

Below are the flagged items with feedback from (1) a blind solver who did not see the key and (2) a strict reviewer. Fix every real problem. If an item is fundamentally weak, rewrite it (you may change the format, as long as it differs from the reference format and tests the same grammar point). Keep the answer position if possible. Do not reintroduce problems; re-solve each revised item yourself and check every option for a second defensible answer.
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
    else for (const i of c.issues || []) lines.push(`- [${i.severity}] ${i.rule}: ${i.problem} → ${i.suggestion}`)
    const serious = !s || !c || (s.solved !== it.ans) || (s.other_defensible || []).some(x => x !== it.ans) || (s.english_issues || []).length > 0 || c.verdict === 'fix' || (c.issues || []).some(i => i.severity !== 'minor')
    const minorOnly = !serious && (c.issues || []).length > 0
    if (serious || minorOnly) fb[it.key] = { text: lines.join('\n'), serious }
  }
  return fb
}

async function runBatch(b) {
  const gen = await agent(writerPrompt(b), { label: `write:${b.id}`, phase: 'Write', schema: GEN })
  if (!gen) return { id: b.id, items: [], history: [], unresolved: b.keys, error: 'writer failed' }
  let cur = {}
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
    // minor-only items are polished only in the first round
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