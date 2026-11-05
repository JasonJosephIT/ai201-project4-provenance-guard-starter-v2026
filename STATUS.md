---
status: active
progress: 55%
next_date: 2026-11-05
updated: 2026-11-04
---

# Provenance Guard — status

## Now
- Unit 8 Milestone 1 done: rate limiting on, flood shows 5×200 then 10×429, README Rate Limiting filled.
- Unit 7 committed to the fork (5 commits, main at 6730618).
- Milestones 3–5 built and tested live: `/submit` (both signals, combined score, labels, validation), `/appeal`, `stylometry.py`, `combine_signals`. README sections What This Does, Signals and Scoring, Label Variants and Sample Run are filled.

## Next
- Submit fork URL for unit 7: https://github.com/JasonJosephIT/ai201-project4-provenance-guard-starter-v2026
- Clone the fork (`git clone` in a normal terminal) and work from the clone from now on.
- Fill `scenarios.py` with inputs for criteria 1–5 (own writing first).

## Decisions
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
