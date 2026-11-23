---
status: active
progress: 90%
next_date: 2026-11-23
updated: 2026-11-22
---

# Provenance Guard — status

## Now
- 2026-11-23: Unit 8 done locally. README filled: Attack Run Before (56 rows, 10 broke / 46 held / 0 crashes), Run Log Verdicts (C1 met, C2 missed, C3–5 met), Diagnoses, Improvement, Attack Run After, What's Still Broken, 12 audit entries (4 rejected).
- Fix: HUMAN_THRESHOLD 0.35 → 0.38. After: C2 met all 3 trials, attack results identical (56/56 same).
- Evidence files in results/: attack_run_*_before/after.md, run_*_before/after.md, audit_before_full.jsonl.
- Not yet pushed to the fork (no git in this folder; earlier commits went via GitHub API).

## Next
- Check `eval_inputs/own/plain_4.txt` and `plain_nft.txt` against originals (words were filled in by guess).
- Push unit 8 work to the fork: README.md, config.py, scenarios.py, run_eval.py, eval_inputs/, results/, logs/audit.jsonl, STATUS.md.

## Decisions
- 2026-11-23: Third signal (stock-AI-word rate) tested offline and NOT shipped: every cutoff that catches evasions labels own proposal (10.0 AI words/100) `ai`. Written up in README What's Still Broken; evidence in results/third_signal_*.
- 2026-11-23: Unit 8 fix = HUMAN_THRESHOLD 0.35 → 0.38 (criterion 2 label-mapping miss). Evasions left unfixed: lowering AI line would flag FP04 (0.845) and own proposal (0.850).
- 2026-11-22: Criterion 2 "confident human" texts are Project Gutenberg passages (Jerome 1889, Bird 1879, Twain 1883); AI texts written by Claude; borderline = AI drafts lightly hand-edited. Eval inputs live as files in `eval_inputs/`.
- 2026-11-11: Unit 8 scope locked to three additions to the submitted fork, nothing else: (1) run log: 5 criteria x 3 trials, before fix and after fix; (2) verdict + diagnosis: met/missed per criterion and the cause of every miss; (3) audit log: 10+ entries pasted as text, mostly from the attack run, at least one rejected request.
- 2026-11-04: Rate limiting on by default: 5/minute, 50/day, keyed per creator_id (IP fallback). Known gap: rotating creator_id bypasses it. Rejection log entries now carry all nine fields (nulls for scores).
- 2026-11-04: Two Claude entries written with a humanizer skill scored unsure (0.595, 0.423): zero stock AI words, colons read as human punctuation. Accepted as a safe miss; becomes a unit 8 evasion test case.
- 2026-11-04: Stock AI word list extended to 1,075 entries in `ai_words.txt` (loaded by `stylometry.py`). Risk: a human student essay using taught transitions scored 0.850, near the 0.88 AI line.
- 2026-11-04: Added a stock-AI-words measure (`stylometry.AI_WORDS`, `ai_word_rate`) at weight 0.2; style = 0.5 spread + 0.3 punctuation + 0.2 AI words. Plain human now 0.761, generic AI 0.910.
- 2026-11-04: Vocabulary variety (type-token ratio) removed from the style signal and docs. Humans can have a set word choice just as AI can, so it isn't a fair differentiator.
- 2026-11-04: Combining rule is a 0.5/0.5 average; if the signals are more than 0.30 apart, the score is capped below the AI line. AI_THRESHOLD is 0.88 (supersedes the proposed 0.75): plain human writing scored 0.847. HUMAN_THRESHOLD stays 0.35.
- 2026-11-04: Style signal = 0.6 sentence-length spread + 0.4 expressive punctuation. TTR removed entirely (see 2026-11-04 entry above).
- 2026-11-04: criteria.md written. Text limit is 20,000 chars (longer gets a 413 before the model runs), and only English prose is judged (other input is never labelled `ai`).
- 2026-11-04 (proposed, pending review): raise `AI_THRESHOLD` to 0.75; label `ai` only when both signals ≥ 0.6.
- 2026-11-04 (proposed): `confidence = abs(combined − 0.5) × 2`; `/submit` text 40–20,000 chars; second appeal returns 409.

## Open items / waiting on
- `logs/audit.jsonl` holds 19 test entries from today's runs. Clear it before unit 8 attack runs.
- The language check misses code and Spanish; both get scored.
- Nobody reads `under_review` appeals yet. This is a known gap.
- This folder has no git; the 5 unit 7 commits were made on the fork via the GitHub API because git couldn't reach github.com from the agent shell.
- docs/milestone1.html is not committed (no HTML in this repo).

## Idea Shelf
