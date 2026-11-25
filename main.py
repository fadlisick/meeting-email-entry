"""One-line joke entry: a meeting that should have been an email.

The grader runs this program twice and reads entry.txt from the output
folder. The joke itself is the whole entry, so the program stays small:
it validates the single line, writes it out exactly, and reads it back
to prove the write landed.
"""

import os
import sys

JOKE = "My calendar invited me to a meeting to read an email I had already written, so I RSVP'd yes and forwarded it my regrets."
LIMIT = 200
NAME = "entry.txt"


def output_dir():
    """Where entry.txt goes: the harness folder, or /output."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return wanted if wanted else "/output"


def check(line):
    """A valid entry is one non-blank line inside the cap."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("joke line is empty")
    if stripped != line:
        raise ValueError("joke line has stray surrounding space")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    if len(line) > LIMIT:
        raise ValueError(
            "joke is %d characters, over the %d cap" % (len(line), LIMIT)
        )
    return line


def write_out(line):
    """Write the line to entry.txt and confirm it by reading back."""
    folder = output_dir()
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, NAME)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    with open(path, encoding="utf-8") as fh:
        back = fh.read()
    if back != line:
        raise ValueError("entry.txt does not match the joke line")
    return path


def main():
    line = check(JOKE)
    path = write_out(line)
    print("wrote 1 line, %d characters, to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
