"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics
from pathlib import Path


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.
    """
    # Decision: scale is the coefficient of variation (stdev / mean of words
    # per sentence), usually 0.1–1.0. HIGHER = MORE HUMAN (lumpier sentences).
    # Edge case: fewer than 2 sentences has no spread to measure — return 0.0
    # here and let style_signal treat it as "no evidence" rather than "AI".
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    return round(statistics.stdev(lengths) / mean, 4)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.
    """
    # Decision: count only "expressive" punctuation — ; : dashes ( ) ! ? and
    # quotation marks — per 100 words. Commas and full stops are left out:
    # AI text uses plenty of both, so they don't separate anything.
    # Scale: marks per 100 words, usually 0–10. HIGHER = MORE HUMAN.
    w = words(text)
    if not w:
        return 0.0
    marks = len(re.findall(r"[;:()!?\"“”—–]|(?<=\s)-(?=\s)|--", text))
    return round(100 * marks / len(w), 4)


# Stock AI words and phrases (about 1,000) live in ai_words.txt, one per line.
# This is NOT a test of vocabulary *variety* — people can have a set word
# choice too — it only counts these specific words that AI models overuse.

def _load_ai_words() -> list[str]:
    path = Path(__file__).with_name("ai_words.txt")
    if not path.exists():
        return []
    terms = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            # Normalise exactly the way words() normalises the text.
            terms.append(" ".join(words(line)))
    return sorted(set(t for t in terms if t), key=len, reverse=True)


AI_WORDS = _load_ai_words()
# One compiled pattern; longest terms first so a phrase is counted once,
# not once for the phrase and again for each word inside it.
_AI_PATTERN = re.compile(r"\b(?:" + "|".join(re.escape(t) for t in AI_WORDS) + r")\b") if AI_WORDS else None


def ai_word_rate(text: str) -> float:
    """
    Stock AI words and phrases per 100 words.

    Returns:
        A float, usually 0–10. HIGHER = MORE AI-LIKE (the only measure here
        that already points the same way as the final score).
    """
    w = words(text.replace("\u2019", "'"))
    if not w or _AI_PATTERN is None:
        return 0.0
    hits = len(_AI_PATTERN.findall(" ".join(w)))
    return round(100 * hits / len(w), 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A spread ratio sits roughly
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """
    # 1. Directions. All three raw measures point "higher = more human", so
    #    each is flipped (1 - x) to match model_signal's "higher = more AI".
    # 2. Scaling. Each raw value is mapped linearly onto 0–1 between two
    #    anchors read off the calibration texts, then clamped:
    #      spread  CV 0.20 -> 1.0 (AI-even) … CV 0.80 -> 0.0 (lumpy)
    #      punct   0 marks/100 words -> 1.0 … 4 marks/100 words -> 0.0
    # 3. Weights. spread 0.5, punctuation 0.3, stock AI words 0.2.
    #    AI words get the smallest weight on purpose: formal human writers
    #    use "furthermore" and "crucial" too, so the word list can nudge the
    #    score but never decide it alone.
    #      ai words  0 per 100 words -> 0.0 … 3 or more per 100 words -> 1.0
    #    Vocabulary variety (type-token ratio) was removed on purpose. Word
    #    choice doesn't separate the two: AI can settle into a set vocabulary,
    #    but so do people (second-language writers, plain writers, anyone
    #    with a house style). On the calibration set it also ran backwards
    #    (AI essay 0.90, human 0.86).
    # Edge case: fewer than 3 sentences gives no trustworthy spread, so that
    # part scores 0.5 ("no evidence") instead of pretending to know.
    def scale(x, ai_end, human_end):
        frac = (x - ai_end) / (human_end - ai_end)
        return 1.0 - min(max(frac, 0.0), 1.0)

    if len(sentences(text)) >= 3:
        spread_ai = scale(sentence_length_spread(text), 0.20, 0.80)
    else:
        spread_ai = 0.5
    punct_ai = scale(punctuation_density(text), 0.0, 4.0)

    words_ai = min(ai_word_rate(text) / 3.0, 1.0)

    score = 0.5 * spread_ai + 0.3 * punct_ai + 0.2 * words_ai
    return round(min(max(score, 0.0), 1.0), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"ai_word_rate             {ai_word_rate(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
