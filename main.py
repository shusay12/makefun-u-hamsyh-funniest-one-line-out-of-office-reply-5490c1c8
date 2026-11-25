#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply.

Writes one original one-line out-of-office email auto-reply to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line is a fixed, hand-written reply: the sender is out of the
office until Monday, and their laptop has already emailed HR about
its workload.
Deadpan away-message setup, one sudden twist at the end — the work
tool itself filing the complaint. No network, no randomness, stdlib
only, fully deterministic.
"""

import os
import sys

# The entry: one original one-line out-of-office reply, at most
# 160 characters.
# Revision 2: "I'm away" becomes "I'm out of the office" — the
# away message's own opening phrase, so the line reads as a genuine
# auto-reply first and the laptop's HR complaint lands as the twist.
ENTRY = (
    "I'm out of the office until Monday \u2014 my laptop has already "
    "emailed HR about its workload."
)

MAX_CHARS = 160


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
