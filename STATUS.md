---
status: active
progress: 45%
next_date: 2026-11-05
updated: 2026-11-04
---

# Provenance Guard — status

## Now
- Milestones 3–5 built and tested live: `/submit` (both signals, combined score, labels, validation), `/appeal`, `stylometry.py`, `combine_signals`. README sections What This Does, Signals and Scoring, Label Variants and Sample Run are filled.

## Next
- `git init` and commit (the checklist needs 4+ commits).
- Fill README "How I Used AI" (2 moments).
- Fill `scenarios.py` with inputs for criteria 1–5 (own writing first).

## Decisions
- 2026-11-04: Combining rule is a 0.5/0.5 average; if the signals are more than 0.30 apart, the score is capped below the AI line. AI_THRESHOLD is 0.88 (supersedes the proposed 0.75): plain human writing scored 0.847. HUMAN_THRESHOLD stays 0.35.
- 2026-11-04: Style signal = 0.6 sentence-length spread + 0.4 expressive punctuation. TTR is weighted 0 because it ran backwards on the calibration set.
- 2026-11-04: criteria.md written. Text limit is 20,000 chars (longer gets a 413 before the model runs), and only English prose is judged (other input is never labelled `ai`).
- 2026-11-04 (proposed, pending review): raise `AI_THRESHOLD` to 0.75; label `ai` only when both signals ≥ 0.6.
- 2026-11-04 (proposed): `confidence = abs(combined − 0.5) × 2`; `/submit` text 40–20,000 chars; second appeal returns 409.

## Open items / waiting on
- `logs/audit.jsonl` holds 19 test entries from today's runs. Clear it before unit 8 attack runs.
- The language check misses code and Spanish; both get scored.
- Nobody reads `under_review` appeals yet. This is a known gap.
- The repo is not a git repository yet, and the README checklist requires commits.

## Idea Shelf
