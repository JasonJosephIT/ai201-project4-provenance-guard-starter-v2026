"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
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


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    # Decision: moving-average type-token ratio (MATTR) over 50-word windows,
    # because plain TTR falls as text gets longer and would make length look
    # like a signal. Texts under 50 words fall back to plain TTR.
    # Scale 0–1. HIGHER = MORE HUMAN (more varied vocabulary).
    w = words(text)
    if not w:
        return 0.0
    window = 50
    if len(w) <= window:
        return round(len(set(w)) / len(w), 4)
    ratios = [len(set(w[i:i + window])) / window for i in range(len(w) - window + 1)]
    return round(statistics.mean(ratios), 4)


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
      2. How to get each onto a comparable scale. A raw type-token ratio sits
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
    # 3. Weights. spread 0.6, punctuation 0.4, type-token ratio 0.0.
    #    TTR is computed and printed but NOT used: on the calibration set it
    #    ran backwards (the AI essay scored 0.90, the human one 0.86), and a
    #    low TTR would push plain human writing toward "AI" — the exact false
    #    positive this service must avoid.
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

    score = 0.6 * spread_ai + 0.4 * punct_ai
    return round(min(max(score, 0.0), 1.0), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
