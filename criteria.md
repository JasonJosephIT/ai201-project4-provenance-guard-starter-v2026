# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. My own writing is not called AI

Of 10 pieces I wrote myself (at least 4 of them deliberately plain: short
sentences, common words), **at most 1 is labelled high-confidence AI in each of
the three trials**, and **none of the 4 plain pieces is ever labelled
high-confidence AI**.

**Why this target:** A wrong accusation costs the writer far more than a missed
detection costs the site, so I allow almost none. I single out plain writing
because that's where both signals share a blind spot (see `docs/milestone1.md`):
low perplexity and even sentence lengths are how many real people write,
especially in a second language. If the system only spares *fancy* human
writing, it isn't sparing the people most likely to be accused.

---

## 2. Clearly-AI and clearly-human text land far apart, and every label is reachable

Across 3 texts I'm confident are AI-generated and 3 I'm confident are
human-written, the **average combined score of the AI texts is at least 0.30
higher** than the average of the human texts, in every trial. Across those 6
plus 3 borderline texts (lightly edited AI), **each of the three labels —
`human`, `unsure`, `ai` — is returned at least once in every trial**.

**Why this target:** With thresholds 0.35 / 0.75, a gap under 0.30 means the
clear cases can't land in opposite labels even in principle — the signals
wouldn't be telling AI and human apart, just nudging both toward "unsure". And
a label that no input reaches is a gap in the ranges, not a design choice; the
starter's own note warns the 0.5 weighted average can make `human` unreachable
while one signal is weak.

---

## 3. Large submissions are handled at the character limit, never crash

The limit is **20,000 characters** of `text` (after trimming). Sent in all three
trials:

| Input | Expected |
|---|---|
| 19,999 characters of prose | `200`, scored, `truncated: true` |
| 20,001 characters | `413`, `error: "text_too_long"` |
| 250,000 characters (`"word " * 50000`) | `413`, `error: "text_too_long"`, response in **under 2 seconds** |
| 300-word essay (under the 400-token cap) | `200`, `truncated: false` |

**4 of 4 behave as listed in every trial, 0 return a 500**, and every `413` is
written to the audit log as a rejection.

**Why this target:** 20,000 characters is about 3,500 words — longer than any
essay or blog post a writer would reasonably check, so no real user hits it.
Above that, sending text costs only the attacker's bandwidth while the model
costs my CPU; rejecting by length *before* the model runs is what keeps a
250,000-character request from tying up the service. The `truncated` flag
matters because signal one only reads the first 400 tokens (~300 words): a
writer should be told when most of their text wasn't read, rather than the
score silently describing only their opening.

---

## 4. Input that isn't English prose is never labelled AI

The detector was trained on English (GPT-2), so this service only judges
English prose. Of these **10 inputs**, sent in every trial:

- **Wrong type (4):** `text` as a number, `null`, a list, an object →
  **all 4 return `400` `invalid_text`**.
- **Not English prose (6):** a paragraph in Spanish, one in Chinese, one in
  Arabic, a block of Python code, a list of URLs, emoji only →
  **0 of 6 labelled high-confidence `ai`, 0 return a 500.** Each either gets
  `unsure` or a `422` saying the service only reads English prose.

**Why this target:** Both signals measure things that only mean something in
English prose. Code is extremely predictable to a language model, so it would
score as AI; Chinese splits into odd tokens and has no `. ! ?` for my sentence
splitter. A non-English writer getting an "AI" label because the tool can't
read their language is the same false positive as criterion 1, just harder to
appeal. "Unsure" or a clear refusal is honest; "AI" is not.

---

## 5. Every appeal changes status and is recorded

For **10 of 10** appeals against real `content_id`s: the response is `200` with
`status: "under_review"`, and `audit.entries_for(content_id)` shows the
original `decided` entry **unchanged** followed by one new `appeal` entry
carrying the writer's reasoning. For **3 of 3** bad appeals — an unknown
`content_id` (`404`), missing `reasoning` (`400`), and a second appeal on the
same item (`409`) — **no new appeal entry is written**. Holds in all three
trials.

**Why this target:** The appeal is the only thing a wrongly-labelled writer can
do, so it can't be "usually works" — one lost appeal is a person who was
accused and then ignored. 10 of 10, not 9: there's no model in this path, so
there's no randomness to excuse a miss. The bad cases matter as much: an appeal
on a typo'd ID that silently "succeeds" tells the writer they're under review
when nothing was recorded.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
