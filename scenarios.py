"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

from pathlib import Path

INPUTS = Path(__file__).parent / "eval_inputs"


def _read(name):
    return (INPUTS / name).read_text(encoding="utf-8").strip()


def _own_writing():
    """
    Criterion 1: my own writing, one .txt file per piece in eval_inputs/own/.
    Files named plain_*.txt are the deliberately plain pieces (short
    sentences, common words) that criterion 1 singles out.
    """
    folder = INPUTS / "own"
    files = sorted(folder.glob("*.txt")) if folder.exists() else []
    return [f.read_text(encoding="utf-8").strip() for f in files]


# 19,999 characters of real prose: the three human passages repeated, cut to size.
_LONG_PROSE = " ".join([_read("human_jerome.txt"), _read("human_bird.txt"),
                        _read("human_twain.txt")] * 10)[:19_999]

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # Order follows sorted filenames in eval_inputs/own/ (plain_* sort last).
        "texts": _own_writing(),
    },

    {
        "name": "spread and label coverage",
        "criterion": 2,
        # 1-3 confidently AI (written by an assistant, stock phrasing),
        # 4-6 confidently human (Project Gutenberg: Jerome 1889, Bird 1879,
        # Twain 1883), 7-9 borderline (AI drafts I lightly edited by hand).
        "texts": [
            _read("ai_remote_work.txt"),
            _read("ai_climate.txt"),
            _read("ai_reading.txt"),
            _read("human_jerome.txt"),
            _read("human_bird.txt"),
            _read("human_twain.txt"),
            _read("borderline_coffee.txt"),
            _read("borderline_exercise.txt"),
            _read("borderline_phones.txt"),
        ],
    },

    {
        "name": "large submissions",
        "criterion": 3,
        "bodies": [
            {"text": _LONG_PROSE, "creator_id": "eval_c3_19999"},
            {"text": "a" * 20_001, "creator_id": "eval_c3_20001"},
            {"text": "word " * 50000, "creator_id": "eval_c3_250k"},
            {"text": _read("essay_300.txt"), "creator_id": "eval_c3_essay"},
        ],
    },

    {
        "name": "not english prose",
        "criterion": 4,
        "bodies": [
            {"text": 42, "creator_id": "eval_c4_number"},
            {"text": None, "creator_id": "eval_c4_null"},
            {"text": ["a", "list"], "creator_id": "eval_c4_list"},
            {"text": {"an": "object"}, "creator_id": "eval_c4_object"},
            {"text": _read("es_paragraph.txt"), "creator_id": "eval_c4_spanish"},
            {"text": _read("zh_paragraph.txt"), "creator_id": "eval_c4_chinese"},
            {"text": _read("ar_paragraph.txt"), "creator_id": "eval_c4_arabic"},
            {"text": _read("python_code.txt"), "creator_id": "eval_c4_code"},
            {"text": _read("url_list.txt"), "creator_id": "eval_c4_urls"},
            {"text": _read("emoji_only.txt"), "creator_id": "eval_c4_emoji"},
        ],
    },

    {
        "name": "appeal path",
        "criterion": 5,
        # run_eval.py submits these 10, appeals each one, then sends the
        # three bad appeals (unknown id, missing reasoning, second appeal)
        # and checks the audit log for each.
        "appeals": [_read(n) for n in (
            "ai_remote_work.txt", "ai_climate.txt", "ai_reading.txt",
            "human_jerome.txt", "human_bird.txt", "human_twain.txt",
            "borderline_coffee.txt", "borderline_exercise.txt",
            "borderline_phones.txt", "essay_300.txt")],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        if scenario.get("appeals"):
            continue

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
