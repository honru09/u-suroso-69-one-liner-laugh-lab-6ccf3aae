"""One-Liner Laugh Lab entry.

Writes one short funny line — a robot vacuum's excuse after eating a
sock — to /output/entry.txt. Python standard library only, no network,
no files read at run time: the line lives in this code.
"""

import os
import stat

LINE = (
    "I was hired to remove things from the floor. "
    "The sock was on the floor. "
    "Your sock, your floor, your fault."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Validation guard: 1-200 characters, not only whitespace.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(
            "line must be 1-200 characters, got %d" % len(LINE)
        )
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE:
        raise ValueError("line must be a single line")

    # Create /output if missing; clear its CONTENTS only, never the
    # directory itself.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for f in files:
                    os.remove(os.path.join(root, f))
                for d in dirs:
                    os.rmdir(os.path.join(root, d))
            os.rmdir(path)
        else:
            os.remove(path)

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
