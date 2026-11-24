"""The Worst App Idea Ever Pitched.

Writes one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt: a pitch for
the worst, most useless app imaginable — an app that notifies you to
check the notification you just received.
Standard library only.
"""

import os

PITCH = (
    "Ping is the app that notifies you to check the notification you "
    "just received, so you never miss an alert about an alert."
)


def check_pitch(text):
    """Check the pitch against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 240 characters, not only white
    space, in a single sentence: one pitch for the worst, most useless
    app imaginable. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("pitch must not be only whitespace")
    if len(cleaned) > 240:
        raise ValueError("pitch is %d characters, over the 240 limit" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("pitch must be exactly one sentence")
    if cleaned.count(".") != 1 or not cleaned.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_pitch(PITCH)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
