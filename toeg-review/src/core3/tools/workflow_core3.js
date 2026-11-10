export const meta = {
  name: 'toeg-core3',
  description: 'For each TOEG reference item ending in 1 or 2, write 3 core-check variants at the same difficulty (no explanations), blind-solve + strict review, revise up to 2 rounds',
  phases: [
    { title: 'Write', detail: 'one writer per batch of ≤5 numbers (3 variants each); check3.py self-check' },
    { title: 'Verify', detail: 'blind solver + difficulty/rules critic per batch' },
    { title: 'Revise', detail: 'fix flagged variants, re-verify (max 2 rounds)' },
  ],
}

const P = args.dir
const RULES = `${P}/RULES3.md`
const CHECK = `${P}/tools/check3.py`
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
    key: { type: 'string' }, variant: { type: 'integer', minimum: 1, maximum: 3 },
    ref_format: { type: 'string' }, new_format: { type: 'string' }, design: { type: 'string' },
    stem: { type: 'string' }, passage: { type: 'string' },
    c: { type: 'array', items: { type: 'string' }, minItems: 5, maxItems: 5 },
    ans: { type: 'integer', minimum: 1, maximum: 5 },
  },
  required: ['key', 'variant', 'ref_format', 'new_format', 'design', 'stem', 'passage', 'c', 'ans'],
}
const GEN = { type: 'object', properties: { items: { type: 'array', items: ITEM }, check_output: { type: 'string' } }, required: ['items', 'check_output'] }
const SOLVE = { type: 'object', properties: { results: { type: 'array', items: { type: 'object', properties: {
  id: { type: 'string' }, solved: { type: 'integer' }, other_defensible: { type: 'array', items: { type: 'integer' } },
  confidence: { type: 'string', enum: ['high', 'medium', 'low'] }, english_issues: { type: 'array', items: { type: 'string' } }, notes: { type: 'string' } },
  required: ['id', 'solved', 'other_defensible', 'confidence', 'english_issues', 'notes'] } } }, required: ['results'] }
const CRIT = { type: 'object', properties: { results: { type: 'array', items: { type: 'object', properties: {
  id: { type: 'string' },
  difficulty_vs_reference: { type: 'string', enum: ['harder', 'same', 'easier'] },
  difficulty_reason: { type: 'string' },
  verdict: { type: 'string', enum: ['ok', 'fix'] },
  issues: { type: 'array', items: { type: 'object', properties: {
    severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, rule: { type: 'string' }, problem: { type: 'string' }, suggestion: { type: 'string' } },
    required: ['severity', 'rule', 'problem', 'suggestion'] } } },
  required: ['id', 'difficulty_vs_reference', 'difficulty_reason', 'verdict', 'issues'] } } }, required: ['results'] }

const CIRC = ['①', '②', '③', '④', '⑤']
const idOf = (it) => `${it.key}#${it.variant}`
const blindFmt = (it) => `[${idOf(it)}]\n발문: ${it.stem}\n${it.passage ? '지문:\n' + it.passage + '\n' : ''}보기:\n` + it.c.map((x, i) => `${CIRC[i]} ${x}`).join('\n')
const fullFmt = (it) => `${blindFmt(it)}\n정답: ${CIRC[it.ans - 1]}\n원문항 형식: ${it.ref_format}\n이 변형의 형식: ${it.new_format}\n출제 의도: ${it.design}`
const chapterCtx = (g) => Object.keys(args.chapters).filter(x => +x >= g).sort((a, b) => b - a).map(x => `${x}급: ${args.chapters[x].join(' / ')}`).join('\n')

const writerPrompt = (b) => `You are a senior writer of Korean school English-grammar test items (TOEG). Teachers review every item.

Task: for each of the ${b.keys.length} reference items in batch ${b.id} (grade ${b.grade}급), write THREE new "핵심 확인" variants (variant 1, 2, 3). Each variant must test exactly the same core grammar rule as the reference, at the SAME difficulty, in a sideways format that differs from the reference and from the other two variants. No explanations in this stage.
1. Read the guidelines fully (Korean): ${RULES}  Section "1. 난이도 맞추기" first: same number of judgments as the reference, no heavy formats (combination, counting, 3-blank pairs, tables/long passages) unless the reference uses them, reading load 1.0x–1.3x of the reference (max 1.5x; +8 words for very short references), vocabulary/sentence complexity and traps no higher than the reference.
2. Read the input: ${b.file}. Each entry has the reference item (ref, with its explanation — the 핵심 규칙 line names the rule to test), confirmed variants B~F and, for some numbers, an existing pretest item (existing_pretest) — do NOT reuse any of their sentences, option sets or answer sentences — and target_answer_positions (three recommended answer positions, one per variant).
3. Grade level: ${LEVEL[b.grade]}
   Scope chapters (use only grammar from this grade's chapters up to the reference's chapter and from easier grades):
${chapterCtx(b.grade)}
4. For each reference: (a) state the rule that decides the reference answer and what a student does to solve it (judgments, reading); (b) choose THREE different sideways formats of the same load (opposite direction, word options ↔ very short sentence options, blank ↔ correct the underlined part, statement ↔ short dialogue, transformation ↔ Korean-to-English, explanation ↔ short application options …); the three stems must differ from each other and from the reference stem; (c) write short, natural sentences at the reference's level with new characters and topics; (d) make sure the core rule alone decides the answer — a student who knows that rule answers correctly, one who does not cannot, and no other knowledge is needed; (e) solve each yourself: exactly one answer, distractors from real student errors, no surface cues (length, form, position), wrong sentences wrong in exactly one place; (f) compare difficulty honestly with the reference and simplify if harder.
   design must say how difficulty was matched (판단 개수·읽을 양·어휘 수준) and what the distractors are.
5. Save the batch as a JSON list (${b.keys.length * 3} items, fields: key, variant, ref_format, new_format, design, stem, passage, c, ans) to ${P}/drafts/${b.id}.json and run:
   python3 ${CHECK} ${P}/drafts/${b.id}.json ${b.file}
   Fix every ERR (shorter/longer than allowed, heavy format, same stem as the reference or a sibling, reused sentences or option sets) and real WARNs. Re-run until there is no ERR.
6. Return the final items (identical to the saved file) and the last check output. Write files only under ${P}/drafts/.`

const solverPrompt = (b, items) => `You are an independent checker of Korean school English-grammar test items. ${LEVEL[b.grade]}
Solve each item below WITHOUT any answer key, as a careful teacher. For each: the option you find correct (solved; 0 if none or more than one is defensible), other options a careful teacher could defend (other_defensible), and unnatural/wrong English in sentences meant to be correct or any error other than the one being tested (english_issues). Use the id in brackets as id. Report only real problems.

${items.map(blindFmt).join('\n\n')}`

const criticPrompt = (b, items, prior) => `You are the strict reviewer (감수자) of TOEG "핵심 확인" variant items. Read the guidelines fully, especially "0. 무엇을 만드나" and "1. 난이도 맞추기": ${RULES}
Input data (reference items with explanations, B~F, existing pretest items): ${b.file}. Grade ${b.grade}급. ${LEVEL[b.grade]}
Scope chapters:
${chapterCtx(b.grade)}

For every variant below (id = 번호#변형):
- difficulty_vs_reference: compare with the reference item on (1) number of judgments, (2) amount of English to read, (3) vocabulary and sentence complexity, (4) reasoning steps, (5) number and subtlety of traps. 'harder' if a student who can solve the reference would need noticeably more effort; 'easier' if the answer has become obvious.
- Core check: the same rule as the reference's 핵심 규칙 must be the only thing that decides the answer; nothing else (other grammar, vocabulary, world knowledge) may be needed, and the rule must not be given away by the stem or passage.
- The three variants of one number must use three different formats (different stems), none identical to the reference/B~F format, each still a 5-option multiple-choice of the same kind and weight.
- Then all other rules: exactly one correct answer; correct sentences fully natural; wrong sentences wrong in exactly one place; no surface cues; scope/level; no reuse of reference/B~F/pretest/sibling sentences or option sets; length not shorter than the reference and within the upper bound; underline range matches what the options replace. You may save the items to ${P}/review/${b.id}_${items.length}_${prior ? 'r' : 'f'}.json and run python3 ${CHECK} <that file> ${b.file} (check3 compares siblings only when they are in the same file).
severity: critical = wrong/multiple answer, a supposedly correct sentence is wrong, different grammar point, out-of-scope grammar decides the answer; major = harder than the reference, same format as the reference or a sibling, too short/long, heavy format, answer cue, reuse, unnatural English, anything a teacher would mark 부적합; minor = polish, or slightly easier than the reference.
verdict='fix' if any critical or major issue. Do not invent problems.${prior ? `\n\nThese items were revised after earlier review. Earlier issues (confirm each is resolved and look for new problems):\n${prior}` : ''}

${items.map(fullFmt).join('\n\n')}`

const reviserPrompt = (b, items, feedback, round) => `You revise TOEG "핵심 확인" variant items that reviewers flagged. Read the guidelines fully (sections 0 and 1 first): ${RULES}
Input data (reference with explanation, B~F, pretest): ${b.file}. Grade ${b.grade}급. ${LEVEL[b.grade]}
Scope chapters:
${chapterCtx(b.grade)}

Below are the flagged variants with feedback from a blind solver and a strict reviewer. Fix every real problem; if a variant is harder than its reference, simplify it (fewer judgments, shorter sentences, lighter format) while keeping the same core rule and a stem different from the reference and from its two sibling variants (the siblings' current stems are listed under each item). Keep the answer position if possible. Re-solve each revised item yourself.
Save the revised items as a JSON list to ${P}/drafts/${b.id}_rev${round}.json and run python3 ${CHECK} ${P}/drafts/${b.id}_rev${round}.json ${b.file}; fix all ERR (sibling-stem ERRs apply only among items in that file — also make sure your stems differ from the sibling stems listed below). Return ONLY the revised items (all fields) and the last check output.

${items.map(it => fullFmt(it) + '\n[같은 번호의 다른 변형 발문]\n' + feedback[idOf(it)].siblings + '\n[피드백]\n' + feedback[idOf(it)].text).join('\n\n----\n\n')}`

function flagsFor(items, solve, crit) {
  const S = {}, C = {}
  for (const r of (solve && solve.results) || []) S[r.id] = r
  for (const r of (crit && crit.results) || []) C[r.id] = r
  const fb = {}
  for (const it of items) {
    const id = idOf(it); const s = S[id], c = C[id]
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
    if (serious || minorOnly) fb[id] = { text: lines.join('\n'), serious }
  }
  return fb
}

async function runBatch(b) {
  const gen = await agent(writerPrompt(b), { label: `write:${b.id}`, phase: 'Write', schema: GEN })
  if (!gen) return { id: b.id, items: [], history: [], unresolved: b.keys.flatMap(k => [1, 2, 3].map(v => `${k}#${v}`)), error: 'writer failed' }
  const cur = {}
  for (const it of gen.items) cur[idOf(it)] = it
  const order = b.keys.flatMap(k => [1, 2, 3].map(v => `${k}#${v}`)).filter(id => cur[id])
  const history = []
  let toCheck = order.map(id => cur[id]); let prior = ''
  for (let round = 0; round <= 2; round++) {
    const [solve, crit] = await parallel([
      () => agent(solverPrompt(b, toCheck), { label: `solve:${b.id}:${round}`, phase: 'Verify', schema: SOLVE }),
      () => agent(criticPrompt(b, toCheck, prior), { label: `review:${b.id}:${round}`, phase: 'Verify', schema: CRIT }),
    ])
    const fb = flagsFor(toCheck, solve, crit)
    history.push({ round, checked: toCheck.map(idOf), solve: (solve && solve.results) || [], critic: (crit && crit.results) || [], flagged: Object.keys(fb).map(id => ({ id, serious: fb[id].serious, feedback: fb[id].text })) })
    const flagged = Object.keys(fb)
    if (!flagged.length || round === 2) break
    const targets = flagged.filter(id => fb[id].serious || round === 0)
    if (!targets.length) break
    const feedback = {}
    for (const id of targets) {
      const it = cur[id]
      const sibs = order.filter(o => o !== id && cur[o].key === it.key).map(o => `변형 ${cur[o].variant}: ${cur[o].stem}`).join('\n')
      feedback[id] = { text: fb[id].text, siblings: sibs }
    }
    const rev = await agent(reviserPrompt(b, targets.map(id => cur[id]), feedback, round + 1), { label: `revise:${b.id}:${round + 1}`, phase: 'Revise', schema: GEN })
    if (!rev) break
    const changed = []
    for (const it of rev.items) { const id = idOf(it); if (cur[id]) { cur[id] = it; changed.push(id) } }
    if (!changed.length) break
    toCheck = changed.map(id => cur[id])
    prior = changed.map(id => `[${id}]\n${feedback[id] ? feedback[id].text : ''}`).join('\n')
  }
  const last = history[history.length - 1]
  const unresolved = last ? last.flagged.filter(f => f.serious).map(f => f.id) : []
  return { id: b.id, items: order.map(id => cur[id]), history, unresolved }
}

const results = await pipeline(args.batches, b => runBatch(b))
const ok = results.filter(Boolean)
log(`done: ${ok.length}/${args.batches.length} batches, ${ok.reduce((s, r) => s + r.items.length, 0)} items, unresolved ${ok.reduce((s, r) => s + r.unresolved.length, 0)}`)
return ok