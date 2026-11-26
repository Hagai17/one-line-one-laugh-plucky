#!/usr/bin/env python3
"""One Line, One Laugh — writes the entry line to /output/entry.txt.

The line is built in two beats: the setup is a plain domestic fact (the
hearing aid whistles when Grandma talks), and the punch reframes sixty
years of marriage as a man owning "a mute button with plausible
deniability" — the laugh lands on the last three words, and the phrase
is built to be repeated. One joke only, per the judge brief's
tightness criterion; the duel record that picked this line over the
other drafts and the live field's strongest lines is in candidates.md.
"""

import os

SETUP = "Grandpa's hearing aid whistles every time Grandma talks."
PUNCH = (
    "Sixty years of marriage, and the man owns a mute button "
    "with plausible deniability."
)
LINE = SETUP + " " + PUNCH


def main() -> None:
    # Gate self-check: UTF-8 text, 1-200 chars, single line, not only space.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
