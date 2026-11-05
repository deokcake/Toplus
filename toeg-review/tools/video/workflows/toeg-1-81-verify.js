export const meta = {
  name: 'toeg-1-81-verify',
  description: 'Independently verify the revised TOEG item 1-81 A (option ② whose → which), its explanation and its video script',
  phases: [{ title: 'Verify', detail: 'one skeptical checker' }],
}
const P = args.root
const OUT = { type: 'object', properties: { item_ok: { type: 'boolean' }, unique_answer: { type: 'boolean' }, expl_issues: { type: 'array', items: { type: 'string' } }, script_issues: { type: 'array', items: { type: 'string' } }, fixed: { type: 'array', items: { type: 'string' } }, notes: { type: 'string' } }, required: ['item_ok', 'unique_answer', 'expl_issues', 'script_issues', 'fixed', 'notes'] }
phase('Verify')
const r = await agent(`You are a skeptical checker for a Korean English-grammar test item that was just revised at the client's request. Grade 1급 = Korean middle school 3 to high school 1. Project root: ${P}.
Item 1-81 A (the reference item): stem "다음 빈칸에 들어갈 말로 가장 알맞은 것을 고르시오.", passage "The Amazon Rainforest is a place ____________ biodiversity thrives.", options ① where ② which ③ when ④ whom ⑤ how, answer ①. Option ② used to be "whose", which was also grammatical ("a place whose biodiversity thrives"); the client asked to replace it with a definitely wrong option and to update the explanation and video script.
1) Solve it yourself. Is exactly one option correct (unique_answer)? Could "which" be defended in any reading? Is every distractor clearly wrong?
2) Check the explanation in page/data/ref.json["1-81"].expl against src/expl_review/EXPL_RULES.md: every claim true for this item and true of English in general (no overgeneralization), specific distractor reasons, grade-level wording. Report problems in expl_issues (Korean). Do not edit the explanation source; just report.
3) Check the video script 결과/영상대본/1급/1-81-A.md (generated from work/video/fill/1-81.json "A" by python3 tools/video/apply_fill.py 1-81; spec src/video/SCRIPT_SPEC.md): correctness and universality of every statement, steps lead to the answer, no mention of whose, symbols spoken, Korean particles after English words, length ≤150 s (apply_fill prints it). If you find a real problem in the script, fix it by editing only the "A" entry of work/video/fill/1-81.json and re-running python3 tools/video/apply_fill.py 1-81 until ERR is 0; list what you changed in fixed. Do not edit any other file.
Return item_ok, unique_answer, expl_issues, script_issues, fixed, notes.`, { label: 'verify:1-81-A', phase: 'Verify', schema: OUT })
return r