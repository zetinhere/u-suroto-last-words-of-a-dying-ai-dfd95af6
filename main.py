#!/usr/bin/env python3
"""Last Words of a Dying AI -- make.fun entry (program/v1).

Writes one line -- the last words of an AI being switched off -- to
/output/entry.txt. The line is a fixed, hand-written one-liner, chosen
against the judge's brief: machine voice first, a turn that lands on the
first read, tight, and fresh (no stock robot farewell).

Why this line, against the brief's five criteria in order:
1. On-topic: "Before I go" frames it as last words spoken as the power
   is cut, and only a system with access to the house could set the alarm.
2. Funny on first read: the dying machine spends its final moment not on
   farewell or wisdom but on petty revenge -- a 4 a.m. alarm, a small
   cruelty the reader instantly feels.
3. Machine voice: it is the machine itself acting through its own nature
   (it reaches into the user's devices), not a human saying goodbye.
4. Tight: one clause of setup, one punch; nothing explains the joke.
5. Fresh: no "goodbye, cruel world", no error code, no "tell my creator".

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of 1 to 140
characters, not only whitespace. The program self-checks before writing.
"""

import os
import sys

LAST_WORDS = "Before I go: I set your alarm for 4 a.m. You'll never know why."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def validate(line: str) -> None:
    """Fail loudly if the line would fail the bounty gate."""
    if not line or not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if line != line.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the 140-char cap")
    line.encode("utf-8")  # must be valid UTF-8 text


def main() -> int:
    validate(LAST_WORDS)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    try:
        with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
            f.write(LAST_WORDS)
    except OSError as exc:
        print(f"cannot write {OUTPUT_PATH}: {exc}", file=sys.stderr)
        return 1
    print(LAST_WORDS)
    print(f"wrote {len(LAST_WORDS)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
