"""Meeting-email joke entry: one line, written out as entry.txt.

The grader runs this program twice and reads the file it leaves in the
output folder. The joke is the whole entry, so the program does one
job only: check the single line against the cap, write it exactly,
then read it back to confirm the write.
"""

import os
import sys

LINE = "The email got promoted to a meeting, then demoted back to an email, and the email still had to attend the meeting about itself."
MAX_CHARS = 200
OUT_NAME = "entry.txt"


def target_folder():
    """The harness folder when set, otherwise /output."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if folder:
        return folder
    return "/output"


def validate(line):
    """One non-blank line, inside the character cap, nothing else."""
    if not line.strip():
        raise ValueError("joke line is blank")
    if line.strip() != line:
        raise ValueError("joke line has stray surrounding space")
    if "\n" in line or "\r" in line:
        raise ValueError("joke line must stay on one line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "joke line is %d characters, over the %d cap"
            % (len(line), MAX_CHARS)
        )
    return line


def save(line):
    """Write entry.txt, then read it back and compare."""
    folder = target_folder()
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, OUT_NAME)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(path, encoding="utf-8") as handle:
        stored = handle.read()
    if stored != line:
        raise ValueError("entry.txt does not match the joke line")
    return path


def run():
    line = validate(LINE)
    path = save(line)
    print("wrote 1 line, %d characters, to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(run())
