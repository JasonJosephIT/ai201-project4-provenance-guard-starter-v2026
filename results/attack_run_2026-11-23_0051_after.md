# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-23 00:51
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `f2119029-6eb4-4892-a535-5ed5664f47a4` | unsure | 0.120 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `93326f36-2527-4e85-a697-1ab9804ee0d1` | unsure | 0.206 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `77f165c4-2c1a-4736-bccc-3080afd5fd86` | unsure | 0.106 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `5fde6a0c-acd6-41f4-9036-831692547ccd` | unsure | 0.489 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `5d3d2835-444c-4989-96ea-85e72a797395` | human | 0.366 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `8db9a099-f8af-4a42-b96a-bb62353dea21` | unsure | 0.073 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `bb77f6fb-f2e0-4d4a-b8f5-73bd7c920b05` | unsure | 0.036 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `cb230e9d-863e-4d2b-98e6-efffb98aecdf` | unsure | 0.205 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `00bcf590-f27b-4f02-b32d-bcfd2db3b64f` | unsure | 0.401 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `126eca99-f73d-4b1c-a73d-d523fe8b0377` | ai | 0.818 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `4235e37d-d52b-416e-8ecf-d6c48bd32ec7` | unsure | 0.203 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `4a7a1a40-b238-4f58-a81c-12fc77b66561` | unsure | 0.505 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `319e5704-9d92-431e-8a1c-2dd812a585d2` | unsure | 0.498 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `be84dc82-d2cc-4b8d-8686-c592f26d6ebb` | unsure | 0.690 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `56a3b908-5337-484b-ac1e-7356e86486be` | unsure | 0.536 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `6fd59d18-a1fb-446a-9052-a58984790a69` | unsure | 0.415 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `83e56d7b-76b6-4bb6-8a6c-1dd8ecdc1b5c` | unsure | 0.239 |  |
| FP08 | false_positive | very short genuine human submission | 422 | `—` | — | — |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `8c9bdd68-9324-4c66-a794-61a1d47abe43` | unsure | 0.025 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `caccfe56-e99a-4452-87c4-c5257cad65b8` | human | 0.391 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `b36d7fd9-8cba-41b6-b3c7-03a2696012b3` | unsure | 0.096 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `d414a222-2d4d-41ed-be78-aed348df6912` | unsure | 0.158 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `f884fadb-3fef-4bc1-b1ea-928643ea75ec` | unsure | 0.090 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `d0530e75-da12-4363-a335-d2fa5c31d61e` | unsure | 0.154 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 422 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 422 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 422 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 200 | `c232ae7d-6fbb-4618-809b-1baa61ea9fbc` | unsure | 0.548 |  |
| MF06 | malformed | text is emoji only | 422 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 422 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f21660a5-5183-43b4-8943-c2a2fd1fc80a` | human | 0.421 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4a846b3d-dde0-4672-aa65-c2844091d222` | human | 0.421 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b4c609c0-4c96-4bdf-b2e0-52233959457d` | human | 0.421 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fac281b1-28d5-41af-9ff4-373e458dcff4` | human | 0.421 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a73b5a28-de57-4353-b21d-5bda370ac327` | human | 0.421 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "f2119029-6eb4-4892-a535-5ed5664f47a4",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.1204,
  "model_score": 0.1635,
  "style_score": 0.9569,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "93326f36-2527-4e85-a697-1ab9804ee0d1",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.2064,
  "model_score": 0.5943,
  "style_score": 0.1993,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "77f165c4-2c1a-4736-bccc-3080afd5fd86",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.1062,
  "model_score": 0.6662,
  "style_score": 0.4399,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "5fde6a0c-acd6-41f4-9036-831692547ccd",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.489,
  "model_score": 0.6114,
  "style_score": 0.8775,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "5d3d2835-444c-4989-96ea-85e72a797395",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3664,
  "model_score": 0.3212,
  "style_score": 0.3125,
  "label": "This reads like it was written by a person. Our check found the kind of variety (in sentence length and punctuation) that people's writing usually has.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "8db9a099-f8af-4a42-b96a-bb62353dea21",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.0726,
  "model_score": 0.5727,
  "style_score": 0.5,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "bb77f6fb-f2e0-4d4a-b8f5-73bd7c920b05",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.0362,
  "model_score": 0.5862,
  "style_score": 0.45,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "cb230e9d-863e-4d2b-98e6-efffb98aecdf",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.2048,
  "model_score": 0.2452,
  "style_score": 0.55,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "00bcf590-f27b-4f02-b32d-bcfd2db3b64f",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.4014,
  "model_score": 0.7042,
  "style_score": 0.6972,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "126eca99-f73d-4b1c-a73d-d523fe8b0377",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8176,
  "model_score": 0.9792,
  "style_score": 0.8384,
  "label": "This writing has strong patterns we usually see in AI-generated text. This is an estimate, not proof, and it says nothing about you; people's own writing sometimes looks this way too. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "4235e37d-d52b-416e-8ecf-d6c48bd32ec7",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.203,
  "model_score": 0.6175,
  "style_score": 0.5854,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "4a7a1a40-b238-4f58-a81c-12fc77b66561",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.5052,
  "model_score": 0.7387,
  "style_score": 0.7664,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "319e5704-9d92-431e-8a1c-2dd812a585d2",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.4982,
  "model_score": 0.8051,
  "style_score": 0.6932,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "be84dc82-d2cc-4b8d-8686-c592f26d6ebb",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.69,
  "model_score": 0.8329,
  "style_score": 0.8572,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "56a3b908-5337-484b-ac1e-7356e86486be",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.5364,
  "model_score": 0.8005,
  "style_score": 0.7359,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "6fd59d18-a1fb-446a-9052-a58984790a69",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.4154,
  "model_score": 0.8814,
  "style_score": 0.534,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "83e56d7b-76b6-4bb6-8a6c-1dd8ecdc1b5c",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.2392,
  "model_score": 0.8816,
  "style_score": 0.3576,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_FP08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "8c9bdd68-9324-4c66-a794-61a1d47abe43",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.0252,
  "model_score": 0.4625,
  "style_score": 0.5626,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "caccfe56-e99a-4452-87c4-c5257cad65b8",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.3906,
  "model_score": 0.2044,
  "style_score": 0.405,
  "label": "This reads like it was written by a person. Our check found the kind of variety (in sentence length and punctuation) that people's writing usually has.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "b36d7fd9-8cba-41b6-b3c7-03a2696012b3",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.0964,
  "model_score": 0.5943,
  "style_score": 0.502,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "d414a222-2d4d-41ed-be78-aed348df6912",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.1582,
  "model_score": 0.4998,
  "style_score": 0.342,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "f884fadb-3fef-4bc1-b1ea-928643ea75ec",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.0902,
  "model_score": 0.6401,
  "style_score": 0.45,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "d0530e75-da12-4363-a335-d2fa5c31d61e",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.1538,
  "model_score": 0.5583,
  "style_score": 0.5955,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "c232ae7d-6fbb-4618-809b-1baa61ea9fbc",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.5476,
  "model_score": 0.9976,
  "style_score": 0.55,
  "label": "We can't tell from the writing alone whether this was written by a person or with help from AI, and that's common: plain, clear writing often looks this way. This is not a finding that you used AI, and no action is taken because of it. If this doesn't match how you wrote it, you can ask a person to review it: send an appeal with your content ID and a few words about how you wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "f21660a5-5183-43b4-8943-c2a2fd1fc80a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4214,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "This reads like it was written by a person. Our check found the kind of variety (in sentence length and punctuation) that people's writing usually has.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "4a846b3d-dde0-4672-aa65-c2844091d222",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4214,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "This reads like it was written by a person. Our check found the kind of variety (in sentence length and punctuation) that people's writing usually has.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "b4c609c0-4c96-4bdf-b2e0-52233959457d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4214,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "This reads like it was written by a person. Our check found the kind of variety (in sentence length and punctuation) that people's writing usually has.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "fac281b1-28d5-41af-9ff4-373e458dcff4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4214,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "This reads like it was written by a person. Our check found the kind of variety (in sentence length and punctuation) that people's writing usually has.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "a73b5a28-de57-4353-b21d-5bda370ac327",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.4214,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "This reads like it was written by a person. Our check found the kind of variety (in sentence length and punctuation) that people's writing usually has.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
