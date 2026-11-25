#!/usr/bin/env python3
"""Write one short family scene to /output/entry.txt.

Deterministic, stdlib only, no network. Writes a single scene
(one line, 1-280 characters) and nothing else.
"""

import os

SCENE = (
    "Mum ate the blackest toast without a flinch — Dad had burnt a "
    "lopsided heart into it again — then kissed his cheek and said, "
    "'Twenty years, love, and you still cook like a romantic arsonist.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(SCENE)


if __name__ == "__main__":
    main()
