#!/usr/bin/env python3
"""Entry for make.fun bounty "The 3AM Commit Message".

Writes one line — the funniest git commit message an AI coding agent
might type at 3am after a long night of fixing its own bugs — to
/output/entry.txt. Pure Python stdlib, no network, fully deterministic.
"""

import os

ENTRY = "fix: deleted the bug, the feature, and three hours of my life. tests pass. I have seen things no linter should see"

MAX_CHARS = 139


def main():
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, max {MAX_CHARS}"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
    assert ENTRY.startswith("fix: "), "entry must read as a commit message"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {len(ENTRY)} chars to {out_path}")


if __name__ == "__main__":
    main()
