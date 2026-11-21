#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be
given -- to /output/entry.txt. Deterministic: the same text, every run.
"""

from pathlib import Path

POEM = """You asked to hold the string.
I gave it \u2014 not the kite,
the wind it leaned against.

It pulled. You let it climb
till your arm ached. You reeled
it home and gave it back.

The kite was never yours.
The sky was never mine.
The string knew both our hands."""


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
