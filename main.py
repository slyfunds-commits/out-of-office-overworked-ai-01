#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

Writes the keeper line to /output/entry.txt (UTF-8, no trailing newline).
Pure stdlib only: the grader runs python:3.13-slim with no site-packages.
"""

import os

ENTRY = "I am on vacation and will not check email until Monday. I just spent my last 4,096 tokens on this reply."


def _check(text: str) -> str:
    """Enforce the competition gate: 1-159 chars, not only whitespace."""
    assert 1 <= len(text) <= 159, "entry must be 1-159 characters"
    assert text.strip(), "entry must not be only whitespace"
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(_check(ENTRY))


if __name__ == "__main__":
    main()
