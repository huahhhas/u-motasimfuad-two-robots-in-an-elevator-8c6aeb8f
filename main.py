"""Two Robots in an Elevator — make.fun entry.

Writes one funny line of awkward robot elevator small talk to entry.txt.

The line is a single line of 1-200 characters, validated before writing,
so the sealed gate (UTF-8 text, 1-200 chars, not only whitespace) passes.
"""

import os

ENTRY = "So\u2026 do you also stare at the floor numbers to avoid eye contact, or is your camera just buffering too?"


def validate(line):
    """Check the entry line against the competition gate."""
    assert isinstance(line, str), "entry must be text"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters, got %d" % len(line)
    assert line.strip(), "entry must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    return line


def write_line(line, out_path):
    """Write one validated line (plus trailing newline) to out_path."""
    validate(line)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    write_line(ENTRY, out)


if __name__ == "__main__":
    main()
