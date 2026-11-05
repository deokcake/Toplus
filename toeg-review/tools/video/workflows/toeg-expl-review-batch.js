export const meta = {
  name: 'toeg-expl-review-g',
  description: 'Review TOEG explanations (A + confirmed B~F) batch group: accuracy, specificity, level, consistency; propose fixes; skeptic-verify',
  phases: [{ title: 'Review', detail: 'one reviewer per batch of 5 item numbers' }, { title: 'Verify', detail: 'skeptic re-checks flagged explanations' }],
}
const P = args.dir
const RULES = `${P}/EXPL_RULES.md`
const LEVEL = { 7: '7급 = Korean elementary grade 3-4 (present tense only; subject/possessive pronouns only).', 6: '6급 = Korean elementary grade 4 (regular past only).', 5: '5급 = Korean elementary grade 5-6.', 4: '4급 = Korean elementary grade 6 to middle school 1.', 3: '3급 = Korean middle school 1.', 2: '2급 = Korean middle school 2.', 1: '1급 = Korean middle school 3 to high school 1.' }
const ISSUE = { type: 'object', properties: { kind: { type: 'string', enum: ['정확성', '구체성', '눈높이', '일관성', '표기', '대본', '정답의심'] }, where: { type: 'string' }, detail: { type: 'string' } }, required: ['kind', 'where', 'detail'] }
const RESULT = { type: 'object', properties: { results: { type: 'array', items: { type: 'object', properties: { key: { type: 'string' }, type: { type: 'string', enum: ['A', 'B', 'C', 'D', 'E', 'F'] }, verdict: { type: 'string', enum: ['이상 없음', '보완 권장', '수정 필요'] }, issues: { type: 'array', items: ISSUE }, proposed: { type: 'string' } }, required: ['key', 'type', 'verdict', 'issues', 'proposed'] } } }, required: ['results'] }
const VERIFY = { type: 'object', properties: { results: { type: 'array', items: { type: 'object', properties: { key: { type: 'string' }, type: { type: 'string', enum: ['A', 'B', 'C', 'D', 'E', 'F'] }, final_verdict: { type: 'string', enum: ['이상 없음', '보완 권장', '수정 필요'] }, issues: { type: 'array', items: ISSUE }, proposed: { type: 'string' }, verifier_note: { type: 'string' } }, required: ['key', 'type', 'final_verdict', 'issues', 'proposed', 'verifier_note'] } } }, required: ['results'] }
const reviewPrompt = (b) => `You are a senior reviewer of explanations (해설) for a Korean school English-grammar test bank. Read the review standard first (Korean): ${RULES}
Input: ${P}/in/${b.id}.json — ${b.n} item numbers of grade ${b.g}급 (${b.ch}). ${LEVEL[b.g]} Each number has the reference item A and the confirmed variants B~F (same grammar point, same format). Each item has stem, passage, c (5 options), ans (1-5), expl (the explanation to review) and auto_flags (hints from a script; judge them yourself — some are noisy).
Task: review EVERY one of the ${b.n * 6} explanations against the standard, in this order: accuracy (check every claim against the actual option text; solve the item yourself first), specificity of distractor reasons, student level (baseline = vocabulary of the grade's A explanations), consistency across A~F of the same number, format/notation, suitability as a spoken video script.
For each explanation return key, type, verdict (이상 없음 / 보완 권장 / 수정 필요), issues (each with kind, where, detail in Korean, concrete: quote the wrong phrase and say what is right), and proposed = the full corrected explanation in the fixed 5-part format (minimal edits; empty string when 이상 없음). Never change the item itself. If you believe the answer key itself is wrong, say so with kind=정답의심 and keep the explanation on the current key.
Be strict about accuracy but do not invent problems; most explanations should pass. Also save your results as JSON to ${P}/out/${b.id}_review.json (same structure as your return).`
const verifyPrompt = (b, flagged) => `You are a skeptical second reviewer. Standard: ${RULES}. Items: ${P}/in/${b.id}.json (grade ${b.g}급, ${LEVEL[b.g]}).
A first reviewer flagged the explanations below (key/type → verdict, issues, proposed replacement). For each flagged explanation: (1) re-read the actual item and its current explanation; (2) try to REFUTE each issue — keep only issues that are really wrong or really worth improving under the standard; (3) check the proposed explanation line by line: every claim matches the option text, the answer is the current key, format and notation follow the standard, grade-level wording, and distractor reasons are specific; amend the proposal if needed (minimal edits), or clear it if nothing should change; (4) decide final_verdict (downgrade to 이상 없음 when the flags were not justified). Return one result per flagged explanation, with a short verifier_note. Also save your results as JSON to ${P}/out/${b.id}_final.json.

Flagged:
${JSON.stringify(flagged)}`
async function runBatch(b) {
  const rev = await agent(reviewPrompt(b), { label: `review:${b.id}`, phase: 'Review', schema: RESULT })
  if (!rev) return { id: b.id, error: 'reviewer failed', results: [] }
  const flagged = rev.results.filter(r => r.verdict !== '이상 없음')
  let fin = []
  if (flagged.length) { const v = await agent(verifyPrompt(b, flagged), { label: `verify:${b.id}`, phase: 'Verify', schema: VERIFY }); fin = (v && v.results) || [] }
  const F = {}; for (const r of fin) F[r.key + '|' + r.type] = r
  const merged = rev.results.map(r => { const f = F[r.key + '|' + r.type]; return f ? { key: r.key, type: r.type, verdict: f.final_verdict, issues: f.issues, proposed: f.proposed, note: f.verifier_note, first: r.verdict } : { key: r.key, type: r.type, verdict: r.verdict, issues: r.issues, proposed: r.proposed, note: '', first: r.verdict } })
  return { id: b.id, results: merged, flagged: flagged.length, verified: fin.length }
}
const out = await pipeline(args.batches, b => runBatch(b))
const ok = out.filter(Boolean)
log(`batches ${ok.length}/${args.batches.length}, 수정 필요 ${ok.reduce((s, r) => s + r.results.filter(x => x.verdict === '수정 필요').length, 0)}, 보완 권장 ${ok.reduce((s, r) => s + r.results.filter(x => x.verdict === '보완 권장').length, 0)}`)
return ok