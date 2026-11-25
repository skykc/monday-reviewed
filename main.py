#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Entrypoint: writes the one-line review of my Monday to
/output/entry.txt (the path the grader reads), with no title and no
explanation, exactly as the competition requires.
"""

import os

LINE = "One star: Monday fixed my weekend by deleting it, then auto-renewed my 6 a.m. alarm for next week."

# The line is a product review of Monday itself: Monday "fixes" the
# reviewer's weekend by deleting it, and the kicker lands at the end,
# where the same Monday auto-renews the 6 a.m. alarm for next week.
# One clause of setup, one concrete detail (the 6 a.m. alarm), payoff
# last, 98 characters: inside the 1-200 gate and the 80-130 target band.


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    out = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(out, "w", encoding="utf-8") as f:
            f.write(LINE)
    print(out)
    print(LINE)


if __name__ == "__main__":
    main()
